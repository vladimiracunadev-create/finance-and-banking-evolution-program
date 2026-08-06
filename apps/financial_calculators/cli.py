from __future__ import annotations
import argparse
from calculators import compound_interest, amortization_schedule


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

    args = parser.parse_args()
    if args.command == "compound":
        result = compound_interest(args.principal, args.rate, args.years, args.compounds)
        print(f"Valor futuro: {result:,.2f}")
    else:
        schedule = amortization_schedule(args.principal, args.annual_rate, args.months)
        print(f"Cuota: {schedule[0].payment:,.2f}")
        print("periodo,pago,interes,capital,saldo")
        for row in schedule:
            print(f"{row.period},{row.payment:.2f},{row.interest:.2f},{row.principal:.2f},{row.balance:.2f}")


if __name__ == "__main__":
    main()
