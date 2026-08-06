---
part: 10
class: 6
title: "Transferencias"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 06 · Transferencias

> [← 05 · Depósitos y giros](05-depositos-y-giros.md) · [Índice de la parte](../README.md) · [07 · Compensación y liquidación →](07-compensacion-y-liquidacion.md)

**Parte 10 — Operaciones bancarias** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Comprender el mecanismo por el que se mueve la mayor parte del dinero moderno. Una transferencia
parece instantánea y en realidad recorre varios sistemas con reglas, horarios y riesgos propios.
Conocerlos permite explicar demoras, prevenir fraudes y gestionar la liquidez.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** los sistemas de pago por monto, velocidad y firmeza.
2. **Trazar** el recorrido de una transferencia entre bancos.
3. **Explicar** la firmeza de un pago y por qué importa.
4. **Aplicar** los controles de prevención de fraude en transferencias.
5. **Gestionar** una transferencia errónea o fraudulenta.

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
| `sistema de alto valor` | Liquidación bruta en tiempo real, operación por operación. Irrevocable. |
| `sistema minorista` | Liquidación neta diferida o pagos inmediatos de bajo monto. |
| `firmeza` | Momento a partir del cual un pago es irrevocable. |
| `liquidación bruta` | Cada operación se liquida individualmente. |
| `liquidación neta` | Se compensan las obligaciones y se liquida el neto. |
| `riesgo de liquidación` | Riesgo de que una parte cumpla y la otra no. |
| `transferencia inmediata` | Disponible en segundos, con reglas propias de firmeza. |

## 🧠 Modelo mental

Una transferencia mueve **dos cosas en dos sistemas distintos**:

```text
INFORMACIÓN   el mensaje de pago viaja entre bancos
DINERO        las reservas se mueven en el banco central

el cliente ve un solo evento; el sistema ejecuta dos
```

Cuando ambos ocurren simultáneamente (liquidación bruta en tiempo real), el riesgo de liquidación
desaparece. Cuando se separan, aparece.

## 📖 Desarrollo

### 1. Sistemas de pago

| Sistema | Monto típico | Velocidad | Liquidación | Firmeza |
|---|---|---|---|---|
| Alto valor | Alto | Minutos | Bruta en tiempo real | Inmediata e irrevocable |
| Cámara de compensación | Bajo a medio | 1 día | Neta diferida | Al liquidar el neto |
| Pagos inmediatos | Bajo | Segundos | Según diseño | Habitualmente inmediata |
| Interno (mismo banco) | Cualquiera | Inmediato | Contable | Inmediata |
| Internacional | Cualquiera | 1 a 5 días | Vía corresponsales | Al abonar el beneficiario |

### 2. Recorrido de una transferencia

```text
TRANSFERENCIA ENTRE BANCOS, SISTEMA MINORISTA

1. el cliente ordena la transferencia en su banco (banco emisor)
2. el banco valida: saldo, límites, datos del beneficiario, listas restrictivas
3. el banco debita la cuenta del ordenante
4. el mensaje se envía al sistema de pagos
5. el sistema lo enruta al banco receptor
6. el banco receptor valida la cuenta destino
7. el banco receptor abona al beneficiario
8. al cierre, el sistema calcula posiciones netas entre bancos
9. la liquidación neta se realiza en las cuentas del banco central
```

**Entre los pasos 7 y 9 existe riesgo de liquidación:** el beneficiario ya tiene el dinero y los bancos
aún no han liquidado entre sí. Los sistemas lo mitigan con garantías, límites y fondos de respaldo.

### 3. Firmeza

```text
FIRMEZA = momento desde el cual el pago no puede revocarse
```

```text
antes de la firmeza:
  · el pago puede anularse por error operativo
  · puede detenerse por orden judicial
  · puede rechazarse por el banco receptor

después de la firmeza:
  · el pago es definitivo
  · una devolución requiere una NUEVA transferencia en sentido contrario,
    que exige el consentimiento del beneficiario
```

**Consecuencia práctica crítica:** una transferencia enviada por error a un tercero **no se puede
"cancelar"** después de la firmeza. El banco puede contactar al receptor y solicitar la devolución, y
el receptor puede negarse.

Esa es la razón por la que la validación del beneficiario **antes** de ejecutar es el control más
importante del proceso.

### 4. Controles de prevención de fraude

| Control | Efecto | Momento |
|---|---|---|
| Verificación del nombre del beneficiario | Detecta cuenta errónea o fraudulenta | Antes de ejecutar |
| Registro previo de destinatarios | Reduce transferencias a cuentas nuevas | Configuración |
| Periodo de espera para destinatarios nuevos | Ventana para detectar el fraude | Antes de ejecutar |
| Límites diferenciados por tipo de destinatario | Acota la pérdida | Configuración |
| Autenticación reforzada por monto | Verificación proporcional | Antes de ejecutar |
| Alerta por desviación del perfil | Detección de operación atípica | En tiempo real |
| Retención temporal de operaciones atípicas | Ventana de confirmación | Antes de liquidar |
| Notificación inmediata al ordenante | Detección temprana | Al ejecutar |

