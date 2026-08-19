<!-- meta
part: 23
class: 1
title: "Alcance y modelo de negocio"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [chile, internacional]
regulatory_topics: [gobierno-corporativo, modelo-de-negocio, viabilidad]
regulation_last_verified: 2026-08-19
regulatory_status: vigente
primary_authorities: [BCBS, CMF, FSB]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 01 · Alcance y modelo de negocio

> [← Índice de la parte](../README.md) · [Índice de la parte](../README.md) · [02 · Construir, integrar o comprar →](02-construir-integrar-o-comprar.md)

**Parte 23 — Proyecto — banco digital y mercado tokenizado** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Delimitar qué se construye antes de construir nada. **La mayoría de los capstones
fracasan por exceso de alcance**, no por dificultad técnica, y el instrumento que
lo evita es una decisión explícita sobre a quién se sirve y a quién no.

Esta es la primera clase del proyecto final del programa. No introduce conceptos
nuevos: obliga a tomar la decisión que las seis partes anteriores dejaron
abierta, que es qué hacer con todo lo aprendido.

## 📚 Objetivos

Al finalizar podrás:

1. **Definir** el alcance del sistema con exclusiones explícitas.
2. **Construir** el modelo de negocio con sus fuentes de ingreso y sus costes.
3. **Calcular** el punto en que el proyecto se sostiene, incluida la carga
   regulatoria.
4. **Identificar** las decisiones que hay que tomar antes de escribir código.
5. **Justificar** por qué se deja fuera lo que se deja fuera.

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

Los cuatro primeros términos son el alcance y lo que lo justifica; los cuatro siguientes, su coste y su umbral. El **punto de sostenibilidad** es la cifra que decide si el proyecto existe: la facturación por debajo de la cual el sistema no cubre su carga regulatoria, calculada antes de construir nada.

| Concepto | Comprensión verificable |
|---|---|
| `alcance` | Lo que el sistema hace y, sobre todo, lo que no |
| `exclusión explícita` | Función descartada con su razón escrita |
| `segmento objetivo` | A quién se sirve, con qué necesidad |
| `fuente de ingreso` | De dónde sale el dinero, y de quién |
| `coste unitario` | Lo que cuesta atender a un cliente |
| `carga regulatoria` | Coste anual de estar autorizado y supervisado |
| `punto de sostenibilidad` | Volumen desde el que el sistema se paga |
| `decisión previa` | La que condiciona el diseño y no admite marcha atrás |

## 🧠 Modelo mental

Un capstone tiene una tentación característica: como se conoce todo el temario,
se quiere usar todo. El resultado es un sistema que hace muchas cosas mal en vez
de pocas bien, y que no se puede defender porque nadie puede sostener veinte
decisiones a la vez.

```text
LA REGLA DEL ALCANCE

  para cada función que se incluye,
  hay que poder responder:

  1 ¿QUIÉN LA NECESITA?      un segmento concreto
  2 ¿QUÉ PAGA POR ELLA?      una cifra
  3 ¿QUÉ CUESTA SERVIRLA?    otra cifra
  4 ¿QUÉ DECISIÓN OBLIGA?    y si condiciona
                             otras, cuál

SI LA 1 ES «TODOS» O LA 2 ES «NADA»,
LA FUNCIÓN SE EXCLUYE.

Y la exclusión se escribe con su razón:
un alcance sin exclusiones explícitas
no es un alcance, es una lista de deseos.
```

## 📖 Desarrollo

### 1. Las cuatro decisiones previas

Hay decisiones que condicionan todo lo demás y que no admiten marcha atrás sin
rehacer el sistema. Conviene identificarlas antes de empezar, porque cambiarlas
en la clase 12 cuesta el proyecto entero.

```text
1 ¿HACE FALTA UN REGISTRO DISTRIBUIDO?
    la pregunta de la Parte 19, clase 1
    · condiciona la arquitectura completa

2 ¿DÓNDE ESTÁ EL DINERO?
    la de la Parte 21, clase 10
    · condiciona si la atomicidad es posible

3 ¿QUIÉN MANDA SI DOS REGISTROS DIVERGEN?
    la de la Parte 21, clase 2
    · condiciona la conciliación permanente

4 ¿QUÉ ACTIVIDADES SE EJERCEN?
    la de la Parte 22, clase 1
    · condiciona la autorización y su coste
```

Las cuatro se resuelven en las clases 3 a 7. Lo que esta clase exige es
reconocerlas y no dar ninguna por supuesta.

### 2. El modelo de negocio

Un modelo de negocio en este contexto no es una proyección de crecimiento: es la
respuesta a de quién sale el dinero y por qué estaría dispuesto a darlo.

