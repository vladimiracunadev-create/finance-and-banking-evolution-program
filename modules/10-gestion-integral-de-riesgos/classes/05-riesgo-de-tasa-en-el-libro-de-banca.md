---
part: 11
class: 5
title: "Riesgo de tasa en el libro de banca"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 05 · Riesgo de tasa en el libro de banca

> [← 04 · Riesgo de liquidez](04-riesgo-de-liquidez.md) · [Índice de la parte](../README.md) · [06 · Riesgo de mercado y valor en riesgo →](06-riesgo-de-mercado-y-valor-en-riesgo.md)

**Parte 11 — Gestión integral de riesgos** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Medir y gestionar el efecto de los movimientos de tasas sobre el balance estructural de un banco. Es el
riesgo más grande que no aparece en el estado de resultados hasta que ya ocurrió, y el que puede
destruir el patrimonio económico de un banco que muestra utilidades.

Esta clase mide lo que ocurre cuando cambian las tasas, que para un banco es doblemente grave: cambia lo que gana este año y cambia el valor de todo su balance. Las dos cosas se miden por separado y pueden apuntar en direcciones opuestas, y esa contradicción es el centro de la clase.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** las cuatro fuentes del riesgo de tasa en el libro de banca.
2. **Calcular** la sensibilidad del margen financiero a un movimiento de tasas.
3. **Calcular** la sensibilidad del valor económico del patrimonio.
4. **Explicar** por qué ambas medidas pueden dar señales opuestas.
5. **Aplicar** escenarios de tasa estandarizados y evaluar su resultado.

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

Los cuatro primeros términos son las fuentes del riesgo; los cuatro siguientes, las dos medidas y su marco. El **riesgo de opcionalidad** es el que más sorprende: los clientes prepagan cuando conviene prepagar y retiran cuando conviene retirar, y esa opción es gratuita para ellos y cara para el banco.

| Concepto | Comprensión verificable |
|---|---|
| `riesgo de repreciación` | Diferencia de fechas en que activos y pasivos ajustan su tasa. |
| `riesgo de curva` | Cambios en la forma de la curva, no solo en su nivel. |
| `riesgo de base` | Activos y pasivos ligados a índices distintos que no se mueven igual. |
| `riesgo de opcionalidad` | Prepagos, retiros anticipados y topes que el cliente ejerce a su favor. |
| `margen financiero` | Diferencia entre ingresos y gastos por intereses. Visión de corto plazo. |
| `valor económico del patrimonio` | Valor presente de activos menos pasivos. Visión de largo plazo. |
| `brecha de duración` | Duración del activo menos duración del pasivo ajustada por apalancamiento. |
| `escenario estandarizado` | Los seis choques de tasa que el marco supervisor exige aplicar. |

## 🧠 Modelo mental

El modelo mental es una balanza con dos platillos que no se pueden equilibrar a la vez: proteger el margen del año exige una estructura de plazos, y proteger el valor económico del patrimonio exige otra. Elegir cuál se protege es una decisión del comité, no un cálculo.

```text
DOS FORMAS DE MIRAR EL MISMO RIESGO

MARGEN FINANCIERO          ¿cuánto gano el próximo año?
  horizonte 12 meses       lo ve el estado de resultados
  ve solo lo que repacta   sensible al tramo corto

VALOR ECONÓMICO            ¿cuánto vale el banco hoy?
  horizonte: toda la vida  no lo ve el estado de resultados
  del balance              sensible al tramo largo
```

**El error consiste en gestionar solo el primero.** Un banco puede cubrir su margen a 12 meses y estar
destruyendo su valor económico. La supervisión exige medir ambos precisamente porque pueden apuntar en
direcciones opuestas.

## 📖 Desarrollo

### 1. Las cuatro fuentes

El riesgo de tasa tiene cuatro orígenes distintos y cada uno exige una medición propia. La tabla los recoge.

```text
1. REPRECIACIÓN   activos y pasivos ajustan tasa en momentos distintos
   ejemplo: crédito a 5 años fijo, financiado con depósito a 90 días

2. CURVA          la curva cambia de forma, no solo de nivel
   ejemplo: el tramo corto sube y el largo baja (aplanamiento)
   una posición cubierta ante un desplazamiento paralelo
   puede quedar expuesta a un aplanamiento

3. BASE           activos y pasivos ligados a índices distintos
   ejemplo: crédito indexado a un índice interbancario,
   depósito remunerado a la tasa de política, ambos "variables"
   pero con correlación menor a uno

4. OPCIONALIDAD   el cliente ejerce opciones a su favor
   · prepaga el hipotecario cuando las tasas bajan
   · retira el depósito a plazo cuando las tasas suben
   · el banco queda con la peor parte de ambos movimientos
```

