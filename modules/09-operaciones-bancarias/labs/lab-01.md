# Laboratorio 1: Modelo operativo de un banco

## Propósito

Recorrer una operación por las tres áreas y **encontrar el punto donde falta segregación**.

Es el primer laboratorio de la parte y el que enseña a leer cualquier proceso bancario. Casi todos los controles de las quince clases siguientes se deducen de aquí.

## Escenario

Una operación de crédito desde la solicitud en sucursal hasta su asiento contable, en un banco donde una misma persona ejecuta dos pasos que deberían estar separados.

## Datos

El flujo completo con sus pasos, sus responsables y sus sistemas.

## Supuestos del ejercicio

- Cada paso indica quién lo ejecuta y en qué sistema.
- El organigrama de las tres áreas se entrega como dato.
- El día operativo con sus cortes horarios está definido.

## Pasos

1. Sitúa cada paso en su área: front, middle o back.
2. Marca los puntos de control y quién los ejecuta.
3. Identifica el paso donde la misma persona origina y aprueba, o aprueba y registra.
4. Cuantifica la exposición de ese punto: cuánto podría moverse sin detección.
5. Propón la corrección con el menor cambio organizativo posible.
6. Ubica la operación en el día operativo y señala qué pasa si llega tras el corte.
7. Clasifica los riesgos operacionales del proceso en las siete categorías.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Cada paso está en su área | Front, middle o back |
| 2 | Los controles están marcados con su responsable | Uno a uno |
| 3 | El fallo de segregación está identificado | Con el paso concreto |
| 4 | La exposición está cuantificada | En importe |
| 5 | La corrección es mínima y viable | Sin rehacer el proceso |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Suponer segregación por el organigrama | Lo que importa es quién ejecuta cada paso |
| No cuantificar la exposición | Sin cifra, el hallazgo no prioriza |
| Proponer rehacer el proceso | La corrección mínima es la que se implanta |
| Ignorar el corte horario | Cambia la fecha valor y el riesgo |

## Entregables

- `solution.md` con el flujo por áreas y sus controles.
- El fallo de segregación con su exposición cuantificada.
- La corrección propuesta.
- Los riesgos clasificados en las siete categorías.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Flujo por áreas | 25 |
| Controles con responsable | 20 |
| Fallo identificado | 25 |
| Exposición cuantificada | 15 |
| Corrección mínima | 15 |
