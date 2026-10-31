"""Costo total de un incidente, componente por componente.

Formula:

    C_total = D + C_rep + C_for + C_op + C_comp
    C_neto  = C_total - min(cobertura_seguro, perdida_asegurable)

    D       perdida definitiva (S - F * p), ver `incident`
    C_rep   costo de reponer reservas (compra con impacto, financiamiento)
    C_for   forense, legal, auditoria externa y notificacion (monto fijo)
    C_op    costo de oportunidad de la pausa = ingreso_diario * dias_de_pausa
    C_comp  compensaciones a clientes = tasa_comp * P_afectado

Supuestos: los componentes son aditivos y no hay efecto fiscal.
Limitacion: no incluye perdida de clientes futura ni dano reputacional, que son
reales pero no estimables con los datos de este ejercicio.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Costos:
    perdida_definitiva: float
    reposicion: float
    forense_legal: float
    oportunidad: float
    compensaciones: float
    recuperacion_seguro: float = 0.0

    @property
    def bruto(self) -> float:
        return (
            self.perdida_definitiva
            + self.reposicion
            + self.forense_legal
            + self.oportunidad
            + self.compensaciones
        )

    @property
    def neto(self) -> float:
        return self.bruto - self.recuperacion_seguro


def costo_de_oportunidad(ingreso_diario: float, dias_pausa: int) -> float:
    if ingreso_diario < 0 or dias_pausa < 0:
        raise ValueError("parametros invalidos")
    return ingreso_diario * dias_pausa


def compensaciones(tasa: float, pasivo_afectado: float) -> float:
    if not 0.0 <= tasa <= 1.0 or pasivo_afectado < 0:
        raise ValueError("parametros invalidos")
    return tasa * pasivo_afectado


def recuperacion_de_seguro(cobertura: float, perdida_asegurable: float) -> float:
    if cobertura < 0 or perdida_asegurable < 0:
        raise ValueError("parametros invalidos")
    return min(cobertura, perdida_asegurable)
