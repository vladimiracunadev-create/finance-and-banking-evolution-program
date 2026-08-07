---
part: 1
class: 8
title: "Valor del dinero en el tiempo"
level: fundamento
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 08 · Valor del dinero en el tiempo

> [← 07 · Inflación y poder adquisitivo](07-inflacion-y-poder-adquisitivo.md) · [Índice de la parte](../README.md) · [09 · Valor presente →](09-valor-presente.md)

**Parte 01 — Matemática financiera básica** · **Nivel:** Fundamento — sin conocimientos previos · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Formalizar el principio que sostiene todas las finanzas: **un peso hoy vale más que un peso mañana**,
y por lo tanto sumar cantidades ubicadas en momentos distintos es matemáticamente inválido. Esta
clase entrega la herramienta que hace comparables flujos de distintas fechas —el eje de tiempo y la
tasa de descuento— y prepara las clases 9 y 10, que son su aplicación mecánica.

Las clases 5 a 7 dieron las tres piezas —el precio del tiempo, la capitalización y la pérdida de poder adquisitivo—. Esta las junta en un solo principio y en una sola herramienta. El principio es que dos cantidades en momentos distintos no se pueden sumar; la herramienta es el eje de tiempo, que a partir de aquí se usa en todo el programa hasta la última clase.

## 📚 Objetivos

Al finalizar podrás:

1. **Justificar** por qué un peso hoy vale más, con las tres razones económicas que lo explican.
2. **Dibujar** un eje de tiempo correcto con flujos, signos y punto de vista declarado.
3. **Trasladar** cualquier flujo hacia adelante o hacia atrás en el tiempo.
4. **Comparar** dos alternativas llevándolas a una fecha focal común.
5. **Elegir** una tasa de descuento y defender esa elección.

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

Los tres primeros términos son de método y los cuatro últimos de operación. La **fecha focal** es la que más resistencia genera, porque parece un tecnicismo y es lo que hace comparable una decisión: mientras no se elige un momento al que traer todos los flujos, cualquier comparación entre alternativas es aritmética sin sentido.

| Concepto | Comprensión verificable |
|---|---|
| `valor temporal del dinero` | Principio: el mismo monto tiene valores distintos según cuándo ocurra. Tres causas: costo de oportunidad, inflación y riesgo. |
| `eje de tiempo` | Recta con los periodos numerados desde 0 y los flujos con su signo. Es la herramienta de trabajo, no un adorno didáctico. |
| `fecha focal` | Momento al que se llevan todos los flujos para poder compararlos. Cualquier fecha sirve **si es la misma para todos**. |
| `capitalizar` | Mover un flujo hacia el futuro: `× (1+i)^n`. |
| `descontar` | Mover un flujo hacia el pasado: `÷ (1+i)^n`. |
| `tasa de descuento` | Rendimiento de la mejor alternativa de riesgo comparable. No es un dato del problema: es una decisión que debe justificarse. |
| `equivalencia financiera` | Dos conjuntos de flujos son equivalentes si tienen el mismo valor en una fecha focal, con una tasa dada. |

## 🧠 Modelo mental

Cada flujo vive en una "moneda distinta" según su fecha:

```text
100 000 en el mes 0     ≠     100 000 en el mes 12
```

Convertir entre esas monedas exige un "tipo de cambio temporal", que es exactamente `(1 + i)^n`. Con
esa imagen, el error de sumar flujos de fechas distintas se vuelve tan visible como sumar dólares
con pesos sin convertir.

## 📖 Desarrollo

### 1. Las tres razones

El dinero vale distinto en momentos distintos por tres razones independientes, y conviene separarlas porque cada una responde a un problema diferente. La tabla las enfrenta con lo que ocurriría si esa razón desapareciera, que es la forma más rápida de entender qué aporta cada una.

| Razón | Qué dice | Qué pasa si desaparece |
|---|---|---|
| **Costo de oportunidad** | El peso de hoy puede invertirse y producir | Si no hubiera alternativas de inversión, la tasa sería 0 |
| **Inflación** | El peso de mañana compra menos (clase 7) | Con inflación 0, aún quedan las otras dos razones |
| **Riesgo** | El peso prometido para mañana puede no llegar | Con certeza absoluta, la prima de riesgo sería 0 |

La tasa de descuento incorpora las tres. Cuando en la Parte 13, clase 6, calcules un costo de
capital, estarás poniendo un número a cada una de estas tres líneas.

### 2. El eje de tiempo

El eje de tiempo es la herramienta central de todo lo que queda de programa, y su valor está en obligar a declarar dos cosas que se suelen dar por supuestas: desde qué punto de vista se mira la operación y con qué tasa se mueve el dinero.

```text
punto de vista: el inversionista · tasa 10 % anual

  0        1        2        3        4
  |--------|--------|--------|--------|
 −500      +150     +150     +150     +250
```

Reglas del eje que evitan la mayoría de los errores:

