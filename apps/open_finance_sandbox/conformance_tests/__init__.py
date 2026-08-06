"""Bateria de conformidad del entorno de finanzas abiertas.

Cuatro familias, con casos NEGATIVOS: autorizacion, contrato, seguridad y
resiliencia. Una bateria que solo prueba el camino feliz no dice nada, porque
del camino feliz depende que la demostracion funcione, no que el sistema sea
integrable.

El informe incluye siempre la seccion de limitaciones: un informe sin ella se
lee como cobertura completa, y esa lectura es la que produce incidentes.
"""

from __future__ import annotations

import secrets
from dataclasses import dataclass

from .. import CLIENT_ID, REDIRECT_URI, build
from ..authorization_server import AuthError, s256
from ..bank_api import ApiError

LIMITACIONES = (
    "TLS y autenticacion mutua: el entorno los simula, no los prueba",
    "certificados de una autoridad real: fuera de alcance",
    "carga sostenida: solo se ejecuta una rafaga corta",
    "comportamiento bajo particion de red: no se prueba",
    "datos sinteticos: no cubren distribuciones reales de volumen",
)


@dataclass(frozen=True)
class Case:
    family: str
    name: str
    passed: bool
    detail: str


def _expect(family: str, name: str, fn, expected_code: str) -> Case:
    """Ejecuta un caso que DEBE fallar con un codigo concreto del catalogo."""
    try:
        fn()
    except (AuthError, ApiError) as exc:
        ok = exc.code == expected_code
        return Case(family, name, ok, f"esperado {expected_code}, obtenido {exc.code}")
    return Case(family, name, False, f"esperado {expected_code}, no fallo")


