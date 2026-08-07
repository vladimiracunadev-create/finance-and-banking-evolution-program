"""Diseno de dos tokens con respaldo endogeno y su espiral.

La clase 7 sostiene dos cosas que este modulo demuestra ejecutando:

1. El ratio de absorcion SUBE durante el colapso, y por eso es el indicador
   equivocado.
2. El indicador correcto es la emision por unidad retirada, porque mide la
   aceleracion del mecanismo en vez de una foto de su estado.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Vuelta:
    """Una iteracion del mecanismo de canje."""

    numero: int
    retirado: int
    unidades_emitidas: float
    precio_v_antes: float
    precio_v_despues: float
    circulante_e: int
    capitalizacion_v: float

    @property
    def ratio_absorcion(self) -> float:
        """Capitalizacion del token variable sobre el estable restante."""
        if self.circulante_e == 0:
            return float("inf")
        return self.capitalizacion_v / self.circulante_e

    @property
    def emision_por_unidad(self) -> float:
        """Unidades de V emitidas por cada unidad de E retirada."""
        if self.retirado == 0:
            return 0.0
        return self.unidades_emitidas / self.retirado


@dataclass
class SistemaDeDosTokens:
    """Token estable E respaldado unicamente por el token variable V.

    No hay ningun activo fuera del sistema: por eso el respaldo es circular y
    por eso nada detiene la espiral desde dentro.
    """

    circulante_e: int
    unidades_v: float
    precio_v: float
    fraccion_que_vende: float = 0.70
    impacto_por_millon: float = 0.01 / 20_000_000
    volumen_diario_v: float = 60_000_000
    vueltas: list[Vuelta] = field(default_factory=list)

    @property
    def capitalizacion_v(self) -> float:
        return self.unidades_v * self.precio_v

    @property
    def ratio_absorcion(self) -> float:
        if self.circulante_e == 0:
            return float("inf")
        return self.capitalizacion_v / self.circulante_e

    def canjear(self, importe: int) -> Vuelta:
        """Retira `importe` de E emitiendo V por ese valor."""
        if importe <= 0:
            raise ValueError("el importe debe ser positivo")
        if self.precio_v <= 0:
            raise ValueError("el token variable ya no tiene precio")

        precio_antes = self.precio_v
        capitalizacion_antes = self.capitalizacion_v

        emitidas = importe / precio_antes
        self.unidades_v += emitidas
        self.circulante_e -= min(importe, self.circulante_e)

        # La capitalizacion no crece por emitir: se reparte entre mas unidades.
        precio_sin_venta = capitalizacion_antes / self.unidades_v

        # Y ademas quien recibe V lo vende, lo que hunde el precio.
        vendido = importe * self.fraccion_que_vende
        impacto = min(vendido * self.impacto_por_millon, 0.95)
        self.precio_v = precio_sin_venta * (1 - impacto)

        vuelta = Vuelta(
            numero=len(self.vueltas) + 1,
            retirado=importe,
            unidades_emitidas=emitidas,
            precio_v_antes=precio_antes,
            precio_v_despues=self.precio_v,
            circulante_e=self.circulante_e,
            capitalizacion_v=self.capitalizacion_v,
        )
        self.vueltas.append(vuelta)
        return vuelta

    def venta_generada(self, importe: int) -> float:
        """Venta de V que produce retirar `importe` de E."""
        return importe * self.fraccion_que_vende

    def veces_el_volumen(self, importe: int) -> float:
        """Cuantas veces el volumen diario normal supone esa venta."""
        if self.volumen_diario_v == 0:
            return float("inf")
        return self.venta_generada(importe) / self.volumen_diario_v

    def espiral_acelera(self) -> bool:
        """Cierto si la emision por unidad retirada crece vuelta a vuelta."""
        if len(self.vueltas) < 2:
            return False
        serie = [v.emision_por_unidad for v in self.vueltas]
        return all(b > a for a, b in zip(serie, serie[1:]))


def descomponer_rendimiento(
    circulante: int, rendimiento_anual: float, ingresos_reales: int
) -> dict[str, float]:
    """Separa el rendimiento pagado entre ingresos reales y dilucion.

    Si el rendimiento pagado supera los ingresos, la diferencia no es un
    rendimiento: es una transferencia de los que entran despues a los que
    entraron antes (clase 7).
    """
    pagado = circulante * rendimiento_anual
    dilucion = max(pagado - ingresos_reales, 0)
    return {
        "pagado": pagado,
        "ingresos_reales": float(min(ingresos_reales, pagado)),
        "dilucion": dilucion,
        "porcentaje_dilucion": dilucion / pagado if pagado else 0.0,
    }


def cobertura_de_hibrido(
    exogeno: int, endogeno: int, circulante: int
) -> dict[str, float]:
    """Cobertura en calma y en tension de un diseno hibrido.

    En tension el tramo endogeno se cuenta a cero, porque ese es el escenario
    en el que la cobertura importa (clase 7).
    """
    if circulante == 0:
        return {"en_calma": 0.0, "en_tension": 0.0}
    return {
        "en_calma": (exogeno + endogeno) / circulante,
        "en_tension": exogeno / circulante,
    }
