<!-- meta
part: 16
class: 9
title: "Operaciones y pagos"
level: profesional
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 09 · Operaciones y pagos

> [← 08 · Modelos de riesgo](08-modelos-de-riesgo.md) · [Índice de la parte](../README.md) · [10 · Contabilidad y estados financieros →](10-contabilidad-y-estados-financieros.md)

**Parte 16 — Proyecto Banco Virtual** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Construir la operación diaria del Banco Austral: pagos, conciliación, cobranza y atención. Es donde se
gana o se pierde el compromiso de eficiencia del 48 %, y donde el diseño de los procesos determina si el
banco puede crecer sin que su costo crezca en la misma proporción.

El banco de las clases anteriores ya coloca crédito. Esta construye la operación diaria que lo sostiene, aplicando la Parte 10. Y añade la dimensión que un proyecto obliga a dimensionar: cuántas personas y cuánta capacidad hacen falta para el volumen proyectado.

## 📚 Objetivos

Al finalizar podrás:

1. **Diseñar** los procesos operativos críticos y sus controles.
2. **Dimensionar** la capacidad operativa por volumen.
3. **Construir** el proceso de conciliación diaria.
4. **Diseñar** la cobranza por etapas y su economía.
5. **Verificar** que la operación produce el índice de eficiencia comprometido.

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

Los cuatro primeros términos son los procesos y su control; los cuatro siguientes, su economía y su escalabilidad. La **tasa de automatización** es la variable que decide el costo por operación y la que más se puede mover con diseño.

| Concepto | Comprensión verificable |
|---|---|
| `proceso crítico` | Aquel cuya interrupción impide operar. |
| `conciliación` | Verificación de que dos registros de lo mismo coinciden. |
| `partida pendiente` | Diferencia no explicada entre dos registros. |
| `tasa de automatización` | Operaciones sin intervención manual. |
| `cobranza temprana` | Gestión en los primeros días de atraso. |
| `costo por operación` | Costo total de un proceso dividido por su volumen. |
| `capacidad instalada` | Volumen máximo que la operación puede atender. |
| `escalabilidad` | Que el costo crezca menos que el volumen. |

## 🧠 Modelo mental

El modelo mental es una capacidad que se dimensiona por el pico y no por la media: los procesos operativos se saturan en los días de mayor volumen, y dimensionar por el promedio produce colas exactamente cuando más importa.

```text
EL COMPROMISO DE EFICIENCIA DEL 48 % EXIGE
QUE EL COSTO CREZCA MENOS QUE EL NEGOCIO

  costo fijo:    no crece con el volumen
  costo variable: crece proporcionalmente
  costo escalonado: crece a saltos

  UN BANCO DIGITAL BIEN DISEÑADO
    · costo variable por transacción cercano a cero
    · costo escalonado en la capacidad de atención
    · costo fijo en tecnología y control

  UN BANCO DIGITAL MAL DISEÑADO
    tiene una trastienda manual que convierte
    cada operación digital en una tarea de una persona
    (Parte 14, clase 13)
    → su costo crece igual que su volumen
```

## 📖 Desarrollo

### 1. Procesos críticos

Los procesos críticos se identifican por su efecto sobre el cliente. La tabla los recoge.

| Proceso | Volumen anual proyectado | Automatización objetivo |
|---|---:|---:|
| Apertura de cuenta | 42 000 | 96 % |
| Originación de crédito P2 | 84 000 solicitudes | 38 % automático, 62 % asistido |
| Originación E2 | 3 400 solicitudes | 22 % automático |
| Procesamiento de pagos | 8,4 M | 99,8 % |
| Recaudación de empresas | 12,6 M | 99,9 % |
| Conciliación | Diaria | 97 % |
| Cobranza temprana | 118 000 casos | 84 % |
| Atención de consultas | 340 000 | 73 % en canal digital |
| Reclamos | 2 800 | 42 % resolución automática |

La cifra de automatización del proceso más voluminoso parece exigente hasta
que se traduce a personas.

```text
LA TASA DE AUTOMATIZACIÓN DEL 99,8 % EN PAGOS
NO ES UN OBJETIVO AMBICIOSO: ES EL MÍNIMO

  con 8,4 M de pagos, un 1 % de tareas manuales
  son 84 000 tareas al año
  a 0,00021 por tarea: 17,6 anuales
  y a 5 minutos cada una: 7 000 horas = 4 personas
```

