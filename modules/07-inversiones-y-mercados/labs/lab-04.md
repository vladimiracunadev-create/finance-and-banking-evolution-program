# Laboratorio 4: Diversificación

## Propósito

Medir la diversificación efectiva de una cartera y **recalcularla con correlaciones de crisis**.

El laboratorio 3 trató un activo aislado. Este trata el conjunto, y su hallazgo incómodo es que la protección desaparece justo cuando se necesita.

## Escenario

Una cartera de diez fondos que parece muy diversificada y cuya exposición efectiva se concentra en tres factores.

## Datos

Los diez fondos con su composición y la matriz de correlaciones en calma y en crisis.

## Supuestos del ejercicio

- Las correlaciones en calma provienen de los últimos cinco años sin episodios adversos.
- Las correlaciones de crisis provienen de los tres peores trimestres observados.
- El número efectivo de activos se calcula sobre las ponderaciones.

## Pasos

1. Calcula el riesgo de la cartera con las correlaciones en calma.
2. Calcula el número efectivo de activos y compáralo con los diez nominales.
3. Identifica los factores comunes a los que están expuestos varios fondos.
4. Recalcula el riesgo con las correlaciones de crisis.
5. Cuantifica cuánto se pierde de diversificación entre ambos escenarios.
6. Propón dos cambios que aumenten la diversificación real y recalcula.
7. Distingue en la cartera lo que es diversificación real de lo que es aparente.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | El riesgo está calculado en ambos escenarios | Calma y crisis |
| 2 | El número efectivo está calculado | Y difiere de diez |
| 3 | Los factores comunes están identificados | Con los fondos que los comparten |
| 4 | La pérdida de diversificación está cuantificada | Entre escenarios |
| 5 | Los dos cambios propuestos mejoran la medida | Recalculado |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Contar instrumentos | Diez fondos del mismo factor diversifican como uno |
| Usar correlaciones de periodos tranquilos | Suben justo cuando importa |
| Diversificar por gestora o por nombre | No es una dimensión de diversificación |
| No recalcular tras los cambios | La propuesta puede no mejorar nada |

## Entregables

- `solution.md` con el riesgo en ambos escenarios.
- El número efectivo de activos y los factores comunes.
- La pérdida de diversificación cuantificada.
- Los dos cambios propuestos con su efecto recalculado.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Riesgo en ambos escenarios | 30 |
| Número efectivo | 20 |
| Factores comunes | 20 |
| Pérdida cuantificada | 15 |
| Cambios recalculados | 15 |
