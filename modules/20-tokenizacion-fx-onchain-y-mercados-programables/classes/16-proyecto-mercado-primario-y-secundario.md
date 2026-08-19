<!-- meta
part: 21
class: 16
title: "Proyecto: mercado primario y secundario"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [chile, internacional]
regulatory_topics: [infraestructura, gestion-de-riesgos, gobierno-corporativo]
regulation_last_verified: 2026-08-19
regulatory_status: vigente
primary_authorities: [CPMI, IOSCO, CMF]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 16 · Proyecto: mercado primario y secundario

> [← 15 · Interoperabilidad entre infraestructuras](15-interoperabilidad-entre-infraestructuras.md) · [Índice de la parte](../README.md) · [Proyecto de la parte →](../project/README.md)

**Parte 21 — Tokenización, FX on-chain y mercados programables** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Integrar las quince clases en el **expediente de una infraestructura**: emitir un
instrumento, liquidarlo de forma atómica, darle mercado secundario y demostrar
que cada promesa del folleto se sostiene con un número.

Esta clase cierra la parte construyendo un mercado completo. Y con una exigencia que ordena el entregable: cada beneficio prometido va con la medición que lo demuestra, o se retira.

## 📚 Objetivos

Al finalizar podrás:

1. **Ensamblar** el expediente de diseño de un mercado primario y secundario.
2. **Justificar** cada decisión de arquitectura con su alternativa medida.
3. **Especificar** qué promete el folleto y con qué evidencia se sostiene.
4. **Defender** el diseño ante las preguntas que un supervisor hará.
5. **Concluir** que no procede tokenizar, si los números lo dicen.

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

Los cuatro primeros términos son el expediente y sus exigencias; los cuatro siguientes, la prueba y el cierre. La **promesa verificable** es el criterio que ordena el proyecto: cada beneficio que el diseño promete tiene que ir con la medición que lo demuestra o retirarse.

| Concepto | Comprensión verificable |
|---|---|
| `expediente de diseño` | Conjunto de decisiones con su justificación medida |
| `promesa verificable` | Afirmación del folleto con evidencia detrás |
| `alternativa medida` | La opción descartada, con sus números |
| `criterio de aceptación` | Condición comprobable antes de operar |
| `prueba de extremo a extremo` | Ejecución completa del ciclo en entorno de pruebas |
| `plan de contingencia` | Qué se hace si un componente falla |
| `revisión posterior` | Comprobación de que lo prometido se cumplió |
| `condición de cierre` | Hecho que obliga a detener la operación |

## 🧠 Modelo mental

El modelo mental es un diseño que se compara con la alternativa que ya existe. La tokenización de un mercado se justifica si mejora algo medible frente a la infraestructura actual, y esa comparación es el entregable central.

```text
LAS DOCE DECISIONES DEL EXPEDIENTE

  IDENTIFICACIÓN
   1 qué derecho se representa y su régimen
   2 registro de referencia y procedimiento
     de divergencia

  EMISIÓN
   3 mecanismo de adjudicación
   4 tramo de dinero y su emisor
   5 procedimiento de emisión desierta

  CICLO DE VIDA
   6 eventos programables y no programables
   7 función de inmovilización y su gobierno

  MERCADO
   8 estructura: continuo, subasta o fórmula
   9 compromisos de liquidez y sus cláusulas

  OPERACIÓN
  10 custodia, segregación y sustitución
  11 conexión con otras infraestructuras

  CIERRE
  12 promesas del folleto con su evidencia

CADA UNA CON SU ALTERNATIVA MEDIDA.
Una decisión sin alternativa medida
es una preferencia, no una decisión.
```

## 📖 Desarrollo

### 1. La regla del expediente

El expediente se evalúa decisión a decisión, y cada una necesita tres
elementos. El bloque los fija y los ilustra con un ejemplo correcto y otro
que no lo es.

```text
CADA DECISIÓN NECESITA TRES COSAS

  LO ELEGIDO         qué se hace
  LA ALTERNATIVA     qué se descartó
  EL NÚMERO          por cuánto

EJEMPLO CORRECTO
  «subasta semanal en vez de mercado continuo,
   porque con 412 operaciones en 182 días
   el libro continuo estaría vacío el 59 %
   de los días»

EJEMPLO INCORRECTO
  «subasta semanal, porque es más adecuado
   para este tipo de activo»

LA DIFERENCIA ES QUE LA PRIMERA
SE PUEDE DISCUTIR Y LA SEGUNDA NO.
```

### 2. Las promesas del folleto

Toda afirmación del material comercial debe poder respaldarse con una
evidencia concreta. El bloque empareja las promesas habituales con la
evidencia que las sostiene.

