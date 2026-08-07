---
part: 1
class: 12
title: "Amortización básica"
level: fundamento
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 12 · Amortización básica

> [← 11 · Cuotas y cronogramas de pago](11-cuotas-y-cronogramas-de-pago.md) · [Índice de la parte](../README.md) · [13 · Herramientas: calculadora, Excel y Python →](13-herramientas-calculadora-excel-y-python.md)

**Parte 01 — Matemática financiera básica** · **Nivel:** Fundamento — sin conocimientos previos · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Comparar los tres sistemas de amortización que existen en el mundo real —francés, alemán y
americano— y entender que **no hay uno mejor**: hay uno adecuado según el flujo de caja de quien
paga. Esta clase entrega el criterio para elegir y el vocabulario para discutirlo con un ejecutivo
de banco sin quedar en desventaja.

La clase anterior construyó la cuota del sistema francés y su tabla de desarrollo. Esta muestra que ese sistema es una elección entre varias, no la única forma de amortizar, y que la elección cambia cuánto se paga en total. Es la primera vez en el programa en que el mismo capital, la misma tasa y el mismo plazo producen costos distintos.

## 📚 Objetivos

Al finalizar podrás:

1. **Construir** las tablas de los tres sistemas para un mismo crédito.
2. **Comparar** el interés total pagado y el perfil de cuota de cada sistema.
3. **Elegir** el sistema adecuado según el perfil de ingresos del deudor.
4. **Explicar** el efecto de un periodo de gracia sobre el costo total.
5. **Reconocer** la amortización negativa y por qué es peligrosa.

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

Los tres primeros términos son sistemas de amortización y los tres últimos son variantes que se les añaden. La **amortización negativa** es la que hay que saber reconocer antes que ninguna: es la única situación en la que se paga puntualmente y la deuda crece, y su detección es un control de consumo financiero, no un cálculo.

| Concepto | Comprensión verificable |
|---|---|
| `sistema francés` | Cuota **constante**; amortización creciente, interés decreciente. Es el estándar del crédito de consumo e hipotecario. |
| `sistema alemán` | Amortización **constante**; cuota decreciente. Paga menos interés total y exige más al principio. |
| `sistema americano` | Solo intereses durante el plazo y **capital íntegro al vencimiento**. Es la estructura de un bono. |
| `periodo de gracia` | Tramo inicial sin amortización. Puede ser **total** (no se paga nada, y el interés se capitaliza) o **parcial** (se pagan solo intereses). |
| `amortización negativa` | La cuota no alcanza a cubrir el interés y el saldo **crece**. Señal de alerta severa. |
| `costo total` | Suma de todos los pagos. Depende del sistema, del plazo y de la gracia, no solo de la tasa. |

## 🧠 Modelo mental

Los tres sistemas responden a la misma pregunta con distinta prioridad:

```text
francés    "quiero pagar siempre lo mismo"        → predecibilidad
alemán     "quiero deber menos cuanto antes"      → menor costo
americano  "quiero pagar poco ahora"              → liquidez hoy, riesgo al final
```

Elegir sistema es elegir **dónde poner el esfuerzo en el tiempo**. El costo total es la consecuencia,
no el objetivo.

## 📖 Desarrollo

### 1. Los tres sistemas sobre el mismo crédito

Capital 6 000 000, tasa 1,2 % mensual, 12 cuotas.

**Francés — cuota constante:**

```text
A = 6 000 000 × 0,012 × (1,012)^12 / ((1,012)^12 − 1) = 540 234
```

| Cuota | Saldo inicial | Cuota | Interés | Amortización |
|---:|---:|---:|---:|---:|
| 1 | 6 000 000 | 540 234 | 72 000 | 468 234 |
| 6 | 3 600 470 | 540 234 | 43 206 | 497 028 |
| 12 | 533 830 | 540 234 | 6 406 | 533 828 |
| | **Interés total** | | **482 808** | |

**Alemán — amortización constante de `6 000 000/12 = 500 000`:**

| Cuota | Saldo inicial | Cuota | Interés | Amortización |
|---:|---:|---:|---:|---:|
| 1 | 6 000 000 | 572 000 | 72 000 | 500 000 |
| 6 | 3 500 000 | 542 000 | 42 000 | 500 000 |
| 12 | 500 000 | 506 000 | 6 000 | 500 000 |
| | **Interés total** | | **468 000** | |

**Americano — solo interés, capital al final:**

| Cuota | Saldo inicial | Cuota | Interés | Amortización |
|---:|---:|---:|---:|---:|
| 1–11 | 6 000 000 | 72 000 | 72 000 | 0 |
| 12 | 6 000 000 | 6 072 000 | 72 000 | 6 000 000 |
| | **Interés total** | | **864 000** | |

### 2. Comparación

Los tres sistemas se comparan mejor sobre el mismo crédito que en abstracto. La tabla siguiente enfrenta la primera cuota, la última y el interés total, que son las tres cifras que decide cada sistema.

