---
part: 18
class: 6
title: "SWIFT, CBPR+ e ISO 20022"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global]
regulatory_topics: [cross-border-payments, mensajeria, datos-estructurados]
regulation_last_verified: 2026-08-06
regulatory_status: estandar-vigente
primary_authorities: [ISO, CPMI]
requires_legal_review: false
---

<!-- gen:header:start -->
# Clase 06 · SWIFT, CBPR+ e ISO 20022

> [← 05 · Mensajería frente a movimiento de fondos](05-mensajeria-frente-a-movimiento-de-fondos.md) · [Índice de la parte](../README.md) · [07 · Compensación, liquidación y finalidad →](07-compensacion-liquidacion-y-finalidad.md)

**Parte 18 — Pagos transfronterizos, remesas y liquidación internacional** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Leer y construir los mensajes de pago que el sistema financiero usa realmente.
ISO 20022 no es «un formato nuevo»: es la diferencia entre un pago que se procesa
solo y uno que acaba en una cola manual.

## 📚 Objetivos

Al finalizar podrás:

1. **Identificar** los siete mensajes de la familia de pagos y cuándo se usa
   cada uno.
2. **Construir** un `pacs.008` con sus campos obligatorios y sus partes.
3. **Distinguir** deudor de deudor último y acreedor de acreedor último, y
   explicar por qué importa.
4. **Usar** los códigos de propósito y la referencia extremo a extremo.
5. **Diagnosticar** por qué un pago con datos no estructurados degrada el
   procesamiento directo.

<!-- gen:agenda:start -->
## Agenda de 90 minutos

La clase dura noventa minutos y se recorre en cinco tramos. No es un horario
rígido: es el orden en que los bloques de esta página se sostienen unos a otros, y
por eso conviene respetarlo aunque cambien los tiempos.

Los **diez primeros minutos** se dedican a recuperar la clase anterior, porque casi
todo lo que aquí se explica supone algo que ya se vio. Los **veinticinco
siguientes** desarrollan los conceptos con la fuente oficial a la vista: las
referencias del final de la página no son un adorno bibliográfico, se consultan
mientras se estudia. Del **minuto 35 al 55** se resuelve el ejemplo guiado paso a
paso, sin saltarse ninguno, porque el error típico vive precisamente en el paso que
parece obvio. Los **veinticinco minutos siguientes** son de práctica con datos
propios o sintéticos —nunca reales de terceros—, que es cuando se comprueba si se
entendió. Los **diez últimos** cierran con las preguntas de comprobación y el
registro del entregable.

Si el tiempo aprieta, lo que se recorta es la práctica y se traslada al
laboratorio de la parte; lo que no se recorta nunca es el ejemplo guiado.
<!-- gen:agenda:end -->

## 🧩 Conceptos centrales

Los tres primeros términos son el estándar y su perfil; los cinco siguientes, los mensajes concretos y su trazabilidad. La **referencia extremo a extremo** es lo que hace posible seguir un pago por toda la cadena: sin ella, cada tramo tiene su propia referencia y nadie puede reconstruir el trayecto.

| Concepto | Comprensión verificable |
|---|---|
| `ISO 20022` | Norma internacional de mensajería financiera con diccionario común |
| `CBPR+` | Guías de uso de ISO 20022 para pagos transfronterizos |
| `pacs.008` | Transferencia de crédito de cliente entre instituciones |
| `pacs.009` | Transferencia entre instituciones financieras por cuenta propia |
| `pacs.002` | Informe de estado de un pago |
| `pacs.004` | Devolución de un pago |
| `camt.056` | Solicitud de cancelación de un pago |
| `referencia extremo a extremo` | Identificador único que acompaña al pago en toda la cadena |

## 🧠 Modelo mental

El modelo mental es un vocabulario común: el estándar no mueve dinero, define cómo se dice lo que hay que hacer. Su valor está en que todos los participantes entiendan lo mismo por cada campo, y su coste está en la migración.

