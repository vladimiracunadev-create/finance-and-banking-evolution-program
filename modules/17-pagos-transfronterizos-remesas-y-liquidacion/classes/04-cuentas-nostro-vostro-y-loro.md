---
part: 18
class: 4
title: "Cuentas nostro, vostro y loro"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global]
regulatory_topics: [cross-border-payments, liquidez, contabilidad]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [CPMI]
requires_legal_review: false
---

<!-- gen:header:start -->
# Clase 04 · Cuentas nostro, vostro y loro

> [← 03 · Corresponsalía bancaria](03-corresponsalia-bancaria.md) · [Índice de la parte](../README.md) · [05 · Mensajería frente a movimiento de fondos →](05-mensajeria-frente-a-movimiento-de-fondos.md)

**Parte 18 — Pagos transfronterizos, remesas y liquidación internacional** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Dominar el vocabulario contable que sostiene la corresponsalía. Nostro y vostro
son **la misma cuenta vista desde los dos lados**, y confundirlos produce
descuadres que tardan semanas en resolverse.

La corresponsalía de la clase anterior se materializa en cuentas. Esta las abre, y con ellas el coste que sostiene todo el modelo: dinero inmovilizado en varias monedas que no rinde y que nadie factura como tal.

## 📚 Objetivos

Al finalizar podrás:

1. **Nombrar** correctamente una cuenta desde la perspectiva de cada banco.
2. **Registrar** los asientos de un pago en los dos libros a la vez.
3. **Conciliar** un extracto de corresponsal e identificar las cinco causas
   típicas de partida pendiente.
4. **Calcular** el coste de mantener saldos en cuenta y el descubierto intradía.
5. **Explicar** por qué una cuenta espejo bien llevada es la única defensa
   contra un descuadre.

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

Los tres primeros términos son la misma cuenta vista desde tres posiciones; los cinco siguientes, su operación y su coste. El **saldo ocioso** es el coste que nadie factura y todos pagan: el dinero inmovilizado en cuentas de corresponsalía no rinde y financia la operación de otro.

| Concepto | Comprensión verificable |
|---|---|
| `nostro` | «Nuestra cuenta en vuestro banco», en moneda extranjera |
| `vostro` | «Vuestra cuenta en nuestro banco», desde el corresponsal |
| `loro` | «Su cuenta», la de un tercero, cuando se habla de ella |
| `cuenta espejo` | Réplica interna del nostro, llevada por el banco titular |
| `partida pendiente` | Apunte en un libro sin contrapartida en el otro |
| `conciliación` | Proceso que casa los dos libros y explica las diferencias |
| `descubierto intradía` | Saldo negativo temporal admitido por el corresponsal |
| `saldo ocioso` | Fondos en cuenta que no rinden y no se necesitan |

## 🧠 Modelo mental

El modelo mental es un espejo: la misma cuenta es nostro para uno y vostro para el otro, y los dos registros tienen que coincidir siempre. Cuando no coinciden, la diferencia es una partida pendiente que hay que explicar.

```text
UNA SOLA CUENTA, DOS NOMBRES

  Banco chileno mantiene USD en un banco de Nueva York

  DESDE EL BANCO CHILENO   →  es su NOSTRO
                              activo en su balance
                              «nuestro dinero, allá»

  DESDE EL BANCO DE NY     →  es un VOSTRO
                              pasivo en su balance
                              «su dinero, aquí»

  Y SI UN TERCERO HABLA DE ELLA  →  la llama LORO

REGLA MNEMOTÉCNICA QUE NO FALLA
  el prefijo indica DE QUIÉN ES EL DINERO,
  no dónde está la cuenta

LA CONSECUENCIA CONTABLE
  el mismo pago produce un CARGO en un libro
  y un ABONO en el otro, por el mismo importe,
  en la misma divisa, con la misma fecha valor.
  Si esos cuatro datos no coinciden, hay descuadre.
```

## 📖 Desarrollo

### 1. Los asientos de un pago, en los dos libros

```text
BANCO CL paga 10 000 USD a un cliente del BANCO NY

  LIBRO DEL BANCO CL
    Cargo    Cuenta corriente del cliente         9 500 000 CLP
    Abono    Posición de cambio                   9 500 000 CLP
    Cargo    Posición de cambio                      10 000 USD
    Abono    Nostro en Banco NY                      10 000 USD

  LIBRO DEL BANCO NY
    Cargo    Vostro de Banco CL                      10 000 USD
    Abono    Cuenta del beneficiario                 10 000 USD

OBSERVA
  · el nostro del CL DISMINUYE (abono en un activo)
  · el vostro en NY DISMINUYE (cargo en un pasivo)
  · los dos movimientos son el MISMO hecho
  · la posición de cambio es la cuenta puente
    entre las dos monedas: es donde vive el riesgo de cambio
```

