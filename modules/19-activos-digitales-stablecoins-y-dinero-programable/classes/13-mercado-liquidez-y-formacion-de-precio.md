---
part: 20
class: 13
title: "Mercado, liquidez y formación de precio"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [integridad-del-mercado, liquidez, transparencia]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [IOSCO, FSB, BIS]
requires_legal_review: false
---

<!-- gen:header:start -->
# Clase 13 · Mercado, liquidez y formación de precio

> [← 12 · Custodia de activos digitales](12-custodia-de-activos-digitales.md) · [Índice de la parte](../README.md) · [14 · Contagio y riesgo sistémico →](14-contagio-y-riesgo-sistemico.md)

**Parte 20 — Activos digitales, stablecoins y dinero programable** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Medir la liquidez de un mercado de activos digitales con las herramientas de la
Parte 8, sin importar los eslóganes. **El volumen no es liquidez**, y la
diferencia se nota exactamente el día en que hay que vender.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** volumen, profundidad, amplitud y resiliencia.
2. **Calcular** el impacto en el precio de una orden grande sobre un libro dado.
3. **Explicar** cómo se forma el precio de referencia y por qué es manipulable.
4. **Identificar** las prácticas que inflan el volumen sin aportar liquidez.
5. **Evaluar** la fragmentación entre plataformas y su efecto sobre la ejecución.

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
| `volumen` | Cantidad negociada en un periodo |
| `profundidad` | Importe disponible cerca del precio actual |
| `amplitud` | Diferencia entre compra y venta |
| `resiliencia` | Velocidad de reposición del libro tras una orden |
| `impacto de mercado` | Movimiento del precio causado por la propia orden |
| `fragmentación` | Liquidez repartida entre plataformas |
| `precio de referencia` | Valor compuesto usado por terceros |
| `operación circular` | Compraventa entre partes vinculadas que infla volumen |

## 🧠 Modelo mental

```text
LAS CUATRO DIMENSIONES, Y SOLO SE PUBLICA UNA

  VOLUMEN        cuánto se negoció ayer
                 → es la que aparece en todas partes
                 → puede inflarse sin coste real

  AMPLITUD       cuánto cuesta entrar y salir ya
                 → visible, pero solo para el
                   primer tramo

  PROFUNDIDAD    cuánto puedo vender sin mover
                 el precio un 1 %
                 → hay que medirla; casi nadie lo hace

  RESILIENCIA    en cuánto tiempo vuelve el libro
                 → solo se observa tras una orden real

LA QUE DECIDE SI PUEDES SALIR
ES LA TERCERA.
```

## 📖 Desarrollo

### 1. Por qué el volumen engaña

```text
FORMAS DE VOLUMEN SIN LIQUIDEZ

  · operaciones entre cuentas del mismo titular
  · programas que pagan por operar
  · comisiones negativas para ciertos operadores
  · órdenes que se cruzan entre dos algoritmos
    del mismo proveedor

  TODAS PRODUCEN VOLUMEN REAL EN LA CINTA
  Y CERO CAPACIDAD DE ABSORBER UNA VENTA

CÓMO SE DETECTA
  · relación entre volumen y profundidad:
    un volumen alto con libro fino es
    la señal más clara
  · concentración por horario y por tamaño
  · comparación con plataformas equivalentes
```

### 2. Medir profundidad

```text
PROCEDIMIENTO

  1 toma una foto del libro
  2 acumula el importe disponible por niveles
  3 halla el importe que mueve el precio un 1 %
  4 repite para 2 % y 5 %
  5 hazlo en varios momentos del día
     y en día de tensión, no solo en calma

RESULTADO ÚTIL
  «para mover el precio un 1 % hacen falta
   X; una posición de Y equivale a Z veces
   ese importe»

ESE COCIENTE Y/X ES EL DATO
QUE DEBE ESTAR EN EL LÍMITE DE POSICIÓN
```

### 3. El precio de referencia

