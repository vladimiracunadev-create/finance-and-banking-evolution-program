---
part: 5
class: 12
title: "Estado de flujo de efectivo"
level: intermedio
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 12 · Estado de flujo de efectivo

> [← 11 · Estado de resultados](11-estado-de-resultados.md) · [Índice de la parte](../README.md) · [13 · Depreciaciones y provisiones →](13-depreciaciones-y-provisiones.md)

**Parte 05 — Contabilidad financiera** · **Nivel:** Intermedio — requiere las partes anteriores · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Dominar el estado que un analista de crédito lee primero, porque es el más difícil de manipular: el
que muestra de dónde vino y a dónde fue el efectivo. Utilidad e ingresos dependen de estimaciones; el
efectivo, no. Esta clase enseña a construirlo, a leerlo por combinación de signos y a detectar
empresas que crecen consumiendo caja.

## 📚 Objetivos

Al finalizar podrás:

1. **Construir** el flujo operativo por el método indirecto desde el resultado.
2. **Clasificar** correctamente cada flujo en operación, inversión y financiamiento.
3. **Interpretar** las ocho combinaciones de signos y su diagnóstico.
4. **Calcular** el flujo de caja libre y su relación con el servicio de la deuda.
5. **Detectar** divergencias persistentes entre resultado y flujo operativo.

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
| `flujo operativo` | Efectivo generado o consumido por el giro. Es el indicador de sostenibilidad. |
| `flujo de inversión` | Compra y venta de activos de largo plazo. Negativo indica crecimiento o reposición. |
| `flujo de financiamiento` | Aportes, dividendos, obtención y pago de deuda. |
| `método indirecto` | Parte del resultado y ajusta partidas sin efecto en efectivo y variaciones de capital de trabajo. |
| `método directo` | Muestra cobros y pagos brutos. Más informativo, menos usado. |
| `flujo de caja libre` | `flujo operativo − inversión en activos fijos`. Efectivo disponible para acreedores y dueños. |
| `calidad del resultado` | `flujo operativo / resultado neto`. Sostenidamente bajo 1 exige explicación. |

## 🧠 Modelo mental

Los tres flujos responden tres preguntas y su **combinación de signos cuenta una historia**:

```text
operación    ¿el negocio genera caja por sí mismo?
inversión    ¿estoy creciendo, manteniendo o vendiendo activos?
financiamiento ¿estoy captando o devolviendo capital y deuda?
```

Una empresa madura y sana muestra habitualmente `(+, −, −)`: genera caja, invierte y devuelve capital.
Una que muestra `(−, −, +)` está financiando con deuda tanto su operación como su crecimiento, y eso
tiene un límite.

## 📖 Desarrollo

### 1. Método indirecto, paso a paso

```text
Resultado del ejercicio                                   1 197 000
(+) Depreciación y amortización                           1 350 000
(+) Deterioro de activos                                    410 000
(−) Utilidad por venta de activo fijo                      −850 000
(+) Gastos financieros                                      640 000
(+/−) Variaciones de capital de trabajo:
      (−) Aumento de cuentas por cobrar                    −620 000
      (−) Aumento de existencias                         −1 100 000
      (+) Aumento de cuentas por pagar                      480 000
(−) Impuestos pagados                                      −390 000
(−) Intereses pagados                                      −640 000
FLUJO OPERATIVO                                            −477 000
```

Tres reglas que hay que entender, no memorizar:

```text
1. se SUMAN las partidas que redujeron el resultado sin salida de efectivo
   (depreciación, deterioro, provisiones)
2. se RESTAN las utilidades sin entrada de efectivo o que pertenecen a otra sección
   (utilidad por venta de activos: su efectivo va a inversión)
3. un AUMENTO de un activo corriente CONSUME efectivo; un aumento de un pasivo lo GENERA
```

La regla 3 es la que explica por qué una empresa que crece consume caja: al crecer aumentan las
cuentas por cobrar y las existencias, y ambas son salidas de efectivo.

### 2. Clasificación de flujos

| Concepto | Sección |
|---|---|
| Cobros a clientes, pagos a proveedores y personal | Operación |
| Intereses pagados | Operación o financiamiento (política declarada) |
| Impuestos pagados | Operación, salvo asociación específica |
| Compra de propiedades y equipos | Inversión |
| Venta de activos fijos (el efectivo recibido) | Inversión |
| Compra de participaciones en otras empresas | Inversión |
| Obtención y pago de préstamos | Financiamiento |
| Aportes de capital y dividendos pagados | Financiamiento |
| Pago del principal de arrendamientos | Financiamiento |

La clasificación de intereses admite alternativas bajo NIIF y **debe ser consistente entre periodos**;
cambiarla altera el flujo operativo sin que cambie nada real.

### 3. Las ocho combinaciones

