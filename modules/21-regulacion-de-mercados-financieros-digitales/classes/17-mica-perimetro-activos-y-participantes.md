<!-- meta
part: 22
class: 17
title: "MiCA I: perímetro, activos y participantes"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [union-europea]
regulatory_topics: [mica, perimetro, calificacion, criptoactivos]
regulation_last_verified: 2026-08-20
regulatory_status: vigente
primary_authorities: [EBA, ESMA, Comision Europea]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 17 · MiCA I: perímetro, activos y participantes

> [← 16 · Regulación comparada: Chile y el mundo](16-regulacion-comparada-chile-y-el-mundo.md) · [Índice de la parte](../README.md) · [18 · MiCA II: obligaciones, reservas y supervisión →](18-mica-obligaciones-reservas-y-supervision.md)

**Parte 22 — Regulación de mercados financieros digitales** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Estudiar el primer régimen del mundo que reguló los criptoactivos de forma
completa y con una sola norma, y usarlo para lo que sirve en este programa: **ver
cómo un legislador dibuja el perímetro cuando tiene que dibujarlo entero de una
vez.**

La clase 16 comparó regímenes en abstracto y demostró que una tabla comparada sin
referencia ni fecha no sirve para decidir. Esta clase hace lo contrario: toma un
régimen concreto —el Reglamento (UE) 2023/1114, MiCA— y lo lee por dentro, con su
número, su fecha y sus exclusiones.

Hay una razón para elegir MiCA y no otro. Casi todas las jurisdicciones
regularon por parches: una norma para los proveedores, otra para el lavado, una
tercera para las stablecoins cuando una perdió la paridad. MiCA intentó lo otro
—definir las categorías, los sujetos y las obligaciones de una sola vez— y por eso
sus costuras son visibles. Donde el reglamento tuvo que excluir algo se ve el
límite del método, y esos límites son la parte más instructiva.

## 📚 Objetivos

Al finalizar podrás:

1. **Delimitar** qué entra y qué queda fuera del ámbito de MiCA, con el criterio
   que usa el propio reglamento y no con la etiqueta comercial del producto.
2. **Clasificar** un criptoactivo en las tres categorías del régimen y justificar
   la elección con la promesa que incorpora.
3. **Identificar** qué servicios convierten a una entidad en proveedor sujeto a
   autorización y cuáles no.
4. **Explicar** qué es el libro blanco, qué efecto tiene y por qué no equivale a
   una aprobación del producto.
5. **Determinar** cuándo un instrumento significativo cambia de supervisor y qué
   consecuencia práctica tiene ese cambio.

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

Los tres primeros términos son las categorías del reglamento y ordenan todo lo
demás: la obligación aplicable se deduce de la categoría, no del nombre del
producto. Los cinco siguientes describen a los sujetos y los actos. La distinción
que más se confunde es la última: **notificar un libro blanco no es obtener una
autorización**, y hay proyectos que anuncian lo primero como si fuera lo segundo.

| Concepto | Comprensión verificable |
|---|---|
| `ficha referenciada a activos` | Criptoactivo que estabiliza su valor contra una cesta |
| `ficha de dinero electrónico` | Criptoactivo que estabiliza su valor contra una moneda oficial |
| `otros criptoactivos` | Los que no prometen estabilidad frente a una referencia |
| `proveedor de servicios` | Persona jurídica autorizada para prestar servicios listados |
| `libro blanco` | Documento de información con responsabilidad del emisor |
| `oferta pública` | Comunicación dirigida al público para adquirir el activo |
| `admisión a negociación` | Incorporación del activo a una plataforma |
| `instrumento significativo` | El que supera umbrales y cambia de supervisor |

## 🧠 Modelo mental

El modelo mental de MiCA es un embudo de tres filtros que se aplican en orden, y
el orden importa porque el primero descarta la mayor parte de los casos difíciles.

El primer filtro pregunta si el activo ya es otra cosa. Si un token es un
instrumento financiero conforme a la directiva de mercados de instrumentos
financieros, MiCA no se le aplica: se le aplica el régimen de valores, con su
folleto, su intermediación y su depositario. Ese filtro es el que resuelve el
noventa por ciento de las discusiones, y es el mismo que la clase 3 de esta parte
enseñó a aplicar sin jurisdicción. El segundo filtro clasifica lo que queda según
la promesa de estabilidad. El tercero mira quién lo hace y con qué servicio.

