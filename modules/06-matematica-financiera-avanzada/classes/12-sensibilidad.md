---
part: 7
class: 12
title: "Sensibilidad"
level: avanzado
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 12 · Sensibilidad

> [← 11 · Duración y convexidad](11-duracion-y-convexidad.md) · [Índice de la parte](../README.md) · [13 · Escenarios y simulación →](13-escenarios-y-simulacion.md)

**Parte 07 — Matemática financiera avanzada** · **Nivel:** Avanzado — perfil analista · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Reemplazar el número único por el rango informado. Todo modelo financiero descansa en supuestos, y el
análisis de sensibilidad responde la pregunta que un comité siempre hace: **¿qué tendría que pasar
para que esta decisión fuera equivocada?** Esta clase entrega las cuatro técnicas y el criterio para
presentar sus resultados.

## 📚 Objetivos

Al finalizar podrás:

1. **Construir** análisis de sensibilidad univariante y bivariante.
2. **Identificar** las variables críticas con un diagrama de tornado.
3. **Calcular** valores de equilibrio y márgenes de seguridad.
4. **Distinguir** sensibilidad de escenarios y de simulación.
5. **Presentar** resultados de forma que orienten la decisión.

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
| `sensibilidad univariante` | Cambia una variable a la vez, con las demás fijas. |
| `sensibilidad bivariante` | Tabla de dos variables simultáneas. Muestra interacciones. |
| `diagrama de tornado` | Gráfico que ordena las variables por su impacto. Identifica las críticas. |
| `valor de equilibrio` | Valor de una variable que hace el resultado igual a cero o al umbral. |
| `margen de seguridad` | Distancia porcentual entre el valor esperado y el de equilibrio. |
| `elasticidad del resultado` | `%Δ resultado / %Δ variable`. Permite comparar variables de distinta unidad. |

## 🧠 Modelo mental

Un modelo tiene muchos supuestos y **solo unos pocos importan**:

```text
20 supuestos en un modelo
  → 3 o 4 explican el 80 % de la variación del resultado
  → el resto es ruido que consume tiempo de análisis
```

El análisis de sensibilidad existe para **encontrar esos tres o cuatro** y concentrar en ellos el
esfuerzo de estimación, de negociación y de seguimiento.

## 📖 Desarrollo

### 1. Sensibilidad univariante

Se varía cada supuesto en un rango razonable manteniendo los demás en su valor base:

```text
proyecto con VAN base de 42 000

Variable            Base      −20 %     +20 %     Rango de VAN
volumen             12 000    −18 400   102 400   120 800
precio unitario      8 500    −34 600   118 600   153 200
costo variable       4 900     96 200   −12 200   108 400
costo fijo         18 000     58 300    25 700    32 600
inversión         180 000     78 000     6 000    72 000
WACC                12,0 %    71 400    18 900    52 500
```

**Regla de construcción:** el rango de variación debe ser **realista para cada variable**, no un ±20 %
uniforme. Un WACC puede variar ±3 puntos; un precio unitario, ±25 %; una inversión ya cotizada, ±5 %.

### 2. Diagrama de tornado

Ordenando las variables por amplitud del rango:

```text
precio unitario   ████████████████████████  153 200
volumen           ███████████████████       120 800
costo variable    █████████████████         108 400
inversión         ███████████               72 000
WACC              ████████                  52 500
costo fijo        █████                     32 600
```

Lectura inmediata:

```text
las tres primeras variables explican la mayor parte de la incertidumbre
→ concentrar el esfuerzo de estimación ahí
→ el costo fijo, aunque importante contablemente, es poco relevante para la decisión
```

### 3. Valores de equilibrio y margen de seguridad

```text
valor de equilibrio = valor de la variable que hace VAN = 0
margen de seguridad = (valor base − valor de equilibrio)/valor base
```

| Variable | Base | Equilibrio | Margen de seguridad |
|---|---:|---:|---:|
| Volumen | 12 000 | 9 340 | 22,2 % |
| Precio unitario | 8 500 | 7 620 | 10,4 % |
| Costo variable | 4 900 | 5 780 | 18,0 % |
| Inversión | 180 000 | 222 000 | 23,3 % |
| WACC | 12,0 % | 17,4 % | 45,0 % |

**El precio unitario tiene el menor margen de seguridad: basta una caída del 10,4 % para que el
proyecto deje de crear valor.** Ese es el hallazgo operativo del análisis, y define qué hay que
proteger contractualmente.

### 4. Sensibilidad bivariante

Cuando dos variables interactúan, la tabla cruzada muestra lo que las univariantes ocultan:

