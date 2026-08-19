<!-- meta
part: 5
class: 10
title: "Estado de situación financiera"
level: intermedio
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 10 · Estado de situación financiera

> [← 09 · Balance de comprobación](09-balance-de-comprobacion.md) · [Índice de la parte](../README.md) · [11 · Estado de resultados →](11-estado-de-resultados.md)

**Parte 05 — Contabilidad financiera** · **Nivel:** Intermedio — requiere las partes anteriores · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Construir e interpretar la fotografía patrimonial de una entidad a una fecha. Esta clase enseña la
presentación exigida, los criterios de clasificación, los indicadores que se leen directamente del
balance, y —lo más importante— qué preguntas hacer cuando una cifra no calza con la historia que la
empresa cuenta.

Las nueve clases anteriores construyeron el registro. Esta presenta el primero de los estados que salen de él, y añade lo que un analista hace con él: leerlo, calcular indicadores y desconfiar de la fecha, porque un balance es una foto y las fotos se pueden preparar.

## 📚 Objetivos

Al finalizar podrás:

1. **Presentar** un estado de situación financiera conforme a la estructura requerida.
2. **Clasificar** correctamente cada partida entre corriente y no corriente.
3. **Calcular** los indicadores de liquidez, endeudamiento y estructura.
4. **Interpretar** la evolución del balance entre dos periodos.
5. **Formular** las preguntas que un balance no responde por sí solo.

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

Los cinco primeros términos son la lectura del balance y los dos últimos, sus límites. El **maquillaje de cierre** es lo que hay que saber detectar: hay operaciones legítimas cuyo único efecto es mejorar los indicadores del día del corte, y se reconocen comparando la foto con la serie.

| Concepto | Comprensión verificable |
|---|---|
| `fecha de corte` | El balance describe una fecha, no un periodo. Un día antes o después puede verse distinto. |
| `capital de trabajo` | `activo corriente − pasivo corriente`. Colchón operativo de corto plazo. |
| `razón corriente` | `activo corriente / pasivo corriente`. Cobertura de las obligaciones inmediatas. |
| `prueba ácida` | `(activo corriente − existencias) / pasivo corriente`. Liquidez sin depender de vender inventario. |
| `endeudamiento` | `pasivo total / patrimonio` o `pasivo total / activo total`. |
| `maquillaje de cierre` | Operaciones realizadas cerca de la fecha de corte para mejorar la presentación. |
| `patrimonio tangible` | Patrimonio menos intangibles y plusvalía. Métrica conservadora habitual en banca. |

## 🧠 Modelo mental

El balance es una fotografía, y las fotografías se pueden posar:

```text
28-12  se cobra anticipadamente a clientes con descuento     → sube caja
29-12  se posterga el pago a proveedores hasta enero         → sube caja, sube pasivo
30-12  se vende cartera con descuento                        → sube caja, baja CxC
31-12  FECHA DE CORTE: la razón corriente se ve mejor
05-01  todo vuelve a la normalidad
```

Ninguna de esas operaciones es ilegal y todas mejoran los indicadores del día del corte. Por eso un
analista experimentado mira **la serie de balances**, no uno solo, y compara con el flujo de efectivo,
que es más difícil de posar.

## 📖 Desarrollo

### 1. Estructura de presentación

El balance se presenta en un orden que no es arbitrario: refleja liquidez y exigibilidad. La tabla lo recoge.

```text
ACTIVO
  Activo corriente
    Efectivo y equivalentes
    Cuentas por cobrar comerciales (neto de provisión)
    Existencias
    Gastos pagados por anticipado
    Otros activos corrientes
  Activo no corriente
    Propiedades, planta y equipo (neto de depreciación)
    Activos por derecho de uso
    Activos intangibles
    Plusvalía
    Inversiones en asociadas
    Activos por impuestos diferidos

PASIVO
  Pasivo corriente
    Cuentas por pagar comerciales
    Otras cuentas por pagar
    Porción corriente de préstamos y arrendamientos
    Provisiones corrientes
  Pasivo no corriente
    Préstamos y arrendamientos
    Provisiones
    Pasivos por impuestos diferidos

PATRIMONIO
    Capital emitido
    Otras reservas
    Resultados acumulados
    Participaciones no controladoras
```

