<!-- meta
part: 20
class: 3
title: "Stablecoins: tipologías y mecánica de la paridad"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional, union-europea]
regulatory_topics: [stablecoins, activos-referenciados, paridad]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [FSB, CPMI, IOSCO]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 03 · Stablecoins: tipologías y mecánica de la paridad

> [← 02 · Criptoactivos no respaldados](02-criptoactivos-no-respaldados.md) · [Índice de la parte](../README.md) · [04 · Reservas: composición, calidad y verificación →](04-reservas-composicion-calidad-y-verificacion.md)

**Parte 20 — Activos digitales, stablecoins y dinero programable** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Entender **qué sostiene realmente una paridad**. La estabilidad de una stablecoin
no la produce el nombre ni el respaldo declarado: la produce un mecanismo de
arbitraje que solo funciona si alguien puede redimir de verdad.

El activo de la clase anterior no tiene ancla. Esta trata los que sí la tienen, o dicen tenerla, y separa dos cosas que se confunden: el derecho a redimir a la par y el precio al que se negocia.

## 📚 Objetivos

Al finalizar podrás:

1. **Clasificar** una stablecoin por su mecanismo de estabilización, no por su
   etiqueta.
2. **Explicar** cómo el arbitraje de redención mantiene el precio de mercado.
3. **Identificar** las condiciones que rompen ese arbitraje.
4. **Calcular** la banda de precio que el arbitraje puede sostener dados sus
   costes.
5. **Distinguir** paridad de derecho y paridad de mercado.

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

Los cuatro primeros términos son los dos tipos de paridad y su arbitraje; los cuatro siguientes, los mecanismos que la sostienen. La distinción entre **paridad de derecho y de mercado** es la que ordena la clase: una es un derecho a redimir y la otra es el precio al que se negocia, y solo la primera obliga a alguien.

| Concepto | Comprensión verificable |
|---|---|
| `paridad` | Relación de valor declarada frente a una referencia |
| `paridad de derecho` | El emisor se obliga a redimir a ese valor |
| `paridad de mercado` | El precio al que se intercambia entre terceros |
| `arbitraje de redención` | Comprar barato y redimir a la par, o al revés |
| `participante autorizado` | Quien puede emitir y redimir contra el emisor |
| `banda de no arbitraje` | Rango de precio donde arbitrar no compensa |
| `sobrecolateralización` | Respaldo superior al valor emitido |
| `mecanismo endógeno` | Estabilización basada en el propio sistema |

## 🧠 Modelo mental

El modelo mental es un arbitraje que mantiene el precio: mientras se pueda redimir a la par, cualquier desviación de mercado se corrige comprando barato y redimiendo. La paridad se sostiene sobre esa posibilidad, y desaparece en cuanto la redención se cierra.

```text
POR QUÉ EL PRECIO DE MERCADO SE PEGA A LA PARIDAD

  SI EL PRECIO CAE A 0,99
    alguien compra en mercado a 0,99
    y redime contra el emisor a 1,00
    → gana 0,01, y su compra empuja el precio arriba

  SI EL PRECIO SUBE A 1,01
    alguien entrega 1,00 al emisor,
    recibe una unidad y la vende a 1,01
    → gana 0,01, y su venta empuja el precio abajo

EL PRECIO NO SE MANTIENE POR EL RESPALDO.
SE MANTIENE PORQUE ALGUIEN GANA DINERO
CORRIGIÉNDOLO.

  → SI ESE ALGUIEN NO PUEDE REDIMIR,
    EL MECANISMO DESAPARECE
    Y EL RESPALDO SE VUELVE IRRELEVANTE
    PARA EL PRECIO
```

## 📖 Desarrollo

### 1. Tipologías por mecanismo

| Tipo | Respaldo | Qué sostiene la paridad | Modo de fallo principal |
|---|---|---|---|
| Respaldo fiduciario | Efectivo y deuda pública a corto | Redención contra el emisor | Reservas ilíquidas o insuficientes |
| Respaldo en activos diversos | Cesta de activos | Redención por valor de cesta | Valoración y liquidez de la cesta |
| Respaldo en criptoactivos | Criptoactivos sobrecolateralizados | Liquidación automática de garantías | Caída brusca y liquidaciones en cascada |
| Endógena o algorítmica | Otro token del sistema | Incentivos de arbitraje internos | Espiral reflexiva (clase 7) |
| Híbrida | Combinación | Depende del tramo | El tramo más débil |

### 2. La banda de no arbitraje

El arbitraje que sostiene la paridad no es gratuito, y mientras el desvío no
cubra sus costes nadie lo ejecuta. El bloque los enumera y saca la conclusión
que reordena todo el análisis: la paridad es una banda, no un punto.

