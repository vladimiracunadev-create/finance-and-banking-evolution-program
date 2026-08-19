<!-- meta
part: 18
class: 13
title: "Interconexión de sistemas de pagos inmediatos"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global]
regulatory_topics: [cross-border-payments, infraestructura, interoperabilidad]
regulation_last_verified: 2026-08-19
regulatory_status: en-desarrollo
primary_authorities: [CPMI, BIS Innovation Hub]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 13 · Interconexión de sistemas de pagos inmediatos

> [← 12 · AML, sanciones y regla del viaje](12-aml-sanciones-y-regla-del-viaje.md) · [Índice de la parte](../README.md) · [14 · Stablecoins y pagos internacionales →](14-stablecoins-y-pagos-internacionales.md)

**Parte 18 — Pagos transfronterizos, remesas y liquidación internacional** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Estudiar la arquitectura que más ha reducido el tiempo y el coste de un pago
transfronterizo sin usar ninguna tecnología nueva: **conectar dos sistemas de
pagos inmediatos que ya existen**.

Las doce clases anteriores describen el modelo de corresponsalía y sus costes. Esta presenta la alternativa que varios países están construyendo: conectar los sistemas nacionales entre sí y eliminar la cadena de intermediarios.

## 📚 Objetivos

Al finalizar podrás:

1. **Comparar** los tres modelos de interconexión y sus requisitos.
2. **Identificar** los seis problemas que hay que resolver para enlazar dos
   sistemas.
3. **Explicar** dónde ocurre el cambio de divisa y quién lo asume.
4. **Evaluar** qué demostró y qué no demostró cada proyecto institucional.
5. **Diseñar** el enlace bilateral de dos sistemas con sus reglas.

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

Los cuatro primeros términos son los modelos de conexión; los cuatro siguientes, lo que hace falta para que funcionen. La **armonización** es el requisito más difícil: conectar dos sistemas exige que coincidan en formatos, horarios, identificadores y reglas de finalidad, y eso es más trabajo que la conexión técnica.

| Concepto | Comprensión verificable |
|---|---|
| `sistema de pagos inmediatos` | Sistema nacional que liquida en segundos, 24/7 |
| `enlace bilateral` | Conexión directa entre dos sistemas |
| `modelo de eje` | Plataforma común a la que se conectan varios sistemas |
| `interoperabilidad` | Que dos sistemas se entiendan sin acuerdo caso a caso |
| `proveedor de liquidez` | Entidad que aporta la divisa de destino |
| `alias` | Identificador simple del beneficiario, como un teléfono |
| `armonización` | Alineación de mensajes, horarios y reglas |
| `gobernanza del enlace` | Quién decide las reglas comunes y resuelve disputas |

## 🧠 Modelo mental

El modelo mental es una alternativa a la corresponsalía: en vez de encadenar bancos, se conectan los sistemas nacionales entre sí. El pago deja de recorrer intermediarios y el problema pasa a ser la gobernanza del enlace.

```text
LA IDEA ES SENCILLA Y LO DIFÍCIL ES TODO LO DEMÁS

  cada país tiene un sistema que mueve dinero
  en segundos, las 24 horas

  si los conectas, un pago transfronterizo
  puede ser dos pagos domésticos instantáneos
  con un cambio de divisa en medio

LO QUE HAY QUE RESOLVER
  1. cómo se identifica al beneficiario del otro lado
  2. quién aporta la divisa de destino
  3. a qué tipo y quién asume el riesgo
  4. cómo se cumplen los controles de los dos países
  5. quién responde si algo falla
  6. quién decide las reglas comunes

NINGUNO DE LOS SEIS ES UN PROBLEMA TÉCNICO
```

## 📖 Desarrollo

### 1. Los tres modelos

| Modelo | Cómo funciona | Escala | Complejidad |
|---|---|---|---|
| **Bilateral** | Dos sistemas se conectan directamente | n(n−1)/2 enlaces | Baja por enlace, alta en total |
| **Eje (hub)** | Todos se conectan a una plataforma común | n enlaces | Alta al inicio, baja después |
| **Acuerdo común** | Reglas y mensajes comunes, conexión libre | n enlaces | Media; exige gobernanza fuerte |

El primero de los tres modelos tiene un problema aritmético que explica por
que los proyectos institucionales no lo eligen.

