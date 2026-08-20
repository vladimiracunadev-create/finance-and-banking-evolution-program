<!-- meta
part: 10
class: 13
title: "Operaciones internacionales"
level: profesional
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 13 · Operaciones internacionales

> [← 12 · Tesorería](12-tesoreria.md) · [Índice de la parte](../README.md) · [14 · Comercio exterior →](14-comercio-exterior.md)

**Parte 10 — Operaciones bancarias** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Ejecutar y controlar las operaciones que cruzan una frontera: transferencias al exterior, remesas,
cuentas en moneda extranjera y compraventa de divisas. Un pago internacional no es un pago local en
otra moneda: involucra bancos que no se conocen, dos sistemas de pago distintos, dos regímenes
normativos y un tipo de cambio que se fija en algún momento del recorrido.

Las clases anteriores operan dentro de un país. Esta cruza la frontera, y con eso aparece una limitación estructural: no existe un sistema de pagos global, y por eso un pago internacional se resuelve con cuentas entre bancos. Esta clase explica ese mecanismo, que la Parte 18 desarrolla entero.

## 📚 Objetivos

Al finalizar podrás:

1. **Explicar** la red de corresponsalía y por qué existe.
2. **Trazar** el recorrido de una transferencia internacional y sus actores.
3. **Descomponer** el costo total de un envío entre comisión y margen cambiario.
4. **Aplicar** los controles de cumplimiento propios de las operaciones transfronterizas.
5. **Gestionar** la posición de cambios de una mesa de divisas.

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

Los cuatro primeros términos son la red de corresponsalía y sus cuentas; los cuatro siguientes, el margen, la posición y el fenómeno que está reduciendo la red. La distinción entre **nostro y vostro** es la que hay que fijar: es la misma cuenta vista desde los dos lados, y confundirlas descuadra cualquier conciliación internacional.

| Concepto | Comprensión verificable |
|---|---|
| `banco corresponsal` | Banco que mantiene una cuenta para otro banco en su propia plaza y moneda. |
| `cuenta nostro` | «Nuestra cuenta en su banco». La que el banco local tiene en el corresponsal. |
| `cuenta vostro` | «Su cuenta en nuestro banco». La imagen espejo de la anterior. |
| `mensaje de pago` | Instrucción estandarizada que viaja entre bancos; no mueve dinero por sí sola. |
| `banco intermediario` | Tercer banco que aparece cuando origen y destino no tienen relación directa. |
| `margen cambiario` | Diferencia entre el tipo de cambio aplicado al cliente y el de mercado. |
| `posición de cambios` | Exposición neta del banco en cada moneda extranjera. |
| `de-risking` | Cierre de relaciones de corresponsalía por costo de cumplimiento. |

## 🧠 Modelo mental

**El dinero no cruza la frontera. Cruzan las instrucciones.**

```text
un dólar que "va" de Santiago a Madrid
nunca sale de Nueva York

lo que ocurre es:
  el banco chileno reduce su saldo en su cuenta nostro en Nueva York
  el banco español aumenta el suyo
  ambos ajustan las cuentas de sus clientes

el dólar sigue estando en Estados Unidos, donde se liquida esa moneda
```

De ahí se deduce todo lo demás: por qué hacen falta corresponsales, por qué aparecen intermediarios
que cobran, por qué hay horarios de corte, y por qué el cumplimiento normativo del país de la moneda
alcanza a operaciones entre dos terceros países.

## 📖 Desarrollo

### 1. La red de corresponsalía

La corresponsalía es la infraestructura que sustituye a un sistema de pagos global que no existe. El esquema la describe.

```text
un banco no puede tener cuenta en el banco central de todos los países
tampoco puede tener relación bilateral con los ~25 000 bancos del mundo

SOLUCIÓN: red jerárquica
  bancos locales  →  bancos regionales  →  bancos globales  →  banco central
                                             de cada moneda
```

