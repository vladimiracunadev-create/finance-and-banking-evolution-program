<!-- meta
part: 1
class: 10
title: "Valor futuro"
level: fundamento
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 10 · Valor futuro

> [← 09 · Valor presente](09-valor-presente.md) · [Índice de la parte](../README.md) · [11 · Cuotas y cronogramas de pago →](11-cuotas-y-cronogramas-de-pago.md)

**Parte 01 — Matemática financiera básica** · **Nivel:** Fundamento — sin conocimientos previos · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Aprender a proyectar hacia adelante: cuánto tendré, cuánto necesito aportar y cuánto tiempo me falta.
El valor futuro es la operación inversa de la clase 9 y la herramienta con la que se planifica todo
objetivo de ahorro. Aquí también aparece el hallazgo que más cambia conductas: en un plan de ahorro
largo, **el aporte importa menos que el momento en que empiezas**.

La clase anterior trajo flujos al presente. Esta hace el movimiento inverso, y sirve para responder la pregunta con la que llega casi todo el mundo a las finanzas personales: cuánto tendré, y cuánto tengo que aportar para llegar a una meta. Es la misma mecánica de la clase 8 aplicada a series de aportes en vez de a flujos sueltos.

## 📚 Objetivos

Al finalizar podrás:

1. **Calcular** el valor futuro de un capital único y de aportes periódicos.
2. **Determinar** el aporte mensual necesario para alcanzar una meta con fecha.
3. **Cuantificar** el costo de postergar el inicio de un plan de ahorro.
4. **Separar** el aporte propio del rendimiento acumulado en cualquier proyección.
5. **Expresar** una meta en valor futuro ajustando por inflación (clase 7).

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

Las tres primeras entradas son la mecánica y las tres últimas son lo que la mecánica revela. El **costo de postergar** es el concepto que da sentido a toda la clase: no es una advertencia moral sobre el ahorro, es una cifra que se calcula y que casi siempre sorprende por su tamaño.

| Concepto | Comprensión verificable |
|---|---|
| `valor futuro (VF)` | `VF = P(1+i)^n`. Lo que un capital llega a valer si se deja capitalizar. |
| `serie de aportes` | `VF = A · [((1+i)^n − 1)/i]`. Aportes iguales al **final** de cada periodo. |
| `factor de acumulación` | `[((1+i)^n − 1)/i]`. Cuántas veces el aporte periódico cabe en el resultado final. |
| `aporte necesario` | `A = VF · i / ((1+i)^n − 1)`. El despeje que convierte una meta en una cuota de ahorro. |
| `costo de postergar` | Pérdida por empezar tarde. Crece de forma no lineal: los primeros años son los que más pesan. |
| `composición del resultado` | Todo VF se descompone en `aportes` + `rendimiento`. Mostrar ambas cifras es una exigencia de honestidad. |

## 🧠 Modelo mental

Un plan de ahorro tiene **dos motores**: lo que pones y lo que el tiempo pone por ti.

```text
aportando 100 000 mensuales al 0,6 % mensual
  a 5 años    aportado 6 000 000   ganado  1 013 000   → 14 % del total
  a 15 años   aportado 18 000 000  ganado 12 400 000   → 41 % del total
  a 30 años   aportado 36 000 000  ganado 65 600 000   → 65 % del total
```

En horizontes cortos manda el aporte; en horizontes largos manda el tiempo. Esa transición explica
por qué la previsión (Parte 2, clase 12) se decide a los 25 años y no a los 55.

## 📖 Desarrollo

### 1. Capital único

Se empieza por el caso más simple, un solo capital que se deja crecer. Es la misma fórmula del interés compuesto de la clase 6, leída ahora desde la pregunta de la meta.

```text
VF = P (1 + i)^n
```

Ocho millones al 6,5 % anual durante 12 años:

```text
VF = 8 000 000 × (1,065)^12 = 8 000 000 × 2,129096 = 17 032 768
```

De los cuales 8 000 000 son aporte y 9 032 768 rendimiento: el dinero más que se duplicó sin agregar
nada. Control con la regla del 72: `72/6,5 = 11,1 años` para duplicar; a 12 años debe estar algo por
encima del doble. ✔

### 2. Serie de aportes iguales

Cuando en vez de un capital hay un aporte que se repite, cada aporte capitaliza durante un plazo distinto. La fórmula siguiente resume esa suma, y conviene ver de dónde sale antes de usarla.

```text
VF = A · [((1+i)^n − 1) / i]
```

Aportando 150 000 mensuales al 0,5 % mensual durante 10 años (120 meses):

```text
(1,005)^120 = 1,819397
VF = 150 000 × (1,819397 − 1)/0,005 = 150 000 × 163,8793 = 24 581 895

aportado    150 000 × 120 = 18 000 000
rendimiento              =  6 581 895   (26,8 % del total)
```