Requisitos de presentación relevantes:

```text
· comparativo con el periodo anterior, obligatorio
· partidas correctoras presentadas restando de la cuenta que corrigen
· desglose adicional en notas para toda partida material
· clasificación corriente/no corriente, salvo presentación por liquidez cuando sea más relevante
```

### 2. Indicadores que se leen del balance

Cinco indicadores se calculan directamente sobre el balance y responden a preguntas distintas. La tabla los reúne con su umbral habitual.

```text
capital de trabajo    = AC − PC
razón corriente       = AC / PC
prueba ácida          = (AC − existencias) / PC
razón de efectivo     = efectivo / PC
endeudamiento         = pasivo total / patrimonio
solvencia             = patrimonio / activo total
patrimonio tangible   = patrimonio − intangibles − plusvalía
```

Rangos de referencia orientativos, que dependen fuertemente del sector:

| Indicador | Comercial | Industrial | Servicios |
|---|---|---|---|
| Razón corriente | 1,2–1,8 | 1,5–2,5 | 1,0–1,5 |
| Prueba ácida | 0,6–1,0 | 0,8–1,3 | 0,9–1,4 |
| Endeudamiento | 1,0–2,0 | 0,8–1,5 | 0,5–1,2 |

Una razón corriente de 3,5 no es "mejor": puede indicar existencias inmovilizadas o cuentas por cobrar
incobrables acumuladas. **Los indicadores tienen rango óptimo, no dirección óptima.**

### 3. Interpretar la evolución

Un balance aislado dice poco. La tabla muestra qué se lee cuando hay tres o cuatro cierres seguidos, que es donde aparece la tendencia.

| Partida | Año 1 | Año 2 | Variación | Lectura |
|---|---:|---:|---:|---|
| Efectivo | 820 000 | 1 940 000 | +136,6 % | ¿De dónde? |
| Cuentas por cobrar | 4 200 000 | 3 100 000 | −26,2 % | ¿Se cobró o se vendió cartera? |
| Existencias | 3 800 000 | 4 900 000 | +28,9 % | ¿Rota o se acumula? |
| Total activo corriente | 8 820 000 | 9 940 000 | +12,7 % | |
| Proveedores | 2 900 000 | 4 700 000 | +62,1 % | ¿Se estiró el pago? |
| Préstamos corrientes | 1 800 000 | 900 000 | −50,0 % | ¿Se pagó o se reclasificó? |
| Total pasivo corriente | 5 100 000 | 6 200 000 | +21,6 % | |
| **Razón corriente** | **1,73** | **1,60** | **−0,13** | Deterioro leve |

La lectura completa exige responder las cuatro preguntas de la columna derecha, y **ninguna se responde
con el balance**: requieren el flujo de efectivo (clase 12) y las notas.

### 4. Señales de maquillaje de cierre

Las operaciones de cierre dejan huellas concretas. La tabla las recoge con la comprobación que las confirma.

| Señal | Qué buscar |
|---|---|
| Efectivo sube fuerte y baja en enero | Comparar con balances intermedios |
| Cuentas por cobrar caen sin aumento de caja | Venta de cartera o castigo |
| Proveedores suben mucho en el último mes | Postergación de pagos |
| Préstamos corrientes bajan y no corrientes suben | Reclasificación o refinanciamiento |
| Existencias caen fuerte al cierre | Ventas con derecho de devolución |
| Operaciones significativas con relacionadas cerca del corte | Nota de partes relacionadas |

El control más simple: **comparar el balance de cierre con uno intermedio** (trimestral). Si los
indicadores del cierre son notoriamente mejores que los de los trimestres, hay una pregunta que hacer.

### 5. Lo que el balance no dice

El balance omite cosas importantes por diseño, y saber cuáles evita conclusiones falsas. La lista las recoge.

```text
· la CALIDAD de los activos (¿se cobrarán? ¿se venderán?)
· el VENCIMIENTO detallado de los pasivos (está en notas)
· las obligaciones FUERA de balance (clase 4)
· la capacidad de GENERAR CAJA (clase 12)
· el VALOR de mercado de la entidad
· los riesgos ASUMIDOS que aún no se materializan
```

