<!-- meta
part: 17
class: 13
title: "Disponibilidad, SLA, observabilidad e incidentes"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global, chile, union-europea]
regulatory_topics: [open-finance, resiliencia-operacional, riesgo-de-terceros]
regulation_last_verified: 2026-08-20
regulatory_status: vigente
primary_authorities: [CMF]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 13 · Disponibilidad, SLA, observabilidad e incidentes

> [← 12 · Privacidad, finalidad, minimización y portabilidad](12-privacidad-finalidad-y-portabilidad.md) · [Índice de la parte](../README.md) · [14 · Proyecto: agregador financiero regulado →](14-proyecto-agregador-financiero-regulado.md)

**Parte 17 — Finanzas abiertas, APIs y economía de datos** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Convertir «el servicio funciona» en un compromiso medible, y preparar el día en
que no funcione. En un ecosistema de finanzas abiertas, la caída de uno se
convierte en el incidente de muchos.

Todo lo construido en las doce clases anteriores tiene que estar disponible cuando alguien lo use. Esta clase mide esa disponibilidad con las métricas correctas y establece qué se compromete frente a terceros, que no es lo mismo que el objetivo interno.

## 📚 Objetivos

Al finalizar podrás:

1. **Definir** un objetivo de nivel de servicio con indicador, ventana y umbral.
2. **Calcular** presupuesto de error y usarlo para decidir, no para informar.
3. **Diseñar** la observabilidad mínima de una API financiera.
4. **Clasificar** un incidente y determinar a quién y cuándo hay que notificar.
5. **Evaluar** el riesgo de concentración de proveedores y su plan de salida.

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

Los cuatro primeros términos son las métricas de servicio y su presupuesto; los cuatro siguientes, la observación y la salida. La distinción entre **SLI, SLO y SLA** es la que hay que fijar: el compromiso contractual tiene que ser más laxo que el objetivo interno, o cada desviación se convierte en un incumplimiento y el equipo deja de reportar la verdad.

| Concepto | Comprensión verificable |
|---|---|
| `SLI` | Indicador que mide el servicio desde la perspectiva de quien lo usa |
| `SLO` | Objetivo interno sobre ese indicador |
| `SLA` | Compromiso contractual, con consecuencia si se incumple |
| `presupuesto de error` | Fallo admisible dentro del objetivo, expresado en tiempo o peticiones |
| `observabilidad` | Capacidad de responder preguntas nuevas sobre el sistema sin desplegar |
| `degradación` | Servicio parcial en vez de caída total |
| `incidente` | Interrupción o deterioro con impacto en el usuario |
| `plan de salida` | Cómo se sustituye un proveedor sin detener el servicio |

## 🧠 Modelo mental

El modelo mental es un presupuesto de error que se gasta: si el objetivo es 99,5 %, el 0,5 % restante es una cantidad concreta de fallos admisibles que se puede consumir en mejoras o en incidentes. Verlo como presupuesto convierte la disponibilidad en una decisión.

```text
LA CADENA DE UNA CAÍDA EN FINANZAS ABIERTAS

  proveedor tecnológico cae
    → 40 terceros dejan de funcionar
      → 2 millones de clientes ven su app vacía
        → llaman a SU BANCO, que no tiene el problema
          → el banco recibe el coste de un incidente ajeno

  POR ESO LA DISPONIBILIDAD NO ES UN ASUNTO INTERNO:
  es una externalidad del ecosistema

LAS TRES SIGLAS
  SLI  qué mido        «% de peticiones con éxito en < 2 s»
  SLO  qué me exijo    «99,5 % en 28 días»
  SLA  qué firmo       «99,0 % o penalización de X»

  SLA SIEMPRE MÁS LAXO QUE EL SLO
  si son iguales, cada desviación interna es un incumplimiento
  contractual y el equipo deja de reportar la verdad
```

## 📖 Desarrollo

### 1. Elegir el indicador correcto

Un indicador mal elegido puede estar en verde mientras ningún cliente logra
usar el servicio. El bloque contrapone las dos formulaciones, explica qué mide
cada una y propone los tres indicadores mínimos de una API financiera.

