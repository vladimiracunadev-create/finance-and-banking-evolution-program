<!-- meta
part: 16
class: 10
title: "Contabilidad y estados financieros"
level: profesional
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 10 · Contabilidad y estados financieros

> [← 09 · Operaciones y pagos](09-operaciones-y-pagos.md) · [Índice de la parte](../README.md) · [11 · Tesorería y balance →](11-tesoreria-y-balance.md)

**Parte 16 — Proyecto Banco Virtual** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Construir los estados financieros del Banco Austral y el sistema contable que los produce. Es la clase
donde todas las decisiones anteriores se traducen a cifras auditables, y donde **cualquier incoherencia
del proyecto se hace visible**, porque un balance que no cuadra no admite interpretación.

Todo lo anterior produce hechos económicos que hay que registrar. Esta clase construye la contabilidad del banco aplicando la Parte 5 y el modelo de tres etapas de la Parte 9, y produce el primer juego de estados financieros proyectados del proyecto.

## 📚 Objetivos

Al finalizar podrás:

1. **Construir** el plan de cuentas de un banco y su estructura.
2. **Aplicar** el modelo de pérdidas crediticias esperadas de NIIF 9.
3. **Elaborar** balance, resultado y flujo de efectivo proyectados.
4. **Conciliar** las cifras contables con las de gestión.
5. **Preparar** la información para el supervisor y para el mercado.

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

Los cinco primeros términos son la provisión y su modelo de etapas; los tres siguientes, la conciliación y la información periódica. El **aumento significativo del riesgo** es el criterio que decide el salto de etapa uno a dos, y con él un salto de provisión que no requiere ningún impago.

| Concepto | Comprensión verificable |
|---|---|
| `plan de cuentas` | Estructura de cuentas contables del banco. |
| `pérdida crediticia esperada` | Provisión según NIIF 9, en tres etapas. |
| `etapa 1` | Sin aumento significativo del riesgo; pérdida a 12 meses. |
| `etapa 2` | Con aumento significativo; pérdida de toda la vida. |
| `etapa 3` | Deteriorado; pérdida de toda la vida, con interés sobre el neto. |
| `aumento significativo del riesgo` | Criterio de traspaso entre etapas. |
| `conciliación contable-gestión` | Puente entre las cifras de ambos sistemas. |
| `información financiera intermedia` | Estados de períodos menores al año. |

## 🧠 Modelo mental

El modelo mental es una doble contabilidad que tiene que conciliar: la de gestión, que se usa para decidir, y la contable, que se publica. Cuando difieren, la diferencia tiene que poder explicarse partida a partida, y esa conciliación es el control que detecta errores en ambas.

```text
LA CONTABILIDAD ES DONDE EL PROYECTO
SE VERIFICA A SÍ MISMO

  el balance debe cuadrar
  el resultado debe explicar la variación del patrimonio
  el flujo debe explicar la variación de la caja
  las provisiones deben corresponder al modelo de riesgo
  el capital regulatorio debe partir del patrimonio contable

  SI ALGUNA DE ESAS CINCO NO SE SOSTIENE,
  HAY UNA DECISIÓN INCOHERENTE EN ALGUNA CLASE ANTERIOR
```

## 📖 Desarrollo

### 1. Plan de cuentas

El plan de cuentas del banco se estructura por naturaleza y por producto. La tabla lo recoge.

```text
ESTRUCTURA
  1 ACTIVO
    11 disponible y equivalentes
    12 inversiones
    13 cartera de créditos
      131 colocaciones vigentes
      132 colocaciones vencidas
      139 provisiones por pérdidas esperadas  (negativa)
    14 activo fijo e intangibles
    15 otros activos
  2 PASIVO
    21 depósitos y captaciones
    22 obligaciones con bancos y emisiones
    23 provisiones y contingencias
    24 otros pasivos
  3 PATRIMONIO
    31 capital pagado
    32 reservas
    33 resultados acumulados
    34 otro resultado integral
  4 RESULTADO
    41 ingresos por intereses
    42 gastos por intereses
    43 comisiones
    44 provisiones por deterioro
    45 gastos operativos
    46 impuestos
  5 CUENTAS DE ORDEN
    51 líneas no utilizadas
    52 garantías recibidas
```

Dentro de ese plan hay una cuenta que concentra la atención de la auditoría, porque es donde el modelo de riesgo se convierte en pérdida contable.

```text
LA CUENTA 139 ES LA MÁS IMPORTANTE DEL BANCO
  es donde el modelo de riesgo se convierte
  en una cifra que reduce el patrimonio

  y es la que el auditor examinará primero
  (Parte 12, clase 15)
```

### 2. Pérdidas crediticias esperadas

La provisión se calcula por etapas con horizontes distintos. La tabla lo recoge.

