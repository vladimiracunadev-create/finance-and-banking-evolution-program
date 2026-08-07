---
part: 20
class: 7
title: "Stablecoins algorítmicas y su modo de fallo"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [estabilidad-financiera, disenio-de-producto, riesgo-de-modelo]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [FSB, BIS, IOSCO]
requires_legal_review: false
---

<!-- gen:header:start -->
# Clase 07 · Stablecoins algorítmicas y su modo de fallo

> [← 06 · Pérdida de paridad: anatomía de una corrida](06-perdida-de-paridad-anatomia-de-una-corrida.md) · [Índice de la parte](../README.md) · [08 · Depósitos tokenizados y dinero de banco comercial →](08-depositos-tokenizados-y-dinero-de-banco-comercial.md)

**Parte 20 — Activos digitales, stablecoins y dinero programable** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Analizar el diseño en el que **la garantía es el propio sistema**. No se estudia
para replicarlo: se estudia porque su modo de fallo es matemático, se puede
calcular por adelantado y aparece disfrazado en otros productos.

## 📚 Objetivos

Al finalizar podrás:

1. **Describir** el mecanismo de acuñación y quema de un diseño de dos tokens.
2. **Demostrar** por qué el respaldo endógeno es circular.
3. **Calcular** el punto en que el rescate deja de ser posible.
4. **Reconocer** el mismo mecanismo cuando aparece con otro nombre.
5. **Explicar** por qué un rendimiento sostenido por emisión no es un
   rendimiento.

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
| `respaldo endógeno` | El colateral es un activo del propio sistema |
| `acuñación y quema` | Crear y destruir unidades según una regla de canje |
| `dilución` | Emitir para pagar reduce el valor de cada unidad |
| `espiral` | Cada paso del mecanismo empeora la condición inicial |
| `capitalización absorbente` | Valor del token secundario disponible para absorber pérdidas |
| `rendimiento por emisión` | Pago financiado creando unidades, no con ingresos |
| `punto de agotamiento` | Nivel donde la absorción ya no cubre |
| `reflexividad` | El precio sostiene la demanda que sostiene el precio |

## 🧠 Modelo mental

```text
EL DISEÑO DE DOS TOKENS

  TOKEN E (estable)   pretende valer 1
  TOKEN V (variable)  absorbe la variación

  REGLA: siempre se puede canjear
         1 unidad de E por 1 de valor en V

  SI E COTIZA A 0,98
    compro E a 0,98, lo canjeo por 1 de V,
    vendo V y gano 0,02
    → la compra de E empuja su precio arriba

  EL MECANISMO FUNCIONA...
  MIENTRAS V VALGA ALGO

  ¿Y DE QUÉ DEPENDE EL VALOR DE V?
    de que el sistema funcione
    → es decir, de que E mantenga la paridad

  → EL RESPALDO ES CIRCULAR.
    No hay ningún activo fuera del sistema.
```

## 📖 Desarrollo

### 1. Por qué funciona en calma

```text
CON DEMANDA CRECIENTE DE E

  entran fondos → se acuña E quemando V
  → la oferta de V baja → V sube
  → la capitalización absorbente crece
  → el sistema parece cada vez más sólido

Y ESA APARIENCIA ES EL PROBLEMA:
la solidez medida crece justo cuando
la exposición crece, porque ambas
son la misma cosa vista dos veces.
```

### 2. La espiral

```text
CON SALIDA DE FONDOS

  1  E cotiza por debajo de 1
  2  los tenedores canjean E por V
  3  se emite V para pagar el canje
  4  la oferta de V crece
  5  V cae
  6  hace falta emitir MÁS V por cada E
  7  vuelve a 4

  CADA VUELTA ES MÁS RÁPIDA QUE LA ANTERIOR
  porque la cantidad emitida crece de forma
  multiplicativa, no aditiva

  Y NO HAY NADA FUERA DEL SISTEMA
  QUE PUEDA DETENERLA
```

### 3. El rendimiento como acelerador

