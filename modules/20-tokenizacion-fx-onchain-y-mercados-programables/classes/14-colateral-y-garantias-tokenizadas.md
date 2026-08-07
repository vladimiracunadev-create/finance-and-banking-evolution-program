---
part: 21
class: 14
title: "Colateral y garantías tokenizadas"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [colateral, garantias, riesgo-de-credito]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [CPMI, IOSCO, BCBS]
requires_legal_review: true
---

<!-- gen:header:start -->
# Clase 14 · Colateral y garantías tokenizadas

> [← 13 · Creación de mercado automatizada](13-creacion-de-mercado-automatizada.md) · [Índice de la parte](../README.md) · [15 · Interoperabilidad entre infraestructuras →](15-interoperabilidad-entre-infraestructuras.md)

**Parte 21 — Tokenización, FX on-chain y mercados programables** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Usar un instrumento tokenizado como garantía. **La movilidad del colateral es una
de las ventajas reales de la tokenización**, y también el camino más corto hacia
una cascada de liquidaciones si el margen se programa mal.

## 📚 Objetivos

Al finalizar podrás:

1. **Explicar** qué aporta la tokenización a la movilidad del colateral.
2. **Calcular** el recorte aplicable a una garantía y su justificación.
3. **Diseñar** una llamada de margen con sus plazos y su vía de excepción.
4. **Simular** una cascada de liquidaciones y hallar su punto de amplificación.
5. **Determinar** cuándo la liquidación automática empeora el resultado.

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
| `colateral` | Activo entregado en garantía de una obligación |
| `recorte` | Descuento sobre el valor de mercado del colateral |
| `margen inicial` | Garantía exigida al abrir la posición |
| `margen de variación` | Ajuste según el movimiento del precio |
| `llamada de margen` | Requerimiento de aportar más garantía |
| `liquidación` | Venta del colateral para cubrir la obligación |
| `cascada` | Liquidaciones que provocan más liquidaciones |
| `movilidad del colateral` | Capacidad de moverlo donde hace falta |

## 🧠 Modelo mental

```text
QUÉ APORTA DE VERDAD LA TOKENIZACIÓN AQUÍ

  MOVILIDAD
    el colateral puede moverse entre
    contrapartes en minutos en vez de días
    → menos garantía inmovilizada por el
      simple hecho de estar en el sitio
      equivocado

  Y ESO SÍ ES UNA VENTAJA MEDIBLE

QUÉ NO APORTA
  · no mejora la calidad del colateral
  · no reduce su volatilidad
  · no elimina el riesgo de que valga menos
    cuando haga falta

QUÉ EMPEORA SI SE DISEÑA MAL
  la velocidad. Un margen programado que
  liquida en segundos convierte una caída
  en una cascada.
```

## 📖 Desarrollo

### 1. El recorte y su justificación

```text
EL RECORTE CUBRE LO QUE PUEDE PASAR
ENTRE QUE SE DECIDE LIQUIDAR Y SE VENDE

  · movimiento de precio en ese intervalo
  · impacto de la venta sobre el precio
  · coste de la operación
  · riesgo de que el emisor no responda

CÁLCULO
  recorte ≥ volatilidad del periodo de
           liquidación × factor de confianza
           + impacto de mercado esperado

Y EL IMPACTO DE MERCADO SE MIDE CON
LA PROFUNDIDAD (Parte 20, clase 13),
no se supone.

ERROR HABITUAL
  aplicar el recorte estándar de un activo
  líquido a uno tokenizado con profundidad
  cien veces menor
```

### 2. Movilidad y su valor

```text
UN MISMO COLATERAL PUEDE ESTAR EXIGIDO
EN VARIOS SITIOS A LA VEZ

  EN EL MUNDO TRADICIONAL
    mover una garantía entre depositarios
    lleva días
    → hay que mantener garantía sobrante
      en cada sitio

  CON COLATERAL MOVIBLE EN MINUTOS
    se puede mantener un fondo común y
    dirigirlo donde se necesite

AHORRO
  = garantía sobrante que deja de hacer falta
  × coste de financiarla

Y ESO SE CALCULA, NO SE ESTIMA:
depende de cuántos sitios y de cuánto
tarda hoy el traslado.
```

### 3. La llamada de margen bien diseñada

