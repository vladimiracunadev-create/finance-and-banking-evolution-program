<!-- meta
part: 21
class: 6
title: "Mercado secundario y liquidez prometida"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [mercado-secundario, liquidez, transparencia]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [IOSCO, CPMI]
requires_legal_review: false
-->

<!-- gen:header:start -->
# Clase 06 · Mercado secundario y liquidez prometida

> [← 05 · Ciclo de vida del instrumento](05-ciclo-de-vida-del-instrumento.md) · [Índice de la parte](../README.md) · [07 · Fraccionamiento y acceso →](07-fraccionamiento-y-acceso.md)

**Parte 21 — Tokenización, FX on-chain y mercados programables** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Contrastar la liquidez que promete un folleto con la que existe. **La promesa
más repetida de la tokenización es la liquidez de activos ilíquidos**, y es la
que peor resiste una medición.

El instrumento de las clases anteriores se puede transferir. Esta clase comprueba si además se puede vender, y separa tres cosas que se prometen juntas y no vienen juntas.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** transferibilidad de negociabilidad y de liquidez.
2. **Medir** la liquidez efectiva de un mercado secundario tokenizado.
3. **Explicar** por qué fraccionar no crea liquidez por sí mismo.
4. **Calcular** el coste de una salida en un mercado con pocos participantes.
5. **Evaluar** los compromisos de un proveedor de liquidez y sus condiciones de
   retirada.

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

Los tres primeros términos separan tres cosas que se prometen juntas; los cinco siguientes, los mecanismos de liquidez y su fragilidad. La distinción entre **transferibilidad, negociabilidad y liquidez** es la que ordena la clase: que un token se pueda transferir no significa que haya con quién negociarlo.

| Concepto | Comprensión verificable |
|---|---|
| `transferibilidad` | Que el instrumento pueda cambiar de titular |
| `negociabilidad` | Que exista un lugar donde se cruce oferta y demanda |
| `liquidez` | Que se pueda salir en un plazo a un precio previsible |
| `proveedor de liquidez` | Quien se compromete a cotizar de compra y venta |
| `compromiso de cotización` | Obligación de dar precio con un diferencial máximo |
| `cláusula de retirada` | Condiciones que liberan al proveedor |
| `frecuencia de cruce` | Cada cuánto se casan órdenes |
| `mercado por subasta` | Cruce periódico en vez de continuo |

## 🧠 Modelo mental

El modelo mental es una escalera de tres peldaños que se presentan como uno. Tokenizar da el primero casi gratis, el segundo exige un mercado y el tercero exige que alguien se comprometa a cotizar, y ese compromiso tiene cláusulas de retirada.

```text
TRES COSAS DISTINTAS QUE SE PRESENTAN
COMO UNA

  TRANSFERIBILIDAD
    puedo cambiar de titular
    → la da el registro

  NEGOCIABILIDAD
    hay un sitio donde encontrar contraparte
    → la da una plataforma, y exige régimen

  LIQUIDEZ
    puedo salir mañana a un precio previsible
    → la dan PARTICIPANTES DISPUESTOS A COMPRAR

  Y ESO ÚLTIMO NO LO DA NINGUNA TECNOLOGÍA.

UN ACTIVO ILÍQUIDO TOKENIZADO
ES UN ACTIVO ILÍQUIDO CON MEJOR
INFRAESTRUCTURA DE TRANSFERENCIA.
```

## 📖 Desarrollo

### 1. Por qué fraccionar no crea liquidez

```text
ARGUMENTO HABITUAL
  «al fraccionar, más gente puede comprar,
   luego habrá más demanda»

QUÉ FALTA EN ESE RAZONAMIENTO
  · más compradores potenciales no es
    más demanda: es más gente que PODRÍA
  · la demanda depende de que el activo
    interese a ese precio
  · y un activo ilíquido suele serlo porque
    es difícil de valorar, no porque el
    importe mínimo sea alto

CUÁNDO SÍ AYUDA FRACCIONAR
  · cuando la barrera era efectivamente
    el importe y hay demanda demostrada
    por debajo de él
  · cuando existe un precio de referencia
    creíble e independiente

CUÁNDO NO
  · cuando el activo no tiene valoración
    frecuente e independiente
  → y entonces el fraccionamiento solo
    reparte la iliquidez entre más gente
```

