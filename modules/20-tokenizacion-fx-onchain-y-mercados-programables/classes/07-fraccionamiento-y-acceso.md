<!-- meta
part: 21
class: 7
title: "Fraccionamiento y acceso"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [chile, internacional]
regulatory_topics: [proteccion-al-inversionista, idoneidad, inclusion-financiera]
regulation_last_verified: 2026-08-20
regulatory_status: vigente
primary_authorities: [IOSCO, OCDE, CMF]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 07 · Fraccionamiento y acceso

> [← 06 · Mercado secundario y liquidez prometida](06-mercado-secundario-y-liquidez-prometida.md) · [Índice de la parte](../README.md) · [08 · Entrega contra pago atómica →](08-entrega-contra-pago-atomica.md)

**Parte 21 — Tokenización, FX on-chain y mercados programables** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Examinar el argumento más simpático de la tokenización —**democratizar el acceso
a activos antes reservados**— y separar en él lo que es real, lo que es
irrelevante y lo que es un riesgo trasladado al que menos puede soportarlo.

La liquidez de la clase anterior condiciona esta. El fraccionamiento baja la barrera de importe y no la de idoneidad, y sin liquidez produce tenedores pequeños que no encuentran a quién vender.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** barrera de importe de barrera de idoneidad y de información.
2. **Calcular** el coste unitario de servicio y su efecto sobre la rentabilidad
   del inversionista pequeño.
3. **Evaluar** si un activo es apropiado para inversionistas minoristas
   independientemente de su importe mínimo.
4. **Diseñar** las salvaguardas de una oferta fraccionada.
5. **Explicar** por qué el acceso sin salida no es acceso.

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

Los tres primeros términos son las barreras que el fraccionamiento pretende bajar; los cinco siguientes, su economía y sus consecuencias. El **acceso sin salida** es el problema que crea: bajar el importe mínimo incorpora tenedores que después no encuentran a quién vender.

| Concepto | Comprensión verificable |
|---|---|
| `fraccionamiento` | División del instrumento en unidades menores |
| `barrera de importe` | Mínimo de inversión que excluye por tamaño |
| `barrera de idoneidad` | Requisito de conocimiento o patrimonio |
| `coste unitario de servicio` | Lo que cuesta atender a un inversionista |
| `rentabilidad neta` | La que queda tras comisiones y costes |
| `concentración por tenedor` | Peso del activo en el patrimonio de cada uno |
| `acceso sin salida` | Poder entrar en algo de lo que no se puede salir |
| `divulgación adaptada` | Información comprensible para el destinatario |

## 🧠 Modelo mental

El modelo mental es que hay dos barreras y el fraccionamiento solo baja una. La de importe se resuelve dividiendo; la de idoneidad es regulatoria y no se resuelve así. Y bajar la primera sin resolver la liquidez produce tenedores atrapados.

```text
TRES BARRERAS, Y EL FRACCIONAMIENTO
SOLO TOCA UNA

  DE IMPORTE
    «hacen falta 100 000 para entrar»
    → el fraccionamiento la elimina

  DE IDONEIDAD
    «este producto exige entender qué es
     un flujo descontado y qué es un
     covenant»
    → el fraccionamiento NO la toca,
      y bajar el importe la agrava

  DE INFORMACIÓN
    «el folleto tiene 180 páginas y supone
     conocimientos de estructuración»
    → el fraccionamiento NO la toca

BAJAR EL IMPORTE SIN TOCAR LAS OTRAS DOS
NO DEMOCRATIZA EL ACCESO:
DEMOCRATIZA LA EXPOSICIÓN.
```

## 📖 Desarrollo

### 1. El coste unitario cambia todo

Atender a un inversionista tiene un coste casi fijo, y sobre importes
pequeños ese coste se vuelve dominante. El bloque pone la cifra y la aplica a
dos tamaños de inversión.