```text
ISO 20022 NO ES UN FORMATO: ES UN DICCIONARIO

  antes    «campo 50K, línea 3: BENEFICIARIO»
           texto libre de 35 caracteres, interpretado
           de forma distinta en cada banco

  ahora    <Cdtr><Nm>…</Nm><PstlAdr><StrtNm>…</StrtNm>
           <TwnNm>…</TwnNm><Ctry>…</Ctry></PstlAdr></Cdtr>
           cada dato en su sitio, con su significado

LO QUE ESTO CAMBIA REALMENTE
  · el screening compara campos, no cadenas de texto
  · el banco receptor no tiene que adivinar dónde está la ciudad
  · la conciliación se automatiza con la referencia
  · los códigos de propósito permiten reglas por tipo de pago

LO QUE NO CAMBIA
  la velocidad de LIQUIDACIÓN (clase 5).
  ISO 20022 actúa en la capa 1.
```

## 📖 Desarrollo

### 1. La familia de mensajes

| Mensaje | Nombre | Cuándo se usa |
|---|---|---|
| `pacs.008` | FIToFICustomerCreditTransfer | Pago de un cliente a otro |
| `pacs.009` | FinancialInstitutionCreditTransfer | Movimiento entre bancos por cuenta propia, y coberturas |
| `pacs.002` | FIToFIPaymentStatusReport | Aceptado, rechazado, pendiente |
| `pacs.004` | PaymentReturn | Devolución de un pago ya liquidado |
| `camt.056` | FIToFIPaymentCancellationRequest | Petición de cancelar antes de liquidar |
| `camt.029` | ResolutionOfInvestigation | Respuesta a una investigación o cancelación |
| `camt.053` / `camt.054` | Statement / Notification | Extracto y aviso de cargo o abono |

```text
LA SECUENCIA HABITUAL DE UN PAGO CORRECTO
  pacs.008  →  pacs.002 (aceptado)  →  camt.054 (aviso)  →  camt.053 (extracto)

LA SECUENCIA DE UN PAGO QUE FALLA
  pacs.008  →  pacs.002 (rechazado, con código de motivo)

LA SECUENCIA DE UN PAGO QUE HAY QUE DESHACER
  pacs.008  →  liquidado  →  camt.056 (petición)
            →  camt.029 (resolución)  →  pacs.004 (devolución) si procede

EL ORDEN IMPORTA
  antes de liquidar se CANCELA (camt.056)
  después de liquidar se DEVUELVE (pacs.004)
  y la devolución NO es automática: depende del receptor
```

### 2. Anatomía de un `pacs.008`

```text
GroupHeader
  MsgId                identificador del mensaje
  CreDtTm              fecha y hora de creación
  NbOfTxs              número de operaciones
  SttlmInf             método de liquidación e intermediarios

CreditTransferTransactionInformation
  PmtId
    InstrId            referencia del banco emisor
    EndToEndId         REFERENCIA EXTREMO A EXTREMO ← la clave
    UETR               identificador único de la operación
  IntrBkSttlmAmt       importe y divisa de liquidación
  IntrBkSttlmDt        fecha de liquidación interbancaria
  ChrgBr               reparto de gastos: DEBT / CRED / SHAR
  Dbtr                 DEUDOR: quien paga
  DbtrAcct             su cuenta
  DbtrAgt              su banco
  CdtrAgt              banco del acreedor
  Cdtr                 ACREEDOR: quien cobra
  CdtrAcct             su cuenta
  Purp                 CÓDIGO DE PROPÓSITO
  RmtInf               información de remesa para conciliar
```

### 3. Deudor y deudor último: la distinción que cuesta dinero

```text
Dbtr        DEUDOR: quien ordena y de cuya cuenta sale el dinero
UltmtDbtr   DEUDOR ÚLTIMO: por cuenta de quién se paga realmente

Cdtr        ACREEDOR: en cuya cuenta entra el dinero
UltmtCdtr   ACREEDOR ÚLTIMO: quien realmente se beneficia

EJEMPLO
  una gestora paga la factura de una empresa que administra
    Dbtr       = la gestora (sale de su cuenta)
    UltmtDbtr  = la empresa administrada

  una plataforma cobra por cuenta de sus vendedores
    Cdtr       = la plataforma (entra en su cuenta)
    UltmtCdtr  = el vendedor

POR QUÉ IMPORTA
  el screening de sanciones y la Recomendación 16 del GAFI
  exigen conocer a las partes REALES, no solo a las cuentas.
  Omitir el último es lo que convierte una operación
  legítima en un hallazgo de auditoría.
```

### 4. Códigos de propósito y referencias

