<!-- meta
part: 21
class: 15
title: "Interoperabilidad entre infraestructuras"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [infraestructura, interoperabilidad, riesgo-operacional]
regulation_last_verified: 2026-08-19
regulatory_status: vigente
primary_authorities: [CPMI, IOSCO, ISO]
requires_legal_review: false
-->

<!-- gen:header:start -->
# Clase 15 · Interoperabilidad entre infraestructuras

> [← 14 · Colateral y garantías tokenizadas](14-colateral-y-garantias-tokenizadas.md) · [Índice de la parte](../README.md) · [16 · Proyecto: mercado primario y secundario →](16-proyecto-mercado-primario-y-secundario.md)

**Parte 21 — Tokenización, FX on-chain y mercados programables** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Resolver el problema que la tokenización crea al resolverlo todo dentro de un
registro: **qué pasa cuando hay varios registros**. Y comprobar que el precio de
la atomicidad interna es la fragmentación externa.

Los mercados de las clases anteriores no viven aislados. Esta clase los conecta, y mide la seguridad real de esa conexión con el umbral efectivo y no con el declarado.

## 📚 Objetivos

Al finalizar podrás:

1. **Enumerar** los cuatro modelos de interoperabilidad y su riesgo.
2. **Explicar** por qué un puente reintroduce el riesgo de principal.
3. **Calcular** el umbral efectivo de seguridad de una conexión.
4. **Diseñar** la liquidación entre dos registros sin puente.
5. **Evaluar** si la fragmentación justifica la consolidación.

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

Los cuatro primeros términos son los mecanismos de conexión; los cuatro siguientes, su seguridad y su alternativa. El **umbral efectivo** es la medida que decide la seguridad de un enlace: de nada sirve un esquema de muchos validadores si comparten operador o jurisdicción.

| Concepto | Comprensión verificable |
|---|---|
| `interoperabilidad` | Capacidad de operar entre infraestructuras distintas |
| `puente` | Mecanismo que representa en un registro un activo de otro |
| `enlace directo` | Conexión entre dos infraestructuras sin intermediario |
| `participante común` | Entidad presente en ambas, que hace de nexo |
| `notario` | Tercero que confirma a ambos lados |
| `umbral efectivo` | Independencia real de quien custodia el puente |
| `fragmentación` | Liquidez repartida entre infraestructuras |
| `libro unificado` | Un solo registro con dinero y activos |

## 🧠 Modelo mental

El modelo mental es que conectar dos registros no los unifica: crea un tercer punto de fallo que hereda lo peor de los dos. Por eso la alternativa de un libro unificado siempre hay que ponerla sobre la mesa.

```text
LA PARADOJA DE ESTA PARTE

  la atomicidad exige que ambos tramos
  estén en el MISMO registro (clase 8)

  → cuanto más se cumple esa condición,
    más registros aislados aparecen

  → y entre registros vuelve el problema
    original: dos sistemas, un intervalo,
    riesgo de principal

CUATRO SALIDAS
  1 PUENTE            representar el activo del otro
  2 ENLACE DIRECTO    las infraestructuras se conectan
  3 PARTICIPANTE COMÚN alguien está en ambas
  4 CONSOLIDACIÓN     un solo registro

LA 4 RESUELVE EL PROBLEMA Y CREA OTRO:
un punto único de fallo y de gobierno.
```

## 📖 Desarrollo

### 1. Puentes

La primera opción es la más conocida y la que más incidentes acumula. El
bloque describe cómo funciona y por qué el riesgo no se mide por operación
sino por todo lo acumulado.

```text
CÓMO FUNCIONA

  el activo se bloquea en el registro A
  y se emite su representación en el B
  · al volver, se destruye y se libera

QUÉ RIESGO INTRODUCE

  · quien custodia el activo bloqueado
    es un punto único de fallo
  · el umbral efectivo del puente es el que
    protege TODO lo que ha pasado por él,
    no lo de una operación
  · si el puente falla, la representación
    en B queda sin respaldo

REGLA DE LA PARTE 19, CLASE 11, APLICADA
  el valor total acumulado en un puente
  suele superar con mucho el valor de
  cualquier operación individual
  → y su seguridad es la del umbral
    más débil de su custodia
```

### 2. Enlace directo

La segunda opción evita representar nada: cada activo se queda donde está y
solo se coordina la liquidación. El bloque expone su ventaja y su coste.

