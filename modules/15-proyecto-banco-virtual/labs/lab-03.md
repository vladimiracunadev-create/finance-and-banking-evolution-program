# Laboratorio 3: Motor de cuotas

## Propósito

Construir el motor de amortización y **probar los casos que rompen**: prepago, mora, reajuste y cierre en cero.

El laboratorio 2 construyó el registro. Este construye el producto principal del banco, y su valor está en los casos límite que casi ningún motor prueba.

## Escenario

Un motor que tiene que amortizar créditos en dos sistemas, con prepago, con mora y en unidad indexada.

## Datos

Las condiciones de los créditos y los casos límite a probar.

## Supuestos del ejercicio

- El sistema francés y el alemán se implementan ambos.
- El prepago se imputa a capital y admite reducir plazo o cuota.
- La unidad indexada se reajusta con un índice entregado.

## Pasos

1. Implementa la generación de la tabla en los dos sistemas.
2. Prueba que el saldo cierra exactamente en cero en ambos.
3. Implementa el prepago con sus dos modalidades y prueba las dos.
4. Implementa el devengo de mora y prueba que no capitaliza.
5. Implementa el reajuste por unidad indexada y prueba con inflación variable.
6. Prueba el caso de cuota insuficiente para cubrir el interés y comprueba que se rechaza.
7. Escribe una prueba por cada caso límite y comprueba que falla si el caso se rompe.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los dos sistemas están implementados | Con su tabla |
| 2 | El cierre en cero está probado | En ambos |
| 3 | Las dos modalidades de prepago funcionan | Con su prueba |
| 4 | La mora no capitaliza | Comprobado por prueba |
| 5 | La cuota insuficiente se rechaza | En vez de producir amortización negativa |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Redondear sin ajustar la última cuota | El saldo no cierra en cero |
| Capitalizar la mora | En muchas jurisdicciones está prohibido |
| Permitir cuota menor que el interés | Produce amortización negativa silenciosa |
| Probar solo el camino feliz | Los casos límite son los que rompen en producción |

## Entregables

- `solution.md` con las decisiones de implementación.
- El motor con sus pruebas en verde.
- Las pruebas de los cinco casos límite.
- El caso de cuota insuficiente y su rechazo.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Dos sistemas | 20 |
| Cierre en cero | 20 |
| Prepago | 20 |
| Mora sin capitalizar | 20 |
| Casos límite probados | 20 |
