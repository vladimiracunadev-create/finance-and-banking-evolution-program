---
part: 21
class: 5
title: "Ciclo de vida del instrumento"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [eventos-corporativos, operaciones, riesgo-operacional]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [CPMI, IOSCO, ISO]
requires_legal_review: false
---

<!-- gen:header:start -->
# Clase 05 · Ciclo de vida del instrumento

> [← 04 · Emisión: mercado primario tokenizado](04-emision-mercado-primario-tokenizado.md) · [Índice de la parte](../README.md) · [06 · Mercado secundario y liquidez prometida →](06-mercado-secundario-y-liquidez-prometida.md)

**Parte 21 — Tokenización, FX on-chain y mercados programables** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Recorrer la vida del instrumento después de la emisión: cupones, amortizaciones,
canjes, embargos y vencimiento. **Es donde se rompen los proyectos**, porque la
emisión se prueba y el ciclo de vida se improvisa.

La emisión de la clase anterior es un día. Esta trata los años siguientes, que es donde fallan casi todos los diseños: cupones, opciones, embargos y amortizaciones que nadie modeló porque la emisión ya funcionaba.

## 📚 Objetivos

Al finalizar podrás:

1. **Enumerar** los eventos del ciclo de vida y cuáles son programables.
2. **Diseñar** el pago de un cupón con su fecha de corte y su reintento.
3. **Explicar** por qué un embargo no puede programarse y qué se hace en su
   lugar.
4. **Calcular** el efecto de un error en la fecha de corte.
5. **Especificar** el procedimiento de vencimiento y destrucción del
   instrumento.

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

Los cuatro primeros términos son los eventos corporativos y su fecha; los cuatro siguientes, los casos difíciles y el final del instrumento. El **embargo** es el evento que ningún diseño automatiza bien: una orden judicial exige inmovilizar sin transferir, y eso no es un pago programado.

| Concepto | Comprensión verificable |
|---|---|
| `evento corporativo` | Hecho que altera el instrumento o sus derechos |
| `fecha de corte` | Momento que fija quién tiene derecho |
| `evento obligatorio` | Se aplica a todos sin opción |
| `evento con opción` | El tenedor elige entre alternativas |
| `reintento` | Nuevo intento de un pago que falló |
| `embargo` | Inmovilización ordenada por una autoridad |
| `amortización parcial` | Devolución de parte del principal |
| `destrucción` | Retirada definitiva del instrumento del registro |

## 🧠 Modelo mental

El modelo mental es que la emisión se prueba y el ciclo de vida se improvisa. Un instrumento vive años y durante esos años hay pagos, opciones, embargos y amortizaciones, y casi todos los diseños se detienen en la emisión.

```text
TRES FAMILIAS DE EVENTOS

  PROGRAMABLES POR COMPLETO
    cupón fijo, amortización a vencimiento,
    devengo de intereses
    → la condición es el calendario, y el
      calendario se conoce

  PROGRAMABLES CON DATO EXTERNO
    cupón variable, dividendo, canje por
    ratio de mercado
    → exigen un oráculo, y con él vuelven
      los problemas de la Parte 19, clase 9

  NO PROGRAMABLES
    embargo, orden judicial, sucesión,
    fusión, concurso del emisor
    → vienen de fuera del sistema y exigen
      una vía humana con autorización

EL ERROR TÍPICO ES DISEÑAR SOLO
LA PRIMERA FAMILIA.
```

## 📖 Desarrollo

### 1. El cupón, paso a paso

```text
1 SE FIJA LA FECHA DE CORTE
    y se publica con antelación

2 SE CONGELA EL REGISTRO A ESA HORA
    o se toma una instantánea verificable
    (Parte 19, clase 4)

3 SE CALCULA EL IMPORTE POR TITULAR
    con la base de cálculo declarada

4 SE APROVISIONA EL DINERO
    y aquí está el primer punto de fallo:
    si el dinero no está, el contrato no
    puede pagar por mucho que esté programado

5 SE EJECUTA EL PAGO
    contra el registro de la instantánea

6 SE REGISTRAN LOS FALLOS
    titulares no localizables, cuentas
    bloqueadas, importes por debajo del mínimo

7 SE REINTENTA
    con un calendario declarado y un límite

8 SE CONSIGNA LO NO COBRADO
    según el procedimiento del emisor
```

### 2. Por qué la fecha de corte es crítica