```text
CUATRO PARÁMETROS

  UMBRAL         desde qué caída se llama
  PLAZO          cuánto tiempo hay para aportar
  IMPORTE        cuánto se pide
  CONSECUENCIA   qué pasa si no se aporta

Y UNA VÍA DE EXCEPCIÓN (Parte 20, clase 11)
  quién puede prorrogar el plazo,
  con qué justificación y qué registro

POR QUÉ EL PLAZO ES CRÍTICO
  un plazo de horas permite al deudor
  vender ordenadamente y aportar
  un plazo de segundos no permite nada
  → y liquidar es siempre peor que
    dejar aportar
```

### 4. La cascada

```text
CÓMO SE FORMA

  1 el precio del colateral cae
  2 se disparan llamadas de margen
  3 quien no aporta, es liquidado
  4 la liquidación vende colateral
  5 la venta hace caer más el precio
  6 vuelve a 2

CADA VUELTA ES MÁS RÁPIDA
  porque el precio cae más deprisa
  y más posiciones cruzan su umbral

PUNTO DE AMPLIFICACIÓN
  el nivel de precio a partir del cual
  la venta forzada de una vuelta basta
  para disparar la siguiente

  → se calcula con la profundidad del mercado
    y la distribución de umbrales
```

### 5. Cuándo la liquidación automática empeora

```text
LIQUIDAR AUTOMÁTICAMENTE ES CORRECTO SI

  · el mercado tiene profundidad suficiente
    para absorber la venta
  · las posiciones están dispersas en umbrales
  · hay tiempo entre la llamada y la ejecución

ES INCORRECTO SI

  · muchas posiciones comparten umbral
  · la profundidad es menor que el volumen
    a liquidar
  · el plazo es tan corto que nadie puede
    aportar

MECANISMOS QUE LO CORRIGEN
  · liquidación parcial: vender lo justo
    para restablecer el margen, no todo
  · escalonamiento: repartir las liquidaciones
    en el tiempo
  · subasta en vez de venta al mercado
  · pausa si la caída supera un umbral,
    con reanudación ordenada

LA PAUSA ES LA MÁS EFICAZ Y LA MÁS
CRITICADA, porque deja posiciones
infragarantizadas mientras dura.
```

## 🧮 Ejemplo guiado

**Situación.** Una plataforma acepta bonos tokenizados como colateral de
préstamos. Hay que fijar el recorte y comprobar si el diseño de margen resiste.

```text
DATOS
  colateral total                   180 000 000
  préstamos vivos                   120 000 000
  ratio de garantía exigido               150 %
  umbral de llamada                       135 %
  umbral de liquidación                   120 %
  plazo para aportar                     4 horas
  profundidad del colateral al 1 %    2 400 000
  volatilidad diaria del colateral         1,8 %
  posiciones                                340
```

**Paso 1 — calcula el recorte adecuado.**

```text
PERIODO DE LIQUIDACIÓN SUPUESTO: 1 DÍA

  movimiento de precio a 99 % de confianza
  1,8 % × 2,33 = 4,19 %

  IMPACTO DE MERCADO
  liquidación media = 120 000 000 / 340
                    = 352 941 por posición
  frente a profundidad de 2 400 000
  → 14,7 % de la profundidad al 1 %
  → impacto ≈ 0,15 %

  COSTE DE OPERACIÓN: 0,05 %

  RECORTE ≥ 4,19 % + 0,15 % + 0,05 % = 4,39 %

  → RECORTE PROPUESTO: 5 %
```

**Paso 2 — comprueba el recorte implícito del ratio.**

```text
RATIO DE 150 % SIGNIFICA QUE EL COLATERAL
DEBE VALER 1,5 VECES EL PRÉSTAMO

  recorte implícito = 1 − 1/1,5 = 33,3 %

  MUY POR ENCIMA DEL 5 % CALCULADO

¿ESTÁ SOBRECUBIERTO?
  no necesariamente: el ratio del 150 %
  cubre además la caída del precio hasta
  el umbral de liquidación

  del 150 % al 120 % hay un colchón del 20 %
  de caída de precio antes de liquidar

  → el recorte del 5 % cubre lo que pasa
    DESPUÉS de decidir liquidar
  → el colchón del 20 % cubre lo que pasa
    ANTES

SON DOS COSAS DISTINTAS Y SE CONFUNDEN
CON FRECUENCIA.
```

**Paso 3 — mide la concentración de umbrales.**

