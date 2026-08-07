# Laboratorio 2: Presupuesto base cero

## Propósito

Construir el mismo presupuesto por tres métodos y **comprobar que dan asignaciones distintas sin que ninguno sea erróneo**.

El laboratorio 1 midió la situación. Este decide qué hacer con el excedente antes de que llegue, que es lo único que distingue un presupuesto de un registro.

## Escenario

El mismo perfil del laboratorio 1, con tres meses de gasto real y un mes con un gasto irregular grande.

## Datos

Tres meses de movimientos sintéticos con un seguro anual en el mes 2.

## Supuestos del ejercicio

- El gasto irregular se mensualiza antes de presupuestar.
- La tasa de ahorro objetivo es del 15 % del ingreso base.
- La conciliación se hace a fin de mes contra los movimientos reales.

## Pasos

1. Clasifica el gasto de los tres meses en esencial, discrecional, fijo, variable e irregular.
2. Mensualiza el gasto irregular y recalcula el gasto mensual normalizado.
3. Construye el presupuesto por base cero, por la regla 50/30/20 y por sobres.
4. Compara las tres asignaciones y explica en qué difieren y por qué.
5. Elige un método y justifica la elección por el perfil, no por preferencia.
6. Concilia el mes 3 contra lo presupuestado y clasifica cada desviación.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | El gasto está clasificado en los cinco ejes | Tabla completa |
| 2 | El gasto irregular está mensualizado | Con su cálculo |
| 3 | Los tres presupuestos están construidos | Sobre los mismos datos |
| 4 | La elección de método está justificada | Por perfil |
| 5 | La conciliación clasifica cada desviación | No solo la suma |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Presupuestar sin mensualizar lo irregular | El mes del seguro descuadra todo |
| Poner el ahorro al final | Es lo que hace que nunca quede nada |
| Categorías demasiado finas | No se sostienen al segundo mes |
| No conciliar | Sin conciliación no se aprende nada del mes anterior |

## Entregables

- `solution.md` con la clasificación de los tres meses.
- Los tres presupuestos comparados.
- La justificación del método elegido.
- La conciliación del mes 3 con sus desviaciones clasificadas.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Clasificación en cinco ejes | 20 |
| Mensualización | 15 |
| Tres presupuestos | 25 |
| Elección justificada | 20 |
| Conciliación | 20 |
