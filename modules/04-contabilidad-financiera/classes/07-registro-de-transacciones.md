---
part: 5
class: 7
title: "Registro de transacciones"
level: intermedio
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 07 · Registro de transacciones

> [← 06 · Ingresos, costos y gastos](06-ingresos-costos-y-gastos.md) · [Índice de la parte](../README.md) · [08 · Libro diario y mayor →](08-libro-diario-y-mayor.md)

**Parte 05 — Contabilidad financiera** · **Nivel:** Intermedio — requiere las partes anteriores · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Aprender a convertir un hecho económico en un asiento contable correcto, que es la operación
elemental sobre la que se construye todo lo demás. Esta clase entrega el método de análisis en cuatro
preguntas, el mecanismo del cargo y el abono deducido de la ecuación, y los asientos típicos que
cubren el 90 % de las operaciones de una empresa.

## 📚 Objetivos

Al finalizar podrás:

1. **Analizar** cualquier hecho económico con las cuatro preguntas del método.
2. **Registrar** asientos correctos aplicando cargo y abono deducidos de la ecuación.
3. **Reconocer** los quince asientos típicos de una empresa comercial y de servicios.
4. **Registrar** asientos de ajuste al cierre del periodo.
5. **Detectar** asientos incorrectos por sus consecuencias en los estados financieros.

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
| `asiento` | Registro de un hecho económico con al menos un cargo y un abono de igual monto. |
| `cargo (debe)` | Anotación a la izquierda. Aumenta activo, gasto y retiros; disminuye pasivo, patrimonio e ingreso. |
| `abono (haber)` | Anotación a la derecha. Lo inverso. |
| `cuenta` | Registro individual de una partida. El plan de cuentas las organiza. |
| `documento de respaldo` | Factura, contrato, comprobante. Todo asiento debe tenerlo. |
| `asiento de ajuste` | Registro al cierre para reflejar devengos, consumos y estimaciones. |
| `asiento de cierre` | Traspasa los saldos de resultado al patrimonio al terminar el periodo. |

## 🧠 Modelo mental

Antes de escribir cualquier asiento, responde **cuatro preguntas en orden**:

```text
1. ¿qué RECIBIÓ o consumió la entidad?
2. ¿qué ENTREGÓ o se obligó a entregar?
3. ¿qué ELEMENTOS se afectan? (activo, pasivo, patrimonio, ingreso, gasto)
4. ¿en qué DIRECCIÓN se mueve cada uno? (aumenta o disminuye)
```

Con esas cuatro respuestas, el asiento se escribe solo. Sin ellas, se memorizan casos particulares y
se falla ante el primero que no coincide.

## 📖 Desarrollo

### 1. El mecanismo, deducido

De la ecuación ampliada (clase 2):

```text
Activo + Gasto + Retiros  =  Pasivo + Patrimonio + Ingreso
    lado del CARGO                  lado del ABONO
```

| Elemento | Aumenta con | Disminuye con |
|---|---|---|
| Activo | Cargo | Abono |
| Gasto | Cargo | Abono |
| Retiros | Cargo | Abono |
| Pasivo | Abono | Cargo |
| Patrimonio | Abono | Cargo |
| Ingreso | Abono | Cargo |

**Regla única:** la suma de cargos siempre iguala la suma de abonos. Si no cuadra, hay error.

### 2. Los asientos típicos

**Aporte de capital:**

```text
CARGO   Caja                    20 000 000
  ABONO   Capital                            20 000 000
```

**Compra de mercadería a crédito:**

```text
CARGO   Existencias              5 000 000
  ABONO   Proveedores                         5 000 000
```

**Venta al contado con costo asociado:**

```text
CARGO   Caja                     3 000 000
  ABONO   Ingresos por ventas                 3 000 000

CARGO   Costo de ventas          1 800 000
  ABONO   Existencias                         1 800 000
```

