<!-- meta
part: 18
class: 8
title: "Liquidez, prefinanciación, netting y horarios"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global]
regulatory_topics: [cross-border-payments, liquidez, tesoreria]
regulation_last_verified: 2026-08-20
regulatory_status: vigente
primary_authorities: [CPMI, Comité de Basilea]
requires_legal_review: false
-->

<!-- gen:header:start -->
# Clase 08 · Liquidez, prefinanciación, netting y horarios

> [← 07 · Compensación, liquidación y finalidad](07-compensacion-liquidacion-y-finalidad.md) · [Índice de la parte](../README.md) · [09 · El cambio de divisa dentro de un pago →](09-fx-dentro-de-un-pago-transfronterizo.md)

**Parte 18 — Pagos transfronterizos, remesas y liquidación internacional** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Entender por qué un banco tiene dinero inmovilizado en veinte países y qué se
puede hacer al respecto. La liquidez atrapada es el coste silencioso de la
corresponsalía, y la mayor parte de las arquitecturas nuevas prometen atacarlo.

La liquidación de la clase anterior exige tener fondos donde hacen falta y cuando hacen falta. Esta clase cuantifica ese requisito, que es el coste principal del modelo, y recorre los mecanismos que lo reducen.

## 📚 Objetivos

Al finalizar podrás:

1. **Calcular** la liquidez necesaria de un corredor y su coste anual.
2. **Modelar** el efecto del netting bilateral y multilateral.
3. **Determinar** el saldo objetivo de un nostro con un criterio de servicio.
4. **Evaluar** el efecto de ampliar ventanas operativas.
5. **Distinguir** el ahorro que viene del netting del que viene del horario.

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

Los cuatro primeros términos son el coste de tener fondos donde hacen falta; los cuatro siguientes, los mecanismos que lo reducen. La **liquidez atrapada** es el coste principal del modelo de corresponsalía: dinero inmovilizado en varias monedas que no rinde y que financia la operación.

| Concepto | Comprensión verificable |
|---|---|
| `prefinanciación` | Fondos colocados por adelantado para poder pagar |
| `liquidez atrapada` | Saldos inmovilizados que no se pueden usar en otro sitio |
| `netting bilateral` | Compensación de posiciones entre dos participantes |
| `netting multilateral` | Compensación entre todos los participantes de un grupo |
| `ratio de netting` | Cuánto se reduce el importe a liquidar |
| `saldo objetivo` | Nivel deseado de un nostro, con su banda |
| `barrido` | Traslado automático de excedentes a la cuenta central |
| `ventana operativa` | Horario en que un sistema acepta y liquida operaciones |

## 🧠 Modelo mental

El modelo mental es un coste de oportunidad repartido por el mundo: cada corredor exige saldo previo en la moneda de destino, y ese saldo multiplicado por los corredores es el capital que el modelo consume.

```text
LA LIQUIDEZ DE UN NOSTRO ES UN SEGURO
QUE SE PAGA TODOS LOS DÍAS

  demasiada  → coste de fondeo sin contrapartida
  demasiado poca → pagos rechazados, clientes perdidos,
                   descubierto caro o corredor cerrado

EL PROBLEMA NO ES EL NIVEL MEDIO: ES LA COLA
  con salidas medias de 400 000 al día,
  el saldo no se fija en 400 000:
  se fija en el percentil alto de la distribución
  más un colchón por el peor día imaginable

Y AHÍ ESTÁ EL COSTE
  el 95 % de los días, ese colchón no se usa
```

## 📖 Desarrollo

### 1. De dónde sale la necesidad de liquidez

El saldo de un nostro no es una decisión arbitraria: responde a un desfase
entre salidas y entradas. El bloque enumera las causas y propone la fórmula
con la que se fija un saldo objetivo defendible.

