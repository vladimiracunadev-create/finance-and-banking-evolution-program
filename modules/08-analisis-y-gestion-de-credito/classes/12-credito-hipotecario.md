---
part: 9
class: 12
title: "Crédito hipotecario"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 12 · Crédito hipotecario

> [← 11 · Crédito de consumo](11-credito-de-consumo.md) · [Índice de la parte](../README.md) · [13 · Crédito comercial y pyme →](13-credito-comercial-y-pyme.md)

**Parte 09 — Análisis y gestión de crédito** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Evaluar la operación de mayor monto, mayor plazo y menor pérdida esperada de la banca minorista. El
hipotecario combina una garantía sólida con un horizonte de veinte a treinta años, lo que traslada el
foco desde la probabilidad de incumplimiento hacia la **sostenibilidad de la capacidad de pago en el
tiempo** y hacia la calidad de la garantía.

El crédito de consumo de la clase anterior dura meses. Este dura veinte años, y esa diferencia cambia todo: la evaluación tiene que proyectar la capacidad de pago a lo largo de una vida laboral, y la garantía tiene que valorarse sabiendo que el mercado inmobiliario también tiene ciclos.

## 📚 Objetivos

Al finalizar podrás:

1. **Estructurar** la evaluación hipotecaria con sus variables específicas.
2. **Calcular** y aplicar la relación préstamo/valor y sus límites.
3. **Evaluar** la garantía con criterio de liquidación y de evolución del mercado.
4. **Proyectar** la capacidad de pago en un horizonte de veinte años.
5. **Aplicar** los mitigantes propios del producto.

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

Los tres primeros términos son la estructura de la operación; los cuatro siguientes, los riesgos propios del plazo largo y de la unidad de cuenta. El **riesgo de reajuste** es el que menos se explica al cliente y más problemas causa: la cuota expresada en una unidad indexada sube con la inflación aunque el sueldo no lo haga.

| Concepto | Comprensión verificable |
|---|---|
| `relación préstamo/valor (LTV)` | `crédito / valor de tasación`. Determina el colchón ante caídas de precio. |
| `dividendo` | Cuota mensual: amortización, interés y seguros. |
| `tasación` | Valoración independiente del inmueble. Base del LTV. |
| `unidad indexada` | Unidad de cuenta reajustada por inflación en la que se expresa el crédito. |
| `riesgo de reajuste` | La cuota en moneda local sube con la inflación. |
| `patrimonio del deudor en el inmueble` | `valor del inmueble − saldo del crédito`. Alinea incentivos. |
| `prepago` | Pago anticipado. Afecta la duración y el ingreso proyectado del banco. |

## 🧠 Modelo mental

El hipotecario tiene un perfil de riesgo distinto del consumo:

```text
CONSUMO       PD alta · LGD alta · plazo corto · monto bajo
HIPOTECARIO   PD baja · LGD BAJA · plazo largo · monto alto

la pérdida esperada del hipotecario es una fracción de la del consumo
PERO la exposición individual es diez a veinte veces mayor
```

De ahí que el análisis se concentre en dos preguntas: **¿podrá pagar durante veinte años?** y **¿cuánto
recupero si no puede?**

## 📖 Desarrollo

### 1. Variables específicas de la evaluación

La evaluación hipotecaria añade variables que no aparecen en otros créditos. La tabla las recoge.

```text
además de las variables generales (clases 4 a 7):

DEL DEUDOR
  · estabilidad proyectada del ingreso a largo plazo
  · edad al vencimiento del crédito
  · composición del hogar y su evolución esperada
  · ahorro acumulado (el pie es un indicador de disciplina)

DEL INMUEBLE
  · tasación independiente y vigente
  · ubicación, antigüedad, estado
  · liquidez del mercado de esa zona y ese segmento
  · situación legal: dominio, gravámenes, servidumbres
  · recepción municipal y regularidad de las construcciones

DE LA OPERACIÓN
  · LTV
  · plazo y edad del deudor al término
  · tipo de tasa: fija, variable o mixta
  · moneda o unidad de expresión
```