```text
MUCHOS DISEÑOS OFRECEN UN RENDIMIENTO ALTO
SOBRE EL TOKEN ESTABLE

  ¿DE DÓNDE SALE?
    a  ingresos reales (comisiones, préstamos)
    b  emisión de nuevas unidades

  SI ES b, NO ES UN RENDIMIENTO:
  es una transferencia de los que entran
  después a los que entraron antes

CÓMO SE COMPRUEBA
  compara el rendimiento pagado con
  los ingresos declarados del protocolo

  si el rendimiento pagado es mayor,
  la diferencia es dilución

EFECTO SOBRE EL RIESGO
  el rendimiento atrae depósitos
  → la exposición crece
  → el día de la salida es mayor
```

### 4. Reconocerlo con otro nombre

```text
EL MISMO MECANISMO APARECE COMO:

  · «respaldado por el token de gobernanza»
  · «colateralizado con el activo nativo»
  · «estabilizado por incentivos de mercado»
  · «reserva parcial con módulo algorítmico»
  · «respaldado por acciones de la propia sociedad»

LA PRUEBA QUE LOS DETECTA TODOS
  rastrea el respaldo paso a paso
  y pregunta en cada uno:
  «¿este activo pierde valor si el instrumento
   principal pierde la paridad?»

  si la respuesta es SÍ en algún paso,
  ese respaldo no absorbe: amplifica
```

### 5. Diseños híbridos

```text
UN HÍBRIDO TIENE UNA PARTE EXÓGENA
Y OTRA ENDÓGENA

  ejemplo: 70 % en deuda pública,
           30 % en token propio

  EN CALMA la cobertura parece del 100 %
  EN TENSIÓN el 30 % puede ir a cero

  → LA COBERTURA EFECTIVA EN TENSIÓN
    ES EL TRAMO EXÓGENO: 70 %

REGLA DE ANÁLISIS
  la cobertura de un híbrido se calcula
  SIEMPRE con el tramo endógeno a cero,
  porque ese es el escenario en el que
  la cobertura importa
```

## 🧮 Ejemplo guiado

**Situación.** Un diseño de dos tokens con datos sintéticos. Hay que calcular
cuánto aguanta y en qué punto la espiral se vuelve irreversible.

```text
SITUACIÓN INICIAL
  E en circulación            2 000 000 000
  precio de E                          1,000
  V en circulación              400 000 000 unid.
  precio de V                          3,000
  capitalización de V         1 200 000 000

  RATIO DE ABSORCIÓN
  1 200 000 000 / 2 000 000 000 = 60 %

  ingresos reales del protocolo    42 000 000 /año
  rendimiento pagado sobre E             12 % /año
```

**Paso 1 — comprueba si el rendimiento es real.**

```text
RENDIMIENTO PAGADO
  2 000 000 000 × 12 % = 240 000 000 al año

INGRESOS REALES
  42 000 000

DIFERENCIA FINANCIADA POR EMISIÓN
  240 000 000 − 42 000 000 = 198 000 000

  → EL 82,5 % DEL RENDIMIENTO ES DILUCIÓN

  en unidades de V a precio 3,000:
  198 000 000 / 3 = 66 000 000 unidades al año
  sobre 400 000 000 existentes = 16,5 % anual
  de dilución permanente
```

**Paso 2 — modela la primera salida.**

```text
SALEN 200 000 000 DE E (10 % del circulante)

  se emite V por 200 000 000 de valor
  a precio 3,000 → 66 666 667 unidades nuevas

  V pasa de 400 000 000 a 466 666 667 unidades

  SI LA CAPITALIZACIÓN NO CAMBIARA,
  el precio sería 1 200 / 466,67 = 2,571

  pero la capitalización TAMPOCO se mantiene:
  quien recibe V lo vende
```

**Paso 3 — añade la venta del V recibido.**

