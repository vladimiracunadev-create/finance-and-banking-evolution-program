<!-- meta
part: 18
class: 3
title: "Corresponsalía bancaria"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global]
regulatory_topics: [cross-border-payments, aml-cft, acceso-financiero]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [CPMI, FSB, GAFI]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 03 · Corresponsalía bancaria

> [← 02 · Arquitectura de participantes y responsabilidades](02-arquitectura-de-participantes.md) · [Índice de la parte](../README.md) · [04 · Cuentas nostro, vostro y loro →](04-cuentas-nostro-vostro-y-loro.md)

**Parte 18 — Pagos transfronterizos, remesas y liquidación internacional** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Entender la corresponsalía como lo que es —**una relación de crédito y confianza
entre dos bancos, no un cable**— y analizar por qué la red mundial se ha
contraído aunque el volumen de pagos haya crecido.

La cadena de la clase anterior se sostiene sobre relaciones entre bancos. Esta explica esas relaciones, sus obligaciones asimétricas y por qué la red mundial se está reduciendo en vez de crecer.

## 📚 Objetivos

Al finalizar podrás:

1. **Explicar** qué obtiene cada parte de una relación de corresponsalía y qué
   riesgo asume.
2. **Describir** el proceso de debida diligencia y el concepto de banca anidada.
3. **Analizar** el fenómeno de retirada de relaciones con datos, no con
   opiniones.
4. **Evaluar** la decisión de mantener o cerrar un corredor con un cálculo
   completo.
5. **Distinguir** la reducción de riesgo legítima del abandono indiscriminado.

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

Los cuatro primeros términos son la relación y sus partes; los cuatro siguientes, sus riesgos y su crisis. La **retirada de relaciones** es el fenómeno que está reduciendo la red mundial: los corresponsales cierran cuentas cuando el coste de cumplimiento supera al ingreso, y corredores enteros se quedan sin vía formal.

| Concepto | Comprensión verificable |
|---|---|
| `corresponsalía` | Relación por la que un banco presta servicios a otro en su plaza |
| `banco respondedor` | Banco que recibe el servicio, mantiene cuenta en el corresponsal |
| `banco corresponsal` | Banco que presta el servicio y custodia la cuenta |
| `debida diligencia reforzada` | Análisis exigido antes de abrir la relación y periódicamente |
| `banca anidada` | Un respondedor da acceso a la cuenta a bancos terceros |
| `pago de terceros` | Pago cuyo ordenante no es cliente del respondedor |
| `retirada de relaciones` | Cierre masivo de corresponsalías por coste o riesgo |
| `banco de último recurso` | Único corresponsal que queda en un corredor |

## 🧠 Modelo mental

El modelo mental es una relación de confianza con obligaciones asimétricas: el corresponsal responde ante su supervisor por lo que haga el respondedor, y por eso exige una diligencia que puede ser más cara que el negocio.

```text
UNA CORRESPONSALÍA NO ES UNA CONEXIÓN TÉCNICA:
ES UN CRÉDITO Y UNA RESPONSABILIDAD

  EL CORRESPONSAL LE PRESTA AL RESPONDEDOR
    · acceso a su sistema de pagos nacional
    · acceso a su moneda
    · a veces, descubierto intradía

  Y ASUME
    · el riesgo de crédito del respondedor
    · el riesgo de cumplimiento de los clientes del
      respondedor, a los que NO conoce
    · la responsabilidad ante SU supervisor
      por lo que pase en esa cuenta

LA ASIMETRÍA QUE EXPLICA TODO
  el corresponsal cobra unos pocos dólares por operación
  y responde ante su supervisor por operaciones
  de clientes que nunca ha visto
```

## 📖 Desarrollo

### 1. Qué obtiene cada parte

