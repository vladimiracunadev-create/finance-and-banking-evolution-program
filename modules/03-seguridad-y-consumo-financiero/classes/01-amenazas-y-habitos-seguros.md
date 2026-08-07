---
part: 4
class: 1
title: "Amenazas y hábitos seguros"
level: fundamento
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 01 · Amenazas y hábitos seguros

> [← Índice de la parte](../README.md) · [Índice de la parte](../README.md) · [02 · Phishing y suplantación →](02-phishing-y-suplantacion.md)

**Parte 04 — Seguridad y consumo financiero** · **Nivel:** Fundamento — sin conocimientos previos · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Construir el mapa de amenazas que enfrenta cualquier persona con productos financieros, y convertirlo
en un conjunto acotado de hábitos que efectivamente se sostienen. La seguridad financiera personal no
se logra con vigilancia permanente —que nadie mantiene— sino con controles que funcionan solos y con
un pequeño número de reglas ejecutables bajo presión.

## 📚 Objetivos

Al finalizar podrás:

1. **Clasificar** las amenazas financieras por vector y por probabilidad realista.
2. **Aplicar** el marco identificar–proteger–detectar–responder–recuperar a tu situación.
3. **Configurar** los siete controles que más reducen la pérdida esperada.
4. **Reconocer** los principios de manipulación que usan los fraudes.
5. **Definir** tu superficie de exposición y reducirla de forma medible.

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

| Concepto | Comprensión verificable |
|---|---|
| `vector de ataque` | Camino por el que llega la amenaza: mensaje, llamada, sitio falso, dispositivo, persona conocida. |
| `superficie de exposición` | Conjunto de cuentas, dispositivos, cupos y datos que un atacante podría alcanzar. Se puede medir y reducir. |
| `pérdida máxima` | Lo peor que puede pasar con los controles actuales. Es la métrica que importa, no la probabilidad. |
| `control preventivo` | Impide el evento: límites, doble factor, cupos reducidos. |
| `control detectivo` | Avisa que ocurrió: notificaciones, revisión de cartola. |
| `control correctivo` | Reduce el daño después: bloqueo, desconocimiento, denuncia. |
| `ingeniería social` | Manipulación de la persona en lugar del sistema. Es el vector dominante en fraude financiero. |

## 🧠 Modelo mental

Los sistemas bancarios modernos son difíciles de vulnerar técnicamente. Por eso **el objetivo del
atacante eres tú**:

```text
atacar el sistema     → criptografía, monitoreo, capas de control   → costoso
atacar a la persona   → un mensaje bien redactado                   → barato
```

De ahí la consecuencia práctica: la mayor parte de tu esfuerzo de seguridad no debe ir a "protegerse
de hackers", sino a **no autorizar tú mismo la operación** que el atacante necesita.

## 📖 Desarrollo

### 1. Mapa de amenazas por vector

| Vector | Ejemplo | Probabilidad relativa | Pérdida típica |
|---|---|---|---|
| Mensaje o correo suplantado | Enlace a sitio falso del banco | **Muy alta** | Media a alta |
| Llamada telefónica | "Departamento de fraude" que pide claves | **Muy alta** | Alta |
| Sitio de comercio falso | Tienda inexistente en redes | Alta | Baja a media |
| Aplicación maliciosa | App que captura credenciales | Media | Alta |
| Robo físico de tarjeta o teléfono | Hurto con acceso a la app | Media | Media |
| Filtración de datos de un tercero | Comercio o servicio comprometido | Alta | Variable |
| Fraude de inversión | Esquema piramidal, rentabilidad garantizada | Media | **Muy alta** |
| Persona conocida | Uso indebido de acceso o confianza | Baja | Alta |

La combinación que produce más pérdida en términos absolutos: **fraude de inversión**, porque
involucra montos grandes y rara vez es recuperable. La que produce más incidentes: **mensajes y
llamadas suplantadas**.

### 2. El marco de cinco funciones

Adaptado del marco de ciberseguridad del NIST a la situación de una persona:

```text
IDENTIFICAR  ¿qué tengo, dónde, con qué acceso?      → inventario
PROTEGER     ¿qué impide que ocurra?                 → límites, doble factor, cupos
DETECTAR     ¿cómo me entero rápido?                 → notificaciones, revisión periódica
RESPONDER    ¿qué hago en la primera hora?           → protocolo escrito
RECUPERAR    ¿cómo vuelvo a la normalidad?           → reemisión, reclamo, denuncia
```