Nótese que una venta genera **dos asientos**: el ingreso y el consumo del inventario. Omitir el segundo
sobrestima el activo y el resultado.

**Venta a crédito:**

```text
CARGO   Cuentas por cobrar       4 500 000
  ABONO   Ingresos por ventas                 4 500 000
```

**Cobro de una cuenta por cobrar:**

```text
CARGO   Caja                     4 500 000
  ABONO   Cuentas por cobrar                  4 500 000
```

Este asiento **no genera ingreso**: el ingreso ya se reconoció al vender. Registrarlo de nuevo duplica
las ventas, y es uno de los errores más frecuentes de quien empieza.

**Pago de sueldos:**

```text
CARGO   Gastos de personal       1 800 000
  ABONO   Caja                                1 800 000
```

**Obtención de un préstamo:**

```text
CARGO   Caja                    10 000 000
  ABONO   Préstamos bancarios                10 000 000
```

**Pago de una cuota de préstamo (capital + interés):**

```text
CARGO   Préstamos bancarios        820 000
CARGO   Gastos financieros         180 000
  ABONO   Caja                                1 000 000
```

**Compra de un activo fijo con pago parcial:**

```text
CARGO   Propiedades y equipos    6 000 000
  ABONO   Caja                                2 000 000
  ABONO   Proveedores de activo fijo          4 000 000
```

**Anticipo recibido de un cliente:**

```text
CARGO   Caja                     1 500 000
  ABONO   Anticipos de clientes (pasivo)      1 500 000
```

**Distribución de dividendos:**

```text
CARGO   Resultados acumulados      560 000
  ABONO   Dividendos por pagar                  560 000
```

### 3. Asientos de ajuste al cierre

Son los que convierten un registro de caja en uno de devengo. Los cinco tipos:

**Gasto devengado no pagado:**

```text
CARGO   Gastos de arriendo         700 000
  ABONO   Arriendo por pagar                    700 000
```

**Ingreso devengado no cobrado:**

```text
CARGO   Cuentas por cobrar         320 000
  ABONO   Ingresos por servicios                320 000
```

**Gasto pagado por anticipado que se consume:**

```text
CARGO   Gastos de seguros          150 000
  ABONO   Seguros pagados por anticipado        150 000
```

**Ingreso cobrado por anticipado que se devenga:**

```text
CARGO   Anticipos de clientes      500 000
  ABONO   Ingresos por servicios                500 000
```

**Depreciación del periodo:**

```text
CARGO   Gasto por depreciación     125 000
  ABONO   Depreciación acumulada                125 000
```

La cuenta *Depreciación acumulada* es **correctora del activo**: se presenta restando de propiedades y
equipos, no como pasivo.

### 4. Documento de respaldo

```text
todo asiento debe tener:
  · fecha del hecho económico (no de la digitación)
  · documento de respaldo identificado
  · glosa que explique el hecho
  · aprobación cuando corresponda
```

Un asiento sin respaldo es una afirmación sin evidencia. En una auditoría, los asientos manuales sin
documento son el primer foco de revisión, precisamente porque son el mecanismo típico de la
manipulación.

### 5. Detectar asientos incorrectos por sus consecuencias

| Error | Consecuencia en los estados |
|---|---|
| Se registra el cobro como venta | Ingresos y cuentas por cobrar duplicados |
| Se omite el costo de ventas | Existencias y resultado sobrestimados |
| Se carga un activo fijo a gasto | Resultado subestimado; activo subestimado |
| Se carga un gasto a activo | Resultado sobrestimado; activo sobrestimado |
| Se omite la depreciación | Activo y resultado sobrestimados |
| Se registra un anticipo como ingreso | Ingresos sobrestimados; pasivo subestimado |
| Se paga un pasivo y se carga a gasto | Gastos sobrestimados; pasivo sobrestimado |

Método de detección: **partir de la anomalía en el estado y retroceder al asiento**. Si el margen bruto
es imposiblemente alto, revisa el costo de ventas; si el activo crece sin explicación, revisa qué se
activó.