Un balance sólido con flujo operativo negativo describe una empresa que se está consumiendo despacio.
La conclusión solo aparece cruzando los tres estados.

## 🧮 Ejemplo guiado

**Situación.** Un analista de crédito evalúa dos empresas del mismo sector que solicitan un crédito de
5 000 000 cada una.

| Partida | Empresa A | Empresa B |
|---|---:|---:|
| Efectivo | 900 000 | 2 800 000 |
| Cuentas por cobrar (neto) | 5 400 000 | 3 100 000 |
| Existencias | 4 800 000 | 6 900 000 |
| Total activo corriente | 11 100 000 | 12 800 000 |
| Propiedades y equipos | 8 200 000 | 5 100 000 |
| Plusvalía e intangibles | 400 000 | 4 200 000 |
| **Total activo** | **19 700 000** | **22 100 000** |
| Proveedores | 4 100 000 | 7 300 000 |
| Préstamos corrientes | 2 200 000 | 1 400 000 |
| Total pasivo corriente | 6 300 000 | 8 700 000 |
| Préstamos no corrientes | 4 400 000 | 3 200 000 |
| **Total pasivo** | **10 700 000** | **11 900 000** |
| **Patrimonio** | **9 000 000** | **10 200 000** |

Ventas: A = 24 000 000; B = 26 500 000. Costo de ventas: A = 16 800 000; B = 19 100 000.

**Paso 1 — indicadores de liquidez.**

```text
                       A         B
razón corriente      1,76      1,47
prueba ácida         1,00      0,68
razón de efectivo    0,14      0,32
capital de trabajo  4 800 000  4 100 000
```

B tiene más efectivo y peor prueba ácida: su liquidez depende de existencias.

**Paso 2 — indicadores de endeudamiento.**

```text
                          A         B
pasivo/patrimonio       1,19      1,17
patrimonio/activo      45,7 %    46,2 %
patrimonio tangible   8 600 000  6 000 000
pasivo/patrimonio tangible 1,24    1,98
```

**El indicador cambia por completo al usar patrimonio tangible**: B pasa de 1,17 a 1,98, porque
4 200 000 de su patrimonio está respaldado por plusvalía e intangibles.

**Paso 3 — rotación.**

```text
                              A          B
días de cobro     5 400 000/24 000 000×365 = 82   3 100 000/26 500 000×365 = 43
días de existencias 4 800 000/16 800 000×365 = 104  6 900 000/19 100 000×365 = 132
días de proveedores 4 100 000/16 800 000×365 = 89   7 300 000/19 100 000×365 = 139
CICLO DE CONVERSIÓN  82 + 104 − 89 = 97 días        43 + 132 − 139 = 36 días
```

**Paso 4 — la lectura contraintuitiva.** B tiene un ciclo de conversión mucho mejor (36 vs. 97 días),
pero por una razón que merece atención: **paga a sus proveedores a 139 días**. Eso puede significar
poder de negociación o tensión de pago.

**Paso 5 — la pregunta decisiva.**

```text
si B tuviera que pagar a sus proveedores a 90 días como A:
  proveedores caerían de 7 300 000 a 4 710 000
  necesitaría 2 590 000 de caja adicional
  su efectivo de 2 800 000 quedaría en 210 000
  razón corriente pasaría de 1,47 a 1,03
```

La aparente solidez de caja de B depende de mantener un plazo de pago de 139 días.

**Paso 6 — recomendación.**

| Criterio | A | B |
|---|---|---|
| Liquidez sin existencias | Mejor | Peor |
| Patrimonio tangible | Mejor | Peor |
| Ciclo de conversión | Peor | Mejor, pero por plazo de proveedores |
| Resistencia a normalizar pagos | Alta | **Baja** |
| Recomendación | Aprobar con seguimiento de cobranza | Solicitar antigüedad de proveedores y explicación del plazo |

**Interpreta:** el balance de B se ve mejor en efectivo y en total de activos. Tres ajustes —patrimonio
tangible, prueba ácida y simulación de normalización de proveedores— invierten la conclusión. **Ninguno
de los tres requiere información adicional: los tres salen del mismo balance, leído con criterio.**

