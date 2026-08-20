<!-- meta
part: 15
class: 6
title: "Gestión del balance"
level: profesional
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 06 · Gestión del balance

> [← 05 · Planificación estratégica y de capital](05-planificacion-estrategica-y-de-capital.md) · [Índice de la parte](../README.md) · [07 · Política de precios →](07-politica-de-precios.md)

**Parte 15 — Estrategia y dirección bancaria** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Optimizar la composición del balance de un banco sujeta a todas sus restricciones a la vez: capital,
liquidez, apalancamiento, financiamiento estable, rentabilidad y apetito de riesgo. Es un problema de
optimización con restricciones múltiples, y **la restricción que domina cambia con el entorno**.

El plan de la clase anterior está limitado por varias restricciones a la vez: capital, liquidez y apalancamiento. Esta clase identifica cuál de ellas manda de verdad, porque optimizar contra la restricción equivocada consume esfuerzo sin liberar nada.

## 📚 Objetivos

Al finalizar podrás:

1. **Identificar** la restricción activa de un balance en cada momento.
2. **Calcular** el consumo de cada restricción por unidad de cada activo.
3. **Optimizar** la composición del balance con criterios explícitos.
4. **Evaluar** los instrumentos de gestión del balance.
5. **Anticipar** el efecto de un cambio de entorno sobre la restricción activa.

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

Los cuatro primeros términos son las restricciones y su medida; los cuatro siguientes, los instrumentos para gestionarlas. El **retorno por unidad de restricción** es la medida que ordena las decisiones: cuánto se gana por cada unidad del recurso que escasea.

| Concepto | Comprensión verificable |
|---|---|
| `restricción activa` | La que limita efectivamente la decisión. |
| `holgura` | Distancia entre el nivel actual y el límite de una restricción. |
| `consumo unitario` | Cuánto consume de cada restricción una unidad de un activo. |
| `retorno por unidad de restricción` | Resultado por cada unidad de la restricción escasa. |
| `titularización` | Transformación de una cartera en valores negociables. |
| `venta de cartera` | Transferencia de activos a un tercero. |
| `optimización de activos ponderados` | Reducción del denominador sin reducir el negocio. |
| `balance estructural` | Composición de largo plazo del activo y del pasivo. |

## 🧠 Modelo mental

El modelo mental es una restricción activa: de todas las que limitan al banco, solo una está apretando en cada momento. Todo el rendimiento marginal está en esa, y cuando se libera, otra pasa a ser la activa.

```text
UN BANCO OPTIMIZA SUJETO A CINCO RESTRICCIONES

  1. capital sobre activos ponderados
  2. apalancamiento sobre exposición total
  3. cobertura de liquidez a 30 días
  4. financiamiento estable neto a 1 año
  5. límites de apetito y de concentración

EN CADA MOMENTO, UNA SOLA ES LA ACTIVA
  y la decisión correcta es maximizar el retorno
  POR UNIDAD DE ESA RESTRICCIÓN

  optimizar contra la restricción equivocada
  produce decisiones que parecen buenas
  y no mejoran nada
```

**Ejemplo del error:** un banco cuya restricción activa es el apalancamiento decide crecer en activos de
baja ponderación de riesgo. Su ratio de capital mejora, su apalancamiento empeora, y su capacidad de
crecer no aumenta en absoluto.

## 📖 Desarrollo

### 1. Consumo unitario por restricción

Cada operación consume distintas cantidades de cada restricción. La tabla las recoge.

| Activo | Ponderación de riesgo | Apalancamiento | Cobertura de liquidez | Financiamiento estable requerido |
|---|---:|---:|---|---:|
| Efectivo y reservas | 0 % | 100 % | Aporta | 0 % |
| Deuda soberana de alta calidad | 0 % | 100 % | Aporta | 5 % |
| Crédito hipotecario (LTV bajo) | 30 % | 100 % | Neutro | 65 % |
| Crédito de consumo | 75 % | 100 % | Neutro | 85 % |
| Crédito comercial | 90 % | 100 % | Neutro | 85 % |
| Línea no utilizada | 20-50 % | 10-40 % | Consume | 5 % |
| Derivados | Según método | Según método | Consume margen | Según posición |

