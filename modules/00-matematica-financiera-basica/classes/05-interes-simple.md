<!-- meta
part: 1
class: 5
title: "Interés simple"
level: fundamento
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 05 · Interés simple

> [← 04 · Variaciones porcentuales e índices](04-variaciones-porcentuales-e-indices.md) · [Índice de la parte](../README.md) · [06 · Interés compuesto →](06-interes-compuesto.md)

**Parte 01 — Matemática financiera básica** · **Nivel:** Fundamento — sin conocimientos previos · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Instalar la primera fórmula financiera real y, con ella, la idea de que **el dinero tiene precio y ese
precio depende del tiempo**. El interés simple es raro en el crédito de consumo y frecuente en
operaciones de corto plazo, mora, papeles comerciales y descuento de documentos. Aprenderlo bien
importa menos por su uso directo que porque establece la base de comparación contra la cual el
interés compuesto de la clase 6 se vuelve comprensible.

Hasta aquí el programa ha trabajado con cantidades y con cambios entre periodos, pero sin poner precio al tiempo. Esta clase pone ese precio por primera vez, y con él aparece la idea que sostiene todo lo demás: el dinero cuesta, y cuesta en proporción al tiempo que se retiene. Conviene entrar sabiendo que el interés simple es la excepción y no la regla en el crédito; se estudia primero porque es la línea recta contra la cual se mide la curva.

## 📚 Objetivos

Al finalizar podrás:

1. **Aplicar** `I = C · i · n` cuidando que `i` y `n` compartan la misma unidad temporal.
2. **Distinguir** la convención de días comerciales (360) de la exacta (365) y cuantificar el efecto.
3. **Calcular** cualquiera de las cuatro variables despejando la fórmula.
4. **Explicar** por qué el interés simple no capitaliza y qué significa eso para el prestamista.
5. **Identificar** en qué operaciones reales se usa efectivamente interés simple.

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

Las cinco primeras entradas son las variables de una sola fórmula y sus relaciones; las dos últimas son convenciones de contrato que no aparecen en ninguna fórmula y deciden cuánto se cobra de verdad. El **plazo** es donde ocurre el ochenta por ciento de los errores de esta clase, porque exige compartir unidad con la tasa y nadie lo comprueba.

| Concepto | Comprensión verificable |
|---|---|
| `capital (C)` | Monto sobre el que se calcula el interés. En interés simple **nunca cambia**: siempre es el capital inicial. |
| `tasa (i)` | Precio del dinero por unidad de tiempo, expresado en decimal. `18 % anual` es `i = 0,18` con `n` en años. |
| `plazo (n)` | Tiempo en la **misma unidad** que la tasa. Este es el punto donde ocurre el 80 % de los errores. |
| `interés (I)` | `I = C · i · n`. Crece de forma lineal con el tiempo. |
| `monto o valor futuro (M)` | `M = C · (1 + i · n)`. El capital más el interés acumulado. |
| `convención de días` | `360` (comercial u ordinaria) o `365` (exacta). No es un detalle: cambia el interés cobrado en operaciones de días. |
| `interés bancario vs. racional` | Base 360 con días reales (bancario) frente a base 365 con días reales (racional). El bancario siempre cobra más. |

## 🧠 Modelo mental

En interés simple, el dinero gana **la misma cantidad cada periodo**, porque siempre se calcula sobre
el capital original:

```text
capital 1 000 000, 2 % mensual
  mes 1   +20 000    saldo 1 020 000
  mes 2   +20 000    saldo 1 040 000
  mes 3   +20 000    saldo 1 060 000   ← el interés NUNCA se suma a la base
```

Es una recta. El interés compuesto de la clase 6 es una curva. Toda la diferencia entre ahorrar e
invertir bien o mal cabe en esa frase.

## 📖 Desarrollo

### 1. La fórmula y sus cuatro despejes

La fórmula del interés simple tiene cuatro variables, y en la práctica se conoce cualquier combinación de tres. Por eso no se aprende una fórmula sino cuatro despejes de la misma, que es lo que recoge el esquema siguiente.

```text
I = C · i · n            interés
M = C + I = C(1 + i·n)   monto

C = I / (i · n)          capital
i = I / (C · n)          tasa
n = I / (C · i)          plazo
```

La única regla no negociable: **`i` y `n` en la misma unidad temporal**.

```text
i = 18 % anual, plazo 8 meses
  ✗ n = 8          → I = C × 0,18 × 8    (ocho AÑOS)
  ✓ n = 8/12       → I = C × 0,18 × 0,667
  ✓ o bien i = 0,18/12 = 1,5 % mensual y n = 8
```

