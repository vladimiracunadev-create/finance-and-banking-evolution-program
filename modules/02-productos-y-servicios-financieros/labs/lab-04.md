# Laboratorio 4: Crédito hipotecario

## Propósito

Medir el efecto de medio punto de tasa a veinte años y **comparar el prepago temprano con el tardío**.

Los laboratorios anteriores trataron plazos cortos. Este multiplica todo por veinte años, que es donde las diferencias pequeñas se vuelven grandes.

## Escenario

Un crédito de 80 000 000 a 20 años, con dos ofertas que difieren en medio punto de tasa y en sus gastos operacionales.

## Datos

Las dos ofertas con su tasa, sus gastos y su unidad de cuenta.

## Supuestos del ejercicio

- El crédito se expresa en una unidad indexada que se reajusta con la inflación.
- La inflación supuesta es del 3,2 % anual y se declara como supuesto.
- El prepago se imputa a capital reduciendo plazo.

## Pasos

1. Calcula la cuota de las dos ofertas y su costo total a 20 años.
2. Cuantifica el efecto de medio punto de tasa en pesos y en años de cuota.
3. Suma los gastos operacionales y recalcula cuál oferta conviene.
4. Aplica un prepago de 8 000 000 en el año 3 y en el año 12, y compara el ahorro.
5. Calcula el efecto del reajuste sobre la cuota si la inflación supera lo supuesto.
6. Determina la relación préstamo/valor y qué exige cada tramo.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Las dos ofertas están comparadas por costo total | No por cuota |
| 2 | El efecto de medio punto está cuantificado | En pesos |
| 3 | Los gastos operacionales están sumados | Y cambian o no la conclusión |
| 4 | Los dos prepagos están comparados | Temprano frente a tardío |
| 5 | El riesgo de reajuste está cuantificado | Con un escenario de inflación mayor |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Comparar por la cuota | La cuota menor puede ser la oferta más cara |
| Omitir los gastos operacionales | Cambian el orden de las ofertas |
| Suponer que el prepago rinde igual en cualquier momento | El temprano ahorra mucho más |
| Ignorar la unidad indexada | La cuota sube con la inflación aunque el sueldo no |

## Entregables

- `solution.md` con las dos ofertas comparadas por costo total.
- El efecto de medio punto en pesos y en años.
- La comparación de los dos prepagos.
- El escenario de inflación mayor con su efecto sobre la cuota.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Comparación por costo total | 25 |
| Efecto de la tasa | 20 |
| Gastos incluidos | 15 |
| Prepagos comparados | 25 |
| Riesgo de reajuste | 15 |