```text
FUENTES HABITUALES Y QUIÉN PAGA

  comisión por operación        el que opera
  diferencial de cambio         el que cambia
  margen de intermediación      el prestatario
  custodia                      el titular
  suscripción                   el cliente
  datos                         un tercero
  flotante                      nadie lo ve

LAS DOS ÚLTIMAS EXIGEN CUIDADO
  · vender datos exige base de licitud
    y suele ser incompatible con la
    confianza que el negocio necesita
  · el flotante es ingreso del cliente
    que la entidad retiene, y en varios
    regímenes está limitado
```

### 3. El coste unitario decide el segmento

Es la conclusión de la Parte 21, clase 7, aplicada al propio proyecto: atender a
un cliente cuesta casi lo mismo sea grande o pequeño, y ese coste fijo determina
por debajo de qué tamaño el cliente no es rentable ni le conviene serlo.

```text
COSTE UNITARIO ANUAL POR CLIENTE

  verificación de identidad
  evaluación de idoneidad
  información periódica
  atención de consultas
  gestión de eventos

  SUPUESTO TÍPICO: 14 a 24 al año

Y DE AHÍ SALE EL SALDO MÍNIMO
  con un margen del 1,8 % sobre saldo,
  un coste de 18 exige un saldo de 1 000
  solo para cubrirse

  → por debajo de eso, cada cliente
    resta, y el crecimiento empeora
    el resultado
```

### 4. La carga regulatoria en el modelo

La Parte 22, clase 4 produjo la cifra que decide si el negocio existe. Aquí entra
en el modelo desde el principio, no como un ajuste posterior.

```text
CARGA ANUAL
  = cumplimiento recurrente
  + amortización de la autorización
  + coste del capital inmovilizado

Y LA FACTURACIÓN NECESARIA
  = carga anual / margen

SI ESA CIFRA SUPERA LO QUE EL MERCADO
OBJETIVO PUEDE GENERAR, EL PROYECTO
NO EXISTE, y saberlo en la clase 1
ahorra las diecisiete siguientes.
```

### 5. Exclusiones que conviene escribir

Un alcance útil se reconoce por lo que excluye. Estas son las exclusiones que más
frecuentemente hacen falta y que casi nunca se escriben.

```text
  · segmentos que no cubren su coste unitario
  · instrumentos cuya calificación no está clara
  · jurisdicciones donde se activaría otro régimen
  · funciones que exigen una autorización adicional
  · integraciones con un solo proveedor posible
  · cualquier promesa que no se pueda demostrar

LA ÚLTIMA ES LA MÁS IMPORTANTE
  si el folleto no puede decirlo con evidencia,
  el sistema no lo hace
```

## 🧮 Ejemplo guiado

El ejemplo aplica las cuatro preguntas a once funciones y comprueba que excluir siete no baja el ingreso. Conviene mirar la carga regulatoria antes y después: es donde está el ahorro real.

**Situación.** Un equipo define el alcance de su capstone. La propuesta inicial
incluye once funciones. Hay que reducirla y justificar cada exclusión.

```text
PROPUESTA INICIAL
  1 cuentas y pagos locales
  2 pagos transfronterizos
  3 custodia de activos digitales
  4 cambio de divisas
  5 emisión de bonos tokenizados
  6 mercado secundario
  7 crédito con colateral tokenizado
  8 stablecoin propia
  9 interfaz de datos para terceros
 10 asesoría automatizada
 11 tarjeta de pago

MERCADO OBJETIVO
  pymes exportadoras                       2 400
  saldo medio previsto                    38 000
  operaciones al mes por cliente               9
```

**Paso 1 — calcula el ingreso potencial.**

```text
SALDO TOTAL
  2 400 × 38 000 = 91 200 000

INGRESO POR MARGEN SOBRE SALDO
  supuesto 1,4 % = 1 276 800 al año

INGRESO POR OPERACIONES
  2 400 × 9 × 12 = 259 200 operaciones
  supuesto 0,35 por operación = 90 720

INGRESO TOTAL ESTIMADO = 1 367 520 al año
```

**Paso 2 — calcula la carga regulatoria.**

```text
SEGÚN LA PARTE 22, CLASE 4

  cumplimiento recurrente supuesto   240 000
  amortización de 480 000 en 5 años   96 000
  capital de 350 000 al 8 %           28 000

  CARGA ANUAL                        364 000

  → EL 26,6 % DEL INGRESO ESTIMADO
```

**Paso 3 — comprueba si el modelo se sostiene.**

```text
INGRESO                         1 367 520
carga regulatoria                −364 000
coste unitario 2 400 × 20         −48 000
tecnología y operación supuesto  −540 000

RESULTADO                         415 520

  → se sostiene, con un margen del 30,4 %

Y ESO ES CON LAS ONCE FUNCIONES SUPUESTAS
como si costaran lo que se ha estimado.
```

