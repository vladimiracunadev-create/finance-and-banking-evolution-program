"""Contrato de deposito en garantia, con y sin el defecto de reentrada.

El modulo permite ejecutar el ataque y su correccion. La diferencia entre las
dos versiones son dos lineas intercambiadas, y esa es toda la leccion.

`Escrow` simula la ejecucion sobre un registro: no reproduce el modelo de
ejecucion ni el coste de ninguna plataforma real.
"""

from __future__ import annotations

from dataclasses import dataclass, field


class EstadoIlegal(Exception):
    """Transicion que la maquina de estados no admite."""


class SinFondos(Exception):
    """No hay saldo que retirar."""


class ContratoDetenido(Exception):
    """El interruptor de emergencia esta activado."""


TRANSICIONES = {
    "creado": {"fondeado"},
    "fondeado": {"liberado", "en_disputa", "devuelto"},
    "en_disputa": {"liberado", "devuelto"},
    "liberado": set(),
    "devuelto": set(),
}


@dataclass
class Interruptor:
    """Solo DETIENE. No altera saldos, no transfiere, no revierte.

    Que solo pare es la decision importante: da capacidad de contener sin dar
    a nadie capacidad de mover fondos.
    """

    umbral: int = 2
    firmantes: set[str] = field(default_factory=set)
    activo: bool = False

    def firmar(self, quien: str) -> bool:
        self.firmantes.add(quien)
        if len(self.firmantes) >= self.umbral:
            self.activo = True
        return self.activo

    def reanudar(self, quien: str) -> None:
        self.firmantes.discard(quien)
        if len(self.firmantes) < self.umbral:
            self.activo = False


@dataclass
class Deposito:
    identificador: str
    importe: int
    estado: str = "creado"


@dataclass
class Escrow:
    """Deposito en garantia.

    `orden_correcto=False` reproduce el defecto de reentrada del laboratorio 5.
    """

    verificador: str
    orden_correcto: bool = True
    depositos: dict[str, Deposito] = field(default_factory=dict)
    saldos: dict[str, int] = field(default_factory=dict)
    interruptor: Interruptor = field(default_factory=Interruptor)
    _transferir_a = None

    # ------------------------------------------------------------- estados

    def _transitar(self, deposito: Deposito, destino: str) -> None:
        if destino not in TRANSICIONES[deposito.estado]:
            raise EstadoIlegal(f"{deposito.estado} -> {destino}")
        deposito.estado = destino

    def saldo_del_contrato(self) -> int:
        return sum(self.saldos.values())

    def comprobar_invariantes(self) -> None:
        activos = sum(
            d.importe for d in self.depositos.values() if d.estado == "fondeado"
        )
        if self.saldo_del_contrato() != activos + self._liberado_pendiente():
            raise AssertionError("el saldo no cuadra con los depositos activos")

    def _liberado_pendiente(self) -> int:
        return sum(
            v for k, v in self.saldos.items() if k.startswith("beneficiario:")
        )

    # ----------------------------------------------------------- operaciones

    def depositar(self, identificador: str, quien: str, importe: int) -> None:
        if self.interruptor.activo:
            raise ContratoDetenido()
        deposito = Deposito(identificador, importe)
        self.depositos[identificador] = deposito
        self._transitar(deposito, "fondeado")
        self.saldos[f"deposito:{identificador}"] = importe

    def confirmar(self, identificador: str, quien: str, beneficiario: str) -> None:
        if self.interruptor.activo:
            raise ContratoDetenido()
        # Control de acceso explicito: sin esta linea, cualquiera libera fondos.
        if quien != self.verificador:
            raise PermissionError("solo el verificador puede confirmar")
        deposito = self.depositos[identificador]
        self._transitar(deposito, "liberado")
        importe = self.saldos.pop(f"deposito:{identificador}")
        clave = f"beneficiario:{beneficiario}"
        self.saldos[clave] = self.saldos.get(clave, 0) + importe

    def acreditar_beneficiario(self, beneficiario: str, importe: int) -> None:
        """Solo para montar escenarios de prueba."""
        clave = f"beneficiario:{beneficiario}"
        self.saldos[clave] = self.saldos.get(clave, 0) + importe

    def registrar_receptor(self, receptor) -> None:
        self._transferir_a = receptor

    def retirar(self, beneficiario: str) -> int:
        if self.interruptor.activo:
            raise ContratoDetenido()
        clave = f"beneficiario:{beneficiario}"
        importe = self.saldos.get(clave, 0)
        if importe <= 0:
            raise SinFondos(beneficiario)

        if self.orden_correcto:
            # Estado ANTES de la llamada externa.
            self.saldos[clave] = 0
            self._transferir(beneficiario, importe)
        else:
            # DEFECTO: la llamada externa ocurre con el saldo aun sin poner
            # a cero, y el receptor puede volver a entrar.
            self._transferir(beneficiario, importe)
            self.saldos[clave] = 0
        return importe

    def _transferir(self, beneficiario: str, importe: int) -> None:
        if self._transferir_a is not None:
            self._transferir_a.recibir(importe)
