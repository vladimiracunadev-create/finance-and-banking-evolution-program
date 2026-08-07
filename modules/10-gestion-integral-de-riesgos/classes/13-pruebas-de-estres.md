---
part: 11
class: 13
title: "Pruebas de estrés"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 13 · Pruebas de estrés

> [← 12 · Riesgo de modelo](12-riesgo-de-modelo.md) · [Índice de la parte](../README.md) · [14 · Capital económico y asignación →](14-capital-economico-y-asignacion.md)

**Parte 11 — Gestión integral de riesgos** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Responder la pregunta que ninguna medición estadística responde: **¿qué le pasa a este banco si el
escenario adverso ocurre?** La prueba de estrés no estima probabilidades: construye un mundo coherente,
lo aplica al balance completo y muestra si el banco sobrevive.

Todas las medidas anteriores se calculan en condiciones normales. Esta clase las lleva a condiciones que no lo son, y añade la exigencia que separa un ejercicio útil de uno decorativo: el escenario tiene que ser coherente y suficientemente severo como para que el banco no lo apruebe con holgura.

## 📚 Objetivos

Al finalizar podrás:

1. **Diseñar** un escenario macroeconómico adverso internamente coherente.
2. **Traducir** variables macro a parámetros de riesgo por cartera.
3. **Proyectar** resultado, capital y liquidez bajo el escenario.
4. **Ejecutar** una prueba inversa y encontrar el punto de quiebre.
5. **Vincular** el resultado con decisiones concretas de capital y negocio.

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

Los tres primeros términos son los escenarios y su exigencia; los cinco siguientes, la mecánica de la proyección y sus variantes. La **prueba inversa** es la más informativa y la menos usada: en vez de preguntar qué pasa en este escenario, pregunta qué escenario haría inviable al banco.

| Concepto | Comprensión verificable |
|---|---|
| `escenario base` | Proyección más probable. Sirve de referencia. |
| `escenario adverso` | Deterioro severo pero plausible del entorno. |
| `escenario severo` | Deterioro extremo, en el límite de lo concebible. |
| `coherencia interna` | Las variables del escenario se mueven de forma compatible entre sí. |
| `función de traducción` | Relación estimada entre variables macro y parámetros de riesgo. |
| `balance estático` | Supuesto de que el balance no cambia durante el horizonte. |
| `acción de gestión` | Respuesta del banco durante el escenario. Debe ser creíble. |
| `prueba inversa` | Se parte del resultado intolerable y se busca qué lo produce. |

## 🧠 Modelo mental

El modelo mental es una cadena de traducción: un escenario macroeconómico se convierte en parámetros de riesgo, esos parámetros en pérdidas, y esas pérdidas en capital. Cada eslabón puede romperse, y el más frágil suele ser la traducción del escenario a los parámetros.

```text
UNA PRUEBA DE ESTRÉS NO PREGUNTA "¿QUÉ TAN PROBABLE ES?"
PREGUNTA "¿QUÉ PASA SI OCURRE?"

  el valor en riesgo dice: en 99 de 100 días pierdo menos de X
  la prueba de estrés dice: si ocurre este escenario, pierdo Y
                            y me queda Z de capital

  la primera es una distribución
  la segunda es una historia con números
```

**La utilidad de la prueba está en su coherencia narrativa, no en su precisión.** Un escenario donde el
desempleo sube 6 puntos y los precios de la vivienda no caen no es conservador: es incoherente, y sus
resultados no significan nada.

## 📖 Desarrollo

### 1. Tipos de prueba

Hay varios tipos de prueba de estrés con propósitos distintos. La tabla los recoge.

| Tipo | Qué varía | Uso |
|---|---|---|
| Sensibilidad | Una variable a la vez | Entender la mecánica |
| Escenario | Un conjunto coherente de variables | Evaluar resistencia |
| Inversa | Se busca el escenario dado el resultado | Encontrar vulnerabilidades |
| Supervisora | Escenario común a todo el sistema | Comparabilidad y política |
| Interna | Escenario propio del banco | Gestión y planificación de capital |

### 2. Diseño del escenario