```text
ATENDER A UN INVERSIONISTA CUESTA
CASI LO MISMO SEA GRANDE O PEQUEÑO

  · verificación de identidad
  · evaluación de idoneidad
  · información periódica
  · atención de consultas
  · gestión de eventos corporativos

SUPUESTO TÍPICO: 18 al año por inversionista

  SOBRE UNA INVERSIÓN DE 100 000
    0,018 % anual → despreciable

  SOBRE UNA INVERSIÓN DE 1 000
    1,8 % anual → se come casi toda
    la rentabilidad esperada de muchos activos

SI ESE COSTE SE CARGA AL INVERSIONISTA,
EL PEQUEÑO PAGA CIEN VECES MÁS
POR EL MISMO SERVICIO.

SI NO SE LE CARGA, LO PAGA EL EMISOR
O LA PLATAFORMA, Y HAY QUE VER
DE DÓNDE LO SACAN.
```

### 2. Idoneidad

La idoneidad no pregunta si alguien puede permitirse perder el dinero, sino si
entiende lo que compra. El bloque reformula el criterio y detalla qué exige
una evaluación seria.

```text
LA PREGUNTA NO ES «¿PUEDE PERMITÍRSELO?»
SINO «¿ENTIENDE QUÉ ESTÁ COMPRANDO?»

  y para muchos activos tokenizados
  —crédito privado, inmuebles en desarrollo,
  participaciones en proyectos— la respuesta
  honesta para un minorista es no

QUÉ EXIGE UNA EVALUACIÓN SERIA
  · conocimiento del tipo de activo
  · experiencia previa
  · capacidad de soportar la pérdida
  · horizonte compatible con la iliquidez
  · comprensión de que no hay garantía

Y UNA REGLA QUE SE OLVIDA
  la evaluación tiene que poder dar «no».
  Un cuestionario que nunca excluye a nadie
  no es una evaluación: es un trámite.
```

### 3. Concentración por tenedor

El mismo instrumento puede ser prudente o temerario según el patrimonio de
quien lo compra. El bloque lo muestra con dos casos numéricos y propone el
control que lo tiene en cuenta.

```text
UN MISMO INSTRUMENTO PUEDE SER PRUDENTE
PARA UNO Y TEMERARIO PARA OTRO

  100 000 en un inversionista con
  4 000 000 de patrimonio → 2,5 %

  1 000 en un inversionista con
  3 000 de ahorro → 33 %

  EL SEGUNDO ESTÁ MUCHO MÁS EXPUESTO
  aunque invierta cien veces menos

QUÉ HACER
  · límite de concentración por tenedor,
    no solo mínimo de entrada
  · advertencia explícita si la inversión
    supera un porcentaje del patrimonio
    declarado
  · y aceptar que eso reduce la colocación
```

### 4. Acceso sin salida

Dar acceso a un activo del que no se puede salir no amplía las oportunidades
de nadie. El bloque desarrolla el argumento con los datos de la clase 6 y fija
la regla que se deriva.

```text
EL ACCESO A UN ACTIVO DEL QUE NO SE
PUEDE SALIR NO ES ACCESO: ES UNA TRAMPA

  el inversionista grande puede esperar
  cinco años; el pequeño suele necesitar
  el dinero antes

  y el mercado secundario que se le prometió
  tiene, según la clase 6, un 59 % de días
  sin ninguna operación

REGLA
  antes de fraccionar, mide la liquidez
  secundaria REAL y decláralas en el mismo
  sitio y con el mismo tamaño de letra
  que el importe mínimo
```

### 5. Divulgación adaptada

Un folleto extenso cumple la norma y no informa a quien invierte poco. El
bloque describe qué contenido sí informa, en el formato en que puede leerse.