def run() -> list[Case]:
    cases: list[Case] = []

    # ------------------------------------------------------------ autorizacion
    sandbox = build()
    consent = sandbox.grant(["accounts:balances"])
    verifier = secrets.token_urlsafe(48)

    def sin_pkce():
        sandbox.auth.authorize(
            client_id=CLIENT_ID, redirect_uri=REDIRECT_URI,
            scope="accounts:balances", state="x", code_challenge=None,
            code_challenge_method=None, consent_id=consent.consent_id,
        )

    def redirect_con_sufijo():
        sandbox.auth.authorize(
            client_id=CLIENT_ID,
            redirect_uri="https://app.cuentasclaras.cl.atacante.io/callback",
            scope="accounts:balances", state="x", code_challenge=s256(verifier),
            code_challenge_method="S256", consent_id=consent.consent_id,
        )

    def codigo_reusado():
        r = sandbox.auth.authorize(
            client_id=CLIENT_ID, redirect_uri=REDIRECT_URI,
            scope="accounts:balances", state="x", code_challenge=s256(verifier),
            code_challenge_method="S256", consent_id=consent.consent_id,
        )
        sandbox.auth.token(CLIENT_ID, r["code"], verifier)
        sandbox.auth.token(CLIENT_ID, r["code"], verifier)

    def fuera_de_alcance():
        sandbox.bank.transactions(consent.access_token, "acc_0100")

    cases += [
        _expect("autorizacion", "A1 sin code_challenge", sin_pkce, "invalid_request"),
        _expect("autorizacion", "A2 redirect_uri con sufijo", redirect_con_sufijo,
                "invalid_request"),
        _expect("autorizacion", "A3 codigo reusado", codigo_reusado, "invalid_grant"),
        _expect("autorizacion", "A4 alcance no concedido", fuera_de_alcance,
                "resource_forbidden"),
    ]

    # ----------------------------------------------------------------- contrato
    full = sandbox.grant(
        [
            "accounts:list",
            "accounts:balances",
            "accounts:transactions",
            "payments:initiate",
        ]
    )
    pagina = sandbox.bank.transactions(full.access_token, "acc_0100", limit=100000)
    cases.append(
        Case("contrato", "C1 limit acotado al maximo",
             pagina["meta"]["count"] <= 100, f"count={pagina['meta']['count']}")
    )
    cases.append(
        _expect("contrato", "C2 cursor manipulado",
                lambda: sandbox.bank.transactions(full.access_token, "acc_0100",
                                                  cursor="no-es-un-cursor!!"),
                "invalid_request")
    )
    cases.append(
        _expect("contrato", "C3 limit no positivo",
                lambda: sandbox.bank.transactions(full.access_token, "acc_0100", limit=0),
                "invalid_request")
    )
    cases.append(
        _expect("contrato", "C4 campo obligatorio ausente en el pago",
                lambda: sandbox.payments.create(full.access_token, "k1",
                                                {"amount": "1000.00"}),
                "invalid_request")
    )

    # ---------------------------------------------------------------- seguridad
    cases.append(
        _expect("seguridad", "S1 token desconocido",
                lambda: sandbox.bank.accounts("token-inventado"), "invalid_token")
    )

    revocable = sandbox.grant(["accounts:balances"])
    sandbox.consents.revoke(revocable.consent_id, actor="cliente", reason="prueba")
    cases.append(
        _expect("seguridad", "S2 consentimiento revocado",
                lambda: sandbox.bank.balances(revocable.access_token, "acc_0100"),
                "invalid_token")
    )

    # S3 es el caso que mas implementaciones falla: la diferencia entre las dos
    # respuestas es lo que permite enumerar cuentas.
    def _codigo(fn) -> str:
        try:
            fn()
        except (ApiError, AuthError) as exc:
            detalle = getattr(exc, "message", getattr(exc, "description", ""))
            return f"{exc.code}|{detalle}"
        return "sin error"

    ajena = _codigo(lambda: sandbox.bank.balances(full.access_token, "acc_0200"))
    inexistente = _codigo(lambda: sandbox.bank.balances(full.access_token, "acc_9999"))
    cases.append(
        Case("seguridad", "S3 cuenta ajena e inexistente indistinguibles",
             ajena == inexistente, f"{ajena} vs {inexistente}")
    )
    cases.append(
        Case("seguridad", "S4 sin tokens en el registro de auditoria",
             all(full.access_token not in str(e) for e in sandbox.auth.audit),
             f"{len(sandbox.auth.audit)} entradas revisadas")
    )

    # -------------------------------------------------------------- resiliencia
    cuerpo = {"amount": "45000.00", "currency": "CLP",
              "creditor": "acc_0300", "debtor_account": "acc_0100"}
    primera = sandbox.payments.create(full.access_token, "idem-1", cuerpo)
    repetidas = [sandbox.payments.create(full.access_token, "idem-1", cuerpo)
                 for _ in range(5)]
    cases.append(
        Case("resiliencia", "R1 cinco reintentos, un solo pago",
             all(r["payment_id"] == primera["payment_id"] for r in repetidas),
             f"payment_id={primera['payment_id']}")
    )
    cases.append(
        _expect("resiliencia", "R2 misma clave, cuerpo distinto",
                lambda: sandbox.payments.create(full.access_token, "idem-1",
                                                {**cuerpo, "amount": "99000.00"}),
                "idempotency_conflict")
    )
    cases.append(
        _expect("resiliencia", "R3 transicion ilegal de estado",
                lambda: sandbox.payments.advance(primera["payment_id"], "liquidado"),
                "invalid_request")
    )

    sonda = sandbox.grant(["payments:initiate"], customer_ref="cus_synthetic_0002")
    for importe in ("900000.00", "500000.00"):
        sandbox.payments.confirm_funds(sonda.access_token, "acc_0200", importe)
    cases.append(
        _expect("resiliencia", "R4 patron de biseccion en confirmacion de fondos",
                lambda: sandbox.payments.confirm_funds(sonda.access_token, "acc_0200",
                                                       "250000.00"),
                "rate_limited")
    )
    return cases


def report(cases: list[Case] | None = None) -> str:
    cases = cases if cases is not None else run()
    aprobados = sum(1 for c in cases if c.passed)
    lineas = [
        "INFORME DE CONFORMIDAD",
        "  implementacion:       open_finance_sandbox",
        f"  casos ejecutados:     {len(cases)}",
        f"  aprobados:            {aprobados}",
        f"  fallidos:             {len(cases) - aprobados}",
        "",
    ]
    for familia in ("autorizacion", "contrato", "seguridad", "resiliencia"):
        lineas.append(familia.upper())
        for case in (c for c in cases if c.family == familia):
            marca = "OK   " if case.passed else "FALLO"
            lineas.append(f"  {marca} {case.name} -- {case.detail}")
        lineas.append("")
    lineas.append("FUERA DE ALCANCE (declarado)")
    lineas += [f"  - {limite}" for limite in LIMITACIONES]
    return "\n".join(lineas)
