---
part: 9
class: 11
title: "Crédito de consumo"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 11 · Crédito de consumo

> [← 10 · Scoring](10-scoring.md) · [Índice de la parte](../README.md) · [12 · Crédito hipotecario →](12-credito-hipotecario.md)

**Parte 09 — Análisis y gestión de crédito** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Aplicar todo lo anterior al producto de mayor volumen y mayor riesgo relativo de la banca minorista.
El crédito de consumo se decide en minutos, sin garantía, y su rentabilidad depende de un equilibrio
fino entre volumen, precio y calidad de originación.

## 📚 Objetivos

Al finalizar podrás:

1. **Estructurar** la evaluación completa de un crédito de consumo.
2. **Calcular** el precio que cubre la pérdida esperada y el capital.
3. **Diseñar** políticas de admisión por segmento.
4. **Evaluar** el efecto de las decisiones de política sobre el resultado.
5. **Aplicar** mitigantes específicos del producto.

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
| `crédito de consumo` | Préstamo sin garantía específica, destinado a consumo, con cuotas fijas. |
| `pérdida esperada` | `PD × LGD × EAD`. Costo estadístico del riesgo. |
| `pricing basado en riesgo` | Precio diferenciado por nivel de riesgo del deudor. |
| `rentabilidad ajustada por riesgo` | Resultado después de la pérdida esperada y del costo de capital. |
| `política de admisión` | Reglas que determinan a quién se aprueba y bajo qué condiciones. |
| `mitigante` | Condición que reduce el riesgo sin cambiar el precio. |

## 🧠 Modelo mental

El resultado del producto se descompone en cinco términos:

```text
resultado = tasa − costo de fondos − pérdida esperada − costo operativo − costo de capital
```

```text
tasa                     22,0 %
− costo de fondos        −6,2 %
− pérdida esperada       −4,3 %
− costo operativo        −3,8 %
− costo de capital       −2,1 %
= RESULTADO               5,6 %
```

**Cada punto de deterioro en la originación se traslada íntegro a la pérdida esperada**, y con un
resultado de 5,6 %, un aumento de 2 puntos en la pérdida se lleva el 36 % del resultado.

## 📖 Desarrollo

### 1. Estructura de la evaluación

```text
1. identificación y conocimiento del cliente (clase 3)
2. renta admisible (clase 4)
3. capacidad de pago: carga financiera y excedente (clase 5)
4. endeudamiento consolidado (clase 6)
5. historial y comportamiento (clase 7)
6. scoring: probabilidad de incumplimiento (clase 10)
7. decisión: aprobar, rechazar o condicionar
8. pricing según el riesgo
9. mitigantes
```

Los pasos 1 a 6 son **acumulativos, no alternativos**: un buen score no exime de verificar la
capacidad de pago.

### 2. Calcular la pérdida esperada y el precio

```text
pérdida esperada = PD × LGD × EAD
```

```text
segmento A: PD 1,2 % · LGD 62 % · exposición promedio 100 %
  pérdida esperada = 1,2 % × 62 % = 0,74 %

segmento D: PD 9,8 % · LGD 68 % (peor recuperación)
  pérdida esperada = 9,8 % × 68 % = 6,66 %
```

**Precio que cubre el riesgo y el capital:**

```text
tasa mínima = costo de fondos + pérdida esperada + costo operativo + costo de capital + margen

costo de capital = capital requerido × rentabilidad exigida
  capital requerido: 10 % de la exposición
  rentabilidad exigida: 15 %
  costo de capital = 10 % × 15 % = 1,5 % de la exposición
```

| Segmento | PD | Pérdida esperada | Costo operativo | Tasa mínima | Margen objetivo | Tasa final |
|---|---:|---:|---:|---:|---:|---:|
| A | 1,2 % | 0,74 % | 2,8 % | 11,24 % | 3,0 % | 14,24 % |
| B | 2,8 % | 1,74 % | 3,2 % | 12,64 % | 3,0 % | 15,64 % |
| C | 5,4 % | 3,51 % | 3,6 % | 14,81 % | 3,0 % | 17,81 % |
| D | 9,8 % | 6,66 % | 4,1 % | 18,46 % | 3,0 % | 21,46 % |
| E | 16,2 % | 11,18 % | 4,6 % | 23,48 % | 3,0 % | 26,48 % |

