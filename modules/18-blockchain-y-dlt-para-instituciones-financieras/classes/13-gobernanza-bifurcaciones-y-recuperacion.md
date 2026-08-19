<!-- meta
part: 19
class: 13
title: "Gobernanza, bifurcaciones y recuperación"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global]
regulatory_topics: [dlt, gobernanza, resiliencia-operacional]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [CPMI, IOSCO]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 13 · Gobernanza, bifurcaciones y recuperación

> [← 12 · Escalabilidad, capas y disponibilidad](12-escalabilidad-capas-y-disponibilidad.md) · [Índice de la parte](../README.md) · [14 · Proyecto: red financiera autorizada →](14-proyecto-red-financiera-autorizada.md)

**Parte 19 — Blockchain y DLT para instituciones financieras** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Responder la pregunta que ninguna arquitectura resuelve: **¿quién decide cuando
hay que cambiar algo, y qué se hace cuando ya ha ocurrido un desastre?** La
irreversibilidad convierte la gobernanza en el control más importante de todos.

Todo lo construido hasta aquí necesita poder cambiar. Esta clase trata de cómo, y plantea la pregunta que casi ninguna red tiene resuelta por escrito: quién decide, con qué mayoría y qué pasa con quien pierde.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** gobernanza del protocolo, de la aplicación y del consorcio.
2. **Explicar** qué es una bifurcación y por qué no siempre es un accidente.
3. **Diseñar** el procedimiento de cambio de reglas de una red autorizada.
4. **Especificar** un plan de recuperación ante un error irreversible.
5. **Evaluar** el dilema de revertir: qué se gana y qué se destruye.

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

Los cuatro primeros términos son el gobierno y sus formas de cambio; los cuatro siguientes, la reversión y su coste. La **bifurcación incompatible** es la que obliga a todos a actualizarse a la vez, y coordinar eso en una red con participantes independientes es un problema de gobierno y no técnico.

| Concepto | Comprensión verificable |
|---|---|
| `gobernanza` | Quién decide las reglas y con qué procedimiento |
| `bifurcación compatible` | Cambio que los nodos antiguos siguen aceptando |
| `bifurcación incompatible` | Cambio que exige que todos actualicen |
| `bifurcación de cadena` | Dos historias que coexisten y no se reconcilian |
| `reversión` | Deshacer operaciones ya consideradas finales |
| `compensación` | Corregir el efecto sin deshacer el registro |
| `plan de recuperación` | Procedimiento previsto ante un fallo grave |
| `parada coordinada` | Detener la red de forma acordada |

## 🧠 Modelo mental

El modelo mental es que un registro inmutable sí se puede cambiar, pero solo por acuerdo. La pregunta no es si se puede revertir sino quién decide revertir, con qué mayoría y con qué compensación a quien pierda.

```text
TRES GOBERNANZAS QUE SE CONFUNDEN

  DEL PROTOCOLO      quién puede cambiar las reglas
                     de la red
  DE LA APLICACIÓN   quién puede cambiar un contrato
                     concreto (clase 8)
  DEL CONSORCIO      quién admite, expulsa y resuelve
                     disputas (clase 7)

  UNA RED PUEDE TENER GOBERNANZA DE CONSORCIO
  IMPECABLE Y GOBERNANZA DE APLICACIÓN INEXISTENTE

LA PREGUNTA QUE LAS ORDENA
  «si mañana hay que cambiar X, ¿quién decide,
   con qué mayoría, en cuánto tiempo, y qué pasa
   con quien no está de acuerdo?»
```

## 📖 Desarrollo

### 1. Los dos tipos de cambio

Un cambio de reglas puede ser compatible con los nodos antiguos o no serlo, y
de eso depende si se puede desplegar por etapas. El bloque define ambos tipos
y matiza qué cambia en una red de participantes conocidos.

