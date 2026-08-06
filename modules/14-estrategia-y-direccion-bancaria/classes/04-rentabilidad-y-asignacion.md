---
part: 15
class: 4
title: "Rentabilidad y asignación"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 04 · Rentabilidad y asignación

> [← 03 · Segmentos y propuesta de valor](03-segmentos-y-propuesta-de-valor.md) · [Índice de la parte](../README.md) · [05 · Planificación estratégica y de capital →](05-planificacion-estrategica-y-de-capital.md)

**Parte 15 — Estrategia y dirección bancaria** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Medir dónde gana y dónde pierde dinero un banco, con el nivel de detalle que permite decidir. Es el
sistema de información sobre el que descansan las decisiones de precio, de segmento y de inversión, y
sus errores de método producen decisiones equivocadas con apariencia de rigor.

## 📚 Objetivos

Al finalizar podrás:

1. **Construir** un sistema de rentabilidad por unidad, producto y cliente.
2. **Aplicar** el precio de transferencia interno correctamente.
3. **Asignar** costos con métodos que soporten decisiones.
4. **Distinguir** costo evitable de costo asignado en cada decisión.
5. **Interpretar** un informe de rentabilidad sin caer en sus trampas.

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
| `precio de transferencia interno` | Tasa a la que la tesorería compra y vende fondos internamente. |
| `margen de captación` | Diferencia entre el precio de transferencia y la tasa pagada. |
| `margen de colocación` | Diferencia entre la tasa cobrada y el precio de transferencia. |
| `costo directo` | Atribuible a la actividad sin criterio de reparto. |
| `costo indirecto` | Requiere un criterio de asignación. |
| `costeo por actividad` | Asigna costos según las actividades que cada producto consume. |
| `costo evitable` | El que desaparece si se elimina la actividad. |
| `contribución` | Ingreso menos costos evitables. |

## 🧠 Modelo mental

```text
UN SISTEMA DE RENTABILIDAD TIENE DOS USOS
Y EXIGEN CIFRAS DISTINTAS

  MEDIR EL DESEMPEÑO
    todos los costos asignados
    → responde: ¿esta unidad cubre su parte del total?

  DECIDIR
    solo costos evitables
    → responde: ¿qué cambia si dejo de hacerlo?

USAR LA PRIMERA PARA DECIDIR
ES EL ERROR MÁS FRECUENTE Y MÁS CARO
```

**El caso de la clase anterior lo mostró:** un segmento con resultado asignado negativo contribuía
positivamente. La cifra no estaba mal calculada; estaba mal usada.

## 📖 Desarrollo

### 1. Precio de transferencia interno

```text
SIN PRECIO DE TRANSFERENCIA, LA RENTABILIDAD NO SE PUEDE MEDIR

  el área que capta no sabe cuánto vale lo que capta
  el área que coloca no sabe cuánto cuesta lo que coloca
  y el riesgo de tasa queda repartido sin dueño

CON PRECIO DE TRANSFERENCIA
  captación: margen = precio de transferencia − tasa pagada
  colocación: margen = tasa cobrada − precio de transferencia
  tesorería: gestiona el descalce (Parte 10, clase 12)
```

```text
LA REGLA DE CONSTRUCCIÓN
  el precio de transferencia de cada operación
  corresponde a su PLAZO y su PERFIL DE REPRECIACIÓN

  un crédito a 5 años fijo se financia
  al precio de transferencia a 5 años
  aunque el banco lo financie con depósitos a 90 días

  → el descalce y su riesgo quedan en la tesorería,
    que es donde se gestionan
```

| Error de precio de transferencia | Consecuencia |
|---|---|
| Un solo precio para todos los plazos | El área de colocación gana con el descalce |
| Precio basado en el costo medio histórico | No refleja el costo marginal |
| Sin cargo por liquidez | Los productos ilíquidos parecen baratos |
| Sin precio para las líneas no usadas | El compromiso parece gratuito |

### 2. Asignación de costos

```text
TRES MÉTODOS, DE PEOR A MEJOR PARA DECIDIR

  1. REPARTO PROPORCIONAL
     todos los costos indirectos según un solo criterio
     (ingresos, activos, número de clientes)
     simple, y produce señales falsas

  2. REPARTO POR ETAPAS
     los centros de apoyo se reparten a los operativos
     y estos a los productos
     mejor, aún arbitrario en los criterios

  3. COSTEO POR ACTIVIDAD
     se identifican las actividades, su costo
     y cuánto consume cada producto
     más caro de construir, mucho mejor para decidir
```

