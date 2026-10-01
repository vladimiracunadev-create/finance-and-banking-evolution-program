# Laboratorio 6: Proyecto de modelo y financiamiento

## Propósito

Transformar supuestos de un negocio en unit economics, presupuesto, proyección
de caja y necesidad de capital; después estructurar el financiamiento. El caso
se resuelve primero en papel o planilla y solo entonces se contrasta con la
aplicación existente.

Es el último laboratorio de la parte y la antesala del proyecto. Reúne costos,
capital de trabajo, inversión, escenarios y covenants en una propuesta que un
comité puede aprobar o rechazar con fundamento.

## Caso integrador: Taller Circular

Taller Circular reacondiciona pequeños equipos para clientes recurrentes. El
mercado esperado es de 5 000 clientes, pero el modelo nunca supone capturarlos
todos: ventas y capacidad salen de la adquisición y la retención mensuales.
Todos los datos son sintéticos y la unidad monetaria es deliberadamente neutra.

### INPUT

| Dato observado del caso | Valor | Unidad |
|---|---:|---|
| Mercado esperado | 5 000 | clientes |
| Clientes al inicio | 25 | clientes |
| Capacidad instalada | 500 | clientes |
| Caja disponible | 12 000 | moneda |
| Reserva mínima de caja | 3 000 | moneda |

### SUPUESTO

| Supuesto | Valor | Justificación que debe validarse |
|---|---:|---|
| Oportunidades calificadas mensuales | 140 | Capacidad comercial |
| Conversión | 20 % | Historial sintético del embudo |
| Abandono mensual | 4 % | Relación recurrente |
| Frecuencia | 2 | servicios por cliente y mes |
| Precio unitario | 45 | Tarifa del caso |
| Costo variable unitario | 18 | Insumos directos |
| OPEX fijo mensual | 3 500 | Personal e infraestructura |
| OPEX semifijo base | 800 | Capacidad del primer tramo |
| Salto semifijo | 1 200 | Cada 200 clientes adicionales |
| Adquisición mensual | 900 | Gasto atribuible a clientes nuevos |
| CAPEX inicial | 18 000 | Equipamiento con vida de 36 meses |
| Costo hundido | 1 500 | Estudio ya pagado; no entra a la decisión |
| Cobro / inventario / pago | 15 / 10 / 20 | días |
| Horizonte | 12 | meses |

## CÁLCULO manual

La planilla debe tener cuatro zonas distintas: `INPUT`, `SUPUESTO`, `CÁLCULO` y
`OUTPUT`. Se penalizan números escritos dentro de fórmulas sin referencia a la
zona de supuestos.

1. Clasifica cada costo por comportamiento, trazabilidad, relevancia y
   tratamiento: fijo/variable/semifijo, directo/indirecto,
   hundido/incremental y CAPEX/OPEX.
2. Calcula precio, ingreso y costo variable unitarios, margen de contribución,
   CAC, LTV y payback. Declara por qué las tres últimas métricas aplican en este
   caso y cuándo dejarían de aplicar.
3. Resuelve el punto de equilibrio incluyendo el tramo de costo semifijo que
   corresponde al volumen obtenido.
4. Proyecta por mes clientes retenidos, clientes nuevos, volumen, ingresos,
   costos, margen, EBITDA y resultado operativo.
5. Calcula cuentas por cobrar, inventario, proveedores, capital de trabajo y su
   variación mensual.
6. Reconcilia EBITDA con caja: resta variación de capital de trabajo y CAPEX.
7. Informa inversión inicial, capital de trabajo máximo, déficit máximo
   acumulado, runway, mes de equilibrio y necesidad de financiamiento para
   conservar la reserva mínima.
8. Sensibiliza **solo el precio** a −10 %, base y +10 %. No cambies otra celda.
9. Construye después los escenarios conservador, base y expansivo con una tabla
   que explique qué variables cambian juntas y por qué.
10. Dimensiona el financiamiento desde el peor saldo de caja y estructura un
    calendario que siga el flujo, con covenants medibles.

## Escenarios

| Variable | Conservador | Base | Expansivo |
|---|---:|---:|---:|
| Oportunidades | 80 % del base | 100 % | 120 % |
| Conversión | 85 % del base | 100 % | 110 % |
| Precio | 95 % del base | 100 % | 103 % |
| Costo variable | 110 % del base | 100 % | 97 % |
| Días de cobro | base + 15 | 15 | base − 5 |

La capacidad de 500 clientes sigue vigente en los tres escenarios. El expansivo
no puede vender por encima de una restricción física solo porque la hoja de
cálculo lo permita.

## Verificación con la aplicación

Una vez cerrada la planilla manual, ejecuta:

```bash
python apps/financial_calculators/cli.py business-model --scenario base
python apps/financial_calculators/cli.py business-model --scenario conservador
python apps/financial_calculators/cli.py business-model --scenario expansivo --format json
```

No copies la salida como solución. Compara cada diferencia contra la fórmula y
documenta si proviene de redondeo, período, clasificación o una referencia
incorrecta. La aplicación es una segunda implementación del mismo modelo.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | La trazabilidad está separada | Cada output vuelve a una fórmula y a un supuesto |
| 2 | La estructura de costos es completa | Incluye los cuatro ejes y excluye el hundido |
| 3 | Unit economics y equilibrio reconcilian | El costo semifijo corresponde al tramo |
| 4 | Resultados y caja están conectados | EBITDA, capital de trabajo y CAPEX reconcilian |
| 5 | La sensibilidad mueve una variable | Precio cambia; el resto permanece constante |
| 6 | Los escenarios son coherentes | Cada conjunto tiene causalidad documentada |
| 7 | El capital sale del peor saldo | Incluye reserva mínima y momento del déficit |
| 8 | La aplicación reproduce la lógica | Diferencias explicadas, no ocultas |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Tratar el costo hundido como inversión futura | Sesga una decisión que ya no puede cambiarlo |
| Usar EBITDA como caja | Omite capital de trabajo y CAPEX |
| Promediar el costo semifijo | Oculta el salto de capacidad |
| Forzar CAC o LTV sin recurrencia | La métrica deja de representar el negocio |
| Cambiar muchas variables en sensibilidad | No identifica el driver del resultado |
| Financiar el importe solicitado | El capital correcto sale de la caja proyectada |
| Fórmulas con números pegados | Rompen trazabilidad y actualización |

## Entregables

- `modelo.xlsx`, `.ods` o equivalente, con las cuatro zonas identificadas.
- `solution.md` con cálculos manuales, fórmulas y diferencias contra la app.
- La matriz de costos y unit economics con aplicabilidad declarada.
- La sensibilidad de precio y los tres escenarios comparados.
- La necesidad de capital, su calendario y tres covenants con holgura medida.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Trazabilidad y estructura de costos | 20 |
| Unit economics y punto de equilibrio | 20 |
| Presupuesto, resultado y caja | 25 |
| Sensibilidad y escenarios | 15 |
| Necesidad de capital y estructura | 20 |

**Total:** 100 puntos.
