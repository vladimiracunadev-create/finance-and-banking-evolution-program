# Laboratorio 6: Detección de conducta anómala

## Propósito

Calibrar una vigilancia y demostrar que **decidir con el coste medio invierte la conclusión**.

El laboratorio anterior gestionó un riesgo que no se puede eliminar; este calibra la detección de uno que sí se puede medir. El hallazgo es un error de razonamiento que aparece en casi todos los comités: comparar el coste marginal de un indicador nuevo con el coste medio del sistema actual, en vez de con el valor de los casos que detecta.

## Escenario

Una plataforma con 412 000 operaciones al mes genera 3 640 alertas y confirma 44 casos, mientras 62 ocurrieron de verdad. Hay que decidir si añadir un indicador.

## Contexto

La clase 11 muestra que la transparencia del registro facilita unas prácticas y dificulta otras, y que el mayor grupo de casos no detectados —la anticipación de órdenes— no tenía ningún indicador porque los indicadores se copiaron de otro mercado.

## Datos

Un mes de vigilancia sintética con alertas, confirmaciones y casos conocidos a posteriori.

## Supuestos del ejercicio

- Valor de detectar un caso: 45 000.
- El indicador nuevo añade 940 alertas y 9 casos.
- Coste de revisar una alerta: 18.

## Requisitos

- Laboratorio 5 completado.
- Haber leído la clase 11.

## Pasos

1. Calcula precisión, exhaustividad y coste del sistema actual.
2. Simula subir el umbral y mide qué exhaustividad se pierde.
3. Añade el indicador que falta y recalcula ambas métricas.
4. Comprueba que la precisión empeora y la exhaustividad mejora.
5. Calcula el coste marginal por caso y compáralo con el medio.
6. Decide con el coste marginal frente al valor del caso.
7. Comprueba que un indicador sin casos extra no se justifica.
8. Evalúa los cuatro conflictos de una plataforma que además opera.

## Arquitectura

```text
PRECISION     confirmados / alertas
EXHAUSTIVIDAD confirmados / casos reales

AÑADIR UN INDICADOR
  empeora la precision
  mejora la exhaustividad

Y LA DECISION SE TOMA CON
  coste MARGINAL por caso
  frente al VALOR del caso
  nunca con el coste medio
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Precisión y exhaustividad se separan | Cálculo independiente |
| 2 | Subir el umbral pierde exhaustividad | Comparación |
| 3 | El indicador mejora la exhaustividad | 14,5 puntos |
| 4 | El coste marginal supera al medio | Y aun así se justifica |
| 5 | Sin casos extra no se justifica | Comprobación |
| 6 | Los cuatro conflictos se identifican | Con su mitigación |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Copiar indicadores | Es lo rápido | El abuso aquí es distinto |
| Optimizar la precisión | Reduce el ruido | La exhaustividad es lo que protege |
| Decidir con el coste medio | Es el que se calcula | Decide el marginal |
| Conflictos «gestionados» | Hay una política | La separación funciona mejor |
| Mejor ejecución afirmada | Nadie la pide | Hay que demostrarla con datos |

## Pruebas

```bash
python -m pytest tests/test_regulatory_perimeter_engine.py -q -k "precision or indicador or marginal"
```

```bash
python apps/regulatory_perimeter_engine/cli.py compliance
```

## Entregables

- Precisión, exhaustividad y coste del sistema actual.
- El efecto de mover el umbral.
- El indicador nuevo con su justificación por coste marginal.
- `solution.md` con los cuatro conflictos y su mitigación.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Métricas calculadas | 20 |
| Efecto del umbral | 20 |
| Indicador nuevo diseñado | 25 |
| Decisión por coste marginal | 20 |
| Conflictos de interés | 15 |

## Solución de referencia

En [`solutions/lab-06.md`](../solutions/lab-06.md).
