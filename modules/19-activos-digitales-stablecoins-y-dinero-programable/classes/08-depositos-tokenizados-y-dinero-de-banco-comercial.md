---
part: 20
class: 8
title: "Depósitos tokenizados y dinero de banco comercial"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [chile, internacional]
regulatory_topics: [depositos, dinero-bancario, liquidacion]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [BIS, BCBS, CMF]
requires_legal_review: true
---

<!-- gen:header:start -->
# Clase 08 · Depósitos tokenizados y dinero de banco comercial

> [← 07 · Stablecoins algorítmicas y su modo de fallo](07-stablecoins-algoritmicas-y-su-modo-de-fallo.md) · [Índice de la parte](../README.md) · [09 · Dinero electrónico: el régimen que ya existía →](09-dinero-electronico-el-regimen-que-ya-existia.md)

**Parte 20 — Activos digitales, stablecoins y dinero programable** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Estudiar la opción que las instituciones prefieren y que menos titulares genera:
**tokenizar el depósito bancario**. No crea un instrumento nuevo, no cambia el
régimen y conserva la singularidad del dinero.

## 📚 Objetivos

Al finalizar podrás:

1. **Explicar** qué es la singularidad del dinero y por qué se pierde.
2. **Distinguir** un depósito tokenizado de una stablecoin emitida por un banco.
3. **Describir** cómo liquida una transferencia entre dos bancos con depósitos
   tokenizados.
4. **Calcular** el ahorro operativo real de la tokenización, sin atribuirle lo
   que no le corresponde.
5. **Identificar** qué obligaciones bancarias no cambian por tokenizar.

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

| Concepto | Comprensión verificable |
|---|---|
| `depósito tokenizado` | Un depósito bancario anotado en un registro programable |
| `singularidad del dinero` | Que un peso valga lo mismo sea del banco que sea |
| `liquidación en dinero de banco central` | El tramo interbancario se salda en el banco central |
| `dinero de banco comercial` | Pasivo de un banco, no del banco central |
| `atomicidad` | Dos movimientos ocurren juntos o no ocurren |
| `libro unificado` | Registro común para activos y dinero |
| `garantía de depósitos` | Cobertura estatal hasta un límite |
| `descuento entre bancos` | Cotizar el pasivo de un banco por debajo de otro |

## 🧠 Modelo mental

```text
LA SINGULARIDAD DEL DINERO

  hoy, 1 000 en el banco A y 1 000 en el banco B
  valen exactamente lo mismo

  ¿POR QUÉ?
    · ambos se convierten a la par en efectivo
    · la liquidación interbancaria se salda
      en dinero de banco central
    · la supervisión y la garantía los igualan

  → NADIE COTIZA «pesos del banco A» frente
    a «pesos del banco B»

SI CADA BANCO EMITIERA SU PROPIO TOKEN
NEGOCIABLE EN UN MERCADO,
ESA PROPIEDAD SE PIERDE:
aparecería un descuento por banco,
y eso es un sistema monetario peor,
no uno más moderno.
```

## 📖 Desarrollo

### 1. Qué cambia y qué no

```text
CAMBIA
  · el registro donde se anota el saldo
  · la posibilidad de condicionar el movimiento
  · la posibilidad de liquidar de forma atómica
    contra otro activo del mismo registro
  · el horario: el registro puede operar 24/7

NO CAMBIA
  · quién es el obligado: el banco
  · la garantía de depósitos y su límite
  · el encaje, la liquidez y el capital
  · las obligaciones de prevención de lavado
  · el derecho del cliente a retirar
  · la contabilidad del depósito

REGLA
  si un banco te dice que tokenizar reduce
  su encaje o su capital, está equivocado
```

### 2. Cómo liquida entre dos bancos