**La opcionalidad es asimétrica y sistemáticamente desfavorable al banco.** El cliente ejerce cuando le
conviene, y lo que le conviene al cliente perjudica al banco. Modelar prepagos y retiros con supuestos
neutrales subestima la exposición.

### 2. Sensibilidad del margen

La sensibilidad del margen mide el efecto sobre el resultado de los próximos doce meses. El procedimiento siguiente la calcula.

```text
BRECHA DE REPRECIACIÓN por tramo temporal

  brecha_t = activos que repactan en t − pasivos que repactan en t

  Δ margen ≈ Σ  brecha_t × Δtasa × (días restantes del año / 365)
```

| Signo de la brecha | Si las tasas suben | Si las tasas bajan |
|---|---|---|
| Positiva (activos > pasivos) | Margen sube | Margen baja |
| Negativa (pasivos > activos) | Margen baja | Margen sube |
| Cero | Sin efecto por nivel | Sin efecto por nivel |

**Limitación estructural:** el margen a 12 meses solo captura lo que repacta en ese plazo. Un banco con
todo su descalce más allá de 12 meses mostrará sensibilidad cero del margen y una exposición enorme.

### 3. Sensibilidad del valor económico

La sensibilidad del valor económico mide el efecto sobre el valor presente de todo el balance. El procedimiento la calcula, y usa la duración de la Parte 7.

```text
VALOR ECONÓMICO = VP(activos) − VP(pasivos)

Δ VEP ≈ − brecha de duración × Δtasa × activos totales

  brecha de duración = D_activo − D_pasivo × (pasivos / activos)
```

```text
EJEMPLO
  activos 1 000, duración 4,2
  pasivos   920, duración 1,6
  brecha = 4,2 − 1,6 × 0,92 = 4,2 − 1,472 = 2,728

  alza de 200 pb:
  Δ VEP ≈ −2,728 × 0,02 × 1 000 = −54,6
  patrimonio contable 80 → pérdida de valor del 68 % del patrimonio
```

**Ese resultado no aparece en el estado de resultados si los activos se miden a costo amortizado.** El
banco sigue reportando utilidades mientras su patrimonio económico se erosiona. Es exactamente el
mecanismo de las quiebras bancarias de 2023.

### 4. Los seis escenarios estandarizados

El marco supervisor exige aplicar seis choques:

```text
1. desplazamiento paralelo al alza
2. desplazamiento paralelo a la baja
3. empinamiento    (corto baja, largo sube)
4. aplanamiento    (corto sube, largo baja)
5. alza del tramo corto
6. baja del tramo corto
```

```text
CRITERIO DE ATENCIÓN SUPERVISORA
  si la caída del valor económico en el PEOR de los seis escenarios
  supera el 15 % del capital nivel 1 ordinario,
  el banco es considerado atípico y debe explicarlo
```

### 5. Depósitos sin vencimiento: el problema central

Los depósitos a la vista no tienen vencimiento contractual y sí tienen un comportamiento estimable, y de esa estimación depende todo el cálculo. El esquema plantea el problema.

```text
un depósito a la vista no tiene fecha de repreciación contractual
pero SÍ tiene comportamiento de repreciación

  ¿cuánto sube la tasa del depósito cuando sube la de mercado?
  → coeficiente de traspaso (beta del depósito)

  ¿cuánto tiempo permanece el saldo?
  → vida media conductual
```

| Producto | Traspaso típico | Vida media supuesta |
|---|---:|---|
| Cuenta corriente no remunerada | 0 % | Larga (3–5 años) |
| Cuenta corriente remunerada | 20–40 % | Media (2–4 años) |
| Ahorro | 40–60 % | Media |
| Depósito a plazo | 90–100 % | Su vencimiento |

```text
EL SUPUESTO QUE MÁS PESA: la vida media de los depósitos a la vista

  vida media larga  → el depósito se comporta como pasivo largo
                    → reduce la brecha de duración
                    → el banco parece menos expuesto

  el marco supervisor LIMITA la vida media que puede suponerse
  (habitualmente 5 años como máximo para el núcleo estable),
  precisamente porque es el supuesto más fácil de estirar
```

## 🧮 Ejemplo guiado

El ejemplo calcula las dos sensibilidades del mismo balance ante el mismo movimiento de tasas. Los signos son opuestos, y esa es exactamente la contradicción que el comité tiene que resolver.

**Situación.** Un banco mide su exposición con ambas métricas y obtiene señales contradictorias.

