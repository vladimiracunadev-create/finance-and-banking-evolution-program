---
part: 21
class: 8
title: "Entrega contra pago atómica"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [liquidacion, riesgo-de-principal, infraestructura]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [CPMI, IOSCO, BIS]
requires_legal_review: false
---

<!-- gen:header:start -->
# Clase 08 · Entrega contra pago atómica

> [← 07 · Fraccionamiento y acceso](07-fraccionamiento-y-acceso.md) · [Índice de la parte](../README.md) · [09 · Custodia de valores tokenizados →](09-custodia-de-valores-tokenizados.md)

**Parte 21 — Tokenización, FX on-chain y mercados programables** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Diseñar la única ventaja que la tokenización aporta y no se puede conseguir de
otra forma: **que la entrega del valor y el pago del dinero sean el mismo acto**.
Y demostrar que lo es, incluidos sus modos de fallo.

## 📚 Objetivos

Al finalizar podrás:

1. **Definir** atomicidad como propiedad de un conjunto de movimientos.
2. **Distinguir** los tres modelos de entrega contra pago y cuál elimina el
   riesgo de principal.
3. **Diseñar** una liquidación atómica y probar que no existe estado intermedio.
4. **Enumerar** los modos de fallo que la atomicidad **no** cubre.
5. **Calcular** el riesgo de principal eliminado y su valor.

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
| `entrega contra pago` | Que la entrega ocurra si y solo si ocurre el pago |
| `atomicidad` | Todos los movimientos ocurren o no ocurre ninguno |
| `riesgo de principal` | Entregar y no cobrar, o pagar y no recibir |
| `estado intermedio` | Momento en que uno se movió y el otro no |
| `liquidación bruta` | Operación a operación |
| `liquidación neta` | Por saldos, tras compensar |
| `condición de reversión` | Regla que deshace lo hecho si falla algo |
| `fallo parcial` | Un tramo se ejecuta y el otro no |

## 🧠 Modelo mental

```text
LOS TRES MODELOS DE ENTREGA CONTRA PAGO

  MODELO 1 · BRUTO SIMULTÁNEO
    valor y dinero, operación a operación,
    a la vez
    → elimina el riesgo de principal
    → exige más liquidez

  MODELO 2 · VALOR BRUTO, DINERO NETO
    el valor se entrega al momento;
    el dinero se salda al final del día
    → hay exposición hasta el saldo
    → menos liquidez

  MODELO 3 · AMBOS NETOS
    todo al final del ciclo
    → máxima eficiencia de liquidez
    → máxima exposición durante el ciclo

LA TOKENIZACIÓN PERMITE EL MODELO 1
SIN SU COSTE HABITUAL DE LIQUIDEZ,
si ambos tramos están en el mismo registro.

Y ESA ES LA FRASE COMPLETA:
si no lo están, no hay atomicidad.
```

## 📖 Desarrollo

### 1. Qué es y qué no es atomicidad

```text
ATOMICIDAD ES UNA PROPIEDAD DE UN CONJUNTO
DE MOVIMIENTOS, NO DE UNA TECNOLOGÍA

  se cumple cuando NO EXISTE ningún estado
  observable en que uno se haya movido
  y el otro no

  NO BASTA CON QUE OCURRAN «CASI A LA VEZ»
  NO BASTA CON QUE HAYA UNA REVERSIÓN
    → una reversión implica que hubo un
      estado intermedio, y en ese estado
      alguien pudo actuar

CÓMO SE DEMUESTRA
  una prueba que intente observar el estado
  entre los dos movimientos y falle en
  encontrar el estado intermedio
```

### 2. La condición: mismo registro