### 2. LTV y sus límites

La relación préstamo/valor determina la severidad y suele tener límites regulatorios. La tabla los recoge con su fundamento.

```text
LTV = crédito / min(valor de tasación, precio de compra)
```

**Se usa el menor** entre tasación y precio: si el comprador paga más que la tasación, la diferencia es
riesgo suyo, no del banco.

| LTV | Perfil | Efecto |
|---|---|---|
| ≤ 60 % | Muy conservador | Menor tasa; mínima pérdida esperada |
| 60–80 % | Estándar | Tasa estándar |
| 80–90 % | Alto | Mayor tasa; puede exigir seguro adicional |
| > 90 % | Muy alto | Habitualmente restringido por normativa |

**Efecto del LTV sobre la severidad:**

```text
inmueble tasado en 100 · factor de liquidación 75 % · costos de ejecución 10 %
valor recuperable = 100 × 0,75 × 0,90 = 67,5

LTV 60 %: crédito 60 → recuperación 67,5 → LGD 0 %
LTV 80 %: crédito 80 → recuperación 67,5 → LGD 15,6 %
LTV 90 %: crédito 90 → recuperación 67,5 → LGD 25,0 %

con una caída de precios del 20 %:
  valor recuperable = 54
  LTV 60 %: LGD 10,0 %
  LTV 80 %: LGD 32,5 %
  LTV 90 %: LGD 40,0 %
```

**El LTV determina la severidad, y su efecto se amplifica con las caídas de precio.** Por eso los
límites de LTV son un instrumento macroprudencial (Parte 6, clase 11).

### 3. Evaluar la garantía

La tasación de un inmueble tiene métodos y sesgos conocidos. La tabla los recoge.

```text
□ tasación por profesional independiente registrado
□ tasación con antigüedad menor a 6 meses
□ metodología declarada: comparables, costo de reposición o renta
□ verificación de la ubicación y del estado por visita
□ certificado de dominio vigente, sin gravámenes ni prohibiciones
□ recepción municipal de todas las construcciones
□ certificado de no expropiación
□ si es en construcción: garantías del constructor y seguros
□ seguro de incendio y sismo con el banco como beneficiario
```

**Riesgo específico de las construcciones irregulares:**

```text
un inmueble con ampliaciones sin recepción municipal:
  · la tasación puede incluir esas superficies
  · su valor de liquidación es menor: un comprador exigirá regularizarlas
  · en algunos casos, la irregularidad impide la inscripción o la venta

→ la tasación debe indicar qué superficie está regularizada
→ el LTV se calcula sobre el valor de lo regularizado
```

### 4. Proyectar la capacidad a veinte años

Proyectar a veinte años exige supuestos sobre la vida laboral y sobre las tasas. El procedimiento siguiente los estructura.

```text
la evaluación estándar mira el presente
el hipotecario exige proyectar
```

**Variables a proyectar:**

| Variable | Proyección | Efecto |
|---|---|---|
| Renta | Reajuste esperado, trayectoria de carrera | Determina si la carga baja o sube |
| Dividendo | En unidad indexada: sube con la inflación | Compite con la renta |
| Gastos del hogar | Composición familiar esperada | Reduce el excedente |
| Edad | Al vencimiento del crédito | Capacidad de generar renta |
| Otras deudas | Vencimientos que liberan capacidad | Mejora la carga con el tiempo |

```text
PROYECCIÓN DE CARGA FINANCIERA
                          año 1    año 5    año 10   año 20
renta (reajuste 3,5 %)  2 400 000 2 851 000 3 386 000 4 777 000
dividendo (inflación 3,5 %) 720 000  856 000 1 016 000 1 433 000
otras cuotas              320 000  180 000        0        0
carga financiera           43,3 %   36,3 %   30,0 %   30,0 %
```

**La carga baja con el tiempo si la renta se reajusta al menos como la inflación.** Si el reajuste
salarial fuera del 2,0 % con inflación del 3,5 %:

