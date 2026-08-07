<!-- meta
part: 9
class: 14
title: "Provisiones e incumplimiento"
level: profesional
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 14 · Provisiones e incumplimiento

> [← 13 · Crédito comercial y pyme](13-credito-comercial-y-pyme.md) · [Índice de la parte](../README.md) · [15 · Cobranza y reestructuración →](15-cobranza-y-reestructuracion.md)

**Parte 09 — Análisis y gestión de crédito** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Medir y reconocer la pérdida de una cartera antes de que se materialice. Las provisiones son el
mecanismo por el que un banco reconoce que parte de sus colocaciones no se recuperará, y su
subestimación es la forma más directa de sobrestimar el patrimonio.

Las clases anteriores deciden si se otorga. Esta mide lo que ya se otorgó, y aplica el marco contable que reemplazó al de pérdida incurrida: hoy se provisiona la pérdida esperada, lo que significa reconocer el deterioro antes de que ocurra, en cuanto el riesgo aumenta.

## 📚 Objetivos

Al finalizar podrás:

1. **Definir** el incumplimiento con criterios objetivos.
2. **Calcular** la pérdida esperada con sus tres componentes.
3. **Aplicar** el modelo de tres etapas de la norma contable.
4. **Estimar** PD, LGD y EAD con métodos verificables.
5. **Evaluar** la suficiencia de las provisiones de una cartera.

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

Los dos primeros términos son el evento y la medida; los cinco siguientes, sus componentes y el marco de tres etapas. El **modelo de tres etapas** es la estructura de IFRS 9: la etapa en que está una operación decide si se provisiona la pérdida de doce meses o la de toda la vida, y el salto entre etapas es lo que produce los saltos de provisión.

| Concepto | Comprensión verificable |
|---|---|
| `incumplimiento` | Evento definido: habitualmente mora ≥ 90 días o improbabilidad de pago. |
| `pérdida esperada` | `PD × LGD × EAD`. Costo estadístico previsible del riesgo de crédito. |
| `probabilidad de incumplimiento (PD)` | Probabilidad de que ocurra el evento en un horizonte definido. |
| `severidad (LGD)` | Proporción de la exposición que se pierde si hay incumplimiento. |
| `exposición al incumplimiento (EAD)` | Monto expuesto al momento del evento. |
| `modelo de tres etapas` | Marco de la norma contable: sin deterioro significativo, con deterioro, con incumplimiento. |
| `pérdida esperada de por vida` | Pérdida a lo largo de toda la vida del instrumento. Se aplica en las etapas 2 y 3. |

## 🧠 Modelo mental

Las provisiones responden a una pregunta prospectiva:

```text
de los 100 que presté, ¿cuánto NO voy a recuperar?

no se pregunta cuánto ya se perdió: se estima cuánto se perderá
```

Ese cambio de perspectiva —de pérdida incurrida a pérdida esperada— es el núcleo de la norma contable
vigente y la razón por la que las provisiones se constituyen **antes** del incumplimiento.

## 📖 Desarrollo

### 1. Definir el incumplimiento

El incumplimiento tiene una definición técnica con criterios objetivos y subjetivos. La tabla los recoge.

```text
CRITERIO OBJETIVO
  mora ≥ 90 días en una obligación material

CRITERIO SUBJETIVO (improbabilidad de pago)
  · reestructuración con quita
  · castigo de la operación
  · quiebra o procedimiento concursal del deudor
  · venta de la operación con pérdida significativa
  · deterioro severo de la situación financiera
```

**Ambos criterios operan:** un deudor puede estar al día y ser incumplido si hay evidencia de
improbabilidad de pago.

Principio de **contagio**: si un deudor incumple en una operación, todas sus operaciones se consideran
incumplidas. La razón es que la capacidad de pago es del deudor, no de la operación.

### 2. Los tres componentes

La pérdida esperada es el producto de tres componentes que se estiman por separado. La tabla los recoge con su forma de estimación.

```text
pérdida esperada = PD × LGD × EAD
```

| Componente | Qué mide | Cómo se estima |
|---|---|---|
| PD | Probabilidad del evento | Modelos estadísticos sobre cosechas históricas |
| LGD | Proporción perdida | Recuperaciones históricas descontadas |
| EAD | Exposición al momento | Saldo + uso esperado de líneas |

Con los tres componentes estimados para una cartera concreta, la pérdida
esperada se obtiene multiplicándolos.

```text
ejemplo:
  cartera de consumo de 100 000 millones
  PD anual 4,2 % · LGD 63 % · EAD 100 % del saldo

  pérdida esperada = 100 000 × 0,042 × 0,63 = 2 646 millones
```

### 3. El modelo de tres etapas

Las tres etapas dependen del deterioro del riesgo desde el origen y no del nivel absoluto. La tabla las separa.

