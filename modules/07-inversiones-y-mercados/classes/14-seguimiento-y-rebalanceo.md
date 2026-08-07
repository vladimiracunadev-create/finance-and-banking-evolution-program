<!-- meta
part: 8
class: 14
title: "Seguimiento y rebalanceo"
level: intermedio
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 14 · Seguimiento y rebalanceo

> [← 13 · Costos, impuestos y sesgos](13-costos-impuestos-y-sesgos.md) · [Índice de la parte](../README.md) · [15 · Proyecto: cartera simulada →](15-proyecto-cartera-simulada.md)

**Parte 08 — Inversiones y mercados** · **Nivel:** Intermedio — requiere las partes anteriores · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Mantener una cartera alineada con su política a lo largo del tiempo, que es donde se juega el
resultado de largo plazo. El rebalanceo es la única disciplina que **obliga a vender lo que subió y
comprar lo que bajó**, en contra del instinto, y por eso funciona.

Una cartera construida se desvía sola: lo que sube pesa más y el riesgo aumenta sin que nadie lo decida. Esta clase trata la disciplina que la devuelve a su sitio, y la distinción que evita el peor error de la gestión: rebalancear no es lo mismo que cambiar de opinión.

## 📚 Objetivos

Al finalizar podrás:

1. **Explicar** por qué una cartera se desalinea sola y qué implica.
2. **Comparar** las estrategias de rebalanceo y elegir según costo y disciplina.
3. **Calcular** el efecto del rebalanceo sobre riesgo y retorno.
4. **Diseñar** un tablero de seguimiento con indicadores y umbrales.
5. **Distinguir** una revisión de política de una reacción al mercado.

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

Los cinco primeros términos son la mecánica del rebalanceo y su beneficio; los dos últimos, la deriva y la revisión de la política. La distinción entre **rebalanceo y revisión de política** es la que hay que fijar: el primero es mecánico y el segundo es una decisión, y disfrazar la segunda de primero es como se abandonan las estrategias.

| Concepto | Comprensión verificable |
|---|---|
| `desviación` | Diferencia entre el peso actual y el objetivo de una clase. |
| `rebalanceo` | Operaciones que devuelven la cartera a su asignación objetivo. |
| `rebalanceo por calendario` | En fechas fijas, independientemente de la desviación. |
| `rebalanceo por bandas` | Cuando una clase sale de un rango definido. |
| `prima de rebalanceo` | Retorno adicional que puede generar el rebalanceo en mercados que revierten. |
| `deriva` | Alejamiento gradual de la asignación objetivo por rendimientos distintos. |
| `revisión de política` | Cambio del objetivo por cambio de circunstancias, no por movimiento de mercado. |

## 🧠 Modelo mental

Una cartera **se desalinea sola**, porque sus componentes rinden distinto:

```text
asignación inicial:  60 % RV / 40 % RF
un año después, RV +25 % y RF +3 %:
  RV: 60 × 1,25 = 75,0 → 75/(75+41,2) = 64,6 %
  RF: 40 × 1,03 = 41,2 → 35,4 %
```

Sin hacer nada, la cartera pasó de 60/40 a 64,6/35,4: **asumió más riesgo del decidido**. El
rebalanceo la devuelve al perfil elegido, y su efecto secundario es forzar la conducta correcta:
vender lo que subió.

## 📖 Desarrollo

### 1. Estrategias de rebalanceo

Hay varias formas de decidir cuándo rebalancear y ninguna domina a las demás. La tabla las compara.

| Estrategia | Regla | Ventaja | Desventaja |
|---|---|---|---|
| Calendario | Rebalancear cada N meses | Simple, predecible | Puede operar sin necesidad |
| Bandas absolutas | Si una clase se desvía más de X puntos | Solo opera cuando importa | Puede pasar mucho tiempo sin revisar |
| Bandas relativas | Si se desvía más de X % de su peso objetivo | Se adapta al tamaño de la clase | Más compleja |
| Híbrida | Revisar por calendario, rebalancear por bandas | **Combina lo mejor** | Requiere ambas reglas |
| Por flujos | Dirigir los aportes a las clases bajo su objetivo | Sin costo de transacción | Insuficiente si los aportes son pequeños |

**La estrategia híbrida es la recomendación defendible:**

```text
revisar trimestralmente
rebalancear solo si alguna clase supera su banda
dirigir los aportes nuevos a las clases más rezagadas
```

### 2. Diseñar las bandas

Las bandas se diseñan según la volatilidad del activo y el costo de operar. El procedimiento siguiente las fija.

```text
banda absoluta = ±5 puntos porcentuales para clases con peso > 20 %
banda relativa = ±25 % del peso objetivo para clases con peso < 20 %
```