```text
EL PROBLEMA DEL MODELO BILATERAL
  con 5 sistemas: 10 enlaces
  con 20 sistemas: 190 enlaces
  cada uno con su acuerdo, su tipo de cambio,
  su reparto de responsabilidad y su calendario

  → no escala, y por eso los proyectos
    institucionales apuntan al eje o al acuerdo común
```

### 2. Cómo se resuelve la identificación

Enlazar dos sistemas nacionales obliga a resolver primero cómo se nombra al
destinatario. El bloque plantea el problema, describe la solución habitual y
enumera los dos cuidados que la hacen segura.

```text
EL PROBLEMA
  el ordenante conoce el teléfono de su familiar,
  no su número de cuenta internacional

LA SOLUCIÓN
  un servicio de resolución de alias:
  teléfono o identificador → cuenta y banco

LO QUE HAY QUE CUIDAR
  · confirmación del NOMBRE antes de pagar
    (evita el pago al beneficiario equivocado
     y es un control antifraude, Parte 17 clase 11)
  · privacidad: la resolución expone que un número
    tiene cuenta y en qué banco
  · límite de consultas: sin él, se puede enumerar
```

### 3. Dónde ocurre el cambio de divisa

En un enlace, la conversión de divisa puede colocarse en tres sitios, y la
elección determina quién asume el riesgo y quién ve el tipo. El bloque
describe los tres diseños con sus consecuencias.

```text
TRES DISEÑOS

  A · EN EL ORIGEN
      el banco ordenante compra la divisa de destino
      y envía ya convertido
      → el ordenante sabe exactamente cuánto llega
      → el banco ordenante asume el riesgo de cambio

  B · EN EL ENLACE
      un proveedor de liquidez cotiza en el momento
      → tipo competitivo por subasta entre proveedores
      → exige que alguien tenga las dos divisas

  C · EN EL DESTINO
      llega la divisa de origen y se convierte allí
      → el ordenante NO sabe cuánto llegará
      → peor para el cliente

EL DISEÑO B ES EL QUE MÁS PROMETE
Y EL QUE MÁS DEPENDE DE QUE HAYA
PROVEEDORES DE LIQUIDEZ DISPUESTOS
```

### 4. Los proyectos institucionales

Varios proyectos institucionales han probado estas ideas en pilotos
documentados. El bloque los recorre con una rejilla común y, en especial, con
la columna que más se omite al citarlos: qué NO demostraron.

```text
QUÉ MIRAR EN CADA UNO
  problema · arquitectura · participantes · activo de
  liquidación · estado · qué demostró · qué NO demostró

PROYECTO NEXUS (BIS Innovation Hub)
  problema     conectar sistemas de pagos inmediatos
               sin construir n(n−1)/2 enlaces
  arquitectura esquema y pasarela comunes; modelo de eje
  activo       moneda de banco central de cada sistema
  demostró     que un enlace estandarizado es viable
               y que el diseño B de cambio funciona
  NO demostró  operación a escala global en producción

PROYECTO mBRIDGE
  problema     pagos transfronterizos mayoristas
  arquitectura plataforma común multi-CBDC
  activo       monedas digitales de banco central mayoristas
  demostró     liquidación casi instantánea entre
               participantes de varias jurisdicciones
  NO demostró  gobernanza duradera ni escala

PROYECTOS JURA, DUNBAR, MARIANA, AGORÁ, MERIDIAN FX, RIALTO
  cada uno aborda una pieza distinta: PvP mayorista,
  plataforma multi-CBDC, creación automatizada de mercado
  de divisas, corresponsalía tokenizada, sincronización
  de liquidación y liquidación de FX mayorista

REGLA DEL PROGRAMA
  ninguno de estos proyectos es un sistema en producción
  a escala global. Son PRUEBAS DE CONCEPTO o pilotos.
  Presentarlos como infraestructura operativa es el error
  más común al citarlos.
  Verifica el estado de cada uno en la fuente antes de
  usarlo en una decisión.
```

### 5. Lo que un enlace no resuelve

Un enlace mejora el tramo técnico y deja intacto todo lo demás. El bloque
separa lo que resuelve de la lista de problemas que siguen ahí, para calibrar
qué se puede prometer al presentar uno.

