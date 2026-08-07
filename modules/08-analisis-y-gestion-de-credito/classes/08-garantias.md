<!-- meta
part: 9
class: 8
title: "Garantías"
level: profesional
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 08 · Garantías

> [← 07 · Historial crediticio](07-historial-crediticio.md) · [Índice de la parte](../README.md) · [09 · Flujo de caja del deudor empresarial →](09-flujo-de-caja.md)

**Parte 09 — Análisis y gestión de crédito** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Entender qué hace y qué no hace una garantía. Una garantía **no mejora la capacidad de pago del
deudor**: reduce la pérdida si el deudor incumple. Confundir ambas cosas produce el error más caro de
la originación: aprobar a quien no puede pagar porque "tiene garantía".

Las clases anteriores evalúan la primera fuente de pago, que es el flujo del deudor. Esta trata la segunda, y con una advertencia que ordena toda la clase: una garantía no convierte un mal crédito en uno bueno. Reduce la pérdida si el crédito falla, y eso es distinto de reducir la probabilidad de que falle.

## 📚 Objetivos

Al finalizar podrás:

1. **Clasificar** las garantías por tipo y por eficacia real.
2. **Valorar** una garantía con criterio de liquidación, no de mercado.
3. **Calcular** la severidad de la pérdida considerando la garantía.
4. **Verificar** la constitución correcta y su exigibilidad.
5. **Aplicar** el criterio de que la garantía es la segunda fuente de pago, nunca la primera.

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

Los dos primeros términos son los tipos de garantía; los cinco siguientes, cómo se valoran y qué efecto tienen. La distinción entre **valor de tasación y valor de liquidación** es la que hay que fijar: lo que importa no es cuánto vale el bien sino cuánto se obtendría vendiéndolo con prisa.

| Concepto | Comprensión verificable |
|---|---|
| `garantía real` | Recae sobre un bien: hipoteca, prenda. Da preferencia sobre otros acreedores. |
| `garantía personal` | Compromiso de un tercero: aval, fianza, codeuda. Vale lo que valga ese tercero. |
| `valor de tasación` | Valor estimado del bien en condiciones normales. |
| `valor de liquidación` | Valor obtenible en una venta forzada. Sustancialmente menor. |
| `relación préstamo/valor (LTV)` | `crédito / valor de la garantía`. Determina el colchón. |
| `severidad (LGD)` | Proporción de la exposición que se pierde si hay incumplimiento. |
| `primera y segunda fuente de pago` | El flujo del deudor es la primera; la garantía, la segunda. |

## 🧠 Modelo mental

Antes de entrar en tipos y valoraciones conviene fijar el orden de las dos fuentes de pago, porque de él depende para qué sirve una garantía y para qué no.

```text
PRIMERA FUENTE DE PAGO   el flujo de caja del deudor
                         determina si la operación se aprueba

SEGUNDA FUENTE DE PAGO   la garantía
                         determina cuánto se pierde si la primera falla
```

Una garantía excelente con una primera fuente insuficiente produce un crédito que **se cobrará
ejecutando el bien**, con costo, demora y deterioro de la relación. Ese no es el negocio bancario: es
el negocio inmobiliario o de remates.

## 📖 Desarrollo

### 1. Tipos de garantía y su eficacia

Las garantías se diferencian mucho en su eficacia real, que depende de cuánto se recupera y en cuánto tiempo. La tabla las compara.

| Tipo | Bien | Constitución | Eficacia relativa |
|---|---|---|---|
| Hipoteca | Inmueble | Escritura pública e inscripción | **Alta** |
| Prenda sin desplazamiento | Maquinaria, vehículos, existencias | Inscripción en registro | Media-alta |
| Prenda con desplazamiento | Bien mueble entregado | Entrega del bien | Alta, poco práctica |
| Cesión de créditos | Cuentas por cobrar | Notificación al deudor cedido | Media |
| Depósito en garantía | Efectivo o instrumento | Bloqueo | **Muy alta** |
| Aval o fianza | Patrimonio de un tercero | Documento | Variable |
| Carta de crédito standby | Compromiso de un banco | Emisión | Alta |
| Garantía estatal | Fondo de garantía público | Adhesión al programa | Alta, con condiciones |

**Factores que determinan la eficacia:**

```text
· liquidez del bien: ¿cuánto tarda en venderse?
· estabilidad del valor: ¿fluctúa mucho?
· facilidad de ejecución: ¿cuánto dura el procedimiento?
· preferencia: ¿hay acreedores anteriores?
· control: ¿puede el deudor deteriorar o enajenar el bien?
```

