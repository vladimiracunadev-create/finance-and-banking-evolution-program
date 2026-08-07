<!-- meta
part: 7
class: 9
title: "Tasa interna de retorno"
level: avanzado
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 09 · Tasa interna de retorno

> [← 08 · Valor actual neto](08-valor-actual-neto.md) · [Índice de la parte](../README.md) · [10 · Payback y rentabilidad →](10-payback-y-rentabilidad.md)

**Parte 07 — Matemática financiera avanzada** · **Nivel:** Avanzado — perfil analista · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Manejar el indicador más popular de evaluación de proyectos y —precisamente por popular— el más
malinterpretado. La TIR es intuitiva, comunicable y tiene tres problemas estructurales que pueden
invertir una decisión. Esta clase enseña a calcularla, a reconocer cuándo falla y a usar la TIR
modificada cuando corresponde.

El VAN de la clase anterior da una cifra en dinero. La TIR da un porcentaje, que se comunica mejor y por eso se usa más. Esta clase la calcula y, sobre todo, delimita sus tres problemas conocidos, porque usarla sin conocerlos lleva a ordenar mal los proyectos.

## 📚 Objetivos

Al finalizar podrás:

1. **Calcular** la TIR por iteración y verificar el resultado.
2. **Aplicar** la regla de decisión y sus condiciones de validez.
3. **Identificar** los tres problemas de la TIR con ejemplos concretos.
4. **Calcular** la TIR modificada y explicar qué corrige.
5. **Elegir** entre TIR y VAN según la situación.

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

Los dos primeros términos son el indicador y su regla; los cinco siguientes, sus problemas y sus correcciones. La **TIR modificada** es la respuesta al más grave de ellos: la TIR supone que los flujos se reinvierten a la propia TIR, que casi nunca es realista.

| Concepto | Comprensión verificable |
|---|---|
| `TIR` | Tasa que hace `VAN = 0`. Rendimiento implícito del proyecto. |
| `regla de decisión` | Aceptar si `TIR > tasa de descuento`. Válida solo bajo condiciones. |
| `TIR múltiple` | Cuando el flujo cambia de signo más de una vez, puede haber varias TIR. |
| `supuesto de reinversión` | La TIR supone reinvertir los flujos a la propia TIR, lo que rara vez es realista. |
| `problema de escala` | La TIR ignora el tamaño: 40 % sobre 10 puede valer menos que 15 % sobre 1 000. |
| `TIR modificada (TIRM)` | Corrige el supuesto de reinversión usando una tasa explícita. |
| `tasa de Fisher` | Tasa a la que dos proyectos tienen el mismo VAN. Marca dónde se cruza el orden. |

## 🧠 Modelo mental

La TIR es **el rendimiento que el proyecto entrega sobre el capital que mantiene invertido**:

```text
VAN = 0  ⟺  el proyecto rinde exactamente la tasa de descuento
TIR > k  ⟺  el proyecto rinde más que la alternativa  ⟺  VAN > 0
```

La equivalencia es exacta para un proyecto convencional. Los problemas aparecen cuando el proyecto no
es convencional o cuando se comparan proyectos entre sí.

## 📖 Desarrollo

### 1. Cálculo por iteración

La TIR no tiene solución cerrada y se obtiene por aproximaciones sucesivas. El procedimiento siguiente converge en pocas iteraciones y sirve para hacerlo a mano.

```text
se busca r tal que:  Σ FCF_t/(1+r)^t = 0
```

Método de bisección:

```text
FCF: −100 000, 35 000, 40 000, 45 000, 30 000

r = 10 %  → VAN = +18 372
r = 20 %  → VAN =  −1 435
r = 19 %  → VAN =   +332
r = 19,2 % → VAN =    −20
TIR ≈ 19,19 %
```

Verificación obligatoria:

```text
35 000/1,1919 + 40 000/1,1919² + 45 000/1,1919³ + 30 000/1,1919⁴
= 29 365 + 28 158 + 26 578 + 14 866 = 98 967 ≈ 100 000 ✔ (diferencia por redondeo de r)
```

