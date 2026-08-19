<!-- meta
part: 22
class: 19
title: "Regímenes europeos conexos: piloto DLT, DORA y regla del viaje"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [union-europea]
regulatory_topics: [dlt-pilot, resiliencia-operativa, regla-del-viaje, terceros-criticos]
regulation_last_verified: 2026-08-12
regulatory_status: vigente
primary_authorities: [ESMA, EBA, EIOPA]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 19 · Regímenes europeos conexos: piloto DLT, DORA y regla del viaje

> [← 18 · MiCA II: obligaciones, reservas y supervisión](18-mica-obligaciones-reservas-y-supervision.md) · [Índice de la parte](../README.md) · [20 · El Salvador: bitcoin, Chivo y activos digitales →](20-el-salvador-bitcoin-chivo-y-activos-digitales.md)

**Parte 22 — Regulación de mercados financieros digitales** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Completar el mapa europeo con las tres normas que MiCA **no** cubre y sin las
cuales el régimen no funciona: la que permite negociar y liquidar valores
tokenizados, la que impone resiliencia operativa a todo el sector financiero, y
la que obliga a que los datos del ordenante viajen con la transferencia.

Las dos clases anteriores dejaron una impresión incompleta a propósito. Quien
solo estudia MiCA concluye que el régimen europeo de los activos digitales es un
reglamento; en realidad son cuatro piezas que se aplican a la vez, y la mayoría
de los proyectos que fallan en la práctica no fallan por MiCA sino por una de
las otras tres.

Hay una razón adicional para estudiarlas juntas. Cada una responde una pregunta
que este programa ya había planteado sin jurisdicción: la Parte 21 preguntó cómo
se negocia un valor tokenizado cuando la norma de depositarios exige un
depositario; la clase 14 midió qué pasa cuando veintidós entidades comparten un
proveedor; la Parte 18 explicó la regla del viaje como estándar internacional.
Aquí están las tres respuestas escritas en derecho aplicable.

## 📚 Objetivos

Al finalizar podrás:

1. **Explicar** qué exenciones concede el régimen piloto de infraestructuras DLT
   y a cambio de qué límites.
2. **Distinguir** las tres figuras de infraestructura que el régimen piloto crea
   y qué hace posible la tercera.
3. **Enumerar** los cinco pilares de la resiliencia operativa digital y señalar
   cuál es una novedad estructural.
4. **Determinar** qué información debe acompañar a una transferencia de
   criptoactivos y qué ocurre si falta.
5. **Analizar** el tratamiento de las direcciones autoalojadas y por qué es el
   punto más discutido del régimen.

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

Los tres primeros términos pertenecen al régimen piloto; los tres siguientes, a
la resiliencia operativa; los dos últimos, a la regla del viaje. La distinción
que más consecuencias tiene es `exención con límite`: el piloto no elimina un
requisito, lo suspende a cambio de un tamaño máximo.

| Concepto | Comprensión verificable |
|---|---|
| `infraestructura DLT` | Mercado o sistema de liquidación sobre registro distribuido |
| `exención con límite` | Dispensa temporal a cambio de un tope de volumen |
| `sistema conjunto` | Negociación y liquidación en la misma entidad |
| `pruebas de resiliencia` | Ejercicios que verifican la continuidad real |
| `proveedor crítico` | Tercero designado y vigilado por la autoridad |
| `vigilancia directa` | Supervisión del proveedor, no solo de su cliente |
| `regla del viaje` | Datos del ordenante y beneficiario que acompañan la operación |
| `dirección autoalojada` | Dirección controlada por su titular, sin proveedor |

## 🧠 Modelo mental

El modelo mental es un edificio de cuatro plantas donde MiCA es solo una de
ellas, y donde quitar cualquiera deja el conjunto sin sostén.

