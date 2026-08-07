<!-- meta
part: 16
class: 7
title: "Originación y decisión"
level: profesional
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 07 · Originación y decisión

> [← 06 · Modelo de precios](06-modelo-de-precios.md) · [Índice de la parte](../README.md) · [08 · Modelos de riesgo →](08-modelos-de-riesgo.md)

**Parte 16 — Proyecto Banco Virtual** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Construir el proceso por el que el Banco Austral capta, evalúa y aprueba a sus clientes. Es el proceso
que determina la calidad de toda la cartera futura, y su diseño debe conciliar tres exigencias que
tiran en direcciones distintas: **velocidad, calidad de riesgo y protección del cliente**.

Con productos y precios definidos, esta clase construye el proceso que los coloca. Aplica la Parte 9 entera y añade lo que un proyecto obliga a decidir: dónde está exactamente la frontera entre aprobar, rechazar y derivar a análisis manual.

## 📚 Objetivos

Al finalizar podrás:

1. **Diseñar** el flujo de originación completo, paso a paso.
2. **Definir** la política de crédito con criterios verificables.
3. **Configurar** el motor de decisión y sus tres zonas.
4. **Establecer** el régimen de excepciones y su control.
5. **Medir** el proceso con indicadores que anticipan el riesgo.

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

Los cuatro primeros términos son el proceso y su política; los cuatro siguientes, las zonas y su medición. La **excepción** es lo que hay que gobernar desde el principio: un proceso sin vía formal de excepción produce excepciones informales que nadie registra.

| Concepto | Comprensión verificable |
|---|---|
| `flujo de originación` | Secuencia desde la solicitud hasta el desembolso. |
| `política de crédito` | Criterios que definen a quién y cuánto se presta. |
| `motor de decisión` | Sistema que aplica la política y el modelo. |
| `zona de decisión` | Aprobación automática, revisión o rechazo. |
| `excepción` | Aprobación fuera de política, registrada y aprobada. |
| `capacidad de pago` | Que el cliente pueda pagar sin deteriorar su situación. |
| `verificación` | Contraste de un dato con una fuente independiente. |
| `tasa de conversión` | Solicitudes que llegan a desembolso. |

## 🧠 Modelo mental

El modelo mental son tres zonas de decisión: una donde se aprueba automáticamente, otra donde se rechaza y una intermedia donde decide una persona. El tamaño de la zona intermedia determina el costo del proceso y la calidad de la cartera, y es una decisión de negocio.

```text
TRES EXIGENCIAS QUE TIRAN EN DIRECCIONES DISTINTAS

  VELOCIDAD        el cliente la valora; es la propuesta
  CALIDAD          determina el costo de riesgo comprometido
  PROTECCIÓN       la fricción cumple una función (Parte 14, clase 7)

  EL DISEÑO NO ELIGE ENTRE ELLAS: LAS ORDENA

    velocidad donde el riesgo es bajo y el dato es fiable
    fricción donde la decisión es irreversible o el cliente
      puede no entenderla
    calidad siempre, con datos verificados

  UN PROCESO DE 90 SEGUNDOS PARA TODO
  MAXIMIZA LA CONVERSIÓN Y DESTRUYE LAS OTRAS DOS
```

## 📖 Desarrollo

### 1. Flujo de originación

El flujo tiene etapas con puntos de decisión y de abandono. El esquema lo recorre.

```text
1. CAPTACIÓN         canal digital, corresponsal o referido
2. IDENTIFICACIÓN    documento y biometría con prueba de vida
3. CRIBADO           listas de sanciones y verificaciones básicas
4. CONSENTIMIENTOS   datos alternativos, con alcance y plazo
5. RECOPILACIÓN      fuentes alternativas y buró, si existe
6. EVALUACIÓN        modelo + política → recomendación
7. DECISIÓN          automática, revisión humana o rechazo
8. OFERTA            monto, plazo y tasa, con costo total
9. COMPRENSIÓN       verificación de que el cliente entendió
10. ACEPTACIÓN       firma electrónica con evidencia
11. DESEMBOLSO       a cuenta a nombre del solicitante
12. REGISTRO         decisión, factores y datos, para explicabilidad
```

