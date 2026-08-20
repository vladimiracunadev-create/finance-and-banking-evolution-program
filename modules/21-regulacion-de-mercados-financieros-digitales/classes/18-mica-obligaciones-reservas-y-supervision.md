<!-- meta
part: 22
class: 18
title: "MiCA II: obligaciones, reservas y supervisión"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [union-europea]
regulatory_topics: [mica, reservas, redencion, supervision, abuso-de-mercado]
regulation_last_verified: 2026-08-20
regulatory_status: vigente
primary_authorities: [EBA, ESMA]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 18 · MiCA II: obligaciones, reservas y supervisión

> [← 17 · MiCA I: perímetro, activos y participantes](17-mica-perimetro-activos-y-participantes.md) · [Índice de la parte](../README.md) · [19 · Regímenes europeos conexos: piloto DLT, DORA y regla del viaje →](19-regimenes-europeos-conexos.md)

**Parte 22 — Regulación de mercados financieros digitales** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Recorrer lo que MiCA exige a quien ya está dentro del perímetro: **qué reserva,
qué reembolso, qué gobierno, qué plan para el día malo y qué pasa cuando la
entidad incumple.**

La clase 17 resolvió la pregunta de si el régimen aplica. Esta responde la que
viene después y es la que decide si el negocio existe: cuánto cuesta cumplirlo y
qué obligaciones no se pueden externalizar.

Hay una obligación que conviene mirar desde el principio porque cambia el diseño
de todo lo demás. MiCA exige a los emisores de fichas referenciadas y de dinero
electrónico un **plan de reembolso**: un procedimiento escrito, revisado por la
autoridad, que explica cómo se devuelve el valor a todos los tenedores si la
actividad se detiene de forma ordenada. Es la pieza que la Parte 20 echó de menos
al estudiar las corridas, y es la que ningún emisor redacta por voluntad propia.

## 📚 Objetivos

Al finalizar podrás:

1. **Enumerar** los requisitos de autorización de un emisor y de un proveedor, y
   distinguir los que se comprueban una vez de los que se comprueban siempre.
2. **Evaluar** una reserva de activos contra los criterios de composición,
   custodia, segregación e inversión que exige el régimen.
3. **Calcular** el efecto del derecho de reembolso a la par sobre la liquidez del
   emisor en un escenario de salida.
4. **Distinguir** el plan de recuperación del plan de reembolso, y explicar qué
   pregunta responde cada uno.
5. **Identificar** las conductas de abuso de mercado que el régimen tipifica para
   los criptoactivos y cómo se detectan.

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

Los cuatro primeros términos describen el patrimonio que respalda la promesa; los
cuatro siguientes, el gobierno y la salida. El que más se malinterpreta es
`segregación`: separar contablemente no es separar jurídicamente, y solo lo
segundo protege al tenedor cuando el emisor entra en concurso.

| Concepto | Comprensión verificable |
|---|---|
| `reserva de activos` | Patrimonio afecto que respalda las fichas emitidas |
| `segregación` | Separación jurídica del patrimonio propio del emisor |
| `custodia de la reserva` | Depósito en entidad habilitada y distinta |
| `reembolso a la par` | Derecho a recuperar el valor nominal sin descuento |
| `fondos propios` | Capital exigido de forma permanente |
| `plan de recuperación` | Cómo se restablece el cumplimiento sin cerrar |
| `plan de reembolso` | Cómo se devuelve a todos si se cierra |
| `externalización` | Delegar una función sin delegar la responsabilidad |

## 🧠 Modelo mental

El modelo mental es un balance con una promesa encima y dos salidas debajo. La
promesa es el reembolso a la par; el activo que la sostiene es la reserva; y las
dos salidas son la recuperación y el reembolso ordenado. Casi todos los fallos
que la Parte 20 estudió consisten en que la promesa era diaria y la reserva no.