```text
CADA AFIRMACIÓN DEL MATERIAL COMERCIAL
DEBE TENER SU EVIDENCIA

  «liquidación atómica»
    → evidencia: ambos tramos en el mismo
      registro; prueba de ausencia de estado
      intermedio

  «liquidez secundaria»
    → evidencia: días con operación medidos,
      compromiso de cotización con parámetros

  «acceso desde 1 000»
    → evidencia: cálculo del importe de
      equilibrio; si es 2 250, la promesa
      es incorrecta

  «menos intermediarios»
    → evidencia: lista de los que se eliminan
      y de por qué no eran exigidos por norma

SI UNA PROMESA NO TIENE EVIDENCIA,
SE QUITA DEL FOLLETO.
Ese es el criterio, y es el que evita
la mayor parte de los problemas posteriores.
```

### 3. Criterios de aceptación

Antes de operar con dinero real hay que poder demostrar seis escenarios, y
todos incluyen un fallo. El bloque los enumera.

```text
QUÉ HAY QUE PODER DEMOSTRAR
ANTES DE OPERAR CON DINERO REAL

  1 emisión completa en entorno de pruebas,
    incluido el escenario desierto
  2 pago de un cupón con incidencias
    y su reintento
  3 aplicación de una inmovilización
    con doble aprobación
  4 liquidación atómica con fallo de cada
    tramo por separado
  5 divergencia entre registros detectada,
    congelada y resuelta
  6 sustitución del custodio, ejecutada
  7 vencimiento con destrucción solo de
    lo pagado
  8 medición de profundidad publicada

LOS OCHO SE EJECUTAN, NO SE DOCUMENTAN.
```

### 4. Contingencias

Cada componente puede fallar, y para cada uno debe existir una respuesta
escrita. El bloque las recoge en una tabla que sirve de índice del plan de
contingencia.

```text
QUÉ SE HACE SI FALLA CADA COMPONENTE

  el registro          modo degradado y
                       reconstrucción desde copia
  el emisor del dinero límite de saldo y ruta
                       alternativa de liquidación
  el custodio          plan de sustitución
                       (clase 9)
  el oráculo de precio pausa y precio manual
                       con doble aprobación
  el enlace externo    participante común
                       de respaldo
  la plataforma        rescate al registro
                       oficial (clase 3)

Y CADA UNO CON UN PLAZO MÁXIMO DECLARADO
y una prueba anual documentada.
```

### 5. La conclusión que el proyecto permite

El proyecto admite concluir que no procede tokenizar, y esa conclusión se
evalúa igual que la contraria. El bloque enumera las señales que suelen llevar
a ella.

```text
UN EXPEDIENTE PUEDE CONCLUIR
QUE NO PROCEDE TOKENIZAR

  y esa conclusión vale lo mismo que la
  contraria, si está sostenida por las doce
  decisiones con sus alternativas medidas

SEÑALES QUE LLEVAN A ESA CONCLUSIÓN
  · el registro oficial seguirá mandando
  · el tramo de dinero está fuera
  · el beneficio se consigue acortando
    el ciclo actual
  · no hay compromiso de liquidez
  · el importe de equilibrio está por encima
    del mínimo prometido

CON TRES DE LAS CINCO, LA RECOMENDACIÓN
HONESTA ES NO HACERLO.
```

## 🧮 Ejemplo guiado

El ejemplo compara el mercado diseñado con su alternativa no tokenizada en coste, plazo y riesgo. En algunas dimensiones gana la alternativa, y decirlo es parte del proyecto.

**Situación.** Se diseña el mercado de un bono corporativo tokenizado de
40 000 000 a 3 años. Recorremos el expediente hasta la recomendación.

```text
DATOS
  nominal                          40 000 000
  plazo                                3 años
  cupón                            6,4 % semestral
  inversionistas objetivo               1 200
  mínimo propuesto                      1 000
  registro oficial disponible              sí
  depósito tokenizado disponible           sí
  volumen secundario estimado    900 000 al mes
```

**Paso 1 — decisiones 1 y 2.**

```text
DERECHO
  bono corporativo; régimen de valores;
  oferta pública

REGISTRO DE REFERENCIA
  elegido: bloqueo de origen
  alternativa: espejo, con conciliación
  número: espejo costaría 400 464 al año
          (clase 2); bloqueo, 40 500

  → DECISIÓN JUSTIFICADA
```

**Paso 2 — decisiones 3, 4 y 5.**