Nota crítica: la fórmula asume aportes al **final** de cada periodo. Si se aportan al inicio
(modalidad anticipada), el resultado se multiplica por `(1+i)`:

```text
24 581 895 × 1,005 = 24 704 804    → 122 909 más, solo por aportar el día 1 y no el día 30
```

### 3. Aporte necesario para una meta

Despejando la misma expresión se obtiene la pregunta que de verdad interesa: cuánto hay que aportar cada periodo para llegar a una cifra concreta.

```text
A = VF · i / ((1+i)^n − 1)
```

Meta: 30 000 000 en 8 años (96 meses), al 0,55 % mensual.

```text
(1,0055)^96 = 1,694356
A = 30 000 000 × 0,0055 / 0,694356 = 165 000 / 0,694356 = 237 631
```

Se necesitan **237 631 pesos mensuales**. De los 30 millones, 22 812 576 serán aporte propio y
7 187 424 rendimiento.

### 4. El costo de postergar

Dos personas quieren tener un fondo a los 65 años, con rendimiento de 0,55 % mensual (6,8 % anual):

| Persona | Empieza | Años | Aporte mensual | Total aportado | Fondo final |
|---|---:|---:|---:|---:|---:|
| Ana | 25 | 40 | 100 000 | 48 000 000 | 219 200 000 |
| Beto | 35 | 30 | 100 000 | 36 000 000 | 106 300 000 |
| Carla | 45 | 20 | 100 000 | 24 000 000 | 46 400 000 |

Ana aporta un 33 % más que Beto y termina con **106 % más**. Los diez años iniciales de Ana —los que
parecen menos importantes porque los montos son pequeños— son los que más capitalizan. Dicho de otro
modo: para igualar a Ana empezando a los 35, Beto necesitaría aportar **206 000 mensuales**, más del
doble.

### 5. Meta en términos reales

Combinando con la clase 7: si la meta es comprar algo que hoy cuesta `X` y la inflación es `π`, la
meta nominal debe ser `X(1+π)^n`, y conviene además calcular el aporte con la **tasa real**.

```text
meta hoy 30 000 000, inflación 4 %, plazo 8 años
meta nominal = 30 000 000 × 1,04^8 = 41 057 000
```

Con la tasa nominal de 6,8 % anual (0,55 % mensual), el aporte para 41 057 000 es **325 200**
mensuales, no 237 631. Ignorar la inflación subestima el aporte necesario en un **37 %**.

## 🧮 Ejemplo guiado

**Situación.** Marcos, 32 años, quiere reunir el pie de una vivienda que hoy cuesta 40 000 000. Puede
ahorrar 380 000 mensuales, obtiene 0,50 % mensual y estima inflación de 4,2 % anual. ¿En cuántos años
llega, y qué pasa si demora un año en empezar?

**Paso 1 — plantea la ecuación con meta móvil.** La meta crece mientras él ahorra:

```text
meta(n) = 40 000 000 × (1,042)^(n/12)      n en meses
fondo(n) = 380 000 × [((1,005)^n − 1)/0,005]
```

**Paso 2 — tantea.**

| Meses | Fondo acumulado | Meta ajustada | ¿Alcanza? |
|---:|---:|---:|---|
| 84 | 38 129 000 | 52 040 000 | No |
| 108 | 51 220 000 | 55 460 000 | No |
| 120 | 58 260 000 | 57 260 000 | **Sí** |
| 118 | 57 060 000 | 56 970 000 | Sí (justo) |

**Paso 3 — resultado.** Marcos llega en aproximadamente **118 meses (9 años y 10 meses)**, a los 41
años. En ese punto habrá aportado 44 840 000 y ganado 12 220 000 de rendimiento.

**Paso 4 — el efecto de demorar un año.** Si empieza 12 meses después con los mismos 380 000:

```text
alcanza en ≈ 122 meses de ahorro, es decir 134 meses desde hoy → 11 años y 2 meses
retraso efectivo: 16 meses de retraso por 12 meses de demora
```

Demorar un año cuesta **un año y cuatro meses**. La razón es la meta móvil: mientras no ahorra, el
objetivo sigue subiendo con la inflación.

**Paso 5 — alternativa.** Para llegar en 84 meses (7 años) necesitaría:

```text
A = 52 040 000 × 0,005 / ((1,005)^84 − 1) = 260 200 / 0,520370 = 500 029 mensuales
```

**Paso 6 — interpreta con límites.** El modelo supone rendimiento constante, inflación constante y
aporte sin interrupciones. Ninguna de las tres se cumple en la vida real. El uso correcto de este
cálculo no es predecir la fecha exacta, sino **dimensionar el esfuerzo** y detectar que 380 000
mensuales implican casi diez años. Esa conversación es la que abre el plan financiero anual de la
Parte 2, clase 14.

