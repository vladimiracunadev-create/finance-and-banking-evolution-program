<!-- meta
part: 14
class: 7
title: "Crédito digital y datos alternativos"
level: profesional
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 07 · Crédito digital y datos alternativos

> [← 06 · Inteligencia artificial en banca](06-inteligencia-artificial-en-banca.md) · [Índice de la parte](../README.md) · [08 · Fraude digital →](08-fraude-digital.md)

**Parte 14 — Fintech, datos e inteligencia artificial** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Evaluar solvencia sin historial crediticio. Es la aplicación de datos con mayor potencial de inclusión
del sector —cientos de millones de personas no tienen historial— y también la de mayor potencial de
daño, porque un dato alternativo mal usado excluye con apariencia de objetividad.

El crédito de la Parte 9 usa datos financieros. Esta clase añade los que no lo son, y con ellos una promesa y un riesgo: permiten evaluar a quien no tiene historial, y permiten discriminar por variables que ninguna política habría aprobado. Distinguir un uso del otro es todo el contenido de la clase.

## 📚 Objetivos

Al finalizar podrás:

1. **Identificar** las fuentes de datos alternativos y su poder predictivo.
2. **Evaluar** un dato alternativo por su validez, estabilidad y aceptabilidad.
3. **Diseñar** un proceso de originación digital completo.
4. **Medir** el efecto sobre la inclusión y sobre el riesgo.
5. **Reconocer** los usos inaceptables y sus razones.

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

Los cinco primeros términos son la evaluación del dato; los tres siguientes, el producto digital. La **variable sustituta** es el riesgo central: un dato aparentemente neutro que en la práctica identifica un atributo protegido, y que produce discriminación sin que nadie la haya decidido.

| Concepto | Comprensión verificable |
|---|---|
| `dato alternativo` | Información no crediticia usada para evaluar solvencia. |
| `sin historial` | Persona sin registro en los burós de crédito. |
| `poder predictivo` | Capacidad del dato de discriminar buenos de malos pagadores. |
| `estabilidad` | Que el dato mantenga su relación con el resultado en el tiempo. |
| `manipulabilidad` | Facilidad con que el solicitante puede alterar el dato. |
| `variable sustituta` | Dato que actúa como aproximación de un atributo prohibido. |
| `originación digital` | Proceso completo sin presencia física. |
| `préstamo escalonado` | Estrategia de límites crecientes según comportamiento. |

## 🧠 Modelo mental

El modelo mental son tres filtros que un dato alternativo debe pasar: que prediga, que sea estable en el tiempo y que el solicitante no lo pueda manipular. Un dato que falla cualquiera de los tres no sirve, por muy correlacionado que esté.

```text
EL PROBLEMA QUE RESUELVEN LOS DATOS ALTERNATIVOS

  sin historial crediticio → sin evaluación posible
  sin evaluación → sin crédito
  sin crédito → nunca se genera historial

  es un círculo que excluye a quien nunca entró al sistema

LOS DATOS ALTERNATIVOS LO ROMPEN
  usando información que la persona SÍ genera:
  pagos de servicios, flujo de una cuenta, ventas de un negocio

Y LA PREGUNTA CRÍTICA ES SIEMPRE LA MISMA
  ¿este dato mide capacidad de pago,
   o mide una característica de la persona
   que se correlaciona con su origen o su condición?
```

## 📖 Desarrollo

### 1. Fuentes y su valor

Las fuentes de datos alternativos se diferencian mucho en poder predictivo y en aceptabilidad. La tabla las recoge.

| Fuente | Qué mide | Poder predictivo | Aceptabilidad |
|---|---|---|---|
| Pagos de servicios básicos | Cumplimiento de obligaciones recurrentes | Alto | Alta |
| Flujo de cuenta bancaria | Ingreso real y estabilidad | Muy alto | Alta |
| Ventas por medios de pago | Ingreso de un negocio | Muy alto | Alta |
| Pagos de arriendo | Cumplimiento y capacidad | Alto | Alta |
| Historial con proveedores | Comportamiento comercial | Alto | Alta |
| Datos de telefonía (recarga, plan) | Estabilidad y capacidad | Medio | Media |
| Datos de comercio electrónico | Consumo y estabilidad | Medio | Media |
| Comportamiento en la aplicación | Atención, consistencia | Bajo-medio | Baja |
| Redes sociales | — | Bajo | Muy baja |
| Contactos del teléfono | — | Espurio | Inaceptable |

