# Laboratorio 4: Factoraje y confirmación de pagos

## Propósito

Comparar factoraje con recurso y sin recurso, y **comprobar que la diferencia de precio es exactamente el riesgo transferido**.

Los laboratorios anteriores financiaron con el balance. Este financia contra un cobro concreto, donde una diferencia jurídica que parece técnica decide quién asume la pérdida.

## Escenario

Una empresa con 340 000 000 en facturas a 90 días de cinco deudores, uno de ellos con calificación deteriorada.

## Datos

La cartera de facturas con su deudor, su plazo y la calificación de cada uno.

## Supuestos del ejercicio

- Las probabilidades de impago por calificación se entregan como dato.
- El aforo aplicado es del 85 % en ambas modalidades.
- La dilución histórica de la empresa se entrega como dato.

## Pasos

1. Calcula el anticipo que recibe la empresa en ambas modalidades.
2. Calcula el costo financiero de cada una y expresa la diferencia.
3. Estima la pérdida esperada de la cartera con las probabilidades dadas.
4. Compara la diferencia de precio con la pérdida esperada transferida.
5. Evalúa el efecto de la dilución sobre el aforo necesario.
6. Diseña una operación de confirmación de pagos y explica la inversión de riesgo.
7. Determina qué modalidad conviene a la empresa y cuál al banco, y por qué difieren.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los dos anticipos están calculados | Con el aforo |
| 2 | El costo de cada modalidad está calculado | Con su diferencia |
| 3 | La pérdida esperada está estimada | Con las probabilidades |
| 4 | La diferencia se compara con la pérdida transferida | Y se explica |
| 5 | La confirmación de pagos está diseñada | Con su inversión de riesgo |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Comparar solo por la tasa | La modalidad decide quién asume el impago |
| Ignorar la dilución | Reduce el cobro efectivo sin que haya impago |
| Aplicar el mismo aforo a deudores distintos | El aforo se calibra por riesgo |
| Confundir factoraje con confirmación | El riesgo evaluado es de partes distintas |

## Entregables

- `solution.md` con las dos modalidades comparadas.
- La pérdida esperada frente a la diferencia de precio.
- El efecto de la dilución sobre el aforo.
- El diseño de la confirmación de pagos.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Anticipos y costos | 25 |
| Pérdida esperada | 20 |
| Comparación con el precio | 25 |
| Dilución y aforo | 15 |
| Confirmación diseñada | 15 |