### 2. Medir en vez de suponer

```text
LO QUE HAY QUE MEDIR, CON LA PARTE 20,
CLASE 13

  · número de operaciones al mes
  · número de contrapartes distintas
  · profundidad al 1 % del precio
  · tiempo medio hasta encontrar contraparte
  · diferencial medio entre compra y venta
  · mayor operación ejecutada

Y UNA MÁS, PROPIA DE ESTE MERCADO
  · porcentaje de las operaciones en que
    interviene el propio promotor o una
    parte vinculada

  si es alto, la liquidez observada no es
  del mercado: es del promotor sosteniéndolo,
  y se acabará cuando él decida
```

### 3. El proveedor de liquidez y su letra pequeña

```text
UN COMPROMISO DE COTIZACIÓN TIENE
CUATRO PARÁMETROS Y UNA TRAMPA

  · diferencial máximo
  · importe mínimo cotizado
  · horario
  · plazo del compromiso

  Y LA TRAMPA: las condiciones de retirada

CLÁUSULAS HABITUALES DE RETIRADA
  «circunstancias excepcionales de mercado»
  «volatilidad superior a X»
  «imposibilidad de cubrir la posición»
  «a discreción, con preaviso de N días»

CUÁNDO SE ACTIVAN
  exactamente cuando hace falta la liquidez

REGLA DE ANÁLISIS
  la liquidez comprometida vale lo que valen
  sus cláusulas de retirada, y hay que
  leerlas antes de contar con ella
```

### 4. Subasta frente a mercado continuo

```text
MERCADO CONTINUO
  se cruza en cualquier momento
  · exige presencia constante de contrapartes
  · con pocos participantes, el libro está
    vacío la mayor parte del tiempo
  · y un libro vacío da precios erráticos

SUBASTA PERIÓDICA
  se acumulan órdenes y se cruzan a una hora
  · concentra la liquidez en un momento
  · da un precio único y más robusto
  · reduce la sensación de inmediatez

PARA UN MERCADO PEQUEÑO,
LA SUBASTA ES CASI SIEMPRE MEJOR,
y sin embargo casi todas las plataformas
eligen el continuo porque parece más moderno.
```

### 5. La transparencia que sí sirve

```text
QUÉ DEBE PUBLICAR UNA PLATAFORMA
PARA QUE UN INVERSIONISTA DECIDA

  · operaciones ejecutadas, con importe y hora
  · libro agregado por niveles
  · número de contrapartes distintas del mes
  · operaciones en que interviene una parte
    vinculada
  · periodos sin ninguna operación
  · mayor operación ejecutada y su impacto

EL PENÚLTIMO ES EL MÁS INFORMATIVO
Y EL QUE NUNCA SE PUBLICA:
«este instrumento no tuvo ninguna operación
durante 23 de los últimos 30 días» dice más
que cualquier cifra de volumen.
```

## 🧮 Ejemplo guiado

El ejemplo evalúa un compromiso de cotización y sus cláusulas de retirada. Conviene leer las cláusulas: el compromiso desaparece justo cuando haría falta.

**Situación.** Una plataforma promete «liquidez diaria» para participaciones
inmobiliarias tokenizadas. Hay que comprobarlo con seis meses de datos.

```text
DATOS DE SEIS MESES
  operaciones totales                      412
  días con al menos una operación           74 de 182
  contrapartes distintas                    96
  volumen total                     18 400 000
  operación media                       44 660
  mayor operación                      620 000
  operaciones con parte vinculada          148
  volumen de esas operaciones        9 900 000
  diferencial medio publicado             1,8 %
  emisión total                    120 000 000
```

**Paso 1 — mide la frecuencia real.**

```text
DÍAS CON OPERACIÓN
  74 / 182 = 40,7 %

  → EN EL 59,3 % DE LOS DÍAS
    NO SE PUDO OPERAR

  «liquidez diaria» describe la posibilidad
  de enviar una orden, no la de ejecutarla
```

**Paso 2 — separa la actividad del promotor.**