```text
EL RESPONDEDOR OBTIENE
  · alcance a una moneda y a un sistema de pagos ajenos
  · sin abrir sucursal ni obtener licencia local
  · sin cumplir la regulación prudencial de esa plaza

EL CORRESPONSAL OBTIENE
  · comisiones por operación
  · saldos en cuenta que puede remunerar por debajo del mercado
  · volumen que amortiza su infraestructura

LO QUE NINGUNO OBTIENE
  · conocimiento directo del cliente final
  → esa es la raíz del problema de cumplimiento
```

### 2. La debida diligencia reforzada

```text
ANTES DE ABRIR LA RELACIÓN, EL CORRESPONSAL EVALÚA

  1. propiedad y control del respondedor
  2. su licencia, su supervisor y la calidad de esa supervisión
  3. su programa de prevención de lavado y su gobierno
  4. su base de clientes y sus mercados
  5. si permite BANCA ANIDADA, y a quién
  6. si opera pagos de terceros
  7. su historial de sanciones y de incidentes
  8. la reputación del país y su marco normativo

Y ACUERDA POR ESCRITO
  · qué operaciones se admiten y cuáles no
  · qué información acompaña a cada pago
  · qué derecho de auditoría existe
  · en qué casos se suspende la relación
```

### 3. Banca anidada: el riesgo que no se ve

```text
BANCO A (corresponsal, plaza fuerte)
   │ cuenta
BANCO B (respondedor, país X)
   │ le da acceso a...
BANCO C, D, E (bancos de países Y y Z)
   │
   └── sus clientes usan la cuenta de B en A

LO QUE VE EL BANCO A
  operaciones de su cliente B

LO QUE REALMENTE PASA POR SU BALANCE
  operaciones de clientes de C, D y E,
  en países que A quizá no aceptaría directamente

POR QUÉ IMPORTA
  A responde ante su supervisor por esas operaciones
  y no tiene forma de conocer a sus originadores

  → la banca anidada no está prohibida en general,
    pero exige declararse, autorizarse y controlarse
```

### 4. La retirada de relaciones

```text
QUÉ SE OBSERVA
  el número de relaciones de corresponsalía activas
  en el mundo lleva más de una década descendiendo,
  mientras el volumen y el valor de los pagos crecen

INTERPRETACIÓN CORRECTA
  concentración: los mismos pagos por menos rutas

POR QUÉ OCURRE
  · el coste de cumplimiento por relación creció mucho
  · las sanciones por incumplimiento son muy altas
  · la rentabilidad por operación es baja
  · el riesgo reputacional no se compensa con comisiones
  · un corredor pequeño no amortiza su propia diligencia

DÓNDE DUELE
  corredores pequeños, economías en desarrollo,
  jurisdicciones con supervisión percibida como débil,
  organizaciones sin fines de lucro y remesas
```

### 5. Reducción de riesgo frente a abandono

| | Reducción de riesgo legítima | Abandono indiscriminado |
|---|---|---|
| Criterio | Por cliente y operación | Por país o por categoría entera |
| Base | Evaluación documentada | Percepción o titular de prensa |
| Alternativa | Se ofrece otra vía o se avisa | Se cierra sin transición |
| Efecto | Menos riesgo, mismo acceso | Exclusión y flujos hacia canales opacos |
| Coherencia | Consistente con el apetito declarado | Reactiva |

```text
LA PARADOJA QUE HAY QUE PODER EXPLICAR
  cerrar un corredor por riesgo de lavado
  empuja esos flujos a canales informales,
  donde no hay screening, ni registro, ni trazabilidad

  → el riesgo no desaparece del sistema:
    desaparece de la vista
```

## 🧮 Ejemplo guiado

El ejemplo evalúa una relación de corresponsalía con su diligencia reforzada. Conviene comparar el coste del cumplimiento con el ingreso: es la cuenta que produce las retiradas.

**Situación.** Un banco evalúa si mantiene su corresponsalía con un banco
respondedor de un país pequeño. La relación lleva 9 años.

