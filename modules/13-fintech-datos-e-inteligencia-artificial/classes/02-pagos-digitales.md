---
part: 14
class: 2
title: "Pagos digitales y dinero electrónico"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 02 · Pagos digitales y dinero electrónico

> [← 01 · Qué es fintech y cómo cambia la banca](01-que-es-fintech.md) · [Índice de la parte](../README.md) · [03 · Banca abierta y APIs →](03-banca-abierta-y-apis.md)

**Parte 14 — Fintech, datos e inteligencia artificial** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Dominar la capa donde se juega la mayor parte de la competencia digital en finanzas. Los pagos son la
puerta de entrada a la relación con el cliente, el generador de datos más rico del sistema y la función
donde la política pública ha intervenido con más fuerza.

El primer eslabón que se desagregó fue el pago, y esta clase explica por qué. Un pago parece un servicio simple y es una infraestructura con tres tipos de dinero distintos por debajo. Entender esa arquitectura es lo que permite ver por qué un pago inmediato cambia el negocio y un pago con tarjeta no.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** dinero de banco central, de banco comercial y electrónico.
2. **Describir** la arquitectura de un sistema de pagos inmediatos.
3. **Analizar** la economía de un pago y el reparto de sus ingresos.
4. **Evaluar** los códigos de respuesta rápida y la interoperabilidad.
5. **Identificar** los riesgos específicos de los pagos instantáneos.

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

Los tres primeros términos son los tipos de dinero; los cinco siguientes, la infraestructura y su economía. La **irrevocabilidad** es la característica que cambia el negocio: un pago inmediato e irrevocable elimina el riesgo del comercio y elimina también el mecanismo de contracargo que protegía al cliente.

| Concepto | Comprensión verificable |
|---|---|
| `dinero de banco central` | Reservas y efectivo; sin riesgo de crédito. |
| `dinero de banco comercial` | Depósitos; con riesgo del banco emisor. |
| `dinero electrónico` | Saldo emitido contra fondos recibidos, respaldado íntegramente. |
| `pago inmediato` | Liquidación en segundos, disponible todo el día. |
| `interoperabilidad` | Que cualquier usuario pueda pagar a cualquier otro. |
| `tasa de intercambio` | Comisión que el adquirente paga al emisor de la tarjeta. |
| `alias` | Identificador simple que sustituye al número de cuenta. |
| `irrevocabilidad` | Que el pago no pueda deshacerse una vez liquidado. |

## 🧠 Modelo mental

El modelo mental son tres dineros que se parecen y no lo son: el del banco central, el del banco comercial y el electrónico de un emisor no bancario. Un pago mueve uno de los tres, y el riesgo que asume quien lo recibe depende de cuál.

```text
TRES DINEROS QUE CIRCULAN A LA VEZ

  DE BANCO CENTRAL    reservas, efectivo
                      riesgo cero, acceso restringido
  DE BANCO COMERCIAL  depósitos
                      riesgo del banco, acceso universal
  ELECTRÓNICO         saldo en billeteras y emisores no bancarios
                      respaldado 1:1, no es depósito, sin seguro

UN PAGO ES SIEMPRE UNA TRANSFORMACIÓN ENTRE ESTOS DINEROS
  y la pregunta de riesgo es siempre la misma:
  ¿en qué dinero está el saldo del usuario
   y quién responde si el emisor falla?
```

**El dinero electrónico no está cubierto por el seguro de depósitos.** Su protección viene de la
obligación de respaldar el 100 % de los saldos en cuentas segregadas, y esa obligación —y su
verificación— es lo que separa un emisor seguro de uno que no lo es.

## 📖 Desarrollo

### 1. Arquitectura de pagos inmediatos

Un sistema de pagos inmediatos tiene componentes definidos y opera veinticuatro horas. El esquema lo recorre.

```text
COMPONENTES
  · esquema: reglas, participantes, tarifas
  · infraestructura de mensajería y compensación
  · liquidación en dinero de banco central
  · directorio de alias (teléfono, identificador, correo)
  · reglas de disputa y devolución
```

```text
FLUJO
  pagador → app del banco A → esquema → banco B → beneficiario
                                 ↓
                        liquidación en el banco central
                        (en tiempo real o diferida con garantías)

  tiempo total: segundos
  disponibilidad: 24 horas, todos los días
```

| Modelo de liquidación | Cómo funciona | Riesgo |
|---|---|---|
| Bruta en tiempo real | Cada pago se liquida individualmente | Necesidad de liquidez alta |
| Neta diferida con prefinanciamiento | Se compensa y se liquida por saldos | Riesgo de liquidación acotado |
| Híbrida | Neta con ciclos frecuentes y garantías | El más usado |

### 2. Economía de un pago con tarjeta

