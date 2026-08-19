<!-- meta
part: 20
class: 6
title: "Pérdida de paridad: anatomía de una corrida"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [estabilidad-financiera, liquidez, contagio]
regulation_last_verified: 2026-08-19
regulatory_status: vigente
primary_authorities: [FSB, BIS, IOSCO]
requires_legal_review: false
-->

<!-- gen:header:start -->
# Clase 06 · Pérdida de paridad: anatomía de una corrida

> [← 05 · Redención: el derecho, el proceso y la cola](05-redencion-el-derecho-el-proceso-y-la-cola.md) · [Índice de la parte](../README.md) · [07 · Stablecoins algorítmicas y su modo de fallo →](07-stablecoins-algoritmicas-y-su-modo-de-fallo.md)

**Parte 20 — Activos digitales, stablecoins y dinero programable** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Reconstruir una pérdida de paridad separando **detonante** de **mecanismo**. El
detonante cambia en cada episodio y no se puede predecir; el mecanismo se repite
y sí se puede medir por adelantado.

Las tres clases anteriores describen los mecanismos en condiciones normales. Esta reconstruye qué pasa cuando fallan, fase a fase, e identifica el punto a partir del cual ninguna intervención sirve.

## 📚 Objetivos

Al finalizar podrás:

1. **Separar** detonante, mecanismo y amplificador en un episodio real.
2. **Construir** la línea de tiempo de una pérdida de paridad con sus fases.
3. **Calcular** el punto en que la venta forzada se retroalimenta.
4. **Identificar** los indicadores que anticipan cada fase.
5. **Explicar** por qué el precio se recupera sin que el riesgo haya
   desaparecido.

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

Los tres primeros términos son la estructura de un episodio; los cinco siguientes, sus fases y su punto crítico. El **punto de no retorno** es el que hay que saber identificar: a partir de él la corrida se alimenta sola y ninguna intervención del emisor la detiene.

| Concepto | Comprensión verificable |
|---|---|
| `detonante` | El hecho concreto que inicia el episodio |
| `mecanismo` | La cadena causal que amplifica ese hecho |
| `amplificador` | Elemento que acelera el mecanismo |
| `venta forzada` | Realizar activos porque hay que pagar, no porque convenga |
| `espiral de liquidez` | Vender deprime el precio, que obliga a vender más |
| `contagio` | Propagación a instrumentos no afectados directamente |
| `recuperación aparente` | Vuelta del precio sin corrección de la causa |
| `punto de no retorno` | Nivel a partir del cual el mecanismo se sostiene solo |

## 🧠 Modelo mental

El modelo mental es una espiral con tres fases: un detonante que hace dudar, un mecanismo que convierte la duda en redenciones y un amplificador que convierte las redenciones en ventas forzadas que confirman la duda. Cortar la espiral exige intervenir antes de la tercera fase.

```text
LAS CINCO FASES DE UNA PÉRDIDA DE PARIDAD

  1 DETONANTE
      una noticia, un fallo técnico, un depositario
      en problemas, una venta grande

  2 DESVÍO INICIAL
      el precio se separa de la paridad
      dentro o justo fuera de la banda

  3 PRUEBA DEL CANAL
      alguien intenta redimir
      · funciona   → el desvío se corrige
      · no funciona→ la noticia es EL CANAL

  4 CARRERA
      el orden de la cola premia al primero
      y todos lo saben

  5 REALIZACIÓN FORZADA
      el emisor vende para pagar
      la venta deprime el precio de sus activos
      → hace falta vender más

EL DETONANTE ES IRREPETIBLE.
LAS FASES 3, 4 Y 5 SON SIEMPRE LAS MISMAS.
Por eso se preparan de antemano.
```

## 📖 Desarrollo

### 1. Detonantes observados

| Familia de detonante | Cómo entra | Qué revela |
|---|---|---|
| Depositario en problemas | Parte del efectivo queda atrapado | Concentración de custodia |
| Duda sobre la composición | Un informe o una filtración | Opacidad previa |
| Fallo técnico del emisor | La redención no procesa | Fragilidad operativa |
| Venta grande en mercado fino | El precio cae por profundidad | Liquidez sobreestimada |
| Acción de una autoridad | Congelación o requerimiento | Riesgo jurídico |
| Contagio de otro instrumento | Se vende lo que se puede vender | Correlación oculta |

### 2. La fase 3 es la que decide

Un desvío de precio no es todavía una crisis: es una pregunta que se le hace
al canal de redención. El bloque describe las dos respuestas posibles y qué
ocurre después de cada una.

