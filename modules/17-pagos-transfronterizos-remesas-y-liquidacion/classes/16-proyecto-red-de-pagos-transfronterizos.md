<!-- meta
part: 18
class: 16
title: "Proyecto: red de pagos transfronterizos"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global, chile]
regulatory_topics: [cross-border-payments, aml-cft, cambios-internacionales]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [CPMI, FSB, Banco Central de Chile]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 16 · Proyecto: red de pagos transfronterizos

> [← 15 · Payment versus Payment y liquidación atómica](15-payment-versus-payment-y-liquidacion-atomica.md) · [Índice de la parte](../README.md) · [Proyecto de la parte →](../project/README.md)

**Parte 18 — Pagos transfronterizos, remesas y liquidación internacional** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Integrar las quince clases en una decisión de arquitectura defendible: qué ruta
usa cada corredor, por qué, con qué controles y con qué evidencia. El proyecto
se evalúa por lo que puedes **medir**, no por lo que propones.

Esta clase cierra la parte construyendo una red completa. No introduce mecanismo nuevo: obliga a elegir entre los quince anteriores con un criterio de enrutamiento escrito, y a medir el resultado agregado en vez de operación a operación.

## 📚 Objetivos

Al finalizar podrás:

1. **Construir** el motor de rutas con criterios explícitos y comparables.
2. **Medir** las quince métricas obligatorias de una red de pagos.
3. **Defender** cada elección de arquitectura frente a la alternativa descartada.
4. **Detectar** la atribución errónea de un ahorro a la tecnología.
5. **Evaluar** el proyecto de otra persona con la rúbrica.

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

Los cuatro primeros términos son el motor y sus métricas; los cuatro siguientes, el criterio de decisión y su registro. La **tasa de procesamiento directo** es la métrica que resume la calidad de una red: qué proporción de pagos llega sin intervención manual.

| Concepto | Comprensión verificable |
|---|---|
| `motor de rutas` | Componente que elige la ruta de cada pago con criterios explícitos |
| `métrica de red` | Medida del funcionamiento real, no del diseño |
| `tasa de procesamiento directo` | Proporción de pagos sin intervención manual |
| `coste total por corredor` | Comisiones más diferencial, sobre importe de referencia |
| `disponibilidad` | Proporción de tiempo en que la ruta funciona |
| `atribución del ahorro` | Identificar la causa real de una mejora |
| `criterio de enrutamiento` | Regla que decide entre rutas, escrita y verificable |
| `registro de decisiones` | Cada elección con su alternativa y su motivo |

## 🧠 Modelo mental

El modelo mental es una red de corredores con costes y plazos distintos, y un motor que elige ruta. Lo que se optimiza no es una operación sino el conjunto, y por eso el criterio de enrutamiento tiene que estar escrito.

```text
UNA RED DE PAGOS SE DEFIENDE CON TRES RESPUESTAS

  1. ¿POR QUÉ ESTA RUTA PARA ESTE CORREDOR?
     criterio explícito, no preferencia

  2. ¿CUÁNTO CUESTA Y CUÁNTO TARDA, MEDIDO?
     percentiles, no promedios

  3. ¿QUÉ PASA CUANDO FALLA?
     ruta alternativa probada, no documentada

LA PREGUNTA QUE DESMONTA UN MAL PROYECTO
  «este ahorro, ¿de dónde viene exactamente?»

  si la respuesta es «de la tecnología»,
  el proyecto no ha hecho el análisis
```

## 📖 Desarrollo

### 1. El motor de rutas

El motor de rutas es el corazón del proyecto y se define por sus entradas y
por el orden en que aplica los criterios. El bloque fija ambos: el orden
importa, porque el coste solo decide entre rutas que ya son admisibles.

