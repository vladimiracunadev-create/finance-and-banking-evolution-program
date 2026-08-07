---
part: 21
class: 3
title: "Derechos económicos y políticos del tenedor"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [chile, internacional]
regulatory_topics: [valores, proteccion-al-inversionista, gobierno-corporativo]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [IOSCO, CMF, OCDE]
requires_legal_review: true
---

<!-- gen:header:start -->
# Clase 03 · Derechos económicos y políticos del tenedor

> [← 02 · El registro de referencia](02-el-registro-de-referencia.md) · [Índice de la parte](../README.md) · [04 · Emisión: mercado primario tokenizado →](04-emision-mercado-primario-tokenizado.md)

**Parte 21 — Tokenización, FX on-chain y mercados programables** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Especificar **qué puede exigir el tenedor y a quién**. Un token que no dice qué
derechos otorga no es un instrumento financiero incompleto: es un instrumento
distinto del que el inversionista cree tener.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** derechos económicos, políticos y de información.
2. **Determinar** contra quién se ejerce cada derecho en una cadena con
   envoltorio.
3. **Diseñar** el ejercicio de un derecho político sobre un instrumento
   tokenizado.
4. **Calcular** el efecto del fraccionamiento sobre los derechos con umbral.
5. **Identificar** los derechos que se pierden por diseño y no por norma.

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
| `derecho económico` | Cobrar: cupón, dividendo, amortización, liquidación |
| `derecho político` | Decidir: voto, impugnación, convocatoria |
| `derecho de información` | Saber: cuentas, hechos esenciales, registro |
| `titularidad indirecta` | El derecho se ejerce a través de un intermediario |
| `derecho con umbral` | Requiere un porcentaje mínimo del capital |
| `fecha de corte` | Momento que fija quién tiene derecho |
| `agrupación de votos` | Ejercicio conjunto por un representante |
| `derecho perdido por diseño` | La norma lo concede y la arquitectura lo impide |

## 🧠 Modelo mental

```text
TRES FAMILIAS Y UNA PREGUNTA POR CADA UNA

  ECONÓMICOS   ¿quién paga, cuándo y a quién
               según qué registro?

  POLÍTICOS    ¿quién vota, cómo se acredita
               y con qué fecha de corte?

  INFORMACIÓN  ¿a quién se informa, por qué canal
               y con qué antelación?

Y UNA CUARTA, TRANSVERSAL:

  ¿CONTRA QUIÉN SE EJERCE?
    contra el emisor            → titularidad directa
    contra un intermediario     → indirecta
    contra un vehículo          → hay un envoltorio

  CADA ESLABÓN AÑADE UN OBLIGADO
  Y UNA POSIBILIDAD DE QUE EL DERECHO
  SE QUEDE POR EL CAMINO.
```

## 📖 Desarrollo

### 1. Los económicos son los fáciles

```text
CUPÓN, DIVIDENDO, AMORTIZACIÓN

  el problema no es el derecho: es la
  fecha de corte y el registro que la fija

  · si el registro de referencia es el oficial,
    la fecha de corte se toma allí
  · si es el token, allí
  · si no está decidido (clase 2), habrá
    quien cobre dos veces y quien no cobre

PROGRAMAR EL PAGO NO ELIMINA EL PROBLEMA
  el contrato paga a quien figure en el token
  a una hora dada; si el registro oficial dice
  otra cosa, el pago fue a quien no debía
  y hay que recuperarlo
```

### 2. Los políticos son los difíciles

```text
POR QUÉ EL VOTO SE COMPLICA

  · la titularidad puede ser indirecta:
    el que aparece en el registro es un
    custodio, no el inversionista

  · la fecha de corte del voto y la del
    dividendo no tienen por qué coincidir

  · un instrumento fraccionado multiplica
    los titulares y con ellos el coste
    de acreditar a cada uno

  · el préstamo del valor separa el voto
    de la exposición económica

QUÉ PERMITE UN REGISTRO PROGRAMABLE
  · acreditar la tenencia a la fecha de corte
    sin pedir certificados
  · votar directamente sin cadena de
    instrucciones
  · publicar el resultado verificable

QUÉ NO RESUELVE
  · quién puede votar, que lo decide la norma
  · el préstamo de valores para votar,
    que sigue siendo posible
```