```text
DATOS DE LOS ÚLTIMOS 12 MESES
  operaciones procesadas                        14 200
  valor total                                   186 000 000 USD
  ingreso por comisiones                           142 000 USD
  saldo medio en la cuenta vostro                4 100 000 USD
  margen por el saldo (2,1 % neto)                  86 100 USD
  INGRESO TOTAL                                    228 100 USD

COSTES DIRECTOS
  diligencia anual y revisión periódica             48 000 USD
  screening y revisión de alertas                   71 000 USD
  personal de relación                              55 000 USD
  auditoría específica                              26 000 USD
  TOTAL                                            200 000 USD

MARGEN CONTABLE: 28 100 USD

ALERTAS DEL AÑO
  alertas generadas                                  2 840
  escaladas a revisión                                 312
  reportes a la unidad de inteligencia financiera        7
  operaciones bloqueadas                                 3

INCIDENTES
  una operación de 2023 objeto de requerimiento del supervisor;
  cerrada sin sanción, coste legal 34 000 USD
```

**Paso 1 — corrige el margen con el coste no recurrente.**

```text
EL COSTE LEGAL NO ES ANUAL, PERO NO ES CERO
  amortizado en 5 años: 34 000 / 5 = 6 800 USD/año

MARGEN CORREGIDO
  28 100 − 6 800 = 21 300 USD
  sobre 228 100 de ingreso: 9,3 % de margen
```

**Paso 2 — calcula el coste por operación.**

```text
COSTE TOTAL / OPERACIONES
  206 800 / 14 200 = 14,56 USD por operación
INGRESO POR OPERACIÓN
  228 100 / 14 200 = 16,06 USD
MARGEN POR OPERACIÓN: 1,50 USD
```

**Paso 3 — evalúa el riesgo con la métrica correcta.**

```text
TASA DE ALERTAS
  2 840 / 14 200 = 20,0 % de las operaciones generan alerta

TASA DE ESCALADO
  312 / 2 840 = 11,0 %

TASA DE REPORTE
  7 / 312 = 2,2 %

COMPARACIÓN CON LA CARTERA GENERAL DEL BANCO
  tasa de alertas de la cartera:      3,8 %
  → este corredor genera 5,3 veces más alertas

  PERO la tasa de reporte de la cartera es 1,9 %
  y aquí es 2,2 %: SIMILAR

INTERPRETACIÓN
  el corredor genera muchas alertas y una proporción
  de reportes parecida a la del resto
  → el problema es de CALIBRACIÓN del modelo,
    no necesariamente de riesgo del corredor
```

**Paso 4 — evalúa la exposición máxima.**

```text
LA PREGUNTA QUE DECIDE
  ¿cuánto puede costar un incumplimiento?

  no se puede estimar con una distribución:
  las sanciones por infracciones graves en corresponsalía
  se han situado en órdenes de magnitud muy superiores
  al ingreso de una relación como esta

  MARGEN ANUAL:        21 300 USD
  EXPOSICIÓN POSIBLE:  varios órdenes de magnitud mayor

  → el margen NO compensa la cola de la distribución
```

**Paso 5 — no saltes a la conclusión fácil.**

```text
LA CONCLUSIÓN FÁCIL ES «CERRAR».
ANTES HAY QUE RESPONDER TRES PREGUNTAS.

  1. ¿ES ESTE BANCO EL ÚNICO CORRESPONSAL DEL PAÍS?
     si sí, cerrar deja el corredor sin ruta formal
     → el flujo no desaparece: se informaliza

  2. ¿EL RIESGO ESTÁ EN EL RESPONDEDOR O EN NUESTRO MODELO?
     20 % de alertas con 2,2 % de reportes sugiere
     un modelo mal calibrado para ese corredor

  3. ¿HAY MEDIDAS INTERMEDIAS ENTRE MANTENER Y CERRAR?
     · prohibir banca anidada
     · limitar tipos de operación y umbrales
     · exigir información estructurada completa
     · pedir derecho de auditoría anual
     · recalibrar el screening por corredor
```

