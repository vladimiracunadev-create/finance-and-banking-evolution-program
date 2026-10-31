# Diccionario: `custody_crisis_balance_synthetic.csv`

- **Nombre:** balance de una entidad custodio de ejercicio, antes del incidente (sintético)
- **Ruta:** `datasets/synthetic/custody_crisis_balance_synthetic.csv`
- **Filas:** 8
- **Origen:** caso determinístico redactado para el laboratorio de crisis de custodia; no deriva de datos reales
- **Licencia:** CC BY-NC-SA 4.0; ver `DATA_LICENSES.md`
- **Fecha de generación:** 2026-10-30
- **Privacidad:** sin clientes, cuentas ni direcciones reales
- **Usado en:** `apps/custody_crisis_lab/`, `docs/crisis-financiera-digital.md`

## Método de generación

Se diseñó para que los activos totales (100 000 MUSD) igualen los pasivos con
clientes (100 000 MUSD), con 80 % de los activos líquidos a 24 h, y para que
reproduzca `caso_sintetico()` del laboratorio. Los importes no representan a
ninguna entidad real.

## Diccionario

| Campo | Tipo | Significado | NO significa |
|---|---|---|---|
| `line_id` | cadena | Identificador único de la línea | No identifica a un cliente |
| `side` | enumerado | `asset`, `liability` o `protection` | No es una clasificación contable formal |
| `item` | cadena | Descripción de la línea | No es una cuenta de un plan contable real |
| `liquidity` | enumerado | `liquid`, `non_liquid` o `not_applicable` | No es una calificación de mercado |
| `amount_musd` | entero | Importe en millones de USD equivalentes | No es una cotización ni un saldo real |

## Supuestos

- Todo se mide a una misma hora de corte y en una unidad común.
- «Líquido» significa realizable en 24 horas sin descuento material.
- El fondo de protección no se suma a los activos que respaldan a clientes.

## Calidad

Unicidad de `line_id`: 100 %. Activos totales igual a pasivos: sin diferencia.

## Limitaciones

- Un solo corte y una sola entidad; no hay desglose por activo ni por cliente.
- Un balance cuadrado no prueba propiedad, segregación ni disponibilidad.
- No sirve para valorar, invertir ni operar.
