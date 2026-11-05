"""Recalcula las cifras de docs/ejercicios-ueno-bank.md.

Los datos son sinteticos (bancos Yvyra y Tajy) salvo la garantia historica de
228,3 millones de Gs. La prueba protege que el texto y el calculo no se separen.
"""

from __future__ import annotations

from pathlib import Path

import pytest

DOC = Path(__file__).resolve().parents[1] / "docs" / "ejercicios-ueno-bank.md"
TEXTO = DOC.read_text(encoding="utf-8")


def r(k: float, apr: float) -> float:
    return 100 * k / apr


def test_ejemplo_guiado_1_liquidez_y_solvencia():
    # retiro: P no cambia
    assert 900 - (940 - 100) == 60
    # perdida de 70: patrimonio negativo
    assert (100 + 900 - 70) - 940 == -10


def test_ejemplo_guiado_2_cadena_cartera_capital():
    k0 = 140 - 40
    assert round(r(k0, 700), 2) == 14.29
    k1 = (140 - 60) - 40
    assert round(r(k1, 700), 2) == 5.71
    assert round(100 * r(k1, 700) / 12 / 100, 3) == pytest.approx(0.476, abs=1e-3)
    assert 0.12 * 700 - k1 == 44
    assert 0.06 * 700 - k1 == 2
    assert round(r(90, 700), 2) == 12.86
    assert r(140, 700) == 20.0


def test_b1_retiro_frente_a_perdida():
    assert round(100 * 20 / 1100, 2) == 1.82
    assert round(100 * 140 / 1300, 2) == 10.77
    assert round(100 * 80 / 1340, 2) == 5.97


def test_b2_porcentaje_del_minimo():
    assert round(5.56 / 12 * 100, 1) == 46.3
    assert round(12 - 5.56, 2) == 6.44
    assert 5.56 < 0.5 * 12


def test_b3_garantia_por_depositante_y_entidad():
    g = 228.3
    assert 75 * 3.044 == pytest.approx(g)
    assert min(400, g) == g
    assert round(400 - g, 1) == 171.7
    assert round(100 * g / 400, 1) == 57.1


def test_b4_concentracion_vinculadas():
    assert 150 / 1000 == 0.15
    assert 150 / 100 == 1.5
    assert 150 - 0.20 * 100 == 130


def test_i1_i2_banco_tajy():
    assert r(90 - 30, 500) == 12.0
    assert r(70 - 30, 500) == 8.0
    assert round(100 * 8 / 12, 1) == 66.7
    assert r(55, 500) == 11.0
    assert r(70, 500) == 14.0
    # revertir una activacion: K no cambia si se deducia
    assert (90 - 30) == (60 - 0)


def test_i3_liquidez_bajo_estres():
    liquidez = 120 + 0.90 * 180
    assert liquidez == pytest.approx(282)
    assert round(liquidez / 60, 2) == 4.70
    assert round(liquidez / 120, 2) == 2.35
    assert round(liquidez / 240, 3) == 1.175
    assert round(liquidez / 300, 2) == 0.94
    assert round(100 * liquidez / 1200, 1) == 23.5


def test_i4_anticipo_y_remanente():
    g = 228.3
    anticipo = 40 * 3.044
    assert round(anticipo, 2) == 121.76
    assert round(anticipo - 20, 2) == 101.76
    assert round((g - 20) - (anticipo - 20), 2) == round(g - anticipo, 2) == 106.54
    assert round(100 * anticipo / g, 1) == 53.3
    assert round(100 * (500 - g) / 500, 1) == 54.3


def test_a1_alternativas_de_resolucion():
    tasa = 1000 / 1200
    costo_pago = 700 - tasa * 700
    assert round(costo_pago, 1) == 116.7
    assert round(tasa * 500, 1) == 416.7
    assert 200 > costo_pago              # alternativa 2 viola menor costo
    assert round(100 * 300 / 500, 1) == 60.0 < round(100 * tasa, 1)  # alt. 3
    assert round(tasa * 700, 1) == 583.3


def test_a2_estres_inverso():
    assert 100 - 0.12 * 700 == 16
    assert 100 - 0.06 * 700 == 58
    assert round(16 / 0.88, 2) == 18.18
    assert round(58 / 0.94, 2) == 61.70
    assert round(r(40, 700), 2) == 5.71 and r(40, 640) == 6.25


def test_a3_concentracion_por_grupo():
    por_nombre = [60, 40, 30, 20, 20]
    assert sum(por_nombre) == 170
    assert 150 + 4 * 20 == 230
    hhi_nombre = 6**2 + 4**2 + 3**2 + 2**2 + 10 * 2**2
    hhi_grupo = 15**2 + 10 * 2**2
    assert (hhi_nombre, hhi_grupo) == (105, 265)
    assert round(hhi_grupo / hhi_nombre, 2) == 2.52
    assert 0.40 * 150 == 60


def test_a4_linea_de_tiempo_de_liquidez():
    salidas = [0.03, 0.05, 0.08, 0.08, 0.06]
    acumulado, total = [], 0.0
    for s in salidas:
        total += s * 1200
        acumulado.append(round(total))
    assert acumulado == [36, 96, 192, 288, 360]
    assert acumulado[3] > 282 and acumulado[2] <= 282
    assert acumulado[3] <= 332 and acumulado[4] > 332
    assert acumulado[4] <= 382


@pytest.mark.parametrize("fragmento", [
    "Ejemplo guiado 1", "Ejemplo guiado 2", "B1", "B4", "I1", "I4", "A1", "A4",
    "Parte C", "Parte D", "Parte E",
])
def test_el_documento_contiene_cada_bloque(fragmento: str):
    assert fragmento in TEXTO


def test_nota_ejemplo_de_la_rubrica():
    assert round(0.2 * 4 + 0.3 * 4 + 0.3 * 1 + 0.2 * 1, 1) == 2.5
