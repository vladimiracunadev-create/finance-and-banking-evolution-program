"""Consenso bizantino DIDACTICO con nodos configurables.

El modulo existe para que el umbral se MIDA en vez de suponerse, y para
demostrar el hallazgo de la clase 5: el consenso tolera nodos que MIENTEN de
forma independiente, y no tolera software que se equivoca igual en todos.

No reproduce ningun protocolo de produccion ni sus optimizaciones.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from enum import Enum


class Comportamiento(Enum):
    HONESTO = "honesto"
    SILENCIOSO = "silencioso"
    MENTIROSO = "mentiroso"
    DEFECTO_COMUN = "defecto_comun"


@dataclass
class Nodo:
    identificador: str
    comportamiento: Comportamiento = Comportamiento.HONESTO
    implementacion: str = "principal"
    operador: str = "propio"
    jurisdiccion: str = "local"
    estado: str | None = None

    def votar(self, propuesta: str) -> str | None:
        if self.comportamiento is Comportamiento.SILENCIOSO:
            return None
        if self.comportamiento is Comportamiento.MENTIROSO:
            return f"mentira:{self.identificador}"
        if self.comportamiento is Comportamiento.DEFECTO_COMUN:
            # No miente: se equivoca. Y varios nodos con la misma
            # implementacion se equivocan IGUAL, que es lo que rompe el umbral.
            return "valor_incorrecto"
        return propuesta


@dataclass
class ResultadoRonda:
    decidido: bool
    valor: str | None
    votos: dict[str, int]
    quorum: int


@dataclass
class Red:
    nodos: list[Nodo] = field(default_factory=list)
    mensajes_ultima_ronda: int = 0

    @property
    def n(self) -> int:
        return len(self.nodos)

    @property
    def f(self) -> int:
        """Fallos bizantinos tolerables: n >= 3f + 1."""
        return (self.n - 1) // 3

    @property
    def quorum(self) -> int:
        return 2 * self.f + 1

    def nodos_honestos(self) -> list[Nodo]:
        return [n for n in self.nodos if n.comportamiento is Comportamiento.HONESTO]

    def ejecutar_ronda(self, propuesta: str = "bloque_valido") -> ResultadoRonda:
        # Cada nodo habla con todos: el coste es cuadratico, y con pocos
        # participantes eso es irrelevante (clase 5).
        self.mensajes_ultima_ronda = self.n * self.n

        votos = Counter(
            voto for nodo in self.nodos if (voto := nodo.votar(propuesta)) is not None
        )
        if not votos:
            return ResultadoRonda(False, None, {}, self.quorum)

        valor, cuenta = votos.most_common(1)[0]
        if cuenta >= self.quorum:
            for nodo in self.nodos_honestos():
                nodo.estado = valor
            return ResultadoRonda(True, valor, dict(votos), self.quorum)

        # Sin quorum NO se avanza. En finanzas se prefiere detenerse a divergir:
        # dos nodos con estados distintos han creado dinero.
        return ResultadoRonda(False, None, dict(votos), self.quorum)

    def estados_honestos(self) -> set[str | None]:
        return {n.estado for n in self.nodos_honestos()}


def independencia_efectiva(nodos: list[Nodo]) -> dict[str, int]:
    """Mayor grupo de nodos que puede fallar por una causa comun.

    Contar nodos no es contar independencias: el numero que importa es cuantos
    caen a la vez, no cuantos hay.
    """
    def mayor(atributo: str) -> int:
        cuenta = Counter(getattr(n, atributo) for n in nodos)
        return max(cuenta.values()) if cuenta else 0

    return {
        "por_implementacion": mayor("implementacion"),
        "por_operador": mayor("operador"),
        "por_jurisdiccion": mayor("jurisdiccion"),
    }
