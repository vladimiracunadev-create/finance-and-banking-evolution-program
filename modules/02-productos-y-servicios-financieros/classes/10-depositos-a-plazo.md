---
part: 3
class: 10
title: "Depósitos a plazo"
level: fundamento
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 10 · Depósitos a plazo

> [← 09 · Crédito hipotecario](09-credito-hipotecario.md) · [Índice de la parte](../README.md) · [11 · Fondos y ahorro previsional →](11-fondos-y-ahorro-previsional.md)

**Parte 03 — Productos y servicios financieros** · **Nivel:** Fundamento — sin conocimientos previos · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Dominar el instrumento de ahorro más simple y más usado, y entender por qué su rentabilidad real
suele ser menor de lo que aparenta. Un depósito a plazo cambia liquidez por tasa; esta clase enseña a
evaluar si ese intercambio conviene, a construir escaleras de vencimientos y a comparar depósitos
nominales con reajustables.

## 📚 Objetivos

Al finalizar podrás:

1. **Calcular** el rendimiento nominal, real y después de impuestos de un depósito.
2. **Comparar** depósitos nominales y reajustables en distintos escenarios de inflación.
3. **Construir** una escalera de vencimientos y explicar qué problema resuelve.
4. **Evaluar** el costo de un rescate anticipado.
5. **Decidir** entre depósito, fondo de liquidez y cuenta de ahorro según el propósito.

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
| `depósito a plazo` | Captación con monto, tasa y plazo pactados. El banco queda debiendo; está cubierto por la garantía de depósitos hasta el límite. |
| `depósito nominal` | Tasa en moneda corriente. El riesgo inflacionario lo asume el depositante. |
| `depósito reajustable` | Expresado en unidad indexada más una tasa real. El riesgo inflacionario lo asume el banco. |
| `renovación automática` | Se renueva al vencimiento a la tasa vigente. Cómodo y frecuentemente desventajoso. |
| `rescate anticipado` | Retiro antes del vencimiento. Habitualmente con pérdida total o parcial de intereses. |
| `escalera de vencimientos` | Varios depósitos con vencimientos escalonados. Combina liquidez periódica con tasas de plazo largo. |
| `rendimiento después de impuestos` | Lo que queda tras la tributación aplicable. Es la única cifra comparable entre instrumentos. |

## 🧠 Modelo mental

Un depósito es un **intercambio explícito**:

```text
entregas   liquidez durante N días
recibes    una tasa mayor que la de una cuenta a la vista
```

La pregunta correcta no es "¿cuánto paga?" sino **"¿cuánto vale para mí la liquidez que entrego?"**.
Si el dinero podría necesitarse antes del vencimiento, la tasa adicional no compensa el riesgo de
rescatar con pérdida de intereses.

## 📖 Desarrollo

### 1. Los tres rendimientos

Depósito de 5 000 000 a 180 días, tasa nominal 5,8 % anual, inflación esperada 4,3 %, impuesto sobre
intereses 10 %.

```text
interés bruto = 5 000 000 × 0,058 × 180/365 = 143 014
impuesto      = 143 014 × 0,10              =  14 301
interés neto                                = 128 713

rendimiento nominal neto del periodo = 128 713/5 000 000 = 2,574 %
anualizado ≈ (1,02574)^(365/180) − 1 = 5,25 %

rendimiento real = (1,0525 / 1,043) − 1 = 0,91 %
```

**De 5,8 % publicado a 0,91 % real después de impuestos.** No hay engaño: hay tres capas que casi
nunca se calculan juntas. El depósito preserva el capital y agrega poco; ese es exactamente su rol.

### 2. Nominal frente a reajustable

Depósito de 5 000 000 a 12 meses:

```text
A  nominal      6,2 % anual
B  reajustable  unidad indexada + 1,8 % anual real
```

| Inflación efectiva | Rendimiento A (real) | Rendimiento B (real) | Mejor |
|---:|---:|---:|---|
| 2,0 % | 4,12 % | 1,80 % | A |
| 4,0 % | 2,12 % | 1,80 % | A |
| 4,4 % | 1,72 % | 1,80 % | B |
| 6,0 % | 0,19 % | 1,80 % | B |
| 9,0 % | −2,57 % | 1,80 % | B |

El punto de indiferencia está en una inflación de **4,3 %**. El depósito nominal gana si la inflación
resulta menor que la esperada por el mercado, y el reajustable gana si resulta mayor. Elegir entre
ambos es, en el fondo, tomar posición sobre la inflación futura —y conviene saber que se está haciendo.

### 3. Escalera de vencimientos

