"""API de informacion de cuentas del entorno simulado.

Implementa las tres decisiones de diseno de la Parte 17, clases 3 y 8:

1. importes como cadena decimal con la moneda aparte (nunca coma flotante);
2. paginacion por cursor sobre un orden TOTAL (fecha, id), no por desplazamiento;
3. respuesta identica para «cuenta inexistente» y «cuenta ajena», para que la
   diferencia entre ambas no permita enumerar cuentas.
"""

from __future__ import annotations

import base64
import json
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
MAX_LIMIT = 100

# Catalogo cerrado de errores. Un llamante solo puede programar decisiones si
# el conjunto de errores es conocido y estable.
ERRORS = {
    "invalid_request": 400,
    "invalid_token": 401,
    "consent_revoked": 403,
    "resource_forbidden": 403,
    "idempotency_conflict": 409,
    "rate_limited": 429,
    "provider_unavailable": 503,
}


class ApiError(Exception):
    def __init__(self, code: str, message: str = "") -> None:
        super().__init__(f"{code}: {message}" if message else code)
        self.code = code
        self.status = ERRORS.get(code, 400)
        self.message = message


@dataclass(frozen=True)
class Account:
    account_id: str
    customer_ref: str
    kind: str
    currency: str
    opened_at: str


def _load(name: str) -> list[dict]:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def encode_cursor(booking_date: str, transaction_id: str) -> str:
    """Cursor opaco. Si el llamante lo interpreta, el formato queda congelado."""
    raw = f"{booking_date}|{transaction_id}".encode("utf-8")
    return base64.urlsafe_b64encode(raw).decode("ascii").rstrip("=")


def decode_cursor(cursor: str) -> tuple[str, str]:
    try:
        padding = "=" * (-len(cursor) % 4)
        raw = base64.urlsafe_b64decode(cursor + padding).decode("utf-8")
        booking_date, transaction_id = raw.split("|", 1)
        return booking_date, transaction_id
    except Exception as exc:  # noqa: BLE001 - se traduce a error del catalogo
        raise ApiError("invalid_request", "cursor invalido") from exc


class BankApi:
    def __init__(self, auth) -> None:
        self.auth = auth
        self._accounts = [Account(**a) for a in _load("accounts.json")]
        self._transactions = _load("transactions.json")
        self._opening = _load("opening_balances.json")

    # ------------------------------------------------------------------ helpers

    def _consent_accounts(self, token) -> list[Account]:
        consent = self.auth.consents.get(token.consent_id)
        return [a for a in self._accounts if a.customer_ref == consent.customer_ref]

    def _account_or_forbidden(self, token, account_id: str) -> Account:
        """Una cuenta ajena y una inexistente devuelven EXACTAMENTE lo mismo.

        Si difirieran, un llamante recorreria el espacio de identificadores y
        deduciria cuales existen comparando las dos respuestas.
        """
        for account in self._consent_accounts(token):
            if account.account_id == account_id:
                return account
        raise ApiError("resource_forbidden", "no tienes acceso a ese recurso")

    # ------------------------------------------------------------------ recursos

    def accounts(self, token_value: str) -> dict:
        token = self.auth.check(token_value, "accounts:list")
        return {
            "data": [
                {
                    "account_id": a.account_id,
                    "kind": a.kind,
                    "currency": a.currency,
                    "opened_at": a.opened_at,
                }
                for a in self._consent_accounts(token)
            ]
        }

    def balances(self, token_value: str, account_id: str) -> dict:
        token = self.auth.check(token_value, "accounts:balances")
        account = self._account_or_forbidden(token, account_id)
        movimientos = [t for t in self._transactions if t["account_id"] == account_id]
        # El saldo se reconstruye desde el saldo inicial de la ventana mas los
        # movimientos. Exponer «saldo al inicio de la ventana» es lo que permite
        # al tercero cuadrar la respuesta consigo misma (clase 4).
        inicial = Decimal(self._opening.get(account_id, "0.00"))
        contable = inicial + sum(Decimal(t["amount"]) for t in movimientos)
        return {
            "data": {
                "account_id": account.account_id,
                "currency": account.currency,
                "opening_balance": f"{inicial:.2f}",
                "booked_balance": f"{contable:.2f}",
                "available_balance": f"{contable:.2f}",
                "window_months": 24,
            }
        }

    def transactions(
        self,
        token_value: str,
        account_id: str,
        limit: int = 50,
        cursor: str | None = None,
    ) -> dict:
        token = self.auth.check(token_value, "accounts:transactions")
        self._account_or_forbidden(token, account_id)
        if limit < 1:
            raise ApiError("invalid_request", "limit debe ser positivo")
        limit = min(limit, MAX_LIMIT)

        # Orden TOTAL: el desempate por identificador es lo que hace la posicion
        # inequivoca cuando dos movimientos comparten fecha.
        filas = sorted(
            (t for t in self._transactions if t["account_id"] == account_id),
            key=lambda t: (t["booking_date"], t["transaction_id"]),
            reverse=True,
        )
        if cursor:
            fecha, ident = decode_cursor(cursor)
            filas = [t for t in filas
                     if (t["booking_date"], t["transaction_id"]) < (fecha, ident)]

        pagina = filas[:limit]
        siguiente = None
        if len(filas) > limit:
            ultimo = pagina[-1]
            siguiente = encode_cursor(ultimo["booking_date"], ultimo["transaction_id"])

        return {
            "data": [
                {
                    "transaction_id": t["transaction_id"],
                    "booking_date": t["booking_date"],
                    "amount": t["amount"],
                    "currency": t["currency"],
                    "category": t["category"],
                }
                for t in pagina
            ],
            "meta": {"count": len(pagina)},
            "links": {"next": siguiente},
        }
