<!-- meta
part: 18
class: 2
title: "Arquitectura de participantes y responsabilidades"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global]
regulatory_topics: [cross-border-payments, riesgo-de-terceros]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [CPMI, FSB]
requires_legal_review: false
-->

<!-- gen:header:start -->
# Clase 02 · Arquitectura de participantes y responsabilidades

> [← 01 · Qué es un pago transfronterizo](01-que-es-un-pago-transfronterizo.md) · [Índice de la parte](../README.md) · [03 · Corresponsalía bancaria →](03-corresponsalia-bancaria.md)

**Parte 18 — Pagos transfronterizos, remesas y liquidación internacional** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Dibujar quién hace qué en un pago transfronterizo y, sobre todo, **quién responde
cuando falla**. La cadena tiene más eslabones de los que el cliente ve, y la
responsabilidad no siempre está donde está el fallo.

La clase anterior situó el problema y su coste. Esta abre la cadena que lo produce, y muestra por qué nadie puede responder qué pasó con un pago: cada participante solo conoce a sus vecinos inmediatos.

## 📚 Objetivos

Al finalizar podrás:

1. **Nombrar** los ocho papeles de la cadena y decir qué hace cada uno.
2. **Trazar** los cuatro flujos —mensaje, fondos, contable y cumplimiento— sobre
   un caso concreto.
3. **Determinar** dónde se rompe la responsabilidad frente al cliente.
4. **Distinguir** pago en serie de pago con cobertura, y sus consecuencias.
5. **Identificar** los eslabones que concentran riesgo sin ser visibles.

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

Los cuatro primeros términos son las partes del pago; los cuatro siguientes, los intermediarios y las dos formas de encadenarlos. La distinción entre **pago en serie y con cobertura** decide dónde puede detenerse un pago y quién puede informar de su estado.

| Concepto | Comprensión verificable |
|---|---|
| `ordenante` | Quien instruye el pago |
| `beneficiario` | Quien debe recibir los fondos |
| `banco ordenante` | Institución que recibe la instrucción del ordenante |
| `banco beneficiario` | Institución que abona al beneficiario |
| `corresponsal` | Banco que mantiene cuenta para otro banco en su plaza |
| `intermediario` | Banco que participa sin relación con ordenante ni beneficiario |
| `pago en serie` | La instrucción y los fondos recorren la misma cadena |
| `pago con cobertura` | Instrucción directa al beneficiario y fondos por otra vía |

## 🧠 Modelo mental

El modelo mental es una cadena donde cada eslabón solo conoce a sus vecinos. El banco ordenante no sabe qué hará el tercer intermediario, y por eso no puede garantizar ni el plazo ni el importe que llegará.

```text
UN PAGO TRANSFRONTERIZO TIENE CUATRO FLUJOS
QUE NO VIAJAN JUNTOS

  FLUJO DE MENSAJE       la instrucción: quién paga a quién y cuánto
  FLUJO DE FONDOS        el movimiento real en cuentas
  FLUJO CONTABLE         los apuntes en cada libro
  FLUJO DE CUMPLIMIENTO  screening, sanciones, origen de fondos

CADA UNO PUEDE FALLAR POR SU CUENTA

  mensaje sin fondos     → el beneficiario ve un aviso y no cobra
  fondos sin mensaje     → llega dinero que nadie sabe aplicar
  contable descuadrado   → el corresponsal reclama
  cumplimiento detenido  → todo se para y nadie avisa

EL 80 % DE LAS INVESTIGACIONES NACEN
DE UNA DESINCRONIZACIÓN ENTRE DOS DE LOS CUATRO
```

## 📖 Desarrollo

### 1. Los ocho papeles

```text
1 ORDENANTE            instruye; asume el coste según OUR/SHA/BEN
2 BANCO ORDENANTE      valida, aplica cumplimiento, ejecuta
3 CORRESPONSAL DEL 2   mantiene la cuenta del banco ordenante
4 INTERMEDIARIOS       eslabones sin relación con el cliente
5 CORRESPONSAL DEL 6   mantiene la cuenta del banco beneficiario
6 BANCO BENEFICIARIO   abona al beneficiario
7 BENEFICIARIO         recibe
8 INFRAESTRUCTURA      red de mensajería y sistemas de liquidación

Y DOS FIGURAS QUE NO APARECEN EN EL DIAGRAMA CLÁSICO
9  PROVEEDOR DE MENSAJERÍA O DE PLATAFORMA
10 PROVEEDOR DE SCREENING DE SANCIONES
   ambos son terceros críticos: su caída detiene la cadena
   y ninguno tiene relación con el cliente
```

### 2. Pago en serie frente a pago con cobertura

