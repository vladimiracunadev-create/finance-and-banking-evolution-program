---
part: 7
class: 4
title: "Anualidades vencidas"
level: avanzado
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 04 · Anualidades vencidas

> [← 03 · Conversión de periodicidades](03-conversion-de-periodicidades.md) · [Índice de la parte](../README.md) · [05 · Anualidades anticipadas →](05-anualidades-anticipadas.md)

**Parte 07 — Matemática financiera avanzada** · **Nivel:** Avanzado — perfil analista · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Dominar la estructura de flujo más común de las finanzas: una serie de pagos iguales al final de cada
periodo. Créditos, arriendos, sueldos, seguros y bonos con cupón fijo son anualidades vencidas. Esta
clase deriva sus fórmulas, muestra sus cuatro despejes y las aplica a los cálculos que se usan a
diario.

## 📚 Objetivos

Al finalizar podrás:

1. **Derivar** las fórmulas de valor presente y futuro de una anualidad vencida.
2. **Despejar** cualquiera de las cuatro variables.
3. **Calcular** anualidades con crecimiento constante.
4. **Aplicar** anualidades diferidas con periodo de gracia.
5. **Resolver** problemas con anualidades combinadas.

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
| `anualidad vencida` | Serie de pagos iguales al **final** de cada periodo. Es la convención por defecto. |
| `factor de valor presente` | `a(n,i) = [1 − (1+i)^-n] / i`. Cuántas veces el pago cabe en el valor presente. |
| `factor de valor futuro` | `s(n,i) = [(1+i)^n − 1] / i`. |
| `anualidad diferida` | Los pagos empiezan después de `k` periodos de gracia. |
| `anualidad creciente` | Los pagos crecen a una tasa constante `g`. |
| `relación entre factores` | `s(n,i) = a(n,i) × (1+i)^n`. |

## 🧠 Modelo mental

Una anualidad es una **suma de valores presentes que tiene forma cerrada**:

```text
VP = A/(1+i) + A/(1+i)² + ... + A/(1+i)^n
```

Es una progresión geométrica, y su suma es:

```text
VP = A × [1 − (1+i)^-n] / i
```

Entender que es una suma —no una fórmula mágica— permite adaptarla a cualquier variante: si un pago
falta, se resta; si hay crecimiento, cambia la razón de la progresión.

## 📖 Desarrollo

### 1. Derivación

```text
VP = A Σ(t=1 a n) (1+i)^-t
```

Multiplicando por `(1+i)` y restando la original:

```text
VP(1+i) = A Σ(t=0 a n-1) (1+i)^-t
VP(1+i) − VP = A [1 − (1+i)^-n]
VP × i = A [1 − (1+i)^-n]

VP = A × [1 − (1+i)^-n] / i
```

Análogamente:

```text
VF = A × [(1+i)^n − 1] / i
```

Y la relación entre ambos:

```text
VF = VP × (1+i)^n
```

### 2. Los cuatro despejes

```text
VP  = A × [1 − (1+i)^-n]/i
A   = VP × i / [1 − (1+i)^-n]
n   = −ln(1 − VP×i/A) / ln(1+i)
i   → sin solución cerrada: se resuelve por iteración (Parte 1, clase 14)
```

Ejemplos:

```text
VP: A = 250 000 · i = 1,2 % · n = 48
    VP = 250 000 × [1 − (1,012)^-48]/0,012 = 250 000 × 36,1568 = 9 039 200

A:  VP = 9 039 200 · i = 1,2 % · n = 48  →  A = 250 000  ✔

n:  VP = 5 000 000 · A = 180 000 · i = 1,2 %
    n = −ln(1 − 5 000 000 × 0,012/180 000)/ln(1,012)
      = −ln(1 − 0,333333)/ln(1,012) = 0,405465/0,011928 = 34,0 periodos

i:  VP = 5 000 000 · A = 180 000 · n = 34  →  por iteración: i = 1,2000 %
```

### 3. Anualidad diferida

```text
VP = A × a(n,i) × (1+i)^-k

k = periodos de diferimiento
```

```text
crédito con 6 meses de gracia total y luego 36 cuotas de 420 000, i = 1,1 %

VP = 420 000 × [1 − (1,011)^-36]/0,011 × (1,011)^-6
   = 420 000 × 29,6432 × 0,936360
   = 420 000 × 27,7562 = 11 657 604
```

