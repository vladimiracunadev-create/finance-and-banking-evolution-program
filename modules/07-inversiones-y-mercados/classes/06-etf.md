<!-- meta
part: 8
class: 6
title: "ETF y fondos indexados"
level: intermedio
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 06 · ETF y fondos indexados

> [← 05 · Fondos mutuos](05-fondos-mutuos.md) · [Índice de la parte](../README.md) · [07 · Divisas y commodities →](07-divisas-y-commodities.md)

**Parte 08 — Inversiones y mercados** · **Nivel:** Intermedio — requiere las partes anteriores · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Analizar el vehículo que ha transformado la industria de inversión: fondos que replican un índice y se
transan como una acción. Su ventaja de costo es real y verificable, y tienen riesgos propios —de
réplica, de liquidez y de estructura— que conviene entender antes de usarlos.

El fondo de la clase anterior se compra y se rescata con el emisor. Este se negocia en bolsa como una acción, y de ahí salen sus ventajas y sus riesgos propios: puede cotizar por encima o por debajo de lo que valen sus activos, y su forma de replicar el índice introduce riesgos que no son evidentes.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** un ETF de un fondo mutuo indexado y de un fondo tradicional.
2. **Explicar** el mecanismo de creación y rescate y por qué mantiene el precio alineado.
3. **Evaluar** un ETF con las siete variables que importan.
4. **Identificar** los riesgos de réplica sintética y de préstamo de valores.
5. **Calcular** el costo total de propiedad, incluidos los costos implícitos.

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

Los cuatro primeros términos son el vehículo y su mecánica de precio; los cuatro siguientes, sus formas de réplica y sus riesgos. La **réplica sintética** es la que hay que saber reconocer: replica el índice mediante un contrato con una contraparte, y eso añade un riesgo que la réplica física no tiene.

| Concepto | Comprensión verificable |
|---|---|
| `ETF` | Fondo que cotiza en bolsa y se transa como una acción durante la sesión. |
| `valor liquidativo (NAV)` | Valor de los activos del fondo por cuota. Se calcula al cierre. |
| `prima o descuento` | Diferencia entre el precio de mercado y el valor liquidativo. |
| `creación y rescate` | Mecanismo por el que participantes autorizados crean o eliminan cuotas, arbitrando la diferencia. |
| `réplica física` | El fondo posee los activos del índice. |
| `réplica sintética` | El fondo obtiene el rendimiento del índice mediante un contrato con una contraparte. |
| `error de seguimiento` | Desviación del rendimiento del fondo respecto de su índice. |
| `préstamo de valores` | El fondo presta sus activos a cambio de una comisión. Genera ingreso y riesgo de contraparte. |

## 🧠 Modelo mental

La diferencia clave con un fondo mutuo está en **cómo se compra y se vende**:

```text
fondo mutuo   compras y vendes a la administradora, al valor liquidativo del día
ETF           compras y vendes en bolsa, a otro inversionista, al precio de mercado
```

De ahí se derivan sus ventajas —negociación intradía, menor costo, transparencia diaria— y sus
riesgos: **el precio de mercado puede separarse del valor de los activos**, especialmente en momentos
de estrés.

## 📖 Desarrollo

### 1. Comparación de vehículos

El ETF se entiende mejor comparado con el fondo mutuo y con la compra directa. La tabla los enfrenta.

| Característica | Fondo mutuo tradicional | Fondo mutuo indexado | ETF |
|---|---|---|---|
| Gestión | Activa | Pasiva | Habitualmente pasiva |
| Comisión típica | 1,0–3,5 % | 0,3–0,9 % | 0,05–0,60 % |
| Negociación | Al valor liquidativo del día | Al valor liquidativo del día | Intradía, en bolsa |
| Transparencia de cartera | Periódica | Periódica | Habitualmente diaria |
| Monto mínimo | Variable | Variable | Una cuota |
| Costo de transacción | Habitualmente nulo | Habitualmente nulo | Comisión de corretaje + diferencial |
| Eficiencia tributaria | Depende del régimen | Depende del régimen | Suele ser mayor en algunos regímenes |

Consecuencia práctica: **para aportes pequeños y frecuentes, un fondo indexado sin comisión de
transacción puede ser mejor que un ETF barato**, porque la comisión de corretaje domina.

```text
aporte mensual de 100 000 · comisión de corretaje 3 500 por operación
costo de transacción anual = 42 000 = 3,5 % del aporte anual
→ supera cualquier ahorro de comisión de administración
```

### 2. Creación y rescate

El mecanismo que mantiene el precio cerca del valor de los activos es institucional y conviene conocerlo, porque explica cuándo deja de funcionar. El esquema lo recorre.

