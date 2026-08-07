---
part: 20
class: 5
title: "Redención: el derecho, el proceso y la cola"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional, union-europea]
regulatory_topics: [redencion, liquidez, proteccion-al-cliente]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [FSB, CPMI, CMF]
requires_legal_review: true
---

<!-- gen:header:start -->
# Clase 05 · Redención: el derecho, el proceso y la cola

> [← 04 · Reservas: composición, calidad y verificación](04-reservas-composicion-calidad-y-verificacion.md) · [Índice de la parte](../README.md) · [06 · Pérdida de paridad: anatomía de una corrida →](06-perdida-de-paridad-anatomia-de-una-corrida.md)

**Parte 20 — Activos digitales, stablecoins y dinero programable** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Estudiar el mecanismo que convierte una promesa en dinero. **La redención no es
un botón: es una cola**, y el orden de esa cola decide quién cobra íntegro y
quién no cobra.

La reserva de la clase anterior se convierte en dinero mediante la redención. Esta clase la desarrolla, y muestra que su diseño decide si un episodio de tensión se contiene o se convierte en corrida.

## 📚 Objetivos

Al finalizar podrás:

1. **Describir** el ciclo completo de una redención, con sus siete etapas.
2. **Calcular** el efecto de una cola por orden de llegada frente a un prorrateo.
3. **Explicar** por qué el orden de llegada crea el incentivo a correr.
4. **Diseñar** salvaguardas que reducen la carrera sin bloquear al cliente.
5. **Evaluar** una cláusula de suspensión por sus cuatro elementos.

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

Los tres primeros términos son el derecho y su mecánica de reparto; los cinco siguientes, los mecanismos de contención. El **orden de llegada** es el diseño que produce la corrida: si quien redime primero cobra entero, todos tienen incentivo a ser el primero, y ese incentivo es el que hay que eliminar.

| Concepto | Comprensión verificable |
|---|---|
| `redención` | Entrega del instrumento a cambio del importe prometido |
| `orden de llegada` | Se atiende por turno hasta agotar la liquidez |
| `prorrateo` | Todos cobran la misma fracción |
| `incentivo a correr` | Ventaja de ser de los primeros |
| `ventana de liquidez` | Horario y plazo en que se ejecuta |
| `comisión antidilución` | Cargo que traslada el coste al que sale |
| `puerta` | Límite temporal a la salida |
| `suspensión` | Cierre del canal de redención |

## 🧠 Modelo mental

El modelo mental es una cola con dos reglas posibles: por orden de llegada, que premia correr, o a prorrata, que no. La segunda es más justa y más difícil de operar, y la elección de una u otra determina si el emisor sobrevive a un episodio de tensión.

```text
LAS SIETE ETAPAS DE UNA REDENCIÓN

  1 SOLICITUD        el tenedor pide redimir
  2 ADMISIÓN         se comprueba mínimo, elegibilidad,
                     verificación de identidad
  3 INMOVILIZACIÓN   el instrumento se bloquea o se destruye
  4 COLA             se ordena frente a las demás solicitudes
  5 VENTA            el emisor obtiene efectivo de la reserva
  6 PAGO             se transfiere por un sistema de pagos
  7 CONCILIACIÓN     se casa lo pagado con lo destruido

ENTRE 3 Y 6 EL TENEDOR NO TIENE NI EL
INSTRUMENTO NI EL DINERO.

Ese intervalo es donde vive todo el riesgo,
y casi ninguna documentación lo acota.
```

## 📖 Desarrollo

### 1. El incentivo a correr

```text
CON ORDEN DE LLEGADA Y LIQUIDEZ LIMITADA

  quien pide primero cobra 1,00
  quien pide después cobra 1,00
  ...
  quien pide cuando se agota la liquidez
  cobra cuando se venda algo, a un precio peor
  o no cobra

  → CADA TENEDOR SABE ESTO
  → LA RESPUESTA RACIONAL ES PEDIR YA
  → AUNQUE NO NECESITE EL DINERO

LA CORRIDA NO LA CAUSA EL PÁNICO:
LA CAUSA EL DISEÑO DE LA COLA.

Un tenedor tranquilo que sabe que los demás
correrán, corre. Y tiene razón.
```

### 2. Prorrateo

