# Laboratorio 1: Mapa financiero personal

## Propósito

Construir el mapa con cinco indicadores y **descubrir cuál es el dato que no se tenía a mano**, que suele ser el más revelador.

Es el primer laboratorio de la parte y la línea base de todos los demás. Sin él, cualquier decisión posterior se toma sin saber desde dónde se parte.

## Escenario

Una persona con ingreso mixto, tres deudas y dos productos de ahorro quiere saber en qué situación está antes de decidir nada.

## Datos

Un perfil sintético completo, o los datos propios si se prefiere.

## Supuestos del ejercicio

- El capital humano se estima como ingreso anual por años restantes de vida laboral, descontado.
- Las deudas se registran por su saldo insoluto, no por su cuota.
- Los activos de uso se separan de los productivos.

## Pasos

1. Inventaria activos y pasivos y calcula el patrimonio neto.
2. Calcula el excedente mensual y la tasa de ahorro.
3. Calcula la carga financiera sobre la renta líquida.
4. Mide la liquidez en meses de gasto esencial cubiertos.
5. Estima el capital humano y compáralo con el patrimonio financiero.
6. Comprueba las tres señales de alerta y declara cuáles se activan.
7. Anota qué dato no tenías a mano y de dónde tuviste que obtenerlo.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los cinco indicadores están calculados | Con su fórmula visible |
| 2 | El capital humano se estima y se compara | Suele ser el mayor activo |
| 3 | Las señales de alerta se comprueban una a una | Con su resultado |
| 4 | Los activos de uso están separados | No inflan el patrimonio productivo |
| 5 | El dato que faltaba está identificado | Con su fuente |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Contar la vivienda de uso como activo productivo | No genera ingreso y no se puede gastar |
| Registrar la deuda por su cuota | El saldo insoluto es lo que se debe |
| Omitir el capital humano | En una persona joven es el activo dominante |
| Calcular la carga sobre la renta bruta | La cuota se paga con la líquida |

## Entregables

- `solution.md` con el mapa completo y sus cinco indicadores.
- El balance con activos de uso y productivos separados.
- Las tres señales de alerta con su resultado.
- El dato que faltaba y cómo se obtuvo.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Mapa completo | 30 |
| Cinco indicadores correctos | 25 |
| Capital humano estimado | 15 |
| Señales comprobadas | 15 |
| Dato faltante identificado | 15 |

> **Sobre los datos.** Si usas datos propios, no salen de tu equipo y no se
> entregan a nadie. El ejercicio se puede resolver entero con el perfil sintético.
