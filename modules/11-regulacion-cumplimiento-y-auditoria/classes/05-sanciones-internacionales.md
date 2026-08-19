<!-- meta
part: 12
class: 5
title: "Sanciones internacionales"
level: profesional
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 05 · Sanciones internacionales

> [← 04 · Conozca a su cliente y debida diligencia](04-conozca-a-su-cliente.md) · [Índice de la parte](../README.md) · [06 · Capital regulatorio: Pilar 1 →](06-capital-regulatorio-pilar-1.md)

**Parte 12 — Regulación, cumplimiento y auditoría** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Operar el control de sanciones: la única obligación de cumplimiento donde un error tiene consecuencia
inmediata, automática y sin gradación. A diferencia de la prevención de lavado, que exige juicio, el
régimen de sanciones exige **exactitud**: una operación con una parte sancionada es una infracción
aunque el banco haya actuado de buena fe.

Las dos clases anteriores tratan el riesgo de que el dinero tenga origen ilícito. Esta trata algo distinto: la prohibición de operar con determinadas personas, con independencia de que la operación sea lícita. Y tiene una particularidad que la hace crítica: su alcance puede ser extraterritorial y su incumplimiento no admite gradación.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** los tipos de sanciones y sus emisores.
2. **Explicar** el alcance extraterritorial y por qué afecta a bancos de terceros países.
3. **Operar** el cribado de listas y gestionar sus coincidencias.
4. **Aplicar** el bloqueo, la retención y el reporte según corresponda.
5. **Evaluar** el riesgo de elusión y sus indicadores.

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

Los cuatro primeros términos son el régimen y su aplicación operativa; los cuatro siguientes, sus reglas de alcance. La **regla del 50 %** es la que más se pasa por alto: una entidad no designada pero controlada por designados queda igualmente alcanzada.

| Concepto | Comprensión verificable |
|---|---|
| `sanción` | Restricción impuesta a personas, entidades, sectores o países. |
| `lista de designados` | Registro oficial de sujetos alcanzados por sanciones. |
| `cribado` | Contraste de partes y operaciones contra listas. |
| `coincidencia` | Resultado del cribado que requiere análisis. Puede ser falsa. |
| `bloqueo` | Congelamiento de fondos: no se devuelven ni se transfieren. |
| `regla del 50 %` | Una entidad participada mayoritariamente por designados queda alcanzada. |
| `elusión` | Uso de intermediarios o estructuras para evadir la restricción. |
| `alcance extraterritorial` | Aplicación de un régimen fuera de la jurisdicción que lo emite. |

## 🧠 Modelo mental

El modelo mental es un filtro binario: no hay operación pequeña ni cliente antiguo que justifique una excepción. Frente a una coincidencia confirmada, la operación se bloquea, y esa es la única respuesta admisible.

```text
PREVENCIÓN DE LAVADO         RÉGIMEN DE SANCIONES

basada en riesgo             basada en REGLAS
admite juicio                exige exactitud
reportar y decidir           bloquear e informar
error = deficiencia          error = INFRACCIÓN
gradación de la sanción      responsabilidad objetiva

son sistemas distintos
usar el enfoque de uno para el otro produce fallas
```

**Consecuencia operativa:** no existe una «tolerancia razonable» en sanciones. Un banco no puede decidir
que una coincidencia es de bajo riesgo y seguir adelante; debe resolverla antes de ejecutar la
operación.

## 📖 Desarrollo

### 1. Tipos y emisores

Las sanciones tienen emisores y alcances distintos, y una entidad puede estar sujeta a varios a la vez. La tabla los recoge.

| Tipo | Alcance | Ejemplo de restricción |
|---|---|---|
| Individuales | Personas y entidades designadas | Congelamiento de fondos, prohibición de operar |
| Sectoriales | Actividades o sectores de un país | Prohibición de financiamiento de largo plazo |
| Territoriales | Un territorio completo | Prohibición general de operaciones |
| De proliferación | Programas de armas de destrucción masiva | Restricciones específicas de bienes y finanzas |

Los tipos dicen qué se restringe; los emisores dicen quién obliga y con que
alcance, que es lo que determina si aplican fuera de su territorio.

```text
EMISORES
  CONSEJO DE SEGURIDAD DE NACIONES UNIDAS
    obligatorias para todos los Estados miembros
    se implementan por norma nacional

  BLOQUES REGIONALES Y ESTADOS
    obligatorias en su jurisdicción
    algunas con ALCANCE EXTRATERRITORIAL

  NACIONALES
    propias de cada país
```

### 2. Alcance extraterritorial

Algunos regímenes alcanzan a entidades fuera de su jurisdicción por el uso de su moneda o de su sistema. La tabla lo explica.

