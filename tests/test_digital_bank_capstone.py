"""Pruebas del capstone del banco digital (Parte 23).

Cada prueba esta asociada a una afirmacion concreta de una clase. Las que llevan
el sufijo `_documenta_el_problema` deben pasar precisamente porque reproducen un
razonamiento que el capstone persigue.
"""

from __future__ import annotations

import pytest

from apps.digital_bank_capstone.build import (
    NO_EXTERNALIZABLES,
    Componente,
    Decision as DecisionBuild,
    Salida,
    concentracion_del_sector,
)
from apps.digital_bank_capstone.scope import (
    Alcance,
    Funcion,
    carga_regulatoria,
    facturacion_necesaria,
    saldo_minimo,
)
from apps.digital_bank_capstone.stress import (
    Escenario,
    NivelDePrueba,
    Proveedor,
    coste_de_las_correcciones,
    desviaciones,
)
from apps.digital_bank_capstone.tensions import Decision, Sistema

# --------------------------------------------------------------------------
# Clase 1 — el alcance
# --------------------------------------------------------------------------


def _alcance() -> Alcance:
    a = Alcance()
    for nombre, quien, ingreso, coste, reg in (
        ("cuentas y pagos", 2400, 620_000, 180_000, "captacion"),
        ("transfronterizos", 2400, 430_000, 210_000, "pagos"),
        ("custodia digital", 0, 0, 240_000, "custodia"),
        ("cambio de divisas", 2400, 240_000, 90_000, "cambio"),
        ("emision tokenizada", 0, 0, 320_000, "oferta publica"),
        ("mercado secundario", 0, 0, 280_000, "mercado"),
        ("credito con colateral", 640, 77_520, 160_000, "credito"),
    ):
        a.proponer(Funcion(nombre, quien, ingreso, coste, reg))
    return a


def test_reducir_el_alcance_no_baja_el_ingreso_documenta_el_problema():
    """Clase 1: las funciones excluidas no generaban ingreso, y por eso el
    recorte sube el margen sin coste comercial.
    """
    a = _alcance()
    ingreso_con_todas = a.ingreso
    regimenes_con_todas = len(a.regimenes)

    excluidas = a.excluir_las_que_no_aportan()

    assert excluidas == 3
    assert a.ingreso == ingreso_con_todas  # <- NO BAJA
    assert len(a.regimenes) < regimenes_con_todas
    assert a.coste < 1_280_000


def test_una_exclusion_sin_razon_no_es_una_exclusion():
    a = _alcance()
    with pytest.raises(ValueError):
        a.excluir("custodia digital", razon="")


def test_una_funcion_sin_segmento_no_aporta():
    sin = Funcion("stablecoin propia", 0, 0, 300_000, "emisor")
    con = Funcion("cambio", 2400, 240_000, 90_000, "cambio")
    assert not sin.aporta
    assert con.aporta
    assert con.margen == 150_000


def test_la_carga_regulatoria_crece_con_cada_regimen():
    cuatro = carga_regulatoria(4, 70_000, 480_000, 5, 350_000, 0.08)
    nueve = carga_regulatoria(9, 70_000, 480_000, 5, 350_000, 0.08)
    assert nueve - cuatro == 350_000


def test_la_facturacion_necesaria_es_la_cifra_que_decide():
    carga = carga_regulatoria(4, 70_000, 480_000, 5, 350_000, 0.08)
    assert facturacion_necesaria(carga, 0.22) == pytest.approx(1_836_364, rel=0.001)
    with pytest.raises(ValueError):
        facturacion_necesaria(carga, 0)


def test_el_saldo_minimo_sale_del_coste_unitario():
    assert saldo_minimo(20, 0.018) == pytest.approx(1_111, abs=1)


# --------------------------------------------------------------------------
# Clase 2 — construir o integrar
# --------------------------------------------------------------------------


def _nucleo() -> Componente:
    return Componente("nucleo", False, True, 420_000, 265_000, 90_000, 185_000,
                      Salida(True, True, 6, 340_000))


def _sin_salida() -> Componente:
    return Componente("registro de colateral", True, False, 380_000, 140_000,
                      120_000, 110_000, Salida(False, False, None, None))


def test_la_salida_manda_sobre_el_coste_documenta_el_problema():
    """Clase 2: integrar el registro de colateral es mas barato y aun asi se
    construye, porque no hay a donde migrar.
    """
    componente = _sin_salida()
    assert componente.coste_integrar(5) < componente.coste_construir(5)

    decision, motivo = componente.decidir()
    assert decision is DecisionBuild.CONSTRUIR
    assert "dependencia estructural" in motivo


def test_integrar_gana_cuando_la_salida_es_real():
    decision, motivo = _nucleo().decidir()
    assert decision is DecisionBuild.INTEGRAR
    assert "ahorra" in motivo


def test_sin_salida_real_el_coste_de_abandonar_es_rehacer():
    componente = _sin_salida()
    con_salida = componente.coste_integrar(5, con_una_salida=True)
    assert con_salida > componente.coste_construir(5) - componente.coste_construir_anual * 5


def test_la_salida_exige_las_cuatro_respuestas():
    assert Salida(True, True, 6, 340_000).es_real
    assert not Salida(True, True, None, 340_000).es_real
    assert not Salida(False, True, 6, 340_000).es_real


