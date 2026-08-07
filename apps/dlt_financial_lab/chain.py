"""Cadena de bloques DIDACTICA.

Su razon de ser es demostrar el resultado incomodo del laboratorio 1: el
encadenamiento hace detectable manipular SIN recalcular, y no hace nada contra
recalcular todo. La inmutabilidad la dan el consenso y el coste de rehacer.

No es segura, no es eficiente y no debe usarse para nada real.
"""

from __future__ import annotations

import hashlib
import time
from dataclasses import dataclass, field

from .crypto import Par, firmar, resumen_hex, verificar
from .merkle import ArbolMerkle


class TransaccionInvalida(Exception):
    """La transaccion no pasa la validacion del protocolo."""


@dataclass
class Transaccion:
    origen: str
    destino: str
    importe: int
    orden: int
    firma: bytes = b""

    def cuerpo(self) -> bytes:
        return f"{self.origen}|{self.destino}|{self.importe}|{self.orden}".encode()

    def firmar_con(self, par: Par) -> "Transaccion":
        self.firma = firmar(par, self.cuerpo())
        return self


@dataclass
class Bloque:
    indice: int
    resumen_anterior: str
    transacciones: list[Transaccion] = field(default_factory=list)
    marca: float = field(default_factory=time.time)
    nonce: int = 0

    def raiz_merkle(self) -> str:
        arbol = ArbolMerkle()
        for posicion, tx in enumerate(self.transacciones):
            arbol.agregar(f"{posicion:06d}", tx.importe)
        return arbol.raiz().hex()

    def resumen(self) -> str:
        contenido = (
            f"{self.indice}|{self.resumen_anterior}|{self.raiz_merkle()}"
            f"|{self.marca:.0f}|{self.nonce}"
        )
        return resumen_hex(contenido.encode())


@dataclass
class Cadena:
    dificultad: int = 0
    bloques: list[Bloque] = field(default_factory=list)
    saldos: dict[str, int] = field(default_factory=dict)
    ordenes: dict[str, int] = field(default_factory=dict)
    claves: dict[str, Par] = field(default_factory=dict)
    instantaneas: dict[int, dict[str, int]] = field(default_factory=dict)
    cada: int = 10

    def __post_init__(self) -> None:
        if not self.bloques:
            self.bloques.append(Bloque(0, "0" * 64))

    # --------------------------------------------------------------- cuentas

    def acreditar(self, cuenta: str, importe: int) -> None:
        self.saldos[cuenta] = self.saldos.get(cuenta, 0) + importe

    def registrar_clave(self, cuenta: str, par: Par) -> None:
        self.claves[cuenta] = par

    # ---------------------------------------------------------- transacciones

    def validar_transaccion(self, tx: Transaccion) -> None:
        par = self.claves.get(tx.origen)
        if par is None or not verificar(par, tx.cuerpo(), tx.firma):
            raise TransaccionInvalida("firma invalida")
        if tx.importe <= 0:
            raise TransaccionInvalida("importe no positivo")
        if self.saldos.get(tx.origen, 0) < tx.importe:
            raise TransaccionInvalida("saldo insuficiente")
        # Sin esta comprobacion, la misma transaccion firmada se reenvia y se
        # ejecuta dos veces. Es la idempotencia resuelta en el protocolo.
        esperado = self.ordenes.get(tx.origen, 0)
        if tx.orden != esperado:
            raise TransaccionInvalida(
                f"orden {tx.orden}, se esperaba {esperado}"
            )

    def aplicar(self, tx: Transaccion) -> None:
        self.validar_transaccion(tx)
        self.saldos[tx.origen] -= tx.importe
        self.acreditar(tx.destino, tx.importe)
        self.ordenes[tx.origen] = tx.orden + 1

    # ------------------------------------------------------------- bloques

    def _minar(self, bloque: Bloque) -> Bloque:
        objetivo = "0" * self.dificultad
        while not bloque.resumen().startswith(objetivo):
            bloque.nonce += 1
        return bloque

    def anadir_bloque(self, transacciones: list[Transaccion]) -> Bloque:
        for tx in transacciones:
            self.aplicar(tx)
        bloque = Bloque(
            indice=len(self.bloques),
            resumen_anterior=self.bloques[-1].resumen(),
            transacciones=transacciones,
        )
        self._minar(bloque)
        self.bloques.append(bloque)
        if bloque.indice % self.cada == 0:
            self.instantaneas[bloque.indice] = dict(self.saldos)
        return bloque

    # ------------------------------------------------------------ validacion

    def validar(self) -> bool:
        objetivo = "0" * self.dificultad
        for i in range(1, len(self.bloques)):
            actual, anterior = self.bloques[i], self.bloques[i - 1]
            if actual.resumen_anterior != anterior.resumen():
                return False
            if self.dificultad and not actual.resumen().startswith(objetivo):
                return False
        return True

    def recalcular_desde(self, indice: int) -> float:
        """Reescribe la cadena desde `indice`. Devuelve el tiempo empleado.

        Que esto funcione es el punto del laboratorio 1: la cadena vuelve a
        validar. Lo unico que lo impide en una red real es el coste de rehacer
        y que otros conserven la version original.
        """
        inicio = time.perf_counter()
        for i in range(indice, len(self.bloques)):
            if i > 0:
                self.bloques[i].resumen_anterior = self.bloques[i - 1].resumen()
            self.bloques[i].nonce = 0
            self._minar(self.bloques[i])
        return time.perf_counter() - inicio

    def estado_en(self, indice: int) -> dict[str, int]:
        """Reconstruye el estado con la instantanea mas cercana."""
        base = max((k for k in self.instantaneas if k <= indice), default=None)
        if base is None:
            estado: dict[str, int] = {}
            desde = 1
        else:
            estado = dict(self.instantaneas[base])
            desde = base + 1
        for bloque in self.bloques[desde : indice + 1]:
            for tx in bloque.transacciones:
                estado[tx.origen] = estado.get(tx.origen, 0) - tx.importe
                estado[tx.destino] = estado.get(tx.destino, 0) + tx.importe
        return estado
