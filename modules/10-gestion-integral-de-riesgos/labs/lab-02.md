# Laboratorio 2: Riesgo de liquidez

## Propósito

Calcular la cobertura de liquidez con los supuestos regulatorios y **recalcularla con supuestos de retiro realistas**.

El laboratorio 1 midió el riesgo que tarda meses. Este mide el que puede acabar con un banco en días, y su fragilidad no está en la métrica sino en los supuestos que la alimentan.

## Escenario

Un banco con cobertura de liquidez del 128 %, fondeo concentrado en pocos depositantes mayoristas y una base minorista pequeña.

## Datos

El balance con su detalle de fondeo y la composición de sus activos líquidos.

## Supuestos del ejercicio

- Los supuestos de retiro regulatorios se entregan como dato.
- El 34 % del fondeo proviene de cinco depositantes.
- Los descuentos por nivel de activo líquido se entregan.

## Pasos

1. Clasifica los activos líquidos por nivel y aplica sus descuentos.
2. Calcula las salidas netas a 30 días con los supuestos regulatorios.
3. Obtén la cobertura de liquidez y compárala con el mínimo.
4. Recalcula con supuestos de retiro del doble para el fondeo mayorista.
5. Determina en cuántos días se agota la liquidez en el escenario severo.
6. Calcula el financiamiento estable neto y evalúa la estructura.
7. Propón dos medidas del plan de contingencia y cuantifica cuánto liberan.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los activos están clasificados y descontados | Por nivel |
| 2 | La cobertura regulatoria está calculada | Frente al mínimo |
| 3 | El escenario severo está calculado | Con supuestos duplicados |
| 4 | Los días hasta el agotamiento están calculados | En el severo |
| 5 | Las dos medidas están cuantificadas | En liquidez liberada |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Cumplir la métrica y darse por seguro | El banco pasa la regulatoria y no el escenario realista |
| Ignorar la concentración del fondeo | Cinco depositantes pueden salir el mismo día |
| No aplicar los descuentos | Un activo de nivel 2B no vale su nominal en estrés |
| Plan de contingencia sin cuantificar | No se sabe si alcanza |

## Entregables

- `solution.md` con la cobertura regulatoria y la severa.
- Los días hasta el agotamiento en el escenario severo.
- El financiamiento estable neto y la evaluación de la estructura.
- Las dos medidas de contingencia cuantificadas.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Clasificación y descuentos | 20 |
| Cobertura regulatoria | 20 |
| Escenario severo | 30 |
| Financiamiento estable | 15 |
| Contingencia cuantificada | 15 |
