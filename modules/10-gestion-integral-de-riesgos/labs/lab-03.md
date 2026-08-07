# Laboratorio 3: Riesgo operacional

## Propósito

Construir la base de eventos de pérdida y **comprobar que las casi-pérdidas son las que más informan**.

Los laboratorios anteriores midieron riesgos con series de precios. Este mide el que se materializa en procesos y personas, cuya medición depende de datos propios que casi ninguna entidad tiene completos.

## Escenario

Una entidad con 180 eventos registrados en tres años, umbral de registro alto y ninguna casi-pérdida documentada.

## Datos

Los 180 eventos con su categoría, su importe y su fecha.

## Supuestos del ejercicio

- El umbral de registro actual es de 500 000.
- El multiplicador de pérdidas internas se calcula sobre la serie propia.
- El indicador de negocio se entrega como dato.

## Pasos

1. Clasifica los 180 eventos en las siete categorías supervisoras.
2. Analiza la distribución por categoría y por severidad.
3. Calcula el capital operacional por el método estandarizado.
4. Estima cuántos eventos quedan fuera por el umbral de registro y su efecto.
5. Diseña el registro de casi-pérdidas y explica qué información aportaría.
6. Construye tres indicadores clave de riesgo con su umbral.
7. Evalúa la proporcionalidad de tres controles: coste frente a riesgo que reducen.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los eventos están clasificados | En las siete categorías |
| 2 | El capital está calculado | Método estandarizado |
| 3 | El efecto del umbral está estimado | En eventos y en importe |
| 4 | El registro de casi-pérdidas está diseñado | Con lo que aportaría |
| 5 | Los tres controles están evaluados | Coste frente a riesgo |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Umbral de registro alto | Deja fuera la mayor parte de la distribución |
| No registrar casi-pérdidas | Es la información que revela controles que fallaron |
| Medir solo con datos propios | Los eventos extremos no están en la propia serie |
| Controles sin proporcionalidad | Un control que cuesta más que el riesgo destruye valor |

## Entregables

- `solution.md` con los eventos clasificados y su distribución.
- El capital operacional calculado.
- El efecto del umbral y el diseño del registro de casi-pérdidas.
- Los tres controles evaluados por proporcionalidad.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Clasificación | 20 |
| Capital calculado | 20 |
| Efecto del umbral | 20 |
| Casi-pérdidas diseñadas | 20 |
| Proporcionalidad | 20 |
