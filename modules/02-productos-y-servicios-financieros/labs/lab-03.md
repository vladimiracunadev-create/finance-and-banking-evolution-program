# Laboratorio 3: Líneas de crédito

## Propósito

Resolver la misma necesidad con tres productos y **encontrar el plazo en que se cruzan sus costos**.

El laboratorio 2 trató un medio de pago. Este trata el crédito que está disponible sin pedirlo, y su valor está en la comparación: no hay un producto mejor, hay un punto de cruce.

## Escenario

Una necesidad de 2 000 000 que puede durar 15, 60 o 180 días, resoluble con línea de crédito, tarjeta o crédito de consumo.

## Datos

Las condiciones sintéticas de los tres productos, con sus comisiones fijas y sus tasas.

## Supuestos del ejercicio

- El crédito de consumo tiene comisión de apertura y plazo mínimo de 6 meses.
- La línea cobra interés solo sobre lo usado más una comisión fija por giro.
- La tarjeta cobra la tasa rotativa desde el primer día del avance.

## Pasos

1. Calcula el costo total de cada producto a 15, 60 y 180 días.
2. Tabula los nueve resultados y ordénalos por plazo.
3. Encuentra el plazo en que la línea deja de ser la más barata.
4. Anualiza el costo efectivo de cada uno y compáralos en la misma unidad.
5. Escribe las tres reglas de uso que fijarías para la línea.
6. Determina qué producto recomendarías si el plazo es incierto y justifícalo.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los nueve costos están calculados | Tres productos por tres plazos |
| 2 | El punto de cruce está identificado | Con el plazo concreto |
| 3 | Los costos están anualizados | En la misma unidad |
| 4 | Las reglas de uso están escritas | Tres, concretas |
| 5 | La recomendación ante plazo incierto está justificada | Con su razón |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Comparar por la tasa | La comisión fija domina en plazos cortos |
| Ignorar el cupo comprometido | Consume capacidad aunque no se use |
| Usar la línea sin plazo de devolución decidido | Se convierte en deuda permanente |
| No anualizar | Un 2 % a 15 días y un 2 % a 180 no son lo mismo |

## Entregables

- `solution.md` con la tabla de nueve costos.
- El punto de cruce identificado.
- Los costos efectivos anualizados.
- Las tres reglas de uso y la recomendación justificada.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Nueve costos correctos | 30 |
| Punto de cruce | 20 |
| Anualización | 20 |
| Reglas de uso | 15 |
| Recomendación justificada | 15 |
