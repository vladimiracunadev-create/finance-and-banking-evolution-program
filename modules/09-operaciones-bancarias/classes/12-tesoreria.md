---
part: 10
class: 12
title: "Tesorería"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 12 · Tesorería

> [← 11 · Caja y sucursales](11-caja-y-sucursales.md) · [Índice de la parte](../README.md) · [13 · Operaciones internacionales →](13-operaciones-internacionales.md)

**Parte 10 — Operaciones bancarias** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Gestionar la liquidez, el calce y las posiciones de mercado de un banco. La tesorería es el área que
conecta el balance con los mercados financieros, y su gestión determina si el banco puede cumplir sus
obligaciones cada día y si su margen resiste los movimientos de tasas.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** las funciones de la tesorería y sus libros.
2. **Gestionar** la posición de liquidez diaria e intradía.
3. **Aplicar** el precio de transferencia interno.
4. **Medir** y gestionar el calce de plazos y de tasas.
5. **Aplicar** los controles y límites de una mesa de operaciones.

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

| Concepto | Comprensión verificable |
|---|---|
| `libro de banca` | Posiciones mantenidas hasta el vencimiento: colocaciones y captaciones. |
| `libro de negociación` | Posiciones tomadas para obtener beneficio de corto plazo. Se valoran a mercado. |
| `precio de transferencia interno` | Tasa a la que la tesorería compra fondos a las áreas captadoras y los vende a las colocadoras. |
| `calce` | Correspondencia entre plazos, tasas y monedas de activos y pasivos. |
| `posición de liquidez` | Disponibilidad de fondos para cumplir obligaciones en cada horizonte. |
| `límite de riesgo` | Restricción cuantitativa a una posición. Se aprueba en el comité. |
| `activos líquidos de alta calidad` | Activos convertibles en efectivo sin pérdida significativa en estrés. |

## 🧠 Modelo mental

La tesorería cumple **dos funciones que conviene no confundir**:

```text
FUNCIÓN DE BALANCE      gestionar liquidez, calce y precio de transferencia
                        objetivo: que el banco funcione y su margen sea estable

FUNCIÓN DE NEGOCIACIÓN  tomar posiciones para obtener resultado
                        objetivo: generar ingreso, dentro de límites
```

Confundirlas produce el error clásico: **usar la gestión de liquidez como excusa para tomar posiciones
especulativas**. Por eso ambas funciones se separan en libros distintos, con límites y medición
distintos.

## 📖 Desarrollo

### 1. Los dos libros

| | Libro de banca | Libro de negociación |
|---|---|---|
| Intención | Mantener | Negociar |
| Valoración | Costo amortizado | Valor razonable |
| Efecto de cambios de tasa | En el margen y en el valor económico | En el resultado, de inmediato |
| Requerimiento de capital | Riesgo de crédito | Riesgo de mercado |
| Límites | De calce y de duración | De posición, de pérdida, de sensibilidad |

**La clasificación no es discrecional:** una vez asignado un instrumento a un libro, moverlo requiere
justificación y suele estar restringido. Esa restricción evita el arbitraje contable.

### 2. Gestión de liquidez

```text
HORIZONTES DE GESTIÓN
  intradía        cumplir pagos durante el día (Parte 10, clase 7)
  corto plazo     1 a 30 días
  estructural     más de 30 días, calce de plazos
```

**Escalera de vencimientos:**

```text
tramo          activos    pasivos    brecha    brecha acumulada
1–7 días        18 400     24 600    −6 200      −6 200
8–30 días       22 100     31 800    −9 700     −15 900
31–90 días      41 600     48 200    −6 600     −22 500
91–180 días     38 900     29 400    +9 500     −13 000
181–365 días    62 300     41 700   +20 600      +7 600
1–3 años       184 000     96 000   +88 000     +95 600
> 3 años       412 000    108 000  +304 000    +399 600
```

**La brecha negativa en los tramos cortos es normal y esperada:** es la transformación de plazos, el
negocio bancario. Lo que se gestiona es su magnitud y su cobertura con activos líquidos.

```text
brecha acumulada a 30 días: −15 900
activos líquidos de alta calidad: 28 400
cobertura: 1,79 veces  ✓
```

