"""Escenario de crisis digital para el simulador OpenBank.

Extiende el simulador sin modificar `bank.py` ni su esquema: agrega tablas
propias (`crisis_reserves`, `crisis_state`) en la misma base SQLite y opera
sobre las cuentas existentes.

Idea: el banco tiene depositos de clientes (pasivos, `accounts.balance`) y una
reserva respaldada por activos (`crisis_reserves`). Un incidente retira activos
de la reserva sin autorizacion; los depositos de los clientes NO cambian, y por
eso el respaldo (reserva / depositos) cae por debajo de 100 %.

    respaldo = reserva_total / depositos_totales

Es un modelo pedagogico: no es software bancario real, no usa datos reales y no
implementa requisitos regulatorios, contables ni de seguridad completos.
"""

from __future__ import annotations

from dataclasses import dataclass

try:  # ejecucion como script (cli.py) o con apps/openbank_simulator en sys.path
    from bank import Bank, now
except ImportError:  # ejecucion como paquete
    from .bank import Bank, now  # type: ignore[no-redef]

SCHEMA = """
CREATE TABLE IF NOT EXISTS crisis_reserves (
  bucket TEXT PRIMARY KEY,
  amount REAL NOT NULL CHECK(amount >= 0)
);
CREATE TABLE IF NOT EXISTS crisis_state (
  key TEXT PRIMARY KEY,
  value TEXT NOT NULL
);
"""


class RetirosPausados(RuntimeError):
    """Los retiros estan pausados por decision de la gestion de crisis."""


class ReservaInsuficiente(RuntimeError):
    """La reserva liquida no alcanza para pagar el retiro."""


@dataclass(frozen=True)
class Foto:
    """Estado del banco en un instante: reservas, depositos y respaldo."""

    reserva_liquida: float
    reserva_no_liquida: float
    depositos: float

    @property
    def reserva_total(self) -> float:
        return self.reserva_liquida + self.reserva_no_liquida

    @property
    def respaldo(self) -> float:
        return self.reserva_total / self.depositos if self.depositos else 1.0

    @property
    def respaldo_disponible(self) -> float:
        return self.reserva_liquida / self.depositos if self.depositos else 1.0


