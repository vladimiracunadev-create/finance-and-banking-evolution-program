<!-- meta
part: 17
class: 7
title: "Financial-grade APIs, certificados y firma de mensajes"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global]
regulatory_topics: [open-finance, seguridad, criptografia]
regulation_last_verified: 2026-08-06
regulatory_status: estandar-vigente
primary_authorities: [OpenID Foundation, IETF]
requires_legal_review: false
-->

<!-- gen:header:start -->
# Clase 07 · Financial-grade APIs, certificados y firma de mensajes

> [← 06 · OAuth, OpenID Connect y autorización financiera](06-oauth-openid-connect-y-autorizacion.md) · [Índice de la parte](../README.md) · [08 · Diseño, versionado e idempotencia →](08-diseno-versionado-e-idempotencia.md)

**Parte 17 — Finanzas abiertas, APIs y economía de datos** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Entender por qué el perfil por defecto de OAuth y OpenID Connect no basta cuando
lo que hay al otro lado es dinero, y qué añade exactamente un perfil de grado
financiero: identidad del canal, prueba de posesión, firma de mensajes y gestión
de claves.

El protocolo de la clase anterior es el estándar general de internet. Esta añade lo que un contexto financiero exige por encima, y cada exigencia cierra un ataque concreto que el perfil base deja abierto.

## 📚 Objetivos

Al finalizar podrás:

1. **Explicar** qué amenazas quedan abiertas con el perfil por defecto y cuáles
   cierra un perfil financiero.
2. **Distinguir** token al portador de token ligado al emisor, y decir cuándo
   hace falta cada uno.
3. **Diseñar** la cadena de confianza: autoridad certificadora, certificado,
   huella y directorio.
4. **Especificar** la firma de una petición y su verificación, incluida la
   protección contra repetición.
5. **Planificar** una rotación de claves sin cortar el servicio.

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

Los tres primeros términos son el perfil de seguridad y su transporte; los cinco siguientes, los mecanismos criptográficos y su gestión. La diferencia entre **token al portador y prueba de posesión** es la que decide el daño de una filtración: el primero lo puede usar cualquiera que lo tenga.

| Concepto | Comprensión verificable |
|---|---|
| `perfil de seguridad` | Restricción de un estándar general para un uso concreto |
| `mTLS` | Autenticación mutua en la capa de transporte: ambos extremos presentan certificado |
| `token al portador` | Quien lo tiene, lo usa; no prueba ser su titular |
| `prueba de posesión` | El token solo sirve a quien posee la clave asociada |
| `DPoP` | Prueba de posesión en la capa de aplicación, con una clave del cliente |
| `JWS` | Firma de un contenido en formato JSON Web Signature |
| `JWE` | Cifrado de un contenido en formato JSON Web Encryption |
| `rotación de claves` | Sustitución planificada de claves sin interrupción |

## 🧠 Modelo mental

El modelo mental es una escalera de exigencia: el perfil financiero añade sobre el protocolo base la autenticación mutua, la firma de mensajes y la prueba de posesión. Cada escalón cierra un ataque concreto y cuesta implementación.

```text
EL PROBLEMA DEL TOKEN AL PORTADOR

  un token al portador es como un billete:
  quien lo tiene, lo gasta

  si se filtra —registro, proxy, error de caché,
  cabecera reenviada— quien lo encuentre tiene acceso

LA RESPUESTA DE UN PERFIL FINANCIERO
  ligar el token a algo que el atacante NO puede robar
  con el token:

    mTLS   el token solo sirve desde el canal cuyo certificado
           se usó para pedirlo
    DPoP   el token solo sirve acompañado de una firma hecha
           con la clave privada del cliente

  en ambos casos: robar el token ya no basta
```

## 📖 Desarrollo

### 1. Qué deja abierto el perfil por defecto

