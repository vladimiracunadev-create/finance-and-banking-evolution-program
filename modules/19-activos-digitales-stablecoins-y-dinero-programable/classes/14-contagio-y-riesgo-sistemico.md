---
part: 20
class: 14
title: "Contagio y riesgo sistémico"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [estabilidad-financiera, contagio, interconexion]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [FSB, BIS, CMF]
requires_legal_review: false
---

<!-- gen:header:start -->
# Clase 14 · Contagio y riesgo sistémico

> [← 13 · Mercado, liquidez y formación de precio](13-mercado-liquidez-y-formacion-de-precio.md) · [Índice de la parte](../README.md) · [15 · Contabilidad, tributación y balance →](15-contabilidad-tributacion-y-balance.md)

**Parte 20 — Activos digitales, stablecoins y dinero programable** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Construir el mapa de exposición que una institución necesita cuando el riesgo no
llega por su balance sino por el de otros. **La exposición directa es la que se
mide; la indirecta es la que hace daño.**

Las clases anteriores analizan instrumentos y mercados por separado. Esta los conecta, y encuentra lo que ningún balance muestra: la exposición indirecta de un banco que no tiene un solo activo digital.

## 📚 Objetivos

Al finalizar podrás:

1. **Construir** un grafo de exposición con nodos, aristas y sus pesos.
2. **Calcular** la exposición de segundo y tercer grado de una institución.
3. **Identificar** los canales de contagio que no pasan por el balance.
4. **Simular** el orden de caída ante un fallo inicial dado.
5. **Diseñar** los indicadores que un comité de riesgo debe recibir.

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

Los cuatro primeros términos son las vías de exposición; los cuatro siguientes, los mecanismos de propagación. La **exposición indirecta** es la que no aparece en ningún balance: un banco sin criptoactivos puede tener clientes cuya solvencia depende de ellos, y eso es exposición.

| Concepto | Comprensión verificable |
|---|---|
| `exposición directa` | Posición propia en el instrumento |
| `exposición indirecta` | A través de una contraparte expuesta |
| `canal de contagio` | Vía por la que un fallo se propaga |
| `nodo crítico` | Aquel cuya caída desconecta o arrastra a muchos |
| `dependencia común` | Proveedor o infraestructura compartida |
| `venta correlacionada` | Todos venden lo mismo a la vez |
| `interconexión` | Densidad de vínculos entre participantes |
| `cascada` | Secuencia de caídas encadenadas |

## 🧠 Modelo mental

El modelo mental es un mapa de dependencias comunes: lo que propaga una crisis no son las exposiciones directas, que son pequeñas, sino los nodos que varios participantes comparten sin saberlo.

```text
CINCO CANALES, Y SOLO EL PRIMERO
APARECE EN LOS ESTADOS FINANCIEROS

  1 EXPOSICIÓN DIRECTA
      tengo el instrumento

  2 EXPOSICIÓN POR CONTRAPARTE
      le presté a quien lo tiene

  3 DEPENDENCIA COMÚN
      compartimos custodio, plataforma,
      proveedor de precios o banco

  4 VENTA CORRELACIONADA
      cuando cae uno, todos venden lo mismo
      para conseguir liquidez

  5 CONFIANZA
      «si aquello podía pasar, esto también»
      y se retira financiación a quien
      no tenía nada que ver

EL CANAL 3 ES EL MENOS VISIBLE
Y EL QUE MÁS SORPRENDE.
```

## 📖 Desarrollo

### 1. Construir el grafo

```text
NODOS
  emisores, custodios, plataformas,
  prestamistas, fondos, bancos,
  proveedores de precios, infraestructuras

ARISTAS
  · posición de A en el instrumento de B
  · crédito de A a B
  · custodia de A en B
  · dependencia operativa de A en B

PESOS
  importe, o porcentaje del capital de A

FUENTES DE DATOS
  · estados financieros
  · informes de reservas
  · condiciones de servicio publicadas
  · registros públicos de la red
  · cuestionarios a contrapartes

LA MAYOR PARTE DEL TRABAJO ES
CONSTRUIR EL GRAFO, NO ANALIZARLO
```

### 2. Exposición de segundo grado

```text
FÓRMULA OPERATIVA

  exposición indirecta de A vía B
  = crédito de A a B
    × (exposición de B al instrumento
       / capital de B)

INTERPRETACIÓN
  la fracción mide qué parte del capital
  de B está en riesgo; si el instrumento
  cae, B pierde esa fracción y A pierde
  proporcionalmente su crédito

LÍMITE DEL MÉTODO
  supone que la pérdida se traslada de forma
  lineal, y en una quiebra no lo hace
  → sirve para ORDENAR, no para predecir
    el importe exacto
```