```text
VAN según precio unitario y volumen (miles)

              volumen
precio      9 000    10 500    12 000    13 500    15 000
  7 500    −52 100   −24 800     2 500    29 800    57 100
  8 000    −28 400      3 100    34 600    66 100    97 600
  8 500     −4 700     31 000    42 000    102 400   138 100
  9 000     19 000     58 900   102 400   145 900   189 400
  9 500     42 700     86 800   146 200   189 400   240 700
```

```text
FRONTERA DE VAN = 0: la línea que separa las celdas negativas de las positivas
combinaciones inviables: precio ≤ 8 000 con volumen ≤ 10 500
```

La tabla permite formular la conclusión de forma accionable: **"el proyecto es viable si el precio se
mantiene sobre 8 000 y el volumen sobre 10 500; si el precio cae a 7 500 se requiere un volumen
superior a 11 600"**.

### 5. Elasticidad del resultado

Para comparar variables con unidades distintas:

```text
elasticidad = (%Δ VAN)/(%Δ variable)
```

| Variable | %Δ variable | %Δ VAN | Elasticidad |
|---|---:|---:|---:|
| Precio unitario | +10 % | +90,7 % | 9,07 |
| Volumen | +10 % | +71,9 % | 7,19 |
| Costo variable | +10 % | −64,5 % | −6,45 |
| Inversión | +10 % | −42,9 % | −4,29 |
| Costo fijo | +10 % | −19,4 % | −1,94 |

**Una elasticidad de 9,07 significa que un 1 % de variación en el precio mueve el VAN un 9 %.** Esa
métrica hace comparables variables medidas en unidades, en pesos y en porcentaje.

## 🧮 Ejemplo guiado

**Situación.** Un banco evalúa el financiamiento de un proyecto agroindustrial por 2 400 millones. El
comité pide el análisis de sensibilidad antes de decidir.

```text
SUPUESTOS BASE
  producción anual            4 200 toneladas
  precio de venta            980 000 por tonelada
  costo variable             560 000 por tonelada
  costos fijos               720 millones/año
  inversión                2 400 millones
  vida del proyecto             8 años
  WACC                         13,5 %
  tasa del crédito             11,2 %
  plazo del crédito              7 años
```

**Paso 1 — resultado base.**

```text
margen de contribución = (980 000 − 560 000) × 4 200 = 1 764 millones
resultado operativo = 1 764 − 720 = 1 044 millones
a(8; 13,5%) = 4,7716
VAN = 1 044 × 4,7716 − 2 400 = 4 981 − 2 400 = 2 581 millones
```

**Paso 2 — sensibilidad univariante con rangos realistas.**

| Variable | Rango realista | VAN mínimo | VAN máximo | Amplitud |
|---|---|---:|---:|---:|
| Precio | ±30 % (volatilidad histórica) | −3 315 | 8 477 | 11 792 |
| Producción | −25 % / +10 % | 481 | 3 421 | 2 940 |
| Costo variable | ±15 % | 1 098 | 4 064 | 2 966 |
| Costos fijos | ±10 % | 2 237 | 2 925 | 688 |
| WACC | ±2,5 pp | 2 044 | 3 219 | 1 175 |
| Inversión | +15 % / −5 % | 2 221 | 2 701 | 480 |

**Paso 3 — tornado y variables críticas.**

```text
precio            ████████████████████████  11 792
costo variable    ██████                     2 966
producción        ██████                     2 940
WACC             ██                          1 175
costos fijos      █                            688
inversión         █                            480
```

**El precio domina completamente.** Su amplitud es cuatro veces la de la siguiente variable.

**Paso 4 — valores de equilibrio del precio.**

```text
VAN = 0 cuando:
  resultado operativo × 4,7716 = 2 400
  resultado operativo = 502,97
  margen de contribución = 502,97 + 720 = 1 222,97
  (P − 560 000) × 4 200 = 1 222 970 000
  P − 560 000 = 291 183
  P equilibrio = 851 183

margen de seguridad = (980 000 − 851 183)/980 000 = 13,1 %
```

**Paso 5 — contrasta con la volatilidad histórica del precio.**

```text
serie histórica del precio (10 años):
  media 945 000 · desviación estándar 178 000 · coeficiente de variación 18,8 %
  mínimo observado 621 000 (hace 4 años)
  precio actual 980 000, un 3,7 % sobre la media histórica

probabilidad estimada de que el precio caiga bajo 851 183:
  z = (851 183 − 945 000)/178 000 = −0,527
  probabilidad ≈ 30 %
```

**Hay aproximadamente un 30 % de probabilidad de que el precio promedio del proyecto caiga bajo el
punto de equilibrio.** Esa cifra —no el VAN de 2 581 millones— es la que el comité necesita.

**Paso 6 — decisión y estructura de mitigación.**

