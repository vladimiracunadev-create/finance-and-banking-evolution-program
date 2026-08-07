<!-- meta
part: 14
class: 6
title: "Inteligencia artificial en banca"
level: profesional
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 06 · Inteligencia artificial en banca

> [← 05 · Analítica aplicada](05-analitica-aplicada.md) · [Índice de la parte](../README.md) · [07 · Crédito digital y datos alternativos →](07-credito-digital-y-datos-alternativos.md)

**Parte 14 — Fintech, datos e inteligencia artificial** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Aplicar inteligencia artificial en un banco con criterio: **sabiendo qué problemas resuelve, cuáles no,
y qué obligaciones adicionales impone su uso** en un sector donde cada decisión afecta a una persona y
debe poder explicarse.

La analítica de la clase anterior usa modelos que se pueden explicar. Esta trata los que no siempre se pueden, y su criterio central es de proporcionalidad: la exigencia de explicabilidad y de control depende de qué decide el modelo, y no de qué tecnología usa.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** los tipos de sistema de inteligencia artificial y sus usos bancarios.
2. **Evaluar** un caso de uso por su valor, su riesgo y su exigencia de explicación.
3. **Aplicar** los controles específicos que estos sistemas requieren.
4. **Reconocer** los límites y los modos de falla característicos.
5. **Diseñar** la supervisión humana de un sistema automatizado.

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

Los tres primeros términos son las familias de técnica; los cinco siguientes, los controles y los modos de fallo. La **alucinación** es el modo de fallo característico de los sistemas generativos: producen respuestas plausibles y falsas con la misma confianza que las correctas.

| Concepto | Comprensión verificable |
|---|---|
| `aprendizaje supervisado` | Aprende de ejemplos con la respuesta conocida. |
| `aprendizaje no supervisado` | Encuentra estructura sin respuestas etiquetadas. |
| `modelo de lenguaje` | Sistema que genera texto a partir de un contexto. |
| `alucinación` | Salida plausible y falsa de un modelo generativo. |
| `humano en el circuito` | Persona que revisa o decide antes del efecto. |
| `explicabilidad` | Capacidad de justificar una salida concreta. |
| `caso de uso de alto riesgo` | Aquel cuyo error daña derechos de una persona. |
| `deriva` | Degradación del desempeño por cambio del entorno. |

## 🧠 Modelo mental

El modelo mental es una clasificación por consecuencia: un modelo que ordena una lista de correos y uno que rechaza un crédito son la misma tecnología con exigencias radicalmente distintas. Lo que decide los controles es el efecto sobre la persona, no la sofisticación del algoritmo.

```text
LA PREGUNTA QUE ORDENA TODA LA CLASE

  ¿QUÉ PASA SI EL SISTEMA SE EQUIVOCA
   EN ESTE CASO CONCRETO?

  error sin consecuencia para nadie
    → automatización plena, control por muestreo
  error con consecuencia económica acotada
    → automatización con umbrales y revisión
  error que afecta derechos de una persona
    → decisión humana, sistema como apoyo
    → explicación obligatoria y derecho a revisión

la sofisticación técnica NO cambia esta clasificación
```

## 📖 Desarrollo

### 1. Tipos y usos

Las técnicas se aplican a usos concretos en banca. La tabla los relaciona.

| Tipo de sistema | Qué hace | Uso bancario típico |
|---|---|---|
| Clasificación supervisada | Asigna categorías | Admisión, fraude, cobranza |
| Regresión supervisada | Estima valores | Pérdida esperada, valoración |
| Agrupación no supervisada | Encuentra grupos | Segmentación, anomalías |
| Detección de anomalías | Señala lo atípico | Fraude, lavado, operación |
| Procesamiento de lenguaje | Entiende y genera texto | Atención, documentos, resúmenes |
| Visión | Interpreta imágenes | Verificación documental, biometría |
| Sistemas generativos | Producen contenido | Borradores, análisis, asistencia |
| Aprendizaje por refuerzo | Optimiza secuencias de decisión | Precios, cobranza (con cautela) |

### 2. Clasificación por riesgo

Los casos de uso se clasifican por su efecto sobre las personas, y de ahí salen los controles. La tabla los recoge.

