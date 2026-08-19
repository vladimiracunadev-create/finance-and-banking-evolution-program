<!-- meta
part: 20
class: 11
title: "Dinero programable y sus límites"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [dinero-programable, proteccion-al-cliente, disenio-de-producto]
regulation_last_verified: 2026-08-19
regulatory_status: vigente
primary_authorities: [BIS, CPMI, OCDE]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 11 · Dinero programable y sus límites

> [← 10 · Monedas digitales de banco central](10-monedas-digitales-de-banco-central.md) · [Índice de la parte](../README.md) · [12 · Custodia de activos digitales →](12-custodia-de-activos-digitales.md)

**Parte 20 — Activos digitales, stablecoins y dinero programable** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Separar dos cosas que se confunden con consecuencias graves: **pago programable**
—una condición sobre una operación— y **dinero programable** —una restricción
adherida a la unidad monetaria—. La primera es útil; la segunda destruye la
fungibilidad.

Todas las formas de dinero de las clases anteriores permiten añadir condiciones. Esta clase separa dos cosas que se nombran igual y tienen consecuencias opuestas: programar un pago y programar la unidad monetaria.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** pago programable de dinero programable con un criterio
   operativo.
2. **Explicar** qué es la fungibilidad y por qué su pérdida es un problema.
3. **Diseñar** una condición programable que no adhiera restricciones a la
   unidad.
4. **Enumerar** las condiciones que no deben programarse nunca y por qué.
5. **Evaluar** un caso de uso por su reversibilidad y su vía de excepción.

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

Los cuatro primeros términos separan programar el pago de programar el dinero; los cuatro siguientes, sus consecuencias jurídicas. La **fungibilidad** es lo que se pierde al programar el dinero: si una unidad tiene condiciones y otra no, dejan de ser intercambiables, y eso rompe una propiedad básica del dinero.

| Concepto | Comprensión verificable |
|---|---|
| `pago programable` | Condición que se evalúa al ejecutar una operación |
| `dinero programable` | Restricción que viaja con la unidad monetaria |
| `fungibilidad` | Que una unidad sea intercambiable por otra sin distinción |
| `condición de liberación` | Regla que determina cuándo se entrega el importe |
| `vía de excepción` | Procedimiento humano para casos no previstos |
| `reversibilidad` | Posibilidad de deshacer un efecto no deseado |
| `caducidad` | Pérdida de validez del saldo por tiempo |
| `uso restringido` | Limitación del destino del importe |

## 🧠 Modelo mental

El modelo mental es una distinción con consecuencias: programar la condición de un pago es inocuo y programar la unidad monetaria no lo es. La primera afecta a una operación y la segunda afecta a todo lo que se haga después con esa unidad.

```text
LA PRUEBA QUE LOS SEPARA

  PREGUNTA: cuando el dinero llega al destinatario,
  ¿SIGUE LLEVANDO LA RESTRICCIÓN?

    NO  → es un PAGO programable
          la condición se evaluó y se agotó
          el destinatario recibe dinero normal

    SÍ  → es DINERO programable
          la unidad lleva la regla adherida
          y el destinatario recibe algo
          que NO es equivalente al resto

CONSECUENCIA
  el dinero programable rompe la fungibilidad:
  1 000 con restricción vale menos que 1 000 sin ella
  → aparece un descuento
  → y con él, un mercado secundario y una brecha
    entre lo que dice la ley y lo que vale
```

## 📖 Desarrollo

### 1. Qué sí conviene programar

Programar la operación y programar la unidad de dinero son cosas muy
distintas, y solo la primera es aceptable. El bloque recoge casos de uso
legítimos y señala la propiedad que todos comparten.

```text
CONDICIONES SOBRE LA OPERACIÓN, NO SOBRE LA UNIDAD

  · pagar contra entrega verificada
  · liberar por tramos según hitos de obra
  · retener hasta el fin de un plazo de devolución
  · dividir un cobro entre varios beneficiarios
  · repetir un pago según un calendario
  · exigir doble firma por encima de un importe
  · devolver automáticamente si no se cumple
    la condición en un plazo

TODAS COMPARTEN UNA PROPIEDAD
  cuando el importe llega al destinatario,
  es dinero sin marcas
```

### 2. Qué no debe programarse

Hay cuatro condiciones que no deberían programarse nunca, y todas empiezan
pareciendo razonables. El bloque las enumera con el efecto al que conducen.

