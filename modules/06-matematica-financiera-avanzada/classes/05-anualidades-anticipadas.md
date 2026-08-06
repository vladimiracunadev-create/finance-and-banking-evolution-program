---
part: 7
class: 5
title: "Anualidades anticipadas"
level: avanzado
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 05 · Anualidades anticipadas

> [← 04 · Anualidades vencidas](04-anualidades-vencidas.md) · [Índice de la parte](../README.md) · [06 · Perpetuidades →](06-perpetuidades.md)

**Parte 07 — Matemática financiera avanzada** · **Nivel:** Avanzado — perfil analista · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Manejar la variante donde los pagos ocurren al **inicio** de cada periodo, que es la estructura de los
arriendos, los seguros, muchos leasing y los aportes de ahorro programado. La diferencia con la
anualidad vencida es un solo factor `(1+i)`, y su omisión produce errores sistemáticos de un periodo
completo de interés.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** anualidad vencida de anticipada por la ubicación del primer flujo.
2. **Aplicar** las fórmulas de anualidad anticipada y su relación con la vencida.
3. **Cuantificar** el efecto de la anticipación sobre el valor y sobre la cuota.
4. **Resolver** casos reales: arriendos, seguros, leasing y ahorro programado.
5. **Detectar** en un contrato cuál de las dos estructuras se está aplicando.

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
| `anualidad anticipada` | Pagos al **inicio** de cada periodo. El primero ocurre en `t = 0`. |
| `factor anticipado` | `ä(n,i) = a(n,i) × (1+i)`. Un factor `(1+i)` mayor que el vencido. |
| `relación de cuotas` | Para el mismo valor presente, la cuota anticipada es `A_venc / (1+i)`. |
| `último periodo` | En la anticipada, el último pago ocurre en `t = n−1`, no en `t = n`. |
| `estructura del contrato` | Determina cuál se aplica. Debe verificarse, no suponerse. |

## 🧠 Modelo mental

La diferencia es **un periodo de adelanto en cada pago**:

```text
VENCIDA      0    1    2    3  ...  n
                  A    A    A       A

ANTICIPADA   0    1    2    3  ...  n
             A    A    A    A       (nada en n)
```

Cada pago ocurre un periodo antes, de modo que gana un periodo de interés. De ahí que todo el valor
presente se multiplique por `(1+i)`.

## 📖 Desarrollo

### 1. Las fórmulas

```text
VP anticipada = A × [1 − (1+i)^-n]/i × (1+i)  =  A × ä(n,i)
VF anticipada = A × [(1+i)^n − 1]/i × (1+i)   =  A × s̈(n,i)

ä(n,i) = a(n,i) × (1+i)
s̈(n,i) = s(n,i) × (1+i)
```

Formulación alternativa, a veces más intuitiva:

```text
ä(n,i) = 1 + a(n−1, i)
```

Es decir: el primer pago no se descuenta (vale 1) y los `n−1` restantes forman una anualidad vencida.

### 2. Efecto cuantificado

```text
A = 500 000 · i = 1,2 % · n = 36

vencida:     VP = 500 000 × 29,17419 = 14 587 095
anticipada:  VP = 14 587 095 × 1,012 = 14 762 140

diferencia = 175 045 (1,2 %, exactamente la tasa de un periodo)
```

Y en sentido inverso, para el mismo valor presente:

```text
VP = 14 587 095 · i = 1,2 % · n = 36

cuota vencida    = 500 000
cuota anticipada = 500 000 / 1,012 = 494 071

diferencia = 5 929 por cuota → 213 444 en total
```

**La regla:** pagar al inicio permite una cuota menor para el mismo capital, o financia más capital
con la misma cuota.

### 3. Casos reales

| Operación | Estructura | Razón |
|---|---|---|
| Arriendo de inmueble | Anticipada | Se paga por el mes que comienza |
| Prima de seguro | Anticipada | Se paga por la cobertura futura |
| Leasing operativo | Habitualmente anticipada | Se paga por el uso del periodo |
| Crédito de consumo | Vencida | Se paga al final del mes transcurrido |
| Depósito programado | Anticipada | Se aporta al inicio |
| Cupón de bono | Vencida | Se paga por el periodo transcurrido |
| Sueldo | Vencida | Se paga por el trabajo realizado |

