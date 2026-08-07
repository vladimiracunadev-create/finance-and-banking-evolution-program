---
part: 19
class: 9
title: "Oráculos"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global]
regulatory_topics: [dlt, riesgo-de-terceros, integridad]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [IOSCO, CPMI]
requires_legal_review: false
---

<!-- gen:header:start -->
# Clase 09 · Oráculos

> [← 08 · Contratos inteligentes](08-contratos-inteligentes.md) · [Índice de la parte](../README.md) · [10 · Privacidad y pruebas criptográficas →](10-privacidad-y-pruebas-criptograficas.md)

**Parte 19 — Blockchain y DLT para instituciones financieras** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Estudiar el punto por donde el mundo real entra en un registro que no puede
mirarlo. **Un oráculo es un tercero de confianza**, y por eso todo caso de uso
que dependa de uno ha reintroducido justo lo que el registro decía eliminar.

## 📚 Objetivos

Al finalizar podrás:

1. **Explicar** por qué un registro no puede acceder al exterior por sí mismo.
2. **Clasificar** los oráculos por dirección, número de fuentes y modo de
   entrega.
3. **Cuantificar** el coste de manipular un oráculo frente al beneficio de
   hacerlo.
4. **Diseñar** una agregación con protección frente a fuentes discrepantes.
5. **Determinar** cuándo un oráculo hace inviable un caso de uso.

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

| Concepto | Comprensión verificable |
|---|---|
| `oráculo` | Mecanismo que introduce en el registro un dato del exterior |
| `determinismo` | Todos los nodos deben llegar al mismo resultado |
| `oráculo de entrada` | Trae un dato del exterior al registro |
| `oráculo de salida` | Provoca una acción fuera del registro |
| `agregación` | Combinación de varias fuentes en un valor |
| `coste de manipulación` | Lo que cuesta hacer que el oráculo diga otra cosa |
| `retardo` | Tiempo entre el hecho real y su reflejo en el registro |
| `mecanismo de disputa` | Procedimiento para impugnar un dato publicado |

## 🧠 Modelo mental

```text
POR QUÉ UN REGISTRO NO PUEDE MIRAR FUERA

  todos los nodos deben llegar al MISMO resultado
  al ejecutar la misma operación

  si un contrato consultara una dirección de internet,
  dos nodos podrían recibir respuestas distintas
  → el estado divergiría

  → la única forma de introducir un dato externo es
    que ALGUIEN lo escriba dentro como una transacción

Y AHÍ ESTÁ TODO EL PROBLEMA
  ese alguien es un tercero de confianza.
  Un sistema que existía para no necesitar uno
  acaba dependiendo de uno para funcionar.
```

## 📖 Desarrollo

### 1. Clasificación operativa

| Eje | Opciones | Qué cambia |
|---|---|---|
| Dirección | Entrada / salida | La salida no es verificable por el registro |
| Fuentes | Única / múltiple | Coste de manipulación |
| Confianza | Designado / abierto con incentivo | Quién responde |
| Entrega | Bajo demanda / publicación periódica | Retardo y coste |
| Disputa | Sin mecanismo / con impugnación | Qué pasa si el dato es falso |

```text
EL EJE DE DIRECCIÓN ES EL QUE MÁS SE OLVIDA

  ENTRADA   «el tipo de cambio es X»
            el registro puede al menos comprobar
            que varias fuentes coinciden

  SALIDA    «transfiere estos euros por el sistema nacional»
            el registro NO PUEDE VERIFICAR que ocurrió
            → hace falta un oráculo de entrada que confirme
            → y ese confirma lo que le dicen
```

### 2. Coste de manipulación

```text
LA PREGUNTA CORRECTA SOBRE UN ORÁCULO NO ES
«¿ES FIABLE?» SINO
«¿CUÁNTO CUESTA HACER QUE DIGA OTRA COSA,
Y CUÁNTO SE GANA CON ELLO?»

  CON FUENTE ÚNICA
    coste = comprometer una fuente

  CON n FUENTES Y MEDIANA
    coste = comprometer ⌊n/2⌋ + 1 fuentes

  CON n FUENTES Y MEDIA
    coste = comprometer UNA, si no hay filtro de atípicos
    → la media es manipulable con un solo valor extremo

  → la mediana es preferible a la media,
    y esa decisión de una línea cambia el coste
    de atacar en un orden de magnitud
```