```text
DISTRIBUCIÓN SUPUESTA DE LAS 340 POSICIONES
POR RATIO ACTUAL

  > 200 %        88 posiciones
  170 – 200 %    96
  150 – 170 %   102
  135 – 150 %    41
  < 135 %        13

CAÍDA DEL PRECIO DEL COLATERAL DEL 12 %
  todos los ratios se multiplican por 0,88

  > 200 %  → > 176 %      88 seguras
  170–200  → 150–176      96 seguras
  150–170  → 132–150     102, de las que
                         las de ratio inicial
                         < 153 % cruzan 135 %
  135–150  → 119–132      41 en llamada,
                         algunas en liquidación
  < 135    → < 119        13 en liquidación

  SUPUESTO: 58 posiciones cruzan el umbral
  de llamada y 24 el de liquidación
```

**Paso 4 — calcula el volumen a liquidar.**

```text
24 POSICIONES EN LIQUIDACIÓN

  colateral medio por posición
  180 000 000 / 340 = 529 412

  volumen a vender = 24 × 529 412
                   = 12 705 888

FRENTE A LA PROFUNDIDAD AL 1 %
  12 705 888 / 2 400 000 = 5,29 veces

  → LA VENTA MUEVE EL PRECIO
    MUCHO MÁS DEL 1 %
```

**Paso 5 — estima el impacto y la segunda vuelta.**

```text
SUPUESTO · IMPACTO PROPORCIONAL
  5,29 veces la profundidad al 1 %
  → impacto ≈ 5,3 %

  EL PRECIO CAE OTRO 5,3 %
  caída acumulada: 12 % + 5,3 % = 16,6 %

  RATIOS × 0,834

  las 96 posiciones del tramo 170–200 %
  pasan a 142–167 %
  → las de ratio inicial < 162 % cruzan 135 %

  SUPUESTO: 44 posiciones más en llamada
  y 31 más en liquidación

  VOLUMEN DE LA SEGUNDA VUELTA
  31 × 529 412 = 16 411 772
  → 6,84 veces la profundidad
  → impacto ≈ 6,8 %

LA SEGUNDA VUELTA ES MAYOR QUE LA PRIMERA:
ESTAMOS EN CASCADA.
```

**Paso 6 — encuentra el punto de amplificación.**

```text
LA CASCADA SE SOSTIENE CUANDO EL IMPACTO
DE UNA VUELTA DISPARA MÁS LIQUIDACIONES
QUE LA ANTERIOR

  vuelta 1: impacto 5,3 % → 31 liquidaciones
  vuelta 2: impacto 6,8 % → ?

  el detonante fue una caída del 12 %

  PROBANDO CON CAÍDAS MENORES
  · 6 %  → 9 liquidaciones → impacto 2,0 %
           → 4 más → se apaga
  · 9 %  → 16 liquidaciones → impacto 3,5 %
           → 12 más → impacto 2,6 % → se apaga
  · 12 % → 24 → 31 → CRECE

  PUNTO DE AMPLIFICACIÓN ≈ 10,5 % DE CAÍDA

  y con una volatilidad diaria del 1,8 %,
  una caída del 10,5 % está a 5,8 desviaciones
  en un día... o a 2,3 en una semana
```

**Paso 7 — corrige el diseño.**

```text
1 LIQUIDACIÓN PARCIAL
    vender solo lo necesario para volver
    al 150 %, no toda la posición
    → el volumen de la vuelta 1 baja de
      12,7 a supuesto 4,2 millones
    → impacto 1,75 % en vez de 5,3 %

2 ESCALONAMIENTO
    repartir las liquidaciones en ventanas
    de 15 minutos, máximo el 20 % de la
    profundidad por ventana

3 PAUSA POR CAÍDA
    si el precio cae más del 8 % en una hora,
    se suspenden las liquidaciones 30 minutos
    y se amplía el plazo de aportación

4 PLAZO REAL PARA APORTAR
    4 horas es razonable; 4 minutos no
    → verificar que el plazo se respeta
      también cuando el sistema está saturado

CON LAS CUATRO, EL PUNTO DE AMPLIFICACIÓN
SUBE DE 10,5 % A UN SUPUESTO 21 %
```

**Interpreta:** el recorte del 5 % estaba bien calculado y era irrelevante para
el problema. **Lo que rompía el sistema era liquidar posiciones enteras contra un
mercado cinco veces menos profundo que el volumen a vender**, y la corrección más
eficaz —liquidar solo lo necesario— no toca ningún parámetro de riesgo.

