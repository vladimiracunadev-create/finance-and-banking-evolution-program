"""Pruebas del laboratorio de crisis de custodia.

Las pruebas marcadas `documenta_el_problema` fijan una trampa conceptual: deben
pasar, porque sin ellas el material afirmaria algo que el codigo no sostiene.
"""

import csv
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from apps.custody_crisis_lab import cases, costs, datos, recovery, replenish, runs  # noqa: E402
from apps.custody_crisis_lab.entity import Custodio, caso_sintetico  # noqa: E402
from apps.custody_crisis_lab.incident import (  # noqa: E402
    aplicar_perdida,
    aplicar_restitucion,
    clasificar_fondos,
)
from apps.custody_crisis_lab.scenario import ejecutar  # noqa: E402


# --- entity -----------------------------------------------------------------


def test_respaldo_antes_del_incidente():
    e = caso_sintetico()
    assert e.respaldo_bruto == pytest.approx(1.0)
    assert e.respaldo_disponible == pytest.approx(0.8)
    assert e.brecha == pytest.approx(0.0)


def test_entidad_rechaza_valores_invalidos():
    with pytest.raises(ValueError):
        Custodio(-1, 0, 10)
    with pytest.raises(ValueError):
        Custodio(1, 1, 0)


# --- incident ---------------------------------------------------------------


def test_clasificar_fondos_ejercicio_resuelto():
    f = clasificar_fondos(6300, 3000, 0.8)
    assert f.restituible == pytest.approx(2400)
    assert f.sin_congelar == pytest.approx(3300)
    assert f.perdida_definitiva == pytest.approx(3900)


@pytest.mark.parametrize(
    "s,f,p", [(100, 200, 0.5), (-1, 0, 0.5), (100, 50, 1.5), (100, 50, -0.1)]
)
def test_clasificar_fondos_rechaza_entradas_incoherentes(s, f, p):
    with pytest.raises(ValueError):
        clasificar_fondos(s, f, p)


def test_congelado_no_es_recuperado_documenta_el_problema():
    """El respaldo cae en S aunque F este congelado; solo sube al restituir."""
    e = caso_sintetico()
    despues = aplicar_perdida(e, 6300)
    assert despues.respaldo_bruto == pytest.approx(0.937)
    # Congelar 3 000 no cambia el balance de la entidad.
    assert despues.respaldo_bruto == pytest.approx(0.937)
    restituido = aplicar_restitucion(despues, 2400)
    assert restituido.respaldo_bruto == pytest.approx(0.961)


def test_perdida_se_imputa_al_otro_tramo_si_excede():
    e = Custodio(10, 90, 100)
    despues = aplicar_perdida(e, 40, parte_liquida=1.0)
    assert despues.activos_liquidos == pytest.approx(0)
    assert despues.activos_no_liquidos == pytest.approx(60)


def test_perdida_mayor_que_activos_falla():
    with pytest.raises(ValueError):
        aplicar_perdida(caso_sintetico(), 100_001)


# --- runs -------------------------------------------------------------------


def test_tasa_maxima_atendible_es_el_respaldo_disponible():
    despues = aplicar_perdida(caso_sintetico(), 6300)
    assert runs.tasa_maxima_atendible(despues) == pytest.approx(0.737)
    assert runs.cobertura_de_retiros(despues, 0.10) == pytest.approx(7.37)


def test_corrida_con_pausa_no_paga_durante_la_pausa():
    despues = aplicar_perdida(caso_sintetico(), 6300)
    h = runs.simular_corrida(despues, 0.03, 1.0, 5, pausa_dias=2)
    assert [d.pagado for d in h[:2]] == [0.0, 0.0]
    assert h[2].pagado > 0


def test_corrida_agota_liquidez_y_deja_impagos():
    despues = aplicar_perdida(caso_sintetico(), 20_000)
    h = runs.simular_corrida(despues, 0.20, 3.0, 8)
    assert sum(d.impagado for d in h) > 0


def test_reposicion_durante_la_corrida_evita_impagos():
    despues = aplicar_perdida(caso_sintetico(), 20_000)
    sin = runs.simular_corrida(despues, 0.20, 3.0, 8)
    con = runs.simular_corrida(despues, 0.20, 3.0, 8, reposiciones={1: 20_000})
    assert sum(d.impagado for d in con) < sum(d.impagado for d in sin)


def test_corrida_rechaza_parametros_invalidos():
    with pytest.raises(ValueError):
        runs.simular_corrida(caso_sintetico(), 0.1, 1.0, 0)
    with pytest.raises(ValueError):
        runs.simular_corrida(caso_sintetico(), 0.1, 1.0, 3, descuento=1.0)


# --- replenish --------------------------------------------------------------