```text
EN SERIE
  banco ordenante → corresponsal → intermediario → banco beneficiario
  la instrucción y los fondos recorren la MISMA cadena

  ventaja   cada eslabón ve la operación completa
  problema  cada eslabón puede deducir comisión y añadir demora

CON COBERTURA
  instrucción:  banco ordenante ──────────────► banco beneficiario
  fondos:       banco ordenante → corresponsales → corresponsal del beneficiario

  ventaja   el beneficiario recibe el detalle sin degradar
  problema  el banco beneficiario abona confiando en que
            la cobertura llegará; asume riesgo si no llega
            y los intermediarios ven menos información,
            lo que degrada el control de cumplimiento
```

### 3. Dónde se rompe la responsabilidad

```text
FRENTE AL CLIENTE
  responde su banco: el ordenante reclama al banco ordenante

ENTRE BANCOS
  cada uno responde ante el siguiente, por contrato
  → la cadena de reclamación es bilateral y secuencial

LA CONSECUENCIA PRÁCTICA
  el banco ordenante responde ante su cliente por un fallo
  que ocurrió tres eslabones más allá, con un banco
  con el que no tiene contrato

  → por eso el banco ordenante limita la red de corresponsales:
    cada eslabón nuevo es un riesgo que asume sin controlar
```

### 4. Los cuatro flujos sobre un caso

```text
PAGO DE 10 000 USD, CHILE → VIETNAM

  MENSAJE
    T0    banco CL envía instrucción a su corresponsal en NY
    T0+1s corresponsal NY envía a corresponsal en Singapur
    T0+2s corresponsal SG envía a banco VN

  FONDOS
    T0    banco CL adeuda su cuenta nostro en NY
    T+1d  liquidación en el sistema de EE. UU.
    T+1d  corresponsal NY acredita a corresponsal SG
    T+2d  corresponsal SG acredita a banco VN

  CONTABLE
    banco CL:      cargo a cliente, abono a nostro NY
    corresp. NY:   cargo a vostro CL, abono a nostro SG
    banco VN:      cargo a nostro SG, abono a cliente

  CUMPLIMIENTO
    banco CL:      screening del ordenante y del beneficiario
    corresp. NY:   screening de todas las partes y del banco CL
    corresp. SG:   ídem
    banco VN:      screening y verificación del beneficiario

EL MENSAJE TARDÓ 2 SEGUNDOS.
LOS FONDOS, DOS DÍAS.
EL CLIENTE PERCIBE LOS DOS DÍAS.
```

### 5. Los eslabones invisibles que concentran riesgo

| Eslabón | Por qué no se ve | Qué pasa si cae |
|---|---|---|
| Proveedor de mensajería | Es infraestructura común | Ningún pago sale |
| Proveedor de screening | Es un servicio contratado | Todo queda en cola manual |
| Proveedor de datos de sanciones | Se actualiza solo | Se opera con listas viejas |
| Corresponsal único del corredor | Es una decisión antigua | El corredor se cierra |
| Proveedor de tipo de cambio | Es un dato, no un actor | Se aplica un tipo obsoleto |

## 🧮 Ejemplo guiado

El ejemplo recorre un pago en serie y otro con cobertura sobre la misma operación. Conviene comparar en qué punto cada uno puede informar del estado.

**Situación.** Un banco investiga por qué su corredor Chile → Vietnam tiene una
tasa de procesamiento directo del 71 % cuando su objetivo es 95 %. Analiza
1 000 pagos del mes.

```text
RESULTADO DE LOS 1 000 PAGOS
  procesados sin intervención (STP)          710
  detenidos por cumplimiento                 148
  con datos incompletos (reparación)          97
  rechazados por el banco beneficiario        31
  devueltos                                   14

TIEMPO MEDIO POR CATEGORÍA
  STP                          4 h
  detenidos por cumplimiento  31 h
  reparación                  19 h
  rechazo + reenvío           52 h

COSTE OPERATIVO POR INTERVENCIÓN MANUAL: 14 USD
```

**Paso 1 — calcula el coste operativo del problema.**

```text
INTERVENCIONES MANUALES
  148 + 97 + 31 + 14 = 290

COSTE MENSUAL
  290 × 14 = 4 060 USD
ANUALIZADO
  48 720 USD
```

**Paso 2 — calcula el plazo medio real que percibe el cliente.**

```text
PLAZO MEDIO PONDERADO
  (710×4 + 148×31 + 97×19 + 31×52 + 14×52) / 1 000
  = (2 840 + 4 588 + 1 843 + 1 612 + 728) / 1 000
  = 11 611 / 1 000 = 11,6 horas

PERO EL PROMEDIO ENGAÑA
  el 71 % de los clientes ve 4 horas
  el 15 % ve 31 horas
  el 4,5 % ve 52 horas

  → el compromiso comercial debe fijarse sobre el percentil,
    no sobre la media: p95 ≈ 52 h
```