**El control de mayor efecto documentado** es la verificación del nombre del beneficiario: muchos
fraudes consisten en desviar un pago legítimo a una cuenta distinta, y la discordancia entre el nombre
esperado y el titular real lo revela.

### 5. Gestionar una transferencia errónea o fraudulenta

```text
TRANSFERENCIA POR ERROR DEL CLIENTE
  1. el cliente solicita la devolución a su banco
  2. el banco emisor contacta al banco receptor
  3. el banco receptor contacta al beneficiario y solicita autorización
  4. si el beneficiario autoriza: se devuelve
  5. si no autoriza: el ordenante debe accionar civilmente
  → el banco NO puede debitar la cuenta del beneficiario sin su autorización

TRANSFERENCIA FRAUDULENTA
  1. el cliente desconoce la operación
  2. el banco emisor bloquea y contacta de inmediato al receptor
  3. si los fondos no se han retirado: retención cautelar
  4. denuncia y, en su caso, medida judicial
  5. evaluación de responsabilidad conforme a la normativa
  6. registro como evento de fraude y análisis de causa
```

**La ventana de recuperación es muy corta:** en fraudes documentados, los fondos se retiran o se
transfieren nuevamente en minutos. De ahí la importancia de la detección en tiempo real.

## 🧮 Ejemplo guiado

**Situación.** Una empresa denuncia el desvío de un pago a un proveedor por 148 millones.

```text
HECHOS
  la empresa paga mensualmente a un proveedor habitual
  el 8 de abril recibió un correo del "proveedor" informando cambio de cuenta bancaria
  el 10 de abril transfirió 148 millones a la cuenta nueva
  el 15 de abril el proveedor real reclamó el pago
```

**Paso 1 — clasifica el evento.**

```text
NO es una transferencia no autorizada: la empresa la ordenó
SÍ es un fraude: la orden se basó en información falsa

tipología: fraude de suplantación de proveedor (compromiso de correo empresarial)
```

**Paso 2 — reconstruye la ventana de recuperación.**

```text
10-abr 10:14  transferencia ejecutada
10-abr 10:14  fondos disponibles en la cuenta destino
10-abr 10:31  el beneficiario transfiere 92 millones a otras 3 cuentas
10-abr 11:47  retira 34 millones en efectivo en dos sucursales
10-abr 14:20  transfiere 21 millones al exterior
15-abr 09:00  la empresa denuncia
15-abr 09:40  el banco bloquea: saldo remanente 1 millón
```

**RECUPERACIÓN INMEDIATA: 1 millón de 148.**

**Paso 3 — analiza los controles del banco emisor.**

```text
□ ¿verificó el nombre del beneficiario contra el titular de la cuenta?
  NO — el sistema no tenía esa funcionalidad

□ ¿alertó por destinatario nuevo?
  NO — la cuenta se registró el 9 de abril y se usó el 10

□ ¿alertó por monto atípico?
  NO — la empresa transfiere montos similares mensualmente

□ ¿hubo periodo de espera para el destinatario nuevo?
  NO
```

**Paso 4 — analiza los controles del banco receptor.**

```text
□ ¿la cuenta receptora tenía perfil compatible con recibir 148 millones?
  NO — cuenta abierta hace 3 meses, saldo promedio 400 000

□ ¿se alertó por desviación del perfil?
  El sistema generó una alerta a las 10:22
  la alerta se revisó el 11 de abril a las 09:00  ← 23 HORAS DESPUÉS

□ ¿existía retención automática para operaciones atípicas?
  NO
```

**El banco receptor detectó la anomalía en 8 minutos y la revisó 23 horas después.** En ese intervalo
se retiraron 147 de los 148 millones.

**Paso 5 — analiza los controles de la empresa.**

```text
□ ¿verificó el cambio de cuenta por un canal independiente?
  NO — respondió al mismo correo

□ ¿tenía un procedimiento para cambios de datos bancarios de proveedores?
  NO

□ ¿existía doble aprobación para pagos sobre un umbral?
  SÍ, pero ambos aprobadores recibieron el mismo correo falso
```

**Paso 6 — diagnóstico integrado.**

```text
fallaron controles en las TRES partes:

EMPRESA
  · sin verificación por canal independiente ante cambio de datos bancarios
  · doble aprobación inefectiva: ambos aprobadores con la misma información falsa

BANCO EMISOR
  · sin verificación de nombre del beneficiario
  · sin control de destinatario nuevo

BANCO RECEPTOR
  · alerta generada y no atendida durante 23 horas
  · sin retención automática de operaciones atípicas
```

**Paso 7 — la corrección de mayor impacto por parte.**