```text
ARBITRAR TIENE COSTES

  · comisión de redención del emisor
  · mínimo de redención
  · tiempo hasta recibir los fondos
  · coste de la operación en el registro
  · riesgo de que el precio se mueva mientras tanto

SI EL DESVÍO ES MENOR QUE LA SUMA DE ESOS COSTES,
NADIE ARBITRA Y EL PRECIO SE QUEDA DONDE ESTÁ

  → LA PARIDAD NO ES UN PUNTO: ES UNA BANDA
    y su anchura la fija el diseño del emisor
```

### 3. Quién puede arbitrar

De poco sirve una banda estrecha si solo unos pocos pueden operar dentro de
ella. El bloque describe la restricción habitual de acceso a la redención y
sus consecuencias para todos los demás tenedores.

```text
LA PIEZA MÁS IGNORADA DEL DISEÑO

  MUCHOS EMISORES SOLO REDIMEN A
  «PARTICIPANTES AUTORIZADOS»
    · verificación reforzada
    · importe mínimo elevado
    · contrato bilateral

  PARA EL RESTO DEL MERCADO
    la paridad NO ES UN DERECHO:
    es el resultado de que esos pocos arbitren

  CONSECUENCIAS
    · si los participantes autorizados se retiran,
      el arbitraje se detiene aunque las reservas
      estén intactas
    · el número de participantes autorizados es
      un dato de riesgo tan importante como
      la composición de las reservas
    · concentración: si dos hacen el 80 % del
      arbitraje, el mecanismo tiene dos puntos
      únicos de fallo
```

### 4. Paridad de derecho frente a paridad de mercado

Hay dos paridades y conviene no confundirlas: una es una obligación exigible y
la otra es un precio observado. El bloque las define y describe qué se ve
cuando ambas se separan.

```text
PARIDAD DE DERECHO
  el emisor se obliga a entregar 1,00 por unidad
  es una obligación contractual
  se reclama ante un tribunal
  puede tener condiciones, plazos y suspensión

PARIDAD DE MERCADO
  el precio observado en las plataformas
  es un hecho, no un derecho
  puede estar por encima o por debajo

CUANDO SE SEPARAN
  · el emisor sigue redimiendo a 1,00 a los grandes
  · el mercado cotiza a 0,97 para los pequeños
  · ambos datos son ciertos a la vez

Y LA PRENSA INFORMARÁ DEL SEGUNDO
mientras el emisor comunicará el primero
```

### 5. Suspensión de la redención

Casi toda documentación contempla suspender la redención, y ese es el
apartado que decide el riesgo real del instrumento. El bloque recoge las
causas típicas, el efecto inmediato y qué hay que buscar al leerla.

```text
CASI TODA DOCUMENTACIÓN CONTEMPLA SUSPENDER

  causas típicas declaradas
    · circunstancias de mercado extraordinarias
    · requerimiento de una autoridad
    · fallo técnico
    · sospecha de actividad ilícita

  EFECTO INMEDIATO
    el arbitraje se apaga
    el precio queda a merced del flujo
    y quien no pudo salir soporta la diferencia

QUÉ MIRAR EN LA DOCUMENTACIÓN
  1 ¿quién decide la suspensión?
  2 ¿con qué criterio y qué plazo máximo?
  3 ¿hay obligación de comunicarlo y en cuánto tiempo?
  4 ¿se reanuda por orden de llegada o a prorrata?
```

## 🧮 Ejemplo guiado

El ejemplo calcula la banda de no arbitraje de una stablecoin. Conviene mirar quién puede redimir: si solo unos pocos participantes autorizados, la banda es mucho más ancha de lo que parece.

**Situación.** Una stablecoin con respaldo fiduciario cotiza a 0,9940. Hay que
decidir si arbitrar y calcular la banda que su diseño puede sostener.

```text
DATOS DEL EMISOR
  redención mínima                 100 000 unidades
  comisión de redención                    0,10 %
  plazo de liquidación                   2 días hábiles
  coste de operación en el registro   12 por operación

DATOS DE MERCADO
  precio de compra                        0,9940
  profundidad a ese precio            2 400 000 unid.
  coste de financiación anual              5,20 %
```

**Paso 1 — calcula el beneficio bruto por unidad.**

```text
COMPRA a 0,9940 · REDIME a 1,0000

  bruto por unidad = 1,0000 − 0,9940 = 0,0060
  → 60 puntos básicos
```

**Paso 2 — resta los costes.**

