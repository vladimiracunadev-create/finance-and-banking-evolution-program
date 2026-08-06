# Solución de referencia — Laboratorio 3: API de cuentas y movimientos

> Material docente.

## Importes

```json
{ "amount": "-124350.00", "currency": "CLP" }
```

Cadena decimal, no número. Razón: `0.1 + 0.2 != 0.3` en coma flotante binaria, y
un error de representación en un saldo es un descuadre contable. La moneda va en
campo aparte porque el número de decimales depende de ella, y porque un importe
sin moneda no es un importe.

## Fechas

`booking_date` (contabilización) y `value_date` (valor) en ISO 8601 con zona:
`2026-06-30T03:14:00Z`. Nunca formato local: `06/07/2026` es ambiguo entre dos
continentes.

## Paginación por cursor frente a desplazamiento

Con `offset`, si llegan tres movimientos nuevos entre la página 1 y la página 2,
los tres últimos de la página 1 se repiten en la 2 y tres se pierden. El cliente
ve importes duplicados en su categorización.

Con cursor, el servidor codifica la posición exacta:

```text
cursor = base64(booking_date + "|" + transaction_id)
orden  = (booking_date DESC, transaction_id DESC)   ← orden TOTAL
```

La clave está en que el orden sea total: si dos movimientos comparten fecha, el
desempate por identificador hace la posición inequívoca. Sin desempate, el cursor
tiene el mismo problema que el desplazamiento.

El cursor se devuelve opaco para que el cliente no dependa de su forma interna y
el servidor pueda cambiarla sin romper a nadie.

## Catálogo de errores

| HTTP | `code` | Para máquina | Para persona |
|---:|---|---|---|
| 400 | `invalid_request` | Parámetro ausente o mal formado | «Falta un dato de la petición» |
| 401 | `invalid_token` | Token ausente, expirado o inválido | «Vuelve a autorizar» |
| 403 | `consent_revoked` | Consentimiento no vigente | «Autorizaste y luego revocaste» |
| 403 | `resource_forbidden` | Fuera del alcance concedido | «No tienes acceso a ese recurso» |
| 404 | `resource_forbidden` | **Mismo código que el 403** | Igual |
| 409 | `idempotency_conflict` | Clave reusada con otro cuerpo | «Petición contradictoria» |
| 429 | `rate_limited` | Límite de tasa | «Demasiadas peticiones» |
| 503 | `provider_unavailable` | Origen no disponible | «Intenta más tarde» |

La fila 404 es la decisión de diseño relevante: **una cuenta que no existe y una
cuenta ajena deben responder lo mismo**. Si difieren, el llamante enumera cuentas
comparando respuestas.

## Contrato

```yaml
openapi: 3.1.0
info:
  title: API de informacion de cuentas
  version: "1.0.0"
paths:
  /v1/accounts:
    get:
      security: [{ oauth2: [accounts:list] }]
      responses:
        "200": { $ref: "#/components/responses/AccountList" }
```

El `security` por operación con el alcance exacto es lo que permite generar la
prueba de conformidad automáticamente.

## Límite de tasa

```text
X-RateLimit-Limit: 300
X-RateLimit-Remaining: 12
X-RateLimit-Reset: 1786000000
Retry-After: 37
```

`Retry-After` en el `429` es obligatorio: sin él, el cliente reintenta en bucle y
convierte el límite en una denegación de servicio mutua.

## Límites

- El ejercicio usa una sola moneda. Con multidivisa aparecen la fecha de valor
  por divisa y el redondeo por unidad monetaria, que se tratan en la Parte 18.
- El historial de 24 meses es un supuesto: el mínimo exigible depende de la norma
  local y debe verificarse.
