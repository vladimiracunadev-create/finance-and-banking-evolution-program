from __future__ import annotations
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

SCHEMA = """
PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS customers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS accounts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  customer_id INTEGER NOT NULL REFERENCES customers(id),
  currency TEXT NOT NULL DEFAULT 'CLP',
  balance REAL NOT NULL DEFAULT 0 CHECK(balance >= 0),
  created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS transactions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  account_id INTEGER NOT NULL REFERENCES accounts(id),
  kind TEXT NOT NULL,
  amount REAL NOT NULL CHECK(amount > 0),
  balance_after REAL NOT NULL,
  reference TEXT,
  created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS loans (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  customer_id INTEGER NOT NULL REFERENCES customers(id),
  principal REAL NOT NULL CHECK(principal > 0),
  annual_rate REAL NOT NULL,
  months INTEGER NOT NULL CHECK(months > 0),
  status TEXT NOT NULL DEFAULT 'active',
  created_at TEXT NOT NULL
);
"""


def now() -> str:
    return datetime.now(timezone.utc).isoformat()

@dataclass
class Bank:
    db_path: Path

    def connect(self) -> sqlite3.Connection:
        con = sqlite3.connect(self.db_path)
        con.row_factory = sqlite3.Row
        con.execute("PRAGMA foreign_keys = ON")
        return con

    def initialize(self) -> None:
        with self.connect() as con:
            con.executescript(SCHEMA)

    def create_customer(self, name: str) -> int:
        if not name.strip():
            raise ValueError("El nombre es obligatorio")
        with self.connect() as con:
            cur = con.execute("INSERT INTO customers(name, created_at) VALUES (?, ?)", (name.strip(), now()))
            return int(cur.lastrowid)

    def open_account(self, customer_id: int, initial_deposit: float = 0.0) -> int:
        if initial_deposit < 0:
            raise ValueError("El depósito inicial no puede ser negativo")
        with self.connect() as con:
            cur = con.execute("INSERT INTO accounts(customer_id, balance, created_at) VALUES (?, ?, ?)", (customer_id, initial_deposit, now()))
            account_id = int(cur.lastrowid)
            if initial_deposit:
                con.execute("INSERT INTO transactions(account_id, kind, amount, balance_after, reference, created_at) VALUES (?, 'deposit', ?, ?, 'initial', ?)", (account_id, initial_deposit, initial_deposit, now()))
            return account_id

    def balance(self, account_id: int) -> float:
        with self.connect() as con:
            row = con.execute("SELECT balance FROM accounts WHERE id = ?", (account_id,)).fetchone()
            if row is None:
                raise KeyError("Cuenta inexistente")
            return float(row['balance'])

    def deposit(self, account_id: int, amount: float, reference: str = '') -> None:
        if amount <= 0:
            raise ValueError("El monto debe ser positivo")
        with self.connect() as con:
            row = con.execute("SELECT balance FROM accounts WHERE id = ?", (account_id,)).fetchone()
            if row is None:
                raise KeyError("Cuenta inexistente")
            new_balance = float(row['balance']) + amount
            con.execute("UPDATE accounts SET balance = ? WHERE id = ?", (new_balance, account_id))
            con.execute("INSERT INTO transactions(account_id, kind, amount, balance_after, reference, created_at) VALUES (?, 'deposit', ?, ?, ?, ?)", (account_id, amount, new_balance, reference, now()))

    def transfer(self, source_id: int, target_id: int, amount: float, reference: str = '') -> None:
        if source_id == target_id:
            raise ValueError("Las cuentas deben ser distintas")
        if amount <= 0:
            raise ValueError("El monto debe ser positivo")
        with self.connect() as con:
            source = con.execute("SELECT balance FROM accounts WHERE id = ?", (source_id,)).fetchone()
            target = con.execute("SELECT balance FROM accounts WHERE id = ?", (target_id,)).fetchone()
            if source is None or target is None:
                raise KeyError("Cuenta inexistente")
            if float(source['balance']) < amount:
                raise ValueError("Saldo insuficiente")
            source_balance = float(source['balance']) - amount
            target_balance = float(target['balance']) + amount
            con.execute("UPDATE accounts SET balance = ? WHERE id = ?", (source_balance, source_id))
            con.execute("UPDATE accounts SET balance = ? WHERE id = ?", (target_balance, target_id))
            stamp = now()
            con.execute("INSERT INTO transactions(account_id, kind, amount, balance_after, reference, created_at) VALUES (?, 'transfer_out', ?, ?, ?, ?)", (source_id, amount, source_balance, reference, stamp))
            con.execute("INSERT INTO transactions(account_id, kind, amount, balance_after, reference, created_at) VALUES (?, 'transfer_in', ?, ?, ?, ?)", (target_id, amount, target_balance, reference, stamp))

    def create_loan(self, customer_id: int, principal: float, annual_rate: float, months: int) -> int:
        if principal <= 0 or months <= 0 or annual_rate < 0:
            raise ValueError("Parámetros inválidos")
        with self.connect() as con:
            cur = con.execute("INSERT INTO loans(customer_id, principal, annual_rate, months, created_at) VALUES (?, ?, ?, ?, ?)", (customer_id, principal, annual_rate, months, now()))
            return int(cur.lastrowid)

    def summary(self) -> dict[str, float]:
        with self.connect() as con:
            customers = con.execute("SELECT COUNT(*) FROM customers").fetchone()[0]
            accounts = con.execute("SELECT COUNT(*) FROM accounts").fetchone()[0]
            deposits = con.execute("SELECT COALESCE(SUM(balance), 0) FROM accounts").fetchone()[0]
            loans = con.execute("SELECT COALESCE(SUM(principal), 0) FROM loans WHERE status='active'").fetchone()[0]
        return {'customers': customers, 'accounts': accounts, 'deposits': float(deposits), 'active_loans': float(loans)}
