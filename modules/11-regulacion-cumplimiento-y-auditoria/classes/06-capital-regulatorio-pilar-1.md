---
part: 12
class: 6
title: "Capital regulatorio: Pilar 1"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 06 · Capital regulatorio: Pilar 1

> [← 05 · Sanciones internacionales](05-sanciones-internacionales.md) · [Índice de la parte](../README.md) · [07 · Proceso supervisor: Pilar 2 →](07-proceso-supervisor-pilar-2.md)

**Parte 12 — Regulación, cumplimiento y auditoría** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Calcular el capital que la norma exige. La Parte 11 estudió el capital que el riesgo real requiere; esta
clase estudia el que el supervisor obliga a mantener, cómo se compone, cómo se calculan sus
denominadores y qué ocurre cuando los colchones se consumen.

La Parte 11 calculó el capital que un banco necesita según sus propios modelos. Esta calcula el que la norma le exige, que es otra cifra y con otra lógica. Las dos coexisten y la que obliga es la mayor, y entender por qué difieren es lo que permite gestionar ambas.

## 📚 Objetivos

Al finalizar podrás:

1. **Componer** el capital regulatorio por sus niveles y deducciones.
2. **Calcular** activos ponderados por riesgo de crédito, mercado y operacional.
3. **Aplicar** los colchones y sus consecuencias automáticas.
4. **Calcular** el ratio de apalancamiento y explicar su función.
5. **Interpretar** un estado de solvencia completo.

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

Los cuatro primeros términos son la composición del numerador; los cuatro siguientes, el denominador y las exigencias adicionales. Los **colchones** son la parte con más consecuencias prácticas: incumplirlos no cierra el banco, pero restringe el reparto de dividendos y de bonos, que es una sanción muy eficaz.

| Concepto | Comprensión verificable |
|---|---|
| `capital nivel 1 ordinario` | Capital de máxima calidad: acciones y utilidades retenidas. |
| `capital nivel 1 adicional` | Instrumentos perpetuos con absorción de pérdidas en marcha. |
| `capital nivel 2` | Instrumentos subordinados con absorción en liquidación. |
| `deducción` | Partida que se resta del capital por no ser realizable en estrés. |
| `activos ponderados por riesgo` | Denominador del ratio: exposición ajustada por su riesgo. |
| `colchón de conservación` | Capital adicional cuyo consumo restringe distribuciones. |
| `colchón contracíclico` | Capital adicional activado por el supervisor en expansiones. |
| `ratio de apalancamiento` | Capital sobre exposición total, sin ponderar por riesgo. |

## 🧠 Modelo mental

El modelo mental es una fracción con dos partes que se pueden mover: arriba el capital que califica como tal según reglas estrictas, y abajo los activos ponderados por su riesgo. Mejorar el ratio se puede hacer subiendo el numerador o bajando el denominador, y la segunda vía es la que más gestión admite.

```text
DOS RESTRICCIONES QUE OPERAN EN PARALELO

RATIO DE CAPITAL          capital / activos PONDERADOS por riesgo
  sensible al riesgo
  vulnerable a la manipulación del denominador

RATIO DE APALANCAMIENTO   capital / exposición TOTAL, sin ponderar
  insensible al riesgo
  inmune a la manipulación del denominador

el segundo existe porque el primero falló:
bancos con ratios de capital altos
y apalancamiento extremo quebraron
```

**El ratio de apalancamiento es una red de seguridad, no una medida de riesgo.** Su función es acotar el
tamaño del balance con independencia de cuán poco riesgoso lo declaren los modelos.

## 📖 Desarrollo

### 1. Composición del capital

El capital regulatorio tiene niveles con capacidad de absorción decreciente. La tabla los recoge con sus requisitos.

```text
CAPITAL NIVEL 1 ORDINARIO (CET1) — el que absorbe primero
  + acciones ordinarias
  + prima de emisión
  + utilidades retenidas
  + otro resultado integral acumulado
  − plusvalía y otros intangibles
  − activos por impuestos diferidos que dependen de rentabilidad futura
  − participaciones significativas en entidades financieras
  − déficit de provisiones respecto de la pérdida esperada
  − activos de fondos de pensiones de beneficio definido

CAPITAL NIVEL 1 ADICIONAL (AT1)
  instrumentos perpetuos, sin incentivo de rescate,
  con mecanismo de absorción de pérdidas en marcha
  (conversión en acciones o reducción del principal)

CAPITAL NIVEL 2 (T2)
  instrumentos subordinados con plazo mínimo,
  provisiones genéricas hasta un límite
```

