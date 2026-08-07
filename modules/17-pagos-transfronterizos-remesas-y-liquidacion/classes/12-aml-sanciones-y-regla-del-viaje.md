<!-- meta
part: 18
class: 12
title: "AML, sanciones y regla del viaje"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global, chile]
regulatory_topics: [cross-border-payments, aml-cft, sanciones]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [GAFI, UAF]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 12 · AML, sanciones y regla del viaje

> [← 11 · Pagos empresariales y comercio exterior](11-pagos-empresariales-y-comercio-exterior.md) · [Índice de la parte](../README.md) · [13 · Interconexión de sistemas de pagos inmediatos →](13-interconexion-de-pagos-inmediatos.md)

**Parte 18 — Pagos transfronterizos, remesas y liquidación internacional** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Entender los tres controles que detienen pagos —prevención de lavado, sanciones y
regla del viaje— como lo que son: **obligaciones distintas, con lógicas distintas
y consecuencias distintas**. Confundirlas produce colas manuales y, a la vez,
huecos reales.

Todos los pagos de las clases anteriores atraviesan controles. Esta los desarrolla, y plantea su tensión propia: un filtro estricto bloquea pagos legítimos y uno laxo deja pasar los que no lo son, y no existe un punto sin error.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** prevención de lavado, sanciones y regla del viaje por su
   obligación, su lógica y su consecuencia.
2. **Explicar** qué información debe acompañar a una transferencia y qué pasa si
   falta.
3. **Calibrar** un sistema de coincidencias con precisión y exhaustividad.
4. **Diseñar** el proceso ante una coincidencia de sanciones, que no admite
   criterio comercial.
5. **Evaluar** el equilibrio entre falsos positivos y riesgo real con datos.

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

Los tres primeros términos son las obligaciones; los cinco siguientes, el cribado y sus medidas de calidad. La **regla del viaje** es la que obliga a que la información del ordenante y del beneficiario acompañe al pago en toda la cadena, y su incumplimiento es la causa más frecuente de devoluciones.

| Concepto | Comprensión verificable |
|---|---|
| `prevención de lavado` | Régimen basado en riesgo, con conocimiento del cliente y reporte |
| `sanciones` | Prohibición absoluta de operar con personas o entidades designadas |
| `regla del viaje` | Obligación de que ciertos datos acompañen a la transferencia |
| `screening` | Comparación de las partes contra listas |
| `falso positivo` | Coincidencia que tras revisión no corresponde |
| `precisión` | Proporción de alertas que son verdaderas |
| `exhaustividad` | Proporción de casos reales que el sistema detecta |
| `congelamiento` | Inmovilización de fondos exigida por una designación |

## 🧠 Modelo mental

El modelo mental es un filtro con dos errores posibles: bloquear pagos legítimos y dejar pasar los que no lo son. Subir el umbral reduce uno y aumenta el otro, y el punto se elige con criterio y no por defecto.

```text
TRES OBLIGACIONES QUE NO SE PARECEN

  PREVENCIÓN DE LAVADO
    lógica     basada en RIESGO: más control donde más riesgo
    criterio   proporcionalidad, juicio profesional
    fallo      no detectar un patrón sospechoso
    respuesta  reportar a la unidad de inteligencia financiera

  SANCIONES
    lógica     BINARIA: está en la lista o no está
    criterio   ninguno: no hay apetito de riesgo posible
    fallo      operar con una persona designada
    respuesta  bloquear, congelar y comunicar

  REGLA DEL VIAJE
    lógica     de DATOS: la información debe viajar
    criterio   completitud y exactitud de los campos
    fallo      transferencia sin la información exigida
    respuesta  rechazar, devolver o pedir completar

EL ERROR MÁS CARO
  aplicar criterio comercial a una coincidencia de sanciones.
  En prevención de lavado hay proporcionalidad.
  En sanciones no hay negociación posible.
```

## 📖 Desarrollo

### 1. La regla del viaje, en concreto

La regla del viaje se resume en una idea —la información del ordenante y del
beneficiario acompaña al pago— y se aplica con una lista concreta de campos. El
bloque la detalla y reparte la obligación entre las partes de la cadena.