### 3. Diseño de la agregación

```text
UNA AGREGACIÓN DEFENDIBLE

  1. n fuentes independientes (distinto operador,
     distinta metodología, distinta infraestructura)
  2. mediana, no media
  3. descartar valores fuera de una banda respecto
     de la mediana anterior
  4. exigir un mínimo de fuentes vivas; si no,
     NO PUBLICAR en vez de publicar con pocas
  5. límite de variación por publicación
     (un salto imposible es un error, no un precio)
  6. registro de qué fuentes aportaron cada valor

EL PUNTO 4 ES EL QUE SALVA
  publicar un precio con 2 de 9 fuentes vivas
  es peor que no publicar: el contrato actuará
  sobre un dato sin respaldo
```

### 4. Retardo y su consecuencia

```text
ENTRE EL HECHO Y SU PUBLICACIÓN HAY TIEMPO

  · el dato se observa
  · se agrega
  · se firma
  · se difunde
  · se incluye en un bloque
  · se considera final

  CON UN MERCADO VOLÁTIL, ESE RETARDO ES DINERO
  quien conoce el dato antes que el contrato
  puede operar contra él

CONTROLES
  · publicaciones más frecuentes (más coste)
  · umbral de desviación que fuerza publicación
  · penalizaciones a operaciones muy próximas
    a una publicación
  · usar precios promediados en el tiempo,
    más caros de manipular y más lentos
```

### 5. Cuándo el oráculo hace inviable el caso

```text
SI EL ORÁCULO ES LA PIEZA CRÍTICA
Y ES UN TERCERO DE CONFIANZA,
HAY QUE VOLVER A LA PREGUNTA DE LA CLASE 1

  «¿existe un tercero de confianza disponible?»
  la respuesta acaba de ser: sí, y lo estamos usando

  → si toda la lógica depende de lo que diga
    ese tercero, una base de datos operada por él
    haría lo mismo, más barato y corregible

CASOS DONDE SIGUE COMPENSANDO
  · el oráculo aporta un dato objetivo y verificable
    a posteriori por varios
  · la lógica que se ejecuta es la parte valiosa,
    y el dato es auxiliar
  · hay muchas partes que no confían entre sí
    pero sí en ese dato concreto
```

## 🧮 Ejemplo guiado

**Situación.** Un contrato de préstamo con garantía en activos digitales liquida
la posición si el valor de la garantía cae por debajo de un umbral. El oráculo
publica el precio.

```text
PARÁMETROS
  préstamos vivos                     240
  importe medio prestado          420 000
  garantía media                  680 000
  umbral de liquidación   garantía < 125 % del préstamo
  penalización de liquidación          8 %

ORÁCULO ACTUAL
  media de 3 fuentes
  publicación cada 60 segundos
  sin mecanismo de disputa
  sin mínimo de fuentes vivas
```

**Paso 1 — calcula el beneficio de manipular.**

```text
SI EL ATACANTE HACE QUE EL PRECIO PAREZCA UN 20 % MENOR

  garantías que caen bajo el umbral:
  supuesto: 62 de los 240 préstamos

  el atacante liquida esas posiciones y cobra
  la penalización del 8 %

  62 × 420 000 × 8 % = 2 083 200

  ADEMÁS puede comprar la garantía liquidada
  a precio deprimido: beneficio adicional
```

**Paso 2 — calcula el coste de manipular con el diseño actual.**

```text
MEDIA DE 3 FUENTES, SIN FILTRO DE ATÍPICOS

  para mover la media un 20 %, basta que UNA fuente
  publique un valor un 60 % menor

  coste = comprometer o influir en UNA fuente

  si una de las tres es un mercado de poca profundidad,
  «comprometerla» puede significar simplemente
  operar en él con volumen suficiente

COSTE ESTIMADO: mucho menor que 2 083 200
→ EL ATAQUE ES RENTABLE
```

**Paso 3 — corrige la agregación.**

