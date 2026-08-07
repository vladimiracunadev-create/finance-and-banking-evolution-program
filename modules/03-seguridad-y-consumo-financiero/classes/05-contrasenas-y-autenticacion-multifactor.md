---
part: 4
class: 5
title: "Contraseñas y autenticación multifactor"
level: fundamento
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 05 · Contraseñas y autenticación multifactor

> [← 04 · Estafas digitales](04-estafas-digitales.md) · [Índice de la parte](../README.md) · [06 · Comercio electrónico seguro →](06-comercio-electronico-seguro.md)

**Parte 04 — Seguridad y consumo financiero** · **Nivel:** Fundamento — sin conocimientos previos · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Construir un sistema de credenciales que resista tanto los ataques automatizados como el engaño, sin
exigir memoria heroica. Esta clase reemplaza las recomendaciones obsoletas —cambiar la clave cada 90
días, mezclar símbolos raros— por las prácticas que la evidencia respalda, y jerarquiza los factores
de autenticación por su resistencia real.

Las cuatro clases anteriores describieron las amenazas. Esta construye el control que las cubre a casi todas y que casi nadie tiene bien montado. No es una clase de recomendaciones: la fortaleza de una credencial se mide, y de esa medida sale qué hay que cambiar y en qué orden.

## 📚 Objetivos

Al finalizar podrás:

1. **Evaluar** la fortaleza de una credencial por su entropía, no por su apariencia.
2. **Implementar** un gestor de contraseñas con credencial maestra robusta.
3. **Jerarquizar** los factores de autenticación por resistencia al phishing.
4. **Configurar** el segundo factor en el orden correcto de prioridad.
5. **Diseñar** tu plan de recuperación sin crear una puerta trasera.

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

Los tres primeros términos miden la fortaleza y el modo en que se pierde; los cuatro últimos son los factores adicionales y su recuperación. La **recuperación** es la que hay que diseñar con más cuidado y la que casi nadie mira: es el camino más corto para entrar en una cuenta, y suele estar peor protegido que la contraseña.

| Concepto | Comprensión verificable |
|---|---|
| `entropía` | Medida de imprevisibilidad, en bits. Cada bit adicional duplica el esfuerzo de un ataque por fuerza bruta. |
| `frase de paso` | Varias palabras aleatorias. Alta entropía y memorizable; superior a una clave corta con símbolos. |
| `credencial reutilizada` | La misma clave en varios servicios. Una filtración compromete todos: efecto dominó. |
| `relleno de credenciales` | Ataque automatizado que prueba combinaciones filtradas en otros servicios. |
| `segundo factor` | Elemento adicional: algo que tienes o algo que eres. |
| `resistente al phishing` | Factor que no puede ser retransmitido por la víctima: llave de seguridad o clave de acceso vinculada al dominio. |
| `recuperación` | Mecanismo para volver a entrar. Es tan fuerte como su eslabón más débil. |

## 🧠 Modelo mental

Tu seguridad de credenciales tiene forma de **árbol con una raíz**:

```text
                    correo principal
                   /       |        \
              banco     redes     comercios
```

Quien controla el correo restablece todo lo que cuelga de él. Por eso el orden de refuerzo no es
"primero el banco": es **primero el correo**, con el factor más fuerte disponible, y después el resto.

## 📖 Desarrollo

### 1. Entropía: qué hace fuerte a una credencial

La fortaleza de una contraseña no depende de tener símbolos raros sino de cuántas combinaciones posibles hay. El cálculo siguiente lo cuantifica, y su conclusión contradice buena parte de los consejos habituales.

```text
entropía ≈ longitud × log₂(tamaño del alfabeto)
```

| Credencial | Entropía aprox. | Resistencia relativa |
|---|---:|---|
| `Pedro123` | 27 bits | Trivial |
| `P3dr0!23` | 42 bits | Baja (patrón predecible) |
| `Xk9#mQ2v` | 52 bits | Media, imposible de recordar |
| `caballo-batería-grapa-correcto` | 66 bits | **Alta y memorizable** |
| `tortuga verde plaza lunes cobre` | 82 bits | Muy alta |

El hallazgo contraintuitivo: **la longitud aporta más que la complejidad de caracteres**. Cuatro
palabras aleatorias superan a ocho caracteres con símbolos, y se recuerdan sin esfuerzo. La condición
es que las palabras sean **elegidas al azar**, no una frase con sentido: una frase de una canción
tiene entropía cercana a cero.

Prácticas obsoletas que conviene abandonar:

```text
✗ cambiar la contraseña cada 90 días sin motivo  → produce claves peores y predecibles
✗ exigir un símbolo y un número                  → produce "Password1!" en todo el mundo
✗ preguntas de seguridad                         → sus respuestas son públicas o adivinables
✓ contraseñas largas, únicas por servicio, cambiadas solo ante indicio de compromiso
```

### 2. Gestor de contraseñas

Un gestor resuelve el problema real, que no es recordar una contraseña buena sino tener cientos distintas. La comparación siguiente recoge las opciones con sus supuestos de confianza.

