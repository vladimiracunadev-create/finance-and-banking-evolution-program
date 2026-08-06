---
part: 10
class: 10
title: "Tarjetas y adquirencia"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 10 · Tarjetas y adquirencia

> [← 09 · Medios de pago](09-medios-de-pago.md) · [Índice de la parte](../README.md) · [11 · Caja y sucursales →](11-caja-y-sucursales.md)

**Parte 10 — Operaciones bancarias** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Analizar los dos lados del negocio de tarjetas —emisión y adquirencia— con su economía, sus riesgos y
su gestión operativa. Es un negocio de red donde el valor depende de que ambos lados crezcan de forma
equilibrada, y donde la gestión del fraude determina la rentabilidad.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** los roles de emisor, adquirente y marca.
2. **Descomponer** la rentabilidad de cada lado del negocio.
3. **Gestionar** el ciclo de contracargos y su efecto.
4. **Aplicar** los controles de fraude por tipo de operación.
5. **Evaluar** el riesgo del comercio afiliado.

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
| `emisión` | Negocio de emitir tarjetas a tarjetahabientes. |
| `adquirencia` | Negocio de afiliar comercios y procesar sus ventas. |
| `contracargo` | Reversa de una operación a solicitud del tarjetahabiente. |
| `riesgo del comercio` | Riesgo de que el adquirente deba responder por operaciones del comercio. |
| `retención de garantía` | Fondos retenidos al comercio para cubrir contracargos futuros. |
| `tasa de contracargo` | Proporción de operaciones disputadas. Indicador clave de riesgo. |
| `mercado de dos lados` | Negocio donde el valor de cada lado depende del tamaño del otro. |

## 🧠 Modelo mental

El adquirente asume un riesgo que no es evidente:

```text
si un comercio recibe el pago y NO entrega el producto,
el tarjetahabiente reclama y obtiene un contracargo

el emisor devuelve el dinero al tarjetahabiente
el adquirente debe recuperarlo del comercio
si el comercio quebró o desapareció: LA PÉRDIDA ES DEL ADQUIRENTE
```

Por eso la adquirencia **no es solo procesamiento**: es una exposición crediticia al comercio
afiliado, con un plazo que puede extenderse meses.

## 📖 Desarrollo

### 1. Roles y flujo

```text
TARJETAHABIENTE ←→ EMISOR ←→ MARCA ←→ ADQUIRENTE ←→ COMERCIO
```

| Rol | Función | Ingreso principal |
|---|---|---|
| Emisor | Emite la tarjeta, otorga crédito, asume el riesgo del tarjetahabiente | Tasa de intercambio, intereses, comisiones |
| Marca | Provee la red, las reglas y el enrutamiento | Comisión por transacción |
| Adquirente | Afilia comercios, procesa y abona | Diferencia entre comisión al comercio e intercambio |
| Procesador | Provee la infraestructura técnica | Tarifa por transacción |

### 2. Rentabilidad de la emisión

```text
por cada 100 000 de volumen transaccional:

INGRESOS
  tasa de intercambio (1,5 %)                    1 500
  comisión de administración (prorrateada)         180
  intereses de saldo rotativo                      840
  comisiones (avances, mora, seguros)              220
  TOTAL                                          2 740

COSTOS
  costo de fondos del saldo rotativo              −310
  pérdida esperada por incumplimiento             −620
  fraude neto                                      −85
  beneficios al tarjetahabiente (puntos)          −450
  costo operativo (procesamiento, servicio)       −380
  costo de capital                                −180
  TOTAL                                         −2 025

RESULTADO                                          715  (0,72 % del volumen)
```

**Los beneficios al tarjetahabiente son el 22 % de los costos**, y su función es competitiva: sin
ellos, el cliente usa otra tarjeta y el emisor pierde el 100 % del ingreso, no el 22 %.

### 3. Rentabilidad de la adquirencia

