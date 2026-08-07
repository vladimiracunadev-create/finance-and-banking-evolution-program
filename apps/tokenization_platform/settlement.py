"""Entrega contra pago atomica y sus modos de fallo.

La clase 8 define la atomicidad como la AUSENCIA de un estado observable en que
uno de los tramos se haya movido y el otro no. Este modulo la implementa de forma
que esa ausencia se pueda comprobar desde fuera: `observar()` devuelve el estado
del sistema y las pruebas verifican que nunca aparece un estado a medias.

El diseno rechaza ANTES de bloquear: una reversion implica que hubo un estado
intermedio, y en ese estado alguien pudo actuar.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Modelo(str, Enum):
    BRUTO_SIMULTANEO = "bruto_simultaneo"
    VALOR_BRUTO_DINERO_NETO = "valor_bruto_dinero_neto"
    AMBOS_NETOS = "ambos_netos"


class Motivo(str, Enum):
    ACEPTADA = "aceptada"
    SIN_VALOR = "sin_valor"
    SIN_DINERO = "sin_dinero"
    TRAMO_DE_DINERO_FUERA = "tramo_de_dinero_fuera"
    REGISTRO_DETENIDO = "registro_detenido"


class NoHayAtomicidad(RuntimeError):
    """El tramo de dinero esta fuera del registro: no puede haber atomicidad."""


@dataclass(frozen=True)
class Operacion:
    identificador: str
    vendedor: str
    comprador: str
    unidades: int
    importe: int


@dataclass(frozen=True)
class ResultadoLiquidacion:
    operacion: str
    ejecutada: bool
    motivo: Motivo


@dataclass
class Liquidador:
    """Liquida valor contra dinero en un solo acto.

    `dinero_en_el_registro` es la condicion de la clase 8: si es falso, el
    liquidador se niega a prometer atomicidad en vez de simularla.
    """

    valores: dict[str, int] = field(default_factory=dict)
    dinero: dict[str, int] = field(default_factory=dict)
    dinero_en_el_registro: bool = True
    detenido: bool = False
    ejecutadas: list[str] = field(default_factory=list)
    rechazadas: list[ResultadoLiquidacion] = field(default_factory=list)

    def acreditar_valor(self, titular: str, unidades: int) -> None:
        self.valores[titular] = self.valores.get(titular, 0) + unidades

    def acreditar_dinero(self, titular: str, importe: int) -> None:
        self.dinero[titular] = self.dinero.get(titular, 0) + importe

    def observar(self) -> dict[str, dict[str, int]]:
        """Estado completo del sistema, para comprobar que no hay estados a medias."""
        return {"valores": dict(self.valores), "dinero": dict(self.dinero)}

    @property
    def permite_atomicidad(self) -> bool:
        return self.dinero_en_el_registro

    def liquidar(self, operacion: Operacion) -> ResultadoLiquidacion:
        """Ejecuta la operacion o la rechaza sin haber tocado nada."""
        if not self.dinero_en_el_registro:
            resultado = ResultadoLiquidacion(
                operacion.identificador, False, Motivo.TRAMO_DE_DINERO_FUERA
            )
            self.rechazadas.append(resultado)
            raise NoHayAtomicidad(
                "el tramo de dinero esta fuera del registro: "
                "esta liquidacion no puede ser atomica"
            )

        if self.detenido:
            resultado = ResultadoLiquidacion(
                operacion.identificador, False, Motivo.REGISTRO_DETENIDO
            )
            self.rechazadas.append(resultado)
            return resultado

        # Verificacion ANTES de bloquear nada. Rechazar no deja rastro;
        # bloquear y revertir, si.
        if self.valores.get(operacion.vendedor, 0) < operacion.unidades:
            resultado = ResultadoLiquidacion(
                operacion.identificador, False, Motivo.SIN_VALOR
            )
            self.rechazadas.append(resultado)
            return resultado
        if self.dinero.get(operacion.comprador, 0) < operacion.importe:
            resultado = ResultadoLiquidacion(
                operacion.identificador, False, Motivo.SIN_DINERO
            )
            self.rechazadas.append(resultado)
            return resultado

        # Un solo acto: los cuatro movimientos se aplican juntos.
        self.valores[operacion.vendedor] -= operacion.unidades
        self.valores[operacion.comprador] = (
            self.valores.get(operacion.comprador, 0) + operacion.unidades
        )
        self.dinero[operacion.comprador] -= operacion.importe
        self.dinero[operacion.vendedor] = (
            self.dinero.get(operacion.vendedor, 0) + operacion.importe
        )

        self.ejecutadas.append(operacion.identificador)
        return ResultadoLiquidacion(operacion.identificador, True, Motivo.ACEPTADA)


def netear(operaciones: list[Operacion]) -> dict[str, dict[str, int]]:
    """Compensa un ciclo de operaciones en saldos por participante.

    El conjunto compensado debe liquidarse como una sola unidad: o todo el neteo
    o nada. Si falla, fallan TODAS las operaciones del ciclo, y ese escenario hay
    que dimensionarlo (clase 8).
    """
    valores: dict[str, int] = {}
    dinero: dict[str, int] = {}
    for op in operaciones:
        valores[op.vendedor] = valores.get(op.vendedor, 0) - op.unidades
        valores[op.comprador] = valores.get(op.comprador, 0) + op.unidades
        dinero[op.vendedor] = dinero.get(op.vendedor, 0) + op.importe
        dinero[op.comprador] = dinero.get(op.comprador, 0) - op.importe
    return {"valores": valores, "dinero": dinero}


def ahorro_de_la_atomicidad(
    volumen_diario: int,
    dias_de_ciclo: int,
    probabilidad_incumplimiento: float,
    recuperacion: float,
    dias_habiles: int = 250,
) -> float:
    """Perdida esperada por riesgo de principal que la atomicidad elimina."""
    exposicion = volumen_diario * dias_de_ciclo
    return exposicion * probabilidad_incumplimiento * (1 - recuperacion) * dias_habiles


def coste_de_liquidez(
    volumen_diario: int,
    fraccion_saldo: float,
    coste_financiacion_anual: float,
) -> float:
    """Coste del saldo prefinanciado que exige liquidar en T+0."""
    return volumen_diario * fraccion_saldo * coste_financiacion_anual


# Los cinco riesgos de la clase 8. La atomicidad elimina exactamente uno, y
# presentarla como si los cubriera todos es el error de la clase.
RIESGOS = {
    "principal": "lo elimina la atomicidad",
    "reemplazo": "subsiste: hay que rehacer la operacion a otro precio",
    "liquidez": "subsiste: el saldo estaba comprometido",
    "operativo": "subsiste: el registro puede detenerse",
    "juridico": "subsiste: la finalidad legal puede no coincidir",
}
