<!-- meta
part: 22
class: 12
title: "Prevención de lavado y financiamiento del terrorismo"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [chile, internacional]
regulatory_topics: [prevencion-de-lavado, regla-del-viaje, sanciones]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [GAFI, UAF, FSB]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 12 · Prevención de lavado y financiamiento del terrorismo

> [← 11 · Conducta de mercado e integridad](11-conducta-de-mercado-e-integridad.md) · [Índice de la parte](../README.md) · [13 · Protección de datos y economía de la información →](13-proteccion-de-datos-y-economia-de-la-informacion.md)

**Parte 22 — Regulación de mercados financieros digitales** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Aplicar el régimen de prevención a los proveedores de servicios sobre activos
virtuales. Esta clase enseña a **cumplir y a detectar**; no proporciona
técnicas de evasión ni describe cómo eludir controles.

Las clases anteriores regulan el mercado. Esta trata la obligación que lo atraviesa entero, y su dificultad propia: la regla del viaje supone un intermediario en el destino y a veces no lo hay.

## 📚 Objetivos

Al finalizar podrás:

1. **Identificar** al sujeto obligado en una cadena de servicios.
2. **Aplicar** la regla del viaje a una transferencia de activos virtuales.
3. **Diseñar** un enfoque basado en riesgo proporcionado y documentado.
4. **Evaluar** el análisis de la contraparte antes de transferir.
5. **Determinar** qué hacer cuando el destinatario no es un sujeto obligado.

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

Los cuatro primeros términos son las obligaciones y sus figuras; los cuatro siguientes, la regla del viaje y sus medidas. La **contraparte** es el problema propio de este ámbito: cuando el destinatario es una dirección sin entidad detrás, la regla del viaje no tiene a quién transmitir la información.

| Concepto | Comprensión verificable |
|---|---|
| `sujeto obligado` | Quien debe aplicar el régimen |
| `enfoque basado en riesgo` | Intensidad del control proporcional al riesgo |
| `debida diligencia` | Conocimiento del cliente y del propósito |
| `beneficiario final` | Persona natural que controla en último término |
| `regla del viaje` | Datos que deben acompañar a la transferencia |
| `contraparte` | Proveedor que recibe la transferencia |
| `operación sospechosa` | La que no se explica por la actividad conocida |
| `congelamiento` | Inmovilización por lista de sanciones |

## 🧠 Modelo mental

El modelo mental es una obligación diseñada para un mundo de intermediarios aplicada a uno donde puede no haberlos. La norma exige transmitir datos del ordenante y del beneficiario, y a veces el beneficiario es una cartera autocustodiada.

```text
LA REGLA DEL VIAJE, TRASLADADA

  EN UNA TRANSFERENCIA BANCARIA
    el mensaje lleva ordenante y beneficiario
    y viaja por un canal común

  EN UNA TRANSFERENCIA DE ACTIVOS VIRTUALES
    el registro NO transporta esos datos
    → hay que enviarlos por un canal aparte
    → y hay que saber A QUIÉN enviarlos

Y AHÍ ESTÁ EL PROBLEMA ESTRUCTURAL
  antes de transferir hay que determinar
  si la dirección de destino pertenece a
  un sujeto obligado, y el registro no lo dice.
```

## 📖 Desarrollo

### 1. Quién es sujeto obligado

```text
HABITUALMENTE, QUIEN PRESTA POR CUENTA
DE TERCEROS ALGUNO DE ESTOS SERVICIOS

  · cambio entre activos virtuales y moneda
  · cambio entre activos virtuales
  · transferencia
  · custodia o administración
  · participación en la oferta de un emisor

QUIEN NO SUELE SERLO
  · quien opera por cuenta propia
  · quien solo desarrolla software
  · quien custodia sus propios activos

Y LA FRONTERA SE DECIDE POR LOS HECHOS
observables de la clase 1, no por la
descripción del servicio.
```

### 2. Enfoque basado en riesgo

```text
NO ES «MENOS CONTROL SI SOMOS PEQUEÑOS»

  ES: más intensidad donde hay más riesgo
  y menos donde hay menos, con un análisis
  documentado que lo justifique

FACTORES HABITUALES
  · jurisdicción del cliente y del destino
  · tipo de producto y su trazabilidad
  · canal de contratación
  · importe y frecuencia
  · perfil del cliente

LO QUE HACE VÁLIDO EL ENFOQUE
  · el análisis está escrito
  · los umbrales derivan de él
  · se revisa periódicamente
  · y hay evidencia de que se aplica
```

### 3. La regla del viaje en la práctica

```text
PASOS

  1 determinar si el destino es un sujeto
    obligado
  2 si lo es, enviar los datos por el canal
    acordado, antes o con la transferencia
  3 si no lo es, aplicar medidas reforzadas
    sobre el cliente
  4 conservar la información
  5 no ejecutar si falta información exigida

EL PASO 1 ES EL DIFÍCIL
  · listas compartidas entre proveedores
  · protocolos de descubrimiento
  · consulta al propio cliente

Y NINGUNO ES COMPLETO: siempre hay un
resto de destinos no identificables, y el
tratamiento de ese resto es la decisión
que define el programa.
```

