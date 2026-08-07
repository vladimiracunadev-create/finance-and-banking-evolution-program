<!-- meta
part: 7
class: 1
title: "Tasas nominales y efectivas"
level: avanzado
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 01 · Tasas nominales y efectivas

> [← Índice de la parte](../README.md) · [Índice de la parte](../README.md) · [02 · Tasas equivalentes →](02-tasas-equivalentes.md)

**Parte 07 — Matemática financiera avanzada** · **Nivel:** Avanzado — perfil analista · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Eliminar de forma definitiva la confusión más costosa de las finanzas: una tasa nominal no es una
tasa. Es una convención de cotización que solo adquiere significado al declarar su frecuencia de
capitalización. Esta clase entrega el aparato completo de conversión y el criterio para comparar
cualquier par de tasas.

La Parte 1 usó una sola tasa por periodo y funcionó porque todos los ejemplos estaban alineados. Esta parte levanta ese supuesto, y empieza por donde se rompe: una tasa publicada no dice cuánto se paga si no se sabe con qué frecuencia capitaliza. Dos ofertas con la misma cifra pueden costar distinto, y la diferencia es exactamente esta clase.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** tasa nominal, periódica y efectiva con precisión.
2. **Convertir** entre las tres en cualquier dirección.
3. **Calcular** la tasa efectiva anual de cualquier cotización.
4. **Aplicar** la capitalización continua y saber cuándo importa.
5. **Comparar** ofertas de cotización distinta sobre una base única.

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

Los cuatro primeros términos son la misma tasa expresada de formas distintas; los dos últimos son el caso límite y la relación general. La **tasa efectiva anual** es la única comparable entre ofertas, y por eso la regulación de casi todos los países obliga a publicarla.

| Concepto | Comprensión verificable |
|---|---|
| `tasa nominal (j)` | Cotización anual que **debe** acompañarse de su frecuencia de capitalización. Sola, no significa nada. |
| `frecuencia (m)` | Número de capitalizaciones por año. |
| `tasa periódica (i)` | `j/m`. Es la que efectivamente se aplica en cada periodo. |
| `tasa efectiva anual (TEA)` | `(1 + j/m)^m − 1`. Rendimiento real de un año, comparable siempre. |
| `capitalización continua` | Límite cuando `m → ∞`: `TEA = e^j − 1`. |
| `tasa equivalente` | Tasa de otra periodicidad que produce el mismo resultado en el mismo plazo. |

## 🧠 Modelo mental

Piensa en la tasa nominal como un **precio sin unidad**:

```text
"12 % anual"                      → incompleto, no se puede operar
"12 % anual capitalizable mensual" → completo: i = 1 % mensual, TEA = 12,683 %
"12 % efectivo anual"              → completo: TEA = 12 %
```

Toda cotización financiera profesional declara la frecuencia. Cuando no lo hace, la primera pregunta
—antes de cualquier cálculo— es cuál es.

## 📖 Desarrollo

### 1. Las tres tasas y su relación

Nominal, periódica y efectiva no son tres conceptos sino tres formas de escribir lo mismo, y pasar de una a otra es mecánico. El esquema siguiente recoge las tres relaciones.

```text
tasa periódica     i = j / m
tasa efectiva      TEA = (1 + i)^m − 1 = (1 + j/m)^m − 1
tasa nominal       j = m × [(1 + TEA)^(1/m) − 1]
```

Con `j = 18 %` y distintas frecuencias:

| Capitalización | m | i periódica | TEA |
|---|---:|---:|---:|
| Anual | 1 | 18,0000 % | 18,0000 % |
| Semestral | 2 | 9,0000 % | 18,8100 % |
| Trimestral | 4 | 4,5000 % | 19,2519 % |
| Mensual | 12 | 1,5000 % | 19,5618 % |
| Quincenal | 24 | 0,7500 % | 19,6412 % |
| Diaria | 365 | 0,0493 % | 19,7164 % |
| Continua | ∞ | — | 19,7217 % |

