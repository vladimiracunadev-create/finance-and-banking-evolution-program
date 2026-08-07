<!-- meta
part: 10
class: 7
title: "Compensación y liquidación"
level: profesional
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 07 · Compensación y liquidación

> [← 06 · Transferencias](06-transferencias.md) · [Índice de la parte](../README.md) · [08 · Conciliación bancaria →](08-conciliacion-bancaria.md)

**Parte 10 — Operaciones bancarias** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Entender la infraestructura que permite que millones de operaciones diarias entre bancos se resuelvan
sin que cada una exija mover dinero físicamente. La compensación y la liquidación son invisibles para
el cliente y son el corazón operativo del sistema financiero.

Las transferencias de la clase anterior no se liquidan una a una entre bancos: se compensan. Esta clase explica ese mecanismo y el riesgo que introduce, que es el que ha producido las intervenciones más grandes de bancos centrales: entre que se compensa y se liquida, hay una exposición entre entidades.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** compensación de liquidación y explicar por qué son etapas separadas.
2. **Calcular** posiciones netas multilaterales.
3. **Identificar** los riesgos del proceso y sus mitigantes.
4. **Explicar** el papel de la contraparte central.
5. **Gestionar** la liquidez intradía necesaria para operar.

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

Los tres primeros términos son el mecanismo y su resultado; los cuatro siguientes, los riesgos y las soluciones institucionales. El **riesgo de liquidación** es el que lo justifica todo: si un participante no cumple después de que la compensación calculó las posiciones, el fallo se propaga a todos los demás.

| Concepto | Comprensión verificable |
|---|---|
| `compensación` | Cálculo de las obligaciones netas entre participantes. |
| `liquidación` | Transferencia efectiva de fondos que extingue las obligaciones. |
| `posición neta` | Diferencia entre lo que un participante debe y lo que le deben. |
| `contraparte central` | Entidad que se interpone entre las partes y garantiza el cumplimiento. |
| `liquidez intradía` | Fondos necesarios durante el día para cumplir obligaciones antes de recibir. |
| `riesgo de liquidación` | Riesgo de que una parte cumpla y la otra no. |
| `entrega contra pago` | Mecanismo que condiciona la entrega del activo al pago simultáneo. |

## 🧠 Modelo mental

La compensación reduce el movimiento de dinero de forma drástica:

```text
sin compensación: 4 bancos con 12 pares de obligaciones → 12 pagos
con compensación: se calculan 4 posiciones netas → 4 pagos (o menos)

reducción típica del monto a liquidar: 85 % a 95 %
```

Esa reducción es la razón por la que el sistema financiero puede procesar volúmenes enormes con
reservas relativamente pequeñas.

## 📖 Desarrollo

### 1. Compensación bilateral y multilateral

La compensación reduce enormemente el volumen a liquidar, y la multilateral más que la bilateral. El procedimiento siguiente las compara sobre el mismo conjunto de operaciones.

```text
OBLIGACIONES BRUTAS DEL DÍA (millones)
        A debe a    B debe a    C debe a    D debe a
  A         —         420         180         340
  B        280          —         510         120
  C        390         160          —         280
  D        150         480         220          —
```

**Compensación bilateral:**

```text
A y B: A debe 420, B debe 280 → A paga 140
A y C: A debe 180, C debe 390 → C paga 210
A y D: A debe 340, D debe 150 → A paga 190
B y C: B debe 510, C debe 160 → B paga 350
B y D: B debe 120, D debe 480 → D paga 360
C y D: C debe 280, D debe 220 → C paga 60

total a liquidar: 140 + 210 + 190 + 350 + 360 + 60 = 1 310
versus bruto: 3 530
reducción: 62,9 %
```

**Compensación multilateral:**

```text
posición neta de cada participante:
  A: paga 940, recibe 820 → posición −120 (debe)
  B: paga 910, recibe 1 060 → posición +150 (recibe)
  C: paga 830, recibe 910 → posición +80 (recibe)
  D: paga 850, recibe 740 → posición −110 (debe)

verificación: −120 + 150 + 80 − 110 = 0  ✓

total a liquidar: 230 (A y D pagan; B y C reciben)
versus bruto: 3 530
reducción: 93,5 %
```

**La compensación multilateral reduce 93,5 % del monto a mover.** Esa es su función económica.

### 2. Riesgos del proceso

El proceso introduce riesgos que la liquidación operación por operación no tiene. La tabla los recoge.

