---
part: 7
class: 8
title: "Valor actual neto"
level: avanzado
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 08 · Valor actual neto

> [← 07 · Sistemas de amortización](07-sistemas-de-amortizacion.md) · [Índice de la parte](../README.md) · [09 · Tasa interna de retorno →](09-tasa-interna-de-retorno.md)

**Parte 07 — Matemática financiera avanzada** · **Nivel:** Avanzado — perfil analista · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Dominar el criterio de decisión de inversión más sólido de las finanzas: el valor actual neto. Su
regla es simple —aceptar si es positivo— y su aplicación correcta exige rigor en tres puntos que se
descuidan sistemáticamente: qué flujos incluir, qué tasa usar y cómo comparar proyectos de distinta
escala o duración.

## 📚 Objetivos

Al finalizar podrás:

1. **Calcular** el VAN de un proyecto con flujos correctamente definidos.
2. **Determinar** qué flujos son relevantes y cuáles no.
3. **Justificar** la tasa de descuento con la alternativa concreta que representa.
4. **Comparar** proyectos de distinta escala y duración con el método correcto.
5. **Presentar** el resultado con su análisis de sensibilidad.

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
| `VAN` | `Σ FCF_t/(1+k)^t − I₀`. Valor creado por el proyecto, en unidades monetarias de hoy. |
| `flujo incremental` | Diferencia entre el flujo con proyecto y sin proyecto. Es el único relevante. |
| `costo hundido` | Desembolso ya realizado. **No** se incluye (Parte 6, clase 1). |
| `costo de oportunidad` | Valor del recurso propio usado en el proyecto. **Sí** se incluye. |
| `externalidad` | Efecto del proyecto sobre otros negocios de la empresa. Se incluye, positivo o negativo. |
| `VAN anualizado` | `VAN × k/[1−(1+k)^-n]`. Permite comparar proyectos de distinta duración. |
| `índice de rentabilidad` | `VP de los flujos / inversión`. Ordena proyectos con capital limitado. |

## 🧠 Modelo mental

El VAN responde una pregunta muy concreta:

```text
¿cuánto más rico soy hoy si hago este proyecto,
 en comparación con poner el mismo dinero en mi mejor alternativa de igual riesgo?
```

Un VAN de 4 200 000 significa: **este proyecto crea 4,2 millones de valor por sobre la alternativa**.
No significa que gane 4,2 millones: la alternativa también gana.

## 📖 Desarrollo

### 1. Qué flujos incluir

| Concepto | ¿Se incluye? | Por qué |
|---|---|---|
| Inversión inicial en activos | Sí | Salida de caja del proyecto |
| Capital de trabajo adicional | **Sí** | Inmoviliza caja; se recupera al final |
| Ingresos incrementales | Sí | Solo los que no existirían sin el proyecto |
| Costos incrementales | Sí | Solo los que se evitan sin el proyecto |
| Costo hundido (estudio ya pagado) | **No** | Irrecuperable, no cambia con la decisión |
| Depreciación | **No directamente** | No es flujo de caja; sí afecta el impuesto |
| Escudo fiscal de la depreciación | **Sí** | `depreciación × tasa de impuesto` |
| Intereses del financiamiento | **No** | Están en la tasa de descuento; incluirlos es doble conteo |
| Costo de oportunidad de un terreno propio | **Sí** | Su valor de mercado es una salida implícita |
| Canibalización de otro producto | **Sí, negativo** | Es un flujo incremental negativo |
| Valor de rescate de los activos | Sí | Entrada al final |

Las tres filas críticas son: **no incluir intereses**, **sí incluir capital de trabajo** y **sí incluir
el costo de oportunidad de los recursos propios**.

### 2. Construcción del flujo

