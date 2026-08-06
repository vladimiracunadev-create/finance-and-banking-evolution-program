---
part: 5
class: 8
title: "Libro diario y mayor"
level: intermedio
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 08 · Libro diario y mayor

> [← 07 · Registro de transacciones](07-registro-de-transacciones.md) · [Índice de la parte](../README.md) · [09 · Balance de comprobación →](09-balance-de-comprobacion.md)

**Parte 05 — Contabilidad financiera** · **Nivel:** Intermedio — requiere las partes anteriores · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Entender la arquitectura del sistema contable: cómo los asientos se acumulan, se organizan por cuenta
y producen los saldos que alimentan los estados financieros. Esta clase muestra el recorrido completo
de un dato desde el documento hasta el balance, que es exactamente el camino que un auditor recorre
en sentido inverso.

## 📚 Objetivos

Al finalizar podrás:

1. **Explicar** el flujo completo del ciclo contable con sus siete etapas.
2. **Registrar** en libro diario y mayorizar correctamente.
3. **Diseñar** un plan de cuentas coherente con la presentación requerida.
4. **Rastrear** una cifra del balance hasta su documento de origen.
5. **Usar** los libros auxiliares y conciliarlos con el mayor.

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
| `libro diario` | Registro cronológico de todos los asientos. Es la fuente primaria. |
| `libro mayor` | Agrupación por cuenta. Muestra movimientos y saldo de cada una. |
| `mayorización` | Traspaso de los asientos del diario a las cuentas del mayor. |
| `plan de cuentas` | Estructura codificada de cuentas, ordenada por elemento y por presentación. |
| `libro auxiliar` | Detalle de una cuenta de control: clientes, proveedores, activo fijo. |
| `cuenta de control` | Cuenta del mayor cuyo saldo debe igualar la suma de su auxiliar. |
| `pista de auditoría` | Cadena que permite ir del estado financiero al documento y viceversa. |

## 🧠 Modelo mental

El sistema contable es un **embudo con pista de retorno**:

```text
documento → asiento → diario → mayor → balance de comprobación → estados financieros
                                                    ↑
                         y se puede recorrer en sentido inverso: PISTA DE AUDITORÍA
```

Cada etapa agrega agregación y quita detalle. La pista de auditoría es la garantía de que ese detalle
sigue siendo recuperable, y su ausencia es lo que hace inauditable a un sistema.

## 📖 Desarrollo

### 1. El ciclo contable completo

```text
1. identificar el hecho económico y su documento
2. analizar y registrar el asiento en el DIARIO
3. mayorizar al LIBRO MAYOR
4. elaborar el BALANCE DE COMPROBACIÓN previo a ajustes
5. registrar los AJUSTES de cierre
6. elaborar el balance de comprobación AJUSTADO
7. preparar los ESTADOS FINANCIEROS y cerrar las cuentas de resultado
```

En un sistema informático las etapas 3, 4 y 6 son automáticas, lo que no las hace innecesarias:
**siguen siendo los puntos donde se detectan los errores**.

### 2. Del diario al mayor

Libro diario:

```text
FECHA   GLOSA                                   DEBE        HABER
08-03   Cuentas por cobrar / Ingresos        6 200 000
        Factura N.º 1042, servicio marzo                 6 200 000
20-03   Gastos de personal / Caja            2 400 000
        Sueldos marzo, planilla N.º 03                   2 400 000
25-03   Proveedores / Caja                   1 600 000
        Pago parcial factura equipo N.º 88               1 600 000
```

Libro mayor, cuenta Caja:

```text
CUENTA: 1.1.01 Caja y bancos
FECHA   DETALLE                      DEBE        HABER       SALDO
01-03   Aporte de capital        15 000 000                15 000 000
03-03   Compra equipos                       4 800 000     10 200 000
05-03   Seguro anual                         1 440 000      8 760 000
12-03   Insumos                                850 000      7 910 000
15-03   Anticipo cliente          2 000 000                  9 910 000
20-03   Sueldos marzo                        2 400 000      7 510 000
25-03   Pago proveedor                       1 600 000      5 910 000
                                 17 000 000  11 090 000     5 910 000
```

El saldo final de la cuenta —5 910 000— es el que aparecerá en el balance. **Cada peso de esa cifra es
rastreable hasta un documento.**

### 3. Plan de cuentas

Estructura codificada por elemento:

