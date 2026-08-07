"""Enlace entre dos sistemas de pagos inmediatos.

De los seis problemas de un enlace, solo uno es tecnico. Este modulo implementa
ese uno —la resolucion de alias— y hace explicitos los otros cinco, porque un
proyecto que solo resuelve el primero no tiene un enlace: tiene una integracion.

Dos decisiones que la implementacion hace cumplir:

* la respuesta es UNIFORME cuando el alias no existe; si difiere, se puede
  enumerar que numeros tienen cuenta;
* el nombre se devuelve ENMASCARADO: basta para que el ordenante confirme y no
  expone el nombre completo a quien solo tiene un telefono.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

LIMITE_CONSULTAS_POR_HORA = 20


class NoResuelto(Exception):
    """Respuesta uniforme: no revela si el alias existe."""


class LimiteExcedido(Exception):
    """Posible enumeracion del directorio de alias."""


@dataclass(frozen=True)
class Cuenta:
    alias: str
    banco: str
    titular: str
    tiene_cuenta: bool = True


@dataclass(frozen=True)
class Resolucion:
    banco: str
    nombre_mascara: str


def enmascarar(nombre: str) -> str:
    """«Juan Perez Soto» -> «J*** P**** S***»."""
    partes = []
    for palabra in nombre.split():
        partes.append(palabra[0] + "*" * max(len(palabra) - 1, 1))
    return " ".join(partes)


@dataclass
class Directorio:
    cuentas: dict[str, Cuenta] = field(default_factory=dict)
    consultas: dict[str, int] = field(default_factory=dict)

    def registrar(self, cuenta: Cuenta) -> None:
        self.cuentas[cuenta.alias] = cuenta

    def resolver(self, alias: str, solicitante: str) -> Resolucion:
        self.consultas[solicitante] = self.consultas.get(solicitante, 0) + 1
        if self.consultas[solicitante] > LIMITE_CONSULTAS_POR_HORA:
            raise LimiteExcedido("posible enumeracion del directorio")

        cuenta = self.cuentas.get(alias)
        if cuenta is None or not cuenta.tiene_cuenta:
            raise NoResuelto("alias no disponible")
        return Resolucion(cuenta.banco, enmascarar(cuenta.titular))


@dataclass(frozen=True)
class Cotizacion:
    proveedor: str
    diferencial_pb: Decimal


def subastar(cotizaciones: list[Cotizacion]) -> Cotizacion:
    """Gana el mejor tipo. Con un solo proveedor no hay subasta: hay precio."""
    if not cotizaciones:
        raise ValueError("sin proveedores de liquidez")
    return min(cotizaciones, key=lambda c: (c.diferencial_pb, c.proveedor))


@dataclass(frozen=True)
class Enlace:
    limite_origen: Decimal
    limite_destino: Decimal
    cobertura_cuentas_destino: Decimal

    @property
    def limite_efectivo(self) -> Decimal:
        """El enlace queda acotado por el sistema MENOR de los dos."""
        return min(self.limite_origen, self.limite_destino)

    def cobertura(self, proporcion_bajo_limite: Decimal) -> dict[str, Decimal]:
        """Cobertura real del corredor y, sobre todo, quien queda fuera."""
        alcanzable = proporcion_bajo_limite * self.cobertura_cuentas_destino
        return {
            "por_limite": Decimal(1) - proporcion_bajo_limite,
            "por_falta_de_cuenta": proporcion_bajo_limite
            * (Decimal(1) - self.cobertura_cuentas_destino),
            "cobertura_real": alcanzable,
            "excluido": Decimal(1) - alcanzable,
        }


# Los cinco problemas que NO son tecnicos. Se declaran aqui para que ningun
# proyecto pueda decir que los resolvio sin haberlos escrito.
REGLAS_MINIMAS = (
    "ley aplicable a la operacion y en que momento cambia",
    "responsabilidad ante un pago no autorizado y quien repite contra quien",
    "plazo y procedimiento de devolucion",
    "foro y reglas de arbitraje de disputas",
    "contingencia si un sistema cae con pagos a medias",
)


def reglas_pendientes(escritas: set[str]) -> list[str]:
    return [regla for regla in REGLAS_MINIMAS if regla not in escritas]