```text
CÓMO SE COMPONE

  varias plataformas → se filtra → se pondera
  → se publica un precio

  DECISIONES QUE PARECEN TÉCNICAS
  Y NO LO SON
    · qué plataformas entran
    · cómo se ponderan
    · qué se hace con una plataforma caída
    · si se usa mediana o media (Parte 19, clase 9)
    · qué ventana temporal

CADA UNA CAMBIA EL PRECIO PUBLICADO
Y, CON ÉL, LIQUIDACIONES, VALORACIONES
Y GARANTÍAS

  → EL PRECIO DE REFERENCIA ES UN ÍNDICE,
    y los índices tienen un régimen propio
    por una razón
```

### 4. Fragmentación

```text
LA MISMA POSICIÓN EN 6 PLATAFORMAS

  VENTAJA   más profundidad agregada
  PROBLEMA  no es accesible a la vez:
            hay que mover fondos entre ellas,
            y eso lleva tiempo y riesgo

EFECTO EN TENSIÓN
  · los retiros se ralentizan justo cuando
    hacen falta
  · el precio diverge entre plataformas
  · el arbitraje que igualaba los precios
    depende de mover fondos, y no puede

  → LA PROFUNDIDAD AGREGADA EN CALMA
    SOBREESTIMA LA DISPONIBLE EN TENSIÓN
```

### 5. Prácticas que distorsionan

```text
QUÉ VIGILAR EN UN MERCADO

  · órdenes grandes que se cancelan antes
    de ejecutarse, de forma repetida
  · movimientos bruscos en momentos de poca
    actividad, cerca de una hora de cálculo
    de referencia
  · concentración de la contraparte
  · diferencias persistentes entre plataformas
    sin arbitraje

QUÉ HACE UN PARTICIPANTE RESPONSABLE
  · no participar en operaciones circulares
  · no operar contra información propia
    no pública
  · registrar y reportar lo anómalo
  · no calcular su valoración con un solo
    precio de una sola plataforma

Este curso NO enseña a manipular mercados
ni proporciona herramientas para ello:
enseña a detectarlo y a protegerse.
```

## 🧮 Ejemplo guiado

**Situación.** Una tesorería tiene 12 000 000 en un activo digital y necesita
saber en cuánto tiempo puede salir sin destruir el precio.

```text
LIBRO DE ÓRDENES AGREGADO (compra)
  nivel      precio    importe acumulado
  1          100,00           420 000
  2           99,50         1 150 000
  3           99,00         2 080 000
  4           98,00         3 340 000
  5           96,00         5 100 000
  6           93,00         7 800 000
  7           88,00        11 200 000

VOLUMEN DIARIO PUBLICADO      184 000 000
POSICIÓN A LIQUIDAR            12 000 000
```

**Paso 1 — mide la profundidad al 1 % y al 5 %.**

```text
PRECIO ACTUAL 100,00

  −1 %  → 99,00  → 2 080 000 absorbibles
  −2 %  → 98,00  → 3 340 000
  −5 %  → 95,00  → interpolando entre
          96,00 (5 100 000) y 93,00 (7 800 000):
          5 100 000 + (1/3)×2 700 000
        = 6 000 000

PROFUNDIDAD AL 1 %: 2 080 000
```

**Paso 2 — calcula el cociente de la posición.**

```text
POSICIÓN / PROFUNDIDAD AL 1 %
  12 000 000 / 2 080 000 = 5,77

  → LA POSICIÓN ES CASI 6 VECES
    LO QUE EL MERCADO ABSORBE
    CON UN 1 % DE IMPACTO
```

**Paso 3 — compara con el volumen publicado.**

```text
POSICIÓN / VOLUMEN DIARIO
  12 000 000 / 184 000 000 = 6,5 %

  ESE COCIENTE PARECE CÓMODO
  y es completamente engañoso:

  el volumen incluye operaciones que no
  aportan profundidad; el libro real solo
  absorbe 2,08 millones con un 1 % de impacto

DOS MÉTRICAS, CONCLUSIONES OPUESTAS.
La correcta es la del libro.
```