```text
1 CADUCIDAD DEL SALDO
    el dinero que expira es una quita
    encubierta al tenedor

2 RESTRICCIÓN DE DESTINO PERMANENTE
    «solo puede gastarse en X para siempre»
    → dos clases de dinero, y una vale menos

3 LISTA DE COMERCIOS PERMITIDOS EN LA UNIDAD
    lo que empieza como control de un subsidio
    acaba como control del gasto de una persona

4 BLOQUEO AUTOMÁTICO POR PERFIL
    una condición evaluada sobre datos del
    tenedor, sin decisión humana ni recurso

5 REVERSIÓN UNILATERAL POR EL EMISOR
    convierte la propiedad en una concesión

6 CONDICIONES SIN VÍA DE EXCEPCIÓN
    el mundo real tiene casos que ninguna
    regla previó: una urgencia médica,
    un error de dato, una muerte
```

### 3. El caso de los subsidios

El subsidio con destino restringido es el caso donde mejor se ve la distancia
entre la intención y el resultado. El bloque presenta el argumento a favor y,
a continuación, lo que se observa cuando se aplica.

```text
EL ARGUMENTO A FAVOR
  «si el subsidio es para alimentación,
   que solo pueda gastarse en alimentación»

QUÉ OCURRE EN LA PRÁCTICA
  · el beneficiario vende el saldo con descuento
    para obtener dinero libre
  · nace un mercado gris con pérdida para el más
    necesitado
  · el comercio no adherido queda excluido,
    y suele ser el pequeño y el rural
  · el coste administrativo de mantener listas
    supera lo que se pretendía ahorrar

DISEÑO ALTERNATIVO QUE SÍ FUNCIONA
  · transferencia en dinero libre
  · condicionalidad en la ELEGIBILIDAD,
    no en la unidad monetaria
  · verificación posterior por muestreo
  · el control se aplica a la persona
    con procedimiento y recurso,
    no al billete
```

### 4. La vía de excepción

Una condición programada sin vía de excepción convierte cualquier error en
definitivo. El bloque fija las cuatro preguntas que debe responder esa vía
para no convertirse ella misma en el agujero.

```text
TODA CONDICIÓN PROGRAMADA NECESITA
UN CAMINO PARA SALTÁRSELA

  ¿QUIÉN PUEDE ACTIVARLA?
    una función con nombre, no «el sistema»

  ¿CON QUÉ JUSTIFICACIÓN?
    causas previstas más una cláusula abierta
    con doble aprobación

  ¿CON QUÉ REGISTRO?
    quién, cuándo, por qué, y quién lo aprobó

  ¿CON QUÉ REVISIÓN POSTERIOR?
    muestreo de excepciones y reporte periódico

SIN VÍA DE EXCEPCIÓN, LA AUTOMATIZACIÓN
CONVIERTE CADA ERROR EN UN DAÑO PERMANENTE
```

### 5. Reversibilidad

Antes de programar una condición conviene clasificarla por lo que costaría
deshacerla. El bloque propone tres categorías y coloca en cada una los casos
habituales.

```text
CLASIFICACIÓN POR CONSECUENCIA

  REVERSIBLE
    retención temporal, pago diferido,
    división de un cobro
    → un error se corrige

  REVERSIBLE CON COSTE
    liberación anticipada, pago a un tercero
    → se corrige con una compensación

  IRREVERSIBLE
    caducidad, destrucción de saldo,
    envío a una dirección inexistente
    → no se corrige

REGLA DE DISEÑO
  cuanto menos reversible sea el efecto,
  más humana debe ser la decisión que lo activa
```

## 🧮 Ejemplo guiado

El ejemplo compara un pago programable y una unidad programada sobre el mismo caso. Solo el segundo produce pérdida de fungibilidad.

**Situación.** Una administración quiere entregar una ayuda de emergencia a
120 000 hogares y propone restringir su uso. Hay que evaluar el diseño.

```text
PROPUESTA INICIAL
  importe por hogar                       180 000
  total                            21 600 000 000
  restricción: solo comercios de la lista A
  caducidad: 90 días
  comercios en la lista A                   4 200
  comercios totales del país               61 000
```

**Paso 1 — clasifica la propuesta.**

```text
¿LA RESTRICCIÓN VIAJA CON LA UNIDAD? SÍ
¿EL COMERCIO RECIBE DINERO LIBRE?

  si el comercio recibe dinero normal
  al cobrar → la restricción se agota
  en el primer pago

  si el comercio recibe saldo también
  restringido → la restricción se propaga

LA PROPUESTA NO LO ACLARA.
Primera pregunta al diseño, y es decisiva.
```

**Paso 2 — mide la cobertura de la lista.**

