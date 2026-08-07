---
part: 1
class: 2
title: "Fracciones, decimales y razones"
level: fundamento
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 02 · Fracciones, decimales y razones

> [← 01 · Diagnóstico y operaciones esenciales](01-diagnostico-y-operaciones-esenciales.md) · [Índice de la parte](../README.md) · [03 · Porcentajes en decisiones financieras →](03-porcentajes-en-decisiones-financieras.md)

**Parte 01 — Matemática financiera básica** · **Nivel:** Fundamento — sin conocimientos previos · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Dominar las tres formas de expresar una misma proporción —fracción, decimal y razón— y saber cuándo
cada una engaña. Un banco no dice "la mitad": dice `0,5`, `50 %`, `1:1` o `50 puntos base` según el
contexto, y cada forma tiene un lector distinto y un riesgo distinto de malinterpretación. Esta clase
también instala la unidad que domina la banca profesional: el **punto base**.

## 📚 Objetivos

Al finalizar podrás:

1. **Convertir** sin error entre fracción, decimal, porcentaje, razón y puntos base.
2. **Distinguir** una razón `parte:parte` de una proporción `parte:todo`, que es la confusión que
   más ruido genera en informes.
3. **Usar** puntos base para hablar de tasas con la precisión que exige una mesa de dinero.
4. **Detectar** cuándo un decimal periódico obliga a fijar una convención de precisión.
5. **Leer** un ratio financiero identificando qué hay arriba y qué hay abajo.

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
| `fracción` | Parte sobre todo: `3/4`. Útil para razonar, incómoda para operar en cadena. |
| `decimal` | La misma cantidad en base 10: `0,75`. Es la forma en la que se calcula. |
| `porcentaje` | El decimal por 100: `75 %`. Es la forma en la que se comunica. |
| `razón` | Comparación entre dos cantidades: `3:1` significa tres de uno por cada uno del otro. **No** es `3/4`. |
| `punto base (pb)` | Una centésima de punto porcentual: `1 pb = 0,01 % = 0,0001`. Existe porque decir "subió 0,25 %" es ambiguo y "subió 25 pb" no lo es. |
| `ratio financiero` | Cociente entre dos magnitudes del mismo estado o periodo. Su significado depende por completo de qué se pone en el denominador. |

## 🧠 Modelo mental

Toda proporción responde a la pregunta **"¿cuánto de esto por cada cuánto de aquello?"**. Antes de
convertir nada, nombra las dos cantidades:

```text
razón     deuda : patrimonio = 3 : 1     por cada 1 de patrimonio hay 3 de deuda
fracción  deuda / activos    = 3/4       la deuda es tres cuartos del total
```

Son el **mismo balance** descrito de dos maneras. Confundirlas convierte un apalancamiento de 300 %
en uno de 75 % en el mismo párrafo, y eso ocurre en informes reales.

## 📖 Desarrollo

### 1. Las cuatro formas y sus conversiones

```text
fracción → decimal      dividir:            3/8 = 0,375
decimal  → porcentaje   multiplicar × 100:  0,375 = 37,5 %
porcentaje → pb         multiplicar × 100:  0,375 % = 37,5 pb
pb → decimal            dividir ÷ 10 000:   37,5 pb = 0,00375
```

La cadena completa, para no perderse nunca:

| Forma | Valor | Cuándo se usa |
|---|---:|---|
| Fracción | 1/8 | Razonamiento y explicación oral |
| Decimal | 0,125 | Cálculo y código |
| Porcentaje | 12,5 % | Comunicación al cliente |
| Puntos base | 1 250 pb | Mesa de dinero, tesorería, pricing |

### 2. Razón `parte:parte` frente a proporción `parte:todo`

Un fondo tiene 60 millones en renta fija y 40 en renta variable.

```text
razón renta fija : renta variable  = 60 : 40 = 3 : 2
proporción de renta fija sobre el total = 60 / 100 = 0,60 = 60 %
```

