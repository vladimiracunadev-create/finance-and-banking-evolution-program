"""Pruebas del laboratorio de riesgo de activos digitales (Parte 20).

Cada prueba esta asociada a una afirmacion concreta de una clase. Las que
llevan el sufijo `_documenta_el_problema` deben pasar precisamente porque
reproducen un defecto: sin ellas, el material afirmaria cosas que el codigo no
sostiene.
"""

from __future__ import annotations

import pytest

from apps.digital_assets_risk_lab.algorithmic import (
    SistemaDeDosTokens,
    cobertura_de_hibrido,
    descomponer_rendimiento,
)
from apps.digital_assets_risk_lab.classification import (
    CadenaDeRespaldo,
    Exigibilidad,
    Ficha,
    Obligado,
    Tipo,
    TresElementos,
    clasificar,
    incumplimientos_dinero_electronico,
)
from apps.digital_assets_risk_lab.contagion import Entidad, Grafo
from apps.digital_assets_risk_lab.custody import (
    Esquema,
    Guardian,
    PoliticaDeRetirada,
    Recuperacion,
    Retirada,
)
from apps.digital_assets_risk_lab.depeg import (
    CostesDeArbitraje,
    Episodio,
    Fase,
    VigilanciaDeDesvio,
    arbitraje_rentable,
    banda_de_no_arbitraje,
    recuperacion_corrige_la_causa,
)
from apps.digital_assets_risk_lab.market import (
    Libro,
    Nivel,
    cocientes,
    limite_de_posicion,
    riesgo_de_esperar,
    venta_escalonada,
)
from apps.digital_assets_risk_lab.redemption import (
    Cola,
    Regla,
    solicitud_del_dia_siguiente,
)
from apps.digital_assets_risk_lab.reserves import (
    Cartera,
    TramoDesconocido,
    atender,
    punto_de_no_retorno,
)

# --------------------------------------------------------------------------
# Clase 1 — clasificacion por la promesa
# --------------------------------------------------------------------------


def _ficha_deposito() -> Ficha:
    return Ficha(
        nombre="deposito tokenizado",
        quien_promete=Obligado.BANCO,
        que_promete="un deposito",
        respaldo="balance del banco",
        exigible=Exigibilidad.A_LA_VISTA,
        ante_quien="supervisor y tribunal",
    )


def _ficha_sin_obligado() -> Ficha:
    return Ficha(
        nombre="token con canje interno",
        quien_promete=Obligado.NADIE,
        que_promete="canje por otro token",
        respaldo="otro token del sistema",
        exigible=Exigibilidad.SOLO_CANJE,
        ante_quien="nadie",
    )


def test_la_clasificacion_no_mira_la_red_sino_al_obligado():
    assert clasificar(_ficha_deposito()) is Tipo.DEPOSITO_TOKENIZADO
    assert clasificar(_ficha_sin_obligado()) is Tipo.NO_RESPALDADO


def test_sin_obligado_ni_foro_no_hay_credito():
    assert not _ficha_sin_obligado().hay_credito
    assert _ficha_deposito().hay_credito


def test_el_minimo_de_redencion_convierte_la_paridad_en_privilegio_de_tamano():
    ficha = Ficha(
        nombre="stablecoin con umbral",
        quien_promete=Obligado.EMISOR,
        que_promete="1,00 por unidad",
        respaldo="cartera declarada",
        exigible=Exigibilidad.A_LA_VISTA,
        ante_quien="tribunal",
        umbral_redencion=100_000,
    )
    assert not ficha.derecho_universal

    apta_grande, _ = ficha.apta_para_tesoreria(500_000)
    apta_pequena, motivo = ficha.apta_para_tesoreria(40_000)
    assert apta_grande
    assert not apta_pequena
    assert "minimo de redencion" in motivo


def test_el_respaldo_circular_no_llega_a_ningun_activo_externo():
    cadena = CadenaDeRespaldo()
    cadena.agregar("E", externo=False, respalda_a="V")
    cadena.agregar("V", externo=False, respalda_a="E")

    assert cadena.es_circular("E")
    assert not cadena.llega_a_activo_externo("E")