```text
POR QUÉ AFECTA A UN BANCO QUE NO ESTÁ EN ESA JURISDICCIÓN

  · si la operación se denomina en su moneda,
    se liquida en su sistema de pagos (Parte 10, clase 13)
  · si el banco tiene relación de corresponsalía allí
  · si usa infraestructura, tecnología o servicios de allí
  · si opera con entidades sujetas a ese régimen

CONSECUENCIA DE INFRINGIR
  · sanción económica de magnitud
  · pérdida de la relación de corresponsalía
  · exclusión práctica de la moneda de referencia
  → el costo de la exclusión suele superar
    con mucho al de la multa
```

**Esta es la razón por la que los regímenes de sanciones se cumplen de facto mucho más allá de su
jurisdicción formal.** No es una obligación jurídica directa: es una condición de acceso a la
infraestructura financiera internacional.

### 3. Cribado

El cribado compara clientes y operaciones contra las listas, y su calibración decide entre falsos positivos y omisiones. La tabla recoge los criterios.

```text
QUÉ SE CRIBA
  · clientes, al inicio y de forma continua
  · beneficiarios finales y representantes
  · contrapartes de operaciones
  · bancos intervinientes en pagos
  · buques, aeronaves, mercancías y puertos (comercio exterior)
  · direcciones y jurisdicciones

CUÁNDO
  · al establecer la relación
  · ante cada actualización de las listas
  · antes de ejecutar cada operación internacional
  · de forma periódica sobre toda la base
```

| Parámetro del cribado | Efecto de un umbral estricto | Efecto de un umbral laxo |
|---|---|---|
| Sensibilidad de coincidencia difusa | Muchas coincidencias falsas | Se escapan designados |
| Transliteración de nombres | Coincidencias por variantes | Se escapan grafías alternativas |
| Campos cribados | Más carga | Menos cobertura |

Detras de esos parámetros hay una dificultad de fondo que ningún umbral
resuelve por si solo.

```text
EL PROBLEMA DE LOS NOMBRES
  transliteración desde otros alfabetos
  orden de nombres y apellidos según cultura
  abreviaturas, apodos, errores de digitación

  un cribado que solo busca coincidencia exacta
  no encuentra prácticamente nada
  un cribado demasiado difuso produce
  cientos de coincidencias falsas por día
```

### 4. Gestión de coincidencias

Una coincidencia se resuelve con un procedimiento y plazos estrictos. Los pasos siguientes lo recogen.

```text
1. COINCIDENCIA GENERADA     el sistema detiene la operación
2. ANÁLISIS                  se contrastan identificadores adicionales:
                             fecha de nacimiento, documento, nacionalidad,
                             domicilio, actividad
3. RESOLUCIÓN
   FALSA        se documenta y se registra en la lista blanca
                (para que no vuelva a generarse)
   VERDADERA    se bloquea, no se ejecuta, se informa a la autoridad
   NO CONCLUYENTE  no se ejecuta hasta resolver
4. PLAZO                     las coincidencias tienen plazo de resolución
5. REGISTRO                  toda decisión, documentada
```

Junto al procedimiento conviene fijar por escrito lo que queda excluido, porque son precisamente las salidas que la presión del momento sugiere.

```text
LO QUE NUNCA DEBE HACERSE
  · devolver los fondos al ordenante en una coincidencia verdadera
    (bloquear NO es rechazar: los fondos se congelan)
  · informar al cliente el motivo del bloqueo antes de
    la autorización de la autoridad competente
  · resolver una coincidencia por presión comercial
  · dejar coincidencias pendientes sin plazo
```

### 5. Elusión

Las técnicas de elusión son conocidas y su detección es parte de la obligación. La tabla las recoge con su señal.

| Indicador de elusión | Qué sugiere |
|---|---|
| Cambio repentino de la ruta de pago | Evitar una jurisdicción |
| Aparición de intermediarios sin rol económico | Interposición |
| Documentación de comercio con descripciones vagas | Ocultar el bien real |
| Contrapartes recién constituidas en países limítrofes | Triangulación |
| Buques con transpondedor apagado | Transbordo no declarado |
| Cambio de bandera o de nombre de un buque | Ocultar identidad |
| Pagos por montos que evitan umbrales | Estructuración |
| Reticencia a identificar al usuario final de un bien | Desvío |

Además de esos indicadores conductuales, existe una regla de propiedad que
alcanza a entidades que no figuran en ninguna lista.

```text
LA REGLA DEL 50 %
  una entidad no designada, pero participada en 50 % o más
  por uno o varios designados, queda alcanzada
  aunque no aparezca en ninguna lista

  → el cribado de nombres NO basta
  → se necesita conocer la propiedad (Parte 12, clase 4)
```

## 🧮 Ejemplo guiado

