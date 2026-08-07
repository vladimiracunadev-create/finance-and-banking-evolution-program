<!-- meta
part: 7
class: 10
title: "Payback y rentabilidad"
level: avanzado
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 10 · Payback y rentabilidad

> [← 09 · Tasa interna de retorno](09-tasa-interna-de-retorno.md) · [Índice de la parte](../README.md) · [11 · Duración y convexidad →](11-duracion-y-convexidad.md)

**Parte 07 — Matemática financiera avanzada** · **Nivel:** Avanzado — perfil analista · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Completar el conjunto de criterios de evaluación con los indicadores de recuperación y de
rentabilidad, entendiendo qué aporta cada uno y qué no. El payback es el criterio más usado en la
práctica pese a sus defectos conocidos, y esa popularidad tiene una razón que conviene comprender
antes de descartarlo.

Las dos clases anteriores dan los dos indicadores principales. Esta añade los que se usan junto a ellos en la práctica y explica por qué se usan aunque sean teóricamente inferiores: responden a preguntas que el VAN no responde, empezando por cuánto tiempo está el dinero comprometido.

## 📚 Objetivos

Al finalizar podrás:

1. **Calcular** payback simple y descontado.
2. **Explicar** por qué el payback persiste pese a sus defectos.
3. **Calcular** el índice de rentabilidad y usarlo en asignación de capital.
4. **Comparar** los cinco criterios y saber cuándo usar cada uno.
5. **Construir** un tablero de evaluación multicriterio defendible.

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

Los cuatro primeros términos son indicadores complementarios; los dos últimos son la forma de combinarlos. El **criterio multicriterio** es lo que se hace en la práctica: ningún indicador decide solo, y el tablero que los reúne es lo que se lleva al comité.

| Concepto | Comprensión verificable |
|---|---|
| `payback simple` | Periodos hasta recuperar la inversión con flujos sin descontar. |
| `payback descontado` | Lo mismo con flujos descontados. Siempre mayor que el simple. |
| `índice de rentabilidad (IR)` | `VP de los flujos / inversión inicial`. Valor creado por unidad invertida. |
| `rentabilidad contable` | `resultado promedio / inversión promedio`. No es un criterio financiero: usa resultado, no caja. |
| `criterio multicriterio` | Uso conjunto de varios indicadores, cada uno con su propósito declarado. |
| `umbral de aceptación` | Valor mínimo exigido a cada indicador, definido por política. |

## 🧠 Modelo mental

Cada criterio responde una pregunta distinta:

```text
VAN     ¿cuánto valor crea?              → decisión
TIR     ¿qué rendimiento entrega?        → comunicación
IR      ¿cuánto valor por peso invertido? → asignación con capital limitado
Payback ¿cuándo recupero lo invertido?    → riesgo y liquidez
```

Usar uno solo es empobrecer la decisión; usarlos sin jerarquía es no decidir. **El VAN decide; los
demás informan.**

## 📖 Desarrollo

### 1. Payback simple y descontado

El payback mide cuándo se recupera lo invertido, con y sin descontar. El procedimiento siguiente calcula los dos.

```text
FCF: −120 000, 40 000, 45 000, 38 000, 32 000, 28 000
k = 12 %
```

**Simple:**

| Año | FCF | Acumulado |
|---:|---:|---:|
| 0 | −120 000 | −120 000 |
| 1 | 40 000 | −80 000 |
| 2 | 45 000 | −35 000 |
| 3 | 38 000 | +3 000 |

```text
payback simple = 2 + 35 000/38 000 = 2,92 años
```

**Descontado:**

| Año | FCF | Factor | VP | Acumulado |
|---:|---:|---:|---:|---:|
| 0 | −120 000 | 1,000000 | −120 000 | −120 000 |
| 1 | 40 000 | 0,892857 | 35 714 | −84 286 |
| 2 | 45 000 | 0,797194 | 35 874 | −48 412 |
| 3 | 38 000 | 0,711780 | 27 048 | −21 364 |
| 4 | 32 000 | 0,635518 | 20 337 | −1 027 |
| 5 | 28 000 | 0,567427 | 15 888 | +14 861 |

```text
payback descontado = 4 + 1 027/15 888 = 4,06 años
```

