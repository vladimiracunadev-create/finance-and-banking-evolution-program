"""Panel de consentimientos por linea de comandos.

Demuestra lo que la clase 5 exige que se pueda demostrar: el segundo posterior
a una revocacion.

Uso:
    python apps/open_finance_sandbox/consent_dashboard/cli.py demo
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from apps.open_finance_sandbox import build  # noqa: E402
from apps.open_finance_sandbox.authorization_server import AuthError  # noqa: E402


def demo() -> int:
    sandbox = build()
    grant = sandbox.grant(
        ["accounts:list", "accounts:balances", "accounts:transactions"]
    )
    consent = sandbox.consents.get(grant.consent_id)

    print("PANEL DE CONSENTIMIENTOS")
    print(f"  proveedor:  {consent.provider_id}")
    print(f"  finalidad:  {consent.purpose}")
    print(f"  vigente hasta: {consent.expires_at.date().isoformat()}")
    print("  que puede ver:")
    for linea in consent.explain():
        print(f"    - {linea}")

    print("\nANTES DE REVOCAR")
    saldo = sandbox.bank.balances(grant.access_token, "acc_0100")["data"]
    print(f"  saldo contable: {saldo['booked_balance']} {saldo['currency']}")

    inicio = time.perf_counter()
    sandbox.consents.revoke(grant.consent_id, actor="cliente", reason="demo")
    try:
        sandbox.bank.balances(grant.access_token, "acc_0100")
    except AuthError as exc:
        transcurrido = (time.perf_counter() - inicio) * 1000
        print("\nDESPUES DE REVOCAR")
        print(f"  respuesta: {exc.code}")
        print(f"  retardo revocacion -> primer rechazo: {transcurrido:.3f} ms")
        return 0

    print("\nFALLO: el acceso siguio funcionando tras la revocacion")
    return 1


def main() -> int:
    if len(sys.argv) < 2 or sys.argv[1] != "demo":
        print(__doc__)
        return 2
    return demo()


if __name__ == "__main__":
    sys.exit(main())