| Amenaza | ¿La cubre el perfil por defecto? | Qué la cierra |
|---|---|---|
| Robo del código de autorización | Parcial (PKCE) | PKCE obligatorio con S256 |
| Robo del token de acceso | No | mTLS o DPoP |
| Sustitución de la respuesta de autorización | No | Respuesta firmada |
| Manipulación de los parámetros de la petición | No | Petición firmada |
| Repetición de una petición firmada | No | `nonce` y ventana temporal |
| Suplantación del cliente | Parcial | Autenticación por certificado |
| Confusión de servidor de autorización | No | `iss` en la respuesta de autorización |

```text
LA AMENAZA QUE MÁS SE SUBESTIMA
  «manipulación de los parámetros de la petición»

  si el importe y el beneficiario de una iniciación de pago
  viajan como parámetros no firmados en la URL del navegador,
  cualquier cosa entre medias puede cambiarlos

  → el cliente aprueba una pantalla que dice 45 000
    y el sistema ejecuta lo que llegó, que puede ser otra cosa
```

### 2. Objeto de petición firmado

La primera diferencia visible de un perfil de grado financiero es que los
parámetros dejan de viajar sueltos. El bloque compara las dos formas de enviar
la misma petición y detalla qué gana el servidor al recibir la segunda.

```text
EN VEZ DE ENVIAR LOS PARÁMETROS SUELTOS

  ?client_id=...&scope=...&amount=45000&creditor=...

SE ENVÍA UN OBJETO FIRMADO

  ?client_id=...&request=<JWS con todos los parámetros>

QUÉ CAMBIA
  · el servidor verifica la firma con la clave pública del cliente
  · cualquier alteración invalida la firma
  · el contenido puede ir cifrado (JWE) si es sensible
  · el objeto incluye exp y jti para acotar su validez y su uso

QUÉ NO CAMBIA
  la firma NO autentica al usuario: autentica al CLIENTE
  y protege la INTEGRIDAD de lo que pidió
```

### 3. mTLS y DPoP: cuándo cada uno

| | mTLS | DPoP |
|---|---|---|
| Capa | Transporte | Aplicación |
| Qué liga el token | Al certificado del canal | A una clave del cliente |
| Requiere | Infraestructura de certificados | Solo criptografía en el cliente |
| Sobrevive a un proxy que termina TLS | No sin cuidado | Sí |
| Encaja bien en | Servidor a servidor | Aplicaciones móviles y de navegador |
| Coste operativo | Alto: emisión, renovación, revocación | Menor |

```text
CRITERIO DE ELECCIÓN
  ¿el cliente es un servidor bajo tu control operativo?
    → mTLS: además identifica a la entidad
  ¿el cliente es una aplicación en el dispositivo del usuario?
    → DPoP: no hay dónde guardar un certificado de entidad

  y en muchos esquemas: mTLS entre entidades
  + DPoP entre la aplicación y su propio servidor
```

### 4. La cadena de confianza

La firma solo vale si se puede decir de quién es la clave, y eso lo resuelve
una cadena de certificados que llega hasta la autoridad del esquema. El
diagrama la recorre y enumera las cinco comprobaciones del servidor.

```text
AUTORIDAD DEL ESQUEMA
      │ emite
      ▼
CERTIFICADO DEL PARTICIPANTE  (identidad + rol + alcances permitidos)
      │ se presenta en
      ▼
CANAL mTLS  ──► el servidor comprueba:
                 1. cadena hasta la autoridad del esquema
                 2. certificado no revocado
                 3. huella coincide con la del directorio
                 4. el rol del certificado permite la operación
                 5. el participante está ACTIVO hoy

LOS CINCO SE COMPRUEBAN. Omitir el 5 es el error operativo típico:
un participante suspendido conserva un certificado técnicamente válido.
```

### 5. Protección contra repetición

Una petición firmada es auténtica aunque la reenvíe un atacante: la firma
sigue siendo válida. El bloque presenta los tres campos que, usados a la vez,
convierten una petición válida en una petición válida **una sola vez**.

