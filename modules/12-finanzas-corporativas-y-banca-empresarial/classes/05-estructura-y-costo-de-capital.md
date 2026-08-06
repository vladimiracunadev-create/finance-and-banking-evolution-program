---
part: 13
class: 5
title: "Estructura y costo de capital"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 05 · Estructura y costo de capital

> [← 04 · Capital de trabajo y financiamiento de corto plazo](04-capital-de-trabajo-y-corto-plazo.md) · [Índice de la parte](../README.md) · [06 · Decisiones de inversión →](06-decisiones-de-inversion.md)

**Parte 13 — Finanzas corporativas y banca empresarial** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Determinar cuánta deuda debe tener una empresa y qué le cuesta financiarse. Es la decisión que más
afecta al valor de una empresa después de sus decisiones operativas, y la que el banco necesita
entender para saber si su crédito está sosteniendo un negocio o inflando un riesgo.

## 📚 Objetivos

Al finalizar podrás:

1. **Calcular** el costo promedio ponderado de capital y sus componentes.
2. **Explicar** el efecto del escudo fiscal y sus límites.
3. **Aplicar** la teoría del equilibrio y la de la jerarquía de preferencias.
4. **Estimar** la estructura óptima de capital de una empresa concreta.
5. **Reconocer** las señales que envía una decisión de financiamiento.

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
| `costo de la deuda` | Tasa que la empresa paga, después de impuestos. |
| `costo del patrimonio` | Retorno exigido por los accionistas. |
| `costo promedio ponderado` | Media ponderada de ambos, por su peso en la estructura. |
| `escudo fiscal` | Ahorro de impuestos por la deducibilidad de intereses. |
| `costo de dificultades financieras` | Pérdida de valor por el riesgo de insolvencia. |
| `teoría del equilibrio` | La estructura óptima equilibra escudo fiscal y costos de insolvencia. |
| `jerarquía de preferencias` | Orden observado: caja propia, deuda, capital. |
| `efecto señal` | Información que el mercado infiere de la decisión de financiamiento. |

## 🧠 Modelo mental

```text
LA DEUDA TIENE DOS EFECTOS OPUESTOS SOBRE EL VALOR

  ESCUDO FISCAL           +  los intereses son deducibles
                             el Estado financia parte del costo

  DIFICULTADES FINANCIERAS −  a más deuda, más probabilidad
                             de insolvencia, y esa probabilidad
                             tiene costo antes de materializarse

VALOR = valor sin deuda + valor del escudo − costo esperado de dificultades

la estructura óptima está donde la derivada se anula:
donde el escudo marginal iguala al costo marginal de dificultades
```

**Los costos de dificultades financieras empiezan mucho antes de la quiebra.** Un cliente que duda de la
continuidad de su proveedor busca alternativas; un empleado clave se va; los proveedores acortan los
plazos. Esos costos son reales y ocurren con la empresa todavía solvente.

## 📖 Desarrollo

### 1. Costo de la deuda

```text
COSTO DE LA DEUDA DESPUÉS DE IMPUESTOS
  kd × (1 − t)

  kd  tasa efectiva que la empresa paga
  t   tasa de impuesto a la renta

EJEMPLO
  tasa 10,4 %, impuesto 27 %
  costo después de impuestos: 10,4 % × 0,73 = 7,59 %
```

```text
CÓMO ESTIMAR kd
  · si la empresa emite bonos: el rendimiento al vencimiento
  · si tiene crédito bancario: la tasa efectiva de su deuda
  · si no tiene deuda: tasa libre de riesgo + diferencial
    por su calificación estimada

NO uses la tasa histórica de deudas antiguas:
el costo relevante es el MARGINAL, el de la próxima unidad de deuda
```

### 2. Costo del patrimonio

```text
MODELO DE VALORACIÓN DE ACTIVOS DE CAPITAL

  ke = rf + β × (rm − rf)   [+ primas adicionales]

  rf      tasa libre de riesgo
  β       sensibilidad al mercado
  rm − rf prima de riesgo de mercado
```

| Prima adicional | Cuándo se añade | Rango típico |
|---|---|---|
| Riesgo país | Empresa en economía emergente | Diferencial soberano |
| Tamaño | Empresa pequeña | 1 – 4 puntos |
| Iliquidez | Sin mercado para sus acciones | 2 – 5 puntos |
| Concentración | Dependencia de pocos clientes o de su dueño | Juicio |

