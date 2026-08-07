---
part: 5
class: 15
title: "Proyecto: estados financieros completos"
level: intermedio
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 15 · Proyecto: estados financieros completos

> [← 14 · Análisis vertical y horizontal](14-analisis-vertical-y-horizontal.md) · [Índice de la parte](../README.md) · [Proyecto de la parte →](../project/README.md)

**Parte 05 — Contabilidad financiera** · **Nivel:** Intermedio — requiere las partes anteriores · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Producir el ciclo contable completo de una empresa durante un periodo, desde los documentos hasta los
cuatro estados financieros con sus notas, y luego analizarlos como lo haría un tercero. Es el
entregable que demuestra dominio de toda la parte y el insumo directo del análisis crediticio de la
Parte 9.

Esta clase cierra la parte construyendo un juego completo de estados a partir de operaciones, con sus notas y su coherencia comprobada. No introduce técnica nueva: introduce la exigencia de que los cuatro estados cuadren entre sí, que es donde aparecen los errores que ninguna clase por separado mostraba.

## 📚 Objetivos

Al finalizar podrás:

1. **Ejecutar** el ciclo contable completo de un periodo.
2. **Preparar** los cuatro estados financieros con información comparativa.
3. **Redactar** las notas mínimas que hacen interpretables los estados.
4. **Analizar** tus propios estados con las técnicas de la clase 14.
5. **Defender** las estimaciones y políticas contables aplicadas.

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

Los cinco primeros términos son los componentes de la entrega y el último, lo que se evalúa. La **coherencia entre estados** es el criterio central: cada estado por separado puede estar bien y el conjunto no cuadrar, y esa comprobación es la que hace un auditor primero.

| Concepto | Comprensión verificable |
|---|---|
| `juego completo` | Situación financiera, resultados y otro resultado integral, cambios en el patrimonio, flujo de efectivo y notas. |
| `nota de políticas` | Declara marco normativo, bases de medición y estimaciones aplicadas. |
| `información comparativa` | El periodo anterior, obligatorio para todos los estados. |
| `revelación material` | Todo hecho que pueda influir en las decisiones de los usuarios. |
| `coherencia entre estados` | Los cuatro estados deben conciliar entre sí. Es el control final. |
| `defensa de estimaciones` | Justificación de vidas útiles, provisiones y criterios aplicados. |

## 🧠 Modelo mental

Los cuatro estados forman **un sistema cerrado** y cada uno debe conciliar con los otros:

```text
resultado del ejercicio        → estado de cambios en el patrimonio
patrimonio final               → estado de situación financiera
resultado + ajustes            → flujo operativo
variación de efectivo del flujo → variación de efectivo del balance
```

Si alguna conciliación falla, hay un error. **Ese conjunto de cuatro controles es la verificación final
del proyecto.**

## 📖 Desarrollo

### 1. Alcance del proyecto

El proyecto tiene un alcance acotado y declarado. La tabla lo delimita, incluida la columna de lo que queda fuera.

```text
· empresa ficticia con actividad comercial o de servicios
· periodo: 12 meses
· mínimo 60 transacciones de al menos 12 tipos distintos
· al menos 6 asientos de ajuste al cierre
· los cuatro estados financieros con comparativo del periodo anterior
· mínimo 8 notas
· análisis vertical, horizontal y DuPont de los estados producidos
```

### 2. Estructura de entrega

La entrega tiene una estructura fija que reproduce la de un juego real de estados financieros. La tabla la recoge.

```text
portfolio/parte-05/clase-15/
  01-transacciones.csv       las 60+ transacciones con documento de respaldo
  02-libro-diario.md         asientos en orden cronológico
  03-libro-mayor.md          mayorización por cuenta
  04-balance-comprobacion.md previo y ajustado
  05-estados-financieros.md  los cuatro estados con comparativo
  06-notas.md                mínimo 8 notas
  07-analisis.md             vertical, horizontal, ratios y DuPont
  08-defensa.md              justificación de estimaciones y políticas
```

### 3. Las notas mínimas

Las notas no son un anexo: son parte del estado financiero y hay un mínimo que no se puede omitir. La tabla lo recoge.

| # | Nota | Contenido obligatorio |
|---:|---|---|
| 1 | Información de la entidad | Actividad, domicilio, periodo cubierto |
| 2 | Bases de preparación | Marco normativo aplicado, moneda, supuesto de empresa en marcha |
| 3 | Políticas contables | Reconocimiento de ingresos, medición de existencias, depreciación |
| 4 | Estimaciones y juicios | Vidas útiles, provisión de incobrables, sus supuestos |
| 5 | Efectivo y equivalentes | Composición y restricciones |
| 6 | Cuentas por cobrar | Antigüedad y provisión, con movimiento del periodo |
| 7 | Propiedades y equipos | Movimiento de costo y depreciación acumulada |
| 8 | Préstamos | Perfil de vencimientos, tasas y garantías |
| 9 | Contingencias y compromisos | Avales, juicios, compromisos de compra |
| 10 | Hechos posteriores | Eventos relevantes entre el cierre y la emisión |

