from __future__ import annotations
import argparse
import json
from dataclasses import asdict
from calculators import compound_interest, amortization_schedule
from financial_model import (
    CALCULATION_RULES,
    SCENARIOS,
    integrated_case,
    price_sensitivity,
    project,
    summarize,
    unit_economics,
)


def _print_model(args: argparse.Namespace) -> None:
    assumptions = integrated_case(args.months)
    scenario = SCENARIOS[args.scenario]
    rows = project(assumptions, scenario)
    economics = unit_economics(assumptions, scenario)
    summary = summarize(assumptions, scenario)
    sensitivity = price_sensitivity(assumptions)

    if args.format == "json":
        print(json.dumps({
            "INPUT": {"case": "Taller Circular", "market_customers": assumptions.market_customers},
            "ASSUMPTION": asdict(assumptions),
            "CALCULATION": {
                "rules": list(CALCULATION_RULES),
                "cost_classification": [
                    asdict(item) for item in assumptions.costs.classify()
                ],
            },
            "OUTPUT": {
                "unit_economics": asdict(economics),
                "projection": [asdict(row) for row in rows],
                "summary": asdict(summary),
                "price_sensitivity": [asdict(item) for item in sensitivity],
            },
        }, ensure_ascii=False, indent=2))
        return

    print("INPUT")
    print("  caso: Taller Circular (sintetico)")
    print(f"  mercado esperado: {assumptions.market_customers:,.0f} clientes")
    print("ASSUMPTION")
    print(f"  clientes iniciales: {assumptions.initial_customers:,.0f}")
    print(f"  leads / conversion: {assumptions.qualified_leads_monthly:,.0f} / {assumptions.conversion_rate:.0%}")
    print(f"  precio / frecuencia: {assumptions.price_per_unit:,.2f} / {assumptions.purchases_per_customer:g}")
    print(f"  costo variable unitario: {assumptions.costs.variable_cost_per_unit:,.2f}")
    print(f"  OPEX fijo / semifijo base: {assumptions.costs.fixed_opex_monthly:,.2f} / {assumptions.costs.semifixed_base_monthly:,.2f}")
    print(f"  CAPEX / caja / reserva: {assumptions.costs.initial_capex:,.2f} / {assumptions.initial_cash:,.2f} / {assumptions.minimum_cash_reserve:,.2f}")
    print(f"  cobro / inventario / pago: {assumptions.receivable_days:g} / {assumptions.inventory_days:g} / {assumptions.payable_days:g} dias")
    print(f"  escenario: {scenario.name}")
    print("CALCULATION")
    print("  clasificacion de costos:")
    for item in assumptions.costs.classify():
        print(
            f"    {item.name}: {item.behavior.value}, {item.traceability.value}, "
            f"{item.relevance.value}, {item.treatment.value}"
        )
    for rule in CALCULATION_RULES:
        print(f"  - {rule}")
    print("OUTPUT")
    print(f"  margen unitario: {economics.unit_contribution_margin:,.2f}")
    print(f"  CAC / LTV / payback: {economics.cac:,.2f} / {economics.ltv:,.2f} / {economics.payback_months:,.2f} meses")
    for message in economics.applicability:
        print(f"  aplicabilidad: {message}")
    print(f"  punto de equilibrio: {summary.break_even_units_monthly} unidades/mes")
    print(f"  mes de equilibrio operativo: {summary.operating_break_even_month or 'no alcanzado'}")
    print(f"  inversion inicial: {summary.initial_investment:,.2f}")
    print(f"  capital de trabajo maximo: {summary.peak_working_capital:,.2f}")
    print(f"  deficit maximo acumulado: {summary.maximum_accumulated_deficit:,.2f}")
    print(f"  necesidad de financiamiento: {summary.financing_need:,.2f}")
    print(f"  runway: {summary.runway_months if summary.runway_months is not None else 'no aplica'}")
    print("  presupuesto y proyeccion mensual:")
    print("    mes clientes ingresos contribucion EBITDA capital_trabajo caja")
    for row in rows:
        print(
            f"    {row.month:>3} {row.customers:>8.1f} {row.revenue:>9.2f} "
            f"{row.contribution_margin:>12.2f} {row.ebitda:>9.2f} "
            f"{row.working_capital:>15.2f} {row.closing_cash:>10.2f}"
        )
    print("  sensibilidad de una variable (precio):")
    for item in sensitivity:
        print(f"    {item.scenario}: EBITDA {item.total_ebitda:,.2f}; capital {item.financing_need:,.2f}")
    print("  escenarios coherentes:")
    for name, configured in SCENARIOS.items():
        item = summarize(assumptions, configured)
        print(f"    {name}: ingresos {item.total_revenue:,.2f}; EBITDA {item.total_ebitda:,.2f}; capital {item.financing_need:,.2f}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculadoras financieras educativas")
    sub = parser.add_subparsers(dest="command", required=True)

    compound = sub.add_parser("compound")
    compound.add_argument("--principal", type=float, required=True)
    compound.add_argument("--rate", type=float, required=True)
    compound.add_argument("--years", type=float, required=True)
    compound.add_argument("--compounds", type=int, default=1)

    loan = sub.add_parser("loan")
    loan.add_argument("--principal", type=float, required=True)
    loan.add_argument("--annual-rate", type=float, required=True)
    loan.add_argument("--months", type=int, required=True)

    model = sub.add_parser("business-model", help="proyeccion trazable del caso integrador")
    model.add_argument("--scenario", choices=tuple(SCENARIOS), default="base")
    model.add_argument("--months", type=int, default=12)
    model.add_argument("--format", choices=("text", "json"), default="text")

    args = parser.parse_args()
    if args.command == "compound":
        result = compound_interest(args.principal, args.rate, args.years, args.compounds)
        print(f"Valor futuro: {result:,.2f}")
    elif args.command == "loan":
        schedule = amortization_schedule(args.principal, args.annual_rate, args.months)
        print(f"Cuota: {schedule[0].payment:,.2f}")
        print("periodo,pago,interes,capital,saldo")
        for row in schedule:
            print(f"{row.period},{row.payment:.2f},{row.interest:.2f},{row.principal:.2f},{row.balance:.2f}")
    else:
        _print_model(args)


if __name__ == "__main__":
    main()