Un escenario se diseña desde una narrativa coherente y no desde una lista de variables movidas. El procedimiento siguiente lo estructura.

```text
VARIABLES MACRO TÍPICAS
  producto interno bruto        caída acumulada
  desempleo                     alza en puntos
  inflación                     desviación
  tasa de política monetaria    trayectoria
  tipo de cambio                depreciación
  precios de vivienda           caída
  precios de acciones           caída
  diferencial soberano          ampliación
```

```text
COHERENCIA INTERNA — relaciones que deben respetarse
  caída del producto  →  alza del desempleo (con rezago)
  alza del desempleo  →  caída del ingreso disponible
  depreciación fuerte →  inflación al alza
  inflación al alza   →  política monetaria restrictiva
  política restrictiva→  caída de precios de activos
  caída de precios    →  menor valor de garantías
```

| Severidad de referencia | Criterio |
|---|---|
| Adverso | Comparable a una recesión histórica del país |
| Severo | Peor que cualquier episodio del registro histórico |

### 3. Traducción a parámetros de riesgo

La traducción del escenario a probabilidad de incumplimiento y severidad es el eslabón más frágil. La tabla recoge los métodos.

```text
FUNCIÓN DE TRADUCCIÓN — ejemplo para cartera de consumo

  PD_t = f(desempleo_t, ingreso_real_t, tasa_t)

  estimada sobre historia propia, con validación fuera de muestra
  y con criterio experto cuando la historia no cubre el rango
```

```text
EJEMPLO DE ELASTICIDADES ESTIMADAS
  consumo:      +1 punto de desempleo → PD × 1,42
  hipotecario:  +1 punto de desempleo → PD × 1,18
                −10 % precios vivienda → LGD +6 puntos
  comercial:    −1 % del producto      → PD × 1,25
  moneda extranjera a no generadores:
                −10 % tipo de cambio   → PD × 1,30
```

**Advertencia sobre no linealidad.** Las elasticidades estimadas en el rango histórico se aplican a un
escenario fuera de ese rango. La relación real suele ser convexa: el deterioro se acelera. Extrapolar
linealmente **subestima sistemáticamente** la pérdida en la parte severa del escenario.

### 4. Proyección integral

La proyección integra resultado, balance y capital bajo el escenario. El procedimiento la recorre.

```text
LO QUE DEBE PROYECTARSE (no solo pérdidas de crédito)

RESULTADO
  margen financiero      (volumen menor, tasas distintas, mora que no devenga)
  comisiones             (menor actividad)
  costo de riesgo        (provisiones por deterioro)
  resultado de mercado   (valoración de carteras)
  gastos                 (rígidos en el corto plazo)

BALANCE
  crecimiento de activos ponderados (migración de calificación)
  activos improductivos
  liquidez y financiamiento

CAPITAL
  resultado acumulado → capital
  activos ponderados → denominador
  dividendos → restricción automática al cruzar colchones
```

```text
ERROR FRECUENTE: proyectar solo las provisiones
  el margen cae, las comisiones caen, los activos ponderados suben
  y los gastos no bajan al mismo ritmo
  la caída de capital viene de los cuatro efectos, no de uno
```

### 5. Acciones de gestión y credibilidad

Las acciones de gestión que el banco supone que tomará tienen que ser creíbles y ejecutables en el escenario. La tabla recoge los criterios.

```text
ACCIONES CREÍBLES              ACCIONES NO CREÍBLES
  suspender dividendos           vender cartera a valor libro en plena crisis
  reducir originación            emitir capital cuando nadie compra
  recortar gasto discrecional    reducir gastos de personal 30 % en un trimestre
  no renovar líneas              subir comisiones sin perder clientes

REGLA: si la acción depende de que otros actúen de forma normal
       mientras el escenario adverso ocurre, no es creíble
```

### 6. Prueba inversa

La prueba inversa busca el escenario que rompe al banco en vez de comprobar que sobrevive a uno dado. El procedimiento la plantea.

