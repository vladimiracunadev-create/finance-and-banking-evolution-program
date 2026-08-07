---
part: 18
class: 1
title: "Qué es un pago transfronterizo"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global, chile]
regulatory_topics: [cross-border-payments, cambios-internacionales]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [Banco Central de Chile, CPMI]
requires_legal_review: true
---

<!-- gen:header:start -->
# Clase 01 · Qué es un pago transfronterizo

> [← Índice de la parte](../README.md) · [Índice de la parte](../README.md) · [02 · Arquitectura de participantes y responsabilidades →](02-arquitectura-de-participantes.md)

**Parte 18 — Pagos transfronterizos, remesas y liquidación internacional** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Separar cuatro cosas que se usan como sinónimos y no lo son: **pago
transfronterizo**, **remesa**, **transferencia internacional** y **operación de
cambio**. La distinción no es académica: cada una tiene régimen, coste, riesgo y
supervisor distintos.

## 📚 Objetivos

Al finalizar podrás:

1. **Definir** un pago transfronterizo por su propiedad estructural, no por su
   apariencia.
2. **Distinguir** los cuatro conceptos con casos límite que los separen.
3. **Identificar** los cuatro problemas estructurales que la comunidad
   internacional intenta resolver.
4. **Descomponer** el coste total de un pago en sus componentes reales.
5. **Explicar** por qué un pago doméstico y uno internacional no se diferencian
   por la distancia.

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

Los cuatro primeros términos son los tipos de operación que se confunden entre sí; los cuatro siguientes, su segmentación y su medida. El **coste total** es el concepto que ordena la parte entera: lo que paga el ordenante no es la comisión sino la suma de comisiones, márgenes cambiarios y deducciones de intermediarios, y casi nunca se cotiza junto.

| Concepto | Comprensión verificable |
|---|---|
| `pago transfronterizo` | Pago en que ordenante y beneficiario están en jurisdicciones distintas |
| `remesa` | Transferencia de persona a persona, típicamente de trabajador migrante a su hogar |
| `transferencia internacional` | Movimiento de fondos entre cuentas en países distintos |
| `operación de cambio` | Compraventa de una divisa contra otra |
| `pago mayorista` | Entre instituciones financieras, importes altos |
| `pago minorista` | De personas o empresas, importes bajos, alto volumen |
| `corredor` | Par origen-destino con sus características propias |
| `coste total` | Comisión explícita más comisiones de intermediarios más diferencial de cambio |

## 🧠 Modelo mental

El modelo mental es que no existe una infraestructura global de pagos. Un pago transfronterizo se resuelve encadenando sistemas nacionales mediante cuentas entre bancos, y de esa arquitectura improvisada salen su coste, su lentitud y su opacidad.

```text
LA PROPIEDAD QUE DEFINE UN PAGO TRANSFRONTERIZO
NO ES LA DISTANCIA: ES QUE NINGÚN SISTEMA ÚNICO
LIQUIDA LAS DOS PATAS

  PAGO DOMÉSTICO
    ordenante y beneficiario en el mismo sistema
    → un solo libro contable resuelve el pago
    → hay un banco central que puede darle finalidad

  PAGO TRANSFRONTERIZO
    dos sistemas, dos monedas, dos ordenamientos,
    dos horarios y dos supervisores
    → NINGUNA autoridad puede dar finalidad a las dos patas
    → hace falta encadenar libros contables

TODO LO DEMÁS —el coste, la lentitud, la opacidad—
SALE DE ESA PROPIEDAD
```

## 📖 Desarrollo

### 1. Los cuatro conceptos, separados

