<!-- meta
part: 5
class: 2
title: "Ecuación contable"
level: intermedio
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 02 · Ecuación contable

> [← 01 · Lenguaje contable](01-lenguaje-contable.md) · [Índice de la parte](../README.md) · [03 · Activos →](03-activos.md)

**Parte 05 — Contabilidad financiera** · **Nivel:** Intermedio — requiere las partes anteriores · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Dominar la identidad que sostiene todo el sistema contable y que permite verificar cualquier registro
sin conocer el detalle: **activo = pasivo + patrimonio**. Esta clase demuestra por qué la igualdad se
mantiene siempre, cómo se extiende para incorporar el resultado, y cómo se usa para detectar errores
en segundos.

La clase anterior estableció qué registra la contabilidad y bajo qué criterio. Esta introduce la restricción que hace que ese registro sea verificable: toda operación afecta al menos a dos cuentas y la ecuación sigue cuadrando. No es una convención de escritura, es un control de integridad.

## 📚 Objetivos

Al finalizar podrás:

1. **Demostrar** por qué la ecuación se mantiene ante cualquier transacción.
2. **Extender** la ecuación para incorporar ingresos, gastos, aportes y retiros.
3. **Aplicar** la partida doble como consecuencia de la ecuación, no como regla memorizada.
4. **Detectar** errores de registro usando la ecuación como control.
5. **Interpretar** qué dice la estructura de la ecuación sobre el financiamiento de una entidad.

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

Los tres primeros términos son la ecuación y su mecánica; los tres últimos, lo que se lee en ella. El **origen y aplicación** es la lectura que más aclara: el lado derecho dice de dónde salió el dinero y el izquierdo en qué se puso, y esa lectura convierte el balance en una historia.

| Concepto | Comprensión verificable |
|---|---|
| `ecuación contable` | `Activo = Pasivo + Patrimonio`. No es una convención: expresa que todo recurso tiene un origen. |
| `partida doble` | Todo hecho afecta al menos dos partidas de modo que la igualdad se conserve. |
| `ecuación ampliada` | `A = P + (Capital + Ingresos − Gastos − Retiros)`. Incorpora el resultado del periodo. |
| `origen y aplicación` | El pasivo y el patrimonio dicen **de dónde salió**; el activo dice **en qué está**. |
| `estructura de financiamiento` | Proporción entre pasivo y patrimonio. Define el apalancamiento (Parte 13, clase 5). |
| `control de cuadratura` | Verificación de que la igualdad se mantiene. Detecta errores, no todos. |

## 🧠 Modelo mental

La ecuación dice algo simple y profundo:

```text
todo lo que la entidad TIENE      =    todo lo que la entidad DEBE
                                        + lo que corresponde a los dueños

ACTIVO                            =    PASIVO + PATRIMONIO
 en qué está el dinero                  de dónde vino el dinero
```

No puede haber un recurso sin origen. Por eso la igualdad no se "mantiene": es imposible que se rompa
si el registro es correcto, y cuando se rompe, hay un error.

## 📖 Desarrollo

### 1. La ecuación básica y su lógica

La ecuación no es una fórmula que haya que memorizar: es una identidad que se cumple por construcción. El esquema siguiente muestra por qué.

```text
Activo = Pasivo + Patrimonio
```

Reordenada, se lee de otra forma igualmente útil:

```text
Patrimonio = Activo − Pasivo
```

Esta segunda forma es la definición operativa del patrimonio: **lo que quedaría para los dueños si se
liquidaran todos los activos y se pagaran todas las deudas**. Es exactamente el patrimonio neto
personal de la Parte 2, clase 9, aplicado a una entidad.

### 2. Por qué se mantiene siempre

Cualquier transacción produce uno de estos cuatro efectos:

