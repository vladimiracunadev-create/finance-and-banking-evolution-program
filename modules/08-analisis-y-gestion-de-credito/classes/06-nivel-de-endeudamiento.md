---
part: 9
class: 6
title: "Nivel de endeudamiento"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 06 · Nivel de endeudamiento

> [← 05 · Capacidad de pago](05-capacidad-de-pago.md) · [Índice de la parte](../README.md) · [07 · Historial crediticio →](07-historial-crediticio.md)

**Parte 09 — Análisis y gestión de crédito** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Determinar la exposición total del deudor, incluida la que no aparece en el informe estándar. Un
análisis que solo considera las deudas declaradas subestima sistemáticamente el riesgo, y el
sobreendeudamiento es la causa más frecuente de incumplimiento en carteras minoristas.

La capacidad de pago de la clase anterior se calcula sobre las deudas conocidas. Esta clase se ocupa de encontrarlas todas, que es más difícil de lo que parece: hay deuda que no aparece en el informe, cupos disponibles que se pueden usar mañana y avales que obligan sin figurar como deuda propia.

## 📚 Objetivos

Al finalizar podrás:

1. **Construir** el endeudamiento total consolidado de un deudor.
2. **Incorporar** cupos disponibles, avales y deudas no registradas.
3. **Calcular** los indicadores de endeudamiento y sus límites.
4. **Analizar** la composición y el perfil de vencimientos de la deuda.
5. **Detectar** patrones de sobreendeudamiento incipiente.

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

Los tres primeros términos son las formas de endeudamiento y su disponibilidad; los cuatro siguientes, los indicadores y lo que se escapa. La **deuda no registrada** es la que más sorpresas da: créditos informales, deudas con proveedores o avales que no constan en ningún informe.

| Concepto | Comprensión verificable |
|---|---|
| `endeudamiento directo` | Deudas vigentes a nombre del deudor. |
| `endeudamiento indirecto` | Avales, codeudas y garantías otorgadas a terceros. |
| `cupo disponible` | Crédito aprobado no utilizado. Es deuda potencial. |
| `endeudamiento relativo` | `deuda total / renta anual`. Mide el tamaño del compromiso. |
| `composición` | Proporción de deuda cara, con garantía, de corto plazo. |
| `perfil de vencimientos` | Distribución temporal de las obligaciones. |
| `deuda no registrada` | Obligaciones con casas comerciales, cajas, particulares o proveedores. |

## 🧠 Modelo mental

El endeudamiento real tiene **cuatro capas**, y el informe estándar muestra solo la primera:

```text
capa 1  deudas registradas en el sistema financiero    → informe estándar
capa 2  cupos disponibles no utilizados                → informe, pero suele ignorarse
capa 3  avales y codeudas                              → informe, en sección separada
capa 4  deudas fuera del sistema financiero            → NO aparece: se pregunta y se verifica
```

Omitir las capas 2 a 4 es el error que más subestima el riesgo en carteras de consumo.

## 📖 Desarrollo

### 1. Construir el endeudamiento consolidado

El endeudamiento consolidado se arma de varias fuentes porque ninguna las tiene todas. El procedimiento siguiente las reúne.

```text
ENDEUDAMIENTO TOTAL =
    deudas directas vigentes
  + porcentaje de cupos disponibles
  + avales y codeudas ponderados
  + deudas fuera del sistema financiero
```

```text
ejemplo:
  crédito de consumo, saldo                       3 200 000
  crédito automotriz, saldo                       5 800 000
  tarjeta banco A, utilizado                      1 400 000
  tarjeta banco A, cupo disponible                2 600 000
  tarjeta casa comercial, utilizado                 680 000
  línea de crédito, no utilizada                  1 500 000
  aval a un familiar                              4 000 000
  deuda con caja de compensación                    920 000
```

```text
CONSOLIDADO
  directas vigentes                              11 080 000
  cupos disponibles × 50 % (política)             2 050 000
  aval × 50 % (probabilidad de ejecución)         2 000 000
  deuda fuera del sistema (verificada)              920 000
  TOTAL                                          16 050 000

versus el informe estándar, que mostraría 10 400 000
diferencia: 5 650 000 (54 % más)
```

### 2. Tratamiento de los cupos disponibles

Un cupo no usado no es deuda hoy y puede serlo mañana sin que nadie lo autorice. La tabla recoge los criterios de tratamiento.

```text
¿por qué computar un cupo no utilizado?
  · el deudor puede usarlo mañana sin pedir autorización
  · la evidencia muestra que el uso de cupos aumenta ante estrés financiero
  · un deudor con cupos amplios tiene mayor capacidad de deteriorarse rápido
```

