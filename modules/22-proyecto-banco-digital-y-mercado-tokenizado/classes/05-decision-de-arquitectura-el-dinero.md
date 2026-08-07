---
part: 23
class: 5
title: "Decisión de arquitectura: el dinero"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [liquidacion, dinero-de-banco-central, liquidez]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [CPMI, BIS, BCCh]
requires_legal_review: false
---

<!-- gen:header:start -->
# Clase 05 · Decisión de arquitectura: el dinero

> [← 04 · Decisión de arquitectura: ¿hace falta un registro?](04-decision-de-arquitectura-registro.md) · [Índice de la parte](../README.md) · [06 · Decisión de producto: qué se ofrece →](06-decision-de-producto-que-se-ofrece.md)

**Parte 23 — Proyecto — banco digital y mercado tokenizado** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Decidir **con qué dinero se liquida**, que es la decisión que determina si la
liquidación atómica es siquiera posible y cuánto saldo hay que inmovilizar para
sostenerla.

La clase 4 dejó abierta una dependencia: el registro de colateral solo se
justifica si la atomicidad es alcanzable, y eso depende de dónde esté el dinero.
Esta clase la resuelve, y con ella cierra la decisión anterior.

## 📚 Objetivos

Al finalizar podrás:

1. **Comparar** las cuatro opciones de tramo de dinero por su riesgo de emisor.
2. **Calcular** el saldo prefinanciado que exige cada una.
3. **Determinar** si la atomicidad es alcanzable en este sistema.
4. **Cerrar** la decisión de la clase 4 con el resultado.
5. **Diseñar** la gestión de liquidez y el horario.

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

Los cuatro primeros términos son las opciones de tramo de dinero; los cuatro siguientes, su coste de liquidez. El **saldo prefinanciado** es el coste que decide entre las opciones: la que elimina el riesgo de emisor exige inmovilizar dinero, y esa inmovilización se paga todos los días.

| Concepto | Comprensión verificable |
|---|---|
| `tramo de dinero` | El activo con el que se liquida la pata de efectivo |
| `dinero de banco central` | Pasivo sin riesgo de crédito |
| `depósito tokenizado` | Pasivo de un banco supervisado |
| `saldo prefinanciado` | Fondos inmovilizados para liquidar en el momento |
| `riesgo de emisor` | Que quien debe el dinero no pueda pagar |
| `crédito intradía` | Posición entre bancos dentro del día |
| `ventana de liquidación` | Horario en que se salda |
| `saldo ocioso` | Fondos sin rendimiento |

## 🧠 Modelo mental

Las cuatro opciones no son grados de una misma cosa: la cuarta cambia el tipo de
riesgo, no su intensidad. Liquidar fuera del registro no es «peor»: es cambiar
riesgo de emisor por riesgo de principal.

```text
LAS CUATRO OPCIONES

  1 CBDC MAYORISTA      sin riesgo de crédito
                        existe en pocos sitios
  2 DEPÓSITO TOKENIZADO riesgo del banco, con
                        supervisión detrás
  3 STABLECOIN          riesgo del emisor privado
  4 FUERA DEL REGISTRO  sin riesgo de emisor
                        y SIN ATOMICIDAD

Y LA CONDICIÓN QUE DECIDE TODO
  la atomicidad exige que ambos tramos
  estén en el MISMO registro
```

## 📖 Desarrollo

### 1. El saldo prefinanciado es el coste real

Liquidar en el momento exige tener el dinero antes. Ese saldo no rinde, y su
coste suele superar al ahorro por eliminar el riesgo de principal en sistemas
del tamaño de este proyecto.

```text
SALDO NECESARIO

  sin neteo   una fracción alta del volumen
              diario, por la dispersión de
              las operaciones
  con neteo   mucho menor, porque solo se
              liquida el saldo

Y EL COSTE
  saldo × coste de financiación

  → es el que hay que comparar con la
    pérdida esperada que se evita
```

### 2. El horario también decide

Un registro opera 24/7 y el sistema de pagos no. Prometer operación continua sin
resolver de dónde sale el dinero de noche es la promesa que más se incumple.

```text
LO QUE OCURRE FUERA DE HORARIO

  · el dinero no entra ni sale del registro
  · se liquida contra el saldo que ya estaba
  · y si se agota, no hay más hasta abrir

DISEÑO
  · saldo de reserva calculado
  · límite por operación fuera de horario
  · cola con ejecución a la apertura
  · y decirlo: «esta operación se liquidará
    a las 09:00»
```