### 2. Dimensionamiento

La capacidad se dimensiona por volumen pico y por tiempo de proceso. El procedimiento lo hace.

```text
MÉTODO
  para cada proceso:
    volumen anual × proporción que requiere intervención
    × tiempo por intervención
    ÷ horas productivas anuales por persona (1 560)
    = personas necesarias
```

| Proceso | Volumen | % manual | Minutos | Personas |
|---|---:|---:|---:|---:|
| Originación P2 (asistida) | 84 000 | 62 % | 14 | 7,8 |
| Originación E2 | 3 400 | 78 % | 95 | 2,7 |
| Excepciones de pagos | 8,4 M | 0,2 % | 6 | 10,8 |
| Conciliación | 260 días | — | 210 | 0,6 |
| Cobranza temprana | 118 000 | 16 % | 9 | 1,8 |
| Atención asistida | 340 000 | 27 % | 7 | 6,9 |
| Reclamos | 2 800 | 58 % | 42 | 0,7 |
| **Total operativo** | | | | **31,3** |

El dimensionamiento revela que el proceso más costoso no es el de mayor
volumen, sino el de mayor porcentaje manual.

```text
EL PROCESO MÁS COSTOSO ES EL MENOS EVIDENTE
  excepciones de pagos: 10,8 personas
  con solo el 0,2 % de intervención manual

  reducir ese 0,2 % a 0,08 % libera 6,5 personas
  → 156 anuales
  → y exige invertir en el manejo automático
    de los casos de excepción más frecuentes
```

### 3. Conciliación

La conciliación diaria es el control que detecta lo que los demás dejaron pasar. La tabla recoge su diseño.

```text
QUÉ SE CONCILIA CADA DÍA
  · saldos del núcleo contra la contabilidad
  · movimientos del esquema de pagos contra los propios
  · recaudación de empresas contra lo abonado
  · saldos en cuentas de corresponsales
  · cartera contra el sistema de créditos
  · provisiones contra el modelo

PROCESO
  1. extracción automática de ambos registros
  2. cruce automático por identificador y monto
  3. las partidas que cruzan se cierran
  4. las que no, se convierten en PARTIDAS PENDIENTES
  5. cada pendiente se investiga con plazo
  6. se registra su causa y su corrección
```

| Indicador de conciliación | Objetivo |
|---|---|
| Cruce automático | ≥ 97 % |
| Pendientes > 3 días | 0 |
| Pendientes > 30 días | 0 |
| Monto de pendientes / volumen | ≤ 0,002 % |
| Pendientes con causa identificada | 100 % |

De esos indicadores, el de partidas pendientes es el que se mueve primero
cuando algo va mal.

```text
LAS PARTIDAS PENDIENTES SON EL SÍNTOMA
MÁS TEMPRANO DE UN PROBLEMA OPERATIVO

  su crecimiento sostenido anticipa
  errores de proceso, fallas de integración
  o fraude, semanas antes de que se manifiesten
```

### 4. Cobranza por etapas

La cobranza se organiza por etapas con estrategias distintas. La tabla las recoge.

```text
ETAPAS Y SU ECONOMÍA

  DÍA 1-3 — RECORDATORIO AUTOMÁTICO
    canal: mensaje y notificación en la aplicación
    costo por caso: 0,00008
    recuperación: 62 % de los casos
    → es el 84 % de la automatización del proceso

  DÍA 4-15 — CONTACTO ASISTIDO
    canal: llamada
    costo por caso: 0,0021
    recuperación: 54 % de los que quedan
    OBJETIVO: entender la causa, no solo cobrar
      si es transitoria → reprogramación (clase 5)
      si es estructural → renegociación

  DÍA 16-60 — GESTIÓN INTENSIVA
    costo por caso: 0,0084
    recuperación: 38 %

  DÍA 61-90 — PREJUDICIAL
    costo por caso: 0,018
    recuperación: 22 %

  DÍA 90+ — RECUPERACIÓN
    externalizada o judicial según monto
    recuperación: 24 % del saldo, en 14 meses
```