| Riesgo | Descripción | Mitigante |
|---|---|---|
| De crédito | Un participante no cumple su posición neta | Garantías, fondo de respaldo |
| De liquidez | Un participante no tiene fondos en el momento | Liquidez intradía, facilidades |
| Sistémico | El incumplimiento de uno afecta a los demás | Contraparte central, límites |
| Operacional | Falla del sistema o de un participante | Respaldo, planes de contingencia |
| Legal | Incertidumbre sobre la firmeza | Marco legal de firmeza |

**El riesgo sistémico es el que justifica toda la arquitectura:**

```text
si A no cumple su posición de −120:
  · B y C no reciben lo esperado
  · sus propias obligaciones con otros pueden incumplirse
  · el efecto se propaga

sin mitigantes, el incumplimiento de un participante puede paralizar el sistema
```

### 3. Contraparte central

Una contraparte central se interpone entre los participantes y concentra el riesgo para poder gestionarlo. El esquema muestra el cambio de estructura.

```text
sin contraparte central:  A ←→ B  (cada uno asume el riesgo del otro)
con contraparte central:  A ←→ CCP ←→ B  (ambos asumen el riesgo de la CCP)
```

**Funciones y mitigantes de una contraparte central:**

```text
· novación: se convierte en la contraparte de ambas partes
· márgenes iniciales: garantía exigida al abrir la posición
· márgenes de variación: ajuste diario según el valor de la posición
· fondo de garantía: aportes de los participantes
· cascada de recursos: orden en que se usan los recursos ante un incumplimiento
```

Si un participante incumple, esos recursos se consumen en un orden fijado de antemano, y el orden es tan importante como el importe.

```text
CASCADA DE RECURSOS TÍPICA
  1. márgenes del participante incumplidor
  2. aporte del incumplidor al fondo de garantía
  3. recursos propios de la contraparte central (tramo comprometido)
  4. fondo de garantía de los demás participantes
  5. recursos adicionales según reglas
```

**El orden importa:** el incumplidor paga primero. Ese diseño alinea incentivos y evita que el riesgo
se socialice de inmediato.

### 4. Liquidez intradía

La liquidación exige tener fondos en momentos concretos del día, y esa necesidad es distinta de la liquidez diaria. La tabla la explica.

```text
un banco debe pagar antes de recibir, y necesita fondos para ese intervalo
```

Seguido hora a hora, el saldo de un banco en el banco central deja ver los dos momentos del día en que necesita fondos que todavía no ha recibido.

```text
PERFIL INTRADÍA DE UN BANCO
  09:00  saldo inicial en el banco central: 1 200
  09:30  pagos emitidos: −2 400 · recibidos: +800 → saldo −400  ✗ DESCUBIERTO
  11:00  recibidos: +1 900 → saldo 1 500
  14:00  pagos emitidos: −2 100 → saldo −600  ✗ DESCUBIERTO
  16:00  recibidos: +2 800 → saldo 2 200
  17:00  liquidación neta: −180 → saldo final 2 020
```

**El saldo final es positivo y el banco estuvo en descubierto dos veces durante el día.** Esa
necesidad intradía se cubre con:

```text
· saldo inicial mayor (costo: fondos inmovilizados sin rendimiento)
· facilidad de liquidez intradía del banco central (garantizada, sin costo o con costo bajo)
· gestión activa del orden de los pagos (postergar los no urgentes)
· acuerdos bilaterales con otros bancos
```

**La gestión del orden de los pagos** es la herramienta de menor costo y exige coordinación: si todos
los bancos postergan sus pagos esperando recibir primero, el sistema se paraliza.

### 5. Entrega contra pago

La entrega contra pago elimina el riesgo de principal condicionando cada tramo al otro. El esquema lo muestra, y este mecanismo reaparece en la Parte 21.

```text
en operaciones de valores existe un riesgo adicional:
  A entrega los títulos y B no paga, o viceversa

ENTREGA CONTRA PAGO: ambas transferencias ocurren simultáneamente
o ninguna ocurre
```

Modelos:

```text
modelo 1  liquidación bruta simultánea de títulos y fondos
modelo 2  títulos brutos, fondos netos
modelo 3  ambos netos, al final del ciclo
```

El modelo 1 elimina el riesgo de principal por completo, a costa de mayor necesidad de liquidez.

## 🧮 Ejemplo guiado

El ejemplo compensa un conjunto de operaciones bilateral y multilateralmente. La diferencia en el importe a liquidar es grande, y explica por qué todos los sistemas compensan.