class CrisisDigital:
    """Orquesta el escenario sobre una instancia de `Bank`."""

    def __init__(self, bank: Bank) -> None:
        self.bank = bank

    def inicializar(self, liquida: float, no_liquida: float) -> None:
        if liquida < 0 or no_liquida < 0:
            raise ValueError("las reservas no pueden ser negativas")
        self.bank.initialize()
        with self.bank.connect() as con:
            con.executescript(SCHEMA)
            con.execute("DELETE FROM crisis_reserves")
            con.executemany(
                "INSERT INTO crisis_reserves(bucket, amount) VALUES (?, ?)",
                [("liquid", liquida), ("non_liquid", no_liquida)],
            )
            con.execute(
                "INSERT OR REPLACE INTO crisis_state(key, value) VALUES ('paused', '0')"
            )

    # -- lectura -----------------------------------------------------------

    def foto(self) -> Foto:
        with self.bank.connect() as con:
            reservas = dict(
                con.execute("SELECT bucket, amount FROM crisis_reserves").fetchall()
            )
        return Foto(
            reserva_liquida=float(reservas.get("liquid", 0.0)),
            reserva_no_liquida=float(reservas.get("non_liquid", 0.0)),
            depositos=float(self.bank.summary()["deposits"]),
        )

    def pausado(self) -> bool:
        with self.bank.connect() as con:
            row = con.execute(
                "SELECT value FROM crisis_state WHERE key = 'paused'"
            ).fetchone()
        return bool(row) and row[0] == "1"

    # -- eventos del escenario --------------------------------------------

    def transferencia_no_autorizada(self, monto: float) -> float:
        """Retira activos liquidos de la reserva sin tocar los depositos."""
        if monto <= 0:
            raise ValueError("el monto debe ser positivo")
        with self.bank.connect() as con:
            liquida = con.execute(
                "SELECT amount FROM crisis_reserves WHERE bucket = 'liquid'"
            ).fetchone()[0]
            sustraido = min(monto, float(liquida))
            con.execute(
                "UPDATE crisis_reserves SET amount = amount - ? WHERE bucket = 'liquid'",
                (sustraido,),
            )
        return sustraido

    def pausar_retiros(self) -> None:
        self._fijar_pausa("1")

    def reanudar_retiros(self) -> None:
        self._fijar_pausa("0")

    def _fijar_pausa(self, valor: str) -> None:
        with self.bank.connect() as con:
            con.execute(
                "INSERT OR REPLACE INTO crisis_state(key, value) VALUES ('paused', ?)",
                (valor,),
            )

    def reponer(self, monto: float) -> None:
        """Aporte de capital propio a la reserva liquida."""
        if monto <= 0:
            raise ValueError("el monto debe ser positivo")
        with self.bank.connect() as con:
            con.execute(
                "UPDATE crisis_reserves SET amount = amount + ? WHERE bucket = 'liquid'",
                (monto,),
            )

    def retirar(self, account_id: int, monto: float) -> None:
        """Retiro de un cliente: baja su saldo y paga con reserva liquida."""
        if monto <= 0:
            raise ValueError("el monto debe ser positivo")
        if self.pausado():
            raise RetirosPausados("retiros pausados")
        with self.bank.connect() as con:
            fila = con.execute(
                "SELECT balance FROM accounts WHERE id = ?", (account_id,)
            ).fetchone()
            if fila is None:
                raise KeyError("Cuenta inexistente")
            saldo = float(fila["balance"])
            if saldo < monto:
                raise ValueError("Saldo insuficiente")
            liquida = float(
                con.execute(
                    "SELECT amount FROM crisis_reserves WHERE bucket = 'liquid'"
                ).fetchone()[0]
            )
            if liquida < monto:
                raise ReservaInsuficiente("la reserva liquida no alcanza")
            nuevo = saldo - monto
            con.execute("UPDATE accounts SET balance = ? WHERE id = ?", (nuevo, account_id))
            con.execute(
                "UPDATE crisis_reserves SET amount = amount - ? WHERE bucket = 'liquid'",
                (monto,),
            )
            con.execute(
                "INSERT INTO transactions(account_id, kind, amount, balance_after, "
                "reference, created_at) VALUES (?, 'withdrawal', ?, ?, 'crisis', ?)",
                (account_id, monto, nuevo, now()),
            )


def ejecutar_escenario(
    bank: Bank,
    depositos_por_cliente: float = 1_000.0,
    clientes: int = 10,
    perdida: float = 1_500.0,
    retiros_pct: float = 0.7,
    reposicion: float = 1_500.0,
) -> dict[str, object]:
    """Corre el escenario completo y devuelve las fotos de cada etapa.

    Etapas: normal -> incidente -> pausa y corrida bloqueada -> reposicion ->
    reapertura y retiros. Los importes estan en unidades del simulador (CLP).
    """
    crisis = CrisisDigital(bank)
    total = depositos_por_cliente * clientes
    crisis.inicializar(liquida=0.8 * total, no_liquida=0.2 * total)
    cuentas = []
    for i in range(clientes):
        cliente = bank.create_customer(f"Cliente {i + 1}")
        cuentas.append(bank.open_account(cliente, depositos_por_cliente))

    etapas: dict[str, object] = {"normal": crisis.foto()}
    sustraido = crisis.transferencia_no_autorizada(perdida)
    etapas["sustraido"] = sustraido
    etapas["incidente"] = crisis.foto()

    crisis.pausar_retiros()
    bloqueados = 0
    for cuenta in cuentas:
        try:
            crisis.retirar(cuenta, depositos_por_cliente * retiros_pct)
        except RetirosPausados:
            bloqueados += 1
    etapas["retiros_bloqueados"] = bloqueados

    crisis.reponer(reposicion)
    etapas["repuesto"] = crisis.foto()

    crisis.reanudar_retiros()
    pagados = fallidos = 0
    for cuenta in cuentas:
        try:
            crisis.retirar(cuenta, depositos_por_cliente * retiros_pct)
            pagados += 1
        except ReservaInsuficiente:
            fallidos += 1
    etapas["retiros_pagados"] = pagados
    etapas["retiros_fallidos"] = fallidos
    etapas["final"] = crisis.foto()
    return etapas