```text
INDICADOR MALO
  «disponibilidad del servidor: 99,9 %»
  el servidor responde... 500 a todo el mundo

INDICADOR BUENO
  «proporción de peticiones válidas que devuelven una
   respuesta correcta en menos de 2 s»

LA DIFERENCIA
  el primero mide el sistema
  el segundo mide la EXPERIENCIA de quien lo usa

TRES INDICADORES MÍNIMOS EN UNA API FINANCIERA
  disponibilidad  % de peticiones sin error del servidor
  latencia        % de peticiones bajo el umbral
  corrección      % de respuestas coherentes con el contrato
```

### 2. Presupuesto de error

El presupuesto de error convierte un objetivo abstracto en minutos concretos
que se pueden gastar. El bloque lo calcula sobre un objetivo realista y
explica en qué decisión se traduce cuando queda saldo y cuando se agota.

```text
SLO 99,5 % EN 28 DÍAS
  28 × 24 × 60 = 40 320 minutos
  0,5 % = 201,6 minutos de presupuesto

PARA QUÉ SIRVE
  · si queda presupuesto: se puede desplegar, experimentar,
    migrar
  · si se agotó: se congelan los cambios y se dedica
    el esfuerzo a fiabilidad

ES UNA HERRAMIENTA DE DECISIÓN, NO UN INFORME
  «este trimestre gastamos el 80 % del presupuesto en
   dos incidentes de la misma causa» es una decisión
   de inversión, no una métrica de vanidad

EL PRESUPUESTO SE GASTA DONDE DUELE
  201 minutos repartidos en 30 días ≈ imperceptible
  201 minutos seguidos el día 5 de mes, en hora punta,
  con vencimientos de tarjeta ≈ incidente mayor

  → por eso se mide además la CONCENTRACIÓN del gasto
```

### 3. Observabilidad mínima

Observar no es solo guardar registros: son tres fuentes que responden
preguntas distintas y que se necesitan a la vez. El bloque detalla qué lleva
cada una, y también qué no debe llevar nunca la primera.

```text
REGISTRO (qué pasó)
  por petición: id de petición, cliente, consentimiento,
  endpoint, versión, código de respuesta, duración
  NUNCA: tokens, credenciales, cuerpo con datos personales

MÉTRICAS (cuánto y con qué forma)
  peticiones por segundo, por endpoint y por cliente
  latencia en percentiles, no en promedio
  errores por código y por cliente
  saturación: colas, conexiones, límites de tasa alcanzados

TRAZAS (por dónde pasó)
  identificador de correlación que atraviesa todos los
  componentes, propagado desde la cabecera del llamante

LA PREGUNTA QUE HAY QUE PODER RESPONDER SIN DESPLEGAR
  «¿por qué las peticiones del cliente X al endpoint Y
   fallaron entre las 14:03 y las 14:19?»
  si hace falta añadir código para responderla,
  no hay observabilidad: hay monitorización
```

### 4. Degradar en vez de caer

Ante la saturación hay una escalera de respuestas, y todas son preferibles a
la caída. El bloque las ordena de menos a más drástica y cierra con la regla
que las justifica.

```text
JERARQUÍA DE RESPUESTA A LA SATURACIÓN

  1. limitar por tasa a quien más consume
  2. servir desde caché con marca de antigüedad
     «saldo a las 14:02»
  3. reducir el alcance: posiciones sí, movimientos no
  4. cola con respuesta 202 y consulta posterior
  5. rechazar con 503 y Retry-After

  CAER SIN CONTROL ES LA OPCIÓN 6, Y ES LA PEOR
  PORQUE NO INFORMA

REGLA DE DISEÑO
  el dato viejo declarado como viejo es mejor que
  la ausencia de dato. El dato viejo presentado
  como fresco es peor que ambos.
```

### 5. Incidentes: clasificar y notificar

| Nivel | Criterio | Notificación |
|---|---|---|
| 1 — Crítico | Servicio no disponible o datos incorrectos publicados | Inmediata a terceros y, según norma, al supervisor |
| 2 — Mayor | Degradación con impacto en el usuario | En horas, a terceros afectados |
| 3 — Menor | Deterioro sin impacto perceptible | En el informe periódico |
| 4 — Sin impacto | Detectado y contenido | Registro interno |

La clasificación por niveles se aplica con un criterio que no siempre coincide
con la gravedad técnica del fallo.

```text
LO QUE CONVIERTE UN INCIDENTE EN CRÍTICO NO ES LA CAUSA:
ES EL EFECTO SOBRE EL CLIENTE FINAL

  publicar saldos incorrectos durante 6 minutos
  es más grave que estar caído 40 minutos

  porque en el primer caso el cliente DECIDIÓ
  con un dato falso, y esa decisión no se revierte
  restableciendo el servicio
```