```text
OPERACIONES CON PARTE VINCULADA
  148 / 412 = 35,9 % de las operaciones
  9 900 000 / 18 400 000 = 53,8 % del volumen

  VOLUMEN DE MERCADO GENUINO
  18 400 000 − 9 900 000 = 8 500 000
  en seis meses

  → 1 416 667 al mes
  → sobre una emisión de 120 000 000
    es el 1,18 % mensual
```

**Paso 3 — calcula la rotación.**

```text
ROTACIÓN ANUAL GENUINA
  1,18 % × 12 = 14,2 % del capital al año

COMPARACIÓN
  un fondo cotizado líquido rota
  varias veces su capital al año
  un inmueble directo rota una vez
  cada muchos años

  14,2 % ESTÁ MÁS CERCA DEL INMUEBLE
  QUE DEL FONDO COTIZADO
```

**Paso 4 — mide el tiempo de salida.**

```text
UN TENEDOR QUIERE VENDER 400 000

  volumen genuino mensual   1 416 667
  contrapartes distintas al mes ≈ 16

  SI ABSORBE EL 10 % DEL VOLUMEN MENSUAL
  sin mover el precio:
  141 667 al mes
  → 400 000 / 141 667 = 2,8 meses

  SI QUIERE SALIR EN UNA SEMANA
  tendría que absorber 400 000 de un volumen
  semanal de 354 167
  → el 113 % del volumen normal
  → impacto de precio muy alto
```

**Paso 5 — estima el impacto de la salida rápida.**

```text
SUPUESTO DECLARADO
  el impacto crece un 1 % por cada 25 % del
  volumen mensual que se vende de golpe

  vender 400 000 = 28,2 % del volumen mensual
  impacto ≈ 1,13 %

  vender 620 000 (la mayor operación
  registrada) = 43,8 %
  impacto ≈ 1,75 %

  Y ESTOS SUPUESTOS SON OPTIMISTAS:
  se basan en un mercado donde el 53,8 %
  del volumen lo pone el promotor
```

**Paso 6 — evalúa el compromiso de liquidez.**

```text
EL FOLLETO DICE QUE EL PROMOTOR
«PROCURARÁ DAR CONTRAPARTIDA»

  · «procurará» no es una obligación
  · no hay diferencial máximo
  · no hay importe mínimo
  · no hay plazo
  · no hay condiciones de retirada porque
    no hay compromiso del que retirarse

  → EL 53,8 % DEL VOLUMEN DEPENDE
    DE UNA INTENCIÓN

QUÉ EXIGIRÍA UN COMPROMISO REAL
  · diferencial máximo del 2 %
  · importe mínimo cotizado de 50 000
    por lado
  · horario de subasta declarado
  · plazo de 24 meses
  · retirada solo por causas tasadas
    y con preaviso de 30 días
```

**Paso 7 — propón el cambio de estructura.**

```text
DE MERCADO CONTINUO A SUBASTA SEMANAL

  con 412 operaciones en 182 días,
  el continuo tiene el libro vacío
  la mayor parte del tiempo

  CON SUBASTA SEMANAL
    26 subastas en seis meses
    412 / 26 = 15,8 operaciones por subasta
    → un libro con contenido

  EFECTOS
    · precio único y más robusto
    · menor diferencial efectivo
    · menos sensación de inmediatez,
      y esa sensación era falsa igualmente

Y LA COMUNICACIÓN CAMBIA
  de «liquidez diaria» a «ventana semanal
  de negociación», que es lo que hay.
```

**Interpreta:** la plataforma no mentía al decir que se podía enviar una orden
cualquier día. **La palabra «liquidez» hacía todo el trabajo**: el 59 % de los
días no había ejecución, el 54 % del volumen lo ponía el promotor sin
obligación, y salir de 400 000 llevaba casi tres meses.

## 🧭 Perspectivas

La liquidez prometida afecta a cada participante de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | «Liquidez diaria» | Si cuenta con poder salir |
| Inversionista | Un volumen agregado | Qué tamaño toma |
| Emisor | Un mercado que sostener | Si asume un compromiso |
| Promotor | El 54 % del volumen | Cuándo deja de ponerlo |
| Plataforma | Continuo frente a subasta | Qué estructura elige |
| Custodio | Transferencias | — |
| Mercado | Pocos participantes | Si entra |
| Supervisor | Una promesa sin respaldo | Qué exige en el folleto |
| Auditor | Operaciones vinculadas | Qué revela |
| Sociedad | Acceso a activos ilíquidos | Qué información exige |

