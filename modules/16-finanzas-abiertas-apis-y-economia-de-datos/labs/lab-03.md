# Laboratorio 3: API de cuentas y movimientos

## Propósito

Especificar y publicar una API de información financiera que un tercero pueda
consumir sin preguntar nada por correo: contrato explícito, paginación estable,
errores predecibles y versionado que no rompe a nadie.

## Escenario

La institución proveedora debe exponer cuentas, saldos y movimientos. El primer
borrador devuelve una lista completa sin paginar, con importes como número en
coma flotante y fechas en el formato local. Los tres son defectos que hay que
corregir antes de publicar.

## Contexto

Una API financiera se rompe casi siempre por el mismo sitio: la paginación con
desplazamiento sobre datos que cambian mientras se recorren, y la representación
de importes. Este laboratorio ataca los dos.

## Datos

`apps/open_finance_sandbox/bank_api/data/` (cuentas y movimientos sintéticos).

## Supuestos del ejercicio

- Los movimientos se ordenan por fecha de contabilización descendente.
- Existen movimientos con la misma fecha: el orden debe ser total y estable.
- El historial disponible es de 24 meses.
- La moneda del ejercicio es una sola; la multidivisa se trata en la Parte 18.

## Requisitos

- Python 3.11 o superior.
- `tools/validate_openapi.py` del repositorio.

## Pasos

1. Modela los recursos: `accounts`, `accounts/{id}/balances`,
   `accounts/{id}/transactions`.
2. Define la representación de importes como **cadena decimal** con la moneda
   en campo aparte. Justifica por qué no usas coma flotante.
3. Define fechas en formato ISO 8601 con zona horaria explícita.
4. Implementa **paginación por cursor**, no por desplazamiento. Explica en
   `solution.md` qué falla con `offset` cuando llegan movimientos nuevos.
5. Define el catálogo de errores: código, estado HTTP, mensaje para máquina y
   mensaje para persona.
6. Escribe el contrato `openapi.json` y valídalo.
7. Implementa el filtro por rango de fechas y el límite máximo de página.
8. Añade cabeceras de límite de tasa y documenta su comportamiento.

## Arquitectura

```text
GET /v1/accounts                       → lista de cuentas del consentimiento
GET /v1/accounts/{id}/balances         → saldo disponible y contable
GET /v1/accounts/{id}/transactions     → página de movimientos
     ?from=2026-01-01&to=2026-06-30
     &cursor=<opaco>&limit=100

respuesta:
{
  "data": [...],
  "meta": { "count": 100 },
  "links": { "next": "...cursor=..." }
}
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | El contrato OpenAPI valida | `python tools/validate_openapi.py` |
| 2 | Importes sin coma flotante | Revisión del esquema |
| 3 | Paginación estable | Prueba con inserción concurrente |
| 4 | Límite de página aplicado | `limit=100000` se acota |
| 5 | Errores del catálogo | Prueba por código |
| 6 | Solo devuelve lo consentido | Cuenta fuera del alcance da 403 |

## Amenazas a considerar

| Amenaza | Efecto | Control |
|---|---|---|
| Enumeración de cuentas | Descubrir cuentas ajenas | Identificador opaco y alcance |
| Extracción masiva | Copia del historial completo | Límite de tasa y de página |
| Fuga en el error | El mensaje revela existencia | Error uniforme para no autorizado |
| Redondeo | Diferencia de céntimos | Decimal en cadena |
| Cursor manipulable | Salto a datos ajenos | Cursor firmado o opaco por servidor |

## Pruebas

```bash
python tools/validate_openapi.py
python -m pytest tests/test_open_finance_sandbox.py -q -k accounts
```

## Entregables

- `openapi.json` validado.
- Implementación de los tres recursos.
- `solution.md` con la justificación de cursor frente a desplazamiento.
- Catálogo de errores.
- Pruebas, incluida la de paginación con inserción concurrente.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Contrato completo y válido | 25 |
| Paginación correcta y justificada | 25 |
| Representación de importes y fechas | 20 |
| Catálogo de errores | 15 |
| Pruebas | 15 |

## Solución de referencia

En [`solutions/lab-03.md`](../solutions/lab-03.md).
