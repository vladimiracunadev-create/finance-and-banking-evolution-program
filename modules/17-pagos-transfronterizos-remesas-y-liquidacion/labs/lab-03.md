# Laboratorio 3: Mensajes ISO 20022

## Propósito

Construir, validar y encadenar los mensajes que el sistema financiero usa
realmente. Al terminar sabrás por qué un campo mal puesto convierte un pago
automático en una cola manual.

## Escenario

Tras migrar a ISO 20022, `Banco Andino` ve su tasa de procesamiento directo caer
del 88 % al 81 %. Producto quiere revertir la migración. Tu tarea es demostrar
qué está fallando realmente y corregirlo en origen.

## Contexto

Un validador de esquema comprueba que el XML esté bien formado. **Eso no basta**:
casi todos los rechazos de la migración pasan el esquema y fallan por contenido.
Este laboratorio construye el validador que sí detecta el problema.

## Datos

`apps/cross_border_payments_lab/data/messages/` — un lote de 200 mensajes
sintéticos, de los que 47 tienen defectos deliberados y documentados.

## Supuestos del ejercicio

- Se trabaja con un subconjunto de campos, no con el esquema completo.
- Los mensajes son sintéticos y ningún identificador corresponde a una entidad
  real.
- El validador comprueba estructura y contenido, no conformidad plena con las
  guías de uso vigentes.

## Requisitos

- Python 3.11 o superior; `xml.etree` de la biblioteca estándar.
- Haber leído la clase 6.

## Pasos

1. Construye un `pacs.008` completo con: identificadores, importe y divisa,
   deudor, acreedor, sus bancos, código de propósito e información de remesa.
2. Añade `UltmtDbtr` y `UltmtCdtr` cuando el caso lo requiera, y explica cuándo.
3. Valida con `tools/validate_iso20022.py`: estructura, campos obligatorios,
   formato de importe, código de divisa e identificadores.
4. Genera el `pacs.002` de aceptación y el de rechazo, con su código de motivo.
5. Modela la secuencia de cancelación: `camt.056` seguido de `camt.029`.
6. Modela la devolución: `pacs.004` con su motivo y su referencia original.
7. Procesa el lote de 200 y clasifica los 47 defectos por causa.
8. Escribe la corrección **en origen** de las tres causas más frecuentes.

## Arquitectura

```text
pacs.008 ──► validación ──┬── conforme ──► pacs.002 (ACCP)
                          │                    │
                          │                    ▼
                          │              camt.054 · camt.053
                          │
                          └── no conforme ──► pacs.002 (RJCT + código)

liquidado ──► camt.056 ──► camt.029 ──► pacs.004 (si procede)
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | El `pacs.008` valida | `tools/validate_iso20022.py` |
| 2 | Importe con formato correcto y divisa ISO | Prueba negativa por campo |
| 3 | Deudor último presente cuando aplica | Caso de plataforma de cobro |
| 4 | Rechazo con código del catálogo | Comparación con la lista |
| 5 | Cancelación antes de liquidar, devolución después | Prueba de orden |
| 6 | Los 47 defectos se detectan y clasifican | Informe del lote |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Campo truncado por un intermediario | Información del ordenante perdida | Verificación en destino |
| Referencia regenerada en el reintento | Detectado como duplicado | Referencia estable |
| Deudor último omitido | Screening incompleto | Campo obligatorio cuando aplica |
| Dirección en texto libre | Falsos positivos y reparaciones | Campos estructurados |
| Código de propósito inválido | Rechazo en destino | Tabla por corredor |
| Devolución antes de liquidar | Operación imposible | Máquina de estados |

## Pruebas

```bash
python tools/validate_iso20022.py
```

```bash
python -m pytest tests/test_cross_border_payments_lab.py -q -k iso20022
```

## Entregables

- Un `pacs.008` completo y validado.
- La cadena de estados de un pago aceptado y de uno rechazado.
- El informe del lote con los 47 defectos clasificados por causa.
- La corrección en origen de las tres causas más frecuentes.
- `solution.md` explicando por qué la caída de la tasa no era una regresión.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Mensaje completo y válido | 25 |
| Cadena de estados correcta | 20 |
| Clasificación de los 47 defectos | 25 |
| Corrección en origen | 20 |
| Explicación de la métrica | 10 |

## Solución de referencia

En [`solutions/lab-03.md`](../solutions/lab-03.md).
