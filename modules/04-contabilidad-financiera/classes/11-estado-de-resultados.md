---
part: 5
class: 11
title: "Estado de resultados"
level: intermedio
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 11 · Estado de resultados

> [← 10 · Estado de situación financiera](10-estado-de-situacion-financiera.md) · [Índice de la parte](../README.md) · [12 · Estado de flujo de efectivo →](12-estado-de-flujo-de-efectivo.md)

**Parte 05 — Contabilidad financiera** · **Nivel:** Intermedio — requiere las partes anteriores · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Leer el estado que responde "cómo me fue" separando lo recurrente de lo excepcional, y lo operativo
de lo financiero. Un resultado neto positivo puede provenir de la venta de un terreno y ocultar una
operación que pierde dinero. Esta clase enseña a descomponerlo en sus niveles de margen y a construir
el resultado normalizado que un analista usa para proyectar.

## 📚 Objetivos

Al finalizar podrás:

1. **Presentar** un estado de resultados por función y por naturaleza.
2. **Calcular** e interpretar los cinco niveles de margen.
3. **Separar** resultado operativo, no operativo y excepcional.
4. **Construir** un resultado normalizado eliminando partidas no recurrentes.
5. **Relacionar** el resultado con el balance y con el flujo de efectivo.

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

| Concepto | Comprensión verificable |
|---|---|
| `presentación por función` | Costo de ventas, gastos de administración, gastos de distribución. Es la más común. |
| `presentación por naturaleza` | Materias primas, remuneraciones, depreciación, servicios. Más informativa sobre la estructura. |
| `margen bruto` | `(ventas − costo de ventas) / ventas`. Poder de fijación de precio y eficiencia de producción. |
| `resultado operativo` | Antes de intereses e impuestos. Mide el desempeño del negocio, sin financiamiento. |
| `EBITDA` | Resultado operativo más depreciación y amortización. **No** es flujo de caja, aunque se use como aproximación. |
| `partida no recurrente` | Ingreso o gasto que no se repetirá: venta de activos, indemnizaciones, deterioros extraordinarios. |
| `resultado normalizado` | Resultado depurado de partidas no recurrentes. Base para proyectar. |

## 🧠 Modelo mental

El estado de resultados se lee **en cascada**, y cada peldaño responde una pregunta distinta:

```text
Ventas                        ¿cuánto vendí?
− Costo de ventas             ¿a qué costo produje?      → MARGEN BRUTO
− Gastos operativos           ¿cuánto cuesta operar?     → RESULTADO OPERATIVO
± Resultado no operativo      ¿qué pasó fuera del giro?
− Gastos financieros          ¿cuánto cuesta mi deuda?   → RESULTADO ANTES DE IMPUESTOS
− Impuestos                                              → RESULTADO NETO
```

Un problema en el peldaño 2 (margen bruto) es estructural; uno en el peldaño 4 (gastos financieros) es
de estructura de capital. **Confundirlos lleva a la solución equivocada.**

## 📖 Desarrollo

### 1. Las dos presentaciones

**Por función:**

```text
Ingresos por ventas                    26 500 000
Costo de ventas                       −19 100 000
MARGEN BRUTO                            7 400 000
Gastos de distribución                 −2 100 000
Gastos de administración               −3 200 000
Otros ingresos operativos                 180 000
RESULTADO OPERATIVO                     2 280 000
Gastos financieros                       −640 000
RESULTADO ANTES DE IMPUESTOS            1 640 000
Impuesto a las ganancias                 −443 000
RESULTADO DEL EJERCICIO                 1 197 000
```

**Por naturaleza (mismos datos):**

```text
Ingresos por ventas                    26 500 000
Variación de existencias                 −380 000
Consumo de materias primas            −12 400 000
Gastos de personal                     −7 900 000
Depreciación y amortización            −1 350 000
Otros gastos operativos                −2 190 000
RESULTADO OPERATIVO                     2 280 000
```

La presentación por naturaleza revela algo que la funcional oculta: **el 30 % de los costos son
personal y el 5 % es depreciación**. Esa información determina el apalancamiento operativo (clase 6).

### 2. Los cinco niveles de margen

```text
margen bruto      = margen bruto / ventas            = 7 400 000/26 500 000 = 27,9 %
margen operativo  = resultado operativo / ventas     = 2 280 000/26 500 000 =  8,6 %
margen EBITDA     = (RO + D&A) / ventas              = 3 630 000/26 500 000 = 13,7 %
margen antes de impuestos = 1 640 000/26 500 000     =  6,2 %
margen neto       = 1 197 000/26 500 000             =  4,5 %
```

Diagnóstico por comparación entre niveles:

| Situación | Diagnóstico |
|---|---|
| Margen bruto cae, operativo estable | Presión de costos absorbida con menos gasto operativo |
| Margen bruto estable, operativo cae | Crecimiento del gasto de estructura |
| Margen operativo estable, neto cae | Aumento del costo financiero o de impuestos |
| Margen bruto sube y operativo cae | Posible reclasificación de costos a gastos |

