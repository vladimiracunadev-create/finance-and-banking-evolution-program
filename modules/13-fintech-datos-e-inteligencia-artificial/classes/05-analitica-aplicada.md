---
part: 14
class: 5
title: "Analítica aplicada"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 05 · Analítica aplicada

> [← 04 · Datos en un banco](04-datos-en-un-banco.md) · [Índice de la parte](../README.md) · [06 · Inteligencia artificial en banca →](06-inteligencia-artificial-en-banca.md)

**Parte 14 — Fintech, datos e inteligencia artificial** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Convertir datos en decisiones. Esta clase cubre el trabajo analítico que un banco hace todos los días
—segmentar, predecir, priorizar, medir— y el error metodológico que más lo arruina: **confundir
correlación con causalidad al diseñar una intervención**.

## 📚 Objetivos

Al finalizar podrás:

1. **Formular** una pregunta de negocio como problema analítico.
2. **Elegir** la técnica adecuada al tipo de problema.
3. **Diseñar** un experimento controlado para medir el efecto de una acción.
4. **Distinguir** predicción de causalidad y sus usos distintos.
5. **Comunicar** un resultado analítico de forma accionable.

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
| `problema de predicción` | Estimar un valor o una clase a partir de datos. |
| `problema causal` | Estimar el efecto de una intervención. |
| `grupo de control` | Conjunto que no recibe la intervención, comparable al que sí. |
| `asignación aleatoria` | Reparto al azar que hace comparables los grupos. |
| `sesgo de selección` | Diferencia entre grupos anterior a la intervención. |
| `elevación (uplift)` | Efecto incremental de la acción sobre quien la recibe. |
| `significancia` | Probabilidad de que el resultado no sea azar. |
| `validez externa` | Que el resultado se sostenga fuera de la muestra. |

## 🧠 Modelo mental

```text
DOS PREGUNTAS QUE PARECEN LA MISMA Y NO LO SON

  PREDICCIÓN   ¿quién va a comprar?
               → sirve para PRIORIZAR a quién contactar

  CAUSALIDAD   ¿a quién hace comprar el que yo lo contacte?
               → sirve para DECIDIR a quién contactar

  y son grupos DISTINTOS:
  quien iba a comprar de todos modos aparece primero
  en el modelo de predicción, y contactarlo no aporta nada
```

**Este es el error analítico más caro y más común en banca comercial.** Un modelo de propensión
identifica a quien va a contratar; una campaña dirigida a ese grupo muestra una conversión altísima y un
efecto incremental cercano a cero, porque esas personas habrían contratado igual.

## 📖 Desarrollo

### 1. Del problema de negocio al problema analítico

```text
FORMULACIÓN EN CUATRO PARTES
  1. DECISIÓN     ¿qué se va a decidir con el resultado?
  2. UNIDAD       ¿sobre qué se decide? cliente, operación, producto
  3. RESULTADO    ¿qué se quiere estimar, con qué definición exacta?
  4. RESTRICCIÓN  ¿qué recursos, plazos y límites hay?

si no se puede responder la pregunta 1,
el análisis no debe hacerse
```

| Pregunta de negocio | Tipo de problema | Técnica |
|---|---|---|
| ¿Quién va a incumplir? | Predicción, clasificación | Modelos de clasificación |
| ¿Cuánto va a consumir? | Predicción, regresión | Modelos de regresión |
| ¿Qué clientes se parecen? | Agrupación | Segmentación no supervisada |
| ¿Qué producto ofrecer? | Recomendación | Filtrado colaborativo o reglas |
| ¿Sirvió la campaña? | Causalidad | Experimento controlado |
| ¿A quién conviene contactar? | Causalidad, elevación | Modelo de elevación |
| ¿Por qué se van los clientes? | Explicación | Análisis y experimentación |

### 2. El experimento controlado

