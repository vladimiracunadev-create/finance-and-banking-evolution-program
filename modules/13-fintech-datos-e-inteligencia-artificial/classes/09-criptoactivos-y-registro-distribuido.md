---
part: 14
class: 9
title: "Criptoactivos y registro distribuido"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 09 · Criptoactivos y registro distribuido

> [← 08 · Fraude digital](08-fraude-digital.md) · [Índice de la parte](../README.md) · [10 · Monedas digitales de banco central →](10-monedas-digitales-de-banco-central.md)

**Parte 14 — Fintech, datos e inteligencia artificial** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Entender qué resuelve técnicamente un registro distribuido, qué son los criptoactivos y cómo un banco
debe tratarlos. La clase separa deliberadamente **la tecnología, que tiene usos verificables**, del
mercado de criptoactivos, que tiene características de riesgo propias y bien documentadas.

Esta clase introduce la tecnología que la Etapa 5 desarrolla en tres partes enteras. Aquí se da el marco mínimo: qué es un registro distribuido, en qué se diferencia de una base de datos y qué exposición tiene un banco a estos activos, que casi siempre es indirecta y mayor de lo que sus cifras muestran.

## 📚 Objetivos

Al finalizar podrás:

1. **Explicar** qué problema resuelve un registro distribuido y a qué costo.
2. **Clasificar** los criptoactivos por su naturaleza económica.
3. **Identificar** los riesgos para un banco que se relaciona con ellos.
4. **Aplicar** el tratamiento prudencial de exposiciones a criptoactivos.
5. **Evaluar** casos de uso de la tecnología con criterio.

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

Los tres primeros términos son la tecnología; los cinco siguientes, los activos que la usan y su custodia. La **custodia de claves** es el problema práctico que decide todo: quien tiene las claves tiene los activos, y no hay forma de recuperarlos si se pierden.

| Concepto | Comprensión verificable |
|---|---|
| `registro distribuido` | Base de datos replicada y sincronizada sin autoridad central. |
| `cadena de bloques` | Registro encadenado por resúmenes criptográficos. |
| `mecanismo de consenso` | Procedimiento por el que la red acuerda el estado válido. |
| `criptoactivo` | Activo digital cuyo registro y transferencia usan criptografía. |
| `moneda estable` | Criptoactivo que busca mantener un valor de referencia. |
| `contrato inteligente` | Código que se ejecuta automáticamente sobre el registro. |
| `finanzas descentralizadas` | Servicios financieros sobre protocolos sin intermediario. |
| `custodia de claves` | Control de las claves privadas que dan acceso a los activos. |

## 🧠 Modelo mental

El modelo mental es un registro compartido sin dueño único: varios participantes mantienen la misma anotación y acuerdan cómo actualizarla sin que ninguno decida solo. Todo lo demás —las cadenas de bloques, los consensos, los contratos— es la mecánica de ese acuerdo.

```text
QUÉ PROBLEMA RESUELVE UN REGISTRO DISTRIBUIDO

  permite que partes que NO confían entre sí
  ni en un tercero común
  mantengan un registro compartido que ninguna controla

  EL COSTO DE ESA PROPIEDAD
    · redundancia masiva: todos guardan todo
    · lentitud comparada con una base de datos centralizada
    · consumo de recursos del consenso
    · irreversibilidad de los errores

LA PREGUNTA DE DISEÑO
  ¿existe en este caso un tercero de confianza disponible?
  si existe, una base de datos centralizada
  es más rápida, más barata y corregible
```

**Casi todos los casos de uso fallidos comparten el mismo error:** aplicar la tecnología donde sí había
un tercero de confianza disponible, pagando su costo sin obtener su beneficio.

## 📖 Desarrollo

### 1. Cómo funciona

Un registro distribuido resuelve un problema concreto con componentes concretos. El esquema los recorre.

```text
COMPONENTES
  · transacciones firmadas con clave privada
  · agrupadas en bloques
  · encadenadas por resumen criptográfico del bloque anterior
  · validadas por un mecanismo de consenso
  · replicadas en todos los nodos
```

| Mecanismo de consenso | Cómo decide | Costo | Uso |
|---|---|---|---|
| Prueba de trabajo | Quien resuelve un problema costoso | Muy alto en energía | Redes abiertas iniciales |
| Prueba de participación | Quien compromete activos | Bajo | Redes abiertas actuales |
| Consenso entre autorizados | Acuerdo entre nodos conocidos | Bajo | Redes privadas |