```text
CÓDIGO DE PROPÓSITO (Purp)
  SALA  salario          SUPP  pago a proveedor
  TAXS  impuestos        LOAN  préstamo
  DIVI  dividendos       TRAD  comercio
  CHAR  donación         RENT  arrendamiento

  PARA QUÉ SIRVE REALMENTE
    · permite reglas de cumplimiento por tipo
    · permite estadística de balanza de pagos
    · reduce falsos positivos: un salario recurrente
      al mismo beneficiario no es un patrón sospechoso

REFERENCIA EXTREMO A EXTREMO (EndToEndId)
  la fija el ORDENANTE y NINGÚN eslabón la altera
  → es lo que permite al ordenante y al beneficiario
    hablar del mismo pago sin ambigüedad

IDENTIFICADOR ÚNICO (UETR)
  se genera al crear el pago y acompaña toda la cadena
  → es lo que permite el seguimiento extremo a extremo
```

### 5. Por qué el texto libre destruye el procesamiento directo

```text
DIRECCIÓN EN TEXTO LIBRE
  "AV LIB BDO OHIGGINS 1234 DPTO 55 STGO CHILE"

  el screening la compara con listas donde figura
  "AVENIDA LIBERTADOR BERNARDO O'HIGGINS"
  → no coincide, o coincide con algo que no es

  el banco receptor busca la ciudad
  → «STGO» no está en su tabla de ciudades
  → cae a revisión manual

DIRECCIÓN ESTRUCTURADA
  <StrtNm>Avenida Libertador Bernardo O'Higgins</StrtNm>
  <BldgNb>1234</BldgNb>
  <Flr>55</Flr>
  <TwnNm>Santiago</TwnNm>
  <Ctry>CL</Ctry>

  cada campo se compara con su equivalente
  → menos falsos positivos y menos reparaciones
```

## 🧮 Ejemplo guiado

El ejemplo construye un mensaje de pago con sus campos obligatorios. Conviene comprobar la referencia extremo a extremo: es el campo que hace posible el seguimiento.

**Situación.** Un banco migró a ISO 20022 hace seis meses y su tasa de
procesamiento directo **empeoró**, de 88 % a 81 %. Hay que averiguar por qué.

```text
RECHAZOS DEL MES: 1 900 DE 10 000 PAGOS
CÓDIGOS DE MOTIVO MÁS FRECUENTES
  AC01  identificador de cuenta incorrecto          612
  BE05  identificador del emisor incorrecto         441
  AM05  duplicado                                   287
  RR04  falta información regulatoria               318
  BE23  código de propósito no admitido             142
  Otros                                             100
```

**Paso 1 — descarta la hipótesis fácil.**

```text
HIPÓTESIS INICIAL DEL EQUIPO
  «el formato nuevo es más estricto, por eso rechaza más»

COMPROBACIÓN
  ¿los rechazos son por VALIDACIÓN DE ESQUEMA
  o por CONTENIDO?

  revisión de los 1 900: ninguno es error de esquema.
  Todos pasan la validación XML.

  → el formato no rechaza: rechaza el RECEPTOR,
    por el contenido de campos que antes iban en texto libre
    y nadie comprobaba
```

**Paso 2 — analiza los 612 de AC01.**

```text
IDENTIFICADOR DE CUENTA INCORRECTO

  MUESTRA DE 50 CASOS
    IBAN con dígito de control erróneo        31
    IBAN con espacios y guiones                12
    identificador nacional en el campo IBAN     7

LOS 31 SON EL HALLAZGO
  antes, el identificador viajaba en texto libre
  y el banco receptor lo «arreglaba» a mano
  → el error existía y nadie lo veía

  ahora el campo es estructurado y el receptor valida
  → el error aflora
```

**Paso 3 — reinterpreta la métrica.**

```text
LA TASA DE PROCESAMIENTO DIRECTO EMPEORÓ
PORQUE LA CALIDAD DEL DATO ERA PEOR DE LO QUE PARECÍA

  antes:  88 % «directo», con reparación manual
          invisible en el banco receptor
  ahora:  81 % directo, con el error devuelto al origen

  el 7 % de diferencia no es una regresión:
  es trabajo que se ha hecho visible

  Y ESO ES MEJOR: el error vuelve a quien puede corregirlo
```

**Paso 4 — analiza los 318 de RR04.**

