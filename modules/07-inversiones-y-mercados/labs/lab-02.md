# Laboratorio 2: Bonos

## Propósito

Valorar el mismo bono a cinco tasas y **comprobar que la sensibilidad crece con el plazo**, sin que haya cambiado el riesgo de crédito.

El laboratorio 1 fijó el perfil. Este entra en el instrumento donde la relación entre precio y tasa es más visible, y donde más gente se sorprende de perder dinero sin que nadie haya incumplido.

## Escenario

Tres bonos del mismo emisor con cupones iguales y plazos de 2, 7 y 20 años.

## Datos

Los tres bonos con su valor nominal, su cupón y su precio de mercado.

## Supuestos del ejercicio

- El emisor no cambia de calificación durante el ejercicio.
- Los cupones son anuales y se pagan al final de cada año.
- No hay opción de rescate anticipado.

## Pasos

1. Calcula el precio de los tres bonos a la tasa de mercado inicial.
2. Recalcula a cuatro tasas más, dos por encima y dos por debajo.
3. Tabula la variación porcentual del precio de cada bono ante cada movimiento.
4. Ordena los tres por sensibilidad y relaciónala con el plazo.
5. Calcula el rendimiento al vencimiento de cada uno con su precio de mercado.
6. Determina cuál cotiza sobre la par y cuál bajo la par, y explica por qué.
7. Enumera los riesgos del bono además del de impago.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los quince precios están calculados | Tres bonos por cinco tasas |
| 2 | La sensibilidad está tabulada | En porcentaje |
| 3 | El orden por sensibilidad es correcto | Y se relaciona con el plazo |
| 4 | El rendimiento al vencimiento está calculado | Para los tres |
| 5 | La posición respecto de la par está explicada | Con su razón |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Suponer que sin impago no hay pérdida | El precio cae cuando suben las tasas |
| Confundir cupón con rendimiento | Coinciden solo si el bono cotiza a la par |
| Ignorar el riesgo de reinversión | Los cupones se reinvierten a la tasa que haya |
| Valorar sin descontar cada cupón | Es la Parte 7 aplicada |

## Entregables

- `solution.md` con la matriz de quince precios.
- La sensibilidad tabulada y su relación con el plazo.
- El rendimiento al vencimiento de los tres.
- La lista de riesgos además del de impago.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Precios correctos | 30 |
| Sensibilidad tabulada | 25 |
| Rendimiento al vencimiento | 20 |
| Par explicada | 15 |
| Riesgos enumerados | 10 |