Leida por filas, la tabla describe activos; leida por columnas, plantea un
dilema que no tiene solución optima.

```text
LEE LA TABLA POR COLUMNAS Y APARECE EL DILEMA
  la deuda soberana no consume capital ponderado
  y consume apalancamiento igual que un crédito

  el crédito hipotecario consume poco capital ponderado
  y mucho financiamiento estable

  no hay un activo bueno en todas las columnas
```

### 2. Identificar la restricción activa

La restricción activa se identifica comparando holguras. El procedimiento siguiente lo hace.

```text
PROCEDIMIENTO
  1. calcula la holgura de cada restricción,
     expresada en capacidad de crecimiento
  2. la menor de todas es la restricción activa
```

Aplicado a un balance concreto, el procedimiento traduce cada restricción a capacidad de crecimiento y deja ver cuál es la que realmente limita.

```text
EJEMPLO
  capital: 12,46 %, requerimiento 11,34 %
    capacidad: 329 400/0,1134 − 2 642 900 = 262 830 de APR
    → equivale a ~350 000 de cartera al mix actual

  apalancamiento: 11,28 %, mínimo 3,00 %
    capacidad: 371 400/0,03 − 3 291 400 = 9 088 600 de exposición

  cobertura de liquidez: 131 %, mínimo 110 %
    capacidad: depende de la composición del crecimiento

  financiamiento estable: 118 %, mínimo 105 %
    capacidad: 118/105 = 12,4 % de crecimiento del activo largo

  RESTRICCIÓN ACTIVA: capital
  la menor capacidad de crecimiento
```

### 3. Retorno por unidad de restricción

El retorno se calcula sobre la restricción activa y no sobre el capital por defecto. El procedimiento lo obtiene.

```text
CON LA RESTRICCIÓN IDENTIFICADA, SE ORDENAN
LOS ACTIVOS POR SU RETORNO POR UNIDAD DE ELLA

  si la restricción es CAPITAL:
    retorno por unidad de activo ponderado

  si es APALANCAMIENTO:
    retorno por unidad de exposición

  si es FINANCIAMIENTO ESTABLE:
    retorno por unidad de financiamiento estable requerido
```

| Activo | Margen neto | APR por unidad | Retorno por APR |
|---|---:|---:|---:|
| Crédito de consumo | 12,2 % | 0,75 | 16,3 % |
| Crédito comercial | 5,4 % | 0,90 | 6,0 % |
| Hipotecario | 2,4 % | 0,30 | 8,0 % |
| Deuda soberana | 0,6 % | 0,00 | infinito |

El orden que produce la última columna es el que debe guiar el crecimiento,
con una excepción que conviene mirar dos veces.

```text
LA COLUMNA FINAL ORDENA LAS DECISIONES
  con capital como restricción activa,
  el consumo crece mejor que el comercial
  y el hipotecario mejor que el comercial

  y la deuda soberana no consume capital ponderado:
  parece infinitamente rentable
  → hasta que se mira el apalancamiento
```

### 4. Instrumentos de gestión

Hay instrumentos para liberar cada restricción, con sus costos. La tabla los recoge.

| Instrumento | Qué libera | Costo | Consideraciones |
|---|---|---|---|
| Venta de cartera | Capital, apalancamiento, financiamiento | Descuento sobre valor libro | Pérdida de la relación |
| Titularización | Capital si hay transferencia de riesgo | Costo de estructura | Requisitos de transferencia significativa |
| Garantías y coberturas | Capital por mitigación | Prima | Elegibilidad del mitigante |
| Cambio de mix de originación | Capital, gradual | Menor crecimiento donde se reduce | Efecto lento |
| Emisión de instrumentos computables | Capital | Cupón | Ventana de mercado |
| Reducción de líneas no utilizadas | Capital y apalancamiento | Relación con clientes | Efecto inmediato |
| Alargamiento del financiamiento | Financiamiento estable | Mayor costo de fondos | Efecto inmediato |
| Compra de activos líquidos | Cobertura de liquidez | Diferencial negativo | Empeora apalancamiento |

El primero de esos instrumentos solo cumple su función si se cumple una
condición que el marco prudencial verifica con detalle.

