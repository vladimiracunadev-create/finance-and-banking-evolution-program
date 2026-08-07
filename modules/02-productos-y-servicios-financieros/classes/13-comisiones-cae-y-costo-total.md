---
part: 3
class: 13
title: "Comisiones, CAE y costo total"
level: intermedio
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 13 · Comisiones, CAE y costo total

> [← 12 · Seguros asociados a productos financieros](12-seguros-asociados.md) · [Índice de la parte](../README.md) · [14 · Proyecto: comparador de productos →](14-proyecto-comparador-de-productos.md)

**Parte 03 — Productos y servicios financieros** · **Nivel:** Intermedio — requiere las partes anteriores · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Consolidar el indicador que hace comparables productos con estructuras distintas: el costo total
expresado como tasa anual equivalente. Esta clase es la síntesis técnica de la parte: enseña a
calcular la carga anual equivalente desde cero, a entender qué incluye y qué no, y a detectar cuándo
un producto barato en apariencia resulta el más caro.

## 📚 Objetivos

Al finalizar podrás:

1. **Calcular** la tasa que iguala el monto recibido con el flujo completo de pagos.
2. **Explicar** qué incluye y qué excluye la carga anual equivalente normativa.
3. **Comparar** productos con estructuras distintas sobre una base común.
4. **Identificar** las comisiones más frecuentes y cuáles son negociables.
5. **Auditar** una oferta detectando costos no informados.

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
| `carga anual equivalente (CAE)` | Tasa anual que iguala el valor presente de todos los pagos con el monto recibido. Es el indicador comparable por excelencia. |
| `monto recibido` | Base del cálculo. Si hay cargos financiados o interés anticipado, es menor al capital firmado. |
| `flujo del crédito` | Todos los pagos en sus fechas: cuotas, seguros, comisiones periódicas y pago final. |
| `tasa interna de retorno` | El método matemático detrás de la CAE. Se resuelve por iteración. |
| `costos excluidos` | Notaría, tasación e impuestos suelen quedar fuera de la CAE normativa aunque sean desembolsos reales. |
| `comisión negociable` | Apertura, administración y prepago suelen tener margen; los impuestos no. |

## 🧠 Modelo mental

La CAE responde a una sola pregunta:

```text
si este crédito fuera un depósito, ¿a qué tasa tendría que estar
para que sus flujos me costaran exactamente lo mismo?
```

Por eso permite comparar un crédito de 36 cuotas con uno de 24 y comisión distinta: los reduce a un
único número anual. Y por eso su cálculo exige el **flujo completo**, no la tasa del contrato.

## 📖 Desarrollo

### 1. El cálculo, paso a paso

```text
se busca la tasa i tal que:

  monto recibido = Σ  pagoₜ / (1 + i)^t
```

Crédito de 3 000 000 con comisión de apertura de 45 000 financiada, 24 cuotas de 152 400 (incluye
seguro de 4 300):

```text
monto recibido = 3 000 000
flujo = 24 pagos de 152 400
```

Resolviendo por bisección (Parte 1, clase 14):

| i mensual | Valor presente de los pagos |
|---:|---:|
| 1,20 % | 3 155 000 |
| 1,60 % | 3 020 000 |
| 1,70 % | 2 988 000 |
| **1,66 %** | **3 000 800** |

```text
i mensual ≈ 1,66 %
CAE = (1,0166)^12 − 1 = 21,84 % anual
tasa del contrato                      1,35 % mensual = 17,45 % anual
brecha                                 4,39 puntos porcentuales
```

### 2. Qué incluye y qué no

| Concepto | ¿Entra en la CAE? |
|---|---|
| Interés | Sí |
| Comisión de apertura | Sí |
| Seguros exigidos por el acreedor | Sí |
| Comisión de administración mensual | Sí |
| Impuesto de timbres | Depende de la jurisdicción |
| Notaría e inscripción | Habitualmente **no** |
| Tasación | Habitualmente **no** |
| Comisión de prepago | No (es eventual) |
| Gastos de cobranza por mora | No (es eventual) |

Consecuencia práctica: **la CAE es el mejor indicador disponible y aun así subestima el desembolso
real** en operaciones con gastos operacionales altos, como el hipotecario. Por eso la comparación
completa suma la CAE **más** los gastos excluidos expresados como monto.

