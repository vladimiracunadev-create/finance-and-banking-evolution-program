---
part: 7
class: 6
title: "Perpetuidades"
level: avanzado
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 06 · Perpetuidades

> [← 05 · Anualidades anticipadas](05-anualidades-anticipadas.md) · [Índice de la parte](../README.md) · [07 · Sistemas de amortización →](07-sistemas-de-amortizacion.md)

**Parte 07 — Matemática financiera avanzada** · **Nivel:** Avanzado — perfil analista · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Valorar flujos sin fecha de término, que es la base de la valoración de empresas, de acciones y de
rentas vitalicias. La perpetuidad parece un artificio teórico y es la herramienta que sostiene el
valor terminal de casi toda valoración por flujos descontados: entre el 60 % y el 80 % del valor de
una empresa suele estar en ese término.

Las anualidades anteriores tienen un número finito de pagos. Esta clase trata el caso en que no lo tienen, que parece teórico y es la pieza que sostiene la mitad del valor de cualquier valoración de empresa: el valor terminal se calcula como una perpetuidad.

## 📚 Objetivos

Al finalizar podrás:

1. **Derivar** y aplicar la fórmula de la perpetuidad simple y creciente.
2. **Explicar** por qué un flujo infinito tiene valor finito.
3. **Calcular** valores terminales en modelos de valoración.
4. **Medir** la sensibilidad del valor a la tasa de crecimiento supuesta.
5. **Reconocer** los límites y los errores típicos de su aplicación.

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

Los dos primeros términos son la perpetuidad y su versión creciente; los cuatro siguientes, su aplicación y sus límites. La **condición de convergencia** es la que hay que comprobar siempre: si el crecimiento supuesto iguala o supera a la tasa de descuento, la fórmula no tiene sentido económico y aun así devuelve un número.

| Concepto | Comprensión verificable |
|---|---|
| `perpetuidad` | Serie infinita de pagos iguales. `VP = A / i`. |
| `perpetuidad creciente` | Los pagos crecen a tasa `g` constante. `VP = A / (i − g)`, válida solo si `g < i`. |
| `valor terminal` | Valor de todos los flujos posteriores al horizonte explícito de proyección. |
| `condición de convergencia` | `g < i`. Si no se cumple, el valor es infinito y el modelo carece de sentido. |
| `sensibilidad al crecimiento` | Pequeños cambios en `g` producen grandes cambios en el valor. |
| `modelo de Gordon` | Aplicación de la perpetuidad creciente a la valoración de acciones por dividendos. |

## 🧠 Modelo mental

Un flujo infinito tiene valor finito porque **el descuento vence al infinito**:

```text
1 000 000 al año, descontado al 10 %

  año 1    909 091
  año 10   385 543
  año 50     8 519
  año 100       73
  año 200        0,006
  ...
  SUMA = 10 000 000 = 1 000 000 / 0,10
```

A partir del año 70, cada flujo aporta menos del 0,1 % del valor. **La perpetuidad no valora el
infinito: valora los primeros 60 a 80 años y el resto es ruido.**

## 📖 Desarrollo

### 1. Derivación

Partiendo de la anualidad vencida y haciendo `n → ∞`:

```text
VP = A × [1 − (1+i)^-n] / i

cuando n → ∞, (1+i)^-n → 0

VP = A / i
```

Para la perpetuidad creciente:

```text
VP = A / (i − g)      con g < i

donde A es el flujo del PRIMER periodo (no el actual)
```

La condición `g < i` no es un tecnicismo: si el flujo crece más rápido de lo que se descuenta, la
suma diverge. Un modelo con `g ≥ i` está mal planteado, no describe una empresa infinitamente valiosa.

### 2. Aplicaciones

Las perpetuidades aparecen en instrumentos concretos y en valoraciones. La tabla recoge los casos.

| Aplicación | Fórmula | Comentario |
|---|---|---|
| Bono perpetuo | `VP = cupón / i` | Existen emisiones reales de este tipo |
| Renta vitalicia (aproximación) | `VP = renta / i` | Sobrestima: la vida es finita |
| Valor terminal en valoración | `VT = FCF_{n+1} / (WACC − g)` | El uso más frecuente |
| Modelo de Gordon (acciones) | `P = D₁ / (k − g)` | Valoración por dividendos |
| Capitalización de rentas inmobiliarias | `V = NOI / tasa de capitalización` | Estándar en tasación |

