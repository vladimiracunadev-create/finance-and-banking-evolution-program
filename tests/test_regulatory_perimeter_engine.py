"""Pruebas del motor de perimetro regulatorio (Parte 22).

Cada prueba esta asociada a una afirmacion concreta de una clase. Las que llevan
el sufijo `_documenta_el_problema` deben pasar precisamente porque reproducen un
error de razonamiento que el material persigue.
"""

from __future__ import annotations

import pytest

from apps.regulatory_perimeter_engine.compliance import (
    MapaDeTerceros,
    Salvaguarda,
    Vigilancia,
    justifica_el_indicador,
)
from apps.regulatory_perimeter_engine.dossier import (
    PIEZAS,
    AfirmacionSinEvidencia,
    Expediente,
    Nivel,
)
from apps.regulatory_perimeter_engine.perimeter import (
    SIEMPRE_APLICAN,
    Entidad,
    Regimen,
    informe,
)
from apps.regulatory_perimeter_engine.qualification import (
    Calificacion,
    Instrumento,
    coste_de_una_recalificacion,
)

# --------------------------------------------------------------------------
# Clase 1 — el perimetro lo determinan los hechos
# --------------------------------------------------------------------------


def _plataforma() -> Entidad:
    entidad = Entidad("plataforma")
    for clave, fuente in (
        ("recibe_fondos", "condiciones 4.1"),
        ("obligacion_de_devolver", "condiciones 4.3"),
        ("tiene_las_claves", "documentacion tecnica"),
        ("casa_ordenes_de_terceros", "manual de usuario"),
        ("ejecuta_por_cuenta_ajena", "condiciones 7.2"),
        ("destaca_instrumentos", "captura del 2026-08-06"),
        ("cobra_por_destacar", "tarifario 2026"),
        ("convierte_moneda_con_margen", "tarifario 2026"),
        ("presta_fondos", "condiciones 9.1"),
    ):
        entidad.observar(clave, clave.replace("_", " "), fuente)
    return entidad


def test_una_entidad_puede_ejercer_siete_regimenes_sin_declarar_ninguno():
    """Clase 1: no declarar una actividad no la desactiva."""
    entidad = _plataforma()
    assert entidad.declarados == set()
    assert len(entidad.efectivos()) == 7
    assert entidad.no_declarados() == entidad.efectivos()


def test_tener_las_claves_activa_la_custodia_aunque_se_declare_lo_contrario():
    entidad = _plataforma()
    entidad.declarar(Regimen.MERCADO)  # declara mercado y niega custodia
    assert Regimen.CUSTODIA in entidad.efectivos()
    assert Regimen.CUSTODIA in entidad.no_declarados()


def test_un_hecho_sin_fuente_no_es_observable_documenta_el_problema():
    """Clase 1: lo que decide no es lo que la entidad dice, y una afirmacion
    sin fuente es una declaracion disfrazada de hecho.
    """
    entidad = Entidad("x")
    with pytest.raises(ValueError):
        entidad.observar("tiene_las_claves", "las tiene", fuente="")


def test_la_asesoria_exige_dos_hechos_juntos():
    entidad = Entidad("x")
    entidad.observar("destaca_instrumentos", "portada", "captura")
    assert Regimen.ASESORIA not in entidad.efectivos()

    entidad.observar("cobra_por_destacar", "tarifa", "tarifario")
    assert Regimen.ASESORIA in entidad.efectivos()


def test_cada_regimen_activado_tiene_su_evidencia():
    entidad = _plataforma()
    for regimen in entidad.efectivos():
        evidencia = entidad.evidencia(regimen)
        assert evidencia
        assert all(h.fuente for h in evidencia)


def test_aunque_no_se_active_ningun_regimen_siguen_aplicando_cinco_normas():
    vacia = Entidad("sin actividad")
    resultado = informe(vacia)
    assert resultado["hecho"] == {}
    assert len(resultado["siempre_aplican"]) == len(SIEMPRE_APLICAN)


