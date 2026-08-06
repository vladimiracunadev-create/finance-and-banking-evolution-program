# Proyecto integrador: agregador financiero regulado

## Desafío

Diseña, implementa y defiende un **agregador financiero** que acceda a datos de
cuatro instituciones con el consentimiento del cliente, muestre una posición
consolidada e inicie un pago. Todo en entorno simulado, con datos sintéticos.

El proyecto se evalúa por lo que puedes **demostrar ejecutando**, no por lo que
afirmas en el documento.

## Alcance

| Incluido | Fuera de alcance |
|---|---|
| Consentimiento con ciclo de vida completo | Conexión con entidades reales |
| Autorización con PKCE y alcances | Certificados de una autoridad real |
| API de cuentas, saldos y movimientos | Multidivisa (Parte 18) |
| Iniciación de pago doméstico | Liquidación real |
| Panel de consentimientos con revocación | Inscripción ante el supervisor |
| Batería de conformidad | Auditoría externa |

## Requisitos mínimos

1. **Producto definido**: qué problema resuelve y para quién. Una frase.
2. **Dato mínimo**: lista de datos necesarios, escrita antes de mirar la API.
3. **Modelo de alcances**: uno por finalidad, con base de licitud y plazo.
4. **Flujo de autorización** funcional, con las siete pruebas negativas del
   laboratorio 2.
5. **Contrato OpenAPI** validado por `tools/validate_openapi.py`.
6. **Iniciación de pago** idempotente, con la máquina de estados probada.
7. **Panel de consentimientos** con revocación de efecto verificable.
8. **Modelo de amenazas** con al menos 12 amenazas priorizadas por impacto y
   probabilidad, y el control asociado a cada una.
9. **Matriz regulatoria**: actividad → posible obligación → autoridad → fuente
   oficial → fecha de verificación → limitaciones.
10. **Registro de decisiones**: cada decisión de diseño con su alternativa
    descartada y el motivo.

## Entregables

```text
project/
├── README.md
├── requirements.md
├── architecture.md
├── assumptions.md
├── risk-register.md
├── regulatory-matrix.md
├── security.md
├── data/
├── src/
├── tests/
├── evidence/
├── presentation-outline.md
├── rubric.md
└── solution-reference/
```

| Archivo | Qué contiene |
|---|---|
| `requirements.md` | Producto, usuarios, dato mínimo, alcances |
| `architecture.md` | Componentes, flujos y diagramas |
| `assumptions.md` | Supuestos del ejercicio y su efecto si cambian |
| `risk-register.md` | Amenazas priorizadas con control y responsable |
| `regulatory-matrix.md` | Actividad, obligación, autoridad, fuente, fecha |
| `security.md` | Modelo de amenazas, gestión de secretos, pruebas negativas |
| `evidence/` | Trazas, capturas de ejecución, informe de conformidad |
| `presentation-outline.md` | Guion de la defensa de 10 minutos |

## Criterios de aceptación

| # | Criterio | Verificación |
|---:|---|---|
| 1 | El flujo completo se ejecuta de principio a fin | Demostración en vivo |
| 2 | Sin PKCE, el flujo falla | Prueba negativa |
| 3 | Un reintento no duplica el pago | Saldo tras 5 reintentos |
| 4 | La revocación bloquea el acceso siguiente | Prueba temporizada |
| 5 | El contrato OpenAPI valida | `tools/validate_openapi.py` |
| 6 | No hay secretos en el repositorio | `tools/detect_secrets.py` |
| 7 | No hay datos personales reales | `tools/detect_pii.py` |
| 8 | Cada norma citada tiene fecha | Revisión de la matriz |

## Defensa

Diez minutos ante un panel que hace de comité de riesgo. Las tres preguntas que
siempre se hacen:

1. ¿Qué datos pediste que no necesitabas, y por qué los pediste?
2. Enséñame el segundo posterior a una revocación.
3. Si tu proveedor de identidad cae una hora, ¿qué ve el cliente?

## Rúbrica

| Área | Peso | Qué distingue el nivel alto |
|---|---:|---|
| Diseño de consentimiento | 20 % | Alcance por finalidad, no por comodidad |
| Seguridad de la autorización | 20 % | Pruebas negativas antes que positivas |
| Calidad del contrato de API | 15 % | Versionado e idempotencia resueltos |
| Riesgo y regulación | 20 % | Matriz con fuente y fecha, límites declarados |
| Evidencia y reproducibilidad | 15 % | Otro puede ejecutarlo sin ayuda |
| Defensa | 10 % | Responde con datos, no con intenciones |

## Solución de referencia

`solution-reference/` contiene una implementación de referencia comentada. Es
material **docente**: sirve para corregir y para desbloquear, no para entregar.
Un proyecto que la reproduce sin decisiones propias obtiene el mínimo de la
franja de aprobación.
