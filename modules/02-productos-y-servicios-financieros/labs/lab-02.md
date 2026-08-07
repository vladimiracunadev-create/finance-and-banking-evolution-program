# Laboratorio 2: Tarjetas de débito

## Propósito

Reconstruir la cronología de una operación con retención y devolución, y **explicar por qué la devolución tarda más que el cargo**.

El laboratorio 1 verificó dónde está el dinero. Este sigue el dinero en movimiento, y resuelve de una vez la confusión que más reclamos genera en el mostrador.

## Escenario

Una operación en un hotel con preautorización de 350 000, consumo final de 210 000 y devolución de la diferencia, más un cargo duplicado por un fallo de red.

## Datos

La secuencia de mensajes de la operación con sus horas.

## Supuestos del ejercicio

- La preautorización retiene fondos sin cobrarlos.
- La captura se envía al cierre del comercio.
- El cargo duplicado se produce por un reintento no idempotente.

## Pasos

1. Sitúa cada mensaje en la cadena: autorización, captura y liquidación.
2. Marca el saldo contable y el saldo disponible después de cada paso.
3. Explica por qué el disponible baja antes de que el comercio cobre.
4. Sigue la devolución y calcula cuántos días tarda en estar disponible.
5. Localiza el cargo duplicado y determina en qué etapa se produjo.
6. Escribe el protocolo que seguirías ante el cargo no reconocido, con sus plazos.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los tres momentos están separados | Con su hora |
| 2 | Los dos saldos se siguen en paralelo | Contable y disponible |
| 3 | La demora de la devolución se explica | Por la etapa, no por el banco |
| 4 | El cargo duplicado se localiza | En su etapa |
| 5 | El protocolo tiene plazos | Los de la red |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Tratar el cargo y la captura como lo mismo | Están separados por días |
| Confundir saldo contable con disponible | Es el origen de casi todos los reclamos |
| Reclamar sin plazo | El contracargo tiene plazos cortos y tasados |
| Suponer que la devolución es inmediata | Recorre la cadena en sentido inverso |

## Entregables

- `solution.md` con la cronología completa y los dos saldos.
- La explicación de la demora de la devolución.
- La etapa donde se produjo el cargo duplicado.
- El protocolo de reclamo con sus plazos.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Cronología correcta | 25 |
| Dos saldos en paralelo | 25 |
| Demora explicada | 20 |
| Duplicado localizado | 15 |
| Protocolo con plazos | 15 |