Aplicadas a una cartera concreta, las dos reglas producen la tabla de rangos que después dispara cada rebalanceo.

```text
Clase                objetivo   banda        rango
renta variable global   32 %    ±5 pp        27 % – 37 %
renta fija local        26 %    ±5 pp        21 % – 31 %
renta variable local    10 %    ±25 % rel.   7,5 % – 12,5 %
renta variable emerg.    6 %    ±25 % rel.   4,5 % – 7,5 %
inmobiliario             8 %    ±25 % rel.   6,0 % – 10,0 %
```

Bandas más estrechas producen más operaciones y más costo; más anchas, mayor deriva del perfil. La
evidencia sugiere que **bandas entre 3 y 8 puntos capturan la mayor parte del beneficio** con costo
razonable.

### 3. Efecto sobre riesgo y retorno

Comparación en un periodo de 20 años, cartera 60/40:

| Estrategia | Retorno anual | Desviación estándar | Caída máxima | N.º de rebalanceos |
|---|---:|---:|---:|---:|
| Sin rebalanceo | 7,84 % | 12,9 % | −38,2 % | 0 |
| Anual | 7,71 % | 10,8 % | −31,4 % | 20 |
| Bandas ±5 pp | 7,79 % | 10,9 % | −31,8 % | 11 |
| Trimestral | 7,68 % | 10,7 % | −31,1 % | 80 |

**El hallazgo principal no es de retorno sino de riesgo:**

```text
sin rebalanceo: la cartera terminó en 78/22 (la renta variable creció más)
              → asumió un riesgo que nunca se decidió
              → caída máxima 7 puntos mayor
con rebalanceo: se mantuvo el perfil elegido durante todo el periodo
```

La "prima de rebalanceo" —retorno adicional— **existe solo cuando los activos revierten** y puede ser
negativa en periodos de tendencia sostenida. **El argumento sólido a favor del rebalanceo es el
control del riesgo, no el retorno.**

### 4. Tablero de seguimiento

El seguimiento se hace con pocos indicadores y en fechas fijas. La tabla recoge el tablero mínimo.

```text
TABLERO — [fecha]

ASIGNACIÓN
  clase                 objetivo   actual   desviación   banda    estado
  RV global               32 %     36,4 %     +4,4 pp    ±5 pp     OK
  RF local                26 %     21,8 %     −4,2 pp    ±5 pp     OK
  RV local                10 %     12,9 %     +2,9 pp    ±2,5 pp   ⚠ FUERA
  RV emergente             6 %      5,1 %     −0,9 pp    ±1,5 pp   OK
  inmobiliario             8 %      7,4 %     −0,6 pp    ±2,0 pp   OK
  liquidez                18 %     16,4 %     −1,6 pp    ±5 pp     OK

  ACCIÓN REQUERIDA: rebalancear RV local de 12,9 % a 10 %

RIESGO
  desviación estándar estimada        10,4 %   (política: máx. 12 %)     OK
  caída máxima simulada en estrés    −23,1 %   (política: máx. −25 %)    OK
  exposición a moneda extranjera      41,5 %   (política: máx. 45 %)     OK
  máximo por emisor individual         3,8 %   (política: máx. 5 %)      OK

COSTOS
  costo ponderado de la cartera        0,34 %  (objetivo: < 0,50 %)      OK
  operaciones en 12 meses                  3   (objetivo: < 6)           OK

PROGRESO DE OBJETIVOS
  objetivo B (vivienda, 6 años)   avance 34 %   requerido 33 %          OK
  objetivo C (retiro, 22 años)    avance  8 %   requerido  7 %          OK
```

### 5. Rebalanceo frente a revisión de política

Las dos cosas se parecen y son opuestas. La tabla las separa con el criterio que decide cuál corresponde.

```text
REBALANCEO       devolver la cartera a la asignación objetivo
                 gatillo: desviación de bandas
                 frecuencia: cuando corresponda
                 NO cambia el objetivo

REVISIÓN DE POLÍTICA   cambiar la asignación objetivo
                 gatillo: cambio de circunstancias del inversionista
                 frecuencia: anual, o ante un evento
                 SÍ cambia el objetivo
```

Gatillos legítimos de revisión de política:

```text
✓ cambio de horizonte (se acerca un objetivo)
✓ cambio material de patrimonio o de ingreso
✓ cambio de situación familiar
✓ un objetivo se cumplió o se descartó
✓ cambio en la tolerancia demostrado por conducta
✓ cambio estructural del régimen tributario o normativo
```

Gatillos **no** legítimos:

```text
✗ el mercado cayó
✗ el mercado subió
✗ una noticia
✗ la recomendación de un tercero sin análisis
✗ el desempeño de un instrumento en los últimos meses
```

