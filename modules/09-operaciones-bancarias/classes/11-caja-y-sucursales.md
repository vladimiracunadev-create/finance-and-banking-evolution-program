---
part: 10
class: 11
title: "Caja y sucursales"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 11 · Caja y sucursales

> [← 10 · Tarjetas y adquirencia](10-tarjetas-y-adquirencia.md) · [Índice de la parte](../README.md) · [12 · Tesorería →](12-tesoreria.md)

**Parte 10 — Operaciones bancarias** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Gestionar el canal físico en un contexto de digitalización acelerada. La sucursal pasó de ser el canal
principal a ser un canal especializado y caro, y su gestión exige decisiones sobre red, dotación,
efectivo y seguridad que tienen efecto directo en el costo y en el servicio.

Las clases anteriores tratan operaciones y sus costos. Esta trata el canal más caro y el que más discusiones estratégicas genera. Y lo plantea como una decisión económica y no ideológica: una sucursal tiene un costo de servir medible y una función que puede no ser transaccional.

## 📚 Objetivos

Al finalizar podrás:

1. **Analizar** la rentabilidad de una sucursal y de la red.
2. **Dimensionar** la dotación y el efectivo necesarios.
3. **Aplicar** los controles de seguridad física y operativa.
4. **Evaluar** decisiones de apertura, transformación o cierre.
5. **Diseñar** el rol de la sucursal en un modelo multicanal.

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

Los tres primeros términos son la economía del canal; los cuatro siguientes, la operación de efectivo y los dos papeles posibles de una sucursal. La distinción entre **sucursal transaccional y de asesoría** es la que resuelve el debate: la primera compite con el móvil y pierde, la segunda no compite con él.

| Concepto | Comprensión verificable |
|---|---|
| `costo de servir` | Costo total de atender a un cliente por un canal determinado. |
| `transaccionalidad` | Volumen de operaciones que realiza la sucursal. |
| `migración de canal` | Traslado de operaciones desde la sucursal hacia canales digitales. |
| `dotación de efectivo` | Cantidad de efectivo que la sucursal mantiene. Tiene costo y riesgo. |
| `remesa` | Traslado de efectivo entre la sucursal y el centro de acopio. |
| `sucursal transaccional` | Enfocada en operaciones. Modelo en declive. |
| `sucursal de asesoría` | Enfocada en venta y servicio complejo. Modelo predominante. |

## 🧠 Modelo mental

El modelo mental es una comparación de costos por transacción: la misma operación cuesta órdenes de magnitud distintas según el canal, y esa diferencia es lo que decide qué se migra y qué no.

El costo de una operación difiere radicalmente por canal:

```text
operación en sucursal con cajero      1 800 a 3 200 unidades
operación en cajero automático          280 a   450
operación en aplicación móvil            12 a    40
operación en canal de voz automatizado   90 a   160
```

**Una operación en sucursal cuesta entre 45 y 150 veces más que en la aplicación.** De ahí que la
migración de transacciones sea la palanca de eficiencia más potente de la banca minorista.

## 📖 Desarrollo

### 1. Rentabilidad de una sucursal

Una sucursal se evalúa como una unidad de negocio con ingresos y costos propios. El procedimiento siguiente lo hace.

```text
INGRESOS ATRIBUIBLES (mensual, millones)
  margen de captaciones                       38,4
  margen de colocaciones                      52,1
  comisiones de productos vendidos            14,8
  TOTAL                                      105,3

COSTOS
  personal                                   −42,6
  arriendo y gastos de local                 −18,2
  seguridad                                   −6,4
  efectivo (costo de oportunidad y remesas)   −4,1
  tecnología y comunicaciones                 −3,8
  costos asignados de servicios centrales    −16,9
  TOTAL                                      −92,0

RESULTADO                                     13,3
```

**El desafío de la atribución:**

```text
· un cliente abre su cuenta en la sucursal y opera 100 % en la aplicación
  ¿a qué canal se atribuye el margen?
· un cliente contrata un crédito en línea tras una asesoría en sucursal
  ¿quién generó la venta?

sin una metodología clara de atribución, la sucursal parece menos rentable
de lo que es, y la decisión de cierre se toma con datos incompletos
```

### 2. Dotación de personal y de efectivo

**Personal:**

```text
dotación = f(transacciones, tiempo por transacción, horario, nivel de servicio)
```

```text
transacciones diarias promedio: 340
tiempo promedio por transacción: 4,2 minutos
horario de atención: 6 horas efectivas
tiempo productivo por cajero: 75 % (descansos, cierres, arqueos)

cajeros necesarios = (340 × 4,2)/(6 × 60 × 0,75) = 1 428/270 = 5,3 → 6 cajeros

para nivel de servicio con espera máxima de 10 minutos en hora peak,
el cálculo requiere teoría de colas: la demanda no es uniforme
```