Ponderaciones habituales:

| Tipo de cupo | Ponderación de referencia |
|---|---:|
| Tarjeta de crédito | 50–100 % |
| Línea de crédito | 50–100 % |
| Sobregiro pactado | 100 % |
| Cupo de crédito preaprobado no aceptado | 0–25 % |

**Consecuencia práctica para el cliente:** cerrar cupos no utilizados antes de solicitar un crédito
importante mejora materialmente la evaluación (Parte 3, clase 6).

### 3. Avales y codeudas

Un aval obliga igual que una deuda propia y no aparece igual en los informes. La tabla recoge su tratamiento.

```text
un aval es una obligación contingente que puede volverse directa
```

Ponderación según la situación del deudor principal:

| Situación del avalado | Ponderación del aval |
|---|---:|
| Al día, con buen historial | 25–50 % |
| Con mora reciente | 75–100 % |
| En mora significativa | 100 % |
| Sin información | 50 % |

```text
además, se evalúa:
  · el número de avales otorgados (concentración)
  · si el avalado es una empresa relacionada
  · si existe contragarantía
```

### 4. Indicadores y límites

Los indicadores de endeudamiento se leen juntos y con sus límites de referencia. La tabla los recoge.

```text
endeudamiento relativo = deuda total / renta anual
carga financiera       = cuotas / renta mensual (clase 5)
composición cara       = deuda con tasa > 20 % / deuda total
cobertura de garantías = deuda con garantía / deuda total
```

| Indicador | Sano | Atención | Riesgo | Crítico |
|---|---|---|---|---|
| Endeudamiento relativo (consumo) | < 2× | 2–4× | 4–6× | > 6× |
| Endeudamiento relativo (con hipotecario) | < 4× | 4–6× | 6–8× | > 8× |
| Carga financiera | < 30 % | 30–40 % | 40–50 % | > 50 % |
| Composición cara | < 15 % | 15–30 % | 30–50 % | > 50 % |

```text
del ejemplo anterior, con renta anual de 28 800 000:
  endeudamiento relativo = 16 050 000/28 800 000 = 0,56×  → sano en tamaño
  composición cara = (1 400 000 + 680 000 + 920 000)/16 050 000 = 18,7 % → atención
```

**Los indicadores se leen juntos:** un endeudamiento relativo bajo con composición cara alta describe
a alguien que debe poco y lo debe mal.

### 5. Patrones de sobreendeudamiento incipiente

Antes de que los indicadores se disparen hay patrones reconocibles en el comportamiento. La tabla los recoge.

| Patrón | Qué indica |
|---|---|
| Aumento del número de acreedores en 12 meses | Búsqueda de crédito en múltiples fuentes |
| Uso creciente de cupos rotativos | Deterioro del flujo |
| Avances en efectivo | Estrés de liquidez agudo |
| Refinanciamientos sucesivos | Incapacidad de amortizar |
| Consultas frecuentes al informe de deudas | Solicitudes múltiples simultáneas |
| Migración de deuda bancaria a no bancaria | Pérdida de acceso al crédito formal |
| Cuotas que crecen más rápido que la renta | Trayectoria insostenible |

```text
señal compuesta de alerta:
  ≥ 3 patrones simultáneos → alta probabilidad de deterioro en 6–12 meses
```

## 🧮 Ejemplo guiado

El ejemplo consolida el endeudamiento de un solicitante con cupos y avales. Conviene comparar con el informe simple: la diferencia suele cambiar la decisión.

**Situación.** Un solicitante pide un crédito de consumo de 8 000 000. Analiza su endeudamiento.

```text
INFORME DEL SISTEMA FINANCIERO
  banco A · crédito consumo · saldo 2 400 000 · cuota 145 000 · al día
  banco A · tarjeta · utilizado 890 000 · cupo total 2 500 000 · al día
  banco B · crédito automotriz · saldo 6 100 000 · cuota 198 000 · al día
  banco B · línea de crédito · utilizado 0 · cupo 1 200 000
  banco C · tarjeta · utilizado 1 340 000 · cupo total 1 800 000 · mora 15 días
  emisor D · tarjeta · utilizado 620 000 · cupo total 900 000 · al día

SECCIÓN DE AVALES
  aval a Comercial Vega SpA · deuda avalada 12 000 000 · estado: al día

DECLARADO POR EL SOLICITANTE
  deuda con caja de compensación: 1 100 000, cuota 62 000
  deuda con una casa comercial: "no recuerda el monto"

RENTA ADMISIBLE: 1 950 000 mensuales
```