```text
COSTEO POR ACTIVIDAD — CÓMO SE CONSTRUYE
  1. identifica las actividades (abrir cuenta, evaluar crédito,
     procesar pago, atender reclamo, cobrar)
  2. determina el costo total de cada actividad
  3. define el inductor: qué hace que la actividad ocurra
     (número de aperturas, de solicitudes, de transacciones)
  4. calcula el costo unitario por inductor
  5. asigna a cada producto según su consumo real
```

| Actividad | Inductor | Consumo típico |
|---|---|---|
| Apertura de cuenta | Número de aperturas | Alto en cuentas nuevas |
| Evaluación de crédito | Número de solicitudes | Alto en consumo |
| Procesamiento de pago | Número de transacciones | Alto en cuentas transaccionales |
| Atención de reclamo | Número de reclamos | Alto en productos complejos |
| Cobranza | Número de casos en mora | Alto en consumo |
| Cumplimiento | Número de clientes de alto riesgo | Alto en empresas |

### 3. Niveles de rentabilidad

```text
POR UNIDAD DE NEGOCIO
  para gestión de recursos y evaluación de la dirección
  requiere: precio de transferencia, asignación completa

POR PRODUCTO
  para decisiones de catálogo y de precio
  requiere: costeo por actividad

POR CLIENTE
  para decisiones comerciales y de servicio
  requiere: atribución de cada operación al cliente

POR OPERACIÓN
  para el precio de cada transacción
  requiere: el modelo de tasa mínima (Parte 11, clase 14)
```

```text
LA RENTABILIDAD POR CLIENTE ES LA MÁS ÚTIL
Y LA MÁS DIFÍCIL
  · un cliente usa varios productos
  · algunos productos comparten costos
  · la relación tiene valor más allá de sus operaciones
  · el valor futuro importa más que el actual
```

### 4. Costo evitable

```text
LA PREGUNTA QUE DEFINE UN COSTO EVITABLE
  si dejamos de hacer esto, ¿este costo desaparece?
  ¿en qué plazo?

  inmediato: variables directos (papel, procesamiento)
  medio (6-18 meses): personal dedicado, arriendos
  largo (2+ años): sistemas, estructura central
  nunca: costos regulatorios mínimos, dirección
```

| Decisión | Costos relevantes |
|---|---|
| Precio de una operación marginal | Solo variables directos |
| Continuar o discontinuar un producto | Evitables a 12-18 meses |
| Cerrar una unidad de negocio | Evitables a 24-36 meses |
| Evaluar el desempeño de una unidad | Todos los asignados |
| Fijar la tasa mínima de un crédito | Directos + capital + riesgo |

### 5. Trampas de interpretación

```text
· UN PRODUCTO CON RENTABILIDAD NEGATIVA
  puede ser la puerta de entrada de una relación rentable
  → mide la rentabilidad del CLIENTE, no solo del producto

· UN CLIENTE CON RENTABILIDAD NEGATIVA
  puede tener alto potencial o alto valor de vida
  → mide el valor esperado, no el resultado del año

· UNA UNIDAD CON MEJOR RENTABILIDAD
  puede tener mejores clientes asignados, no mejor gestión
  → compara a igual composición de cartera

· LA MEJORA DE RENTABILIDAD DE UNA UNIDAD
  puede venir de trasladar costos a otra
  → verifica que el total no cambió

· LA RENTABILIDAD SIN AJUSTE POR RIESGO
  premia al que toma más riesgo
  → usa siempre pérdida esperada y capital asignado
```

## 🧮 Ejemplo guiado

**Situación.** El comité evalúa el catálogo de productos de personas.

```text
INFORME DE RENTABILIDAD POR PRODUCTO (anual)

  producto            saldo/vol   ingreso   costo    resultado
  cuenta corriente     162 000      6 480    8 940     −2 460
  cuenta de ahorro      94 000      2 820    2 180        640
  depósito a plazo     286 000      3 432    1 140      2 292
  crédito de consumo   520 000     42 640   24 880     17 760
  hipotecario          890 000     26 700   12 460     14 240
  tarjeta de crédito   184 000     22 080   16 320      5 760
  seguros                 —         8 140    2 460      5 680
  TOTAL                             112 292  68 380     43 912
```

**Paso 1 — cuestiona la cuenta corriente.**

```text
RESULTADO: −2 460
la primera reacción: subir comisiones o cerrarla

ANTES DE DECIDIR, REVISA EL PRECIO DE TRANSFERENCIA

  la cuenta corriente tiene 162 000 de saldo
  a tasa 0 %
  ¿qué precio de transferencia se le aplicó?

  respuesta: el de 30 días, 5,8 %
  ingreso reconocido: 162 000 × 5,8 % = 9 396

  pero el informe muestra ingreso de 6 480
  → se aplicó un precio de transferencia de 4,0 %
```

