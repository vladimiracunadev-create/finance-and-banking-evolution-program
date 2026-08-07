<!-- meta
part: 16
class: 15
title: "Prueba de estrés del banco"
level: profesional
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 15 · Prueba de estrés del banco

> [← 14 · Cuadro de mando del banco](14-cuadro-de-mando-del-banco.md) · [Índice de la parte](../README.md) · [16 · Simulación de un ciclo →](16-simulacion-de-un-ciclo.md)

**Parte 16 — Proyecto Banco Virtual** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Someter el Banco Austral a un escenario adverso y determinar si sobrevive. Catorce clases lo
construyeron en condiciones normales; esta clase responde la única pregunta que importa sobre un banco:
**¿qué le pasa cuando el entorno se deteriora?**

El banco construido hasta aquí funciona en condiciones normales. Esta clase lo somete a las que no lo son, aplicando la Parte 11. Y con la misma exigencia: el escenario tiene que ser lo bastante severo como para romper alguna métrica, porque un escenario que el banco aguanta con holgura no informa de nada.

## 📚 Objetivos

Al finalizar podrás:

1. **Diseñar** un escenario adverso coherente para el modelo del banco.
2. **Traducir** las variables macro a parámetros de riesgo por cartera.
3. **Proyectar** resultado, capital y liquidez en el escenario.
4. **Ejecutar** una prueba inversa y localizar el punto de quiebre.
5. **Derivar** las decisiones que la prueba exige.

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

Los cuatro primeros términos son el escenario y su traducción; los cuatro siguientes, el resultado y su respuesta. La **vulnerabilidad específica** es lo que distingue una prueba útil de un ejercicio: el escenario ataca donde este banco es débil, no donde lo sería cualquiera.

| Concepto | Comprensión verificable |
|---|---|
| `escenario adverso` | Deterioro severo pero plausible del entorno. |
| `coherencia interna` | Que las variables se muevan de forma compatible. |
| `función de traducción` | Relación entre variables macro y parámetros de riesgo. |
| `vulnerabilidad específica` | La que depende del modelo propio, no del entorno. |
| `punto de quiebre` | Escenario que produce el resultado intolerable. |
| `acción de gestión` | Respuesta creíble durante el escenario. |
| `holgura mínima` | Distancia menor al requerimiento durante el horizonte. |
| `prueba inversa` | Se parte del resultado y se busca qué lo produce. |

## 🧠 Modelo mental

El modelo mental es una vulnerabilidad específica: el escenario no se elige de un catálogo genérico sino que se diseña contra las debilidades concretas de este banco, que son su dependencia mayorista y la concentración de su segmento.

```text
UN BANCO NUEVO TIENE DOS VULNERABILIDADES
QUE UN BANCO ESTABLECIDO NO TIENE

  1. CARTERA JOVEN
     la mora madura entre los meses 12 y 30
     un escenario adverso en el año 3
     encuentra la cartera en su peor momento

  2. DEPENDENCIA MAYORISTA DEL 74 %
     el mercado deja de prestarle
     antes que a un banco establecido

  Y AMBAS SE MATERIALIZAN A LA VEZ
    porque el escenario que deteriora la cartera
    es el que cierra el mercado
```

## 📖 Desarrollo

### 1. Diseño del escenario

El escenario se diseña desde las vulnerabilidades específicas del banco. El procedimiento lo estructura.

```text
ESCENARIO ADVERSO A 3 AÑOS

  año 1
    producto interno bruto            −3,8 %
    desempleo                         +3,2 pp
    inflación                         +4,4 pp
    tasa de política                  +320 pb
    tipo de cambio                    −18 %
    ventas del comercio minorista     −11 %
    diferencial de emisión bancaria   +240 pb

  año 2
    producto                          −1,4 %
    desempleo                         +4,8 pp
    tasa de política                  +80 pb
    ventas del comercio               −16 % acumulado

  año 3
    producto                          +0,6 %
    desempleo                         +4,1 pp
    tasa de política                  −140 pb
    ventas del comercio               −12 % acumulado
```