```text
TRANSFERENCIA DE 1 000 DEL CLIENTE X (BANCO A)
AL CLIENTE Y (BANCO B)

  1 el registro quema 1 000 del token del banco A
  2 el registro acuña 1 000 del token del banco B
  3 el banco A debe 1 000 al banco B
  4 esa deuda se salda en el sistema de pagos
    de alto valor, en dinero de banco central

EL PASO 4 ES EL QUE CONSERVA LA SINGULARIDAD

  sin él, el banco B estaría acumulando
  un crédito frente al banco A
  → y empezaría a mirar cuánto le fía
  → y ahí nace el descuento
```

### 3. Qué aporta de verdad

```text
LO QUE SÍ APORTA
  · liquidación atómica contra un activo
    en el mismo registro (Parte 21)
  · condiciones programables sobre el pago
    (clase 11)
  · operación fuera del horario del sistema
    de alto valor, con el neteo posterior
  · trazabilidad y conciliación automática

LO QUE NO APORTA
  · eliminar el riesgo de crédito del banco
  · reducir el coste del cumplimiento
  · funcionar sin el sistema de pagos
  · hacer el dinero «programable» en el sentido
    de que alguien lo controle a distancia

EL AHORRO REAL SUELE ESTAR EN LA CONCILIACIÓN
Y EN EL HORARIO, NO EN LA COMISIÓN
```

### 4. Frente a una stablecoin emitida por un banco

| Aspecto | Depósito tokenizado | Stablecoin de un banco |
|---|---|---|
| Naturaleza | Depósito | Instrumento aparte |
| Garantía de depósitos | Aplica según su límite | No, salvo que la norma lo diga |
| Transferible a no clientes | Con acuñación en el otro banco | Sí, al portador |
| Riesgo de descuento | No, si liquida en banco central | Sí, cotiza en mercado |
| Cumplimiento | Del banco, con su cliente | Del emisor, con el tenedor |
| Balance | Depósito, con su encaje | Pasivo distinto |

### 5. El límite de horario

```text
EL REGISTRO OPERA 24/7.
EL SISTEMA DE ALTO VALOR, NO.

  → LAS OPERACIONES DE LA NOCHE Y DEL FIN
    DE SEMANA GENERAN POSICIONES ENTRE BANCOS
    QUE SE SALDAN AL ABRIR

  ESO ES CRÉDITO INTRADÍA ENTRE BANCOS,
  y hay que gestionarlo:
    · límites bilaterales por banco
    · garantías si se superan
    · corte automático al alcanzar el límite

QUIEN PRESENTA EL 24/7 COMO UNA MEJORA
SIN MENCIONAR ESTE CRÉDITO
NO HA MIRADO EL DISEÑO COMPLETO
```

## 🧮 Ejemplo guiado

**Situación.** Dos bancos evalúan un piloto de depósitos tokenizados para pagos
entre empresas. Hay que calcular el ahorro y separar qué parte se debe a la
tokenización.

```text
DATOS
  operaciones al mes                     84 000
  importe medio                          52 000
  coste operativo actual por operación     0,42
  incidencias de conciliación al mes        620
  coste medio de resolver una incidencia     38
  operaciones fuera de horario              9,5 %
  coste actual del retraso por operación
    fuera de horario                        2,10
```

**Paso 1 — calcula el coste actual.**

```text
COSTE OPERATIVO
  84 000 × 0,42 = 35 280

INCIDENCIAS
  620 × 38 = 23 560

RETRASO FUERA DE HORARIO
  84 000 × 9,5 % = 7 980 operaciones
  7 980 × 2,10 = 16 758

TOTAL MENSUAL = 75 598
```

**Paso 2 — estima el efecto de la tokenización.**

```text
SUPUESTOS DECLARADOS

  coste operativo por operación:  0,42 → 0,31
    (la instrucción y el asiento son el mismo acto)

  incidencias:                    620 → 150
    (el registro es común: no hay dos versiones)

  retraso fuera de horario:       eliminado
    (el registro opera 24/7)

NUEVO COSTE
  operativo    84 000 × 0,31 = 26 040
  incidencias     150 × 38   =  5 700
  retraso                    =      0
  TOTAL = 31 740

AHORRO MENSUAL = 43 858
```

**Paso 3 — separa qué parte se debe a qué.**