```text
UNA PETICIÓN FIRMADA VÁLIDA, CAPTURADA, PUEDE REENVIARSE

  CONTROLES, LOS TRES A LA VEZ
    jti    identificador único de la petición; el servidor
           lo recuerda durante la ventana de validez
    iat    momento de emisión
    exp    caducidad corta (segundos, no minutos)

  VENTANA TÍPICA: 60 s
    · demasiado corta → fallos por desfase de reloj
    · demasiado larga → ventana de repetición
    · se sincronizan relojes y se documenta la tolerancia
```

### 6. Rotación de claves sin cortar el servicio

Cambiar la clave de firma sin cortar el servicio es un problema de
calendario, no de criptografía. El bloque fija la regla de solape, los dos
plazos que hay que respetar y el error que se comete cuando se ignoran.

```text
LA REGLA: SIEMPRE HAY DOS CLAVES VÁLIDAS A LA VEZ

  T0   se publica la clave nueva junto a la vigente,
       con identificador distinto (kid)
  T1   se empieza a firmar con la nueva
       (los verificadores ya la conocen: la publicaste en T0)
  T2   se retira la antigua del conjunto publicado

  T1 − T0 ≥ tiempo máximo de caché del conjunto de claves
  T2 − T1 ≥ vida máxima de un token firmado con la antigua

EL ERROR CLÁSICO
  publicar y empezar a firmar el mismo día:
  los verificadores con caché siguen sin conocer la clave nueva
  y rechazan todo hasta que la caché expira
```

## 🧮 Ejemplo guiado

El ejemplo construye una petición firmada con prueba de posesión. Conviene comparar con una al portador: la diferencia es qué puede hacer quien intercepte el token.

**Situación.** Un esquema debe elegir perfil de seguridad. Se comparan tres
opciones para 42 entidades proveedoras y 180 terceros.

```text
OPCIÓN A · perfil por defecto, token al portador
OPCIÓN B · mTLS + objeto de petición firmado
OPCIÓN C · DPoP + objeto de petición firmado
```

**Paso 1 — enumera la exposición residual de A.**

```text
CON TOKEN AL PORTADOR, UN TOKEN FILTRADO ES ACCESO PLENO

  vías de filtración observadas en incidentes del sector:
    · registro de aplicación (H4 de la clase 6)
    · cabecera reenviada por un proxy mal configurado
    · caché intermedia que almacena la respuesta
    · traza de error que incluye la cabecera
    · captura en el dispositivo

  probabilidad conjunta con 180 terceros:
  basta que UNO tenga uno de los cinco defectos
```

**Paso 2 — cuantifica el coste operativo de B.**

```text
CERTIFICADOS: 42 + 180 = 222 participantes
  emisión inicial                    222 × 40      =  8 880
  renovación anual                   222 × 25      =  5 550
  soporte de incidencias de certificado
    supuesto: 8 % anual con incidencia
    222 × 8 % × 180 (coste por caso)               =  3 197
  infraestructura de validación y revocación       = 12 000
  TOTAL primer año                                 ≈ 29 627
  TOTAL años siguientes                            ≈ 20 747
```

**Paso 3 — cuantifica el coste operativo de C.**

```text
DPoP NO NECESITA CERTIFICADOS DE ENTIDAD

  implementación en el servidor de autorización     =  9 000
  soporte a 180 terceros en la integración          = 14 000
  infraestructura (almacén de jti, ventana)         =  4 000
  TOTAL primer año                                  ≈ 27 000
  TOTAL años siguientes                             ≈  5 000
```

**Paso 4 — compara lo que NO cuesta dinero.**

```text
mTLS APORTA ALGO QUE DPoP NO
  identidad verificable de la ENTIDAD en cada conexión
  → el servidor sabe con qué participante habla
    antes de leer un solo byte de la aplicación
  → permite cortar por rol y por estado en el directorio

DPoP APORTA ALGO QUE mTLS NO
  sobrevive a terminación de TLS en balanceadores y proxies
  → menos incidentes de configuración
  → viable en aplicaciones de navegador
```

