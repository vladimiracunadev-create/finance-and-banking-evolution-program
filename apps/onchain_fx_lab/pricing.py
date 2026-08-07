"""Coste total de un cambio de divisa: mayorista frente a registro.

La clase 11 sostiene que el registro no compite en precio sino en topologia:
gana cuando elimina tramos de corresponsalia, exactamente igual que la ruta con
stablecoin de la Parte 18. Comparar solo el precio mostrado esconde cuatro de los
seis tramos.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Mecanismo(str, Enum):
    """De donde sale el precio en un registro (clase 11)."""

    ORACULO_IMPORTADO = "oraculo_importado"
    LIBRO_PROPIO = "libro_propio"
    FORMULA_AUTOMATIZADA = "formula_automatizada"

    @property
    def forma_precio(self) -> bool:
        """Solo un libro propio forma precio; los otros lo copian o lo derivan."""
        return self is Mecanismo.LIBRO_PROPIO


@dataclass(frozen=True)
class Tramo:
    """Un componente del coste, en puntos basicos sobre el nominal."""

    nombre: str
    puntos_basicos: float


@dataclass
class Ruta:
    """Una forma de ejecutar el cambio, con todos sus tramos declarados."""

    nombre: str
    tramos: list[Tramo] = field(default_factory=list)

    def agregar(self, nombre: str, puntos_basicos: float) -> None:
        self.tramos.append(Tramo(nombre, puntos_basicos))

    @property
    def total_pb(self) -> float:
        return sum(t.puntos_basicos for t in self.tramos)

    def coste(self, nominal: int) -> float:
        return nominal * self.total_pb / 10_000

    def desglose(self, nominal: int) -> dict[str, float]:
        return {t.nombre: nominal * t.puntos_basicos / 10_000 for t in self.tramos}


def ruta_mayorista(
    diferencial_pb: float, comision_pb: float, corresponsalia_pb: float = 0.0
) -> Ruta:
    """Ruta clasica. El diferencial se paga a la mitad: se opera en un lado."""
    ruta = Ruta("mayorista")
    ruta.agregar("diferencial", diferencial_pb / 2)
    ruta.agregar("comision", comision_pb)
    if corresponsalia_pb:
        ruta.agregar("corresponsalia", corresponsalia_pb)
    return ruta


def ruta_registro(
    margen_pb: float,
    diferencial_pb: float,
    entrada_pb: float,
    salida_pb: float,
) -> Ruta:
    """Ruta por registro, con los cuatro tramos que el precio mostrado esconde."""
    ruta = Ruta("registro")
    ruta.agregar("margen sobre el importado", margen_pb)
    ruta.agregar("diferencial", diferencial_pb / 2)
    ruta.agregar("entrada al registro", entrada_pb)
    ruta.agregar("salida del registro", salida_pb)
    return ruta


def comparar(mayorista: Ruta, registro: Ruta, nominal: int) -> dict:
    """Compara dos rutas y devuelve el ahorro en puntos basicos y en importe."""
    ahorro_pb = mayorista.total_pb - registro.total_pb
    return {
        "mayorista_pb": mayorista.total_pb,
        "registro_pb": registro.total_pb,
        "ahorro_pb": ahorro_pb,
        "ahorro": nominal * ahorro_pb / 10_000,
        "gana_el_registro": ahorro_pb > 0,
        "veces": registro.total_pb / mayorista.total_pb
        if mayorista.total_pb
        else float("inf"),
    }


def ahorro_corregido_por_profundidad(
    ahorro_pb: float,
    nominal: int,
    profundidad_1pc: float,
    tramos_de_ejecucion: int,
    reposicion: float = 0.70,
) -> dict:
    """Descuenta del ahorro el impacto de ejecutar contra un libro fino.

    El ahorro anunciado supone que se ejecuta todo al precio mostrado. Con una
    posicion varias veces mayor que la profundidad, ese supuesto es falso y el
    ahorro real puede ser una fraccion del anunciado (clase 11, paso 6).
    """
    if tramos_de_ejecucion < 1:
        raise ValueError("hacen falta al menos un tramo de ejecucion")
    if profundidad_1pc <= 0:
        raise ValueError("la profundidad debe ser positiva")

    por_tramo = nominal / tramos_de_ejecucion
    impacto_tramo_pb = por_tramo / profundidad_1pc * 100  # 1 % = 100 pb
    residuo = 1 - reposicion
    impacto_total_pb = impacto_tramo_pb * (1 + (tramos_de_ejecucion - 1) * residuo)

    return {
        "impacto_pb": impacto_total_pb,
        "ahorro_anunciado_pb": ahorro_pb,
        "ahorro_real_pb": ahorro_pb - impacto_total_pb,
        "sigue_compensando": ahorro_pb - impacto_total_pb > 0,
    }
