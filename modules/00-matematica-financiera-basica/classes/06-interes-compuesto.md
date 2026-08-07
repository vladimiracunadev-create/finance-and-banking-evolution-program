---
part: 1
class: 6
title: "Interés compuesto"
level: fundamento
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 06 · Interés compuesto

> [← 05 · Interés simple](05-interes-simple.md) · [Índice de la parte](../README.md) · [07 · Inflación y poder adquisitivo →](07-inflacion-y-poder-adquisitivo.md)

**Parte 01 — Matemática financiera básica** · **Nivel:** Fundamento — sin conocimientos previos · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Entender el mecanismo que gobierna casi todo el sistema financiero: **los intereses generan
intereses**. Esta clase es la bisagra del programa. Quien la domina puede leer un crédito
hipotecario, evaluar un fondo, entender por qué la inflación destruye ahorro y por qué una deuda de
tarjeta se vuelve inmanejable. Quien no la domina hará todo lo demás de memoria.

## 📚 Objetivos

Al finalizar podrás:

1. **Aplicar** `M = C(1 + i)^n` y explicar qué representa cada elemento del exponente.
2. **Cuantificar** la brecha entre interés simple y compuesto para distintos plazos.
3. **Determinar** el efecto de la frecuencia de capitalización sobre el resultado final.
4. **Usar** la regla del 72 como control mental de razonabilidad.
5. **Explicar** por qué el mismo mecanismo construye patrimonio y destruye a un deudor.

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
| `capitalización` | Momento en que el interés se suma al capital y empieza a generar interés por sí mismo. Es un **evento con fecha**, no una abstracción. |
| `factor de capitalización` | `(1 + i)^n`. Multiplica el capital. Todo el resto de la matemática financiera son variantes de este factor. |
| `frecuencia de capitalización` | Cuántas veces al año se capitaliza. A mayor frecuencia, mayor monto final con la misma tasa nominal. |
| `crecimiento exponencial` | El interés de cada periodo es mayor que el anterior porque la base creció. La curva se dispara al final, no al principio. |
| `regla del 72` | El capital se duplica aproximadamente en `72 / i%` periodos. Al 8 %, en 9 años. Error menor a 2 % para tasas entre 4 % y 15 %. |
| `simetría del daño` | El mismo mecanismo que multiplica un ahorro multiplica una deuda impaga. La tarjeta de crédito es interés compuesto en contra. |

## 🧠 Modelo mental

Piensa en una **escalera cuyos peldaños crecen**:

```text
capital 1 000 000, 2 % mensual COMPUESTO
  mes 1   +20 000,00   saldo 1 020 000,00
  mes 2   +20 400,00   saldo 1 040 400,00   ← el interés creció
  mes 3   +20 808,00   saldo 1 061 208,00
  mes 12  +23 787,63   saldo 1 268 241,79
```

Compáralo con la clase 5, donde cada peldaño medía exactamente 20 000. La diferencia a 12 meses son
**8 242 pesos**; a 120 meses, la diferencia es de 6 780 000 contra 3 400 000. El tiempo es el
multiplicador, no la tasa.

## 📖 Desarrollo

### 1. La fórmula y sus despejes

```text
M = C (1 + i)^n

C = M / (1 + i)^n              capital inicial (valor presente, clase 9)
i = (M/C)^(1/n) − 1            tasa implícita
n = ln(M/C) / ln(1 + i)        plazo necesario
```

El despeje de `n` usa logaritmos y es el único punto de la clase con matemática nueva. Su lectura es
directa: *cuántas veces hay que multiplicar por `(1+i)` para llegar de `C` a `M`*.

### 2. Simple contra compuesto: la brecha crece con el tiempo

Capital 1 000 000 al 10 % anual:

| Años | Simple | Compuesto | Brecha | Brecha % |
|---:|---:|---:|---:|---:|
| 1 | 1 100 000 | 1 100 000 | 0 | 0,0 % |
| 5 | 1 500 000 | 1 610 510 | 110 510 | 7,4 % |
| 10 | 2 000 000 | 2 593 742 | 593 742 | 29,7 % |
| 20 | 3 000 000 | 6 727 500 | 3 727 500 | 124,3 % |
| 30 | 4 000 000 | 17 449 402 | 13 449 402 | 336,2 % |

Dos lecciones. La primera: **en el primer periodo no hay diferencia**, por eso la gente subestima el
efecto. La segunda: la brecha no crece linealmente sino que se acelera, y a 30 años el compuesto
cuadruplica al simple.

### 3. Frecuencia de capitalización

