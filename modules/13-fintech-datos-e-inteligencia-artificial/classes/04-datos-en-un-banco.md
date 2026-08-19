<!-- meta
part: 14
class: 4
title: "Datos en un banco"
level: profesional
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 04 · Datos en un banco

> [← 03 · Banca abierta y APIs](03-banca-abierta-y-apis.md) · [Índice de la parte](../README.md) · [05 · Analítica aplicada →](05-analitica-aplicada.md)

**Parte 14 — Fintech, datos e inteligencia artificial** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Construir la base sobre la que descansa todo lo demás de esta parte. Ningún modelo, ningún algoritmo y
ninguna estrategia de datos funciona sobre información que nadie gobierna: **la calidad del dato es el
límite superior de la calidad de cualquier decisión que se tome con él**.

Las tres clases anteriores mueven datos. Esta explica cómo están organizados dentro del banco, y por qué casi ningún proyecto analítico funciona a la primera: los datos existen, están repartidos entre sistemas que no se hablan y nadie es responsable de su calidad.

## 📚 Objetivos

Al finalizar podrás:

1. **Describir** la arquitectura de datos de un banco y sus capas.
2. **Definir** las dimensiones de calidad del dato y medirlas.
3. **Aplicar** un marco de gobierno de datos con roles y responsabilidades.
4. **Trazar** el linaje de un dato desde su origen hasta el reporte.
5. **Evaluar** el costo real de la mala calidad de datos.

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

Los cuatro primeros términos son las capas de la arquitectura; los cuatro siguientes, el gobierno que las hace fiables. El **linaje** es el requisito que los supervisores exigen y que casi nadie tiene completo: poder rastrear cualquier cifra hasta su origen.

| Concepto | Comprensión verificable |
|---|---|
| `sistema de origen` | Aplicación donde el dato se genera. |
| `almacén de datos` | Repositorio estructurado para análisis. |
| `lago de datos` | Repositorio de datos en su formato original. |
| `linaje` | Recorrido del dato desde su origen hasta su uso. |
| `dueño del dato` | Responsable de su definición y calidad. |
| `diccionario de datos` | Definición única y compartida de cada campo. |
| `dimensión de calidad` | Atributo medible: exactitud, completitud, oportunidad. |
| `dato maestro` | Información de referencia compartida: cliente, producto. |

## 🧠 Modelo mental

El modelo mental es una cadena de custodia: cada dato nace en un sistema, se copia, se transforma y llega a un informe. Si no se puede recorrer esa cadena hacia atrás, el número del informe no se puede defender ante nadie.

```text
UN BANCO NO TIENE UN PROBLEMA DE DATOS: TIENE VARIOS

  1. EL MISMO DATO EN VARIOS SISTEMAS, DISTINTO
     el domicilio del cliente en cinco aplicaciones,
     con cinco valores

  2. EL MISMO NOMBRE PARA COSAS DISTINTAS
     "cliente activo" significa algo distinto
     en riesgo, en comercial y en contabilidad

  3. NADIE ES RESPONSABLE DEL DATO
     todos lo usan, ninguno lo define ni lo corrige

LOS TRES SE RESUELVEN CON LO MISMO: GOBIERNO
  y ninguno se resuelve comprando tecnología
```

## 📖 Desarrollo

### 1. Arquitectura por capas

Los datos recorren capas con propósitos distintos. La tabla las recoge.

```text
SISTEMAS DE ORIGEN
  núcleo bancario, tarjetas, créditos, canales, CRM,
  contabilidad, riesgo, cumplimiento
        ↓ ingesta
CAPA DE ALMACENAMIENTO
  lago (datos en bruto) + almacén (datos modelados)
        ↓ transformación
CAPA SEMÁNTICA
  definiciones de negocio, métricas certificadas
        ↓ consumo
CONSUMO
  reportes regulatorios, gestión, modelos, análisis, productos
```

