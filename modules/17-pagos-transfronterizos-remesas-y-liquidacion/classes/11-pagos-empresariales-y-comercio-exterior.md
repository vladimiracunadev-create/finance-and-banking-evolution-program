---
part: 18
class: 11
title: "Pagos empresariales y comercio exterior"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global, chile]
regulatory_topics: [cross-border-payments, comercio-exterior, cambios-internacionales]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [Banco Central de Chile, CCI]
requires_legal_review: true
---

<!-- gen:header:start -->
# Clase 11 · Pagos empresariales y comercio exterior

> [← 10 · Remesas y corredores internacionales](10-remesas-y-corredores-internacionales.md) · [Índice de la parte](../README.md) · [12 · AML, sanciones y regla del viaje →](12-aml-sanciones-y-regla-del-viaje.md)

**Parte 18 — Pagos transfronterizos, remesas y liquidación internacional** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Pasar del pago de 300 dólares al pago de 300 000. Cambian el riesgo dominante,
los instrumentos, la documentación y la pregunta central: ya no es «cuánto
cuesta», sino **quién asume el riesgo de que la otra parte no cumpla**.

## 📚 Objetivos

Al finalizar podrás:

1. **Situar** cada instrumento de comercio exterior en el eje de confianza entre
   las partes.
2. **Explicar** cómo una carta de crédito traslada el riesgo comercial a riesgo
   bancario.
3. **Calcular** el coste financiero completo de una operación, incluido el
   capital inmovilizado.
4. **Identificar** los puntos donde una discrepancia documental detiene un cobro.
5. **Diseñar** la conciliación de cobros con la referencia estructurada.

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

Los cuatro primeros términos son las formas de pago según la confianza entre las partes; los cuatro siguientes, los instrumentos documentales y su automatización. La **cuenta abierta** es la que más volumen mueve y menos protección da, y por eso convive con la financiación de la cadena de suministro.

| Concepto | Comprensión verificable |
|---|---|
| `cuenta abierta` | El exportador envía y cobra después, sin garantía |
| `pago anticipado` | El importador paga antes de recibir |
| `cobranza documentaria` | El banco entrega documentos contra pago o aceptación |
| `carta de crédito` | Compromiso de pago de un banco si se presentan documentos conformes |
| `discrepancia` | Diferencia entre los documentos y lo exigido por el crédito |
| `garantía a primer requerimiento` | Pago contra reclamación, sin discutir el fondo |
| `financiación de la cadena de suministro` | Adelanto de cobro con el riesgo del comprador |
| `conciliación automática` | Casar cobro y factura sin intervención manual |

## 🧠 Modelo mental

El modelo mental es una escala de confianza: cuanto menos se conocen las partes, más caro y más documental es el instrumento. Elegirlo es una decisión de riesgo y no de trámite.

```text
LOS INSTRUMENTOS SE ORDENAN EN UN SOLO EJE:
CUÁNTO CONFÍAN LAS PARTES ENTRE SÍ

  máxima confianza          CUENTA ABIERTA
    riesgo del exportador (envía y espera cobrar)
                    │
                    │  COBRANZA DOCUMENTARIA
                    │    el banco controla los documentos
                    │    pero NO garantiza el pago
                    │
                    │  CARTA DE CRÉDITO
                    │    un banco SE OBLIGA a pagar
                    │    contra documentos conformes
                    ▼
  mínima confianza          PAGO ANTICIPADO
    riesgo del importador (paga y espera recibir)

EL COSTE SIGUE EL MISMO EJE, AL REVÉS
  cuanta menos confianza, más instrumento,
  y más caro
```

## 📖 Desarrollo

### 1. Los cuatro instrumentos, comparados

| Instrumento | Riesgo del exportador | Riesgo del importador | Coste | Cuándo |
|---|---|---|---|---|
| Pago anticipado | Ninguno | Alto | Bajo | Comprador nuevo o sin poder |
| Carta de crédito | Bajo (banco emisor) | Bajo | Alto | Partes sin relación previa |
| Cobranza documentaria | Medio | Medio | Medio | Relación en construcción |
| Cuenta abierta | Alto | Ninguno | Muy bajo | Relación consolidada |

