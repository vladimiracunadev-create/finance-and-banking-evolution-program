"""Modelo didáctico de economía virtual y flujo financiero de GAMECO.

El módulo no decide una clasificación jurídica. Separa hechos económicos que
sí pueden medirse: emisión y destrucción de GEM, transferibilidad, cash-out,
bookings, recepción neta, obligación comercial pendiente y conciliación.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class NivelGameco:
    """Características observables de una fase del producto."""

    transferible: bool = False
    convertible: bool = False
    mercado_externo: bool = False
    custodia_por_operador: bool = True
    payout: bool = False

    @property
    def nivel(self) -> str:
        if self.convertible or self.payout:
            return "C"
        if self.transferible:
            return "B"
        return "A"

    @property
    def naturaleza_economica(self) -> str:
        if self.nivel == "A":
            return "unidad interna de acceso a bienes o servicios"
        if self.nivel == "B":
            return "valor transferible dentro de una plataforma"
        return "valor convertible con canal de salida monetaria"

    @property
    def exige_analisis_especializado(self) -> bool:
        return self.convertible or self.mercado_externo or self.payout


@dataclass(frozen=True)
class EconomiaVirtual:
    """Stock y flujo de una unidad virtual durante un periodo."""

    stock_inicial: int
    sources: int
    sinks: int
    volumen_transferido: int = 0
    saldos: tuple[int, ...] = ()

    def __post_init__(self) -> None:
        if min(self.stock_inicial, self.sources, self.sinks, self.volumen_transferido) < 0:
            raise ValueError("stock y flujos no pueden ser negativos")
        if self.sinks > self.stock_inicial + self.sources:
            raise ValueError("los sinks no pueden destruir más unidades que las disponibles")
        if any(saldo < 0 for saldo in self.saldos):
            raise ValueError("los saldos no pueden ser negativos")

    @property
    def emision_neta(self) -> int:
        return self.sources - self.sinks

    @property
    def stock_final(self) -> int:
        return self.stock_inicial + self.emision_neta

    @property
    def ratio_sinks_sources(self) -> float:
        return self.sinks / self.sources if self.sources else float("inf")

    @property
    def velocidad(self) -> float:
        stock_medio = (self.stock_inicial + self.stock_final) / 2
        return self.volumen_transferido / stock_medio if stock_medio else 0.0

    @property
    def concentracion_top_10(self) -> float:
        if not self.saldos or sum(self.saldos) == 0:
            return 0.0
        cuantos = max(1, (len(self.saldos) + 9) // 10)
        return sum(sorted(self.saldos, reverse=True)[:cuantos]) / sum(self.saldos)


@dataclass(frozen=True)
class UnitEconomics:
    """Puente reproducible entre jugadores, bookings y recepción neta.

    El impuesto se supone incluido en el precio y la comisión de plataforma se
    aplica sobre la venta neta de ese impuesto. Es un supuesto del ejercicio,
    no una regla contractual universal.
    """

    jugadores: int
    payer_conversion: float
    arppu_clp: int
    impuesto_incluido: float = 0.19
    platform_fee_rate: float = 0.15
    payment_fee_rate: float = 0.02
    refund_rate: float = 0.03
    chargeback_rate: float = 0.005

    def __post_init__(self) -> None:
        tasas = (
            self.payer_conversion,
            self.platform_fee_rate,
            self.payment_fee_rate,
            self.refund_rate,
            self.chargeback_rate,
        )
        if self.jugadores < 0 or self.arppu_clp < 0 or any(not 0 <= x <= 1 for x in tasas):
            raise ValueError("volúmenes y tasas fuera de rango")
        if self.impuesto_incluido < 0:
            raise ValueError("el impuesto no puede ser negativo")

    @property
    def pagadores(self) -> int:
        return round(self.jugadores * self.payer_conversion)

    @property
    def gross_bookings(self) -> int:
        return self.pagadores * self.arppu_clp

    @property
    def impuesto(self) -> float:
        return self.gross_bookings * self.impuesto_incluido / (1 + self.impuesto_incluido)

    @property
    def base_sin_impuesto(self) -> float:
        return self.gross_bookings - self.impuesto

    @property
    def platform_fee(self) -> float:
        return self.base_sin_impuesto * self.platform_fee_rate

    @property
    def payment_fee(self) -> float:
        return self.base_sin_impuesto * self.payment_fee_rate

    @property
    def refunds(self) -> float:
        return self.gross_bookings * self.refund_rate

    @property
    def chargebacks(self) -> float:
        return self.gross_bookings * self.chargeback_rate

    @property
    def net_receipts(self) -> float:
        return (
            self.gross_bookings
            - self.impuesto
            - self.platform_fee
            - self.payment_fee
            - self.refunds
            - self.chargebacks
        )


@dataclass(frozen=True)
class ObligacionVirtual:
    """Análisis pedagógico de cobro, consumo y breakage bajo un contrato dado."""

    cobro_asignado: float
    unidades_vendidas: int
    unidades_consumidas: int
    breakage_estimado: float = 0.0

    def __post_init__(self) -> None:
        if self.cobro_asignado < 0 or self.unidades_vendidas <= 0:
            raise ValueError("cobro y unidades deben ser positivos")
        if not 0 <= self.unidades_consumidas <= self.unidades_vendidas:
            raise ValueError("consumo fuera de rango")
        if not 0 <= self.breakage_estimado < 1:
            raise ValueError("breakage fuera de rango")

    @property
    def proporcion_ejercida(self) -> float:
        return self.unidades_consumidas / self.unidades_vendidas

    @property
    def ingreso_por_ejercicio(self) -> float:
        return self.cobro_asignado * self.proporcion_ejercida

    @property
    def ingreso_por_breakage_proporcional(self) -> float:
        return self.cobro_asignado * self.breakage_estimado * self.proporcion_ejercida

    @property
    def ingreso_pedagogico(self) -> float:
        return min(
            self.cobro_asignado,
            self.ingreso_por_ejercicio + self.ingreso_por_breakage_proporcional,
        )

    @property
    def pasivo_contractual_pedagogico(self) -> float:
        return self.cobro_asignado - self.ingreso_pedagogico


@dataclass(frozen=True)
class EstadoOrden:
    orden: str
    pago: str
    settlement: str
    ledger: str
    wallet: str
    entitlement: str

    @property
    def conciliada(self) -> bool:
        if self.pago == "PAID":
            return self.ledger == "CREDITED" and self.entitlement == "DELIVERED"
        return self.ledger != "CREDITED" and self.entitlement != "DELIVERED"

    @property
    def excepcion(self) -> str:
        if self.conciliada:
            return ""
        if self.pago == "PAID" and self.ledger != "CREDITED":
            return "cobrado_no_acreditado"
        if self.ledger == "CREDITED" and self.entitlement != "DELIVERED":
            return "saldo_sin_entitlement"
        return "estado_inconsistente"


def caso_gameco() -> dict[str, object]:
    """Escenario sintético recurrente del laboratorio."""

    economia = EconomiaVirtual(
        stock_inicial=960_000,
        sources=100_000,
        sinks=60_000,
        volumen_transferido=240_000,
        saldos=(310_000, 180_000, 140_000, 90_000, 80_000, 70_000, 45_000, 35_000, 30_000, 20_000),
    )
    unit = UnitEconomics(10_000, 0.05, 12_000)
    obligacion = ObligacionVirtual(5_990, 1_000, 600, 0.15)
    excepcion = EstadoOrden("CREATED", "PAID", "SETTLED", "NOT_CREDITED", "EMPTY", "NOT_DELIVERED")
    return {
        "nivel_a": NivelGameco(),
        "nivel_b": NivelGameco(transferible=True),
        "nivel_c": NivelGameco(transferible=True, convertible=True, mercado_externo=True, payout=True),
        "economia": economia,
        "unit_economics": unit,
        "obligacion": obligacion,
        "excepcion": excepcion,
    }