```text
LA TITULARIZACIÓN SOLO LIBERA CAPITAL
SI HAY TRANSFERENCIA SIGNIFICATIVA DE RIESGO

  vender la cartera y retener el primer tramo de pérdida
  no transfiere el riesgo: lo concentra
  → el marco prudencial no reconoce
    la liberación de capital en ese caso
```

### 5. Cambio de restricción activa

Liberar una restricción hace que otra pase a ser la activa, y conviene saber cuál. El esquema lo muestra.

```text
LA RESTRICCIÓN ACTIVA CAMBIA CON EL ENTORNO

  entorno de tasas bajas y balance con muchos activos líquidos
    → APALANCAMIENTO

  entorno de crecimiento del crédito
    → CAPITAL

  entorno de salida de depósitos
    → LIQUIDEZ Y FINANCIAMIENTO ESTABLE

  entorno de deterioro de cartera
    → CAPITAL, por el consumo de provisiones

ANTICIPARLO PERMITE ACTUAR ANTES
  el instrumento que libera una restricción
  suele estar disponible solo cuando no se necesita
```

## 🧮 Ejemplo guiado

El ejemplo identifica la restricción activa de un banco y ordena sus operaciones por retorno sobre ella. El orden cambia respecto del que da la rentabilidad sobre capital.

**Situación.** Un banco debe liberar capital para financiar el plan de la clase anterior.

```text
SITUACIÓN
  activos ponderados                     2 642 900
  capital nivel 1 ordinario                329 400   (12,46 %)
  objetivo interno revisado                  14,20 %
  capital necesario para el objetivo:
    0,1420 × 2 642 900 = 375 292
  DÉFICIT CONTRA EL OBJETIVO: 45 892

  el plan a 3 años lo cierra con resultado retenido
  pero el directorio quiere alcanzar el objetivo en 12 meses
```

**Paso 1 — verifica que capital sea la restricción activa.**

```text
capital:                déficit de 45 892 contra el objetivo
apalancamiento:         11,28 % contra un mínimo de 3,00 %
cobertura de liquidez:  131 % contra 110 %
financiamiento estable: 118 % contra 105 %
concentración:          24,1 % contra un límite de 25 %

RESTRICCIÓN ACTIVA: capital
SEGUNDA MÁS AJUSTADA: concentración sectorial (0,9 puntos)
```

**Paso 2 — evalúa la venta de cartera.**

```text
CARTERA CANDIDATA: comercial del sector construcción
  saldo: 493 000  (el 24,1 % de concentración)
  ponderación media: 92 %
  activos ponderados: 453 560

VENTA DEL 20 % (98 600)
  activos ponderados liberados: 90 712
  efecto en el ratio: 329 400 / 2 552 188 = 12,91 %
  mejora: 0,45 puntos

  COSTO
    descuento sobre valor libro: 2,4 % = 2 366
    margen anual perdido: 98 600 × 5,4 % = 5 324
    pérdida de la relación con esos clientes

  EFECTO ADICIONAL
    concentración sectorial: 24,1 % → 19,3 %  ✓
    resuelve las dos restricciones a la vez
```

**Paso 3 — evalúa la titularización.**

```text
CARTERA HIPOTECARIA: 890 000, ponderación 30 %
  activos ponderados: 267 000

TITULARIZACIÓN DE 300 000
  activos ponderados liberados si hay transferencia
  significativa: 90 000

  ESTRUCTURA
    tramo sénior (85 %): 255 000, colocado en el mercado
    tramo intermedio (10 %): 30 000, colocado
    tramo de primera pérdida (5 %): 15 000

  ¿QUIÉN RETIENE EL TRAMO DE PRIMERA PÉRDIDA?
    si lo retiene el banco: no hay transferencia significativa
    → no libera capital, y el tramo retenido
      se deduce del capital

    si se coloca: hay transferencia
    → libera capital, con un costo de colocación alto
      (el tramo de primera pérdida es el más caro de colocar)

  COSTO ESTIMADO
    estructura y colocación: 4 200
    diferencial del tramo de primera pérdida: alto
    margen retenido: 300 000 × 0,8 % = 2 400 anuales
    margen perdido: 300 000 × 2,4 % − 2 400 = 4 800 anuales
```

