<!-- meta
part: 19
class: 1
title: "Sistemas distribuidos aplicados a finanzas"
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
# Clase 01 · Sistemas distribuidos aplicados a finanzas

> [← Índice de la parte](../README.md) · [Índice de la parte](../README.md) · [02 · Resúmenes, firmas y árboles de Merkle →](02-resumenes-firmas-y-arboles-de-merkle.md)

**Parte 19 — Blockchain y DLT para instituciones financieras** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Situar el registro distribuido donde le corresponde: **es un sistema
distribuido con una propiedad concreta y un precio concreto**. Antes de estudiar
sus piezas hay que saber qué problema resuelve y qué cuesta resolverlo así.

La Parte 18 terminó con la liquidación atómica entre infraestructuras. Esta parte estudia la tecnología que la hace posible, y empieza por su fundamento: el problema de ponerse de acuerdo entre participantes que no se fían unos de otros.

## 📚 Objetivos

Al finalizar podrás:

1. **Explicar** qué problema resuelve un registro distribuido, en una frase que
   no incluya la palabra «blockchain».
2. **Aplicar** el compromiso entre consistencia, disponibilidad y tolerancia a
   la partición a un caso financiero.
3. **Distinguir** fallo por caída de fallo bizantino, y decir por qué el segundo
   cambia todo.
4. **Comparar** un registro distribuido con una base de datos compartida usando
   seis criterios medibles.
5. **Decidir** si un caso de uso justifica el coste, con el criterio de las seis
   preguntas.

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

Los cinco primeros términos son el problema de los sistemas distribuidos y sus modos de fallo; los tres siguientes, la tensión que ningún diseño resuelve del todo. El **fallo bizantino** es el que justifica toda la parte: un participante que miente es un problema distinto de uno que se cae, y solo el primero exige el aparato de las trece clases siguientes.

| Concepto | Comprensión verificable |
|---|---|
| `sistema distribuido` | Conjunto de nodos que cooperan sin memoria compartida |
| `replicación` | Cada nodo mantiene una copia del estado |
| `partición de red` | Los nodos no pueden comunicarse entre sí |
| `fallo por caída` | Un nodo deja de responder |
| `fallo bizantino` | Un nodo responde, y responde mal o miente |
| `consistencia` | Todos los nodos ven el mismo estado |
| `disponibilidad` | El sistema responde aunque haya nodos caídos |
| `registro distribuido` | Registro replicado y sincronizado sin autoridad central |

## 🧠 Modelo mental

El modelo mental es una elección forzosa: ante una partición de red, un sistema distribuido puede seguir respondiendo o seguir siendo consistente, y no las dos cosas. En finanzas, la consistencia casi siempre gana, y esa decisión explica por qué estos sistemas son más lentos.

```text
LA FRASE QUE HAY QUE PODER DECIR SIN LA PALABRA «BLOCKCHAIN»

  «permite que partes que no confían entre sí
   ni en un tercero común mantengan un registro
   compartido que ninguna controla»

EL PRECIO DE ESA PROPIEDAD
  · redundancia total: todos guardan todo
  · lentitud: el acuerdo cuesta rondas de mensajes
  · irreversibilidad: el error no se corrige, se compensa
  · coste de consenso: energía, capital comprometido o votos

LA PREGUNTA QUE ORDENA TODA LA PARTE
  ¿existe en este caso un tercero de confianza disponible?
    SÍ  → una base de datos compartida es más rápida,
          más barata y CORREGIBLE
    NO  → el precio puede compensar
```

## 📖 Desarrollo

### 1. El compromiso fundamental

Todo sistema repartido entre varias máquinas se topa con la misma disyuntiva
en cuanto la red falla. El bloque la enuncia y explica por qué en finanzas la
elección está prácticamente decidida de antemano.