```text
                          año 1    año 5    año 10   año 20
renta (reajuste 2,0 %)  2 400 000 2 598 000 2 869 000 3 476 000
dividendo                 720 000   856 000 1 016 000 1 433 000
carga financiera           43,3 %    39,9 %   35,4 %   41,2 %
```

**La carga vuelve a subir en el largo plazo.** Ese escenario —reajuste salarial inferior a la
inflación— es el riesgo estructural de los créditos indexados y debe evaluarse explícitamente.

### 5. Mitigantes específicos

El producto hipotecario tiene mitigantes propios que reducen la severidad. La tabla los recoge.

| Mitigante | Efecto |
|---|---|
| Mayor pie (menor LTV) | Reduce la severidad y mejora la tasa |
| Seguro de desgravamen | Cubre el saldo ante fallecimiento |
| Seguro de incendio y sismo | Protege la garantía |
| Seguro de cesantía | Cubre dividendos ante desempleo |
| Codeudor | Mejora la capacidad y la recuperación |
| Plazo que termina antes de la edad de retiro | Evita el tramo de menor renta |
| Cuenta de reserva de dividendos | Colchón ante interrupciones de ingreso |
| Tasa fija en lugar de variable | Elimina el riesgo de tasa del deudor |

## 🧮 Ejemplo guiado

El ejemplo evalúa una operación hipotecaria completa con estrés de tasa y de reajuste. Conviene mirar la cuota en el peor escenario: es la que decide si la operación es prudente.

**Situación.** Evalúa una solicitud hipotecaria completa.

```text
SOLICITANTES
  cónyuges, 38 y 36 años
  renta admisible conjunta                  3 180 000
  cuotas vigentes                             295 000
  gasto de subsistencia (hogar de 4)          985 000
  ahorro acumulado                         42 000 000
  antigüedad laboral: 8 y 6 años, ambos con contrato indefinido

INMUEBLE
  precio de compra                       3 800 UF
  tasación                               3 720 UF
  ubicación: zona consolidada, buena liquidez
  antigüedad: 12 años

OPERACIÓN SOLICITADA
  crédito                                3 100 UF
  plazo                                  25 años
  tasa real                              4,20 % anual
  valor UF                               38 200
```

**Paso 1 — verifica el LTV.**

```text
base de cálculo = min(3 800; 3 720) = 3 720 UF
LTV = 3 100/3 720 = 83,3 %

límite de política estándar: 80 %
→ EXCEDE: requiere condiciones adicionales o mayor pie
```

**Paso 2 — calcula el pie disponible y el ajuste necesario.**

```text
ahorro acumulado: 42 000 000 = 1 099,5 UF
precio: 3 800 UF
pie con el ahorro: 1 099,5 UF → crédito de 2 700,5 UF → LTV = 72,6 % ✓

pero el solicitante pidió 3 100 UF, lo que implica un pie de solo 700 UF
→ ¿por qué no usa todo su ahorro?
```

**Consulta al cliente:** desean reservar 400 UF (15,3 millones) como fondo de emergencia y para gastos
operacionales.

```text
gastos operacionales estimados: 58 UF
fondo de emergencia deseado: 342 UF = 13,1 millones = 9,5 meses de gasto esencial
```

**La reserva es razonable y prudente.** Un solicitante que agota su ahorro en el pie queda sin colchón
ante cualquier evento, lo que aumenta la PD.

**Paso 3 — busca la estructura que cumple ambos objetivos.**

```text
opción A: crédito 2 976 UF (LTV 80,0 %), pie 824 UF
  reserva del cliente: 1 099,5 − 824 − 58 = 217,5 UF = 8,3 millones (6 meses de gasto)
  
opción B: crédito 3 100 UF con seguro adicional de LTV alto
  costo del seguro: ~0,25 UF/mes adicional
  reserva del cliente: 341,5 UF = 13,0 millones (9,5 meses)
```

**Paso 4 — calcula el dividendo de la opción A.**

