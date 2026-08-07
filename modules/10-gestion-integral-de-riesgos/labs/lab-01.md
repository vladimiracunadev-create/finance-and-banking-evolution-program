# Laboratorio 1: Marco integral de riesgos

## Propósito

Separar la pérdida esperada de la inesperada en una cartera y **determinar qué se provisiona y qué se capitaliza**.

Es el primer laboratorio de la parte y el que instala su distinción fundacional. Sin ella, las quince clases siguientes se estudian sin saber para qué sirve cada medida.

## Escenario

Una cartera de 500 operaciones con probabilidad de incumplimiento heterogénea y correlación entre deudores.

## Datos

La cartera con sus tres parámetros por operación y la matriz de correlación por sector.

## Supuestos del ejercicio

- La severidad media es del 45 %.
- La correlación intrasectorial se entrega como dato.
- El nivel de solvencia objetivo es el percentil 99,9.

## Pasos

1. Calcula la pérdida esperada de cada operación y de la cartera.
2. Simula la distribución de pérdidas de la cartera con la correlación dada.
3. Obtén el percentil 99,9 de la distribución.
4. Calcula la pérdida inesperada como diferencia entre ese percentil y la esperada.
5. Determina cuánto se provisiona y cuánto se capitaliza.
6. Repite con correlación cero y compara la pérdida inesperada.
7. Explica por qué la correlación no afecta a la esperada y sí a la inesperada.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | La pérdida esperada está calculada | Por operación y agregada |
| 2 | La distribución está simulada | Con la correlación |
| 3 | El percentil está obtenido | 99,9 |
| 4 | Provisión y capital están separados | Con su importe |
| 5 | El efecto de la correlación está aislado | Comparando ambos casos |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Cubrir la inesperada con provisiones | Se cubre con capital |
| Sumar pérdidas esperadas individuales y llamarlo riesgo | Falta la cola |
| Simular sin correlación | Subestima la pérdida inesperada de forma grave |
| Confundir percentil con máximo | Por encima del percentil todavía hay cola |

## Entregables

- `solution.md` con la pérdida esperada e inesperada.
- La distribución simulada con su percentil.
- El reparto entre provisión y capital.
- La comparación con correlación cero.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Pérdida esperada | 20 |
| Distribución simulada | 25 |
| Percentil y pérdida inesperada | 25 |
| Reparto provisión-capital | 15 |
| Efecto de la correlación | 15 |