### 2. La cuenta espejo

```text
EL PROBLEMA
  el banco CL no ve el libro del banco NY en tiempo real:
  recibe un extracto (camt.053) al cierre

LA SOLUCIÓN
  el banco CL lleva una CUENTA ESPEJO: su propia réplica
  de lo que cree que dice el nostro

  espejo = lo que YO creo que hay
  extracto = lo que EL CORRESPONSAL dice que hay

LA CONCILIACIÓN COMPARA LAS DOS
  y cada diferencia tiene que tener nombre
```

### 3. Las cinco causas de partida pendiente

| Causa | Qué ocurre | Cómo se resuelve |
|---|---|---|
| **Diferencia temporal** | El apunte está en un libro y aún no en el otro | Espera al siguiente extracto |
| **Comisión no prevista** | El corresponsal cobró algo no registrado | Registrar y revisar el tarifario |
| **Importe distinto** | Un intermediario dedujo en tránsito | Investigación con referencia |
| **Apunte duplicado** | Reintento sin idempotencia | Solicitud de anulación |
| **Apunte ajeno** | Movimiento que no corresponde | Reclamación inmediata |

```text
LA REGLA DE ORO DE LA CONCILIACIÓN
  una partida pendiente sin CAUSA IDENTIFICADA
  no es una partida pendiente: es una pérdida
  que todavía no se ha reconocido

  por eso las partidas se clasifican por ANTIGÜEDAD:
    0–5 días     normal
    6–30 días    investigar
    31–90 días   escalar y provisionar
    > 90 días    reconocer el quebranto
```

### 4. El coste de tener saldos

```text
UN NOSTRO NECESITA SALDO PARA PODER PAGAR.
ESE SALDO CUESTA.

  SALDO MEDIO           4 100 000 USD
  REMUNERACIÓN RECIBIDA          0,8 % anual
  COSTE DE FONDEO DEL BANCO      4,6 % anual
  COSTE NETO                     3,8 % anual

  4 100 000 × 3,8 % = 155 800 USD al año
  solo por tener el dinero disponible

DE AHÍ SALE TODA LA GESTIÓN DE LIQUIDEZ
  bajar el saldo medio ahorra dinero
  y aumenta el riesgo de no poder pagar
```

### 5. Descubierto intradía

```text
EL CORRESPONSAL PUEDE ADMITIR SALDO NEGATIVO
DURANTE EL DÍA, A CAMBIO DE

  · un límite explícito
  · una comisión de disponibilidad
  · a veces, garantía
  · y la obligación de cerrar en positivo

QUÉ PERMITE
  operar con saldo medio mucho menor

QUÉ RIESGO CREA
  si el banco no puede cerrar en positivo,
  el corresponsal tiene una exposición no prevista
  → y suele reaccionar reduciendo el límite
    justo cuando el banco más lo necesita
```

## 🧮 Ejemplo guiado

El ejemplo concilia una cuenta nostro con su espejo. Conviene clasificar cada diferencia: unas son desfases y otras son errores.

**Situación.** Un banco concilia su nostro en dólares al cierre de mes. El espejo
y el extracto no coinciden.

```text
SALDO SEGÚN CUENTA ESPEJO      6 482 350,00 USD
SALDO SEGÚN EXTRACTO           6 471 128,40 USD
DIFERENCIA                        11 221,60 USD

PARTIDAS IDENTIFICADAS
  P1  pago de 8 500,00 registrado el 30, no aparece en el extracto
  P2  comisión de 45,00 en el extracto, no registrada
  P3  abono de 2 800,00 en el extracto, sin identificar
  P4  pago de 15 000,00 registrado; en el extracto figura 14 976,60
  P5  cargo de 1 500,00 en el extracto por un pago del mes anterior
```

**Paso 1 — clasifica cada partida.**

```text
P1  8 500,00   diferencia temporal (enviado el 30, valor el 1)
P2     45,00   comisión no prevista
P3  2 800,00   apunte no identificado
P4     23,40   diferencia de importe (15 000,00 − 14 976,60)
P5  1 500,00   apunte del mes anterior, aplicado tarde
```

**Paso 2 — reconstruye la diferencia.**

```text
Espejo dice 6 482 350,00. Empezamos ahí y aplicamos
lo que el corresponsal ve y nosotros no, y viceversa.

  − P1  el espejo ya restó 8 500 que el extracto aún no
        → para llegar al extracto hay que SUMARLOS
        +8 500,00

  − P2  el extracto restó 45 que el espejo no
        −45,00

  − P3  el extracto sumó 2 800 que el espejo no
        +2 800,00

  − P4  el extracto restó 23,40 menos de lo previsto...
        NO: restó 14 976,60 en vez de 15 000,00
        el espejo restó 23,40 de más → +23,40
        ESPERA: eso no cuadra. Ver paso 3.

  − P5  el extracto restó 1 500 que el espejo ya había
        restado el mes pasado
        −1 500,00
```