```text
LA ECONOMÍA DE LA COBRANZA TEMPRANA

  118 000 casos entran en atraso al año
  con el recordatorio automático se resuelven 73 160
  costo: 118 000 × 0,00008 = 9,4

  si esos 73 160 llegaran a gestión intensiva:
  costo: 73 160 × 0,0084 = 614

  AHORRO DE LA COBRANZA TEMPRANA: 605 anuales
  Y ADEMÁS
    la recuperación temprana no daña la relación
    con un cliente que solo se atrasó unos días
```

### 5. Escalabilidad

El modelo operativo tiene que escalar con el negocio sin escalar el costo en la misma proporción. La tabla recoge los criterios.

```text
LA PRUEBA DE ESCALABILIDAD
  si el volumen se duplica, ¿cuánto crece el costo?

  costo fijo (tecnología, control, dirección):     0 %
  costo variable (transacciones):                +100 %
  costo escalonado (personas de atención):        +85 %
    (por la curva de aprendizaje y la automatización
     de los casos más frecuentes)

  COSTO TOTAL: crece 62 % cuando el volumen crece 100 %
  → el índice de eficiencia MEJORA con la escala
```

## 🧮 Ejemplo guiado

El ejemplo dimensiona la capacidad operativa del Banco Austral. Conviene dimensionar por pico: la diferencia con la media es grande.

**Situación.** Verificar que la operación diseñada produce el índice de eficiencia del 48 %.

```text
COMPROMISO: índice de eficiencia 48 %
margen bruto proyectado: 55 942
gastos máximos: 26 852
```

**Paso 1 — dimensiona la plantilla completa.**

```text
OPERATIVOS (del cálculo anterior)              31,3
COMERCIAL Y ATENCIÓN
  ejecutivos de empresa (9 200 clientes,
    cartera de 180 por ejecutivo)              51,1
  atención digital y corresponsales             18,0
  marketing y captación                          8,0
TECNOLOGÍA
  desarrollo y mantenimiento                    22,0
  infraestructura y seguridad                    9,0
RIESGOS                                         14,0
CUMPLIMIENTO                                     9,0
AUDITORÍA INTERNA                                5,0
FINANZAS Y CONTABILIDAD                         12,0
ADMINISTRACIÓN Y DIRECCIÓN                      10,0
TOTAL                                          189,4  → 190 personas
```

**Paso 2 — calcula el costo de personal.**

```text
costo medio por persona: 24,0
  (incluye remuneración, cargas y beneficios)

190 × 24,0 = 4 560
```

**Paso 3 — calcula los demás gastos.**

```text
TECNOLOGÍA
  licencias y servicios en la nube             1 840
  amortización de la inversión inicial
    (6 940 en 5 años)                          1 388
INMUEBLES Y SERVICIOS
  oficinas (sin red de sucursales)               680
CORRESPONSALES
  comisiones a la red (12 000 puntos)          2 460
PROVEEDORES
  verificación de identidad (42 000 × 0,0018)     76
  antifraude y prevención de lavado              640
  procesamiento de medios de pago              3 180
  buró de crédito (87 400 consultas × 0,0009)     79
MARKETING Y CAPTACIÓN                          2 840
AUDITORÍA EXTERNA Y ASESORÍAS                    420
OTROS                                            890
TOTAL OTROS GASTOS                            14 493
```

**Paso 4 — consolida.**

```text
personal:      4 560
otros gastos: 14 493
GASTOS TOTALES: 19 053

  margen bruto: 55 942
  ÍNDICE DE EFICIENCIA: 19 053 / 55 942 = 34,1 %

  COMPROMISO: 48,0 %
  PROYECTADO: 34,1 %
```

**Paso 5 — cuestiona el resultado favorable.**

```text
UN 34,1 % SERÍA EXCEPCIONAL INCLUSO
PARA UN BANCO DIGITAL MADURO

  LAS REFERENCIAS
    bancos digitales establecidos: 42 % a 58 %
    mejores del sector: 38 %

  → 34,1 % es implausible
  → hay costos omitidos
```

**Paso 6 — busca los costos omitidos.**

