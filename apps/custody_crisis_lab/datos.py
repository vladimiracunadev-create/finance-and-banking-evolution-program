"""Carga de los datasets sinteticos de crisis de custodia.

Los CSV viven en datasets/synthetic/ y tienen su ficha en datasets/schemas/.
Cargarlos desde aqui garantiza que el codigo y los datos cuenten la misma
historia: una prueba de regresion compara los totales del CSV con
`caso_sintetico()`.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

from .entity import Custodio

RAIZ = Path(__file__).resolve().parents[2]
BALANCE = RAIZ / "datasets" / "synthetic" / "custody_crisis_balance_synthetic.csv"
ESCENARIOS = RAIZ / "datasets" / "synthetic" / "custody_crisis_scenarios_synthetic.csv"


@dataclass(frozen=True)
class Escenario:
    scenario_id: str
    nombre: str
    sustraido: float
    congelado: float
    p_restitucion: float
    parte_liquida: float
    r0: float
    k: float
    pausa_dias: int
    descuento: float


def _filas(ruta: Path) -> list[dict[str, str]]:
    with ruta.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def cargar_entidad(ruta: Path = BALANCE) -> Custodio:
    liquidos = no_liquidos = pasivos = proteccion = 0.0
    for fila in _filas(ruta):
        monto = float(fila["amount_musd"])
        if fila["side"] == "asset" and fila["liquidity"] == "liquid":
            liquidos += monto
        elif fila["side"] == "asset" and fila["liquidity"] == "non_liquid":
            no_liquidos += monto
        elif fila["side"] == "liability":
            pasivos += monto
        elif fila["side"] == "protection":
            proteccion += monto
        else:
            raise ValueError(f"fila no reconocida: {fila['line_id']}")
    return Custodio(liquidos, no_liquidos, pasivos, proteccion)


def cargar_escenarios(ruta: Path = ESCENARIOS) -> dict[str, Escenario]:
    resultado = {}
    for f in _filas(ruta):
        resultado[f["scenario_id"]] = Escenario(
            scenario_id=f["scenario_id"],
            nombre=f["name"],
            sustraido=float(f["stolen_musd"]),
            congelado=float(f["frozen_musd"]),
            p_restitucion=float(f["restitution_prob"]),
            parte_liquida=float(f["liquid_share_of_loss"]),
            r0=float(f["run_base_rate"]),
            k=float(f["run_sensitivity"]),
            pausa_dias=int(f["pause_days"]),
            descuento=float(f["sale_haircut"]),
        )
    return resultado