def test_necesidad_de_reposicion():
    despues = aplicar_perdida(caso_sintetico(), 6300)
    assert replenish.necesidad_de_reposicion(despues) == pytest.approx(6300)
    assert replenish.necesidad_de_reposicion(caso_sintetico()) == 0
    assert replenish.necesidad_de_reposicion(despues, 0.9) == pytest.approx(0)


def test_costo_de_compra_crece_mas_que_proporcional():
    c1 = replenish.costo_de_compra(100, 0.02, 1000)
    c2 = replenish.costo_de_compra(200, 0.02, 1000)
    assert c1 == pytest.approx(0.2)
    assert c2 == pytest.approx(4 * c1)


def test_plan_de_reposicion_usa_fuentes_en_orden():
    fuentes = [
        replenish.Fuente("a", 100, 0.0),
        replenish.Fuente("b", 200, 0.01),
        replenish.Fuente("c", 1000, 0.05),
    ]
    plan = replenish.plan_de_reposicion(350, fuentes)
    assert [a.monto for a in plan.aportes] == [100, 200, 50]
    assert plan.costo_total == pytest.approx(0 + 2 + 2.5)
    assert plan.faltante == 0


def test_plan_de_reposicion_informa_faltante():
    plan = replenish.plan_de_reposicion(500, [replenish.Fuente("a", 100, 0.0)])
    assert plan.faltante == pytest.approx(400)


# --- costs ------------------------------------------------------------------


def test_costo_total_suma_componentes_y_descuenta_seguro():
    c = costs.Costos(3900, 80, 50, 16, 0, recuperacion_seguro=100)
    assert c.bruto == pytest.approx(4046)
    assert c.neto == pytest.approx(3946)
    assert costs.recuperacion_de_seguro(100, 60) == 60
    assert costs.costo_de_oportunidad(8, 2) == 16
    assert costs.compensaciones(0.01, 1000) == 10


def test_el_costo_no_es_el_monto_sustraido_documenta_el_problema():
    """Costo total (4 046) != sustraido (6 300): una cifra no sustituye a la otra."""
    r = ejecutar(caso_sintetico(), datos.cargar_escenarios()["crd_002"])
    assert r.costos.bruto != pytest.approx(r.fondos.sustraido)
    assert r.costos.bruto == pytest.approx(4046)


# --- recovery ---------------------------------------------------------------


def test_trayectoria_cae_primero_y_sube_con_reposicion_y_restitucion():
    e = caso_sintetico()
    t = recovery.trayectoria_de_respaldo(e, 6300, {14: 2400}, {3: 6300}, 15)
    assert t[0][1] == pytest.approx(0.937)
    assert t[3][1] == pytest.approx(1.0)
    assert t[14][1] == pytest.approx(1.024)


def test_plan_tiene_siete_fases_con_entrada_y_salida():
    assert len(recovery.PLAN) == 7
    for fase in recovery.PLAN:
        assert fase.entrada and fase.salida and fase.responsable


# --- datos y escenario ------------------------------------------------------


def test_el_dataset_reproduce_el_caso_sintetico():
    assert datos.cargar_entidad() == caso_sintetico()


def test_los_escenarios_del_dataset_son_coherentes():
    escenarios = datos.cargar_escenarios()
    assert set(escenarios) == {"crd_001", "crd_002", "crd_003"}
    for esc in escenarios.values():
        assert esc.congelado <= esc.sustraido
        assert 0 <= esc.p_restitucion <= 1


def test_escenario_extraordinario_completo():
    r = ejecutar(caso_sintetico(), datos.cargar_escenarios()["crd_002"])
    assert r.despues.respaldo_bruto == pytest.approx(0.937)
    assert r.reposicion.faltante == 0
    assert r.reposicion.costo_total == pytest.approx(80)
    assert r.trayectoria[-1][1] == pytest.approx(1.024)


def test_escenario_severo_exige_financiamiento_externo():
    r = ejecutar(caso_sintetico(), datos.cargar_escenarios()["crd_003"])
    nombres = [a.fuente for a in r.reposicion.aportes]
    assert "financiamiento externo" in nombres


def test_la_severidad_ordena_el_costo():
    e = caso_sintetico()
    esc = datos.cargar_escenarios()
    costos = [ejecutar(e, esc[k]).costos.bruto for k in ("crd_001", "crd_002", "crd_003")]
    assert costos == sorted(costos)


def test_el_dataset_de_escenarios_no_cambia_sin_darse_cuenta():
    with datos.ESCENARIOS.open(newline="", encoding="utf-8") as f:
        filas = list(csv.DictReader(f))
    assert [fila["scenario_id"] for fila in filas] == ["crd_001", "crd_002", "crd_003"]