def test_el_respaldo_exogeno_llega_a_un_activo_externo():
    cadena = CadenaDeRespaldo()
    cadena.agregar("S", externo=False, respalda_a="letras")
    cadena.agregar("letras", externo=True)

    assert not cadena.es_circular("S")
    assert cadena.llega_a_activo_externo("S")


# --------------------------------------------------------------------------
# Clase 9 — dinero electronico: la sustancia manda sobre el nombre
# --------------------------------------------------------------------------


def test_los_tres_elementos_califican_aunque_el_producto_se_llame_token():
    assert TresElementos(True, True, True).es_dinero_electronico
    assert not TresElementos(True, True, False).es_dinero_electronico


def test_los_tres_incumplimientos_de_la_variante_2():
    ficha = Ficha(
        nombre="token estable",
        quien_promete=Obligado.EMISOR,
        que_promete="1,00 por unidad",
        respaldo="cartera",
        exigible=Exigibilidad.CON_UMBRAL,
        ante_quien="tribunal",
        umbral_redencion=50_000,
        remunera=True,
    )
    fallos = incumplimientos_dinero_electronico(ficha)
    assert len(fallos) == 3
    assert any("remunera" in f for f in fallos)
    assert any("minimo" in f for f in fallos)
    assert any("a la vista" in f for f in fallos)


# --------------------------------------------------------------------------
# Clase 4 — la cobertura publicada se mueve al reves que el riesgo
# --------------------------------------------------------------------------


def _cartera() -> Cartera:
    return Cartera(
        circulante=8_400_000_000,
        tramos={
            "efectivo": 840_000_000,
            "letras": 3_010_000_000,
            "deuda_corta": 2_580_000_000,
            "pactos_inversos": 860_000_000,
            "papel_comercial": 945_000_000,
            "deposito_plazo": 358_200_000,
        },
    )


def test_la_cobertura_contable_no_distingue_la_composicion():
    liquida = Cartera(1_000, {"efectivo": 700, "letras": 320})
    ilikida = Cartera(1_000, {"efectivo": 200, "papel_comercial": 820})

    assert liquida.cobertura_contable == pytest.approx(1.02, abs=0.001)
    assert ilikida.cobertura_contable == pytest.approx(1.02, abs=0.001)
    assert liquida.cobertura_liquida > ilikida.cobertura_liquida


def test_un_tramo_sin_descuento_declarado_no_se_puede_valorar():
    with pytest.raises(TramoDesconocido):
        Cartera(1_000, {"activo_exotico": 1_020})


def test_la_cobertura_sube_mientras_la_composicion_empeora_documenta_el_problema():
    """Clase 4, paso 6: la cifra publicada mejora y el riesgo aumenta."""
    cartera = _cartera()
    cobertura_antes = cartera.cobertura_contable
    iliquido_antes = cartera.peso_iliquido

    resultado = atender(cartera, 2_940_000_000)

    assert resultado.cubierta
    assert cartera.cobertura_contable > cobertura_antes  # <- la cifra MEJORA
    assert cartera.peso_iliquido > iliquido_antes  # <- el riesgo EMPEORA
    assert cartera.tramos["efectivo"] == 0


def test_el_coste_de_la_redencion_del_35_por_ciento():
    cartera = _cartera()
    resultado = atender(cartera, 2_940_000_000)
    assert resultado.coste_de_venta == 1_862_794
    assert resultado.coste_relativo == pytest.approx(0.00063, abs=0.00001)


def test_la_escalera_encarece_la_venta_frente_al_descuento_constante():
    constante = _cartera()
    escalonada = _cartera()

    plano = atender(constante, 5_000_000_000).coste_de_venta
    creciente = atender(escalonada, 5_000_000_000, escalera=True).coste_de_venta

    assert creciente > plano


def test_el_punto_de_no_retorno_es_menor_que_el_circulante():
    cartera = _cartera()
    margen = cartera.total - cartera.circulante
    punto = punto_de_no_retorno(cartera, margen)

    assert 0 < punto < cartera.circulante


# --------------------------------------------------------------------------
# Clase 3 — banda de no arbitraje y desvio persistente
# --------------------------------------------------------------------------


def _costes() -> CostesDeArbitraje:
    return CostesDeArbitraje(
        comision_redencion=0.0010,
        coste_financiacion_anual=0.052,
        dias_de_liquidacion=2,
        coste_operacion=12,
        minimo_redencion=100_000,
    )