```text
BIFURCACIÓN COMPATIBLE
  el cambio restringe lo que antes era válido
  los nodos antiguos siguen aceptando los bloques nuevos
  → se puede desplegar de forma gradual

BIFURCACIÓN INCOMPATIBLE
  el cambio amplía lo que es válido, o cambia una regla
  los nodos antiguos RECHAZAN los bloques nuevos
  → si no actualizan todos, la red se parte

EN UNA RED AUTORIZADA
  se puede coordinar: los participantes son conocidos
  → la bifurcación incompatible es gestionable
    con preaviso y ventana de actualización

EN UNA RED ABIERTA
  no se puede obligar a nadie
  → una bifurcación incompatible sin consenso social
    produce dos cadenas, y ambas siguen
```

### 2. Qué es realmente una bifurcación de cadena

Una bifurcación de cadena no es una avería: es un desacuerdo que el software
se limita a ejecutar. El bloque lo explica y enumera las preguntas que abre
inmediatamente en el balance de una institución.

```text
NO ES UN FALLO TÉCNICO: ES UN DESACUERDO

  un grupo cree que la regla debe ser A
  otro cree que debe ser B
  ambos siguen produciendo bloques

  RESULTADO
    dos historias que comparten pasado y divergen
    los activos «existen» en las dos

CONSECUENCIAS PARA UNA INSTITUCIÓN
  · ¿cuál es el activo del balance?
  · ¿qué precio se usa para cada uno?
  · ¿el contrato con el cliente se refiere a cuál?
  · ¿hay riesgo de repetición entre cadenas?

  NINGUNA ES TÉCNICA, Y HAY QUE RESPONDERLAS
  ANTES, EN LA POLÍTICA DE LA ENTIDAD
```

### 3. El dilema de revertir

Cuando un defecto destruye fondos, la comunidad puede coordinarse para
deshacerlo, y ahí empieza la discusión. El bloque recoge los argumentos de las
dos partes sin resolverla, porque la decisión es de gobierno, no técnica.

```text
OCURRE UN DEFECTO Y SE PIERDEN FONDOS.
LA COMUNIDAD PUEDE COORDINARSE PARA DESHACERLO.

  A FAVOR
    · se repara el daño a las víctimas
    · el defecto no era culpa de ellas
    · la alternativa es una pérdida enorme

  EN CONTRA
    · la irreversibilidad era la propiedad del sistema
    · si se revierte una vez, se puede revertir siempre
    · ¿quién decide qué pérdida merece reversión?
    · quien confió en la irreversibilidad la pierde

NO HAY RESPUESTA CORRECTA UNIVERSAL.
Lo que sí es incorrecto es no haberlo decidido antes.

EN UNA RED FINANCIERA AUTORIZADA
  la respuesta razonable suele ser: NO se revierte
  el registro; se COMPENSA fuera de él, con un fondo
  o con la responsabilidad de quien corresponda
  → el registro conserva su propiedad y el daño
    se repara por la vía contractual
```

### 4. Compensación frente a reversión

Existe una salida intermedia que la contabilidad lleva siglos usando: en vez
de borrar el error, se registra su corrección. El bloque compara ambas vías y
enumera las ventajas de la segunda.

```text
REVERSIÓN
  se cambia la historia
  destruye la propiedad del sistema

COMPENSACIÓN
  se añade una operación que corrige el efecto
  la historia queda: se ve el error y se ve la corrección

  VENTAJAS
    · auditable: queda constancia de lo ocurrido
    · no exige coordinar a todos los nodos
    · compatible con la contabilidad, que también
      corrige con asientos, no borrando

LA COMPENSACIÓN ES LA RESPUESTA CONTABLE
Y ES LA CORRECTA AQUÍ POR LA MISMA RAZÓN:
un registro que se puede reescribir no es un registro
```

### 5. El plan de recuperación

El plan de recuperación se escribe en frío y se ejecuta en caliente, así que
debe responder por escrito a preguntas concretas. El bloque las enumera en el
orden en que se plantean durante un incidente real.

