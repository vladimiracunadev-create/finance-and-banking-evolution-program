<!-- meta
part: 11
class: 4
title: "Riesgo de liquidez"
level: profesional
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 04 · Riesgo de liquidez

> [← 03 · Riesgo de crédito de cartera y concentración](03-riesgo-de-credito-de-cartera.md) · [Índice de la parte](../README.md) · [05 · Riesgo de tasa en el libro de banca →](05-riesgo-de-tasa-en-el-libro-de-banca.md)

**Parte 11 — Gestión integral de riesgos** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Gestionar el riesgo que mata bancos rápido. Un banco puede sobrevivir años con pérdidas y morir en 48
horas por falta de liquidez. Esta clase explica por qué la solvencia y la liquidez son problemas
distintos, cómo se miden y por qué el segundo se manifiesta casi siempre como consecuencia del primero.

El riesgo de crédito de la clase anterior se materializa en meses. Este puede acabar con un banco en días, y no requiere que haya pérdidas: basta con que los depositantes duden. Es el riesgo que la Parte 3 anticipó al hablar de transformación de plazos, tratado ahora con sus métricas regulatorias.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** insolvencia de iliquidez y explicar cómo se retroalimentan.
2. **Calcular** e interpretar la cobertura de liquidez y el financiamiento estable neto.
3. **Construir** una escalera de vencimientos con supuestos conductuales.
4. **Diseñar** un plan de financiamiento de contingencia con indicadores de activación.
5. **Evaluar** la velocidad de una corrida en el contexto de la banca digital.

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

Los dos primeros términos son la distinción que ordena la clase; los seis siguientes, las métricas y los supuestos que las sostienen. El **supuesto conductual** es donde vive la fragilidad de todo el aparato: las métricas dependen de cuánto se supone que se retirará en estrés, y esa cifra no se observa hasta que ocurre.

| Concepto | Comprensión verificable |
|---|---|
| `iliquidez` | Incapacidad de cumplir obligaciones a tiempo, aun siendo solvente. |
| `insolvencia` | Patrimonio negativo: los activos no cubren los pasivos. |
| `activos líquidos de alta calidad` | Convertibles en efectivo sin pérdida significativa incluso en estrés. |
| `cobertura de liquidez` | Activos líquidos sobre salidas netas a 30 días de estrés. |
| `financiamiento estable neto` | Financiamiento estable disponible sobre el requerido a un año. |
| `supuesto conductual` | Comportamiento esperado de un flujo sin vencimiento contractual. |
| `depósito estable` | Aquel con baja probabilidad de retiro en estrés. |
| `plan de contingencia` | Conjunto de fuentes y acciones activables con indicadores definidos. |

## 🧠 Modelo mental

```text
UN BANCO ES ILÍQUIDO POR DISEÑO

  activos:  ilíquidos y largos   (créditos a 20 años)
  pasivos:  líquidos y cortos    (depósitos a la vista)

  esa transformación es su función económica
  y es también su vulnerabilidad estructural

  no existe banco que sobreviva
  al retiro simultáneo de todos sus depósitos
```

De ahí se deducen las tres defensas: **activos líquidos** (colchón), **seguro de depósitos** (evita que
el retiro empiece) y **prestamista de última instancia** (evita que el retiro se propague). Ninguna
funciona sola.

## 📖 Desarrollo

### 1. Iliquidez e insolvencia

Las dos situaciones se distinguen en teoría y se confunden en el momento, porque la duda sobre una provoca la otra. El esquema muestra el círculo.

| | Iliquidez | Insolvencia |
|---|---|---|
| Definición | No puede pagar hoy | No podría pagar nunca |
| Velocidad | Horas o días | Meses o años |
| Solución | Liquidez de emergencia | Capital o resolución |
| Visibilidad | Inmediata y pública | Puede ocultarse mucho tiempo |
| Causa | Descalce y pérdida de confianza | Pérdidas acumuladas |

```text
LA CONEXIÓN
  la duda sobre la SOLVENCIA provoca el retiro
  el retiro provoca la ILIQUIDEZ
  la iliquidez obliga a vender activos con descuento
  la venta con descuento provoca la INSOLVENCIA

  el círculo se cierra: la duda se vuelve verdadera
```

**Por eso la distinción, correcta en teoría, es difícil de aplicar en el momento.** El prestamista de
última instancia solo debe asistir a bancos solventes, y la solvencia es precisamente lo que está en
duda cuando se necesita la asistencia.

### 2. Cobertura de liquidez

