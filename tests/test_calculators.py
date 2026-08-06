from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parents[1] / "apps" / "financial_calculators"))
from calculators import compound_interest, present_value, fixed_payment, amortization_schedule


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
