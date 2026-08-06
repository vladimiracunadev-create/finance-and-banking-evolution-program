# Laboratorio 1: Consentimiento granular

## Propósito

Construir un modelo de consentimiento que un supervisor pueda auditar: qué
autorizó exactamente el cliente, cuándo, sobre qué datos, por cuánto tiempo, con
qué finalidad y cómo se demuestra que lo revocó.

## Escenario

`Cuentas Claras SpA` es un agregador que quiere ofrecer un panel con los saldos y
movimientos de las cuentas que una persona tiene en cuatro instituciones. El
equipo de producto pide «acceso a todo, una vez, para siempre». Cumplimiento lo
rechaza. Tu tarea es diseñar el modelo intermedio que sí es defendible.

## Contexto

Un consentimiento no es una casilla: es un acto jurídico con alcance, plazo y
prueba. Si el alcance no está delimitado, el proveedor no puede demostrar que no
excedió lo autorizado; y si no puede demostrarlo, la carga recae sobre él.

## Datos

Usa `datasets/synthetic/open_finance_consents.csv`, incluido en el repositorio.
Diccionario en `datasets/schemas/open_finance_consents.md`.

## Supuestos del ejercicio

- Cuatro instituciones proveedoras y un proveedor de información.
- El cliente es persona natural.
- No hay iniciación de pagos en este laboratorio: solo lectura.
- Plazo máximo de vigencia: 12 meses, renovable con acto expreso del cliente.

## Requisitos

- Python 3.11 o superior. Sin dependencias externas.
- Editor de texto y un cliente HTTP cualquiera para revisar respuestas JSON.

## Pasos

1. Enumera los **datos mínimos** que el panel necesita para funcionar. Escribe la
   lista antes de mirar qué ofrece la API: así distingues necesidad de apetito.
2. Define **alcances** (`scopes`) que correspondan uno a uno con esa necesidad.
   Un alcance que agrupa dos finalidades distintas es un alcance mal diseñado.
3. Para cada alcance escribe: finalidad, dato al que da acceso, base de licitud,
   plazo propuesto y consecuencia de no otorgarlo.
4. Diseña el **objeto de consentimiento**: identificador, cliente, proveedor,
   alcances, fecha de creación, fecha de expiración, estado y versión del texto
   presentado al cliente.
5. Define la **máquina de estados**: `borrador → autorizado → vigente → (revocado
   | expirado | rechazado)`. Ningún estado puede volver atrás.
6. Especifica la **evidencia**: qué se registra en el momento de autorizar para
   poder reconstruir la decisión seis meses después.
7. Implementa `consent_model.py` con la validación del objeto y las transiciones
   de estado.
8. Escribe una prueba que demuestre que un acceso con consentimiento revocado
   **falla**, no que simplemente «no debería ocurrir».

## Arquitectura

```text
cliente
  │ 1. solicita alcances (lista explícita)
  ▼
proveedor de información
  │ 2. redirige a la institución
  ▼
institución proveedora
  │ 3. autentica y presenta los alcances
  │ 4. registra el consentimiento con su evidencia
  ▼
consentimiento vigente ──► acceso permitido, limitado al alcance
       │
       └── revocación ──► acceso denegado desde el instante siguiente
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Cada alcance tiene una única finalidad | Revisión de la tabla de alcances |
| 2 | Ningún alcance excede el dato mínimo | Comparación con el paso 1 |
| 3 | El objeto de consentimiento se valida | `pytest` sobre `consent_model.py` |
| 4 | Las transiciones ilegales fallan | Prueba negativa por transición |
| 5 | La revocación tiene efecto inmediato | Prueba de acceso posterior |
| 6 | La evidencia reconstruye la decisión | Revisión del registro |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Alcance sobredimensionado | Acceso a datos no necesarios | Alcance por finalidad |
| Consentimiento perpetuo | Pérdida de control del cliente | Plazo y renovación expresa |
| Revocación con retardo | Acceso posterior a la revocación | Verificación en cada llamada |
| Texto cambiado a posteriori | El cliente no autorizó eso | Versión del texto en la evidencia |
| Reutilización entre finalidades | Uso no consentido | Finalidad ligada al alcance |

## Pruebas

```bash
python -m pytest tests/test_open_finance_sandbox.py -q
```

Además, ejecuta manualmente:

```bash
python apps/open_finance_sandbox/consent_dashboard/cli.py demo
```

## Entregables

- `solution.md` con la tabla de alcances y su justificación.
- `consent_model.py` con validación y máquina de estados.
- Pruebas, incluidas las negativas.
- Diagrama del ciclo de vida.
- Tabla de supuestos.
- Nota de límites: qué de este modelo depende de la norma local vigente.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Diseño de alcances por finalidad | 25 |
| Ciclo de vida y transiciones | 25 |
| Evidencia y trazabilidad | 20 |
| Pruebas negativas | 20 |
| Límites y supuestos declarados | 10 |

## Solución de referencia

En [`solutions/lab-01.md`](../solutions/lab-01.md). Úsala para corregir, no para
sustituir el trabajo: la tabla de alcances correcta depende del producto que
cada estudiante haya definido en el paso 1.
