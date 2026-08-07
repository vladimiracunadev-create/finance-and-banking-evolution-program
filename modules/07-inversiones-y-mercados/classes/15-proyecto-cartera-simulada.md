<!-- meta
part: 8
class: 15
title: "Proyecto: cartera simulada"
level: avanzado
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 15 · Proyecto: cartera simulada

> [← 14 · Seguimiento y rebalanceo](14-seguimiento-y-rebalanceo.md) · [Índice de la parte](../README.md) · [Proyecto de la parte →](../project/README.md)

**Parte 08 — Inversiones y mercados** · **Nivel:** Avanzado — perfil analista · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Construir, documentar y operar una cartera simulada durante un periodo definido, con la misma
disciplina que exigiría una cartera real. El objetivo no es acertar el rendimiento: es **demostrar que
se puede construir, sostener y explicar una decisión de inversión** bajo reglas escritas.

Esta clase cierra la parte y la Etapa 2. Construye una cartera completa con datos sintéticos y la sigue durante un periodo, con una exigencia que no ha aparecido antes: llevar bitácora de las decisiones para poder distinguir después la suerte del criterio.

## 📚 Objetivos

Al finalizar podrás:

1. **Producir** un documento de política de inversión completo.
2. **Construir** una cartera coherente con esa política.
3. **Operar** la cartera con bitácora de decisiones durante el periodo.
4. **Evaluar** el resultado con medidas ajustadas por riesgo.
5. **Defender** las decisiones y reconocer los errores.

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

Los tres primeros términos son el entregable y su registro; los dos últimos, cómo se evalúa. El **error de proceso** es lo que de verdad se evalúa: una decisión mal tomada que salió bien sigue siendo un error, y solo la bitácora permite verlo.

| Concepto | Comprensión verificable |
|---|---|
| `cartera simulada` | Cartera con datos reales de mercado y sin dinero real. Todas las reglas se aplican igual. |
| `bitácora de decisiones` | Registro de cada decisión con su fecha, motivo y expectativa declarada. |
| `evaluación honesta` | Medición contra el índice y contra la política, no contra el resultado deseado. |
| `atribución de resultado` | Descomposición del resultado en asignación, selección y momento. |
| `error de proceso` | Fallo en cumplir la propia política. Es más grave que un mal resultado. |

## 🧠 Modelo mental

Un buen proceso puede dar un mal resultado y viceversa:

```text
                       buen resultado    mal resultado
buen proceso            merecido          mala suerte
mal proceso             suerte            merecido
```

La evaluación de este proyecto es del **proceso**, no del resultado. Un estudiante que sigue su
política y pierde obtiene mejor evaluación que uno que la incumple y gana.

## 📖 Desarrollo

### 1. Estructura del proyecto

El proyecto tiene cuatro fases y cada una produce un entregable. La tabla las recoge.

```text
FASE 1 — Política (semana 1)
  documento de política de inversión completo, firmado y fechado

FASE 2 — Construcción (semana 2)
  cartera implementada con instrumentos reales y precios de mercado
  costos de transacción aplicados

FASE 3 — Operación (semanas 3 a 14)
  seguimiento quincenal con tablero
  bitácora de toda decisión
  rebalanceo según las reglas propias

FASE 4 — Evaluación (semanas 15 y 16)
  medición del resultado
  atribución
  identificación de errores de proceso
  informe final y defensa
```

### 2. Documento de política (Fase 1)

Debe contener, como mínimo:

```text
1. objetivos, con monto, horizonte y prioridad
2. perfil: capacidad, tolerancia y necesidad (Parte 8, clase 1)
3. asignación estratégica por clase, con rangos
4. límites: por emisor, sector, país, moneda, liquidez
5. instrumentos permitidos y prohibidos
6. reglas de rebalanceo con bandas
7. reglas de decisión previas (qué hacer ante escenarios definidos)
8. índice de referencia contra el cual se evaluará
9. pérdida máxima aceptable
10. criterios de revisión de la política
```

### 3. Construcción (Fase 2)

La construcción sigue el orden de la clase 10 y se documenta a medida que se hace. Los pasos siguientes la recorren.

```text
capital simulado: 50 000 000
fecha de construcción: [fecha real]
precios: de cierre del día, verificables

para cada instrumento:
  · nombre, identificador, clase de activo
  · precio de compra y fecha
  · número de unidades
  · monto invertido
  · costo de transacción aplicado
  · peso resultante
  · justificación de la selección (por qué este y no otro de la misma clase)
```

La última línea es la más exigente: **justificar la selección dentro de la clase**, con costo, error de
seguimiento, liquidez y tamaño (Parte 8, clases 5 y 6).

### 4. Operación (Fase 3)

**Tablero quincenal** con la estructura de la clase 14.

**Bitácora de decisiones:**

