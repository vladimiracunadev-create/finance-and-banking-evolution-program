# Laboratorio 5: Liquidación de extremo a extremo

## Propósito

Construir el motor de liquidación y **probar cada uno de sus modos de fallo**, incluido el que nadie escribe: el sistema detenido.

El laboratorio 4 protegió las claves. Este ejecuta la operación completa y comprueba que cada fallo deja el sistema en un estado consistente, que es la única forma de demostrar la atomicidad.

## Escenario

Se liquida colateral contra depósito tokenizado, y se somete el motor a cinco escenarios de fallo distintos.

## Contexto

Las clases 10 y 11 construyen la liquidación interna y la conexión con el exterior. La 10 insiste en que la atomicidad elimina un riesgo de cinco.

## Datos

Un liquidador sintético con saldos de colateral y de dinero.

## Supuestos del ejercicio

- Volumen diario de colateral de 1 200 000.
- Ciclo actual T+1 y recuperación del 45 %.
- Disponibilidad del registro del 99,9 %.

## Requisitos

- Laboratorio 4 completado.
- Haber leído las clases 10 y 11.

## Pasos

1. Implementa la liquidación con rechazo previo al bloqueo.
2. Prueba que no existe estado intermedio observable.
3. Provoca el fallo de cada tramo y comprueba que el otro queda intacto.
4. Comprueba que dos operaciones sobre el mismo saldo no se ejecutan ambas.
5. Detén el registro y comprueba que rechaza sin tocar nada.
6. Calcula el ahorro neto restando el coste de liquidez.
7. Dimensiona el fallo del ciclo completo.
8. Modela los cuatro flujos de un pago por separado.

## Arquitectura

```text
LAS CINCO PRUEBAS

  1 sin estado intermedio observable
  2 falla el activo → dinero intacto
  3 falla el dinero → activo intacto
  4 doble gasto imposible
  5 REGISTRO DETENIDO → rechaza sin tocar

LA 5 ES LA QUE NADIE ESCRIBE.
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | No hay estado intermedio | Observación antes y después |
| 2 | Cada tramo que falla deja el otro intacto | Dos pruebas |
| 3 | El doble gasto es imposible | La segunda se rechaza |
| 4 | El registro detenido rechaza | Sin tocar saldos |
| 5 | El ahorro neto se calcula | Restando liquidez y fallo del ciclo |
| 6 | Los cuatro flujos se modelan | Con su momento y su fallo |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Bloquear y revertir | Es más fácil | Rechazar antes de bloquear |
| Probar solo el camino feliz | Es lo que funciona | Cada fallo con su prueba |
| Ignorar el coste de liquidez | Solo se mira el ahorro | Restarlo |
| No dimensionar el fallo del ciclo | Es improbable | Afecta a todo el ciclo |
| Abonar con el mensaje | Llegan casi juntos | El asiento va con los fondos |

## Pruebas

```bash
python -m pytest tests/test_digital_bank_capstone.py -q -k "tension or tolerancia or fuente"
```

```bash
python apps/digital_bank_capstone/cli.py stress
```

## Entregables

- La implementación con rechazo previo.
- Las cinco pruebas de modos de fallo ejecutadas.
- El ahorro neto con liquidez y fallo del ciclo restados.
- `solution.md` con los cuatro flujos modelados.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Rechazo previo implementado | 20 |
| Cinco pruebas ejecutadas | 30 |
| Ahorro neto corregido | 20 |
| Fallo del ciclo dimensionado | 15 |
| Cuatro flujos modelados | 15 |

## Solución de referencia

En [`solutions/lab-05.md`](../solutions/lab-05.md).