### 3. Precio de transferencia interno

```text
la tesorería COMPRA los fondos a las áreas que captan
y los VENDE a las áreas que colocan

precio de transferencia = tasa de mercado del plazo correspondiente
```

```text
EJEMPLO
  el área de personas capta un depósito a 90 días al 5,80 %
  la tesorería se lo compra a la tasa de mercado a 90 días: 6,10 %
  → el área de captación gana 0,30 puntos

  el área de consumo coloca un crédito a 36 meses al 21,4 %
  la tesorería le vende los fondos a la tasa de mercado a 36 meses: 6,90 %
  → el área de colocación gana 14,50 puntos brutos

  la tesorería queda con el descalce: compró a 90 días y vendió a 36 meses
  su resultado es la gestión de ese descalce
```

**Por qué importa:**

```text
· cada área conoce su margen real, sin depender de lo que hagan las otras
· el riesgo de tasa queda concentrado en la tesorería, donde se gestiona
· las decisiones de precio de cada producto se toman con el costo correcto
· sin precio de transferencia, un área puede parecer rentable porque otra
  le entrega fondos baratos
```

### 4. Calce y su gestión

```text
CALCE DE PLAZOS      correspondencia entre vencimientos
CALCE DE TASAS       correspondencia entre fechas de repreciación
CALCE DE MONEDAS     correspondencia entre monedas de activos y pasivos
```

Los tres se miden por separado porque **un balance puede estar calzado en plazo y descalzado en
tasa**: un crédito a 5 años a tasa variable repacta cada 90 días, aunque venza en 5 años.

**Instrumentos de gestión:**

| Necesidad | Instrumento |
|---|---|
| Alargar el plazo del pasivo | Emisión de bonos |
| Acortar la duración del activo | Venta de cartera, titularización |
| Cubrir riesgo de tasa | Swap de tasa de interés |
| Cubrir riesgo de moneda | Forward o swap de moneda |
| Obtener liquidez sin vender | Operaciones de venta con pacto de retrocompra |
| Colocar excedentes | Depósitos interbancarios, instrumentos de corto plazo |

### 5. Controles y límites de la mesa

```text
LÍMITES DE POSICIÓN
  · posición máxima por instrumento, moneda y plazo
  · posición neta máxima del libro de negociación
  · concentración por emisor y por contraparte

LÍMITES DE RIESGO
  · valor en riesgo diario
  · sensibilidad a movimientos de tasa (por punto base)
  · pérdida máxima diaria y acumulada (stop loss)

CONTROLES DE PROCESO
  · confirmación independiente de toda operación
  · valoración por un área distinta de la mesa
  · conciliación diaria de posiciones
  · grabación de las comunicaciones de la mesa
  · vacaciones obligatorias continuas
  · prohibición de operar por cuenta propia
```

**El control de valoración independiente es el más importante.** Los casos documentados de pérdidas
grandes en mesas de operaciones tienen un elemento común: **el operador podía influir en la valoración
de sus propias posiciones**.

## 🧮 Ejemplo guiado

**Situación.** El comité de activos y pasivos revisa la posición de la tesorería.

```text
POSICIÓN DE LIQUIDEZ
  activos líquidos de alta calidad         28 400
  salidas netas estimadas a 30 días        21 600
  ratio de cobertura de liquidez           131,5 %   (mínimo 100 %)

CALCE DE TASAS (brecha de repreciación)
  tramo             activos    pasivos    brecha
  0–30 días          64 200    142 800   −78 600
  31–90 días         88 400     96 200    −7 800
  91–180 days        72 100     48 400   +23 700
  181–365 días       94 600     31 200   +63 400
  > 365 días        460 000     84 000  +376 000

LIBRO DE NEGOCIACIÓN
  posición neta                             8 400
  valor en riesgo diario (99 %, 1 día)        142
  límite de valor en riesgo                   180
  pérdida acumulada del mes                    −68
  límite de pérdida mensual                   −250
```

**Paso 1 — evalúa la liquidez.**

