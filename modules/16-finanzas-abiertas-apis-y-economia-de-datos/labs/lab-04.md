# Laboratorio 4: Iniciación de pagos

## Propósito

Implementar una iniciación de pago que no duplique dinero cuando la red falla.
Es el laboratorio donde la idempotencia deja de ser una palabra.

## Escenario

Un comercio integra un botón de pago que inicia una transferencia desde la cuenta
del cliente. En la primera prueba de carga, el 3 % de las peticiones da tiempo de
espera agotado; el comercio reintenta; algunos clientes pagan dos veces.

## Contexto

En una iniciación de pago hay dos entidades distintas que suelen confundirse: la
**orden** (lo que el cliente autorizó) y el **pago** (lo que la institución
ejecutó). El reintento debe repetir la orden, nunca crear una nueva.

## Datos

Cuentas sintéticas de `apps/open_finance_sandbox/bank_api/data/`.

## Supuestos del ejercicio

- Pago doméstico, misma moneda, entre cuentas del entorno simulado.
- El consentimiento de pago es **de un solo uso** y ligado al importe y al
  beneficiario.
- La autenticación reforzada ocurre dentro del flujo de autorización.
- No hay liquidación real: se simula el estado final.

## Requisitos

- Haber completado los laboratorios 1 y 2.
- Python 3.11 o superior.

## Pasos

1. Define el objeto **orden de pago**: importe, moneda, beneficiario, referencia,
   fecha de ejecución solicitada y identificador de idempotencia.
2. Exige la cabecera `Idempotency-Key` en la creación. Sin ella, `400`.
3. Guarda la huella de la petición junto con la clave. Si llega la misma clave
   con **cuerpo distinto**, responde `409`: es un error del cliente, no un
   reintento.
4. Si llega la misma clave con el mismo cuerpo, devuelve **la misma respuesta**
   que la primera vez, con el mismo identificador de pago.
5. Implementa la máquina de estados del pago:
   `recibido → autorizado → aceptado → (liquidado | rechazado | devuelto)`.
6. Define qué estados son finales y cuáles admiten consulta posterior.
7. Simula tres fallos: tiempo de espera tras aceptar, caída antes de responder y
   respuesta duplicada. Verifica que el saldo final es correcto en los tres.
8. Implementa la confirmación de fondos como operación separada, sin retención.

## Arquitectura

```text
comercio ── POST /v1/payments  (Idempotency-Key: K, cuerpo B)
              │
              ├─ K nueva          → crea orden, guarda (K, hash(B), respuesta)
              ├─ K vista, B igual → devuelve la respuesta guardada
              └─ K vista, B ≠     → 409 conflicto

estados
  recibido ─► autorizado ─► aceptado ─► liquidado
                  │              └────► rechazado
                  └──────────────────► rechazado
  liquidado ─────────────────────────► devuelto
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Sin clave de idempotencia, falla | Prueba `400` |
| 2 | Reintento idéntico no duplica | Saldo tras 5 reintentos |
| 3 | Clave reusada con otro cuerpo da `409` | Prueba de conflicto |
| 4 | Estados ilegales rechazados | Prueba por transición |
| 5 | El consentimiento de pago es de un uso | Segundo pago falla |
| 6 | La confirmación de fondos no retiene | Saldo sin cambio |

## Amenazas a considerar

| Amenaza | Efecto | Control |
|---|---|---|
| Reintento ciego | Pago duplicado | Idempotencia con huella del cuerpo |
| Manipulación del beneficiario | Desvío de fondos | Beneficiario dentro del consentimiento |
| Reutilización del consentimiento | Pago no autorizado | Consentimiento de un solo uso |
| Confirmación de fondos como sonda | Perfilado del saldo | Respuesta booleana y límite de tasa |
| Carrera entre reintentos | Doble creación | Clave única con bloqueo |

## Pruebas

```bash
python -m pytest tests/test_open_finance_sandbox.py -q -k payment
```

## Entregables

- `payment_initiation/` con la máquina de estados.
- Pruebas de los tres escenarios de fallo.
- `solution.md` con la diferencia entre orden y pago.
- Tabla de estados finales y consultables.
- Tabla de supuestos.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Idempotencia correcta | 30 |
| Máquina de estados | 25 |
| Escenarios de fallo probados | 25 |
| Confirmación de fondos bien acotada | 10 |
| Documentación de supuestos | 10 |

## Solución de referencia

En [`solutions/lab-04.md`](../solutions/lab-04.md).