```text
UN FOLLETO DE 180 PÁGINAS NO INFORMA
A QUIEN INVIERTE 1 000

  QUÉ SÍ INFORMA
    · una página con: qué es, qué pasa si
      sale bien, qué pasa si sale mal,
      cuándo puedo salir y cuánto cuesta
    · el peor escenario histórico del tipo
      de activo, no el escenario base
    · el coste total anual en dinero, no en
      porcentaje
    · una frase sobre qué pasa si la
      plataforma cierra

  QUÉ NO INFORMA
    · rentabilidades pasadas destacadas
    · proyecciones sin escenario adverso
    · la palabra «garantizado» en cualquier
      contexto

ESTO NO SUSTITUYE AL FOLLETO:
LO ACOMPAÑA, Y ES LO QUE LA MAYORÍA LEERÁ.
```

## 🧮 Ejemplo guiado

El ejemplo calcula la rentabilidad neta de un tenedor pequeño tras el coste unitario de servicio. Por debajo de cierto importe, el instrumento no rinde nada para quien lo tiene.

**Situación.** Una emisión de crédito privado tokenizado baja el mínimo de
50 000 a 500. Hay que evaluar si el acceso es real.

```text
DATOS
  rentabilidad bruta esperada           9,2 % anual
  comisión de gestión                   1,5 % anual
  comisión de plataforma                0,8 % anual
  coste unitario de servicio           18 al año
  plazo                                 4 años
  liquidez secundaria      74 días con operación de 182
  inversión mínima nueva                     500
  inversionistas previstos                12 000
```

**Paso 1 — calcula la rentabilidad neta por tamaño.**

```text
RENTABILIDAD NETA DE COMISIONES
  9,2 % − 1,5 % − 0,8 % = 6,9 %

MENOS EL COSTE UNITARIO

  INVERSIÓN DE 50 000
    18 / 50 000 = 0,036 %
    neta = 6,864 %

  INVERSIÓN DE 5 000
    18 / 5 000 = 0,36 %
    neta = 6,54 %

  INVERSIÓN DE 500
    18 / 500 = 3,60 %
    neta = 3,30 %

EL PEQUEÑO OBTIENE MENOS DE LA MITAD
DE LA RENTABILIDAD NETA DEL GRANDE.
```

**Paso 2 — compara con la alternativa sin riesgo.**

```text
SUPUESTO · DEPÓSITO A PLAZO AL 4,1 %

  INVERSIÓN DE 50 000
    6,864 % frente a 4,1 %
    prima por el riesgo: 2,76 puntos

  INVERSIÓN DE 500
    3,30 % frente a 4,1 %
    prima por el riesgo: −0,80 puntos

  → EL INVERSIONISTA DE 500 ASUME
    RIESGO DE CRÉDITO PRIVADO E ILIQUIDEZ
    A CUATRO AÑOS PARA GANAR MENOS
    QUE EN UN DEPÓSITO

Y ESO ANTES DE QUE FALLE NINGÚN CRÉDITO.
```

**Paso 3 — encuentra el importe de equilibrio.**

```text
¿DESDE QUÉ IMPORTE COMPENSA?

  se necesita neta > 4,1 %
  6,9 % − 18/x > 4,1 %
  18/x < 2,8 %
  x > 18 / 0,028 = 642,86

  MÍNIMO TEÓRICO ≈ 643

  Y ESO SOLO PARA EMPATAR CON EL DEPÓSITO.
  Para una prima razonable de 2 puntos:
  6,9 % − 18/x > 6,1 %
  x > 2 250
```

**Paso 4 — mide quién absorbe el coste unitario.**

```text
SI LA PLATAFORMA NO LO CARGA AL PEQUEÑO

  12 000 inversionistas × 18 = 216 000 al año

  ¿DE DÓNDE SALE?
    a  de la comisión de plataforma del 0,8 %
    b  del emisor
    c  de reducir el servicio

  SUPUESTO · EMISIÓN DE 40 000 000
    0,8 % = 320 000 al año
    coste unitario = 216 000
    → el 67,5 % de la comisión se va en
      atender a los pequeños

  → o la plataforma sube la comisión,
    o reduce el servicio (opción c),
    y la opción c es la que ocurre
```