```text
SI EL VALOR ESTÁ EN UN REGISTRO
Y EL DINERO EN OTRO

  hace falta coordinar dos sistemas
  → protocolo de dos fases, o una cadena
    de bloqueo y confirmación
  → y en ambos hay un intervalo

  ese intervalo puede ser corto, y no es cero

DÓNDE PUEDE ESTAR EL DINERO
  · depósito tokenizado del mismo registro
    (Parte 20, clase 8)
  · CBDC mayorista en el mismo registro
    (Parte 20, clase 10)
  · stablecoin del mismo registro
    → con el riesgo de emisor de la Parte 20
  · fuera → NO HAY ATOMICIDAD

ESTA LISTA ES LA QUE DECIDE
si un proyecto puede prometerla.
```

### 3. Los modos de fallo que la atomicidad no cubre

```text
LA ATOMICIDAD ELIMINA EL RIESGO DE PRINCIPAL.
NO ELIMINA:

  · RIESGO DE REEMPLAZO
      si la operación no se ejecuta, hay que
      rehacerla a otro precio

  · RIESGO DE LIQUIDEZ
      el dinero estaba bloqueado y no
      disponible para otra cosa

  · RIESGO OPERATIVO
      el registro se detiene y no se liquida
      nada

  · RIESGO JURÍDICO
      la liquidación técnica no coincide con
      la finalidad jurídica (Parte 19, clase 6)

  · RIESGO DE CONTRAPARTE PREVIO
      entre la contratación y la liquidación

CADA UNO NECESITA SU PROPIO CONTROL,
y presentar la atomicidad como si los
cubriera todos es el error de esta clase.
```

### 4. Diseño de la liquidación

```text
SECUENCIA DE UNA OPERACIÓN ATÓMICA

  1 se casan las órdenes y nace la operación
  2 se verifica que el vendedor tiene el valor
    y el comprador el dinero
  3 se bloquean AMBOS
  4 se ejecuta el intercambio en un solo acto
  5 se registra el resultado
  6 si cualquier verificación falla, no se
    bloquea nada y la operación se rechaza

EL PASO 6 ES EL DISEÑO CORRECTO
  rechazar antes de bloquear es mejor que
  bloquear y revertir, porque una reversión
  deja rastro y un rechazo no

QUÉ HAY QUE PROBAR
  · que no hay estado intermedio observable
  · que un fallo en el tramo de dinero deja
    el valor intacto
  · que un fallo en el tramo de valor deja
    el dinero intacto
  · que dos operaciones sobre el mismo saldo
    no pueden ejecutarse ambas
```

### 5. Neteo y atomicidad

```text
¿SE PUEDEN COMBINAR?

  SÍ, Y ES LO INTERESANTE

  se compensan las operaciones del ciclo
  y se liquida el saldo neto DE FORMA ATÓMICA

  · eficiencia de liquidez del neteo
  · ausencia de riesgo de principal
    de la liquidación bruta

  CONDICIÓN
    el conjunto compensado debe liquidarse
    como una sola unidad: o todo el neteo
    o nada

  RIESGO NUEVO
    si el neteo falla, fallan TODAS las
    operaciones del ciclo, no una
    → hay que dimensionar ese escenario
```

## 🧮 Ejemplo guiado

**Situación.** Una plataforma liquida 2 400 operaciones diarias de bonos
tokenizados. Hay que calcular qué riesgo elimina la atomicidad y cuánto vale.

```text
DATOS
  operaciones diarias                    2 400
  importe medio                        185 000
  volumen diario                   444 000 000
  ciclo actual                             T+2
  probabilidad de incumplimiento
    de contraparte en 2 días             0,004 %
  recuperación esperada                     45 %
  coste de financiar el bloqueo           4,3 % anual
```

**Paso 1 — calcula la exposición actual.**

```text
CON T+2 Y SIN ENTREGA CONTRA PAGO

  exposición de principal
  = volumen pendiente de liquidar
  = 444 000 000 × 2 días
  = 888 000 000 en cualquier momento
```

**Paso 2 — calcula la pérdida esperada.**

```text
PÉRDIDA ESPERADA DIARIA
  888 000 000 × 0,004 % × (1 − 45 %)
  = 888 000 000 × 0,00004 × 0,55
  = 19 536 al día

ANUAL (250 días hábiles)
  4 884 000
```

