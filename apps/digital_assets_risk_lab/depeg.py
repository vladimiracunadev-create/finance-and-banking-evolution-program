"""Anatomia de una perdida de paridad: fases, banda y punto de no retorno.

La clase 3 define la banda de no arbitraje; la clase 6 encadena las cinco fases
y sostiene que el detonante no se repite pero el mecanismo si. Este modulo
implementa ambas cosas para poder medirlas antes del episodio, no despues.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import IntEnum


class Fase(IntEnum):
    DETONANTE = 1
    DESVIO_INICIAL = 2
    PRUEBA_DEL_CANAL = 3
    CARRERA = 4
    REALIZACION_FORZADA = 5


@dataclass(frozen=True)
class CostesDeArbitraje:
    """Lo que cuesta corregir un desvio, por unidad."""

    comision_redencion: float
    coste_financiacion_anual: float
    dias_de_liquidacion: int
    coste_operacion: int
    minimo_redencion: int

    def por_unidad(self, tamano: int) -> float:
        if tamano <= 0:
            raise ValueError("el tamano debe ser positivo")
        financiacion = (
            self.coste_financiacion_anual * self.dias_de_liquidacion / 360
        )
        operacion = self.coste_operacion / tamano
        return self.comision_redencion + financiacion + operacion


def banda_de_no_arbitraje(
    costes: CostesDeArbitraje, tamano: int, paridad: float = 1.0
) -> tuple[float, float]:
    """Rango de precio donde arbitrar no compensa.

    La paridad no es un punto: es una banda, y su anchura la fija el diseno del
    emisor (clase 3).
    """
    ancho = costes.por_unidad(tamano)
    return paridad * (1 - ancho), paridad * (1 + ancho)


def arbitraje_rentable(
    precio: float, costes: CostesDeArbitraje, tamano: int, paridad: float = 1.0
) -> dict:
    """Resultado de comprar en mercado y redimir contra el emisor."""
    if tamano < costes.minimo_redencion:
        return {
            "puede_arbitrar": False,
            "motivo": "no alcanza el minimo de redencion",
            "neto": 0.0,
            "rentabilidad": 0.0,
        }
    bruto = (paridad - precio) * tamano
    coste = costes.por_unidad(tamano) * tamano
    neto = bruto - coste
    desembolso = precio * tamano
    return {
        "puede_arbitrar": True,
        "motivo": "arbitraje ejecutable",
        "bruto": bruto,
        "coste": coste,
        "neto": neto,
        "rentabilidad": neto / desembolso if desembolso else 0.0,
        "anualizada": (neto / desembolso) * 360 / max(costes.dias_de_liquidacion, 1)
        if desembolso
        else 0.0,
    }


# Las causas posibles de un desvio persistente. La cuarta es la unica que
# anticipa una crisis, y por eso un desvio persistente es una senal y no una
# oportunidad (clase 3, paso 6).
CAUSAS_DE_DESVIO_PERSISTENTE = (
    "la redencion esta suspendida",
    "los participantes autorizados agotaron su linea",
    "el plazo declarado es incierto en la practica",
    "hay dudas sobre las reservas",
    "las plataformas no permiten retirar",
)


@dataclass
class VigilanciaDeDesvio:
    """Indicador de desvio persistente fuera de banda.

    Dentro de banda el desvio es normal. Fuera de banda y sostenido significa
    que el mecanismo de arbitraje no opera, y eso el balance no lo muestra.
    """

    banda: tuple[float, float]
    horas_para_alerta: int = 6
    observaciones: list[float] = field(default_factory=list)

    def observar(self, precio: float) -> None:
        self.observaciones.append(precio)

    @property
    def horas_fuera_de_banda(self) -> int:
        bajo, alto = self.banda
        cuenta = 0
        for precio in reversed(self.observaciones):
            if bajo <= precio <= alto:
                break
            cuenta += 1
        return cuenta

    @property
    def en_alerta(self) -> bool:
        return self.horas_fuera_de_banda >= self.horas_para_alerta


@dataclass
class Episodio:
    """Linea de tiempo de una perdida de paridad."""

    detonante: str
    fases: list[tuple[Fase, str]] = field(default_factory=list)

    def registrar(self, fase: Fase, detalle: str) -> None:
        self.fases.append((fase, detalle))

    @property
    def canal_funciono(self) -> bool:
        """La fase 3 es la que decide si el episodio se cierra en horas."""
        for fase, detalle in self.fases:
            if fase is Fase.PRUEBA_DEL_CANAL:
                return "funciono" in detalle
        return False

    @property
    def llego_a_realizacion_forzada(self) -> bool:
        return any(fase is Fase.REALIZACION_FORZADA for fase, _ in self.fases)


def recuperacion_corrige_la_causa(motivo: str) -> bool:
    """Solo la reanudacion de la redencion corrige la causa (clase 6).

    Liquidez externa, compra de un tercero o ausencia de vendedores devuelven
    el precio dejando el mecanismo intacto.
    """
    return motivo == "se reanudo la redencion"
