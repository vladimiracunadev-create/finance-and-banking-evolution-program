---
part: 21
class: 10
title: "El tramo de dinero"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [liquidacion, dinero-de-banco-central, riesgo-de-credito]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [CPMI, BIS, IOSCO]
requires_legal_review: false
---

<!-- gen:header:start -->
# Clase 10 · El tramo de dinero

> [← 09 · Custodia de valores tokenizados](09-custodia-de-valores-tokenizados.md) · [Índice de la parte](../README.md) · [11 · FX: del mercado mayorista al registro →](11-fx-del-mercado-mayorista-al-registro.md)

**Parte 21 — Tokenización, FX on-chain y mercados programables** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Decidir **con qué dinero se liquida**. La clase 8 mostró que sin el dinero en el
mismo registro no hay atomicidad; esta clase estudia las cuatro opciones
disponibles y qué riesgo introduce cada una.

## 📚 Objetivos

Al finalizar podrás:

1. **Comparar** las cuatro opciones de tramo de dinero por su riesgo de emisor.
2. **Calcular** el capital que consume liquidar contra cada una.
3. **Explicar** por qué el dinero de banco central es el patrón y qué se pierde
   al alejarse.
4. **Diseñar** la gestión de liquidez de una plataforma que liquida en T+0.
5. **Evaluar** el efecto del horario del sistema de pagos sobre la operación.

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

Los tres primeros términos son las opciones de dinero y su riesgo; los cinco siguientes, su coste operativo. El **riesgo de emisor** es lo que separa las opciones: el dinero de banco central no tiene y el de banco comercial sí, y esa diferencia decide si la atomicidad elimina todo el riesgo o solo una parte.

| Concepto | Comprensión verificable |
|---|---|
| `dinero de banco central` | Pasivo del banco central, sin riesgo de crédito |
| `dinero de banco comercial` | Depósito, con riesgo del banco |
| `riesgo de emisor` | Que quien debe el dinero no pueda pagar |
| `liquidez intradía` | Fondos disponibles durante la sesión |
| `cuenta de liquidación` | Aquella donde se salda el tramo de dinero |
| `prefinanciación` | Depositar antes de operar |
| `horario de apertura` | Ventana en que el sistema de pagos opera |
| `saldo ocioso` | Fondos inmovilizados sin rendimiento |

## 🧠 Modelo mental

El modelo mental es que la atomicidad solo alcanza a lo que está dentro del registro. Si el dinero está fuera, no hay atomicidad posible por mucho que el activo esté tokenizado, y esa restricción decide toda la arquitectura.

```text
LAS CUATRO OPCIONES, DE MENOR A MAYOR RIESGO

  1 CBDC MAYORISTA EN EL REGISTRO
      pasivo del banco central
      → sin riesgo de crédito
      → existe en pocos sitios

  2 DEPÓSITO TOKENIZADO
      pasivo de un banco supervisado
      → riesgo del banco, con garantía y
        supervisión detrás

  3 STABLECOIN
      pasivo de un emisor privado
      → riesgo del emisor, con todo lo de
        la Parte 20

  4 DINERO FUERA DEL REGISTRO
      transferencia bancaria clásica
      → sin riesgo de emisor nuevo
      → PERO SIN ATOMICIDAD

LA OPCIÓN 4 NO ES «PEOR»: ES OTRA COSA.
Cambia riesgo de emisor por riesgo de principal.
```

## 📖 Desarrollo

### 1. Por qué el dinero de banco central es el patrón

```text
NO ES UNA PREFERENCIA INSTITUCIONAL:
ES UNA PROPIEDAD

  · el banco central no quiebra en su moneda
  · su pasivo es aceptado por todos sin
    evaluar su crédito
  · no hay que fijar límites bilaterales
    frente a él

CONSECUENCIA PARA UNA INFRAESTRUCTURA
  liquidar en dinero de banco central
  elimina la necesidad de que cada participante
  evalúe el crédito de la contraparte
  en el tramo de dinero

  → y eso es lo que permite que un mercado
    tenga muchos participantes sin que cada
    uno tenga que analizar a los demás

CUANDO SE LIQUIDA CON OTRO DINERO
  esa evaluación vuelve, y con ella
  los límites, las garantías y el coste
```

### 2. Prefinanciación y saldo ocioso