```text
REDES ABIERTAS vs. AUTORIZADAS
  ABIERTA      cualquiera participa, sin permiso
               máxima descentralización, mínimo control
  AUTORIZADA   participantes conocidos y aprobados
               menos descentralización, gobernanza posible

  para uso bancario, las redes autorizadas
  son las únicas compatibles con las obligaciones
  de identificación y cumplimiento
```

### 2. Clasificación económica

Los criptoactivos se clasifican por lo que representan económicamente, y esa clasificación decide su tratamiento. La tabla la recoge.

| Tipo | Qué es económicamente | Riesgo dominante |
|---|---|---|
| Sin respaldo | Activo especulativo sin flujo ni emisor | Precio, liquidez, sin valor intrínseco |
| Moneda estable con respaldo | Instrumento de deuda del emisor | Crédito del emisor, calidad del respaldo |
| Moneda estable algorítmica | Mecanismo de estabilización sin respaldo | Colapso del mecanismo, documentado |
| Token de valores | Valor tradicional en formato digital | El del valor subyacente |
| Token de utilidad | Derecho de acceso a un servicio | Del emisor y del servicio |
| Token de activo real | Representación de un bien | Custodia y exigibilidad del bien |
| Moneda digital de banco central | Pasivo del banco central | Ver clase 10 |

```text
LA CLASIFICACIÓN NO ES ACADÉMICA: DETERMINA EL RÉGIMEN
  un token que representa un valor ES un valor
  y le aplica toda la regulación de valores,
  con independencia de su formato técnico

  el principio es el mismo de la Parte 12, clase 1:
  misma actividad, mismo riesgo, misma regla
```

### 3. Riesgos para un banco

Un banco tiene exposición a estos activos por vías directas e indirectas. La tabla las recoge.

```text
EXPOSICIÓN DIRECTA
  · precio: volatilidad muy superior a la de otros activos
  · liquidez: mercados que se estrechan bruscamente
  · custodia: la pérdida de una clave es irreversible
  · operacional: irreversibilidad de las transferencias

EXPOSICIÓN INDIRECTA
  · clientes con exposición que afecta su solvencia
  · flujos de origen no verificable
  · contrapartes con exposición no declarada
  · riesgo reputacional por asociación

CUMPLIMIENTO
  · trazabilidad limitada en redes abiertas
  · la regla del viaje de la información (Parte 10, clase 13)
    es de aplicación difícil pero exigible
  · servicios de mezcla diseñados para romper la trazabilidad
```

| Riesgo de custodia | Por qué es distinto |
|---|---|
| Pérdida de clave | No hay recuperación posible |
| Robo de clave | Transferencia irreversible |
| Error de dirección | Fondos perdidos definitivamente |
| Custodia de terceros | Riesgo de contraparte sin garantía |

**La custodia es el punto donde un banco puede aportar valor real:** una institución regulada, con
controles de segregación, seguros y procedimientos, resuelve un problema que el usuario individual
gestiona mal.

### 4. Tratamiento prudencial

El tratamiento de capital de estas exposiciones es muy conservador y depende de la clasificación. La tabla lo recoge.

```text
EL MARCO PRUDENCIAL DISTINGUE DOS GRUPOS

  GRUPO 1 — criptoactivos que cumplen condiciones estrictas
    · tokens de activos tradicionales con derechos equivalentes
    · monedas estables con mecanismo de estabilización efectivo
      y respaldo verificado
    → tratamiento equivalente al del activo subyacente,
      con recargo por riesgo de infraestructura

  GRUPO 2 — todos los demás
    · sin respaldo, o con mecanismo no verificado
    → tratamiento muy conservador:
      ponderación de riesgo del 1 250 %
      (equivale a deducir la exposición del capital)
    → límite de exposición sobre el capital nivel 1
```

```text
QUÉ SIGNIFICA UNA PONDERACIÓN DE 1 250 %
  exposición 100 × 1 250 % = 1 250 de activos ponderados
  capital al 8 %: 100
  → el banco debe tener capital igual al 100 % de la exposición

  es una forma de decir: si quieres tenerlo,
  fináncialo íntegramente con capital
```

### 5. Casos de uso con criterio

