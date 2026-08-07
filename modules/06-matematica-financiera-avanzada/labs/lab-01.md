# Laboratorio 1: Tasas nominales y efectivas

## Propósito

Comparar ocho ofertas que **tienen la misma tasa nominal y cuestan distinto**, y ordenarlas por su costo real.

Es el primer laboratorio de la parte y el que resuelve el error silencioso de toda ella: operar con una tasa sin saber a qué periodo corresponde.

## Escenario

Ocho ofertas de crédito y de depósito con la misma tasa nominal anual y frecuencias de capitalización distintas, de anual a diaria.

## Datos

Las ocho ofertas con su tasa nominal y su frecuencia.

## Supuestos del ejercicio

- Todas las ofertas son del mismo plazo total.
- No hay comisiones: la única diferencia es la frecuencia.
- Una de las ocho capitaliza de forma continua.

## Pasos

1. Convierte las ocho a tasa efectiva anual y tabúlalas.
2. Ordena las de crédito de más barata a más cara y las de depósito al revés.
3. Calcula la brecha entre la primera y la última en puntos y en pesos sobre un capital dado.
4. Resuelve el caso de capitalización continua y compáralo con la diaria.
5. Toma una tasa efectiva anual y divídela entre doce; compara con la periódica correcta.
6. Cuantifica el error de esa división y explica por qué crece con la tasa.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Las ocho están en tasa efectiva anual | Con su conversión visible |
| 2 | El orden es correcto en ambos sentidos | Crédito y depósito |
| 3 | La brecha está cuantificada | En puntos y en pesos |
| 4 | El caso continuo está resuelto | Y comparado con el diario |
| 5 | El error de dividir está cuantificado | Con su dependencia de la tasa |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Comparar por la tasa nominal | Es el error que el laboratorio persigue |
| Dividir una tasa efectiva entre doce | Da un resultado sistemáticamente equivocado |
| Olvidar el sentido del orden | En depósitos la mejor es la mayor |
| No cuantificar en pesos | Los puntos base no comunican la magnitud |

## Entregables

- `solution.md` con las ocho conversiones y su orden.
- La brecha en puntos y en pesos.
- El caso de capitalización continua.
- El error de la división, cuantificado.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Ocho conversiones correctas | 30 |
| Orden en ambos sentidos | 20 |
| Brecha cuantificada | 20 |
| Caso continuo | 15 |
| Error de división | 15 |