### 6. Concentración y plan de salida

Depender de un proveedor no es un riesgo mientras exista una salida probada. El
bloque plantea las seis preguntas que la comprueban y señala en cuál se cae
casi siempre.

```text
PREGUNTAS DEL PLAN DE SALIDA

  1. ¿cuántos participantes dependen de este proveedor?
  2. ¿cuánto tarda una sustitución, con qué esfuerzo?
  3. ¿los datos son portables a otro proveedor?
  4. ¿hay dependencia de formatos propietarios?
  5. ¿existe un segundo proveedor probado, no solo contratado?
  6. ¿se ha ENSAYADO la sustitución alguna vez?

LA PREGUNTA 6 ES LA QUE FALLA
  un plan de salida no ensayado es un documento,
  no un plan
```

## 🧮 Ejemplo guiado

El ejemplo calcula el presupuesto de error de un servicio y lo contrasta con su consumo. Conviene medirlo en peticiones y no en minutos: el goteo continuo de errores no aparece en los minutos de incidente.

**Situación.** Una institución proveedora revisa su trimestre antes de renovar el
acuerdo de nivel de servicio con 180 terceros.

```text
DATOS DEL TRIMESTRE (90 días)
  peticiones                            412 000 000
  errores del servidor (5xx)              3 296 000
  peticiones sobre 2 s                   18 540 000
  respuestas incoherentes detectadas         82 400

INCIDENTES
  I1  día 12, 04:10-05:32,  82 min, caída total
  I2  día 45, 14:03-14:09,   6 min, saldos incorrectos
  I3  día 61, 09:20-10:38,  78 min, degradación parcial
  I4  día 78, 18:44-19:02,  18 min, caída total

SLO VIGENTE: 99,5 % disponibilidad, ventana 28 días
SLA VIGENTE: 99,0 % con penalización de 4 200 000 por incumplimiento
```

**Paso 1 — calcula los tres indicadores.**

```text
DISPONIBILIDAD
  1 − 3 296 000 / 412 000 000 = 99,20 %      ✗ (SLO 99,5 %)

LATENCIA
  1 − 18 540 000 / 412 000 000 = 95,50 %     ✗ (objetivo 99,0 %)

CORRECCIÓN
  1 − 82 400 / 412 000 000 = 99,98 %         ✓ en porcentaje
```

**Paso 2 — no te quedes en el porcentaje de corrección.**

```text
82 400 RESPUESTAS INCOHERENTES ES UN 0,02 %

  PERO todas ocurrieron en I2: 6 minutos
  → 82 400 clientes vieron un saldo falso
  → algunos decidieron con él

  EL PORCENTAJE DICE «excelente»
  EL VALOR ABSOLUTO DICE «82 400 personas»

  regla: en corrección se reporta el valor absoluto,
  no solo la proporción
```

**Paso 3 — calcula el presupuesto de error por ventana.**

```text
VENTANA 1 (días 1-28):   I1 = 82 min
  presupuesto 201,6 min → gastado 40,7 %      ✓

VENTANA 2 (días 29-56):  I2 = 6 min
  gastado 3,0 %                                ✓

VENTANA 3 (días 57-84):  I3 = 78 min, I4 = 18 min
  gastado 96 min = 47,6 %                      ✓

SORPRESA
  ninguna ventana agotó el presupuesto,
  y sin embargo la disponibilidad trimestral (99,20 %)
  está por debajo del SLO

  CAUSA
    los 5xx no ocurren solo durante los incidentes:
    hay un goteo continuo que ninguna ventana captura
    como «tiempo caído»

  → medir por MINUTOS DE INCIDENTE oculta el goteo
  → el presupuesto debe calcularse sobre PETICIONES,
    no sobre minutos
```

**Paso 4 — recalcula sobre peticiones.**

```text
PRESUPUESTO EN PETICIONES (99,5 % de 412 000 000)
  admisible: 2 060 000 errores
  real:      3 296 000
  exceso:    1 236 000  → 160 % del presupuesto

DESGLOSE DEL EXCESO
  durante incidentes:  1 910 000
  goteo continuo:      1 386 000  ← 42 % del total

  el goteo, invisible en el informe de incidentes,
  es casi la mitad del problema
```

