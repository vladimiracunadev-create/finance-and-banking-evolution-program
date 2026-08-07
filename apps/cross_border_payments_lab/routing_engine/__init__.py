"""Motor de rutas con criterios explicitos.

Los tres primeros criterios son FILTROS y los tres ultimos son FACTORES. La
distincion es la razon de ser del modulo: si el cumplimiento se pondera, una
ruta muy barata que no soporta un control exigido puede ganar la comparacion, y
el motor acaba eligiendo una operacion no autorizada.

Toda decision devuelve su `motivo`. Un motor que elige sin explicar no se puede
auditar ni corregir cuando se equivoca.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Pesos:
    tiempo: float = 0.35
    coste: float = 0.50
    riesgo: float = 0.15

    def __post_init__(self) -> None:
        total = self.tiempo + self.coste + self.riesgo
        if abs(total - 1.0) > 1e-9:
            raise ValueError(f"los pesos deben sumar 1,0; suman {total}")


@dataclass(frozen=True)
class Pago:
    corredor: str
    importe: float
    moneda_origen: str
    moneda_destino: str
    canal_beneficiario: str
    controles: frozenset[str] = frozenset()


@dataclass(frozen=True)
class Ruta:
    nombre: str
    tipo: str
    corredor: str
    importe_maximo: float
    monedas: frozenset[str]
    canales: frozenset[str]
    controles_soportados: frozenset[str]
    coste_fijo: float
    coste_variable: float
    diferencial_pb: float
    plazo_p50_h: float
    plazo_p95_h: float
    riesgo: float
    disponibilidad: float

    def admite(self, pago: Pago) -> bool:
        return (
            self.corredor == pago.corredor
            and pago.importe <= self.importe_maximo
            and pago.moneda_origen in self.monedas
            and pago.moneda_destino in self.monedas
            and pago.canal_beneficiario in self.canales
        )

    def soporta(self, controles: frozenset[str]) -> bool:
        return controles <= self.controles_soportados

    def coste_total(self, pago: Pago) -> float:
        variable = pago.importe * (self.coste_variable + self.diferencial_pb / 10_000)
        return round(self.coste_fijo + variable, 2)

    def coste_relativo(self, pago: Pago) -> float:
        return self.coste_total(pago) / pago.importe if pago.importe else 0.0


@dataclass
class Decision:
    ruta: Ruta | None
    alternativa: Ruta | None
    motivo: str
    descartadas: dict[str, str] = field(default_factory=dict)


def _normalizar(valores: list[float]) -> list[float]:
    menor, mayor = min(valores), max(valores)
    if mayor - menor < 1e-12:
        return [0.0 for _ in valores]
    return [(v - menor) / (mayor - menor) for v in valores]


def elegir(pago: Pago, rutas: list[Ruta], pesos: Pesos | None = None) -> Decision:
    pesos = pesos or Pesos()
    descartadas: dict[str, str] = {}

    # ---- Filtro 1: elegibilidad -------------------------------------------
    elegibles = []
    for ruta in rutas:
        if ruta.admite(pago):
            elegibles.append(ruta)
        else:
            descartadas[ruta.nombre] = "no elegible"
    if not elegibles:
        return Decision(None, None, "ninguna ruta admite este pago", descartadas)

    # ---- Filtro 2: cumplimiento -------------------------------------------
    # No se pondera: una ruta que no soporta un control exigido queda fuera,
    # por barata que sea.
    conformes = []
    for ruta in elegibles:
        if ruta.soporta(pago.controles):
            conformes.append(ruta)
        else:
            faltan = sorted(pago.controles - ruta.controles_soportados)
            descartadas[ruta.nombre] = f"no soporta {faltan}"
    if not conformes:
        return Decision(
            None, None, f"ninguna ruta soporta {sorted(pago.controles)}", descartadas
        )

    # ---- Filtro 3: disponibilidad -----------------------------------------
    disponibles = []
    for ruta in conformes:
        if ruta.disponibilidad >= 0.90:
            disponibles.append(ruta)
        else:
            descartadas[ruta.nombre] = f"disponibilidad {ruta.disponibilidad:.0%}"
    if not disponibles:
        return Decision(None, None, "todas las rutas no disponibles", descartadas)

    # ---- Regla de la clase 14: el enlace directo gana antes de ponderar ----
    enlaces = [r for r in disponibles if r.tipo == "enlace_pagos_inmediatos"]
    if enlaces:
        elegida = min(enlaces, key=lambda r: r.coste_total(pago))
        resto = [r for r in disponibles if r is not elegida]
        return Decision(
            elegida,
            min(resto, key=lambda r: r.coste_total(pago)) if resto else None,
            "enlace de pagos inmediatos disponible: mas barato y sin riesgo de emisor",
            descartadas,
        )

    # ---- Factores: tiempo, coste y riesgo ---------------------------------
    tiempos = _normalizar([r.plazo_p95_h for r in disponibles])
    costes = _normalizar([r.coste_relativo(pago) for r in disponibles])
    riesgos = _normalizar([r.riesgo for r in disponibles])

    puntuadas = sorted(
        (
            (
                pesos.tiempo * t + pesos.coste * c + pesos.riesgo * g,
                ruta,
            )
            for ruta, t, c, g in zip(disponibles, tiempos, costes, riesgos)
        ),
        key=lambda par: (par[0], par[1].nombre),
    )
    elegida = puntuadas[0][1]
    alternativa = puntuadas[1][1] if len(puntuadas) > 1 else None

    motivo = (
        f"coste {elegida.coste_relativo(pago):.2%} y plazo p95 {elegida.plazo_p95_h} h "
        f"con pesos tiempo={pesos.tiempo} coste={pesos.coste} riesgo={pesos.riesgo}"
    )
    if alternativa is not None:
        motivo += (
            f"; alternativa {alternativa.nombre} a "
            f"{alternativa.coste_relativo(pago):.2%} y {alternativa.plazo_p95_h} h"
        )
    return Decision(elegida, alternativa, motivo, descartadas)
