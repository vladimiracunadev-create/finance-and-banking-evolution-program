# Solución de referencia — Laboratorio 3: mensajes ISO 20022

> Material docente.

## Por qué la tasa cayó del 88 % al 81 %

Porque el sistema empezó a medir bien. Antes, el identificador de cuenta viajaba
en texto libre y el banco receptor lo corregía a mano sin devolver nada. El error
existía y nadie lo veía. Con campos estructurados, el receptor valida y rechaza.

```text
88 % «directo» con reparación invisible en destino
81 % directo con el error devuelto al origen

el 7 % de diferencia es trabajo que se hizo VISIBLE,
y volvió a quien puede corregirlo
```

La métrica correcta no es la tasa antes y después: es **cuántos pagos llegan mal
a destino**.

## Clasificación de los 47 defectos del lote

| Causa | Casos | Corrección |
|---|---:|---|
| IBAN con dígito de control erróneo | 14 | Validar en origen |
| Referencia regenerada en el reintento | 9 | Identificador estable |
| Información regulatoria en `RmtInf` | 8 | Mapear al campo correcto |
| Dirección en una sola línea | 6 | Campos estructurados |
| Código de propósito no admitido | 5 | Tabla por corredor |
| `UltmtDbtr` ausente en pago por cuenta ajena | 3 | Campo obligatorio cuando aplica |
| Divisa con código no ISO | 2 | Validación de dominio |

## Cuándo hace falta `UltmtDbtr` y `UltmtCdtr`

```text
UltmtDbtr  cuando quien paga NO es de cuya cuenta sale el dinero
           ejemplo: una gestora paga la factura de su administrada

UltmtCdtr  cuando quien cobra NO es el titular de la cuenta destino
           ejemplo: una plataforma cobra por cuenta de un vendedor
```

Omitirlos no rompe el esquema: rompe el screening y la Recomendación 16. Es el
defecto que menos se detecta en pruebas y más aparece en auditoría.

## La cadena de estados

```text
ACEPTACIÓN
  pacs.008 ──► pacs.002 (GrpSts = ACCP) ──► camt.054 ──► camt.053

RECHAZO
  pacs.008 ──► pacs.002 (GrpSts = RJCT, StsRsnInf/Rsn/Cd = AC01)

CANCELACIÓN (antes de liquidar)
  camt.056 ──► camt.029 (Cnfdntl/Cncl = aceptada o rechazada)

DEVOLUCIÓN (después de liquidar)
  pacs.004 con RtrRsnInf y referencia al pacs.008 original
```

La prueba de orden que se exige:

```python
def test_no_se_puede_devolver_antes_de_liquidar(pago):
    pago.estado = "aceptado"
    with pytest.raises(TransicionIlegal):
        pago.devolver(motivo="AC04")
```

## La referencia estable

```python
# MAL: la referencia se regenera en cada intento
def enviar(orden):
    mensaje = construir(orden, end_to_end_id=uuid4())   # ← defecto
    red.enviar(mensaje)

# BIEN: se genera al crear la orden y se conserva
def crear_orden(datos):
    return Orden(**datos, end_to_end_id=uuid4(), uetr=uuid4())

def enviar(orden):
    mensaje = construir(orden, end_to_end_id=orden.end_to_end_id)
    red.enviar(mensaje)
```

Es la idempotencia de la Parte 17, clase 8, aplicada a la mensajería. Sin ella,
el receptor detecta el reintento como duplicado por heurística de contenido.

## Retorno de las correcciones

```text
defectos evitables      33 de 47   (70,2 %)
coste por rechazo       35,75 USD  (gestión + reenvío + reclamación)
lote mensual estimado   1 900 rechazos
ahorro mensual          1 359 × 35,75 = 48 584 USD
coste de las cinco correcciones      34 000 USD
retorno                 3 semanas
```

Orden de ejecución: primero la referencia estable, porque un duplicado puede
significar un pago ejecutado dos veces, no solo un rechazo.

## Límites

- El validador cubre un subconjunto de campos, no el esquema completo ni las
  guías de uso vigentes.
- Los mensajes son sintéticos; ningún identificador corresponde a una entidad
  real.
- La conformidad plena exige la batería del esquema y del proveedor de red, que
  el laboratorio no reproduce.
