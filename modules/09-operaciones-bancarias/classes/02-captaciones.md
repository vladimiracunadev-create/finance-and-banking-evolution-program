<!-- meta
part: 10
class: 2
title: "Captaciones"
level: profesional
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 02 · Captaciones

> [← 01 · Modelo operativo de un banco](01-modelo-operativo-de-un-banco.md) · [Índice de la parte](../README.md) · [03 · Colocaciones →](03-colocaciones.md)

**Parte 10 — Operaciones bancarias** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Gestionar el lado del balance que financia todo lo demás. Las captaciones determinan el costo de
fondos, la estabilidad del banco y su capacidad de crecer. Esta clase enseña a analizar su
composición, a medir su estabilidad y a fijar su precio.

El modelo operativo de la clase anterior mueve dinero ajeno. Esta explica de dónde sale ese dinero, que es la materia prima del negocio bancario. Y añade la variable que decide cuánto cuesta: no todos los depósitos son igual de estables, y la parte estable vale mucho más que la volátil.

## 📚 Objetivos

Al finalizar podrás:

1. **Clasificar** las fuentes de fondeo por costo, estabilidad y plazo.
2. **Calcular** el costo de fondos y su composición.
3. **Medir** la estabilidad de los depósitos y su comportamiento.
4. **Fijar** el precio de un producto de captación.
5. **Evaluar** la concentración y el riesgo del fondeo.

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

Los tres primeros términos son las fuentes de fondeo; los cuatro siguientes, cómo se mide su estabilidad y su costo. El **saldo núcleo** es el concepto operativo: la parte de los depósitos a la vista que permanece pese a los movimientos individuales, y que por eso se puede financiar a largo plazo.

| Concepto | Comprensión verificable |
|---|---|
| `captación` | Fondos recibidos del público o del mercado. Constituyen el pasivo del banco. |
| `depósito a la vista` | Sin plazo, retirable en cualquier momento. Bajo costo, alta volatilidad teórica. |
| `depósito a plazo` | Con vencimiento pactado. Mayor costo, mayor estabilidad. |
| `saldo núcleo` | Porción de los depósitos a la vista que permanece de forma estable. |
| `beta de depósitos` | Proporción de un cambio en la tasa de mercado que se traslada al depositante. |
| `costo de fondos` | Costo promedio ponderado de todas las fuentes. |
| `concentración de fondeo` | Dependencia de pocos depositantes o de una sola fuente. |

## 🧠 Modelo mental

Las captaciones se evalúan en **tres dimensiones simultáneas**:

```text
COSTO         cuánto cuesta el fondo
ESTABILIDAD   cuánto permanece ante un evento de estrés
PLAZO         cuánto dura contractualmente
```

Las tres suelen ir en direcciones opuestas: **el fondeo más barato es el menos estable**, y el más
estable es el más caro. La composición óptima equilibra las tres.

## 📖 Desarrollo

### 1. Fuentes de fondeo

Un banco se financia de varias fuentes con costos y estabilidades muy distintos. La tabla las compara.

| Fuente | Costo | Estabilidad | Plazo |
|---|---|---|---|
| Depósitos a la vista de personas | Muy bajo | **Alta** | Indefinido |
| Depósitos a la vista de empresas | Bajo | Media | Indefinido |
| Depósitos a plazo minoristas | Medio | Alta | Definido |
| Depósitos a plazo mayoristas | Medio-alto | **Baja** | Definido |
| Bonos emitidos | Alto | Muy alta | Largo |
| Financiamiento interbancario | Variable | **Muy baja** | Muy corto |
| Financiamiento del banco central | Variable | Contingente | Corto |
| Patrimonio | El más alto | Permanente | Permanente |

**La paradoja del depósito a la vista:** contractualmente puede retirarse hoy y **en la práctica es la
fuente más estable**, porque el comportamiento agregado de miles de depositantes es predecible. Esa es
la base de la transformación de plazos.