1. El periodo `0` es **hoy**, no "el primer año".
2. Un flujo en el periodo `1` ocurre al **final** del primer periodo.
3. Los signos son consistentes con un único punto de vista declarado.
4. Los periodos son de igual duración; si no lo son, se subdivide.

### 3. Mover flujos

Solo hay dos movimientos posibles sobre el eje y son inversos entre sí. Todo el resto de las finanzas —valoración, crédito, proyectos, instrumentos— es alguna combinación de estos dos.

```text
hacia el futuro (capitalizar)     F = P (1+i)^n
hacia el pasado (descontar)       P = F / (1+i)^n
```

Llevando los flujos del eje anterior a la fecha focal `t = 4`, con `i = 10 %`:

| Flujo | Periodo | Traslado | Valor en t=4 |
|---:|---:|---|---:|
| −500 | 0 | `× 1,10⁴` | −732,05 |
| +150 | 1 | `× 1,10³` | +199,65 |
| +150 | 2 | `× 1,10²` | +181,50 |
| +150 | 3 | `× 1,10¹` | +165,00 |
| +250 | 4 | `× 1,10⁰` | +250,00 |
| | | **Total** | **+64,10** |

El proyecto genera 64,10 más de lo que costaría haber puesto los 500 al 10 %. Ese número, llevado a
`t = 0`, es el valor actual neto de la Parte 7, clase 8: `64,10 / 1,10⁴ = 43,78`.

### 4. La fecha focal no cambia la decisión

Mismo caso, fecha focal en `t = 0`:

| Flujo | Periodo | Traslado | Valor en t=0 |
|---:|---:|---|---:|
| −500 | 0 | `× 1` | −500,00 |
| +150 | 1 | `÷ 1,10` | +136,36 |
| +150 | 2 | `÷ 1,10²` | +123,97 |
| +150 | 3 | `÷ 1,10³` | +112,70 |
| +250 | 4 | `÷ 1,10⁴` | +170,75 |
| | | **Total** | **+43,78** |

```text
43,78 × 1,10⁴ = 64,10   ✔
```

**Ambas fechas focales dan la misma conclusión.** Elegir `t = 0` es convención porque el decisor está
hoy y porque permite comparar proyectos de distinta duración.

### 5. Elegir la tasa de descuento

Es la decisión más discutida y la menos documentada de los informes financieros. Criterios:

| Contexto | Tasa razonable | Justificación |
|---|---|---|
| Persona con deuda de consumo al 24 % | 24 % | Prepagar deuda es su mejor alternativa de igual riesgo |
| Persona sin deuda, perfil conservador | Tasa de depósito a plazo | Alternativa efectivamente disponible |
| Empresa evaluando un proyecto de su giro | Costo promedio ponderado de capital | Parte 13, clase 6 |
| Banco evaluando una colocación | Costo de fondos + prima de riesgo + capital | Parte 15, clase 7 |

Regla práctica: **si no puedes nombrar la alternativa concreta que la tasa representa, la tasa está
inventada**. Y una tasa inventada convierte cualquier evaluación en una opinión con decimales.

## 🧮 Ejemplo guiado

El ejemplo se resuelve moviendo cada flujo por separado hasta la fecha focal. Conviene no adelantar la suma: sumar antes de traer todos los flujos al mismo momento es exactamente el error que la clase persigue.

**Situación.** A Sofía le ofrecen vender su motocicleta con tres formas de pago. Su alternativa real
es un depósito que rinde 0,55 % mensual (6,8 % efectivo anual).

```text
A  1 900 000 al contado hoy
B  700 000 hoy + 700 000 en 6 meses + 700 000 en 12 meses
C  2 200 000 en 12 meses
```

**Paso 1 — declara la tasa y la fecha focal.** Tasa: 0,55 % mensual, porque es la alternativa que
Sofía efectivamente tiene. Fecha focal: `t = 0`.

**Paso 2 — opción A.**

```text
VA(A) = 1 900 000
```

**Paso 3 — opción B.**

```text
700 000
700 000 / (1,0055)^6  = 700 000 / 1,033520 = 677 297
700 000 / (1,0055)^12 = 700 000 / 1,068164 = 655 328
VA(B) = 700 000 + 677 297 + 655 328 = 2 032 625
```

**Paso 4 — opción C.**

```text
VA(C) = 2 200 000 / 1,068164 = 2 059 604
```

**Paso 5 — ordena.**

| Opción | Valor actual | Diferencia vs. A |
|---|---:|---:|
| C | 2 059 604 | +159 604 |
| B | 2 032 625 | +132 625 |
| A | 1 900 000 | — |

**Paso 6 — verifica con otra fecha focal (`t = 12`).**

```text
A  1 900 000 × 1,068164 = 2 029 512
B  700 000×1,068164 + 700 000×1,033520 + 700 000 = 2 171 177
C  2 200 000
orden: C > B > A   ✔ mismo orden
```

**Paso 7 — interpreta con los límites correctos.** Financieramente C es la mejor, pero el cálculo
supone que **el comprador paga**. La diferencia entre C y A es de 159 604 pesos, un 8,4 %: esa es la
prima que Sofía cobra por asumir riesgo de crédito durante un año sin garantía ni evaluación. Si
estima que hay más de un 8 % de probabilidad de impago, A es mejor. La matemática ordena las
opciones; el riesgo decide (Parte 11, clase 2).