```text
COMERCIOS ADHERIDOS
  4 200 / 61 000 = 6,9 %

  SUPUESTO DECLARADO: la adhesión es menor
  en zonas rurales

  hogares con al menos un comercio adherido
  a menos de 2 km: supuesto 71 %

  → EL 29 % DE LOS HOGARES TIENE
    UNA BARRERA FÍSICA REAL
    = 34 800 hogares
```

**Paso 3 — estima el descuento del mercado gris.**

```text
UN HOGAR SIN COMERCIO CERCANO
BUSCARÁ CAMBIAR EL SALDO POR DINERO LIBRE

  supuesto: descuento del 20 %
  (observado en programas comparables;
   es un supuesto, no un dato de este caso)

  pérdida para esos hogares
  34 800 × 180 000 × 20 % = 1 252 800 000

  → EL 5,8 % DE LA AYUDA SE PIERDE
    EN EL MECANISMO, Y LA PIERDEN
    LOS HOGARES PEOR SITUADOS
```

**Paso 4 — calcula el efecto de la caducidad.**

```text
CADUCIDAD A 90 DÍAS

  supuesto: el 8 % del importe no se gasta
  a tiempo, concentrado en hogares con
  menor acceso

  21 600 000 000 × 8 % = 1 728 000 000
  que vuelven a la administración

  ¿ES UN AHORRO? NO:
  es una ayuda que no llegó,
  a quien más la necesitaba
```

**Paso 5 — suma el coste administrativo.**

```text
MANTENER LA LISTA A

  altas y bajas mensuales     supuesto 380
  coste por gestión                     14 000
  coste mensual                      5 320 000
  coste en 3 meses                  15 960 000

  reclamaciones de comercios excluidos
  supuesto 900 × 22 000 =           19 800 000

  TOTAL ADMINISTRATIVO ≈ 35 760 000
```

**Paso 6 — compara con el diseño alternativo.**

```text
ALTERNATIVA · DINERO LIBRE CON
CONDICIONALIDAD EN LA ELEGIBILIDAD

  pérdida por mercado gris             0
  pérdida por caducidad                0
  coste de listas                      0

  COSTE NUEVO
  verificación posterior por muestreo
  del 3 % de beneficiarios
  120 000 × 3 % × 26 000 =    93 600 000

  COMPARACIÓN
  propuesta inicial   1 252 800 000
                    + 1 728 000 000
                    +    35 760 000
                    = 3 016 560 000

  alternativa                93 600 000

  DIFERENCIA: 2 922 960 000
  = 13,5 % de la ayuda total
```

**Paso 7 — responde al objetivo declarado.**

```text
EL OBJETIVO ERA «QUE SE GASTE EN ALIMENTACIÓN»

  ¿LO CONSIGUE LA RESTRICCIÓN?
    parcialmente: el mercado gris la elude
    con un 20 % de coste para el beneficiario

  ¿LO CONSIGUE LA ALTERNATIVA?
    con verificación por muestreo, sin
    barrera física y sin pérdida

  ¿HAY ALGO QUE SOLO LA RESTRICCIÓN LOGRE?
    la apariencia de control
    y esa no es una finalidad legítima
    de política pública

CONDICIÓN PROGRAMABLE QUE SÍ CABE
  liberar el importe contra una compra
  verificada, con el saldo remanente
  siempre disponible en dinero libre
  → es un PAGO programable,
    y no rompe la fungibilidad
```

**Interpreta:** la restricción no consigue su objetivo y cuesta el 13,5 % de la
ayuda, pagado por los hogares con peor acceso. **La condicionalidad pertenece a
la elegibilidad de la persona, donde hay procedimiento y recurso, no a la unidad
monetaria, donde no los hay.**

## 🧭 Perspectivas

El dinero programable afecta a cada participante de forma distinta, y a algunos les restringe derechos. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Dinero que no puede usar donde necesita | Si lo vende con descuento |
| Comercio | Estar dentro o fuera de la lista | Si se adhiere |
| Fintech | Un producto con reglas | Qué construye |
| Banco | Saldos con restricciones | Cómo los contabiliza |
| Banco central | Fungibilidad del dinero | Qué permite programar |
| Emisor | Control sobre el uso | Hasta dónde llega |
| Administración | Cumplimiento del objetivo | Qué diseño elige |
| Supervisor | Trato desigual entre unidades | Qué límites impone |
| Auditor | Excepciones aplicadas | Qué revisa |
| Sociedad | Quién controla el gasto ajeno | Qué acepta |

## 🏦 Del cliente al banco