Verificación por otro camino:

```text
valor de las cuotas en el mes 6 = 420 000 × 29,6432 = 12 450 144
traído a hoy: 12 450 144 / (1,011)^6 = 12 450 144 / 1,067950 = 11 657 604 ✔
```

### 4. Anualidad creciente

Cuando los pagos crecen a una tasa `g` constante:

```text
si i ≠ g:   VP = A/(i − g) × [1 − ((1+g)/(1+i))^n]
si i = g:   VP = A × n / (1+i)
```

```text
A = 800 000 (primer pago) · g = 3 % anual · i = 9 % anual · n = 15

VP = 800 000/(0,09 − 0,03) × [1 − (1,03/1,09)^15]
   = 800 000/0,06 × [1 − (0,944954)^15]
   = 13 333 333 × [1 − 0,424553]
   = 13 333 333 × 0,575447 = 7 672 627
```

Comparación con una anualidad constante de 800 000:

```text
constante: 800 000 × [1 − (1,09)^-15]/0,09 = 800 000 × 8,06069 = 6 448 552
creciente: 7 672 627
diferencia: 1 224 075 (19,0 % más)
```

Este cálculo es la base de la valoración de flujos de arriendo indexados y de la proyección de
aportes de ahorro que crecen con el salario.

### 5. Anualidades combinadas

Cuando el flujo cambia de monto o de periodicidad, se descompone en tramos:

```text
crédito: 12 cuotas de 300 000 seguidas de 24 cuotas de 450 000, i = 1,3 %

VP tramo 1 = 300 000 × [1 − (1,013)^-12]/0,013 = 300 000 × 11,0703 = 3 321 090
VP tramo 2 = 450 000 × [1 − (1,013)^-24]/0,013 × (1,013)^-12
           = 450 000 × 20,5164 × 0,856348 = 7 906 429
VP total   = 11 227 519
```

La regla general: **cada tramo se valora como anualidad independiente y se descuenta al inicio del
tramo, luego se trae a hoy**.

## 🧮 Ejemplo guiado

**Situación.** Un banco estructura un crédito de capital de trabajo para una empresa con estacionalidad
marcada.

```text
monto solicitado           60 000 000
tasa                       1,15 % mensual
estructura propuesta:
  meses 1–4    gracia total (temporada baja)
  meses 5–16   cuotas de X (temporada media)
  meses 17–28  cuotas de 1,5X (temporada alta)
```

**Paso 1 — capitaliza durante la gracia.**

```text
saldo al mes 4 = 60 000 000 × (1,0115)^4 = 60 000 000 × 1,046790 = 62 807 400
```

**Paso 2 — plantea la ecuación de valor en el mes 4.**

```text
62 807 400 = X × a(12; 1,15%) + 1,5X × a(12; 1,15%) × (1,0115)^-12
```

**Paso 3 — calcula los factores.**

```text
(1,0115)^12 = 1,147211
a(12) = [1 − 1/1,147211]/0,0115 = [1 − 0,871680]/0,0115 = 11,15826
(1,0115)^-12 = 0,871680
```

**Paso 4 — resuelve.**

```text
62 807 400 = X × 11,15826 + 1,5X × 11,15826 × 0,871680
           = X × 11,15826 + X × 14,59006
           = X × 25,74832

X = 62 807 400 / 25,74832 = 2 439 285
1,5X = 3 658 928
```

**Paso 5 — construye la tabla de verificación (extracto).**

| Mes | Saldo inicial | Cuota | Interés | Amortización | Saldo final |
|---:|---:|---:|---:|---:|---:|
| 1 | 60 000 000 | 0 | 690 000 | −690 000 | 60 690 000 |
| 4 | 62 093 373 | 0 | 714 074 | −714 074 | 62 807 447 |
| 5 | 62 807 447 | 2 439 285 | 722 286 | 1 716 999 | 61 090 448 |
| 16 | 42 866 231 | 2 439 285 | 492 962 | 1 946 323 | 40 919 908 |
| 17 | 40 919 908 | 3 658 928 | 470 579 | 3 188 349 | 37 731 559 |
| 28 | 3 617 401 | 3 658 928 | 41 600 | 3 617 328 | **73** |

**Paso 6 — verifica y evalúa.**