def test_declarar_lo_que_no_se_ejerce_tambien_se_detecta():
    entidad = Entidad("x")
    entidad.declarar(Regimen.CREDITO)
    assert entidad.declarados_sin_ejercer() == {Regimen.CREDITO}


# --------------------------------------------------------------------------
# Clase 3 — la calificacion no la elige quien emite
# --------------------------------------------------------------------------


def _token_de_logistica(**cambios) -> Instrumento:
    base = dict(
        nombre="token de logistica",
        servicio_en_funcionamiento=False,
        se_consume_al_usarlo=True,
        mercado_secundario_desde_el_inicio=True,
        financia_el_desarrollo=True,
        promocion=[
            "El token da acceso a la plataforma.",
            "A medida que crezca la red, la demanda del token aumentara.",
        ],
        compradores_que_usan_el_servicio=0.08,
    )
    base.update(cambios)
    return Instrumento(**base)


def test_los_cuatro_criterios_califican_como_valor():
    criterios = _token_de_logistica().criterios()
    assert criterios.cuantos == 4
    assert criterios.probablemente_valor
    assert _token_de_logistica().calificar() is Calificacion.VALOR


def test_la_promocion_forma_parte_de_la_calificacion_documenta_el_problema():
    """Clase 3: el mismo instrumento es utilidad o valor segun como se venda,
    y no hace falta prometer rentabilidad: basta con crear la expectativa.
    """
    con_frase = _token_de_logistica()
    sin_frase = _token_de_logistica(
        promocion=["El token da acceso a la plataforma."],
        compradores_que_usan_el_servicio=0.9,
    )

    assert con_frase.criterios().expectativa_de_beneficio
    assert not sin_frase.criterios().expectativa_de_beneficio
    assert len(con_frase.frases_que_crean_expectativa()) == 1


def test_el_servicio_que_no_funciona_hoy_hace_la_utilidad_aparente():
    assert _token_de_logistica().utilidad_aparente

    real = _token_de_logistica(
        servicio_en_funcionamiento=True,
        financia_el_desarrollo=False,
        mercado_secundario_desde_el_inicio=False,
    )
    assert not real.utilidad_aparente


def test_una_utilidad_genuina_se_califica_como_tal():
    genuina = Instrumento(
        nombre="acceso",
        servicio_en_funcionamiento=True,
        se_consume_al_usarlo=True,
        mercado_secundario_desde_el_inicio=False,
        financia_el_desarrollo=False,
        promocion=["Da acceso al servicio de seguimiento."],
        compradores_que_usan_el_servicio=0.94,
    )
    assert genuina.calificar() is Calificacion.UTILIDAD


def test_el_dinero_electronico_exige_emisor_autorizado_y_reembolso():
    saldo = Instrumento(
        nombre="saldo prepago",
        servicio_en_funcionamiento=True,
        se_consume_al_usarlo=False,
        mercado_secundario_desde_el_inicio=False,
        financia_el_desarrollo=False,
        emitido_contra_fondos=True,
        derecho_de_reembolso_a_la_par=True,
        emisor_autorizado=True,
        compradores_que_usan_el_servicio=1.0,
    )
    assert saldo.calificar() is Calificacion.DINERO_ELECTRONICO


def test_el_ahorro_de_calificar_mal_es_una_fraccion_del_riesgo():
    coste = coste_de_una_recalificacion(30_000_000, 400_000, Calificacion.VALOR)
    assert coste["ahorro"] == 340_000
    assert coste["riesgo"] == 30_400_000
    assert coste["ahorro_sobre_riesgo"] == pytest.approx(0.011, abs=0.001)


# --------------------------------------------------------------------------
# Clase 6 — la salvaguarda falla siempre en la misma pregunta
# --------------------------------------------------------------------------


def _salvaguarda(**cambios) -> Salvaguarda:
    base = dict(
        a_nombre_de_clientes=True,
        contrato_especifico=True,
        renuncia_a_compensar=False,
        conciliacion_diaria=False,
        saldo_de_clientes=68_000_000,
        deuda_con_el_banco=4_200_000,
        diferencia_de_conciliacion=900_000,
    )
    base.update(cambios)
    return Salvaguarda(**base)