```text
ENTRE LA FECHA DE CORTE Y EL PAGO
EL INSTRUMENTO SIGUE NEGOCIÁNDOSE

  quien compra después del corte
  NO cobra ese cupón
  → el precio debe reflejarlo

SI EL REGISTRO NO MARCA ESA DIFERENCIA
  el comprador cree que compra con cupón
  y recibe un instrumento sin él

QUÉ EXIGE EL DISEÑO
  · marcar el instrumento como «sin cupón»
    entre el corte y el pago
  · publicar el corte con antelación suficiente
  · que la plataforma muestre ambos precios

Y SI HAY DOS REGISTROS (clase 2),
la fecha de corte debe tomarse en el de
referencia, no en el que sea más cómodo.
```

### 3. Lo que no se puede programar

```text
UN EMBARGO ES UNA ORDEN DE UNA AUTORIDAD
SOBRE UN TITULAR CONCRETO

  · no se conoce de antemano
  · no tiene una condición verificable en
    el registro
  · su alcance lo determina un tercero
  · puede ser parcial, temporal o condicional

LO QUE SE DISEÑA EN SU LUGAR

  una FUNCIÓN DE INMOVILIZACIÓN
  · activable solo por una función designada
  · con doble aprobación
  · que solo INMOVILIZA: no transfiere
    ni altera saldos
  · con registro inmutable del quién,
    cuándo y en virtud de qué

ES EL INTERRUPTOR DE LA PARTE 19, CLASE 8,
aplicado a un titular en vez de al contrato.
```

### 4. Eventos con opción

```text
EL TENEDOR ELIGE: CANJE, SUSCRIPCIÓN
PREFERENTE, COBRO EN EFECTIVO O EN TÍTULOS

  PROBLEMA
    hay que recoger la instrucción de miles
    de tenedores en un plazo, y aplicar
    una opción por defecto a quien no responda

  DISEÑO
    · plazo declarado y recordatorios
    · opción por defecto explícita en el folleto
    · instrucción revocable hasta el cierre
    · publicación del recuento antes de ejecutar

  RIESGO ESPECÍFICO DEL FRACCIONAMIENTO
    una opción que exige unidades enteras
    deja fuera a quien tiene fracciones
    → hay que decidir qué pasa con ellas
      ANTES, no cuando ocurra
```

### 5. Vencimiento y destrucción

```text
AL VENCIMIENTO

  1 se paga el principal y el último cupón
  2 se marca el instrumento como vencido
  3 se destruyen las unidades
  4 se conserva el registro histórico
     durante el plazo legal

QUÉ SE HACE MAL CON FRECUENCIA
  · destruir las unidades antes de confirmar
    el pago → el tenedor se queda sin nada
  · no destruirlas → siguen negociándose
    unidades de un instrumento que ya no existe
  · borrar el registro histórico → se pierde
    la trazabilidad exigida

ORDEN CORRECTO
  pago confirmado → marcado → destrucción
  y nunca al revés
```

## 🧮 Ejemplo guiado

El ejemplo procesa varios eventos corporativos sobre el mismo instrumento, incluido un embargo. Conviene fijarse en el evento con opción: exige recoger la decisión de cada tenedor en un plazo.

**Situación.** Un bono tokenizado de 30 000 000 paga cupón semestral del 6,4 %
anual. Hay que ejecutar el segundo cupón, con incidencias.

```text
DATOS
  nominal vivo                   30 000 000
  cupón anual                          6,4 %
  periodicidad                     semestral
  titulares                            4 120
  fecha de corte             día 178, 18:00
  fecha de pago              día 182
  titulares con cuenta bloqueada          37
  titulares no localizables               14
  importe mínimo de pago                   1
```

**Paso 1 — calcula el cupón total.**

```text
CUPÓN SEMESTRAL
  30 000 000 × 6,4 % / 2 = 960 000

POR UNIDAD (30 000 unidades de 1 000)
  960 000 / 30 000 = 32 por unidad
```

**Paso 2 — mide el efecto de un error de una hora en el corte.**

```text
SUPUESTO · SE TOMA LA INSTANTÁNEA A LAS 19:00
EN VEZ DE LAS 18:00

  operaciones en esa hora: 46
  volumen: 214 unidades

  CONSECUENCIA
  46 pares de titulares con el cobro cambiado
  importe afectado: 214 × 32 = 6 848

  ¿ES POCO? El importe sí.
  El problema no es el importe: es que
  46 tenedores recibieron lo que no les
  correspondía y 46 no recibieron lo suyo,
  y corregirlo exige recuperar dinero ya pagado.

COSTE DE CORRECCIÓN
  supuesto: 92 gestiones × 85 = 7 820
  → MÁS QUE EL IMPORTE EN DISPUTA
```

