---
part: 11
class: 3
title: "Riesgo de crédito de cartera y concentración"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 03 · Riesgo de crédito de cartera y concentración

> [← 02 · Taxonomía de riesgos bancarios](02-taxonomia-de-riesgos.md) · [Índice de la parte](../README.md) · [04 · Riesgo de liquidez →](04-riesgo-de-liquidez.md)

**Parte 11 — Gestión integral de riesgos** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Pasar del riesgo de un crédito al riesgo de una cartera. La Parte 9 enseñó a evaluar un deudor; esta
clase enseña que **una cartera de buenos deudores puede ser una mala cartera** si están correlacionados,
y que la concentración es el mecanismo por el que eso ocurre.

## 📚 Objetivos

Al finalizar podrás:

1. **Agregar** pérdidas individuales en una distribución de pérdidas de cartera.
2. **Explicar** el efecto de la correlación sobre la pérdida inesperada.
3. **Medir** la concentración con índices verificables.
4. **Calcular** el capital económico por riesgo de crédito.
5. **Diseñar** límites de concentración con fundamento cuantitativo.

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
| `pérdida esperada de cartera` | Suma de las pérdidas esperadas individuales. Es aditiva. |
| `pérdida inesperada de cartera` | Menor que la suma de las individuales, salvo correlación perfecta. |
| `correlación de incumplimiento` | Tendencia de dos deudores a incumplir en el mismo escenario. |
| `factor sistémico` | Variable común que afecta a todos los deudores a la vez. |
| `concentración individual` | Exposición grande a un solo deudor o grupo. |
| `concentración sectorial` | Exposición grande a un sector, región o producto. |
| `índice de Herfindahl` | Suma de los cuadrados de las participaciones. Mide concentración. |
| `capital económico` | Capital necesario para absorber la pérdida a un nivel de confianza dado. |

## 🧠 Modelo mental

```text
DOS CARTERAS con la misma pérdida esperada

CARTERA A: 1 000 créditos de 100, PD 2 %, sectores diversos
  pérdida esperada = 1 000 × 100 × 0,02 × LGD 45 % = 900
  pérdida inesperada (99,9 %) ≈ 1 400

CARTERA B: 10 créditos de 10 000, PD 2 %, mismo sector
  pérdida esperada = 10 × 10 000 × 0,02 × 0,45 = 900
  pérdida inesperada (99,9 %) ≈ 13 500

MISMA pérdida esperada. La inesperada es casi 10 veces mayor.
```

**Ese es todo el contenido de la clase.** La pérdida esperada no distingue carteras; la inesperada sí, y
es la que consume capital.

## 📖 Desarrollo

### 1. De la pérdida individual a la de cartera

```text
PÉRDIDA ESPERADA (aditiva, siempre)
  PE_cartera = Σ  PD_i × LGD_i × EAD_i

PÉRDIDA INESPERADA (no aditiva)
  PI_cartera = √( Σ Σ  PI_i × PI_j × ρ_ij )

  si ρ = 0 para todo par:  PI_cartera = √(Σ PI_i²)  ← diversificación máxima
  si ρ = 1 para todo par:  PI_cartera = Σ PI_i      ← ninguna diversificación
```

**La diversificación reduce la pérdida inesperada, nunca la esperada.** Un banco que diversifica no
espera perder menos: espera que la pérdida se aparte menos de lo previsto.

### 2. El modelo de factor único

El modelo que subyace al enfoque de Basilea para riesgo de crédito supone que el incumplimiento depende
de un factor sistémico común y de un factor idiosincrático:

```text
capacidad_i = √ρ · Z  +  √(1−ρ) · ε_i

  Z    factor sistémico (la economía)
  ε_i  factor propio del deudor
  ρ    correlación con el factor sistémico
```

```text
CONSECUENCIAS
  · el riesgo idiosincrático se diversifica con muchos deudores
  · el riesgo sistémico NO se diversifica: afecta a todos a la vez
  · por eso una cartera infinitamente granular sigue teniendo pérdida inesperada
```