```text
VERIFICACIÓN DE COHERENCIA
  producto cae → desempleo sube con rezago  ✓
  depreciación → inflación → tasa sube      ✓
  desempleo alto → ventas del comercio caen ✓
  tasa alta → diferencial de emisión sube   ✓
  año 3: producto se recupera, desempleo aún alto  ✓
```

### 2. Traducción a parámetros

El escenario macroeconómico se traduce a parámetros de riesgo. El procedimiento lo hace.

```text
P2 — PERSONAS SIN HISTORIAL
  el segmento depende del EMPLEO y del INGRESO REAL
  elasticidad estimada: +1 pp de desempleo → PD × 1,38
  y el ingreso real cae con la inflación

  PD base: 6,84 %
  año 1: 6,84 % × 1,38^3,2 = 6,84 % × 2,53 = 17,31 %
  año 2: 6,84 % × 1,38^4,8 = 6,84 % × 4,03 = 27,57 %
  año 3: 6,84 % × 1,38^4,1 = 6,84 % × 3,26 = 22,30 %

E2 — PEQUEÑA EMPRESA
  el segmento depende de las VENTAS
  elasticidad: −1 % de ventas → PD × 1,09

  PD base: 4,20 %
  año 1: 4,20 % × 1,09^11 = 4,20 % × 2,58 = 10,84 %
  año 2: 4,20 % × 1,09^16 = 4,20 % × 3,97 = 16,67 %
  año 3: 4,20 % × 1,09^12 = 4,20 % × 2,81 = 11,80 %
```

```text
LGD EN ESTRÉS
  P2 (sin garantía): la recuperación cae
    de 46 % a 34 % → LGD de 69,2 % a 78,4 %
  E2 (con cesión de flujo): la cesión vale menos
    porque las ventas caen
    recuperación de 45 % a 31 % → LGD de 46,3 % a 58,7 %
```

### 3. Efecto sobre el negocio

El escenario afecta a volumen, margen y pérdida a la vez. El procedimiento lo proyecta.

```text
VOLUMEN
  la demanda de crédito cae y el banco endurece
  crecimiento de cartera: +32 % base → −8 % año 1, −4 % año 2

MARGEN
  el costo de fondos sube 240 pb (diferencial)
  la tasa activa no puede subir lo mismo:
    tasa máxima convencional y capacidad de pago
  compresión del margen: −140 pb

COMISIONES
  el volumen recaudado cae con las ventas: −16 %
  comisiones: −18 %

GASTOS
  rígidos en el corto plazo: −2 % año 1, −6 % año 2
```

### 4. Efecto sobre la liquidez

El efecto sobre la liquidez suele ser el que rompe primero en un banco nuevo. El procedimiento lo calcula.

```text
EL ESCENARIO CIERRA EL MERCADO MAYORISTA

  supuesto: no se renueva el interbancario (111 136)
  y las emisiones que vencen no se refinancian

  salida de depósitos por la señal: 22 %
    81 920 × 22 % = 18 022

  NECESIDAD DE LIQUIDEZ AÑO 1: 129 158
  RECURSOS
    activos líquidos: 120 030
    colateral preparado: 83 460
    TOTAL: 203 490

  ¿SE CUBRE? sí, con 74 332 de holgura
  PERO se consume el 63 % de la capacidad
```

### 5. Acciones de gestión

Las acciones supuestas tienen que ser creíbles y ejecutables en el escenario. La tabla recoge los criterios.

| Acción | Efecto | Viabilidad en estrés |
|---|---|---|
| Suspensión de dividendos | Ya suspendidos | — |
| Freno a la originación | Reduce activos ponderados | Alta |
| Uso del colateral preparado | Liquidez | Alta |
| Captación de depósito a plazo con prima | Financiamiento | Media |
| Reducción de gastos discrecionales | Resultado | Alta |
| Aporte de los accionistas | Capital | Media (comprometido hasta 12 000) |
| Venta de cartera | Capital y liquidez | Baja en estrés |

