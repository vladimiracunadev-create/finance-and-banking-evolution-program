<!-- meta
part: 18
class: 5
title: "Mensajería frente a movimiento de fondos"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global]
regulatory_topics: [cross-border-payments, infraestructura]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [CPMI]
requires_legal_review: false
-->

<!-- gen:header:start -->
# Clase 05 · Mensajería frente a movimiento de fondos

> [← 04 · Cuentas nostro, vostro y loro](04-cuentas-nostro-vostro-y-loro.md) · [Índice de la parte](../README.md) · [06 · SWIFT, CBPR+ e ISO 20022 →](06-swift-cbpr-e-iso-20022.md)

**Parte 18 — Pagos transfronterizos, remesas y liquidación internacional** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Desmontar la confusión más extendida del área: **SWIFT no mueve dinero**. Es una
red de mensajería. El dinero se mueve en cuentas y se liquida en sistemas de
pago. De esa distinción dependen el diagnóstico de la lentitud y la elección de
cualquier arquitectura alternativa.

Las clases anteriores describen la infraestructura. Esta separa dos cosas que se confunden todo el tiempo y que viajan por vías distintas: la instrucción de pago y el dinero. Un mensaje entregado no es un pago hecho.

## 📚 Objetivos

Al finalizar podrás:

1. **Separar** red de mensajería, sistema de liquidación y libro contable.
2. **Explicar** qué garantiza y qué no garantiza la entrega de un mensaje.
3. **Trazar** el desfase entre el momento del mensaje y el de la liquidación.
4. **Evaluar** qué parte del retraso de un pago es atribuible a cada capa.
5. **Identificar** qué mejora realmente una arquitectura que promete rapidez.

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

Los cuatro primeros términos separan la instrucción del dinero; los cuatro siguientes, los plazos que produce esa separación. El **desfase mensaje-fondos** es el concepto central: el mensaje llega en segundos y los fondos pueden tardar días, y confundir uno con otro es el error más frecuente de esta parte.

| Concepto | Comprensión verificable |
|---|---|
| `red de mensajería` | Infraestructura que transporta instrucciones entre bancos |
| `sistema de liquidación` | Infraestructura donde los fondos cambian de titular |
| `libro contable` | Registro de cada banco sobre sus propias posiciones |
| `entrega garantizada` | El mensaje llegó, íntegro y autenticado |
| `desfase mensaje-fondos` | Tiempo entre la instrucción y la liquidación efectiva |
| `ventana operativa` | Horario en que un sistema de liquidación acepta operaciones |
| `día inhábil` | Día en que una plaza no liquida |
| `fecha valor` | Día en que el importe produce efectos económicos |

## 🧠 Modelo mental

El modelo mental son dos vías paralelas que no se mueven al mismo ritmo: la mensajería lleva la instrucción y la liquidación mueve el dinero. Un mensaje entregado no significa un pago hecho.

```text
TRES CAPAS QUE SE CONFUNDEN CONSTANTEMENTE

  CAPA 1 · MENSAJERÍA
    qué hace     transporta una instrucción autenticada
    quién es     redes financieras, APIs, ficheros
    garantiza    que el mensaje llegó, íntegro y de quien dice
    NO garantiza que haya fondos, ni que se paguen

  CAPA 2 · LIQUIDACIÓN
    qué hace     transfiere la titularidad de los fondos
    quién es     sistemas de liquidación bruta en tiempo real,
                 cámaras de compensación, libros de corresponsales
    garantiza    finalidad, cuando la norma se la da
    NO garantiza que el beneficiario tenga el dinero disponible

  CAPA 3 · CONTABILIDAD
    qué hace     registra el efecto en cada balance
    garantiza    trazabilidad
    NO garantiza nada al cliente por sí sola

EL MENSAJE VIAJA EN SEGUNDOS.
LA LIQUIDACIÓN VIAJA EN VENTANAS OPERATIVAS.
EL CLIENTE PERCIBE LA SEGUNDA.
```

## 📖 Desarrollo

### 1. Qué garantiza una red de mensajería

