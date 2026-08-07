"""Oraculo con agregacion defendible.

Dos decisiones que la clase 9 justifica y que el modulo hace cumplir:

1. MEDIANA, no media. Con media, un solo valor extremo mueve el resultado; con
   mediana hacen falta la mitad mas una de las fuentes. Es una linea de codigo
   y cambia el coste de atacar en un orden de magnitud.
2. MINIMO DE FUENTES VIVAS. Publicar un precio con dos de nueve fuentes es peor
   que no publicar: el contrato actuaria sobre un dato sin respaldo.
"""

from __future__ import annotations

import statistics
from dataclasses import dataclass, field
from decimal import Decimal


class SinFuentesSuficientes(Exception):
    """No hay fuentes vivas bastantes: se pausa en vez de publicar."""


@dataclass(frozen=True)
class Lectura:
    fuente: str
    valor: Decimal


@dataclass
class Oraculo:
    minimo_fuentes: int = 4
    banda_descarte: Decimal = Decimal("0.10")
    ultimo_valor: Decimal | None = None
    descartadas: list[str] = field(default_factory=list)

    def publicar(self, lecturas: list[Lectura], usar_mediana: bool = True) -> Decimal:
        self.descartadas = []
        vivas = list(lecturas)

        # Descarte de atipicos respecto de la publicacion anterior. Un salto
        # imposible es un error, no un precio.
        if self.ultimo_valor is not None and self.ultimo_valor > 0:
            conservadas = []
            for lectura in vivas:
                desviacion = abs(lectura.valor - self.ultimo_valor) / self.ultimo_valor
                if desviacion > self.banda_descarte:
                    self.descartadas.append(lectura.fuente)
                else:
                    conservadas.append(lectura)
            vivas = conservadas

        if len(vivas) < self.minimo_fuentes:
            raise SinFuentesSuficientes(
                f"{len(vivas)} fuentes vivas, se exigen {self.minimo_fuentes}"
            )

        valores = [lectura.valor for lectura in vivas]
        valor = (
            Decimal(statistics.median(valores))
            if usar_mediana
            else sum(valores) / Decimal(len(valores))
        )
        self.ultimo_valor = valor
        return valor


def fuentes_para_mover(n: int, usar_mediana: bool) -> int:
    """Cuantas fuentes hay que comprometer para mover el resultado.

    Con media basta una, si no hay filtro de atipicos. Con mediana hacen falta
    la mitad mas una. Ese es todo el argumento.
    """
    return (n // 2) + 1 if usar_mediana else 1