```text
SUPUESTO · EL 70 % DEL V RECIBIDO SE VENDE
Y LA PROFUNDIDAD DEL MERCADO ABSORBE
CON UN IMPACTO DEL 1 % POR CADA 20 000 000
DE VENTA

  valor vendido = 200 000 000 × 70 % = 140 000 000
  impacto = 140 / 20 = 7 %

  precio de V = 2,571 × (1 − 7 %) = 2,391

  capitalización de V
  466 666 667 × 2,391 = 1 115 800 000

  E restante = 1 800 000 000
  RATIO DE ABSORCIÓN = 61,99 %
```

**Paso 4 — repite la vuelta.**

```text
SEGUNDA SALIDA DE 200 000 000 DE E

  unidades emitidas = 200 000 000 / 2,391
                    = 83 647 000
  V total = 550 313 667

  precio antes de vender
  1 115 800 000 / 550 313 667 = 2,027

  venta del 70 % → impacto 7 %
  precio = 1,885
  capitalización = 1 037 341 000

  E restante = 1 600 000 000
  RATIO = 64,83 %

OBSERVACIÓN IMPORTANTE
  el ratio SUBE mientras el precio de V
  se derrumba, porque E cae más deprisa
  → el ratio no es el indicador útil
```

**Paso 5 — encuentra el indicador que sí sirve.**

```text
UNIDADES DE V EMITIDAS POR CADA E RETIRADO

  primera vuelta   66 666 667 / 200 000 000 = 0,333
  segunda vuelta   83 647 000 / 200 000 000 = 0,418

  crecimiento: 25,5 %

TERCERA VUELTA con precio 1,885
  106 100 796 / 200 000 000 = 0,531  (+27,0 %)

CUARTA con precio ≈ 1,753
  114 090 000 / 200 000 000 = 0,570

EL RITMO DE EMISIÓN POR UNIDAD RETIRADA
CRECE EN CADA VUELTA
→ ESE ES EL INDICADOR DE LA ESPIRAL
```

**Paso 6 — calcula el punto de agotamiento.**

```text
LA ESPIRAL SE VUELVE IRREVERSIBLE CUANDO
LA EMISIÓN NECESARIA SUPERA LO QUE EL MERCADO
DE V PUEDE ABSORBER SIN LLEVAR EL PRECIO A CERO

  CRITERIO OPERATIVO
  cuando la venta diaria de V supera
  N veces su volumen medio diario

  volumen medio diario de V   60 000 000
  venta generada por vuelta  140 000 000
  → 2,3 veces el volumen en UNA vuelta

  CON DOS VUELTAS EN UN DÍA
  la venta es 4,6 veces el volumen normal
  → el impacto del 7 % supuesto es OPTIMISTA

CONCLUSIÓN DEL CÁLCULO
  el diseño no soporta una salida
  del 20 % en un día
```

**Paso 7 — compara con el diseño respaldado.**

```text
UN EMISOR CON RESERVA EXÓGENA
ANTE LA MISMA SALIDA DEL 20 %

  vende 400 000 000 de letras
  con un descuento del 0,20 %
  coste = 800 000

  la reserva restante SIGUE SIENDO
  deuda pública

LA DIFERENCIA NO ES DE GRADO.
En un caso el activo que paga es ajeno
al problema; en el otro ES el problema.
```

**Interpreta:** el ratio de absorción **subió durante toda la espiral** y habría
tranquilizado a cualquiera que lo vigilara. El indicador que funciona es la
**emisión por unidad retirada**, porque mide la aceleración del mecanismo en vez
de una foto de su estado.

## 🧭 Perspectivas

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un 12 % de rendimiento | Si deposita |
| Inversionista | Una capitalización que crece | Qué peso le da |
| Fintech | Un producto de rendimiento | Si lo ofrece a sus usuarios |
| Banco | Riesgo reputacional y de contagio | Si lo permite en sus rieles |
| Emisor | Crecimiento y comisiones | Si lo comunica con honestidad |
| Mercado | Volumen creciente | Si provee liquidez a V |
| Supervisor | Un producto con fallo previsible | Qué advertencia o prohibición aplica |
| Auditor | Sin activos externos que verificar | Qué puede opinar |
| Sociedad | Pérdidas concentradas en minoristas | Qué educación y qué límite exige |

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Paga 12 %, es mejor que el depósito» | El 82,5 % de ese pago es dilución | 20, clase 7 |
| «Está respaldado por el otro token» | El respaldo es circular | 20, clase 7 |
| «El ratio de cobertura mejoró» | Subió mientras el sistema se hundía | 20, clase 7 |

