# Laboratorio 3: Entrega contra pago atómica

## Propósito

Demostrar que **no existe ningún estado observable** en que uno de los tramos se haya movido y el otro no, y medir qué cuesta esa propiedad.

## Escenario

Una plataforma liquida 2 400 operaciones diarias de bonos tokenizados contra depósitos tokenizados en el mismo registro.

## Contexto

La clase 8 define la atomicidad como la ausencia de estado intermedio, no como que los movimientos ocurran «casi a la vez». La clase 10 añade que sin el dinero en el mismo registro no puede existir.

## Datos

Liquidador sintético con saldos de valor y de dinero por participante.

## Supuestos del ejercicio

- Saldo prefinanciado del 22 % del volumen sin neteo y del 9 % con neteo.
- Probabilidad de incumplimiento a 2 días del 0,004 %.
- Recuperación esperada del 45 %.

## Requisitos

- Laboratorio 2 completado.
- Haber leído las clases 8 y 10.

## Pasos

1. Observa el estado antes y después de una liquidación y comprueba que no hay ningún estado a medias.
2. Provoca el fallo del tramo de dinero y verifica que el valor queda intacto.
3. Provoca el fallo del tramo de valor y verifica que el dinero queda intacto.
4. Intenta liquidar dos operaciones sobre el mismo saldo y comprueba que solo una se ejecuta.
5. Configura el liquidador con el dinero fuera del registro y comprueba que **se niega** en vez de simular atomicidad.
6. Netea un ciclo de operaciones y verifica que los saldos suman cero.
7. Calcula el ahorro por atomicidad y el coste de liquidez con bruto y con neteo.
8. Enumera los cinco riesgos y comprueba que la atomicidad elimina exactamente uno.

## Arquitectura

```text
Liquidador.liquidar(operacion)
   1 verificar valor del vendedor
   2 verificar dinero del comprador
   3 si falla cualquiera → RECHAZAR sin tocar nada
   4 si no → los cuatro movimientos en un solo acto

observar() devuelve el estado completo
→ las pruebas comprueban que nunca esta a medias
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | No hay estado intermedio | Comparación de `observar()` |
| 2 | El fallo de dinero deja el valor intacto | Saldo sin cambios |
| 3 | El fallo de valor deja el dinero intacto | Saldo sin cambios |
| 4 | Doble gasto imposible | La segunda operación se rechaza |
| 5 | Sin dinero dentro se niega | Excepción esperada |
| 6 | El neteo suma cero | Saldos compensados |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Bloquear y revertir | Hubo un estado intermedio observable | Rechazar antes de bloquear |
| Prometer atomicidad con el dinero fuera | La arquitectura lo impide | Verificar dónde está cada tramo |
| Ignorar el coste de liquidez | El ahorro se sobrestima | Restarlo del cálculo |
| Fallo del neteo no dimensionado | Fallan todas las operaciones | Calcular el coste de reemplazo del ciclo |
| Riesgo trasladado al emisor del dinero | Se elimina uno y aparece otro | Declararlo y medirlo |

## Pruebas

```bash
python -m pytest tests/test_tokenization_platform.py -q -k "estado_intermedio or tramo or doble or atomicidad or neteo"
```

```bash
python apps/tokenization_platform/cli.py settlement
```

## Entregables

- Las pruebas de ausencia de estado intermedio y de fallo por tramo.
- El neteo de un ciclo con sus saldos.
- El cálculo de ahorro neto con bruto y con neteo.
- `solution.md` con los cinco riesgos y su control.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Ausencia de estado intermedio demostrada | 25 |
| Fallos por tramo probados | 20 |
| Rechazo antes de bloquear | 20 |
| Ahorro neto calculado | 20 |
| Los cinco riesgos con su control | 15 |

## Solución de referencia

En [`solutions/lab-03.md`](../solutions/lab-03.md).
