---
part: 5
class: 9
title: "Balance de comprobación"
level: intermedio
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 09 · Balance de comprobación

> [← 08 · Libro diario y mayor](08-libro-diario-y-mayor.md) · [Índice de la parte](../README.md) · [10 · Estado de situación financiera →](10-estado-de-situacion-financiera.md)

**Parte 05 — Contabilidad financiera** · **Nivel:** Intermedio — requiere las partes anteriores · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Usar el instrumento de control que antecede a los estados financieros, entendiendo con precisión qué
detecta y qué no. El balance de comprobación es el punto de revisión donde un contador competente
encuentra los errores antes de que lleguen al balance, y donde un analista entrenado detecta las
partidas que exigen explicación.

## 📚 Objetivos

Al finalizar podrás:

1. **Elaborar** un balance de comprobación de sumas y saldos.
2. **Distinguir** el balance previo, el ajustado y el de cierre.
3. **Enumerar** los errores que el balance detecta y los que no.
4. **Aplicar** técnicas de localización de errores según el tipo de descuadre.
5. **Revisar** un balance identificando partidas anómalas antes del cierre.

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
| `balance de comprobación` | Listado de todas las cuentas con sus sumas y saldos, verificando la igualdad de cargos y abonos. |
| `sumas` | Total de cargos y de abonos de cada cuenta en el periodo. |
| `saldo` | Diferencia entre cargos y abonos. Deudor si predomina el cargo; acreedor si el abono. |
| `balance previo` | Antes de los ajustes de cierre. |
| `balance ajustado` | Después de los ajustes. Es el que alimenta los estados financieros. |
| `saldo anómalo` | Cuenta con saldo de signo contrario al esperado. Siempre exige explicación. |
| `error de transposición` | Dígitos intercambiados. Produce una diferencia divisible por 9. |

## 🧠 Modelo mental

El balance de comprobación es un **detector de metales, no un detector de mentiras**:

```text
detecta   asientos descuadrados, sumas mal hechas, cuentas omitidas del traspaso
NO detecta  asiento omitido por completo
            asiento duplicado íntegramente
            asiento con importe equivocado en ambos lados
            asiento imputado a la cuenta equivocada del mismo tipo
```

Un balance que cuadra es condición necesaria y muy lejos de ser suficiente. Los errores que no detecta
son precisamente los que más afectan la interpretación.

## 📖 Desarrollo

### 1. Estructura

```text
                              SUMAS                    SALDOS
CUENTA                    DEBE       HABER        DEUDOR    ACREEDOR
1.1.01 Caja y bancos   17 000 000  11 090 000    5 910 000
1.1.02 Cuentas x cobrar 6 200 000           0    6 200 000
1.1.04 Insumos            850 000     340 000      510 000
1.1.05 Seguros anticip. 1 440 000     120 000    1 320 000
1.2.01 Equipos          8 000 000           0    8 000 000
1.2.02 Depreciac. acum.         0     133 333                133 333
2.1.01 Proveedores      1 600 000   3 200 000                1 600 000
2.1.03 Anticipos clien.         0   2 000 000                2 000 000
2.1.05 Cuentas x pagar          0     185 000                  185 000
3.1.01 Capital                  0  15 000 000               15 000 000
4.1.01 Ingresos                 0   6 200 000                6 200 000
5.2.01 Gastos personal  2 400 000           0    2 400 000
5.2.02 Servicios básicos  185 000           0      185 000
5.2.03 Seguros            120 000           0      120 000
5.2.04 Insumos consumidos 340 000           0      340 000
5.2.05 Depreciación       133 333           0      133 333
TOTALES                38 268 333  38 268 333   25 118 333   25 118 333
```

Dos igualdades que deben cumplirse:

```text
suma de DEBE = suma de HABER
suma de saldos DEUDORES = suma de saldos ACREEDORES
```

### 2. Previo, ajustado y de cierre

| Momento | Contenido | Uso |
|---|---|---|
| **Previo** | Solo asientos del periodo | Verificar el registro corriente |
| **Ajustado** | Incluye ajustes de devengo, consumos y estimaciones | Base de los estados financieros |
| **De cierre** | Tras cerrar cuentas de resultado contra patrimonio | Solo quedan cuentas de balance |

Tras el cierre, las cuentas de ingreso y gasto quedan en cero y su efecto neto se traslada a
resultados acumulados:

```text
CARGO Ingresos 6 200 000
  ABONO Resultado del ejercicio 6 200 000

CARGO Resultado del ejercicio 3 178 333
  ABONO Gastos de personal 2 400 000
  ABONO Servicios básicos    185 000
  ABONO Seguros              120 000
  ABONO Insumos consumidos   340 000
  ABONO Depreciación         133 333
```

### 3. Qué detecta y qué no

