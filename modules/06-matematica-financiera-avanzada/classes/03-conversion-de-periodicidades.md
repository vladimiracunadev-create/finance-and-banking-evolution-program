---
part: 7
class: 3
title: "Conversión de periodicidades"
level: avanzado
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 03 · Conversión de periodicidades

> [← 02 · Tasas equivalentes](02-tasas-equivalentes.md) · [Índice de la parte](../README.md) · [04 · Anualidades vencidas →](04-anualidades-vencidas.md)

**Parte 07 — Matemática financiera avanzada** · **Nivel:** Avanzado — perfil analista · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Resolver el problema práctico que aparece en toda operación real: los flujos no siempre ocurren con la
misma frecuencia que la tasa cotizada. Un crédito con cuotas trimestrales y tasa mensual, un
arrendamiento con pagos irregulares, un bono con cupones semestrales y tasa anual. Esta clase entrega
el procedimiento sistemático para resolver cualquiera de esos casos.

## 📚 Objetivos

Al finalizar podrás:

1. **Aplicar** el procedimiento de tres pasos para cualquier desalineación de periodicidades.
2. **Resolver** operaciones con flujos irregulares en el tiempo.
3. **Manejar** periodos fraccionarios sin aproximar.
4. **Construir** un eje de tiempo con la periodicidad correcta.
5. **Verificar** un resultado mediante recomposición del flujo.

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
| `periodicidad de la tasa` | Frecuencia con que la tasa capitaliza. |
| `periodicidad del flujo` | Frecuencia con que ocurren los pagos. |
| `desalineación` | Cuando ambas no coinciden. Es la situación normal, no la excepción. |
| `periodo de referencia` | Unidad temporal elegida para el cálculo. Debe ser la del flujo. |
| `periodo fraccionario` | Plazo que no es múltiplo entero del periodo de referencia. |
| `recomposición` | Verificación reconstruyendo el flujo desde el resultado. |

## 🧠 Modelo mental

El procedimiento es siempre el mismo:

```text
1. elige el PERIODO DE REFERENCIA = la periodicidad del FLUJO
2. convierte la TASA a ese periodo (clase 2)
3. opera normalmente
```

El error universal es el inverso: intentar convertir los flujos a la periodicidad de la tasa. Los
flujos ocurren cuando ocurren; **la tasa es la que se adapta**.

## 📖 Desarrollo

### 1. El procedimiento, caso por caso

**Caso A — tasa mensual, flujos trimestrales:**

```text
tasa: 1,4 % mensual
flujos: cada 3 meses

periodo de referencia = trimestre
i_trimestral = (1,014)^3 − 1 = 4,2588 %
```

**Caso B — TEA, flujos mensuales:**

```text
tasa: 16 % efectivo anual
flujos: mensuales

i_mensual = (1,16)^(1/12) − 1 = 1,2445 %
```

**Caso C — tasa nominal semestral, flujos trimestrales:**

```text
tasa: 14 % nominal capitalizable semestral → i_semestral = 7 %
flujos: trimestrales

i_trimestral = (1,07)^(1/2) − 1 = 3,4408 %
```

**Caso D — tasa mensual, flujos cada 45 días:**

```text
tasa: 1,1 % mensual
periodo de referencia = 45 días = 1,5 meses

i_45 = (1,011)^1,5 − 1 = 1,6545 %
```

### 2. Flujos irregulares

Cuando los flujos no tienen periodicidad fija, se trabaja **en días**:

```text
i_diaria = (1 + TEA)^(1/365) − 1
factor de descuento del flujo t = (1 + i_diaria)^(−días_t)
```

Ejemplo:

```text
TEA 13 %  →  i_diaria = (1,13)^(1/365) − 1 = 0,0334855 %

Flujo      Fecha       Días desde hoy   Factor            Valor presente
2 000 000  15-mar               42      0,986017          1 972 034
3 500 000  08-jun              127      0,958290          3 354 015
1 800 000  22-sep              233      0,924554          1 664 197
5 200 000  30-dic              332      0,894244          4 650 069
                                        TOTAL VP         11 640 315
```

Este método —descontar por días exactos— es el que usan los sistemas de tesorería y el que evita los
errores de aproximar meses de 30 días.

### 3. Periodos fraccionarios

Dos convenciones para un plazo que incluye una fracción de periodo:

```text
convención EXPONENCIAL (compuesta):  M = C (1 + i)^n     con n fraccionario
convención LINEAL (mixta):           M = C (1 + i)^⌊n⌋ × (1 + i × fracción)
```

```text
C = 10 000 000 · i = 2 % mensual · n = 5,4 meses

exponencial: 10 000 000 × (1,02)^5,4 = 11 133 456
lineal:      10 000 000 × (1,02)^5 × (1 + 0,02 × 0,4) = 11 129 396

diferencia: 4 060
```

La convención debe declararse en el contrato. La exponencial es la matemáticamente consistente; la
lineal se usa por tradición en algunos mercados y **siempre produce un monto menor** para fracciones
positivas.

### 4. Construir el eje de tiempo

Reglas que evitan la mayoría de los errores:

```text
1. el periodo 0 es la fecha de la operación, no el primer pago
2. si el primer flujo ocurre al final del primer periodo, va en t = 1
3. si el primer flujo ocurre al inicio, va en t = 0 (anualidad anticipada, clase 5)
4. si hay un periodo de gracia, los primeros periodos tienen flujo cero
5. todos los flujos deben estar en la misma periodicidad de referencia
```

Ejemplo con gracia:

```text
crédito de 20 000 000, tasa 1,3 % mensual
3 meses de gracia total, luego 24 cuotas mensuales

  0    1    2    3    4    5   ...  27
  |----|----|----|----|----|--- ... --|
+20M   0    0    0    A    A         A

saldo al mes 3 = 20 000 000 × (1,013)^3 = 20 790 233
cuota = 20 790 233 × 0,013 × (1,013)^24 / ((1,013)^24 − 1) = 1 016 200
```

### 5. Verificación por recomposición

Todo resultado debe verificarse reconstruyendo el flujo:

```text
capital 20 790 233 al mes 3
cuota 1 016 200 durante 24 meses

mes 4:  interés 270 273 · amortización 745 927 · saldo 20 044 306
mes 5:  interés 260 576 · amortización 755 624 · saldo 19 288 682
...
mes 27: interés  13 049 · amortización 1 003 151 · saldo 0  ✔
```

Si el saldo final no es cero (salvo el ajuste de centavos), la conversión de periodicidad fue
incorrecta.

## 🧮 Ejemplo guiado

**Situación.** Estructura una operación de leasing con estas condiciones:

```text
valor del equipo             48 000 000
tasa cotizada                14,5 % nominal capitalizable semestral
pagos                        trimestrales, vencidos
plazo                        4 años
pago inicial                 15 % del valor, al momento de la firma
valor residual (opción)      8 % del valor, pagadero al final
```

**Paso 1 — periodo de referencia y tasa.**

```text
periodo de referencia = trimestre (periodicidad del flujo)
i_semestral = 14,5 %/2 = 7,25 %
i_trimestral = (1,0725)^(1/2) − 1 = 3,5617 %
```

**Paso 2 — monto a financiar.**

```text
pago inicial = 48 000 000 × 0,15 = 7 200 000
monto financiado = 48 000 000 − 7 200 000 = 40 800 000
```

**Paso 3 — descuenta el valor residual.**

```text
valor residual = 48 000 000 × 0,08 = 3 840 000, pagadero en el trimestre 16
VP del residual = 3 840 000 / (1,035617)^16 = 3 840 000 / 1,750434 = 2 193 748

monto a amortizar en cuotas = 40 800 000 − 2 193 748 = 38 606 252
```

**Paso 4 — cuota trimestral.**

```text
n = 16 trimestres
(1,035617)^16 = 1,750434

cuota = 38 606 252 × 0,035617 × 1,750434 / (1,750434 − 1)
      = 38 606 252 × 0,062338 / 0,750434
      = 2 406 726 / 0,750434 = 3 207 132
```

**Paso 5 — construye el eje de tiempo completo.**

```text
  t=0     t=1      t=2     ...    t=16
   |-------|--------|------ ... ----|
 −7 200 000  ...                    
 +48 000 000 equipo recibido
          −3 207 132 cada trimestre
                                −3 840 000 (residual)
```

**Paso 6 — verifica con el valor presente completo.**

```text
VP de las cuotas = 3 207 132 × [1 − (1,035617)^-16] / 0,035617
                 = 3 207 132 × [1 − 0,571287] / 0,035617
                 = 3 207 132 × 12,03672 = 38 601 900

VP total = 7 200 000 (inicial) + 38 601 900 (cuotas) + 2 193 748 (residual)
         = 47 995 648 ≈ 48 000 000  ✔ (diferencia por redondeo)
```