```text
PROCEDIMIENTO
  1. define el resultado intolerable
     (capital bajo el mínimo, pérdida de la licencia, iliquidez)
  2. trabaja hacia atrás: ¿qué combinación lo produce?
  3. evalúa qué tan lejano es ese escenario
  4. si está cerca, esa es la vulnerabilidad principal

VALOR: no requiere estimar probabilidades
       y encuentra vulnerabilidades que los escenarios estándar no tocan
```

## 🧮 Ejemplo guiado

El ejemplo proyecta el capital de un banco bajo un escenario adverso. Conviene mirar las acciones de gestión supuestas: son las que más suelen inflar el resultado.

**Situación.** Un banco ejecuta su prueba de estrés interna a tres años.

```text
POSICIÓN INICIAL
  activos totales                    3 800 000
  cartera total                      2 940 000
    consumo                            520 000
    hipotecario                        890 000
    comercial                        1 530 000
  activos ponderados por riesgo      2 280 000
  capital nivel 1 ordinario            296 400   → 13,0 %
  mínimo + colchones                                10,5 %
  margen financiero anual              218 000
  comisiones netas                      64 000
  gastos operativos                    162 000
  costo de riesgo base                  38 000

ESCENARIO ADVERSO (3 años)
  año 1: producto −3,4 %, desempleo +2,8 pp, vivienda −12 %, tasa +250 pb
  año 2: producto −1,2 %, desempleo +4,1 pp, vivienda −19 %, tasa +150 pb
  año 3: producto +0,8 %, desempleo +3,6 pp, vivienda −17 %, tasa  −50 pb
```

**Paso 1 — verifica la coherencia del escenario.**

```text
producto cae → desempleo sube        ✓ (con rezago: el pico en año 2)
tasa sube → vivienda cae             ✓
desempleo alto en año 3 pese a recuperación del producto  ✓ (rezago típico)
inflación implícita al alza → tasa sube en años 1-2       ✓
tasa baja en año 3 cuando la inflación cede               ✓

escenario internamente coherente
```

**Paso 2 — traduce a parámetros de riesgo.**

```text
CONSUMO (PD base 3,2 %, LGD 62 %)
  año 1: PD × 1,42^2,8 = 3,2 % × 2,63 =  8,42 %
  año 2: PD × 1,42^4,1 = 3,2 % × 4,10 = 13,12 %
  año 3: PD × 1,42^3,6 = 3,2 % × 3,38 = 10,82 %

HIPOTECARIO (PD base 1,1 %, LGD 24 %)
  año 1: PD × 1,18^2,8 = 1,1 % × 1,58 = 1,74 %   LGD 24+7,2 = 31,2 %
  año 2: PD × 1,18^4,1 = 1,1 % × 1,91 = 2,10 %   LGD 24+11,4 = 35,4 %
  año 3: PD × 1,18^3,6 = 1,1 % × 1,77 = 1,95 %   LGD 24+10,2 = 34,2 %

COMERCIAL (PD base 2,4 %, LGD 45 %)
  año 1: PD × 1,25^3,4 = 2,4 % × 1,99 = 4,78 %
  año 2: PD × 1,25^1,2 = 4,78 % × 1,31 = 6,26 %  (acumulativo)
  año 3: recuperación parcial            = 5,40 %
```

**Paso 3 — calcula el costo de riesgo por año.**

```text
AÑO 1
  consumo:      520 000 × 8,42 % × 62 % =  27 146
  hipotecario:  890 000 × 1,74 % × 31,2 % =  4 832
  comercial:  1 530 000 × 4,78 % × 45 %  =  32 910
  TOTAL AÑO 1                              64 888

AÑO 2
  consumo:      520 000 × 13,12 % × 62 % = 42 299
  hipotecario:  890 000 × 2,10 % × 35,4 % =  6 616
  comercial:  1 530 000 × 6,26 % × 45 %  =  43 100
  TOTAL AÑO 2                              92 015

AÑO 3
  consumo:      520 000 × 10,82 % × 62 % = 34 884
  hipotecario:  890 000 × 1,95 % × 34,2 % =  5 936
  comercial:  1 530 000 × 5,40 % × 45 %  =  37 179
  TOTAL AÑO 3                              77 999
```

**Paso 4 — proyecta el resto del resultado.**