```text
LA ESTRUCTURA QUE MICA IMPONE

  PROMESA        reembolso a la par,
                 en todo momento

  RESERVA        activos afectos
                 · segregados jurídicamente
                 · custodiados fuera
                 · invertidos solo en
                   instrumentos muy líquidos
                   y de riesgo mínimo

  FONDOS PROPIOS capital del emisor,
                 adicional a la reserva
                 y no confundible con ella

  DOS SALIDAS
   RECUPERACIÓN  vuelvo a cumplir sin cerrar
   REEMBOLSO     cierro y devuelvo a todos

EL ERROR DE DISEÑO MÁS COMÚN
  usar la reserva como fondos propios
  → un solo euro respondiendo dos veces
```

## 📖 Desarrollo

### 1. La autorización: lo que se comprueba una vez y lo que se comprueba siempre

Un expediente de autorización mezcla dos naturalezas de requisito, y confundirlas
produce entidades que se autorizan bien y se supervisan mal.

```text
SE COMPRUEBA UNA VEZ
  · forma jurídica y domicilio en la Unión
  · idoneidad de administradores y de
    accionistas significativos
  · descripción de los servicios
  · sistemas y procedimientos escritos
  · capital inicial

SE COMPRUEBA SIEMPRE
  · fondos propios por encima del mínimo
  · segregación efectiva de los fondos
    y activos de clientes
  · política de conflictos aplicada
  · continuidad probada, no descrita
  · comunicaciones publicitarias veraces
  · información al supervisor, en plazo

EL EXPEDIENTE ES LA PUERTA.
LA SUPERVISIÓN ES EL PASILLO,
Y EL PASILLO NO TERMINA.
```

Que el capital exigido sea permanente, y no un depósito de entrada, es lo que
convierte la autorización en una decisión de negocio y no en un trámite: la
clase 4 de esta parte lo tradujo en la cifra que decide si el negocio existe, y
aquí se ve de dónde sale esa cifra.

### 2. La reserva de activos: composición, custodia y segregación

La reserva es el corazón del régimen de las fichas estables. MiCA no se conforma
con exigir que exista: le impone reglas sobre en qué puede invertirse, quién debe
custodiarla y cómo debe separarse del patrimonio del emisor.

```text
LAS CUATRO REGLAS DE LA RESERVA

  1 · COMPOSICIÓN
      instrumentos muy líquidos y de riesgo
      mínimo; se limita la concentración por
      emisor y por vencimiento

  2 · CUSTODIA
      en entidad habilitada y distinta del
      emisor; con responsabilidad del
      custodio por la pérdida

  3 · SEGREGACIÓN
      jurídica, no solo contable; la reserva
      no responde de las deudas del emisor

  4 · VALORACIÓN Y PUBLICACIÓN
      con periodicidad, y con auditoría
      independiente

LO QUE ESTAS REGLAS COMPRAN
  que en el concurso del emisor la reserva
  no entre en la masa

LO QUE NO COMPRAN
  que la reserva valga lo prometido si el
  mercado de esos activos se cierra
```

La cuarta regla merece una precisión que la Parte 20 ya introdujo: una atestación
periódica no es una auditoría, y una auditoría de existencia no es una auditoría
de suficiencia. Comprobar que los activos están no es lo mismo que comprobar que
alcanzan, y esa diferencia solo se nota cuando hacen falta.

### 3. El derecho de reembolso y lo que hace con la liquidez

El reembolso a la par y en todo momento es la obligación que más condiciona el
diseño del activo de la reserva, porque convierte un pasivo teóricamente estable
en un pasivo a la vista.

