"""Liquidacion con pago contra pago y gestion de liquidez.

Dos ideas que el modulo demuestra ejecutando:

1. la exposicion de liquidacion es el MAXIMO SIMULTANEO, no la operacion mayor;
2. el plazo de la reserva vive en cada sistema, no en el coordinador. Un plazo
   gestionado por el coordinador no protege del fallo del coordinador.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal


# --------------------------------------------------------------- exposicion


@dataclass(frozen=True)
class Operacion:
    identificador: str
    contraparte: str
    importe: Decimal
    hora_entrega: int
    hora_recepcion: int


def exposicion_maxima(operaciones: list[Operacion]) -> Decimal:
    """Maximo simultaneo: las exposiciones se acumulan mientras estan vivas."""
    eventos: list[tuple[int, Decimal]] = []
    for op in operaciones:
        eventos.append((op.hora_entrega, op.importe))
        eventos.append((op.hora_recepcion, -op.importe))
    # A igual hora, primero las recepciones: no se cuenta como expuesto
    # un importe que ya se recibio en ese mismo instante.
    eventos.sort(key=lambda e: (e[0], e[1]))

    viva = maxima = Decimal(0)
    for _, delta in eventos:
        viva += delta
        maxima = max(maxima, viva)
    return maxima


def exposicion_por_contraparte(operaciones: list[Operacion]) -> dict[str, Decimal]:
    contrapartes = {op.contraparte for op in operaciones}
    return {
        c: exposicion_maxima([op for op in operaciones if op.contraparte == c])
        for c in sorted(contrapartes)
    }


# ------------------------------------------------------------ pago contra pago


class ReservaExpirada(Exception):
    """La reserva vencio antes de que llegara la orden de liberar."""


@dataclass
class Reserva:
    identificador: str
    importe: Decimal
    expira_en: int
    liberada: bool = False
    deshecha: bool = False


@dataclass
class SistemaLiquidacion:
    """Un sistema de liquidacion de una divisa.

    El plazo de la reserva lo controla EL SISTEMA. Si el coordinador cae entre
    el bloqueo y la liberacion, la reserva se deshace sola.
    """

    divisa: str
    reservas: dict[str, Reserva] = field(default_factory=dict)
    reloj: int = 0

    def reservar(self, identificador: str, importe: Decimal, plazo_s: int) -> Reserva:
        reserva = Reserva(identificador, importe, self.reloj + plazo_s)
        self.reservas[identificador] = reserva
        return reserva

    def avanzar(self, segundos: int) -> None:
        self.reloj += segundos
        for reserva in self.reservas.values():
            if not reserva.liberada and self.reloj > reserva.expira_en:
                reserva.deshecha = True

    def liberar(self, identificador: str) -> None:
        reserva = self.reservas[identificador]
        if reserva.deshecha or self.reloj > reserva.expira_en:
            raise ReservaExpirada(identificador)
        reserva.liberada = True

    def deshacer(self, identificador: str) -> None:
        self.reservas[identificador].deshecha = True


@dataclass
class Resultado:
    liquidado: bool
    motivo: str
    patas_liberadas: int = 0


def liquidar_pvp(
    identificador: str,
    importe_a: Decimal,
    importe_b: Decimal,
    sistema_a: SistemaLiquidacion,
    sistema_b: SistemaLiquidacion,
    plazo_s: int = 30,
    coordinador_cae: bool = False,
    sistema_b_falla_al_liberar: bool = False,
) -> Resultado:
    """Bloqueo, comprobacion y liberacion.

    `coordinador_cae` y `sistema_b_falla_al_liberar` existen para poder ejecutar
    los dos escenarios de fallo del laboratorio 7. El segundo es el caso
    peligroso: la atomicidad del protocolo no cubre un fallo posterior a la
    primera liberacion.
    """
    reserva_a = sistema_a.reservar(identificador, importe_a, plazo_s)
    if reserva_a.deshecha:
        return Resultado(False, "reserva A rechazada")

    reserva_b = sistema_b.reservar(identificador, importe_b, plazo_s)
    if reserva_b.deshecha:
        sistema_a.deshacer(identificador)
        return Resultado(False, "reserva B rechazada; se deshace A")

    if coordinador_cae:
        # El coordinador desaparece aqui. Nadie ordena liberar: los plazos
        # de cada sistema tienen que deshacer las reservas por si solos.
        sistema_a.avanzar(plazo_s + 1)
        sistema_b.avanzar(plazo_s + 1)
        return Resultado(False, "coordinador caido; reservas expiradas", 0)

    sistema_a.liberar(identificador)
    if sistema_b_falla_al_liberar:
        # Caso limite documentado: la pata A ya se liquido. La exposicion es
        # total y el protocolo no la cubre.
        return Resultado(False, "pata A liquidada, pata B fallida", 1)
    sistema_b.liberar(identificador)
    return Resultado(True, "liquidado", 2)


# ------------------------------------------------------------------- liquidez


def saldo_objetivo(
    percentil: Decimal, maximo_observado: Decimal, usar_colchon: bool = True
) -> Decimal:
    """El colchon cubre la distancia entre el percentil y el peor caso conocido."""
    return maximo_observado if usar_colchon else percentil


def coste_saldo(saldo: Decimal, coste_neto_anual: Decimal) -> Decimal:
    return saldo * coste_neto_anual


def ratio_netting(bruto: Decimal, neto: Decimal) -> Decimal:
    return Decimal(1) - (neto / bruto) if bruto else Decimal(0)


def netting_multilateral(posiciones: dict[tuple[str, str], Decimal]) -> dict[str, Decimal]:
    """Posiciones netas de cada participante a partir de las bilaterales."""
    netas: dict[str, Decimal] = {}
    for (paga, cobra), importe in posiciones.items():
        netas[paga] = netas.get(paga, Decimal(0)) - importe
        netas[cobra] = netas.get(cobra, Decimal(0)) + importe
    return dict(sorted(netas.items()))
