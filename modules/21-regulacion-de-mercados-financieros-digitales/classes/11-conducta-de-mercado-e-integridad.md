<!-- meta
part: 22
class: 11
title: "Conducta de mercado e integridad"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [integridad-del-mercado, abuso-de-mercado, transparencia]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [IOSCO, FSB, CMF]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 11 · Conducta de mercado e integridad

> [← 10 · Infraestructuras de mercado y su régimen](10-infraestructuras-de-mercado-y-su-regimen.md) · [Índice de la parte](../README.md) · [12 · Prevención de lavado y financiamiento del terrorismo →](12-prevencion-de-lavado-y-financiamiento.md)

**Parte 22 — Regulación de mercados financieros digitales** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Estudiar qué protege la integridad de un mercado digital y **por qué los
controles clásicos se quedan cortos**: en un registro abierto, quien vigila no
sabe quién está detrás de una dirección, y quien opera puede ver las órdenes
antes de que se ejecuten.

Este curso enseña a **detectar y prevenir** el abuso de mercado. No proporciona
técnicas para cometerlo.

La infraestructura de la clase anterior necesita que lo que ocurre dentro sea limpio. Esta clase trata las conductas prohibidas, y muestra que la transparencia del registro facilita su detección y rara vez se aprovecha.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** las tres familias de abuso de mercado.
2. **Explicar** por qué la transparencia del registro facilita unas prácticas y
   dificulta otras.
3. **Diseñar** indicadores de detección con su precisión y su exhaustividad.
4. **Evaluar** el conflicto de interés de una plataforma que además opera.
5. **Determinar** qué obligaciones de conducta aplican aunque no haya régimen de
   mercado.

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

Los cuatro primeros términos son las conductas prohibidas; los cuatro siguientes, los deberes y su vigilancia. La **operación circular** es la práctica más extendida en mercados digitales: operar consigo mismo para inflar el volumen, y su detección es técnicamente sencilla y rara vez se hace.

| Concepto | Comprensión verificable |
|---|---|
| `información privilegiada` | No pública, precisa y que afectaría al precio |
| `manipulación` | Conducta que altera artificialmente el precio o el volumen |
| `operación circular` | Compraventa entre partes vinculadas que infla volumen |
| `anticipación de órdenes` | Operar conociendo una orden ajena pendiente |
| `conflicto de interés` | Interés propio que puede perjudicar al cliente |
| `mejor ejecución` | Obligación de obtener el mejor resultado para el cliente |
| `vigilancia` | Sistema de detección de conducta anómala |
| `reporte de sospecha` | Comunicación obligatoria a la autoridad |

## 🧠 Modelo mental

El modelo mental es que las conductas prohibidas en mercados tradicionales lo son también aquí, y que la transparencia del registro hace su detección más fácil y no menos. Lo que falta suele ser el sistema de vigilancia, no la información.

```text
TRES FAMILIAS

  USO DE INFORMACIÓN
    operar sabiendo lo que otros no saben

  MANIPULACIÓN
    hacer que el precio o el volumen digan
    algo que no es cierto

  CONFLICTO DE INTERÉS
    anteponer el interés propio al del cliente

Y UNA PARTICULARIDAD DEL REGISTRO ABIERTO

  · las órdenes pendientes son VISIBLES
    antes de ejecutarse
  · quien decide el orden puede colocarse
    delante
  → la anticipación de órdenes deja de ser
    una conducta de un intermediario desleal
    y pasa a ser una propiedad del sistema

  ES EL VALOR EXTRAÍBLE DEL ORDEN
  de la Parte 19, clase 12, visto desde
  la integridad del mercado.
```

## 📖 Desarrollo

### 1. Lo que la transparencia facilita y lo que dificulta

```text
DIFICULTA
  · ocultar el volumen real: las operaciones
    son observables
  · negar una operación: queda registrada
  · manipular sin dejar rastro

FACILITA
  · anticipar órdenes ajenas
  · identificar posiciones grandes y
    operar contra ellas
  · coordinar sin comunicarse, observando

CONCLUSIÓN
  la transparencia del registro no sustituye
  a la vigilancia: cambia qué hay que vigilar
```