```text
EL EMBUDO DE MICA

  FILTRO 1 · ¿YA ES OTRA COSA?
    instrumento financiero → régimen de valores
    depósito               → régimen bancario
    fondo                  → régimen de fondos
    seguro o pensión       → su propio régimen
    moneda de banco central→ fuera del reglamento
    → SI SALE AQUÍ, MICA NO APLICA

  FILTRO 2 · ¿QUÉ PROMETE?
    estabilidad contra una moneda oficial
      → ficha de dinero electrónico
    estabilidad contra una cesta
      → ficha referenciada a activos
    no promete estabilidad
      → otros criptoactivos

  FILTRO 3 · ¿QUIÉN Y CON QUÉ SERVICIO?
    emitir, ofrecer, admitir a negociación
      → obligaciones de emisor u oferente
    custodiar, cambiar, ejecutar, asesorar…
      → autorización de proveedor

LA PREGUNTA NUNCA ES «¿ES UN CRIPTOACTIVO?»
ES «¿EN QUÉ CASILLA CAE, Y QUIÉN LO HACE?»
```

## 📖 Desarrollo

### 1. Qué es MiCA y qué problema resolvió

MiCA es el Reglamento (UE) 2023/1114, publicado en el Diario Oficial de la Unión
Europea el 9 de junio de 2023. Su aplicación fue escalonada: los títulos sobre
fichas referenciadas a activos y fichas de dinero electrónico entraron antes que
el resto, precisamente porque eran los que el legislador consideraba más
urgentes. Ese escalonamiento no es un detalle administrativo: significa que
durante un periodo hubo emisores de stablecoins sujetos y proveedores de
servicios todavía no sujetos, y esa asimetría produjo situaciones que conviene
entender antes de comparar regímenes.

Por ser un reglamento y no una directiva, se aplica de forma directa en todos los
Estados miembros sin necesidad de transposición. Esa elección de instrumento fue
deliberada: una directiva habría producido veintisiete variantes nacionales, y el
objetivo declarado era exactamente lo contrario, un pasaporte único.

```text
POR QUÉ UN REGLAMENTO Y NO UNA DIRECTIVA

  DIRECTIVA   cada Estado la transpone
              → 27 versiones
              → arbitraje entre ellas
              → y una autorización que no viaja

  REGLAMENTO  se aplica igual en todos
              → una autorización
              → válida en los 27
              → «pasaporte»

EL PRECIO DE ESA UNIFORMIDAD
  el texto es más rígido: adaptarlo exige
  reformar el reglamento, no una circular
  nacional
```

### 2. Qué queda fuera, y por qué eso importa más que lo que queda dentro

Las exclusiones de MiCA son la parte del reglamento que más trabajo da en la
práctica, porque determinan si un proyecto debe hablar con el supervisor de
criptoactivos o con el de valores, y ese error de puerta cuesta meses.

Quedan fuera los criptoactivos que ya son instrumentos financieros, los depósitos
—incluidos los estructurados—, los fondos que no sean fichas de dinero
electrónico, las posiciones de titulización, los productos de seguro y de
pensiones, y las monedas digitales emitidas por bancos centrales cuando actúan
como autoridad monetaria. También quedan fuera, con matices, los activos
verdaderamente únicos y no fungibles, y aquí conviene ser preciso: la exclusión
mira la fungibilidad real, no la etiqueta. Una serie de miles de piezas
intercambiables no deja de ser fungible porque cada una lleve un número distinto.

```text
LA EXCLUSIÓN QUE MÁS SE INVOCA MAL

  «ES UN NFT, ESTÁ EXCLUIDO»

  LA PREGUNTA REAL
    · ¿son intercambiables entre sí?
    · ¿se emiten en serie amplia?
    · ¿se cotizan como una unidad genérica?
    · ¿el precio de uno predice el del otro?

  SI LA RESPUESTA ES SÍ, SON FUNGIBLES
  aunque cada uno tenga identificador propio,
  y la exclusión no se aplica

Y SI ADEMÁS OTORGAN UN DERECHO ECONÓMICO
SOBRE UN FLUJO, el filtro 1 los saca de MiCA
y los mete en el régimen de valores
```