```text
BALANCE (valores en millones)
  ACTIVOS                        monto   duración   repacta ≤12m
  efectivo y líquidos            84 000     0,2       84 000
  créditos comerciales variables 320 000    0,3      320 000
  créditos consumo fijos         180 000    1,8       62 000
  hipotecarios fijos             410 000    6,4       38 000
  inversiones a vencimiento      206 000    5,1       21 000
  TOTAL ACTIVOS                1 200 000

  PASIVOS                        monto   duración   repacta ≤12m
  cuenta corriente               290 000    3,5*          0
  ahorro                         246 000    2,8*      98 400
  depósitos a plazo              384 000    0,6      346 000
  emisiones                      142 000    3,9       28 000
  TOTAL PASIVOS                1 062 000
  PATRIMONIO                     138 000

  * duración conductual supuesta
```

**Paso 1 — calcula la brecha de repreciación a 12 meses.**

```text
activos que repactan ≤ 12m:  84 000+320 000+62 000+38 000+21 000 = 525 000
pasivos que repactan ≤ 12m:        0+ 98 400+346 000+ 28 000     = 472 400

BRECHA = +52 600  (positiva)
```

**Paso 2 — calcula la sensibilidad del margen.**

```text
alza de 200 pb, efecto medio a 6 meses del año:
  Δ margen ≈ 52 600 × 0,02 × 0,5 = +526

el margen MEJORA con el alza de tasas
señal: el banco está bien posicionado
```

**Paso 3 — calcula la duración del activo.**

```text
D_activo = Σ (peso × duración)
  84 000/1 200 000 × 0,2 = 0,070 × 0,2 = 0,014
  320 000/1 200 000 × 0,3 = 0,267 × 0,3 = 0,080
  180 000/1 200 000 × 1,8 = 0,150 × 1,8 = 0,270
  410 000/1 200 000 × 6,4 = 0,342 × 6,4 = 2,187
  206 000/1 200 000 × 5,1 = 0,172 × 5,1 = 0,875
  D_activo = 3,426
```

**Paso 4 — calcula la duración del pasivo.**

```text
D_pasivo = Σ (peso × duración)
  290 000/1 062 000 × 3,5 = 0,273 × 3,5 = 0,956
  246 000/1 062 000 × 2,8 = 0,232 × 2,8 = 0,649
  384 000/1 062 000 × 0,6 = 0,362 × 0,6 = 0,217
  142 000/1 062 000 × 3,9 = 0,134 × 3,9 = 0,521
  D_pasivo = 2,343
```

**Paso 5 — calcula la brecha de duración y el efecto en el valor económico.**

```text
apalancamiento = 1 062 000 / 1 200 000 = 0,885
brecha de duración = 3,426 − 2,343 × 0,885 = 3,426 − 2,074 = 1,352

alza de 200 pb:
  Δ VEP ≈ −1,352 × 0,02 × 1 200 000 = −32 448

sobre capital de 138 000: −23,5 %
supera el umbral de atención del 15 %
```

**Paso 6 — reconcilia las dos señales.**

```text
MARGEN a 12 meses:  +526      señal favorable
VALOR ECONÓMICO:    −32 448   señal desfavorable

no se contradicen: miden cosas distintas
  el margen mejora porque el tramo corto está calzado a favor
  el valor cae porque los hipotecarios a 6,4 años de duración
  se financian con pasivos de 2,3 años de duración

el descalce está en el TRAMO LARGO, que el margen a 12 meses no ve
```

**Paso 7 — somete el supuesto más frágil a prueba.**

```text
¿qué pasa si la vida media conductual de la cuenta corriente
no es 3,5 años sino 1,5?

D_pasivo recalculada:
  0,273 × 1,5 = 0,410  (en vez de 0,956)
  D_pasivo = 0,410 + 0,649 + 0,217 + 0,521 = 1,797

brecha de duración = 3,426 − 1,797 × 0,885 = 3,426 − 1,590 = 1,836
Δ VEP ≈ −1,836 × 0,02 × 1 200 000 = −44 064
sobre capital: −31,9 %

UN SOLO SUPUESTO explica 11 616 de diferencia:
el 36 % de la exposición medida
```

**Paso 8 — decisiones.**

```text
1. Reportar AMBAS métricas al comité, siempre juntas
   el margen por sí solo daba una señal tranquilizadora falsa

2. Documentar y validar la vida media de los depósitos a la vista
   con datos propios y bajo escenario de estrés
   (en estrés, la vida media se acorta justo cuando las tasas suben)

3. Reducir la brecha de duración:
   · swaps receptores de tasa fija por 180 000 nocionales
     efecto estimado: brecha 1,352 → 0,88
   · originar hipotecario a tasa variable o con repactación
   · alargar el plazo de las emisiones

4. Aplicar los seis escenarios estandarizados, no solo el paralelo:
   el aplanamiento suele ser el peor caso para este perfil

5. Fijar límite de apetito: caída del valor económico ≤ 15 % del capital
   en el peor de los seis escenarios
```