```text
SOBRE UNA OPERACIÓN DE 2 400 000 UNIDADES

  desembolso        2 400 000 × 0,9940 = 2 385 600
  se recibe                              2 400 000

  bruto                                     14 400

  MENOS
  comisión de redención  2 400 000 × 0,10 % = 2 400
  operación en registro                          12
  financiación 2 días
    2 385 600 × 5,20 % × 2/360 =                689

  total costes                                3 101

  NETO = 14 400 − 3 101 = 11 299
  rentabilidad sobre desembolso = 0,474 %
```

**Paso 3 — anualiza para compararlo.**

```text
LA OPERACIÓN DURA 2 DÍAS

  0,474 % × 360/2 = 85,3 % anualizado

  → ES MUY RENTABLE Y EL ARBITRAJE
    DEBERÍA ESTAR OCURRIENDO YA

Si el precio sigue en 0,9940, algo impide
que ocurra, y esa es la pregunta importante.
```

**Paso 4 — calcula la banda de no arbitraje.**

```text
¿QUÉ DESVÍO MÍNIMO HACE FALTA PARA QUE COMPENSE?

  costes fijos y proporcionales por unidad,
  sobre 2 400 000 unidades:

  comisión        0,0010 por unidad
  financiación    689 / 2 400 000 = 0,000287
  operación        12 / 2 400 000 = 0,000005

  coste total ≈ 0,001292 por unidad

  → CON UN DESVÍO MENOR DE 12,9 pb
    ARBITRAR NO COMPENSA

  BANDA DE NO ARBITRAJE: 0,99871 – 1,00129
```

**Paso 5 — comprueba el efecto del mínimo de redención.**

```text
UN TENEDOR CON 40 000 UNIDADES

  no alcanza el mínimo de 100 000
  → NO PUEDE REDIMIR

  su única salida es vender a 0,9940
  pérdida = 40 000 × 0,0060 = 240

PARA ÉL LA BANDA NO EXISTE:
el precio de mercado es el único precio.

EL MÍNIMO DE REDENCIÓN CONVIERTE
LA PARIDAD EN UN PRIVILEGIO DE TAMAÑO
```

**Paso 6 — explica por qué el desvío persiste.**

```text
SI ARBITRAR RINDE UN 85 % ANUALIZADO
Y NADIE LO HACE, LAS CAUSAS POSIBLES SON:

  a  la redención está suspendida
  b  los participantes autorizados agotaron
     su límite operativo con el emisor
  c  el plazo de 2 días es en realidad incierto
     y el riesgo percibido excede el beneficio
  d  hay dudas sobre las reservas y nadie quiere
     quedarse con el instrumento ni 2 días
  e  las plataformas no permiten retirar el importe

CADA CAUSA SE INVESTIGA DE FORMA DISTINTA,
Y LA d ES LA ÚNICA QUE ANTICIPA UNA CRISIS

→ UN DESVÍO PERSISTENTE ES UNA SEÑAL,
  NO UNA OPORTUNIDAD
```

**Paso 7 — deriva el indicador de vigilancia.**

```text
INDICADOR: DESVÍO PERSISTENTE FUERA DE BANDA

  medir  precio de mercado cada hora
  banda  calculada con los costes reales
  alerta si el precio permanece fuera de la banda
         más de N horas seguidas

  POR QUÉ FUNCIONA
    dentro de banda, el desvío es normal
    fuera de banda y persistente significa
    que el mecanismo de arbitraje no opera

  ESTE INDICADOR ANTICIPA LO QUE
  EL BALANCE DE RESERVAS NO MUESTRA
```

**Interpreta:** el arbitraje rentable que nadie ejecuta es la información más
valiosa del mercado. **Un desvío de 60 puntos básicos con reservas supuestamente
intactas dice que el canal de redención está cerrado**, y ese cierre es el
verdadero primer síntoma.

## 🧭 Perspectivas

La paridad significa cosas distintas para cada participante. La tabla las recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | «Vale 1» | Si lo usa para cobrar |
| Comercio | Un cobro que puede valer 0,994 | Si acepta y a qué precio |
| Fintech | Un riel de pagos | Si lo integra y con qué salvaguardas |
| Banco | Exposición indirecta vía clientes | Qué límites pone |
| Emisor | Presión sobre las reservas | Si suspende |
| Participante autorizado | Un arbitraje rentable | Si lo ejecuta o se retira |
| Custodio | Instrumento con riesgo de emisor | Cómo lo segrega |
| Mercado | Un precio fuera de banda | Cómo cotiza el riesgo |
| Supervisor | Señal temprana | Si pregunta al emisor |
| Auditor | Reservas y documentación | Qué puede atestiguar |
| Sociedad | Un medio de pago que falla | Qué protección espera |