```text
LA REGLA DE EVALUACIÓN DE UN DATO ALTERNATIVO

  1. ¿tiene relación CAUSAL plausible con la capacidad de pago?
     si solo hay correlación sin mecanismo, desconfía
  2. ¿es estable en el tiempo?
  3. ¿es manipulable por el solicitante?
  4. ¿es verificable?
  5. ¿su uso es aceptable para el afectado si se lo explicas?
  6. ¿actúa como sustituto de un atributo prohibido?

el punto 5 es la prueba práctica más útil:
si no puedes explicárselo al cliente sin que le parezca abusivo,
no lo uses
```

### 2. Usos inaceptables

Hay datos que predicen y no se pueden usar, por razones legales o éticas. La tabla los recoge con su razón.

```text
· contactos del teléfono como señal de riesgo
  → convierte la relación social en garantía implícita
  → habilita cobranza a terceros no obligados

· redes sociales y opiniones personales
  → sin relación causal, alto riesgo de discriminación

· ubicación como sustituto de zona socioeconómica
  → sustituto de origen; excluye por dirección

· patrones de uso que reflejan discapacidad o edad
  → discriminación por condición protegida

· datos obtenidos sin consentimiento específico
  → ilícito, con independencia de su poder predictivo

EL CRITERIO NO ES SI FUNCIONA: ES SI ES LEGÍTIMO
un dato puede predecir bien y ser inaceptable
```

### 3. Originación digital

La originación digital tiene un recorrido propio con puntos de abandono medibles. El esquema lo recorre.

```text
FLUJO COMPLETO
  1. SOLICITUD          datos mínimos, en pasos cortos
  2. IDENTIDAD          verificación documental y biométrica
  3. DATOS              consentimiento para fuentes alternativas
  4. EVALUACIÓN         modelo con datos tradicionales y alternativos
  5. OFERTA             monto, plazo y tasa personalizados
  6. INFORMACIÓN        costo total, con comprensión verificada
  7. FIRMA              electrónica con evidencia
  8. DESEMBOLSO         a cuenta verificada del solicitante
  9. SEGUIMIENTO        comportamiento y actualización del límite
```

| Punto del flujo | Riesgo | Control |
|---|---|---|
| Identidad | Suplantación, identidad sintética | Biometría con prueba de vida |
| Datos | Consentimiento no informado | Alcance y fin específicos |
| Evaluación | Sesgo, dato manipulable | Pruebas de equidad y verificabilidad |
| Oferta | Sobreendeudamiento | Verificación de deuda total |
| Información | Incomprensión del costo | Costo total y verificación de comprensión |
| Desembolso | Fraude por cuenta de tercero | Cuenta a nombre del solicitante |

```text
LA FRICCIÓN ES UN CONTROL, NO UN DEFECTO
  un proceso de 90 segundos maximiza la conversión
  y minimiza la reflexión del solicitante

  en crédito de consumo, parte de la fricción
  cumple una función de protección
```

### 4. Préstamo escalonado

El préstamo escalonado construye historial con exposiciones crecientes. El esquema lo describe.

```text
ESTRATEGIA PARA QUIEN NO TIENE HISTORIAL

  paso 1: monto pequeño, plazo corto, precio con prima alta
  paso 2: si cumple, monto mayor y precio menor
  paso 3: si cumple, límite mayor, plazos más largos
  ...

  el propio comportamiento genera la información
  que permite aumentar la exposición
```

```text
POR QUÉ FUNCIONA
  · la pérdida máxima del primer paso es acotada
  · cada paso genera datos propios, mucho más predictivos
    que cualquier dato alternativo
  · el cliente construye historial

RIESGO DEL DISEÑO
  si el escalonamiento es demasiado rápido,
  se construye sobreendeudamiento con apariencia
  de buen comportamiento
  → el límite debe crecer con la CAPACIDAD verificada,
    no solo con el cumplimiento
```

### 5. Medir inclusión y riesgo a la vez

