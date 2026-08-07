---
part: 16
class: 6
title: "Modelo de precios"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 06 · Modelo de precios

> [← 05 · Catálogo de productos](05-catalogo-de-productos.md) · [Índice de la parte](../README.md) · [07 · Originación y decisión →](07-originacion-y-decision.md)

**Parte 16 — Proyecto Banco Virtual** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Construir el sistema de precios del Banco Austral: la tasa mínima de cada producto, el precio de
transferencia interno y la estructura de comisiones. Es la clase donde los compromisos de margen se
convierten en cifras concretas que el banco cobrará a personas reales.

## 📚 Objetivos

Al finalizar podrás:

1. **Construir** el precio de transferencia interno por plazo y producto.
2. **Calcular** la tasa mínima de cada producto del catálogo.
3. **Fijar** los precios finales con criterio de piso, contexto y techo.
4. **Diseñar** la estructura de comisiones y su correspondencia con el costo.
5. **Verificar** que los precios producen el margen comprometido.

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
| `curva de precios de transferencia` | Tasa interna por plazo. |
| `tasa mínima` | Precio bajo el cual la operación destruye valor. |
| `piso, contexto y techo` | Costo, competencia y valor. |
| `estructura de comisiones` | Componentes y su correspondencia con el costo que cubren. |
| `precio de captación` | Tasa máxima a pagar por un depósito. |
| `margen por producto` | Aporte de cada producto al margen financiero. |
| `sensibilidad de precio` | Efecto de un cambio de tasa sobre el volumen. |
| `transparencia` | Que el cliente pueda comparar y entender. |

## 🧠 Modelo mental

```text
EL SISTEMA DE PRECIOS TIENE TRES CAPAS

  1. PRECIO DE TRANSFERENCIA
     define cuánto vale el dinero dentro del banco
     y reparte el margen entre captación y colocación

  2. TASA MÍNIMA
     define el piso de cada producto

  3. PRECIO FINAL
     se decide entre el piso y el techo,
     con el contexto competitivo

SIN LA PRIMERA, LAS OTRAS DOS SON ARBITRARIAS
  porque no se sabe cuánto cuesta el dinero
```

## 📖 Desarrollo

### 1. Curva de precios de transferencia

```text
CONSTRUCCIÓN
  base: curva de rendimiento soberano local
  + diferencial de financiamiento del banco
  + prima de liquidez por plazo

  plazo      soberano   diferencial   liquidez   precio de transf.
  30 días      6,10 %      0,80 %       0,00 %       6,90 %
  90 días      6,25 %      0,85 %       0,05 %       7,15 %
  180 días     6,40 %      0,90 %       0,10 %       7,40 %
  1 año        6,60 %      0,95 %       0,15 %       7,70 %
  2 años       6,90 %      1,05 %       0,25 %       8,20 %
  3 años       7,15 %      1,15 %       0,35 %       8,65 %
  5 años       7,50 %      1,30 %       0,50 %       9,30 %
```

```text
EL DIFERENCIAL DE FINANCIAMIENTO DE UN BANCO NUEVO
  es mayor que el de uno establecido
  · sin historia crediticia
  · sin calificación
  · sin base de depósitos estable

  y ese mayor costo es una desventaja estructural
  que el modelo de negocio debe compensar
```

### 2. Tasa mínima por producto