```text
ENTRADA
  corredor, importe, moneda de origen y destino,
  urgencia, canal de entrega del beneficiario,
  perfil de cumplimiento

CRITERIOS, EN ORDEN
  1. ELEGIBILIDAD  ¿la ruta admite este pago?
       límites, monedas, canal, jurisdicción
  2. CUMPLIMIENTO  ¿la ruta soporta los controles exigidos?
  3. DISPONIBILIDAD ¿está operativa ahora?
  4. TIEMPO        ¿llega dentro del compromiso?
  5. COSTE         ¿cuál es el coste total?
  6. RIESGO        ¿qué exposición añade?

SALIDA
  ruta elegida, ruta alternativa, coste estimado,
  fecha y hora de disponibilidad, y EL MOTIVO

EL MOTIVO ES OBLIGATORIO
  un motor que elige sin explicar no se puede auditar
  ni corregir cuando se equivoca
```

### 2. Las quince métricas obligatorias

| # | Métrica | Unidad | Por qué |
|---:|---|---|---|
| 1 | Coste total | % del importe | El precio real |
| 2 | Comisión explícita | Importe | La parte visible |
| 3 | Diferencial de cambio | pb | La parte invisible |
| 4 | Tiempo de envío | Minutos | Lo que controla el emisor |
| 5 | Tiempo hasta acreditación | Horas | Lo que percibe el receptor |
| 6 | Tiempo hasta disponibilidad | Horas | Cuándo puede usarlo |
| 7 | Número de intermediarios | Recuento | Cadena y opacidad |
| 8 | Tasa de procesamiento directo | % | Calidad del dato |
| 9 | Reparaciones | % | Dónde falla el origen |
| 10 | Rechazos | % | Dónde falla el destino |
| 11 | Devoluciones | % | Qué se deshace |
| 12 | Liquidez prefinanciada | Importe | Coste inmovilizado |
| 13 | Cumplimiento del compromiso | % | Si la promesa se sostiene |
| 14 | Transparencia | Booleano por ruta | Si el coste es comparable |
| 15 | Disponibilidad de la ruta | % | Si se puede usar |

Tres de esas metricas no admiten promedio, y conviene fijar la regla de
presentación antes de empezar a medir.

```text
REGLA DE PRESENTACIÓN
  las métricas 4, 5 y 6 se reportan en percentiles
  p50, p95 y p99. Nunca en promedio.

  el promedio de un corredor con 71 % en 4 horas
  y 29 % en 18 horas no describe la experiencia
  de nadie
```

### 3. La atribución del ahorro

Decir que una ruta ahorra no basta: hay que decir de dónde sale el ahorro. El
bloque enumera las fuentes posibles, ninguna de las cuales es «la tecnología»,
y propone la prueba que valida la atribución.

```text
CUANDO UNA RUTA NUEVA AHORRA, HAY QUE DECIR DE DÓNDE

  FUENTES POSIBLES
    · menos intermediarios en la cadena
    · menos prefinanciación inmovilizada
    · ventana operativa más larga o continua
    · menor diferencial por más competencia
    · menos reparaciones por mejor dato
    · menor coste operativo por más automatización

  NINGUNA DE ESAS SEIS ES «LA TECNOLOGÍA»

LA PRUEBA
  si el ahorro viene de eliminar dos intermediarios,
  cualquier arquitectura que los elimine produce
  el mismo ahorro

  → entonces la decisión no es tecnológica:
    es sobre la topología de la red
```

### 4. Contingencia

Una ruta alternativa solo cuenta si se ha usado. El bloque fija qué se prueba
en un ensayo de conmutación y con qué frecuencia, retomando la regla que ya
apareció en la parte anterior.

```text
CADA CORREDOR NECESITA UNA RUTA ALTERNATIVA
Y UN PROCEDIMIENTO PROBADO

  ¿QUÉ SE PRUEBA?
    · conmutación con tráfico real, no simulado
    · tiempo hasta que la alternativa opera
    · coste de operar en la alternativa
    · límites de la alternativa

  UNA ALTERNATIVA NO ENSAYADA NO ES UNA ALTERNATIVA:
  es una intención (Parte 17, clase 13)

FRECUENCIA MÍNIMA DEL ENSAYO
  la que haga que nadie tenga que recordar
  cómo se hacía: trimestral es lo habitual
```

### 5. Lo que el proyecto debe declarar

El expediente se cierra declarando los límites del trabajo. El bloque los
enumera para que el panel evalúe lo que el proyecto sí demuestra, sin tener
que descubrir por su cuenta lo que queda fuera.

