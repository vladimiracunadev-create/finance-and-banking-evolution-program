# Laboratorio 4: Experiencia del cliente y eficiencia

## Propósito

Calcular el costo de la mala calidad y el de la complejidad, y **comprobar que superan a lo que un programa de eficiencia suele recortar**.

El laboratorio 3 definió la promesa. Este mide lo que cuesta incumplirla y lo que cuesta la complejidad acumulada, dos costos reales que no aparecen en ninguna partida.

## Escenario

Un banco con 34 productos vivos, de los cuales 11 tienen menos de 400 clientes, y un índice de eficiencia del 58 %.

## Datos

El catálogo con sus volúmenes, los reclamos por producto y la base de costos desglosada.

## Supuestos del ejercicio

- El costo fijo por producto vivo se entrega como dato.
- El costo de atender un reclamo y el de rehacer una operación se entregan.
- La tasa de resolución en primer contacto se entrega por canal.

## Pasos

1. Descompón la base de costos por naturaleza y por causa.
2. Calcula el costo de la mala calidad: reprocesos, reclamos y compensaciones.
3. Calcula el costo de la complejidad de los 11 productos marginales.
4. Compara ambos con el recorte típico de un programa de eficiencia.
5. Identifica qué recortes empeorarían el índice en vez de mejorarlo.
6. Diseña un programa que ataque los dos costos anteriores.
7. Estima el efecto sobre el índice de eficiencia y sobre la experiencia.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | La base está descompuesta | Por naturaleza y por causa |
| 2 | El costo de la mala calidad está calculado | Con sus tres componentes |
| 3 | El costo de la complejidad está calculado | De los productos marginales |
| 4 | Los recortes contraproducentes están identificados | Con su razón |
| 5 | El efecto sobre el índice está estimado | Y sobre la experiencia |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Recortar lo que sostiene ingresos | Empeora el índice que se quería mejorar |
| No medir el costo de la mala calidad | Suele ser mayor que el recorte propuesto |
| Ignorar la complejidad | Cada producto vivo cuesta aunque no venda |
| Medir eficiencia solo por el numerador | El denominador también se puede mover |

## Entregables

- `solution.md` con la base descompuesta.
- Los dos costos calculados.
- Los recortes contraproducentes identificados.
- El programa diseñado con su efecto estimado.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Base descompuesta | 20 |
| Costo de la mala calidad | 25 |
| Costo de la complejidad | 25 |
| Recortes contraproducentes | 15 |
| Programa con efecto | 15 |
