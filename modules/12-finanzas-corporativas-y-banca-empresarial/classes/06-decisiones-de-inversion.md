---
part: 13
class: 6
title: "Decisiones de inversión"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 06 · Decisiones de inversión

> [← 05 · Estructura y costo de capital](05-estructura-y-costo-de-capital.md) · [Índice de la parte](../README.md) · [07 · Crédito corporativo y estructuración →](07-credito-corporativo-y-estructuracion.md)

**Parte 13 — Finanzas corporativas y banca empresarial** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Evaluar si un proyecto crea o destruye valor. Es la decisión que el banco financia y por lo tanto la que
debe saber juzgar: un crédito que financia un proyecto de valor presente negativo tiene una fuente de
pago que se está deteriorando desde el día uno.

## 📚 Objetivos

Al finalizar podrás:

1. **Construir** el flujo de caja incremental de un proyecto.
2. **Aplicar** valor presente neto, tasa interna de retorno y período de recuperación.
3. **Reconocer** los errores clásicos de cada criterio.
4. **Incorporar** el análisis de sensibilidad y de escenarios.
5. **Valorar** la flexibilidad y las opciones reales de un proyecto.

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
| `flujo incremental` | Diferencia entre hacer y no hacer el proyecto. |
| `costo hundido` | Gasto ya incurrido; irrelevante para la decisión. |
| `costo de oportunidad` | Valor del mejor uso alternativo de un recurso. |
| `canibalización` | Pérdida de ventas de productos existentes por el nuevo. |
| `valor presente neto` | Suma descontada de los flujos menos la inversión. |
| `tasa interna de retorno` | Tasa que hace el valor presente neto igual a cero. |
| `período de recuperación descontado` | Tiempo hasta recuperar la inversión, descontando. |
| `opción real` | Flexibilidad de expandir, postergar o abandonar. |

## 🧠 Modelo mental

```text
LA ÚNICA PREGUNTA DE UNA DECISIÓN DE INVERSIÓN

  ¿qué cambia si hago esto,
   comparado con no hacerlo?

TODO LO QUE NO CAMBIA ES IRRELEVANTE
  el estudio ya pagado, la deuda existente,
  el edificio que ya tienes, los sueldos que pagarías igual

TODO LO QUE CAMBIA ES RELEVANTE
  aunque no sea un desembolso:
  el terreno que podrías vender, las ventas que perderás
  en otro producto, el capital de trabajo que consumirás
```

## 📖 Desarrollo

### 1. Flujo incremental

```text
CONSTRUCCIÓN
  + ingresos incrementales
  − costos incrementales
  − depreciación (para calcular impuestos)
  = resultado antes de impuestos
  − impuestos
  + depreciación (que no es salida de caja)
  = flujo operativo
  − inversión en activo fijo
  − inversión en capital de trabajo
  + valor residual al final
  = FLUJO DE CAJA DEL PROYECTO
```

| Qué incluir | Qué excluir |
|---|---|
| Costo de oportunidad de recursos propios | Costos hundidos |
| Canibalización de otros productos | Gastos generales que no cambian |
| Aumento del capital de trabajo | Intereses del financiamiento |
| Valor residual o de liquidación | Depreciación como salida de caja |
| Efectos fiscales de la venta de activos | Costos de estudios ya realizados |

```text
POR QUÉ NO SE INCLUYEN LOS INTERESES
  el costo del financiamiento ya está en la TASA DE DESCUENTO
  incluirlo también en el flujo lo contaría dos veces

  el flujo del proyecto es el flujo PARA TODOS los proveedores
  de capital; el WACC reparte ese flujo entre ellos
```

### 2. Los criterios

| Criterio | Regla | Ventaja | Limitación |
|---|---|---|---|
| Valor presente neto | Aceptar si > 0 | Mide creación de valor en unidades monetarias | Requiere estimar la tasa |
| Tasa interna de retorno | Aceptar si > costo de capital | Intuitiva, comparable | Múltiples soluciones; supone reinversión a la TIR |
| Índice de rentabilidad | Aceptar si > 1 | Útil con capital racionado | No mide magnitud |
| Período de recuperación | Aceptar si < umbral | Simple, mide liquidez | Ignora lo posterior; no descuenta |
| Período descontado | Aceptar si < umbral | Corrige el anterior | Sigue ignorando lo posterior |

