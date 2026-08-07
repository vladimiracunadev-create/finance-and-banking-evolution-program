# Laboratorio 3: Ahorro y automatización

## Propósito

Diseñar el sistema de tres destinos con montos, fechas e instrumentos, y **comprobar que funciona sin que nadie tenga que acordarse**.

El laboratorio 2 dejó un excedente asignado. Este lo convierte en ahorro efectivo, y su criterio no es cuánto se ahorra sino si el mecanismo sobrevive a un mes malo.

## Escenario

El excedente del laboratorio 2, que hay que repartir entre gasto del año, imprevistos y largo plazo.

## Datos

El excedente mensual y el calendario de ingresos.

## Supuestos del ejercicio

- El ingreso llega el día 5 de cada mes.
- El fondo de emergencia objetivo es de seis meses de gasto esencial.
- Los instrumentos disponibles son los del catálogo sintético entregado.

## Pasos

1. Separa el excedente en los tres destinos con su proporción justificada.
2. Elige el instrumento de cada destino por su horizonte, no por su rendimiento.
3. Programa la transferencia para el día del ingreso y explica por qué no a fin de mes.
4. Calcula en cuántos meses se completa el fondo de emergencia.
5. Diseña la escalada: qué pasa con el excedente cuando suba el ingreso.
6. Escribe qué falla del sistema si un mes no alcanza, y qué destino cede primero.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los tres destinos tienen proporción justificada | No repartida por igual |
| 2 | Cada instrumento corresponde a su horizonte | Con su razón |
| 3 | La transferencia va el día del ingreso | Con la razón escrita |
| 4 | El plazo del fondo está calculado | En meses |
| 5 | El orden de cesión está decidido | Antes de que haga falta |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Un solo saldo para todo | El dinero de largo plazo se gasta |
| Transferir a fin de mes | Se ahorra lo que sobra, que es nada |
| Elegir instrumento por rendimiento | Un fondo a tres días no sirve para el de emergencia |
| No decidir qué cede primero | En el primer mes malo lo decide el azar |

## Entregables

- `solution.md` con el sistema de tres destinos completo.
- La elección de instrumento por horizonte, con su razón.
- El plazo de constitución del fondo de emergencia.
- El orden de cesión ante un mes insuficiente.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Tres destinos con proporción justificada | 25 |
| Instrumento por horizonte | 20 |
| Automatización con su fecha | 20 |
| Plazo del fondo | 15 |
| Orden de cesión | 20 |
