"""Recalcula las cifras de docs/ejercicios-ley-21850.md.

Los datos son sinteticos (Andes Insumos, Banco Costanera). Las tasas y plazos de
la ley (27 / 25,5 / 24 / 23 %, 15 % y 20 % de credito, tope de 75 UTM, condonacion
de Tesoreria) estan en el expediente con su articulo. La prueba protege que el
texto y el calculo no se separen.
"""

from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "ejercicios-ley-21850.md"
TEXTO = DOC.read_text(encoding="utf-8")

TASAS = {2026: 0.27, 2027: 0.255, 2028: 0.24, 2029: 0.23}
RESTITUCION = {2026: 0.35, 2027: 0.30, 2028: 0.20, 2029: 0.0}


def carga(rli: float, tc: float, rho: float, tf: float = 0.40) -> float:
    return tf * rli + rho * tc * rli


def test_ejemplo_1_carga_total_por_ano():
    esperado = {2026: 494.5, 2027: 476.5, 2028: 448.0, 2029: 400.0}
    for ano, valor in esperado.items():
        assert carga(1000, TASAS[ano], RESTITUCION[ano]) == pytest.approx(valor)
    # toda la baja de la carga viene de la restitucion
    assert 0.35 * 270 == pytest.approx(94.5)
    assert 494.5 - 400 == pytest.approx(94.5)


def test_la_formula_coincide_con_el_calculo_por_escalones():
    for ano in TASAS:
        rli, tc, rho = 1000, TASAS[ano], RESTITUCION[ano]
        idpc = tc * rli
        d = rli - idpc
        credito = idpc  # se imputa entero y luego se restituye la fraccion rho
        final = 0.40 * (d + idpc) - credito + rho * credito
        assert idpc + final == pytest.approx(carga(rli, tc, rho))


def test_ejemplo_2_wacc_y_valor():
    def wacc(t):
        return 0.6 * 0.12 + 0.4 * 0.07 * (1 - t)

    assert round(wacc(0.27) * 100, 3) == 9.244
    assert round(wacc(0.23) * 100, 3) == 9.356
    v27 = 1000 * (1 - 0.27) / wacc(0.27)
    v23 = 1000 * (1 - 0.23) / wacc(0.23)
    assert round(v27) == 7897
    assert round(v23) == 8230
    assert round(100 * (v23 / v27 - 1), 1) == 4.2
    assert round(100 * (770 / 730 - 1), 1) == 5.5


def test_b1_cobertura_y_covenant():
    cob = {a: 1000 * (1 - t) / 600 for a, t in TASAS.items()}
    assert round(cob[2026], 3) == 1.217
    assert round(cob[2027], 3) == 1.242
    assert round(cob[2028], 3) == 1.267
    assert round(cob[2029], 3) == 1.283
    assert [a for a, c in cob.items() if c >= 1.25][0] == 2028


def test_b2_costo_de_repartir():
    assert round(carga(1000, 0.27, 0.35) - 270, 1) == 224.5
    assert round(carga(1000, 0.23, 0.0) - 230, 1) == 170.0
    assert 224.5 - 170 == pytest.approx(54.5)


def test_b3_ganancia_de_capital():
    ganancia = 160 - 100
    antes = ganancia - 0.10 * ganancia
    assert (ganancia, antes) == (60, 54)
    assert round(100 * (60 / 54 - 1), 1) == 11.1


def test_b4_credito_por_exportacion():
    rem = 36_000_000
    assert 0.15 * 0.60 * rem == pytest.approx(3_240_000)
    assert 0.20 * 0.60 * rem == pytest.approx(4_320_000)
    assert 75 * 69_000 == 5_175_000
    assert 4_320_000 < 5_175_000


def test_b5_b6_tesoreria():
    contado = 100 + 30 * (1 - 1.00) + 10 * (1 - 0.80)
    convenio = 100 + 30 * (1 - 0.95) + 10 * (1 - 0.75)
    assert contado == pytest.approx(102)
    assert convenio == pytest.approx(104)
    cuota = (convenio - 10) / 48
    assert round(cuota, 3) == 1.958
    r = 1.12 ** (1 / 12) - 1
    vp = 10 + sum(cuota / (1 + r) ** k for k in range(1, 49))
    assert round(vp, 1) == 85.2


def test_a1_sensibilidad_ke():
    kd = lambda t: 0.07 * (1 - t)  # noqa: E731
    v27 = 730 / (0.6 * 0.12 + 0.4 * kd(0.27))
    wacc_eq = 770 / v27
    assert round(wacc_eq * 100, 3) == 9.751
    ke = (wacc_eq - 0.4 * kd(0.23)) / 0.6
    assert round(ke * 100, 2) == 12.66


def test_a2_invariabilidad_punto_de_equilibrio():
    factor_10 = sum(1 / 1.1**k for k in range(1, 11))
    factor_6_10 = sum(1 / 1.1**k for k in range(6, 11))
    assert round(factor_10, 4) == 6.1446
    assert round(factor_6_10, 4) == 2.3538
    costo = 3 * factor_10
    perdida_por_p = 14 * factor_6_10
    assert round(costo, 2) == 18.43
    assert round(perdida_por_p, 2) == 32.95
    assert round(100 * costo / perdida_por_p, 1) == 55.9


def test_a3_impuesto_diferido_del_banco():
    nuevo = 200 * 23 / 27
    assert round(nuevo, 1) == 170.4
    assert round(nuevo - 200, 1) == -29.6
    assert round(100 * 1400 / 10000, 2) == 14.00
    assert round(100 * (1400 - 29.63) / 10000, 2) == 13.70


def test_a4_recaudacion_neutra():
    assert round(100 * (27 / 23 - 1), 1) == 17.4


def test_a5_impuesto_unico_sobre_saldos():
    ordinario = 0.40 * (500 + 100) - 100
    opcion = 0.10 * 500
    assert (ordinario, opcion) == (140, 50)
    assert ordinario - opcion == 90
    vp = ordinario / 1.1**3
    assert round(vp, 1) == 105.2
    assert round(vp - opcion, 1) == 55.2


def test_plazos_calculados_desde_la_publicacion():
    publicacion = date(2026, 10, 17)
    assert publicacion + timedelta(days=90) == date(2027, 1, 15)
    assert publicacion + timedelta(days=180) == date(2027, 4, 15)


def test_el_script_del_laboratorio_corre():
    bloque = TEXTO.split("```python", 1)[1].split("```", 1)[0]
    exec(compile(bloque, "laboratorio", "exec"), {})  # noqa: S102


def test_el_documento_declara_la_naturaleza_de_las_cifras():
    assert "sintéticas" in TEXTO
    assert "no es asesoría" in TEXTO.lower() or "Nada de esto es asesoría" in TEXTO