**Paso 3 — detente en P4: la trampa de la clase.**

```text
EL BANCO ORDENÓ 15 000,00 Y EL EXTRACTO DICE 14 976,60

  LECTURA INGENUA
    «nos cobraron 23,40 menos, mejor para nosotros»

  LECTURA CORRECTA
    el nostro se adeudó por 14 976,60, no por 15 000,00
    → SALIERON MENOS FONDOS DE LOS QUE ORDENAMOS
    → o el beneficiario recibió menos,
      o el corresponsal aplicó mal la instrucción

  ESTO NO ES UNA DIFERENCIA A NUESTRO FAVOR:
  ES UN PAGO QUE PUEDE ESTAR MAL EJECUTADO

  ACCIÓN: investigación con referencia extremo a extremo
  ANTES de ajustar nada
```

**Paso 4 — completa la conciliación con el signo correcto.**

```text
PARTIENDO DEL ESPEJO           6 482 350,00
  + P1 (aún no en el extracto)      8 500,00   → 6 490 850,00
  − P2 (comisión no registrada)        45,00   → 6 490 805,00
  + P3 (abono no registrado)        2 800,00   → 6 493 605,00
  + P4 (diferencia de importe)         23,40   → 6 493 628,40
  − P5 (cargo del mes anterior)     1 500,00   → 6 492 128,40

RESULTADO                       6 492 128,40
EXTRACTO                        6 471 128,40
DIFERENCIA RESIDUAL                21 000,00  ← NO CUADRA
```

**Paso 5 — busca la partida que falta.**

```text
QUEDAN 21 000,00 SIN EXPLICAR.

  ¿Es un número redondo? Sí.
  ¿Coincide con algún pago del día? Se revisa el diario.

  HALLAZGO
    dos pagos de 10 500,00 al mismo beneficiario,
    el mismo día, con la misma referencia del ordenante,
    y una sola clave de idempotencia en el mensaje

  → apunte duplicado (causa 4)
  → el espejo registró uno, el corresponsal ejecutó dos

CONCILIACIÓN FINAL
  6 492 128,40 − 21 000,00 = 6 471 128,40  ✓ CUADRA
```

**Paso 6 — clasifica y actúa.**

```text
P1   temporal          se resuelve solo         sin acción
P2   comisión           registrar y revisar tarifario
P3   no identificado    reclamar identificación en 5 días
P4   importe distinto   INVESTIGACIÓN: pago posiblemente mal ejecutado
P5   aplicación tardía  registrar y medir el retraso del corresponsal
P6   duplicado 21 000   SOLICITUD DE ANULACIÓN URGENTE

PRIORIDAD
  P6 primero: son 21 000 fuera del banco por un defecto propio
  P4 después: puede afectar a un cliente que no ha reclamado aún
```

**Paso 7 — extrae la lección de proceso.**

```text
EL DUPLICADO NO ES UN PROBLEMA DE CONCILIACIÓN:
ES UN PROBLEMA DE IDEMPOTENCIA (Parte 17, clase 8)

  el mensaje salió dos veces con la misma referencia
  y el corresponsal, que no tiene por qué deduplicar,
  ejecutó los dos

  CORRECCIÓN
    identificador extremo a extremo único por operación,
    control de duplicados ANTES de enviar,
    y alerta si dos mensajes comparten referencia
    en la misma ventana

  LA CONCILIACIÓN LO DETECTÓ A FIN DE MES.
  UN CONTROL EN ORIGEN LO HABRÍA EVITADO EL MISMO DÍA.
```

**Interpreta:** de las seis partidas, dos eran normales, una era una comisión,
una un retraso, y **dos eran incidentes reales** que la conciliación sacó a la
luz. Una conciliación que solo persigue cuadrar el número desperdicia la única
oportunidad estructurada de detectarlos.

## 🧭 Perspectivas

Las cuentas de corresponsalía significan cosas distintas para cada parte. La tabla las recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | «Pagué y llegó otra cifra» | Si reclama |
| Tesorería | Saldo ocioso de 4,1 millones | Cuánto deja en cuenta |
| Contabilidad | Partidas pendientes por antigüedad | Cuándo provisiona |
| Banco corresponsal | Vostro con duplicados | Si endurece condiciones |
| Auditor | Partidas de más de 90 días | Si exige quebranto |
| Riesgo operacional | Duplicado por falta de control | Qué control implanta |
| Supervisor | Descuadres recurrentes | Si observa el proceso |

## 🏦 Del cliente al banco

