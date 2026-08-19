<!-- meta
part: 19
class: 5
title: "Mecanismos de consenso"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global]
regulatory_topics: [dlt, infraestructura, riesgo-operacional]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [CPMI, NIST]
requires_legal_review: false
-->

<!-- gen:header:start -->
# Clase 05 · Mecanismos de consenso

> [← 04 · Transacciones, bloques, nodos y estado](04-transacciones-bloques-nodos-y-estado.md) · [Índice de la parte](../README.md) · [06 · Finalidad, reorganizaciones y tolerancia a fallos →](06-finalidad-reorganizaciones-y-tolerancia-a-fallos.md)

**Parte 19 — Blockchain y DLT para instituciones financieras** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Entender qué problema resuelve un mecanismo de consenso —**quién decide el
orden**— y comparar las familias por lo que cuestan y por lo que garantizan, no
por lo que prometen.

La clase anterior deja abierta la pregunta de quién ordena las transacciones. Esta la responde, y compara las familias de mecanismos por lo único que las hace comparables: cuánto cuesta atacarlas.

## 📚 Objetivos

Al finalizar podrás:

1. **Formular** el problema del consenso en una frase operativa.
2. **Comparar** las tres familias por coste, finalidad, escala y supuesto de
   seguridad.
3. **Calcular** el umbral de tolerancia de un consenso bizantino y su coste en
   mensajes.
4. **Identificar** de qué depende la seguridad de cada familia y cuándo deja de
   sostenerse.
5. **Elegir** el mecanismo de una red financiera con criterios explícitos.

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

Los cuatro primeros términos son las familias de consenso; los cuatro siguientes, sus parámetros y su economía. El **coste de ataque** es la medida que permite comparar mecanismos que parecen incomparables: cuánto cuesta reescribir la historia, y si ese coste supera al valor que protege.

| Concepto | Comprensión verificable |
|---|---|
| `consenso` | Acuerdo sobre el orden de las operaciones entre nodos que no confían |
| `prueba de trabajo` | Derecho a proponer que se gana gastando cómputo |
| `prueba de participación` | Derecho que se gana comprometiendo capital |
| `consenso bizantino` | Acuerdo por votación entre participantes conocidos |
| `productor de bloques` | Nodo que propone el siguiente bloque |
| `umbral de tolerancia` | Fracción de nodos defectuosos que el sistema soporta |
| `coste de ataque` | Lo que cuesta imponer un orden distinto |
| `liveness` | Propiedad de seguir progresando |

## 🧠 Modelo mental

El modelo mental es un acuerdo caro por diseño: el consenso hace que mentir cueste más que decir la verdad. Cada mecanismo elige una forma distinta de imponer ese coste, y de ahí salen sus propiedades.

```text
EL CONSENSO NO DECIDE SI UNA TRANSACCIÓN ES VÁLIDA:
ESO LO DECIDE CADA NODO POR SÍ MISMO

  EL CONSENSO DECIDE EL ORDEN
  y con el orden, cuál de dos gastos del mismo saldo vale

TODAS LAS FAMILIAS RESUELVEN LO MISMO Y SE DIFERENCIAN EN
  · quién tiene derecho a proponer
  · qué cuesta obtener ese derecho
  · qué pasa si el que propone miente
  · cuándo se puede considerar irreversible

Y EN UNA PROPIEDAD QUE SE OLVIDA
  SEGURIDAD  no ocurren dos historias incompatibles
  PROGRESO   el sistema sigue avanzando

  ante una partición hay que sacrificar una de las dos.
  En finanzas se sacrifica el progreso (clase 1).
```

## 📖 Desarrollo

### 1. Las tres familias

| | Prueba de trabajo | Prueba de participación | Bizantino entre conocidos |
|---|---|---|---|
| Participantes | Abiertos, anónimos | Abiertos con capital | Conocidos y autorizados |
| Derecho a proponer | Cómputo gastado | Capital comprometido | Turno o votación |
| Coste continuo | Energía | Coste de oportunidad | Infraestructura |
| Finalidad | Probabilística | Casi determinística | Determinística |
| Escala de nodos | Miles | Miles | Decenas |
| Rendimiento | Bajo | Medio | Alto |
| Supuesto de seguridad | Mayoría del cómputo honesta | Mayoría del capital honesta | Menos de 1/3 defectuosos |
| Coste de ataque | Adquirir cómputo | Adquirir capital | Coludir con conocidos |