```text
DISEÑO MÍNIMO
  1. define la población elegible
  2. asigna AL AZAR: grupo tratado y grupo de control
  3. aplica la intervención solo al grupo tratado
  4. mide el mismo indicador en ambos
  5. la diferencia es el EFECTO CAUSAL

la asignación aleatoria es lo que hace válida la comparación:
garantiza que los grupos sean iguales en todo
salvo en la intervención
```

```text
ERRORES QUE INVALIDAN UN EXPERIMENTO
  · elegir el grupo tratado por conveniencia
    (los "mejores clientes" reciben la oferta)
  · comparar con los que no aceptaron
    (quien acepta es distinto de quien no)
  · comparar antes y después sin control
    (cualquier cambio del entorno se atribuye a la acción)
  · mirar muchos indicadores y reportar el que salió bien
  · detener el experimento cuando el resultado gusta
```

### 3. Tamaño de muestra y significancia

```text
ANTES DE EMPEZAR, CALCULA EL TAMAÑO NECESARIO
  depende de:
    · el efecto mínimo que interesa detectar
    · la variabilidad del indicador
    · el nivel de confianza y la potencia deseados

  un experimento con muestra insuficiente
  produce un resultado no concluyente
  y consume el mismo tiempo que uno bien dimensionado
```

| Situación | Interpretación |
|---|---|
| Efecto grande, muestra grande | Resultado sólido |
| Efecto grande, muestra pequeña | Puede ser azar; repetir |
| Efecto pequeño, muestra grande | Real pero quizá no relevante |
| Efecto pequeño, muestra pequeña | No concluyente |

```text
SIGNIFICANCIA NO ES RELEVANCIA
  un efecto de 0,02 puntos sobre 4 millones de clientes
  puede ser estadísticamente significativo
  y económicamente irrelevante

  siempre pregunta: ¿cuánto vale este efecto en dinero?
```

### 4. Modelos de elevación

```text
CUATRO TIPOS DE CLIENTE ANTE UNA ACCIÓN

  PERSUADIBLES   contratan si los contacto, no si no lo hago
                 → EL ÚNICO GRUPO QUE JUSTIFICA LA ACCIÓN
  SEGUROS        contratan de todos modos
                 → contactarlos gasta sin aportar
  PERDIDOS       no contratan de ninguna manera
                 → contactarlos gasta sin aportar
  CONTRAPRODUCENTES  contratarían, pero el contacto los aleja
                 → contactarlos DESTRUYE valor
```

```text
CÓMO SE ESTIMA
  se ejecuta un experimento con control
  se modela la DIFERENCIA de probabilidad entre tratados y control
  para cada perfil
  → el modelo predice el efecto incremental, no la probabilidad
```

**El grupo contraproducente existe y se subestima.** Recordar a un cliente que su seguro se renueva
puede hacer que lo cancele; ofrecer una refinanciación puede activar la búsqueda de alternativas en
otros bancos.

### 5. Comunicar un resultado

```text
ESTRUCTURA DE UNA COMUNICACIÓN ÚTIL
  1. la decisión que se recomienda
  2. el efecto estimado, en unidades de negocio
  3. el rango de incertidumbre
  4. los supuestos que sostienen el resultado
  5. qué lo invalidaría
  6. qué se debe medir después para verificarlo

LO QUE NO DEBE APARECER
  · métricas técnicas sin traducción
  · un número sin rango
  · una recomendación sin acción concreta
```

## 🧮 Ejemplo guiado

**Situación.** El área comercial evalúa una campaña de colocación de tarjetas de crédito.

```text
CAMPAÑA EJECUTADA
  contactados: 84 000 clientes
  criterio de selección: modelo de propensión, decil superior
  contrataciones: 12 600  (15,0 % de conversión)
  costo de contacto: 0,0021 por cliente → 176 total
  margen anual por tarjeta contratada: 0,082

RESULTADO PRESENTADO
  ingreso anual: 12 600 × 0,082 = 1 033
  costo: 176
  RETORNO: 5,9 veces
```

**Paso 1 — cuestiona la medición.**