```text
UN ENLACE ENTRE DOS SISTEMAS RESUELVE
  velocidad, coste y transparencia del tramo

NO RESUELVE
  · el cumplimiento: cada país aplica el suyo
  · la protección al consumidor: ¿qué ley se aplica?
  · las disputas: ¿quién arbitra?
  · los límites de importe de cada sistema
  · la inclusión: si el receptor no tiene cuenta,
    el enlace no le sirve
  · la liquidez: alguien tiene que tener las dos divisas

  → el enlace baja el coste del tramo técnico
    y deja intacto el coste de todo lo demás
```

## 🧮 Ejemplo guiado

El ejemplo compara un pago por corresponsalía y otro por enlace directo. La diferencia en coste y en plazo es de orden de magnitud.

**Situación.** Dos bancos centrales evalúan enlazar sus sistemas de pagos
inmediatos. Hay que decidir el diseño y estimar el efecto.

```text
CORREDOR: país P → país Q
  remesas anuales                       860 000 000 USD
  operaciones anuales                     2 900 000
  ticket medio                                  297 USD
  coste medio actual                            7,9 %
  tiempo medio actual                         26 horas

SISTEMAS
  P: pagos inmediatos, 24/7, límite 5 000 USD equivalente
  Q: pagos inmediatos, 24/7, límite 2 000 USD equivalente

INFRAESTRUCTURA
  cobertura de cuentas o billeteras en Q:   74 %
  resolución por alias en ambos:            sí
  ISO 20022 en ambos:                       sí

PROVEEDORES DE LIQUIDEZ INTERESADOS: 4
```

**Paso 1 — comprueba la compatibilidad básica.**

```text
LÍMITE DE IMPORTE
  el enlace queda acotado por el MENOR: 2 000 USD
  ¿cuántas operaciones caben?
  ticket medio 297, con distribución sesgada a la baja
  supuesto: 96 % de las operaciones bajo 2 000
  → 2 784 000 operaciones elegibles

COBERTURA EN DESTINO
  74 % tiene cuenta o billetera
  → 2 060 160 operaciones alcanzables
  = 71 % del corredor
```

**Paso 2 — estima el coste con el enlace.**

```text
COMPONENTES DEL COSTE NUEVO
  comisión del banco ordenante          1,20 USD
  comisión del sistema de P             0,05 USD
  comisión del enlace                   0,08 USD
  comisión del sistema de Q             0,04 USD
  comisión del banco beneficiario       0,60 USD
  diferencial de cambio (diseño B)      45 pb
  SUBTOTAL FIJO                         1,97 USD
  SOBRE TICKET DE 297                   1,97 + 1,34 = 3,31 USD
  COSTE PORCENTUAL                      1,11 %

FRENTE AL 7,9 % ACTUAL: −6,79 puntos
```

**Paso 3 — comprueba el supuesto del diferencial.**

```text
45 pb SUPONE COMPETENCIA ENTRE 4 PROVEEDORES

  ¿QUÉ PASA SI SOLO SE PRESENTA UNO?
    sin competencia, el diferencial puede ser
    de 200 pb o más

  MODELADO
    4 proveedores:   45 pb → coste total 1,11 %
    2 proveedores:  110 pb → coste total 1,32 %
    1 proveedor:    250 pb → coste total 1,79 %

  INCLUSO EN EL PEOR CASO, 1,79 % FRENTE A 7,9 %

  → el resultado es ROBUSTO al número de proveedores
    → la decisión no depende de ese supuesto
```

**Paso 4 — calcula el ahorro para las familias.**

```text
OPERACIONES ALCANZABLES: 2 060 160
VOLUMEN ALCANZABLE: 2 060 160 × 297 = 611 867 520 USD

AHORRO CON EL ESCENARIO CENTRAL (1,11 %)
  611 867 520 × (7,9 % − 1,11 %) = 41 545 806 USD/año

POR FAMILIA
  suponiendo 12 envíos al año por remitente:
  171 680 remitentes
  ahorro por remitente: 242 USD/año

  sobre un envío anual de 3 564 USD:
  el 6,8 % de su envío deja de ser coste
```

**Paso 5 — enfrenta lo que el enlace NO resuelve.**

