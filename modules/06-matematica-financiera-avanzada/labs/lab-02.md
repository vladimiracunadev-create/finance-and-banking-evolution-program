# Laboratorio 2: Anualidades vencidas

## Propósito

Resolver los cuatro despejes sobre el mismo contrato y **cerrar el circuito comprobando que el cuarto devuelve el dato del primero**.

El laboratorio 1 alineó las tasas. Este valora series de flujos, que es la operación que sostiene la valoración de bonos, créditos y proyectos del resto del programa.

## Escenario

Un contrato que paga 1 800 000 al año durante doce años, con una variante diferida a tres años y otra creciente al 4 % anual.

## Datos

El contrato base y sus dos variantes.

## Supuestos del ejercicio

- Los pagos son al final de cada periodo.
- La tasa de descuento es del 8,5 % anual.
- En la variante creciente, el primer pago no crece.

## Pasos

1. Calcula el valor presente y el valor futuro del contrato base.
2. Despeja la cuota conocido el valor presente, y el plazo conocidos los demás.
3. Despeja la tasa por iteración y comprueba que devuelve la original.
4. Resuelve la variante diferida y explica el ajuste que exige.
5. Resuelve la variante creciente y compárala con la base.
6. Construye la tabla de factores y comprueba la relación entre el de valor presente y el de valor futuro.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los cuatro despejes están resueltos | Sobre el mismo contrato |
| 2 | El circuito cierra | La tasa despejada es la original |
| 3 | La variante diferida está resuelta | Con su ajuste explicado |
| 4 | La creciente está comparada con la base | Con la diferencia |
| 5 | La relación entre factores está comprobada | Numéricamente |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| No cerrar el circuito | Es la verificación que detecta el error |
| Descontar la diferida al plazo equivocado | El diferimiento se ajusta aparte |
| Hacer crecer el primer pago | La convención es que el primero no crece |
| Memorizar fórmulas sin la derivación | Las variantes se deducen; memorizarlas no |

## Entregables

- `solution.md` con los cuatro despejes y el cierre del circuito.
- Las dos variantes resueltas con su ajuste.
- La tabla de factores.
- La comprobación de la relación entre factores.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Cuatro despejes | 30 |
| Circuito cerrado | 20 |
| Variante diferida | 20 |
| Variante creciente | 15 |
| Relación entre factores | 15 |
