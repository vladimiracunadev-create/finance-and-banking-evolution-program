"""Libro de ordenes, profundidad e impacto de mercado.

La clase 13 sostiene que el volumen no es liquidez y que el cociente sobre
volumen y el cociente sobre profundidad pueden dar conclusiones opuestas. Aqui
se calculan los dos, para poder compararlos.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from math import sqrt


@dataclass(frozen=True)
class Nivel:
    """Un escalon del libro, con importe ACUMULADO hasta ese precio."""

    precio: float
    acumulado: int


@dataclass
class Libro:
    """Lado de compra de un libro de ordenes.

    Los niveles se ordenan de mejor a peor precio y su importe es acumulado,
    como se publican habitualmente los libros agregados.
    """

    precio_actual: float
    niveles: list[Nivel] = field(default_factory=list)
    volumen_diario: int = 0

    def __post_init__(self) -> None:
        self.niveles = sorted(self.niveles, key=lambda n: -n.precio)
        anterior = 0
        for nivel in self.niveles:
            if nivel.acumulado < anterior:
                raise ValueError("el importe acumulado no puede decrecer")
            anterior = nivel.acumulado

    def profundidad(self, caida: float) -> int:
        """Importe absorbible sin que el precio caiga mas de `caida`.

        Interpola entre niveles: el libro real no tiene escalones infinitos.
        """
        objetivo = self.precio_actual * (1 - caida)
        anterior_precio, anterior_acumulado = self.precio_actual, 0
        for nivel in self.niveles:
            if nivel.precio <= objetivo:
                tramo_precio = anterior_precio - nivel.precio
                if tramo_precio <= 0:
                    return nivel.acumulado
                proporcion = (anterior_precio - objetivo) / tramo_precio
                extra = (nivel.acumulado - anterior_acumulado) * proporcion
                return round(anterior_acumulado + extra)
            anterior_precio, anterior_acumulado = nivel.precio, nivel.acumulado
        return anterior_acumulado

    def vender(self, unidades: int, precio_de_cola: float | None = None) -> dict:
        """Ejecuta una venta contra el libro y devuelve el precio medio.

        `precio_de_cola` es el supuesto para lo que excede el ultimo nivel; sin
        el, la funcion no puede inventarse un precio y lo declara.
        """
        if unidades <= 0:
            raise ValueError("las unidades deben ser positivas")

        ingreso = 0.0
        restante = unidades
        anterior_acumulado = 0
        for nivel in self.niveles:
            tramo = nivel.acumulado - anterior_acumulado
            usado = min(tramo, restante)
            ingreso += usado * nivel.precio
            restante -= usado
            anterior_acumulado = nivel.acumulado
            if restante == 0:
                break

        agotado = restante > 0
        if agotado:
            if precio_de_cola is None:
                raise ValueError(
                    "la venta agota el libro y no se declaro precio de cola"
                )
            ingreso += restante * precio_de_cola

        precio_medio = ingreso / unidades
        teorico = unidades * self.precio_actual
        return {
            "ingreso": ingreso,
            "precio_medio": precio_medio,
            "impacto": 1 - precio_medio / self.precio_actual,
            "perdida": teorico - ingreso,
            "libro_agotado": agotado,
        }


def venta_escalonada(
    unidades: int, por_sesion: int, impacto_sesion: float, reposicion: float
) -> dict:
    """Impacto acumulado de trocear la venta en sesiones.

    Cada sesion deja un residuo `1 - reposicion` que el libro no recupera; el
    impacto total es el de una sesion mas los residuos de las anteriores.
    """
    if por_sesion <= 0:
        raise ValueError("el tamano por sesion debe ser positivo")
    if not 0.0 <= reposicion <= 1.0:
        raise ValueError("la reposicion debe estar entre 0 y 1")

    sesiones = -(-unidades // por_sesion)  # division hacia arriba
    impacto = impacto_sesion * (1 + (sesiones - 1) * (1 - reposicion))
    return {"sesiones": sesiones, "impacto": impacto}


def riesgo_de_esperar(volatilidad_diaria: float, horas: float) -> float:
    """Movimiento tipico del precio durante la ventana de ejecucion.

    Escalonar solo compensa si el ahorro supera este riesgo, y en un dia de
    tension la relacion se invierte (clase 13, paso 6).
    """
    if horas < 0:
        raise ValueError("las horas no pueden ser negativas")
    return volatilidad_diaria * sqrt(horas / 24)


def limite_de_posicion(libro: Libro, factor: float = 3.0) -> int:
    """Limite colgado de la profundidad al 1 %, no del volumen publicado."""
    return round(libro.profundidad(0.01) * factor)


def cocientes(libro: Libro, posicion: int) -> dict[str, float]:
    """Los dos cocientes de la clase 13, para poder contrastarlos.

    El de volumen suele tranquilizar; el de profundidad suele decir la verdad.
    """
    profundidad = libro.profundidad(0.01)
    return {
        "sobre_volumen": posicion / libro.volumen_diario if libro.volumen_diario else 0.0,
        "sobre_profundidad": posicion / profundidad if profundidad else float("inf"),
    }