**Paso 3 — mide qué elimina la atomicidad.**

```text
CON LIQUIDACIÓN ATÓMICA EN T+0

  exposición de principal = 0
  pérdida esperada por principal = 0

  AHORRO BRUTO: 4 884 000 al año
```

**Paso 4 — resta el coste de liquidez.**

```text
LA LIQUIDACIÓN BRUTA EXIGE TENER
EL DINERO Y EL VALOR EN EL MOMENTO

  supuesto: se necesita mantener el 22 %
  del volumen diario en saldo disponible
  frente al 6 % del ciclo actual

  saldo adicional
  444 000 000 × (22 % − 6 %) = 71 040 000

  COSTE
  71 040 000 × 4,3 % = 3 054 720 al año

  AHORRO NETO
  4 884 000 − 3 054 720 = 1 829 280
```

**Paso 5 — añade el neteo.**

```text
CON NETEO Y LIQUIDACIÓN ATÓMICA DEL SALDO

  supuesto: el neteo reduce la necesidad
  de saldo al 9 % del volumen

  saldo adicional
  444 000 000 × (9 % − 6 %) = 13 320 000
  coste = 572 760 al año

  AHORRO NETO
  4 884 000 − 572 760 = 4 311 240

  → CASI EL DOBLE QUE CON BRUTO
```

**Paso 6 — dimensiona el riesgo nuevo del neteo.**

```text
SI EL NETEO FALLA, FALLAN LAS 2 400
OPERACIONES DEL CICLO

  · las contrapartes tienen que rehacerlas
    al precio del día siguiente
  · riesgo de reemplazo sobre 444 000 000

  supuesto: variación media de precio
  en un día del 0,35 %
  coste de reemplazo = 1 554 000
  por episodio

  ¿CUÁNTOS EPISODIOS AL AÑO?
  supuesto: disponibilidad del 99,9 %
  → 0,25 días al año
  → coste esperado = 388 500 al año

  AHORRO NETO CORREGIDO
  4 311 240 − 388 500 = 3 922 740
```

**Paso 7 — enumera lo que sigue sin cubrir.**

```text
LO QUE ESTOS 3,9 MILLONES NO INCLUYEN

  · riesgo de reemplazo ordinario, que
    subsiste operación a operación
  · riesgo de liquidez de la contraparte
  · riesgo operativo de la plataforma
  · riesgo jurídico: si la finalidad legal
    no coincide con la técnica, un tribunal
    puede deshacer lo atómicamente liquidado
  · riesgo del emisor del dinero, si el tramo
    de dinero es una stablecoin

EL ÚLTIMO ES EL MÁS IGNORADO
  se elimina el riesgo de principal frente
  a la contraparte y se introduce el riesgo
  de crédito frente al emisor del dinero
  → si ese emisor no es un banco central,
    el riesgo no desapareció: cambió de sitio
```

**Interpreta:** la atomicidad ahorra 3,9 millones al año y **elimina exactamente
un riesgo de cinco**. Combinada con neteo casi duplica el ahorro, a cambio de
concentrar el fallo en un único episodio que hay que dimensionar. Y si el tramo
de dinero no es un pasivo de banco central, el riesgo de principal se transformó
en riesgo de emisor.

## 🧭 Perspectivas

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Liquidación el mismo día | — |
| Inversionista | Menos riesgo de contraparte | Con quién opera |
| Banco | Más saldo inmovilizado | Cómo lo financia |
| Infraestructura | Un modelo de liquidación | Cuál implementa |
| Custodio | Bloqueos y liberaciones | Cómo los refleja |
| Emisor del dinero | Riesgo trasladado a él | Qué respaldo mantiene |
| Banco central | Liquidación fuera de sus libros | Si ofrece CBDC mayorista |
| Supervisor | Riesgo concentrado en el neteo | Qué resiliencia exige |
| Auditor | Ausencia de estado intermedio | Cómo lo verifica |
| Sociedad | Un mercado más rápido | Qué continuidad exige |

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Liquida al instante» | Y exige mucho más saldo disponible | 21, clase 8 |
| «No hay riesgo» | Se eliminó uno de cinco | 21, clase 8 |
| «Es dinero, es igual» | Si no es de banco central, hay emisor | 21, clase 8 |