**Paso 4 — calcula el coste de vender todo de golpe.**

El libro está expresado en **importe acumulado**, de modo que la venta consume
tramos sucesivos. Cada tramo es la diferencia con el nivel anterior.

```text
VENTA DE 12 000 000 UNIDADES CONTRA EL LIBRO

  tramo 1     420 000 a 100,00 =    42 000 000
  tramo 2     730 000 a  99,50 =    72 635 000
  tramo 3     930 000 a  99,00 =    92 070 000
  tramo 4   1 260 000 a  98,00 =   123 480 000
  tramo 5   1 760 000 a  96,00 =   168 960 000
  tramo 6   2 700 000 a  93,00 =   251 100 000
  tramo 7   3 400 000 a  88,00 =   299 200 000
  acumulado 11 200 000

  faltan      800 000 por debajo de 88,00
  supuesto: se ejecutan a 84,00 = 67 200 000

  INGRESO TOTAL = 1 116 645 000
  para 12 000 000 de unidades
  PRECIO MEDIO = 93,05

  VALOR TEÓRICO A 100,00
  12 000 000 × 100,00 = 1 200 000 000

  IMPACTO = 100,00 → 93,05 = −6,95 %
  PÉRDIDA = 1 200 000 000 − 1 116 645 000
          =    83 355 000
```

**Paso 5 — calcula la venta escalonada.**

```text
SUPUESTO · EL LIBRO SE REPONE UN 70 %
CADA 30 MINUTOS

  vender 1 500 000 por sesión de 30 min
  → impacto por sesión ≈ 0,70 %

  sesiones necesarias: 12 000 000 / 1 500 000 = 8
  tiempo total: 4 horas

  IMPACTO ACUMULADO
  cada sesión deja un residuo del 30 %
  que la reposición no recupera:
  0,70 % × [1 + 7 × 0,30] = 2,17 %

COMPARACIÓN SOBRE EL VALOR DE LA POSICIÓN

  VENTA DE GOLPE   1 200 000 000 × 6,95 %
                 =    83 400 000

  VENTA ESCALONADA 1 200 000 000 × 2,17 %
                 =    26 040 000

  AHORRO POR ESCALONAR: 57 360 000
  a cambio de 4 horas de exposición al mercado
```

**Paso 6 — evalúa el riesgo de esas 4 horas.**

```text
DURANTE 4 HORAS EL PRECIO PUEDE MOVERSE
POR OTRAS RAZONES

  volatilidad diaria supuesta      5,2 %
  volatilidad en 4 horas
  5,2 % × √(4/24) = 2,12 %

  → EL RIESGO DE ESPERAR (2,12 %)
    ES DEL MISMO ORDEN QUE EL AHORRO
    DE ESCALONAR (4,78 puntos)

  CONCLUSIÓN: escalonar sigue compensando,
  pero no por un margen cómodo,
  y en un día de tensión la relación se invierte
```

**Paso 7 — deriva el límite de posición.**

```text
REGLA PROPUESTA

  posición máxima = 3 × profundidad al 1 %

  con profundidad de 2 080 000
  → límite de 6 240 000

  la posición actual de 12 000 000
  DUPLICA el límite

  Y EL LÍMITE SE RECALCULA MENSUALMENTE
  CON UNA MEDICIÓN DEL LIBRO,
  no con el volumen publicado
```

**Interpreta:** el cociente sobre volumen decía 6,5 % y sugería tranquilidad; el
cociente sobre profundidad decía 5,77 veces y decía la verdad. **La liquidez se
mide en el libro, no en la cinta**, y el límite de posición tiene que colgar de
la medición, no del dato publicado.

