"""Pruebas del entorno de finanzas abiertas de la Parte 17.

La mayoria son NEGATIVAS a proposito: comprueban que el sistema falla donde
debe fallar. Una bateria de camino feliz no demuestra que una API financiera
sea integrable.
"""

from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from apps.open_finance_sandbox import CLIENT_ID, REDIRECT_URI, build  # noqa: E402
from apps.open_finance_sandbox.authorization_server import AuthError, s256  # noqa: E402
from apps.open_finance_sandbox.bank_api import ApiError  # noqa: E402
from apps.open_finance_sandbox.conformance_tests import run as run_conformance  # noqa: E402
from apps.open_finance_sandbox.consent_dashboard import ConsentError  # noqa: E402
from apps.open_finance_sandbox.payment_initiation import canonical  # noqa: E402
from apps.open_finance_sandbox.third_party_provider import (  # noqa: E402
    CAMPOS_DESCARTADOS,
    ingest,
    savings_capacity,
)


@pytest.fixture()
def sandbox():
    return build()


# --------------------------------------------------------------- consentimiento


def test_alcance_desconocido_se_rechaza(sandbox):
    with pytest.raises(ConsentError):
        sandbox.consents.create(
            consent_id="c1", customer_ref="cus_synthetic_0001",
            provider_id=CLIENT_ID, scopes=["accounts:todo"],
            purpose="p", notice_version="v1",
        )


def test_no_se_concede_un_alcance_que_no_se_presento(sandbox):
    with pytest.raises(ConsentError):
        sandbox.consents.create(
            consent_id="c2", customer_ref="cus_synthetic_0001",
            provider_id=CLIENT_ID, scopes=["accounts:list", "payments:initiate"],
            purpose="p", notice_version="v1",
            presented_scopes=["accounts:list"],
        )


def test_transicion_ilegal_de_consentimiento(sandbox):
    grant = sandbox.grant(["accounts:list"])
    sandbox.consents.revoke(grant.consent_id, actor="cliente", reason="x")
    with pytest.raises(ConsentError):
        sandbox.consents.transition(grant.consent_id, "vigente")


def test_el_historico_conserva_los_consentimientos_revocados(sandbox):
    grant = sandbox.grant(["accounts:list"])
    sandbox.consents.revoke(grant.consent_id, actor="cliente", reason="x")
    historico = sandbox.consents.for_customer("cus_synthetic_0001")
    assert [c.status for c in historico] == ["revocado"]


# ----------------------------------------------------------------- autorizacion


def test_flujo_completo_devuelve_saldo(sandbox):
    grant = sandbox.grant(["accounts:balances"])
    saldo = sandbox.bank.balances(grant.access_token, "acc_0100")["data"]
    assert saldo["currency"] == "CLP"
    # El saldo debe cuadrar con la suma de movimientos mas el saldo inicial:
    # sin `opening_balance` el tercero no puede reconstruirlo (clase 4).
    assert "opening_balance" in saldo


def test_authorize_sin_pkce_falla(sandbox):
    grant = sandbox.grant(["accounts:list"])
    with pytest.raises(AuthError) as exc:
        sandbox.auth.authorize(
            client_id=CLIENT_ID, redirect_uri=REDIRECT_URI, scope="accounts:list",
            state="s", code_challenge=None, code_challenge_method=None,
            consent_id=grant.consent_id,
        )
    assert exc.value.code == "invalid_request"


@pytest.mark.parametrize(
    "uri",
    [
        "https://app.cuentasclaras.cl.atacante.io/callback",
        "https://app.cuentasclaras.cl@atacante.io/callback",
        "https://app.cuentasclaras.cl/callback/../../otro",
    ],
)
def test_redirect_uri_por_prefijo_no_pasa(sandbox, uri):
    grant = sandbox.grant(["accounts:list"])
    with pytest.raises(AuthError):
        sandbox.auth.authorize(
            client_id=CLIENT_ID, redirect_uri=uri, scope="accounts:list",
            state="s", code_challenge=s256("v" * 50), code_challenge_method="S256",
            consent_id=grant.consent_id,
        )


