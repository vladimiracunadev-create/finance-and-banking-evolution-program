<!-- meta
part: 21
class: 13
title: "Creación de mercado automatizada"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [formacion-de-precio, liquidez, riesgo-de-modelo]
regulation_last_verified: 2026-08-20
regulatory_status: vigente
primary_authorities: [IOSCO, BIS, FSB]
requires_legal_review: false
-->

<!-- gen:header:start -->
# Clase 13 · Creación de mercado automatizada

> [← 12 · Pago contra pago y riesgo de liquidación](12-pago-contra-pago-y-riesgo-de-liquidacion.md) · [Índice de la parte](../README.md) · [14 · Colateral y garantías tokenizadas →](14-colateral-y-garantias-tokenizadas.md)

**Parte 21 — Tokenización, FX on-chain y mercados programables** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Entender el mecanismo que sustituye al libro de órdenes cuando no hay
contrapartes esperando: **una fórmula que fija el precio según los saldos de dos
reservas**. Y calcular quién paga por que funcione.

Las clases anteriores suponen que hay contrapartida. Esta trata el mecanismo que la garantiza siempre mediante una fórmula, y calcula su coste real para quien provee la liquidez.

## 📚 Objetivos

Al finalizar podrás:

1. **Explicar** cómo una fórmula de producto constante fija un precio.
2. **Calcular** el precio y el impacto de una operación de tamaño dado.
3. **Cuantificar** la pérdida por divergencia de quien aporta las reservas.
4. **Comparar** este mecanismo con un libro de órdenes en profundidad y coste.
5. **Determinar** cuándo aportar reservas compensa y cuándo no.

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

Los cuatro primeros términos son la mecánica de la reserva y sus dos precios; los cuatro siguientes, el coste para quien provee liquidez. La **pérdida por divergencia** es el concepto que hay que entender antes de proveer liquidez: cuando el precio se mueve, la reserva termina con más del activo que baja y menos del que sube.

| Concepto | Comprensión verificable |
|---|---|
| `reserva` | Saldo de un activo que sostiene el mecanismo |
| `producto constante` | Regla que mantiene fijo el producto de las reservas |
| `precio marginal` | El de la siguiente unidad infinitesimal |
| `precio efectivo` | El medio realmente obtenido en la operación |
| `pérdida por divergencia` | Diferencia entre aportar reservas y conservar los activos |
| `comisión de operación` | Lo que cobra el mecanismo por cada cambio |
| `arbitraje` | Operación que devuelve el precio al del mercado externo |
| `deslizamiento` | Diferencia entre el precio esperado y el obtenido |

## 🧠 Modelo mental

El modelo mental es una fórmula que cotiza sin opinar: la reserva ofrece precio según una regla matemática, y por eso siempre hay contrapartida y siempre hay deslizamiento. Cuanto mayor la operación respecto de la reserva, peor el precio efectivo.

```text
LA IDEA

  dos reservas, X del activo A y Y del activo B
  la regla mantiene X × Y = K constante

  para llevarse ΔY del activo B hay que
  entregar el ΔX que mantenga el producto

  → el precio sale de la fórmula,
    no de una contraparte

QUÉ RESUELVE
  no hace falta que alguien esté esperando
  al otro lado: siempre hay precio

QUÉ CUESTA
  · el precio se aleja del externo y hay que
    esperar a que alguien arbitre
  · quien aporta las reservas acaba con
    MÁS del activo que baja y MENOS del que sube
  → esa es la pérdida por divergencia,
    y es estructural, no un accidente
```

## 📖 Desarrollo

### 1. El cálculo del precio

El mecanismo se apoya en una fórmula que cabe en tres líneas, y todo lo demás
se deriva de ella. El bloque la desarrolla y distingue el precio marginal del
precio efectivamente pagado.

```text
RESERVAS X e Y, PRODUCTO K = X × Y

  entregar Δx de A para recibir Δy de B:

  (X + Δx) × (Y − Δy) = K

  Δy = Y − K / (X + Δx)

PRECIO MARGINAL (antes de operar)
  Y / X

PRECIO EFECTIVO DE LA OPERACIÓN
  Δy / Δx

Y SIEMPRE
  precio efectivo < precio marginal
  → la diferencia es el deslizamiento,
    y crece con el tamaño relativo a la reserva
```

### 2. El deslizamiento es la profundidad

En este mecanismo la profundidad no se lee en el libro: es el tamaño de la
reserva. El bloque establece la correspondencia y la resume en una regla
práctica.