| Elemento | Qué es | Riesgo asociado |
|---|---|---|
| Relación directa | Banco A tiene cuenta en Banco B | Contraparte y liquidez |
| Cadena con intermediarios | A → C → B | Costo, demora, trazabilidad |
| Cuenta nostro | Activo del banco en el exterior | Liquidez en moneda extranjera |
| Cuenta vostro | Pasivo con un banco extranjero | Cumplimiento por cuenta ajena |

**El fenómeno del *de-risking*.** Desde la década de 2010, los bancos globales han cerrado relaciones
de corresponsalía con bancos de jurisdicciones percibidas como de alto riesgo. El efecto documentado
por el FSB y el Banco Mundial es una reducción de la conectividad de economías pequeñas, con encarecimiento
de las remesas. Es un caso donde **el cumplimiento correctamente aplicado en un banco produce exclusión
financiera en otro país**: la clase 3 de la Parte 12 vuelve sobre este dilema.

### 2. Recorrido de una transferencia

Un pago internacional puede pasar por varios bancos, y cada uno cobra y demora. El esquema recorre el trayecto.

```text
ORDENANTE                                              BENEFICIARIO
   │                                                        ▲
   │ 1. instrucción con datos completos                     │ 8. abono
   ▼                                                        │
BANCO ORIGEN ──2. control de cumplimiento──┐                │
   │                                       │            BANCO DESTINO
   │ 3. debita cuenta del cliente          │                ▲
   │ 4. mensaje de pago ───────────────────┴──────5. ───────┘
   ▼                                                        
CORRESPONSAL ORIGEN ──6. liquidación en la plaza de la moneda──▶ CORRESPONSAL DESTINO
                              7. confirmación
```

**Datos que deben viajar completos** (regla del «viaje» de la información, GAFI Recomendación 16):

```text
del ordenante:     nombre, número de cuenta, dirección o identificador
del beneficiario:  nombre, número de cuenta
del pago:          monto, moneda, concepto
```

Un mensaje incompleto se retiene, se investiga o se devuelve. Cada retención cuesta días y comisiones.

### 3. Estructura del costo

El cliente ve un solo número. Dentro hay al menos cuatro:

```text
1. COMISIÓN DE ENVÍO         explícita, del banco origen
2. COMISIÓN DE INTERMEDIARIOS descontada del monto en tránsito
3. COMISIÓN DE ABONO         del banco destino
4. MARGEN CAMBIARIO          implícito, casi nunca declarado
```

| Modalidad de gastos | Quién paga | Qué recibe el beneficiario |
|---|---|---|
| Compartidos | Origen paga las suyas; el resto se descuenta | Monto incierto |
| Por cuenta del ordenante | El ordenante paga todo | Monto íntegro |
| Por cuenta del beneficiario | El beneficiario paga todo | Monto menos todas las comisiones |

**El margen cambiario suele superar a todas las comisiones juntas.** Un margen de 2,5 % sobre USD 1 000
son USD 25; la comisión declarada puede ser USD 12. La clase 6 de la Parte 4 desarrolla por qué la
comparación honesta se hace sobre el monto que efectivamente recibe el destinatario.

### 4. Posición de cambios

La posición de cambios es la exposición neta del banco en cada moneda, y se controla con límites. El procedimiento siguiente la calcula.

```text
POSICIÓN LARGA en una moneda   activos > pasivos en esa moneda
                                gana si la moneda se aprecia

POSICIÓN CORTA                  pasivos > activos
                                gana si la moneda se deprecia

POSICIÓN CALZADA                activos = pasivos
                                resultado independiente del tipo de cambio
```

Los bancos operan con **límites de posición por moneda y de posición global**, porque el riesgo de
cambio no es su negocio: su negocio es la intermediación y el servicio. Un banco que gana dinero
adivinando el tipo de cambio está tomando un riesgo que sus depositantes no eligieron.

### 5. Controles específicos

Las operaciones internacionales tienen controles adicionales de sanciones y de origen de fondos. La tabla los recoge.