```text
CON PRORRATEO

  se recogen todas las solicitudes de la ventana
  se calcula el efectivo disponible
  todos cobran la MISMA FRACCIÓN

  → SER PRIMERO NO DA VENTAJA
  → EL INCENTIVO A CORRER SE APAGA

COSTE DEL PRORRATEO
  · el tenedor que necesita el dinero de verdad
    tampoco lo recibe entero
  · exige ventanas, no continuidad
  · es más complejo de operar

INTERCAMBIO REAL: se cambia inmediatez
por equidad y por estabilidad del conjunto.
```

### 3. Comisión antidilución

```text
EL PROBLEMA QUE RESUELVE

  vender activos para pagar una redención
  tiene un coste (clase 4)

  si ese coste lo soporta la reserva,
  lo pagan LOS QUE SE QUEDAN

  → los que salen primero externalizan
    su coste sobre los que permanecen

LA CORRECCIÓN
  cargar al que redime el coste real
  de realizar los activos

EFECTO SECUNDARIO ÚTIL
  redimir sin necesidad deja de ser gratis
  → parte del incentivo a correr desaparece
```

### 4. Puertas y suspensión

```text
PUERTA
  límite al porcentaje redimible por ventana
  · el resto pasa a la siguiente
  · es gradual y previsible si está publicado

SUSPENSIÓN
  cierre total del canal
  · es discreta y binaria
  · su anuncio ES la noticia que provoca
    la caída del precio de mercado

LOS CUATRO ELEMENTOS DE UNA CLÁUSULA
DE SUSPENSIÓN QUE HAY QUE EXIGIR
  1 CAUSA    tasada y verificable, no «a criterio»
  2 PLAZO    máximo, con revisión periódica
  3 AVISO    obligación de comunicar y en cuánto
  4 REANUDACIÓN  a prorrata de lo pendiente,
                 no por orden de llegada
```

### 5. La redención en la práctica del cliente

```text
LO QUE UN CLIENTE MINORISTA VIVE

  · no alcanza el mínimo de redención
  · su plataforma no es participante autorizado
  · «redimir» para él significa VENDER en mercado
  · el precio de mercado ya recogió la noticia

  → SU EXPERIENCIA NO ES UNA REDENCIÓN
    ES UNA VENTA A PRECIO DE TENSIÓN

DISEÑOS QUE SÍ LE SIRVEN
  · redención sin mínimo, aunque sea con ventana
  · redención a través de su intermediario,
    con obligación de trasladarla
  · o decir claramente que no hay derecho,
    para que lo sepa al comprar
```

## 🧮 Ejemplo guiado

El ejemplo compara el resultado de una cola por orden de llegada y una a prorrata sobre la misma reserva insuficiente. El reparto cambia por completo y el incentivo a correr desaparece.

**Situación.** Un emisor con 5 000 000 000 en circulación recibe en un día
solicitudes por 1 800 000 000. Su efectivo disponible ese día es 900 000 000.
Comparamos orden de llegada y prorrateo.

```text
DATOS
  circulante                 5 000 000 000
  solicitudes del día        1 800 000 000
  efectivo disponible          900 000 000
  solicitantes                       12 000
  importe medio                    150 000
  activos vendibles a 24 h   2 100 000 000
  descuento medio de venta            1,10 %
```

**Paso 1 — resuelve con orden de llegada.**

```text
EFECTIVO 900 000 000 / IMPORTE MEDIO 150 000
  = 6 000 solicitantes cobran íntegro

LOS OTROS 6 000
  quedan en espera
  su instrumento ya está inmovilizado
  cobrarán cuando se vendan activos

RESULTADO
  6 000 tenedores: 100 % · sin coste
  6 000 tenedores: 0 % ese día · plazo incierto
```

**Paso 2 — calcula qué cobran los rezagados al día siguiente.**

```text
FALTA CUBRIR 900 000 000

  se venden activos por ese importe neto
  nominal necesario = 900 000 000 / (1 − 1,10 %)
                    = 910 010 111

  COSTE DE LA VENTA = 10 010 111

¿QUIÉN LO PAGA?
  si lo paga la reserva → lo pagan los que se quedan
  si lo pagan los rezagados → cobran
     900 000 000 − 10 010 111 = 889 989 889
     es decir, 0,98887 por unidad

EL SEGUNDO GRUPO COBRA UN 1,11 % MENOS
POR HABER LLEGADO DESPUÉS
```