De los pasos anteriores hay dos que se omiten con frecuencia y cuya ausencia tiene consecuencias distintas: uno comercial y otro normativo.

```text
LOS PASOS 9 Y 12 SON LOS QUE MÁS SE OMITEN

  el 9 protege al cliente y reduce reclamos futuros
  el 12 es obligatorio por norma (Parte 14, clase 11)
    y sin él no hay explicación ni revisión posible
```

### 2. Política de crédito

La política de crédito se escribe como reglas con su origen. La tabla las recoge.

```text
P2 — CRÉDITO ESCALONADO A PERSONAS

  CRITERIOS DE ADMISIÓN
    edad                        21 a 68 años
    ingreso verificable         al menos una fuente, 6+ meses
    carga financiera total      ≤ 45 % del ingreso verificado
    mora vigente en el sistema  ninguna > 60 días
    documentación               identidad verificada

  DIMENSIONAMIENTO
    monto máximo del escalón    según tabla de escalones
    Y limitado por: (ingreso − gastos estimados) × 0,35
                    × plazo, descontado a la tasa

  ASCENSO DE ESCALÓN
    cumplimiento íntegro del escalón anterior
    Y capacidad verificada para el nuevo monto
    Y sin deterioro de su carga financiera total

E2 — CAPITAL DE TRABAJO A EMPRESAS

  CRITERIOS DE ADMISIÓN
    antigüedad                  ≥ 12 meses de operación
    ventas por medios de pago   ≥ 6 meses de historial
    variabilidad de ventas      coeficiente de variación ≤ 0,45
    mora en el sistema          ninguna > 60 días
    beneficiario final          identificado y verificado

  DIMENSIONAMIENTO
    línea = ventas medias mensuales × 1,8
    limitado por: cobertura del servicio ≥ 1,35
```

```text
EL CRITERIO DE VARIABILIDAD DE VENTAS
  es el más específico del modelo del Banco Austral

  una empresa con ventas muy variables
  puede tener buenas ventas medias y no poder pagar
  en los meses malos
  → el coeficiente de variación lo captura
    y ningún estado financiero anual lo muestra
```

### 3. Motor de decisión

El motor aplica la política y devuelve una decisión con su motivo. El esquema lo describe.

```text
TRES ZONAS (Parte 14, clase 6)

  APROBACIÓN AUTOMÁTICA
    cumple todos los criterios de política
    Y el modelo lo sitúa en el rango de menor riesgo
    → decisión en segundos, sin intervención humana
    → automatizar lo que BENEFICIA al solicitante

  REVISIÓN HUMANA
    cumple los criterios y el modelo lo sitúa
    en el rango intermedio
    O hay una discrepancia entre fuentes de datos
    → analista con la recomendación y sus factores

  RECHAZO RECOMENDADO
    incumple un criterio de política
    O el modelo lo sitúa en el rango de mayor riesgo
    → NUNCA automático: pasa a revisión humana
    → el analista puede confirmar o discrepar
```

| Zona | P2 personas | E2 empresas |
|---|---:|---:|
| Aprobación automática | 38 % | 22 % |
| Revisión humana | 34 % | 51 % |
| Rechazo recomendado | 28 % | 27 % |

La diferencia de automatización entre ambos productos no es un descuido:
responde a lo que el modelo puede y no puede capturar.

```text
POR QUÉ E2 TIENE MENOS AUTOMATIZACIÓN
  la evaluación de una empresa exige juicio
  sobre su modelo de negocio y su variabilidad
  que el modelo captura parcialmente
  → la automatización se amplía cuando el modelo madura,
    no antes
```

### 4. Excepciones

Las excepciones tienen vía, nivel y registro. La tabla los recoge.

