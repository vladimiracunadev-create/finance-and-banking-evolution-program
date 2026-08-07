<!-- meta
part: 1
class: 7
title: "Inflación y poder adquisitivo"
level: fundamento
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 07 · Inflación y poder adquisitivo

> [← 06 · Interés compuesto](06-interes-compuesto.md) · [Índice de la parte](../README.md) · [08 · Valor del dinero en el tiempo →](08-valor-del-dinero-en-el-tiempo.md)

**Parte 01 — Matemática financiera básica** · **Nivel:** Fundamento — sin conocimientos previos · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Separar dos preguntas que suelen mezclarse: *¿cuánto dinero tengo?* y *¿cuánto puedo comprar con
él?*. La inflación es el interés compuesto de la clase 6 operando en contra del que guarda dinero
quieto. Esta clase enseña a calcular en términos reales, a leer una tasa real negativa y a entender
por qué existen las unidades indexadas como la UF, la UVR o la UDI.

Las dos clases anteriores calcularon cuánto crece un capital. Esta pregunta si ese crecimiento significa algo. Un saldo que aumenta un cinco por ciento mientras los precios suben un siete es un saldo que perdió, y esa resta —que es la operación más simple del programa— es la que separa contar pesos de contar capacidad de compra.

## 📚 Objetivos

Al finalizar podrás:

1. **Calcular** el poder adquisitivo de una suma en cualquier momento del tiempo.
2. **Aplicar** la ecuación de Fisher exacta y saber cuándo su aproximación falla.
3. **Interpretar** una tasa real negativa y sus consecuencias sobre el ahorro.
4. **Explicar** el propósito de una unidad de cuenta indexada y cómo se opera con ella.
5. **Proyectar** el costo futuro de una meta ajustando por inflación.

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

Las cuatro primeras entradas separan lo que se cuenta en pesos de lo que se cuenta en canastas, y las tres últimas son las herramientas y los riesgos que aparecen cuando esa separación se ignora. La **tasa real** es el concepto que hay que interiorizar: es la única que responde a la pregunta de si se ganó o se perdió.

| Concepto | Comprensión verificable |
|---|---|
| `inflación (π)` | Variación porcentual sostenida del nivel general de precios, medida por un índice de precios al consumidor. No es "que todo suba"; es el promedio ponderado de una canasta definida. |
| `poder adquisitivo` | Cantidad de bienes que compra una suma. `PA = monto / (1 + π)^n`. Cae de forma exponencial, igual que el interés compuesto sube. |
| `tasa nominal` | La que aparece en el contrato. No dice nada sobre capacidad de compra. |
| `tasa real (r)` | `(1 + nominal)/(1 + π) − 1`. Lo que realmente ganaste o perdiste en bienes. |
| `ecuación de Fisher` | `(1+n) = (1+r)(1+π)`. La aproximación `r ≈ n − π` solo sirve con tasas bajas. |
| `unidad indexada` | Unidad de cuenta que se reajusta por inflación (UF en Chile, UVR en Colombia, UDI en México, ICP/UMA). Traslada el riesgo inflacionario del acreedor al deudor. |
| `represión financiera` | Situación de tasa real negativa sostenida: quien ahorra en depósitos pierde poder de compra aunque su saldo nominal suba. |

## 🧠 Modelo mental

Imagina dos reglas para medir el mismo dinero:

```text
regla nominal    cuenta pesos            → siempre parece que hay más
regla real       cuenta canastas         → dice la verdad
```

Un salario que sube 8 % con inflación de 8 % no subió: cambió de número. Todo informe financiero
serio declara si sus cifras son nominales o reales, y a qué fecha están expresadas.

## 📖 Desarrollo

### 1. Pérdida de poder adquisitivo

Antes de comparar tasas conviene ver el efecto sobre un monto quieto, que no rinde nada. Un capital guardado bajo el colchón no baja de valor nominal y sí baja de valor real, y la fórmula siguiente es la que cuantifica exactamente cuánto.

```text
poder adquisitivo futuro = monto / (1 + π)^n
```

Diez millones guardados bajo el colchón, con inflación de 4,5 % anual:

| Años | Valor nominal | Poder adquisitivo | Pérdida |
|---:|---:|---:|---:|
| 0 | 10 000 000 | 10 000 000 | 0 % |
| 5 | 10 000 000 | 8 024 510 | −19,8 % |
| 10 | 10 000 000 | 6 439 277 | −35,6 % |
| 20 | 10 000 000 | 4 146 429 | −58,5 % |
| 30 | 10 000 000 | 2 670 000 | −73,3 % |

Nadie te quitó el dinero. Simplemente compra un cuarto de lo que compraba. Y con inflación de 10 %
—no excepcional en América Latina— la pérdida a 10 años es del 61 %.

### 2. La ecuación de Fisher