Un modelo puede incluir más y perder menos, y las dos cosas se miden juntas. El procedimiento lo hace.

```text
DOS MÉTRICAS QUE DEBEN REPORTARSE JUNTAS

  INCLUSIÓN
    · solicitantes sin historial aprobados
    · tasa de aprobación por segmento
    · primer crédito formal de la persona

  RIESGO
    · mora por cosecha y por segmento
    · sobreendeudamiento posterior
    · reincidencia en mora

  REPORTAR SOLO INCLUSIÓN produce colocación irresponsable
  REPORTAR SOLO RIESGO produce exclusión conservadora
```

## 🧮 Ejemplo guiado

El ejemplo evalúa tres datos alternativos con los tres filtros. Uno de ellos predice bien y es manipulable, y por eso no sirve.

**Situación.** Un banco evalúa incorporar datos alternativos a su admisión de consumo.

```text
SITUACIÓN ACTUAL
  solicitudes mensuales                        28 000
  con historial en buró                        18 200  (65 %)
  sin historial                                 9 800  (35 %)
  aprobación con historial                       48 %
  aprobación sin historial                        6 %
  monto medio                                     3,2
  mora a 12 meses de la cartera actual           4,8 %

DATOS ALTERNATIVOS DISPONIBLES
  pagos de servicios básicos (con consentimiento)
  flujo de cuenta en el propio banco (para clientes)
  ventas por medios de pago (para comercios)
```

**Paso 1 — evalúa cada dato con la regla de seis puntos.**

```text
PAGOS DE SERVICIOS BÁSICOS
  1. causalidad: cumplir obligaciones recurrentes
     con monto fijo predice cumplimiento de crédito  ✓
  2. estable: sí, con series de 12+ meses  ✓
  3. manipulable: difícilmente  ✓
  4. verificable: con la empresa de servicios  ✓
  5. explicable al cliente: sí  ✓
  6. sustituto prohibido: cuidado — tener servicios
     a nombre propio correlaciona con formalidad
     y con condición de propietario o arrendatario formal
     → verificar con pruebas de equidad
  ACEPTABLE con verificación

FLUJO DE CUENTA PROPIA
  1. causalidad: mide ingreso y estabilidad directamente  ✓
  2-5: todos ✓
  6. solo disponible para quien ya es cliente
     → NO excluye a nadie, pero solo ayuda a algunos
  ACEPTABLE

VENTAS POR MEDIOS DE PAGO
  aplicable solo a comercios; excelente para ese segmento
  ACEPTABLE
```

**Paso 2 — mide el poder predictivo sobre una muestra retrospectiva.**

```text
MUESTRA: 14 200 créditos otorgados hace 18 meses
a solicitantes que HOY tienen datos alternativos disponibles

MODELO ACTUAL (solo buró y declarados)
  Gini: 0,42 sobre el subconjunto sin historial pleno

MODELO CON DATOS ALTERNATIVOS
  + pagos de servicios (18 meses):     Gini 0,54
  + flujo de cuenta (12 meses):        Gini 0,61
  + ambos:                             Gini 0,64

la mejora es sustancial en el segmento sin historial
```

**Paso 3 — simula el efecto sobre la aprobación.**

```text
SEGMENTO SIN HISTORIAL: 9 800 solicitudes mensuales

CON EL MODELO ACTUAL
  aprobados: 588  (6 %)
  mora esperada a 12 meses: 9,2 %

CON DATOS ALTERNATIVOS
  el modelo distingue dentro del segmento
  aprobados con el mismo umbral de riesgo: 2 842  (29 %)
  mora esperada: 7,4 %

INCLUSIÓN: +2 254 personas al mes acceden a crédito formal
```

**Paso 4 — verifica que no se esté relajando el criterio.**

```text
LA APROBACIÓN SUBE Y LA MORA ESPERADA BAJA
¿es coherente?

  sí, y esa es exactamente la promesa de un mejor modelo:
  al discriminar mejor, se aprueban buenos que antes
  se rechazaban por desconocimiento

VERIFICACIÓN
  distribución de la mora esperada de los aprobados
    modelo actual:      media 9,2 %, todos en un rango estrecho
    modelo alternativo: media 7,4 %, con dispersión mayor
      · 42 % con mora esperada < 5 %
      · 38 % entre 5 % y 9 %
      · 20 % entre 9 % y 12 %

  el modelo actual no podía identificar al 42 %
  de bajo riesgo: los rechazaba junto con el resto
```