La otra exclusión relevante es la de los servicios prestados de forma
completamente descentralizada sin intermediario. Es una exclusión honesta y a la
vez es el mayor agujero declarado del régimen: la norma reconoce que no puede
exigir cumplimiento a quien no existe como sujeto. La clase 2 de esta parte ya
había identificado ese límite del principio de «misma actividad, mismo riesgo»;
MiCA es la prueba de que un legislador que lo intenta se encuentra con él.

### 3. Las tres categorías, y la promesa que las separa

La clasificación de MiCA no mira la tecnología ni el respaldo declarado: mira
**contra qué se estabiliza el valor**. Esa es la misma pregunta que la Parte 20
enseñó a hacer sin jurisdicción, y aquí aparece convertida en derecho positivo.

```text
LAS TRES CATEGORÍAS

  FICHA DE DINERO ELECTRÓNICO
    · referencia: UNA moneda oficial
    · reembolso a la par, en todo momento
    · emisor: entidad de crédito o de
      dinero electrónico
    · no se remunera el saldo

  FICHA REFERENCIADA A ACTIVOS
    · referencia: una cesta, varias monedas,
      materias primas u otros criptoactivos
    · reserva de activos con reglas propias
    · emisor autorizado específicamente
    · tampoco se remunera el saldo

  OTROS CRIPTOACTIVOS
    · no prometen estabilidad
    · régimen mucho más ligero
    · libro blanco notificado, no aprobado
```

La prohibición de remunerar el saldo aparece en las dos categorías estables y
merece una explicación, porque casi nadie la anticipa. No es una medida de
protección del consumidor: es una medida de estabilidad financiera. Un
instrumento que paga interés, es reembolsable a la par y circula sin fricción
compite directamente con el depósito bancario, y si esa competencia se resuelve a
favor del instrumento, el crédito bancario se financia peor. El legislador
prefirió cortar esa vía por delante. Quien diseñe un producto sobre estas
categorías debe saber que el rendimiento tendrá que venir de otro sitio.

### 4. Los proveedores de servicios y la lista que los define

MiCA no define al proveedor por lo que es sino por lo que hace, con una lista
cerrada de servicios. Estar en la lista obliga a autorizarse; no estarlo, no.

```text
SERVICIOS QUE ACTIVAN LA AUTORIZACIÓN

  · custodia y administración por cuenta
    de terceros
  · explotación de una plataforma de
    negociación
  · canje de criptoactivos por fondos
  · canje de criptoactivos por otros
    criptoactivos
  · ejecución de órdenes por cuenta ajena
  · colocación de criptoactivos
  · recepción y transmisión de órdenes
  · asesoramiento
  · gestión de carteras
  · servicios de transferencia por cuenta
    de terceros

CADA UNO TIENE REQUISITOS PROPIOS
de capital, gobierno y salvaguarda; no es
una autorización única con diez casillas
```

El detalle operativo que más sorprende es que la autorización se concede por
servicio. Una entidad autorizada para custodiar no puede, por ese solo hecho,
explotar una plataforma. Y el orden en que se piden los servicios condiciona el
coste: ampliar una autorización existente es más barato que obtener una nueva,
pero pedir de entrada más servicios de los que se van a prestar carga a la
entidad con requisitos que tendrá que sostener aunque el servicio no genere
ingresos. Es la misma aritmética que la clase 4 de esta parte convirtió en una
cifra de facturación de equilibrio.

### 5. El libro blanco: qué es y qué no es

El libro blanco es el documento de información del emisor u oferente. Contiene la
descripción del proyecto, del activo, de los derechos y obligaciones asociados,
de la tecnología subyacente y de los riesgos. Y su régimen tiene una asimetría
que hay que memorizar, porque es donde se producen los anuncios engañosos.

