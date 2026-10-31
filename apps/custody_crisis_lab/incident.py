"""Clasificacion de fondos tras un incidente y efecto sobre el respaldo.

Cuatro conceptos que las noticias mezclan:

    S   sustraido o transferido sin autorizacion  (hecho, estimado)
    F   congelado: parte de S inmovilizada por terceros (F <= S)
    p   probabilidad de restitucion de F           (supuesto, 0 <= p <= 1)

    restituible esperado   E[rec] = F * p
    perdida definitiva     D      = S - F * p
    sin congelar           U      = S - F

Un congelamiento NO es una recuperacion: hasta la restitucion, el activo no esta
en el balance de la entidad. Por eso el respaldo cae en S el primer dia y solo
sube a medida que F se restituye.

Limitacion: p es un supuesto unico; en la practica cada emisor, red y monto
tiene su propia probabilidad y su propio plazo.
"""

from __future__ import annotations

from dataclasses import dataclass

from .entity import Custodio


@dataclass(frozen=True)
class Fondos:
    sustraido: float
    congelado: float
    restituible: float  # F * p
    sin_congelar: float
    perdida_definitiva: float


def clasificar_fondos(
    sustraido: float, congelado: float, p_restitucion: float
) -> Fondos:
    if sustraido < 0 or congelado < 0:
        raise ValueError("los importes no pueden ser negativos")
    if congelado > sustraido:
        raise ValueError("no se puede congelar mas de lo sustraido")
    if not 0.0 <= p_restitucion <= 1.0:
        raise ValueError("p_restitucion debe estar entre 0 y 1")
    restituible = congelado * p_restitucion
    return Fondos(
        sustraido=sustraido,
        congelado=congelado,
        restituible=restituible,
        sin_congelar=sustraido - congelado,
        perdida_definitiva=sustraido - restituible,
    )


def aplicar_perdida(
    entidad: Custodio, sustraido: float, parte_liquida: float = 1.0
) -> Custodio:
    """Resta `sustraido` de los activos; `parte_liquida` es la fraccion hot/liquida.

    Si la perdida supera el activo de un tramo, el exceso se imputa al otro; si
    supera el total de activos, se lanza ValueError (el modelo deja de aplicar).
    """
    if sustraido < 0:
        raise ValueError("sustraido no puede ser negativo")
    if not 0.0 <= parte_liquida <= 1.0:
        raise ValueError("parte_liquida debe estar entre 0 y 1")
    if sustraido > entidad.activos_totales:
        raise ValueError("la perdida supera los activos totales")
    de_liquidos = sustraido * parte_liquida
    de_no_liquidos = sustraido - de_liquidos
    if de_liquidos > entidad.activos_liquidos:
        de_no_liquidos += de_liquidos - entidad.activos_liquidos
        de_liquidos = entidad.activos_liquidos
    if de_no_liquidos > entidad.activos_no_liquidos:
        de_liquidos += de_no_liquidos - entidad.activos_no_liquidos
        de_no_liquidos = entidad.activos_no_liquidos
    return entidad.con_activos(
        entidad.activos_liquidos - de_liquidos,
        entidad.activos_no_liquidos - de_no_liquidos,
    )


def aplicar_restitucion(entidad: Custodio, restituido: float) -> Custodio:
    """Devuelve a la entidad fondos congelados que fueron restituidos (liquidos)."""
    if restituido < 0:
        raise ValueError("restituido no puede ser negativo")
    return entidad.con_activos(
        entidad.activos_liquidos + restituido, entidad.activos_no_liquidos
    )