```text
QUÉ DEBE ACOMPAÑAR A UNA TRANSFERENCIA

  DEL ORDENANTE
    nombre
    número de cuenta o identificador de la operación
    dirección, o número de identificación nacional,
    o número de cliente, o lugar y fecha de nacimiento

  DEL BENEFICIARIO
    nombre
    número de cuenta o identificador de la operación

QUÉ TIENE QUE HACER CADA PARTE
  ordenante      incluir la información y verificarla
  intermediario  CONSERVARLA: no puede eliminarla
  beneficiario   verificar que está y actuar si falta

EL PUNTO QUE SE INCUMPLE MÁS
  el intermediario que trunca campos para que el mensaje
  quepa en un formato antiguo. La información se pierde
  y el banco beneficiario recibe una transferencia
  incompleta que no puede aplicar ni justificar.

  → es una de las razones por las que ISO 20022 importa
    (clase 6): los campos estructurados no se truncan
```

### 2. Screening: precisión y exhaustividad

El filtrado contra listas se evalúa con dos medidas que se mueven en
direcciones opuestas. El bloque las define sobre la matriz de resultados y
explica por qué, en sanciones, no se equilibran: manda una de las dos.

```text
CUATRO RESULTADOS POSIBLES

                    es realmente     no lo es
  alerta            verdadero pos.   FALSO POSITIVO
  no alerta         FALSO NEGATIVO   verdadero neg.

  PRECISIÓN     VP / (VP + FP)   ¿cuántas alertas sirven?
  EXHAUSTIVIDAD VP / (VP + FN)   ¿cuántos casos detecto?

EL COMPROMISO
  bajar el umbral → más exhaustividad, menos precisión
  subirlo         → menos alertas, más falsos negativos

EN SANCIONES, LA EXHAUSTIVIDAD MANDA
  un falso negativo es una operación con una persona
  designada. No hay coste operativo que lo justifique.

EN PREVENCIÓN DE LAVADO, HAY EQUILIBRIO
  un modelo con 20 % de alertas y 2 % de reportes
  no está detectando mejor: está saturando la revisión
  y, por fatiga, PERDIENDO casos reales
```

### 3. Por qué hay tantos falsos positivos

| Causa | Ejemplo | Corrección |
|---|---|---|
| Nombres comunes | Apellidos muy frecuentes en un país | Reglas por origen del nombre |
| Transliteración | El mismo nombre escrito de cinco formas | Normalización fonética |
| Datos incompletos | Sin fecha de nacimiento no se puede descartar | Exigir campos adicionales |
| Coincidencia parcial | Solo el apellido coincide | Umbral por número de campos |
| Listas sin depurar | Entradas duplicadas o antiguas | Gestión de la fuente |
| Texto libre | La dirección no es comparable | Campos estructurados |

Frente a todas esas correcciones legítimas hay una que se propone siempre y
que no lo es.

```text
LA CORRECCIÓN QUE NUNCA ES CORRECTA
  «subimos el umbral porque hay demasiadas alertas»

  eso reduce el trabajo y aumenta el falso negativo.
  La corrección legítima es mejorar la CALIDAD
  de la comparación, no relajar el criterio.
```

### 4. Qué hacer ante una coincidencia de sanciones

Cuando salta una coincidencia, el margen de improvisación es nulo. El bloque
fija el procedimiento en orden y cierra con las tres cosas que no se hacen
nunca, por muy razonable que parezca la presión del momento.

```text
PROCEDIMIENTO, SIN EXCEPCIONES

  1. DETENER la operación. No ejecutar «mientras se revisa».
  2. Escalar al responsable designado, no al comercial.
  3. Verificar la coincidencia con datos adicionales.
  4. Si se descarta: documentar POR QUÉ y liberar.
  5. Si se confirma: bloquear o congelar según la norma,
     comunicar a la autoridad en el plazo exigido,
     y NO informar al cliente del motivo si la norma
     lo prohíbe.
  6. Conservar la evidencia completa.

LO QUE NUNCA SE HACE
  · liberar por presión comercial
  · ejecutar y reportar después
  · avisar al cliente para que retire la operación
  · resolver la coincidencia sin documentarlo
```

### 5. El efecto sobre el acceso

El cumplimiento estricto tiene un efecto secundario medible sobre quién queda
dentro y fuera del sistema. El bloque expone la tensión, la conecta con las
clases 3 y 10 y precisa dónde cabe proporcionalidad y dónde no.

