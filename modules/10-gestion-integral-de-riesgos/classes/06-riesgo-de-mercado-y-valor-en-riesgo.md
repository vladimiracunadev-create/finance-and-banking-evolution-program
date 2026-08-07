---
part: 11
class: 6
title: "Riesgo de mercado y valor en riesgo"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 06 · Riesgo de mercado y valor en riesgo

> [← 05 · Riesgo de tasa en el libro de banca](05-riesgo-de-tasa-en-el-libro-de-banca.md) · [Índice de la parte](../README.md) · [07 · Riesgo de moneda →](07-riesgo-de-moneda.md)

**Parte 11 — Gestión integral de riesgos** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Medir cuánto puede perder una cartera de negociación en un día malo, y entender por qué la medida más
usada del sector —el valor en riesgo— es útil, insuficiente y peligrosa si se interpreta mal.

Las clases anteriores miden el balance. Esta mide las posiciones que se negocian, y presenta la medida más usada y más criticada de la gestión de riesgo. La clase la enseña completa y también sus límites, porque su uso sin entenderlos es lo que produjo varias de las pérdidas más grandes de la historia bancaria.

## 📚 Objetivos

Al finalizar podrás:

1. **Calcular** el valor en riesgo por los tres métodos principales.
2. **Interpretar** correctamente qué dice y qué no dice esa cifra.
3. **Calcular** el déficit esperado y explicar por qué lo reemplazó.
4. **Ejecutar** una prueba retrospectiva y evaluar el modelo con ella.
5. **Complementar** la medición con escenarios de estrés.

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

Los cuatro primeros términos son la medida y sus parámetros; los cuatro siguientes, su verificación y sus problemas. El **déficit esperado** es la respuesta al problema principal: promedia las pérdidas de la cola en vez de ignorarlas, y por eso reemplazó al valor en riesgo en la norma.

| Concepto | Comprensión verificable |
|---|---|
| `valor en riesgo` | Pérdida que no se superará con probabilidad p en un horizonte h. |
| `déficit esperado` | Pérdida media condicionada a superar el valor en riesgo. |
| `nivel de confianza` | Probabilidad asociada al cuantil elegido. |
| `horizonte` | Período sobre el que se mide la pérdida potencial. |
| `prueba retrospectiva` | Comparación entre pérdidas reales y las predichas por el modelo. |
| `excepción` | Día en que la pérdida real supera el valor en riesgo. |
| `subaditividad` | Propiedad deseable: el riesgo del todo no supera la suma de las partes. |
| `estrés` | Escenario extremo definido, no derivado de la distribución histórica. |

## 🧠 Modelo mental

El modelo mental es una frase incómoda: el valor en riesgo dice cuánto se pierde en el peor día de cada cien, y no dice nada sobre cuánto se pierde en ese uno por ciento restante. Todo lo que importa de verdad está en la parte que la medida no cubre.

```text
EL VALOR EN RIESGO RESPONDE:
  "en 99 de cada 100 días, no perderé más de X"

NO RESPONDE:
  "cuánto perderé en el día 100"

y el día 100 es el que importa
```

**Esa es la limitación estructural, no un defecto de implementación.** El valor en riesgo es un umbral,
no una medida de la cola. El déficit esperado responde justamente la pregunta que el valor en riesgo
deja abierta.

## 📖 Desarrollo

### 1. Los tres métodos

Hay tres formas de calcular el valor en riesgo y dan resultados distintos sobre la misma cartera. La tabla las compara.

| Método | Cómo funciona | Ventaja | Limitación |
|---|---|---|---|
| Paramétrico | Supone normalidad; usa media, volatilidad y correlaciones | Rápido, transparente | Subestima colas; falla con opciones |
| Simulación histórica | Aplica los cambios reales de los últimos N días a la cartera actual | Sin supuesto de distribución | Depende de la ventana; no ve lo que no pasó |
| Monte Carlo | Simula miles de escenarios desde un modelo | Flexible; maneja no linealidad | Costoso; depende del modelo supuesto |

```text
PARAMÉTRICO
  VaR = z × σ × √h × V

  z    cuantil de la normal (1,645 al 95 %; 2,326 al 99 %)
  σ    volatilidad diaria de la cartera
  h    horizonte en días
  V    valor de la cartera
```

```text
HISTÓRICO
  1. toma los N rendimientos diarios más recientes (típico: 250 a 500)
  2. aplícalos a la cartera ACTUAL → N resultados hipotéticos
  3. ordénalos de peor a mejor
  4. el VaR al 99 % es el percentil 1 de esa distribución
```

### 2. Por qué el déficit esperado lo reemplazó