## 🏦 Del cliente al banco

El cliente compara cifras y el banco compara valores presentes. La tabla enfrenta las dos lecturas y muestra por qué una oferta que parece mejor en pesos totales puede ser peor una vez traída al mismo momento.

| Decisión cotidiana | Mecanismo | Dónde se profundiza |
|---|---|---|
| ¿Contado o en cuotas sin interés? | Comparar valores actuales; "sin interés" rara vez lo es | Parte 3, clase 13 |
| ¿Prepago mi crédito o invierto? | La tasa de descuento correcta es la tasa de tu deuda | Parte 2, clase 8 |
| ¿Acepto pago diferido de un cliente? | Valor actual menos probabilidad de impago | Parte 13, clase 2 |
| ¿Vale la pena este proyecto? | VAN con tasa justificada | Parte 7, clase 8 |

## 🧪 Práctica

El laboratorio pide comparar alternativas cuyos flujos totales son iguales y cuyos calendarios no lo son. La respuesta intuitiva —que valen lo mismo— es la equivocada, y comprobarlo con el eje de tiempo es lo que instala el principio de esta clase.

En `labs/lab-04.md`, sección de equivalencia:

1. Dibuja el eje de tiempo de tres alternativas de pago reales y resuélvelas en dos fechas focales.
2. Demuestra numéricamente que la elección de fecha focal no altera el orden.
3. Justifica por escrito tu tasa de descuento nombrando la alternativa concreta.
4. Calcula la tasa de indiferencia entre dos opciones (aquella que las iguala).

## ⚠️ Errores frecuentes

Los síntomas de la tabla se reconocen porque producen comparaciones que no cuadran con la intuición financiera. La causa suele ser una sola: se sumaron cantidades de momentos distintos sin traerlas antes a una fecha común.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se suman flujos de distintas fechas | No se llevó todo a una fecha focal | Traslada primero, suma después. Siempre. |
| El resultado cambia según la fecha focal | Error aritmético o tasas distintas por flujo | Con una tasa única, el orden es invariante; revisa el cálculo. |
| Un flujo del "primer año" se pone en el periodo 0 | Confusión entre inicio y fin de periodo | El periodo 0 es hoy; el flujo de fin del primer año va en 1. |
| La tasa de descuento no se justifica | Se tomó un número redondo | Nombra la alternativa concreta que representa la tasa. |
| "Cuotas sin interés" parece igual al contado | No se descontó | Descuenta las cuotas: casi siempre el contado con descuento gana. |
| Se descuenta con tasa anual un flujo mensual | Unidades incompatibles | Convierte la tasa a la periodicidad del flujo (Parte 7, clase 3). |

## ❓ Preguntas de comprobación

1. Nombra las tres razones por las que un peso hoy vale más que uno mañana.
2. ¿Por qué la elección de la fecha focal no altera la decisión?
3. ¿Qué tasa de descuento debería usar alguien con una deuda de tarjeta al 40 % anual y por qué?
4. Un flujo ocurre al final del tercer año. ¿En qué periodo del eje se ubica?
5. ¿Qué información adicional a la matemática necesitas para elegir entre pago al contado y pago diferido?

## 📥 Entregable

Guarda en `portfolio/parte-01/clase-08/`:

- los ejes de tiempo dibujados de tres alternativas;
- la resolución en dos fechas focales con la demostración de invariancia;
- la justificación escrita de tu tasa de descuento;
- la tasa de indiferencia calculada y su interpretación.

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

- Brealey, R., Myers, S. y Allen, F. (2023). *Principios de finanzas corporativas* (14.ª ed.). McGraw-Hill. Capítulo 2: valor presente y el principio del valor temporal del dinero.
- Ross, S., Westerfield, R. y Jordan, B. (2022). *Fundamentos de finanzas corporativas* (12.ª ed.). McGraw-Hill. Capítulo 4: valuación descontada y ejes de tiempo.
- Blank, L. y Tarquin, A. (2018). *Ingeniería económica* (8.ª ed.). McGraw-Hill. Capítulos 2 y 3: equivalencia financiera y fecha focal.
- Damodaran, A. (2012). *Investment Valuation* (3.ª ed.). Wiley. Capítulo 2: elección y justificación de la tasa de descuento.
- Kellison, S. (2008). *The Theory of Interest* (3.ª ed.). McGraw-Hill/Irwin. Capítulo 2: ecuaciones de valor y fecha de comparación.
- Verificación local: usa como tasa de referencia la tasa de captación vigente publicada por el banco central o el supervisor de tu país, registrando fecha y fuente.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 07 · Inflación y poder adquisitivo](07-inflacion-y-poder-adquisitivo.md) | [Parte 01](../README.md) · [Programa](../../../SYLLABUS.md) | [09 · Valor presente →](09-valor-presente.md) |
<!-- gen:footer:end -->
