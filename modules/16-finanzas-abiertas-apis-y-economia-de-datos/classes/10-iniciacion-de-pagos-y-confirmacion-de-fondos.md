---
part: 17
class: 10
title: "Iniciación de pagos y confirmación de fondos"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global, chile, union-europea]
regulatory_topics: [open-finance, pagos, autenticacion]
regulation_last_verified: 2026-08-06
regulatory_status: en-despliegue-por-fases
primary_authorities: [CMF, Banco Central de Chile]
requires_legal_review: true
---

<!-- gen:header:start -->
# Clase 10 · Iniciación de pagos y confirmación de fondos

> [← 09 · APIs de cuentas, productos, créditos, seguros e inversiones](09-apis-de-informacion-financiera.md) · [Índice de la parte](../README.md) · [11 · Autenticación reforzada, fraude y responsabilidad →](11-autenticacion-reforzada-fraude-y-responsabilidad.md)

**Parte 17 — Finanzas abiertas, APIs y economía de datos** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Pasar de leer a mover dinero. La iniciación de pagos cambia la figura
regulatoria, el régimen de responsabilidad y el diseño técnico: el error deja de
mostrar un número equivocado y pasa a transferir fondos.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** orden de pago, pago y liquidación, y decir quién responde en
   cada etapa.
2. **Diseñar** el consentimiento de pago, que es de naturaleza distinta al de
   información.
3. **Implementar** la máquina de estados de un pago con sus estados finales.
4. **Especificar** la confirmación de fondos sin convertirla en una fuga de saldo.
5. **Evaluar** el momento en que un comercio puede entregar la mercancía.

<!-- gen:agenda:start -->
## Agenda de 90 minutos

| Minutos | Bloque | Qué ocurre |
|---:|---|---|
| 0–10 | Activación | Pregunta diagnóstica y recuperación de la clase anterior. |
| 10–35 | Conceptos | Desarrollo guiado con la fuente oficial a la vista. |
| 35–55 | Ejemplo guiado | El docente resuelve el caso numérico paso a paso. |
| 55–80 | Práctica | El estudiante replica con datos propios o sintéticos. |
| 80–90 | Cierre | Preguntas de comprobación y registro en el portafolio. |
<!-- gen:agenda:end -->

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| `orden de pago` | Instrucción autorizada por el cliente |
| `pago` | Ejecución de la orden por la institución |
| `liquidación` | Momento en que los fondos son definitivos e irrevocables |
| `consentimiento de pago` | Autorización ligada a importe, beneficiario y una sola ejecución |
| `confirmación de fondos` | Respuesta booleana sobre suficiencia, sin retención |
| `estado final` | Estado del que un pago ya no sale |
| `devolución` | Retorno de fondos posterior a la liquidación |
| `firmeza` | Punto a partir del cual el pago no puede revertirse unilateralmente |

## 🧠 Modelo mental

```text
TRES MOMENTOS QUE NO SON EL MISMO

  AUTORIZACIÓN   el cliente aprueba: existe una orden
  ACEPTACIÓN     la institución admite la orden a trámite
  LIQUIDACIÓN    los fondos están en la cuenta del beneficiario,
                 de forma definitiva

EL ERROR QUE CUESTA DINERO
  el iniciador informa «pago realizado» en la ACEPTACIÓN
  el comercio entrega la mercancía
  el pago se rechaza después
  → el comercio entregó y no cobró

REGLA
  el comercio entrega cuando hay LIQUIDACIÓN o firmeza,
  no cuando hay aceptación.
  Si el sistema no distingue los tres estados,
  el comercio no puede aplicar la regla.
```

## 📖 Desarrollo

### 1. El consentimiento de pago no es el de información

| | Consentimiento de información | Consentimiento de pago |
|---|---|---|
| Duración | Meses | Una operación |
| Alcance | Familias de datos | Importe y beneficiario concretos |
| Reutilizable | Sí, mientras vigente | No |
| Autenticación | Al otorgar | Reforzada, por operación |
| Revocación | Efecto hacia el futuro | No aplica: se agota al usarse |
| Riesgo si falla | Acceso indebido a datos | Pérdida patrimonial |

```text
EXCEPCIÓN: PAGOS RECURRENTES
  existen consentimientos de pago de uso múltiple
  (suscripciones, pagos periódicos)

  cuando existen, llevan SIEMPRE:
    · importe máximo por operación
    · importe máximo por periodo
    · fecha de fin
    · beneficiario fijo
    · derecho de revocación con efecto sobre los futuros

  un consentimiento de pago sin esos cinco límites
  es una autorización en blanco
```

### 2. La máquina de estados completa

