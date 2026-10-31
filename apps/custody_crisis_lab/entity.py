"""Entidad custodio: activos, obligaciones y ratios de respaldo.

Formulas (unidades: MUSD; ratios sin unidad):

    A_liq   activos liquidos disponibles a 24 h
    A_nl    activos no liquidos o no disponibles a 24 h
    P       pasivos con clientes (obligacion de restituir)

    respaldo bruto        R_b = (A_liq + A_nl) / P
    respaldo disponible   R_d = A_liq / P
    brecha                B   = P - (A_liq + A_nl)      (>0 hay faltante)

Supuestos: P esta medido a la misma hora de corte que los activos y en una
unidad comun; los activos se valoran a precio de mercado sin descuento.
Limitacion: un ratio de 100 % no prueba propiedad ni segregacion; solo dice que
la cifra de activos alcanza la cifra de obligaciones.
"""

from __future__ import annotations

from dataclasses import dataclass, replace


@dataclass(frozen=True)
class Custodio:
    """Balance simplificado de una entidad que custodia activos de clientes."""

    activos_liquidos: float
    activos_no_liquidos: float
    pasivos_clientes: float
    fondo_proteccion: float = 0.0

    def __post_init__(self) -> None:
        for nombre in (
            "activos_liquidos",
            "activos_no_liquidos",
            "pasivos_clientes",
            "fondo_proteccion",
        ):
            if getattr(self, nombre) < 0:
                raise ValueError(f"{nombre} no puede ser negativo")
        if self.pasivos_clientes == 0:
            raise ValueError("pasivos_clientes debe ser positivo")

    @property
    def activos_totales(self) -> float:
        return self.activos_liquidos + self.activos_no_liquidos

    @property
    def respaldo_bruto(self) -> float:
        return self.activos_totales / self.pasivos_clientes

    @property
    def respaldo_disponible(self) -> float:
        return self.activos_liquidos / self.pasivos_clientes

    @property
    def brecha(self) -> float:
        """Faltante (positivo) o exceso (negativo) de activos frente a pasivos."""
        return self.pasivos_clientes - self.activos_totales

    def con_activos(self, liquidos: float, no_liquidos: float) -> "Custodio":
        return replace(
            self, activos_liquidos=liquidos, activos_no_liquidos=no_liquidos
        )


def caso_sintetico() -> Custodio:
    """Entidad de ejercicio: 100 % respaldada, 80 % liquida."""
    return Custodio(
        activos_liquidos=80_000.0,
        activos_no_liquidos=20_000.0,
        pasivos_clientes=100_000.0,
        fondo_proteccion=800.0,
    )