```text
EL EDIFICIO EUROPEO

  QUÉ SE EMITE Y QUIÉN LO PRESTA
    MiCA · categorías, emisores,
    proveedores, abuso de mercado

  DÓNDE SE NEGOCIA Y LIQUIDA UN VALOR
    piloto DLT · exenciones temporales
    con topes

  QUE NO SE CAIGA
    DORA · riesgo tecnológico, incidentes,
    pruebas, terceros críticos

  DE DÓNDE VIENE EL DINERO
    regla del viaje · datos que acompañan
    a la transferencia

SI FALTA LA SEGUNDA, un valor tokenizado
no encuentra dónde liquidarse.
SI FALTA LA TERCERA, el mercado depende de
proveedores que nadie supervisa.
SI FALTA LA CUARTA, el mercado queda fuera
del sistema de prevención.
```

## 📖 Desarrollo

### 1. Por qué hizo falta un régimen piloto

La Parte 21 lo dejó planteado con precisión: la norma de infraestructuras de
mercado se escribió suponiendo que existe un depositario central que anota los
valores, y una liquidación atómica sobre un registro distribuido no lo necesita.
El resultado es una contradicción práctica: la tecnología permite algo que la
norma exige hacer de otra manera.

Un legislador tiene tres salidas ante esa situación y las tres son malas. Puede
prohibir, y renuncia a la innovación. Puede reformar la norma general, y hacerlo
sin evidencia es imprudente. O puede crear un régimen temporal con exenciones y
topes, recoger la experiencia y decidir después. El Reglamento (UE) 2022/858
eligió la tercera.

```text
EL RÉGIMEN PILOTO EN UNA LÍNEA

  «te dispenso de requisitos concretos,
   durante un tiempo, y a cambio no puedes
   pasar de cierto tamaño»

TRES FIGURAS

  SISTEMA MULTILATERAL DE NEGOCIACIÓN DLT
    negocia; no liquida

  SISTEMA DE LIQUIDACIÓN DLT
    liquida; no negocia

  SISTEMA CONJUNTO DLT
    negocia Y liquida en la misma entidad
    → ESTA ES LA NOVEDAD REAL:
      en el régimen ordinario esas dos
      funciones deben estar separadas
```

### 2. Los límites: lo que el piloto compra y lo que cuesta

Las exenciones vienen con topes cuantitativos por instrumento y por
infraestructura. Los importes concretos deben verificarse en el texto vigente,
pero la lógica no cambia: el tope existe para que un fallo del experimento no se
convierta en un problema del sistema.

```text
LA LÓGICA DE LOS TOPES

  · límite por emisión admitida
  · límite por tipo de instrumento
  · límite agregado por infraestructura
  · y si se supera, hay que salir del
    régimen de forma ordenada

LO QUE COMPRA EL PILOTO
  · probar la liquidación en el registro
  · probar el sistema conjunto
  · producir evidencia para la reforma

LO QUE CUESTA
  · un techo que impide escalar
  · una estrategia de transición obligatoria
  · y la incertidumbre de qué pasa al final
    del periodo
```

Ese último punto es el que más condiciona las decisiones de inversión. Construir
una infraestructura sabiendo que el régimen que la ampara es temporal exige
responder desde el primer día qué se hace con los instrumentos admitidos si el
régimen no se prorroga o no se convierte en definitivo. La clase 21 de esta
parte, sobre espacios de prueba, explica por qué la mayoría de estos regímenes
producen menos conocimiento del que prometen: quien entra sin plan de salida
suele salir sin nada.

### 3. Resiliencia operativa: los cinco pilares

El Reglamento (UE) 2022/2554 —DORA— se aplica desde enero de 2025 y armoniza lo
que antes estaba repartido en normas sectoriales. Su alcance incluye a los
proveedores de servicios de criptoactivos autorizados conforme a MiCA, lo que
significa que la entidad de la clase 17 tiene dos reglamentos encima.

```text
LOS CINCO PILARES

  1 · GESTIÓN DEL RIESGO TECNOLÓGICO
      marco escrito, aprobado por el órgano
      de administración, con responsable

  2 · NOTIFICACIÓN DE INCIDENTES
      clasificación por gravedad y plazos
      de comunicación al supervisor

  3 · PRUEBAS DE RESILIENCIA
      periódicas; y para las entidades más
      significativas, pruebas avanzadas
      guiadas por amenazas reales

  4 · RIESGO DE TERCEROS
      registro de acuerdos, cláusulas
      mínimas, plan de salida

  5 · INTERCAMBIO DE INFORMACIÓN
      sobre amenazas, entre entidades
```