```text
EL COMPROMISO DE APORTE DE LOS ACCIONISTAS (clase 3)
ES LA ACCIÓN DECISIVA

  y su viabilidad depende de que los accionistas
  puedan aportar en el mismo escenario
  que los está afectando a ellos
  → por eso el supervisor verifica su solvencia
```

## 🧮 Ejemplo guiado

El ejemplo somete al Banco Austral a un escenario diseñado contra su vulnerabilidad. Conviene identificar qué métrica rompe primero: es la que hay que reforzar.

**Situación.** Ejecutar la prueba de estrés completa del Banco Austral.

**Paso 1 — proyecta el costo de riesgo.**

```text
AÑO 1
  P2: cartera 108 604 (tras −8 %)
      PD 17,31 %, LGD 78,4 %
      pérdida esperada: 14 738
  E2: EAD 226 000, PD 10,84 %, LGD 58,7 %
      pérdida esperada: 14 380
  E3: 3 600 × 0,9 % × 45 % = 15
  COSTO DE RIESGO AÑO 1: 29 133

AÑO 2
  P2: cartera 104 260, PD 27,57 %, LGD 78,4 %
      pérdida: 22 536
  E2: EAD 216 960, PD 16,67 %, LGD 58,7 %
      pérdida: 21 231
  COSTO DE RIESGO AÑO 2: 43 782

AÑO 3
  P2: PD 22,30 %, pérdida: 18 227
  E2: PD 11,80 %, pérdida: 15 030
  COSTO DE RIESGO AÑO 3: 33 272
```

**Paso 2 — proyecta el resultado.**

```text
                            año 1     año 2     año 3
  margen financiero        38 275    35 420    36 890
  comisiones                10 203     9 320     9 954
  MARGEN BRUTO             48 478    44 740    46 844
  gastos                  −23 039   −22 099   −22 320
  RESULTADO ANTES DE PROV. 25 439    22 641    24 524
  costo de riesgo         −29 133   −43 782   −33 272
  RESULTADO ANTES DE IMP.  −3 694   −21 141    −8 748
  impuesto (sin recupero)       0         0         0
  RESULTADO NETO           −3 694   −21 141    −8 748

  PÉRDIDA ACUMULADA A 3 AÑOS: −33 583
```

**Paso 3 — proyecta el capital.**

```text
  capital inicial (año 3 base):        55 575
  año 1: 55 575 − 3 694 =              51 881
  año 2: 51 881 − 21 141 =             30 740
  año 3: 30 740 − 8 748 =              21 992

  ACTIVOS PONDERADOS
    año 1: 311 725 × 0,92 = 286 787
      + migración de calificación (+9 %) = 312 598
    año 2: 300 094 + migración (+14 %) = 342 107
    año 3: 288 090 + migración (+11 %) = 319 780

  RATIO CET1
    año 1: 51 881 / 312 598 = 16,60 %
    año 2: 30 740 / 342 107 =  8,99 %
    año 3: 21 992 / 319 780 =  6,88 %

  REQUERIMIENTO TOTAL: 11,34 %

  EL BANCO INCUMPLE EN EL AÑO 2
  Y ESTÁ MUY POR DEBAJO EN EL AÑO 3
```

**Paso 4 — evalúa la magnitud del déficit.**

```text
AÑO 2
  capital necesario: 11,34 % × 342 107 = 38 795
  capital disponible: 30 740
  DÉFICIT: 8 055

AÑO 3
  capital necesario: 11,34 % × 319 780 = 36 263
  capital disponible: 21 992
  DÉFICIT: 14 271

  Y PARA VOLVER AL OBJETIVO INTERNO DEL 14 %
    año 3: 44 769 − 21 992 = 22 777
```

**Paso 5 — aplica las acciones de gestión.**