**Paso 5 — ejecuta las pruebas de equidad.**

```text
TASA DE APROBACIÓN POR GRUPO, MODELO ALTERNATIVO

  grupo                        aprobación   mora esperada
  con vivienda propia             34 %          6,8 %
  con arriendo formal             31 %          7,1 %
  con arriendo informal           18 %          8,4 %
  sin domicilio estable            9 %          9,6 %

  trabajador formal               38 %          6,2 %
  trabajador independiente        24 %          8,1 %
  trabajador informal             16 %          9,1 %
```

```text
ANÁLISIS
  la diferencia de aprobación entre formal e informal
  es de 22 puntos, y la de mora esperada, de 2,9 puntos

  ¿la diferencia de aprobación está JUSTIFICADA
   por la diferencia de riesgo?

  al mismo nivel de mora esperada, ¿se aprueba igual?
    corte al 8 % de mora esperada:
      formales bajo el corte: 78 % del grupo → aprobados
      informales bajo el corte: 34 % del grupo → aprobados
    dentro de cada grupo, el criterio es el MISMO

  → no hay trato diferenciado por grupo:
    hay distinta distribución de riesgo dentro del grupo

PERO EL EFECTO AGREGADO ES DE MENOR ACCESO
  y eso debe declararse y gestionarse,
  no justificarse solo con la corrección técnica
```

**Paso 6 — diseña el escalonamiento para los más riesgosos.**

```text
LOS 20 % CON MORA ESPERADA ENTRE 9 % Y 12 %
  aprobarlos con el monto medio de 3,2 produce pérdidas

  ALTERNATIVA: préstamo escalonado
    paso 1: monto 0,8, plazo 6 meses, tasa con prima
    paso 2 (si cumple): monto 1,6, plazo 12 meses
    paso 3: monto 3,2, tasa reducida

  pérdida máxima del paso 1: 0,8 × 12 % × 65 % = 0,062
  frente a 3,2 × 12 % × 65 % = 0,250

  y el 68 % que cumple el paso 1
  tiene mora del 4,1 % en el paso 2
  → el propio comportamiento reveló la información
```

**Paso 7 — cuantifica el resultado.**

```text
COLOCACIÓN ADICIONAL MENSUAL
  aprobados adicionales de riesgo bajo y medio (80 %): 1 803
    monto 3,2 → 5 770
  aprobados adicionales escalonados (20 %): 451
    monto 0,8 → 361
  TOTAL: 6 131 mensuales = 73 572 anuales

RESULTADO
  margen financiero (18,4 % − costo de fondos 6,2 %): 8 976
  pérdida esperada: 73 572 × 7,4 % × 65 % = 3 539
  costo operativo: 2 254 × 12 × 0,0084 = 227
  costo de datos alternativos: 2 254 × 12 × 0,0006 = 16
  costo del capital: 73 572 × 9,2 % × 14 % = 948
  RESULTADO NETO: 4 246 anuales

INCLUSIÓN
  27 048 personas al año acceden a su primer crédito formal
```

**Paso 8 — define las obligaciones de gestión.**

```text
1. MEDICIÓN CONJUNTA
   reportar al comité, en el mismo cuadro:
     · personas incluidas por primera vez
     · mora por cosecha del segmento sin historial
     · sobreendeudamiento posterior de los incluidos
     · tasa de aprobación por grupo

2. TRANSPARENCIA
   informar al solicitante qué datos se usaron
   y permitir corregir los inexactos

3. PRUEBAS DE EQUIDAD TRIMESTRALES
   con el análisis del paso 5, no solo la tasa agregada

4. LÍMITE AL ESCALONAMIENTO
   el límite crece con la capacidad verificada,
   no solo con el cumplimiento
   verificación de deuda total en cada paso

5. REVISIÓN DEL DATO
   si un dato alternativo pierde poder predictivo
   o su relación causal deja de ser plausible, se retira
   → revalidación anual (Parte 11, clase 12)
```

