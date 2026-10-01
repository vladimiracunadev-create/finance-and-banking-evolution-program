from pathlib import Path
import sys
from dataclasses import replace
sys.path.insert(0, str(Path(__file__).parents[1] / "apps" / "financial_calculators"))
from calculators import compound_interest, present_value, fixed_payment, amortization_schedule
from financial_model import (
    AccountingTreatment,
    CostBehavior,
    DecisionRelevance,
    CostTraceability,
    SCENARIOS,
    break_even_units,
    integrated_case,
    price_sensitivity,
    project,
    summarize,
    unit_economics,
)


def test_compound_interest():
    assert round(compound_interest(100, 0.10, 2), 2) == 121.00


def test_present_value():
    assert round(present_value(121, 0.10, 2), 2) == 100.00


def test_zero_rate_payment():
    assert fixed_payment(1200, 0, 12) == 100


def test_schedule_finishes_near_zero():
    rows = amortization_schedule(1000000, 0.12, 12)
    assert len(rows) == 12
    assert rows[-1].balance < 0.01


def test_cost_structure_covers_decision_classifications():
    items = integrated_case().costs.classify()
    assert {item.behavior for item in items} == {
        CostBehavior.FIXED,
        CostBehavior.VARIABLE,
        CostBehavior.SEMIFIXED,
    }
    assert {item.treatment for item in items} == {
        AccountingTreatment.CAPEX,
        AccountingTreatment.OPEX,
    }
    assert {item.traceability for item in items} == {
        CostTraceability.DIRECT,
        CostTraceability.INDIRECT,
    }
    assert {item.relevance for item in items} == {
        DecisionRelevance.SUNK,
        DecisionRelevance.INCREMENTAL,
    }


def test_sunk_cost_is_visible_but_does_not_change_projection():
    case = integrated_case()
    larger_sunk_cost = replace(
        case,
        costs=replace(case.costs, sunk_cost_before_decision=999_999),
    )
    assert project(case) == project(larger_sunk_cost)


def test_first_month_reconciles_assumptions_to_revenue_and_cash():
    case = integrated_case()
    first = project(case)[0]
    expected_customers = 25 * (1 - 0.04) + 140 * 0.20
    assert first.customers == expected_customers
    assert first.revenue == expected_customers * 2 * 45
    assert first.closing_cash == case.initial_cash + first.net_cash_flow


def test_unit_economics_use_contribution_not_revenue():
    economics = unit_economics(integrated_case())
    assert economics.unit_contribution_margin == 27
    assert round(economics.cac or 0, 2) == 32.14
    assert economics.ltv == 1_350
    assert round(economics.payback_months or 0, 3) == 0.595


def test_cac_ltv_and_payback_explain_when_they_do_not_apply():
    case = replace(
        integrated_case(),
        acquisition_spend_monthly=None,
        recurring_relationship=False,
    )
    economics = unit_economics(case)
    assert economics.cac is None
    assert economics.ltv is None
    assert economics.payback_months is None
    assert any("no aplica" in message for message in economics.applicability)


def test_break_even_includes_semifixed_cost_at_the_relevant_scale():
    assert break_even_units(integrated_case()) == 193


def test_summary_exposes_capital_need_and_break_even_moment():
    summary = summarize(integrated_case())
    assert summary.initial_investment == 18_000
    assert summary.peak_working_capital > 0
    assert summary.financing_need > summary.maximum_accumulated_deficit
    assert summary.operating_break_even_month == 3
    assert summary.runway_months == 0


def test_scenarios_order_revenue_and_capital_coherently():
    case = integrated_case()
    conservative = summarize(case, SCENARIOS["conservador"])
    base = summarize(case, SCENARIOS["base"])
    expansive = summarize(case, SCENARIOS["expansivo"])
    assert conservative.total_revenue < base.total_revenue < expansive.total_revenue
    assert conservative.financing_need > base.financing_need > expansive.financing_need


def test_price_sensitivity_changes_one_driver_and_keeps_three_points():
    case = integrated_case()
    summaries = price_sensitivity(case)
    assert [item.scenario for item in summaries] == [
        "precio -10%",
        "precio +0%",
        "precio +10%",
    ]
    assert summaries[0].total_ebitda < summaries[1].total_ebitda < summaries[2].total_ebitda
