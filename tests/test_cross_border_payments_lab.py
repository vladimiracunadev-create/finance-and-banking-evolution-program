"""Pruebas del laboratorio de pagos transfronterizos de la Parte 18.

Cada prueba corresponde a una afirmacion concreta de una clase. Si la prueba
falla, la clase esta diciendo algo que el codigo no sostiene.
"""

from datetime import datetime
from decimal import Decimal
from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from apps.cross_border_payments_lab import build  # noqa: E402
from apps.cross_border_payments_lab.fast_payment_link import (  # noqa: E402
    Cotizacion,
    Enlace,
    LimiteExcedido,
    NoResuelto,
    REGLAS_MINIMAS,
    reglas_pendientes,
    subastar,
)
from apps.cross_border_payments_lab.flows import cuadra  # noqa: E402
from apps.cross_border_payments_lab.iso20022 import (  # noqa: E402
    Orden,
    Parte,
    TransicionIlegal,
    construir_pacs008,
    pacs002,
    transitar,
    validar,
)
from apps.cross_border_payments_lab.remittances import (  # noqa: E402
    Ruta as RutaRemesa,
    Tramo,
)
from apps.cross_border_payments_lab.routing_engine import Pago, Pesos, Ruta  # noqa: E402
from apps.cross_border_payments_lab.screening import (  # noqa: E402
    Designado,
    evaluar,
    medir,
    prueba_retrospectiva,
)
from apps.cross_border_payments_lab.settlement import (  # noqa: E402
    Operacion,
    SistemaLiquidacion,
    exposicion_maxima,
    liquidar_pvp,
    netting_multilateral,
    ratio_netting,
)
from apps.cross_border_payments_lab.stablecoin_route import (  # noqa: E402
    RutaClasica,
    RutaStablecoin,
    comparar,
    descomponer_ahorro,
    enrutar,
    porcentaje_atribuible_al_registro,
)


@pytest.fixture()
def lab():
    return build()


# ------------------------------------------------------------------- flujos


def test_el_mensaje_no_espera_a_los_fondos(lab):
    """Clase 5: el mensaje tarda segundos y el dinero, horas."""
    traza, _ = lab.pagar("CL-VN", 10_000, "2026-06-16T16:40:00")
    inicio = datetime.fromisoformat("2026-06-16T16:40:00")

    assert traza.duracion("mensaje", inicio).total_seconds() < 30
    assert traza.duracion("fondos", inicio).total_seconds() > 3600


def test_la_espera_domina_el_tiempo_total(lab):
    traza, _ = lab.pagar("CL-VN", 10_000, "2026-06-16T16:40:00")
    partes = traza.descomposicion(datetime.fromisoformat("2026-06-16T16:40:00"))
    assert partes["espera_horas"] / partes["total_horas"] > 0.95


def test_un_festivo_alarga_el_pago_dias(lab):
    """Clase 5: el mensaje sigue tardando dos segundos."""
    normal, _ = lab.pagar("CL-VN", 10_000, "2026-06-16T16:40:00")
    festivo, _ = lab.pagar("CL-VN", 10_000, "2026-06-18T16:40:00")

    inicio_n = datetime.fromisoformat("2026-06-16T16:40:00")
    inicio_f = datetime.fromisoformat("2026-06-18T16:40:00")
    assert festivo.duracion("fondos", inicio_f) > normal.duracion("fondos", inicio_n)
    assert festivo.duracion("mensaje", inicio_f).total_seconds() < 30


def test_cada_asiento_tiene_contrapartida(lab):
    _, asientos = lab.pagar("CL-VN", 10_000, "2026-06-16T16:40:00")
    assert asientos
    assert cuadra(asientos)