| Sistema | Primera cuota | Última cuota | Interés total | Sobrecosto vs. alemán |
|---|---:|---:|---:|---:|
| Alemán | 572 000 | 506 000 | 468 000 | — |
| Francés | 540 234 | 540 234 | 482 808 | +3,2 % |
| Americano | 72 000 | 6 072 000 | 864 000 | +84,6 % |

Las conclusiones que hay que poder defender:

- El **alemán** es el más barato porque reduce el capital más rápido, y es el más exigente al inicio.
- El **francés** cuesta un 3,2 % más y compra predecibilidad. En plazos largos la brecha crece.
- El **americano** casi duplica el interés y traslada todo el riesgo al vencimiento. Solo tiene
  sentido si el capital estará disponible con certeza en esa fecha —por eso es la estructura de un
  bono corporativo, donde el emisor refinancia o tiene el flujo previsto.

### 3. Periodo de gracia

Sobre el mismo crédito, con 6 meses de gracia y 12 cuotas posteriores:

| Modalidad | Qué se paga en la gracia | Capital al iniciar cuotas | Interés total |
|---|---|---:|---:|
| Sin gracia | — | 6 000 000 | 482 808 |
| Gracia parcial (solo interés) | 72 000/mes | 6 000 000 | 914 808 |
| Gracia total (nada) | 0 | **6 445 000** | 960 000 |

En la gracia **total** el interés no pagado se capitaliza: la deuda crece de 6 000 000 a 6 445 000
antes de pagar la primera cuota. Un periodo de gracia no es un regalo: es un aplazamiento con costo,
y en la modalidad total es amortización negativa consentida.

### 4. Amortización negativa

Ocurre cuando `cuota < saldo × tasa`. El saldo crece cada periodo aunque se pague puntualmente.

```text
saldo 4 000 000, tasa 3,0 % mensual → interés 120 000
cuota pactada 90 000
  → saldo del mes siguiente: 4 030 000
```

Aparece en tres situaciones reales: pago mínimo de tarjetas de crédito, créditos con cuota
"flexible" y refinanciamientos mal estructurados. Es la firma matemática del sobreendeudamiento, y
la Parte 4, clase 10, la usa como indicador de alerta temprana.

### 5. Cómo elegir

La elección del sistema no depende de cuál cobra menos intereses, sino de qué perfil de pago soporta el deudor. La tabla relaciona las dos cosas.

| Perfil del deudor | Sistema recomendable | Motivo |
|---|---|---|
| Ingreso estable, prioriza predecibilidad | Francés | Cuota constante, fácil de presupuestar |
| Ingreso alto hoy que puede bajar | Alemán | Concentra el esfuerzo cuando hay capacidad |
| Proyecto que genera caja recién al final | Americano o gracia parcial | Alinea pagos con generación de flujo |
| Ingreso variable o estacional | Cuotas ajustadas al ciclo | Evita mora en meses bajos |

## 🧮 Ejemplo guiado

El ejemplo compara los tres sistemas sobre el mismo crédito, paso a paso. Conviene resistir la tentación de saltar a la fila del total: la diferencia entre sistemas se explica en las primeras cuotas y solo se ve siguiéndolas.

**Situación.** Una pyme agrícola necesita 20 000 000 para una plantación que empieza a generar
ingresos al mes 10. El banco ofrece 1,1 % mensual a 24 meses en tres estructuras.

```text
A  francés puro, 24 cuotas
B  gracia parcial de 9 meses (solo interés) + 24 cuotas francesas
C  gracia total de 9 meses + 24 cuotas francesas
```

**Paso 1 — opción A.**

```text
(1,011)^24 = 1,299887
cuota = 20 000 000 × 0,011 × 1,299887 / 0,299887 = 953 780
interés total = 953 780 × 24 − 20 000 000 = 2 890 720
```

Problema: durante 9 meses la pyme no tiene ingresos y debe pagar 953 780 mensuales. Necesita
8 584 020 de capital de trabajo adicional solo para sobrevivir hasta el mes 10.

**Paso 2 — opción B (gracia parcial).**

```text
interés mensual en gracia = 20 000 000 × 0,011 = 220 000  (9 meses = 1 980 000)
capital al mes 9 = 20 000 000 (sin cambio)
cuota posterior = 953 780 (misma que A)
interés total = 1 980 000 + 2 890 720 = 4 870 720
```

**Paso 3 — opción C (gracia total).**

```text
saldo al mes 9 = 20 000 000 × (1,011)^9 = 20 000 000 × 1,103479 = 22 069 580
cuota posterior = 22 069 580 × 0,011 × 1,299887/0,299887 = 1 052 460
interés total = 1 052 460 × 24 − 20 000 000 = 5 259 040
```

**Paso 4 — compara.**

| Opción | Desembolso meses 1–9 | Cuota posterior | Interés total | Sobrecosto vs. A |
|---|---:|---:|---:|---:|
| A | 953 780/mes | 953 780 | 2 890 720 | — |
| B | 220 000/mes | 953 780 | 4 870 720 | +1 980 000 |
| C | 0 | 1 052 460 | 5 259 040 | +2 368 320 |

