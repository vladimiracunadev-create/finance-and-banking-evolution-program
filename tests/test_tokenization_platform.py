"""Pruebas de la plataforma de tokenizacion (Parte 21).

Cada prueba esta asociada a una afirmacion concreta de una clase. Las que llevan
el sufijo `_documenta_el_problema` deben pasar precisamente porque reproducen un
defecto: sin ellas, el material afirmaria cosas que el codigo no sostiene.
"""

from __future__ import annotations

import pytest

from apps.tokenization_platform.collateral import (
    Posicion,
    Sistema,
    colchon_implicito,
    recorte,
)
from apps.tokenization_platform.issuance import Emision, Mecanismo
from apps.tokenization_platform.lifecycle import (
    AprovisionamientoInsuficiente,
    EstadoPago,
    Instrumento,
    SinDobleAprobacion,
    Titular,
    coste_de_un_error_de_corte,
)
from apps.tokenization_platform.registry import (
    Causa,
    Configuracion,
    Emisor,
    SaldoCongelado,
    SinAutoridadDeResolucion,
    coste_anual,
    ventana_protege,
)
from apps.tokenization_platform.settlement import (
    RIESGOS,
    Liquidador,
    Motivo,
    NoHayAtomicidad,
    Operacion,
    ahorro_de_la_atomicidad,
    coste_de_liquidez,
    netear,
)

# --------------------------------------------------------------------------
# Clase 2 — el registro de referencia
# --------------------------------------------------------------------------


def test_el_espejo_no_permite_atomicidad_documenta_el_problema():
    """Clase 2: no se puede entregar de forma atomica algo cuya titularidad
    decide otro registro. Un proyecto que promete DvP atomico y mantiene el
    registro oficial como referencia promete lo que su arquitectura impide.
    """
    espejo = Emisor(Configuracion.ESPEJO)
    bloqueo = Emisor(Configuracion.BLOQUEO_DE_ORIGEN)

    assert not espejo.permite_atomicidad
    assert bloqueo.permite_atomicidad


def test_el_bloqueo_de_origen_no_deja_dos_versiones_activas():
    emisor = Emisor(Configuracion.BLOQUEO_DE_ORIGEN)
    emisor.emitir("inv", 1_000)
    emisor.bloquear_y_representar("inv", 400)

    assert emisor.oficial.saldo("inv") == 600
    assert emisor.token.saldo("inv") == 400
    assert emisor.bloqueado["inv"] == 400
    # En cada momento, para cada unidad, solo un registro esta operativo.
    assert emisor.oficial.saldo("inv") + emisor.bloqueado["inv"] == 1_000


def test_el_rescate_devuelve_el_saldo_al_registro_oficial():
    emisor = Emisor(Configuracion.BLOQUEO_DE_ORIGEN)
    emisor.emitir("inv", 1_000)
    emisor.bloquear_y_representar("inv", 400)
    emisor.rescatar("inv", 400)

    assert emisor.oficial.saldo("inv") == 1_000
    assert emisor.token.saldo("inv") == 0


def test_sin_dos_registros_operativos_no_hay_divergencia_estructural():
    emisor = Emisor(Configuracion.BLOQUEO_DE_ORIGEN)
    emisor.emitir("inv", 1_000)
    with pytest.raises(ValueError):
        emisor.provocar_divergencia("inv", Causa.ERROR_OPERATIVO, -10)


def test_la_conciliacion_detecta_la_divergencia_y_la_causa():
    emisor = Emisor(Configuracion.ESPEJO, autoridad_de_resolucion="administrador")
    emisor.emitir("a", 1_000)
    emisor.emitir("b", 500)
    emisor.provocar_divergencia("a", Causa.EVENTO_CORPORATIVO, -40)

    encontradas = emisor.conciliar({"a": Causa.EVENTO_CORPORATIVO})
    assert len(encontradas) == 1
    assert encontradas[0].titular == "a"
    assert encontradas[0].viene_de_fuera


def test_la_congelacion_alcanza_a_los_dos_registros():
    emisor = Emisor(Configuracion.ESPEJO, autoridad_de_resolucion="administrador")
    emisor.emitir("a", 1_000)
    emisor.congelar("a")

    with pytest.raises(SaldoCongelado):
        emisor.oficial.transferir("a", "b", 100)
    with pytest.raises(SaldoCongelado):
        emisor.token.transferir("a", "b", 100)


def test_resolver_sin_autoridad_designada_falla():
    emisor = Emisor(Configuracion.ESPEJO)
    emisor.emitir("a", 1_000)
    emisor.provocar_divergencia("a", Causa.ERROR_OPERATIVO, -40)
    emisor.congelar("a")

    with pytest.raises(SinAutoridadDeResolucion):
        emisor.resolver("a", 1_000)