El cuarto pilar contiene la novedad estructural del régimen y merece detenerse.
Hasta DORA, un supervisor financiero solo podía exigir a la entidad supervisada;
si el problema estaba en un proveedor común a muchas entidades, la única vía era
exigir a cada una que controlara a su proveedor. DORA crea una figura distinta:
los proveedores designados como críticos quedan sujetos a **vigilancia directa**
de la autoridad europea correspondiente, que puede formular requerimientos al
proveedor.

```text
EL CAMBIO QUE INTRODUCE LA VIGILANCIA
DIRECTA

  ANTES
    supervisor → entidad → proveedor
    (22 conversaciones para un problema)

  AHORA
    supervisor → entidad
    autoridad   → proveedor crítico
    (1 conversación para el problema común)

ES LA RESPUESTA EXPRESA AL CASO QUE LA
CLASE 14 CUANTIFICÓ: veintidós entidades
que cumplen su norma y un proveedor que
concentra el 86 %.
```

### 4. La regla del viaje europea

El Reglamento (UE) 2023/1113 traslada a las transferencias de criptoactivos la
obligación que ya regía para las transferencias de fondos: que la operación viaje
acompañada de la identificación del ordenante y del beneficiario. Es la versión
vinculante de la Recomendación 16 del GAFI que la Parte 18 estudió como
estándar, y la diferencia entre ambas cosas es exactamente la que la clase 16 de
esta parte enseñó a no confundir: un estándar orienta, un reglamento obliga y se
sanciona.

```text
QUÉ DEBE ACOMPAÑAR A LA TRANSFERENCIA

  DEL ORDENANTE
    nombre, identificador de cuenta o
    dirección, y datos identificativos
    adicionales según el caso

  DEL BENEFICIARIO
    nombre e identificador de cuenta
    o dirección

UNA DIFERENCIA IMPORTANTE CON LOS FONDOS
  en las transferencias de fondos existe un
  umbral por debajo del cual la información
  exigida se reduce

  en las transferencias de criptoactivos el
  régimen NO establece ese umbral general:
  la información acompaña a la operación
  con independencia del importe

VERIFICA ESTE PUNTO EN EL TEXTO VIGENTE
antes de configurar ningún sistema.
```

### 5. Direcciones autoalojadas: el punto discutido

Una transferencia entre dos proveedores autorizados es sencilla de resolver:
ambos son sujetos obligados y ambos tienen a quién pedir los datos. El problema
aparece cuando el otro extremo es una dirección que su titular controla
directamente, sin intermediario.

```text
LAS TRES POSTURAS QUE SE ENFRENTARON

  A · prohibir esas transferencias
      → empuja la actividad fuera del
        perímetro y no la elimina

  B · tratarlas como cualquier otra
      → la información del otro extremo
        no es verificable

  C · admitirlas con medidas reforzadas
      → el proveedor debe verificar que su
        cliente controla la dirección
        cuando se superan ciertos importes

EL RÉGIMEN EUROPEO SIGUIÓ LA TERCERA VÍA

POR QUÉ SIGUE SIENDO DISCUTIDO
  · verificar el control de una dirección
    es técnicamente posible y molesto
  · una dirección autoalojada puede ser
    de un tercero
  · y la medida no impide la transferencia,
    solo la documenta
```

### 6. Cómo se aplican las cuatro normas a la vez

La consecuencia práctica de tener cuatro regímenes simultáneos es que una misma
decisión de producto se evalúa cuatro veces, y las cuatro respuestas pueden no
coincidir. Es exactamente el ejercicio de cruce que la clase 22 de esta parte
convierte en expediente.