```text
LA TENSIÓN CENTRAL DE ESTA CLASE

  el cumplimiento estricto protege el sistema
  y, aplicado sin proporcionalidad, expulsa
  a clientes, corredores y países enteros

  → retirada de corresponsalías (clase 3)
  → remesas hacia canales informales (clase 10)
  → organizaciones humanitarias sin acceso bancario

LA RESPUESTA NO ES RELAJAR SANCIONES
  es aplicar la proporcionalidad DONDE LA NORMA
  la admite —prevención de lavado— y no donde no
  la admite —designaciones—, y mejorar la calidad
  de los datos para que el control sea preciso
  en vez de amplio
```

## 🧮 Ejemplo guiado

El ejemplo calibra un sistema de cribado midiendo precisión y exhaustividad. Conviene mirar las dos juntas: mejorar una empeora la otra.

**Situación.** Un banco revisa su sistema de screening. La cola manual crece y el
área de negocio pide subir el umbral.

```text
DATOS DEL TRIMESTRE
  pagos internacionales procesados       420 000
  alertas generadas                       31 500   7,5 %
  alertas revisadas y descartadas         31 118
  coincidencias confirmadas                    9
  operaciones bloqueadas                       9
  reportes por operación sospechosa          373

COSTE DE REVISIÓN: 11 USD por alerta
PLANTILLA DE REVISIÓN: 14 personas
TIEMPO MEDIO DE REVISIÓN POR ALERTA: 6 minutos
DEMORA MEDIA INTRODUCIDA: 3,2 horas

PROPUESTA DE NEGOCIO
  «subir el umbral de coincidencia del 82 % al 90 %
   reduciría las alertas un 58 %»
```

**Paso 1 — calcula la precisión actual.**

```text
PRECISIÓN EN SANCIONES
  9 / 31 500 = 0,029 %

  es decir: 1 alerta útil por cada 3 500

COSTE DE LA REVISIÓN
  31 500 × 11 = 346 500 USD por trimestre
  1 386 000 USD al año

COSTE POR COINCIDENCIA ENCONTRADA
  346 500 / 9 = 38 500 USD
```

**Paso 2 — evalúa la propuesta de subir el umbral.**

```text
CON UN 58 % MENOS DE ALERTAS
  alertas: 13 230
  ahorro: 18 270 × 11 = 200 970 USD/trimestre

LA PREGUNTA QUE FALTA
  ¿cuántas de las 9 coincidencias confirmadas
  habrían quedado por debajo del 90 %?

PRUEBA RETROSPECTIVA
  se recalculan las 9 con el umbral nuevo:
    puntuación ≥ 90 %:  6
    puntuación 82–90 %: 3

  → subir el umbral habría dejado pasar 3 operaciones
    con personas designadas
```

**Paso 3 — evalúa esas 3.**

```text
NO HAY CÁLCULO DE COSTE-BENEFICIO QUE APLICAR

  una operación ejecutada con una persona designada
  es un incumplimiento. Las consecuencias no se
  distribuyen normalmente: incluyen sanción,
  pérdida de relaciones de corresponsalía
  y, en casos graves, la viabilidad del negocio
  internacional del banco.

  200 970 USD de ahorro trimestral frente a eso
  no es una comparación: es una categoría distinta.

DECISIÓN SOBRE LA PROPUESTA: RECHAZADA
```

**Paso 4 — busca la corrección legítima.**

```text
EL PROBLEMA ES REAL: 31 500 ALERTAS SON DEMASIADAS.
LA SOLUCIÓN NO ES EL UMBRAL, ES LA CALIDAD.

  ANÁLISIS DE LAS 31 118 DESCARTADAS
    coincidencia solo por apellido común       14 220   45,7 %
    transliteración de nombres                  7 890   25,4 %
    falta de fecha de nacimiento para descartar 5 106   16,4 %
    entidad con nombre genérico                 2 480    8,0 %
    otras                                       1 422    4,6 %
```

**Paso 5 — cuantifica cada corrección.**