En un consorcio financiero hay una fila que decide la elección antes de mirar
las demás.

```text
LA FILA QUE DECIDE EN UN CONSORCIO FINANCIERO
  «participantes»

  si son conocidos y autorizados —y en un consorcio
  bancario lo son— gastar energía o inmovilizar capital
  para decidir el orden es pagar por una propiedad
  que ya se tiene
```

### 2. El umbral bizantino y por qué es un tercio

La cifra de un tercio no es una convención: se deduce de contar cuántas
respuestas hacen falta para que las honestas sean mayoría. El bloque hace la
deducción y la aplica a dos tamaños de red.

```text
CON n NODOS Y f DEFECTUOSOS

  para decidir hace falta esperar respuestas de n − f
  (los f defectuosos pueden no responder)

  de esas n − f, hasta f pueden ser mentiras

  para que las honestas sean mayoría en cualquier
  quórum: n − f − f > f  →  n > 3f

  → n ≥ 3f + 1

CON 4 NODOS SE TOLERA 1 DEFECTUOSO
CON 7, SE TOLERAN 2
CON 10, SE TOLERAN 3

LA CUENTA QUE HAY QUE HACER EN UN CONSORCIO
  cinco bancos → n = 5 → f = 1
  un solo participante defectuoso, y el sistema aguanta
  dos, y se detiene
```

### 3. El coste en mensajes

El coste de un consenso bizantino clásico crece con el cuadrado del número de
participantes, y eso decide dónde se puede usar. El bloque pone las cifras y
extrae la frontera práctica entre red abierta y consorcio.

```text
UN PROTOCOLO BIZANTINO CLÁSICO INTERCAMBIA
MENSAJES EN CADA RONDA

  cada nodo habla con todos: O(n²) mensajes por ronda

  CON n = 5:   25 mensajes por ronda
  CON n = 20:  400
  CON n = 100: 10 000

POR ESO NO ESCALA A MILES DE NODOS
  y por eso las redes abiertas usan otra familia

EN UN CONSORCIO DE 5 A 20 PARTICIPANTES
  O(n²) es perfectamente manejable
  → el «no escala» que se le reprocha
    es irrelevante para este caso de uso
```

### 4. De qué depende la seguridad de cada familia

Cada familia de consenso apoya su seguridad en un supuesto económico distinto,
y conviene saber cuál es para saber cuándo deja de sostenerse. El bloque los
enuncia uno a uno con la condición que los rompe.

```text
PRUEBA DE TRABAJO
  seguridad = coste de adquirir más cómputo que el resto
  DEJA DE SOSTENERSE si el cómputo se concentra
  o si la red es pequeña: una red con poco cómputo
  se ataca barato

PRUEBA DE PARTICIPACIÓN
  seguridad = coste de adquirir capital + penalización
  DEJA DE SOSTENERSE si el capital se concentra
  o si la penalización no cubre el beneficio del ataque

BIZANTINO ENTRE CONOCIDOS
  seguridad = dificultad de que f + 1 participantes
  conocidos se pongan de acuerdo para mentir
  DEJA DE SOSTENERSE si los participantes tienen
  el mismo dueño, el mismo proveedor o el mismo interés

  → es exactamente el problema de correlación
    de la clase 3: contar nodos no es contar
    independencias
```

### 5. Quién ordena y por qué importa

Quien produce un bloque decide qué entra y en qué orden, y eso es poder
económico en cualquiera de las tres familias. El bloque describe lo que puede
hacer y los controles que lo acotan.