def test_el_espejo_cuesta_un_orden_de_magnitud_mas():
    espejo = coste_anual(264, 380, 40, 4_200) + 120_384
    bloqueo = 27_900 + 12_600
    assert espejo > 9 * bloqueo


def test_la_ventana_solo_protege_si_es_menor_que_el_intervalo():
    assert ventana_protege(horas_de_conciliacion=1, horas_entre_operaciones=139)
    assert not ventana_protege(horas_de_conciliacion=168, horas_entre_operaciones=139)


# --------------------------------------------------------------------------
# Clase 4 — mercado primario
# --------------------------------------------------------------------------


def _emision(bloqueo: bool = False, tramo: int = 0) -> Emision:
    emision = Emision(
        objetivo=30_000_000,
        minimo=18_000_000,
        tramo_minimo=tramo,
        bloqueo_obligatorio=bloqueo,
    )
    for i in range(6_800):
        emision.ordenar(f"inv{i}", 16_529)
    return emision


def test_el_orden_de_llegada_premia_al_primero_tambien_en_el_primario():
    resultado = _emision().adjudicar(Mecanismo.ORDEN_DE_LLEGADA)
    assert resultado.ventaja_del_primero == pytest.approx(1.0)


def test_el_prorrateo_reparte_por_igual():
    resultado = _emision().adjudicar(Mecanismo.PRORRATEO_SIMPLE)
    assert resultado.ventaja_del_primero == pytest.approx(0.0, abs=0.001)
    assert resultado.adjudicaciones[0].adjudicado == pytest.approx(4_412, abs=2)


def test_el_tramo_minimo_redistribuye_hacia_el_pequeno():
    emision = Emision(objetivo=30_000_000, minimo=18_000_000, tramo_minimo=2_000)
    emision.ordenar("pequeno", 16_529)
    for i in range(6_799):
        emision.ordenar(f"grande{i}", 500_000)

    con_minimo = emision.adjudicar(Mecanismo.PRORRATEO_CON_MINIMO)
    pequeno = next(a for a in con_minimo.adjudicaciones if a.inversionista == "pequeno")
    grande = next(a for a in con_minimo.adjudicaciones if a.inversionista == "grande0")

    assert pequeno.fraccion > grande.fraccion
    assert pequeno.adjudicado >= 2_000


def test_el_bloqueo_del_importe_cuesta_dinero():
    """Clase 4: es lo que convierte exagerar la orden en algo caro."""
    sin = _emision(bloqueo=False)
    con = _emision(bloqueo=True)

    assert sin.coste_del_bloqueo(500_000) == 0.0
    assert con.coste_del_bloqueo(500_000) == pytest.approx(583, abs=2)


def test_la_demanda_genuina_exige_declarar_el_factor():
    emision = _emision()
    assert emision.sobredemanda == pytest.approx(3.746, abs=0.01)
    assert emision.demanda_genuina(2.86) < emision.demanda
    with pytest.raises(ValueError):
        emision.demanda_genuina(0)


def test_la_emision_desierta_no_coloca_nada_y_libera_todo():
    emision = Emision(objetivo=30_000_000, minimo=18_000_000)
    for i in range(100):
        emision.ordenar(f"inv{i}", 150_000)

    resultado = emision.adjudicar(Mecanismo.PRORRATEO_SIMPLE)
    assert resultado.desierta
    assert resultado.colocado == 0
    assert all(a.adjudicado == 0 for a in resultado.adjudicaciones)


# --------------------------------------------------------------------------
# Clase 5 — ciclo de vida
# --------------------------------------------------------------------------


def _bono() -> Instrumento:
    bono = Instrumento(nominal_por_unidad=1_000, unidades=30_000, cupon_anual=0.064)
    for i in range(40):
        bono.registrar(
            Titular(f"t{i}", unidades=750, cuenta_bloqueada=i < 3, localizable=i != 5)
        )
    return bono


def test_sin_aprovisionamiento_no_se_paga_a_nadie_documenta_el_problema():
    """Clase 5: un contrato que paga por orden hasta quedarse sin fondos
    divide a los tenedores en dos grupos sin ningun criterio.
    """
    bono = _bono()
    foto = bono.instantanea("corte")
    necesario = bono.cupon_total(foto)

    with pytest.raises(AprovisionamientoInsuficiente):
        bono.pagar_cupon(foto, necesario - 1)

    # Y nadie cobro: el estado no cambio.
    assert bono.pagos_confirmados == set()


