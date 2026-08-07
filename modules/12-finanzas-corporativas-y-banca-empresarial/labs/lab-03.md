# Laboratorio 3: Costo de capital

## Propósito

Calcular el costo promedio ponderado con valores de mercado y **comprobar cuánto cambia usando valores contables**.

El laboratorio 2 evaluó un proyecto con una tasa dada. Este construye esa tasa, que es la decisión que más mueve cualquier valoración y la que menos se justifica por escrito.

## Escenario

Una empresa con deuda cotizada, patrimonio en bolsa y valores contables muy distintos de los de mercado.

## Datos

El balance, la cotización de la acción, el precio de la deuda y los datos de mercado.

## Supuestos del ejercicio

- La tasa impositiva efectiva se entrega como dato.
- La beta se estima con los últimos cinco años.
- La prima por riesgo de mercado se entrega con su fuente.

## Pasos

1. Calcula el costo de la deuda antes y después del escudo fiscal.
2. Estima el costo del patrimonio con el modelo entregado.
3. Calcula el costo promedio ponderado con valores de mercado.
4. Repítelo con valores contables y cuantifica la diferencia.
5. Evalúa el efecto de un cambio de estructura sobre el costo total.
6. Determina la estructura que minimiza el costo y contrástala con la del sector.
7. Recalcula el valor actual del proyecto del laboratorio 2 con esta tasa.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | El costo de la deuda está calculado | Antes y después del escudo |
| 2 | El costo del patrimonio está estimado | Con su método declarado |
| 3 | Las dos ponderaciones se comparan | Mercado y contable |
| 4 | La estructura óptima se contrasta con el sector | Con su diferencia |
| 5 | El proyecto se recalcula | Con la tasa obtenida |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Ponderar con valores contables | Puede cambiar la tasa en varios puntos |
| Olvidar el escudo fiscal | El costo de la deuda es después de impuestos |
| Estimar el costo del patrimonio sin declarar el método | Es la parte más discutible |
| Usar una tasa única para todos los proyectos | El riesgo del proyecto puede diferir del de la empresa |

## Entregables

- `solution.md` con los dos costos y las dos ponderaciones.
- La diferencia entre valores de mercado y contables.
- La estructura óptima contrastada con el sector.
- El proyecto del laboratorio 2 recalculado.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Costo de la deuda | 20 |
| Costo del patrimonio | 25 |
| Dos ponderaciones | 25 |
| Estructura óptima | 15 |
| Proyecto recalculado | 15 |
