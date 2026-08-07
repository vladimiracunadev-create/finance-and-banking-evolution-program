---
part: 6
class: 12
title: "Creación de dinero"
level: intermedio
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 12 · Creación de dinero

> [← 11 · Bancos centrales](11-bancos-centrales.md) · [Índice de la parte](../README.md) · [13 · Tipo de cambio →](13-tipo-de-cambio.md)

**Parte 06 — Economía y sistema financiero** · **Nivel:** Intermedio — requiere las partes anteriores · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Entender de dónde viene el dinero que circula, que es la pregunta cuya respuesta más sorprende a quien
llega desde fuera: **la mayor parte del dinero la crean los bancos comerciales al otorgar crédito**.
Esta clase explica el mecanismo, sus límites reales y por qué el modelo del multiplicador que se enseña
tradicionalmente describe mal el proceso.

Esta clase corrige una idea muy extendida y equivocada: que los bancos prestan el dinero que captan. En realidad el crédito crea depósitos, y esa dirección invertida explica por qué el crédito bancario es una variable macroeconómica y por qué se regula tanto.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** base monetaria de agregados monetarios más amplios.
2. **Explicar** cómo un banco crea dinero al otorgar un crédito.
3. **Identificar** los límites reales a la creación de dinero.
4. **Criticar** el modelo del multiplicador monetario y explicar por qué es incompleto.
5. **Relacionar** el crecimiento del crédito con la inflación y con la estabilidad financiera.

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

Los cuatro primeros términos son los agregados monetarios y los tres últimos, el mecanismo y sus límites. El **dinero bancario** es el concepto central: la mayor parte del dinero que circula no lo emitió ningún banco central, lo crearon los bancos comerciales al prestar.

| Concepto | Comprensión verificable |
|---|---|
| `base monetaria (M0)` | Circulante más reservas de los bancos en el banco central. La crea el banco central. |
| `M1` | Circulante en poder del público más depósitos a la vista. |
| `M2` | M1 más depósitos a plazo y de ahorro de menor monto. |
| `M3` | M2 más otros instrumentos de menor liquidez. |
| `dinero bancario` | Depósitos creados por los bancos al otorgar crédito. Es la mayor parte del dinero. |
| `encaje` | Fracción de los depósitos que el banco debe mantener en reservas. |
| `multiplicador monetario` | Razón entre un agregado amplio y la base. Es una **razón observada**, no un mecanismo causal. |

## 🧠 Modelo mental

El mecanismo real, en dos asientos:

```text
un banco otorga un crédito de 10 000 000 a un cliente

  CARGO   Colocaciones (activo)      10 000 000
    ABONO   Depósito del cliente (pasivo)   10 000 000
```

**El banco no prestó dinero que tenía: creó un depósito.** El dinero apareció en el momento del
asiento. Y cuando el cliente paga el crédito, el asiento se revierte y ese dinero desaparece.

Esta descripción no es una teoría alternativa: es cómo funciona operativamente el registro bancario, y
así lo describen las publicaciones de varios bancos centrales.

## 📖 Desarrollo

### 1. Los agregados monetarios

Los agregados van de lo más líquido a lo menos, y cada uno incluye al anterior. La tabla los define.

```text
M0 (base)    circulante + reservas de los bancos en el banco central
M1           circulante en poder del público + depósitos a la vista
M2           M1 + depósitos a plazo y de ahorro
M3           M2 + instrumentos de mayor plazo y menor liquidez
```

Proporción típica en una economía desarrollada:

| Agregado | Proporción del total |
|---|---:|
| Circulante (billetes y monedas) | 3–8 % |
| Depósitos (dinero bancario) | 92–97 % |

**Más del 90 % del dinero que existe son anotaciones contables en bancos comerciales.** El efectivo es
una fracción menor y decreciente.

### 2. El mecanismo de creación