```text
RÉGIMEN DE EXCEPCIONES

  QUÉ ES UNA EXCEPCIÓN
    aprobar una operación que incumple
    un criterio de política

  QUIÉN PUEDE APROBARLA
    comité de crédito; nunca por delegación individual
    (la lección de la Parte 12, clase 14)

  QUÉ SE REGISTRA
    · el criterio incumplido y su valor
    · el fundamento de la excepción
    · quién la aprobó y cuándo
    · el desempeño posterior de la operación

  LÍMITE
    excepciones ≤ 10 % de las aprobaciones,
    medido mensualmente por canal y por analista

  CONTROL QUE EVITA EL FRAUDE DE LA PARTE 12, CLASE 14
    · todo dato de entrada del solicitante
      queda registrado con su origen y su momento
    · cualquier modificación posterior a la evaluación
      queda trazada y bloquea la aprobación automática
    · verificación mensual del 100 % de las aprobaciones
      contra los parámetros de política, de forma automática
      → detecta las excepciones NO registradas
```

### 5. Indicadores del proceso

El proceso se mide con indicadores de conversión y de calidad. La tabla los recoge.

| Indicador | Objetivo | Qué anticipa |
|---|---:|---|
| Tiempo de decisión (P2) | < 5 minutos | Propuesta de valor |
| Tiempo de decisión (E2) | < 48 horas | Propuesta de valor |
| Tasa de aprobación (P2) | 34 % | Acceso |
| Tasa de conversión a desembolso | 78 % | Fricción del proceso |
| Excepciones sobre aprobaciones | ≤ 10 % | Costo de riesgo futuro |
| Excepciones no registradas | 0 | Integridad del control |
| Verificación de comprensión superada | ≥ 95 % | Reclamos futuros |
| Mora a 6 meses de la cosecha | ≤ 2,4 % | Costo de riesgo |
| Abandono en el proceso | ≤ 18 % | Fricción excesiva |

De los nueve indicadores, dos anticipan el deterioro con meses de ventaja
sobre el resto.

```text
LOS DOS INDICADORES DECISIVOS
  · excepciones sobre aprobaciones: anticipa el costo
    de riesgo con 12 meses de ventaja
  · mora a 6 meses de la cosecha: lo confirma antes
    que el costo de riesgo del período
```

## 🧮 Ejemplo guiado

El ejemplo define las tres zonas de decisión y calcula su efecto sobre conversión y pérdida. Mover la frontera mejora una y empeora la otra.

**Situación.** Calibrar la política de crédito de P2 para alcanzar el costo de riesgo comprometido.

```text
COMPROMISO (clase 5): costo de riesgo 3,60 % de la cartera total
  la cartera de P2 es la de mayor riesgo
  y representa el 35 % de la cartera
```

**Paso 1 — determina el costo de riesgo admisible de P2.**

```text
COSTO DE RIESGO TOTAL: 3,60 % de 335 971 = 12 095

  E2 (capital de trabajo): PD 4,2 %, LGD 48 %
    214 000 × 4,2 % × 48 % = 4 314
  E3 (anticipo): PD 0,4 %, LGD 35 %
    3 923 × 0,4 % × 35 % = 5

  DISPONIBLE PARA P2: 12 095 − 4 319 = 7 776
  sobre cartera P2 de 118 048: 6,59 %
```

**Paso 2 — determina la PD máxima admisible de P2.**

```text
con LGD del 58 %:
  PD máxima = 6,59 % / 58 % = 11,36 %

  ¿ES ALCANZABLE EN UN SEGMENTO SIN HISTORIAL?
    PD del segmento sin selección: 18-24 %
    PD con modelo de datos alternativos
    y corte en el 34 % superior: 11,4 %  (Parte 14, clase 7)
    → SÍ, con el corte correcto
```

**Paso 3 — calibra el corte del modelo.**

```text
DISTRIBUCIÓN DE PD PREDICHA DE LOS SOLICITANTES

  decil de riesgo    PD media   % acumulado de solicitantes
    1 (mejor)          3,2 %          10 %
    2                  5,1 %          20 %
    3                  7,4 %          30 %
    4                 10,2 %          40 %
    5                 13,8 %          50 %
    6                 18,1 %          60 %
    7                 23,6 %          70 %
    8                 30,4 %          80 %
    9                 39,8 %          90 %
   10 (peor)          54,2 %         100 %

  CORTE EN EL DECIL 4
    aprobación: 40 % de los solicitantes
    PD media de los aprobados:
      (3,2+5,1+7,4+10,2)/4 = 6,48 %
    costo de riesgo: 6,48 % × 58 % = 3,76 %
    → muy por debajo del 6,59 % admisible

  CORTE EN EL DECIL 6
    aprobación: 60 %
    PD media: (3,2+5,1+7,4+10,2+13,8+18,1)/6 = 9,63 %
    costo de riesgo: 5,59 %
    → dentro del admisible
```