**Paso 4 — aplica las cuatro preguntas a cada función.**

```text
                         QUIÉN LA   QUÉ    QUÉ    DECISIÓN
                         NECESITA   PAGA   CUESTA QUE OBLIGA

 1 cuentas y pagos       todas      sí     medio  captación
 2 transfronterizos      todas      sí     alto   corresponsalía
 3 custodia digital      pocas      poco   alto   claves
 4 cambio de divisas     todas      sí     medio  cambio
 5 emisión tokenizada    ninguna    no     alto   oferta pública
 6 mercado secundario    ninguna    no     alto   mercado
 7 crédito con colateral algunas    sí     alto   crédito
 8 stablecoin propia     ninguna    no     alto   emisor
 9 interfaz de datos     pocas      no     medio  consentimiento
10 asesoría automatizada ninguna    no     medio  asesoría
11 tarjeta de pago       algunas    sí     alto   emisor de tarjeta

  CINCO FUNCIONES NO TIENEN QUIEN LAS
  NECESITE EN ESTE SEGMENTO
```

**Paso 5 — reduce el alcance.**

```text
SE INCLUYEN
  1 cuentas y pagos locales
  2 pagos transfronterizos
  4 cambio de divisas
  7 crédito con colateral tokenizado

SE EXCLUYEN, CON SU RAZÓN

  3 custodia digital
    ninguna pyme exportadora la pidió;
    activaría el régimen de custodia y
    exigiría un esquema de claves completo

  5 y 6 emisión y mercado secundario
    el segmento no emite; construirlos
    activaría dos regímenes más para
    servir a cero clientes

  8 stablecoin propia
    la Parte 20 mostró que el régimen que
    resuelve esto ya existe; emitir una
    propia añade obligaciones de emisor
    sin resolver ningún problema del
    segmento

  9 interfaz de datos
    útil para terceros, no para el cliente;
    se pospone a una fase posterior

 10 asesoría automatizada
    activaría el régimen de asesoría y
    el segmento no lo demanda

 11 tarjeta de pago
    exige un emisor de tarjetas o un
    acuerdo con uno; se integra en vez
    de construirse
```

**Paso 6 — recalcula con el alcance reducido.**

```text
INGRESO
  las cuatro funciones incluidas mantienen
  el ingreso: las excluidas no generaban

  1 367 520 sin cambios

COSTES
  carga regulatoria
    con cuatro regímenes en vez de nueve
    supuesto 280 000 en vez de 364 000

  tecnología y operación
    supuesto 320 000 en vez de 540 000

RESULTADO
  1 367 520 − 280 000 − 48 000 − 320 000
  = 719 520

  MARGEN 52,6 % FRENTE AL 30,4 % INICIAL
```

**Paso 7 — anota las cuatro decisiones previas.**

```text
1 ¿REGISTRO DISTRIBUIDO?
   pendiente · se resuelve en la clase 4
   nota: el crédito con colateral tokenizado
   es la única función que lo sugiere

2 ¿DÓNDE ESTÁ EL DINERO?
   pendiente · clase 5
   nota: sin dinero en el registro no hay
   atomicidad en el colateral

3 ¿QUIÉN MANDA SI DIVERGEN?
   pendiente · clase 7
   nota: solo aplica si la respuesta a 1
   es sí

4 ¿QUÉ ACTIVIDADES SE EJERCEN?
   captación, pagos, cambio y crédito
   se confirma en la clase 3 con hechos
```

**Interpreta:** reducir de once funciones a cuatro **no bajó el ingreso** —las
excluidas no lo generaban— y subió el margen del 30,4 % al 52,6 %. El alcance no
se recortó por prudencia: se recortó porque cinco funciones no tenían quien las
necesitara en el segmento elegido.

## 🧭 Perspectivas

El alcance elegido afecta a cada actor de forma distinta, y algunos aparecen solo por una función que podría excluirse. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un servicio que resuelve su problema | Si contrata |
| Pyme exportadora | Pagos y cambio, no custodia | Qué usa |
| Equipo | Once funciones que sabe construir | Cuáles construye |
| Inversionista | Margen del 30,4 % o del 52,6 % | Si financia |
| Banco | Un socio con alcance definido | Si le presta servicios |
| Proveedor | Integraciones necesarias | Qué ofrece |
| Supervisor | Cuatro regímenes en vez de nueve | Qué autoriza |
| Auditor | Exclusiones con su razón | Qué verifica |
| Sociedad | Un servicio acotado y sostenible | — |

## 🏦 Del cliente al banco

