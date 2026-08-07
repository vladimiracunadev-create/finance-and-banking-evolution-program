---
part: 4
class: 12
title: "Prevención y respuesta ante fraude"
level: intermedio
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 12 · Prevención y respuesta ante fraude

> [← 11 · Renegociación responsable](11-renegociacion-responsable.md) · [Índice de la parte](../README.md) · [13 · Análisis de incidentes →](13-analisis-de-incidentes.md)

**Parte 04 — Seguridad y consumo financiero** · **Nivel:** Intermedio — requiere las partes anteriores · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Integrar todo lo aprendido en la parte en un sistema operativo de dos componentes: controles que
funcionan sin atención y un protocolo que se ejecuta bajo presión. La diferencia entre una pérdida
menor y una catastrófica se juega casi siempre en los primeros sesenta minutos, y esos sesenta minutos
no se improvisan.

Las once clases anteriores tratan amenazas concretas. Esta las reúne en una arquitectura y añade la dimensión que decide el resultado de cualquier caso real: el tiempo. Los derechos de reclamo tienen plazos cortos, y casi todo lo que se pierde en un fraude se pierde por haber reaccionado tarde y sin evidencia.

## 📚 Objetivos

Al finalizar podrás:

1. **Diseñar** tu arquitectura de controles con las tres capas de defensa.
2. **Ejecutar** el protocolo de respuesta cronometrado por fases.
3. **Reunir** la evidencia que determina el resultado de un reclamo.
4. **Conocer** los plazos legales que condicionan tu derecho a reembolso.
5. **Recuperarte** tras un incidente y cerrar el vector que lo permitió.

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

Los tres primeros términos son de arquitectura de controles y los tres últimos son los que deciden un reclamo. La **evidencia contemporánea** es la que hay que producir en el momento: capturas, horas y registros tomados durante el incidente valen más que cualquier reconstrucción posterior.

| Concepto | Comprensión verificable |
|---|---|
| `defensa en profundidad` | Varias capas de control: si una falla, otra contiene. |
| `pérdida máxima` | Lo peor que puede ocurrir con los controles actuales. Se dimensiona y se reduce. |
| `ventana de reclamo` | Plazo legal para desconocer una operación. Su pérdida elimina el derecho. |
| `desconocimiento formal` | Declaración escrita ante el emisor de que la operación no fue autorizada por ti. |
| `evidencia contemporánea` | Registros generados en el momento del incidente. Tienen más peso que una reconstrucción posterior. |
| `cierre del vector` | Eliminar la causa que permitió el incidente. Sin esto, se repite. |

## 🧠 Modelo mental

Tu defensa tiene **tres capas con funciones distintas**:

```text
capa 1  PREVENIR    límites, cupos reducidos, factores resistentes, tarjetas virtuales
capa 2  DETECTAR    notificaciones, revisión periódica, alertas de consulta
capa 3  CONTENER    protocolo de 60 minutos, evidencia, reclamo en plazo
```

La mayoría invierte todo en la capa 1 y nada en las otras dos. Y como la capa 1 **va a fallar alguna
vez** —basta un día de cansancio—, el resultado depende de las capas 2 y 3.

## 📖 Desarrollo

### 1. Arquitectura de controles

Los controles se organizan en capas para que el fallo de una no deje todo abierto. El esquema siguiente es esa arquitectura aplicada a finanzas personales.

| Capa | Control | Reduce | Verificación |
|---|---|---|---|
| Prevenir | Límite diario por canal | Pérdida máxima | Captura de la configuración |
| Prevenir | Cupos ajustados al uso real | Pérdida máxima | Certificado de reducción |
| Prevenir | Factor resistente al phishing en correo | Compromiso de la raíz | Llave registrada |
| Prevenir | Tarjeta virtual para comercios nuevos | Exposición de datos | Función activa |
| Prevenir | Cuenta operativa separada del ahorro | Alcance del incidente | Estructura de cuentas |
| Detectar | Notificación instantánea de todo monto | Tiempo de detección | Alerta recibida de prueba |
| Detectar | Revisión mensual de cartola y deudas | Fraudes de baja intensidad | Registro de revisiones |
| Detectar | Alerta de consulta de historial | Intentos de contratación | Servicio activo |
| Contener | Protocolo escrito con teléfonos | Tiempo de respuesta | Documento accesible sin internet |
| Contener | Carpeta de evidencia preparada | Calidad del reclamo | Plantillas listas |