## 🧭 Perspectivas

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Una llamada de margen | Si aporta o es liquidado |
| Prestatario | 4 horas o 4 minutos | Si puede reaccionar |
| Prestamista | Garantía que se deprecia | Cuándo liquida |
| Plataforma | Cascada en curso | Si pausa |
| Creador de mercado | Ventas forzadas | Si provee liquidez |
| Custodio | Colateral que se mueve | Cómo lo registra |
| Banco | Colateral movible entre sitios | Cuánta garantía sobrante ahorra |
| Supervisor | Liquidaciones automáticas | Qué salvaguardas exige |
| Auditor | Recortes y su justificación | Qué verifica |
| Sociedad | Pérdidas concentradas | Qué protección exige |

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Me liquidaron entero» | Bastaba vender el 33 % | 21, clase 14 |
| «El recorte era del 5 %» | El problema era la profundidad | 21, clase 14 |
| «Cayó un 12 % y perdí todo» | La cascada añadió otro 12 % | 21, clase 14 |

## ⚖️ Riesgos y controles

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Recorte estándar mal aplicado | Se usa el de un activo líquido | Calcularlo con la profundidad real |
| Liquidación total innecesaria | Se vende toda la posición | Liquidación parcial al umbral |
| Umbrales concentrados | Muchas posiciones cruzan a la vez | Medir la distribución |
| Plazo irreal | Nadie puede aportar en minutos | Plazo verificado bajo carga |
| Sin pausa | La cascada no encuentra freno | Pausa por caída con reanudación ordenada |
| Confundir recorte con colchón | Cubren cosas distintas | Separarlos en el análisis |

## 🧪 Práctica

En [`labs/lab-08.md`](../labs/lab-08.md):

1. Calcula el recorte con volatilidad, impacto y coste de operación.
2. Mide la distribución de umbrales y el volumen a liquidar.
3. Simula la cascada y halla el punto de amplificación.
4. Aplica las cuatro correcciones y vuelve a medirlo.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Recorte por analogía | Se copia de otro activo | Calcúlalo con la profundidad |
| Liquidar posiciones enteras | Es lo simple de programar | Vende solo lo necesario |
| Ignorar la distribución de umbrales | No se tiene el dato | Es lo que decide la cascada |
| Plazo de minutos | Se busca proteger al prestamista | Liquidar es peor que dejar aportar |
| Sin pausa por caída | Se teme la posición desprotegida | Sin pausa, la cascada no para |
| Confundir recorte y colchón | Ambos son márgenes | Cubren momentos distintos |

## ❓ Preguntas de comprobación

1. ¿Qué aporta realmente la tokenización al colateral?
2. ¿Cómo se calcula un recorte y qué cubre exactamente?
3. ¿En qué se diferencia el recorte del colchón hasta el umbral de liquidación?
4. ¿Cómo se halla el punto de amplificación de una cascada?
5. ¿Cuál de las cuatro correcciones es la más eficaz y por qué?

## 📥 Entregable

Guarda en `portfolio/parte-21/clase-14/`:

- el recorte calculado con sus tres componentes;
- la distribución de umbrales y el volumen a liquidar por vuelta;
- el punto de amplificación antes y después de las correcciones;
- la llamada de margen con sus cuatro parámetros y su vía de excepción.

## 🔗 Referencias cruzadas

- **Viene de:** clases 9 y 12; Parte 20, clase 13.
- **Continúa en:** clases 15 y 16 de esta parte.
- **Se aplica en:** Parte 22, clase 10; Parte 23, clases 9 y 14.

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

- CPMI e IOSCO (2012). *Principles for Financial Market Infrastructures*. BIS. <https://www.bis.org/cpmi/publ/d101.htm>
- Basel Committee on Banking Supervision (2020). *Margin requirements for non-centrally cleared derivatives*. BIS. <https://www.bis.org/bcbs/publ/d499.htm>
- Financial Stability Board (2022). *Review of Margining Practices*. FSB. <https://www.fsb.org/2022/09/review-of-margining-practices/>
- IOSCO (2023). *Policy Recommendations for Decentralized Finance*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD754.pdf>
- Verificación local: comprueba qué exige tu jurisdicción sobre recortes, plazos de llamada de margen y salvaguardas ante liquidaciones automáticas. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 13 · Creación de mercado automatizada](13-creacion-de-mercado-automatizada.md) | [Parte 21](../README.md) · [Programa](../../../SYLLABUS.md) | [15 · Interoperabilidad entre infraestructuras →](15-interoperabilidad-entre-infraestructuras.md) |
<!-- gen:footer:end -->