```text
LA ARITMÉTICA QUE NADIE HACE ANTES

  fichas en circulación        800 000 000
  reserva                      800 000 000
    · 55 % vencimiento < 7 días
    · 30 % vencimiento < 90 días
    · 15 % vencimiento > 90 días

  PETICIÓN DE REEMBOLSO EN UN DÍA: 12 %
                              96 000 000

  DISPONIBLE SIN VENDER        440 000 000
  → SE ATIENDE

  PETICIÓN EN UNA SEMANA: 60 %
                             480 000 000
  DISPONIBLE SIN VENDER        440 000 000
  FALTAN                        40 000 000
  → HAY QUE VENDER EL TRAMO LARGO
    Y ESE TRAMO SE VENDE JUSTO CUANDO
    TODOS VENDEN

LA PROMESA ES DIARIA.
EL ACTIVO NO PUEDE SER SEMESTRAL.
```

### 4. Recuperación y reembolso: dos planes, dos preguntas

Los dos planes se confunden porque ambos se escriben para el día malo, pero
responden preguntas distintas y se activan en momentos distintos.

```text
PLAN DE RECUPERACIÓN
  pregunta: ¿cómo vuelvo a cumplir
            sin dejar de operar?
  contiene: indicadores de activación,
            medidas de liquidez y de capital,
            gobierno de la decisión
  se activa: cuando cruzo un umbral

PLAN DE REEMBOLSO
  pregunta: ¿cómo devuelvo a todos
            si dejo de operar?
  contiene: orden de prelación, calendario,
            comunicación, y quién ejecuta si
            el emisor ya no puede
  se activa: cuando la actividad cesa

LA PRUEBA DE QUE UN PLAN DE REEMBOLSO
ESTÁ BIEN ESCRITO
  se puede ejecutar sin el emisor
```

Ese último criterio es el que separa un plan útil de un documento de
cumplimiento. Un plan que depende de que el equipo del emisor esté disponible y
de que sus sistemas funcionen no sirve para el escenario en el que se activa.

### 5. Conducta, publicidad y responsabilidad por la información

MiCA traslada al mundo de los criptoactivos las tres conductas que el derecho de
mercados prohíbe desde hace décadas, y añade una regla de publicidad que en la
práctica es la que más expedientes genera.

```text
TRES CONDUCTAS TIPIFICADAS

  OPERACIÓN CON INFORMACIÓN PRIVILEGIADA
    operar sabiendo lo que el mercado
    todavía no sabe

  COMUNICACIÓN ILÍCITA
    contarlo a quien no debe saberlo

  MANIPULACIÓN DE MERCADO
    operaciones u órdenes que dan una
    señal falsa sobre precio u oferta

Y UNA REGLA DE PUBLICIDAD
  toda comunicación comercial debe ser
  identificable como tal, ser veraz, no
  inducir a error, y ser coherente con el
  libro blanco

LA INFRACCIÓN MÁS FRECUENTE NO ES
LA MANIPULACIÓN: es una pieza de marketing
que promete algo que el libro blanco
no dice.
```

La responsabilidad por el libro blanco es civil y recae sobre el órgano de
administración del emisor. No es una responsabilidad de la entidad como
abstracción: tiene nombres, y esa es exactamente la diferencia que la clase 17
señaló entre este régimen y la situación anterior.

### 6. Externalización, supervisión y régimen transitorio

Delegar una función no delega la responsabilidad. Es una frase que aparece en
todos los regímenes y que se incumple de la misma manera en todos: la entidad
contrata a un tercero, el tercero subcontrata a un cuarto, y nadie tiene el mapa
completo. La clase 14 de esta parte midió lo que eso cuesta cuando el cuarto es
común a veintidós entidades.

```text
LO QUE EXIGE LA EXTERNALIZACIÓN

  · contrato escrito con niveles de servicio
  · derecho de acceso y de auditoría, propio
    y del supervisor
  · plan de salida ejecutable
  · notificación de la subcontratación
  · y la responsabilidad se queda en casa

RÉGIMEN TRANSITORIO
  las entidades que ya operaban al amparo de
  normas nacionales dispusieron de un plazo
  para adaptarse

  EL ERROR TÍPICO
    tratar el transitorio como si fuera
    definitivo, y llegar al final del plazo
    con el expediente sin empezar
```