```text
1  ACTIVO
   1.1  Activo corriente
        1.1.01  Caja y bancos
        1.1.02  Cuentas por cobrar comerciales
        1.1.03  Provisión de incobrables (correctora)
        1.1.04  Existencias
        1.1.05  Gastos pagados por anticipado
   1.2  Activo no corriente
        1.2.01  Propiedades, planta y equipo
        1.2.02  Depreciación acumulada (correctora)
        1.2.03  Activos intangibles
2  PASIVO
   2.1  Pasivo corriente
        2.1.01  Cuentas por pagar comerciales
        2.1.02  Remuneraciones por pagar
        2.1.03  Anticipos de clientes
        2.1.04  Porción corriente de préstamos
   2.2  Pasivo no corriente
        2.2.01  Préstamos bancarios largo plazo
        2.2.02  Provisiones
3  PATRIMONIO
   3.1.01  Capital emitido
   3.1.02  Resultados acumulados
   3.1.03  Resultado del ejercicio
4  INGRESOS
   4.1.01  Ingresos por ventas
   4.1.02  Otros ingresos
5  COSTOS Y GASTOS
   5.1.01  Costo de ventas
   5.2.01  Gastos de personal
   5.2.02  Gastos de administración
   5.2.03  Depreciación y amortización
   5.3.01  Gastos financieros
```

Dos principios de diseño:

```text
· el código refleja la PRESENTACIÓN: sumar 1.1.* da el activo corriente
· las cuentas correctoras van junto a la cuenta que corrigen, con signo contrario
```

Un plan de cuentas mal diseñado obliga a reclasificar manualmente en cada cierre, que es donde
aparecen los errores.

### 4. Libros auxiliares y conciliación

| Cuenta de control | Auxiliar | Qué contiene |
|---|---|---|
| Cuentas por cobrar | Auxiliar de clientes | Saldo y antigüedad por cliente |
| Cuentas por pagar | Auxiliar de proveedores | Saldo y vencimiento por proveedor |
| Propiedades y equipos | Auxiliar de activo fijo | Ficha por bien, con vida útil y depreciación |
| Existencias | Auxiliar de inventarios | Cantidad y costo por artículo |
| Bancos | Conciliación bancaria | Diferencias entre mayor y cartola |

Control obligatorio en cada cierre:

```text
saldo de la cuenta de control = suma del auxiliar
```

Si no coinciden, hay un asiento registrado en la cuenta de control sin detalle en el auxiliar, o
viceversa. Esta conciliación es la que detecta, por ejemplo, cobros aplicados a un cliente equivocado.

### 5. Pista de auditoría

```text
partiendo del estado financiero:
  "Cuentas por cobrar 6 200 000"
    → balance de comprobación, cuenta 1.1.02
      → libro mayor, cuenta 1.1.02, movimientos del periodo
        → libro diario, asiento del 08-03
          → factura N.º 1042
            → orden de servicio, contrato, evidencia de entrega
```

Cada eslabón debe existir y ser recuperable. Una pista rota —un asiento sin documento, un ajuste sin
glosa, una cuenta sin auxiliar— es un hallazgo de auditoría, independientemente de si el monto es
correcto.

## 🧮 Ejemplo guiado

**Situación.** El saldo de Cuentas por cobrar en el mayor es 8 940 000. El auxiliar de clientes suma
8 615 000. Hay que encontrar la diferencia de 325 000.

**Paso 1 — plantea las hipótesis posibles.**

```text
H1  asiento registrado en la cuenta de control sin detalle en el auxiliar
H2  cobro aplicado en el auxiliar y no registrado en el mayor
H3  nota de crédito registrada en el auxiliar y no en el mayor
H4  error de digitación en uno de los dos
H5  asiento de ajuste global (por ejemplo, provisión) registrado en la cuenta equivocada
```

**Paso 2 — revisa los movimientos del mayor sin contrapartida en el auxiliar.**

```text
CUENTA 1.1.02, movimientos del periodo
  08-03  factura 1042        6 200 000   → existe en auxiliar (cliente A)
  14-03  factura 1043        2 415 000   → existe en auxiliar (cliente B)
  22-03  ajuste manual         325 000   → SIN detalle de cliente  ← hallazgo
```

**Paso 3 — investiga el asiento manual.**

```text
glosa: "regularización"
documento de respaldo: ninguno
usuario: contabilidad
fecha de digitación: 31-03 (nueve días después de la fecha del asiento)
```

Tres señales de alerta simultáneas: asiento manual, sin respaldo, con fecha de digitación posterior al
cierre del mes.

**Paso 4 — determina el origen real.** Al revisar, el asiento se hizo para "cuadrar" una diferencia
en la conciliación bancaria. La diferencia real provenía de un depósito de un cliente que el banco
registró y que no se había aplicado:

```text
asiento correcto que debió hacerse:
  CARGO Caja 325 000 / ABONO Cuentas por cobrar - Cliente C 325 000

asiento que se hizo:
  CARGO Cuentas por cobrar 325 000 / ABONO Caja 325 000   ← signo invertido
```

**Paso 5 — corrección.**

