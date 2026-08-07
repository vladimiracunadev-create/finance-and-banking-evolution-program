# Laboratorio 3: Interés compuesto

## Propósito

Construir la misma serie con y sin capitalización y **medir dónde empieza a importar la diferencia**.

El laboratorio 2 midió cambios entre periodos. Este pone precio al tiempo, y su valor está en ver que la brecha es despreciable al principio, que es justo cuando se toman las decisiones que la producen.

## Escenario

Un capital de 1 000 000 al 2 % mensual durante 60 meses, y una deuda de tarjeta de 800 000 al 3,2 % mensual pagando el mínimo del 5 %.

## Datos

Los dos casos, con su tabla mes a mes.

## Supuestos del ejercicio

- El pago mínimo se calcula sobre el saldo del periodo.
- No hay consumos nuevos en la tarjeta.
- El capital no recibe aportes adicionales.

## Pasos

1. Construye la tabla mes a mes del capital, con y sin capitalización.
2. Marca el mes en que la brecha supera el 5 % y el mes en que supera el 25 %.
3. Aplica la regla del 72 y compárala con el resultado exacto.
4. Construye la tabla de la deuda pagando solo el mínimo.
5. Calcula cuántos meses tarda en pagarse y cuánto se paga en total.
6. Explica en tres frases por qué el mismo mecanismo construye y destruye.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Las dos series están completas | Mes a mes, 60 filas |
| 2 | Los dos meses de brecha se identifican | 5 % y 25 % |
| 3 | La regla del 72 se contrasta | Con su error respecto del exacto |
| 4 | La deuda se paga y se cuentan los meses | Tabla hasta saldo cero |
| 5 | El total pagado se compara con el capital | En pesos y en veces |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Aplicar la tasa anual a un periodo mensual | El error más caro de la parte |
| Detener la tabla antes de saldo cero | El total pagado queda incompleto |
| Confundir pago mínimo con amortización | El mínimo cubre casi solo interés |
| Usar la regla del 72 como exacta | Es una aproximación y su error crece con la tasa |

## Entregables

- `solution.md` con las dos tablas y la brecha marcada.
- El contraste entre la regla del 72 y el cálculo exacto.
- El total pagado por la deuda y su relación con el capital.
- Las tres frases de conclusión.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Series completas | 25 |
| Brecha identificada | 20 |
| Regla del 72 contrastada | 15 |
| Tabla de deuda hasta cero | 25 |
| Conclusión | 15 |