Confundir «mensaje entregado» con «dinero recibido» es el malentendido más
caro de esta parte. El bloque separa con precisión lo que una red de
mensajería sí garantiza de lo que no puede garantizar por diseño.

```text
GARANTIZA
  · autenticación: el mensaje viene de quien dice
  · integridad: no se alteró en tránsito
  · no repudio: el emisor no puede negar haberlo enviado
  · entrega o notificación de fallo
  · orden y trazabilidad del propio mensaje

NO GARANTIZA
  · que el ordenante tenga fondos
  · que el receptor ejecute
  · que los fondos se liquiden
  · que el beneficiario pueda disponer
  · que el importe llegue íntegro

CONSECUENCIA OPERATIVA
  «el mensaje salió» no es «el pago está hecho».
  Confundirlos es lo que lleva a un comercio a entregar
  mercancía contra una copia de la instrucción.
```

### 2. Dónde se mueve realmente el dinero

El dinero se mueve en un libro contable, y qué libro sea depende de dónde
estén las cuentas. El bloque recorre los tres casos, de menor a mayor
complejidad, con el factor que determina el plazo en cada uno.

```text
CASO A · las dos partes tienen cuenta en el mismo banco
  el dinero se mueve en UN libro contable
  no hay liquidación externa
  → instantáneo y sin riesgo de liquidación

CASO B · bancos distintos, mismo país
  se liquida en el sistema nacional
  (bruto en tiempo real, o compensado por lotes)
  → depende del horario y del modelo

CASO C · bancos en países distintos
  se liquida en el libro de un corresponsal común,
  o en el sistema nacional de la moneda de pago
  → depende de DOS horarios y de la cadena

LA REGLA GENERAL
  cuanto más «lejos» está el libro común,
  más eslabones y más ventanas hay que atravesar
```

### 3. El desfase, contado

El desfase se entiende mejor con reloj en mano. El bloque sigue un pago real
minuto a minuto y muestra que la demora no la produce la red, sino los
horarios de los sistemas de liquidación que hay al otro lado.

```text
PAGO EN DÓLARES, ORDENADO EN SANTIAGO A LAS 16:40 (hora local)

  16:40:00  el cliente ordena
  16:40:02  validación y controles internos
  16:41:30  screening de sanciones: sin coincidencia
  16:41:35  mensaje enviado al corresponsal en Nueva York
  16:41:37  mensaje ENTREGADO                     ← 2 segundos
  ...
  16:41:37  en Nueva York son las 15:41 del mismo día
  17:00:00  ventana del sistema de EE. UU. sigue abierta
  17:12:00  el corresponsal liquida                ← 31 minutos
  ...
  el corresponsal en Singapur recibe el mensaje 16:41:40 CL,
  que en Singapur son las 03:41 del DÍA SIGUIENTE
  09:00 SG  abre la ventana operativa
  09:20 SG  liquida hacia el banco vietnamita      ← +16 horas
  ...
  banco VN abona al beneficiario                   ← +2 horas

  MENSAJE:      2 segundos
  LIQUIDACIÓN:  ~19 horas
  PERCEPCIÓN DEL CLIENTE: «tardó un día»
```

### 4. Ventanas, husos y días inhábiles

| Factor | Efecto típico | Se puede mitigar |
|---|---|---|
| Huso horario | El destino está cerrado cuando el origen envía | Parcialmente: enviar antes |
| Ventana operativa | El sistema no acepta fuera de horario | Con sistemas de operación continua |
| Corte diario | Después de cierta hora, valor del día siguiente | Conociéndolo y ordenando antes |
| Día inhábil local | Ni origen ni destino liquidan | No: es calendario |
| Día inhábil de la moneda | La moneda no liquida ese día | No |
| Fin de semana | Dos o tres días sin liquidación | Solo con sistemas 24/7 |

```text
EL CASO QUE MÁS SORPRENDE
  un pago ordenado el jueves por la tarde en una plaza
  hacia otra cuya moneda tiene festivo el viernes
  liquida el LUNES

  el mensaje llegó el jueves en dos segundos
  y el dinero estuvo disponible cuatro días después
```

### 5. Qué mejora realmente cada arquitectura

