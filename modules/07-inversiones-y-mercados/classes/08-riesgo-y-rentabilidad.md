<!-- meta
part: 8
class: 8
title: "Riesgo y rentabilidad"
level: avanzado
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 08 · Riesgo y rentabilidad

> [← 07 · Divisas y commodities](07-divisas-y-commodities.md) · [Índice de la parte](../README.md) · [09 · Diversificación →](09-diversificacion.md)

**Parte 08 — Inversiones y mercados** · **Nivel:** Avanzado — perfil analista · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Formalizar la relación que gobierna toda decisión de inversión: **mayor rentabilidad esperada exige
mayor riesgo**, y no al revés. Esta clase enseña a medir el riesgo, a distinguir el que se remunera
del que no, y a evaluar cualquier inversión ajustando por el riesgo asumido.

Las cinco clases anteriores describieron instrumentos. Esta introduce la medida que permite compararlos entre sí, y la separación que ordena toda la teoría de carteras: hay riesgo que se puede eliminar diversificando y riesgo que no, y solo el segundo se remunera.

## 📚 Objetivos

Al finalizar podrás:

1. **Medir** riesgo con desviación estándar, caída máxima y semidesviación.
2. **Distinguir** riesgo sistemático de específico y explicar por qué solo uno se remunera.
3. **Calcular** e interpretar beta, y sus límites.
4. **Evaluar** inversiones con medidas ajustadas por riesgo.
5. **Reconocer** las limitaciones de la desviación estándar como medida de riesgo.

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

Los dos primeros términos miden el riesgo total; los cinco siguientes lo descomponen y lo relacionan con la rentabilidad. La distinción entre riesgo **sistemático y específico** es la que justifica diversificar: asumir riesgo específico no aumenta la rentabilidad esperada, solo la incertidumbre.

| Concepto | Comprensión verificable |
|---|---|
| `desviación estándar` | Dispersión de los retornos alrededor de su media. Medida más usada, con límites conocidos. |
| `caída máxima (drawdown)` | Mayor pérdida desde un máximo hasta un mínimo posterior. Es lo que el inversionista experimenta. |
| `riesgo sistemático` | El que afecta a todo el mercado. **No se puede diversificar** y por eso se remunera. |
| `riesgo específico` | Propio de un emisor. Se elimina con diversificación y por eso **no se remunera**. |
| `beta (β)` | Sensibilidad de un activo respecto del mercado. β = 1 se mueve como el mercado. |
| `prima por riesgo` | Rentabilidad esperada por sobre la tasa libre de riesgo. |
| `ratio de Sharpe` | `(retorno − tasa libre)/desviación estándar`. Retorno por unidad de riesgo total. |

## 🧠 Modelo mental

El mercado remunera **solo el riesgo que no se puede evitar**:

```text
riesgo ESPECÍFICO     se elimina gratis con diversificación
                      → el mercado NO paga por asumirlo
                      → asumirlo es riesgo sin compensación

riesgo SISTEMÁTICO    no se puede eliminar
                      → el mercado paga una prima por asumirlo
```

De ahí la conclusión operativa más importante de la parte: **concentrar la cartera en pocos emisores
aumenta el riesgo sin aumentar el retorno esperado**. Es la única decisión de inversión que es
inequívocamente mala.

## 📖 Desarrollo

### 1. Medir el riesgo

**Desviación estándar:**

```text
σ = √[Σ(r_t − r̄)²/(n−1)]
```

Sobre una serie corta de retornos anuales, la medida se calcula en dos pasos y ya permite comparar activos entre sí.

```text
retornos anuales: 12,4 % · −8,1 % · 21,3 % · 4,7 % · −3,2 % · 16,8 %
media = 7,32 %
σ = 11,26 %
```

Interpretación bajo normalidad (aproximada):

```text
≈ 68 % de los años entre  −3,9 % y +18,6 %
≈ 95 % de los años entre −15,2 % y +29,8 %
```

**Caída máxima:**

```text
serie de valor: 100 → 118 → 131 → 96 → 112 → 145
máximo previo: 131 · mínimo posterior: 96
caída máxima = (96 − 131)/131 = −26,7 %
```

La caída máxima es **lo que el inversionista experimenta y lo que determina si vende**. Dos carteras
con la misma desviación estándar pueden tener caídas máximas muy distintas.

**Semidesviación (riesgo de caída):**

```text
solo considera los retornos bajo la media
σ_down = √[Σ(min(r_t − r̄, 0))²/(n−1)]
```

Útil porque **el inversionista no percibe como riesgo los retornos por sobre la media**. La desviación
estándar penaliza igual una sorpresa positiva que una negativa.