```text
DESCOMPOSICIÓN DEL AHORRO DE 43 858

  registro común (menos incidencias)
    23 560 − 5 700 = 17 860        40,7 %

  instrucción y asiento unificados
    35 280 − 26 040 =  9 240        21,1 %

  horario ampliado
    16 758 − 0      = 16 758        38,2 %

  TOTAL                43 858       100,0 %
```

**Paso 4 — pregunta qué de eso exige tokenizar.**

```text
REGISTRO COMÚN (17 860)
  se consigue también con una base de datos
  compartida entre los dos bancos
  → NO exige tokenizar

INSTRUCCIÓN Y ASIENTO UNIFICADOS (9 240)
  exige que el movimiento del saldo y la
  instrucción sean el mismo acto
  → SÍ es propio de un registro programable

HORARIO AMPLIADO (16 758)
  exige operar cuando el sistema de alto valor
  está cerrado
  → se consigue con neteo diferido, tokenizado
    o no

ATRIBUIBLE ESTRICTAMENTE A LA TOKENIZACIÓN:
  9 240 de 43 858 = 21,1 %
```

**Paso 5 — añade el coste que la tokenización introduce.**

```text
CRÉDITO INTRADÍA ENTRE BANCOS

  operaciones fuera de horario  7 980 al mes
  importe medio                52 000
  volumen fuera de horario  414 960 000

  supuesto: la posición neta máxima acumulada
  es el 6 % de ese volumen
  = 24 897 600

  COSTE DE GARANTIZAR ESA POSICIÓN
  al 4,5 % anual, sobre el tiempo medio
  de 14 horas:
  24 897 600 × 4,5 % × 14/(365×24) = 1 790

  más el coste de gestionar límites
  y garantías: supuesto 3 500 al mes

  COSTE NUEVO ≈ 5 290 al mes
```

**Paso 6 — calcula el resultado neto.**

```text
AHORRO BRUTO           43 858
COSTE NUEVO            −5 290
AHORRO NETO            38 568 al mes
                      462 816 al año

COSTE DE IMPLANTACIÓN (supuesto)  1 400 000
RECUPERACIÓN: 1 400 000 / 462 816 = 3,02 años

DECISIÓN
  el proyecto se sostiene, pero NO por el
  argumento con el que se presentó
```

**Paso 7 — formula la comparación obligatoria.**

```text
ALTERNATIVA SIN REGISTRO PROGRAMABLE

  base de datos compartida entre los dos bancos
  con neteo diferido y ventana ampliada

  captura  17 860 + 16 758 = 34 618
  pierde    9 240
  no introduce contrato inteligente
  coste de implantación supuesto: 500 000

  RECUPERACIÓN: 500 000 / (34 618 × 12)
               = 1,20 años

LA ALTERNATIVA RECUPERA ANTES.
Y esa comparación tiene que estar en el
expediente, aunque la decisión final
sea tokenizar por razones estratégicas.
```

**Interpreta:** el 78,9 % del ahorro no viene de tokenizar sino de tener un
registro común y un horario más largo, **dos cosas que se consiguen sin
tokens**. La decisión sigue pudiendo ser correcta, pero se justifica por la
atomicidad futura de la Parte 21, no por este ahorro.

## 🧭 Perspectivas

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un pago que llega el domingo | Si cambia su operativa |
| Comercio | Cobros conciliados solos | Si integra |
| Fintech | Un riel bancario programable | Qué construye encima |
| Banco | Menos incidencias, más crédito intradía | Si entra al consorcio |
| Banco central | La singularidad del dinero | Qué exige del tramo interbancario |
| Infraestructura | Neteo fuera de horario | Cómo lo procesa al abrir |
| Custodio | Sin cambio: es un depósito | — |
| Supervisor | Mismo régimen, nuevo riesgo operativo | Qué controles pide |
| Auditor | Conciliación automática | Qué evidencia acepta |
| Sociedad | Pagos más rápidos | Qué continuidad exige |

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Es una moneda del banco» | Es un depósito con otro soporte | 20, clase 8 |
| «Funciona el domingo» | Genera crédito intradía entre bancos | 20, clase 8 |
| «¿Sigue garantizado?» | Sí: es un depósito | 20, clase 8 |

