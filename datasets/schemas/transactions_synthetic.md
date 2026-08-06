# Diccionario: `transactions_synthetic.csv`

- **Nombre:** Transacciones con anomalías artificiales (sintético)
- **Ruta:** `datasets/transactions_synthetic.csv`
- **Filas:** 300
- **Origen:** generado para el programa; ninguna transacción es real
- **Licencia:** MIT, como el resto del repositorio
- **Fecha de generación:** 2025 (versión 1.0.0 del programa)
- **Privacidad:** sin datos personales; las cuentas son etiquetas sintéticas
- **Usado en:** Parte 14 (fraude digital), Parte 11 (riesgo operacional)

## Método de generación

Transacciones con una etiqueta `is_anomaly` insertada de forma **deliberada y
conocida**. Esa es la razón de ser del conjunto: permite medir si un método de
detección encuentra lo que se sabe que está.

## Diccionario

| Campo | Tipo | Obligatorio | Significado | NO significa |
|---|---|---|---|---|
| `transaction_id` | cadena | sí | Identificador de la transacción | No es una referencia bancaria |
| `account_id` | cadena | sí | Cuenta de cargo, seudónima | No identifica a una persona |
| `hour` | entero 0–23 | sí | Hora de la operación | No hay fecha ni zona horaria |
| `amount` | entero | sí | Importe de la operación | Siempre positivo |
| `channel` | enumerado | sí | `pos`, `web`, u otro canal | Trata cualquier valor desconocido como `otro` |
| `country_code` | cadena ISO-3166 alfa-2 | sí | País de la operación | No indica residencia del titular |
| `is_anomaly` | 0/1 | sí | Etiqueta **conocida** del ejercicio | No es una alerta real ni un fraude confirmado |

## Supuestos

- Una sola moneda.
- No hay fecha: solo hora del día. El conjunto sirve para estudiar patrones
  horarios y de canal, no series temporales.
- La proporción de anomalías es artificialmente alta respecto de la observada en
  un sistema real, para que el ejercicio tenga señal.

## Calidad

| Dimensión | Valor | Umbral |
|---|---:|---:|
| Completitud | 100 % | > 99,9 % |
| Unicidad de `transaction_id` | 100 % | 100 % |
| Validez de `hour` (0–23) | 100 % | 100 % |

## Limitaciones

- La proporción de anomalías **no** es representativa: un modelo calibrado aquí
  produciría un número inasumible de falsos positivos en producción.
- Sin fecha, sin comercio y sin contraparte: no permite estudiar inferencia
  sensible (Parte 17, clase 4).
- La etiqueta es del generador, no de una investigación: mide capacidad de
  recuperar una señal inyectada, no de detectar fraude.

## Verificación

```bash
python tools/validate_datasets.py
```