La distinción es la que impide que "revisar la política" se convierta en un eufemismo para vender en
el pánico.

## 🧮 Ejemplo guiado

El ejemplo rebalancea una cartera desviada por bandas y calcula el costo de hacerlo. Conviene comparar con la alternativa de no rebalancear: el riesgo de la cartera sin rebalancear crece de forma sostenida.

**Situación.** Una cartera de 92 000 000 después de un año de mercado volátil.

```text
                     objetivo   valor actual   peso actual
RV global               32 %     38 640 000      42,0 %
RF local                26 %     19 320 000      21,0 %
RV local                10 %      9 200 000      10,0 %
RV emergente             6 %      4 140 000       4,5 %
inmobiliario             8 %      6 900 000       7,5 %
liquidez                18 %     13 800 000      15,0 %
TOTAL                  100 %     92 000 000     100,0 %

bandas: ±5 pp para clases > 20 % · ±25 % relativo para clases < 20 %
```

**Paso 1 — verifica cada banda.**

| Clase | Objetivo | Actual | Desviación | Banda | Estado |
|---|---:|---:|---:|---|---|
| RV global | 32 % | 42,0 % | +10,0 pp | ±5 pp | **FUERA** |
| RF local | 26 % | 21,0 % | −5,0 pp | ±5 pp | En el límite |
| RV local | 10 % | 10,0 % | 0,0 pp | 7,5–12,5 % | OK |
| RV emergente | 6 % | 4,5 % | −1,5 pp | 4,5–7,5 % | En el límite |
| Inmobiliario | 8 % | 7,5 % | −0,5 pp | 6,0–10,0 % | OK |
| Liquidez | 18 % | 15,0 % | −3,0 pp | ±5 pp | OK |

**Paso 2 — calcula el riesgo actual contra la política.**

```text
desviación estándar de la cartera objetivo:  10,4 %
desviación estándar de la cartera actual:    12,6 %
límite de política:                          12,0 %  → EXCEDIDO

caída máxima estimada actual: −27,4 %
límite de política:           −25,0 %  → EXCEDIDO
```

**La cartera excede dos límites de política sin que el inversionista haya tomado ninguna decisión.**
Eso es exactamente lo que el rebalanceo corrige.

**Paso 3 — calcula las operaciones necesarias.**

```text
valores objetivo sobre 92 000 000:
  RV global      29 440 000   (actual 38 640 000)  → VENDER 9 200 000
  RF local       23 920 000   (actual 19 320 000)  → COMPRAR 4 600 000
  RV local        9 200 000   (actual  9 200 000)  → sin cambio
  RV emergente    5 520 000   (actual  4 140 000)  → COMPRAR 1 380 000
  inmobiliario    7 360 000   (actual  6 900 000)  → COMPRAR   460 000
  liquidez       16 560 000   (actual 13 800 000)  → COMPRAR 2 760 000
```

**Paso 4 — evalúa el costo.**

```text
volumen a operar: 9 200 000 de venta + 9 200 000 de compra
costo estimado: 0,30 % sobre el volumen operado = 27 600 por lado ≈ 55 200
efecto tributario: la venta de RV global realiza una ganancia
  ganancia estimada 4 100 000 · impuesto 20 % = 820 000
COSTO TOTAL DEL REBALANCEO: 875 200 (0,95 % de la cartera)
```

**Paso 5 — busca alternativas de menor costo.**

```text
opción A: rebalanceo completo con venta → costo 875 200
opción B: rebalanceo parcial, solo hasta el borde de la banda (37 %)
          vender 4 600 000 → costo estimado 450 000
          riesgo resultante: desviación estándar 11,6 % (dentro del límite) ✔
opción C: dirigir los próximos 12 meses de aportes a las clases rezagadas
          aporte mensual 500 000 × 12 = 6 000 000
          insuficiente para cerrar una brecha de 9 200 000, y sin costo tributario
opción D: combinación de B y C
          vender 4 600 000 ahora + dirigir aportes durante 12 meses
          costo inmediato 450 000, cierre progresivo de la brecha restante
```

**Paso 6 — decisión.**

```text
RECOMENDACIÓN: opción D

fundamento:
  · lleva el riesgo dentro del límite de política de inmediato (11,6 % < 12 %)
  · costo de 450 000 en lugar de 875 200: ahorro de 425 200
  · el resto de la brecha se cierra con aportes, sin costo de transacción
    ni efecto tributario
  · verificación trimestral para confirmar la convergencia

REGISTRO EN LA BITÁCORA
  fecha, motivo (banda excedida + límite de riesgo excedido),
  operaciones realizadas, costo, y estado posterior de cada límite
```

**Paso 7 — lo que NO se hace.**