```text
LA MAYOR PARTE DEL COMERCIO MUNDIAL
SE HACE EN CUENTA ABIERTA

  no porque no haya riesgo, sino porque
  la relación comercial repetida es la garantía

  y porque la carta de crédito es cara y lenta:
  se reserva para operaciones grandes,
  contrapartes nuevas o mercados difíciles
```

### 2. Cómo funciona una carta de crédito

```text
1. importador y exportador acuerdan pagar con crédito documentario
2. el importador pide a SU banco que emita el crédito
3. el banco emisor se OBLIGA a pagar si se presentan
   documentos conformes con lo que el crédito exige
4. el crédito llega al exportador a través de un banco avisador
5. el exportador embarca y presenta los documentos
6. el banco EXAMINA LOS DOCUMENTOS, no la mercancía
7. si son conformes, paga

LA FRASE QUE HAY QUE ENTENDER
  el banco paga contra DOCUMENTOS, no contra mercancía.
  Si los documentos son conformes y la mercancía es basura,
  el banco paga igual.
  Si la mercancía es perfecta y falta una firma, no paga.

  → el crédito documentario traslada el riesgo COMERCIAL
    a riesgo BANCARIO, y añade un riesgo nuevo:
    el riesgo DOCUMENTAL
```

### 3. Las discrepancias

```text
LAS MÁS FRECUENTES

  · documentos presentados fuera de plazo
  · descripción de la mercancía distinta de la del crédito
  · importe o cantidad fuera de tolerancia
  · puerto de embarque o destino distintos
  · falta de un documento exigido
  · fechas incoherentes entre documentos
  · seguro por importe insuficiente
  · firma o endoso ausente

QUÉ PASA CUANDO HAY DISCREPANCIA
  el banco NO está obligado a pagar
  → consulta al importador si acepta
  → si acepta, paga; si no, devuelve documentos

  y mientras tanto:
    la mercancía está en destino, generando almacenaje
    el exportador no cobra
    el importador tiene poder de negociación sobre el precio

UNA PROPORCIÓN MUY ALTA DE PRIMERAS PRESENTACIONES
TIENE ALGUNA DISCREPANCIA. Verifica la cifra vigente
en la fuente: es un indicador que se publica y varía.
```

### 4. El coste financiero completo

```text
NO ES SOLO LA COMISIÓN

  COMISIONES
    emisión, aviso, confirmación, examen de documentos,
    modificación, discrepancia

  COSTE DE OPORTUNIDAD
    el importador puede tener que inmovilizar garantía
    o consumir su línea de crédito

  COSTE DE PLAZO
    el exportador cobra días o semanas después del embarque
    → financia esa diferencia

  COSTE DE CAMBIO
    si la factura está en otra divisa, hay exposición
    entre el contrato y el cobro

  COSTE DE DISCREPANCIA
    almacenaje, demoras, renegociación del precio
```

### 5. Conciliación: el problema silencioso

```text
UNA EMPRESA CON 400 COBROS INTERNACIONALES AL MES
TIENE UN PROBLEMA QUE NO ES DE PAGOS: ES DE CASAR

  el cobro llega con
    · un importe que no coincide (comisiones deducidas)
    · una referencia truncada o alterada
    · varias facturas en un solo pago
    · el nombre del ordenante distinto del cliente

  RESULTADO
    cobros sin aplicar, clientes reclamados por error,
    y días de trabajo manual

LA SOLUCIÓN ESTÁ EN LA CLASE 6
  referencia estructurada, información de remesa,
  identificador extremo a extremo estable

  → el problema de conciliación de una empresa
    se resuelve en el diseño del mensaje del banco
```

## 🧮 Ejemplo guiado