| Tipo | Efecto | Ejemplo |
|---|---|---|
| A | Activo + / Activo − | Se cobra una cuenta por cobrar: caja sube, cuentas por cobrar baja |
| B | Activo + / Pasivo + | Se compra a crédito: existencias sube, proveedores sube |
| C | Activo + / Patrimonio + | Aporte de capital: caja sube, capital sube |
| D | Pasivo − / Activo − | Se paga a un proveedor: proveedores baja, caja baja |

En los cuatro casos la igualdad se conserva por construcción:

```text
tipo A  ambos cambios en el mismo lado, se compensan
tipo B  ambos lados suben lo mismo
tipo C  ambos lados suben lo mismo
tipo D  ambos lados bajan lo mismo
```

No existe una transacción que rompa la igualdad. **Si se rompe, no es un hecho económico raro: es un
error de registro.**

### 3. La ecuación ampliada

El resultado del periodo es un movimiento del patrimonio. Desagregándolo:

```text
Activo = Pasivo + Capital + Ingresos − Gastos − Retiros

o bien, reagrupando:

Activo + Gastos + Retiros = Pasivo + Capital + Ingresos
```

La segunda forma es útil porque **todos los términos son positivos**, y explica la lógica del cargo y
el abono:

| Aumenta con cargo (debe) | Aumenta con abono (haber) |
|---|---|
| Activo | Pasivo |
| Gasto | Patrimonio |
| Retiros | Ingreso |

Esta tabla no hay que memorizarla: se **deduce** de la ecuación ampliada. Lo que está a la izquierda
aumenta con cargo; lo que está a la derecha, con abono.

### 4. La ecuación como control

Cuatro comprobaciones que se hacen en segundos:

```text
1. ¿A = P + PN al cierre?                     → si no, hay error
2. ¿ΔA = ΔP + ΔPN entre dos fechas?           → si no, falta una transacción
3. ¿PN final = PN inicial + resultado + aportes − retiros?  → conecta los estados
4. ¿la suma de cargos = suma de abonos?       → clase 9, balance de comprobación
```

Lo que la ecuación **no** detecta: una transacción omitida por completo, una registrada dos veces
íntegramente, o una imputada a la cuenta equivocada dentro del mismo elemento. Por eso el control de
cuadratura es necesario y no suficiente.

### 5. Qué dice la estructura

La proporción entre pasivo y patrimonio dice cómo se financia la empresa y cuánto margen tiene ante una pérdida. La tabla recoge las lecturas habituales.

```text
Empresa A   activo 100  pasivo 20   patrimonio 80    → apalancamiento 0,25
Empresa B   activo 100  pasivo 75   patrimonio 25    → apalancamiento 3,00
```

Ambas controlan los mismos 100 de recursos. La diferencia es **quién los financió** y, por lo tanto,
quién asume el riesgo:

| | Empresa A | Empresa B |
|---|---|---|
| Si los activos caen 20 % | Patrimonio 60, sigue solvente | Patrimonio 5, casi insolvente |
| Si los activos caen 30 % | Patrimonio 50 | **Patrimonio −5: insolvente** |
| Rentabilidad sobre patrimonio si el activo rinde 10 % | 12,5 %* | 40,0 %* |

*Antes de considerar el costo de la deuda.

El apalancamiento amplifica en ambas direcciones. En un banco, esta estructura es el corazón del
negocio y de su regulación: la Parte 12, clase 1, muestra por qué existe un requerimiento mínimo de
capital.

## 🧮 Ejemplo guiado

**Situación.** Sigue la misma pyme de la clase 1 durante febrero:

```text
1. se cobran 2 000 000 de la cuenta por cobrar de enero
2. se paga el arriendo de enero (700 000) y se devenga el de febrero (700 000)
3. se compran insumos por 900 000 a crédito
4. se presta un servicio por 3 200 000, cobrado 1 200 000 al contado
5. se pagan sueldos de febrero por 1 800 000
6. se paga la mitad de la deuda por el equipo: 2 000 000
```

Saldos al inicio de febrero (de la clase 1):