### 3. Catálogo de comisiones y su margen de negociación

| Comisión | Frecuencia | ¿Negociable? | Comentario |
|---|---|---|---|
| Apertura / originación | Una vez | **Alta** | Suele eliminarse con cotización competidora |
| Administración | Mensual | Media | A veces se exime por antigüedad o convenio |
| Mantención de cuenta | Mensual | Media | Exención por saldo o convenio |
| Avance en efectivo | Por operación | Baja | Estructural del producto |
| Prepago | Eventual | Baja | Tope legal en muchas jurisdicciones |
| Cobranza | Eventual | Baja | Regulada por tramos |
| Emisión de estado de cuenta en papel | Mensual | **Alta** | Se elimina optando por formato digital |
| Renovación de línea | Anual | Media | Se elimina cerrando cupos no usados |

### 4. Comparar estructuras distintas

Tres ofertas para financiar 6 000 000:

| | A: crédito 36 m | B: crédito 24 m | C: tarjeta en 12 cuotas |
|---|---:|---:|---:|
| Tasa contrato | 1,25 % mensual | 1,55 % mensual | "sin interés" |
| Comisión | 90 000 | 0 | 0 |
| Seguro mensual | 5 100 | 5 100 | 0 |
| Cuota | 209 700 | 297 800 | 541 700 |
| Pagos totales | 7 549 200 | 7 147 200 | 6 500 400 |
| Precio contado equivalente | 6 000 000 | 6 000 000 | 6 000 000 |
| **CAE** | **20,1 %** | **21,6 %** | **16,4 %** |

La opción C —"sin interés"— tiene la CAE más baja porque el recargo sobre el precio contado es menor
que el interés de las otras dos. Pero exige una cuota de 541 700, más del doble que A. **La CAE ordena
por costo; el flujo decide la viabilidad.** Ambas dimensiones son necesarias.

### 5. Auditar una oferta

```text
1. pide el monto que se depositará en tu cuenta (no el capital firmado)
2. pide la tabla de desarrollo completa con cuota desglosada
3. verifica que la suma de cuotas coincida con lo informado
4. calcula tú la CAE y compárala con la informada
5. lista los gastos excluidos y súmalos aparte
6. exige por escrito qué seguros son exigibles
```

Si la CAE que calculas difiere en más de 0,3 puntos de la informada, hay un concepto que no está en tu
flujo: pregunta cuál antes de firmar.

## 🧮 Ejemplo guiado

**Situación.** Un cliente compara dos hipotecarios por 2 400 UF a 20 años.

```text
Banco A  tasa 4,10 % · comisión 0 · desgravamen 0,40 UF/mes · incendio 0,30 UF/mes
         gastos operacionales 58 UF
Banco B  tasa 4,45 % · comisión 12 UF · desgravamen 0,28 UF/mes · incendio 0,22 UF/mes
         gastos operacionales 41 UF
```

**Paso 1 — cuota base.**

```text
A  i mensual = (1,041)^(1/12) − 1 = 0,003354
   cuota = 2 400 × 0,003354 × (1,003354)^240 / ((1,003354)^240 − 1) = 14,63 UF
B  i mensual = (1,0445)^(1/12) − 1 = 0,003635
   cuota = 15,13 UF
```

**Paso 2 — dividendo total.**

```text
A  14,63 + 0,40 + 0,30 = 15,33 UF
B  15,13 + 0,28 + 0,22 = 15,63 UF
```

**Paso 3 — CAE de cada uno** (monto recibido = 2 400 UF para A; 2 388 UF para B, por la comisión).

```text
A  i que iguala 2 400 con 240 pagos de 15,33 → 0,003876 mensual → CAE 4,75 %
B  i que iguala 2 388 con 240 pagos de 15,63 → 0,004030 mensual → CAE 4,94 %
```

**Paso 4 — suma los gastos excluidos.**

| | Pagos totales (UF) | Gastos operacionales | **Desembolso total** |
|---|---:|---:|---:|
| A | 3 679,2 | 58 | **3 737,2** |
| B | 3 751,2 | 41 | **3 792,2** |

**Paso 5 — decide.** A es mejor por CAE (4,75 % vs. 4,94 %) y por desembolso total (55 UF menos, unos
2,1 millones). El menor gasto operacional de B no compensa su mayor tasa.

