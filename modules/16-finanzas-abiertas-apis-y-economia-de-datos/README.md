# Parte 17: Finanzas abiertas, APIs y economía de datos

- **Etapa:** 5 — Finanzas digitales, infraestructura y mercados tokenizados
- **Clases:** 14
- **Horas:** 21
- **Laboratorios:** 6
- **Evaluaciones:** 2
- **Proyecto:** 1

## Descripción

La Parte 14, clase 3 introdujo la banca abierta como concepto. Esta parte la
convierte en ingeniería: qué se comparte, con qué consentimiento, sobre qué
protocolo de autorización, con qué garantías criptográficas, con qué contrato de
servicio y bajo qué responsabilidad cuando algo falla.

El eje es que **las finanzas abiertas no son una API: son un régimen de
consentimiento del cliente con soporte técnico**. Toda la parte se organiza en
torno a esa distinción.

## Prerrequisitos

| Parte | Clase | Qué aporta |
|---|---|---|
| 3 | Seguridad y consumo financiero | Protección del cliente y fraude |
| 12 | Regulación, cumplimiento y auditoría | Perímetro y actividad regulada |
| 14 | 3 · Banca abierta y APIs | Concepto y modelos de implantación |
| 14 | 4 · Datos en un banco | Gobierno del dato |
| 14 | 8 · Fraude digital | Autenticación y responsabilidad |

## Resultados de aprendizaje

- Distinguir banca abierta, finanzas abiertas y datos abiertos, y explicar qué
  cambia en cada caso para el cliente, el proveedor y el supervisor.
- Diseñar un ciclo de consentimiento completo: alcance, vigencia, renovación,
  revocación y evidencia.
- Implementar y auditar un flujo de autorización con OAuth 2.x y OpenID Connect
  con los refuerzos que exige el perfil financiero.
- Especificar una API financiera versionada, idempotente y observable, con su
  contrato OpenAPI y sus pruebas de conformidad.
- Evaluar los riesgos sistémicos del modelo: concentración de agregadores,
  proveedores tecnológicos críticos y reparto de responsabilidad.

## Competencias

| Competencia | Nivel esperado |
|---|---|
| Diseño de API financiera | Especifica, versiona y prueba |
| Autorización y criptografía aplicada | Implementa y audita |
| Gobierno del consentimiento | Diseña el ciclo completo |
| Análisis regulatorio | Ubica la actividad en el perímetro |
| Modelado de amenazas | Construye y prioriza |

## Secuencia

1. [Banca abierta, finanzas abiertas y datos abiertos](classes/01-banca-abierta-finanzas-abiertas-y-datos-abiertos.md)
2. [Ecosistema, participantes y modelos de implantación](classes/02-ecosistema-participantes-y-modelos-de-implantacion.md)
3. [El Sistema de Finanzas Abiertas de Chile](classes/03-sistema-de-finanzas-abiertas-de-chile.md)
4. [Clasificación, calidad y gobierno de datos financieros](classes/04-clasificacion-calidad-y-gobierno-de-datos.md)
5. [Consentimiento: creación, vigencia, renovación y revocación](classes/05-consentimiento-ciclo-de-vida.md)
6. [OAuth, OpenID Connect y autorización financiera](classes/06-oauth-openid-connect-y-autorizacion.md)
7. [Financial-grade APIs, certificados y firma de mensajes](classes/07-financial-grade-apis-y-firma.md)
8. [Diseño, versionado e idempotencia](classes/08-diseno-versionado-e-idempotencia.md)
9. [APIs de cuentas, productos, créditos, seguros e inversiones](classes/09-apis-de-informacion-financiera.md)
10. [Iniciación de pagos y confirmación de fondos](classes/10-iniciacion-de-pagos-y-confirmacion-de-fondos.md)
11. [Autenticación reforzada, fraude y responsabilidad](classes/11-autenticacion-reforzada-fraude-y-responsabilidad.md)
12. [Privacidad, finalidad, minimización y portabilidad](classes/12-privacidad-finalidad-y-portabilidad.md)
13. [Disponibilidad, SLA, observabilidad e incidentes](classes/13-disponibilidad-sla-y-observabilidad.md)
14. [Proyecto: agregador financiero regulado](classes/14-proyecto-agregador-financiero-regulado.md)

## Laboratorios

| # | Laboratorio | Entregable principal |
|---:|---|---|
| 1 | [Consentimiento granular](labs/lab-01.md) | Modelo de alcances y evidencia |
| 2 | [Servidor de autorización simulado](labs/lab-02.md) | Flujo con PKCE y validación de tokens |
| 3 | [API de cuentas y movimientos](labs/lab-03.md) | Contrato OpenAPI y paginación |
| 4 | [Iniciación de pagos](labs/lab-04.md) | Idempotencia y máquina de estados |
| 5 | [Panel de consentimientos](labs/lab-05.md) | Revocación con efecto verificable |
| 6 | [Conformidad y seguridad](labs/lab-06.md) | Batería de pruebas negativas |

## Evaluaciones

- [Diagnóstico](assessments/diagnostic.md)
- [Evaluación final](assessments/final.md)

## Proyecto

- [Agregador financiero regulado](project/README.md)

## Evidencias

- Mapa de alcances de consentimiento con su base de licitud.
- Flujo de autorización ejecutado y trazado extremo a extremo.
- Contrato OpenAPI validado.
- Registro de pruebas de conformidad, incluidas las negativas.
- Modelo de amenazas priorizado.
- Matriz de responsabilidad ante fraude.

## Mapa de dependencias

```text
Parte 14 (introducción fintech)
   └── Parte 17 — finanzas abiertas
          ├── Parte 18 · iniciación de pagos en contexto transfronterizo
          ├── Parte 21 · identidad y elegibilidad en mercados tokenizados
          ├── Parte 22 · perímetro regulatorio del prestador
          └── Parte 23 · capa de consentimiento del banco digital
```

## Aplicación asociada

- [`apps/open_finance_sandbox/`](../../apps/open_finance_sandbox/README.md)

## Fuentes oficiales de referencia

- Comisión para el Mercado Financiero (Chile) — normativa del Sistema de Finanzas Abiertas.
- Banco Central de Chile — normativa de sistemas de pago.
- OpenID Foundation — perfiles FAPI.
- IETF — RFC 6749, RFC 7636, RFC 8705, RFC 9449.
- Bank for International Settlements — informes sobre open banking y open finance.

## Limitaciones

- La normativa chilena de finanzas abiertas está en despliegue por fases: cada
  clase indica la fecha de verificación y qué debe revisarse en la fuente oficial.
- Los perfiles de seguridad citados evolucionan; se indica la versión mencionada
  y se pide comprobar la vigente.
- El material no habilita a conectarse con entidades reales ni sustituye el
  proceso de inscripción o autorización ante el supervisor.