| Concepto | ¿Cruza frontera? | ¿Cambia de moneda? | ¿Persona a persona? | Ejemplo |
|---|:---:|:---:|:---:|---|
| Pago transfronterizo | Sí | No necesariamente | No necesariamente | Empresa chilena paga a proveedor peruano |
| Remesa | Sí | Casi siempre | Sí | Trabajador envía dinero a su familia |
| Transferencia internacional | Sí | No necesariamente | No necesariamente | Mover fondos entre cuentas propias en dos países |
| Operación de cambio | No necesariamente | Sí, por definición | No necesariamente | Comprar dólares en el mercado local |

```text
LOS DOS CASOS LÍMITE QUE ORDENAN TODO

  CASO A · transferencia internacional SIN cambio de divisa
    una empresa mueve dólares de su cuenta en Nueva York
    a su cuenta en Santiago
    → cruza frontera, NO hay operación de cambio
    → sigue siendo pago transfronterizo

  CASO B · operación de cambio SIN cruzar frontera
    una persona compra euros en su banco local
    y los deja en una cuenta en el mismo banco
    → hay operación de cambio, NO cruza frontera
    → NO es un pago transfronterizo

  CONSECUENCIA
    la normativa de cambios internacionales y la de pagos
    NO se activan por las mismas causas
```

### 2. Mayorista y minorista

```text
MAYORISTA
  entre instituciones financieras
  importes altos, volumen bajo
  riesgo dominante: liquidación y contraparte
  infraestructura: sistemas de liquidación bruta en tiempo real

MINORISTA
  de personas y empresas
  importes bajos, volumen muy alto
  riesgo dominante: fraude, coste unitario, experiencia
  infraestructura: compensación por lotes o pagos inmediatos

POR QUÉ IMPORTA LA DISTINCIÓN
  una mejora de 5 segundos en el mayorista
  no cambia nada para nadie

  una mejora de 2 días en una remesa
  cambia cuándo come una familia
```

### 3. Los cuatro problemas estructurales

La hoja de ruta del G20 los nombró así, y toda la parte gira alrededor de ellos:

| Problema | Qué significa | Causa dominante |
|---|---|---|
| **Coste** | El envío consume una fracción alta del importe | Cadena de intermediarios y diferencial de cambio |
| **Velocidad** | Días en vez de segundos | Horarios, días inhábiles, controles secuenciales |
| **Acceso** | Corredores sin oferta o con una sola | Retirada de corresponsalías, escala insuficiente |
| **Transparencia** | Nadie sabe cuánto llega ni cuándo | Comisiones deducidas en tránsito, sin trazabilidad |

```text
EL ERROR DE DIAGNÓSTICO MÁS FRECUENTE
  «es lento porque la tecnología es antigua»

  la tecnología de mensajería es rápida: el mensaje
  llega en segundos. Lo lento es:
    · el horario del sistema de liquidación de destino
    · el día inhábil en una de las dos plazas
    · la revisión manual de un caso marcado por cumplimiento
    · la reparación de un mensaje con datos incompletos
    · la espera a que el corresponsal tenga saldo

  ninguno de los cinco se arregla cambiando el protocolo
```

### 4. Descomposición del coste

```text
COSTE TOTAL = comisión explícita del banco ordenante
            + comisiones de los intermediarios
            + comisión del banco beneficiario
            + DIFERENCIAL DE CAMBIO

EL CUARTO COMPONENTE SUELE SER EL MAYOR
Y ES EL ÚNICO QUE NO APARECE COMO COMISIÓN

  un envío de 500 con «comisión 4,90»
  y un tipo aplicado un 3,2 % peor que el de referencia
  cuesta en realidad 4,90 + 16,00 = 20,90

  la comisión visible era el 23 % del coste real
```

### 5. Las tres opciones de reparto de gastos

```text
OUR    el ordenante paga todas las comisiones;
       el beneficiario recibe el importe íntegro
SHA    cada parte paga las suyas; los intermediarios
       deducen de la propia transferencia
BEN    el beneficiario paga todo; se deduce del importe

DÓNDE APARECE LA OPACIDAD
  con SHA y BEN, los intermediarios deducen EN TRÁNSITO.
  El ordenante no sabe cuántos habrá ni cuánto cobrarán.
  → «envié 1 000 y llegaron 964» sin explicación posible
```