### 2. Problema 1 — TIR múltiple

Un flujo convencional cambia de signo una sola vez: `−, +, +, +`. Cuando cambia más de una vez, puede
haber tantas TIR como cambios de signo.

```text
proyecto minero: −60 000, +155 000, −100 000
  (inversión, operación, cierre y remediación)

r = 10 %  → VAN = −1 736
r = 25 %  → VAN = +60
r = 50 %  → VAN = +819
r = 100 % → VAN = +2 500... 
```

Resolviendo, este flujo tiene **dos TIR**: aproximadamente 23,7 % y 143,0 %. Ambas hacen VAN = 0.

```text
¿la regla "aceptar si TIR > 10 %" se aplica a cuál de las dos?
→ la pregunta no tiene respuesta: la regla NO ES APLICABLE
```

En estos casos se decide por VAN, que siempre tiene un único valor para una tasa dada.

### 3. Problema 2 — supuesto de reinversión

La TIR supone algo que rara vez se cumple, y ese supuesto la infla. El esquema muestra el mecanismo.

```text
la TIR supone implícitamente que los flujos intermedios
se reinvierten a la propia TIR hasta el final del proyecto
```

Puesto sobre una cifra concreta, el supuesto deja de sonar razonable: basta compararlo con el costo de capital de la propia empresa.

```text
proyecto con TIR de 38 %
¿es realista suponer que los flujos anuales se reinvertirán al 38 %?
  si la empresa tiene un WACC de 11 %, lo realista es reinvertir al 11 %
```

El efecto es que **la TIR sobrestima el rendimiento efectivo** de proyectos con TIR muy superior a la
tasa de descuento. Cuanto mayor la brecha, mayor la sobrestimación.

### 4. Problema 3 — escala y orden

Dos proyectos de tamaños distintos pueden ordenarse al revés por TIR y por VAN. El contraste siguiente lo muestra.

```text
Proyecto A: −10 000, +14 000        TIR = 40,0 %, VAN al 10 % = +2 727
Proyecto B: −100 000, +125 000      TIR = 25,0 %, VAN al 10 % = +13 636

por TIR:  A > B
por VAN:  B > A
```

**Con capital disponible, B crea cinco veces más valor.** La TIR ordena mal porque ignora la escala.

El punto donde se cruzan los órdenes es la **tasa de Fisher**:

```text
se busca k tal que VAN(A) = VAN(B)
−10 000 + 14 000/(1+k) = −100 000 + 125 000/(1+k)
111 000/(1+k) = 90 000
k = 23,33 %

para k < 23,33 % → B es mejor por VAN
para k > 23,33 % → A es mejor por VAN
```

### 5. TIR modificada

La TIRM corrige el supuesto de reinversión usando una tasa realista. El procedimiento la calcula.

```text
TIRM = [VF de las entradas a la tasa de reinversión / VP de las salidas a la tasa de financiamiento]^(1/n) − 1
```

Sobre el mismo flujo de antes, la tasa modificada se calcula en dos etapas y entrega un resultado que sí es comparable entre proyectos.

```text
FCF: −100 000, 35 000, 40 000, 45 000, 30 000
tasa de reinversión = WACC = 11 %
tasa de financiamiento = 11 %

VF de entradas al año 4:
  35 000 × 1,11³ + 40 000 × 1,11² + 45 000 × 1,11 + 30 000
  = 47 866 + 49 284 + 49 950 + 30 000 = 177 100

VP de salidas = 100 000

TIRM = (177 100/100 000)^(1/4) − 1 = (1,771)^0,25 − 1 = 15,40 %
```

```text
TIR    = 19,19 %
TIRM   = 15,40 %
diferencia: 3,79 puntos, que es la sobrestimación del supuesto de reinversión
```

La TIRM además **siempre tiene solución única**, lo que resuelve también el problema de TIR múltiple.

## 🧮 Ejemplo guiado

