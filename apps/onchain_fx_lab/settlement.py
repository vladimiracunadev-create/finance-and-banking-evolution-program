"""Riesgo de liquidacion en divisas: ventana, neteo, limites y PvP.

La clase 12 sostiene tres cosas que este modulo hace explicitas:

1. La ventana va de que MI pago es irrevocable a que CONFIRMO el contravalor,
   no del envio a la recepcion esperada.
2. Cada mecanismo se compara con la perdida esperada SIN ningun mecanismo.
   Compararlo con la que ya redujo otro invierte la conclusion.
3. El neteo solo reduce la exposicion si el acuerdo es oponible en el concurso
   de la contraparte. Si no lo es, no reduce nada.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Mecanismo(str, Enum):
    NINGUNO = "ninguno"
    NETEO = "neteo"
    PVP_BRUTO = "pvp_bruto"
    PVP_NETEADO = "pvp_neteado"


@dataclass(frozen=True)
class Ventana:
    """Intervalo de exposicion al principal, en horas."""

    horas: float
    descripcion: str

    @property
    def dias(self) -> float:
        return self.horas / 24


def ventana_de_exposicion(
    hora_irrevocable: int,
    hora_confirmacion: int,
    diferencia_horaria: int,
    dias_no_habiles: int = 0,
) -> Ventana:
    """De irrevocable a confirmado, con husos y dias no habiles.

    `hora_confirmacion` esta en hora local de la divisa recibida; se traduce a
    la hora de la divisa entregada restando la diferencia horaria.
    """
    confirmacion_en_origen = hora_confirmacion - diferencia_horaria
    horas = confirmacion_en_origen - hora_irrevocable
    if horas <= 0:
        horas += 24
    horas += dias_no_habiles * 24
    descripcion = (
        f"irrevocable a las {hora_irrevocable:02d}:00, "
        f"confirmado {horas:.0f} horas despues"
    )
    return Ventana(horas, descripcion)


def perdida_esperada(
    exposicion: float,
    probabilidad_diaria: float,
    recuperacion: float,
    dias_de_exposicion: float,
    ocasiones_al_ano: int,
) -> float:
    """Perdida esperada anual por riesgo de principal."""
    return (
        exposicion
        * probabilidad_diaria
        * dias_de_exposicion
        * (1 - recuperacion)
        * ocasiones_al_ano
    )


@dataclass
class Comparacion:
    """Evalua los mecanismos contra la MISMA base: la perdida sin mecanismo."""

    perdida_sin_mecanismo: float
    exposicion_bruta: float
    fraccion_neteada: float
    coste_financiacion_anual: float
    fraccion_prefinanciada: float
    neteo_oponible: bool = True

    def _perdida(self, mecanismo: Mecanismo) -> float:
        if mecanismo is Mecanismo.NINGUNO:
            return self.perdida_sin_mecanismo
        if mecanismo is Mecanismo.NETEO:
            if not self.neteo_oponible:
                # Sin oponibilidad, el neteo no reduce nada en el concurso.
                return self.perdida_sin_mecanismo
            return self.perdida_sin_mecanismo * self.fraccion_neteada
        return 0.0  # los dos PvP eliminan el riesgo de principal

    def _coste(self, mecanismo: Mecanismo) -> float:
        if mecanismo in (Mecanismo.NINGUNO, Mecanismo.NETEO):
            return 0.0
        base = self.exposicion_bruta
        if mecanismo is Mecanismo.PVP_NETEADO:
            if not self.neteo_oponible:
                # Sin neteo valido, el PvP liquida el bruto.
                base = self.exposicion_bruta
            else:
                base = self.exposicion_bruta * self.fraccion_neteada
        # Prefinanciacion en ambas divisas.
        return base * self.fraccion_prefinanciada * 2 * self.coste_financiacion_anual

    def evaluar(self) -> dict[str, dict[str, float]]:
        resultado: dict[str, dict[str, float]] = {}
        for mecanismo in Mecanismo:
            perdida = self._perdida(mecanismo)
            coste = self._coste(mecanismo)
            resultado[mecanismo.value] = {
                "perdida_esperada": perdida,
                "coste": coste,
                "total": perdida + coste,
            }
        return resultado

    def mejor(self) -> str:
        evaluacion = self.evaluar()
        return min(evaluacion, key=lambda k: evaluacion[k]["total"])


def limite_bilateral(
    perdida_sin_mecanismo: float, exposicion_bruta: float, apetito: float
) -> float:
    """Limite que deja la perdida esperada dentro del apetito declarado.

    Es lo que procede cuando ningun mecanismo mejora: reducir la exposicion
    hasta que la perdida quepa (clase 12, paso 8).
    """
    if perdida_sin_mecanismo <= 0:
        return exposicion_bruta
    return apetito / perdida_sin_mecanismo * exposicion_bruta