**Efectivo:**

```text
dotación óptima de efectivo equilibra:
  · costo de quedarse sin efectivo (servicio, reputación)
  · costo de mantener exceso (oportunidad, seguridad, seguro)
  · costo de las remesas (transporte, riesgo)
```

```text
demanda diaria promedio de efectivo:    82 millones
desviación estándar:                    24 millones
nivel de servicio objetivo: 98 % (z = 2,05)

dotación = 82 + 2,05 × 24 = 131 millones

costo de mantener 131 millones:
  costo de oportunidad: 131 × 6,2 %/365 = 22 250 por día
  seguro y seguridad: 8 400 por día
  TOTAL: 30 650 por día

costo de una remesa adicional: 180 000
frecuencia óptima: la que iguala el costo marginal de mantener con el de reponer
```

### 3. Controles de seguridad

El manejo de efectivo tiene controles físicos y de procedimiento. La tabla los recoge.

```text
SEGURIDAD FÍSICA
  · bóveda con doble clave y apertura con retardo
  · cajas fuertes de depósito temporal para cajeros
  · límite de efectivo en poder de cada cajero
  · sistema de alarma y videovigilancia con respaldo
  · protocolo de asalto: no resistir, activar alarma silenciosa
  · control de acceso a áreas restringidas

SEGURIDAD OPERATIVA
  · arqueos diarios y sorpresivos (clase 5)
  · segregación entre operación y control
  · doble intervención para operaciones sobre umbral
  · rotación de personal
  · vacaciones obligatorias continuas (detectan fraudes que requieren gestión diaria)
  · revisión de operaciones del personal en sus propias cuentas
```

**Las vacaciones obligatorias continuas** son un control subestimado: muchos fraudes internos
requieren intervención diaria para mantenerse ocultos, y una ausencia de dos semanas los revela.

### 4. Decisiones sobre la red

Las decisiones sobre la red se toman con datos de transaccionalidad y de valor del cliente. La tabla recoge los criterios.

```text
ANÁLISIS DE UNA SUCURSAL

  transaccionalidad         ¿cuántas operaciones y de qué tipo?
  migración                 ¿qué proporción puede migrar a digital?
  cartera                   ¿qué clientes y qué saldos dependen de ella?
  cobertura                 ¿hay alternativa cercana?
  rentabilidad              ¿cuál es su resultado con atribución correcta?
  estratégico               ¿tiene valor de presencia o de captación?
```

**Opciones más allá de abrir o cerrar:**

| Opción | Cuándo |
|---|---|
| Transformar a sucursal de asesoría | Alta migración transaccional, cartera relevante |
| Reducir horario o dotación | Baja transaccionalidad en ciertas franjas |
| Convertir a punto de autoservicio | Transaccionalidad simple y baja asesoría |
| Compartir espacio con otro servicio | Costo de local alto |
| Corresponsalía (agente no bancario) | Zonas de baja densidad |
| Cerrar con plan de migración | Sin cartera relevante y con alternativa cercana |

**El cierre exige un plan de migración:** contactar a los clientes, ofrecer alternativas, acompañar a
los de mayor dificultad digital. Un cierre sin plan produce fuga de clientes muy superior a la
esperada.

### 5. El rol en un modelo multicanal

En un modelo multicanal la sucursal tiene un papel acotado y valioso, o ninguno. La tabla lo delimita.

```text
la sucursal deja de ser el canal transaccional y pasa a ser:
  · el canal de la venta compleja (hipotecario, empresas, inversión)
  · el canal de la resolución de problemas
  · el canal de la incorporación de clientes con menor autonomía digital
  · el punto de presencia y de confianza
```

```text
INDICADORES DEL NUEVO ROL
  · % de transacciones simples migradas a digital
  · ventas por ejecutivo, no transacciones por cajero
  · tasa de resolución en primera visita
  · satisfacción en operaciones complejas
  · clientes incorporados a canales digitales desde la sucursal
```

## 🧮 Ejemplo guiado

El ejemplo evalúa la rentabilidad de una sucursal y decide sobre su continuidad. Conviene separar el resultado transaccional del valor de los clientes atendidos: la decisión cambia.

**Situación.** Un banco evalúa qué hacer con una sucursal de bajo resultado.