El valor en riesgo tiene dos defectos teóricos con consecuencias prácticas. El esquema los muestra.

```text
DOS CARTERAS, MISMO VaR al 99 %

  cartera A: en el 1 % peor, pierde entre 100 y 120
  cartera B: en el 1 % peor, pierde entre 100 y 4 000

  VaR(99 %) = 100 en ambas
  la medida no las distingue
```

```text
DÉFICIT ESPERADO (Expected Shortfall)
  ES = media de las pérdidas que superan el VaR

  cartera A: ES ≈ 108
  cartera B: ES ≈ 1 250

  ahora sí las distingue
```

| Propiedad | Valor en riesgo | Déficit esperado |
|---|---|---|
| Mide la cola | No | Sí |
| Subaditivo (siempre) | No | Sí |
| Fácil de comunicar | Sí | Menos |
| Fácil de validar retrospectivamente | Sí | Más difícil |
| Uso regulatorio actual | Complementario | Principal (Basilea III revisado) |

**La falta de subaditividad del valor en riesgo es su defecto teórico más serio:** puede indicar que
juntar dos carteras aumenta el riesgo total, lo que contradice el principio de diversificación y crea
incentivos perversos para fragmentar posiciones.

### 3. Prueba retrospectiva

La prueba retrospectiva compara las pérdidas observadas con las predichas y es lo que valida el modelo. El procedimiento siguiente la ejecuta.

```text
COMPARAR cada día:
  pérdida real del día  vs.  VaR predicho el día anterior

  si la pérdida real supera al VaR → EXCEPCIÓN

  al 99 % de confianza, en 250 días hábiles
  se esperan 2,5 excepciones
```

| Excepciones en 250 días | Zona | Consecuencia |
|---:|---|---|
| 0–4 | Verde | Modelo aceptable |
| 5–9 | Amarilla | Multiplicador de capital creciente; investigar |
| 10 o más | Roja | Modelo rechazado; enfoque estandarizado |

```text
QUÉ INVESTIGAR ANTE EXCEPCIONES
  · ¿la cartera cambió y el modelo no se recalibró?
  · ¿la ventana histórica excluye el episodio relevante?
  · ¿hay posiciones no capturadas por los factores del modelo?
  · ¿las excepciones se agrupan en el tiempo?  ← la señal más grave
```

**Excepciones agrupadas** indican que el modelo falla justo cuando importa: no es mala suerte, es que la
volatilidad se agrupa y el modelo no lo captura.

### 4. Lo que ninguna medida estadística ve

Hay riesgos que no aparecen en ninguna serie histórica y por eso ninguna medida estadística los captura. La tabla los recoge.

```text
· eventos sin precedente en la ventana histórica
· quiebres de correlación (todo cae junto)
· iliquidez (no puedes salir al precio que el modelo supone)
· riesgo de contraparte del que te cubre
· cambios de régimen normativo o político

PARA ESO EXISTEN LOS ESCENARIOS DE ESTRÉS
  no se derivan de la distribución: se DEFINEN
```

| Tipo de escenario | Ejemplo |
|---|---|
| Histórico | Repetir un episodio real documentado sobre la cartera actual |
| Hipotético | Choque definido por el comité, coherente internamente |
| Inverso | ¿Qué escenario me haría perder mi capital? Trabajar hacia atrás |

**El escenario inverso es el más informativo** y el menos usado: en lugar de preguntar cuánto pierdo en
un escenario dado, pregunta qué tendría que pasar para que la pérdida sea intolerable, y luego evalúa
qué tan lejano es eso realmente.

## 🧮 Ejemplo guiado

El ejemplo calcula el valor en riesgo por los tres métodos y el déficit esperado. La diferencia entre las cifras es grande, y elegir cuál se reporta es una decisión con consecuencias.

**Situación.** Una mesa mide su riesgo y el comité evalúa si la medición es confiable.

```text
CARTERA DE NEGOCIACIÓN: 240 000
  bonos soberanos locales      120 000   σ diaria 0,42 %
  bonos corporativos            60 000   σ diaria 0,68 %
  posición en moneda extranjera 40 000   σ diaria 0,95 %
  acciones                      20 000   σ diaria 1,60 %

CORRELACIONES
                sob    corp    fx    acc
  soberanos    1,00   0,78   0,15   0,32
  corporativos 0,78   1,00   0,22   0,48
  moneda       0,15   0,22   1,00   0,18
  acciones     0,32   0,48   0,18   1,00
```

**Paso 1 — calcula la volatilidad de la cartera.**

