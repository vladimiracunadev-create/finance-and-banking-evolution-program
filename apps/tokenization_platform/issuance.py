"""Mercado primario: libro de ordenes, adjudicacion y emision desierta.

La clase 4 sostiene que el bloqueo del importe no es un requisito operativo: es
lo que hace que el libro de ordenes INFORME, porque convierte exagerar la orden
en algo que cuesta dinero.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Mecanismo(str, Enum):
    PRORRATEO_SIMPLE = "prorrateo_simple"
    PRORRATEO_CON_MINIMO = "prorrateo_con_minimo"
    ORDEN_DE_LLEGADA = "orden_de_llegada"


@dataclass(frozen=True)
class Orden:
    inversionista: str
    importe: int
    turno: int
    intencion_real: int | None = None


@dataclass(frozen=True)
class Adjudicacion:
    inversionista: str
    solicitado: int
    adjudicado: int

    @property
    def fraccion(self) -> float:
        return self.adjudicado / self.solicitado if self.solicitado else 0.0


@dataclass(frozen=True)
class Resultado:
    mecanismo: Mecanismo
    adjudicaciones: list[Adjudicacion]
    colocado: int
    desierta: bool

    @property
    def ventaja_del_primero(self) -> float:
        if not self.adjudicaciones:
            return 0.0
        fracciones = [a.fraccion for a in self.adjudicaciones]
        return max(fracciones) - min(fracciones)


@dataclass
class Emision:
    """Una colocacion con periodo de suscripcion y minimo declarado."""

    objetivo: int
    minimo: int
    dias_de_suscripcion: int = 10
    tramo_minimo: int = 0
    bloqueo_obligatorio: bool = False
    coste_financiacion_anual: float = 0.042
    ordenes: list[Orden] = field(default_factory=list)

    def ordenar(
        self, inversionista: str, importe: int, intencion_real: int | None = None
    ) -> Orden:
        orden = Orden(inversionista, importe, len(self.ordenes), intencion_real)
        self.ordenes.append(orden)
        return orden

    @property
    def demanda(self) -> int:
        return sum(o.importe for o in self.ordenes)

    @property
    def sobredemanda(self) -> float:
        return self.demanda / self.objetivo if self.objetivo else 0.0

    def coste_del_bloqueo(self, importe: int) -> float:
        """Lo que cuesta inmovilizar un importe durante el periodo.

        Es el precio de exagerar la orden, y sin el, el libro no informa.
        """
        if not self.bloqueo_obligatorio:
            return 0.0
        return importe * self.coste_financiacion_anual * self.dias_de_suscripcion / 360

    def demanda_genuina(self, factor_de_exageracion: float) -> int:
        """Demanda real estimada corrigiendo la exageracion declarada.

        El factor es un SUPUESTO del analista y hay que declararlo: sin el, el
        libro de ordenes sugiere una demanda que no existe.
        """
        if factor_de_exageracion <= 0:
            raise ValueError("el factor debe ser positivo")
        return round(self.demanda / factor_de_exageracion)

    def adjudicar(self, mecanismo: Mecanismo) -> Resultado:
        if self.demanda < self.minimo:
            # Emision desierta: no se anota nada y los bloqueos se liberan en
            # el mismo acto, sin instruccion de nadie.
            return Resultado(
                mecanismo,
                [Adjudicacion(o.inversionista, o.importe, 0) for o in self.ordenes],
                colocado=0,
                desierta=True,
            )

        colocable = min(self.objetivo, self.demanda)
        if mecanismo is Mecanismo.ORDEN_DE_LLEGADA:
            return self._orden_de_llegada(colocable)
        if mecanismo is Mecanismo.PRORRATEO_CON_MINIMO:
            return self._prorrateo(colocable, self.tramo_minimo)
        return self._prorrateo(colocable, 0)

    def _orden_de_llegada(self, colocable: int) -> Resultado:
        restante = colocable
        adjudicaciones: list[Adjudicacion] = []
        for orden in sorted(self.ordenes, key=lambda o: o.turno):
            dado = min(orden.importe, restante)
            restante -= dado
            adjudicaciones.append(
                Adjudicacion(orden.inversionista, orden.importe, dado)
            )
        return Resultado(
            Mecanismo.ORDEN_DE_LLEGADA, adjudicaciones, colocable - restante, False
        )

    def _prorrateo(self, colocable: int, tramo_minimo: int) -> Resultado:
        reservado = 0
        integro: dict[str, int] = {}
        if tramo_minimo > 0:
            for orden in self.ordenes:
                trozo = min(orden.importe, tramo_minimo)
                integro[orden.inversionista] = trozo
                reservado += trozo
            if reservado > colocable:
                integro, reservado = {}, 0

        resto_disponible = colocable - reservado
        resto_solicitado = self.demanda - reservado
        fraccion = resto_disponible / resto_solicitado if resto_solicitado > 0 else 0.0
        fraccion = min(fraccion, 1.0)

        adjudicaciones: list[Adjudicacion] = []
        colocado = 0
        for orden in self.ordenes:
            base = integro.get(orden.inversionista, 0)
            extra = round((orden.importe - base) * fraccion)
            dado = min(base + extra, orden.importe)
            colocado += dado
            adjudicaciones.append(
                Adjudicacion(orden.inversionista, orden.importe, dado)
            )
        mecanismo = (
            Mecanismo.PRORRATEO_CON_MINIMO if tramo_minimo else Mecanismo.PRORRATEO_SIMPLE
        )
        return Resultado(mecanismo, adjudicaciones, colocado, False)
