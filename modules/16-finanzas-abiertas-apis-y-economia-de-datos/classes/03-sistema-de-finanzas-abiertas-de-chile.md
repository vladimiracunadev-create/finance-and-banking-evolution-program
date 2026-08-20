<!-- meta
part: 17
class: 3
title: "El Sistema de Finanzas Abiertas de Chile"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [chile]
regulatory_topics: [open-finance, licenciamiento, proteccion-de-datos]
regulation_last_verified: 2026-08-20
regulatory_status: en-despliegue-por-fases
primary_authorities: [CMF, Banco Central de Chile, UAF]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 03 · El Sistema de Finanzas Abiertas de Chile

> [← 02 · Ecosistema, participantes y modelos de implantación](02-ecosistema-participantes-y-modelos-de-implantacion.md) · [Índice de la parte](../README.md) · [04 · Clasificación, calidad y gobierno de datos financieros →](04-clasificacion-calidad-y-gobierno-de-datos.md)

**Parte 17 — Finanzas abiertas, APIs y economía de datos** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Estudiar un sistema de finanzas abiertas **real**, con su ley, su normativa, sus
figuras y su calendario de despliegue, y aprender a leer una norma financiera
para responder tres preguntas: qué actividad realizo, qué me exige y desde cuándo.

> **Aviso de vigencia.** Esta clase describe el marco chileno a la fecha de
> verificación indicada en el encabezado. El Sistema de Finanzas Abiertas está en
> **despliegue por fases** y su normativa se ha modificado y puede volver a
> modificarse. Ningún dato de esta clase sustituye la consulta de la fuente
> oficial vigente. Esta clase **no es asesoría legal**.

Las dos clases anteriores describen el modelo en abstracto. Esta lo aterriza en una jurisdicción concreta, con su ley, su registro y su calendario de fases, porque lo que obliga nunca es el modelo sino la norma que lo transpone.

## 📚 Objetivos

Al finalizar podrás:

1. **Ubicar** la Ley N.º 21.521 dentro del ordenamiento financiero chileno y
   explicar qué crea y qué no crea.
2. **Distinguir** las figuras del registro de prestadores de servicios financieros
   de las del Sistema de Finanzas Abiertas.
3. **Determinar** qué obligaciones aplican a una actividad concreta y ante qué
   autoridad.
4. **Leer** una norma de carácter general y extraer de ella una matriz de
   obligaciones con fechas.
5. **Verificar** la vigencia de cada elemento antes de usarlo en una decisión.

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

Los cuatro primeros términos son el marco legal y su registro; los cuatro siguientes, las figuras que reconoce y su calendario. El **registro de prestadores** es la puerta de entrada: sin inscripción no se puede operar, y la figura que se solicita determina qué se puede hacer y qué capital hace falta.

| Concepto | Comprensión verificable |
|---|---|
| `Ley N.º 21.521` | Ley que promueve la competencia e inclusión financiera mediante innovación y tecnología |
| `registro de prestadores` | Registro ante la CMF de quienes realizan las actividades que la ley enumera |
| `Sistema de Finanzas Abiertas` | Régimen de intercambio de información financiera con consentimiento, creado por la misma ley |
| `institución proveedora de información` | Entidad obligada a poner información a disposición |
| `proveedor de servicios basados en información` | Quien accede a esa información con consentimiento del cliente |
| `proveedor de iniciación de pagos` | Quien instruye pagos con cargo a cuentas del cliente |
| `norma de carácter general` | Instrumento con el que la CMF desarrolla la ley |
| `despliegue por fases` | Entrada en vigor escalonada por tipo de entidad y de información |

## 🧠 Modelo mental

El modelo mental es un despliegue por fases: la norma no entra en vigor de golpe, sino que abre capacidades sucesivas con plazos publicados. Saber en qué fase está cada capacidad decide qué se puede construir hoy y qué hay que esperar.

```text
LA LEY 21.521 HACE DOS COSAS DISTINTAS EN UN MISMO TEXTO

  BLOQUE A · REGISTRO DE PRESTADORES
    crea un perímetro para actividades que antes estaban fuera:
      · plataformas de financiamiento colectivo
      · sistemas alternativos de transacción
      · intermediación de instrumentos financieros
      · custodia de instrumentos financieros
      · asesoría crediticia y asesoría de inversión
      · enrutamiento de órdenes
    → «si haces esto, te inscribes y te supervisan»

  BLOQUE B · SISTEMA DE FINANZAS ABIERTAS
    crea la obligación de compartir información
    con consentimiento del cliente
    → «si custodias el dato, debes darle acceso al tercero autorizado»

CONFUNDIRLOS ES EL ERROR MÁS FRECUENTE
  una empresa puede estar en el Bloque A y no en el B
  y viceversa
```

