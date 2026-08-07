"""Colateral, llamadas de margen y cascada de liquidaciones.

La clase 14 sostiene que lo que rompe un sistema de margen no es el recorte sino
liquidar posiciones ENTERAS contra un mercado menos profundo que el volumen a
vender. La correccion mas eficaz —liquidar solo lo necesario— no toca ningun
parametro de riesgo.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Posicion:
    identificador: str
    prestamo: int
    colateral_unidades: int

    def ratio(self, precio: float) -> float:
        if self.prestamo == 0:
            return float("inf")
        return self.colateral_unidades * precio / self.prestamo


@dataclass(frozen=True)
class Vuelta:
    numero: int
    precio_antes: float
    precio_despues: float
    en_llamada: int
    liquidadas: int
    volumen_vendido: float
    impacto: float


def recorte(
    volatilidad_diaria: float,
    factor_confianza: float,
    impacto_de_mercado: float,
    coste_operacion: float,
) -> float:
    """Recorte minimo: cubre lo que pasa DESPUES de decidir liquidar.

    No debe confundirse con el colchon entre el ratio exigido y el umbral de
    liquidacion, que cubre lo que pasa ANTES (clase 14, paso 2).
    """
    return volatilidad_diaria * factor_confianza + impacto_de_mercado + coste_operacion


def colchon_implicito(ratio_exigido: float, umbral_liquidacion: float) -> float:
    """Caida de precio admisible antes de liquidar."""
    if ratio_exigido <= 0:
        raise ValueError("el ratio exigido debe ser positivo")
    return 1 - umbral_liquidacion / ratio_exigido


@dataclass
class Sistema:
    """Cartera de posiciones con umbrales de llamada y liquidacion."""

    precio: float
    ratio_exigido: float = 1.50
    umbral_llamada: float = 1.35
    umbral_liquidacion: float = 1.20
    profundidad_1pc: float = 2_400_000
    liquidacion_parcial: bool = False
    max_por_ventana: float | None = None
    pausa_si_cae_mas_de: float | None = None
    posiciones: list[Posicion] = field(default_factory=list)
    vueltas: list[Vuelta] = field(default_factory=list)
    pausado: bool = False

    def agregar(self, posicion: Posicion) -> None:
        self.posiciones.append(posicion)

    def en_llamada(self) -> list[Posicion]:
        return [
            p
            for p in self.posiciones
            if self.umbral_liquidacion <= p.ratio(self.precio) < self.umbral_llamada
        ]

    def en_liquidacion(self) -> list[Posicion]:
        return [
            p for p in self.posiciones if p.ratio(self.precio) < self.umbral_liquidacion
        ]

    def volumen_a_vender(self, posicion: Posicion) -> float:
        """Unidades a vender: la posicion entera o solo lo necesario.

        Con liquidacion parcial se vende lo justo para volver al ratio exigido,
        y eso reduce el volumen de la vuelta en un factor grande.
        """
        if not self.liquidacion_parcial:
            return posicion.colateral_unidades * self.precio

        objetivo = posicion.prestamo * self.ratio_exigido
        actual = posicion.colateral_unidades * self.precio
        if actual >= objetivo:
            return 0.0
        # Vender colateral reduce el prestamo y el colateral a la vez.
        faltante = objetivo - actual
        return min(faltante / self.ratio_exigido, actual)

    def impacto(self, volumen: float) -> float:
        """Impacto proporcional al volumen frente a la profundidad al 1 %."""
        if self.profundidad_1pc <= 0:
            return 1.0
        return min(volumen / self.profundidad_1pc * 0.01, 0.95)

    def aplicar_caida(self, caida: float) -> Vuelta:
        """Baja el precio y ejecuta una vuelta de liquidaciones."""
        precio_antes = self.precio
        self.precio = precio_antes * (1 - caida)

        if self.pausa_si_cae_mas_de is not None and caida > self.pausa_si_cae_mas_de:
            self.pausado = True
            vuelta = Vuelta(
                len(self.vueltas) + 1, precio_antes, self.precio, 0, 0, 0.0, 0.0
            )
            self.vueltas.append(vuelta)
            return vuelta

        llamada = len(self.en_llamada())
        liquidables = self.en_liquidacion()
        volumen = sum(self.volumen_a_vender(p) for p in liquidables)
        if self.max_por_ventana is not None:
            volumen = min(volumen, self.max_por_ventana)

        impacto = self.impacto(volumen)
        for posicion in liquidables:
            self.posiciones.remove(posicion)

        vuelta = Vuelta(
            numero=len(self.vueltas) + 1,
            precio_antes=precio_antes,
            precio_despues=self.precio,
            en_llamada=llamada,
            liquidadas=len(liquidables),
            volumen_vendido=volumen,
            impacto=impacto,
        )
        self.vueltas.append(vuelta)
        return vuelta

    def cascada(self, caida_inicial: float, max_vueltas: int = 10) -> list[Vuelta]:
        """Encadena vueltas mientras la venta forzada siga moviendo el precio."""
        vuelta = self.aplicar_caida(caida_inicial)
        while (
            len(self.vueltas) < max_vueltas
            and vuelta.impacto > 0
            and vuelta.liquidadas > 0
            and not self.pausado
        ):
            vuelta = self.aplicar_caida(vuelta.impacto)
        return self.vueltas

    @property
    def amplifica(self) -> bool:
        """Cierto si alguna vuelta liquido mas que la anterior."""
        if len(self.vueltas) < 2:
            return False
        return any(
            b.liquidadas > a.liquidadas
            for a, b in zip(self.vueltas, self.vueltas[1:])
        )