```text
EN UN LIBRO DE ÓRDENES, LA PROFUNDIDAD
SE MIDE SOBRE LOS NIVELES

EN ESTE MECANISMO, LA PROFUNDIDAD
ES EL TAMAÑO DE LA RESERVA

  operar el 1 % de la reserva
  → deslizamiento ≈ 1 %

  operar el 10 % de la reserva
  → deslizamiento ≈ 10 %

REGLA PRÁCTICA
  el deslizamiento es aproximadamente
  el tamaño de la operación como fracción
  de la reserva

  → PARA OPERAR 1 000 000 CON MENOS DEL 1 %
    DE DESLIZAMIENTO HACE FALTA UNA RESERVA
    DE 100 000 000

Y ESE ES EL PROBLEMA: el capital necesario
es enorme comparado con el volumen que sirve.
```

### 3. La pérdida por divergencia

Quien aporta reservas cobra comisiones y soporta una pérdida frente a no haber
hecho nada. El bloque explica de dónde sale esa pérdida y por qué es
sistemática.

```text
QUIEN APORTA LAS RESERVAS RECIBE COMISIONES
Y SOPORTA UNA PÉRDIDA

  SI EL PRECIO EXTERNO SE MUEVE,
  LOS ARBITRAJISTAS OPERAN CONTRA LA RESERVA
  HASTA IGUALARLO

  · si A sube, se llevan A y dejan B
  · el aportante acaba con más del que baja

  COMPARADO CON HABERSE QUEDADO QUIETO,
  PIERDE. Siempre. La única pregunta es
  si las comisiones lo compensan.

FÓRMULA APROXIMADA PARA PRODUCTO CONSTANTE
  con un cambio de precio de factor r:

  pérdida = 2·√r / (1 + r) − 1

  r = 1,25 → −0,62 %
  r = 1,50 → −2,02 %
  r = 2,00 → −5,72 %
  r = 4,00 → −20,00 %
```

### 4. Cuándo compensa aportar

Aportar reservas compensa o no según una comparación con dos términos que
dependen de cosas distintas. El bloque la plantea y la traduce a la apuesta
que realmente se está haciendo.

```text
COMISIONES ACUMULADAS > PÉRDIDA POR DIVERGENCIA

  las comisiones dependen del VOLUMEN
  la pérdida depende del MOVIMIENTO DE PRECIO

  → aportar reservas es una apuesta a que
    habrá mucho volumen y poco movimiento

  Y ES EXACTAMENTE LA APUESTA DE UN CREADOR
  DE MERCADO TRADICIONAL, con la diferencia
  de que este no puede retirarse ni ajustar
  su cotización: la fórmula opera sola

CONSECUENCIA
  en un par volátil y de poco volumen,
  aportar reservas pierde dinero de forma
  sistemática, y quien lo hace suele no
  haberlo calculado
```

### 5. Frente al libro de órdenes

| Aspecto | Creador automatizado | Libro de órdenes |
|---|---|---|
| Precio disponible | Siempre | Solo si hay órdenes |
| Capital necesario | Muy alto por unidad de volumen | Menor |
| Deslizamiento | Predecible por fórmula | Depende del libro |
| Ajuste a noticias | Solo por arbitraje, con retardo | Inmediato por retirada de órdenes |
| Quien provee | Aportante pasivo | Creador activo |
| Coste del proveedor | Pérdida por divergencia | Riesgo de inventario |
| Idóneo para | Pares sin creadores dispuestos | Mercados con participantes |

## 🧮 Ejemplo guiado

El ejemplo calcula el precio marginal y el efectivo de una operación grande. La diferencia entre ambos es el deslizamiento, y crece con el tamaño relativo.

**Situación.** Se evalúa aportar reservas a un mecanismo automatizado para un par
de activos tokenizados. Hay que decidir si compensa.

```text
DATOS
  reserva del activo A                 500 000 unidades
  reserva del activo B               1 000 000 unidades
  precio marginal inicial            2,000 B por A
  producto K                     500 000 000 000
  comisión por operación                    0,25 %
  volumen mensual del par           8 400 000 en B
  aportación evaluada         5 % de ambas reservas
  volatilidad mensual del par                 9 %
```

**Paso 1 — calcula el precio de una operación.**

```text
UN OPERADOR ENTREGA 10 000 DE A

  X + Δx = 510 000
  Y' = K / 510 000 = 980 392,16
  Δy = 1 000 000 − 980 392,16 = 19 607,84

  PRECIO EFECTIVO
  19 607,84 / 10 000 = 1,96078

  PRECIO MARGINAL ANTES: 2,00000
  DESLIZAMIENTO: 1,96 %
```