El ejemplo compara el coste y la protección de tres instrumentos sobre la misma operación. La protección se paga, y cuantificarla es lo que permite decidir.

**Situación.** Una empresa exportadora de 8 millones de dólares anuales evalúa
cambiar de carta de crédito a cuenta abierta con su principal cliente.

```text
RELACIÓN ACTUAL
  cliente desde hace 4 años
  operaciones al año                      24
  importe medio por operación        180 000 USD
  volumen con este cliente         4 320 000 USD
  impagos históricos                       0
  retrasos de más de 30 días               2 (año 1)

COSTES ACTUALES CON CARTA DE CRÉDITO
  comisión de aviso            0,15 % sobre el importe
  comisión de confirmación     0,90 % anual sobre 60 días
  examen de documentos              280 USD por operación
  discrepancias (35 % de las operaciones)
      comisión                      180 USD
      demora media                    9 días

PLAZOS
  con carta de crédito: cobro a 18 días del embarque
  en cuenta abierta:    cobro a 45 días del embarque

COSTE DE FINANCIACIÓN DE LA EMPRESA: 7,2 % anual
```

**Paso 1 — calcula el coste actual por operación.**

```text
COMISIONES
  aviso:         180 000 × 0,15 %              = 270,00
  confirmación:  180 000 × 0,90 % × (60/365)   = 266,30
  examen                                        = 280,00
  discrepancia:  180 × 35 %                     =  63,00
  SUBTOTAL COMISIONES                             879,30

COSTE FINANCIERO DEL PLAZO
  días medios = 18 + (9 × 35 %) = 21,15 días
  180 000 × 7,2 % × (21,15/365)                = 750,90

COSTE TOTAL POR OPERACIÓN                       1 630,20
ANUAL (24 operaciones)                         39 124,80
```

**Paso 2 — calcula el coste en cuenta abierta.**

```text
COMISIONES
  transferencia internacional recibida            45,00
  SUBTOTAL                                        45,00

COSTE FINANCIERO DEL PLAZO
  180 000 × 7,2 % × (45/365)                   1 597,80

COSTE TOTAL POR OPERACIÓN                       1 642,80
ANUAL                                          39 427,20
```

**Paso 3 — detente: el resultado es contraintuitivo.**

```text
CUENTA ABIERTA CUESTA 302 USD MÁS AL AÑO

  ¿POR QUÉ, SI NO TIENE COMISIONES?

  porque el plazo pasa de 21 a 45 días.
  El coste financiero del plazo adicional
  (1 597,80 − 750,90 = 846,90) supera
  el ahorro en comisiones (879,30 − 45,00 = 834,30)

LA LECCIÓN
  el instrumento no solo cambia el riesgo:
  cambia CUÁNDO SE COBRA, y eso tiene precio
```

**Paso 4 — introduce el riesgo, que es lo que falta.**

```text
EL CÁLCULO ANTERIOR IGNORA EL RIESGO DE IMPAGO

  con carta de crédito confirmada:
    el riesgo es del banco confirmador
    probabilidad de impago: muy baja

  en cuenta abierta:
    el riesgo es del cliente
    4 años sin impagos NO significa probabilidad cero

  ESTIMACIÓN PRUDENTE
    probabilidad anual de impago de un cliente
    comercial consolidado: supongamos 0,8 %
    exposición media: 180 000 × (45/365) × 24 = 532 603 USD
    ... no: la exposición es la de las operaciones vivas

    operaciones vivas simultáneas: 24 × (45/365) ≈ 2,96
    exposición media: 2,96 × 180 000 = 532 800 USD

  PÉRDIDA ESPERADA
    532 800 × 0,8 % × (1 − 0,35 de recuperación)
    = 532 800 × 0,8 % × 0,65 = 2 770,56 USD/año
```

**Paso 5 — recalcula con el riesgo.**

```text
CUENTA ABIERTA
  coste operativo y financiero    39 427,20
  pérdida esperada                 2 770,56
  TOTAL                           42 197,76

CARTA DE CRÉDITO
  TOTAL                           39 124,80

DIFERENCIA: la carta de crédito es 3 072,96 USD más barata
```