## 📖 Desarrollo

### 1. Qué crea la ley y qué no

La forma más rápida de entender una ley marco es contrastar lo que crea con lo
que deliberadamente deja fuera. La segunda columna del bloque evita el error
más caro de esta parte: dar por autorizado lo que la ley nunca autorizó.

```text
CREA
  · un registro de prestadores de servicios financieros ante la CMF
  · requisitos de inscripción, autorización, capital y garantía
    diferenciados según la actividad y su escala
  · el Sistema de Finanzas Abiertas
  · potestades de la CMF para dictar normativa de desarrollo

NO CREA
  · una licencia bancaria simplificada
  · un régimen de criptoactivos como categoría propia
  · una autorización automática para operar en el mercado cambiario
  · una excepción a la normativa de prevención de lavado de activos
```

El último punto es el que más sorpresas produce: inscribirse en el registro **no
exime** de las obligaciones ante la Unidad de Análisis Financiero ni de las de
protección al consumidor.

### 2. Las actividades del registro

| Actividad | Qué es en una frase | Riesgo dominante |
|---|---|---|
| Financiamiento colectivo | Poner en contacto a quien pide financiamiento con quien lo aporta | Selección adversa e información al inversionista |
| Sistema alternativo de transacción | Plataforma donde se transan instrumentos fuera de una bolsa | Formación de precios y abuso de mercado |
| Intermediación de instrumentos financieros | Comprar o vender por cuenta de terceros | Conflicto de interés y mejor ejecución |
| Custodia de instrumentos financieros | Mantener instrumentos por cuenta de terceros | Segregación e insolvencia |
| Asesoría crediticia | Recomendar sobre productos de crédito | Incentivos y transparencia |
| Asesoría de inversión | Recomendar sobre instrumentos | Idoneidad y conflicto de interés |
| Enrutamiento de órdenes | Dirigir órdenes hacia intermediarios | Mejor ejecución y pago por flujo |

El registro se organiza por actividades, y de ahi se sigue una consecuencia
que sorprende a muchos equipos.

```text
EL CRITERIO ES LA ACTIVIDAD, NO LA TECNOLOGÍA
  una aplicación móvil que recomienda instrumentos
  hace asesoría de inversión
  aunque su equipo se defina como «empresa de software»
```

### 3. Las figuras del Sistema de Finanzas Abiertas

El Sistema define tres figuras con obligaciones crecientes: la que custodia el
dato, la que lo consume y la que además mueve dinero. Cada escalón añade
requisitos a los del anterior, no los sustituye.

```text
INSTITUCIÓN PROVEEDORA DE INFORMACIÓN
  custodia el dato o la cuenta
  obligación: poner la información a disposición
  típicamente: bancos, emisores de tarjetas, cooperativas,
               aseguradoras, administradoras, según la fase

PROVEEDOR DE SERVICIOS BASADOS EN INFORMACIÓN
  accede a la información con consentimiento
  obligación: inscripción, seguridad, uso limitado a la finalidad

PROVEEDOR DE INICIACIÓN DE PAGOS
  instruye pagos con cargo a cuentas del cliente
  obligación: la anterior + régimen de pagos y autenticación

INSTITUCIÓN PROVEEDORA DE SERVICIOS DE INICIACIÓN
  ejecuta la instrucción recibida
```

### 4. Cómo leer una norma de carácter general

Es la destreza operativa de la clase. El procedimiento es siempre el mismo:

```text
PASO 1 · ÁMBITO
  ¿a quién aplica? ¿desde qué umbral? ¿hay exclusiones?

PASO 2 · DEFINICIONES
  la norma redefine términos; el significado del texto
  es el de sus definiciones, no el del uso común

PASO 3 · OBLIGACIONES
  qué hay que hacer, con qué frecuencia y ante quién

PASO 4 · PLAZOS Y VIGENCIA
  fecha de publicación ≠ fecha de entrada en vigor
  ≠ fecha de exigibilidad de cada obligación

PASO 5 · TRANSITORIOS
  suelen contener el calendario real; se leen SIEMPRE

PASO 6 · REMISIONES
  «en lo no previsto, se aplicará…» abre otro cuerpo normativo

PASO 7 · ANEXOS TÉCNICOS
  en finanzas abiertas, el anexo técnico es donde está
  la especificación de las APIs, la seguridad y los formatos
```