## ⚖️ Riesgos y controles

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Atomicidad prometida sin cumplirla | El dinero está fuera del registro | Verificar dónde está cada tramo |
| Estado intermedio observable | Se bloquea y luego se revierte | Rechazar antes de bloquear |
| Riesgo trasladado al emisor del dinero | Se elimina uno y aparece otro | Declararlo y medirlo |
| Fallo del neteo | Fallan todas las operaciones del ciclo | Dimensionar el coste de reemplazo |
| Coste de liquidez ignorado | El ahorro se sobrestima | Restarlo del cálculo |
| Finalidad jurídica distinta | Un tribunal deshace lo liquidado | Verificar el régimen aplicable |

## 🧪 Práctica

En [`labs/lab-03.md`](../labs/lab-03.md) y
[`labs/lab-04.md`](../labs/lab-04.md):

1. Implementa la liquidación atómica con verificación previa al bloqueo.
2. Prueba que no existe estado intermedio observable.
3. Provoca el fallo de cada tramo y comprueba que el otro queda intacto.
4. Calcula el ahorro neto con bruto y con neteo, y el coste del fallo del ciclo.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Llamar atómico a «casi a la vez» | Suena equivalente | No debe existir estado intermedio |
| Bloquear y revertir | Es más fácil de implementar | Rechaza antes de bloquear |
| Olvidar el coste de liquidez | Solo se mira el riesgo eliminado | Réstalo |
| Prometerla con el dinero fuera | Se copia del material comercial | Verifica dónde está cada tramo |
| Ignorar el emisor del dinero | Parece neutro | Es riesgo de crédito nuevo |
| No dimensionar el fallo del neteo | Es poco probable | Afecta a todo el ciclo a la vez |

## ❓ Preguntas de comprobación

1. ¿Qué es exactamente la atomicidad y cómo se demuestra?
2. ¿Cuál es la condición sin la cual no puede existir?
3. Enumera los cinco riesgos y di cuál elimina la atomicidad.
4. ¿Por qué es mejor rechazar antes de bloquear que bloquear y revertir?
5. ¿Qué gana y qué arriesga combinar neteo con liquidación atómica?

## 📥 Entregable

Guarda en `portfolio/parte-21/clase-08/`:

- la secuencia de liquidación con el paso de rechazo previo;
- las pruebas de ausencia de estado intermedio y de fallo por tramo;
- el cálculo de ahorro neto con bruto y con neteo;
- la lista de los riesgos que la atomicidad no cubre, con su control.

## 🔗 Referencias cruzadas

- **Viene de:** clase 2; Parte 18, clase 15; Parte 20, clases 8 y 10.
- **Continúa en:** clases 10 y 12 de esta parte.
- **Se aplica en:** Parte 22, clase 10; Parte 23, clases 7 y 9.

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
- Committee on Payments and Market Infrastructures (1992). *Delivery versus Payment in Securities Settlement Systems*. BIS. <https://www.bis.org/cpmi/publ/d06.htm>
- Committee on Payments and Market Infrastructures (2024). *Tokenisation in the context of money and other assets*. BIS. <https://www.bis.org/cpmi/publ/d225.htm>
- Bank for International Settlements (2023). *Annual Economic Report*, capítulo III. BIS. <https://www.bis.org/publ/arpdf/ar2023e3.htm>
- Verificación local: comprueba qué momento reconoce tu jurisdicción como finalidad de la liquidación en una infraestructura basada en registro distribuido. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 07 · Fraccionamiento y acceso](07-fraccionamiento-y-acceso.md) | [Parte 21](../README.md) · [Programa](../../../SYLLABUS.md) | [09 · Custodia de valores tokenizados →](09-custodia-de-valores-tokenizados.md) |
<!-- gen:footer:end -->
