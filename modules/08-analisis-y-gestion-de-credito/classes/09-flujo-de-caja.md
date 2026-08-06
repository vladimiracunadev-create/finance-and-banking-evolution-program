---
part: 9
class: 9
title: "Flujo de caja del deudor empresarial"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 09 · Flujo de caja del deudor empresarial

> [← 08 · Garantías](08-garantias.md) · [Índice de la parte](../README.md) · [10 · Scoring →](10-scoring.md)

**Parte 09 — Análisis y gestión de crédito** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Determinar si una empresa genera la caja necesaria para servir su deuda, que es la única pregunta que
importa en el crédito comercial. Los estados financieros muestran utilidad; **la deuda se paga con
caja**, y esta clase enseña a construir, proyectar y estresar el flujo que la sostiene.

## 📚 Objetivos

Al finalizar podrás:

1. **Construir** el flujo de caja disponible para el servicio de deuda.
2. **Calcular** e interpretar los indicadores de cobertura.
3. **Proyectar** el flujo con supuestos verificables.
4. **Estresar** la proyección y determinar el punto de quiebre.
5. **Dimensionar** el monto y el plazo que la empresa puede sostener.

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
| `EBITDA` | Aproximación del flujo operativo antes de capital de trabajo e inversión. No es caja. |
| `flujo de caja operativo` | Caja generada por la operación, después de capital de trabajo. |
| `flujo disponible para deuda` | `flujo operativo − inversión de mantenimiento − impuestos`. |
| `cobertura del servicio de deuda (DSCR)` | `flujo disponible / (intereses + amortización)`. Indicador central. |
| `cobertura de intereses` | `EBITDA / intereses`. Menos exigente que el DSCR. |
| `deuda/EBITDA` | Años de EBITDA necesarios para pagar la deuda. |
| `punto de quiebre` | Caída de ventas o margen que lleva el DSCR a 1,0. |

## 🧠 Modelo mental

La secuencia desde la utilidad hasta la caja disponible:

```text
resultado operativo
+ depreciación y amortización        → EBITDA (aproximación gruesa)
− variación de capital de trabajo    → flujo operativo real
− impuestos pagados
− inversión de MANTENIMIENTO         → flujo disponible para deuda
= lo que efectivamente puede pagar intereses y amortización
```

**La distinción entre inversión de mantenimiento y de expansión es crítica:** la de mantenimiento es
obligatoria (sin ella el negocio se deteriora); la de expansión es discrecional y puede postergarse.

## 📖 Desarrollo

### 1. Construir el flujo disponible

```text
                                      Año −2    Año −1    Año 0
Ingresos                              84 200    91 600    96 300
Resultado operativo                    9 260    10 080     9 150
+ Depreciación                         3 400     3 620     3 810
= EBITDA                              12 660    13 700    12 960
− Δ capital de trabajo                −1 840    −2 210    −3 480
= Flujo operativo                     10 820    11 490     9 480
− Impuestos pagados                   −1 980    −2 150    −1 840
− Inversión de mantenimiento          −3 200    −3 400    −3 600
= FLUJO DISPONIBLE PARA DEUDA          5 640     5 940     4 040

Servicio de deuda (intereses + amortización)  4 100   4 350   4 620
DSCR                                            1,38    1,37    0,87
```

**El deterioro del año 0 no proviene del resultado** —que cayó 9 %— sino del **capital de trabajo**,
que consumió 3 480 en lugar de 2 210. Esa es la información que el estado de resultados no muestra.

### 2. Indicadores de cobertura

| Indicador | Fórmula | Referencia mínima | Qué mide |
|---|---|---:|---|
| Cobertura de intereses | EBITDA / intereses | 2,5x | Capacidad de pagar el costo |
| DSCR | Flujo disponible / servicio total | 1,25x | Capacidad de pagar todo |
| Deuda / EBITDA | Deuda financiera neta / EBITDA | ≤ 3,5x | Tamaño relativo de la deuda |
| Flujo / deuda | Flujo disponible / deuda financiera | ≥ 15 % | Velocidad de repago |

```text
del ejemplo, año 0:
  deuda financiera neta              41 200
  intereses                           2 180
  cobertura de intereses = 12 960/2 180 = 5,95x   ✓
  DSCR = 4 040/4 620 = 0,87x                       ✗
  deuda/EBITDA = 41 200/12 960 = 3,18x             ✓
  flujo/deuda = 4 040/41 200 = 9,8 %               ✗
```