```text
LIQUIDAR EN T+0 EXIGE TENER EL DINERO ANTES

  con T+2, el pago se prepara en dos días
  con T+0, tiene que estar ya

  → SALDO PREFINANCIADO

COSTE
  el saldo prefinanciado no rinde, o rinde
  menos que su alternativa

  y crece con el volumen y con la dispersión
  de las operaciones a lo largo del día

MITIGACIONES
  · neteo (clase 8): reduce la necesidad
  · líneas de liquidez intradía
  · colas de operaciones que se ejecutan
    cuando entra el dinero
  · ventanas de liquidación en vez de continuo

LA ÚLTIMA ES LA MÁS EFICAZ Y LA MENOS
POPULAR, porque reduce la inmediatez.
```

### 3. El horario

```text
UN REGISTRO OPERA 24/7.
EL SISTEMA DE PAGOS DE ALTO VALOR, NO.

  → el dinero solo entra y sale del registro
    durante el horario

  CONSECUENCIA
  las operaciones fuera de horario liquidan
  contra el saldo que ya estaba dentro

  y si se agota, no hay más hasta la apertura

DISEÑO
  · saldo de reserva calculado para cubrir
    la actividad prevista fuera de horario
  · límite de operación individual fuera
    de horario
  · cola con ejecución a la apertura
  · comunicación clara: «esta operación se
    liquidará a las 09:00»

LO QUE NO SE DEBE HACER
  presentar el 24/7 sin decir que el dinero
  tiene horario.
```

### 4. Consumo de capital

```text
UNA EXPOSICIÓN AL TRAMO DE DINERO
CONSUME CAPITAL SEGÚN QUIÉN LO EMITA

  banco central          ponderación mínima
  banco supervisado      ponderación del banco
  emisor de stablecoin   según su calificación
                         y el marco aplicable

  Y EL SALDO PREFINANCIADO ES UNA EXPOSICIÓN
  QUE ESTÁ AHÍ TODO EL TIEMPO,
  no solo durante la operación

CÁLCULO QUE HAY QUE HACER
  saldo medio × ponderación × requerimiento
  = capital consumido por operar en esa
    plataforma

  y compararlo con el ahorro de la atomicidad
  (clase 8)
```

### 5. La opción sin atomicidad

```text
LIQUIDAR EL DINERO FUERA DEL REGISTRO
NO ES UN FRACASO: ES UNA DECISIÓN

  QUÉ SE PIERDE
    · la atomicidad
    · el riesgo de principal vuelve

  QUÉ SE GANA
    · no hay riesgo de emisor nuevo
    · no hay saldo prefinanciado
    · no hay que resolver el horario

  CUÁNDO ES CORRECTA
    · si el volumen no justifica el saldo
      prefinanciado
    · si no hay dinero de banco central
      ni depósito tokenizado disponible
    · si el riesgo de principal se cubre
      con garantías

Y ENTONCES HAY QUE DEJAR DE PROMETER
LIQUIDACIÓN ATÓMICA EN EL MATERIAL
COMERCIAL, que es lo que no se hace.
```

## 🧮 Ejemplo guiado

El ejemplo compara las cuatro opciones de tramo de dinero por riesgo y por coste. La opción sin riesgo de emisor es la más cara en liquidez.

**Situación.** Una plataforma decide con qué dinero liquidar. Hay que comparar
las cuatro opciones con números.

```text
DATOS
  volumen diario                   444 000 000
  operaciones diarias                    2 400
  saldo prefinanciado necesario
    sin neteo                        22 % del volumen
    con neteo                         9 % del volumen
  coste de financiación                  4,3 % anual
  requerimiento de capital              10,5 %
  ponderación banco central                 0 %
  ponderación banco supervisado            20 %
  ponderación emisor privado               100 %
  ahorro por atomicidad (clase 8)    4 884 000 al año
```

**Paso 1 — calcula el saldo prefinanciado.**

```text
SIN NETEO
  444 000 000 × 22 % = 97 680 000

CON NETEO
  444 000 000 × 9 % = 39 960 000
```

**Paso 2 — calcula el coste de financiar ese saldo.**

```text
CON NETEO, 39 960 000 AL 4,3 %
  = 1 718 280 al año

  (este coste es el mismo sea cual sea
   el emisor del dinero: es el coste de
   tener el saldo, no de quién lo debe)
```

**Paso 3 — calcula el capital consumido por emisor.**

```text
CAPITAL = saldo × ponderación × requerimiento

  CBDC MAYORISTA
    39 960 000 × 0 % × 10,5 % = 0

  DEPÓSITO TOKENIZADO
    39 960 000 × 20 % × 10,5 % = 839 160
    coste de ese capital al 12 %: 100 699 al año

  STABLECOIN
    39 960 000 × 100 % × 10,5 % = 4 195 800
    coste al 12 %: 503 496 al año

  FUERA DEL REGISTRO
    sin saldo prefinanciado → 0
```