### 2. Sistemático y específico

El riesgo total de un activo se descompone en dos partes con tratamientos opuestos. El esquema las separa.

```text
riesgo total = riesgo sistemático + riesgo específico
```

Efecto de la diversificación:

| N° de acciones | Desviación estándar de la cartera | Reducción |
|---:|---:|---:|
| 1 | 45,0 % | — |
| 2 | 36,0 % | −20,0 % |
| 5 | 26,0 % | −42,2 % |
| 10 | 22,0 % | −51,1 % |
| 20 | 20,0 % | −55,6 % |
| 30 | 19,4 % | −56,9 % |
| 50 | 19,0 % | −57,8 % |
| 100 | 18,7 % | −58,4 % |
| Mercado completo | 18,5 % | −58,9 % |

```text
la mayor parte del beneficio se obtiene con 20–30 instrumentos
más allá, la reducción adicional es marginal
el piso de 18,5 % es el RIESGO SISTEMÁTICO: no se puede eliminar
```

### 3. Beta

La beta mide cuánto se mueve un activo respecto del mercado, y es la medida del riesgo sistemático. El procedimiento siguiente la calcula e indica cómo leerla.

```text
β = covarianza(activo, mercado) / varianza(mercado)
```

| β | Interpretación |
|---:|---|
| 0,0 | Sin relación con el mercado |
| 0,5 | Se mueve la mitad que el mercado |
| 1,0 | Se mueve como el mercado |
| 1,5 | Amplifica los movimientos en un 50 % |
| < 0 | Se mueve en dirección contraria |

```text
mercado sube 10 % · β = 1,4 → se espera que el activo suba 14 %
mercado cae 10 %  · β = 1,4 → se espera que caiga 14 %
```

Modelo de valoración de activos de capital:

```text
E(r) = r_f + β × (E(r_m) − r_f)
```

Con los tres parámetros del mercado, el modelo entrega el retorno que habría que exigir a ese activo para compensar su riesgo.

```text
r_f = 4,0 % · E(r_m) = 9,5 % · β = 1,4
E(r) = 4,0 + 1,4 × 5,5 = 11,7 %
```

**Límites de beta que hay que conocer:**

```text
· es una estimación histórica y cambia en el tiempo
· depende del índice de mercado y del periodo elegidos
· en crisis, las betas tienden a converger a 1: la diversificación
  funciona peor justo cuando más se necesita
· no captura riesgos que no se manifiestan en el periodo estimado
```

### 4. Medidas ajustadas por riesgo

Comparar rentabilidades sin ajustar por riesgo no dice nada. La tabla recoge las medidas ajustadas y qué compara cada una.

```text
Sharpe    = (r − r_f)/σ                     retorno por unidad de riesgo TOTAL
Treynor   = (r − r_f)/β                     retorno por unidad de riesgo SISTEMÁTICO
Sortino   = (r − r_f)/σ_down                penaliza solo la caída
Alfa      = r − [r_f + β(r_m − r_f)]        retorno sobre lo esperado dado el riesgo
Información = (r − r_índice)/error de seguimiento
```

Ejemplo comparado:

| Fondo | Retorno | σ | β | σ_down | Sharpe | Treynor | Sortino | Alfa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| P | 14,2 % | 22,4 % | 1,32 | 15,1 % | 0,455 | 7,73 | 0,675 | +2,94 % |
| Q | 10,8 % | 12,1 % | 0,71 | 7,4 % | 0,562 | 9,58 | 0,919 | +2,90 % |
| R | 16,5 % | 31,0 % | 1,85 | 24,8 % | 0,403 | 6,76 | 0,504 | +2,32 % |

```text
por retorno bruto:      R > P > Q
por Sharpe:             Q > P > R
por Sortino:            Q > P > R
por alfa:               P ≈ Q > R
```

**El fondo con mayor retorno (R) es el peor en toda medida ajustada por riesgo.** Su retorno superior
se explica por haber asumido más riesgo, no por habilidad.

### 5. Límites de la desviación estándar

La desviación estándar es la medida más usada y tiene supuestos que los mercados no cumplen. La tabla recoge sus límites.

```text
· supone distribución simétrica: los retornos financieros no lo son
· penaliza igual las sorpresas positivas y las negativas
· subestima el riesgo de eventos extremos (colas gruesas)
· es inestable: cambia según el periodo de estimación
· no captura el riesgo de iliquidez ni el de crédito
```

Evidencia de colas gruesas:

```text
bajo distribución normal, un movimiento de −5 desviaciones estándar
ocurriría aproximadamente una vez cada 14 000 años

en los mercados accionarios han ocurrido varios movimientos de esa magnitud
en el último siglo
```

