"""Proveedor de servicios basados en informacion (el tercero).

Consume la API del entorno con el minimo de datos necesario para su finalidad.
Es la pieza donde se demuestra la minimizacion de la Parte 17, clase 12: el
producto declara su formula, deriva de ella el dato minimo y DESCARTA en la
ingesta cualquier campo que no la alimente, aunque el proveedor lo envie.
"""

from __future__ import annotations

from decimal import Decimal

# Campos de contraparte: identifican a una persona que no consintio. El producto
# no los necesita para su formula, asi que no se almacenan.
CAMPOS_DESCARTADOS = frozenset({"counterparty_name", "counterparty_account", "narrative"})


def ingest(movimientos: list[dict]) -> list[dict]:
    """Descarta los campos que la finalidad no necesita.

    Se descarta en la INGESTA, no en la presentacion: si el dato se almacena y
    solo se oculta, sigue estando cuando haya una brecha.
    """
    return [
        {k: v for k, v in movimiento.items() if k not in CAMPOS_DESCARTADOS}
        for movimiento in movimientos
    ]


def savings_capacity(movimientos: list[dict]) -> dict[str, str]:
    """Capacidad de ahorro mensual segun la formula de la clase 9.

    capacidad = ingreso recurrente - gasto recurrente - servicio de deuda

    El entorno no expone seguros, asi que la prima no entra. Esa limitacion se
    devuelve en la respuesta, no en un pie de pagina: es parte del producto.
    """
    limpios = ingest(movimientos)
    meses = {m["booking_date"][:7] for m in limpios} or {"2026-01"}
    ingresos = sum(Decimal(m["amount"]) for m in limpios if Decimal(m["amount"]) > 0)
    gastos = sum(Decimal(m["amount"]) for m in limpios if Decimal(m["amount"]) < 0)
    capacidad = (ingresos + gastos) / len(meses)
    return {
        "months_observed": str(len(meses)),
        "monthly_income": f"{ingresos / len(meses):.2f}",
        "monthly_expense": f"{abs(gastos) / len(meses):.2f}",
        "savings_capacity": f"{capacidad:.2f}",
        "limitation": (
            "no vemos los seguros que pagas fuera de tus cuentas; "
            "si tienes alguno, tu capacidad real es algo menor"
        ),
    }
