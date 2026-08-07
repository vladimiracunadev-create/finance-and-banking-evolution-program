# Laboratorio 4: Consenso con nodos defectuosos

## Propósito

Medir la tolerancia de un consenso en vez de suponerla, y demostrar el hallazgo
de la clase 5: **el umbral protege de nodos que mienten, no de software que se
equivoca igual en todos**.

## Escenario

El consorcio afirma que su red «tolera un fallo» porque tiene cinco nodos. Tu
tarea es comprobarlo ejecutándolo, y después comprobar qué ocurre con un fallo
común que afecta a tres.

## Contexto

Contar nodos no es contar independencias. El laboratorio construye las dos
situaciones y mide la diferencia.

## Datos

Nodos simulados en memoria, con comportamientos configurables.

## Supuestos del ejercicio

- El consenso es una implementación **didáctica** de un protocolo de votación
  por rondas; no reproduce ningún protocolo de producción.
- La red no pierde mensajes salvo cuando se le indica.
- Los relojes están sincronizados.

## Requisitos

- Laboratorio 1 completado.
- Haber leído las clases 5 y 6.

## Pasos

1. Implementa un nodo con tres comportamientos: honesto, silencioso y mentiroso.
2. Implementa una ronda de consenso con quórum de 2f + 1 sobre 3f + 1.
3. Ejecuta con n = 4 y f = 1: comprueba que llega a acuerdo con un mentiroso.
4. Ejecuta con dos mentirosos y comprueba que **no** llega a acuerdo.
5. Verifica que ante la falta de quórum el sistema **se detiene** en vez de
   divergir.
6. Introduce un **fallo común**: tres nodos que devuelven el mismo resultado
   incorrecto. Comprueba que el sistema acuerda un valor erróneo.
7. Mide el número de mensajes por ronda y compáralo con n².
8. Implementa la rotación de productor y la detección de desviación de orden.

## Arquitectura

```text
ronda
  1. el productor propone un bloque
  2. cada nodo vota (aceptar / rechazar)
  3. si hay 2f+1 votos de aceptación, se decide
  4. si no, se pasa al siguiente productor

comportamientos
  honesto     vota según lo que verifica
  silencioso  no responde
  mentiroso   vota lo contrario, o distinto a cada uno
  común       varios devuelven el mismo error
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Con f mentirosos hay acuerdo | Prueba con n = 4, f = 1 |
| 2 | Con f + 1 no hay acuerdo | Prueba con 2 mentirosos |
| 3 | Sin quórum el sistema se detiene | No hay dos estados distintos |
| 4 | El fallo común produce acuerdo erróneo | Prueba documentada |
| 5 | Los mensajes crecen con n² | Medición para n = 4, 7, 10 |
| 6 | Una desviación de orden se detecta | Prueba con productor desviado |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Más de f mentirosos | No hay acuerdo | Detenerse, no divergir |
| Fallo común | Acuerdo sobre un valor erróneo | Diversidad o riesgo declarado |
| Productor que censura | Operaciones excluidas | Orden verificable y consecuencia |
| Partición de red | Dos grupos avanzan | Exigir quórum estricto |
| Reloj desajustado | Reorganizaciones espurias | Tolerancia acotada |

## Pruebas

```bash
python -m pytest tests/test_dlt_financial_lab.py -q -k consenso
```

```bash
python apps/dlt_financial_lab/cli.py consensus --nodes 4 --faulty 1
```

## Entregables

- El consenso implementado con los cuatro comportamientos.
- La medición del umbral real, ejecutada.
- La demostración del fallo común y su acuerdo erróneo.
- La medición de mensajes para tres tamaños.
- `solution.md` con la diferencia entre contar nodos y contar independencias.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Consenso funcional | 20 |
| Umbral medido, no supuesto | 25 |
| Demostración del fallo común | 25 |
| Detenerse en vez de divergir | 20 |
| Medición de mensajes | 10 |

## Solución de referencia

En [`solutions/lab-04.md`](../solutions/lab-04.md).