```text
FECHA        DECISIÓN                    MOTIVO (regla aplicada)         EXPECTATIVA
2026-04-15   sin operaciones             ninguna banda excedida          —
2026-04-30   sin operaciones             ninguna banda excedida          —
2026-05-14   rebalanceo RV global        banda +5pp excedida (R2)        vuelve a 32 %
             venta 3 200 000
2026-05-28   sin operaciones             —                                —
2026-06-11   NO se vendió pese a caída   regla R3: no vender por caída   recuperación
             del 12 % en RV emergente    de mercado                       en horizonte
```

La columna **"expectativa"** es la que hace evaluable la bitácora: al final se compara lo esperado con
lo ocurrido, y eso permite calibrar el juicio propio.

**Toda decisión, incluida la de no hacer nada, se registra con la regla que la fundamenta.** Una
decisión sin regla aplicable es un error de proceso.

### 5. Evaluación (Fase 4)

La evaluación separa el resultado del proceso, que es lo que la hace útil. La tabla recoge los criterios.

```text
RESULTADO
  valor inicial            50 000 000
  valor final              [X]
  aportes                  [Y]
  rentabilidad (TIR)       [Z] %
  índice de referencia     [W] %
  diferencia               [Z−W] pp

RIESGO
  desviación estándar de los retornos quincenales, anualizada
  caída máxima observada
  comparación con la pérdida máxima declarada en la política

MEDIDAS AJUSTADAS
  Sharpe, Sortino, información
  comparación con el índice

ATRIBUCIÓN
  efecto asignación:  (peso propio − peso índice) × retorno del índice por clase
  efecto selección:   peso propio × (retorno propio − retorno del índice por clase)
  efecto momento:     residuo

ERRORES DE PROCESO
  □ ¿se cumplieron todas las reglas de la política?
  □ ¿hubo decisiones sin regla aplicable?
  □ ¿se excedió algún límite sin corregirlo en el plazo definido?
  □ ¿se registró toda decisión en la bitácora?
  □ ¿se revisó la política por razones no legítimas?
```

## 🧮 Ejemplo guiado

El ejemplo recorre las cuatro fases sobre una cartera concreta. Conviene fijarse en la fase de evaluación: es la que distingue este proyecto de una simulación de resultados.

**Situación de defensa.** Presentas el proyecto y el evaluador formula cuatro preguntas.

**Pregunta 1: "Tu cartera rindió 3,2 % y el índice 6,8 %. ¿Qué salió mal?"**

```text
"El resultado fue inferior en 3,6 puntos. La atribución muestra:

  efecto asignación:  −2,9 pp  → tenía 26 % en renta fija y el índice 15 %
  efecto selección:   −0,4 pp  → mis instrumentos rindieron algo menos que sus índices
  efecto momento:     −0,3 pp  → el rebalanceo de mayo vendió antes de una subida

 La mayor parte de la diferencia proviene de la ASIGNACIÓN, y esa asignación
 fue una decisión deliberada de mi política: mi pérdida máxima aceptable era
 18 % y una asignación como la del índice implicaba una caída estimada de 24 %.

 En el periodo evaluado, mi caída máxima fue −9,1 % y la del índice −14,3 %.
 Cumplí mi política. El índice no era mi objetivo: era mi referencia.

 El error de proceso que sí reconozco es el efecto momento: la banda de
 rebalanceo de ±5 pp era demasiado estrecha para una clase que representa
 el 32 % de la cartera, y generó una operación que no era necesaria."
```

**Pregunta 2: "El 11 de junio la renta variable emergente cayó 12 % y no hiciste nada. ¿Fue disciplina
o parálisis?"**

```text
"Fue una decisión registrada, no una omisión.

 La bitácora del 11 de junio dice: 'no se vende pese a la caída del 12 %;
 regla R3 prohíbe vender por movimientos de mercado; la posición sigue
 dentro de su banda (4,8 % contra un rango de 4,5 %–7,5 %)'.

 La expectativa declarada fue 'recuperación en el horizonte del objetivo,
 no en el trimestre'. Al cierre del proyecto la posición estaba en −7 %,
 de modo que la expectativa aún no se verificó, y ese es el punto: mi
 horizonte es de 22 años y el proyecto duró 16 semanas.

 Lo que sí puedo evaluar es si la regla R3 era correcta, y creo que sí:
 sin ella, habría vendido en el peor momento, que es exactamente lo que
 la brecha del inversionista documenta."
```

**Pregunta 3: "¿Cometiste algún error de proceso?"**

```text
"Tres, y los documenté:

 E1  el 28 de abril compré un fondo sin verificar si existía una serie
     más barata. Al descubrirlo en mayo, el traspaso costó 0,18 % adicional.
     Costo del error: aproximadamente 34 000 sobre la cartera simulada.

 E2  las bandas de ±5 pp para clases grandes generaron un rebalanceo
     innecesario. Debí usar bandas más anchas para clases sobre el 30 %.

 E3  no registré en la bitácora la revisión del 21 de mayo, donde decidí
     no actuar. La decisión fue correcta; la omisión del registro es el error.

 De los tres, el más grave es E3, porque un registro incompleto impide
 evaluar el proceso, que es lo único que puedo controlar."
```

