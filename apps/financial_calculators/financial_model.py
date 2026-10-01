"""Modelo empresarial trazable: supuestos, calculos, proyeccion y capital.

El modulo evita mezclar datos observados, supuestos, formulas y resultados. El
caso integrado es deliberadamente pequeno para que pueda reconstruirse en una
planilla antes de ejecutarlo aqui.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum
from math import ceil


class CostBehavior(str, Enum):
    FIXED = "fijo"
    VARIABLE = "variable"
    SEMIFIXED = "semifijo"


class CostTraceability(str, Enum):
    DIRECT = "directo"
    INDIRECT = "indirecto"


class DecisionRelevance(str, Enum):
    SUNK = "hundido"
    INCREMENTAL = "incremental"


class AccountingTreatment(str, Enum):
    CAPEX = "CAPEX"
    OPEX = "OPEX"


@dataclass(frozen=True)
class CostItem:
    name: str
    amount: float
    unit: str
    behavior: CostBehavior
    traceability: CostTraceability
    relevance: DecisionRelevance
    treatment: AccountingTreatment
    decision_use: str


@dataclass(frozen=True)
class CostStructure:
    variable_cost_per_unit: float
    fixed_opex_monthly: float
    semifixed_base_monthly: float
    semifixed_step_monthly: float
    customers_per_step: int
    initial_capex: float
    depreciation_months: int
    sunk_cost_before_decision: float = 0.0

    def __post_init__(self) -> None:
        numeric = (
            self.variable_cost_per_unit,
            self.fixed_opex_monthly,
            self.semifixed_base_monthly,
            self.semifixed_step_monthly,
            self.initial_capex,
            self.sunk_cost_before_decision,
        )
        if any(value < 0 for value in numeric):
            raise ValueError("Los costos no pueden ser negativos")
        if self.customers_per_step <= 0 or self.depreciation_months <= 0:
            raise ValueError("La capacidad por tramo y la vida util deben ser positivas")

    def semifixed_cost(self, customers: float) -> float:
        steps = max(1, ceil(customers / self.customers_per_step))
        return self.semifixed_base_monthly + (steps - 1) * self.semifixed_step_monthly

    def classify(self) -> tuple[CostItem, ...]:
        """Devuelve la clasificacion que conecta cada costo con una decision."""
        return (
            CostItem(
                "insumo por unidad",
                self.variable_cost_per_unit,
                "por unidad vendida",
                CostBehavior.VARIABLE,
                CostTraceability.DIRECT,
                DecisionRelevance.INCREMENTAL,
                AccountingTreatment.OPEX,
                "entra al margen de contribucion y al precio minimo",
            ),
            CostItem(
                "personal e infraestructura base",
                self.fixed_opex_monthly,
                "por mes",
                CostBehavior.FIXED,
                CostTraceability.INDIRECT,
                DecisionRelevance.INCREMENTAL,
                AccountingTreatment.OPEX,
                "determina la escala necesaria para alcanzar equilibrio",
            ),
            CostItem(
                "capacidad operativa por tramos",
                self.semifixed_base_monthly,
                "base mensual mas escalones",
                CostBehavior.SEMIFIXED,
                CostTraceability.INDIRECT,
                DecisionRelevance.INCREMENTAL,
                AccountingTreatment.OPEX,
                "obliga a comprobar el salto de costo antes de expandir",
            ),
            CostItem(
                "equipamiento inicial",
                self.initial_capex,
                "desembolso inicial",
                CostBehavior.FIXED,
                CostTraceability.DIRECT,
                DecisionRelevance.INCREMENTAL,
                AccountingTreatment.CAPEX,
                "consume caja al inicio y se deprecia durante su vida util",
            ),
            CostItem(
                "estudio ya pagado",
                self.sunk_cost_before_decision,
                "incurrido antes de decidir",
                CostBehavior.FIXED,
                CostTraceability.DIRECT,
                DecisionRelevance.SUNK,
                AccountingTreatment.OPEX,
                "se documenta, pero se excluye de la decision futura",
            ),
        )


@dataclass(frozen=True)
class BusinessAssumptions:
    market_customers: int
    initial_customers: float
    qualified_leads_monthly: float
    conversion_rate: float
    churn_rate_monthly: float
    purchases_per_customer: float
    price_per_unit: float
    capacity_customers: int
    months: int
    initial_cash: float
    minimum_cash_reserve: float
    receivable_days: float
    inventory_days: float
    payable_days: float
    acquisition_spend_monthly: float | None
    recurring_relationship: bool
    costs: CostStructure

    def __post_init__(self) -> None:
        if self.market_customers <= 0 or self.capacity_customers <= 0 or self.months <= 0:
            raise ValueError("Mercado, capacidad y meses deben ser positivos")
        if self.initial_customers < 0 or self.initial_customers > self.capacity_customers:
            raise ValueError("Los clientes iniciales deben caber en la capacidad")
        if not 0 <= self.conversion_rate <= 1 or not 0 <= self.churn_rate_monthly <= 1:
            raise ValueError("Conversion y abandono deben estar entre 0 y 1")
        if self.purchases_per_customer < 0 or self.price_per_unit < 0:
            raise ValueError("Frecuencia y precio no pueden ser negativos")
        if min(self.initial_cash, self.minimum_cash_reserve) < 0:
            raise ValueError("La caja no puede ser negativa")
        if min(self.receivable_days, self.inventory_days, self.payable_days) < 0:
            raise ValueError("Los dias de capital de trabajo no pueden ser negativos")
        if self.acquisition_spend_monthly is not None and self.acquisition_spend_monthly < 0:
            raise ValueError("El gasto de adquisicion no puede ser negativo")


@dataclass(frozen=True)
class Scenario:
    name: str
    leads_multiplier: float = 1.0
    conversion_multiplier: float = 1.0
    price_multiplier: float = 1.0
    variable_cost_multiplier: float = 1.0
    extra_receivable_days: float = 0.0


SCENARIOS = {
    "conservador": Scenario("conservador", 0.80, 0.85, 0.95, 1.10, 15.0),
    "base": Scenario("base"),
    "expansivo": Scenario("expansivo", 1.20, 1.10, 1.03, 0.97, -5.0),
}


@dataclass(frozen=True)
class MonthlyProjection:
    month: int
    customers: float
    new_customers: float
    units: float
    revenue: float
    variable_cost: float
    contribution_margin: float
    fixed_opex: float
    semifixed_opex: float
    ebitda: float
    depreciation: float
    operating_result: float
    working_capital: float
    working_capital_change: float
    capex: float
    net_cash_flow: float
    closing_cash: float


@dataclass(frozen=True)
class UnitEconomics:
    unit_price: float
    unit_revenue: float
    unit_variable_cost: float
    unit_contribution_margin: float
    contribution_margin_ratio: float | None
    cac: float | None
    ltv: float | None
    payback_months: float | None
    applicability: tuple[str, ...]


@dataclass(frozen=True)
class ProjectionSummary:
    scenario: str
    initial_investment: float
    peak_working_capital: float
    maximum_accumulated_deficit: float
    financing_need: float
    break_even_units_monthly: int | None
    operating_break_even_month: int | None
    runway_months: int | None
    total_revenue: float
    total_ebitda: float
    ending_cash: float


def integrated_case(months: int = 12) -> BusinessAssumptions:
    """Caso Taller Circular: valores pequenos, explicitos y reproducibles."""
    return BusinessAssumptions(
        market_customers=5_000,
        initial_customers=25,
        qualified_leads_monthly=140,
        conversion_rate=0.20,
        churn_rate_monthly=0.04,
        purchases_per_customer=2,
        price_per_unit=45,
        capacity_customers=500,
        months=months,
        initial_cash=12_000,
        minimum_cash_reserve=3_000,
        receivable_days=15,
        inventory_days=10,
        payable_days=20,
        acquisition_spend_monthly=900,
        recurring_relationship=True,
        costs=CostStructure(
            variable_cost_per_unit=18,
            fixed_opex_monthly=3_500,
            semifixed_base_monthly=800,
            semifixed_step_monthly=1_200,
            customers_per_step=200,
            initial_capex=18_000,
            depreciation_months=36,
            sunk_cost_before_decision=1_500,
        ),
    )


def _scenario_values(
    assumptions: BusinessAssumptions, scenario: Scenario
) -> tuple[float, float, float, float, float]:
    leads = assumptions.qualified_leads_monthly * scenario.leads_multiplier
    conversion = min(1.0, assumptions.conversion_rate * scenario.conversion_multiplier)
    price = assumptions.price_per_unit * scenario.price_multiplier
    variable_cost = assumptions.costs.variable_cost_per_unit * scenario.variable_cost_multiplier
    receivable_days = max(0.0, assumptions.receivable_days + scenario.extra_receivable_days)
    return leads, conversion, price, variable_cost, receivable_days


def project(
    assumptions: BusinessAssumptions, scenario: Scenario = SCENARIOS["base"]
) -> list[MonthlyProjection]:
    leads, conversion, price, variable_cost_unit, receivable_days = _scenario_values(
        assumptions, scenario
    )
    rows: list[MonthlyProjection] = []
    previous_customers = assumptions.initial_customers
    previous_working_capital = 0.0
    closing_cash = assumptions.initial_cash
    fixed_opex = assumptions.costs.fixed_opex_monthly + (
        assumptions.acquisition_spend_monthly or 0.0
    )

    for month in range(1, assumptions.months + 1):
        retained = previous_customers * (1 - assumptions.churn_rate_monthly)
        possible_new = leads * conversion
        customer_limit = min(assumptions.market_customers, assumptions.capacity_customers)
        new_customers = min(possible_new, max(0.0, customer_limit - retained))
        customers = retained + new_customers
        units = customers * assumptions.purchases_per_customer
        revenue = units * price
        variable_cost = units * variable_cost_unit
        contribution = revenue - variable_cost
        semifixed = assumptions.costs.semifixed_cost(customers)
        ebitda = contribution - fixed_opex - semifixed
        depreciation = assumptions.costs.initial_capex / assumptions.costs.depreciation_months
        operating_result = ebitda - depreciation
        receivables = revenue * receivable_days / 30
        inventory = variable_cost * assumptions.inventory_days / 30
        payables = variable_cost * assumptions.payable_days / 30
        working_capital = receivables + inventory - payables
        working_capital_change = working_capital - previous_working_capital
        capex = assumptions.costs.initial_capex if month == 1 else 0.0
        net_cash_flow = ebitda - working_capital_change - capex
        closing_cash += net_cash_flow
        rows.append(
            MonthlyProjection(
                month,
                customers,
                new_customers,
                units,
                revenue,
                variable_cost,
                contribution,
                fixed_opex,
                semifixed,
                ebitda,
                depreciation,
                operating_result,
                working_capital,
                working_capital_change,
                capex,
                net_cash_flow,
                closing_cash,
            )
        )
        previous_customers = customers
        previous_working_capital = working_capital
    return rows


def unit_economics(
    assumptions: BusinessAssumptions, scenario: Scenario = SCENARIOS["base"]
) -> UnitEconomics:
    leads, conversion, price, variable_cost, _ = _scenario_values(assumptions, scenario)
    contribution = price - variable_cost
    ratio = contribution / price if price else None
    new_customers = leads * conversion
    messages: list[str] = []

    cac: float | None = None
    if assumptions.acquisition_spend_monthly is None:
        messages.append("CAC no aplica: no hay gasto de adquisicion atribuible")
    elif new_customers <= 0:
        messages.append("CAC no calculable: no hay clientes adquiridos")
    else:
        cac = assumptions.acquisition_spend_monthly / new_customers

    contribution_per_customer = contribution * assumptions.purchases_per_customer
    ltv: float | None = None
    if not assumptions.recurring_relationship:
        messages.append("LTV no aplica: no existe una relacion recurrente")
    elif assumptions.churn_rate_monthly <= 0:
        messages.append("LTV no calculable: falta una tasa de abandono finita")
    elif contribution_per_customer <= 0:
        messages.append("LTV no es util: el margen por cliente no es positivo")
    else:
        ltv = contribution_per_customer / assumptions.churn_rate_monthly

    payback: float | None = None
    if cac is None:
        messages.append("payback de CAC no aplica sin CAC")
    elif contribution_per_customer <= 0:
        messages.append("payback de CAC no existe con contribucion no positiva")
    else:
        payback = cac / contribution_per_customer

    if not messages:
        messages.append("CAC, LTV y payback aplican por adquisicion medible y relacion recurrente")
    return UnitEconomics(price, price, variable_cost, contribution, ratio, cac, ltv, payback, tuple(messages))


def break_even_units(
    assumptions: BusinessAssumptions, scenario: Scenario = SCENARIOS["base"]
) -> int | None:
    _, _, price, variable_cost, _ = _scenario_values(assumptions, scenario)
    contribution = price - variable_cost
    if contribution <= 0 or assumptions.purchases_per_customer <= 0:
        return None
    fixed = assumptions.costs.fixed_opex_monthly + (assumptions.acquisition_spend_monthly or 0.0)
    maximum_units = ceil(assumptions.capacity_customers * assumptions.purchases_per_customer)
    for units in range(maximum_units + 1):
        customers = units / assumptions.purchases_per_customer
        required = fixed + assumptions.costs.semifixed_cost(customers)
        if units * contribution >= required:
            return units
    return None


def summarize(
    assumptions: BusinessAssumptions, scenario: Scenario = SCENARIOS["base"]
) -> ProjectionSummary:
    rows = project(assumptions, scenario)
    minimum_cash = min(row.closing_cash for row in rows)
    deficit = max(0.0, -minimum_cash)
    financing_need = max(0.0, assumptions.minimum_cash_reserve - minimum_cash)
    operating_break_even = next((row.month for row in rows if row.ebitda >= 0), None)
    reserve_breach = next(
        (row.month for row in rows if row.closing_cash < assumptions.minimum_cash_reserve), None
    )
    runway = None if reserve_breach is None else reserve_breach - 1
    return ProjectionSummary(
        scenario.name,
        assumptions.costs.initial_capex,
        max(row.working_capital for row in rows),
        deficit,
        financing_need,
        break_even_units(assumptions, scenario),
        operating_break_even,
        runway,
        sum(row.revenue for row in rows),
        sum(row.ebitda for row in rows),
        rows[-1].closing_cash,
    )


def price_sensitivity(
    assumptions: BusinessAssumptions, changes: tuple[float, ...] = (-0.10, 0.0, 0.10)
) -> list[ProjectionSummary]:
    """Mueve solo el precio; los escenarios multivariables se ejecutan despues."""
    return [
        summarize(assumptions, Scenario(f"precio {change:+.0%}", price_multiplier=1 + change))
        for change in changes
    ]


def with_months(assumptions: BusinessAssumptions, months: int) -> BusinessAssumptions:
    if months <= 0:
        raise ValueError("Los meses deben ser positivos")
    return replace(assumptions, months=months)


CALCULATION_RULES = (
    "clientes = clientes retenidos + leads x conversion, limitado por capacidad",
    "ventas = clientes x frecuencia; ingresos = ventas x precio",
    "margen de contribucion = ingresos - costo variable",
    "EBITDA = contribucion - OPEX fijo - OPEX semifijo",
    "resultado operativo = EBITDA - depreciacion del CAPEX",
    "capital de trabajo = cuentas por cobrar + inventario - proveedores",
    "caja = caja anterior + EBITDA - variacion de capital de trabajo - CAPEX",
    "financiamiento = reserva minima - peor saldo de caja, si es positivo",
)
