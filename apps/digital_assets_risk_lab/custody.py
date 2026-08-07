"""Custodia por umbral: independencia efectiva y controles de retirada.

La clase 12 sostiene que «3 de 5» no dice nada por si solo: lo que importa es
que eventos dejan inoperativos a cuantos guardianes a la vez. Es la misma
independencia efectiva de la Parte 19, clase 5, aplicada a la custodia.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from math import comb


@dataclass(frozen=True)
class Guardian:
    nombre: str
    ubicacion: str
    dispositivo: str
    jurisdiccion: str
    proveedor: str = "propio"


@dataclass
class Esquema:
    """Esquema m-de-n con sus guardianes."""

    umbral: int
    guardianes: list[Guardian] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.umbral < 1:
            raise ValueError("el umbral debe ser al menos 1")

    @property
    def n(self) -> int:
        return len(self.guardianes)

    def grupos_correlacionados(self) -> dict[str, int]:
        """Mayor grupo de guardianes que comparte cada factor.

        Cinco guardianes con el mismo proveedor son, a efectos de un fallo del
        proveedor, uno solo.
        """
        factores = ("ubicacion", "dispositivo", "jurisdiccion", "proveedor")
        resultado: dict[str, int] = {}
        for factor in factores:
            cuenta: dict[str, int] = {}
            for guardian in self.guardianes:
                valor = getattr(guardian, factor)
                cuenta[valor] = cuenta.get(valor, 0) + 1
            resultado[factor] = max(cuenta.values()) if cuenta else 0
        return resultado

    def independencia_efectiva(self) -> int:
        """Cuantos guardianes realmente independientes hay.

        Se toma el peor factor: si un solo evento tumba a k, el esquema se
        comporta como si tuviera n - k + 1 participantes independientes.
        """
        if not self.guardianes:
            return 0
        peor = max(self.grupos_correlacionados().values())
        return self.n - peor + 1

    def tolera_evento_correlacionado(self) -> bool:
        """Cierto si ningun evento unico alcanza el umbral por si solo."""
        if not self.guardianes:
            return False
        return max(self.grupos_correlacionados().values()) < self.umbral

    def probabilidad_de_bloqueo(self, p_indisponible: float) -> float:
        """Probabilidad de no reunir el umbral, suponiendo independencia.

        El supuesto de independencia solo es defendible DESPUES de corregir la
        distribucion: por eso la funcion se usa junto a la anterior, no en su
        lugar.
        """
        if not 0.0 <= p_indisponible <= 1.0:
            raise ValueError("la probabilidad debe estar entre 0 y 1")
        faltan = self.n - self.umbral + 1
        total = 0.0
        for k in range(faltan, self.n + 1):
            total += (
                comb(self.n, k)
                * p_indisponible**k
                * (1 - p_indisponible) ** (self.n - k)
            )
        return total


@dataclass
class Recuperacion:
    """Procedimiento de recuperacion sin puerta trasera.

    Tres propiedades lo distinguen de un segundo camino de ataque: umbral mas
    alto que el de firma, retardo obligatorio y capacidad de cancelacion de
    cualquier tenedor.
    """

    umbral: int
    tenedores: int
    retardo_dias: int
    umbral_de_firma: int

    @property
    def es_mas_dificil_que_firmar(self) -> bool:
        return self.umbral > self.umbral_de_firma

    @property
    def defectos(self) -> list[str]:
        fallos: list[str] = []
        if not self.es_mas_dificil_que_firmar:
            fallos.append(
                "el umbral de recuperacion no supera al de firma: es un "
                "segundo camino igual de facil"
            )
        if self.retardo_dias < 1:
            fallos.append("sin retardo no hay ventana para cancelar")
        if self.umbral > self.tenedores:
            fallos.append("el umbral supera el numero de tenedores: irrecuperable")
        return fallos


# Los siete controles de una retirada, en orden. El tercero es el que detiene
# el ataque mas comun: comprometer una sesion y retirar a una direccion nueva.
CONTROLES = (
    "origen_autorizado",
    "destino_en_lista_blanca",
    "alta_de_destino_con_espera",
    "limite_por_importe",
    "segunda_aprobacion_fuera_de_banda",
    "verificacion_de_direccion_completa",
    "registro_inmutable",
)


@dataclass(frozen=True)
class Retirada:
    origen_autorizado: bool
    destino_en_lista_blanca: bool
    importe: int
    segunda_aprobacion: bool


@dataclass
class PoliticaDeRetirada:
    espera_alta_horas: int = 48
    limite_sin_segunda_aprobacion: int = 1_000_000
    lista_blanca: set[str] = field(default_factory=set)

    def evaluar(self, retirada: Retirada, destino: str) -> tuple[bool, str, int]:
        """Devuelve (permitida, motivo, horas de deteccion ganadas)."""
        if not retirada.origen_autorizado:
            return False, "origen no autorizado", 0
        if destino not in self.lista_blanca:
            return (
                False,
                "destino fuera de lista blanca: el alta exige espera",
                self.espera_alta_horas,
            )
        if (
            retirada.importe > self.limite_sin_segunda_aprobacion
            and not retirada.segunda_aprobacion
        ):
            return False, "importe sobre el limite sin segunda aprobacion", 0
        return True, "retirada conforme", 0
