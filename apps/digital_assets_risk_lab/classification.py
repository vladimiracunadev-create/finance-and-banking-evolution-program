"""Clasificacion de activos digitales por la promesa, no por la tecnologia.

La clase 1 sostiene que dos instrumentos identicos tecnicamente pueden tener
regimenes opuestos, y que la ficha de cinco preguntas hace todo el trabajo.
Este modulo la implementa y anade el rastreo del respaldo, que es lo que
detecta la circularidad de la clase 7.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Obligado(str, Enum):
    """Quien responde con su patrimonio."""

    NADIE = "nadie"
    EMISOR = "emisor"
    EMISOR_AUTORIZADO = "emisor_autorizado"
    BANCO = "banco"
    BANCO_CENTRAL = "banco_central"


class Exigibilidad(str, Enum):
    """Cuando puede reclamarse la promesa."""

    NUNCA = "nunca"
    SOLO_CANJE = "solo_canje"
    CON_UMBRAL = "con_umbral"
    A_LA_VISTA = "a_la_vista"


class Tipo(str, Enum):
    NO_RESPALDADO = "no_respaldado"
    REFERENCIADO = "referenciado"
    DINERO_ELECTRONICO = "dinero_electronico"
    DEPOSITO_TOKENIZADO = "deposito_tokenizado"
    CBDC = "cbdc"
    INDETERMINADO = "indeterminado"


@dataclass(frozen=True)
class Ficha:
    """Las cinco preguntas de la clase 1.

    Ninguna es tecnica: la red, el estandar y la billetera no aparecen.
    """

    nombre: str
    quien_promete: Obligado
    que_promete: str
    respaldo: str
    exigible: Exigibilidad
    ante_quien: str
    umbral_redencion: int = 0
    remunera: bool = False

    @property
    def hay_credito(self) -> bool:
        """Si no hay obligado ni foro, no hay credito: hay un objeto."""
        return self.quien_promete is not Obligado.NADIE and self.ante_quien != "nadie"

    @property
    def derecho_universal(self) -> bool:
        """La paridad solo es un DERECHO si cualquiera puede ejercerla."""
        return self.exigible is Exigibilidad.A_LA_VISTA and self.umbral_redencion == 0

    def apta_para_tesoreria(self, saldo: int) -> tuple[bool, str]:
        """Criterio de la clase 1: disponer del nominal cuando haga falta."""
        if not self.hay_credito:
            return False, "sin obligado: el precio depende de que otro compre"
        if self.exigible in (Exigibilidad.NUNCA, Exigibilidad.SOLO_CANJE):
            return False, "no hay derecho de redencion contra el emisor"
        if saldo < self.umbral_redencion:
            return False, (
                f"el saldo {saldo} no alcanza el minimo de redencion "
                f"{self.umbral_redencion}: la salida seria vender en mercado"
            )
        return True, "derecho de redencion ejercitable con este saldo"


def clasificar(ficha: Ficha) -> Tipo:
    """Clasifica por la promesa. Deliberadamente no mira la red ni el token."""
    if ficha.quien_promete is Obligado.BANCO_CENTRAL:
        return Tipo.CBDC
    if ficha.quien_promete is Obligado.BANCO:
        return Tipo.DEPOSITO_TOKENIZADO
    if ficha.quien_promete is Obligado.EMISOR_AUTORIZADO:
        return Tipo.DINERO_ELECTRONICO
    if ficha.quien_promete is Obligado.NADIE:
        return Tipo.NO_RESPALDADO
    if ficha.quien_promete is Obligado.EMISOR:
        return Tipo.REFERENCIADO
    return Tipo.INDETERMINADO


# Los tres elementos del dinero electronico (clase 9). La calificacion sigue a
# la sustancia: un producto que cumple los tres lo es, se llame como se llame.
@dataclass(frozen=True)
class TresElementos:
    valor_almacenado: bool
    emitido_contra_fondos: bool
    aceptado_por_terceros: bool

    @property
    def es_dinero_electronico(self) -> bool:
        return (
            self.valor_almacenado
            and self.emitido_contra_fondos
            and self.aceptado_por_terceros
        )


def incumplimientos_dinero_electronico(ficha: Ficha) -> list[str]:
    """Que le falta a un producto para encajar en el regimen de la clase 9."""
    fallos: list[str] = []
    if ficha.remunera:
        fallos.append("remunera el saldo, y el regimen lo prohibe")
    if ficha.umbral_redencion > 0:
        fallos.append(
            "la redencion tiene minimo, incompatible con la redencion a la par"
        )
    if ficha.exigible is not Exigibilidad.A_LA_VISTA:
        fallos.append("la redencion no es a la vista")
    return fallos


@dataclass
class Respaldo:
    """Un eslabon de la cadena de respaldo."""

    nombre: str
    externo: bool
    respalda_a: str | None = None


@dataclass
class CadenaDeRespaldo:
    """Rastrea el respaldo hasta un activo fuera del sistema.

    La clase 1 exige llegar a un activo externo; la clase 7 muestra que si el
    rastreo vuelve sobre sus pasos, el respaldo no absorbe: amplifica.
    """

    eslabones: dict[str, Respaldo] = field(default_factory=dict)

    def agregar(self, nombre: str, externo: bool, respalda_a: str | None = None) -> None:
        self.eslabones[nombre] = Respaldo(nombre, externo, respalda_a)

    def rastrear(self, inicio: str) -> list[str]:
        """Devuelve el camino recorrido. Se detiene al repetir un eslabon."""
        camino: list[str] = []
        actual: str | None = inicio
        while actual is not None and actual in self.eslabones:
            if actual in camino:
                camino.append(actual)  # se marca el cierre del ciclo
                break
            camino.append(actual)
            actual = self.eslabones[actual].respalda_a
        return camino

    def es_circular(self, inicio: str) -> bool:
        camino = self.rastrear(inicio)
        return len(camino) != len(set(camino))

    def llega_a_activo_externo(self, inicio: str) -> bool:
        if self.es_circular(inicio):
            return False
        camino = self.rastrear(inicio)
        return any(self.eslabones[n].externo for n in camino)