Dos observaciones que hay que poder explicar:

```text
· la TEA siempre es ≥ que la nominal, y son iguales solo si m = 1
· la TEA CONVERGE: entre diaria y continua hay 0,0053 puntos
```

La convergencia explica por qué en la práctica casi nadie usa capitalización continua salvo en
modelos teóricos y en instrumentos de mercados profesionales.

### 2. Capitalización continua

Si la frecuencia de capitalización crece sin límite, la tasa efectiva converge a un valor concreto. El resultado tiene uso práctico en valoración de derivados y conviene conocerlo.

```text
TEA = e^j − 1
j = ln(1 + TEA)
```

```text
j = 18 % continua → TEA = e^0,18 − 1 = 0,197217 → 19,7217 %
TEA = 19,7217 % → j continua = ln(1,197217) = 0,18 = 18 %
```

La ventaja de la capitalización continua es algebraica: las tasas continuas **se suman**, mientras las
efectivas se multiplican.

```text
efectivas:  (1 + 0,08)(1 + 0,05) − 1 = 13,40 %
continuas:  8 % + 5 % = 13 % continua → equivale a 13,88 % efectiva
```

Por eso los modelos de valoración de derivados y las medidas de rendimiento en finanzas cuantitativas
usan tasas continuas: simplifican la aritmética.

### 3. Comparar ofertas

Cuatro ofertas de depósito a un año:

```text
A  8,40 % nominal capitalizable mensual
B  8,60 % nominal capitalizable trimestral
C  8,75 % efectivo anual
D  8,35 % nominal continua
```

```text
A  TEA = (1 + 0,084/12)^12 − 1 = (1,007)^12 − 1 = 8,7311 %
B  TEA = (1 + 0,086/4)^4 − 1 = (1,0215)^4 − 1 = 8,8836 %
C  TEA = 8,7500 %
D  TEA = e^0,0835 − 1 = 8,7085 %
```

| Oferta | Cotización | TEA | Orden |
|---|---|---:|---:|
| B | 8,60 % trimestral | 8,8836 % | 1 |
| C | 8,75 % efectivo | 8,7500 % | 2 |
| A | 8,40 % mensual | 8,7311 % | 3 |
| D | 8,35 % continua | 8,7085 % | 4 |

**La oferta con la cotización más alta (C, 8,75 %) no es la mejor, y la más baja (D, 8,35 %) no es la
peor.** Sin convertir a TEA, el orden es aleatorio.

### 4. El error de dividir una tasa efectiva

Dividir una tasa efectiva anual entre doce para obtener la mensual es el error más frecuente de esta parte, y produce una diferencia que crece con la tasa. El contraste siguiente lo cuantifica.

```text
✗ tasa mensual de una TEA de 24 % = 24/12 = 2 %
✓ tasa mensual de una TEA de 24 % = (1,24)^(1/12) − 1 = 1,8088 %
```

Verificación:

```text
(1,02)^12 − 1 = 26,824 %   ← no es 24 %
(1,018088)^12 − 1 = 24,000 % ✔
```

Dividir solo es correcto para tasas **nominales**, porque es su definición. Para efectivas hay que
usar la raíz. Este error, aplicado a un crédito, produce una cuota un 3 % más alta de lo que
corresponde.

### 5. Convención de días

Cuando el plazo no es un número entero de periodos:

```text
TEA con base 365:  i_días = (1 + TEA)^(días/365) − 1
TEA con base 360:  i_días = (1 + TEA)^(días/360) − 1
```

```text
TEA 12 %, plazo 47 días
  base 365: (1,12)^(47/365) − 1 = 1,4633 %
  base 360: (1,12)^(47/360) − 1 = 1,4835 %
  diferencia sobre 10 000 000: 20 200
```

La base debe declararse en el contrato. La Parte 1, clase 5, mostró el mismo problema con interés
simple; aquí reaparece con capitalización.