```text
REVISIÓN SISTEMÁTICA

  ¿ESTÁ EL COSTO DE LA CAPACIDAD OCIOSA?
    la plantilla se dimensionó para el volumen del año 3
    en los años 1 y 2 el volumen es menor
    y la plantilla no puede ser proporcional
    → el año 3 sí es representativo  ✓

  ¿ESTÁ EL COSTO DE LA MALA CALIDAD?
    el dimensionamiento supone que todo funciona
    a la primera
    con una tasa de reproceso del 8 % (realista en el año 3):
    31,3 personas operativas × 8 % = 2,5 personas
    + gestión de las partidas pendientes: 1,2
    + corrección de datos: 1,8
    TOTAL: 5,5 personas = 132
    → OMITIDO

  ¿ESTÁ EL COSTO DE LOS CORRESPONSALES POR OPERACIÓN?
    2 460 son las comisiones de la red
    ¿incluye las operaciones de depósito y retiro?
    volumen: 2,8 M de operaciones × 0,0011 = 3 080
    → los 2 460 subestiman en 620

  ¿ESTÁ LA ROTACIÓN Y LA FORMACIÓN?
    rotación del 22 % en un banco nuevo
    42 personas al año × costo de reemplazo 3,2 = 134
    → OMITIDO

  ¿ESTÁ EL COSTO DEL FRAUDE?
    (Parte 14, clase 8): pérdida + falsos positivos
    estimado para este volumen: 480
    → OMITIDO

  ¿ESTÁ EL SEGURO Y LA CONTINGENCIA?
    seguros de la institución, contingencias legales
    provisión: 340
    → OMITIDO
```

**Paso 7 — recalcula.**

```text
gastos originales:                19 053
+ costo de la mala calidad:          132
+ corresponsales subestimados:       620
+ rotación y formación:              134
+ fraude:                            480
+ seguros y contingencias:           340
GASTOS CORREGIDOS:                20 759

ÍNDICE DE EFICIENCIA: 20 759 / 55 942 = 37,1 %

  sigue siendo muy favorable
  → ¿qué más falta?
```

**Paso 8 — encuentra la omisión principal.**

```text
LA PLANTILLA DE 190 PERSONAS PARA 77 200 CLIENTES
  ratio: 406 clientes por persona

  REFERENCIAS
    banco digital maduro: 280 a 420 clientes por persona
    banco tradicional: 90 a 160

  → el ratio es alcanzable en régimen

PERO EL DIMENSIONAMIENTO COMERCIAL
  51,1 ejecutivos para 9 200 empresas
  = 180 empresas por ejecutivo

  ¿ES REALISTA?
    una empresa pequeña con línea de crédito
    exige: evaluación anual, seguimiento trimestral,
    atención de consultas, gestión de renovación
    tiempo anual por empresa: 6,4 horas
    9 200 × 6,4 = 58 880 horas / 1 560 = 37,7 personas

    para 180 empresas por ejecutivo: 6,4 h × 180 = 1 152 h
    sobre 1 560 disponibles: 74 % de ocupación
    → deja 26 % para captación de nuevos clientes
    → AJUSTADO PERO VIABLE

  Y EL CRECIMIENTO
    captar 3 000 empresas nuevas al año
    exige 12 personas dedicadas a captación
    → NO ESTÁN EN LA PLANTILLA

  AJUSTE: +12 personas = 288
```

```text
GASTOS FINALES: 20 759 + 288 = 21 047
ÍNDICE DE EFICIENCIA: 21 047 / 55 942 = 37,6 %

  COMPROMISO: 48,0 %
  PROYECTADO: 37,6 %

  LA DIFERENCIA DE 10,4 PUNTOS
  EQUIVALE A 5 818 DE GASTOS ADICIONALES

  ¿SE LOS ASIGNAMOS A ALGO?
    NO. el compromiso del 48 % se estableció
    en la clase 5 como una estimación
    el diseño detallado produce 37,6 %

  DECISIÓN
    revisar el compromiso a 42,0 %
    (entre el 37,6 % calculado y el 48 % estimado)
    y usar los 3 552 de diferencia como RESERVA
    para lo que el diseño detallado no anticipó

  Y DECLARARLO
    "el índice de eficiencia proyectado es 37,6 %;
     el compromiso de gestión es 42,0 %;
     la diferencia es reserva para costos no anticipados
     de un banco en su tercer año"
```

