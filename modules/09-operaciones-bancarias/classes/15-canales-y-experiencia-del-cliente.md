<!-- meta
part: 10
class: 15
title: "Canales y experiencia del cliente"
level: profesional
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 15 · Canales y experiencia del cliente

> [← 14 · Comercio exterior](14-comercio-exterior.md) · [Índice de la parte](../README.md) · [16 · Continuidad y eficiencia operativa →](16-continuidad-y-eficiencia-operativa.md)

**Parte 10 — Operaciones bancarias** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Diseñar y medir la relación operativa con el cliente a través de todos los canales: sucursal, cajero,
banca en línea, aplicación móvil, contacto telefónico y corresponsales. La calidad de esa relación no
es un tema de amabilidad: es una variable operativa que determina costo, riesgo, reclamos y permanencia.

Las clases anteriores describen operaciones. Esta las mira desde el canal por el que llegan, y añade la dimensión económica que decide la estrategia: la misma operación cuesta cien veces más en una sucursal que en una aplicación, y esa diferencia es lo que financia todo lo demás.

## 📚 Objetivos

Al finalizar podrás:

1. **Comparar** los canales por costo, alcance y riesgo.
2. **Segmentar** una base de clientes con criterios operativos y de valor.
3. **Medir** la experiencia con indicadores verificables, no con impresiones.
4. **Gestionar** el ciclo de un reclamo y extraer de él información de proceso.
5. **Evaluar** la inclusión financiera como decisión de diseño de canales.

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

Los cuatro primeros términos son la economía de los canales y su segmentación; los cuatro siguientes, la medición de la experiencia y su límite. La **accesibilidad** es la restricción que no se puede optimizar: migrar canales tiene un límite en las poblaciones que no pueden usar el canal barato.

| Concepto | Comprensión verificable |
|---|---|
| `costo por transacción` | Costo total del canal dividido por su volumen. Varía en órdenes de magnitud. |
| `canal de autoservicio` | Aquel donde el cliente ejecuta la operación sin intervención del banco. |
| `corresponsal no bancario` | Comercio que presta servicios financieros básicos por cuenta del banco. |
| `segmentación` | Agrupación de clientes por comportamiento y valor, no solo por ingreso. |
| `valor del cliente` | Contribución esperada del cliente durante su relación con el banco. |
| `tasa de resolución en primer contacto` | Reclamos resueltos sin escalar ni reabrir. |
| `causa raíz` | Falla de proceso que origina un reclamo recurrente. |
| `accesibilidad` | Capacidad del canal de ser usado por personas con distintas condiciones. |

## 🧠 Modelo mental

**Un reclamo no es una molestia: es un dato de proceso que llegó por el canal equivocado.**

```text
UN RECLAMO AISLADO       error puntual → se corrige el caso
UN PATRÓN DE RECLAMOS    falla de proceso → se corrige el proceso

el banco que solo resuelve casos paga el mismo error muchas veces
el banco que busca la causa raíz lo paga una vez
```

Y su corolario económico: **cada reclamo evitado ahorra el costo de atenderlo más el costo del riesgo
operativo, reputacional y regulatorio que arrastra**.

## 📖 Desarrollo

### 1. Los canales y su economía

Cada canal tiene un costo por transacción muy distinto. La tabla los recoge con órdenes de magnitud.

| Canal | Costo relativo por transacción | Alcance | Riesgo dominante |
|---|---:|---|---|
| Sucursal con ejecutivo | 100 | Bajo | Operativo y de fraude interno |
| Contacto telefónico | 35 | Medio | Suplantación |
| Cajero automático | 12 | Alto | Físico y clonación |
| Corresponsal no bancario | 8 | Muy alto | Efectivo y agente |
| Banca en línea | 3 | Alto | Fraude digital |
| Aplicación móvil | 2 | Muy alto | Dispositivo comprometido |

*(Índice relativo; las proporciones entre canales son estables aunque los valores absolutos varíen por
mercado. Verifica los datos de tu institución.)*

```text
LA TENTACIÓN: migrar todo al canal más barato
EL LÍMITE:    hay operaciones que no deben ser autoservicio
              y hay personas que no pueden usarlo

migrar sin resolver ambos puntos convierte
un ahorro de costo en exclusión y en riesgo
```

### 2. Qué operación va en qué canal

No toda operación puede ir a cualquier canal, y forzarlo produce reclamos. La tabla las asigna.