**Paso 1 — construye el consolidado.**

```text
DIRECTAS VIGENTES
  consumo banco A                     2 400 000
  tarjeta banco A                       890 000
  automotriz banco B                  6 100 000
  tarjeta banco C                     1 340 000
  tarjeta emisor D                      620 000
  caja de compensación                1 100 000
  SUBTOTAL                           12 450 000

CUPOS DISPONIBLES (ponderación 50 %)
  banco A: 2 500 000 − 890 000 = 1 610 000
  banco B línea: 1 200 000
  banco C: 1 800 000 − 1 340 000 = 460 000
  emisor D: 900 000 − 620 000 = 280 000
  total disponible 3 550 000 × 50 % =  1 775 000

AVALES
  Comercial Vega al día → ponderación 50 %
  12 000 000 × 50 % =                 6 000 000

DEUDA NO VERIFICADA
  casa comercial: monto desconocido → EXIGE VERIFICACIÓN

TOTAL CONOCIDO                       20 225 000
```

**Paso 2 — el hallazgo del aval.**

```text
el aval de 12 000 000 a Comercial Vega SpA es 96 % del endeudamiento directo del solicitante

preguntas obligatorias:
  · ¿qué relación tiene el solicitante con Comercial Vega?
  · ¿es socio, administrador o solo avalista?
  · ¿existe contragarantía?
  · ¿cuál es la situación financiera de Comercial Vega?
```

**Respuesta obtenida:** el solicitante es socio en un 40 % y administrador. Entonces:

```text
el aval NO es una obligación de un tercero: es su propia empresa
la ponderación de 50 % es INSUFICIENTE
si la empresa falla, el solicitante responde por el total
ponderación aplicable: 100 % → 12 000 000
```

**Paso 3 — recalcula.**

```text
directas                             12 450 000
cupos ponderados                      1 775 000
aval a empresa propia (100 %)        12 000 000
TOTAL                                26 225 000
```

**Paso 4 — indicadores.**

```text
renta anual = 1 950 000 × 12 = 23 400 000

endeudamiento relativo = 26 225 000/23 400 000 = 1,12×
  → parece sano

carga financiera actual:
  cuotas conocidas: 145 000 + 198 000 + 62 000 = 405 000
  tarjetas (pago mínimo estimado 5 %): 2 850 000 × 0,05 = 142 500
  total: 547 500
  carga = 547 500/1 950 000 = 28,1 %

con el crédito solicitado (8 000 000 a 48 meses, tasa 1,4 %):
  cuota nueva ≈ 231 000
  carga = 778 500/1 950 000 = 39,9 %  → en el límite
```

**Paso 5 — busca los patrones de sobreendeudamiento.**

```text
□ aumento de acreedores en 12 meses        → 5 acreedores; hace 12 meses tenía 3  ✗ PATRÓN
□ uso creciente de rotativos               → tarjetas al 68 % del cupo total      ✗ PATRÓN
□ avances en efectivo                      → sin evidencia                          —
□ refinanciamientos sucesivos              → sin evidencia                          —
□ consultas frecuentes al informe          → 7 consultas en 6 meses                ✗ PATRÓN
□ migración a no bancario                  → caja de compensación reciente         ✗ PATRÓN
□ cuotas creciendo más que la renta        → cuotas +42 % en 12 meses, renta +5 %  ✗ PATRÓN

CINCO PATRONES SIMULTÁNEOS
```

**Paso 6 — la mora de 15 días en el banco C.**

```text
mora de 15 días es menor y NO es aislada en este contexto:
  · ocurre con cinco patrones de sobreendeudamiento presentes
  · el cupo del banco C está al 74 %
  · es el emisor con mayor utilización relativa

interpretación: primera manifestación de estrés de liquidez
```

**Paso 7 — decisión.**

```text
RECHAZAR la operación en su forma solicitada

fundamento:
  1. el aval a la empresa propia debe computarse al 100 %: el endeudamiento
     real es 2,5 veces el que muestra el informe estándar
  2. cinco patrones simultáneos de sobreendeudamiento incipiente
  3. mora incipiente en el acreedor con mayor utilización de cupo
  4. la carga financiera llegaría al 39,9 %, en el límite, sin considerar
     una eventual ejecución del aval
  5. existe una deuda declarada no cuantificada (casa comercial)

ALTERNATIVA CONSTRUCTIVA
  ofrecer una operación de CONSOLIDACIÓN por 4 800 000 que:
    · extinga las tres tarjetas y la deuda de la caja
    · reduzca la carga financiera de 28,1 % a 22,4 %
    · exija el cierre de los cupos consolidados
    · reduzca la composición cara de 40 % a 8 %
  
  esta operación mejora la posición del cliente Y la del banco,
  y es la respuesta correcta a un perfil de sobreendeudamiento incipiente

CONDICIÓN PREVIA en cualquier caso
  cuantificar y verificar la deuda con la casa comercial
```

