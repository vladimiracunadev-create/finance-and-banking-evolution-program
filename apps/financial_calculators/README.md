# Calculadoras financieras

La aplicación reúne dos niveles: cálculos financieros puntuales y un modelo
empresarial mensual que convierte supuestos comerciales en resultados, caja y
necesidad de capital. No sustituye una planilla: el caso está diseñado para
resolverse primero a mano y usarse después como verificación reproducible.

```bash
python apps/financial_calculators/cli.py compound --principal 100000 --rate 0.08 --years 5
python apps/financial_calculators/cli.py loan --principal 5000000 --annual-rate 0.18 --months 36
python apps/financial_calculators/cli.py business-model --scenario base
python apps/financial_calculators/cli.py business-model --scenario conservador --format json
```

Las tasas se expresan en formato decimal: 8% = `0.08`.

## Modelo empresarial

El comando `business-model` utiliza el caso sintético **Taller Circular** de la
Parte 13. La salida separa cuatro capas para que ningún número quede sin origen:

| Capa | Contenido |
|---|---|
| `INPUT` | Identidad del caso y dato externo de mercado |
| `ASSUMPTION` | Clientes, conversión, precio, capacidad, costos y plazos |
| `CALCULATION` | Fórmulas explícitas que transforman los supuestos |
| `OUTPUT` | Unit economics, presupuesto, caja, equilibrio y capital |

El módulo clasifica costos fijos, variables y semifijos; directos e indirectos;
hundidos e incrementales; y CAPEX frente a OPEX. El costo hundido queda visible,
pero no entra a la decisión futura. CAC, LTV y payback solo se calculan cuando
existen adquisición atribuible y relación recurrente; si no, la salida explica
por qué la métrica no aplica.

Primero se muestra sensibilidad de **una sola variable** (precio -10 %, base y
+10 %). Después se comparan escenarios conservador, base y expansivo, donde los
cambios son coherentes entre demanda, conversión, precio, costo y cobranza.