**Tres indicadores en verde y dos en rojo.** El DSCR es el vinculante, porque incluye la amortización:
la empresa puede pagar los intereses y no puede amortizar. Ese es un perfil que sobrevive refinanciando
y colapsa cuando el refinanciamiento se cierra.

### 3. Proyectar con supuestos verificables

```text
cada supuesto debe tener una fuente:
  · crecimiento de ingresos    → contratos firmados, historial, sector
  · margen                     → tendencia histórica, no aspiración
  · capital de trabajo         → días de cobro, existencias y pago históricos
  · inversión de mantenimiento → depreciación como piso, plan de inversión
  · impuestos                  → tasa efectiva histórica
```

```text
PROYECCIÓN AÑO 1
  ingresos: +4,0 % (crecimiento del sector, no del 8 % declarado por la empresa)
            96 300 × 1,04 = 100 152
  margen operativo: 9,5 % (promedio de 3 años, no el 10,5 % del mejor año)
            resultado operativo = 9 514
  depreciación: 3 950
  EBITDA = 13 464
  Δ capital de trabajo: con días históricos (cobro 78, existencias 96, pago 71)
            necesidad adicional por el crecimiento = −2 100
  flujo operativo = 11 364
  impuestos (tasa efectiva 22 %) = −2 093
  inversión de mantenimiento = −3 950 (igual a depreciación)
  FLUJO DISPONIBLE = 5 321
  
  servicio de deuda proyectado = 4 850
  DSCR proyectado = 1,10x
```

**Regla de proyección:** usar el promedio histórico, no el mejor año, y el crecimiento del sector, no
el que declara la empresa. Un analista que proyecta con los supuestos del cliente no está analizando.

### 4. Estresar y encontrar el punto de quiebre

```text
PRUEBA 1 — caída de ingresos
  ¿cuánto pueden caer los ingresos antes de que DSCR = 1,0?

  DSCR = 1,0 requiere flujo disponible = 4 850
  flujo actual proyectado = 5 321
  margen = 471

  con margen operativo de 9,5 %, cada 1 % de caída de ingresos
  reduce el flujo en aproximadamente 1 002 × 0,095 = 95
  caída tolerable = 471/95 = 4,95 %

  PUNTO DE QUIEBRE: caída de ingresos del 4,95 %
```

```text
PRUEBA 2 — compresión de margen
  cada punto de margen equivale a 1 002 de resultado operativo
  caída tolerable = 471/1 002 = 0,47 puntos de margen
  
  PUNTO DE QUIEBRE: margen de 9,03 % (vs. 9,5 % proyectado)
```

```text
PRUEBA 3 — alza de tasas
  la deuda a tasa variable es 24 000
  cada 100 pb aumenta el servicio en 240
  alza tolerable = 471/240 = 196 pb
  
  PUNTO DE QUIEBRE: +196 puntos base
```

```text
PRUEBA 4 — deterioro de cobranza
  cada día adicional de cobro consume 100 152/365 = 274
  días tolerables = 471/274 = 1,7 días
  
  PUNTO DE QUIEBRE: +1,7 días de cobro
```

**El punto de quiebre más ajustado es el de cobranza: 1,7 días.** Esa es la vulnerabilidad crítica, y
solo aparece al estresar cada variable por separado.

### 5. Dimensionar monto y plazo

```text
servicio máximo sostenible = flujo disponible / DSCR objetivo
```

```text
flujo disponible proyectado 5 321 · DSCR objetivo 1,30x
servicio máximo = 5 321/1,30 = 4 093

servicio actual comprometido = 4 850
→ la empresa YA excede su capacidad: no hay espacio para deuda adicional
→ necesita REDUCIR el servicio en 757
```

Alternativas para reducir el servicio:

| Alternativa | Efecto sobre el servicio | Condición |
|---|---:|---|
| Reperfilar a mayor plazo | −680 | Acuerdo con acreedores |
| Aporte de capital de 6 000 | −620 | Disposición de los socios |
| Reducir días de cobro de 78 a 65 | +3 560 de caja única | Gestión comercial |
| Vender activos no operativos | Variable | Existencia de activos prescindibles |