```text
CAMBIO 1 · MEDIANA EN VEZ DE MEDIA
  ahora hace falta mover 2 de 3 fuentes
  el coste se multiplica

CAMBIO 2 · CINCO FUENTES INDEPENDIENTES
  hacen falta 3 de 5

CAMBIO 3 · DESCARTE DE ATÍPICOS
  un valor a más de un 10 % de la mediana anterior
  se descarta y se registra

CAMBIO 4 · MÍNIMO DE 4 FUENTES VIVAS
  con menos, NO se publica y el contrato
  entra en estado de pausa

NUEVO COSTE DE ATAQUE
  comprometer 3 de 5 fuentes independientes,
  y que las tres publiquen dentro de la banda
  del 10 % de forma sostenida
```

**Paso 4 — evalúa el efecto de la pausa.**

```text
EL CAMBIO 4 INTRODUCE UN ESTADO NUEVO: PAUSA

  ¿QUÉ PASA CON LAS LIQUIDACIONES DURANTE LA PAUSA?
    no se ejecutan
    → si el precio cae de verdad, el préstamo queda
      infragarantizado y nadie liquida

  ES UN INTERCAMBIO REAL
    protege de la manipulación
    expone al movimiento genuino

  MITIGACIÓN
    · pausa con límite de tiempo
    · procedimiento manual con aprobación humana
      si la pausa supera N minutos
    · notificación inmediata al prestatario para que
      aporte garantía
```

**Paso 5 — cuantifica el retardo.**

```text
PUBLICACIÓN CADA 60 SEGUNDOS

  en un mercado con desviación diaria del 4 %,
  el movimiento típico en 60 s es pequeño...
  salvo en un episodio de tensión, donde
  puede ser de varios puntos

  UN PRESTATARIO QUE VE LA CAÍDA EN EL MERCADO
  Y SABE QUE EL ORÁCULO TARDA 60 s
  puede retirar garantía antes de que el contrato
  reaccione

  CORRECCIÓN
    publicación forzada si la desviación respecto
    del último valor supera el 2 %
```

**Paso 6 — añade el mecanismo de disputa.**

```text
NO HABÍA NINGUNO. HACE FALTA UNO.

  · una liquidación puede impugnarse en un plazo corto
  · la impugnación no revierte automáticamente:
    congela el resultado
  · un comité resuelve con la evidencia de las fuentes
  · si el dato era falso, se compensa al perjudicado
    con cargo a un fondo del propio protocolo

ESTO ES EXACTAMENTE LO QUE LA CLASE 8 DICE:
el código ejecuta, y el contrato jurídico
resuelve lo que el código no puede
```

**Paso 7 — vuelve a la pregunta de la clase 1.**

```text
CON CINCO FUENTES, MEDIANA, BANDA, PAUSA, DISPUTA
Y COMITÉ HUMANO...

  ¿QUÉ QUEDA DE «SIN TERCEROS DE CONFIANZA»?

  quedan las fuentes, el comité y el fondo.
  El contrato automatiza la ejecución de una decisión
  que en último término toman personas.

  ¿ESO INVALIDA EL DISEÑO?
    NO, si se reconoce. Lo que aporta el registro aquí
    es que TODAS las partes ven el mismo precio,
    la misma regla y el mismo momento de liquidación,
    sin que ninguna pueda alegar otra cosa.

  ESO ES VALIOSO. Lo que no es cierto es que
  no haya terceros de confianza.
```

**Interpreta:** el oráculo convirtió un contrato «sin confianza» en un sistema
con cinco fuentes, un comité y un fondo de compensación. **El diseño resultante es
bueno; la descripción que lo acompañaba era falsa**, y esa diferencia es la que
un comité de riesgo tiene que ver.

## 🧭 Perspectivas

| Actor | Qué ve | Qué decide |
|---|---|---|
| Prestatario | Su posición liquidada | Si impugna |
| Prestamista | Garantía que puede evaporarse | Si presta |
| Fuente de precio | Responsabilidad sin contrato | Si acepta el rol |
| Atacante | 2 M de beneficio potencial | Si el coste compensa |
| Comité de disputa | Evidencia de cinco fuentes | Cómo resuelve |
| Riesgo | Un tercero de confianza reintroducido | Qué controles exige |
| Auditor | La descripción y el diseño | Qué observa |

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Me liquidaron a un precio que no existía» | Oráculo manipulado | 19, clase 9 |
| «El sistema se detuvo» | Pausa por falta de fuentes vivas | 19, clase 9 |
| «Es automático, no hay intermediarios» | Hay cinco fuentes y un comité | 19, clase 9 |