| Control | Qué previene |
|---|---|
| Listas de sanciones sobre ambas partes y bancos de la cadena | Financiamiento prohibido |
| Verificación de país de origen y destino | Jurisdicciones de alto riesgo |
| Coherencia del concepto con el perfil del cliente | Estructuración y lavado |
| Límite de posición por moneda | Riesgo de cambio |
| Conciliación diaria de cuentas nostro | Pérdida por partidas no aplicadas |
| Corte horario por moneda | Riesgo de liquidación |

## 🧮 Ejemplo guiado

El ejemplo sigue un pago internacional por la cadena de corresponsales. Conviene sumar las comisiones de cada tramo: la diferencia con lo cotizado explica la mayoría de los reclamos.

**Situación.** Una clienta envía dinero a su hija en el exterior. Compara dos opciones.

```text
MONTO A ENVIAR: equivalente a 1 000 unidades de moneda extranjera
TIPO DE CAMBIO DE MERCADO (medio): 950 moneda local por unidad extranjera

OPCIÓN A — Banco
  comisión de envío        18 000 moneda local
  tipo de cambio aplicado  974 (venta)
  gastos                   compartidos
  intermediarios estimados 1, cobra 15 unidades extranjeras

OPCIÓN B — Empresa de remesas
  comisión de envío        6 500 moneda local
  tipo de cambio aplicado  988
  gastos                   por cuenta del ordenante
  intermediarios           ninguno declarado
```

**Paso 1 — costo total de la Opción A.**

```text
costo de las 1 000 unidades:  1 000 × 974 = 974 000
comisión de envío:                            18 000
COSTO PARA LA ORDENANTE:                     992 000

lo que llega:
  1 000 − 15 (intermediario) = 985 unidades
```

**Paso 2 — costo total de la Opción B.**

```text
costo de las 1 000 unidades:  1 000 × 988 = 988 000
comisión de envío:                             6 500
COSTO PARA LA ORDENANTE:                     994 500

lo que llega: 1 000 unidades íntegras
```

**Paso 3 — compara por la única medida honesta: costo por unidad recibida.**

```text
OPCIÓN A:  992 000 / 985 unidades  = 1 007,1 por unidad recibida
OPCIÓN B:  994 500 / 1 000 unidades =  994,5 por unidad recibida

DIFERENCIA A FAVOR DE B: 12,6 por unidad → 12 600 en total
```

**Paso 4 — descompón el costo real de cada una.**

```text
                          OPCIÓN A          OPCIÓN B
margen cambiario     (974−950)×1 000     (988−950)×1 000
                      = 24 000            = 38 000
comisión explícita     18 000               6 500
costo de intermediario 15 × 950 = 14 250        0
COSTO TOTAL SOBRE MERCADO  56 250            44 500
```

**Paso 5 — interpreta.**

```text
la opción con la comisión declarada MÁS BARATA (B: 6 500)
tiene el margen cambiario MÁS CARO (38 000)

y aun así resulta mejor, porque A suma un intermediario
que la clienta no podía prever al comparar
```

**Paso 6 — desde el banco: por qué existe cada componente.**

```text
comisión de envío     cubre proceso, cumplimiento y mensajería
margen cambiario      cubre el riesgo de posición entre la operación y su cierre
                      + el margen de intermediación de la mesa
intermediario         cobra por prestar su relación de corresponsalía
```

**Paso 7 — la decisión de gestión.**

```text
si el banco quiere competir en remesas debe:
  · declarar el tipo de cambio aplicado ANTES de la operación
  · ofrecer gastos por cuenta del ordenante como opción visible
  · publicar el monto que recibirá el beneficiario, no solo el enviado
  · reducir la cadena de intermediarios en los corredores de mayor volumen
```

**Interpreta:** el precio de una remesa no está en la comisión, sino en el **monto que llega**. Un banco
que solo compite bajando la comisión declarada y compensa con margen cambiario está compitiendo por
apariencia. El indicador que el G20 y el Banco Mundial usan para medir el costo de las remesas es
precisamente el costo total sobre el monto enviado, por esta razón.

## 🏦 Del cliente al banco

