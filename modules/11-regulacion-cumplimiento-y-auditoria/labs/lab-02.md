# Laboratorio 2: Programa de cumplimiento

## Propósito

Mapear diez obligaciones hasta su prueba y **encontrar las que no tienen control asignado**.

El laboratorio 1 identificó qué obliga. Este comprueba que cada obligación tiene dueño, control y prueba, que es donde casi todos los programas se quedan a medias.

## Escenario

Un programa con inventario de 120 obligaciones, del que se toma una muestra de diez para el ejercicio.

## Datos

Las diez obligaciones con su área asignada y sus controles declarados.

## Supuestos del ejercicio

- Dos de las diez no tienen control asignado.
- Tres tienen control declarado y sin prueba documentada.
- La frecuencia de prueba exigible se entrega como dato.

## Pasos

1. Verifica que cada obligación tiene responsable identificado.
2. Mapea cada una a su control y comprueba que el control la cubre.
3. Comprueba que cada control tiene prueba documentada y con su frecuencia.
4. Identifica las obligaciones sin control y las que tienen control sin prueba.
5. Diseña el control y la prueba de las que faltan.
6. Construye tres indicadores de efectividad del programa que no sean horas de formación.
7. Propón cómo se integran los hallazgos de cumplimiento, auditoría y supervisión.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Cada obligación tiene responsable | Identificado |
| 2 | El mapeo obligación-control está completo | Con la cobertura verificada |
| 3 | Las que carecen de control están identificadas | Las dos |
| 4 | Las que carecen de prueba están identificadas | Las tres |
| 5 | Los indicadores no son de actividad | Sino de efectividad |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Inventario sin dueño | Lo que no tiene dueño no se cumple |
| Control sin prueba | Es una intención documentada |
| Medir por horas de formación | Mide actividad y no efectividad |
| Tres ciclos de hallazgos separados | Se duplica trabajo y se pierden hallazgos |

## Entregables

- `solution.md` con el mapeo de las diez obligaciones.
- Las que carecen de control y las que carecen de prueba.
- El control y la prueba diseñados para las que faltan.
- Los tres indicadores de efectividad.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Responsables verificados | 15 |
| Mapeo completo | 25 |
| Huecos identificados | 25 |
| Controles diseñados | 20 |
| Indicadores de efectividad | 15 |