**Paso 5 — evalúa el SLA con 180 terceros.**

```text
SLA 99,0 %: el trimestre dio 99,20 % → NO se incumple
SLO 99,5 %: sí se incumple

ESTA ES LA SITUACIÓN QUE HAY QUE SABER LEER
  contractualmente: todo bien, sin penalización
  operativamente:   objetivo interno incumplido
  para el cliente:  3,3 millones de peticiones fallidas

  SI SE MIRA SOLO EL SLA, NO SE HACE NADA.
  El SLO existe precisamente para actuar antes
  de llegar al SLA.
```

**Paso 6 — decide sobre la renovación.**

```text
PROPUESTA DE LOS TERCEROS: subir el SLA a 99,5 %

ANÁLISIS
  con el desempeño actual (99,20 %), firmar 99,5 %
  significa penalización esperada en 3 de 4 trimestres

  penalización: 4 200 000 × 3 = 12 600 000 al año

  COSTE DE ALCANZAR 99,5 % DE VERDAD
    eliminar el goteo (causa raíz: agotamiento de
    conexiones en el pico)                   14 000 000
    redundancia del componente de I1          22 000 000
    observabilidad para detectar el goteo      8 000 000
    ensayo de conmutación trimestral           6 000 000/año
    TOTAL PRIMER AÑO                          50 000 000

DECISIÓN
  NO firmar 99,5 % hoy. Firmar 99,2 % con compromiso
  escalonado: 99,35 % a los 6 meses y 99,5 % a los 12,
  con la inversión aprobada y verificable.

  MOTIVO
    firmar un objetivo que no se puede cumplir
    convierte el acuerdo en una transferencia de dinero,
    no en una mejora del servicio.
    Los 180 terceros prefieren el servicio.
```

**Paso 7 — cierra el incidente I2 con lo que importa.**

```text
I2 DURÓ 6 MINUTOS Y ES EL MÁS GRAVE DEL TRIMESTRE

  ACCIONES
    · notificación a los 180 terceros: hecha en 11 min
    · notificación al supervisor: según la norma aplicable
      (verificar plazo y umbral vigentes)
    · identificación de los 82 400 clientes afectados
    · aviso a los terceros para que invaliden su caché
    · análisis de causa raíz publicado

  CONTROL NUEVO
    verificación de coherencia saldo/movimientos
    ANTES de responder, con corte del servicio
    si falla: es preferible no responder
    a responder mal
```

**Interpreta:** el informe de incidentes decía que ninguna ventana agotó el
presupuesto. La medición sobre peticiones reveló que el 42 % del fallo era un
goteo continuo que ningún incidente registró. **La métrica elegida determinó qué
problema se veía.**

## 🧭 Perspectivas

La disponibilidad afecta a cada actor de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Una app que no carga | Si la sigue usando |
| Tercero | Fallos que no puede explicar | Si exige SLA o cambia de proveedor |
| Banco | SLA cumplido, SLO incumplido | Si invierte o si espera |
| Proveedor tecnológico | 40 clientes afectados a la vez | Su plan de continuidad |
| Supervisor | Incidente con datos incorrectos | Si abre expediente |
| Auditor | Plan de salida no ensayado | Qué observa |
| Sociedad | Dependencia de pocos proveedores | Regulación de terceros críticos |

## 🏦 Del cliente al banco

El cliente no puede operar y el banco consume presupuesto de error. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «La app no carga mi banco» | Goteo de 5xx, no un incidente | 17, clase 13 |
| «Me mostró un saldo que no era» | Incidente crítico por corrección | 17, clase 13 |
| «Va lenta a fin de mes» | Latencia en hora punta | 17, clase 13 |
| «Todas las apps fallaron a la vez» | Proveedor tecnológico crítico | 17, clase 2 |

## ⚖️ Riesgos y controles

Los riesgos son de disponibilidad y de dependencia. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Métrica que oculta el problema | Presupuesto medido en minutos | Medir sobre peticiones |
| SLA igual al SLO | Cada desviación es incumplimiento | SLA más laxo que el SLO |
| Dato incorrecto publicado | Incoherencia no detectada | Verificación antes de responder |
| Caída sin degradación | Todo o nada | Jerarquía de degradación |
| Proveedor concentrado | 40 participantes en uno | Plan de salida ensayado |
| Observabilidad insuficiente | Hace falta desplegar para diagnosticar | Trazas con correlación |