```text
CUANDO LA RED SE PARTE, HAY QUE ELEGIR

  CONSISTENCIA   todos ven lo mismo, pero el sistema
                 deja de responder hasta que se repara
  DISPONIBILIDAD el sistema responde, pero dos nodos
                 pueden dar respuestas distintas

  NO SE PUEDEN TENER LAS DOS DURANTE UNA PARTICIÓN

EN FINANZAS, LA ELECCIÓN CASI SIEMPRE ES CONSISTENCIA
  un sistema de pagos que responde «pagado» a los dos
  lados de una partición ha creado dinero

  → por eso los sistemas de liquidación prefieren
    detenerse a divergir
```

### 2. Fallo por caída y fallo bizantino

Un nodo puede fallar callándose o fallar hablando, y la diferencia decide
cuántos nodos hacen falta para tolerarlo. El bloque define ambos modos con su
umbral y explica qué se pierde al pasar del primero al segundo.

```text
FALLO POR CAÍDA
  el nodo deja de responder
  el resto lo detecta por ausencia
  tolerar f caídas exige 2f + 1 nodos

FALLO BIZANTINO
  el nodo RESPONDE, y responde mal:
  puede mentir, contradecirse o decir cosas distintas
  a distintos interlocutores

  tolerar f bizantinos exige 3f + 1 nodos

POR QUÉ ESO CAMBIA TODO
  con caídas, el silencio es información
  con bizantinos, ninguna respuesta individual
  es información: hay que contrastar

EN UN CONSORCIO FINANCIERO
  ¿los participantes pueden mentir?
  no por malicia necesariamente: basta un fallo de software
  que produzca respuestas incoherentes
  → se diseña para bizantino, no para caída
```

### 3. Los seis criterios de comparación

| Criterio | Base de datos compartida | Registro distribuido |
|---|---|---|
| Quién controla el estado | Un operador | Ninguno en solitario |
| Corrección de un error | Actualización, con traza | Compensación, no corrección |
| Latencia de escritura | Milisegundos | Segundos o minutos |
| Coste por operación | Bajo | Alto |
| Verificación por un tercero | Requiere confiar en el operador | Independiente |
| Qué pasa si el operador desaparece | El sistema muere | El sistema sigue |

```text
LAS DOS FILAS QUE DECIDEN
  «verificación por un tercero» y «si el operador desaparece»

  si a la institución le da igual confiar en el operador
  y el operador no va a desaparecer,
  las otras cuatro filas favorecen a la base de datos
```

### 4. Las seis preguntas del criterio

Antes de elegir tecnología conviene saber qué problema se está resolviendo,
porque solo uno de los seis posibles justifica un registro distribuido. El
bloque plantea las preguntas en el orden en que conviene hacérselas.

```text
ANTES DE DISEÑAR NADA, RESPONDER

  1. ¿EL PROBLEMA ES DE CONFIANZA?
     ¿hay partes que no confían y no aceptan un tercero?
  2. ¿EL PROBLEMA ES DE COORDINACIÓN?
     ¿el coste está en ponerse de acuerdo, no en confiar?
  3. ¿EL PROBLEMA ES DE DATOS?
     ¿lo que falta es un formato común?
  4. ¿EL PROBLEMA ES DE PROCESO?
     ¿el coste está en pasos manuales evitables?
  5. ¿EL PROBLEMA ES REGULATORIO?
     ¿la fricción viene de una obligación, no de la técnica?
  6. ¿EL PROBLEMA ES DE LIQUIDEZ?
     ¿lo caro es el capital inmovilizado?

  SOLO LA 1 JUSTIFICA POR SÍ SOLA UN REGISTRO DISTRIBUIDO.
  Las otras cinco tienen soluciones más baratas,
  y confundirlas con la 1 es el error del que salen
  casi todos los proyectos fallidos.
```

### 5. Lo que un registro distribuido no arregla

La lista de lo que esta tecnología no resuelve es tan útil como la de lo que
resuelve, y más corta de encontrar en la bibliografía. El bloque la recoge y
añade los tres problemas nuevos que aparecen al adoptarla.

