"""Pruebas del laboratorio de FX sobre registros (Parte 21).

Cada prueba esta asociada a una afirmacion concreta de una clase. Las que llevan
el sufijo `_documenta_el_problema` deben pasar precisamente porque reproducen un
defecto de razonamiento que el material persigue.
"""

from __future__ import annotations

import pytest

from apps.onchain_fx_lab.amm import (
    Piscina,
    ReservaAgotada,
    perdida_por_divergencia,
    razon_que_anula_las_comisiones,
    resultado_del_aportante,
)
from apps.onchain_fx_lab.pricing import (
    Mecanismo,
    ahorro_corregido_por_profundidad,
    comparar,
    ruta_mayorista,
    ruta_registro,
)
from apps.onchain_fx_lab.settlement import (
    Comparacion,
    Mecanismo as MecanismoLiquidacion,
    limite_bilateral,
    perdida_esperada,
    ventana_de_exposicion,
)

# --------------------------------------------------------------------------
# Clase 11 — formacion de precio y coste total
# --------------------------------------------------------------------------


def test_solo_un_libro_propio_forma_precio():
    assert Mecanismo.LIBRO_PROPIO.forma_precio
    assert not Mecanismo.ORACULO_IMPORTADO.forma_precio
    assert not Mecanismo.FORMULA_AUTOMATIZADA.forma_precio


def test_el_precio_mostrado_esconde_cuatro_tramos_documenta_el_problema():
    """Clase 11: comparar precios mostrados omite margen, entrada y salida."""
    registro = ruta_registro(8.0, 6.0, 4.0, 4.5)
    nombres = [t.nombre for t in registro.tramos]

    assert "margen sobre el importado" in nombres
    assert "entrada al registro" in nombres
    assert "salida del registro" in nombres
    # Solo el diferencial seria visible en el precio mostrado.
    assert registro.total_pb > registro.tramos[1].puntos_basicos * 4


def test_en_el_par_principal_el_registro_pierde_por_5_veces():
    resultado = comparar(
        ruta_mayorista(1.2, 3.0),
        ruta_registro(8.0, 6.0, 4.0, 4.5),
        3_000_000,
    )
    assert resultado["mayorista_pb"] == pytest.approx(3.6)
    assert resultado["registro_pb"] == pytest.approx(19.5)
    assert not resultado["gana_el_registro"]
    assert resultado["veces"] == pytest.approx(5.4, abs=0.1)


def test_en_el_par_poco_liquido_el_registro_gana_por_la_corresponsalia():
    resultado = comparar(
        ruta_mayorista(45.0, 18.0, 22.0),
        ruta_registro(12.0, 18.0, 4.0, 4.5),
        3_000_000,
    )
    assert resultado["mayorista_pb"] == pytest.approx(62.5)
    assert resultado["registro_pb"] == pytest.approx(29.5)
    assert resultado["ahorro_pb"] == pytest.approx(33.0)
    assert resultado["ahorro"] == pytest.approx(9_900)


def test_la_profundidad_reduce_el_ahorro_anunciado():
    corregido = ahorro_corregido_por_profundidad(33.0, 3_000_000, 5_200_000, 6)
    assert corregido["impacto_pb"] == pytest.approx(24.0, abs=0.2)
    assert corregido["ahorro_real_pb"] == pytest.approx(9.0, abs=0.2)
    assert corregido["sigue_compensando"]


def test_con_un_libro_muy_fino_el_ahorro_desaparece():
    corregido = ahorro_corregido_por_profundidad(33.0, 3_000_000, 480_000, 6)
    assert corregido["ahorro_real_pb"] < 0
    assert not corregido["sigue_compensando"]


def test_ejecutar_en_un_solo_tramo_es_peor_que_escalonar():
    de_golpe = ahorro_corregido_por_profundidad(33.0, 3_000_000, 5_200_000, 1)
    escalonado = ahorro_corregido_por_profundidad(33.0, 3_000_000, 5_200_000, 6)
    assert de_golpe["impacto_pb"] > escalonado["impacto_pb"]


def test_la_correccion_exige_una_profundidad_valida():
    with pytest.raises(ValueError):
        ahorro_corregido_por_profundidad(33.0, 3_000_000, 0, 6)
    with pytest.raises(ValueError):
        ahorro_corregido_por_profundidad(33.0, 3_000_000, 5_200_000, 0)


# --------------------------------------------------------------------------
# Clase 13 — creador de mercado automatizado
# --------------------------------------------------------------------------


def _piscina() -> Piscina:
    return Piscina(reserva_a=500_000, reserva_b=1_000_000, comision=0.0025)


def test_el_deslizamiento_es_el_tamano_relativo_a_la_reserva():
    for entrega in (5_000, 10_000, 25_000):
        c = _piscina().cotizar(entrega)
        assert c["deslizamiento"] == pytest.approx(c["tamano_relativo"], abs=0.005)


def test_el_precio_efectivo_es_siempre_peor_que_el_marginal():
    c = _piscina().cotizar(10_000)
    assert c["precio_efectivo"] < c["precio_marginal"]


def test_operar_mueve_las_reservas_y_el_precio():
    piscina = _piscina()
    antes = piscina.precio_marginal
    piscina.operar(20_000)
    assert piscina.precio_marginal < antes
    assert piscina.reserva_a > 500_000
    assert piscina.reserva_b < 1_000_000


def test_la_reserva_nunca_se_vacia_por_grande_que_sea_la_operacion():
    """Propiedad del producto constante: la reserva tiende a cero sin llegar.

    Por eso el mecanismo siempre da precio, y por eso ese precio puede ser
    absurdo: dar precio no es lo mismo que dar liquidez.
    """
    c = _piscina().cotizar(10_000_000_000)
    assert c["recibe"] < 1_000_000
    assert c["deslizamiento"] > 0.99  # el precio efectivo es ruinoso


