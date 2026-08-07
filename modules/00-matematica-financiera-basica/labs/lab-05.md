# Laboratorio 5: Cuotas y cronogramas de pago

## Propósito

Construir una tabla de amortización que cierre en cero y **auditar una ajena que contiene un error**.

El laboratorio 4 valoró flujos conocidos. Este construye el calendario que los produce, que es la operación que aparece en casi todo crédito.

## Escenario

Un crédito de 6 000 000 a 36 cuotas y 1,45 % mensual. Después, la tabla que entrega una entidad para el mismo crédito, con una diferencia que no cuadra.

## Datos

El crédito y la tabla ajena, ambos sintéticos.

## Supuestos del ejercicio

- El sistema es francés: cuota constante.
- No hay seguros ni comisiones en esta tabla.
- El prepago se imputa a capital.

## Pasos

1. Calcula la cuota y construye la tabla completa de 36 filas.
2. Comprueba que el saldo cierra exactamente en cero.
3. Identifica el mes en que la amortización supera al interés.
4. Aplica un prepago de 500 000 en el mes 8 y recalcula, primero reduciendo plazo y después cuota.
5. Compara el ahorro de intereses de las dos opciones.
6. Audita la tabla ajena con los cinco controles y localiza el error.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | La tabla cierra en cero | Última fila, saldo exacto |
| 2 | El punto de equilibrio se identifica | Mes concreto |
| 3 | Las dos formas de prepago se comparan | Ahorro en pesos |
| 4 | El error de la tabla ajena se localiza | Fila y concepto |
| 5 | Los cinco controles se aplican | Uno a uno, con su resultado |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Redondear la cuota y no ajustar la última | El saldo no cierra en cero |
| Calcular el interés sobre el capital original | Se calcula sobre el saldo insoluto |
| Suponer que reducir cuota y reducir plazo dan lo mismo | Reducir plazo ahorra más |
| Auditar recalculando la tabla entera | Los cinco controles localizan el error sin rehacerla |

## Entregables

- `solution.md` con la tabla completa y su cierre en cero.
- El punto de equilibrio de la cuota.
- La comparación de las dos formas de prepago.
- El error de la tabla ajena, con su fila y su explicación.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Tabla correcta y cerrada | 30 |
| Punto de equilibrio | 10 |
| Prepago comparado | 25 |
| Auditoría con los cinco controles | 25 |
| Trazabilidad | 10 |
