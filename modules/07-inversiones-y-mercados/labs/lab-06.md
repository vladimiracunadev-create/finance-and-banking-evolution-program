# Laboratorio 6: Proyecto: cartera simulada

## Propósito

Construir la cartera y **llevar bitácora de cada decisión con la información que había en ese momento**.

Es el último laboratorio de la parte y la antesala del proyecto. Sin bitácora, al final no se puede distinguir el criterio de la suerte, y eso es lo único que se evalúa.

## Escenario

Una cartera para el perfil elegido en el laboratorio 1, seguida durante ocho periodos con información que llega con rezago.

## Datos

El perfil, el universo de instrumentos y las series de los ocho periodos.

## Supuestos del ejercicio

- Cada decisión se registra con la información disponible en ese momento.
- Los costos de transacción y las comisiones se aplican en cada operación.
- El rebalanceo sigue la política escrita, no la intuición del periodo.

## Pasos

1. Define la asignación estratégica desde el perfil del laboratorio 1.
2. Selecciona instrumentos y calcula el costo total de propiedad de la cartera.
3. Registra cada decisión con su fecha, su razón y la información disponible.
4. Aplica la política de rebalanceo cuando corresponda y anota el costo.
5. Al final, calcula el resultado y sepáralo entre asignación, selección y sincronización.
6. Evalúa cada decisión por su proceso y no por su resultado.
7. Identifica una decisión que salió bien y fue un error de proceso.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | La asignación deriva del perfil | No al revés |
| 2 | El costo total de propiedad está calculado | Con todos sus componentes |
| 3 | Cada decisión está en la bitácora | Con la información del momento |
| 4 | El resultado está atribuido | Asignación, selección y sincronización |
| 5 | La decisión correcta por suerte está identificada | Con su explicación |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Elegir instrumentos antes que la asignación | El orden decide el resultado |
| Registrar la razón después | Es una justificación, no una bitácora |
| Evaluar solo por rentabilidad | Una decisión mala puede salir bien |
| Rebalancear por intuición | Eso es cambiar de opinión, no rebalancear |

## Entregables

- `solution.md` con la asignación y su derivación del perfil.
- El costo total de propiedad de la cartera.
- La bitácora completa de los ocho periodos.
- La atribución del resultado y la decisión correcta por suerte.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Asignación derivada del perfil | 20 |
| Costo total | 15 |
| Bitácora completa | 30 |
| Atribución del resultado | 20 |
| Evaluación de proceso | 15 |
