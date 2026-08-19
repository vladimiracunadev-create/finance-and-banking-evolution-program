<!-- meta
part: 7
class: 7
title: "Sistemas de amortización"
level: avanzado
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 07 · Sistemas de amortización

> [← 06 · Perpetuidades](06-perpetuidades.md) · [Índice de la parte](../README.md) · [08 · Valor actual neto →](08-valor-actual-neto.md)

**Parte 07 — Matemática financiera avanzada** · **Nivel:** Avanzado — perfil analista · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Profundizar los sistemas de amortización de la Parte 1, clase 12, con las variantes que aparecen en
operaciones profesionales: cuotas variables, amortización con reajuste, sistemas mixtos y estructuras
con prepago. Esta clase entrega el criterio de estructuración y las tablas completas de cada sistema.

La Parte 3 comparó tres sistemas de amortización con cifras. Esta los generaliza, añade dos más y plantea la pregunta profesional: no cuál es más barato, sino cuál encaja con el flujo de caja del deudor, porque un sistema barato con cuotas que el deudor no puede pagar termina en incumplimiento.

## 📚 Objetivos

Al finalizar podrás:

1. **Construir** las tablas de los cinco sistemas de amortización principales.
2. **Comparar** su costo total, su perfil de cuota y su duración.
3. **Estructurar** un crédito según el perfil de flujo del deudor.
4. **Modelar** prepagos y su efecto sobre plazo y costo.
5. **Analizar** el comportamiento del saldo insoluto en cada sistema.

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

Los cinco primeros términos son sistemas y el sexto, la medida que los compara con una sola cifra. La **duración del crédito** es esa medida: resume en un número cuándo se recupera el capital en promedio, y permite comparar sistemas que tienen calendarios muy distintos.

| Concepto | Comprensión verificable |
|---|---|
| `sistema francés` | Cuota constante. Amortización creciente, interés decreciente. |
| `sistema alemán` | Amortización constante. Cuota decreciente. |
| `sistema americano` | Solo interés; capital al vencimiento. |
| `sistema de cuota creciente` | La cuota crece a tasa `g`. Alinea el pago con el crecimiento esperado del ingreso. |
| `fondo de amortización (sinking fund)` | Se pagan intereses y se acumula el capital en un fondo paralelo. |
| `duración del crédito` | Plazo promedio ponderado de recuperación del capital. Difiere entre sistemas. |
| `prepago` | Pago extraordinario a capital. Su efecto depende del sistema y del momento. |

## 🧠 Modelo mental

Todos los sistemas amortizan el mismo capital y **difieren en la velocidad**:

```text
velocidad de amortización:  alemán > francés > cuota creciente > americano
costo total de intereses:   alemán < francés < cuota creciente < americano
exigencia inicial de caja:  alemán > francés > cuota creciente > americano
```

Elegir sistema es decidir **dónde poner el esfuerzo en el tiempo**, y el costo total es la
consecuencia aritmética de esa decisión, no un objetivo independiente.

## 📖 Desarrollo

### 1. Los cinco sistemas sobre un mismo caso

Capital 30 000 000, tasa 1,2 % mensual, 24 periodos.

**Francés — cuota constante:**

```text
(1,012)^24 = 1,330872
cuota = 30 000 000 × 0,012 × 1,330872/0,330872 = 1 448 297
```

| Periodo | Saldo inicial | Cuota | Interés | Amortización |
|---:|---:|---:|---:|---:|
| 1 | 30 000 000 | 1 448 297 | 360 000 | 1 088 297 |
| 12 | 16 993 000 | 1 448 297 | 203 916 | 1 244 381 |
| 24 | 1 431 122 | 1 448 297 | 17 173 | 1 431 124 |
| | **Interés total** | | **4 759 128** | |

**Alemán — amortización constante de 1 250 000:**

| Periodo | Saldo inicial | Cuota | Interés | Amortización |
|---:|---:|---:|---:|---:|
| 1 | 30 000 000 | 1 610 000 | 360 000 | 1 250 000 |
| 12 | 16 250 000 | 1 445 000 | 195 000 | 1 250 000 |
| 24 | 1 250 000 | 1 265 000 | 15 000 | 1 250 000 |
| | **Interés total** | | **4 500 000** | |

