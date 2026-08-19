<!-- meta
part: 21
class: 12
title: "Pago contra pago y riesgo de liquidación"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [liquidacion, riesgo-de-principal, fx]
regulation_last_verified: 2026-08-19
regulatory_status: vigente
primary_authorities: [CPMI, BIS, FSB]
requires_legal_review: false
-->

<!-- gen:header:start -->
# Clase 12 · Pago contra pago y riesgo de liquidación

> [← 11 · FX: del mercado mayorista al registro](11-fx-del-mercado-mayorista-al-registro.md) · [Índice de la parte](../README.md) · [13 · Creación de mercado automatizada →](13-creacion-de-mercado-automatizada.md)

**Parte 21 — Tokenización, FX on-chain y mercados programables** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Aplicar la lógica de la clase 8 al cambio de divisas: **que las dos patas se
liquiden juntas o no se liquide ninguna**. Y medir la exposición que queda cuando
no es así, que es el riesgo que dio nombre al problema en 1974.

El cambio de divisa de la clase anterior tiene dos tramos que se liquidan por separado. Esta clase los condiciona uno al otro, y precisa qué riesgo elimina el mecanismo y cuál queda vivo.

## 📚 Objetivos

Al finalizar podrás:

1. **Definir** el riesgo de liquidación en divisas y por qué existe.
2. **Calcular** la ventana de exposición entre dos husos horarios.
3. **Comparar** las tres formas de acotarlo: PvP, neteo y límites.
4. **Diseñar** un PvP entre dos activos anotados y probar sus modos de fallo.
5. **Determinar** qué parte de la exposición no elimina ningún mecanismo.

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

Los cuatro primeros términos son el riesgo y su mecanismo de eliminación; los cuatro siguientes, los mitigantes parciales y lo que queda. La **exposición residual** es lo que hay que declarar: el pago contra pago elimina el riesgo de principal y no el de reemplazo, y decir que elimina el riesgo de liquidación es inexacto.

| Concepto | Comprensión verificable |
|---|---|
| `riesgo de liquidación` | Entregar una divisa y no recibir la otra |
| `pago contra pago` | Liquidar ambas patas de forma condicionada |
| `ventana de exposición` | Tiempo entre entregar y recibir |
| `irrevocabilidad` | Momento a partir del cual no se puede cancelar |
| `neteo bilateral` | Compensación entre dos partes |
| `límite bilateral` | Máximo de exposición admitida frente a otro |
| `riesgo de reemplazo` | Coste de rehacer la operación si falla |
| `exposición residual` | La que no elimina ningún mecanismo |

## 🧠 Modelo mental

El modelo mental son dos riesgos distintos bajo un mismo nombre: el de principal, que es perder el importe entero, y el de reemplazo, que es tener que rehacer la operación a otro precio. El mecanismo elimina el primero y deja el segundo.

```text
POR QUÉ EXISTE EL RIESGO

  un cambio de divisas tiene DOS PAGOS
  en DOS SISTEMAS DISTINTOS,
  en DOS HUSOS DISTINTOS

  el que paga primero entrega el principal
  y espera

  SI LA CONTRAPARTE FALLA EN ESE INTERVALO,
  PIERDE TODO EL PRINCIPAL, no una diferencia
  de precio

  → ES EL ÚNICO RIESGO DE MERCADO EN QUE
    SE PIERDE EL 100 % Y NO UNA VARIACIÓN

TRES FORMAS DE ACOTARLO
  1 PAGO CONTRA PAGO   lo elimina
  2 NETEO              reduce el importe
  3 LÍMITES            acota la pérdida máxima

Y NINGUNA ELIMINA EL RIESGO DE REEMPLAZO.
```

## 📖 Desarrollo

### 1. La ventana entre husos

La exposición no empieza ni termina donde la intuición sugiere, y esa
imprecisión hace que se subestime. El bloque fija sus dos extremos y enumera
lo que puede caber entre ellos.

