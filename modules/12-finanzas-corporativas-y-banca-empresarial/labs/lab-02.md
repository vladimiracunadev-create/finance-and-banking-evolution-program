# Laboratorio 2: Evaluación de proyectos

## Propósito

Construir el flujo incremental de un proyecto **con canibalización y costos hundidos**, y ver cómo cambia el signo.

El laboratorio 1 midió la necesidad. Este evalúa en qué se va a usar el dinero, y su dificultad no está en el descuento sino en decidir qué flujos entran.

## Escenario

Una empresa evalúa lanzar un producto que reemplazará parcialmente a otro suyo, tras haber gastado ya 180 000 000 en desarrollo.

## Datos

Las proyecciones del producto nuevo, las del existente con y sin lanzamiento, y el gasto ya incurrido.

## Supuestos del ejercicio

- El desarrollo ya gastado no es recuperable.
- El producto existente pierde el 30 % de sus ventas si se lanza el nuevo.
- El costo de capital es del 12,4 % anual.

## Pasos

1. Construye el flujo del proyecto sin considerar la canibalización.
2. Calcula el valor actual neto con ese flujo.
3. Añade la canibalización como flujo negativo y recalcula.
4. Comprueba si el desarrollo ya gastado está incluido y sácalo si lo está.
5. Determina el costo de oportunidad de los recursos que el proyecto usa.
6. Recalcula el valor actual neto con el flujo incremental completo.
7. Identifica y valora la opción de posponer el lanzamiento un año.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | El flujo sin canibalización está construido | Con su valor actual |
| 2 | La canibalización está incorporada | Como flujo negativo |
| 3 | El costo hundido está excluido | Y se señala si estaba |
| 4 | El costo de oportunidad está incluido | Con su cálculo |
| 5 | El signo del resultado cambia | Entre el flujo ingenuo y el incremental |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Incluir el desarrollo ya gastado | No se recupera con ninguna decisión futura |
| Omitir la canibalización | El proyecto parece rentable y destruye valor |
| Ignorar el costo de oportunidad | Los recursos que usa tienen alternativa |
| No valorar la opción de esperar | Puede valer más que el proyecto |

## Entregables

- `solution.md` con los dos flujos y sus valores actuales.
- Las exclusiones e inclusiones justificadas una a una.
- El costo de oportunidad calculado.
- El valor de la opción de posponer.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Flujo incremental correcto | 30 |
| Canibalización | 20 |
| Costo hundido excluido | 20 |
| Costo de oportunidad | 15 |
| Opción de esperar | 15 |
