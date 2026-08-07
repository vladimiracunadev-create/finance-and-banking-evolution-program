<!-- meta
part: 19
class: 12
title: "Escalabilidad, capas y disponibilidad"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global]
regulatory_topics: [dlt, infraestructura, resiliencia-operacional]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [CPMI, IOSCO]
requires_legal_review: false
-->

<!-- gen:header:start -->
# Clase 12 · Escalabilidad, capas y disponibilidad

> [← 11 · Interoperabilidad y puentes](11-interoperabilidad-y-puentes.md) · [Índice de la parte](../README.md) · [13 · Gobernanza, bifurcaciones y recuperación →](13-gobernanza-bifurcaciones-y-recuperacion.md)

**Parte 19 — Blockchain y DLT para instituciones financieras** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Entender por qué un registro distribuido es lento y qué se puede hacer al
respecto **sin regalar la propiedad que lo justificaba**. Cada solución de escala
cambia un supuesto de seguridad, y hay que saber cuál.

Las redes de las clases anteriores tienen capacidad limitada por diseño. Esta clase trata las soluciones, y muestra que ninguna resuelve el compromiso de fondo: lo trasladan a otra capa con supuestos nuevos.

## 📚 Objetivos

Al finalizar podrás:

1. **Explicar** el compromiso entre capacidad, descentralización y seguridad.
2. **Comparar** las cuatro familias de solución por el supuesto que cambian.
3. **Identificar** el problema de disponibilidad de datos y por qué es central.
4. **Cuantificar** el valor extraíble del orden y sus efectos.
5. **Elegir** una arquitectura de escala con criterios trazables.

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

Los cuatro primeros términos son la tensión de la escalabilidad y sus soluciones; los cuatro siguientes, sus riesgos propios. El **valor extraíble del orden** es el problema que ninguna capa resuelve: quien decide el orden de las transacciones puede beneficiarse de ese orden, y eso es una forma de anticipación.

| Concepto | Comprensión verificable |
|---|---|
| `capacidad` | Operaciones por segundo que el sistema procesa |
| `descentralización` | Número y diversidad de verificadores independientes |
| `capa base` | Registro donde reside la seguridad última |
| `segunda capa` | Sistema que ejecuta fuera y liquida en la base |
| `disponibilidad de datos` | Garantía de que los datos necesarios para verificar existen |
| `partición del estado` | División del registro en fragmentos con validadores propios |
| `valor extraíble del orden` | Beneficio de decidir el orden de las operaciones |
| `salida de emergencia` | Mecanismo para recuperar fondos si la capa superior falla |

## 🧠 Modelo mental

El modelo mental es un compromiso de tres vértices: capacidad, descentralización y seguridad. Mejorar uno empeora alguno de los otros dos, y las segundas capas trasladan el compromiso en vez de resolverlo.

```text
EL COMPROMISO QUE NO SE PUEDE ESQUIVAR

  CAPACIDAD          más operaciones por segundo
  DESCENTRALIZACIÓN  más verificadores independientes
  SEGURIDAD          más caro atacar el sistema

  MEJORAR UNA SIN TOCAR LAS OTRAS DOS
  EXIGE UN AVANCE TÉCNICO REAL,
  NO UN CAMBIO DE PARÁMETRO

SUBIR EL TAMAÑO DE BLOQUE
  + capacidad
  − descentralización (menos pueden verificar, clase 4)

REDUCIR VALIDADORES
  + capacidad
  − seguridad (menos independencias, clase 5)

LA PREGUNTA ANTE CUALQUIER PROPUESTA
  «¿qué supuesto ha cambiado?»
```

## 📖 Desarrollo

### 1. Las cuatro familias

