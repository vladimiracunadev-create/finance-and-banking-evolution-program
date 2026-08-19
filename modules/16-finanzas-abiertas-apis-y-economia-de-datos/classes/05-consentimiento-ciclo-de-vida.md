<!-- meta
part: 17
class: 5
title: "Consentimiento: creación, vigencia, renovación y revocación"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global, chile, union-europea]
regulatory_topics: [open-finance, consentimiento, proteccion-de-datos]
regulation_last_verified: 2026-08-19
regulatory_status: vigente
primary_authorities: [CMF]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 05 · Consentimiento: creación, vigencia, renovación y revocación

> [← 04 · Clasificación, calidad y gobierno de datos financieros](04-clasificacion-calidad-y-gobierno-de-datos.md) · [Índice de la parte](../README.md) · [06 · OAuth, OpenID Connect y autorización financiera →](06-oauth-openid-connect-y-autorizacion.md)

**Parte 17 — Finanzas abiertas, APIs y economía de datos** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Diseñar el ciclo de vida completo de un consentimiento y demostrar que funciona.
Esta es la clase central de la parte: **todo lo demás es la maquinaria que hace
cumplir lo que el cliente autorizó**.

La clase anterior clasificó los datos. Esta desarrolla el permiso que los libera, que es la pieza central de todo el régimen. Y lo trata como lo que es: un objeto con ciclo de vida, no una casilla que se marca una vez.

## 📚 Objetivos

Al finalizar podrás:

1. **Diseñar** alcances por finalidad, con el criterio de dato mínimo.
2. **Modelar** el ciclo de vida como una máquina de estados sin retrocesos.
3. **Especificar** la evidencia que permite reconstruir la decisión del cliente
   meses después.
4. **Implementar** una revocación con efecto verificable e inmediato.
5. **Evaluar** la fatiga de consentimiento y su efecto sobre la validez del acto.

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

Los cinco primeros términos son el ciclo de vida del consentimiento; los tres siguientes, su evidencia y sus patologías. La **fatiga de consentimiento** es el problema de diseño que arruina el régimen desde dentro: si se pide permiso demasiadas veces, el titular acepta sin leer y el consentimiento deja de informar.

| Concepto | Comprensión verificable |
|---|---|
| `alcance` | Unidad mínima de autorización, ligada a una finalidad |
| `finalidad` | Para qué se usará el dato; determina el alcance, no al revés |
| `vigencia` | Plazo durante el cual el consentimiento produce efectos |
| `renovación` | Acto expreso que crea un consentimiento nuevo |
| `revocación` | Acto del cliente que termina el consentimiento |
| `evidencia` | Registro que reconstruye qué autorizó el cliente y con qué texto |
| `fatiga de consentimiento` | Aceptación mecánica por exceso de solicitudes |
| `consentimiento de un solo uso` | Autorización ligada a una operación concreta |

## 🧠 Modelo mental

El modelo mental es un permiso con cuatro dimensiones: qué datos, para qué finalidad, durante cuánto tiempo y con qué posibilidad de retirarlo. Un consentimiento que no acota las cuatro no es un consentimiento, es una autorización general.

```text
UN CONSENTIMIENTO ES UN CONTRATO CON CUATRO COORDENADAS

  QUIÉN     el proveedor concreto, identificado
  QUÉ       los alcances, uno por finalidad
  PARA QUÉ  la finalidad declarada, verificable
  HASTA     la fecha de expiración, absoluta

SI FALTA UNA COORDENADA, EL CONSENTIMIENTO NO ES OPONIBLE
  sin QUIÉN     no se sabe a quién autorizó
  sin QUÉ       autoriza todo
  sin PARA QUÉ  no hay límite de uso
  sin HASTA     es perpetuo, y ningún cliente quiso eso

Y UNA QUINTA, QUE NO ES DEL CONSENTIMIENTO SINO DE SU PRUEBA
  CON QUÉ TEXTO  la versión exacta que el cliente leyó
```

## 📖 Desarrollo

