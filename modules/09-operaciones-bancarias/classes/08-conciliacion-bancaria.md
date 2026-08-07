---
part: 10
class: 8
title: "Conciliación bancaria"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 08 · Conciliación bancaria

> [← 07 · Compensación y liquidación](07-compensacion-y-liquidacion.md) · [Índice de la parte](../README.md) · [09 · Medios de pago →](09-medios-de-pago.md)

**Parte 10 — Operaciones bancarias** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Dominar el control que verifica que dos registros independientes coincidan, y que es el mecanismo por
el que se detectan la mayoría de los errores y fraudes operacionales. Una conciliación bien diseñada
detecta; una mal diseñada da falsa tranquilidad.

## 📚 Objetivos

Al finalizar podrás:

1. **Construir** una conciliación bancaria completa con sus partidas.
2. **Clasificar** las partidas conciliatorias y su tratamiento.
3. **Establecer** los controles de antigüedad y de resolución.
4. **Detectar** los patrones que indican error o fraude.
5. **Diseñar** un proceso de conciliación con la independencia adecuada.

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
| `conciliación` | Comparación de dos registros independientes del mismo hecho. |
| `partida conciliatoria` | Diferencia explicable entre ambos registros. |
| `antigüedad` | Días desde que la partida apareció. Es el indicador de calidad del proceso. |
| `partida no identificada` | Diferencia sin explicación. Es siempre un hallazgo. |
| `conciliación automática` | Cruce por reglas. Debe complementarse con revisión de excepciones. |
| `independencia` | Quien concilia no opera ni contabiliza. |

## 🧠 Modelo mental

Una conciliación responde una pregunta simple con una exigencia estricta:

```text
¿coinciden los dos registros?
  sí  → sin partidas: la conciliación cierra
  no  → CADA diferencia debe tener nombre, monto, origen y fecha de resolución
```

**Una diferencia sin explicación no es una partida conciliatoria: es un hallazgo.** Confundirlas es lo
que convierte una conciliación en un trámite.

## 📖 Desarrollo

### 1. Estructura de una conciliación

```text
CONCILIACIÓN DE LA CUENTA CORRIENTE — al 30 de abril

  Saldo según el banco                            18 420 000
  (+) depósitos en tránsito                        2 180 000
  (−) cheques girados y no cobrados               −3 640 000
  (+) abonos del banco no registrados                140 000
  (−) cargos del banco no registrados               −285 000
  (+/−) errores del banco                             0
  = Saldo conciliado                              16 815 000

  Saldo según nuestros registros                  16 940 000
  (+/−) errores propios                             −125 000
  = Saldo conciliado                              16 815 000   ✓ COINCIDE
```

**Ambos lados deben llegar al mismo saldo conciliado.** Si no coinciden, hay una partida no
identificada.

### 2. Clasificación de partidas

| Tipo | Origen | Tratamiento | Antigüedad máxima |
|---|---|---|---|
| Depósito en tránsito | Registrado por nosotros, no por el banco | Se regulariza solo | 2 días hábiles |
| Cheque no cobrado | Girado y no presentado | Se regulariza al cobrarse | Hasta la caducidad |
| Cargo del banco no registrado | Comisión, impuesto, interés | Registrar | 1 día |
| Abono del banco no registrado | Transferencia recibida no identificada | Identificar y registrar | 3 días |
| Error del banco | Cargo o abono indebido | Reclamar y hacer seguimiento | 5 días |
| Error propio | Digitación, duplicación, omisión | Corregir | 1 día |
| **No identificada** | **Desconocido** | **Investigar** | **0: es un hallazgo** |

### 3. Controles de antigüedad

```text
el indicador de calidad de una conciliación NO es que cierre:
es la ANTIGÜEDAD de sus partidas
```

```text
REPORTE DE ANTIGÜEDAD

  tramo          partidas   monto        estado
  0–2 días          48      4 180 000    normal
  3–5 días          12        860 000    revisar
  6–15 días          6        420 000    escalar
  16–30 días         3        180 000    escalar
  > 30 días          2        340 000    ✗ HALLAZGO
```

**Una partida de más de 30 días no es una partida conciliatoria: es un problema no resuelto.** Las
razones habituales:

```text
· nadie tiene asignada la responsabilidad de resolverla
· requiere una gestión con un tercero que no se ha hecho
· oculta un error que nadie quiere reconocer
· oculta un desvío
```

### 4. Patrones que indican error o fraude

| Patrón | Qué sugiere |
|---|---|
| Partidas que aparecen y desaparecen sin resolución documentada | Compensación entre errores |
| Partidas de monto similar y signo opuesto | Posible desvío temporal con reposición |
| Aumento sostenido del número de partidas | Deterioro del proceso operativo |
| Partidas concentradas en una cuenta o un operador | Foco de investigación |
| Conciliaciones que siempre cierran exactamente | Posible ajuste forzado |
| Partidas antiguas que se castigan sin investigar | Ocultamiento de pérdidas |