| Capa | Responsable típico | Riesgo si falla |
|---|---|---|
| Origen | Área dueña del proceso | El error nace y se propaga |
| Almacenamiento | Tecnología | Pérdida, latencia, inconsistencia |
| Semántica | Gobierno de datos | Cada área calcula distinto |
| Consumo | Área usuaria | Decisiones sobre datos mal entendidos |

De las cuatro capas hay una que rara vez tiene dueno y cuya ausencia se nota
en cada comite.

```text
LA CAPA SEMÁNTICA ES LA MÁS DESCUIDADA Y LA MÁS IMPORTANTE
  sin definiciones únicas, dos áreas presentan
  al mismo comité dos cifras distintas del mismo indicador
  y la reunión se dedica a reconciliar, no a decidir
```

### 2. Dimensiones de calidad

La calidad de un dato se mide en varias dimensiones y cada una se comprueba distinto. La tabla las recoge.

| Dimensión | Pregunta | Cómo se mide |
|---|---|---|
| Exactitud | ¿Refleja la realidad? | Contraste con fuente autorizada |
| Completitud | ¿Falta información? | Porcentaje de campos vacíos |
| Consistencia | ¿Coincide entre sistemas? | Comparación cruzada |
| Oportunidad | ¿Está a tiempo? | Latencia desde el evento |
| Validez | ¿Cumple el formato y el dominio? | Reglas de validación |
| Unicidad | ¿Hay duplicados? | Detección de registros repetidos |
| Trazabilidad | ¿Se sabe de dónde viene? | Linaje documentado |

Medir las siete dimensiones no sirve de nada si la corrección se aplica en el
lugar equivocado.

```text
LA REGLA DE ORO
  la calidad se corrige EN EL ORIGEN
  corregirla aguas abajo:
    · es más cara
    · hay que repetirla en cada uso
    · el error vuelve en la siguiente carga
```

### 3. Gobierno de datos

El gobierno asigna dueños y responsabilidades sobre cada dato. La tabla lo recoge.

```text
ROLES
  DUEÑO DEL DATO       ejecutivo del área de negocio
                       define el dato, responde por su calidad
  ADMINISTRADOR        experto operativo del dominio
                       aplica reglas, resuelve incidencias
  CUSTODIO             tecnología
                       almacena, protege, entrega
  CONSUMIDOR           quien lo usa
                       reporta problemas, no los corrige por su cuenta

COMITÉ DE DATOS
  resuelve definiciones en conflicto
  aprueba el diccionario
  prioriza la remediación
```

```text
LA SEÑAL DE UN GOBIERNO QUE NO FUNCIONA
  cada área mantiene su propia copia "corregida"
  de los datos centrales

  esas copias son la evidencia de que
  nadie confía en el dato oficial
```

### 4. Linaje

El linaje se construye o no se tiene: reconstruirlo después es casi imposible. El esquema lo describe.

```text
POR QUÉ IMPORTA
  · un reporte regulatorio con un error exige explicar
    de dónde vino el dato: sin linaje, no se puede
  · un cambio en un sistema de origen puede romper
    veinte reportes: sin linaje, se descubre después
  · un modelo entrenado con un campo que cambió de significado
    empieza a fallar sin causa aparente

QUÉ DEBE REGISTRARSE
  origen, transformaciones aplicadas, reglas de negocio,
  responsables de cada paso, fecha de cada cambio
```

### 5. Requisitos supervisores

Los supervisores exigen capacidades concretas de agregación de datos de riesgo. La tabla las recoge.

```text
EL PRINCIPIO SUPERVISOR CENTRAL
  un banco debe poder AGREGAR sus datos de riesgo
  de forma exacta, completa y oportuna,
  especialmente en situaciones de estrés

  esto no es un requisito técnico: es un requisito
  de gobierno, porque en una crisis el directorio
  necesita saber su exposición total en horas, no en semanas
```