### 1. La finalidad manda sobre el alcance

El orden en que se piensan finalidad y alcance decide si el consentimiento es
real o decorativo. El bloque contrapone la secuencia correcta con la que se ve
en la práctica, y ofrece una pregunta que revela cuál de las dos se siguió.

```text
ORDEN CORRECTO
  finalidad declarada
    → dato mínimo necesario para esa finalidad
      → alcance que da acceso exactamente a ese dato

ORDEN INCORRECTO (y frecuente)
  catálogo de alcances de la API
    → pedimos los que suenan útiles
      → luego inventamos la finalidad que los justifica

CÓMO SE DETECTA EL ORDEN INCORRECTO
  pregunta: «si el cliente rechaza este alcance,
  ¿qué función concreta deja de funcionar?»
  si la respuesta es «ninguna, pero nos vendría bien»,
  el alcance sobra
```

### 2. Granularidad: ni un solo alcance ni cuarenta

| Diseño | Efecto en el cliente | Efecto en el producto |
|---|---|---|
| Un alcance para todo | No puede aceptar una parte | Máxima conversión, mínima confianza |
| Un alcance por finalidad | Elige qué habilita | Equilibrio |
| Un alcance por campo | Fatiga y abandono | Conversión nula |

Entre los dos extremos hay un criterio para acertar, y no es el modelo de
datos de la API.

```text
LA GRANULARIDAD CORRECTA ES LA DEL PRODUCTO,
NO LA DEL MODELO DE DATOS

  «ver tus cuentas» y «ver tus movimientos»
  son dos funciones que el cliente entiende → dos alcances

  «leer la tabla de cuentas» y «leer la tabla de titulares»
  son dos tablas → un solo alcance
```

### 3. La máquina de estados

Un consentimiento no es un interruptor: es un objeto con estados y con
transiciones permitidas. El diagrama las fija, y las reglas de abajo explican
por qué ninguna flecha vuelve hacia atrás.

```text
borrador ──autoriza──► vigente ──┬── revoca ────► revocado
   │                             ├── expira ────► expirado
   └── rechaza ──► rechazado     └── cesa ──────► terminado

REGLAS
  · ningún estado vuelve a «vigente»
  · la renovación NO reactiva: crea un consentimiento NUEVO
  · todos los estados finales conservan su evidencia
  · el histórico no se borra: se archiva
```

```text
POR QUÉ LA RENOVACIÓN CREA UNO NUEVO
  si se «extiende» el existente, se pierde la prueba
  de qué autorizó el cliente en cada periodo:
  el texto pudo cambiar, los alcances pudieron cambiar,
  y la evidencia quedaría sobrescrita
```

### 4. La evidencia

Meses después, un reclamo obliga a reconstruir qué aceptó el cliente y en qué
condiciones. Solo se puede reconstruir lo que se guardó, así que el bloque
fija el mínimo y explica por qué dos de esos campos van separados.

```text
MÍNIMO PARA RECONSTRUIR LA DECISIÓN
  1. identificador del proveedor solicitante
  2. alcances PRESENTADOS y alcances CONCEDIDOS, por separado
  3. versión del texto mostrado al cliente
  4. método de autenticación empleado
  5. marca temporal con zona horaria
  6. canal e identificador de sesión
  7. finalidad declarada, en el mismo texto que vio el cliente

POR QUÉ «PRESENTADOS» Y «CONCEDIDOS» VAN SEPARADOS
  si solo se guarda «concedidos», no se puede detectar
  que el sistema concedió un alcance que nunca se mostró
```

### 5. La revocación es el examen del sistema

La revocación es donde se comprueba si el consentimiento era de verdad
reversible. El bloque describe las cuatro acciones que la componen, insiste en
su orden y termina con la medida que hay que publicar para demostrar que
funciona.

