---
part: 17
class: 6
title: "OAuth, OpenID Connect y autorización financiera"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global]
regulatory_topics: [open-finance, seguridad, autenticacion]
regulation_last_verified: 2026-08-06
regulatory_status: estandar-vigente
primary_authorities: [IETF, OpenID Foundation]
requires_legal_review: false
---

<!-- gen:header:start -->
# Clase 06 · OAuth, OpenID Connect y autorización financiera

> [← 05 · Consentimiento: creación, vigencia, renovación y revocación](05-consentimiento-ciclo-de-vida.md) · [Índice de la parte](../README.md) · [07 · Financial-grade APIs, certificados y firma de mensajes →](07-financial-grade-apis-y-firma.md)

**Parte 17 — Finanzas abiertas, APIs y economía de datos** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Entender qué resuelve OAuth 2.x, qué **no** resuelve, dónde entra OpenID Connect
y por qué el perfil por defecto de ambos es insuficiente para dinero. La clase
separa autorización de autenticación, que es la confusión más cara del área.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** autenticación de autorización y decir qué estándar resuelve cada
   una.
2. **Explicar** el flujo de código de autorización paso a paso, con sus
   parámetros y su razón de ser.
3. **Justificar** PKCE describiendo el ataque concreto que corta.
4. **Identificar** qué añade OpenID Connect sobre OAuth y cuándo hace falta.
5. **Detectar** los siete errores de implementación que aparecen en auditoría.

<!-- gen:agenda:start -->
## Agenda de 90 minutos

| Minutos | Bloque | Qué ocurre |
|---:|---|---|
| 0–10 | Activación | Pregunta diagnóstica y recuperación de la clase anterior. |
| 10–35 | Conceptos | Desarrollo guiado con la fuente oficial a la vista. |
| 35–55 | Ejemplo guiado | El docente resuelve el caso numérico paso a paso. |
| 55–80 | Práctica | El estudiante replica con datos propios o sintéticos. |
| 80–90 | Cierre | Preguntas de comprobación y registro en el portafolio. |
<!-- gen:agenda:end -->

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| `autenticación` | Comprobar quién es alguien |
| `autorización` | Comprobar qué puede hacer |
| `flujo de código` | Intercambio en dos etapas: código en el navegador, token en el canal directo |
| `PKCE` | Prueba de posesión que liga el código a quien lo pidió |
| `token de acceso` | Credencial de corta vida acotada a alcances |
| `token de refresco` | Credencial para obtener nuevos tokens de acceso |
| `token de identidad` | Afirmación firmada sobre quién es el usuario (OpenID Connect) |
| `introspección` | Consulta al emisor sobre la validez de un token |

## 🧠 Modelo mental

```text
LA PREGUNTA QUE ORDENA TODO

  «¿QUIÉN ERES?»          → autenticación → OpenID Connect
  «¿QUÉ PUEDES HACER?»    → autorización  → OAuth 2.x

OAUTH NO ES UN PROTOCOLO DE AUTENTICACIÓN
  usarlo como tal es el error clásico:
  un token de acceso demuestra que ALGUIEN autorizó algo,
  no demuestra QUIÉN está delante

EL ACTO CENTRAL DE OAUTH
  el cliente nunca ve la credencial del usuario.
  El usuario se autentica ANTE SU PROPIA INSTITUCIÓN
  y esta emite una autorización acotada.
```

## 📖 Desarrollo

### 1. Los cuatro papeles

```text
PROPIETARIO DEL RECURSO     el cliente, dueño de los datos
CLIENTE                     la aplicación que quiere acceder
SERVIDOR DE AUTORIZACIÓN    quien autentica y emite tokens
SERVIDOR DE RECURSOS        la API que expone los datos

CONFUSIÓN FRECUENTE
  «cliente» en OAuth es la APLICACIÓN, no la persona.
  La persona es el propietario del recurso.
```

### 2. El flujo de código, paso a paso

```text
1. El cliente redirige el navegador al servidor de autorización con:
     response_type=code
     client_id=<público>
     redirect_uri=<registrada, exacta>
     scope=<alcances solicitados>
     state=<aleatorio, del cliente>
     code_challenge=<S256(code_verifier)>
     code_challenge_method=S256

2. El servidor autentica al usuario y le presenta los alcances.

3. El usuario aprueba (o rechaza alcances concretos).

4. El servidor redirige a redirect_uri con:
     code=<un solo uso, vida corta>
     state=<el mismo que llegó>

5. El cliente verifica que state coincide con el que envió.

6. El cliente llama al endpoint de token, POR CANAL DIRECTO:
     grant_type=authorization_code
     code=<el recibido>
     code_verifier=<el original, sin transformar>
     + autenticación del cliente

7. El servidor verifica que S256(code_verifier) == code_challenge
   y emite access_token acotado a los alcances CONCEDIDOS.
```