```text
C1 · EXIGIR SEGUNDO CAMPO COINCIDENTE
     para apellidos de alta frecuencia
     efecto: −11 400 alertas
     riesgo: si el segundo campo falta, NO se descarta:
             se envía a revisión igualmente
     coste: 26 000 USD

C2 · NORMALIZACIÓN FONÉTICA POR ORIGEN DEL NOMBRE
     efecto: −6 300 alertas
     mejora TAMBIÉN la exhaustividad: detecta variantes
     que hoy no coinciden con ninguna entrada
     coste: 48 000 USD

C3 · EXIGIR FECHA DE NACIMIENTO EN EL MENSAJE
     efecto: −4 100 alertas
     depende de que el ordenante la envíe (clase 6)
     coste: 15 000 USD

C4 · DEPURAR LA LISTA DE ENTIDADES GENÉRICAS
     efecto: −1 900 alertas
     coste: 9 000 USD

TOTAL: −23 700 alertas (−75,2 %)
ALERTAS RESULTANTES: 7 800
COSTE DE IMPLANTACIÓN: 98 000 USD
AHORRO ANUAL: 23 700 × 11 × 4 = 1 042 800 USD
RETORNO: 5 semanas
```

**Paso 6 — comprueba el efecto sobre la exhaustividad.**

```text
LA PRUEBA QUE NO SE PUEDE OMITIR

  se vuelven a pasar las 9 coincidencias confirmadas
  por el sistema corregido:
    detectadas: 9 de 9  ✓

  y se prueba con un conjunto de casos sintéticos
  construidos a partir de variantes conocidas:
    detectados por el sistema actual:    41 de 60
    detectados por el corregido:         57 de 60

  → la corrección MEJORA la exhaustividad
    mientras reduce el ruido

  LOS 3 NO DETECTADOS
    se analizan uno a uno y se documentan como
    limitación conocida del sistema, con su plan
```

**Paso 7 — cierra con la diferencia de fondo.**

```text
LAS 373 OPERACIONES REPORTADAS POR SOSPECHA
NO SON EL MISMO PROBLEMA

  ese es el régimen de prevención de lavado,
  donde SÍ hay proporcionalidad y juicio profesional

  ahí la pregunta correcta no es «¿cuántas alertas?»
  sino «¿los analistas tienen tiempo para pensar?»

  CON 31 500 ALERTAS Y 14 PERSONAS
    31 500 × 6 min = 3 150 horas por trimestre
    por persona: 225 horas de 480 disponibles
    → casi la mitad del tiempo revisando ruido

  CON 7 800 ALERTAS
    56 horas por persona
    → tiempo para análisis real de los casos
      que sí lo merecen

EL BENEFICIO MAYOR DE LA CORRECCIÓN NO ES EL AHORRO:
ES QUE EL EQUIPO PUEDE HACER SU TRABAJO
```

**Interpreta:** la propuesta de negocio —subir el umbral— habría ahorrado dinero
dejando pasar tres operaciones prohibidas. La corrección correcta atacó la
**calidad de la comparación**, redujo el ruido un 75 % y **mejoró** la detección.
En sanciones, el ruido no se resuelve relajando el criterio.

## 🧭 Perspectivas

El cumplimiento afecta a cada participante con obligaciones propias. La tabla las recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Su pago detenido 3,2 horas | Si reclama o cambia |
| Negocio | Cola que afecta al servicio | Si presiona por el umbral |
| Cumplimiento | 1 alerta útil por cada 3 500 | Cómo mejora la calidad |
| Analista | Media jornada revisando ruido | Su capacidad de análisis real |
| Corresponsal | Calidad del control del respondedor | Si mantiene la relación |
| Supervisor | Exhaustividad del sistema | Si observa el umbral |
| Autoridad de sanciones | Operaciones bloqueadas y comunicadas | Si sanciona |

## 🏦 Del cliente al banco

El cliente sufre una demora y el banco cumple una obligación con sanción asociada. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Mi pago lleva horas detenido» | Alerta en cola de revisión | 18, clase 12 |
| «Me piden mi fecha de nacimiento» | Campo que permite descartar | 18, clases 6 y 12 |
| «Me devolvieron el pago sin motivo» | La norma puede prohibir explicarlo | 18, clase 12 |
| «Mi ONG no consigue banco» | Efecto del cumplimiento sin proporcionalidad | 18, clases 3 y 12 |

## ⚖️ Riesgos y controles