| Familia | Cómo escala | Supuesto que cambia |
|---|---|---|
| **Parámetros** | Bloques mayores o más frecuentes | Menos verificadores pueden participar |
| **Segunda capa** | Ejecuta fuera, liquida dentro | La seguridad depende de poder salir a la base |
| **Partición** | Divide el estado entre grupos | Cada fragmento tiene menos validadores |
| **Cambio de consenso** | Menos participantes en el acuerdo | Menos independencias |

```text
LA SEGUNDA CAPA ES LA ÚNICA QUE PUEDE CONSERVAR
LA SEGURIDAD DE LA BASE, Y SOLO SI SE CUMPLE
UNA CONDICIÓN:

  que cualquiera pueda RECUPERAR sus fondos
  en la capa base sin la cooperación del operador
  de la segunda capa

  esa es la salida de emergencia, y sin ella
  la segunda capa es un custodio con otro nombre
```

### 2. Disponibilidad de datos: el problema central

```text
UNA SEGUNDA CAPA PUBLICA EN LA BASE UN COMPROMISO
DE SU ESTADO. LA BASE NO EJECUTA NADA: SOLO LO GUARDA.

  ¿CÓMO SABE UN USUARIO QUE SU SALDO ES CORRECTO?
    necesita los datos que produjeron ese compromiso

  SI EL OPERADOR NO LOS PUBLICA
    el usuario no puede construir la prueba
    para retirar sus fondos
    → está atrapado

ESO ES EL PROBLEMA DE DISPONIBILIDAD DE DATOS,
Y ES LA DIFERENCIA REAL ENTRE LAS ARQUITECTURAS

  · datos publicados en la base:
    más caro, y la salida siempre es posible
  · datos fuera de la base:
    mucho más barato, y la salida depende
    de que alguien los tenga

  → la segunda opción NO hereda la seguridad de la base,
    aunque su documentación diga lo contrario
```

### 3. Valor extraíble del orden

```text
QUIEN DECIDE EL ORDEN DE LAS OPERACIONES
PUEDE EXTRAER VALOR

  ADELANTARSE       ver una operación en la mempool
                    y ejecutar la propia antes
  ENCAJONAR         poner una operación antes y otra
                    después de la de la víctima
  CENSURAR          retrasar o excluir

EFECTOS
  · el usuario recibe peor precio del que vio
  · el coste no aparece como comisión
  · en un mercado, distorsiona la formación de precios

CONTROLES
  · mempool cifrada hasta la inclusión
  · subasta de ordenación con reglas públicas
  · orden por hora de llegada firmada (clase 5)
  · lotes con precio único por lote

NINGUNO ES COMPLETO, Y TODOS SON MEJORES QUE NADA
```

### 4. Disponibilidad del servicio

```text
UN REGISTRO DISTRIBUIDO NO SE CAE DEL MISMO MODO
QUE UN SISTEMA CENTRALIZADO

  MODOS DE FALLO PROPIOS
    · congestión: las comisiones suben y las operaciones
      esperan; el sistema «funciona» y es inutilizable
    · parada por consenso: sin quórum, no avanza
    · bifurcación: dos historias, ambas «disponibles»
    · defecto de un contrato: la aplicación se detiene
      aunque el registro funcione

CONSECUENCIA PARA UN ACUERDO DE NIVEL DE SERVICIO
  «disponibilidad de la red» no es la métrica útil.
  La útil es la de la Parte 17, clase 13:
  proporción de operaciones que se completan
  en el tiempo comprometido
```

### 5. Elegir con criterios trazables

```text
PREGUNTAS ANTES DE ADOPTAR UNA SOLUCIÓN DE ESCALA

  1. ¿qué supuesto de seguridad cambia?
  2. ¿dónde están los datos y quién los publica?
  3. ¿puedo salir sin la cooperación del operador?
  4. ¿cuánto tarda esa salida en el peor caso?
  5. ¿quién decide el orden y qué gana con ello?
  6. ¿qué pasa si el operador desaparece?

LA 3 Y LA 6 SON LAS QUE DISTINGUEN
UNA SEGUNDA CAPA DE UN CUSTODIO
```