```text
DOS REGÍMENES DISTINTOS

  OTROS CRIPTOACTIVOS
    · el libro blanco se NOTIFICA a la
      autoridad
    · no hay aprobación previa
    · la autoridad puede intervenir después

  FICHAS REFERENCIADAS A ACTIVOS
    · hay AUTORIZACIÓN del emisor
    · y APROBACIÓN del libro blanco

LO QUE NUNCA SIGNIFICA UN LIBRO BLANCO
  · que la autoridad avale el proyecto
  · que el activo sea seguro
  · que el rendimiento prometido exista

LO QUE SÍ SIGNIFICA
  · que hay un responsable identificable
  · y que responde civilmente por la
    información incompleta o engañosa

Y ESO ÚLTIMO ES MUCHO MÁS DE LO QUE HABÍA
ANTES: antes no había a quién demandar.
```

### 6. Instrumentos significativos y el cambio de supervisor

Cuando una ficha alcanza determinada escala deja de ser un asunto nacional. MiCA
prevé umbrales —número de tenedores, valor emitido, volumen y número de
operaciones diarias, relevancia para los sistemas de pago— y, superados, la
supervisión se traslada a la Autoridad Bancaria Europea.

```text
QUÉ CAMBIA AL SER SIGNIFICATIVO

  ANTES   supervisor nacional
          requisitos ordinarios

  DESPUÉS supervisión de la EBA
          requisitos reforzados de fondos
          propios, liquidez e
          interoperabilidad
          plan de recuperación y de
          reembolso exigidos y revisados

POR QUÉ EXISTE ESTE ESCALÓN
  una ficha de dinero electrónico grande
  deja de ser un producto y pasa a ser
  infraestructura de pagos: su fallo ya no
  daña solo a sus tenedores

ES EL MISMO RAZONAMIENTO QUE LA CLASE 15
aplicó a la estabilidad financiera, aquí
escrito en un artículo con umbrales.
```

## 🧮 Ejemplo guiado

El ejemplo recorre el embudo con cuatro productos que una misma entidad quiere
lanzar. Ninguno es real; los cuatro reproducen discusiones habituales de
calificación.

**Situación.** Una entidad quiere lanzar cuatro productos dirigidos a residentes
de la Unión Europea y pregunta cuántas autorizaciones necesita.

```text
PRODUCTOS
  A · token que promete un euro por unidad,
      reembolsable en todo momento
  B · token respaldado por una cesta de
      cuatro monedas y oro
  C · token de una plataforma, sin promesa
      de valor, que da descuentos de uso
  D · token que reparte el 4 % del ingreso
      de una cartera de inmuebles

SERVICIOS PREVISTOS
  · custodiar los cuatro para sus clientes
  · permitir el cambio contra euros
  · operar un tablón donde los clientes
    publican ofertas y casan entre sí
```

**Paso 1 — aplica el filtro 1 a cada producto.**

```text
A · ¿es instrumento financiero?  no
B · ¿es instrumento financiero?  no
C · ¿es instrumento financiero?  no
D · reparte el 4 % del ingreso de
    una cartera → derecho económico
    sobre un flujo de un tercero

  → D SALE DE MICA
    régimen de valores: folleto,
    intermediación, depositario

  ESTE ES EL HALLAZGO MÁS CARO DEL
  EJERCICIO Y APARECE EN EL PRIMER PASO
```

**Paso 2 — clasifica los tres restantes.**

```text
A · estabiliza contra UNA moneda oficial
    → ficha de dinero electrónico
    → emisor: entidad de crédito o de
      dinero electrónico
    → la entidad NO lo es hoy

B · estabiliza contra una cesta
    → ficha referenciada a activos
    → autorización específica de emisor
    → y aprobación del libro blanco

C · no promete estabilidad
    → otros criptoactivos
    → libro blanco notificado
```

**Paso 3 — cuenta las autorizaciones de emisor.**

```text
A · exige ser entidad de dinero electrónico
    o de crédito       → NO la tiene
B · exige autorización de emisor de fichas
    referenciadas      → NO la tiene
C · no exige autorización de emisor
D · fuera de MiCA; exige régimen de valores

  AUTORIZACIONES DE EMISOR PENDIENTES: 3
  (dos en MiCA y una en valores)
```

**Paso 4 — clasifica los servicios previstos.**

```text
custodiar por cuenta de clientes
  → servicio listado · autorización

cambiar contra euros
  → canje por fondos · autorización

«un tablón donde los clientes publican
 ofertas y casan entre sí»
  → esto es una plataforma de negociación
    aunque la entidad lo llame tablón

  → tercer servicio · autorización
```