La cobertura de liquidez mide si los activos líquidos alcanzan para treinta días de estrés. El procedimiento siguiente la calcula.

```text
                    activos líquidos de alta calidad
COBERTURA (LCR) = ─────────────────────────────────────  ≥ 100 %
                  salidas netas de efectivo a 30 días
                        en escenario de estrés
```

| Nivel | Activos elegibles | Descuento |
|---|---|---:|
| Nivel 1 | Efectivo, reservas en el banco central, deuda soberana de alta calidad | 0 % |
| Nivel 2A | Deuda soberana de menor calidad, corporativa de muy alta calificación | 15 % |
| Nivel 2B | Corporativa de calificación menor, acciones de índice, hipotecas titularizadas | 25–50 % |

*(Los niveles 2 tienen límites de participación en el total. Verifica los aplicables en tu jurisdicción.)*

```text
SALIDAS EN ESTRÉS — tasas de retiro supuestas
  depósitos minoristas estables (cubiertos por seguro)      3–5 %
  depósitos minoristas menos estables                      10 %
  depósitos operativos de empresas                         25 %
  depósitos no operativos de empresas                      40 %
  financiamiento mayorista no garantizado                 100 %
  líneas comprometidas no utilizadas (retiro)             10–40 %
```

**El supuesto clave es que el financiamiento mayorista desaparece por completo.** No es pesimismo: es lo
que se observó. El financiamiento minorista con seguro de depósitos es el que resiste.

### 3. Financiamiento estable neto

La segunda métrica mira el horizonte de un año y la estructura del fondeo. El procedimiento la calcula.

```text
                financiamiento estable DISPONIBLE
ESTABLE (NSFR) = ──────────────────────────────────  ≥ 100 %
                financiamiento estable REQUERIDO
```

```text
DISPONIBLE (ponderaciones)      REQUERIDO (ponderaciones)
  capital                100 %    efectivo y líquidos       0–5 %
  depósitos minoristas    90–95 % créditos < 1 año         50 %
  mayorista > 1 año      100 %    créditos hipotecarios    65 %
  mayorista < 1 año        0–50 % créditos > 1 año         85 %
                                  activos ilíquidos       100 %
```

**Mientras la cobertura mira 30 días, el financiamiento estable mira un año.** Un banco puede cumplir el
primero con un colchón de bonos y fallar el segundo por financiar crédito hipotecario con depósitos a
la vista. Son controles complementarios, no redundantes.

### 4. Supuestos conductuales

Los supuestos de retiro son la parte más frágil y la más determinante. La tabla los recoge con su origen.

```text
EL PROBLEMA
  una cuenta corriente vence "a la vista": contractualmente, mañana
  conductualmente, el saldo medio de la cartera lleva años estable

  si se modela contractualmente: brecha catastrófica a 1 día
  si se modela conductualmente: brecha razonable
  y el supuesto conductual es el que falla justo cuando importa
```

| Flujo | Vencimiento contractual | Supuesto conductual típico |
|---|---|---|
| Cuenta corriente | A la vista | Núcleo estable 70–85 %, resto volátil |
| Ahorro | A la vista | Núcleo estable 60–80 % |
| Depósito a plazo | Fecha fija | Renovación 60–80 % |
| Línea de crédito no usada | — | Utilización 10–40 % según segmento |
| Hipotecario | 20 años | Prepago 4–10 % anual |
| Tarjeta revolvente | — | Saldo persistente con perfil propio |

**Regla de gobierno:** todo supuesto conductual debe estar documentado, calibrado con datos propios,
revisado al menos anualmente y **sometido a estrés en el escenario adverso**. Un supuesto conductual sin
escenario adverso es una suposición optimista con apariencia técnica.

### 5. Velocidad de la corrida

Las corridas actuales son mucho más rápidas que las que inspiraron las métricas. La tabla recoge la evidencia.

```text
CORRIDA CLÁSICA (siglo XX)
  fila física en la sucursal
  velocidad limitada por horario y por capacidad de caja
  días para materializarse

CORRIDA DIGITAL (actual)
  transferencia inmediata desde el teléfono
  amplificada por redes sociales
  horas para materializarse
```

Los episodios de 2023 mostraron retiros de una fracción muy alta de los depósitos en un solo día. Las
implicancias operativas son concretas:

```text
· el horizonte de 30 días de la cobertura puede ser demasiado largo
  para el primer día: se necesita medición INTRADÍA
· la capacidad de monetizar el colchón depende del horario del mercado
  y del acceso a las facilidades del banco central
· la concentración de depositantes importa más que nunca:
  pocos depositantes grandes, conectados entre sí, se mueven juntos
· la comunicación pública es parte del plan de liquidez
```

