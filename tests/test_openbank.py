from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parents[1] / "apps" / "openbank_simulator"))
from bank import Bank


def test_transfer(tmp_path):
    bank = Bank(tmp_path / "bank.db")
    bank.initialize()
    c1 = bank.create_customer("Uno")
    c2 = bank.create_customer("Dos")
    a1 = bank.open_account(c1, 1000)
    a2 = bank.open_account(c2, 0)
    bank.transfer(a1, a2, 300)
    assert bank.balance(a1) == 700
    assert bank.balance(a2) == 300