```text
BETA APALANCADA Y DESAPALANCADA
  βu = βL / [1 + (1−t) × D/E]        desapalancar (quitar el efecto deuda)
  βL = βu × [1 + (1−t) × D/E]        apalancar (aplicar la estructura propia)

para una empresa sin acciones cotizadas:
  1. toma betas de empresas comparables cotizadas
  2. desapalánsalas con SU estructura
  3. promédialas
  4. apalánsala con la estructura de TU empresa
```

### 3. Costo promedio ponderado

```text
WACC = ke × E/(D+E) + kd × (1−t) × D/(D+E)

  E  valor de mercado del patrimonio
  D  valor de mercado de la deuda

USA VALORES DE MERCADO, NO CONTABLES
  el patrimonio contable no refleja lo que vale la empresa
  usar valores contables distorsiona los pesos
```

```text
EJEMPLO
  ke = 16,4 %, kd = 10,4 %, t = 27 %
  D = 6 500, E = 12 000  → D+E = 18 500

  WACC = 16,4 % × (12 000/18 500) + 10,4 % × 0,73 × (6 500/18 500)
       = 16,4 % × 0,6486 + 7,59 % × 0,3514
       = 10,64 % + 2,67 % = 13,31 %
```

### 4. Estructura óptima

```text
EL WACC EN FUNCIÓN DEL ENDEUDAMIENTO

  WACC
   │╲
   │ ╲___
   │     ╲______        ___/
   │            ╲_____/
   │              ↑
   │          óptimo
   └────────────────────────► D/(D+E)

  al principio baja: la deuda es más barata y el escudo aporta
  después sube: ke crece con el riesgo y kd crece con la calificación
```

| Factor | Empuja hacia MÁS deuda | Empuja hacia MENOS deuda |
|---|---|---|
| Tasa de impuesto | Alta | Baja o con pérdidas acumuladas |
| Estabilidad del flujo | Alta | Volátil |
| Activos tangibles | Muchos (sirven de garantía) | Pocos, intangibles |
| Oportunidades de crecimiento | Pocas | Muchas (flexibilidad) |
| Costo de insolvencia del sector | Bajo | Alto (marca, servicio, talento) |
| Acceso al mercado de capitales | Amplio | Limitado |

### 5. Jerarquía de preferencias y señales

```text
ORDEN OBSERVADO EN LAS EMPRESAS
  1. caja generada internamente
  2. deuda
  3. emisión de capital

  RAZÓN: asimetría de información
  quien dirige sabe más que el mercado sobre el valor real
  → emitir capital cuando la acción está cara es racional
  → el mercado lo sabe, y penaliza el anuncio de emisión
```

| Decisión | Señal que el mercado infiere |
|---|---|
| Aumento de deuda | Confianza en el flujo futuro |
| Emisión de capital | Posible sobrevaloración |
| Recompra de acciones | Acción infravalorada, o falta de proyectos |
| Aumento de dividendos | Flujo sostenible |
| Recorte de dividendos | Dificultad; señal muy negativa |

**Para el banco esto tiene un uso directo:** una empresa con acceso a deuda que decide emitir capital
está diciendo algo. Puede ser que sus accionistas quieran reducir riesgo, o que sepan algo sobre su
flujo futuro que aún no está en los estados.

## 🧮 Ejemplo guiado

**Situación.** Una empresa evalúa aumentar su endeudamiento y el banco analiza si acompañarla.

```text
LA EMPRESA
  valor de mercado del patrimonio        12 000
  deuda financiera                        6 500
  tasa de la deuda actual                 10,4 %
  resultado operacional                   3 592
  depreciación                              380
  tasa de impuesto                           27 %
  beta apalancada estimada                 1,42
  tasa libre de riesgo                      5,8 %
  prima de riesgo de mercado                6,4 %
  prima por tamaño                          2,0 %

PROPUESTA DE LA EMPRESA
  tomar 4 000 adicionales de deuda
  y repartir un dividendo extraordinario de 4 000
```

**Paso 1 — calcula el WACC actual.**

```text
ke = 5,8 % + 1,42 × 6,4 % + 2,0 % = 5,8 % + 9,09 % + 2,0 % = 16,89 %
kd después de impuestos = 10,4 % × 0,73 = 7,59 %

pesos: E = 12 000, D = 6 500, total 18 500
  E/(D+E) = 64,86 %    D/(D+E) = 35,14 %

WACC = 16,89 % × 0,6486 + 7,59 % × 0,3514 = 10,96 % + 2,67 % = 13,63 %
```