### 2. Indicadores de detección

| Indicador | Qué busca | Falso positivo típico |
|---|---|---|
| Órdenes canceladas antes de ejecutar | Simulación de interés | Estrategia legítima de cotización |
| Operaciones entre direcciones vinculadas | Volumen circular | Reorganización interna |
| Movimiento antes de un anuncio | Uso de información | Coincidencia |
| Operación justo antes de una orden grande | Anticipación | Casualidad de tiempos |
| Precio anómalo cerca de la hora de cálculo | Manipulación de referencia | Baja liquidez horaria |
| Concentración de contraparte | Acuerdo tácito | Mercado pequeño |

```text
CADA UNO EXIGE UN UMBRAL, Y EL UMBRAL
DECIDE PRECISIÓN Y EXHAUSTIVIDAD
  → es el mismo problema del screening
    de la Parte 18, clase 12
```

### 3. El conflicto de la plataforma que opera

```text
UNA PLATAFORMA QUE ADEMÁS
  · opera por cuenta propia
  · emite su propio instrumento
  · decide qué se lista
  · decide el orden de ejecución

TIENE CUATRO CONFLICTOS SIMULTÁNEOS

  QUÉ EXIGE LA NORMA HABITUAL
  · separación funcional
  · política de conflictos publicada
  · prioridad de la orden del cliente
  · información al cliente

  QUÉ FUNCIONA MEJOR
  · separación societaria
  · no operar por cuenta propia en el
    instrumento propio
  · publicar el volumen propio sobre el total
```

### 4. Mejor ejecución en un mercado fragmentado

```text
LA OBLIGACIÓN EXIGE OBTENER EL MEJOR
RESULTADO CONSIDERANDO PRECIO, COSTE,
RAPIDEZ Y PROBABILIDAD

  EN UN MERCADO FRAGMENTADO
  · hay que comparar entre plataformas
  · y el coste de entrar y salir de cada
    una forma parte del resultado

QUÉ HAY QUE PODER DEMOSTRAR
  · la política de ejecución
  · los datos que la sostienen
  · una revisión periódica con evidencia

Y LO QUE NO SIRVE
  «ejecutamos siempre en nuestra plataforma
   porque es la más rápida», sin datos
```

### 5. Lo que aplica sin régimen de mercado

```text
AUNQUE UNA PLATAFORMA NO ESTÉ SUJETA
A UN RÉGIMEN DE MERCADO, SIGUEN APLICANDO

  · prohibición de engañar
  · responsabilidad por la información
  · protección del consumidor
  · competencia desleal
  · en su caso, tipos penales de estafa
    y de manipulación

«NO ESTAMOS REGULADOS COMO MERCADO»
NO SIGNIFICA QUE MANIPULAR SEA LÍCITO.
```

## 🧮 Ejemplo guiado

El ejemplo detecta operaciones circulares en un conjunto de transacciones. El patrón es reconocible y la información está disponible en el registro.

**Situación.** Una plataforma con vigilancia básica quiere calibrar su detección.

```text
DATOS DE UN MES
  operaciones                          412 000
  alertas generadas                      3 640
  alertas revisadas                      3 640
  casos confirmados                         44
  reportes a la autoridad                   31
  coste de revisar una alerta                18
  casos conocidos a posteriori              62
```

**Paso 1 — calcula precisión y exhaustividad.**

```text
PRECISIÓN = confirmados / alertas
  44 / 3 640 = 1,21 %

EXHAUSTIVIDAD = confirmados / casos reales
  44 / 62 = 70,97 %

  → SE DETECTA EL 71 % Y SE REVISA MUCHO
    RUIDO
```

**Paso 2 — calcula el coste.**

```text
COSTE DE REVISIÓN
  3 640 × 18 = 65 520 al mes
  = 786 240 al año

COSTE POR CASO CONFIRMADO
  65 520 / 44 = 1 489
```