(costo de fondos 6,2 % y costo de capital 1,5 % en todos)

**Observación importante:** si la tasa que resulta para un segmento **supera el límite legal de usura**,
ese segmento no puede atenderse a precio adecuado y debe rechazarse. Prestarle a tasa insuficiente
produce pérdida sistemática.

### 3. Política de admisión por segmento

```text
la política define, para cada segmento:
  · punto de corte del score
  · carga financiera máxima
  · monto y plazo máximos
  · mitigantes obligatorios
  · nivel de aprobación requerido
```

```text
SEGMENTO A (score > 700)
  carga financiera máxima     45 %
  monto máximo                12 × renta admisible
  plazo máximo                60 meses
  mitigantes                  ninguno
  aprobación                  automática

SEGMENTO C (score 500–599)
  carga financiera máxima     35 %
  monto máximo                6 × renta admisible
  plazo máximo                36 meses
  mitigantes                  débito automático obligatorio
  aprobación                  automática con revisión de excepciones

SEGMENTO E (score < 400)
  carga financiera máxima     25 %
  monto máximo                3 × renta admisible
  plazo máximo                24 meses
  mitigantes                  débito automático + codeudor
  aprobación                  comité
```

### 4. Efecto de las decisiones de política

```text
simulación: relajar la carga financiera máxima de 40 % a 45 % en el segmento B
```

```text
                        antes        después     variación
solicitudes aprobadas   58 %          67 %        +9 pp
volumen originado       142 000      164 000     +15,5 %
PD promedio             2,8 %         3,4 %       +0,6 pp
pérdida esperada        1,74 %        2,11 %      +0,37 pp
margen bruto            9,44 %        9,44 %      —
resultado unitario      5,60 %        5,23 %      −0,37 pp
RESULTADO TOTAL         7 952         8 577       +7,9 %
```

**El resultado total mejora 7,9 % pese al deterioro de la calidad**, porque el volumen adicional
compensa. Esa es la aritmética que justifica relajar controles, y es correcta **en el corto plazo**.

El análisis completo requiere dos verificaciones adicionales:

```text
1. ¿la PD de 3,4 % es estable o el modelo la subestima en el nuevo tramo?
   si la PD real fuera 4,2 %: resultado unitario 4,69 % → resultado total 7 692 → PEOR

2. ¿el capital regulatorio adicional está considerado?
   mayor riesgo puede implicar mayor ponderación y más capital
```

**La decisión de relajar controles es defendible solo si el modelo está bien calibrado en el nuevo
tramo**, y esa es precisamente la zona donde la calibración suele fallar (clase 10).

### 5. Mitigantes del producto

| Mitigante | Efecto | Aplicable a |
|---|---|---|
| Débito automático | Reduce PD entre 15 % y 30 % | Todos los segmentos |
| Fecha de vencimiento alineada al pago de la renta | Reduce mora por conducta | Rentas de fecha fija |
| Codeudor con renta acreditada | Reduce PD y LGD | Segmentos de mayor riesgo |
| Seguro de cesantía | Reduce PD ante desempleo | Rentas dependientes |
| Monto escalonado (construcción de historial) | Limita la exposición inicial | Sin historial |
| Plazo acotado | Reduce la exposición al ciclo | Segmentos de mayor riesgo |
| Cierre de cupos rotativos | Reduce el endeudamiento total | Perfiles con alta utilización |

```text
efecto combinado de débito automático + fecha alineada:
  PD baja de 5,4 % a 4,1 % (−24 %)
  pérdida esperada baja de 3,51 % a 2,67 %
  → permite reducir la tasa 0,84 puntos manteniendo el mismo resultado
  → o mantener la tasa y mejorar el resultado en 0,84 puntos
```

## 🧮 Ejemplo guiado

