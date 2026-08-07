"""Laboratorio de pagos transfronterizos de la Parte 18.

Reune los seis componentes en un objeto para que los laboratorios y las pruebas
monten un escenario completo sin ceremonia:

    lab = build()
    traza, asientos = lab.pagar("CL-VN", 10_000, "2026-06-16T16:40:00")

No hay red, no hay credenciales reales, no se mueven fondos y todos los datos
son sinteticos.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from pathlib import Path

from .fast_payment_link import Cotizacion, Cuenta, Directorio, Enlace, subastar
from .flows import Asiento, PagoEnCadena, Plaza, Traza, cuadra
from .iso20022 import Orden, Parte, construir_pacs008, pacs002, transitar, validar
from .remittances import Ruta as RutaRemesa
from .remittances import Tramo, comparar as comparar_remesas
from .routing_engine import Decision, Pago, Pesos, Ruta, elegir
from .screening import Designado, evaluar, medir, prueba_retrospectiva
from .settlement import (
    Operacion,
    SistemaLiquidacion,
    exposicion_maxima,
    exposicion_por_contraparte,
    liquidar_pvp,
    netting_multilateral,
    ratio_netting,
)
from .stablecoin_route import (
    RutaClasica,
    RutaStablecoin,
    comparar as comparar_rutas,
    descomponer_ahorro,
    enrutar,
    porcentaje_atribuible_al_registro,
)

DATA = Path(__file__).resolve().parent / "data"


def _cargar(nombre: str):
    return json.loads((DATA / nombre).read_text(encoding="utf-8"))


@dataclass
class Laboratorio:
    plazas: dict[str, Plaza]
    corredores: dict[str, list[str]]
    rutas: list[Ruta]
    directorio: Directorio

    def pagar(
        self,
        corredor: str,
        importe: float,
        ordenado: str,
        alerta_en: int | None = None,
    ) -> tuple[Traza, list[Asiento]]:
        cadena = [self.plazas[c] for c in self.corredores[corredor]]
        motor = PagoEnCadena(cadena)
        return motor.ejecutar(importe, datetime.fromisoformat(ordenado), alerta_en)

    def enrutar(self, pago: Pago, pesos: Pesos | None = None) -> Decision:
        return elegir(pago, self.rutas, pesos)

    def rutas_de(self, corredor: str) -> list[Ruta]:
        return [r for r in self.rutas if r.corredor == corredor]


def build() -> Laboratorio:
    plazas = {
        p["codigo"]: Plaza(
            codigo=p["codigo"],
            huso=p["huso"],
            apertura=p["apertura"],
            cierre=p["cierre"],
            minutos_liquidacion=p["minutos_liquidacion"],
            festivos=frozenset(p.get("festivos", [])),
        )
        for p in _cargar("plazas.json")
    }
    corredores = _cargar("corredores.json")
    rutas = [
        Ruta(
            nombre=r["nombre"],
            tipo=r["tipo"],
            corredor=r["corredor"],
            importe_maximo=r["importe_maximo"],
            monedas=frozenset(r["monedas"]),
            canales=frozenset(r["canales"]),
            controles_soportados=frozenset(r["controles_soportados"]),
            coste_fijo=r["coste_fijo"],
            coste_variable=r["coste_variable"],
            diferencial_pb=r["diferencial_pb"],
            plazo_p50_h=r["plazo_p50_h"],
            plazo_p95_h=r["plazo_p95_h"],
            riesgo=r["riesgo"],
            disponibilidad=r["disponibilidad"],
        )
        for r in _cargar("rutas.json")
    ]
    directorio = Directorio()
    for cuenta in _cargar("alias.json"):
        directorio.registrar(Cuenta(**cuenta))
    return Laboratorio(plazas, corredores, rutas, directorio)


__all__ = [
    "Asiento",
    "Cotizacion",
    "Cuenta",
    "Decision",
    "Designado",
    "Directorio",
    "Enlace",
    "Laboratorio",
    "Operacion",
    "Orden",
    "Pago",
    "Parte",
    "Pesos",
    "Plaza",
    "Ruta",
    "RutaClasica",
    "RutaRemesa",
    "RutaStablecoin",
    "SistemaLiquidacion",
    "Tramo",
    "Traza",
    "build",
    "comparar_remesas",
    "comparar_rutas",
    "construir_pacs008",
    "cuadra",
    "descomponer_ahorro",
    "elegir",
    "enrutar",
    "evaluar",
    "exposicion_maxima",
    "exposicion_por_contraparte",
    "liquidar_pvp",
    "medir",
    "netting_multilateral",
    "pacs002",
    "porcentaje_atribuible_al_registro",
    "prueba_retrospectiva",
    "ratio_netting",
    "subastar",
    "transitar",
    "validar",
]
