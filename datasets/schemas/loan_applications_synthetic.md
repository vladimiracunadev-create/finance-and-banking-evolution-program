# Diccionario: `loan_applications_synthetic.csv`

- **Nombre:** Solicitudes de crédito (sintético)
- **Ruta:** `datasets/loan_applications_synthetic.csv`
- **Filas:** 100
- **Origen:** generado para el programa; ninguna fila corresponde a una persona
- **Licencia:** MIT, como el resto del repositorio
- **Fecha de generación:** 2025 (versión 1.0.0 del programa)
- **Privacidad:** sin datos personales; el identificador es secuencial
- **Usado en:** Parte 9 (análisis y gestión de crédito) y `apps/credit_scoring/`

## Método de generación

Cada fila es una solicitud con las variables mínimas para calcular carga
financiera y construir un modelo de decisión elemental. La variable `approved`
existe para poder medir un modelo, **no** para afirmar que esa decisión fue
correcta: es una etiqueta del ejercicio.

## Diccionario

| Campo | Tipo | Obligatorio | Significado | NO significa |
|---|---|---|---|---|
| `application_id` | cadena | sí | Identificador de la solicitud | No identifica al solicitante |
| `monthly_income` | entero | sí | Ingreso mensual declarado | No está verificado con documento |
| `monthly_debt` | entero | sí | Servicio de deuda mensual actual | No incluye la cuota solicitada |
| `requested_amount` | entero | sí | Monto solicitado | No es el monto aprobado |
| `term_months` | entero | sí | Plazo solicitado en meses | No es el plazo final |
| `years_employed` | entero | sí | Antigüedad laboral en años | No mide estabilidad del sector |
| `past_due_events` | entero | sí | Eventos de mora en el histórico | No indica su gravedad ni su antigüedad |
| `approved` | 0/1 | sí | Etiqueta del ejercicio | **No** es una decisión de crédito correcta |

## Supuestos

- Una sola moneda; importes mensuales salvo `requested_amount`.
- `monthly_debt` **no** incluye la cuota del crédito solicitado: calcularla es
  parte del ejercicio.
- La etiqueta `approved` se generó con una regla del ejercicio, no con una
  política real de riesgo.

## Calidad

| Dimensión | Valor | Umbral |
|---|---:|---:|
| Completitud | 100 % | > 99,9 % |
| Unicidad de `application_id` | 100 % | 100 % |
| Validez (`monthly_income > 0`) | 100 % | 100 % |

## Limitaciones

- 100 filas no bastan para entrenar ni evaluar un modelo con validez
  estadística; sirven para practicar el procedimiento.
- No hay variable temporal: no se pueden estudiar cosechas.
- No hay garantías, avales ni tipo de producto.
- **No usar para calibrar ninguna política de crédito real.**

## Verificación

```bash
python tools/validate_datasets.py
python -m pytest tests/test_scoring.py -q
```