```text
FALTA INFORMACIÓN REGULATORIA

  todos corresponden a pagos hacia dos jurisdicciones
  que exigen el propósito y el identificador fiscal
  del beneficiario

  el banco los enviaba en RmtInf (información de remesa)
  en vez de en los campos regulatorios previstos

  → no es un dato que falte: es un dato en el sitio equivocado
```

**Paso 5 — analiza los 287 duplicados.**

```text
AM05 DUPLICADO

  investigación: los 287 comparten patrón
    · mismo importe, beneficiario y fecha
    · EndToEndId DISTINTO en cada envío
    · UETR distinto

  CAUSA
    el sistema regenera la referencia en cada reintento
    → el receptor no puede reconocer el reintento como tal
      y lo detecta como duplicado por heurística de contenido

  CORRECCIÓN
    la referencia extremo a extremo y el UETR se generan
    UNA VEZ, al crear la orden, y se conservan en los reintentos
    (es exactamente la idempotencia de la Parte 17, clase 8,
     aplicada a la mensajería)
```

**Paso 6 — cuantifica cada corrección.**

```text
CORRECCIÓN 1 · validar IBAN en origen (dígito de control)
  evita 31/50 × 612 ≈ 379 rechazos/mes
  coste: 4 000 USD  (una biblioteca de validación)

CORRECCIÓN 2 · normalizar el identificador antes de enviar
  evita ≈ 233 rechazos/mes
  coste: incluido en la anterior

CORRECCIÓN 3 · mapear los campos regulatorios
  evita 318 rechazos/mes
  coste: 16 000 USD

CORRECCIÓN 4 · referencia estable en reintentos
  evita 287 rechazos/mes
  coste: 9 000 USD

CORRECCIÓN 5 · tabla de códigos de propósito admitidos por corredor
  evita 142 rechazos/mes
  coste: 5 000 USD

TOTAL EVITADO: 1 359 de 1 900 rechazos = 71,5 %
COSTE TOTAL: 34 000 USD
```

**Paso 7 — calcula el retorno y decide.**

```text
COSTE POR RECHAZO
  gestión manual        14 USD
  reenvío                 6 USD
  reclamación (35 %)     45 × 0,35 = 15,75 USD
  TOTAL                 35,75 USD

AHORRO MENSUAL
  1 359 × 35,75 = 48 584 USD
ANUALIZADO
  583 008 USD

RETORNO: 34 000 / 583 008 = 3 semanas

DECISIÓN: ejecutar las cinco, en el orden 4, 1, 3, 5, 2
  el 4 primero porque un duplicado puede significar
  un pago ejecutado dos veces, no solo un rechazo

Y CORREGIR LA NARRATIVA INTERNA
  la migración no empeoró nada: hizo visible un problema
  de calidad de datos que ya existía y que el banco
  receptor venía absorbiendo. La métrica correcta no es
  la tasa de procesamiento directo antes y después,
  sino el número de pagos que llegan mal a destino.
```

**Interpreta:** una métrica empeoró y la causa era que **el sistema empezó a
medir bien**. El error más caro de la migración no fue técnico: fue interpretar
la caída de la tasa como una regresión en vez de como un diagnóstico.

## 🧭 Perspectivas

El estándar afecta a cada participante de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un pago devuelto con un código | Si vuelve a intentarlo |
| Banco ordenante | Tasa que empeora tras migrar | Si revierte o corrige |
| Banco beneficiario | Datos que por fin puede validar | Si rechaza en vez de reparar |
| Cumplimiento | Campos comparables | Cómo recalibra el screening |
| Infraestructura | Mensajes más grandes | Capacidad y almacenamiento |
| Supervisor | Estadística de balanza de pagos | Qué códigos exige |
| Auditor | Deudor último ausente | Si observa |

## 🏦 Del cliente al banco

El cliente quiere saber dónde está su pago y el banco puede decírselo solo si la referencia se conservó. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Me devolvieron el pago con un código raro» | Motivo estructurado del rechazo | 18, clase 6 |
| «Me piden la dirección completa» | Campos estructurados obligatorios | 18, clase 6 |
| «Puse la referencia y no aparece» | La referencia extremo a extremo se alteró | 18, clase 6 |
| «Pagué dos veces» | Referencia regenerada en el reintento | 18, clases 4 y 6 |