```text
ETAPA 1   sin aumento significativo del riesgo desde el origen
          provisión: pérdida esperada a 12 MESES

ETAPA 2   aumento significativo del riesgo, sin incumplimiento
          provisión: pérdida esperada DE POR VIDA

ETAPA 3   con incumplimiento
          provisión: pérdida esperada de por vida
          el interés se reconoce sobre el importe neto
```

**Criterios de traspaso a la etapa 2:**

```text
· mora superior a 30 días (presunción refutable)
· deterioro significativo de la calificación interna
· aparición de indicadores de alerta temprana
· reestructuración sin quita
· deterioro del sector o de la contraparte
```

**Efecto del traspaso:**

```text
operación de 10 millones · PD a 12 meses 3 % · PD de por vida 14 % · LGD 60 %

etapa 1: provisión = 10 × 0,03 × 0,60 = 180 000
etapa 2: provisión = 10 × 0,14 × 0,60 = 840 000

el traspaso multiplica la provisión por 4,7
```

**Esta es la razón por la que el criterio de traspaso importa tanto:** un criterio laxo posterga el
reconocimiento; uno estricto lo adelanta y produce volatilidad en el resultado.

### 4. Estimar cada componente

**PD — a partir de cosechas:**

```text
cosecha originada en el año −3, 12 400 operaciones

  a 12 meses:  incumplieron 312  → PD 12m = 2,52 %
  a 24 meses:  acumulado  684    → PD 24m = 5,52 %
  a 36 meses:  acumulado  891    → PD 36m = 7,19 %
  a 48 meses:  acumulado 1 014   → PD 48m = 8,18 %
  
  PD de por vida (plazo promedio 42 meses) ≈ 7,8 %
```

**LGD — a partir de recuperaciones:**

```text
operaciones incumplidas hace 36 meses: exposición 8 400 millones

  recuperado mes 1–12:     2 180 millones
  recuperado mes 13–24:      940 millones
  recuperado mes 25–36:      310 millones
  costos de recuperación:   −420 millones
  recuperación neta:        3 010 millones

  descontando al 8 % anual: valor presente de la recuperación = 2 720 millones
  LGD = (8 400 − 2 720)/8 400 = 67,6 %
```

**El descuento importa:** una recuperación de 3 010 en tres años vale 2 720 hoy, y la diferencia de
290 millones es pérdida real.

**EAD — con líneas comprometidas:**

```text
línea aprobada 5 000 · saldo utilizado actual 1 800
factor de conversión estimado: 55 % del disponible se usa antes del incumplimiento

EAD = 1 800 + (5 000 − 1 800) × 0,55 = 1 800 + 1 760 = 3 560
```

**El uso de líneas aumenta antes del incumplimiento**, un fenómeno documentado: el deudor en
dificultad utiliza todo el crédito disponible.

### 5. Evaluar la suficiencia de las provisiones

Las provisiones se contrastan con la pérdida observada, y la diferencia sostenida indica un problema de modelo. El procedimiento siguiente lo hace.

```text
INDICADORES
  cobertura de mora = provisiones / cartera en mora ≥ 90 días
  cobertura de cartera = provisiones / cartera total
  provisiones / pérdida esperada calculada
```

Los indicadores cobran sentido al compararlos entre dos entidades del mismo mercado y de tamaño parecido.

```text
                              banco A    banco B
cartera total                 840 000    920 000
cartera en mora ≥ 90 días      21 000     18 400
provisiones                    24 400     14 700
cobertura de mora               116 %       80 %
cobertura de cartera            2,90 %     1,60 %
```

La combinación de menos mora y menos cobertura admite varias lecturas, y distinguirlas es el trabajo del analista.

```text
banco B tiene MENOS mora y MENOS cobertura
posibles explicaciones:
  · su cartera es efectivamente mejor
  · sus criterios de traspaso a etapa 2 son más laxos
  · refinancia operaciones antes de que lleguen a 90 días
  · sus modelos subestiman la PD o la LGD
```

**Prueba de suficiencia:**

```text
1. calcular la pérdida esperada con parámetros propios verificados
2. comparar con la provisión constituida
3. analizar la diferencia por segmento y por etapa
4. verificar la migración entre etapas en los últimos periodos
5. contrastar la LGD estimada con las recuperaciones efectivas
```

## 🧮 Ejemplo guiado

El ejemplo calcula la provisión de una cartera por etapas. Conviene mirar el efecto del salto de etapa uno a dos: multiplica la provisión sin que haya habido ningún impago.

**Situación.** Evalúa la suficiencia de las provisiones de una cartera de consumo.

