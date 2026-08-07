---
part: 1
class: 3
title: "Porcentajes en decisiones financieras"
level: fundamento
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 03 · Porcentajes en decisiones financieras

> [← 02 · Fracciones, decimales y razones](02-fracciones-decimales-y-razones.md) · [Índice de la parte](../README.md) · [04 · Variaciones porcentuales e índices →](04-variaciones-porcentuales-e-indices.md)

**Parte 01 — Matemática financiera básica** · **Nivel:** Fundamento — sin conocimientos previos · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Convertir el porcentaje de un cálculo escolar en una herramienta de decisión. El porcentaje es la
operación más usada y peor aplicada de las finanzas: se equivoca la base, se encadenan descuentos
como si se sumaran, y se confunde "descontar 20 %" con "recuperar 20 %". Esta clase fija las tres
reglas que impiden esos errores y muestra por qué un aumento del 10 % seguido de una caída del 10 %
no devuelve al punto de partida.

## 📚 Objetivos

Al finalizar podrás:

1. **Identificar** la base correcta de cualquier porcentaje antes de calcularlo.
2. **Encadenar** porcentajes sucesivos multiplicando factores, no sumando tasas.
3. **Demostrar** por qué `+10 %` seguido de `−10 %` deja un saldo de `−1 %`.
4. **Calcular** el porcentaje inverso: recuperar la base cuando solo conoces el resultado.
5. **Detectar** presentaciones engañosas de descuentos, recargos y rentabilidades.

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
| `base` | La cantidad sobre la que se aplica el porcentaje. Cambiarla cambia el resultado aunque la tasa sea idéntica. Es el dato que más se omite. |
| `factor multiplicativo` | Un `+15 %` es `× 1,15` y un `−15 %` es `× 0,85`. Trabajar con factores hace imposible sumar mal. |
| `encadenamiento` | Varios porcentajes sucesivos se **multiplican**: `1,15 × 0,85 = 0,9775`, no `1,00`. |
| `porcentaje inverso` | Si el precio con IVA es 119 y el IVA es 19 %, la base es `119 / 1,19 = 100`, no `119 × 0,81`. |
| `punto porcentual` | Diferencia entre dos porcentajes. De 20 % a 25 % hay 5 **puntos porcentuales** y un aumento del **25 %**. |
| `asimetría de la caída` | Perder 50 % exige ganar 100 % para volver al inicio. La recuperación siempre es mayor que la caída. |

## 🧠 Modelo mental

Deja de pensar en "sumar y restar porcentajes" y piensa en **multiplicar factores**:

```text
precio final = precio inicial × f₁ × f₂ × f₃ ...
   descuento 20 %  → f = 0,80
   recargo 15 %    → f = 1,15
   IVA 19 %        → f = 1,19
```

Con factores, el orden no importa para el resultado final y el error de sumar tasas desaparece por
construcción. Toda la Parte 7 (capitalización) es esta misma idea llevada al tiempo.

## 📖 Desarrollo

### 1. La base: el dato que decide el resultado

Un producto cuesta 40 000 y sube a 50 000.

```text
¿cuánto subió?          (50 000 − 40 000) / 40 000 = 25 %   base = precio viejo
¿cuánto era antes?      (50 000 − 40 000) / 50 000 = 20 %   base = precio nuevo
```

Ambos números son correctos y responden preguntas distintas: **subió 25 %**, y el precio viejo era
**20 % menor** que el nuevo. Un titular puede elegir cualquiera de los dos y ser técnicamente veraz.
Por eso la regla es: **nombra la base en la misma frase que el porcentaje**.

### 2. Encadenamiento: descuentos que no se suman

Una tienda ofrece "30 % + 20 % adicional".

```text
intuición errónea    30 % + 20 % = 50 % de descuento
cálculo correcto     1 − (0,70 × 0,80) = 1 − 0,56 = 0,44 → 44 % de descuento
```

Seis puntos porcentuales de diferencia sobre 200 000 pesos son 12 000 pesos. La misma mecánica, con
signo contrario, aparece en los recargos:

```text
recargo 10 % y luego 10 %:   1,10 × 1,10 = 1,21 → 21 %, no 20 %
```

### 3. La asimetría: por qué caer y subir lo mismo no empata

Un fondo de 1 000 000 sube 10 % y luego baja 10 %.

```text
1 000 000 × 1,10 = 1 100 000
1 100 000 × 0,90 =   990 000   ← 1 % por debajo del inicio
```

La razón es que la caída se aplica sobre una base mayor. Generalizando, para volver al punto de
partida tras una caída `d`:

```text
ganancia necesaria = d / (1 − d)

caída 10 %  → 11,1 % para recuperar
caída 20 %  → 25,0 %
caída 50 %  → 100,0 %
caída 80 %  → 400,0 %
```

Esta tabla es una de las razones por las que la gestión de riesgo de la Parte 8 prioriza **limitar
pérdidas** antes que maximizar ganancias: la aritmética castiga la caída dos veces.

### 4. Porcentaje inverso: recuperar la base

Es el cálculo que más se equivoca en facturación y en comisiones.

```text
Precio con IVA (19 %) = 119 000
  ✗ 119 000 × 0,81 = 96 390     ← incorrecto
  ✓ 119 000 / 1,19 = 100 000    ← correcto
  IVA = 119 000 − 100 000 = 19 000
```

La misma lógica se usa para descontar una comisión retenida en origen, para pasar de un monto neto
recibido a un monto bruto solicitado, y para calcular el capital de un crédito cuando el banco
descuenta gastos del desembolso.

## 🧮 Ejemplo guiado

**Situación.** Un cliente solicita un crédito de 3 000 000. El banco descuenta en el desembolso una
comisión de 2 % y un seguro de 1,5 %, ambos sobre el capital. Además ofrece una promoción de "20 % de
descuento en la comisión". El cliente necesita recibir exactamente 3 000 000 en su cuenta.