```text
NO ARREGLA
  · un dato de mala calidad: lo replica igual de malo
  · un proceso mal diseñado: lo automatiza igual de mal
  · una obligación regulatoria: sigue estando
  · la falta de acuerdo entre partes: lo exige antes
  · la identidad: hay que resolverla fuera
  · la conexión con el mundo físico: eso son los oráculos

Y AÑADE
  · irreversibilidad: el error se vuelve permanente
  · dependencia de claves: perderlas es perder el acceso
  · riesgo de gobernanza: quién decide cuando hay que cambiar
```

## 🧮 Ejemplo guiado

El ejemplo compara el comportamiento de dos diseños ante una partición. Conviene fijarse en qué sacrifica cada uno: no hay un diseño que no sacrifique nada.

**Situación.** Cuatro bancos quieren compartir el registro de garantías
constituidas sobre bienes muebles, hoy repartido en cuatro sistemas que no se
hablan. Hay que decidir la arquitectura.

```text
SITUACIÓN ACTUAL
  garantías registradas al año           42 000
  duplicidades detectadas (misma garantía
  pignorada dos veces sin saberlo)          310
  pérdida media por duplicidad          180 000
  coste anual de conciliación manual  1 400 000
  tiempo medio de verificación           3,2 días

EXISTE UN REGISTRO PÚBLICO NACIONAL
  cobertura: solo bienes inscribibles (58 % de los casos)
  actualización: 5 días hábiles
  consulta: de pago, 4 200 por consulta
```

**Paso 1 — cuantifica el problema.**

```text
PÉRDIDA POR DUPLICIDADES
  310 × 180 000 = 55 800 000 al año

COSTE DE CONCILIACIÓN
  1 400 000 al año

COSTE DE CONSULTA AL REGISTRO PÚBLICO
  42 000 × 58 % × 4 200 = 102 312 000 al año

COSTE TOTAL DEL PROBLEMA: 159 512 000
```

**Paso 2 — aplica las seis preguntas.**

```text
1. ¿CONFIANZA?
   ¿un banco aceptaría que otro opere el registro común?
   respuesta de los cuatro: NO, por riesgo competitivo
   → SÍ hay problema de confianza

2. ¿COORDINACIÓN?
   sí: nadie quiere ser el primero en publicar sus garantías

3. ¿DATOS?
   sí: cuatro formatos distintos de identificar un bien

4. ¿PROCESO?
   sí: 3,2 días de verificación manual

5. ¿REGULATORIO?
   parcialmente: la publicidad de la garantía tiene
   requisitos legales que hay que respetar

6. ¿LIQUIDEZ?
   no
```

**Paso 3 — no te quedes con «sí hay confianza».**

```text
LA PREGUNTA 1 SE RESPONDIÓ «NO ACEPTARÍAN QUE OTRO OPERE».
ESO NO ES LO MISMO QUE «NO EXISTE UN TERCERO DE CONFIANZA».

  ¿aceptarían un TERCERO NEUTRAL?
    · una cámara de compensación existente
    · una entidad conjunta creada al efecto
    · el propio registro público, si mejorara

  PREGUNTA A LOS CUATRO
    ¿aceptarían una sociedad conjunta con gobierno paritario
    operando una base de datos compartida?
    respuesta: SÍ, tres de los cuatro

  → la pregunta 1 NO estaba respondida:
    hay tercero de confianza posible
```

**Paso 4 — compara las dos arquitecturas con números.**

```text
OPCIÓN A · SOCIEDAD CONJUNTA CON BASE DE DATOS COMPARTIDA
  constitución y gobierno          2 800 000 inicial
  desarrollo                       4 200 000 inicial
  operación anual                  1 900 000
  auditoría independiente anual      600 000
  TOTAL AÑO 1                      9 500 000
  TOTAL AÑOS SIGUIENTES            2 500 000

OPCIÓN B · RED AUTORIZADA CON REGISTRO DISTRIBUIDO
  diseño y gobernanza del consorcio 3 400 000 inicial
  desarrollo                        7 800 000 inicial
  operación de nodos (4 × 620 000)  2 480 000 anual
  auditoría de contratos anual        900 000
  TOTAL AÑO 1                      14 580 000
  TOTAL AÑOS SIGUIENTES             3 380 000
```

