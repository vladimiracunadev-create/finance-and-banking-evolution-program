---
part: 10
class: 9
title: "Medios de pago"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 09 · Medios de pago

> [← 08 · Conciliación bancaria](08-conciliacion-bancaria.md) · [Índice de la parte](../README.md) · [10 · Tarjetas y adquirencia →](10-tarjetas-y-adquirencia.md)

**Parte 10 — Operaciones bancarias** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Comprender el ecosistema de pagos desde la perspectiva del banco: qué medios existen, cómo se
monetizan, qué riesgos generan y cómo compiten entre sí. El negocio de pagos es de alto volumen y
bajo margen unitario, y su rentabilidad depende de escala y de eficiencia operativa.

Las clases anteriores tratan operaciones concretas. Esta las mira como un mercado: qué medios existen, cuánto cuesta cada uno y por qué el que gana no siempre es el más barato. Es la clase que explica la economía de los pagos, que es la base de la Parte 18 y de buena parte de la Parte 14.

## 📚 Objetivos

Al finalizar podrás:

1. **Clasificar** los medios de pago por tecnología, costo y riesgo.
2. **Descomponer** los ingresos y costos de cada medio.
3. **Evaluar** la competencia entre medios y su evolución.
4. **Identificar** los riesgos operacionales y de fraude por medio.
5. **Diseñar** una estrategia de medios de pago para un segmento.

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

Los tres primeros términos son la estructura de costos del sistema; los cuatro siguientes, sus características técnicas y comerciales. La **tasa de intercambio** es la pieza que explica el modelo de negocio de las tarjetas y por qué su precio se regula en tantos países.

| Concepto | Comprensión verificable |
|---|---|
| `medio de pago` | Instrumento que permite transferir valor entre partes. |
| `tasa de intercambio` | Comisión que el adquirente paga al emisor por cada transacción con tarjeta. |
| `comisión de adquirencia` | Lo que paga el comercio por aceptar el medio. |
| `costo por transacción` | Costo operativo unitario de procesar un pago. |
| `interoperabilidad` | Capacidad de un medio de funcionar entre distintos participantes. |
| `tokenización` | Sustitución del identificador real por uno de uso limitado. |
| `pago inmediato` | Transferencia de bajo monto disponible en segundos. |

## 🧠 Modelo mental

Cada medio de pago se evalúa en **cuatro dimensiones**:

```text
COSTO para el pagador
COSTO para el receptor
VELOCIDAD de disponibilidad
IRREVOCABILIDAD y protección ante disputa
```

Ningún medio es superior en las cuatro. La tarjeta de crédito ofrece protección al pagador y cuesta
caro al comercio; la transferencia inmediata es barata y no ofrece contracargo. **La elección del medio
es un intercambio, no una jerarquía.**

## 📖 Desarrollo

### 1. Panorama de medios

Los medios de pago se comparan por costo, velocidad, alcance y reversibilidad. La tabla los enfrenta.

| Medio | Costo comercio | Velocidad | Protección al pagador | Uso típico |
|---|---|---|---|---|
| Efectivo | Bajo (manejo) | Inmediata | Ninguna | Bajo monto, presencial |
| Cheque | Bajo | Días | Limitada | Empresas, en declive |
| Tarjeta de débito | Medio | 1–3 días | Media | Consumo cotidiano |
| Tarjeta de crédito | Alto | 1–3 días | **Alta** | Consumo, en línea |
| Transferencia | Muy bajo | Minutos a 1 día | Baja | Entre personas, empresas |
| Pago inmediato | Muy bajo | Segundos | Baja | Persona a persona, comercio |
| Billetera digital | Variable | Según medio subyacente | Según medio | Presencial y en línea |
| Débito automático | Muy bajo | Programado | Media | Servicios recurrentes |

### 2. Economía del negocio

**Tarjetas — flujo de la comisión:**

```text
compra de 100 000 con tarjeta de crédito

comercio recibe                    97 800  (comisión de adquirencia 2,2 %)
  de los 2 200 de comisión:
    tasa de intercambio al emisor   1 500  (68 %)
    comisión de la marca              180  (8 %)
    margen del adquirente             520  (24 %)
```

**El emisor recibe la mayor parte**, y con ella financia los beneficios al tarjetahabiente, el
periodo de gracia y el riesgo de crédito.