## 🧪 Práctica

El laboratorio pide calcular el presupuesto de error de un servicio y contrastarlo con su consumo real. La medición en peticiones y no en minutos es lo que hace visible el goteo continuo de errores.

En [`labs/lab-06.md`](../labs/lab-06.md):

1. Define SLI, SLO y SLA de tu API, con ventana y umbral.
2. Calcula el presupuesto de error sobre peticiones y sobre minutos, y compara.
3. Diseña la jerarquía de degradación de tu servicio.
4. Escribe el procedimiento de notificación por nivel de incidente.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen servicios que cumplen el compromiso y no funcionan. La causa es la métrica elegida.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Medir disponibilidad del servidor | Se midió el sistema | Mide la experiencia del llamante |
| Latencia en promedio | El promedio esconde la cola | Percentiles p95 y p99 |
| Presupuesto en minutos | Se contaron incidentes | Cuenta peticiones |
| SLA = SLO | Se igualaron por simplicidad | SLA más laxo |
| Caer en vez de degradar | No hay jerarquía | Cinco niveles antes del 503 |
| Plan de salida sin ensayo | Se documentó y se archivó | Ensayo periódico con evidencia |

## ❓ Preguntas de comprobación

1. ¿Qué diferencia hay entre SLI, SLO y SLA, y por qué el SLA debe ser más laxo?
2. ¿Por qué medir el presupuesto de error en minutos ocultó el 42 % del fallo?
3. ¿Por qué un incidente de 6 minutos fue más grave que uno de 82?
4. ¿Cuáles son los cinco niveles de degradación antes de rechazar?
5. ¿Qué pregunta del plan de salida es la que más veces queda sin responder?

## 📥 Entregable

Guarda en `portfolio/parte-17/clase-13/`:

- SLI, SLO y SLA de tu API con ventana, umbral y justificación;
- el presupuesto de error calculado de las dos formas, con la comparación;
- la jerarquía de degradación de tu servicio;
- el plan de salida de tu proveedor crítico, con la fecha del ensayo previsto.

## 🔗 Referencias cruzadas

- **Viene de:** clase 2 (proveedores críticos), clase 8 (límite de tasa),
  clase 12 (retención); Parte 11, clase 12 (riesgo operacional).
- **Continúa en:** clase 14 (proyecto).
- **Se aplica en:** Parte 18, clase 13; Parte 22, clase 15 (resiliencia
  operacional); Parte 23, clases 16 y 17.

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

- Parlamento Europeo y Consejo. *Reglamento (UE) 2022/2554 sobre la resiliencia operativa digital del sector financiero*. Obligaciones de resiliencia digital y reporte de incidentes. <https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32022R2554>
- Basel Committee on Banking Supervision (2021). *Principles for operational resilience*. BIS. Tolerancia a la interrupción de los servicios críticos. <https://www.bis.org/bcbs/publ/d516.htm>
- Financial Stability Board (2023). *Enhancing third-party risk management and oversight: a toolkit*. FSB. Dependencia de terceros y planes de salida. <https://www.fsb.org/2023/12/final-report-on-enhancing-third-party-risk-management-and-oversight-a-toolkit-for-financial-institutions-and-financial-authorities/>
- Comisión para el Mercado Financiero. *Normativa sobre gestión de la continuidad operacional, ciberseguridad y reporte de incidentes*. CMF. Exigencias chilenas de continuidad y reporte de incidentes. <https://www.cmfchile.cl/>
- Committee on Payments and Market Infrastructures e IOSCO (2016). *Guidance on cyber resilience for financial market infrastructures*. BIS. Expectativas de ciberresiliencia aplicables a la infraestructura. <https://www.bis.org/cpmi/publ/d146.htm>
- Verificación local: comprueba los umbrales y plazos de notificación de incidentes exigidos en tu jurisdicción y si existe régimen de proveedores tecnológicos críticos. **Fecha de verificación de esta clase: 2026-08-20.** Esta clase no constituye asesoría legal.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 12 · Privacidad, finalidad, minimización y portabilidad](12-privacidad-finalidad-y-portabilidad.md) | [Parte 17](../README.md) · [Programa](../../../SYLLABUS.md) | [14 · Proyecto: agregador financiero regulado →](14-proyecto-agregador-financiero-regulado.md) |
<!-- gen:footer:end -->