Hay usos donde la tecnología aporta y usos donde no. La tabla los separa con el criterio que decide.

| Caso de uso | ¿Hay tercero de confianza? | Valoración |
|---|---|---|
| Pagos transfronterizos entre bancos | Sí (corresponsales) | La mejora está en el proceso, no en la descentralización |
| Registro de garantías | Sí (registro público) | Útil si el registro es deficiente |
| Trazabilidad de cadena de suministro | Depende | Útil con muchas partes sin confianza mutua |
| Liquidación de valores | Sí (depositario central) | La mejora es de sincronización, no de confianza |
| Emisión de valores tokenizados | Sí | Ahorro de proceso; el marco legal es la restricción |
| Identidad autogestionada | No plenamente | Prometedor, con marcos aún en desarrollo |
| Contratos con ejecución automática | Depende | Útil donde la ejecución es objetiva y verificable |

```text
CRITERIO DE EVALUACIÓN
  1. ¿el problema es de confianza o de proceso?
     si es de proceso, una base de datos compartida basta
  2. ¿cuántas partes participan y confían entre sí?
  3. ¿la irreversibilidad es una ventaja o un riesgo?
  4. ¿el marco legal reconoce el registro como prueba?
  5. ¿qué pasa si hay un error?
```

## 🧮 Ejemplo guiado

El ejemplo compara un registro distribuido con una base de datos centralizada para el mismo problema. Conviene fijarse en la pregunta de si hace falta que no haya un dueño único: si no hace falta, la base centralizada gana.

**Situación.** Un banco recibe tres propuestas relacionadas con criptoactivos y debe decidir.

```text
PROPUESTA A — servicio de custodia de criptoactivos para clientes
  demanda estimada: 4 200 clientes, 68 000 de activos bajo custodia
  comisión: 0,85 % anual

PROPUESTA B — aceptar criptoactivos como garantía de crédito
  demanda estimada: 180 operaciones, 42 000 de crédito
  garantía: criptoactivos sin respaldo, con aforo del 50 %

PROPUESTA C — liquidación de pagos transfronterizos con moneda estable
  volumen: 340 000 anuales
  ahorro estimado: 1,2 días de plazo y 0,35 % de costo
```

**Paso 1 — evalúa la Propuesta A.**

```text
INGRESO
  68 000 × 0,85 % = 578 anuales

EXPOSICIÓN DEL BANCO
  la custodia NO es exposición propia:
  los activos son de los clientes
  → sin consumo de capital por riesgo de mercado

  PERO SÍ HAY RIESGO OPERACIONAL Y LEGAL
    · pérdida de claves por falla propia
    · robo desde la infraestructura del banco
    · error en una transferencia
    → responsabilidad frente al cliente
```

```text
COSTOS Y CONTROLES NECESARIOS
  infraestructura de custodia (almacenamiento en frío,
    firmas múltiples, segregación): 1 400 inicial
  seguro de custodia: 180 anuales
  personal especializado: 320 anuales
  cumplimiento (origen de fondos, trazabilidad): 240 anuales
  auditoría específica: 90 anuales
  TOTAL: 1 400 inicial + 830 anuales

RESULTADO: 578 − 830 = −252 anuales
```

**Paso 2 — evalúa si la Propuesta A puede corregirse.**

```text
EL PROBLEMA ES DE ESCALA
  con 68 000 bajo custodia, los costos fijos dominan

PUNTO DE EQUILIBRIO
  830 / 0,85 % = 97 647 de activos bajo custodia

  ¿es alcanzable? depende del mercado local
  y de la disposición de los clientes a custodiar
  en un banco en lugar de en una plataforma especializada

VENTAJA COMPETITIVA DEL BANCO
  · entidad regulada, con seguro y auditoría
  · segregación verificable
  · el usuario individual gestiona mal sus claves
  → hay valor real que ofrecer

DECISIÓN: aplazar hasta que la demanda estimada
supere el punto de equilibrio con margen
```

**Paso 3 — evalúa la Propuesta B.**

```text
CRÉDITO CON GARANTÍA DE CRIPTOACTIVOS SIN RESPALDO

  crédito: 42 000
  garantía: 84 000 de criptoactivos (aforo 50 %)

TRATAMIENTO PRUDENCIAL
  ¿la garantía es elegible como mitigante de riesgo de crédito?
  los criptoactivos del Grupo 2 NO son garantía elegible
  → el crédito se pondera como si no tuviera garantía
  → y si el banco tomara los activos, ponderación de 1 250 %
```

