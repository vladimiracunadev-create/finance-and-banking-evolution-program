# Laboratorio 5: Crédito comercial y pyme

## Propósito

Ajustar los estados de una pyme con confusión patrimonial y **comprobar que los indicadores cambian de signo**.

Los laboratorios anteriores evaluaron personas. Este evalúa una empresa pequeña, donde los estados financieros necesitan ajustes antes de poder analizarse y la dependencia del dueño es el riesgo característico.

## Escenario

Una pyme con 14 000 000 de facturación anual, gastos personales del dueño registrados como de la empresa y un inmueble del socio usado sin arriendo.

## Datos

Los estados de dos ejercicios y el detalle de las partidas discutibles.

## Supuestos del ejercicio

- El dueño no recibe sueldo declarado.
- El inmueble del socio se usa sin contrato ni pago.
- Hay tres partidas de gasto claramente personales.

## Pasos

1. Identifica las partidas que requieren ajuste y clasifícalas.
2. Ajusta los estados: sueldo de mercado del dueño, arriendo de mercado del inmueble y gastos personales.
3. Recalcula los indicadores antes y después del ajuste.
4. Construye el flujo disponible para deuda con los estados ajustados.
5. Calcula la cobertura del servicio de deuda y el punto de quiebre.
6. Evalúa la dependencia del dueño y propón dos mitigantes de estructura.
7. Estructura la operación con el calendario que su flujo soporta.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Las partidas a ajustar están identificadas | Con su clasificación |
| 2 | Los tres ajustes están aplicados | Sueldo, arriendo y gastos personales |
| 3 | Los indicadores cambian y se comparan | Antes y después |
| 4 | El punto de quiebre está calculado | Sobre los estados ajustados |
| 5 | Los dos mitigantes son de estructura | No declaraciones de intención |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Analizar sin ajustar | Los indicadores de una pyme sin ajustar no significan nada |
| Olvidar el sueldo del dueño | Infla el resultado de forma sistemática |
| Tratar la dependencia del dueño como algo menor | Es el riesgo característico del segmento |
| Estructurar sin mirar el flujo | El calendario tiene que seguir a la estacionalidad |

## Entregables

- `solution.md` con las partidas ajustadas y su clasificación.
- Los indicadores antes y después.
- El flujo disponible y el punto de quiebre.
- La estructura propuesta con sus mitigantes.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Partidas identificadas | 20 |
| Ajustes aplicados | 25 |
| Indicadores comparados | 20 |
| Punto de quiebre | 20 |
| Estructura y mitigantes | 15 |