**Paso 3 — aprovisiona y detecta el fallo previo.**

```text
DINERO APROVISIONADO POR EL EMISOR
  955 000

NECESARIO
  960 000

  FALTAN 5 000

QUÉ HACE UN CONTRATO BIEN DISEÑADO
  · comprueba el aprovisionamiento ANTES
    de empezar a pagar
  · si no alcanza, NO PAGA A NADIE
    y emite una alerta

QUÉ HACE UNO MAL DISEÑADO
  · empieza a pagar por orden y se queda
    sin fondos a mitad
  → 156 titulares cobran y 3 964 no,
    sin ningún criterio

ES EL MISMO PRINCIPIO DE LA PARTE 20,
CLASE 5: el orden de llegada no reparte,
discrimina.
```

**Paso 4 — ejecuta con el aprovisionamiento corregido.**

```text
APROVISIONADO 960 000

  titulares que cobran: 4 120 − 37 − 14 = 4 069
  importe pagado: supuesto 946 300

  pendiente por cuentas bloqueadas: 9 100
  pendiente por no localizables:     4 600
  TOTAL PENDIENTE: 13 700
```

**Paso 5 — diseña el reintento.**

```text
CALENDARIO DE REINTENTO DECLARADO

  cuentas bloqueadas
    reintento a los 5, 15 y 30 días
    tras el desbloqueo, pago inmediato

  no localizables
    notificación por los canales declarados
    conservación del importe durante el
    plazo legal
    consignación al vencer ese plazo

LO QUE NO SE HACE
  · reintentar indefinidamente y de forma
    automática, porque cada intento fallido
    tiene coste y ruido
  · devolver el importe al emisor sin plazo,
    porque el derecho del tenedor subsiste
```

**Paso 6 — resuelve un embargo llegado el día 180.**

```text
ORDEN JUDICIAL SOBRE UN TITULAR CON
1 200 UNIDADES, RECIBIDA EL DÍA 180

  la fecha de corte fue el 178:
  ese titular TIENE derecho al cupón

  PROCEDIMIENTO
  1 la función designada inmoviliza las
    1 200 unidades, con doble aprobación
  2 el cupón correspondiente (38 400)
    NO se paga al titular: se consigna
    a disposición de la autoridad
  3 se registra el quién, cuándo y en virtud
    de qué
  4 se comunica al titular

LO QUE NO SE HACE
  · transferir las unidades a nadie
  · anular el derecho al cupón
  · aplicar el embargo antes de recibirlo
    por el cauce formal
```

**Paso 7 — comprueba el orden en el vencimiento.**

```text
SIMULACIÓN DEL VENCIMIENTO

  1 aprovisionar 30 000 000 + último cupón
  2 verificar aprovisionamiento completo
  3 tomar instantánea a la fecha de corte
  4 pagar
  5 CONFIRMAR el pago de cada titular
  6 marcar el instrumento como vencido
  7 destruir SOLO las unidades cuyo pago
    está confirmado
  8 mantener vivas las de pagos pendientes
    hasta resolverlos

EL PASO 7 ES EL QUE SE HACE MAL:
destruir todas a la vez deja sin instrumento
a quien todavía no ha cobrado, y con él
sin prueba de su derecho.
```

**Interpreta:** el error de una hora en la fecha de corte costó más corregirlo
que el importe en disputa, y el aprovisionamiento insuficiente habría dividido a
los tenedores en dos grupos sin ningún criterio. **La emisión se prueba y el
ciclo de vida se improvisa**, y es en el ciclo de vida donde vive el riesgo.

## 🧭 Perspectivas

El ciclo de vida afecta a cada participante de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un cupón que llega o no | Si reclama |
| Inversionista | Precio con o sin cupón | Cuándo compra |
| Emisor | Un pago que ejecutar | Cómo aprovisiona |
| Agente de pagos | Incidencias por resolver | Qué reintenta |
| Custodio | Instrucciones de eventos con opción | Cómo las recoge |
| Plataforma | Instantánea y ejecución | Cómo la verifica |
| Autoridad | Un embargo que ejecutar | Sobre qué registro |
| Supervisor | Un evento mal aplicado | Qué exige corregir |
| Auditor | Trazabilidad del pago | Qué muestrea |
| Sociedad | Derechos que se cumplen | Qué certeza espera |