Consecuencia práctica: **las medidas basadas en desviación estándar subestiman el riesgo de pérdidas
extremas**. Complementarlas con caída máxima y con pruebas de estrés es obligatorio.

## 🧮 Ejemplo guiado

El ejemplo calcula la beta y el ratio de Sharpe de dos activos y los ordena. El orden por rentabilidad y el orden ajustado por riesgo son distintos, y ese es el punto.

**Situación.** Un comité evalúa tres gestores externos con cinco años de historia.

```text
                    Gestor A   Gestor B   Gestor C   Índice
retorno anual         13,8 %     9,4 %     11,2 %     10,1 %
desviación estándar   19,6 %     8,7 %     14,2 %     13,4 %
beta                   1,38       0,58      1,02       1,00
caída máxima         −34,2 %   −12,8 %   −21,6 %    −20,3 %
peor año             −22,4 %    −4,1 %   −14,8 %    −13,9 %
error de seguimiento   9,8 %      7,2 %      3,1 %       —
tasa libre de riesgo   4,0 %
```

**Paso 1 — medidas ajustadas por riesgo.**

```text
Sharpe:  A = (13,8−4,0)/19,6 = 0,500
         B = (9,4−4,0)/8,7   = 0,621
         C = (11,2−4,0)/14,2 = 0,507
         Índice = (10,1−4,0)/13,4 = 0,455

Treynor: A = 9,8/1,38 = 7,10
         B = 5,4/0,58 = 9,31
         C = 7,2/1,02 = 7,06

Alfa:    A = 13,8 − [4,0 + 1,38×6,1] = 13,8 − 12,42 = +1,38 %
         B = 9,4 − [4,0 + 0,58×6,1] = 9,4 − 7,54 = +1,86 %
         C = 11,2 − [4,0 + 1,02×6,1] = 11,2 − 10,22 = +0,98 %

Información: A = (13,8−10,1)/9,8 = 0,378
             B = (9,4−10,1)/7,2 = −0,097
             C = (11,2−10,1)/3,1 = 0,355
```

**Paso 2 — el conflicto entre medidas.**

```text
por retorno:       A > C > B
por Sharpe:        B > C > A
por Treynor:       B > A > C
por alfa:          B > A > C
por información:   A > C > B
```

**Ninguna ordenación coincide con otra.** Eso es normal y significa que cada medida responde una
pregunta distinta.

**Paso 3 — qué pregunta responde cada medida.**

| Medida | Pregunta | Cuándo usarla |
|---|---|---|
| Sharpe | ¿Cuánto retorno por unidad de riesgo total? | Si el gestor es toda la cartera |
| Treynor | ¿Cuánto por unidad de riesgo sistemático? | Si el gestor es una parte de una cartera diversificada |
| Alfa | ¿Superó lo esperado dado su riesgo? | Para medir habilidad |
| Información | ¿Cuán consistente fue su desviación del índice? | Para evaluar gestión activa |

**Paso 4 — evalúa la significancia estadística.**

```text
con solo 5 años de datos, ¿es el alfa distinguible de cero?

error estándar del alfa ≈ error de seguimiento / √n
  A: 9,8/√5 = 4,38 %  → alfa de 1,38 % está muy dentro del error → NO significativo
  B: 7,2/√5 = 3,22 %  → alfa de 1,86 % NO significativo
  C: 3,1/√5 = 1,39 %  → alfa de 0,98 % NO significativo
```

**Ninguno de los tres alfas es estadísticamente distinguible de cero con cinco años de datos.** Este
es el hallazgo más importante y el que casi nunca se calcula: **se necesitan décadas de datos para
distinguir habilidad de suerte con confianza razonable**.

**Paso 5 — la caída máxima y su relevancia conductual.**

```text
A: caída máxima −34,2 %
   ¿el comité mantendría la asignación tras una caída del 34 %?
   la política declara pérdida máxima aceptable del 25 %
   → A EXCEDE el límite de la política
```

**Paso 6 — recomendación.**

```text
DECISIÓN

  · descartar A por exceder la pérdida máxima declarada en la política,
    independientemente de su retorno

  · entre B y C:
      B tiene mejor Sharpe, mejor Treynor, mejor alfa y menor caída máxima
      C tiene mejor ratio de información y menor error de seguimiento

      si el objetivo es exposición al mercado con bajo error de seguimiento → C
      si el objetivo es retorno ajustado por riesgo → B

  · RECOMENDACIÓN: 60 % C (núcleo, bajo error de seguimiento) + 40 % B (estabilizador)

  ADVERTENCIA OBLIGATORIA en el acta:
    ningún alfa es estadísticamente significativo con 5 años de datos.
    La selección se fundamenta en el perfil de riesgo y en la consistencia,
    NO en evidencia de habilidad. Se revisará con 3 años adicionales de historia.
```