**Paso 5 — evalúa el beneficio, que es el mismo en ambas.**

```text
LAS DOS OPCIONES ELIMINAN
  duplicidades (supuesto: 92 %)     51 336 000
  conciliación manual (85 %)         1 190 000
  consultas al registro público (70 %) 71 618 400
  BENEFICIO ANUAL                  124 144 400

  las dos, IGUAL. La tecnología no cambia el beneficio:
  lo cambia tener un registro común

RETORNO
  Opción A: 9 500 000 / 124 144 400 → 28 días
  Opción B: 14 580 000 / 124 144 400 → 43 días

  las dos son claramente rentables
```

**Paso 6 — decide con la fila que las distingue.**

```text
SI EL BENEFICIO ES IGUAL, LA DECISIÓN ESTÁ EN LOS SEIS CRITERIOS

  verificación por un tercero
    A: hay que confiar en la sociedad conjunta y su auditoría
    B: cada banco verifica por sí mismo

  si el operador desaparece
    A: el registro queda en manos de la liquidación de la sociedad
    B: los nodos siguen

  corrección de un error
    A: se corrige con traza  ← VENTAJA DE A
    B: se compensa, no se corrige

  latencia y coste
    A: mejores  ← VENTAJA DE A

DECISIÓN: OPCIÓN A, LA SOCIEDAD CONJUNTA

  MOTIVO
    tres de los cuatro aceptan el tercero neutral.
    Con tercero disponible, el registro distribuido
    paga su precio sin obtener su beneficio.

  CONDICIÓN QUE CAMBIARÍA LA DECISIÓN
    si el cuarto banco no entra, o si se incorporan
    participantes de otras jurisdicciones que no acepten
    la sociedad conjunta, la pregunta 1 se responde
    distinto y la opción B vuelve a la mesa.

  Y UNA CLÁUSULA DE DISEÑO
    la opción A se construye con el estado del registro
    exportable y firmado, para que migrar a B
    no exija empezar de cero.
```

**Interpreta:** el proyecto tenía un caso de uso excelente y **la tecnología no
era la decisión**. El beneficio venía de tener un registro común; la elección
entre las dos arquitecturas dependía de si existía un tercero aceptable, y la
primera respuesta —«no confiamos en que otro lo opere»— no era la respuesta a
esa pregunta.

## 🧭 Perspectivas

Un registro distribuido significa cosas distintas para cada participante del sistema financiero. La tabla las recoge, y conviene volver a ella al final de la parte.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Una garantía verificada en horas | Si acepta la operación |
| Banco participante | 180 000 de pérdida por duplicidad | Si entra en el consorcio |
| Banco no participante | Un registro al que no accede | Si se une o compite |
| Registro público | Consultas que dejan de llegar | Si mejora su servicio |
| Tecnología | Dos arquitecturas con coste distinto | Cuál construye |
| Riesgo operacional | Irreversibilidad frente a corregibilidad | Qué controles exige |
| Supervisor | Registro privado de garantías | Si lo vigila |
| Auditor | Verificación independiente | Qué evidencia acepta |

## 🏦 Del cliente al banco

El cliente no ve nada de esto y su operación depende de qué garantías eligió el diseño. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Mi garantía tardó tres días» | Verificación manual entre cuatro sistemas | 19, clase 1 |
| «Me pidieron un bien ya pignorado» | Duplicidad no detectada | 19, clase 1 |
| «El registro no está actualizado» | Cinco días hábiles de desfase | 19, clase 1 |

## ⚖️ Riesgos y controles

Los riesgos son de consistencia y de disponibilidad, y reducir uno aumenta el otro. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Pregunta 1 mal respondida | Se confunde «no confío en ese» con «no hay tercero» | Preguntar por el tercero neutral |
| Irreversibilidad | Un error queda permanente | Diseño de compensación desde el inicio |
| Coste de consenso subestimado | Operar nodos cuesta más de lo previsto | Coste por nodo y por año, medido |
| Divergencia en partición | Dos nodos con estados distintos | Elegir consistencia sobre disponibilidad |
| Fallo bizantino no previsto | Un nodo responde mal, no calla | Diseñar para 3f + 1 |
| Dependencia sin salida | Migrar exige empezar de cero | Estado exportable y firmado |