| Requerimiento mínimo | Nivel |
|---|---:|
| Capital nivel 1 ordinario | 4,5 % |
| Capital nivel 1 total | 6,0 % |
| Capital total | 8,0 % |
| + colchón de conservación | 2,5 % |
| + colchón contracíclico | 0 – 2,5 % |
| + recargo por importancia sistémica | 1,0 – 3,5 % |

**Las deducciones son el elemento más subestimado.** Un banco puede tener un patrimonio contable
holgado y un capital regulatorio ajustado porque una parte relevante de ese patrimonio son intangibles
y activos por impuestos diferidos que no absorberían pérdidas en un escenario de estrés.

### 2. Activos ponderados: riesgo de crédito

La ponderación de riesgo de crédito se calcula por método estándar o interno, con resultados muy distintos. La tabla los compara.

```text
ENFOQUE ESTANDARIZADO — ponderaciones por tipo de exposición
  soberanos                según calificación o método propio
  bancos                   según grado de la contraparte (Parte 12, clase 2)
  empresas                 según calificación o tamaño y riesgo
  minorista regulatorio    75 %
  hipotecario residencial  según relación préstamo/garantía: 20 % a 70 %
  hipotecario comercial    según criterios específicos
  en incumplimiento        100 % a 150 % según provisiones
  otros activos            100 %

ENFOQUE BASADO EN CALIFICACIONES INTERNAS (IRB)
  el banco estima PD (y en el avanzado, LGD y EAD)
  la fórmula supervisora los convierte en requerimiento
  sujeto a un piso: el resultado no puede ser inferior
  al 72,5 % del que daría el enfoque estandarizado
```

```text
POR QUÉ EXISTE EL PISO
  la variabilidad observada entre bancos en el cálculo IRB
  para carteras equivalentes era demasiado grande
  para atribuirse solo a diferencias de riesgo real
```

### 3. Mercado y operacional

Los otros dos riesgos del pilar tienen sus propias metodologías. La tabla las recoge.

| Riesgo | Enfoques | Base |
|---|---|---|
| Mercado | Estandarizado (sensibilidades) o modelos internos | Libro de negociación, déficit esperado |
| Operacional | Estandarizado único | Indicador de negocio × multiplicador de pérdidas |
| Ajuste de valoración por crédito | Estandarizado o básico | Exposición de derivados |

```text
CONVERSIÓN A ACTIVOS PONDERADOS
  para mercado y operacional se calcula un REQUERIMIENTO de capital
  y se convierte a activos ponderados equivalentes:

  activos ponderados = requerimiento / 8 %  = requerimiento × 12,5
```

### 4. Colchones y sus consecuencias

Los colchones se acumulan sobre el mínimo y su incumplimiento restringe distribuciones. La tabla recoge la gradación.

```text
LOS COLCHONES NO SON MÍNIMOS: SON UMBRALES DE RESTRICCIÓN

  al consumirlos, el banco no infringe la norma
  pero pierde libertad para distribuir resultados

RESTRICCIÓN AUTOMÁTICA DE DISTRIBUCIONES
  cuartil del colchón consumido   % máximo de distribución
  primer cuartil (más consumido)         0 %
  segundo cuartil                       20 %
  tercer cuartil                        40 %
  cuarto cuartil                        60 %
  colchón completo                     100 %

  "distribución" incluye dividendos, recompras,
  pagos discrecionales de instrumentos AT1 y bonos del personal
```

**Esta es la consecuencia más concreta de toda la clase:** el consumo del colchón toca la remuneración
variable y el dividendo antes que ninguna otra cosa, y por diseño. Alinea el incentivo de quienes
deciden con la conservación del capital.

### 5. Ratio de apalancamiento

El ratio de apalancamiento no pondera por riesgo, y por eso actúa como red frente a los modelos internos. El procedimiento lo calcula.

```text
                       capital nivel 1
APALANCAMIENTO = ───────────────────────────────  ≥ 3 %
                 medida de exposición total

  medida de exposición =
    + activos del balance (sin ponderar)
    + exposición de derivados (método estandarizado)
    + operaciones de financiación de valores
    + partidas fuera de balance con factores de conversión
    − deducciones aplicadas al capital
```

```text
CUÁL RESTRINGE
  banco con activos de bajo riesgo (hipotecario, soberanos)
  → ratio de capital cómodo, apalancamiento ajustado
  → LA RESTRICCIÓN ES EL APALANCAMIENTO

  banco con activos de alto riesgo (consumo, empresas)
  → apalancamiento cómodo, ratio de capital ajustado
  → LA RESTRICCIÓN ES EL RATIO DE CAPITAL

saber cuál restringe determina qué crecimiento es posible
```

## 🧮 Ejemplo guiado