| Exigencia | Qué implica |
|---|---|
| Gobierno y arquitectura | Responsabilidades definidas y documentadas |
| Exactitud e integridad | Conciliación con la contabilidad |
| Completitud | Todas las exposiciones materiales |
| Oportunidad | Plazos compatibles con la toma de decisiones |
| Adaptabilidad | Capacidad de responder consultas no previstas |

**La adaptabilidad es el requisito que más bancos incumplen.** Producir el reporte mensual establecido
es una cosa; responder en 48 horas «cuál es nuestra exposición total a este grupo económico, incluyendo
derivados y contingentes, consolidada» es otra muy distinta.

## 🧮 Ejemplo guiado

El ejemplo rastrea el linaje de una cifra de un informe regulatorio. Conviene contar las transformaciones: cada una es un punto donde el dato pudo cambiar sin que nadie lo notara.

**Situación.** Un banco mide el costo de su mala calidad de datos.

```text
SÍNTOMAS REPORTADOS
  · el reporte de exposición por grupo económico tarda 9 días
  · dos áreas reportan cifras distintas de clientes activos
  · el 18 % de los envíos postales se devuelven
  · un reporte regulatorio fue corregido tres veces en el año
  · el modelo de admisión tuvo que recalibrarse por cambio
    no comunicado en un campo de origen
```

**Paso 1 — mide las dimensiones de calidad de los datos críticos.**

```text
DATO: domicilio del cliente
  completitud:    94,2 %   (37 120 clientes sin domicilio)
  exactitud:      78,4 %   (contrastado con devoluciones postales)
  consistencia:   61,3 %   (coincide entre los 5 sistemas)
  unicidad:       —

DATO: identificación del grupo económico
  completitud:    68,0 %   (204 800 clientes sin grupo asignado)
  exactitud:      no medible sin revisión manual
  consistencia:   —

DATO: ingreso declarado del cliente
  completitud:    82,6 %
  oportunidad:    antigüedad media 3,4 años
  validez:        4,1 % con valores fuera de rango plausible
```

**Paso 2 — cuantifica el costo del domicilio.**

```text
ENVÍOS DEVUELTOS
  envíos anuales: 2 840 000
  devueltos: 18 % = 511 200
  costo unitario del envío: 0,0008
  costo de los devueltos: 409

REPROCESO
  gestión de devoluciones: 511 200 × 0,0004 = 204

COBRANZA
  clientes en mora sin domicilio válido: 4 620
  costo adicional de localización: 4 620 × 0,012 = 55
  recuperación perdida por no localizar: estimada 340

TOTAL COSTO ANUAL DEL DOMICILIO: 1 008
```

**Paso 3 — cuantifica el costo del grupo económico.**

```text
32 % de los clientes sin grupo asignado

CONSECUENCIAS
  · el límite de concentración por grupo (Parte 11, clase 3)
    se calcula sobre datos incompletos
  · exposición real a grupos: subestimada

REVISIÓN MANUAL DE UNA MUESTRA
  se revisaron 400 clientes sin grupo asignado
  se identificaron 118 que pertenecen a grupos ya registrados
  extrapolando: 60 416 clientes mal clasificados
  exposición asociada estimada: 68 000

RECÁLCULO DEL MAYOR GRUPO
  exposición registrada: 68 000 → 16,2 % del patrimonio efectivo
  exposición real estimada: 89 400 → 21,3 %
  límite normativo: 25 %

  el banco está más cerca del límite de lo que cree,
  y no puede demostrar su cumplimiento
```

**Paso 4 — cuantifica el costo del tiempo de agregación.**

```text
EL REPORTE DE EXPOSICIÓN POR GRUPO TARDA 9 DÍAS

  en una situación de estrés, 9 días es inaceptable
  el requisito supervisor exige capacidad de agregación
  rápida en estrés

  COSTO DIRECTO
    esfuerzo manual: 3 personas × 9 días × 6 veces al año
    = 162 días-persona = 78 anuales

  COSTO REGULATORIO
    hallazgo supervisor probable
    requerimiento de plan de remediación
    posible cargo de capital de Pilar 2 por deficiencia
    estimado: 400 de capital adicional → 56 anuales
```