```text
                              Año 0      Año 1      Año 2   ...
Ingresos                          —      45 000     52 000
− Costos operativos               —     −28 000    −31 500
− Depreciación                    —      −9 000     −9 000
= Resultado operativo             —       8 000     11 500
− Impuesto (25 %)                 —      −2 000     −2 875
= Resultado operativo neto        —       6 000      8 625
+ Depreciación                    —       9 000      9 000
= Flujo operativo                 —      15 000     17 625
− Inversión en activos      −45 000           —          —
− Δ capital de trabajo       −6 000      −1 200     −1 000
+ Recuperación de KT              —           —          —
= FLUJO DE CAJA LIBRE       −51 000      13 800     16 625
```

Nótese que la depreciación **se resta para calcular el impuesto y se suma de vuelta**, porque no es
salida de caja. Su único efecto real es el escudo fiscal.

### 3. Elegir y justificar la tasa

```text
la tasa de descuento debe reflejar el RIESGO DEL PROYECTO,
no el costo de la deuda que lo financia
```

| Contexto | Tasa apropiada |
|---|---|
| Proyecto del giro habitual de la empresa | Costo promedio ponderado de capital (WACC) |
| Proyecto de riesgo distinto al del giro | WACC ajustado por el riesgo del sector del proyecto |
| Evaluación desde el punto de vista del accionista | Costo del patrimonio, con flujos después de deuda |
| Persona evaluando una inversión | Rendimiento de su mejor alternativa de igual riesgo |

Regla de verificación: **si no puedes nombrar la alternativa concreta que la tasa representa, la tasa
está inventada** (Parte 1, clase 8).

### 4. Comparar proyectos

**Proyectos de distinta escala** — el VAN mayor gana si no hay restricción de capital:

```text
A: inversión 10 000, VAN 2 800
B: inversión 40 000, VAN 6 500
sin restricción de capital → B (crea más valor)
```

Con capital limitado a 40 000, se usa el **índice de rentabilidad**:

```text
IR = VP de los flujos / inversión
A: IR = 12 800/10 000 = 1,28
B: IR = 46 500/40 000 = 1,16
con 40 000 disponibles: 4 proyectos como A → VAN 11 200 > 6 500 de B
```

**Proyectos de distinta duración** — se usa el VAN anualizado:

```text
C: 4 años, VAN 8 400, k = 10 %
D: 7 años, VAN 11 900, k = 10 %

VAN anualizado C = 8 400 × 0,10/[1 − 1,10^-4] = 8 400/3,16987 = 2 650
VAN anualizado D = 11 900 × 0,10/[1 − 1,10^-7] = 11 900/4,86842 = 2 445

→ C es mejor, pese a tener menor VAN total
```

La lógica: si los proyectos son repetibles, C se puede repetir con más frecuencia.

### 5. Presentar el resultado

```text
✗ "El VAN del proyecto es 4 237 812"
✓ "El VAN es positivo en el rango de tasas de 9 % a 14 % y en los escenarios
   base y optimista. Se vuelve negativo si el volumen cae más de 18 % o si la
   tasa supera 15,2 %. El caso base al 11 % es 4,2 millones."
```

Toda presentación de VAN incluye:

```text
· caso base con su tasa y supuestos declarados
· tabla de sensibilidad a las dos variables más influyentes
· tasa de indiferencia (la que hace VAN = 0, es decir, la TIR)
· umbral de las variables operativas que anula el VAN
```

## 🧮 Ejemplo guiado

**Situación.** Una empresa evalúa una nueva línea de producción.

```text
DATOS
  inversión en equipos                   240 000
  vida útil y horizonte                   6 años
  valor de rescate al año 6               30 000
  capital de trabajo inicial              35 000 (se recupera al final)
  estudio de factibilidad ya pagado       18 000
  terreno propio, valor de mercado       120 000 (se usaría en el proyecto)
  ingresos año 1                         210 000, creciendo 5 % anual
  costos operativos                       58 % de los ingresos
  costos fijos incrementales              32 000/año
  canibalización de otra línea           −14 000/año de margen
  tasa de impuesto                        25 %
  WACC de la empresa                      11,5 %
```