### 3. Operativo, no operativo y excepcional

```text
OPERATIVO      ventas, costo de ventas, gastos de administración y distribución
NO OPERATIVO   ingresos financieros, resultado de inversiones, diferencias de cambio
EXCEPCIONAL    venta de activos fijos, indemnizaciones, deterioros extraordinarios,
               resultados de operaciones discontinuadas
```

Criterio práctico para clasificar como no recurrente:

```text
1. ¿ocurrió por una decisión ajena al giro habitual?
2. ¿es improbable que se repita en los próximos 3 años?
3. ¿su magnitud es material respecto del resultado?
si las tres son sí → no recurrente
```

### 4. Resultado normalizado

```text
Resultado del ejercicio reportado              1 197 000
(−) utilidad por venta de terreno                −850 000
(+) indemnizaciones por reestructuración          320 000
(+) deterioro extraordinario de existencias       410 000
(−) efecto tributario de los ajustes anteriores    32 000
RESULTADO NORMALIZADO                          1 045 000
```

El resultado reportado sobreestima la capacidad recurrente en **14,5 %**. Un analista proyecta desde
1 045 000, no desde 1 197 000, y esa diferencia cambia una valoración o una decisión de crédito.

### 5. Relación con los otros estados

```text
resultado del ejercicio → estado de cambios en el patrimonio (clase 5)
resultado del ejercicio → punto de partida del flujo operativo por método indirecto (clase 12)
depreciación del periodo → aumenta la depreciación acumulada del balance
provisión de incobrables → reduce las cuentas por cobrar netas del balance
```

Control obligatorio de coherencia:

```text
PN final − PN inicial = resultado + ORI + aportes − dividendos
```

Si no cuadra, hay un movimiento patrimonial no explicado, y es lo primero que un auditor pregunta.

## 🧮 Ejemplo guiado

**Situación.** Tres años de una empresa manufacturera.

| | Año 1 | Año 2 | Año 3 |
|---|---:|---:|---:|
| Ventas | 42 000 000 | 46 200 000 | 51 300 000 |
| Costo de ventas | 27 300 000 | 30 800 000 | 35 400 000 |
| Margen bruto | 14 700 000 | 15 400 000 | 15 900 000 |
| Gastos operativos | 9 800 000 | 10 900 000 | 12 600 000 |
| Resultado operativo | 4 900 000 | 4 500 000 | 3 300 000 |
| Otros ingresos | 120 000 | 180 000 | 1 900 000 |
| Gastos financieros | 780 000 | 1 040 000 | 1 380 000 |
| Resultado antes de impuestos | 4 240 000 | 3 640 000 | 3 820 000 |
| Resultado neto | 3 095 000 | 2 657 000 | 2 789 000 |

**Paso 1 — márgenes por nivel.**

| | Año 1 | Año 2 | Año 3 |
|---|---:|---:|---:|
| Margen bruto | 35,0 % | 33,3 % | 31,0 % |
| Margen operativo | 11,7 % | 9,7 % | 6,4 % |
| Margen neto | 7,4 % | 5,8 % | 5,4 % |

**Paso 2 — el hallazgo del año 3.** El resultado neto **sube** de 2 657 000 a 2 789 000 mientras el
resultado operativo **cae** de 4 500 000 a 3 300 000. La diferencia está en "otros ingresos", que pasa
de 180 000 a 1 900 000.

**Paso 3 — normaliza.**

```text
otros ingresos año 3: 1 900 000
  de los cuales 1 750 000 corresponden a la venta de una planta (no recurrente)
resultado antes de impuestos normalizado = 3 820 000 − 1 750 000 = 2 070 000
resultado neto normalizado ≈ 1 511 000  (aplicando la misma tasa efectiva)
```

| | Año 1 | Año 2 | Año 3 reportado | Año 3 normalizado |
|---|---:|---:|---:|---:|
| Resultado neto | 3 095 000 | 2 657 000 | 2 789 000 | **1 511 000** |
| Margen neto | 7,4 % | 5,8 % | 5,4 % | **2,9 %** |

**Paso 4 — diagnostica el deterioro por nivel.**

```text
margen bruto        35,0 % → 31,0 %   caída de 4,0 pp
  causa: costo de ventas crece 29,7 % con ventas creciendo 22,1 %

gastos operativos   23,3 % → 24,6 % de las ventas
  causa: gastos crecen 28,6 %, por sobre las ventas

gastos financieros   1,9 % →  2,7 % de las ventas
  causa: mayor deuda
```

Los tres niveles se deterioran simultáneamente. El único que mejora es "otros ingresos", y por una vez.

**Paso 5 — proyecta el año 4 sin la venta de la planta.**

