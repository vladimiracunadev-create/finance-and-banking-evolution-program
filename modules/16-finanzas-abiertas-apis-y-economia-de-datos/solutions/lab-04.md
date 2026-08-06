# Solución de referencia — Laboratorio 4: iniciación de pagos

> Material docente.

## Orden y pago no son lo mismo

| | Orden de pago | Pago |
|---|---|---|
| Quién la crea | El iniciador, con el consentimiento del cliente | La institución |
| Qué representa | La intención autorizada | La ejecución |
| Cuántas hay | Una por `Idempotency-Key` | Una por orden aceptada |
| Se puede repetir | Sí, la petición | No, el efecto |

El reintento repite la **petición de creación de la orden**. Si el servidor ya la
creó, devuelve la misma orden. Nunca crea una segunda.

## Idempotencia: las tres ramas

```python
def crear_pago(key: str, cuerpo: dict) -> Respuesta:
    huella = sha256(canonical_json(cuerpo))
    with bloqueo(key):                      # sin el bloqueo hay carrera
        registro = almacen.get(key)
        if registro is None:
            respuesta = ejecutar(cuerpo)
            almacen.put(key, huella, respuesta)
            return respuesta
        if registro.huella != huella:
            raise Conflicto("idempotency_conflict")   # 409
        return registro.respuesta                     # misma respuesta, 200
```

Tres detalles que la corrección busca:

1. **`canonical_json`**: sin canonicalizar, `{"a":1,"b":2}` y `{"b":2,"a":1}`
   producen huellas distintas y un reintento legítimo daría `409`.
2. **Bloqueo por clave**: dos reintentos simultáneos entran a la vez si no hay
   bloqueo, y ambos ven `registro is None`.
3. **Se guarda la respuesta, no solo el identificador**: el cliente que reintenta
   necesita el mismo cuerpo, no solo el mismo id.

## Máquina de estados

```text
recibido ──► autorizado ──► aceptado ──► liquidado ──► devuelto
    │             │             │
    └──► rechazado└──► rechazado└──► rechazado

finales y no consultables: (ninguno)
finales:                    liquidado, rechazado, devuelto
consultables siempre:       todos, durante 90 días
```

`aceptado` no es `liquidado`. Es el error conceptual más frecuente: el iniciador
informa «pago realizado» al comercio cuando la institución solo aceptó la orden.
Si el pago se rechaza después, el comercio ya entregó la mercancía.

## Los tres fallos y el saldo esperado

| Fallo simulado | Qué hace el cliente | Saldo final correcto |
|---|---|---|
| Tiempo de espera tras aceptar | Reintenta con la misma clave | Un solo cargo |
| Caída antes de responder | Reintenta con la misma clave | Un solo cargo |
| Respuesta duplicada del gateway | Ignora la segunda | Un solo cargo |

La prueba correcta compara el **saldo**, no el número de respuestas `200`.

## Confirmación de fondos

```text
POST /v1/funds-confirmations
{ "account_id": "...", "amount": "45000.00", "currency": "CLP" }
→ { "funds_available": true }
```

Reglas:

- Responde **booleano**, nunca el saldo. Si devolviera el saldo, sería una API de
  información disfrazada de comprobación de pago.
- **No retiene** fondos: no es un bloqueo, es una foto del instante.
- Lleva límite de tasa propio: sin él, repetir la consulta con importes
  crecientes permite deducir el saldo por bisección.

## Límites

- No hay liquidación real: el estado `liquidado` se simula. En un sistema real
  ese estado lo determina la infraestructura de pagos, no la institución sola.
- El pago es doméstico y en una moneda. La versión transfronteriza, con sus
  estados adicionales (`en investigación`, `reparado`, `recall`), está en la
  Parte 18.