**Paso 4 — arma la comparación completa.**

```text
                      COSTE DE     COSTE DE    AHORRO POR    NETO
                      FINANCIAR    CAPITAL     ATOMICIDAD

  CBDC mayorista      1 718 280           0     4 884 000   +3 165 720
  Depósito tokenizado 1 718 280     100 699     4 884 000   +3 065 021
  Stablecoin          1 718 280     503 496     4 884 000   +2 662 224
  Fuera del registro          0           0             0            0

LAS TRES PRIMERAS GANAN.
Y LA DIFERENCIA ENTRE ELLAS ES MENOR
DE LO QUE SUGIERE EL DEBATE PÚBLICO.
```

**Paso 5 — añade el riesgo que no está en la tabla.**

```text
LO QUE EL CÁLCULO NO CAPTURA

  STABLECOIN
    · el emisor puede suspender la redención
      (Parte 20, clase 5)
    · si pierde la paridad, el saldo
      prefinanciado vale menos
    · una pérdida del 3 % sobre 39 960 000
      son 1 198 800: dos años de ventaja

  DEPÓSITO TOKENIZADO
    · riesgo del banco, acotado por
      supervisión y garantía
    · si el banco tiene problemas, el saldo
      queda atrapado

  CBDC
    · riesgo operativo del banco central
    · disponibilidad limitada a su horario
      y a los participantes admitidos

EL RIESGO DE COLA DE LA STABLECOIN
BORRA SU VENTAJA EN UN SOLO EPISODIO.
```

**Paso 6 — resuelve el horario.**

```text
OPERACIONES FUERA DE HORARIO
  supuesto: 14 % del volumen
  444 000 000 × 14 % = 62 160 000

SALDO DE RESERVA NECESARIO
  con neteo intradía no disponible fuera
  de horario, hace falta el bruto:
  supuesto 30 % de ese volumen
  = 18 648 000 adicionales

COSTE
  18 648 000 × 4,3 % = 801 864 al año

  → el 24/7 cuesta 801 864 al año
    en saldo ocioso adicional

DECISIÓN
  ¿vale 801 864 poder liquidar de noche?
  supuesto: el 14 % del volumen paga
  una comisión adicional de 0,004 %
  62 160 000 × 0,004 % × 250 = 621 600

  → NO LO CUBRE
  → ventana ampliada en vez de 24/7,
    o comisión mayor para ese horario
```

**Paso 7 — decide.**

```text
RECOMENDACIÓN

  1 TRAMO DE DINERO
      depósito tokenizado como opción base,
      con CBDC mayorista si está disponible
      · la stablecoin solo si no hay otra,
        con límite de saldo y vigilancia
        del desvío (Parte 20, clase 3)

  2 NETEO
      reduce el saldo de 97 a 40 millones
      y con él el capital consumido

  3 HORARIO
      ventana ampliada de 07:00 a 22:00
      en vez de 24/7, con cola nocturna
      que ejecuta a la apertura

  4 LÍMITE DE SALDO EN EL EMISOR
      si es stablecoin, máximo el 5 % del
      capital de la plataforma

Y TODO ESTO SE REVISA SI EL VOLUMEN
CAMBIA UN 30 %, porque los cálculos
son lineales y las conclusiones no.
```

**Interpreta:** las tres opciones con atomicidad ganan y **la diferencia entre
ellas es menor de lo que sugiere el debate**; lo que decide no es el cálculo sino
el riesgo de cola, que la stablecoin concentra. El 24/7, presentado como ventaja,
costaba 801 864 al año y generaba 621 600.

## 🧭 Perspectivas

El tramo de dinero afecta a cada participante de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Liquidación inmediata | — |
| Inversionista | Un saldo que debe tener antes | Cuánto prefinancia |
| Banco | Capital consumido por el saldo | En qué plataforma opera |
| Emisor del dinero | Saldos de la plataforma | Qué respaldo mantiene |
| Banco central | Liquidación fuera de sus libros | Si ofrece CBDC mayorista |
| Infraestructura | Coste de liquidez | Qué modelo elige |
| Custodio | Saldos bloqueados | Cómo los refleja |
| Supervisor | Riesgo de emisor concentrado | Qué límites impone |
| Auditor | Saldo ocioso y su emisor | Qué revela |
| Sociedad | Un mercado que opera de noche | Qué continuidad exige |