**Interpreta:** el cálculo inicial dio 34,1 % y la revisión sistemática encontró **1 994 de costos
omitidos**, todos reales y todos fáciles de olvidar porque ninguno corresponde a un proceso del negocio:
mala calidad, rotación, fraude, seguros y captación. El compromiso final del 42 % incorpora una reserva
explícita, que es la forma honesta de reconocer que un diseño en papel siempre omite algo.

## 🏦 Del cliente al banco

El cliente espera que su operación se ejecute y el banco dimensiona capacidad para el peor día. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Me avisaron el mismo día del atraso» | Cobranza temprana automatizada | 16, clase 9 |
| «Me llamaron para entender mi situación» | Cobranza que busca la causa | 12, clase 8 |
| «Todo funciona sin errores» | Conciliación diaria y partidas cero | 10, clase 8 |
| «Deposito en el almacén del barrio» | Red de corresponsales | 10, clase 15 |
| «El banco no me cobra comisiones» | Costo por operación muy bajo | 16, clase 6 |

## 🧪 Práctica

El laboratorio pide dimensionar la operación y diseñar la conciliación. El dimensionamiento por pico es lo que se evalúa.

En `labs/lab-05.md`:

1. Dimensiona la plantilla por proceso con volumen, porcentaje manual y tiempo.
2. Diseña el proceso de conciliación con sus indicadores.
3. Calcula la economía de la cobranza por etapas.
4. Verifica el índice de eficiencia y busca sistemáticamente los costos omitidos.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen operaciones saturadas. La causa es dimensionar por volumen medio.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Índice de eficiencia implausible | Costos omitidos | Revisión sistemática. |
| Se olvida el costo de la mala calidad | Se supone que todo funciona | Añade la tasa de reproceso. |
| Trastienda manual sobre canal digital | El costo crece con el volumen | Automatiza la trastienda. |
| Sin capacidad de captación | Solo se dimensiona la atención | Añádela. |
| Partidas pendientes sin plazo | Síntoma temprano ignorado | Plazo y causa obligatorios. |
| Cobranza que empieza tarde | Costo por caso multiplicado | Recordatorio automático desde el día 1. |

## ❓ Preguntas de comprobación

1. ¿Por qué el 0,2 % de intervención manual en pagos cuesta 10,8 personas?
2. ¿Qué anticipa el crecimiento de las partidas pendientes?
3. ¿Cuál es la economía de la cobranza temprana?
4. ¿Qué cinco costos suelen omitirse al dimensionar una operación?
5. ¿Por qué el compromiso final incorpora una reserva explícita?

## 📥 Entregable

Guarda en `portfolio/parte-16/clase-09/`:

- el dimensionamiento por proceso con su método;
- el proceso de conciliación con sus indicadores y plazos;
- la economía de la cobranza por etapas;
- el índice de eficiencia con la revisión de costos omitidos y el compromiso revisado.

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

- Rose, P. y Hudgins, S. (2013). *Bank Management and Financial Services* (9.ª ed.). McGraw-Hill. Diseño de los procesos operativos y de cobranza.
- Basel Committee on Banking Supervision (2021). *Principles for Operational Resilience*. BIS. Tolerancia a la interrupción de los procesos críticos.
- Committee on Payments and Market Infrastructures (2016). *Fast payments — Enhancing the speed and availability of retail payments*. BIS. Requisitos del esquema de pagos inmediatos al que se conecta.
- Kaplan, R. y Anderson, S. (2007). *Time-Driven Activity-Based Costing*. Harvard Business School Press. Costeo de los procesos que sostiene el compromiso de eficiencia.
- European Banking Authority (2018). *Guidelines on management of non-performing and forborne exposures*. EBA. Cobranza y reestructuración.
- Verificación local: revisa las obligaciones sobre prácticas de cobranza, horarios de contacto y conservación de registros de tu país.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 08 · Modelos de riesgo](08-modelos-de-riesgo.md) | [Parte 16](../README.md) · [Programa](../../../SYLLABUS.md) | [10 · Contabilidad y estados financieros →](10-contabilidad-y-estados-financieros.md) |
<!-- gen:footer:end -->