def test_el_cupon_se_paga_contra_la_instantanea():
    bono = _bono()
    foto = bono.instantanea("corte")
    resultado = bono.pagar_cupon(foto, bono.cupon_total(foto))

    assert resultado.importe_por_unidad == 32
    assert resultado.pagado + resultado.pendiente == bono.cupon_total(foto)
    assert resultado.detalle["t0"] is EstadoPago.CUENTA_BLOQUEADA
    assert resultado.detalle["t5"] is EstadoPago.NO_LOCALIZABLE
    assert resultado.detalle["t10"] is EstadoPago.PAGADO


def test_el_inmovilizado_no_pierde_el_derecho_al_cupon():
    bono = _bono()
    bono.inmovilizar("t10", 750, ("operaciones", "cumplimiento"), "orden judicial")
    foto = bono.instantanea("corte")
    resultado = bono.pagar_cupon(foto, bono.cupon_total(foto))

    # El importe queda pendiente, consignado: no se anula.
    assert resultado.detalle["t10"] is EstadoPago.INMOVILIZADO
    assert resultado.pendiente >= 32 * 750


def test_la_inmovilizacion_exige_dos_aprobadores_distintos():
    bono = _bono()
    with pytest.raises(SinDobleAprobacion):
        bono.inmovilizar("t1", 750, ("operaciones", "operaciones"), "orden")


def test_al_vencer_solo_se_destruye_lo_pagado_y_confirmado():
    bono = _bono()
    foto = bono.instantanea("corte")
    bono.pagar_cupon(foto, bono.cupon_total(foto))

    cierre = bono.vencer(bono.pagos_confirmados)
    assert cierre["destruidas"] > 0
    assert cierre["vivas"] > 0  # los no cobrados conservan su instrumento
    assert cierre["destruidas"] + cierre["vivas"] == 40 * 750


def test_corregir_un_error_de_corte_cuesta_mas_que_el_importe():
    resultado = coste_de_un_error_de_corte(46, 214, 32, 85)
    assert resultado["importe_en_disputa"] == 6_848
    assert resultado["coste_de_correccion"] == 7_820
    assert resultado["corregir_cuesta_mas"]


# --------------------------------------------------------------------------
# Clase 8 — entrega contra pago atomica
# --------------------------------------------------------------------------


def _liquidador() -> Liquidador:
    liquidador = Liquidador()
    liquidador.acreditar_valor("vendedor", 1_000)
    liquidador.acreditar_dinero("comprador", 185_000)
    return liquidador


def test_no_existe_estado_intermedio_observable():
    liquidador = _liquidador()
    antes = liquidador.observar()
    liquidador.liquidar(Operacion("op", "vendedor", "comprador", 1_000, 185_000))
    despues = liquidador.observar()

    # Solo hay dos estados: el de antes y el de despues. En ninguno se movio
    # un tramo sin el otro.
    assert antes["valores"]["vendedor"] == 1_000
    assert antes["dinero"].get("vendedor", 0) == 0
    assert despues["valores"]["vendedor"] == 0
    assert despues["dinero"]["vendedor"] == 185_000
    assert despues["valores"]["comprador"] == 1_000
    assert despues["dinero"]["comprador"] == 0


def test_el_fallo_del_tramo_de_dinero_deja_el_valor_intacto():
    liquidador = Liquidador()
    liquidador.acreditar_valor("v", 1_000)
    resultado = liquidador.liquidar(Operacion("op", "v", "c", 1_000, 185_000))

    assert not resultado.ejecutada
    assert resultado.motivo is Motivo.SIN_DINERO
    assert liquidador.valores["v"] == 1_000  # nada se bloqueo


def test_el_fallo_del_tramo_de_valor_deja_el_dinero_intacto():
    liquidador = Liquidador()
    liquidador.acreditar_dinero("c", 185_000)
    resultado = liquidador.liquidar(Operacion("op", "v", "c", 1_000, 185_000))

    assert not resultado.ejecutada
    assert resultado.motivo is Motivo.SIN_VALOR
    assert liquidador.dinero["c"] == 185_000


def test_dos_operaciones_sobre_el_mismo_saldo_no_se_ejecutan_ambas():
    liquidador = _liquidador()
    liquidador.acreditar_dinero("c2", 185_000)

    primera = liquidador.liquidar(
        Operacion("op1", "vendedor", "comprador", 1_000, 185_000)
    )
    segunda = liquidador.liquidar(Operacion("op2", "vendedor", "c2", 1_000, 185_000))

    assert primera.ejecutada
    assert not segunda.ejecutada
    assert segunda.motivo is Motivo.SIN_VALOR