### 2. Valorar con criterio de liquidación

La valoración de liquidación descuenta plazo, costos y descuento de venta forzada. El procedimiento siguiente la obtiene.

```text
valor de liquidación = valor de tasación × factor de castigo
```

| Tipo de bien | Factor de castigo de referencia | Fundamento |
|---|---:|---|
| Depósito en la propia institución | 100 % | Sin riesgo de valor |
| Inmueble habitacional urbano | 70–80 % | Mercado profundo |
| Inmueble comercial | 60–70 % | Mercado más estrecho |
| Inmueble industrial o especializado | 40–60 % | Pocos compradores |
| Terreno urbano | 60–70 % | Depende de la zonificación |
| Vehículo comercial | 50–65 % | Deprecia rápido |
| Maquinaria estándar | 40–55 % | Mercado secundario limitado |
| Maquinaria especializada | 20–40 % | Puede no tener comprador |
| Existencias | 30–50 % | Obsolescencia y dispersión |
| Cuentas por cobrar | 50–70 % | Depende de la calidad del deudor cedido |

Al factor de castigo hay que restarle todavía lo que cuesta llegar hasta el
remate, que no es un porcentaje despreciable.

```text
además se descuentan los costos de ejecución:
  gastos judiciales, honorarios, comisión de remate, mantención del bien,
  impuestos: habitualmente 8 % a 15 % del valor
```

Encadenados sobre una tasación concreta, el castigo y los costos dejan un valor recuperable muy inferior al que figura en el informe del tasador.

```text
ejemplo:
  inmueble comercial, tasación                180 000 000
  factor de castigo (65 %)                    117 000 000
  costos de ejecución (12 %)                  −14 040 000
  VALOR RECUPERABLE ESTIMADO                  102 960 000  (57 % de la tasación)
```

### 3. LTV y severidad

La relación préstamo/valor determina la severidad esperada, y esa es la conexión entre garantía y provisión. El cálculo siguiente la establece.

```text
LTV = crédito / valor de tasación
severidad (LGD) = (exposición − recuperación) / exposición
```

Con esas dos definiciones se puede recorrer un mismo crédito en dos escenarios y ver cómo la severidad depende del momento del incumplimiento.

```text
crédito 120 000 000 · tasación 180 000 000 · LTV = 66,7 %
valor recuperable estimado 102 960 000

si el incumplimiento ocurre con exposición de 110 000 000:
  recuperación = min(110 000 000; 102 960 000) = 102 960 000
  pérdida = 7 040 000
  LGD = 6,4 %

si el incumplimiento ocurre con exposición de 118 000 000 y el mercado cayó 20 %:
  valor recuperable = 102 960 000 × 0,80 = 82 368 000
  pérdida = 35 632 000
  LGD = 30,2 %
```

**La severidad depende del momento del incumplimiento y del estado del mercado**, no solo del LTV
inicial. Por eso los LTV altos son especialmente peligrosos: dejan poco colchón ante una caída de
precios.

### 4. Verificar la constitución

Una garantía mal constituida no sirve en el momento de ejecutarla. La lista recoge las comprobaciones.

```text
□ el bien existe y está identificado sin ambigüedad
□ el constituyente es el dueño (certificado de dominio vigente)
□ no hay gravámenes anteriores (certificado de gravámenes)
□ la garantía está inscrita en el registro correspondiente
□ la inscripción es a favor de la institución y por el monto correcto
□ el bien está asegurado, con el acreedor como beneficiario
□ existe tasación independiente y vigente
□ el bien es enajenable (no tiene prohibiciones)
□ si es un bien conyugal, existe la autorización requerida
□ en garantías sobre existencias: hay control de inventario pactado
```

**El error más frecuente y más costoso** es desembolsar antes de que la garantía esté efectivamente
inscrita. Entre la firma y la inscripción pueden aparecer gravámenes de terceros que tomen preferencia.

### 5. Garantía como segunda fuente, nunca primera

Otorgar mirando la garantía en vez del flujo es la causa más frecuente de carteras problemáticas con buenas garantías. El esquema explica por qué.

```text
la garantía NO:
  ✗ mejora la capacidad de pago
  ✗ justifica aprobar a quien no puede pagar
  ✗ convierte un mal crédito en uno bueno
  ✗ elimina la necesidad de análisis del flujo

la garantía SÍ:
  ✓ reduce la pérdida esperada
  ✓ permite un mejor precio (menor prima de riesgo)
  ✓ alinea incentivos: el deudor tiene algo que perder
  ✓ reduce el consumo de capital regulatorio
```

