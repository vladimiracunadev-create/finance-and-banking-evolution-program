# Diccionario: `remittance_corridors.csv`

- **Nombre:** Corredores de remesas y sus operadores (sintético)
- **Ruta:** `datasets/synthetic/remittance_corridors.csv`
- **Filas:** 36 (9 corredores × 4 operadores)
- **Origen:** generado con `random.Random(20260806)`; semilla fija, reproducible
- **Licencia:** MIT, como el resto del repositorio
- **Fecha de generación:** 2026-08-06
- **Privacidad:** sin datos personales; los operadores son etiquetas inventadas
- **Usado en:** Parte 18, laboratorio 5; clases 1, 9 y 10

## Método de generación

Cada fila es una ruta ofrecida por un operador en un corredor. El tipo aplicado
se genera como el de referencia menos un margen aleatorio, de modo que **el
diferencial esté siempre presente y sea siempre distinto de la comisión
anunciada**: sin esa propiedad, el laboratorio no podría demostrar que la
comisión explica menos de la mitad del precio.

Los nombres de operador (`Alfa`, `Beta`, `Gamma`, `Delta`) son deliberadamente
genéricos. **Ninguno corresponde a un operador real y las cifras no describen a
ninguno.**

## Diccionario

| Campo | Tipo | Obligatorio | Significado | NO significa |
|---|---|---|---|---|
| `corridor_id` | cadena | sí | Identificador de la fila | No identifica el corredor: eso son `origin` y `destination` |
| `origin` | cadena ISO-3166 alfa-2 | sí | País de origen del envío | No es la nacionalidad del remitente |
| `destination` | cadena ISO-3166 alfa-2 | sí | País de destino | No es la nacionalidad del receptor |
| `operator` | cadena | sí | Operador que ofrece la ruta | Nombre inventado, sin correspondencia real |
| `send_fee` | decimal | sí | Comisión de envío, en moneda de origen | No es el coste total |
| `applied_rate` | decimal | sí | Unidades de destino por unidad de origen que aplica el operador | No es el tipo de mercado |
| `reference_rate` | decimal | sí | Tipo medio de mercado en el mismo instante | No es el tipo que el cliente obtiene |
| `intermediary_fee` | decimal | sí | Comisión deducida en tránsito | Cero no significa que no haya intermediarios |
| `payout_fee` | decimal | sí | Comisión del punto de retiro, en moneda de destino | No incluye el coste de desplazamiento del receptor |
| `declared_hours` | decimal | sí | Plazo **declarado** por el operador | No es el plazo observado |
| `payout_channel` | enumerado | sí | `cuenta`, `billetera` o `efectivo` | Trata cualquier valor desconocido como `otro` |

## Supuestos

- Todos los tipos de referencia corresponden al **mismo instante**: comparar
  rutas que liquidan en momentos distintos mezclaría coste con movimiento de
  mercado.
- No se modelan promociones, primeros envíos gratuitos ni descuentos por volumen,
  que son habituales y cambian la comparación.
- Un solo tramo de conversión por fila. El diferencial cruzado del laboratorio se
  construye combinando dos filas.

## Calidad

| Dimensión | Valor | Umbral |
|---|---:|---:|
| Completitud | 100 % | > 99,9 % |
| Unicidad de `corridor_id` | 100 % | 100 % |
| Validez (`applied_rate` ≤ `reference_rate`) | 100 % | 100 % |
| Validez de `payout_channel` | 100 % | 100 % |

## Limitaciones

- **No es información de mercado.** Cualquier conclusión sobre precios reales de
  remesas debe apoyarse en la fuente citada en la clase 10.
- 36 filas no representan la estructura competitiva de ningún corredor real.
- No hay dimensión temporal: no se pueden estudiar tendencias de precio.
- El plazo es el declarado, y en la práctica es el dato que más se aparta del
  observado.

## Verificación

```bash
python tools/validate_datasets.py
```