```text
P2 — CRÉDITO ESCALONADO (plazo medio 14 meses)

  costo de fondos (precio de transferencia 14 meses)  7,88 %
  pérdida esperada (PD 6,8 %, LGD 58 %)               3,94 %
  costo operativo del producto                        3,20 %
  costo del capital (11,4 % × 17,68 %)                2,02 %
  margen objetivo                                     2,00 %
  TASA MÍNIMA                                        19,04 %

E2 — CAPITAL DE TRABAJO (plazo medio 8 meses, revolvente)

  costo de fondos (precio de transferencia 8 meses)   7,55 %
  pérdida esperada (PD 4,2 %, LGD 48 %)               2,02 %
  costo operativo                                     1,80 %
  costo del capital (9,4 % × 17,68 %)                 1,66 %
  costo del compromiso no utilizado                   0,35 %
  margen objetivo                                     1,60 %
  TASA MÍNIMA                                        14,98 %

E3 — ANTICIPO DE LIQUIDACIONES (plazo 2 días)

  costo de fondos (30 días)                           6,90 %
  pérdida esperada (riesgo del pagador, PD 0,4 %)     0,19 %
  costo operativo                                     2,40 %
  costo del capital (4,2 % × 17,68 %)                 0,74 %
  margen objetivo                                     1,20 %
  TASA MÍNIMA                                        11,43 %
```

### 3. Precio final

```text
P2 — CRÉDITO ESCALONADO
  piso (tasa mínima):              19,04 %
  contexto (competencia del segmento):
    financieras no bancarias:      38-52 %
    prestamistas informales:       muy superior
    otros bancos: no atienden el segmento
  techo (valor para el cliente):   alto, por acceso
  PRECIO DECIDIDO:                 23,50 %

  margen sobre el piso: 4,46 puntos
  posición frente a la competencia: muy por debajo

  ¿POR QUÉ NO COBRAR 35 %, SI EL MERCADO LO ADMITE?
    · el objetivo es que el cliente pueda pagar
      y ascender de escalón: un precio de 35 %
      aumenta la PD y destruye el modelo
    · la propuesta de valor es el acceso a precio razonable
    · un precio abusivo en un segmento vulnerable
      es riesgo de conducta (Parte 12, clase 8)
```

```text
E2 — CAPITAL DE TRABAJO
  piso: 14,98 %
  contexto: bancos establecidos 15,5 % a 18,2 %
            factoraje no bancario 22-28 %
  PRECIO DECIDIDO: 16,40 %
  margen sobre el piso: 1,42 puntos
  posición: en el rango bajo de la banca

E3 — ANTICIPO
  piso: 11,43 %
  contexto: factoraje 22-28 %
  PRECIO DECIDIDO: 28,00 % anual equivalente
    (0,153 % por operación de 2 días)
  margen sobre el piso: 16,57 puntos

  ¿ES ABUSIVO?
    la comparación correcta no es con el crédito:
    es con la alternativa del cliente
    su alternativa es esperar 2 días o pagar factoraje
    al 25 %
    → el precio está bajo la alternativa
    Y el margen es alto porque el costo operativo
      unitario de una operación pequeña lo es
```

### 4. Precio de captación

```text
TASA MÁXIMA A PAGAR POR UN DEPÓSITO

  precio de transferencia del plazo conductual
  − costo operativo de la cuenta
  − margen objetivo de captación

CUENTA DE PAGOS (P1)
  plazo conductual del núcleo estable: 2,5 años
  precio de transferencia: 8,40 %
  costo operativo por unidad de saldo: 4,80 %
    (saldo medio bajo, muchas transacciones)
  margen objetivo: 1,20 %
  TASA MÁXIMA: 2,40 %

  DECISIÓN: 0 % de remuneración
  → el margen de captación de P1 es de 8,40 %
    y financia el costo operativo del producto

AHORRO PROGRAMADO (P3)
  plazo conductual: 1,8 años
  precio de transferencia: 8,05 %
  costo operativo: 0,90 %
  margen objetivo: 1,20 %
  TASA MÁXIMA: 5,95 %

  DECISIÓN: 5,20 %
  → competitivo, y con margen para el banco
  → y su propósito es que el cliente construya
    un colchón, que reduce su PD
```

### 5. Estructura de comisiones