**Paso 4 — evalúa el riesgo económico, no solo el regulatorio.**

```text
VOLATILIDAD DEL COLATERAL
  desviación diaria observada: 4,2 %
  caída máxima en 30 días en episodios documentados: −62 %

  con aforo del 50 %, una caída del 50 % agota la garantía
  probabilidad de caída del 50 % en 12 meses: sustancial
  según la historia del activo
```

```text
CORRELACIÓN ADVERSA (Parte 11, clase 8)
  ¿quién pide un crédito con garantía de criptoactivos?
  típicamente, alguien cuyo patrimonio está en criptoactivos

  si el activo cae 50 %:
    · la garantía se agota
    · el patrimonio del deudor cae con ella
    · su capacidad de reponer garantía desaparece
    · su capacidad de pago se deteriora

  la garantía y la solvencia del deudor
  caen POR LA MISMA CAUSA
  → CORRELACIÓN ADVERSA ESPECÍFICA
```

**Paso 5 — decide sobre la Propuesta B.**

```text
RECHAZAR

MOTIVOS
  1. la garantía no es elegible prudencialmente
  2. correlación adversa específica entre garantía y deudor
  3. la liquidación de la garantía en un mercado en caída
     es exactamente cuando la liquidez desaparece
  4. requeriría llamadas de margen intradía,
     capacidad que el banco no tiene para este activo

CONDICIÓN PARA RECONSIDERAR
  garantía en criptoactivos del Grupo 1 (tokens de activos
  tradicionales o monedas estables verificadas),
  con aforo alto, llamadas de margen automáticas
  y liquidación garantizada
```

**Paso 6 — evalúa la Propuesta C.**

```text
LIQUIDACIÓN CON MONEDA ESTABLE

  ¿QUÉ PROBLEMA RESUELVE?
    los pagos transfronterizos son lentos y caros
    por la cadena de corresponsales (Parte 10, clase 13)

  ¿ES UN PROBLEMA DE CONFIANZA O DE PROCESO?
    de PROCESO: los bancos corresponsales confían entre sí
    → la descentralización no es la solución al problema real
```

```text
PERO EL AHORRO PROPUESTO ES REAL
  1,2 días de plazo y 0,35 % de costo
  sobre 340 000: ahorro de 1 190 anuales

  ¿de dónde viene ese ahorro?
    · elimina intermediarios de la cadena
    · liquidación continua, sin cortes horarios
    · menos conciliación manual

  ninguno de esos ahorros REQUIERE un registro distribuido:
  requieren una infraestructura compartida
  con liquidación continua
```

**Paso 7 — evalúa los riesgos de la Propuesta C.**

```text
RIESGO DE LA MONEDA ESTABLE
  · ¿quién es el emisor y qué respalda los tokens?
  · ¿el respaldo está segregado y auditado?
  · ¿existe derecho de rescate a la par, exigible?
  · ¿qué ocurre si el emisor suspende los rescates?

  el banco tendría exposición al EMISOR
  durante el tiempo en que mantiene el saldo

RIESGO DE LIQUIDACIÓN
  · la irreversibilidad significa que un error de dirección
    es una pérdida definitiva
  · el volumen de 340 000 operaciones anuales
    implica errores estadísticamente ciertos
```

**Paso 8 — formula la decisión sobre C.**

```text
APROBAR EN PILOTO, CON CONDICIONES

  1. moneda estable del Grupo 1: respaldo verificado,
     segregado, auditado, con rescate exigible a la par
  2. exposición máxima al emisor: límite específico,
     tratado como exposición de contraparte
  3. saldo mantenido en la moneda estable: mínimo operativo,
     con conversión inmediata
  4. verificación de dirección de destino con lista blanca
     de contrapartes conocidas
  5. límite de monto por operación durante el piloto
  6. evaluación a 12 meses del ahorro real

  ahorro estimado neto del costo de controles: 840 anuales

  Y REGISTRAR LA CONCLUSIÓN METODOLÓGICA
    el ahorro proviene de eliminar intermediarios
    y liquidar de forma continua, no de la descentralización
    → si aparece una infraestructura compartida convencional
      con las mismas propiedades, será preferible
```