def test_la_paridad_no_es_un_punto_sino_una_banda():
    bajo, alto = banda_de_no_arbitraje(_costes(), 2_400_000)
    assert bajo == pytest.approx(0.99871, abs=0.00002)
    assert alto == pytest.approx(1.00129, abs=0.00002)


def test_el_arbitraje_de_60_puntos_basicos_es_muy_rentable():
    resultado = arbitraje_rentable(0.9940, _costes(), 2_400_000)
    assert resultado["puede_arbitrar"]
    assert resultado["neto"] == pytest.approx(11_299, abs=5)
    assert resultado["anualizada"] > 0.80


def test_quien_no_alcanza_el_minimo_no_puede_arbitrar():
    resultado = arbitraje_rentable(0.9940, _costes(), 40_000)
    assert not resultado["puede_arbitrar"]
    assert resultado["neto"] == 0.0


def test_el_desvio_persistente_dispara_la_alerta():
    vigilancia = VigilanciaDeDesvio(banda=(0.99871, 1.00129), horas_para_alerta=6)
    for _ in range(5):
        vigilancia.observar(0.9940)
    assert not vigilancia.en_alerta

    vigilancia.observar(0.9940)
    assert vigilancia.en_alerta


def test_volver_a_la_banda_reinicia_el_contador():
    vigilancia = VigilanciaDeDesvio(banda=(0.99871, 1.00129), horas_para_alerta=3)
    for _ in range(5):
        vigilancia.observar(0.9940)
    vigilancia.observar(1.0000)
    assert vigilancia.horas_fuera_de_banda == 0
    assert not vigilancia.en_alerta


# --------------------------------------------------------------------------
# Clase 6 — el canal decide, y la recuperacion no corrige la causa
# --------------------------------------------------------------------------


def test_la_fase_3_decide_si_el_episodio_se_cierra():
    bueno = Episodio("un banco depositario en resolucion")
    bueno.registrar(Fase.DETONANTE, "efectivo atrapado")
    bueno.registrar(Fase.PRUEBA_DEL_CANAL, "el emisor pago: funciono")
    assert bueno.canal_funciono
    assert not bueno.llego_a_realizacion_forzada

    malo = Episodio("dudas sobre las reservas")
    malo.registrar(Fase.DETONANTE, "informe filtrado")
    malo.registrar(Fase.PRUEBA_DEL_CANAL, "la redencion se suspendio")
    malo.registrar(Fase.CARRERA, "todos solicitan")
    malo.registrar(Fase.REALIZACION_FORZADA, "venta con descuento creciente")
    assert not malo.canal_funciono
    assert malo.llego_a_realizacion_forzada


def test_solo_la_reanudacion_de_la_redencion_corrige_la_causa():
    assert recuperacion_corrige_la_causa("se reanudo la redencion")
    for motivo in (
        "liquidez externa del emisor",
        "un tercero compro para sostener",
        "dejo de haber vendedores",
    ):
        assert not recuperacion_corrige_la_causa(motivo)


# --------------------------------------------------------------------------
# Clase 5 — el diseno de la cola crea el incentivo a correr
# --------------------------------------------------------------------------


def _cola(**kwargs) -> Cola:
    cola = Cola(efectivo=900_000_000, coste_de_venta=0.01112, **kwargs)
    for i in range(12_000):
        cola.solicitar(f"t{i}", 150_000, necesita=i % 5 == 0)
    return cola


def test_el_orden_de_llegada_premia_al_primero_documenta_el_problema():
    """Clase 5: la corrida no la causa el panico, la causa la cola."""
    resultado = _cola().resolver(Regla.ORDEN_DE_LLEGADA)
    assert resultado.ventaja_del_primero == pytest.approx(1.0)

    fracciones = [p.fraccion for p in resultado.pagos]
    assert fracciones[0] == pytest.approx(1.0)
    assert fracciones[-1] == pytest.approx(0.0)


def test_el_prorrateo_apaga_la_ventaja_de_ser_primero():
    resultado = _cola().resolver(Regla.PRORRATEO)
    assert resultado.ventaja_del_primero == pytest.approx(0.0, abs=0.001)
    for pago in resultado.pagos:
        assert pago.fraccion == pytest.approx(0.5, abs=0.01)


