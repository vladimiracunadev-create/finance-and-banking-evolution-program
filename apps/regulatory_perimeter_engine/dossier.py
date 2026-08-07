"""Expediente regulatorio: doce piezas y su lectura cruzada.

La clase 18 sostiene que las contradicciones no aparecen dentro de una pieza sino
al cruzarlas por parejas, que es como lee un supervisor. Este modulo implementa
esa lectura y ordena los hallazgos por efecto sobre el cliente, no por gravedad
formal.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import IntEnum


class Nivel(IntEnum):
    """Orden por efecto sobre el cliente (clase 18)."""

    BLOQUEANTE = 1
    RELEVANTE = 2
    ORDINARIO = 3


PIEZAS = (
    "perimetro",
    "calificacion",
    "autorizacion",
    "regimen_por_jurisdiccion",
    "salvaguarda",
    "informacion_y_conducta",
    "prevencion_de_lavado",
    "datos_personales",
    "vigilancia_de_mercado",
    "resiliencia",
    "prudencial",
    "hallazgos_y_remediacion",
)


class AfirmacionSinEvidencia(ValueError):
    """Una afirmacion sin evidencia se retira; no se acepta con reservas."""


@dataclass(frozen=True)
class Afirmacion:
    pieza: str
    texto: str
    evidencia: str

    def __post_init__(self) -> None:
        if self.pieza not in PIEZAS:
            raise ValueError(f"pieza desconocida: {self.pieza}")
        if not self.evidencia:
            raise AfirmacionSinEvidencia(self.texto)


@dataclass(frozen=True)
class Hallazgo:
    nivel: Nivel
    piezas: tuple[str, str]
    descripcion: str
    clientes_afectados: int

    @property
    def es_bloqueante(self) -> bool:
        return self.nivel is Nivel.BLOQUEANTE


@dataclass(frozen=True)
class Remediacion:
    hallazgo: str
    correccion: str
    responsable: str
    plazo_dias: int
    verificacion: str
    medida_provisional: str

    def __post_init__(self) -> None:
        if not self.medida_provisional:
            # Entre que se detecta y se corrige, el cliente esta expuesto: es el
            # elemento que falta casi siempre (clase 18).
            raise ValueError(
                "falta la medida provisional: el intervalo tambien expone al cliente"
            )


# Parejas de piezas cuya lectura cruzada revela las contradicciones habituales.
PAREJAS_CRITICAS = (
    ("perimetro", "resiliencia"),
    ("calificacion", "informacion_y_conducta"),
    ("salvaguarda", "prevencion_de_lavado"),
    ("datos_personales", "vigilancia_de_mercado"),
    ("regimen_por_jurisdiccion", "informacion_y_conducta"),
)


@dataclass
class Expediente:
    """Las doce piezas, con sus afirmaciones y sus hallazgos."""

    entidad: str
    clientes: int
    afirmaciones: list[Afirmacion] = field(default_factory=list)
    hallazgos: list[Hallazgo] = field(default_factory=list)
    remediaciones: list[Remediacion] = field(default_factory=list)

    def afirmar(self, pieza: str, texto: str, evidencia: str) -> Afirmacion:
        afirmacion = Afirmacion(pieza, texto, evidencia)
        self.afirmaciones.append(afirmacion)
        return afirmacion

    @property
    def piezas_presentes(self) -> set[str]:
        return {a.pieza for a in self.afirmaciones}

    @property
    def piezas_faltantes(self) -> list[str]:
        return [p for p in PIEZAS if p not in self.piezas_presentes]

    @property
    def completo(self) -> bool:
        return not self.piezas_faltantes

    def registrar_hallazgo(
        self, nivel: Nivel, piezas: tuple[str, str], descripcion: str, afectados: int
    ) -> Hallazgo:
        hallazgo = Hallazgo(nivel, piezas, descripcion, afectados)
        self.hallazgos.append(hallazgo)
        return hallazgo

    def remediar(self, **kwargs) -> Remediacion:
        remediacion = Remediacion(**kwargs)
        self.remediaciones.append(remediacion)
        return remediacion

    def priorizados(self) -> list[Hallazgo]:
        """Por nivel y, dentro de cada nivel, por clientes afectados."""
        return sorted(self.hallazgos, key=lambda h: (h.nivel, -h.clientes_afectados))

    @property
    def bloqueantes(self) -> list[Hallazgo]:
        return [h for h in self.hallazgos if h.es_bloqueante]

    @property
    def revision_miro_donde_debia(self) -> bool:
        """Si todos los hallazgos son ordinarios, la revision no miro bien."""
        if not self.hallazgos:
            return False
        return any(h.nivel is not Nivel.ORDINARIO for h in self.hallazgos)

    def hallazgos_sin_remediar(self) -> list[Hallazgo]:
        remediados = {r.hallazgo for r in self.remediaciones}
        return [h for h in self.hallazgos if h.descripcion not in remediados]

    def puede_operar(self) -> tuple[bool, str]:
        """Un bloqueante sin remediar impide operar hasta corregirse."""
        if not self.completo:
            return False, f"faltan piezas: {', '.join(self.piezas_faltantes)}"
        pendientes = [h for h in self.hallazgos_sin_remediar() if h.es_bloqueante]
        if pendientes:
            return False, f"{len(pendientes)} hallazgo(s) bloqueante(s) sin remediar"
        return True, "expediente completo y sin bloqueantes pendientes"
