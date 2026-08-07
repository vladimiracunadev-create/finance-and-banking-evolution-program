"""Dos registros y su divergencia: espejo frente a bloqueo de origen.

La clase 2 sostiene que un espejo NUNCA permite liquidacion atomica, porque el
movimiento del valor solo es valido cuando lo confirma el registro oficial, y ese
intervalo es justo el riesgo que la atomicidad pretendia eliminar.

Este modulo implementa las dos configuraciones para poder comprobarlo.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Configuracion(str, Enum):
    ESPEJO = "espejo"
    BLOQUEO_DE_ORIGEN = "bloqueo_de_origen"
    SIN_DECIDIR = "sin_decidir"


class Causa(str, Enum):
    """Las seis causas de divergencia de la clase 2.

    Las dos ultimas vienen de fuera del sistema y ninguna automatizacion las
    resuelve: por eso hay que designar una autoridad de resolucion.
    """

    FALLO_DE_PROPAGACION = "fallo_de_propagacion"
    ORDEN_DISTINTO = "orden_distinto"
    ERROR_OPERATIVO = "error_operativo"
    ATAQUE = "ataque"
    EVENTO_CORPORATIVO = "evento_corporativo"
    DECISION_JUDICIAL = "decision_judicial"


VIENEN_DE_FUERA = (Causa.EVENTO_CORPORATIVO, Causa.DECISION_JUDICIAL)


class SinAutoridadDeResolucion(RuntimeError):
    """No se puede resolver una divergencia sin designar quien decide."""


class SaldoCongelado(RuntimeError):
    """Un saldo en divergencia no admite movimientos hasta resolverse."""


@dataclass
class Libro:
    """Un registro de saldos por titular."""

    nombre: str
    saldos: dict[str, int] = field(default_factory=dict)
    congelados: set[str] = field(default_factory=set)

    def saldo(self, titular: str) -> int:
        return self.saldos.get(titular, 0)

    def acreditar(self, titular: str, unidades: int) -> None:
        if titular in self.congelados:
            raise SaldoCongelado(f"{titular} esta congelado en {self.nombre}")
        self.saldos[titular] = self.saldo(titular) + unidades

    def transferir(self, origen: str, destino: str, unidades: int) -> None:
        for titular in (origen, destino):
            if titular in self.congelados:
                raise SaldoCongelado(f"{titular} esta congelado en {self.nombre}")
        if self.saldo(origen) < unidades:
            raise ValueError(f"saldo insuficiente de {origen} en {self.nombre}")
        self.saldos[origen] -= unidades
        self.saldos[destino] = self.saldo(destino) + unidades


@dataclass(frozen=True)
class Divergencia:
    titular: str
    saldo_oficial: int
    saldo_token: int
    causa: Causa

    @property
    def viene_de_fuera(self) -> bool:
        return self.causa in VIENEN_DE_FUERA


@dataclass
class Emisor:
    """Coordina el registro oficial y el registro del token.

    En configuracion ESPEJO ambos registros mantienen saldo simultaneo y hay que
    conciliarlos. En BLOQUEO_DE_ORIGEN solo uno esta operativo para cada saldo,
    de modo que la divergencia estructural no puede existir.
    """

    configuracion: Configuracion
    oficial: Libro = field(default_factory=lambda: Libro("oficial"))
    token: Libro = field(default_factory=lambda: Libro("token"))
    autoridad_de_resolucion: str | None = None
    bloqueado: dict[str, int] = field(default_factory=dict)
    incidencias: list[Divergencia] = field(default_factory=list)

    # ------------------------------------------------------------------
    # Alta de posiciones
    # ------------------------------------------------------------------

    def emitir(self, titular: str, unidades: int) -> None:
        self.oficial.acreditar(titular, unidades)
        if self.configuracion is Configuracion.ESPEJO:
            self.token.acreditar(titular, unidades)

    def bloquear_y_representar(self, titular: str, unidades: int) -> None:
        """Inmoviliza en el oficial y emite la representacion en el token."""
        if self.configuracion is not Configuracion.BLOQUEO_DE_ORIGEN:
            raise ValueError("el bloqueo de origen exige esa configuracion")
        if self.oficial.saldo(titular) < unidades:
            raise ValueError("saldo insuficiente para bloquear")
        self.oficial.saldos[titular] -= unidades
        self.bloqueado[titular] = self.bloqueado.get(titular, 0) + unidades
        self.token.acreditar(titular, unidades)

    def rescatar(self, titular: str, unidades: int) -> None:
        """Destruye el token y libera el saldo en el registro oficial."""
        if self.token.saldo(titular) < unidades:
            raise ValueError("no hay token suficiente para rescatar")
        if self.bloqueado.get(titular, 0) < unidades:
            raise ValueError("no hay saldo bloqueado suficiente")
        self.token.saldos[titular] -= unidades
        self.bloqueado[titular] -= unidades
        self.oficial.acreditar(titular, unidades)

    # ------------------------------------------------------------------
    # La propiedad que decide todo
    # ------------------------------------------------------------------

    @property
    def permite_atomicidad(self) -> bool:
        """Solo el bloqueo de origen la permite.

        Con un espejo, la transferencia del token no es valida hasta que la
        confirma el oficial: existe un intervalo, y por tanto un estado
        intermedio observable.
        """
        return self.configuracion is Configuracion.BLOQUEO_DE_ORIGEN

    # ------------------------------------------------------------------
    # Divergencia
    # ------------------------------------------------------------------

    def provocar_divergencia(self, titular: str, causa: Causa, delta: int) -> None:
        """Introduce una diferencia entre ambos registros, para el laboratorio."""
        if self.configuracion is not Configuracion.ESPEJO:
            raise ValueError(
                "sin dos registros operativos no hay divergencia estructural"
            )
        self.token.saldos[titular] = self.token.saldo(titular) + delta

    def conciliar(self, causas: dict[str, Causa] | None = None) -> list[Divergencia]:
        """Compara TODOS los saldos, no una muestra.

        Una divergencia no vista es una perdida, y por eso el muestreo no sirve
        aqui (clase 2).
        """
        causas = causas or {}
        titulares = set(self.oficial.saldos) | set(self.token.saldos)
        encontradas: list[Divergencia] = []
        for titular in sorted(titulares):
            oficial = self.oficial.saldo(titular)
            token = self.token.saldo(titular)
            if oficial != token:
                encontradas.append(
                    Divergencia(
                        titular,
                        oficial,
                        token,
                        causas.get(titular, Causa.FALLO_DE_PROPAGACION),
                    )
                )
        self.incidencias.extend(encontradas)
        return encontradas

    def congelar(self, titular: str) -> None:
        """Congela en AMBOS registros: congelar uno solo agrava el problema."""
        self.oficial.congelados.add(titular)
        self.token.congelados.add(titular)

    def resolver(self, titular: str, saldo_correcto: int) -> None:
        """Corrige el registro equivocado y descongela.

        Nunca se «revierte» el registro correcto: se corrige el erroneo y se
        compensa al perjudicado (Parte 19, clase 13).
        """
        if self.autoridad_de_resolucion is None:
            raise SinAutoridadDeResolucion(
                "hay que designar quien decide antes de que ocurra"
            )
        self.oficial.saldos[titular] = saldo_correcto
        self.token.saldos[titular] = saldo_correcto
        self.oficial.congelados.discard(titular)
        self.token.congelados.discard(titular)


def coste_anual(
    conciliaciones_al_ano: int,
    coste_conciliacion: int,
    divergencias_al_ano: float,
    coste_resolucion: int,
) -> int:
    """Coste de mantener alineados dos registros (clase 2, pasos 3 y 4)."""
    return round(
        conciliaciones_al_ano * coste_conciliacion
        + divergencias_al_ano * coste_resolucion
    )


def ventana_protege(
    horas_de_conciliacion: float, horas_entre_operaciones: float
) -> bool:
    """La ventana debe ser menor que el intervalo entre dos operaciones.

    Si no lo es, la conciliacion no protege: solo documenta el dano.
    """
    return horas_de_conciliacion < horas_entre_operaciones