```text
BAJO RIESGO — el error no daña a nadie
  · resumen de documentos internos
  · clasificación de correos
  · generación de borradores para revisión
  · optimización de rutas de proceso
  → automatización plena con control de calidad

RIESGO MEDIO — el error tiene costo económico acotado
  · priorización de gestiones de cobranza
  · detección de anomalías operativas
  · asistencia al analista con recomendaciones
  → automatización con umbrales y revisión por muestreo

ALTO RIESGO — el error afecta derechos o acceso
  · aprobación o rechazo de crédito
  · fijación de precio individual
  · cierre de cuentas
  · clasificación de riesgo de un cliente
  · decisiones de cumplimiento sobre personas
  → decisión humana informada, explicación y revisión
```

**El criterio no es la técnica sino la consecuencia.** Una regla simple que rechaza créditos es un
sistema de alto riesgo; un modelo sofisticado que ordena una lista de trabajo interno no lo es.

### 3. Controles específicos

Cada nivel de riesgo exige controles concretos. La tabla los recoge.

| Control | Qué previene |
|---|---|
| Validación independiente (Parte 11, clase 12) | Modelo incorrecto |
| Documentación del dominio de aplicación | Uso fuera de su rango válido |
| Pruebas de equidad por grupo | Sesgo sistemático |
| Explicabilidad de la decisión individual | Imposibilidad de justificar |
| Registro de decisiones y sus insumos | Falta de trazabilidad |
| Monitoreo de deriva | Degradación silenciosa |
| Supervisión humana significativa | Automatización sin responsable |
| Plan de reversión | Falla sin alternativa |

```text
SUPERVISIÓN HUMANA SIGNIFICATIVA
  no basta con que una persona apruebe la salida del sistema

  para ser significativa, la persona debe:
    · tener la información para evaluar la recomendación
    · tener tiempo real para hacerlo
    · tener autoridad y ausencia de presión para discrepar
    · ver el desempeño de sus discrepancias

  un revisor que aprueba 400 casos por hora
  no está supervisando: está firmando
```

### 4. Sistemas generativos

Los sistemas generativos tienen usos legítimos en banca y límites claros. La tabla los separa.

```text
LO QUE HACEN BIEN                    LO QUE NO HACEN
  redactar y resumir                   ser una fuente de verdad
  extraer información de texto         calcular con exactitud
  traducir entre formatos              garantizar consistencia
  asistir en búsqueda y análisis       decidir sobre personas
  generar borradores                   sustituir la verificación
```

El límite de la columna derecha no es una carencia que se corrija con más datos: es una consecuencia de cómo funciona el sistema, y de ahí salen las reglas de uso.

```text
LA ALUCINACIÓN NO ES UN ERROR CORREGIBLE: ES UNA PROPIEDAD
  el sistema genera lo plausible, no lo verificado

  CONSECUENCIA OPERATIVA
    toda salida que se use como información
    debe verificarse contra una fuente

  USOS SEGUROS: donde la verificación es barata o el error visible
  USOS PELIGROSOS: donde la salida se usa sin verificar
                   y el error es plausible
```

| Uso generativo en banca | Riesgo | Control |
|---|---|---|
| Resumen de documentos internos | Bajo | Revisión del usuario |
| Borrador de respuesta a cliente | Medio | Revisión obligatoria antes de enviar |
| Respuesta automática a cliente | Alto | Restringir a consultas cerradas y verificadas |
| Análisis de crédito | Alto | Solo como apoyo; la decisión no se automatiza |
| Asesoría de inversión | Muy alto | Deber de idoneidad; no automatizar |
| Interpretación de normativa | Alto | Siempre contrastar con la fuente |

### 5. Modos de falla característicos

Estos sistemas fallan de formas propias y reconocibles. La tabla las recoge.

```text
1. DERIVA SILENCIOSA
   el mundo cambia y el sistema sigue respondiendo
   con confianza sobre un mundo que ya no existe

2. FALLA CORRELACIONADA
   todos los casos fallan de la misma manera
   a diferencia del error humano, que es disperso
   → un error sistemático afecta a miles a la vez

3. AUTOMATIZACIÓN COMPLACIENTE
   el revisor humano deja de revisar porque
   el sistema "casi siempre acierta"

4. RETROALIMENTACIÓN
   el sistema rechaza a un grupo, no genera datos de ese grupo,
   y al reentrenarse confirma su propio sesgo

5. DEPENDENCIA DE UN PROVEEDOR
   el modelo lo provee un tercero que puede cambiarlo
   sin aviso (Parte 11, clase 11)
```