```text
ACTIVO      caja 15 700 000 · cuentas por cobrar 4 500 000 · equipo 6 000 000  = 26 200 000
PASIVO      proveedores equipo 4 000 000 · arriendo por pagar 700 000          =  4 700 000
PATRIMONIO  capital 20 000 000 − retiros 500 000 + resultados 2 000 000        = 21 500 000
```

**Paso 1 — registra cada hecho como efecto sobre la ecuación.**

| # | Activo | Pasivo | Patrimonio |
|---:|---|---|---|
| 1 | +2 000 000 caja, −2 000 000 CxC | — | — |
| 2 | −700 000 caja | −700 000 arriendo por pagar, +700 000 nuevo | −700 000 (gasto feb) |
| 3 | +900 000 insumos | +900 000 proveedores | — |
| 4 | +1 200 000 caja, +2 000 000 CxC | — | +3 200 000 (ingreso) |
| 5 | −1 800 000 caja | — | −1 800 000 (gasto) |
| 6 | −2 000 000 caja | −2 000 000 proveedores equipo | — |

**Paso 2 — saldos al cierre de febrero.**

```text
CAJA          15 700 000 + 2 000 000 − 700 000 + 1 200 000 − 1 800 000 − 2 000 000 = 14 400 000
CxC            4 500 000 − 2 000 000 + 2 000 000                                   =  4 500 000
INSUMOS                                                                             =    900 000
EQUIPO                                                                              =  6 000 000
ACTIVO TOTAL                                                                        = 25 800 000

PROVEEDORES EQUIPO   4 000 000 − 2 000 000 = 2 000 000
ARRIENDO POR PAGAR   700 000 − 700 000 + 700 000 =   700 000
PROVEEDORES INSUMOS                              =   900 000
PASIVO TOTAL                                     = 3 600 000

PATRIMONIO   21 500 000 + 3 200 000 − 700 000 − 1 800 000 = 22 200 000
```

**Paso 3 — verifica la ecuación.**

```text
25 800 000 = 3 600 000 + 22 200 000   ✔
```

**Paso 4 — verifica la variación (control 2).**

```text
ΔA = 25 800 000 − 26 200 000 = −400 000
ΔP = 3 600 000 − 4 700 000   = −1 100 000
ΔPN = 22 200 000 − 21 500 000 = +700 000

−400 000 = −1 100 000 + 700 000   ✔
```

**Paso 5 — verifica la conexión con el resultado (control 3).**

```text
resultado de febrero = 3 200 000 − 700 000 − 1 800 000 = +700 000
PN final = PN inicial + resultado = 21 500 000 + 700 000 = 22 200 000  ✔
```

**Paso 6 — interpreta la estructura.**

```text
apalancamiento = 3 600 000 / 22 200 000 = 0,16
caja / pasivo total = 14 400 000 / 3 600 000 = 4,0 veces
```

La empresa está poco endeudada y con amplia liquidez. Pero hay una señal que la ecuación por sí sola
no muestra y que exige atención: **las cuentas por cobrar se mantienen en 4 500 000 pese a haber
cobrado 2 000 000**, porque se generaron otros 2 000 000. Si esa tendencia continúa, el crecimiento de
las ventas consumirá caja de forma sostenida. Ese fenómeno es el capital de trabajo de la Parte 13,
clase 2.

## 🏦 Del cliente al banco

El cliente ve un balance y el banco ve estructura de financiamiento y capacidad de absorber pérdidas. La tabla enfrenta las dos lecturas.

| Vista de la empresa | Vista del banco | Parte |
|---|---|---|
| Ecuación cuadrada | Requisito mínimo; no acredita calidad | 9, clase 9 |
| Alto patrimonio relativo | Mayor colchón ante pérdidas | 9, clase 9 |
| Alto apalancamiento | Mayor rentabilidad y mayor riesgo | 13, clase 5 |
| Patrimonio negativo | Insolvencia contable; causal de alerta | 9, clase 14 |
| Estructura del propio banco | Capital regulatorio mínimo exigido | 12, clase 1 |