```text
UN NOSTRO NECESITA SALDO PORQUE
  · los pagos salen antes de que entren los cobros
  · el corresponsal no admite descubierto, o lo cobra caro
  · la ventana de liquidación cierra antes de que
    lleguen los cobros del día
  · un pago rechazado por falta de fondos es un incidente
    con el cliente y con el corresponsal

LA FÓRMULA DEL SALDO OBJETIVO
  saldo = percentil P de las salidas netas diarias
        + colchón de seguridad
        − entradas previsibles antes del corte

  donde P se elige por NIVEL DE SERVICIO:
    P95  → 1 día de cada 20 con tensión
    P99  → 1 día de cada 100
    P99,5 → 1 día cada 200
```

### 2. Netting bilateral

El netting bilateral se entiende con dos cifras. El bloque compara la liquidez
que hace falta con y sin él, calcula el ratio de ahorro y termina con lo que
se paga a cambio, que no es dinero sino exposición durante un intervalo.

```text
SIN NETTING, EN UN DÍA
  Banco A paga a Banco B:   3 200 000
  Banco B paga a Banco A:   2 900 000
  liquidez movilizada:      6 100 000

CON NETTING BILATERAL
  posición neta: A debe a B 300 000
  liquidez movilizada:        300 000

RATIO DE NETTING
  1 − (300 000 / 6 100 000) = 95,1 %

EL PRECIO
  entre el momento de compensar y el de liquidar
  existe una exposición: si B falla, A ya no puede
  cobrar sus 2 900 000 pero puede tener que pagar
  sus 3 200 000 (según las reglas del acuerdo)
```

### 3. Netting multilateral

Con tres o más participantes el ahorro crece, porque las deudas cruzadas se
cancelan entre sí. El bloque desarrolla el caso completo, de las posiciones
bilaterales a las netas, hasta la liquidez que realmente se moviliza.

```text
TRES BANCOS, POSICIONES BILATERALES

        a B        a C        total paga
  A     1 200      800        2 000
  B       —      1 500        1 500
  C     1 900      —          1 900
  total 3 100    2 300        5 400

POSICIONES NETAS MULTILATERALES
  A: paga 2 000, cobra 1 900  →  neto −100
  B: paga 1 500, cobra 1 200  →  neto −300
  C: paga 1 900, cobra 2 300  →  neto +400

LIQUIDEZ MOVILIZADA: 400 (lo que recibe C)
RATIO: 1 − (400 / 5 400) = 92,6 %

LO QUE HACE FALTA PARA QUE ESTO FUNCIONE
  · un acuerdo multilateral, no bilateral
  · una entidad que calcule y liquide el neto
  · garantías: si un participante falla,
    el neto de todos cambia
  → por eso el netting multilateral suele exigir
    una cámara con fondo de garantía
```

### 4. Horarios: el ahorro que no es netting

Ampliar horarios y compensar importes reducen la necesidad de liquidez por
mecanismos distintos, y conviene no atribuir a uno lo que consiguió el otro. El
bloque los separa y muestra el efecto del horario con un ejemplo.

```text
DOS FUENTES DE AHORRO QUE SE CONFUNDEN

  NETTING     reduce el IMPORTE a liquidar
  HORARIO     reduce el TIEMPO que el saldo está inmóvil

EJEMPLO
  si el sistema de destino abre 4 horas más,
  los cobros del día llegan antes del corte
  → el banco puede fijar un saldo objetivo menor
    sin cambiar nada del netting

  CPMI lo identificó como una de las palancas
  con mejor relación entre efecto y coste:
  ampliar y alinear ventanas no requiere
  tecnología nueva, requiere acuerdo
```

### 5. Barrido y concentración

Cuando un banco tiene veinte nostros, la gestión deja de ser cuenta a cuenta.
El bloque describe las dos técnicas habituales, con lo que ahorra cada una y
lo que sigue haciendo falta después de aplicarlas.

```text
BARRIDO (sweeping)
  al cierre, los excedentes de cada nostro se trasladan
  automáticamente a una cuenta central de la divisa

  QUÉ AHORRA
    evita saldos ociosos dispersos en veinte cuentas

  QUÉ NO RESUELVE
    el saldo mínimo operativo sigue haciendo falta
    en cada cuenta al abrir el día siguiente

CONCENTRACIÓN POR DIVISA
  un solo nostro grande por divisa, en vez de tres pequeños
  QUÉ AHORRA   colchones duplicados
  QUÉ CUESTA   dependencia de un solo corresponsal
               (riesgo de concentración, clase 3)
```