```text
CUANDO VPN Y TIR SE CONTRADICEN
  ocurre con proyectos MUTUAMENTE EXCLUYENTES
  de tamaño o perfil temporal distinto

  proyecto A: inversión 100, VPN 40, TIR 28 %
  proyecto B: inversión 500, VPN 120, TIR 19 %

  la TIR prefiere A; el VPN prefiere B
  EL VPN TIENE RAZÓN: 120 de valor supera a 40

  la TIR es un porcentaje y no sabe sobre cuánto se aplica
```

```text
TIR MÚLTIPLE
  ocurre cuando el flujo cambia de signo más de una vez
  (inversión, flujos positivos, y un desembolso final:
   cierre de mina, desmantelamiento)

  → hay tantas TIR como cambios de signo
  → usa VPN
```

### 3. Sensibilidad y escenarios

```text
ANÁLISIS DE SENSIBILIDAD
  ¿cuánto cambia el VPN si una variable cambia un 10 %?
  → identifica las variables CRÍTICAS

VALOR CRÍTICO
  ¿hasta dónde puede empeorar una variable
  antes de que el VPN sea cero?
  → es la información más útil para el banco

ESCENARIOS
  combinaciones coherentes de variables
  optimista, base, pesimista

SIMULACIÓN
  distribuciones para las variables clave
  → distribución del VPN, no un número
```

### 4. Opciones reales

```text
UN PROYECTO NO ES UNA DECISIÓN IRREVERSIBLE TOMADA HOY
  es una secuencia de decisiones con información creciente

TIPOS DE OPCIÓN
  DIFERIR      esperar información antes de invertir
  EXPANDIR     invertir más si el proyecto va bien
  ABANDONAR    salir si va mal, recuperando algo
  CAMBIAR      alterar insumos, productos o escala
  ETAPAS       invertir por fases, con decisión en cada una
```

```text
POR QUÉ IMPORTAN
  el VPN tradicional supone un plan fijo
  y por lo tanto SUBESTIMA los proyectos flexibles

  un proyecto con VPN de −20 puede valer +60
  si incorpora la opción de abandonar tras la primera fase
```

**Para el banco, la opción más relevante es la de abandono**, porque define el valor de recuperación si
el proyecto falla, y ese valor es exactamente la LGD de su crédito.

## 🧮 Ejemplo guiado

**Situación.** Una empresa evalúa una planta nueva y solicita financiamiento.

```text
PROYECTO
  inversión en activo fijo                    8 400
  vida útil y horizonte                       8 años
  valor residual estimado al año 8            1 200
  ingresos incrementales anuales              6 800
  costos operativos incrementales anuales     4 420
  aumento de capital de trabajo (año 0)         840
  depreciación lineal a 8 años                1 050
  tasa de impuesto                               27 %
  WACC de la empresa                          13,6 %

DATOS ADICIONALES
  · el estudio de factibilidad costó 180, ya pagado
  · el terreno es propio; podría venderse en 1 600
  · la nueva planta canibalizará 620 anuales
    de margen de la planta existente
```

**Paso 1 — decide qué entra en el flujo.**

```text
ESTUDIO DE FACTIBILIDAD (180)     COSTO HUNDIDO → NO entra
TERRENO PROPIO (1 600)            COSTO DE OPORTUNIDAD → SÍ entra
                                  como salida en el año 0
CANIBALIZACIÓN (620 anuales)      SÍ entra como menor margen
CAPITAL DE TRABAJO (840)          SÍ entra; se recupera al final
```

**Paso 2 — construye el flujo anual.**

```text
ingresos incrementales               6 800
costos operativos                   −4 420
canibalización                        −620
depreciación                        −1 050
resultado antes de impuestos           710
impuestos (27 %)                      −192
resultado neto                         518
+ depreciación                       1 050
FLUJO OPERATIVO ANUAL                1 568
```

**Paso 3 — construye el flujo completo.**