### 5. Las otras autoridades

La inscripción ante la CMF no agota el mapa regulatorio. Un producto de
finanzas abiertas toca, según lo que haga, a tres autoridades más, y cada una
tiene competencias propias que no se delegan entre sí.

```text
COMISIÓN PARA EL MERCADO FINANCIERO
  registro, autorización, supervisión de conducta y solvencia

BANCO CENTRAL DE CHILE
  sistemas de pago, normativa de cambios internacionales,
  Mercado Cambiario Formal
  → relevante en cuanto el producto toque divisas o pagos

UNIDAD DE ANÁLISIS FINANCIERO
  prevención de lavado de activos y financiamiento del terrorismo
  → obligación propia, independiente del registro ante la CMF

SERNAC
  protección del consumidor en la relación de consumo

AUTORIDAD DE PROTECCIÓN DE DATOS PERSONALES
  régimen de datos personales, en implantación
```

La consecuencia práctica: una fintech de finanzas abiertas responde ante **cuatro
o cinco autoridades distintas**, y el calendario de cada una es independiente.

## 🧮 Ejemplo guiado

El ejemplo determina qué figura corresponde a un proyecto concreto y qué exige. Conviene mirar el calendario de fases: la figura puede estar disponible y su capacidad todavía no.

**Situación.** Una empresa quiere lanzar en Chile un producto que: (a) muestra la
posición consolidada del cliente en bancos y tarjetas; (b) recomienda cuál de sus
créditos conviene prepagar; y (c) permite ordenar ese prepago desde la aplicación.

**Paso 1 — descompón el producto en actividades.**

```text
(a) mostrar posición consolidada
    → acceso a información financiera con consentimiento
    → figura: proveedor de servicios basados en información

(b) recomendar qué crédito prepagar
    → ¿es información o es recomendación personalizada?
    → si dice «tu crédito A tiene tasa mayor: prepágalo»
      es RECOMENDACIÓN sobre un producto de crédito
    → figura probable: asesoría crediticia

(c) ordenar el prepago desde la aplicación
    → instrucción de pago con cargo a la cuenta del cliente
    → figura: proveedor de iniciación de pagos
```

**Paso 2 — separa lo que parece uno y son tres.**

```text
EL EQUIPO CREÍA TENER UN PRODUCTO
TIENE TRES ACTIVIDADES CON TRES REGÍMENES

  la (a) es la más simple
  la (b) es la que el equipo NO había identificado
  la (c) es la que más exige
```

**Paso 3 — evalúa el punto (b), que es el que se pasa por alto.**

```text
¿CÓMO DISTINGUIR INFORMACIÓN DE ASESORÍA?

  INFORMACIÓN   «tus créditos son: A al 1,8 % y B al 2,4 % mensual»
                el cliente concluye

  ASESORÍA      «te conviene prepagar el B»
                la empresa concluye POR el cliente
                y el cliente actúa sobre esa conclusión

  LA FRONTERA NO ESTÁ EN EL ALGORITMO:
  está en si hay una recomendación personalizada
```

**Paso 4 — construye la matriz de obligaciones.**

```text
ACTIVIDAD (a) · INFORMACIÓN
  inscripción                    sí
  seguridad de la información    sí, con estándar del anexo técnico
  limitación de finalidad        sí
  prevención de LA/FT            evaluar según el rol
  protección al consumidor       sí

ACTIVIDAD (b) · ASESORÍA CREDITICIA
  todo lo anterior
  + idoneidad de la recomendación
  + gestión de conflictos de interés
  + transparencia de incentivos
  → si la empresa cobra del prestamista recomendado,
    el conflicto es estructural y debe revelarse

ACTIVIDAD (c) · INICIACIÓN DE PAGOS
  todo lo anterior
  + autenticación reforzada
  + régimen de operaciones no autorizadas
  + continuidad operacional
  + capital y garantía según la actividad y escala
```

**Paso 5 — pon fechas.**