El pago con tarjeta reparte una comisión entre cuatro actores. El procedimiento siguiente la descompone.

```text
COMPRA DE 100 CON TARJETA

  comercio recibe                     97,60
  descuento del comercio               2,40
     ├── tasa de intercambio  1,50 → EMISOR (banco del tarjetahabiente)
     ├── comisión de la red   0,25 → RED DE TARJETAS
     └── margen del adquirente 0,65 → ADQUIRENTE

EL EMISOR RECIBE LA MAYOR PARTE
  y con ella financia: recompensas, fraude, plazo de pago, cobranza
```

```text
LA REGULACIÓN DE LA TASA DE INTERCAMBIO
  varias jurisdicciones la han limitado

  EFECTO OBSERVADO
    · baja el costo para el comercio
    · el emisor reduce recompensas y sube comisiones al usuario
    · el efecto sobre los precios finales al consumidor
      es difícil de aislar empíricamente

  es un caso donde una intervención bien fundada
  produce efectos redistributivos que hay que declarar
```

### 3. Códigos de respuesta rápida

Los códigos de respuesta rápida son la vía de menor costo para aceptar pagos, y tienen sus propios riesgos. La tabla los recoge.

| Modalidad | Cómo funciona | Ventaja | Riesgo |
|---|---|---|---|
| Estático del comercio | Un código fijo por comercio | Costo cero | Suplantación del código |
| Dinámico del comercio | Código con monto y referencia | Menos errores | Requiere terminal |
| Del pagador | El comercio escanea al cliente | Control del comercio | Requiere lector |
| Interoperable | Cualquier app lee cualquier código | Universalidad | Exige estándar común |

```text
LA INTEROPERABILIDAD ES LA VARIABLE DECISIVA
  sin ella, cada billetera crea su propia red
  y el comercio necesita aceptar todas

  con ella, el efecto de red pertenece al SISTEMA
  y no a un actor privado
  → por eso los bancos centrales la imponen
```

### 4. Riesgos del pago instantáneo

La inmediatez elimina la ventana de reversión y con ella varias protecciones. La tabla recoge los riesgos.

```text
IRREVOCABILIDAD + INMEDIATEZ = RIESGO DE FRAUDE ELEVADO

  el pago tradicional daba horas o días para detectar
  el pago inmediato da segundos

RIESGOS ESPECÍFICOS
  · fraude por inducción: el usuario paga voluntariamente
    a un estafador → no hay error técnico que revertir
  · suplantación de alias
  · errores de destinatario sin posibilidad de deshacer
  · uso para mover fondos de origen ilícito con rapidez
  · disponibilidad: un fallo detiene la economía de pagos
```

| Mitigante | Qué resuelve |
|---|---|
| Confirmación de nombre del beneficiario | Errores y suplantación de alias |
| Límites por transacción y por período | Magnitud del daño |
| Retardo voluntario para destinatarios nuevos | Ventana de detección |
| Análisis de comportamiento en tiempo real | Fraude por inducción |
| Reparto de responsabilidad entre bancos | Incentivo a invertir en prevención |
| Reglas de devolución para fraude confirmado | Reparación al cliente |

**El reparto de responsabilidad es el mitigante más potente y el más discutido.** Si el banco del
pagador responde siempre, no tiene incentivo el banco receptor —que es quien abrió la cuenta del
estafador— a controlar mejor. Los esquemas modernos reparten la responsabilidad entre ambos.

### 5. Dinero electrónico

El dinero electrónico no es un depósito y su protección es distinta. La tabla lo separa.

```text
OBLIGACIONES DE UN EMISOR DE DINERO ELECTRÓNICO
  · respaldo del 100 % de los saldos
  · fondos en cuentas SEGREGADAS del patrimonio propio
  · en activos de alta calidad y liquidez
  · conciliación diaria de saldos emitidos contra respaldo
  · prohibición de intermediación con esos fondos
  · información clara de que NO es un depósito

LO QUE UN EMISOR NO PUEDE HACER
  · prestar los fondos recibidos
  · pagar intereses sobre los saldos (en la mayoría de las normas)
  · usar los fondos para su operación
```

## 🧮 Ejemplo guiado

El ejemplo compara el costo y el riesgo de la misma operación por tres medios. Conviene mirar quién asume el riesgo en cada uno: cambia con el medio y no con el importe.

**Situación.** Un banco evalúa su posición en pagos tras la introducción del sistema inmediato.

```text
DATOS DEL AÑO
  transferencias inmediatas emitidas       46 M
  transferencias inmediatas recibidas      52 M
  comisión cobrada por emisión              0,00  (gratuito por norma)
  costo unitario de procesamiento           1,80
  saldos en cuenta corriente               84 000
  costo de fondos alternativo                6,2 %

FRAUDE
  casos de fraude por inducción              3 840
  monto reclamado                            1 240
  monto devuelto al cliente                    620
  costo de gestión                             180
```

