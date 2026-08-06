# Solución de referencia — Laboratorio 6: conformidad y seguridad

> Material docente.

## Las cuatro familias y sus casos mínimos

### Autorización (4 casos)

| Caso | Petición | Resultado esperado |
|---|---|---|
| A1 | `/authorize` sin `code_challenge` | `invalid_request` |
| A2 | `redirect_uri` con sufijo añadido | `invalid_request`, sin redirigir |
| A3 | Canje del mismo código dos veces | Segundo: `invalid_grant` |
| A4 | Token con alcance no concedido | `403 resource_forbidden` |

### Contrato (4 casos)

| Caso | Petición | Resultado esperado |
|---|---|---|
| C1 | `limit=100000` | Acotado al máximo documentado |
| C2 | `cursor` manipulado | `400 invalid_request`, no `500` |
| C3 | `from` posterior a `to` | `400 invalid_request` |
| C4 | Campo obligatorio ausente en el pago | `400`, con el campo nombrado |

### Seguridad (4 casos)

| Caso | Petición | Resultado esperado |
|---|---|---|
| S1 | Token de otro cliente | `401 invalid_token` |
| S2 | Consentimiento revocado | `403 consent_revoked` |
| S3 | Cuenta inexistente frente a cuenta ajena | **Respuestas idénticas** |
| S4 | Error provocado en el servidor | Sin traza interna en el cuerpo |

### Resiliencia (4 casos)

| Caso | Petición | Resultado esperado |
|---|---|---|
| R1 | 5 reintentos con la misma clave | Un solo cargo |
| R2 | Misma clave, cuerpo distinto | `409 idempotency_conflict` |
| R3 | Superar el límite de tasa | `429` con `Retry-After` |
| R4 | Origen no disponible | `503 provider_unavailable`, no `500` |

## El caso S3, que es el que más implementaciones falla

```python
def test_no_se_puede_enumerar_cuentas(cliente):
    ajena = cliente.get("/v1/accounts/acc_de_otro_cliente")
    inexistente = cliente.get("/v1/accounts/acc_que_no_existe")

    assert ajena.status_code == inexistente.status_code
    assert ajena.json()["code"] == inexistente.json()["code"]
    assert ajena.json()["message"] == inexistente.json()["message"]
```

Si la implementación devuelve `403` para la ajena y `404` para la inexistente, un
atacante recorre el espacio de identificadores y obtiene la lista de cuentas que
existen en la institución. El defecto no está en ninguna de las dos respuestas por
separado: está en la diferencia.

## Informe de conformidad: estructura mínima

```text
INFORME DE CONFORMIDAD
  implementación:        open_finance_sandbox
  versión del contrato:  1.0.0
  fecha de ejecución:    2026-08-06
  casos ejecutados:      16    aprobados: 15    fallidos: 1

FALLO
  S3 · enumeración de cuentas
     esperado: respuestas idénticas
     obtenido: 403 para cuenta ajena, 404 para inexistente
     efecto:   permite enumerar identificadores válidos
     estado:   abierto

FUERA DE ALCANCE (declarado)
  · TLS y autenticación mutua: el entorno los simula
  · certificados de una autoridad real
  · pruebas de carga sostenida (solo ráfaga de 60 s)
  · comportamiento bajo partición de red
```

La sección «fuera de alcance» es obligatoria. Un informe que no la tiene se lee
como cobertura completa, y esa lectura es la que produce incidentes.

## Latencia

```text
GET /v1/accounts/{id}/transactions?limit=100
  p50:  34 ms
  p95: 118 ms
  p99: 265 ms
  n = 3 000 peticiones, 60 s, concurrencia 20
```

Se reportan `n`, duración y concurrencia junto a los percentiles: sin esos tres
datos los percentiles no son comparables con nada.

## Límites de la propia batería

- Prueba la implementación contra su contrato, no contra la norma. Que la batería
  pase no significa que la actividad esté autorizada.
- No cubre la capa de transporte ni la gestión de certificados.
- Los datos son sintéticos: no detecta problemas que solo aparecen con
  distribuciones reales de volumen y de longitud de historial.