**Paso 2 — evalúa la capacidad de servicio actual.**

```text
resultado operacional + depreciación = 3 972
intereses actuales: 6 500 × 10,4 % = 676
cobertura de intereses: 3 972 / 676 = 5,88   ✓ cómodo

deuda / (resultado operacional + depreciación) = 6 500/3 972 = 1,64
```

**Paso 3 — proyecta la situación tras la operación.**

```text
deuda: 6 500 + 4 000 = 10 500
patrimonio: 12 000 − 4 000 (dividendo) = 8 000
valor total: 18 500 (sin cambio; solo cambia la estructura)

nueva tasa de la deuda: con mayor endeudamiento, el mercado exige más
  deuda / (RO + D) pasa de 1,64 a 2,64
  diferencial estimado adicional: +140 pb
  kd nueva sobre el total: aproximadamente 11,3 %

intereses: 10 500 × 11,3 % = 1 187
cobertura: 3 972 / 1 187 = 3,35   (era 5,88)
```

**Paso 4 — recalcula el costo del patrimonio.**

```text
desapalancar la beta actual:
  βu = 1,42 / [1 + 0,73 × (6 500/12 000)] = 1,42 / 1,3954 = 1,0176

apalancar con la nueva estructura:
  D/E nuevo = 10 500/8 000 = 1,3125
  βL = 1,0176 × [1 + 0,73 × 1,3125] = 1,0176 × 1,9581 = 1,9926

ke nuevo = 5,8 % + 1,9926 × 6,4 % + 2,0 % = 5,8 % + 12,75 % + 2,0 % = 20,55 %
```

**Paso 5 — calcula el WACC resultante.**

```text
kd después de impuestos: 11,3 % × 0,73 = 8,25 %
pesos: E = 8 000, D = 10 500, total 18 500
  E/(D+E) = 43,24 %   D/(D+E) = 56,76 %

WACC = 20,55 % × 0,4324 + 8,25 % × 0,5676 = 8,89 % + 4,68 % = 13,57 %

WACC actual:    13,63 %
WACC propuesto: 13,57 %
mejora: 0,06 puntos
```

**Paso 6 — evalúa si esa mejora justifica el riesgo.**

```text
GANANCIA
  reducción del WACC de 6 pb
  sobre un valor de 18 500: aumento de valor de ~80

  (aproximación: valor ≈ flujo/WACC; una caída de 6 pb
   sobre un WACC de 13,6 % aumenta el valor en ~0,44 %)

COSTOS Y RIESGOS
  cobertura de intereses: 5,88 → 3,35
  deuda / flujo: 1,64 → 2,64
  ke: 16,89 % → 20,55 %

la empresa asume un riesgo sustancialmente mayor
por una ganancia de valor del 0,44 %
```

**Paso 7 — busca el óptimo real.**

```text
SIMULACIÓN DEL WACC POR NIVEL DE DEUDA

  deuda   D/(D+E)   kd     βL     ke      WACC
   4 000    21,6 %   9,8 %  1,22  15,61 %  13,79 %
   6 500    35,1 %  10,4 %  1,42  16,89 %  13,63 %
   8 000    43,2 %  10,8 %  1,60  18,04 %  13,58 %
  10 500    56,8 %  11,3 %  1,99  20,55 %  13,57 %
  12 000    64,9 %  12,6 %  2,32  22,65 %  13,92 %
  14 000    75,7 %  14,8 %  2,98  26,87 %  14,71 %

el WACC es MUY PLANO entre 8 000 y 10 500
mínimo teórico: alrededor de 10 500
diferencia con 8 000: 1 punto básico
```

**Paso 8 — formula la respuesta del banco.**

```text
CONCLUSIÓN TÉCNICA
  la curva del WACC es plana en un rango amplio
  la "optimización" de la estructura aporta menos de 10 pb
  y el riesgo crece de forma no lineal

  esta planitud es un resultado general, no una particularidad:
  cerca del óptimo, la derivada es cero por definición

DECISIÓN DEL BANCO
  · financiar 4 000 para un dividendo extraordinario
    aumenta el riesgo del banco sin financiar ningún activo
  · la cobertura cae de 5,88 a 3,35
  · en un escenario de caída de ventas del 20 %:
    RO cae a 2 428, cobertura: (2 428+380)/1 187 = 2,37
    todavía aceptable, pero sin margen para un segundo golpe

  CONTRAPROPUESTA
    financiar 2 000, no 4 000
    cobertura resultante: 3 972 / (8 500 × 10,8 %) = 4,33
    WACC resultante: 13,58 % (a 1 pb del mínimo teórico)
    → el 99 % del beneficio con el 50 % del riesgo adicional

  CONDICIONES
    · covenant de cobertura de intereses ≥ 3,0
    · covenant de deuda / flujo ≤ 2,5
    · restricción de dividendos adicionales mientras
      la cobertura esté bajo 4,0
```