### 4. El destino no identificable

```text
OPCIONES QUE SE USAN

  a  prohibir la transferencia
  b  permitirla con límite de importe
  c  permitirla con declaración del cliente
     sobre el destino
  d  permitirla con medidas reforzadas
     y vigilancia posterior

QUÉ NO FUNCIONA
  · aceptar cualquier declaración sin
    contraste
  · prohibir sin excepción, porque empuja
    la actividad fuera del perímetro

DISEÑO RAZONABLE
  b + c + d con umbrales derivados del
  análisis de riesgo, y revisión del resto
  no identificable como métrica de gestión
```

### 5. Sanciones

```text
LAS LISTAS DE SANCIONES OBLIGAN
CON INDEPENDENCIA DEL RÉGIMEN FINANCIERO

  · hay que cotejar antes de operar
  · y congelar sin previo aviso si hay
    coincidencia

PARTICULARIDAD DE LOS REGISTROS
  algunas listas incluyen DIRECCIONES,
  no solo nombres
  → el cotejo es sobre el destino, no
    solo sobre el cliente

Y UNA DIRECCIÓN PUEDE RECIBIR FONDOS
DE UNA SANCIONADA SIN QUE SU TITULAR
LO SEPA
  → de ahí el análisis de la procedencia
    y no solo del titular
```

## 🧮 Ejemplo guiado

El ejemplo aplica la regla del viaje a tres casos, uno de ellos con cartera autocustodiada. El tercero es el que no tiene solución limpia.

**Situación.** Un proveedor calibra su programa. Hay que dimensionar el resto no
identificable y decidir su tratamiento.

```text
DATOS DE UN MES
  transferencias salientes             28 400
  a proveedores identificados          19 300
  a destinos no identificables          9 100
  importe medio                          3 200
  coste de una medida reforzada             22
  alertas de sanciones                      86
  coincidencias confirmadas                  3
```

**Paso 1 — mide el resto.**

```text
NO IDENTIFICABLES
  9 100 / 28 400 = 32,0 %
  importe = 9 100 × 3 200 = 29 120 000

  → UN TERCIO DE LAS TRANSFERENCIAS
    NO PUEDE CUMPLIR LA REGLA DEL VIAJE
```

**Paso 2 — evalúa prohibirlas.**

```text
PROHIBIR EL 32 %

  · pérdida de ingreso supuesta: 0,25 %
    de 29 120 000 = 72 800 al mes
  · y el cliente que quiera hacerlo lo hará
    en otro proveedor, probablemente peor

  → la prohibición total desplaza la
    actividad, no la elimina
```

**Paso 3 — diseña el tratamiento por tramos.**

```text
TRAMO 1 · hasta 1 000
  declaración del cliente sobre el destino
  sin medida adicional
  supuesto: 5 400 transferencias

TRAMO 2 · 1 000 – 15 000
  declaración más análisis de procedencia
  del destino
  supuesto: 3 200 transferencias
  coste 3 200 × 22 = 70 400

TRAMO 3 · más de 15 000
  medidas reforzadas y aprobación
  supuesto: 500 transferencias
  coste 500 × 22 × 3 = 33 000

COSTE TOTAL 103 400 al mes
frente a 72 800 de pérdida por prohibir
```

**Paso 4 — compara y decide.**

```text
PROHIBIR    pérdida  72 800 al mes
POR TRAMOS  coste   103 400 al mes

  → PROHIBIR PARECE MÁS BARATO

Y ES LA CONCLUSIÓN EQUIVOCADA
  porque no cuenta el riesgo de que el
  cliente se vaya a un proveedor sin
  controles, ni la pérdida del cliente
  completo, ni el valor de la información
  que el tramo 2 genera

DECISIÓN
  por tramos, y el coste de 103 400 se
  presenta al comité como lo que es:
  el precio de mantener la actividad
  dentro del perímetro vigilado
```

**Paso 5 — revisa las sanciones.**

```text
86 ALERTAS · 3 COINCIDENCIAS

  precisión 3,49 %
  y las 83 restantes se resolvieron
  como falsos positivos

  ¿SE COTEJA LA PROCEDENCIA?
  no: solo el titular y el destino directo

  RIESGO
  una dirección limpia que recibió fondos
  de una sancionada dos saltos atrás

  MEDIDA
  análisis de procedencia hasta N saltos
  para importes del tramo 3
  supuesto: añade 210 alertas y 2
  coincidencias al mes
```

**Interpreta:** el 32 % de destinos no identificables no era un fallo del
programa: **es una consecuencia estructural de que el registro no transporta la
identidad**. Prohibir parecía más barato y solo desplazaba la actividad a un
proveedor sin controles.