```text
   recibido
      │ validación de formato y de consentimiento
      ▼
   autorizado ─────────────► rechazado   (no autenticó, o revocó)
      │ autenticación reforzada superada
      ▼
   aceptado ───────────────► rechazado   (sin fondos, límite, cumplimiento)
      │ la institución admite a trámite
      ▼
   en_ejecucion ───────────► rechazado   (fallo en la infraestructura)
      │
      ▼
   liquidado ──────────────► devuelto    (devolución posterior)

ESTADOS FINALES:  rechazado, devuelto
ESTADO FIRME:     liquidado (pero admite devolución por causa tasada)
CONSULTABLES:     todos, durante la ventana declarada
```

```text
POR QUÉ «en_ejecucion» ES UN ESTADO Y NO UN DETALLE
  entre la aceptación y la liquidación puede haber
  horas (o días, si hay corte horario o día inhábil)

  sin ese estado, el iniciador tiene que elegir entre
  mentir hacia arriba («liquidado») o hacia abajo («pendiente»)
  → y elige mal
```

### 3. Los datos mínimos de una orden

```text
OBLIGATORIOS
  importe y moneda            (cadena decimal + código)
  beneficiario                identificador de cuenta y nombre
  cuenta de cargo             elegida por el cliente en la autenticación
  referencia del ordenante    para su conciliación
  fecha de ejecución solicitada

OPCIONALES CON EFECTO
  concepto para el beneficiario   → aparece en su extracto
  identificador de extremo a extremo → clave para conciliar

NUNCA
  datos de tarjeta, credenciales, ni el saldo del ordenante
```

### 4. Confirmación de fondos: la sonda que hay que acotar

```text
QUÉ ES
  «¿hay al menos X en esta cuenta ahora mismo?»  → sí / no

QUÉ NO ES
  · no es una retención: no bloquea nada
  · no es un saldo: no devuelve el importe
  · no es una garantía: el saldo puede cambiar en el segundo siguiente

EL ATAQUE POR BISECCIÓN
  el llamante consulta 1 000 000 → no
                        500 000 → no
                        250 000 → sí
                        375 000 → sí ...
  en ~20 consultas obtiene el saldo con precisión de peso

CONTROLES, LOS TRES A LA VEZ
  1. límite de tasa PROPIO de este endpoint, por consentimiento
  2. el importe consultado debe corresponder a una orden en curso
  3. registro y alerta por patrón de importes decrecientes
```

### 5. Quién responde en cada etapa

```text
ANTES DE LA AUTORIZACIÓN
  el iniciador responde de lo que muestra al cliente:
  importe, beneficiario y consecuencia

EN LA AUTENTICACIÓN
  la institución que mantiene la cuenta responde
  de autenticar correctamente

TRAS LA ACEPTACIÓN
  la institución responde de ejecutar lo aceptado

SI LA OPERACIÓN RESULTA NO AUTORIZADA
  el régimen concreto lo fija la norma local, pero el patrón
  habitual es:
    · la institución devuelve al cliente
    · y repite contra quien corresponda según dónde falló
  → la clave probatoria es la EVIDENCIA de la autenticación
    y del consentimiento (clase 5)
```

## 🧮 Ejemplo guiado

**Situación.** Un comercio integra el botón de pago. En la primera semana
aparecen tres incidentes.

```text
INCIDENTE A
  47 clientes reportan doble cargo.
  El comercio reintentó tras tiempos de espera agotados.

INCIDENTE B
  El comercio entregó 213 pedidos que después se rechazaron.
  Importe total: 8 940 000.

INCIDENTE C
  Un integrador consulta confirmación de fondos 41 veces
  para una sola orden, con importes descendentes.
```

**Paso 1 — diagnostica A.**

```text
CAUSA: el iniciador no exige clave de idempotencia

CÁLCULO DEL DAÑO
  47 dobles cargos, ticket medio 42 000
  47 × 42 000 = 1 974 000 devueltos
  + coste de gestión: 47 × 3 500 = 164 500
  + 47 clientes con una mala primera experiencia

CORRECCIÓN (clase 8)
  Idempotency-Key obligatoria
  + canonicalización + bloqueo + respuesta guardada
```

**Paso 2 — diagnostica B, que es el más caro.**

```text
CAUSA: el iniciador informa «pago realizado» en ACEPTADO

  el comercio programó: si estado == "ok" → entregar
  el iniciador devolvía "ok" en la aceptación

VERIFICACIÓN
  de los 213 rechazos posteriores:
    118  fondos insuficientes entre aceptación y ejecución
     61  límite diario del cliente superado
     23  cuenta beneficiaria inválida
     11  control de cumplimiento
```