El ejemplo calcula el capital regulatorio de un banco con todos sus colchones. Conviene comparar con el capital económico de la Parte 11: las dos cifras difieren y la mayor manda.

**Situación.** Un banco calcula su estado de solvencia completo.

```text
PATRIMONIO CONTABLE                          412 000
  acciones ordinarias y prima                240 000
  utilidades retenidas                       148 000
  otro resultado integral acumulado           24 000

PARTIDAS A DEDUCIR
  plusvalía                                   38 000
  software y otros intangibles                18 400
  activos por impuestos diferidos
    dependientes de rentabilidad futura       26 200
  participación en aseguradora (18 %)         14 800

OTROS INSTRUMENTOS
  instrumentos AT1                            42 000
  bonos subordinados computables T2           58 000

EXPOSICIONES
  cartera minorista regulatoria              680 000
  hipotecario residencial (LTV medio 62 %)   890 000
  empresas sin calificación externa          960 000
  bancos, grado A                            186 000
  soberanos locales                          320 000
  otros activos                              164 000
  requerimiento de riesgo de mercado           9 600
  requerimiento de riesgo operacional          34 200
  partidas fuera de balance (nominal)         240 000
```

**Paso 1 — calcula el capital nivel 1 ordinario.**

```text
patrimonio contable                          412 000
− plusvalía                                  −38 000
− intangibles                                −18 400
− impuestos diferidos dependientes           −26 200
− participación significativa*                     0
CAPITAL NIVEL 1 ORDINARIO                    329 400

* la participación del 18 % no supera el umbral de significatividad
  (10 % del capital de la participada con criterios adicionales);
  se verifica y, en este caso, no se deduce
```

**Paso 2 — calcula los demás niveles.**

```text
CAPITAL NIVEL 1 TOTAL = 329 400 + 42 000 = 371 400
CAPITAL TOTAL         = 371 400 + 58 000 = 429 400
```

**Paso 3 — calcula los activos ponderados por riesgo de crédito.**

```text
minorista regulatoria     680 000 × 75 %  = 510 000
hipotecario (LTV 62 %)    890 000 × 30 %  = 267 000
empresas sin calificación 960 000 × 100 % = 960 000
bancos grado A            186 000 × 40 %  =  74 400
soberanos locales         320 000 ×  0 %  =       0
otros activos             164 000 × 100 % = 164 000
fuera de balance          240 000 × 50 %* × 100 % = 120 000
                                             ─────────
CRÉDITO                                    2 095 400

* factor de conversión de crédito medio supuesto
```

**Paso 4 — añade mercado y operacional.**

```text
mercado:      9 600 × 12,5 =   120 000
operacional: 34 200 × 12,5 =   427 500

ACTIVOS PONDERADOS TOTALES = 2 095 400 + 120 000 + 427 500 = 2 642 900
```

**Paso 5 — calcula los ratios.**

```text
capital nivel 1 ordinario: 329 400 / 2 642 900 = 12,46 %
capital nivel 1 total:     371 400 / 2 642 900 = 14,05 %
capital total:             429 400 / 2 642 900 = 16,25 %
```

**Paso 6 — compara con los requerimientos.**

```text
REQUERIMIENTO APLICABLE
  mínimo CET1                          4,50 %
  colchón de conservación              2,50 %
  colchón contracíclico (activado)     1,00 %
  recargo sistémico local              1,00 %
  REQUERIMIENTO CET1 TOTAL             9,00 %

  actual 12,46 % → holgura de 3,46 puntos
  en unidades: 3,46 % × 2 642 900 = 91 444
```

**Paso 7 — calcula el ratio de apalancamiento.**

```text
medida de exposición
  activos del balance (suma sin ponderar):
    680 000+890 000+960 000+186 000+320 000+164 000 = 3 200 000
  fuera de balance con factores del apalancamiento (10 % a 100 %):
    240 000 × 40 % = 96 000
  exposición de derivados (dato): 78 000
  − deducciones aplicadas al capital: −82 600
  MEDIDA DE EXPOSICIÓN                3 291 400

APALANCAMIENTO = 371 400 / 3 291 400 = 11,28 %
mínimo 3,00 %  → holgura muy amplia
```

**Paso 8 — determina cuál restringe y qué crecimiento permite.**