**El quinto patrón es contraintuitivo:** una conciliación que **siempre** cierra sin partidas en un
volumen alto de operaciones es estadísticamente improbable, y sugiere que se está forzando el cuadre
con un asiento de ajuste en lugar de investigar.

### 5. Diseño del proceso

```text
INDEPENDENCIA
  quien concilia NO opera la cuenta
  quien concilia NO contabiliza
  quien aprueba los ajustes NO concilia

FRECUENCIA
  cuentas operativas de alto volumen: diaria
  cuentas de menor movimiento: semanal
  cuentas de tránsito y puente: DIARIA sin excepción

AUTOMATIZACIÓN
  cruce automático por monto, fecha y referencia
  revisión manual solo de las excepciones
  regla: si más del 15 % requiere revisión manual, las reglas están mal calibradas

DOCUMENTACIÓN
  cada partida con: descripción, monto, fecha de origen, responsable, fecha
  comprometida de resolución, estado

ESCALAMIENTO
  partidas sobre umbral de monto: escalamiento inmediato
  partidas sobre umbral de antigüedad: escalamiento automático
  partidas no identificadas: escalamiento inmediato, sin excepción
```

## 🧮 Ejemplo guiado

**Situación.** Auditas el proceso de conciliación de un banco y revisas la cuenta de tránsito de
transferencias.

```text
CUENTA DE TRÁNSITO DE TRANSFERENCIAS
  saldo al cierre del mes: 18 400 000
  debe cerrar en cero al término de cada día hábil
```

**Paso 1 — revisa la composición del saldo.**

```text
partidas que componen el saldo:
  operaciones post-corte del último día         12 800 000   (legítimas)
  partidas de 3 a 10 días                        2 100 000
  partidas de 11 a 30 días                       1 900 000
  partidas de más de 30 días                     1 600 000
  TOTAL                                         18 400 000
```

**5 600 000 en partidas de más de 3 días en una cuenta que debe cerrar diariamente.**

**Paso 2 — analiza las partidas de más de 30 días.**

```text
  partida 1   680 000   antigüedad 47 días   descripción: "diferencia"
  partida 2   420 000   antigüedad 61 días   descripción: "pendiente aclarar"
  partida 3   310 000   antigüedad 38 días   descripción: "en gestión"
  partida 4   190 000   antigüedad 92 días   descripción: (vacía)
```

**Ninguna tiene descripción útil, responsable ni fecha comprometida.** Las cuatro son hallazgos, no
partidas conciliatorias.

**Paso 3 — investiga la partida más antigua.**

```text
partida 4: 190 000, 92 días, sin descripción

rastreo del origen:
  · asiento del 15 de enero, cuenta de tránsito contra cuenta puente
  · sin documento de respaldo
  · usuario: un operador del área de transferencias
  · sin aprobación registrada
```

**Paso 4 — busca operaciones relacionadas.**

```text
búsqueda de asientos del mismo usuario en la cuenta de tránsito:
  15-ene   cargo 190 000    sin respaldo
  22-ene   abono 190 000    sin respaldo    ← se compensó
  04-feb   cargo 240 000    sin respaldo
  11-feb   abono 240 000    sin respaldo    ← se compensó
  19-mar   cargo 190 000    sin respaldo    ← NO se compensó: es la partida 4
```

**El patrón de "cargo seguido de abono del mismo monto" apareció tres veces.** Las dos primeras se
compensaron; la tercera quedó abierta.

**Paso 5 — formula la hipótesis.**

```text
HIPÓTESIS: uso temporal de fondos con reposición posterior
  · se carga la cuenta de tránsito (los fondos salen)
  · se repone antes de que alguien lo note (el abono compensa)
  · la tercera vez, la reposición no ocurrió

el patrón es el mismo de las diferencias de caja de la clase 5,
aplicado a una cuenta contable en lugar de a efectivo físico
```

**Paso 6 — evalúa por qué el control no lo detectó.**

```text
□ ¿la cuenta se concilia diariamente?
  registro: sí, formalmente
  
□ ¿las partidas tienen antigüedad controlada?
  NO: el reporte muestra el saldo total, no la antigüedad por partida

□ ¿existe escalamiento por antigüedad?
  NO

□ ¿quién concilia?
  el mismo equipo que opera las transferencias  ✗ SIN INDEPENDENCIA

□ ¿se revisan los asientos manuales sin respaldo?
  NO
```

**Paso 7 — el hallazgo de fondo.**

```text
la conciliación EXISTÍA y era INEFECTIVA por cuatro razones:
  1. no controlaba antigüedad por partida
  2. no escalaba automáticamente
  3. la realizaba el área que opera
  4. no revisaba asientos manuales sin respaldo

el saldo total de la cuenta parecía razonable porque los 12 800 000
de operaciones post-corte legítimas ocultaban los 5 600 000 anómalos
```