**Paso 3 — resuelve con prorrateo.**

```text
TODOS RECIBEN LA MISMA FRACCIÓN

  fracción = 900 000 000 / 1 800 000 000 = 50 %

  cada solicitante de 150 000 recibe 75 000
  y conserva 75 000 en instrumento

RESULTADO
  12 000 tenedores: 50 % hoy, sin diferencia
  entre ellos
```

**Paso 4 — compara el incentivo generado.**

```text
CON ORDEN DE LLEGADA
  ventaja de ser primero: 1,11 % + certeza
  → todo tenedor racional solicita hoy
  → la solicitud de mañana será mayor
     que la necesidad real

CON PRORRATEO
  ventaja de ser primero: CERO
  → solicita quien necesita el dinero
  → la solicitud refleja la necesidad

LA DIFERENCIA ENTRE 1,11 % Y 0 %
DECIDE SI HAY CORRIDA O NO
```

**Paso 5 — añade comisión antidilución al prorrateo.**

```text
COMISIÓN = COSTE REAL DE REALIZAR LOS ACTIVOS

  para pagar 900 000 000 hubo que vender
  con un coste de 10 010 111
  → 1,112 % sobre lo pagado

  cada solicitante recibe
  75 000 × (1 − 1,112 %) = 74 166

  y los que NO redimen
  no soportan ningún coste

EFECTO SOBRE EL INCENTIVO
  redimir cuesta 1,112 %
  → quien no necesita el dinero, no redime
  → la solicitud del día siguiente baja
```

**Paso 6 — mide el efecto en la segunda jornada.**

```text
SUPUESTO · SIN COMISIÓN, EL 40 % DE LOS QUE
COBRARON PARCIAL VUELVE A SOLICITAR,
MÁS UN 25 % DE NUEVOS

  ORDEN DE LLEGADA
    todos los que no cobraron vuelven: 900 000 000
    más nuevos por miedo:              625 000 000
    total día 2 = 1 525 000 000

  PRORRATEO CON COMISIÓN
    vuelven los que necesitan: 900 000 000 × 40 %
                             = 360 000 000
    nuevos, sin ventaja por correr: 150 000 000
    total día 2 = 510 000 000

  DIFERENCIA: casi tres veces
```

**Paso 7 — evalúa el coste de la equidad.**

```text
EL PRORRATEO NO ES GRATIS

  UN TENEDOR QUE NECESITA 150 000 PARA PAGAR
  UNA NÓMINA RECIBE 74 166
  → tiene un problema real

  MITIGACIONES POSIBLES
    · tramo mínimo íntegro para importes pequeños
      (por ejemplo, los primeros 5 000 al 100 %)
    · ventanas más frecuentes
    · línea de liquidez contratada por el emisor

  EL TRAMO MÍNIMO ES IMPORTANTE
    protege al minorista sin reabrir la carrera,
    porque el grande sigue prorrateado
```

**Interpreta:** la diferencia entre una redención ordenada y una corrida no está
en la calidad de las reservas, sino en **si ser el primero de la cola vale
algo**. El prorrateo con comisión antidilución y tramo mínimo elimina la ventaja
sin dejar desprotegido al pequeño.

## 🧭 Perspectivas

La redención afecta a cada participante de forma distinta según su posición en la cola. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Una cola que no ve | Si solicita ya |
| Comercio | Un cobro inmovilizado | Si sigue aceptando |
| Fintech | Un plazo incierto | Qué comunica a sus usuarios |
| Banco | Un cliente que no recibe fondos | Si adelanta liquidez |
| Emisor | Solicitudes que crecen | Si abre puerta o suspende |
| Custodio | Instrumentos inmovilizados | Cómo los refleja |
| Mercado | El anuncio de la puerta | Cómo cotiza |
| Supervisor | Un mecanismo que crea la corrida | Qué diseño exige |
| Auditor | Conciliación entre destruido y pagado | Qué verifica |
| Sociedad | Gente sin acceso a su dinero | Qué protección exige |

## 🏦 Del cliente al banco

El cliente espera redimir a la par y el emisor tiene una cola con reglas. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Pedí redimir y no llega» | Está en cola tras la inmovilización | 20, clase 5 |
| «Cobré menos que mi vecino» | Orden de llegada con coste de venta | 20, clase 5 |
| «Todos pidieron a la vez» | El diseño de la cola lo provocó | 20, clase 5 |

