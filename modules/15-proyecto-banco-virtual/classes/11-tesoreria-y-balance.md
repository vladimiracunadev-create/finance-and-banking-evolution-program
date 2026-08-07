<!-- meta
part: 16
class: 11
title: "Tesorería y balance"
level: profesional
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 11 · Tesorería y balance

> [← 10 · Contabilidad y estados financieros](10-contabilidad-y-estados-financieros.md) · [Índice de la parte](../README.md) · [12 · Marco de riesgos →](12-marco-de-riesgos.md)

**Parte 16 — Proyecto Banco Virtual** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Gestionar la liquidez y el balance estructural del Banco Austral. El estado de flujo de la clase
anterior mostró un banco que **genera resultado y consume caja**, financiado en un 78 % con recursos
mayoristas: esta clase determina si esa estructura es sostenible y qué hay que cambiar.

Los estados de la clase anterior muestran un balance. Esta lo gestiona, aplicando las Partes 10 y 11: cómo se financia el banco, cuánta liquidez mantiene y qué riesgo de tasa asume. Y añade la pregunta que la Parte 15 introdujo: cuál de las restricciones es la que de verdad limita.

## 📚 Objetivos

Al finalizar podrás:

1. **Construir** la estructura de financiamiento y evaluar su vulnerabilidad.
2. **Calcular** la cobertura de liquidez y el financiamiento estable neto.
3. **Medir** la brecha de repreciación y el riesgo de tasa.
4. **Diseñar** el plan de financiamiento de contingencia.
5. **Optimizar** el balance contra su restricción activa.

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

Los cuatro primeros términos son la estructura de financiamiento y sus métricas; los cuatro siguientes, el riesgo de tasa y la contingencia. La **dependencia mayorista** es la vulnerabilidad característica de un banco nuevo: sin base de depósitos minoristas, el fondeo es más caro y mucho menos estable.

| Concepto | Comprensión verificable |
|---|---|
| `estructura de financiamiento` | Composición de las fuentes de fondos. |
| `dependencia mayorista` | Proporción del financiamiento no minorista. |
| `cobertura de liquidez` | Activos líquidos sobre salidas netas a 30 días. |
| `financiamiento estable neto` | Financiamiento estable disponible sobre requerido. |
| `brecha de repreciación` | Diferencia entre activos y pasivos que repactan en un tramo. |
| `plan de contingencia de liquidez` | Fuentes y acciones activables con disparadores. |
| `colateral elegible` | Activo aceptable en las facilidades del banco central. |
| `restricción activa` | La que limita efectivamente el crecimiento. |

## 🧠 Modelo mental

El modelo mental es un balance con varias restricciones simultáneas y una sola apretando. Un banco nuevo suele estar limitado por liquidez y no por capital, que es lo contrario de lo que la intuición sugiere.

```text
LA VULNERABILIDAD ESTRUCTURAL DEL BANCO AUSTRAL

  depósitos de clientes:      81 920   (19 %)
  financiamiento mayorista:  321 136   (74 %)
  capital:                    60 615    (7 %)

  UN BANCO CUYO FINANCIAMIENTO ES 74 % MAYORISTA
  DEPENDE DE QUE EL MERCADO LE PRESTE CADA MES

  y el mercado deja de prestar exactamente cuando
  el banco lo necesita (Parte 11, clase 4)

ESTA ES LA MAYOR DEBILIDAD DEL PROYECTO
  y aparece recién ahora porque el diseño
  se centró en el activo
```

## 📖 Desarrollo

### 1. Estructura de financiamiento

La estructura de financiamiento del Banco Austral se define con fuentes y proporciones. La tabla la recoge.

| Fuente | Monto | Estabilidad | Costo |
|---|---:|---|---:|
| Cuenta de pagos (P1) | 28 560 | Alta, con seguro | 0,00 % |
| Ahorro programado (P3) | 18 400 | Alta | 5,20 % |
| Cuenta empresa (E1) | 34 960 | Media | 0,00 % |
| Emisión a 3 años | 120 000 | Alta, hasta vencer | 9,10 % |
| Emisión a 18 meses | 90 000 | Media | 8,60 % |
| Financiamiento interbancario | 111 136 | Baja | 7,80 % |
| **Total** | **403 056** | | |

