---
part: 10
class: 1
title: "Modelo operativo de un banco"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 01 · Modelo operativo de un banco

> [← Índice de la parte](../README.md) · [Índice de la parte](../README.md) · [02 · Captaciones →](02-captaciones.md)

**Parte 10 — Operaciones bancarias** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Comprender cómo funciona un banco por dentro: qué áreas existen, qué hace cada una, cómo se conectan y
dónde se generan los riesgos operacionales. Sin este mapa, las decisiones de producto, de riesgo y de
tecnología se toman sin entender sus consecuencias operativas.

## 📚 Objetivos

Al finalizar podrás:

1. **Describir** la estructura funcional de un banco y sus áreas.
2. **Distinguir** las funciones de negocio, de soporte y de control.
3. **Trazar** el recorrido completo de una operación por la organización.
4. **Identificar** los puntos de control y de riesgo operacional.
5. **Explicar** la arquitectura de sistemas y su efecto en la operación.

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
| `front office` | Áreas que atienden al cliente y originan negocio. |
| `middle office` | Áreas que controlan, miden y gestionan riesgos. |
| `back office` | Áreas que procesan, liquidan, contabilizan y concilian. |
| `segregación de funciones` | Quien origina no procesa, quien procesa no controla. |
| `core bancario` | Sistema central que mantiene cuentas, saldos y movimientos. |
| `conciliación` | Verificación de que dos registros independientes coinciden. |
| `riesgo operacional` | Pérdida por fallas de procesos, personas, sistemas o eventos externos. |

## 🧠 Modelo mental

Un banco procesa **tres flujos simultáneos** por cada operación:

```text
FLUJO DE INFORMACIÓN   la operación se registra y se comunica
FLUJO DE DINERO        los fondos se mueven entre cuentas
FLUJO DE RIESGO        la exposición cambia y debe medirse
```

Los tres deben cuadrar. Cuando el flujo de información y el de dinero se separan —una operación
registrada que no se liquidó, o un pago realizado sin registro— se produce una pérdida operacional.

## 📖 Desarrollo

### 1. Estructura funcional

```text
NEGOCIO (front office)
  banca de personas · banca de empresas · banca privada
  tesorería y mercados · banca de inversión

CONTROL (middle office)
  riesgo de crédito · riesgo de mercado · riesgo operacional
  cumplimiento · control de gestión

SOPORTE (back office)
  operaciones · contabilidad · tecnología · recursos humanos
  legal · seguridad

INDEPENDIENTES
  auditoría interna · contraloría
```

**Segregación mínima obligatoria:**

```text
· quien origina una operación NO la aprueba
· quien aprueba NO la procesa
· quien procesa NO la contabiliza
· quien contabiliza NO la concilia
· quien opera NO administra los accesos al sistema
```

Cada separación existe porque su ausencia permitió un fraude documentado. La concentración de dos o
más de estas funciones en una persona es uno de los hallazgos más frecuentes de auditoría.

### 2. Recorrido de una operación

```text
SOLICITUD DE CRÉDITO DE CONSUMO

1. ORIGINACIÓN (sucursal o canal digital)
   captura de datos · verificación de identidad · consulta de informes

2. EVALUACIÓN (motor de decisión + analista si corresponde)
   renta admisible · endeudamiento · scoring · política

3. APROBACIÓN (automática o comité, según facultades)
   registro de la decisión y de su fundamento

4. FORMALIZACIÓN (operaciones)
   generación de documentos · firma · verificación de completitud

5. DESEMBOLSO (operaciones + tesorería)
   validación de cuenta destino · abono · registro contable

6. CONTABILIZACIÓN (contabilidad)
   asiento de colocación · provisión inicial · comisiones

7. SEGUIMIENTO (riesgo + negocio)
   monitoreo de pago · alertas · migración de calificación

8. COBRANZA (si corresponde)
   gestión segmentada · reestructuración · castigo
```

**Puntos de control en el recorrido:**

| Etapa | Control | Riesgo que mitiga |
|---|---|---|
| 1 | Verificación de identidad | Fraude de identidad |
| 2 | Segregación originación/evaluación | Aprobación indebida |
| 3 | Facultades por monto | Exceso de atribuciones |
| 4 | Verificación documental | Operación inexigible |
| 5 | Validación de cuenta destino | Desvío de fondos |
| 6 | Cuadratura contable diaria | Descuadre y fraude |
| 7 | Alertas automáticas | Deterioro no detectado |
| 8 | Registro de gestiones | Conducta indebida |

### 3. Arquitectura de sistemas