### 3. Dependencias comunes

```text
CÓMO SE DESCUBREN

  · leer las condiciones de servicio:
    quién custodia, quién liquida,
    quién publica el precio
  · observar la red: direcciones de custodia
    compartidas
  · preguntar en el cuestionario de contraparte
  · revisar los informes de incidentes: dos
    entidades caídas a la vez comparten algo

LO QUE SUELE APARECER
  el mismo banco depositario
  la misma plataforma de negociación
  el mismo proveedor de precios
  el mismo custodio técnico
  el mismo proveedor de nube
```

### 4. Venta correlacionada

```text
POR QUÉ CAE LO QUE NO TENÍA PROBLEMA

  un participante necesita liquidez
  → vende lo que PUEDE vender,
    no lo que quiere vender

  y lo que puede vender es lo líquido:
  la deuda pública, el instrumento
  con mercado profundo

  → EL ACTIVO SANO CAE PRIMERO
    porque es el único que se puede vender

CONSECUENCIA PARA EL ANÁLISIS
  no basta con preguntar «¿quién tiene
  el activo problemático?»
  hay que preguntar «¿quién necesitará
  liquidez y qué venderá?»
```

### 5. Qué debe recibir un comité

```text
CUATRO INDICADORES, ACTUALIZADOS MENSUALMENTE

  1 EXPOSICIÓN DIRECTA por instrumento,
    frente al límite

  2 EXPOSICIÓN INDIRECTA de segundo grado
    por contraparte, con el método declarado

  3 MAPA DE DEPENDENCIAS COMUNES
    con el número de contrapartes que
    dependen de cada proveedor

  4 ESCENARIO DE CASCADA
    orden de caída y pérdida acumulada
    ante el fallo del nodo más conectado

Y UNA PÁGINA DE SUPUESTOS.
Sin ella, los cuatro indicadores
son cifras sin significado.
```

## 🧮 Ejemplo guiado

El ejemplo mide la exposición directa e indirecta de un sistema bancario. La segunda es varios órdenes de magnitud mayor.

**Situación.** Un banco quiere conocer su exposición total al instrumento S, del
que **no tiene ni una unidad**.

```text
POSICIÓN DIRECTA DEL BANCO EN S:  0

RELACIONES DEL BANCO
  crédito a la fintech F            42 000 000
  crédito al fondo D                68 000 000
  línea a la plataforma P           25 000 000
  depósitos del custodio C         180 000 000

DATOS DE LAS CONTRAPARTES
  F  capital 120 000 000 · posición en S  38 000 000
  D  capital 340 000 000 · posición en S 105 000 000
  P  capital  80 000 000 · posición en S  12 000 000
  C  capital 210 000 000 · posición en S       0
     (custodia S por cuenta de clientes: 900 000 000)
```

**Paso 1 — calcula la exposición de segundo grado.**

```text
VÍA F
  38 000 000 / 120 000 000 = 31,7 %
  42 000 000 × 31,7 % = 13 300 000

VÍA D
  105 000 000 / 340 000 000 = 30,9 %
  68 000 000 × 30,9 % = 21 000 000

VÍA P
  12 000 000 / 80 000 000 = 15,0 %
  25 000 000 × 15,0 % = 3 750 000

VÍA C
  posición propia 0 → 0

EXPOSICIÓN INDIRECTA DE SEGUNDO GRADO
  38 050 000
```

**Paso 2 — analiza el custodio con más cuidado.**

```text
C NO TIENE POSICIÓN PROPIA
PERO CUSTODIA 900 000 000 POR CUENTA DE CLIENTES

  SI S SE DESPLOMA
    · los clientes de C retiran
    · C tiene un problema de INGRESOS
      (comisiones sobre saldo custodiado)
    · si hay litigio por la custodia,
      tiene un problema de CAPITAL

  EFECTO SOBRE EL BANCO
    el banco tiene 180 000 000 EN DEPÓSITOS
    de C, es decir, C es su ACREEDOR

  → SI C RETIRA ESOS DEPÓSITOS DE GOLPE
    EL BANCO TIENE UN PROBLEMA DE LIQUIDEZ,
    no de crédito

ESTE ES EL CANAL QUE NINGUNA FÓRMULA
DE SEGUNDO GRADO CAPTURA
```