## 🧮 Ejemplo guiado

El ejemplo compara la capacidad y las garantías de una capa base y de una segunda capa. La segunda capa gana capacidad y añade un supuesto de disponibilidad de datos.

**Situación.** El consorcio de la clase 5 necesita pasar de 40 a 400 operaciones
por segundo por el crecimiento de un nuevo servicio. Evalúa cuatro opciones.

```text
SITUACIÓN ACTUAL
  consenso bizantino, 5 nodos, f = 1
  bloques de 80 KB cada 2 s
  capacidad efectiva: ~40 operaciones por segundo
  finalidad: 3 s

REQUISITO NUEVO
  400 operaciones por segundo en pico
  finalidad: sigue siendo 5 s como máximo
```

**Paso 1 — evalúa el ajuste de parámetros.**

```text
OPCIÓN A · BLOQUES DE 800 KB CADA 2 s

  capacidad: 400 op/s  ✓
  crecimiento anual: 12,6 TB en vez de 1,26 TB
  a 10 años: 126 TB frente a 40 TB disponibles  ✗

  Y ADEMÁS
    propagar 800 KB a 4 nodos cada 2 s:
    12,8 Mbps, dentro de los 200 disponibles  ✓

  EL LÍMITE ES EL ALMACENAMIENTO, NO LA RED

OPCIÓN A' · BLOQUES DE 200 KB CADA 0,5 s
  capacidad: 400 op/s  ✓
  mismo volumen anual: 12,6 TB  ✗
  y 4 rondas de consenso por segundo:
  100 mensajes/s con n = 5, asumible

  EL VOLUMEN NO DEPENDE DE CÓMO SE REPARTA:
  400 op/s son 400 op/s
```

**Paso 2 — ataca el volumen, no la capacidad.**

```text
400 op/s × 450 bytes = 180 KB/s
× 31 536 000 s = 5,68 TB al año de datos útiles

  (los 12,6 TB anteriores incluían bloques a medio llenar)

A 10 AÑOS: 56,8 TB frente a 40 TB  ✗ sigue sin caber

OPCIONES
  · ampliar almacenamiento: 60 TB por nodo
    coste estimado: 180 000 por nodo, 900 000 total
  · poda con instantáneas (clase 4): conservar
    los últimos 24 meses completos y el resto
    como instantáneas más resúmenes
    → 5,68 × 2 + instantáneas ≈ 15 TB  ✓
```

**Paso 3 — evalúa la segunda capa.**

```text
OPCIÓN B · SEGUNDA CAPA OPERADA POR EL CONSORCIO

  ejecuta fuera, publica compromisos en la base
  capacidad: prácticamente ilimitada

  PREGUNTA 3: ¿puedo salir sin el operador?
    el operador es el propio consorcio, que ya es
    quien opera la base
    → no hay un tercero del que salir

  ENTONCES, ¿QUÉ APORTA?
    reduce el volumen de la base
    y añade una capa de software que puede fallar

  CONCLUSIÓN
    una segunda capa tiene sentido cuando el operador
    de la capa superior NO es el mismo que el de la base.
    Aquí lo es → añade complejidad sin añadir propiedad
```

**Paso 4 — evalúa la partición.**

```text
OPCIÓN C · PARTICIÓN POR TIPO DE OPERACIÓN

  fragmento 1: pagos entre participantes
  fragmento 2: el servicio nuevo

  cada fragmento con su consenso

  PREGUNTA 1: ¿qué supuesto cambia?
    con 5 nodos repartidos en 2 fragmentos,
    cada uno tendría 2 o 3 → f = 0
    → el sistema no tolera NINGÚN fallo

  PARA MANTENER f = 1 EN CADA FRAGMENTO
    hacen falta 4 nodos por fragmento = 8 nodos
    con 5 participantes, alguien opera dos

  → y entonces la independencia baja (clase 5)

  DESCARTADA salvo que entren más participantes
```