def test_una_reserva_vacia_no_tiene_precio():
    with pytest.raises(ReservaAgotada):
        Piscina(reserva_a=0, reserva_b=1_000).precio_marginal


def test_la_perdida_por_divergencia_es_siempre_negativa_o_cero():
    assert perdida_por_divergencia(1.0) == pytest.approx(0.0)
    for r in (0.5, 1.25, 1.5, 2.0, 4.0):
        assert perdida_por_divergencia(r) < 0


def test_la_perdida_reproduce_los_valores_de_la_clase():
    assert perdida_por_divergencia(1.25) == pytest.approx(-0.0062, abs=0.0002)
    assert perdida_por_divergencia(1.50) == pytest.approx(-0.0202, abs=0.0002)
    assert perdida_por_divergencia(2.00) == pytest.approx(-0.0572, abs=0.0002)
    assert perdida_por_divergencia(4.00) == pytest.approx(-0.2000, abs=0.0002)


def test_la_divergencia_es_simetrica_en_ambos_sentidos():
    assert perdida_por_divergencia(2.0) == pytest.approx(perdida_por_divergencia(0.5))


def test_las_comisiones_se_comen_una_parte_del_rendimiento():
    resultado = resultado_del_aportante(100_000, 12_600, 1.45)
    assert resultado["divergencia"] == pytest.approx(-1_701, abs=5)
    assert resultado["neto"] == pytest.approx(10_899, abs=5)
    assert resultado["rendimiento"] == pytest.approx(0.109, abs=0.001)
    assert resultado["compensa"]


def test_con_un_movimiento_grande_aportar_deja_de_compensar():
    resultado = resultado_del_aportante(100_000, 12_600, 4.0)
    assert not resultado["compensa"]


def test_la_razon_que_anula_las_comisiones_se_calcula():
    r = razon_que_anula_las_comisiones(12_600, 100_000)
    assert r == pytest.approx(2.89, abs=0.05)
    assert perdida_por_divergencia(r) == pytest.approx(-0.126, abs=0.002)


def test_un_valor_aportado_no_positivo_falla():
    with pytest.raises(ValueError):
        razon_que_anula_las_comisiones(12_600, 0)


# --------------------------------------------------------------------------
# Clase 12 — riesgo de liquidacion
# --------------------------------------------------------------------------


def test_la_ventana_va_de_irrevocable_a_confirmado():
    normal = ventana_de_exposicion(10, 16, 11)
    assert normal.horas == 19


def test_el_fin_de_semana_triplica_la_ventana():
    finde = ventana_de_exposicion(10, 16, 11, dias_no_habiles=2)
    assert finde.horas == 67
    assert finde.dias == pytest.approx(2.79, abs=0.01)


def _base() -> float:
    diario = perdida_esperada(40_000_000, 0.00003, 0.45, 1.0, 250)
    finde = perdida_esperada(40_000_000, 0.00003, 0.45, 2.8, 50)
    return diario + finde


def test_la_perdida_esperada_sin_mecanismo():
    assert _base() == pytest.approx(257_400, rel=0.001)


def test_con_neteo_oponible_el_neteo_es_la_opcion_mas_barata():
    comparacion = Comparacion(
        perdida_sin_mecanismo=_base(),
        exposicion_bruta=40_000_000,
        fraccion_neteada=0.18,
        coste_financiacion_anual=0.043,
        fraccion_prefinanciada=0.25,
        neteo_oponible=True,
    )
    assert comparacion.mejor() == MecanismoLiquidacion.NETEO.value

    evaluacion = comparacion.evaluar()
    assert evaluacion["neteo"]["total"] == pytest.approx(46_332, rel=0.001)
    assert evaluacion["pvp_neteado"]["total"] == pytest.approx(154_800, rel=0.001)


def test_sin_oponibilidad_el_neteo_no_reduce_nada_documenta_el_problema():
    """Clase 12: un acuerdo firmado que no es oponible en el concurso de la
    contraparte no reduce la exposicion, aunque el informe la declare reducida.
    """
    comparacion = Comparacion(
        perdida_sin_mecanismo=_base(),
        exposicion_bruta=40_000_000,
        fraccion_neteada=0.18,
        coste_financiacion_anual=0.043,
        fraccion_prefinanciada=0.25,
        neteo_oponible=False,
    )
    evaluacion = comparacion.evaluar()

    assert evaluacion["neteo"]["total"] == evaluacion["ninguno"]["total"]
    assert comparacion.mejor() == MecanismoLiquidacion.NINGUNO.value


def test_cada_mecanismo_se_compara_con_la_misma_base():
    comparacion = Comparacion(
        perdida_sin_mecanismo=_base(),
        exposicion_bruta=40_000_000,
        fraccion_neteada=0.18,
        coste_financiacion_anual=0.043,
        fraccion_prefinanciada=0.25,
    )
    evaluacion = comparacion.evaluar()

    # Los dos PvP eliminan el riesgo de principal, no lo reducen.
    assert evaluacion["pvp_bruto"]["perdida_esperada"] == 0
    assert evaluacion["pvp_neteado"]["perdida_esperada"] == 0
    # Y el neteo reduce la perdida sin coste de liquidez.
    assert evaluacion["neteo"]["coste"] == 0


def test_el_limite_bilateral_ajusta_la_exposicion_al_apetito():
    limite = limite_bilateral(_base(), 40_000_000, 80_000)
    assert limite == pytest.approx(12_433_000, rel=0.01)
    assert limite < 40_000_000