```text
LÍMITES LEGÍTIMOS DE ESTE PROYECTO
  · entorno simulado: no hay red de pagos real
  · datos sintéticos: no reflejan distribuciones reales
  · las cifras de coste y plazo son ilustrativas
  · los proyectos institucionales citados son pilotos
    o pruebas de concepto, no infraestructura operativa
  · la matriz normativa refleja una consulta con fecha
    y no sustituye asesoría legal
  · no se ha probado carga sostenida
```

## 🧮 Ejemplo guiado

El ejemplo enruta pagos por criterios distintos y compara el resultado agregado. El criterio de coste y el de plazo producen redes distintas.

**Situación.** Revisas el proyecto de otra persona. Extractos relevantes.

```text
EXTRACTO 1 · criterio de enrutamiento
  «se prioriza la ruta con stablecoin por ser
   más rápida y barata»

EXTRACTO 2 · métricas reportadas
  tiempo medio: 42 minutos
  coste medio: 1,4 %
  tasa de procesamiento directo: 94 %

EXTRACTO 3 · corredores cubiertos
  8 corredores, todos con la misma ruta

EXTRACTO 4 · contingencia
  «si la ruta principal falla, se usa la corresponsalía»

EXTRACTO 5 · cumplimiento
  screening en origen, con la lista actualizada a diario

EXTRACTO 6 · ahorro declarado
  «la tecnología reduce el coste un 78 %»
```

**Paso 1 — evalúa el extracto 1.**

```text
EL CRITERIO NO ES UN CRITERIO: ES UNA PREFERENCIA

  no dice
    · qué pasa si el corredor tiene enlace de pagos inmediatos
    · qué pasa si la salida local es ilíquida
    · qué límite de tenencia aplica
    · qué exposición por emisor admite

HALLAZGO 1 · criterio sin condiciones
  gravedad: alta
  un motor que siempre elige lo mismo no es un motor
```

**Paso 2 — evalúa las métricas.**

```text
TRES MÉTRICAS DE QUINCE, Y LAS TRES EN PROMEDIO

  faltan las doce restantes, y en particular
    · diferencial de cambio (la parte invisible del coste)
    · tiempo hasta DISPONIBILIDAD, no hasta acreditación
    · liquidez prefinanciada
    · disponibilidad de la ruta

HALLAZGO 2 · métricas insuficientes y en promedio
  gravedad: alta
  «coste medio 1,4 %» sin el diferencial desglosado
  no permite comprobar si el 1,4 % es el coste real
```

**Paso 3 — evalúa la cobertura.**

```text
OCHO CORREDORES, LA MISMA RUTA EN TODOS

  ¿alguno tiene enlace de pagos inmediatos?
  ¿alguno tiene salida ilíquida?
  ¿alguno tiene restricción normativa al canal?

  el proyecto no lo dice, lo que significa
  que no lo miró

HALLAZGO 3 · misma ruta sin analizar el corredor
  gravedad: alta
  contradice el criterio de la clase 14:
  la ruta con stablecoin es respuesta a la ausencia
  de infraestructura, no una preferencia
```

**Paso 4 — evalúa la contingencia.**

```text
«SI FALLA, SE USA LA CORRESPONSALÍA»

  ¿existe la relación de corresponsalía?
  ¿está probada la conmutación?
  ¿cuánto tarda? ¿cuánto cuesta operar así?
  ¿tiene los mismos límites?

HALLAZGO 4 · contingencia no ensayada
  gravedad: media
  una alternativa mencionada no es una alternativa
```

**Paso 5 — evalúa el cumplimiento.**

```text
SCREENING EN ORIGEN CON LISTA DIARIA: correcto pero incompleto

  falta
    · la regla del viaje en el tramo de activos virtuales
    · qué pasa si el proveedor de salida no la soporta
    · el procedimiento ante coincidencia
    · la medición de precisión y exhaustividad

HALLAZGO 5 · cumplimiento parcial en el tramo nuevo
  gravedad: alta
  es el punto donde la ruta nueva tiene más
  incertidumbre y es el que menos se documentó
```