```text
EL PROBLEMA ESTÁ EN LOS 111 136 INTERBANCARIOS
  se renuevan constantemente
  se supone 100 % de salida en estrés
  y son el 27,6 % del financiamiento total
```

### 2. Cobertura de liquidez

La cobertura se calcula con los supuestos de la Parte 11. El procedimiento la obtiene.

```text
ACTIVOS LÍQUIDOS DE ALTA CALIDAD
  disponible en el banco central        32 400   nivel 1
  deuda soberana local                  74 200   nivel 1
  otros activos elegibles               15 800   nivel 2A, −15 %
  TOTAL AJUSTADO: 32 400 + 74 200 + 13 430 = 120 030

SALIDAS EN 30 DÍAS DE ESTRÉS
  P1 minorista, cubierto por seguro
    28 560 × 5 %                          1 428
  P3 ahorro, cubierto
    18 400 × 5 %                            920
  E1 empresa, operativo
    34 960 × 25 %                         8 740
  interbancario que vence en 30 días
    46 000 × 100 %                       46 000
  líneas E2 no utilizadas
    78 892 × 20 %                        15 778
  SALIDAS BRUTAS                         72 866

ENTRADAS
  vencimientos de cartera a 30 días      18 400
  tope del 75 % de las salidas: 54 650  → se reconocen 18 400

SALIDAS NETAS: 54 466
COBERTURA: 120 030 / 54 466 = 220,4 %
```

```text
UNA COBERTURA DEL 220 % PARECE EXCELENTE
Y REVELA OTRO PROBLEMA

  el banco mantiene 120 030 de activos líquidos
  con un costo neto de 2,30 puntos (clase 6)
  costo anual: 2 761

  ¿POR QUÉ TANTO?
    porque su apetito exige 130 % (clase 2)
    y el mínimo normativo es 110 %
    → con 130 % bastarían 70 806 de activos líquidos
    → los 49 224 excedentes cuestan 1 132 anuales
```

### 3. Financiamiento estable neto

La segunda métrica mira el horizonte anual. El procedimiento la calcula.

```text
FINANCIAMIENTO ESTABLE DISPONIBLE
  capital                          60 615 × 100 % =  60 615
  emisión a 3 años                120 000 × 100 % = 120 000
  emisión a 18 meses               90 000 × 100 % =  90 000
  P1 minorista                     28 560 ×  90 % =  25 704
  P3 ahorro                        18 400 ×  90 % =  16 560
  E1 empresa                       34 960 ×  50 % =  17 480
  interbancario < 1 año           111 136 ×   0 % =       0
  TOTAL DISPONIBLE: 330 359

FINANCIAMIENTO ESTABLE REQUERIDO
  activos líquidos nivel 1        106 600 ×   5 % =   5 330
  activos líquidos nivel 2A        13 430 ×  15 % =   2 015
  cartera P2 (< 1 año)             62 000 ×  50 % =  31 000
  cartera P2 (> 1 año)             56 048 ×  85 % =  47 641
  cartera E2 (revolvente)         214 000 ×  50 % = 107 000
  cartera E3                        3 923 ×  10 % =     392
  activo fijo e intangibles         8 400 × 100 % =   8 400
  otros activos                    12 600 ×  85 % =  10 710
  líneas no utilizadas             78 892 ×   5 % =   3 945
  TOTAL REQUERIDO: 216 433

NSFR: 330 359 / 216 433 = 152,6 %
```

```text
EL NSFR ES HOLGADO PORQUE EL BANCO EMITIÓ A PLAZO
  las emisiones a 3 años y 18 meses computan al 100 %

  PERO ESO CAMBIA
    la emisión a 18 meses, cuando le queden 11 meses,
    computa al 50 %; con menos de 6, al 0 %
    → el NSFR se deteriora por el simple paso del tiempo
```

### 4. Riesgo de tasa

La brecha de repreciación mide el efecto de un cambio de tasas sobre el margen. El procedimiento la calcula.