El mecanismo se ve mejor siguiendo los asientos contables de la Parte 5, que es lo que hace el esquema siguiente.

```text
PASO 1  el banco otorga el crédito
  activo: colocación +10 000 000
  pasivo: depósito   +10 000 000
  → M1 aumentó en 10 000 000

PASO 2  el cliente usa el dinero para pagar a un proveedor de otro banco
  banco A: pasivo depósito −10 000 000, activo reservas −10 000 000
  banco B: pasivo depósito +10 000 000, activo reservas +10 000 000
  → el dinero sigue existiendo, cambió de banco
  → el banco A necesita reservas para liquidar la transferencia

PASO 3  el crédito se paga
  activo: colocación −10 000 000
  pasivo: depósito   −10 000 000
  → M1 disminuyó: el dinero DESAPARECIÓ
```

El paso 2 muestra dónde está la restricción real: **el banco necesita reservas para liquidar los pagos
que salen**. Si presta mucho más que sus pares, sus salidas superan sus entradas y debe conseguir
reservas en el mercado interbancario, a la tasa que fija el banco central.

### 3. Los límites reales

La creación de dinero no es ilimitada, y los límites reales no son los que suele decirse. La tabla los recoge.

| Límite | Cómo opera |
|---|---|
| **Rentabilidad** | El banco presta si el margen supera el costo de fondos, el riesgo y el capital consumido |
| **Demanda solvente** | Debe existir alguien que quiera y pueda endeudarse |
| **Capital regulatorio** | Cada colocación consume capital; el capital es el límite duro |
| **Liquidez** | Debe poder liquidar las salidas de pagos |
| **Tasa de política** | Encarece el costo de las reservas y del fondeo |
| **Regulación macroprudencial** | Límites a la relación préstamo/valor, cuota/ingreso, colchones |
| **Encaje** | Inmoviliza una fracción de los depósitos |

El límite que la práctica muestra como más vinculante en sistemas modernos es el **capital**, no el
encaje. Un banco con capital insuficiente no puede crecer aunque tenga reservas de sobra.

### 4. Por qué el multiplicador monetario describe mal el proceso

El modelo tradicional dice:

```text
1. el banco central inyecta reservas
2. los bancos prestan un múltiplo de esas reservas
3. multiplicador = 1 / encaje
```

Las objeciones documentadas por bancos centrales y por la evidencia:

```text
· el orden causal está invertido: los bancos prestan primero y consiguen las reservas después
· el banco central fija la TASA, no la cantidad de reservas: provee las que el sistema demande
  a esa tasa
· con encaje de 10 %, el multiplicador teórico sería 10; los valores observados difieren
  ampliamente y varían en el tiempo
· en periodos de expansión masiva del balance del banco central, las reservas crecieron
  mucho más que el crédito, contradiciendo la predicción del modelo
```

La conclusión práctica: el multiplicador es una **razón contable observada** (`M2/M0`), útil como
descripción y no como mecanismo. Quien lo usa como mecanismo predice mal.

### 5. Crédito, inflación y estabilidad

El crecimiento del crédito se relaciona con la inflación y con la estabilidad financiera, y esa relación justifica buena parte de la regulación. La tabla la desarrolla.

```text
crecimiento del crédito muy por sobre el del PIB nominal
  → si financia CONSUMO: presión de demanda → inflación
  → si financia ACTIVOS: alza de precios de activos → riesgo de burbuja
  → si financia INVERSIÓN productiva: aumenta la capacidad → menos presión inflacionaria
```

Por eso el seguimiento macroprudencial no mira solo cuánto crece el crédito, sino **hacia dónde va**:

| Destino del crédito | Riesgo dominante |
|---|---|
| Consumo | Sobreendeudamiento de hogares, inflación |
| Vivienda | Burbuja inmobiliaria, concentración |
| Inversión productiva | Menor, si el proyecto es viable |
| Compra de activos financieros | Apalancamiento y fragilidad de mercado |