**Paso 2 — determina el precio de transferencia correcto.**

```text
LA CUENTA CORRIENTE NO ES UN PASIVO A 30 DÍAS
  su vida media conductual (Parte 11, clase 5): 3,5 años
  el núcleo estable es el 78 % del saldo

  PRECIO DE TRANSFERENCIA CORRECTO
    núcleo estable (126 360) al precio de 3,5 años: 6,9 %
    parte volátil (35 640) al precio de 30 días: 5,8 %

  ingreso correcto:
    126 360 × 6,9 % + 35 640 × 5,8 % = 8 719 + 2 067 = 10 786

  frente a los 6 480 reconocidos
  DIFERENCIA: 4 306
```

**Paso 3 — recalcula.**

```text
CUENTA CORRIENTE CON PRECIO CORRECTO
  ingreso:   10 786
  costo:      8 940
  RESULTADO: +1 846   (era −2 460)

  el producto no perdía dinero:
  el sistema de rentabilidad lo estaba midiendo mal
```

**Paso 4 — verifica el efecto en el resto.**

```text
SI LA CAPTACIÓN RECIBE 4 306 MÁS,
¿QUIÉN LOS PAGA?

  la tesorería, que compra esos fondos
  → el resultado de la tesorería baja en 4 306
  → y el resultado TOTAL del banco no cambia

VERIFICACIÓN
  el precio de transferencia redistribuye resultado
  entre áreas; no crea ni destruye

  Y ESO ES EXACTAMENTE SU FUNCIÓN
  cada área ve el resultado que le corresponde
```

**Paso 5 — analiza el costo de la cuenta corriente.**

```text
COSTO DE 8 940 SOBRE 162 000 DE SALDO

  descomposición por costeo por actividad:
    procesamiento de transacciones: 4 820
      (68 M de transacciones × 0,000071)
    mantención de la cuenta:        1 640
    atención y reclamos:            1 280
    estructura asignada:            1 200

  COSTO EVITABLE si el producto se elimina: 7 740
  COSTO NO EVITABLE: 1 200
```

**Paso 6 — evalúa la rentabilidad del cliente, no del producto.**

```text
¿QUIÉNES TIENEN CUENTA CORRIENTE?

  clientes con solo cuenta corriente:      84 000
    resultado por cliente: −0,014
  clientes con cuenta corriente y crédito: 218 000
    resultado por cliente: +0,186
  clientes con cuenta corriente y 3+ productos: 96 000
    resultado por cliente: +0,412

LA CUENTA CORRIENTE ES LA PUERTA
  el 78 % de los clientes con crédito de consumo
  llegó primero por la cuenta corriente

VALOR DE LA PUERTA
  84 000 clientes de solo cuenta corriente
  tasa de conversión anual a un segundo producto: 8,4 %
  7 056 clientes al año × valor del segundo producto (0,186)
  = 1 312 anuales de valor generado por esa "puerta"
```

**Paso 7 — evalúa el crédito de consumo con ajuste por riesgo.**

```text
RESULTADO REPORTADO: 17 760 sobre 520 000

¿INCLUYE PÉRDIDA ESPERADA Y CAPITAL?
  el costo de 24 880 incluye:
    provisiones del año:        19 760   (3,8 %)
    costo operativo:             5 120
  NO incluye el costo del capital

  capital asignado: 520 000 × 11,4 % = 59 280
  costo del capital: 59 280 × 14 % = 8 299

  RESULTADO AJUSTADO: 17 760 − 8 299 = 9 461
  RAROC: 17 760 / 59 280 = 30,0 %  → sobre el costo de capital ✓
```

```text
Y UNA VERIFICACIÓN MÁS
  ¿las provisiones del año son la PÉRDIDA ESPERADA
  o la observada?

  observada: 19 760 (3,8 %)
  esperada según modelo: 22 360 (4,3 %)

  el producto está reconociendo menos pérdida
  de la que su riesgo implica
  → resultado ajustado real: 17 760 − 2 600 − 8 299 = 6 861
  → RAROC: 25,6 %  → sigue sobre el costo de capital
```

**Paso 8 — construye la decisión.**