**Paso 6 — evalúa la atribución del ahorro.**

```text
«LA TECNOLOGÍA REDUCE EL COSTE UN 78 %»

  DESCOMPOSICIÓN QUE EL PROYECTO NO HIZO
    ¿cuánto viene de eliminar intermediarios?
    ¿cuánto de no prefinanciar?
    ¿cuánto de un diferencial menor?
    ¿cuánto de operar en fin de semana?

  al pedirle el desglose al autor, resulta que:
    62 % del ahorro: eliminar dos intermediarios
    24 %: no prefinanciar el nostro
    11 %: menor diferencial por competencia en la salida
     3 %: coste de red frente a comisión de mensajería

  → el 3 % es lo atribuible al registro.
    El 97 % restante lo produciría cualquier
    arquitectura con la misma topología

HALLAZGO 6 · atribución errónea del ahorro
  gravedad: alta
  es el error que la Parte 14, clase 9 y la clase 14
  de esta parte advierten explícitamente
```

**Paso 7 — puntúa y devuelve.**

```text
Motor de rutas y criterios      25 %  →  8/25
Métricas y medición             20 %  →  6/20
Cumplimiento                    20 %  →  9/20
Arquitectura y contingencia     15 %  →  7/15
Análisis de coste y atribución  15 %  →  4/15
Límites declarados               5 %  →  2/5
TOTAL                                   36/100 → NO APRUEBA

DEVOLUCIÓN

  LO QUE ESTÁ BIEN
    · la ruta implementada funciona y está probada
    · el screening en origen está bien resuelto

  LO QUE HAY QUE CORREGIR, EN ORDEN
    1. escribir el criterio de enrutamiento con
       condiciones, y aplicarlo por corredor
    2. desglosar el ahorro por fuente y corregir
       la afirmación sobre la tecnología
    3. completar el cumplimiento del tramo nuevo
    4. reportar las quince métricas en percentiles
    5. ensayar la contingencia y medirla
    6. escribir la sección de límites

  OBSERVACIÓN DE CRITERIO
    el proyecto eligió una arquitectura y luego
    buscó los argumentos. El orden correcto es
    el inverso: medir el corredor, y que la
    arquitectura salga de la medición.
```

**Interpreta:** el software funcionaba y el proyecto suspendía. La diferencia
está en que **una red de pagos no se evalúa por la ruta que implementa, sino por
el criterio con que elige entre rutas** y por la honestidad con que atribuye sus
resultados.

## 🧭 Perspectivas

La red afecta a todos los participantes de las quince clases anteriores. La tabla los reúne.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un pago que llega o no llega | Si vuelve |
| Autor del proyecto | Una ruta que funciona | Si mide o si defiende |
| Revisor | Seis hallazgos | Qué puntúa |
| Tesorería | Liquidez de cada ruta | Cuánto prefinancia |
| Cumplimiento | Un tramo nuevo poco documentado | Si autoriza |
| Comité de riesgo | Exposición por emisor y contraparte | Qué límites impone |
| Supervisor | Actividad de cambio y de pagos | Qué exige verificar |

## 🏦 Del cliente al banco

El cliente quiere que su pago llegue barato y rápido y la red optimiza el conjunto. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Siempre me mandan por el mismo sitio» | Criterio sin condiciones | 18, clase 16 |
| «Un día tardó cinco veces más» | Se reportó el promedio | 18, clase 16 |
| «Falló y no había alternativa» | Contingencia no ensayada | 18, clase 16 |
| «Dijeron que era más barato» | Ahorro mal atribuido | 18, clases 14 y 16 |

## ⚖️ Riesgos y controles

Los riesgos del proyecto reúnen los de toda la parte. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Criterio sin condiciones | Siempre la misma ruta | Reglas con condiciones por corredor |
| Métrica en promedio | Se oculta la cola | Percentiles p50, p95, p99 |
| Ahorro mal atribuido | Se acredita a la tecnología | Desglose por fuente |
| Contingencia no probada | Falla cuando se necesita | Ensayo trimestral con evidencia |
| Cumplimiento parcial | El tramo nuevo sin controles | Cobertura completa antes de operar |
| Límites no declarados | Se lee como cobertura total | Sección obligatoria |

