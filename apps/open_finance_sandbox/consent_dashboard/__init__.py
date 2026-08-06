"""Modelo de consentimiento y panel de revocacion.

Implementa lo que la Parte 17, clase 5 exige de un consentimiento: alcance por
finalidad, plazo absoluto, evidencia que reconstruye el acto y revocacion con
efecto inmediato.

La decision de diseno central es que la revocacion invalida los tokens vivos
ANTES de responder. Un panel que informa «revocado» mientras la API sigue
autorizando es peor que no tener panel: crea una expectativa que el sistema
incumple.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone

# Alcances del entorno. Uno por finalidad: agrupar dos finalidades en un alcance
# impide que el cliente acepte una y rechace la otra.
SCOPES = {
    "accounts:list": "Ver que cuentas tienes y de que tipo son",
    "accounts:balances": "Ver cuanto dinero hay en cada cuenta",
    "accounts:transactions": "Ver tus movimientos de los ultimos 12 meses",
    "payments:initiate": "Ordenar pagos desde tu cuenta, uno por uno",
}

# borrador es el unico estado desde el que se puede autorizar; ningun estado
# final vuelve a vigente. La renovacion crea un consentimiento NUEVO.
TRANSITIONS = {
    "borrador": {"vigente", "rechazado"},
    "vigente": {"revocado", "expirado", "terminado"},
    "revocado": set(),
    "expirado": set(),
    "rechazado": set(),
    "terminado": set(),
}

FINAL_STATES = {"revocado", "expirado", "rechazado", "terminado"}


class ConsentError(Exception):
    """Error de dominio del consentimiento."""


@dataclass
class Consent:
    """Un consentimiento con las cuatro coordenadas y su evidencia.

    Las cuatro coordenadas de la clase 5 son quien (provider_id), que (scopes),
    para que (purpose) y hasta cuando (expires_at). La quinta pieza, que no es
    del consentimiento sino de su prueba, es notice_version.
    """

    consent_id: str
    customer_ref: str
    provider_id: str
    scopes: tuple[str, ...]
    purpose: str
    created_at: datetime
    expires_at: datetime
    notice_version: str
    presented_scopes: tuple[str, ...]
    status: str = "borrador"
    revoked_at: datetime | None = None
    revoked_by: str | None = None
    reason: str | None = None
    evidence: dict[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        unknown = [s for s in self.scopes if s not in SCOPES]
        if unknown:
            raise ConsentError(f"alcances desconocidos: {unknown}")
        if not self.purpose.strip():
            raise ConsentError("la finalidad no puede estar vacia")
        if self.expires_at <= self.created_at:
            raise ConsentError("expires_at debe ser posterior a created_at")
        # Un alcance concedido que nunca se presento al cliente es una escalada
        # silenciosa: por eso se guardan los dos conjuntos y se comparan.
        concedido_no_presentado = set(self.scopes) - set(self.presented_scopes)
        if concedido_no_presentado:
            raise ConsentError(
                f"alcances concedidos sin presentar: {sorted(concedido_no_presentado)}"
            )

    def is_active(self, now: datetime | None = None) -> bool:
        now = now or datetime.now(timezone.utc)
        return self.status == "vigente" and now < self.expires_at

    def allows(self, scope: str, now: datetime | None = None) -> bool:
        return self.is_active(now) and scope in self.scopes

    def explain(self) -> list[str]:
        """Traduce los alcances a lenguaje de consecuencia para el cliente."""
        return [SCOPES[s] for s in self.scopes]


class ConsentStore:
    """Almacen de consentimientos con transiciones verificadas.

    `on_revoke` recibe el identificador del consentimiento revocado y es donde
    el servidor de autorizacion engancha la invalidacion de tokens. Se invoca
    ANTES de que `revoke` retorne, para que no exista una ventana en la que el
    panel ya respondio y la API todavia autoriza.
    """

    def __init__(self) -> None:
        self._items: dict[str, Consent] = {}
        self._callbacks: list = []

    def on_revoke(self, callback) -> None:
        self._callbacks.append(callback)

    def create(
        self,
        consent_id: str,
        customer_ref: str,
        provider_id: str,
        scopes: list[str],
        purpose: str,
        notice_version: str,
        presented_scopes: list[str] | None = None,
        months: int = 12,
        now: datetime | None = None,
    ) -> Consent:
        now = now or datetime.now(timezone.utc)
        if consent_id in self._items:
            raise ConsentError(f"consentimiento duplicado: {consent_id}")
        consent = Consent(
            consent_id=consent_id,
            customer_ref=customer_ref,
            provider_id=provider_id,
            scopes=tuple(scopes),
            purpose=purpose,
            created_at=now,
            # Plazo ABSOLUTO, no relativo: un plazo relativo se recalcula mal.
            expires_at=now + timedelta(days=30 * months),
            notice_version=notice_version,
            presented_scopes=tuple(presented_scopes or scopes),
        )
        self._items[consent_id] = consent
        return consent

    def transition(self, consent_id: str, target: str, **extra) -> Consent:
        consent = self.get(consent_id)
        if target not in TRANSITIONS[consent.status]:
            raise ConsentError(
                f"transicion ilegal: {consent.status} -> {target}"
            )
        consent.status = target
        for key, value in extra.items():
            setattr(consent, key, value)
        return consent

    def authorize(self, consent_id: str, auth_method: str, channel: str) -> Consent:
        consent = self.transition(consent_id, "vigente")
        consent.evidence = {
            "auth_method": auth_method,
            "channel": channel,
            "authorized_at": datetime.now(timezone.utc).isoformat(),
            "notice_version": consent.notice_version,
            "presented_scopes": ",".join(consent.presented_scopes),
            "granted_scopes": ",".join(consent.scopes),
        }
        return consent

    def revoke(self, consent_id: str, actor: str, reason: str) -> Consent:
        consent = self.transition(
            consent_id,
            "revocado",
            revoked_at=datetime.now(timezone.utc),
            revoked_by=actor,
            reason=reason,
        )
        # El orden importa: se invalida antes de retornar.
        for callback in self._callbacks:
            callback(consent_id)
        return consent

    def get(self, consent_id: str) -> Consent:
        if consent_id not in self._items:
            raise ConsentError(f"consentimiento inexistente: {consent_id}")
        return self._items[consent_id]

    def for_customer(self, customer_ref: str) -> list[Consent]:
        """Todos los consentimientos, incluidos los terminados.

        El historico no se borra: es la prueba que protege a las dos partes.
        """
        return [c for c in self._items.values() if c.customer_ref == customer_ref]


def evidence_digest(consent: Consent) -> str:
    """Huella estable de la evidencia, para detectar alteraciones posteriores."""
    payload = json.dumps(consent.evidence, sort_keys=True, ensure_ascii=True)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()