## 🧮 Ejemplo guiado

El ejemplo descompone el coste total de un pago concreto. Conviene sumar las tres fuentes por separado: la comisión declarada suele ser la menor de las tres.

**Situación.** Una persona en Chile envía dinero a un familiar en Filipinas y
compara dos rutas. Hay que calcular el coste real de cada una.

```text
IMPORTE A ENVIAR: 500 000 CLP
TIPO DE REFERENCIA DEL DÍA (mercado medio):
  1 USD = 950 CLP      1 USD = 56,0 PHP

RUTA A — banco tradicional
  comisión de envío:            18 000 CLP
  tipo CLP/USD aplicado:        978 CLP por USD
  comisión del intermediario:   15 USD (deducida en tránsito)
  comisión del banco receptor:  200 PHP
  tipo USD/PHP aplicado:        54,6 PHP por USD
  plazo declarado:              2 a 5 días hábiles

RUTA B — operador de remesas
  comisión de envío:             6 900 CLP
  tipo CLP/PHP aplicado directo: 1 CLP = 0,0566 PHP
  sin intermediarios
  plazo declarado:               minutos
```

**Paso 1 — calcula la Ruta A hasta dólares.**

```text
IMPORTE NETO TRAS COMISIÓN
  500 000 − 18 000 = 482 000 CLP

CONVERSIÓN A USD AL TIPO APLICADO
  482 000 / 978 = 492,84 USD

CUÁNTO SERÍA AL TIPO DE REFERENCIA
  482 000 / 950 = 507,37 USD

DIFERENCIAL DE CAMBIO EN ESTA PATA
  507,37 − 492,84 = 14,53 USD
```

**Paso 2 — sigue la Ruta A hasta pesos filipinos.**

```text
TRAS LA COMISIÓN DEL INTERMEDIARIO
  492,84 − 15 = 477,84 USD

CONVERSIÓN A PHP AL TIPO APLICADO
  477,84 × 54,6 = 26 090,1 PHP

MENOS LA COMISIÓN DEL BANCO RECEPTOR
  26 090,1 − 200 = 25 890,1 PHP RECIBIDOS
```

**Paso 3 — calcula la Ruta B.**

```text
IMPORTE NETO TRAS COMISIÓN
  500 000 − 6 900 = 493 100 CLP

CONVERSIÓN DIRECTA
  493 100 × 0,0566 = 27 909,5 PHP RECIBIDOS
```

**Paso 4 — construye el punto de comparación.**

```text
¿CUÁNTO SE RECIBIRÍA SIN NINGÚN COSTE?
  tipo cruzado de referencia:
    1 CLP = (1/950) USD = (1/950) × 56,0 PHP = 0,058947 PHP

  500 000 × 0,058947 = 29 473,7 PHP

ESTE ES EL DENOMINADOR HONESTO.
Comparar las dos rutas entre sí sin esta cifra
oculta cuánto se pierde en ambas.
```

**Paso 5 — calcula el coste total de cada ruta.**

```text
RUTA A
  29 473,7 − 25 890,1 = 3 583,6 PHP de coste
  3 583,6 / 29 473,7 = 12,16 % del importe

RUTA B
  29 473,7 − 27 909,5 = 1 564,2 PHP de coste
  1 564,2 / 29 473,7 = 5,31 % del importe
```

**Paso 6 — descompón el coste de la Ruta A.**