La **brecha crédito/PIB** de la clase 8 es el indicador agregado de este seguimiento.

## 🧮 Ejemplo guiado

**Situación.** Un sistema bancario simplificado con tres bancos. Analiza qué ocurre con el dinero.

```text
SITUACIÓN INICIAL
  base monetaria: 10 000 (circulante 3 000 + reservas 7 000)
  depósitos totales: 70 000
  colocaciones totales: 63 000
  encaje exigido: 10 % de los depósitos = 7 000  ✔ exactamente cumplido
```

**Paso 1 — el banco A otorga un crédito de 5 000.**

```text
banco A: colocación +5 000, depósito +5 000
depósitos del sistema: 75 000
encaje exigido: 7 500
reservas disponibles: 7 000  → DÉFICIT de 500
```

**Paso 2 — cómo se resuelve el déficit.**

```text
opción 1  el banco A pide reservas en el mercado interbancario
          → otro banco con exceso se las presta a la tasa interbancaria
          → si el sistema en conjunto tiene déficit, la tasa SUBE

opción 2  el banco central provee las reservas
          → mediante operaciones de mercado abierto, a la tasa de política
          → la base monetaria aumenta a 10 500
```

**Lo decisivo:** el banco central provee las reservas **para mantener la tasa en su nivel objetivo**.
Si no las proveyera, la tasa interbancaria subiría sobre la meta. Es decir, **la cantidad de reservas
es endógena a la decisión de tasa**, no al revés.

**Paso 3 — cálculo del multiplicador observado.**

```text
antes:   M2/M0 = 73 000 / 10 000 = 7,30
después: M2/M0 = 78 000 / 10 500 = 7,43
```

El multiplicador cambió sin que nadie lo decidiera. Es una razón resultante, no un parámetro.

**Paso 4 — el límite que sí operó.**

```text
supongamos que el banco A tiene capital de 4 200 y activos ponderados por riesgo de 42 000
  razón de capital = 10,0 % (mínimo exigido: 10,0 %)

el nuevo crédito de 5 000, con ponderación de 100 %:
  activos ponderados = 47 000
  razón de capital = 4 200 / 47 000 = 8,94 %  → INCUMPLE
```

**El banco A no puede otorgar ese crédito por falta de capital, aunque las reservas estuvieran
disponibles.** Ese es el límite vinculante en la práctica.

**Paso 5 — qué debería hacer el banco A.**

```text
opción 1  aumentar capital: emitir acciones o retener utilidades
          capital necesario para 47 000 al 10 % = 4 700 → aportar 500
opción 2  otorgar el crédito con menor ponderación de riesgo (garantía real)
          si la ponderación fuera 50 %: activos ponderados = 44 500
          razón = 9,44 % → aún incumple
opción 3  reducir otros activos ponderados
opción 4  no otorgar el crédito
```

**Paso 6 — la conclusión sistémica.**

```text
si TODOS los bancos están cerca de su mínimo de capital:
  · el crédito no crece aunque haya reservas abundantes
  · la política monetaria expansiva tiene poco efecto sobre el crédito
  · el instrumento efectivo es el CAPITAL, no la liquidez

este es exactamente el diagnóstico de varias economías tras 2008:
  reservas enormes, crédito estancado, porque el límite era el capital
```

**Interpreta:** el modelo del multiplicador predice que más reservas producen más crédito. **El caso
muestra que el límite operativo fue el capital**, y que las reservas se ajustaron a la decisión de tasa
del banco central. Entender esta diferencia es lo que permite anticipar si una medida de política
tendrá efecto sobre el crédito o no.

## 🏦 Del cliente al banco