La consecuencia práctica: **al valorar un contrato de arriendo hay que usar la fórmula anticipada**, y
usar la vencida subestima el valor presente en un `(1+i)` completo.

### 4. Anualidad anticipada diferida

```text
VP = A × ä(n,i) × (1+i)^-k
```

```text
leasing con 3 meses de gracia y 24 cuotas anticipadas de 850 000, i = 1,05 %

a(24) = [1 − (1,0105)^-24]/0,0105 = 21,1246
ä(24) = 21,1246 × 1,0105 = 21,3464
VP = 850 000 × 21,3464 × (1,0105)^-3
   = 850 000 × 21,3464 × 0,969122
   = 850 000 × 20,6873 = 17 584 205
```

### 5. Detectar la estructura en un contrato

```text
señales de anualidad ANTICIPADA:
  · "el primer pago se efectuará a la firma del contrato"
  · "las rentas se pagarán por adelantado, dentro de los primeros 5 días"
  · el número de pagos es igual al número de periodos y el último cae antes del vencimiento

señales de anualidad VENCIDA:
  · "el primer pago se efectuará a los 30 días de la firma"
  · "los intereses se devengan y pagan al vencimiento de cada periodo"
  · el último pago coincide con el término del contrato
```

Ante duda, la prueba definitiva es la **tabla de desarrollo**: si el primer pago aparece en la fila 0 o
si la fila 1 tiene interés cero, es anticipada.

## 🧮 Ejemplo guiado

**Situación.** Una empresa evalúa dos ofertas para el mismo equipo industrial.

```text
OFERTA A — compra financiada
  precio                    72 000 000
  pie                       20 % al contado
  saldo en 48 cuotas mensuales VENCIDAS
  tasa                      1,08 % mensual

OFERTA B — leasing operativo
  36 cuotas mensuales ANTICIPADAS de 1 950 000
  opción de compra al final: 18 000 000
  sin pie
```

La empresa descuenta a 1,15 % mensual (su costo de capital).

**Paso 1 — flujo de la oferta A.**

```text
pie = 72 000 000 × 0,20 = 14 400 000
saldo financiado = 57 600 000

(1,0108)^48 = 1,674247
cuota = 57 600 000 × 0,0108 × 1,674247/(1,674247 − 1)
      = 57 600 000 × 0,018082/0,674247 = 1 041 523/0,674247 = 1 544 723
```

**Paso 2 — valor presente de A a la tasa de la empresa (1,15 %).**

```text
a(48; 1,15%) = [1 − (1,0115)^-48]/0,0115
(1,0115)^48 = 1,726246 → (1,0115)^-48 = 0,579292
a(48) = (1 − 0,579292)/0,0115 = 36,5833

VP(A) = 14 400 000 + 1 544 723 × 36,5833 = 14 400 000 + 56 505 090 = 70 905 090
```

**Paso 3 — valor presente de B.**

```text
a(36; 1,15%) = [1 − (1,0115)^-36]/0,0115
(1,0115)^36 = 1,510437 → (1,0115)^-36 = 0,662062
a(36) = (1 − 0,662062)/0,0115 = 29,3859
ä(36) = 29,3859 × 1,0115 = 29,7238

VP cuotas = 1 950 000 × 29,7238 = 57 961 410
VP opción = 18 000 000 × 0,662062 = 11 917 116
VP(B) = 69 878 526
```

**Paso 4 — compara.**

| Oferta | Valor presente | Diferencia |
|---|---:|---:|
| B — leasing | 69 878 526 | — |
| A — compra financiada | 70 905 090 | +1 026 564 |

**B es mejor por 1 026 564** en valor presente.

**Paso 5 — el efecto de haber usado la fórmula equivocada.**

```text
si B se hubiera valorado con la fórmula VENCIDA:
  VP cuotas = 1 950 000 × 29,3859 = 57 302 505
  VP(B) = 69 219 621
  diferencia con A = 1 685 469
```

El error habría **exagerado la ventaja de B en 658 905**, un 64 % más. La conclusión cualitativa no
cambia en este caso, y en una comparación más ajustada podría invertirse.

**Paso 6 — factores no financieros que completan la decisión.**