La relación entre tasa nominal, tasa real e inflación tiene una forma exacta y una aproximación que se usa a diario. Conviene conocer las dos y, sobre todo, saber cuándo la aproximación deja de servir, que es cuando la inflación es alta.

```text
exacta         r = (1 + n)/(1 + π) − 1
aproximada     r ≈ n − π
```

| Nominal | Inflación | Aproximada | Exacta | Error |
|---:|---:|---:|---:|---:|
| 5 % | 3 % | 2,00 % | 1,94 % | 0,06 pp |
| 12 % | 8 % | 4,00 % | 3,70 % | 0,30 pp |
| 30 % | 25 % | 5,00 % | 4,00 % | 1,00 pp |
| 80 % | 70 % | 10,00 % | 5,88 % | 4,12 pp |
| 200 % | 180 % | 20,00 % | 7,14 % | 12,86 pp |

La aproximación es cómoda y peligrosa: en contextos de inflación alta sobreestima de forma
sistemática el rendimiento real. Usa siempre la exacta; cuesta una división.

### 3. Tasa real negativa

Un depósito a 3,5 % anual con inflación de 5,2 %:

```text
r = (1,035 / 1,052) − 1 = −0,016160 → −1,62 % real
```

Sobre 20 000 000 durante tres años:

```text
nominal   20 000 000 × 1,035³ = 22 174 000    ← "gané 2,17 millones"
real      20 000 000 × 0,9838³ = 19 044 000   ← perdiste 956 000 en capacidad de compra
```

Esta es la situación normal en gran parte del mundo durante buena parte de la última década, y es la
razón por la cual una cuenta de ahorro no es un instrumento de inversión sino de liquidez. Aparece
formalmente en la Parte 2, clase 6, y en la Parte 8, clase 1.

### 4. Unidades indexadas

Una unidad indexada resuelve un problema concreto: **prestar a 20 años sin saber la inflación
futura**. En lugar de fijar el crédito en pesos, se fija en una unidad que se reajusta con el índice
de precios.

```text
crédito de 2 000 UF a 20 años, tasa real 4,2 %
  la cuota se calcula en UF con la tasa REAL
  cada mes se paga el equivalente en pesos al valor de la UF de ese día
```

Consecuencias que hay que entender antes de firmar:

| Ventaja | Riesgo |
|---|---|
| La tasa contratada es **real**: el acreedor no necesita un colchón por inflación esperada, por lo que la tasa nominal equivalente suele ser menor | La cuota en pesos **sube con la inflación**, aunque la cuota en UF sea constante |
| Permite plazos largos (20–30 años) que en pesos serían inviables | Si el ingreso del deudor no se reajusta al mismo ritmo, la carga real aumenta |
| Hace comparables créditos de distintas épocas | Requiere entender dos monedas a la vez |

La Parte 3, clase 9, desarrolla el crédito hipotecario en unidad indexada con su tabla completa.

### 5. Proyectar una meta

Una meta futura debe expresarse en pesos **del momento en que se gastará**:

```text
costo futuro = costo hoy × (1 + π)^n
```

Un pie de vivienda que hoy cuesta 25 000 000, con inflación de 4 % y compra en 6 años:

```text
25 000 000 × 1,04^6 = 25 000 000 × 1,265319 = 31 632 975
```

Ahorrar "25 millones" para dentro de seis años es quedarse 6,6 millones corto. Este cálculo es el
que abre la Parte 2, clase 10, sobre metas SMART.

## 🧮 Ejemplo guiado

**Situación.** Paula tiene 12 000 000 en un depósito que renta 6,3 % anual nominal. La inflación
esperada es 4,8 % anual. Quiere comprar en 4 años un equipo que hoy cuesta 14 500 000. ¿Le alcanza?

**Paso 1 — monto nominal en 4 años.**

```text
12 000 000 × (1,063)^4 = 12 000 000 × 1,276901 = 15 322 812
```

**Paso 2 — costo del equipo en 4 años.**

```text
14 500 000 × (1,048)^4 = 14 500 000 × 1,206478 = 17 493 931
```

**Paso 3 — comparación en el mismo momento del tiempo.**

```text
disponible   15 322 812
necesario    17 493 931
brecha       −2 171 119     ← NO le alcanza
```

**Paso 4 — verificación por la vía real.**

```text
tasa real r = (1,063 / 1,048) − 1 = 0,014313 → 1,4313 %
capital real en 4 años = 12 000 000 × (1,014313)^4 = 12 700 000 (en pesos de hoy)
costo hoy del equipo = 14 500 000
brecha en pesos de hoy = −1 800 000
```

Y `−1 800 000 × 1,048^4 = −2 171 800`. ✔ Coincide con el paso 3 salvo redondeo. **Los dos caminos
—todo nominal o todo real— deben dar el mismo resultado; mezclarlos es el error clásico.**

**Paso 5 — decide.** Paula necesita aportar 1 800 000 adicionales en pesos de hoy, o bien buscar un
instrumento con tasa real superior a 4,9 % anual, o postergar la compra. Ninguna de las tres es
gratis, y esa es la conversación honesta.