```text
contribuciones individuales (peso × σ, en unidades monetarias):
  soberanos     120 000 × 0,0042 = 504,0
  corporativos   60 000 × 0,0068 = 408,0
  moneda         40 000 × 0,0095 = 380,0
  acciones       20 000 × 0,0160 = 320,0
  suma simple                     1 612,0

varianza de la cartera = Σ Σ σ_i σ_j ρ_ij
  términos diagonales:
    504² + 408² + 380² + 320² = 254 016+166 464+144 400+102 400 = 667 280
  términos cruzados (×2):
    sob-corp:  2 × 504 × 408 × 0,78 = 320 785
    sob-fx:    2 × 504 × 380 × 0,15 =  57 456
    sob-acc:   2 × 504 × 320 × 0,32 = 103 219
    corp-fx:   2 × 408 × 380 × 0,22 =  68 218
    corp-acc:  2 × 408 × 320 × 0,48 = 125 337
    fx-acc:    2 × 380 × 320 × 0,18 =  43 776
    suma cruzada                      718 791

  varianza = 667 280 + 718 791 = 1 386 071
  σ_cartera = √1 386 071 = 1 177,3
```

**Paso 2 — calcula el valor en riesgo paramétrico.**

```text
VaR(99 %, 1 día) = 2,326 × 1 177,3 = 2 739

beneficio de diversificación:
  suma sin correlación: 2,326 × 1 612,0 = 3 750
  con correlación:                        2 739
  reducción: 1 011  (27,0 %)
```

**Paso 3 — escala al horizonte regulatorio.**

```text
VaR(99 %, 10 días) = 2 739 × √10 = 8 662

ADVERTENCIA sobre la regla de la raíz:
supone rendimientos independientes entre días
si la volatilidad se agrupa (y se agrupa), SUBESTIMA
```

**Paso 4 — calcula el déficit esperado.**

```text
bajo normalidad, ES(97,5 %) ≈ 2,338 × σ  (calibrado para ser
comparable con VaR al 99 % en distribución normal)

ES(97,5 %, 1 día) = 2,338 × 1 177,3 = 2 753

bajo normalidad, VaR y ES casi coinciden
la diferencia aparece con colas gruesas: y las colas SON gruesas
```

**Paso 5 — contrasta con la simulación histórica.**

```text
aplicando los 500 días históricos a la cartera actual:
  percentil 1 (VaR histórico 99 %):        3 480
  media del 1 % peor (ES histórico):       5 210

  VaR paramétrico:  2 739
  VaR histórico:    3 480      +27 %
  ES histórico:     5 210      +90 % sobre el VaR paramétrico

el supuesto de normalidad subestima la pérdida
en casi un tercio en el umbral
y en un 90 % en la cola
```

**Paso 6 — evalúa la prueba retrospectiva.**

```text
últimos 250 días hábiles:
  excepciones observadas: 7
  esperadas al 99 %: 2,5
  ZONA AMARILLA

distribución temporal de las excepciones:
  días 41, 43, 44, 47, 48, 189, 231
  → 5 de las 7 en un lapso de 8 días

DIAGNÓSTICO: las excepciones están AGRUPADAS
no es mala suerte: el modelo no captura el agrupamiento de volatilidad
```

**Paso 7 — aplica un escenario de estrés y uno inverso.**

```text
ESTRÉS HISTÓRICO (episodio de tensión soberana)
  soberanos    −6,8 %  → −8 160
  corporativos −9,2 %  → −5 520
  moneda       +11,4 % → +4 560  (posición larga en la divisa)
  acciones    −14,1 %  → −2 820
  PÉRDIDA TOTAL                   −11 940

  el estrés produce 4,4 veces el VaR paramétrico
  y las correlaciones asumidas se rompen:
  en el escenario, soberanos y corporativos caen juntos (ρ→0,95)

ESCENARIO INVERSO
  ¿qué pérdida agotaría el límite de pérdida mensual de 12 000?
  → exactamente el escenario histórico anterior
  → ese episodio NO es hipotético: ya ocurrió
```

**Paso 8 — decisiones del comité.**

```text
1. MEDICIÓN
   migrar de VaR paramétrico a déficit esperado histórico
   como medida principal; conservar el VaR para continuidad de serie

2. MODELO
   las excepciones agrupadas exigen un modelo de volatilidad
   condicional; recalibrar y volver a probar

3. CAPITAL
   zona amarilla → multiplicador de capital incrementado
   reconocer el mayor requerimiento

4. LÍMITES
   el límite de pérdida mensual (12 000) es inferior a la pérdida
   del escenario de estrés (11 940 en un solo evento)
   → el límite no deja margen para nada más en el mes
   → revisar: límite de estrés separado del límite de pérdida realizada

5. CORRELACIONES
   incorporar un escenario con correlaciones en 1 dentro de la
   familia de renta fija: la diversificación entre soberanos
   y corporativos desaparece justo en el evento
```