```text
CRITERIOS DE ASIGNACIÓN
  frecuencia       alta frecuencia → autoservicio
  complejidad      alta complejidad → asesoría
  irreversibilidad alta irreversibilidad → verificación reforzada
  monto            alto monto → autenticación fuerte y confirmación
  vulnerabilidad   cliente vulnerable → canal asistido disponible
```

| Operación | Canal preferente | Por qué |
|---|---|---|
| Consulta de saldo | Móvil | Frecuencia altísima, riesgo bajo |
| Transferencia a tercero nuevo | Móvil con verificación reforzada | Irreversible (Parte 4, clase 5) |
| Contratación de crédito hipotecario | Asistido | Complejidad y deber de información |
| Reclamo por cargo no reconocido | Cualquiera, con registro formal | Derecho del consumidor |
| Depósito de efectivo | Corresponsal o cajero | Cobertura territorial |
| Cierre de producto | Debe existir en el mismo canal donde se contrató | Simetría de acceso |

**La regla de simetría** —si un producto se contrata en un canal, debe poder cancelarse en ese canal—
es una exigencia creciente en las normas de protección al consumidor financiero, precisamente porque
la asimetría se usó como fricción deliberada.

### 3. Segmentación operativa

La atención se segmenta por valor del cliente y por complejidad de la operación. La tabla recoge el criterio.

```text
SEGMENTACIÓN POR INGRESO SOLAMENTE → obsoleta
  ignora comportamiento, riesgo y potencial

SEGMENTACIÓN ÚTIL: tres ejes
  VALOR ACTUAL        contribución de los últimos 12 meses
  POTENCIAL           productos que podría usar y no usa
  COSTO DE SERVICIO   canales que utiliza y su intensidad
```

```text
                  alto valor
                       │
   servicio      ●─────┼─────●   relación
   eficiente           │         a preservar
   ──────────────── ───┼─── ────────────────
   bajo costo          │        alto costo
   de servicio         │        de servicio
   activación    ●─────┼─────●   revisar
                       │         precio o canal
                  bajo valor
```

**Advertencia ética y regulatoria.** La segmentación puede derivar en trato discriminatorio si se apoya
en variables prohibidas o en sus correlatos (código postal como sustituto de origen étnico, por
ejemplo). La Parte 14, clase 11 desarrolla el sesgo algorítmico; aquí basta la regla operativa:
**si no puedes explicar por qué un cliente recibe peor servicio, no lo apliques**.

### 4. Medir la experiencia

La experiencia se mide con indicadores concretos y no con encuestas de satisfacción. La tabla los recoge.

| Indicador | Qué mide | Trampa frecuente |
|---|---|---|
| Tiempo de espera | Eficiencia del canal | Se mide solo en horario valle |
| Resolución en primer contacto | Calidad del proceso | Se cierra el caso sin resolverlo |
| Reclamos por cada 1 000 clientes | Salud del proceso | Se dificulta reclamar y el número baja |
| Tiempo de respuesta a reclamos | Cumplimiento | Se responde sin resolver |
| Reapertura de reclamos | Efectividad real | No se mide |
| Recomendación del cliente | Percepción global | Se encuesta solo a quien tuvo éxito |
| Abandono en el proceso digital | Fricción | Se mide sin distinguir causa |

**El indicador más honesto es la tasa de reapertura**, porque no se puede mejorar con presentación:
o el problema quedó resuelto o volvió.

### 5. Ciclo del reclamo

Un reclamo tiene un ciclo y su análisis de causa raíz es lo que evita el siguiente. El esquema lo recorre.

```text
1. RECEPCIÓN      por cualquier canal, con constancia y número de caso
2. CLASIFICACIÓN  tipo, producto, canal, monto, criticidad
3. INVESTIGACIÓN  con plazo definido y evidencia
4. RESOLUCIÓN     con respuesta fundamentada, no genérica
5. COMUNICACIÓN   en lenguaje comprensible
6. ANÁLISIS       ¿es un caso o un patrón?
7. CORRECCIÓN     si es patrón, se corrige el proceso, no solo el caso
8. VERIFICACIÓN   ¿bajaron los reclamos de esa causa?
```

```text
ANÁLISIS DE CAUSA RAÍZ — ejemplo
  reclamo: "me cobraron mantención dos veces"
  caso:    se devuelve el cobro
  patrón:  400 reclamos iguales en un mes

  causa raíz: el proceso de cobro corre dos veces
              cuando el ciclo cierra en fin de semana

  corrección de caso:   400 devoluciones
  corrección de proceso: una regla de idempotencia en el cobro
```

