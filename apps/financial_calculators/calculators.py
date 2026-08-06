from __future__ import annotations
from dataclasses import dataclass


def compound_interest(principal: float, annual_rate: float, years: float, compounds_per_year: int = 1) -> float:
    if principal < 0 or years < 0 or compounds_per_year <= 0:
        raise ValueError("Parámetros inválidos")
    return principal * (1 + annual_rate / compounds_per_year) ** (compounds_per_year * years)


def present_value(future_value: float, rate: float, periods: int) -> float:
    if periods < 0 or rate <= -1:
        raise ValueError("Parámetros inválidos")
    return future_value / ((1 + rate) ** periods)


def fixed_payment(principal: float, periodic_rate: float, periods: int) -> float:
    if principal < 0 or periods <= 0 or periodic_rate <= -1:
        raise ValueError("Parámetros inválidos")
    if periodic_rate == 0:
        return principal / periods
    factor = (1 + periodic_rate) ** periods
    return principal * periodic_rate * factor / (factor - 1)


@dataclass(frozen=True)
class AmortizationRow:
    period: int
    payment: float
    interest: float
    principal: float
    balance: float


def amortization_schedule(principal: float, annual_rate: float, months: int) -> list[AmortizationRow]:
    monthly_rate = annual_rate / 12
    payment = fixed_payment(principal, monthly_rate, months)
    balance = principal
    rows: list[AmortizationRow] = []
    for period in range(1, months + 1):
        interest = balance * monthly_rate
        principal_paid = payment - interest
        balance = max(0.0, balance - principal_paid)
        rows.append(AmortizationRow(period, payment, interest, principal_paid, balance))
    return rows