```text
CONVERTIDO TODO A PHP AL TIPO DE REFERENCIA

  comisión de envío   18 000 CLP × 0,058947 =  1 061,0 PHP   29,6 %
  diferencial CLP/USD 14,53 USD × 56,0      =    813,7 PHP   22,7 %
  comisión intermed.  15 USD × 56,0         =    840,0 PHP   23,4 %
  diferencial USD/PHP 477,84 × (56,0−54,6)  =    669,0 PHP   18,7 %
  comisión receptora                        =    200,0 PHP    5,6 %
  ────────────────────────────────────────────────────────────────
  TOTAL                                        3 583,7 PHP  100,0 %

EL DATO QUE IMPORTA
  comisiones visibles: 1 061,0 + 840,0 + 200,0 = 2 101,0 (58,6 %)
  diferenciales de cambio: 813,7 + 669,0 = 1 482,7 (41,4 %)

  → el 41 % del coste NO aparece en ninguna línea
    del comprobante que recibe el remitente
```

**Paso 7 — formula la decisión y lo que falta.**

```text
LA RUTA B CUESTA 2 019,4 PHP MENOS: 6,85 PUNTOS PORCENTUALES

PERO LA DECISIÓN NO ES SOLO PRECIO
  · ¿el operador está registrado y supervisado?
  · ¿qué ocurre si el pago no llega? ¿hay reclamación?
  · ¿el familiar tiene un punto de retiro cercano?
  · ¿el tipo mostrado se garantiza o cambia al liquidar?
  · ¿hay límites por operación o por mes?

Y UNA PREGUNTA DE MÉTODO
  el tipo de referencia usado como denominador es del
  momento del cálculo. Si las rutas liquidan en momentos
  distintos, parte de la diferencia es movimiento de
  mercado, no coste. Se declara como supuesto.
```

**Interpreta:** las dos rutas se anunciaban con su comisión —18 000 y 6 900—, y
esa cifra explicaba menos del 60 % del coste en una y menos de la mitad en la
otra. **El diferencial de cambio es el coste que no se declara**, y es la razón
por la que el problema de la transparencia aparece antes que el del precio.

## 🧭 Perspectivas

Un mismo pago se ve distinto desde cada participante de la cadena, y ninguno ve el trayecto completo. La tabla los enfrenta, y esa visión parcial es el origen de la opacidad.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | «Envié 500 000 y llegaron 25 890» | Si vuelve a usar esa ruta |
| Comercio | Cobro internacional incierto | Si acepta el medio |
| Fintech | Un corredor con margen | Si entra y cómo lo precia |
| Banco | Cadena de corresponsales heredada | Si mantiene o reduce la red |
| Banco central | Coste y acceso del corredor | Si interviene o vigila |
| Infraestructura | Volumen y horarios | Capacidad y ventanas |
| Supervisor | Transparencia del precio | Qué exige revelar |
| Auditor | Diferenciales aplicados | Si son consistentes con la política |
| Sociedad | Remesas como ingreso familiar | Presión por reducir el coste |

## 🏦 Del cliente al banco

El cliente ve un envío y el banco ve una cadena de corresponsales con sus propias comisiones. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Llegó menos de lo que envié» | Comisiones deducidas en tránsito | 18, clase 1 |
| «Tardó cuatro días» | Horarios, día inhábil, revisión manual | 18, clases 7 y 8 |
| «El tipo no era el que vi» | Diferencial aplicado al liquidar | 18, clase 9 |
| «Nadie sabe dónde está mi dinero» | Falta de trazabilidad extremo a extremo | 18, clase 6 |

## ⚖️ Riesgos y controles

Los riesgos aquí son de coste opaco y de plazo incierto antes que de crédito. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Coste oculto | El diferencial no se declara | Revelar tipo aplicado y de referencia |
| Comparación engañosa | Se compara solo la comisión | Comparar importe recibido |
| Confusión de conceptos | Se aplica la norma equivocada | Clasificar por las cuatro definiciones |
| Plazo indeterminado | «2 a 5 días hábiles» | Compromiso de fecha de disponibilidad |
| Pérdida en tránsito | Nadie sabe qué intermediario dedujo | Trazabilidad y confirmación de cargos |
| Ruta única | Un solo corresponsal en el corredor | Redundancia y plan de sustitución |

