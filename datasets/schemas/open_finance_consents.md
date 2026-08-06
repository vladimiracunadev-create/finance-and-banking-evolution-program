# Diccionario: `open_finance_consents.csv`

- **Nombre:** Consentimientos de finanzas abiertas (sintético)
- **Ruta:** `datasets/synthetic/open_finance_consents.csv`
- **Filas:** 1 200
- **Origen:** generado con `random.Random(20260806)`; semilla fija, reproducible
- **Licencia:** MIT, como el resto del repositorio
- **Fecha de generación:** 2026-08-06
- **Privacidad:** ningún dato corresponde a una persona real; los identificadores
  de cliente son secuenciales y no se corresponden con ningún padrón
- **Usado en:** Parte 17, laboratorios 1 y 5; clases 5 y 12

## Método de generación

Cada fila es un consentimiento con su ciclo de vida. La generación **reproduce a
propósito los patrones que las clases analizan**, para que los ejercicios
encuentren algo que analizar:

- el 63 % de las revocaciones ocurre en los primeros 7 días (clase 5: el cliente
  descubre después lo que aceptó antes);
- el 2,4 % de los consentimientos abre el detalle de alcances (señal de fatiga);
- la mediana de tiempo en pantalla está por debajo de 4 segundos;
- `presented_scopes` puede contener más alcances que `granted_scopes`, nunca al
  revés: conceder lo que no se presentó es un defecto, no un caso de uso.

## Diccionario

| Campo | Tipo | Obligatorio | Significado | NO significa |
|---|---|---|---|---|
| `consent_id` | cadena | sí | Identificador del consentimiento | No es el identificador del cliente |
| `customer_ref` | cadena | sí | Referencia seudónima del cliente | No es un documento de identidad |
| `provider_id` | cadena | sí | Tercero que solicitó el acceso | No es la institución que custodia |
| `institution_id` | cadena | sí | Institución proveedora de información | No es el tercero solicitante |
| `purpose` | cadena | sí | Finalidad declarada al cliente | No es la categoría comercial del producto |
| `presented_scopes` | cadena, separada por `\|` | sí | Alcances **mostrados** en la pantalla | No es lo que el cliente concedió |
| `granted_scopes` | cadena, separada por `\|` | sí | Alcances **concedidos** | No es lo que se solicitó |
| `notice_version` | cadena | sí | Versión del texto que vio el cliente | No es la versión de la API |
| `auth_method` | cadena | sí | Método de autenticación en el momento del acto | No indica si fue reforzada e independiente |
| `channel` | cadena | sí | Canal de otorgamiento | — |
| `created_at` | fecha ISO | sí | Fecha de otorgamiento | — |
| `expires_at` | fecha ISO | sí | Expiración **absoluta** | No es un plazo relativo recalculable |
| `status` | enumerado | sí | `vigente`, `revocado`, `expirado`, `rechazado` | Trata cualquier valor desconocido como `otro` |
| `revoked_at` | fecha ISO o vacío | no | Fecha de revocación | Vacío no significa vigente: mira `status` |
| `revoked_by` | cadena o vacío | no | Quién revocó | — |
| `revocation_reason` | cadena o vacío | no | Motivo declarado | No es una causa verificada |
| `seconds_on_consent_screen` | decimal | sí | Segundos en la pantalla de alcances | No mide comprensión, mide exposición |
| `opened_scope_detail` | 0/1 | sí | Si abrió el detalle de alcances | — |

## Supuestos

- Un solo mercado y una sola moneda.
- Plazo máximo de vigencia de 12 meses: es un **supuesto del ejercicio**, no una
  regla universal. El plazo exigible depende de la norma local.
- Los alcances usan una nomenclatura didáctica; no reproducen literalmente los de
  ningún anexo técnico real.

## Calidad

| Dimensión | Valor | Umbral |
|---|---:|---:|
| Completitud de campos obligatorios | 100 % | > 99,9 % |
| Unicidad de `consent_id` | 100 % | 100 % |
| Consistencia `granted ⊆ presented` | 100 % | 100 % |
| Validez de fechas (`expires_at > created_at`) | 100 % | 100 % |

## Limitaciones

- Es un conjunto **sintético**: no reproduce las distribuciones reales de
  volumen, longitud de historial ni estacionalidad.
- No contiene consentimientos de titularidad compartida ni delegados, que añaden
  un nivel de autorización (clase 9).
- No sustituye datos de producción para evaluar un modelo: sirve para practicar
  el análisis, no para calibrarlo.

## Verificación

```bash
python tools/detect_pii.py
python tools/validate_datasets.py
```