```text
EL 29 % DEL CORREDOR QUEDA FUERA

  26 % por no tener cuenta ni billetera en destino
   3 % por superar el límite de 2 000 USD

  PARA ESOS
    el coste sigue siendo 7,9 %
    y probablemente SUBA: los operadores actuales
    pierden el 71 % de su volumen y sus costes fijos
    se reparten entre menos operaciones

  EFECTO ESTIMADO
    coste del segmento excluido: de 7,9 % a ~9,5 %

  → el enlace mejora mucho al 71 % y EMPEORA al 29 %,
    que es justamente el segmento más vulnerable
```

**Paso 6 — diseña la mitigación.**

```text
MEDIDA 1 · elevar el límite del sistema de Q
  de 2 000 a 5 000 recupera el 3 %
  decisión del banco central de Q, no del enlace

MEDIDA 2 · entrega en efectivo desde el enlace
  el pago llega instantáneo a un agente en destino
  y el receptor retira sin cuenta
  → recupera una parte del 26 %
  → coste mayor que cuenta a cuenta, pero muy inferior
    al 9,5 % del canal actual

MEDIDA 3 · apertura simplificada de billetera
  el receptor abre una billetera básica al recibir
  su primer pago
  → convierte el enlace en una palanca de inclusión

SIN LA MEDIDA 2 O LA 3, EL ENLACE AUMENTA
LA DESIGUALDAD DENTRO DEL CORREDOR
```

**Paso 7 — decide y fija las reglas.**

```text
CONSTRUIR EL ENLACE, EN MODELO BILATERAL CON
DISEÑO DE CAMBIO EN EL ENLACE, Y CON TRES CONDICIONES

  1. la medida 2 o la 3 entra EN LA FASE 1,
     no «más adelante»
  2. mínimo de dos proveedores de liquidez activos;
     si queda uno, se revisa el modelo de cotización
  3. reglas escritas antes de operar:
       · qué ley se aplica a la operación
       · quién responde ante un pago no autorizado
       · plazo y procedimiento de devolución
       · quién arbitra una disputa
       · qué pasa si un sistema cae

  Y UNA REGLA DE COMUNICACIÓN
    no presentar el enlace como «pagos internacionales
    instantáneos» sin decir que cubre el 71 % del corredor
    y bajo qué condiciones. La cifra honesta sostiene
    la credibilidad del proyecto mejor que el titular.
```

**Interpreta:** el enlace reducía el coste de 7,9 % a 1,11 % y el análisis
importante no fue ese: fue **qué pasaba con el 29 % que quedaba fuera**. Una
mejora que empeora la situación del segmento más vulnerable no es una mejora
completa, y la mitigación tenía que entrar en la fase 1.

## 🧭 Perspectivas

La interconexión afecta a cada participante de forma distinta, y a algunos les quita negocio. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Remitente | Coste del 1,1 % y llegada en segundos | Si usa el canal |
| Receptor sin cuenta | Nada cambia, o empeora | Si sigue en el canal informal |
| Banco de P | Menos margen por operación | Si participa |
| Operador de remesas actual | Pierde el 71 % del volumen | Si se reconvierte |
| Proveedor de liquidez | Nuevo mercado de divisa | Si cotiza |
| Banco central de P y Q | Reglas comunes y gobernanza | Cómo lo acuerdan |
| Supervisor | Qué ley aplica a la operación | Qué exige antes de autorizar |
| Sociedad | 41 millones de ahorro anual | Y una brecha que puede crecer |

## 🏦 Del cliente al banco

El cliente recibe el dinero en segundos y el sistema resolvió liquidez y divisa por detrás. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Llegó en segundos» | Dos pagos domésticos y un cambio | 18, clase 13 |
| «Solo puedo enviar 2 000» | Límite del sistema de destino | 18, clase 13 |
| «Mi familia no tiene cuenta» | Cobertura de la última milla | 18, clase 10 |
| «¿Y si me equivoco de número?» | Confirmación de nombre antes de pagar | 18, clase 13 |

## ⚖️ Riesgos y controles

Los riesgos son de gobernanza y de liquidez del enlace. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Exclusión del segmento sin cuenta | El enlace solo sirve a quien ya tiene | Entrega en efectivo o billetera básica |
| Proveedor único de liquidez | Diferencial sin presión | Mínimo de dos y revisión del modelo |
| Ley aplicable indefinida | Disputa sin foro | Reglas escritas antes de operar |
| Enumeración por alias | Se descubre quién tiene cuenta | Límite de consultas y confirmación de nombre |
| Caída de un sistema | El enlace queda a medias | Procedimiento de contingencia acordado |
| Comunicación exagerada | Se promete cobertura total | Publicar la cobertura real |

