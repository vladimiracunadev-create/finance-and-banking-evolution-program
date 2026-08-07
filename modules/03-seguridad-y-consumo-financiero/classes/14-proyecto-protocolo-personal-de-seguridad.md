---
part: 4
class: 14
title: "Proyecto: protocolo personal de seguridad"
level: intermedio
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 14 · Proyecto: protocolo personal de seguridad

> [← 13 · Análisis de incidentes](13-analisis-de-incidentes.md) · [Índice de la parte](../README.md) · [Proyecto de la parte →](../project/README.md)

**Parte 04 — Seguridad y consumo financiero** · **Nivel:** Intermedio — requiere las partes anteriores · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Producir el documento operativo que integra las trece clases de la parte: un protocolo personal de
seguridad financiera que sirva bajo presión, que sea verificable y que se mantenga vigente. No es un
resumen de buenas prácticas: es un procedimiento con controles configurados, evidencia de
verificación y fechas de revisión.

## 📚 Objetivos

Al finalizar podrás:

1. **Redactar** un protocolo personal con sus seis secciones.
2. **Verificar** cada control con evidencia, no con declaración.
3. **Probar** el protocolo mediante un simulacro documentado.
4. **Dimensionar** tu pérdida máxima antes y después de las medidas.
5. **Mantener** el protocolo vigente con un calendario de revisión.

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
| `protocolo` | Documento de procedimiento, no de recomendaciones. Se ejecuta, no se consulta. |
| `control verificado` | Control cuya configuración fue comprobada, con evidencia archivada. |
| `simulacro` | Ejecución de prueba del protocolo sin incidente real. Revela lo que falta. |
| `accesibilidad bajo presión` | El protocolo debe estar disponible sin internet, sin la aplicación y sin el teléfono comprometido. |
| `vigencia` | Los teléfonos, canales y plazos cambian. Un protocolo desactualizado falla. |
| `pérdida máxima residual` | Lo que aún podrías perder tras aplicar todos los controles. Debe ser un número conocido. |

## 🧠 Modelo mental

Un protocolo se juzga por una sola pregunta:

```text
¿podría ejecutarlo una persona alterada, un domingo a las 23:00,
 sin acceso a su teléfono habitual?
```

Si la respuesta es no, el documento es un resumen de buenas intenciones. Todo el diseño —formato,
ubicación, nivel de detalle— responde a esa pregunta.

## 📖 Desarrollo

### 1. Las seis secciones

| # | Sección | Contenido |
|---:|---|---|
| 1 | Inventario | Productos, instituciones, cupos, saldos típicos, contactos oficiales |
| 2 | Controles | Cada control con su estado, evidencia y fecha de verificación |
| 3 | Pérdida máxima | Cálculo antes y después, con el residual declarado |
| 4 | Protocolo de respuesta | Procedimiento cronometrado por fases (clase 12) |
| 5 | Evidencia y plantillas | Modelos de desconocimiento, reclamo y solicitud de expediente |
| 6 | Calendario | Revisiones periódicas con qué se verifica en cada una |

### 2. Sección 1 — inventario

```text
INSTITUCIÓN        PRODUCTO           CUPO/SALDO   BLOQUEO 24/7     CANAL DE RECLAMO
Banco A            Cuenta corriente   ~900 000     600 123 4567     app / sucursal
Banco A            Tarjeta crédito    1 500 000    600 123 4567     app
Banco B            Cuenta ahorro      4 200 000    600 987 6543     app
Emisor C           Tarjeta            0 (cerrada)  —                —
Registro deudas    Informe            —            —                sitio oficial
```

Requisito: los teléfonos deben estar **verificados llamando**, no copiados de un sitio. Y el documento
debe existir en un formato accesible sin el teléfono principal: impreso o en un segundo dispositivo.

### 3. Sección 2 — controles con evidencia