def test_la_antidilucion_carga_el_coste_a_quien_sale():
    sin = _cola(antidilucion=False).resolver(Regla.PRORRATEO)
    con = _cola(antidilucion=True).resolver(Regla.PRORRATEO)

    assert sin.coste_total == 0
    assert con.coste_total > 0
    assert con.pagos[0].pagado < sin.pagos[0].pagado


def test_el_tramo_minimo_integro_protege_al_pequeno_sin_reabrir_la_carrera():
    cola = Cola(efectivo=900_000_000, tramo_minimo_integro=5_000)
    cola.solicitar("pequeno", 6_000)
    for i in range(11_999):
        cola.solicitar(f"grande{i}", 150_000)

    resultado = cola.resolver(Regla.PRORRATEO)
    pequeno = next(p for p in resultado.pagos if p.tenedor == "pequeno")
    grande = next(p for p in resultado.pagos if p.tenedor == "grande0")

    assert pequeno.pagado >= 5_000
    assert pequeno.fraccion > grande.fraccion
    # El orden entre los grandes sigue sin importar: no hay carrera entre ellos.
    grandes = [p.fraccion for p in resultado.pagos if p.tenedor.startswith("grande")]
    assert max(grandes) - min(grandes) < 0.01


def test_la_solicitud_del_dia_siguiente_depende_de_la_ventaja():
    llegada = _cola().resolver(Regla.ORDEN_DE_LLEGADA)
    prorrateo = _cola(antidilucion=True).resolver(Regla.PRORRATEO)

    manana_llegada = solicitud_del_dia_siguiente(llegada, 0.40, 625_000_000)
    manana_prorrateo = solicitud_del_dia_siguiente(prorrateo, 0.40, 625_000_000)

    assert manana_llegada > 2 * manana_prorrateo


# --------------------------------------------------------------------------
# Clase 7 — el ratio de absorcion es el indicador equivocado
# --------------------------------------------------------------------------


def _sistema() -> SistemaDeDosTokens:
    return SistemaDeDosTokens(
        circulante_e=2_000_000_000, unidades_v=400_000_000, precio_v=3.0
    )


def test_el_ratio_de_absorcion_sube_durante_el_colapso_documenta_el_problema():
    """Clase 7, paso 4: el indicador intuitivo mejora mientras todo se hunde."""
    sistema = _sistema()
    for _ in range(4):
        sistema.canjear(200_000_000)

    ratios = [v.ratio_absorcion for v in sistema.vueltas]
    precios = [v.precio_v_despues for v in sistema.vueltas]

    assert all(b > a for a, b in zip(ratios, ratios[1:]))  # <- SUBE
    assert all(b < a for a, b in zip(precios, precios[1:]))  # <- y V se hunde


def test_la_emision_por_unidad_retirada_si_detecta_la_espiral():
    sistema = _sistema()
    for _ in range(4):
        sistema.canjear(200_000_000)

    assert sistema.espiral_acelera()
    assert sistema.vueltas[0].emision_por_unidad == pytest.approx(0.3333, abs=0.001)
    assert sistema.vueltas[-1].emision_por_unidad > 0.6


def test_una_vuelta_genera_varias_veces_el_volumen_diario():
    sistema = _sistema()
    assert sistema.veces_el_volumen(200_000_000) > 2.0


def test_el_rendimiento_pagado_por_encima_de_los_ingresos_es_dilucion():
    reparto = descomponer_rendimiento(2_000_000_000, 0.12, 42_000_000)
    assert reparto["pagado"] == 240_000_000
    assert reparto["dilucion"] == 198_000_000
    assert reparto["porcentaje_dilucion"] == pytest.approx(0.825, abs=0.001)


def test_la_cobertura_de_un_hibrido_se_calcula_con_el_tramo_endogeno_a_cero():
    cobertura = cobertura_de_hibrido(exogeno=700, endogeno=300, circulante=1_000)
    assert cobertura["en_calma"] == pytest.approx(1.0)
    assert cobertura["en_tension"] == pytest.approx(0.7)


