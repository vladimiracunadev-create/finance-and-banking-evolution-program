<!-- meta
part: 17
class: 8
title: "Diseño, versionado e idempotencia"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global]
regulatory_topics: [open-finance, contratos-de-api]
regulation_last_verified: 2026-08-20
regulatory_status: estandar-vigente
primary_authorities: [OpenID Foundation]
requires_legal_review: false
-->

<!-- gen:header:start -->
# Clase 08 · Diseño, versionado e idempotencia

> [← 07 · Financial-grade APIs, certificados y firma de mensajes](07-financial-grade-apis-y-firma.md) · [Índice de la parte](../README.md) · [09 · APIs de cuentas, productos, créditos, seguros e inversiones →](09-apis-de-informacion-financiera.md)

**Parte 17 — Finanzas abiertas, APIs y economía de datos** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Diseñar una API que un tercero pueda programar sin preguntar y que puedas cambiar
sin romperlo. Las tres decisiones que lo determinan son el contrato, la política
de versiones y la idempotencia.

Las dos clases anteriores aseguran el canal. Esta se ocupa de que el contrato entre los dos sistemas siga funcionando cuando uno de ellos cambie, y de que un reintento por un error de red no produzca dos pagos.

## 📚 Objetivos

Al finalizar podrás:

1. **Escribir** un contrato OpenAPI que sirva como especificación y como fuente de
   pruebas.
2. **Distinguir** cambio compatible de cambio incompatible con una regla operativa.
3. **Implementar** idempotencia correcta, incluidos los tres detalles que la mayoría
   omite.
4. **Diseñar** paginación y límite de tasa que no se rompan bajo concurrencia.
5. **Definir** un catálogo de errores que permita a la otra parte programar
   decisiones, no adivinanzas.

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

Los tres primeros términos son el contrato y su evolución; los cinco siguientes, los mecanismos que hacen fiable una API. La **idempotencia** es el que evita el problema más caro: un pago reintentado por un error de red no se puede ejecutar dos veces, y eso exige diseño y no buena voluntad.

| Concepto | Comprensión verificable |
|---|---|
| `contrato` | Especificación formal que ambas partes tratan como fuente de verdad |
| `cambio compatible` | El cliente existente sigue funcionando sin tocar código |
| `versionado` | Mecanismo para introducir cambios incompatibles sin romper a nadie |
| `idempotencia` | Repetir la petición no repite el efecto |
| `paginación por cursor` | Recorrido estable sobre datos que cambian |
| `límite de tasa` | Techo de peticiones por unidad de tiempo y por sujeto |
| `catálogo de errores` | Conjunto cerrado de errores con semántica documentada |
| `depreciación` | Retirada anunciada de una versión, con fecha |

## 🧠 Modelo mental

El modelo mental es un contrato entre dos sistemas que evolucionan a ritmos distintos. El consumidor no se actualiza cuando el proveedor quiere, y por eso todo cambio tiene que ser compatible o tener versión propia y calendario de retirada.

```text
UNA API ES UNA PROMESA QUE OTRO PROGRAMA EN SU CÓDIGO

  cada campo que expones, alguien lo lee
  cada error que devuelves, alguien lo trata
  cada orden que garantizas, alguien lo asume

  CAMBIAR CUALQUIERA DE LOS TRES SIN AVISO
  ES ROMPER CÓDIGO AJENO EN PRODUCCIÓN

LA REGLA OPERATIVA DE COMPATIBILIDAD
  ¿un cliente escrito contra la versión anterior,
  sin tocar una línea, sigue funcionando?
    SÍ  → compatible: no cambia la versión
    NO  → incompatible: versión nueva y periodo de coexistencia
```

## 📖 Desarrollo

### 1. Cambios compatibles e incompatibles