```text
UNA REVOCACIÓN CORRECTA HACE CUATRO COSAS, EN ESTE ORDEN

  1. cambia el estado del consentimiento
  2. invalida los tokens vivos asociados
  3. invalida la caché de estado
  4. responde al cliente

SI EL PASO 4 OCURRE ANTES QUE EL 3,
existe una ventana en la que el panel dice «revocado»
y la API sigue autorizando

MEDIDA QUE HAY QUE PUBLICAR
  retardo entre la revocación y el primer rechazo efectivo,
  en percentiles p50, p95 y p99
```

### 6. Fatiga de consentimiento

Un consentimiento que el cliente firma sin leer sigue siendo válido en el
papel y ha dejado de proteger a nadie. El bloque nombra el problema, propone
señales que lo detectan con datos propios y apunta la única solución que
funciona.

```text
EL PROBLEMA
  si al cliente se le piden 6 consentimientos al mes,
  deja de leer. El acto sigue existiendo jurídicamente
  y deja de existir materialmente.

SEÑALES MEDIBLES DE FATIGA
  · tiempo medio en la pantalla de consentimiento < 4 s
  · tasa de aceptación de TODOS los alcances > 97 %
  · tasa de lectura del detalle < 3 %
  · revocaciones concentradas en los 7 días siguientes

QUÉ HACER
  · reducir el número de solicitudes, no mejorar el texto
  · agrupar por finalidad y pedir una vez
  · pedir el alcance adicional CUANDO se necesita,
    no por adelantado
```

## 🧮 Ejemplo guiado

El ejemplo construye un consentimiento completo con sus cuatro dimensiones y su evidencia. Conviene comparar con uno en bloque: el primero es más trabajo y es el único que resiste una revisión.

**Situación.** Un producto de categorización de gastos mide su embudo de
consentimiento y sus revocaciones durante un trimestre.

```text
EMBUDO
  clientes que inician el flujo            140 000
  llegan a la pantalla de alcances         126 400
  aceptan todos los alcances               121 100
  aceptan parcialmente                       1 900
  rechazan                                   3 400

TIEMPO EN LA PANTALLA (mediana)                3,1 s
ABREN EL DETALLE DE ALCANCES                   2,4 %

REVOCACIONES EN 90 DÍAS                       19 800
  en los primeros 7 días                      12 500
  entre el día 8 y el 90                       7 300

ALCANCES SOLICITADOS: 5
ALCANCES QUE EL PRODUCTO USA REALMENTE: 3
```

**Paso 1 — calcula el embudo.**

```text
CONVERSIÓN GLOBAL
  121 100 + 1 900 = 123 000 consentimientos otorgados
  123 000 / 140 000 = 87,9 %

ACEPTACIÓN TOTAL SOBRE QUIENES DECIDEN
  121 100 / 126 400 = 95,8 %
```

**Paso 2 — contrasta con las señales de fatiga.**

```text
mediana de 3,1 s en la pantalla        < 4 s     → señal
aceptación total del 95,8 %            ≈ umbral  → señal
apertura del detalle del 2,4 %         < 3 %     → señal
revocaciones en 7 días: 12 500 / 19 800 = 63 %   → señal

CUATRO DE CUATRO
  el consentimiento se está otorgando sin leerse
```

**Paso 3 — cuantifica la revocación temprana.**

```text
12 500 / 123 000 = 10,2 % revoca en la primera semana

INTERPRETACIÓN
  no es que el producto decepcione en una semana:
  es que el cliente descubre DESPUÉS lo que aceptó ANTES

  el consentimiento fue formalmente válido
  y materialmente no informado
```

**Paso 4 — analiza los alcances sobrantes.**

```text
SE PIDEN 5, SE USAN 3

ALCANCES NO USADOS
  · «ver tus productos de inversión»     → no hay función que los use
  · «ver tus seguros»                    → previsto para 2027

COSTE DE PEDIRLOS
  · alarga la pantalla → menos lectura → más fatiga
  · amplía la superficie de riesgo sin contrapartida
  · si hay una brecha, se expuso dato que no se necesitaba
  · incumple minimización

BENEFICIO DE PEDIRLOS
  «evitar volver a pedirlo en 2027»
```