**Paso 5 — evalúa el cambio de consenso.**

```text
OPCIÓN D · REDUCIR A 4 NODOS VALIDADORES

  menos mensajes, más capacidad
  f pasa de 1 a 1 (3f+1 = 4 → f = 1)  igual

  y con 3 nodos: f = 0

  → no aporta capacidad significativa
    y reduce la tolerancia

  DESCARTADA
```

**Paso 6 — cuantifica la opción viable.**

```text
OPCIÓN A' + PODA CON INSTANTÁNEAS

  bloques de 200 KB cada 0,5 s
  capacidad: 400 op/s  ✓
  finalidad: 0,5 s + ronda ≈ 1 s  ✓ (mejor que ahora)
  almacenamiento con poda: ~15 TB a 10 años  ✓
  ancho de banda: 12,8 Mbps  ✓
  f sigue siendo 1  ✓

  COSTE
    desarrollo de la poda e instantáneas  2 400 000
    pruebas de conformidad                  900 000
    ampliación de almacenamiento
    (20 TB por nodo × 5)                  1 000 000
    TOTAL                                 4 300 000

  FRENTE A LA OPCIÓN B (segunda capa)
    desarrollo estimado                   9 800 000
    y añade una capa que puede fallar
```

**Paso 7 — decide y añade lo que faltaba.**

```text
DECISIÓN: OPCIÓN A' CON PODA E INSTANTÁNEAS

  Y DOS COSAS QUE EL ANÁLISIS DE CAPACIDAD NO CUBRÍA

  1. VALOR EXTRAÍBLE DEL ORDEN
     con 400 op/s y un servicio nuevo que puede
     ser sensible al orden, hay que decidir ahora
     la regla de ordenación
     → orden por hora de llegada firmada,
       con detección de desviación (clase 5)

  2. MÉTRICA DE DISPONIBILIDAD
     el acuerdo interno debe medir
     «operaciones completadas en menos de 5 s»,
     no «red disponible»
     → si la red funciona y las operaciones esperan,
       el sistema está caído para el usuario

  CONDICIÓN DE REVISIÓN
    si el volumen supera 800 op/s o entran más
    participantes, la partición vuelve a la mesa
    con f recalculado
```

**Interpreta:** tres de las cuatro opciones se descartaron por lo que le hacían
al supuesto de seguridad, no por su coste. Y la solución elegida obligó a decidir
dos cosas —**la regla de ordenación y la métrica de disponibilidad**— que no
aparecían en ningún requisito de capacidad.

## 🧭 Perspectivas

La escalabilidad afecta a cada participante de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Usuario del servicio | Operaciones que esperan | Si el sistema le sirve |
| Participante pequeño | Requisito de 60 TB | Si puede seguir |
| Operador de la red | 400 op/s exigidas | Qué arquitectura |
| Riesgo | Supuestos que cambian | Qué aprueba |
| Auditor | Poda del histórico | Si acepta la evidencia |
| Supervisor | Retención y verificabilidad | Qué exige conservar |
| Quien ordena | Valor extraíble | Si se controla |

## 🏦 Del cliente al banco

El cliente quiere operaciones rápidas y baratas y el sistema traslada el compromiso a otra capa. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «La red funciona pero no pasa nada» | Congestión: disponible e inutilizable | 19, clase 12 |
| «Me dieron peor precio del que vi» | Valor extraíble del orden | 19, clase 12 |
| «Ahora va más rápido» | Se cambió un supuesto: ¿cuál? | 19, clase 12 |

## ⚖️ Riesgos y controles

