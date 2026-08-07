---
part: 10
class: 5
title: "Depósitos y giros"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 05 · Depósitos y giros

> [← 04 · Apertura y administración de cuentas](04-apertura-y-administracion-de-cuentas.md) · [Índice de la parte](../README.md) · [06 · Transferencias →](06-transferencias.md)

**Parte 10 — Operaciones bancarias** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Dominar las operaciones más elementales y de mayor frecuencia de un banco. Su volumen las convierte en
la principal fuente de riesgo operacional por acumulación: un error de baja severidad repetido miles
de veces produce pérdidas materiales y deteriora la confianza del cliente.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** los tipos de depósito y su disponibilidad.
2. **Aplicar** las reglas de canje y de disponibilidad de fondos.
3. **Ejecutar** los controles de un giro por caja y por canal remoto.
4. **Gestionar** las diferencias de caja y su tratamiento.
5. **Identificar** los riesgos de fraude en depósitos y giros.

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
| `depósito en efectivo` | Entrega de dinero físico. Disponibilidad inmediata tras el conteo. |
| `depósito en documentos` | Cheques u otros valores. Sujeto a canje antes de estar disponible. |
| `canje` | Proceso interbancario de cobro de documentos. Define cuándo el fondo es disponible. |
| `saldo contable y disponible` | El contable incluye documentos en canje; el disponible, no. |
| `giro` | Retiro de fondos. Por caja, cajero automático o canal remoto. |
| `diferencia de caja` | Descuadre entre el efectivo físico y el registro. |
| `arqueo` | Recuento del efectivo y su comparación con el registro. |

## 🧠 Modelo mental

El cliente ve un saldo; el banco maneja **dos**:

```text
saldo CONTABLE     incluye todo lo registrado, esté disponible o no
saldo DISPONIBLE   lo que efectivamente puede girarse hoy

diferencia = documentos en canje + retenciones + saldos comprometidos
```

Explicar esta diferencia al momento del depósito evita la mayoría de los reclamos por "mi dinero no
está".

## 📖 Desarrollo

### 1. Tipos de depósito y disponibilidad

| Tipo | Disponibilidad | Control principal |
|---|---|---|
| Efectivo por caja | Inmediata | Conteo, detección de billetes falsos |
| Efectivo en máquina depositaria | Inmediata o siguiente día | Validación automática |
| Cheque del mismo banco | Inmediata o 1 día | Verificación de fondos |
| Cheque de otro banco | Según plazo de canje | Canje interbancario |
| Transferencia recibida | Inmediata | Validación de origen |
| Documento en cobranza | Al cobrarse efectivamente | Gestión de cobro |

**Reglas de disponibilidad:**

```text
· el plazo de canje debe estar publicado y ser informado al depositante
· el banco puede retener fondos por causales definidas y comunicadas
· una vez vencido el plazo, los fondos deben estar disponibles
· si el documento se devuelve, el cargo se revierte y debe informarse
```

### 2. El proceso de canje

```text
día 0  el cliente deposita un cheque de otro banco
       el banco lo recibe y lo registra en saldo contable, no disponible
día 0  al cierre, los documentos se envían a la cámara de compensación
día 1  la cámara distribuye los documentos a los bancos librados
día 1  el banco librado verifica fondos y firma
día 1  si acepta: se liquida y el fondo queda disponible
       si rechaza: se protesta y el documento se devuelve
día 2  el resultado se refleja en la cuenta del depositante
```

**Motivos de devolución y su tratamiento:**

| Motivo | Acción del banco depositario |
|---|---|
| Fondos insuficientes | Reversa el abono; informa al cliente; puede cobrar comisión |
| Firma disconforme | Reversa; devuelve el documento al cliente |
| Cuenta cerrada | Reversa; el cliente debe gestionar con el girador |
| Documento caducado | Reversa; el cliente puede solicitar reemisión |
| Endoso irregular | Reversa; se corrige y se redeposita |

### 3. Controles del giro por caja

```text
1. identificación del solicitante (documento vigente)
2. verificación de la titularidad o del poder
3. verificación de saldo DISPONIBLE, no contable
4. verificación de límites y de bloqueos
5. registro de la operación con identificación del cajero
6. conteo del efectivo en presencia del cliente
7. entrega del comprobante
8. para montos altos: doble verificación o autorización de supervisor
```

**Umbrales que activan controles adicionales:**

```text
· monto sobre el umbral de reporte: registro adicional para prevención de lavado
· monto sobre el umbral operativo: autorización de supervisor
· giro de un apoderado: verificación de vigencia del poder
· giro por un tercero autorizado: verificación específica
· patrón inusual respecto del perfil: alerta y eventual retención
```