## 🏦 Del cliente al banco

El cliente ve una liquidación y el banco eligió con qué dinero se liquida. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Liquida al instante» | Con 40 millones inmovilizados | 21, clase 10 |
| «Da igual con qué dinero» | Cambia el capital y el riesgo de cola | 21, clase 10 |
| «Funciona 24/7» | El dinero tiene horario | 21, clase 10 |

## ⚖️ Riesgos y controles

Los riesgos son de emisor y de liquidez intradía. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Riesgo de emisor del dinero | La stablecoin pierde paridad | Límite de saldo y vigilancia del desvío |
| Saldo ocioso excesivo | Coste de financiación alto | Neteo y ventanas de liquidación |
| Capital no calculado | Se compara solo el ahorro | Incluir ponderación por emisor |
| Horario mal resuelto | Se agota el saldo de noche | Reserva calculada y cola a la apertura |
| Atomicidad prometida sin dinero dentro | El material comercial no coincide | Corregir la comunicación |
| Cálculo lineal extrapolado | El volumen cambia y no la conclusión | Revisar con ±30 % de volumen |

## 🧪 Práctica

El laboratorio pide comparar las cuatro opciones y elegir con criterio. El coste de la prefinanciación es lo que decide.

En [`labs/lab-03.md`](../labs/lab-03.md):

1. Calcula el saldo prefinanciado con y sin neteo.
2. Compara capital consumido por las cuatro opciones.
3. Añade el escenario de pérdida de paridad del emisor privado.
4. Dimensiona el saldo de reserva para operar fuera de horario.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen liquidaciones con riesgo no eliminado. La causa es el dinero fuera del registro.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Elegir el dinero por comodidad | Es lo disponible | Calcula capital y riesgo de cola |
| Ignorar el saldo prefinanciado | No aparece en el piloto | Es el coste principal |
| Prometer 24/7 | Suena a ventaja | El dinero tiene horario |
| Comparar solo el ahorro | Es lo que se publicita | Resta financiación y capital |
| Olvidar el riesgo de cola | No cabe en la tabla | Un episodio borra años de ventaja |
| Extrapolar el cálculo | Es lineal | Revísalo con otro volumen |

## ❓ Preguntas de comprobación

1. ¿Cuáles son las cuatro opciones de tramo de dinero y cómo se ordenan?
2. ¿Por qué el dinero de banco central permite mercados con muchos
   participantes?
3. ¿Cómo se calcula el capital consumido por el saldo prefinanciado?
4. ¿Qué borra la ventaja de una stablecoin como tramo de dinero?
5. ¿Qué costó el 24/7 en el ejemplo y qué generó?

## 📥 Entregable

Guarda en `portfolio/parte-21/clase-10/`:

- el saldo prefinanciado con y sin neteo;
- la comparación de las cuatro opciones con capital incluido;
- el escenario de pérdida de paridad del emisor privado;
- la decisión de horario con su cálculo de coste y de ingreso.

## 🔗 Referencias cruzadas

- **Viene de:** clase 8; Parte 20, clases 8 y 10.
- **Continúa en:** clases 11 y 12 de esta parte.
- **Se aplica en:** Parte 22, clase 10; Parte 23, clases 5 y 7.

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

- CPMI e IOSCO (2012). *Principles for Financial Market Infrastructures*. BIS. <https://www.bis.org/cpmi/publ/d101.htm>
- Committee on Payments and Market Infrastructures (2024). *Tokenisation in the context of money and other assets*. BIS. <https://www.bis.org/cpmi/publ/d225.htm>
- Bank for International Settlements (2023). *Annual Economic Report*, capítulo III. BIS. <https://www.bis.org/publ/arpdf/ar2023e3.htm>
- Basel Committee on Banking Supervision (2022). *Prudential treatment of cryptoasset exposures* (SCO60). BIS. <https://www.bis.org/bcbs/publ/d545.htm>
- Verificación local: comprueba qué tipos de dinero admite tu jurisdicción para liquidar valores y si existe acceso a dinero de banco central para infraestructuras no bancarias. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 09 · Custodia de valores tokenizados](09-custodia-de-valores-tokenizados.md) | [Parte 21](../README.md) · [Programa](../../../SYLLABUS.md) | [11 · FX: del mercado mayorista al registro →](11-fx-del-mercado-mayorista-al-registro.md) |
<!-- gen:footer:end -->