| Error | ¿Descuadra? | Cómo se detecta |
|---|---|---|
| Asiento con cargo y abono distintos | **Sí** | Balance de comprobación |
| Traspaso omitido al mayor | **Sí** | Balance de comprobación |
| Suma mal calculada en una cuenta | **Sí** | Balance de comprobación |
| Asiento completo omitido | No | Conciliaciones y revisión analítica |
| Asiento duplicado completo | No | Revisión de auxiliares |
| Importe equivocado en ambos lados | No | Documento de respaldo |
| Cuenta equivocada del mismo tipo | No | Conciliación de auxiliares |
| Asiento invertido (cargo por abono) | No | Saldo anómalo o análisis |

Las cinco últimas filas son la razón por la que existen la conciliación bancaria, la conciliación de
auxiliares y la revisión analítica: **el balance de comprobación no las cubre**.

### 4. Localizar un descuadre

Método ordenado por probabilidad:

```text
1. la diferencia es divisible por 9  → error de TRANSPOSICIÓN (54 por 45)
   busca cifras con dígitos intercambiados

2. la diferencia es divisible por 2  → asiento registrado en el LADO EQUIVOCADO
   busca un monto igual a la mitad de la diferencia

3. la diferencia coincide con un monto exacto → asiento omitido o mal traspasado
   busca ese monto en el diario

4. ninguna de las anteriores → revisa sumas por cuenta, luego cuenta por cuenta
```

Ejemplo:

```text
descuadre de 1 620
1 620 / 9 = 180 exacto  → probable transposición
buscar cifras del tipo: 3 420 registrado como 2 420... 
o bien 4 590 registrado como 4 950 (diferencia 360)... 
o 5 940 registrado como 4 320 (diferencia 1 620) ✔
```

### 5. Revisar antes del cierre

Lista de verificación analítica sobre el balance ajustado:

```text
□ ninguna cuenta tiene saldo anómalo (caja acreedora, proveedores deudor)
□ las cuentas correctoras tienen el signo esperado
□ los saldos de cuentas de control coinciden con sus auxiliares
□ las cuentas transitorias están en cero
□ los saldos son razonables respecto del periodo anterior
□ los ajustes de cierre están todos registrados
□ no hay cuentas con saldo desproporcionado sin explicación
□ las cuentas de "otros" no concentran montos relevantes
```

El primer punto es el más productivo: un **saldo anómalo** siempre indica algo. Una caja con saldo
acreedor significa que se registraron pagos que la caja no podía cubrir; un proveedor con saldo deudor
significa que se le pagó de más o que falta registrar una factura.

## 🧮 Ejemplo guiado

**Situación.** El balance de comprobación de una empresa no cuadra: los cargos suman 42 856 000 y los
abonos 42 838 000.

**Paso 1 — calcula la diferencia y aplica el método.**

```text
diferencia = 42 856 000 − 42 838 000 = 18 000
18 000 / 9 = 2 000 exacto  → probable transposición
18 000 / 2 = 9 000         → también posible lado equivocado
```

Se prueban ambas hipótesis, empezando por la de transposición.

**Paso 2 — busca transposiciones.** Se revisan los montos del diario buscando pares de dígitos
intercambiados cuya diferencia sea 18 000:

```text
candidatos:  x − y = 18 000 con dígitos transpuestos
  2 000 000 y 200 000... no
    36 000 y  18 000... no cumple transposición
   198 000 y 180 000  → 18 000 ✔ dígitos: 1-9-8 y 1-8-0... no es transposición pura
   
buscando de otra forma: si un monto de la forma "ab" se registró como "ba",
la diferencia es 9 × (a − b) × 10^k
  18 000 = 9 × 2 × 1000  → a − b = 2, en la posición de los miles
  candidatos: 5 300 000 registrado como 3 500 000 (diferencia 1 800 000, no)
              742 000 registrado como 724 000 (diferencia 18 000) ✔
```

**Paso 3 — verifica en el diario.**

```text
15-04  CARGO Existencias 742 000 / ABONO Proveedores 742 000
mayor de Existencias: 742 000  ✔
mayor de Proveedores: 724 000  ✗  ← error de traspaso
```

Encontrado: el traspaso al mayor de Proveedores se digitó con los dígitos de las centenas y decenas
intercambiados.

**Paso 4 — corrige y verifica.**

```text
Proveedores: 724 000 → 742 000
nuevos totales: cargos 42 856 000, abonos 42 856 000  ✔
```

**Paso 5 — revisión analítica del balance corregido.**

