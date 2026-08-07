"""Escenario de tension: donde se rompe el sistema.

La clase 15 sostiene que un escenario que el sistema aguanta no ensena nada, y
que la correlacion entre fallos —no su numero— es lo que hace el episodio. Aqui
la correlacion se modela explicitamente: un proveedor con varios papeles es la
fuente, y un solo fallo suyo alcanza a todos.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import IntEnum


class NivelDePrueba(IntEnum):
    """El gradiente de la clase 15. Declarar el nivel es lo que informa."""

    DOCUMENTAL = 1
    ESCRITORIO = 2
    ENTORNO_AISLADO = 3
    CONMUTACION_PLANIFICADA = 4
    CONMUTACION_NO_ANUNCIADA = 5


@dataclass(frozen=True)
class Proveedor:
    """Un proveedor y los papeles que desempena.

    Varios papeles en un mismo proveedor son la fuente de correlacion del
    sistema: un solo fallo alcanza a todos ellos.
    """

    nombre: str
    papeles: frozenset[str]

    @property
    def es_fuente_de_correlacion(self) -> bool:
        return len(self.papeles) > 1


@dataclass(frozen=True)
class Fallo:
    componente: str
    interrupcion_horas: float
    causa: str


@dataclass
class Escenario:
    """Un escenario adverso construido desde una fuente de correlacion."""

    fuente: Proveedor
    fallos: list[Fallo] = field(default_factory=list)
    nivel_de_prueba: NivelDePrueba = NivelDePrueba.DOCUMENTAL

    def desencadenar(self, horas: float, causa: str) -> list[Fallo]:
        """Un fallo del proveedor alcanza a todos sus papeles a la vez."""
        nuevos = [Fallo(p, horas, causa) for p in sorted(self.fuente.papeles)]
        self.fallos.extend(nuevos)
        return nuevos

    def anadir(self, componente: str, horas: float, causa: str) -> Fallo:
        fallo = Fallo(componente, horas, causa)
        self.fallos.append(fallo)
        return fallo

    def interrupciones(self) -> dict[str, float]:
        """Peor interrupcion por componente."""
        peor: dict[str, float] = {}
        for f in self.fallos:
            peor[f.componente] = max(peor.get(f.componente, 0.0), f.interrupcion_horas)
        return peor

    @property
    def componentes_afectados(self) -> int:
        return len(self.interrupciones())

    @property
    def demuestra_algo(self) -> bool:
        """Un escenario con un solo componente afectado no ensena nada."""
        return self.componentes_afectados >= 2


def desviaciones(caida: float, volatilidad_diaria: float, dias: int = 1) -> float:
    """A cuantas desviaciones esta el punto de rotura de un dia normal.

    Si esta a menos de tres, no es un escenario adverso: es un martes
    (clase 15).
    """
    if volatilidad_diaria <= 0 or dias <= 0:
        raise ValueError("volatilidad y dias deben ser positivos")
    return caida / (volatilidad_diaria * dias**0.5)


def coste_de_las_correcciones(correcciones: dict[str, int]) -> int:
    return sum(correcciones.values())


def coste_de_un_dia_de_interrupcion(
    volumen_diario: int, margen: float, coste_reputacional: int
) -> int:
    """Con qué se compara el coste de las correcciones."""
    return round(volumen_diario * margen) + coste_reputacional