Con una tasa nominal anual `j` capitalizada `m` veces al año:

```text
M = C (1 + j/m)^(m·n)
```

Un capital de 1 000 000 al 12 % nominal anual durante un año:

| Capitalización | m | Cálculo | Monto | Tasa efectiva |
|---|---:|---|---:|---:|
| Anual | 1 | `1,12^1` | 1 120 000 | 12,000 % |
| Semestral | 2 | `1,06^2` | 1 123 600 | 12,360 % |
| Trimestral | 4 | `1,03^4` | 1 125 509 | 12,551 % |
| Mensual | 12 | `1,01^12` | 1 126 825 | 12,683 % |
| Diaria | 365 | `(1+0,12/365)^365` | 1 127 475 | 12,747 % |
| Continua | ∞ | `e^0,12` | 1 127 497 | 12,750 % |

La misma tasa nominal produce seis resultados distintos. Esto explica por qué comparar créditos por
su tasa nominal es un error y por qué existe la tasa efectiva anual, que es el tema central de la
Parte 7, clase 1. Nótese también que el efecto **converge**: entre diaria y continua hay 22 pesos.

### 4. La regla del 72 y el control mental

```text
periodos para duplicar ≈ 72 / tasa en %
```

| Tasa | Regla del 72 | Exacto | Error |
|---:|---:|---:|---:|
| 3 % | 24,0 | 23,45 | +2,3 % |
| 6 % | 12,0 | 11,90 | +0,9 % |
| 9 % | 8,0 | 8,04 | −0,5 % |
| 12 % | 6,0 | 6,12 | −2,0 % |
| 24 % | 3,0 | 3,22 | −6,9 % |

Sirve para detectar disparates en segundos: si alguien promete duplicar tu dinero en 2 años, está
ofreciendo un 41 % anual, y esa cifra exige una explicación muy sólida sobre el riesgo asumido. Es
la primera defensa contra esquemas fraudulentos, tema de la Parte 4, clase 4.

### 5. El mismo mecanismo, en contra

Una deuda de tarjeta de 800 000 al 3,2 % mensual, pagando solo el mínimo del 5 %:

```text
mes 1   interés 25 600   pago 40 000   saldo 785 600
mes 12  interés 21 940   pago 34 280   saldo 673 220
mes 24  interés 18 297   pago 28 589   saldo 561 420
```

Tras dos años pagando puntualmente se han desembolsado **827 000 pesos** y aún se deben 561 420. El
interés compuesto no es bueno ni malo: es un multiplicador que amplifica la posición en la que
estás. La Parte 4, clase 10, desarrolla este caso completo.

## 🧮 Ejemplo guiado

**Situación.** Andrés tiene 3 500 000 y dos alternativas: un depósito a 24 meses al 7,2 % nominal
anual con capitalización mensual, o un fondo que promete 8,0 % efectivo anual. Además quiere saber
cuánto tardaría en duplicar su capital en la mejor opción.

**Paso 1 — depósito, tasa periódica.**

```text
i mensual = 0,072 / 12 = 0,006 → 0,6 % mensual
n = 24 meses
M = 3 500 000 × (1,006)^24
```

```text
(1,006)^24 = 1,154349...
M = 3 500 000 × 1,154349 = 4 040 222
```

**Paso 2 — depósito, tasa efectiva anual equivalente.**

```text
TEA = (1,006)^12 − 1 = 0,074424 → 7,4424 %
```

**Paso 3 — fondo al 8,0 % efectivo anual.**

```text
M = 3 500 000 × (1,08)^2 = 3 500 000 × 1,1664 = 4 082 400
```

**Paso 4 — compara sobre una base común.**

| Opción | TEA | Monto a 24 meses | Diferencia |
|---|---:|---:|---:|
| Depósito 7,2 % nominal, cap. mensual | 7,4424 % | 4 040 222 | — |
| Fondo 8,0 % efectivo | 8,0000 % | 4 082 400 | +42 178 |

**Paso 5 — tiempo de duplicación en la mejor opción.**

```text
n = ln(2) / ln(1,08) = 0,693147 / 0,076961 = 9,006 años
regla del 72: 72/8 = 9,0 años   ✔ coincide
```

**Paso 6 — interpreta con límites.** El fondo rinde 42 178 pesos más **si entrega el 8 %**, y ese es
justamente el punto: el depósito tiene tasa contractual conocida y el fondo tiene una expectativa
sujeta a riesgo. Comparar 7,4424 % garantizado contra 8,0 % esperado no es comparar iguales. La
Parte 8, clase 8, formaliza esa asimetría.