```text
SUCURSAL LAS PALMAS
  transacciones mensuales                     6 800
  de las cuales, simples (giro, depósito, pago)  5 440  (80 %)
  clientes atribuidos                          4 200
  saldo de captaciones                        18 400 millones
  saldo de colocaciones                       12 100 millones
  resultado mensual                           −4,2 millones
  sucursal más cercana                        3,8 km
  dotación                                    11 personas
```

**Paso 1 — analiza la composición de las transacciones.**

```text
transacciones simples: 5 440 (80 %)
  de las cuales, migrables a digital: 4 900 (90 % de las simples)
  
transacciones complejas: 1 360 (20 %)
  asesoría, apertura, crédito, resolución de problemas
```

**Paso 2 — estima el potencial de migración.**

```text
perfil de los clientes que realizan transacciones simples:
  con aplicación instalada y activa:        62 %
  con aplicación instalada sin uso:         21 %
  sin aplicación:                           17 %

potencial de migración realista:
  · el 62 % ya podría migrar: falta incentivo o hábito
  · el 21 % requiere acompañamiento
  · el 17 % requiere incorporación
```

**Paso 3 — evalúa la opción de cierre.**

```text
ahorro estimado: 92 millones anuales (costo total de la sucursal)

riesgo de fuga de clientes:
  experiencia del banco en cierres previos: 12 % a 18 % de fuga de saldos
  con plan de migración estructurado: 6 % a 9 %

pérdida por fuga (escenario con plan, 7,5 %):
  captaciones: 18 400 × 0,075 = 1 380 millones
  colocaciones: 12 100 × 0,075 = 908 millones
  margen perdido anual: 1 380 × 0,059 + 908 × 0,041 = 81 + 37 = 118 millones

RESULTADO DEL CIERRE: ahorro 92 − pérdida de margen 118 = −26 millones
→ EL CIERRE DESTRUYE VALOR
```

**Paso 4 — evalúa la transformación.**

```text
TRANSFORMACIÓN A SUCURSAL DE ASESORÍA

cambios:
  · dotación de 11 a 6 personas (2 ejecutivos comerciales, 2 de servicio,
    1 jefe, 1 cajero para operaciones que lo requieran)
  · instalación de dos terminales de autoservicio
  · reducción de superficie a la mitad, subarriendo del resto
  · plan de acompañamiento digital a clientes

costos:
  inversión inicial (remodelación y equipos): 140 millones
  costos anuales: de 92 a 51 millones → ahorro 41 millones

ingresos:
  con 2 ejecutivos dedicados a venta en lugar de operación:
  incremento estimado de colocaciones: 8 % de la cartera
  margen adicional: 12 100 × 0,08 × 0,041 = 40 millones anuales
  
  ingreso por subarriendo: 14 millones anuales

RESULTADO ANUAL DE LA TRANSFORMACIÓN:
  41 (ahorro) + 40 (venta) + 14 (subarriendo) = 95 millones de mejora
  resultado de la sucursal: −4,2 × 12 = −50,4 → +44,6 millones anuales
  
  recuperación de la inversión: 140/95 = 1,5 años
```

**Paso 5 — verifica los supuestos críticos.**

```text
SUPUESTO 1: la migración de transacciones simples es viable
  verificación: el 62 % ya tiene aplicación activa
  riesgo: el 17 % sin aplicación puede requerir la sucursal
  mitigante: los terminales de autoservicio cubren la mayoría de esas operaciones

SUPUESTO 2: los ejecutivos liberados generan 8 % más colocaciones
  verificación: comparar con sucursales ya transformadas
  dato: en 6 transformaciones previas, el incremento fue de 5 % a 11 %
  → el supuesto de 8 % es el punto medio: razonable

SUPUESTO 3: el subarriendo se concreta
  verificación: demanda de locales en la zona
  riesgo: si no se concreta, la mejora baja a 81 millones
  → sigue siendo positiva
```

**Paso 6 — plan de acompañamiento digital.**

```text
el elemento que determina el éxito de la transformación

FASE 1 (mes 1–2): identificación
  segmentar a los 4 200 clientes por autonomía digital

FASE 2 (mes 2–4): acompañamiento activo
  · el 21 % con aplicación sin uso: sesión de acompañamiento en sucursal
  · el 17 % sin aplicación: instalación y primera operación asistida
  · clientes de mayor edad o menor autonomía: acompañamiento extendido

FASE 3 (mes 4–6): transición
  · terminales de autoservicio con asistencia presencial
  · reducción gradual de la caja tradicional

FASE 4 (mes 6+): operación en régimen
  · caja disponible para operaciones que la requieran
  · foco de la dotación en asesoría y venta

INDICADOR DE ÉXITO: % de clientes que realiza al menos una operación
digital al mes, medido mensualmente
```