```text
MARGEN FINANCIERO
  año 1: −6 % (menor volumen, mora que no devenga)     204 920
  año 2: −11 % acumulado                               194 020
  año 3: −8 % acumulado                                200 560

COMISIONES
  año 1: −12 %   56 320
  año 2: −18 %   52 480
  año 3: −14 %   55 040

GASTOS OPERATIVOS
  año 1: −2 %   158 760
  año 2: −5 %   153 900
  año 3: −4 %   155 520
```

**Paso 5 — construye el resultado proyectado.**

```text
                        año 1     año 2     año 3
margen financiero      204 920   194 020   200 560
comisiones              56 320    52 480    55 040
gastos operativos     −158 760  −153 900  −155 520
resultado operacional  102 480    92 600   100 080
costo de riesgo        −64 888   −92 015   −77 999
RESULTADO ANTES DE IMPUESTO
                        37 592       585    22 081
impuesto (27 %)        −10 150      −158    −5 962
RESULTADO NETO          27 442       427    16 119
```

**Paso 6 — proyecta capital y activos ponderados.**

```text
ACTIVOS PONDERADOS (migración de calificación en el escenario)
  año 1: +7 %   2 439 600
  año 2: +13 % acumulado   2 576 400
  año 3: +11 % acumulado   2 530 800

CAPITAL (sin dividendos: la restricción se activa al cruzar el colchón)
  inicial              296 400
  año 1: +27 442       323 842
  año 2: +   427       324 269
  año 3: +16 119       340 388

RATIO DE CAPITAL
  año 1: 323 842 / 2 439 600 = 13,27 %
  año 2: 324 269 / 2 576 400 = 12,59 %
  año 3: 340 388 / 2 530 800 = 13,45 %

mínimo exigido: 10,5 %
punto más bajo: 12,59 % en el año 2
HOLGURA MÍNIMA: 2,09 puntos → 53 847 de capital
```

**Paso 7 — ejecuta la prueba inversa.**

```text
¿QUÉ ESCENARIO LLEVA EL CAPITAL AL 10,5 %?

capital necesario en el punto bajo: 10,5 % × 2 576 400 = 270 522
capital proyectado en año 2: 324 269
déficit que se necesitaría: 53 747 de pérdida adicional

¿de dónde vendría?
  si el costo de riesgo del año 2 fuera 92 015 + 53 747/0,73 = 165 638
  → PD del escenario × 1,80 sobre la ya estresada

TRADUCIDO A MACRO: desempleo +7,2 pp en lugar de +4,1
                   producto acumulado −8,9 % en lugar de −4,6 %

¿QUÉ TAN LEJANO ES ESO?
  el peor episodio del registro histórico del país: −6,8 % acumulado
  el escenario de quiebre está un 31 % más allá del peor registro

CONCLUSIÓN: el banco resiste el escenario adverso
            y su punto de quiebre está fuera del rango histórico
```

**Paso 8 — decisiones que se derivan.**

```text
1. CAPITAL
   holgura mínima de 53 847 en el año 2
   el plan de capital debe preservar esa holgura:
   suspensión automática de dividendos si el ratio proyectado < 11,5 %

2. CONCENTRACIÓN DEL DAÑO
   consumo aporta 46 % del costo de riesgo del año 2
   con solo 17,7 % de la cartera
   → revisar el apetito de crecimiento en ese segmento

3. NO LINEALIDAD
   las elasticidades se aplicaron linealmente sobre un rango
   sin precedente; ejecutar una variante con elasticidades
   convexas (+25 % en la parte severa) como sensibilidad

4. LIQUIDEZ
   este ejercicio proyectó solvencia. Falta la contraparte:
   proyectar la cobertura de liquidez bajo el mismo escenario,
   con fuga de depósitos coherente con el deterioro de solvencia

5. ACCIONES DE GESTIÓN
   ninguna acción de gestión se incluyó en la proyección
   → el resultado es el peor caso sin respuesta
     documentar qué acciones se activarían y en qué orden
```