## ⚖️ Riesgos y controles

Los riesgos son de incentivo a correr y de mecanismos de contención mal diseñados. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Incentivo a correr | Ser primero da ventaja | Prorrateo por ventana |
| Coste externalizado | Los que salen lo cargan a los que quedan | Comisión antidilución |
| Inmovilización sin plazo | El instrumento se bloquea y no llega el pago | Plazo máximo contractual |
| Suspensión discrecional | Se cierra a criterio del emisor | Causas tasadas y plazo máximo |
| Minorista desprotegido | El prorrateo le deja sin efectivo | Tramo mínimo íntegro |
| Reanudación por turno | Reabre la carrera al reabrir | Reanudar a prorrata de lo pendiente |

## 🧪 Práctica

El laboratorio pide simular las dos reglas de cola sobre la misma reserva. El resultado por tenedor es lo que decide cuál es defendible.

En [`labs/lab-03.md`](../labs/lab-03.md):

1. Simula la cola con orden de llegada y con prorrateo.
2. Añade comisión antidilución y mide el efecto en el día 2.
3. Introduce un tramo mínimo íntegro y comprueba que no reabre la carrera.
4. Redacta la cláusula de suspensión con sus cuatro elementos.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen redenciones que degeneran en corrida. La causa es el orden de llegada.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Culpar al pánico | Es la explicación fácil | El diseño de la cola crea el incentivo |
| Orden de llegada por defecto | Parece justo | Es lo que produce la corrida |
| Sin comisión antidilución | Se teme molestar al cliente | El coste lo pagan los que se quedan |
| Inmovilizar sin plazo | Se omite en el contrato | Plazo máximo y consecuencia si se incumple |
| Prorrateo sin tramo mínimo | Se busca pureza | El minorista necesita un mínimo |
| Reanudar por turno | Es lo operativamente simple | Reabre la carrera entera |

## ❓ Preguntas de comprobación

1. Enumera las siete etapas de una redención y di dónde está el riesgo.
2. ¿Por qué el orden de llegada crea el incentivo a correr?
3. ¿Qué problema resuelve la comisión antidilución y a quién protege?
4. ¿Qué coste tiene el prorrateo y cómo se mitiga?
5. ¿Qué cuatro elementos debe tener una cláusula de suspensión?

## 📥 Entregable

Guarda en `portfolio/parte-20/clase-05/`:

- la simulación comparada de orden de llegada y prorrateo;
- el cálculo de la comisión antidilución con el coste real de venta;
- el efecto medido sobre la solicitud del día siguiente;
- la cláusula de suspensión redactada con sus cuatro elementos.

## 🔗 Referencias cruzadas

- **Viene de:** clases 3 y 4.
- **Continúa en:** clases 6 y 7 de esta parte.
- **Se aplica en:** Parte 22, clase 6; Parte 23, clase 6.

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

- Financial Stability Board (2023). *High-level Recommendations for the Regulation, Supervision and Oversight of Global Stablecoin Arrangements*. FSB. <https://www.fsb.org/2023/07/high-level-recommendations-for-the-regulation-supervision-and-oversight-of-global-stablecoin-arrangements-final-report/>
- Financial Stability Board (2021). *Policy Proposals to Enhance Money Market Fund Resilience*. FSB. <https://www.fsb.org/2021/10/policy-proposals-to-enhance-money-market-fund-resilience-final-report/>
- CPMI e IOSCO (2022). *Application of the Principles for Financial Market Infrastructures to stablecoin arrangements*. BIS. <https://www.bis.org/cpmi/publ/d206.htm>
- Diario Oficial de la Unión Europea (2023). *Reglamento (UE) 2023/1114*, disposiciones sobre derecho de reembolso. EUR-Lex. <https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32023R1114>
- Verificación local: comprueba si tu jurisdicción admite puertas, prorrateo o comisiones antidilución en este tipo de instrumento y qué plazo máximo de reembolso impone. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 04 · Reservas: composición, calidad y verificación](04-reservas-composicion-calidad-y-verificacion.md) | [Parte 20](../README.md) · [Programa](../../../SYLLABUS.md) | [06 · Pérdida de paridad: anatomía de una corrida →](06-perdida-de-paridad-anatomia-de-una-corrida.md) |
<!-- gen:footer:end -->