Ambas son correctas y describen lo mismo. El error aparece al decir "la razón es 60 %", que mezcla
las dos formas. La regla de lectura: **si los dos números suman el todo, es proporción; si se
comparan entre sí, es razón**.

### 3. Puntos base: por qué la banca inventó otra unidad

Una tasa sube de 4,00 % a 4,25 %. ¿Subió 0,25 % o subió 6,25 %?

```text
en puntos porcentuales   4,25 − 4,00 = 0,25 puntos porcentuales = 25 pb
en variación relativa    (4,25 − 4,00) / 4,00 = 0,0625 = 6,25 %
```

**Las dos afirmaciones son verdaderas y hablan de cosas distintas.** El punto base elimina la
ambigüedad: "el spread subió 25 pb" no admite dos lecturas. En la Parte 15, clase 7, el precio de un
crédito se construye sumando puntos base sobre una tasa base; sin esta unidad esa conversación es
imposible.

### 4. Decimales periódicos y precisión declarada

```text
1/3 = 0,333...   2/7 = 0,285714285714...
```

Ningún sistema financiero guarda infinitos decimales. La consecuencia práctica: cuando repartes un
monto en partes iguales, **la suma de las partes redondeadas no es el total**.

```text
1 000 000 repartido en 3 cuotas
  333 333,33 × 3 = 999 999,99   ← faltan 0,01
```

La solución profesional es la **cuota de ajuste**: dos cuotas de 333 333,33 y una de 333 333,34. La
misma técnica aparece en la clase 12 con las tablas de amortización y en la Parte 10 con la
conciliación.

## 🧮 Ejemplo guiado

**Situación.** Un banco publica: cartera de consumo 420 000 millones, cartera hipotecaria
780 000 millones, cartera comercial 1 300 000 millones. La tasa de un crédito pasó de 11,90 % a
12,55 %. Se pide describir la composición y la variación con precisión.

**Paso 1 — total y proporciones.**

```text
total = 420 000 + 780 000 + 1 300 000 = 2 500 000 millones

consumo     420 000 / 2 500 000 = 0,168  = 16,8 %
hipotecaria 780 000 / 2 500 000 = 0,312  = 31,2 %
comercial 1 300 000 / 2 500 000 = 0,520  = 52,0 %
                                  suma   = 100,0 %  ✔ control
```

La suma a 100 % es el control obligatorio de toda tabla de composición. Si no suma, hay una partida
olvidada o un doble conteo.

**Paso 2 — razón entre dos carteras.**

```text
comercial : consumo = 1 300 000 : 420 000 ≈ 3,10 : 1
```

Se lee: "por cada peso colocado en consumo hay 3,10 en comercial". Nótese que **no** es 310 % de la
cartera total; es una razón parte:parte.

**Paso 3 — variación de la tasa, en las dos lecturas.**

```text
en puntos base       (12,55 − 11,90) × 100 = 65 pb
en variación relativa (12,55 − 11,90) / 11,90 = 0,0546 = 5,46 %
```

**Paso 4 — redacta sin ambigüedad.** "La tasa subió 65 puntos base, un alza relativa de 5,5 %." Esta
frase es inmune a la confusión; "la tasa subió 0,65 %" no lo es.

## 🏦 Del cliente al banco

| Expresión coloquial | Expresión profesional | Por qué importa |
|---|---|---|
| "Subió un poquito la tasa" | "+65 pb sobre la tasa base" | Permite fijar precio y comparar entre productos |
| "La mitad está en depósitos" | "50,0 % de los pasivos son depósitos a la vista" | Alimenta el ratio de liquidez de la Parte 11 |
| "Debemos el triple de lo que tenemos" | "Razón deuda/patrimonio = 3:1" | Es una variable de covenant en contratos reales |
| "Repartimos en tres cuotas iguales" | "Dos cuotas de 333 333,33 y cuota de ajuste de 333 333,34" | Evita descuadres de centavos en la contabilidad |