```text
EL PRODUCTOR DE UN BLOQUE ELIGE QUÉ INCLUIR
Y EN QUÉ ORDEN

  PUEDE
    · retrasar una operación
    · adelantar la suya
    · excluir a un participante

  ESO ES PODER ECONÓMICO, y existe en las tres familias

CONTROLES POSIBLES
  · rotación obligatoria del productor
  · reglas de ordenación verificables (por ejemplo,
    por orden de llegada firmado)
  · penalización por censura demostrada
  · umbral de inclusión: una operación que lleva k bloques
    pendiente debe incluirse

NINGUNO ES AUTOMÁTICO: HAY QUE DISEÑARLOS
```

## 🧮 Ejemplo guiado

El ejemplo calcula el coste de atacar dos mecanismos distintos. Conviene compararlo con el valor asegurado: si el coste es menor, el mecanismo no protege lo suficiente.

**Situación.** El consorcio de cinco bancos de la clase 4 debe elegir mecanismo
de consenso y justificarlo.

```text
PARTICIPANTES
  5 bancos, todos conocidos y autorizados
  1 supervisor con nodo de solo lectura

REQUISITOS
  pico de 40 operaciones por segundo
  finalidad en menos de 5 segundos
  ningún banco puede imponer el orden por sí solo
  el sistema debe seguir con un banco caído

CANDIDATOS
  A · prueba de trabajo
  B · prueba de participación
  C · bizantino entre conocidos, rotación de productor
```

**Paso 1 — descarta lo que no cumple un requisito duro.**

```text
FINALIDAD EN MENOS DE 5 SEGUNDOS

  A · probabilística: nunca hay finalidad, solo
      probabilidad creciente. Para un riesgo razonable
      hacen falta varios bloques
      → INCUMPLE

  B · casi determinística, pero típicamente en
      decenas de segundos a minutos
      → INCUMPLE en la mayoría de configuraciones

  C · determinística al cerrar la ronda
      → CUMPLE

  El requisito de finalidad ya decide, y no por
  preferencia: por definición del mecanismo.
```

**Paso 2 — comprueba el umbral con cinco participantes.**

```text
n = 5  →  f = 1

  el sistema tolera UN banco defectuoso
  con DOS, se detiene (elige seguridad sobre progreso)

  ¿ES SUFICIENTE?
    requisito: «seguir con un banco caído» → sí, cumple
    pero el margen es de uno

  ¿SE PUEDE AMPLIAR?
    con 7 nodos, f = 2
    los 5 bancos + 2 nodos operados por... ¿quién?
    si los operan los mismos bancos, NO son independientes:
    n crece y f no
```

**Paso 3 — analiza la correlación, que es lo que importa.**

```text
CINCO BANCOS, ¿CINCO INDEPENDENCIAS?

  · dos usan el mismo proveedor de nube
  · los cinco usan la misma implementación del software
  · los cinco están en la misma jurisdicción

  UN DEFECTO EN LA IMPLEMENTACIÓN AFECTA A LOS CINCO
  → f = 1 protege de un banco malicioso
  → f = 1 NO protege de un fallo común

HALLAZGO
  el consenso bizantino tolera participantes que mienten,
  no software que se equivoca igual en todos
```

**Paso 4 — diseña la mitigación del fallo común.**

```text
DIVERSIDAD DE IMPLEMENTACIÓN
  dos implementaciones distintas del mismo protocolo,
  3 nodos con una y 2 con otra

  coste: la segunda implementación y su mantenimiento
  beneficio: un defecto de una no detiene la red

  PERO
    dos implementaciones que interpretan una regla
    de forma distinta producen una BIFURCACIÓN,
    que es peor que una parada

  → la diversidad exige una especificación tan precisa
    que las dos implementaciones no puedan discrepar,
    y eso es difícil y caro

DECISIÓN
  una sola implementación, con:
    · pruebas de conformidad exhaustivas
    · procedimiento de parada coordinada ante
      comportamiento anómalo
    · capacidad de revertir a una versión anterior
  y se DECLARA como riesgo residual aceptado
```

**Paso 5 — resuelve el orden de las transacciones.**

