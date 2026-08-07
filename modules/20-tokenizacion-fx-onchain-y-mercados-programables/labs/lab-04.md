# Laboratorio 4: Modos de fallo de la liquidación

## Propósito

Recorrer los fallos que la atomicidad **no** cubre y comprobar que cada uno necesita su propio control.

## Escenario

La misma plataforma del laboratorio 3, ahora con el registro que se detiene, un custodio que hay que sustituir y tres infraestructuras que conectar.

## Contexto

La clase 8 enumera cinco riesgos y la atomicidad elimina uno. La clase 9 añade la custodia y su conciliación a tres bandas; la clase 15, la conexión entre registros.

## Datos

Liquidador sintético, esquema de custodia 3-de-5 y tres infraestructuras con su volumen por par.

## Supuestos del ejercicio

- Disponibilidad del registro del 99,9 %.
- Variación media de precio en un día del 0,35 %.
- El 20 % del volumen diario permanecería en un puente.

## Requisitos

- Laboratorio 3 completado.
- Haber leído las clases 8, 9 y 15.

## Pasos

1. Detén el registro y comprueba que las operaciones se rechazan sin tocar saldos.
2. Calcula el coste de reemplazo de un ciclo completo fallido.
3. Mide la independencia efectiva de un esquema de custodia 3-de-5 con cuatro guardianes en la sede.
4. Redistribuye las partes sin cambiar el umbral y vuelve a medir.
5. Simula la conciliación a tres bandas y provoca la diferencia que una comprobación dos a dos oculta.
6. Compara los cuatro modelos de interoperabilidad con el volumen por par.
7. Mide el umbral efectivo de un puente y su valor acumulado.
8. Escribe el plan de sustitución del custodio con sus seis elementos.

## Arquitectura

```text
RIESGOS = {
  principal  → lo elimina la atomicidad
  reemplazo  → subsiste
  liquidez   → subsiste
  operativo  → subsiste
  juridico   → subsiste
}

CONEXION ENTRE REGISTROS
  puente · enlace directo · participante comun · consolidacion
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | El registro detenido rechaza sin tocar nada | Saldos sin cambios |
| 2 | El coste de reemplazo se calcula | Sobre el volumen del ciclo |
| 3 | La independencia efectiva se mide | Cuatro factores |
| 4 | La redistribución no cambia el umbral | Sigue siendo 3-de-5 |
| 5 | La conciliación a tres bandas ve la diferencia | Caso construido |
| 6 | El umbral efectivo del puente se mide | Frente al valor acumulado |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Conciliar dos a dos | Una diferencia persiste dando ambas por buenas | Conciliación a tres bandas con responsable |
| Puente con umbral efectivo bajo | Objetivo económico racional | Medir independencia y valor acumulado |
| Sin plan de sustitución | Depende del que está en dificultades | Copia diaria en un tercero |
| Fallo del ciclo no dimensionado | Afecta a todas las operaciones | Coste de reemplazo calculado |
| Consolidación como proyecto técnico | Fracasa por gobierno | Abordarla como negociación |

## Pruebas

```bash
python -m pytest tests/test_tokenization_platform.py -q -k "detenido or riesgo or neteo"
```

```bash
python apps/tokenization_platform/cli.py settlement
```

## Entregables

- El escenario de registro detenido con su coste de reemplazo.
- La independencia efectiva antes y después de redistribuir.
- La comparación de los cuatro modelos de conexión.
- `solution.md` con el plan de sustitución del custodio.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Fallos que la atomicidad no cubre | 25 |
| Independencia efectiva medida | 20 |
| Conciliación a tres bandas | 20 |
| Modelos de conexión comparados | 20 |
| Plan de sustitución con seis elementos | 15 |

## Solución de referencia

En [`solutions/lab-04.md`](../solutions/lab-04.md).