def test_una_alerta_retrasa_los_fondos_no_el_mensaje(lab):
    sin_alerta, _ = lab.pagar("CL-US", 10_000, "2026-06-16T14:00:00")
    con_alerta, _ = lab.pagar("CL-US", 10_000, "2026-06-16T14:00:00", alerta_en=0)
    inicio = datetime.fromisoformat("2026-06-16T14:00:00")

    assert con_alerta.duracion("fondos", inicio) > sin_alerta.duracion("fondos", inicio)
    assert con_alerta.duracion("mensaje", inicio) == sin_alerta.duracion("mensaje", inicio)


# ------------------------------------------------------------ motor de rutas


def _pago(corredor: str, **extra) -> Pago:
    base = dict(
        corredor=corredor,
        importe=20_000.0,
        moneda_origen="MA",
        moneda_destino="MB",
        canal_beneficiario="cuenta",
        controles=frozenset({"screening", "travel_rule"}),
    )
    base.update(extra)
    return Pago(**base)


def test_el_enlace_de_pagos_inmediatos_tiene_prioridad(lab):
    decision = lab.enrutar(_pago("A", importe=1_000.0))
    assert decision.ruta.tipo == "enlace_pagos_inmediatos"
    assert "enlace" in decision.motivo


def test_cadena_corta_prefiere_la_ruta_clasica(lab):
    decision = lab.enrutar(_pago("B"))
    assert decision.ruta.nombre == "B-clasica"


def test_cadena_larga_prefiere_la_ruta_con_stablecoin(lab):
    decision = lab.enrutar(_pago("C"))
    assert decision.ruta.nombre == "C-stablecoin"


def test_un_filtro_de_cumplimiento_no_se_compensa_con_precio(lab):
    """Clase 12: en cumplimiento no hay apetito de riesgo."""
    decision = lab.enrutar(_pago("D", controles=frozenset({"screening", "travel_rule"})))
    assert decision.ruta.nombre == "D-clasica"
    assert "travel_rule" in decision.descartadas["D-stablecoin"]


def test_toda_decision_lleva_motivo(lab):
    for corredor in ("A", "B", "C", "D", "E", "F"):
        decision = lab.enrutar(_pago(corredor, importe=1_000.0))
        assert decision.motivo


def test_sin_ruta_para_un_canal_no_soportado(lab):
    decision = lab.enrutar(_pago("B", canal_beneficiario="efectivo_rural"))
    assert decision.ruta is None
    assert "ninguna ruta admite" in decision.motivo


def test_cambiar_un_peso_cambia_la_eleccion():
    rapida = Ruta(
        nombre="rapida", tipo="x", corredor="Z", importe_maximo=1e9,
        monedas=frozenset({"MA", "MB"}), canales=frozenset({"cuenta"}),
        controles_soportados=frozenset({"screening"}), coste_fijo=0.0,
        coste_variable=0.04, diferencial_pb=0, plazo_p50_h=1, plazo_p95_h=1,
        riesgo=0.2, disponibilidad=0.99,
    )
    barata = Ruta(
        nombre="barata", tipo="x", corredor="Z", importe_maximo=1e9,
        monedas=frozenset({"MA", "MB"}), canales=frozenset({"cuenta"}),
        controles_soportados=frozenset({"screening"}), coste_fijo=0.0,
        coste_variable=0.012, diferencial_pb=0, plazo_p50_h=30, plazo_p95_h=30,
        riesgo=0.2, disponibilidad=0.99,
    )
    pago = _pago("Z", controles=frozenset({"screening"}))
    from apps.cross_border_payments_lab.routing_engine import elegir

    con_prisa = elegir(pago, [rapida, barata], Pesos(tiempo=0.8, coste=0.1, riesgo=0.1))
    con_precio = elegir(pago, [rapida, barata], Pesos(tiempo=0.1, coste=0.8, riesgo=0.1))
    assert con_prisa.ruta.nombre == "rapida"
    assert con_precio.ruta.nombre == "barata"


def test_los_pesos_deben_sumar_uno():
    with pytest.raises(ValueError):
        Pesos(tiempo=0.5, coste=0.5, riesgo=0.5)


# ------------------------------------------------------------------ iso20022