**Situación.** Un comité de inversiones evalúa tres proyectos mutuamente excluyentes con un WACC de
12 %.

```text
Proyecto   Año 0      Año 1     Año 2     Año 3     Año 4
   A      −180 000    75 000    75 000    75 000    75 000
   B      −180 000    30 000    50 000    80 000   140 000
   C      −450 000   140 000   150 000   160 000   170 000
```

**Paso 1 — calcula TIR y VAN.**

| Proyecto | TIR | VAN al 12 % |
|---|---:|---:|
| A | 24,08 % | 47 810 |
| B | 21,44 % | 41 305 |
| C | 14,03 % | 20 452 |

**Paso 2 — el conflicto aparente.**

```text
por TIR:  A > B > C
por VAN:  A > B > C
→ en este caso coinciden, pero hay que verificar el motivo
```

Coinciden porque A y B tienen la misma inversión, y C, pese a ser mayor, tiene un rendimiento
sustancialmente menor.

**Paso 3 — calcula la TIRM con reinversión al WACC.**

```text
A: VF entradas = 75 000 × (1,12³ + 1,12² + 1,12 + 1) = 75 000 × 4,77933 = 358 450
   TIRM = (358 450/180 000)^0,25 − 1 = 18,80 %

B: VF entradas = 30 000×1,12³ + 50 000×1,12² + 80 000×1,12 + 140 000
                = 42 148 + 62 720 + 89 600 + 140 000 = 334 468
   TIRM = (334 468/180 000)^0,25 − 1 = 16,73 %

C: VF entradas = 140 000×1,12³ + 150 000×1,12² + 160 000×1,12 + 170 000
                = 196 691 + 188 160 + 179 200 + 170 000 = 734 051
   TIRM = (734 051/450 000)^0,25 − 1 = 13,00 %
```

| Proyecto | TIR | TIRM | Diferencia |
|---|---:|---:|---:|
| A | 24,08 % | 18,80 % | −5,28 pp |
| B | 21,44 % | 16,73 % | −4,71 pp |
| C | 14,03 % | 13,00 % | −1,03 pp |

**La TIR sobrestima más cuanto mayor es su distancia respecto del WACC.**

**Paso 4 — el escenario que cambia la conclusión.**

Supongamos que el comité tiene 450 000 disponibles y los proyectos **no** son mutuamente excluyentes:

```text
opción 1: proyecto C solo             → VAN 20 452
opción 2: A + B (360 000)             → VAN 89 115, sobran 90 000
opción 3: A + B + 90 000 al WACC      → VAN 89 115 (el excedente rinde exactamente el WACC)
```

**A + B crea 4,4 veces más valor que C.** La TIR de C (14,03 %) superaba el WACC, así que era
"aceptable", y aun así es la peor asignación del capital disponible.

**Paso 5 — verifica el flujo de C por si hay TIR múltiple.**

```text
signos: −, +, +, +, +  → un solo cambio de signo → TIR única ✔
```

**Paso 6 — recomendación del comité.**

```text
APROBAR A y B; RECHAZAR C

fundamento:
  · A + B: VAN conjunto 89 115 con inversión de 360 000
  · C: VAN 20 452 con inversión de 450 000
  · el índice de rentabilidad confirma: A = 1,27 · B = 1,23 · C = 1,05

nota metodológica para el acta:
  la decisión se toma por VAN. La TIR se reporta como referencia comunicable,
  y la TIRM se incluye porque la brecha TIR−TIRM de A (5,28 pp) indica que
  el rendimiento comunicado supone una reinversión no disponible.
```

**Interpreta:** los tres proyectos tenían TIR superior al WACC y por lo tanto eran "aceptables". **La
decisión de asignación no la resuelve la TIR: la resuelve el VAN combinado con la restricción de
capital.** Y la TIRM aporta el matiz de cuánto de la TIR reportada es real.

## 🏦 Del cliente al banco

