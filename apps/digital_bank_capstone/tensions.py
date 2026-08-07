"""Tensiones de diseno: decisiones correctas que se contradicen al integrarse.

Es el contenido especifico del capstone. Cada decision de las clases 4 a 11 era
correcta por separado; la clase 12 las hace funcionar juntas y aparecen las
contradicciones. Este modulo las representa y exige que cada una se resuelva
eligiendo y declarando lo que se sacrifica.
"""

from __future__ import annotations

from dataclasses import dataclass, field


class TensionSinResolver(RuntimeError):
    """Una tension sin resolucion declarada bloquea el expediente."""


@dataclass(frozen=True)
class Decision:
    """Una decision de diseno con lo que gana y lo que cuesta."""

    nombre: str
    clase: int
    beneficio: str
    coste_anual: int


@dataclass
class Tension:
    """Dos decisiones correctas que se contradicen al integrarse."""

    a: Decision
    b: Decision
    descripcion: str
    sacrificio: str | None = None
    cuantificacion: int | None = None

    @property
    def resuelta(self) -> bool:
        return bool(self.sacrificio) and self.cuantificacion is not None

    def resolver(self, sacrificio: str, cuantificacion: int) -> None:
        if not sacrificio:
            raise ValueError("hay que declarar qué se sacrifica")
        self.sacrificio = sacrificio
        self.cuantificacion = cuantificacion


@dataclass
class Tolerancia:
    """Interrupcion maxima admisible de una funcion, fijada por el consejo."""

    funcion: str
    horas: float
    fijada_por: str

    def se_cumple(self, interrupcion_horas: float) -> bool:
        return interrupcion_horas <= self.horas


@dataclass
class Sistema:
    """El sistema integrado, con sus decisiones y sus tensiones."""

    decisiones: list[Decision] = field(default_factory=list)
    tensiones: list[Tension] = field(default_factory=list)
    tolerancias: list[Tolerancia] = field(default_factory=list)

    def decidir(self, decision: Decision) -> None:
        self.decisiones.append(decision)

    def declarar_tension(self, a: str, b: str, descripcion: str) -> Tension:
        por_nombre = {d.nombre: d for d in self.decisiones}
        for nombre in (a, b):
            if nombre not in por_nombre:
                raise KeyError(f"decision desconocida: {nombre}")
        tension = Tension(por_nombre[a], por_nombre[b], descripcion)
        self.tensiones.append(tension)
        return tension

    def fijar_tolerancia(self, funcion: str, horas: float, fijada_por: str) -> None:
        if fijada_por != "consejo":
            # La clase 12 y la Parte 22, clase 14 lo exigen: la tolerancia se
            # fija por funcion de negocio y desde el consejo, no por el area
            # tecnica que mide disponibilidad.
            raise ValueError("la tolerancia la fija el consejo, no el area tecnica")
        self.tolerancias.append(Tolerancia(funcion, horas, fijada_por))

    def sin_resolver(self) -> list[Tension]:
        return [t for t in self.tensiones if not t.resuelta]

    def coste_anual(self) -> int:
        return sum(d.coste_anual for d in self.decisiones)

    def tolerancias_incumplidas(self, interrupciones: dict[str, float]) -> list[str]:
        """Funciones cuya tolerancia no se cumple en un escenario dado."""
        return [
            t.funcion
            for t in self.tolerancias
            if t.funcion in interrupciones
            and not t.se_cumple(interrupciones[t.funcion])
        ]

    def puede_operar(self) -> tuple[bool, str]:
        pendientes = self.sin_resolver()
        if pendientes:
            return False, f"{len(pendientes)} tension(es) sin resolver ni declarar"
        return True, "todas las tensiones resueltas y declaradas"