**Paso 3 — cuantifica y reparte.**

```text
PÉRDIDA DEL COMERCIO: 8 940 000

¿DE QUIÉN ES LA CULPA?
  del iniciador   por colapsar tres estados en «ok»
  del comercio    por entregar sin verificar firmeza
  del contrato    por no definir qué estado habilita la entrega

EL DATO QUE ORDENA LA DISCUSIÓN
  de los 213, ¿cuántos habrían sido evitables esperando?
    118 + 61 = 179 se conocían en la EJECUCIÓN (minutos)
     23 + 11 =  34 se conocían antes o durante

  esperar a «liquidado» habría evitado los 213
  esperar 5 minutos habría evitado ~179 (75 % del importe)
```

**Paso 4 — diseña la corrección de B.**

```text
CAMBIO EN EL CONTRATO DEL INICIADOR
  exponer el estado real, no un booleano
  y documentar: «entrega con LIQUIDADO»

CAMBIO EN EL COMERCIO
  entrega inmediata solo si:
    estado == liquidado
  entrega diferida si:
    estado == aceptado o en_ejecucion
  con notificación al cliente: «confirmando tu pago»

EFECTO SOBRE LA CONVERSIÓN
  supuesto: el 88 % liquida en menos de 20 segundos
  → 88 % de los pedidos no percibe diferencia
  → 12 % espera; de ellos, el 4 % abandona

  ABANDONO ESTIMADO: 12 % × 4 % = 0,48 % de los pedidos
  PÉRDIDA EVITADA:   8 940 000 en una semana

  0,48 % de abandono frente a 8,94 millones semanales:
  la comparación no está reñida
```

**Paso 5 — diagnostica C.**

```text
41 CONSULTAS CON IMPORTES DESCENDENTES PARA UNA ORDEN

  patrón de bisección: el integrador está deduciendo el saldo

  ¿ES MALICIOSO?
    puede no serlo: quizá implementó «buscar el importe
    máximo que el cliente puede pagar» para ofrecer cuotas

  DA IGUAL LA INTENCIÓN
    el efecto es el mismo: obtiene un dato
    que el consentimiento de pago no le concedió
```

**Paso 6 — corrige C.**

```text
CONTROLES APLICADOS
  1. límite: 3 consultas por orden, 20 por consentimiento y día
  2. el importe consultado debe coincidir con el de una orden
     en curso, con tolerancia cero
  3. alerta automática ante ≥ 4 consultas descendentes
  4. contacto con el integrador y revisión de su caso de uso

Y UNA DECISIÓN DE PRODUCTO
  si el caso de uso legítimo es «ofrecer cuotas»,
  la respuesta correcta NO es abrir la sonda:
  es un alcance de información con su propio consentimiento,
  que el cliente pueda ver y revocar
```

**Paso 7 — cierra con la lección común.**

```text
LOS TRES INCIDENTES TIENEN LA MISMA RAÍZ

  A · el sistema no distinguió petición de efecto
  B · el sistema no distinguió aceptación de liquidación
  C · el sistema no distinguió comprobar de consultar

  → toda la clase es la misma idea aplicada tres veces:
    en pagos, colapsar dos conceptos en uno cuesta dinero
```

**Interpreta:** el incidente B costó 8,94 millones en una semana y la corrección
técnica era una línea de contrato: **exponer el estado real en vez de un
booleano**. La mayoría de las pérdidas en iniciación de pagos no vienen de fallos
del sistema, sino de estados mal comunicados.

## 🧭 Perspectivas

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un botón «pagar con mi banco» | Si lo usa |
| Comercio | Un estado «ok» | Cuándo entrega |
| Iniciador | Complejidad de estados | Si la expone o la esconde |
| Banco | Órdenes de terceros | Qué límites aplica |
| Banco central | Nuevo canal de pagos | Si lo vigila |
| Supervisor | Reclamos por doble cargo | Qué exige al iniciador |
| Auditor | Evidencia de autenticación | Si prueba la autorización |

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Me cobraron dos veces» | Idempotencia ausente | 17, clases 8 y 10 |
| «Dijo pagado y no llegó» | Aceptación comunicada como liquidación | 17, clase 10 |
| «No autoricé ese pago» | Evidencia de autenticación reforzada | 17, clase 11 |
| «Pagué y esperé un rato» | Ejecución con corte horario | 18, clase 7 |