### 3. Valor terminal en una valoración

El valor terminal suele ser la mayor parte del valor de una empresa, y sale de una perpetuidad creciente. El procedimiento siguiente lo calcula.

```text
estructura típica de una valoración por flujos descontados:

  VP = Σ(t=1 a n) FCF_t/(1+WACC)^t  +  VT/(1+WACC)^n

  VT = FCF_{n+1}/(WACC − g)
```

Ejemplo con horizonte explícito de 5 años:

```text
FCF proyectados (millones): 820, 890, 950, 1 010, 1 070
WACC = 10,5 % · g perpetuo = 2,5 %

FCF_6 = 1 070 × 1,025 = 1 096,75
VT = 1 096,75 / (0,105 − 0,025) = 1 096,75/0,08 = 13 709,4

VP de los flujos explícitos:
  820/1,105 + 890/1,105² + 950/1,105³ + 1 010/1,105⁴ + 1 070/1,105⁵
  = 742,1 + 728,8 + 704,0 + 677,3 + 649,1 = 3 501,3

VP del valor terminal = 13 709,4 / 1,105⁵ = 13 709,4/1,64745 = 8 321,4

VALOR TOTAL = 3 501,3 + 8 321,4 = 11 822,7
```

```text
proporción del valor terminal = 8 321,4 / 11 822,7 = 70,4 %
```

**El 70 % del valor proviene de dos supuestos: `g = 2,5 %` y `WACC = 10,5 %`.** Los cinco años de
proyección detallada explican el 30 % restante. Esta desproporción es característica y hay que
declararla siempre.

### 4. Sensibilidad al crecimiento

Con `WACC = 10,5 %` y `FCF_6 = 1 096,75`:

| g | VT | VP del VT | Valor total | Variación |
|---:|---:|---:|---:|---:|
| 1,0 % | 11 544 | 7 007 | 10 508 | −11,1 % |
| 1,5 % | 12 186 | 7 397 | 10 898 | −7,8 % |
| 2,0 % | 12 903 | 7 832 | 11 333 | −4,1 % |
| **2,5 %** | **13 709** | **8 321** | **11 823** | **—** |
| 3,0 % | 14 623 | 8 876 | 12 378 | +4,7 % |
| 3,5 % | 15 668 | 9 510 | 13 011 | +10,1 % |
| 4,0 % | 16 874 | 10 242 | 13 744 | +16,3 % |

**Un punto porcentual en `g` mueve el valor un 20 %.** Y `g` es un supuesto sobre el crecimiento
perpetuo de una empresa, que nadie puede conocer.

Restricción de sensatez ampliamente aceptada:

```text
g perpetuo ≤ crecimiento nominal de largo plazo de la economía
```

Ninguna empresa puede crecer perpetuamente más que la economía, porque en el límite sería toda la
economía. Un `g` de 5 % en una economía que crece 4 % nominal es indefendible.

### 5. Límites y errores

La fórmula es extremadamente sensible a dos supuestos, y por eso se presenta siempre con su rango. La tabla recoge los errores habituales.

| Error | Consecuencia | Corrección |
|---|---|---|
| Usar `g ≥ i` | Valor infinito o negativo | Verifica la condición de convergencia |
| Usar `g` superior al crecimiento de la economía | Sobrevaloración severa | Limita `g` al crecimiento nominal de largo plazo |
| Usar el flujo del año `n` en lugar del `n+1` | Subestima el valor terminal | `VT = FCF_{n+1}/(i − g)` |
| Aplicar perpetuidad a un negocio con vida finita | Sobrevaloración | Usa valor de liquidación o anualidad finita |
| No declarar la proporción del valor terminal | Falta de transparencia | Reporta siempre qué % del valor proviene del VT |
| Usar el mismo `g` para el flujo y para la inversión | Inconsistencia | Un crecimiento perpetuo exige reinversión perpetua |

El último punto es sutil y frecuente: si la empresa crece 2,5 % para siempre, necesita invertir para
sostener ese crecimiento, y esa inversión debe estar descontada del flujo. Un modelo que proyecta
crecimiento sin inversión asociada sobrestima el valor.