```text
CORE BANCARIO
  cuentas · saldos · movimientos · productos · contabilidad

SISTEMAS SATÉLITE
  originación de crédito · scoring · cobranza
  canales (sucursal, web, aplicación, cajeros)
  medios de pago · tesorería · comercio exterior
  cumplimiento · riesgo · información de gestión

INTEGRACIÓN
  interfaces · colas de mensajes · procesos por lotes
  servicios de consulta en línea
```

**Dos modelos de procesamiento:**

```text
EN LÍNEA (tiempo real)     el saldo se actualiza al instante
                           transferencias, tarjetas, consultas

POR LOTES (batch)          el procesamiento ocurre en un cierre diario
                           devengo de intereses, provisiones, contabilidad
```

**El cierre diario** es el proceso más crítico de la operación bancaria: consolida todos los
movimientos, devenga intereses, calcula posiciones y produce la contabilidad. Un cierre que falla
detiene la operación del día siguiente.

### 4. El día operativo

```text
06:00  apertura de sistemas · verificación del cierre anterior
08:00  apertura de sucursales y canales
09:00  inicio de la sesión de pagos de alto valor
12:00  corte de operaciones de canje
15:00  cierre de sucursales
16:00  corte de operaciones interbancarias
17:00  liquidación de la cámara de compensación
18:00  inicio del cierre: consolidación de movimientos
20:00  devengo, provisiones, contabilidad
23:00  conciliaciones automáticas · generación de reportes
02:00  respaldo · procesos de fin de mes si corresponde
05:00  validación del cierre · disponibilidad de sistemas
```

**Cada corte horario tiene consecuencias:** una transferencia enviada después del corte se liquida al
día siguiente, y esa diferencia importa para el cliente y para la posición de liquidez del banco.

### 5. Riesgo operacional

```text
categorías estándar:
  · fraude interno
  · fraude externo
  · prácticas laborales
  · clientes, productos y prácticas de negocio
  · daños a activos físicos
  · interrupción del negocio y fallas de sistemas
  · ejecución, entrega y gestión de procesos
```

**La última categoría concentra la mayor frecuencia** y la más baja severidad individual: errores de
digitación, operaciones duplicadas, conciliaciones no realizadas. Su gestión es de proceso, no de
capital.

```text
matriz de riesgo operacional por proceso:

proceso              frecuencia   severidad   control principal
apertura de cuenta      alta        baja       validación automática
transferencia          muy alta     baja       límites y doble validación
desembolso              media       alta       segregación y validación de cuenta
cierre diario           baja        muy alta   cuadratura y respaldo
custodia de valores     baja        muy alta   conciliación con depósito central
```

## 🧮 Ejemplo guiado

**Situación.** Un banco detecta un descuadre de 84 millones en su cierre diario. Diagnostica el
proceso.

```text
SÍNTOMA
  la cuadratura del cierre no coincide: activos superan pasivos + patrimonio en 84 millones
  el cierre no puede completarse hasta resolverlo
```

**Paso 1 — identifica el alcance.**

```text
el descuadre está en una cuenta puente de operaciones pendientes
saldo de la cuenta puente: 84 000 000
en condiciones normales debe cerrar en cero
```

**Paso 2 — analiza los movimientos de la cuenta puente del día.**

```text
movimientos: 1 247 operaciones
suma de cargos: 12 486 000 000
suma de abonos: 12 402 000 000
diferencia: 84 000 000
```

**Paso 3 — busca operaciones sin contrapartida.**

```text
al cruzar por identificador de operación:
  1 243 operaciones tienen cargo y abono
  4 operaciones tienen solo cargo, sin abono

  operación 88412: 21 000 000
  operación 88413: 18 500 000
  operación 88419: 26 000 000
  operación 88427: 18 500 000
  TOTAL: 84 000 000  ✓ coincide
```

**Paso 4 — investiga las cuatro operaciones.**

```text
las cuatro son transferencias a otro banco, emitidas entre las 16:02 y las 16:18
el corte de operaciones interbancarias es a las 16:00

→ las transferencias se cargaron a la cuenta del cliente
→ NO se enviaron al sistema de pagos porque el corte ya había pasado
→ quedaron en la cuenta puente esperando el siguiente ciclo
```

**Paso 5 — determina si es un error o un comportamiento esperado.**

```text
comportamiento esperado del sistema:
  operaciones posteriores al corte deben quedar en cuenta puente
  y liquidarse al día siguiente

entonces, ¿por qué el descuadre?
  porque el proceso de cierre NO consideraba el saldo de la cuenta puente
  como partida conciliatoria válida

→ NO es un error de operación: es un error del PROCESO DE CIERRE
```

**Paso 6 — evalúa el riesgo del hallazgo.**

```text
el descuadre en sí no representa pérdida: el dinero está identificado
PERO el proceso de cierre no distingue un descuadre legítimo de uno fraudulento

consecuencia: si alguien desviara 84 millones, el proceso mostraría
el mismo síntoma y podría atribuirse a operaciones post-corte

ESE es el riesgo real: el control no discrimina
```