Las notas 4, 6 y 8 son las que un analista de crédito lee primero. Un juego de estados sin ellas es
formalmente completo y prácticamente inutilizable.

### 4. Los cuatro controles de coherencia

Cuatro comprobaciones enfrentan los estados entre sí, y su fallo indica un error concreto. La tabla las recoge con lo que revela cada una.

```text
CONTROL 1  ecuación contable
  activo total = pasivo total + patrimonio total

CONTROL 2  conexión resultado-patrimonio
  PN final = PN inicial + resultado + ORI + aportes − dividendos

CONTROL 3  conexión flujo-balance
  variación de efectivo del flujo = efectivo final − efectivo inicial del balance

CONTROL 4  conexión resultado-flujo
  el resultado del estado de resultados es el punto de partida del flujo operativo
```

Además, controles de razonabilidad:

```text
□ ninguna cuenta con saldo anómalo
□ la depreciación del periodo coincide con el movimiento de la depreciación acumulada
□ la provisión del periodo coincide con el movimiento de la provisión acumulada
□ los intereses del resultado son coherentes con la deuda promedio y su tasa
□ los días de cobro, de existencias y de pago son razonables para el sector
```

### 5. La defensa

Tres preguntas que hay que poder responder con argumentos, no con "así lo hice":

**"¿Por qué elegiste esa vida útil?"**

```text
respuesta débil:  "es la que usa la mayoría"
respuesta fuerte: "10 años, consistente con la vida técnica del equipo según
                   el fabricante, con la práctica del sector (8–12 años) y con
                   nuestro plan de reposición. Un cambio a 8 años reduciría el
                   resultado en 240 000; a 12 años lo aumentaría en 160 000."
```

**"¿Por qué tu provisión de incobrables es de 6,2 %?"**

```text
respuesta fuerte: "Método de antigüedad con tasas por tramo derivadas de la
                   experiencia de los últimos 24 meses. La cartera sobre 90
                   días es el 4,1 % del total. Con las tasas del periodo
                   anterior la provisión sería 6,0 %; el aumento responde al
                   envejecimiento de dos clientes concretos, revelados en la nota 6."
```

**"¿Tu empresa es viable?"**

```text
respuesta fuerte: "El flujo operativo es positivo (1,4 M) y cubre 2,1 veces el
                   servicio de la deuda. El crecimiento consumió 900 000 de
                   capital de trabajo. Las dos vulnerabilidades son la
                   concentración de un cliente en el 34 % de las ventas y un
                   ciclo de conversión de 96 días. Ambas están cuantificadas
                   en el análisis."
```

Lo que distingue una defensa fuerte: **cuantifica la sensibilidad y nombra las vulnerabilidades sin
que se las pregunten**.

## 🧮 Ejemplo guiado

El ejemplo recorre la construcción completa desde las operaciones hasta los cuatro controles de coherencia. Conviene ejecutar los controles aunque todo parezca bien: los tres primeros suelen pasar y el cuarto es el que falla.

**Situación de autoevaluación.** Antes de entregar, aplica esta revisión completa a tu propio trabajo.

**Paso 1 — controles de coherencia.**

```text
CONTROL 1  activo 24 000 000 = pasivo 12 000 000 + patrimonio 12 000 000  ✔
CONTROL 2  PN final 12 000 000 = 10 600 000 + 1 900 000 − 500 000          ✔
CONTROL 3  variación efectivo del flujo 420 000 = 1 240 000 − 820 000      ✔
CONTROL 4  resultado 1 900 000 es el punto de partida del flujo operativo  ✔
```

**Paso 2 — controles de razonabilidad.**

```text
depreciación del resultado          1 200 000
movimiento de depreciación acumulada 1 200 000  ✔
provisión del resultado                340 000
movimiento de provisión acumulada      340 000  ✔
intereses del resultado                490 000
deuda promedio 6 600 000 × tasa 7,4 % = 488 400  ✔ coherente
```

**Paso 3 — indicadores y razonabilidad sectorial.**

```text
días de cobro       79    → sector 60–90   ✔
días de existencias 118   → sector 90–130  ✔
días de pago         88   → sector 60–95   ✔
ciclo de conversión 109 días
razón corriente    2,20   → sector 1,5–2,5 ✔
```

**Paso 4 — análisis DuPont del propio trabajo.**

```text
margen neto       1 900 000/28 000 000 = 6,8 %
rotación          28 000 000/24 000 000 = 1,17
multiplicador     24 000 000/12 000 000 = 2,00
ROE                                      = 15,9 %
```

**Paso 5 — identifica tus propias vulnerabilidades.**