**Paso 3 — evalúa subir el umbral.**

```text
SUBIR EL UMBRAL REDUCE ALERTAS Y CASOS

  supuesto: alertas 3 640 → 1 820
            confirmados 44 → 34

  precisión      34 / 1 820 = 1,87 %
  exhaustividad  34 / 62 = 54,84 %
  coste          1 820 × 18 = 32 760 al mes

  SE AHORRAN 32 760 AL MES
  Y SE DEJAN DE DETECTAR 10 CASOS

  ¿CUÁNTO VALE UN CASO NO DETECTADO?
  esa es la pregunta que decide, y no
  la puede responder el equipo de vigilancia
  solo: es una decisión del comité
```

**Paso 4 — busca el indicador que falta.**

```text
DE LOS 18 CASOS NO DETECTADOS

  supuesto de análisis posterior
  · 11 fueron anticipación de órdenes
  · 5 operaciones circulares entre
    direcciones no vinculadas formalmente
  · 2 uso de información

  EL PRIMER GRUPO ES EL MAYOR
  y no había ningún indicador para él

  INDICADOR PROPUESTO
  operación de la misma dirección en los
  N segundos anteriores a una orden grande
  del mismo instrumento, repetida más de
  K veces en el mes

  supuesto: añade 940 alertas al mes
  y detecta 9 de los 11
```

**Paso 5 — recalcula con el indicador nuevo.**

```text
  alertas        3 640 + 940 = 4 580
  confirmados    44 + 9 = 53
  precisión      53 / 4 580 = 1,16 %
  exhaustividad  53 / 62 = 85,48 %
  coste          4 580 × 18 = 82 440 al mes

  LA PRECISIÓN EMPEORA LIGERAMENTE
  Y LA EXHAUSTIVIDAD SUBE 14,5 PUNTOS

  COSTE ADICIONAL: 16 920 al mes
  POR 9 CASOS MÁS: 1 880 por caso

  → mejor relación que el coste medio actual
    de 1 489... no, es peor

  COMPARACIÓN CORRECTA
  el coste marginal (1 880) frente al valor
  de detectar un caso, no frente al coste
  medio
```

**Paso 6 — decide con el criterio correcto.**

```text
EL COSTE MEDIO NO DECIDE NADA:
DECIDE EL MARGINAL FRENTE AL VALOR

  valor de detectar un caso
  · perjuicio evitado a clientes
  · sanción evitada
  · reputación

  supuesto declarado: 45 000 por caso

  9 casos × 45 000 = 405 000 al año
  coste adicional 16 920 × 12 = 203 040

  → EL INDICADOR SE JUSTIFICA

Y EL SUPUESTO DE 45 000 ES LO QUE HAY
QUE DISCUTIR EN EL COMITÉ, no el umbral.
```

**Interpreta:** la vigilancia detectaba el 71 % y el mayor grupo de casos no
detectados —la anticipación de órdenes— **no tenía ningún indicador**, porque los
indicadores se habían copiado de un mercado donde las órdenes pendientes no son
visibles.

## 🧭 Perspectivas

La conducta de mercado afecta a cada participante de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un precio que se mueve contra él | Si sigue operando |
| Operador | Órdenes visibles antes de ejecutar | Cómo se protege |
| Plataforma | Cuatro conflictos simultáneos | Cómo los separa |
| Creador de mercado | Cancelaciones legítimas señaladas | Qué explica |
| Banco | Obligación de mejor ejecución | Cómo la demuestra |
| Supervisor | 71 % de exhaustividad | Qué exige |
| Auditor | Indicadores copiados de otro mercado | Qué observa |
| Autoridad | 31 reportes de sospecha | Qué investiga |
| Sociedad | Mercados manipulables | Qué protección exige |

## 🏦 Del cliente al banco

