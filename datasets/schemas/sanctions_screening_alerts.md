# Diccionario: `sanctions_screening_alerts.csv`

- **Nombre:** Alertas de screening de sanciones (sintético)
- **Ruta:** `datasets/synthetic/sanctions_screening_alerts.csv`
- **Filas:** 12 000
- **Origen:** generado con `random.Random(20260806)`; semilla fija, reproducible
- **Licencia:** MIT, como el resto del repositorio
- **Fecha de generación:** 2026-08-06
- **Privacidad:** sin datos personales
- **Usado en:** Parte 18, laboratorio 4; clase 12

> **Aviso obligatorio.** Los nombres, países y entradas de lista son
> **inventados**. **No corresponden a ninguna lista oficial de sanciones ni a
> ninguna persona real**, y este conjunto **no sirve para calibrar ningún
> sistema de screening en producción**.

## Método de generación

Cada fila es una alerta con su **resolución etiquetada**, cosa que en producción
no ocurre: ahí la resolución la produce un analista. Esa etiqueta existe para
que el laboratorio pueda calcular precisión y exhaustividad y ejecutar la prueba
retrospectiva.

La proporción de verdaderos positivos es muy baja (del orden de 1 por cada
1 500 alertas) **a propósito**: reproduce el orden de magnitud del problema real,
donde la precisión de un sistema de sanciones es de fracciones de punto
porcentual y la exhaustividad es lo que manda.

## Diccionario

| Campo | Tipo | Obligatorio | Significado | NO significa |
|---|---|---|---|---|
| `alert_id` | cadena | sí | Identificador de la alerta | No identifica a una persona |
| `screened_name` | cadena | sí | Nombre tal como venía en el pago | Nombre inventado |
| `list_entry` | cadena | sí | Entrada de la lista con la que coincidió | No es una designación real |
| `score` | decimal 0–1 | sí | Puntuación de similitud | No es una probabilidad de que sea la persona |
| `date_of_birth` | fecha ISO o vacío | no | Fecha de nacimiento del pago | Vacío significa **dato ausente**, no descarte |
| `country` | ISO-3166 alfa-2 | sí | País asociado a la operación | No es la nacionalidad del titular |
| `resolution` | enumerado | sí | `true_positive` o `false_positive` | En producción no se conoce de antemano |
| `cause` | enumerado | sí | Causa del falso positivo | Trata cualquier valor desconocido como `otras` |

## Supuestos

- Solo se modela el componente de **nombres**. El de comportamiento, que tiene
  su propia calibración, queda fuera.
- La etiqueta de resolución es correcta por construcción; en la realidad la
  revisión humana introduce su propio error.
- Un `date_of_birth` vacío significa que el dato **no llegó en el mensaje**, no
  que la persona no lo tenga. Es el caso que obliga a escalar en vez de
  descartar.

## Calidad

| Dimensión | Valor | Umbral |
|---|---:|---:|
| Completitud de campos obligatorios | 100 % | > 99,9 % |
| Unicidad de `alert_id` | 100 % | 100 % |
| Validez de `score` (0–1) | 100 % | 100 % |
| Validez de `resolution` | 100 % | 100 % |

## Limitaciones

- **No sirve para calibrar un sistema real.** La distribución de nombres, la
  frecuencia de apellidos y la composición de las listas oficiales son distintas.
- No contiene entidades jurídicas, alias, ni variantes de escritura no latina,
  que son una parte importante del problema real.
- La proporción de verdaderos positivos es un supuesto del ejercicio.
- Un modelo entrenado sobre este conjunto produciría resultados sin validez
  fuera del laboratorio.

## Verificación

```bash
python tools/validate_datasets.py && python tools/detect_pii.py
```
