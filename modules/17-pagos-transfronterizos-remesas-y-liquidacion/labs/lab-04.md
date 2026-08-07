# Laboratorio 4: Screening y reparaciones

## Propósito

Calibrar un sistema de detección midiendo **precisión y exhaustividad**, y
demostrar por qué subir el umbral es casi siempre la corrección equivocada.

## Escenario

El área de negocio de `Banco Andino` pide subir el umbral de coincidencia del
82 % al 90 % porque la cola manual crece. Tu tarea es responder con la prueba
retrospectiva, y proponer la corrección que sí funciona.

## Contexto

En sanciones no hay apetito de riesgo: un falso negativo es una operación con
una persona designada. La reducción del ruido debe venir de la **calidad de la
comparación**, no de relajar el criterio.

## Datos

`datasets/synthetic/sanctions_screening_alerts.csv` — 12 000 alertas sintéticas
con su resolución conocida, y una lista de designados sintética. Diccionario en
`datasets/schemas/sanctions_screening_alerts.md`.

## Supuestos del ejercicio

- La lista y los nombres son **sintéticos**: no corresponden a personas reales
  ni a ninguna lista oficial.
- La resolución de cada alerta está etiquetada, lo que en producción no ocurre.
- Se ignora el componente de comportamiento: solo se trabaja el de nombres.

## Requisitos

- Python 3.11 o superior.
- Haber leído la clase 12.

## Pasos

1. Implementa la comparación de nombres con una medida de similitud.
2. Calcula **precisión**, **exhaustividad** y su media armónica para umbrales
   del 70 % al 95 %.
3. Dibuja la curva y localiza el punto donde la exhaustividad empieza a caer.
4. Ejecuta la **prueba retrospectiva**: con umbral del 90 %, ¿cuántos verdaderos
   positivos se pierden?
5. Clasifica los falsos positivos por causa: apellido común, transliteración,
   dato ausente, entidad genérica.
6. Implementa dos correcciones de calidad: exigencia de segundo campo para
   apellidos frecuentes y normalización fonética.
7. Recalcula las métricas con las correcciones y compara.
8. Implementa la cola de reparación: los mensajes con datos incompletos y su
   causa.

## Arquitectura

```text
mensaje ──► normalización ──► comparación ──► puntuación
                                                  │
                    ┌─────────────────────────────┤
                    ▼                             ▼
              < umbral: pasa              ≥ umbral: alerta
                                                  │
                                    ┌─────────────┴────────────┐
                                    ▼                          ▼
                          descartada con motivo        escalada
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Precisión y exhaustividad calculadas | Informe con las dos |
| 2 | Prueba retrospectiva ejecutada | Verdaderos positivos perdidos por umbral |
| 3 | Falsos positivos clasificados por causa | Tabla de causas |
| 4 | Las correcciones mejoran la exhaustividad | Comparación antes y después |
| 5 | Ningún descarte sin motivo registrado | Revisión del registro |
| 6 | La cola de reparación identifica la causa | Informe por campo |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Umbral relajado por presión | Falso negativo en sanciones | Prueba retrospectiva obligatoria |
| Descarte sin evidencia | No se puede auditar | Motivo obligatorio |
| Normalización que pierde información | Se dejan de detectar variantes | Medir exhaustividad tras cada cambio |
| Lista desactualizada | Se opera con datos viejos | Alerta si no se actualiza |
| Datos sintéticos tomados por reales | Confusión grave | Declararlo en cada salida |

## Pruebas

```bash
python -m pytest tests/test_cross_border_payments_lab.py -q -k screening
```

```bash
python apps/cross_border_payments_lab/cli.py screening --threshold 0.82
```

## Entregables

- La curva de precisión y exhaustividad por umbral.
- La prueba retrospectiva completa, con los verdaderos positivos perdidos.
- La clasificación de falsos positivos por causa.
- Las dos correcciones implementadas y su efecto medido.
- `solution.md` con la respuesta escrita al área de negocio.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Métricas correctamente calculadas | 25 |
| Prueba retrospectiva | 25 |
| Clasificación por causa | 20 |
| Correcciones que mejoran la exhaustividad | 20 |
| Respuesta argumentada al negocio | 10 |

## Solución de referencia

En [`solutions/lab-04.md`](../solutions/lab-04.md).