```text
por cada 100 000 de volumen procesado:

INGRESOS
  comisión al comercio (2,2 %)                   2 200
  servicios adicionales (terminal, conciliación)    90
  TOTAL                                          2 290

COSTOS
  tasa de intercambio al emisor                 −1 500
  comisión de la marca                            −180
  costo operativo de procesamiento               −220
  pérdida por contracargos irrecuperables         −105
  costo del terminal y su mantención               −95
  TOTAL                                         −2 100

RESULTADO                                          190  (0,19 % del volumen)
```

**El margen de la adquirencia es una fracción del de la emisión**, y depende críticamente de dos
variables: la tasa de intercambio (que no controla) y las pérdidas por contracargos (que sí gestiona).

### 4. Ciclo de contracargos

```text
1. el tarjetahabiente disputa una operación ante su emisor
2. el emisor evalúa la causal y, si procede, inicia el contracargo
3. la marca enruta el contracargo al adquirente
4. el adquirente notifica al comercio y le solicita evidencia
5. si el comercio aporta evidencia suficiente: se representa el cargo
6. si no: el adquirente debita al comercio
7. si el comercio no tiene fondos: la pérdida es del adquirente
```

**Causales habituales:**

| Causal | Quién suele ganar | Evidencia decisiva |
|---|---|---|
| Producto no recibido | Tarjetahabiente | Comprobante de entrega firmado |
| Producto distinto al descrito | Tarjetahabiente | Descripción publicada y fotos |
| Operación no autorizada | Tarjetahabiente | Autenticación reforzada aplicada |
| Cobro duplicado | Tarjetahabiente | Registro de la operación única |
| Suscripción no cancelada | Variable | Política de cancelación aceptada |
| Calidad del producto | Variable | Términos de la venta |

**El control de mayor efecto para el comercio** es la autenticación reforzada en operaciones en línea:
traslada la responsabilidad de la operación no autorizada del comercio al emisor.

### 5. Riesgo del comercio afiliado

```text
el adquirente evalúa al comercio como un deudor
```

| Factor | Mayor riesgo |
|---|---|
| Rubro | Entrega diferida, servicios futuros, viajes, formación |
| Antigüedad | Reciente |
| Volumen respecto de su tamaño | Desproporcionado |
| Tasa de contracargo histórica | Superior al umbral de la marca |
| Modalidad | Venta a distancia sin presencia física de la tarjeta |
| Estacionalidad | Concentración extrema |

**El rubro de entrega diferida es el crítico:**

```text
una agencia de viajes cobra hoy por un servicio de dentro de 6 meses
si quiebra antes, TODOS los clientes reclaman contracargo
la exposición del adquirente es el volumen de los últimos 6 meses,
no el saldo del día
```

**Mitigantes:**

```text
· retención de un porcentaje de las ventas como garantía
· plazo de abono extendido para rubros de riesgo
· límites de volumen por comercio
· monitoreo de la tasa de contracargo con umbrales
· garantías o avales del comercio
· seguro de contracargos
```

## 🧮 Ejemplo guiado

**Situación.** Un adquirente evalúa la afiliación de una empresa de cursos en línea.

```text
SOLICITANTE
  empresa de formación en línea, 14 meses de operación
  volumen mensual proyectado: 380 millones
  ticket promedio: 420 000
  modalidad: 100 % venta a distancia
  producto: cursos de 6 a 12 meses de duración, pago único anticipado
  patrimonio de la empresa: 84 millones
```

**Paso 1 — identifica el perfil de riesgo.**

```text
□ rubro de entrega diferida (6 a 12 meses)          ✗ riesgo alto
□ venta a distancia sin presencia de tarjeta        ✗ riesgo alto
□ antigüedad de 14 meses                            ⚠ riesgo medio
□ volumen 4,5 veces su patrimonio mensual           ✗ riesgo alto
□ pago único anticipado por servicio futuro         ✗ riesgo alto

PERFIL: RIESGO ALTO en cinco de cinco factores
```

**Paso 2 — dimensiona la exposición.**

```text
si la empresa deja de operar, los clientes con curso vigente reclaman

exposición = volumen de los últimos 12 meses (duración máxima del servicio)
           = 380 × 12 = 4 560 millones

patrimonio de la empresa: 84 millones
cobertura: 1,8 % de la exposición
```