Problema: 12 000 000 disponibles; se necesita liquidez trimestral eventual, pero los plazos largos
pagan más.

```text
CONSTRUCCIÓN (año 1)
  3 000 000 a  3 meses    tasa 5,1 %
  3 000 000 a  6 meses    tasa 5,5 %
  3 000 000 a  9 meses    tasa 5,7 %
  3 000 000 a 12 meses    tasa 6,2 %
  tasa promedio ponderada 5,625 %

RÉGIMEN (año 2 en adelante)
  cada vencimiento se renueva a 12 meses
  → un depósito vence cada 3 meses
  → todos rinden la tasa de 12 meses: 6,2 %
```

| Estrategia | Tasa promedio | Liquidez | Riesgo de reinversión |
|---|---:|---|---|
| Todo a 3 meses | 5,1 % | Cada 3 meses | Alto (renovación completa) |
| Todo a 12 meses | 6,2 % | Anual | Concentrado en una fecha |
| Escalera | 6,2 % en régimen | Cada 3 meses | Diversificado |

La escalera entrega la tasa del plazo largo con la liquidez del plazo corto, a cambio de un año de
construcción. Es la misma técnica de calce de plazos que usa la tesorería bancaria (Parte 10, clase 12).

### 4. Rescate anticipado

```text
depósito 5 000 000 a 360 días al 6,2 %
rescate al día 200:
  interés devengado teórico = 5 000 000 × 0,062 × 200/365 = 169 863
  condición contractual típica: pérdida total o parcial de intereses
  escenario habitual: se devuelve el capital sin intereses o con tasa de cuenta vista
  pérdida = hasta 169 863
```

La pérdida no es una penalidad arbitraria: el depósito es un contrato de plazo, y el banco calzó ese
plazo en su balance. La consecuencia práctica: **nunca deposites a plazo dinero que podrías
necesitar**, y si hay duda, divide el monto para rescatar solo una parte.

### 5. Elegir instrumento por propósito

| Propósito | Instrumento | Razón |
|---|---|---|
| Fondo de emergencia | Fondo de liquidez o cuenta de ahorro | Disponibilidad en 24–48 h |
| Meta con fecha conocida a 6–24 meses | Depósito al plazo exacto | Tasa cierta, sin riesgo de mercado |
| Excedente sin destino, con incertidumbre | Escalera | Liquidez periódica sin sacrificar tasa |
| Protección ante inflación alta | Depósito reajustable | Traslada el riesgo inflacionario |
| Horizonte superior a 3 años | Otras alternativas (Parte 8) | El depósito rara vez gana a la inflación en el largo plazo |

## 🧮 Ejemplo guiado

**Situación.** Elena recibe una indemnización de 18 000 000. Necesitará 6 000 000 en 8 meses para una
matrícula; el resto no tiene destino definido y podría usarse en 1 a 3 años. Inflación esperada 4,2 %,
impuesto sobre intereses 10 %.

Ofertas: 90 días 4,9 % · 180 días 5,4 % · 360 días 6,1 % · reajustable 12 meses UF + 1,7 %.

**Paso 1 — separa por propósito.**

```text
6 000 000  destino cierto en 8 meses → plazo calzado
12 000 000 destino incierto 1–3 años → escalera + protección inflacionaria
```

**Paso 2 — los 6 000 000 a 8 meses.** No hay plazo de 240 días; dos opciones:

```text
opción 1: 180 días al 5,4 % + 60 días al 4,9 %
  interés 180 d = 6 000 000 × 0,054 × 180/365 = 159 780
  capital al día 180 = 6 159 780
  interés 60 d = 6 159 780 × 0,049 × 60/365 = 49 610
  total bruto = 209 390 → neto 188 451

opción 2: 360 días al 6,1 % con rescate al día 240 → pérdida de intereses
  DESCARTADA: el rescate anticipado anula la ventaja
```

**Paso 3 — los 12 000 000 en escalera.**

```text
3 000 000 a  90 días  4,9 %
3 000 000 a 180 días  5,4 %
3 000 000 a 270 días  5,8 % (estimado)
3 000 000 a 360 días  6,1 %
tasa promedio ponderada 5,55 % → en régimen, 6,1 %
```

**Paso 4 — evalúa la alternativa reajustable para una parte.**

```text
punto de indiferencia: 6,1 % nominal vs. UF + 1,7 %
  (1,061 / (1 + π)) − 1 = 0,017  →  π = 4,33 %
```

Si Elena cree que la inflación superará 4,33 %, conviene el reajustable. Decisión razonable:
**dividir**, colocando 6 000 000 de la escalera en reajustable, lo que reduce la exposición a un
escenario inflacionario sin apostar todo a una sola visión.