**Paso 5 — decide con criterio, no con el número menor.** A es la más barata y la que puede quebrar
la empresa: exige 8,6 millones de caja antes del primer ingreso. B cuesta 1,98 millones más y baja
la exigencia a 1,98 millones en el periodo crítico. C es la más cara y la única que no exige nada
durante la gracia.

**Recomendación defendible:** B, si la pyme tiene 2 millones de caja; C, si no los tiene. Elegir A
por ser "la más barata" sería optimizar el costo e ignorar el riesgo de liquidez, que es exactamente
el error que la Parte 11, clase 4, enseña a no cometer.

## 🏦 Del cliente al banco

El cliente compara cuotas y el banco compara duración e ingreso financiero. La tabla enfrenta las dos lecturas de la misma decisión de amortización.

| Sistema | Dónde lo verás como cliente | Dónde lo verás como bancario |
|---|---|---|
| Francés | Consumo, automotriz, hipotecario | Producto estándar de la cartera minorista |
| Alemán | Algunos créditos comerciales | Estructuras con amortización lineal en banca empresa |
| Americano | Poco frecuente al público | Bonos, papel comercial, créditos puente |
| Gracia | Crédito estudiantil, agrícola, de proyecto | Estructuración de banca empresarial (Parte 13) |

## 🧪 Práctica

El laboratorio pide amortizar el mismo capital por los tres sistemas y tabular el sobrecosto. El objetivo es llegar a la conclusión incómoda de que el sistema más barato en intereses no es el recomendable para todos los perfiles.

En `labs/lab-06.md`, sección de sistemas:

1. Construye las tres tablas para un mismo crédito y grafica las cuotas.
2. Calcula el interés total de cada sistema y la brecha porcentual.
3. Modela una gracia parcial y una total, cuantificando el capital capitalizado.
4. Construye un caso de amortización negativa y determina en qué cuota el saldo empieza a crecer.

## ⚠️ Errores frecuentes

Los síntomas de la tabla se refieren a créditos que se comportan de forma inesperada. En casi todos, la causa es un periodo de gracia mal entendido o una cuota que no alcanza a cubrir el interés devengado.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se elige el sistema por el interés total | Se ignoró el perfil de flujo de caja | Evalúa costo **y** capacidad de pago periodo a periodo. |
| La deuda creció durante la gracia | Gracia total con capitalización | Verifica si la gracia es total o parcial antes de firmar. |
| El sistema alemán parece más caro | Se miró solo la primera cuota | Compara el interés total, no la cuota inicial. |
| Se aplicó cuota constante a un sistema alemán | Confusión de sistemas | En alemán lo constante es la **amortización**, no la cuota. |
| Se pactó una cuota menor al interés devengado | Amortización negativa no detectada | Control: `cuota > saldo × tasa` en todos los periodos. |
| Se compara crédito americano con francés por la cuota | Estructuras no comparables | Compara valor presente de todos los flujos a una tasa común. |

## ❓ Preguntas de comprobación

1. ¿Por qué el sistema alemán paga menos interés total que el francés con la misma tasa y plazo?
2. ¿Qué diferencia hay entre gracia total y gracia parcial, y cuál capitaliza?
3. ¿En qué situación real tiene sentido un crédito americano?
4. ¿Cómo detectas amortización negativa en una tabla antes de firmar?
5. Una pyme sin caja recibe tres ofertas. ¿Por qué la de menor interés total puede ser la peor?

## 📥 Entregable

Guarda en `portfolio/parte-01/clase-12/`:

- las tres tablas de amortización con el gráfico comparativo de cuotas;
- la tabla de interés total y brechas porcentuales;
- el análisis de gracia parcial vs. total con el capital capitalizado;
- una recomendación de estructura para un caso con su justificación de riesgo de liquidez.

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

- Broverman, S. (2017). *Mathematics of Investment and Credit* (7.ª ed.). ACTEX. Capítulo 3: sistemas de amortización comparados.
- Kellison, S. (2008). *The Theory of Interest* (3.ª ed.). McGraw-Hill/Irwin. Capítulos 6 y 7: amortización, fondo de amortización y periodos de gracia.
- Ross, S., Westerfield, R. y Jordan, B. (2022). *Fundamentos de finanzas corporativas* (12.ª ed.). McGraw-Hill. Capítulo 6: préstamos con amortización constante y con pago único.
- Saunders, A. y Cornett, M. (2021). *Financial Institutions Management: A Risk Management Approach* (10.ª ed.). McGraw-Hill. Capítulo sobre estructura de productos de crédito y riesgo de liquidez del deudor.
- Basel Committee on Banking Supervision (2017). *Guidelines: Prudential treatment of problem assets*. BIS. Tratamiento de reestructuraciones y periodos de gracia. <https://www.bis.org/bcbs/publ/d403.htm>
- Verificación local: confirma qué sistemas de amortización admite la normativa de tu país y qué información debe entregarse sobre periodos de gracia.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 11 · Cuotas y cronogramas de pago](11-cuotas-y-cronogramas-de-pago.md) | [Parte 01](../README.md) · [Programa](../../../SYLLABUS.md) | [13 · Herramientas: calculadora, Excel y Python →](13-herramientas-calculadora-excel-y-python.md) |
<!-- gen:footer:end -->