**Pregunta 4: "Si tuvieras que empezar de nuevo, ¿qué cambiarías de tu política?"**

```text
"Dos cosas, y ninguna es la asignación:

 1. las bandas: ±5 pp para clases sobre el 30 %, ±25 % relativo para las menores,
    en lugar de ±5 pp para todas

 2. agregaría una regla R8: 'antes de comprar cualquier instrumento, verificar
    todas las series disponibles y documentar la elección'

 NO cambiaría la asignación estratégica pese a haber rendido menos que el índice,
 porque la asignación responde a mi tolerancia y a mi horizonte, no al resultado
 de 16 semanas. Cambiarla ahora sería exactamente el error que la política
 existe para evitar."
```

**Lo que estas cuatro respuestas enseñan:** el proyecto se defiende **separando resultado de proceso,
reconociendo errores concretos y sosteniendo las decisiones que siguen siendo correctas pese al
resultado**. La cuarta respuesta —no cambiar la asignación— es la más difícil y la más importante.

## 🏦 Del cliente al banco

El inversionista evalúa su resultado y el banco evalúa el proceso de sus gestores. La tabla enfrenta las dos lecturas.

| Elemento del proyecto | Equivalente profesional | Parte |
|---|---|---|
| Política de inversión | Mandato de gestión institucional | 15, clase 12 |
| Bitácora de decisiones | Registro de asesoría exigido por norma | 12, clase 14 |
| Atribución de resultado | Informe de desempeño a clientes | 15, clase 9 |
| Errores de proceso | Hallazgos de control interno | 12, clase 12 |
| Defensa ante evaluador | Comité de inversiones | 15, clase 12 |

## 🧪 Práctica

Este proyecto es la práctica. Trabaja en `project/README.md` de esta parte.

1. Redacta la política completa con sus diez elementos y fírmala.
2. Construye la cartera con precios reales, costos aplicados y justificación de cada selección.
3. Opera durante el periodo con tablero quincenal y bitácora de toda decisión.
4. Evalúa el resultado con atribución, identifica errores de proceso y prepara la defensa.

## ⚠️ Errores frecuentes

Los síntomas de la tabla aparecen en la evaluación final. Casi todos vienen de no haber llevado bitácora, que es lo que impide distinguir criterio de suerte.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se evalúa solo el resultado | Proceso ignorado | Un buen proceso con mal resultado es mejor que lo inverso. |
| La bitácora solo registra operaciones | Las no-decisiones también importan | Registra también las decisiones de no actuar. |
| Se cambia la política tras un mal periodo | Reacción al resultado | Solo cambios de circunstancias justifican revisión. |
| No se justifica la selección dentro de la clase | Trabajo incompleto | Documenta costo, liquidez y tamaño. |
| Se omiten los costos de transacción | Resultado inflado | Aplícalos en cada operación. |
| Se compara con un índice inadecuado | Referencia incorrecta | El índice debe corresponder a la asignación. |

## ❓ Preguntas de comprobación

1. ¿Por qué se evalúa el proceso y no el resultado?
2. ¿Qué debe registrarse en la bitácora además de las operaciones?
3. ¿Cómo se descompone el resultado en asignación, selección y momento?
4. ¿Qué gatillos justifican cambiar la política y cuáles no?
5. ¿Cuál es el error de proceso más grave y por qué?

## 📥 Entregable

Guarda en `portfolio/parte-08/clase-15/`:

- la política de inversión completa, firmada y fechada;
- la cartera construida con precios, costos y justificación de cada selección;
- los tableros quincenales y la bitácora completa de decisiones;
- el informe final con atribución, errores de proceso reconocidos y notas de defensa.

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

- CFA Institute (2023). *Standards of Practice Handbook* y *Global Investment Performance Standards (GIPS)*. Medición y presentación de desempeño. <https://www.cfainstitute.org/>
- Bodie, Z., Kane, A. y Marcus, A. (2023). *Investments* (13.ª ed.). McGraw-Hill. Capítulo 24: evaluación de desempeño y atribución.
- Brinson, G., Hood, R. y Beebower, G. (1986). "Determinants of Portfolio Performance". *Financial Analysts Journal*. Metodología de atribución.
- Ellis, C. (2017). *Winning the Loser's Game* (7.ª ed.). McGraw-Hill. Foco en el proceso por sobre el resultado.
- Kahneman, D. (2011). *Pensar rápido, pensar despacio*. Debate. Evaluación de decisiones bajo incertidumbre y sesgo retrospectivo.
- Verificación local: usa precios de cierre publicados por la bolsa de tu país y fichas de fondos del registro del supervisor, documentando la fecha de cada dato.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 14 · Seguimiento y rebalanceo](14-seguimiento-y-rebalanceo.md) | [Parte 08](../README.md) · [Programa](../../../SYLLABUS.md) | [Proyecto de la parte →](../project/README.md) |
<!-- gen:footer:end -->