## 🧭 Perspectivas

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un precio en pantalla | Si compra o vende |
| Inversionista | Un volumen alto | Qué tamaño toma |
| Fintech | Un precio para su producto | Qué fuente usa |
| Banco | Un límite de posición | Cómo lo calibra |
| Custodio | Movimientos entre plataformas | Cómo los autoriza |
| Mercado | Órdenes y cancelaciones | Cómo provee liquidez |
| Infraestructura | Fragmentación | Si interconecta |
| Supervisor | Prácticas anómalas | Qué investiga |
| Auditor | Valoración a precio de mercado | Qué jerarquía aplica |
| Sociedad | Precios que parecen sólidos | Qué transparencia exige |

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Mueve 184 millones al día» | Absorbe 2 con un 1 % de impacto | 20, clase 13 |
| «Vendo cuando quiera» | Salir cuesta el 7 % de golpe | 20, clase 13 |
| «El precio es 100» | Es un índice con decisiones dentro | 20, clase 13 |

## ⚖️ Riesgos y controles

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Confundir volumen con liquidez | Se usa el dato publicado | Medir el libro y el impacto |
| Límite de posición mal calibrado | Se fija sobre volumen | Colgarlo de la profundidad al 1 % |
| Fragmentación en tensión | No se puede mover fondos | Medir profundidad accesible, no agregada |
| Precio de referencia manipulable | Ventana y ponderación | Mediana, varias fuentes y mínimo vivo |
| Operaciones circulares | Inflan el volumen | Contrastar volumen con profundidad |
| Valoración con una sola fuente | Es lo simple | Componer y documentar el método |

## 🧪 Práctica

En [`labs/lab-07.md`](../labs/lab-07.md):

1. Mide profundidad al 1 %, 2 % y 5 % sobre un libro dado.
2. Calcula el impacto de una venta de golpe y de una escalonada.
3. Compara el ahorro de escalonar con el riesgo del tiempo de exposición.
4. Deriva un límite de posición y justifícalo.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar volumen | Es el dato disponible | Mide el libro |
| Ignorar la reposición | Complica el cálculo | Determina si escalonar compensa |
| No cronometrar la salida | Se supone instantánea | El tiempo tiene su propio riesgo |
| Sumar profundidad de plataformas | Parece razonable | No es accesible a la vez |
| Un solo precio | Es lo cómodo | Compón y documenta |
| Medir solo en calma | Es cuando se hacen los informes | Mide también en tensión |

## ❓ Preguntas de comprobación

1. ¿Cuáles son las cuatro dimensiones de la liquidez y cuál decide la salida?
2. ¿Cómo puede haber volumen alto con profundidad baja?
3. ¿Qué decisiones esconde un precio de referencia?
4. En el ejemplo, ¿por qué las dos métricas dan conclusiones opuestas?
5. ¿Cómo se calibra un límite de posición y con qué frecuencia?

## 📥 Entregable

Guarda en `portfolio/parte-20/clase-13/`:

- la medición de profundidad a tres niveles;
- el cálculo del impacto de golpe y escalonado, con el riesgo del tiempo;
- el límite de posición derivado y su justificación;
- la lista de señales de volumen inflado que revisarías.

## 🔗 Referencias cruzadas

- **Viene de:** Parte 8, mercados; clase 2 de esta parte.
- **Continúa en:** clase 14 de esta parte.
- **Se aplica en:** Parte 21, clases 6 y 7; Parte 22, clase 10; Parte 23,
  clase 11.

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
- IOSCO (2013). *Principles for Financial Benchmarks*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD415.pdf>
- Financial Stability Board (2022). *Assessment of Risks to Financial Stability from Crypto-assets*. FSB. <https://www.fsb.org/2022/02/assessment-of-risks-to-financial-stability-from-crypto-assets/>
- Bank for International Settlements (2022). *Annual Economic Report*, capítulo III. BIS. <https://www.bis.org/publ/arpdf/ar2022e3.htm>
- Verificación local: comprueba qué régimen de integridad de mercado y de índices de referencia aplica en tu jurisdicción a estas plataformas y a los precios que publican. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 12 · Custodia de activos digitales](12-custodia-de-activos-digitales.md) | [Parte 20](../README.md) · [Programa](../../../SYLLABUS.md) | [14 · Contagio y riesgo sistémico →](14-contagio-y-riesgo-sistemico.md) |
<!-- gen:footer:end -->