```text
UNA MISMA OPERACIÓN, CUATRO LECTURAS

  «lanzar un servicio de transferencia de
   fichas de dinero electrónico»

  MiCA      ¿está el servicio en la lista?
            → sí: autorización

  PILOTO    no aplica: no hay valor
            negociado

  DORA      ¿quién opera el sistema?
            → si es un tercero, contrato,
              plan de salida y registro

  VIAJE     ¿acompaña la información?
            → sí, siempre, y hay que
              decidir qué se hace con las
              direcciones autoalojadas

TRES DE LAS CUATRO OBLIGAN.
Y NINGUNA DE LAS TRES SUSTITUYE A OTRA.
```

## 🧮 Ejemplo guiado

El ejemplo evalúa un mismo proyecto contra las cuatro normas y calcula qué parte
del coste procede de cada una, que es el dato que ningún plan de negocio incluye
al principio.

**Situación.** Una entidad quiere operar un sistema conjunto de negociación y
liquidación de bonos tokenizados, con liquidación en fichas de dinero
electrónico, y contratar la infraestructura técnica a un proveedor externo.

```text
DATOS DEL PROYECTO
  emisiones previstas, año 1        12
  importe medio por emisión  40 000 000
  volumen negociado esperado 90 000 000
  clientes institucionales          180
  transferencias mensuales       14 000
  proveedor técnico              1, externo
  entidades que usan ese mismo
    proveedor en el mercado          19
```

**Paso 1 — determina qué norma alcanza cada pieza.**

```text
BONO TOKENIZADO
  → es un valor: sale de MiCA por el
    filtro 1 (clase 17)
  → régimen de valores, y para negociar y
    liquidar en la misma entidad hace falta
    el RÉGIMEN PILOTO

FICHA DE DINERO ELECTRÓNICO usada para
liquidar
  → MiCA: emisor habilitado y reembolso
    a la par

SISTEMA OPERADO POR UN TERCERO
  → DORA: registro, cláusulas y salida

TRANSFERENCIAS ENTRE CLIENTES
  → regla del viaje
```

**Paso 2 — comprueba el tope del piloto.**

```text
VOLUMEN ADMITIDO PREVISTO
  12 × 40 000 000 = 480 000 000

  → hay que contrastarlo con el límite
    agregado vigente de la infraestructura
    y con el límite por tipo de instrumento

SI EL CRECIMIENTO PREVISTO PARA EL AÑO 3 ES
  36 emisiones × 40 000 000 = 1 440 000 000

  LA PREGUNTA NO ES SI CABE HOY
  ES CUÁNDO DEJA DE CABER, Y QUÉ SE HACE
  ESE DÍA
```

**Paso 3 — evalúa la concentración del proveedor.**

```text
19 ENTIDADES + LA PROPIA = 20 CLIENTES
DEL MISMO PROVEEDOR

  → candidato claro a designación como
    proveedor crítico

CONSECUENCIAS SI SE DESIGNA
  · vigilancia directa sobre el proveedor
  · requerimientos que pueden obligarle a
    cambiar su servicio
  · y la entidad hereda esos cambios sin
    haberlos pedido

CONSECUENCIA SI NO SE DESIGNA
  · la entidad responde sola de un riesgo
    que comparte con 19 competidores
```

**Paso 4 — dimensiona el plan de salida.**

```text
PREGUNTA DE DORA QUE NADIE SABE RESPONDER
  «si este proveedor deja de prestar el
   servicio, ¿en cuánto tiempo operas?»

INVENTARIO NECESARIO
  · datos que están en el proveedor
  · formato en que se pueden extraer
  · alternativa identificada
  · tiempo de migración estimado
  · y una prueba de que la extracción
    funciona

SI LA EXTRACCIÓN NO SE HA PROBADO,
EL PLAN DE SALIDA ES UNA REDACCIÓN.
```

**Paso 5 — calcula la carga de la regla del viaje.**

```text
TRANSFERENCIAS MENSUALES        14 000
  entre proveedores autorizados   11 200   80 %
  con dirección autoalojada        2 800   20 %

COSTE UNITARIO SUPUESTO
  automática                        0,12
  con verificación de control       3,40

COSTE MENSUAL
  11 200 × 0,12 =                 1 344
   2 800 × 3,40 =                 9 520
  TOTAL                          10 864
  ANUAL                         130 368

  EL 20 % DE LAS OPERACIONES GENERA
  EL 88 % DEL COSTE
```

