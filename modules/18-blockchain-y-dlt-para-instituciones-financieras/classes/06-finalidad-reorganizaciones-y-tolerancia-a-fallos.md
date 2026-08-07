<!-- meta
part: 19
class: 6
title: "Finalidad, reorganizaciones y tolerancia a fallos"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global]
regulatory_topics: [dlt, firmeza, riesgo-de-liquidacion]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [CPMI, IOSCO]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 06 · Finalidad, reorganizaciones y tolerancia a fallos

> [← 05 · Mecanismos de consenso](05-mecanismos-de-consenso.md) · [Índice de la parte](../README.md) · [07 · Redes públicas, privadas y autorizadas →](07-redes-publicas-privadas-y-autorizadas.md)

**Parte 19 — Blockchain y DLT para instituciones financieras** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Responder la pregunta que un banco necesita responder antes de usar cualquier
registro distribuido: **¿cuándo puedo tratar esto como definitivo?** Y demostrar
que la respuesta técnica y la jurídica no son la misma.

El consenso de la clase anterior produce acuerdo, y no siempre inmediato. Esta clase precisa cuándo una operación deja de poder revertirse, y distingue tres momentos que se confunden y no coinciden.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** finalidad probabilística, determinística y jurídica.
2. **Calcular** cuántas confirmaciones exige un importe dado para un riesgo
   aceptado.
3. **Explicar** qué es una reorganización y qué la provoca.
4. **Evaluar** si un registro puede dar finalidad en el sentido de las normas de
   sistemas de pago.
5. **Diseñar** la política de aceptación de una institución.

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

Los tres primeros términos son los tipos de finalidad, y son tres cosas distintas; los cinco siguientes, la reorganización y la política que la absorbe. La **finalidad jurídica** es la que decide en un tribunal y no coincide con ninguna de las dos técnicas: un registro puede considerar firme una operación que la norma todavía no.

| Concepto | Comprensión verificable |
|---|---|
| `finalidad probabilística` | La reversión nunca es imposible, solo cada vez menos probable |
| `finalidad determinística` | A partir de un punto, el protocolo garantiza que no revierte |
| `finalidad jurídica` | Momento en que la norma declara la transferencia irrevocable |
| `reorganización` | Sustitución de bloques ya difundidos por una cadena alternativa |
| `profundidad` | Número de bloques posteriores a uno dado |
| `confirmación` | Cada bloque añadido sobre el que contiene la operación |
| `regla de la cadena` | Criterio para elegir entre dos cadenas competidoras |
| `política de aceptación` | Regla propia sobre cuándo tratar algo como definitivo |

## 🧠 Modelo mental

El modelo mental son tres relojes que no marcan la misma hora: el técnico dice cuándo es improbable revertir, el determinístico dice cuándo es imposible y el jurídico dice cuándo es oponible. Una entidad tiene que esperar al tercero.

```text
TRES FINALIDADES QUE NO SON LA MISMA

  TÉCNICA PROBABILÍSTICA
    «con 6 confirmaciones, revertir cuesta X»
    nunca es cero

  TÉCNICA DETERMINÍSTICA
    «cerrada la ronda, el protocolo no revierte»
    es cero, SI el supuesto de seguridad se sostiene

  JURÍDICA
    «la norma declara esta transferencia irrevocable»
    la da la ley, no el software (Parte 18, clase 7)

LAS TRES PUEDEN NO COINCIDIR
  y la que protege a la institución en un concurso
  es la tercera
```

## 📖 Desarrollo

### 1. Finalidad probabilística: cuánto hay que esperar

```text
UN ATACANTE QUE CONTROLA UNA FRACCIÓN q DEL PODER
DE PRODUCCIÓN PUEDE REESCRIBIR LOS ÚLTIMOS BLOQUES

  la probabilidad de conseguir revertir z bloques
  cae de forma exponencial con z, y crece con q

  CON q PEQUEÑO Y z CRECIENTE
    z = 1  probabilidad alta
    z = 3  probabilidad moderada
    z = 6  probabilidad baja
    z = 12 probabilidad muy baja

LA PREGUNTA CORRECTA NO ES «¿CUÁNTAS CONFIRMACIONES?»
ES «¿CUÁNTO ESTOY DISPUESTO A PERDER, Y CUÁNTO
LE CUESTA AL ATACANTE INTENTARLO?»

  para un importe pequeño, 1 confirmación puede bastar:
  el ataque cuesta más que el botín
  para un importe grande, ni 12 bastan si el coste
  del ataque es menor que el importe
```

### 2. Finalidad determinística y su supuesto

