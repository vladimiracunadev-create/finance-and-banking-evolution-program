---
part: 22
class: 8
title: "Tratamiento prudencial de las exposiciones"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [prudencial, capital, liquidez]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [BCBS, BIS, CMF]
requires_legal_review: true
---

## 🎯 Propósito

Traducir la exposición a activos digitales en **capital y liquidez**. El marco
prudencial no informa: protege, y por eso sus cifras no coinciden con las
contables ni tienen por qué hacerlo.

## 📚 Objetivos

Al finalizar podrás:

1. **Clasificar** una exposición en los grupos del marco prudencial.
2. **Calcular** el capital que consume cada grupo.
3. **Aplicar** el límite de exposición y medir su holgura.
4. **Distinguir** exposición directa, indirecta y por servicios prestados.
5. **Explicar** por qué el balance y el capital regulatorio no coinciden.

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| `grupo 1` | Activos tokenizados y referenciados que superan la prueba |
| `grupo 2` | El resto, con tratamiento conservador |
| `prueba de estabilización` | Condiciones para que un referenciado sea grupo 1 |
| `deducción del capital` | Restar la exposición del capital regulatorio |
| `límite de exposición` | Tope del grupo 2 sobre el capital |
| `exposición por servicios` | La que nace de custodiar o intermediar |
| `riesgo operacional` | Capital por fallos de proceso, personas o sistemas |
| `coeficiente de liquidez` | Cobertura de salidas en tensión |

## 🧠 Modelo mental

```text
LA LÓGICA DEL MARCO

  el capital cubre pérdidas inesperadas
  → para calcularlo hace falta una
    distribución con ancla

  SIN ANCLA DE VALORACIÓN, el supervisor
  no puede validar ningún modelo interno
  → solución conservadora: tratar la
    exposición como si pudiera perderse

DOS GRUPOS

  GRUPO 1  hay ancla: un activo subyacente
           identificable o una reserva
           que supera la prueba
           → tratamiento del subyacente,
             más un recargo por riesgo
             de infraestructura

  GRUPO 2  no hay ancla
           → tratamiento conservador
             y límite sobre el capital

Y EL LÍMITE ES LA PIEZA QUE MÁS DECIDE:
no encarece la exposición, la prohíbe
por encima de un umbral.
```

## 📖 Desarrollo

### 1. La prueba de estabilización

```text
UN REFERENCIADO ES GRUPO 1 SI, ADEMÁS
DE OTROS REQUISITOS

  · la reserva es suficiente en todo momento
  · se compone de activos de bajo riesgo
  · hay derecho de reembolso ejercitable
  · el emisor está supervisado
  · el valor se mantiene dentro de una banda
    estrecha, comprobado con datos

EL ÚLTIMO ES EL QUE MÁS FALLA
  y se comprueba con la serie de precios,
  no con la declaración del emisor
  → es exactamente el indicador de desvío
    de la Parte 20, clase 3
```

### 2. Los tres tipos de exposición

```text
DIRECTA
  el activo está en el balance
  → el más fácil de medir y el menos
    frecuente en un banco

INDIRECTA
  crédito a quien lo tiene, participación
  en un fondo expuesto, derivado
  → la de la Parte 20, clase 14

POR SERVICIOS PRESTADOS
  custodia por cuenta de terceros,
  intermediación, liquidación
  → NO es exposición de crédito,
    y sí de riesgo operacional

LA TERCERA SE OLVIDA
  custodiar 900 000 000 por cuenta de
  clientes no pone 900 000 000 en el balance,
  y sí genera un riesgo operacional que
  consume capital
```

### 3. El límite y su holgura

```text
UN LÍMITE HABITUAL ES UN PORCENTAJE
DEL CAPITAL DE NIVEL 1

  exposición del grupo 2 ≤ X % del capital

CÓMO SE MIDE LA HOLGURA
  · exposición actual frente al límite
  · y frente al límite tras una caída
    del valor de lo que sí computa

Y AHÍ ESTÁ LA TRAMPA
  si el activo cae, la exposición baja
  en términos absolutos... y el capital
  también, porque se dedujo
  → la holgura no mejora tanto como parece
```

### 4. Balance y capital no coinciden

```text
POR QUÉ

  CONTABILIDAD   informa a terceros
  PRUDENCIAL     protege al depositante

  la primera puede mostrar 13 275 000
  la segunda puede haberlo deducido entero

NO ES UNA INCOHERENCIA
  son dos marcos con finalidades distintas

QUÉ HAY QUE HACER
  explicarlo en la memoria, porque el
  lector supondrá que coinciden
  (Parte 20, clase 15)
```

### 5. Liquidez