**Paso 5 — comprueba el cruce que nadie mira.**

```text
LOS SERVICIOS SE PRESTARÍAN TAMBIÉN SOBRE D

  y D no es un criptoactivo de MiCA:
  es un valor

  → CUSTODIAR D NO ES «CUSTODIA MICA»
    es custodia de instrumentos financieros
  → CASAR ÓRDENES SOBRE D NO ES UNA
    PLATAFORMA MICA
    es un centro de negociación

  LA MISMA OPERACIÓN, DOS RÉGIMENES,
  DOS SUPERVISORES Y DOS AUTORIZACIONES
```

**Paso 6 — cuantifica antes de decidir.**

```text
SUPUESTOS DEL EJERCICIO (sintéticos)

  autorización de proveedor, 3 servicios
    inicial            420 000
    anual              260 000
  emisor de fichas referenciadas
    inicial            350 000
    anual              180 000
  entidad de dinero electrónico
    inicial            300 000
    anual              150 000
  régimen de valores para D
    inicial            480 000
    anual              300 000

  TOTAL INICIAL      1 550 000
  TOTAL ANUAL          890 000
```

**Paso 7 — decide qué se lanza.**

```text
INGRESO ESPERADO POR PRODUCTO (supuesto)
  A   180 000     B   120 000
  C    90 000     D   640 000

  D FINANCIA SU PROPIO RÉGIMEN
    640 000 frente a 300 000 anuales

  B NO
    120 000 frente a 180 000 anuales
    y 350 000 de entrada

DECISIÓN RAZONADA
  · lanzar D por el régimen de valores
  · lanzar A solo si se obtiene la licencia
    de dinero electrónico, que sirve además
    para otros productos
  · aplazar B: es el más caro y el que menos
    aporta
  · C entra casi sin coste marginal
```

**Interpreta:** el producto que parecía más simple —B, «una stablecoin de cesta»—
resultó el más caro y el menos rentable, y el que parecía más exótico —D— era el
único que financiaba su propio régimen. El error que el ejercicio evita es el
habitual: **decidir la cartera por afinidad tecnológica y descubrir la
calificación después**, cuando ya hay contratos firmados.

## 🧭 Perspectivas

Un mismo régimen se ve distinto según desde dónde se mire, y esas diferencias
explican buena parte de las tensiones de aplicación.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente minorista | Un libro blanco que no leerá | Si compra |
| Emisor | Tres categorías y un umbral | Qué promete y qué no |
| Proveedor | Diez servicios con requisitos propios | Cuáles solicita |
| Entidad de crédito | Una vía propia para el dinero electrónico | Si compite o se asocia |
| Plataforma | Que operar un tablón es operar un mercado | Si se autoriza o cierra |
| Autoridad nacional | Notificaciones sin aprobación previa | Cuándo interviene |
| EBA y ESMA | Instrumentos que cruzan umbrales | Cuándo asumen la supervisión |
| Supervisor de valores | Tokens que salen por el filtro 1 | Si exige folleto |
| Sociedad | Un mercado con responsables identificables | Qué protección espera |

## 🏦 Del cliente al banco

Las tres frases de la columna izquierda se oyen en el mercado y las tres son
incorrectas por el mismo motivo: confunden un acto de información con un aval.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Está aprobado por Europa» | El libro blanco se notifica, no se aprueba | 22, clase 17 |
| «Es una stablecoin, están reguladas» | Solo si cae en las dos categorías estables | 22, clase 17 |
| «Es un NFT, no aplica la norma» | La exclusión mira la fungibilidad real | 22, clase 17 |

## ⚖️ Riesgos y controles

Los riesgos de esta clase son de calificación, y su coste no es una multa: es
haber construido un producto bajo el régimen equivocado.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Saltarse el filtro 1 | Se diseña bajo MiCA algo que es un valor | Aplicar el filtro antes que nada |
| Etiqueta en lugar de análisis | «Es un NFT, está excluido» | Comprobar fungibilidad real |
| Confundir notificación y aprobación | Se comunica un aval inexistente | Revisar toda pieza comercial |
| Pedir servicios de más | Requisitos sin ingreso que los sostenga | Solicitar por servicio y por fase |
| Ignorar el umbral de significatividad | Cambio de supervisor no previsto | Monitorizar tenedores y volumen |
| Prometer rendimiento del saldo | Está prohibido en las dos categorías estables | Rediseñar la fuente del rendimiento |