### 2. Costo de fondos

El costo de fondos es el promedio ponderado de todas las fuentes, y es el suelo de cualquier tasa de colocación. El procedimiento siguiente lo calcula.

```text
costo de fondos = Σ (saldo_i × tasa_i) / Σ saldo_i
```

El promedio ponderado se calcula fuente a fuente, y la última fila muestra por qué la composición del fondeo importa tanto como su volumen.

```text
Fuente                        saldo      tasa     costo
depósitos a la vista        420 000     0,30 %    1 260
depósitos a plazo ≤ 90 d    380 000     5,80 %   22 040
depósitos a plazo > 90 d    260 000     6,40 %   16 640
bonos emitidos              180 000     7,20 %   12 960
interbancario                60 000     6,90 %    4 140
TOTAL                     1 300 000              57 040

costo de fondos = 57 040/1 300 000 = 4,39 %
```

**Costo marginal frente a costo medio:**

```text
costo medio: 4,39 %
si el crecimiento se financia con depósitos a plazo al 6,40 %:
  costo MARGINAL del nuevo fondeo: 6,40 %

la decisión de colocar un crédito adicional debe evaluarse contra el costo
MARGINAL, no contra el medio
```

Usar el costo medio para decidir operaciones marginales lleva a colocar por debajo del costo real.

### 3. Estabilidad y saldo núcleo

El saldo núcleo se estima observando el comportamiento histórico del agregado, no de las cuentas individuales. El procedimiento lo obtiene.

```text
saldo núcleo = porción de los depósitos a la vista que permanece
               ante un escenario de estrés definido
```

**Método de estimación:**

```text
1. analizar la serie histórica de saldos diarios (mínimo 3 años)
2. identificar la caída máxima observada en un periodo de 30 días
3. segmentar por tipo de cliente y por rango de saldo
4. estimar el porcentaje que permanece bajo estrés
```

Aplicado a dos tipos de depositante, el procedimiento entrega saldos núcleo muy distintos, y esa diferencia es la que se lleva a la gestión de liquidez.

```text
depósitos a la vista de personas, análisis de 5 años:
  saldo promedio                       320 000
  caída máxima en 30 días (observada)   −4,2 %
  caída máxima en 30 días (estrés)      −12 %  (supuesto prudencial)
  SALDO NÚCLEO estimado: 88 %

depósitos a la vista de empresas:
  caída máxima observada                −18,4 %
  caída bajo estrés                     −40 %
  SALDO NÚCLEO estimado: 60 %
```

**Factores que determinan la estabilidad:**

| Factor | Mayor estabilidad | Menor estabilidad |
|---|---|---|
| Tipo de cliente | Persona natural | Institucional o mayorista |
| Monto | Bajo el límite de garantía | Sobre el límite |
| Relación | Cuenta operativa principal | Cuenta secundaria |
| Antigüedad | Alta | Reciente |
| Productos asociados | Nómina, pagos automáticos | Solo depósito |
| Canal de captación | Sucursal, relación | Plataforma de comparación de tasas |

**El último factor merece atención:** los depósitos captados por diferencial de tasa en plataformas de
comparación se van con la misma facilidad con que llegaron. Su estabilidad es sustancialmente menor
aunque el producto sea idéntico.

### 4. Fijar el precio

El precio de una captación se fija con la curva de mercado y con el valor que ese fondo tiene para el banco. La tabla recoge los criterios.

```text
tasa de captación = tasa de referencia − diferencial
```

El diferencial depende de:

```text
· la estabilidad esperada del depósito
· el valor de la relación con el cliente
· la necesidad de fondeo del banco
· la competencia
· el costo de otras fuentes alternativas
```

Traducidos a un diferencial concreto, esos criterios explican por qué dos depósitos del mismo plazo pagan tasas distintas.