**Paso 4 — evalúa la reducción de líneas no utilizadas.**

```text
LÍNEAS COMPROMETIDAS NO UTILIZADAS: 240 000
  factor de conversión: 50 %
  activos ponderados: 120 000

REDUCCIÓN DEL 30 % (72 000 de nominal)
  activos ponderados liberados: 36 000
  efecto en el ratio: +0,17 puntos

  COSTO
    comisión de disponibilidad perdida: 72 000 × 0,4 % = 288
    relación con clientes: reducir una línea comprometida
    es una señal negativa para el cliente

  ANÁLISIS DE LAS LÍNEAS
    utilización media de las líneas: 34 %
    líneas con utilización < 5 % en 24 meses: 84 000
    → esas se pueden reducir con bajo impacto en la relación
```

**Paso 5 — evalúa la emisión de instrumentos computables.**

```text
EMISIÓN DE AT1 POR 40 000
  computa como capital nivel 1, no como CET1
  → NO mejora el ratio CET1
  → mejora el ratio de capital nivel 1 y el total

  el objetivo interno está definido sobre CET1
  → esta opción NO resuelve el problema planteado

LECCIÓN
  verifica siempre sobre qué ratio está definido el objetivo
```

**Paso 6 — evalúa el cambio de mix de originación.**

```text
REDUCIR EL CRECIMIENTO DEL CONSUMO DE 14 % A 10 %
  activos ponderados no originados:
    520 000 × 4 % × 75 % = 15 600 en el año 1
  efecto: +0,07 puntos en el ratio

  efecto lento, y ya está en el plan corregido
  de la clase anterior
```

**Paso 7 — construye la combinación.**

```text
                              APR liberados  ratio  costo anual
  venta de cartera (20 %)          90 712    +0,45      5 324
  reducción de líneas sin uso      42 000    +0,20        336
  titularización de 200 000        60 000    +0,29      3 200
  cambio de mix                    15 600    +0,07          0
  TOTAL                           208 312    +1,01      8 860

  ratio resultante: 329 400 / 2 434 588 = 13,53 %
  objetivo: 14,20 %
  DÉFICIT RESIDUAL: 0,67 puntos = 16 312
```

**Paso 8 — cierra el déficit residual y decide.**

```text
EL RESULTADO RETENIDO DEL AÑO 1
  resultado neto proyectado: 67 716
  dividendos al 40 %: 27 086
  retención: 40 630

  con la retención del año 1:
    capital: 370 030
    ratio: 370 030 / 2 434 588 = 15,20 %  ✓ supera el objetivo

DECISIÓN FINAL
  1. venta del 20 % de la cartera de construcción
     → resuelve capital y concentración simultáneamente
     → costo: 5 324 anuales de margen + 2 366 de descuento
  2. reducción de las 84 000 de líneas sin uso
     → costo mínimo, efecto inmediato
  3. la decisión sobre titularizar exige comparar
     el costo por punto de capital de cada instrumento,
     no su costo absoluto

  COSTO POR PUNTO DE CAPITAL LIBERADO
    venta de cartera:  5 324 / 0,45 = 11 831 por punto
    reducción líneas:    336 / 0,20 =  1 680 por punto
    titularización:    3 200 / 0,29 = 11 034 por punto
    cambio de mix:         0 / 0,07 =      0 por punto

  ORDEN CORRECTO DE EJECUCIÓN
    1. cambio de mix (costo cero)
    2. reducción de líneas sin uso (1 680 por punto)
    3. titularización (11 034 por punto)
    4. venta de cartera (11 831 por punto)

  PERO la venta de cartera resuelve TAMBIÉN
  la concentración sectorial, cuyo valor no está
  en el costo por punto de capital

  → se ejecutan 1, 2 y 4
  → la venta se justifica por la doble restricción
```

**Interpreta:** el ejercicio produjo un orden de ejecución **por costo por unidad de restricción
liberada**, que es la métrica correcta y rara vez se calcula. Y la decisión final se apartó de ese orden
por una razón explícita: la venta de cartera resolvía dos restricciones a la vez. Ese es el criterio de
la clase: **optimizar contra la restricción activa, y reconocer cuándo una acción libera más de una**.