## 🧮 Ejemplo guiado

El ejemplo calcula la cobertura de liquidez de un banco y la recalcula con supuestos de retiro más severos. La diferencia entre las dos cifras es la medida real de la fragilidad.

**Situación.** Un banco calcula su posición de liquidez y la somete a un escenario de estrés propio.

```text
ACTIVOS LÍQUIDOS
  efectivo y reservas en el banco central     18 400   nivel 1
  deuda soberana local                        42 600   nivel 1
  bonos corporativos AA                       11 200   nivel 2A
  acciones de índice                           6 800   nivel 2B

DEPÓSITOS
  minoristas cubiertos por seguro            286 000
  minoristas no cubiertos                     94 000
  empresas, operativos                        78 000
  empresas, no operativos                     52 000
  mayorista a menos de 30 días                46 000

OTROS
  líneas comprometidas no utilizadas          88 000
  entradas contractuales a 30 días            34 000
```

**Paso 1 — calcula los activos líquidos ajustados.**

```text
nivel 1:   18 400 + 42 600 = 61 000, sin descuento     → 61 000
nivel 2A:  11 200 × (1 − 0,15)                          →  9 520
nivel 2B:   6 800 × (1 − 0,50)                          →  3 400
                                                  TOTAL   73 920

verificación de límites:
  nivel 2 total = 12 920, sobre 73 920 = 17,5 %  (límite 40 %)  ✓
  nivel 2B = 3 400, sobre 73 920 = 4,6 %         (límite 15 %)  ✓
```

**Paso 2 — calcula las salidas en estrés.**

```text
minoristas cubiertos     286 000 × 5 %   = 14 300
minoristas no cubiertos   94 000 × 10 %  =  9 400
empresas operativos       78 000 × 25 %  = 19 500
empresas no operativos    52 000 × 40 %  = 20 800
mayorista < 30 días       46 000 × 100 % = 46 000
líneas comprometidas      88 000 × 20 %  = 17 600
SALIDAS BRUTAS                            127 600
```

**Paso 3 — calcula las entradas admisibles.**

```text
entradas contractuales                     34 000
límite: las entradas se reconocen hasta el 75 % de las salidas
  tope = 127 600 × 75 % = 95 700  → 34 000 se reconocen íntegras

SALIDAS NETAS = 127 600 − 34 000 = 93 600
```

**Paso 4 — calcula la cobertura.**

```text
LCR = 73 920 / 93 600 = 78,97 %

INCUMPLE el mínimo de 100 %
déficit: 93 600 − 73 920 = 19 680 de activos líquidos
```

**Paso 5 — identifica la causa.**

```text
mayorista a menos de 30 días: 46 000
representa el 49 % de las salidas netas
y el 8,4 % del financiamiento total

el problema NO es el tamaño del colchón
es la DEPENDENCIA de financiamiento mayorista de corto plazo
que en estrés se supone íntegramente perdido
```

**Paso 6 — evalúa dos alternativas.**

```text
ALTERNATIVA A — aumentar el colchón
  comprar 19 680 de deuda soberana
  costo: diferencial entre el rendimiento del soberano (5,2 %)
         y el costo del financiamiento (6,4 %) = −1,2 %
  costo anual: 19 680 × 1,2 % = 236

ALTERNATIVA B — alargar el financiamiento mayorista
  emitir 46 000 a 3 años y no renovar el mayorista corto
  costo: diferencial de plazo 6,4 % → 7,3 % = +0,9 %
  costo anual: 46 000 × 0,9 % = 414

  efecto sobre la cobertura:
    salidas se reducen en 46 000 → salidas netas 47 600
    LCR = 73 920 / 47 600 = 155,3 %
```

**Paso 7 — decide con el segundo indicador a la vista.**

```text
la alternativa A cumple la cobertura y NO mejora el NSFR:
  el mayorista corto sigue financiando activos largos

la alternativa B cumple la cobertura CON HOLGURA
  y mejora el financiamiento estable disponible

  costo adicional de B sobre A: 414 − 236 = 178 anuales
  → es el precio de resolver la causa en lugar del síntoma

DECISIÓN: alternativa B, con una porción de A (colchón de 8 000)
para la gestión intradía. Costo total ≈ 510 anuales.

ADEMÁS, incorporar al plan de contingencia:
  · medición intradía de la posición
  · indicadores de activación (fuga de depósitos > 2 % semanal,
    diferencial de emisión > 80 pb sobre el par, retiro de un
    depositante > 5 % del total)
  · concentración de depositantes: los 20 mayores
  · protocolo de comunicación pública
```

