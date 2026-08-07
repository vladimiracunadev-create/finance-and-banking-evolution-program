# Laboratorio 6: Proyecto: motor de valoración

## Propósito

Construir el motor con **capas separadas, controles automáticos y casos de prueba** que otro pueda ejecutar.

Es el último laboratorio de la parte y la antesala del proyecto. Reúne los cinco anteriores en algo que se pueda auditar, que es lo que la Parte 11 exigirá como gestión del riesgo de modelo.

## Escenario

El motor debe valorar series de flujos, resolver los cuatro despejes, amortizar por cinco sistemas y producir sensibilidad.

## Datos

Los casos ya resueltos en los laboratorios 1 a 5.

## Supuestos del ejercicio

- Los valores esperados vienen de los cálculos manuales previos.
- Las capas de supuestos, cálculo y presentación están separadas.
- Los controles automáticos avisan cuando algo no cuadra.

## Pasos

1. Escribe los casos de prueba desde los resultados de los laboratorios 1 a 5.
2. Separa el modelo en capas: supuestos, cálculo y presentación.
3. Implementa las funciones hasta que las pruebas pasen.
4. Añade controles automáticos: cierre en cero, suma de flujos y rangos válidos.
5. Genera la sensibilidad del laboratorio 5 desde el motor.
6. Documenta el modelo: qué hace, qué supone y qué no puede hacer.
7. Pide a otra persona que lo ejecute sin explicárselo y registra dónde se traba.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Las pruebas se escribieron antes | Con valores independientes |
| 2 | Las tres capas están separadas | El cálculo se prueba sin la presentación |
| 3 | Los controles automáticos existen | Y avisan |
| 4 | La sensibilidad sale del motor | No de un cálculo aparte |
| 5 | La prueba con otra persona está registrada | Con dónde se trabó |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Supuestos incrustados en fórmulas | Impide auditar y reproducir |
| Sin controles automáticos | El error se descubre cuando ya se usó |
| Documentar después | Se documenta lo que se recuerda, no lo que se hizo |
| No probar con otra persona | El modelo se entiende solo a quien lo hizo |

## Entregables

- `solution.md` con las decisiones de diseño y la separación de capas.
- El motor con sus pruebas en verde y sus controles.
- La documentación del modelo con sus límites.
- El registro de la prueba con otra persona.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Pruebas antes que código | 20 |
| Capas separadas | 25 |
| Controles automáticos | 20 |
| Documentación con límites | 20 |
| Prueba independiente | 15 |