```text
UN CONSENSO BIZANTINO DECLARA UN BLOQUE FINAL
CUANDO 2f + 1 DE 3f + 1 LO HAN FIRMADO

  a partir de ahí, revertir exige que f + 1 firmantes
  contradigan su propia firma

  ESO ES DETECTABLE Y ATRIBUIBLE
  → se puede penalizar

PERO LA GARANTÍA ES CONDICIONAL
  «no revierte SI menos de un tercio es defectuoso»

  si el supuesto se rompe, la finalidad determinística
  no es más fuerte que ninguna otra: es CERO

  → por eso la clase 5 insistía en la independencia real
```

### 3. Reorganizaciones: qué las provoca

| Causa | Profundidad típica | ¿Malicia? |
|---|---|---|
| Dos bloques producidos casi a la vez | 1 | No |
| Partición de red temporal | Varios | No |
| Nodo con reloj desajustado | 1–2 | No |
| Defecto en la implementación | Variable | No |
| Ataque con poder de producción | Elegida por el atacante | Sí |

```text
LA MAYORÍA DE LAS REORGANIZACIONES NO SON ATAQUES
  son el funcionamiento normal de un sistema distribuido
  donde dos nodos proponen a la vez

  POR ESO UNA INSTITUCIÓN NO PUEDE TRATAR
  UNA REORGANIZACIÓN COMO UN INCIDENTE DE SEGURIDAD:
  tiene que tratarla como un estado previsto,
  con su procedimiento
```

### 4. Finalidad jurídica: lo que el software no da

```text
LAS NORMAS DE SISTEMAS DE PAGO DEFINEN UN MOMENTO
A PARTIR DEL CUAL UNA TRANSFERENCIA ES IRREVOCABLE
INCLUSO FRENTE A UN PROCEDIMIENTO DE INSOLVENCIA

  esa protección la da la ley aplicable al sistema,
  y suele exigir que el sistema esté DESIGNADO
  o reconocido

UN REGISTRO DISTRIBUIDO NO DESIGNADO
  puede tener finalidad determinística perfecta
  y no tener ninguna protección jurídica

  → si un participante entra en concurso, un
    administrador puede pretender revertir operaciones
    que el protocolo considera definitivas

LA PREGUNTA QUE HAY QUE HACER AL ASESOR JURÍDICO
  «¿este sistema tiene reconocimiento de firmeza
   en las jurisdicciones de todos los participantes?»
  si la respuesta es no, la finalidad técnica
  es una propiedad del software, no una protección
```

### 5. Política de aceptación

```text
UNA POLÍTICA DE ACEPTACIÓN DICE, POR TRAMO DE IMPORTE

  · cuántas confirmaciones se exigen
  · qué se hace mientras tanto (¿se informa? ¿se retiene?)
  · qué se hace si hay reorganización
  · quién autoriza una excepción
  · cómo se comunica al cliente

EJEMPLO DE ESTRUCTURA
  importe        confirmaciones   estado mostrado
  < 1 000            1            «recibido»
  1 000 – 50 000     3            «en confirmación»
  > 50 000          12            «en confirmación»
  cualquiera, con reorganización reciente: +50 %

LO IMPORTANTE NO ES EL NÚMERO: ES QUE EXISTA
LA POLÍTICA, ESTÉ ESCRITA Y SE APLIQUE IGUAL
PARA TODOS
```

## 🧮 Ejemplo guiado

El ejemplo compara los tres momentos sobre la misma operación. La distancia entre ellos es la exposición que alguien está asumiendo.

**Situación.** Un banco acepta liquidaciones sobre una red autorizada con
finalidad determinística. El asesor jurídico pregunta si puede tratarlas como
firmes en su contabilidad y ante un concurso.

```text
LA RED
  consenso bizantino, 7 nodos, f = 2
  finalidad declarada al cerrar la ronda: 3 segundos
  operadores: 7 bancos de 3 jurisdicciones
  reconocimiento como sistema de pagos designado: NO

VOLUMEN
  operaciones al día                          8 400
  importe medio                             620 000
  importe máximo por operación           38 000 000
  saldo medio expuesto durante el día   142 000 000
```

**Paso 1 — separa las tres preguntas.**

```text
1. ¿EL PROTOCOLO REVIERTE?
   con menos de 3 de 7 defectuosos, no.

2. ¿EL SUPUESTO SE SOSTIENE?
   hay que analizar la independencia real (clase 5).

3. ¿LA NORMA PROTEGE?
   la red no está designada → NO hay protección
   específica de firmeza
```

**Paso 2 — evalúa la segunda pregunta.**

```text
7 NODOS, 3 JURISDICCIONES

  ¿cuántos pueden fallar por causa común?
    · 4 de los 7 usan la misma implementación
      (los otros 3 usan una variante)
    · 3 están en la misma jurisdicción

  UN DEFECTO DE LA IMPLEMENTACIÓN MAYORITARIA
  AFECTA A 4 > f = 2  →  el supuesto no se sostiene
  ante ese escenario

  UNA ORDEN JUDICIAL EN LA JURISDICCIÓN CON 3 NODOS
  afecta a 3 > f = 2  →  tampoco
```

