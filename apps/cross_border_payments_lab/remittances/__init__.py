"""Comparador de remesas con el denominador honesto.

La unica cifra comparable entre rutas es cuanto RECIBE el beneficiario, medida
contra lo que recibiria al tipo de referencia sin ningun coste. Comparar
comisiones anunciadas es lo que hace que dos rutas caras parezcan competitivas
entre si.

Los datos de operadores del laboratorio son SINTETICOS.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(frozen=True)
class Tramo:
    """Una conversion con su tipo aplicado y su tipo de referencia."""

    tipo_aplicado: Decimal
    tipo_referencia: Decimal

    @property
    def diferencial_pb(self) -> Decimal:
        # El tipo se expresa como unidades de destino por unidad de origen:
        # un tipo aplicado menor que el de referencia perjudica al cliente.
        if self.tipo_referencia == 0:
            return Decimal(0)
        return (
            (self.tipo_referencia - self.tipo_aplicado) / self.tipo_referencia
        ) * Decimal(10_000)


@dataclass
class Ruta:
    nombre: str
    comision_envio: Decimal
    tramos: list[Tramo]
    comisiones_intermedias: list[Decimal] = field(default_factory=list)
    comision_retiro: Decimal = Decimal(0)

    def recibido(self, importe: Decimal) -> Decimal:
        valor = importe - self.comision_envio
        for indice, tramo in enumerate(self.tramos):
            valor = valor * tramo.tipo_aplicado
            if indice < len(self.comisiones_intermedias):
                valor -= self.comisiones_intermedias[indice]
        return valor - self.comision_retiro

    def sin_coste(self, importe: Decimal) -> Decimal:
        valor = importe
        for tramo in self.tramos:
            valor = valor * tramo.tipo_referencia
        return valor

    def coste_total(self, importe: Decimal) -> Decimal:
        referencia = self.sin_coste(importe)
        if referencia == 0:
            return Decimal(0)
        return (referencia - self.recibido(importe)) / referencia

    def diferencial_compuesto_pb(self) -> Decimal:
        """Los diferenciales de un tipo cruzado se COMPONEN, no se suman."""
        acumulado = Decimal(1)
        for tramo in self.tramos:
            acumulado *= Decimal(1) - tramo.diferencial_pb / Decimal(10_000)
        return (Decimal(1) - acumulado) * Decimal(10_000)

    def descomponer(self, importe: Decimal) -> dict[str, Decimal]:
        """Reparte el coste entre comisiones visibles y diferencial."""
        referencia = self.sin_coste(importe)
        recibido_sin_diferencial = Ruta(
            nombre=self.nombre,
            comision_envio=self.comision_envio,
            tramos=[Tramo(t.tipo_referencia, t.tipo_referencia) for t in self.tramos],
            comisiones_intermedias=self.comisiones_intermedias,
            comision_retiro=self.comision_retiro,
        ).recibido(importe)

        coste_comisiones = referencia - recibido_sin_diferencial
        coste_total = referencia - self.recibido(importe)
        return {
            "coste_total": coste_total,
            "comisiones_visibles": coste_comisiones,
            "diferencial": coste_total - coste_comisiones,
            "porcentaje_invisible": (
                (coste_total - coste_comisiones) / coste_total * Decimal(100)
                if coste_total
                else Decimal(0)
            ),
        }

    def aviso_transparencia(self, importe: Decimal) -> str | None:
        """Avisa cuando la comision explicita no llega a la mitad del coste."""
        partes = self.descomponer(importe)
        if partes["porcentaje_invisible"] > Decimal(50):
            return (
                "Mas de la mitad del coste de esta ruta esta en el tipo de cambio, "
                "no en la comision."
            )
        return None


def comparar(rutas: list[Ruta], importes: list[Decimal]) -> list[dict[str, object]]:
    """Precio efectivo por importe: el ganador puede cambiar por tramo."""
    filas = []
    for importe in importes:
        costes = {r.nombre: r.coste_total(importe) for r in rutas}
        ganadora = min(costes, key=lambda nombre: costes[nombre])
        filas.append({"importe": importe, "costes": costes, "ganadora": ganadora})
    return filas
