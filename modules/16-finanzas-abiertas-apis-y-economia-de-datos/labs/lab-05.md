# Laboratorio 5: Panel de consentimientos

## Propósito

Construir la pantalla donde el cliente ve y revoca lo que autorizó, y demostrar
que la revocación tiene efecto **en el sistema**, no solo en la pantalla.

## Escenario

El regulador pregunta: «¿cómo sabe un cliente suyo qué está compartiendo, y qué
pasa exactamente en el segundo siguiente a que pulse revocar?». La respuesta
tiene que ser una demostración, no un documento.

## Contexto

El panel de consentimientos es el punto donde el modelo de finanzas abiertas se
gana o se pierde la confianza. Un panel que informa pero no ejecuta es peor que
no tener panel: crea una expectativa que el sistema incumple.

## Datos

`datasets/synthetic/open_finance_consents.csv`.

## Supuestos del ejercicio

- El cliente accede autenticado a la institución proveedora.
- Existen consentimientos vigentes, expirados y revocados.
- La revocación no borra el histórico: cambia el estado y conserva la evidencia.

## Requisitos

- Laboratorios 1 y 2 completados.
- Python 3.11 o superior.

## Pasos

1. Diseña la vista: por cada consentimiento, quién accede, a qué, desde cuándo,
   hasta cuándo y cuándo fue el último acceso.
2. Traduce los alcances técnicos a lenguaje comprensible. `accounts:read` no es
   una explicación; «ver el saldo y los movimientos de tus cuentas» sí.
3. Implementa la revocación: cambia el estado, registra el instante y el actor.
4. Invalida los tokens vivos asociados al consentimiento. Una revocación que
   deja tokens válidos hasta que expiren **no es una revocación**.
5. Implementa la comprobación de estado en cada llamada a la API de recursos.
6. Mide el retardo entre la revocación y el primer rechazo efectivo. Documenta
   el valor obtenido y el objetivo.
7. Añade el histórico: consentimientos terminados, con su motivo.
8. Escribe la prueba que revoca y, sin esperar, intenta acceder.

## Arquitectura

```text
panel ── POST /consents/{id}/revoke
             │
             ├─ estado := revocado, revoked_at := ahora
             ├─ invalida tokens del consentimiento
             └─ registra actor, canal y motivo
                        │
API de recursos ── verifica estado del consentimiento en CADA llamada
                        └─ revocado ⇒ 403, sin excepción de caché
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Alcances explicados en lenguaje claro | Revisión de textos |
| 2 | Revocación cambia el estado | Consulta posterior |
| 3 | Tokens vivos quedan inválidos | Llamada con token previo da 403 |
| 4 | Verificación en cada llamada | Inspección del código y prueba |
| 5 | Histórico conservado | El consentimiento revocado sigue listado |
| 6 | Retardo medido y documentado | Informe con el número |

## Amenazas a considerar

| Amenaza | Efecto | Control |
|---|---|---|
| Caché de estado | Acceso tras revocar | Verificación sin caché o con invalidación |
| Token de larga vida | Ventana de acceso indebido | Invalidación explícita |
| Revocación no autenticada | Denegación de servicio al cliente | Autenticación en el panel |
| Texto ambiguo | Consentimiento no informado | Lenguaje verificado con usuarios |
| Borrado del histórico | Pérdida de prueba | Estado, no eliminación |

## Pruebas

```bash
python -m pytest tests/test_open_finance_sandbox.py -q -k revoke
```

## Entregables

- `consent_dashboard/` funcional.
- Tabla de traducción de alcances a lenguaje claro.
- Medición del retardo de revocación.
- Pruebas de acceso posterior a la revocación.
- `solution.md` con la decisión sobre caché y su justificación.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Revocación efectiva y verificada | 30 |
| Invalidación de tokens | 20 |
| Claridad del lenguaje del panel | 20 |
| Histórico y evidencia | 15 |
| Medición documentada | 15 |

## Solución de referencia

En [`solutions/lab-05.md`](../solutions/lab-05.md).