**La falla correlacionada es la diferencia esencial con el error humano.** Cien analistas se equivocan
de cien maneras distintas; un modelo se equivoca de la misma manera cien mil veces, y eso convierte un
error pequeño en un evento material.

## 🧮 Ejemplo guiado

El ejemplo clasifica tres casos de uso por su riesgo y define sus controles. Conviene fijarse en el caso de riesgo alto: exige humano en el circuito y explicación individual.

**Situación.** Un banco evalúa tres casos de uso propuestos por distintas áreas.

```text
CASO A — asistente de atención al cliente
  responde consultas de clientes por chat
  sobre productos, saldos y procedimientos
  volumen: 340 000 consultas al mes
  costo actual de atención humana: 0,0031 por consulta

CASO B — priorización de gestiones de cobranza
  ordena la lista diaria de clientes en mora
  por probabilidad de recuperación
  cartera en mora: 62 000 clientes
  capacidad de gestión: 4 800 contactos diarios

CASO C — decisión automática de admisión de crédito
  aprueba o rechaza solicitudes de consumo
  sin intervención humana
  solicitudes: 28 000 mensuales
  costo actual de análisis: 0,0084 por solicitud
```

**Paso 1 — clasifica cada caso por riesgo.**

```text
CASO A
  ¿qué pasa si se equivoca?
    respuesta incorrecta sobre un saldo o un procedimiento
    → el cliente actúa con información errónea
    → consecuencia económica posible, reclamo probable
  CLASIFICACIÓN: RIESGO MEDIO-ALTO según el alcance

CASO B
  ¿qué pasa si se equivoca?
    se contacta primero a quien iba a pagar igual
    y tarde a quien se podía recuperar
    → costo económico, sin daño a derechos
  CLASIFICACIÓN: RIESGO MEDIO

CASO C
  ¿qué pasa si se equivoca?
    se rechaza a quien podía pagar → exclusión, daño
    se aprueba a quien no podía → sobreendeudamiento, daño
    → AFECTA DERECHOS Y ACCESO DE UNA PERSONA
  CLASIFICACIÓN: ALTO RIESGO
```

**Paso 2 — evalúa el Caso B, el más sencillo.**

```text
SITUACIÓN ACTUAL
  62 000 clientes en mora, 4 800 contactos diarios
  orden actual: por monto adeudado, mayor a menor
  recuperación mensual: 3 840

CON PRIORIZACIÓN POR PROBABILIDAD DE RECUPERACIÓN × MONTO
  se maximiza el valor esperado recuperado por contacto
  mejora estimada en experimento controlado: +14,2 %
  recuperación adicional: 545 mensuales = 6 540 anuales

  costo del sistema: 280 inicial + 90 anuales
  BENEFICIO NETO: 6 394 anuales

CONTROLES NECESARIOS
  · el sistema NO decide la acción de cobranza,
    solo el ORDEN de la lista
  · reglas de protección: clientes vulnerables identificados
    salen de la priorización automática
  · límites de frecuencia de contacto por cliente
  · monitoreo de deriva trimestral
  · muestreo de casos no contactados para verificar
    que no se está abandonando sistemáticamente a un grupo

APROBADO
```

**Paso 3 — evalúa el Caso A.**

```text
DELIMITACIÓN DEL ALCANCE
  · consultas sobre PROCEDIMIENTOS (cómo hacer algo):
    respuesta verificable contra base documental → seguro
  · consultas sobre DATOS del cliente (saldo, movimientos):
    la respuesta viene de un sistema, no del modelo
    el modelo solo formula la consulta y presenta el dato → seguro
  · consultas de ASESORÍA (qué producto me conviene):
    deber de idoneidad → NO automatizar
  · RECLAMOS: derecho a respuesta fundamentada
    → NO automatizar la resolución

ALCANCE APROBADO: procedimientos y consulta de datos
  volumen dentro del alcance: 248 000 de 340 000  (73 %)
```

**Paso 4 — cuantifica el Caso A.**