**Interpreta:** la cobertura al 79 % no era un problema de colchón sino de **estructura de
financiamiento**. Comprar bonos habría hecho cumplir el indicador dejando la vulnerabilidad intacta.
Este es el uso correcto de un indicador regulatorio: **no como meta a alcanzar, sino como síntoma a
diagnosticar**.

## 🏦 Del cliente al banco

El cliente retira su depósito y el banco pierde su fuente de fondeo más barata en el peor momento. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Mi depósito está seguro» | Seguro de depósitos y su límite | 4, clase 11 |
| «El banco me ofrece más tasa a plazo» | Necesidad de financiamiento estable | 10, clase 2 |
| «Todos retiraron al mismo tiempo» | Corrida digital y su velocidad | 11, clase 4 |
| «El banco central prestó al banco» | Prestamista de última instancia | 6, clase 10 |
| «Cerraron el banco un viernes» | Resolución ordenada | 12, clase 12 |

## 🧪 Práctica

El laboratorio pide calcular las dos métricas y estresar los supuestos conductuales. El banco pasa la métrica regulatoria y no sobrevive al escenario realista.

En `labs/lab-02.md`, sección de liquidez:

1. Calcula la cobertura de liquidez de un banco sintético con sus descuentos y límites.
2. Calcula el financiamiento estable neto y explica por qué difiere del anterior.
3. Construye una escalera de vencimientos con supuestos conductuales documentados.
4. Diseña un plan de contingencia con indicadores de activación cuantificados.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen crisis de liquidez en bancos solventes. Las causas son supuestos conductuales optimistas y concentración de fondeo.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se cumple el indicador comprando bonos | Se trata el síntoma | Diagnostica la estructura de financiamiento. |
| Supuestos conductuales sin estrés | Optimismo con apariencia técnica | Somete cada supuesto al escenario adverso. |
| Se mide solo a 30 días | Corrida digital más rápida | Añade medición intradía. |
| Concentración de depositantes no medida | Foco en el agregado | Mide los 20 mayores y su correlación. |
| Plan de contingencia sin activadores | Documento inerte | Define indicadores cuantitativos. |
| Se confunde iliquidez con insolvencia | Concepto | Distínguelas y observa su retroalimentación. |

## ❓ Preguntas de comprobación

1. ¿Cómo se convierte una duda sobre la solvencia en una insolvencia real?
2. ¿Por qué el financiamiento mayorista se supone íntegramente perdido en estrés?
3. ¿Qué mide el financiamiento estable neto que la cobertura de liquidez no mide?
4. ¿Por qué un supuesto conductual puede fallar justo cuando más importa?
5. ¿Qué cambia en la gestión de liquidez con la banca digital?

## 📥 Entregable

Guarda en `portfolio/parte-11/clase-04/`:

- el cálculo de cobertura de liquidez con descuentos, límites y salidas;
- el cálculo del financiamiento estable neto con su interpretación;
- la escalera de vencimientos con los supuestos conductuales documentados;
- el plan de contingencia con sus indicadores de activación.

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

- Basel Committee on Banking Supervision (2013). *Basel III: The Liquidity Coverage Ratio and liquidity risk monitoring tools*. BIS. <https://www.bis.org/publ/bcbs238.htm>
- Basel Committee on Banking Supervision (2014). *Basel III: The Net Stable Funding Ratio*. BIS. <https://www.bis.org/bcbs/publ/d295.htm>
- Basel Committee on Banking Supervision (2008). *Principles for Sound Liquidity Risk Management and Supervision*. BIS.
- Diamond, D. y Dybvig, P. (1983). "Bank Runs, Deposit Insurance, and Liquidity". *Journal of Political Economy*, 91(3). Modelo fundacional de corridas.
- Bank for International Settlements (2023). *Annual Economic Report*, capítulo sobre las turbulencias bancarias de 2023. BIS.
- Verificación local: revisa los mínimos de liquidez, activos elegibles y facilidades del banco central aplicables en tu país.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 03 · Riesgo de crédito de cartera y concentración](03-riesgo-de-credito-de-cartera.md) | [Parte 11](../README.md) · [Programa](../../../SYLLABUS.md) | [05 · Riesgo de tasa en el libro de banca →](05-riesgo-de-tasa-en-el-libro-de-banca.md) |
<!-- gen:footer:end -->