**Paso 6 — reparte el coste regulatorio por norma.**

```text
SUPUESTOS ANUALES (sintéticos)

  régimen de valores + piloto     540 000
  MiCA (emisor y servicios)       260 000
  DORA (marco, pruebas, terceros) 310 000
  regla del viaje                 130 368

  TOTAL                         1 240 368

  MiCA ES EL 21 %
  Y ES LA ÚNICA QUE APARECÍA EN EL PLAN
  DE NEGOCIO INICIAL
```

**Paso 7 — decide.**

```text
DOS CONCLUSIONES ACCIONABLES

  1 · el techo del piloto llega antes que
      el punto de equilibrio
      → o se diseña la transición desde el
        inicio, o el proyecto tiene fecha
        de caducidad

  2 · el coste de la regla del viaje se
      concentra en el 20 % de operaciones
      → decidir explícitamente si se
        admiten direcciones autoalojadas,
        y comunicarlo

LO QUE NO ES UNA OPCIÓN
  descubrir cualquiera de las dos cosas
  en el año 3
```

**Interpreta:** el proyecto era viable y su principal riesgo no era regulatorio en
el sentido habitual —ninguna norma lo prohibía—, sino **de secuencia**: el
régimen que lo hacía posible era temporal y con techo, y el plan de negocio
suponía un crecimiento que ese techo no admite. Ese es el fallo típico de los
regímenes experimentales, y se detecta en el paso 2 o no se detecta.

## 🧭 Perspectivas

Las tres normas reparten carga y protección de forma muy desigual entre los
participantes.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Inversor institucional | Un mercado con techo de volumen | Si entra o espera |
| Emisor de bonos | Una vía nueva de emisión | Si tokeniza |
| Infraestructura | Exenciones con fecha | Cómo planifica la transición |
| Proveedor técnico | Posible designación como crítico | Si acepta la vigilancia |
| Entidad usuaria | Un riesgo compartido con 19 | Si diversifica |
| Cliente que autocustodia | Verificación de control | Si usa el servicio |
| Autoridad de mercados | Evidencia del experimento | Si propone reforma |
| Autoridad de resiliencia | Un proveedor común | Si lo designa y qué exige |
| Sociedad | Un mercado más trazable | Qué privacidad acepta |

## 🏦 Del cliente al banco

Las tres frases resumen malentendidos que aparecen en proyectos reales, y las
tres se corrigen con el contenido de esta clase.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Ya cumplimos MiCA» | MiCA es el 21 % del coste regulatorio | 22, clase 19 |
| «El proveedor es certificado» | La certificación no es un plan de salida | 22, clase 19 |
| «Mi cartera es mía, no aplica» | La verificación de control sí aplica | 22, clase 19 |

## ⚖️ Riesgos y controles

Los seis riesgos son los que hacen fracasar proyectos que sí tenían la
autorización correcta.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Techo del piloto | El negocio crece y no cabe | Planificar la transición desde el inicio |
| Régimen temporal | Termina sin sucesor | Escenario de no prórroga documentado |
| Proveedor crítico | Requerimientos heredados | Vigilar la designación y sus efectos |
| Plan de salida no probado | Se activa y no funciona | Probar la extracción de datos |
| Coste del viaje mal estimado | Se concentra en pocas operaciones | Separar coste por tipo de contraparte |
| Creer que MiCA basta | Es la norma más visible | Evaluar las cuatro por separado |

## 🧪 Práctica

El laboratorio de resiliencia y terceros críticos es el que mejor sostiene esta
clase, porque obliga a medir la concentración real y no la aparente.

En [`labs/lab-07.md`](../labs/lab-07.md):

1. Construye el mapa de terceros del proyecto, incluida la subcontratación.
2. Calcula la concentración real por infraestructura, no por contrato.
3. Redacta el plan de salida y define cómo probarías la extracción de datos.
4. Reparte el coste regulatorio anual por norma y señala la partida mayor.

