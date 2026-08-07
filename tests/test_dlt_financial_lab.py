"""Pruebas del laboratorio de registro distribuido de la Parte 19.

Varias de estas pruebas DEBEN pasar aunque documenten un defecto: son las que
demuestran que el encadenamiento no basta, que un fallo comun rompe el umbral y
que la reentrada vacia un contrato. Sin ellas, el material afirma cosas que el
codigo no sostiene.
"""

from decimal import Decimal
from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from apps.dlt_financial_lab.chain import (  # noqa: E402
    Cadena,
    Transaccion,
    TransaccionInvalida,
)
from apps.dlt_financial_lab.consensus import (  # noqa: E402
    Comportamiento,
    Nodo,
    Red,
    independencia_efectiva,
)
from apps.dlt_financial_lab.contracts import (  # noqa: E402
    ContratoDetenido,
    Escrow,
    EstadoIlegal,
    Interruptor,
)
from apps.dlt_financial_lab.crypto import (  # noqa: E402
    LARGO_DIRECCION,
    derivar_direccion,
    direccion_valida,
    firmar,
    generar_par,
    verificar,
)
from apps.dlt_financial_lab.merkle import ArbolMerkle  # noqa: E402
from apps.dlt_financial_lab.oracle import (  # noqa: E402
    Lectura,
    Oraculo,
    SinFuentesSuficientes,
    fuentes_para_mover,
)
from apps.dlt_financial_lab.signatures import (  # noqa: E402
    EsquemaMultifirma,
    Guardian,
    analizar_correlacion,
)


# ---------------------------------------------------------------- cadena


@pytest.fixture()
def cadena():
    c = Cadena(dificultad=0, cada=10)
    par_a, par_b = generar_par(), generar_par()
    c.registrar_clave("acc_a", par_a)
    c.registrar_clave("acc_b", par_b)
    c.acreditar("acc_a", 1_000_000)
    c.claves_prueba = {"acc_a": par_a, "acc_b": par_b}  # type: ignore[attr-defined]
    return c


def _tx(cadena, origen, destino, importe, orden):
    par = cadena.claves[origen]
    return Transaccion(origen, destino, importe, orden).firmar_con(par)


def test_la_cadena_valida_de_extremo_a_extremo(cadena):
    for i in range(20):
        cadena.anadir_bloque([_tx(cadena, "acc_a", "acc_b", 100, i)])
    assert cadena.validar()


def test_una_transaccion_repetida_se_rechaza(cadena):
    tx = _tx(cadena, "acc_a", "acc_b", 500, 0)
    cadena.anadir_bloque([tx])
    with pytest.raises(TransaccionInvalida):
        cadena.aplicar(tx)


def test_una_firma_de_otra_cuenta_no_sirve(cadena):
    tx = Transaccion("acc_a", "acc_b", 100, 0).firmar_con(cadena.claves["acc_b"])
    with pytest.raises(TransaccionInvalida):
        cadena.aplicar(tx)


def test_manipular_sin_recalcular_se_detecta(cadena):
    for i in range(10):
        cadena.anadir_bloque([_tx(cadena, "acc_a", "acc_b", 100, i)])
    cadena.bloques[4].transacciones[0].importe = 999_999
    assert not cadena.validar()


def test_recalcular_toda_la_cadena_NO_se_detecta(cadena):
    """Clase 1 y laboratorio 1: el encadenamiento no impide reescribir.

    Esta prueba DEBE pasar. Documenta que la inmutabilidad la dan el consenso
    y el coste de rehacer, no el encadenamiento.
    """
    for i in range(10):
        cadena.anadir_bloque([_tx(cadena, "acc_a", "acc_b", 100, i)])
    cadena.bloques[4].transacciones[0].importe = 999_999
    assert not cadena.validar()

    cadena.recalcular_desde(4)
    assert cadena.validar()


def test_el_coste_de_rehacer_crece_con_la_dificultad():
    rapida, lenta = Cadena(dificultad=0), Cadena(dificultad=2)
    for c in (rapida, lenta):
        par = generar_par()
        c.registrar_clave("acc_a", par)
        c.acreditar("acc_a", 1_000_000)
        for i in range(5):
            c.anadir_bloque([_tx(c, "acc_a", "acc_b", 10, i)])
    assert lenta.recalcular_desde(1) > rapida.recalcular_desde(1)


