# Laboratorio 6: Proyecto: simulador de sucursal

## Propósito

Dimensionar la operación **por volumen pico y no por la media**, y comprobar la diferencia.

Es el último laboratorio de la parte y la antesala del proyecto. Reúne los cinco anteriores en una operación que tiene que funcionar el peor día, no el día medio.

## Escenario

Una sucursal con cinco procesos críticos, volumen estacional y un día de pago de pensiones que multiplica por cuatro la afluencia.

## Datos

Los volúmenes por proceso y por día durante un trimestre, con sus tiempos de atención.

## Supuestos del ejercicio

- El tiempo de atención por tipo de operación se entrega como dato.
- El día de mayor afluencia se identifica en la serie.
- El costo por hora de atención y el costo de la espera se entregan.

## Pasos

1. Identifica los cinco procesos críticos por su efecto sobre el cliente.
2. Calcula la capacidad necesaria dimensionando por el volumen medio.
3. Recalcula dimensionando por el volumen pico.
4. Compara ambas y calcula el costo de la diferencia.
5. Calcula el costo de la espera en el escenario dimensionado por la media.
6. Diseña la conciliación diaria con su independencia y su escalamiento.
7. Propón qué operaciones migrar a otro canal y cuantifica el ahorro.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los procesos críticos están identificados | Por efecto sobre el cliente |
| 2 | Las dos capacidades están calculadas | Media y pico |
| 3 | El costo de la diferencia está calculado | En ambos sentidos |
| 4 | La conciliación tiene independencia definida | Y escalamiento |
| 5 | La migración de canal está cuantificada | En ahorro y en accesibilidad |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Dimensionar por la media | Produce colas exactamente cuando más importa |
| Ignorar el costo de la espera | Es real aunque no se facture |
| Conciliar sin independencia | No detecta nada |
| Migrar sin considerar accesibilidad | Excluye a quien no puede usar el canal barato |

## Entregables

- `solution.md` con los procesos críticos y las dos capacidades.
- El costo de la diferencia en ambos sentidos.
- El diseño de la conciliación diaria.
- La propuesta de migración con su ahorro y su efecto sobre la accesibilidad.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Procesos críticos | 15 |
| Dos capacidades | 30 |
| Costo comparado | 20 |
| Conciliación diseñada | 20 |
| Migración cuantificada | 15 |