**Paso 2 — comprueba la regla práctica.**

```text
TAMAÑO RELATIVO A LA RESERVA
  10 000 / 500 000 = 2,0 %

DESLIZAMIENTO OBSERVADO
  1,96 %

  → LA REGLA PRÁCTICA SE CONFIRMA:
    el deslizamiento es aproximadamente
    el tamaño relativo
```

**Paso 3 — calcula las comisiones esperadas.**

```text
VOLUMEN MENSUAL 8 400 000 EN B
COMISIÓN 0,25 %

  comisiones totales del mecanismo
  8 400 000 × 0,25 % = 21 000 al mes

  APORTACIÓN DEL 5 %
  21 000 × 5 % = 1 050 al mes
  = 12 600 al año
```

**Paso 4 — calcula el valor aportado.**

```text
APORTACIÓN
  A: 500 000 × 5 % = 25 000 unidades
  B: 1 000 000 × 5 % = 50 000 unidades

  VALOR EN B (a precio 2,000)
  25 000 × 2 + 50 000 = 100 000

  RENDIMIENTO POR COMISIONES
  12 600 / 100 000 = 12,6 % anual
```

**Paso 5 — calcula la pérdida por divergencia.**

```text
VOLATILIDAD MENSUAL DEL 9 %

  supuesto: en un año el precio se mueve
  y vuelve varias veces, con un recorrido
  acumulado equivalente a r = 1,45
  en el peor tramo

  pérdida = 2·√1,45 / (1 + 1,45) − 1
          = 2 × 1,20416 / 2,45 − 1
          = 0,98299 − 1
          = −1,70 %

  SOBRE 100 000 APORTADOS: −1 700

  Y ESO SUPONE QUE EL PRECIO VUELVE.
  Si no vuelve, la pérdida se materializa.
```

**Paso 6 — compara.**

```text
COMISIONES         +12 600
DIVERGENCIA         −1 700
NETO               +10 900 al año
                   = 10,9 % sobre lo aportado

¿COMPENSA?
  depende de la alternativa

  si esos 100 000 rendirían un 4,3 %
  en un depósito: la prima es de 6,6 puntos

  ¿POR QUÉ RIESGO?
  · pérdida por divergencia mayor si el
    precio se mueve más
  · riesgo del emisor de cada activo
  · riesgo del contrato
  · iliquidez: retirar la reserva mueve
    el precio
```

**Paso 7 — encuentra el punto en que deja de compensar.**

```text
¿CON QUÉ MOVIMIENTO DE PRECIO
LA DIVERGENCIA SE COME LAS COMISIONES?

  hace falta pérdida > 12,6 %
  2·√r / (1 + r) − 1 = −0,126
  2·√r / (1 + r) = 0,874

  resolviendo: r ≈ 2,75 (o su inverso 0,364)

  → SI EL PRECIO DEL PAR SE MUEVE
    UN 175 % EN UN SENTIDO,
    LAS COMISIONES DE UN AÑO SE PIERDEN

CON UNA VOLATILIDAD MENSUAL DEL 9 %
  la anualizada es 9 % × √12 = 31,2 %
  un movimiento de 175 % está a
  unas 5,6 desviaciones

  → improbable en un año, y perfectamente
    posible en tres

CONCLUSIÓN
  aportar compensa con este volumen y esta
  volatilidad, y deja de compensar si el
  volumen cae o si el par se vuelve
  direccional
```

**Interpreta:** el rendimiento del 12,6 % por comisiones parecía atractivo, y la
pérdida por divergencia se lo comió en un 13,5 %. **El mecanismo paga por volumen
y cobra por movimiento**, y quien aporta reservas está apostando —sin poder
retirarse ni ajustar— a que habrá mucho del primero y poco del segundo.

## 🧭 Perspectivas

La creación de mercado automatizada afecta a cada participante de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un precio siempre disponible | Si opera |
| Operador | Deslizamiento por tamaño | Cómo trocea |
| Aportante de reservas | Un 12,6 % de comisiones | Si aporta |
| Arbitrajista | Divergencia con el externo | Cuándo opera |
| Plataforma | Volumen y comisión | Qué fórmula elige |
| Banco | Un mercado sin creador designado | Si participa |
| Emisor del activo | Precio formado por fórmula | Si lo acepta como referencia |
| Supervisor | Precio sin creador responsable | Qué exige |
| Auditor | Reservas y su valoración | Qué revela |
| Sociedad | Mercados sin intermediarios visibles | Qué protección exige |

## 🏦 Del cliente al banco