```text
ADJUDICACIÓN
  elegida: prorrateo con tramo mínimo de 2 000
  alternativa: orden de llegada
  número: el orden de llegada da ventaja 1,0
          al primero y produce sobredemanda
          artificial (clase 4)

TRAMO DE DINERO
  elegido: depósito tokenizado
  alternativa: stablecoin
  número: capital consumido 100 699 frente
          a 503 496 al año (clase 10)

EMISIÓN DESIERTA
  mínimo declarado: 24 000 000
  liberación automática de bloqueos
  probado en entorno de pruebas
```

**Paso 3 — decisiones 6 y 7.**

```text
EVENTOS
  programables: cupón fijo, amortización
  con dato externo: ninguno
  no programables: embargo, concurso

FUNCIÓN DE INMOVILIZACIÓN
  activable por el responsable de operaciones
  con doble aprobación
  solo inmoviliza; no transfiere
  registro inmutable de cada uso
  revisión trimestral por el comité
```

**Paso 4 — decisiones 8 y 9.**

```text
ESTRUCTURA DE MERCADO
  volumen estimado 900 000 al mes
  operación media supuesta 22 000
  → 41 operaciones al mes ≈ 2 al día

  elegida: subasta diaria
  alternativa: mercado continuo
  número: con 2 operaciones al día, el libro
          continuo está vacío casi siempre
          (clase 6)

COMPROMISO DE LIQUIDEZ
  diferencial máximo 1,5 %
  importe mínimo cotizado 50 000 por lado
  horario: la subasta
  plazo: 24 meses
  retirada: solo por causas tasadas,
            preaviso de 30 días
```

**Paso 5 — comprueba el mínimo prometido.**

```text
MÍNIMO PROPUESTO: 1 000

  coste unitario de servicio supuesto: 14 al año
  comisiones: 0,9 % anual
  rentabilidad bruta: 6,4 %
  neta de comisiones: 5,5 %

  CON 1 000
    14 / 1 000 = 1,4 %
    neta = 4,1 %

  ALTERNATIVA SIN RIESGO: 4,3 %

  → CON 1 000, EL INVERSIONISTA RINDE
    MENOS QUE SIN RIESGO

  IMPORTE DE EQUILIBRIO PARA UNA PRIMA
  DE 1 PUNTO:
  5,5 % − 14/x > 5,3 %
  x > 7 000

  → EL MÍNIMO DE 1 000 NO SE SOSTIENE
    Y HAY QUE SUBIRLO A 7 000
```

**Paso 6 — decisiones 10 y 11.**

```text
CUSTODIA
  cuenta segregada, no ómnibus
  número: 1 200 posiciones × 0,4 × 12
          = 5 760 al año sobre 40 000 000
          = 0,014 % (clase 9)
  esquema 3-de-5 con independencia efectiva 4
  copia diaria en un tercero
  custodio sustituto identificado

CONEXIÓN
  solo con la infraestructura de dinero
  elegida: enlace directo
  alternativa: puente
  número: el puente acumularía saldo y su
          umbral efectivo sería 2 (clase 15)
```

**Paso 7 — cierra con las promesas del folleto.**

```text
                          PROMESA        EVIDENCIA

  liquidación atómica     sí             ambos tramos
                                         en el registro;
                                         prueba ejecutada

  liquidez secundaria     REFORMULADA    «subasta diaria
                                         con compromiso
                                         de cotización de
                                         50 000 por lado»

  acceso desde 1 000      RETIRADA       el equilibrio
                                         está en 7 000

  menos intermediarios    RETIRADA       ninguno de los
                                         eliminados era
                                         prescindible

  cupón automático        sí             probado con
                                         incidencias

DE CINCO PROMESAS, DOS SE MANTIENEN,
UNA SE REFORMULA Y DOS SE RETIRAN.

Y EL PROYECTO SIGUE ADELANTE:
lo que se corrigió fue el folleto,
no la arquitectura.
```

**Interpreta:** las doce decisiones se sostenían y **dos de las cinco promesas
comerciales no**. Corregir el folleto costó una tarde; descubrirlo después de la
emisión habría costado una reclamación por cada uno de los 1 200 inversionistas
que hubieran entrado con 1 000.

## 🧭 Perspectivas

El proyecto afecta a todos los participantes de las quince clases anteriores. La tabla los reúne.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un folleto con cinco promesas | Si invierte |
| Inversionista | Evidencia detrás de cada una | Si confía |
| Emisor | Un diseño con alternativas medidas | Si aprueba |
| Colocador | Un mínimo que sube a 7 000 | Cómo coloca |
| Plataforma | Doce decisiones justificadas | Qué construye |
| Custodio | Segregada por 0,014 % | Si la ofrece |
| Infraestructura | Un enlace directo | Si lo acepta |
| Supervisor | Promesas con evidencia | Qué autoriza |
| Auditor | Ocho criterios ejecutados | Qué verifica |
| Sociedad | Un mercado que dice lo que hace | Qué exige |