**Paso 4 — evalúa el corte por su efecto en el negocio.**

```text
                     decil 4    decil 5    decil 6
  aprobación            40 %       50 %       60 %
  PD media            6,48 %     7,94 %     9,63 %
  costo de riesgo     3,76 %     4,61 %     5,59 %
  margen (23,5 % − 7,88 % − costo de riesgo)
                     11,86 %    11,01 %    10,03 %
  cartera            118 048    147 560    177 072
  MARGEN NETO         14 000     16 246     17 760

  el corte en el decil 6 produce más margen
  Y consume más capital y más costo de riesgo
```

**Paso 5 — verifica contra las restricciones.**

```text
CORTE EN EL DECIL 6
  cartera P2: 177 072
  activos ponderados: 132 804  (era 88 536)
  incremento: 44 268

  ACTIVOS PONDERADOS TOTALES: 311 725 + 44 268 = 355 993
  capital al 14 %: 49 839
  capital disponible: 50 000  ✓ apenas

  COSTO DE RIESGO TOTAL
    P2: 177 072 × 5,59 % = 9 898
    E2 + E3: 4 319
    TOTAL: 14 217
    sobre cartera de 394 995: 3,60 %  ✓ exactamente el compromiso
```

**Paso 6 — cuestiona el resultado.**

```text
EL CORTE EN EL DECIL 6 CUMPLE JUSTO
TODAS LAS RESTRICCIONES

  capital: 49 839 de 50 000 → holgura de 0,3 %
  costo de riesgo: exactamente el compromiso

  UNA SOLUCIÓN QUE CUMPLE JUSTO
  NO TIENE MARGEN PARA NINGUNA DESVIACIÓN

  Y HAY UNA CONSIDERACIÓN ADICIONAL
    el decil 6 tiene PD del 18,1 %
    ¿es responsable prestar a alguien
     con 18 % de probabilidad de incumplir?
```

**Paso 7 — introduce el escalonamiento como respuesta.**

```text
EL ESCALONAMIENTO RESUELVE EL DILEMA (Parte 14, clase 7)

  DECILES 1 A 4: escalón inicial 1,0
  DECILES 5 Y 6: escalón inicial 0,4, plazo 6 meses
    · pérdida máxima por operación: 0,4 × 58 % = 0,232
    · el cliente construye historial
    · el ascenso exige cumplimiento Y capacidad

  EFECTO
    cartera del decil 5-6 en el año 1: menor
    59 024 clientes × 0,4 = 23 610
    frente a 59 024 × 2,80 = 165 267 si entraran
    al monto medio

  CARTERA P2 AJUSTADA
    deciles 1-4: 47 219 clientes × 2,80 = 132 213
      (ajustado: no todos toman el máximo)
      cartera efectiva: 94 438
    deciles 5-6: 23 610
    TOTAL: 118 048  → coincide con la proyección original
```

**Paso 8 — establece la política final.**

```text
POLÍTICA DE P2 — CALIBRACIÓN FINAL

  CORTE DE APROBACIÓN: decil 6 (PD ≤ 18,1 %)
  aprobación: 60 % de los solicitantes que cumplen
  los criterios de admisión

  ESCALÓN INICIAL SEGÚN RIESGO
    deciles 1-2:  escalón 2 (1,0), plazo 9 meses
    deciles 3-4:  escalón 1-2 (0,4-1,0), plazo 6-9 meses
    deciles 5-6:  escalón 1 (0,4), plazo 6 meses
    deciles 7-10: rechazo, con explicación y con indicación
                  de qué cambiaría la decisión

  RESULTADO
    cartera P2: 118 048
    PD media ponderada por monto: 6,84 %
      (los deciles altos pesan poco por su monto menor)
    costo de riesgo P2: 3,97 %
    costo de riesgo total: 3,26 %
    → BAJO el compromiso de 3,60 %  ✓ con holgura

    activos ponderados: 311 725
    capital al 14 %: 43 642 de 50 000  ✓ holgura de 12,7 %

  Y EL EFECTO SOCIAL
    se aprueba al 60 % de los solicitantes,
    no al 40 %, sin aumentar el costo de riesgo
    → 20 puntos más de inclusión, financiados
      por el escalonamiento y no por más riesgo
```