```text
POR QUÉ DOS ETAPAS
  la etapa 1-4 viaja por el NAVEGADOR: es observable
  la etapa 6-7 viaja por el CANAL DIRECTO: no lo es

  el código puede filtrarse (historial, referer, aplicación
  maliciosa registrada en el mismo esquema).
  El token nunca pasa por el navegador.
```

### 3. PKCE: el ataque que corta

```text
SIN PKCE, EN UN CLIENTE PÚBLICO

  1. la aplicación legítima no puede guardar un secreto:
     está instalada en el dispositivo del usuario
  2. una aplicación maliciosa registra el mismo esquema
     de redirección (myapp://callback)
  3. el sistema operativo entrega el código a la maliciosa
  4. la maliciosa canjea el código por un token:
     solo necesita client_id, que es público por definición
  5. obtiene acceso a los datos del cliente

CON PKCE
  el canje exige code_verifier, que la aplicación legítima
  generó y nunca envió por el navegador.
  El código robado no sirve para nada.

REGLA
  PKCE es obligatorio en clientes públicos
  y RECOMENDADO en todos, incluidos los confidenciales:
  también corta la inyección de código en clientes con secreto.
```

### 4. Qué añade OpenID Connect

```text
OAUTH DEVUELVE          un token de acceso: «puede leer X»
OPENID CONNECT AÑADE    un token de identidad: «el usuario es Y,
                        autenticado con el método M, a la hora H»

EL TOKEN DE IDENTIDAD ES UN JWT FIRMADO CON
  iss   quién lo emitió
  sub   identificador estable del usuario ANTE ESE EMISOR
  aud   para qué cliente se emitió
  exp   cuándo expira
  iat   cuándo se emitió
  nonce  liga el token a ESTA petición concreta
  acr / amr  nivel y método de autenticación

CUÁNDO HACE FALTA
  · cuando el producto necesita saber quién es el usuario
  · cuando debe comprobar QUÉ MÉTODO de autenticación se usó
    (relevante para autenticación reforzada, clase 11)

CUÁNDO NO
  · si solo necesitas leer datos consentidos, el token de acceso basta
```

### 5. Validación del token de identidad

```text
UN TOKEN DE IDENTIDAD SIN VALIDAR ES UN TEXTO CUALQUIERA

  1. verificar la firma con la clave pública del emisor,
     obtenida de su conjunto de claves publicado
  2. comprobar iss contra el emisor esperado
  3. comprobar aud contra el propio client_id
  4. comprobar exp y iat con margen de reloj acotado
  5. comprobar nonce contra el enviado en la petición
  6. si hay acr, comprobar que cumple el nivel exigido

OMITIR EL PASO 3 ES EL DEFECTO MÁS COMÚN
  sin verificar aud, un token emitido para OTRO cliente
  del mismo emisor se acepta como propio
```

### 6. Los siete defectos que aparecen en auditoría

| # | Defecto | Consecuencia |
|---:|---|---|
| 1 | Falta PKCE en cliente público | Robo de código |
| 2 | `redirect_uri` validada por prefijo | Redirección abierta |
| 3 | `state` no verificado | Falsificación de petición |
| 4 | Código reutilizable | Repetición |
| 5 | `aud` no comprobado en el token de identidad | Confusión de cliente |
| 6 | Token de acceso registrado en el log | Credencial en observabilidad |
| 7 | Alcance solicitado tratado como concedido | Escalada silenciosa |

## 🧮 Ejemplo guiado

**Situación.** Auditas la implementación de un proveedor de información. Estos son
los hallazgos de la revisión de código y de tráfico.

```text
HALLAZGO 1
  la aplicación móvil usa flujo de código sin code_challenge

HALLAZGO 2
  el servidor acepta redirect_uri que empiece por
  https://app.cuentasclaras.cl

HALLAZGO 3
  el token de acceso vive 24 horas

HALLAZGO 4
  el registro de aplicación contiene la línea:
  "token emitido: eyJ<...847 caracteres redactados en este material...>"

HALLAZGO 5
  el token de identidad se decodifica sin verificar firma
  «porque viene del servidor de autorización»
```

**Paso 1 — clasifica por explotabilidad.**