**Transferencias — economía distinta:**

```text
costo de procesar una transferencia: 15 a 60 unidades monetarias
ingreso: comisión al ordenante (frecuentemente cero en canal digital)

el negocio NO está en la comisión: está en
  · retener el saldo transaccional (fondeo barato)
  · la relación y la venta cruzada
  · los datos de comportamiento
```

### 3. Competencia entre medios

Los medios compiten en dimensiones distintas y la elección del comercio no es la del cliente. La tabla recoge esa tensión.

```text
tendencias documentadas en la mayoría de los mercados:
  · el efectivo pierde participación de forma sostenida
  · el cheque está en declive acelerado
  · las tarjetas crecen en volumen y pierden margen unitario
  · los pagos inmediatos crecen muy rápido donde existen
  · las billeteras digitales concentran la experiencia del usuario
```

**El efecto competitivo de los pagos inmediatos sobre las tarjetas:**

```text
si un pago inmediato cuesta al comercio 0,1 % y una tarjeta 2,2 %,
el comercio tiene incentivo a promover el primero

contramedidas de los emisores:
  · beneficios al tarjetahabiente (puntos, descuentos, cuotas)
  · protección ante disputa que el pago inmediato no ofrece
  · financiamiento (el pago inmediato es débito puro)
```

**El diferenciador estructural de la tarjeta de crédito es el crédito**, no el pago. Donde el pago
inmediato compite, la tarjeta debe apoyarse en su componente de financiamiento y de protección.

### 4. Riesgos por medio

Cada medio tiene su perfil de riesgo y su forma de fraude característica. La tabla los recoge.

| Medio | Riesgo principal | Control |
|---|---|---|
| Efectivo | Robo, falsificación | Seguridad física, detectores |
| Cheque | Adulteración, protesto | Verificación, canje |
| Tarjeta presencial | Clonación, uso indebido | Chip, tokenización, límites |
| Tarjeta en línea | Uso de datos robados | Autenticación reforzada, tokenización |
| Transferencia | Desvío por ingeniería social | Verificación de beneficiario |
| Pago inmediato | Irrevocabilidad ante fraude | Límites, retención, educación |
| Billetera | Compromiso del dispositivo | Biometría, tokenización |
| Débito automático | Cargo no autorizado | Mandato verificable, derecho a revocar |

**El riesgo de los pagos inmediatos merece atención:** su velocidad e irrevocabilidad los hace
atractivos para el fraude por ingeniería social. La víctima autoriza el pago y el dinero es
irrecuperable en segundos.

### 5. Estrategia por segmento

El medio que conviene depende del segmento y del tipo de operación. La tabla los relaciona.

```text
PERSONAS DE CONSUMO COTIDIANO
  objetivo: ser el medio por defecto
  · tarjeta de débito sin costo con notificaciones
  · billetera digital integrada
  · pagos inmediatos gratuitos
  monetización: fondeo transaccional y venta cruzada

PERSONAS DE ALTO CONSUMO
  objetivo: capturar el gasto
  · tarjeta de crédito con beneficios
  · cuotas sin interés en comercios aliados
  monetización: intercambio, financiamiento, comisiones

MICROEMPRESA Y COMERCIO PEQUEÑO
  objetivo: ser su medio de cobro
  · terminal de bajo costo o cobro por código
  · abono rápido de las ventas
  monetización: adquirencia y datos de venta para crédito

EMPRESAS
  objetivo: ser su plataforma de pagos
  · pagos masivos, nómina, proveedores
  · integración con sus sistemas
  monetización: comisiones por servicio y saldos transaccionales
```

## 🧮 Ejemplo guiado

**Situación.** Un banco evalúa el efecto de la entrada de pagos inmediatos en su negocio de tarjetas.

```text
SITUACIÓN ACTUAL (anual, millones)
  volumen transaccional con tarjeta de débito     4 200 000
  volumen con tarjeta de crédito                  2 800 000
  ingreso por intercambio (emisor)                   62 400
  ingreso por adquirencia                            38 200
  costo operativo de procesamiento                   28 600
  RESULTADO DEL NEGOCIO DE PAGOS                     72 000
```

**Paso 1 — estima la migración.**

