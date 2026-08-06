---
part: 1
class: 4
title: "Variaciones porcentuales e índices"
level: fundamento
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 04 · Variaciones porcentuales e índices

> [← 03 · Porcentajes en decisiones financieras](03-porcentajes-en-decisiones-financieras.md) · [Índice de la parte](../README.md) · [05 · Interés simple →](05-interes-simple.md)

**Parte 01 — Matemática financiera básica** · **Nivel:** Fundamento — sin conocimientos previos · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Aprender a medir cambios en el tiempo sin dejarse engañar por la base ni por el periodo. Aquí
aparecen los tres instrumentos con los que se lee cualquier informe económico o bancario: la
**variación mes contra mes**, la **variación de doce meses** y el **número índice**. También se
introduce la media geométrica, que es la única forma correcta de promediar crecimientos.

## 📚 Objetivos

Al finalizar podrás:

1. **Calcular** variaciones absolutas, relativas y acumuladas sin confundirlas.
2. **Construir** un número índice con base 100 y explicar qué significa cada punto.
3. **Distinguir** variación mensual, variación en doce meses y variación acumulada del año.
4. **Promediar** tasas de crecimiento con media geométrica y demostrar por qué la aritmética miente.
5. **Deflactar** una serie para separar crecimiento real de crecimiento nominal.

<!-- gen:agenda:start -->
## Agenda de 90 minutos

| Minutos | Bloque | Qué ocurre |
|---:|---|---|
| 0–10 | Activación | Pregunta diagnóstica y recuperación de la clase anterior. |
| 10–35 | Conceptos | Desarrollo guiado con la fuente oficial a la vista. |
| 35–55 | Ejemplo guiado | El docente resuelve el caso numérico paso a paso. |
| 55–80 | Práctica | El estudiante replica con datos propios o sintéticos. |
| 80–90 | Cierre | Preguntas de comprobación y registro en el portafolio. |
<!-- gen:agenda:end -->

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| `variación absoluta` | Diferencia simple: `V₁ − V₀`. Tiene unidades (pesos, puntos) y no permite comparar entre magnitudes distintas. |
| `variación relativa` | `(V₁ − V₀) / V₀`. Adimensional, comparable, y absolutamente dependiente de `V₀`. |
| `número índice` | Serie reescalada a un periodo base = 100. El índice 112,4 significa "12,4 % por encima del periodo base", no "12,4 %". |
| `variación en 12 meses` | Compara un mes con el mismo mes del año anterior. Neutraliza la estacionalidad; es la que publican los bancos centrales. |
| `variación acumulada` | Producto de factores del periodo: `Π(1 + rᵢ) − 1`. No es la suma de las variaciones. |
| `media geométrica` | `(Π(1 + rᵢ))^(1/n) − 1`. Es el crecimiento constante equivalente. La media aritmética de rentabilidades **sobreestima** siempre. |
| `serie real` | Serie nominal deflactada por un índice de precios. Separa "más dinero" de "más capacidad de compra". |

## 🧠 Modelo mental

Una serie temporal se lee en **tres velocidades** simultáneas:

```text
mes contra mes    ¿qué pasó ahora?          ruidoso, estacional
doce meses        ¿qué pasó en el año?      limpio de estacionalidad
acumulado         ¿cómo vamos en el año?    depende de en qué mes estemos
```

Un titular que dice "los precios cayeron" usando la primera velocidad y otro que dice "los precios
subieron" usando la segunda pueden ser ambos correctos el mismo día. Leer sin declarar la velocidad
es la fuente número uno de malentendidos en información económica.

## 📖 Desarrollo

### 1. Las tres variaciones y cuándo usar cada una

Serie de colocaciones de un banco, en miles de millones:

| Mes | Valor | Var. mensual | Var. 12 meses | Acumulado del año |
|---|---:|---:|---:|---:|
| dic año 0 | 2 400 | — | — | — |
| ene | 2 388 | −0,50 % | +6,1 % | −0,50 % |
| feb | 2 421 | +1,38 % | +6,4 % | +0,88 % |
| mar | 2 466 | +1,86 % | +6,9 % | +2,75 % |

El acumulado **no** es `−0,50 + 1,38 + 1,86 = 2,74 %`. Es:

```text
(1 − 0,0050) × (1 + 0,0138) × (1 + 0,0186) − 1 = 0,02750 → 2,750 %
```

