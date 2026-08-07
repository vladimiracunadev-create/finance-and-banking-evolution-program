# Laboratorio 6: Proyecto: tablero de riesgos

## Propósito

Construir el tablero integrado y **someterlo a un escenario único para ver qué se activa a la vez**.

Es el último laboratorio de la parte y la antesala del proyecto. Su hallazgo es el de la clase 16: un banco puede cumplir todos sus límites por separado y no sobrevivir al escenario que los activa juntos.

## Escenario

Los quince riesgos de la parte, cada uno con su métrica y su límite, sobre el mismo banco.

## Datos

Las métricas actuales de los quince riesgos y sus límites vigentes.

## Supuestos del ejercicio

- Todos los límites están cumplidos en la situación actual.
- El escenario único es el diseñado en el laboratorio 5.
- Las acciones comprometidas de cada límite están declaradas.

## Pasos

1. Construye el tablero con las quince métricas, su límite y su holgura.
2. Comprueba que todas cumplen en la situación actual.
3. Aplica el escenario único del laboratorio 5 a las quince a la vez.
4. Identifica cuáles se activan y en qué orden temporal.
5. Detecta las interacciones: métricas que se deterioran por el deterioro de otra.
6. Verifica si las acciones comprometidas de dos límites son compatibles entre sí.
7. Propón el orden de escalamiento y quién decide en cada nivel.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | El tablero tiene las quince métricas | Con límite y holgura |
| 2 | Todas cumplen en la situación actual | Comprobado |
| 3 | Las que se activan están identificadas | Con su orden temporal |
| 4 | Las interacciones están detectadas | Con la métrica que las produce |
| 5 | La compatibilidad de acciones está verificada | Al menos dos pares |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Mirar las métricas por separado | Es lo que el laboratorio desmonta |
| Acciones comprometidas incompatibles | Dos límites que exigen lo contrario |
| No ordenar temporalmente | El orden decide qué se puede hacer |
| Tablero sin holgura | Cumplir no dice a qué distancia se está |

## Entregables

- `solution.md` con el tablero de quince métricas.
- Las que se activan bajo el escenario único, en orden.
- Las interacciones detectadas.
- El orden de escalamiento con su nivel de decisión.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Tablero completo | 25 |
| Escenario aplicado | 25 |
| Interacciones detectadas | 25 |
| Compatibilidad verificada | 15 |
| Escalamiento | 10 |
