# Laboratorio 3: Historial crediticio

## Propósito

Clasificar cinco historiales con el mismo número de eventos y **decidir distinto en cada uno**.

El laboratorio 2 midió la capacidad. Este mira el comportamiento pasado, y su dificultad está en que el informe presenta igual una mora circunstancial y un patrón.

## Escenario

Cinco solicitantes con tres eventos de mora cada uno, distribuidos de forma muy distinta en el tiempo.

## Datos

Los cinco informes completos con fechas, importes y estado actual.

## Supuestos del ejercicio

- Todos tienen el mismo número de eventos y el mismo importe acumulado.
- Uno de los cinco no tiene historial suficiente y se entrega aparte.
- Las consultas recientes se entregan como serie.

## Pasos

1. Lee los cinco informes en el orden correcto, empezando por lo que no es la morosidad.
2. Reconstruye la secuencia temporal de eventos de cada uno.
3. Clasifica cada caso entre mora circunstancial y patrón, con su criterio.
4. Analiza las consultas recientes y qué señal dan.
5. Decide sobre los cinco y justifica por qué decisiones distintas con los mismos eventos.
6. Propón la evaluación alternativa para el solicitante sin historial.
7. Determina cuánto peso darías al historial frente a la capacidad de pago.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los cinco están leídos en el orden correcto | Con lo que se mira primero |
| 2 | La secuencia temporal está reconstruida | Los cinco |
| 3 | La clasificación tiene criterio explícito | Circunstancial o patrón |
| 4 | Las consultas recientes se interpretan | Con su señal |
| 5 | El caso sin historial tiene alternativa | Que no lo excluye |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Contar eventos | El mismo número puede significar cosas opuestas |
| Rechazar por ausencia de historial | Excluye poblaciones enteras sin fundamento |
| Ignorar las consultas recientes | Muchas consultas en poco tiempo son una señal |
| Dar al historial peso absoluto | Es un insumo, no la decisión |

## Entregables

- `solution.md` con los cinco historiales clasificados.
- La secuencia temporal de cada uno.
- Las cinco decisiones con su justificación.
- La evaluación alternativa para el caso sin historial.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Lectura en orden | 15 |
| Secuencias reconstruidas | 25 |
| Clasificación con criterio | 30 |
| Consultas interpretadas | 15 |
| Alternativa sin historial | 15 |