**Situación.** Evalúa una solicitud de crédito de consumo por 7 500 000 a 48 meses.

```text
SOLICITANTE
  renta admisible                     1 620 000
  cuotas vigentes                       285 000
  gasto de subsistencia estimado        780 000
  score                                     548
  PD estimada                             5,1 %
  historial: una mora de 22 días hace 9 meses; utilización de cupos 44 %
  antigüedad laboral: 3 años · cotizaciones continuas
```

**Paso 1 — capacidad de pago.**

```text
cuota estimada (48 meses, tasa 17,8 %): 
  i mensual = 1,375 % → cuota = 7 500 000 × 0,01375 × 1,9358/0,9358 = 213 300
  más seguro de desgravamen 6 400 → cuota total 219 700

carga financiera = (285 000 + 219 700)/1 620 000 = 31,2 %
excedente = 1 620 000 − 780 000 − 504 700 = 335 300
```

**Paso 2 — verifica contra la política del segmento.**

```text
score 548 → segmento C
  carga financiera máxima 35 %  →  31,2 % ✓
  monto máximo 6 × renta = 9 720 000  →  7 500 000 ✓
  plazo máximo 36 meses  →  48 meses SOLICITADOS ✗ EXCEDE
  mitigante obligatorio: débito automático
```

**Paso 3 — evalúa el exceso de plazo.**

```text
opción A: reducir el plazo a 36 meses
  cuota = 7 500 000 × 0,01375 × 1,6398/0,6398 = 264 200 + 6 400 = 270 600
  carga financiera = (285 000 + 270 600)/1 620 000 = 34,3 %  ✓ dentro del límite
  excedente = 1 620 000 − 780 000 − 555 600 = 284 400

opción B: mantener 48 meses como excepción
  requiere aprobación de nivel superior y justificación
```

**Paso 4 — calcula el pricing.**

```text
PD 5,1 % · LGD 65 % · pérdida esperada = 3,32 %

tasa mínima = 6,2 % (fondos) + 3,32 % (pérdida) + 3,6 % (operativo) + 1,5 % (capital)
            = 14,62 %
tasa con margen objetivo de 3 % = 17,62 %
tasa aplicada: 17,8 %  ✓ cubre
```

**Paso 5 — aplica mitigantes y recalcula.**

```text
mitigantes propuestos:
  · débito automático (obligatorio del segmento)
  · fecha de vencimiento el día 30, alineada con su pago de renta

efecto estimado: PD baja de 5,1 % a 3,9 %
pérdida esperada = 3,9 % × 65 % = 2,54 %
tasa mínima = 6,2 + 2,54 + 3,6 + 1,5 = 13,84 %
```

**Con los mitigantes, la operación soporta una tasa de 16,84 % con el mismo margen.**

**Paso 6 — evalúa la mora histórica.**

```text
una mora de 22 días hace 9 meses:
  · ¿es aislada? → sí, ninguna otra en 24 meses
  · ¿fue regularizada? → sí, en 6 días
  · ¿coincide con algún evento? → sí, cambio de empleador con desfase de pago
  
→ MORA CIRCUNSTANCIAL, no patrón (clase 7)
→ ya está incorporada en el score
→ no justifica un ajuste adicional
```

**Paso 7 — decisión.**

```text
APROBAR

condiciones:
  · monto 7 500 000 · plazo 36 meses (no 48, por política del segmento)
  · tasa 16,84 % (reducida por los mitigantes)
  · débito automático obligatorio desde su cuenta
  · fecha de vencimiento día 30
  · seguro de desgravamen obligatorio

comunicación al cliente:
  "Podemos aprobar 7 500 000 a 36 meses con cuota de 270 600, a una tasa de
   16,84 % anual, que es 0,96 puntos menor a la estándar de su perfil porque
   el débito automático reduce el riesgo de la operación.
   
   Si necesita una cuota menor, las opciones son reducir el monto a 6 000 000
   (cuota 216 500) o incorporar un codeudor con renta acreditada, lo que
   permitiría extender el plazo a 48 meses."

resultado esperado de la operación:
  tasa 16,84 % − fondos 6,2 % − pérdida 2,54 % − operativo 3,6 % − capital 1,5 %
  = 3,00 % de margen sobre 7 500 000 = 225 000 anuales
```