## ⚖️ Riesgos y controles

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Pérdida de singularidad | Tokens de bancos negociados entre sí | Liquidar el tramo interbancario en banco central |
| Crédito intradía no gestionado | Posiciones que crecen de noche | Límites bilaterales y corte automático |
| Atribución de ahorro | Se acredita todo a la tokenización | Descomponer y comparar con la alternativa |
| Continuidad 24/7 | Un fallo nocturno sin equipo | Turno de guardia y modo degradado |
| Confusión con stablecoin | Se comunica mal al cliente | Materiales que digan «es un depósito» |
| Cumplimiento asumido | Se cree que el registro lo resuelve | Las obligaciones siguen siendo del banco |

## 🧪 Práctica

En [`labs/lab-01.md`](../labs/lab-01.md):

1. Clasifica un depósito tokenizado con la ficha de cinco preguntas.
2. Descompón un ahorro declarado y calcula la parte atribuible.
3. Estima el crédito intradía generado por operar fuera de horario.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Llamarlo «moneda del banco» | Suena mejor | Es un depósito; dilo así |
| Atribuir todo el ahorro | No se comparó | Descompón y compara |
| Olvidar el tramo interbancario | Se mira solo al cliente | Sin él se pierde la singularidad |
| Ignorar el crédito intradía | No aparece en el piloto | Es el coste nuevo del 24/7 |
| Suponer menos capital | Se confunde con innovación | El régimen no cambia |
| Prometer transferibilidad libre | Se copia de las stablecoins | Exige acuñación en el banco destino |

## ❓ Preguntas de comprobación

1. ¿Qué es la singularidad del dinero y qué la conserva?
2. Describe los cuatro pasos de una transferencia entre bancos.
3. ¿Qué diferencias hay entre un depósito tokenizado y una stablecoin bancaria?
4. En el ejemplo, ¿qué porcentaje del ahorro exige realmente tokenizar?
5. ¿Qué coste nuevo introduce operar 24/7 y cómo se controla?

## 📥 Entregable

Guarda en `portfolio/parte-20/clase-08/`:

- la ficha de clasificación del depósito tokenizado;
- la descomposición del ahorro con la parte atribuible aislada;
- el cálculo del crédito intradía y su coste;
- la comparación con la alternativa sin registro programable.

## 🔗 Referencias cruzadas

- **Viene de:** clases 1 y 3; Parte 18, clase 7.
- **Continúa en:** clases 10 y 11 de esta parte.
- **Se aplica en:** Parte 21, clases 10 y 11; Parte 23, clases 5 y 6.

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

- Bank for International Settlements (2023). *Annual Economic Report*, capítulo III: Blueprint for the future monetary system. BIS. <https://www.bis.org/publ/arpdf/ar2023e3.htm>
- Committee on Payments and Market Infrastructures (2024). *Tokenisation in the context of money and other assets*. BIS. <https://www.bis.org/cpmi/publ/d225.htm>
- Basel Committee on Banking Supervision (2022). *Prudential treatment of cryptoasset exposures* (SCO60). BIS. <https://www.bis.org/bcbs/publ/d545.htm>
- Comisión para el Mercado Financiero. *Normativa sobre captación de depósitos y sistemas de pago*. CMF. <https://www.cmfchile.cl/portal/principal/613/w3-channel.html>
- Verificación local: comprueba si tu jurisdicción admite anotar depósitos en registros distribuidos, qué autorización exige y cómo trata la garantía de depósitos en ese soporte. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 07 · Stablecoins algorítmicas y su modo de fallo](07-stablecoins-algoritmicas-y-su-modo-de-fallo.md) | [Parte 20](../README.md) · [Programa](../../../SYLLABUS.md) | [09 · Dinero electrónico: el régimen que ya existía →](09-dinero-electronico-el-regimen-que-ya-existia.md) |
<!-- gen:footer:end -->
