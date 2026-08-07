---
part: 20
class: 2
title: "Criptoactivos no respaldados"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [criptoactivos, riesgo-de-mercado, prudencial]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [BCBS, IOSCO, FSB]
requires_legal_review: false
---

<!-- gen:header:start -->
# Clase 02 · Criptoactivos no respaldados

> [← 01 · Taxonomía de los activos digitales](01-taxonomia-de-los-activos-digitales.md) · [Índice de la parte](../README.md) · [03 · Stablecoins: tipologías y mecánica de la paridad →](03-stablecoins-tipologias-y-mecanica-de-la-paridad.md)

**Parte 20 — Activos digitales, stablecoins y dinero programable** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Estudiar el instrumento donde **no hay obligado**: qué determina su oferta, de
qué depende su precio y por qué el tratamiento prudencial más severo del sistema
financiero se le aplica precisamente a él.

## 📚 Objetivos

Al finalizar podrás:

1. **Describir** cómo se determina la oferta de un criptoactivo no respaldado.
2. **Explicar** por qué su precio no tiene un ancla de valoración por descuento
   de flujos.
3. **Calcular** el consumo de capital de una exposición bajo un tratamiento
   deductivo.
4. **Distinguir** volatilidad de riesgo de crédito, que aquí no existe.
5. **Argumentar** por qué la escasez programada no implica valor.

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
| `oferta programada` | Emisión fijada por reglas del protocolo, no por un emisor |
| `escasez` | Límite de unidades; no es una fuente de valor por sí sola |
| `sin obligado` | Nadie debe nada al tenedor |
| `valor de uso` | Lo que permite hacer; puede ser cero |
| `reflexividad` | El precio influye en la demanda que lo sostiene |
| `deducción del capital` | Tratamiento que resta la exposición del capital regulatorio |
| `volatilidad realizada` | Dispersión observada de rendimientos |
| `riesgo de mercado sin ancla` | No hay flujo futuro contra el que contrastar |

## 🧠 Modelo mental

```text
UN BONO VALE POR SUS FLUJOS
UNA ACCIÓN VALE POR EL BENEFICIO RESIDUAL
UN DEPÓSITO VALE POR LA OBLIGACIÓN DEL BANCO

UN CRIPTOACTIVO NO RESPALDADO
NO TIENE FLUJO, NI BENEFICIO, NI OBLIGADO

  → SU PRECIO ES EXACTAMENTE
    LO QUE OTRO ESTÉ DISPUESTO A PAGAR

ESTO NO SIGNIFICA «VALE CERO».
SIGNIFICA QUE NO HAY UN MÉTODO DE VALORACIÓN
QUE PERMITA DECIR SI EL PRECIO ES ALTO O BAJO.

Un analista puede decir que un bono está caro.
Sobre esto no puede decirlo, y quien lo diga
está expresando una opinión, no un cálculo.
```

## 📖 Desarrollo

### 1. Cómo se determina la oferta

```text
TRES MODELOS HABITUALES

  LÍMITE FIJO Y EMISIÓN DECRECIENTE
    total conocido, ritmo predefinido
    → la oferta es predecible; la demanda no

  EMISIÓN CONTINUA
    con o sin destrucción de unidades
    → la oferta neta depende del uso

  EMISIÓN DISCRECIONAL POR GOBERNANZA
    un voto puede cambiarla
    → la «escasez» es una decisión, no una ley

LA PREGUNTA ÚTIL NO ES CUÁNTAS UNIDADES HAY,
SINO QUIÉN PUEDE CAMBIAR ESA CIFRA Y CÓMO
```

### 2. Escasez no es valor

```text
ARGUMENTO FRECUENTE
  «solo habrá N unidades, luego subirá»

POR QUÉ NO SE SOSTIENE
  · hay una cantidad limitada de casi todo
  · el valor exige DEMANDA, y la escasez
    no la crea
  · un bien escaso sin demanda vale poco:
    la escasez es condición, no causa

LO QUE SÍ IMPORTA
  · qué permite hacer que otra cosa no permita
  · cuánta gente lo necesita para eso
  · a qué coste está disponible la alternativa
```

### 3. Reflexividad

```text
EN UN ACTIVO CON FLUJOS
  precio ↑  →  rendimiento esperado ↓  →  demanda ↓
  hay un mecanismo de retorno

SIN FLUJOS
  precio ↑  →  atención ↑  →  demanda ↑  →  precio ↑
  y en el otro sentido, igual de rápido

  → EL MECANISMO ESTABILIZADOR NO EXISTE
    y por eso la volatilidad es estructural,
    no un accidente de mercado inmaduro
```

### 4. Tratamiento prudencial

```text
POR QUÉ EL TRATAMIENTO ES SEVERO

  el marco prudencial asigna capital
  según pérdida esperada e inesperada

  para estimarlas hace falta
  una distribución con ancla

  sin ancla, el supervisor no puede
  validar ningún modelo interno

  → SOLUCIÓN CONSERVADORA:
    tratar la exposición como si pudiera
    perderse por completo

CONSECUENCIA PRÁCTICA
  cada unidad de exposición consume
  capital como si fuera pérdida
  → el coste de mantenerla en balance
    es muy alto, y esa es la intención
```