```text
LA EXPOSICIÓN NO ES «HASTA QUE PAGUE
LA OTRA PARTE»

  EMPIEZA cuando mi pago se vuelve
  IRREVOCABLE, no cuando lo envío

  TERMINA cuando confirmo que recibí
  el contravalor, no cuando la otra parte
  dice haberlo enviado

  Y ENTRE AMBOS PUEDE HABER
  · diferencia de husos
  · fin de semana
  · festivo en uno de los dos países
  · cierre del sistema de destino

CASO PEOR HABITUAL
  pago irrevocable un viernes en un huso
  adelantado, contravalor confirmado el lunes
  → 72 horas de exposición al principal
```

### 2. Pago contra pago

El pago contra pago se define por lo que exige y por lo que garantiza. El
bloque separa ambas cosas y conecta el segundo caso con la atomicidad de la
clase 8.

```text
QUÉ EXIGE

  · un mecanismo que controle ambas patas
  · o que ambas estén en el mismo registro

  y en el segundo caso es exactamente
  la atomicidad de la clase 8

QUÉ ELIMINA
  el riesgo de principal: ya no se puede
  entregar sin recibir

QUÉ NO ELIMINA
  · el riesgo de reemplazo: si la operación
    no se ejecuta, hay que rehacerla a otro
    precio
  · el riesgo de liquidez: los fondos estaban
    comprometidos
  · el riesgo operativo del propio mecanismo

COSTE
  prefinanciación en ambas divisas,
  con el saldo ocioso de la clase 10
```

### 3. Neteo

Compensar las operaciones del día reduce el importe expuesto sin eliminar el
riesgo. El bloque muestra la diferencia con un ejemplo.

```text
COMPENSAR LAS OPERACIONES DEL DÍA
ENTRE DOS PARTES

  20 operaciones en ambos sentidos
  → un solo saldo por divisa

  REDUCE EL IMPORTE EXPUESTO,
  no la existencia del riesgo

  · si el saldo neto es pequeño, la pérdida
    máxima es pequeña
  · pero sigue habiendo un momento en que
    uno paga y el otro no

EXIGE
  · acuerdo de neteo con validez jurídica
    en un concurso
  · y esa validez es lo que hay que verificar,
    no darla por supuesta
```

### 4. Límites bilaterales

Los límites bilaterales son el control más extendido y el más fácil de aplicar
mal. El bloque explica cómo se calculan y cuándo se liberan, que es donde está
el error habitual.

```text
EL MECANISMO MÁS SIMPLE Y EL MÁS USADO

  «no tendré más de X de exposición
   simultánea frente a esta contraparte»

  · se calcula sobre la exposición máxima
    simultánea, no sobre el volumen del día
    (Parte 18, clase 11)
  · se consume al hacerse irrevocable el pago
  · se libera al confirmar el contravalor

ERROR HABITUAL
  liberar el límite al enviar el contravalor
  esperado, no al confirmarlo
  → el límite deja de proteger justo
    cuando hace falta
```

### 5. La exposición residual

Después de aplicar todos los mecanismos queda una exposición residual que
conviene tener nombrada. El bloque la enumera y se detiene en la que aparece
precisamente al llevar el mecanismo a un registro.

```text
LO QUE NO ELIMINA NINGÚN MECANISMO

  · riesgo de reemplazo, siempre
  · riesgo operativo del mecanismo mismo
  · riesgo de que la finalidad jurídica
    no coincida con la técnica
  · riesgo del emisor del activo anotado,
    si las patas no son dinero de banco central

EL ÚLTIMO ES EL QUE APARECE AL LLEVAR
EL PvP A UN REGISTRO
  se elimina el riesgo de principal frente
  a la contraparte y se asume el riesgo
  de crédito frente a dos emisores

  → si ambos son bancos centrales, el cambio
    es una mejora clara
  → si son emisores privados, hay que sumar
    su riesgo y compararlo
```