**Paso 5 — cuantifica el costo del modelo.**

```text
CAMBIO NO COMUNICADO EN UN CAMPO DE ORIGEN
  el campo "tipo de contrato laboral" cambió su codificación
  el modelo de admisión lo usaba como variable
  4 meses de decisiones con la variable mal interpretada

  colocación en esos 4 meses: 18 400
  deterioro adicional observado: 1,8 puntos de mora
  pérdida esperada adicional: 18 400 × 1,8 % × 58 % = 192

  costo de recalibración y revisión: 140
  TOTAL: 332 (evento único, con probabilidad de repetición)
```

**Paso 6 — consolida el costo.**

```text
domicilio                          1 008 anuales
grupo económico (capital y riesgo)   340 anuales estimado
agregación lenta                     134 anuales
riesgo de modelo por linaje          332 × probabilidad 0,4 = 133
inconsistencia de indicadores
  (tiempo de reconciliación en comités)  86 anuales
reportes regulatorios corregidos      78 anuales
TOTAL ESTIMADO                     1 779 anuales

MÁS EL RIESGO NO CUANTIFICADO
  no poder demostrar el cumplimiento del límite de concentración
```

**Paso 7 — evalúa la remediación.**

```text
PROGRAMA DE REMEDIACIÓN
  1. gobierno: dueños de dato designados para 40 datos críticos
     costo: 0 (asignación de responsabilidad existente)
  2. diccionario y capa semántica: definiciones únicas
     costo: 420 inicial + 90 anuales
  3. validación en el origen: reglas en los sistemas
     que capturan el dato
     costo: 680 inicial
  4. remediación de domicilios: campaña de actualización
     costo: 340 inicial
  5. asignación de grupo económico: proceso automatizado
     con revisión de excepciones
     costo: 520 inicial + 120 anuales
  6. linaje documentado de los 40 datos críticos
     costo: 380 inicial + 60 anuales
  7. capacidad de agregación: modelo de datos de riesgo
     costo: 1 240 inicial + 180 anuales

  TOTAL: 3 580 inicial + 450 anuales
```

**Paso 8 — evalúa el retorno.**

```text
BENEFICIO ANUAL
  reducción del costo medido: 1 779 × 75 % = 1 334
  capital de Pilar 2 evitado: 56
  TOTAL: 1 390 anuales

COSTO ANUAL
  operación: 450
  amortización de 3 580 en 5 años: 716
  TOTAL: 1 166 anuales

BENEFICIO NETO: 224 anuales
período de recuperación: 4,2 años
```

```text
EL RETORNO CUANTIFICADO ES MODESTO
Y LA DECISIÓN ES CLARA IGUALMENTE

  porque lo no cuantificado domina:
  · no poder demostrar cumplimiento de un límite normativo
  · no poder responder al supervisor en estrés
  · cada modelo de la Parte 14 descansa en estos datos
  · el punto 2 de la Parte 11, clase 12: un modelo
    con datos de entrada manipulables o mal definidos
    produce decisiones incorrectas a escala industrial

  la calidad del dato no es un proyecto con retorno:
  es una CONDICIÓN de todo lo demás
```

**Interpreta:** el ejercicio de cuantificación fue útil y **su conclusión no dependía del número**. Un
retorno de 224 anuales no justificaría por sí solo un programa de 3 580, y el programa se justifica de
todos modos porque los datos son el insumo de cada decisión que las clases siguientes van a construir
sobre ellos. Cuando algo es una condición y no una opción, el análisis de retorno sirve para
dimensionarlo, no para decidirlo.

## 🏦 Del cliente al banco