```text
LAS DOS INFRAESTRUCTURAS SE CONECTAN
Y COORDINAN LA LIQUIDACIÓN

  · sin representar nada
  · cada activo se queda en su registro
  · la coordinación se hace con un protocolo
    de bloqueo y confirmación

VENTAJA
  no hay activo bloqueado acumulándose
  en ningún sitio

COSTE
  · hay un intervalo entre bloqueo y
    confirmación
  · y ese intervalo es riesgo de principal,
    aunque acotado

EXIGE
  acuerdo bilateral, compatibilidad técnica
  y una regla común de finalidad
```

### 3. Participante común

La tercera opción no necesita acuerdo entre infraestructuras porque reproduce
un mecanismo antiguo. El bloque la describe y la nombra por lo que es.

```text
UNA ENTIDAD ESTÁ EN AMBAS INFRAESTRUCTURAS

  recibe en una y entrega en la otra
  → asume el riesgo de principal a cambio
    de una comisión

  ES EXACTAMENTE LA CORRESPONSALÍA
  DE LA PARTE 18, con otro nombre

VENTAJA
  no exige acuerdo entre infraestructuras
  ni desarrollo técnico

COSTE
  · el participante común cobra por el riesgo
  · concentra exposición
  · y se convierte en un punto crítico

CUÁNDO SE USA
  cuando el volumen no justifica un enlace
  y no hay puente disponible
```

### 4. El umbral efectivo

Un umbral de firma anuncia una independencia que casi nunca existe en esa
cantidad. El bloque aplica la medición de la parte anterior y añade el cálculo
que falta.

```text
UN PUENTE CON FIRMA 5-DE-9 NO TIENE
NECESARIAMENTE 9 INDEPENDENCIAS

  aplicar la medición de la Parte 20,
  clase 12:
  · misma organización
  · mismo proveedor de infraestructura
  · misma jurisdicción
  · mismo modelo de dispositivo

  y el resultado suele ser mucho menor

CÁLCULO ADICIONAL
  valor acumulado en el puente
  ÷ coste de comprometer el umbral efectivo

  si ese cociente es alto, el puente
  es un objetivo económico racional
```

### 5. Consolidación

La cuarta opción elimina el problema haciendo desaparecer la frontera, y crea
otros. El bloque enumera unas y otros, y devuelve la pregunta de fondo.

```text
UN SOLO REGISTRO CON DINERO Y ACTIVOS

  · atomicidad universal
  · sin puentes ni enlaces
  · sin fragmentación de liquidez

Y LOS PROBLEMAS QUE CREA
  · punto único de fallo operativo
  · gobierno: quién decide las reglas
  · competencia: quién puede participar
  · dependencia de un operador

LA PREGUNTA DE LA PARTE 19, CLASE 1,
VUELVE AQUÍ CON OTRA FORMA
  «¿existe un operador aceptable por todos?»
  · si lo hay, la consolidación es lo mejor
  · si no lo hay, la fragmentación es el
    precio de que nadie mande
```

## 🧮 Ejemplo guiado

El ejemplo mide el umbral efectivo de un enlace y lo compara con su umbral declarado. La diferencia suele ser grande.

**Situación.** Un mercado tiene tres infraestructuras tokenizadas. Hay que
decidir cómo conectarlas.

```text
DATOS
  infraestructura A · valores       2 400 000 000
  infraestructura B · valores       1 100 000 000
  infraestructura C · dinero          800 000 000
  operaciones entre A y C diarias           1 800
  operaciones entre B y C diarias             620
  operaciones entre A y B diarias             140
  importe medio                           185 000
  coste de un enlace directo            2 800 000 una vez
  comisión de un participante común        0,012 % por operación
  puente disponible                   sí, 5-de-9
```

**Paso 1 — calcula el volumen por par.**

```text
A ↔ C   1 800 × 185 000 = 333 000 000 al día
B ↔ C     620 × 185 000 = 114 700 000
A ↔ B     140 × 185 000 =  25 900 000

TOTAL DIARIO = 473 600 000
```

**Paso 2 — evalúa el participante común.**

```text
COMISIÓN 0,012 % SOBRE EL VOLUMEN

  473 600 000 × 0,012 % = 56 832 al día
  × 250 días = 14 208 000 al año

  Y ADEMÁS ASUME RIESGO DE PRINCIPAL
  sobre el importe en tránsito

  exposición media supuesta: 4 horas
  473 600 000 × 4/24 = 78 933 333

  → un solo participante con 79 millones
    de exposición permanente
```

**Paso 3 — evalúa los enlaces directos.**