```text
el VAN base es atractivo y el margen de seguridad del precio es delgado (13,1 %)

CONDICIONES PARA APROBAR:
1. contratos de venta a precio mínimo garantizado por al menos el 60 % de la producción
   → eleva el precio de equilibrio efectivo y reduce la probabilidad de pérdida a ~12 %
2. covenant de cobertura de servicio de deuda mínima de 1,25 veces, medida anualmente
3. cuenta de reserva del servicio de deuda equivalente a 6 meses
4. estructura de amortización con cuotas crecientes, alineada con la maduración del cultivo
5. seguimiento trimestral del precio de mercado, con umbral de alerta en 880 000

sin la condición 1, la operación NO se aprueba:
  la exposición al precio de un único commodity, sin cobertura, con un margen
  de seguridad del 13 %, excede el apetito de riesgo del banco para este sector
```

**Interpreta:** el VAN de 2 581 millones parecía holgado. **El análisis de sensibilidad mostró que
todo el proyecto depende de una sola variable y que su margen de seguridad es del 13 %**, con un 30 %
de probabilidad histórica de cruzarlo. Esa información transformó una aprobación simple en una
aprobación condicionada con cinco mitigantes concretos.

## 🏦 Del cliente al banco

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| Variables críticas | Foco del análisis de crédito | 9, clase 9 |
| Margen de seguridad | Criterio de aprobación | 13, clase 13 |
| Frontera de viabilidad | Diseño de covenants | 13, clase 10 |
| Elasticidad del resultado | Priorización del seguimiento | 11, clase 12 |
| Sensibilidad al WACC | Riesgo de tasa del proyecto | 11, clase 5 |

## 🧪 Práctica

En `labs/lab-06.md`, sección de sensibilidad:

1. Construye el análisis univariante de un proyecto con rangos realistas justificados.
2. Elabora el diagrama de tornado e identifica las variables críticas.
3. Calcula valores de equilibrio y márgenes de seguridad de las tres variables principales.
4. Construye una tabla bivariante y traza la frontera de viabilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se usa ±20 % para todas las variables | Rango no realista | Ajusta el rango a la volatilidad de cada variable. |
| Se analizan veinte variables por igual | Sin priorización | Usa el tornado para identificar las críticas. |
| Se presenta un VAN puntual | Sensibilidad omitida | Presenta rango, equilibrio y margen de seguridad. |
| Las variables se mueven de forma independiente | Correlaciones ignoradas | Usa tabla bivariante o simulación (clase 13). |
| El margen de seguridad no se contrasta con datos | Sin base empírica | Compara con la volatilidad histórica. |
| No se derivan mitigantes | Análisis sin consecuencia | Cada variable crítica debe tener un mitigante. |

## ❓ Preguntas de comprobación

1. ¿Cómo se elige el rango de variación de cada variable?
2. ¿Qué muestra un diagrama de tornado y para qué sirve?
3. Calcula el margen de seguridad de una variable con base 500 y equilibrio 430.
4. ¿Qué muestra una tabla bivariante que la univariante oculta?
5. ¿Por qué la elasticidad del resultado permite comparar variables de distinta unidad?

## 📥 Entregable

Guarda en `portfolio/parte-07/clase-12/`:

- el análisis univariante con rangos justificados por variable;
- el diagrama de tornado con las variables críticas identificadas;
- los valores de equilibrio y márgenes de seguridad contrastados con datos históricos;
- la tabla bivariante con la frontera de viabilidad y los mitigantes derivados.

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

- Brealey, R., Myers, S. y Allen, F. (2023). *Principios de finanzas corporativas* (14.ª ed.). McGraw-Hill. Capítulo 10: análisis de proyectos y sensibilidad.
- Benninga, S. (2014). *Financial Modeling* (4.ª ed.). MIT Press. Construcción de tablas de sensibilidad y de datos.
- Damodaran, A. (2012). *Investment Valuation* (3.ª ed.). Wiley. Capítulo 6: análisis de escenarios y de sensibilidad.
- Savage, S. (2012). *The Flaw of Averages*. Wiley. Por qué un valor puntual induce a error en decisiones bajo incertidumbre.
- Ross, S., Westerfield, R. y Jaffe, J. (2021). *Corporate Finance* (12.ª ed.). McGraw-Hill. Capítulo 7: punto de equilibrio y análisis de riesgo del proyecto.
- Verificación local: usa series históricas de precios del sector correspondiente publicadas por organismos oficiales de tu país para justificar los rangos.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 11 · Duración y convexidad](11-duracion-y-convexidad.md) | [Parte 07](../README.md) · [Programa](../../../SYLLABUS.md) | [13 · Escenarios y simulación →](13-escenarios-y-simulacion.md) |
<!-- gen:footer:end -->
