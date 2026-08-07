# Laboratorio 4: Riesgo reputacional y de conducta

## Propósito

Cuantificar un evento de conducta por sus dos vías y **comprobar que la reputacional supera a la sanción**.

El laboratorio 3 midió pérdidas operativas directas. Este mide el riesgo que no aparece en ninguna base de eventos y que suele costar más: el que se materializa en clientes que se van.

## Escenario

Una entidad que vendió un producto fuera de su mercado objetivo a 4 200 clientes durante dieciocho meses.

## Datos

El detalle de la venta, la sanción estimada y las series de fuga de clientes tras episodios comparables.

## Supuestos del ejercicio

- El margen anual por cliente se entrega como dato.
- La tasa de fuga observada en episodios comparables se entrega.
- El costo de reparación por cliente afectado se estima.

## Pasos

1. Cuantifica la pérdida directa: reparación a clientes y sanción estimada.
2. Estima la fuga de clientes con la tasa observada en episodios comparables.
3. Cuantifica la pérdida reputacional como valor presente del margen perdido.
4. Compara ambas vías y calcula la proporción.
5. Identifica el incentivo comercial que produjo la venta indebida.
6. Rediseña ese incentivo y estima el efecto sobre el volumen.
7. Propón el control de gobierno de productos que lo habría evitado.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | La pérdida directa está cuantificada | Reparación y sanción |
| 2 | La fuga está estimada | Con la tasa comparable |
| 3 | La pérdida reputacional está en valor presente | Del margen perdido |
| 4 | Las dos vías se comparan | Con su proporción |
| 5 | El incentivo está identificado y rediseñado | Con su efecto |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Cuantificar solo la sanción | Suele ser la menor de las dos vías |
| Tratar la fuga como no medible | Hay tasas observadas en episodios comparables |
| Culpar a la fuerza de venta | El incentivo produjo la conducta |
| Proponer formación como control | No corrige un incentivo mal diseñado |

## Entregables

- `solution.md` con las dos vías cuantificadas.
- La proporción entre reputacional y directa.
- El incentivo identificado y su rediseño.
- El control de gobierno de productos propuesto.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Pérdida directa | 20 |
| Fuga estimada | 25 |
| Reputacional en valor presente | 25 |
| Incentivo rediseñado | 20 |
| Control propuesto | 10 |