```text
EL DESVÍO INICIAL NO ES LA CRISIS.
LA CRISIS ES EL RESULTADO DE LA PRUEBA.

  SI EL CANAL FUNCIONA
    los primeros redimen, ganan el desvío,
    el precio vuelve, y el episodio se cierra
    en horas

  SI EL CANAL NO FUNCIONA
    · mínimo demasiado alto
    · participantes autorizados sin línea
    · suspensión
    · plazo que se alarga sin explicación

    → LA NOTICIA DEJA DE SER EL DETONANTE
      Y PASA A SER «NO SE PUEDE SALIR»

    esa segunda noticia es mucho peor,
    porque afecta a todos los tenedores,
    no solo a los expuestos al detonante
```

### 3. La espiral de realización forzada

Cuando el emisor tiene que vender para pagar, cada venta empeora las
condiciones de la siguiente. El bloque describe el bucle y localiza el punto a
partir del cual deja de poder cerrarse.

```text
EL EMISOR VENDE PARA PAGAR REDENCIONES

  vende → el precio de sus activos baja
       → la reserva vale menos
       → la cobertura publicada baja
       → más tenedores redimen
       → vende más

  Y CADA VENTA ES MÁS CARA QUE LA ANTERIOR,
  porque el mercado ya sabe que hay un vendedor
  forzado y de qué tamaño

PUNTO DE NO RETORNO
  ocurre cuando el descuento por venta
  supera el margen de sobrecolateralización

  a partir de ahí, cada redención pagada
  reduce la cobertura del remanente
```

### 4. Contagio a instrumentos sanos

En una tensión también caen instrumentos que no tenían ningún problema, y hay
cuatro razones distintas para ello. El bloque las separa, porque cada una se
mitiga de una forma.

```text
POR QUÉ CAE LO QUE NO TENÍA PROBLEMA

  1 NECESIDAD DE EFECTIVO
      quien pierde acceso a un instrumento
      vende otro para conseguir liquidez

  2 CORRELACIÓN OPERATIVA
      comparten depositario, plataforma,
      participante autorizado o proveedor

  3 REEVALUACIÓN DEL SUPUESTO
      «esto podía pasar» se aplica a todos

  4 COBERTURA MECÁNICA
      posiciones apalancadas se liquidan
      y arrastran otros activos

EL PUNTO 2 ES EL MÁS SUBESTIMADO:
dos instrumentos con emisores distintos
pueden depender del mismo banco
```

### 5. La recuperación aparente

Que el precio vuelva a la paridad no significa que el problema se haya
resuelto. El bloque enumera las cuatro causas posibles de la recuperación y
señala cuál es la única que corrige la causa.

```text
EL PRECIO VUELVE A 1,00 Y TODOS RESPIRAN

  ¿QUÉ CAMBIÓ REALMENTE?
    a  el emisor consiguió liquidez externa
    b  un tercero compró para sostener
    c  la redención se reanudó
    d  simplemente dejó de haber vendedores

  SOLO c CORRIGE LA CAUSA

  EN a, b Y d EL MECANISMO SIGUE INTACTO
  y el siguiente detonante encontrará
  una reserva peor que la anterior

REGLA DE ANÁLISIS
  no preguntes «¿se recuperó?»
  pregunta «¿qué cambió en el canal de redención
  y en la composición de la reserva?»
```

## 🧮 Ejemplo guiado

El ejemplo reconstruye una pérdida de paridad fase a fase. Conviene identificar el punto donde la recuperación aparente engañó: casi todos los episodios tienen uno.

**Situación.** Reconstruimos un episodio con datos sintéticos construidos para
reproducir el mecanismo. Hay que hallar el punto de no retorno.

```text
SITUACIÓN INICIAL
  circulante                    12 000 000 000
  reserva                       12 240 000 000
  sobrecolateralización                  2,00 %
  efectivo                       1 200 000 000
  letras ≤ 3 meses               4 800 000 000
  deuda 1–3 años                 5 040 000 000
  papel comercial                1 200 000 000

DETONANTE
  el banco donde está el 55 % del efectivo
  entra en resolución un viernes
```

**Paso 1 — mide el impacto directo del detonante.**

```text
EFECTIVO ATRAPADO
  1 200 000 000 × 55 % = 660 000 000

  ¿PÉRDIDA? todavía no se sabe
  ¿DISPONIBILIDAD? cero hasta que se resuelva

RESERVA CONTABLE: sin cambios, 12 240 000 000
RESERVA DISPONIBLE: 12 240 − 660 = 11 580 000 000

EL DETONANTE NO TOCÓ EL VALOR.
TOCÓ LA DISPONIBILIDAD.
Y la disponibilidad es lo que paga redenciones.
```

**Paso 2 — sigue la fase 3.**

```text
LUNES · SOLICITUDES POR 1 400 000 000

  efectivo libre = 540 000 000
  no alcanza

  el emisor vende letras por 900 000 000
  descuento 0,20 % → coste 1 803 607

  PAGA TODO. EL CANAL FUNCIONÓ.
  precio de mercado: 0,9985 → vuelve a 0,9998

SI EL EPISODIO SE HUBIERA DETENIDO AQUÍ,
sería una anécdota operativa.
```

