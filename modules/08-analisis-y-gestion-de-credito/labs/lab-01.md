# Laboratorio 1: Ciclo de vida del crédito

## Propósito

Rastrear un deterioro de cartera hacia atrás hasta su origen, y **comprobar que no está donde aparece el síntoma**.

Es el primer laboratorio de la parte y el que fija su tesis: la mora es el síntoma y la admisión es la causa, separadas por dieciocho meses.

## Escenario

Una cartera de consumo cuya mora a 90 días pasa del 2,1 % al 5,4 % en cuatro trimestres, con cosechas mensuales identificables.

## Datos

Las cosechas mensuales de 24 meses con su mora por antigüedad y las políticas vigentes en cada momento.

## Supuestos del ejercicio

- Las cosechas se siguen por su mes de originación, no por el mes de la mora.
- Los cambios de política están fechados.
- No hubo cambios macroeconómicos relevantes en el periodo.

## Pasos

1. Construye la matriz de cosechas por mes de originación y antigüedad.
2. Identifica las cosechas que se deterioran más que la media.
3. Ubica el mes de originación donde empieza el deterioro.
4. Contrasta ese mes con el calendario de cambios de política.
5. Determina qué decisión de admisión produjo el deterioro y cuándo se tomó.
6. Calcula cuántos meses pasaron entre la decisión y su primera señal visible.
7. Enumera qué indicador de la etapa de admisión lo habría anticipado.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | La matriz de cosechas está construida | Por originación y antigüedad |
| 2 | Las cosechas deterioradas están identificadas | Frente a la media |
| 3 | El mes de origen está ubicado | Concreto |
| 4 | Se contrasta con el cambio de política | Con su fecha |
| 5 | El rezago está calculado | En meses |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Analizar la mora por mes de observación | Mezcla cosechas y esconde el origen |
| Culpar a la cobranza | No puede arreglar lo que la admisión originó |
| Buscar causas macro sin descartar la política | Aquí no hubo cambio macro |
| No cuantificar el rezago | Es lo que explica por qué se detecta tarde |

## Entregables

- `solution.md` con la matriz de cosechas.
- El mes de originación donde empieza el deterioro.
- El cambio de política que lo produjo, con su fecha.
- El indicador de admisión que lo habría anticipado.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Matriz de cosechas | 30 |
| Cosechas deterioradas | 20 |
| Origen ubicado | 25 |
| Rezago calculado | 15 |
| Indicador anticipador | 10 |