```text
· en A la empresa es propietaria desde el inicio: el activo entra al balance y se deprecia
· en B, bajo NIIF 16, también se reconoce un activo por derecho de uso y un pasivo
· A no tiene restricciones de uso; B suele tener límites de horas o de mantención
· B transfiere el riesgo de valor residual al arrendador si no se ejerce la opción
· A exige 14 400 000 de caja inmediata; B no exige pie
```

**Interpreta:** la comparación financiera favorece a B por 1,03 millones, **y la restricción de caja
del pie es probablemente el factor decisivo** para una empresa con capital de trabajo ajustado. La
matemática ordena; el contexto decide, y el rol del analista es entregar ambos elementos.

## 🏦 Del cliente al banco

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| Anualidad anticipada | Valoración de leasing y arriendos | 13, clase 8 |
| Diferencia de un periodo | Efecto material en operaciones largas | 13, clase 8 |
| Estructura del contrato | Determina la fórmula aplicable | 4, clase 8 |
| Opción de compra | Flujo terminal a descontar | 13, clase 8 |
| Comparación de estructuras | Valor presente a la tasa del cliente | 7, clase 8 |

## 🧪 Práctica

En `labs/lab-03.md`:

1. Calcula el valor presente y futuro de cinco anualidades en ambas modalidades y tabula la diferencia.
2. Determina la cuota anticipada equivalente a una vencida para el mismo capital.
3. Valora un contrato de arriendo real con la fórmula correcta.
4. Compara una compra financiada y un leasing con opción de compra, con verificación.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se subestima el valor de un arriendo | Se usó la fórmula vencida | Los arriendos son anticipados. |
| El número de pagos no coincide con el plazo | Confusión de estructura | En anticipada el último pago va en `t = n−1`. |
| Se omite el factor `(1+i)` | Fórmula incompleta | `ä = a × (1+i)`. |
| Se supone la estructura sin leer el contrato | Verificación omitida | Busca cuándo ocurre el primer pago. |
| La opción de compra no se descuenta | Flujo terminal olvidado | Descuéntala al periodo en que se paga. |
| Se comparan estructuras sin usar la misma tasa | Bases distintas | Descuenta ambas a la tasa del decisor. |

## ❓ Preguntas de comprobación

1. ¿Cuál es la única diferencia entre las fórmulas vencida y anticipada?
2. Para el mismo capital, ¿cuánto menor es la cuota anticipada?
3. Nombra cuatro operaciones reales con estructura anticipada.
4. ¿Cómo detectas en un contrato cuál estructura se aplica?
5. ¿Qué error se comete al valorar un arriendo con la fórmula vencida?

## 📥 Entregable

Guarda en `portfolio/parte-07/clase-05/`:

- la tabla comparativa de cinco anualidades en ambas modalidades;
- el cálculo de cuota anticipada equivalente con su verificación;
- la valoración de un contrato de arriendo real con la fórmula correcta;
- la comparación compra vs. leasing con el efecto del error de fórmula cuantificado.

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

- Kellison, S. (2008). *The Theory of Interest* (3.ª ed.). McGraw-Hill/Irwin. Capítulo 3: anualidades anticipadas y su relación con las vencidas.
- Broverman, S. (2017). *Mathematics of Investment and Credit* (7.ª ed.). ACTEX. Capítulo 2: notación actuarial de anualidades.
- IFRS Foundation. *NIIF 16 Arrendamientos*: medición inicial del pasivo por arrendamiento con pagos anticipados. <https://www.ifrs.org/>
- Ross, S., Westerfield, R. y Jordan, B. (2022). *Fundamentos de finanzas corporativas* (12.ª ed.). McGraw-Hill. Capítulo 5: anualidades anticipadas.
- Brealey, R., Myers, S. y Allen, F. (2023). *Principios de finanzas corporativas* (14.ª ed.). McGraw-Hill. Capítulo 25: arrendamiento frente a compra.
- Verificación local: revisa cómo se documenta la periodicidad de pago en los contratos de leasing de tu mercado y qué exige la norma contable aplicable.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 04 · Anualidades vencidas](04-anualidades-vencidas.md) | [Parte 07](../README.md) · [Programa](../../../SYLLABUS.md) | [06 · Perpetuidades →](06-perpetuidades.md) |
<!-- gen:footer:end -->