| Cambio | ¿Compatible? | Por qué |
|---|---|---|
| Añadir un campo opcional en la respuesta | Sí | El cliente lo ignora |
| Añadir un endpoint | Sí | Nadie lo llamaba |
| Añadir un valor a un enumerado de respuesta | **No** | El cliente no lo trata |
| Añadir un parámetro opcional en la petición | Sí | Tiene valor por defecto |
| Hacer obligatorio un parámetro opcional | No | Rompe a quien no lo enviaba |
| Renombrar un campo | No | Rompe a todos |
| Cambiar el tipo de un campo | No | Rompe el análisis sintáctico |
| Reducir el rango de un campo | No | Rompe casos válidos |
| Añadir un error nuevo | **No** | El cliente no lo trata |

Dos filas de la tabla se clasifican mal casi siempre, y conviene detenerse en
ellas.

```text
LAS DOS FILAS MARCADAS SON LAS QUE MÁS SE EQUIVOCAN

  «añadir un valor al enumerado es aditivo»
  → sí, en el esquema. No, en el código del cliente,
    que tiene un switch con los valores que conocía

  → por eso los enumerados de respuesta se diseñan
    con una cláusula por defecto documentada desde el día 1:
    «trata cualquier valor desconocido como OTHER»
```

### 2. Estrategia de versión

Hay tres sitios donde se puede declarar la versión de una API, y la elección
tiene consecuencias operativas más que estéticas. El bloque los compara y
justifica la recomendación con los cuatro lugares donde se diagnostica un
incidente.

```text
TRES OPCIONES

  EN LA RUTA        /v1/accounts        visible, cacheable, simple
  EN LA CABECERA    Accept: ...;v=1     limpia, invisible en el registro
  POR CONTENIDO     media types propios  precisa, poco usada

RECOMENDACIÓN PARA FINANZAS ABIERTAS: EN LA RUTA
  motivo: el registro de acceso, el límite de tasa,
  el enrutamiento y el soporte trabajan sobre la URL.
  Una versión invisible en la URL es invisible en los
  cuatro sitios donde se diagnostica un incidente.

VERSIONA LA API, NO CADA RECURSO
  /v1/accounts y /v2/payments a la vez es un mapa mental
  que ningún integrador mantiene
```

### 3. Depreciación con fecha

Apagar una versión de golpe rompe integraciones ajenas que nadie avisó. El
bloque describe la retirada como un calendario con tres hitos y cabeceras que
lo anuncian en cada respuesta, de modo que el integrador se entere sin leer un
correo.

```text
UNA VERSIÓN NO SE APAGA: SE DEPRECIA

  T0  se publica v2 y se anuncia la depreciación de v1
      cabecera en cada respuesta de v1:
        Deprecation: true
        Sunset: Sat, 30 Jan 2027 00:00:00 GMT
        Link: <https://…/migracion-v2>; rel="deprecation"
  T1  se avisa a los integradores que siguen en v1,
      con su volumen y su nombre
  T2  v1 responde 410 Gone

  T2 − T0 ≥ 6 meses en un ecosistema regulado

SIN FECHA EN LA CABECERA
  el integrador se entera el día que deja de funcionar
```

### 4. Idempotencia: los tres detalles que se omiten

La idempotencia se explica en una frase y se implementa mal casi siempre,
porque tres detalles se dan por supuestos. El bloque los desarrolla; el
segundo es el que falla justo en el escenario para el que existe el
mecanismo.

```text
1 · CANONICALIZAR EL CUERPO ANTES DE LA HUELLA
    {"a":1,"b":2} y {"b":2,"a":1} son el mismo cuerpo.
    Sin canonicalizar, un reintento legítimo da 409.

2 · BLOQUEO POR CLAVE
    dos reintentos simultáneos entran a la vez
    y ambos ven «clave no vista». Sin bloqueo,
    la idempotencia falla exactamente en el caso
    para el que existe.

3 · GUARDAR LA RESPUESTA, NO SOLO EL IDENTIFICADOR
    el cliente que reintenta necesita el mismo cuerpo,
    con el mismo estado y las mismas cabeceras.

Y UNO MÁS, DE OPERACIÓN
4 · VENTANA DE RETENCIÓN DECLARADA
    ¿cuánto tiempo se recuerda una clave? 24 h es habitual.
    Pasada la ventana, la misma clave crea una operación nueva:
    hay que decirlo en la documentación.
```