**Interpreta:** la operación se aprueba con **plazo menor al solicitado y tasa menor a la estándar**.
Ambas decisiones tienen fundamento: el plazo por política del segmento, la tasa porque los mitigantes
reducen la PD estimada. Y la comunicación ofrece dos alternativas concretas en lugar de un "no" a la
solicitud original.

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| "¿Por qué esa tasa?" | Pricing basado en la pérdida esperada del segmento | 15, clase 7 |
| Débito automático exigido | Mitigante que reduce la PD y permite mejor precio | 9, clase 10 |
| Plazo menor al solicitado | Política del segmento | 9, clase 1 |
| Tasa menor a la estándar | Efecto del mitigante trasladado al cliente | 15, clase 7 |
| Rechazo por límite de usura | El segmento no puede atenderse a precio adecuado | 3, clase 13 |

## 🧪 Práctica

En `labs/lab-06.md`:

1. Evalúa tres solicitudes completas aplicando los nueve pasos.
2. Calcula la tasa mínima de cinco segmentos con sus componentes.
3. Simula el efecto de relajar un parámetro de política sobre el resultado total.
4. Cuantifica el efecto de tres mitigantes sobre la PD y el precio.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se aprueba solo por el score | Capacidad de pago no verificada | Los pasos son acumulativos. |
| El precio no cubre la pérdida | Pricing no basado en riesgo | Calcula la tasa mínima por segmento. |
| Se relaja la política por volumen | Calibración del nuevo tramo no verificada | Verifica la PD real del tramo ampliado. |
| Los mitigantes no se traducen en precio | Efecto no cuantificado | Mide su impacto sobre la PD. |
| Se presta sobre el límite de usura | Segmento no atendible | Rechaza en lugar de prestar a pérdida. |
| Una mora aislada se trata como patrón | Análisis incompleto | Distingue circunstancial de patrón. |

## ❓ Preguntas de comprobación

1. Descompón el resultado de un crédito de consumo en sus cinco términos.
2. Calcula la tasa mínima para un segmento con PD 4 % y LGD 65 %.
3. ¿Cuándo es defendible relajar un parámetro de política y qué debe verificarse?
4. ¿Cómo se traduce un mitigante en el precio de la operación?
5. ¿Qué se hace cuando la tasa requerida supera el límite legal?

## 📥 Entregable

Guarda en `portfolio/parte-09/clase-11/`:

- tres solicitudes evaluadas con los nueve pasos completos;
- la tasa mínima de cinco segmentos con todos sus componentes;
- la simulación del efecto de relajar un parámetro sobre el resultado total;
- el efecto cuantificado de tres mitigantes sobre PD y precio.

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

- Basel Committee on Banking Supervision (2017). *Basel III: Finalising post-crisis reforms*. BIS. Requerimiento de capital para exposiciones minoristas.
- Anderson, R. (2007). *The Credit Scoring Toolkit*. Oxford University Press. Políticas de admisión y puntos de corte.
- Rose, P. y Hudgins, S. (2013). *Bank Management & Financial Services* (9.ª ed.). McGraw-Hill. Capítulo 17: crédito de consumo.
- Thomas, L., Edelman, D. y Crook, J. (2017). *Credit Scoring and Its Applications* (2.ª ed.). SIAM. Pricing basado en riesgo.
- World Bank (2017). *Good Practices for Financial Consumer Protection*. Banco Mundial. Estándares de originación responsable.
- Verificación local: revisa el límite legal de tasa de tu país y las normas sobre originación responsable y evaluación de capacidad de pago.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 10 · Scoring](10-scoring.md) | [Parte 09](../README.md) · [Programa](../../../SYLLABUS.md) | [12 · Crédito hipotecario →](12-credito-hipotecario.md) |
<!-- gen:footer:end -->