```text
AÑO 0
  inversión en activo fijo          −8 400
  costo de oportunidad del terreno  −1 600
  capital de trabajo                  −840
  TOTAL AÑO 0                      −10 840

AÑOS 1 a 7
  flujo operativo                    1 568

AÑO 8
  flujo operativo                    1 568
  recuperación de capital de trabajo   840
  valor residual del activo            1 200
    efecto fiscal: valor libro 0
    → impuesto sobre 1 200 × 27 % =    −324
  valor del terreno recuperado       1 600
  TOTAL AÑO 8                        4 884
```

**Paso 4 — calcula el valor presente neto.**

```text
factor de anualidad a 13,6 %, 7 años: 4,3457
VP de los años 1-7: 1 568 × 4,3457 = 6 814

factor de descuento año 8: 1/1,136^8 = 0,3617
VP del año 8: 4 884 × 0,3617 = 1 766

VPN = −10 840 + 6 814 + 1 766 = −2 260
```

**Paso 5 — interpreta y busca el error de diseño.**

```text
VPN NEGATIVO: el proyecto destruye 2 260 de valor

¿QUÉ LO HUNDE?
  · el terreno tiene un costo de oportunidad de 1 600
    que se recupera al año 8, pero descontado vale 579
    → costo neto del terreno: 1 021
  · la canibalización resta 620 anuales
    valor presente: 620 × 0,73 × 4,3457 + año 8 = ~2 190
  · el flujo operativo de 1 568 sobre una inversión de 10 840
    da un retorno contable del 14,5 %, apenas sobre el WACC
```

**Paso 6 — calcula los valores críticos.**

```text
¿QUÉ TENDRÍA QUE CAMBIAR PARA QUE EL VPN SEA CERO?

INGRESOS
  el flujo operativo debe subir en 2 260/4,7074 (factor total) = 480
  480 / (1 − 0,27) = 658 de margen adicional
  sobre ingresos de 6 800: +9,7 % de ingresos, o
  reducción de costos equivalente

CANIBALIZACIÓN
  si fuera de 620 − 658 = negativa: imposible
  la canibalización sola no puede corregirlo

WACC
  TIR del proyecto: resolviendo, ≈ 9,4 %
  el proyecto solo es viable si el costo de capital baja a 9,4 %
```

**Paso 7 — evalúa la opción de abandono.**

```text
EL PROYECTO PUEDE HACERSE EN DOS FASES
  fase 1: 4 600 de inversión, capacidad del 55 %
          ingresos 3 900, costos 2 620, canibalización 340
  decisión al año 2: expandir o no

  si la demanda se confirma: invertir 3 800 adicionales
  si no: operar a escala reducida o vender la instalación
         valor de liquidación estimado: 2 900
```

```text
VALOR CON FLEXIBILIDAD (árbol simplificado)
  probabilidad de demanda alta: 55 %
  probabilidad de demanda baja: 45 %

  ESCENARIO ALTO (expande en el año 2)
    VPN desde el año 2 de la expansión: +1 840
    VPN de la fase 1 en escenario alto: +680
    total: +2 520

  ESCENARIO BAJO (no expande, opera reducido)
    VPN de la fase 1 en escenario bajo: −1 420
    con opción de venta en 2 900 al año 3: −620

  VPN ESPERADO CON FLEXIBILIDAD
    0,55 × 2 520 + 0,45 × (−620) = 1 386 − 279 = 1 107
    descontado al año 0 y neto de la inversión inicial: +1 107
```

**Paso 8 — formula la recomendación.**

```text
PROYECTO COMPLETO EN UNA FASE:   VPN −2 260   → rechazar
PROYECTO EN DOS FASES:           VPN +1 107   → aceptar

LA DIFERENCIA NO ES EL PROYECTO: ES LA ESTRUCTURA DE LA DECISIÓN

DESDE EL BANCO
  · financiar la fase 1 (4 600) con un crédito a 5 años
  · comprometer, sin obligar, la fase 2 sujeta a resultados
  · la opción de venta en 2 900 es la garantía real
    del escenario bajo → define la LGD
  · covenant de resultados de la fase 1 como condición
    para desembolsar la fase 2

  exposición máxima en el escenario malo: 4 600
  valor de recuperación: 2 900 → LGD 37 %
  frente al proyecto completo: exposición 8 400,
  recuperación estimada 3 400 → LGD 60 %
```