def test_la_salvaguarda_falla_en_la_renuncia_a_compensar_documenta_el_problema():
    """Clase 6: cuenta segregada y contrato especifico no bastan; sin renuncia
    expresa del banco a compensar, la proteccion se evapora.
    """
    salvaguarda = _salvaguarda()
    assert not salvaguarda.acreditada
    assert "renuncia_a_compensar" in salvaguarda.fallos()

    exposicion = salvaguarda.exposicion()
    assert exposicion["por_compensacion"] == 4_200_000
    assert exposicion["recuperable"] == 62_900_000


def test_con_las_cuatro_preguntas_resueltas_no_hay_exposicion():
    salvaguarda = _salvaguarda(renuncia_a_compensar=True, conciliacion_diaria=True)
    assert salvaguarda.acreditada
    exposicion = salvaguarda.exposicion()
    assert exposicion["por_compensacion"] == 0
    assert exposicion["por_conciliacion"] == 0
    assert exposicion["recuperable"] == 68_000_000


# --------------------------------------------------------------------------
# Clase 11 — decide el coste marginal, no el medio
# --------------------------------------------------------------------------


def _vigilancia() -> Vigilancia:
    return Vigilancia(alertas=3_640, confirmados=44, casos_reales=62,
                      coste_por_alerta=18)


def test_precision_y_exhaustividad_se_calculan_por_separado():
    v = _vigilancia()
    assert v.precision == pytest.approx(0.0121, abs=0.0005)
    assert v.exhaustividad == pytest.approx(0.7097, abs=0.0005)
    assert v.coste == 65_520


def test_el_indicador_nuevo_empeora_la_precision_y_mejora_la_exhaustividad():
    antes = _vigilancia()
    despues = antes.con_indicador(alertas_extra=940, confirmados_extra=9)

    assert despues.precision < antes.precision
    assert despues.exhaustividad > antes.exhaustividad
    assert despues.exhaustividad == pytest.approx(0.8548, abs=0.0005)


def test_el_coste_marginal_supera_al_medio_y_aun_asi_se_justifica():
    """Clase 11: decidir con el coste medio invierte la conclusion."""
    antes = _vigilancia()
    despues = antes.con_indicador(alertas_extra=940, confirmados_extra=9)
    decision = justifica_el_indicador(antes, despues, valor_de_un_caso=45_000)

    assert decision["coste_marginal_por_caso"] > decision["coste_medio_por_caso"]
    assert decision["se_justifica"]


def test_sin_casos_extra_el_indicador_no_se_justifica():
    antes = _vigilancia()
    igual = antes.con_indicador(alertas_extra=500, confirmados_extra=0)
    decision = justifica_el_indicador(antes, igual, valor_de_un_caso=45_000)
    assert not decision["se_justifica"]


# --------------------------------------------------------------------------
# Clase 14 — contar proveedores da diversificacion aparente
# --------------------------------------------------------------------------


def _mapa() -> MapaDeTerceros:
    mapa = MapaDeTerceros()
    mapa.registrar("p1", "C")
    mapa.registrar("p2", "C")
    mapa.registrar("p3", "D")
    for i in range(19):
        mapa.depende(f"e{i}", "p1" if i % 2 == 0 else "p2")
    for i in range(19, 22):
        mapa.depende(f"e{i}", "p3")
    return mapa


def test_contar_proveedores_oculta_la_concentracion_documenta_el_problema():
    """Clase 14: 41 proveedores sobre 3 infraestructuras es diversificacion
    aparente, y el riesgo no esta en el perimetro de ninguna entidad.
    """
    mapa = _mapa()
    por_proveedor = mapa.concentracion_por_proveedor()
    por_infraestructura = mapa.concentracion_por_infraestructura()

    assert max(por_proveedor.values()) < 0.50  # ninguno parece critico
    assert por_infraestructura["C"] == pytest.approx(0.864, abs=0.005)