```text
no se revisa la política de asignación

la RV global subió y ahora pesa más: eso NO es razón para aumentar
su objetivo del 32 % al 40 %

hacerlo sería justificar retrospectivamente el resultado del mercado,
que es el sesgo que el rebalanceo existe para contrarrestar
```

**Interpreta:** el rebalanceo obligó a **vender lo que más subió**, que es lo contrario del instinto, y
lo hizo por una razón objetiva: dos límites de política estaban excedidos. La opción elegida redujo el
costo a la mitad usando los aportes futuros. Y el paso 7 —**no cambiar la política**— es tan importante
como los seis anteriores.

## 🏦 Del cliente al banco

El cliente rebalancea y el banco cobra por cada operación. La tabla enfrenta las dos lecturas, y explica por qué el rebalanceo demasiado frecuente destruye su propio beneficio.

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| Bandas de tolerancia | Límites de exposición en el marco de apetito | 11, clase 12 |
| Tablero de seguimiento | Reporte de riesgo al comité | 11, clase 12 |
| Rebalanceo disciplinado | Gestión de carteras institucionales | 15, clase 5 |
| Revisión de política | Aprobación por el órgano de gobierno | 15, clase 12 |
| Bitácora de decisiones | Trazabilidad exigida en la asesoría | 12, clase 14 |

## 🧪 Práctica

El laboratorio pide rebalancear la misma cartera por calendario y por bandas y comparar costo y resultado. La comparación decide cuál conviene a cada tamaño de cartera.

En `labs/lab-06.md`, sección de rebalanceo:

1. Simula una cartera 60/40 durante 20 años con y sin rebalanceo y compara riesgo y retorno.
2. Diseña bandas para tu asignación objetivo y justifícalas.
3. Construye tu tablero de seguimiento con todos sus indicadores y umbrales.
4. Calcula el costo total de un rebalanceo y evalúa tres alternativas de menor costo.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen carteras que se desviaron o que se operaron de más. Las causas son bandas mal diseñadas o revisiones de política disfrazadas de rebalanceo.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| La cartera asume más riesgo del decidido | Deriva sin rebalanceo | Revisa las bandas trimestralmente. |
| Se rebalancea con demasiada frecuencia | Bandas muy estrechas | Amplía las bandas; mide el costo. |
| Se aumenta el objetivo de lo que subió | Justificación retrospectiva | El rebalanceo no cambia la política. |
| No se considera el efecto tributario | Costo subestimado | Inclúyelo en la evaluación de alternativas. |
| Se rebalancea vendiendo cuando hay aportes disponibles | Costo evitable | Dirige los aportes a las clases rezagadas. |
| Se "revisa la política" tras una caída | Reacción al mercado | Solo cambios de circunstancias justifican revisión. |

## ❓ Preguntas de comprobación

1. ¿Por qué una cartera se desalinea sola y qué riesgo implica?
2. ¿Cuál es el argumento sólido a favor del rebalanceo: retorno o riesgo?
3. ¿Cómo se diseñan bandas para clases de distinto peso?
4. Nombra tres gatillos legítimos y tres no legítimos de revisión de política.
5. ¿Cómo se rebalancea con el menor costo posible?

## 📥 Entregable

Guarda en `portfolio/parte-08/clase-14/`:

- la simulación de 20 años con y sin rebalanceo, con riesgo y retorno comparados;
- tus bandas diseñadas y justificadas por clase;
- tu tablero de seguimiento completo con umbrales;
- el cálculo de costo de un rebalanceo con tres alternativas evaluadas.

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

- Bodie, Z., Kane, A. y Marcus, A. (2023). *Investments* (13.ª ed.). McGraw-Hill. Capítulo 28: gestión y monitoreo de carteras.
- Vanguard (2022). *Best practices for portfolio rebalancing*. Comparación empírica de estrategias de rebalanceo.
- Perold, A. y Sharpe, W. (1988). "Dynamic Strategies for Asset Allocation". *Financial Analysts Journal*. Efecto de las reglas de rebalanceo.
- Ilmanen, A. (2011). *Expected Returns*. Wiley. Prima de rebalanceo y sus condiciones.
- CFA Institute (2023). *Investment Policy Statement guidance*. Distinción entre rebalanceo y revisión de política.
- Verificación local: verifica el efecto tributario de realizar ganancias en tu país antes de diseñar la estrategia de rebalanceo.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 13 · Costos, impuestos y sesgos](13-costos-impuestos-y-sesgos.md) | [Parte 08](../README.md) · [Programa](../../../SYLLABUS.md) | [15 · Proyecto: cartera simulada →](15-proyecto-cartera-simulada.md) |
<!-- gen:footer:end -->