**Interpreta:** el banco tenía **la señal correcta en la métrica equivocada**. Con un margen que mejoraba
y un valor económico que caía 23,5 % del capital, gestionar solo el margen habría llevado a mantener —o
incluso ampliar— exactamente la posición que lo estaba dañando. Y un solo supuesto conductual explicaba
un tercio de la exposición: **la parte más importante del modelo no es la fórmula, es el supuesto**.

## 🏦 Del cliente al banco

El cliente ve su tasa y el banco ve la diferencia entre la velocidad de repreciación de sus activos y la de sus pasivos. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Prepagué mi hipotecario cuando bajaron las tasas» | Riesgo de opcionalidad | 11, clase 5 |
| «El banco no me sube la tasa del ahorro» | Coeficiente de traspaso bajo | 10, clase 2 |
| «Me ofrecen tasa fija a 20 años» | El banco asume el riesgo de tasa | 3, clase 9 |
| «El banco reportaba utilidades y quebró» | Valor económico erosionado, no visible | 11, clase 5 |
| «Me cobran comisión por prepago» | Compensación de la opcionalidad | 4, clase 7 |

## 🧪 Práctica

El laboratorio pide calcular ambas sensibilidades y proponer una cobertura. La cobertura que protege una medida empeora la otra, y justificar la elección es el ejercicio.

En `labs/lab-03.md`:

1. Construye la brecha de repreciación por tramos y calcula la sensibilidad del margen.
2. Calcula las duraciones de activo y pasivo y la brecha de duración.
3. Aplica los seis escenarios estandarizados y determina el peor caso.
4. Somete el supuesto de vida media de los depósitos a un análisis de sensibilidad.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen bancos que se protegieron de un riesgo y quedaron expuestos al otro. La causa es haber medido solo una de las dos sensibilidades.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se gestiona solo el margen | Horizonte de 12 meses | Mide también el valor económico. |
| Solo se aplica el escenario paralelo | Riesgo de curva ignorado | Aplica los seis escenarios. |
| Vida media de depósitos muy larga | Supuesto no validado | Calibra con datos y limita el supuesto. |
| Prepagos modelados neutralmente | Opcionalidad asimétrica | Modela el ejercicio racional del cliente. |
| Activos «variables» que no se mueven juntos | Riesgo de base | Mide correlación entre índices. |
| Se reportan utilidades con valor en caída | Medición a costo amortizado | Reporta ambas visiones al comité. |

## ❓ Preguntas de comprobación

1. ¿Por qué el margen y el valor económico pueden dar señales opuestas?
2. ¿Qué hace asimétrico al riesgo de opcionalidad?
3. ¿Por qué el supervisor limita la vida media que puede suponerse para los depósitos a la vista?
4. ¿Qué es el riesgo de base y por qué no lo captura la brecha de repreciación?
5. ¿Cómo puede un banco reportar utilidades mientras destruye su patrimonio económico?

## 📥 Entregable

Guarda en `portfolio/parte-11/clase-05/`:

- la brecha de repreciación y la sensibilidad del margen calculadas;
- las duraciones y la brecha de duración con el efecto en el valor económico;
- los seis escenarios aplicados con la identificación del peor caso;
- el análisis de sensibilidad del supuesto de vida media de los depósitos.

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

- Basel Committee on Banking Supervision (2016). *Interest rate risk in the banking book*. BIS. <https://www.bis.org/bcbs/publ/d368.htm>
- Basel Committee on Banking Supervision (2024). *Standards: Interest rate risk in the banking book* (revisión). BIS.
- European Banking Authority (2022). *Guidelines on IRRBB and CSRBB*. EBA.
- Saunders, A. y Cornett, M. (2021). *Financial Institutions Management* (10.ª ed.). McGraw-Hill. Capítulos 8 y 9: modelos de repreciación y duración.
- Bank for International Settlements (2023). *Annual Economic Report*. Análisis de las pérdidas por riesgo de tasa en 2023.
- Verificación local: revisa los escenarios de tasa, los límites al supuesto de vida media y el umbral de atención supervisora aplicables en tu jurisdicción.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 04 · Riesgo de liquidez](04-riesgo-de-liquidez.md) | [Parte 11](../README.md) · [Programa](../../../SYLLABUS.md) | [06 · Riesgo de mercado y valor en riesgo →](06-riesgo-de-mercado-y-valor-en-riesgo.md) |
<!-- gen:footer:end -->