### 2. Dimensionar la pérdida máxima

La pérdida máxima no es el patrimonio: es lo que alguien con un acceso concreto puede llegar a mover. El cálculo siguiente la acota y suele sugerir cambios simples de configuración.

```text
pérdida máxima = saldo accesible en cuentas operativas
               + cupos de crédito disponibles
               + capacidad de contratación a tu nombre (si no hay bloqueo)
```

Ejemplo de reducción:

| Componente | Antes | Después | Medida |
|---|---:|---:|---|
| Saldo en cuenta operativa | 4 200 000 | 900 000 | Ahorro en cuenta separada |
| Límite diario de transferencia | Sin límite | 400 000 | Configuración |
| Cupos de crédito | 6 800 000 | 1 500 000 | Reducción solicitada |
| Compras internacionales | Habilitadas | Deshabilitadas | Configuración |
| **Pérdida máxima estimada** | **11 000 000** | **2 400 000** | **−78 %** |

Ninguna de estas medidas cuesta dinero ni reduce la funcionalidad cotidiana. Es la intervención de
mayor retorno de toda la parte.

### 3. Protocolo cronometrado

El protocolo se organiza por minutos y no por importancia, porque las acciones que conservan derechos son las que tienen plazo. La secuencia siguiente está cronometrada.

```text
MINUTO 0–5   CONTENER
  1. bloquea tarjetas y accesos desde la aplicación oficial
  2. si no puedes entrar, llama al número del reverso de la tarjeta
  3. NO uses ningún número o enlace que te hayan enviado

MINUTO 5–20  EVALUAR
  4. revisa TODOS tus productos, no solo el afectado
  5. anota cada operación no reconocida: fecha, hora, monto, comercio
  6. captura pantallas de todo antes de que cambie

MINUTO 20–60  RECLAMAR
  7. desconoce formalmente por el canal oficial; exige número de caso
  8. cambia la clave del correo desde un dispositivo distinto
  9. cierra sesiones activas y revoca aplicaciones autorizadas

HORA 1–24   ASEGURAR
 10. denuncia ante la autoridad competente; guarda copia con folio
 11. solicita reemisión de tarjetas y cambio de claves restantes
 12. revisa tu informe de deudas por contrataciones a tu nombre

DÍA 1–7     SEGUIR
 13. presenta los antecedentes escritos que te soliciten
 14. verifica el plazo legal de respuesta y agéndalo
 15. si hay rechazo, escala al supervisor (clase 9)

DÍA 7–30    CERRAR EL VECTOR
 16. identifica cómo ocurrió y elimina esa vía
 17. ajusta controles y documenta la lección
```

El paso 6 —capturar pantallas antes de que cambie— es el más olvidado y el más valioso: las
operaciones pendientes se transforman, los sitios fraudulentos desaparecen y los mensajes se borran.

### 4. La evidencia que decide el reclamo

Hay evidencia que decide y evidencia que no aporta. La tabla las separa e indica cómo capturar la primera.

| Evidencia | Por qué pesa |
|---|---|
| Hora exacta del bloqueo | Acredita diligencia |
| Capturas del momento | Evidencia contemporánea, no reconstruida |
| Mensajes o correos recibidos | Acreditan el engaño y su origen |
| Denuncia con folio y fecha | Documento formal de respaldo |
| Número de caso del emisor | Permite escalar |
| Registro de que no compartiste claves | Refuta la negligencia |
| Historial de controles configurados | Muestra diligencia previa |

La última fila es la menos obvia: tener límites configurados y factores fuertes **antes** del incidente
respalda que actuaste con la diligencia esperable, lo que importa cuando se discute la
responsabilidad.

### 5. Plazos: el factor que elimina derechos

