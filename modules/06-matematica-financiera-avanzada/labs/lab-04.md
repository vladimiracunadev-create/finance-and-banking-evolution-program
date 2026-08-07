# Laboratorio 4: Tasa interna de retorno

## Propósito

Ordenar cuatro proyectos por tasa interna y por valor actual neto, y **explicar por qué los dos órdenes no coinciden**.

El laboratorio 3 estructuró un crédito. Este decide entre proyectos, y su valor está en los tres problemas del indicador más comunicado y peor entendido.

## Escenario

Cuatro proyectos de escalas distintas, uno con flujos que cambian de signo dos veces y otro con recuperación muy tardía.

## Datos

Los cuatro flujos completos y el costo de capital.

## Supuestos del ejercicio

- El costo de capital es del 11 % anual.
- Los proyectos son mutuamente excluyentes.
- La tasa de reinversión realista es del 7 %.

## Pasos

1. Calcula el valor actual neto de los cuatro al costo de capital.
2. Calcula la tasa interna de cada uno por iteración.
3. Identifica el proyecto con más de una tasa interna y explica por qué ocurre.
4. Ordena por ambos criterios y explica la discrepancia con el problema de escala.
5. Calcula la tasa interna modificada con la tasa de reinversión realista.
6. Encuentra la tasa de Fisher entre los dos proyectos que se cruzan.
7. Recomienda uno y justifica con el criterio que corresponde.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los cuatro valores actuales están calculados | Al costo de capital |
| 2 | Las tasas internas están calculadas | Por iteración |
| 3 | El caso de tasa múltiple está identificado | Con su causa |
| 4 | La discrepancia de órdenes se explica | Por escala o por perfil temporal |
| 5 | La tasa modificada corrige el supuesto | Con la tasa realista |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Ordenar por tasa interna | Falla con escalas distintas |
| Ignorar los cambios de signo | Producen más de una solución |
| Suponer reinversión a la propia tasa interna | Casi nunca es realista |
| No calcular la tasa de Fisher | Es donde el orden se invierte |

## Entregables

- `solution.md` con los dos órdenes y su discrepancia explicada.
- El proyecto con tasa múltiple y su causa.
- La tasa interna modificada de los cuatro.
- La recomendación con su criterio justificado.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Valores actuales | 20 |
| Tasas internas | 20 |
| Tasa múltiple identificada | 20 |
| Discrepancia explicada | 25 |
| Tasa modificada | 15 |