**Paso 5 — evalúa esa compensación con números.**

```text
COSTE DE VOLVER A PEDIR EN 2027
  supuesto: 60 % de los clientes acepta el alcance nuevo
  cuando se pide en el momento en que aporta valor

COSTE DE PEDIRLO AHORA
  2 alcances de 5 = 40 % de la pantalla
  dedicados a funciones inexistentes

  y el riesgo real: si el 10,2 % revoca en 7 días,
  parte de esa revocación se explica por la sorpresa
  de haber concedido acceso a productos que
  no tienen nada que ver con «categorizar gastos»

ESTIMACIÓN DEL EFECTO
  si eliminar los 2 alcances reduce la revocación temprana
  del 10,2 % al 6 %:
    123 000 × 4,2 % = 5 166 clientes retenidos por trimestre
```

**Paso 6 — decide.**

```text
DECISIÓN

  1. reducir de 5 alcances a 3
  2. pedir los otros dos CUANDO exista la función,
     en el momento en que aporten valor
  3. rediseñar la pantalla: una línea por finalidad,
     en la consecuencia para el cliente
  4. medir de nuevo las cuatro señales de fatiga a 60 días

CONDICIÓN DE ÉXITO
  · apertura del detalle > 8 %
  · revocación en 7 días < 6 %
  · conversión global no cae más de 2 puntos

Y SI LA CONVERSIÓN CAE MÁS DE 2 PUNTOS
  no se revierte automáticamente: se investiga si cayó
  porque el cliente ahora ENTIENDE lo que concede.
  Una conversión menor con consentimiento informado
  es un resultado mejor, no peor.
```

**Interpreta:** el embudo decía 87,9 % de conversión, que parece excelente. Las
cuatro señales de fatiga decían que ese 87,9 % no era una decisión. La métrica
de producto y la validez del acto apuntaban en direcciones opuestas.

## 🧭 Perspectivas

El consentimiento significa cosas distintas para cada actor de la cadena. La tabla las recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Una pantalla con cinco líneas | Si lee o si acepta |
| Fintech | Conversión del 87,9 % | Si optimiza o si informa |
| Banco | Consentimientos que debe honrar | Cómo verifica su vigencia |
| Supervisor | Revocación temprana del 10,2 % | Si investiga la calidad del acto |
| Auditor | Evidencia con versión de texto | Si la decisión es reconstruible |
| Oficial de privacidad | 2 alcances sin finalidad | Si autoriza |
| Sociedad | Consentimiento como formalidad | Presión por diseño honesto |

## 🏦 Del cliente al banco

El cliente dice que autorizó algo y el banco tiene que poder demostrar exactamente qué. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Acepté sin leer» | Fatiga: cuatro señales medibles | 17, clase 5 |
| «No sabía que veían mis inversiones» | Alcance sin finalidad | 17, clase 5 |
| «Revoqué y sigue apareciendo» | Caché o token no invalidado | 17, clase 5 |
| «Me lo volvieron a pedir» | Renovación crea un consentimiento nuevo | 17, clase 5 |

## ⚖️ Riesgos y controles

Los riesgos del consentimiento son de diseño y de evidencia. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Alcance sin finalidad | Se pide lo que no se usa | Regla: si se rechaza, ¿qué deja de funcionar? |
| Consentimiento no informado | Aceptación en 3 s sin abrir detalle | Medir fatiga y reducir solicitudes |
| Revocación con retardo | Acceso posterior a la revocación | Invalidar antes de responder |
| Evidencia incompleta | No se puede probar qué vio el cliente | Versión del texto en el registro |
| Renovación silenciosa | Se extiende sin acto del cliente | Nuevo consentimiento, nuevo registro |
| Alcance concedido no presentado | Escalada por defecto del sistema | Guardar presentados y concedidos |

## 🧪 Práctica

En [`labs/lab-01.md`](../labs/lab-01.md) y [`labs/lab-05.md`](../labs/lab-05.md):