**Paso 5 — evalúa la concentración.**

```text
INVERSIONISTA CON 3 000 DE AHORRO
QUE INVIERTE 500

  16,7 % de su patrimonio financiero
  en crédito privado ilíquido a 4 años

  ¿ES APROPIADO?
    una regla habitual limita los activos
    ilíquidos al 10 % del patrimonio
    financiero de un minorista

  → 500 SUPERA EL LÍMITE PARA QUIEN
    TIENE MENOS DE 5 000

CONSECUENCIA DE DISEÑO
  el mínimo de 500 solo es apropiado para
  quien tiene más de 5 000 de patrimonio
  financiero, y eso hay que evaluarlo,
  no suponerlo
```

**Paso 6 — comprueba la salida.**

```text
LIQUIDEZ SECUNDARIA
  74 días con operación de 182 = 40,7 %

  UN TENEDOR DE 500 QUE NECESITA EL DINERO
  · puede enviar la orden cualquier día
  · se ejecutará en el 40,7 % de los días
  · a un precio que no controla

  Y EL PLAZO DEL INSTRUMENTO ES 4 AÑOS

  → EL ACCESO ES REAL; LA SALIDA, NO
```

**Paso 7 — propón el diseño corregido.**

```text
CORRECCIONES

  1 MÍNIMO DE 2 500
      por debajo, el coste unitario se come
      la prima por riesgo

  2 LÍMITE DE CONCENTRACIÓN
      máximo el 10 % del patrimonio financiero
      declarado, con advertencia si se acerca

  3 EVALUACIÓN DE IDONEIDAD QUE PUEDA
    DAR «NO»
      y publicar cuántos son excluidos:
      si es cero, el cuestionario no evalúa

  4 UNA PÁGINA DE DIVULGACIÓN
      con qué pasa si sale mal, cuándo puedo
      salir y cuánto cuesta en dinero

  5 DECLARAR LA LIQUIDEZ REAL
      «en los últimos seis meses hubo
      operaciones en 74 de 182 días»
      con el mismo tamaño de letra que
      el mínimo de entrada

CON LAS CINCO, EL PRODUCTO SIGUE SIENDO
ACCESIBLE Y DEJA DE SER UNA TRAMPA.
```

**Interpreta:** bajar el mínimo de 50 000 a 500 no democratizó el acceso: creó
un producto en el que **el inversionista pequeño asume riesgo de crédito
privado e iliquidez a cuatro años para rendir menos que un depósito**. El
importe de equilibrio era 2 250, y estaba a un cálculo de distancia.

## 🧭 Perspectivas

El fraccionamiento afecta a cada participante de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Acceso desde 500 | Si invierte sus ahorros |
| Inversionista | Un 9,2 % anunciado | Si mira la neta |
| Emisor | 12 000 inversionistas | Si asume el coste unitario |
| Plataforma | Comisión que no cubre el servicio | Si recorta servicio |
| Banco | Un competidor por el ahorro minorista | Qué ofrece |
| Custodio | Muchos titulares pequeños | Cómo escala |
| Supervisor | Idoneidad que nunca excluye | Qué exige |
| Auditor | Divulgación adaptada | Qué revisa |
| Sociedad | Ahorro minorista en crédito privado | Qué protección exige |

## 🏦 Del cliente al banco

El cliente accede a un instrumento que antes no podía comprar y puede quedar atrapado en él. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Rinde un 9,2 %» | Neta para él, un 3,3 % | 21, clase 7 |
| «Ahora puedo acceder» | Con 500 gana menos que en depósito | 21, clase 7 |
| «Puedo salir cuando quiera» | En el 40,7 % de los días | 21, clase 7 |

## ⚖️ Riesgos y controles