Los riesgos son de cumplimiento y de exclusión. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Falso negativo en sanciones | Umbral relajado por presión | Prueba retrospectiva antes de tocar el umbral |
| Fatiga del analista | Media jornada revisando ruido | Mejorar la calidad, no el umbral |
| Información truncada | El intermediario elimina campos | Campos estructurados y verificación en destino |
| Criterio comercial en sanciones | Se libera por presión | Escalado a responsable designado |
| Lista desactualizada | Se opera con datos viejos | Actualización con alerta de fallo |
| Exclusión por sobrecumplimiento | Se cierra un corredor entero | Proporcionalidad donde la norma la admite |

## 🧪 Práctica

El laboratorio pide calibrar un cribado y medir sus dos errores. El punto elegido con su justificación es lo que se evalúa.

En [`labs/lab-04.md`](../labs/lab-04.md):

1. Clasifica quince casos en las tres obligaciones.
2. Calcula precisión y exhaustividad de un sistema con datos dados.
3. Ejecuta la prueba retrospectiva de un cambio de umbral.
4. Diseña el procedimiento ante una coincidencia, paso a paso.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen pagos bloqueados o devueltos. Las causas son datos incompletos y cribado sin calibrar.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Subir el umbral por la cola | Se optimizó el trabajo | Prueba retrospectiva primero |
| Tratar sanciones como riesgo | Se aplicó proporcionalidad | Es binario, sin apetito |
| Truncar campos | Se adaptó a un formato antiguo | Conservar la información |
| Medir solo alertas | Se ignoró la exhaustividad | Mide las dos métricas |
| Liberar sin documentar | Se resolvió verbalmente | Evidencia de cada descarte |
| Cerrar corredores enteros | Se aplicó criterio por país | Criterio por cliente y operación |

## ❓ Preguntas de comprobación

1. ¿En qué se diferencian la lógica de sanciones y la de prevención de lavado?
2. ¿Qué información debe acompañar a una transferencia y quién debe conservarla?
3. ¿Qué es la prueba retrospectiva y por qué es obligatoria antes de tocar un
   umbral?
4. ¿Por qué reducir falsos positivos puede mejorar la detección?
5. ¿Cuál es el mayor beneficio de reducir el ruido, y por qué no es el ahorro?

## 📥 Entregable

Guarda en `portfolio/parte-18/clase-12/`:

- quince casos clasificados en las tres obligaciones;
- el cálculo de precisión y exhaustividad de un sistema;
- una prueba retrospectiva completa de un cambio de umbral;
- el procedimiento ante coincidencia, con sus seis pasos y su evidencia.

## 🔗 Referencias cruzadas

- **Viene de:** clases 2, 3 y 6; Parte 12, clases 3 a 6 (cumplimiento).
- **Continúa en:** clase 14 (stablecoins y trazabilidad), clase 16 (proyecto).
- **Se aplica en:** Parte 20, clase 15 (KYT y regla del viaje en activos
  virtuales); Parte 23, clase 15.

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

- Financial Action Task Force. *Las Recomendaciones del GAFI*, en particular la Recomendación 16 y su nota interpretativa. FATF. <https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html>
- Financial Action Task Force. *Guidance for a risk-based approach*. FATF. <https://www.fatf-gafi.org/>
- Basel Committee on Banking Supervision (2020). *Sound management of risks related to money laundering and financing of terrorism*. BIS. <https://www.bis.org/bcbs/publ/d505.htm>
- Wolfsberg Group. *Guidance on sanctions screening*. <https://www.wolfsberg-group.org/>
- Unidad de Análisis Financiero (Chile). *Normativa aplicable y guías de reporte*. UAF. <https://www.uaf.cl/>
- Verificación local: comprueba qué listas de sanciones te obligan, qué plazos de comunicación aplican y qué información exige tu jurisdicción que acompañe a las transferencias. **Fecha de verificación de esta clase: 2026-08-06.** Esta clase no constituye asesoría legal.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 11 · Pagos empresariales y comercio exterior](11-pagos-empresariales-y-comercio-exterior.md) | [Parte 18](../README.md) · [Programa](../../../SYLLABUS.md) | [13 · Interconexión de sistemas de pagos inmediatos →](13-interconexion-de-pagos-inmediatos.md) |
<!-- gen:footer:end -->