**Paso 5 — decide.**

```text
DECISIÓN: mTLS ENTRE ENTIDADES + OBJETO DE PETICIÓN FIRMADO
          y DPoP donde el cliente es una aplicación del usuario

MOTIVOS
  1. la identidad de entidad es un requisito del esquema,
     no una preferencia técnica: el directorio necesita
     un punto de corte antes de la capa de aplicación
  2. el sobrecoste anual de mTLS frente a DPoP (≈ 15 700)
     es menor que el coste esperado de un solo incidente
     de token filtrado con 180 terceros
  3. el objeto firmado es obligatorio en ambos casos:
     protege la integridad del importe y el beneficiario,
     que es lo que ninguna de las dos opciones cubre por sí sola

CONDICIÓN
  · plan de rotación de claves documentado, con T0/T1/T2
  · tolerancia de reloj declarada: 60 s
  · comprobación de estado en el directorio en cada conexión,
    con caché máxima de 5 minutos
```

**Paso 6 — planifica la primera rotación.**

```text
CALENDARIO

  T0  01-09-2026  publicar kid=2026-09 junto a kid=2026-03
  T1  08-09-2026  empezar a firmar con kid=2026-09
                  (7 días > caché máxima declarada de 24 h)
  T2  22-09-2026  retirar kid=2026-03
                  (14 días > vida máxima de token firmado: 12 h)

PRUEBA PREVIA
  en preproducción, con un verificador que cachea 24 h,
  comprobar que en T1 no hay rechazos

SEÑAL DE ALARMA DURANTE LA ROTACIÓN
  tasa de error de verificación por encima del 0,1 %
  → detener, no continuar
```

**Interpreta:** las tres opciones se compararon por coste, pero la decisión la
determinó un requisito que no era de coste: **el esquema necesita identificar a la
entidad antes de la capa de aplicación**. El objeto firmado, en cambio, no era una
opción: cubría una amenaza que ninguna de las tres alternativas cubría.

## 🧭 Perspectivas

El perfil de seguridad afecta a cada actor de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Nada: todo ocurre bajo el capó | Nada, y por eso hay que protegerlo |
| Fintech | Coste de gestionar certificados | Si usa un proveedor o lo hace |
| Banco | 180 terceros conectándose | Qué perfil exige |
| Esquema | Cadena de confianza | Quién es la autoridad certificadora |
| Infraestructura | Terminación de TLS en el balanceador | Arquitectura compatible con mTLS |
| Supervisor | Perfil de seguridad del anexo técnico | Qué certifica y con qué frecuencia |
| Auditor | Rotación y revocación | Si hay plan y si se ejecutó |

## 🏦 Del cliente al banco

El cliente no ve nada de esto y su exposición depende por completo de qué perfil se implementó. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «La app dejó de funcionar hoy» | Certificado caducado o rotación mal planificada | 17, clase 7 |
| «Aprobé 45 000 y cobraron otra cosa» | Petición no firmada | 17, clase 7 |
| «Nunca me pidieron nada raro» | Todo el perfil es invisible para el cliente | 17, clase 7 |
| «Esa empresa ya no opera» | Estado del directorio, no solo el certificado | 17, clase 2 |

## ⚖️ Riesgos y controles

Los riesgos son criptográficos y de gestión de claves. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Token filtrado y usado | Registro o proxy mal configurado | mTLS o DPoP |
| Manipulación de parámetros | Importe alterado en tránsito | Objeto de petición firmado |
| Repetición | Petición firmada capturada y reenviada | `jti`, `iat`, `exp` con ventana corta |
| Participante suspendido | Certificado válido, entidad no activa | Estado del directorio en cada conexión |
| Rotación mal planificada | Rechazos masivos en T1 | T0/T1/T2 con márgenes de caché |
| Clave comprometida | Firmas válidas del atacante | Revocación y rotación de emergencia probada |

## 🧪 Práctica