**Paso 3 — introduce la segunda noticia.**

```text
MARTES · SE PUBLICA QUE EL 55 % DEL EFECTIVO
ESTÁ EN RESOLUCIÓN Y QUE LA RECUPERACIÓN
PUEDE SER PARCIAL

  supuesto de recuperación: 90 %
  pérdida esperada = 660 000 000 × 10 % = 66 000 000

  RESERVA AJUSTADA = 12 174 000 000
  COBERTURA = 12 174 / 12 000 = 101,45 %

  sigue por encima de 100 %
  → PERO LA SOBRECOLATERALIZACIÓN
    CAYÓ DEL 2,00 % AL 1,45 %
```

**Paso 4 — calcula el punto de no retorno.**

```text
EL MARGEN RESTANTE ES 1,45 % DEL CIRCULANTE
  12 000 000 000 × 1,45 % = 174 000 000

¿CUÁNTA VENTA FORZADA CONSUME ESE MARGEN?

  vender deuda 1–3 años con descuento del 1,40 %
  cada 1 000 000 000 vendidos cuesta 14 000 000

  174 000 000 / 14 000 000 = 12,43

  → VENDER 12 430 000 000 DE DEUDA
    AGOTARÍA EL MARGEN

  pero solo hay 5 040 000 000 de deuda
  → con el descuento del 1,40 % el margen aguanta
```

**Paso 5 — recalcula con descuento creciente.**

```text
EL DESCUENTO NO ES CONSTANTE.
CRECE CON EL TAMAÑO Y CON LA URGENCIA.

  primeros 1 000 M    1,40 %  →  14 000 000
  siguientes 1 000 M  2,10 %  →  21 000 000
  siguientes 1 000 M  3,20 %  →  32 000 000
  siguientes 1 000 M  4,80 %  →  48 000 000
  siguientes 1 000 M  7,00 %  →  70 000 000

  acumulado tras 4 000 M: 115 000 000
  acumulado tras 5 000 M: 185 000 000

  EL MARGEN ERA 174 000 000

  → SE AGOTA ENTRE 4 000 Y 5 000 MILLONES
    DE VENTA DE DEUDA

  interpolando: 174 − 115 = 59
  59 / 70 = 0,84
  PUNTO DE NO RETORNO ≈ 4 840 000 000
```

**Paso 6 — traduce ese punto a redenciones.**

```text
¿CUÁNTA REDENCIÓN OBLIGA A VENDER 4 840 M
DE DEUDA?

  primero se agota lo barato
    efectivo libre        540 000 000
    letras restantes    3 900 000 000
    subtotal            4 440 000 000

  a partir de ahí, deuda
    4 840 000 000

  REDENCIÓN ACUMULADA ≈ 9 280 000 000
  sobre un circulante de 12 000 000 000

  → EL 77 % DEL CIRCULANTE

INDICADOR OPERATIVO
  vigilar la redención acumulada
  frente a ese 77 %, no frente a la cobertura
```

**Paso 7 — separa hecho, supuesto e interpretación.**

```text
HECHO
  el 55 % del efectivo quedó indisponible;
  el emisor pagó el lunes vendiendo letras

SUPUESTO
  recuperación del 90 %, escalera de descuentos
  y que las letras se venden antes que la deuda
  → los tres son decisiones del analista
    y cambian el punto de no retorno

INTERPRETACIÓN
  el episodio es de disponibilidad, no de
  solvencia; se vuelve de solvencia solo si
  la venta forzada supera el margen

ESTA SEPARACIÓN ES LO QUE DISTINGUE
UN INFORME DE RIESGO DE UN TITULAR
```

**Interpreta:** el detonante fue un banco, no la stablecoin. El instrumento
sobrevivió a la primera prueba y **lo que decidió su suerte fue la escalera de
descuentos**, un dato que no aparece en ningún informe de reservas y que cada
institución tiene que estimar por su cuenta.

## 🧭 Perspectivas

Una corrida afecta a cada participante de forma distinta y en momentos distintos. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un precio que se aleja de 1 | Si vende |
| Comercio | Cobros que valen menos | Si deja de aceptar |
| Fintech | Usuarios que no pueden salir | Qué comunica |
| Banco | Clientes con problemas de liquidez | Si adelanta fondos |
| Banco central | Un sustituto de dinero fallando | Si actúa y con qué mandato |
| Emisor | Redenciones y margen que cae | Si vende o si suspende |
| Infraestructura | Volumen anómalo | Si aplica límites |
| Mercado | Un vendedor forzado identificable | Cómo opera contra él |
| Supervisor | Fase 3 en curso | Qué información exige ya |
| Auditor | Valoraciones que se mueven | Qué reconoce |
| Sociedad | Un medio de pago que falla | Qué protección exige |