```text
EMPRESA (costo: cero)
  procedimiento obligatorio: todo cambio de datos bancarios de un proveedor
  se verifica llamando al teléfono REGISTRADO PREVIAMENTE, nunca al del correo

BANCO EMISOR (costo: desarrollo)
  verificación del nombre del beneficiario antes de ejecutar
  advertencia visible al cliente si no coincide

BANCO RECEPTOR (costo: proceso)
  retención automática de operaciones que superan 20x el perfil,
  con revisión en un plazo máximo de 2 horas hábiles
```

**Paso 8 — el análisis que cambia la política.**

```text
la alerta del banco receptor funcionó: detectó en 8 minutos
lo que falló fue el PROCESO DE ATENCIÓN de la alerta

revisión del área de monitoreo:
  alertas generadas por día: 1 840
  alertas revisadas en menos de 2 horas: 14 %
  alertas revisadas en más de 24 horas: 38 %
  
  el sistema genera más alertas de las que el equipo puede atender
  → la calibración del motor genera exceso de falsos positivos
  → el efecto práctico es que el control no existe
```

**Interpreta:** el banco receptor tenía el control correcto y **su exceso de alertas lo volvió
inoperante**. Un motor que genera 1 840 alertas diarias para un equipo que puede atender 250 no es un
control: es un registro. La corrección no era generar más alertas, sino **calibrar el motor y
priorizar** para que las críticas se atiendan en minutos.

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| "Quiero cancelar mi transferencia" | Después de la firmeza no es posible unilateralmente | 10, clase 7 |
| Verificación del nombre del destinatario | Control de mayor efecto contra el desvío | 4, clase 12 |
| Periodo de espera para destinatario nuevo | Ventana de detección de fraude | 4, clase 1 |
| Retención temporal de una operación | Control por desviación del perfil | 12, clase 8 |
| Transferencia internacional demorada | Recorrido por corresponsales | 10, clase 13 |

## 🧪 Práctica

En `labs/lab-03.md`, sección de transferencias:

1. Compara los cinco sistemas de pago por monto, velocidad, liquidación y firmeza.
2. Traza el recorrido de una transferencia con sus nueve pasos y sus riesgos.
3. Diseña la matriz de controles de fraude con su momento de aplicación.
4. Analiza un caso de desvío de pago identificando los controles fallidos en cada parte.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se promete "cancelar" una transferencia | Firmeza no comprendida | Explica que requiere autorización del receptor. |
| Sin verificación del nombre del beneficiario | Control ausente | Es el de mayor efecto contra el desvío. |
| Alertas generadas y no atendidas | Motor mal calibrado | Reduce falsos positivos y prioriza. |
| Cambio de datos verificado por el mismo canal | Canal del atacante | Verifica por canal independiente registrado. |
| Doble aprobación con la misma información | Control aparente | Los aprobadores deben verificar independientemente. |
| Sin retención de operaciones atípicas | Ventana de recuperación nula | Retén y confirma antes de liquidar. |

## ❓ Preguntas de comprobación

1. ¿Qué distingue la liquidación bruta de la neta y qué riesgo elimina la primera?
2. ¿Qué significa la firmeza de un pago y qué implica para una transferencia errónea?
3. ¿Cuál es el control de mayor efecto contra el desvío de pagos?
4. ¿Por qué un exceso de alertas equivale a la ausencia de control?
5. ¿Cómo debe verificarse un cambio de datos bancarios de un proveedor?

## 📥 Entregable

Guarda en `portfolio/parte-10/clase-06/`:

- la comparación de los cinco sistemas de pago;
- el recorrido de una transferencia con sus riesgos por etapa;
- la matriz de controles de fraude con su momento de aplicación;
- el análisis de un caso de desvío con los controles fallidos de cada parte.

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

- Committee on Payments and Market Infrastructures (2012). *Principles for Financial Market Infrastructures*. CPMI-IOSCO/BIS. Firmeza, liquidación y riesgo. <https://www.bis.org/cpmi/publ/d101.htm>
- Committee on Payments and Market Infrastructures (2016). *Fast payments — Enhancing the speed and availability of retail payments*. BIS.
- Bank for International Settlements (2020). *Payment aspects of financial inclusion*. CPMI/Banco Mundial.
- Financial Action Task Force (2023). *FATF Recommendations*, R.16: transferencias electrónicas e información del ordenante y beneficiario.
- Europol (2024). *Internet Organised Crime Threat Assessment (IOCTA)*. Fraude de suplantación de proveedor.
- Verificación local: revisa los sistemas de pago de tu país, sus horarios de corte, sus reglas de firmeza y la normativa sobre operaciones no autorizadas.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 05 · Depósitos y giros](05-depositos-y-giros.md) | [Parte 10](../README.md) · [Programa](../../../SYLLABUS.md) | [07 · Compensación y liquidación →](07-compensacion-y-liquidacion.md) |
<!-- gen:footer:end -->