Los riesgos son de acceso sin salida y de rentabilidad neta negativa. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Coste unitario que anula la prima | El pequeño rinde menos que sin riesgo | Mínimo calculado, no elegido |
| Idoneidad que nunca excluye | El cuestionario es un trámite | Publicar la tasa de exclusión |
| Concentración excesiva | 500 es el 17 % de un ahorro pequeño | Límite sobre patrimonio declarado |
| Acceso sin salida | Se entra y no se sale | Declarar la liquidez real medida |
| Servicio recortado | La comisión no cubre el coste | Verificar de dónde sale |
| Folleto no leído | 180 páginas | Una página de divulgación adaptada |

## 🧪 Práctica

El laboratorio pide calcular el importe mínimo por debajo del cual el instrumento no rinde. Esa cifra es el mínimo defendible.

En [`labs/lab-05.md`](../labs/lab-05.md):

1. Calcula la rentabilidad neta por tamaño de inversión.
2. Halla el importe de equilibrio frente a una alternativa sin riesgo.
3. Mide quién absorbe el coste unitario del servicio.
4. Redacta la página de divulgación adaptada.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen inversores pequeños atrapados. La causa es haber bajado el importe sin resolver la salida.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Elegir el mínimo por marketing | «Desde 1» suena bien | Calcula el de equilibrio |
| Ignorar el coste unitario | No aparece en el folleto | Es la variable que decide |
| Cuestionario que nunca excluye | Reduce la colocación | Publica la tasa de exclusión |
| Confundir acceso con democratización | Suena bien | Sin salida no hay acceso |
| Folleto como única información | Cumple la norma | Añade la página adaptada |
| Suponer patrimonio del inversionista | No se pregunta | Límite de concentración declarado |

## ❓ Preguntas de comprobación

1. ¿Cuáles son las tres barreras y cuál toca el fraccionamiento?
2. ¿Por qué el coste unitario de servicio cambia la conclusión?
3. ¿Cómo se calcula el importe mínimo de equilibrio?
4. ¿Por qué la misma inversión puede ser prudente para uno y temeraria para
   otro?
5. ¿Qué cinco correcciones hacen accesible un producto sin convertirlo en una
   trampa?

## 📥 Entregable

Guarda en `portfolio/parte-21/clase-07/`:

- la rentabilidad neta calculada para tres tamaños de inversión;
- el importe de equilibrio con su alternativa de referencia;
- el análisis de quién absorbe el coste unitario;
- la página de divulgación adaptada, de una sola cara.

## 🔗 Referencias cruzadas

- **Viene de:** clases 3 y 6.
- **Continúa en:** clase 16 de esta parte.
- **Se aplica en:** Parte 22, clases 11 y 14; Parte 23, clase 8.

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

- IOSCO (2009). *Objectives and Principles of Securities Regulation*. IOSCO. Reglas de idoneidad y clasificación del inversionista. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD323.pdf>
- OCDE (2020). *Recommendation of the Council on Financial Literacy*. OECD. Evidencia sobre comprensión del producto por el inversionista minorista. <https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0461>
- IOSCO (2023). *Policy Recommendations for Crypto and Digital Asset Markets*. IOSCO. Riesgos de conducta del acceso fraccionado. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- Comisión para el Mercado Financiero. *Normativa sobre conducta de mercado e información al inversionista*. CMF. Obligaciones chilenas de información al inversionista. <https://www.cmfchile.cl/portal/principal/613/w3-channel.html>
- Verificación local: comprueba qué obligaciones de idoneidad y qué límites de comercialización a minoristas impone tu jurisdicción para este tipo de activo. Esta clase no constituye asesoría legal ni recomendación de inversión. **Fecha de verificación de esta clase: 2026-08-20.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 06 · Mercado secundario y liquidez prometida](06-mercado-secundario-y-liquidez-prometida.md) | [Parte 21](../README.md) · [Programa](../../../SYLLABUS.md) | [08 · Entrega contra pago atómica →](08-entrega-contra-pago-atomica.md) |
<!-- gen:footer:end -->
