"""Firma multiple m-de-n y analisis de correlacion entre guardianes.

El modulo hace cumplir el hallazgo de la clase 3: contar claves no es contar
independencias. Siete guardianes sobre un solo proveedor de modulos son, para
el fallo que importa, una sola clave.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field

from .crypto import Par, firmar, verificar


@dataclass(frozen=True)
class Guardian:
    identificador: str
    par: Par
    ubicacion: str
    proveedor: str
    jurisdiccion: str


@dataclass
class EsquemaMultifirma:
    umbral: int
    guardianes: list[Guardian] = field(default_factory=list)

    @property
    def n(self) -> int:
        return len(self.guardianes)

    def firmar(self, quienes: list[str], mensaje: bytes) -> dict[str, bytes]:
        elegidos = [g for g in self.guardianes if g.identificador in quienes]
        return {g.identificador: firmar(g.par, mensaje) for g in elegidos}

    def autoriza(self, firmas: dict[str, bytes], mensaje: bytes) -> bool:
        validas = 0
        for guardian in self.guardianes:
            firma = firmas.get(guardian.identificador)
            if firma is not None and verificar(guardian.par, mensaje, firma):
                validas += 1
        return validas >= self.umbral


def analizar_correlacion(esquema: EsquemaMultifirma) -> dict[str, object]:
    """Cuantos guardianes caen a la vez por cada causa comun.

    El esquema solo tolera una causa comun si, tras perder ese grupo, quedan
    al menos `umbral` guardianes.
    """
    def mayor(atributo: str) -> tuple[str, int]:
        cuenta = Counter(getattr(g, atributo) for g in esquema.guardianes)
        if not cuenta:
            return ("", 0)
        return cuenta.most_common(1)[0]

    resultado: dict[str, object] = {
        "n": esquema.n,
        "umbral": esquema.umbral,
        "perdidas_independientes_toleradas": esquema.n - esquema.umbral,
    }
    for atributo in ("proveedor", "ubicacion", "jurisdiccion"):
        valor, cuantos = mayor(atributo)
        quedan = esquema.n - cuantos
        resultado[atributo] = {
            "mayor_grupo": valor,
            "cuantos": cuantos,
            "quedan_si_falla": quedan,
            "sobrevive": quedan >= esquema.umbral,
        }
    resultado["sobrevive_a_cualquier_causa_comun"] = all(
        resultado[a]["sobrevive"]  # type: ignore[index]
        for a in ("proveedor", "ubicacion", "jurisdiccion")
    )
    return resultado
