<!-- meta
part: 23
class: 10
title: "Liquidación y sus modos de fallo"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [liquidacion, atomicidad, riesgo-operativo]
regulation_last_verified: 2026-08-20
regulatory_status: vigente
primary_authorities: [CPMI, IOSCO, BIS]
requires_legal_review: false
-->

<!-- gen:header:start -->
# Clase 10 · Liquidación y sus modos de fallo

> [← 09 · Custodia y gestión de claves](09-custodia-y-gestion-de-claves.md) · [Índice de la parte](../README.md) · [11 · Pagos y conexión con el exterior →](11-pagos-y-conexion-con-el-exterior.md)

**Parte 23 — Proyecto — banco digital y mercado tokenizado** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Construir el motor de liquidación y **probar cada uno de sus modos de fallo**,
porque la atomicidad se demuestra por lo que no ocurre, no por lo que ocurre.

La clase 7 estableció que la atomicidad es alcanzable en el componente de
colateral. Esta la implementa y, sobre todo, la prueba: cada tramo que falla debe
dejar el otro intacto, y el sistema detenido debe rechazar sin tocar nada.

## 📚 Objetivos

Al finalizar podrás:

1. **Implementar** la liquidación que rechaza antes de bloquear.
2. **Probar** la ausencia de estado intermedio observable.
3. **Enumerar** los riesgos que la atomicidad no elimina.
4. **Calcular** el ahorro neto tras restar el coste de liquidez.
5. **Dimensionar** el fallo del ciclo completo.

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

Los cuatro primeros términos son la atomicidad y su prueba; los cuatro siguientes, los riesgos que no elimina. El **fallo del ciclo** es el modo que nadie prueba: no falla una parte, falla el registro entero, y el sistema tiene que rechazar sin tocar nada.

| Concepto | Comprensión verificable |
|---|---|
| `atomicidad` | Todos los movimientos ocurren o ninguno |
| `estado intermedio` | Momento con un tramo movido y el otro no |
| `rechazo previo` | Verificar antes de bloquear nada |
| `neteo` | Compensar el ciclo y liquidar el saldo |
| `riesgo de reemplazo` | Coste de rehacer la operación fallida |
| `riesgo de emisor` | El del dinero con el que se liquida |
| `saldo prefinanciado` | Fondos inmovilizados para liquidar |
| `fallo del ciclo` | Cuando falla el neteo entero |

## 🧠 Modelo mental

La atomicidad no se mide en milisegundos. Se demuestra intentando observar un
estado a medias y no encontrándolo, y por eso el diseño expone el estado completo
en vez de esconderlo.

```text
LA SECUENCIA CORRECTA

  1 verificar que el vendedor tiene el activo
  2 verificar que el comprador tiene el dinero
  3 si falla cualquiera → RECHAZAR sin tocar
  4 si no → los cuatro movimientos juntos

RECHAZAR NO DEJA RASTRO.
BLOQUEAR Y REVERTIR, SÍ, y ese rastro
es un estado intermedio en el que alguien
pudo actuar.
```

## 📖 Desarrollo

### 1. Los cinco riesgos y el que se elimina

Presentar la atomicidad como si resolviera la liquidación entera es el error de
esta clase. Elimina uno de cinco, y los otros cuatro necesitan su propio
control.

```text
principal   ELIMINADO por la atomicidad
reemplazo   subsiste: rehacer a otro precio
liquidez    subsiste: el saldo comprometido
operativo   subsiste: el registro se detiene
jurídico    subsiste: la finalidad legal

Y UN SEXTO QUE APARECE AL LLEVARLA
A UN REGISTRO
  el riesgo del emisor del dinero
```

### 2. El neteo y su riesgo nuevo

Combinar neteo con liquidación atómica captura la eficiencia de liquidez del
primero y la ausencia de riesgo de principal de la segunda. A cambio concentra
el fallo.

```text
CON NETEO
  se compensa el ciclo y se liquida el
  saldo como una sola unidad

  → menos saldo prefinanciado
  → y si falla, fallan TODAS las
    operaciones del ciclo

HAY QUE DIMENSIONAR ESE ESCENARIO
  volumen del ciclo × variación de precio
  × probabilidad de fallo
```