**Interpreta:** el banco resiste, y **la información valiosa del ejercicio no es ese resultado sino su
descomposición**: el 17,7 % de la cartera genera el 46 % de la pérdida, y el punto de quiebre está a un
31 % más allá del peor episodio histórico. Una prueba de estrés que solo produce «aprobado» no se ha
usado; se usa cuando cambia una decisión de capital, de apetito o de negocio.

## 🏦 Del cliente al banco

El cliente no ve nada de esto y el banco calcula si sobreviviría a una recesión severa. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «El banco dejó de dar créditos de consumo» | Apetito revisado tras la prueba | 11, clase 13 |
| «Suspendieron el dividendo» | Restricción automática por colchón | 12, clase 11 |
| «El supervisor publicó los resultados» | Prueba supervisora y disciplina de mercado | 12, clase 13 |
| «Subieron las exigencias para mi crédito» | Migración de calificación en el escenario | 9, clase 6 |
| «Mi banco resistió la crisis» | Holgura de capital planificada | 11, clase 14 |

## 🧪 Práctica

El laboratorio pide diseñar un escenario coherente y proyectar el capital. El escenario tiene que romper alguna métrica: si no, no informa.

En `labs/lab-06.md`, sección de estrés:

1. Diseña un escenario adverso a tres años y verifica su coherencia interna.
2. Traduce las variables macro a parámetros de riesgo por cartera.
3. Proyecta resultado, activos ponderados y capital año a año.
4. Ejecuta una prueba inversa y evalúa qué tan lejano está el punto de quiebre.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen pruebas de estrés que no informan. Las causas son escenarios suaves y acciones de gestión no creíbles.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| El escenario es incoherente | Variables elegidas por separado | Verifica las relaciones entre ellas. |
| Solo se proyectan provisiones | Visión parcial | Proyecta margen, comisiones, gastos y activos ponderados. |
| Elasticidades lineales fuera de rango | Extrapolación | Añade una variante convexa. |
| Acciones de gestión heroicas | No creíbles en el escenario | Solo acciones ejecutables en crisis. |
| Se proyecta solvencia sin liquidez | Ejercicio incompleto | Ejecuta ambos, con supuestos coherentes. |
| Resultado «aprobado» sin decisiones | La prueba no se usó | Vincúlala a capital y apetito. |

## ❓ Preguntas de comprobación

1. ¿Qué pregunta responde una prueba de estrés que no responde el valor en riesgo?
2. ¿Por qué la coherencia interna del escenario importa más que su precisión?
3. ¿Por qué extrapolar elasticidades linealmente subestima la pérdida?
4. ¿Qué hace que una acción de gestión sea creíble en un escenario adverso?
5. ¿Qué aporta la prueba inversa que no aporta el escenario estándar?

## 📥 Entregable

Guarda en `portfolio/parte-11/clase-13/`:

- el escenario adverso con la verificación de coherencia;
- la traducción a parámetros de riesgo por cartera;
- la proyección de resultado, activos ponderados y capital;
- la prueba inversa con la distancia al punto de quiebre.

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

- Basel Committee on Banking Supervision (2018). *Stress testing principles*. BIS. <https://www.bis.org/bcbs/publ/d450.htm>
- European Banking Authority. *EU-wide stress test methodology* (ediciones sucesivas). EBA. <https://www.eba.europa.eu/risk-and-data-analysis/risk-analysis/eu-wide-stress-testing>
- Board of Governors of the Federal Reserve System. *Comprehensive Capital Analysis and Review (CCAR)* y *Dodd-Frank Act Stress Tests*. Federal Reserve.
- International Monetary Fund (2012). *Macrofinancial Stress Testing: Principles and Practices*. IMF.
- Hull, J. (2018). *Risk Management and Financial Institutions* (5.ª ed.). Wiley. Capítulo sobre pruebas de estrés.
- Verificación local: revisa el escenario supervisor vigente, su horizonte y las exigencias de autoevaluación de capital de tu jurisdicción.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 12 · Riesgo de modelo](12-riesgo-de-modelo.md) | [Parte 11](../README.md) · [Programa](../../../SYLLABUS.md) | [14 · Capital económico y asignación →](14-capital-economico-y-asignacion.md) |
<!-- gen:footer:end -->