## 🧪 Práctica

En `labs/lab-01.md`, sección de proporciones:

1. Toma el dataset `datasets/personal_budget_synthetic.csv` y construye la tabla de composición del
   gasto, verificando que sume 100 %.
2. Expresa tres relaciones como razón parte:parte y explica por qué no son porcentajes.
3. Convierte cinco tasas de porcentaje a puntos base y de vuelta.
4. Reparte 1 000 000 en 7 partes iguales y aplica la cuota de ajuste.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Una tabla de composición suma 99,7 % o 100,4 % | Redondeo de cada fila sin ajuste | Redondea y asigna el residuo a la fila mayor; declara el ajuste. |
| "La razón es 60 %" | Se mezcló razón con proporción | Razón se expresa `a:b`; proporción, en % sobre el todo. |
| Discusión sobre si la tasa subió 0,25 % o 6,25 % | Se habló en puntos porcentuales y en variación relativa sin distinguir | Usa puntos base para el cambio absoluto y "% de variación" para el relativo. |
| Las cuotas iguales no suman el capital | Decimal periódico truncado en todas las cuotas | Aplica cuota de ajuste en la última. |
| Un ratio parece enorme o ridículo | Numerador y denominador de periodos distintos | Verifica que ambos sean del mismo corte o del mismo periodo. |
| `1 pb` se interpreta como `1 %` | Confusión de unidad | 1 pb = 0,01 % = 0,0001. Cien puntos base son un punto porcentual. |

## ❓ Preguntas de comprobación

1. Una cartera se reparte 3:2 entre dos productos. ¿Qué porcentaje del total representa cada uno?
2. La tasa pasa de 6,00 % a 6,90 %. Expresa el cambio en puntos base y en variación relativa.
3. ¿Por qué la suma de tres cuotas redondeadas puede no igualar el capital y cómo se resuelve?
4. ¿Qué información falta para interpretar el ratio "0,42" que aparece en un informe?
5. ¿Cuándo conviene comunicar en fracción y cuándo en puntos base?

## 📥 Entregable

Guarda en `portfolio/parte-01/clase-02/`:

- la tabla de composición con control de suma a 100 %;
- tres razones parte:parte correctamente redactadas;
- una tabla de conversión de cinco tasas entre las cuatro formas;
- el ejercicio de cuota de ajuste con la comprobación del total.

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

- Brealey, R., Myers, S. y Allen, F. (2023). *Principios de finanzas corporativas* (14.ª ed.). McGraw-Hill. Capítulo 3: expresión de tasas y convenciones de mercado.
- Bodie, Z., Kane, A. y Marcus, A. (2023). *Investments* (13.ª ed.). McGraw-Hill. Capítulo 2: uso del punto base en instrumentos de renta fija.
- Fabozzi, F. (2021). *Bond Markets, Analysis, and Strategies* (10.ª ed.). MIT Press. Capítulo 2: spreads expresados en puntos base.
- Blank, L. y Tarquin, A. (2018). *Ingeniería económica* (8.ª ed.). McGraw-Hill. Capítulo 2: manejo de precisión y convenciones de redondeo.
- Bank for International Settlements. *BIS Statistical Bulletin* — convenciones de publicación de tasas y spreads. <https://www.bis.org/statistics/>
- Verificación local: revisa cómo expresa las tasas el regulador bancario de tu país (anual, mensual, base 360 o 365) antes de comparar cifras entre fuentes.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 01 · Diagnóstico y operaciones esenciales](01-diagnostico-y-operaciones-esenciales.md) | [Parte 01](../README.md) · [Programa](../../../SYLLABUS.md) | [03 · Porcentajes en decisiones financieras →](03-porcentajes-en-decisiones-financieras.md) |
<!-- gen:footer:end -->