## 🏦 Del cliente al banco

El cliente mira su saldo y el banco mira el margen real de la captación. La tabla enfrenta las dos lecturas y muestra por qué una tasa que parece generosa puede estar por debajo de la inflación sin que el titular se entere.

| Situación | Lectura ingenua | Lectura profesional |
|---|---|---|
| "Mi depósito rindió 6 %" | Ganancia | Tasa real de 1,4 %; el resto compensó inflación |
| "La cuota de mi hipotecario subió" | Error del banco | Crédito en unidad indexada; la cuota en UF no cambió |
| "El sueldo subió 5 %" | Aumento | Con inflación 5,5 %, es una caída real de 0,47 % |
| Proyección de negocio a 5 años | Pesos de hoy | Se declara si es nominal o real y con qué supuesto de inflación |

## 🧪 Práctica

El laboratorio pide deflactar series y calcular tasas reales en escenarios donde la nominal es positiva y la real es negativa. Es el ejercicio que más cambia la intuición de quien empieza, porque produce el resultado incómodo de que un depósito que paga intereses puede estar perdiendo dinero.

En `labs/lab-04.md`:

1. Calcula la pérdida de poder adquisitivo de un monto a 5, 10, 20 y 30 años con tres escenarios de inflación.
2. Compara Fisher exacta contra aproximada en seis combinaciones y tabula el error.
3. Toma tres productos de ahorro reales y calcula su tasa real con la inflación oficial vigente.
4. Proyecta dos metas personales a valor futuro y determina el aporte mensual necesario.

## ⚠️ Errores frecuentes

Los síntomas de la tabla comparten la misma raíz: se compararon pesos de momentos distintos como si fueran la misma unidad. La corrección casi siempre consiste en deflactar antes de comparar, no en rehacer el cálculo.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| La proyección da un resultado imposible | Se mezcló capital nominal con costo en pesos de hoy | Elige un marco —todo nominal o todo real— y no lo mezcles. |
| La tasa real calculada es demasiado optimista | Se usó `n − π` con inflación alta | Usa Fisher exacta siempre. |
| "Mi ahorro creció" pero no alcanza para lo mismo | Se midió en pesos y no en canastas | Deflacta antes de concluir. |
| Sorpresa por el alza de la cuota hipotecaria | Crédito en unidad indexada no comprendido | La cuota es constante en UF, variable en pesos. |
| Se ahorra el precio actual de una meta futura | No se proyectó el costo | `costo futuro = costo hoy × (1+π)^n`. |
| Se usa la inflación del año pasado para proyectar 20 años | Supuesto único sin escenarios | Modela al menos tres escenarios de inflación. |

## ❓ Preguntas de comprobación

1. Con inflación de 6 %, ¿cuánto poder de compra pierde un monto guardado 10 años?
2. ¿Por qué la aproximación `r ≈ n − π` falla con inflación de 60 %?
3. ¿Qué significa una tasa real negativa y quién gana en esa situación?
4. ¿Qué riesgo asume el deudor en un crédito en unidad indexada que no asume en uno en pesos?
5. ¿Por qué es un error ahorrar exactamente el precio de hoy de una meta a cinco años?

## 📥 Entregable

Guarda en `portfolio/parte-01/clase-07/`:

- la tabla de pérdida de poder adquisitivo en tres escenarios;
- la comparación Fisher exacta vs. aproximada con el error tabulado;
- la tasa real de tres productos de ahorro reales, con fuente y fecha del dato de inflación;
- una meta personal proyectada a valor futuro con el aporte mensual requerido.

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

- Fisher, I. (1930). *The Theory of Interest*. Macmillan. Capítulo 2: formulación original de la relación entre tasa nominal, real e inflación.
- Mankiw, N. G. (2021). *Principios de economía* (9.ª ed.). Cengage. Capítulos 24 y 30: medición del costo de vida y efecto Fisher.
- Blanchard, O. (2021). *Macroeconomía* (8.ª ed.). Pearson. Capítulo 14: tasas nominales y reales, y expectativas de inflación.
- Mishkin, F. (2022). *The Economics of Money, Banking and Financial Markets* (13.ª ed.). Pearson. Capítulo 4: cálculo de rendimientos reales.
- International Labour Organization (2004). *Consumer Price Index Manual: Theory and Practice*. OIT/FMI/OCDE. Construcción y limitaciones del IPC.
- Verificación local: usa la serie oficial de inflación de tu país y el valor publicado de la unidad indexada correspondiente (UF, UVR, UDI), registrando la fecha del dato.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 06 · Interés compuesto](06-interes-compuesto.md) | [Parte 01](../README.md) · [Programa](../../../SYLLABUS.md) | [08 · Valor del dinero en el tiempo →](08-valor-del-dinero-en-el-tiempo.md) |
<!-- gen:footer:end -->