Los plazos de reclamo son cortos y su vencimiento cierra la vía por completo, con independencia de la razón que se tenga. La tabla los recoge.

```text
· desconocimiento de operaciones no autorizadas: plazo breve, frecuentemente de días
· contracargo por producto no recibido: 30–120 días según causal
· reclamo ante autoridad de consumo: plazos propios
· prescripción de acciones: varía por materia
```

Los plazos corren desde que **conociste o debiste conocer** la operación, no desde que la
descubriste. Ese matiz hace que la revisión periódica de cartolas (capa 2) tenga consecuencias
jurídicas: quien no revisa durante seis meses puede perder el derecho a reclamar operaciones antiguas.

Verificar los plazos exactos de tu país es parte del entregable.

## 🧮 Ejemplo guiado

**Situación.** Un domingo a las 22:40, Esteban recibe una notificación: transferencia de 780 000 a un
destinatario desconocido. Su banco no atiende por teléfono los domingos por la noche.

**Paso 1 — minuto 0–5.**

```text
22:41  abre la app y bloquea todos sus productos
22:43  intenta el canal telefónico de emergencia (opera 24/7 para bloqueos)
22:45  bloqueo confirmado, caso preliminar N.º 9912
```

El hallazgo relevante: **los canales de bloqueo operan 24/7 aunque la atención comercial no**. Saberlo
de antemano ahorra minutos críticos.

**Paso 2 — minuto 5–20.**

```text
22:46  revisa todos sus productos:
        · transferencia de 780 000 (no reconocida)
        · intento de transferencia de 1 200 000 rechazado por límite diario
        · compra en línea de 89 000 pendiente de autorización
22:52  captura pantalla de las tres operaciones y del detalle del destinatario
22:55  revisa su correo: encuentra un mensaje de "verificación de seguridad"
        recibido a las 22:12, que él respondió con un código
```

El límite diario configurado semanas antes **evitó una pérdida adicional de 1 200 000**. Ese es el
retorno concreto de la capa 1.

**Paso 3 — minuto 20–60.**

```text
23:00  desconocimiento formal por el canal digital → caso N.º 2026-77410
23:08  cambia la clave del correo desde el computador (no desde el teléfono comprometido)
23:15  cierra 6 sesiones activas y revoca 4 aplicaciones autorizadas
23:25  cambia clave de banca en línea
```

**Paso 4 — hora 1–24.**

```text
lunes 09:00  denuncia con folio 2026-118234
lunes 10:30  solicita reemisión de tarjetas
lunes 11:00  revisa informe de deudas: sin contrataciones nuevas
lunes 11:30  presenta al banco: capturas, correo del engaño, denuncia
```

**Paso 5 — el punto que define el resultado.** El banco plantea inicialmente que Esteban autorizó la
operación al entregar el código. La respuesta de Esteban:

```text
1. el mensaje de verificación no describía la operación autorizada
   (adjunta captura: decía "código de verificación de seguridad" sin detalle)
2. la operación se realizó a las 22:38 y el bloqueo se solicitó a las 22:41: 3 minutos
3. tenía configurados límite diario, notificaciones y segundo factor: diligencia acreditada
4. el intento posterior de 1 200 000 muestra un patrón de ataque, no una operación propia
```

**Paso 6 — resultado y cierre del vector.**

```text
día 18   el banco reembolsa 780 000
día 20   Esteban identifica el vector: respondió a un mensaje de correo suplantado
día 21   medidas de cierre:
          · llave de seguridad física en el correo (resistente al phishing)
          · límite diario reducido de 800 000 a 400 000
          · regla personal: ningún código se entrega por ningún canal, sin excepción
          · saldo operativo máximo de 900 000; el resto en cuenta separada
```

**Interpreta:** Esteban cometió el error que la clase 2 advierte —entregó un código— y aun así el
resultado fue reembolso completo. Las tres razones: **detectó en 3 minutos** (capa 2), **ejecutó un
protocolo** (capa 3) y **acreditó diligencia previa** (capa 1). Ninguna de las tres es azar; todas se
configuran antes de que ocurra nada.

## 🏦 Del cliente al banco