**Paso 3 — investiga los 148 detenidos por cumplimiento.**

```text
DESGLOSE
  coincidencia con lista de sanciones, descartada     119
  coincidencia confirmada                               2
  país de alto riesgo, revisión estándar               21
  importe inusual para el ordenante                     6

EL DATO
  119 de 148 fueron FALSOS POSITIVOS: 80,4 %

CAUSA DE LOS FALSOS POSITIVOS
  nombres transliterados del vietnamita sin criterio único
  → «Nguyen Van Minh» coincide parcialmente con múltiples
    entradas por la frecuencia del apellido
```

**Paso 4 — investiga los 97 de reparación.**

```text
CAMPO QUE FALTA
  dirección del beneficiario incompleta        58
  propósito del pago ausente                   22
  identificador del beneficiario mal formado   17

LOS 58 SON EL HALLAZGO
  el formulario del banco ordenante pedía
  «dirección» en un campo de texto libre de 35 caracteres

  el banco beneficiario exige calle, número, ciudad y país
  en campos estructurados

  → no es un error del cliente: es un formulario
    que no puede producir un mensaje válido
```

**Paso 5 — cuantifica la corrección del formulario.**

```text
SI LOS 58 DESAPARECEN
  intervenciones: 290 − 58 = 232
  ahorro: 58 × 14 = 812 USD/mes = 9 744 USD/año
  STP sube de 71,0 % a 76,8 %

COSTE DE LA CORRECCIÓN
  rediseño del formulario con campos estructurados
  y validación en origen: 22 000 USD

RETORNO SOLO POR COSTE OPERATIVO: 2,3 años
```

**Paso 6 — corrige el análisis: el coste operativo no es el argumento.**

```text
LO QUE NO ESTABA EN EL CÁLCULO
  · 58 clientes al mes con un pago retenido 19 horas
  · reclamaciones asociadas: 40 % de los casos
  · 23 reclamaciones/mes × 45 USD de gestión = 1 035 USD/mes
  · abandono estimado: 3 % de los clientes afectados
    58 × 3 % = 1,7 clientes/mes
    valor anual por cliente del corredor: 340 USD
    → 1,7 × 12 × 340 = 6 936 USD/año de ingreso perdido

RETORNO CORREGIDO
  9 744 + 12 420 + 6 936 = 29 100 USD/año
  22 000 / 29 100 = 0,76 años
```

**Paso 7 — decide y ordena.**

```text
PRIORIDAD 1 · formulario con campos estructurados
  retorno en 9 meses, y elimina la causa raíz

PRIORIDAD 2 · afinar el screening para nombres transliterados
  119 falsos positivos al mes
  requiere reglas por origen del nombre, no un umbral global
  ATENCIÓN: bajar la sensibilidad NO es la solución;
  los 2 verdaderos positivos son el motivo del control

PRIORIDAD 3 · analizar los 31 rechazos del banco beneficiario
  antes de tocarlos hay que saber POR QUÉ rechaza:
  puede ser su política, no un defecto del mensaje

NO HACER
  · reducir el número de eslabones «para ir más rápido»
    sin medir antes cuánto aporta cada uno:
    los dos días son de liquidación, no de mensajería
```

**Interpreta:** la tasa de procesamiento directo del 71 % parecía un problema de
cumplimiento, y la mayor causa corregible era **un formulario que no podía
producir un mensaje válido**. El flujo de mensaje se estaba rompiendo antes de
salir del banco ordenante.

## 🧭 Perspectivas

Cada participante ve su tramo y decide sobre él. La tabla los enfrenta.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un pago detenido sin explicación | Si reclama o cambia de banco |
| Banco ordenante | 290 intervenciones manuales | Dónde invierte |
| Corresponsal | Mensajes que hay que reparar | Si mantiene la relación |
| Banco beneficiario | Datos insuficientes para abonar | Si rechaza |
| Proveedor de screening | Volumen de coincidencias | Cómo calibra |
| Supervisor | Tasa de falsos positivos | Si exige revisar el modelo |
| Auditor | 2 verdaderos positivos | Si el control funciona |
| Sociedad | Corredores que se cierran | Riesgo de exclusión |

## 🏦 Del cliente al banco