### 4. Diferencias de caja

```text
arqueo = recuento físico del efectivo comparado con el registro del sistema

diferencia positiva (sobrante)   más efectivo del registrado
diferencia negativa (faltante)   menos efectivo del registrado
```

**Tratamiento:**

```text
1. TODA diferencia se registra, cualquiera sea su monto y su signo
2. se investiga el origen: revisión de operaciones del día, grabaciones, comprobantes
3. si se identifica: se corrige la operación y se documenta
4. si no se identifica: se registra como pérdida o ganancia operacional
5. diferencias reiteradas de un mismo cajero: investigación específica
6. diferencias sobre un umbral: escalamiento obligatorio
```

**Señal de alerta que suele pasarse por alto:**

```text
un cajero con diferencias FRECUENTES Y PEQUEÑAS, algunas positivas y otras negativas,
puede indicar descuido... o puede indicar la ocultación de faltantes mediante
compensación con sobrantes de otras operaciones

el patrón a vigilar no es el monto acumulado, sino la FRECUENCIA
```

### 5. Riesgos de fraude

| Riesgo | Mecanismo | Control |
|---|---|---|
| Billetes falsos | Depósito de efectivo falsificado | Detectores y capacitación |
| Cheque adulterado | Alteración de monto o beneficiario | Verificación de menciones y de firma |
| Depósito ficticio | Registro sin entrega efectiva de fondos | Segregación entre registro y custodia |
| Giro con documento falso | Suplantación del titular | Verificación biométrica o presencial reforzada |
| Poder falsificado | Apoderado inexistente | Verificación en el registro de poderes |
| Retención indebida de efectivo | El cajero registra el depósito y no lo ingresa | Arqueo diario y cuadratura |
| Manipulación de comprobantes | Alteración de registros | Numeración correlativa y auditoría |

## 🧮 Ejemplo guiado

**Situación.** Una sucursal presenta diferencias de caja recurrentes. Investiga.

```text
REGISTRO DE DIFERENCIAS (últimos 6 meses, por cajero)

cajero    operaciones   diferencias   monto acumulado   frecuencia
  A          8 420           4            −18 000         0,05 %
  B          9 180           6            +12 000         0,07 %
  C          7 940          38            −4 000          0,48 %
  D          8 610           5            −22 000         0,06 %
```

**Paso 1 — identifica la anomalía.**

```text
el cajero C tiene 38 diferencias con un monto acumulado de solo −4 000
los demás tienen 4 a 6 diferencias con montos mayores

la anomalía NO es el monto: es la FRECUENCIA
C tiene 7 veces más diferencias que el promedio
```

**Paso 2 — analiza el detalle de las diferencias de C.**

```text
        faltantes        sobrantes
número      21               17
monto    −186 000        +182 000
neto                      −4 000
```

**Los faltantes y sobrantes casi se compensan.** Ese patrón no es aleatorio: en una distribución de
errores genuinos, la compensación tan precisa es improbable.

**Paso 3 — analiza la distribución temporal.**

```text
los faltantes ocurren mayoritariamente los días 1 a 10 del mes
los sobrantes, los días 20 a 30

patrón: el faltante aparece primero y el sobrante después
```

**Paso 4 — formula la hipótesis.**

```text
HIPÓTESIS: el cajero toma efectivo temporalmente y lo repone después

mecanismo:
  · retira efectivo al inicio del mes (faltante)
  · lo repone antes del cierre (sobrante que compensa)
  · el neto acumulado es cercano a cero, lo que evita alertas por monto
```

**Paso 5 — busca evidencia adicional.**

```text
· revisión de grabaciones en fechas de faltantes: pendiente
· horarios de las operaciones con diferencia: 12 de 21 faltantes ocurrieron
  en el último turno, con menor supervisión
· el cajero C es quien realiza el arqueo de cierre en 60 % de los casos
  → CONFLICTO: quien opera realiza el control
```

**Paso 6 — el hallazgo de control.**

```text
el problema NO es solo la conducta del cajero:
  el arqueo lo realiza la misma persona que operó la caja

CONTROL FALLIDO: sin segregación entre operación y control
```

**Paso 7 — acciones.**