```text
BRECHA DE REPRECIACIÓN

  tramo        activos    pasivos     brecha
  0-30 días     32 400    157 136   −124 736
  31-90         48 200     36 000    +12 200
  91-180        62 400     28 000    +34 400
  181-365       94 800     42 000    +52 800
  1-3 años     186 400    120 000    +66 400
  > 3 años      50 017     19 920    +30 097

  BRECHA ACUMULADA A 12 MESES: −25 336
```

```text
SENSIBILIDAD DEL MARGEN
  alza de 200 pb:
  Δ margen ≈ −25 336 × 2,0 % × 0,5 = −253

  sobre un margen financiero de 43 499: −0,58 %
  → efecto acotado

SENSIBILIDAD DEL VALOR ECONÓMICO
  duración del activo: 1,42 años
  duración del pasivo: 1,08 años
  apalancamiento: 422 317/474 217 = 0,891
  brecha de duración: 1,42 − 1,08 × 0,891 = 0,458

  alza de 200 pb:
  Δ VEP ≈ −0,458 × 2,0 % × 474 217 = −4 344
  sobre capital de 55 575: −7,8 %

  umbral de atención: 15 %  → dentro  ✓
```

### 5. Restricción activa

La restricción activa se identifica comparando holguras. El procedimiento lo hace.

```text
CAPACIDAD DE CRECIMIENTO POR RESTRICCIÓN

  CAPITAL
    capital 55 575, objetivo 14,0 %
    activos ponderados máximos: 396 964
    actuales: 311 725
    capacidad: 85 239 de APR → 109 277 de cartera

  APALANCAMIENTO
    capital nivel 1 55 575, mínimo 3 %
    exposición máxima: 1 852 500
    actual: 553 109
    capacidad: enorme

  COBERTURA DE LIQUIDEZ
    con apetito de 130 %: activos líquidos mínimos 70 806
    disponibles: 120 030
    capacidad: crecer hasta que las salidas netas
    lleguen a 92 331 → 37 865 de salidas adicionales
    → equivale a ~189 000 de cartera adicional
    (por el efecto de las líneas no utilizadas)

  FINANCIAMIENTO ESTABLE
    con mínimo de 105 %: requerido máximo 314 628
    actual: 216 433
    capacidad: 98 195 de requerido
    → equivale a ~145 000 de cartera adicional

  RESTRICCIÓN ACTIVA: CAPITAL  (109 277 de cartera)
```

## 🧮 Ejemplo guiado

El ejemplo calcula las métricas de liquidez del Banco Austral e identifica su restricción activa. La restricción no es el capital, que es lo que el proyecto suponía.

**Situación.** Resolver la dependencia de financiamiento mayorista.

```text
PROBLEMA
  74 % del financiamiento es mayorista
  de ese, 111 136 es interbancario de corto plazo

  ESCENARIO: el mercado interbancario se cierra
  para el Banco Austral durante 60 días
```

**Paso 1 — proyecta el escenario.**

```text
VENCIMIENTOS INTERBANCARIOS
  días 1-30:   46 000
  días 31-60:  38 000
  días 61-90:  27 136

  A 60 DÍAS: 84 000 que no se renuevan

  RECURSOS DISPONIBLES
    activos líquidos: 120 030
    vencimientos de cartera a 60 días: 34 200
    TOTAL: 154 230

  ¿SE CUBRE? sí, con 70 230 de holgura
```

**Paso 2 — proyecta el escenario extendido.**

```text
SI EL CIERRE DURA 180 DÍAS
  vencimientos interbancarios: 111 136 (todos)
  vencimiento de la emisión a 18 meses (si cae en el período)
  + salida de depósitos por la señal: estimada 18 %
    81 920 × 18 % = 14 746

  NECESIDAD: 125 882
  RECURSOS
    activos líquidos: 120 030
    vencimientos de cartera a 180 días: 96 400
    TOTAL: 216 430

  ¿SE CUBRE? sí, PERO
    usar los vencimientos de cartera significa
    NO RENOVAR créditos a clientes
    → la cartera se reduce en 96 400  (29 %)
    → el banco deja de operar como banco
```

**Paso 3 — evalúa el colateral elegible.**