El cliente ve un mercado activo y una parte del volumen puede ser circular. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Mi orden movió el precio antes» | Anticipación de órdenes | 22, clase 11 |
| «Hay mucho volumen» | Parte puede ser circular | 22, clase 11 |
| «Ejecutan en su plataforma» | Hay que demostrar la mejor ejecución | 22, clase 11 |

## ⚖️ Riesgos y controles

Los riesgos son de manipulación y de conflicto de interés. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Indicadores copiados | No cubren el abuso propio del registro | Diseñarlos sobre las prácticas observadas |
| Umbral fijado por coste | Se optimiza el gasto, no la detección | Coste marginal frente al valor del caso |
| Conflictos no separados | La plataforma opera contra su cliente | Separación societaria y prioridad del cliente |
| Mejor ejecución sin datos | Se justifica con una afirmación | Política, datos y revisión con evidencia |
| «No somos un mercado» | Se supone que nada aplica | Engaño, consumidor y competencia sí |
| Reporte sin análisis | Se comunica y se olvida | Revisar por qué se produjo |

## 🧪 Práctica

El laboratorio pide detectar conductas prohibidas en datos de mercado. La operación circular es la que se busca.

En [`labs/lab-06.md`](../labs/lab-06.md):

1. Calcula precisión, exhaustividad y coste de una vigilancia.
2. Simula subir el umbral y mide qué se pierde.
3. Diseña el indicador que falta y recalcula.
4. Decide con el coste marginal frente al valor del caso.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen mercados con integridad comprometida. La causa es la ausencia de vigilancia y no la falta de datos.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Copiar indicadores | Es lo rápido | El abuso aquí es distinto |
| Optimizar la precisión | Reduce el ruido | La exhaustividad es lo que protege |
| Decidir con el coste medio | Es el que se calcula | Decide el marginal |
| Conflictos «gestionados» | Hay una política | La separación funciona mejor |
| Mejor ejecución afirmada | Nadie lo pide | Hay que demostrarla con datos |
| Suponer que nada aplica | No hay régimen de mercado | Engañar sigue siendo ilícito |

## ❓ Preguntas de comprobación

1. ¿Cuáles son las tres familias de abuso de mercado?
2. ¿Qué facilita y qué dificulta la transparencia del registro?
3. ¿Por qué la anticipación de órdenes es aquí una propiedad del sistema?
4. ¿Con qué criterio se decide añadir un indicador de detección?
5. ¿Qué sigue aplicando aunque no haya régimen de mercado?

## 📥 Entregable

Guarda en `portfolio/parte-22/clase-11/`:

- el cálculo de precisión, exhaustividad y coste;
- el efecto de mover el umbral;
- el indicador nuevo con su justificación;
- la decisión con coste marginal frente a valor del caso.

## 🔗 Referencias cruzadas

- **Viene de:** clases 3 y 6; Parte 19, clase 12; Parte 20, clase 13.
- **Continúa en:** clases 12 y 15 de esta parte.
- **Se aplica en:** clase 18 de esta parte; Parte 23, clase 11.

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

- IOSCO (2023). *Policy Recommendations for Crypto and Digital Asset Markets*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- IOSCO (2013). *Principles for Financial Benchmarks*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD415.pdf>
- IOSCO (2009). *Objectives and Principles of Securities Regulation*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD323.pdf>
- Financial Stability Board (2023). *The Financial Stability Implications of Multifunction Crypto-asset Intermediaries*. FSB. <https://www.fsb.org/2023/11/the-financial-stability-implications-of-multifunction-crypto-asset-intermediaries/>
- Verificación local: comprueba qué régimen de abuso de mercado aplica en tu jurisdicción a estas plataformas y qué obligaciones de vigilancia y reporte impone. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 10 · Infraestructuras de mercado y su régimen](10-infraestructuras-de-mercado-y-su-regimen.md) | [Parte 22](../README.md) · [Programa](../../../SYLLABUS.md) | [12 · Prevención de lavado y financiamiento del terrorismo →](12-prevencion-de-lavado-y-financiamiento.md) |
<!-- gen:footer:end -->