## ⚖️ Riesgos y controles

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Doble cargo | Reintento sin idempotencia | Clave obligatoria con bloqueo |
| Entrega sin cobro | «ok» en aceptación | Exponer estado real; entregar con firmeza |
| Fuga de saldo | Bisección con confirmación de fondos | Límite por orden y coincidencia de importe |
| Autorización en blanco | Recurrente sin límites | Cinco límites obligatorios |
| Beneficiario alterado | Parámetros sin firmar | Objeto de petición firmado (clase 7) |
| Pago no autorizado sin prueba | Evidencia insuficiente | Registro de autenticación y consentimiento |

## 🧪 Práctica

En [`labs/lab-04.md`](../labs/lab-04.md):

1. Implementa la máquina de estados con los seis estados y sus transiciones.
2. Simula los tres fallos y verifica el saldo final en cada uno.
3. Implementa la confirmación de fondos con los tres controles.
4. Escribe la prueba que detecta el patrón de bisección.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Estado booleano | Se simplificó la API | Exponer los seis estados |
| Entregar en aceptado | El contrato no lo definía | Definir qué estado habilita la entrega |
| Confirmación sin límite | Se trató como consulta barata | Límite propio por consentimiento |
| Recurrente sin tope | Se copió el modelo de un solo uso | Cinco límites obligatorios |
| Consentimiento de pago reutilizado | Se trató como el de información | Se agota al usarse |
| Sin evidencia de autenticación | Se registró el resultado | Registrar método y momento |

## ❓ Preguntas de comprobación

1. ¿Qué distingue autorización, aceptación y liquidación, y por qué colapsarlas
   cuesta dinero?
2. ¿En qué se diferencia el consentimiento de pago del de información, en seis
   dimensiones?
3. ¿Cómo se ataca por bisección una confirmación de fondos y con qué tres
   controles se corta?
4. ¿Qué cinco límites debe llevar un consentimiento de pago recurrente?
5. En el ejemplo guiado, ¿por qué un 0,48 % de abandono fue aceptable?

## 📥 Entregable

Guarda en `portfolio/parte-17/clase-10/`:

- el diagrama de la máquina de estados con estados finales y firmes;
- la especificación del consentimiento de pago, incluida la variante recurrente;
- los tres controles de la confirmación de fondos, implementados y probados;
- el análisis de qué estado habilita la entrega en tu caso, con su justificación.

## 🔗 Referencias cruzadas

- **Viene de:** clase 5 (consentimiento), clase 7 (firma), clase 8 (idempotencia).
- **Continúa en:** clase 11 (autenticación reforzada y responsabilidad),
  clase 13 (disponibilidad).
- **Se aplica en:** Parte 18, clases 7 y 13 (liquidación y pagos inmediatos);
  Parte 23, clase 8.

<!-- gen:etica:start -->
## 🔐 Seguridad, ética y límites

Trabaja siempre con datos sintéticos o propios: nunca uses datos reales de terceros,
números de cuenta, documentos de identidad ni antecedentes crediticios ajenos. Este
material es formativo y **no constituye asesoría financiera, tributaria ni legal**; las
tasas, comisiones, límites y normas citados cambian y deben verificarse en la fuente
oficial vigente del país donde se aplique. Cuando un cálculo alimente una decisión que
afecte a otra persona, registra los supuestos y quién los aprobó.
<!-- gen:etica:end -->

## 📗 Fuentes y verificación

- Comisión para el Mercado Financiero. *Normativa del Sistema de Finanzas Abiertas: iniciación de pagos*. CMF. <https://www.cmfchile.cl/>
- Banco Central de Chile. *Compendio de Normas Financieras: normativa de sistemas de pago*. <https://www.bcentral.cl/>
- Parlamento Europeo y Consejo. *Directiva (UE) 2015/2366 (PSD2): iniciación de pagos y confirmación de fondos*. <https://eur-lex.europa.eu/eli/dir/2015/2366/oj>
- Committee on Payments and Market Infrastructures e IOSCO (2012). *Principles for Financial Market Infrastructures*. BIS. <https://www.bis.org/cpmi/publ/d101.htm>
- Internet Engineering Task Force. *RFC 9110 — HTTP Semantics: métodos idempotentes*. IETF. <https://www.rfc-editor.org/rfc/rfc9110>
- Verificación local: comprueba el régimen de operaciones no autorizadas, los plazos de devolución y las exigencias de autenticación vigentes en tu jurisdicción. **Fecha de verificación de esta clase: 2026-08-06.** Esta clase no constituye asesoría legal.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 09 · APIs de cuentas, productos, créditos, seguros e inversiones](09-apis-de-informacion-financiera.md) | [Parte 17](../README.md) · [Programa](../../../SYLLABUS.md) | [11 · Autenticación reforzada, fraude y responsabilidad →](11-autenticacion-reforzada-fraude-y-responsabilidad.md) |
<!-- gen:footer:end -->