def _orden(**extra) -> Orden:
    base = dict(
        end_to_end_id="E2E-1", uetr="uetr-1", importe="10000.00", divisa="USD",
        fecha_liquidacion="2026-06-18",
        deudor=Parte("Comercial Andina SpA", "CL", "Avenida Apoquindo", "4501", "Santiago"),
        deudor_agente="BANDCLRMXXX",
        acreedor=Parte("Hanoi Trading JSC", "VN", "Pho Ba Trieu", "88", "Hanoi"),
        acreedor_agente="NGVNVNVXXXX", proposito="TRAD",
    )
    base.update(extra)
    return Orden(**base)


def test_un_pacs008_bien_formado_valida():
    xml = construir_pacs008(_orden(), "MSG-1", "2026-06-16T16:40:00Z")
    assert validar(xml) == []


def test_importe_sin_dos_decimales_se_rechaza():
    xml = construir_pacs008(_orden(importe="10000"), "MSG-1", "2026-06-16T16:40:00Z")
    assert any("importe" in e for e in validar(xml))


def test_divisa_no_iso_se_rechaza():
    xml = construir_pacs008(_orden(divisa="DOLAR"), "MSG-1", "2026-06-16T16:40:00Z")
    assert any("divisa" in e for e in validar(xml))


def test_direccion_sin_ciudad_estructurada_se_marca():
    """Clase 6: el texto libre degrada el screening en destino."""
    sin_ciudad = Parte("Hanoi Trading JSC", "VN")
    xml = construir_pacs008(_orden(acreedor=sin_ciudad), "MSG-1", "2026-06-16T16:40:00Z")
    assert any("ciudad estructurada" in e for e in validar(xml))


def test_codigo_de_proposito_fuera_del_catalogo_se_rechaza():
    xml = construir_pacs008(_orden(proposito="XXXX"), "MSG-1", "2026-06-16T16:40:00Z")
    assert any("proposito" in e for e in validar(xml))


def test_las_partes_ultimas_se_incluyen_cuando_aplican():
    plataforma = Parte("Marketplace SA", "CL", "Isidora", "3000", "Santiago")
    vendedor = Parte("Taller Nguyen", "VN", "Le Loi", "12", "Da Nang")
    xml = construir_pacs008(
        _orden(deudor=plataforma, deudor_ultimo=vendedor), "MSG-1", "2026-06-16T16:40:00Z"
    )
    assert "UltmtDbtr" in xml
    assert validar(xml) == []


def test_el_reintento_conserva_la_referencia():
    """Clase 6: la referencia se genera una vez, al crear la orden."""
    orden = _orden()
    primero = construir_pacs008(orden, "MSG-1", "2026-06-16T16:40:00Z")
    orden.reintentar()
    segundo = construir_pacs008(orden, "MSG-2", "2026-06-16T16:45:00Z")
    assert "E2E-1" in primero and "E2E-1" in segundo
    assert orden.intentos == 1


def test_un_rechazo_exige_codigo_del_catalogo():
    with pytest.raises(ValueError):
        pacs002(_orden(), aceptado=False, motivo="MOTIVO_INVENTADO")
    assert "AC01" in pacs002(_orden(), aceptado=False, motivo="AC01")


def test_no_se_puede_devolver_antes_de_liquidar():
    """Clase 6: antes se cancela, despues se devuelve."""
    estado = transitar("recibido", "aceptado")
    with pytest.raises(TransicionIlegal):
        transitar(estado, "devuelto")
    assert transitar(transitar(estado, "liquidado"), "devuelto") == "devuelto"


# ----------------------------------------------------------------- screening


LISTA = [
    Designado("D1", "Nguyen Van Minh", "VN", "1978-03-14"),
    Designado("D2", "Olga Petrova Ivanova", "RU", "1985-11-02"),
]


def test_un_apellido_frecuente_sin_fecha_se_escala_no_se_descarta():
    """Clase 12: descartar por falta de dato es el falso negativo a evitar."""
    alertas = evaluar("Nguyen Van Minh", "", LISTA, umbral=0.8)
    assert alertas and alertas[0].escalada