```text
saldo final 73 ≈ 0  ✔ (ajuste en la última cuota)

pagos totales = 12 × 2 439 285 + 12 × 3 658 928 = 73 178 556
intereses totales = 73 178 556 − 60 000 000 = 13 178 556
costo sobre el monto = 21,96 %
TEA = (1,0115)^12 − 1 = 14,7211 %
```

**Interpreta:** la estructura estacional resolvió el problema de la empresa —no pagar en temporada
baja— a un costo concreto: **los cuatro meses de gracia total capitalizaron 2 807 400 de intereses**
que se pagan durante toda la vida del crédito. El cliente debe conocer ese número antes de firmar, y
calcularlo es exactamente lo que esta clase permite.

## 🏦 Del cliente al banco

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| Anualidad vencida | Cuota de todo crédito de cuotas iguales | 1, clase 11 |
| Anualidad diferida | Créditos con periodo de gracia | 13, clase 4 |
| Anualidad creciente | Arriendos indexados, proyección de aportes | 8, clase 10 |
| Anualidades combinadas | Estructuración estacional | 13, clase 2 |
| Verificación por tabla | Control obligatorio del cálculo | 1, clase 11 |

## 🧪 Práctica

En `labs/lab-02.md`, sección de anualidades:

1. Deriva la fórmula de valor presente a partir de la suma de la progresión.
2. Resuelve los cuatro despejes en cuatro casos distintos.
3. Calcula una anualidad creciente y compárala con la constante equivalente.
4. Estructura un crédito con tramos de cuota distinta y verifica con la tabla completa.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| El saldo final no cierra | Error en la conversión de tasa o en el diferimiento | Verifica con la tabla completa. |
| La anualidad diferida se descuenta k+1 periodos | Confusión sobre el punto de valoración | El factor `a(n,i)` ya sitúa el valor un periodo antes del primer pago. |
| Se suma la gracia al plazo sin capitalizar | Gracia total mal tratada | En gracia total el saldo capitaliza. |
| Se aplica la fórmula constante a flujos crecientes | Estructura distinta | Usa la fórmula de anualidad creciente. |
| Se resuelve `i` algebraicamente | No tiene solución cerrada | Usa iteración. |
| Se valoran tramos combinados sumando factores | Descuento omitido | Cada tramo se descuenta a su inicio y luego a hoy. |

## ❓ Preguntas de comprobación

1. Deriva la fórmula del valor presente de una anualidad vencida.
2. Calcula la cuota de 8 000 000 a 30 periodos con tasa de 1,4 % por periodo.
3. ¿Cuántos periodos toma amortizar 12 000 000 con cuotas de 400 000 al 1,1 %?
4. ¿Cómo se valora una anualidad que empieza después de 5 periodos de gracia?
5. Compara el valor presente de una anualidad constante y una creciente al 4 %.

## 📥 Entregable

Guarda en `portfolio/parte-07/clase-04/`:

- la derivación escrita de la fórmula de valor presente;
- los cuatro despejes resueltos con verificación;
- la comparación entre anualidad constante y creciente;
- la estructuración de un crédito con tramos y su tabla de verificación completa.

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

- Kellison, S. (2008). *The Theory of Interest* (3.ª ed.). McGraw-Hill/Irwin. Capítulos 3 y 4: anualidades vencidas, diferidas y variables.
- Broverman, S. (2017). *Mathematics of Investment and Credit* (7.ª ed.). ACTEX. Capítulo 2: anualidades y sus variantes.
- Ross, S., Westerfield, R. y Jordan, B. (2022). *Fundamentos de finanzas corporativas* (12.ª ed.). McGraw-Hill. Capítulo 5: anualidades y perpetuidades.
- Brealey, R., Myers, S. y Allen, F. (2023). *Principios de finanzas corporativas* (14.ª ed.). McGraw-Hill. Capítulo 2: fórmulas de valor presente de series.
- Luenberger, D. (2013). *Investment Science* (2.ª ed.). Oxford University Press. Capítulo 3: flujos determinísticos.
- Verificación local: contrasta con la estructura de cuotas que exige informar tu regulador en la tabla de desarrollo de un crédito.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 03 · Conversión de periodicidades](03-conversion-de-periodicidades.md) | [Parte 07](../README.md) · [Programa](../../../SYLLABUS.md) | [05 · Anualidades anticipadas →](05-anualidades-anticipadas.md) |
<!-- gen:footer:end -->
