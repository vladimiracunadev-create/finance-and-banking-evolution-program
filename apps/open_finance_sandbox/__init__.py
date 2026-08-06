"""Entorno simulado de finanzas abiertas de la Parte 17.

Reune las piezas del ecosistema en un solo objeto para que los laboratorios y
las pruebas puedan montar el flujo completo en tres lineas:

    sandbox = build()
    concesion = sandbox.grant(["accounts:balances"])
    sandbox.bank.balances(concesion.access_token, "acc_0100")

No hay red, no hay credenciales reales y todos los datos son sinteticos.
"""

from __future__ import annotations

import secrets
from dataclasses import dataclass

from .authorization_server import AuthorizationServer, Client, s256
from .bank_api import ApiError, BankApi
from .consent_dashboard import ConsentStore
from .payment_initiation import PaymentInitiation

CLIENT_ID = "tpp_cuentas_claras"
REDIRECT_URI = "https://app.cuentasclaras.cl/callback"


@dataclass(frozen=True)
class Grant:
    consent_id: str
    access_token: str
    scopes: tuple[str, ...]


class Sandbox:
    def __init__(self) -> None:
        self.consents = ConsentStore()
        self.auth = AuthorizationServer(self.consents)
        self.auth.register(
            Client(
                client_id=CLIENT_ID,
                redirect_uris=frozenset({REDIRECT_URI}),
                allowed_scopes=frozenset(
                    {
                        "accounts:list",
                        "accounts:balances",
                        "accounts:transactions",
                        "payments:initiate",
                    }
                ),
            )
        )
        self.bank = BankApi(self.auth)
        self.payments = PaymentInitiation(self.auth)
        self._seq = 0

    def grant(
        self,
        scopes: list[str],
        customer_ref: str = "cus_synthetic_0001",
        purpose: str = "panel de posicion consolidada",
    ) -> Grant:
        """Recorre el flujo completo: consentimiento, authorize y token."""
        self._seq += 1
        consent_id = f"cns_{self._seq:05d}"
        self.consents.create(
            consent_id=consent_id,
            customer_ref=customer_ref,
            provider_id=CLIENT_ID,
            scopes=scopes,
            purpose=purpose,
            notice_version="consent-notice-v3",
        )
        self.consents.authorize(consent_id, auth_method="sca-otp", channel="web")

        verifier = secrets.token_urlsafe(48)
        respuesta = self.auth.authorize(
            client_id=CLIENT_ID,
            redirect_uri=REDIRECT_URI,
            scope=" ".join(scopes),
            state=secrets.token_urlsafe(16),
            code_challenge=s256(verifier),
            code_challenge_method="S256",
            consent_id=consent_id,
        )
        token = self.auth.token(
            client_id=CLIENT_ID, code=respuesta["code"], code_verifier=verifier
        )
        return Grant(
            consent_id=consent_id,
            access_token=str(token["access_token"]),
            scopes=tuple(str(token["scope"]).split()),
        )


def build() -> Sandbox:
    return Sandbox()


__all__ = [
    "ApiError",
    "AuthorizationServer",
    "BankApi",
    "Client",
    "ConsentStore",
    "Grant",
    "PaymentInitiation",
    "Sandbox",
    "build",
    "s256",
]