```text
TRES PARES → TRES ENLACES
  3 × 2 800 000 = 8 400 000 una vez

  MANTENIMIENTO SUPUESTO
  15 % anual = 1 260 000 al año

COMPARACIÓN CON EL PARTICIPANTE COMÚN
  año 1:  8 400 000 + 1 260 000 = 9 660 000
          frente a 14 208 000
  año 2:  1 260 000 frente a 14 208 000

  LOS ENLACES SE PAGAN EN MENOS DE UN AÑO
```

**Paso 4 — evalúa priorizar por volumen.**

```text
¿HACEN FALTA LOS TRES ENLACES?

  A ↔ C es el 70,3 % del volumen
  B ↔ C es el 24,2 %
  A ↔ B es el 5,5 %

  CON SOLO A↔C Y B↔C
    coste 5 600 000 + 840 000 anual
    cubre el 94,5 % del volumen

  EL 5,5 % RESTANTE (A↔B)
    por participante común:
    25 900 000 × 0,012 % × 250 = 777 000 al año

  TOTAL AÑO 1
    5 600 000 + 840 000 + 777 000 = 7 217 000
    frente a 9 660 000 con los tres enlaces

  → DOS ENLACES Y UN PARTICIPANTE COMÚN
    PARA EL PAR PEQUEÑO
```

**Paso 5 — evalúa el puente.**

```text
EL PUENTE 5-DE-9 EVITARÍA TODO EL DESARROLLO

  MEDICIÓN DEL UMBRAL EFECTIVO
  supuesto de composición:
    5 firmantes de la misma organización
    3 de un proveedor común
    1 externo

  mayor grupo: 5
  umbral: 5
  → UN SOLO EVENTO ALCANZA EL UMBRAL
  → independencia efectiva = 9 − 5 + 1 = 5,
    pero no tolera el evento correlacionado

VALOR QUE ACUMULARÍA
  supuesto: el 20 % del volumen diario
  permanece en el puente
  473 600 000 × 20 % = 94 720 000

  ¿CUÁNTO CUESTA COMPROMETER A 5 FIRMANTES
  DE LA MISMA ORGANIZACIÓN?
  mucho menos de 94 millones

  → EL PUENTE ES UN OBJETIVO ECONÓMICO
    RACIONAL Y SE DESCARTA
```

**Paso 6 — evalúa la consolidación.**

```text
UN SOLO REGISTRO CON A, B Y C

  AHORRO
    sin enlaces, sin participante común,
    sin puente
    atomicidad en los tres pares

  COSTE
    migración supuesta: 11 000 000
    y el gobierno: ¿quién opera?

  LA PREGUNTA DECISIVA
    A, B y C son entidades distintas
    con intereses distintos

    ¿aceptarían las tres un operador común?
    · si es una de ellas: las otras dos no
    · si es una sociedad conjunta: hay que
      constituirla y gobernarla
    · si es una infraestructura pública:
      depende del régimen

  → LA CONSOLIDACIÓN NO ES UN PROBLEMA
    TÉCNICO, Y POR ESO NO SE RESUELVE
    CON UNA MIGRACIÓN
```

**Paso 7 — decide.**

```text
RECOMENDACIÓN

  CORTO PLAZO
    dos enlaces directos (A↔C, B↔C)
    y participante común para A↔B
    coste año 1: 7 217 000
    recuperación: menos de un año

  DESCARTADO
    el puente, por umbral efectivo
    insuficiente frente al valor acumulado

  MEDIO PLAZO
    abrir la conversación de consolidación,
    sabiendo que es una negociación de
    gobierno y no un proyecto técnico

  Y MIENTRAS TANTO
    diseñar los enlaces con un protocolo
    común, de modo que la consolidación
    futura no exija rehacerlos
```

**Interpreta:** el puente era la opción más barata y se descartó por una
medición de tres líneas: **cinco firmantes de la misma organización con umbral
cinco**. La consolidación resolvería todo y no es un problema técnico: es la
misma pregunta de la Parte 19, clase 1, sobre si existe un tercero aceptable por
todos.

## 🧭 Perspectivas

La interoperabilidad afecta a cada participante de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Operaciones que cruzan sistemas | — |
| Inversionista | Liquidez fragmentada | Dónde opera |
| Banco | Saldos en varias infraestructuras | Cuántos mantiene |
| Infraestructura | Un competidor o un socio | Si se conecta |
| Participante común | Comisión y exposición | Si asume el papel |
| Custodio del puente | Valor acumulado creciente | Qué umbral aplica |
| Banco central | Fragmentación del sistema | Si promueve consolidación |
| Supervisor | Puntos críticos nuevos | Qué exige a cada modelo |
| Auditor | Conexiones y sus controles | Qué verifica |
| Sociedad | Un mercado dividido | Qué eficiencia espera |

## 🏦 Del cliente al banco