El ejemplo resuelve una coincidencia con la regla del 50 %. Conviene seguir la estructura de propiedad: la entidad no está en la lista y queda alcanzada igualmente.

**Situación.** Una operación de comercio exterior activa una coincidencia y el análisis se amplía.

```text
OPERACIÓN
  crédito documentario por 340 000
  ordenante: Importadora Delta (cliente del banco, 6 años de relación)
  beneficiario: Meridian Trading Co., jurisdicción C
  mercancía: "equipos y componentes industriales"
  buque: MV Northern Star
  puerto de embarque: puerto en el país D

COINCIDENCIA GENERADA
  el nombre "Meridian Trading" presenta similitud de 0,87
  con "Meridian Trade Ltd", entidad designada
```

**Paso 1 — resuelve la coincidencia de nombre.**

```text
CONTRASTE DE IDENTIFICADORES
  designado: Meridian Trade Ltd, jurisdicción E, registro 44xxxx,
             designado hace 3 años
  beneficiario: Meridian Trading Co., jurisdicción C, registro 91xxxx,
                constituida hace 14 meses

  jurisdicción distinta, registro distinto, denominación distinta
  → COINCIDENCIA FALSA en cuanto al nombre
```

**Paso 2 — no cierres el análisis ahí.**

```text
la coincidencia es falsa, PERO el análisis levantó datos
que deben evaluarse por sí mismos:

  · empresa constituida hace 14 meses
  · jurisdicción C, limítrofe con un país bajo sanciones sectoriales
  · descripción de mercancía genérica: "equipos y componentes"
  · primera operación con este beneficiario

  → el cribado terminó; la evaluación de riesgo empieza
```

**Paso 3 — aplica la regla del 50 %.**

```text
propiedad de Meridian Trading Co.:
  52 % Anadyr Holdings (jurisdicción C)
  48 % dos personas naturales de jurisdicción C

Anadyr Holdings:
  100 % de una entidad de jurisdicción F

esa entidad de jurisdicción F:
  61 % de una persona DESIGNADA

CÁLCULO
  la persona designada controla el 61 % de la entidad F
  → la entidad F queda alcanzada por la regla del 50 %
  la entidad F posee el 100 % de Anadyr
  → Anadyr queda alcanzada
  Anadyr posee el 52 % de Meridian Trading
  → MERIDIAN TRADING QUEDA ALCANZADA

el beneficiario está sancionado
sin aparecer en ninguna lista
```

**Paso 4 — revisa los demás elementos de la operación.**

```text
BUQUE MV Northern Star
  · cambió de nombre hace 9 meses (antes: MV Kestrel)
  · cambió de bandera hace 7 meses
  · datos de posición con interrupciones de 40 a 60 horas
    en tres tramos del último año, en la misma zona marítima

PUERTO DE EMBARQUE
  puerto del país D, limítrofe con el país bajo sanciones sectoriales

MERCANCÍA
  "equipos y componentes industriales" — descripción genérica
  la factura detalla partidas arancelarias que corresponden a bienes
  de doble uso sujetos a control de exportación
```

**Paso 5 — evalúa el conjunto.**

```text
INDICADORES DE ELUSIÓN PRESENTES
  ✓ beneficiario alcanzado por la regla del 50 %
  ✓ empresa recientemente constituida en país limítrofe
  ✓ buque con cambio de nombre y bandera
  ✓ interrupciones de posición compatibles con transbordo
  ✓ descripción genérica de mercancía
  ✓ bienes de doble uso
  ✓ puerto de embarque en país de tránsito

siete indicadores concurrentes
```

**Paso 6 — decide.**

```text
1. NO EJECUTAR la operación
2. BLOQUEAR los fondos si ya fueron provisionados
   (bloquear, no devolver: devolverlos al ordenante
    sería facilitar la elusión y constituye infracción)
3. INFORMAR a la autoridad competente en el plazo normativo
4. NO REVELAR al cliente el motivo hasta contar
   con la instrucción de la autoridad
5. REVISAR el historial del ordenante:
   ¿operaciones anteriores con contrapartes relacionadas?
6. EVALUAR la relación con Importadora Delta:
   ¿sabía? ¿fue instrumentalizada? ¿hay un patrón?
7. REPORTE de operación sospechosa por la vía de prevención de lavado,
   en paralelo y de forma independiente
```

**Paso 7 — extrae las lecciones de proceso.**

```text
1. EL CRIBADO NO ES EL CONTROL: ES SU PUNTO DE PARTIDA
   la coincidencia de nombre era falsa
   y el beneficiario sí estaba alcanzado

2. LA REGLA DEL 50 % EXIGE DATOS DE PROPIEDAD
   sin la cadena societaria, este caso no se detecta
   → el control de sanciones depende de la calidad
     de la debida diligencia (clase 4)

3. EL COMERCIO EXTERIOR EXIGE CRIBAR MÁS QUE NOMBRES
   buques, puertos, rutas, mercancías, usuario final

4. LOS SISTEMAS DEBEN INTEGRARSE
   el dato de propiedad estaba en el expediente del cliente
   y no llegaba al sistema de cribado de operaciones
```