| Segmento | Correlación típica supuesta | Razón |
|---|---:|---|
| Hipotecario residencial | 15 % | Alta sensibilidad al ciclo y a las tasas |
| Consumo revolvente | 4 % | Incumplimiento más idiosincrático |
| Otros minoristas | 3–16 % | Según sensibilidad al empleo |
| Empresas grandes | 12–24 % | Decreciente con el tamaño del deudor |
| Pequeñas empresas | Ajuste a la baja | Más idiosincrático |

*(Valores del marco de Basilea III para el enfoque basado en calificaciones internas. Verifica los que
aplica tu jurisdicción.)*

### 3. Medición de la concentración

```text
ÍNDICE DE HERFINDAHL
  HHI = Σ w_i²        w_i = participación de la exposición i

  cartera perfectamente granular (n iguales): HHI = 1/n
  una sola exposición:                        HHI = 1

  "número efectivo de exposiciones" = 1 / HHI
```

```text
EJEMPLO
  cartera con 200 deudores, pero:
    5 deudores concentran el 40 %  (8 % cada uno)
    195 deudores el 60 %           (0,308 % cada uno)

  HHI = 5 × 0,08² + 195 × 0,00308²
      = 5 × 0,0064 + 195 × 0,0000095
      = 0,0320 + 0,0019 = 0,0339

  número efectivo = 1/0,0339 = 29,5 exposiciones

  la cartera tiene 200 deudores y se comporta como si tuviera 30
```

| Tipo de concentración | Cómo se mide | Límite típico |
|---|---|---|
| Individual | Exposición / patrimonio efectivo | 10–25 % por deudor o grupo |
| Grupo económico | Exposición agregada del grupo | 15–25 % |
| Sectorial | Participación del sector; HHI sectorial | 15–30 % por sector |
| Geográfica | Participación por región | Según exposición del país |
| Producto | Participación por producto | Según apetito |
| Garantía | Dependencia de un tipo de colateral | Especialmente inmobiliario |
| Fuente de repago | Deudores distintos, misma fuente | El más olvidado |

**La concentración por fuente de repago** es la más difícil de detectar: cincuenta proveedores de una
misma empresa grande son formalmente cincuenta deudores independientes y sustantivamente uno solo.

### 4. Capital económico

```text
CAPITAL ECONÓMICO = percentil de la distribución de pérdidas − pérdida esperada

  nivel de confianza    99,9 %  ← usual en banca, coherente con
                                  una probabilidad de quiebra de 1 en 1 000 años
  horizonte             1 año
```

```text
FÓRMULA DE BASILEA (enfoque IRB, cartera granular)

  K = LGD × [ N( (N⁻¹(PD) + √ρ · N⁻¹(0,999)) / √(1−ρ) ) − PD ] × ajuste_plazo

  N   distribución normal acumulada
  ρ   correlación del segmento
```

**Esta fórmula supone granularidad perfecta.** Cuando la cartera está concentrada, subestima el capital,
y por eso el Pilar 2 exige un cargo adicional por concentración.

## 🧮 Ejemplo guiado

**Situación.** Un banco analiza si su cartera comercial está adecuadamente diversificada.

```text
CARTERA COMERCIAL: 1 240 000, patrimonio efectivo 420 000

DIEZ MAYORES EXPOSICIONES
  deudor  exposición   sector
   1        68 000     construcción
   2        54 000     construcción
   3        49 000     inmobiliario
   4        41 000     construcción
   5        38 000     retail
   6        36 000     inmobiliario
   7        31 000     agroindustria
   8        29 000     retail
   9        27 000     construcción
  10        24 000     transporte
  resto    843 000     diversos (612 deudores)

PARÁMETROS: PD media 2,4 %, LGD 42 %, correlación del segmento 18 %
```

**Paso 1 — evalúa la concentración individual.**

```text
mayor exposición / patrimonio efectivo = 68 000 / 420 000 = 16,2 %
límite normativo habitual: 25 % individual  ✓ cumple

diez mayores / cartera = 397 000 / 1 240 000 = 32,0 %
diez mayores / patrimonio = 397 000 / 420 000 = 94,5 %
```