1. Diseña los alcances de tu producto aplicando la regla del rechazo.
2. Implementa la máquina de estados y prueba cada transición ilegal.
3. Mide el retardo de revocación en p50, p95 y p99.
4. Calcula las cuatro señales de fatiga sobre los datos del ejercicio.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen consentimientos que no sirven. Las causas son alcances demasiado amplios y evidencia que no reconstruye la decisión.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Alcances copiados del catálogo | Se partió de la API, no de la finalidad | Empieza por el dato mínimo |
| Un solo alcance para todo | Se optimizó la conversión | Uno por finalidad |
| Revocar solo cambia el estado | No se invalidaron tokens | Invalida antes de responder |
| Evidencia sin versión de texto | Se guardó el resultado, no el acto | Añade `notice_version` |
| Renovación automática | Se confundió con prórroga técnica | Acto expreso del cliente |
| Optimizar la pantalla para aceptar | Se midió conversión, no comprensión | Mide fatiga |

## ❓ Preguntas de comprobación

1. ¿Qué pregunta permite detectar un alcance que sobra, y por qué funciona?
2. ¿Por qué la renovación debe crear un consentimiento nuevo en lugar de extender
   el existente?
3. ¿Por qué la caché debe invalidarse antes de responder al cliente que revocó?
4. ¿Cuáles son las cuatro señales medibles de fatiga de consentimiento?
5. En el ejemplo guiado, ¿por qué una caída de conversión podría ser un buen
   resultado?

## 📥 Entregable

Guarda en `portfolio/parte-17/clase-05/`:

- la tabla de alcances de tu producto, con la regla del rechazo aplicada;
- el diagrama de la máquina de estados y la lista de transiciones ilegales;
- la especificación de la evidencia, con los siete elementos;
- las cuatro señales de fatiga calculadas y tu decisión sobre ellas.

## 🔗 Referencias cruzadas

- **Viene de:** clases 1, 3 y 4; Parte 3, clase 11 (protección del consumidor).
- **Continúa en:** clase 6 (autorización), clase 11 (responsabilidad), clase 12
  (privacidad y portabilidad).
- **Se aplica en:** Parte 21, clase 11 (identidad y restricciones); Parte 23,
  clase 6 (consentimiento del banco digital).

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

- Comisión para el Mercado Financiero. *Normativa del Sistema de Finanzas Abiertas: consentimiento, vigencia y revocación*. CMF. Reglas de vigencia, renovación y revocación del consentimiento. <https://www.cmfchile.cl/>
- European Data Protection Board (2020). *Guidelines 05/2020 on consent under Regulation 2016/679*. EDPB. Requisitos de validez del consentimiento en protección de datos. <https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-052020-consent-under-regulation-2016679_en>
- OpenID Foundation. *FAPI 2.0 — Grant Management for OAuth 2.0*. Mecanismo técnico de gestión y revocación de autorizaciones. <https://openid.net/wg/fapi/>
- Bank for International Settlements (2021). *Data governance and consent in open finance*. BIS. Gobierno del consentimiento en un ecosistema de finanzas abiertas. <https://www.bis.org/publ/bppdf/bispap117.htm>
- Biblioteca del Congreso Nacional de Chile. *Ley N.º 19.628 sobre protección de la vida privada y su normativa sucesora en materia de datos personales*. Régimen chileno de datos personales aplicable al consentimiento. <https://www.bcn.cl/leychile>
- Verificación local: comprueba el plazo máximo de vigencia y los requisitos de revocación exigidos por la norma vigente en tu jurisdicción. **Fecha de verificación de esta clase: 2026-08-19.** Esta clase no constituye asesoría legal.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 04 · Clasificación, calidad y gobierno de datos financieros](04-clasificacion-calidad-y-gobierno-de-datos.md) | [Parte 17](../README.md) · [Programa](../../../SYLLABUS.md) | [06 · OAuth, OpenID Connect y autorización financiera →](06-oauth-openid-connect-y-autorizacion.md) |
<!-- gen:footer:end -->