**Americano — solo interés de 360 000, capital al final:**

```text
interés total = 360 000 × 24 = 8 640 000
```

**Cuota creciente al 1 % mensual:**

```text
VP = A × [1 − ((1+g)/(1+i))^n]/(i − g)
30 000 000 = A × [1 − (1,01/1,012)^24]/(0,012 − 0,01)
(1,01/1,012)^24 = (0,998024)^24 = 0,953675
30 000 000 = A × 0,046325/0,002 = A × 23,1625
A = 1 295 197 (primera cuota)
última cuota = 1 295 197 × (1,01)^23 = 1 626 258
interés total ≈ 4 950 000
```

**Fondo de amortización — interés al acreedor, capital acumulado al 0,8 % mensual:**

```text
interés pagado = 360 000 × 24 = 8 640 000
aporte al fondo = 30 000 000 × 0,008/((1,008)^24 − 1) = 30 000 000 × 0,008/0,210599 = 1 139 604
desembolso total = (360 000 + 1 139 604) × 24 = 35 990 496
costo neto = 5 990 496
```

### 2. Comparación

Los cinco sistemas se comparan sobre el mismo capital y plazo, que es la única forma de ver la diferencia. La tabla los enfrenta.

| Sistema | Primera cuota | Última cuota | Interés total | Sobre francés |
|---|---:|---:|---:|---:|
| Alemán | 1 610 000 | 1 265 000 | 4 500 000 | −5,4 % |
| Francés | 1 448 297 | 1 448 297 | 4 759 128 | — |
| Cuota creciente | 1 295 197 | 1 626 258 | 4 950 000 | +4,0 % |
| Fondo de amortización | 1 499 604 | 1 499 604 | 5 990 496 | +25,9 % |
| Americano | 360 000 | 30 360 000 | 8 640 000 | +81,5 % |

### 3. Duración del crédito

La duración mide el plazo promedio ponderado de recuperación:

```text
D = Σ [t × VP(flujo_t)] / Σ VP(flujo_t)
```

| Sistema | Duración (periodos) | Interpretación |
|---|---:|---|
| Alemán | 8,42 | Recupera antes |
| Francés | 8,79 | Intermedio |
| Cuota creciente | 9,31 | Recupera más tarde |
| Americano | 22,64 | Casi todo al final |

Para el banco, **la duración determina el riesgo de tasa** (clase 11) y la exposición al riesgo de
crédito en el tiempo. Un crédito americano mantiene la exposición máxima durante todo el plazo.

### 4. Estructurar según el flujo del deudor

El sistema se elige a partir del perfil de ingresos del deudor y no de su costo total. La tabla los relaciona.

| Perfil del deudor | Sistema recomendable | Razón |
|---|---|---|
| Ingreso estable y alto hoy | Alemán | Menor costo, capacidad presente |
| Ingreso estable, prioriza predecibilidad | Francés | Cuota constante |
| Ingreso creciente (profesional joven, empresa en expansión) | Cuota creciente | Alinea cuota con capacidad |
| Proyecto que genera caja al final | Americano con garantía | Alinea pago con generación |
| Empresa con obligación de acumular fondos | Fondo de amortización | Usado en emisiones de bonos |
| Ingreso estacional | Cuotas variables por temporada | Evita mora en meses bajos |

### 5. Modelar prepagos

Un prepago de 5 000 000 en el periodo 8, en cada sistema:

| Sistema | Saldo antes | Efecto si mantiene cuota | Intereses ahorrados |
|---|---:|---|---:|
| Francés | 20 738 000 | Plazo baja de 24 a 19,7 | 720 400 |
| Alemán | 21 250 000 | Plazo baja de 24 a 20,0 | 690 000 |
| Americano | 30 000 000 | Interés baja a 300 000/periodo | 960 000 |

**El prepago ahorra más en el sistema americano** porque el capital pendiente es mayor durante todo el
plazo restante. Y ahorra más cuanto antes se haga, en cualquier sistema (Parte 1, clase 11).

Dos modalidades, que deben elegirse explícitamente:

```text
reducción de PLAZO   mantiene la cuota, acorta el crédito → maximiza el ahorro
reducción de CUOTA   mantiene el plazo, baja la cuota    → alivia el flujo, ahorra menos
```

## 🧮 Ejemplo guiado