El cliente recibe dinero con condiciones y esas condiciones limitan lo que puede hacer. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Tengo 180 000 que no puedo usar» | La restricción viaja con la unidad | 20, clase 11 |
| «Me lo cambian por 144 000» | Mercado gris por pérdida de fungibilidad | 20, clase 11 |
| «Se me venció el saldo» | Caducidad: una quita encubierta | 20, clase 11 |

## ⚖️ Riesgos y controles

Los riesgos son de fungibilidad y de vías de excepción ausentes. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Pérdida de fungibilidad | Dos clases de dinero con precios distintos | Restricción que se agota en el primer pago |
| Mercado gris | Descuento sobre el más necesitado | Dinero libre con condicionalidad en la elegibilidad |
| Exclusión geográfica | Sin comercio adherido cerca | Medir cobertura antes de decidir |
| Caducidad | Saldo que se pierde | No programar caducidad |
| Sin vía de excepción | Un error queda permanente | Excepción con nombre, registro y revisión |
| Ampliación silenciosa del control | Se añaden reglas sin debate | Cambios con procedimiento público |

## 🧪 Práctica

El laboratorio pide clasificar casos entre pago programable y dinero programado. La pérdida de fungibilidad es el criterio.

En [`labs/lab-06.md`](../labs/lab-06.md):

1. Clasifica cinco condiciones como pago o dinero programable.
2. Calcula el coste total de una restricción de destino.
3. Rediseña el caso con condicionalidad en la elegibilidad.
4. Redacta la vía de excepción con sus cuatro elementos.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen usos problemáticos de la programabilidad. La causa es haber programado la unidad y no el pago.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Llamar programable a todo | Es la palabra de moda | Aplica la prueba de la restricción |
| Programar caducidad | Parece incentivar el gasto | Es una quita al tenedor |
| Listas de comercios | Da sensación de control | Mide la cobertura y el mercado gris |
| Sin vía de excepción | Se confía en la regla | El mundo real no cabe en la regla |
| Ignorar la fungibilidad | No se nota hasta que hay descuento | El descuento es el síntoma |
| Confundir objetivo con apariencia | El control se ve; el resultado no | Mide si el objetivo se cumplió |

## ❓ Preguntas de comprobación

1. ¿Qué prueba distingue pago programable de dinero programable?
2. ¿Por qué la pérdida de fungibilidad crea un mercado gris?
3. Enumera cuatro condiciones que no deben programarse y por qué.
4. ¿Qué cuatro elementos tiene una vía de excepción?
5. ¿Dónde debe estar la condicionalidad y por qué allí?

## 📥 Entregable

Guarda en `portfolio/parte-20/clase-11/`:

- la clasificación de cinco condiciones con la prueba aplicada;
- el cálculo del coste total de una restricción de destino;
- el rediseño con condicionalidad en la elegibilidad;
- la vía de excepción redactada con sus cuatro elementos.

## 🔗 Referencias cruzadas

- **Viene de:** clases 8 y 10; Parte 19, clase 8.
- **Continúa en:** clases 12 y 15 de esta parte.
- **Se aplica en:** Parte 21, clase 12; Parte 22, clase 12; Parte 23, clase 8.

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

- Bank for International Settlements (2023). *Annual Economic Report, capítulo III*. BIS. Programabilidad como propiedad de la plataforma y no de la unidad monetaria. <https://www.bis.org/publ/arpdf/ar2023e3.htm>
- Committee on Payments and Market Infrastructures (2024). *Tokenisation in the context of money and other assets: concepts and implications for central banks*. BIS. Distinción entre pago programable y unidad restringida. <https://www.bis.org/cpmi/publ/d225.htm>
- OCDE (2021). *Recommendation of the Council on Financial Literacy*. OECD. Efectos de la restricción sobre la comprensión del usuario. <https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0461>
- Bank for International Settlements (2021). *CBDCs: an opportunity for the monetary system*, Annual Economic Report. BIS. Argumento sobre programabilidad en el sistema monetario. <https://www.bis.org/publ/arpdf/ar2021e3.htm>
- Verificación local: comprueba qué límites impone tu jurisdicción a la restricción de uso del dinero, a la caducidad de saldos y al tratamiento automatizado de decisiones que afectan a personas. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-19.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 10 · Monedas digitales de banco central](10-monedas-digitales-de-banco-central.md) | [Parte 20](../README.md) · [Programa](../../../SYLLABUS.md) | [12 · Custodia de activos digitales →](12-custodia-de-activos-digitales.md) |
<!-- gen:footer:end -->