## 🧮 Ejemplo guiado

El ejemplo compara cuatro mecanismos contra la misma exposición base. Conviene mirar la oponibilidad del neteo: sin ella, la reducción que muestra no existe en un concurso.

**Situación.** Una tesorería opera 40 000 000 diarios en un par entre husos
separados por 11 horas. Hay que medir la exposición y evaluar los mecanismos.

```text
DATOS
  volumen diario                    40 000 000
  operaciones diarias                       28
  huso de la divisa A          irrevocable 10:00 local
  huso de la divisa B          confirmación 16:00 local
  diferencia horaria                  11 horas
  probabilidad de incumplimiento
    de contraparte en 1 día              0,003 %
  recuperación esperada                     45 %
  coste de financiación                    4,3 % anual
  volatilidad diaria del par               0,7 %
```

**Paso 1 — calcula la ventana un día normal.**

```text
PAGO A IRREVOCABLE
  10:00 hora local de A

CONFIRMACIÓN DE B
  16:00 hora local de B
  = 16:00 − 11 h = 05:00 del día siguiente
    en hora de A

VENTANA
  de 10:00 a 05:00 del día siguiente
  = 19 horas
```

**Paso 2 — calcula la ventana del peor día.**

```text
VIERNES

  pago irrevocable viernes 10:00 en A
  el sistema de B cierra y no reabre
  hasta el lunes

  confirmación lunes 16:00 en B
  = lunes 05:00 en A

  VENTANA = viernes 10:00 → lunes 05:00
          = 67 horas
```

**Paso 3 — mide la exposición máxima simultánea.**

```text
CON 19 HORAS DE VENTANA Y OPERACIONES
REPARTIDAS EN LA JORNADA

  supuesto: las 28 operaciones se concentran
  en 6 horas, y ninguna se confirma antes
  del cierre

  EXPOSICIÓN MÁXIMA SIMULTÁNEA
  = volumen del día = 40 000 000

  EL FIN DE SEMANA
  = volumen del viernes = 40 000 000
  durante 67 horas

  Y SI EL LUNES SE OPERA ANTES DE CONFIRMAR
  EL VIERNES: 80 000 000
```

**Paso 4 — calcula la pérdida esperada.**

```text
DÍA NORMAL
  40 000 000 × 0,003 % × (1 − 45 %)
  = 40 000 000 × 0,00003 × 0,55
  = 660 al día

ANUAL (250 días)
  165 000

FIN DE SEMANA
  la probabilidad se aplica sobre 2,8 días
  40 000 000 × 0,003 % × 2,8 × 0,55
  = 1 848 por fin de semana
  × 50 = 92 400 al año

TOTAL ≈ 257 400 al año
```

**Paso 5 — evalúa el neteo.**

```text
28 OPERACIONES EN AMBOS SENTIDOS

  supuesto: el neteo reduce el importe
  expuesto al 18 % del bruto
  = 7 200 000

  PÉRDIDA ESPERADA
  257 400 × 18 % = 46 332 al año

  AHORRO: 211 068

  CONDICIÓN
  el acuerdo de neteo debe ser oponible
  en el concurso de la contraparte
  → si no lo es, el neteo no reduce nada
    y el cálculo anterior es falso
```

**Paso 6 — evalúa el PvP en registro.**

```text
AMBAS PATAS COMO ACTIVOS ANOTADOS,
LIQUIDACIÓN ATÓMICA

  riesgo de principal = 0
  pérdida esperada por principal = 0

COSTE · PvP SOBRE EL BRUTO
  prefinanciación en ambas divisas
  supuesto: 25 % del volumen diario en cada una
  40 000 000 × 25 % × 2 = 20 000 000
  × 4,3 % = 860 000 al año

COSTE · PvP SOBRE EL SALDO NETEADO
  el importe a liquidar es el neto, no el bruto
  saldo neto                        7 200 000
  prefinanciación al 25 %           1 800 000
  en dos divisas                    3 600 000
  × 4,3 %                             154 800 al año
```

