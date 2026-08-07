---
part: 11
class: 9
title: "Derivados y coberturas"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 09 · Derivados y coberturas

> [← 08 · Riesgo país y de contraparte](08-riesgo-pais-y-de-contraparte.md) · [Índice de la parte](../README.md) · [10 · Riesgo operacional →](10-riesgo-operacional.md)

**Parte 11 — Gestión integral de riesgos** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Usar derivados para reducir riesgo, y reconocer cuándo se están usando para lo contrario. La misma
herramienta que permite a un banco eliminar un descalce permite acumular una posición direccional
invisible en el balance: la diferencia está en la intención, la documentación y la medición.

Las clases anteriores miden riesgos. Esta trata los instrumentos con los que se cubren, y su punto crítico no es cómo funcionan sino cuándo dejan de cubrir. Una cobertura que no cumple los requisitos de efectividad no es una cobertura: es una posición especulativa con otro nombre.

## 📚 Objetivos

Al finalizar podrás:

1. **Describir** los cuatro derivados básicos y su perfil de resultado.
2. **Diseñar** una cobertura y calcular su ratio óptimo.
3. **Medir** la efectividad de una cobertura y su porción inefectiva.
4. **Aplicar** los requisitos de contabilidad de coberturas.
5. **Distinguir** una cobertura de una posición especulativa documentada como cobertura.

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

Los cuatro primeros términos son los instrumentos; los cuatro siguientes, la relación de cobertura y su medición. La **inefectividad** es lo que hay que vigilar: una cobertura que se mueve menos o más que la partida cubierta deja una parte descubierta que sí impacta el resultado.

| Concepto | Comprensión verificable |
|---|---|
| `forward` | Obligación de comprar o vender a un precio fijado, en una fecha futura. |
| `futuro` | Forward estandarizado, negociado en bolsa, con margen diario. |
| `swap` | Intercambio de flujos entre dos partes durante un período. |
| `opción` | Derecho, no obligación, de comprar o vender a un precio dado. |
| `partida cubierta` | El riesgo que se quiere neutralizar. |
| `instrumento de cobertura` | El derivado que lo neutraliza. |
| `ratio de cobertura` | Proporción del nocional del derivado sobre la partida cubierta. |
| `inefectividad` | Parte del movimiento que la cobertura no neutraliza. |

## 🧠 Modelo mental

El modelo mental es una pareja: un instrumento de cobertura solo existe respecto de una partida cubierta concreta. Sin esa pareja documentada desde el principio, el mismo contrato es una posición direccional, y su resultado va a la cuenta de resultados sin compensar nada.

```text
UNA COBERTURA ES UNA POSICIÓN OPUESTA A UNA QUE YA TIENES

  si no tienes la posición original,
  el derivado no es una cobertura: es una apuesta

TRES PREGUNTAS QUE DISTINGUEN UNA DE OTRA
  1. ¿cuál es exactamente la partida cubierta?
  2. ¿el derivado se mueve en dirección contraria a ella?
  3. ¿el nocional guarda relación con la exposición real?

  si alguna no tiene respuesta clara y documentada,
  no es una cobertura
```

## 📖 Desarrollo

### 1. Los cuatro instrumentos

Los cuatro instrumentos básicos cubren necesidades distintas y tienen perfiles de pago distintos. La tabla los compara.

| Instrumento | Obligación | Costo inicial | Perfil |
|---|---|---|---|
| Forward | Ambas partes | Cero | Lineal y simétrico |
| Futuro | Ambas partes | Margen inicial | Lineal, con flujo diario |
| Swap | Ambas partes | Cero al inicio | Lineal, en el tiempo |
| Opción | Solo el vendedor | Prima | Asimétrico |

```text
PERFILES DE RESULTADO

FORWARD comprado          OPCIÓN de compra comprada
resultado                 resultado
   │      ╱                  │      ╱
   │    ╱                    │    ╱
───┼──╱──── precio        ───┼───────── precio
   │╱                        │  −prima
   ╱                         │
```

```text
LA ASIMETRÍA DE LA OPCIÓN TIENE PRECIO
  el forward no cuesta nada y elimina el riesgo Y la oportunidad
  la opción cuesta la prima y elimina el riesgo conservando la oportunidad

  no hay almuerzo gratis: la prima ES el precio de esa asimetría
```