| Op | Inv | Fin | Diagnóstico típico |
|:--:|:--:|:--:|---|
| + | − | − | **Madura y sana**: genera caja, invierte y devuelve capital |
| + | − | + | **En crecimiento**: genera caja e invierte más de lo que genera, con deuda |
| + | + | − | **Desinvirtiendo**: vende activos y devuelve capital; puede ser reestructuración |
| + | + | + | Acumula caja de todas las fuentes; posible preparación de una operación mayor |
| − | − | + | **Alerta**: la operación no genera caja y todo se financia con deuda |
| − | + | + | **Alerta severa**: vende activos y se endeuda para sostener la operación |
| − | + | − | Vende activos para pagar deuda; contracción |
| − | − | − | **Insostenible**: consume caja acumulada en todos los frentes |

Las filas 5 y 6 son las que un analista de crédito marca de inmediato: **una operación que no genera
caja financiada con deuda tiene un horizonte finito y calculable**.

### 4. Flujo de caja libre y servicio de la deuda

```text
flujo de caja libre = flujo operativo − inversión en activos fijos de mantenimiento

cobertura del servicio de deuda = flujo operativo / (intereses + amortización de capital)
```

| Cobertura | Lectura |
|---|---|
| > 1,5 | Holgada |
| 1,2–1,5 | Adecuada |
| 1,0–1,2 | Ajustada; sin margen ante un imprevisto |
| < 1,0 | **La operación no cubre el servicio de la deuda** |

Este es el indicador que aparece como covenant en la mayoría de los contratos de crédito comercial
(Parte 13, clase 10).

### 5. Calidad del resultado

```text
calidad del resultado = flujo operativo / resultado neto
```

| Valor | Lectura |
|---|---|
| > 1,2 | El resultado subestima la generación de caja |
| 0,8–1,2 | Coherente |
| 0,3–0,8 | El resultado se convierte parcialmente en caja: investigar |
| < 0,3 o negativo | **Divergencia severa**: prioridad de análisis |

Una divergencia puntual puede explicarse por un año de crecimiento fuerte. **Tres años consecutivos de
divergencia exigen una explicación estructural**, y las hipótesis son las de la clase 6:
reconocimiento agresivo, cobranza deteriorada o costos diferidos.

## 🧮 Ejemplo guiado

**Situación.** Reconstruye el flujo de efectivo de una empresa a partir de sus estados.

```text
BALANCE                          Año 1        Año 2      Variación
Efectivo                        820 000    1 240 000     +420 000
Cuentas por cobrar            4 200 000    6 100 000   +1 900 000
Existencias                   3 800 000    5 200 000   +1 400 000
Propiedades y equipos (bruto)10 000 000   13 500 000   +3 500 000
Depreciación acumulada       −3 200 000   −4 400 000   −1 200 000
Cuentas por pagar             2 900 000    3 800 000     +900 000
Préstamos                     5 000 000    8 200 000   +3 200 000
Capital                       6 000 000    6 000 000            0
Resultados acumulados         1 720 000    3 640 000   +1 920 000

RESULTADOS Año 2
Resultado del ejercicio       2 420 000
Depreciación del periodo      1 200 000
Dividendos pagados              500 000
```

**Paso 1 — flujo operativo (método indirecto).**

```text
Resultado del ejercicio                        2 420 000
(+) Depreciación                               1 200 000
(−) Aumento de cuentas por cobrar             −1 900 000
(−) Aumento de existencias                    −1 400 000
(+) Aumento de cuentas por pagar                 900 000
FLUJO OPERATIVO                                1 220 000
```

**Paso 2 — flujo de inversión.**

```text
compra de propiedades y equipos = variación bruta = −3 500 000
FLUJO DE INVERSIÓN                            −3 500 000
```

**Paso 3 — flujo de financiamiento.**

```text
aumento de préstamos                           3 200 000
dividendos pagados                              −500 000
FLUJO DE FINANCIAMIENTO                        2 700 000
```

**Paso 4 — verifica.**

```text
1 220 000 − 3 500 000 + 2 700 000 = 420 000
variación de efectivo del balance = 420 000  ✔
```

**Paso 5 — diagnóstico por combinación de signos.**

```text
(+, −, +)  → empresa en crecimiento financiado con deuda
```

**Paso 6 — los indicadores que matizan el diagnóstico.**

```text
calidad del resultado = 1 220 000 / 2 420 000 = 0,50   → divergencia relevante
flujo de caja libre   = 1 220 000 − 3 500 000 = −2 280 000
cobertura del servicio (intereses ~490 000 + amortización 0) = 2,49  → holgada por ahora

capital de trabajo consumido = 1 900 000 + 1 400 000 − 900 000 = 2 400 000
sobre ventas (supuestas 28 000 000, +18 %) → el crecimiento consumió 2,4 M de caja
```

