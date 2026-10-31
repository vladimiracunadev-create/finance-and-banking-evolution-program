# Diccionario: `custody_crisis_scenarios_synthetic.csv`

- **Nombre:** escenarios de pérdida extraordinaria para el laboratorio de crisis de custodia (sintético)
- **Ruta:** `datasets/synthetic/custody_crisis_scenarios_synthetic.csv`
- **Filas:** 3
- **Origen:** parámetros de ejercicio redactados para el laboratorio; no derivan de datos reales
- **Licencia:** CC BY-NC-SA 4.0; ver `DATA_LICENSES.md`
- **Fecha de generación:** 2026-10-30
- **Privacidad:** sin personas ni entidades reales
- **Usado en:** `apps/custody_crisis_lab/`, `docs/crisis-financiera-digital.md`

## Método de generación

Tres severidades crecientes. `crd_002` tiene la misma proporción de fondos
congelados (≈ 48 %) que la que reportó la prensa en el caso de octubre de 2026,
aplicada a la entidad de ejercicio; es un paralelo de orden de magnitud, no una
reproducción.

## Diccionario

| Campo | Tipo | Significado | NO significa |
|---|---|---|---|
| `scenario_id` | cadena | Identificador único del escenario | No es un caso real |
| `name` | cadena | Nombre pedagógico | No es una predicción |
| `stolen_musd` | entero | Sustraído S en MUSD | No es pérdida definitiva |
| `frozen_musd` | entero | Congelado F en MUSD (F ≤ S) | No es dinero recuperado |
| `restitution_prob` | decimal | Probabilidad p de restituir F | No es una probabilidad calibrada |
| `liquid_share_of_loss` | decimal | Fracción de S que sale de activos líquidos | No es una política |
| `run_base_rate` | decimal | Tasa diaria base de retiros r0 | No es un dato observado |
| `run_sensitivity` | decimal | Sensibilidad k de los retiros al deterioro | No es una ley de comportamiento |
| `pause_days` | entero | Días de pausa de retiros | No es una recomendación |
| `sale_haircut` | decimal | Descuento al vender activos no líquidos | No es una cotización |

## Supuestos

- Los parámetros son independientes entre sí y constantes en el período.
- La relación entre deterioro del respaldo y retiros es lineal.

## Calidad

Unicidad de `scenario_id`: 100 %. En todas las filas F ≤ S y 0 ≤ p ≤ 1.

## Limitaciones

- Tres escenarios no cubren la distribución de incidentes posibles.
- Los parámetros de comportamiento son hipótesis y deben re-estimarse con datos.
- No sirve para predecir el desenlace de ningún incidente real.