## 🧮 Ejemplo guiado

El ejemplo calcula el coste de la liquidez atrapada de una red y el ahorro del netting. Conviene comparar el ratio de netting con el coste: el ahorro depende del volumen bidireccional.

**Situación.** Un banco revisa la liquidez de su nostro en dólares. Tiene datos
de 250 días hábiles.

```text
SALIDAS NETAS DIARIAS (USD)
  media                    412 000
  desviación típica        186 000
  percentil 95             742 000
  percentil 99           1 108 000
  máximo observado       1 640 000

SALDO ACTUAL MEDIO      2 400 000
COSTE NETO DE FONDEO         3,8 % anual

PAGOS RECHAZADOS POR FALTA DE FONDOS EN 250 DÍAS: 0
DESCUBIERTO INTRADÍA USADO: nunca

COBROS QUE LLEGAN DESPUÉS DEL CORTE: 38 % del total diario
```

**Paso 1 — calcula el coste actual.**

```text
2 400 000 × 3,8 % = 91 200 USD al año
```

**Paso 2 — calcula el saldo teórico por nivel de servicio.**

```text
CON P95
  saldo = 742 000 + colchón

CON P99
  saldo = 1 108 000 + colchón

EL COLCHÓN
  ¿de cuánto? El máximo observado (1 640 000) supera
  el P99 en 532 000.
  Un colchón razonable cubre la distancia entre
  el percentil elegido y el peor caso conocido.

  CON P99 Y COLCHÓN AL MÁXIMO OBSERVADO
    saldo = 1 640 000
    coste = 62 320 USD
    ahorro frente al actual: 28 880 USD
```

**Paso 3 — cuestiona el dato de «0 rechazos».**

```text
CERO RECHAZOS EN 250 DÍAS CON UN SALDO DE 2 400 000
NO DEMUESTRA QUE 2 400 000 SEA NECESARIO

  demuestra que 2 400 000 es SUFICIENTE.
  El saldo necesario está entre 1 640 000 y 2 400 000,
  y los datos no lo distinguen porque nunca se probó.

  ES UN SESGO CLÁSICO
    «nunca falló» con un margen amplio no informa
    sobre dónde estaría el punto de fallo
```

**Paso 4 — introduce el efecto del horario.**

```text
EL 38 % DE LOS COBROS LLEGA DESPUÉS DEL CORTE

  cobros diarios medios: supongamos 620 000
  después del corte: 620 000 × 38 % = 235 600

  ESO SIGNIFICA QUE CADA DÍA EL BANCO PREFINANCIA
  235 600 QUE YA TIENE, PERO NO PUEDE USAR

SI EL CORTE SE MOVIERA 2 HORAS
  supuesto: entraría el 60 % de ese importe antes del corte
  235 600 × 60 % = 141 360 menos de saldo necesario
  ahorro: 141 360 × 3,8 % = 5 372 USD al año

  Y ADEMÁS reduce la cola: menos días de tensión
```

**Paso 5 — evalúa el netting con el corresponsal.**

```text
FLUJOS BRUTOS DIARIOS CON EL CORRESPONSAL
  salidas   1 032 000
  entradas    620 000
  bruto     1 652 000
  neto        412 000

RATIO DE NETTING POTENCIAL
  1 − (412 000 / 1 652 000) = 75,1 %

PERO ATENCIÓN
  el netting NO reduce el saldo objetivo por sí solo
  si las entradas siguen llegando después del corte

  → el netting solo ahorra si compensa DENTRO
    de la misma ventana

  → por eso horario y netting van juntos:
    netting sin alineación de horarios es un cálculo
    que no se convierte en liquidez
```

**Paso 6 — construye el plan.**