El cliente pregunta dónde está su dinero y el banco solo conoce su propio tramo. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Mi pago está detenido» | Screening con 80 % de falsos positivos | 18, clases 2 y 12 |
| «Me pidieron la dirección otra vez» | Campo libre que no produce mensaje válido | 18, clase 6 |
| «El mensaje salió, ¿dónde está el dinero?» | Mensaje y fondos no viajan juntos | 18, clase 5 |
| «Me lo devolvieron sin motivo» | Rechazo del banco beneficiario | 18, clase 7 |

## ⚖️ Riesgos y controles

Los riesgos vienen de la cadena y de la información parcial. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Desincronización de flujos | Fondos sin mensaje aplicable | Identificador extremo a extremo |
| Responsabilidad sin control | Se responde por un eslabón ajeno | Red acotada y acuerdos claros |
| Tercero crítico invisible | Cae el proveedor de screening | Registro de terceros y plan de salida |
| Datos insuficientes en origen | Reparación en destino | Campos estructurados con validación |
| Falsos positivos masivos | Cola manual y demora | Calibración por origen, no umbral global |
| Corresponsal único | El corredor se cierra | Redundancia probada |

## 🧪 Práctica

En [`labs/lab-01.md`](../labs/lab-01.md) y [`labs/lab-04.md`](../labs/lab-04.md):

1. Traza los cuatro flujos de un pago con tres eslabones.
2. Identifica en qué punto se rompe cada uno en cuatro incidentes dados.
3. Calcula la tasa de procesamiento directo y su descomposición por causa.
4. Prioriza tres correcciones con su retorno, incluido el efecto sobre el cliente.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen pagos perdidos o retrasados. La causa es casi siempre un intermediario que nadie eligió.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Un solo diagrama para el pago | Se dibujó solo el mensaje | Traza los cuatro flujos |
| Bajar la sensibilidad del screening | Se optimizó la cola | Calibra, no desactives |
| Compromiso sobre el plazo medio | El promedio esconde la cola | Usa percentiles |
| Culpar al cliente de los datos | El formulario no permitía otra cosa | Revisa el origen del dato |
| Ignorar proveedores críticos | No tienen relación con el cliente | Inclúyelos en el mapa |
| Acortar la cadena sin medir | Se asumió que el retraso era mensajería | Mide dónde está el tiempo |

## ❓ Preguntas de comprobación

1. ¿Cuáles son los cuatro flujos y qué falla característico tiene cada uno?
2. ¿Qué diferencia hay entre pago en serie y con cobertura, y qué riesgo añade
   el segundo?
3. ¿Por qué el banco ordenante responde ante su cliente por un fallo de un banco
   con el que no tiene contrato?
4. En el ejemplo guiado, ¿por qué el formulario era la causa raíz y no el
   cumplimiento?
5. ¿Por qué reducir la sensibilidad del screening no es la corrección correcta?

## 📥 Entregable

Guarda en `portfolio/parte-18/clase-02/`:

- el diagrama de los cuatro flujos de un pago con tres eslabones;
- el mapa de participantes, incluidos los dos terceros invisibles;
- el cálculo de la tasa de procesamiento directo y su descomposición;
- tres correcciones priorizadas con su retorno y su efecto sobre el cliente.

## 🔗 Referencias cruzadas

- **Viene de:** clase 1; Parte 10, clase 13; Parte 17, clase 13 (terceros
  críticos).
- **Continúa en:** clase 3 (corresponsalía), clase 5 (mensaje y fondos),
  clase 12 (cumplimiento).
- **Se aplica en:** Parte 23, clase 8 (pagos del banco digital).

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
- Financial Stability Board (2023). *Enhancing third-party risk management and oversight: a toolkit*. FSB. <https://www.fsb.org/2023/12/enhancing-third-party-risk-management-and-oversight-a-toolkit-for-financial-institutions-and-financial-authorities/>
- Committee on Payments and Market Infrastructures (2020). *Enhancing cross-border payments: building blocks of a global roadmap*. BIS. <https://www.bis.org/cpmi/publ/d193.htm>
- Wolfsberg Group. *Correspondent Banking Due Diligence Questionnaire*. <https://www.wolfsberg-group.org/>
- Committee on Payments and Market Infrastructures e IOSCO (2012). *Principles for Financial Market Infrastructures*. BIS. <https://www.bis.org/cpmi/publ/d101.htm>
- Verificación local: comprueba qué exige tu supervisor sobre gestión de terceros críticos y sobre trazabilidad de pagos internacionales. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 01 · Qué es un pago transfronterizo](01-que-es-un-pago-transfronterizo.md) | [Parte 18](../README.md) · [Programa](../../../SYLLABUS.md) | [03 · Corresponsalía bancaria →](03-corresponsalia-bancaria.md) |
<!-- gen:footer:end -->