### 3. Las pruebas que hay que escribir

No basta con probar que funciona. Hay que probar que cada fallo deja el sistema
en un estado consistente, y eso son cinco pruebas que se escriben una vez y valen
para siempre.

```text
1 no hay estado intermedio observable
2 fallo del tramo de activo → dinero intacto
3 fallo del tramo de dinero → activo intacto
4 dos operaciones sobre el mismo saldo:
  solo una se ejecuta
5 registro detenido → rechaza sin tocar nada

LA 5 ES LA QUE NADIE ESCRIBE
```

## 🧮 Ejemplo guiado

El ejemplo somete el liquidador a sus cinco modos de fallo. La quinta prueba —el registro detenido— es la que casi nadie escribe y la que más se activa.

**Situación.** El equipo implementa la liquidación del colateral y calcula el
ahorro neto.

```text
DATOS
  volumen diario de colateral   1 200 000
  operaciones diarias                  18
  ciclo actual                        T+1
  probabilidad de incumplimiento
    a 1 día                        0,003 %
  recuperación                        45 %
  coste de financiación              4,3 %
  saldo sin neteo                     22 %
  saldo con neteo                     12 %
```

**Paso 1 — calcula la pérdida esperada sin atomicidad.**

```text
exposición = 1 200 000 × 1 = 1 200 000
pérdida diaria
  1 200 000 × 0,00003 × 0,55 = 19,8
anual (250 días) = 4 950
```

**Paso 2 — calcula el coste de liquidez.**

```text
sin neteo
  1 200 000 × (22 % − 6 %) × 4,3 % = 8 256
con neteo
  1 200 000 × (12 % − 6 %) × 4,3 % = 3 096

  CON NETEO EL AHORRO NETO ES
  4 950 − 3 096 = 1 854 al año
```

**Paso 3 — dimensiona el fallo del ciclo.**

```text
si falla el neteo, fallan las 18 operaciones

  volumen 1 200 000
  variación de precio en un día 0,4 %
  coste de reemplazo 4 800 por episodio

  disponibilidad 99,9 % → 0,25 días al año
  coste esperado 1 200 al año

  AHORRO NETO CORREGIDO
  1 854 − 1 200 = 654 al año
```

**Paso 4 — concluye con honestidad.**

```text
EL AHORRO ES DE 654 AL AÑO

  ¿justifica la complejidad?
  por sí solo, no

  LO QUE SÍ LA JUSTIFICA
  · el colateral se libera en el momento,
    y eso permite ofrecer crédito a plazos
    más cortos
  · el cliente recupera su garantía sin
    esperar un día

Y ESO ES UN BENEFICIO DE PRODUCTO,
no de riesgo, y hay que declararlo así
en vez de justificar la arquitectura con
un ahorro de 654
```

**Interpreta:** El ahorro por eliminar el riesgo de principal era de 654 al año, una cifra que no
justifica nada por sí sola. **Lo honesto fue reconocerlo y justificar la
arquitectura por el beneficio de producto** —liberar el colateral en el
momento— en vez de inflar el argumento de riesgo.

## 🧭 Perspectivas

La liquidación afecta a cada actor de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Su garantía liberada al instante | Si lo valora |
| Equipo | 654 de ahorro anual | Si justifica la complejidad |
| Tesorería | Saldo prefinanciado | Cómo lo financia |
| Riesgos | Cinco riesgos, uno eliminado | Qué controla los otros |
| Banco emisor | Saldos de liquidación | Qué límite acepta |
| Supervisor | Fallo del ciclo dimensionado | Qué verifica |
| Auditor | Cinco pruebas de fallo | Qué comprueba |
| Sociedad | Un mercado más rápido | — |

## 🏦 Del cliente al banco

El cliente ve una operación y el sistema elimina o no el riesgo de principal. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Es atómico, no hay riesgo» | Elimina uno de cinco | 23, clase 10 |
| «Ahorra mucho» | 654 al año | 23, clase 10 |
| «Nunca falla» | Y si falla el ciclo, fallan las 18 | 23, clase 10 |