def test_el_umbral_de_designacion_se_aplica_sobre_infraestructuras():
    mapa = _mapa()
    assert mapa.criticos(0.40) == ["C"]
    assert mapa.criticos(0.90) == []


def test_depender_de_un_proveedor_desconocido_falla():
    mapa = MapaDeTerceros()
    with pytest.raises(KeyError):
        mapa.depende("e1", "inexistente")


# --------------------------------------------------------------------------
# Clase 18 — las contradicciones aparecen al cruzar
# --------------------------------------------------------------------------


def _expediente() -> Expediente:
    expediente = Expediente("entidad", clientes=42_000)
    for pieza in PIEZAS:
        expediente.afirmar(pieza, f"seccion {pieza}", f"doc-{pieza}.pdf")
    return expediente


def test_una_afirmacion_sin_evidencia_se_rechaza():
    expediente = Expediente("entidad", clientes=100)
    with pytest.raises(AfirmacionSinEvidencia):
        expediente.afirmar("perimetro", "no custodiamos", evidencia="")


def test_el_expediente_incompleto_no_permite_operar():
    expediente = Expediente("entidad", clientes=100)
    expediente.afirmar("perimetro", "seccion", "doc.pdf")
    puede, motivo = expediente.puede_operar()
    assert not puede
    assert "faltan piezas" in motivo


def test_un_bloqueante_sin_remediar_impide_operar():
    expediente = _expediente()
    expediente.registrar_hallazgo(
        Nivel.BLOQUEANTE, ("perimetro", "resiliencia"), "custodia no declarada", 42_000
    )
    puede, motivo = expediente.puede_operar()
    assert not puede
    assert "bloqueante" in motivo


def test_los_hallazgos_se_ordenan_por_efecto_sobre_el_cliente():
    expediente = _expediente()
    expediente.registrar_hallazgo(Nivel.ORDINARIO, ("prudencial", "autorizacion"),
                                  "documentacion mejorable", 42_000)
    expediente.registrar_hallazgo(Nivel.BLOQUEANTE, ("salvaguarda", "prevencion_de_lavado"),
                                  "fondos no segregados", 11_000)
    expediente.registrar_hallazgo(Nivel.BLOQUEANTE, ("perimetro", "resiliencia"),
                                  "custodia no declarada", 42_000)

    orden = expediente.priorizados()
    assert orden[0].descripcion == "custodia no declarada"
    assert orden[1].descripcion == "fondos no segregados"
    assert orden[2].nivel is Nivel.ORDINARIO


def test_si_todo_es_ordinario_la_revision_no_miro_donde_debia():
    expediente = _expediente()
    expediente.registrar_hallazgo(Nivel.ORDINARIO, ("prudencial", "autorizacion"),
                                  "documentacion mejorable", 42_000)
    assert not expediente.revision_miro_donde_debia


def test_la_remediacion_exige_medida_provisional_documenta_el_problema():
    """Clase 18: entre que se detecta y se corrige hay un intervalo, y el
    cliente esta expuesto durante ese intervalo.
    """
    expediente = _expediente()
    with pytest.raises(ValueError):
        expediente.remediar(
            hallazgo="custodia no declarada",
            correccion="solicitar autorizacion",
            responsable="cumplimiento",
            plazo_dias=60,
            verificacion="resolucion del supervisor",
            medida_provisional="",
        )


def test_con_remediacion_completa_el_expediente_permite_operar():
    expediente = _expediente()
    expediente.registrar_hallazgo(
        Nivel.BLOQUEANTE, ("perimetro", "resiliencia"), "custodia no declarada", 42_000
    )
    expediente.remediar(
        hallazgo="custodia no declarada",
        correccion="solicitar autorizacion de custodia",
        responsable="direccion de cumplimiento",
        plazo_dias=60,
        verificacion="resolucion del supervisor",
        medida_provisional="no admitir clientes nuevos para ese servicio",
    )
    puede, _ = expediente.puede_operar()
    assert puede