```text
ACTIVOS ELEGIBLES EN LAS FACILIDADES DEL BANCO CENTRAL
  deuda soberana (ya en activos líquidos):  74 200
  cartera de créditos elegible:
    la cartera E2 con cesión de flujo puede
    ser elegible según la norma local
    saldo elegible estimado: 128 400
    descuento aplicable: 35 %
    capacidad: 83 460

  CAPACIDAD TOTAL CON COLATERAL PREPARADO
    120 030 (líquidos) + 83 460 (cartera pignorable)
    = 203 490

  → cubre el escenario de 180 días
    SIN reducir la cartera
```

**Paso 4 — verifica la preparación del colateral.**

```text
LA LECCIÓN DE LA PARTE 15, CLASE 13
  el colateral disponible y no preparado
  no sirve en una crisis

  PREPARACIÓN REQUERIDA
    · contrato marco con el banco central firmado
    · cartera identificada y con documentación completa
    · proceso de constitución probado
    · prueba anual de movilización

  COSTO DE LA PREPARACIÓN: 84 anuales
  VALOR: 83 460 de capacidad disponible en horas
```

**Paso 5 — reduce la dependencia estructural.**

```text
OBJETIVO: bajar el financiamiento mayorista
de 74 % a 55 % en 24 meses

  ESO EXIGE AUMENTAR LOS DEPÓSITOS
  de 81 920 a 181 375

  ¿CÓMO?
    a) depósito a plazo (producto no incluido en el catálogo)
       tasa competitiva: 8,20 %
       captación estimada: 62 000 en 24 meses
       costo: por encima de la emisión a 18 meses (8,60 %)
       → NO: el depósito a plazo es MÁS BARATO
         y computa mejor en el NSFR

    b) aumentar el saldo medio de P1 y E1
       con servicios que retengan el saldo
       potencial: 24 000

    c) captación de nómina de empresas clientes
       9 200 empresas × 18 empleados × 0,42 de saldo
       potencial: 34 800 en 24 meses

  TOTAL POTENCIAL: 120 800
  → supera el objetivo
```

**Paso 6 — evalúa el efecto del depósito a plazo.**

```text
AÑADIR EL PRODUCTO P5 — DEPÓSITO A PLAZO

  costo fijo del producto: 1,81 anuales

  EFECTO ECONÓMICO
    62 000 captados al 8,20 %
    sustituyen a interbancario al 7,80 %
    costo adicional: 62 000 × 0,40 % = 248

    ¿POR QUÉ PAGAR MÁS?
      · el depósito a plazo computa al 90-95 %
        en el NSFR; el interbancario, al 0 %
      · en estrés, el depósito a plazo tiene
        una salida supuesta del 5-10 %;
        el interbancario, del 100 %
      · el depósito minorista está cubierto
        por el seguro de depósitos

    EL SOBRECOSTO DE 248 ES EL PRECIO
    DE ELIMINAR 62 000 DE VULNERABILIDAD
```

**Paso 7 — recalcula la estructura.**

```text
ESTRUCTURA OBJETIVO AL AÑO 5

  depósitos de clientes:     181 375   (43 %)
    P1 cuenta de pagos:       42 000
    P3 ahorro:                26 400
    E1 cuenta empresa:        50 975
    P5 depósito a plazo:      62 000
  emisiones a plazo:         180 000   (43 %)
  interbancario:              30 000    (7 %)
  capital:                    30 000*   (7 %)
  * capital adicional generado

  DEPENDENCIA MAYORISTA: 50 %
  frente al 74 % actual
```

**Paso 8 — decide el uso de la holgura de liquidez.**

```text
LOS 49 224 DE ACTIVOS LÍQUIDOS EXCEDENTES
CUESTAN 1 132 ANUALES

  ¿SE REDUCEN?

  ARGUMENTOS A FAVOR
    · el apetito de 130 % es propio, no normativo
    · el mínimo es 110 %
    · 1 132 anuales es el 5,2 % del resultado

  ARGUMENTOS EN CONTRA
    · el banco tiene 74 % de financiamiento mayorista
    · su apetito de 130 % se fijó precisamente
      porque es un banco nuevo y vulnerable (clase 2)
    · reducir el colchón antes de reducir
      la dependencia es invertir el orden

  DECISIÓN
    mantener el 130 % hasta que la dependencia
    mayorista baje del 60 %
    entonces revisar el apetito a 120 %

  Y REGISTRARLO COMO DECISIÓN CONDICIONADA
    con su disparador explícito
```