def test_la_normalizacion_detecta_variantes_de_transliteracion():
    sin = evaluar("Olga Petrowa Iwanowa", "1985-11-02", LISTA, 0.6, con_correcciones=False)
    con = evaluar("Olga Petrowa Iwanowa", "1985-11-02", LISTA, 0.6, con_correcciones=True)
    assert not sin
    assert con


def test_la_prueba_retrospectiva_detecta_verdaderos_positivos_perdidos():
    # Coincidencia parcial: dos de tres tokens. La detecta un umbral de 0,60
    # y la pierde uno de 0,99. Es exactamente el caso que la clase 12 exige
    # comprobar antes de aceptar una subida de umbral.
    confirmados = [("Olga Petrova Smirnova", "1985-11-02")]
    resultado = prueba_retrospectiva(confirmados, LISTA, 0.60, 0.99)
    assert resultado["perdidos"] == 1
    assert resultado["aceptable"] is False


def test_subir_el_umbral_sin_perder_positivos_es_aceptable():
    confirmados = [("Olga Petrova Ivanova", "1985-11-02")]
    resultado = prueba_retrospectiva(confirmados, LISTA, 0.50, 0.90)
    assert resultado["aceptable"] is True


def test_precision_y_exhaustividad_se_calculan():
    casos = [
        ("Olga Petrova Ivanova", "1985-11-02", True),
        ("Carlos Mendez Rios", "1990-07-21", False),
    ]
    metricas = medir(casos, LISTA, umbral=0.8)
    assert 0.0 <= metricas.precision <= 1.0
    assert 0.0 <= metricas.exhaustividad <= 1.0


# ----------------------------------------------------------------- remesas


def test_el_diferencial_cruzado_se_compone_no_se_suma():
    """Clase 9: 1 − (1−a)(1−b), no a + b."""
    # CLP -> USD -> PHP, con los tipos expresados como destino por unidad de
    # origen: esa es la base sobre la que el cliente pierde (clase 9).
    ruta = RutaRemesa(
        nombre="dos-patas",
        comision_envio=Decimal(0),
        tramos=[
            Tramo(Decimal(1) / Decimal(978), Decimal(1) / Decimal(950)),
            Tramo(Decimal("54.6"), Decimal("56.0")),
        ],
    )
    compuesto = ruta.diferencial_compuesto_pb()
    suma = Decimal("286.3") + Decimal("250")
    assert compuesto < suma
    assert abs(compuesto - Decimal("529.1")) < Decimal(2)


def test_el_denominador_es_el_tipo_de_referencia():
    ruta = RutaRemesa(
        nombre="r", comision_envio=Decimal(100),
        tramos=[Tramo(Decimal("0.9"), Decimal("1.0"))],
    )
    importe = Decimal(1000)
    assert ruta.sin_coste(importe) == Decimal(1000)
    assert ruta.coste_total(importe) > Decimal("0.15")


def test_se_avisa_cuando_la_comision_no_llega_a_la_mitad_del_coste():
    """Clase 1: «sin comisiones» significa que todo el precio esta en el tipo."""
    ruta = RutaRemesa(
        nombre="sin-comisiones", comision_envio=Decimal(0),
        tramos=[Tramo(Decimal("0.95"), Decimal("1.0"))],
    )
    assert ruta.aviso_transparencia(Decimal(1000)) is not None


def test_la_descomposicion_suma_el_coste_total():
    ruta = RutaRemesa(
        nombre="r", comision_envio=Decimal(50),
        tramos=[Tramo(Decimal("0.96"), Decimal("1.0"))],
        comision_retiro=Decimal(10),
    )
    partes = ruta.descomponer(Decimal(1000))
    assert partes["comisiones_visibles"] + partes["diferencial"] == partes["coste_total"]


# --------------------------------------------------------------- liquidacion