```text
MEDIDA 1 · bajar el saldo objetivo a 1 800 000 por etapas
  1ª etapa: 2 100 000 durante 60 días, con vigilancia diaria
  2ª etapa: 1 900 000 durante 60 días
  3ª etapa: 1 800 000
  ahorro final: 600 000 × 3,8 % = 22 800 USD/año
  REGLA DE PARADA: un solo día con tensión → volver a la etapa anterior

MEDIDA 2 · negociar descubierto intradía
  límite de 500 000, comisión de disponibilidad 0,35 %
  coste: 1 750 USD/año
  permite bajar el saldo otros 400 000
  ahorro neto: 400 000 × 3,8 % − 1 750 = 13 450 USD/año

MEDIDA 3 · acordar netting bilateral con corte alineado
  requiere acuerdo con el corresponsal
  efecto: reduce la volatilidad de la posición diaria
  ahorro estimado: 8 000 USD/año

MEDIDA 4 · barrido automático de excedentes
  evita saldos ociosos por encima del objetivo
  ahorro estimado: 6 000 USD/año

TOTAL ESTIMADO: 50 250 USD/año sobre 91 200 actuales
```

**Paso 7 — declara el riesgo que se está asumiendo.**

```text
LO QUE SE GANA: 50 250 USD/AÑO
LO QUE SE ASUME

  · menos margen ante un día atípico
  · dependencia de un descubierto que el corresponsal
    puede reducir unilateralmente, y suele hacerlo
    justo cuando hay tensión de mercado
  · el netting exige que el corresponsal cumpla:
    si falla, la exposición neta es real

CONTROLES QUE ACOMPAÑAN AL PLAN
  1. vigilancia intradía de la posición, no solo al cierre
  2. alerta al 70 % del descubierto disponible
  3. prueba de tensión: simular el peor día conocido
     con el saldo nuevo, antes de cada etapa
  4. límite de exposición neta con el corresponsal
  5. plan de contingencia si el descubierto se retira

Y UNA CONDICIÓN
  el plan avanza etapa a etapa. Saltarse una etapa
  «porque va bien» convierte una reducción medida
  en una apuesta.
```

**Interpreta:** el banco tenía 91 200 dólares al año inmovilizados y el dato que
justificaba ese nivel —«nunca falló»— no lo justificaba: solo demostraba que
sobraba. La reducción se hace **por etapas con regla de parada** porque el punto
de fallo es desconocido por construcción.

## 🧭 Perspectivas

La liquidez afecta a cada participante de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Tesorería | 2,4 millones parados | Cuánto reduce |
| Cliente | Un pago rechazado por fondos | Si cambia de banco |
| Corresponsal | Descubierto solicitado | Si lo concede y a qué precio |
| Riesgo de liquidez | Colchón que se recorta | Qué prueba de tensión exige |
| Banco central | Ventanas operativas | Si amplía horarios |
| Supervisor | Ratio de liquidez | Qué exige mantener |
| Auditor | Reducción sin prueba | Si observa el proceso |

## 🏦 Del cliente al banco

El cliente no lo ve y su comisión incluye este coste. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Mi pago no salió hoy» | Falta de saldo en el nostro | 18, clase 8 |
| «Otro banco lo hace más barato» | Menos liquidez atrapada | 18, clase 8 |
| «Tengo que ordenar antes de las 12» | Corte de la ventana | 18, clase 5 |
| «Me cobran comisión de urgencia» | Uso de descubierto intradía | 18, clase 8 |

## ⚖️ Riesgos y controles

Los riesgos son de liquidez y de ventana operativa. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Saldo insuficiente | Pagos rechazados | Reducción por etapas con regla de parada |
| Descubierto retirado | El corresponsal reduce el límite en tensión | Plan de contingencia y alternativas |
| Exposición neta | El corresponsal falla antes de liquidar | Límite de exposición neta |
| Netting sin alineación | El cálculo no se convierte en liquidez | Compensar dentro de la ventana |
| Concentración por divisa | Un solo nostro grande | Segundo corresponsal probado |
| «Nunca falló» como prueba | Se confunde suficiente con necesario | Prueba de tensión antes de reducir |