## 🏦 Del cliente al banco

El tenedor espera cobrar un cupón y el sistema tiene que ejecutar un evento con fecha de corte. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «No me llegó el cupón» | Cuenta bloqueada, con reintento programado | 21, clase 5 |
| «Compré antes del pago» | Después del corte: el cupón no era suyo | 21, clase 5 |
| «Es automático, no falla» | Falla si el emisor no aprovisiona | 21, clase 5 |

## ⚖️ Riesgos y controles

Los riesgos son de eventos no previstos y de reintentos. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Fecha de corte errónea | Cobra quien no debía | Instantánea verificable y publicada |
| Aprovisionamiento insuficiente | Se paga a unos y a otros no | Verificar antes de empezar a pagar |
| Embargo aplicado mal | Se transfiere o se anula un derecho | Función que solo inmoviliza |
| Opción sin defecto declarado | Quien no responde queda indefinido | Opción por defecto en el folleto |
| Destrucción anticipada | El tenedor pierde la prueba de su derecho | Destruir solo lo pagado y confirmado |
| Reintento indefinido | Coste y ruido crecientes | Calendario declarado con límite |

## 🧪 Práctica

El laboratorio pide procesar un año de eventos corporativos. El embargo y el evento con opción son los que deciden el ejercicio.

En [`labs/lab-02.md`](../labs/lab-02.md):

1. Implementa el pago de cupón con instantánea y verificación previa.
2. Provoca un aprovisionamiento insuficiente y comprueba que no paga a nadie.
3. Aplica un embargo con la función de inmovilización y su registro.
4. Ejecuta el vencimiento con destrucción solo de lo confirmado.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen eventos mal procesados. La causa es haber diseñado solo la emisión.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Diseñar solo lo programable | Es lo que se puede probar | Los eventos de fuera son los que rompen |
| Pagar sin verificar fondos | El contrato «ya paga» | Verificar antes de empezar |
| Corte tomado donde conviene | Hay dos registros | Se toma en el de referencia |
| Programar el embargo | Se busca automatizarlo todo | Solo se diseña la inmovilización |
| Destruir todo al vencer | Es lo ordenado | Solo lo pagado y confirmado |
| Sin opción por defecto | Se asume que todos responden | La mayoría no responde |

## ❓ Preguntas de comprobación

1. ¿Cuáles son las tres familias de eventos y cuál se diseña peor?
2. ¿Por qué la fecha de corte necesita marcar el instrumento como sin cupón?
3. ¿Qué se diseña en lugar de programar un embargo?
4. ¿Por qué hay que verificar el aprovisionamiento antes de pagar?
5. ¿Cuál es el orden correcto de vencimiento y por qué importa el paso 7?

## 📥 Entregable

Guarda en `portfolio/parte-21/clase-05/`:

- el procedimiento de cupón en ocho pasos, con su calendario de reintento;
- el cálculo del efecto de un error de una hora en el corte;
- el diseño de la función de inmovilización con su doble aprobación;
- la secuencia de vencimiento con la regla de destrucción.

## 🔗 Referencias cruzadas

- **Viene de:** clases 2, 3 y 4; Parte 19, clase 8.
- **Continúa en:** clases 8 y 9 de esta parte.
- **Se aplica en:** Parte 22, clase 12; Parte 23, clases 8 y 12.

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

- CPMI e IOSCO (2012). *Principles for Financial Market Infrastructures*. BIS. <https://www.bis.org/cpmi/publ/d101.htm>
- ISO 20022. *Corporate Actions message definitions*. ISO 20022. <https://www.iso20022.org/iso-20022-message-definitions>
- IOSCO (2023). *Policy Recommendations for Crypto and Digital Asset Markets*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- Committee on Payments and Market Infrastructures (2024). *Tokenisation in the context of money and other assets*. BIS. <https://www.bis.org/cpmi/publ/d225.htm>
- Verificación local: comprueba qué plazos de prescripción y qué procedimiento de consignación aplican en tu jurisdicción a los importes no cobrados. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 04 · Emisión: mercado primario tokenizado](04-emision-mercado-primario-tokenizado.md) | [Parte 21](../README.md) · [Programa](../../../SYLLABUS.md) | [06 · Mercado secundario y liquidez prometida →](06-mercado-secundario-y-liquidez-prometida.md) |
<!-- gen:footer:end -->