def test_la_exposicion_es_el_maximo_simultaneo():
    """Clase 15: las exposiciones se acumulan, no se toma la mayor."""
    operaciones = [
        Operacion("1", "CP1", Decimal(40), 9, 15),
        Operacion("2", "CP2", Decimal(25), 10, 15),
        Operacion("3", "CP3", Decimal(30), 14, 15),
    ]
    assert exposicion_maxima(operaciones) == Decimal(95)


def test_pvp_liquida_las_dos_patas_o_ninguna():
    a, b = SistemaLiquidacion("EUR"), SistemaLiquidacion("USD")
    resultado = liquidar_pvp("OP1", Decimal(100), Decimal(108), a, b)
    assert resultado.liquidado
    assert resultado.patas_liberadas == 2


def test_si_el_coordinador_cae_las_reservas_expiran():
    """Clase 15: el plazo vive en cada sistema, no en el coordinador."""
    a, b = SistemaLiquidacion("EUR"), SistemaLiquidacion("USD")
    resultado = liquidar_pvp("OP1", Decimal(100), Decimal(108), a, b, coordinador_cae=True)
    assert not resultado.liquidado
    assert resultado.patas_liberadas == 0
    assert a.reservas["OP1"].deshecha and b.reservas["OP1"].deshecha


def test_el_fallo_tras_la_primera_liberacion_es_el_caso_limite():
    """Clase 15: la atomicidad del protocolo no cubre este caso."""
    a, b = SistemaLiquidacion("EUR"), SistemaLiquidacion("USD")
    resultado = liquidar_pvp(
        "OP1", Decimal(100), Decimal(108), a, b, sistema_b_falla_al_liberar=True
    )
    assert not resultado.liquidado
    assert resultado.patas_liberadas == 1


def test_el_netting_multilateral_cuadra():
    posiciones = {
        ("A", "B"): Decimal(1200), ("A", "C"): Decimal(800),
        ("B", "C"): Decimal(1500), ("C", "A"): Decimal(1900),
    }
    netas = netting_multilateral(posiciones)
    assert sum(netas.values()) == Decimal(0)
    assert netas["C"] == Decimal(400)


def test_el_ratio_de_netting_se_calcula():
    assert ratio_netting(Decimal(6_100_000), Decimal(300_000)) > Decimal("0.95")


# ---------------------------------------------------------- enlace y alias


def test_el_alias_inexistente_responde_igual_que_el_sin_cuenta(lab):
    """Clase 13: si difieren, se puede enumerar quien tiene cuenta."""
    with pytest.raises(NoResuelto):
        lab.directorio.resolver("+5550000000", "tpp1")
    with pytest.raises(NoResuelto):
        lab.directorio.resolver("+5553334444", "tpp1")


def test_el_nombre_se_devuelve_enmascarado(lab):
    resolucion = lab.directorio.resolver("+5551234567", "tpp1")
    assert "*" in resolucion.nombre_mascara
    assert "Maria Elena Rojas" not in resolucion.nombre_mascara


def test_el_limite_de_consultas_corta_la_enumeracion(lab):
    with pytest.raises(LimiteExcedido):
        for _ in range(25):
            try:
                lab.directorio.resolver("+5551234567", "atacante")
            except NoResuelto:
                pass


def test_la_subasta_elige_el_mejor_tipo():
    mejor = subastar([Cotizacion("p1", Decimal(58)), Cotizacion("p2", Decimal(42))])
    assert mejor.proveedor == "p2"


def test_el_enlace_queda_acotado_por_el_sistema_menor():
    enlace = Enlace(Decimal(5000), Decimal(2000), Decimal("0.74"))
    assert enlace.limite_efectivo == Decimal(2000)


def test_la_cobertura_declara_quien_queda_fuera():
    """Clase 13: el analisis que importa es el del segmento excluido."""
    enlace = Enlace(Decimal(5000), Decimal(2000), Decimal("0.74"))
    cobertura = enlace.cobertura(Decimal("0.96"))
    assert abs(cobertura["cobertura_real"] - Decimal("0.7104")) < Decimal("0.001")
    assert cobertura["excluido"] > Decimal("0.28")