| Comisión | Cubre | Nivel |
|---|---|---|
| Recaudación (E1) | Procesamiento y disponibilidad | 0,22 % del monto |
| Pago de nómina (E4) | Procesamiento | 0,18 % del monto |
| Transferencias sobre cupo | Costo del canal | Costo real + margen |
| Mora | Gestión de cobranza temprana | Costo real, sin exceso |
| Reposición de medio de pago | Costo del plástico y envío | Costo real |
| Mantención de cuenta | — | 0: no se cobra |
| Apertura de crédito | — | 0: no se cobra |
| Prepago | — | 0: no se cobra |

```text
LA COMISIÓN DE MORA MERECE ATENCIÓN
  su costo real: gestión de contacto temprano
  costo por caso: 0,018
  DECISIÓN: comisión de 0,020 por evento,
  con máximo de 2 por período

  LO QUE SE EVITA
    comisiones acumulativas que crecen con el atraso
    y convierten un problema de 0,4 en uno de 1,2
    (el mecanismo del sobreendeudamiento, Parte 4, clase 7)
```

## 🧮 Ejemplo guiado

**Situación.** Verificar que los precios producen el margen financiero comprometido.

```text
COMPROMISO (clase 5): margen de intermediación 9,45 %
sobre activos productivos
```

**Paso 1 — calcula el margen de cada producto de colocación.**

```text
P2 — CRÉDITO ESCALONADO
  cartera: 118 048
  tasa: 23,50 %
  precio de transferencia (14 meses): 7,88 %
  MARGEN DE COLOCACIÓN: 15,62 %
  aporte: 118 048 × 15,62 % = 18 439

E2 — CAPITAL DE TRABAJO
  cartera utilizada: 214 000
  tasa: 16,40 %
  precio de transferencia (8 meses): 7,55 %
  MARGEN: 8,85 %
  aporte: 214 000 × 8,85 % = 18 939

E3 — ANTICIPO
  saldo medio: 3 923
  tasa: 28,00 %
  precio de transferencia (30 días): 6,90 %
  MARGEN: 21,10 %
  aporte: 3 923 × 21,10 % = 828

  CARTERA TOTAL: 118 048 + 214 000 + 3 923 = 335 971
  frente a los 410 940 proyectados
  → falta la cartera no utilizada de E2 y el crecimiento
```

**Paso 2 — reconcilia con la cartera proyectada.**

```text
E2 ES REVOLVENTE
  línea aprobada: 292 892
  utilización media: 73 %  → 214 000 utilizados
  no utilizado: 78 892

  LA CARTERA CONTABLE es la utilizada: 214 000
  la línea aprobada consume capital por su parte
  no utilizada (factor de conversión)

CARTERA CONTABLE TOTAL: 335 971
ACTIVOS PONDERADOS
  P2: 118 048 × 75 % =  88 536
  E2 utilizado: 214 000 × 78 % = 166 920
  E2 no utilizado: 78 892 × 20 % × 78 % = 12 307
  E3: 3 923 × 50 % = 1 962
  otros activos: 42 000
  TOTAL: 311 725

  capital al 14 %: 43 642
  capital disponible: 50 000  ✓ con holgura
```

**Paso 3 — calcula el margen de captación.**

```text
P1 — CUENTA DE PAGOS
  saldo medio: 68 000 clientes × 0,42 = 28 560
  tasa pagada: 0 %
  precio de transferencia (2,5 años): 8,40 %
  MARGEN DE CAPTACIÓN: 8,40 %
  aporte: 28 560 × 8,40 % = 2 399

P3 — AHORRO PROGRAMADO
  saldo: 18 400
  tasa pagada: 5,20 %
  precio de transferencia (1,8 años): 8,05 %
  MARGEN: 2,85 %
  aporte: 18 400 × 2,85 % = 524

E1 — CUENTA EMPRESA
  saldo medio: 9 200 empresas × 3,80 = 34 960
  tasa pagada: 0 %
  precio de transferencia: 8,20 %
  MARGEN: 8,20 %
  aporte: 34 960 × 8,20 % = 2 867

  TOTAL CAPTACIÓN: 81 920 de saldos
  MARGEN DE CAPTACIÓN: 5 790
```