## 🧮 Ejemplo guiado

**Situación.** Registra el mes completo de una empresa de servicios y prepara los ajustes de cierre.

```text
01-03  aporte de capital en efectivo                       15 000 000
03-03  compra de equipos, 60 % al contado                   8 000 000
05-03  pago anticipado de seguro anual                       1 440 000
08-03  servicio prestado y facturado, cobro a 30 días        6 200 000
12-03  compra de insumos al contado                           850 000
15-03  anticipo recibido por un servicio de abril            2 000 000
20-03  pago de sueldos de marzo                              2 400 000
25-03  pago parcial a proveedor de equipos                   1 600 000
28-03  se recibe factura de electricidad de marzo, a pagar     185 000
```

**Paso 1 — asientos del periodo.**

```text
01-03  CARGO Caja 15 000 000 / ABONO Capital 15 000 000
03-03  CARGO Equipos 8 000 000 / ABONO Caja 4 800 000, ABONO Proveedores 3 200 000
05-03  CARGO Seguros anticipados 1 440 000 / ABONO Caja 1 440 000
08-03  CARGO Cuentas por cobrar 6 200 000 / ABONO Ingresos 6 200 000
12-03  CARGO Insumos 850 000 / ABONO Caja 850 000
15-03  CARGO Caja 2 000 000 / ABONO Anticipos de clientes 2 000 000
20-03  CARGO Gastos de personal 2 400 000 / ABONO Caja 2 400 000
25-03  CARGO Proveedores 1 600 000 / ABONO Caja 1 600 000
28-03  CARGO Gastos de servicios básicos 185 000 / ABONO Cuentas por pagar 185 000
```

**Paso 2 — ajustes de cierre a marzo.**

```text
A1  consumo del seguro (1 mes de 12): 1 440 000/12 = 120 000
    CARGO Gastos de seguros 120 000 / ABONO Seguros anticipados 120 000

A2  depreciación de equipos (vida útil 5 años, desde marzo): 8 000 000/60 = 133 333
    CARGO Gasto por depreciación 133 333 / ABONO Depreciación acumulada 133 333

A3  consumo de insumos del mes (según inventario físico): 340 000
    CARGO Gasto de insumos 340 000 / ABONO Insumos 340 000
```

El anticipo de 2 000 000 **no se ajusta**: el servicio es de abril, así que sigue siendo pasivo.

**Paso 3 — mayorización de caja.**

```text
15 000 000 − 4 800 000 − 1 440 000 − 850 000 + 2 000 000 − 2 400 000 − 1 600 000 = 5 910 000
```

**Paso 4 — estado de resultados de marzo.**

```text
Ingresos                        6 200 000
Gastos de personal             −2 400 000
Gastos de servicios básicos      −185 000
Gastos de seguros                −120 000
Gasto de insumos                 −340 000
Gasto por depreciación           −133 333
RESULTADO                       3 021 667
```

**Paso 5 — situación financiera al 31-03.**

```text
ACTIVO
  caja                          5 910 000
  cuentas por cobrar            6 200 000
  insumos (850 000 − 340 000)     510 000
  seguros anticipados           1 320 000
  equipos                       8 000 000
  depreciación acumulada         −133 333
  TOTAL                        21 806 667

PASIVO
  proveedores (3 200 000 − 1 600 000) 1 600 000
  anticipos de clientes               2 000 000
  cuentas por pagar                     185 000
  TOTAL                               3 785 000

PATRIMONIO
  capital                      15 000 000
  resultado del periodo         3 021 667
  TOTAL                        18 021 667
```

**Paso 6 — verifica.**

```text
21 806 667 = 3 785 000 + 18 021 667  ✔
```