**La exposición potencial es 54 veces el patrimonio de la empresa.**

**Paso 3 — estima la probabilidad y la pérdida.**

```text
tasa de quiebra de empresas de formación en línea con menos de 3 años:
  estimada en 18 % a 24 % anual (dato sectorial)

si quiebra:
  proporción de clientes que reclaman contracargo: 55 % a 75 %
  recuperación del comercio: cercana a cero

pérdida esperada = 4 560 × 0,21 (quiebra) × 0,65 (reclamo) = 622 millones
```

**Paso 4 — compara con el ingreso.**

```text
ingreso anual de la adquirencia:
  380 × 12 × 0,019 (margen neto de intercambio y marca) = 87 millones

pérdida esperada: 622 millones
ingreso: 87 millones

RELACIÓN: la pérdida esperada es 7,1 veces el ingreso anual
```

**Paso 5 — diseña los mitigantes.**

```text
MITIGANTE 1: retención de garantía
  retener 15 % de cada venta durante 12 meses
  fondo acumulado en régimen: 380 × 12 × 0,15 = 684 millones
  cobertura de la exposición: 15 %

MITIGANTE 2: abono diferido
  abonar las ventas a los 30 días en lugar de a los 2
  reduce la exposición marginal, no la acumulada

MITIGANTE 3: límite de volumen
  límite mensual de 150 millones en lugar de 380
  exposición máxima: 1 800 millones
  pérdida esperada: 246 millones
  ingreso: 34 millones
  relación: 7,2 veces  → NO MEJORA la relación

MITIGANTE 4: garantía real o aval de los socios
  exigir garantía por 400 millones
  cobertura: 8,8 % de la exposición máxima

MITIGANTE 5: verificación de entrega
  exigir que el comercio registre la entrega efectiva del servicio
  reduce la tasa de éxito de los contracargos por "no recibido"

MITIGANTE 6: fideicomiso de fondos
  los fondos se liberan al comercio a medida que se presta el servicio
  cobertura: cercana al 100 % de la exposición
```

**Paso 6 — evalúa la combinación.**

```text
con MITIGANTE 6 (fideicomiso) el riesgo cambia por completo:
  los fondos no cobrados por el comercio están disponibles para devolver
  exposición residual: solo el desfase operativo

pero el fideicomiso:
  · reduce el flujo de caja del comercio
  · puede hacer inviable su modelo de negocio
  · exige infraestructura operativa
```

**Paso 7 — decisión.**

```text
AFILIAR CON CONDICIONES

  C1  retención de garantía del 15 %, liberada progresivamente a medida
      que los cursos se completan (no a plazo fijo)
  C2  límite de volumen mensual de 200 millones el primer año,
      revisable con historial
  C3  aval solidario de los socios por 400 millones
  C4  obligación de registrar la entrega efectiva del servicio en la plataforma
  C5  monitoreo mensual de la tasa de contracargo, con umbral de 0,8 %
  C6  derecho a suspender el abono si la tasa supera el umbral
  C7  revisión de estados financieros semestral

  exposición máxima estimada con las condiciones: 2 400 millones
  cobertura (retención + aval): 760 millones = 31,7 %
  pérdida esperada residual: 336 millones
  ingreso anual: 46 millones
  relación: 7,3 veces  → SIGUE SIENDO DESFAVORABLE
```

**Paso 8 — la decisión correcta.**

```text
RECHAZAR bajo las condiciones evaluadas

la relación pérdida esperada / ingreso de 7,3 veces no se corrige
con mitigantes parciales

ALTERNATIVA: afiliar con fideicomiso de fondos
  · los fondos se liberan mensualmente conforme se presta el servicio
  · exposición residual: 1 mes de ventas = 200 millones
  · pérdida esperada: 27 millones
  · ingreso: 46 millones
  · relación: 0,59 veces  → VIABLE

  esta estructura es común en rubros de entrega diferida y protege
  a las tres partes: al cliente, al adquirente y al propio comercio,
  que gana credibilidad
```

