"""Reposicion de reservas: cuanto falta y cuanto cuesta reponerlo.

Formulas:

    necesidad       N = max(0, objetivo * P - (A_liq + A_nl))
    costo de compra C = impacto * monto^2 / profundidad       (impacto lineal)

Variables: objetivo = respaldo bruto buscado (1,00 = 100 %), impacto =
deslizamiento por cada fraccion de la profundidad consumida, profundidad =
monto que el mercado absorbe con ese impacto, en las mismas unidades que monto.

Supuestos: el impacto es lineal en el monto comprado; las fuentes se usan en el
orden dado y cada una tiene un tope y un costo proporcional.
Limitacion: en tension la profundidad se contrae y el impacto no es lineal; el
modelo subestima el costo de comprar grandes montos en poco tiempo.
"""

from __future__ import annotations

from dataclasses import dataclass

from .entity import Custodio


@dataclass(frozen=True)
class Fuente:
    nombre: str
    tope: float
    costo_relativo: float  # costo por unidad aportada (0,02 = 2 %)
    dias: int = 0  # plazo hasta disponibilidad


def necesidad_de_reposicion(entidad: Custodio, objetivo: float = 1.0) -> float:
    if objetivo <= 0:
        raise ValueError("objetivo debe ser positivo")
    return max(0.0, objetivo * entidad.pasivos_clientes - entidad.activos_totales)


def costo_de_compra(monto: float, impacto: float, profundidad: float) -> float:
    if monto < 0 or impacto < 0 or profundidad <= 0:
        raise ValueError("parametros invalidos")
    return impacto * monto * monto / profundidad


@dataclass(frozen=True)
class Aporte:
    fuente: str
    monto: float
    costo: float
    dias: int


@dataclass(frozen=True)
class PlanReposicion:
    necesidad: float
    aportes: list[Aporte]
    cubierto: float
    faltante: float
    costo_total: float


def plan_de_reposicion(necesidad: float, fuentes: list[Fuente]) -> PlanReposicion:
    """Cubre `necesidad` usando las fuentes en el orden recibido."""
    if necesidad < 0:
        raise ValueError("necesidad no puede ser negativa")
    pendiente = necesidad
    aportes: list[Aporte] = []
    for f in fuentes:
        if pendiente <= 0:
            break
        monto = min(f.tope, pendiente)
        aportes.append(Aporte(f.nombre, monto, monto * f.costo_relativo, f.dias))
        pendiente -= monto
    return PlanReposicion(
        necesidad=necesidad,
        aportes=aportes,
        cubierto=necesidad - pendiente,
        faltante=pendiente,
        costo_total=sum(a.costo for a in aportes),
    )
