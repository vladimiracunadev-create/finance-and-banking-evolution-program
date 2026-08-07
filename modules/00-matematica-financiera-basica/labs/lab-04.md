# Laboratorio 4: Valor presente

## Propósito

Valorar el mismo contrato a cinco tasas distintas y **presentar el resultado como rango y no como cifra**.

El laboratorio 3 llevó dinero hacia el futuro. Este lo trae al presente, que es la operación que sostiene toda decisión de inversión del resto del programa.

## Escenario

Un contrato que paga 2 400 000 al año durante ocho años, con un pago final adicional de 6 000 000. Tres analistas proponen tasas de descuento distintas y ninguno la justifica.

## Datos

El calendario de flujos y las tres tasas propuestas, más dos de contraste.

## Supuestos del ejercicio

- Los flujos son ciertos: no hay probabilidad de impago.
- Los pagos son al final de cada año.
- No hay inflación adicional que ajustar.

## Pasos

1. Construye la tabla de factores de descuento para las cinco tasas.
2. Calcula el valor presente del contrato con cada una.
3. Tabula la dispersión entre el mínimo y el máximo, en pesos y en porcentaje.
4. Justifica por escrito qué tasa usarías y con qué criterio.
5. Presenta el resultado como rango con la precisión que el cálculo soporta.
6. Calcula qué proporción del valor aporta el pago final.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los cinco valores presentes están calculados | Con la tabla de factores |
| 2 | La dispersión se cuantifica | En pesos y en porcentaje |
| 3 | La tasa elegida se justifica | Por escrito y con criterio |
| 4 | El resultado se presenta como rango | Sin céntimos |
| 5 | El peso del pago final se calcula | Como proporción del total |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Presentar el valor presente con céntimos | Comunica una precisión que el cálculo no tiene |
| Elegir la tasa sin justificar | Es la decisión que más mueve el resultado |
| Descontar el pago final al plazo equivocado | Un año de diferencia cambia mucho a ocho años |
| Ignorar la dispersión | Sin ella, el número parece exacto |

## Entregables

- `solution.md` con la tabla de factores y los cinco valores.
- La dispersión cuantificada.
- La justificación escrita de la tasa elegida.
- El resultado presentado como rango.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Cinco valoraciones correctas | 25 |
| Dispersión cuantificada | 20 |
| Tasa justificada | 25 |
| Presentación honesta | 15 |
| Peso del pago final | 15 |
