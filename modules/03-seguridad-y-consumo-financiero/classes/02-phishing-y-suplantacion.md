---
part: 4
class: 2
title: "Phishing y suplantación"
level: fundamento
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 02 · Phishing y suplantación

> [← 01 · Amenazas y hábitos seguros](01-amenazas-y-habitos-seguros.md) · [Índice de la parte](../README.md) · [03 · Robo de identidad →](03-robo-de-identidad.md)

**Parte 04 — Seguridad y consumo financiero** · **Nivel:** Fundamento — sin conocimientos previos · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Aprender a detectar suplantación en los cuatro canales por los que llega —correo, mensaje de texto,
llamada y aplicaciones de mensajería— con un método que funciona bajo presión y sin conocimientos
técnicos. Esta clase entrega el procedimiento de verificación de dominio, la regla del canal inverso y
el análisis de casos reales.

## 📚 Objetivos

Al finalizar podrás:

1. **Analizar** un dominio y determinar si pertenece a la organización que dice ser.
2. **Aplicar** la regla del canal inverso en cualquier contacto no solicitado.
3. **Reconocer** las variantes: correo, mensaje de texto, llamada, código QR y mensajería.
4. **Explicar** por qué el segundo factor puede ser vulnerado con engaño.
5. **Responder** correctamente cuando ya entregaste información.

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
| `phishing` | Suplantación de una entidad de confianza para obtener credenciales o autorizaciones. |
| `smishing` | Phishing por mensaje de texto. Aprovecha la brevedad y la falta de contexto visual. |
| `vishing` | Phishing por llamada de voz. Usa autoridad y urgencia en tiempo real. |
| `dominio registrable` | Los dos últimos componentes antes del primer `/`. Es lo único que identifica al titular real. |
| `homógrafo` | Dominio visualmente similar usando caracteres distintos o dígitos por letras. |
| `canal inverso` | Verificar por un medio que **tú** inicias, con datos que tú ya tenías. |
| `phishing en tiempo real` | El atacante usa tus datos en el sitio verdadero mientras los escribes en el falso, incluido el segundo factor. |

## 🧠 Modelo mental

Toda suplantación depende de que **verifiques dentro del canal del atacante**:

```text
canal del atacante:  mensaje → enlace → sitio → teléfono que aparece en el sitio
                     todo lo que verifiques ahí lo controla él

canal inverso:       cierras todo → tomas tu tarjeta → llamas al número impreso
                     nada de eso lo controla él
```

Esta sola regla neutraliza la mayoría de los ataques, sin necesidad de detectar nada sofisticado.

## 📖 Desarrollo

### 1. Leer un dominio correctamente

```text
https://www.bancoxx.cl.verificacion-segura.net/login
                                ↑
        el dominio real es verificacion-segura.net
```

Método en tres pasos:

```text
1. localiza el primer "/" después de "https://"
2. mira lo que hay inmediatamente antes de ese "/"
3. toma los DOS últimos componentes separados por punto: ese es el titular
```

| URL | Dominio real | ¿Legítimo si el banco es bancoxx.cl? |
|---|---|---|
| `bancoxx.cl/personas` | bancoxx.cl | Sí |
| `www.bancoxx.cl/login` | bancoxx.cl | Sí |
| `bancoxx-seguridad.cl` | bancoxx-seguridad.cl | **No** |
| `bancoxx.cl.seguro.net` | seguro.net | **No** |
| `bancoxx.com.mx-pagos.info` | mx-pagos.info | **No** |
| `bancoxx.cl@evil.net` | evil.net | **No** |
| `bancoxx.c1` | bancoxx.c1 | **No** (dígito uno) |

La última fila ilustra el homógrafo: `c1` en lugar de `cl`, `rn` en lugar de `m`, `0` en lugar de `o`.
A tamaño de letra de teléfono son indistinguibles.

### 2. Señales por canal

**Correo:**

```text
· el remitente visible no coincide con la dirección real (revisa la dirección completa)
· saludo genérico o con tu correo en vez de tu nombre
· el enlace mostrado difiere del destino real
· archivo adjunto inesperado
· dominio del remitente distinto del oficial
```

**Mensaje de texto:**