### 2. Los tres tipos de cobertura contable

La contabilidad reconoce tres tipos de cobertura con tratamientos distintos. La tabla los separa.

| Tipo | Qué cubre | Dónde va el resultado |
|---|---|---|
| Valor razonable | Cambios de valor de un activo o pasivo reconocido | Resultado, junto con la partida |
| Flujos de efectivo | Variabilidad de flujos futuros | Otro resultado integral, hasta que el flujo ocurra |
| Inversión neta en el extranjero | Traslación de una operación en el exterior | Otro resultado integral |

```text
REQUISITOS PARA APLICAR CONTABILIDAD DE COBERTURAS (NIIF 9)
  1. relación económica entre partida e instrumento
  2. el riesgo de crédito no domina los cambios de valor
  3. ratio de cobertura coherente con la gestión real del riesgo
  4. designación y documentación FORMAL AL INICIO

  el punto 4 es el que más se incumple:
  no se puede designar una cobertura retroactivamente
  cuando ya se sabe que funcionó
```

### 3. Ratio de cobertura

El ratio de cobertura determina qué proporción de la partida queda cubierta. El procedimiento siguiente lo calcula.

```text
RATIO ÓPTIMO (mínima varianza)

  h* = ρ × (σ_S / σ_F)

  ρ    correlación entre el precio de la partida y el del derivado
  σ_S  volatilidad del precio de la partida
  σ_F  volatilidad del precio del derivado
```

```text
si ρ = 1 y σ_S = σ_F  →  h* = 1  (cobertura perfecta, uno a uno)
si ρ < 1              →  h* < 1  (cubrir uno a uno SOBRECUBRE)

nocional del derivado = h* × valor de la partida cubierta
```

**Riesgo de base:** cuando el derivado no está referido exactamente a la partida cubierta. Se cubre
combustible de aviación con futuros de petróleo, o una tasa local con un índice internacional. La
diferencia entre ambos es lo que la cobertura no neutraliza.

### 4. Efectividad

La efectividad se mide y se documenta periódicamente, no se supone. El procedimiento la evalúa.

```text
MEDICIÓN DE EFECTIVIDAD
  cambio de valor del instrumento de cobertura
  ──────────────────────────────────────────  → debe compensar
  cambio de valor de la partida cubierta

INEFECTIVIDAD = la parte que no se compensa
  se reconoce SIEMPRE en resultado, en todos los tipos de cobertura
```

| Fuente de inefectividad | Causa |
|---|---|
| Riesgo de base | Subyacentes distintos |
| Desajuste de plazo | Vencimientos distintos |
| Desajuste de nocional | Ratio distinto del óptimo |
| Riesgo de crédito del derivado | Ajuste de valoración por crédito |
| Valor temporal de la opción | Si no se excluye de la designación |

### 5. Cuándo una cobertura deja de serlo

Hay situaciones concretas en que la relación de cobertura se rompe, con efectos contables inmediatos. La tabla las recoge.

```text
SEÑALES DE ALERTA
  · el nocional supera la exposición real
  · la "partida cubierta" es una transacción futura poco probable
  · el derivado se contrata y la posición original nunca aparece
  · se cierra el derivado cuando gana y se mantiene cuando pierde
  · la mesa que cubre es la misma que mide la efectividad
  · la cobertura se designa después de conocer su resultado
  · el resultado del "libro de cobertura" es sistemáticamente positivo
```

**La última señal es la más reveladora.** Una cobertura bien hecha produce, por definición, un resultado
aproximadamente opuesto al de la partida cubierta. **Un libro de coberturas que siempre gana no está
cubriendo nada.**

## 🧮 Ejemplo guiado

El ejemplo documenta una relación de cobertura y mide su efectividad. Conviene fijarse en la parte inefectiva: por pequeña que sea, va directa al resultado.

**Situación.** Un banco cubre el riesgo de tasa de una emisión y evalúa la efectividad.