```text
AHORRO
  248 000 × 0,0031 = 769 mensuales
  tasa de resolución sin escalar esperada: 78 %
  ahorro efectivo: 769 × 78 % = 600 mensuales = 7 200 anuales

COSTO
  desarrollo e integración: 1 400 inicial
  operación (infraestructura y modelo): 620 anuales
  revisión de calidad y actualización: 180 anuales

BENEFICIO NETO: 7 200 − 800 = 6 400 anuales, tras el primer año
```

```text
CONTROLES OBLIGATORIOS
  · el sistema declara que es un asistente automatizado
  · escalamiento a persona disponible SIEMPRE, en un clic
  · las respuestas sobre procedimientos se generan
    contra la base documental vigente, con cita de la fuente
  · registro completo de las conversaciones
  · muestreo diario de conversaciones revisadas por personas
  · métrica de alucinación: revisión de 500 respuestas
    semanales contra la fuente
  · reversión inmediata a atención humana si la tasa
    de error supera un umbral

APROBADO CON ALCANCE RESTRINGIDO
```

**Paso 5 — evalúa el Caso C.**

```text
LA PROPUESTA ES AUTOMATIZAR LA DECISIÓN COMPLETA

CUANTIFICACIÓN DEL AHORRO
  28 000 × 0,0084 = 235 mensuales = 2 820 anuales
  más rapidez: aprobación en minutos, no en días
  efecto comercial estimado: +8 % de conversión
  ingreso adicional: 1 640 anuales
  TOTAL: 4 460 anuales
```

```text
OBLIGACIONES QUE ACTIVA
  1. derecho del cliente a no ser objeto de una decisión
     basada únicamente en tratamiento automatizado
     que le produzca efectos jurídicos o le afecte
     significativamente
     → en la mayoría de las normas de datos personales
  2. derecho a obtener intervención humana
  3. derecho a una explicación de la decisión
  4. derecho a impugnar
  5. prueba de no discriminación por grupo protegido
```

**Paso 6 — rediseña el Caso C.**

```text
EN LUGAR DE AUTOMATIZACIÓN COMPLETA

  APROBACIONES AUTOMÁTICAS
    solicitudes que superan holgadamente todos los criterios
    → aprobar automáticamente NO afecta negativamente
      al solicitante
    volumen estimado: 41 % de las solicitudes

  RECHAZOS: NUNCA AUTOMÁTICOS
    toda solicitud que el sistema recomiende rechazar
    pasa a revisión humana con:
      · la recomendación y sus factores principales
      · los datos que la sustentan
      · tiempo suficiente para evaluarla
    volumen: 34 % de las solicitudes

  ZONA GRIS
    revisión humana con apoyo del sistema
    volumen: 25 %
```

**Paso 7 — recalcula.**

```text
AHORRO CON EL DISEÑO REVISADO
  41 % automatizado: 11 480 solicitudes × 0,0084 = 96 mensuales
  = 1 157 anuales
  efecto comercial de la rapidez en ese 41 %: 672 anuales
  TOTAL: 1 829 anuales

  frente a 4 460 de la automatización completa
  se pierde el 59 % del beneficio

COSTO DE LOS CONTROLES ADICIONALES
  explicabilidad de cada recomendación: 340 inicial
  registro y trazabilidad: 180 inicial + 60 anuales
  pruebas de equidad trimestrales: 90 anuales
  proceso de impugnación: 120 anuales
  TOTAL: 520 inicial + 270 anuales

BENEFICIO NETO: 1 829 − 270 = 1 559 anuales
```

**Paso 8 — decide y justifica.**

```text
DECISIONES
  CASO B: aprobado, con controles de protección   +6 394
  CASO A: aprobado con alcance restringido        +6 400
  CASO C: aprobado solo en modalidad asimétrica   +1 559

  TOTAL: 14 353 anuales

LA ASIMETRÍA DEL CASO C ES EL PUNTO CENTRAL
  automatizar la aprobación no daña a nadie
  automatizar el rechazo sí

  el mismo modelo, con la misma exactitud,
  tiene una obligación distinta según la dirección
  de su recomendación

OBSERVACIÓN DE GOBIERNO
  los tres casos comparten un requisito no negociable:
  la calidad de los datos de la clase 4
  ninguno funciona sobre datos que nadie gobierna
```