## 🧮 Ejemplo guiado

El ejemplo evalúa una reserva concreta contra las cuatro reglas y calcula qué
pasa el día en que el reembolso se pide en serio.

**Situación.** Un emisor de fichas referenciadas a una cesta pide autorización.
Presenta esta reserva y este balance.

```text
FICHAS EN CIRCULACIÓN     500 000 000
RESERVA DECLARADA         505 000 000

COMPOSICIÓN
  depósitos a la vista, banco A  60 000 000
  depósitos a plazo, banco A    140 000 000
  deuda pública < 90 días       180 000 000
  deuda pública 1 a 3 años       80 000 000
  bonos corporativos             30 000 000
  oro custodiado                 15 000 000

FONDOS PROPIOS DECLARADOS
  «los 5 000 000 de exceso de la reserva»
```

**Paso 1 — comprueba la regla de fondos propios.**

```text
LOS 5 000 000 DE EXCESO ESTÁN DENTRO
DE LA RESERVA

  → un mismo activo respondiendo dos veces:
    como respaldo de las fichas y como
    capital del emisor

  DEFECTO ESTRUCTURAL, NO CONTABLE
  los fondos propios deben ser adicionales
  y estar fuera de la reserva

  FONDOS PROPIOS REALES: 0
```

**Paso 2 — comprueba la composición.**

```text
INSTRUMENTOS DE RIESGO NO MÍNIMO
  bonos corporativos    30 000 000   5,9 %
  oro                   15 000 000   3,0 %
  deuda 1 a 3 años      80 000 000  15,8 %

CONCENTRACIÓN EN BANCO A
  60 000 000 + 140 000 000 = 200 000 000
  = 39,6 % DE LA RESERVA EN UNA CONTRAPARTE

  → dos hallazgos: composición y
    concentración
```

**Paso 3 — mide la liquidez frente a la promesa.**

```text
DISPONIBLE EN EL DÍA
  depósitos a la vista        60 000 000
  deuda pública < 90 días    180 000 000
  TOTAL                      240 000 000
                            = 48 % del pasivo

DISPONIBLE EN LA SEMANA
  + plazo banco A (con penalización)
                             140 000 000
  TOTAL                      380 000 000
                            = 76 %

EL RESTO EXIGE VENDER EN MERCADO
  125 000 000 en activos que se venden mal
  el día que hace falta venderlos
```

**Paso 4 — simula la salida ordenada.**

```text
ESCENARIO · 35 % PIDE REEMBOLSO EN 5 DÍAS
                            175 000 000

  se atiende con el disponible del día
  y parte del plazo
  → SE CUMPLE

ESCENARIO · 70 % EN 5 DÍAS  350 000 000

  disponible en la semana     380 000 000
  → SE CUMPLE POR 30 000 000

  PERO el banco A es a la vez depositario
  de 200 000 000 y contraparte del emisor
  → si el estrés viene del banco A,
    los 380 000 000 no están
```

**Paso 5 — comprueba la custodia y la segregación.**

```text
PREGUNTAS QUE HAY QUE RESPONDER CON UN
DOCUMENTO, NO CON UNA AFIRMACIÓN

  · ¿la reserva está a nombre de quién?
  · ¿figura como patrimonio afecto?
  · ¿qué dice el contrato de custodia sobre
    la pérdida?
  · ¿hay derecho de reutilización?
  · ¿qué ocurre en el concurso del custodio?
  · ¿y en el del emisor?

SI ALGUNA RESPUESTA ES «ESTÁ SEPARADO
CONTABLEMENTE», LA SEGREGACIÓN NO EXISTE
```

**Paso 6 — evalúa el plan de reembolso presentado.**