El ejemplo amortiza el mismo capital por los cinco sistemas y calcula la duración de cada uno. Conviene mirar la duración junto al costo total: son dos criterios distintos y no coinciden.

**Situación.** Estructura el financiamiento de un proyecto de energía con este perfil de generación de
caja.

```text
inversión requerida                    180 000 millones
tasa disponible                        0,95 % mensual
plazo máximo                           96 meses (8 años)

generación de caja proyectada:
  meses 1–18    construcción, sin ingresos
  meses 19–42   operación parcial, EBITDA 2 800 millones/mes
  meses 43–96   operación plena, EBITDA 5 400 millones/mes
```

**Paso 1 — evalúa el sistema francés puro.**

```text
(1,0095)^96 = 2,470512
cuota = 180 000 × 0,0095 × 2,470512/1,470512 = 180 000 × 0,015960 = 2 872 800

problema: durante los meses 1–18 no hay ingresos
          → requeriría 51 710 millones de capital de trabajo adicional
```

**Paso 2 — incorpora gracia total durante la construcción.**

```text
saldo al mes 18 = 180 000 × (1,0095)^18 = 180 000 × 1,185545 = 213 398

cuota para 78 meses restantes:
(1,0095)^78 = 2,082464
cuota = 213 398 × 0,0095 × 2,082464/1,082464 = 213 398 × 0,018277 = 3 900 245

problema: en los meses 19–42 el EBITDA es 2 800 < 3 900
          → cobertura de 0,72 veces: INSUFICIENTE
```

**Paso 3 — estructura en dos tramos alineados con la generación.**

```text
tramo 1 (meses 19–42, 24 cuotas): cuota A, con cobertura objetivo de 1,30
  A máxima = 2 800/1,30 = 2 154 millones

tramo 2 (meses 43–96, 54 cuotas): cuota B, con cobertura objetivo de 1,40
  B máxima = 5 400/1,40 = 3 857 millones
```

**Paso 4 — verifica que la estructura amortiza el capital.**

```text
valor presente en el mes 18 de ambos tramos:

a(24; 0,95%) = [1 − (1,0095)^-24]/0,0095
(1,0095)^24 = 1,255086 → (1,0095)^-24 = 0,796758
a(24) = 21,3939

a(54; 0,95%) = [1 − (1,0095)^-54]/0,0095
(1,0095)^54 = 1,664952 → (1,0095)^-54 = 0,600618
a(54) = 42,0402

VP tramo 1 = 2 154 × 21,3939 = 46 082
VP tramo 2 = 3 857 × 42,0402 × 0,796758 = 3 857 × 33,4959 = 129 194
VP total = 175 276

necesario: 213 398
DÉFICIT: 38 122 millones
```

**Paso 5 — ajusta la estructura.**

Opciones:

| Opción | Efecto |
|---|---|
| Extender el plazo a 120 meses | Aumenta la capacidad en ~28 000; aún insuficiente |
| Reducir la gracia a parcial (pagar intereses) | Saldo al mes 18 = 180 000; capacidad requerida cae 33 398 |
| Aportar más capital propio | Reduce el monto financiado |
| Cuota balón al vencimiento | Concentra el riesgo de refinanciamiento |

**Estructura recomendada — gracia parcial:**

```text
meses 1–18: pagar solo intereses = 180 000 × 0,0095 = 1 710 millones/mes
            (financiado con capital de trabajo del proyecto: 30 780 millones)
saldo al mes 18 = 180 000 (sin capitalizar)

VP requerido = 180 000
VP disponible con las cuotas máximas = 175 276
déficit = 4 724 → se cubre extendiendo el tramo 2 a 60 meses
```

**Paso 6 — estructura final y verificación.**

```text
meses 1–18    solo intereses: 1 710 millones/mes
meses 19–42   24 cuotas de 2 154 millones    (cobertura 1,30)
meses 43–102  60 cuotas de 3 857 millones    (cobertura 1,40)

verificación del valor presente:
  VP = 30 780 (intereses de gracia, ya pagados) 
  a(60; 0,95%) = 45,4218
  VP tramo 2 = 3 857 × 45,4218 × 0,796758 = 139 585
  VP tramo 1 = 46 082
  total = 185 667 ≥ 180 000  ✔ con margen
```