def test_el_estado_pasado_se_reconstruye_con_instantaneas(cadena):
    for i in range(25):
        cadena.anadir_bloque([_tx(cadena, "acc_a", "acc_b", 100, i)])
    estado = cadena.estado_en(15)
    assert estado["acc_b"] == 15 * 100


# ------------------------------------------------------------ criptografia


def test_un_mensaje_alterado_invalida_la_firma():
    par = generar_par()
    firma = firmar(par, b"transferir 1000 a acc_02")
    assert verificar(par, b"transferir 1000 a acc_02", firma)
    assert not verificar(par, b"transferir 9000 a acc_02", firma)


def test_una_direccion_valida_se_reconoce():
    par = generar_par()
    assert direccion_valida(derivar_direccion(par.publica))


def test_toda_direccion_tiene_el_mismo_largo_documenta_el_problema():
    """Clase 3: la codificacion de longitud variable perdia el byte inicial
    cuando valia cero, y una de cada doscientas cincuenta y seis direcciones se
    generaba bien y no validaba. Con longitud fija no puede volver a ocurrir.
    """
    for _ in range(1000):
        direccion = derivar_direccion(generar_par().publica)
        assert len(direccion) == LARGO_DIRECCION
        assert direccion_valida(direccion)


def test_un_cuerpo_que_empieza_por_cero_va_y_vuelve():
    from apps.dlt_financial_lab.crypto import _codificar, _decodificar

    cuerpo = bytes([0]) + bytes(range(1, 20))
    assert _decodificar(_codificar(cuerpo), 20) == cuerpo


def test_una_direccion_mal_tecleada_se_detecta():
    par = generar_par()
    direccion = derivar_direccion(par.publica)
    con_error = direccion[:-3] + "xyz"
    assert con_error != direccion
    assert not direccion_valida(con_error)


# ------------------------------------------------------------------ merkle


@pytest.fixture()
def arbol():
    a = ArbolMerkle()
    for i in range(1, 1001):
        a.agregar(f"cuenta_{i:05d}", i * 10)
    return a


def test_la_prueba_de_inclusion_verifica(arbol):
    prueba = arbol.probar("cuenta_00500")
    assert ArbolMerkle.verificar(prueba, arbol.raiz())


def test_la_prueba_de_inclusion_es_logaritmica(arbol):
    prueba = arbol.probar("cuenta_00500")
    assert len(prueba.camino) <= 11  # log2(1000) ~ 10


def test_una_prueba_alterada_no_verifica(arbol):
    prueba = arbol.probar("cuenta_00500")
    falsa = type(prueba)(prueba.clave, prueba.valor + 1, prueba.camino)
    assert not ArbolMerkle.verificar(falsa, arbol.raiz())


def test_la_prueba_de_exclusion_demuestra_la_ausencia(arbol):
    prueba = arbol.probar_exclusion("cuenta_00500x")
    assert ArbolMerkle.verificar_exclusion(prueba, arbol.raiz())


def test_no_se_puede_probar_la_exclusion_de_algo_presente(arbol):
    with pytest.raises(ValueError):
        arbol.probar_exclusion("cuenta_00500")


def test_la_raiz_declara_el_total(arbol):
    assert arbol.total() == sum(arbol.hojas.values())


def test_omitir_una_hoja_cambia_el_total(arbol):
    total_original = arbol.total()
    del arbol.hojas["cuenta_00500"]
    assert arbol.total() == total_original - 5000


def test_una_hoja_negativa_reduce_el_total_sin_omitir(arbol):
    total_original = arbol.total()
    arbol.agregar("cuenta_zzzzz", -5000)
    assert arbol.total() == total_original - 5000


# --------------------------------------------------------------- consenso


def _red(n: int, mentirosos: int = 0, defecto_comun: int = 0) -> Red:
    nodos = []
    for i in range(n):
        if i < mentirosos:
            comportamiento = Comportamiento.MENTIROSO
        elif i < mentirosos + defecto_comun:
            comportamiento = Comportamiento.DEFECTO_COMUN
        else:
            comportamiento = Comportamiento.HONESTO
        nodos.append(Nodo(f"n{i}", comportamiento))
    return Red(nodos)