La mayoría de las personas trabaja solo en "proteger" y no tiene nada en "detectar" ni en
"responder". El resultado típico: se enteran tarde y improvisan.

### 3. Los siete controles de mayor impacto

| # | Control | Reduce | Costo |
|---:|---|---|---|
| 1 | Segundo factor en banca y correo | Acceso no autorizado | 0 |
| 2 | Notificación instantánea de todo movimiento | Tiempo de detección | 0 |
| 3 | Límites por canal (internet, extranjero, giro) | Pérdida máxima | 0 |
| 4 | Cupos de crédito reducidos al uso real | Pérdida máxima | 0 |
| 5 | Correo exclusivo para banca, distinto del público | Superficie de exposición | 0 |
| 6 | Actualización automática del sistema y del navegador | Explotación técnica | 0 |
| 7 | Regla de los 10 minutos ante cualquier urgencia | Ingeniería social | 0 |

Los siete cuestan cero pesos y se configuran en menos de una hora. El séptimo es el más difícil y el
más valioso: **ninguna operación financiera legítima exige decidir en menos de diez minutos**.

### 4. Los principios que explotan los fraudes

| Principio | Cómo se usa | Contramedida |
|---|---|---|
| Autoridad | "Le habla el departamento de fraude" | Cortar y llamar tú al número oficial |
| Urgencia | "Su cuenta será bloqueada en 15 minutos" | Regla de los 10 minutos |
| Escasez | "Solo quedan 3 cupos de inversión" | La escasez artificial es una bandera roja |
| Reciprocidad | Un regalo o "beneficio" previo | El beneficio no obliga a nada |
| Prueba social | "Muchos vecinos ya invirtieron" | Verificar en el registro oficial |
| Simpatía | Contacto amable y prolongado | La confianza no reemplaza la verificación |
| Compromiso | "Usted ya aceptó el primer paso" | Se puede detener en cualquier punto |

Reconocer el principio en uso durante la conversación es la defensa más eficaz, porque estos
mecanismos funcionan sobre todo cuando no se los ve.

### 5. Medir y reducir tu superficie

```text
superficie = Σ (cuentas con acceso remoto)
           + Σ (cupos de crédito disponibles)
           + Σ (dispositivos con sesión iniciada)
           + Σ (servicios con tu tarjeta guardada)
           + Σ (datos personales publicados)
```

Ejemplo de reducción en una tarde:

| Elemento | Antes | Después | Efecto |
|---|---:|---:|---|
| Cupos de crédito | 8 400 000 | 2 000 000 | Pérdida máxima −76 % |
| Dispositivos con sesión | 6 | 2 | Menos puntos de compromiso |
| Servicios con tarjeta guardada | 14 | 3 | Menos filtraciones posibles |
| Cuentas con la misma contraseña | 11 | 0 | Elimina el efecto dominó |
| Límite diario de transferencia | Sin límite | 500 000 | Acota la pérdida |

## 🧮 Ejemplo guiado

**Situación.** Camilo recibe un mensaje: *"Banco XX: detectamos una compra de $890.000 en el
extranjero. Si no la reconoce, ingrese aquí para anularla: bancoxx-seguridad.cl"*. Dos minutos después
recibe una llamada de alguien que se identifica como ejecutivo de fraude del banco.

**Paso 1 — identifica los principios en uso.**

```text
autoridad   "ejecutivo de fraude del banco"
urgencia    monto alto + acción inmediata
miedo       pérdida ya ocurrida
compromiso  el mensaje pide un primer paso pequeño (ingresar al enlace)
```

Cuatro principios simultáneos es, por sí solo, una señal: una comunicación legítima rara vez los
combina.

**Paso 2 — verifica el dominio.**

```text
dominio del mensaje   bancoxx-seguridad.cl
dominio oficial       bancoxx.cl
```

Un guion y un subdominio distinto. Regla: **el dominio real es lo que está inmediatamente antes del
primer `/` y después del último punto antes de él**. `bancoxx-seguridad.cl` no pertenece a `bancoxx.cl`.

**Paso 3 — aplica la regla de los 10 minutos.**

```text
corta la llamada
NO usa el enlace
llama al número impreso en el reverso de su tarjeta
```

**Paso 4 — verifica en el canal oficial.** Al ingresar por la aplicación, comprueba que **no existe
ninguna compra de 890 000**. El mensaje era el ataque completo.

**Paso 5 — qué habría pasado si seguía el enlace.**