**Interpreta:** las tres propuestas se resolvieron con **la misma pregunta aplicada tres veces**: qué
problema resuelve y a qué costo. La custodia tiene valor real y no escala todavía; la garantía tiene
correlación adversa que ninguna aforo corrige; la liquidación aporta ahorro real por razones que no son
las que su propuesta invocaba. Separar la tecnología de su relato es el trabajo analítico central de
esta clase.

## 🏦 Del cliente al banco

El cliente compra criptoactivos y el banco tiene exposición indirecta por sus clientes y sus contrapartes. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Perdí mi clave y perdí todo» | Irreversibilidad de la custodia propia | 14, clase 9 |
| «Quiero que el banco custodie mis criptoactivos» | Valor real, con costos fijos altos | 14, clase 9 |
| «Tengo patrimonio en criptoactivos» | No es garantía elegible | 14, clase 9 |
| «Mi transferencia llegó en minutos» | Liquidación continua | 10, clase 13 |
| «El banco no acepta fondos de esa plataforma» | Trazabilidad del origen | 12, clase 3 |

## 🧪 Práctica

El laboratorio pide clasificar criptoactivos y estimar la exposición indirecta de un banco. La exposición indirecta supera con mucho a la directa.

En `labs/lab-05.md`:

1. Clasifica diez criptoactivos por su naturaleza económica y su régimen aplicable.
2. Evalúa cinco casos de uso con el criterio de las cinco preguntas.
3. Calcula el requerimiento de capital de una exposición del Grupo 2.
4. Identifica la correlación adversa en un esquema de garantía.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen decisiones mal fundadas sobre esta tecnología. Las causas son usarla sin necesidad y medir solo la exposición directa.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se aplica la tecnología donde hay tercero de confianza | Costo sin beneficio | Pregunta si el problema es de confianza. |
| Se clasifica por formato técnico | El régimen depende de la sustancia | Un token de valor es un valor. |
| Aforo alto como único mitigante | Correlación adversa | Evalúa el vínculo garantía-deudor. |
| Custodia sin infraestructura específica | Pérdida irreversible | Almacenamiento en frío y firmas múltiples. |
| Moneda estable sin verificar el respaldo | Riesgo del emisor | Exige segregación y auditoría. |
| Se atribuye el ahorro a la descentralización | Diagnóstico erróneo | Identifica la fuente real del ahorro. |

## ❓ Preguntas de comprobación

1. ¿Qué problema resuelve un registro distribuido y a qué costo?
2. ¿Por qué la clasificación económica determina el régimen aplicable?
3. ¿Qué significa una ponderación de riesgo del 1 250 %?
4. ¿Por qué un criptoactivo sin respaldo es mala garantía aun con aforo alto?
5. ¿Cuál es el error común de los casos de uso fallidos?

## 📥 Entregable

Guarda en `portfolio/parte-14/clase-09/`:

- los diez criptoactivos clasificados con su régimen;
- los cinco casos de uso evaluados con las cinco preguntas;
- el cálculo de capital de una exposición del Grupo 2;
- el análisis de correlación adversa del esquema de garantía.

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

- Basel Committee on Banking Supervision (2022). *Prudential treatment of cryptoasset exposures*. BIS. <https://www.bis.org/bcbs/publ/d545.htm>
- Financial Stability Board (2023). *Global Regulatory Framework for Crypto-asset Activities*. FSB. <https://www.fsb.org/2023/07/fsb-global-regulatory-framework-for-crypto-asset-activities/>
- Financial Action Task Force (2021). *Updated Guidance for a Risk-Based Approach to Virtual Assets and VASPs*. FATF.
- Bank for International Settlements (2022). *Annual Economic Report*, capítulo sobre el sistema monetario del futuro. BIS.
- Committee on Payments and Market Infrastructures e IOSCO (2022). *Application of the Principles for Financial Market Infrastructures to stablecoin arrangements*. BIS.
- Verificación local: revisa el régimen aplicable a los proveedores de servicios de activos virtuales en tu país y si tu supervisor permite a los bancos operar con criptoactivos.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 08 · Fraude digital](08-fraude-digital.md) | [Parte 14](../README.md) · [Programa](../../../SYLLABUS.md) | [10 · Monedas digitales de banco central →](10-monedas-digitales-de-banco-central.md) |
<!-- gen:footer:end -->