El cliente cree que le prestan lo que otros depositaron y el banco crea un depósito al otorgar el crédito. La tabla enfrenta las dos lecturas, y es de las que más cambian la comprensión del negocio bancario.

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| Creación de depósitos | Naturaleza del negocio bancario | 10, clase 1 |
| Capital como límite | Planificación de crecimiento | 12, clase 1 |
| Reservas y liquidación | Gestión diaria de tesorería | 10, clase 12 |
| Encaje | Costo del fondeo de depósitos | 10, clase 2 |
| Destino del crédito | Concentración y riesgo sistémico | 11, clase 1 |

## 🧪 Práctica

El laboratorio pide seguir los asientos de una operación de crédito y comprobar el efecto sobre los agregados. Verlo en asientos es lo que hace creíble el mecanismo.

En `labs/lab-06.md`, sección de dinero:

1. Obtén los agregados monetarios de tu país y calcula la proporción de dinero bancario.
2. Registra los asientos de creación y destrucción de dinero de un crédito completo.
3. Calcula el multiplicador observado de tu país en cinco años y explica su variación.
4. Determina si el límite vinculante de un banco simplificado es el capital o la liquidez.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen razonamientos que parten del modelo equivocado. La causa es el multiplicador monetario entendido como una restricción operativa y no como una relación observada.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se cree que los bancos prestan los depósitos que reciben | Modelo de intermediación simple | El crédito crea el depósito. |
| Se usa el multiplicador como mecanismo causal | Modelo incompleto | Es una razón observada, no un parámetro. |
| Se espera que más reservas produzcan más crédito | Límite mal identificado | El límite habitual es el capital. |
| Se cree que el dinero es principalmente efectivo | Proporción real desconocida | Más del 90 % son depósitos. |
| Se ignora el destino del crédito | Solo se mira el volumen | El riesgo depende de hacia dónde va. |
| Se supone que el banco central controla la cantidad de dinero | Instrumento confundido | Controla la tasa; la cantidad se ajusta. |

## ❓ Preguntas de comprobación

1. Escribe los asientos por los que un banco crea dinero al otorgar un crédito.
2. ¿Qué proporción del dinero es circulante y qué proporción es dinero bancario?
3. Nombra tres límites reales a la creación de dinero e indica cuál suele ser vinculante.
4. ¿Por qué el modelo del multiplicador describe mal el proceso?
5. ¿Por qué importa hacia dónde va el crédito y no solo cuánto crece?

## 📥 Entregable

Guarda en `portfolio/parte-06/clase-12/`:

- los agregados monetarios de tu país con la proporción de dinero bancario;
- los asientos de creación y destrucción de dinero de un crédito completo;
- el multiplicador observado de cinco años con la explicación de su variación;
- el análisis del límite vinculante de un banco simplificado.

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

- McLeay, M., Radia, A. y Thomas, R. (2014). "Money creation in the modern economy". *Bank of England Quarterly Bulletin*, Q1. Descripción operativa de la creación de dinero por los bancos. <https://www.bankofengland.co.uk/quarterly-bulletin/2014/q1/money-creation-in-the-modern-economy>
- Bank for International Settlements (2015). *Should monetary policy target financial stability?*. BIS. Relación entre crédito, dinero y estabilidad.
- Mishkin, F. (2022). *The Economics of Money, Banking and Financial Markets* (13.ª ed.). Pearson. Capítulos 3 y 14: agregados monetarios y oferta de dinero.
- Jakab, Z. y Kumhof, M. (2015). "Banks are not intermediaries of loanable funds — and why this matters". *Bank of England Working Paper 529*.
- Basel Committee on Banking Supervision (2017). *Basel III: Finalising post-crisis reforms*. BIS. El capital como restricción al crecimiento del balance.
- Verificación local: descarga los agregados monetarios publicados por el banco central de tu país y la tasa de encaje vigente por tipo de depósito.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 11 · Bancos centrales](11-bancos-centrales.md) | [Parte 06](../README.md) · [Programa](../../../SYLLABUS.md) | [13 · Tipo de cambio →](13-tipo-de-cambio.md) |
<!-- gen:footer:end -->
