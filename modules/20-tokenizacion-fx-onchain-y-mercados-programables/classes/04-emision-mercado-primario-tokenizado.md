---
part: 21
class: 4
title: "Emisión: mercado primario tokenizado"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [chile, internacional]
regulatory_topics: [oferta-publica, mercado-primario, proteccion-al-inversionista]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [IOSCO, CMF]
requires_legal_review: true
---

<!-- gen:header:start -->
# Clase 04 · Emisión: mercado primario tokenizado

> [← 03 · Derechos económicos y políticos del tenedor](03-derechos-economicos-y-politicos-del-tenedor.md) · [Índice de la parte](../README.md) · [05 · Ciclo de vida del instrumento →](05-ciclo-de-vida-del-instrumento.md)

**Parte 21 — Tokenización, FX on-chain y mercados programables** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Recorrer una emisión completa, desde la decisión de emitir hasta la anotación en
el registro. **La norma de oferta pública aplica igual**, y lo que cambia es la
mecánica de suscripción, adjudicación y liquidación.

## 📚 Objetivos

Al finalizar podrás:

1. **Describir** las nueve etapas de una emisión y qué cambia en cada una.
2. **Diseñar** un mecanismo de adjudicación con sus reglas de prorrateo.
3. **Calcular** el resultado de una colocación con sobredemanda.
4. **Identificar** qué obligaciones de información no cambian por tokenizar.
5. **Evaluar** el riesgo de que la colocación quede desierta.

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

Los cuatro primeros términos son la colocación y su mecánica; los cuatro siguientes, sus plazos y sus resultados posibles. La **colocación desierta** es el escenario que casi ningún diseño contempla y que hay que resolver antes: qué pasa con las suscripciones si no se alcanza el mínimo.

| Concepto | Comprensión verificable |
|---|---|
| `oferta pública` | Ofrecimiento dirigido al público, sujeto a régimen |
| `colocación privada` | Dirigida a inversionistas determinados |
| `libro de órdenes` | Registro de la demanda durante el periodo |
| `adjudicación` | Reparto del papel entre los demandantes |
| `prorrateo` | Reparto proporcional ante sobredemanda |
| `período de suscripción` | Plazo en que se recogen órdenes |
| `liquidación de la emisión` | Entrega del valor contra el pago |
| `colocación desierta` | Demanda insuficiente para emitir |

## 🧠 Modelo mental

El modelo mental es que el mercado primario tokenizado no cambia el proceso de colocación: cambia su liquidación, que puede ser atómica. Todo lo demás —libro, adjudicación, prorrateo— sigue siendo lo mismo con otra anotación.

```text
LAS NUEVE ETAPAS, Y QUÉ CAMBIA EN CADA UNA

  1 DECISIÓN DE EMITIR         nada
  2 ESTRUCTURACIÓN             nada
  3 DOCUMENTACIÓN Y FOLLETO    nada
  4 AUTORIZACIÓN               nada, y hay que
                               explicar la mecánica
  5 DIFUSIÓN                   canal, no contenido
  6 SUSCRIPCIÓN                sí: orden y pago
                               pueden ser el mismo acto
  7 ADJUDICACIÓN               sí: puede ser
                               automática y verificable
  8 LIQUIDACIÓN                sí: puede ser atómica
                               si el dinero está dentro
  9 ANOTACIÓN                  sí: es el registro

DE NUEVE ETAPAS, CUATRO CAMBIAN.
Las cinco primeras —las que protegen
al inversionista— son idénticas.
```

## 📖 Desarrollo

### 1. Lo que no cambia

```text
OBLIGACIONES QUE SIGUEN IGUAL

  · calificación del instrumento y régimen
  · folleto o documento equivalente,
    con su contenido mínimo
  · responsabilidad por la información
  · deber de no publicidad engañosa
  · idoneidad del inversionista, si aplica
  · información periódica y hechos esenciales
  · prevención de lavado sobre los suscriptores

EL ERROR MÁS CARO DE ESTA ETAPA
  suponer que emitir en un registro
  distribuido convierte la oferta en algo
  distinto de una oferta pública.
  No lo hace: lo que decide es a quién
  se dirige y cómo se difunde.
```

### 2. Suscripción y pago como un solo acto