## 🏦 Del cliente al banco

El cliente cree tener un peso y tiene un derecho contra un emisor. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Cotiza a 0,994, es temporal» | Desvío fuera de banda persistente | 20, clase 3 |
| «El emisor dice que hay reservas» | El precio dice que nadie puede redimir | 20, clase 3 |
| «Puedo cambiarlo cuando quiera» | Solo si supera el mínimo de redención | 20, clase 3 |

## ⚖️ Riesgos y controles

Los riesgos son de emisor y de mecanismo de paridad. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Arbitraje concentrado | Dos participantes lo sostienen todo | Medir y limitar la concentración |
| Mínimo de redención excluyente | Los pequeños no tienen derecho | Declararlo en la ficha del instrumento |
| Suspensión discrecional | El emisor cierra el canal | Leer causas, plazo y orden de reanudación |
| Banda mal calculada | Se confunde ruido con crisis | Calcular con costes reales |
| Desvío tomado por oportunidad | Se compra en la caída | Investigar la causa antes de operar |
| Paridad de derecho asumida | Se supone un derecho que no se tiene | Verificar el contrato, no el nombre |

## 🧪 Práctica

El laboratorio pide calcular la banda de no arbitraje de varias stablecoins. El acceso a la redención es lo que decide su anchura.

En [`labs/lab-01.md`](../labs/lab-01.md):

1. Calcula la banda de no arbitraje de tres diseños distintos.
2. Simula el efecto de subir el mínimo de redención.
3. Construye el indicador de desvío persistente y pruébalo con una serie.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen paridades que se rompen. La causa es la redención restringida o cerrada.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Creer que el respaldo fija el precio | Es la explicación intuitiva | Lo fija el arbitraje que el respaldo permite |
| Ignorar el mínimo de redención | No aparece en el resumen | Define quién tiene derecho |
| Banda de cero | Se supone paridad exacta | Los costes crean una banda |
| Comprar el desvío | Parece rentable | Investiga por qué nadie lo hizo |
| No contar participantes autorizados | No es un dato publicitado | Es un dato de riesgo de primer orden |
| Confundir atestación con auditoría | Los informes se parecen | Ver clase 4 |

## ❓ Preguntas de comprobación

1. ¿Qué mantiene realmente el precio de mercado en la paridad?
2. ¿Cómo se calcula la banda de no arbitraje y de qué depende su anchura?
3. ¿Qué diferencia hay entre paridad de derecho y paridad de mercado?
4. ¿Por qué un arbitraje rentable no ejecutado es una señal de alarma?
5. ¿Qué cuatro preguntas hay que hacerle a la cláusula de suspensión?

## 📥 Entregable

Guarda en `portfolio/parte-20/clase-03/`:

- el cálculo de la banda de no arbitraje con costes desglosados;
- el análisis de quién puede redimir y con qué mínimo;
- las cuatro respuestas sobre la cláusula de suspensión de un emisor real;
- el indicador de desvío persistente con su umbral justificado.

## 🔗 Referencias cruzadas

- **Viene de:** clase 1.
- **Continúa en:** clases 4, 5, 6 y 7 de esta parte.
- **Se aplica en:** Parte 21, clase 14; Parte 22, clase 5; Parte 23, clase 6.

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

- Financial Stability Board (2023). *High-level Recommendations for the Regulation, Supervision and Oversight of Global Stablecoin Arrangements*. FSB. <https://www.fsb.org/2023/07/high-level-recommendations-for-the-regulation-supervision-and-oversight-of-global-stablecoin-arrangements-final-report/>
- CPMI e IOSCO (2022). *Application of the Principles for Financial Market Infrastructures to stablecoin arrangements*. BIS. <https://www.bis.org/cpmi/publ/d206.htm>
- Bank for International Settlements (2023). *Stablecoins: fundamentals, emerging issues and open questions*. BIS. <https://www.bis.org/publ/work905.htm>
- Diario Oficial de la Unión Europea (2023). *Reglamento (UE) 2023/1114 relativo a los mercados de criptoactivos*. EUR-Lex. <https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32023R1114>
- Verificación local: comprueba en la fuente oficial vigente qué obligaciones de redención impone tu jurisdicción y si admite mínimos o participantes autorizados exclusivos. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 02 · Criptoactivos no respaldados](02-criptoactivos-no-respaldados.md) | [Parte 20](../README.md) · [Programa](../../../SYLLABUS.md) | [04 · Reservas: composición, calidad y verificación →](04-reservas-composicion-calidad-y-verificacion.md) |
<!-- gen:footer:end -->