**Paso 7 — decisión.**

```text
TRANSFORMAR, NO CERRAR

fundamento:
  · el cierre destruye 26 millones anuales de valor
  · la transformación crea 95 millones anuales
  · la inversión se recupera en 1,5 años
  · los supuestos críticos están verificados con experiencia propia

CONDICIÓN: el plan de acompañamiento digital es parte de la decisión,
no un accesorio. Sin él, la migración no ocurre y la transformación
solo reduce el servicio.
```

**Interpreta:** la sucursal tenía resultado negativo y **cerrarla habría destruido valor**, porque el
resultado atribuido no capturaba el margen de la cartera que depende de ella. La transformación —con
un plan de acompañamiento que suele tratarse como accesorio— convierte una pérdida de 50 millones
anuales en una ganancia de 45.

## 🏦 Del cliente al banco

El cliente valora la cercanía y el banco mide el costo de servir. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| "Cerraron mi sucursal" | Decisión de red con plan de migración | 15, clase 10 |
| Menos cajas, más autoservicio | Migración de transacciones simples | 15, clase 10 |
| Ejecutivo asignado | Foco de la sucursal en asesoría | 15, clase 9 |
| Acompañamiento para usar la aplicación | Inversión en autonomía digital del cliente | 14, clase 2 |
| Espera en hora peak | Dimensionamiento de dotación | 10, clase 11 |

## 🧪 Práctica

El laboratorio pide evaluar tres sucursales y recomendar. Una de ellas pierde dinero en transacciones y concentra clientes de alto valor, que es el caso interesante.

En `labs/lab-06.md`:

1. Construye el estado de resultados de una sucursal con atribución de ingresos.
2. Dimensiona la dotación de personal y de efectivo con los métodos de la clase.
3. Evalúa las seis opciones de red para una sucursal de bajo resultado.
4. Diseña un plan de acompañamiento digital con sus fases e indicadores.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen decisiones de red mal tomadas. Las causas son evaluar solo por transacciones o solo por cercanía.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se cierra por resultado negativo | Atribución incompleta del margen | Considera la cartera que depende de la sucursal. |
| Se transforma sin plan de acompañamiento | La migración no ocurre | El plan es parte de la decisión. |
| Dotación calculada con promedios | La demanda no es uniforme | Considera la hora peak y el nivel de servicio. |
| Exceso de efectivo en sucursal | Costo de oportunidad y riesgo | Optimiza dotación y frecuencia de remesas. |
| Sin vacaciones obligatorias continuas | Control de fraude interno ausente | Es un control de bajo costo y alto efecto. |
| Se mide por transacciones | Indicador del modelo antiguo | Mide ventas, resolución y migración. |

## ❓ Preguntas de comprobación

1. ¿Cuántas veces más cuesta una operación en sucursal que en la aplicación?
2. ¿Por qué la atribución de ingresos determina la decisión de cierre?
3. ¿Cómo se dimensiona la dotación de efectivo de una sucursal?
4. ¿Por qué las vacaciones obligatorias continuas son un control de fraude?
5. ¿Qué indicadores corresponden al nuevo rol de la sucursal?

## 📥 Entregable

Guarda en `portfolio/parte-10/clase-11/`:

- el estado de resultados de una sucursal con su metodología de atribución;
- el dimensionamiento de dotación de personal y de efectivo;
- la evaluación de las seis opciones de red con su resultado cuantificado;
- el plan de acompañamiento digital con fases, indicadores y responsables.

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

- Rose, P. y Hudgins, S. (2013). *Bank Management & Financial Services* (9.ª ed.). McGraw-Hill. Capítulo 4: organización de la red de distribución.
- Bank for International Settlements (2018). *Sound Practices: Implications of fintech developments for banks and bank supervisors*. BIS. Transformación de canales.
- Basel Committee on Banking Supervision (2011). *Principles for the Sound Management of Operational Risk*. BIS. Controles de seguridad operativa.
- Deloitte / McKinsey. Informes anuales sobre transformación de redes de sucursales. Datos comparados de costo por canal.
- Committee on Payments and Market Infrastructures (2020). *Payment aspects of financial inclusion*. Corresponsalías y acceso en zonas de baja densidad.
- Verificación local: revisa las exigencias de tu supervisor sobre cierre de sucursales, cobertura territorial y corresponsalías no bancarias.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 10 · Tarjetas y adquirencia](10-tarjetas-y-adquirencia.md) | [Parte 10](../README.md) · [Programa](../../../SYLLABUS.md) | [12 · Tesorería →](12-tesoreria.md) |
<!-- gen:footer:end -->