```text
ejemplo de estructura:
  depósito a plazo 90 días, minorista, cliente con nómina
    tasa de referencia 6,50 % − diferencial 0,70 % = 5,80 %
  
  depósito a plazo 90 días, mayorista, sin relación
    tasa de referencia 6,50 % − diferencial 0,10 % = 6,40 %
```

**El cliente con relación recibe menos tasa y aporta más valor:** su depósito es más estable y trae
otros productos. Esa lógica —precio por valor de la relación, no solo por monto— es la base de la
segmentación de la clase 15.

### 5. Concentración y riesgo del fondeo

Un fondeo concentrado en pocos depositantes es frágil aunque sea barato. La tabla recoge los indicadores de concentración.

```text
indicadores de concentración:
  · % del fondeo de los 10 mayores depositantes
  · % del fondeo de una sola fuente (interbancario, bonos)
  · % del fondeo con vencimiento en 30 días
  · % del fondeo sobre el límite de garantía de depósitos
```

Puestos uno junto a otro, los indicadores de dos bancos revelan perfiles de fragilidad muy diferentes ante la misma tensión.

```text
                                        banco A    banco B
10 mayores depositantes / total           8,4 %     31,2 %
fondeo mayorista / total                 22,0 %     54,0 %
vencimientos ≤ 30 días / total           18,4 %     42,6 %
sobre el límite de garantía / total      26,0 %     61,0 %
```

**El banco B tiene un fondeo estructuralmente más frágil**, aunque su costo de fondos pueda ser
similar. En un evento de estrés, la proporción que puede retirarse rápidamente es más del doble.

## 🧮 Ejemplo guiado

El ejemplo calcula el costo de fondos de un banco y estima su saldo núcleo. Conviene comparar el costo medio con el marginal: el segundo es el que decide si conviene captar más.

**Situación.** Un banco evalúa su estructura de fondeo tras un alza de tasas de 300 puntos base.

```text
ESTRUCTURA ANTES DEL ALZA
  fuente                    saldo      tasa    participación
  vista personas          380 000     0,20 %      29,2 %
  vista empresas          140 000     0,40 %      10,8 %
  plazo minorista         310 000     4,10 %      23,8 %
  plazo mayorista         220 000     4,60 %      16,9 %
  bonos                   180 000     5,80 %      13,8 %
  interbancario            70 000     4,80 %       5,4 %
  TOTAL                 1 300 000                100,0 %
  costo de fondos: 2,88 %
```

**Paso 1 — estima las betas de cada fuente.**

```text
fuente                beta estimada    fundamento
vista personas            0,08         alta inercia, baja sensibilidad
vista empresas            0,25         mayor sensibilidad, negociación
plazo minorista           0,72         se repacta al vencimiento
plazo mayorista           0,95         altamente sensible a la tasa
bonos                     0,00         tasa fija hasta el vencimiento
interbancario             1,00         se repacta diariamente
```

**Paso 2 — proyecta el costo tras el alza de 300 pb.**

```text
fuente                nueva tasa            saldo      costo
vista personas    0,20 + 3,00×0,08 = 0,44 % 380 000     1 672
vista empresas    0,40 + 3,00×0,25 = 1,15 % 140 000     1 610
plazo minorista   4,10 + 3,00×0,72 = 6,26 % 310 000    19 406
plazo mayorista   4,60 + 3,00×0,95 = 7,45 % 220 000    16 390
bonos             5,80 + 0        = 5,80 %  180 000    10 440
interbancario     4,80 + 3,00     = 7,80 %   70 000     5 460
TOTAL                                     1 300 000    54 978

costo de fondos: 4,23 %  (antes 2,88 %)
aumento: 1,35 puntos ante un alza de 300 pb
beta agregada: 1,35/3,00 = 0,45
```

**Paso 3 — el efecto de la migración de depósitos.**