## 🏦 Del cliente al banco

El cliente intenta salir y el emisor vende reservas con descuento. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Cayó por una noticia» | La noticia fue el detonante, no la causa | 20, clase 6 |
| «Ya se recuperó» | El canal y la reserva pueden seguir igual | 20, clase 6 |
| «Este no tenía nada que ver» | Comparten depositario o plataforma | 20, clase 6 |

## ⚖️ Riesgos y controles

Los riesgos son de amplificación y de contagio. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Concentración de depositario | Un banco atrapa el efectivo | Límite por depositario y prueba de sustitución |
| Descuento subestimado | Se usa uno constante | Escalera creciente por tamaño |
| Fase 3 no vigilada | Nadie mide si el canal funciona | Indicador de redención efectiva diaria |
| Recuperación aparente | Se cierra el expediente | Exigir qué cambió en canal y reserva |
| Contagio operativo | Proveedores compartidos | Mapa de dependencias comunes |
| Umbral mal elegido | Se vigila la cobertura | Vigilar redención acumulada frente al punto |

## 🧪 Práctica

El laboratorio pide reconstruir un episodio de pérdida de paridad separando detonante, mecanismo y amplificador. Identificar el punto de no retorno es el objetivo, porque es el único momento en que la intervención habría servido.

En [`labs/lab-04.md`](../labs/lab-04.md):

1. Reconstruye un episodio separando detonante, mecanismo y amplificadores.
2. Calcula el punto de no retorno con escalera de descuentos.
3. Traduce ese punto a porcentaje de circulante redimido.
4. Escribe la separación de hecho, supuesto e interpretación.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen episodios de pérdida de paridad. La causa estructural es el descalce entre la reserva y la promesa.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Explicar por el detonante | Es lo que sale en la prensa | El detonante no se repite; el mecanismo sí |
| Descuento constante | Simplifica el cálculo | Crece con tamaño y urgencia |
| Vigilar solo la cobertura | Es la cifra publicada | Vigila disponibilidad y redención acumulada |
| Dar por cerrado el episodio | El precio volvió | Pregunta qué cambió en el canal |
| Ignorar dependencias comunes | No están publicadas | Constrúyelas por observación |
| Confundir disponibilidad con solvencia | Se mezclan en el titular | Sepáralas explícitamente |

## ❓ Preguntas de comprobación

1. ¿Cuáles son las cinco fases y por qué la tercera es la decisiva?
2. ¿Qué es el punto de no retorno y cómo se calcula?
3. ¿Por qué la escalera de descuentos cambia la conclusión?
4. Enumera cuatro vías de contagio a un instrumento sano.
5. ¿Qué hay que preguntar ante una recuperación del precio?

## 📥 Entregable

Guarda en `portfolio/parte-20/clase-06/`:

- la línea de tiempo del episodio con sus cinco fases;
- el cálculo del punto de no retorno con la escalera de descuentos;
- el indicador operativo derivado y su umbral;
- la separación de hecho, supuesto e interpretación.

## 🔗 Referencias cruzadas

- **Viene de:** clases 4 y 5.
- **Continúa en:** clases 7 y 14 de esta parte.
- **Se aplica en:** Parte 22, clase 15; Parte 23, clase 14.

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

- Financial Stability Board (2022). *Assessment of Risks to Financial Stability from Crypto-assets*. FSB. Episodios de pérdida de paridad documentados y sus efectos. <https://www.fsb.org/2022/02/assessment-of-risks-to-financial-stability-from-crypto-assets/>
- Bank for International Settlements (2023). *Stablecoins: fundamentals, emerging issues and open questions*. BIS. Mecanismo de la corrida y su medición anticipada. <https://www.bis.org/publ/work905.htm>
- IOSCO (2023). *Policy Recommendations for Crypto and Digital Asset Markets*. IOSCO. Fallos de mercado observados durante los episodios. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- Financial Stability Board (2021). *Policy Proposals to Enhance Money Market Fund Resilience*. FSB. Analogía con la corrida en fondos del mercado monetario. <https://www.fsb.org/2021/10/policy-proposals-to-enhance-money-market-fund-resilience-final-report/>
- Verificación local: comprueba qué obligaciones de información en tiempo de tensión impone tu jurisdicción al emisor y a las plataformas de negociación. **Fecha de verificación de esta clase: 2026-08-19.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 05 · Redención: el derecho, el proceso y la cola](05-redencion-el-derecho-el-proceso-y-la-cola.md) | [Parte 20](../README.md) · [Programa](../../../SYLLABUS.md) | [07 · Stablecoins algorítmicas y su modo de fallo →](07-stablecoins-algoritmicas-y-su-modo-de-fallo.md) |
<!-- gen:footer:end -->
