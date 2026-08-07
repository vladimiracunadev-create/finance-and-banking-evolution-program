# Laboratorio 5: Fondos y ahorro previsional

## Propósito

Extraer las ocho variables de tres fichas y **comprobar que la rentabilidad histórica es la menos informativa de las ocho**.

El laboratorio 4 trató una deuda a veinte años. Este trata un ahorro al mismo plazo, donde el costo anual sobre el saldo pesa más que casi cualquier diferencia de rentabilidad.

## Escenario

Tres fondos con el mismo mandato, distinta remuneración y rentabilidades históricas que ordenan al revés que sus costos.

## Datos

Las tres fichas sintéticas completas.

## Supuestos del ejercicio

- El horizonte del ahorro es de veinte años.
- Las rentabilidades históricas son de los últimos tres años.
- La remuneración se cobra sobre el saldo, con independencia del resultado.

## Pasos

1. Extrae las ocho variables de cada ficha y tabúlalas.
2. Calcula el efecto de la remuneración sobre el saldo final a veinte años.
3. Compara ese efecto con la diferencia de rentabilidad histórica entre los tres.
4. Identifica el índice de referencia correcto de cada fondo y evalúa su desempeño contra él.
5. Ordena los tres fondos por costo total y por rentabilidad histórica, y compara los órdenes.
6. Recomienda uno y justifica la recomendación con las variables, no con la rentabilidad.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Las ocho variables están extraídas | De las tres fichas |
| 2 | El efecto de la remuneración está calculado | A veinte años |
| 3 | Se compara con la diferencia de rentabilidad | En la misma unidad |
| 4 | El desempeño se evalúa contra la referencia correcta | No contra otra |
| 5 | Los dos órdenes se comparan | Y no coinciden |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Elegir por rentabilidad histórica | Es la variable menos predictiva de las ocho |
| Comparar con la referencia equivocada | Un fondo mixto no se compara con un índice de acciones |
| Ignorar la remuneración | A veinte años pesa más que la habilidad del gestor |
| No mirar el error de seguimiento | Un fondo puede replicar mal su propio índice |

## Entregables

- `solution.md` con las ocho variables de los tres fondos.
- El efecto de la remuneración a veinte años.
- La evaluación contra la referencia correcta.
- La recomendación justificada por variables.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Ocho variables extraídas | 25 |
| Efecto de la remuneración | 25 |
| Referencia correcta | 20 |
| Órdenes comparados | 15 |
| Recomendación justificada | 15 |