## 🧮 Ejemplo guiado

El ejemplo compara dos ofertas con la misma tasa nominal y distinta frecuencia. Conviene llegar hasta la efectiva anual antes de opinar: hasta ese punto las dos ofertas parecen idénticas.

**Situación.** Un tesorero compara cuatro alternativas de inversión de excedentes por 500 millones a
90 días, y cuatro alternativas de financiamiento a 180 días.

```text
INVERSIÓN (90 días)
  I1  4,80 % nominal capitalizable mensual
  I2  1,22 % efectivo trimestral
  I3  4,95 % efectivo anual
  I4  4,75 % nominal continua

FINANCIAMIENTO (180 días)
  F1  9,60 % nominal capitalizable mensual + comisión 0,20 % sobre el monto
  F2  4,85 % efectivo semestral
  F3  9,90 % efectivo anual
  F4  0,79 % efectivo mensual
```

**Paso 1 — lleva todas las inversiones a TEA.**

```text
I1  (1 + 0,048/12)^12 − 1 = (1,004)^12 − 1 = 4,9070 %
I2  (1,0122)^4 − 1 = 4,9698 %
I3  4,9500 %
I4  e^0,0475 − 1 = 4,8646 %
```

**Paso 2 — ordena y calcula el resultado a 90 días.**

| Alternativa | TEA | Rendimiento 90 días | Monto final |
|---|---:|---:|---:|
| I2 | 4,9698 % | 1,2200 % | 506 100 000 |
| I3 | 4,9500 % | 1,2152 % | 506 076 000 |
| I1 | 4,9070 % | 1,2049 % | 506 025 000 |
| I4 | 4,8646 % | 1,1947 % | 505 974 000 |

```text
diferencia entre la mejor y la peor: 126 000 sobre 500 millones en 90 días
```

**Paso 3 — lleva todos los financiamientos a TEA.**

```text
F1  (1 + 0,096/12)^12 − 1 = (1,008)^12 − 1 = 10,0339 %
    más comisión: se calcula sobre el flujo real (paso 4)
F2  (1,0485)^2 − 1 = 9,9352 %
F3  9,9000 %
F4  (1,0079)^12 − 1 = 9,9033 %
```

**Paso 4 — incorpora la comisión de F1 correctamente.**

```text
monto solicitado 500 000 000, comisión 0,20 % = 1 000 000
monto recibido 499 000 000
pago a 180 días = 500 000 000 × (1,100339)^(180/365) = 523 950 000

tasa efectiva sobre lo recibido:
  (523 950 000 / 499 000 000)^(365/180) − 1 = 10,4640 %
```

**La comisión de 0,20 % aumentó la TEA en 0,43 puntos**, más del doble de la comisión nominal, porque
se paga en un plazo de medio año.

**Paso 5 — ordena el financiamiento.**

| Alternativa | TEA efectiva | Costo a 180 días |
|---|---:|---:|
| F3 | 9,9000 % | 23 850 000 |
| F4 | 9,9033 % | 23 858 000 |
| F2 | 9,9352 % | 23 934 000 |
| F1 | 10,4640 % | 24 950 000 |

**Paso 6 — la decisión y lo que enseña.**

```text
invertir en I2 y financiarse con F3
diferencia total frente a la peor combinación: 126 000 + 1 100 000 = 1 226 000

y el hallazgo cualitativo: F1 tenía la SEGUNDA cotización más baja en apariencia
(9,60 % nominal) y resultó la MÁS CARA al incorporar comisión y frecuencia
```

**Interpreta:** ocho cotizaciones expresadas de siete formas distintas, y el orden correcto solo
aparece tras llevarlas todas a una base común. Ese paso —tres minutos de cálculo— es la diferencia
entre una decisión de tesorería informada y una aleatoria.

## 🏦 Del cliente al banco