## 🧮 Ejemplo guiado

El ejemplo calcula el ahorro de migrar un conjunto de operaciones y el efecto sobre los clientes que no pueden migrar. Las dos cifras juntas son la decisión.

**Situación.** El comité de operaciones evalúa cerrar sucursales y migrar clientes a canales digitales.

```text
SITUACIÓN ACTUAL
  sucursales                      120
  costo anual por sucursal        340  (millones de moneda local)
  transacciones en sucursal    18,4 M al año
  clientes que usan solo sucursal  184 000  (14 % de la base)

PROPUESTA: cerrar 30 sucursales de menor volumen
  ahorro anual bruto              10 200
  transacciones a migrar           2,9 M
  clientes afectados               41 000
```

**Paso 1 — calcula el ahorro operativo directo.**

```text
ahorro por cierre:            30 × 340 = 10 200
costo de atender 2,9 M transacciones en canales alternativos:
  60 % migra a móvil:      1,74 M × 2 (índice) → costo relativo bajo
  25 % migra a corresponsal: 0,73 M × 8
  15 % se pierde o migra a otra sucursal

estimación de costo incremental de canales: 1 180
AHORRO NETO OPERATIVO: 10 200 − 1 180 = 9 020
```

**Paso 2 — estima el efecto sobre los clientes afectados.**

```text
de los 41 000 clientes afectados:
  capacidad digital comprobada (usan la app)       23 600  (58 %)
  usan solo sucursal, con smartphone                9 800  (24 %)
  sin smartphone o sin conectividad estable         5 200  (13 %)
  personas mayores o con discapacidad declarada     2 400   (6 %)
```

**Paso 3 — estima el atrición y su costo.**

```text
tasa de fuga histórica tras un cierre de sucursal, por grupo:
  con capacidad digital      3 %  →   708 clientes
  con smartphone sin uso    11 %  → 1 078
  sin acceso digital        28 %  → 1 456
  mayores o con discapacidad 34 %  →   816
  TOTAL FUGA ESTIMADA               4 058 clientes

margen anual medio por cliente: 96 000 moneda local
PÉRDIDA DE MARGEN ANUAL: 4 058 × 96 000 = 389,6 millones
```

**Paso 4 — el resultado se invierte con el horizonte.**

```text
año 1:  ahorro 9 020 − pérdida de margen 390 = +8 630
pero la pérdida de margen es RECURRENTE y creciente:
  esos clientes tenían productos que vencen y no se renuevan
  valor presente de la pérdida a 8 años, al 9 %:
  390 × 5,535 = 2 159
AHORRO NETO EN VALOR PRESENTE (8 años, ahorro 9 020 anual):
  9 020 × 5,535 = 49 926
  − 2 159
  = 47 767  → sigue siendo positivo
```

**Paso 5 — el análisis que falta: los clientes sin alternativa.**

```text
5 200 sin acceso digital + 2 400 con barreras
= 7 600 clientes para los que el cierre NO tiene sustituto

de esos, en cuántas localidades la sucursal cerrada
era la ÚNICA presencia bancaria del territorio?
  → 11 de las 30 sucursales
  → 3 100 clientes quedan sin ninguna alternativa presencial
```

**Paso 6 — rediseña la propuesta.**

```text
DECISIÓN REVISADA
  cerrar 19 sucursales donde existe alternativa a menos de 8 km
  mantener 11 en modalidad reducida (2 días por semana + corresponsal)
  costo de la modalidad reducida: 11 × 140 = 1 540

  ahorro revisado: 19 × 340 − costo canales (750) = 5 710
  fuga estimada revisada: 1 980 clientes → pérdida 190 anual

  ahorro neto anual: 5 520  (vs. 8 630 del plan original)
  clientes sin alternativa: 0
```

**Paso 7 — mide el resultado con indicadores comprometidos de antemano.**

```text
a 12 meses del cierre, medir:
  · fuga real por segmento vs. estimada
  · reclamos por acceso, por localidad
  · adopción digital efectiva de los clientes migrados
  · uso del corresponsal en las localidades sin sucursal
  · tiempo de espera en las sucursales que absorbieron volumen
```