**Interpreta:** la empresa muestra un resultado de 3 021 667 y una caja de 5 910 000, de la cual
2 000 000 corresponden a un anticipo que aún debe prestarse. Su **caja realmente disponible del giro**
es menor de lo que el saldo sugiere, y sus 6 200 000 por cobrar vencen en abril. Ese análisis —que
requiere haber registrado correctamente el anticipo como pasivo— es la razón por la que la técnica de
esta clase importa más allá de la teneduría.

## 🏦 Del cliente al banco

| Vista de la empresa | Vista del banco | Parte |
|---|---|---|
| Asientos con respaldo | Requisito de auditabilidad | 12, clase 14 |
| Asientos manuales frecuentes | Foco de revisión de auditoría | 12, clase 13 |
| Anticipos como pasivo | Obligación de servicio pendiente | 13, clase 2 |
| Depreciación registrada | Afecta covenants de resultado | 13, clase 10 |
| Ajustes de cierre | Determinan la comparabilidad entre periodos | 9, clase 9 |

## 🧪 Práctica

En `labs/lab-04.md`:

1. Aplica las cuatro preguntas a veinte hechos y escribe los asientos correspondientes.
2. Registra un mes completo de una empresa de servicios con sus ajustes de cierre.
3. Introduce deliberadamente tres errores y determina su efecto en los estados.
4. Construye los estados financieros del mes y verifica la ecuación.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Las ventas están duplicadas | Se registró el cobro como venta | El cobro solo mueve activos. |
| El margen bruto es imposible | Falta el asiento de costo de ventas | Toda venta de bienes lleva dos asientos. |
| El activo crece sin razón | Se activó un gasto | Aplica la regla costo/gasto (clase 6). |
| El resultado no cambia con el uso de activos | Falta la depreciación | Registra el ajuste de depreciación. |
| Un anticipo aparece como ingreso | Control no transferido | Es pasivo hasta prestar el servicio. |
| La depreciación acumulada figura en el pasivo | Cuenta mal clasificada | Es correctora del activo. |

## ❓ Preguntas de comprobación

1. ¿Cuáles son las cuatro preguntas del método y en qué orden se aplican?
2. Deduce de la ecuación qué elementos aumentan con cargo.
3. ¿Por qué una venta de mercadería genera dos asientos?
4. ¿Qué efecto tiene en los estados omitir el asiento de depreciación?
5. ¿Por qué los asientos manuales sin respaldo son el foco de una auditoría?

## 📥 Entregable

Guarda en `portfolio/parte-05/clase-07/`:

- veinte hechos analizados con las cuatro preguntas y sus asientos;
- el mes completo registrado con los ajustes de cierre;
- el análisis del efecto de tres errores deliberados;
- los estados financieros del mes con la ecuación verificada.

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

- Kieso, D., Weygandt, J. y Warfield, T. (2022). *Intermediate Accounting* (18.ª ed.). Wiley. Capítulo 3: el ciclo contable y los asientos de ajuste.
- Horngren, C., Sundem, G. y Elliott, J. (2013). *Introduction to Financial Accounting* (11.ª ed.). Pearson. Capítulos 2 y 3: análisis de transacciones y ajustes.
- IFRS Foundation. *NIC 1 Presentación de Estados Financieros*: base de devengo y presentación de partidas correctoras. <https://www.ifrs.org/>
- IFRS Foundation. *NIC 16 Propiedades, Planta y Equipo*: depreciación y su registro.
- IAASB (2021). *ISA 240: The Auditor's Responsibilities Relating to Fraud*. Asientos manuales como foco de riesgo de fraude. <https://www.iaasb.org/>
- Verificación local: revisa qué exige la normativa contable de tu país sobre conservación de documentos de respaldo y plazos de archivo.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 06 · Ingresos, costos y gastos](06-ingresos-costos-y-gastos.md) | [Parte 05](../README.md) · [Programa](../../../SYLLABUS.md) | [08 · Libro diario y mayor →](08-libro-diario-y-mayor.md) |
<!-- gen:footer:end -->