```text
INMEDIATO
  1. suspender al cajero C de funciones de caja mientras se investiga
  2. arqueo sorpresivo de todas las cajas de la sucursal
  3. revisión de grabaciones de las fechas con faltantes
  4. escalamiento al área de seguridad y a recursos humanos

DE CONTROL
  5. el arqueo NUNCA lo realiza quien operó la caja
  6. arqueos sorpresivos aleatorios, con frecuencia mínima mensual
  7. alerta automática por FRECUENCIA de diferencias, no solo por monto:
     umbral de 0,15 % de las operaciones
  8. rotación de cajeros entre turnos y entre cajas
  9. doble control en el turno de cierre

SISTÉMICO
 10. revisar el indicador de diferencias de caja en todas las sucursales
     con el criterio de frecuencia
 11. incorporar el patrón "faltantes seguidos de sobrantes" en el análisis
```

**Paso 8 — resultado.**

```text
el análisis por frecuencia detectó en 6 meses lo que el análisis por monto
no habría detectado nunca: el neto de −4 000 estaba muy por debajo de
cualquier umbral de escalamiento

la pérdida potencial evitada no es de 4 000: es el riesgo de que el patrón
escale a montos mayores, y el riesgo reputacional de un fraude interno
no detectado
```

**Interpreta:** el control basado en **monto acumulado** era ciego a este patrón, y el basado en
**frecuencia** lo detectó de inmediato. Y el hallazgo de fondo fue de segregación: quien operaba la
caja realizaba su propio arqueo, lo que hacía posible la compensación.

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| "Deposité un cheque y no puedo girar" | Documento en canje: saldo contable ≠ disponible | 3, clase 3 |
| Cheque devuelto | Reversa del abono e informe al cliente | 3, clase 3 |
| Verificación adicional en un giro alto | Umbral operativo y de reporte | 12, clase 8 |
| Conteo del efectivo frente al cliente | Control que protege a ambas partes | 10, clase 11 |
| Comprobante de toda operación | Requisito de trazabilidad | 12, clase 14 |

## 🧪 Práctica

En `labs/lab-03.md`:

1. Construye la conciliación entre saldo contable y disponible de una cuenta.
2. Traza el proceso de canje de un cheque con sus plazos y posibles resultados.
3. Diseña los controles de un giro por caja según su monto.
4. Analiza un registro de diferencias de caja por frecuencia y por patrón.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| El cliente reclama por fondos no disponibles | No se le informó el plazo de canje | Informa al momento del depósito. |
| Se gira contra saldo contable | Disponible no verificado | Verifica siempre el disponible. |
| Diferencias de caja no registradas | Umbral mínimo mal aplicado | Toda diferencia se registra. |
| Se vigila solo el monto acumulado | Patrón de compensación no detectado | Vigila también la frecuencia. |
| El arqueo lo hace quien operó | Sin segregación | Control por persona distinta. |
| Sin arqueos sorpresivos | Predictibilidad del control | Aleatoriza la frecuencia. |

## ❓ Preguntas de comprobación

1. ¿Qué diferencia hay entre saldo contable y disponible y de qué se compone?
2. Describe el proceso de canje con sus plazos y resultados posibles.
3. ¿Qué controles adicionales activa un giro de monto alto?
4. ¿Por qué la frecuencia de diferencias de caja es más informativa que el monto?
5. ¿Por qué el arqueo no puede realizarlo quien operó la caja?

## 📥 Entregable

Guarda en `portfolio/parte-10/clase-05/`:

- la conciliación entre saldo contable y disponible de un caso;
- el proceso de canje trazado con plazos y resultados;
- la matriz de controles de giro por tramo de monto;
- el análisis de diferencias de caja por frecuencia con sus hallazgos.

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

- Rose, P. y Hudgins, S. (2013). *Bank Management & Financial Services* (9.ª ed.). McGraw-Hill. Operaciones de caja y servicios transaccionales.
- Committee on Payments and Market Infrastructures (2012). *Principles for Financial Market Infrastructures*. CPMI-IOSCO/BIS. Compensación de instrumentos de pago.
- Basel Committee on Banking Supervision (2011). *Principles for the Sound Management of Operational Risk*. BIS. Controles de proceso y segregación.
- COSO (2013). *Internal Control — Integrated Framework*. Actividades de control y conciliaciones.
- World Bank (2017). *Good Practices for Financial Consumer Protection*. Banco Mundial. Información sobre disponibilidad de fondos.
- Verificación local: revisa los plazos de canje vigentes en tu país, las causales de devolución de documentos y los umbrales de reporte de operaciones en efectivo.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 04 · Apertura y administración de cuentas](04-apertura-y-administracion-de-cuentas.md) | [Parte 10](../README.md) · [Programa](../../../SYLLABUS.md) | [06 · Transferencias →](06-transferencias.md) |
<!-- gen:footer:end -->