```text
· acortadores de enlaces (el destino no se puede leer)
· remitente numérico cuando la entidad usa nombre corto
· solicitud de acción inmediata
· mensaje que llega justo después de una compra real (indica filtración del comercio)
```

**Llamada:**

```text
· conocen datos parciales tuyos (nombre, últimos dígitos): NO prueba legitimidad,
  esos datos circulan en filtraciones
· piden clave, código de verificación o que instales una aplicación
· insisten en no cortar la llamada
· ofrecen "transferir a una cuenta segura del banco": no existe tal cosa
```

**Código QR:** el destino no es visible antes de escanear. Nunca escanees un QR pegado sobre otro, ni
uno recibido por mensaje para "pagar" o "verificar".

### 3. Por qué el segundo factor puede caer

```text
14:02:10  víctima entra al sitio falso y escribe usuario y clave
14:02:14  atacante los ingresa en el sitio REAL
14:02:16  el banco envía un código al teléfono de la víctima
14:02:20  el sitio falso muestra: "ingrese el código que le enviamos"
14:02:28  víctima escribe el código
14:02:31  atacante lo usa en el sitio real → sesión iniciada
```

El segundo factor cumplió su función: el banco verificó que quien tenía el teléfono autorizó. El
problema es que la víctima autorizó una operación que no comprendía. De ahí la regla:

> Un código de verificación **autoriza una operación específica**. Si el mensaje del código describe
> una operación que tú no iniciaste, no lo ingreses en ningún lado y llama al banco.

Los códigos legítimos incluyen la descripción de la operación. Leerla es el control que falta.

### 4. Qué hacer si ya entregaste datos

```text
minuto 0–5
  1. bloquea tarjetas y cuentas desde la aplicación oficial
  2. cambia la clave de banca en línea desde un dispositivo distinto
  3. cambia la clave del correo asociado (es la llave maestra)

minuto 5–60
  4. llama al banco por el número del reverso de la tarjeta
  5. desconoce formalmente cualquier operación no reconocida; anota el número de caso
  6. revisa y cierra sesiones activas en la banca en línea

día 1–3
  7. denuncia ante la autoridad competente
  8. revisa tu informe de deudas: pueden haberse solicitado créditos a tu nombre
  9. activa alertas y reduce límites
```

El paso 3 es el más olvidado y el más importante: con acceso al correo, el atacante puede restablecer
casi cualquier otra credencial.

### 5. La segunda ola

Tras un fraude, es habitual recibir contacto de supuestos "recuperadores de fondos" o de un "área
especial del banco". Es la misma organización, aprovechando que la víctima está alterada y motivada.

```text
señales de la segunda ola:
· contactan ellos, poco después del incidente
· conocen detalles del fraude (porque lo cometieron)
· piden un pago anticipado para "recuperar" el dinero
· piden instalar una aplicación de asistencia remota
```

Ninguna entidad legítima cobra por adelantado para devolverte tu dinero.

## 🧮 Ejemplo guiado

**Situación.** Marta compra en una tienda en línea. Dos horas después recibe un mensaje: *"Su pedido
n.º 48812 no pudo despacharse por un problema de dirección. Actualice sus datos: t.co/xY7kL"*.

**Paso 1 — evalúa la coincidencia temporal.** El mensaje llega justo después de una compra real y cita
un número de pedido. Esto **no** prueba legitimidad: indica que los datos del comercio fueron
filtrados o que el atacante envía mensajes masivos y acertó por probabilidad.

**Paso 2 — analiza el enlace.** Es un acortador: el destino no es legible. Regla: **un acortador en
una comunicación financiera o logística es motivo suficiente para no seguir el enlace**.

**Paso 3 — aplica el canal inverso.**

```text
✗ no toca el enlace
✓ abre el sitio de la tienda escribiendo la dirección conocida
✓ entra a "mis pedidos" con su cuenta
→ el pedido #48812 figura como "en preparación", sin ninguna incidencia
```

**Paso 4 — reconstruye el ataque que evitó.**

```text
1. formulario que pide dirección y "confirmar método de pago"
2. solicita número de tarjeta, vencimiento y código de seguridad
3. el atacante intenta una compra en línea con esos datos
4. el banco envía código de verificación a Marta
5. el sitio falso lo pide "para validar la dirección"
6. compra autorizada
```