def test_codigo_de_un_solo_uso(sandbox):
    grant = sandbox.grant(["accounts:list"])
    verifier = "v" * 60
    resp = sandbox.auth.authorize(
        client_id=CLIENT_ID, redirect_uri=REDIRECT_URI, scope="accounts:list",
        state="s", code_challenge=s256(verifier), code_challenge_method="S256",
        consent_id=grant.consent_id,
    )
    sandbox.auth.token(CLIENT_ID, resp["code"], verifier)
    with pytest.raises(AuthError) as exc:
        sandbox.auth.token(CLIENT_ID, resp["code"], verifier)
    assert exc.value.code == "invalid_grant"


def test_code_verifier_incorrecto_falla(sandbox):
    grant = sandbox.grant(["accounts:list"])
    resp = sandbox.auth.authorize(
        client_id=CLIENT_ID, redirect_uri=REDIRECT_URI, scope="accounts:list",
        state="s", code_challenge=s256("verificador-correcto"),
        code_challenge_method="S256", consent_id=grant.consent_id,
    )
    with pytest.raises(AuthError):
        sandbox.auth.token(CLIENT_ID, resp["code"], "verificador-distinto")


def test_token_acotado_al_alcance_concedido(sandbox):
    grant = sandbox.grant(["accounts:list"])
    with pytest.raises(AuthError) as exc:
        sandbox.bank.balances(grant.access_token, "acc_0100")
    assert exc.value.code == "resource_forbidden"


def test_el_registro_no_contiene_tokens(sandbox):
    grant = sandbox.grant(["accounts:list"])
    assert all(grant.access_token not in str(e) for e in sandbox.auth.audit)


# -------------------------------------------------------------------- revocacion


def test_revocar_invalida_los_tokens_vivos(sandbox):
    grant = sandbox.grant(["accounts:balances"])
    assert sandbox.bank.balances(grant.access_token, "acc_0100")
    sandbox.consents.revoke(grant.consent_id, actor="cliente", reason="prueba")
    # No basta con que el estado cambie: el acceso debe fallar de verdad.
    with pytest.raises(AuthError):
        sandbox.bank.balances(grant.access_token, "acc_0100")


# ------------------------------------------------------------------- cuentas


def test_no_se_pueden_enumerar_cuentas(sandbox):
    grant = sandbox.grant(["accounts:balances"])

    def codigo(account_id):
        try:
            sandbox.bank.balances(grant.access_token, account_id)
        except ApiError as exc:
            return (exc.code, exc.message)
        return ("sin_error", "")

    assert codigo("acc_0200") == codigo("acc_9999")


def test_limite_de_pagina_acotado(sandbox):
    grant = sandbox.grant(["accounts:transactions"])
    pagina = sandbox.bank.transactions(grant.access_token, "acc_0100", limit=100000)
    assert pagina["meta"]["count"] <= 100


def test_paginacion_por_cursor_no_repite_ni_omite(sandbox):
    grant = sandbox.grant(["accounts:transactions"])
    vistos, cursor = [], None
    while True:
        pagina = sandbox.bank.transactions(
            grant.access_token, "acc_0100", limit=7, cursor=cursor
        )
        vistos += [t["transaction_id"] for t in pagina["data"]]
        cursor = pagina["links"]["next"]
        if not cursor:
            break
    assert len(vistos) == len(set(vistos)), "el cursor repite filas"
    assert len(vistos) == 36, "el cursor omite filas"


def test_cursor_invalido_da_400_no_500(sandbox):
    grant = sandbox.grant(["accounts:transactions"])
    with pytest.raises(ApiError) as exc:
        sandbox.bank.transactions(grant.access_token, "acc_0100", cursor="@@@")
    assert exc.value.status == 400


def test_importes_son_cadena_decimal(sandbox):
    grant = sandbox.grant(["accounts:transactions"])
    pagina = sandbox.bank.transactions(grant.access_token, "acc_0100", limit=3)
    assert all(isinstance(t["amount"], str) for t in pagina["data"])