Ambos caminos correctos dan el mismo resultado. Elige uno y sé consistente.

### 2. La convención de días: 360 frente a 365

Para operaciones medidas en días, el denominador importa:

```text
I = C · i · (días / base)      base ∈ {360, 365}
```

Un capital de 10 000 000 al 12 % anual durante 45 días:

| Convención | Cálculo | Interés |
|---|---|---:|
| Comercial 360 | 10 000 000 × 0,12 × 45/360 | 150 000 |
| Exacta 365 | 10 000 000 × 0,12 × 45/365 | 147 945 |
| Diferencia | | **2 055** |

Un 1,39 % más de interés simplemente por elegir el denominador. Sobre una mesa de dinero que rota
miles de millones diarios, esa elección es una línea del contrato marco, no una convención inocente.
La base 360 nació de la comodidad de calcular a mano con meses de 30 días; sobrevive porque favorece
al prestamista.

### 3. Por qué el interés simple casi no existe en el crédito

Si un banco presta a interés simple durante 10 años al 10 %:

```text
simple      M = C(1 + 0,10 × 10) = 2,00 × C
compuesto   M = C(1,10)^10       = 2,59 × C
```

El prestamista pierde el rendimiento de los intereses que ya cobró. Por eso el interés simple
sobrevive donde el plazo es corto —y la diferencia, pequeña— o donde la ley lo impone:

| Uso real | Por qué simple |
|---|---|
| Descuento de facturas y letras | Plazos de 30 a 120 días |
| Pagarés y papel comercial de corto plazo | Convención de mercado monetario |
| Intereses de mora en muchas legislaciones | La norma prohíbe capitalizar la mora (anatocismo) |
| Depósitos a plazo de un solo periodo | No hay periodo intermedio que capitalizar |
| Cálculo de intereses devengados diarios | Se capitaliza recién al cierre del periodo |

### 4. Interés devengado: el uso profesional cotidiano

Un banco reconoce ingresos **cada día**, no cuando cobra. El devengo diario es interés simple:

```text
interés devengado del día = saldo · (tasa anual / base)
```

Sobre una colocación de 250 000 000 al 9,6 % anual, base 360:

```text
250 000 000 × 0,096 / 360 = 66 666,67 por día
```

Ese asiento diario es exactamente el que la Parte 5, clase 7, registra en el libro diario, y el que
la Parte 15, clase 3, agrega para formar el margen financiero.

## 🧮 Ejemplo guiado

El ejemplo siguiente se resuelve paso a paso y sin saltarse ninguno, incluidos los que parecen obvios. El paso que parece obvio es precisamente donde vive el error caro de esta clase.

**Situación.** Una pyme entrega a su banco una factura por 8 400 000 con vencimiento en 72 días. El
banco la descuenta a una tasa de 14,4 % anual, base 360, y cobra además una comisión fija de 35 000.
¿Cuánto recibe la pyme y cuál es su costo real anualizado?

**Paso 1 — interés del descuento.**

```text
I = 8 400 000 × 0,144 × 72/360 = 8 400 000 × 0,0288 = 241 920
```

**Paso 2 — monto recibido.**

```text
recibido = 8 400 000 − 241 920 − 35 000 = 8 123 080
```

**Paso 3 — costo efectivo del periodo.** Aquí está la trampa: el costo **no** se calcula sobre el
valor nominal de la factura, sino sobre lo que efectivamente se recibió.

```text
costo del periodo = (8 400 000 − 8 123 080) / 8 123 080 = 276 920 / 8 123 080 = 0,034090 → 3,4090 %
```

**Paso 4 — anualización simple.**

```text
tasa anual simple = 3,4090 % × 360/72 = 17,045 % anual
```

**Paso 5 — interpreta con honestidad.** La tasa publicada es 14,4 %; el costo real anualizado es
**17,05 %**, y eso sin capitalizar. Dos razones: la comisión y el hecho de que el interés se cobra
por adelantado sobre un monto mayor al recibido. Esta brecha entre tasa nominal y costo efectivo es
la razón de ser de la clase 13 de la Parte 3 y del concepto de carga anual equivalente.

**Verificación.** 3,41 % en 72 días son cinco periodos al año; `3,409 × 5 = 17,045`. ✔

## 🏦 Del cliente al banco

El cliente ve un recargo o un adelanto; el banco ve una colocación con su base de días. La tabla enfrenta las dos lecturas de cuatro operaciones cotidianas, y la última fila es la que más dinero mueve y la única que el cliente no ve.