**Situación.** Un banco mediano evalúa su gestión de liquidez intradía.

```text
DATOS DEL DÍA (millones)
  saldo inicial en el banco central     840
  pagos emitidos totales              9 200
  pagos recibidos totales             9 340
  posición neta al cierre              +140
  
  máximo descubierto intradía          −1 620  a las 11:47
  facilidad de liquidez intradía usada  1 800
  garantías comprometidas               2 100
```

**Paso 1 — analiza el perfil.**

```text
el banco cierra con posición positiva de 140
y necesitó 1 800 de liquidez intradía

la posición neta NO refleja la necesidad de liquidez
```

**Paso 2 — analiza el patrón horario.**

```text
hora     emitidos   recibidos   saldo
09:00       —          —          840
10:00     2 800       420       −1 540
11:00     1 900     1 100       −2 340
11:47     ...         ...       −1 620 (tras recibir 720)
12:00       800     2 400          −20
14:00     2 200     1 800         −420
16:00     1 500     3 620        1 700
17:00       —         —          1 700
17:30    liquidación neta +140    1 840
```

**Paso 3 — identifica la causa del descubierto.**

```text
entre las 09:00 y las 11:00 el banco emitió 4 700 y recibió 1 520
ratio emitido/recibido en la primera hora: 6,7x

comparación con el sistema:
  promedio del sistema en la primera hora: 1,4x
  
→ el banco paga MUY temprano respecto de cuando recibe
```

**Paso 4 — investiga por qué.**

```text
composición de los pagos emitidos entre 09:00 y 10:00:
  pagos de clientes con instrucción de "primera hora"      1 200
  pagos propios de tesorería                                 900
  liquidación de operaciones de mercado                      700
  TOTAL                                                    2 800

de esos 2 800:
  urgentes (con hora comprometida):                          800
  no urgentes (podrían ejecutarse más tarde):              2 000
```

**Paso 5 — simula la reprogramación.**

```text
si los 2 000 no urgentes se ejecutan a las 12:00 en lugar de 09:30:

hora     emitidos   recibidos   saldo
09:00       —          —          840
10:00       800       420          460
11:00     1 900     1 100         −340
12:00     2 800     2 400         −740
14:00     2 200     1 800        −1 140
16:00     1 500     3 620          980
17:00       —         —            980

máximo descubierto: −1 140 (antes −2 340)
reducción: 51 %
```

**Paso 6 — cuantifica el ahorro.**

```text
liquidez intradía requerida: de 1 800 a 1 140
garantías comprometidas: de 2 100 a 1 350

las garantías comprometidas son títulos que no pueden usarse para otra cosa
costo de oportunidad estimado: 0,8 % anual sobre el monto comprometido

ahorro anual = 750 × 0,008 = 6 millones
```

**Paso 7 — el riesgo de la reprogramación.**

```text
si TODOS los bancos posponen sus pagos:
  · nadie recibe temprano
  · todos necesitan más liquidez inicial
  · el sistema se congestiona
  · en el extremo, se produce un bloqueo de pagos

este es un problema de coordinación clásico:
  la estrategia óptima individual (pagar tarde) es subóptima colectivamente
```

**Mitigantes que los sistemas de pago aplican:**

```text
· cortes horarios que obligan a ejecutar un porcentaje antes de cierta hora
· algoritmos de optimización que buscan compensaciones dentro del día
· mecanismos de resolución de bloqueos (gridlock resolution)
· incentivos de precio: tarifa menor para pagos tempranos
```

**Paso 8 — decisión.**

```text
IMPLEMENTAR reprogramación PARCIAL
  · postergar solo los pagos propios de tesorería no urgentes: 900
  · mantener los pagos de clientes en su horario comprometido
  · máximo descubierto estimado: −1 700 (reducción de 27 %)
  · ahorro estimado: 3 millones anuales

FUNDAMENTO DE LA MODERACIÓN
  postergar los 2 000 completos optimiza al banco y contribuye a la
  congestión del sistema. El banco es participante de una infraestructura
  compartida y su comportamiento afecta a los demás.
  
  la reprogramación de los pagos propios captura la mayor parte del beneficio
  sin trasladar el costo al sistema.

ADEMÁS
  · negociar con clientes de alto volumen horarios de pago más distribuidos
  · monitorear el perfil intradía diariamente, no solo la posición neta
  · establecer un umbral de alerta: descubierto máximo sobre 1 500
```

