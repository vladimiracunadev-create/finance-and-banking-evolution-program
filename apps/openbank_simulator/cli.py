from __future__ import annotations
import argparse
from pathlib import Path
from bank import Bank

DB = Path(__file__).with_name("openbank.db")


def demo(bank: Bank) -> None:
    bank.initialize()
    alice = bank.create_customer("Ana Demo")
    bob = bank.create_customer("Bruno Demo")
    a1 = bank.open_account(alice, 1000000)
    a2 = bank.open_account(bob, 250000)
    bank.transfer(a1, a2, 125000, "Pago educativo")
    bank.create_loan(bob, 1800000, 0.16, 24)
    print("Banco virtual creado")
    print(bank.summary())
    print({"cuenta_ana": bank.balance(a1), "cuenta_bruno": bank.balance(a2)})


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["demo", "reset", "summary"])
    args = parser.parse_args()
    bank = Bank(DB)
    if args.command == "reset":
        if DB.exists(): DB.unlink()
        print("Base reiniciada")
    elif args.command == "demo":
        if DB.exists(): DB.unlink()
        demo(bank)
    else:
        bank.initialize(); print(bank.summary())

if __name__ == "__main__":
    main()