### 3. Los derechos con umbral

```text
MUCHOS DERECHOS EXIGEN UN PORCENTAJE

  convocar una junta
  impugnar un acuerdo
  pedir información adicional
  designar un auditor
  ejercer acciones de responsabilidad

EFECTO DEL FRACCIONAMIENTO
  bajar el mínimo de 100 000 a 100 multiplica
  los titulares por mil
  → cada uno tiene una milésima del peso
  → NINGUNO alcanza el umbral

  el derecho existe en la norma
  y es inalcanzable en la práctica

CORRECCIÓN POSIBLE
  · agrupación de votos por un representante
    designado, con mandato revocable
  · umbral computado sobre el conjunto
    de tenedores de la representación
  · foro de tenedores con capacidad de
    designar representante

Y ESTO SE DISEÑA ANTES DE FRACCIONAR,
no cuando alguien quiere impugnar.
```

### 4. Derechos perdidos por diseño

```text
LA NORMA LOS CONCEDE Y LA ARQUITECTURA
LOS IMPIDE

  · derecho a un certificado de titularidad
    si el registro no lo emite

  · derecho a transferir a un tercero
    si la plataforma exige que el destinatario
    esté registrado en ella

  · derecho a salir del registro
    si no hay procedimiento de rescate

  · derecho a información en un formato
    accesible, si solo se publica en la
    aplicación de la plataforma

  · derecho al voto, si el custodio no lo
    traslada

CADA UNO SE DETECTA CON LA MISMA PREGUNTA
  «si el tenedor quisiera ejercerlo hoy,
   ¿cuál sería el procedimiento exacto?»
  Si no hay respuesta, está perdido por diseño.
```

### 5. El derecho de rescate

```text
EL MÁS OLVIDADO Y EL MÁS IMPORTANTE

  ¿PUEDE UN TENEDOR SALIR DEL REGISTRO
   TOKENIZADO Y VOLVER AL OFICIAL?

  · en bloqueo de origen: sí, destruyendo
    el token y liberando el saldo
  · en espejo: no aplica, siempre estuvo
    en el oficial
  · en emisión nativa: solo si existe un
    procedimiento de migración

POR QUÉ IMPORTA
  si la plataforma cierra, quiebra o pierde
  la autorización, el tenedor necesita una
  salida que no dependa de esa plataforma

QUÉ EXIGIR
  · procedimiento escrito y probado
  · plazo máximo
  · un tercero capaz de ejecutarlo si el
    operador no puede
  · una copia del registro en poder de ese
    tercero, actualizada y verificable
```

## 🧮 Ejemplo guiado

**Situación.** Una emisión de participaciones tokenizadas de una sociedad
inmobiliaria. Hay que especificar los derechos y comprobar cuáles sobreviven.

```text
DATOS
  capital                        24 000 000
  participaciones                    24 000
  valor nominal                       1 000
  fraccionamiento del token          1/1 000
  unidades emitidas              24 000 000
  inversionistas previstos            9 500

DERECHOS SEGÚN ESTATUTOS
  dividendo                    proporcional
  voto en junta                1 voto por participación
  convocar junta               5 % del capital
  impugnar acuerdos            1 % del capital
  información adicional        3 % del capital
```

**Paso 1 — traduce los umbrales a unidades del token.**

```text
5 % DEL CAPITAL
  24 000 × 5 % = 1 200 participaciones
  = 1 200 000 unidades del token

1 % → 240 000 unidades
3 % → 720 000 unidades

INVERSIÓN MEDIA POR TENEDOR
  24 000 000 / 9 500 = 2 526 unidades
  = 2,53 participaciones
```

**Paso 2 — comprueba si algún derecho es alcanzable.**

```text
PARA CONVOCAR JUNTA HACEN FALTA
  1 200 000 unidades

UN TENEDOR MEDIO TIENE 2 526
  → necesitaría agrupar a 475 tenedores

PARA IMPUGNAR
  240 000 unidades → 95 tenedores

PARA PEDIR INFORMACIÓN
  720 000 unidades → 285 tenedores

NINGÚN DERECHO CON UMBRAL ES ALCANZABLE
POR UN TENEDOR INDIVIDUAL,
y no hay ningún mecanismo previsto
para agruparse.
```

