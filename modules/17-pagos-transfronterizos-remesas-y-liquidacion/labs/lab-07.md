# Laboratorio 7: Payment versus Payment

## Propósito

Implementar la liquidación condicional y **romperla a propósito**: el valor del
laboratorio está en el escenario donde el coordinador falla entre el bloqueo y
la liberación.

## Escenario

`Banco Andino` opera 180 operaciones de cambio al día con 22 contrapartes
bilaterales. Su exposición máxima simultánea es de 412 millones. Tu tarea es
implementar el mecanismo de pago contra pago y demostrar qué elimina y qué no.

## Contexto

El pago contra pago elimina el riesgo de entregar sin recibir. **No elimina** el
riesgo de reposición, ni el de liquidez, ni el operacional del coordinador. Un
laboratorio que solo demuestra el camino feliz no enseña nada de eso.

## Datos

`apps/cross_border_payments_lab/data/fx_trades.json` — 180 operaciones con
importes, divisas, horas de entrega y contrapartes.

## Supuestos del ejercicio

- Dos sistemas de liquidación, uno por divisa, con husos distintos.
- El coordinador es una entidad simulada, sin garantías.
- El bloqueo tiene un plazo máximo, tras el cual se libera automáticamente.
- No hay red real: todo ocurre en memoria.

## Requisitos

- Laboratorio 1 completado.
- Haber leído las clases 7 y 15.

## Pasos

1. Calcula la **exposición máxima simultánea** de las 180 operaciones sin
   mecanismo, por contraparte y en total.
2. Implementa el mecanismo de **bloqueo y confirmación**: cada sistema reserva
   su pata, el coordinador comprueba ambas y ordena liberar.
3. Implementa la **atomicidad**: si una reserva falla, ninguna se libera.
4. Implementa el **plazo de bloqueo**: si el coordinador no confirma en N
   segundos, las reservas se deshacen.
5. Simula el **fallo del coordinador** después de que ambos sistemas hayan
   reservado y antes de la orden de liberación. Verifica que el plazo actúa.
6. Simula el **fallo de un sistema** tras liberar su pata. Documenta qué pasa y
   por qué este caso es el peligroso.
7. Recalcula la exposición con el mecanismo activo.
8. Calcula el coste: cuota, coste por operación y **prefinanciación**, y
   compáralo con el capital que la reducción de exposición libera.

## Arquitectura

```text
       sistema divisa A            coordinador           sistema divisa B
              │                         │                       │
   1. reservar│◄────────────────────────┼──────────────────────►│reservar
              │                         │                       │
              │─── reserva OK ─────────►│◄──── reserva OK ──────│
              │                         │                       │
              │◄──── liberar ───────────┼────── liberar ───────►│
              │                         │                       │
        liquidado                 registro               liquidado

  si NO llegan las dos reservas → nadie libera
  si el coordinador cae         → el plazo deshace las reservas
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Exposición máxima simultánea, no la mayor operación | Prueba con solapamiento |
| 2 | Una reserva fallida impide ambas liberaciones | Prueba de atomicidad |
| 3 | El plazo deshace las reservas | Prueba de fallo del coordinador |
| 4 | El fallo tras liberar se documenta | Informe del escenario |
| 5 | La exposición cae con el mecanismo | Comparación antes y después |
| 6 | El coste incluye la prefinanciación | Revisión del cálculo |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Coordinador cae tras reservar | Fondos bloqueados indefinidamente | Plazo con liberación automática |
| Un sistema libera y el otro no | Exposición total, sin protección | Documentar: es el caso límite |
| Riesgo de reposición | Hay que rehacer la operación al precio nuevo | Límite por contraparte, aparte |
| Liquidez inmovilizada | La prefinanciación crece | Medirla y gestionarla |
| Concentración en el coordinador | Punto único de fallo sistémico | Contingencia declarada |
| Bloqueo no oponible en quiebra | El mecanismo no protege | Verificación jurídica declarada |

## Pruebas

```bash
python -m pytest tests/test_cross_border_payments_lab.py -q -k pvp
```

```bash
python apps/cross_border_payments_lab/cli.py pvp --scenario coordinator-failure
```

## Entregables

- El cálculo de exposición máxima simultánea, antes y después.
- El mecanismo implementado con atomicidad y plazo.
- Los dos escenarios de fallo, ejecutados y documentados.
- El cálculo de coste frente a capital liberado.
- `solution.md` con la lista de riesgos que persisten y su control.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Exposición máxima simultánea correcta | 20 |
| Atomicidad implementada y probada | 25 |
| Escenarios de fallo ejecutados | 25 |
| Coste frente a capital liberado | 20 |
| Riesgos residuales identificados | 10 |

## Solución de referencia

En [`solutions/lab-07.md`](../solutions/lab-07.md).