## 🧪 Práctica

En [`labs/lab-02.md`](../labs/lab-02.md) y [`labs/lab-06.md`](../labs/lab-06.md):

1. Calcula el saldo objetivo por nivel de servicio con una serie de 250 días.
2. Modela el ratio de netting bilateral y multilateral de tres participantes.
3. Simula el efecto de mover el corte dos horas.
4. Diseña un plan de reducción por etapas con su regla de parada.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen costes de liquidez excesivos. Las causas son saldos objetivo mal dimensionados y netting no aplicado.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Fijar el saldo en la media | Se ignoró la cola | Usa percentiles y colchón |
| «Nunca falló, está bien» | Suficiente confundido con necesario | Reduce por etapas y observa |
| Netting sin mirar horarios | Se calculó el ratio y no la liquidez | Compensa dentro de la ventana |
| Reducción de golpe | Se buscó el ahorro rápido | Etapas con regla de parada |
| Depender del descubierto | Se supuso siempre disponible | Se retira justo en la tensión |
| Concentrar sin alternativa | Se optimizó el colchón | Segundo corresponsal probado |

## ❓ Preguntas de comprobación

1. ¿Por qué el saldo objetivo no se fija en la media de las salidas?
2. ¿Qué diferencia hay entre netting bilateral y multilateral, y qué exige el
   segundo?
3. ¿Por qué el netting sin alineación de horarios no ahorra liquidez?
4. ¿Por qué «nunca falló» no demuestra que el saldo sea necesario?
5. ¿Por qué el descubierto intradía es un colchón poco fiable en tensión?

## 📥 Entregable

Guarda en `portfolio/parte-18/clase-08/`:

- el cálculo del saldo objetivo por tres niveles de servicio;
- el ratio de netting bilateral y multilateral de un grupo de tres;
- la simulación del efecto de mover el corte;
- el plan de reducción por etapas con su regla de parada y sus controles.

## 🔗 Referencias cruzadas

- **Viene de:** clases 4 y 7; Parte 11, clase 5 (riesgo de liquidez).
- **Continúa en:** clase 13 (pagos inmediatos), clase 15 (pago contra pago).
- **Se aplica en:** Parte 23, clase 9 (liquidez multidivisa del banco digital).

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

- Committee on Payments and Market Infrastructures (2021). *Extending and aligning payment system operating hours for cross-border payments*. BIS. Efecto de alinear horarios sobre la liquidez inmovilizada. <https://www.bis.org/cpmi/publ/d194.htm>
- Committee on Payments and Market Infrastructures (2005). *New developments in large-value payment systems*. BIS. Diseños de ahorro de liquidez en sistemas de alto valor. <https://www.bis.org/cpmi/publ/d67.htm>
- Basel Committee on Banking Supervision (2013). *Basel III: The Liquidity Coverage Ratio and liquidity risk monitoring tools*. BIS. Tratamiento de la liquidez atrapada en el ratio de cobertura. <https://www.bis.org/publ/bcbs238.htm>
- Basel Committee on Banking Supervision (2008). *Principles for Sound Liquidity Risk Management and Supervision*. BIS. Gobierno de la liquidez intradía en divisas. <https://www.bis.org/publ/bcbs144.htm>
- Committee on Payments and Market Infrastructures (2020). *Enhancing cross-border payments: building blocks of a global roadmap*. BIS. Bloques del plan global que atacan el coste de liquidez. <https://www.bis.org/cpmi/publ/d193.htm>
- Verificación local: comprueba los requisitos de liquidez en moneda extranjera y las ventanas operativas aplicables en tu jurisdicción. **Fecha de verificación de esta clase: 2026-08-20.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 07 · Compensación, liquidación y finalidad](07-compensacion-liquidacion-y-finalidad.md) | [Parte 18](../README.md) · [Programa](../../../SYLLABUS.md) | [09 · El cambio de divisa dentro de un pago →](09-fx-dentro-de-un-pago-transfronterizo.md) |
<!-- gen:footer:end -->