**Interpreta:** la teoría dice que existe una estructura óptima, y **el ejercicio muestra que en la
práctica el óptimo es un rango, no un punto**. Entre 8 000 y 10 500 de deuda el WACC varía un punto
básico y el riesgo casi se duplica. Optimizar el WACC con precisión decimal es un ejercicio sin
contenido económico; **elegir el extremo conservador del rango plano es casi gratis y compra mucha
resistencia**.

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Endeudarme baja mi costo de capital» | Cierto y marginal cerca del óptimo | 13, clase 5 |
| «Quiero repartir dividendos con deuda» | Aumenta el riesgo sin financiar activos | 13, clase 5 |
| «El banco me pone covenants» | Protección del rango de endeudamiento | 13, clase 8 |
| «Mi empresa va a emitir acciones» | Señal que el mercado interpreta | 13, clase 11 |
| «Mi tasa subió al endeudarme más» | El costo de la deuda crece con el riesgo | 9, clase 12 |

## 🧪 Práctica

En `labs/lab-03.md`:

1. Calcula el WACC de una empresa con sus componentes y valores de mercado.
2. Desapalanca y apalanca betas de comparables para una empresa no cotizada.
3. Simula el WACC en seis niveles de endeudamiento y localiza el rango óptimo.
4. Evalúa una operación de recapitalización desde la perspectiva del banco.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se usan valores contables como pesos | Distorsiona el WACC | Usa valores de mercado. |
| Se usa la tasa histórica de la deuda | El relevante es el marginal | Usa el costo de la próxima unidad. |
| Se optimiza el WACC al decimal | La curva es plana | Elige el extremo conservador del rango. |
| Beta de comparables sin desapalancar | Estructuras distintas | Desapalanca y vuelve a apalancar. |
| Se ignoran los costos de dificultades | Solo se ve el escudo fiscal | Empiezan antes de la quiebra. |
| Escudo fiscal con pérdidas acumuladas | No hay impuesto que escudar | Verifica la posición fiscal. |

## ❓ Preguntas de comprobación

1. ¿Qué dos efectos opuestos tiene la deuda sobre el valor de una empresa?
2. ¿Por qué el costo relevante de la deuda es el marginal y no el histórico?
3. ¿Por qué la curva del WACC es plana cerca del óptimo?
4. ¿Qué señal envía al mercado el anuncio de una emisión de capital?
5. ¿Por qué los costos de dificultades financieras empiezan antes de la insolvencia?

## 📥 Entregable

Guarda en `portfolio/parte-13/clase-05/`:

- el cálculo del WACC con todos sus componentes;
- el proceso de desapalancar y apalancar betas de comparables;
- la simulación del WACC en seis niveles con el rango óptimo identificado;
- la evaluación de la recapitalización desde la perspectiva del banco.

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

- Brealey, R., Myers, S. y Allen, F. (2020). *Principles of Corporate Finance* (13.ª ed.). McGraw-Hill. Capítulos 17 a 19.
- Modigliani, F. y Miller, M. (1958, 1963). "The Cost of Capital, Corporation Finance and the Theory of Investment" y su corrección. *American Economic Review*.
- Myers, S. y Majluf, N. (1984). "Corporate Financing and Investment Decisions When Firms Have Information That Investors Do Not Have". *Journal of Financial Economics*, 13(2).
- Damodaran, A. (2012). *Investment Valuation* (3.ª ed.). Wiley. Estimación de costo de capital y betas.
- Koller, T., Goedhart, M. y Wessels, D. (2020). *Valuation* (7.ª ed.). Wiley.
- Verificación local: revisa la tasa de impuesto a la renta corporativa de tu país y las reglas de limitación a la deducibilidad de intereses (subcapitalización).

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 04 · Capital de trabajo y financiamiento de corto plazo](04-capital-de-trabajo-y-corto-plazo.md) | [Parte 13](../README.md) · [Programa](../../../SYLLABUS.md) | [06 · Decisiones de inversión →](06-decisiones-de-inversion.md) |
<!-- gen:footer:end -->