### 3. Cerrar la decisión de la clase 4

Esta clase existe para cerrar una dependencia, y conviene hacerlo de forma
explícita: si el dinero queda fuera del registro, el registro de colateral pierde
su justificación y hay que volver sobre la clase 4.

```text
LA CADENA DE DECISIONES

  dinero DENTRO del registro
    → atomicidad alcanzable
    → el registro de colateral se justifica
    → y hay que prefinanciar

  dinero FUERA
    → no hay atomicidad
    → el registro de colateral no aporta
    → se sustituye por una base compartida

NO HAY UNA TERCERA RAMA.
```

## 🧮 Ejemplo guiado

El ejemplo compara las cuatro opciones y cierra la cadena de decisiones que la clase 4 dejó abierta. Conviene ver que la conclusión sobre el registro depende por completo de esta elección.

**Situación.** El equipo decide el tramo de dinero para el crédito con colateral y
comprueba qué pasa con la decisión de la clase 4.

```text
DATOS
  volumen diario de colateral      1 200 000
  operaciones diarias                     18
  coste de financiación                4,3 % anual
  probabilidad de incumplimiento
    de contraparte a 2 días           0,004 %
  recuperación esperada                   45 %
  CBDC mayorista disponible                no
  depósito tokenizado disponible           sí
```

**Paso 1 — calcula el riesgo de principal que se evita.**

```text
EXPOSICIÓN CON CICLO T+2
  1 200 000 × 2 = 2 400 000

PÉRDIDA ESPERADA DIARIA
  2 400 000 × 0,00004 × 0,55 = 52,8

ANUAL (250 días)
  13 200

  → ES POCO, y esa es la primera señal
```

**Paso 2 — calcula el coste de prefinanciar.**

```text
SALDO NECESARIO CON NETEO
  supuesto 12 % del volumen diario
  1 200 000 × 12 % = 144 000

COSTE ANUAL
  144 000 × 4,3 % = 6 192

  FRENTE A 13 200 DE PÉRDIDA EVITADA

  → LA ATOMICIDAD COMPENSA,
    por 7 008 al año
```

**Paso 3 — comprueba el horario.**

```text
OPERACIONES FUERA DE HORARIO
  supuesto 8 % del volumen
  1 200 000 × 8 % = 96 000

SALDO DE RESERVA ADICIONAL
  supuesto 30 % de ese volumen = 28 800
  coste = 28 800 × 4,3 % = 1 238 al año

  ¿VALE LA PENA?
  el segmento son pymes exportadoras que
  operan en horario comercial de tres husos

  → SÍ, y con ventana ampliada de 07:00 a
    22:00 en vez de 24/7
```

**Paso 4 — cierra la decisión de la clase 4.**

```text
TRAMO DE DINERO: DEPÓSITO TOKENIZADO
  del banco corresponsal, supervisado
  con límite de exposición al emisor

  → EL DINERO ESTÁ EN EL REGISTRO
  → LA ATOMICIDAD ES ALCANZABLE
  → EL REGISTRO DE COLATERAL SE JUSTIFICA

Y LA DECISIÓN DE LA CLASE 4 SE CIERRA
  no hace falta un registro distribuido
  para el sistema completo, y sí hace
  falta un registro programable para el
  componente de colateral

  esa distinción es la que hay que escribir:
  no es «usamos blockchain», es «el
  colateral y su tramo de dinero viven en
  un registro común operado por nosotros»
```

**Interpreta:** La atomicidad compensaba por 7 008 al año, una cifra pequeña que aun así cierra
la dependencia de la clase 4. **Lo importante no fue el número sino la
distinción que obliga a escribir**: no se usa un registro distribuido para todo
el sistema, sino un registro programable para un componente concreto.

## 🧭 Perspectivas

El tramo de dinero afecta a cada actor de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Liquidación el mismo día | — |
| Equipo | Una dependencia cerrada | Cómo la documenta |
| Tesorería | 144 000 inmovilizados | Cómo los financia |
| Banco emisor | Saldos de la entidad | Qué límite acepta |
| Custodio | Colateral en un registro común | Cómo concilia |
| Supervisor | Riesgo de emisor concentrado | Qué límite exige |
| Auditor | Saldo ocioso y su emisor | Qué revela |
| Sociedad | Un mercado que opera de día | — |