```text
PARTIDA CUBIERTA
  emisión propia de bonos a tasa fija
  nocional 200 000, cupón 7,4 %, plazo residual 4,2 años
  el banco quiere convertir su costo a tasa variable

INSTRUMENTO
  swap de tasa: el banco RECIBE fija 7,25 % y PAGA variable
  nocional propuesto 200 000, plazo 4,2 años

DATOS DE MERCADO
  volatilidad del valor del bono propio      3,8 %
  volatilidad del valor del swap             3,6 %
  correlación entre ambos                     0,96
```

**Paso 1 — verifica que la cobertura tenga sentido económico.**

```text
posición original: PAGA fija 7,4 % (es una emisión propia)
swap:              RECIBE fija 7,25 %, PAGA variable

resultado combinado:
  paga 7,4 % fija      (emisión)
  recibe 7,25 % fija   (swap)
  paga variable        (swap)
  ────────────────────────────
  COSTO NETO = variable + 0,15 %

el objetivo se cumple: costo convertido a variable  ✓
```

**Paso 2 — calcula el ratio de cobertura óptimo.**

```text
h* = ρ × (σ_S / σ_F) = 0,96 × (3,8 / 3,6) = 0,96 × 1,0556 = 1,0133

nocional óptimo = 1,0133 × 200 000 = 202 667

el nocional propuesto (200 000) está 1,3 % por debajo del óptimo
→ ligera subcobertura, aceptable
```

**Paso 3 — mide la efectividad en un movimiento de tasas.**

```text
alza de 100 pb:

valor del bono emitido (pasivo del banco):
  duración modificada 3,64
  Δ valor = −3,64 % × 200 000 = −7 280
  como es un PASIVO, su caída de valor es GANANCIA: +7 280

valor del swap (recibe fija):
  duración modificada 3,58
  Δ valor = −3,58 % × 200 000 = −7 160  (pérdida)

resultado neto: +7 280 − 7 160 = +120
```

**Paso 4 — calcula la efectividad.**

```text
efectividad = 7 160 / 7 280 = 98,35 %
inefectividad = 120  → se reconoce en resultado

fuente de la inefectividad:
  diferencia de duración (3,64 vs. 3,58) = 0,06
  0,06 % × 200 000 = 120  ✓ explicada por completo
```

**Paso 5 — evalúa el efecto del riesgo de crédito.**

```text
la contraparte del swap tiene un ajuste de valoración por crédito
  CVA estimado: 340 sobre el valor del swap

¿domina el riesgo de crédito los cambios de valor?
  cambio de valor por tasa: 7 160
  cambio de valor por crédito: 340 × sensibilidad ≈ 68

  68 / 7 160 = 0,95 %  → NO domina  ✓
  requisito de NIIF 9 cumplido
```

**Paso 6 — documenta la designación.**

```text
DOCUMENTACIÓN AL INICIO (requisito formal)
  · partida cubierta: emisión de bonos, nocional 200 000, cupón 7,4 %,
    vencimiento identificado por número de instrumento
  · riesgo cubierto: componente de tasa libre de riesgo
    (NO el diferencial de crédito propio)
  · instrumento: swap identificado por número de contrato
  · tipo: cobertura de valor razonable
  · ratio: 1:1 sobre el nocional, con h* calculado de 1,0133
  · método de medición de efectividad: comparación de cambios
    de valor, mensual
  · fuentes de inefectividad esperadas: diferencia de duración,
    ajuste de valoración por crédito
```

**Paso 7 — detecta lo que convertiría esto en otra cosa.**

```text
ESCENARIO ALTERNATIVO
  la mesa propone un nocional de 320 000 en lugar de 200 000
  argumento: "aprovechar el nivel actual de tasas"

  nocional 320 000 sobre partida de 200 000 → ratio 1,60
  h* calculado: 1,0133

  el exceso de 120 000 NO cubre nada:
  es una posición direccional receptora de tasa fija

  · no califica para contabilidad de coberturas en su totalidad
  · el exceso debe medirse a valor razonable con efecto en resultado
  · consume límite del libro de negociación, no de cobertura
  · requiere aprobación como posición, no como cobertura

RECHAZAR la propuesta o aprobar 200 000 como cobertura
y 120 000 como posición explícita con su propio límite
```