## 🧪 Práctica

El laboratorio es el proyecto completo. El registro de decisiones de enrutamiento es lo que se evalúa.

En el [proyecto de la parte](../project/README.md):

1. Construye el motor de rutas con sus seis criterios y su motivo.
2. Mide las quince métricas y repórtalas en percentiles.
3. Desglosa el ahorro de tu arquitectura por fuente.
4. Ensaya la contingencia de un corredor y documenta el resultado.

## ⚠️ Errores frecuentes

Los síntomas de la tabla aparecen al operar la red. Casi todos se evitan escribiendo el criterio de enrutamiento antes.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Elegir la arquitectura primero | Se decidió y luego se justificó | Mide el corredor primero |
| Tres métricas de quince | Se reportó lo favorable | Las quince, en percentiles |
| «La tecnología ahorra» | No se descompuso | Seis fuentes posibles |
| Contingencia mencionada | Se documentó, no se probó | Ensayo con tráfico real |
| Cumplimiento del tramo antiguo | Se copió el existente | El tramo nuevo tiene controles nuevos |
| Sin sección de límites | Se temió mostrar debilidad | Declarar fortalece |

## ❓ Preguntas de comprobación

1. ¿Cuáles son los seis criterios del motor de rutas y por qué el motivo es
   obligatorio?
2. ¿Por qué las métricas de tiempo se reportan en percentiles?
3. ¿Cuáles son las seis fuentes posibles de un ahorro, y cuál no está en la lista?
4. ¿Qué distingue una alternativa real de una intención?
5. En el ejemplo guiado, ¿qué porcentaje del ahorro era atribuible al registro?

## 📥 Entregable

Guarda en `portfolio/parte-18/clase-16/`:

- el motor de rutas con sus criterios, condiciones y motivos;
- las quince métricas medidas y reportadas en percentiles;
- el desglose del ahorro por fuente, con la conclusión;
- la revisión del proyecto de otra persona con su puntuación y devolución.

## 🔗 Referencias cruzadas

- **Viene de:** las quince clases anteriores de esta parte.
- **Continúa en:** Parte 19 (qué es realmente un registro distribuido) y
  Parte 20 (el activo con el que se liquida).
- **Se aplica en:** Parte 23, clases 8, 9 y 18.

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

- Financial Stability Board (2021). *Targets for Addressing the Four Challenges of Cross-border Payments*. FSB. Metas que el proyecto debe alcanzar y demostrar. <https://www.fsb.org/2021/10/targets-for-addressing-the-four-challenges-of-cross-border-payments-final-report/>
- Committee on Payments and Market Infrastructures (2020). *Enhancing cross-border payments: building blocks of a global roadmap*. BIS. Bloques constructivos con que se justifica la arquitectura. <https://www.bis.org/cpmi/publ/d193.htm>
- Committee on Payments and Market Infrastructures e IOSCO (2012). *Principles for Financial Market Infrastructures*. BIS. Requisitos de la infraestructura elegida para liquidar. <https://www.bis.org/cpmi/publ/d101.htm>
- Banco Mundial. *Remittance Prices Worldwide*. Datos de coste con que se mide el corredor del proyecto. <https://remittanceprices.worldbank.org/>
- Banco Central de Chile. *Compendio de Normas de Cambios Internacionales*. Obligaciones cambiarias del corredor chileno del proyecto. <https://www.bcentral.cl/>
- Verificación local: comprueba qué operaciones deben informarse, qué autorizaciones exige tu jurisdicción para cada ruta y qué obligaciones de transparencia aplican. **Fecha de verificación de esta clase: 2026-08-06.** Este material no constituye asesoría legal.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 15 · Payment versus Payment y liquidación atómica](15-payment-versus-payment-y-liquidacion-atomica.md) | [Parte 18](../README.md) · [Programa](../../../SYLLABUS.md) | [Proyecto de la parte →](../project/README.md) |
<!-- gen:footer:end -->