**Interpreta:** los datos alternativos multiplicaron por casi cinco el acceso al crédito formal del
segmento sin historial **y redujeron la mora esperada**, porque el problema nunca fue que esas personas
fueran peores pagadoras: era que el banco no podía distinguir entre ellas. La prueba de equidad del paso
5 muestra el límite honesto del logro: el criterio es el mismo para todos y **el efecto agregado sigue
siendo de menor acceso para el trabajador informal**. Reconocer esa diferencia es parte del trabajo, no
una objeción a él.

## 🏦 Del cliente al banco

El solicitante sin historial no accede al crédito y el banco puede evaluarlo con otros datos. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Nunca tuve crédito y por eso no me dan» | El círculo de la falta de historial | 14, clase 7 |
| «Autoricé que vieran mis pagos de servicios» | Dato alternativo con consentimiento | 14, clase 3 |
| «Me dieron poco y luego más» | Préstamo escalonado | 14, clase 7 |
| «El proceso fue muy rápido» | La fricción también protege | 4, clase 12 |
| «Usaron datos que no esperaba» | Transparencia sobre las fuentes | 12, clase 10 |

## 🧪 Práctica

El laboratorio pide evaluar datos alternativos y detectar variables sustitutas. Una de las variables propuestas identifica un atributo protegido.

En `labs/lab-04.md`:

1. Evalúa ocho datos alternativos con la regla de seis puntos.
2. Mide el poder predictivo de un dato sobre una muestra retrospectiva.
3. Ejecuta pruebas de equidad y distingue trato diferenciado de distinta distribución.
4. Diseña un esquema de préstamo escalonado con sus límites.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen modelos con datos alternativos que fallaron. Las causas son datos manipulables y variables sustitutas no detectadas.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se usa un dato porque predice | Sin evaluar legitimidad | Aplica los seis puntos. |
| Contactos o redes sociales como señal | Inaceptable | Retíralos. |
| Se reporta solo inclusión | Colocación irresponsable | Reporta inclusión y riesgo juntos. |
| Escalonamiento por cumplimiento solo | Sobreendeudamiento | El límite sigue a la capacidad. |
| Proceso sin fricción alguna | Sin reflexión del solicitante | La fricción también protege. |
| Equidad medida solo en agregado | Oculta el mecanismo | Analiza a igual nivel de riesgo. |

## ❓ Preguntas de comprobación

1. ¿Qué círculo rompen los datos alternativos?
2. ¿Cuál es la prueba práctica más útil para aceptar un dato alternativo?
3. ¿Por qué la aprobación puede subir y la mora esperada bajar a la vez?
4. ¿Qué distingue trato diferenciado de distinta distribución de riesgo?
5. ¿Por qué el límite del escalonamiento debe seguir a la capacidad y no al cumplimiento?

## 📥 Entregable

Guarda en `portfolio/parte-14/clase-07/`:

- los ocho datos evaluados con la regla de seis puntos;
- la medición de poder predictivo sobre la muestra;
- las pruebas de equidad con su análisis por nivel de riesgo;
- el esquema de préstamo escalonado con sus límites y verificaciones.

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

- World Bank y CGAP (2019). *Alternative Data Transforming SME Finance*. World Bank Group.
- Financial Stability Board (2017). *Artificial intelligence and machine learning in financial services*. FSB.
- Consumer Financial Protection Bureau (2017). *Request for Information Regarding Use of Alternative Data and Modeling Techniques*. CFPB.
- Siddiqi, N. (2017). *Intelligent Credit Scoring* (2.ª ed.). Wiley.
- Berg, T., Burg, V., Gombović, A. y Puri, M. (2020). "On the Rise of FinTechs: Credit Scoring Using Digital Footprints". *Review of Financial Studies*, 33(7).
- OECD (2020). *Digital Disruption in Banking and its Impact on Competition*. OECD.
- Verificación local: revisa qué datos pueden usarse legalmente para evaluar crédito en tu país, las obligaciones de consentimiento y los atributos prohibidos por la normativa antidiscriminación.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 06 · Inteligencia artificial en banca](06-inteligencia-artificial-en-banca.md) | [Parte 14](../README.md) · [Programa](../../../SYLLABUS.md) | [08 · Fraude digital →](08-fraude-digital.md) |
<!-- gen:footer:end -->
