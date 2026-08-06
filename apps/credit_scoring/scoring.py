from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Applicant:
    monthly_income: float
    monthly_debt: float
    requested_amount: float
    term_months: int
    years_employed: int
    past_due_events: int

@dataclass(frozen=True)
class Decision:
    score: int
    band: str
    reasons: tuple[str, ...]


def evaluate(applicant: Applicant) -> Decision:
    if applicant.monthly_income <= 0 or applicant.term_months <= 0:
        raise ValueError("Ingreso y plazo deben ser positivos")
    score = 500
    reasons: list[str] = []
    ratio = applicant.monthly_debt / applicant.monthly_income
    if ratio <= 0.25:
        score += 100; reasons.append("Carga financiera baja")
    elif ratio <= 0.45:
        score += 40; reasons.append("Carga financiera moderada")
    else:
        score -= 120; reasons.append("Carga financiera alta")
    if applicant.years_employed >= 3:
        score += 60; reasons.append("Estabilidad laboral")
    elif applicant.years_employed == 0:
        score -= 40; reasons.append("Sin antigüedad laboral declarada")
    score -= min(applicant.past_due_events * 70, 280)
    if applicant.past_due_events:
        reasons.append("Existen eventos de mora")
    burden = applicant.requested_amount / (applicant.monthly_income * applicant.term_months)
    if burden > 1.0:
        score -= 80; reasons.append("Monto alto respecto del ingreso y plazo")
    score = max(0, min(1000, score))
    band = "bajo" if score >= 700 else "medio" if score >= 550 else "alto"
    return Decision(score, band, tuple(reasons))
