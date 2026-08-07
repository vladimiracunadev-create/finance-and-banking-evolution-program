"""Construir, integrar o comprar: la decision la toma la salida.

La clase 2 sostiene que la comparacion de coste favorece integrar casi siempre, y
que el criterio que cambia la decision no es el coste sino la capacidad de
abandonar al proveedor. Un componente sin salida posible es una dependencia
estructural aunque integrarlo sea mas barato.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Decision(str, Enum):
    CONSTRUIR = "construir"
    INTEGRAR = "integrar"
    ESPERAR = "esperar"


# Funciones cuya responsabilidad no se externaliza. Se puede delegar la
# ejecucion; la responsabilidad sigue siendo de la entidad (clase 2).
NO_EXTERNALIZABLES = (
    "admitir a un cliente",
    "decidir si una operacion es sospechosa",
    "control interno y auditoria",
    "relacion con el supervisor",
    "decisiones de riesgo",
)


@dataclass(frozen=True)
class Salida:
    """Las cuatro preguntas que se hacen ANTES de integrar."""

    hay_alternativa: bool
    datos_portables: bool
    plazo_meses: int | None
    coste: int | None

    @property
    def es_real(self) -> bool:
        return (
            self.hay_alternativa
            and self.datos_portables
            and self.plazo_meses is not None
            and self.coste is not None
        )


@dataclass
class Componente:
    """Un componente del sistema con sus costes y su salida."""

    nombre: str
    diferenciador: bool
    proveedor_maduro: bool
    coste_construir_inicial: int
    coste_construir_anual: int
    coste_integrar_inicial: int
    coste_integrar_anual: int
    salida: Salida

    def coste_construir(self, anios: int) -> int:
        return self.coste_construir_inicial + self.coste_construir_anual * anios

    def coste_integrar(self, anios: int, con_una_salida: bool = False) -> int:
        total = self.coste_integrar_inicial + self.coste_integrar_anual * anios
        if con_una_salida:
            if not self.salida.es_real:
                # Sin salida real, abandonar al proveedor equivale a rehacer
                # el componente desde cero.
                return total + self.coste_construir_inicial
            total += self.salida.coste or 0
        return total

    def decidir(self, anios: int = 5) -> tuple[Decision, str]:
        """La salida manda sobre el coste."""
        if not self.salida.es_real:
            return (
                Decision.CONSTRUIR,
                "sin salida real, integrarlo seria una dependencia estructural",
            )
        if self.diferenciador and not self.proveedor_maduro:
            return Decision.CONSTRUIR, "diferenciador y sin proveedor maduro"
        if not self.diferenciador and not self.proveedor_maduro:
            return Decision.ESPERAR, "no diferencia y no hay proveedor maduro"

        construir = self.coste_construir(anios)
        integrar = self.coste_integrar(anios, con_una_salida=True)
        if integrar < construir:
            return (
                Decision.INTEGRAR,
                f"ahorra {construir - integrar:,} incluso con una salida",
            )
        return Decision.CONSTRUIR, "integrar no ahorra ni con salida real"


def concentracion_del_sector(usuarios_del_proveedor: int, entidades: int) -> float:
    """Cuota del sector que depende del mismo proveedor.

    Elegir al proveedor de casi todos es lo mas seguro para la entidad y lo peor
    para el sector (clase 2 y Parte 22, clase 14).
    """
    if entidades <= 0:
        raise ValueError("el numero de entidades debe ser positivo")
    return usuarios_del_proveedor / entidades