## ⚖️ Riesgos y controles

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Respaldo circular | El colateral es del propio sistema | Rastrear hasta un activo externo |
| Rendimiento por dilución | Se paga emitiendo | Comparar con ingresos declarados |
| Indicador engañoso | El ratio sube durante el colapso | Medir emisión por unidad retirada |
| Híbrido mal contado | Se suma el tramo endógeno | Calcular con ese tramo a cero |
| Liquidez del token absorbente | Venta muy superior al volumen | Medir venta generada frente a volumen |
| Exposición indirecta | Un tercero lo tiene y el banco a él | Mapa de exposición de segundo grado |

## 🧪 Práctica

En [`labs/lab-05.md`](../labs/lab-05.md):

1. Implementa el mecanismo de acuñación y quema con impacto de mercado.
2. Mide el ratio de absorción y la emisión por unidad retirada en cada vuelta.
3. Demuestra que el primero sube mientras el segundo se dispara.
4. Calcula la salida máxima que el diseño soporta en un día.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Vigilar el ratio de absorción | Es el análogo de la cobertura | Sube durante el colapso |
| Aceptar el rendimiento | No se pregunta de dónde sale | Compáralo con los ingresos reales |
| Sumar el tramo endógeno | Aparece en la tabla de reservas | Cuéntalo a cero en tensión |
| Impacto de mercado constante | Simplifica el modelo | Crece con el tamaño de la venta |
| Creer que es un caso pasado | Cambia de nombre | Rastrea el respaldo, no la etiqueta |
| Confundir con sobrecolateralización | Ambos hablan de colateral | Importa si el colateral es externo |

## ❓ Preguntas de comprobación

1. ¿Por qué el respaldo endógeno es circular y qué prueba lo detecta?
2. ¿Cómo se distingue un rendimiento real de uno financiado por emisión?
3. ¿Por qué el ratio de absorción sube durante la espiral?
4. ¿Cuál es el indicador correcto y por qué?
5. ¿Cómo se calcula la cobertura de un diseño híbrido?

## 📥 Entregable

Guarda en `portfolio/parte-20/clase-07/`:

- la simulación de la espiral con al menos cuatro vueltas;
- la comparación entre ratio de absorción y emisión por unidad retirada;
- el desglose del rendimiento entre ingresos reales y dilución;
- la lista de nombres comerciales bajo los que aparece el mismo mecanismo.

## 🔗 Referencias cruzadas

- **Viene de:** clases 3 y 6.
- **Continúa en:** clases 13 y 14 de esta parte.
- **Se aplica en:** Parte 22, clase 5; Parte 23, clase 14.

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

- Bank for International Settlements (2023). *Stablecoins: fundamentals, emerging issues and open questions*. BIS. <https://www.bis.org/publ/work905.htm>
- Financial Stability Board (2022). *Assessment of Risks to Financial Stability from Crypto-assets*. FSB. <https://www.fsb.org/2022/02/assessment-of-risks-to-financial-stability-from-crypto-assets/>
- IOSCO (2022). *Decentralized Finance Report*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD699.pdf>
- Bank for International Settlements (2022). *Annual Economic Report*, capítulo III. BIS. <https://www.bis.org/publ/arpdf/ar2022e3.htm>
- Verificación local: comprueba si tu jurisdicción prohíbe, restringe o somete a advertencia expresa los instrumentos con estabilización algorítmica. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 06 · Pérdida de paridad: anatomía de una corrida](06-perdida-de-paridad-anatomia-de-una-corrida.md) | [Parte 20](../README.md) · [Programa](../../../SYLLABUS.md) | [08 · Depósitos tokenizados y dinero de banco comercial →](08-depositos-tokenizados-y-dinero-de-banco-comercial.md) |
<!-- gen:footer:end -->