El cliente mueve un activo entre infraestructuras y depende de un mecanismo con su propio riesgo. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Está todo conectado» | Por un puente con umbral efectivo bajo | 21, clase 15 |
| «Es atómico» | Dentro de cada registro; entre ellos no | 21, clase 15 |
| «Hay mucha liquidez» | Repartida entre tres infraestructuras | 21, clase 15 |

## ⚖️ Riesgos y controles

Los riesgos son del mecanismo de enlace y de la fragmentación. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Puente con umbral efectivo bajo | Objetivo económico racional | Medir independencia y valor acumulado |
| Participante común concentrado | Exposición permanente alta | Límite y varios participantes |
| Enlace sin regla de finalidad común | Discrepancia sobre qué es definitivo | Acuerdo previo de finalidad |
| Fragmentación de liquidez | Profundidad menor en cada sitio | Medir la accesible, no la agregada |
| Consolidación tratada como proyecto técnico | Fracasa por gobierno | Abordarla como negociación |
| Enlaces incompatibles entre sí | Rehacerlos al consolidar | Protocolo común desde el inicio |

## 🧪 Práctica

El laboratorio pide medir el umbral efectivo de varios enlaces. Los factores compartidos entre validadores son lo que hay que contar.

En [`labs/lab-04.md`](../labs/lab-04.md):

1. Compara los cuatro modelos con el volumen por par.
2. Mide el umbral efectivo de un puente y su valor acumulado.
3. Diseña la liquidación entre dos registros con enlace directo.
4. Cuantifica el coste de la fragmentación sobre la profundidad.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen fallos en enlaces. La causa es el umbral efectivo menor que el declarado.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Elegir el puente por barato | Es la opción sin desarrollo | Mide su umbral efectivo |
| Ignorar el valor acumulado | Se piensa por operación | El puente guarda todo lo que pasó |
| Un enlace por par | Parece completo | Prioriza por volumen |
| Consolidar como proyecto técnico | Es lo que sabe hacer un equipo | Es una negociación de gobierno |
| Sumar la liquidez de todas | Parece disponible | No es accesible a la vez |
| Enlaces sin protocolo común | Cada uno con su socio | Impide consolidar después |

## ❓ Preguntas de comprobación

1. ¿Por qué la atomicidad interna produce fragmentación externa?
2. ¿Cuáles son los cuatro modelos y qué riesgo introduce cada uno?
3. ¿Cómo se mide si un puente es un objetivo económico racional?
4. ¿En qué se parece un participante común a la corresponsalía?
5. ¿Por qué la consolidación no se resuelve con una migración?

## 📥 Entregable

Guarda en `portfolio/parte-21/clase-15/`:

- la comparación de los cuatro modelos con volumen por par;
- la medición del umbral efectivo del puente y su valor acumulado;
- el diseño del enlace directo con su regla de finalidad;
- la recomendación con corto y medio plazo separados.

## 🔗 Referencias cruzadas

- **Viene de:** clases 8, 9 y 10; Parte 19, clase 11.
- **Continúa en:** clase 16 de esta parte.
- **Se aplica en:** Parte 22, clase 10; Parte 23, clases 5 y 15.

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

- CPMI e IOSCO (2012). *Principles for Financial Market Infrastructures*. BIS. Requisitos de los enlaces entre infraestructuras. <https://www.bis.org/cpmi/publ/d101.htm>
- Committee on Payments and Market Infrastructures (2024). *Tokenisation in the context of money and other assets: concepts and implications for central banks*. BIS. Fragmentación de la liquidez entre registros y sus costes. <https://www.bis.org/cpmi/publ/d225.htm>
- Bank for International Settlements (2023). *Annual Economic Report, capítulo III*. BIS. El libro unificado como respuesta a la fragmentación entre registros. <https://www.bis.org/publ/arpdf/ar2023e3.htm>
- ISO/TC 307. *Blockchain and distributed ledger technologies — interoperability*. ISO. Normalización técnica de la interoperabilidad entre registros. <https://www.iso.org/committee/6266604.html>
- Verificación local: comprueba qué exige tu jurisdicción para que dos infraestructuras de mercado se enlacen y qué régimen aplica a un puente entre registros. **Fecha de verificación de esta clase: 2026-08-19.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 14 · Colateral y garantías tokenizadas](14-colateral-y-garantias-tokenizadas.md) | [Parte 21](../README.md) · [Programa](../../../SYLLABUS.md) | [16 · Proyecto: mercado primario y secundario →](16-proyecto-mercado-primario-y-secundario.md) |
<!-- gen:footer:end -->
