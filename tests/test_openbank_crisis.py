"""Pruebas del escenario de crisis digital del simulador OpenBank.

Incluye regresion: el simulador original no debe cambiar su comportamiento.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parents[1] / "apps" / "openbank_simulator"))
from bank import Bank  # noqa: E402
from crisis_digital import (  # noqa: E402
    CrisisDigital,
    ReservaInsuficiente,
    RetirosPausados,
    ejecutar_escenario,
)


@pytest.fixture
def banco(tmp_path):
    b = Bank(tmp_path / "bank.db")
    b.initialize()
    return b


def _con_clientes(banco, n=4, deposito=1000.0):
    crisis = CrisisDigital(banco)
    crisis.inicializar(liquida=0.8 * n * deposito, no_liquida=0.2 * n * deposito)
    cuentas = [
        banco.open_account(banco.create_customer(f"C{i}"), deposito) for i in range(n)
    ]
    return crisis, cuentas


def test_regresion_el_simulador_original_sigue_igual(banco):
    a = banco.open_account(banco.create_customer("Uno"), 1000)
    b = banco.open_account(banco.create_customer("Dos"), 0)
    banco.transfer(a, b, 300)
    assert (banco.balance(a), banco.balance(b)) == (700, 300)
    assert banco.summary()["deposits"] == 1000


def test_respaldo_inicial_es_100_por_ciento(banco):
    crisis, _ = _con_clientes(banco)
    assert crisis.foto().respaldo == pytest.approx(1.0)
    assert crisis.foto().respaldo_disponible == pytest.approx(0.8)


def test_incidente_baja_el_respaldo_sin_tocar_los_depositos(banco):
    crisis, _ = _con_clientes(banco)
    crisis.transferencia_no_autorizada(400)
    f = crisis.foto()
    assert f.depositos == pytest.approx(4000)
    assert f.respaldo == pytest.approx(0.9)


def test_la_perdida_no_supera_la_reserva_liquida(banco):
    crisis, _ = _con_clientes(banco)
    assert crisis.transferencia_no_autorizada(10_000) == pytest.approx(3200)


def test_retiro_con_pausa_se_rechaza(banco):
    crisis, cuentas = _con_clientes(banco)
    crisis.pausar_retiros()
    with pytest.raises(RetirosPausados):
        crisis.retirar(cuentas[0], 100)
    assert banco.balance(cuentas[0]) == 1000


def test_retiro_sin_reserva_liquida_suficiente_falla_sin_mover_saldos(banco):
    crisis, cuentas = _con_clientes(banco)
    crisis.transferencia_no_autorizada(3200)
    with pytest.raises(ReservaInsuficiente):
        crisis.retirar(cuentas[0], 100)
    assert banco.balance(cuentas[0]) == 1000


def test_retiro_exitoso_baja_saldo_reserva_y_registra_movimiento(banco):
    crisis, cuentas = _con_clientes(banco)
    crisis.retirar(cuentas[0], 250)
    assert banco.balance(cuentas[0]) == 750
    assert crisis.foto().reserva_liquida == pytest.approx(2950)
    with banco.connect() as con:
        kinds = [r[0] for r in con.execute(
            "SELECT kind FROM transactions WHERE account_id = ?", (cuentas[0],))]
    assert "withdrawal" in kinds


def test_retiro_mayor_que_el_saldo_falla(banco):
    crisis, cuentas = _con_clientes(banco)
    with pytest.raises(ValueError):
        crisis.retirar(cuentas[0], 5000)


def test_reponer_y_validaciones(banco):
    crisis, _ = _con_clientes(banco)
    crisis.transferencia_no_autorizada(400)
    crisis.reponer(400)
    assert crisis.foto().respaldo == pytest.approx(1.0)
    with pytest.raises(ValueError):
        crisis.reponer(0)
    with pytest.raises(ValueError):
        crisis.transferencia_no_autorizada(-1)


def test_escenario_completo_con_reposicion_paga_todo(banco):
    etapas = ejecutar_escenario(banco)
    assert etapas["normal"].respaldo == pytest.approx(1.0)
    assert etapas["incidente"].respaldo == pytest.approx(0.85)
    assert etapas["retiros_bloqueados"] == 10
    assert etapas["repuesto"].respaldo == pytest.approx(1.0)
    assert etapas["retiros_fallidos"] == 0


def test_sin_reposicion_la_reapertura_deja_clientes_sin_pagar(tmp_path):
    etapas = ejecutar_escenario(
        Bank(tmp_path / "b.db"), perdida=1500.0, reposicion=1e-9, retiros_pct=0.9
    )
    assert etapas["retiros_fallidos"] > 0