**Paso 4 — verifica el balance de la tesorería.**

```text
FONDOS CAPTADOS DE CLIENTES: 81 920
FONDOS COLOCADOS: 335 971

  DÉFICIT DE FINANCIAMIENTO: 254 051
  se cubre con:
    capital: 50 000
    financiamiento mayorista y emisiones: 204 051

COSTO DEL FINANCIAMIENTO MAYORISTA
  plazo medio: 18 meses
  tasa: 8,60 %  (sobre el precio de transferencia:
  el mercado cobra más que la curva interna a un banco nuevo)

  RESULTADO DE LA TESORERÍA
    recibe de colocación: 335 971 × precio de transferencia medio 7,72 % = 25 937
    paga a captación: 81 920 × 8,32 % = 6 816
    paga al mercado: 204 051 × 8,60 % = 17 548
    capital sin costo financiero: 50 000
    RESULTADO: 25 937 − 6 816 − 17 548 = 1 573
```

**Paso 5 — consolida el margen financiero.**

```text
  margen de colocación:   38 206
  margen de captación:     5 790
  resultado de tesorería:  1 573
  MARGEN FINANCIERO:      45 569

  activos productivos: 335 971 + 90 000 (líquidos) = 425 971
  MARGEN DE INTERMEDIACIÓN: 45 569 / 425 971 = 10,70 %

  COMPROMISO: 9,45 %
  PROYECTADO: 10,70 %
```

**Paso 6 — verifica que la holgura no oculte un error.**

```text
UNA HOLGURA DE 1,25 PUNTOS EXIGE VERIFICACIÓN
(la lección de la clase 2)

  ¿ESTÁN TODOS LOS COSTOS?
    · costo del financiamiento mayorista: sí, 8,60 %
    · costo de la liquidez: los 90 000 de activos líquidos
      rinden menos que su costo de fondos
      rendimiento: 6,30 %
      costo: 8,60 %
      COSTO NETO DE LA LIQUIDEZ: 90 000 × 2,30 % = −2 070

      NO ESTABA INCLUIDO

  MARGEN FINANCIERO CORREGIDO: 45 569 − 2 070 = 43 499
  MARGEN DE INTERMEDIACIÓN: 10,21 %
```

**Paso 7 — verifica la utilización de E2.**

```text
LA UTILIZACIÓN DEL 73 % ES UN SUPUESTO CRÍTICO

  si fuera 60 %:
    cartera E2: 175 735
    margen: 15 553  (−3 386)
    margen financiero: 40 113
    margen de intermediación: 9,74 %

  si fuera 85 %:
    cartera E2: 248 958
    margen: 22 033  (+3 094)
    margen de intermediación: 10,89 %

  RANGO: 9,74 % a 10,89 %
  COMPROMISO: 9,45 %
  → se cumple en todo el rango  ✓
```

**Paso 8 — cierra la clase con los precios finales.**

```text
TABLA DE PRECIOS DEL BANCO AUSTRAL

  producto                    precio      piso     margen sobre piso
  P2 crédito escalonado       23,50 %    19,04 %       4,46 pp
  E2 capital de trabajo       16,40 %    14,98 %       1,42 pp
  E3 anticipo                 28,00 %    11,43 %      16,57 pp
  P1 cuenta de pagos           0,00 %     2,40 %*     −2,40 pp*
  P3 ahorro programado         5,20 %     5,95 %*     −0,75 pp*
  E1 cuenta empresa            0,00 %     2,60 %*     −2,60 pp*
  * en captación, el piso es un techo: pagar menos es mejor

  COMISIONES
    recaudación E1: 0,22 %
    nómina E4: 0,18 %
    mora: 0,020 por evento, máximo 2 por período
    mantención, apertura y prepago: 0

  MARGEN DE INTERMEDIACIÓN PROYECTADO: 10,21 %
  (rango 9,74 % a 10,89 % según utilización de E2)
  COMPROMISO: 9,45 %  ✓

  SUPUESTO CRÍTICO DECLARADO
    utilización de la línea E2 del 73 %
    → se monitorea desde el primer mes
```