**Paso 6 — verifica el orden con un contrafactual.** ¿Qué pasaría si B redujera su tasa a 4,20 %?

```text
cuota base B = 14,68 UF; dividendo total = 15,18 UF
CAE B ≈ 4,72 %; desembolso total = 3 643,2 + 41 = 3 684,2 UF
→ B pasaría a ser mejor por 53 UF
```

**Interpreta:** la diferencia entre las dos ofertas se juega en **35 puntos base de tasa**, no en las
comisiones ni en los seguros. Saber qué variable manda permite negociar lo que importa: pedir rebaja
de tasa vale, en este caso, casi cuarenta veces más que pedir rebaja de comisión.

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| CAE informada | Obligación normativa de divulgación | 12, clase 4 |
| Comisión de apertura | Ingreso inmediato que mejora el retorno del año 1 | 15, clase 3 |
| Cliente que compara CAE | Presión competitiva directa sobre el margen | 15, clase 7 |
| Gastos excluidos | No forman parte del ingreso del banco | 15, clase 3 |

## 🧪 Práctica

En `labs/lab-06.md`, sección de costo total:

1. Calcula la CAE de un crédito real desde su flujo, sin usar la informada.
2. Compara tu resultado con la CAE declarada y explica cualquier diferencia.
3. Construye la comparación de tres estructuras distintas sobre base común.
4. Lista los gastos excluidos de tu operación y súmalos al desembolso total.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| La CAE calculada no coincide con la informada | Falta un concepto en el flujo | Pide el desglose completo de la cuota. |
| Se compara CAE de productos con plazos muy distintos | La CAE no captura el esfuerzo mensual | Compara CAE **y** cuota respecto del flujo. |
| Se ignoran notaría y tasación | Están excluidas de la CAE | Súmalas aparte al desembolso total. |
| Se negocia la comisión y no la tasa | No se identificó la variable dominante | Calcula qué variable mueve más el resultado. |
| "Sin interés" se asume sin costo | El recargo está en el precio | Compara contra el precio contado. |
| Se acepta la CAE sin verificarla | Confianza sin control | Recalcula: son cinco minutos. |

## ❓ Preguntas de comprobación

1. ¿Qué pregunta responde la CAE y por qué permite comparar estructuras distintas?
2. ¿Qué conceptos quedan habitualmente fuera de la CAE y cómo se incorporan al análisis?
3. Calcula la CAE de un crédito de 2 000 000 con 12 cuotas de 190 000.
4. ¿Por qué la oferta de menor CAE no siempre es la elegible?
5. ¿Cómo determinas qué variable conviene negociar en una oferta concreta?

## 📥 Entregable

Guarda en `portfolio/parte-03/clase-13/`:

- el cálculo propio de la CAE de un crédito real, con el método documentado;
- la comparación contra la CAE informada y la explicación de la diferencia;
- la comparación de tres estructuras sobre base común;
- la lista de gastos excluidos y el desembolso total corregido.

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

- Ross, S., Westerfield, R. y Jordan, B. (2022). *Fundamentos de finanzas corporativas* (12.ª ed.). McGraw-Hill. Capítulo 6: tasa efectiva anual y tasa interna de retorno de un préstamo.
- Broverman, S. (2017). *Mathematics of Investment and Credit* (7.ª ed.). ACTEX. Capítulo 2: rendimiento de flujos y métodos de iteración.
- World Bank (2017). *Good Practices for Financial Consumer Protection*. Banco Mundial. Estándar de divulgación del costo total del crédito.
- European Union (2008). *Directive 2008/48/EC on credit agreements for consumers*. Definición y fórmula de la tasa anual equivalente (TAE). <https://eur-lex.europa.eu/>
- Consumer Financial Protection Bureau. *Truth in Lending Act (Regulation Z)*. Metodología de cálculo de la APR estadounidense.
- Verificación local: revisa la fórmula normativa de la CAE de tu país y qué conceptos incluye (en Chile, el reglamento de la Ley 20.555).

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 12 · Seguros asociados a productos financieros](12-seguros-asociados.md) | [Parte 03](../README.md) · [Programa](../../../SYLLABUS.md) | [14 · Proyecto: comparador de productos →](14-proyecto-comparador-de-productos.md) |
<!-- gen:footer:end -->