```text
credencial maestra    frase de paso de 5+ palabras aleatorias, NUNCA reutilizada
                      memorizada, no escrita en el propio gestor
segundo factor        activado sobre el gestor
copia de seguridad    exportación cifrada, guardada fuera de línea
recuperación          código de emergencia impreso y guardado físicamente
```

La objeción habitual —"si comprometen el gestor, pierdo todo"— es real y aun así el balance es
favorable: sin gestor, la práctica dominante es reutilizar credenciales, lo que garantiza el efecto
dominó ante cualquier filtración de un servicio de terceros. El gestor concentra el riesgo en un punto
que **puedes proteger bien**, en lugar de distribuirlo en cincuenta que no puedes.

### 3. Jerarquía de factores

No todos los segundos factores protegen igual, y la diferencia entre ellos es grande frente al phishing. La tabla los ordena por resistencia real.

| Factor | Resistente al phishing | Comentario |
|---|---|---|
| Llave de seguridad física (FIDO2) | **Sí** | Verifica el dominio; no puede retransmitirse |
| Clave de acceso (passkey) | **Sí** | Vinculada al dominio y al dispositivo |
| Aplicación de autenticación (TOTP) | No | El código puede ser entregado por engaño |
| Notificación push con número | Parcial | Mejor que push simple; aún engañable |
| Código por mensaje de texto | No | Vulnerable a suplantación de línea y a engaño |
| Pregunta de seguridad | No | No es un factor real |

**Todos los factores de las filas 3 a 5 pueden ser vulnerados por el ataque de la clase 2**, porque la
víctima puede entregar el código. Solo los dos primeros son estructuralmente resistentes, porque la
verificación incluye el dominio y el usuario no puede transmitirla aunque quiera.

### 4. Orden de configuración

El orden en que se configuran las cuentas importa, porque unas dan acceso a otras. La secuencia siguiente empieza por el correo, que es la llave de casi todo lo demás.

```text
1. correo principal        → el factor más fuerte disponible
2. gestor de contraseñas   → segundo factor
3. banca en línea          → segundo factor + límites por canal
4. telefonía móvil         → clave de acceso a la cuenta del operador
5. redes sociales          → segundo factor
6. comercios y servicios   → contraseñas únicas
```

El punto 4 suele omitirse y es crítico: si el atacante consigue duplicar tu línea telefónica, recibe
los códigos por mensaje de texto de todos los servicios. Solicitar a tu operador una clave de
seguridad para cambios de línea cierra ese vector.

### 5. Recuperación sin puerta trasera

Una recuperación mal diseñada anula toda la protección anterior. Los criterios siguientes la cierran sin dejar a nadie fuera de su propia cuenta.

```text
✓ códigos de recuperación impresos, guardados físicamente en un lugar seguro
✓ segunda llave de seguridad física, guardada aparte
✓ contacto de recuperación de confianza, si el servicio lo permite
✗ preguntas de seguridad con respuestas verdaderas
✗ correo de recuperación con seguridad menor que la cuenta principal
✗ códigos de recuperación guardados en el mismo gestor que protegen
```

Los tres puntos negativos son puertas traseras: por más fuerte que sea la puerta principal, el atacante
entrará por la más débil. Un correo de recuperación sin segundo factor anula la protección de la
cuenta que recupera.

## 🧮 Ejemplo guiado

**Situación.** Valeria usa cuatro contraseñas para 43 servicios y recibe el aviso de que un comercio
donde compró fue vulnerado.

**Paso 1 — evalúa el alcance.**

```text
clave filtrada: "Valeria2019!"
¿en cuántos servicios está esa clave? → 14
¿está en su correo principal?         → SÍ  ← crítico
¿está en su banco?                    → sí, con una variante
```

El compromiso de un comercio se convierte en compromiso de su correo y su banco, sin que el atacante
tuviera que vulnerar ninguno de los dos. Esa es la mecánica del relleno de credenciales.

**Paso 2 — orden de acción, por criticidad.**

```text
minuto 0   correo principal: nueva frase de paso + llave de seguridad
minuto 10  banca en línea: nueva clave + segundo factor + límites por canal
minuto 20  operador de telefonía: clave para cambios de línea
minuto 30  gestor de contraseñas instalado, credencial maestra de 5 palabras
hora 1–3   los 41 servicios restantes, con claves únicas generadas
```

**Paso 3 — la credencial maestra.**

```text
generada al azar: "cobre lunes trébol quince sardina"
entropía ≈ 82 bits
memorizada mediante repetición espaciada durante una semana
código de recuperación impreso y guardado físicamente
```

**Paso 4 — jerarquía aplicada.**

| Servicio | Factor elegido | Motivo |
|---|---|---|
| Correo principal | Llave de seguridad | Es la raíz del árbol |
| Gestor | Llave de seguridad (segunda unidad) | Concentra todo lo demás |
| Banca | App de autenticación + límites | El banco no ofrece FIDO2 |
| Telefonía | Clave de operador | Protege el canal de los códigos |
| Resto | App de autenticación | Suficiente para el riesgo |

**Paso 5 — cuantifica la mejora.**