## 🏦 Del cliente al banco

El cliente pregunta cuánto tendré y el banco calcula cuánto capta y a qué costo. La tabla enfrenta las dos lecturas de las mismas operaciones de ahorro.

| Uso personal | Equivalente profesional | Dónde aparece |
|---|---|---|
| Cuánto tendré en mi cuenta de ahorro | Proyección de captaciones de un producto | Parte 10, clase 2 |
| Aporte mensual para una meta | Cálculo de prima de un seguro dotal | Parte 3, clase 12 |
| Fondo de pensiones acumulado | Proyección actuarial de la cuenta individual | Parte 2, clase 12 |
| "Empezar temprano rinde más" | Argumento central del ahorro previsional | Parte 2, clase 12 |

## 🧪 Práctica

El laboratorio pide calcular el aporte necesario para una misma meta empezando en momentos distintos. La brecha entre empezar hoy y empezar en cinco años es el resultado que hace innecesario cualquier discurso sobre la importancia de ahorrar temprano.

En `labs/lab-05.md`, sección de acumulación:

1. Proyecta un capital único a 5, 10, 20 y 30 años separando aporte y rendimiento.
2. Calcula el aporte mensual necesario para tres metas propias con fecha.
3. Reproduce la tabla Ana/Beto/Carla con tus propios números y calcula el aporte de equiparación.
4. Ajusta una meta por inflación y cuantifica el error de no hacerlo.

## ⚠️ Errores frecuentes

Los síntomas de la tabla vienen casi siempre de mezclar la periodicidad del aporte con la de la tasa, o de olvidar que la meta está expresada en pesos de hoy y se alcanzará en pesos de mañana.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| El fondo proyectado no alcanza la meta | La meta no se ajustó por inflación | `meta futura = meta hoy × (1+π)^n`. |
| Se multiplicó el aporte por el número de periodos | Se ignoró la capitalización | Usa el factor `((1+i)^n − 1)/i`. |
| Diferencia inexplicada de un periodo de intereses | Confusión entre aportes vencidos y anticipados | Aportes al inicio: multiplica el resultado por `(1+i)`. |
| Se presenta solo el monto final | No se separó aporte de rendimiento | Muestra siempre ambas cifras; cambia la percepción del plan. |
| "Empiezo el próximo año, da lo mismo" | No se calculó el costo de postergar | Cuantifica: normalmente el retraso efectivo supera al demorado. |
| El plan supone 30 años sin interrupciones | Escenario único | Modela un escenario con dos años de aportes suspendidos. |

## ❓ Preguntas de comprobación

1. ¿Cuál es el valor futuro de 5 000 000 al 7 % durante 15 años, y qué parte es rendimiento?
2. ¿Cuánto hay que aportar mensualmente para reunir 20 000 000 en 6 años al 0,5 % mensual?
3. ¿Por qué demorar un año en empezar puede costar más de un año de retraso?
4. ¿Qué diferencia produce aportar al inicio en lugar del final de cada mes?
5. ¿Por qué es engañoso presentar un plan de ahorro mostrando solo el monto final?

## 📥 Entregable

Guarda en `portfolio/parte-01/clase-10/`:

- la proyección de capital único con la descomposición aporte/rendimiento;
- el cálculo del aporte necesario para tres metas propias;
- la tabla del costo de postergar con el aporte de equiparación;
- una meta ajustada por inflación con la comparación contra la versión sin ajustar.

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

- Ross, S., Westerfield, R. y Jordan, B. (2022). *Fundamentos de finanzas corporativas* (12.ª ed.). McGraw-Hill. Capítulo 5: valor futuro de series uniformes.
- Kellison, S. (2008). *The Theory of Interest* (3.ª ed.). McGraw-Hill/Irwin. Capítulo 3: anualidades vencidas y anticipadas.
- Bodie, Z., Kane, A. y Marcus, A. (2023). *Investments* (13.ª ed.). McGraw-Hill. Capítulo 5: horizonte de inversión y acumulación.
- OECD (2022). *OECD Pensions Outlook*. OCDE. Evidencia sobre el efecto de la edad de inicio del ahorro previsional.
- Benartzi, S. y Thaler, R. (2004). "Save More Tomorrow". *Journal of Political Economy*, 112(S1). Diseño de planes de ahorro y efecto de la postergación.
- Verificación local: usa la rentabilidad histórica publicada por el administrador de fondos previsionales o el supervisor de tu país, y declara el periodo del dato.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 09 · Valor presente](09-valor-presente.md) | [Parte 01](../README.md) · [Programa](../../../SYLLABUS.md) | [11 · Cuotas y cronogramas de pago →](11-cuotas-y-cronogramas-de-pago.md) |
<!-- gen:footer:end -->