**Paso 7 — compara los tres mecanismos contra la misma base.**

Aquí está la trampa del ejercicio. Cada mecanismo debe compararse con la
**pérdida esperada sin ningún mecanismo**, no con la que ya redujo otro: si se
compara el PvP con la pérdida que el neteo ya bajó a 46 332, el PvP parece no
compensar, y esa conclusión es falsa.

```text
                        PÉRDIDA      COSTE      TOTAL
                        ESPERADA

  sin mecanismo          257 400          0    257 400
  solo neteo              46 332          0     46 332
  PvP sobre el bruto           0    860 000    860 000
  PvP sobre el neteado         0    154 800    154 800

  → SOLO NETEO es la opción más barata,
    si el acuerdo es oponible en concurso
```

**Paso 8 — repite sin oponibilidad del neteo.**

```text
SI EL ACUERDO DE NETEO NO ES OPONIBLE
EN EL CONCURSO DE LA CONTRAPARTE

  el neteo no reduce nada:
  la pérdida esperada vuelve a 257 400
  y el saldo a liquidar vuelve al bruto

                        PÉRDIDA      COSTE      TOTAL
  sin mecanismo          257 400          0    257 400
  «neteo»                257 400          0    257 400
  PvP sobre el bruto           0    860 000    860 000

  → NINGÚN MECANISMO MEJORA:
    lo que procede es reducir el LÍMITE
    bilateral hasta que la pérdida esperada
    quepa en el apetito

  límite tal que la pérdida esperada anual
  no supere 80 000:
  80 000 / 257 400 × 40 000 000 = 12 433 000
```

**Interpreta:** la decisión no la determina el volumen sino **la oponibilidad
jurídica del acuerdo de neteo**. Con un acuerdo válido, el neteo basta y cuesta
menos que el PvP; sin él, ningún mecanismo mejora y lo que procede es bajar el
límite bilateral. Y comparar un mecanismo con la pérdida que ya redujo otro es
el error que invierte la conclusión.

## 🧭 Perspectivas

El riesgo de liquidación afecta a cada participante de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Tesorería | Una ventana de 19 o 67 horas | Con quién opera y hasta cuánto |
| Contraparte | Su propio límite | Cuánto acepta |
| Banco | Exposición simultánea | Qué límite bilateral fija |
| Infraestructura | Dos patas que coordinar | Si ofrece PvP |
| Banco central | Riesgo sistémico del par | Si extiende horarios |
| Emisor del activo anotado | Saldos prefinanciados | Qué respaldo mantiene |
| Supervisor | Exposición al principal | Qué reporte exige |
| Auditor | Límites y su liberación | Cuándo se liberan |
| Asesor jurídico | Oponibilidad del neteo | Si emite opinión |
| Sociedad | Un mercado más seguro | — |

## 🏦 Del cliente al banco

El cliente no lo percibe y su banco asume o no una exposición del importe completo. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Se liquida el mismo día» | 19 horas de exposición al principal | 21, clase 12 |
| «El viernes es igual» | 67 horas en vez de 19 | 21, clase 12 |
| «Tenemos neteo» | Solo vale si es oponible en concurso | 21, clase 12 |

## ⚖️ Riesgos y controles

Los riesgos residuales son de reemplazo y de neteo no oponible. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Ventana subestimada | Se mide del envío a la recepción esperada | De irrevocable a confirmado |
| Fin de semana ignorado | El peor caso es el que no se calcula | Calcular el viernes |
| Neteo sin oponibilidad | No reduce nada en el concurso | Opinión jurídica antes de contar con él |
| Límite liberado antes | Deja de proteger al hacer falta | Liberar solo con confirmación |
| PvP comparado con lo que no toca | Se compara con pérdida ya reducida | Comparar con la pérdida sin mecanismo |
| Riesgo de emisor de las patas | Se elimina uno y aparece otro | Sumarlo a la comparación |