```text
con tasas de plazo en 6,26 % y vista en 0,44 %, la brecha es de 5,82 puntos
comportamiento esperado: migración de vista hacia plazo

estimación: 22 % de los depósitos a la vista de personas migran
  380 000 × 0,22 = 83 600 migran de 0,44 % a 6,26 %
  costo adicional = 83 600 × (0,0626 − 0,0044) = 4 866
```

```text
costo de fondos con migración: (54 978 + 4 866)/1 300 000 = 4,60 %
beta efectiva: (4,60 − 2,88)/3,00 = 0,57
```

**La migración eleva la beta efectiva de 0,45 a 0,57.** Ese efecto es el que suele subestimarse en las
proyecciones.

**Paso 4 — evalúa el efecto en el margen.**

```text
el activo tiene una beta de 0,78 (Parte 6, clase 14)
  rendimiento del activo sube: 3,00 × 0,78 = 2,34 puntos
  costo de fondos sube:        1,72 puntos (con migración)
  MARGEN mejora: 0,62 puntos

pero el efecto es transitorio:
  a los 12 meses, más depósitos a plazo se habrán repactado
  beta de fondeo a 12 meses estimada: 0,71
  costo sube 2,13 puntos → margen mejora solo 0,21 puntos
```

**Paso 5 — analiza la concentración y la estabilidad.**

```text
tras la migración, la estructura sería:
  vista personas          296 400    22,8 %  (antes 29,2 %)
  vista empresas          140 000    10,8 %
  plazo minorista         393 600    30,3 %  (antes 23,8 %)
  plazo mayorista         220 000    16,9 %
  bonos                   180 000    13,8 %
  interbancario            70 000     5,4 %

fondeo estable (vista núcleo + plazo minorista + bonos):
  antes:   296 400 (núcleo vista 88 %+60 %) + 310 000 + 180 000 = 810 000  = 62,3 %
  después: 344 400 (núcleo) ... recalculando:
    núcleo vista personas: 296 400 × 0,88 = 260 832
    núcleo vista empresas: 140 000 × 0,60 = 84 000
    plazo minorista: 393 600
    bonos: 180 000
    TOTAL ESTABLE: 918 432 = 70,6 %
```

**La migración empeora el costo y mejora la estabilidad.** El depósito a plazo es más caro y no se
retira antes del vencimiento.

**Paso 6 — decisiones.**

```text
1. GESTIONAR LA MIGRACIÓN, NO IMPEDIRLA
   ofrecer productos de plazo a los clientes de vista, con tasa competitiva
   es preferible que migren dentro del banco a que migren a otro

2. DEFENDER EL SALDO NÚCLEO
   · vincular con nómina y pagos automáticos (aumenta la inercia)
   · beneficios no monetarios que no requieren pagar tasa
   · segmentar: pagar tasa solo donde el cliente efectivamente compara

3. REDUCIR LA DEPENDENCIA DEL FONDEO MAYORISTA
   objetivo: bajar de 16,9 % a 12 % en 18 meses
   sustituir con emisión de bonos de largo plazo

4. AJUSTAR EL PRICING DE COLOCACIONES
   el costo marginal de fondeo es 6,26 %, no el medio de 4,60 %
   toda operación nueva debe evaluarse contra el marginal

5. PROYECTAR EL MARGEN A 12 Y 24 MESES
   la mejora de 0,62 puntos es transitoria: comunicarlo al comité
   para evitar decisiones basadas en un margen que se comprimirá
```

**Interpreta:** el alza de tasas mejoró el margen **en el corto plazo** por la baja beta del fondeo a
la vista, y ese beneficio se erosiona a medida que los depósitos se repactan y migran. Presentar la
mejora de 0,62 puntos sin advertir que a 12 meses será de 0,21 sería un error de comunicación con
consecuencias en la planificación.

## 🏦 Del cliente al banco