def test_el_umbral_se_calcula_desde_el_numero_de_nodos():
    assert _red(4).f == 1
    assert _red(7).f == 2
    assert _red(10).f == 3


def test_con_f_mentirosos_hay_acuerdo():
    resultado = _red(4, mentirosos=1).ejecutar_ronda()
    assert resultado.decidido


def test_con_mas_de_f_mentirosos_no_hay_acuerdo():
    resultado = _red(4, mentirosos=2).ejecutar_ronda()
    assert not resultado.decidido


def test_sin_quorum_los_honestos_no_divergen():
    """Clase 1: en finanzas se prefiere detenerse a divergir."""
    red = _red(4, mentirosos=2)
    red.ejecutar_ronda()
    assert len(red.estados_honestos()) == 1


def test_un_fallo_comun_produce_acuerdo_erroneo():
    """Clase 5: el umbral no cubre software que se equivoca igual.

    Esta prueba DEBE pasar. Es el hallazgo de la parte.
    """
    resultado = _red(5, defecto_comun=3).ejecutar_ronda()
    assert resultado.decidido
    assert resultado.valor == "valor_incorrecto"


def test_los_mensajes_crecen_de_forma_cuadratica():
    for n in (4, 7, 10):
        red = _red(n)
        red.ejecutar_ronda()
        assert red.mensajes_ultima_ronda == n * n


def test_la_independencia_efectiva_no_es_el_numero_de_nodos():
    nodos = [
        Nodo("n1", implementacion="A", operador="banco1", jurisdiccion="CL"),
        Nodo("n2", implementacion="A", operador="banco2", jurisdiccion="CL"),
        Nodo("n3", implementacion="A", operador="banco3", jurisdiccion="CL"),
        Nodo("n4", implementacion="B", operador="banco4", jurisdiccion="PE"),
        Nodo("n5", implementacion="B", operador="banco5", jurisdiccion="PE"),
    ]
    analisis = independencia_efectiva(nodos)
    assert analisis["por_implementacion"] == 3
    assert analisis["por_jurisdiccion"] == 3


# ---------------------------------------------------------------- contratos


def _escrow(orden_correcto: bool) -> Escrow:
    contrato = Escrow(verificador="verif", orden_correcto=orden_correcto)
    contrato.depositar("op1", "importador", 28_000_000)
    return contrato


def test_una_transicion_ilegal_se_rechaza():
    contrato = _escrow(True)
    contrato.confirmar("op1", "verif", "exportador")
    with pytest.raises(EstadoIlegal):
        contrato.confirmar("op1", "verif", "exportador")


def test_solo_el_verificador_confirma():
    contrato = _escrow(True)
    with pytest.raises(PermissionError):
        contrato.confirmar("op1", "cualquiera", "exportador")


class BeneficiarioMalicioso:
    """Vuelve a entrar mientras el saldo aun no se ha puesto a cero."""

    def __init__(self, contrato: Escrow, direccion: str) -> None:
        self.contrato = contrato
        self.direccion = direccion
        self.reentradas = 0

    def recibir(self, importe: int) -> None:
        if self.reentradas >= 40:
            return
        if self.contrato.saldos.get(f"beneficiario:{self.direccion}", 0) >= importe:
            self.reentradas += 1
            self.contrato.retirar(self.direccion)


def test_el_ataque_de_reentrada_vacia_el_contrato_defectuoso():
    """Clase 8: el orden incorrecto permite vaciar el contrato.

    Esta prueba DEBE pasar. Documenta el defecto que la siguiente corrige.
    """
    contrato = Escrow(verificador="verif", orden_correcto=False)
    contrato.acreditar_beneficiario("atacante", 180_000)
    atacante = BeneficiarioMalicioso(contrato, "atacante")
    contrato.registrar_receptor(atacante)

    contrato.retirar("atacante")
    assert atacante.reentradas > 0


def test_tras_la_correccion_el_ataque_falla():
    contrato = Escrow(verificador="verif", orden_correcto=True)
    contrato.acreditar_beneficiario("atacante", 180_000)
    atacante = BeneficiarioMalicioso(contrato, "atacante")
    contrato.registrar_receptor(atacante)

    contrato.retirar("atacante")
    assert atacante.reentradas == 0
    assert contrato.saldos["beneficiario:atacante"] == 0