**Interpreta:** la verificación del paso 6 encontró **un costo de 2 070 que faltaba**: el diferencial
negativo de los activos líquidos que el banco debe mantener para cumplir su cobertura de liquidez. Es un
costo real, obligatorio y fácil de olvidar porque no está asociado a ningún producto. La disciplina de
cuestionar toda holgura favorable es lo que lo hizo aparecer.

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Su tasa es mucho menor que la financiera» | Precio sobre el piso, bajo el contexto | 15, clase 7 |
| «No me cobran por abrir el crédito» | El banco gana por el margen | 16, clase 5 |
| «El anticipo es caro en tasa anual» | Comparación con su alternativa real | 13, clase 4 |
| «Mi cuenta no paga interés» | Margen de captación financia el producto | 16, clase 6 |
| «La comisión de mora es baja» | Costo real, sin exceso | 12, clase 8 |

## 🧪 Práctica

En `labs/lab-03.md`, sección de precios:

1. Construye la curva de precios de transferencia con sus tres componentes.
2. Calcula la tasa mínima de tres productos de colocación y dos de captación.
3. Fija los precios finales con piso, contexto y techo.
4. Verifica que producen el margen comprometido y cuestiona toda holgura.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Precios sin precio de transferencia | Arbitrarios | Constrúyelo primero. |
| Se cobra lo que el mercado admite | Aumenta la PD y destruye el modelo | El precio debe ser pagable. |
| Costo de la liquidez no incluido | Es obligatoria y cuesta | Inclúyelo en el margen. |
| Holgura favorable no cuestionada | Suele ocultar un costo omitido | Verifica siempre. |
| Comisiones acumulativas de mora | Producen sobreendeudamiento | Costo real y tope. |
| Supuesto de utilización no declarado | Es crítico para el margen | Decláralo y monitorea. |

## ❓ Preguntas de comprobación

1. ¿Por qué sin precio de transferencia las otras dos capas son arbitrarias?
2. ¿Por qué un banco nuevo tiene un diferencial de financiamiento mayor?
3. ¿Por qué cobrar lo que el mercado admite puede destruir el modelo?
4. ¿Cuál es la comparación correcta para juzgar el precio de un anticipo?
5. ¿Qué costo suele omitirse y por qué es fácil olvidarlo?

## 📥 Entregable

Guarda en `portfolio/parte-16/clase-06/`:

- la curva de precios de transferencia construida;
- las tasas mínimas de todos los productos;
- la tabla de precios finales con su margen sobre el piso;
- la verificación del margen comprometido con su rango de sensibilidad.

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

- Grant, J. (2011). "Liquidity transfer pricing: a guide to better practice". *BIS Occasional Paper 10*. BIS.
- Matten, C. (2000). *Managing Bank Capital* (2.ª ed.). Wiley.
- Nagle, T., Hogan, J. y Zale, J. (2016). *The Strategy and Tactics of Pricing* (6.ª ed.). Routledge.
- Basel Committee on Banking Supervision (2013). *Basel III: The Liquidity Coverage Ratio*. BIS. Costo del colchón de liquidez.
- OECD (2022). *G20/OECD High-Level Principles on Financial Consumer Protection*. OECD.
- Verificación local: revisa si existen tasas máximas convencionales en tu país y las obligaciones de información del costo total del crédito.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 05 · Catálogo de productos](05-catalogo-de-productos.md) | [Parte 16](../README.md) · [Programa](../../../SYLLABUS.md) | [07 · Originación y decisión →](07-originacion-y-decision.md) |
<!-- gen:footer:end -->