## 🧪 Práctica

El laboratorio pide registrar operaciones y comprobar que la ecuación cuadra en cada paso. El ejercicio incluye operaciones que parecen afectar a un solo lado: descubrir la segunda cuenta es el objetivo.

En `labs/lab-01.md`, sección de ecuación:

1. Registra quince transacciones como efectos sobre la ecuación y verifica la igualdad en cada paso.
2. Aplica los cuatro controles de cuadratura a un caso completo.
3. Construye dos empresas con el mismo activo y distinto apalancamiento, y compara su resistencia a una caída del activo.
4. Deduce la tabla de cargo y abono desde la ecuación ampliada, sin memorizarla.

## ⚠️ Errores frecuentes

Los síntomas de la tabla se refieren a ecuaciones que no cuadran o que cuadran ocultando un error. La causa de las segundas es siempre la misma: dos errores compensados.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| La ecuación no cuadra | Falta un lado del registro | Toda transacción afecta al menos dos partidas. |
| Se memoriza la tabla de cargo y abono | No se dedujo de la ecuación | Deriva la tabla desde la ecuación ampliada. |
| Cuadra pero el resultado es incorrecto | Error dentro del mismo elemento | El control de cuadratura es necesario, no suficiente. |
| Se registra un aporte como ingreso | Elemento equivocado | Aportes afectan patrimonio directamente. |
| El patrimonio final no coincide con el resultado | Se omitieron aportes o retiros | Aplica el control 3 de conexión. |
| Se concluye solvencia por cuadrar | Confusión entre control y análisis | Cuadrar no dice nada sobre la salud financiera. |

## ❓ Preguntas de comprobación

1. ¿Por qué la ecuación contable no puede romperse si el registro es correcto?
2. Escribe la ecuación ampliada y deduce de ella qué aumenta con cargo.
3. ¿Qué tipos de error **no** detecta el control de cuadratura?
4. Dos empresas tienen el mismo activo y distinto apalancamiento. ¿Cuál resiste mejor una caída del 25 % en sus activos?
5. ¿Cómo se conecta el patrimonio final con el resultado del periodo?

## 📥 Entregable

Guarda en `portfolio/parte-05/clase-02/`:

- el registro de quince transacciones con verificación de la ecuación en cada paso;
- los cuatro controles de cuadratura aplicados a un caso completo;
- la comparación de resistencia entre dos estructuras de financiamiento;
- la deducción escrita de la tabla de cargo y abono desde la ecuación ampliada.

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

- IFRS Foundation (2018). *Marco Conceptual para la Información Financiera*, capítulo 4: definiciones de activo, pasivo y patrimonio. <https://www.ifrs.org/>
- Kieso, D., Weygandt, J. y Warfield, T. (2022). *Intermediate Accounting* (18.ª ed.). Wiley. Capítulo 3: el sistema contable y la partida doble.
- Horngren, C., Sundem, G. y Elliott, J. (2013). *Introduction to Financial Accounting* (11.ª ed.). Pearson. Capítulo 2: ecuación contable y análisis de transacciones.
- Penman, S. (2013). *Financial Statement Analysis and Security Valuation* (5.ª ed.). McGraw-Hill. Capítulo 2: relaciones entre los estados financieros.
- Modigliani, F. y Miller, M. (1958). "The Cost of Capital, Corporation Finance and the Theory of Investment". *American Economic Review*. Efecto de la estructura de financiamiento.
- Verificación local: revisa el formato de presentación del estado de situación financiera exigido por el supervisor de tu país para entidades reguladas.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 01 · Lenguaje contable](01-lenguaje-contable.md) | [Parte 05](../README.md) · [Programa](../../../SYLLABUS.md) | [03 · Activos →](03-activos.md) |
<!-- gen:footer:end -->