Efecto sobre el precio:

```text
pérdida esperada = PD × LGD × EAD

sin garantía:  PD 3,0 % × LGD 65 % = 1,95 % de prima de riesgo
con garantía:  PD 3,0 % × LGD 25 % = 0,75 %
diferencia:                           1,20 puntos de menor tasa
```

**La garantía se traduce en precio, no en aprobación.**

## 🧮 Ejemplo guiado

El ejemplo valora una garantía a criterio de liquidación y calcula la severidad resultante. La diferencia con el valor de tasación suele ser de decenas de por ciento.

**Situación.** Una empresa solicita 240 millones ofreciendo garantías. Evalúa la operación.

```text
SOLICITANTE
  empresa de transporte, 9 años
  EBITDA anual                          118 millones
  deuda financiera actual               290 millones
  servicio de deuda anual actual         96 millones
  servicio del crédito solicitado        78 millones

GARANTÍAS OFRECIDAS
  A  hipoteca sobre terreno industrial, tasación 210 millones
  B  prenda sobre 12 camiones, tasación 168 millones
  C  aval del socio controlador, patrimonio declarado 400 millones
```

**Paso 1 — evalúa la PRIMERA fuente de pago antes que las garantías.**

```text
servicio total post-operación: 96 + 78 = 174 millones
EBITDA: 118 millones
cobertura del servicio de deuda = 118/174 = 0,68x

límite de política: mínimo 1,25x
```

**La cobertura es 0,68x: la empresa NO puede pagar el crédito con su flujo.**

**Paso 2 — la pregunta que decide la operación.**

```text
¿pueden las garantías compensar una cobertura de 0,68x?

NO. Una cobertura menor a 1,0 significa que el flujo no alcanza para el
servicio de la deuda. La operación se pagaría ejecutando garantías,
lo que no es un crédito: es una compra de activos con pasos adicionales.
```

**Paso 3 — aun así, valora las garantías para el análisis completo.**

```text
A  terreno industrial
   tasación                            210 000 000
   factor de castigo (industrial 50 %) 105 000 000
   costos de ejecución (12 %)          −12 600 000
   recuperable                          92 400 000
   
   ⚠ verificación: el certificado de gravámenes muestra una hipoteca
     de primer grado a favor de otro banco por 140 millones
   → la garantía ofrecida sería de SEGUNDO grado
   → recuperable efectivo: max(0; 92 400 000 − 140 000 000) = 0

B  12 camiones
   tasación                            168 000 000
   factor de castigo (vehículo comercial 58 %)  97 440 000
   costos de ejecución (15 %)          −14 616 000
   recuperable                          82 824 000
   
   ⚠ verificación: 7 de los 12 camiones ya tienen prenda a favor
     de la financiera del fabricante
   → solo 5 camiones están libres
   → recuperable efectivo: 82 824 000 × (5/12) = 34 510 000

C  aval del socio
   patrimonio declarado                400 000 000
   ⚠ verificación pendiente: certificados de dominio y de gravámenes
     de los bienes que componen ese patrimonio
   ⚠ el socio ya avala 290 millones de la deuda actual de la empresa
   → capacidad de aval remanente: por determinar
```

**Paso 4 — recalcula la severidad con las garantías efectivas.**

```text
garantías efectivas: 0 + 34 510 000 = 34 510 000
exposición: 240 000 000
cobertura de garantías: 14,4 %

LGD estimada = (240 000 000 − 34 510 000)/240 000 000 = 85,6 %
```

**Paso 5 — la lección del caso.**

```text
las garantías OFRECIDAS sumaban 378 millones de tasación (157 % del crédito)
las garantías EFECTIVAS suman 34,5 millones (14,4 % del crédito)

diferencia: 343,5 millones

causas:
  · el terreno ya está hipotecado por 140 millones a otro acreedor
  · 7 de 12 camiones ya están prendados
  · el aval del socio ya está comprometido en la deuda existente
```

**Paso 6 — decisión.**

```text
RECHAZAR

fundamento principal:
  la cobertura del servicio de deuda de 0,68x indica que la empresa
  no puede pagar el crédito con su flujo operativo

fundamento secundario:
  las garantías efectivas cubren el 14,4 % de la exposición,
  no el 157 % que aparentaban

ALTERNATIVA CONSTRUCTIVA
  la empresa necesita reestructurar su deuda existente, no tomar más:
    · deuda actual 290 millones con servicio de 96 millones
    · EBITDA 118 millones → cobertura actual 1,23x, ya en el límite
    · reperfilar la deuda existente a mayor plazo bajaría el servicio a ~68 millones
    · cobertura resultante: 1,74x
  
  esa operación SÍ es viable y resuelve el problema real de la empresa,
  que es de estructura de vencimientos, no de falta de financiamiento
```