```text
reverso del asiento incorrecto:
  CARGO Caja 325 000 / ABONO Cuentas por cobrar 325 000
asiento correcto, con detalle de cliente:
  CARGO Caja 325 000 / ABONO Cuentas por cobrar - Cliente C 325 000

efecto neto: caja +650 000, cuentas por cobrar −650 000
```

**Paso 6 — el efecto que se evitó.**

```text
si no se detecta:
  · cuentas por cobrar sobrestimadas en 650 000
  · caja subestimada en 650 000
  · el cliente C figura como deudor de una factura ya pagada
  · se le enviaría cobranza por una deuda inexistente
```

**Interpreta:** el error no afectaba el total del activo ni la ecuación —por eso el balance cuadraba
igual— y aun así distorsionaba dos cuentas y habría producido una cobranza indebida. **La conciliación
del auxiliar contra la cuenta de control es el único control que lo detecta**, y es exactamente por eso
que existe.

## 🏦 Del cliente al banco

| Vista de la empresa | Vista del banco / auditor | Parte |
|---|---|---|
| Plan de cuentas ordenado | Facilita el análisis y la comparabilidad | 9, clase 9 |
| Auxiliares conciliados | Evidencia de control interno efectivo | 12, clase 12 |
| Asientos manuales sin respaldo | Foco de revisión y posible hallazgo | 12, clase 13 |
| Pista de auditoría completa | Requisito para auditar y para el supervisor | 12, clase 14 |
| Auxiliar de clientes con antigüedad | Insumo del análisis de cartera | 9, clase 9 |

## 🧪 Práctica

En `labs/lab-04.md`, sección de libros:

1. Registra un mes en libro diario y mayoriza a todas las cuentas afectadas.
2. Diseña un plan de cuentas para una empresa de servicios, coherente con la presentación.
3. Concilia una cuenta de control con su auxiliar y explica la diferencia.
4. Rastrea una cifra del estado financiero hasta su documento de origen, documentando cada eslabón.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| El auxiliar no cuadra con el mayor | Asiento global sin detalle | Registra siempre con identificación del tercero. |
| El balance cuadra pero hay cuentas mal | La ecuación no detecta errores intracuenta | Concilia auxiliares en cada cierre. |
| Hay que reclasificar en cada cierre | Plan de cuentas mal diseñado | Codifica según la presentación requerida. |
| No se puede rastrear una cifra | Pista de auditoría rota | Exige documento y glosa en todo asiento. |
| Las cuentas correctoras aparecen como pasivo | Clasificación incorrecta | Van junto al activo que corrigen. |
| Ajustes de "regularización" frecuentes | Se cuadran diferencias sin investigarlas | Toda diferencia se explica antes de ajustar. |

## ❓ Preguntas de comprobación

1. Enumera las siete etapas del ciclo contable.
2. ¿Qué relación debe existir entre una cuenta de control y su auxiliar?
3. ¿Por qué un plan de cuentas debe reflejar la presentación requerida?
4. Describe la pista de auditoría desde un estado financiero hasta el documento.
5. ¿Por qué un error puede existir aunque el balance cuadre?

## 📥 Entregable

Guarda en `portfolio/parte-05/clase-08/`:

- el libro diario y el mayor de un mes completo;
- el plan de cuentas diseñado, con su lógica de codificación explicada;
- la conciliación de una cuenta de control con su auxiliar y la diferencia explicada;
- el rastreo documentado de una cifra desde el estado financiero hasta su respaldo.

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

- Kieso, D., Weygandt, J. y Warfield, T. (2022). *Intermediate Accounting* (18.ª ed.). Wiley. Capítulo 3: sistema contable, diario, mayor y balance de comprobación.
- Horngren, C., Sundem, G. y Elliott, J. (2013). *Introduction to Financial Accounting* (11.ª ed.). Pearson. Capítulo 3: el ciclo contable completo.
- COSO (2013). *Internal Control — Integrated Framework*. Committee of Sponsoring Organizations. Controles de registro y conciliación. <https://www.coso.org/>
- IAASB (2021). *ISA 330: The Auditor's Responses to Assessed Risks*. Pruebas sobre asientos y pista de auditoría. <https://www.iaasb.org/>
- Basel Committee on Banking Supervision (2013). *BCBS 239: Principles for effective risk data aggregation and risk reporting*. BIS. Trazabilidad del dato.
- Verificación local: revisa qué libros contables son obligatorios en tu país, su formato legal y los plazos de conservación exigidos.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 07 · Registro de transacciones](07-registro-de-transacciones.md) | [Parte 05](../README.md) · [Programa](../../../SYLLABUS.md) | [09 · Balance de comprobación →](09-balance-de-comprobacion.md) |
<!-- gen:footer:end -->
