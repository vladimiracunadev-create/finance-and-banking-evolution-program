"""Iniciacion de pagos con idempotencia y maquina de estados.

Implementa los cuatro detalles de la Parte 17, clase 8 que la mayoria de las
implementaciones omite:

1. canonicalizacion del cuerpo antes de calcular la huella;
2. bloqueo por clave, sin el cual la idempotencia falla justo en el caso para el
   que existe;
3. se guarda la RESPUESTA completa, no solo el identificador;
4. ventana de retencion declarada.

Y la distincion de la clase 10: aceptado no es liquidado. El comercio entrega
con firmeza, no con aceptacion.
"""

from __future__ import annotations

import hashlib
import json
import threading
from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal

from ..bank_api import ApiError

IDEMPOTENCY_WINDOW_HOURS = 24

TRANSITIONS = {
    "recibido": {"autorizado", "rechazado"},
    "autorizado": {"aceptado", "rechazado"},
    "aceptado": {"en_ejecucion", "rechazado"},
    "en_ejecucion": {"liquidado", "rechazado"},
    "liquidado": {"devuelto"},
    "rechazado": set(),
    "devuelto": set(),
}

FINAL_STATES = {"rechazado", "devuelto"}
FIRM_STATES = {"liquidado"}


def canonical(payload: dict) -> str:
    """Serializacion canonica: {"a":1,"b":2} y {"b":2,"a":1} son el mismo cuerpo."""
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def fingerprint(payload: dict) -> str:
    return hashlib.sha256(canonical(payload).encode("utf-8")).hexdigest()


@dataclass
class Payment:
    payment_id: str
    consent_id: str
    amount: str
    currency: str
    creditor: str
    debtor_account: str
    status: str = "recibido"
    history: list[str] = field(default_factory=lambda: ["recibido"])

    def to_dict(self) -> dict:
        return {
            "payment_id": self.payment_id,
            "status": self.status,
            "amount": self.amount,
            "currency": self.currency,
            "creditor": self.creditor,
            # El estado real, no un booleano: un «ok» que agrupa aceptado y
            # liquidado hace que el comercio entregue antes de cobrar.
            "is_final": self.status in FINAL_STATES,
            "is_firm": self.status in FIRM_STATES,
        }


class PaymentInitiation:
    def __init__(self, auth) -> None:
        self.auth = auth
        self._payments: dict[str, Payment] = {}
        self._idempotency: dict[str, tuple[str, dict, datetime]] = {}
        self._locks: dict[str, threading.Lock] = {}
        self._global = threading.Lock()
        self._funds_checks: dict[str, list[Decimal]] = {}
        self._counter = 0

    def _lock_for(self, key: str) -> threading.Lock:
        with self._global:
            return self._locks.setdefault(key, threading.Lock())

    def create(self, token_value: str, idempotency_key: str | None, body: dict) -> dict:
        token = self.auth.check(token_value, "payments:initiate")
        if not idempotency_key:
            raise ApiError("invalid_request", "Idempotency-Key obligatoria")

        for campo in ("amount", "currency", "creditor", "debtor_account"):
            if campo not in body:
                raise ApiError("invalid_request", f"falta el campo {campo}")

        huella = fingerprint(body)
        with self._lock_for(idempotency_key):
            registro = self._idempotency.get(idempotency_key)
            if registro is not None:
                guardada, respuesta, _ = registro
                if guardada != huella:
                    raise ApiError("idempotency_conflict", "misma clave, cuerpo distinto")
                return respuesta

            self._counter += 1
            payment = Payment(
                payment_id=f"pay_{self._counter:06d}",
                consent_id=token.consent_id,
                amount=body["amount"],
                currency=body["currency"],
                creditor=body["creditor"],
                debtor_account=body["debtor_account"],
            )
            self._payments[payment.payment_id] = payment
            respuesta = payment.to_dict()
            self._idempotency[idempotency_key] = (
                huella,
                respuesta,
                datetime.now(timezone.utc),
            )
            return respuesta

    def advance(self, payment_id: str, target: str) -> dict:
        payment = self._payments.get(payment_id)
        if payment is None:
            raise ApiError("resource_forbidden", "no tienes acceso a ese recurso")
        if target not in TRANSITIONS[payment.status]:
            raise ApiError(
                "invalid_request", f"transicion ilegal: {payment.status} -> {target}"
            )
        payment.status = target
        payment.history.append(target)
        # `to_dict` recalcula is_final/is_firm, de modo que la respuesta guardada
        # por idempotencia queda deliberadamente congelada en su momento.
        return payment.to_dict()

    def get(self, payment_id: str) -> dict:
        payment = self._payments.get(payment_id)
        if payment is None:
            raise ApiError("resource_forbidden", "no tienes acceso a ese recurso")
        return payment.to_dict()

    def confirm_funds(self, token_value: str, account_id: str, amount: str) -> dict:
        """Confirmacion de fondos: booleano, sin retencion y con limite propio.

        Los tres controles de la clase 10 juntos. Sin el limite por
        consentimiento, repetir la consulta con importes decrecientes deduce el
        saldo por biseccion en unas veinte llamadas.
        """
        token = self.auth.check(token_value, "payments:initiate")
        historial = self._funds_checks.setdefault(token.consent_id, [])
        historial.append(Decimal(amount))
        if len(historial) > 3:
            raise ApiError("rate_limited", "demasiadas confirmaciones para este consentimiento")
        # Patron de biseccion: importes estrictamente decrecientes.
        if len(historial) >= 3 and all(
            historial[i] > historial[i + 1] for i in range(len(historial) - 1)
        ):
            raise ApiError("rate_limited", "patron de sondeo detectado")
        return {"funds_available": True}
