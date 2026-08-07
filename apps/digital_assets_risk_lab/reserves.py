"""Carteras de reserva: cobertura contable, cobertura liquida y venta forzada.

La clase 4 sostiene que una reserva tiene tres cifras y solo se publica la
primera, y que tras una redencion la cobertura puede SUBIR mientras la
composicion empeora. Este modulo permite comprobarlo.
"""

from __future__ import annotations

from dataclasses import dataclass, field

# Descuento por venta forzada de cada tramo, en tanto por uno, para el primer
# mil millones vendido. La escalera de la clase 6 lo hace crecer con el tamano:
# el descuento no es una opinion pesimista, es la diferencia entre valorar y
# realizar.
DESCUENTO_BASE = {
    "efectivo": 0.0,
    "letras": 0.0015,
    "pactos_inversos": 0.0,
    "deuda_corta": 0.0140,
    "papel_comercial": 0.0350,
    "deposito_plazo": 0.0500,
}

# Tramos disponibles en 24 horas. El papel comercial y los depositos a plazo no
# lo estan, y esa es la diferencia entre la cifra publicada y la util.
DISPONIBLE_24H = {
    "efectivo",
    "letras",
    "pactos_inversos",
    "deuda_corta",
}

# Orden de realizacion: un gestor prudente vende primero lo barato.
ORDEN_DE_VENTA = ["efectivo", "pactos_inversos", "letras", "deuda_corta"]


class TramoDesconocido(ValueError):
    """Un tramo sin descuento declarado no se puede valorar."""


@dataclass
class Cartera:
    """Cartera de reserva de un emisor.

    Los importes son enteros en la unidad menor para evitar redondeos.
    """

    circulante: int
    tramos: dict[str, int] = field(default_factory=dict)

    def __post_init__(self) -> None:
        for nombre in self.tramos:
            if nombre not in DESCUENTO_BASE:
                raise TramoDesconocido(nombre)

    @property
    def total(self) -> int:
        return sum(self.tramos.values())

    @property
    def cobertura_contable(self) -> float:
        if self.circulante == 0:
            return 0.0
        return self.total / self.circulante

    def realizable_24h(self, escalera: bool = False) -> int:
        """Cuanto efectivo se obtiene manana vendiendo lo vendible."""
        total = 0
        for nombre, importe in self.tramos.items():
            if nombre not in DISPONIBLE_24H:
                continue
            total += importe - self.coste_de_vender(nombre, importe, escalera)
        return total

    @property
    def cobertura_liquida(self) -> float:
        if self.circulante == 0:
            return 0.0
        return self.realizable_24h() / self.circulante

    @property
    def peso_iliquido(self) -> float:
        if self.total == 0:
            return 0.0
        iliquido = sum(
            v for k, v in self.tramos.items() if k not in DISPONIBLE_24H
        )
        return iliquido / self.total

    def coste_de_vender(
        self, tramo: str, importe: int, escalera: bool = False
    ) -> int:
        """Coste de realizar `importe` del tramo indicado.

        Con `escalera`, el descuento crece con el tamano de la venta: cada mil
        millones adicionales lo multiplica por 1,5. Es el supuesto de la clase 6
        y es lo que mueve el punto de no retorno.
        """
        if tramo not in DESCUENTO_BASE:
            raise TramoDesconocido(tramo)
        base = DESCUENTO_BASE[tramo]
        if not escalera:
            return round(importe * base)
        restante, coste, factor = importe, 0.0, 1.0
        bloque = 1_000_000_000
        while restante > 0:
            trozo = min(restante, bloque)
            coste += trozo * base * factor
            restante -= trozo
            factor *= 1.5
        return round(coste)


@dataclass(frozen=True)
class Redencion:
    """Resultado de atender una redencion contra la cartera."""

    solicitado: int
    pagado: int
    coste_de_venta: int
    vendido_por_tramo: dict[str, int]
    cubierta: bool

    @property
    def coste_relativo(self) -> float:
        return self.coste_de_venta / self.pagado if self.pagado else 0.0


def atender(cartera: Cartera, importe: int, escalera: bool = False) -> Redencion:
    """Paga `importe` vendiendo por orden de coste creciente.

    Devuelve una cartera modificada in situ: es un laboratorio, y ver el
    remanente deteriorado es justamente el punto de la clase 4.
    """
    pendiente = importe
    coste_total = 0
    vendido: dict[str, int] = {}

    for tramo in ORDEN_DE_VENTA:
        if pendiente <= 0:
            break
        disponible = cartera.tramos.get(tramo, 0)
        if disponible <= 0:
            continue
        descuento = DESCUENTO_BASE[tramo]
        # Para obtener `pendiente` neto hay que vender nominal por encima.
        nominal_necesario = round(pendiente / (1 - descuento)) if descuento else pendiente
        nominal = min(disponible, nominal_necesario)
        coste = cartera.coste_de_vender(tramo, nominal, escalera)
        neto = nominal - coste
        cartera.tramos[tramo] = disponible - nominal
        vendido[tramo] = nominal
        coste_total += coste
        pendiente -= neto

    pagado = importe - max(pendiente, 0)
    cartera.circulante -= pagado
    return Redencion(
        solicitado=importe,
        pagado=pagado,
        coste_de_venta=coste_total,
        vendido_por_tramo=vendido,
        cubierta=pendiente <= 0,
    )


def punto_de_no_retorno(cartera: Cartera, margen: int) -> int:
    """Redencion acumulada que agota el margen de sobrecolateralizacion.

    Se calcula con la escalera de descuentos, porque con descuento constante la
    conclusion cambia y deja de ser util (clase 6, paso 5).
    """
    if margen <= 0:
        return 0
    copia = Cartera(cartera.circulante, dict(cartera.tramos))
    acumulado, coste_acumulado = 0, 0
    paso = max(cartera.circulante // 200, 1)
    while coste_acumulado < margen and copia.total > 0:
        resultado = atender(copia, paso, escalera=True)
        if resultado.pagado == 0:
            break
        acumulado += resultado.pagado
        coste_acumulado += resultado.coste_de_venta
    return acumulado