La diferencia es pequeña en tres meses y deja de serlo en doce, o cuando las variaciones son grandes.

### 2. Números índice

Un índice reescala una serie para que el periodo base valga 100:

```text
índiceₜ = (Valorₜ / Valor_base) × 100
```

Con base dic año 0 = 100:

| Mes | Valor | Índice |
|---|---:|---:|
| dic año 0 | 2 400 | 100,0 |
| ene | 2 388 | 99,5 |
| feb | 2 421 | 100,9 |
| mar | 2 466 | 102,8 |

Dos lecturas críticas:

- El índice 102,8 significa **2,8 % por sobre el periodo base**, no 2,8 %.
- La diferencia entre dos índices se mide en **puntos de índice**, y su variación relativa se calcula
  igual que cualquier otra: `(102,8 − 99,5) / 99,5 = 3,3 %`.

Los índices más usados en este programa: IPC (precios), IMACEC o PIB (actividad), índices bursátiles
(Parte 8) y unidades de cuenta indexadas como la UF chilena o la UVR colombiana.

### 3. Media geométrica: la única forma de promediar crecimientos

Un fondo rinde `+50 %` un año y `−50 %` al siguiente.

```text
media aritmética   (0,50 − 0,50) / 2 = 0 %      ← sugiere que quedaste igual
resultado real     1,50 × 0,50 = 0,75 → −25 %   ← perdiste un cuarto
media geométrica   (1,50 × 0,50)^(1/2) − 1 = −13,4 % anual
```

La media geométrica de `−13,4 %` aplicada dos veces reproduce exactamente el `−25 %`. Es el
**crecimiento constante equivalente** y es la cifra que debe publicarse como rentabilidad anualizada.
La media aritmética solo coincide cuando todas las variaciones son iguales, y en cualquier otro caso
sobreestima. En la Parte 8 esta diferencia se llama *volatility drag* y explica por qué un fondo
volátil rinde menos de lo que su promedio simple sugiere.

### 4. Nominal y real: deflactar

```text
valor real = valor nominal × (índice base / índice del periodo)
crecimiento real ≈ (1 + nominal) / (1 + inflación) − 1
```

Un sueldo que sube 6 % con inflación de 4,5 %:

```text
(1,06 / 1,045) − 1 = 0,01435 → +1,44 % real
```

La aproximación `6 − 4,5 = 1,5 %` funciona con tasas bajas y se rompe con inflación alta:

| Nominal | Inflación | Resta ingenua | Real correcto |
|---:|---:|---:|---:|
| 6 % | 4,5 % | 1,5 % | 1,44 % |
| 30 % | 25 % | 5,0 % | 4,00 % |
| 120 % | 100 % | 20,0 % | 10,00 % |

## 🧮 Ejemplo guiado

**Situación.** Los ingresos de una pyme fueron 48, 52, 47, 61 millones en los cuatro trimestres del
año. El IPC del periodo acumuló 5,2 %. Se pide el crecimiento del año, el promedio trimestral
correcto y el crecimiento real.

**Paso 1 — variaciones trimestrales.**

```text
T1→T2  52/48 − 1 = +8,33 %
T2→T3  47/52 − 1 = −9,62 %
T3→T4  61/47 − 1 = +29,79 %
```

**Paso 2 — variación acumulada.**

```text
1,0833 × 0,9038 × 1,2979 − 1 = 0,27083 → +27,08 %
verificación directa: 61/48 − 1 = 0,27083  ✔
```

La verificación directa es obligatoria: si el producto de factores no coincide con el cociente
extremo a extremo, hay un error de cálculo.

**Paso 3 — promedio trimestral correcto.**

```text
media geométrica = (1,2708)^(1/3) − 1 = 0,08313 → +8,31 % por trimestre
media aritmética = (8,33 − 9,62 + 29,79) / 3 = +9,50 %   ← sobreestima 1,19 pp
```

**Paso 4 — crecimiento real.**

```text
(1,2708 / 1,052) − 1 = 0,20800 → +20,80 % real
```

**Paso 5 — interpreta con límites.** La empresa creció 27,1 % nominal y 20,8 % real en el año. El
promedio de 8,31 % trimestral es un equivalente aritmético útil para proyectar, **no** una
descripción del comportamiento: el T3 cayó casi 10 % y esa volatilidad es información relevante para
el capital de trabajo de la Parte 13, clase 2.

