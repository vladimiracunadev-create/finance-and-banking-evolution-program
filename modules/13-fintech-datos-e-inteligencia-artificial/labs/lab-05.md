# Laboratorio 5: Detección de fraude

## Propósito

Calibrar el sistema minimizando el **costo total, incluida la fricción**, que casi nunca se mide.

El laboratorio 4 midió el efecto de una acción. Este calibra un sistema que se equivoca en las dos direcciones, y su hallazgo es que el costo de bloquear operaciones legítimas suele superar al del fraude.

## Escenario

Un sistema con 2,1 millones de operaciones mensuales, tasa de fraude del 0,04 % y tasa de bloqueo del 1,8 %.

## Datos

La distribución de puntajes con su resultado real y los costos unitarios.

## Supuestos del ejercicio

- El costo de un fraude consumado se entrega como dato.
- El costo de una operación legítima bloqueada incluye abandono estimado.
- El costo de revisión manual por operación derivada se entrega.

## Pasos

1. Calcula falsos positivos y falsos negativos en el umbral actual.
2. Cuantifica el costo del fraude no detectado.
3. Cuantifica el costo de la fricción: bloqueos legítimos y abandono.
4. Cuantifica el costo de la revisión manual.
5. Suma el costo total y repítelo para cinco umbrales distintos.
6. Determina el umbral que minimiza el costo total y compáralo con el actual.
7. Diseña la respuesta a un evento masivo, distinta de la gestión ordinaria.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los dos errores están cuantificados | En el umbral actual |
| 2 | Los tres costos están calculados | Fraude, fricción y revisión |
| 3 | Los cinco umbrales están evaluados | Con su costo total |
| 4 | El umbral óptimo está determinado | Y comparado con el actual |
| 5 | La respuesta al evento masivo está diseñada | Distinta de la ordinaria |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Optimizar solo el fraude | El costo de la fricción suele ser mayor |
| No medir el abandono | Es la parte grande del costo de bloquear |
| Ignorar el costo de la revisión manual | Crece con las derivaciones |
| Tratar un evento masivo como muchos casos | Exige otra respuesta |

## Entregables

- `solution.md` con los dos errores y los tres costos.
- Los cinco umbrales con su costo total.
- El umbral óptimo frente al actual.
- El protocolo de evento masivo.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Errores cuantificados | 20 |
| Tres costos | 30 |
| Cinco umbrales | 20 |
| Umbral óptimo | 20 |
| Evento masivo | 10 |