### 5. Qué sí puede decir un análisis serio

```text
NO SE PUEDE DECIR                 SÍ SE PUEDE DECIR

«está infravalorado»              «su volatilidad realizada
                                   a 90 días fue del X %»

«vale N por el modelo»            «la correlación con el
                                   índice de renta variable
                                   en tensión sube a Y»

«subirá porque es escaso»         «el 60 % de la oferta
                                   está en Z direcciones»

«es una reserva de valor»         «su caída máxima desde
                                   máximo fue del W %»

LA SEGUNDA COLUMNA SON HECHOS MEDIBLES.
LA PRIMERA SON OPINIONES.
Un informe de riesgo solo puede contener la segunda.
```

## 🧮 Ejemplo guiado

**Situación.** Un banco evalúa mantener una exposición de 4 000 000 en un
criptoactivo no respaldado como cobertura de un servicio a clientes. Hay que
calcular qué cuesta.

```text
DATOS
  exposición prevista                  4 000 000
  capital regulatorio actual         220 000 000
  activos ponderados por riesgo    1 750 000 000
  ratio de capital actual                 12,57 %
  ratio mínimo exigido                     10,50 %
  volatilidad realizada anualizada         68 %
  caída máxima observada (5 años)          77 %
```

**Paso 1 — calcula el ratio actual y el margen.**

```text
RATIO = 220 000 000 / 1 750 000 000 = 12,571 %

MARGEN SOBRE EL MÍNIMO
  12,571 % − 10,500 % = 2,071 puntos

CAPITAL EXCEDENTE
  1 750 000 000 × 2,071 % = 36 250 000
```

**Paso 2 — aplica el tratamiento deductivo.**

```text
SUPUESTO DE TRABAJO: la exposición se deduce
íntegramente del capital.

  capital tras la deducción
  220 000 000 − 4 000 000 = 216 000 000

  nuevo ratio
  216 000 000 / 1 750 000 000 = 12,343 %

  caída del ratio: 0,229 puntos
```

**Paso 3 — expresa el coste en términos de negocio.**

```text
¿QUÉ MÁS PODRÍA HABER HECHO EL BANCO
CON ESOS 4 000 000 DE CAPITAL?

  con una ponderación media del 75 %,
  4 000 000 de capital sostienen:

  4 000 000 / 10,50 % = 38 095 238 de APR
  38 095 238 / 75 % = 50 793 651 de crédito

  → LA EXPOSICIÓN DE 4 MILLONES
    DESPLAZA UNOS 50,8 MILLONES DE CRÉDITO
```

**Paso 4 — calcula el rendimiento que tendría que dar.**

```text
SI EL CRÉDITO DESPLAZADO DEJA UN MARGEN
NETO DEL 1,8 % SOBRE SALDO

  50 793 651 × 1,8 % = 914 286 al año

PARA COMPENSARLO, LA EXPOSICIÓN DE 4 000 000
TENDRÍA QUE RENDIR

  914 286 / 4 000 000 = 22,86 % anual
  SOLO PARA EMPATAR

y ese rendimiento tendría que ser
razonablemente seguro, cuando la volatilidad
del propio activo es del 68 %
```

**Paso 5 — mide la pérdida en un escenario de tensión.**

```text
APLICANDO LA CAÍDA MÁXIMA OBSERVADA (77 %)

  pérdida = 4 000 000 × 77 % = 3 080 000

  ¿AFECTA AL CAPITAL?
  ya estaba deducido: el capital regulatorio
  no cae otra vez

  → ESA ES LA LÓGICA DEL TRATAMIENTO:
    la pérdida se anticipa en el capital
    en lugar de reconocerse cuando ocurre

  PERO EL RESULTADO CONTABLE SÍ RECIBE
  el golpe de 3 080 000 en el ejercicio
```

**Paso 6 — separa las tres capas de la decisión.**

```text
HECHO
  la exposición consume capital y desplaza crédito
  por 50,8 millones; el cálculo es reproducible

SUPUESTO
  ponderación media del 75 %, margen del 1,8 %
  y deducción íntegra: los tres pueden cambiar
  y hay que declararlos

INTERPRETACIÓN
  con estos números, la exposición solo se
  justifica si el servicio al cliente que
  habilita genera comisiones que compensen,
  y eso hay que medirlo aparte
```

**Paso 7 — formula la alternativa.**

```text
¿HACE FALTA LA EXPOSICIÓN PARA PRESTAR EL SERVICIO?

  · si el banco solo custodia por cuenta de clientes,
    el activo NO es suyo y no consume capital igual
  · si el banco casa órdenes sin tomar posición,
    la exposición es intradía y mucho menor
  · si el banco toma posición para dar liquidez,
    entonces sí, y hay que pagarlo

LA PREGUNTA DE DISEÑO
  ¿el modelo de servicio exige balance propio,
  o se eligió por comodidad operativa?
```