```text
EL PLAN DICE
  «el equipo de tesorería del emisor
   liquidará la reserva y abonará a los
   tenedores en un plazo de 30 días»

  PRUEBA DE EJECUTABILIDAD SIN EL EMISOR
  → falla: depende del equipo del emisor

  FALTAN
   · quién ejecuta si el emisor no puede
   · orden de atención de los tenedores
   · tratamiento de los que no aparecen
   · comunicación y canal
   · financiación del propio proceso
```

**Paso 7 — resume el expediente y cifra la remediación.**

```text
HALLAZGOS               GRAVEDAD

 fondos propios dentro   crítico
   de la reserva
 concentración 39,6 %    alto
   en una contraparte
 composición con         alto
   riesgo no mínimo
 segregación no          crítico
   acreditada
 plan de reembolso       alto
   no ejecutable

REMEDIACIÓN (supuestos)
  aportar fondos propios     8 000 000
  recomponer la reserva      2 400 000
    (coste de rotación)
  estructura de custodia       600 000
  rehacer el plan              120 000
  TOTAL                     11 120 000

  Y NINGUNO DE LOS CINCO SE RESUELVE
  CON UNA POLÍTICA ESCRITA
```

**Interpreta:** la reserva estaba «sobrecolateralizada» en un 1 % y aun así el
expediente tenía dos hallazgos críticos. El exceso declarado era ficticio porque
hacía de capital y de respaldo a la vez, y la protección real del tenedor no
dependía del importe sino de la segregación, que no estaba acreditada. **La cifra
de cobertura es el dato que más se publica y el que menos informa.**

## 🧭 Perspectivas

Las obligaciones de esta clase reparten costes y protecciones de forma desigual,
y conviene ver quién soporta cada cosa.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Tenedor | Una promesa de reembolso a la par | Si confía y cuándo sale |
| Emisor | Capital adicional a la reserva | Si el negocio se sostiene |
| Custodio | Responsabilidad por la pérdida | Qué exige y a qué precio |
| Auditor | Existencia frente a suficiencia | Qué opinión emite |
| Banco depositario | Concentración de la reserva | Si la acepta |
| Supervisor nacional | Un expediente con planes | Si autoriza o requiere |
| EBA | Umbrales de significatividad | Si asume la supervisión |
| Competidor bancario | Un pasivo a la vista sin interés | Si compite o se asocia |
| Sociedad | Un instrumento que circula como dinero | Qué respaldo exige |

## 🏦 Del cliente al banco

Las tres afirmaciones de la izquierda son las que más aparecen en material
comercial, y las tres describen mal lo que protege realmente al tenedor.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Está respaldado al 101 %» | El exceso hacía de capital y de reserva | 22, clase 18 |
| «Hay auditoría de reservas» | Existencia no es suficiencia | 22, clase 18 |
| «Puedo reembolsar cuando quiera» | Si el 70 % lo pide a la vez, no | 22, clase 18 |

## ⚖️ Riesgos y controles

Los seis riesgos son los que un supervisor busca primero en un expediente de
emisor, en este orden.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Capital dentro de la reserva | Un activo responde dos veces | Fondos propios fuera y adicionales |
| Segregación solo contable | La reserva entra en la masa | Acreditar el patrimonio afecto |
| Concentración de contraparte | El custodio es también el estrés | Límite por contraparte y por grupo |
| Desajuste de plazos | Promesa diaria, activo largo | Escalera de vencimientos probada |
| Plan de reembolso decorativo | Se activa y no se puede ejecutar | Probarlo sin el emisor |
| Publicidad incoherente | Promete lo que el libro blanco no dice | Revisión previa de toda pieza |

## 🧪 Práctica

El laboratorio de comparación de regímenes admite esta variante, que es la que
más se parece a un expediente real.

En [`labs/lab-08.md`](../labs/lab-08.md):