**Interpreta:** el caso con mayor beneficio aparente —automatizar la admisión— **terminó siendo el de
menor beneficio real**, porque las obligaciones que activa no son costos evitables: son derechos de las
personas afectadas. La asimetría entre aprobar y rechazar es el criterio más útil de toda la clase:
**automatiza lo que beneficia al afectado y mantén humana la decisión que lo perjudica**.

## 🏦 Del cliente al banco

El cliente recibe una decisión automática y el banco tiene que poder explicarla. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Me atendió un robot» | Asistente con alcance restringido | 14, clase 6 |
| «Me rechazó un sistema, no una persona» | Rechazo nunca automático | 14, clase 11 |
| «Me aprobaron en dos minutos» | Aprobación automática, sin daño | 14, clase 7 |
| «Nadie me explica por qué» | Derecho a explicación | 14, clase 11 |
| «El chat me dio información falsa» | Alucinación sin verificación | 14, clase 6 |

## 🧪 Práctica

El laboratorio pide clasificar casos de uso y definir controles proporcionales. Aplicar controles máximos a todo es tan incorrecto como no aplicarlos.

En `labs/lab-03.md`, sección de inteligencia artificial:

1. Clasifica ocho casos de uso por riesgo según su consecuencia.
2. Define el alcance seguro de un asistente conversacional.
3. Diseña la supervisión humana significativa de un sistema de alto riesgo.
4. Evalúa un caso de uso con su beneficio y el costo de sus controles obligatorios.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen sistemas de inteligencia artificial que causaron problemas. Las causas son controles no proporcionales y modos de fallo no previstos.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se clasifica por técnica, no por consecuencia | Criterio incorrecto | Pregunta qué pasa si se equivoca. |
| Supervisión humana nominal | Revisor sin tiempo ni autoridad | Hazla significativa o no la llames así. |
| Salida generativa usada sin verificar | Alucinación | Verifica contra fuente. |
| Se automatiza el rechazo | Afecta derechos | Automatiza solo lo que beneficia. |
| No se monitorea la deriva | Degradación silenciosa | Monitoreo periódico obligatorio. |
| Se ignora la falla correlacionada | Se compara con el error humano | Un error se replica a escala. |

## ❓ Preguntas de comprobación

1. ¿Qué pregunta clasifica el riesgo de un caso de uso?
2. ¿Qué hace significativa a una supervisión humana?
3. ¿Por qué la alucinación es una propiedad y no un error corregible?
4. ¿Por qué la falla correlacionada es distinta del error humano?
5. ¿Por qué aprobar y rechazar tienen obligaciones distintas?

## 📥 Entregable

Guarda en `portfolio/parte-14/clase-06/`:

- los ocho casos clasificados por riesgo con su justificación;
- el alcance seguro definido para un asistente conversacional;
- el diseño de supervisión humana significativa;
- la evaluación de un caso con beneficio y costo de controles.

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

- Financial Stability Board (2017). *Artificial intelligence and machine learning in financial services*. FSB. <https://www.fsb.org/2017/11/artificial-intelligence-and-machine-learning-in-financial-service/>
- Bank for International Settlements (2024). *Annual Economic Report*, capítulo sobre inteligencia artificial y el sistema financiero. BIS.
- OECD (2019, actualizada). *Recommendation of the Council on Artificial Intelligence*. OECD. <https://oecd.ai/en/ai-principles>
- NIST (2023). *AI Risk Management Framework (AI RMF 1.0)*. NIST. <https://www.nist.gov/itl/ai-risk-management-framework>
- Unión Europea (2024). *Reglamento (UE) 2024/1689 de inteligencia artificial*. Clasificación por riesgo.
- Board of Governors of the Federal Reserve System (2011). *SR 11-7: Guidance on Model Risk Management*.
- Verificación local: revisa si tu país tiene norma sobre decisiones automatizadas, el derecho a intervención humana y las obligaciones de explicación aplicables.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 05 · Analítica aplicada](05-analitica-aplicada.md) | [Parte 14](../README.md) · [Programa](../../../SYLLABUS.md) | [07 · Crédito digital y datos alternativos →](07-credito-digital-y-datos-alternativos.md) |
<!-- gen:footer:end -->