Casi toda propuesta de mejora se puede clasificar preguntando en qué capa
actúa. El bloque ofrece esa pregunta como método y anticipa qué efecto cabe
esperar de una mejora en cada capa, para no prometer lo que no toca.

```text
PREGUNTA DE MÉTODO PARA CUALQUIER PROPUESTA
  «¿en qué capa actúa?»

  MEJORA LA CAPA DE MENSAJERÍA
    formatos más ricos, validación en origen, trazabilidad
    → reduce reparaciones e investigaciones
    → NO reduce el tiempo de liquidación

  MEJORA LA CAPA DE LIQUIDACIÓN
    ventanas más largas u operación continua,
    liquidación en un libro común, prefinanciación
    → reduce el tiempo real

  MEJORA LAS DOS
    interconexión de sistemas de pagos inmediatos
    → mensaje y liquidación en la misma operación

SI UNA PROPUESTA PROMETE VELOCIDAD
Y SOLO TOCA LA CAPA 1, NO VA A ENTREGARLA
```

## 🧮 Ejemplo guiado

El ejemplo sigue el mensaje y los fondos de la misma operación por separado. La diferencia de tiempo entre ambos es lo que explica los reclamos.

**Situación.** Un banco promete a un cliente corporativo «pagos internacionales
en menos de 4 horas» y quiere saber si puede cumplirlo. Analiza 500 pagos del
corredor Chile → España en euros.

```text
DESCOMPOSICIÓN DEL TIEMPO TOTAL (mediana, en minutos)
  validación y controles internos              4
  screening de sanciones                       7
  espera a la ventana de liquidación         214
  liquidación en el sistema europeo            9
  procesamiento del banco beneficiario        38
  abono y disponibilidad                       6
  TOTAL MEDIANO                              278 min = 4,6 h

DISTRIBUCIÓN DE LA ESPERA A LA VENTANA
  pagos ordenados antes de las 10:00 CL      52 %   espera 0 min
  entre 10:00 y 12:30 CL                     19 %   espera ~90 min
  después de las 12:30 CL                    29 %   espera hasta el día siguiente
```

**Paso 1 — identifica dónde está el tiempo.**

```text
DE 278 MINUTOS, 214 SON ESPERA: EL 77 %

  las capas que el banco controla (validación, screening,
  envío) suman 11 minutos: el 4 %

  → optimizar el software del banco puede recortar
    como mucho 11 minutos de 278
```

**Paso 2 — calcula la mediana por franja horaria.**

```text
ANTES DE LAS 10:00 (52 % de los pagos)
  4 + 7 + 0 + 9 + 38 + 6 = 64 min = 1,1 h        ✓ cumple

ENTRE 10:00 Y 12:30 (19 %)
  4 + 7 + 90 + 9 + 38 + 6 = 154 min = 2,6 h      ✓ cumple

DESPUÉS DE LAS 12:30 (29 %)
  la ventana europea ya cerró
  espera hasta la apertura del día siguiente
  ≈ 1 020 min + 64 = 1 084 min = 18,1 h          ✗ no cumple
```

**Paso 3 — evalúa la promesa comercial.**

```text
CUMPLIMIENTO ESPERADO DE «MENOS DE 4 HORAS»
  52 % + 19 % = 71 % de los pagos

  el 29 % restante incumple por un factor
  que el banco NO controla: el huso horario

PROMETER 4 HORAS AL 100 % ES PROMETER
QUE ESPAÑA ABRA POR LA TARDE CHILENA
```

**Paso 4 — busca qué sí se puede mover.**

```text
LOS 38 MINUTOS DEL BANCO BENEFICIARIO
  es el segundo bloque más grande
  ¿de qué se compone?

  INVESTIGACIÓN
    verificación del beneficiario        22 min
    control interno del receptor         11 min
    proceso por lotes cada 15 min         5 min

  DE LOS 22 DE VERIFICACIÓN
    18 min corresponden a pagos cuyo identificador
    de cuenta llega sin validar en origen

  → validar el identificador en origen ahorra ~18 min
    en el 41 % de los pagos
```

**Paso 5 — recalcula con la corrección.**