### 5. Paginación estable

Paginar sobre datos que siguen llegando es distinto de paginar sobre una lista
quieta. El bloque muestra qué le ocurre a la paginación por desplazamiento
cuando entran filas nuevas y qué condición hace fiable al cursor.

```text
DESPLAZAMIENTO (offset)
  página 1: filas 1-100
  llegan 3 filas nuevas al principio
  página 2: filas 101-200  →  las filas 98,99,100 se repiten
                              y tres se pierden

CURSOR
  cursor = posición exacta en un orden TOTAL
  orden total = (fecha DESC, id DESC)

  el desempate por id es lo que hace la posición inequívoca.
  Sin desempate, el cursor tiene el mismo defecto que el offset
  cuando hay empates de fecha.

REGLA
  el cursor se devuelve OPACO. Si el cliente lo interpreta,
  no puedes cambiar su formato nunca más.
```

### 6. Límite de tasa que informa

Limitar la tasa es necesario; limitarla en silencio empeora la saturación que
pretendía evitar. El bloque muestra la respuesta que permite al llamante
reaccionar bien y las dimensiones sobre las que conviene contar.

```text
UN LÍMITE SIN INFORMACIÓN ES UNA DENEGACIÓN DE SERVICIO MUTUA

  RESPUESTA CORRECTA AL 429
    Retry-After: 37
    X-RateLimit-Limit: 300
    X-RateLimit-Remaining: 0
    X-RateLimit-Reset: 1786000000

  SIN Retry-After
    el cliente reintenta de inmediato, agrava la saturación
    y ambos extremos gastan capacidad sin resultado

DIMENSIONES DEL LÍMITE
  por cliente (entidad), por consentimiento y por cuenta.
  Solo el primero deja que un tercero grande consuma
  toda la capacidad con un solo cliente afectado.
```

## 🧮 Ejemplo guiado

El ejemplo implementa una operación idempotente con huella canónica. Conviene reintentar la misma petición: el resultado tiene que ser idéntico y no producir un segundo movimiento.

**Situación.** La API v1 lleva 14 meses en producción con 180 integradores. Hay
que introducir cuatro cambios.

```text
CAMBIO 1  añadir el campo «saldo al inicio de la ventana»
CAMBIO 2  añadir el estado «EN_INVESTIGACION» a los pagos
CAMBIO 3  cambiar «amount» de número a cadena decimal
CAMBIO 4  hacer obligatorio el parámetro «from» en movimientos
```

**Paso 1 — clasifica cada cambio.**

```text
CAMBIO 1  campo nuevo en la respuesta            → COMPATIBLE
CAMBIO 2  valor nuevo en un enumerado            → INCOMPATIBLE
CAMBIO 3  cambio de tipo                          → INCOMPATIBLE
CAMBIO 4  opcional pasa a obligatorio             → INCOMPATIBLE
```

**Paso 2 — evalúa el impacto del cambio 2.**

```text
¿CUÁNTOS INTEGRADORES SE ROMPEN?

  depende de cómo trataron el enumerado:
    · con cláusula por defecto  → no se rompen
    · con switch exhaustivo     → excepción no controlada

  ENCUESTA A LOS 180 INTEGRADORES: responden 96
    con cláusula por defecto:  41
    con switch exhaustivo:     38
    no lo saben:               17

  ESTIMACIÓN
    38 / 96 = 39,6 % de los que responden
    proyectado a 180: ≈ 71 integradores en riesgo
```

**Paso 3 — decide si el cambio 2 justifica una versión nueva.**

```text
OPCIÓN A · v2 solo por este cambio
  coste: migración de 180 integradores
  beneficio: nadie se rompe

OPCIÓN B · introducirlo en v1 con aviso previo
  coste: ~71 integradores con incidente
  beneficio: sin migración

OPCIÓN C · introducirlo en v1 tras un periodo de preparación
  1. publicar hoy la regla «trata desconocidos como OTHER»
  2. exponer el estado nuevo en el entorno de pruebas
  3. dar 90 días y medir en pruebas quién falla
  4. contactar uno a uno a los que fallan
  5. activar en producción

  coste: 90 días y trabajo de coordinación
  beneficio: sin migración y sin incidente
```

