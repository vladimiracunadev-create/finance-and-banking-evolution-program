# Diccionario: `custody_trading_synthetic.csv`

- **Nombre:** operaciones de trading de Custodia Andina Digital (sintético)
- **Ruta:** `datasets/synthetic/custody_trading_synthetic.csv`
- **Filas:** 4
- **Origen:** caso determinístico redactado para la Parte 20
- **Licencia:** CC BY-NC-SA 4.0; ver `DATA_LICENSES.md`
- **Fecha de generación:** 2026-09-07
- **Privacidad:** sin órdenes, cuentas ni contrapartes reales
- **Usado en:** Parte 20, laboratorio 9 y caso integrador

## Método de generación

Se incluyeron spot, margin, futures y derivatives para separar libro propio de
libro de clientes. Las dos operaciones de clientes se marcan como no autorizadas
y explican USD 150 000 del movimiento del mayor.

## Diccionario

| Campo | Tipo | Significado | NO significa |
|---|---|---|---|
| `trade_id` | cadena | Identificador sintético único | No es una orden real |
| `instrument` | enumerado | Spot, margin, futures o derivatives | No describe una estrategia recomendable |
| `book` | enumerado | Libro propio o de clientes | No autoriza usar activos de clientes |
| `notional_usd` | entero | Exposición nocional | No es la pérdida máxima |
| `realized_pl_usd` | entero | Ganancia o pérdida realizada | No incluye todo el riesgo abierto |
| `liability_created_usd` | entero | Obligación adicional creada | No es colateral |
| `collateral_encumbered_usd` | entero | Colateral inmovilizado | No está disponible para retiros |
| `authorized` | booleano | Existencia de mandato previo en el caso | No valida legalidad ni conveniencia |

## Supuestos

- Los P/L son realizados y se expresan en USD.
- Un instrumento apalancado agrega riesgo de contraparte y liquidez.
- Una operación no autorizada sobre el libro de clientes agrega custodia y fraude.

## Calidad

Completitud y unicidad de `trade_id`: 100 %. Están presentes los cuatro tipos
exigidos por el caso.

## Limitaciones

- No modela margen de variación, liquidación parcial ni netting jurídico.
- Los resultados no son escenarios de precio ni datos observados.
- No permite ejecutar operaciones.
