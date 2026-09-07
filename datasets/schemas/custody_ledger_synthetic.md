# Diccionario: `custody_ledger_synthetic.csv`

- **Nombre:** mayor auxiliar de obligaciones de Custodia Andina Digital (sintético)
- **Ruta:** `datasets/synthetic/custody_ledger_synthetic.csv`
- **Filas:** 3
- **Origen:** caso determinístico redactado para la Parte 20; no deriva de datos reales
- **Licencia:** MIT, como el resto del repositorio
- **Fecha de generación:** 2026-09-07
- **Privacidad:** sin clientes, cuentas ni direcciones reales
- **Usado en:** Parte 20, laboratorio 9 y caso integrador de custodia

## Método de generación

Las tres filas se diseñaron para que la ecuación `apertura + entradas − salidas
± trading P/L − comisiones = cierre` cuadre en cada activo y totalice USD
7 000 000. La pérdida de trading de clientes está separada de las comisiones.

## Diccionario

| Campo | Tipo | Significado | NO significa |
|---|---|---|---|
| `entry_id` | cadena | Identificador sintético único | No identifica a un cliente |
| `account_scope` | enumerado | Naturaleza de la cuenta | No acredita propiedad por sí solo |
| `asset` | enumerado | Activo de referencia | No es una recomendación |
| `opening_balance_usd` | entero | Saldo inicial equivalente | No es cotización actual |
| `inflows_usd` | entero | Entradas del período | No todas son depósitos bancarios |
| `outflows_usd` | entero | Salidas del período | No incluye comisiones |
| `trading_pl_usd` | entero | Resultado realizado atribuible | No es saldo disponible |
| `fees_usd` | entero | Comisiones cargadas | No incluye pérdidas de mercado |
| `closing_balance_usd` | entero | Obligación final registrada | No prueba que exista el activo |
| `valuation_currency` | cadena | Unidad común de presentación | No convierte el activo en efectivo |

## Supuestos

- Los equivalentes USD usan una única hora de valoración sintética.
- Todas las operaciones del período están registradas y no existen impuestos.
- Un cierre correcto del mayor prueba integridad aritmética, no reservas.

## Calidad

Completitud y unicidad de `entry_id`: 100 %. Las tres ecuaciones cierran sin
diferencia y la suma reproduce el pasivo de clientes del caso.

## Limitaciones

- Tres activos y un período no representan una institución real.
- No contiene submayor por cliente ni prueba de titularidad.
- No sirve para valorar, invertir ni operar.
