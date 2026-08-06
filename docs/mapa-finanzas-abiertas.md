# Mapa de finanzas abiertas

Guía de navegación de la Parte 17: dónde está cada concepto, con qué se conecta
y qué se puede ejecutar para comprobarlo.

## El eje de la parte

```text
LAS FINANZAS ABIERTAS NO SON UNA API:
SON UN RÉGIMEN DE CONSENTIMIENTO DEL CLIENTE CON SOPORTE TÉCNICO

  el consentimiento decide QUÉ se puede acceder
  la autorización decide QUIÉN accede y CON QUÉ PRUEBA
  el contrato decide CÓMO se pide y qué se devuelve
  la responsabilidad decide QUIÉN PAGA cuando falla
```

Toda la parte es esa frase desarrollada. Si una decisión de diseño no se puede
justificar desde ahí, es una decisión de comodidad.

## Las tres capas

| Capa | Qué se comparte | ¿Consentimiento? | Riesgo dominante | Clase |
|---|---|---|---|:---:|
| Datos abiertos | Tarifas, condiciones, sucursales | No: no hay dato personal | Información desactualizada | 1 |
| Banca abierta | Cuentas, saldos, movimientos, pagos | Sí, por finalidad y con plazo | Acceso indebido, pago no autorizado | 1, 9, 10 |
| Finanzas abiertas | Todo lo anterior + crédito, seguros, inversiones | Sí, y más difícil de explicar | Inferencia sobre salud, familia y solvencia | 1, 9, 12 |

## Recorrido de la parte

```text
FUNDAMENTO          1 · qué es          2 · quién participa      3 · Chile
                             │
GOBIERNO DEL DATO   4 · clasificación y calidad
                             │
NÚCLEO              5 · CONSENTIMIENTO  ◄── todo lo demás lo hace cumplir
                             │
AUTORIZACIÓN        6 · OAuth y OIDC    7 · perfil financiero y firma
                             │
CONTRATO            8 · versionado e idempotencia
                             │
SUPERFICIE          9 · APIs de información   10 · iniciación de pagos
                             │
CONSECUENCIAS      11 · fraude y responsabilidad
                   12 · privacidad y portabilidad
                   13 · disponibilidad e incidentes
                             │
INTEGRACIÓN        14 · expediente y defensa
```

## Dónde está cada concepto

| Concepto | Clase | Laboratorio | Código |
|---|:---:|:---:|---|
| Banca abierta vs. finanzas abiertas | 1 | — | — |
| Proveedor tecnológico crítico | 2, 13 | 6 | — |
| Indicadores de madurez del ecosistema | 2 | — | — |
| Ley N.º 21.521 y sus dos bloques | 3 | — | [`regulatory/chile/ley-21521.yml`](../regulatory/chile/ley-21521.yml) |
| Lectura de una norma en siete pasos | 3 | — | — |
| Sensibilidad por inferencia | 4, 12 | 3 | — |
| Seis dimensiones de calidad del dato | 4 | 3 | — |
| Diccionario con «NO significa» | 4 | 3 | [`openapi.json`](../apps/open_finance_sandbox/bank_api/openapi.json) |
| Alcance por finalidad | 5 | 1 | `consent_dashboard` |
| Máquina de estados del consentimiento | 5 | 1 | `consent_dashboard` |
| Evidencia del acto | 5 | 1 | `consent_dashboard` |
| Revocación con efecto | 5 | 5 | `consent_dashboard`, `authorization_server` |
| Fatiga de consentimiento | 5 | 1 | `datasets/synthetic/open_finance_consents.csv` |
| Flujo de código y PKCE | 6 | 2 | `authorization_server` |
| Validación del token de identidad | 6 | 2 | — |
| mTLS y DPoP | 7 | 2 | — |
| Objeto de petición firmado | 7 | 2 | — |
| Rotación de claves T0/T1/T2 | 7 | 2 | — |
| Cambio compatible e incompatible | 8 | 3 | `openapi.json` |
| Idempotencia con sus cuatro detalles | 8, 10 | 4 | `payment_initiation` |
| Paginación por cursor | 8 | 3 | `bank_api` |
| Cinco familias de producto | 9 | 3 | — |
| Datos de terceros en un movimiento | 9, 12 | 3 | `third_party_provider` |
| Autorización ≠ aceptación ≠ liquidación | 10 | 4 | `payment_initiation` |
| Confirmación de fondos y bisección | 10 | 4 | `payment_initiation` |
| Independencia de factores | 11 | 2 | — |
| Vinculación dinámica | 11 | 2 | — |
| Matriz de responsabilidad | 11 | — | — |
| Base de licitud, finalidad, minimización | 12 | 1 | `third_party_provider` |
| Retención por finalidad | 12 | — | — |
| SLI, SLO y SLA | 13 | 6 | — |
| Presupuesto de error | 13 | 6 | — |
| Degradar en vez de caer | 13 | 6 | — |
| Expediente en doce piezas | 14 | proyecto | — |

## Los cinco errores que la parte persigue

Aparecen una y otra vez porque son los que más cuestan:

1. **Pedir un alcance que ninguna función usa.** La prueba: «si el cliente lo
   rechaza, ¿qué deja de funcionar?».
2. **Revocar sin invalidar los tokens vivos.** El panel dice revocado y la API
   sigue autorizando.
3. **Validar `redirect_uri` por prefijo.** `app.ejemplo.cl.atacante.io` pasa el
   filtro y es otro dominio.
4. **Colapsar aceptación y liquidación en un booleano.** El comercio entrega y
   no cobra.
5. **Distinguir «cuenta ajena» de «cuenta inexistente».** La diferencia entre
   las dos respuestas permite enumerar cuentas.

Los cinco tienen una prueba negativa asociada en
[`tests/test_open_finance_sandbox.py`](../tests/test_open_finance_sandbox.py).

## Qué se puede ejecutar

```bash
python apps/open_finance_sandbox/consent_dashboard/cli.py demo
```

```bash
python apps/open_finance_sandbox/conformance_tests/run.py
```

```bash
python -m pytest tests/test_open_finance_sandbox.py -q
```

```bash
python tools/validate_openapi.py && python tools/validate_metadata.py
```

## Hacia dónde sigue

| De esta parte | A | Qué se profundiza |
|---|---|---|
| Iniciación de pagos (10) | Parte 18 | El mismo pago, entre países y monedas |
| Identidad y elegibilidad (5, 6) | Parte 21 | Restricciones de transferencia en tokenización |
| Perímetro y figuras (3) | Parte 22 | Registro, autorización y expediente |
| Todo | Parte 23 | La capa de consentimiento del banco digital |

---

**Ver también:** [Parte 17](../modules/16-finanzas-abiertas-apis-y-economia-de-datos/README.md) ·
[Etapa 5](etapa-5-finanzas-digitales.md) ·
[Open Finance Sandbox](../apps/open_finance_sandbox/README.md) ·
[Glosario de finanzas digitales](glosario-finanzas-digitales.md)
