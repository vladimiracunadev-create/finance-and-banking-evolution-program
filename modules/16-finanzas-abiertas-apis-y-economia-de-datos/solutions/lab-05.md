# Solución de referencia — Laboratorio 5: panel de consentimientos

> Material docente.

## Traducción de alcances

| Alcance técnico | Texto para el cliente |
|---|---|
| `accounts:list` | «Ver qué cuentas tienes y de qué tipo son» |
| `accounts:balances` | «Ver cuánto dinero hay en cada cuenta» |
| `accounts:transactions` | «Ver tus movimientos de los últimos 12 meses» |
| `payments:initiate` | «Ordenar pagos desde tu cuenta, uno por uno, con tu confirmación» |

Criterio de corrección: el texto debe decir **qué ve o hace el tercero**, no qué
hace el sistema. «Acceso de solo lectura al recurso cuentas» describe el software;
«ver cuánto dinero hay en cada cuenta» describe la consecuencia.

## La decisión sobre la caché

Hay tres opciones y las tres son defendibles si se declaran:

| Opción | Retardo de revocación | Coste | Cuándo |
|---|---|---|---|
| Verificar en cada llamada, sin caché | 0 | Alto | Volumen bajo o medio |
| Caché con invalidación activa al revocar | ~ milisegundos | Medio | Recomendada |
| Caché con vencimiento fijo de N segundos | Hasta N | Bajo | Solo si N ≤ 5 s y se declara |

La opción indefendible es la cuarta: caché con vencimiento largo (minutos) sin
invalidación. Produce un sistema donde «revocar» significa «revocar dentro de un
rato», y eso no es lo que el cliente entendió al pulsar el botón.

Implementación de la opción recomendada:

```python
def revocar(consent_id: str, actor: str, motivo: str) -> None:
    consentimientos.update(consent_id, status="revocado",
                           revoked_at=ahora(), revoked_by=actor, reason=motivo)
    tokens.invalidar_por_consentimiento(consent_id)   # imprescindible
    cache.invalidar(f"consent:{consent_id}")          # antes de responder
    auditoria.registrar("consent.revoked", consent_id, actor, motivo)
```

El orden importa: la caché se invalida **antes** de responder al cliente. Si se
invalida después, existe una ventana en la que el panel ya dijo «revocado» y la
API todavía deja pasar.

## Invalidación de tokens

Un token de acceso opaco se invalida borrándolo del almacén. Un token
autocontenido y firmado no se puede «borrar»: hay que consultar una lista de
revocación, o emitirlo con vida muy corta y revocar el token de refresco. La
decisión debe estar escrita, porque determina el retardo real.

## Medición

```text
revocación → primer 403 efectivo
  p50:  8 ms
  p95: 21 ms
  p99: 44 ms
objetivo declarado: p99 < 100 ms
```

Un informe sin percentiles no vale: el promedio esconde precisamente el caso que
importa, que es el peor.

## Histórico

El consentimiento revocado sigue en la lista, en una sección «terminados», con:
fecha de creación, fecha de término, motivo y quién lo terminó (el cliente, la
institución o el propio proveedor). Borrar el registro elimina la prueba que
protege a las dos partes.

## Límites

- El panel del laboratorio no cubre consentimientos delegados (representantes,
  cuentas de empresa con varios firmantes), que añaden un nivel de autorización.
- El retardo medido es el del entorno simulado, sin red ni replicación
  geográfica: en producción sería mayor y debería medirse de nuevo.
