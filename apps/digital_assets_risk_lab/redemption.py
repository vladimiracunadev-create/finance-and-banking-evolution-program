"""La cola de redencion: orden de llegada, prorrateo y antidilucion.

La clase 5 sostiene que la corrida no la causa el panico sino el diseno de la
cola: si ser el primero vale algo, todo tenedor racional solicita ya. Este
modulo mide cuanto vale ser el primero en cada diseno.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Regla(str, Enum):
    ORDEN_DE_LLEGADA = "orden_de_llegada"
    PRORRATEO = "prorrateo"


@dataclass(frozen=True)
class Solicitud:
    tenedor: str
    importe: int
    turno: int
    necesita: bool = False


@dataclass(frozen=True)
class Pago:
    tenedor: str
    solicitado: int
    pagado: int
    coste_soportado: int

    @property
    def fraccion(self) -> float:
        return self.pagado / self.solicitado if self.solicitado else 0.0


@dataclass(frozen=True)
class Resultado:
    regla: Regla
    pagos: list[Pago]
    efectivo_usado: int
    coste_total: int

    @property
    def ventaja_del_primero(self) -> float:
        """Diferencia entre la mejor y la peor fraccion cobrada.

        Es el numero que decide si hay corrida: si vale cero, solicita quien
        necesita el dinero; si es positivo, solicita todo el mundo.
        """
        if not self.pagos:
            return 0.0
        fracciones = [p.fraccion for p in self.pagos]
        return max(fracciones) - min(fracciones)


@dataclass
class Cola:
    """Ventana de redencion con una regla de reparto.

    `coste_de_venta` es el coste real de realizar activos (clase 4). Con
    `antidilucion`, lo soporta quien redime; sin ella, lo soportan los que se
    quedan, que es exactamente el incentivo a salir primero.
    """

    efectivo: int
    coste_de_venta: float = 0.0
    antidilucion: bool = False
    tramo_minimo_integro: int = 0
    solicitudes: list[Solicitud] = field(default_factory=list)

    def solicitar(
        self, tenedor: str, importe: int, necesita: bool = False
    ) -> Solicitud:
        solicitud = Solicitud(tenedor, importe, len(self.solicitudes), necesita)
        self.solicitudes.append(solicitud)
        return solicitud

    @property
    def total_solicitado(self) -> int:
        return sum(s.importe for s in self.solicitudes)

    def resolver(self, regla: Regla) -> Resultado:
        if regla is Regla.ORDEN_DE_LLEGADA:
            return self._orden_de_llegada()
        return self._prorrateo()

    def _cargo(self, pagado: int) -> int:
        return round(pagado * self.coste_de_venta) if self.antidilucion else 0

    def _orden_de_llegada(self) -> Resultado:
        disponible = self.efectivo
        pagos: list[Pago] = []
        coste_total = 0
        for solicitud in sorted(self.solicitudes, key=lambda s: s.turno):
            bruto = min(solicitud.importe, disponible)
            cargo = self._cargo(bruto)
            disponible -= bruto
            coste_total += cargo
            pagos.append(Pago(solicitud.tenedor, solicitud.importe, bruto - cargo, cargo))
        return Resultado(
            Regla.ORDEN_DE_LLEGADA, pagos, self.efectivo - disponible, coste_total
        )

    def _prorrateo(self) -> Resultado:
        total = self.total_solicitado
        if total == 0:
            return Resultado(Regla.PRORRATEO, [], 0, 0)

        # El tramo minimo integro protege al minorista sin reabrir la carrera:
        # el grande sigue prorrateado (clase 5, paso 7).
        reservado = 0
        integro: dict[str, int] = {}
        if self.tramo_minimo_integro > 0:
            for solicitud in self.solicitudes:
                trozo = min(solicitud.importe, self.tramo_minimo_integro)
                integro[solicitud.tenedor] = trozo
                reservado += trozo
            if reservado > self.efectivo:
                # No alcanza ni para el tramo minimo: se prorratea tambien.
                integro = {}
                reservado = 0

        resto_disponible = self.efectivo - reservado
        resto_solicitado = total - reservado
        fraccion = resto_disponible / resto_solicitado if resto_solicitado > 0 else 0.0
        fraccion = min(fraccion, 1.0)

        pagos: list[Pago] = []
        coste_total = 0
        usado = 0
        for solicitud in self.solicitudes:
            base = integro.get(solicitud.tenedor, 0)
            resto = solicitud.importe - base
            bruto = base + round(resto * fraccion)
            cargo = self._cargo(bruto)
            usado += bruto
            coste_total += cargo
            pagos.append(Pago(solicitud.tenedor, solicitud.importe, bruto - cargo, cargo))
        return Resultado(Regla.PRORRATEO, pagos, usado, coste_total)


def solicitud_del_dia_siguiente(
    resultado: Resultado,
    fraccion_que_necesita: float,
    nuevos_por_miedo: int,
) -> int:
    """Cuanto se solicitara manana segun lo que valio ser primero hoy.

    Con ventaja cero solo vuelve quien necesita el dinero. Con ventaja
    positiva vuelve todo el pendiente y ademas entran los que ven la carrera.
    """
    pendiente = sum(p.solicitado - p.pagado for p in resultado.pagos)
    if resultado.ventaja_del_primero > 0:
        return pendiente + nuevos_por_miedo
    return round(pendiente * fraccion_que_necesita)
