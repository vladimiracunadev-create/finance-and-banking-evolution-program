# Laboratorio 3: Financiamiento ilícito

## Propósito

Calibrar un sistema de monitoreo y **medir sus dos errores a la vez**, porque bajar uno sube el otro.

El laboratorio 2 construyó el programa. Este entra en la obligación cuyo incumplimiento tiene las consecuencias mayores, y en su tensión propia entre integridad e inclusión.

## Escenario

Un sistema de monitoreo con 4 800 alertas mensuales, de las que se reportan 62, y un umbral que nadie ha revisado en tres años.

## Datos

La muestra de alertas con su resultado y las operaciones no alertadas que resultaron sospechosas.

## Supuestos del ejercicio

- Los casos confirmados como sospechosos se entregan etiquetados.
- El costo de analizar una alerta se entrega como dato.
- El segmento objetivo del banco incluye población con poco historial.

## Pasos

1. Calcula la precisión y la exhaustividad del sistema actual.
2. Estima el costo anual de analizar los falsos positivos.
3. Mueve el umbral en cinco puntos y recalcula ambas medidas.
4. Determina el umbral que minimiza el costo total, incluyendo el de no detectar.
5. Evalúa el efecto de cada umbral sobre la tasa de rechazo del segmento objetivo.
6. Aplica el enfoque basado en riesgo: dónde concentrar el esfuerzo.
7. Documenta el análisis de una alerta cerrada sin reporte, con su fundamento.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Precisión y exhaustividad están calculadas | Del sistema actual |
| 2 | El costo de los falsos positivos está estimado | Anual |
| 3 | Los cinco umbrales están evaluados | Con ambas medidas |
| 4 | El umbral óptimo está determinado | Por costo total |
| 5 | El efecto sobre el segmento está medido | Con su tasa de rechazo |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Optimizar solo la exhaustividad | Genera un volumen de alertas inanalizable |
| Optimizar solo la precisión | Deja pasar lo que hay que detectar |
| No medir el efecto sobre el segmento | Un programa estricto excluye sin reducir el delito |
| Cerrar alertas sin documentar | El análisis documentado vale tanto como el reporte |

## Entregables

- `solution.md` con precisión y exhaustividad de los cinco umbrales.
- El costo total y el umbral que lo minimiza.
- El efecto sobre el segmento objetivo.
- El análisis documentado de una alerta cerrada.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Dos medidas calculadas | 25 |
| Costo de falsos positivos | 20 |
| Umbral óptimo | 25 |
| Efecto sobre el segmento | 20 |
| Análisis documentado | 10 |