El cliente reporta un fraude y el banco aplica reglas de responsabilidad con plazos tasados. La tabla enfrenta las dos lecturas, y la columna del plazo es la que decide más casos.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| Desconocimiento formal | Caso de fraude con plazo de resolución regulado | 12, clase 15 |
| Bloqueo en 3 minutos | Reduce la pérdida y refuerza la posición del cliente | 14, clase 11 |
| Controles configurados | Evidencia de diligencia del titular | 12, clase 15 |
| Patrón de intentos | Insumo para el motor de detección | 14, clase 11 |
| Reembolso | Pérdida operacional del banco, no crediticia | 11, clase 7 |

## 🧪 Práctica

El laboratorio pide ejecutar el protocolo cronometrado sobre un caso sintético y producir el expediente. Lo que se mide es el tiempo hasta cada acción, porque es lo que se mide también en un caso real.

En `labs/lab-06.md`, sección de fraude:

1. Diseña tu arquitectura de controles con las tres capas y verifica cada uno.
2. Dimensiona tu pérdida máxima antes y después de aplicar reducciones.
3. Escribe tu protocolo cronometrado con teléfonos y canales reales.
4. Investiga y documenta los plazos legales de desconocimiento de tu país.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen reclamos perdidos con razón de fondo. Las causas son siempre las mismas dos: fuera de plazo o sin evidencia contemporánea.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se pierde tiempo buscando el teléfono | Protocolo no preparado | Ten el protocolo accesible sin internet. |
| Se reclama sin evidencia | No se capturó nada en el momento | Captura pantallas antes de que cambie. |
| Se pierde el derecho a reclamar | Se excedió el plazo legal | Revisa cartolas periódicamente; los plazos corren. |
| El banco alega autorización del cliente | No se acreditó diligencia | Documenta controles previos y tiempos de reacción. |
| Se repite el incidente | No se cerró el vector | Identifica la causa y elimínala. |
| Solo se revisa el producto afectado | El ataque suele ser múltiple | Revisa todos los productos. |

## ❓ Preguntas de comprobación

1. ¿Cuáles son las tres capas de defensa y por qué las dos últimas son decisivas?
2. ¿Cómo se dimensiona la pérdida máxima y cómo se reduce sin costo?
3. ¿Qué debes hacer en los primeros cinco minutos y qué no debes hacer nunca?
4. ¿Por qué la evidencia contemporánea pesa más que la reconstruida?
5. ¿Desde cuándo corren los plazos de desconocimiento y qué implica eso?

## 📥 Entregable

Guarda en `portfolio/parte-04/clase-12/`:

- tu arquitectura de controles con evidencia de verificación de cada uno;
- el dimensionamiento de tu pérdida máxima antes y después;
- tu protocolo cronometrado con canales y teléfonos reales;
- los plazos legales de tu país documentados con su fuente.

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

- NIST (2024). *Cybersecurity Framework 2.0*. National Institute of Standards and Technology. Funciones de detección, respuesta y recuperación. <https://www.nist.gov/cyberframework>
- Financial Stability Board (2020). *Effective Practices for Cyber Incident Response and Recovery*. FSB. Estructura de respuesta a incidentes. <https://www.fsb.org/>
- Basel Committee on Banking Supervision (2021). *Principles for Operational Resilience*. BIS. Marco de resiliencia operacional aplicable por analogía.
- World Bank (2017). *Good Practices for Financial Consumer Protection*. Banco Mundial. Responsabilidad y plazos ante operaciones no autorizadas.
- Europol (2024). *Internet Organised Crime Threat Assessment (IOCTA)*. Europol. Modus operandi y tiempos de reacción.
- Verificación local: revisa la norma de tu país sobre operaciones no reconocidas, los plazos de desconocimiento y las obligaciones de reembolso del emisor (en Chile, Ley 20.009 y sus modificaciones).

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 11 · Renegociación responsable](11-renegociacion-responsable.md) | [Parte 04](../README.md) · [Programa](../../../SYLLABUS.md) | [13 · Análisis de incidentes →](13-analisis-de-incidentes.md) |
<!-- gen:footer:end -->
