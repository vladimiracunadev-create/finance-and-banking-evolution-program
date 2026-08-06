"""Ejecuta la bateria de conformidad y devuelve 1 si algun caso falla.

Uso:
    python apps/open_finance_sandbox/conformance_tests/run.py
"""

from __future__ import annotations

import sys
from pathlib import Path

# El script se invoca por ruta, no como modulo: hay que poner la raiz del
# repositorio en sys.path para que el paquete resuelva.
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from apps.open_finance_sandbox.conformance_tests import report, run  # noqa: E402


def main() -> int:
    cases = run()
    print(report(cases))
    fallidos = [c for c in cases if not c.passed]
    return 1 if fallidos else 0


if __name__ == "__main__":
    sys.exit(main())
