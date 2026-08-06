from scoring import Applicant, evaluate

sample = Applicant(
    monthly_income=1500000,
    monthly_debt=300000,
    requested_amount=4000000,
    term_months=24,
    years_employed=5,
    past_due_events=0,
)
print(evaluate(sample))