## 🏦 Del cliente al banco

El cliente presenta un balance y el banco calcula sus indicadores y los compara con el sector. La tabla enfrenta las dos lecturas.

| Vista de la empresa | Vista del banco | Parte |
|---|---|---|
| "Tengo buena razón corriente" | ¿Con qué activos y a qué plazo? | 9, clase 9 |
| Plusvalía en el patrimonio | Se descuenta: patrimonio tangible | 9, clase 9 |
| Proveedores altos | ¿Poder de negociación o tensión de pago? | 13, clase 2 |
| Balance de cierre favorable | Se compara con balances intermedios | 9, clase 9 |
| Covenants sobre indicadores | Se calculan sobre definiciones contractuales | 13, clase 10 |

## 🧪 Práctica

El laboratorio pide calcular los indicadores de tres cierres consecutivos y detectar maquillaje. La comparación entre cierres es lo que revela lo que un solo balance esconde.

En `labs/lab-05.md`, sección de balance:

1. Presenta un estado de situación financiera completo con comparativo.
2. Calcula los siete indicadores y compáralos con el rango del sector.
3. Analiza la evolución entre dos periodos formulando las preguntas que el balance no responde.
4. Simula la normalización de una partida (proveedores o cobranza) y recalcula los indicadores.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen balances que mejoran sin que el negocio haya mejorado. Las causas están casi siempre en operaciones de cierre.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se interpreta razón corriente alta como buena | Dirección en vez de rango | Compara con el rango del sector. |
| Se ignora la plusvalía al evaluar solvencia | Patrimonio contable sin ajustar | Usa patrimonio tangible. |
| Se concluye desde un solo balance | Fotografía única | Analiza la serie y compara con balances intermedios. |
| Se comparan sectores distintos | Estructuras patrimoniales diferentes | Compara dentro del sector. |
| Se omite el efecto de los plazos de pago | Solo se miraron saldos | Traduce saldos a días de rotación. |
| No se leen las notas | El detalle está fuera del cuerpo | Las notas contienen vencimientos y contingencias. |

## ❓ Preguntas de comprobación

1. ¿Por qué el balance describe una fecha y qué implica para su interpretación?
2. ¿Cuándo una razón corriente alta es una señal negativa?
3. ¿Qué es el patrimonio tangible y por qué la banca lo usa?
4. Nombra cuatro señales de maquillaje de cierre y cómo se verifican.
5. ¿Qué cinco cosas no dice el balance por sí solo?

## 📥 Entregable

Guarda en `portfolio/parte-05/clase-10/`:

- el estado de situación financiera presentado con comparativo;
- los siete indicadores calculados y comparados con el rango sectorial;
- el análisis de evolución con las preguntas abiertas identificadas;
- la simulación de normalización de una partida y el efecto en los indicadores.

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

- IFRS Foundation. *NIC 1 Presentación de Estados Financieros*: estructura, clasificación corriente/no corriente e información comparativa. <https://www.ifrs.org/>
- Kieso, D., Weygandt, J. y Warfield, T. (2022). *Intermediate Accounting* (18.ª ed.). Wiley. Capítulo 5: estado de situación financiera y revelaciones.
- Wild, J., Subramanyam, K. y Halsey, R. (2019). *Financial Statement Analysis* (12.ª ed.). McGraw-Hill. Capítulos 3 y 11: análisis de liquidez y estructura.
- Penman, S. (2013). *Financial Statement Analysis and Security Valuation* (5.ª ed.). McGraw-Hill. Capítulo 9: reformulación del balance para el análisis.
- Palepu, K., Healy, P. y Peek, E. (2019). *Business Analysis and Valuation: IFRS Edition* (5.ª ed.). Cengage. Capítulo 4: análisis contable y detección de distorsiones.
- Verificación local: revisa el formato de presentación exigido por el supervisor de tu país para entidades reguladas y los requisitos de estados financieros intermedios.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 09 · Balance de comprobación](09-balance-de-comprobacion.md) | [Parte 05](../README.md) · [Programa](../../../SYLLABUS.md) | [11 · Estado de resultados →](11-estado-de-resultados.md) |
<!-- gen:footer:end -->