## 🏦 Del cliente al banco

| Concepto | En tu vida | En el banco |
|---|---|---|
| Capitalización mensual | "Los intereses se suman cada mes" | Devengo diario, capitalización en fecha de corte, asiento contable |
| Tasa nominal vs. efectiva | "Dicen 12 % pero pago más" | TEA y CAE obligatorias en la información precontractual |
| Regla del 72 | Control mental rápido | Sanidad de una proyección antes de llevarla al comité |
| Deuda que no baja | "Pago y sigo debiendo" | Pago mínimo insuficiente frente al interés devengado; alerta temprana de sobreendeudamiento |

## 🧪 Práctica

En `labs/lab-03.md`, sección de capitalización:

1. Construye la tabla simple vs. compuesto para 1, 5, 10, 20 y 30 años con tres tasas distintas.
2. Calcula el monto final del mismo capital con las seis frecuencias de capitalización.
3. Verifica la regla del 72 contra el cálculo exacto para seis tasas y tabula el error.
4. Simula la deuda de tarjeta con pago mínimo durante 36 meses y grafica el saldo.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| El monto final es mucho menor de lo esperado | Se usó `1 + i·n` en vez de `(1+i)^n` | Verifica si la operación capitaliza; casi todo crédito de cuotas lo hace. |
| Dos ofertas con la misma tasa dan montos distintos | Frecuencias de capitalización distintas | Compara siempre por tasa efectiva anual, nunca por nominal. |
| La tasa mensual se obtuvo dividiendo la efectiva anual por 12 | Confusión nominal/efectiva | Para efectiva: `i_m = (1+TEA)^(1/12) − 1`. Dividir solo aplica a tasas nominales. |
| El plazo calculado da negativo o indefinido | `M < C` o tasa cero en el logaritmo | Revisa los datos: con tasa positiva `M` siempre supera a `C`. |
| Se proyectan 30 años con la tasa actual | Se supuso tasa constante sin declararlo | Toda proyección larga necesita escenarios (Parte 7, clase 13). |
| El interés parece pequeño en el primer año | Solo se miró un periodo | La aceleración es tardía; evalúa el horizonte completo. |

## ❓ Preguntas de comprobación

1. ¿Por qué en el primer periodo el interés simple y el compuesto coinciden?
2. Una tasa nominal de 12 % capitalizada mensualmente, ¿es mejor o peor que 12,5 % efectiva anual?
3. ¿En cuántos años se duplica un capital al 6 %? Resuélvelo con la regla del 72 y exactamente.
4. ¿Por qué dividir la tasa efectiva anual por 12 da un resultado incorrecto?
5. Explica con un ejemplo por qué el interés compuesto es simétrico entre ahorro y deuda.

## 📥 Entregable

Guarda en `portfolio/parte-01/clase-06/`:

- la tabla simple vs. compuesto con la brecha en pesos y en porcentaje;
- la tabla de las seis frecuencias de capitalización con sus tasas efectivas;
- la verificación de la regla del 72 con el error tabulado;
- la simulación de deuda con pago mínimo y una conclusión de 200 palabras.

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

- Kellison, S. (2008). *The Theory of Interest* (3.ª ed.). McGraw-Hill/Irwin. Capítulos 1 y 2: capitalización, frecuencia y capitalización continua.
- Brealey, R., Myers, S. y Allen, F. (2023). *Principios de finanzas corporativas* (14.ª ed.). McGraw-Hill. Capítulo 2: valor futuro y el papel del horizonte temporal.
- Ross, S., Westerfield, R. y Jordan, B. (2022). *Fundamentos de finanzas corporativas* (12.ª ed.). McGraw-Hill. Capítulo 5: interés compuesto y tasas efectivas.
- Bodie, Z., Kane, A. y Marcus, A. (2023). *Investments* (13.ª ed.). McGraw-Hill. Capítulo 5: capitalización continua y rendimientos anualizados.
- OECD/INFE (2022). *Toolkit for Measuring Financial Literacy and Financial Inclusion*. OCDE. El interés compuesto como indicador central de alfabetización financiera.
- Verificación local: confirma cómo debe informarse la tasa efectiva en tu país y si existe obligación de publicar una carga anual equivalente en la oferta de crédito.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 05 · Interés simple](05-interes-simple.md) | [Parte 01](../README.md) · [Programa](../../../SYLLABUS.md) | [07 · Inflación y poder adquisitivo →](07-inflacion-y-poder-adquisitivo.md) |
<!-- gen:footer:end -->