```text
ratio de 131,5 % supera el mínimo
pero conviene verificar la composición de los activos líquidos:
  efectivo y reservas             6 200   (22 %)
  bonos soberanos                18 900   (67 %)
  otros activos elegibles         3 300   (11 %)

concentración en bonos soberanos: 67 %
→ vínculo soberano-bancario (Parte 6, clase 9)
→ en un escenario de estrés soberano, esos activos pierden valor
   justo cuando se necesitan
```

**Paso 2 — evalúa el calce de tasas.**

```text
brecha a 30 días: −78 600
significa que 78 600 más de pasivos que de activos repactan en 30 días

efecto de un alza de 100 pb:
  Δ margen a 30 días ≈ −78 600 × 0,01 × (30/365) = −64,6
  Δ margen a 12 meses ≈ ?
```

```text
brecha acumulada a 12 meses:
  −78 600 − 7 800 + 23 700 + 63 400 = +700

a 12 meses el balance está prácticamente calzado
el descalce está concentrado en el tramo corto
```

**Paso 3 — interpreta el descalce de corto plazo.**

```text
un descalce negativo en el tramo corto significa:
  · si las tasas SUBEN: el margen se comprime en el corto plazo
  · si las tasas BAJAN: el margen se expande

el banco está posicionado para un escenario de tasas a la baja
```

**Paso 4 — contrasta con la expectativa de mercado.**

```text
curva de tasas actual: ascendente
tasas forward implícitas: alza de 120 pb en 12 meses

el banco está posicionado CONTRA la expectativa del mercado
```

Eso no es necesariamente incorrecto, y **debe ser una decisión consciente y autorizada**, no el
resultado accidental de la estructura del balance.

**Paso 5 — cuantifica el efecto del escenario de mercado.**

```text
si las tasas suben 120 pb según lo implícito:

efecto en el margen a 12 meses:
  tramo 0–30 días:    −78 600 × 0,012 × (335/365) = −865
  tramo 31–90 días:    −7 800 × 0,012 × (290/365) =  −74
  tramo 91–180 días:  +23 700 × 0,012 × (215/365) = +167
  tramo 181–365 días: +63 400 × 0,012 × (90/365)  = +188
  EFECTO TOTAL EN EL MARGEN                        −584

efecto en el valor económico del patrimonio:
  duración del activo 3,4 · duración del pasivo 1,1 · pasivos/activos 0,92
  brecha de duración = 3,4 − 1,1 × 0,92 = 2,388
  Δ valor ≈ −2,388 % × 1,2 × 780 000 = −22 353
```

**El efecto en el valor económico es 38 veces el efecto en el margen.**

**Paso 6 — evalúa el libro de negociación.**

```text
valor en riesgo 142 sobre límite de 180: 79 % de utilización
pérdida acumulada del mes −68 sobre límite de −250: 27 %

ambos dentro de límites

verificación adicional:
  · ¿cuántos días el valor en riesgo superó el 90 % del límite? → 4 de 20
  · ¿hubo excesos? → ninguno
  · ¿la valoración la realiza un área independiente? → sí
  · ¿hay operaciones con valoración modelada sin precio observable? → 12 % de la cartera
```

**El 12 % de la cartera valorada por modelo** merece atención: es donde la valoración depende de
supuestos, y es el punto donde históricamente se han ocultado pérdidas.

**Paso 7 — decisiones del comité.**

```text
1. LIQUIDEZ
   reducir la concentración en bonos soberanos de 67 % a 55 % en 6 meses
   sustituir por activos elegibles de otros emisores

2. CALCE DE TASAS
   la posición está contra la expectativa de mercado y NO fue una decisión explícita
   · alternativa A: cerrar la brecha corta con swaps (costo estimado 180)
   · alternativa B: mantener la posición como decisión consciente, con límite
     y con reporte mensual del efecto
   · DECISIÓN: cerrar el 60 % de la brecha con swaps y mantener el resto
     como posición autorizada, con límite de brecha de −35 000

3. VALOR ECONÓMICO
   incorporar el efecto sobre el valor económico del patrimonio al reporte mensual
   el margen por sí solo oculta la exposición real

4. LIBRO DE NEGOCIACIÓN
   revisión independiente de la valoración del 12 % de cartera modelada
   con verificación de los supuestos por el área de riesgo

5. GOBIERNO
   el descalce de tasas debe ser una decisión del comité, no un residuo
   del balance. Establecer límite de brecha por tramo y reportar su utilización.
```