**Paso 1 — fija la unidad antes de calcular.**

```text
CONVENCIÓN DEL EJERCICIO
  los importes de balance y resultado están en la unidad
  de los estados financieros; el costo unitario
  de procesamiento (1,80 unidades monetarias simples)
  equivale a 0,0018 en esa unidad

  hazlo siempre antes de multiplicar por un volumen
  de millones de transacciones: es donde se produce
  el error de escala más frecuente
```

```text
COSTO DE EMISIÓN:    46 M × 0,0018 = 82,8
COSTO DE RECEPCIÓN:  52 M × 0,0009 = 46,8
COSTO TOTAL DE PROCESAMIENTO:        129,6
```

**Paso 2 — calcula el ingreso indirecto.**

```text
EL SERVICIO ES GRATUITO PARA EL CLIENTE
¿QUÉ GANA EL BANCO?

  1. los saldos en cuenta corriente
     84 000 × 6,2 % = 5 208 de margen de captación

  2. la relación: el cliente que paga por el banco
     mantiene el banco como principal

  3. los datos de flujo, que alimentan el crédito (clase 7)
```

**Paso 3 — evalúa el efecto neto.**

```text
costo de procesamiento:                     −129,6
costo del fraude (devoluciones + gestión):  −800,0
margen de captación atribuible:            +5 208,0

el servicio es rentable POR LOS SALDOS
no por el servicio en sí
```

**Paso 4 — analiza el fraude en detalle.**

```text
3 840 casos, 1 240 reclamados, 620 devueltos

tasa de fraude: 3 840 / 46 M = 0,0083 %
monto medio por caso: 1 240/3 840 = 0,32

DISTRIBUCIÓN POR TIPO
  inducción (el cliente paga voluntariamente):  2 980  (78 %)
  suplantación de credenciales:                   540  (14 %)
  error de destinatario:                          320   (8 %)
```

**Paso 5 — evalúa los mitigantes disponibles.**

```text
CONFIRMACIÓN DE NOMBRE DEL BENEFICIARIO
  antes de confirmar, la app muestra el nombre
  asociado a la cuenta de destino
  efecto esperado: reduce errores (100 %) y parte de la inducción (35 %)
  casos evitados: 320 + 1 043 = 1 363
  monto evitado: 1 363 × 0,32 = 436
  costo de implantación: 340 inicial + 60 anuales

RETARDO PARA DESTINATARIOS NUEVOS
  primer pago a un destinatario nuevo: 30 minutos de retardo
  con opción de cancelar
  efecto: reduce inducción en 28 % adicional
  casos evitados: 834
  monto evitado: 267
  costo: 90 de desarrollo
  costo indirecto: fricción en pagos legítimos

ANÁLISIS DE COMPORTAMIENTO EN TIEMPO REAL
  detecta patrones de inducción (pago inusual,
  destinatario nuevo, monto atípico, urgencia)
  efecto: 22 % adicional de la inducción
  costo: 620 inicial + 180 anuales
```

**Paso 6 — evalúa la combinación.**

```text
                        casos evit.  monto evit.  costo anual
confirmación de nombre      1 363        436         60
retardo destinatario nuevo    834        267          8
análisis de comportamiento    655        210        180
TOTAL (sin solapamiento
completo, factor 0,85)      2 425        776        248

pérdida actual: 800
pérdida residual: 800 − 776 × (620/1 240) = 800 − 388 = 412
   (el monto evitado se aplica proporcionalmente
    a lo que el banco efectivamente devuelve)
AHORRO: 388 anuales
COSTO: 248 anuales
BENEFICIO NETO: 140 anuales
```

**Paso 7 — considera lo que el cálculo no captura.**

```text
EFECTOS NO CUANTIFICADOS
  · 3 840 clientes al año viven un fraude
    de los cuales 2 240 no reciben devolución
    → efecto en confianza y en permanencia
  · reputación: el fraude por inducción es noticia
  · exposición regulatoria: varias jurisdicciones
    están imponiendo reembolso obligatorio
    → si eso ocurre, la pérdida pasa de 620 a 1 240

ESCENARIO CON REEMBOLSO OBLIGATORIO
  pérdida sin mitigantes: 1 240 + 180 = 1 420
  pérdida con mitigantes: 1 420 − 776 = 644
  ahorro: 776 anuales contra costo de 248
  BENEFICIO NETO: 528 anuales
```

**Paso 8 — decide.**