**Interpreta:** el balance del Banco Austral cumple **todos los indicadores con holgura** y tiene una
vulnerabilidad estructural que ningún indicador muestra: el 74 % de su financiamiento depende de que el
mercado se lo renueve. Los ratios de liquidez miden 30 días y un año; la dependencia estructural se mide
en la composición, y su corrección tarda 24 meses. Es el tipo de riesgo que hay que ver antes de que
importe.

## 🏦 Del cliente al banco

El cliente deposita y el banco gestiona un balance con varias restricciones simultáneas. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «El banco me ofrece depósito a plazo» | Reducción de dependencia mayorista | 16, clase 11 |
| «Su tasa de depósito es competitiva» | Vale más que el interbancario | 16, clase 11 |
| «Mi banco tiene mucha liquidez» | Colchón por su vulnerabilidad estructural | 11, clase 4 |
| «Me pidieron traer la nómina» | Captación de saldos estables | 13, clase 1 |
| «El banco resistió el cierre del mercado» | Colateral preparado | 15, clase 13 |

## 🧪 Práctica

El laboratorio pide calcular las métricas y determinar la restricción activa. La consecuencia sobre el plan de crecimiento es parte del entregable.

En `labs/lab-06.md`:

1. Construye la estructura de financiamiento y evalúa su vulnerabilidad.
2. Calcula cobertura de liquidez, financiamiento estable y brecha de repreciación.
3. Proyecta un cierre del mercado mayorista a 60 y 180 días.
4. Diseña el plan de reducción de la dependencia con su costo.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen problemas de balance en bancos nuevos. Las causas son dependencia mayorista y restricción activa mal identificada.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Indicadores holgados y estructura frágil | Miden plazos, no composición | Evalúa la dependencia. |
| Colateral disponible sin preparar | No sirve en crisis | Prepáralo y pruébalo. |
| Se cubre el estrés con vencimientos de cartera | Deja de operar como banco | Usa colateral, no reducción. |
| Se reduce el colchón antes que la dependencia | Orden invertido | Primero la causa. |
| Interbancario visto como barato | Es el más frágil | Su costo real incluye su fragilidad. |
| NSFR holgado sin proyectar | Se deteriora por el paso del tiempo | Proyecta el vencimiento de emisiones. |

## ❓ Preguntas de comprobación

1. ¿Por qué una dependencia mayorista del 74 % es una vulnerabilidad estructural?
2. ¿Por qué cubrir un estrés con vencimientos de cartera no es una solución?
3. ¿Por qué el depósito a plazo más caro es preferible al interbancario más barato?
4. ¿Por qué el NSFR se deteriora sin que nada cambie?
5. ¿Por qué se reduce la dependencia antes que el colchón?

## 📥 Entregable

Guarda en `portfolio/parte-16/clase-11/`:

- la estructura de financiamiento con su evaluación de vulnerabilidad;
- los tres indicadores calculados con sus componentes;
- la proyección del cierre del mercado a 60 y 180 días;
- el plan de reducción de dependencia con su costo y sus disparadores.

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

- Basel Committee on Banking Supervision (2013). *Basel III: The Liquidity Coverage Ratio*. BIS.
- Basel Committee on Banking Supervision (2014). *Basel III: The Net Stable Funding Ratio*. BIS.
- Basel Committee on Banking Supervision (2008). *Principles for Sound Liquidity Risk Management and Supervision*. BIS.
- Basel Committee on Banking Supervision (2016). *Interest rate risk in the banking book*. BIS.
- Bank for International Settlements (2023). *Annual Economic Report*, capítulo sobre las turbulencias bancarias de 2023.
- Verificación local: revisa qué activos y qué carteras acepta tu banco central como colateral, con qué descuentos y qué preparación exige.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 10 · Contabilidad y estados financieros](10-contabilidad-y-estados-financieros.md) | [Parte 16](../README.md) · [Programa](../../../SYLLABUS.md) | [12 · Marco de riesgos →](12-marco-de-riesgos.md) |
<!-- gen:footer:end -->