```text
si el ETF cotiza SOBRE su valor liquidativo (prima):
  un participante autorizado compra los activos del índice
  los entrega al fondo y recibe cuotas nuevas
  vende esas cuotas en el mercado, capturando la prima
  → la oferta aumenta y el precio baja hacia el valor liquidativo

si cotiza BAJO (descuento):
  compra cuotas en el mercado, las entrega al fondo
  recibe los activos y los vende
  → la demanda aumenta y el precio sube
```

Este arbitraje **mantiene el precio alineado con el valor de los activos**, y funciona bien mientras
el mercado subyacente sea líquido. Cuando no lo es —bonos corporativos en estrés, mercados emergentes
cerrados— **las primas y descuentos pueden ser significativos y persistentes**.

### 3. Las siete variables para evaluar un ETF

Siete datos deciden si un ETF sirve, y la comisión es solo uno de ellos. La tabla los recoge.

```text
1. índice replicado          ¿qué mide exactamente? ¿ponderado por capitalización, igual, por factor?
2. comisión de administración (TER)
3. error de seguimiento      diferencia anual respecto del índice
4. tamaño del fondo          los muy pequeños pueden cerrarse
5. volumen y diferencial     costo real de entrar y salir
6. método de réplica         física completa, física por muestreo o sintética
7. tratamiento de dividendos acumulación o distribución
```

Ejemplo comparado:

| | ETF A | ETF B | ETF C |
|---|---|---|---|
| Índice | Global desarrollado | Global desarrollado | Global desarrollado |
| Comisión | 0,20 % | 0,07 % | 0,12 % |
| Error de seguimiento | 0,08 % | 0,15 % | 0,05 % |
| Patrimonio | 8 400 M | 320 M | 41 000 M |
| Diferencial compra-venta | 0,04 % | 0,22 % | 0,02 % |
| Réplica | Física completa | Sintética | Física completa |
| Dividendos | Acumulación | Acumulación | Distribución |

Con esos datos se calcula el costo total de cada alternativa para un horizonte
concreto, y el orden resultante no es el que sugiere la comisión.

```text
costo total anual estimado (rotación baja, tenencia 5 años):
  A: 0,20 + 0,08 + 0,04/5 = 0,288 %
  B: 0,07 + 0,15 + 0,22/5 = 0,264 %
  C: 0,12 + 0,05 + 0,02/5 = 0,174 %

pese a tener la comisión más baja, B tiene mayor error de seguimiento
y un diferencial cinco veces mayor
C es el más barato en costo total, y además el más grande y líquido
```

**La comisión publicada no es el costo total.** El error de seguimiento y el diferencial pueden
superarla.

### 4. Riesgos específicos

**Réplica sintética:**

```text
el fondo NO posee los activos del índice
posee una cartera de garantía y un contrato de intercambio con una contraparte
que le entrega el rendimiento del índice

riesgo: si la contraparte incumple, el fondo depende de la garantía
mitigación: garantía sobrecolateralizada, múltiples contrapartes, reseteo diario
```

No es intrínsecamente malo —permite replicar mercados difíciles de acceder— y **debe conocerse**.

**Préstamo de valores:**

```text
el fondo presta sus acciones a terceros (habitualmente para venta corta)
recibe una comisión que reduce su costo efectivo
riesgo: si el prestatario incumple, el fondo depende de la garantía recibida
verificar: qué proporción de la cartera se presta, quién recibe el ingreso,
           qué garantía se exige
```

Punto que conviene revisar: **quién se queda con el ingreso del préstamo**. Algunos fondos lo
devuelven íntegro al partícipe; otros retienen una parte.

**Liquidez del subyacente:**

```text
un ETF puede ser muy líquido y su subyacente muy ilíquido
en estrés, el arbitraje de creación y rescate se dificulta
→ el ETF puede cotizar con descuento significativo respecto de su valor liquidativo

ejemplos documentados: ETF de bonos corporativos y de alto rendimiento
durante episodios de tensión de mercado
```

### 5. Costo total de propiedad

El costo real de un ETF suma comisión, error de seguimiento, horquilla y costos de operación. El cálculo siguiente lo obtiene.

```text
costo total = comisión de administración
            + error de seguimiento
            + diferencial compra-venta (amortizado por el periodo de tenencia)
            + comisión de corretaje (amortizada)
            + costo de conversión de moneda (si aplica)
            − ingreso por préstamo de valores devuelto al partícipe
            ± efecto tributario de la estructura
```

Sumados sobre una inversión y un horizonte concretos, los componentes revelan cuál pesa de verdad, que no suele ser la comisión anunciada.