**Interpreta:** el proyecto pasó de destruir 2 260 a crear 1 107 **sin cambiar un solo supuesto
operativo**. Lo único que cambió fue la secuencia de decisiones. Y para el banco el efecto fue igual de
grande: la LGD bajó de 60 % a 37 %. Estructurar un proyecto por fases no es una precaución
administrativa: **es la forma de crear valor donde el análisis rígido solo ve destrucción**.

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Ya gasté en el estudio, hay que hacerlo» | Costo hundido, irrelevante | 13, clase 6 |
| «El terreno es mío, no cuesta nada» | Costo de oportunidad | 13, clase 6 |
| «El banco financia solo la primera fase» | Opción de abandono y LGD | 13, clase 6 |
| «Mi TIR es del 28 %» | Sobre cuánto capital importa | 13, clase 6 |
| «El proyecto se paga en 3 años» | El período de recuperación no mide valor | 13, clase 6 |

## 🧪 Práctica

En `labs/lab-03.md`, sección de inversión:

1. Construye el flujo incremental de un proyecto identificando qué entra y qué no.
2. Calcula VPN, TIR y período descontado, y explica cualquier contradicción.
3. Determina los valores críticos de las tres variables más sensibles.
4. Valora la opción de abandono y su efecto sobre la LGD del banco.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se incluye el costo hundido | «Ya lo gastamos» | Es irrelevante para la decisión. |
| Se omite el costo de oportunidad | Recurso propio parece gratis | Valóralo a su mejor uso alternativo. |
| Se incluyen los intereses en el flujo | Doble cómputo | Ya están en la tasa de descuento. |
| Se decide por TIR entre excluyentes | Ignora la magnitud | Decide por VPN. |
| Se ignora la canibalización | Solo se ven los ingresos nuevos | Es un flujo incremental negativo. |
| Se evalúa el proyecto como decisión única | Se pierde el valor de la flexibilidad | Estructura por fases. |

## ❓ Preguntas de comprobación

1. ¿Cuál es la única pregunta que define un flujo incremental?
2. ¿Por qué no se incluyen los intereses en el flujo del proyecto?
3. ¿Cuándo se contradicen VPN y TIR, y cuál tiene razón?
4. ¿Qué información aporta un valor crítico que no aporta el VPN?
5. ¿Por qué la opción de abandono importa especialmente al banco?

## 📥 Entregable

Guarda en `portfolio/parte-13/clase-06/`:

- el flujo incremental construido, con la justificación de cada inclusión y exclusión;
- VPN, TIR y período descontado calculados con su interpretación;
- los valores críticos de las tres variables más sensibles;
- la valoración de la opción de abandono y su efecto sobre la LGD.

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

- Brealey, R., Myers, S. y Allen, F. (2020). *Principles of Corporate Finance* (13.ª ed.). McGraw-Hill. Capítulos 5 a 11 y 22.
- Ross, S., Westerfield, R. y Jaffe, J. (2019). *Corporate Finance* (12.ª ed.). McGraw-Hill.
- Damodaran, A. (2012). *Investment Valuation* (3.ª ed.). Wiley.
- Trigeorgis, L. (1996). *Real Options: Managerial Flexibility and Strategy in Resource Allocation*. MIT Press.
- Blank, L. y Tarquin, A. (2018). *Engineering Economy* (8.ª ed.). McGraw-Hill. Criterios de evaluación y TIR múltiple.
- Verificación local: revisa las reglas de depreciación fiscal, el tratamiento de la venta de activos y los incentivos tributarios a la inversión de tu país.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 05 · Estructura y costo de capital](05-estructura-y-costo-de-capital.md) | [Parte 13](../README.md) · [Programa](../../../SYLLABUS.md) | [07 · Crédito corporativo y estructuración →](07-credito-corporativo-y-estructuracion.md) |
<!-- gen:footer:end -->