**La diferencia de 1,14 años** es el costo del tiempo, que el payback simple ignora por completo.

### 2. Por qué persiste el payback

Defectos conocidos:

```text
✗ ignora el valor del dinero en el tiempo (el simple)
✗ ignora todos los flujos posteriores al periodo de recuperación
✗ el umbral de aceptación es arbitrario
✗ puede rechazar proyectos de alto VAN con recuperación lenta
```

Y sin embargo se usa en la mayoría de las empresas. Las razones son reales:

```text
✓ mide RIESGO de forma intuitiva: cuanto antes recupero, menos expuesto estoy
✓ mide LIQUIDEZ: relevante para empresas con restricción de caja
✓ es fácil de comunicar y de comparar entre proyectos
✓ en entornos de alta incertidumbre, los flujos lejanos son poco confiables
✓ funciona como filtro rápido antes del análisis completo
```

La conclusión razonable: **el payback es un mal criterio de decisión y un buen indicador de riesgo**.
Su lugar es junto al VAN, no en su lugar.

### 3. Índice de rentabilidad

El índice de rentabilidad convierte el VAN en una medida por peso invertido, que es lo que hace falta cuando el capital está racionado.

```text
IR = VP de los flujos futuros / inversión inicial

IR > 1  ⟺  VAN > 0
```

Del ejemplo:

```text
VP de los flujos = 35 714 + 35 874 + 27 048 + 20 337 + 15 888 = 134 861
IR = 134 861/120 000 = 1,124
VAN = 14 861
```

Su utilidad aparece con **capital limitado**:

```text
presupuesto disponible: 300 000

Proyecto   Inversión   VP flujos   VAN      IR
   P        120 000     158 000    38 000   1,317
   Q        180 000     222 000    42 000   1,233
   R        100 000     127 000    27 000   1,270
   S        150 000     181 000    31 000   1,207
```

Ordenando por VAN: Q, P, S, R → se eligen Q + P = 300 000, VAN = 80 000.
Ordenando por IR: P, R, Q, S → se eligen P + R + (80 000 de S proporcionalmente).

```text
si los proyectos son divisibles:
  P (120 000) + R (100 000) + 53 % de S (80 000)
  VAN = 38 000 + 27 000 + 0,533 × 31 000 = 81 523  ← mejor

si son indivisibles, se prueban combinaciones:
  P + R = 220 000, VAN 65 000, sobran 80 000
  Q + P = 300 000, VAN 80 000  ← mejor combinación factible
```

**Con proyectos indivisibles, el IR ordena pero no basta**: hay que evaluar combinaciones. Con
proyectos divisibles, el IR entrega directamente la asignación óptima.

### 4. Rentabilidad contable

La rentabilidad contable no descuenta y aun así se usa, porque es la que aparece en los estados financieros. Conviene saber calcularla y conocer su sesgo.

```text
tasa de rendimiento contable = resultado promedio / inversión promedio
```

El indicador se calcula con cifras contables, no de caja, y eso se aprecia al desarrollarlo sobre una inversión con valor residual.

```text
resultado contable promedio 18 000 · inversión 120 000 · valor residual 20 000
inversión promedio = (120 000 + 20 000)/2 = 70 000
TRC = 18 000/70 000 = 25,7 %
```

**No es un criterio financiero:**

```text
✗ usa resultado contable, no flujo de caja
✗ ignora el valor del dinero en el tiempo
✗ depende de las políticas de depreciación
✗ el promedio oculta el perfil temporal
```

Se incluye aquí porque aparece en la práctica y hay que saber por qué **no debe usarse para decidir**.
Su único uso legítimo: verificar la consistencia con los estados financieros proyectados que se
presentarán a terceros.

### 5. Tablero multicriterio

El tablero reúne los indicadores con sus umbrales y hace visible cuándo se contradicen. La tabla muestra su forma.

```text
PROYECTO: ampliación de planta

  VAN al 12 %              +14 861      umbral: > 0            ✔
  TIR                       15,72 %     umbral: > 12 %         ✔
  TIRM                      13,84 %     referencia             —
  Índice de rentabilidad     1,124      umbral: > 1,10         ✔
  Payback simple             2,92 años  umbral: < 3,5 años     ✔
  Payback descontado         4,06 años  umbral: < 5,0 años     ✔
  Sensibilidad: VAN = 0 si  k > 15,7 % o volumen cae 11 %      ⚠
  
  DECISIÓN: aprobar, con seguimiento del supuesto de volumen
```