```text
i mensual = (1,042)^(1/12) − 1 = 0,003432
n = 300
(1,003432)^300 = 2,7940
cuota base = 2 976 × 0,003432 × 2,7940/1,7940 = 2 976 × 0,005345 = 15,91 UF
seguros (desgravamen 0,42 + incendio 0,28) = 0,70 UF
DIVIDENDO = 16,61 UF = 634 502
```

**Paso 5 — capacidad de pago y proyección.**

```text
carga financiera año 1 = (634 502 + 295 000)/3 180 000 = 29,2 %  ✓
excedente = 3 180 000 − 985 000 − 929 502 = 1 265 498  ✓ holgado

PROYECCIÓN (reajuste salarial 3,0 %, inflación 3,5 %)
                    año 1     año 5     año 10    año 20    año 25
renta            3 180 000 3 578 000 4 148 000 5 574 000 6 462 000
dividendo (UF)      16,61     16,61     16,61     16,61     16,61
dividendo (pesos)  634 502   752 700   894 100 1 260 800 1 496 900
otras cuotas       295 000   140 000         0         0         0
carga financiera    29,2 %    24,9 %    21,6 %    22,6 %    23,2 %
```

**La carga se mantiene bajo el 30 % en todo el horizonte.** El reajuste salarial de 3,0 % contra
inflación de 3,5 % produce una leve alza al final, absorbible.

**Paso 6 — prueba de estrés.**

```text
ESCENARIO A: pérdida de un ingreso (el menor, 1 240 000)
  renta 1 940 000 · carga = 47,9 %  → tensa pero viable con seguro de cesantía
  excedente = 1 940 000 − 985 000 − 929 502 = 25 498  → CRÍTICO

ESCENARIO B: inflación 7 % con reajuste salarial 3 %, durante 5 años
  año 5: dividendo 890 000 · renta 3 686 000 · carga = 28,0 %  ✓

ESCENARIO C: caída del valor del inmueble del 25 %
  valor 2 790 UF · saldo año 3 ≈ 2 830 UF
  → patrimonio del deudor NEGATIVO durante aproximadamente 2 años
  valor recuperable en liquidación: 2 790 × 0,78 × 0,90 = 1 958 UF
  LGD = (2 830 − 1 958)/2 830 = 30,8 %
```

**Paso 7 — decisión.**

```text
APROBAR opción A

  crédito 2 976 UF · plazo 25 años · tasa real 4,20 % · LTV 80,0 %
  dividendo 16,61 UF

CONDICIONES
  C1  seguro de cesantía obligatorio por 6 dividendos (escenario A es el crítico)
  C2  mantener reserva mínima de 200 UF acreditada al desembolso
  C3  seguro de incendio y sismo con el banco como beneficiario
  C4  tasación vigente al desembolso (menos de 6 meses)
  C5  verificación de recepción municipal de la totalidad de las construcciones

FUNDAMENTO DEL PIE MAYOR
  la opción B (LTV 83,3 %) habría dejado mayor reserva al cliente,
  pero aumenta la LGD de 15,6 % a 25,0 % en escenario normal
  y de 30,8 % a 38,1 % en escenario de caída de precios.
  
  La condición C2 resuelve el objetivo del cliente —mantener un colchón—
  con un LTV que respeta la política.

PRICING
  PD estimada 0,9 % · LGD 15,6 % → pérdida esperada 0,14 %
  tasa mínima = 3,1 % (fondos reales) + 0,14 % + 0,45 % (operativo) + 0,35 % (capital)
              = 4,04 %
  tasa aplicada 4,20 % → margen 0,16 %  (típico del producto, de bajo margen y alto volumen)
```

**Interpreta:** la solicitud original excedía el LTV de política, y **la solución no fue rechazarla ni
aprobar la excepción**: fue encontrar una estructura que cumple el límite y preserva el objetivo del
cliente de mantener un fondo de emergencia. La condición C2 es la que hace compatible ambas cosas.

## 🏦 Del cliente al banco