```text
EN UNA EMISIÓN TRADICIONAL
  se ordena, se adjudica, se paga, se anota
  → entre el pago y la anotación hay
    un intervalo con riesgo

CON EL DINERO EN EL MISMO REGISTRO
  el suscriptor bloquea el importe al ordenar
  · si le adjudican, se libera contra el valor
  · si no, se le devuelve automáticamente

QUÉ SE GANA
  · no hay riesgo de impago del suscriptor
  · la devolución del no adjudicado es
    inmediata, y en una emisión con
    sobredemanda eso es mucho dinero
    inmovilizado menos días

QUÉ SE EXIGE
  · que el dinero esté en el mismo registro
    (Parte 20, clase 8)
  · si no lo está, este beneficio no existe
```

### 3. Adjudicación

| Mecanismo | Cómo reparte | Cuándo conviene |
|---|---|---|
| Prorrateo simple | Misma fracción a todos | Demanda homogénea |
| Prorrateo con mínimo | Tramo mínimo íntegro y resto a prorrata | Muchos minoristas |
| Por orden de llegada | Turno hasta agotar | Nunca: crea la carrera |
| Subasta de precio único | Todos al precio de corte | Demanda con precio |
| Por tramos | Cuota fija por tipo de inversionista | Objetivo de base accionaria |

```text
LA REGLA DE LA PARTE 20, CLASE 5, APLICA IGUAL
  el orden de llegada premia al primero
  y produce una carrera, aquí por el papel
  → y en una emisión la carrera se traduce
    en sobredemanda artificial, porque
    todo el mundo pide de más para que
    el prorrateo le deje lo que quería
```

### 4. La sobredemanda artificial

```text
SI EL INVERSIONISTA SABE QUE HABRÁ PRORRATEO,
PIDE MÁS DE LO QUE QUIERE

  quiere 100 000
  espera un prorrateo del 40 %
  → pide 250 000

  y si todos hacen lo mismo, el prorrateo
  baja, y entonces piden aún más

CONSECUENCIA
  el libro de órdenes deja de informar
  sobre la demanda real
  → el emisor no sabe a qué precio colocar
  → y la sobredemanda publicada es ficción

CORRECCIONES
  · exigir bloqueo del importe al ordenar
    (pedir de más cuesta dinero inmovilizado)
  · tramo mínimo íntegro, que reduce la
    incertidumbre del pequeño
  · límite máximo por inversionista
  · subasta de precio, donde exagerar
    la cantidad no mejora la posición
```

### 5. La colocación desierta

```text
UN RIESGO QUE LAS PLATAFORMAS MINIMIZAN

  · sin colocador que asegure, no hay
    compromiso de suscripción
  · el emisor puede quedarse sin financiación
    después de haber gastado en la emisión

QUÉ MIRAR
  · ¿hay aseguramiento, y de quién?
  · ¿hay importe mínimo por debajo del cual
    la emisión se cancela?
  · ¿qué pasa con lo ya suscrito si se cancela?
  · ¿quién paga los costes incurridos?

DISEÑO CORRECTO
  · importe mínimo declarado en el folleto
  · devolución automática e inmediata si no
    se alcanza, con el bloqueo liberado
  · y decirlo antes, no en la letra pequeña
```

## 🧮 Ejemplo guiado

El ejemplo ejecuta una colocación con prorrateo y liquidación atómica. Conviene comprobar el caso de sobresuscripción: el prorrateo es donde aparecen los errores.

**Situación.** Una emisión de 30 000 000 con importe mínimo de 18 000 000. Hay
que resolver la adjudicación y medir el efecto de la sobredemanda artificial.

```text
DATOS
  objetivo                        30 000 000
  mínimo para no quedar desierta  18 000 000
  precio                          fijo, 1 000 por unidad
  unidades ofrecidas                  30 000
  período de suscripción              10 días
  demanda registrada             112 400 000
  órdenes                              6 800
  orden media                         16 529
  límite por inversionista        no declarado
```

**Paso 1 — calcula el prorrateo simple.**

```text
FRACCIÓN
  30 000 000 / 112 400 000 = 26,69 %

  una orden de 16 529 recibe 4 412
  una orden de 500 000 recibe 133 452

RATIO DE SOBREDEMANDA: 3,75 veces
```

**Paso 2 — estima cuánta demanda es artificial.**

```text
SUPUESTO DECLARADO
  los inversionistas anticiparon un prorrateo
  del 35 % y multiplicaron su intención
  por 1 / 0,35 = 2,86

DEMANDA REAL ESTIMADA
  112 400 000 / 2,86 = 39 300 000

  → la demanda genuina cubre el objetivo
    con un margen del 31 %,
    no con un 275 % como sugiere el libro
```