**Interpreta:** el informe estándar mostraba un endeudamiento de 10,4 millones y una carga del 28 %:
un perfil aprobable. **El consolidado con el aval computado correctamente mostró 26,2 millones y cinco
patrones de deterioro.** La diferencia entre ambos análisis es de 2,5 veces, y la decisión se invierte.

## 🏦 Del cliente al banco

El cliente declara sus deudas y el banco reconstruye el endeudamiento real. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| "Solo tengo tres deudas" | El consolidado incluye cupos y avales | 2, clase 8 |
| Cupos no utilizados | Deuda potencial que consume capacidad | 3, clase 6 |
| Aval a la empresa propia | Obligación equivalente a deuda directa | 13, clase 13 |
| Consolidación ofrecida | Mejora la posición de ambas partes | 4, clase 11 |
| Rechazo con alternativa | Gestión responsable del cliente | 9, clase 15 |

## 🧪 Práctica

El laboratorio pide consolidar el endeudamiento de un caso con deuda no registrada y avales. Detectar lo que no está en el informe es el ejercicio.

En `labs/lab-03.md`, sección de endeudamiento:

1. Construye el endeudamiento consolidado de tres casos con las cuatro capas.
2. Aplica ponderaciones a cupos y avales según la situación del avalado.
3. Calcula los cuatro indicadores y ubícalos en el semáforo.
4. Busca los siete patrones de sobreendeudamiento en un caso sintético.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen deudores que resultaron más endeudados de lo evaluado. Las causas son los cupos y los avales no considerados.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se usa solo el informe estándar | Capas 2 a 4 omitidas | Consolida las cuatro capas. |
| Los cupos no se computan | Deuda potencial ignorada | Pondera según política. |
| El aval a empresa propia se pondera al 50 % | Relación no investigada | Si es su empresa, computa al 100 %. |
| No se verifica la deuda no bancaria | Se acepta "no recuerda" | Exige cuantificación y verificación. |
| Una mora menor se descarta | Contexto ignorado | Evalúala junto con los demás patrones. |
| Se rechaza sin alternativa | Oportunidad perdida | Ofrece consolidación cuando corresponda. |

## ❓ Preguntas de comprobación

1. ¿Cuáles son las cuatro capas del endeudamiento y cuál muestra el informe estándar?
2. ¿Por qué se computan los cupos no utilizados?
3. ¿Cómo se pondera un aval según la situación del avalado y de la relación?
4. Nombra cinco patrones de sobreendeudamiento incipiente.
5. ¿Cuándo una consolidación es mejor respuesta que un rechazo?

## 📥 Entregable

Guarda en `portfolio/parte-09/clase-06/`:

- el endeudamiento consolidado de tres casos con las cuatro capas;
- las ponderaciones aplicadas a cupos y avales con su justificación;
- los cuatro indicadores calculados con su ubicación en el semáforo;
- el análisis de patrones de sobreendeudamiento y la decisión con alternativa.

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

- European Banking Authority (2020). *Guidelines on loan origination and monitoring*. EBA. Evaluación del endeudamiento total del deudor.
- Basel Committee on Banking Supervision (2000). *Principles for the Management of Credit Risk*. BIS. Exposiciones directas e indirectas.
- OECD (2020). *Debt and Financial Vulnerability of Households*. OCDE. Indicadores de sobreendeudamiento.
- Anderson, R. (2007). *The Credit Scoring Toolkit*. Oxford University Press. Variables de endeudamiento y su poder predictivo.
- World Bank (2011). *General Principles for Credit Reporting*. Banco Mundial. Alcance y limitaciones de los informes de deuda. <https://www.worldbank.org/>
- Verificación local: revisa qué información contiene el informe de deudas de tu país, qué queda fuera y qué ponderación de cupos aplica tu institución.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 05 · Capacidad de pago](05-capacidad-de-pago.md) | [Parte 09](../README.md) · [Programa](../../../SYLLABUS.md) | [07 · Historial crediticio →](07-historial-crediticio.md) |
<!-- gen:footer:end -->
