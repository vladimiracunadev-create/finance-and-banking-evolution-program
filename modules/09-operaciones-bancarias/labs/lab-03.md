# Laboratorio 3: Compensación y liquidación

## Propósito

Compensar el mismo conjunto de operaciones bilateral y multilateralmente, y **medir el riesgo que la reducción de volumen introduce**.

El laboratorio 2 trató un proceso interno. Este trata lo que ocurre entre bancos, donde reducir el volumen a liquidar concentra el riesgo en vez de eliminarlo.

## Escenario

Sesenta operaciones entre seis bancos en una jornada, con un participante que falla después de calculada la posición neta.

## Datos

Las sesenta operaciones con su ordenante, su beneficiario y su importe.

## Supuestos del ejercicio

- Todos los participantes liquidan en el mismo sistema.
- El fallo del participante ocurre después del cálculo de posiciones y antes de la liquidación.
- La liquidez intradía disponible de cada banco se entrega como dato.

## Pasos

1. Calcula el importe total a liquidar sin compensación.
2. Compensa bilateralmente y recalcula el importe.
3. Compensa multilateralmente y obtén las posiciones netas.
4. Compara los tres importes y calcula el ratio de compensación.
5. Simula el fallo del participante y determina a quién alcanza y por cuánto.
6. Calcula la liquidez intradía que cada banco necesita en cada escenario.
7. Explica qué aporta una contraparte central y qué concentra.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los tres importes están calculados | Sin compensar, bilateral y multilateral |
| 2 | El ratio de compensación está calculado | Con su fórmula |
| 3 | El fallo se propaga y se cuantifica | A quién y por cuánto |
| 4 | La liquidez intradía está calculada | En los tres escenarios |
| 5 | El papel de la contraparte central está explicado | Con lo que concentra |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Ver la compensación solo como ahorro | Concentra el riesgo de liquidación |
| No simular el fallo | Es donde aparece el riesgo que la compensación crea |
| Confundir compensación con liquidación | Son dos momentos distintos |
| Ignorar la liquidez intradía | Es un requisito de momento, no de día |

## Entregables

- `solution.md` con los tres importes y el ratio.
- Las posiciones netas multilaterales.
- La propagación del fallo cuantificada.
- La liquidez intradía necesaria en cada escenario.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Tres importes correctos | 30 |
| Posiciones netas | 20 |
| Fallo propagado | 25 |
| Liquidez intradía | 15 |
| Contraparte central | 10 |