```text
¿CUÁNTOS DE LOS 12 600 HABRÍAN CONTRATADO SIN LA CAMPAÑA?

  el modelo de propensión seleccionó al decil
  con MAYOR probabilidad de contratar

  por construcción, ese decil contrata más que el resto
  con campaña o sin ella

  el resultado presentado NO mide el efecto de la campaña:
  mide la conversión de un grupo seleccionado por su propensión
```

**Paso 2 — diseña la medición correcta.**

```text
EXPERIMENTO
  población elegible: decil superior de propensión, 96 000 clientes
  asignación aleatoria:
    grupo tratado:   84 000  (reciben la campaña)
    grupo de control: 12 000  (no reciben nada)

  se mide la contratación en ambos durante 60 días
```

**Paso 3 — analiza los resultados del experimento.**

```text
GRUPO TRATADO
  84 000 contactados → 12 600 contrataciones = 15,00 %

GRUPO DE CONTROL
  12 000 sin contactar → 1 464 contrataciones = 12,20 %

EFECTO INCREMENTAL: 15,00 % − 12,20 % = 2,80 puntos
```

**Paso 4 — recalcula el resultado real.**

```text
CONTRATACIONES INCREMENTALES
  84 000 × 2,80 % = 2 352

  de las 12 600 contrataciones, 10 248 habrían ocurrido igual
  la campaña causó 2 352

INGRESO INCREMENTAL: 2 352 × 0,082 = 193
COSTO: 176
RETORNO REAL: 1,10 veces

frente al 5,9 presentado
```

**Paso 5 — verifica la significancia.**

```text
diferencia: 2,80 puntos
error estándar de la diferencia:
  √[0,15×0,85/84 000 + 0,122×0,878/12 000]
  = √[0,00000152 + 0,00000893] = √0,00001045 = 0,00323

intervalo de confianza al 95 %:
  2,80 % ± 1,96 × 0,323 % = 2,80 % ± 0,63 %
  → entre 2,17 % y 3,43 %

el efecto es SIGNIFICATIVO
el rango de contrataciones incrementales: 1 823 a 2 881
el rango de retorno: 0,85 a 1,34 veces
```

**Paso 6 — segmenta el efecto por perfil.**

```text
EFECTO INCREMENTAL POR SUBGRUPO

  subgrupo                    tratado  control  elevación
  cliente con nómina en banco   19,4 %  18,1 %   +1,3 pp
  cliente antiguo (>5 años)     16,2 %  14,8 %   +1,4 pp
  cliente nuevo (<2 años)       13,8 %   8,4 %   +5,4 pp
  cliente sin otros productos   11,2 %   5,9 %   +5,3 pp
  cliente con tarjeta de otro
    banco declarada              9,8 %  11,4 %   −1,6 pp
```

**Paso 7 — interpreta la segmentación.**

```text
PERSUADIBLES
  clientes nuevos (+5,4 pp) y sin otros productos (+5,3 pp)
  → la campaña les da información que no tenían

SEGUROS
  clientes con nómina (+1,3) y antiguos (+1,4)
  → contratan de todos modos; el contacto aporta poco

CONTRAPRODUCENTES
  clientes con tarjeta de otro banco declarada (−1,6 pp)
  → el contacto activó la comparación
    y algunos decidieron quedarse con la del competidor
```

**Paso 8 — rediseña la campaña.**

```text
CAMPAÑA DIRIGIDA A PERSUADIBLES
  clientes nuevos y sin otros productos en la base: 31 400
  elevación esperada: 5,35 puntos
  contrataciones incrementales: 1 680
  costo: 31 400 × 0,0021 = 66
  ingreso: 1 680 × 0,082 = 138
  RETORNO: 2,09 veces

COMPARACIÓN
                          contactados  incrementales  costo  retorno
  campaña original           84 000        2 352       176    1,10
  campaña dirigida           31 400        1 680        66    2,09

  se obtiene el 71 % del efecto
  con el 37 % del costo y el 37 % de los contactos

BENEFICIO ADICIONAL NO CONTABILIZADO
  se evita contactar a 8 200 clientes contraproducentes
  efecto evitado: 8 200 × 1,6 % = 131 contrataciones
  que se perdían por contactarlos
  → 131 × 0,082 = 11 anuales de valor preservado

  y se reduce la saturación de los clientes seguros,
  que reciben menos contactos irrelevantes
```