**Paso 4 — agrupa los cambios incompatibles.**

```text
LOS CAMBIOS 3 Y 4 NO ADMITEN LA OPCIÓN C
  un cambio de tipo rompe el análisis sintáctico:
  no hay cláusula por defecto que lo salve

  hacer obligatorio un parámetro rompe la petición:
  el cliente ni siquiera llega a leer la respuesta

DECISIÓN DE AGRUPACIÓN
  v2 contiene los cambios 3 y 4
  v1 recibe el cambio 1 (compatible)
     y el cambio 2 por la vía de la opción C
```

**Paso 5 — calcula el calendario.**

```text
CAMBIO 1 (compatible)        despliegue inmediato en v1

CAMBIO 2 (opción C)
  T0  publicación de la regla y del estado en pruebas
  T0 + 90 d   activación en producción de v1

CAMBIOS 3 y 4 (v2)
  T0      publicación de v2 y aviso de depreciación de v1
  T0 + 6 meses   recordatorio con volumen por integrador
  T0 + 9 meses   v1 responde 410

  ¿POR QUÉ 9 Y NO 6?
    porque 71 integradores ya están gestionando el cambio 2
    en la misma ventana; solapar dos migraciones
    multiplica los incidentes
```

**Paso 6 — mide durante la transición.**

```text
CUADRO DE MANDO DE LA MIGRACIÓN

  · llamadas a v1 y a v2, por integrador y por día
  · integradores con 0 llamadas a v2 a los 3, 6 y 8 meses
  · errores 4xx en v2 por integrador (síntoma de migración parcial)
  · errores por estado desconocido en v1 (síntoma del cambio 2)

REGLA DE PARADA
  si a T0 + 8 meses más del 15 % del volumen sigue en v1,
  la fecha de apagado se revisa: apagar con ese volumen
  no es una decisión técnica, es un incidente programado
```

**Interpreta:** cuatro cambios, tres estrategias distintas. El error habitual es
aplicar la misma a todos: crear una versión nueva por cada cambio (y tener seis
versiones vivas) o meterlos todos en la actual (y romper a 71 integradores).

## 🧭 Perspectivas

El contrato de la API afecta a cada actor de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Que la app deja de mostrar movimientos | Si la desinstala |
| Integrador | Un cambio que no esperaba | Cuándo migra |
| Banco | 180 integradores que coordinar | Cuánto margen da |
| Esquema | Fragmentación de versiones | Si fija la fecha de corte |
| Infraestructura | Dos versiones en paralelo | Coste de mantener ambas |
| Supervisor | Incidentes por migración | Si exige plazo mínimo |
| Auditor | Cabeceras de depreciación | Si el aviso existió |

## 🏦 Del cliente al banco

El cliente ve un pago duplicado y el banco tiene un reintento que no se controló. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «La app dejó de leer mi banco» | Versión apagada sin migración completa | 17, clase 8 |
| «Me cobraron dos veces» | Idempotencia sin bloqueo por clave | 17, clase 8 |
| «Veo movimientos repetidos» | Paginación por desplazamiento | 17, clase 8 |
| «La app va lenta a fin de mes» | Límite de tasa mal dimensionado | 17, clase 13 |

## ⚖️ Riesgos y controles

Los riesgos son de contrato y de reintento. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Cambio incompatible sin versión | 71 integradores rotos | Regla de compatibilidad aplicada por escrito |
| Apagado prematuro | Volumen aún en v1 | Regla de parada por porcentaje |
| Doble cobro | Reintento sin bloqueo | Bloqueo por clave y huella canónica |
| Movimientos duplicados | Paginación por desplazamiento | Cursor con orden total |
| Denegación mutua | 429 sin `Retry-After` | Cabeceras completas |
| Enumerado sin cláusula por defecto | Excepción en el integrador | Regla documentada desde v1 |