## 🏦 Del cliente al banco

El cliente ve una liquidación y el sistema eligió con qué dinero se liquida y qué riesgo asume. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Liquida al instante» | Con 144 000 inmovilizados | 23, clase 5 |
| «Funciona siempre» | Ventana de 07:00 a 22:00 | 23, clase 5 |
| «Da igual con qué dinero» | Decide si la atomicidad existe | 23, clase 5 |

## ⚖️ Riesgos y controles

Los riesgos son de emisor y de liquidez intradía. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Prometer atomicidad sin el dinero dentro | La arquitectura lo impide | Verificar dónde está cada tramo |
| Ignorar el saldo prefinanciado | No aparece en el piloto | Es el coste principal |
| Prometer 24/7 | Suena a ventaja | El dinero tiene horario |
| Riesgo de emisor no limitado | Se concentra en un banco | Límite de exposición |
| No cerrar la dependencia | La clase 4 queda abierta | Escribir la cadena completa |
| Decir «usamos blockchain» | Es la frase cómoda | Precisar qué componente y por qué |

## 🧪 Práctica

El laboratorio pide comparar las cuatro opciones y cerrar la cadena de decisiones. La cadena cerrada con su fundamento es lo que se evalúa.

En [`labs/lab-03.md`](../labs/lab-03.md):

1. Compara las cuatro opciones por riesgo de emisor y coste.
2. Calcula el saldo prefinanciado y su coste anual.
3. Contrasta ese coste con la pérdida esperada que se evita.
4. Cierra la decisión de la clase 4 con la cadena completa.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen arquitecturas con atomicidad prometida y no alcanzable. La causa es el dinero fuera del registro.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Elegir el dinero por comodidad | Es lo disponible | Calcula riesgo y coste |
| Ignorar el horario | El registro opera siempre | El dinero no |
| Sin límite al emisor | Parece neutro | Es exposición concentrada |
| Comparar solo el ahorro | Es lo publicitado | Resta la prefinanciación |
| Dejar la dependencia abierta | Se olvida | La clase 4 depende de esta |
| Generalizar «blockchain» | Es lo que se entiende | Precisa el componente |

## ❓ Preguntas de comprobación

1. ¿Cuáles son las cuatro opciones y cuál cambia el tipo de riesgo?
2. ¿Cuál es la condición sin la cual no hay atomicidad?
3. ¿Por qué el saldo prefinanciado es el coste principal?
4. ¿Qué ocurre con el dinero fuera del horario del sistema de pagos?
5. En el ejemplo, ¿qué distinción obliga a escribir el resultado?

## 📥 Entregable

Guarda en `portfolio/parte-23/clase-05/`:

- la comparación de las cuatro opciones con su riesgo;
- el saldo prefinanciado y su coste anual;
- la contrastación con la pérdida esperada evitada;
- la cadena de decisiones que cierra la clase 4.

## 🔗 Referencias cruzadas

- **Viene de:** clase 4; Parte 20, clases 8 y 10; Parte 21, clase 10.
- **Continúa en:** clases 7 y 10 de esta parte.
- **Se aplica en:** clases 12 y 15 de esta parte.

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

- Committee on Payments and Market Infrastructures (2024). *Tokenisation in the context of money and other assets*. BIS. <https://www.bis.org/cpmi/publ/d225.htm>
- CPMI e IOSCO (2012). *Principles for Financial Market Infrastructures*. BIS. <https://www.bis.org/cpmi/publ/d101.htm>
- Bank for International Settlements (2023). *Annual Economic Report*, capítulo III. BIS. <https://www.bis.org/publ/arpdf/ar2023e3.htm>
- Basel Committee on Banking Supervision (2022). *Prudential treatment of cryptoasset exposures* (SCO60). BIS. <https://www.bis.org/bcbs/publ/d545.htm>
- Verificación local: comprueba en la fuente oficial vigente qué exige tu jurisdicción sobre este punto antes de aplicar cualquier conclusión de la clase. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 04 · Decisión de arquitectura: ¿hace falta un registro?](04-decision-de-arquitectura-registro.md) | [Parte 23](../README.md) · [Programa](../../../SYLLABUS.md) | [06 · Decisión de producto: qué se ofrece →](06-decision-de-producto-que-se-ofrece.md) |
<!-- gen:footer:end -->