**Paso 7 — acciones correctivas.**

```text
INMEDIATO
  1. completar el cierre reconociendo la cuenta puente como partida conciliatoria
  2. verificar que las cuatro operaciones se liquiden al día siguiente

PROCESO
  3. modificar el cierre para reconocer automáticamente las operaciones post-corte
     y presentarlas como partida conciliatoria identificada
  4. establecer que toda partida conciliatoria debe tener identificador de operación
     y antigüedad máxima de 1 día hábil
  5. alerta si el saldo de la cuenta puente supera un umbral o si una partida
     supera 1 día hábil

CONTROL
  6. conciliación diaria de la cuenta puente, con responsable designado
  7. la conciliación la realiza un área distinta de la que opera las transferencias

COMUNICACIÓN
  8. informar a los cuatro clientes que su transferencia se liquidará al día siguiente
  9. revisar si la política de horarios está informada en los canales
```

**Interpreta:** el descuadre no era una pérdida ni un fraude: era **un control mal diseñado que no
distinguía lo legítimo de lo anómalo**. Ese es el hallazgo valioso, y su corrección —reconocer la
partida conciliatoria con identificador y antigüedad— convierte un control ciego en uno que sí
detectaría un desvío real.

## 🏦 Del cliente al banco

| Vista del cliente | Vista operativa | Parte |
|---|---|---|
| "Mi transferencia no llegó hoy" | Se emitió después del corte interbancario | 10, clase 6 |
| Saldo actualizado al instante | Procesamiento en línea | 10, clase 5 |
| Intereses que aparecen al cierre | Devengo en el proceso por lotes | 10, clase 2 |
| Sistema no disponible de madrugada | Ventana de cierre y respaldo | 11, clase 8 |
| Verificación adicional en un desembolso | Segregación de funciones | 12, clase 12 |

## 🧪 Práctica

En `labs/lab-01.md`:

1. Mapea la estructura funcional de un banco con sus áreas y su clasificación.
2. Traza el recorrido completo de tres operaciones distintas con sus puntos de control.
3. Construye la matriz de riesgo operacional de cinco procesos.
4. Diagnostica un descuadre de cierre siguiendo los siete pasos del ejemplo.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Una persona origina y procesa | Segregación incumplida | Separa las funciones. |
| El cierre no distingue descuadres legítimos | Control ciego | Identifica cada partida conciliatoria. |
| Partidas conciliatorias antiguas | Sin control de antigüedad | Umbral máximo de días hábiles. |
| El cliente no conoce los horarios de corte | Información no publicada | Publica los cortes por canal y producto. |
| La conciliación la hace quien opera | Sin independencia | Área distinta de la operativa. |
| El riesgo operacional se gestiona con capital | Enfoque incorrecto | La mayor frecuencia se gestiona con procesos. |

## ❓ Preguntas de comprobación

1. ¿Qué tres flujos procesa un banco por cada operación y qué ocurre si se separan?
2. Enumera las cinco segregaciones mínimas obligatorias.
3. ¿Qué distingue el procesamiento en línea del procesamiento por lotes?
4. ¿Por qué el cierre diario es el proceso más crítico?
5. ¿Por qué un control que no distingue lo legítimo de lo anómalo es un riesgo?

## 📥 Entregable

Guarda en `portfolio/parte-10/clase-01/`:

- el mapa funcional de un banco con la clasificación de cada área;
- el recorrido de tres operaciones con sus puntos de control;
- la matriz de riesgo operacional de cinco procesos;
- el diagnóstico de un descuadre con sus acciones correctivas.

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

- Rose, P. y Hudgins, S. (2013). *Bank Management & Financial Services* (9.ª ed.). McGraw-Hill. Capítulos 1 y 2: organización y operación de un banco.
- Basel Committee on Banking Supervision (2011). *Principles for the Sound Management of Operational Risk*. BIS. Categorías y gestión del riesgo operacional. <https://www.bis.org/publ/bcbs195.htm>
- Basel Committee on Banking Supervision (2021). *Principles for Operational Resilience*. BIS.
- COSO (2013). *Internal Control — Integrated Framework*. Segregación de funciones y actividades de control.
- Committee on Payments and Market Infrastructures (2012). *Principles for Financial Market Infrastructures*. CPMI-IOSCO/BIS. Ciclos de liquidación.
- Verificación local: revisa los horarios de corte del sistema de pagos de alto valor de tu país y las exigencias de tu supervisor sobre segregación de funciones.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← Índice de la parte](../README.md) | [Parte 10](../README.md) · [Programa](../../../SYLLABUS.md) | [02 · Captaciones →](02-captaciones.md) |
<!-- gen:footer:end -->