**Interpreta:** el gestor de mayor retorno se descartó por exceder el límite de riesgo de la política.
Y **el cálculo de la significancia estadística del alfa** —cuatro líneas de aritmética— reveló que
ninguna diferencia de desempeño era distinguible del azar. Incluir esa advertencia en el acta es lo
que impide que la decisión se justifique después como "elegimos al mejor gestor".

## 🏦 Del cliente al banco

El cliente mira rentabilidad y el banco mide riesgo ajustado y consumo de capital. La tabla enfrenta las dos lecturas.

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| Riesgo sistemático | Base del capital económico | 11, clase 3 |
| Beta | Cálculo del costo del patrimonio | 13, clase 6 |
| Caída máxima | Límite de pérdida en mesas de negociación | 11, clase 12 |
| Colas gruesas | Limitación del valor en riesgo | 11, clase 3 |
| Significancia del alfa | Evaluación de gestores y de modelos | 12, clase 13 |

## 🧪 Práctica

El laboratorio pide calcular medidas de riesgo sobre series sintéticas y ordenar activos. El ejercicio incluye un activo con alta rentabilidad y peor Sharpe.

En `labs/lab-04.md`, sección de riesgo:

1. Calcula desviación estándar, caída máxima y semidesviación de tres series reales.
2. Estima la beta de un activo contra su índice y evalúa su estabilidad en subperiodos.
3. Calcula las cinco medidas ajustadas por riesgo de tres carteras y compara sus ordenaciones.
4. Evalúa la significancia estadística del alfa de un gestor.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen comparaciones que ignoran el riesgo. Las causas son la desviación usada sin sus límites y rentabilidades comparadas sin ajustar.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se elige por retorno bruto | Riesgo no ajustado | Usa Sharpe, Treynor o alfa. |
| Se concentra la cartera | Riesgo específico asumido sin compensación | Diversifica: el mercado no lo paga. |
| Se interpreta el alfa como habilidad | Significancia no evaluada | Calcula el error estándar del alfa. |
| Se confía solo en la desviación estándar | Colas gruesas y asimetría | Complementa con caída máxima. |
| Se supone beta estable | Cambia en el tiempo y en crisis | Estímala en subperiodos. |
| Se ignora la caída máxima | Es lo que determina la conducta | Compárala con la pérdida máxima de la política. |

## ❓ Preguntas de comprobación

1. ¿Por qué el mercado no remunera el riesgo específico?
2. ¿Cuántos instrumentos capturan la mayor parte del beneficio de la diversificación?
3. Calcula el retorno esperado de un activo con β 1,25, tasa libre 4 % y prima de mercado 6 %.
4. ¿Qué pregunta responde el ratio de Sharpe y cuál el de Treynor?
5. ¿Por qué cinco años de datos no bastan para distinguir habilidad de suerte?

## 📥 Entregable

Guarda en `portfolio/parte-08/clase-08/`:

- las tres medidas de riesgo de tres series reales con su fuente;
- la beta estimada y su estabilidad en subperiodos;
- las cinco medidas ajustadas por riesgo de tres carteras con sus ordenaciones comparadas;
- la evaluación de significancia estadística del alfa de un gestor.

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

- Bodie, Z., Kane, A. y Marcus, A. (2023). *Investments* (13.ª ed.). McGraw-Hill. Capítulos 5 a 9: riesgo, retorno y modelos de valoración de activos.
- Sharpe, W. (1964). "Capital Asset Prices: A Theory of Market Equilibrium under Conditions of Risk". *Journal of Finance*.
- Sortino, F. y Van der Meer, R. (1991). "Downside Risk". *Journal of Portfolio Management*. Medición del riesgo de caída.
- Taleb, N. (2007). *The Black Swan*. Random House. Límites de la desviación estándar ante eventos extremos.
- Fama, E. y French, K. (2010). "Luck versus Skill in the Cross-Section of Mutual Fund Returns". *Journal of Finance*. Significancia estadística del alfa.
- Verificación local: usa índices accionarios y series de tasa libre de riesgo publicados por la bolsa y el banco central de tu país.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 07 · Divisas y commodities](07-divisas-y-commodities.md) | [Parte 08](../README.md) · [Programa](../../../SYLLABUS.md) | [09 · Diversificación →](09-diversificacion.md) |
<!-- gen:footer:end -->