**Paso 8 — acciones.**

```text
INMEDIATO
  1. investigación del usuario y de las cinco operaciones identificadas
  2. revisión de todas las cuentas de tránsito y puente con el mismo criterio
  3. suspensión de facultades del usuario mientras dure la investigación

DE PROCESO
  4. reporte diario de antigüedad POR PARTIDA, no solo saldo total
  5. escalamiento automático: partida sobre 3 días hábiles → supervisor
                              partida sobre 10 días → gerencia
                              partida no identificada → inmediato
  6. la conciliación de cuentas de tránsito la realiza un área independiente
  7. todo asiento manual en cuentas de tránsito exige respaldo y aprobación
  8. alerta por patrón: cargo y abono del mismo monto en la misma cuenta
     por el mismo usuario dentro de 30 días

DE GOBIERNO
  9. indicador de calidad de conciliaciones en el tablero de riesgo operacional:
     · número de partidas sobre 5 días
     · monto de partidas no identificadas
     · antigüedad promedio ponderada
 10. auditoría trimestral de una muestra de conciliaciones
```

**Interpreta:** el banco tenía conciliaciones diarias y **el control era inefectivo** porque medía el
saldo y no la antigüedad. El patrón de cargo-abono se repitió tres veces sin detección, y solo la
tercera —que no se compensó— dejó rastro visible. La corrección más importante no es el escalamiento:
es **la independencia de quien concilia**.

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| Cargo no reconocido en la cartola | Puede ser partida conciliatoria en investigación | 3, clase 2 |
| Abono que aparece días después | Depósito en tránsito o abono no identificado | 10, clase 5 |
| Reclamo por diferencia | Se investiga contra los registros del banco | 4, clase 9 |
| Conciliación de la propia empresa | Mismo método aplicado a su cuenta corriente | 5, clase 8 |

## 🧪 Práctica

En `labs/lab-04.md`, sección de conciliación:

1. Construye una conciliación bancaria completa con todas sus partidas.
2. Elabora el reporte de antigüedad y define los umbrales de escalamiento.
3. Identifica los seis patrones de error o fraude en un registro sintético.
4. Diseña el proceso de conciliación con su matriz de independencia.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se controla el saldo y no la antigüedad | Indicador equivocado | Reporta antigüedad por partida. |
| Partidas antiguas sin responsable | Sin asignación | Cada partida con responsable y fecha comprometida. |
| Concilia el área que opera | Sin independencia | Área distinta de la operativa. |
| Se fuerza el cuadre con un ajuste | Investigación evitada | Toda diferencia se explica antes de ajustar. |
| Asientos manuales sin respaldo | Control ausente | Exige documento y aprobación. |
| La conciliación siempre cierra exacta | Posible ajuste forzado | Estadísticamente improbable en alto volumen. |

## ❓ Preguntas de comprobación

1. ¿Cuál es la diferencia entre una partida conciliatoria y un hallazgo?
2. ¿Por qué la antigüedad es mejor indicador de calidad que el saldo?
3. Nombra cuatro patrones que sugieren error o fraude en una conciliación.
4. ¿Por qué una conciliación que siempre cierra exactamente es sospechosa?
5. ¿Qué separaciones exige la independencia del proceso?

## 📥 Entregable

Guarda en `portfolio/parte-10/clase-08/`:

- una conciliación bancaria completa con todas sus partidas clasificadas;
- el reporte de antigüedad con los umbrales de escalamiento definidos;
- la identificación de patrones en un registro sintético;
- el diseño del proceso con su matriz de independencia y sus indicadores.

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

- COSO (2013). *Internal Control — Integrated Framework*. Committee of Sponsoring Organizations. Conciliaciones como actividad de control. <https://www.coso.org/>
- Basel Committee on Banking Supervision (2011). *Principles for the Sound Management of Operational Risk*. BIS. Controles de proceso y segregación.
- IAASB (2021). *ISA 330: The Auditor's Responses to Assessed Risks*. Pruebas sobre conciliaciones y asientos manuales.
- IAASB (2021). *ISA 240: The Auditor's Responsibilities Relating to Fraud*. Asientos manuales como foco de riesgo de fraude.
- Basel Committee on Banking Supervision (2013). *BCBS 239: Principles for effective risk data aggregation*. BIS. Calidad y trazabilidad del dato.
- Verificación local: revisa las exigencias de tu supervisor sobre conciliaciones, plazos de resolución de partidas y control de cuentas de tránsito.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 07 · Compensación y liquidación](07-compensacion-y-liquidacion.md) | [Parte 10](../README.md) · [Programa](../../../SYLLABUS.md) | [09 · Medios de pago →](09-medios-de-pago.md) |
<!-- gen:footer:end -->
