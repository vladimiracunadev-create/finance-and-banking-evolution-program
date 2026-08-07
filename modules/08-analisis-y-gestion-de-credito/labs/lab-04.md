# Laboratorio 4: Scoring

## Propósito

Mover el punto de corte de un modelo y **encontrar el que maximiza el resultado ajustado por riesgo, no la aprobación ni la mora**.

El laboratorio 3 evaluó caso a caso. Este automatiza para volumen, y su decisión central no es técnica: dónde se pone el corte es una decisión de negocio con efecto medible.

## Escenario

Un modelo de scoring ya construido, con su distribución de puntajes y la mora observada por tramo.

## Datos

La tabla de puntajes con volumen, mora y margen por tramo.

## Supuestos del ejercicio

- El margen por operación aprobada se entrega como dato.
- La pérdida dado el incumplimiento es del 62 %.
- El costo de originación es fijo por solicitud evaluada.

## Pasos

1. Calcula la discriminación del modelo con la separación entre buenos y malos.
2. Evalúa la calibración comparando la mora predicha con la observada por tramo.
3. Calcula aprobación, mora y resultado para cinco puntos de corte distintos.
4. Encuentra el corte que maximiza el resultado ajustado por riesgo.
5. Compara ese corte con el que minimiza la mora y con el que maximiza el volumen.
6. Calcula el efecto de una deriva del 10 % en la población sobre el corte óptimo.
7. Define qué vigilarías mensualmente para detectar esa deriva.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | La discriminación está medida | Con su métrica |
| 2 | La calibración está evaluada | Predicha frente a observada |
| 3 | Los cinco cortes están calculados | Con sus tres cifras |
| 4 | El corte óptimo está identificado | Por resultado ajustado |
| 5 | Los tres criterios se comparan | Y dan cortes distintos |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Elegir el corte que minimiza la mora | Suele destruir el negocio |
| Confundir discriminación con calibración | Un modelo puede ordenar bien y predecir mal |
| No considerar el costo de originación | Se paga por cada solicitud, se apruebe o no |
| Fijar el corte y no vigilarlo | La población deriva y el corte deja de ser óptimo |

## Entregables

- `solution.md` con discriminación y calibración medidas.
- Los cinco cortes con sus tres cifras.
- El corte óptimo y su comparación con los otros dos criterios.
- El plan de vigilancia mensual de la deriva.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Discriminación y calibración | 25 |
| Cinco cortes | 25 |
| Corte óptimo | 20 |
| Comparación de criterios | 15 |
| Vigilancia de deriva | 15 |