```text
IMPLANTAR LOS TRES MITIGANTES

JUSTIFICACIÓN
  · beneficio neto positivo con el régimen actual (140)
  · beneficio muy superior si el reembolso se vuelve
    obligatorio (528), escenario probable
  · efecto sobre la confianza, no cuantificado pero real
  · la confirmación de nombre está siendo exigida
    por reguladores en varias jurisdicciones:
    anticiparse cuesta menos que reaccionar

ADICIONALMENTE
  · negociar con el esquema el reparto de responsabilidad
    con el banco receptor: el 68 % de las cuentas de destino
    de los fraudes están en tres entidades
  · reportar esa concentración al supervisor
```

**Interpreta:** el servicio de pagos inmediatos **no genera ingreso directo y es rentable por los saldos
que retiene**, y su principal costo no es el procesamiento sino el fraude. La decisión de invertir en
mitigantes fue positiva con el régimen actual y claramente positiva bajo el régimen que probablemente
venga. Anticipar el cambio regulatorio es aquí una decisión económica, no una precaución.

## 🏦 Del cliente al banco

El cliente paga con el móvil y el banco pierde o gana según qué infraestructura se use. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Transferir es instantáneo y gratis» | Costo sin ingreso directo | 14, clase 2 |
| «Me estafaron y el banco no devuelve» | Fraude por inducción y su régimen | 4, clase 4 |
| «La app me muestra el nombre del destinatario» | Mitigante de mayor efecto | 14, clase 2 |
| «Mi saldo en la billetera no está asegurado» | Dinero electrónico, no depósito | 14, clase 2 |
| «El comercio no acepta mi app» | Falta de interoperabilidad | 14, clase 2 |

## 🧪 Práctica

El laboratorio pide comparar tres medios por costo, velocidad y protección. Ningún medio gana en las tres dimensiones.

En `labs/lab-01.md`, sección de pagos:

1. Distingue los tres dineros en cinco situaciones concretas.
2. Descompón la economía de un pago con tarjeta entre sus participantes.
3. Evalúa tres mitigantes de fraude por su costo y efecto.
4. Analiza el efecto de un régimen de reembolso obligatorio.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen problemas con pagos inmediatos. La causa es casi siempre la irrevocabilidad no comprendida.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se evalúa el pago por su ingreso directo | Es cero por norma | Mide saldos y relación. |
| Se trata el saldo de billetera como depósito | No lo es | Verifica el respaldo y la segregación. |
| Solo el banco pagador responde por fraude | El receptor no tiene incentivo | Reparto de responsabilidad. |
| Se ignora el fraude por inducción | No hay error técnico | Es el 78 % de los casos. |
| Se compite sin interoperabilidad | Red propia sin escala | La interoperabilidad es del sistema. |
| Se reacciona al cambio regulatorio | Más caro | Anticípalo cuando es previsible. |

## ❓ Preguntas de comprobación

1. ¿Qué distingue el dinero electrónico de un depósito bancario?
2. ¿Quién recibe la mayor parte del descuento del comercio y para qué la usa?
3. ¿Por qué la interoperabilidad cambia a quién pertenece el efecto de red?
4. ¿Qué hace tan difícil de combatir el fraude por inducción?
5. ¿Por qué el reparto de responsabilidad entre bancos es un mitigante potente?

## 📥 Entregable

Guarda en `portfolio/parte-14/clase-02/`:

- la clasificación de los tres dineros en cinco situaciones;
- la descomposición de la economía de un pago con tarjeta;
- la evaluación de mitigantes con su costo y efecto;
- el análisis del escenario de reembolso obligatorio.

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

- Committee on Payments and Market Infrastructures (2016). *Fast payments — Enhancing the speed and availability of retail payments*. BIS. <https://www.bis.org/cpmi/publ/d154.htm>
- Committee on Payments and Market Infrastructures e IOSCO (2012). *Principles for Financial Market Infrastructures*. BIS. <https://www.bis.org/cpmi/publ/d101.htm>
- Bank for International Settlements (2020). *Payment aspects of financial inclusion in the fintech era*. CPMI y Banco Mundial.
- Rochet, J. y Tirole, J. (2006). "Two-sided markets: a progress report". *RAND Journal of Economics*, 37(3). Economía de las redes de pago.
- Financial Stability Board (2020). *Enhancing Cross-border Payments*. FSB.
- Verificación local: revisa el esquema de pagos inmediatos de tu país, sus reglas de disputa, los límites aplicables y el régimen de emisores de dinero electrónico.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 01 · Qué es fintech y cómo cambia la banca](01-que-es-fintech.md) | [Parte 14](../README.md) · [Programa](../../../SYLLABUS.md) | [03 · Banca abierta y APIs →](03-banca-abierta-y-apis.md) |
<!-- gen:footer:end -->