**Interpreta:** la campaña original **funcionaba** —el retorno de 1,10 es positivo— y su medición era
cinco veces optimista. La corrección no vino de una técnica sofisticada sino de **una asignación
aleatoria y un grupo de control de 12 000 clientes**. El resto del valor apareció al preguntar sobre
quién actúa la campaña, no a quién convierte. Sin experimento no hay respuesta a ninguna de las dos
preguntas.

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Me llaman para ofrecerme lo mismo siempre» | Contacto a clientes seguros | 14, clase 5 |
| «Me ofrecieron algo justo cuando lo necesitaba» | Segmento persuadible bien identificado | 14, clase 5 |
| «Me llamaron y terminé cambiándome» | Efecto contraproducente | 14, clase 5 |
| «Recibo demasiadas ofertas» | Saturación por campañas sin dirigir | 10, clase 15 |
| «El banco parece conocerme» | Analítica bien aplicada | 14, clase 6 |

## 🧪 Práctica

En `labs/lab-03.md`:

1. Formula tres preguntas de negocio en las cuatro partes y clasifícalas.
2. Diseña un experimento con grupo de control y calcula el tamaño de muestra necesario.
3. Calcula el efecto incremental y su intervalo de confianza.
4. Segmenta la elevación e identifica persuadibles y contraproducentes.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Conversión alta se lee como éxito | Sin grupo de control | Mide el efecto incremental. |
| Se compara con quien no aceptó | Sesgo de selección | Asignación aleatoria. |
| Se compara antes y después | El entorno cambió | Control simultáneo. |
| Se contacta al de mayor propensión | Contrata igual | Contacta al persuadible. |
| Se reporta un número sin rango | Falsa precisión | Presenta el intervalo. |
| Significancia sin relevancia | Efecto irrelevante en dinero | Traduce a unidades de negocio. |

## ❓ Preguntas de comprobación

1. ¿Por qué predicción y causalidad identifican grupos distintos?
2. ¿Qué hace válida la comparación en un experimento controlado?
3. ¿Qué es un cliente contraproducente y por qué se subestima?
4. ¿Por qué significancia no es lo mismo que relevancia?
5. ¿Qué debe contener una comunicación analítica útil?

## 📥 Entregable

Guarda en `portfolio/parte-14/clase-05/`:

- las tres preguntas formuladas y clasificadas;
- el experimento diseñado con su tamaño de muestra;
- el efecto incremental calculado con su intervalo;
- la segmentación de elevación con la campaña rediseñada.

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

- Angrist, J. y Pischke, J. (2014). *Mastering 'Metrics: The Path from Cause to Effect*. Princeton University Press.
- Imbens, G. y Rubin, D. (2015). *Causal Inference for Statistics, Social, and Biomedical Sciences*. Cambridge University Press.
- Kohavi, R., Tang, D. y Xu, Y. (2020). *Trustworthy Online Controlled Experiments*. Cambridge University Press.
- Provost, F. y Fawcett, T. (2013). *Data Science for Business*. O'Reilly.
- Radcliffe, N. y Surry, P. (2011). "Real-World Uplift Modelling with Significance-Based Uplift Trees". Stochastic Solutions.
- Verificación local: revisa las obligaciones sobre comunicaciones comerciales y consentimiento de contacto aplicables en tu país.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 04 · Datos en un banco](04-datos-en-un-banco.md) | [Parte 14](../README.md) · [Programa](../../../SYLLABUS.md) | [06 · Inteligencia artificial en banca →](06-inteligencia-artificial-en-banca.md) |
<!-- gen:footer:end -->