```text
experiencia de mercados comparables tras la introducción de pagos inmediatos:
  · migración del débito: 25 % a 40 % del volumen en 3 años
  · migración del crédito: 8 % a 15 % (menor, por el componente de financiamiento)

escenario base a 3 años:
  débito migrado:  4 200 000 × 0,32 = 1 344 000
  crédito migrado: 2 800 000 × 0,11 =   308 000
```

**Paso 2 — cuantifica el efecto en el ingreso.**

```text
ingreso por intercambio perdido:
  débito (tasa 0,60 %):   1 344 000 × 0,0060 =  8 064
  crédito (tasa 1,50 %):    308 000 × 0,0150 =  4 620
  TOTAL                                        12 684

ingreso por adquirencia perdido:
  el comercio migra a un medio de menor comisión
  1 652 000 × (0,022 − 0,001) = 34 692... 
```

Corrigiendo: el volumen migrado como adquirente no es el mismo que como emisor.

```text
volumen adquirido por el banco: 1 900 000
migración estimada: 32 % = 608 000
ingreso perdido: 608 000 × (0,022 − 0,001) = 12 768
```

```text
INGRESO TOTAL PERDIDO: 12 684 + 12 768 = 25 452  (25 % del ingreso del negocio)
```

**Paso 3 — cuantifica el efecto en los costos.**

```text
el costo de procesar un pago inmediato es menor que el de una tarjeta:
  costo por transacción con tarjeta:     42 unidades
  costo por transacción con pago inmediato: 11 unidades

transacciones migradas: 1 652 000 millones / ticket promedio 28 000 = 59 millones de transacciones
ahorro de costo: 59 000 000 × (42 − 11) = 1 829 millones
```

**Paso 4 — efecto neto directo.**

```text
ingreso perdido      −25 452
ahorro de costo       +1 829
EFECTO NETO DIRECTO  −23 623  (33 % del resultado del negocio)
```

**Paso 5 — busca los efectos que la cuenta directa no captura.**

```text
EFECTO POSITIVO 1: fondeo transaccional
  el pago inmediato mantiene el saldo en el banco hasta el momento del pago
  mientras que la tarjeta de crédito lo difiere
  estimación: +180 000 de saldo promedio a la vista
  valor: 180 000 × (costo alternativo 6,2 % − costo vista 0,3 %) = 10 620

EFECTO POSITIVO 2: datos de comportamiento
  mayor granularidad de datos de pago → mejor scoring y venta cruzada
  valor estimado: difícil de cuantificar; se registra cualitativamente

EFECTO NEGATIVO 1: pérdida de relación con el comercio
  si el comercio deja de usar el terminal del banco, se pierde el vínculo
  y con él la información de ventas usada para el crédito pyme

EFECTO NEGATIVO 2: fraude
  los pagos inmediatos concentran fraude por ingeniería social
  costo estimado de fraude y de controles: −2 400
```

**Paso 6 — efecto neto ajustado.**

```text
efecto directo        −23 623
fondeo transaccional  +10 620
fraude y controles     −2 400
EFECTO NETO           −15 403  (21 % del resultado del negocio)
```

**Paso 7 — estrategia de respuesta.**

```text
NO se puede impedir la migración: es una infraestructura pública o de industria
la estrategia es CAPTURAR el nuevo medio, no defender el antiguo

1. SER EL MEJOR EN PAGOS INMEDIATOS
   · experiencia superior en la aplicación
   · disponibilidad y velocidad
   · el objetivo es que el cliente use la app del banco, no otra

2. DIFERENCIAR LA TARJETA DE CRÉDITO POR LO QUE EL PAGO INMEDIATO NO OFRECE
   · financiamiento en cuotas
   · protección ante disputa
   · beneficios y programa de puntos
   → la tarjeta de crédito deja de competir en "pagar" y compite en "financiar"

3. MANTENER LA RELACIÓN CON EL COMERCIO
   · ofrecer aceptación de todos los medios en un solo terminal o aplicación
   · abono inmediato de las ventas
   · usar los datos de venta para ofrecer crédito

4. GESTIONAR EL FRAUDE DEL NUEVO MEDIO
   · límites por defecto conservadores
   · verificación del beneficiario
   · retención de operaciones atípicas
   · educación al cliente

5. MONETIZAR EL FONDEO TRANSACCIONAL
   · el saldo a la vista es el activo del negocio de pagos
   · su valor crece cuando las tasas suben
```