El cliente envía dinero al extranjero y el banco mueve saldos en cuentas de corresponsalía. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Llegó menos de lo que envié» | Comisión de intermediario y modalidad de gastos | 10, clase 13 |
| «El tipo de cambio es peor que el de internet» | Margen cambiario de la mesa | 10, clase 12 |
| «Me pidieron explicar el envío» | Control de cumplimiento y perfil transaccional | 12, clase 3 |
| «Mi banco ya no envía a ese país» | De-risking de corresponsalía | 12, clase 4 |
| «Demoró tres días» | Cadena de corresponsales y cortes horarios | 10, clase 7 |

## 🧪 Práctica

El laboratorio pide reconstruir el costo total de un pago internacional y calcular la posición de cambios. El costo total supera lo cotizado, y localizar dónde se pierde es el objetivo.

En `labs/lab-06.md`, sección de operaciones internacionales:

1. Traza el recorrido completo de una transferencia con dos intermediarios.
2. Compara tres proveedores de remesas por costo total sobre el monto recibido.
3. Calcula la posición de cambios de un banco a partir de su balance por moneda.
4. Diseña la lista de controles de cumplimiento aplicables a un corredor de alto riesgo.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen pagos internacionales con costos o demoras inesperadas. Las causas están en los bancos intermediarios y en los controles de sanciones.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se compara solo la comisión declarada | Margen cambiario ignorado | Compara por monto recibido. |
| El beneficiario recibe menos de lo prometido | Modalidad de gastos compartidos | Declara la modalidad y su efecto. |
| El pago se retiene días | Datos incompletos del beneficiario | Valida los campos antes de enviar. |
| Descalce en cuentas nostro | Sin conciliación diaria | Concilia cada moneda cada día. |
| El banco gana con el tipo de cambio y lo llama servicio | Margen no declarado | Publica el tipo de cambio aplicado. |
| Se asume que el dinero «viaja» | Modelo mental incorrecto | La liquidación ocurre en la plaza de la moneda. |

## ❓ Preguntas de comprobación

1. ¿Por qué un pago en dólares entre dos países terceros se liquida en Estados Unidos?
2. ¿Qué diferencia una cuenta nostro de una vostro?
3. ¿Por qué el margen cambiario suele superar a la comisión declarada?
4. ¿Qué efecto tiene el *de-risking* sobre las economías pequeñas?
5. ¿Por qué un banco limita su posición de cambios en lugar de maximizarla?

## 📥 Entregable

Guarda en `portfolio/parte-10/clase-13/`:

- el recorrido trazado de una transferencia con sus actores y puntos de costo;
- la comparación de tres proveedores por costo sobre monto recibido;
- el cálculo de una posición de cambios con su interpretación;
- la lista de controles de cumplimiento con su justificación.

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

- Committee on Payments and Market Infrastructures (2016). *Correspondent banking*. BIS. Estructura de la banca corresponsal y su retroceso. <https://www.bis.org/cpmi/publ/d147.htm>
- Financial Stability Board (2018). *Stocktake of remittance service providers' access to banking services*. FSB. Acceso de los proveedores de remesas a servicios bancarios. <https://www.fsb.org/2018/03/stocktake-of-remittance-service-providers-access-to-banking-services/>
- Financial Action Task Force (2012-2025). *Recommendation 16: Wire transfers* e Interpretive Note. FATF. Información que debe acompañar a una transferencia transfronteriza. <https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html>
- World Bank (serie trimestral). *Remittance Prices Worldwide*. Metodología de costo total. <https://remittanceprices.worldbank.org/>
- Saunders, A. y Cornett, M. (2021). *Financial Institutions Management: A Risk Management Approach* (10.ª ed.). McGraw-Hill. Capítulo 14: riesgo de cambio.
- Verificación local: consulta el régimen cambiario, los límites de posición y las obligaciones de informe de operaciones transfronterizas de tu país.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 12 · Tesorería](12-tesoreria.md) | [Parte 10](../README.md) · [Programa](../../../SYLLABUS.md) | [14 · Comercio exterior →](14-comercio-exterior.md) |
<!-- gen:footer:end -->