**Paso 3 — mide el error que induce.**

```text
CON UNA SOBREDEMANDA APARENTE DE 3,75 VECES
  el emisor podría concluir que colocó barato
  y que en la próxima emisión puede
  pagar menos cupón

CON LA DEMANDA REAL DE 1,31 VECES
  el margen es normal y no hay señal
  de haber dejado dinero sobre la mesa

DECIDIR SOBRE EL LIBRO SIN CORREGIRLO
LLEVARÍA A ENCARECER LA SIGUIENTE EMISIÓN
HASTA DEJARLA DESIERTA.
```

**Paso 4 — aplica prorrateo con tramo mínimo.**

```text
TRAMO MÍNIMO ÍNTEGRO: 2 000 POR ORDEN

  reservado = 6 800 × 2 000 = 13 600 000
  disponible para el resto = 16 400 000

  resto solicitado = 112 400 000 − 13 600 000
                   = 98 800 000
  fracción del resto = 16,60 %

  ORDEN DE 16 529
    2 000 + (14 529 × 16,60 %) = 4 412
    → recibe lo mismo, pero con más certeza

  ORDEN DE 500 000
    2 000 + (498 000 × 16,60 %) = 84 668
    → recibe un 37 % menos que con prorrateo simple

EL TRAMO MÍNIMO REDISTRIBUYE
HACIA EL PEQUEÑO, COMO SE PRETENDÍA.
```

**Paso 5 — introduce el bloqueo del importe.**

```text
CON BLOQUEO OBLIGATORIO AL ORDENAR

  pedir 500 000 exige inmovilizar 500 000
  durante 10 días

  COSTE PARA EL INVERSIONISTA
  al 4,2 % anual: 500 000 × 4,2 % × 10/360
                = 583

  para recibir 84 668 adjudicados,
  pagó 583 de coste de oportunidad
  → 0,69 % del adjudicado

EFECTO SOBRE LA DEMANDA
  supuesto: la exageración baja de 2,86× a 1,4×
  demanda registrada = 39 300 000 × 1,4
                     = 55 020 000
  ratio = 1,83 veces

  EL LIBRO EMPIEZA A INFORMAR.
```

**Paso 6 — calcula el ahorro por devolución inmediata.**

```text
SIN BLOQUEO EN EL MISMO REGISTRO
  el no adjudicado se devuelve por
  transferencia, con 3 días de retraso medio

  importe no adjudicado con la demanda
  corregida: 55 020 000 − 30 000 000
           = 25 020 000

  25 020 000 × 4,2 % × 3/360 = 8 757
  de coste de oportunidad para el conjunto
  de los inversionistas

CON LIBERACIÓN AUTOMÁTICA
  0 días → 0

  ES POCO DINERO, Y ES EL BENEFICIO REAL:
  conviene declararlo por lo que es y no
  presentarlo como una transformación.
```

**Paso 7 — resuelve el escenario de emisión desierta.**

```text
SI LA DEMANDA REAL HUBIERA SIDO 15 000 000
  por debajo del mínimo de 18 000 000

  PROCEDIMIENTO
  1 la emisión se declara desierta al cierre
    del período, de forma automática
  2 todos los bloqueos se liberan en el mismo
    acto, sin instrucción de nadie
  3 no se anota ninguna unidad
  4 los costes incurridos los asume el emisor,
    según lo declarado en el folleto

LO QUE NO DEBE OCURRIR
  · reducir el mínimo sobre la marcha
  · emitir por lo suscrito sin decirlo antes
  · retener los importes «por si acaso»

Y ESTO SE PRUEBA ANTES DE LA EMISIÓN,
con una ejecución en entorno de pruebas.
```

**Interpreta:** la sobredemanda de 3,75 veces era en su mayor parte artificial y
habría inducido al emisor a encarecer su siguiente emisión. **El bloqueo del
importe no es un requisito operativo: es lo que hace que el libro de órdenes
informe**, porque convierte exagerar en algo que cuesta dinero.

## 🧭 Perspectivas

La emisión tokenizada afecta a cada participante de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Una emisión accesible | Cuánto pide |
| Inversionista | Un prorrateo esperado | Si exagera la orden |
| Emisor | Un libro con 3,75 veces | Qué concluye para la próxima |
| Colocador | Su papel reducido | Qué servicio aporta |
| Plataforma | Miles de órdenes | Cómo adjudica |
| Custodio | Anotación inicial | Cómo la refleja |
| Infraestructura | Liquidación de la emisión | Si es atómica |
| Supervisor | Una oferta pública | Qué información exige |
| Auditor | Adjudicación verificable | Qué comprueba |
| Sociedad | Acceso a emisiones | Qué protección espera |