def test_hay_funciones_que_no_se_externalizan():
    assert len(NO_EXTERNALIZABLES) == 5
    assert any("supervisor" in f for f in NO_EXTERNALIZABLES)


def test_la_concentracion_del_sector_se_mide():
    assert concentracion_del_sector(14, 18) == pytest.approx(0.778, abs=0.005)
    with pytest.raises(ValueError):
        concentracion_del_sector(14, 0)


# --------------------------------------------------------------------------
# Clase 12 — las tensiones aparecen al integrar
# --------------------------------------------------------------------------


def _sistema() -> Sistema:
    s = Sistema()
    s.decidir(Decision("liquidacion atomica", 10, "sin riesgo de principal", 3_096))
    s.decidir(Decision("horario ampliado", 5, "opera de 07:00 a 22:00", 1_238))
    s.decidir(Decision("lista blanca con espera", 9, "48 h de margen", 0))
    s.decidir(Decision("margen a 30 minutos", 12, "reaccion rapida", 0))
    return s


def test_una_tension_sin_resolver_bloquea_el_sistema_documenta_el_problema():
    """Clase 12: dos decisiones correctas por separado se contradicen al
    integrarse, y el expediente exige resolverlas y declararlas.
    """
    s = _sistema()
    s.declarar_tension("liquidacion atomica", "horario ampliado",
                       "prefinanciar mas horas encarece el saldo ocioso")

    puede, motivo = s.puede_operar()
    assert not puede
    assert "sin resolver" in motivo


def test_resolver_exige_declarar_el_sacrificio():
    s = _sistema()
    t = s.declarar_tension("lista blanca con espera", "margen a 30 minutos",
                           "la espera impide atender una urgencia")
    with pytest.raises(ValueError):
        t.resolver("", 8_000)

    t.resolver("via de excepcion con doble aprobacion", 8_000)
    assert t.resuelta
    puede, _ = s.puede_operar()
    assert puede


def test_declarar_una_tension_sobre_una_decision_inexistente_falla():
    s = _sistema()
    with pytest.raises(KeyError):
        s.declarar_tension("liquidacion atomica", "inexistente", "x")


def test_la_tolerancia_la_fija_el_consejo_no_el_area_tecnica():
    s = _sistema()
    with pytest.raises(ValueError):
        s.fijar_tolerancia("liquidacion", 2.0, "sistemas")

    s.fijar_tolerancia("liquidacion", 2.0, "consejo")
    assert s.tolerancias[0].funcion == "liquidacion"


def test_las_tolerancias_incumplidas_se_detectan():
    s = _sistema()
    s.fijar_tolerancia("liquidacion", 2.0, "consejo")
    s.fijar_tolerancia("llamadas de margen", 0.5, "consejo")

    incumplidas = s.tolerancias_incumplidas(
        {"liquidacion": 1.0, "llamadas de margen": 0.7}
    )
    assert incumplidas == ["llamadas de margen"]


# --------------------------------------------------------------------------
# Clase 15 — el escenario de tension
# --------------------------------------------------------------------------


def _corresponsal() -> Proveedor:
    return Proveedor("banco corresponsal",
                     frozenset({"emisor del deposito", "liquidador de pagos",
                                "depositario de efectivo"}))


def test_un_proveedor_con_varios_papeles_es_la_fuente_documenta_el_problema():
    """Clase 15: un solo fallo alcanza a los tres componentes a la vez, y esa
    correlacion es lo que convierte tres fallos improbables en un episodio.
    """
    proveedor = _corresponsal()
    assert proveedor.es_fuente_de_correlacion

    e = Escenario(proveedor)
    nuevos = e.desencadenar(72.0, "problemas de liquidez")

    assert len(nuevos) == 3
    assert e.componentes_afectados == 3


def test_un_proveedor_con_un_solo_papel_no_correlaciona():
    simple = Proveedor("proveedor de identidad", frozenset({"verificacion"}))
    assert not simple.es_fuente_de_correlacion


def test_un_escenario_de_un_solo_componente_no_demuestra_nada():
    simple = Proveedor("x", frozenset({"uno"}))
    e = Escenario(simple)
    e.desencadenar(2.0, "caida")
    assert not e.demuestra_algo


def test_el_escenario_conserva_la_peor_interrupcion_por_componente():
    e = Escenario(_corresponsal())
    e.anadir("pagos", 2.0, "primera")
    e.anadir("pagos", 6.0, "segunda")
    assert e.interrupciones()["pagos"] == 6.0


def test_el_nivel_de_prueba_va_de_uno_a_cinco():
    assert int(NivelDePrueba.DOCUMENTAL) == 1
    assert int(NivelDePrueba.CONMUTACION_NO_ANUNCIADA) == 5
    e = Escenario(_corresponsal(), nivel_de_prueba=NivelDePrueba.ENTORNO_AISLADO)
    assert e.nivel_de_prueba < NivelDePrueba.CONMUTACION_PLANIFICADA


def test_las_desviaciones_situan_el_punto_de_rotura():
    assert desviaciones(0.09, 0.018) == pytest.approx(5.0, abs=0.1)
    with pytest.raises(ValueError):
        desviaciones(0.09, 0)


def test_las_correcciones_se_suman_y_se_comparan():
    correcciones = {"segundo emisor": 18_000, "corresponsal alternativo": 12_000}
    assert coste_de_las_correcciones(correcciones) == 30_000