Los riesgos son de disponibilidad de datos y de extracción de valor por orden. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Supuesto cambiado sin advertirlo | Se sube un parámetro | Preguntar qué supuesto cambia |
| Datos no disponibles | El usuario no puede salir | Publicar en la base o exigir garantía |
| Segunda capa sin salida | Es un custodio con otro nombre | Salida de emergencia probada |
| Partición con f = 0 | Un fallo detiene el fragmento | Recalcular f por fragmento |
| Valor extraíble | Peor precio sin comisión visible | Regla de ordenación y detección |
| Métrica equivocada | Se mide la red, no el servicio | Operaciones completadas en plazo |

## 🧪 Práctica

El laboratorio pide comparar capas por capacidad y por garantías. La salida de emergencia es lo que hay que comprobar en la segunda capa.

En [`labs/lab-06.md`](../labs/lab-06.md):

1. Calcula la capacidad y el volumen de tres configuraciones.
2. Determina qué supuesto cambia cada una.
3. Simula congestión y mide operaciones completadas en plazo.
4. Implementa una regla de ordenación por hora de llegada firmada.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen problemas en segundas capas. Las causas son disponibilidad de datos supuesta y salidas de emergencia no probadas.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Subir el bloque sin más | Se miró la capacidad | Mira el volumen a 10 años |
| Segunda capa por moda | No se preguntó quién opera | Si es el mismo, no aporta |
| Partición sin recalcular f | Se dividieron los nodos | f por fragmento |
| Medir la red | Se copió una métrica de infraestructura | Mide el servicio |
| Ignorar el orden | Se pensó en capacidad | Quien ordena extrae valor |
| «Hereda la seguridad de la base» | Se leyó la documentación | Depende de la disponibilidad de datos |

## ❓ Preguntas de comprobación

1. ¿Cuál es el compromiso entre las tres propiedades y por qué no se esquiva?
2. ¿Qué condición debe cumplir una segunda capa para conservar la seguridad de
   la base?
3. ¿Qué es el problema de disponibilidad de datos y qué distingue?
4. ¿Cómo se extrae valor del orden y qué controles existen?
5. En el ejemplo guiado, ¿por qué se descartaron tres opciones y por qué motivo?

## 📥 Entregable

Guarda en `portfolio/parte-19/clase-12/`:

- el cálculo de capacidad y volumen de tres configuraciones;
- el supuesto que cambia cada una, escrito;
- la medición de operaciones completadas en plazo bajo congestión;
- tu regla de ordenación, con su mecanismo de detección de desviación.

## 🔗 Referencias cruzadas

- **Viene de:** clases 4, 5 y 11; Parte 17, clase 13 (métricas de servicio).
- **Continúa en:** clase 13 (gobernanza), clase 14 (proyecto).
- **Se aplica en:** Parte 21, clase 14 (mercados y orden); Parte 23, clase 11.

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

- Bank for International Settlements (2018). *Annual Economic Report*, capítulo sobre criptomonedas y escalabilidad. BIS. <https://www.bis.org/publ/arpdf/ar2018e5.htm>
- IOSCO (2022). *Decentralized Finance Report*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD699.pdf>
- Committee on Payments and Market Infrastructures (2017). *Distributed ledger technology in payment, clearing and settlement*. BIS. <https://www.bis.org/cpmi/publ/d157.htm>
- Financial Stability Board (2023). *The Financial Stability Risks of Decentralised Finance*. FSB. <https://www.fsb.org/2023/02/the-financial-stability-risks-of-decentralised-finance/>
- NIST (2018). *NISTIR 8202: Blockchain Technology Overview*. NIST. <https://csrc.nist.gov/pubs/ir/8202/final>
- Verificación local: comprueba qué exige tu supervisor sobre capacidad, resiliencia y retención de una infraestructura de mercado. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 11 · Interoperabilidad y puentes](11-interoperabilidad-y-puentes.md) | [Parte 19](../README.md) · [Programa](../../../SYLLABUS.md) | [13 · Gobernanza, bifurcaciones y recuperación →](13-gobernanza-bifurcaciones-y-recuperacion.md) |
<!-- gen:footer:end -->