## 🧪 Práctica

El laboratorio pide comparar los dos modelos sobre el mismo corredor. La armonización necesaria es lo que hay que enumerar.

En [`labs/lab-06.md`](../labs/lab-06.md):

1. Diseña un enlace bilateral con sus seis problemas resueltos.
2. Compara los tres diseños de cambio de divisa y elige uno con su motivo.
3. Calcula la cobertura real del corredor y el efecto sobre el segmento excluido.
4. Escribe las cinco reglas mínimas del acuerdo antes de operar.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen enlaces que no funcionan. Las causas son armonización incompleta y gobernanza sin acordar.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| «Conectamos y ya está» | Se vio solo el problema técnico | Seis problemas, cinco no técnicos |
| Modelo bilateral para muchos | No se contaron los enlaces | n(n−1)/2 no escala |
| Cambio en el destino | Se simplificó el diseño | El ordenante no sabe cuánto llega |
| Citar un piloto como producción | Se leyó el titular | Verifica el estado en la fuente |
| Ignorar el segmento excluido | Se midió la media | Mide qué pasa con quien queda fuera |
| Prometer cobertura total | Se comunicó el mejor caso | Publica la cobertura real |

## ❓ Preguntas de comprobación

1. ¿Cuáles son los tres modelos de interconexión y por qué el bilateral no
   escala?
2. ¿Cuáles son los seis problemas de un enlace y cuántos son técnicos?
3. ¿Dónde puede ocurrir el cambio de divisa y cuál es mejor para el cliente?
4. ¿Qué demostró y qué no demostró cada proyecto institucional citado?
5. En el ejemplo guiado, ¿por qué el análisis importante fue sobre el 29 %?

## 📥 Entregable

Guarda en `portfolio/parte-18/clase-13/`:

- el diseño de un enlace bilateral con los seis problemas resueltos;
- la comparación de los tres diseños de cambio, con la elección justificada;
- el cálculo de cobertura real y del efecto sobre el segmento excluido;
- la ficha de un proyecto institucional con qué demostró y qué no.

## 🔗 Referencias cruzadas

- **Viene de:** clases 5, 8, 9 y 10; Parte 17, clase 2 (esquemas y gobernanza).
- **Continúa en:** clase 14 (stablecoins), clase 15 (pago contra pago).
- **Se aplica en:** Parte 21, clase 15; Parte 23, clases 8 y 9.

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

- BIS Innovation Hub. *Project Nexus: enabling instant cross-border payments*. BIS. Modelo de interconexión que la clase analiza en detalle. <https://www.bis.org/about/bisih/topics/fmis/nexus.htm>
- BIS Innovation Hub. *Project mBridge, Project Jura, Project Dunbar, Project Mariana, Project Agorá y Project Rialto*. BIS. Experimentos de interconexión y liquidación transfronteriza. <https://www.bis.org/about/bisih/topics.htm>
- Committee on Payments and Market Infrastructures (2022). *Interlinking payment systems and the role of application programming interfaces*. BIS. Papel de las interfaces en la interconexión de sistemas. <https://www.bis.org/cpmi/publ/d205.htm>
- Committee on Payments and Market Infrastructures (2021). *Developing a technical standard for cross-border payments*. BIS. Estándar técnico común exigido por la interconexión. <https://www.bis.org/cpmi/publ/d199.htm>
- Financial Stability Board. *Informes de avance de la hoja de ruta del G20*. FSB. Avance medido de la hoja de ruta y sus metas. <https://www.fsb.org/work-of-the-fsb/financial-innovation-and-structural-change/cross-border-payments/>
- Verificación local: comprueba el estado actual de cada proyecto citado y si tu jurisdicción participa en algún enlace, con sus límites y reglas. **Fecha de verificación de esta clase: 2026-08-19.** Esta clase no constituye asesoría legal.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 12 · AML, sanciones y regla del viaje](12-aml-sanciones-y-regla-del-viaje.md) | [Parte 18](../README.md) · [Programa](../../../SYLLABUS.md) | [14 · Stablecoins y pagos internacionales →](14-stablecoins-y-pagos-internacionales.md) |
<!-- gen:footer:end -->
