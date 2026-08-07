# Laboratorio 4: Tarjetas y adquirencia

## Propósito

Calcular la rentabilidad de los dos lados del negocio y **dimensionar la retención de garantía de un comercio con alta tasa de contracargo**.

El laboratorio 3 trató la liquidación entre bancos. Este trata el medio de pago más rentable, que tiene dos negocios opuestos dentro y un riesgo de crédito que rara vez se reconoce como tal.

## Escenario

Un banco que emite tarjetas y afilia comercios, con un comercio de venta anticipada de servicios y tasa de contracargo del 3,8 %.

## Datos

El detalle de comisiones de la red, los volúmenes y el perfil del comercio.

## Supuestos del ejercicio

- La tasa de intercambio y las comisiones de red se entregan como dato.
- El comercio vende servicios con entrega diferida a 90 días.
- El adquirente responde con su patrimonio si el comercio no está.

## Pasos

1. Calcula la rentabilidad del negocio de emisión sobre un volumen dado.
2. Calcula la rentabilidad del negocio de adquirencia sobre el mismo volumen.
3. Descompón el reparto de la comisión entre los cuatro actores.
4. Dimensiona la exposición del adquirente ante el comercio, con su entrega diferida.
5. Calcula la retención de garantía necesaria para cubrir esa exposición.
6. Determina el efecto de esa retención sobre la rentabilidad de afiliarlo.
7. Decide si afiliarlo y justifica la decisión.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Las dos rentabilidades están calculadas | Emisión y adquirencia |
| 2 | El reparto entre cuatro actores está descompuesto | Suma la comisión completa |
| 3 | La exposición está dimensionada | Con la entrega diferida |
| 4 | La retención está calculada | No estimada |
| 5 | La decisión está justificada | Con la rentabilidad tras la retención |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Tratar la adquirencia como un negocio de comisión | Tiene un riesgo de crédito real |
| Ignorar la entrega diferida | Es lo que hace peligroso al comercio |
| Fijar la retención por costumbre | Se calcula desde la exposición |
| Analizar un lado sin el otro | Es un mercado de dos lados |

## Entregables

- `solution.md` con las dos rentabilidades.
- El reparto de la comisión entre los cuatro actores.
- La exposición dimensionada y la retención calculada.
- La decisión sobre el comercio con su justificación.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Rentabilidad de emisión | 20 |
| Rentabilidad de adquirencia | 20 |
| Reparto descompuesto | 15 |
| Exposición y retención | 30 |
| Decisión | 15 |