**Interpreta:** las tres mediciones —2 739, 3 480 y 11 940— **no se contradicen: responden preguntas
distintas**. El error de gestión sería elegir la más baja porque es la que produce el número más
cómodo. La prueba retrospectiva es la que impide hacerlo: **es el único mecanismo que confronta el
modelo con la realidad, y por eso es el control más importante de toda la clase**.

## 🏦 Del cliente al banco

El cliente compra un producto y el banco mide la pérdida potencial de su posición. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Mi fondo perdió más de lo que decía el folleto» | Límite del valor en riesgo como medida | 8, clase 12 |
| «Todo cayó al mismo tiempo» | Quiebre de correlaciones en estrés | 11, clase 6 |
| «El banco tuvo una pérdida enorme en un día» | Excepción de modelo y cola no medida | 11, clase 6 |
| «Me ofrecen un producto estructurado» | La mesa es la contraparte y mide su riesgo | 11, clase 9 |
| «El riesgo estaba dentro de límites» | Límite calibrado sin escenario de estrés | 11, clase 13 |

## 🧪 Práctica

El laboratorio pide calcular las medidas y ejecutar la prueba retrospectiva. El modelo propuesto tiene más excepciones de las admisibles, y explicar por qué es el objetivo.

En `labs/lab-03.md`, sección de mercado:

1. Calcula el valor en riesgo paramétrico de una cartera con matriz de correlaciones.
2. Calcula el valor en riesgo y el déficit esperado por simulación histórica y compara.
3. Ejecuta una prueba retrospectiva sobre 250 días y clasifica el modelo por zona.
4. Diseña un escenario de estrés y un escenario inverso para la cartera.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen pérdidas muy superiores a las modeladas. Las causas son el uso del valor en riesgo sin estrés y series históricas sin episodios adversos.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se reporta solo el valor en riesgo | No mide la cola | Añade déficit esperado. |
| Se elige el método que da el número menor | Sesgo de conveniencia | Reporta los tres y explica la diferencia. |
| Excepciones agrupadas no investigadas | Se cuentan, no se analizan | El agrupamiento es la señal grave. |
| Se escala con la raíz del tiempo sin advertirlo | Independencia supuesta | Declara el supuesto y su efecto. |
| Correlaciones históricas usadas en estrés | Se rompen en el evento | Estresa también las correlaciones. |
| Límites de pérdida sin escenario de estrés | Calibración incompleta | Verifica que el límite resista el escenario. |

## ❓ Preguntas de comprobación

1. ¿Qué pregunta responde el valor en riesgo y cuál deja sin responder?
2. ¿Por qué la falta de subaditividad del valor en riesgo crea incentivos perversos?
3. ¿Qué significa que las excepciones de la prueba retrospectiva estén agrupadas?
4. ¿Por qué el escalamiento por la raíz del tiempo subestima el riesgo?
5. ¿Qué aporta un escenario inverso que no aporta un escenario de estrés convencional?

## 📥 Entregable

Guarda en `portfolio/parte-11/clase-06/`:

- el valor en riesgo paramétrico con el beneficio de diversificación calculado;
- la comparación entre método paramétrico, histórico y déficit esperado;
- la prueba retrospectiva con su clasificación y el análisis del agrupamiento;
- el escenario de estrés y el escenario inverso con sus conclusiones.

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

- Basel Committee on Banking Supervision (2019). *Minimum capital requirements for market risk*. BIS. <https://www.bis.org/bcbs/publ/d457.htm>
- Basel Committee on Banking Supervision (1996). *Supervisory framework for the use of backtesting*. BIS. <https://www.bis.org/publ/bcbs22.htm>
- Artzner, P., Delbaen, F., Eber, J. y Heath, D. (1999). "Coherent Measures of Risk". *Mathematical Finance*, 9(3). Origen de la crítica al VaR.
- Jorion, P. (2006). *Value at Risk* (3.ª ed.). McGraw-Hill.
- Hull, J. (2018). *Risk Management and Financial Institutions* (5.ª ed.). Wiley. Capítulos 12 a 14.
- Verificación local: revisa el enfoque de riesgo de mercado (estandarizado o de modelos internos) y los requisitos de prueba retrospectiva de tu supervisor.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 05 · Riesgo de tasa en el libro de banca](05-riesgo-de-tasa-en-el-libro-de-banca.md) | [Parte 11](../README.md) · [Programa](../../../SYLLABUS.md) | [07 · Riesgo de moneda →](07-riesgo-de-moneda.md) |
<!-- gen:footer:end -->