El cliente genera datos y el banco los reparte entre sistemas que no siempre coinciden. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Me llegó la carta a una dirección vieja» | Calidad del dato de domicilio | 14, clase 4 |
| «Tengo que repetir mis datos en cada área» | Sin dato maestro de cliente | 10, clase 15 |
| «El banco no sabe que tengo otro producto suyo» | Visión de cliente fragmentada | 14, clase 4 |
| «Me rechazaron por un dato incorrecto» | Exactitud del dato de origen | 14, clase 11 |
| «El banco tardó semanas en responder» | Capacidad de agregación | 14, clase 4 |

## 🧪 Práctica

El laboratorio pide construir el linaje de una cifra y medir la calidad de un conjunto de datos. La cifra no cuadra con su origen, y encontrar dónde se rompió es el objetivo.

En `labs/lab-02.md`, sección de datos:

1. Mide las siete dimensiones de calidad sobre un conjunto de datos sintético.
2. Traza el linaje de un dato desde su origen hasta un reporte regulatorio.
3. Cuantifica el costo de la mala calidad en tres procesos.
4. Diseña el marco de gobierno con roles y comité para diez datos críticos.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen informes que no se pueden defender. Las causas son ausencia de linaje y datos sin dueño.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se corrige el dato aguas abajo | Vuelve en la siguiente carga | Corrige en el origen. |
| Cada área tiene su copia corregida | Nadie confía en el dato oficial | Gobierno con dueño designado. |
| Se compra tecnología para resolverlo | El problema es de gobierno | Define primero, herramienta después. |
| Sin diccionario ni capa semántica | Cifras distintas del mismo indicador | Definición única y certificada. |
| Cambio de origen no comunicado | Modelos y reportes se rompen | Linaje y gestión de cambios. |
| Se cumple el reporte mensual y nada más | Falta adaptabilidad | Prueba consultas no previstas. |

## ❓ Preguntas de comprobación

1. ¿Cuáles son los tres problemas de datos de un banco y qué los resuelve?
2. ¿Por qué la calidad se corrige en el origen y no aguas abajo?
3. ¿Qué evidencia un área que mantiene su propia copia corregida?
4. ¿Por qué la adaptabilidad es el requisito supervisor que más se incumple?
5. ¿Por qué la calidad del dato es una condición y no un proyecto con retorno?

## 📥 Entregable

Guarda en `portfolio/parte-14/clase-04/`:

- la medición de las siete dimensiones sobre el conjunto elegido;
- el linaje trazado desde el origen hasta el reporte;
- la cuantificación del costo de la mala calidad;
- el marco de gobierno diseñado con roles y comité.

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

- Basel Committee on Banking Supervision (2013). *Principles for effective risk data aggregation and risk reporting (BCBS 239)*. BIS. Principios de agregación de datos y reporte de riesgos. <https://www.bis.org/publ/bcbs239.htm>
- Basel Committee on Banking Supervision (2020). *Progress in adopting the Principles for effective risk data aggregation*. BIS. Estado real de adopción de esos principios en la banca.
- DAMA International (2017). *DAMA-DMBOK: Data Management Body of Knowledge* (2.ª ed.). Technics Publications. Vocabulario y funciones del gobierno de datos.
- ISO (2015). *ISO 8000: Data quality*. ISO. Dimensiones medibles de calidad del dato.
- Redman, T. (2016). *Getting in Front on Data: Who Does What*. Technics Publications. Reparto de responsabilidades sobre el dato entre negocio y tecnología.
- Verificación local: revisa si tu supervisor exige el cumplimiento de los principios de agregación de datos de riesgo y con qué alcance.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 03 · Banca abierta y APIs](03-banca-abierta-y-apis.md) | [Parte 14](../README.md) · [Programa](../../../SYLLABUS.md) | [05 · Analítica aplicada →](05-analitica-aplicada.md) |
<!-- gen:footer:end -->