El cliente pide funciones y el sistema paga una carga regulatoria por cada una. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Que haga de todo» | Cinco funciones sin quien las necesite | 23, clase 1 |
| «Cuantas más, mejor» | Cada una activa un régimen | 23, clase 1 |
| «Lo pondremos después» | Las decisiones previas no admiten después | 23, clase 1 |

## ⚖️ Riesgos y controles

Los riesgos de esta clase son de alcance excesivo y de carga no calculada. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Exceso de alcance | Muchas cosas mal en vez de pocas bien | Cuatro preguntas por función |
| Exclusiones no escritas | Reaparecen en la reunión siguiente | Exclusión con su razón |
| Carga regulatoria tardía | Se descubre en la clase 12 | Entra en el modelo desde la 1 |
| Coste unitario ignorado | El crecimiento empeora el resultado | Saldo mínimo calculado |
| Decisiones previas pospuestas | Cambiarlas cuesta el proyecto | Identificarlas y resolverlas pronto |
| Función sin quien la pida | Se construye para nadie | Segmento concreto o se excluye |

## 🧪 Práctica

El laboratorio pide aplicar las cuatro preguntas y calcular el punto de sostenibilidad. Las exclusiones con su razón escrita son lo que se evalúa.

En [`labs/lab-01.md`](../labs/lab-01.md):

1. Aplica las cuatro preguntas a una lista de funciones.
2. Calcula ingreso, carga regulatoria y resultado con y sin las exclusiones.
3. Halla el saldo mínimo que cubre el coste unitario.
4. Anota las cuatro decisiones previas con su nota de dependencia.

## ⚠️ Errores frecuentes

La tabla se usa buscando el síntoma. En esta clase casi todos vienen de un alcance decidido por entusiasmo y no por las cuatro preguntas.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Incluir todo lo aprendido | Se conoce el temario entero | Cuatro preguntas por función |
| Alcance sin exclusiones | Nadie quiere descartar | Sin exclusiones no es un alcance |
| Segmento «todos» | Se teme perder mercado | Es la señal de que no hay segmento |
| Carga regulatoria al final | Se ve como un trámite | Decide si el proyecto existe |
| Posponer las decisiones previas | Parecen técnicas | Condicionan todo lo demás |
| Estimar sin coste unitario | No aparece en el plan | Determina el saldo mínimo |

## ❓ Preguntas de comprobación

1. ¿Cuáles son las cuatro preguntas que se aplican a cada función?
2. ¿Por qué un alcance sin exclusiones explícitas no es un alcance?
3. ¿Cuáles son las cuatro decisiones previas y qué condiciona cada una?
4. ¿Cómo determina el coste unitario el saldo mínimo de un cliente?
5. En el ejemplo, ¿por qué reducir el alcance no bajó el ingreso?

## 📥 Entregable

Guarda en `portfolio/parte-23/clase-01/`:

- las cuatro preguntas aplicadas a cada función propuesta;
- el modelo con ingreso, carga regulatoria y resultado;
- las exclusiones con su razón escrita;
- las cuatro decisiones previas con su nota de dependencia.

## 🔗 Referencias cruzadas

- **Viene de:** Parte 16; Parte 21, clase 7; Parte 22, clase 4.
- **Continúa en:** clases 2, 3 y 6 de esta parte.
- **Se aplica en:** clases 13 y 18 de esta parte.

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

- Basel Committee on Banking Supervision (2015). *Corporate governance principles for banks*. BIS. Responsabilidad del órgano que aprueba el alcance del proyecto. <https://www.bis.org/bcbs/publ/d328.htm>
- Basel Committee on Banking Supervision (2018). *Sound Practices: implications of fintech developments for banks and bank supervisors*. BIS. Expectativa prudencial ante un modelo de negocio digital. <https://www.bis.org/bcbs/publ/d431.htm>
- Financial Stability Board (2023). *Global Regulatory Framework for Crypto-asset Activities*. FSB. Marco global que acota lo que el proyecto puede prometer. <https://www.fsb.org/2023/07/fsb-global-regulatory-framework-for-crypto-asset-activities/>
- Comisión para el Mercado Financiero. *Normativa sobre autorización de entidades y planes de negocio*. CMF. Contenido exigible al plan de negocio presentado al supervisor. <https://www.cmfchile.cl/portal/principal/613/w3-channel.html>
- Verificación local: comprueba qué exige tu jurisdicción en un plan de negocio para autorización y qué actividades puede ejercer una misma entidad. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-19.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← Índice de la parte](../README.md) | [Parte 23](../README.md) · [Programa](../../../SYLLABUS.md) | [02 · Construir, integrar o comprar →](02-construir-integrar-o-comprar.md) |
<!-- gen:footer:end -->