**Paso 5 — rendimiento real esperado del conjunto.**

```text
nominal ponderado ≈ 5,9 %
neto de impuesto  ≈ 5,3 %
real (π = 4,2 %)  ≈ 1,06 %
```

**Paso 6 — interpreta con honestidad.** Los 18 000 000 de Elena, colocados con criterio, rendirán
alrededor de **1 % real anual**. Eso es lo que un depósito puede entregar, y está bien: su función es
**preservar** el capital con certeza, no hacerlo crecer. Si Elena necesita crecimiento real, el
instrumento correcto no es el depósito, y esa conversación pertenece a la Parte 8. Confundir ambas
funciones es la causa de dos errores opuestos: esperar rentabilidad de un depósito, o exigir seguridad
de una inversión.

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| Depósito a plazo | Fondeo estable con vencimiento conocido | 10, clase 2 |
| Renovación automática | Retención de fondeo a bajo costo de gestión | 15, clase 7 |
| Rescate anticipado | Descalce imprevisto; por eso la penalización | 11, clase 4 |
| Depósito reajustable | El banco asume el riesgo inflacionario y lo calza | 11, clase 5 |
| Garantía de depósitos | Reduce el riesgo de retiro masivo | 11, clase 4 |

## 🧪 Práctica

En `labs/lab-05.md`, sección de depósitos:

1. Calcula los tres rendimientos (nominal, neto de impuestos, real) de tres ofertas reales.
2. Determina el punto de indiferencia entre un depósito nominal y uno reajustable.
3. Construye una escalera de cuatro tramos y proyecta su tasa en régimen.
4. Cuantifica el costo de un rescate anticipado según el contrato vigente.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| El rendimiento real decepciona | Solo se miró la tasa nominal | Calcula neto de impuestos y descuenta inflación. |
| Se pierde todo el interés al rescatar | Se depositó dinero necesario | Deposita solo excedente con plazo calzado. |
| La renovación quedó a tasa baja | Renovación automática sin revisar | Revisa la tasa en cada vencimiento. |
| Todo el capital vence el mismo día | Concentración de riesgo de reinversión | Usa escalera. |
| Se elige reajustable sin criterio | No se calculó el punto de indiferencia | Compara contra tu expectativa de inflación. |
| Se espera rentabilidad de un depósito | Función del instrumento mal entendida | El depósito preserva; no hace crecer. |

## ❓ Preguntas de comprobación

1. Calcula el rendimiento real después de impuestos de un depósito al 6 % con inflación de 4,5 %.
2. ¿Cuándo conviene un depósito reajustable frente a uno nominal?
3. ¿Qué problema resuelve una escalera de vencimientos y cuánto tarda en entrar en régimen?
4. ¿Por qué la penalización por rescate anticipado no es arbitraria?
5. ¿Cuál es la función propia de un depósito a plazo y cuál no lo es?

## 📥 Entregable

Guarda en `portfolio/parte-03/clase-10/`:

- los tres rendimientos calculados de tres ofertas reales con fecha;
- el punto de indiferencia nominal vs. reajustable y tu decisión;
- la escalera diseñada con su calendario y tasa en régimen;
- el costo documentado de un rescate anticipado según contrato.

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

- Rose, P. y Hudgins, S. (2013). *Bank Management & Financial Services* (9.ª ed.). McGraw-Hill. Capítulo 12: productos de depósito a plazo y su fijación de precio.
- Bodie, Z., Kane, A. y Marcus, A. (2023). *Investments* (13.ª ed.). McGraw-Hill. Capítulo 2: instrumentos del mercado monetario y escaleras de vencimiento.
- Mishkin, F. (2022). *The Economics of Money, Banking and Financial Markets* (13.ª ed.). Pearson. Capítulo 4: rendimiento nominal y real de instrumentos de deuda.
- Fisher, I. (1930). *The Theory of Interest*. Macmillan. Relación entre tasa nominal, real e inflación esperada.
- International Association of Deposit Insurers (2014). *Core Principles for Effective Deposit Insurance Systems*. IADI/BIS. Cobertura aplicable a depósitos a plazo.
- Verificación local: consulta las tasas de captación vigentes publicadas por el supervisor de tu país, el tratamiento tributario de los intereses y el límite de la garantía de depósitos.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 09 · Crédito hipotecario](09-credito-hipotecario.md) | [Parte 03](../README.md) · [Programa](../../../SYLLABUS.md) | [11 · Fondos y ahorro previsional →](11-fondos-y-ahorro-previsional.md) |
<!-- gen:footer:end -->
