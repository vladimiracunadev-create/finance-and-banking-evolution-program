"""Determinacion del perimetro por hechos observables.

La clase 1 sostiene que la pregunta no es «esta regulado el token» sino «que esta
haciendo esta entidad», y que eso no lo decide la etiqueta que ella elija. Este
modulo aplica las seis preguntas sobre HECHOS, y deja constancia de la diferencia
entre lo declarado y lo efectivo.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Regimen(str, Enum):
    CAPTACION = "captacion"
    CUSTODIA = "custodia"
    MERCADO = "mercado"
    INTERMEDIACION = "intermediacion"
    ASESORIA = "asesoria"
    PAGOS = "pagos"
    CREDITO = "credito"
    CAMBIO = "cambio"


@dataclass(frozen=True)
class Hecho:
    """Un dato verificable, con la fuente que permite comprobarlo.

    Un hecho sin fuente no vale: la clase 1 distingue el hecho observable de la
    declaracion precisamente porque el primero se puede contrastar.
    """

    clave: str
    descripcion: str
    fuente: str

    def __post_init__(self) -> None:
        if not self.fuente:
            raise ValueError("un hecho sin fuente no es observable")


# Cada regimen se activa por una combinacion de hechos. La combinacion es una
# lista de conjuntos: basta con que UNO de los conjuntos este completo.
ACTIVADORES: dict[Regimen, tuple[frozenset[str], ...]] = {
    Regimen.CAPTACION: (frozenset({"recibe_fondos", "obligacion_de_devolver"}),),
    Regimen.CUSTODIA: (
        frozenset({"tiene_las_claves"}),
        frozenset({"controla_el_activo_de_terceros"}),
    ),
    Regimen.MERCADO: (frozenset({"casa_ordenes_de_terceros"}),),
    Regimen.INTERMEDIACION: (frozenset({"ejecuta_por_cuenta_ajena"}),),
    Regimen.ASESORIA: (
        frozenset({"recomienda_instrumentos"}),
        frozenset({"destaca_instrumentos", "cobra_por_destacar"}),
    ),
    Regimen.PAGOS: (frozenset({"transfiere_fondos_de_terceros"}),),
    Regimen.CREDITO: (frozenset({"presta_fondos"}),),
    Regimen.CAMBIO: (frozenset({"convierte_moneda_con_margen"}),),
}

# Lo que sigue aplicando aunque ningun regimen financiero se active. «No estamos
# regulados» suele significar «no necesitamos autorizacion financiera», y omite
# estas cinco (clase 1).
SIEMPRE_APLICAN = (
    "proteccion al consumidor",
    "publicidad no enganosa",
    "proteccion de datos personales",
    "prevencion de lavado, si hay umbral",
    "responsabilidad civil y penal general",
)


@dataclass
class Entidad:
    """Una entidad con lo que declara y lo que hace."""

    nombre: str
    declarados: set[Regimen] = field(default_factory=set)
    hechos: dict[str, Hecho] = field(default_factory=dict)

    def declarar(self, *regimenes: Regimen) -> None:
        self.declarados.update(regimenes)

    def observar(self, clave: str, descripcion: str, fuente: str) -> Hecho:
        hecho = Hecho(clave, descripcion, fuente)
        self.hechos[clave] = hecho
        return hecho

    def efectivos(self) -> set[Regimen]:
        """Regimenes que activan los hechos, con independencia de lo declarado."""
        activos: set[Regimen] = set()
        presentes = set(self.hechos)
        for regimen, combinaciones in ACTIVADORES.items():
            if any(combinacion <= presentes for combinacion in combinaciones):
                activos.add(regimen)
        return activos

    def no_declarados(self) -> set[Regimen]:
        """Lo que la entidad ejerce sin haberlo declarado.

        Es el hallazgo de la clase 1: no declarar una actividad no la desactiva.
        """
        return self.efectivos() - self.declarados

    def declarados_sin_ejercer(self) -> set[Regimen]:
        return self.declarados - self.efectivos()

    def evidencia(self, regimen: Regimen) -> list[Hecho]:
        """Hechos que sostienen la activacion de un regimen."""
        for combinacion in ACTIVADORES[regimen]:
            if combinacion <= set(self.hechos):
                return [self.hechos[c] for c in sorted(combinacion)]
        return []


def informe(entidad: Entidad) -> dict:
    """Resumen con las tres capas que la clase 1 exige separar."""
    efectivos = entidad.efectivos()
    return {
        "hecho": {r.value: [h.fuente for h in entidad.evidencia(r)] for r in efectivos},
        "declarado": sorted(r.value for r in entidad.declarados),
        "no_declarado": sorted(r.value for r in entidad.no_declarados()),
        "siempre_aplican": list(SIEMPRE_APLICAN),
    }