**Interpreta:** el negocio de pagos pierde 21 % de su resultado y **la respuesta correcta no es
defender la tarjeta**: es capturar el nuevo medio y reposicionar la tarjeta en el financiamiento, que
es donde el pago inmediato no compite. Intentar frenar la migración con precios habría acelerado la
pérdida de la relación con el cliente.

## 🏦 Del cliente al banco

El cliente elige cómo pagar y el banco gana o pierde según el medio elegido. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| Pago inmediato gratuito | Menor ingreso, menor costo, mismo fondeo | 14, clase 5 |
| Beneficios de la tarjeta de crédito | Financiados por la tasa de intercambio | 3, clase 5 |
| Comercio que prefiere transferencia | Ahorro de comisión de adquirencia | 10, clase 10 |
| Protección ante disputa | Diferenciador de la tarjeta de crédito | 4, clase 6 |
| Fraude en pagos inmediatos | Irrevocabilidad: la prevención es el único control | 4, clase 12 |

## 🧪 Práctica

El laboratorio pide calcular el costo por transacción de varios medios y recomendar por segmento. El medio más barato para el banco y el preferido por el cliente rara vez coinciden.

En `labs/lab-05.md`:

1. Compara ocho medios de pago en las cuatro dimensiones.
2. Descompón la comisión de una transacción con tarjeta entre sus participantes.
3. Estima el efecto de la migración a pagos inmediatos en un negocio de pagos.
4. Diseña la estrategia de medios de pago para dos segmentos distintos.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen estrategias de medios de pago que pierden dinero. Las causas son costos por transacción mal calculados y efectos de red ignorados.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se defiende el medio antiguo con precio | Migración estructural | Captura el nuevo medio. |
| Se ignora el fondeo transaccional | Solo se contó la comisión | El saldo es el activo del negocio. |
| Se compite en pagar con la tarjeta de crédito | Diferenciador equivocado | Compite en financiar y proteger. |
| Se subestima el fraude del pago inmediato | Irrevocabilidad no considerada | La prevención es el único control. |
| Se pierde la relación con el comercio | Foco solo en la comisión | La relación da datos y crédito. |
| Se supone que un medio es superior a otro | Es un intercambio, no jerarquía | Evalúa las cuatro dimensiones. |

## ❓ Preguntas de comprobación

1. ¿Cuáles son las cuatro dimensiones de evaluación de un medio de pago?
2. ¿Cómo se reparte la comisión de adquirencia entre los participantes?
3. ¿Dónde está el negocio de una transferencia gratuita para el banco?
4. ¿En qué debe diferenciarse la tarjeta de crédito frente a los pagos inmediatos?
5. ¿Por qué el fraude en pagos inmediatos exige prevención en lugar de recuperación?

## 📥 Entregable

Guarda en `portfolio/parte-10/clase-09/`:

- la comparación de ocho medios en las cuatro dimensiones;
- la descomposición de la comisión de una transacción real;
- la estimación del efecto de una migración de medios;
- la estrategia diseñada para dos segmentos con su fundamento.

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

- Committee on Payments and Market Infrastructures (2020). *Payment aspects of financial inclusion*. CPMI/Banco Mundial. <https://www.bis.org/cpmi/>
- Evans, D. y Schmalensee, R. (2005). *Paying with Plastic* (2.ª ed.). MIT Press. Economía de las redes de tarjetas.
- Committee on Payments and Market Infrastructures (2016). *Fast payments*. BIS. Diseño y efectos de los pagos inmediatos.
- Bank for International Settlements (2021). *Annual Economic Report*, capítulo sobre el futuro del sistema de pagos.
- Rochet, J. y Tirole, J. (2006). "Two-Sided Markets: A Progress Report". *RAND Journal of Economics*. Economía de los mercados de dos lados.
- Verificación local: revisa las tasas de intercambio reguladas en tu país, si existen, y la infraestructura de pagos inmediatos disponible.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 08 · Conciliación bancaria](08-conciliacion-bancaria.md) | [Parte 10](../README.md) · [Programa](../../../SYLLABUS.md) | [10 · Tarjetas y adquirencia →](10-tarjetas-y-adquirencia.md) |
<!-- gen:footer:end -->
