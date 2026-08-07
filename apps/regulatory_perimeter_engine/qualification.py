"""Calificacion de un instrumento por los cuatro criterios.

La clase 3 sostiene que la calificacion no la elige quien emite y que el material
de promocion FORMA PARTE de ella: la misma unidad puede ser utilidad o valor
segun como se venda. Este modulo lo hace explicito exigiendo que la promocion se
analice, no que se declare.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import Enum


class Calificacion(str, Enum):
    VALOR = "valor"
    DINERO_ELECTRONICO = "dinero_electronico"
    REFERENCIADO = "referenciado"
    UTILIDAD = "utilidad"
    SIN_CALIFICAR = "sin_calificar"


# Expresiones que crean expectativa de beneficio derivada del esfuerzo ajeno.
# No hace falta prometer rentabilidad: basta con crear la expectativa (clase 3).
PATRONES_DE_EXPECTATIVA = (
    r"\bel precio subir[aá]\b",
    r"\brevaloriz",
    r"\bla demanda .{0,30}aumentar[aá]\b",
    r"\bcuando .{0,40}crezca .{0,30}(valor|precio|demanda)",
    r"\brentabilidad\b",
    r"\bretorno de la inversi[oó]n\b",
    r"\bganancia\b",
)


@dataclass(frozen=True)
class CuatroCriterios:
    """Los cuatro criterios de la clase 3. El cuarto es el decisivo."""

    inversion_de_dinero: bool
    proyecto_comun: bool
    expectativa_de_beneficio: bool
    esfuerzo_de_un_tercero: bool

    @property
    def cuantos(self) -> int:
        return sum(
            (
                self.inversion_de_dinero,
                self.proyecto_comun,
                self.expectativa_de_beneficio,
                self.esfuerzo_de_un_tercero,
            )
        )

    @property
    def probablemente_valor(self) -> bool:
        return self.cuantos == 4


@dataclass
class Instrumento:
    """Un instrumento con sus caracteristicas y su material de promocion."""

    nombre: str
    servicio_en_funcionamiento: bool
    se_consume_al_usarlo: bool
    mercado_secundario_desde_el_inicio: bool
    financia_el_desarrollo: bool
    emitido_contra_fondos: bool = False
    derecho_de_reembolso_a_la_par: bool = False
    emisor_autorizado: bool = False
    promocion: list[str] = field(default_factory=list)
    compradores_que_usan_el_servicio: float = 1.0

    def frases_que_crean_expectativa(self) -> list[str]:
        """Devuelve las frases de la promocion que califican.

        Se analiza el material, no se pregunta al emisor: es la diferencia entre
        una calificacion y una preferencia.
        """
        encontradas: list[str] = []
        for frase in self.promocion:
            for patron in PATRONES_DE_EXPECTATIVA:
                if re.search(patron, frase, flags=re.IGNORECASE):
                    encontradas.append(frase)
                    break
        return encontradas

    def criterios(self) -> CuatroCriterios:
        return CuatroCriterios(
            inversion_de_dinero=self.emitido_contra_fondos or self.financia_el_desarrollo,
            proyecto_comun=self.financia_el_desarrollo,
            expectativa_de_beneficio=bool(self.frases_que_crean_expectativa())
            or self.compradores_que_usan_el_servicio < 0.5,
            esfuerzo_de_un_tercero=not self.servicio_en_funcionamiento,
        )

    @property
    def utilidad_aparente(self) -> bool:
        """Utilidad de verdad exige que el servicio funcione HOY."""
        return not self.servicio_en_funcionamiento and (
            self.mercado_secundario_desde_el_inicio or self.financia_el_desarrollo
        )

    def calificar(self) -> Calificacion:
        if self.criterios().probablemente_valor:
            return Calificacion.VALOR
        if self.emisor_autorizado and self.derecho_de_reembolso_a_la_par:
            return Calificacion.DINERO_ELECTRONICO
        if self.emitido_contra_fondos and self.derecho_de_reembolso_a_la_par:
            return Calificacion.REFERENCIADO
        if self.servicio_en_funcionamiento and self.se_consume_al_usarlo:
            return Calificacion.UTILIDAD
        return Calificacion.SIN_CALIFICAR


# Coste anual de cumplimiento por calificacion. La diferencia es el incentivo a
# calificar mal, y es exactamente por lo que la calificacion no la elige quien
# emite (clase 3).
COSTE_DE_CUMPLIMIENTO = {
    Calificacion.VALOR: 380_000,
    Calificacion.DINERO_ELECTRONICO: 260_000,
    Calificacion.REFERENCIADO: 300_000,
    Calificacion.UTILIDAD: 40_000,
    Calificacion.SIN_CALIFICAR: 0,
}


def coste_de_una_recalificacion(
    importe_colocado: int, coste_legal: int, calificacion_correcta: Calificacion
) -> dict:
    """Compara lo «ahorrado» con lo arriesgado si la calificacion se corrige.

    En la clase 3, el ahorro era el 1,1 % del riesgo.
    """
    ahorro = (
        COSTE_DE_CUMPLIMIENTO[calificacion_correcta]
        - COSTE_DE_CUMPLIMIENTO[Calificacion.UTILIDAD]
    )
    riesgo = importe_colocado + coste_legal
    return {
        "ahorro": ahorro,
        "riesgo": riesgo,
        "ahorro_sobre_riesgo": ahorro / riesgo if riesgo else 0.0,
    }