**Interpreta:** la operación se rechaza **por la primera fuente de pago**, y el análisis de garantías
—que reveló una brecha de 343,5 millones entre lo ofrecido y lo efectivo— confirma la decisión sin
ser su fundamento. La alternativa propuesta atiende el problema real: **la empresa no necesita más
deuda, necesita reperfilar la que tiene**.

## 🏦 Del cliente al banco

El cliente ofrece una garantía y el banco calcula su valor de liquidación y su efecto sobre la provisión. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| "Tengo garantías suficientes" | La garantía no reemplaza la capacidad de pago | 9, clase 5 |
| Tasación exigida | Debe ser independiente y vigente | 9, clase 2 |
| Segundo grado de hipoteca | Recupera solo lo que exceda al primer acreedor | 11, clase 2 |
| Seguro exigido sobre el bien | Protege la garantía del acreedor | 3, clase 12 |
| Menor tasa con garantía | La garantía reduce la severidad, y eso baja el precio | 15, clase 7 |

## 🧪 Práctica

El laboratorio pide valorar tres garantías a criterio de liquidación y calcular la severidad. El orden por valor de tasación y por valor de liquidación no coincide.

En `labs/lab-04.md`, sección de garantías:

1. Valora cinco garantías con criterio de liquidación y costos de ejecución.
2. Calcula LTV y severidad en tres escenarios de mercado.
3. Aplica la lista de verificación de constitución a un caso.
4. Calcula el efecto de la garantía sobre el precio de la operación.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen garantías que no cubrieron lo esperado. Las causas son valoraciones sin descuento de liquidación y constituciones defectuosas.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se aprueba por la garantía | Primera fuente ignorada | El flujo decide; la garantía reduce la pérdida. |
| Se usa el valor de tasación | Criterio de liquidación omitido | Aplica factor de castigo y costos de ejecución. |
| No se verifican gravámenes anteriores | Preferencia ignorada | Certificado de gravámenes vigente. |
| Se desembolsa antes de inscribir | Riesgo de gravámenes de terceros | Desembolsa solo con inscripción confirmada. |
| El aval del socio se cuenta íntegro | Compromisos previos ignorados | Descuenta los avales ya otorgados. |
| Prenda sobre bienes ya prendados | Verificación omitida | Consulta el registro de prendas. |

## ❓ Preguntas de comprobación

1. ¿Qué hace y qué no hace una garantía?
2. ¿Por qué el valor de liquidación es sustancialmente menor al de tasación?
3. Calcula la severidad de un crédito con LTV 70 % y una caída de mercado del 25 %.
4. ¿Por qué desembolsar antes de inscribir la garantía es un error grave?
5. ¿Cómo se traduce una garantía en el precio de la operación?

## 📥 Entregable

Guarda en `portfolio/parte-09/clase-08/`:

- la valoración de cinco garantías con factor de castigo y costos;
- el cálculo de LTV y severidad en tres escenarios de mercado;
- la lista de verificación de constitución aplicada a un caso real o sintético;
- el efecto de la garantía sobre el precio con su cálculo de pérdida esperada.

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

- Basel Committee on Banking Supervision (2017). *Basel III: Finalising post-crisis reforms*. BIS. Tratamiento de mitigadores de riesgo de crédito y factores de descuento. <https://www.bis.org/bcbs/publ/d424.htm>
- Saunders, A. y Cornett, M. (2021). *Financial Institutions Management* (10.ª ed.). McGraw-Hill. Garantías y su efecto en la severidad.
- Caouette, J., Altman, E., Narayanan, P. y Nimmo, R. (2008). *Managing Credit Risk* (2.ª ed.). Wiley. Valoración y ejecución de garantías.
- European Banking Authority (2020). *Guidelines on loan origination and monitoring*. EBA. Valoración de garantías y monitoreo de su valor.
- Schuermann, T. (2004). "What Do We Know About Loss Given Default?". Wharton Financial Institutions Center. Evidencia empírica sobre severidad.
- Verificación local: revisa los registros de hipotecas y prendas de tu país, los plazos de ejecución y los costos judiciales aplicables.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 07 · Historial crediticio](07-historial-crediticio.md) | [Parte 09](../README.md) · [Programa](../../../SYLLABUS.md) | [09 · Flujo de caja del deudor empresarial →](09-flujo-de-caja.md) |
<!-- gen:footer:end -->