**Paso 2 — calcula el índice de Herfindahl.**

```text
participaciones de los diez mayores (sobre 1 240 000):
  0,0548  0,0435  0,0395  0,0331  0,0306
  0,0290  0,0250  0,0234  0,0218  0,0194

Σ w² de los diez     = 0,003003+0,001895+0,001562+0,001094+0,000937
                      +0,000843+0,000625+0,000547+0,000474+0,000376
                      = 0,011356
resto: 612 deudores con 843 000 → w medio = 0,001111
Σ w² del resto = 612 × 0,001111² = 0,000755

HHI = 0,012111
número efectivo de exposiciones = 1 / 0,012111 = 82,6

la cartera tiene 622 deudores
y se comporta como si tuviera 83
```

**Paso 3 — evalúa la concentración sectorial.**

```text
construcción:  68+54+41+27 = 190 000  de los diez mayores
inmobiliario:  49+36       =  85 000
retail:        38+29       =  67 000
agroindustria:              27 000  (dato: 31 000)
transporte:                 24 000

construcción + inmobiliario = 275 000 de los diez mayores
en el resto de la cartera, esos sectores suman 218 000

TOTAL construcción + inmobiliario = 493 000 / 1 240 000 = 39,8 %
```

**Paso 4 — evalúa la correlación entre esos dos sectores.**

```text
construcción e inmobiliario NO son sectores independientes:
  · comparten el ciclo de precios de la vivienda
  · comparten sensibilidad a la tasa hipotecaria
  · el constructor vende a la inmobiliaria y ambos dependen del comprador final

correlación histórica de incumplimiento entre ambos: 0,72

para efectos de límite, deben tratarse como UN SOLO sector
39,8 % de la cartera en un sector correlacionado
```

**Paso 5 — calcula el capital regulatorio del segmento.**

```text
usando la fórmula IRB con PD 2,4 %, LGD 42 %, ρ 18 %:

  N⁻¹(0,024) = −1,9774
  N⁻¹(0,999) =  3,0902
  √0,18 = 0,4243    √0,82 = 0,9055

  argumento = (−1,9774 + 0,4243 × 3,0902) / 0,9055
            = (−1,9774 + 1,3112) / 0,9055
            = −0,7358
  N(−0,7358) = 0,2309

  K = 0,42 × (0,2309 − 0,024) = 0,42 × 0,2069 = 0,0869
  → 8,69 % de la exposición, antes del ajuste de plazo

capital sobre la cartera comercial: 0,0869 × 1 240 000 = 107 756
```

**Paso 6 — estima el cargo adicional por concentración.**

```text
la fórmula supone granularidad infinita
con 83 exposiciones efectivas, el ajuste de granularidad
aproximado añade entre 4 % y 9 % del capital del segmento

cargo por concentración individual: ~6 % → 6 465
cargo por concentración sectorial (39,8 % en un sector correlacionado):
  el enfoque supone ρ = 18 %; con un sector que pesa 39,8 %
  la correlación efectiva de la cartera sube a ~0,26
  recalculando K con ρ = 0,26:
    argumento = (−1,9774 + 0,5099 × 3,0902) / 0,8602 = −0,4667
    N(−0,4667) = 0,3203
    K = 0,42 × (0,3203 − 0,024) = 0,1244 → 12,44 %
  capital con correlación ajustada: 154 256

DIFERENCIA POR CONCENTRACIÓN SECTORIAL: 154 256 − 107 756 = 46 500
```

**Paso 7 — decisiones.**

```text
1. El capital regulatorio subestima el riesgo en 46 500 (43 %)
   → reconocerlo como capital adicional en el Pilar 2

2. Límite sectorial: establecer 25 % por sector correlacionado
   exceso actual: 39,8 % − 25 % = 14,8 % → 183 520 a reducir o compensar

3. Plan: no renovar exposiciones del sector al vencimiento,
   originar en sectores no correlacionados, evaluar cobertura
   o venta de cartera

4. Vigilancia: la fuente de repago de construcción e inmobiliario
   es la misma (el comprador final de vivienda). Añadir el indicador
   de precios y de venta de viviendas al tablero de alertas.
```