```text
QUÉ TIENE QUE RESPONDER, POR ESCRITO

  1. QUÉ ACTIVA EL PLAN
     defecto explotado, bifurcación, pérdida de quórum,
     compromiso de claves
  2. QUIÉN LO ACTIVA
     nunca una sola persona
  3. QUÉ SE HACE PRIMERO
     normalmente, PARAR: el interruptor de la clase 8
  4. CÓMO SE PARA DE FORMA COORDINADA
     todos los nodos, con constancia del punto de parada
  5. QUIÉN EVALÚA Y EN CUÁNTO TIEMPO
  6. QUÉ OPCIONES SE CONTEMPLAN
     compensación, actualización, reanudación parcial
  7. CÓMO SE COMUNICA A CLIENTES Y AL SUPERVISOR
  8. CADA CUÁNTO SE ENSAYA

EL PUNTO 3 ES CONTRAINTUITIVO Y CORRECTO
  la reacción natural es «arreglarlo cuanto antes»;
  la correcta es detener el daño y luego decidir
  sin prisa
```

## 🧮 Ejemplo guiado

El ejemplo evalúa una propuesta de reversión con sus perjudicados. Conviene identificar quién decide: en casi todas las redes esa respuesta no está escrita.

**Situación.** En la red autorizada del consorcio, un defecto en el contrato de
depósito en garantía ha permitido a un participante retirar 6 400 000 que no le
correspondían. El error se detecta 40 minutos después.

```text
ESTADO
  fondos retirados                6 400 000
  fondos aún en el contrato      21 600 000
  operaciones afectadas                  38
  participantes afectados                 5
  el retirante es un participante identificado
  el defecto es del contrato, no del registro
```

**Paso 1 — aplica el punto 3 del plan.**

```text
PRIMERO: PARAR

  el interruptor de emergencia del contrato
  se activa con firma 2-de-3 de operaciones

  EFECTO
    no se pueden hacer más retiradas
    los 21 600 000 restantes quedan protegidos

  TIEMPO OBJETIVO: menos de 10 minutos desde la detección

  LO QUE NO SE HACE EN ESTE MOMENTO
    · no se decide qué hacer con los 6 400 000
    · no se comunica públicamente todavía
    · no se toca el registro
```

**Paso 2 — evalúa las opciones sobre los 6,4 millones.**

```text
OPCIÓN A · REVERTIR EL REGISTRO
  coordinar a los 5 nodos para deshacer los bloques
  desde la retirada

  COSTE
    · destruye la propiedad de irreversibilidad
    · sienta el precedente: ¿cuál es el umbral
      a partir del cual se revierte?
    · afecta a las 38 operaciones, incluidas las
      legítimas posteriores

OPCIÓN B · COMPENSAR EN EL REGISTRO
  el retirante devuelve; si no, se ejecuta la garantía
  que aportó al entrar en el consorcio

  COSTE
    · depende de que la garantía cubra
    · deja constancia del incidente

OPCIÓN C · RECLAMAR FUERA DEL REGISTRO
  vía contractual y, si hace falta, judicial

  COSTE
    · lento
    · incierto si el participante es insolvente
```

**Paso 3 — comprueba si la garantía cubre.**

```text
GARANTÍA APORTADA POR CADA PARTICIPANTE
AL ENTRAR EN EL CONSORCIO: 2 000 000

  6 400 000 > 2 000 000
  → la garantía cubre el 31 %

HALLAZGO DE DISEÑO
  la garantía se dimensionó por «riesgo operativo
  esperado» y no por exposición máxima de un
  contrato del consorcio

  → es el mismo error de la clase 3: dimensionar
    por lo típico y no por lo posible
```

**Paso 4 — decide la respuesta inmediata.**

```text
OPCIÓN B + C, EN ESTE ORDEN

  1. requerimiento formal de devolución en 48 horas
  2. si no devuelve, ejecución de la garantía
     (2 000 000) y suspensión como participante
  3. reclamación por los 4 400 000 restantes
     por la vía contractual
  4. el registro NO se toca

  Y SE COMUNICA
    · a los 5 participantes afectados, de inmediato
    · al supervisor, en el plazo que exija la norma
    · a los clientes de los participantes afectados,
      con el importe y el plan
```