El cliente ve una tasa publicada y el banco calcula su rendimiento efectivo. La tabla enfrenta las dos lecturas, y explica por qué la frecuencia de capitalización es una cláusula y no un detalle.

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| TEA | Base de comparación normativa (CAE) | 3, clase 13 |
| Tasa periódica | Cálculo de cuotas y devengo | 1, clase 11 |
| Capitalización continua | Valoración de derivados | 8, clase 7 |
| Base de días | Cláusula contractual con efecto material | 1, clase 5 |
| Comisión sobre el flujo | Diferencia entre tasa cotizada y costo efectivo | 3, clase 13 |

## 🧪 Práctica

El laboratorio pide convertir entre las tres formas y comparar ofertas que solo difieren en frecuencia. El resultado es que la oferta con menor tasa nominal puede ser la más cara.

En `labs/lab-01.md`:

1. Convierte diez cotizaciones distintas a TEA y ordénalas.
2. Demuestra numéricamente por qué dividir una TEA por 12 es incorrecto.
3. Calcula la TEA de un financiamiento con comisión sobre el flujo recibido.
4. Compara base 360 y 365 en cinco plazos y tabula la diferencia.

## ⚠️ Errores frecuentes

La tabla se usa buscando el síntoma. En esta clase casi todos vienen de haber operado con una tasa sin saber a qué periodo corresponde.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se compara por la cotización | Frecuencias distintas | Convierte todo a TEA. |
| Se divide una TEA por 12 | Confusión nominal/efectiva | Usa `(1+TEA)^(1/12) − 1`. |
| Se ignora la comisión al comparar | Costo efectivo mal medido | Calcula sobre el flujo realmente recibido. |
| Se usa base 365 en un contrato de base 360 | Convención no verificada | Declara y verifica la base. |
| Se usa capitalización continua sin necesidad | Complejidad innecesaria | Converge con la diaria; úsala solo si el modelo lo requiere. |
| Una tasa nominal se usa sin su frecuencia | Cotización incompleta | Exige la frecuencia antes de operar. |

## ❓ Preguntas de comprobación

1. ¿Por qué una tasa nominal sin frecuencia no significa nada?
2. Convierte 15 % nominal capitalizable trimestral a TEA y a tasa mensual efectiva.
3. Demuestra que dividir una TEA de 30 % por 12 produce un error material.
4. ¿Cuánto suma una comisión del 0,3 % a la TEA de un crédito a 90 días?
5. ¿Por qué las tasas continuas se suman y las efectivas se multiplican?

## 📥 Entregable

Guarda en `portfolio/parte-07/clase-01/`:

- la tabla de diez cotizaciones convertidas a TEA y ordenadas;
- la demostración numérica del error de dividir una tasa efectiva;
- el cálculo de TEA de un financiamiento con comisión;
- la comparación de bases 360 y 365 en cinco plazos.

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

- Kellison, S. (2008). *The Theory of Interest* (3.ª ed.). McGraw-Hill/Irwin. Capítulo 1: tasas nominales, efectivas y fuerza de interés.
- Broverman, S. (2017). *Mathematics of Investment and Credit* (7.ª ed.). ACTEX. Capítulo 1: equivalencia de tasas y convenciones.
- Ross, S., Westerfield, R. y Jordan, B. (2022). *Fundamentos de finanzas corporativas* (12.ª ed.). McGraw-Hill. Capítulo 6: tasa efectiva anual.
- Hull, J. (2021). *Options, Futures, and Other Derivatives* (11.ª ed.). Pearson. Capítulo 4: capitalización continua y su uso.
- International Capital Market Association. *ICMA Rule Book*: convenciones de conteo de días. <https://www.icmagroup.org/>
- Verificación local: revisa cómo exige tu regulador expresar las tasas en la información al cliente y qué base de días aplica por tipo de operación.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← Índice de la parte](../README.md) | [Parte 07](../README.md) · [Programa](../../../SYLLABUS.md) | [02 · Tasas equivalentes →](02-tasas-equivalentes.md) |
<!-- gen:footer:end -->