# --------------------------------------------------------------------- pagos


def test_pago_sin_clave_de_idempotencia_falla(sandbox):
    grant = sandbox.grant(["payments:initiate"])
    with pytest.raises(ApiError) as exc:
        sandbox.payments.create(grant.access_token, None, {"amount": "1000.00"})
    assert exc.value.code == "invalid_request"


def test_cinco_reintentos_no_duplican_el_pago(sandbox):
    grant = sandbox.grant(["payments:initiate"])
    cuerpo = {"amount": "45000.00", "currency": "CLP",
              "creditor": "acc_0300", "debtor_account": "acc_0100"}
    ids = {sandbox.payments.create(grant.access_token, "k", cuerpo)["payment_id"]
           for _ in range(5)}
    assert len(ids) == 1


def test_orden_de_las_claves_no_altera_la_huella():
    assert canonical({"a": 1, "b": 2}) == canonical({"b": 2, "a": 1})


def test_misma_clave_con_cuerpo_distinto_es_conflicto(sandbox):
    grant = sandbox.grant(["payments:initiate"])
    cuerpo = {"amount": "45000.00", "currency": "CLP",
              "creditor": "acc_0300", "debtor_account": "acc_0100"}
    sandbox.payments.create(grant.access_token, "k", cuerpo)
    with pytest.raises(ApiError) as exc:
        sandbox.payments.create(grant.access_token, "k", {**cuerpo, "amount": "1.00"})
    assert exc.value.code == "idempotency_conflict"


def test_aceptado_no_es_firme(sandbox):
    grant = sandbox.grant(["payments:initiate"])
    cuerpo = {"amount": "45000.00", "currency": "CLP",
              "creditor": "acc_0300", "debtor_account": "acc_0100"}
    pago = sandbox.payments.create(grant.access_token, "k", cuerpo)
    sandbox.payments.advance(pago["payment_id"], "autorizado")
    aceptado = sandbox.payments.advance(pago["payment_id"], "aceptado")
    assert aceptado["is_firm"] is False
    sandbox.payments.advance(pago["payment_id"], "en_ejecucion")
    liquidado = sandbox.payments.advance(pago["payment_id"], "liquidado")
    assert liquidado["is_firm"] is True


def test_confirmacion_de_fondos_corta_la_biseccion(sandbox):
    grant = sandbox.grant(["payments:initiate"])
    sandbox.payments.confirm_funds(grant.access_token, "acc_0100", "900000.00")
    sandbox.payments.confirm_funds(grant.access_token, "acc_0100", "500000.00")
    with pytest.raises(ApiError) as exc:
        sandbox.payments.confirm_funds(grant.access_token, "acc_0100", "250000.00")
    assert exc.value.code == "rate_limited"


# ------------------------------------------------------------------- el tercero


def test_la_ingesta_descarta_los_datos_de_contraparte():
    crudo = [{"transaction_id": "t1", "amount": "-1000.00",
              "booking_date": "2026-01-05T03:14:00Z",
              "counterparty_name": "Juan Perez", "counterparty_account": "***4821"}]
    limpio = ingest(crudo)[0]
    assert not (CAMPOS_DESCARTADOS & set(limpio))


def test_la_capacidad_de_ahorro_declara_su_limitacion():
    resultado = savings_capacity(
        [{"transaction_id": "t1", "amount": "800000.00",
          "booking_date": "2026-01-05T03:14:00Z"},
         {"transaction_id": "t2", "amount": "-500000.00",
          "booking_date": "2026-01-18T03:14:00Z"}]
    )
    assert resultado["savings_capacity"] == "300000.00"
    assert "seguros" in resultado["limitation"]


# ------------------------------------------------------------------ conformidad


def test_la_bateria_de_conformidad_pasa_entera():
    fallidos = [c for c in run_conformance() if not c.passed]
    assert not fallidos, [f"{c.family}/{c.name}: {c.detail}" for c in fallidos]