## 🧮 Ejemplo guiado

**Situación.** Valora una empresa de servicios y evalúa la robustez del resultado.

```text
FCF del último año cerrado         1 400 millones
proyección explícita               5 años, crecimiento decreciente: 8 %, 7 %, 6 %, 5 %, 4 %
WACC                               11,2 %
g perpetuo propuesto por la gerencia 4,0 %
crecimiento nominal de la economía   4,5 % (2,0 % real + 2,5 % inflación)
deuda financiera neta              3 200 millones
```

**Paso 1 — proyecta los flujos explícitos.**

| Año | Crecimiento | FCF | Factor (11,2 %) | VP |
|---:|---:|---:|---:|---:|
| 1 | 8 % | 1 512,0 | 0,899281 | 1 359,7 |
| 2 | 7 % | 1 617,8 | 0,808706 | 1 308,3 |
| 3 | 6 % | 1 714,9 | 0,727254 | 1 247,1 |
| 4 | 5 % | 1 800,6 | 0,654006 | 1 177,6 |
| 5 | 4 % | 1 872,6 | 0,588135 | 1 101,4 |
| | | | **VP explícito** | **6 194,1** |

**Paso 2 — valor terminal con el `g` de la gerencia.**

```text
FCF_6 = 1 872,6 × 1,04 = 1 947,5
VT = 1 947,5/(0,112 − 0,040) = 1 947,5/0,072 = 27 048,6
VP del VT = 27 048,6 × 0,588135 = 15 908,0

VALOR DE LA FIRMA = 6 194,1 + 15 908,0 = 22 102,1
VALOR DEL PATRIMONIO = 22 102,1 − 3 200 = 18 902,1
proporción del VT = 15 908,0/22 102,1 = 72,0 %
```

**Paso 3 — cuestiona el supuesto de `g`.**

```text
g propuesto: 4,0 %
crecimiento nominal de la economía: 4,5 %

la empresa crecería perpetuamente casi al ritmo de toda la economía
→ implica que su participación en la economía NUNCA disminuye
→ defendible solo para una empresa con posición estructuralmente dominante
```

**Paso 4 — valora con supuestos alternativos.**

| g | VT | VP del VT | Valor firma | Valor patrimonio | Variación |
|---:|---:|---:|---:|---:|---:|
| 2,0 % | 20 730 | 12 192 | 18 386 | 15 186 | −19,7 % |
| 2,5 % | 22 059 | 12 974 | 19 168 | 15 968 | −15,5 % |
| 3,0 % | 23 573 | 13 864 | 20 058 | 16 858 | −10,8 % |
| 3,5 % | 25 315 | 14 889 | 21 083 | 17 883 | −5,4 % |
| **4,0 %** | **27 049** | **15 908** | **22 102** | **18 902** | **—** |

**Paso 5 — verifica la consistencia entre crecimiento e inversión.**

```text
para crecer 4 % perpetuamente con un retorno sobre el capital invertido del 15 %:
  tasa de reinversión = g / ROIC = 0,04/0,15 = 26,7 %

¿el FCF proyectado ya descuenta una reinversión del 26,7 % del resultado operativo?
  si NO → el flujo está sobrestimado y el valor también
```

Esta verificación —la relación `g = tasa de reinversión × ROIC`— es la que detecta el error más común
en valoraciones: proyectar crecimiento sin la inversión que lo hace posible.

**Paso 6 — presentación honesta del resultado.**

```text
VALOR DEL PATRIMONIO: rango de 15 200 a 18 900 millones

caso base recomendado (g = 2,5 %, consistente con crecimiento
poblacional y de productividad de largo plazo): 15 968 millones

el 72 % del valor proviene del valor terminal
el supuesto crítico es g: cada 0,5 puntos mueve el valor un 5 %
el supuesto de la gerencia (g = 4,0 %) requiere que la empresa
mantenga su participación en la economía indefinidamente
```

**Interpreta:** presentar "la empresa vale 18 902 millones" habría sido una afirmación de precisión
falsa sobre un número que depende en un 72 % de un supuesto sobre el año 2100. **La presentación
correcta es un rango con el supuesto crítico identificado**, y esa diferencia de forma es lo que
distingue una valoración profesional de un ejercicio de planilla.