## 🧪 Práctica

El laboratorio de comparación de regímenes es el que mejor encaja con esta clase,
porque obliga a citar el artículo y la fecha en cada celda.

En [`labs/lab-08.md`](../labs/lab-08.md):

1. Aplica el embudo de tres filtros a cuatro productos y justifica cada salida.
2. Construye la tabla de autorizaciones de emisor y de proveedor que resulta.
3. Cuantifica la carga inicial y anual, y compárala con el ingreso esperado.
4. Señala qué celdas de tu tabla caducan antes y con qué frecuencia se revisan.

## ⚠️ Errores frecuentes

Los seis síntomas describen proyectos que descubren tarde su calificación. La
causa casi siempre es haber empezado por la tecnología.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Diseñar y calificar después | La calificación parece un trámite | Calificar antes de contratar |
| «MiCA regula todos los tokens» | Es el régimen más citado | Tiene exclusiones amplias |
| Tratar el libro blanco como folleto | Ambos son documentos de oferta | Uno se aprueba, otro se notifica |
| Una autorización para todo | Se piensa en licencias bancarias | Se concede por servicio |
| Llamar tablón a un mercado | El nombre suena informal | La función define el régimen |
| Copiar una tabla comparada | Es rápido | Sin fecha ni artículo no sirve |

## ❓ Preguntas de comprobación

1. ¿Qué hace el primer filtro del embudo y por qué se aplica antes que los otros?
2. ¿Qué separa una ficha de dinero electrónico de una ficha referenciada a activos?
3. ¿Por qué está prohibido remunerar el saldo de ambas categorías?
4. ¿Qué diferencia hay entre notificar un libro blanco y obtener una autorización?
5. ¿Qué cambia cuando un instrumento se declara significativo?

## 📥 Entregable

Guarda en `portfolio/parte-22/clase-17/`:

- el embudo aplicado a cuatro productos, con la salida justificada de cada uno;
- la lista de autorizaciones de emisor y de proveedor que resulta del análisis;
- la cuantificación de carga regulatoria frente al ingreso esperado por producto;
- una nota de una página sobre qué producto aplazarías y por qué.

## 🔗 Referencias cruzadas

- **Viene de:** clase 3 de esta parte, calificación sin jurisdicción; Parte 20,
  clases 1 y 5.
- **Continúa en:** clase 18 de esta parte, que desarrolla las obligaciones.
- **Se aplica en:** clase 22 de esta parte; Parte 23, clases 3 y 11.

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

- Diario Oficial de la Unión Europea (2023). *Reglamento (UE) 2023/1114 relativo a los mercados de criptoactivos*. EUR-Lex. Texto que la clase lee para delimitar el perímetro. <https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32023R1114>
- Autoridad Bancaria Europea. *Markets in Crypto-Assets Regulation (MiCAR)*. EBA. Interpretación supervisora del alcance del reglamento. <https://www.eba.europa.eu/markets-crypto-assets>
- Autoridad Europea de Valores y Mercados. *Crypto-assets and their markets*. ESMA. Criterios de calificación de los activos y de los servicios. <https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica>
- Comisión Europea. *Digital finance package*. European Commission. Encaje de MiCA en el paquete europeo de finanzas digitales. <https://finance.ec.europa.eu/digital-finance_en>
- Ficha normativa del repositorio: `regulatory/union-europea/mica-reglamento-2023-1114.yml`
- Verificación local: MiCA es derecho de la Unión Europea y **no es derecho aplicable en Chile**; se estudia como referencia comparada. Los actos delegados y las normas técnicas posteriores modifican el detalle: consulta siempre la versión consolidada en EUR-Lex. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-20.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 16 · Regulación comparada: Chile y el mundo](16-regulacion-comparada-chile-y-el-mundo.md) | [Parte 22](../README.md) · [Programa](../../../SYLLABUS.md) | [18 · MiCA II: obligaciones, reservas y supervisión →](18-mica-obligaciones-reservas-y-supervision.md) |
<!-- gen:footer:end -->