## 🧪 Práctica

En [`labs/lab-01.md`](../labs/lab-01.md) y [`labs/lab-05.md`](../labs/lab-05.md):

1. Clasifica ocho operaciones en los cuatro conceptos, con su justificación.
2. Calcula el coste total de tres rutas usando el tipo de referencia como
   denominador.
3. Descompón el coste en comisiones visibles y diferencial.
4. Identifica qué componente no aparece en el comprobante del cliente.

## ⚠️ Errores frecuentes

La tabla se usa buscando el síntoma. En esta clase casi todos vienen de haber comparado por comisión en vez de por coste total.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Comparar solo comisiones | Se ignoró el diferencial | Compara importe recibido |
| «Transfronterizo = cambio de divisa» | Se fundieron dos conceptos | Caso A: cruza sin cambiar |
| «Es lento por la tecnología» | Diagnóstico superficial | Enumera las cinco causas reales |
| Usar el tipo del banco como referencia | El denominador está sesgado | Usa el tipo medio de mercado |
| Tratar remesa y pago comercial igual | Regímenes y riesgos distintos | Sepáralos desde el diseño |
| Ignorar el reparto de gastos | No se miró OUR/SHA/BEN | Determina quién paga qué |

## ❓ Preguntas de comprobación

1. ¿Qué propiedad estructural define un pago transfronterizo, y por qué no es la
   distancia?
2. Da un caso que cruce frontera sin operación de cambio y otro al revés.
3. ¿Cuáles son los cuatro problemas estructurales y cuál es la causa dominante
   de cada uno?
4. ¿Por qué el tipo de referencia es el denominador correcto para comparar rutas?
5. En el ejemplo guiado, ¿qué porcentaje del coste no aparecía en el
   comprobante y por qué?

## 📥 Entregable

Guarda en `portfolio/parte-18/clase-01/`:

- la clasificación de ocho operaciones en los cuatro conceptos;
- el cálculo del coste total de dos rutas con el tipo de referencia;
- la descomposición del coste entre comisiones visibles y diferencial;
- una lista de las cinco causas de lentitud aplicadas a un corredor concreto.

## 🔗 Referencias cruzadas

- **Viene de:** Parte 6, clase 12 (tipo de cambio); Parte 10, clase 13
  (pagos internacionales); Parte 14, clase 2 (pagos digitales).
- **Continúa en:** clase 2 (participantes), clase 9 (FX), clase 10 (remesas).
- **Se aplica en:** Parte 22, clase 3 (normativa de cambios); Parte 23, clase 8.

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

- Financial Stability Board (2020). *Enhancing Cross-border Payments: Stage 3 roadmap*. FSB. <https://www.fsb.org/2020/10/enhancing-cross-border-payments-stage-3-roadmap/>
- Committee on Payments and Market Infrastructures (2018). *Cross-border retail payments*. BIS. <https://www.bis.org/cpmi/publ/d173.htm>
- Banco Mundial. *Remittance Prices Worldwide*. <https://remittanceprices.worldbank.org/>
- Committee on Payments and Market Infrastructures (2020). *Enhancing cross-border payments: building blocks of a global roadmap*. BIS. <https://www.bis.org/cpmi/publ/d193.htm>
- Banco Central de Chile. *Compendio de Normas de Cambios Internacionales*. <https://www.bcentral.cl/>
- Verificación local: comprueba qué operaciones deben informarse al banco central de tu país, qué obligaciones de transparencia de precio existen y si tu jurisdicción tiene mercado cambiario formal. **Fecha de verificación de esta clase: 2026-08-06.** Esta clase no constituye asesoría legal.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← Índice de la parte](../README.md) | [Parte 18](../README.md) · [Programa](../../../SYLLABUS.md) | [02 · Arquitectura de participantes y responsabilidades →](02-arquitectura-de-participantes.md) |
<!-- gen:footer:end -->
