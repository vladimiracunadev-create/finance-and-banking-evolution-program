# Laboratorio 3: Cola de redención

## Propósito

Demostrar con números que **la corrida no la causa el pánico, la causa el diseño
de la cola**: si ser el primero vale algo, todo tenedor racional solicita ya.

## Escenario

Un emisor con 5 000 000 000 en circulación recibe solicitudes por 1 800 000 000 y
tiene 900 000 000 de efectivo. Hay que resolver la ventana con dos reglas y medir
qué solicita el mercado al día siguiente.

## Contexto

La clase 5 sostiene que el orden de llegada premia al primero y que ese premio
es lo que produce la carrera. El prorrateo la apaga, pero deja sin efectivo al
que lo necesita: el tramo mínimo íntegro es la corrección.

## Datos

12 000 solicitantes de 150 000 cada uno, con un coste real de realización de
1,112 %.

## Supuestos del ejercicio

- Todas las solicitudes llegan dentro de la misma ventana.
- El coste de venta es el calculado en la clase 5, paso 2.
- El 40 % de los que cobran parcial necesita el dinero de verdad.

## Requisitos

- Laboratorio 2 completado.
- Haber leído la clase 5.

## Pasos

1. Resuelve la ventana con `Regla.ORDEN_DE_LLEGADA` y anota la ventaja del
   primero.
2. Resuélvela con `Regla.PRORRATEO` y comprueba que la ventaja es cero.
3. Activa la comisión antidilución y verifica que el coste lo soporta quien sale.
4. Añade un tramo mínimo íntegro de 5 000 y comprueba que **el pequeño cobra más
   sin que reaparezca la carrera entre los grandes**.
5. Calcula la solicitud del día siguiente con `solicitud_del_dia_siguiente` bajo
   ambas reglas.
6. Explica por qué la diferencia es de casi tres veces.
7. Diseña una ventana que proteja al minorista y no premie al primero, y
   justifica cada parámetro.
8. Redacta la cláusula de suspensión con sus cuatro elementos.

## Arquitectura

```text
Cola(efectivo, coste_de_venta, antidilucion, tramo_minimo_integro)
   ├── ORDEN_DE_LLEGADA  ventaja_del_primero = 1,0
   └── PRORRATEO         ventaja_del_primero = 0,0

ventaja > 0  →  solicita todo el mundo
ventaja = 0  →  solicita quien necesita el dinero
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | El orden de llegada da ventaja 1,0 | Primer y último pago |
| 2 | El prorrateo da ventaja 0,0 | Todas las fracciones iguales |
| 3 | La antidilución carga el coste al que sale | Comparación con y sin |
| 4 | El tramo mínimo protege al pequeño | Fracción mayor que la del grande |
| 5 | No reaparece la carrera entre grandes | Dispersión menor del 1 % |
| 6 | La solicitud de mañana difiere | Comparación de las dos reglas |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Orden de llegada por defecto | Produce la corrida | Prorrateo por ventana |
| Sin antidilución | El coste lo pagan los que quedan | Cargar el coste real al que sale |
| Prorrateo puro | El minorista se queda sin efectivo | Tramo mínimo íntegro |
| Reanudar por turno | Reabre la carrera entera | Reanudar a prorrata |
| Inmovilizar sin plazo | El tenedor queda sin nada | Plazo máximo contractual |

## Pruebas

```bash
python -m pytest tests/test_digital_assets_risk_lab.py -q -k "cola or prorrateo or antidilucion or tramo or solicitud"
```

```bash
python apps/digital_assets_risk_lab/cli.py queue
```

## Entregables

- Los dos resultados con su ventaja del primero.
- El efecto medido de la antidilución y del tramo mínimo.
- La solicitud del día siguiente bajo ambas reglas.
- `solution.md` con la ventana diseñada y la cláusula de suspensión.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Resolución con las dos reglas | 20 |
| Antidilución medida | 20 |
| Tramo mínimo sin reabrir la carrera | 25 |
| Solicitud del día siguiente | 20 |
| Cláusula de suspensión con cuatro elementos | 15 |

## Solución de referencia

En [`solutions/lab-03.md`](../solutions/lab-03.md).