| Control | Estado | Evidencia | Verificado |
|---|---|---|---|
| Factor resistente al phishing en correo | Activo | Captura de llaves registradas | 2026-08-05 |
| Segundo factor en banca | Activo | Captura de configuración | 2026-08-05 |
| Límite diario de transferencia: 400 000 | Activo | Captura | 2026-08-05 |
| Compras internacionales | Deshabilitadas | Captura | 2026-08-05 |
| Notificación de todo monto | Activo | Alerta de prueba recibida | 2026-08-05 |
| Cupos reducidos | 1 500 000 (antes 6 800 000) | Certificado del emisor | 2026-07-28 |
| Correo dedicado a banca | Activo | — | 2026-08-01 |
| Clave con operador de telefonía | Activa | Número de caso | 2026-08-02 |
| Gestor de contraseñas | Activo, con segundo factor | — | 2026-08-03 |
| Alerta de consulta de historial | Activa | Confirmación del servicio | 2026-08-04 |

La columna "Evidencia" es lo que distingue este documento de una lista de buenos propósitos. Un
control declarado y no verificado tiene una probabilidad alta de estar mal configurado.

### 4. Sección 3 — pérdida máxima

```text
ANTES
  saldo en cuenta operativa          4 200 000
  límite diario                      sin límite → todo el saldo
  cupos de crédito                   6 800 000
  contratación a mi nombre           sin bloqueo
  PÉRDIDA MÁXIMA ESTIMADA           11 000 000 + contrataciones

DESPUÉS
  saldo en cuenta operativa            900 000
  límite diario                        400 000
  cupos de crédito                   1 500 000
  contratación a mi nombre           alerta de consulta activa
  PÉRDIDA MÁXIMA RESIDUAL            2 400 000

REDUCCIÓN                            −78 %
```

El residual de 2 400 000 es información valiosa: es el número que Nicolás sabe que podría perder en el
peor caso, y contra el que puede decidir si acepta ese riesgo o toma medidas adicionales.

### 5. Sección 6 — calendario de vigencia

| Frecuencia | Qué se revisa |
|---|---|
| Mensual | Cartolas de todos los productos; cargos recurrentes |
| Trimestral | Informe de deudas; sesiones activas; aplicaciones autorizadas |
| Semestral | Cupos y límites; comercios con tarjeta guardada; contactos oficiales |
| Anual | Simulacro completo; revisión de plazos legales; actualización del protocolo |

### 6. El simulacro

```text
ESCENARIO: "recibo notificación de una transferencia no reconocida,
            son las 23:00 de un domingo y mi teléfono está sin batería"

pasos ejecutados (cronometrados)
  1. ¿dónde está el protocolo impreso?             → __ segundos
  2. ¿qué número llamo para bloquear?              → __ segundos
  3. ¿desde qué dispositivo cambio la clave?       → __ segundos
  4. ¿dónde están mis plantillas de reclamo?       → __ segundos
  5. ¿sé el plazo legal de desconocimiento?        → sí / no

hallazgos del simulacro
  ...
acciones correctivas
  ...
```

El simulacro casi siempre revela lo mismo: el protocolo estaba **solo en el teléfono**, los teléfonos
no estaban verificados, y no había un segundo dispositivo definido para cambiar credenciales. Los tres
hallazgos se corrigen en una hora y solo aparecen al probarlo.

## 🧮 Ejemplo guiado

**Situación de defensa.** Presentas tu protocolo y el revisor pregunta: *"Tu pérdida máxima residual
es 2 400 000. ¿Por qué no la reduces más? Podrías dejar 200 000 en la cuenta y cupo cero."*

**Respuesta defendible.**

1. **Porque un control que impide vivir se desactiva.** Un límite diario de 100 000 hace imposible
   pagar un arriendo o una compra normal, y la reacción previsible es desactivarlo justo cuando se
   necesita. Un control sostenible vale más que uno óptimo abandonado.
2. **Porque el residual está dimensionado contra un criterio.** 2 400 000 equivale a 1,6 meses de mi
   gasto esencial, y mi fondo de emergencia está en una institución distinta, con acceso separado. La
   pérdida máxima no compromete mi capacidad de operar mientras se resuelve el reclamo.
3. **Porque la reducción tiene retornos decrecientes.** Pasar de 11 000 000 a 2 400 000 costó una hora
   y ningún inconveniente. Pasar de 2 400 000 a 800 000 exigiría transferencias manuales frecuentes,
   con un costo de fricción diario para una reducción marginal del riesgo.