```text
TRES ETAPAS DE NIIF 9

  ETAPA 1 — riesgo no aumentado significativamente
    provisión: pérdida esperada de los próximos 12 meses
    interés: sobre el saldo bruto

  ETAPA 2 — aumento significativo del riesgo
    provisión: pérdida esperada de TODA LA VIDA
    interés: sobre el saldo bruto

  ETAPA 3 — deteriorado
    provisión: pérdida esperada de toda la vida
    interés: sobre el saldo NETO de provisión
```

```text
CRITERIOS DE TRASPASO DEL BANCO AUSTRAL

  DE ETAPA 1 A ETAPA 2
    · atraso > 30 días  (presunción refutable)
    · aumento de la PD estimada > 100 % desde el origen
      Y PD absoluta > 8 %
    · reprogramación por dificultad del deudor
    · deterioro del ingreso verificado > 30 %
    · para E2: caída de ventas por medios de pago > 40 %

  DE ETAPA 2 A ETAPA 3
    · atraso > 90 días
    · reestructuración con quita
    · indicios objetivos de deterioro

  RETORNO A ETAPA 1
    · 6 meses de cumplimiento continuo
    · Y desaparición del criterio que causó el traspaso
```

**El criterio de caída de ventas para E2 es el más específico del modelo.** Un banco que evalúa sobre el
flujo de ventas debe usar ese mismo flujo como señal de deterioro, y hacerlo le da 4 a 6 meses de
anticipación sobre el atraso.

### 3. Cálculo de la provisión

El cálculo aplica los tres parámetros de la clase 8. El procedimiento lo recorre.

```text
PROVISIÓN = EAD × PD (del horizonte) × LGD × factor de descuento

  ETAPA 1: PD a 12 meses
  ETAPA 2 y 3: PD de toda la vida restante
```

| Producto | Etapa | % de la cartera | PD | LGD | Provisión |
|---|---|---:|---:|---:|---:|
| P2 | 1 | 84 % | 6,84 % | 69,2 % | 4 693 |
| P2 | 2 | 11 % | 28,4 % | 69,2 % | 2 553 |
| P2 | 3 | 5 % | 100 % | 69,2 % | 4 084 |
| E2 | 1 | 88 % | 4,20 % | 46,3 % | 4 202 |
| E2 | 2 | 9 % | 19,6 % | 46,3 % | 2 006 |
| E2 | 3 | 3 % | 100 % | 46,3 % | 3 411 |
| E3 | 1 | 100 % | 0,40 % | 35,0 % | 5 |

```text
PROVISIÓN TOTAL: 20 954
sobre cartera bruta de 335 971: 6,24 %

  Y AQUÍ APARECE LA DISTINCIÓN CRÍTICA
    la PROVISIÓN es el saldo del balance: 20 954
    el COSTO DE RIESGO es la DOTACIÓN del período
    → en régimen, la dotación cubre el flujo de deterioro
      y la provisión es el acumulado
```

### 4. Estados financieros proyectados

Los estados se proyectan desde el plan de negocio. El procedimiento los construye.

```text
BALANCE AL AÑO 3 (miles)

  ACTIVO
    disponible y equivalentes            48 200
    inversiones (activos líquidos)       90 000
    cartera bruta                       335 971
    provisiones                         −20 954
    cartera neta                        315 017
    activo fijo e intangibles             8 400
    otros activos                        12 600
    TOTAL ACTIVO                        474 217

  PASIVO
    depósitos y captaciones              81 920
    obligaciones y emisiones            329 851
    provisiones y contingencias           1 240
    otros pasivos                         9 306
    TOTAL PASIVO                        422 317

  PATRIMONIO
    capital pagado                       46 000
    resultados acumulados                 5 900
    TOTAL PATRIMONIO                     51 900

  TOTAL PASIVO Y PATRIMONIO             474 217  ✓
```

```text
ESTADO DE RESULTADOS DEL AÑO 3

  ingresos por intereses                 68 274
  gastos por intereses                  −24 775
  MARGEN FINANCIERO                      43 499
  comisiones netas                       12 443
  MARGEN BRUTO                           55 942
  gastos operativos                     −21 047
  RESULTADO ANTES DE PROVISIONES         34 895
  provisiones por deterioro             −10 368
  factor de conservadurismo              −2 592
  RESULTADO ANTES DE IMPUESTOS           21 935
  impuestos (27 %)                       −5 922
  RESULTADO NETO                         16 013
```

### 5. Conciliación contable-gestión

Las dos visiones difieren y la diferencia se explica. La tabla recoge las partidas.