def test_no_se_puede_canjear_contra_un_token_sin_precio():
    sistema = SistemaDeDosTokens(circulante_e=1_000, unidades_v=1_000, precio_v=0.0)
    with pytest.raises(ValueError):
        sistema.canjear(100)


# --------------------------------------------------------------------------
# Clase 12 — custodia: el umbral no dice nada por si solo
# --------------------------------------------------------------------------


def test_un_3_de_5_puede_tener_independencia_efectiva_1_documenta_el_problema():
    """Clase 12, paso 1: cinco guardianes con el mismo dispositivo son uno."""
    esquema = Esquema(
        umbral=3,
        guardianes=[
            Guardian(f"G{i}", "oficina_A", "tipo_X", "cl") for i in range(1, 6)
        ],
    )
    assert esquema.independencia_efectiva() == 1
    assert not esquema.tolera_evento_correlacionado()


def test_redistribuir_las_partes_arregla_el_esquema_sin_tocar_el_umbral():
    esquema = Esquema(
        umbral=3,
        guardianes=[
            Guardian("G1", "oficina_A", "tipo_X", "cl", "interno_1"),
            Guardian("G2", "oficina_B", "tipo_Y", "cl", "interno_2"),
            Guardian("G3", "oficina_C", "tipo_X", "uy", "interno_3"),
            Guardian("G4", "externo_1", "tipo_Z", "pe", "proveedor_ext"),
            Guardian("G5", "externo_2", "tipo_Y", "es", "despacho"),
        ],
    )
    assert esquema.umbral == 3
    assert esquema.tolera_evento_correlacionado()
    assert esquema.independencia_efectiva() == 4


def test_la_probabilidad_de_bloqueo_de_un_3_de_5_es_pequena():
    esquema = Esquema(
        umbral=3,
        guardianes=[
            Guardian(f"G{i}", f"of_{i}", f"tipo_{i}", f"j{i}", f"p{i}")
            for i in range(5)
        ],
    )
    assert esquema.probabilidad_de_bloqueo(0.04) == pytest.approx(0.0006, abs=0.0002)


def test_la_recuperacion_debe_ser_mas_dificil_que_firmar():
    mala = Recuperacion(umbral=3, tenedores=7, retardo_dias=0, umbral_de_firma=3)
    buena = Recuperacion(umbral=4, tenedores=7, retardo_dias=7, umbral_de_firma=3)

    assert len(mala.defectos) == 2
    assert buena.defectos == []


def test_la_lista_blanca_con_espera_detiene_la_sesion_comprometida():
    politica = PoliticaDeRetirada(lista_blanca={"destino_conocido"})
    ataque = Retirada(
        origen_autorizado=True,
        destino_en_lista_blanca=False,
        importe=500_000,
        segunda_aprobacion=False,
    )
    permitida, motivo, horas = politica.evaluar(ataque, "destino_nuevo")

    assert not permitida
    assert horas == 48
    assert "lista blanca" in motivo


def test_el_importe_alto_exige_segunda_aprobacion():
    politica = PoliticaDeRetirada(lista_blanca={"destino_conocido"})
    grande = Retirada(
        origen_autorizado=True,
        destino_en_lista_blanca=True,
        importe=5_000_000,
        segunda_aprobacion=False,
    )
    permitida, motivo, _ = politica.evaluar(grande, "destino_conocido")
    assert not permitida
    assert "segunda aprobacion" in motivo


# --------------------------------------------------------------------------
# Clase 13 — el volumen no es liquidez
# --------------------------------------------------------------------------


def _libro() -> Libro:
    return Libro(
        precio_actual=100.0,
        volumen_diario=184_000_000,
        niveles=[
            Nivel(100.00, 420_000),
            Nivel(99.50, 1_150_000),
            Nivel(99.00, 2_080_000),
            Nivel(98.00, 3_340_000),
            Nivel(96.00, 5_100_000),
            Nivel(93.00, 7_800_000),
            Nivel(88.00, 11_200_000),
        ],
    )


def test_los_dos_cocientes_dan_conclusiones_opuestas_documenta_el_problema():
    """Clase 13: sobre volumen tranquiliza, sobre profundidad dice la verdad."""
    par = cocientes(_libro(), 12_000_000)
    assert par["sobre_volumen"] < 0.07  # parece comodo
    assert par["sobre_profundidad"] > 5.0  # y no lo es