```text
ACCIÓN 1 — FRENO TOTAL A LA ORIGINACIÓN DESDE EL AÑO 1
  la cartera se reduce por amortización natural
  año 2: cartera 248 000 en lugar de 321 220
  activos ponderados año 2: 264 100
  → el ratio del año 2: 30 740 / 264 100 = 11,64 %  ✓ apenas

ACCIÓN 2 — APORTE DE LOS ACCIONISTAS
  compromiso: hasta 12 000
  aporte en el año 2: 12 000
  capital año 2: 42 740
  ratio: 42 740 / 264 100 = 16,18 %  ✓
  capital año 3: 33 992
  activos ponderados año 3: 241 500
  ratio: 14,08 %  ✓ sobre el objetivo interno

ACCIÓN 3 — REDUCCIÓN DE GASTOS DISCRECIONALES
  marketing, proyectos no críticos, formación externa
  ahorro: 2 800 anuales durante 2 años
  reduce la pérdida acumulada en 5 600
  capital año 3: 39 592
  ratio: 16,39 %
```

**Paso 6 — evalúa la viabilidad de las acciones.**

```text
ACCIÓN 1 — freno a la originación
  · viable operativamente: sí
  · consecuencia: el banco deja de crecer
    y su base de clientes se erosiona
  · consecuencia sobre el modelo: los clientes
    del escalonamiento no ascienden
    → se pierde el mecanismo central del negocio
  → viable, con daño estratégico

ACCIÓN 2 — aporte de los accionistas
  · el accionista A es un grupo empresarial local
    que en este escenario también está afectado
  · el accionista B es un fondo regional,
    menos correlacionado con el escenario local
  · el compromiso es contractual
  → viable, con probabilidad estimada del 70 %

  ¿Y SI NO APORTAN?
    ratio año 2 sin aporte: 11,64 %
    ratio año 3 sin aporte: 24 992/241 500 = 10,35 %
    → INCUMPLIMIENTO en el año 3
```

**Paso 7 — ejecuta la prueba inversa.**

```text
¿QUÉ ESCENARIO LLEVA AL BANCO AL INCUMPLIMIENTO
INCLUSO CON TODAS LAS ACCIONES?

  con freno total, aporte de 12 000 y ahorro de gastos:
  capital año 3: 39 592, activos ponderados 241 500
  ratio: 16,39 %

  para llegar al 11,34 %:
    capital necesario: 27 386
    pérdida adicional admisible: 12 206

  ¿QUÉ PRODUCIRÍA 12 206 DE PÉRDIDA ADICIONAL?
    un costo de riesgo 14 % mayor en los tres años
    → PD de P2 al 31,4 % en el año 2
    → equivale a un desempleo de +5,6 pp

  EL ESCENARIO ADVERSO TIENE +4,8 pp
  EL PUNTO DE QUIEBRE ESTÁ EN +5,6 pp
  DISTANCIA: 0,8 puntos de desempleo

  → el margen es ESTRECHO
```

**Paso 8 — deriva las decisiones.**

```text
LO QUE LA PRUEBA EXIGE CAMBIAR

  1. CAPITAL INICIAL INSUFICIENTE
     con 46 000 el banco no resiste el escenario
     sin aporte adicional
     → elevar el capital inicial a 56 000
       o formalizar el compromiso de aporte
       con garantía verificable

  2. CONCENTRACIÓN EN DOS SEGMENTOS CÍCLICOS
     ambos segmentos se deterioran con el mismo ciclo
     correlación entre P2 y E2 en estrés: 0,82
     → el capital económico de la clase 12
       la subestimó
     → recalcular con correlación de 0,80,
       no la implícita en la agregación

  3. EL ESCALONAMIENTO ES PROCÍCLICO
     en el escenario, los clientes no ascienden
     y el monto medio de la cartera cae
     → el modelo de negocio pierde su motor
       exactamente cuando más lo necesita
     → diseñar un mecanismo de ascenso
       que no dependa solo del ciclo

  4. DEPENDENCIA MAYORISTA
     el plan de la clase 11 (bajar a 55 % en 24 meses)
     pasa de ser deseable a ser NECESARIO
     → acelerarlo a 18 meses

  5. LÍMITE DE CRECIMIENTO
     el banco creció 32 % anual en el plan base
     ese crecimiento produjo la cartera joven
     que el escenario encuentra en su peor momento
     → limitar el crecimiento al 24 % anual
       reduce la vulnerabilidad y el resultado

  6. OBJETIVO INTERNO DE CAPITAL
     el 14 % no basta
     → elevarlo a 16,5 %, que es el nivel
       que mantiene el escenario sobre el requerimiento
       sin depender del aporte de los accionistas
```