**Interpreta:** el banco cerraba con posición positiva y **necesitaba 1 800 de liquidez intradía por
un problema de secuencia, no de solvencia**. La reprogramación captura un ahorro real, y la decisión
de moderarla reconoce que el banco opera en una infraestructura compartida donde la optimización
individual completa produce externalidades.

## 🏦 Del cliente al banco

El cliente ve una transferencia y el banco gestiona posiciones netas y liquidez intradía. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del sistema | Parte |
|---|---|---|
| Transferencia que llega en minutos | Compensación y liquidación en segundo plano | 10, clase 6 |
| Horario de corte | Determina el ciclo de liquidación | 10, clase 1 |
| Operación de valores en T+2 | Ciclo de liquidación con entrega contra pago | 8, clase 2 |
| Sistema no disponible | Falla operativa de la infraestructura | 11, clase 14 |
| Garantías del banco inmovilizadas | Liquidez intradía comprometida | 11, clase 4 |

## 🧪 Práctica

El laboratorio pide compensar por los dos métodos y medir el riesgo de liquidación resultante. La reducción de volumen viene con una concentración de riesgo, y verlo así prepara la Parte 11.

En `labs/lab-04.md`:

1. Calcula posiciones netas bilaterales y multilaterales de un conjunto de obligaciones.
2. Compara la reducción de monto a liquidar entre ambos métodos.
3. Construye el perfil intradía de un banco e identifica su máximo descubierto.
4. Simula una reprogramación de pagos y cuantifica el ahorro y el riesgo sistémico.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen fallos de liquidación. Las causas son liquidez intradía mal dimensionada y ausencia de entrega contra pago.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se gestiona solo la posición neta | Necesidad intradía ignorada | Construye el perfil horario. |
| Se posponen todos los pagos | Externalidad al sistema | Modera: es una infraestructura compartida. |
| No se distingue compensación de liquidación | Conceptos confundidos | Compensar calcula; liquidar transfiere. |
| Se subestima el riesgo sistémico | Efecto de red ignorado | El incumplimiento de uno afecta a todos. |
| Garantías comprometidas sin optimizar | Costo de oportunidad no medido | Gestiona el perfil para liberar garantías. |
| Se supone que la contraparte central elimina el riesgo | Lo transforma, no lo elimina | El riesgo pasa a ser el de la contraparte central. |

## ❓ Preguntas de comprobación

1. ¿Qué diferencia hay entre compensación y liquidación?
2. Calcula la reducción de monto a liquidar de una compensación multilateral.
3. ¿Cuál es el orden de la cascada de recursos de una contraparte central y por qué?
4. ¿Por qué un banco con posición neta positiva puede necesitar liquidez intradía?
5. ¿Por qué postergar todos los pagos es individualmente óptimo y colectivamente subóptimo?

## 📥 Entregable

Guarda en `portfolio/parte-10/clase-07/`:

- el cálculo de posiciones netas bilaterales y multilaterales con su comparación;
- el perfil intradía construido con el máximo descubierto identificado;
- la simulación de reprogramación con ahorro y riesgo cuantificados;
- el análisis de la cascada de recursos de una contraparte central.

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

- Committee on Payments and Market Infrastructures (2012). *Principles for Financial Market Infrastructures*. CPMI-IOSCO/BIS. Marco completo de compensación, liquidación y contrapartes centrales. <https://www.bis.org/cpmi/publ/d101.htm>
- Committee on Payments and Market Infrastructures (2013). *Monitoring tools for intraday liquidity management*. BIS. <https://www.bis.org/publ/bcbs248.htm>
- Bank for International Settlements (2005). *New developments in large-value payment systems*. CPSS.
- Bech, M. y Garratt, R. (2003). "The Intraday Liquidity Management Game". *Journal of Economic Theory*. Problema de coordinación en el orden de los pagos.
- Duffie, D. (2011). *How Big Banks Fail and What to Do about It*. Princeton University Press. Riesgo de liquidación y contrapartes centrales.
- Verificación local: revisa los sistemas de compensación y liquidación de tu país, sus horarios, sus reglas de garantías y las facilidades de liquidez intradía del banco central.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 06 · Transferencias](06-transferencias.md) | [Parte 10](../README.md) · [Programa](../../../SYLLABUS.md) | [08 · Conciliación bancaria →](08-conciliacion-bancaria.md) |
<!-- gen:footer:end -->