**Paso 5 — decide la reanudación.**

```text
NO SE REANUDA HASTA QUE

  1. el defecto esté corregido y auditado
  2. las 38 operaciones afectadas estén revisadas
     una a una
  3. exista un límite de saldo del contrato
     mientras dura la vigilancia reforzada
  4. el comité apruebe con la evidencia delante

  TIEMPO ESTIMADO: 3 a 6 semanas

  MIENTRAS TANTO
    las operaciones de garantía se tramitan
    por el procedimiento anterior, manual
    → hay que tenerlo, y por eso no se desmantela
      el proceso antiguo el día del despliegue
```

**Paso 6 — extrae los cambios de gobernanza.**

```text
LO QUE ESTE INCIDENTE OBLIGA A CAMBIAR

  1. GARANTÍA POR EXPOSICIÓN, NO POR RIESGO ESPERADO
     cada participante aporta garantía ≥ exposición
     máxima que puede generar en un contrato

  2. LÍMITE DE SALDO POR CONTRATO
     ningún contrato acumula más de X sin aprobación
     específica del comité

  3. DESPLIEGUE POR FASES OBLIGATORIO
     el límite de la fase 1 se levanta por evidencia,
     no por calendario (clase 8)

  4. POLÍTICA ESCRITA DE NO REVERSIÓN
     «el registro no se revierte; los daños se
     compensan por la vía contractual»
     → decidido ANTES del próximo incidente

  5. ENSAYO SEMESTRAL DEL PLAN
     con parada real en preproducción
```

**Paso 7 — escribe lo que el incidente demostró.**

```text
LO QUE FUNCIONÓ
  · el interruptor de emergencia existía y se activó
    en 8 minutos
  · la parada protegió 21 600 000

LO QUE FALLÓ
  · el contrato tenía un defecto que la revisión
    no detectó
  · la garantía estaba mal dimensionada
  · no había política escrita sobre reversión,
    y se perdieron 3 horas discutiéndolo

LO QUE HAY QUE DECIR AL COMITÉ
  el sistema perdió 4 400 000 no recuperados
  y evitó perder 21 600 000 gracias a un control
  que existía porque alguien lo exigió antes.

  La diferencia entre las dos cifras es el valor
  de tener el plan escrito.
```

**Interpreta:** el incidente lo causó un defecto de código y lo contuvo una
decisión de gobernanza tomada meses antes. Las tres horas perdidas discutiendo si
revertir **eran evitables**: esa decisión se toma cuando no hay dinero encima de
la mesa.

## 🧭 Perspectivas

La gobernanza afecta a cada participante de forma muy distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Participante afectado | Fondos retirados por otro | Si reclama o sale |
| Participante retirante | Un requerimiento en 48 horas | Si devuelve |
| Consorcio | Un incidente de 6,4 M | Si revierte o compensa |
| Cliente | Un servicio detenido | Si confía |
| Supervisor | Un incidente comunicado | Si abre expediente |
| Auditor | Revisión que no detectó el defecto | Qué informa |
| Comité | 4,4 M perdidos, 21,6 M salvados | Qué cambia |

## 🏦 Del cliente al banco

El cliente confía en la inmutabilidad y la red puede cambiar por acuerdo. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «El servicio está parado» | Interruptor activado: es lo correcto | 19, clase 13 |
| «¿Van a deshacerlo?» | Se compensa, no se revierte | 19, clase 13 |
| «Volvió a funcionar rápido» | No se reanuda por calendario | 19, clase 13 |

## ⚖️ Riesgos y controles

Los riesgos son de gobierno y de coordinación. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Sin política de reversión | Se discute con el reloj en marcha | Decidirlo antes por escrito |
| Garantía mal dimensionada | No cubre la exposición posible | Garantía por exposición máxima |
| Sin interruptor | El daño sigue mientras se decide | Parar primero |
| Bifurcación no prevista | Dos activos en balance | Política de entidad escrita |
| Reanudación por calendario | Se vuelve con el defecto | Reanudar por evidencia |
| Proceso antiguo desmantelado | No hay a dónde volver | Mantenerlo durante la fase 1 |