Reglas del tablero:

```text
1. el VAN es el criterio de DECISIÓN; los demás son de INFORMACIÓN
2. cada umbral debe estar en la política de inversiones, no inventarse por proyecto
3. si el VAN es positivo y un payback incumple el umbral, se documenta la excepción
4. la fila de sensibilidad es obligatoria
```

## 🧮 Ejemplo guiado

El ejemplo evalúa un proyecto con los cinco indicadores a la vez. Conviene fijarse en el caso en que se contradicen: resolver esa contradicción con criterio es el objetivo de la clase.

**Situación.** Un comité debe asignar 500 000 entre cuatro proyectos indivisibles, con WACC de 13 %.

```text
Proyecto  Inversión   FCF año 1-5 (anual)   Vida    Riesgo
   T       200 000        68 000            5 años  bajo
   U       150 000        48 000            5 años  bajo
   V       250 000        95 000            5 años  alto
   W       120 000        33 000            5 años  bajo
```

**Paso 1 — calcula todos los indicadores.**

```text
a(5; 13%) = [1 − 1,13^-5]/0,13 = 3,51723
```

| Proyecto | VP flujos | VAN | TIR | IR | Payback simple | Payback desc. |
|---|---:|---:|---:|---:|---:|---:|
| T | 239 172 | 39 172 | 20,89 % | 1,196 | 2,94 | 3,88 |
| U | 168 827 | 18 827 | 18,03 % | 1,126 | 3,13 | 4,29 |
| V | 334 137 | 84 137 | 26,25 % | 1,337 | 2,63 | 3,32 |
| W | 116 069 | −3 931 | 11,52 % | 0,967 | 3,64 | > 5 |

**Paso 2 — descarta W.**

```text
VAN negativo, TIR bajo el WACC, IR < 1 → RECHAZAR
```

**Paso 3 — ajusta V por riesgo.**

```text
V tiene riesgo alto: la política exige aplicar una tasa ajustada de 17 %
a(5; 17%) = 3,19935
VP flujos = 95 000 × 3,19935 = 303 938
VAN ajustado = 53 938 · IR ajustado = 1,216
```

**Paso 4 — evalúa combinaciones factibles con 500 000.**

| Combinación | Inversión | VAN conjunto |
|---|---:|---:|
| V + T | 450 000 | 93 110 |
| V + U | 400 000 | 72 765 |
| T + U + ... | 350 000 | 57 999 |
| V + T + (sobran 50 000) | 450 000 | 93 110 |
| T + U (350 000) + parte de V | — | no divisible |

**La mejor combinación es V + T, con VAN conjunto de 93 110.**

**Paso 5 — verifica el tablero completo de la combinación elegida.**

```text
                          V           T          Conjunto
VAN (ajustado por riesgo) 53 938     39 172      93 110
TIR                       26,25 %    20,89 %     —
IR                        1,216      1,196       1,207
Payback descontado        3,32       3,88        —
umbral payback: < 4,0 años            ✔          ✔
capital no asignado                              50 000
```

**Paso 6 — recomendación y su justificación.**

```text
APROBAR V y T. Rechazar U (por restricción de capital, no por mérito) y W (por VAN negativo).

el capital no asignado de 50 000 se mantiene disponible; su costo de oportunidad
es el WACC, ya considerado en el análisis

nota para el acta:
  · U tiene VAN positivo (18 827) y se rechaza solo por restricción de capital.
    Debe reevaluarse en el siguiente ciclo presupuestario.
  · V se evaluó con tasa ajustada por riesgo de 17 % conforme a la política;
    con el WACC general su VAN sería 84 137.
  · el payback descontado de ambos proyectos cumple el umbral de 4 años.
```

**Interpreta:** el tablero multicriterio no cambió la decisión —el VAN habría bastado— y **sí cambió la
calidad del acta**: documenta por qué se rechaza un proyecto con VAN positivo, qué tasa se aplicó a
cada riesgo, y qué umbral se verificó. Esa documentación es la que permite revisar la decisión más
tarde y aprender de ella.

