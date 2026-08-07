"""Screening de sanciones con metricas y prueba retrospectiva.

La regla que el modulo hace cumplir: en sanciones NO hay apetito de riesgo. Un
falso negativo es una operacion con una persona designada, y no existe ahorro
operativo que lo compense.

Por eso `prueba_retrospectiva` es obligatoria antes de cualquier cambio de
umbral, y `evaluar` nunca descarta un caso por FALTA de informacion: lo escala.

AVISO: las listas y nombres de este modulo y de sus datos son SINTETICOS. No
corresponden a ninguna lista oficial ni a ninguna persona real.
"""

from __future__ import annotations

import unicodedata
from dataclasses import dataclass

# Apellidos de alta frecuencia en el conjunto sintetico. Con uno de estos, la
# coincidencia de nombre sola no basta: hace falta un segundo campo.
APELLIDOS_FRECUENTES = frozenset(
    {"nguyen", "silva", "gonzalez", "kim", "patel", "garcia", "wang"}
)

# Equivalencias de transliteracion del conjunto sintetico.
EQUIVALENCIAS = {
    "ph": "f",
    "kh": "k",
    "th": "t",
    "gh": "g",
    "ie": "i",
    "ee": "i",
    "oo": "u",
    "y": "i",
    "z": "s",
    "v": "b",
    "w": "b",
    "qu": "k",
    "ck": "k",
}


@dataclass(frozen=True)
class Designado:
    identificador: str
    nombre: str
    pais: str
    fecha_nacimiento: str = ""


@dataclass(frozen=True)
class Alerta:
    designado: str
    puntuacion: float
    motivo: str
    escalada: bool = False


def normalizar(nombre: str) -> str:
    """Quita acentos, pasa a minusculas y aplica las equivalencias."""
    sin_acentos = "".join(
        c
        for c in unicodedata.normalize("NFKD", nombre.lower())
        if not unicodedata.combining(c)
    )
    limpio = "".join(c if c.isalnum() or c == " " else " " for c in sin_acentos)
    for origen, destino in EQUIVALENCIAS.items():
        limpio = limpio.replace(origen, destino)
    return " ".join(limpio.split())


def similitud(a: str, b: str) -> float:
    """Similitud por tokens: proporcion de palabras compartidas."""
    tokens_a, tokens_b = set(a.split()), set(b.split())
    if not tokens_a or not tokens_b:
        return 0.0
    return len(tokens_a & tokens_b) / max(len(tokens_a), len(tokens_b))


def _apellido_frecuente(nombre: str) -> bool:
    """Se compara sobre nombres YA normalizados.

    La lista se normaliza tambien: si no, «nguyen» de la lista nunca
    coincidiria con «nguien», que es lo que produce la normalizacion.
    """
    frecuentes = {normalizar(a) for a in APELLIDOS_FRECUENTES}
    return any(token in frecuentes for token in nombre.split())


def evaluar(
    nombre: str,
    fecha_nacimiento: str,
    lista: list[Designado],
    umbral: float,
    con_correcciones: bool = True,
) -> list[Alerta]:
    """Compara un nombre contra la lista y devuelve las alertas.

    Con `con_correcciones`, aplica la normalizacion fonetica y la exigencia de
    segundo campo para apellidos frecuentes. La exigencia NO descarta cuando el
    dato falta: escala. Descartar por ausencia de informacion es exactamente el
    falso negativo que hay que evitar.
    """
    consulta = normalizar(nombre) if con_correcciones else nombre.lower().strip()
    alertas: list[Alerta] = []

    for designado in lista:
        objetivo = (
            normalizar(designado.nombre)
            if con_correcciones
            else designado.nombre.lower().strip()
        )
        puntuacion = similitud(consulta, objetivo)
        if puntuacion < umbral:
            continue

        if con_correcciones and _apellido_frecuente(consulta):
            if not fecha_nacimiento or not designado.fecha_nacimiento:
                alertas.append(
                    Alerta(
                        designado.identificador,
                        puntuacion,
                        "apellido frecuente sin fecha para descartar",
                        escalada=True,
                    )
                )
                continue
            if fecha_nacimiento != designado.fecha_nacimiento:
                continue

        alertas.append(
            Alerta(designado.identificador, puntuacion, "coincidencia de nombre")
        )
    return alertas


@dataclass
class Metricas:
    umbral: float
    alertas: int
    verdaderos_positivos: int
    falsos_positivos: int
    falsos_negativos: int

    @property
    def precision(self) -> float:
        total = self.verdaderos_positivos + self.falsos_positivos
        return self.verdaderos_positivos / total if total else 0.0

    @property
    def exhaustividad(self) -> float:
        total = self.verdaderos_positivos + self.falsos_negativos
        return self.verdaderos_positivos / total if total else 0.0


def medir(
    casos: list[tuple[str, str, bool]],
    lista: list[Designado],
    umbral: float,
    con_correcciones: bool = True,
) -> Metricas:
    """`casos` son ternas (nombre, fecha, es_designado_real)."""
    vp = fp = fn = alertas = 0
    for nombre, fecha, real in casos:
        encontradas = evaluar(nombre, fecha, lista, umbral, con_correcciones)
        alertas += len(encontradas)
        if encontradas and real:
            vp += 1
        elif encontradas and not real:
            fp += 1
        elif not encontradas and real:
            fn += 1
    return Metricas(umbral, alertas, vp, fp, fn)


def prueba_retrospectiva(
    confirmados: list[tuple[str, str]],
    lista: list[Designado],
    umbral_actual: float,
    umbral_propuesto: float,
    con_correcciones: bool = True,
) -> dict[str, object]:
    """¿Cuantos verdaderos positivos se pierden con el umbral propuesto?

    Es la comprobacion que ninguna propuesta de subir el umbral puede saltarse.
    """
    perdidos = []
    for nombre, fecha in confirmados:
        con_actual = evaluar(nombre, fecha, lista, umbral_actual, con_correcciones)
        con_propuesto = evaluar(nombre, fecha, lista, umbral_propuesto, con_correcciones)
        if con_actual and not con_propuesto:
            perdidos.append(nombre)
    return {
        "umbral_actual": umbral_actual,
        "umbral_propuesto": umbral_propuesto,
        "confirmados": len(confirmados),
        "perdidos": len(perdidos),
        "nombres_perdidos": perdidos,
        "aceptable": len(perdidos) == 0,
    }