```text
1. sitio idéntico al del banco solicita usuario y clave
2. mientras Camilo los ingresa, el atacante los usa en el sitio real
3. el banco envía un código de verificación al teléfono de Camilo
4. el sitio falso pide ese código "para confirmar la anulación"
5. el atacante lo usa y transfiere el saldo disponible
```

El segundo factor **no protege** si la persona lo entrega. Por eso la regla operativa es: *un código
de verificación autoriza una operación; si no sabes exactamente cuál, no lo entregues a nadie, por
ningún canal, nunca.*

**Paso 6 — refuerza.** Camilo configura límite de transferencia de 500 000 diarios y notificaciones
instantáneas. Con eso, si en el futuro cae en un engaño similar:

```text
pérdida máxima antes:  todo el saldo disponible (3 200 000)
pérdida máxima después: 500 000, con aviso instantáneo
```

**Interpreta:** el control que más protege a Camilo no es "no caer en engaños" —nadie puede
garantizarlo— sino **haber acotado por adelantado lo que puede perderse**. La seguridad efectiva
supone que en algún momento el engaño va a funcionar.

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| Mensaje sospechoso | Campaña de suplantación de marca detectada y bloqueada | 12, clase 15 |
| Límite por canal | Control de riesgo operacional del emisor | 11, clase 7 |
| Notificación instantánea | Reduce el tiempo de detección y el costo del fraude | 14, clase 11 |
| Operación autorizada por el cliente | Caso complejo: hay autorización formal, pero mediada por engaño | 12, clase 15 |

## 🧪 Práctica

En `labs/lab-01.md`:

1. Construye tu mapa de amenazas con probabilidad y pérdida estimada por vector.
2. Mide tu superficie de exposición con las cinco dimensiones.
3. Configura los siete controles y documenta la evidencia de cada uno.
4. Analiza tres mensajes sospechosos reales identificando los principios de manipulación.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| "A mí no me va a pasar" | Se subestima la probabilidad | Diseña suponiendo que ocurrirá y acota la pérdida. |
| Se entrega un código de verificación | No se comprendió su función | Un código autoriza una operación; nunca se comparte. |
| Se responde por el mismo canal del mensaje | El canal es del atacante | Verifica siempre por un canal que tú inicies. |
| Cupos altos sin uso | Superficie innecesaria | Reduce cupos al uso real. |
| Se detecta el fraude días después | Sin notificaciones | Activa alertas instantáneas. |
| Se confía por la amabilidad del contacto | Principio de simpatía | La confianza no sustituye la verificación. |

## ❓ Preguntas de comprobación

1. ¿Por qué el atacante prefiere a la persona antes que al sistema?
2. Nombra las cinco funciones del marco y qué haces tú en cada una.
3. ¿Cuáles son los siete controles de mayor impacto y cuánto cuestan?
4. Identifica tres principios de manipulación en un mensaje de fraude real.
5. ¿Por qué el segundo factor no protege si se entrega el código?

## 📥 Entregable

Guarda en `portfolio/parte-04/clase-01/`:

- tu mapa de amenazas por vector con probabilidad y pérdida;
- la medición de tu superficie de exposición antes y después;
- la evidencia de configuración de los siete controles;
- el análisis de tres mensajes sospechosos con los principios identificados.

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

- NIST (2024). *Cybersecurity Framework 2.0*. National Institute of Standards and Technology. Funciones identificar, proteger, detectar, responder y recuperar. <https://www.nist.gov/cyberframework>
- Cialdini, R. (2021). *Influence: The Psychology of Persuasion* (edición ampliada). Harper Business. Los siete principios de influencia usados en ingeniería social.
- Mitnick, K. y Simon, W. (2002). *The Art of Deception*. Wiley. Técnicas de ingeniería social documentadas.
- ENISA (2024). *Threat Landscape*. Agencia de la Unión Europea para la Ciberseguridad. Vectores predominantes y tendencias. <https://www.enisa.europa.eu/>
- Europol (2024). *Internet Organised Crime Threat Assessment (IOCTA)*. Europol. Fraude financiero y suplantación.
- Verificación local: consulta los canales oficiales de denuncia de fraude de tu país y los plazos legales de respuesta del emisor ante operaciones no reconocidas.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← Índice de la parte](../README.md) | [Parte 04](../README.md) · [Programa](../../../SYLLABUS.md) | [02 · Phishing y suplantación →](02-phishing-y-suplantacion.md) |
<!-- gen:footer:end -->