| Operación | Vista del cliente | Vista del banco |
|---|---|---|
| Descuento de factura | "Me adelantan la plata" | Colocación de corto plazo con interés cobrado por anticipado |
| Interés de mora | "Me cobraron recargo" | Interés simple sobre saldo vencido, sin capitalizar por norma |
| Depósito a 30 días | "Gané un poco" | Captación con devengo diario y liquidación al vencimiento |
| Base 360 o 365 | Invisible | Cláusula contractual con impacto directo en el margen |

## 🧪 Práctica

El laboratorio pide calcular lo mismo cambiando solo la base de días. Es un ejercicio deliberadamente aburrido y su objetivo es que la brecha deje de ser una abstracción: al tabularla en pesos sobre cinco operaciones, la cláusula de la base pasa a ser algo que se negocia y no un detalle técnico.

En `labs/lab-03.md`:

1. Calcula el interés de cinco operaciones cambiando solo la base (360 y 365) y tabula la brecha.
2. Despeja las cuatro variables en cuatro casos distintos.
3. Reproduce el ejemplo del descuento de factura con tres plazos (30, 72 y 120 días).
4. Construye la tabla de devengo diario de una colocación durante un mes y verifica el total.

## ⚠️ Errores frecuentes

Los seis síntomas de la tabla se reconocen sin recalcular. Los tres primeros vienen de unidades y bases; los tres últimos, de aplicar interés simple donde no corresponde o de capitalizar donde la norma lo prohíbe, que es un problema legal antes que aritmético.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| El interés sale doce veces mayor de lo esperado | Tasa anual usada con plazo en meses | Lleva `i` y `n` a la misma unidad antes de multiplicar. |
| Dos bancos cotizan la misma tasa y cobran distinto | Bases de días diferentes (360 vs. 365) | Exige la base en la cotización y recalcula sobre una común. |
| El costo real no coincide con la tasa publicada | Interés cobrado por anticipado o comisiones | Calcula sobre el monto **recibido**, no sobre el nominal. |
| Se aplica interés simple a un crédito de 5 años | Confusión con interés compuesto | El crédito de cuotas capitaliza; usa la Parte 7, clase 7. |
| El interés de mora crece exponencialmente | Se capitalizó la mora | Verifica la norma local: en muchos países capitalizar mora está prohibido. |
| El devengo mensual no cuadra con el cobro | Meses de distinta cantidad de días | Devenga por días reales y concilia contra el cobro del periodo. |

## ❓ Preguntas de comprobación

1. ¿Por qué `I = C · i · n` exige que `i` y `n` compartan unidad y qué ocurre si no?
2. ¿Cuánto más cobra la base 360 frente a la 365 en una operación de 90 días? Demuéstralo.
3. ¿Por qué el costo efectivo de un descuento de factura supera a la tasa cotizada?
4. Nombra tres operaciones reales donde el interés simple sí es la convención correcta.
5. ¿Qué diferencia hay entre interés devengado e interés cobrado, y por qué importa contablemente?

## 📥 Entregable

Guarda en `portfolio/parte-01/clase-05/`:

- la tabla comparativa de bases 360 y 365 con la brecha en pesos y en porcentaje;
- los cuatro despejes resueltos;
- el caso de descuento de factura con el costo efectivo anualizado;
- la tabla de devengo diario con su verificación.

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

- Kellison, S. (2008). *The Theory of Interest* (3.ª ed.). McGraw-Hill/Irwin. Capítulo 1: interés simple, convenciones de conteo de días y el problema del interés anticipado.
- Broverman, S. (2017). *Mathematics of Investment and Credit* (7.ª ed.). ACTEX. Capítulo 1: bases 30/360, actual/360 y actual/365 con ejemplos comparados.
- Ross, S., Westerfield, R. y Jordan, B. (2022). *Fundamentos de finanzas corporativas* (12.ª ed.). McGraw-Hill. Capítulo 6: tasa cotizada frente a tasa efectiva.
- International Capital Market Association. *ICMA Rule Book* — convenciones de conteo de días en mercados de renta fija. <https://www.icmagroup.org/>
- IFRS Foundation (2014). *NIIF 9 Instrumentos Financieros*, sección 5.4: método del interés efectivo y reconocimiento de ingresos por devengo.
- Verificación local: revisa la ley de operaciones de crédito de dinero de tu país (en Chile, Ley 18.010) para conocer qué base de días y qué régimen de mora son admisibles.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 04 · Variaciones porcentuales e índices](04-variaciones-porcentuales-e-indices.md) | [Parte 01](../README.md) · [Programa](../../../SYLLABUS.md) | [06 · Interés compuesto →](06-interes-compuesto.md) |
<!-- gen:footer:end -->