```text
CARTERA
  saldo total                      620 000 millones
  operaciones                      412 000
  plazo promedio remanente         28 meses

DISTRIBUCIÓN POR ETAPA
  etapa 1                          548 000 (88,4 %)
  etapa 2                           54 000 (8,7 %)
  etapa 3                           18 000 (2,9 %)

PROVISIONES CONSTITUIDAS
  etapa 1                            3 840
  etapa 2                            6 210
  etapa 3                           11 340
  TOTAL                             21 390 (3,45 % de la cartera)
```

**Paso 1 — verifica los parámetros de la etapa 1.**

```text
provisión etapa 1 = 3 840 sobre 548 000 = 0,70 %

implícito: PD 12m × LGD = 0,70 %
si LGD = 62 % → PD 12m implícita = 1,13 %

contraste con las cosechas observadas:
  cosecha año −1: PD 12m observada = 2,84 %
  cosecha año −2: PD 12m observada = 2,61 %
  cosecha año −3: PD 12m observada = 2,38 %
  
  PD 12m promedio observada: 2,61 %
```

**La PD implícita en la provisión (1,13 %) es menos de la mitad de la observada (2,61 %).**

```text
provisión etapa 1 recalculada = 548 000 × 0,0261 × 0,62 = 8 868
déficit etapa 1 = 8 868 − 3 840 = 5 028
```

**Paso 2 — verifica los parámetros de la etapa 2.**

```text
provisión etapa 2 = 6 210 sobre 54 000 = 11,50 %

implícito: PD de por vida × LGD = 11,50 %
si LGD = 62 % → PD de por vida implícita = 18,5 %

contraste: operaciones en etapa 2 hace 24 meses
  cuántas llegaron a incumplimiento: 31,4 %

provisión etapa 2 recalculada = 54 000 × 0,314 × 0,62 = 10 513
déficit etapa 2 = 10 513 − 6 210 = 4 303
```

**Paso 3 — verifica la LGD con recuperaciones efectivas.**

```text
operaciones incumplidas hace 36 meses: exposición 22 400
recuperación nominal acumulada: 8 950
costos de recuperación: −1 340
recuperación neta: 7 610
valor presente al 9 %: 6 820

LGD observada = (22 400 − 6 820)/22 400 = 69,6 %
LGD usada en los modelos: 62,0 %
```

**La LGD está subestimada en 7,6 puntos.**

```text
recalculando todo con LGD 69,6 %:
  etapa 1: 548 000 × 0,0261 × 0,696 = 9 955
  etapa 2:  54 000 × 0,314 × 0,696 = 11 802
  etapa 3:  18 000 × 1,000 × 0,696 = 12 528
  TOTAL REQUERIDO                    34 285
  
  provisión constituida               21 390
  DÉFICIT                             12 895 (60,3 % de lo constituido)
```

**Paso 4 — verifica los criterios de traspaso entre etapas.**

```text
distribución observada:
  etapa 2: 8,7 % de la cartera
  
comparación con la migración esperada:
  operaciones con mora 31–89 días: 4,2 % de la cartera
  operaciones con deterioro de calificación interna: 6,8 %
  operaciones reestructuradas sin quita: 2,1 %
  
  unión de los tres criterios (sin doble conteo): 11,4 %
  
  clasificadas en etapa 2: 8,7 %
  DIFERENCIA: 2,7 puntos = 16 740 millones que deberían estar en etapa 2
```

```text
efecto del traspaso correcto:
  16 740 pasan de etapa 1 a etapa 2
  provisión adicional = 16 740 × (0,314 − 0,0261) × 0,696 = 3 354
```

**Paso 5 — déficit total.**

```text
déficit por parámetros (PD y LGD):        12 895
déficit por clasificación de etapas:       3 354
DÉFICIT TOTAL                             16 249

provisión requerida: 37 639 (6,07 % de la cartera)
provisión constituida: 21 390 (3,45 %)
```

**Paso 6 — efecto sobre el patrimonio y el capital.**

```text
patrimonio del banco: 78 000
déficit de provisiones: 16 249
patrimonio ajustado: 61 751 (−20,8 %)

razón de capital antes: 12,4 %
razón de capital ajustada: 9,8 %
mínimo regulatorio: 10,5 %  → INCUMPLIRÍA
```

**Paso 7 — conclusiones y acciones.**

```text
HALLAZGOS
  H1  la PD usada en etapa 1 es 43 % de la observada en las cosechas
  H2  la LGD está subestimada en 7,6 puntos frente a las recuperaciones efectivas
  H3  16 740 millones no fueron traspasados a etapa 2 pese a cumplir criterios
  H4  el déficit total de 16 249 millones equivale al 20,8 % del patrimonio
  H5  con el ajuste, la razón de capital caería bajo el mínimo regulatorio

ACCIONES
  1. recalibrar la PD con las cosechas observadas de los últimos 3 años
  2. recalibrar la LGD con las recuperaciones efectivas descontadas
  3. revisar y automatizar los criterios de traspaso a etapa 2
  4. constituir el déficit de provisiones de forma gradual, con plan aprobado
  5. plan de fortalecimiento de capital antes de reconocer el déficit completo
  6. informar al supervisor conforme a la normativa

OBSERVACIÓN DE GOBIERNO
  la subestimación no es aleatoria: los tres hallazgos apuntan en la misma
  dirección (menor provisión). Eso exige revisar el proceso de validación
  independiente de los modelos y los incentivos asociados al resultado.
```