**Contra-pregunta esperable:** *"¿Y si el atacante accede al fondo de emergencia en la otra
institución?"* Respuesta: son credenciales distintas, en un gestor distinto y con un correo distinto;
comprometer ambas exige dos ataques independientes. Ese es exactamente el propósito de la separación.

**Lo que este intercambio enseña:** un protocolo se defiende mostrando que **cada control es
sostenible** y que el riesgo residual fue una decisión consciente, no un olvido. Un riesgo residual
nombrado y aceptado es gestión; uno desconocido es exposición.

## 🏦 Del cliente al banco

| Tu protocolo | Equivalente institucional | Parte |
|---|---|---|
| Inventario de productos | Inventario de activos de información | 11, clase 8 |
| Controles con evidencia | Matriz de controles con pruebas de efectividad | 12, clase 12 |
| Pérdida máxima residual | Riesgo residual y apetito declarado | 11, clase 12 |
| Simulacro | Prueba de continuidad operacional | 11, clase 14 |
| Calendario de revisión | Ciclo de revisión de controles | 12, clase 13 |

## 🧪 Práctica

Este proyecto es la práctica. Trabaja en `project/README.md` de esta parte.

1. Redacta las seis secciones del protocolo.
2. Verifica cada control con evidencia archivada y fecha.
3. Calcula tu pérdida máxima antes y después, y declara el residual.
4. Ejecuta el simulacro, documenta los hallazgos y aplica las correcciones.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| El protocolo no se puede usar en la emergencia | Existe solo en el teléfono | Guarda copia impresa y en un segundo dispositivo. |
| Los controles están declarados, no verificados | No se archivó evidencia | Adjunta captura o certificado con fecha. |
| El teléfono de bloqueo no responde | Se copió de una fuente no verificada | Verifica llamando antes de anotarlo. |
| El protocolo queda obsoleto | Sin calendario de revisión | Agenda las revisiones al escribirlo. |
| Se reducen los límites al mínimo y se desactivan | Control no sostenible | Ajusta al uso real, no al mínimo teórico. |
| No se conoce la pérdida residual | No se calculó | Dimensiónala y decide si la aceptas. |

## ❓ Preguntas de comprobación

1. ¿Cuál es la pregunta que juzga la calidad de un protocolo?
2. ¿Por qué un control declarado no equivale a un control verificado?
3. ¿Qué revela habitualmente un simulacro y cómo se corrige?
4. ¿Por qué un control demasiado restrictivo puede empeorar tu seguridad?
5. ¿Qué diferencia hay entre un riesgo residual aceptado y uno desconocido?

## 📥 Entregable

Guarda en `portfolio/parte-04/clase-14/`:

- el protocolo completo con las seis secciones;
- la tabla de controles con evidencia y fecha de verificación de cada uno;
- el cálculo de pérdida máxima antes, después y el residual declarado;
- el registro del simulacro con hallazgos, correcciones y calendario de revisión.

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

- NIST (2024). *Cybersecurity Framework 2.0*. National Institute of Standards and Technology. Estructura de perfil y de controles. <https://www.nist.gov/cyberframework>
- ISO/IEC (2022). *ISO/IEC 27002: Information security controls*. Catálogo de controles y su verificación.
- Financial Stability Board (2020). *Effective Practices for Cyber Incident Response and Recovery*. FSB. Preparación, prueba y mantenimiento de protocolos.
- Basel Committee on Banking Supervision (2021). *Principles for Operational Resilience*. BIS. Pruebas de escenarios y tolerancia a la disrupción.
- World Bank (2017). *Good Practices for Financial Consumer Protection*. Banco Mundial. Derechos y plazos ante operaciones no autorizadas.
- Verificación local: confirma los teléfonos y canales oficiales de bloqueo 24/7 de tus instituciones y los plazos legales de desconocimiento vigentes en tu país.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 13 · Análisis de incidentes](13-analisis-de-incidentes.md) | [Parte 04](../README.md) · [Programa](../../../SYLLABUS.md) | [Proyecto de la parte →](../project/README.md) |
<!-- gen:footer:end -->