| Cuenta | Saldo | Observación |
|---|---:|---|
| Caja y bancos | 1 240 000 deudor | Normal |
| Cuentas por cobrar | 8 940 000 deudor | Normal |
| **Anticipos a proveedores** | **−85 000 acreedor** | **Anómalo** |
| Existencias | 4 320 000 deudor | Normal |
| Cuentas por pagar | 3 610 000 acreedor | Normal |
| **Cuenta "Otros activos"** | **2 800 000 deudor** | **Desproporcionado** |
| Ingresos | 28 400 000 acreedor | Normal |

**Paso 6 — investiga las dos anomalías.**

```text
anticipos a proveedores con saldo acreedor −85 000
  → se registró la recepción de la mercadería sin descontar el anticipo,
    o se registró un anticipo mayor al pagado
  → revisar el auxiliar de proveedores

"otros activos" 2 800 000, el 6,5 % del activo total
  → una cuenta "otros" con esa magnitud oculta partidas que deberían tener
    cuenta propia; exige desagregación antes del cierre
```

**Interpreta:** el descuadre de 18 000 se localizó en minutos aplicando la regla del 9. Pero **los dos
hallazgos importantes aparecieron después de cuadrar**, en la revisión analítica: un saldo anómalo y
una cuenta "otros" desproporcionada. El balance cuadrado era la condición para empezar a revisar, no
el resultado de la revisión.

## 🏦 Del cliente al banco

| Vista de la empresa | Vista del analista o auditor | Parte |
|---|---|---|
| Balance cuadrado | Condición mínima; no acredita nada | 9, clase 9 |
| Saldos anómalos | Hallazgo que exige explicación | 12, clase 13 |
| Cuentas "otros" abultadas | Señal de agregación indebida | 9, clase 9 |
| Ajustes de cierre numerosos | Posible debilidad del registro corriente | 12, clase 12 |
| Revisión analítica documentada | Evidencia de control interno | 12, clase 12 |

## 🧪 Práctica

En `labs/lab-05.md`:

1. Elabora el balance de comprobación previo y ajustado de un caso completo.
2. Introduce cuatro errores distintos y determina cuáles descuadran y cuáles no.
3. Aplica el método de localización a tres descuadres con diferencias distintas.
4. Realiza la revisión analítica con la lista de verificación y documenta los hallazgos.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se asume que cuadrar equivale a estar correcto | Confusión sobre el alcance del control | Cuadrar es necesario, no suficiente. |
| Se busca el descuadre al azar | No se aplicó el método | Usa las reglas del 9 y del 2 primero. |
| Se ajusta la diferencia con un asiento | Se cuadra sin investigar | Toda diferencia se explica antes de ajustar. |
| Se ignoran los saldos anómalos | No se revisó analíticamente | Todo saldo anómalo exige explicación. |
| Cuentas "otros" con montos grandes | Falta de desagregación | Abre cuentas específicas. |
| No se distingue previo de ajustado | Ajustes omitidos | Elabora ambos y compara. |

## ❓ Preguntas de comprobación

1. ¿Qué dos igualdades verifica un balance de comprobación?
2. Enumera cuatro errores que el balance **no** detecta y cómo se detectan.
3. Un descuadre de 4 500. ¿Qué hipótesis pruebas primero y por qué?
4. ¿Qué significa un saldo acreedor en una cuenta de caja?
5. ¿Por qué una cuenta "otros activos" con el 7 % del total es un hallazgo?

## 📥 Entregable

Guarda en `portfolio/parte-05/clase-09/`:

- el balance de comprobación previo y ajustado de un caso completo;
- el análisis de cuatro errores con su efecto en la cuadratura;
- la localización documentada de tres descuadres con el método aplicado;
- la revisión analítica con la lista de verificación y los hallazgos explicados.

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

- Kieso, D., Weygandt, J. y Warfield, T. (2022). *Intermediate Accounting* (18.ª ed.). Wiley. Capítulo 3: balance de comprobación previo y ajustado.
- Horngren, C., Sundem, G. y Elliott, J. (2013). *Introduction to Financial Accounting* (11.ª ed.). Pearson. Capítulo 3: cierre del ciclo contable.
- IAASB (2021). *ISA 520: Analytical Procedures*. Revisión analítica como procedimiento de auditoría. <https://www.iaasb.org/>
- COSO (2013). *Internal Control — Integrated Framework*. Actividades de control y conciliaciones.
- Wild, J., Subramanyam, K. y Halsey, R. (2019). *Financial Statement Analysis* (12.ª ed.). McGraw-Hill. Capítulo 2: revisión de razonabilidad de saldos.
- Verificación local: revisa si el supervisor de tu país exige la presentación del balance de comprobación como anexo de los estados financieros de entidades reguladas.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 08 · Libro diario y mayor](08-libro-diario-y-mayor.md) | [Parte 05](../README.md) · [Programa](../../../SYLLABUS.md) | [10 · Estado de situación financiera →](10-estado-de-situacion-financiera.md) |
<!-- gen:footer:end -->