El cliente ve un precio y ejecuta a otro peor según su tamaño. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Rinde un 12,6 %» | Menos la pérdida por divergencia | 21, clase 13 |
| «Siempre hay precio» | A un deslizamiento proporcional al tamaño | 21, clase 13 |
| «No hay intermediarios» | Hay aportantes que pierden por divergencia | 21, clase 13 |

## ⚖️ Riesgos y controles

Los riesgos son de deslizamiento y de pérdida por divergencia. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Pérdida por divergencia ignorada | Solo se mira la comisión | Calcularla para varios movimientos |
| Deslizamiento no anticipado | Se opera grande contra reserva pequeña | Trocear según el tamaño relativo |
| Reserva insuficiente | Cualquier operación mueve el precio | Dimensionar por volumen objetivo |
| Precio usado como referencia | Es formado por fórmula, no por mercado | No usarlo como índice |
| Retirada que mueve el precio | La salida cuesta como la entrada | Medir el coste de salir antes |
| Par direccional | La divergencia se materializa | Revisar la aportación si aparece tendencia |

## 🧪 Práctica

El laboratorio pide calcular precios efectivos y la pérdida por divergencia de un proveedor. La comparación con las comisiones cobradas decide si proveer liquidez rinde.

En [`labs/lab-06.md`](../labs/lab-06.md):

1. Implementa la fórmula de producto constante y verifica la regla práctica.
2. Calcula la pérdida por divergencia para cinco movimientos de precio.
3. Halla el movimiento que anula un año de comisiones.
4. Compara con un libro de órdenes de la misma profundidad efectiva.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen ejecuciones y rendimientos peores de lo esperado. Las causas son el deslizamiento y la divergencia no calculados.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Mirar solo la comisión | Es lo que se publicita | Resta la divergencia |
| Llamarla «pérdida impermanente» | Suena reversible | Se materializa al retirar |
| Operar grande de golpe | Se ignora el deslizamiento | Trocea según la reserva |
| Usar el precio como índice | Está disponible siempre | Lo forma una fórmula, no un mercado |
| Comparar con un libro sin ajustar | Parece más barato | Compara a igual profundidad |
| Suponer que el precio vuelve | Es el supuesto cómodo | Si no vuelve, la pérdida es real |

## ❓ Preguntas de comprobación

1. ¿Cómo fija el precio una fórmula de producto constante?
2. ¿Qué relación hay entre el tamaño de la operación y el deslizamiento?
3. ¿Por qué la pérdida por divergencia es estructural y no accidental?
4. ¿A qué está apostando quien aporta reservas?
5. En el ejemplo, ¿qué movimiento de precio anula un año de comisiones?

## 📥 Entregable

Guarda en `portfolio/parte-21/clase-13/`:

- el cálculo de precio efectivo y deslizamiento para tres tamaños;
- la pérdida por divergencia para cinco movimientos de precio;
- el neto entre comisiones y divergencia, con su alternativa de referencia;
- el punto en que la aportación deja de compensar.

## 🔗 Referencias cruzadas

- **Viene de:** clases 6 y 11; Parte 20, clase 13.
- **Continúa en:** clase 16 de esta parte.
- **Se aplica en:** Parte 22, clase 10; Parte 23, clase 11.

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

- IOSCO (2022). *Decentralized Finance Report*. IOSCO. Funcionamiento y riesgos de los protocolos de negociación automatizada. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD699.pdf>
- IOSCO (2023). *Policy Recommendations for Decentralized Finance*. IOSCO. Recomendaciones aplicables a las finanzas descentralizadas. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD754.pdf>
- Financial Stability Board (2023). *The Financial Stability Risks of Decentralised Finance*. FSB. Riesgos de estabilidad de la negociación automatizada. <https://www.fsb.org/2023/02/the-financial-stability-risks-of-decentralised-finance/>
- Bank for International Settlements (2021). *DeFi risks and the decentralisation illusion*, Quarterly Review. BIS. Crítica del grado real de descentralización de estos mercados. <https://www.bis.org/publ/qtrpdf/r_qt2112b.htm>
- Verificación local: comprueba si tu jurisdicción considera actividad regulada aportar reservas a un mecanismo de este tipo o explotarlo. **Fecha de verificación de esta clase: 2026-08-20.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 12 · Pago contra pago y riesgo de liquidación](12-pago-contra-pago-y-riesgo-de-liquidacion.md) | [Parte 21](../README.md) · [Programa](../../../SYLLABUS.md) | [14 · Colateral y garantías tokenizadas →](14-colateral-y-garantias-tokenizadas.md) |
<!-- gen:footer:end -->