```text
si las tendencias continúan:
  ventas         56 400 000 (+10 %)
  margen bruto    28,7 %  → 16 187 000
  gastos operativos 26,0 % → 14 664 000
  resultado operativo      →  1 523 000
  gastos financieros       → −1 700 000
  RESULTADO ANTES DE IMPUESTOS → −177 000  ← pérdida
```

**Paso 6 — la conclusión que el resultado neto ocultaba.**

```text
la empresa muestra tres años de utilidad neta positiva
su resultado OPERATIVO cayó 33 % en dos años
sin la venta de la planta, el año 3 habría mostrado un margen neto de 2,9 %
la proyección del año 4 arroja pérdida antes de impuestos

conclusión: la operación se está deteriorando y el año 3 lo ocultó con una venta de activos
```

**Interpreta:** un lector que solo mire el resultado neto ve tres años rentables con una leve
recuperación. **La descomposición en niveles y la normalización muestran lo contrario.** Esa es la
diferencia entre leer un estado de resultados y analizarlo, y es exactamente el trabajo que un
analista de crédito hace antes de aprobar (Parte 9, clase 9).

## 🏦 Del cliente al banco

| Vista de la empresa | Vista del banco | Parte |
|---|---|---|
| "Tuvimos utilidad" | ¿Operativa o por venta de activos? | 9, clase 9 |
| EBITDA como métrica | Aproximación; se verifica contra flujo real | 13, clase 3 |
| Margen bruto en caída | Deterioro estructural del negocio | 9, clase 9 |
| Gastos financieros crecientes | Mayor apalancamiento; se cruza con el balance | 13, clase 5 |
| Covenants sobre EBITDA | Definición contractual precisa | 13, clase 10 |

## 🧪 Práctica

En `labs/lab-06.md`:

1. Presenta un estado de resultados por función y por naturaleza con los mismos datos.
2. Calcula los cinco niveles de margen de tres periodos y diagnostica por nivel.
3. Construye el resultado normalizado identificando partidas no recurrentes.
4. Proyecta el periodo siguiente con las tendencias por nivel y evalúa la sostenibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se concluye desde el resultado neto | No se descompuso en niveles | Analiza margen bruto, operativo y neto por separado. |
| Se proyecta con partidas no recurrentes | No se normalizó | Elimina lo no recurrente antes de proyectar. |
| EBITDA se trata como caja | Aproximación mal entendida | EBITDA ignora capital de trabajo e inversiones. |
| Margen bruto sube y operativo cae | Posible reclasificación de costos | Compara la presentación por naturaleza. |
| Se ignora "otros ingresos" | Partida residual con montos grandes | Desagrégala: suele contener lo excepcional. |
| El patrimonio no concilia con el resultado | Movimiento no explicado | Aplica el control de conciliación. |

## ❓ Preguntas de comprobación

1. ¿Qué información revela la presentación por naturaleza que la funcional oculta?
2. Margen bruto estable y operativo en caída. ¿Qué diagnosticas?
3. ¿Qué tres condiciones definen una partida como no recurrente?
4. ¿Por qué el EBITDA no es flujo de caja?
5. ¿Cómo se concilia el resultado del ejercicio con el patrimonio?

## 📥 Entregable

Guarda en `portfolio/parte-05/clase-11/`:

- el estado de resultados en ambas presentaciones;
- los cinco márgenes de tres periodos con el diagnóstico por nivel;
- el resultado normalizado con las partidas eliminadas justificadas;
- la proyección del periodo siguiente y la evaluación de sostenibilidad.

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

- IFRS Foundation. *NIC 1 Presentación de Estados Financieros*: presentación por función y por naturaleza, resultado integral. <https://www.ifrs.org/>
- Kieso, D., Weygandt, J. y Warfield, T. (2022). *Intermediate Accounting* (18.ª ed.). Wiley. Capítulo 4: estado de resultados y partidas no recurrentes.
- Penman, S. (2013). *Financial Statement Analysis and Security Valuation* (5.ª ed.). McGraw-Hill. Capítulos 9 y 12: reformulación del estado de resultados y análisis de la rentabilidad.
- Palepu, K., Healy, P. y Peek, E. (2019). *Business Analysis and Valuation* (5.ª ed.). Cengage. Capítulo 5: análisis financiero por descomposición.
- Schilit, H., Perler, J. y Engelhart, Y. (2018). *Financial Shenanigans* (4.ª ed.). McGraw-Hill. Uso de partidas no recurrentes para gestionar el resultado.
- Verificación local: revisa si el supervisor de tu país exige un formato específico de estado de resultados o la revelación separada de partidas no recurrentes.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 10 · Estado de situación financiera](10-estado-de-situacion-financiera.md) | [Parte 05](../README.md) · [Programa](../../../SYLLABUS.md) | [12 · Estado de flujo de efectivo →](12-estado-de-flujo-de-efectivo.md) |
<!-- gen:footer:end -->