El cliente compra una vivienda y el banco origina un activo a veinte años que puede vender. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| "Quiero el máximo crédito" | El LTV determina la severidad de la pérdida | 11, clase 2 |
| Tasación menor al precio | Se usa el menor de los dos | 9, clase 8 |
| Seguros exigidos | Protegen la garantía y el saldo | 3, clase 12 |
| Reserva exigida al desembolso | Reduce la PD por falta de colchón | 2, clase 7 |
| Cuota que sube en pesos | Crédito en unidad indexada | 3, clase 9 |

## 🧪 Práctica

El laboratorio pide evaluar una operación hipotecaria con estrés de tasa, de reajuste y de valor del inmueble. Los tres estreses juntos son los que revelan la exposición real.

En `labs/lab-06.md`, sección hipotecaria:

1. Calcula el LTV y la severidad de tres operaciones en dos escenarios de precio.
2. Proyecta la carga financiera a 25 años con dos escenarios de reajuste salarial.
3. Aplica la lista de verificación de la garantía a un caso.
4. Diseña la estructura que cumple el límite de LTV y el objetivo de reserva del cliente.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen carteras hipotecarias que se deterioran con el ciclo. Las causas son LTV alto y estrés insuficiente en la calificación.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se usa el precio de compra para el LTV | Base incorrecta | Usa el menor entre precio y tasación. |
| No se proyecta la carga a largo plazo | Evaluación estática | Proyecta con reajuste salarial e inflación. |
| El cliente agota su ahorro en el pie | Sin colchón, mayor PD | Exige reserva mínima al desembolso. |
| No se verifica la recepción municipal | Valor de liquidación sobrestimado | Calcula el LTV sobre lo regularizado. |
| Se aprueba LTV alto sin seguro adicional | Severidad no mitigada | Exige seguro o mayor pie. |
| No se estresa la caída de precios | Patrimonio negativo no evaluado | Simula caídas de 20 % a 30 %. |

## ❓ Preguntas de comprobación

1. ¿Por qué se usa el menor entre precio de compra y tasación para el LTV?
2. Calcula la LGD de un LTV de 85 % con caída de precios del 20 %.
3. ¿Qué ocurre con la carga financiera si el reajuste salarial es menor que la inflación?
4. ¿Por qué exigir una reserva al desembolso reduce la probabilidad de incumplimiento?
5. ¿Qué riesgo introduce una construcción sin recepción municipal?

## 📥 Entregable

Guarda en `portfolio/parte-09/clase-12/`:

- el LTV y la severidad de tres operaciones en dos escenarios de precio;
- la proyección de carga financiera a 25 años con dos escenarios de reajuste;
- la lista de verificación de garantía aplicada a un caso;
- la estructura diseñada que cumple el LTV y el objetivo de reserva, con su fundamento.

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

- Financial Stability Board (2012). *Principles for Sound Residential Mortgage Underwriting Practices*. FSB. Estándares de LTV, verificación de ingresos y documentación. <https://www.fsb.org/>
- Basel Committee on Banking Supervision (2017). *Basel III: Finalising post-crisis reforms*. BIS. Ponderaciones de riesgo según LTV.
- Brueggeman, W. y Fisher, J. (2018). *Real Estate Finance and Investments* (16.ª ed.). McGraw-Hill. Análisis de crédito hipotecario y valoración de garantías.
- International Monetary Fund (2011). *Macroprudential Policy: An Organizing Framework*. Límites de LTV como instrumento macroprudencial.
- European Banking Authority (2020). *Guidelines on loan origination and monitoring*. EBA. Evaluación y monitoreo de garantías inmobiliarias.
- Verificación local: revisa los límites de LTV vigentes en tu país, los requisitos de tasación y los seguros exigidos por la normativa.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 11 · Crédito de consumo](11-credito-de-consumo.md) | [Parte 09](../README.md) · [Programa](../../../SYLLABUS.md) | [13 · Crédito comercial y pyme →](13-credito-comercial-y-pyme.md) |
<!-- gen:footer:end -->