## 🧪 Práctica

En [`labs/lab-03.md`](../labs/lab-03.md) y [`labs/lab-04.md`](../labs/lab-04.md):

1. Clasifica diez cambios como compatibles o incompatibles y justifica.
2. Implementa la idempotencia con los cuatro detalles.
3. Demuestra el fallo de la paginación por desplazamiento con inserción concurrente.
4. Diseña el calendario de depreciación de una versión, con su regla de parada.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen integraciones que se rompen o que duplican. Las causas son cambios incompatibles sin versión y operaciones no idempotentes.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Versión nueva por cada cambio | No se clasificó la compatibilidad | Aplica la regla del cliente sin tocar |
| Valor nuevo en enumerado sin aviso | Se creyó aditivo | Cláusula por defecto y periodo de preparación |
| Idempotencia sin canonicalizar | Se firmó el texto crudo | Canonicaliza antes de la huella |
| Idempotencia sin bloqueo | No se pensó en la concurrencia | Bloqueo por clave |
| Cursor legible | Se codificó en claro | Cursor opaco |
| Apagar en la fecha pase lo que pase | Se trató como plazo administrativo | Regla de parada por volumen |

## ❓ Preguntas de comprobación

1. ¿Cuál es la regla operativa que distingue un cambio compatible de uno que no lo
   es?
2. ¿Por qué añadir un valor a un enumerado de respuesta rompe a los integradores?
3. ¿Cuáles son los cuatro detalles de una idempotencia correcta y cuál falla bajo
   concurrencia?
4. ¿Por qué el cursor debe ser opaco y qué se pierde si no lo es?
5. ¿Por qué una fecha de apagado no debe cumplirse incondicionalmente?

## 📥 Entregable

Guarda en `portfolio/parte-17/clase-08/`:

- la clasificación de diez cambios con su justificación;
- la implementación de idempotencia con los cuatro detalles y sus pruebas;
- la demostración del fallo de la paginación por desplazamiento;
- el calendario de depreciación con su regla de parada.

## 🔗 Referencias cruzadas

- **Viene de:** clase 4 (diccionario de datos), clase 7 (perfil de seguridad).
- **Continúa en:** clase 9 (APIs de información), clase 10 (iniciación de pagos),
  clase 13 (SLA y observabilidad).
- **Se aplica en:** Parte 18, clase 6 (versionado de mensajería); Parte 23,
  clase 7 (contratos de servicio).

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

- OpenAPI Initiative. *OpenAPI Specification 3.1*. Formato del contrato de la API que la clase escribe. <https://spec.openapis.org/oas/v3.1.0.html>
- Internet Engineering Task Force. *RFC 9110 — HTTP Semantics*. IETF. Definición de método idempotente y semántica de reintento. <https://www.rfc-editor.org/rfc/rfc9110>
- Internet Engineering Task Force. *RFC 8594 — The Sunset HTTP Header Field*. IETF. Anuncio del retiro de una versión con antelación. <https://www.rfc-editor.org/rfc/rfc8594>
- Internet Engineering Task Force. *RFC 9457 — Problem Details for HTTP APIs*. IETF. Formato uniforme de los errores devueltos al tercero. <https://www.rfc-editor.org/rfc/rfc9457>
- Comisión para el Mercado Financiero. *Anexo técnico del Sistema de Finanzas Abiertas: versionado y disponibilidad*. CMF. Exigencias de versionado y disponibilidad de la normativa. <https://www.cmfchile.cl/>
- Verificación local: comprueba si el anexo técnico de tu jurisdicción fija plazos mínimos de coexistencia entre versiones y requisitos de aviso previo. **Fecha de verificación de esta clase: 2026-08-20.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 07 · Financial-grade APIs, certificados y firma de mensajes](07-financial-grade-apis-y-firma.md) | [Parte 17](../README.md) · [Programa](../../../SYLLABUS.md) | [09 · APIs de cuentas, productos, créditos, seguros e inversiones →](09-apis-de-informacion-financiera.md) |
<!-- gen:footer:end -->
