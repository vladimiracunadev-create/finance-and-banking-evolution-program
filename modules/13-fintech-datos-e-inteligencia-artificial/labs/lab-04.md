# Laboratorio 4: Analítica y tableros

## Propósito

Diseñar un experimento con grupo de control y **comprobar que la elevación es casi cero pese a una tasa de respuesta alta**.

El laboratorio 3 evaluó una tecnología. Este evalúa una práctica, y establece la distinción que más resultados analíticos invalida: responder no es lo mismo que responder por la campaña.

## Escenario

Una campaña de crédito preaprobado con tasa de respuesta del 11 %, muy por encima de la media histórica del 4 %.

## Datos

Los datos de la campaña, el universo elegible y el histórico sin campaña.

## Supuestos del ejercicio

- La selección de la campaña no fue aleatoria: se envió a los más propensos.
- El grupo de control se puede construir por emparejamiento.
- El margen por operación y el costo por contacto se entregan.

## Pasos

1. Traduce la pregunta de negocio a una pregunta analítica precisa.
2. Determina si la pregunta es predictiva o causal, y justifica.
3. Construye el grupo de control por emparejamiento con el universo elegible.
4. Calcula la elevación real de la campaña frente a la tasa bruta.
5. Calcula el tamaño de muestra que habría hecho falta para detectar esa elevación.
6. Determina si la campaña creó valor con el margen y el costo por contacto.
7. Diseña el experimento que habría respondido la pregunta desde el principio.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | La pregunta está traducida | Precisa y verificable |
| 2 | Se distingue predictiva de causal | Con su justificación |
| 3 | El grupo de control está construido | Por emparejamiento |
| 4 | La elevación está calculada | Frente a la tasa bruta |
| 5 | El valor creado está determinado | Con margen y costo |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Confundir tasa de respuesta con elevación | Los propensos habrían respondido igual |
| Sin grupo de control | Cualquier resultado admite varias explicaciones |
| Calcular el tamaño de muestra después | Se calcula antes o no sirve |
| Declarar éxito por el volumen | El volumen no mide el efecto de la acción |

## Entregables

- `solution.md` con la pregunta traducida y su tipo.
- El grupo de control construido y la elevación calculada.
- El tamaño de muestra necesario.
- El diseño del experimento correcto.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Pregunta traducida | 15 |
| Grupo de control | 30 |
| Elevación calculada | 25 |
| Tamaño de muestra | 15 |
| Experimento diseñado | 15 |