## 🧮 Ejemplo guiado

**Situación.** Una empresa constructora solicita 320 millones para capital de trabajo.

```text
                              Año −2     Año −1     Año 0
Ingresos                     1 240 000  1 480 000  1 610 000
Resultado operativo             99 200    118 400    96 600
Depreciación                    41 000     44 500    48 200
EBITDA                         140 200    162 900   144 800
Cuentas por cobrar             248 000    340 000    483 000
Existencias (obras en curso)   186 000    237 000    322 000
Cuentas por pagar              149 000    178 000    193 000
Deuda financiera neta          420 000    510 000    680 000
Intereses                       33 600     44 900    64 600
Amortización                    52 000     61 000    74 000
```

**Paso 1 — construye el capital de trabajo y su variación.**

```text
capital de trabajo = CxC + existencias − CxP
  Año −2: 248 000 + 186 000 − 149 000 = 285 000
  Año −1: 340 000 + 237 000 − 178 000 = 399 000
  Año 0:  483 000 + 322 000 − 193 000 = 612 000

Δ capital de trabajo
  Año −1: −114 000
  Año 0:  −213 000
```

**Paso 2 — flujo disponible.**

```text
                              Año −1     Año 0
EBITDA                       162 900    144 800
Δ capital de trabajo        −114 000   −213 000
Flujo operativo               48 900    −68 200
Impuestos (22 %)             −16 300    −10 600
Inversión mantenimiento      −44 500    −48 200
FLUJO DISPONIBLE             −11 900   −127 000
```

**El flujo disponible es negativo en ambos años.**

**Paso 3 — indicadores.**

```text
                              Año −1     Año 0
cobertura de intereses         3,63x      2,24x   ✓ / ⚠
DSCR                          −0,11x     −0,92x   ✗✗
deuda/EBITDA                   3,13x      4,70x   ✓ / ✗
flujo/deuda                    −2,3 %     −18,7 % ✗✗
```

**La cobertura de intereses parece aceptable y el DSCR es negativo.** La diferencia entera está en el
capital de trabajo.

**Paso 4 — diagnostica el capital de trabajo.**

```text
                              Año −2     Año −1     Año 0
días de cobro                     73         84        109
días de existencias              N/A        N/A        N/A (obras en curso)
días de pago                      44         44         44
```

```text
días de cobro: 73 → 109 en dos años (+36 días)
efecto: 36 días × 1 610 000/365 = 158 800 de caja inmovilizada adicional
```

**Paso 5 — la pregunta que define el caso.**

```text
¿por qué crecieron los días de cobro 36 días?

hipótesis A: la empresa creció aceptando clientes que pagan peor
hipótesis B: hay obras terminadas y no cobradas (estados de pago pendientes)
hipótesis C: hay cuentas incobrables no provisionadas

verificación: antigüedad de la cartera de la empresa
  0–60 días:    218 000  (45 %)
  61–120 días:  145 000  (30 %)
  121–180 días:  72 000  (15 %)
  > 180 días:    48 000  (10 %)  ← sin provisión registrada
```

**Hallazgo:** 48 000 con más de 180 días sin provisión. Si son incobrables, el patrimonio y el
resultado están sobrestimados en esa magnitud.

**Paso 6 — decisión.**

```text
RECHAZAR la operación tal como está solicitada

fundamento:
  1. flujo disponible negativo en dos años consecutivos
  2. DSCR negativo: la empresa no puede servir su deuda actual con su flujo
  3. el crecimiento de 30 % en ingresos consumió 327 000 de caja en capital de trabajo
  4. 48 000 de cartera sobre 180 días sin provisión
  5. la deuda creció 260 000 en dos años para financiar capital de trabajo,
     no inversión productiva

DIAGNÓSTICO
  la empresa no tiene un problema de financiamiento: tiene un problema de
  CICLO DE CONVERSIÓN DE EFECTIVO. Cada peso adicional de venta consume
  0,20 pesos de caja, y ese consumo se está financiando con deuda.

  crecer más agrava el problema.

ALTERNATIVA CONSTRUCTIVA
  operación estructurada de factoring sobre los estados de pago:
    · anticipa 218 000 de cartera de 0–60 días
    · no aumenta la deuda: convierte cartera en caja
    · reduce los días de cobro de 109 a ~65
    · libera 195 000 de capital de trabajo

  CONDICIONES
    · provisionar los 48 000 de cartera sobre 180 días
    · política de crédito a clientes con límites y plazos
    · suspender el crecimiento hasta normalizar el ciclo
    · reperfilar la deuda existente a mayor plazo
```