**Interpreta:** el banco cumplía todos sus límites y **tenía una posición direccional de tasas que
nadie había decidido**. El efecto sobre el valor económico —22 353— era 38 veces el efecto sobre el
margen, y no estaba en el reporte mensual. Convertir un residuo del balance en una decisión explícita
con límite es el aporte del análisis.

## 🏦 Del cliente al banco

| Vista del cliente | Vista de la tesorería | Parte |
|---|---|---|
| Tasa de su depósito | Precio de transferencia menos margen del área | 10, clase 2 |
| Tasa de su crédito | Precio de transferencia más riesgo, costos y margen | 15, clase 7 |
| Producto de cobertura ofrecido | La tesorería es la contraparte | 11, clase 6 |
| Banco que no puede pagar | Falla de gestión de liquidez | 11, clase 4 |
| Cambio de tasas del mercado | Efecto en margen y en valor económico | 11, clase 5 |

## 🧪 Práctica

En `labs/lab-06.md`, sección de tesorería:

1. Construye la escalera de vencimientos de un balance y calcula sus brechas.
2. Aplica el precio de transferencia interno a tres productos y calcula el margen por área.
3. Calcula el efecto de un alza de tasas sobre el margen y sobre el valor económico.
4. Diseña el conjunto de límites de una mesa de operaciones.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se mezclan libro de banca y de negociación | Sin clasificación clara | Asigna y restringe los traspasos. |
| Se mide solo el efecto en el margen | Valor económico omitido | Mide ambos; suelen diferir mucho. |
| El descalce es un residuo del balance | Sin decisión explícita | Establece límites por tramo. |
| El operador influye en la valoración | Sin independencia | Valoración por área distinta. |
| Sin precio de transferencia | Márgenes por área distorsionados | Implanta el precio de transferencia. |
| Concentración de activos líquidos en un emisor | Vínculo soberano-bancario | Diversifica los activos líquidos. |

## ❓ Preguntas de comprobación

1. ¿Qué distingue el libro de banca del de negociación y por qué importa la clasificación?
2. ¿Para qué sirve el precio de transferencia interno?
3. ¿Por qué un balance puede estar calzado en plazo y descalzado en tasa?
4. ¿Por qué el efecto de un alza de tasas sobre el valor económico puede superar al del margen?
5. ¿Cuál es el control más importante de una mesa de operaciones?

## 📥 Entregable

Guarda en `portfolio/parte-10/clase-12/`:

- la escalera de vencimientos con sus brechas por tramo;
- el precio de transferencia aplicado a tres productos con el margen por área;
- el efecto de un alza de tasas sobre margen y valor económico;
- el conjunto de límites diseñado para una mesa, con su fundamento.

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

- Saunders, A. y Cornett, M. (2021). *Financial Institutions Management* (10.ª ed.). McGraw-Hill. Capítulos 8, 9 y 17: gestión de activos y pasivos y de liquidez.
- Basel Committee on Banking Supervision (2016). *Interest rate risk in the banking book*. BIS. Medición de margen y valor económico. <https://www.bis.org/bcbs/publ/d368.htm>
- Basel Committee on Banking Supervision (2013). *Basel III: The Liquidity Coverage Ratio*. BIS.
- Basel Committee on Banking Supervision (2008). *Principles for Sound Liquidity Risk Management and Supervision*. BIS. <https://www.bis.org/publ/bcbs144.htm>
- Grant, J. (2011). "Liquidity transfer pricing: a guide to better practice". *BIS Occasional Paper 10*.
- Verificación local: revisa los requerimientos de liquidez y de riesgo de tasa del libro de banca que aplica tu supervisor.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 11 · Caja y sucursales](11-caja-y-sucursales.md) | [Parte 10](../README.md) · [Programa](../../../SYLLABUS.md) | [13 · Operaciones internacionales →](13-operaciones-internacionales.md) |
<!-- gen:footer:end -->