**Interpreta:** el coste no está en la volatilidad, que es visible, sino en el
**capital desplazado**, que no aparece en ningún informe de mercado. Cuatro
millones de exposición cuestan cincuenta millones de crédito no concedido, y esa
es la cifra que decide.

## 🧭 Perspectivas

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un precio que sube y baja | Si compra |
| Inversionista | Un activo sin flujos | Qué peso le da |
| Banco | Capital desplazado | Si presta el servicio con balance propio |
| Emisor | No hay emisor | — |
| Custodio | Un activo al portador | Cómo lo protege |
| Mercado | Profundidad desigual | Cómo cotiza |
| Supervisor | Exposición sin ancla de valoración | Qué capital exige |
| Auditor | Valoración por precio de mercado | Qué nivel de jerarquía aplica |
| Sociedad | Un debate sobre energía y uso | Qué información pública exige |

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «El banco no quiere ofrecerlo» | Consume capital como pérdida | 20, clase 2 |
| «Es escaso, luego subirá» | La escasez no crea demanda | 20, clase 2 |
| «Bajó un 70 %, es un caso raro» | Está dentro de lo observado | 20, clase 2 |

## ⚖️ Riesgos y controles

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Valoración sin ancla | Se presenta una opinión como cálculo | Solo métricas observables en informes |
| Concentración de la oferta | Pocos tenedores mueven el precio | Medir distribución y declararla |
| Capital consumido sin retorno | La exposición desplaza crédito | Cuantificar el desplazamiento antes |
| Liquidez aparente | El volumen no es profundidad | Medir impacto de una venta grande |
| Correlación en tensión | La diversificación desaparece | Escenario conjunto, no marginal |
| Reflexividad | El precio sostiene la demanda | Escenarios sin retorno a la media |

## 🧪 Práctica

En [`labs/lab-01.md`](../labs/lab-01.md):

1. Calcula el capital desplazado por una exposición dada.
2. Halla el rendimiento de equilibrio frente al crédito alternativo.
3. Distingue las afirmaciones medibles de las opiniones en un informe.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| «Está barato» | Se usa vocabulario de valoración | Sin ancla no hay caro ni barato |
| Escasez como argumento | Se confunde condición con causa | Exige demostrar la demanda |
| Ignorar el capital desplazado | Solo se mira el rendimiento | El coste de oportunidad es la cifra |
| Tomar volumen por liquidez | Es el dato más visible | Mide profundidad e impacto |
| Suponer reversión a la media | Se importa de otros mercados | No hay flujo que ancle la media |
| Confundir volatilidad con riesgo total | Es la parte medible | Añade concentración, custodia y liquidez |

## ❓ Preguntas de comprobación

1. ¿Por qué no puede decirse que un criptoactivo no respaldado esté
   infravalorado?
2. ¿Qué significa que la escasez es condición y no causa del valor?
3. Explica la reflexividad y por qué elimina el mecanismo estabilizador.
4. En el ejemplo, ¿cuánto crédito desplaza una exposición de 4 000 000 y por
   qué?
5. ¿Qué afirmaciones puede contener un informe de riesgo y cuáles no?

## 📥 Entregable

Guarda en `portfolio/parte-20/clase-02/`:

- el cálculo de capital desplazado y de rendimiento de equilibrio;
- una tabla de afirmaciones medibles frente a opiniones sobre un activo;
- la declaración explícita de los supuestos usados;
- la alternativa de modelo de servicio sin posición propia.

## 🔗 Referencias cruzadas

- **Viene de:** clase 1; Parte 11, gestión de riesgos.
- **Continúa en:** clases 13 y 14 de esta parte.
- **Se aplica en:** Parte 22, clase 8; Parte 23, clase 9.

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

- Basel Committee on Banking Supervision (2022). *Prudential treatment of cryptoasset exposures* (SCO60). BIS. <https://www.bis.org/bcbs/publ/d545.htm>
- Financial Stability Board (2023). *Global Regulatory Framework for Crypto-asset Activities*. FSB. <https://www.fsb.org/2023/07/fsb-global-regulatory-framework-for-crypto-asset-activities/>
- IOSCO (2023). *Policy Recommendations for Crypto and Digital Asset Markets*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- Bank for International Settlements (2022). *Annual Economic Report*, capítulo III: el futuro del sistema monetario. BIS. <https://www.bis.org/publ/arpdf/ar2022e3.htm>
- Verificación local: comprueba el tratamiento prudencial vigente en tu jurisdicción y su calendario de aplicación antes de usar el cálculo de capital de esta clase. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 01 · Taxonomía de los activos digitales](01-taxonomia-de-los-activos-digitales.md) | [Parte 20](../README.md) · [Programa](../../../SYLLABUS.md) | [03 · Stablecoins: tipologías y mecánica de la paridad →](03-stablecoins-tipologias-y-mecanica-de-la-paridad.md) |
<!-- gen:footer:end -->