**Interpreta:** el banco **cumplía todos los límites individuales** y estaba subcapitalizado en 43 %
para su riesgo real. La concentración sectorial no aparecía en ninguna métrica de límite porque los
límites estaban definidos por deudor. Este es el patrón de casi todas las crisis bancarias
documentadas: **límites individuales cumplidos y una concentración sectorial que nadie limitó**.

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Mi empresa es sólida pero me redujeron la línea» | Límite sectorial alcanzado | 11, clase 3 |
| «Todos los bancos dejaron de prestar a mi sector» | Correlación sectorial reconocida a la vez | 11, clase 3 |
| «El banco prefiere muchos créditos chicos» | Granularidad y capital | 9, clase 14 |
| «Mi tasa subió sin que yo cambiara» | Capital del segmento y su costo | 15, clase 7 |
| «El banco pide garantías distintas» | Concentración de colateral | 9, clase 9 |

## 🧪 Práctica

En `labs/lab-02.md`:

1. Calcula la pérdida esperada e inesperada de dos carteras con la misma media.
2. Mide la concentración con el índice de Herfindahl y el número efectivo.
3. Calcula el capital IRB de un segmento y su ajuste por correlación efectiva.
4. Diseña un conjunto de límites de concentración con su fundamento cuantitativo.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se cumplen los límites individuales y el riesgo es alto | Sin límite sectorial | Limita por sector correlacionado. |
| Se cuentan deudores, no exposiciones efectivas | Concentración no medida | Usa el número efectivo (1/HHI). |
| Sectores correlacionados tratados por separado | Correlación ignorada | Agrupa por fuente de repago. |
| Se cree que diversificar baja la pérdida esperada | Concepto | Baja la inesperada, no la esperada. |
| Se usa el capital IRB sin ajuste | Supone granularidad infinita | Añade cargo por concentración. |
| Cincuenta deudores con un solo pagador final | Fuente de repago única | Agrégalos como una exposición. |

## ❓ Preguntas de comprobación

1. ¿Por qué dos carteras con la misma pérdida esperada pueden exigir capital muy distinto?
2. ¿Qué mide el número efectivo de exposiciones y por qué es más útil que contar deudores?
3. ¿Por qué el riesgo sistémico no se diversifica?
4. ¿Por qué la fórmula IRB subestima el capital de una cartera concentrada?
5. ¿Qué es la concentración por fuente de repago y por qué es difícil de detectar?

## 📥 Entregable

Guarda en `portfolio/parte-11/clase-03/`:

- la comparación de las dos carteras con sus pérdidas esperada e inesperada;
- el índice de Herfindahl y el número efectivo de exposiciones calculados;
- el capital del segmento con y sin ajuste por correlación;
- los límites de concentración diseñados con su fundamento.

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

- Basel Committee on Banking Supervision (2017). *Basel III: Finalising post-crisis reforms*. BIS. <https://www.bis.org/bcbs/publ/d424.htm>
- Basel Committee on Banking Supervision (2005). *An Explanatory Note on the Basel II IRB Risk Weight Functions*. BIS. <https://www.bis.org/bcbs/irbriskweight.htm>
- Basel Committee on Banking Supervision (2014). *Supervisory framework for measuring and controlling large exposures*. BIS.
- Vasicek, O. (2002). "The Distribution of Loan Portfolio Value". *Risk*, 15(12). Modelo de factor único.
- Caouette, J., Altman, E., Narayanan, P. y Nimmo, R. (2008). *Managing Credit Risk* (2.ª ed.). Wiley. Capítulos sobre riesgo de cartera.
- Verificación local: revisa los límites de exposición individual y de grupo económico, y los cargos por concentración del Pilar 2 en tu jurisdicción.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 02 · Taxonomía de riesgos bancarios](02-taxonomia-de-riesgos.md) | [Parte 11](../README.md) · [Programa](../../../SYLLABUS.md) | [04 · Riesgo de liquidez →](04-riesgo-de-liquidez.md) |
<!-- gen:footer:end -->