El cliente presenta una TIR y el banco comprueba la escala y el supuesto de reinversión. La tabla enfrenta las dos lecturas.

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| TIR | Rendimiento de una operación de crédito | 3, clase 13 |
| TIR de un flujo de crédito | Es exactamente la CAE | 3, clase 13 |
| TIR múltiple | Operaciones con flujos no convencionales | 13, clase 4 |
| Supuesto de reinversión | Comparación de alternativas de inversión | 8, clase 8 |
| VAN sobre TIR | Criterio en comités de inversión | 13, clase 13 |

## 🧪 Práctica

El laboratorio pide ordenar proyectos por TIR y por VAN y explicar la discrepancia. La discrepancia está construida a propósito, y explicarla es el objetivo.

En `labs/lab-05.md`:

1. Calcula la TIR de cinco proyectos por bisección y verifica cada resultado.
2. Construye un flujo con TIR múltiple y grafica el VAN en función de la tasa.
3. Calcula la TIRM de tres proyectos y cuantifica la sobrestimación de la TIR.
4. Resuelve un caso de asignación de capital donde TIR y VAN ordenan distinto.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen decisiones de inversión mal ordenadas. Las causas son los tres problemas de la TIR, y cada uno tiene su corrección.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se elige el proyecto de mayor TIR | Escala ignorada | Decide por VAN. |
| Aparecen dos TIR | Flujo no convencional | Usa VAN o TIRM. |
| Se comunica una TIR muy alta como rendimiento efectivo | Supuesto de reinversión | Reporta también la TIRM. |
| Se acepta todo proyecto con TIR > WACC | Restricción de capital ignorada | Ordena por índice de rentabilidad. |
| No se verifica la TIR obtenida | Error de iteración | Recalcula el VAN a esa tasa: debe dar cero. |
| Se compara TIR entre proyectos de distinta duración | Bases distintas | Usa VAN anualizado o TIRM con el mismo horizonte. |

## ❓ Preguntas de comprobación

1. ¿Qué significa exactamente la TIR y cuándo su regla es válida?
2. ¿Cuándo puede haber TIR múltiple y cómo se decide en ese caso?
3. ¿Qué supone la TIR sobre la reinversión y por qué importa?
4. Calcula la TIRM de un proyecto con TIR de 30 % y WACC de 10 %, y explica la diferencia.
5. Dos proyectos, TIR 35 % y 18 %. ¿Cuál eliges y qué necesitas saber antes?

## 📥 Entregable

Guarda en `portfolio/parte-07/clase-09/`:

- las cinco TIR calculadas por bisección con su verificación;
- el flujo con TIR múltiple y el gráfico de VAN contra tasa;
- las TIRM calculadas con la sobrestimación cuantificada;
- el caso de asignación de capital resuelto con la justificación del criterio elegido.

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

- Brealey, R., Myers, S. y Allen, F. (2023). *Principios de finanzas corporativas* (14.ª ed.). McGraw-Hill. Capítulo 5: problemas de la TIR.
- Ross, S., Westerfield, R. y Jaffe, J. (2021). *Corporate Finance* (12.ª ed.). McGraw-Hill. Capítulo 6: TIR, TIR múltiple y comparación con VAN.
- Damodaran, A. (2012). *Investment Valuation* (3.ª ed.). Wiley. Capítulo 5: limitaciones de la TIR.
- Blank, L. y Tarquin, A. (2018). *Ingeniería económica* (8.ª ed.). McGraw-Hill. Capítulo 7: análisis de tasa de retorno y TIR múltiple.
- Kierulff, H. (2008). "MIRR: A Better Measure". *Business Horizons*, 51(4). Fundamento y uso de la TIR modificada.
- Verificación local: verifica cómo define la CAE tu normativa: es la TIR del flujo del crédito expresada en base anual.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 08 · Valor actual neto](08-valor-actual-neto.md) | [Parte 07](../README.md) · [Programa](../../../SYLLABUS.md) | [10 · Payback y rentabilidad →](10-payback-y-rentabilidad.md) |
<!-- gen:footer:end -->