**Paso 7 — la pregunta que decide.**

```text
la empresa creció, invirtió 3,5 M y se endeudó 3,2 M
su operación generó 1,22 M, la mitad de su resultado
si el crecimiento continúa al mismo ritmo:
  año 3: consumo de capital de trabajo ≈ 2 800 000
         inversión requerida ≈ 3 000 000
         flujo operativo estimado ≈ 1 500 000
         necesidad de financiamiento ≈ 4 300 000
  deuda pasaría de 8,2 M a 12,5 M sobre un patrimonio de ~5,6 M → apalancamiento 2,2
```

**Interpreta:** el crecimiento es real y está mal financiado. La empresa necesita **capital, no más
deuda**, o bien reducir el ciclo de conversión de efectivo. El estado de resultados mostraba una
empresa cada vez más rentable; el flujo de efectivo muestra que ese crecimiento consume más caja de la
que produce. **Ambas cosas son ciertas y solo la segunda determina si sobrevive.**

## 🏦 Del cliente al banco

| Vista de la empresa | Vista del banco | Parte |
|---|---|---|
| "Crecimos y somos rentables" | ¿El flujo operativo cubre el servicio de la deuda? | 9, clase 9 |
| Flujo operativo negativo | Alerta prioritaria en la evaluación | 9, clase 9 |
| Alta inversión | ¿De mantenimiento o de expansión? | 13, clase 4 |
| Calidad del resultado baja | Se investiga cobranza y reconocimiento | 9, clase 9 |
| Cobertura del servicio | Covenant habitual en crédito comercial | 13, clase 10 |

## 🧪 Práctica

En `labs/lab-06.md`, sección de flujo:

1. Construye el flujo de efectivo por método indirecto desde dos balances y un estado de resultados.
2. Verifica que la variación de efectivo calculada coincida con la del balance.
3. Diagnostica la combinación de signos de cinco empresas reales.
4. Calcula calidad del resultado y cobertura del servicio de deuda de tres periodos.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| El flujo no cuadra con la variación de efectivo | Falta una partida o hay doble conteo | Verifica siempre contra el balance. |
| La depreciación se trata como entrada de caja | Interpretación incorrecta | Se suma porque redujo el resultado sin salida de efectivo. |
| La venta de un activo se deja en operación | Clasificación incorrecta | El efectivo recibido va a inversión. |
| Se concluye desde el flujo total | Los tres flujos dicen cosas distintas | Analiza la combinación de signos. |
| Se ignora el consumo de capital de trabajo | Solo se miró el resultado | El crecimiento consume caja: cuantifícalo. |
| Se cambia la clasificación de intereses entre periodos | Inconsistencia | Mantén la política y decláralo. |

## ❓ Preguntas de comprobación

1. ¿Por qué se suma la depreciación en el método indirecto?
2. ¿Por qué un aumento de existencias consume efectivo?
3. Interpreta la combinación `(−, +, +)` y explica su urgencia.
4. ¿Cómo se calcula la calidad del resultado y qué valor exige investigación?
5. ¿Por qué el estado de flujo de efectivo es más difícil de manipular que el de resultados?

## 📥 Entregable

Guarda en `portfolio/parte-05/clase-12/`:

- el flujo de efectivo construido por método indirecto, con la verificación contra el balance;
- el diagnóstico por combinación de signos de cinco empresas;
- el cálculo de calidad del resultado y cobertura del servicio de deuda;
- una conclusión de 300 palabras sobre la sostenibilidad del caso analizado.

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

- IFRS Foundation. *NIC 7 Estado de Flujos de Efectivo*. Clasificación, métodos directo e indirecto. <https://www.ifrs.org/>
- Kieso, D., Weygandt, J. y Warfield, T. (2022). *Intermediate Accounting* (18.ª ed.). Wiley. Capítulo 23: preparación e interpretación del flujo de efectivo.
- Penman, S. (2013). *Financial Statement Analysis and Security Valuation* (5.ª ed.). McGraw-Hill. Capítulo 10: reformulación del flujo de efectivo para el análisis.
- Higgins, R. (2019). *Analysis for Financial Management* (12.ª ed.). McGraw-Hill. Capítulo 1: los tres flujos y su interpretación conjunta.
- Mulford, C. y Comiskey, E. (2005). *Creative Cash Flow Reporting*. Wiley. Técnicas de presentación del flujo y su detección.
- Verificación local: revisa si el supervisor de tu país exige el método directo o admite el indirecto, y cómo debe clasificarse el pago de intereses.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 11 · Estado de resultados](11-estado-de-resultados.md) | [Parte 05](../README.md) · [Programa](../../../SYLLABUS.md) | [13 · Depreciaciones y provisiones →](13-depreciaciones-y-provisiones.md) |
<!-- gen:footer:end -->