```text
CON VALIDACIÓN EN ORIGEN
  antes de las 10:00:  64 − 18 = 46 min
  entre 10:00 y 12:30: 154 − 18 = 136 min
  después de 12:30:    1 084 − 18 = 1 066 min

CUMPLIMIENTO DE 4 HORAS: sigue siendo 71 %
  → la mejora es REAL pero no cambia la promesa,
    porque el 29 % falla por la ventana, no por el proceso
```

**Paso 6 — construye una promesa que sí se pueda cumplir.**

```text
OPCIÓN A · promesa por franja horaria
  «ordenado antes de las 10:00 → disponible el mismo día
   ordenado después → disponible al día hábil siguiente»
  cumplimiento estimado: 96 % (falla solo por incidentes)

OPCIÓN B · promesa de fecha de disponibilidad
  el sistema calcula y muestra la fecha y hora concretas
  al ordenar, considerando husos y calendarios
  → convierte una promesa genérica en un compromiso
    verificable por operación

OPCIÓN C · promesa de 4 horas con prefinanciación
  el banco mantiene saldo en euros y abona al beneficiario
  con sus propios fondos antes de la liquidación
  → cumple 4 h en el 96 % de los casos
  → COSTE: saldo adicional en euros y riesgo de crédito
    durante la ventana

  CUANTIFICACIÓN DE C
    saldo adicional necesario: 3 200 000 EUR
    coste neto de fondeo: 3,4 % → 108 800 EUR/año
    ingreso adicional estimado por la promesa: 71 000 EUR/año
    → NO se sostiene con este volumen
```

**Paso 7 — decide.**

```text
OPCIÓN B: fecha de disponibilidad calculada por operación

  MOTIVOS
    1. el 77 % del tiempo es espera que el banco no controla;
       una promesa genérica sobre eso se incumple
    2. la opción C tiene un coste 1,5 veces el ingreso
    3. el cliente corporativo no necesita 4 horas:
       necesita SABER cuándo, para programar su tesorería

  Y APLICAR LA MEJORA DEL PASO 4 IGUALMENTE
    validar el identificador en origen ahorra 18 minutos
    y reduce rechazos, con independencia de la promesa

  REVISAR SI CAMBIA ALGUNO DE ESTOS SUPUESTOS
    · el sistema de destino amplía su ventana
    · aparece un enlace de pagos inmediatos en el corredor
    · el volumen crece hasta amortizar la prefinanciación
```

**Interpreta:** el cliente pedía velocidad y lo que necesitaba era
**previsibilidad**. El análisis por capas mostró que el 77 % del tiempo estaba
en la capa de liquidación, fuera del alcance del banco, y que la mejora
alcanzable estaba en un dato mal validado en origen.

## 🧭 Perspectivas

El desfase entre el mensaje y los fondos afecta a cada actor de forma distinta, y varios de ellos solo ven una de las dos vías. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente corporativo | «No sé cuándo llega» | Cómo programa su tesorería |
| Comercial del banco | Una promesa que vende | Qué compromete |
| Operaciones | 214 minutos de espera | Qué puede optimizar |
| Tesorería | Coste de prefinanciar | Si adelanta fondos |
| Banco beneficiario | Identificadores sin validar | Si rechaza o repara |
| Infraestructura | Ventanas y calendarios | Si amplía horarios |
| Supervisor | Promesas incumplidas | Si exige información al cliente |

## 🏦 Del cliente al banco

El cliente ve una confirmación y el banco sabe que los fondos todavía no se movieron. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «El banco dice que ya salió» | El mensaje salió, no el dinero | 18, clase 5 |
| «Tardó cuatro días» | Festivo de la moneda más fin de semana | 18, clase 5 |
| «Necesito saber cuándo llega» | Fecha de disponibilidad calculada | 18, clase 5 |
| «Otro banco lo hace en minutos» | Enlace directo o prefinanciación | 18, clase 13 |

## ⚖️ Riesgos y controles

