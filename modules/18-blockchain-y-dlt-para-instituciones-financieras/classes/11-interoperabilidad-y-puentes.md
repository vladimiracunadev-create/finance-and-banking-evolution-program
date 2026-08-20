<!-- meta
part: 19
class: 11
title: "Interoperabilidad y puentes"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global]
regulatory_topics: [dlt, riesgo-operacional, custodia]
regulation_last_verified: 2026-08-20
regulatory_status: vigente
primary_authorities: [CPMI, FSB]
requires_legal_review: false
-->

<!-- gen:header:start -->
# Clase 11 · Interoperabilidad y puentes

> [← 10 · Privacidad y pruebas criptográficas](10-privacidad-y-pruebas-criptograficas.md) · [Índice de la parte](../README.md) · [12 · Escalabilidad, capas y disponibilidad →](12-escalabilidad-capas-y-disponibilidad.md)

**Parte 19 — Blockchain y DLT para instituciones financieras** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Entender por qué mover un activo entre dos registros es mucho más difícil de lo
que parece, y por qué los puentes concentran una parte desproporcionada de las
pérdidas conocidas del sector.

Las clases anteriores construyen una red. Esta la conecta con otras, y muestra que nada cruza de verdad: lo que hay es un bloqueo en un lado y una emisión en el otro, con un custodio en medio.

## 📚 Objetivos

Al finalizar podrás:

1. **Explicar** por qué un activo no «se mueve» entre registros y qué ocurre en
   realidad.
2. **Comparar** los tres modelos de puente por dónde queda el riesgo.
3. **Identificar** los cuatro puntos de fallo que concentran los incidentes.
4. **Evaluar** un puente con las mismas preguntas que una relación de
   corresponsalía.
5. **Decidir** cuándo un activo puenteado deja de ser el activo original.

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

Los tres primeros términos son los mecanismos de traslado; los cinco siguientes, sus actores y su riesgo. El **riesgo de emisor del puente** es el concepto que hay que retener: un activo envuelto no es el activo original sino un derecho contra quien custodia el original.

| Concepto | Comprensión verificable |
|---|---|
| `puente` | Mecanismo que representa en un registro un activo de otro |
| `bloqueo y emisión` | El original se inmoviliza y se emite una representación |
| `quema y emisión` | El original se destruye y se emite en el destino |
| `activo envuelto` | Representación de un activo de otro registro |
| `custodio del puente` | Quien guarda el activo original |
| `mensaje entre cadenas` | Comunicación que informa de un hecho de otro registro |
| `cliente ligero en cadena` | Verificación del otro registro dentro del contrato |
| `riesgo de emisor del puente` | Riesgo de que la representación no se pueda canjear |

## 🧠 Modelo mental

El modelo mental es que nada cruza de verdad: el activo se bloquea en un lado y se emite una representación en el otro. Quien custodia el bloqueo es una contraparte, y los puentes son el componente más atacado de este ecosistema.

```text
UN ACTIVO NO SE MUEVE ENTRE REGISTROS.
NUNCA.

  el registro A no puede escribir en el registro B
  y el registro B no puede leer el registro A

  LO QUE OCURRE ES
    1. el activo se inmoviliza o se destruye en A
    2. ALGUIEN afirma que eso ocurrió
    3. en B se emite una representación

  EL PASO 2 ES EL PUENTE, Y ES UN TERCERO DE CONFIANZA
  (o un mecanismo que intenta no serlo)

CONSECUENCIA QUE HAY QUE INTERIORIZAR
  el activo envuelto en B NO es el activo de A:
  es un derecho frente a quien custodia el de A
```

## 📖 Desarrollo

### 1. Los tres modelos

| Modelo | Cómo funciona | Dónde queda el riesgo |
|---|---|---|
| **Custodio** | Una entidad guarda el original y emite en destino | En el custodio: es un emisor |
| **Conjunto de validadores** | m de n firman que el hecho ocurrió | En la colusión de m validadores |
| **Verificación en cadena** | El contrato de destino verifica el registro de origen | En la implementación y en el coste |

El tercer modelo es el mejor desde el punto de vista de la seguridad y el que
menos se implanta, por una razón de coste.

```text
EL TERCERO ES EL MEJOR TÉCNICAMENTE Y EL MÁS CARO
  el contrato de destino ejecuta un cliente ligero
  del registro de origen: verifica cabeceras y pruebas
  de Merkle sin confiar en nadie

  COSTE
    ejecutar esa verificación en cada mensaje
    puede ser prohibitivo, y por eso la mayoría
    de los puentes en producción usan el segundo modelo
```

### 2. Los cuatro puntos de fallo

Los incidentes de puentes se concentran en cuatro puntos, y conocerlos permite
evaluar uno sin ser especialista en su implementación. El bloque los describe
en orden de gravedad observada.