## ⚖️ Riesgos y controles

Los riesgos residuales son de reemplazo, de emisor y de ciclo. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Presentar la atomicidad como solución total | Suena completa | Elimina uno de cinco |
| Bloquear y revertir | Es más fácil de implementar | Rechazar antes de bloquear |
| Ignorar el coste de liquidez | No aparece | Resta del ahorro |
| Fallo del ciclo sin dimensionar | Es improbable | Afecta a todo el ciclo |
| Justificar con un ahorro pequeño | Se infla el argumento | Declara el beneficio real |
| No probar el sistema detenido | No se piensa | Es la quinta prueba |

## 🧪 Práctica

El laboratorio pide probar los cinco modos de fallo y calcular el ahorro neto. El ahorro tras restar liquidez y fallo del ciclo es mucho menor de lo esperado.

En [`labs/lab-05.md`](../labs/lab-05.md):

1. Implementa la liquidación con rechazo previo al bloqueo.
2. Escribe las cinco pruebas de modos de fallo.
3. Calcula el ahorro neto restando el coste de liquidez.
4. Dimensiona el fallo del ciclo y corrige el ahorro.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen liquidaciones con estado intermedio. La causa es bloquear antes de verificar.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Llamar atómico a «casi a la vez» | Suena equivalente | No debe existir estado intermedio |
| Probar solo el camino feliz | Es lo que funciona | Cada fallo con su prueba |
| Comparar solo el ahorro | Es lo publicitado | Resta liquidez y fallo del ciclo |
| Inflar el argumento de riesgo | El ahorro es pequeño | Declara el beneficio de producto |
| Olvidar el emisor del dinero | Parece neutro | Es riesgo de crédito nuevo |
| Neteo sin dimensionar el fallo | Reduce el saldo | Concentra el episodio |

## ❓ Preguntas de comprobación

1. ¿Cómo se demuestra la atomicidad y por qué no se mide en milisegundos?
2. ¿Cuáles son los cinco riesgos y cuál elimina la atomicidad?
3. ¿Por qué rechazar antes de bloquear es mejor que bloquear y revertir?
4. ¿Qué gana y qué arriesga combinar neteo con liquidación atómica?
5. En el ejemplo, ¿con qué se justificó honestamente la arquitectura?

## 📥 Entregable

Guarda en `portfolio/parte-23/clase-10/`:

- la implementación con rechazo previo;
- las cinco pruebas de modos de fallo ejecutadas;
- el ahorro neto con liquidez y fallo del ciclo restados;
- la justificación honesta de la arquitectura.

## 🔗 Referencias cruzadas

- **Viene de:** clases 5 y 7; Parte 21, clase 8.
- **Continúa en:** clases 11 y 12 de esta parte.
- **Se aplica en:** clases 14 y 15 de esta parte.

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

- CPMI e IOSCO (2012). *Principles for Financial Market Infrastructures*. BIS. Firmeza y entrega contra pago exigidas al motor de liquidación. <https://www.bis.org/cpmi/publ/d101.htm>
- Committee on Payments and Market Infrastructures (2024). *Tokenisation in the context of money and other assets: concepts and implications for central banks*. BIS. Modos de fallo de la liquidación atómica y sus controles. <https://www.bis.org/cpmi/publ/d225.htm>
- Bank for International Settlements (2023). *Annual Economic Report, capítulo III*. BIS. Condiciones de la liquidación atómica en el libro unificado. <https://www.bis.org/publ/arpdf/ar2023e3.htm>
- IOSCO (2023). *Policy Recommendations for Crypto and Digital Asset Markets*. IOSCO. Obligaciones de conducta ante una liquidación fallida. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- Verificación local: comprueba en la fuente oficial vigente qué exige tu jurisdicción sobre este punto. **Fecha de verificación de esta clase: 2026-08-20.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 09 · Custodia y gestión de claves](09-custodia-y-gestion-de-claves.md) | [Parte 23](../README.md) · [Programa](../../../SYLLABUS.md) | [11 · Pagos y conexión con el exterior →](11-pagos-y-conexion-con-el-exterior.md) |
<!-- gen:footer:end -->