**Interpreta:** el Banco Austral **incumple su requerimiento de capital en el año 2 del escenario
adverso** y solo sobrevive con el freno total a la originación y el aporte comprometido de los
accionistas. La prueba reveló algo que catorce clases de diseño no habían mostrado: **el escalonamiento,
que es el mecanismo central del modelo, es procíclico**, y deja de funcionar precisamente cuando el banco
más lo necesita. Ese hallazgo vale más que la cifra del ratio.

## 🏦 Del cliente al banco

El cliente no ve nada de esto y el banco comprueba si sobreviviría a una recesión. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «El banco dejó de dar créditos» | Freno a la originación en estrés | 16, clase 15 |
| «No pude subir de escalón» | El mecanismo es procíclico | 16, clase 15 |
| «Los dueños pusieron más capital» | Compromiso de apoyo ejecutado | 16, clase 3 |
| «Mi banco resistió la recesión» | Prueba de estrés que cambió el diseño | 11, clase 13 |
| «Endurecieron todo de golpe» | Acciones de gestión activadas | 15, clase 5 |

## 🧪 Práctica

El laboratorio pide diseñar el escenario y proyectar el efecto. El escenario tiene que romper algo: si no, hay que endurecerlo.

En `labs/lab-06.md`, sección de estrés:

1. Diseña el escenario adverso y verifica su coherencia interna.
2. Traduce las variables macro a parámetros por cartera con sus elasticidades.
3. Proyecta resultado, capital y liquidez con y sin acciones de gestión.
4. Ejecuta la prueba inversa y deriva las decisiones que exige.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen pruebas de estrés que no informan. Las causas son escenarios genéricos y acciones de gestión no creíbles.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se proyecta solo el costo de riesgo | Falta el margen y las comisiones | Proyecta todo el resultado. |
| LGD constante en estrés | La recuperación cae | Estrésala también. |
| Acciones de gestión heroicas | No viables en el escenario | Solo las ejecutables. |
| Se supone el aporte de accionistas | Puede no ocurrir | Proyecta también sin él. |
| Correlación entre segmentos ignorada | Se deterioran juntos | Estímala en estrés. |
| Prueba que solo produce un ratio | Se pierde el hallazgo | Busca la vulnerabilidad del modelo. |

## ❓ Preguntas de comprobación

1. ¿Cuáles son las dos vulnerabilidades específicas de un banco nuevo?
2. ¿Por qué la LGD también debe estresarse?
3. ¿Qué significa que el escalonamiento sea procíclico?
4. ¿Qué distancia hay entre el escenario adverso y el punto de quiebre?
5. ¿Por qué el hallazgo sobre el escalonamiento vale más que el ratio?

## 📥 Entregable

Guarda en `portfolio/parte-16/clase-15/`:

- el escenario adverso con su verificación de coherencia;
- la traducción a parámetros con sus elasticidades;
- la proyección completa con y sin acciones de gestión;
- la prueba inversa y las seis decisiones derivadas.

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

- Basel Committee on Banking Supervision (2018). *Stress testing principles*. BIS.
- European Banking Authority. *EU-wide stress test methodology*. EBA.
- International Monetary Fund (2012). *Macrofinancial Stress Testing: Principles and Practices*. IMF.
- Basel Committee on Banking Supervision (2015). *Guidance on credit risk and accounting for expected credit losses*. BIS.
- Hull, J. (2018). *Risk Management and Financial Institutions* (5.ª ed.). Wiley.
- Verificación local: revisa el escenario adverso publicado por tu supervisor y sus variables, y aplícalo a tu proyecto.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 14 · Cuadro de mando del banco](14-cuadro-de-mando-del-banco.md) | [Parte 16](../README.md) · [Programa](../../../SYLLABUS.md) | [16 · Simulación de un ciclo →](16-simulacion-de-un-ciclo.md) |
<!-- gen:footer:end -->