## ⚠️ Errores frecuentes

Los seis errores tienen una raíz común: tomar la norma más visible por la única
norma.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Plan de negocio solo con MiCA | Es la más comentada | Evaluar las cuatro |
| Entrar al piloto sin salida | El techo parece lejano | Fecha y plan desde el día 1 |
| Contrato sin derecho de auditoría | Lo ofrece el proveedor | Es exigencia, no negociación |
| Plan de salida sin prueba | Se redacta y se archiva | Probar la extracción |
| Umbral inventado para el viaje | Se copia el de fondos | Verificar en el texto vigente |
| Ignorar las autoalojadas | Son minoría de operaciones | Son mayoría del coste |

## ❓ Preguntas de comprobación

1. ¿Qué concede el régimen piloto y a cambio de qué límite?
2. ¿Qué hace posible el sistema conjunto que el régimen ordinario impide?
3. ¿Qué cambia la vigilancia directa sobre un proveedor crítico?
4. ¿Por qué el tratamiento de las direcciones autoalojadas sigue discutiéndose?
5. ¿Por qué el coste de la regla del viaje se concentra en pocas operaciones?

## 📥 Entregable

Guarda en `portfolio/parte-22/clase-19/`:

- la evaluación de un proyecto contra las cuatro normas europeas, una por una;
- el mapa de terceros con la concentración real y la designación probable;
- el plan de salida del proveedor, con la prueba de extracción definida;
- el reparto del coste regulatorio anual por norma, con supuestos declarados.

## 🔗 Referencias cruzadas

- **Viene de:** clases 17 y 18 de esta parte; clase 14, terceros críticos;
  Parte 18, clase 12; Parte 21, clases 9 y 15.
- **Continúa en:** clase 20 de esta parte, con un caso nacional completo.
- **Se aplica en:** clase 22 de esta parte; Parte 23, clases 7, 13 y 15.

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

- Diario Oficial de la Unión Europea (2022). *Reglamento (UE) 2022/858 sobre un régimen piloto de infraestructuras del mercado basadas en la tecnología de registro descentralizado*. EUR-Lex. Régimen que permite negociar y liquidar valores tokenizados. <https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32022R0858>
- Diario Oficial de la Unión Europea (2022). *Reglamento (UE) 2022/2554 sobre la resiliencia operativa digital del sector financiero*. EUR-Lex. Obligaciones de resiliencia operativa digital del sector. <https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32022R2554>
- Diario Oficial de la Unión Europea (2023). *Reglamento (UE) 2023/1113 relativo a la información que acompaña a las transferencias de fondos y de determinados criptoactivos*. EUR-Lex. Información que debe acompañar a la transferencia de criptoactivos. <https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32023R1113>
- Grupo de Acción Financiera Internacional. *Recomendación 16 y activos virtuales*. GAFI-FATF. Origen internacional de la regla del viaje. <https://www.fatf-gafi.org/en/topics/virtual-assets.html>
- Fichas normativas del repositorio: `regulatory/union-europea/dlt-pilot-reglamento-2022-858.yml`, `regulatory/union-europea/dora-reglamento-2022-2554.yml` y `regulatory/union-europea/transferencias-fondos-reglamento-2023-1113.yml`
- Verificación local: los topes cuantitativos del régimen piloto, los umbrales de la regla del viaje y los criterios de designación de proveedor crítico están en el texto consolidado y en normas técnicas posteriores, y **cambian**. Ninguna cifra de esta clase debe usarse para configurar un sistema sin comprobarla en EUR-Lex. Estas normas no son derecho aplicable en Chile. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-12.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 18 · MiCA II: obligaciones, reservas y supervisión](18-mica-obligaciones-reservas-y-supervision.md) | [Parte 22](../README.md) · [Programa](../../../SYLLABUS.md) | [20 · El Salvador: bitcoin, Chivo y activos digitales →](20-el-salvador-bitcoin-chivo-y-activos-digitales.md) |
<!-- gen:footer:end -->
