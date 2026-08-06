# Diccionario: `personal_budget_synthetic.csv`

- **Nombre:** Presupuesto personal anual (sintético)
- **Ruta:** `datasets/personal_budget_synthetic.csv`
- **Filas:** 84 (12 meses × 7 categorías)
- **Origen:** generado para el programa; no procede de ninguna persona ni entidad
- **Licencia:** MIT, como el resto del repositorio
- **Fecha de generación:** 2025 (versión 1.0.0 del programa)
- **Privacidad:** sin datos personales; no hay titular, cuenta ni identificador
- **Usado en:** Parte 1 (finanzas personales) y Parte 2; ejercicios de
  porcentajes, variaciones e índices

## Método de generación

Serie mensual con una fila por combinación de mes y categoría. Los importes se
expresan en unidades monetarias enteras para evitar que el ejercicio se
convierta en un problema de redondeo antes de ser un problema de presupuesto.

## Diccionario

| Campo | Tipo | Obligatorio | Significado | NO significa |
|---|---|---|---|---|
| `month` | entero 1–12 | sí | Mes del año | No es una fecha: no hay año |
| `category` | cadena | sí | Categoría del movimiento | No es una categorización bancaria real |
| `type` | enumerado | sí | `income` o `expense` | El signo de `amount` no lo indica |
| `amount` | entero | sí | Importe del mes en esa categoría | Siempre positivo: el sentido lo da `type` |

## Supuestos

- Una sola moneda y un solo hogar.
- El importe es el **total del mes**, no un movimiento individual.
- `amount` es siempre positivo; sumar sin mirar `type` da un resultado sin
  sentido, y ese es precisamente uno de los errores que el ejercicio busca.

## Calidad

| Dimensión | Valor | Umbral |
|---|---:|---:|
| Completitud | 100 % | > 99,9 % |
| Validez de `month` | 100 % | 100 % |
| Validez de `type` | 100 % | 100 % |

## Limitaciones

- No hay variabilidad intramensual: no sirve para estudiar liquidez diaria.
- No hay eventos extraordinarios ni estacionalidad marcada.
- Es un presupuesto, no un extracto: no se puede conciliar con una cuenta.

## Verificación

```bash
python tools/validate_datasets.py
```
