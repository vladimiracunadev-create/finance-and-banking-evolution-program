"""Creador de mercado automatizado de producto constante.

La clase 13 sostiene dos cosas que este modulo demuestra ejecutando:

1. El deslizamiento es aproximadamente el tamano de la operacion como fraccion
   de la reserva. Es lo que hace que el capital necesario sea enorme comparado
   con el volumen que sirve.
2. La perdida por divergencia es estructural, no accidental: quien aporta
   reservas acaba con mas del activo que baja y menos del que sube, y la unica
   pregunta es si las comisiones lo compensan.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt


class ReservaAgotada(ValueError):
    """Una operacion no puede vaciar una reserva: el precio tenderia a infinito."""


@dataclass
class Piscina:
    """Dos reservas cuyo producto se mantiene constante."""

    reserva_a: float
    reserva_b: float
    comision: float = 0.0025

    @property
    def k(self) -> float:
        return self.reserva_a * self.reserva_b

    @property
    def precio_marginal(self) -> float:
        """Precio de la siguiente unidad infinitesimal: B por cada A."""
        if self.reserva_a == 0:
            raise ReservaAgotada("la reserva de A esta vacia")
        return self.reserva_b / self.reserva_a

    def cotizar(self, entrega_a: float) -> dict:
        """Cuanto B se recibe por entregar `entrega_a` de A, sin ejecutar."""
        if entrega_a <= 0:
            raise ValueError("la entrega debe ser positiva")

        precio_antes = self.precio_marginal
        neto = entrega_a * (1 - self.comision)
        nueva_a = self.reserva_a + neto
        nueva_b = self.k / nueva_a
        recibe = self.reserva_b - nueva_b

        if recibe <= 0 or recibe >= self.reserva_b:
            raise ReservaAgotada("la operacion agotaria la reserva de B")

        precio_efectivo = recibe / entrega_a
        return {
            "recibe": recibe,
            "precio_marginal": precio_antes,
            "precio_efectivo": precio_efectivo,
            "deslizamiento": 1 - precio_efectivo / precio_antes,
            "tamano_relativo": entrega_a / self.reserva_a,
            "comision_cobrada": entrega_a * self.comision,
        }

    def operar(self, entrega_a: float) -> dict:
        """Ejecuta la operacion y actualiza las reservas."""
        cotizacion = self.cotizar(entrega_a)
        self.reserva_a += entrega_a
        self.reserva_b -= cotizacion["recibe"]
        return cotizacion


def perdida_por_divergencia(razon_de_precio: float) -> float:
    """Perdida frente a conservar los activos, para producto constante.

    Con r el factor de cambio del precio:  2·√r / (1 + r) − 1.
    Es siempre negativa o cero, y cero solo si el precio no se movio.
    """
    if razon_de_precio <= 0:
        raise ValueError("la razon de precio debe ser positiva")
    return 2 * sqrt(razon_de_precio) / (1 + razon_de_precio) - 1


def resultado_del_aportante(
    valor_aportado: float,
    comisiones_anuales: float,
    razon_de_precio: float,
) -> dict:
    """Neto entre comisiones cobradas y perdida por divergencia.

    Aportar reservas es una apuesta a que habra mucho volumen y poco movimiento,
    y quien la hace no puede retirarse ni ajustar su cotizacion mientras dura.
    """
    divergencia = perdida_por_divergencia(razon_de_precio) * valor_aportado
    neto = comisiones_anuales + divergencia
    return {
        "comisiones": comisiones_anuales,
        "divergencia": divergencia,
        "neto": neto,
        "rendimiento": neto / valor_aportado if valor_aportado else 0.0,
        "compensa": neto > 0,
    }


def razon_que_anula_las_comisiones(
    comisiones_anuales: float, valor_aportado: float, tolerancia: float = 1e-6
) -> float:
    """Movimiento de precio que se come un ano de comisiones.

    Se resuelve por biseccion sobre r > 1: la funcion de perdida es monotona
    decreciente en ese tramo, de modo que la busqueda converge siempre.
    """
    if valor_aportado <= 0:
        raise ValueError("el valor aportado debe ser positivo")
    objetivo = -comisiones_anuales / valor_aportado
    if objetivo <= -1:
        return float("inf")

    bajo, alto = 1.0, 2.0
    while perdida_por_divergencia(alto) > objetivo:
        alto *= 2
        if alto > 1e9:
            return float("inf")

    while alto - bajo > tolerancia:
        medio = (bajo + alto) / 2
        if perdida_por_divergencia(medio) > objetivo:
            bajo = medio
        else:
            alto = medio
    return (bajo + alto) / 2