**Paso 7 — la TEA efectiva de la operación.**

```text
TEA = (1,035617)^4 − 1 = 15,0256 %
```

Nótese que la cotización decía 14,5 %: **la TEA real es 15,03 %**, medio punto más, por la
capitalización semestral.

**Interpreta:** la operación involucró tres desalineaciones simultáneas —tasa semestral, flujos
trimestrales, valor residual al vencimiento— y el procedimiento de tres pasos las resolvió sin
ambigüedad. **La verificación del paso 6 es obligatoria**: si el valor presente total no reproduce el
valor del equipo, hay un error en alguna conversión.

## 🏦 Del cliente al banco

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| Conversión de periodicidad | Estructuración de operaciones | 13, clase 8 |
| Descuento por días exactos | Valoración de cartera y de tesorería | 10, clase 12 |
| Valor residual | Leasing y su estructura | 13, clase 8 |
| Periodo de gracia | Créditos de proyecto | 13, clase 4 |
| Verificación por recomposición | Control de calidad del cálculo | 1, clase 13 |

## 🧪 Práctica

En `labs/lab-02.md`:

1. Resuelve seis casos de desalineación de periodicidades con el procedimiento de tres pasos.
2. Descuenta un flujo irregular por días exactos y verifica el resultado.
3. Compara la convención exponencial y la lineal en cuatro periodos fraccionarios.
4. Estructura una operación de leasing completa con verificación por valor presente.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se convierten los flujos a la periodicidad de la tasa | Procedimiento invertido | La tasa se adapta al flujo, no al revés. |
| El saldo final no cierra en cero | Conversión incorrecta | Verifica por recomposición. |
| Se usan meses de 30 días para flujos irregulares | Aproximación indebida | Descuenta por días exactos. |
| Se ignora la convención de periodo fraccionario | No declarada | Acuérdala y decláralas en el contrato. |
| El valor residual no se descuenta | Se sumó al capital sin traer a valor presente | Descuéntalo al periodo en que ocurre. |
| Se aplica la tasa cotizada como efectiva | Frecuencia ignorada | Convierte primero (clase 1). |

## ❓ Preguntas de comprobación

1. ¿Cuál es el procedimiento de tres pasos ante una desalineación?
2. Convierte 12 % nominal capitalizable trimestral a una tasa para flujos bimestrales.
3. ¿Cómo se descuentan flujos que no tienen periodicidad fija?
4. ¿Qué diferencia hay entre la convención exponencial y la lineal, y cuál da mayor monto?
5. ¿Cómo verificas que la conversión de periodicidad fue correcta?

## 📥 Entregable

Guarda en `portfolio/parte-07/clase-03/`:

- los seis casos de desalineación resueltos con el procedimiento;
- el flujo irregular descontado por días exactos con su verificación;
- la comparación de convenciones en cuatro periodos fraccionarios;
- la operación de leasing estructurada con la verificación por valor presente y su TEA.

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

- Broverman, S. (2017). *Mathematics of Investment and Credit* (7.ª ed.). ACTEX. Capítulos 1 y 2: conversión de periodicidades y periodos fraccionarios.
- Kellison, S. (2008). *The Theory of Interest* (3.ª ed.). McGraw-Hill/Irwin. Capítulo 2: ecuaciones de valor con flujos irregulares.
- Fabozzi, F. (2021). *Bond Markets, Analysis, and Strategies* (10.ª ed.). MIT Press. Capítulo 2: convenciones de conteo y descuento por días.
- IFRS Foundation. *NIIF 16 Arrendamientos*: medición del pasivo por arrendamiento y valor residual. <https://www.ifrs.org/>
- Benninga, S. (2014). *Financial Modeling* (4.ª ed.). MIT Press. Implementación de descuento por días exactos.
- Verificación local: revisa qué convención de periodo fraccionario y qué base de días exige la normativa de tu país en operaciones de crédito y de leasing.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 02 · Tasas equivalentes](02-tasas-equivalentes.md) | [Parte 07](../README.md) · [Programa](../../../SYLLABUS.md) | [04 · Anualidades vencidas →](04-anualidades-vencidas.md) |
<!-- gen:footer:end -->