## 🏦 Del cliente al banco

El cliente cree que puede vender cuando quiera y depende de un proveedor con cláusulas. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Tiene liquidez diaria» | 59 % de los días sin ninguna operación | 21, clase 6 |
| «Hay volumen» | El 54 % lo pone el promotor | 21, clase 6 |
| «Salgo cuando quiera» | 400 000 tardan 2,8 meses | 21, clase 6 |

## ⚖️ Riesgos y controles

Los riesgos son de liquidez prometida y no entregada. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Confundir transferibilidad con liquidez | El folleto usa una palabra por otra | Medir días con operación |
| Volumen sostenido por el promotor | Se retira y desaparece | Publicar operaciones vinculadas |
| Compromiso sin obligación | «Procurará dar contrapartida» | Exigir parámetros y causas de retirada |
| Mercado continuo con libro vacío | Precios erráticos | Subasta periódica |
| Fraccionar esperando liquidez | Reparte la iliquidez | Demostrar demanda al precio |
| Sin publicar los días sin operación | Es el dato más informativo | Publicarlo por instrumento |

## 🧪 Práctica

El laboratorio pide evaluar compromisos de cotización y sus cláusulas. La liquidez efectiva en tensión es lo que se mide.

En [`labs/lab-05.md`](../labs/lab-05.md):

1. Mide días con operación, contrapartes distintas y rotación genuina.
2. Separa el volumen de partes vinculadas y recalcula.
3. Estima el tiempo de salida de una posición dada.
4. Compara mercado continuo y subasta con los mismos datos.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen mercados secundarios sin contrapartida. La causa es haber confundido transferibilidad con liquidez.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Leer «liquidez» en el folleto | Es la palabra que vende | Mide días con ejecución |
| Volumen agregado sin desglose | Es lo publicado | Separa partes vinculadas |
| Fraccionar por defecto | Parece dar acceso | Demuestra demanda al precio |
| Elegir mercado continuo | Parece moderno | Con pocos participantes, subasta |
| Contar con el promotor | Ha estado ahí seis meses | Sin compromiso, puede irse |
| No medir el tiempo de salida | Nadie lo pide | Es lo que decide para una tesorería |

## ❓ Preguntas de comprobación

1. ¿Qué diferencia hay entre transferibilidad, negociabilidad y liquidez?
2. ¿Por qué fraccionar no crea liquidez por sí mismo?
3. ¿Qué dato es el más informativo y nunca se publica?
4. ¿Qué cuatro parámetros y qué trampa tiene un compromiso de cotización?
5. ¿Cuándo conviene una subasta periódica frente a un mercado continuo?

## 📥 Entregable

Guarda en `portfolio/parte-21/clase-06/`:

- la medición de liquidez con los siete indicadores;
- la separación del volumen de partes vinculadas;
- el cálculo del tiempo y del coste de salida de una posición;
- el compromiso de cotización que exigirías, con sus cinco elementos.

## 🔗 Referencias cruzadas

- **Viene de:** clase 4; Parte 20, clase 13.
- **Continúa en:** clases 7 y 13 de esta parte.
- **Se aplica en:** Parte 22, clase 10; Parte 23, clase 11.

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

- IOSCO (2023). *Policy Recommendations for Crypto and Digital Asset Markets*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- IOSCO (2011). *Principles for Dark Liquidity*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD353.pdf>
- Committee on Payments and Market Infrastructures (2024). *Tokenisation in the context of money and other assets*. BIS. <https://www.bis.org/cpmi/publ/d225.htm>
- Bank for International Settlements (2023). *Annual Economic Report*, capítulo III. BIS. <https://www.bis.org/publ/arpdf/ar2023e3.htm>
- Verificación local: comprueba qué información periódica sobre negociación debe publicar una plataforma en tu jurisdicción y si el régimen exige declarar las operaciones con partes vinculadas. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 05 · Ciclo de vida del instrumento](05-ciclo-de-vida-del-instrumento.md) | [Parte 21](../README.md) · [Programa](../../../SYLLABUS.md) | [07 · Fraccionamiento y acceso →](07-fraccionamiento-y-acceso.md) |
<!-- gen:footer:end -->
