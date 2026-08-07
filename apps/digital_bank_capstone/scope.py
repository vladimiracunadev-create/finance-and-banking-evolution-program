"""Alcance del capstone: las cuatro preguntas por funcion.

La clase 1 sostiene que reducir el alcance de once funciones a cuatro NO baja el
ingreso, porque las excluidas no lo generaban. Este modulo lo hace comprobable.
"""

from __future__ import annotations

from dataclasses import dataclass, field


class FuncionSinSegmento(ValueError):
    """Una funcion que no tiene quien la necesite no entra en el alcance."""


@dataclass(frozen=True)
class Funcion:
    """Una funcion candidata, con las cuatro preguntas de la clase 1."""

    nombre: str
    quien_la_necesita: int          # clientes del segmento que la piden
    ingreso_anual: int              # lo que paga ese segmento por ella
    coste_anual: int                # lo que cuesta servirla
    regimen_que_obliga: str | None  # el que activa, si activa alguno

    @property
    def aporta(self) -> bool:
        """Las dos primeras preguntas deciden si la funcion entra."""
        return self.quien_la_necesita > 0 and self.ingreso_anual > 0

    @property
    def margen(self) -> int:
        return self.ingreso_anual - self.coste_anual


@dataclass
class Alcance:
    """Catalogo de funciones con sus exclusiones razonadas."""

    funciones: list[Funcion] = field(default_factory=list)
    exclusiones: dict[str, str] = field(default_factory=dict)

    def proponer(self, funcion: Funcion) -> None:
        self.funciones.append(funcion)

    def excluir(self, nombre: str, razon: str) -> None:
        """Una exclusion sin razon escrita no es una exclusion."""
        if not razon:
            raise ValueError("una exclusion sin razon no es una exclusion")
        self.exclusiones[nombre] = razon

    @property
    def incluidas(self) -> list[Funcion]:
        return [f for f in self.funciones if f.nombre not in self.exclusiones]

    @property
    def ingreso(self) -> int:
        return sum(f.ingreso_anual for f in self.incluidas)

    @property
    def coste(self) -> int:
        return sum(f.coste_anual for f in self.incluidas)

    @property
    def regimenes(self) -> set[str]:
        return {f.regimen_que_obliga for f in self.incluidas if f.regimen_que_obliga}

    def sin_segmento(self) -> list[Funcion]:
        """Funciones que nadie necesita: las que hay que excluir."""
        return [f for f in self.funciones if not f.aporta]

    def excluir_las_que_no_aportan(self) -> int:
        """Excluye automaticamente las que fallan las dos primeras preguntas."""
        cuantas = 0
        for funcion in self.sin_segmento():
            if funcion.nombre not in self.exclusiones:
                self.excluir(
                    funcion.nombre,
                    "ningun cliente del segmento la necesita y no genera ingreso",
                )
                cuantas += 1
        return cuantas


def carga_regulatoria(
    regimenes: int,
    cumplimiento_por_regimen: int,
    autorizacion: int,
    anios_amortizacion: int,
    capital: int,
    coste_del_capital: float,
) -> int:
    """Coste anual de estar autorizado y supervisado (clase 1)."""
    if anios_amortizacion <= 0:
        raise ValueError("los anios de amortizacion deben ser positivos")
    return round(
        regimenes * cumplimiento_por_regimen
        + autorizacion / anios_amortizacion
        + capital * coste_del_capital
    )


def facturacion_necesaria(carga_anual: int, margen: float) -> float:
    """Lo que hay que facturar solo para cubrir la carga regulatoria.

    Es la cifra que decide si el proyecto existe, y casi nunca esta en el plan
    de negocio inicial.
    """
    if not 0 < margen <= 1:
        raise ValueError("el margen debe estar entre 0 y 1")
    return carga_anual / margen


def saldo_minimo(coste_unitario: int, margen_sobre_saldo: float) -> float:
    """Saldo por debajo del cual el cliente no cubre su coste de servicio."""
    if margen_sobre_saldo <= 0:
        raise ValueError("el margen debe ser positivo")
    return coste_unitario / margen_sobre_saldo
