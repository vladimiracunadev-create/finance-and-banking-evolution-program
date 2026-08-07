# Laboratorio 3: Divisas y commodities

## Propósito

Medir el efecto del rolado durante un año en contango y **comprobar que se pierde dinero con el subyacente al alza**.

El laboratorio 2 trató un activo con flujos. Este trata los que no los tienen, donde el resultado no depende solo del precio y casi nadie lo sabe antes de invertir.

## Escenario

Un fondo de materias primas que mantiene exposición mediante futuros mensuales, durante doce meses con curva en contango.

## Datos

La curva de futuros mes a mes y el precio al contado del subyacente.

## Supuestos del ejercicio

- El subyacente sube un 9 % durante el año.
- La curva está en contango con una pendiente dada cada mes.
- El fondo rola el contrato el último día hábil de cada mes.

## Pasos

1. Calcula el resultado del fondo mes a mes con el rolado.
2. Compara el resultado anual del fondo con la variación del subyacente.
3. Aísla el retorno de rolado y exprésalo en porcentaje anual.
4. Repite el cálculo con la curva en backwardation y compara.
5. Calcula el efecto de la composición diaria en un producto apalancado dos veces.
6. Determina qué papel, si alguno, tendría este activo en la cartera del laboratorio 1.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | El resultado mes a mes está calculado | Con el rolado |
| 2 | La brecha con el subyacente está aislada | En porcentaje |
| 3 | El caso en backwardation está calculado | Y comparado |
| 4 | El efecto de la composición diaria está cuantificado | Sobre el producto apalancado |
| 5 | El papel en la cartera está decidido | Con su justificación |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Suponer que el fondo replica al subyacente | El rolado los separa |
| Ignorar la forma de la curva | Decide el signo del efecto |
| Tratar un producto apalancado como exposición constante | La composición diaria lo desvía |
| Incluirlo en la cartera sin justificar su papel | Un activo sin flujo necesita una razón |

## Entregables

- `solution.md` con el resultado mes a mes y el rolado aislado.
- La comparación entre contango y backwardation.
- El efecto de la composición diaria en el producto apalancado.
- La decisión sobre su papel en la cartera.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Resultado con rolado | 30 |
| Rolado aislado | 25 |
| Backwardation comparado | 20 |
| Composición diaria | 15 |
| Papel en la cartera | 10 |