def test_las_cinco_reglas_minimas_no_son_tecnicas():
    assert len(REGLAS_MINIMAS) == 5
    assert reglas_pendientes(set()) == list(REGLAS_MINIMAS)
    assert reglas_pendientes(set(REGLAS_MINIMAS)) == []


# ------------------------------------------------------------- stablecoin


def _clasica(intermediarios: int) -> RutaClasica:
    return RutaClasica(
        comision_envio=Decimal(38), diferencial_pb=Decimal(185),
        diferencial_por_intermediario_pb=Decimal(70),
        comision_por_intermediario=Decimal(22), intermediarios=intermediarios,
        comision_receptor=Decimal(14), saldo_prefinanciado=Decimal(400_000),
        coste_fondeo_anual=Decimal("0.042"), operaciones_anuales=1_200,
        coste_mensajeria=Decimal("3.84"), horas_hasta_disponible=Decimal(58),
    )


STABLE = RutaStablecoin(
    entrada_comision_pct=Decimal("0.0035"), entrada_diferencial_pb=Decimal(60),
    comision_red=Decimal("0.04"), salida_comision_pct=Decimal("0.0045"),
    salida_diferencial_pb=Decimal(95), comision_retiro=Decimal(9),
    minutos_tenencia=22, horas_hasta_disponible=Decimal("0.63"),
)


def test_con_cadena_corta_la_ruta_clasica_es_mas_barata():
    """Clase 14: el resultado contraintuitivo del ejemplo guiado."""
    resultado = comparar(_clasica(1), STABLE, Decimal(20_000))
    assert not resultado["gana_stablecoin"]


def test_con_cadena_larga_la_ruta_con_stablecoin_gana():
    assert comparar(_clasica(2), STABLE, Decimal(20_000))["gana_stablecoin"]
    assert comparar(_clasica(3), STABLE, Decimal(20_000))["gana_stablecoin"]


def test_el_tramo_de_red_es_el_mas_barato_de_los_cinco():
    tramos = STABLE.tramos(Decimal(20_000))
    assert tramos["transferencia"] == min(v for v in tramos.values() if v > 0)


def test_la_descomposicion_del_ahorro_suma_el_ahorro_total():
    clasica = _clasica(2)
    fuentes = descomponer_ahorro(clasica, STABLE, Decimal(20_000))
    esperado = clasica.coste(Decimal(20_000)) - STABLE.coste(Decimal(20_000))
    assert abs(sum(fuentes.values()) - esperado) < Decimal("0.01")


def test_el_ahorro_atribuible_al_registro_es_marginal():
    """Clase 14: el 97 % viene de la topologia, no de la tecnologia."""
    porcentaje = porcentaje_atribuible_al_registro(_clasica(2), STABLE, Decimal(20_000))
    assert porcentaje < Decimal(10)


def test_la_exposicion_crece_si_la_salida_se_bloquea():
    planificada = STABLE.exposicion(Decimal(20_000))
    bloqueada = STABLE.exposicion(Decimal(20_000), minutos_reales=3 * 24 * 60)
    assert bloqueada > planificada * 100


@pytest.mark.parametrize(
    "argumentos,esperada",
    [
        ((True, 3, True, 20, True), "enlace_pagos_inmediatos"),
        ((False, 1, True, 20, True), "clasica"),
        ((False, 3, False, 20, True), "clasica"),
        ((False, 3, True, 120, True), "clasica"),
        ((False, 3, True, 20, False), "clasica"),
        ((False, 3, True, 20, True), "stablecoin"),
    ],
)
def test_la_regla_de_enrutamiento_cubre_las_seis_condiciones(argumentos, esperada):
    ruta, motivo = enrutar(*argumentos)
    assert ruta == esperada
    assert motivo