**Paso 1 — decide qué incluir.**

```text
✓ inversión 240 000
✓ capital de trabajo 35 000 (salida año 0, entrada año 6)
✓ costo de oportunidad del terreno 120 000 (salida año 0, entrada año 6 a su valor)
✗ estudio de factibilidad 18 000 → COSTO HUNDIDO
✓ canibalización −14 000/año
✓ valor de rescate 30 000, con su efecto tributario
```

**Paso 2 — construye el flujo (extracto).**

```text
depreciación anual = (240 000 − 30 000)/6 = 35 000

                          Año 0      Año 1      Año 3      Año 6
Ingresos                      —    210 000    231 525    268 019
− Costos variables (58 %)     —   −121 800   −134 285   −155 451
− Costos fijos                —    −32 000    −32 000    −32 000
− Canibalización              —    −14 000    −14 000    −14 000
− Depreciación                —    −35 000    −35 000    −35 000
= Resultado operativo         —      7 200     16 240     31 568
− Impuesto (25 %)             —     −1 800     −4 060     −7 892
= Res. operativo neto         —      5 400     12 180     23 676
+ Depreciación                —     35 000     35 000     35 000
= Flujo operativo             —     40 400     47 180     58 676
− Inversión            −240 000          —          —          —
− Terreno (oportunidad)−120 000          —          —          —
− Capital de trabajo    −35 000          —          —          —
+ Recuperación KT             —          —          —     35 000
+ Rescate equipos             —          —          —     30 000
+ Terreno (recuperado)        —          —          —    120 000
= FLUJO DE CAJA LIBRE  −395 000     40 400     47 180    243 676
```

**Paso 3 — calcula el VAN.**

```text
Año   FCF        Factor (11,5 %)   VP
0    −395 000    1,000000         −395 000
1      40 400    0,896861           36 233
2      43 700    0,804360           35 151
3      47 180    0,721399           34 036
4      50 850    0,647004           32 900
5      54 720    0,580272           31 754
6     243 676    0,520424          126 812
                 VAN              −98 114
```

**El VAN es negativo.** El proyecto destruye 98 114 de valor.

**Paso 4 — identifica la causa.**

```text
el terreno, valorado en 120 000, representa el 30 % de la inversión total
sin incluirlo (error frecuente): VAN = −98 114 + 120 000 − 120 000 × 0,520424 = −40 565
sigue siendo negativo, pero mucho menos

la causa real: el margen operativo es demasiado bajo
  margen sobre ingresos año 1 = 7 200/210 000 = 3,4 %
```

**Paso 5 — análisis de sensibilidad.**

| Variable | Valor base | Umbral que hace VAN = 0 | Holgura |
|---|---:|---:|---:|
| WACC | 11,5 % | 6,9 % | −4,6 pp |
| Costos variables | 58,0 % | 52,4 % | −5,6 pp |
| Ingresos año 1 | 210 000 | 243 500 | +16,0 % |
| Canibalización | −14 000 | +6 500 | +20 500 |
| Valor del terreno | 120 000 | 21 000 | −99 000 |

**Paso 6 — recomendación.**

```text
RECHAZAR el proyecto en su configuración actual

alternativas a explorar antes de descartarlo definitivamente:
  1. arrendar el terreno en lugar de usarlo → libera 120 000 de costo de oportunidad
     pero requiere terreno alternativo: evaluar el costo del arriendo
  2. reducir costos variables a 52 % → exige renegociación de proveedores o escala
  3. eliminar la canibalización mediante diferenciación del producto
  4. evaluar el proyecto sin el terreno propio (arrendando uno)

el estudio de 18 000 ya pagado NO justifica continuar: es costo hundido
```