def test_sin_el_dinero_en_el_registro_el_liquidador_se_niega():
    """Clase 8: la condicion sin la cual no puede haber atomicidad."""
    liquidador = Liquidador(dinero_en_el_registro=False)
    assert not liquidador.permite_atomicidad
    with pytest.raises(NoHayAtomicidad):
        liquidador.liquidar(Operacion("op", "v", "c", 1_000, 185_000))


def test_un_registro_detenido_rechaza_sin_tocar_nada():
    liquidador = _liquidador()
    liquidador.detenido = True
    resultado = liquidador.liquidar(
        Operacion("op", "vendedor", "comprador", 1_000, 185_000)
    )

    assert resultado.motivo is Motivo.REGISTRO_DETENIDO
    assert liquidador.valores["vendedor"] == 1_000


def test_el_neteo_compensa_el_ciclo_en_saldos():
    operaciones = [
        Operacion("1", "a", "b", 100, 18_500),
        Operacion("2", "b", "a", 60, 11_100),
        Operacion("3", "a", "c", 40, 7_400),
    ]
    saldos = netear(operaciones)
    assert saldos["valores"]["a"] == -80
    assert saldos["valores"]["b"] == 40
    assert saldos["valores"]["c"] == 40
    assert sum(saldos["valores"].values()) == 0
    assert sum(saldos["dinero"].values()) == 0


def test_el_neteo_reduce_el_coste_de_liquidez_pero_el_ahorro_no_cambia():
    ahorro = ahorro_de_la_atomicidad(444_000_000, 2, 0.00004, 0.45)
    bruto = coste_de_liquidez(444_000_000, 0.22 - 0.06, 0.043)
    neteado = coste_de_liquidez(444_000_000, 0.09 - 0.06, 0.043)

    assert ahorro == pytest.approx(4_884_000, rel=0.001)
    assert neteado < bruto
    assert ahorro - neteado > ahorro - bruto


def test_la_atomicidad_elimina_exactamente_un_riesgo_de_cinco():
    eliminados = [k for k, v in RIESGOS.items() if v.startswith("lo elimina")]
    assert len(RIESGOS) == 5
    assert eliminados == ["principal"]


# --------------------------------------------------------------------------
# Clase 14 — colateral y cascada
# --------------------------------------------------------------------------


def test_el_recorte_y_el_colchon_cubren_momentos_distintos():
    r = recorte(0.018, 2.33, 0.0015, 0.0005)
    c = colchon_implicito(1.50, 1.20)

    assert r == pytest.approx(0.0439, abs=0.0005)
    assert c == pytest.approx(0.20, abs=0.001)
    assert c > r  # y confundirlos lleva a creer que sobra garantia


def _sistema(parcial: bool) -> Sistema:
    sistema = Sistema(precio=1.0, liquidacion_parcial=parcial)
    for i in range(340):
        ratio = 1.15 + i * 0.0035
        sistema.agregar(
            Posicion(f"p{i}", prestamo=352_941, colateral_unidades=round(352_941 * ratio))
        )
    return sistema


def test_liquidar_posiciones_enteras_produce_cascada_documenta_el_problema():
    """Clase 14: lo que rompe el sistema no es el recorte, es vender entero
    contra un mercado menos profundo que el volumen a liquidar.
    """
    entera = _sistema(parcial=False)
    entera.cascada(0.12)

    assert len(entera.vueltas) >= 5
    assert entera.vueltas[0].impacto > 0.05


def test_la_liquidacion_parcial_apaga_la_cascada():
    parcial = _sistema(parcial=True)
    parcial.cascada(0.12)

    entera = _sistema(parcial=False)
    entera.cascada(0.12)

    assert len(parcial.vueltas) < len(entera.vueltas)
    assert parcial.vueltas[0].volumen_vendido < entera.vueltas[0].volumen_vendido


def test_la_pausa_detiene_la_cascada_antes_de_empezar():
    sistema = _sistema(parcial=False)
    sistema.pausa_si_cae_mas_de = 0.08
    sistema.cascada(0.12)

    assert sistema.pausado
    assert sistema.vueltas[0].liquidadas == 0


def test_el_volumen_forzado_crece_con_la_caida_inicial():
    """El detonante decide si la cascada arranca con fuerza o se apaga sola."""
    pequena = _sistema(parcial=False)
    pequena.cascada(0.03)

    grande = _sistema(parcial=False)
    grande.cascada(0.12)

    assert grande.vueltas[0].liquidadas > pequena.vueltas[0].liquidadas
    assert grande.vueltas[0].impacto > pequena.vueltas[0].impacto