## 🏦 Del cliente al banco

| Uso cotidiano | Uso bancario | Dónde aparece en el programa |
|---|---|---|
| "Los precios subieron" | Variación IPC 12 meses, dato oficial del instituto de estadística | Parte 6, clase 6 |
| "Este fondo rindió 12 % promedio" | Rentabilidad anualizada geométrica, obligatoria en la ficha del fondo | Parte 8, clase 8 |
| "Mi sueldo subió" | Crecimiento real deflactado, insumo del análisis de capacidad de pago | Parte 9, clase 4 |
| "Las colocaciones crecen" | Serie indexada base 100 con desestacionalización | Parte 15, clase 5 |

## 🧪 Práctica

En `labs/lab-02.md`, sección de series:

1. Toma 24 meses del dataset `datasets/transactions_synthetic.csv` agregados por mes.
2. Calcula las tres variaciones (mensual, 12 meses, acumulada) y grafícalas juntas.
3. Construye el índice base 100 en el primer mes.
4. Compara media aritmética contra geométrica y cuantifica el sesgo.
5. Deflacta la serie con una inflación supuesta de 4,0 % anual.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| El acumulado no coincide con el cociente extremo a extremo | Se sumaron variaciones en vez de multiplicar factores | Usa `Π(1 + rᵢ) − 1` y verifica contra `Vₙ/V₀ − 1`. |
| La rentabilidad publicada no reproduce el saldo final | Se usó media aritmética | Publica media geométrica (rentabilidad anualizada). |
| "El índice subió 3 %" cuando pasó de 100 a 103 | Confusión entre puntos de índice y porcentaje | Con base 100 coinciden; con base distinta de 100, no. |
| Una serie parece crecer y el poder de compra cae | Se comparó en términos nominales | Deflacta con el índice de precios del mismo periodo. |
| La variación mensual contradice la de 12 meses | Estacionalidad | Usa variación en 12 meses o serie desestacionalizada para tendencia. |
| Resta de tasas con inflación alta da resultados imposibles | La aproximación lineal no aplica | Usa `(1+n)/(1+π) − 1` siempre. |

## ❓ Preguntas de comprobación

1. Una serie sube 10 %, baja 5 % y sube 3 %. ¿Cuál es el acumulado y por qué no es 8 %?
2. Un índice pasa de 128,4 a 133,1. ¿Cuántos puntos subió y cuál es la variación porcentual?
3. ¿Por qué la media aritmética de rentabilidades siempre sobreestima el resultado real?
4. Con inflación de 100 % y salario nominal +120 %, ¿cuánto ganaste realmente?
5. ¿Cuándo la variación mes contra mes es más informativa que la de doce meses?

## 📥 Entregable

Guarda en `portfolio/parte-01/clase-04/`:

- la tabla con las tres variaciones y el índice base 100;
- la comparación media aritmética contra geométrica con el sesgo cuantificado;
- la serie deflactada junto a la nominal;
- una conclusión de 200 palabras sobre qué velocidad de lectura usarías para informar a un directorio y por qué.

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

- Mankiw, N. G. (2021). *Principios de economía* (9.ª ed.). Cengage. Capítulo 24: números índice, IPC y deflactación.
- Blanchard, O. (2021). *Macroeconomía* (8.ª ed.). Pearson. Capítulo 2: variables nominales y reales, construcción de índices.
- Bodie, Z., Kane, A. y Marcus, A. (2023). *Investments* (13.ª ed.). McGraw-Hill. Capítulo 5: medias aritmética y geométrica de rentabilidades.
- International Labour Organization (2004). *Consumer Price Index Manual: Theory and Practice*. OIT/FMI/OCDE. Metodología estándar de construcción de índices de precios.
- International Monetary Fund (2020). *Quarterly National Accounts Manual*. FMI. Capítulo sobre encadenamiento y series desestacionalizadas.
- Verificación local: usa la serie oficial del instituto de estadística de tu país y registra fecha de descarga; los índices se revisan y cambian de base periódicamente.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 03 · Porcentajes en decisiones financieras](03-porcentajes-en-decisiones-financieras.md) | [Parte 01](../README.md) · [Programa](../../../SYLLABUS.md) | [05 · Interés simple →](05-interes-simple.md) |
<!-- gen:footer:end -->