```text
CORRECCIONES AL SISTEMA
  1. precio de transferencia por plazo conductual,
     no contractual → corrige la cuenta corriente
     y todos los productos de captación
  2. usar pérdida ESPERADA, no observada,
     en la rentabilidad de los productos de crédito
  3. incluir el costo del capital en todos los productos
  4. separar en el informe: costo evitable y costo asignado
  5. añadir una vista de rentabilidad por CLIENTE
     con el valor de la relación completa

DECISIONES DE NEGOCIO QUE CAMBIAN
  · la cuenta corriente NO se elimina ni se encarece:
    es rentable y es la puerta de la relación
  · el crédito de consumo rinde 25,6 % de RAROC,
    no el 30,0 % reportado: sigue siendo el mejor producto
    y con menos holgura de la que se creía
  · los 84 000 clientes de solo cuenta corriente
    son el objetivo del plan de profundización:
    generan 1 312 anuales de valor futuro
```

**Interpreta:** el producto que aparecía perdiendo 2 460 al año **ganaba 1 846**, y la diferencia era
enteramente un precio de transferencia mal construido. Una decisión de encarecer o eliminar la cuenta
corriente habría destruido la puerta de entrada del 78 % de los clientes de crédito. El sistema de
rentabilidad no es un sistema contable: **es el sistema que determina qué decisiones parecen razonables**,
y sus errores de método no se corrigen con juicio comercial.

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Mi cuenta corriente no me da interés» | Su valor está en el saldo estable | 15, clase 4 |
| «Subieron la comisión de mantención» | Producto mal medido | 15, clase 4 |
| «El banco me ofrece otro producto» | Valor de la profundización | 13, clase 14 |
| «Mi crédito tiene una tasa alta» | Costo del capital y pérdida esperada | 11, clase 14 |
| «Cerraron un producto que usaba» | Decisión con costo asignado | 15, clase 4 |

## 🧪 Práctica

En `labs/lab-02.md`, sección de rentabilidad:

1. Construye el precio de transferencia por plazo para cinco productos.
2. Asigna costos con costeo por actividad y compáralo con reparto proporcional.
3. Calcula la rentabilidad por producto, por cliente y ajustada por riesgo.
4. Separa costo evitable de asignado y evalúa una decisión de discontinuar.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Un producto de captación pierde dinero | Precio de transferencia mal construido | Usa el plazo conductual. |
| Se decide con el costo totalmente asignado | Mide desempeño, no decisión | Usa costo evitable. |
| Se usa la pérdida observada | Subestima el riesgo del producto | Usa la esperada. |
| No se incluye el costo del capital | Todo parece rentable | Inclúyelo siempre. |
| Se evalúa el producto y no el cliente | Se pierde la puerta de entrada | Añade la vista de cliente. |
| Reparto proporcional único | Señales falsas | Costeo por actividad. |

## ❓ Preguntas de comprobación

1. ¿Por qué medir el desempeño y decidir exigen cifras distintas?
2. ¿Por qué el precio de transferencia de un crédito a 5 años debe ser a 5 años?
3. ¿Qué redistribuye y qué no crea el precio de transferencia?
4. ¿Por qué un producto con rentabilidad negativa puede no deber eliminarse?
5. ¿Qué diferencia hay entre la pérdida observada y la esperada al medir rentabilidad?

## 📥 Entregable

Guarda en `portfolio/parte-15/clase-04/`:

- el precio de transferencia construido por plazo para cinco productos;
- la comparación entre costeo por actividad y reparto proporcional;
- las tres vistas de rentabilidad con ajuste por riesgo;
- la evaluación de una decisión de discontinuar con costo evitable.

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

- Kaplan, R. y Anderson, S. (2007). *Time-Driven Activity-Based Costing*. Harvard Business School Press.
- Grant, J. (2011). "Liquidity transfer pricing: a guide to better practice". *BIS Occasional Paper 10*. <https://www.bis.org/fsi/fsipapers10.htm>
- Basel Committee on Banking Supervision (2016). *Interest rate risk in the banking book*. BIS. Precio de transferencia y descalce.
- Rose, P. y Hudgins, S. (2013). *Bank Management and Financial Services* (9.ª ed.). McGraw-Hill.
- Matten, C. (2000). *Managing Bank Capital* (2.ª ed.). Wiley.
- Verificación local: revisa cómo construye tu institución su precio de transferencia interno y si distingue plazo contractual de conductual.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 03 · Segmentos y propuesta de valor](03-segmentos-y-propuesta-de-valor.md) | [Parte 15](../README.md) · [Programa](../../../SYLLABUS.md) | [05 · Planificación estratégica y de capital →](05-planificacion-estrategica-y-de-capital.md) |
<!-- gen:footer:end -->