**Interpreta:** el escalonamiento permitió **aprobar al 60 % en lugar del 40 % con menos costo de riesgo
que cualquiera de los cortes simples**. La razón es que el riesgo de una cartera no depende solo de a
quién se aprueba, sino de cuánto se le presta: dar 0,4 a alguien con 18 % de PD produce menos pérdida
esperada que dar 2,8 a alguien con 10 %. Ese es el mecanismo que hace compatibles la inclusión y la
prudencia.

## 🏦 Del cliente al banco

El solicitante quiere una respuesta rápida y el banco equilibra automatización con calidad. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Me aprobaron en dos minutos» | Zona de aprobación automática | 14, clase 6 |
| «Me rechazaron y me dijeron por qué» | Rechazo con revisión y explicación | 14, clase 11 |
| «Me dieron menos de lo que pedí» | Escalón inicial según riesgo | 16, clase 7 |
| «Me preguntaron si entendí» | Verificación de comprensión | 12, clase 8 |
| «Subí de monto al cumplir» | Ascenso por cumplimiento y capacidad | 14, clase 7 |

## 🧪 Práctica

El laboratorio pide definir las zonas de decisión y justificar sus umbrales. El efecto sobre conversión y pérdida es lo que sostiene la justificación.

En `labs/lab-04.md`:

1. Diseña el flujo de originación con sus doce pasos y sus controles.
2. Define la política de crédito de dos productos con criterios verificables.
3. Calibra el corte del modelo contra el costo de riesgo comprometido.
4. Diseña el escalonamiento y evalúa su efecto sobre inclusión y riesgo.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen procesos de originación con problemas. Las causas son zonas mal calibradas y excepciones sin registro.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Proceso uniforme de 90 segundos | Ignora protección y calidad | Fricción donde corresponde. |
| Rechazo automático | Afecta derechos | Siempre con revisión humana. |
| Sin registro de la decisión | No hay explicabilidad | Es obligatorio. |
| Excepciones por delegación individual | Se pierde el control | Solo comité. |
| Se calibra el corte sin el escalonamiento | Se sacrifica inclusión o prudencia | Combínalos. |
| Solución que cumple justo | Sin margen para desviaciones | Busca holgura. |

## ❓ Preguntas de comprobación

1. ¿Cómo ordena el diseño las tres exigencias en conflicto?
2. ¿Por qué E2 tiene menos automatización que P2?
3. ¿Qué control detecta las excepciones no registradas?
4. ¿Por qué el escalonamiento permite aprobar más con menos riesgo?
5. ¿Qué indicador anticipa el costo de riesgo con doce meses de ventaja?

## 📥 Entregable

Guarda en `portfolio/parte-16/clase-07/`:

- el flujo de originación con sus pasos y controles;
- la política de crédito de dos productos;
- la calibración del corte con su verificación contra las restricciones;
- el diseño del escalonamiento con su efecto sobre inclusión y costo de riesgo.

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

- Siddiqi, N. (2017). *Intelligent Credit Scoring* (2.ª ed.). Wiley.
- Anderson, R. (2007). *The Credit Scoring Toolkit*. Oxford University Press.
- World Bank y CGAP (2019). *Alternative Data Transforming SME Finance*. World Bank Group.
- OECD (2022). *G20/OECD High-Level Principles on Financial Consumer Protection*. OECD.
- Basel Committee on Banking Supervision (2017). *Basel III: Finalising post-crisis reforms*, exposiciones minoristas. BIS.
- Verificación local: revisa las obligaciones de evaluación de capacidad de pago, información precontractual y notificación de rechazo de tu país.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 06 · Modelo de precios](06-modelo-de-precios.md) | [Parte 16](../README.md) · [Programa](../../../SYLLABUS.md) | [08 · Modelos de riesgo →](08-modelos-de-riesgo.md) |
<!-- gen:footer:end -->
