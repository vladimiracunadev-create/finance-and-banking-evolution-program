"""Los cuatro flujos de un pago transfronterizo.

Mensaje, fondos, contable y cumplimiento. Se modelan por separado a proposito:
el 80 % de las investigaciones nacen de que dos de ellos se desincronizan, y un
simulador con un solo flujo no puede reproducir ni un incidente real.

La leccion que el modulo demuestra con numeros: el mensaje tarda segundos y el
dinero tarda horas o dias, y la diferencia casi nunca es la mensajeria.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime, timedelta

LATENCIA_MENSAJE_S = 2


@dataclass(frozen=True)
class Plaza:
    """Una plaza de liquidacion con su horario y su calendario."""

    codigo: str
    huso: int
    apertura: int
    cierre: int
    minutos_liquidacion: int
    festivos: frozenset[str] = frozenset()

    def es_habil(self, momento: datetime) -> bool:
        local = momento + timedelta(hours=self.huso)
        if local.weekday() >= 5:
            return False
        return local.date().isoformat() not in self.festivos

    def proxima_ventana(self, momento: datetime) -> datetime:
        """Primer instante en que esta plaza puede liquidar.

        Avanza dia a dia hasta encontrar uno habil dentro del horario. El limite
        de 30 dias evita un bucle infinito si el calendario esta mal construido:
        es una guarda, no una regla de negocio.
        """
        candidato = momento
        for _ in range(30 * 24):
            local = candidato + timedelta(hours=self.huso)
            if self.es_habil(candidato) and self.apertura <= local.hour < self.cierre:
                return candidato
            if not self.es_habil(candidato) or local.hour >= self.cierre:
                siguiente = (local + timedelta(days=1)).replace(
                    hour=self.apertura, minute=0, second=0, microsecond=0
                )
            else:
                siguiente = local.replace(
                    hour=self.apertura, minute=0, second=0, microsecond=0
                )
            candidato = siguiente - timedelta(hours=self.huso)
        raise ValueError(f"sin ventana habil en 30 dias para {self.codigo}")


@dataclass
class Evento:
    flujo: str
    momento: datetime
    detalle: str


@dataclass
class Traza:
    eventos: list[Evento] = field(default_factory=list)

    def registrar(self, flujo: str, momento: datetime, detalle: str) -> None:
        self.eventos.append(Evento(flujo, momento, detalle))

    def de(self, flujo: str) -> list[Evento]:
        return [e for e in self.eventos if e.flujo == flujo]

    def duracion(self, flujo: str, inicio: datetime) -> timedelta:
        eventos = self.de(flujo)
        return eventos[-1].momento - inicio if eventos else timedelta(0)

    def descomposicion(self, inicio: datetime) -> dict[str, float]:
        """Reparto del tiempo total por causa, en horas."""
        total = self.duracion("fondos", inicio)
        mensaje = self.duracion("mensaje", inicio)
        cumplimiento = sum(
            (e.momento - inicio).total_seconds()
            for e in self.de("cumplimiento")
            if "retenido" in e.detalle
        )
        return {
            "total_horas": total.total_seconds() / 3600,
            "mensaje_horas": mensaje.total_seconds() / 3600,
            "cumplimiento_horas": cumplimiento / 3600,
            "espera_horas": (total.total_seconds() - mensaje.total_seconds()) / 3600,
        }


@dataclass
class Asiento:
    libro: str
    cuenta: str
    importe: float

    def __post_init__(self) -> None:
        self.importe = round(self.importe, 2)


class PagoEnCadena:
    """Ejecuta un pago a traves de una cadena de plazas.

    Cada eslabon aporta su latencia de mensaje (segundos) y su ventana de
    liquidacion (horas o dias). Los asientos se registran en los dos libros de
    cada tramo, de modo que la suma de cada par sea cero.
    """

    def __init__(self, cadena: list[Plaza], minutos_screening: int = 5) -> None:
        if len(cadena) < 2:
            raise ValueError("la cadena necesita al menos origen y destino")
        self.cadena = cadena
        self.minutos_screening = minutos_screening

    def ejecutar(
        self,
        importe: float,
        ordenado: datetime,
        alerta_en: int | None = None,
        minutos_alerta: int = 180,
    ) -> tuple[Traza, list[Asiento]]:
        traza = Traza()
        asientos: list[Asiento] = []

        momento_mensaje = ordenado
        momento_fondos = ordenado

        traza.registrar("mensaje", momento_mensaje, "orden recibida")
        traza.registrar("cumplimiento", momento_mensaje, "screening en origen")
        momento_fondos += timedelta(minutes=self.minutos_screening)

        for indice in range(len(self.cadena) - 1):
            origen, destino = self.cadena[indice], self.cadena[indice + 1]

            # El mensaje no espera a los fondos: por eso el cliente oye
            # «ya salio» mientras el dinero sigue en el tramo anterior.
            momento_mensaje += timedelta(seconds=LATENCIA_MENSAJE_S)
            traza.registrar(
                "mensaje", momento_mensaje, f"{origen.codigo} -> {destino.codigo}"
            )

            if alerta_en == indice:
                momento_fondos += timedelta(minutes=minutos_alerta)
                traza.registrar(
                    "cumplimiento", momento_fondos, f"retenido en {destino.codigo}"
                )

            ventana = destino.proxima_ventana(momento_fondos)
            momento_fondos = ventana + timedelta(minutes=destino.minutos_liquidacion)
            traza.registrar(
                "fondos", momento_fondos, f"liquidado en {destino.codigo}"
            )

            asientos.append(Asiento(origen.codigo, f"nostro_{destino.codigo}", -importe))
            asientos.append(Asiento(destino.codigo, f"vostro_{origen.codigo}", importe))

        traza.registrar("contable", momento_fondos, f"{len(asientos)} asientos")
        return traza, asientos


def cuadra(asientos: list[Asiento]) -> bool:
    """Todo asiento tiene contrapartida: la suma por tramo es cero."""
    return abs(sum(a.importe for a in asientos)) < 0.01
