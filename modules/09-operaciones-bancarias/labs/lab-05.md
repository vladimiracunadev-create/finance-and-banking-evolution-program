# Laboratorio 5: Operaciones internacionales

## Propósito

Reconstruir el costo total de un pago internacional y **encontrar dónde se pierde lo que el cliente no ve**.

El laboratorio 4 trató un medio de pago local. Este cruza la frontera, donde no hay infraestructura común y el costo real supera con holgura al cotizado.

## Escenario

Un pago de 40 000 unidades de moneda extranjera que atraviesa dos bancos intermediarios y llega con una deducción no anunciada.

## Datos

La cadena completa con las comisiones de cada tramo y el tipo aplicado.

## Supuestos del ejercicio

- El tipo de referencia del día se entrega como dato.
- Cada intermediario aplica su comisión sobre el importe que recibe.
- El banco ordenante cotizó una comisión fija al cliente.

## Pasos

1. Reconstruye el trayecto del pago tramo a tramo.
2. Calcula la deducción de cada intermediario.
3. Aísla el diferencial cambiario y exprésalo en puntos básicos.
4. Suma el costo total y compáralo con lo cotizado al cliente.
5. Determina qué proporción del costo total corresponde a cada fuente.
6. Calcula la posición de cambios del banco tras la operación.
7. Propón dos formas de reducir el costo total y cuantifica cada una.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | El trayecto está reconstruido | Tramo a tramo |
| 2 | Las deducciones están calculadas | De cada intermediario |
| 3 | El diferencial está aislado | En puntos básicos |
| 4 | El costo total se compara con lo cotizado | Con la brecha |
| 5 | Las dos propuestas están cuantificadas | En ahorro |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Comparar por la comisión cotizada | Es la menor de las tres fuentes de costo |
| No aislar el diferencial cambiario | Suele superar a todas las comisiones juntas |
| Olvidar los intermediarios | El ordenante no los elige y cobran igual |
| Ignorar la posición de cambios | La operación deja al banco expuesto |

## Entregables

- `solution.md` con el trayecto y las deducciones.
- El diferencial aislado en puntos básicos.
- El costo total frente a lo cotizado, con su reparto por fuente.
- Las dos propuestas de reducción cuantificadas.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Trayecto reconstruido | 25 |
| Deducciones calculadas | 20 |
| Diferencial aislado | 25 |
| Brecha con lo cotizado | 15 |
| Propuestas cuantificadas | 15 |