**Paso 6 — busca la tercera opción.**

```text
NINGUNA DE LAS DOS ES ÓPTIMA. HAY UNA TERCERA.

  CUENTA ABIERTA + SEGURO DE CRÉDITO
    prima estimada: 0,45 % sobre el volumen asegurado
    4 320 000 × 0,45 % = 19 440 USD/año

    → demasiado caro para este caso

  CUENTA ABIERTA + PLAZO NEGOCIADO A 30 DÍAS
    coste financiero: 180 000 × 7,2 % × (30/365) = 1 065,20
    total operativo: (45 + 1 065,20) × 24 = 26 644,80
    más pérdida esperada ajustada:
      exposición: 24 × (30/365) × 180 000 = 355 068
      355 068 × 0,8 % × 0,65 = 1 846,35
    TOTAL: 28 491,15 USD

    AHORRO frente a la carta de crédito: 10 633,65 USD/año

  CUENTA ABIERTA + DESCUENTO POR PRONTO PAGO
    ofrecer 1 % de descuento por pago a 10 días
    coste del descuento: 180 000 × 1 % × 24 = 43 200 USD
    → mucho más caro que financiar 35 días
    (1 % a 35 días equivale a 10,4 % anual)
```

**Paso 7 — decide.**

```text
CUENTA ABIERTA A 30 DÍAS, NO A 45

  AHORRO: 10 634 USD/año frente a la situación actual

  CONDICIONES
    1. límite de crédito por cliente: 600 000 USD
    2. seguimiento mensual del comportamiento de pago
    3. cláusula de retorno a carta de crédito ante
       un retraso superior a 15 días
    4. revisión anual del límite y de la probabilidad
       de impago con datos propios

  Y UNA ADVERTENCIA SOBRE EL MÉTODO
    la probabilidad de impago del 0,8 % es un SUPUESTO.
    Con 0,3 % la cuenta abierta a 45 días ya sería
    mejor que la carta de crédito; con 2,0 %, ninguna
    versión de cuenta abierta lo sería.

    → el número que decide es el que no tenemos.
      Se declara, y se sustituye por datos propios
      en cuanto haya suficientes operaciones.
```

**Interpreta:** el cambio de instrumento parecía una decisión de comisiones y era
una decisión de **plazo y de riesgo de crédito**. El ahorro apareció al negociar
el plazo, no al cambiar el instrumento.

## 🧭 Perspectivas

El instrumento afecta a cada parte de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Exportador | Cobra a 45 días sin garantía | Qué instrumento acepta |
| Importador | Inmoviliza garantía con el crédito | Qué instrumento propone |
| Banco emisor | Obligación de pago propia | Si emite y con qué garantía |
| Banco confirmador | Riesgo del banco emisor y del país | Si confirma |
| Aseguradora de crédito | Riesgo del comprador | Prima y límite |
| Tesorería del exportador | 35 días adicionales de financiación | Cómo los financia |
| Banco central | Operación de comercio exterior | Qué debe informarse |

## 🏦 Del cliente al banco

El exportador quiere cobrar seguro y el banco asume una obligación documental. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Me rechazaron los documentos» | Discrepancia documental | 18, clase 11 |
| «No sé de qué factura es el cobro» | Referencia sin estructurar | 18, clases 6 y 11 |
| «Prefiero cuenta abierta» | Cambia el plazo y el riesgo | 18, clase 11 |
| «El banco pagó y la mercancía era mala» | El banco examina documentos | 18, clase 11 |

## ⚖️ Riesgos y controles

