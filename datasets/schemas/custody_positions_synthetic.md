# Diccionario: `custody_positions_synthetic.csv`

- **Nombre:** saldos externos de Custodia Andina Digital (sintético)
- **Ruta:** `datasets/synthetic/custody_positions_synthetic.csv`
- **Filas:** 7
- **Origen:** caso determinístico redactado para la Parte 20
- **Licencia:** CC BY-NC-SA 4.0; ver `DATA_LICENSES.md`
- **Fecha de generación:** 2026-09-07
- **Privacidad:** sin cuentas, claves ni direcciones reales
- **Usado en:** Parte 20, laboratorio 9 y `digital_assets_risk_lab`

## Método de generación

Se distribuyeron USD 7 150 000 brutos entre banco, exchange y blockchain. USD
700 000 están inmovilizados, por lo que solo USD 6 450 000 están disponibles
frente a USD 7 000 000 de obligaciones.

## Diccionario

| Campo | Tipo | Significado | NO significa |
|---|---|---|---|
| `position_id` | cadena | Identificador sintético único | No es una dirección pública |
| `asset` | enumerado | Activo valorizado | No acredita fungibilidad entre activos |
| `source` | enumerado | Banco, exchange o cadena observado | No prueba control |
| `gross_usd` | entero | Saldo visible bruto | No equivale a saldo disponible |
| `unavailable_usd` | entero | Tramo pignorado o congelado | No es necesariamente una pérdida final |
| `availability_reason` | enumerado | Razón operativa de indisponibilidad | No reemplaza evidencia contractual |
| `ownership` | enumerado | Dueño económico declarado | No es una opinión jurídica |

## Supuestos

- Todos los saldos se observan a la misma hora de corte.
- `disponible = gross_usd − unavailable_usd`.
- No se permite compensar faltantes entre activos sin modelar la conversión.

## Calidad

Completitud y unicidad de `position_id`: 100 %. Ningún tramo no disponible
supera su saldo bruto.

## Limitaciones

- Un saldo en pantalla o explorador no es prueba de propiedad ni ausencia de gravamen.
- Las valoraciones y fuentes son ficticias.
- No contiene material criptográfico ni permite mover activos.