```text
EXPLOTABLE HOY, SIN CONDICIONES PREVIAS
  H2 · redirección abierta
  H5 · token de identidad sin verificar

EXPLOTABLE CON UNA CONDICIÓN
  H1 · requiere aplicación maliciosa en el dispositivo
  H4 · requiere acceso al sistema de registro

AGRAVANTE, NO VULNERABILIDAD POR SÍ SOLO
  H3 · amplía la ventana de cualquier robo de token
```

**Paso 2 — construye el ataque de H2.**

```text
URI REGISTRADA:  https://app.cuentasclaras.cl/callback
FILTRO:          startswith("https://app.cuentasclaras.cl")

URIs QUE PASAN EL FILTRO Y NO DEBERÍAN
  https://app.cuentasclaras.cl.atacante.io/callback
  https://app.cuentasclaras.cl@atacante.io/callback
  https://app.cuentasclaras.cl.evil/cb

LA PRIMERA ES UN DOMINIO DISTINTO
  el prefijo coincide; el registro de nombres, no.
  El código de autorización se entrega al atacante.
```

**Paso 3 — construye el ataque de H5.**

```text
SIN VERIFICAR FIRMA, UN TOKEN DE IDENTIDAD ES TEXTO EDITABLE

  el atacante construye:
    { "iss": "...", "sub": "cliente_victima", "aud": "...",
      "exp": <futuro> }
  lo codifica en base64url, pone cualquier firma
  y lo presenta.

  si el cliente solo decodifica, acepta la identidad
  de cualquier usuario que el atacante escriba.

  ESTO NO ES TEÓRICO: es el defecto que produce
  la suplantación completa de cuenta.
```

**Paso 4 — cuantifica el efecto de H3.**

```text
VENTANA DE UN TOKEN ROBADO

  con 24 h:      hasta 1 440 minutos de acceso
  con 10 min:    hasta 10 minutos

  con 158 llamadas por cliente y trimestre,
  y un historial de 24 meses accesible,
  10 minutos bastan para extraer el historial completo
  de una cuenta.

  → reducir la vida del token limita el DAÑO,
    no evita la EXTRACCIÓN
  → por eso H3 es agravante y no control suficiente:
    hace falta además límite de tasa (clase 8)
```

**Paso 5 — prioriza la remediación.**

```text
BLOQUEANTE, ANTES DE CUALQUIER OTRA COSA
  H5 · verificar firma, iss, aud, exp y nonce
  H2 · coincidencia exacta contra el conjunto registrado

URGENTE (mismo ciclo)
  H1 · PKCE obligatorio, con S256 y sin admitir "plain"
  H4 · dejar de registrar tokens; purgar el histórico

PLANIFICADO
  H3 · token de acceso a 10 minutos, refresco a 12 horas,
       con rotación del token de refresco

PRUEBA DE NO REGRESIÓN
  una prueba negativa por hallazgo, en la batería
  de conformidad del laboratorio 6
```

**Paso 6 — estima el coste de no hacerlo.**

```text
SUPUESTO: 380 000 clientes con consentimiento vigente

SI H5 SE EXPLOTA
  el atacante elige a qué cliente suplantar
  → no hay límite natural al alcance del incidente
  → el peor caso es «todos»

NO HAY CÁLCULO DE COSTE-BENEFICIO QUE APLICAR AQUÍ
  H5 no es un riesgo que se acepta con una reserva:
  es un defecto que se corrige antes de operar.

  Ese es el punto de la clase: hay controles que se
  evalúan por coste y controles que son condición de entrada.
```

**Interpreta:** cinco hallazgos, dos de ellos con el mismo patrón —**se confió en
que algo venía del sitio correcto sin comprobarlo**—. La firma y la coincidencia
exacta existen precisamente porque «viene del servidor de autorización» no es una
verificación.

## 🧭 Perspectivas

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Una pantalla de su banco | Si aprueba |
| Fintech | Complejidad de implementación | Si usa biblioteca certificada |
| Banco | Peticiones de terceros | Qué exige antes de habilitar |
| Infraestructura | Volumen en el endpoint de token | Capacidad y límite de tasa |
| Supervisor | Perfil de seguridad exigido | Qué certifica |
| Auditor | Código y tráfico | Los siete defectos |
| Sociedad | Suplantación de cuenta | Confianza en el modelo |

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Me llevó a la web de mi banco» | El cliente se autentica ante su institución | 17, clase 6 |
| «No le di mi clave a la app» | Delegación sin compartir credencial | 17, clase 1 |
| «Me pide autorizar cada tanto» | Vida del token y del consentimiento | 17, clase 5 |
| «Alguien entró a mi cuenta» | Token de identidad sin verificar | 17, clase 6 |

