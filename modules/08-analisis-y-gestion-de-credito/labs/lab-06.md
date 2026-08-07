# Laboratorio 6: Proyecto: motor de evaluación crediticia

## Propósito

Codificar la política en reglas y **hacer que cada rechazo devuelva el motivo concreto que lo produjo**.

Es el último laboratorio de la parte y la antesala del proyecto. Un motor que decide y no explica no se puede defender ante el cliente ni ante el supervisor.

## Escenario

El motor debe aplicar la política de las quince clases anteriores y devolver decisión, motivo y trazabilidad.

## Datos

Los casos resueltos en los laboratorios 2 a 5.

## Supuestos del ejercicio

- Cada regla lleva el documento de política que la origina.
- Las excepciones tienen vía, nivel y registro.
- Ningún rechazo se devuelve sin motivo.

## Pasos

1. Escribe la política como reglas con su origen documentado.
2. Separa la política del cálculo y del motor de decisión.
3. Implementa la evaluación hasta que los casos de los laboratorios 2 a 5 pasen.
4. Haz que cada decisión devuelva el motivo concreto y la regla que lo produjo.
5. Implementa la vía de excepción con su nivel de aprobación y su registro.
6. Prueba con un caso que active dos reglas contradictorias y define la precedencia.
7. Comprueba que un cambio de política no exige tocar el código de cálculo.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | La política está escrita como reglas | Con su origen documentado |
| 2 | Las tres capas están separadas | Política, cálculo y decisión |
| 3 | Cada decisión devuelve motivo | Con la regla concreta |
| 4 | La vía de excepción existe y registra | Con nivel de aprobación |
| 5 | La precedencia entre reglas está definida | Probada con el caso contradictorio |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Reglas dispersas en el código | Cambiar la política obliga a tocar el cálculo |
| Rechazar sin motivo | No se puede explicar al cliente ni al supervisor |
| Excepciones sin registro | Se vuelven informales y nadie las audita |
| No definir precedencia | Dos reglas contradictorias producen resultados aleatorios |

## Entregables

- `solution.md` con la política codificada y su origen.
- El motor con sus pruebas en verde.
- Ejemplos de decisión con su motivo y su trazabilidad.
- La precedencia entre reglas y el caso que la prueba.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Política como reglas | 25 |
| Capas separadas | 20 |
| Motivo en cada decisión | 25 |
| Vía de excepción | 15 |
| Precedencia definida | 15 |