```text
REQUISITO: «ningún banco puede imponer el orden»

  ROTACIÓN DE PRODUCTOR
    el turno rota de forma determinista y verificable
    cada banco produce 1 de cada 5 bloques

  ¿BASTA?
    NO. Durante su turno, el productor sigue eligiendo.
    Con 40 operaciones por segundo y bloques de 2 s,
    su turno cada 10 s le da 80 operaciones que ordenar.

  CONTROL ADICIONAL
    · las operaciones llegan a la mempool con marca
      de tiempo firmada por el nodo receptor
    · el productor debe incluirlas en orden de llegada
    · cualquier nodo puede demostrar una desviación
    · una desviación demostrada suspende al productor

  ESO NO ELIMINA EL PODER: LO HACE DETECTABLE
  Y CON CONSECUENCIA, QUE ES LO ALCANZABLE
```

**Paso 6 — verifica el rendimiento.**

```text
CON n = 5 Y O(n²) MENSAJES

  25 mensajes por ronda, 1 ronda por bloque,
  1 bloque cada 2 s → 12,5 mensajes por segundo

  cada mensaje incluye el bloque o su resumen:
  el ancho de banda calculado en la clase 4 sobra

  40 OPERACIONES POR SEGUNDO CON BLOQUES DE 2 s
    80 operaciones por bloque
    dimensionado en 80 KB → cabe  ✓
```

**Paso 7 — escribe la decisión con su condición de revisión.**

```text
MECANISMO: CONSENSO BIZANTINO ENTRE CONOCIDOS,
CON ROTACIÓN DE PRODUCTOR Y ORDEN VERIFICABLE

  MOTIVOS
    1. el requisito de finalidad en 5 s descarta las
       otras dos familias por definición
    2. con participantes conocidos, gastar energía o
       capital para decidir el orden es pagar por una
       propiedad que ya se tiene
    3. n = 5 tolera 1 defectuoso, que cumple el requisito

  RIESGOS RESIDUALES DECLARADOS
    · fallo común de implementación: NO cubierto por f = 1
    · jurisdicción única: una orden judicial alcanza a todos
    · con 2 bancos caídos, la red se detiene

  CONDICIONES DE REVISIÓN
    · si entran participantes hasta n ≥ 7, recalcular f
    · si un participante concentra más de un nodo,
      recalcular la independencia real
    · si aparece un requisito de participación abierta,
      el mecanismo deja de servir y hay que rediseñar
```

**Interpreta:** el requisito de finalidad decidió la familia en el primer paso, y
el análisis útil vino después: **cinco nodos no son cinco independencias**. El
consenso bizantino tolera participantes que mienten y no software que se
equivoca igual en todos, y esa distinción no aparece en ninguna comparativa
comercial.

## 🧭 Perspectivas

El mecanismo de consenso afecta a cada participante de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Banco participante | Un turno de producción cada 10 s | Si acepta el reparto |
| Banco excluido de un bloque | Su operación retrasada | Si reclama |
| Supervisor | Un nodo de solo lectura | Si le basta para vigilar |
| Tecnología | Una implementación única | Qué pruebas exige |
| Riesgo operacional | f = 1 con correlación | Qué residual acepta |
| Auditor | Orden verificable | Cómo comprueba una desviación |
| Nuevo participante | Un consorcio de cinco | Si puede entrar |

## 🏦 Del cliente al banco

El cliente no lo ve y la seguridad de su operación depende de esa elección. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Mi operación tardó más» | El productor la ordenó después | 19, clase 5 |
| «El sistema estuvo parado» | Dos participantes caídos: seguridad sobre progreso | 19, clase 5 |
| «Confirmado en segundos» | Finalidad determinística | 19, clase 6 |

## ⚖️ Riesgos y controles

Los riesgos son de concentración de validadores y de coste de ataque insuficiente. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Nodos correlacionados | Mismo software, misma nube | Analizar independencia real, no contar nodos |
| Censura del productor | Excluye o retrasa operaciones | Orden verificable con consecuencia |
| Umbral insuficiente | Dos caídas detienen la red | Recalcular f al cambiar n |
| Bifurcación por diversidad | Dos implementaciones discrepan | Especificación precisa o implementación única |
| Jurisdicción única | Una orden alcanza a todos | Declararlo como riesgo residual |
| Confundir escala con requisito | Se descarta lo bizantino «porque no escala» | Con 5 a 20 participantes, escala de sobra |