**Interpreta:** el sistema hizo exactamente lo que debía —detener la operación— y **por la razón
equivocada**. La coincidencia de nombre era falsa; el riesgo real estaba tres niveles más abajo en la
estructura de propiedad, donde ningún cribado de nombres lo habría encontrado. El control de sanciones
efectivo no es un motor de comparación de textos: es **la aplicación de la información que la debida
diligencia ya recogió**.

## 🏦 Del cliente al banco

El cliente no entiende el bloqueo y el banco cumple una prohibición sin margen. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Mi transferencia se detuvo y nadie me explica» | Coincidencia en análisis; no se revela | 12, clase 5 |
| «Me bloquearon fondos y no me los devuelven» | Bloqueo no es rechazo | 12, clase 5 |
| «Mi nombre se parece al de un sancionado» | Coincidencia falsa y lista blanca | 12, clase 5 |
| «Mi proveedor es legítimo» | Regla del 50 % sobre la propiedad | 12, clase 4 |
| «El banco no financia ese destino» | Riesgo de elusión y corresponsalía | 10, clase 13 |

## 🧪 Práctica

El laboratorio pide resolver coincidencias, incluida una que activa la regla del 50 %. La decisión y su fundamento son lo que se evalúa.

En `labs/lab-03.md`:

1. Resuelve cinco coincidencias de cribado con identificadores adicionales.
2. Aplica la regla del 50 % a tres estructuras de propiedad.
3. Evalúa una operación de comercio exterior con indicadores de elusión.
4. Diseña el procedimiento de gestión de coincidencias con plazos y responsables.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen incumplimientos de sanciones. Las causas son cribado mal calibrado y la regla del 50 % no aplicada.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se devuelven los fondos al ordenante | Se confunde bloqueo con rechazo | Bloquear es congelar. |
| Se criban solo nombres | Regla del 50 % ignorada | Criba propiedad, buques, puertos y bienes. |
| Coincidencia falsa cierra el análisis | El riesgo real puede estar detrás | Evalúa lo que el análisis levantó. |
| Coincidencias sin plazo de resolución | Operaciones detenidas indefinidamente | Define plazos y escalamiento. |
| Se resuelve por presión comercial | Régimen de reglas, no de riesgo | La resolución es técnica y documentada. |
| Se aplica enfoque de riesgo a sanciones | Sistemas distintos | Sanciones exige exactitud. |

## ❓ Preguntas de comprobación

1. ¿Por qué el régimen de sanciones no admite el enfoque basado en riesgo?
2. ¿Por qué un banco de un tercer país cumple regímenes extraterritoriales?
3. ¿Qué es la regla del 50 % y qué información exige para aplicarse?
4. ¿Por qué devolver los fondos al ordenante puede constituir infracción?
5. ¿Por qué el cribado de nombres es insuficiente en comercio exterior?

## 📥 Entregable

Guarda en `portfolio/parte-12/clase-05/`:

- las cinco coincidencias resueltas con su documentación;
- la aplicación de la regla del 50 % a las tres estructuras;
- la evaluación de la operación de comercio exterior con sus indicadores;
- el procedimiento de gestión de coincidencias diseñado.

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

- United Nations Security Council. *Consolidated List* y resoluciones de los comités de sanciones. UN. <https://www.un.org/securitycouncil/content/un-sc-consolidated-list>
- Financial Action Task Force (2012-2025). *Recommendations 6 y 7*: sanciones financieras dirigidas. FATF.
- Financial Action Task Force (2020). *Guidance on Proliferation Financing Risk Assessment and Mitigation*. FATF. Evaluación del riesgo de financiamiento de la proliferación.
- Wolfsberg Group (2019). *Guidance on Sanctions Screening*. Práctica de filtrado de listas y gestión de coincidencias. <https://www.wolfsberg-principles.com/>
- Financial Action Task Force (2021). *Trade-Based Money Laundering: Risk Indicators*. FATF. Indicadores de lavado basado en comercio que activan alertas.
- Verificación local: identifica las listas de aplicación obligatoria en tu país, la autoridad competente para autorizar operaciones bloqueadas y los plazos de informe.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 04 · Conozca a su cliente y debida diligencia](04-conozca-a-su-cliente.md) | [Parte 12](../README.md) · [Programa](../../../SYLLABUS.md) | [06 · Capital regulatorio: Pilar 1 →](06-capital-regulatorio-pilar-1.md) |
<!-- gen:footer:end -->