## 🧪 Práctica

En [`labs/lab-01.md`](../labs/lab-01.md) y [`labs/lab-06.md`](../labs/lab-06.md):

1. Aplica las seis preguntas a tres casos de uso reales de tu entorno.
2. Compara las dos arquitecturas con los seis criterios y con números.
3. Mide latencia y coste por operación de ambas.
4. Escribe la condición que cambiaría tu decisión.

## ⚠️ Errores frecuentes

La tabla se usa buscando el síntoma. En esta clase casi todos vienen de haber supuesto garantías que el diseño no da.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| «No confiamos en ellos» como respuesta 1 | Se preguntó por un participante | Pregunta por un tercero neutral |
| Atribuir el beneficio a la tecnología | No se comparó la alternativa | El beneficio suele venir del registro común |
| Diseñar para caídas | Se subestimó el fallo bizantino | 3f + 1, no 2f + 1 |
| Elegir disponibilidad en un sistema de pagos | Se copió un criterio web | Consistencia: divergir es crear dinero |
| Ignorar el coste de operar nodos | Solo se contó el desarrollo | Coste por nodo y año |
| No prever la corrección de errores | Se asumió que no habría | Compensación diseñada de antemano |

## ❓ Preguntas de comprobación

1. Di en una frase qué resuelve un registro distribuido, sin usar la palabra
   «blockchain».
2. ¿Por qué un sistema de pagos elige consistencia sobre disponibilidad ante una
   partición?
3. ¿Qué diferencia hay entre 2f + 1 y 3f + 1, y de qué depende cuál aplica?
4. ¿Cuál de las seis preguntas justifica por sí sola un registro distribuido?
5. En el ejemplo guiado, ¿por qué la primera respuesta a la pregunta 1 no era
   una respuesta?

## 📥 Entregable

Guarda en `portfolio/parte-19/clase-01/`:

- las seis preguntas aplicadas a tres casos de uso de tu entorno;
- la comparación de dos arquitecturas con los seis criterios y con números;
- la decisión, con la condición explícita que la cambiaría;
- la lista de lo que la tecnología **no** arregla en tu caso.

## 🔗 Referencias cruzadas

- **Viene de:** Parte 14, clase 9 (criptoactivos y registro distribuido);
  Parte 11, clase 12 (riesgo operacional).
- **Continúa en:** clase 5 (consenso), clase 6 (finalidad), clase 7 (tipos de
  red).
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

- Committee on Payments and Market Infrastructures (2017). *Distributed ledger technology in payment, clearing and settlement: an analytical framework*. BIS. <https://www.bis.org/cpmi/publ/d157.htm>
- Lamport, L., Shostak, R. y Pease, M. (1982). *The Byzantine Generals Problem*. ACM TOPLAS. <https://dl.acm.org/doi/10.1145/357172.357176>
- Gilbert, S. y Lynch, N. (2002). *Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services*. ACM SIGACT News.
- NIST (2018). *NISTIR 8202: Blockchain Technology Overview*. National Institute of Standards and Technology. <https://csrc.nist.gov/pubs/ir/8202/final>
- ISO/TC 307. *Blockchain and distributed ledger technologies: vocabulario y marcos de referencia*. ISO. <https://www.iso.org/committee/6266604.html>
- Verificación local: comprueba si tu supervisor ha publicado criterios sobre el uso de tecnología de registro distribuido en infraestructuras financieras. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← Índice de la parte](../README.md) | [Parte 19](../README.md) · [Programa](../../../SYLLABUS.md) | [02 · Resúmenes, firmas y árboles de Merkle →](02-resumenes-firmas-y-arboles-de-merkle.md) |
<!-- gen:footer:end -->