## 🧪 Práctica

En [`labs/lab-05.md`](../labs/lab-05.md) y el [proyecto](../project/README.md):

1. Escribe el plan de recuperación con sus ocho puntos.
2. Simula un incidente y mide el tiempo hasta la parada.
3. Redacta la política de reversión de tu entidad.
4. Dimensiona la garantía por exposición máxima, no por riesgo esperado.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen crisis de gobernanza. La causa es no haber decidido de antemano quién decide.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Arreglar antes de parar | Reacción natural | Parar, luego decidir |
| Discutir la reversión durante el incidente | No había política | Decidirlo antes |
| Garantía por riesgo esperado | Se dimensionó por lo típico | Por exposición máxima |
| Reanudar por calendario | Presión comercial | Por evidencia |
| Plan sin ensayo | Se documentó | Semestral con parada real |
| Confundir las tres gobernanzas | Se resolvió una | Protocolo, aplicación y consorcio |

## ❓ Preguntas de comprobación

1. ¿Cuáles son las tres gobernanzas y qué pregunta las ordena?
2. ¿Qué diferencia hay entre una bifurcación compatible y una incompatible?
3. ¿Por qué la compensación es preferible a la reversión en una red financiera?
4. ¿Por qué el primer paso de un plan de recuperación es parar?
5. En el ejemplo guiado, ¿qué demostró la diferencia entre 4,4 y 21,6 millones?

## 📥 Entregable

Guarda en `portfolio/parte-19/clase-13/`:

- el plan de recuperación con sus ocho puntos respondidos;
- la política de reversión de tu entidad, redactada;
- el dimensionamiento de la garantía por exposición máxima;
- el resultado de un simulacro, con el tiempo hasta la parada.

## 🔗 Referencias cruzadas

- **Viene de:** clases 6, 7, 8 y 12; Parte 17, clase 13 (incidentes).
- **Continúa en:** clase 14 (proyecto).
- **Se aplica en:** Parte 22, clase 15; Parte 23, clases 16 y 17.

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

- Committee on Payments and Market Infrastructures e IOSCO (2016). *Guidance on cyber resilience for financial market infrastructures*. BIS. Expectativas de recuperación tras un incidente en la infraestructura. <https://www.bis.org/cpmi/publ/d146.htm>
- Basel Committee on Banking Supervision (2021). *Principles for operational resilience*. BIS. Tolerancia a la interrupción aplicada a la red autorizada. <https://www.bis.org/bcbs/publ/d516.htm>
- IOSCO (2022). *Decentralized Finance Report*. IOSCO. Gobernanza observada en redes sin permiso y sus fallos. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD699.pdf>
- Committee on Payments and Market Infrastructures (2017). *Distributed ledger technology in payment, clearing and settlement: an analytical framework*. BIS. Mecánica de la bifurcación y sus consecuencias contables. <https://www.bis.org/cpmi/publ/d157.htm>
- Financial Stability Board (2023). *Enhancing third-party risk management and oversight: a toolkit*. FSB. Responsabilidad sobre operadores y desarrolladores de la red. <https://www.fsb.org/2023/12/enhancing-third-party-risk-management-and-oversight-a-toolkit-for-financial-institutions-and-financial-authorities/>
- Verificación local: comprueba los plazos y umbrales de comunicación de incidentes de tu jurisdicción, y si existe criterio sobre el tratamiento de una bifurcación. **Fecha de verificación de esta clase: 2026-08-06.** Esta clase no constituye asesoría legal.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 12 · Escalabilidad, capas y disponibilidad](12-escalabilidad-capas-y-disponibilidad.md) | [Parte 19](../README.md) · [Programa](../../../SYLLABUS.md) | [14 · Proyecto: red financiera autorizada →](14-proyecto-red-financiera-autorizada.md) |
<!-- gen:footer:end -->