**Paso 3 — construye el escenario de cascada.**

```text
SUPUESTO · S CAE UN 60 %

  RONDA 1
    F pierde 38 000 000 × 60 % = 22 800 000
      sobre capital 120 000 000 → 19,0 %
    D pierde 105 000 000 × 60 % = 63 000 000
      sobre capital 340 000 000 → 18,5 %
    P pierde 12 000 000 × 60 % = 7 200 000
      sobre capital 80 000 000 → 9,0 %

  NINGUNO CAE, PERO TODOS SE DETERIORAN

  RONDA 2 · REACCIÓN
    los tres reducen posiciones para
    recomponer capital
    → venden otros activos
    → y piden liquidez a sus bancos

    demanda de liquidez sobre el banco:
    supuesto 40 % de las líneas comprometidas
    (42 + 68 + 25) × 40 % = 54 000 000

  RONDA 3 · CUSTODIO
    C retira depósitos por presión de clientes
    supuesto 35 % de 180 000 000 = 63 000 000

  NECESIDAD DE LIQUIDEZ TOTAL DEL BANCO
    54 000 000 + 63 000 000 = 117 000 000
    en pocos días
```

**Paso 4 — compara con la exposición declarada.**

```text
EL BANCO DECLARA EXPOSICIÓN A S:  0

EXPOSICIÓN ECONÓMICA REAL
  crédito en riesgo (2.º grado)      38 050 000
  liquidez comprometida             117 000 000

  → LA CIFRA DE «CERO» ERA CIERTA
    Y COMPLETAMENTE INÚTIL
```

**Paso 5 — busca la dependencia común.**

```text
REVISIÓN DE PROVEEDORES

  F, D y P usan el mismo proveedor
  de precios de S

  ¿QUÉ PASA SI ESE PROVEEDOR FALLA
  O PUBLICA UN PRECIO ERRÓNEO?

    los tres valoran mal a la vez
    los tres liquidan garantías a la vez
    el banco recibe las tres llamadas
    de liquidez el mismo día

  → UN FALLO DEL PROVEEDOR DE PRECIOS
    PRODUCE EL MISMO EFECTO QUE UNA
    CAÍDA DEL 60 %, SIN QUE S SE MUEVA

Y ESTE NODO NO ESTABA EN NINGÚN
BALANCE NI EN NINGÚN LÍMITE
```

**Paso 6 — define los límites que faltan.**

```text
LÍMITES ACTUALES
  posición directa en S: 0 ✓ cumplido

LÍMITES PROPUESTOS
  1 exposición indirecta de 2.º grado
    máximo 5 % del capital del banco
  2 concentración por proveedor común
    máximo 3 contrapartes relevantes
    con el mismo proveedor de precios
  3 depósitos de un solo custodio de
    activos digitales: máximo 8 % de los
    depósitos mayoristas
  4 líneas comprometidas a entidades con
    exposición > 15 % de su capital:
    revisión trimestral obligatoria
```

**Paso 7 — declara los supuestos.**

```text
SUPUESTOS QUE SOSTIENEN TODO EL EJERCICIO

  · caída del 60 % de S
  · traslado lineal de la pérdida al capital
  · disposición del 40 % de las líneas
  · retirada del 35 % de los depósitos de C
  · que los tres usan el mismo proveedor

SI ALGUNO CAMBIA, LA CONCLUSIÓN CAMBIA.
Por eso el informe los pone en primera página
y no en un anexo.
```

**Interpreta:** el banco tenía exposición cero y una necesidad de liquidez de
117 millones. **El indicador que se vigilaba era el único irrelevante.** El nodo
que más importaba —el proveedor de precios— no aparecía en ningún estado
financiero y se descubrió leyendo condiciones de servicio.

## 🧭 Perspectivas

El contagio afecta a cada participante de forma distinta y algunos no saben que están expuestos. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Su banco «no está expuesto» | Si confía |
| Fintech | Su capital deteriorado | Si reduce posición |
| Banco | Cero directo, mucho indirecto | Qué límites fija |
| Banco central | Interconexión creciente | Qué información recopila |
| Custodio | Clientes que retiran | Qué liquidez mantiene |
| Infraestructura | Presión simultánea | Si aplica límites |
| Mercado | Ventas correlacionadas | Cómo cotiza el riesgo |
| Supervisor | Un mapa que nadie tiene | Qué reporte exige |
| Auditor | Riesgos fuera de balance | Qué revela |
| Sociedad | Un contagio inesperado | Qué supervisión exige |

