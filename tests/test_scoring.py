from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parents[1] / "apps" / "credit_scoring"))
from scoring import Applicant, evaluate


def test_good_profile_scores_higher_than_risky():
    good = Applicant(2000, 200, 5000, 24, 5, 0)
    risky = Applicant(2000, 1300, 20000, 12, 0, 4)
    assert evaluate(good).score > evaluate(risky).score