def test_la_profundidad_se_mide_sobre_el_libro():
    libro = _libro()
    assert libro.profundidad(0.01) == 2_080_000
    assert libro.profundidad(0.02) == 3_340_000
    assert libro.profundidad(0.05) == 6_000_000


def test_una_venta_que_agota_el_libro_exige_declarar_el_precio_de_cola():
    with pytest.raises(ValueError):
        _libro().vender(12_000_000)


def test_la_venta_de_golpe_cuesta_casi_el_7_por_ciento():
    resultado = _libro().vender(12_000_000, precio_de_cola=84.0)
    assert resultado["libro_agotado"]
    assert resultado["impacto"] == pytest.approx(0.0695, abs=0.0005)
    assert resultado["perdida"] == pytest.approx(83_355_000, rel=0.001)


def test_escalonar_reduce_el_impacto_pero_expone_al_tiempo():
    escalonada = venta_escalonada(12_000_000, 1_500_000, 0.007, 0.70)
    assert escalonada["sesiones"] == 8
    assert escalonada["impacto"] == pytest.approx(0.0217, abs=0.0005)

    riesgo = riesgo_de_esperar(0.052, escalonada["sesiones"] * 0.5)
    assert riesgo == pytest.approx(0.0212, abs=0.0005)


def test_el_limite_de_posicion_cuelga_de_la_profundidad():
    assert limite_de_posicion(_libro()) == 6_240_000


def test_un_libro_con_acumulado_decreciente_es_invalido():
    with pytest.raises(ValueError):
        Libro(
            precio_actual=100.0,
            niveles=[Nivel(100.0, 500), Nivel(99.0, 300)],
        )


# --------------------------------------------------------------------------
# Clase 14 — exposicion cero y 117 millones de necesidad de liquidez
# --------------------------------------------------------------------------


def _grafo() -> Grafo:
    grafo = Grafo()
    grafo.agregar(Entidad("banco", capital=420_000_000))
    grafo.agregar(
        Entidad("F", capital=120_000_000, posicion_directa=38_000_000,
                proveedor_de_precios="P1")
    )
    grafo.agregar(
        Entidad("D", capital=340_000_000, posicion_directa=105_000_000,
                proveedor_de_precios="P1")
    )
    grafo.agregar(
        Entidad("P", capital=80_000_000, posicion_directa=12_000_000,
                proveedor_de_precios="P1")
    )
    grafo.agregar(
        Entidad("C", capital=210_000_000, custodia_por_terceros=900_000_000)
    )
    grafo.vincular("banco", "F", 42_000_000)
    grafo.vincular("banco", "D", 68_000_000)
    grafo.vincular("banco", "P", 25_000_000)
    grafo.vincular("banco", "C", 180_000_000, tipo="deposito_recibido")
    return grafo


def test_exposicion_cero_con_38_millones_en_riesgo_documenta_el_problema():
    """Clase 14: la cifra que se vigilaba era la unica irrelevante."""
    grafo = _grafo()
    assert grafo.exposicion_directa("banco") == 0
    assert grafo.exposicion_economica("banco") == pytest.approx(38_050_000, rel=0.001)


def test_el_custodio_sin_posicion_propia_no_aporta_exposicion_indirecta():
    indirecta = _grafo().exposicion_indirecta("banco")
    assert "C" not in indirecta


def test_el_custodio_si_aporta_riesgo_de_liquidez():
    cascada = _grafo().cascada("banco", 0.60, 0.40, 0.35)
    assert cascada["depositos_retirados"] == 63_000_000
    assert cascada["lineas_dispuestas"] == 54_000_000
    assert cascada["necesidad_de_liquidez"] == 117_000_000


def test_el_nodo_critico_no_aparece_en_ningun_balance():
    critico = _grafo().nodo_critico()
    assert critico is not None
    clave, afectadas = critico
    assert clave == "proveedor_de_precios:P1"
    assert afectadas == ["D", "F", "P"]


def test_vincular_una_entidad_desconocida_falla():
    grafo = _grafo()
    with pytest.raises(KeyError):
        grafo.vincular("banco", "inexistente", 1_000)