**Paso 3 — calcula el voto fraccionado.**

```text
1 VOTO POR PARTICIPACIÓN
  y el token se fracciona en milésimas

  UN TENEDOR CON 2 526 UNIDADES
  tiene 2,526 participaciones
  → ¿2 votos? ¿2,526 votos?

  LOS ESTATUTOS NO LO DICEN

SI SE REDONDEA A LA BAJA
  se pierden 0,526 votos por tenedor
  9 500 × 0,526 ≈ 4 997 votos perdidos
  sobre 24 000 = 20,8 % del capital
  sin voto

ESE 20,8 % NO DESAPARECE:
aumenta el peso relativo de quien tiene
participaciones enteras.
```

**Paso 4 — mide quién gana con el redondeo.**

```text
SUPUESTO · EL PROMOTOR CONSERVA
EL 30 % EN PARTICIPACIONES ENTERAS

  promotor    7 200 participaciones → 7 200 votos
  resto      16 800 participaciones
             repartidas en fracciones

  votos efectivos del resto
  16 800 − 4 997 = 11 803

  TOTAL VOTOS EMITIBLES = 19 003

  PESO DEL PROMOTOR
  7 200 / 19 003 = 37,9 %
  frente al 30 % de su capital

EL REDONDEO LE REGALÓ 7,9 PUNTOS.
```

**Paso 5 — corrige el diseño.**

```text
CORRECCIÓN 1 · VOTO PROPORCIONAL EXACTO
  el voto se computa sobre unidades,
  no sobre participaciones enteras
  → 24 000 000 votos
  → el promotor vuelve al 30 %

CORRECCIÓN 2 · AGRUPACIÓN DE VOTOS
  · un foro de tenedores puede designar
    un representante
  · el mandato es revocable en cualquier momento
  · el representante debe publicar el sentido
    del voto antes de emitirlo

CORRECCIÓN 3 · UMBRAL SOBRE EL CONJUNTO
  el umbral del 1 % para impugnar se computa
  sobre el conjunto de tenedores agrupados,
  no sobre cada uno

CON LAS TRES, LOS DERECHOS EXISTEN
EN LA PRÁCTICA Y NO SOLO EN LOS ESTATUTOS.
```

**Paso 6 — revisa el derecho de rescate.**

```text
¿PUEDE UN TENEDOR SALIR?

  la propuesta no lo contempla

  ESCENARIO: la plataforma pierde la
  autorización

  · el registro oficial es el libro de socios
  · el libro dice que el titular es
    el vehículo tokenizador
  · los 9 500 tenedores no aparecen en él
  · su derecho es contra el vehículo

  → SI EL VEHÍCULO NO PUEDE OPERAR,
    9 500 personas tienen un derecho
    que nadie puede ejecutar

EXIGENCIA MÍNIMA
  · copia del registro de tenedores en poder
    de un tercero independiente, diaria
  · procedimiento de inscripción directa
    en el libro de socios, con plazo
  · designación de ese tercero antes de emitir
```

**Paso 7 — resume qué sobrevive.**

```text
                          ANTES      DESPUÉS
  dividendo               sí         sí
  voto                    parcial    sí, exacto
  convocar junta          no         sí, agrupado
  impugnar                no         sí, agrupado
  información             no         sí, agrupado
  rescate                 no         sí, con tercero

DE SEIS DERECHOS, CUATRO ESTABAN
PERDIDOS POR DISEÑO, NO POR NORMA.
```

**Interpreta:** ninguna de las cuatro pérdidas venía de la ley: las cuatro
venían de decisiones de diseño que nadie había examinado. **El redondeo del
voto, que parecía un detalle de implementación, transfería 7,9 puntos de control
al promotor.**