```text
EL CALENDARIO NO ES UNO SOLO

  inscripción ante la CMF        depende de la actividad y de los
                                 transitorios de la norma aplicable
  acceso a información           por fases: primero cierto tipo de
                                 entidades e información, luego el resto
  iniciación de pagos            fase posterior a la de información
  protección de datos            calendario propio, distinto

CONSECUENCIA DE PLANIFICACIÓN
  el producto (a) puede existir antes que el (c)
  planificar los tres para la misma fecha
  es planificar contra el calendario más lento
```

**Paso 6 — estima el coste de la decisión de secuencia.**

```text
SUPUESTOS DEL EJERCICIO (ilustrativos)

  ESCENARIO 1 — lanzar los tres a la vez
    fecha posible: la del componente más lento
    ingreso hasta esa fecha: 0
    coste de cumplimiento acumulado: el de los tres

  ESCENARIO 2 — lanzar (a), luego (b), luego (c)
    ingreso desde la fase 1
    coste escalonado
    riesgo: el producto (a) solo puede no retener clientes

CÁLCULO DE LA OPCIÓN 2, 24 MESES
  clientes al mes 6 con (a):          18 000
  ingreso mensual por cliente:            420
  ingreso mes 6 a 12:      18 000 × 420 × 6  = 45 360 000
  coste de cumplimiento de (a) en ese periodo:  27 500 000
  margen del periodo:                            17 860 000

  ese margen financia la autorización de (c)
  sin capital externo adicional
```

**Paso 7 — formula la decisión y lo que hay que verificar.**

```text
DECISIÓN: secuenciar (a) → (b) → (c)

Y ANTES DE COMPROMETER LA FECHA, VERIFICAR EN LA FUENTE OFICIAL
  1. qué norma de carácter general regula hoy cada actividad
  2. en qué fase del despliegue está la información que necesito
  3. qué exige el anexo técnico vigente
  4. qué transitorios aplican a mi tipo de entidad
  5. si mi actividad (b) califica como asesoría en la norma vigente
  6. qué obligación tengo ante la UAF con independencia de lo anterior

NINGUNA DE LAS SEIS SE RESPONDE CON ESTA CLASE:
se responden en el sitio del supervisor, con la fecha de consulta anotada
```

**Interpreta:** el trabajo regulatorio no consistió en leer una ley, sino en
**descomponer el producto en actividades**. Casi todos los problemas de perímetro
nacen de un producto que contenía una actividad que nadie nombró.

## 🧭 Perspectivas

El marco chileno afecta a cada actor de forma distinta y en momentos distintos. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Una app que consolida y sugiere | Si confía y consiente |
| Fintech | Tres regímenes en un producto | Qué secuencia sigue |
| Banco | Obligación de compartir por fases | Cómo prioriza su inversión |
| Banco Central | Efecto sobre pagos y cambios | Si su normativa aplica |
| CMF | Nuevas entidades en el registro | Qué exige y cuándo |
| UAF | Nuevo canal de operaciones | Qué reporte requiere |
| Auditor | Fechas de exigibilidad | Qué comprueba en cada fase |
| Sociedad | Más competencia en crédito | Si mejora el precio |

## 🏦 Del cliente al banco

El cliente ve un derecho nuevo y la entidad ve obligaciones con calendario. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Esta app ve mis cuentas» | Obligación de proveer información | 17, clase 3 |
| «Me dijo qué crédito prepagar» | Eso es asesoría, con su régimen | 17, clase 3 |
| «Pagué desde la app» | Iniciación: autenticación y responsabilidad | 17, clase 11 |
| «¿Y si se equivocan?» | Régimen de operaciones no autorizadas | 17, clase 11 |

## ⚖️ Riesgos y controles

Los riesgos aquí son de cumplimiento y de calendario. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Actividad no identificada | El producto asesora sin saberlo | Descomposición por actividad antes de construir |
| Fecha equivocada | Se compromete un lanzamiento imposible | Lectura de transitorios y anexos |
| Norma citada sin vigencia | Se decide con un texto derogado | Fecha de verificación obligatoria |
| Obligación LA/FT ignorada | Se asume que el registro la cubre | Análisis independiente ante la UAF |
| Conflicto de interés oculto | Se recomienda a quien paga | Revelación y gobierno del incentivo |
| Anexo técnico no leído | Implementación no conforme | Conformidad contra el anexo vigente |

## 🧪 Práctica

En [`labs/lab-01.md`](../labs/lab-01.md) y el
[proyecto](../project/README.md):