## 🧭 Perspectivas

La prevención afecta a cada participante de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Preguntas sobre su destino | Si las responde |
| Proveedor | 32 % no identificable | Cómo lo trata |
| Contraparte | Datos que llegan por otro canal | Si los acepta |
| Banco | Un cliente con exposición | Qué exige |
| Autoridad | 3 coincidencias al mes | Qué investiga |
| Supervisor | Enfoque de riesgo documentado | Qué revisa |
| Auditor | Evidencia de aplicación | Qué muestrea |
| Sociedad | Actividad vigilada o desplazada | Qué prefiere |

## 🏦 Del cliente al banco

El cliente envía a una cartera propia y la entidad tiene una obligación que no puede cumplir del todo. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Me piden datos del destino» | La regla del viaje lo exige | 22, clase 12 |
| «Es una dirección normal» | No se puede saber si hay obligado detrás | 22, clase 12 |
| «Me bloquearon sin avisar» | El congelamiento no admite preaviso | 22, clase 12 |

## ⚖️ Riesgos y controles

Los riesgos son de incumplimiento y de exclusión. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Sujeto obligado mal determinado | Se opera sin aplicar el régimen | Hechos observables de la clase 1 |
| Enfoque de riesgo no documentado | No se puede justificar el umbral | Análisis escrito y revisado |
| Resto no identificable ignorado | Un tercio sin regla del viaje | Tratamiento por tramos y métrica |
| Prohibición total | Desplaza la actividad | Tramos con medidas proporcionadas |
| Cotejo solo del titular | La procedencia no se mira | Análisis hasta N saltos en tramos altos |
| Declaración sin contraste | Se acepta cualquier respuesta | Verificación proporcional al importe |

## 🧪 Práctica

El laboratorio pide aplicar la regla del viaje a varios casos. El caso de la cartera autocustodiada es el que decide el ejercicio.

En [`labs/lab-05.md`](../labs/lab-05.md):

1. Mide el resto no identificable y su importe.
2. Diseña el tratamiento por tramos con su coste.
3. Compara con prohibir y explica por qué la comparación simple engaña.
4. Añade el análisis de procedencia y recalcula.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen incumplimientos de la regla del viaje. La causa es la contraparte sin entidad.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Enfoque de riesgo sin análisis | Se copian umbrales | El análisis justifica el umbral |
| Prohibir por simplicidad | Parece más barato | Desplaza la actividad |
| Cotejar solo el nombre | Es lo que hace el sistema | Las listas incluyen direcciones |
| Ignorar la procedencia | Es más caro | En tramos altos lo justifica |
| Aceptar la declaración | El cliente responde | Contrástala según el importe |
| Tratar el resto como error | Se busca llevarlo a cero | Es estructural: gestiónalo |

## ❓ Preguntas de comprobación

1. ¿Quién es sujeto obligado y con qué criterio se determina?
2. ¿Por qué la regla del viaje es estructuralmente más difícil aquí?
3. ¿Qué hace válido un enfoque basado en riesgo?
4. ¿Por qué prohibir las transferencias no identificables no es la mejor opción?
5. ¿Qué añade el análisis de procedencia frente al cotejo del titular?

## 📥 Entregable

Guarda en `portfolio/parte-22/clase-12/`:

- la medición del resto no identificable;
- el tratamiento por tramos con su coste;
- la comparación con la prohibición y su crítica;
- el análisis de procedencia propuesto, con su umbral.

## 🔗 Referencias cruzadas

- **Viene de:** clases 1 y 11; Parte 18, clases 6 y 12.
- **Continúa en:** clases 13 y 16 de esta parte.
- **Se aplica en:** clase 18 de esta parte; Parte 23, clase 13.

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

- Financial Action Task Force (2021). *Updated Guidance for a Risk-Based Approach to Virtual Assets and VASPs*. FATF. <https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-rba-virtual-assets-2021.html>
- Financial Action Task Force. *The FATF Recommendations*, recomendación 15 y 16. FATF. <https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html>
- Financial Stability Board (2023). *Global Regulatory Framework for Crypto-asset Activities*. FSB. <https://www.fsb.org/2023/07/fsb-global-regulatory-framework-for-crypto-asset-activities/>
- Unidad de Análisis Financiero de Chile. *Normativa aplicable a los sujetos obligados*. UAF. <https://www.uaf.cl/>
- Verificación local: comprueba quiénes son sujetos obligados en tu jurisdicción, qué umbrales aplica la regla del viaje y qué canal de intercambio de información se admite. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 11 · Conducta de mercado e integridad](11-conducta-de-mercado-e-integridad.md) | [Parte 22](../README.md) · [Programa](../../../SYLLABUS.md) | [13 · Protección de datos y economía de la información →](13-proteccion-de-datos-y-economia-de-la-informacion.md) |
<!-- gen:footer:end -->