## 🏦 Del cliente al banco

El cliente pide una operación y el banco evalúa qué restricción consume. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «El banco vendió mi crédito a otro» | Venta de cartera para liberar capital | 15, clase 6 |
| «Me redujeron la línea que no usaba» | Consumo de capital de lo no utilizado | 15, clase 6 |
| «El banco dejó de prestar a mi sector» | Restricción de concentración | 11, clase 3 |
| «Mi hipotecario cambió de administrador» | Titularización | 15, clase 6 |
| «El banco tiene mucha deuda pública» | Cero consumo de capital ponderado | 15, clase 6 |

## 🧪 Práctica

El laboratorio pide identificar la restricción activa y reordenar una cartera de operaciones. La restricción activa no es el capital, que es lo que la intuición supondría.

En `labs/lab-03.md`, sección de balance:

1. Calcula la holgura de las cinco restricciones e identifica la activa.
2. Construye la tabla de consumo unitario y de retorno por unidad de la restricción activa.
3. Evalúa cinco instrumentos por su costo por unidad de restricción liberada.
4. Determina qué cambio de entorno haría activa otra restricción.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen esfuerzos de optimización que no liberaron nada. La causa es haber optimizado contra una restricción que no estaba activa.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se optimiza el ratio de capital | Puede no ser la restricción activa | Identifícala primero. |
| Se titulariza reteniendo la primera pérdida | Sin transferencia significativa | No libera capital. |
| Se emite AT1 para mejorar CET1 | No computa | Verifica sobre qué ratio es el objetivo. |
| No se calcula el costo por punto liberado | Se elige el instrumento equivocado | Ordena por costo unitario. |
| Se ignoran las líneas no utilizadas | Consumen capital | Revisa las de baja utilización. |
| Se compra liquidez y empeora apalancamiento | Restricciones en conflicto | Evalúa el efecto en todas. |

## ❓ Preguntas de comprobación

1. ¿Por qué optimizar contra la restricción equivocada no mejora nada?
2. ¿Qué determina si una titularización libera capital?
3. ¿Por qué no hay un activo bueno en todas las columnas de consumo?
4. ¿Cuál es la métrica correcta para ordenar instrumentos de gestión del balance?
5. ¿Qué cambio de entorno hace que la liquidez pase a ser la restricción activa?

## 📥 Entregable

Guarda en `portfolio/parte-15/clase-06/`:

- las holguras calculadas y la restricción activa identificada;
- la tabla de consumo unitario y retorno por unidad de restricción;
- los cinco instrumentos ordenados por costo por unidad liberada;
- el análisis de qué cambio de entorno cambia la restricción activa.

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

- Basel Committee on Banking Supervision (2017). *Basel III: Finalising post-crisis reforms*. BIS. Restricciones de capital que condicionan la composición del balance.
- Basel Committee on Banking Supervision (2014). *Revisions to the securitisation framework*. BIS. Titulización como herramienta de gestión de activos ponderados. <https://www.bis.org/bcbs/publ/d303.htm>
- Basel Committee on Banking Supervision (2014). *Basel III leverage ratio framework and disclosure requirements*. BIS. Restricción de apalancamiento sobre el crecimiento del balance. <https://www.bis.org/publ/bcbs270.htm>
- Saunders, A. y Cornett, M. (2021). *Financial Institutions Management: A Risk Management Approach* (10.ª ed.). McGraw-Hill. Gestión de activos y pasivos.
- Choudhry, M. (2018). *An Introduction to Banking: Principles, Strategy and Risk Management* (2.ª ed.). Wiley. Gestión conjunta de activos y pasivos bancarios.
- Verificación local: revisa los requisitos de transferencia significativa de riesgo en titularizaciones y los factores de conversión de partidas fuera de balance en tu jurisdicción.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 05 · Planificación estratégica y de capital](05-planificacion-estrategica-y-de-capital.md) | [Parte 15](../README.md) · [Programa](../../../SYLLABUS.md) | [07 · Política de precios →](07-politica-de-precios.md) |
<!-- gen:footer:end -->