## 🧪 Práctica

El laboratorio pide calcular el coste de ataque de varios mecanismos. La comparación con el valor asegurado es la conclusión.

En [`labs/lab-04.md`](../labs/lab-04.md):

1. Implementa un consenso con votación y mide el umbral real.
2. Introduce nodos que mienten y comprueba dónde deja de funcionar.
3. Simula un fallo común y demuestra que f no lo cubre.
4. Implementa la rotación de productor y la detección de desviación de orden.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen elecciones de consenso mal fundadas. Las causas son coste de ataque no calculado y concentración de validadores.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Contar nodos como independencias | Se miró el número | Analiza proveedor, software y jurisdicción |
| «Lo bizantino no escala» | Se aplicó un criterio de red abierta | Con pocos participantes escala |
| Elegir prueba de trabajo en un consorcio | Se copió una red pública | Con participantes conocidos, se paga de más |
| Rotación como único control de orden | Se resolvió el turno, no la elección | Orden verificable |
| Olvidar la propiedad de progreso | Solo se miró la seguridad | Ante partición hay que elegir |
| No recalcular f al crecer | Se fijó al inicio | f depende de n |

## ❓ Preguntas de comprobación

1. ¿Qué decide exactamente un mecanismo de consenso y qué no decide?
2. ¿De dónde sale el umbral de 3f + 1?
3. ¿De qué depende la seguridad de cada familia y cuándo deja de sostenerse?
4. ¿Por qué la rotación de productor no basta para controlar el orden?
5. En el ejemplo guiado, ¿qué riesgo no cubría f = 1 y por qué?

## 📥 Entregable

Guarda en `portfolio/parte-19/clase-05/`:

- la comparación de las tres familias con los ocho criterios;
- el cálculo de f para tu número de participantes, con el análisis de
  independencia real;
- el diseño del control de orden, con su mecanismo de detección;
- la decisión con sus riesgos residuales y sus condiciones de revisión.

## 🔗 Referencias cruzadas

- **Viene de:** clases 1 y 4.
- **Continúa en:** clase 6 (finalidad), clase 7 (tipos de red), clase 13
  (gobernanza).
- **Se aplica en:** Parte 21, clase 15; Parte 23, clase 11.

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

- Castro, M. y Liskov, B. (1999). *Practical Byzantine Fault Tolerance*. OSDI. Algoritmo de consenso tolerante a fallos bizantinos que la clase compara. <https://pmg.csail.mit.edu/papers/osdi99.pdf>
- Lamport, L., Shostak, R. y Pease, M. (1982). *The Byzantine Generals Problem*. ACM TOPLAS. Cota teórica de participantes deshonestos que el consenso admite.
- NIST (2018). *NISTIR 8202: Blockchain Technology Overview*. NIST. Clasificación de las familias de consenso y su coste. <https://csrc.nist.gov/pubs/ir/8202/final>
- Committee on Payments and Market Infrastructures (2017). *Distributed ledger technology in payment, clearing and settlement: an analytical framework*. BIS. Efecto del consenso elegido sobre la firmeza del pago. <https://www.bis.org/cpmi/publ/d157.htm>
- Bank for International Settlements (2018). *Annual Economic Report, capítulo V*. BIS. Límites de escalabilidad del consenso por prueba de trabajo. <https://www.bis.org/publ/arpdf/ar2018e5.htm>
- Verificación local: comprueba si tu supervisor exige criterios sobre la gobernanza y la resiliencia del mecanismo de consenso en una infraestructura financiera. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 04 · Transacciones, bloques, nodos y estado](04-transacciones-bloques-nodos-y-estado.md) | [Parte 19](../README.md) · [Programa](../../../SYLLABUS.md) | [06 · Finalidad, reorganizaciones y tolerancia a fallos →](06-finalidad-reorganizaciones-y-tolerancia-a-fallos.md) |
<!-- gen:footer:end -->
