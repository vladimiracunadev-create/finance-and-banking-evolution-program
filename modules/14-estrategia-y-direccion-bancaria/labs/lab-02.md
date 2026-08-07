# Laboratorio 2: Rentabilidad por cliente y producto

## Propósito

Calcular la rentabilidad en cuatro capas y **comprobar que la decisión de cerrar cambia según la capa que se mire**.

El laboratorio 1 miró el banco entero. Este baja al producto y al cliente, donde la asignación de costos indirectos decide qué parece rentable y qué no.

## Escenario

Un producto que aparece como no rentable con costos asignados y aporta margen con costos evitables.

## Datos

El detalle de ingresos, costos directos, indirectos y capital consumido del producto.

## Supuestos del ejercicio

- El precio de transferencia interno se entrega con su curva.
- Los costos indirectos se asignan por dos métodos distintos.
- El costo del capital consumido se entrega como dato.

## Pasos

1. Calcula el margen directo del producto.
2. Resta los costos directos y obtén la segunda capa.
3. Asigna los indirectos por los dos métodos y obtén la tercera capa con cada uno.
4. Resta el costo del capital consumido y obtén la cuarta.
5. Determina qué decisión sugiere cada capa.
6. Calcula el costo evitable del producto si se cerrara.
7. Decide y justifica con la capa que corresponde a la decisión de cerrar.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Las cuatro capas están calculadas | Con su cifra |
| 2 | Los dos métodos de asignación se comparan | Con su efecto |
| 3 | La decisión que sugiere cada capa está identificada | Y difieren |
| 4 | El costo evitable está calculado | No el asignado |
| 5 | La decisión usa la capa correcta | Con su justificación |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Decidir con costos asignados | El costo asignado no desaparece al cerrar |
| Un solo método de asignación | Cambia qué producto parece rentable |
| Olvidar el costo del capital | Un producto puede cubrir costos y destruir valor |
| Cerrar sin calcular el evitable | Es el error más caro de esta clase |

## Entregables

- `solution.md` con las cuatro capas y los dos métodos.
- La decisión que sugiere cada capa.
- El costo evitable calculado.
- La decisión final con su justificación.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Cuatro capas | 30 |
| Dos métodos comparados | 20 |
| Decisiones por capa | 20 |
| Costo evitable | 20 |
| Decisión justificada | 10 |