Los riesgos son documentales y de contraparte. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Riesgo documental | Discrepancia detiene el cobro | Lista de verificación antes de presentar |
| Riesgo de crédito comercial | El comprador no paga | Límite por cliente y seguimiento |
| Riesgo de plazo | El coste financiero supera el ahorro | Calcular el coste del plazo, siempre |
| Riesgo de cambio | Factura en otra divisa | Cobertura desde el contrato |
| Conciliación manual | Cobros sin aplicar | Referencia estructurada exigida |
| Probabilidad supuesta | Se decide con un número inventado | Declararlo y sustituirlo con datos propios |

## 🧪 Práctica

En [`labs/lab-03.md`](../labs/lab-03.md) y el [proyecto](../project/README.md):

1. Sitúa cinco operaciones en el eje de confianza y elige el instrumento.
2. Calcula el coste completo de dos instrumentos, incluido el plazo.
3. Modela la pérdida esperada con tres probabilidades de impago.
4. Diseña la referencia estructurada que permitiría conciliar sin intervención.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen operaciones de comercio exterior que fallaron. La causa suele ser el instrumento elegido por costumbre.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Comparar solo comisiones | Se ignoró el coste del plazo | Incluye la financiación |
| «Cuenta abierta es gratis» | No se contó el riesgo | Añade la pérdida esperada |
| Creer que el banco revisa la mercancía | Se confundió el objeto del examen | Documentos, no mercancía |
| Descuento por pronto pago sin anualizar | Parece pequeño | 1 % a 35 días es 10,4 % anual |
| Referencia libre en la factura | Se dejó al cliente | Exige formato estructurado |
| Decidir con una probabilidad inventada | No había datos | Declárala y mide |

## ❓ Preguntas de comprobación

1. ¿Cómo se ordenan los cuatro instrumentos y qué eje los ordena?
2. ¿Por qué un banco paga una carta de crédito aunque la mercancía sea
   defectuosa?
3. ¿Por qué cuenta abierta puede salir más cara que una carta de crédito?
4. ¿Cómo se calcula la pérdida esperada de una relación en cuenta abierta?
5. En el ejemplo guiado, ¿qué número decidía el resultado y por qué se declaró?

## 📥 Entregable

Guarda en `portfolio/parte-18/clase-11/`:

- cinco operaciones situadas en el eje, con el instrumento elegido;
- el coste completo de dos instrumentos, con el plazo incluido;
- la pérdida esperada con tres probabilidades y su efecto en la decisión;
- el diseño de la referencia estructurada para conciliación automática.

## 🔗 Referencias cruzadas

- **Viene de:** clases 6 y 9; Parte 13 (finanzas corporativas); Parte 9
  (riesgo de crédito).
- **Continúa en:** clase 12 (cumplimiento), clase 16 (proyecto).
- **Se aplica en:** Parte 21, clase 7 (facturas tokenizadas); Parte 23, clase 8.

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

- Cámara de Comercio Internacional. *Reglas uniformes relativas a los créditos documentarios (UCP 600)* y *Reglas uniformes para las cobranzas (URC 522)*. ICC. <https://iccwbo.org/>
- Cámara de Comercio Internacional. *Trade Register Report*. ICC. <https://iccwbo.org/>
- Basel Committee on Banking Supervision (2014). *Treatment of trade finance under the Basel capital framework*. BIS. <https://www.bis.org/publ/bcbs205.htm>
- Organización Mundial del Comercio. *Trade finance and SMEs*. OMC. <https://www.wto.org/>
- Banco Central de Chile. *Capítulo del Compendio de Normas de Cambios Internacionales sobre operaciones de comercio exterior*. <https://www.bcentral.cl/>
- Verificación local: comprueba qué operaciones de comercio exterior deben informarse al banco central y qué documentación de respaldo se exige. **Fecha de verificación de esta clase: 2026-08-06.** Esta clase no constituye asesoría legal.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 10 · Remesas y corredores internacionales](10-remesas-y-corredores-internacionales.md) | [Parte 18](../README.md) · [Programa](../../../SYLLABUS.md) | [12 · AML, sanciones y regla del viaje →](12-aml-sanciones-y-regla-del-viaje.md) |
<!-- gen:footer:end -->