## 🏦 Del cliente al banco

El inversionista opera en un mercado y el diseño decide sus derechos y su liquidez. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Puedo entrar con 1 000» | Con 1 000 rinde menos que sin riesgo | 21, clase 16 |
| «Tiene liquidez» | Subasta diaria con compromiso de 50 000 | 21, clase 16 |
| «Sin intermediarios» | Ninguno era prescindible | 21, clase 16 |

## ⚖️ Riesgos y controles

Los riesgos del proyecto reúnen los de toda la parte. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Decisión sin alternativa medida | Es una preferencia disfrazada | Las tres cosas por decisión |
| Promesa sin evidencia | Reclamaciones posteriores | Se retira del folleto |
| Criterios documentados sin ejecutar | Fallan el primer día | Los ocho se ejecutan |
| Contingencia sin plazo | Nadie sabe cuándo actuar | Plazo máximo declarado |
| Mínimo elegido por marketing | El inversionista pierde | Importe de equilibrio calculado |
| Expediente sin conclusión posible de «no» | Se decidió antes de analizar | El «no» vale igual |

## 🧪 Práctica

El laboratorio es el proyecto completo. Las promesas retiradas por no poder medirse son lo que más credibilidad da.

En [`project/README.md`](../project/README.md) se desarrolla el expediente
completo. Aquí se cierra el ensamblaje y se ensaya la defensa.

## ⚠️ Errores frecuentes

Los síntomas de la tabla aparecen en la defensa. Casi todos se evitan midiendo cada promesa antes de escribirla.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Justificar por «es más adecuado» | No se midió | Da el número |
| Folleto escrito antes del análisis | Lo escribe otro equipo | Cada promesa con su evidencia |
| Criterios de aceptación en papel | Ejecutarlos cuesta | Se ejecutan |
| Mínimo por marketing | «Desde 1 000» vende | Calcula el equilibrio |
| Contingencias genéricas | Se copian de otro proyecto | Una por componente, con plazo |
| Decidir antes de analizar | Ya hay una preferencia | Las doce decisiones primero |

## ❓ Preguntas de comprobación

1. ¿Qué tres cosas necesita cada decisión del expediente?
2. ¿Qué se hace con una promesa del folleto que no tiene evidencia?
3. Enumera los ocho criterios de aceptación que se ejecutan.
4. En el ejemplo, ¿por qué se retiró la promesa de acceso desde 1 000?
5. ¿Qué cinco señales llevan a concluir que no procede tokenizar?

## 📥 Entregable

Guarda en `portfolio/parte-21/clase-16/`:

- las doce decisiones con su alternativa medida;
- la tabla de promesas del folleto con su evidencia o su retirada;
- los ocho criterios de aceptación con su resultado;
- las contingencias por componente, con plazo máximo.

## 🔗 Referencias cruzadas

- **Viene de:** todas las clases de la parte.
- **Continúa en:** Parte 22, clase 1.
- **Se aplica en:** Parte 22, clase 16; Parte 23, clases 7, 8 y 16.

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

- CPMI e IOSCO (2012). *Principles for Financial Market Infrastructures*. BIS. Requisitos que la infraestructura del proyecto debe acreditar. <https://www.bis.org/cpmi/publ/d101.htm>
- IOSCO (2023). *Policy Recommendations for Crypto and Digital Asset Markets*. IOSCO. Obligaciones de conducta y revelación del instrumento emitido. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- Committee on Payments and Market Infrastructures (2024). *Tokenisation in the context of money and other assets: concepts and implications for central banks*. BIS. Diseño del registro y de la liquidación atómica del proyecto. <https://www.bis.org/cpmi/publ/d225.htm>
- Diario Oficial de la Unión Europea (2022). *Reglamento (UE) 2022/858 sobre el régimen piloto de infraestructuras del mercado basadas en DLT*. EUR-Lex. Régimen bajo el que se acoge la infraestructura propuesta. <https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32022R0858>
- Comisión para el Mercado Financiero. *Normativa sobre infraestructuras de mercado y oferta pública*. CMF. Autorizaciones chilenas exigibles al proyecto. <https://www.cmfchile.cl/portal/principal/613/w3-channel.html>
- Verificación local: comprueba qué autorizaciones exige tu jurisdicción para operar una infraestructura de este tipo y si existe un régimen piloto o de exención aplicable. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-19.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 15 · Interoperabilidad entre infraestructuras](15-interoperabilidad-entre-infraestructuras.md) | [Parte 21](../README.md) · [Programa](../../../SYLLABUS.md) | [Proyecto de la parte →](../project/README.md) |
<!-- gen:footer:end -->