1. Evalúa una reserva contra las cuatro reglas y documenta cada hallazgo.
2. Calcula la liquidez disponible a un día, a una semana y a un mes.
3. Simula dos escenarios de reembolso y explica cuál rompe la promesa.
4. Reescribe un plan de reembolso que pueda ejecutarse sin el emisor.

## ⚠️ Errores frecuentes

Los seis errores comparten una raíz: tratar como cumplimiento documental lo que
es una restricción de balance.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Presumir de cobertura | Es la cifra que se publica | Mirar composición y segregación |
| Atestación como auditoría | Ambas llevan sello | Una comprueba existencia |
| Reserva con rendimiento | Mejora la cuenta de resultados | Compromete la liquidez |
| Un solo banco para todo | Simplifica la operativa | Concentra el estrés |
| Plan copiado de otro emisor | Ahorra tiempo | No refleja su reserva |
| Publicidad sin revisión previa | Marketing va más rápido | Coherencia con el libro blanco |

## ❓ Preguntas de comprobación

1. ¿Por qué los fondos propios no pueden formar parte de la reserva?
2. ¿Qué diferencia hay entre segregación contable y segregación jurídica?
3. ¿Qué distingue el plan de recuperación del plan de reembolso?
4. ¿Cuál es la prueba de que un plan de reembolso está bien escrito?
5. ¿Por qué la cifra de cobertura es el dato que menos informa?

## 📥 Entregable

Guarda en `portfolio/parte-22/clase-18/`:

- la evaluación de una reserva contra las cuatro reglas, con hallazgos graduados;
- el cálculo de liquidez disponible a un día, una semana y un mes;
- dos escenarios de reembolso con el resultado de cada uno;
- un plan de reembolso ejecutable sin el emisor, con responsable de cada paso.

## 🔗 Referencias cruzadas

- **Viene de:** clase 17 de esta parte; Parte 20, clases 5, 6 y 7.
- **Continúa en:** clase 19 de esta parte, con los regímenes europeos conexos.
- **Se aplica en:** clase 22 de esta parte; Parte 23, clases 6 y 17.

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

- Diario Oficial de la Unión Europea (2023). *Reglamento (UE) 2023/1114 relativo a los mercados de criptoactivos*. EUR-Lex. Obligaciones de reserva, reembolso y gobierno del emisor. <https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32023R1114>
- Autoridad Bancaria Europea. *Regulatory technical standards under MiCAR*. EBA. Normas técnicas que concretan esas obligaciones. <https://www.eba.europa.eu/markets-crypto-assets>
- Financial Stability Board (2023). *High-level Recommendations for the Regulation, Supervision and Oversight of Global Stablecoin Arrangements*. FSB. Referencia internacional con la que se contrasta el régimen. <https://www.fsb.org/2023/07/high-level-recommendations-for-the-regulation-supervision-and-oversight-of-global-stablecoin-arrangements-final-report/>
- Bank for International Settlements — CPMI e IOSCO (2022). *Application of the Principles for Financial Market Infrastructures to stablecoin arrangements*. BIS. Requisitos de infraestructura aplicables al acuerdo de stablecoin. <https://www.bis.org/cpmi/publ/d206.htm>
- Ficha normativa del repositorio: `regulatory/union-europea/mica-reglamento-2023-1114.yml`
- Verificación local: los importes, porcentajes y escenarios de esta clase son **sintéticos** y sirven para enseñar el método, no para describir a ningún emisor real. MiCA no es derecho aplicable en Chile. Las normas técnicas de desarrollo modifican el detalle de la reserva y de los planes: consulta la versión consolidada en EUR-Lex y las directrices de la EBA. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-20.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 17 · MiCA I: perímetro, activos y participantes](17-mica-perimetro-activos-y-participantes.md) | [Parte 22](../README.md) · [Programa](../../../SYLLABUS.md) | [19 · Regímenes europeos conexos: piloto DLT, DORA y regla del viaje →](19-regimenes-europeos-conexos.md) |
<!-- gen:footer:end -->