Los riesgos vienen de tratar el mensaje como si fuera el pago. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Confundir mensaje con pago | Se entrega mercancía contra la instrucción | Comunicar estado real, no «enviado» |
| Promesa incumplible | Compromiso genérico de horas | Fecha calculada por operación |
| Prefinanciación sin medir | Se adelanta sin comparar coste e ingreso | Cálculo antes de comprometer |
| Corte horario ignorado | Se ordena tarde sin avisar | Aviso en el momento de ordenar |
| Identificador no validado | Rechazos y demoras en destino | Validación en origen |
| Calendario desactualizado | Se promete un día inhábil | Calendario por moneda y plaza |

## 🧪 Práctica

En [`labs/lab-01.md`](../labs/lab-01.md) y [`labs/lab-02.md`](../labs/lab-02.md):

1. Traza el desfase mensaje-liquidación de tres corredores con husos distintos.
2. Descompón el tiempo total por capa e identifica qué controla el banco.
3. Calcula el cumplimiento de una promesa por franja horaria.
4. Compara el coste de prefinanciar con el ingreso que aportaría.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen abonos indebidos y reclamos. La causa es haber contabilizado contra el mensaje.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| «SWIFT mueve dinero» | Se fundieron las capas 1 y 2 | Mensajería transporta instrucciones |
| Optimizar el software para ir rápido | El tiempo estaba en la espera | Mide por capa antes de invertir |
| Prometer horas | Se ignoró el huso y el calendario | Promete fecha calculada |
| «Ya salió» como estado | Se comunicó la capa equivocada | Estado real de liquidación |
| Ignorar el festivo de la moneda | Solo se miró el calendario local | Calendario por moneda |
| Creer que una red nueva es más rápida | Actúa solo en la capa 1 | Pregunta en qué capa actúa |

## ❓ Preguntas de comprobación

1. ¿Qué garantiza y qué no garantiza una red de mensajería financiera?
2. ¿Por qué un mensaje de dos segundos puede acabar en un pago de cuatro días?
3. ¿En qué capa actúa cada tipo de mejora y cuál reduce realmente el tiempo?
4. En el ejemplo guiado, ¿qué porcentaje del tiempo controlaba el banco?
5. ¿Por qué la promesa correcta era de previsibilidad y no de velocidad?

## 📥 Entregable

Guarda en `portfolio/parte-18/clase-05/`:

- el trazado del desfase mensaje-liquidación en tres corredores;
- la descomposición del tiempo por capa, con lo que controla el banco marcado;
- el cálculo de cumplimiento de una promesa por franja horaria;
- una propuesta de compromiso con el cliente, justificada con los números.

## 🔗 Referencias cruzadas

- **Viene de:** clases 2 y 4; Parte 10, clase 10 (sistemas de pago).
- **Continúa en:** clase 6 (ISO 20022), clase 7 (liquidación y finalidad),
  clase 13 (pagos inmediatos).
- **Se aplica en:** Parte 21, clase 15 (liquidación atómica); Parte 23, clase 8.

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

- Committee on Payments and Market Infrastructures (2003). *A glossary of terms used in payments and settlement systems*. BIS. <https://www.bis.org/cpmi/glossary_030301.htm>
- Committee on Payments and Market Infrastructures e IOSCO (2012). *Principles for Financial Market Infrastructures*. BIS. <https://www.bis.org/cpmi/publ/d101.htm>
- Committee on Payments and Market Infrastructures (2021). *Extending and aligning payment system operating hours for cross-border payments*. BIS. <https://www.bis.org/cpmi/publ/d194.htm>
- Financial Stability Board (2021). *Targets for Addressing the Four Challenges of Cross-border Payments*. FSB. <https://www.fsb.org/2021/10/targets-for-addressing-the-four-challenges-of-cross-border-payments-final-report/>
- SWIFT. *Documentación de la red y de sus servicios de mensajería*. <https://www.swift.com/>
- Verificación local: comprueba las ventanas operativas y el calendario de días inhábiles de los sistemas de liquidación de las monedas con las que operes. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 04 · Cuentas nostro, vostro y loro](04-cuentas-nostro-vostro-y-loro.md) | [Parte 18](../README.md) · [Programa](../../../SYLLABUS.md) | [06 · SWIFT, CBPR+ e ISO 20022 →](06-swift-cbpr-e-iso-20022.md) |
<!-- gen:footer:end -->