**Paso 1 — comisión con promoción.**

```text
comisión efectiva = 2 % × (1 − 0,20) = 2 % × 0,80 = 1,6 %
```

**Paso 2 — descuento total sobre el capital.**

```text
descuentos = 1,6 % + 1,5 % = 3,1 %   (aquí SÍ se suman: ambos tienen la misma base, el capital)
factor de desembolso = 1 − 0,031 = 0,969
```

Nótese la diferencia con el punto 2 del desarrollo: dos porcentajes se suman **solo si comparten
base**. Aquí ambos se calculan sobre el capital original, no en cascada.

**Paso 3 — capital necesario (porcentaje inverso).**

```text
capital = 3 000 000 / 0,969 = 3 095 975,23 → 3 095 976 (redondeo al alza al peso)
```

**Paso 4 — verificación.**

```text
comisión = 3 095 976 × 0,016 =  49 535,62
seguro   = 3 095 976 × 0,015 =  46 439,64
desembolso = 3 095 976 − 49 535,62 − 46 439,64 = 3 000 000,74  ✔
```

**Paso 5 — interpreta.** El cliente firmará por **3 095 976** y recibirá **3 000 000**. Pagará
intereses sobre el capital firmado, no sobre lo recibido. Ese es exactamente el motivo por el que la
tasa de interés no basta para comparar créditos y por el que existe el costo total: clase 13 de la
Parte 3.

## 🏦 Del cliente al banco

| Situación | Lectura del cliente | Lectura del banco |
|---|---|---|
| "30 % + 20 % adicional" | 50 % de rebaja | Factor 0,56 aplicado al precio de lista |
| Comisión descontada del desembolso | "Me depositaron menos" | Capital bruto = neto / (1 − tasas), base de cálculo de intereses |
| Fondo que cae 20 % y sube 20 % | "Quedé igual" | −4 % de patrimonio; el reporte debe mostrarlo |
| "La tasa subió de 20 % a 25 %" | "Subió 5 %" | +5 puntos porcentuales = +25 % relativo |

## 🧪 Práctica

En `labs/lab-02.md`:

1. Construye una tabla de factores para diez operaciones porcentuales reales de tu vida.
2. Calcula un descuento encadenado de tres tramos y compáralo con la suma ingenua.
3. Genera la tabla de recuperación para caídas de 5 % a 90 % en pasos de 5 puntos.
4. Resuelve tres casos de porcentaje inverso con verificación completa.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| El descuento aplicado es menor al esperado | Se sumaron descuentos en cascada | Multiplica factores: `1 − Π(1 − dᵢ)`. |
| Al quitar el IVA el número no cuadra | Se multiplicó por `1 − t` en vez de dividir por `1 + t` | Porcentaje inverso: `base = total / (1 + t)`. |
| "Recuperé la caída" pero el saldo es menor | Asimetría entre caída y recuperación | Aplica `d / (1 − d)` para saber cuánto falta de verdad. |
| Dos informes dan variaciones distintas | Bases distintas (valor inicial vs. final) | Nombra la base junto al porcentaje siempre. |
| Se suman porcentajes con bases distintas | Se asumió base común sin verificarla | Solo se suman porcentajes que comparten exactamente la misma base. |
| Confusión entre 5 % y 5 puntos porcentuales | Uso indistinto de ambos términos | Reserva "puntos porcentuales" para diferencias entre tasas. |

## ❓ Preguntas de comprobación

1. Un precio baja 25 % y luego sube 25 %. ¿Cuál es la variación total y por qué no es cero?
2. ¿Cuánto debe subir un fondo que perdió 35 % para volver a su valor inicial?
3. Recibes 4 700 000 tras descuentos de 3 % y 2,5 % sobre el capital. ¿Por cuánto firmaste?
4. ¿En qué caso sí es legítimo sumar dos porcentajes?
5. Un informe dice "la morosidad subió 2 %". ¿Qué información necesitas para interpretarlo?

## 📥 Entregable

Guarda en `portfolio/parte-01/clase-03/`:

- la tabla de factores multiplicativos de tus diez operaciones;
- el cálculo de descuento encadenado con la comparación contra la suma ingenua;
- la tabla de recuperación tras caídas;
- un caso resuelto de capital bruto con verificación numérica completa.

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

- Ross, S., Westerfield, R. y Jordan, B. (2022). *Fundamentos de finanzas corporativas* (12.ª ed.). McGraw-Hill. Capítulo 6: costo efectivo y efecto de comisiones sobre el desembolso.
- Blank, L. y Tarquin, A. (2018). *Ingeniería económica* (8.ª ed.). McGraw-Hill. Capítulo 3: factores y encadenamiento de tasas.
- Kahneman, D. (2011). *Pensar rápido, pensar despacio*. Debate. Capítulos sobre encuadre (*framing*): por qué la presentación de un porcentaje cambia la decisión.
- Thaler, R. y Sunstein, C. (2021). *Nudge: la versión final*. Taurus. Capítulo sobre transparencia de precios y comparabilidad.
- OECD (2020). *Recommendation on Financial Literacy*. OCDE. Principios sobre divulgación comprensible de costos.
- Verificación local: contrasta con la norma de tu país sobre publicidad de descuentos y sobre información precontractual de créditos (en Chile, Ley 19.496 y su reglamento de información financiera).

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 02 · Fracciones, decimales y razones](02-fracciones-decimales-y-razones.md) | [Parte 01](../README.md) · [Programa](../../../SYLLABUS.md) | [04 · Variaciones porcentuales e índices →](04-variaciones-porcentuales-e-indices.md) |
<!-- gen:footer:end -->