```text
CRECIMIENTO POSIBLE HASTA TOCAR EL REQUERIMIENTO CET1
  activos ponderados máximos: 329 400 / 0,09 = 3 660 000
  espacio: 3 660 000 − 2 642 900 = 1 017 100 de activos ponderados

CRECIMIENTO POSIBLE HASTA TOCAR EL APALANCAMIENTO
  exposición máxima: 371 400 / 0,03 = 12 380 000
  espacio: 9 088 600 de exposición

LA RESTRICCIÓN ES EL RATIO DE CAPITAL, con amplio margen

pero el crecimiento posible depende de DÓNDE se crece:
  1 017 100 de activos ponderados equivalen a
    · 1 356 133 de cartera minorista (75 %)
    · 3 390 333 de hipotecario a LTV 62 % (30 %)
    · 1 017 100 de empresas sin calificación (100 %)

el mismo capital financia 2,5 veces más hipotecario que empresas
```

**Interpreta:** el banco tiene un patrimonio contable de 412 000 y un capital regulatorio de 329 400:
**las deducciones consumen el 20 % del patrimonio**. Ese es el número que más sorprende al leer un
estado de solvencia por primera vez, y explica por qué una fusión que genera plusvalía puede deteriorar
la solvencia regulatoria aunque aumente el patrimonio contable.

## 🏦 Del cliente al banco

El cliente no ve nada de esto y el banco decide cuánto puede prestar según su capital. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Mi banco tiene mucho patrimonio» | Deducciones reducen el capital regulatorio | 12, clase 6 |
| «Suspendieron el dividendo» | Colchón consumido, restricción automática | 12, clase 6 |
| «El hipotecario es más barato» | Menor ponderación de riesgo | 3, clase 9 |
| «Mi empresa sin calificación paga más» | Ponderación del 100 % | 13, clase 5 |
| «El banco creció mucho y ahora frena» | Restricción de capital alcanzada | 15, clase 5 |

## 🧪 Práctica

El laboratorio pide calcular el ratio de un banco y determinar sus restricciones de distribución. El banco cumple el mínimo y no los colchones, que es el caso interesante.

En `labs/lab-03.md`, sección de capital:

1. Compón el capital regulatorio de un banco con todas sus deducciones.
2. Calcula los activos ponderados por los tres riesgos.
3. Determina los ratios y su holgura contra el requerimiento aplicable.
4. Determina cuál restricción es activa y cuánto crecimiento permite por segmento.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen bancos que descubren tarde una restricción de capital. Las causas son colchones no proyectados y deducciones no consideradas.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se usa el patrimonio contable como capital | Deducciones omitidas | Aplica todas las deducciones. |
| Se compara el ratio con el mínimo sin colchones | Requerimiento incompleto | Suma conservación, contracíclico y recargo. |
| Se ignora el ratio de apalancamiento | Solo se mira el ponderado | Verifica cuál restringe. |
| Se convierten mal mercado y operacional | Falta el factor 12,5 | Requerimiento ÷ 8 %. |
| Se cree que consumir el colchón es infracción | Concepto | Es restricción de distribuciones. |
| Se planifica crecimiento sin segmentar | Ponderaciones distintas | Calcula por segmento. |

## ❓ Preguntas de comprobación

1. ¿Por qué existe el ratio de apalancamiento si ya existe el ratio de capital?
2. ¿Qué efecto tienen las deducciones sobre la relación entre patrimonio contable y capital regulatorio?
3. ¿Qué ocurre exactamente cuando un banco consume su colchón de conservación?
4. ¿Por qué el enfoque IRB tiene un piso respecto del estandarizado?
5. ¿Cómo determina un banco cuál de las dos restricciones es la activa?

## 📥 Entregable

Guarda en `portfolio/parte-12/clase-06/`:

- la composición del capital con todas las deducciones aplicadas;
- el cálculo de activos ponderados por los tres riesgos;
- los ratios con su holgura frente al requerimiento completo;
- el análisis de restricción activa y crecimiento posible por segmento.

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
- Basel Committee on Banking Supervision (2011). *Basel III: A global regulatory framework for more resilient banks and banking systems*. BIS. <https://www.bis.org/publ/bcbs189.htm>
- Basel Committee on Banking Supervision (2014). *Basel III leverage ratio framework and disclosure requirements*. BIS.
- Basel Committee on Banking Supervision. *The Basel Framework* (compilación consolidada vigente). BIS. <https://www.bis.org/basel_framework/>
- Saunders, A. y Cornett, M. (2021). *Financial Institutions Management* (10.ª ed.). McGraw-Hill. Capítulo 20.
- Verificación local: revisa los porcentajes de colchones activados, el recargo sistémico local y las deducciones específicas que aplica tu supervisor.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 05 · Sanciones internacionales](05-sanciones-internacionales.md) | [Parte 12](../README.md) · [Programa](../../../SYLLABUS.md) | [07 · Proceso supervisor: Pilar 2 →](07-proceso-supervisor-pilar-2.md) |
<!-- gen:footer:end -->
