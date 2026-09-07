"""Conciliacion financiera de custodia con datos sinteticos.

El modulo separa tres universos que nunca deben netearse: activos propios,
activos custodiados por cuenta de clientes y obligaciones con esos clientes.
No se conecta a bancos, exchanges ni blockchains y no mueve fondos.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass


@dataclass(frozen=True)
class MovimientoDeLedger:
    apertura: int
    entradas: int
    salidas: int
    resultado_trading: int
    comisiones: int
    cierre_registrado: int

    @property
    def cierre_esperado(self) -> int:
        return (
            self.apertura
            + self.entradas
            - self.salidas
            + self.resultado_trading
            - self.comisiones
        )

    @property
    def diferencia(self) -> int:
        return self.cierre_registrado - self.cierre_esperado


@dataclass(frozen=True)
class PosicionCustodiada:
    fuente: str
    activo: str
    saldo: int
    no_disponible: int = 0

    def __post_init__(self) -> None:
        if self.saldo < 0 or self.no_disponible < 0:
            raise ValueError("los saldos no pueden ser negativos")
        if self.no_disponible > self.saldo:
            raise ValueError("lo no disponible no puede superar el saldo")

    @property
    def disponible(self) -> int:
        return self.saldo - self.no_disponible


@dataclass(frozen=True)
class EstadoDeReserva:
    activo: str
    pasivo_cliente: int
    activos_brutos: int
    activos_disponibles: int

    @property
    def cobertura_bruta(self) -> float:
        return self.activos_brutos / self.pasivo_cliente

    @property
    def cobertura_disponible(self) -> float:
        return self.activos_disponibles / self.pasivo_cliente

    @property
    def diferencia_disponible(self) -> int:
        return self.activos_disponibles - self.pasivo_cliente


class ConciliacionDeCustodia:
    """Concilia pasivos por cliente contra activos externos verificables."""

    def __init__(
        self,
        pasivos_cliente: dict[str, int],
        posiciones: list[PosicionCustodiada],
    ) -> None:
        if not pasivos_cliente or any(v <= 0 for v in pasivos_cliente.values()):
            raise ValueError("cada pasivo de cliente debe ser positivo")
        self.pasivos_cliente = dict(pasivos_cliente)
        self.posiciones = list(posiciones)

    def por_activo(self) -> list[EstadoDeReserva]:
        brutos: dict[str, int] = defaultdict(int)
        disponibles: dict[str, int] = defaultdict(int)
        for posicion in self.posiciones:
            brutos[posicion.activo] += posicion.saldo
            disponibles[posicion.activo] += posicion.disponible
        return [
            EstadoDeReserva(activo, pasivo, brutos[activo], disponibles[activo])
            for activo, pasivo in sorted(self.pasivos_cliente.items())
        ]

    @property
    def pasivos_totales(self) -> int:
        return sum(self.pasivos_cliente.values())

    @property
    def activos_brutos(self) -> int:
        return sum(p.saldo for p in self.posiciones)

    @property
    def activos_disponibles(self) -> int:
        return sum(p.disponible for p in self.posiciones)

    @property
    def diferencia_disponible(self) -> int:
        return self.activos_disponibles - self.pasivos_totales


@dataclass(frozen=True)
class BalanceInstitucional:
    activos_propios: int
    pasivos_propios: int
    activos_custodiados: int
    pasivos_con_clientes: int

    @property
    def patrimonio(self) -> int:
        return self.activos_propios - self.pasivos_propios

    @property
    def diferencia_de_custodia(self) -> int:
        return self.activos_custodiados - self.pasivos_con_clientes

    @property
    def activos_publicables_en_balance(self) -> int:
        """Los activos segregados de clientes no son fondos propios."""
        return self.activos_propios


@dataclass(frozen=True)
class OperacionDeTrading:
    instrumento: str
    libro: str
    nocional: int
    resultado: int
    pasivo_creado: int = 0
    colateral_inmovilizado: int = 0

    @property
    def riesgos(self) -> tuple[str, ...]:
        base = {"mercado", "liquidez", "operacional"}
        if self.instrumento in {"margin", "futures", "derivatives"}:
            base.update({"contraparte", "apalancamiento"})
        if self.libro == "clientes":
            base.update({"custodia", "fraude"})
        return tuple(sorted(base))


ROLES_REQUERIDOS = (
    "maker",
    "checker",
    "approver",
    "executor",
    "reconciler",
    "auditor",
)


def validar_segregacion_de_funciones(asignaciones: dict[str, str]) -> list[str]:
    """Devuelve defectos: faltantes o una persona concentrando funciones."""
    defectos = [f"falta el rol {rol}" for rol in ROLES_REQUERIDOS if rol not in asignaciones]
    personas: dict[str, list[str]] = defaultdict(list)
    for rol, persona in asignaciones.items():
        personas[persona].append(rol)
    for persona, roles in personas.items():
        if len(roles) > 1:
            defectos.append(f"{persona} concentra: {', '.join(sorted(roles))}")
    return defectos


def brecha_de_liquidez(recursos_disponibles: int, salidas_24h: int) -> int:
    """Importe que falta; un superavit se informa como cero, no como brecha negativa."""
    if recursos_disponibles < 0 or salidas_24h < 0:
        raise ValueError("recursos y salidas no pueden ser negativos")
    return max(salidas_24h - recursos_disponibles, 0)


def caso_custodia_andina() -> tuple[
    MovimientoDeLedger,
    ConciliacionDeCustodia,
    BalanceInstitucional,
    list[OperacionDeTrading],
]:
    """Caso integrador oficial, expresado en USD equivalentes."""
    ledger = MovimientoDeLedger(
        apertura=6_800_000,
        entradas=1_000_000,
        salidas=600_000,
        resultado_trading=-150_000,
        comisiones=50_000,
        cierre_registrado=7_000_000,
    )
    conciliacion = ConciliacionDeCustodia(
        {"BTC": 2_400_000, "ETH": 1_600_000, "USDC": 3_000_000},
        [
            PosicionCustodiada("blockchain-cold", "BTC", 2_100_000),
            PosicionCustodiada("exchange", "BTC", 300_000, 200_000),
            PosicionCustodiada("blockchain-cold", "ETH", 1_300_000),
            PosicionCustodiada("exchange", "ETH", 350_000, 100_000),
            PosicionCustodiada("blockchain-hot", "USDC", 1_500_000),
            PosicionCustodiada("bank", "USDC", 700_000),
            PosicionCustodiada("exchange", "USDC", 900_000, 400_000),
        ],
    )
    balance = BalanceInstitucional(
        activos_propios=1_800_000,
        pasivos_propios=1_350_000,
        activos_custodiados=conciliacion.activos_disponibles,
        pasivos_con_clientes=conciliacion.pasivos_totales,
    )
    operaciones = [
        OperacionDeTrading("spot", "clientes", 800_000, -50_000),
        OperacionDeTrading("margin", "clientes", 1_200_000, -100_000, 150_000, 400_000),
        OperacionDeTrading("futures", "propio", 900_000, -180_000, 250_000, 250_000),
        OperacionDeTrading("derivatives", "propio", 700_000, 30_000, 100_000, 100_000),
    ]
    return ledger, conciliacion, balance, operaciones