**Paso 3 — cuantifica la exposición.**

```text
SALDO MEDIO EXPUESTO INTRADÍA: 142 000 000

  si la finalidad no es oponible en un concurso,
  ese importe está en riesgo de reversión
  ante la insolvencia de un participante

  la probabilidad es baja; la severidad es total
```

**Paso 4 — busca lo que sí se puede hacer.**

```text
OPCIÓN A · solicitar la designación del sistema
  requiere cumplir requisitos de infraestructura
  de mercado y obtener reconocimiento en las
  tres jurisdicciones
  plazo estimado: 18 a 30 meses
  coste estimado: alto, y no depende solo del banco

OPCIÓN B · liquidar en un sistema designado
  el registro distribuido lleva la instrucción
  y la liquidación ocurre en el sistema nacional
  → la firmeza la da el sistema designado
  → se pierde la atomicidad entre las dos patas

OPCIÓN C · reducir la exposición intradía
  liquidar en ciclos más frecuentes contra el
  sistema designado
  → menos importe expuesto, más operaciones

OPCIÓN D · garantías entre participantes
  cada participante aporta garantía que cubre
  su exposición máxima
  → protección contractual, no legal;
    sigue sujeta al concurso
```

**Paso 5 — evalúa la opción C con números.**

```text
CON UN CICLO DIARIO
  exposición media: 142 000 000

CON CUATRO CICLOS AL DÍA
  exposición media ≈ 142 000 000 / 4 = 35 500 000
  coste adicional: 3 liquidaciones más al día
  en el sistema designado
  supuesto: 4 200 por liquidación × 3 × 250 días
  = 3 150 000 al año

CON OCHO CICLOS
  exposición ≈ 17 750 000
  coste: 7 350 000 al año

REDUCCIÓN DE EXPOSICIÓN POR UNIDAD DE COSTE
  de 1 a 4 ciclos: −106,5 M por 3,15 M  → 33,8 : 1
  de 4 a 8 ciclos: −17,75 M por 4,20 M  →  4,2 : 1

  el rendimiento decrece rápido: 4 ciclos es
  el punto donde deja de compensar claramente
```

**Paso 6 — decide.**

```text
DECISIÓN COMBINADA

  1. CUATRO CICLOS DIARIOS contra el sistema designado
     reduce la exposición de 142 M a 35,5 M por 3,15 M/año

  2. POLÍTICA DE ACEPTACIÓN ESCRITA
     el registro se trata como firme ENTRE PARTICIPANTES
     y como no firme frente a terceros hasta la
     liquidación en el sistema designado

  3. CONTABILIDAD
     las operaciones no liquidadas se reconocen como
     exposición con la contraparte, no como liquidadas
     → esto es lo que el asesor preguntaba, y la
       respuesta es NO

  4. INICIAR LA CONSULTA DE DESIGNACIÓN
     18 a 30 meses es largo, y el reloj empieza cuando
     alguien lo arranca

  5. CORREGIR LA CORRELACIÓN
     la implementación mayoritaria en 4 de 7 nodos
     rompe el supuesto; es un hallazgo para el consorcio
```

**Paso 7 — escribe la respuesta al asesor.**

```text
«La red tiene finalidad determinística en el sentido del
protocolo: cerrada la ronda, ningún participante honesto
la revierte.

Eso NO permite tratar las operaciones como firmes a
efectos contables ni de concurso, por dos razones:

  1. el supuesto de seguridad no se sostiene ante un
     defecto de la implementación mayoritaria (4 de 7)
     ni ante una orden judicial en la jurisdicción
     con 3 nodos;
  2. el sistema no está designado, de modo que no le
     aplica la protección de firmeza.

Hasta que ambas cosas cambien, las operaciones se
reconocen como exposición con la contraparte y la
liquidación firme se produce en el sistema designado,
en cuatro ciclos diarios.»
```

**Interpreta:** la red tenía la mejor finalidad técnica disponible y **eso no
respondía la pregunta**. La firmeza que protege a un banco en un concurso la da
la norma, y el trabajo útil consistió en reducir la exposición mientras esa
protección no exista.

## 🧭 Perspectivas

La finalidad significa cosas distintas para cada participante. La tabla las recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | «Confirmado en 3 segundos» | Si dispone |
| Banco | 142 M expuestos intradía | Cuántos ciclos liquida |
| Contabilidad | ¿Liquidado o exposición? | Cómo lo reconoce |
| Asesor jurídico | Sistema no designado | Qué recomienda |
| Consorcio | Correlación de implementación | Si diversifica |
| Supervisor | Un sistema no designado con volumen | Si exige designación |
| Administrador concursal | Operaciones «finales» | Si las impugna |