**Interpreta:** el plan original era rentable y aun así estaba mal diseñado. **La diferencia de 3 110
millones anuales entre ambos planes es el precio de no dejar a 3 100 personas sin acceso.** Ese precio
puede pagarse o no, pero la decisión debe tomarse sabiéndolo. Un análisis que solo muestra el ahorro
no permite decidir: permite justificar.

## 🏦 Del cliente al banco

El cliente elige un canal y el banco paga un costo por transacción muy distinto según cuál. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Cerraron mi sucursal» | Optimización de red con costo de atrición | 10, clase 15 |
| «No puedo cancelar por la app lo que contraté por la app» | Regla de simetría de canal | 4, clase 12 |
| «Nadie resuelve mi reclamo» | Resolución en primer contacto y reapertura | 12, clase 9 |
| «Me atienden distinto que a otros» | Segmentación y su límite ético | 14, clase 11 |
| «La app no la puedo usar» | Accesibilidad como requisito, no como extra | 14, clase 6 |

## 🧪 Práctica

El laboratorio pide diseñar una estrategia de canales con su ahorro y su efecto sobre la accesibilidad. Declarar el segundo es parte del ejercicio.

En `labs/lab-06.md`, sección de canales:

1. Construye la matriz de costo por transacción y por canal de un banco sintético.
2. Segmenta una base de clientes por valor, potencial y costo de servicio.
3. Analiza 50 reclamos sintéticos y determina cuáles responden a una misma causa raíz.
4. Evalúa un plan de cierre de sucursales incorporando el costo de atrición y de exclusión.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen migraciones de canal que produjeron reclamos o exclusión. Las causas son operaciones asignadas al canal equivocado y accesibilidad no considerada.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Los reclamos bajan sin mejorar nada | Se dificultó reclamar | Mide reapertura y accesibilidad del canal. |
| Se migra todo al canal más barato | Costo de atrición ignorado | Incorpora fuga y exclusión al cálculo. |
| Se resuelven casos, no causas | Sin análisis de patrón | Clasifica y agrupa por causa raíz. |
| La segmentación reproduce sesgos | Variables sustitutas prohibidas | Exige explicabilidad de todo trato diferenciado. |
| Se contrata por app y se cancela en sucursal | Fricción deliberada | Aplica simetría de canal. |
| Se mide satisfacción solo a quien tuvo éxito | Sesgo de selección | Encuesta también a quien abandonó. |

## ❓ Preguntas de comprobación

1. ¿Por qué la tasa de reapertura de reclamos es más honesta que el total de reclamos?
2. ¿Qué criterios determinan en qué canal debe ofrecerse una operación?
3. ¿Por qué la segmentación puede convertirse en discriminación y cómo se evita?
4. ¿Qué costos omite un plan de cierre de sucursales que solo mira el ahorro operativo?
5. ¿Qué es la regla de simetría de canal y por qué la exigen los reguladores?

## 📥 Entregable

Guarda en `portfolio/parte-10/clase-15/`:

- la matriz de costo por canal con su interpretación;
- la segmentación construida y las decisiones de servicio que se derivan;
- el análisis de causa raíz de los reclamos con la corrección de proceso propuesta;
- la evaluación del plan de cierre con ahorro, atrición y clientes sin alternativa.

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

- OECD (2022). *Recommendation on Financial Literacy* y *G20/OECD High-Level Principles on Financial Consumer Protection*. OECD. <https://www.oecd.org/finance/financial-education/>
- World Bank (2021). *Good Practices for Financial Consumer Protection*. World Bank Group.
- Consumer Financial Protection Bureau. *Consumer Complaint Database* y su metodología de análisis. CFPB. <https://www.consumerfinance.gov/data-research/consumer-complaints/>
- Rose, P. y Hudgins, S. (2013). *Bank Management and Financial Services* (9.ª ed.). McGraw-Hill. Capítulos 4 y 15: red de distribución y servicio.
- Reichheld, F. (2011). *The Ultimate Question 2.0*. Harvard Business Review Press. Uso y límites de los indicadores de recomendación.
- Verificación local: revisa las obligaciones de atención, plazos de respuesta a reclamos y requisitos de accesibilidad de la normativa de protección al consumidor financiero de tu país.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 14 · Comercio exterior](14-comercio-exterior.md) | [Parte 10](../README.md) · [Programa](../../../SYLLABUS.md) | [16 · Continuidad y eficiencia operativa →](16-continuidad-y-eficiencia-operativa.md) |
<!-- gen:footer:end -->