## ⚖️ Riesgos y controles

Los riesgos son de datos incompletos y de migración. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Dato en el campo equivocado | Información regulatoria en remesa | Mapeo revisado por corredor |
| Referencia inestable | Reintento visto como duplicado | Referencia y UETR generados una vez |
| Deudor último omitido | Screening incompleto | Campo obligatorio cuando aplica |
| Texto libre residual | Falsos positivos y reparaciones | Estructurar antes de enviar |
| Código de propósito inválido | Rechazo en destino | Tabla por corredor, mantenida |
| Interpretar mal la métrica | Se revierte una mejora | Medir pagos que llegan mal, no solo la tasa |

## 🧪 Práctica

El laboratorio pide construir y validar mensajes con sus campos obligatorios. Los mensajes con datos truncados son los que producen las devoluciones.

En [`labs/lab-03.md`](../labs/lab-03.md):

1. Construye un `pacs.008` completo y valídalo con `tools/validate_iso20022.py`.
2. Genera la cadena `pacs.002` de aceptación y de rechazo con su código.
3. Modela una cancelación (`camt.056`) y una devolución (`pacs.004`).
4. Detecta en un lote los mensajes con referencia inestable.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen pagos devueltos o no rastreables. Las causas son campos incompletos y referencias no conservadas.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| «El formato nuevo rechaza más» | Se confundió esquema con contenido | Comprueba dónde falla |
| Deudor último omitido | Se rellenó solo la cuenta | Identifica a las partes reales |
| Referencia regenerada | Se trató como identificador técnico | Estable en toda la vida del pago |
| Cancelar después de liquidar | Se confundió `camt.056` con `pacs.004` | Antes se cancela, después se devuelve |
| Dirección en una sola línea | Se migró el texto libre tal cual | Estructura calle, número, ciudad, país |
| Código de propósito genérico | Se puso el mismo para todo | Reduce falsos positivos usarlo bien |

## ❓ Preguntas de comprobación

1. ¿Qué diferencia hay entre `camt.056` y `pacs.004`, y qué determina cuál usar?
2. ¿Por qué distinguir deudor de deudor último cambia el resultado del screening?
3. ¿Qué papel cumple la referencia extremo a extremo y quién puede alterarla?
4. ¿Por qué la dirección estructurada reduce falsos positivos?
5. En el ejemplo guiado, ¿por qué la caída de la tasa no era una regresión?

## 📥 Entregable

Guarda en `portfolio/parte-18/clase-06/`:

- un `pacs.008` completo y validado;
- la cadena de estados de un pago aceptado y de uno rechazado, con su código;
- el mapeo de campos de tu formulario a los campos estructurados;
- el análisis de un lote con los mensajes de referencia inestable identificados.

## 🔗 Referencias cruzadas

- **Viene de:** clases 2 y 5; Parte 17, clase 8 (idempotencia y contratos).
- **Continúa en:** clase 7 (liquidación), clase 12 (regla del viaje).
- **Se aplica en:** Parte 21, clase 12 (eventos corporativos); Parte 23, clase 8.

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

- ISO 20022. *Message definitions and catalogue*. <https://www.iso20022.org/iso-20022-message-definitions>
- SWIFT. *CBPR+ usage guidelines para pagos transfronterizos*. <https://www.swift.com/standards/iso-20022>
- ISO 20022. *External Code Sets: purpose codes y reason codes*. <https://www.iso20022.org/catalogue-messages/additional-content-messages/external-code-sets>
- Committee on Payments and Market Infrastructures (2018). *Cross-border retail payments*. BIS. <https://www.bis.org/cpmi/publ/d173.htm>
- Financial Action Task Force. *Recomendación 16 e información que debe acompañar a las transferencias*. FATF. <https://www.fatf-gafi.org/>
- Verificación local: comprueba qué versión de las guías de uso rige en tu red y qué campos regulatorios exige cada jurisdicción de destino. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 05 · Mensajería frente a movimiento de fondos](05-mensajeria-frente-a-movimiento-de-fondos.md) | [Parte 18](../README.md) · [Programa](../../../SYLLABUS.md) | [07 · Compensación, liquidación y finalidad →](07-compensacion-liquidacion-y-finalidad.md) |
<!-- gen:footer:end -->