## 🏦 Del cliente al banco

El inversionista suscribe y el emisor coloca con un proceso conocido y otra liquidación. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Hubo 3,75 veces de demanda» | La mayor parte es artificial | 21, clase 4 |
| «Pedí de más para que me dieran» | Y por eso el libro no informa | 21, clase 4 |
| «Es una emisión sin folleto» | La norma de oferta pública aplica igual | 21, clase 4 |

## ⚖️ Riesgos y controles

Los riesgos son de colocación y de liquidación de la emisión. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Sobredemanda artificial | El libro deja de informar | Bloqueo del importe al ordenar |
| Orden de llegada | Crea la carrera por el papel | Prorrateo con tramo mínimo |
| Emisión desierta sin procedimiento | Los fondos quedan retenidos | Mínimo declarado y liberación automática |
| Suponer que no hay oferta pública | Se emite sin autorización | Calificar antes de difundir |
| Sin límite por inversionista | Un solo demandante distorsiona | Límite declarado en el folleto |
| Beneficio exagerado | Se promete transformación | Cuantificar el ahorro real |

## 🧪 Práctica

El laboratorio pide ejecutar una colocación completa con prorrateo. El caso de colocación desierta es el que hay que resolver.

En [`labs/lab-02.md`](../labs/lab-02.md):

1. Resuelve una adjudicación con prorrateo simple y con tramo mínimo.
2. Estima la parte artificial de la sobredemanda.
3. Mide el efecto del bloqueo del importe sobre el libro.
4. Ejecuta el escenario de emisión desierta con liberación automática.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen emisiones con problemas. Las causas son prorrateos mal calculados y escenarios de fracaso no previstos.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Leer el libro literalmente | Es el dato disponible | Corrige la parte artificial |
| Adjudicar por orden de llegada | Parece justo | Crea la carrera |
| Sin bloqueo de importe | Molesta al inversionista | Es lo que hace informar al libro |
| Mínimo no declarado | Se decide sobre la marcha | Va en el folleto |
| Prometer «sin intermediarios» | Suena moderno | La mayoría existe por norma |
| No probar el escenario desierto | Se asume que colocará | Se ejecuta en pruebas antes |

## ❓ Preguntas de comprobación

1. De las nueve etapas, ¿cuáles cambian y cuáles no?
2. ¿Por qué el bloqueo del importe hace que el libro de órdenes informe?
3. ¿Cómo se estima la parte artificial de una sobredemanda?
4. ¿Qué redistribuye el tramo mínimo íntegro y hacia quién?
5. ¿Qué cuatro cosas hay que mirar ante el riesgo de emisión desierta?

## 📥 Entregable

Guarda en `portfolio/parte-21/clase-04/`:

- la adjudicación resuelta con los dos mecanismos;
- la estimación de la demanda real con su supuesto declarado;
- el cálculo del coste del bloqueo y su efecto sobre la demanda;
- el procedimiento de emisión desierta, probado.

## 🔗 Referencias cruzadas

- **Viene de:** clases 1 y 3; Parte 20, clase 5.
- **Continúa en:** clases 5, 6 y 8 de esta parte.
- **Se aplica en:** Parte 22, clase 11; Parte 23, clases 7 y 8.

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

- IOSCO (2009). *Objectives and Principles of Securities Regulation*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD323.pdf>
- IOSCO (2023). *Policy Recommendations for Crypto and Digital Asset Markets*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- Committee on Payments and Market Infrastructures (2024). *Tokenisation in the context of money and other assets*. BIS. <https://www.bis.org/cpmi/publ/d225.htm>
- Comisión para el Mercado Financiero. *Normativa sobre oferta pública de valores e inscripción en el Registro de Valores*. CMF. <https://www.cmfchile.cl/portal/principal/613/w3-channel.html>
- Verificación local: comprueba qué constituye oferta pública en tu jurisdicción, qué exenciones existen y qué información mínima exige el folleto para este tipo de instrumento. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 03 · Derechos económicos y políticos del tenedor](03-derechos-economicos-y-politicos-del-tenedor.md) | [Parte 21](../README.md) · [Programa](../../../SYLLABUS.md) | [05 · Ciclo de vida del instrumento →](05-ciclo-de-vida-del-instrumento.md) |
<!-- gen:footer:end -->