El cliente no las ve y su pago se ejecuta moviendo saldos en ellas. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Me cargaron dos veces» | Apunte duplicado por falta de idempotencia | 18, clase 4 |
| «Llegó menos de lo enviado» | Diferencia de importe en tránsito | 18, clases 1 y 4 |
| «Aparece un cargo raro» | Comisión del corresponsal no repercutida | 18, clase 4 |
| «Tardó en verse» | Diferencia temporal entre libros | 18, clase 7 |

## ⚖️ Riesgos y controles

Los riesgos son de conciliación y de coste de liquidez. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Descuadre no explicado | Diferencia sin causa asignada | Clasificación obligatoria por causa |
| Pérdida no reconocida | Partida vieja arrastrada | Antigüedad con provisión automática |
| Pago duplicado | Mensaje reenviado | Identificador único y control en origen |
| Saldo ocioso | Exceso de fondos sin rendir | Objetivo de saldo y medición del coste |
| Descubierto no controlado | Se supera el límite intradía | Seguimiento en tiempo real y alerta |
| Extracto no procesado | Conciliación con retraso | Ingesta automática con alerta de ausencia |

## 🧪 Práctica

El laboratorio pide conciliar una cuenta nostro y calcular el coste del saldo ocioso. Las dos cifras juntas son el argumento para renegociar el saldo objetivo.

En [`labs/lab-01.md`](../labs/lab-01.md):

1. Registra los asientos de tres pagos en los dos libros.
2. Concilia un extracto con siete partidas y clasifícalas por causa.
3. Calcula el coste anual del saldo medio y el efecto de reducirlo un 30 %.
4. Identifica qué partida es un incidente y no una diferencia.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen descuadres en corresponsalía. Las causas son partidas pendientes antiguas y espejos que no se contrastan.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Confundir nostro y vostro | Se pensó en dónde está la cuenta | El prefijo dice de quién es el dinero |
| «Diferencia a favor» | Se leyó el signo sin pensar | Menos fondos salidos puede ser un fallo |
| Ajustar para cuadrar | Se buscó el número, no la causa | Sin causa no hay ajuste |
| Partidas sin antigüedad | No se clasificaron | Cuatro tramos con acción por tramo |
| Saldo alto «por seguridad» | No se midió su coste | Coste neto de fondeo explícito |
| Conciliar solo a fin de mes | Se trató como tarea contable | Conciliación diaria y alertas |

## ❓ Preguntas de comprobación

1. ¿Qué indica el prefijo *nostro* o *vostro*, y por qué no es la ubicación?
2. Escribe los asientos de un pago de 10 000 USD en los dos libros.
3. ¿Cuáles son las cinco causas de partida pendiente y cuál exige acción
   inmediata?
4. ¿Por qué un cargo menor al ordenado no es una buena noticia?
5. ¿Por qué el duplicado del ejemplo es un problema de idempotencia y no de
   conciliación?

## 📥 Entregable

Guarda en `portfolio/parte-18/clase-04/`:

- los asientos de tres pagos en los dos libros;
- una conciliación completa con las partidas clasificadas por causa;
- el cálculo del coste del saldo medio y del efecto de reducirlo;
- la identificación de qué partidas son incidentes, con la acción propuesta.

## 🔗 Referencias cruzadas

- **Viene de:** clase 3 (corresponsalía); Parte 5 (contabilidad); Parte 17,
  clase 8 (idempotencia).
- **Continúa en:** clase 8 (liquidez y prefinanciación), clase 7 (liquidación).
- **Se aplica en:** Parte 23, clase 9 (liquidez multidivisa).

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

- Committee on Payments and Market Infrastructures (2003). *A glossary of terms used in payments and settlement systems*. BIS. <https://www.bis.org/cpmi/glossary_030301.htm>
- Committee on Payments and Market Infrastructures (2016). *Correspondent banking*. BIS. <https://www.bis.org/cpmi/publ/d147.htm>
- ISO 20022. *camt.053 Bank to Customer Statement: guía de uso*. <https://www.iso20022.org/>
- IFRS Foundation. *NIC 21, Efectos de las variaciones en las tasas de cambio de la moneda extranjera*. <https://www.ifrs.org/>
- Basel Committee on Banking Supervision (2013). *Basel III: The Liquidity Coverage Ratio*. BIS. <https://www.bis.org/publ/bcbs238.htm>
- Verificación local: comprueba el tratamiento contable y prudencial de las posiciones en moneda extranjera y los requisitos de conciliación de tu jurisdicción. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 03 · Corresponsalía bancaria](03-corresponsalia-bancaria.md) | [Parte 18](../README.md) · [Programa](../../../SYLLABUS.md) | [05 · Mensajería frente a movimiento de fondos →](05-mensajeria-frente-a-movimiento-de-fondos.md) |
<!-- gen:footer:end -->