El cliente deposita y el banco obtiene su fuente de financiamiento más barata. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| "Mi cuenta vista no paga nada" | Beta baja: el banco traslada poco | 3, clase 2 |
| Depósito a plazo con mejor tasa | Fondeo más caro y más estable | 3, clase 10 |
| Tasa mejor por ser cliente antiguo | Precio por valor de la relación | 15, clase 6 |
| Renovación automática | Retención de fondeo a bajo costo de gestión | 3, clase 10 |
| Depósito sobre el límite de garantía | Menor estabilidad para el banco | 3, clase 1 |

## 🧪 Práctica

El laboratorio pide calcular el costo de fondos y el saldo núcleo de un banco sintético. La proporción de saldo núcleo decide cuánto puede prestar a largo plazo.

En `labs/lab-01.md`, sección de captaciones:

1. Calcula el costo de fondos medio y marginal de una estructura dada.
2. Estima el saldo núcleo de dos tipos de depósito con series históricas.
3. Proyecta el costo de fondos ante un alza de 300 pb con betas diferenciadas.
4. Evalúa la concentración del fondeo con los cuatro indicadores.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen problemas de fondeo. Las causas son la concentración y un saldo núcleo estimado en periodos tranquilos.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se decide con el costo medio | Costo marginal ignorado | Evalúa operaciones nuevas contra el marginal. |
| Se supone beta cero en depósitos a la vista | Migración no considerada | Estima la beta efectiva con migración. |
| Se trata todo depósito a la vista igual | Estabilidad heterogénea | Segmenta por tipo de cliente y monto. |
| Se compite solo por tasa | Fondeo caro y volátil | Vincula con productos que aumenten la inercia. |
| La mejora de margen se proyecta permanente | Efecto transitorio | Proyecta a 12 y 24 meses. |
| No se mide la concentración | Fragilidad no detectada | Calcula los cuatro indicadores. |

## ❓ Preguntas de comprobación

1. ¿Por qué el depósito a la vista es contractualmente inestable y prácticamente estable?
2. ¿Cuál es la diferencia entre costo medio y marginal de fondos, y cuál se usa para decidir?
3. ¿Qué es la beta de depósitos y cómo se estima?
4. ¿Por qué la migración de vista a plazo eleva la beta efectiva?
5. Nombra cuatro indicadores de concentración del fondeo.

## 📥 Entregable

Guarda en `portfolio/parte-10/clase-02/`:

- el costo de fondos medio y marginal de una estructura;
- el saldo núcleo estimado de dos tipos de depósito con su metodología;
- la proyección del costo ante un alza de 300 pb con migración;
- los cuatro indicadores de concentración con su interpretación.

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

- Rose, P. y Hudgins, S. (2013). *Bank Management & Financial Services* (9.ª ed.). McGraw-Hill. Capítulos 12 y 13: gestión de pasivos y fijación de precios de depósitos.
- Saunders, A. y Cornett, M. (2021). *Financial Institutions Management* (10.ª ed.). McGraw-Hill. Gestión del fondeo y del riesgo de liquidez.
- Basel Committee on Banking Supervision (2013). *Basel III: The Liquidity Coverage Ratio*. BIS. Factores de salida por tipo de depósito. <https://www.bis.org/publ/bcbs238.htm>
- Basel Committee on Banking Supervision (2014). *Basel III: The Net Stable Funding Ratio*. BIS. Estabilidad del fondeo.
- Drechsler, I., Savov, A. y Schnabl, P. (2017). "The Deposits Channel of Monetary Policy". *Quarterly Journal of Economics*. Betas de depósitos.
- Verificación local: revisa los factores de salida por tipo de depósito que aplica tu supervisor y el límite vigente de la garantía de depósitos.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 01 · Modelo operativo de un banco](01-modelo-operativo-de-un-banco.md) | [Parte 10](../README.md) · [Programa](../../../SYLLABUS.md) | [03 · Colocaciones →](03-colocaciones.md) |
<!-- gen:footer:end -->
