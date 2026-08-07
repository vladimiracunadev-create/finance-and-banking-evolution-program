# Laboratorio 6: Comparación con base centralizada

## Propósito

Medir. El laboratorio que cierra la parte no construye nada nuevo: **compara con
números lo construido frente a la alternativa más simple**, que es la pieza que
ningún expediente trae.

## Escenario

El comité pregunta: «¿por qué no una base de datos compartida operada por una
sociedad conjunta?». Tu tarea es responder con mediciones, sea cual sea la
respuesta.

## Contexto

Es la pieza 3 del expediente de la clase 14 y la pregunta 1 del comité. Un
proyecto que no la trae no se puede evaluar.

## Datos

Los generados en los laboratorios 1 a 5, más una implementación de referencia
con SQLite de la biblioteca estándar.

## Supuestos del ejercicio

- La alternativa centralizada es una base de datos con firma de cada apunte y
  registro de auditoría.
- Ambas se ejecutan en la misma máquina: los números son comparables entre sí,
  no con producción.
- No se modela el coste de personal ni de gobierno.

## Requisitos

- Laboratorios 1 a 5 completados.
- Haber leído las clases 1, 7 y 14.

## Pasos

1. Implementa la alternativa: tabla de operaciones con firma y auditoría.
2. Mide **latencia de escritura** de ambas, en percentiles.
3. Mide **capacidad** de ambas, en operaciones por segundo.
4. Mide **almacenamiento** por millón de operaciones.
5. Mide el **tiempo de recuperación** tras un error: corregir en la base frente
   a compensar en la cadena.
6. Aplica los seis criterios de la clase 1 y rellena la tabla con tus números.
7. Aplica las seis preguntas del criterio y responde cada una para tu caso.
8. Escribe la conclusión: qué justifica el sobrecoste, o admite que no lo hay.

## Arquitectura

```text
             CADENA                    BASE COMPARTIDA
  escritura  consenso + bloque         transacción SQL
  latencia   ronda completa            milisegundos
  verificación  cada nodo               confiar en el operador
  corrección    compensación            actualización con traza
  si el operador desaparece  sigue      muere
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Ambas implementaciones funcionan | Mismo conjunto de operaciones |
| 2 | Latencia en percentiles | p50, p95, p99 de las dos |
| 3 | Capacidad medida | Operaciones por segundo |
| 4 | Almacenamiento por millón | Comparación directa |
| 5 | Tiempo de recuperación medido | Los dos procedimientos |
| 6 | Los seis criterios con tus números | Tabla completa |
| 7 | Conclusión explícita | Incluye la posibilidad de que no compense |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Comparación sesgada | Se mide lo favorable | Mismo conjunto de operaciones |
| Ignorar el coste de gobierno | La cadena parece más barata | Declararlo como no medido |
| Medir en producción distinta | Números incomparables | Misma máquina, declararlo |
| Concluir antes de medir | El resultado se busca | Escribir la conclusión al final |
| Omitir la fila que pierde | El expediente no convence | Todas las filas, gane quien gane |

## Pruebas

```bash
python -m pytest tests/test_dlt_financial_lab.py -q -k comparacion
```

```bash
python apps/dlt_financial_lab/cli.py compare --operations 10000
```

## Entregables

- Las dos implementaciones con el mismo conjunto de operaciones.
- Las cuatro mediciones, en percentiles donde corresponda.
- La tabla de los seis criterios con tus números.
- Las seis preguntas respondidas para tu caso.
- `solution.md` con la conclusión, incluida la posibilidad de que no compense.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Ambas implementaciones comparables | 20 |
| Mediciones correctas y en percentiles | 25 |
| Tabla de los seis criterios | 20 |
| Las seis preguntas respondidas | 20 |
| Conclusión honesta | 15 |

## Solución de referencia

En [`solutions/lab-06.md`](../solutions/lab-06.md).
