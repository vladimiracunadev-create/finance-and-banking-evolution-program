# Laboratorio 4: Alertas de fraude

## Propósito

Calibrar las alertas del banco **midiendo el costo de la fricción**, no solo el del fraude.

El laboratorio 3 construyó el producto. Este lo protege, y aplica el criterio de la Parte 14: bloquear operaciones legítimas cuesta clientes, y ese costo suele superar al del fraude.

## Escenario

El primer trimestre del banco con 84 000 operaciones, 31 fraudes confirmados y una tasa de bloqueo del 2,4 %.

## Datos

Las operaciones con su resultado real y los costos unitarios.

## Supuestos del ejercicio

- El costo de un fraude consumado se entrega como dato.
- El costo de una operación legítima bloqueada incluye el abandono estimado.
- El segmento del banco tiene poca tolerancia a la fricción.

## Pasos

1. Calcula falsos positivos y negativos en la configuración actual.
2. Cuantifica los tres costos: fraude, fricción y revisión manual.
3. Evalúa cinco configuraciones y calcula el costo total de cada una.
4. Determina la configuración de menor costo total.
5. Diseña las reglas de detección con su umbral y su justificación.
6. Implementa la lista blanca con espera y prueba que rechaza el caso que debe rechazar.
7. Escribe el protocolo de un evento masivo, distinto de la gestión ordinaria.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los dos errores están cuantificados | En la configuración actual |
| 2 | Los tres costos están calculados | Con sus unitarios |
| 3 | Las cinco configuraciones están evaluadas | Con su costo total |
| 4 | La lista blanca con espera está probada | Rechaza el alta más retirada inmediata |
| 5 | El protocolo de evento masivo está escrito | Distinto del ordinario |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Optimizar solo contra el fraude | La fricción suele costar más |
| No medir el abandono | Es la parte grande del costo de bloquear |
| Lista blanca sin espera | No sirve para nada |
| Tratar un evento masivo como muchos casos | Satura la revisión manual |

## Entregables

- `solution.md` con los dos errores y los tres costos.
- Las cinco configuraciones con su costo total.
- Las reglas de detección con su umbral justificado.
- El protocolo de evento masivo.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Errores cuantificados | 20 |
| Tres costos | 25 |
| Configuraciones evaluadas | 20 |
| Lista blanca probada | 20 |
| Evento masivo | 15 |