```text
antes:   una filtración cualquiera comprometía 14 servicios, incluidos correo y banco
después: una filtración compromete exactamente 1 servicio
         el correo y el gestor son resistentes al phishing
```

**Paso 6 — el punto que suele omitirse.** Valeria también revisa las **sesiones activas** y las
**aplicaciones autorizadas** de su correo:

```text
sesiones activas         9 → cierra 7 desconocidas o antiguas
aplicaciones con acceso  12 → revoca 8 que ya no usa
```

Cambiar la contraseña no cierra sesiones ya iniciadas ni revoca tokens de aplicaciones. Sin este paso,
el atacante puede conservar acceso pese al cambio de credencial.

**Interpreta:** el trabajo total fueron unas tres horas. El cambio estructural es que Valeria pasó de
un sistema donde **cualquier eslabón comprometía todo** a uno donde cada servicio está aislado y los
dos nodos críticos son resistentes al engaño.

## 🏦 Del cliente al banco

El cliente elige una contraseña y el banco gestiona el riesgo de suplantación de todos sus clientes a la vez. La tabla enfrenta las dos lecturas y explica por qué la entidad impone reglas que parecen arbitrarias.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| Segundo factor | Autenticación reforzada exigida por norma | 14, clase 4 |
| Clave de acceso (passkey) | Reduce fraude por suplantación de credenciales | 14, clase 11 |
| Códigos por mensaje de texto | Factor de menor resistencia; en revisión regulatoria | 12, clase 10 |
| Sesiones activas | Control de acceso y trazabilidad | 11, clase 8 |

## 🧪 Práctica

El laboratorio pide medir la entropía de credenciales sintéticas y ordenar las cuentas propias por criticidad. El resultado suele ser que las cuentas peor protegidas son las que dan acceso a las demás.

En `labs/lab-03.md`, sección de credenciales:

1. Calcula la entropía de cinco credenciales que uses y clasifícalas.
2. Instala un gestor, define una frase de paso de cinco palabras aleatorias y activa el segundo factor.
3. Configura los factores en el orden de prioridad de la clase y documenta la evidencia.
4. Revisa sesiones activas y aplicaciones autorizadas en tu correo, y revoca lo innecesario.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen accesos comprometidos sin que la contraseña fuera débil. Las causas son la reutilización y una recuperación mal configurada.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Una filtración compromete varios servicios | Credenciales reutilizadas | Una credencial única por servicio, con gestor. |
| La contraseña "compleja" es débil | Patrón predecible | Prioriza longitud y aleatoriedad sobre símbolos. |
| El segundo factor no evitó el fraude | Factor retransmisible entregado por engaño | Usa factores resistentes al phishing donde se pueda. |
| Se refuerza el banco y no el correo | Orden invertido | El correo es la raíz: refuérzalo primero. |
| Cambiar la clave no expulsó al atacante | Sesiones y tokens seguían activos | Cierra sesiones y revoca aplicaciones. |
| Los códigos de recuperación están en el gestor | Dependencia circular | Guárdalos impresos, fuera de línea. |

## ❓ Preguntas de comprobación

1. ¿Por qué una frase de cuatro palabras aleatorias supera a ocho caracteres con símbolos?
2. ¿Qué factores son resistentes al phishing y por qué los demás no lo son?
3. ¿Por qué se refuerza primero el correo y no la banca en línea?
4. ¿Qué debe hacerse además de cambiar la contraseña tras un compromiso?
5. Nombra tres mecanismos de recuperación que constituyen una puerta trasera.

## 📥 Entregable

Guarda en `portfolio/parte-04/clase-05/`:

- el cálculo de entropía de cinco credenciales con su clasificación;
- la evidencia de instalación del gestor y de la credencial maestra (sin revelarla);
- la tabla de factores configurados por servicio en orden de prioridad;
- el registro de sesiones cerradas y aplicaciones revocadas.

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

- NIST (2017, rev. 2024). *SP 800-63B: Digital Identity Guidelines — Authentication and Lifecycle Management*. Recomendaciones vigentes sobre longitud, rotación y factores. <https://pages.nist.gov/800-63-3/>
- FIDO Alliance (2023). *Passkeys: Passwordless Authentication Specifications*. Fundamento de la resistencia al phishing por vinculación de dominio. <https://fidoalliance.org/>
- Bonneau, J. et al. (2012). "The Quest to Replace Passwords". *IEEE Symposium on Security and Privacy*. Marco comparativo de esquemas de autenticación.
- Wheeler, D. (2016). "zxcvbn: Low-Budget Password Strength Estimation". *USENIX Security*. Medición realista de fortaleza de contraseñas.
- ENISA (2024). *Threat Landscape*. Agencia de la Unión Europea para la Ciberseguridad. Relleno de credenciales y suplantación de línea telefónica.
- Verificación local: consulta qué factores de autenticación ofrece tu banco y si tu operador de telefonía permite establecer una clave para cambios de línea.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 04 · Estafas digitales](04-estafas-digitales.md) | [Parte 04](../README.md) · [Programa](../../../SYLLABUS.md) | [06 · Comercio electrónico seguro →](06-comercio-electronico-seguro.md) |
<!-- gen:footer:end -->