def test_el_interruptor_detiene_sin_alterar_saldos():
    contrato = _escrow(True)
    saldo_antes = contrato.saldo_del_contrato()

    interruptor = Interruptor(umbral=2)
    interruptor.firmar("op1")
    assert not interruptor.activo
    interruptor.firmar("op2")
    assert interruptor.activo

    contrato.interruptor = interruptor
    with pytest.raises(ContratoDetenido):
        contrato.confirmar("op1", "verif", "exportador")
    assert contrato.saldo_del_contrato() == saldo_antes


# ----------------------------------------------------------------- oraculo


def _lecturas(valores: list[str]) -> list[Lectura]:
    return [Lectura(f"f{i}", Decimal(v)) for i, v in enumerate(valores)]


def test_la_mediana_resiste_un_valor_extremo():
    oraculo = Oraculo(minimo_fuentes=4)
    valor = oraculo.publicar(_lecturas(["100", "101", "99", "100", "1"]))
    assert valor == Decimal(100)


def test_la_media_no_resiste_un_valor_extremo():
    oraculo = Oraculo(minimo_fuentes=4)
    valor = oraculo.publicar(_lecturas(["100", "101", "99", "100", "1"]),
                             usar_mediana=False)
    assert valor < Decimal(85)


def test_con_pocas_fuentes_vivas_se_pausa_en_vez_de_publicar():
    oraculo = Oraculo(minimo_fuentes=4)
    with pytest.raises(SinFuentesSuficientes):
        oraculo.publicar(_lecturas(["100", "101"]))


def test_los_atipicos_se_descartan_respecto_de_la_publicacion_anterior():
    oraculo = Oraculo(minimo_fuentes=3, banda_descarte=Decimal("0.10"))
    oraculo.publicar(_lecturas(["100", "100", "100", "100"]))
    oraculo.publicar(_lecturas(["101", "102", "99", "100", "500"]))
    assert "f4" in oraculo.descartadas


def test_el_coste_de_manipular_depende_de_la_agregacion():
    assert fuentes_para_mover(5, usar_mediana=True) == 3
    assert fuentes_para_mover(5, usar_mediana=False) == 1


# ------------------------------------------------------------ firma multiple


def _guardian(nombre, ubicacion, proveedor, jurisdiccion) -> Guardian:
    return Guardian(nombre, generar_par(), ubicacion, proveedor, jurisdiccion)


def test_con_menos_del_umbral_no_se_autoriza():
    esquema = EsquemaMultifirma(
        umbral=3,
        guardianes=[_guardian(f"g{i}", "A", "P1", "CL") for i in range(5)],
    )
    mensaje = b"disponer de 1000000"
    firmas = esquema.firmar(["g0", "g1"], mensaje)
    assert not esquema.autoriza(firmas, mensaje)
    firmas.update(esquema.firmar(["g2"], mensaje))
    assert esquema.autoriza(firmas, mensaje)


def test_siete_guardianes_de_un_proveedor_no_son_siete_independencias():
    """Clase 3: contar claves no es contar independencias."""
    esquema = EsquemaMultifirma(
        umbral=4,
        guardianes=[_guardian(f"g{i}", f"U{i}", "P1", "CL") for i in range(7)],
    )
    analisis = analizar_correlacion(esquema)
    assert analisis["proveedor"]["cuantos"] == 7
    assert analisis["proveedor"]["quedan_si_falla"] == 0
    assert analisis["sobrevive_a_cualquier_causa_comun"] is False


def test_un_reparto_en_tres_proveedores_sobrevive():
    guardianes = (
        [_guardian(f"a{i}", "A", "P1", "CL") for i in range(3)]
        + [_guardian(f"b{i}", "B", "P2", "PE") for i in range(3)]
        + [_guardian(f"c{i}", "C", "P3", "UY") for i in range(3)]
    )
    esquema = EsquemaMultifirma(umbral=4, guardianes=guardianes)
    analisis = analizar_correlacion(esquema)
    assert analisis["sobrevive_a_cualquier_causa_comun"] is True