## 🏦 Del cliente al banco

El cliente muestra un payback corto y el banco calcula el VAN y la duración. La tabla enfrenta las dos lecturas.

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| Payback | Indicador de riesgo del proyecto de un cliente | 13, clase 4 |
| Índice de rentabilidad | Asignación de capital del banco entre negocios | 15, clase 11 |
| Tasa ajustada por riesgo | Pricing y evaluación diferenciada | 15, clase 7 |
| Tablero multicriterio | Formato del acta de comité | 13, clase 13 |
| Umbrales de política | Marco de apetito de riesgo | 11, clase 12 |

## 🧪 Práctica

El laboratorio pide construir el tablero completo de tres proyectos y recomendar uno. La recomendación con su justificación es lo que se evalúa.

En `labs/lab-05.md`, sección de criterios:

1. Calcula payback simple y descontado de cinco proyectos y explica la diferencia.
2. Construye un caso donde el payback rechace un proyecto de alto VAN.
3. Resuelve una asignación de capital con proyectos divisibles e indivisibles.
4. Diseña un tablero multicriterio con umbrales y aplícalo a tres proyectos.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen decisiones basadas en un solo indicador. La causa es haber usado el payback como criterio y no como restricción.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se decide por payback | Criterio de riesgo usado como criterio de decisión | El VAN decide. |
| Se ignoran los flujos posteriores al payback | Defecto estructural del indicador | Complementa con VAN. |
| El IR se usa con proyectos indivisibles | Ordena pero no asigna | Evalúa combinaciones factibles. |
| Se usa rentabilidad contable | No es criterio financiero | Usa flujos de caja descontados. |
| Los umbrales se inventan por proyecto | Falta de política | Define umbrales en la política de inversiones. |
| Se aplica la misma tasa a riesgos distintos | Riesgo no diferenciado | Ajusta la tasa por riesgo del proyecto. |

## ❓ Preguntas de comprobación

1. ¿Por qué el payback descontado siempre supera al simple?
2. Nombra tres defectos del payback y tres razones de su persistencia.
3. ¿Cuándo el índice de rentabilidad entrega la asignación óptima directamente?
4. ¿Por qué la rentabilidad contable no sirve para decidir?
5. ¿Qué reglas debe cumplir un tablero multicriterio para ser defendible?

## 📥 Entregable

Guarda en `portfolio/parte-07/clase-10/`:

- los paybacks simple y descontado de cinco proyectos con su interpretación;
- el caso construido donde el payback rechaza un proyecto de alto VAN;
- la asignación de capital resuelta con proyectos divisibles e indivisibles;
- el tablero multicriterio con umbrales aplicado a tres proyectos y su acta.

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

- Brealey, R., Myers, S. y Allen, F. (2023). *Principios de finanzas corporativas* (14.ª ed.). McGraw-Hill. Capítulo 5: comparación de criterios de inversión.
- Ross, S., Westerfield, R. y Jaffe, J. (2021). *Corporate Finance* (12.ª ed.). McGraw-Hill. Capítulo 6: payback, índice de rentabilidad y racionamiento de capital.
- Graham, J. y Harvey, C. (2001). "The Theory and Practice of Corporate Finance: Evidence from the Field". *Journal of Financial Economics*. Evidencia sobre el uso real de los criterios en las empresas.
- Blank, L. y Tarquin, A. (2018). *Ingeniería económica* (8.ª ed.). McGraw-Hill. Capítulo 5: periodo de recuperación.
- Damodaran, A. (2012). *Investment Valuation* (3.ª ed.). Wiley. Capítulo 5: racionamiento de capital e índice de rentabilidad.
- Verificación local: revisa la política de inversiones de una empresa real de tu mercado, si es pública, y compara sus umbrales con los de esta clase.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 09 · Tasa interna de retorno](09-tasa-interna-de-retorno.md) | [Parte 07](../README.md) · [Programa](../../../SYLLABUS.md) | [11 · Duración y convexidad →](11-duracion-y-convexidad.md) |
<!-- gen:footer:end -->