## ⚖️ Riesgos y controles

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Robo de código | Aplicación maliciosa en el dispositivo | PKCE con S256 |
| Redirección abierta | Validación por prefijo | Coincidencia exacta registrada |
| Confusión de cliente | `aud` no comprobado | Validación completa del token de identidad |
| Suplantación | Firma no verificada | Verificación con clave pública del emisor |
| Credencial en el log | Token registrado | Política de registro sin secretos |
| Escalada de alcance | Solicitado tratado como concedido | Token emitido sobre lo concedido |
| Ventana larga | Token de 24 h | Vida corta y rotación del refresco |

## 🧪 Práctica

En [`labs/lab-02.md`](../labs/lab-02.md):

1. Implementa el flujo completo con PKCE.
2. Escribe una prueba negativa por cada uno de los siete defectos.
3. Construye el ataque de redirección abierta y demuestra que tu filtro lo corta.
4. Valida un token de identidad con los seis pasos, y falla uno a propósito.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar OAuth para autenticar | Se confundió con OpenID Connect | Token de acceso ≠ identidad |
| PKCE solo en móvil | Se creyó innecesario en web | Aplícalo siempre |
| `redirect_uri` por prefijo | Se buscó flexibilidad | Coincidencia exacta |
| Decodificar sin verificar | «Viene del emisor» | Verifica firma, `iss`, `aud`, `exp`, `nonce` |
| Token de larga vida | Se evitó refrescar | Vida corta + rotación |
| Registrar el token | Depuración que quedó | Nunca secretos en el registro |
| Alcance solicitado = concedido | No se distinguieron | Emite sobre lo concedido |

## ❓ Preguntas de comprobación

1. ¿Por qué OAuth no es un protocolo de autenticación y qué se rompe si se usa
   como tal?
2. Describe el ataque que PKCE corta, con los cinco pasos.
3. ¿Qué URI pasa un filtro por prefijo y no debería? Explica por qué.
4. ¿Cuáles son los seis pasos de validación de un token de identidad y cuál se
   omite con más frecuencia?
5. ¿Por qué reducir la vida del token limita el daño pero no evita la extracción?

## 📥 Entregable

Guarda en `portfolio/parte-17/clase-06/`:

- el diagrama del flujo de código con los siete parámetros y su función;
- la descripción del ataque sin PKCE, paso a paso;
- tres URIs que pasarían un filtro por prefijo, con su explicación;
- los seis pasos de validación del token de identidad, con la prueba que
  escribiste para cada uno.

## 🔗 Referencias cruzadas

- **Viene de:** clase 5 (consentimiento); Parte 14, clase 8 (fraude digital).
- **Continúa en:** clase 7 (perfil financiero y firma), clase 11 (autenticación
  reforzada).
- **Se aplica en:** Parte 21, clase 11 (identidad en mercados tokenizados);
  Parte 23, clase 5 (identidad del banco digital).

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

- Internet Engineering Task Force. *RFC 6749 — The OAuth 2.0 Authorization Framework*. IETF. <https://www.rfc-editor.org/rfc/rfc6749>
- Internet Engineering Task Force. *RFC 7636 — Proof Key for Code Exchange by OAuth Public Clients*. IETF. <https://www.rfc-editor.org/rfc/rfc7636>
- Internet Engineering Task Force. *RFC 9700 — Best Current Practice for OAuth 2.0 Security*. IETF. <https://www.rfc-editor.org/rfc/rfc9700>
- OpenID Foundation. *OpenID Connect Core 1.0*. <https://openid.net/specs/openid-connect-core-1_0.html>
- Internet Engineering Task Force. *RFC 7519 — JSON Web Token (JWT)*. IETF. <https://www.rfc-editor.org/rfc/rfc7519>
- Verificación local: comprueba qué versión de cada especificación exige el anexo técnico vigente en tu jurisdicción; los perfiles se actualizan y los identificadores de RFC cambian al obsoletarse. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 05 · Consentimiento: creación, vigencia, renovación y revocación](05-consentimiento-ciclo-de-vida.md) | [Parte 17](../README.md) · [Programa](../../../SYLLABUS.md) | [07 · Financial-grade APIs, certificados y firma de mensajes →](07-financial-grade-apis-y-firma.md) |
<!-- gen:footer:end -->