```text
POR QUÉ DIFIEREN
  · la gestión usa pérdida ESPERADA;
    la contabilidad, la provisión de NIIF 9
  · la gestión usa precio de transferencia;
    la contabilidad, tasas reales
  · la gestión asigna costos por actividad;
    la contabilidad, por naturaleza
  · la gestión mide por cliente;
    la contabilidad, por cuenta

LA CONCILIACIÓN ES OBLIGATORIA
  y su ausencia produce dos verdades
  que se contradicen en el comité
```

## 🧮 Ejemplo guiado

El ejemplo calcula la provisión de una cartera por etapas. Conviene mirar el efecto del salto de etapa: multiplica la provisión sin que haya habido impago.

**Situación.** Verificar la coherencia contable de todo el proyecto.

**Paso 1 — verifica que el balance cuadre.**

```text
ACTIVO: 474 217
PASIVO + PATRIMONIO: 422 317 + 51 900 = 474 217  ✓
```

**Paso 2 — verifica el patrimonio contra el resultado.**

```text
capital pagado:                46 000
resultado acumulado año 1:     −2 400
resultado acumulado año 2:      +2 800
resultado del año 3:           +16 013
PATRIMONIO ESPERADO:            62 413

PATRIMONIO EN EL BALANCE:       51 900
DIFERENCIA:                     10 513
```

**Paso 3 — investiga la diferencia.**

```text
POSIBLES CAUSAS
  · el resultado del año 3 proyectado en la clase 8
    era 13 667 antes del conservadurismo
    y 11 775 después
  · el estado de resultados de esta clase da 16 013

  ¿POR QUÉ DIFIEREN?

  CLASE 8: resultado antes de impuestos 18 722
    menos conservadurismo 2 592 = 16 130
    resultado neto: 11 775

  ESTA CLASE: resultado antes de impuestos 21 935
    ¿de dónde sale la diferencia de 3 213?

  margen bruto: 55 942 en ambas  ✓
  gastos: 26 852 en la clase 8, 21 047 en esta
  DIFERENCIA: 5 805

  la clase 8 usó el 48 % de eficiencia (compromiso)
  esta clase usa los gastos DIMENSIONADOS (clase 9)
```

**Paso 4 — resuelve la incoherencia.**

```text
LA CIFRA CORRECTA ES LA DIMENSIONADA

  la clase 8 aplicó un porcentaje de eficiencia
  la clase 9 calculó los gastos partida por partida

  → el estado de resultados usa los gastos de la clase 9
    más la reserva del compromiso revisado

  GASTOS FINALES
    dimensionados: 21 047
    reserva del compromiso (42 % − 37,6 %): 2 462
    TOTAL: 23 509

  RESULTADO ANTES DE IMPUESTOS: 34 895 − 2 462 − 10 368 − 2 592
                              = 19 473
  RESULTADO NETO: 14 215
```

**Paso 5 — recalcula el patrimonio.**

```text
capital pagado:            46 000
resultado año 1:           −2 400
resultado año 2:           +2 800
resultado año 3:          +14 215
PATRIMONIO:                60 615

  Y EL BALANCE DEBE AJUSTARSE
    patrimonio: 60 615 (era 51 900)
    → el pasivo se reduce en 8 715:
      menos necesidad de financiamiento mayorista
      obligaciones y emisiones: 321 136
```

**Paso 6 — verifica el capital regulatorio.**

```text
DEL PATRIMONIO CONTABLE AL CAPITAL REGULATORIO
  patrimonio contable                60 615
  − intangibles                      −3 200
  − activos por impuestos diferidos
    dependientes de rentabilidad     −1 840
  CAPITAL NIVEL 1 ORDINARIO          55 575

  activos ponderados: 311 725
  RATIO CET1: 17,83 %

  objetivo interno: 14,0 %
  → HOLGURA DE 3,83 PUNTOS
```

**Paso 7 — evalúa la holgura de capital.**

```text
UNA HOLGURA DE 3,83 PUNTOS SOBRE EL OBJETIVO
ES CAPITAL QUE NO ESTÁ TRABAJANDO

  capital excedente: 55 575 − 43 642 = 11 933

  OPCIONES
    a) crecer más: 85 236 de activos ponderados adicionales
       → 109 277 de cartera adicional
    b) repartir dividendos
    c) mantenerlo como colchón

  Y LA PREGUNTA DE LA PARTE 15, CLASE 5
    ¿qué pasa con esta holgura en el escenario adverso?
    → se responde en la clase 15 del proyecto
    → hasta entonces, NO se decide
```

**Paso 8 — verifica el flujo de efectivo.**