## 🏦 Del cliente al banco

El cliente no tiene criptoactivos y su banco puede estar expuesto por otra vía. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «No estamos expuestos» | Cero directo, 117 millones de liquidez | 20, clase 14 |
| «Cada uno es independiente» | Comparten proveedor de precios | 20, clase 14 |
| «Cayó lo que no tenía problema» | Se vende lo que se puede vender | 20, clase 14 |

## ⚖️ Riesgos y controles

Los riesgos son de dependencia común y de venta correlacionada. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Medir solo exposición directa | Es la que hay en el sistema | Añadir segundo grado con método declarado |
| Dependencia común invisible | No está en ningún balance | Mapa por lectura de condiciones y cuestionarios |
| Liquidez comprometida | Todos disponen a la vez | Límite y prueba de tensión conjunta |
| Depósitos de un custodio | Concentración mayorista | Límite por depositante |
| Traslado lineal supuesto | Se toma como predicción | Usarlo para ordenar, no para cuantificar |
| Supuestos ocultos | Van en un anexo | Primera página del informe |

## 🧪 Práctica

El laboratorio pide mapear canales de contagio y medir la exposición indirecta. Los nodos críticos son lo que hay que identificar.

En [`labs/lab-08.md`](../labs/lab-08.md):

1. Construye el grafo con nodos, aristas y pesos.
2. Calcula exposición de segundo y tercer grado.
3. Descubre las dependencias comunes y añádelas como nodos.
4. Simula la cascada y produce los cuatro indicadores del comité.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen contagios inesperados. La causa es haber medido solo la exposición directa.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Reportar «exposición cero» | Solo se mide lo directo | Calcula el segundo grado |
| Ignorar al custodio sin posición | No tiene el activo | Es tu depositante mayorista |
| Olvidar el proveedor de precios | No es una contraparte financiera | Un fallo suyo actúa como una caída |
| Tratar el lineal como predicción | Es lo que da el modelo | Sirve para ordenar |
| Escenarios de un solo nodo | Es más fácil | El daño viene de la simultaneidad |
| Supuestos en anexo | Estorban al resumen | Van delante |

## ❓ Preguntas de comprobación

1. Enumera los cinco canales de contagio y di cuál es el menos visible.
2. ¿Cómo se calcula la exposición de segundo grado y qué límite tiene el método?
3. ¿Por qué cae primero el activo sano en una venta correlacionada?
4. En el ejemplo, ¿por qué el proveedor de precios era el nodo crítico?
5. ¿Qué cuatro indicadores debe recibir un comité de riesgo?

## 📥 Entregable

Guarda en `portfolio/parte-20/clase-14/`:

- el grafo de exposición con sus fuentes de datos;
- el cálculo de segundo y tercer grado con el método declarado;
- el mapa de dependencias comunes descubiertas;
- los cuatro indicadores y la página de supuestos.

## 🔗 Referencias cruzadas

- **Viene de:** clases 6, 7, 12 y 13.
- **Continúa en:** clases 15 y 16 de esta parte.
- **Se aplica en:** Parte 22, clase 15; Parte 23, clases 14 y 16.

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

- Financial Stability Board (2022). *Assessment of Risks to Financial Stability from Crypto-assets*. FSB. <https://www.fsb.org/2022/02/assessment-of-risks-to-financial-stability-from-crypto-assets/>
- Financial Stability Board (2023). *The Financial Stability Implications of Multifunction Crypto-asset Intermediaries*. FSB. <https://www.fsb.org/2023/11/the-financial-stability-implications-of-multifunction-crypto-asset-intermediaries/>
- Bank for International Settlements (2023). *Annual Economic Report*, capítulo III. BIS. <https://www.bis.org/publ/arpdf/ar2023e3.htm>
- Basel Committee on Banking Supervision (2018). *Framework for dealing with domestic systemically important banks*. BIS. <https://www.bis.org/publ/bcbs233.htm>
- Verificación local: comprueba qué reporte de interconexión y de exposición indirecta exige tu supervisor y con qué periodicidad. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 13 · Mercado, liquidez y formación de precio](13-mercado-liquidez-y-formacion-de-precio.md) | [Parte 20](../README.md) · [Programa](../../../SYLLABUS.md) | [15 · Contabilidad, tributación y balance →](15-contabilidad-tributacion-y-balance.md) |
<!-- gen:footer:end -->
