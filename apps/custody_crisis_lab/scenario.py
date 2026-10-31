"""Orquestacion de un escenario completo de crisis de custodia.

Encadena los modulos en el orden en que un comite hace las preguntas:
respaldo antes -> clasificacion de fondos -> respaldo despues -> corrida ->
reposicion -> costo -> trayectoria.

Los parametros de `Parametros` son supuestos del ejercicio y estan visibles a
proposito: cambiarlos cambia la conclusion.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .costs import Costos, costo_de_oportunidad, compensaciones
from .datos import Escenario
from .entity import Custodio
from .incident import Fondos, aplicar_perdida, clasificar_fondos
from .recovery import trayectoria_de_respaldo
from .replenish import Fuente, PlanReposicion, necesidad_de_reposicion, plan_de_reposicion
from .runs import Dia, simular_corrida


@dataclass(frozen=True)
class Parametros:
    """Supuestos del ejercicio, en MUSD salvo indicacion."""

    dias_corrida: int = 7
    dia_restitucion: int = 14
    dia_reposicion: int = 3
    forense_legal: float = 50.0
    ingreso_diario: float = 8.0
    tasa_compensacion: float = 0.0
    objetivo_respaldo: float = 1.0
    fuentes: tuple[Fuente, ...] = field(
        default_factory=lambda: (
            Fuente("fondo de proteccion", 1_000.0, 0.0, 0),
            Fuente("capital propio", 5_000.0, 0.01, 3),
            Fuente("financiamiento externo", 50_000.0, 0.06, 7),
        )
    )


@dataclass(frozen=True)
class Resultado:
    antes: Custodio
    fondos: Fondos
    despues: Custodio
    corrida: list[Dia]
    corrida_con_reposicion: list[Dia]
    reposicion: PlanReposicion
    costos: Costos
    trayectoria: list[tuple[int, float]]


def ejecutar(
    entidad: Custodio, esc: Escenario, params: Parametros = Parametros()
) -> Resultado:
    fondos = clasificar_fondos(esc.sustraido, esc.congelado, esc.p_restitucion)
    despues = aplicar_perdida(entidad, esc.sustraido, esc.parte_liquida)
    corrida = simular_corrida(
        despues,
        esc.r0,
        esc.k,
        params.dias_corrida,
        descuento=esc.descuento,
        pausa_dias=esc.pausa_dias,
    )
    necesidad = necesidad_de_reposicion(despues, params.objetivo_respaldo)
    fuentes = list(params.fuentes)
    # El fondo de proteccion de la entidad es el que declara el balance.
    fuentes[0] = Fuente(
        fuentes[0].nombre, entidad.fondo_proteccion, fuentes[0].costo_relativo, 0
    )
    plan = plan_de_reposicion(necesidad, fuentes)
    ingresos: dict[int, float] = {}
    for a in plan.aportes:
        dia = max(a.dias, 1)
        ingresos[dia] = ingresos.get(dia, 0.0) + a.monto
    corrida_rep = simular_corrida(
        despues,
        esc.r0,
        esc.k,
        params.dias_corrida,
        descuento=esc.descuento,
        pausa_dias=esc.pausa_dias,
        reposiciones=ingresos,
    )
    costos = Costos(
        perdida_definitiva=fondos.perdida_definitiva,
        reposicion=plan.costo_total,
        forense_legal=params.forense_legal,
        oportunidad=costo_de_oportunidad(params.ingreso_diario, esc.pausa_dias),
        compensaciones=compensaciones(params.tasa_compensacion, entidad.pasivos_clientes),
    )
    trayectoria = trayectoria_de_respaldo(
        entidad,
        esc.sustraido,
        {params.dia_restitucion: fondos.restituible},
        {params.dia_reposicion: plan.cubierto},
        horizonte=max(params.dia_restitucion, params.dia_reposicion) + 2,
    )
    return Resultado(
        entidad, fondos, despues, corrida, corrida_rep, plan, costos, trayectoria,
    )