1. Descompón un producto en actividades y asigna figura a cada una.
2. Construye la matriz actividad → obligación → autoridad → fuente → fecha.
3. Identifica qué obligación **no** cubre el registro ante la CMF.
4. Anota, para cada fila, la fecha en que verificaste la fuente.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen proyectos mal planificados frente a esta norma. Las causas son la figura equivocada y el calendario de fases ignorado.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| «Nos inscribimos, ya cumplimos» | Se confunde registro con cumplimiento total | UAF, consumidor y datos son independientes |
| Registro y finanzas abiertas mezclados | Son dos bloques de la misma ley | Sepáralos desde el diagrama |
| Recomendar sin llamarlo asesoría | Se miró la tecnología, no la actividad | La frontera es la recomendación personalizada |
| Fecha de publicación como vigencia | No se leyeron los transitorios | Publicación ≠ vigencia ≠ exigibilidad |
| Anexo técnico ignorado | Se leyó solo el cuerpo de la norma | El anexo contiene la especificación |
| Citar la norma sin fecha | Se copió de una fuente secundaria | Fuente oficial y fecha de consulta |

## ❓ Preguntas de comprobación

1. ¿Qué dos bloques distintos contiene la Ley N.º 21.521 y por qué confundirlos
   lleva a un error de perímetro?
2. ¿Qué obligaciones **no** quedan cubiertas por la inscripción ante la CMF?
3. ¿Dónde está la frontera entre informar y asesorar, y por qué no está en el
   algoritmo?
4. ¿Por qué los artículos transitorios son la parte más importante para planificar
   un lanzamiento?
5. ¿Qué seis cosas hay que verificar en la fuente oficial antes de comprometer una
   fecha, y por qué esta clase no puede responderlas?

## 📥 Entregable

Guarda en `portfolio/parte-17/clase-03/`:

- la descomposición de un producto en actividades, con su figura;
- la matriz actividad → obligación → autoridad → fuente oficial → fecha de
  verificación;
- la lista de obligaciones independientes del registro;
- una nota de límites que declare qué no pudiste verificar y por qué.

## 🔗 Referencias cruzadas

- **Viene de:** clases 1 y 2; Parte 12, clases 1 y 2 (perímetro y supervisión);
  Parte 14, clase 12 (regulación de la tecnología financiera).
- **Continúa en:** clase 5 (consentimiento), clase 12 (privacidad y portabilidad).
- **Se aplica en:** Parte 22, clases 3 a 12 (arquitectura regulatoria chilena);
  Parte 23, clase 3 (perímetro del banco digital).

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

- Biblioteca del Congreso Nacional de Chile. *Ley N.º 21.521, que promueve la competencia e inclusión financiera a través de la innovación y tecnología en la prestación de servicios financieros*. Texto legal que la clase lee artículo por artículo. <https://www.bcn.cl/leychile>
- Comisión para el Mercado Financiero. *Normativa aplicable a los prestadores de servicios financieros de la Ley N.º 21.521 y al Sistema de Finanzas Abiertas, incluidos sus anexos técnicos*. CMF. Normativa y anexos que desarrollan la ley y fijan el calendario. <https://www.cmfchile.cl/>
- Banco Central de Chile. *Compendio de Normas Financieras* y *Compendio de Normas de Cambios Internacionales*. <https://www.bcentral.cl/>
- Unidad de Análisis Financiero. *Normativa de prevención del lavado de activos y del financiamiento del terrorismo*. UAF. Obligaciones de prevención aplicables al prestador inscrito. <https://www.uaf.cl/>
- Biblioteca del Congreso Nacional de Chile. *Ley N.º 19.913, que crea la Unidad de Análisis Financiero*. Creación y facultades de la unidad de inteligencia financiera. <https://www.bcn.cl/leychile>
- Verificación local obligatoria: comprueba en el sitio de la CMF qué normas de carácter general están vigentes hoy para tu actividad, en qué fase está el despliegue del Sistema de Finanzas Abiertas y qué versión del anexo técnico rige. **Fecha de verificación de esta clase: 2026-08-20.** Esta clase no constituye asesoría legal.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 02 · Ecosistema, participantes y modelos de implantación](02-ecosistema-participantes-y-modelos-de-implantacion.md) | [Parte 17](../README.md) · [Programa](../../../SYLLABUS.md) | [04 · Clasificación, calidad y gobierno de datos financieros →](04-clasificacion-calidad-y-gobierno-de-datos.md) |
<!-- gen:footer:end -->
