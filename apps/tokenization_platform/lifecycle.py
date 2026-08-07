"""Ciclo de vida: cupones, inmovilizacion y vencimiento.

La clase 5 sostiene dos cosas que este modulo hace cumplir por construccion:

1. Hay que verificar el aprovisionamiento ANTES de empezar a pagar. Un contrato
   que paga por orden hasta quedarse sin fondos no reparte: discrimina.
2. Al vencer, solo se destruyen las unidades cuyo pago esta CONFIRMADO. Destruir
   todas a la vez deja sin instrumento —y sin prueba de su derecho— a quien
   todavia no ha cobrado.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class EstadoPago(str, Enum):
    PAGADO = "pagado"
    CUENTA_BLOQUEADA = "cuenta_bloqueada"
    NO_LOCALIZABLE = "no_localizable"
    INMOVILIZADO = "inmovilizado"


class AprovisionamientoInsuficiente(RuntimeError):
    """No se paga a nadie si no alcanza para todos."""


class SinDobleAprobacion(RuntimeError):
    """La inmovilizacion exige dos aprobadores distintos."""


@dataclass(frozen=True)
class Titular:
    nombre: str
    unidades: int
    cuenta_bloqueada: bool = False
    localizable: bool = True


@dataclass(frozen=True)
class Instantanea:
    """Foto verificable del registro a la fecha de corte."""

    momento: str
    posiciones: dict[str, int]

    @property
    def total(self) -> int:
        return sum(self.posiciones.values())


@dataclass(frozen=True)
class ResultadoCupon:
    importe_por_unidad: int
    pagado: int
    pendiente: int
    detalle: dict[str, EstadoPago]

    @property
    def titulares_pagados(self) -> int:
        return sum(1 for e in self.detalle.values() if e is EstadoPago.PAGADO)


@dataclass
class Inmovilizacion:
    """Registro inmutable de una orden de autoridad aplicada a un titular."""

    titular: str
    unidades: int
    aprobado_por: tuple[str, str]
    motivo: str

    def __post_init__(self) -> None:
        if self.aprobado_por[0] == self.aprobado_por[1]:
            raise SinDobleAprobacion("los dos aprobadores deben ser distintos")


@dataclass
class Instrumento:
    """Un bono tokenizado con su ciclo de vida."""

    nominal_por_unidad: int
    unidades: int
    cupon_anual: float
    periodicidad: int = 2
    titulares: dict[str, Titular] = field(default_factory=dict)
    inmovilizaciones: list[Inmovilizacion] = field(default_factory=list)
    vencido: bool = False
    destruidas: int = 0
    pagos_confirmados: set[str] = field(default_factory=set)

    def registrar(self, titular: Titular) -> None:
        self.titulares[titular.nombre] = titular

    def instantanea(self, momento: str) -> Instantanea:
        return Instantanea(
            momento, {t.nombre: t.unidades for t in self.titulares.values()}
        )

    @property
    def cupon_por_unidad(self) -> int:
        return round(self.nominal_por_unidad * self.cupon_anual / self.periodicidad)

    def cupon_total(self, instantanea: Instantanea) -> int:
        return self.cupon_por_unidad * instantanea.total

    def _inmovilizados(self) -> set[str]:
        return {i.titular for i in self.inmovilizaciones}

    def pagar_cupon(self, instantanea: Instantanea, aprovisionado: int) -> ResultadoCupon:
        """Paga contra la instantanea, tras verificar los fondos.

        Si no alcanza, NO paga a nadie: es el mismo principio de la Parte 20,
        clase 5, donde el orden de llegada no reparte, discrimina.
        """
        necesario = self.cupon_total(instantanea)
        if aprovisionado < necesario:
            raise AprovisionamientoInsuficiente(
                f"aprovisionado {aprovisionado} < necesario {necesario}"
            )

        inmovilizados = self._inmovilizados()
        detalle: dict[str, EstadoPago] = {}
        pagado = pendiente = 0

        for nombre, unidades in instantanea.posiciones.items():
            importe = self.cupon_por_unidad * unidades
            titular = self.titulares.get(nombre)
            if nombre in inmovilizados:
                # El derecho al cupon subsiste: el importe se consigna a
                # disposicion de la autoridad, no se anula.
                detalle[nombre] = EstadoPago.INMOVILIZADO
                pendiente += importe
            elif titular is not None and titular.cuenta_bloqueada:
                detalle[nombre] = EstadoPago.CUENTA_BLOQUEADA
                pendiente += importe
            elif titular is not None and not titular.localizable:
                detalle[nombre] = EstadoPago.NO_LOCALIZABLE
                pendiente += importe
            else:
                detalle[nombre] = EstadoPago.PAGADO
                pagado += importe
                self.pagos_confirmados.add(nombre)

        return ResultadoCupon(self.cupon_por_unidad, pagado, pendiente, detalle)

    def inmovilizar(
        self, titular: str, unidades: int, aprobadores: tuple[str, str], motivo: str
    ) -> Inmovilizacion:
        """Solo inmoviliza: no transfiere ni altera saldos.

        Es el interruptor de la Parte 19, clase 8, aplicado a un titular.
        """
        if titular not in self.titulares:
            raise KeyError(titular)
        registro = Inmovilizacion(titular, unidades, aprobadores, motivo)
        self.inmovilizaciones.append(registro)
        return registro

    def vencer(self, confirmados: set[str]) -> dict[str, int]:
        """Marca el vencimiento y destruye SOLO lo pagado y confirmado."""
        self.vencido = True
        destruidas = 0
        vivas = 0
        for nombre, titular in self.titulares.items():
            if nombre in confirmados:
                destruidas += titular.unidades
            else:
                vivas += titular.unidades
        self.destruidas = destruidas
        return {"destruidas": destruidas, "vivas": vivas}


def coste_de_un_error_de_corte(
    operaciones_en_la_ventana: int,
    unidades_afectadas: int,
    cupon_por_unidad: int,
    coste_por_gestion: int,
) -> dict[str, int]:
    """Compara el importe en disputa con el coste de corregirlo.

    En la clase 5 el segundo supera al primero, y esa es la leccion: el problema
    de un error de corte no es su importe, es que hay que recuperar dinero ya
    pagado a personas identificadas.
    """
    importe = unidades_afectadas * cupon_por_unidad
    gestiones = operaciones_en_la_ventana * 2  # el que cobro y el que no
    correccion = gestiones * coste_por_gestion
    return {
        "importe_en_disputa": importe,
        "coste_de_correccion": correccion,
        "corregir_cuesta_mas": correccion > importe,
    }