```text
1. LAS CLAVES DEL PUENTE
   comprometer m de n validadores permite emitir
   representaciones sin respaldo
   → es la causa de los mayores incidentes conocidos

2. EL CONTRATO DE EMISIÓN
   un defecto de control de acceso permite acuñar
   sin depósito (clase 8)

3. LA VERIFICACIÓN DEL MENSAJE
   aceptar una prueba mal verificada permite
   afirmar hechos falsos del otro registro

4. LA RECONFIGURACIÓN DEL CONJUNTO
   el procedimiento para cambiar los validadores
   suele estar menos protegido que la operación normal
   → se ataca ahí

LOS CUATRO SON DEFECTOS DE IMPLEMENTACIÓN
O DE GOBIERNO, NO DEL CONCEPTO
```

### 3. Evaluar un puente como una corresponsalía

Un puente hace lo mismo que un corresponsal: custodia un activo en un sitio y
emite un derecho en otro. El bloque reutiliza las preguntas de la parte
anterior y añade la única que no tiene equivalente clásico.

```text
LAS PREGUNTAS DE LA PARTE 18, CLASE 3, APLICAN AQUÍ

  · ¿quién es el custodio y quién lo controla?
  · ¿qué licencia tiene y qué supervisor?
  · ¿el activo original está segregado?
  · ¿hay auditoría de las reservas?
  · ¿existe derecho de canje exigible, y frente a quién?
  · ¿qué pasa si el custodio quiebra?
  · ¿qué pasa si el registro de origen se bifurca?

LA ÚLTIMA NO TIENE EQUIVALENTE EN CORRESPONSALÍA
  si el registro de origen se bifurca, ¿cuál de las
  dos cadenas respalda la representación?
  → hay que responderlo ANTES, no durante
```

### 4. Cuándo el activo envuelto deja de ser el activo

Una representación deja de valer lo que el activo original de forma gradual, y
hay señales que lo anticipan. El bloque las enumera y saca la consecuencia
contable, que es la que suele llegar tarde.

```text
SEÑALES DE QUE LA REPRESENTACIÓN SE HA DESPEGADO

  · el canje no es inmediato ni garantizado
  · el custodio impone límites o comisiones al canje
  · la representación cotiza con descuento sostenido
  · hay más representación emitida que original
    custodiado
  · el custodio está en una jurisdicción distinta
    de la del titular

CONSECUENCIA CONTABLE Y PRUDENCIAL
  un activo envuelto NO se trata como el subyacente:
  se trata como una exposición al puente

  confundirlos es el error que hace que una cartera
  «diversificada» tenga en realidad una sola contraparte
```

### 5. Interoperabilidad sin puente

Antes de asegurar un puente conviene comprobar si hace falta. El bloque
recoge las tres formas de interoperar sin mover activos y señala cuál eligen
los proyectos institucionales, y por qué motivo.

```text
NO TODA INTEROPERABILIDAD EXIGE MOVER ACTIVOS

  · MENSAJERÍA: un registro informa a otro de un hecho,
    sin que nada cruce
  · LIQUIDACIÓN ATÓMICA ENTRE REGISTROS: dos operaciones
    condicionadas la una a la otra, cada activo
    en su registro (Parte 18, clase 15)
  · PLATAFORMA COMÚN: los dos activos viven en el mismo
    registro y el problema desaparece

LA TERCERA ES LA QUE ELIGEN VARIOS PROYECTOS
INSTITUCIONALES, y no es casualidad: evita el puente
en vez de asegurarlo
```

## 🧮 Ejemplo guiado

El ejemplo sigue un activo a través de un puente y sitúa el riesgo de contraparte. El activo envuelto vale lo que valga el custodio.

**Situación.** Un banco quiere ofrecer a sus clientes exposición a un activo que
vive en otro registro. Evalúa usar un puente.

```text
DATOS DEL PUENTE CANDIDATO
  modelo: conjunto de validadores, 8 de 13
  validadores: 13 entidades, 5 del mismo grupo
  activo custodiado                  1 240 000 000
  representación emitida             1 240 000 000
  auditoría de reservas              trimestral, firma no publicada
  canje                              disponible, comisión 0,3 %
  historial                          2 años, sin incidentes
  seguro                             no

VOLUMEN PREVISTO DEL BANCO
  exposición máxima                     85 000 000
```

**Paso 1 — analiza el umbral real.**

```text
8 DE 13, PERO 5 SON DEL MISMO GRUPO

  si ese grupo actúa como uno, aporta 5 firmas
  hacen falta 3 más de las 8 restantes

  UMBRAL EFECTIVO: 5 (grupo) + 3 = colusión de 4 entidades
  frente a los 8 nominales

  Y SI EL GRUPO TIENE UN INCIDENTE INTERNO,
  se pierden 5 firmas de golpe: quedan 8,
  justo el umbral. Un fallo más y el puente se detiene.
```