**Paso 6 — cuantifica la vía intermedia.**

```text
MEDIDAS Y SU EFECTO ESTIMADO

  recalibrar screening por corredor
    alertas: 2 840 → 980  (−65 %)
    ahorro en revisión: 71 000 × 60 % = 42 600 USD

  prohibir banca anidada y pagos de terceros
    operaciones: 14 200 → 12 400  (−12,7 %)
    ingreso: 228 100 × 0,873 ≈ 199 100 USD
    reduce la exposición a originadores desconocidos

  exigir datos estructurados completos
    reparaciones y rechazos a la baja
    coste de implantación: 18 000 USD, una vez

MARGEN RESULTANTE
  ingreso        199 100
  costes         200 000 − 42 600 = 157 400
  amortización de la implantación (3 años): 6 000
  margen         199 100 − 163 400 = 35 700 USD
  → margen SUPERIOR al actual, con menos exposición
```

**Paso 7 — decide.**

```text
MANTENER CON RESTRICCIONES, NO CERRAR

  1. prohibir banca anidada y pagos de terceros, por escrito
  2. recalibrar el screening específicamente para el corredor
  3. exigir datos estructurados y rechazar lo incompleto
  4. derecho de auditoría anual, con la primera a 6 meses
  5. límite de exposición intradía
  6. revisión de la decisión a 12 meses con estos umbrales:
       tasa de reporte > 4 %          → reevaluar
       hallazgo grave en auditoría    → suspender
       margen < 15 000 USD            → reevaluar

  Y DEJAR ESCRITO EL RAZONAMIENTO
    la decisión se sostiene en que el riesgo medido
    es de calibración, no de conducta del respondedor.
    Si la auditoría contradice ese supuesto,
    la decisión cambia: no es una posición, es una hipótesis.
```

**Interpreta:** el análisis empezó pareciendo una decisión de rentabilidad
—21 300 de margen— y terminó siendo una decisión sobre **si el riesgo estaba en
el corredor o en el propio modelo de detección**. Cerrar habría eliminado el
ingreso, mantenido el riesgo en el sistema y cerrado un corredor.

## 🧭 Perspectivas

La corresponsalía afecta a cada actor con incentivos distintos. La tabla los recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente del corredor | Su banco ya no envía a ese país | Usa un canal informal |
| Banco respondedor | Pierde acceso a la moneda | Busca otro corresponsal o cierra |
| Banco corresponsal | 21 300 de margen y cola de riesgo | Mantener, restringir o cerrar |
| Banco central del país pequeño | Corredor sin ruta formal | Negocia o busca alternativas |
| Supervisor del corresponsal | Exposición a originadores desconocidos | Qué exige |
| GAFI | Flujos que se informalizan | Guía sobre retirada indiscriminada |
| Sociedad | Remesas más caras o inexistentes | Coste social del cierre |

## 🏦 Del cliente al banco

El cliente no sabe que existe y su pago depende de que esa relación siga viva. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Mi banco ya no envía ahí» | Corredor cerrado por riesgo | 18, clase 3 |
| «Me piden mil datos» | Debida diligencia reforzada | 18, clase 3 |
| «Uso una casa de cambio informal» | El flujo se informalizó | 18, clase 10 |
| «Antes tardaba menos» | Menos rutas, más eslabones | 18, clase 8 |

## ⚖️ Riesgos y controles

Los riesgos son de cumplimiento y de continuidad del corredor. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Banca anidada no declarada | Operaciones de bancos desconocidos | Prohibición expresa y auditoría |
| Cliente del cliente desconocido | No hay conocimiento directo | Datos estructurados completos |
| Screening mal calibrado | 20 % de alertas, cola manual | Calibración por corredor |
| Cierre indiscriminado | Exclusión y flujos opacos | Medidas intermedias documentadas |
| Concentración | Un solo corresponsal en el corredor | Vigilancia y alternativas |
| Exposición intradía | Descubierto sin límite | Límite y seguimiento |