**Paso 5 — la parte que la mayoría omite: denunciar.**

```text
· reporta el mensaje al canal de fraude de su banco y de la tienda
· si el número de pedido era real, informa a la tienda de una posible filtración
```

Ese aviso permite a la tienda investigar y advertir a otros clientes. Es la parte del proceso que
convierte una defensa individual en una colectiva.

**Paso 6 — interpreta.** Marta no detectó nada técnico: aplicó una regla —**verificar por el canal que
ella inicia**— que funciona sin saber leer un encabezado de correo ni analizar un certificado. Esa es
la propiedad que hace útil el método: es ejecutable por cualquier persona, bajo presión y desde el
teléfono.

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| Mensaje suplantado | Uso indebido de marca; se gestiona bloqueo del dominio | 12, clase 15 |
| Código de verificación | Autenticación reforzada exigida por norma | 14, clase 4 |
| Operación autorizada bajo engaño | Zona gris: hay autorización, mediada por fraude | 12, clase 15 |
| Reporte del cliente | Insumo para el sistema de detección | 14, clase 11 |

## 🧪 Práctica

En `labs/lab-02.md`:

1. Analiza diez URL y determina el dominio registrable de cada una.
2. Recolecta tres mensajes sospechosos reales y clasifica sus señales por canal.
3. Escribe tu procedimiento de canal inverso con números y direcciones oficiales verificadas.
4. Documenta el protocolo de respuesta si ya entregaste datos.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se confía porque conocen datos personales | Se asume que solo el banco los tiene | Esos datos circulan en filtraciones. |
| Se verifica llamando al número del mensaje | Verificación dentro del canal del atacante | Usa el número del reverso de tu tarjeta. |
| Se entrega el código de verificación | No se leyó la operación que autoriza | Lee siempre qué autoriza el código. |
| Se sigue un enlace acortado | El destino no era legible | Escribe tú la dirección conocida. |
| Se cambia la clave del banco pero no la del correo | El correo es la llave maestra | Cambia ambas, desde un dispositivo limpio. |
| Se atiende al "recuperador de fondos" | Segunda ola del mismo fraude | Nadie cobra por adelantado para devolverte tu dinero. |

## ❓ Preguntas de comprobación

1. ¿Cuál es el dominio real de `https://bancoxx.cl.verificar.net/login` y por qué?
2. ¿Qué es la regla del canal inverso y por qué neutraliza la mayoría de los ataques?
3. Explica paso a paso cómo un atacante vulnera un segundo factor con engaño.
4. ¿Cuál es el primer cambio de credencial que debes hacer y por qué?
5. ¿Cómo reconoces la segunda ola de un fraude?

## 📥 Entregable

Guarda en `portfolio/parte-04/clase-02/`:

- el análisis de diez URL con el dominio registrable identificado;
- tres mensajes sospechosos reales con sus señales clasificadas;
- tu procedimiento de canal inverso con datos oficiales verificados;
- tu protocolo de respuesta ante entrega de datos, con plazos.

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

- Anti-Phishing Working Group (2024). *Phishing Activity Trends Report*. APWG. Estadísticas y vectores predominantes. <https://apwg.org/>
- NIST (2017). *SP 800-63B: Digital Identity Guidelines — Authentication and Lifecycle Management*. Limitaciones de los factores basados en códigos de un solo uso.
- Cialdini, R. (2021). *Influence: The Psychology of Persuasion*. Harper Business. Autoridad y urgencia como palancas del engaño.
- ENISA (2024). *Threat Landscape*. Agencia de la Unión Europea para la Ciberseguridad. Tendencias de suplantación y fraude.
- Europol (2024). *Internet Organised Crime Threat Assessment (IOCTA)*. Europol. Modus operandi de suplantación bancaria.
- Verificación local: identifica el canal oficial de reporte de phishing de tu banco y el organismo nacional de respuesta a incidentes de tu país.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 01 · Amenazas y hábitos seguros](01-amenazas-y-habitos-seguros.md) | [Parte 04](../README.md) · [Programa](../../../SYLLABUS.md) | [03 · Robo de identidad →](03-robo-de-identidad.md) |
<!-- gen:footer:end -->