**Paso 2 — evalúa la auditoría.**

```text
TRIMESTRAL Y SIN FIRMA PUBLICADA

  ¿qué prueba? que en una fecha, alguien dijo
  que las reservas cuadraban

  LO QUE FALTA
    · quién audita y con qué alcance
    · prueba criptográfica de reservas y pasivos
      (clase 2: árbol de sumas con prueba de rango)
    · continuidad entre auditorías

  ENTRE DOS AUDITORÍAS HAY 90 DÍAS EN LOS QUE
  NADIE COMPRUEBA NADA
```

**Paso 3 — busca el derecho de canje.**

```text
«CANJE DISPONIBLE, COMISIÓN 0,3 %»

  PREGUNTAS SIN RESPONDER
    · ¿es un derecho contractual o una práctica?
    · ¿frente a quién se ejerce?
    · ¿en qué plazo?
    · ¿puede suspenderse? ¿por quién?
    · ¿qué ley lo rige?

  SI NO HAY CONTRATO, NO HAY DERECHO:
  hay una función de un programa que alguien
  puede desactivar
```

**Paso 4 — calcula la exposición real.**

```text
EL BANCO CREE QUE TIENE EXPOSICIÓN AL ACTIVO.
TIENE EXPOSICIÓN AL PUENTE.

  85 000 000 frente a un conjunto de 13 entidades
  con umbral efectivo de 4, sin seguro y sin
  derecho de canje documentado

  TRATAMIENTO CORRECTO
    · límite de contraparte frente al puente
    · no computar la representación como el subyacente
    · tratamiento prudencial de la exposición
```

**Paso 5 — evalúa las alternativas.**

```text
A · usar el puente con límite reducido
    exposición máxima 15 000 000 en vez de 85 000 000
    coste: menos producto que ofrecer

B · custodiar directamente en el registro de origen
    el banco opera un nodo y custodia el activo original
    coste: infraestructura y gestión de claves (clase 3)
    ventaja: sin riesgo de puente

C · exposición sintética
    un derivado con una contraparte regulada
    replica el rendimiento sin tocar el activo
    coste: prima y riesgo de contraparte conocido
    ventaja: contraparte supervisada y contrato

D · no ofrecerlo
```

**Paso 6 — compara con el criterio correcto.**

```text
LA PREGUNTA NO ES «¿CUÁL ES MÁS BARATA?»
ES «¿QUÉ RIESGO ESTOY ASUMIENDO Y LO SÉ MEDIR?»

  A · riesgo de un puente sin contrato ni seguro
      medible: no. La colusión de 4 no tiene probabilidad
      estimable y la severidad es total.

  B · riesgo de custodia propia
      medible: sí. Es el de la clase 3, con controles
      conocidos.

  C · riesgo de contraparte
      medible: sí. Es el de toda la Parte 11.

  D · sin riesgo y sin producto
```

**Paso 7 — decide.**

```text
DECISIÓN: OPCIÓN B PARA POSICIÓN PROPIA,
OPCIÓN C PARA EXPOSICIÓN DE CLIENTES

  MOTIVOS
    1. el puente introduce un riesgo que el banco
       no sabe medir ni limitar
    2. las opciones B y C tienen riesgos que el banco
       ya gestiona con marcos existentes
    3. el coste adicional de B y C es conocido;
       el de A es una cola sin estimar

  SI SE USARA EL PUENTE ALGUNA VEZ
    · límite de exposición explícito y bajo
    · tratamiento como exposición al puente,
      no al subyacente
    · seguimiento del umbral efectivo, no del nominal
    · condición de salida si la auditoría se retrasa

  Y UNA OBSERVACIÓN PARA EL COMITÉ
    «2 años sin incidentes» no es evidencia de
    seguridad: los incidentes de puentes conocidos
    ocurrieron en sistemas con historiales similares
    hasta el día anterior.
```

**Interpreta:** el puente prometía 8 de 13 y el umbral efectivo era 4. La
decisión no se tomó comparando costes, sino preguntando **cuál de los riesgos
sabía medir el banco**, que es el criterio que un comité puede sostener ante un
supervisor.

## 🧭 Perspectivas

La interoperabilidad afecta a cada participante de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Exposición a un activo | Si distingue el envuelto del original |
| Banco | 85 M de exposición | A quién se la asigna |
| Puente | 13 validadores | Cómo lo comunica |
| Custodio | Reserva de 1 240 M | Si publica prueba |
| Riesgo de contraparte | Un emisor sin contrato | Qué límite pone |
| Supervisor | Activo envuelto en balance | Cómo lo trata |
| Auditor | Auditoría trimestral sin firma | Qué evidencia acepta |

## 🏦 Del cliente al banco