## 🏦 Del cliente al banco

El cliente ve una operación confirmada y el banco espera a la finalidad jurídica. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Ya está confirmado» | Firme entre participantes, no frente a terceros | 19, clase 6 |
| «Se deshizo una operación» | Reorganización: estado previsto, no incidente | 19, clase 6 |
| «Tarda más si el importe es alto» | Política de aceptación por tramo | 19, clase 6 |

## ⚖️ Riesgos y controles

Los riesgos son de reorganización y de finalidad no oponible. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Confundir finalidad técnica con jurídica | Se contabiliza como liquidado | Reconocer exposición hasta la firmeza |
| Supuesto de seguridad roto | Correlación por implementación | Diversidad o riesgo declarado |
| Exposición intradía | Un ciclo diario acumula | Más ciclos contra sistema designado |
| Reorganización tratada como incidente | Se para todo cada vez | Procedimiento previsto |
| Política de aceptación inexistente | Cada caso se decide distinto | Escrita, por tramo, igual para todos |
| Sistema sin designación | Sin protección de firmeza | Iniciar la consulta y declarar el riesgo |

## 🧪 Práctica

En [`labs/lab-04.md`](../labs/lab-04.md) y el [proyecto](../project/README.md):

1. Calcula las confirmaciones necesarias para tres importes y un riesgo dado.
2. Simula una reorganización y comprueba qué operaciones se deshacen.
3. Escribe una política de aceptación por tramos.
4. Analiza si el supuesto de seguridad de tu red se sostiene.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen operaciones revertidas o no oponibles. La causa es haber confundido los tres tipos de finalidad.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| «Determinística, luego firme» | Se ignoró la finalidad jurídica | La da la norma |
| Número fijo de confirmaciones | No se relacionó con el importe | Política por tramos |
| Reorganización como alarma | Se trató como ataque | Es funcionamiento normal |
| Supuesto no verificado | Se confió en el número de nodos | Analiza la independencia |
| Exposición intradía no medida | Se miró la operación, no el saldo | Mide el acumulado |
| Contabilizar como liquidado | Se siguió al software | Reconoce exposición |

## ❓ Preguntas de comprobación

1. ¿Cuáles son las tres finalidades y cuál protege en un concurso?
2. ¿Por qué la pregunta correcta no es «cuántas confirmaciones»?
3. ¿Qué condición hace que la finalidad determinística valga cero?
4. ¿Por qué una reorganización no es necesariamente un ataque?
5. En el ejemplo guiado, ¿por qué la respuesta al asesor fue «no»?

## 📥 Entregable

Guarda en `portfolio/parte-19/clase-06/`:

- el cálculo de confirmaciones para tres importes, con el riesgo aceptado;
- el análisis del supuesto de seguridad de una red concreta;
- tu política de aceptación por tramos;
- la respuesta escrita a la pregunta «¿podemos contabilizarlo como firme?».

## 🔗 Referencias cruzadas

- **Viene de:** clases 4 y 5; Parte 18, clase 7 (finalidad).
- **Continúa en:** clase 7 (tipos de red), clase 13 (recuperación).
- **Se aplica en:** Parte 21, clase 15; Parte 22, clase 7; Parte 23, clase 14.

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

- Committee on Payments and Market Infrastructures e IOSCO (2012). *Principles for Financial Market Infrastructures*, principio 8 sobre firmeza de la liquidación. BIS. <https://www.bis.org/cpmi/publ/d101.htm>
- Committee on Payments and Market Infrastructures (2017). *Distributed ledger technology in payment, clearing and settlement*. BIS. <https://www.bis.org/cpmi/publ/d157.htm>
- Parlamento Europeo y Consejo. *Directiva 98/26/CE sobre firmeza de la liquidación en los sistemas de pagos y de liquidación de valores*. <https://eur-lex.europa.eu/eli/dir/1998/26/oj>
- IOSCO (2022). *Decentralized Finance Report*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD699.pdf>
- NIST (2018). *NISTIR 8202: Blockchain Technology Overview*. NIST. <https://csrc.nist.gov/pubs/ir/8202/final>
- Verificación local: comprueba qué norma otorga firmeza en tu jurisdicción, qué requisitos exige para designar un sistema y si el reconocimiento es mutuo entre las jurisdicciones de todos los participantes. **Fecha de verificación de esta clase: 2026-08-06.** Esta clase no constituye asesoría legal.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 05 · Mecanismos de consenso](05-mecanismos-de-consenso.md) | [Parte 19](../README.md) · [Programa](../../../SYLLABUS.md) | [07 · Redes públicas, privadas y autorizadas →](07-redes-publicas-privadas-y-autorizadas.md) |
<!-- gen:footer:end -->