En [`labs/lab-02.md`](../labs/lab-02.md) y [`labs/lab-06.md`](../labs/lab-06.md):

1. Firma un objeto de petición y verifícalo; altera un campo y comprueba el fallo.
2. Implementa la ventana de repetición con `jti` y mide el efecto del desfase.
3. Diseña el calendario T0/T1/T2 de una rotación con tus propios márgenes.
4. Escribe la prueba que detecta un participante suspendido con certificado válido.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen implementaciones que no alcanzan el perfil. Las causas son tokens al portador y rotación de claves no ejecutada.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Solo se valida la cadena del certificado | Se olvidó el estado del participante | Comprueba los cinco puntos |
| Rotación publicada y usada el mismo día | No se consideró la caché | Respeta T1 − T0 |
| Ventana de repetición de 15 minutos | Se evitaron fallos de reloj | 60 s y relojes sincronizados |
| Parámetros sin firmar | Se confió en TLS | TLS protege el canal, no la intención |
| DPoP sin almacén de `jti` | Se implementó la firma, no la unicidad | Sin almacén no hay antirrepetición |
| Clave privada en el repositorio | Comodidad de despliegue | Gestión de secretos fuera del código |

## ❓ Preguntas de comprobación

1. ¿Qué diferencia hay entre un token al portador y uno con prueba de posesión, y
   qué ataque concreto cambia?
2. ¿Qué amenaza cubre el objeto de petición firmado que no cubren ni mTLS ni DPoP?
3. ¿Cuáles son los cinco puntos de comprobación de la cadena de confianza y cuál
   se omite con más frecuencia?
4. ¿Por qué la ventana de repetición no puede ser larga ni muy corta?
5. ¿Qué determina la distancia mínima entre T0 y T1 en una rotación de claves?

## 📥 Entregable

Guarda en `portfolio/parte-17/clase-07/`:

- la comparación de mTLS y DPoP para tu caso, con la decisión y su motivo;
- un objeto de petición firmado y la traza de su verificación fallida al alterarlo;
- el calendario de rotación T0/T1/T2 con los márgenes justificados;
- los cinco puntos de la cadena de confianza aplicados a un participante concreto.

## 🔗 Referencias cruzadas

- **Viene de:** clase 6 (OAuth y OpenID Connect); clase 2 (directorio y esquema).
- **Continúa en:** clase 8 (diseño de API), clase 13 (incidentes y continuidad).
- **Se aplica en:** Parte 18, clase 6 (firma en mensajería de pagos); Parte 19,
  clase 3 (gestión criptográfica); Parte 23, clase 16.

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

- OpenID Foundation. *FAPI 2.0 Security Profile*. <https://openid.net/wg/fapi/>
- Internet Engineering Task Force. *RFC 8705 — OAuth 2.0 Mutual-TLS Client Authentication and Certificate-Bound Access Tokens*. IETF. <https://www.rfc-editor.org/rfc/rfc8705>
- Internet Engineering Task Force. *RFC 9449 — OAuth 2.0 Demonstrating Proof of Possession (DPoP)*. IETF. <https://www.rfc-editor.org/rfc/rfc9449>
- Internet Engineering Task Force. *RFC 7515 — JSON Web Signature (JWS)* y *RFC 7516 — JSON Web Encryption (JWE)*. IETF. <https://www.rfc-editor.org/rfc/rfc7515>
- NIST (2020). *SP 800-57 Part 1 Rev. 5 — Recommendation for Key Management*. National Institute of Standards and Technology. <https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final>
- Verificación local: comprueba qué perfil y qué versión exige el anexo técnico vigente en tu jurisdicción, y quién actúa como autoridad certificadora del esquema. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 06 · OAuth, OpenID Connect y autorización financiera](06-oauth-openid-connect-y-autorizacion.md) | [Parte 17](../README.md) · [Programa](../../../SYLLABUS.md) | [08 · Diseño, versionado e idempotencia →](08-diseno-versionado-e-idempotencia.md) |
<!-- gen:footer:end -->