El cliente cree tener el activo original y tiene un derecho contra un custodio. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Tengo el activo» | Tiene un derecho frente al puente | 19, clase 11 |
| «Puedo canjearlo cuando quiera» | Si hay contrato; si no, es una función | 19, clase 11 |
| «El puente lleva dos años bien» | El historial no mide la cola | 19, clase 11 |

## ⚖️ Riesgos y controles

Los riesgos son de custodia del puente y de validación de mensajes. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Umbral efectivo menor que el nominal | Validadores del mismo grupo | Analizar propiedad y control |
| Sin derecho de canje | Una función que se desactiva | Exigir contrato y ley aplicable |
| Emisión sin respaldo | Defecto o colusión | Prueba criptográfica de reservas |
| Reconfiguración de validadores | El procedimiento está menos protegido | Mismo umbral que la operación |
| Bifurcación del origen | ¿Qué cadena respalda? | Responder antes de operar |
| Tratar el envuelto como el subyacente | Cartera con una sola contraparte real | Exposición al puente |

## 🧪 Práctica

El laboratorio pide analizar el riesgo de contraparte de varios puentes. El mecanismo de bloqueo y emisión es el que concentra el riesgo.

En [`labs/lab-06.md`](../labs/lab-06.md):

1. Calcula el umbral efectivo de tres puentes con distinta estructura.
2. Aplica las siete preguntas de corresponsalía a un puente.
3. Modela qué ocurre si el registro de origen se bifurca.
4. Compara tres alternativas por «riesgo que sé medir», no por coste.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen pérdidas en puentes. La causa es el custodio tratado como si no existiera.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Contar validadores | Se leyó el número nominal | Analiza propiedad y control |
| «El activo se mueve» | Se creyó la metáfora | Se inmoviliza y se representa |
| Tratar el envuelto como el subyacente | Se copió el ticker | Es exposición al puente |
| Historial como evidencia | Se miró hacia atrás | La cola no está en el historial |
| Canje asumido | No se pidió el contrato | Sin contrato no hay derecho |
| Elegir por coste | Se comparó lo comparable | Compara riesgos medibles |

## ❓ Preguntas de comprobación

1. ¿Qué ocurre realmente cuando un activo «pasa» de un registro a otro?
2. ¿Cuáles son los tres modelos y dónde queda el riesgo en cada uno?
3. ¿Cuáles son los cuatro puntos de fallo y cuál se ataca por estar menos
   protegido?
4. ¿Cuándo un activo envuelto deja de ser equivalente al original?
5. En el ejemplo guiado, ¿por qué 8 de 13 eran en realidad 4?

## 📥 Entregable

Guarda en `portfolio/parte-19/clase-11/`:

- el cálculo del umbral efectivo de tres puentes;
- las siete preguntas aplicadas a uno concreto, con las respuestas que faltan;
- el análisis de qué ocurre ante una bifurcación del origen;
- la comparación de alternativas por riesgo medible, con tu decisión.

## 🔗 Referencias cruzadas

- **Viene de:** clases 3, 6 y 8; Parte 18, clase 3 (corresponsalía).
- **Continúa en:** clase 12 (coste de la verificación), clase 13 (bifurcaciones).
- **Se aplica en:** Parte 20, clase 5; Parte 21, clase 15; Parte 23, clase 10.

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

- Financial Stability Board (2023). *The Financial Stability Risks of Decentralised Finance*. FSB. Pérdidas observadas en puentes y su concentración. <https://www.fsb.org/2023/02/the-financial-stability-risks-of-decentralised-finance/>
- IOSCO (2022). *Decentralized Finance Report*. IOSCO. Riesgos de la interoperabilidad entre registros. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD699.pdf>
- Committee on Payments and Market Infrastructures (2022). *Interlinking payment systems and the role of application programming interfaces*. BIS. Comparación con la interconexión de sistemas de pago tradicionales. <https://www.bis.org/cpmi/publ/d205.htm>
- Basel Committee on Banking Supervision (2022). *Prudential treatment of cryptoasset exposures*. BIS. Tratamiento de capital de la exposición transferida entre registros. <https://www.bis.org/bcbs/publ/d545.htm>
- NIST (2018). *NISTIR 8202: Blockchain Technology Overview*. NIST. Mecanismos técnicos de transferencia entre registros. <https://csrc.nist.gov/pubs/ir/8202/final>
- Verificación local: comprueba cómo trata tu marco prudencial la exposición a un activo envuelto frente al subyacente. **Fecha de verificación de esta clase: 2026-08-20.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 10 · Privacidad y pruebas criptográficas](10-privacidad-y-pruebas-criptograficas.md) | [Parte 19](../README.md) · [Programa](../../../SYLLABUS.md) | [12 · Escalabilidad, capas y disponibilidad →](12-escalabilidad-capas-y-disponibilidad.md) |
<!-- gen:footer:end -->