```text
inversión de 12 000 000, tenencia de 7 años, ETF C:
  comisión           0,12 % × 7 = 0,84 %
  error seguimiento  0,05 % × 7 = 0,35 %
  diferencial        0,02 % × 2 (entrada y salida) = 0,04 %
  corretaje          7 000 × 2 / 12 000 000 = 0,12 %
  conversión moneda  0,30 % × 2 = 0,60 %   ← el mayor componente
  TOTAL                              1,95 % en 7 años = 0,28 % anual
```

**El costo de conversión de moneda resultó el mayor componente**, y no aparece en ninguna ficha del
ETF. Para inversión internacional desde una moneda local, ese costo debe incluirse siempre.

## 🧮 Ejemplo guiado

El ejemplo compara dos ETF sobre el mismo índice con las siete variables. La conclusión suele depender del error de seguimiento y no de la comisión.

**Situación.** Una persona quiere construir una cartera global de 30 000 000 con aportes mensuales de
350 000 y evalúa tres vías de implementación.

```text
VÍA 1  ETF internacionales comprados directamente en el extranjero
VÍA 2  fondo mutuo indexado local que invierte en el exterior
VÍA 3  ETF locales que replican índices internacionales
```

**Paso 1 — estructura de costos de cada vía.**

| Concepto | Vía 1 | Vía 2 | Vía 3 |
|---|---:|---:|---:|
| Comisión de administración | 0,10 % | 0,65 % | 0,45 % |
| Error de seguimiento | 0,05 % | 0,20 % | 0,18 % |
| Corretaje por operación | 8 000 | 0 | 3 200 |
| Diferencial | 0,03 % | — | 0,35 % |
| Conversión de moneda | 0,35 % por operación | Incluido en la comisión | Incluido |
| Custodia internacional | 0,10 % anual | 0 | 0 |

**Paso 2 — costo del aporte inicial de 30 000 000.**

```text
vía 1: conversión 105 000 + corretaje 8 000 + diferencial 9 000 = 122 000 (0,41 %)
vía 2: 0
vía 3: corretaje 3 200 + diferencial 105 000 = 108 200 (0,36 %)
```

**Paso 3 — costo de los aportes mensuales de 350 000.**

```text
vía 1: (350 000 × 0,0035) + 8 000 + (350 000 × 0,0003) = 1 225 + 8 000 + 105 = 9 330
       → 2,67 % de cada aporte  ← PROHIBITIVO mensualmente
       solución: acumular y aportar trimestral o semestralmente

vía 2: 0 → 0 % de cada aporte

vía 3: 3 200 + (350 000 × 0,0035) = 3 200 + 1 225 = 4 425
       → 1,26 % de cada aporte
```

**Paso 4 — costo anual recurrente.**

```text
vía 1: 0,10 % + 0,05 % + 0,10 % (custodia) = 0,25 %
vía 2: 0,65 % + 0,20 % = 0,85 %
vía 3: 0,45 % + 0,18 % = 0,63 %
```

**Paso 5 — proyección a 20 años (rentabilidad bruta 7,5 %).**

```text
                     vía 1        vía 2        vía 3
costo recurrente     0,25 %       0,85 %       0,63 %
costo de aportes     0,67 %*      0 %          1,26 %
patrimonio a 20 años 419 800 000  387 200 000  381 900 000

* asumiendo aportes trimestrales acumulados en lugar de mensuales
```

**Paso 6 — decisión considerando lo que el costo no captura.**

| Criterio | Vía 1 | Vía 2 | Vía 3 |
|---|---|---|---|
| Costo total a 20 años | Menor | Medio | Mayor |
| Complejidad operativa | **Alta** | Baja | Media |
| Tratamiento tributario | Puede exigir declaración de activos en el exterior | Simple | Simple |
| Riesgo de custodia | Intermediario extranjero | Local | Local |
| Trámite sucesorio | Complejo si es en el extranjero | Simple | Simple |
| Requiere disciplina | Aportes trimestrales, no mensuales | Automático | Trimestral |

```text
DECISIÓN RECOMENDADA: combinación

  · aportes mensuales automáticos a la vía 2 (fondo indexado local, costo de aporte cero)
  · una vez al año, traspaso del acumulado a la vía 1, con conversión y corretaje únicos
  
  costo del aporte anual consolidado: 122 000 sobre 4 200 000 = 2,9 %... 
  → aún alto; conviene consolidar cada 2 años

  ALTERNATIVA MÁS SIMPLE Y DEFENDIBLE:
  todo en la vía 2, aceptando 0,60 puntos anuales adicionales de costo
  a cambio de simplicidad operativa, tributaria y sucesoria
  
  diferencia a 20 años: 32 600 000 (7,8 % del patrimonio final)
  ¿vale la simplicidad 32,6 millones? es una decisión personal, y debe tomarse
  con el número a la vista, no por defecto
```