```text
EL COEFICIENTE DE COBERTURA SUPONE
UNA SALIDA EN TENSIÓN

  ¿QUÉ SALIDA SUPONER PARA UN DEPÓSITO
   DE UN CLIENTE DE ACTIVOS DIGITALES?

  · más volátil que un depósito minorista
  · concentrado en pocos depositantes
  · correlacionado con el precio del activo

  → EL FACTOR DE SALIDA ESTÁNDAR
    SE QUEDA CORTO

Y LOS ACTIVOS DIGITALES DEL GRUPO 2
NO COMPUTAN COMO ACTIVOS LÍQUIDOS
DE ALTA CALIDAD, por definición
```

## 🧮 Ejemplo guiado

**Situación.** Un banco calcula el efecto prudencial de tres exposiciones.

```text
DATOS DEL BANCO
  capital de nivel 1              320 000 000
  activos ponderados            2 400 000 000
  ratio actual                          13,3 %
  límite del grupo 2                       1 %

EXPOSICIONES
  A  bono tokenizado de emisor supervisado,
     registro con bloqueo de origen     18 000 000
  B  referenciado que no supera la prueba
     de estabilización                   2 400 000
  C  custodia por cuenta de clientes    340 000 000
```

**Paso 1 — clasifica A.**

```text
BONO TOKENIZADO

  ¿hay subyacente identificable?      sí
  ¿el emisor está supervisado?        sí
  ¿el registro tiene finalidad clara? sí

  → GRUPO 1
  tratamiento del bono, más un recargo
  por riesgo de infraestructura

  supuesto: ponderación del bono 50 %
  más recargo del 2,5 % del valor

  APR = 18 000 000 × 50 % = 9 000 000
  recargo = 18 000 000 × 2,5 % = 450 000
  APR total = 9 450 000
  capital = 9 450 000 × 10,5 % = 992 250
```

**Paso 2 — clasifica B.**

```text
REFERENCIADO QUE NO SUPERA LA PRUEBA

  la serie de precios muestra desvíos
  fuera de banda sostenidos

  → GRUPO 2
  tratamiento conservador: deducción íntegra

  capital deducido = 2 400 000

  NUEVO CAPITAL
  320 000 000 − 2 400 000 = 317 600 000
```

**Paso 3 — comprueba el límite.**

```text
LÍMITE DEL GRUPO 2: 1 % DEL CAPITAL

  1 % de 320 000 000 = 3 200 000
  exposición actual   2 400 000

  HOLGURA: 800 000  (25 % del límite)

  ¿Y SI EL CAPITAL BAJA?
  el capital ya está deducido
  → el límite se calcula sobre el capital
    antes o después de deducir, y la norma
    lo dice: hay que leerlo, porque cambia
    la holgura

  con el capital tras deducción
  1 % de 317 600 000 = 3 176 000
  holgura 776 000
```

**Paso 4 — clasifica C.**

```text
CUSTODIA POR CUENTA DE CLIENTES

  ¿es exposición de crédito?
  NO, si hay segregación jurídica y el banco
  no puede disponer

  ¿genera capital?
  SÍ, por riesgo operacional

  supuesto: método del indicador de negocio
  ingresos por custodia          4 200 000
  factor supuesto                     15 %
  componente de riesgo operacional  630 000
  APR = 630 000 × 12,5 = 7 875 000
  capital = 826 875
```

**Paso 5 — suma el efecto.**

```text
CAPITAL CONSUMIDO
  A  992 250     por APR
  B  2 400 000   por deducción
  C  826 875     por APR operacional

  TOTAL          4 219 125

EFECTO SOBRE EL RATIO
  capital 320 000 000 − 2 400 000 = 317 600 000
  APR 2 400 000 000 + 9 450 000 + 7 875 000
      = 2 417 325 000

  ratio = 13,14 %  (antes 13,33 %)
  caída de 0,19 puntos
```

**Paso 6 — mide el coste de oportunidad de B.**

```text
2 400 000 DE EXPOSICIÓN DEDUCIDA

  ese capital sostendría, con ponderación
  media del 75 % y requerimiento del 10,5 %:
  2 400 000 / 10,5 % = 22 857 143 de APR
  / 75 % = 30 476 190 de crédito

  con un margen neto del 1,8 %
  548 571 al año de margen renunciado

  → LA EXPOSICIÓN DE 2,4 MILLONES CUESTA
    548 571 AL AÑO EN MARGEN
    y tiene que rendir un 22,9 % solo
    para empatar
```

**Paso 7 — revisa la liquidez.**

```text
DEPÓSITOS DE CLIENTES DE ACTIVOS DIGITALES

  saldo               96 000 000
  depositantes             1 240
  factor de salida estándar para
    mayorista no operativo    40 %

  ¿ES SUFICIENTE?
  · concentración: los 20 mayores tienen
    el 58 % del saldo
  · correlación: si el activo cae, retiran
    todos a la vez

  supuesto de salida en tensión: 70 %

  SALIDA ESPERADA
  96 000 000 × 70 % = 67 200 000
  frente a 38 400 000 con el factor estándar

  DIFERENCIA: 28 800 000 de activos líquidos
  adicionales que el estándar no exige
  y el riesgo real sí
```