# --- caso Binance 2026 ------------------------------------------------------


def test_cifras_publicas_son_estimaciones_con_fuente():
    for valor, quien, nota in cases.CIFRAS_PUBLICAS.values():
        assert valor > 0 and quien and nota


def test_las_fuentes_discrepan_documenta_el_problema():
    """Los emisores no suman lo congelado que declara la entidad."""
    c = cases.CIFRAS_PUBLICAS
    emisores = c["congelado_tether"][0] + c["congelado_circle"][0]
    assert emisores == pytest.approx(2370)
    assert emisores < c["congelado_binance"][0]
    assert c["sustraido_chainalysis"][0] > c["sustraido_binance"][0]
    assert c["congelado_inicial"][0] != c["congelado_binance"][0]


def test_binance_estilizado_respaldo_antes_y_despues():
    c = cases.CIFRAS_PUBLICAS
    e = cases.entidad_binance_estilizada()
    despues = aplicar_perdida(e, c["sustraido_binance"][0])
    assert e.respaldo_bruto == pytest.approx(1.0)
    assert despues.respaldo_bruto == pytest.approx(1 - 6300 / 155_000)
    # La reserva anunciada cubre la brecha estimada con un margen pequeno.
    assert c["reserva_compania"][0] - despues.brecha == pytest.approx(40)


# --- CLI --------------------------------------------------------------------


@pytest.mark.parametrize(
    "args",
    [
        ["caso", "--escenario", "crd_002"],
        ["fondos", "--sustraido", "6300", "--congelado", "3000"],
        ["plan"],
        ["binance"],
    ],
)
def test_cli_ejecuta(args):
    r = subprocess.run(
        [sys.executable, str(ROOT / "apps/custody_crisis_lab/cli.py"), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    assert r.returncode == 0, r.stderr
    assert r.stdout.strip()


def test_cli_rechaza_fondos_incoherentes():
    r = subprocess.run(
        [sys.executable, str(ROOT / "apps/custody_crisis_lab/cli.py"),
         "fondos", "--sustraido", "100", "--congelado", "200"],
        capture_output=True,
        text=True,
    )
    assert r.returncode == 2


# --- ejercicios del documento ----------------------------------------------


def test_los_ejercicios_resueltos_del_documento_coinciden_con_el_codigo():
    """Si cambia una cifra del documento o del codigo, esta prueba lo delata."""
    e = caso_sintetico()
    despues = aplicar_perdida(e, 6300)
    assert (despues.respaldo_bruto, despues.respaldo_disponible) == (
        pytest.approx(0.937),
        pytest.approx(0.737),
    )
    for p, rec, perdida in ((0.5, 1500, 4800), (0.8, 2400, 3900), (1.0, 3000, 3300)):
        f = clasificar_fondos(6300, 3000, p)
        assert (f.restituible, f.perdida_definitiva) == (
            pytest.approx(rec),
            pytest.approx(perdida),
        )
    assert runs.cobertura_de_retiros(despues, 0.10) == pytest.approx(7.37)
    assert replenish.costo_de_compra(500, 0.02, 1000) == pytest.approx(5)
    assert replenish.costo_de_compra(1000, 0.02, 1000) == pytest.approx(20)
    assert costs.Costos(3900, 80, 50, 16, 0, 300).neto == pytest.approx(3746)


def test_la_pauta_de_evaluacion_coincide_con_el_codigo():
    e = Custodio(36_000, 9_000, 50_000, fondo_proteccion=500)
    assert (e.respaldo_bruto, e.respaldo_disponible, e.brecha) == (
        pytest.approx(0.90), pytest.approx(0.72), pytest.approx(5000))
    d = aplicar_perdida(e, 2000)
    assert (d.respaldo_bruto, d.respaldo_disponible, d.brecha) == (
        pytest.approx(0.86), pytest.approx(0.68), pytest.approx(7000))
    f = clasificar_fondos(2000, 1200, 0.5)
    assert (f.sin_congelar, f.restituible, f.perdida_definitiva) == (
        pytest.approx(800), pytest.approx(600), pytest.approx(1400))
    assert runs.cobertura_de_retiros(d, 0.08) == pytest.approx(8.5)
    plan = replenish.plan_de_reposicion(
        replenish.necesidad_de_reposicion(d),
        [replenish.Fuente("fondo", 500, 0.0), replenish.Fuente("capital", 4000, 0.01),
         replenish.Fuente("externo", 20_000, 0.05)],
    )
    assert plan.costo_total == pytest.approx(165)
    total = costs.Costos(f.perdida_definitiva, plan.costo_total, 20,
                         costs.costo_de_oportunidad(3, 4), 0).bruto
    assert total == pytest.approx(1597)