**Interpreta:** la vía más barata en comisión resultó la más cara en costos de aporte y la más compleja
en operación, tributación y sucesión. **La decisión correcta depende del monto, de la frecuencia de
aporte y de la tolerancia a la complejidad**, y presentar el costo de la simplicidad —32,6 millones—
permite tomarla con información en lugar de por comodidad.

## 🏦 Del cliente al banco

El cliente compra un ETF y el banco lo intermedia y a veces también lo emite. La tabla enfrenta las dos lecturas.

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| Creación y rescate | Rol del banco como participante autorizado | 8, clase 2 |
| Préstamo de valores | Negocio de custodia y de mesa | 10, clase 12 |
| ETF en carteras institucionales | Instrumento de gestión táctica | 8, clase 10 |
| Descuento en estrés | Riesgo de liquidez de la cartera | 11, clase 4 |
| Costo de conversión | Ingreso de la mesa de cambios | 10, clase 13 |

## 🧪 Práctica

El laboratorio pide evaluar tres ETF sobre el mismo índice y calcular su costo total de propiedad. El orden por comisión y el orden por costo total no coinciden.

En `labs/lab-03.md`, sección de ETF:

1. Evalúa tres ETF del mismo índice con las siete variables.
2. Calcula el costo total de propiedad de cada uno para un horizonte de 7 años.
3. Investiga el método de réplica y la política de préstamo de valores de dos ETF.
4. Compara tres vías de implementación de una cartera global con aportes periódicos.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen ETF que no siguieron a su índice. Las causas son el error de seguimiento y las primas o descuentos en momentos de tensión.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se elige por la comisión más baja | Costo total ignorado | Suma error de seguimiento, diferencial y conversión. |
| Aportes mensuales pequeños a un ETF | Corretaje domina | Acumula y aporta con menor frecuencia, o usa fondo indexado. |
| Se ignora el método de réplica | Riesgo de contraparte desconocido | Verifica si es física o sintética. |
| Se compra un ETF de subyacente ilíquido | Descuento en estrés | Evalúa la liquidez del mercado subyacente. |
| Se omite el costo de conversión de moneda | No aparece en la ficha | Inclúyelo: suele ser el mayor componente. |
| Se compra un ETF muy pequeño | Riesgo de cierre | Prefiere fondos con patrimonio relevante. |

## ❓ Preguntas de comprobación

1. ¿Cómo mantiene el mecanismo de creación y rescate el precio alineado con el valor liquidativo?
2. ¿Por qué un ETF de comisión 0,07 % puede ser más caro que uno de 0,12 %?
3. ¿Qué riesgo introduce la réplica sintética y cómo se mitiga?
4. ¿Cuándo un fondo indexado es preferible a un ETF más barato?
5. ¿Qué componente del costo total suele omitirse en inversión internacional?

## 📥 Entregable

Guarda en `portfolio/parte-08/clase-06/`:

- la evaluación de tres ETF del mismo índice con las siete variables;
- el costo total de propiedad de cada uno a 7 años;
- la investigación del método de réplica y del préstamo de valores de dos ETF;
- la comparación de tres vías de implementación con su decisión justificada.

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

- Bodie, Z., Kane, A. y Marcus, A. (2023). *Investments* (13.ª ed.). McGraw-Hill. Capítulo 4: fondos cotizados y su estructura.
- Bogle, J. (2017). *The Little Book of Common Sense Investing*. Wiley. Fundamento de la inversión indexada.
- IOSCO (2013). *Principles for the Regulation of Exchange Traded Funds*. Riesgos de réplica sintética y de préstamo de valores. <https://www.iosco.org/>
- Bank for International Settlements (2018). *The implications of passive investing for securities markets*. BIS Quarterly Review. Efectos de la gestión pasiva sobre la liquidez y la formación de precios. <https://www.bis.org/publ/qtrpdf/r_qt1803j.htm>
- Financial Stability Board (2022). *Liquidity in Core Government Bond Markets*. Comportamiento de ETF de renta fija en estrés. <https://www.fsb.org/2022/10/liquidity-in-core-government-bond-markets/>
- Verificación local: revisa el tratamiento tributario de ETF extranjeros en tu país y las obligaciones de declaración de activos en el exterior.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 05 · Fondos mutuos](05-fondos-mutuos.md) | [Parte 08](../README.md) · [Programa](../../../SYLLABUS.md) | [07 · Divisas y commodities →](07-divisas-y-commodities.md) |
<!-- gen:footer:end -->