## 🏦 Del cliente al banco

El cliente ve un valor de empresa y el banco comprueba de qué supuestos depende. La tabla enfrenta las dos lecturas.

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| Valor terminal | Valoración de empresas en banca de inversión | 13, clase 7 |
| Modelo de Gordon | Valoración de acciones | 8, clase 11 |
| Capitalización de rentas | Tasación de inmuebles en garantía | 9, clase 8 |
| Sensibilidad a `g` | Rango de valoración, no punto único | 13, clase 7 |
| Consistencia crecimiento-inversión | Control de calidad del modelo | 13, clase 7 |

## 🧪 Práctica

El laboratorio pide calcular un valor terminal y su sensibilidad al crecimiento supuesto. La dispersión resultante es la razón por la que estas cifras se presentan como rangos.

En `labs/lab-03.md`, sección de perpetuidades:

1. Demuestra numéricamente por qué un flujo infinito tiene valor finito.
2. Calcula el valor terminal de una valoración con cinco supuestos de `g`.
3. Determina la proporción del valor que proviene del valor terminal.
4. Verifica la consistencia entre `g`, la tasa de reinversión y el retorno sobre el capital.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen valoraciones desproporcionadas. La causa está casi siempre en un crecimiento perpetuo demasiado cerca de la tasa de descuento.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| El valor terminal es enorme o negativo | `g ≥ i` | Verifica la condición de convergencia. |
| Se usa `g` mayor que el crecimiento de la economía | Supuesto indefendible | Limita `g` al crecimiento nominal de largo plazo. |
| Se usa `FCF_n` en la fórmula | Flujo equivocado | Usa `FCF_{n+1}`. |
| No se declara la proporción del VT | Falta de transparencia | Repórtala siempre. |
| Se proyecta crecimiento sin inversión | Inconsistencia | `g = reinversión × ROIC`. |
| Se entrega un valor puntual | Falsa precisión | Presenta un rango con el supuesto crítico. |

## ❓ Preguntas de comprobación

1. ¿Por qué un flujo infinito tiene valor finito?
2. ¿Qué condición debe cumplir `g` y qué ocurre si no se cumple?
3. Calcula el valor terminal con `FCF_{n+1}` de 500, `WACC` 9 % y `g` 2 %.
4. ¿Por qué `g` no puede superar el crecimiento de largo plazo de la economía?
5. ¿Cómo verificas que el crecimiento supuesto es consistente con la inversión proyectada?

## 📥 Entregable

Guarda en `portfolio/parte-07/clase-06/`:

- la demostración numérica de la convergencia de la perpetuidad;
- el valor terminal calculado con cinco supuestos de `g` y su efecto en el valor;
- la proporción del valor proveniente del valor terminal;
- la verificación de consistencia entre crecimiento, reinversión y retorno sobre el capital.

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

- Damodaran, A. (2012). *Investment Valuation* (3.ª ed.). Wiley. Capítulo 12: valor terminal, restricciones al crecimiento perpetuo y consistencia.
- Koller, T., Goedhart, M. y Wessels, D. (2020). *Valuation: Measuring and Managing the Value of Companies* (7.ª ed.). McKinsey/Wiley. Capítulo 12: valor de continuación.
- Gordon, M. (1959). "Dividends, Earnings and Stock Prices". *Review of Economics and Statistics*. Formulación del modelo de crecimiento constante.
- Brealey, R., Myers, S. y Allen, F. (2023). *Principios de finanzas corporativas* (14.ª ed.). McGraw-Hill. Capítulos 2 y 4: perpetuidades y valoración de acciones.
- Kellison, S. (2008). *The Theory of Interest* (3.ª ed.). McGraw-Hill/Irwin. Capítulo 3: perpetuidades.
- Verificación local: usa el crecimiento nominal de largo plazo proyectado por el banco central de tu país como techo del `g` perpetuo.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 05 · Anualidades anticipadas](05-anualidades-anticipadas.md) | [Parte 07](../README.md) · [Programa](../../../SYLLABUS.md) | [07 · Sistemas de amortización →](07-sistemas-de-amortizacion.md) |
<!-- gen:footer:end -->