**Interpreta:** el proyecto se rechaza y el hallazgo más valioso es **el costo de oportunidad del
terreno**, que representa el 30 % de la inversión y que no aparecía en ninguna planilla contable. Un
análisis que lo omitiera habría concluido que el proyecto es marginalmente negativo en lugar de
claramente negativo, y la recomendación habría sido distinta.

## 🏦 Del cliente al banco

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| VAN | Evaluación de proyectos del cliente y del banco | 13, clase 4 |
| Flujo incremental | Base del análisis de viabilidad de un crédito | 13, clase 4 |
| Costo de oportunidad | Valoración de garantías y de recursos propios | 9, clase 8 |
| Sensibilidad | Requisito del comité de crédito | 13, clase 13 |
| Índice de rentabilidad | Asignación de capital con restricción | 15, clase 11 |

## 🧪 Práctica

En `labs/lab-04.md`, sección de VAN:

1. Clasifica veinte conceptos en relevantes e irrelevantes para el flujo incremental.
2. Construye el flujo de caja libre completo de un proyecto con impuestos y capital de trabajo.
3. Calcula el VAN y la tabla de sensibilidad a cinco variables.
4. Compara dos proyectos de distinta escala y dos de distinta duración con los métodos correctos.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se incluyen los intereses en el flujo | Doble conteo | El financiamiento está en la tasa. |
| Se incluye un costo hundido | Concepto no aplicado | Solo flujos futuros e incrementales. |
| Se omite el capital de trabajo | Flujo incompleto | Inclúyelo como salida y recupéralo al final. |
| Se ignora el costo de oportunidad de recursos propios | Salida implícita omitida | Valora a precio de mercado. |
| Se comparan proyectos de distinta duración por VAN | Bases distintas | Usa VAN anualizado. |
| Se presenta un VAN puntual | Falsa precisión | Presenta rango y umbrales. |

## ❓ Preguntas de comprobación

1. ¿Por qué no se incluyen los intereses en el flujo de un proyecto?
2. ¿Cómo se trata la depreciación en el flujo de caja libre?
3. Un terreno propio se usará en el proyecto. ¿Se incluye y por qué?
4. ¿Cómo comparas dos proyectos de 4 y 9 años?
5. ¿Qué debe acompañar siempre a un VAN en una presentación?

## 📥 Entregable

Guarda en `portfolio/parte-07/clase-08/`:

- la clasificación de veinte conceptos en relevantes e irrelevantes;
- el flujo de caja libre completo de un proyecto con todos sus componentes;
- el VAN con la tabla de sensibilidad a cinco variables y sus umbrales;
- la comparación de proyectos de distinta escala y duración con el método justificado.

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

- Brealey, R., Myers, S. y Allen, F. (2023). *Principios de finanzas corporativas* (14.ª ed.). McGraw-Hill. Capítulos 5 y 6: criterios de inversión y flujos relevantes.
- Ross, S., Westerfield, R. y Jaffe, J. (2021). *Corporate Finance* (12.ª ed.). McGraw-Hill. Capítulos 6 y 7: VAN y análisis de proyectos.
- Damodaran, A. (2012). *Investment Valuation* (3.ª ed.). Wiley. Capítulo 5: reglas de decisión de inversión.
- Blank, L. y Tarquin, A. (2018). *Ingeniería económica* (8.ª ed.). McGraw-Hill. Capítulos 5 y 6: VAN y comparación de alternativas.
- Koller, T., Goedhart, M. y Wessels, D. (2020). *Valuation* (7.ª ed.). McKinsey/Wiley. Definición del flujo de caja libre.
- Verificación local: usa la tasa de impuesto a la renta vigente en tu país y las reglas de depreciación tributaria aplicables al calcular el escudo fiscal.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 07 · Sistemas de amortización](07-sistemas-de-amortizacion.md) | [Parte 07](../README.md) · [Programa](../../../SYLLABUS.md) | [09 · Tasa interna de retorno →](09-tasa-interna-de-retorno.md) |
<!-- gen:footer:end -->