**Interpreta:** la empresa crecía 30 % y **su flujo disponible era negativo**. El estado de resultados
mostraba utilidad; el flujo mostraba que ese crecimiento se financiaba con deuda. La solución correcta
no era prestar más: era **convertir la cartera en caja y detener el crecimiento** hasta normalizar el
ciclo.

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| "Tenemos utilidad y crecemos" | ¿La utilidad se convierte en caja? | 5, clase 12 |
| Necesidad de capital de trabajo | Puede ser síntoma de un ciclo deteriorado | 13, clase 2 |
| Cobertura de intereses aceptable | El DSCR incluye la amortización | 13, clase 10 |
| Solicitud de más crédito | Puede agravar el problema | 9, clase 15 |
| Factoring ofrecido | Convierte activo en caja sin aumentar deuda | 13, clase 9 |

## 🧪 Práctica

En `labs/lab-05.md`:

1. Construye el flujo disponible para deuda de tres empresas a partir de sus estados.
2. Calcula los cuatro indicadores de cobertura e identifica cuál es vinculante.
3. Proyecta el flujo con supuestos verificables y documenta la fuente de cada uno.
4. Encuentra los cuatro puntos de quiebre y determina la vulnerabilidad crítica.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se usa el EBITDA como flujo | Capital de trabajo e inversión omitidos | Construye el flujo disponible completo. |
| Se proyecta con los supuestos del cliente | Sin verificación independiente | Usa promedios históricos y datos del sector. |
| Se mira solo la cobertura de intereses | La amortización se ignora | El DSCR es el indicador vinculante. |
| No se estresa la proyección | Escenario único | Encuentra los puntos de quiebre. |
| Se presta para financiar capital de trabajo creciente | Síntoma tratado, no la causa | Diagnostica el ciclo de conversión. |
| No se revisa la antigüedad de la cartera | Incobrables ocultos | Solicita el detalle por tramo. |

## ❓ Preguntas de comprobación

1. ¿Por qué el EBITDA no es el flujo disponible para deuda?
2. ¿Qué diferencia hay entre inversión de mantenimiento y de expansión, y cuál se descuenta?
3. Calcula el punto de quiebre de ingresos con un DSCR de 1,15 y margen de 8 %.
4. ¿Por qué la cobertura de intereses puede estar bien y el DSCR mal?
5. Una empresa crece 30 % y su flujo es negativo. ¿Cuál es tu diagnóstico?

## 📥 Entregable

Guarda en `portfolio/parte-09/clase-09/`:

- el flujo disponible para deuda de tres empresas construido paso a paso;
- los cuatro indicadores con la identificación del vinculante;
- la proyección con la fuente documentada de cada supuesto;
- los cuatro puntos de quiebre con la vulnerabilidad crítica identificada.

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

- Higgins, R. (2019). *Analysis for Financial Management* (12.ª ed.). McGraw-Hill. Capítulo 6: capacidad de endeudamiento y flujo de caja.
- Caouette, J., Altman, E., Narayanan, P. y Nimmo, R. (2008). *Managing Credit Risk* (2.ª ed.). Wiley. Análisis de flujo del deudor corporativo.
- Penman, S. (2013). *Financial Statement Analysis and Security Valuation* (5.ª ed.). McGraw-Hill. Reformulación del flujo de efectivo.
- European Banking Authority (2020). *Guidelines on loan origination and monitoring*. EBA. Análisis de capacidad de pago de empresas.
- Damodaran, A. (2012). *Investment Valuation* (3.ª ed.). Wiley. Definición de flujo de caja libre y de inversión de mantenimiento.
- Verificación local: usa estados financieros publicados de empresas de tu país para practicar la construcción del flujo disponible.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 08 · Garantías](08-garantias.md) | [Parte 09](../README.md) · [Programa](../../../SYLLABUS.md) | [10 · Scoring →](10-scoring.md) |
<!-- gen:footer:end -->