**Interpreta:** la cobertura correcta produjo una inefectividad de 120 —el 1,6 % del movimiento— y esa
cifra estaba **completamente explicada** por la diferencia de duración. Ese es el estándar: no que la
inefectividad sea cero, sino que sea **pequeña y explicable**. Una inefectividad que no se puede
descomponer en causas identificadas es la señal de que la cobertura está cubriendo algo distinto de lo
que dice cubrir.

## 🏦 Del cliente al banco

El cliente contrata una cobertura y el banco la registra como tal solo si cumple requisitos formales. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Me ofrecen fijar el tipo de cambio» | Forward vendido; el banco cubre su posición | 13, clase 9 |
| «Pagué una prima y no la usé» | Precio de la asimetría de la opción | 8, clase 13 |
| «El banco perdió con derivados» | Posición direccional documentada como cobertura | 11, clase 9 |
| «Me vendieron un producto que no entendí» | Deber de idoneidad del producto | 12, clase 8 |
| «La cobertura no me protegió del todo» | Riesgo de base | 11, clase 9 |

## 🧪 Práctica

El laboratorio pide evaluar la efectividad de tres coberturas. Una de ellas no califica, y explicar por qué es el objetivo.

En `labs/lab-05.md`:

1. Dibuja el perfil de resultado de los cuatro instrumentos ante movimientos del subyacente.
2. Calcula el ratio de cobertura óptimo y compáralo con la cobertura uno a uno.
3. Mide la efectividad de una cobertura y descompón su inefectividad por fuente.
4. Evalúa tres operaciones y determina cuáles son coberturas y cuáles posiciones.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen coberturas que produjeron volatilidad en el resultado. Las causas son documentación insuficiente y ratios mal calculados.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| El libro de coberturas siempre gana | No está cubriendo | Verifica la partida cubierta. |
| Nocional mayor que la exposición | Posición direccional encubierta | Separa el exceso y dale su límite. |
| Designación posterior al resultado | Requisito formal incumplido | Documenta al inicio, siempre. |
| Cobertura uno a uno con ρ < 1 | Sobrecobertura | Calcula el ratio óptimo. |
| Inefectividad no explicada | Cobertura mal especificada | Descomponla por fuente. |
| La misma mesa cubre y mide | Sin independencia | Medición por área distinta. |

## ❓ Preguntas de comprobación

1. ¿Qué tres preguntas distinguen una cobertura de una apuesta?
2. ¿Por qué cubrir uno a uno puede ser sobrecubrir?
3. ¿Por qué la inefectividad se reconoce siempre en resultado?
4. ¿Qué requisito formal de NIIF 9 es el que más se incumple y por qué importa?
5. ¿Por qué un libro de coberturas que siempre gana es una señal de alerta?

## 📥 Entregable

Guarda en `portfolio/parte-11/clase-09/`:

- los perfiles de resultado de los cuatro instrumentos;
- el cálculo del ratio óptimo y su comparación con la cobertura uno a uno;
- la medición de efectividad con la inefectividad descompuesta;
- la clasificación de tres operaciones entre cobertura y posición, con justificación.

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

- IFRS Foundation. *NIIF 9 Instrumentos Financieros*, capítulo 6: contabilidad de coberturas. <https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/>
- Hull, J. (2021). *Options, Futures, and Other Derivatives* (11.ª ed.). Pearson. Capítulos 1 a 4 y 7.
- Basel Committee on Banking Supervision (2019). *Minimum capital requirements for market risk*. BIS.
- International Swaps and Derivatives Association. *ISDA Master Agreement* y su documentación de respaldo. ISDA.
- Ederington, L. (1979). "The Hedging Performance of the New Futures Markets". *Journal of Finance*, 34(1). Origen del ratio de mínima varianza.
- Verificación local: revisa los requisitos de designación y documentación de coberturas y el tratamiento contable aplicable a tu institución.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 08 · Riesgo país y de contraparte](08-riesgo-pais-y-de-contraparte.md) | [Parte 11](../README.md) · [Programa](../../../SYLLABUS.md) | [10 · Riesgo operacional →](10-riesgo-operacional.md) |
<!-- gen:footer:end -->