```text
1. rotación del activo de 1,17 es baja para una empresa comercial
   → causa: 47 % del activo en capital de trabajo
2. ciclo de conversión de 109 días exige financiamiento permanente
   → cada 10 % de crecimiento en ventas consume ~840 000 de caja
3. concentración de clientes: verificar en la nota 6
```

**Paso 6 — prepara las respuestas.** Para cada vulnerabilidad, una acción y su cuantificación:

```text
vulnerabilidad 1 → reducir días de existencias de 118 a 95 libera 1 760 000
vulnerabilidad 2 → cada día menos de cobro libera 76 700
vulnerabilidad 3 → política de límite de exposición por cliente
```

**Interpreta:** el proyecto no se evalúa por producir estados que cuadren —eso es el mínimo— sino por
**la capacidad de analizarlos críticamente y de defender cada estimación con números**. Esa es
exactamente la habilidad que la Parte 9 exigirá cuando el objeto de análisis sean los estados
financieros de un tercero.

## 🏦 Del cliente al banco

El cliente entrega estados y el banco los somete a sus propios controles antes de leerlos. La tabla enfrenta las dos lecturas.

| Tu proyecto | Equivalente profesional | Parte |
|---|---|---|
| Juego completo con notas | Estados auditados que exige el banco | 9, clase 2 |
| Nota de estimaciones | Primera lectura del analista | 9, clase 9 |
| Controles de coherencia | Revisión de razonabilidad del analista | 9, clase 9 |
| Defensa de estimaciones | Reunión con el comité de crédito | 13, clase 13 |
| Vulnerabilidades declaradas | Sección de riesgos del informe de crédito | 9, clase 9 |

## 🧪 Práctica

Este proyecto es la práctica. Trabaja en `project/README.md` de esta parte.

1. Diseña la empresa y registra al menos 60 transacciones de 12 tipos.
2. Ejecuta el ciclo completo hasta los cuatro estados con comparativo.
3. Redacta las diez notas y aplica los cuatro controles de coherencia.
4. Analiza tus estados y prepara la defensa de tres estimaciones con su sensibilidad.

## ⚠️ Errores frecuentes

Los síntomas de la tabla aparecen en los controles de coherencia. Las causas están en asientos que afectaron a un estado y no al otro.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Los estados no concilian entre sí | Falta algún control | Aplica los cuatro controles de coherencia. |
| Faltan las notas | Se entregaron solo los estados | El juego completo incluye notas. |
| Las estimaciones no se justifican | No se documentaron | Declara supuesto, fuente y sensibilidad. |
| No hay comparativo | Se preparó un solo periodo | El comparativo es obligatorio. |
| El análisis solo describe | Falta interpretación | Formula hipótesis y cuantifica su efecto. |
| La defensa es "así lo hice" | No se prepararon argumentos | Cuantifica la sensibilidad de cada estimación. |

## ❓ Preguntas de comprobación

1. ¿Qué compone un juego completo de estados financieros?
2. Enumera los cuatro controles de coherencia entre estados.
3. ¿Cuáles son las tres notas que un analista de crédito lee primero y por qué?
4. ¿Qué distingue una defensa fuerte de una estimación de una débil?
5. ¿Por qué producir estados que cuadran es el mínimo y no el objetivo?

## 📥 Entregable

Guarda en `portfolio/parte-05/clase-15/` los ocho archivos de la estructura de entrega:

- transacciones, libro diario, libro mayor y balances de comprobación;
- los cuatro estados financieros con comparativo;
- las diez notas mínimas;
- el análisis completo y la defensa de tres estimaciones con su sensibilidad cuantificada.

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

- IFRS Foundation. *NIC 1 Presentación de Estados Financieros*: juego completo, información comparativa y revelaciones. <https://www.ifrs.org/>
- IFRS Foundation. *NIC 7 Estado de Flujos de Efectivo* y *NIC 8 Políticas Contables, Cambios en Estimaciones y Errores*.
- Kieso, D., Weygandt, J. y Warfield, T. (2022). *Intermediate Accounting* (18.ª ed.). Wiley. Capítulos 3 a 5 y 23: ciclo completo y presentación.
- Palepu, K., Healy, P. y Peek, E. (2019). *Business Analysis and Valuation* (5.ª ed.). Cengage. Capítulos 3 a 5: análisis contable y financiero.
- IFRS Foundation (2017). *Práctica: Materialidad (IFRS Practice Statement 2)*. Criterio para decidir qué revelar.
- Verificación local: revisa qué juego de estados y qué notas exige el supervisor de tu país a las entidades que solicitan crédito o que están obligadas a informar.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 14 · Análisis vertical y horizontal](14-analisis-vertical-y-horizontal.md) | [Parte 05](../README.md) · [Programa](../../../SYLLABUS.md) | [Proyecto de la parte →](../project/README.md) |
<!-- gen:footer:end -->