## ⚖️ Riesgos y controles

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Manipulación de la agregación | Una fuente mueve la media | Mediana y descarte de atípicos |
| Fuentes correlacionadas | Todas leen el mismo mercado | Independencia de metodología |
| Publicación con pocas fuentes | Dato sin respaldo | Mínimo de fuentes vivas y pausa |
| Retardo explotable | Se opera antes de la publicación | Publicación forzada por desviación |
| Sin mecanismo de disputa | El error es definitivo | Impugnación con plazo y comité |
| Descripción engañosa | «Sin terceros de confianza» | Declarar las dependencias reales |

## 🧪 Práctica

En [`labs/lab-05.md`](../labs/lab-05.md):

1. Implementa la agregación con media y con mediana, y compara el coste de
   manipular.
2. Añade banda de descarte y mínimo de fuentes vivas.
3. Simula un episodio de tensión y comprueba el efecto de la pausa.
4. Escribe la lista de dependencias reales de tu diseño.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Media en vez de mediana | Es lo primero que se escribe | Una línea que cambia el coste de atacar |
| Preguntar «¿es fiable?» | Pregunta sin respuesta útil | Pregunta cuánto cuesta manipularlo |
| Publicar con pocas fuentes | Se priorizó la disponibilidad | Mejor pausar que publicar sin respaldo |
| Fuentes que leen el mismo mercado | Se contaron fuentes | Independencia de metodología |
| Sin disputa | Se confió en el código | Impugnación con comité |
| «Sin terceros de confianza» | Se repitió el eslogan | Declara las dependencias |

## ❓ Preguntas de comprobación

1. ¿Por qué un contrato no puede consultar una fuente externa por sí mismo?
2. ¿Cuál es la pregunta correcta sobre un oráculo y por qué?
3. ¿Por qué la mediana es preferible a la media, y cuánto cambia?
4. ¿Qué intercambio introduce el mínimo de fuentes vivas?
5. En el ejemplo guiado, ¿qué era correcto del diseño y qué era falso de su
   descripción?

## 📥 Entregable

Guarda en `portfolio/parte-19/clase-09/`:

- el cálculo de coste de manipulación con media y con mediana;
- el diseño de agregación con sus seis elementos;
- el análisis del intercambio que introduce la pausa;
- la lista de dependencias reales de tu sistema, escrita sin eslóganes.

## 🔗 Referencias cruzadas

- **Viene de:** clases 1 y 8.
- **Continúa en:** clase 11 (puentes), clase 12 (orden).
- **Se aplica en:** Parte 20, clase 13 (creación de mercado); Parte 21,
  clase 12; Parte 23, clase 13.

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

- IOSCO (2022). *Decentralized Finance Report*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD699.pdf>
- IOSCO (2013). *Principles for Financial Benchmarks*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD415.pdf>
- Financial Stability Board (2023). *The Financial Stability Risks of Decentralised Finance*. FSB. <https://www.fsb.org/2023/02/the-financial-stability-risks-of-decentralised-finance/>
- Bank for International Settlements (2023). *Annual Economic Report*, capítulo sobre el sistema monetario del futuro. BIS. <https://www.bis.org/publ/arpdf/ar2023e3.htm>
- NIST (2018). *NISTIR 8202: Blockchain Technology Overview*. NIST. <https://csrc.nist.gov/pubs/ir/8202/final>
- Verificación local: comprueba si los principios sobre índices de referencia aplican al oráculo que uses y qué régimen tiene su administrador en tu jurisdicción. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 08 · Contratos inteligentes](08-contratos-inteligentes.md) | [Parte 19](../README.md) · [Programa](../../../SYLLABUS.md) | [10 · Privacidad y pruebas criptográficas →](10-privacidad-y-pruebas-criptograficas.md) |
<!-- gen:footer:end -->