```text
FLUJO DE EFECTIVO DEL AÑO 3 (método indirecto)

  OPERACIÓN
    resultado neto                      14 215
    + provisiones                       12 960
    + amortizaciones                     1 388
    − aumento de cartera bruta         −98 400
    + aumento de depósitos              24 600
    FLUJO DE OPERACIÓN                 −45 237

  INVERSIÓN
    inversión en activo fijo            −2 100
    aumento de activos líquidos        −18 000
    FLUJO DE INVERSIÓN                 −20 100

  FINANCIAMIENTO
    aumento de obligaciones            +72 400
    FLUJO DE FINANCIAMIENTO            +72 400

  VARIACIÓN DE CAJA                     +7 063
  caja inicial                          41 137
  CAJA FINAL                            48 200  ✓
```

```text
LO QUE EL FLUJO REVELA
  el banco genera resultado y CONSUME caja
  porque está creciendo

  un banco en crecimiento tiene flujo de operación
  negativo por definición: la cartera crece
  más rápido que los depósitos

  → y por eso depende del financiamiento mayorista
    → y por eso su liquidez es el riesgo a vigilar
      (clase 11)
```

**Interpreta:** la verificación contable encontró **una incoherencia de 5 805 entre el gasto supuesto y
el gasto dimensionado**, y esa diferencia había estado propagándose por dos clases. El balance no admite
interpretación: si no cuadra, hay un error, y esa propiedad es la que convierte a la contabilidad en el
verificador de todo el proyecto.

## 🏦 Del cliente al banco

El cliente se atrasa y el banco reconoce una pérdida esperada en su resultado. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «El banco publica sus estados» | Información al mercado | 15, clase 12 |
| «Mi crédito pasó a otra clasificación» | Traspaso de etapa NIIF 9 | 5, clase 12 |
| «El banco provisionó por mi atraso» | Pérdida esperada de toda la vida | 16, clase 10 |
| «Me reprogramaron y cambió mi clasificación» | Reprogramación como criterio de etapa 2 | 13, clase 13 |
| «El banco crece y no reparte utilidades» | Consume caja al crecer | 16, clase 10 |

## 🧪 Práctica

El laboratorio pide calcular la provisión y proyectar los estados. La conciliación entre gestión y contabilidad es parte del entregable.

En `labs/lab-05.md`, sección contable:

1. Construye el plan de cuentas y los criterios de traspaso entre etapas.
2. Calcula la provisión por etapa y por producto.
3. Elabora los tres estados proyectados y verifica que cuadren.
4. Concilia el patrimonio con el resultado acumulado y resuelve las diferencias.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen provisiones mal calculadas. Las causas son etapas mal asignadas y parámetros no actualizados.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| El patrimonio no cuadra con el resultado | Incoherencia en alguna clase | Búscala y resuélvela. |
| Se confunde provisión con costo de riesgo | Saldo frente a flujo | Distínguelos. |
| Criterios de etapa solo por atraso | Se pierde anticipación | Añade señales propias del modelo. |
| Se usa un porcentaje de gasto | El dimensionado es la cifra correcta | Usa el cálculo detallado. |
| Capital regulatorio igual al patrimonio | Faltan deducciones | Aplícalas. |
| Flujo de operación positivo en crecimiento | Improbable | Verifica el aumento de cartera. |

## ❓ Preguntas de comprobación

1. ¿Qué cinco condiciones verifican la coherencia contable de un banco?
2. ¿Qué distingue la provisión del costo de riesgo?
3. ¿Por qué el criterio de caída de ventas anticipa más que el atraso?
4. ¿Por qué un banco en crecimiento tiene flujo de operación negativo?
5. ¿Qué separa el patrimonio contable del capital regulatorio?

## 📥 Entregable

Guarda en `portfolio/parte-16/clase-10/`:

- el plan de cuentas y los criterios de traspaso entre etapas;
- el cálculo de la provisión por etapa y producto;
- los tres estados financieros proyectados, cuadrados;
- la conciliación del patrimonio y la resolución de las diferencias encontradas.

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

- IFRS Foundation. *NIIF 9 Instrumentos Financieros*, sección de deterioro. <https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/>
- Basel Committee on Banking Supervision (2015). *Guidance on credit risk and accounting for expected credit losses*. BIS. <https://www.bis.org/bcbs/publ/d350.htm>
- IFRS Foundation. *NIC 1* y *NIC 7*: presentación y flujos de efectivo. IFRS.
- Kieso, D., Weygandt, J. y Warfield, T. (2020). *Intermediate Accounting* (17.ª ed.). Wiley.
- Basel Committee on Banking Supervision (2017). *Prudential treatment of problem assets*. BIS.
- Verificación local: revisa el plan de cuentas y las normas de provisiones que exige tu supervisor, que pueden ser más estrictas que NIIF 9.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 09 · Operaciones y pagos](09-operaciones-y-pagos.md) | [Parte 16](../README.md) · [Programa](../../../SYLLABUS.md) | [11 · Tesorería y balance →](11-tesoreria-y-balance.md) |
<!-- gen:footer:end -->