**Interpreta:** el análisis convencional —volumen, antigüedad, patrimonio— habría llevado a un rechazo
o a una afiliación con retención estándar. **El dimensionamiento de la exposición por duración del
servicio** mostró que ningún mitigante parcial corrige la relación, y que la solución estructural es
cambiar el momento en que el comercio recibe los fondos.

## 🏦 Del cliente al banco

| Vista del comercio | Vista del adquirente | Parte |
|---|---|---|
| "Retienen parte de mis ventas" | Garantía ante contracargos futuros | 10, clase 10 |
| Abono en 2 días | Plazo según el riesgo del rubro | 10, clase 10 |
| Comisión alta en venta a distancia | Mayor tasa de contracargo | 4, clase 6 |
| Autenticación reforzada exigida | Traslada la responsabilidad al emisor | 4, clase 5 |
| Contracargo perdido | Sin evidencia de entrega | 4, clase 6 |

## 🧪 Práctica

En `labs/lab-05.md`, sección de tarjetas:

1. Descompón la rentabilidad de emisión y adquirencia por cada 100 000 de volumen.
2. Traza el ciclo de un contracargo con sus siete pasos y la evidencia de cada causal.
3. Dimensiona la exposición de tres comercios de rubros distintos.
4. Diseña los mitigantes de un comercio de alto riesgo y evalúa su suficiencia.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se evalúa al comercio por su saldo del día | Exposición por entrega diferida | Dimensiona por duración del servicio. |
| Se aplica retención estándar a todo rubro | Riesgo no diferenciado | Ajusta según el rubro y la duración. |
| Se ignora la tasa de contracargo | Indicador clave omitido | Monitorea con umbral y derecho a suspender. |
| Se afilia por volumen sin evaluar riesgo | La adquirencia es exposición crediticia | Evalúa al comercio como deudor. |
| Se supone que el contracargo lo pierde el comercio | Si quiebra, la pérdida es del adquirente | Exige garantías o fideicomiso. |
| Se compite solo por comisión | Margen ya estrecho | Compite por servicio y por gestión de riesgo. |

## ❓ Preguntas de comprobación

1. ¿Por qué la adquirencia es una exposición crediticia y no solo procesamiento?
2. ¿Cómo se reparte la comisión entre emisor, marca y adquirente?
3. ¿Cómo se dimensiona la exposición de un comercio de entrega diferida?
4. ¿Qué efecto tiene la autenticación reforzada sobre la responsabilidad?
5. ¿Por qué un fideicomiso de fondos cambia estructuralmente el riesgo?

## 📥 Entregable

Guarda en `portfolio/parte-10/clase-10/`:

- la descomposición de rentabilidad de emisión y adquirencia;
- el ciclo de contracargo con la evidencia decisiva por causal;
- la exposición dimensionada de tres comercios de rubros distintos;
- el diseño de mitigantes de un comercio de alto riesgo con su evaluación.

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

- Evans, D. y Schmalensee, R. (2005). *Paying with Plastic* (2.ª ed.). MIT Press. Economía de la emisión y la adquirencia.
- Rochet, J. y Tirole, J. (2006). "Two-Sided Markets: A Progress Report". *RAND Journal of Economics*.
- PCI Security Standards Council (2022). *PCI DSS v4.0*. Requisitos de seguridad para comercios y adquirentes. <https://www.pcisecuritystandards.org/>
- Committee on Payments and Market Infrastructures (2020). *Payment aspects of financial inclusion*. CPMI/Banco Mundial.
- European Banking Authority (2019). *Guidelines on Strong Customer Authentication*. Efecto de la autenticación reforzada sobre la responsabilidad.
- Verificación local: revisa las reglas de las marcas de tarjetas vigentes en tu mercado, los umbrales de tasa de contracargo y la normativa sobre retenciones a comercios.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 09 · Medios de pago](09-medios-de-pago.md) | [Parte 10](../README.md) · [Programa](../../../SYLLABUS.md) | [11 · Caja y sucursales →](11-caja-y-sucursales.md) |
<!-- gen:footer:end -->