**Interpreta:** el sistema francés estándar era inviable, no por el costo sino **por el desalineamiento
entre la cuota y la generación de caja**. La estructura correcta no minimiza el interés total: maximiza
la probabilidad de que el crédito se pague. Ese criterio —viabilidad antes que costo— es el que rige
en financiamiento de proyectos (Parte 13, clase 4).

## 🏦 Del cliente al banco

El cliente elige una cuota y el banco estructura según el riesgo y la duración. La tabla enfrenta las dos lecturas.

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| Elección de sistema | Estructuración de operaciones | 13, clase 4 |
| Cobertura del servicio de deuda | Criterio de viabilidad y covenant | 13, clase 10 |
| Duración del crédito | Riesgo de tasa y exposición | 11, clase 5 |
| Prepago | Riesgo de prepago en la gestión de activos | 11, clase 5 |
| Gracia parcial vs. total | Efecto sobre el capital y sobre el riesgo | 1, clase 12 |

## 🧪 Práctica

El laboratorio pide estructurar un crédito para tres perfiles de flujo distintos y justificar el sistema elegido. La justificación es lo que se evalúa.

En `labs/lab-04.md`:

1. Construye las tablas completas de los cinco sistemas para un mismo crédito.
2. Calcula la duración de cada sistema y explica las diferencias.
3. Modela prepagos en tres momentos y en dos modalidades para cada sistema.
4. Estructura un financiamiento de proyecto alineado con un perfil de generación de caja.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen créditos que incumplen pese a estar bien calculados. La causa es un sistema que no encajaba con el flujo del deudor.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se elige el sistema por el interés total | Viabilidad ignorada | Verifica la cobertura periodo a periodo. |
| La gracia total sorprende con mayor deuda | Capitalización no comprendida | En gracia total el saldo crece. |
| El valor presente de las cuotas no cubre el capital | Estructura mal dimensionada | Verifica siempre con valor presente. |
| Se supone que el prepago ahorra lo mismo en todos los sistemas | Saldo pendiente distinto | Ahorra más donde el saldo es mayor. |
| No se elige la modalidad de prepago | Reducción por defecto del acreedor | Solicita por escrito reducción de plazo. |
| Se ignora la duración | Riesgo de tasa no medido | Calcula la duración de cada estructura. |

## ❓ Preguntas de comprobación

1. Ordena los cinco sistemas por interés total y explica el orden.
2. ¿Por qué el sistema americano tiene la mayor duración?
3. ¿En qué sistema un prepago ahorra más y por qué?
4. ¿Cómo verificas que una estructura de cuotas amortiza el capital?
5. ¿Por qué en financiamiento de proyectos la viabilidad manda sobre el costo?

## 📥 Entregable

Guarda en `portfolio/parte-07/clase-07/`:

- las cinco tablas de amortización completas de un mismo crédito;
- el cálculo de duración de cada sistema con su interpretación;
- los prepagos modelados en tres momentos y dos modalidades;
- la estructuración de un financiamiento de proyecto con verificación por valor presente.

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

- Kellison, S. (2008). *The Theory of Interest* (3.ª ed.). McGraw-Hill/Irwin. Capítulos 6 y 7: amortización y fondos de amortización.
- Broverman, S. (2017). *Mathematics of Investment and Credit* (7.ª ed.). ACTEX. Capítulo 3: sistemas de amortización comparados.
- Yescombe, E. (2013). *Principles of Project Finance* (2.ª ed.). Academic Press. Estructuración de deuda alineada con generación de caja.
- Ross, S., Westerfield, R. y Jaffe, J. (2021). *Corporate Finance* (12.ª ed.). McGraw-Hill. Capítulo 25: estructuras de deuda.
- Basel Committee on Banking Supervision (2017). *Prudential treatment of problem assets — definitions of non-performing exposures and forbearance*. BIS. Tratamiento de estructuras con gracia.
- Verificación local: revisa qué sistemas de amortización admite tu normativa y qué información debe entregarse sobre periodos de gracia.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 06 · Perpetuidades](06-perpetuidades.md) | [Parte 07](../README.md) · [Programa](../../../SYLLABUS.md) | [08 · Valor actual neto →](08-valor-actual-neto.md) |
<!-- gen:footer:end -->