## 🧪 Práctica

El laboratorio pide comparar los cuatro mecanismos sobre la misma base. La oponibilidad del neteo es lo que decide cuál sirve.

En [`labs/lab-07.md`](../labs/lab-07.md):

1. Calcula la ventana de exposición un día normal y un viernes.
2. Mide la exposición máxima simultánea, no el volumen.
3. Compara neteo, límites y PvP frente a la pérdida esperada sin mecanismo.
4. Repite suponiendo que el acuerdo de neteo no es oponible, y halla el límite
   bilateral que deja la pérdida esperada dentro del apetito.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen exposiciones mal medidas. Las causas son neteo sin oponibilidad y riesgo de reemplazo ignorado.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Medir la ventana del envío | Es lo intuitivo | De irrevocable a confirmado |
| Olvidar el fin de semana | No es un día normal | Es el peor caso y es recurrente |
| Contar el volumen | Es el dato disponible | Mide la exposición simultánea |
| Dar el neteo por válido | Está firmado | Exige opinión de oponibilidad |
| Liberar el límite pronto | Agiliza la operativa | Solo con confirmación |
| Comparar mecanismos mal | Se acumulan reducciones | Cada uno frente a la pérdida base |

## ❓ Preguntas de comprobación

1. ¿Por qué el riesgo de liquidación en divisas es del 100 % del principal?
2. ¿Cuándo empieza y cuándo termina la ventana de exposición?
3. ¿Qué elimina el pago contra pago y qué no?
4. ¿Qué condición jurídica hace que el neteo reduzca la exposición?
5. En el ejemplo, ¿qué determina la elección entre neteo y PvP?

## 📥 Entregable

Guarda en `portfolio/parte-21/clase-12/`:

- el cálculo de la ventana normal y del peor caso;
- la exposición máxima simultánea con su supuesto de distribución;
- la comparación de los tres mecanismos frente a la pérdida base;
- la conclusión con y sin oponibilidad del acuerdo de neteo.

## 🔗 Referencias cruzadas

- **Viene de:** clases 8, 10 y 11; Parte 18, clases 10 y 11.
- **Continúa en:** clase 14 de esta parte.
- **Se aplica en:** Parte 22, clase 10; Parte 23, clases 9 y 11.

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

- Committee on Payments and Market Infrastructures (1996). *Settlement Risk in Foreign Exchange Transactions*. BIS. Origen y medición del riesgo de liquidación cambiaria. <https://www.bis.org/cpmi/publ/d17.htm>
- CPMI e IOSCO (2012). *Principles for Financial Market Infrastructures*. BIS. Exigencia de pago contra pago en la infraestructura. <https://www.bis.org/cpmi/publ/d101.htm>
- Bank for International Settlements (2022). *Triennial Central Bank Survey of foreign exchange and OTC derivatives markets*. BIS. Volumen expuesto al riesgo de liquidación según la encuesta. <https://www.bis.org/statistics/rpfx22.htm>
- Financial Stability Board (2020). *Enhancing Cross-border Payments: Stage 3 roadmap*. FSB. Prioridad del programa global sobre este riesgo. <https://www.fsb.org/2020/10/enhancing-cross-border-payments-stage-3-roadmap/>
- Verificación local: comprueba la oponibilidad de los acuerdos de neteo en la jurisdicción de cada contraparte antes de reducir la exposición declarada. **Fecha de verificación de esta clase: 2026-08-19.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 11 · FX: del mercado mayorista al registro](11-fx-del-mercado-mayorista-al-registro.md) | [Parte 21](../README.md) · [Programa](../../../SYLLABUS.md) | [13 · Creación de mercado automatizada →](13-creacion-de-mercado-automatizada.md) |
<!-- gen:footer:end -->