**Interpreta:** la exposición del grupo 2 era de 2,4 millones y costaba 548 571
al año de margen renunciado. **La partida que nadie había calculado era la
liquidez**: 28,8 millones de activos líquidos adicionales que el factor estándar
no exige porque supone una base de depósitos que no es esta.

## 🧭 Perspectivas

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un banco que no ofrece el servicio | Dónde va |
| Fintech | Un banco que le cierra la cuenta | Con quién trabaja |
| Banco | 548 571 de margen renunciado | Si presta el servicio |
| Emisor | La prueba de estabilización | Si la supera |
| Custodio | Riesgo operacional que computa | Cómo lo controla |
| Tesorería | Liquidez adicional | Cómo la financia |
| Supervisor | Factor de salida insuficiente | Si lo recalibra |
| Auditor | Balance y capital que no coinciden | Qué revela |
| Inversionista | Ratio que cae 0,19 puntos | Qué exige |
| Sociedad | Bancos prudentes | Qué protección obtiene |

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «El banco no quiere ofrecerlo» | Consume capital como pérdida | 22, clase 8 |
| «Solo custodian, no arriesgan» | La custodia consume capital operacional | 22, clase 8 |
| «El balance dice otra cosa» | Son dos marcos con fines distintos | 22, clase 8 |

## ⚖️ Riesgos y controles

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Prueba de estabilización supuesta | Se acepta la declaración del emisor | Comprobar con la serie de precios |
| Exposición por servicios olvidada | Custodiar «no es exposición» | Computar riesgo operacional |
| Límite mal calculado | Antes o después de deducir | Leer la norma, cambia la holgura |
| Factor de salida estándar | Supone otra base de depósitos | Recalibrar con concentración y correlación |
| Coste de oportunidad ignorado | Solo se mira el capital | Calcular el margen renunciado |
| Balance y capital confundidos | Se supone que coinciden | Explicarlo en la memoria |

## 🧪 Práctica

En [`labs/lab-05.md`](../labs/lab-05.md):

1. Clasifica tres exposiciones y calcula el capital de cada una.
2. Comprueba el límite del grupo 2 y su holgura.
3. Calcula el margen renunciado por la exposición deducida.
4. Recalibra el factor de salida con concentración y correlación.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Aceptar la clasificación del emisor | Es lo que declara | Aplicar la prueba con datos |
| Ignorar la custodia | No está en el balance | Consume capital operacional |
| Usar el factor estándar | Es lo que dice la tabla | Esta base de depósitos es distinta |
| Mirar solo el ratio | Cae poco | El margen renunciado es la cifra |
| Suponer coherencia contable | Parece lógico | Dos marcos, dos finalidades |
| Calcular el límite una vez | La exposición varía | Recalcularlo con cada operación |

## ❓ Preguntas de comprobación

1. ¿Por qué el marco es conservador cuando no hay ancla de valoración?
2. ¿Cuáles son los tres tipos de exposición y cuál se olvida?
3. ¿Qué requisito de la prueba de estabilización falla más y cómo se comprueba?
4. ¿Por qué el balance y el capital regulatorio no coinciden?
5. En el ejemplo, ¿cuál era la partida que nadie había calculado?

## 📥 Entregable

Guarda en `portfolio/parte-22/clase-08/`:

- la clasificación de tres exposiciones con su capital;
- el límite del grupo 2 y su holgura, calculado como dice la norma;
- el margen renunciado por la deducción;
- el factor de salida recalibrado con su justificación.

## 🔗 Referencias cruzadas

- **Viene de:** clase 2; Parte 20, clases 2, 14 y 15.
- **Continúa en:** clases 9 y 15 de esta parte.
- **Se aplica en:** clase 18 de esta parte; Parte 23, clase 9.

## 📗 Fuentes y verificación

- Basel Committee on Banking Supervision (2022). *Prudential treatment of cryptoasset exposures* (SCO60). BIS. <https://www.bis.org/bcbs/publ/d545.htm>
- Basel Committee on Banking Supervision (2013). *Basel III: The Liquidity Coverage Ratio*. BIS. <https://www.bis.org/publ/bcbs238.htm>
- Basel Committee on Banking Supervision (2017). *Basel III: Finalising post-crisis reforms*. BIS. <https://www.bis.org/bcbs/publ/d424.htm>
- Comisión para el Mercado Financiero. *Normativa de adecuación de capital y liquidez*. CMF. <https://www.cmfchile.cl/portal/principal/613/w3-channel.html>
- Verificación local: comprueba el tratamiento prudencial vigente en tu jurisdicción, su calendario de aplicación y si ha recalibrado los factores de salida para este tipo de depósitos. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-06.**