## 🧭 Perspectivas

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Una participación desde 1 | Si invierte |
| Inversionista | Derechos en el folleto | Si son ejercitables |
| Emisor | Miles de tenedores | Cómo organiza la junta |
| Promotor | Un peso relativo mayor | Si lo corrige |
| Custodio | Titularidad indirecta | Si traslada el voto |
| Infraestructura | Fecha de corte | Cómo la acredita |
| Supervisor | Derechos inalcanzables | Qué exige en el folleto |
| Auditor | Voto y capital que no cuadran | Qué observa |
| Sociedad | Accionistas sin capacidad de decidir | Qué protección exige |

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Tengo derecho a voto» | Con redondeo, pierde el 20 % | 21, clase 3 |
| «Puedo impugnar» | Necesitaría agrupar 95 tenedores | 21, clase 3 |
| «Es mi participación» | Su derecho es contra el vehículo | 21, clase 3 |

## ⚖️ Riesgos y controles

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Umbrales inalcanzables | El fraccionamiento los diluye | Cómputo sobre tenedores agrupados |
| Redondeo del voto | Transfiere control al que tiene enteros | Voto proporcional exacto |
| Derecho perdido por diseño | No hay procedimiento para ejercerlo | Preguntar «¿cómo se ejerce hoy?» |
| Sin derecho de rescate | El tenedor depende de la plataforma | Tercero con copia del registro |
| Fechas de corte distintas | Cobra quien no debía | Registro de referencia único |
| Voto sin exposición económica | Préstamo de valores | Declarar la tenencia neta |

## 🧪 Práctica

En [`labs/lab-02.md`](../labs/lab-02.md):

1. Traduce los umbrales estatutarios a unidades del token.
2. Calcula el efecto del redondeo del voto sobre el peso relativo.
3. Diseña la agrupación de votos con mandato revocable.
4. Escribe el procedimiento de rescate con su tercero designado.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Copiar los estatutos sin traducir | Los umbrales están en porcentaje | Tradúcelos a unidades |
| Redondear el voto a la baja | Es lo simple de implementar | Transfiere control |
| Suponer que agruparse es posible | No hay mecanismo | Diséñalo antes de emitir |
| Olvidar el rescate | Nadie piensa en el cierre | Es lo que protege si cierra |
| Confundir titular con inversionista | En el registro figura el vehículo | Declara la cadena completa |
| Fechas de corte por separado | Cada evento va por su lado | Un solo registro de referencia |

## ❓ Preguntas de comprobación

1. ¿Cuáles son las tres familias de derechos y qué pregunta define cada una?
2. ¿Por qué el fraccionamiento hace inalcanzables los derechos con umbral?
3. ¿Cómo se detecta un derecho perdido por diseño?
4. En el ejemplo, ¿cuánto control transfirió el redondeo del voto y a quién?
5. ¿Qué exige un derecho de rescate para ser real?

## 📥 Entregable

Guarda en `portfolio/parte-21/clase-03/`:

- la traducción de umbrales a unidades del token;
- el cálculo del efecto del redondeo sobre el peso relativo;
- el diseño de agrupación de votos;
- la tabla de derechos antes y después, con lo que sobrevive.

## 🔗 Referencias cruzadas

- **Viene de:** clases 1 y 2; Parte 8.
- **Continúa en:** clases 5, 7 y 9 de esta parte.
- **Se aplica en:** Parte 22, clases 3 y 11; Parte 23, clase 8.

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

- IOSCO (2023). *Policy Recommendations for Crypto and Digital Asset Markets*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- OCDE (2023). *G20/OECD Principles of Corporate Governance*. OECD. <https://www.oecd.org/corporate/principles-corporate-governance/>
- IOSCO (2009). *Objectives and Principles of Securities Regulation*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD323.pdf>
- Comisión para el Mercado Financiero. *Normativa sobre sociedades anónimas y derechos de accionistas*. CMF. <https://www.cmfchile.cl/portal/principal/613/w3-channel.html>
- Verificación local: comprueba qué derechos son irrenunciables en tu jurisdicción, qué umbrales fija la norma y si admite el cómputo agrupado. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 02 · El registro de referencia](02-el-registro-de-referencia.md) | [Parte 21](../README.md) · [Programa](../../../SYLLABUS.md) | [04 · Emisión: mercado primario tokenizado →](04-emision-mercado-primario-tokenizado.md) |
<!-- gen:footer:end -->