## 🧪 Práctica

En [`labs/lab-02.md`](../labs/lab-02.md) y [`labs/lab-04.md`](../labs/lab-04.md):

1. Evalúa una relación de corresponsalía con los ocho puntos de diligencia.
2. Calcula margen, coste por operación y tasas de alerta, escalado y reporte.
3. Diseña tres medidas intermedias entre mantener y cerrar, con su efecto.
4. Escribe los umbrales que harían cambiar la decisión.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen corredores que se cierran. Las causas son diligencia insuficiente y banca anidada no declarada.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Decidir solo por margen | No se miró la cola del riesgo | Evalúa la exposición máxima |
| Cerrar el corredor entero | Se aplicó criterio por país | Criterio por cliente y operación |
| Tasa de alertas como medida de riesgo | Se confundió con reportes | Compara tasa de reporte |
| Ignorar la banca anidada | No se preguntó | Pregunta y prohíbe por escrito |
| Decisión sin umbral de revisión | Se tomó como definitiva | Escribe qué la cambiaría |
| Suponer que cerrar elimina el riesgo | Se miró el propio balance | El flujo se informaliza |

## ❓ Preguntas de comprobación

1. ¿Qué asimetría explica que la corresponsalía sea un negocio difícil?
2. ¿Qué es la banca anidada y por qué el corresponsal no la ve?
3. ¿Por qué una tasa de alertas alta no significa por sí sola un corredor
   riesgoso?
4. ¿Qué distingue la reducción de riesgo legítima del abandono indiscriminado?
5. En el ejemplo guiado, ¿por qué las medidas intermedias mejoraron el margen?

## 📥 Entregable

Guarda en `portfolio/parte-18/clase-03/`:

- la evaluación de una relación con los ocho puntos de diligencia;
- el cálculo de margen y de las tres tasas de riesgo;
- tres medidas intermedias con su efecto cuantificado;
- los umbrales que harían revisar la decisión.

## 🔗 Referencias cruzadas

- **Viene de:** clases 1 y 2; Parte 12, clase 3 (prevención de lavado).
- **Continúa en:** clase 4 (nostro y vostro), clase 12 (sanciones y regla del
  viaje), clase 10 (remesas).
- **Se aplica en:** Parte 22, clase 16 (regulación comparada); Parte 23,
  clase 15.

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

- Committee on Payments and Market Infrastructures (2016). *Correspondent banking*. BIS. <https://www.bis.org/cpmi/publ/d147.htm>
- Financial Stability Board (2019). *Correspondent Banking Data Report update*. FSB. <https://www.fsb.org/2019/05/fsb-correspondent-banking-data-report-update-2/>
- Financial Action Task Force (2016). *Guidance on correspondent banking services*. FATF. <https://www.fatf-gafi.org/>
- Wolfsberg Group. *Correspondent Banking Due Diligence Questionnaire* y *Principles for Correspondent Banking*. <https://www.wolfsberg-group.org/>
- Basel Committee on Banking Supervision (2017). *Sound management of risks related to money laundering and financing of terrorism: correspondent banking annex*. BIS. <https://www.bis.org/bcbs/publ/d405.htm>
- Verificación local: comprueba qué exige tu supervisor en materia de debida diligencia de corresponsalía y si existe orientación sobre retirada de relaciones. **Fecha de verificación de esta clase: 2026-08-06.** Esta clase no constituye asesoría legal.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 02 · Arquitectura de participantes y responsabilidades](02-arquitectura-de-participantes.md) | [Parte 18](../README.md) · [Programa](../../../SYLLABUS.md) | [04 · Cuentas nostro, vostro y loro →](04-cuentas-nostro-vostro-y-loro.md) |
<!-- gen:footer:end -->