**Interpreta:** las provisiones estaban subestimadas en un **60 %**, y las tres causas —PD, LGD y
clasificación de etapas— **apuntaban en la misma dirección**. Esa coincidencia es en sí misma un
hallazgo: sugiere un sesgo sistemático, no errores independientes.

## 🏦 Del cliente al banco

El cliente se atrasa y el banco reconoce una pérdida esperada en su resultado. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| Mora de 35 días | Traspaso a etapa 2: la provisión se multiplica | 9, clase 15 |
| Reestructuración | Puede implicar traspaso de etapa | 9, clase 15 |
| Contagio entre operaciones | Un incumplimiento afecta todas sus operaciones | 9, clase 1 |
| Uso de línea antes de incumplir | Aumenta la exposición al incumplimiento | 9, clase 6 |
| Castigo de la deuda | Baja contable; la deuda sigue siendo exigible | 9, clase 15 |

## 🧪 Práctica

El laboratorio pide clasificar una cartera por etapas y calcular la provisión. El caso incluye operaciones al día con deterioro significativo, que es donde el criterio importa.

En `labs/lab-06.md`, sección de provisiones:

1. Estima PD a partir de cosechas históricas con datos sintéticos.
2. Calcula la LGD con recuperaciones descontadas y compárala con la nominal.
3. Clasifica una cartera en tres etapas aplicando los criterios de traspaso.
4. Evalúa la suficiencia de las provisiones y cuantifica el déficit o exceso.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen provisiones insuficientes o volátiles. Las causas son etapas mal asignadas y componentes estimados con datos de un solo ciclo.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| La LGD no descuenta las recuperaciones | Valor del tiempo ignorado | Descuenta al costo de fondos o a la tasa efectiva. |
| Se usa una PD desactualizada | Sin recalibración | Contrasta con cosechas recientes. |
| Pocas operaciones en etapa 2 | Criterios de traspaso laxos | Aplica todos los criterios, no solo la mora. |
| No se considera el uso de líneas | EAD subestimada | Aplica factores de conversión. |
| Se provisiona solo lo vencido | Modelo de pérdida incurrida | La norma exige pérdida esperada. |
| Los sesgos apuntan todos en la misma dirección | Posible sesgo sistemático | Revisa la validación independiente. |

## ❓ Preguntas de comprobación

1. ¿Qué dos criterios definen el incumplimiento?
2. ¿Por qué el traspaso a etapa 2 multiplica la provisión?
3. ¿Por qué la LGD debe calcularse con recuperaciones descontadas?
4. ¿Por qué la exposición al incumplimiento supera el saldo actual en líneas comprometidas?
5. ¿Qué sugiere que tres subestimaciones apunten en la misma dirección?

## 📥 Entregable

Guarda en `portfolio/parte-09/clase-14/`:

- la PD estimada a partir de cosechas con su metodología;
- la LGD calculada con recuperaciones descontadas y su comparación con la nominal;
- la clasificación de una cartera en tres etapas con los criterios aplicados;
- la evaluación de suficiencia con el déficit o exceso cuantificado y su efecto en el capital.

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

- IFRS Foundation (2014). *NIIF 9 Instrumentos Financieros*, sección 5.5: modelo de pérdida crediticia esperada y las tres etapas. <https://www.ifrs.org/>
- Basel Committee on Banking Supervision (2015). *Guidance on credit risk and accounting for expected credit losses*. BIS. <https://www.bis.org/bcbs/publ/d350.htm>
- Basel Committee on Banking Supervision (2017). *Prudential treatment of problem assets — definitions of non-performing exposures and forbearance*. BIS.
- Schuermann, T. (2004). "What Do We Know About Loss Given Default?". Wharton Financial Institutions Center. Estimación empírica de la severidad.
- European Banking Authority (2017). *Guidelines on PD estimation, LGD estimation and treatment of defaulted exposures*. EBA. <https://www.eba.europa.eu/>
- Verificación local: revisa la normativa de provisiones de tu supervisor, sus modelos estándar y los requisitos de validación de modelos internos.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 13 · Crédito comercial y pyme](13-credito-comercial-y-pyme.md) | [Parte 09](../README.md) · [Programa](../../../SYLLABUS.md) | [15 · Cobranza y reestructuración →](15-cobranza-y-reestructuracion.md) |
<!-- gen:footer:end -->
