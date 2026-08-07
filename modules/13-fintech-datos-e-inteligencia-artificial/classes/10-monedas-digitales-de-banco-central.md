---
part: 14
class: 10
title: "Monedas digitales de banco central"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 10 · Monedas digitales de banco central

> [← 09 · Criptoactivos y registro distribuido](09-criptoactivos-y-registro-distribuido.md) · [Índice de la parte](../README.md) · [11 · Ética algorítmica y sesgo →](11-etica-algoritmica-y-sesgo.md)

**Parte 14 — Fintech, datos e inteligencia artificial** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Evaluar la transformación potencialmente más profunda del sistema bancario: **que el público pueda tener
un pasivo directo del banco central**. Esta clase analiza sus diseños posibles, sus efectos sobre la
intermediación bancaria y las decisiones que un banco debe anticipar.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** la moneda digital mayorista de la minorista.
2. **Analizar** las decisiones de diseño y sus consecuencias.
3. **Evaluar** el efecto sobre los depósitos y la intermediación bancaria.
4. **Explicar** el conflicto entre privacidad y trazabilidad.
5. **Anticipar** el papel que un banco puede desempeñar.

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
| `moneda digital de banco central` | Pasivo digital del banco central, de curso legal. |
| `mayorista` | Restringida a entidades financieras para liquidación. |
| `minorista` | Disponible para el público general. |
| `modelo de dos niveles` | El banco central emite; los intermediarios distribuyen. |
| `desintermediación` | Migración de depósitos bancarios hacia el banco central. |
| `remuneración` | Que la moneda digital pague o no interés. |
| `límite de tenencia` | Tope al saldo que una persona puede mantener. |
| `programabilidad` | Capacidad de condicionar el uso de los fondos. |

## 🧠 Modelo mental

```text
HOY EL PÚBLICO TIENE DOS FORMAS DE DINERO

  EFECTIVO             pasivo del banco central
                       anónimo, físico, sin interés, sin riesgo
  DEPÓSITO BANCARIO    pasivo de un banco comercial
                       digital, con riesgo del banco,
                       cubierto parcialmente por el seguro

UNA MONEDA DIGITAL MINORISTA AÑADE UNA TERCERA

  DIGITAL Y SIN RIESGO DE CRÉDITO
  → es efectivo con las propiedades del depósito

Y AHÍ ESTÁ EL PROBLEMA
  si un instrumento sin riesgo tiene las ventajas
  del depósito, ¿por qué alguien mantendría depósitos?
```

**Todo el diseño de una moneda digital minorista consiste en responder esa pregunta sin destruir la
intermediación bancaria.** Los límites de tenencia y la no remuneración son las respuestas principales.

## 📖 Desarrollo

### 1. Mayorista y minorista

| | Mayorista | Minorista |
|---|---|---|
| Usuarios | Bancos y entidades autorizadas | Público general |
| Función | Liquidación entre entidades | Pagos y tenencia de valor |
| Novedad | Limitada: ya existen las reservas | Alta: nueva forma de dinero público |
| Riesgo para la banca | Bajo | Potencialmente alto |
| Estado de avance | Pruebas avanzadas | Diseño y pilotos |

```text
LA MAYORISTA ES EVOLUTIVA
  los bancos ya tienen cuentas en el banco central
  la novedad está en la programabilidad y en la liquidación
  simultánea de valores y efectivo

LA MINORISTA ES DISRUPTIVA
  cambia quién es la contraparte del público
```

### 2. Decisiones de diseño

```text
CADA DECISIÓN TIENE UN INTERCAMBIO EXPLÍCITO
```

| Decisión | Opción A | Opción B | Intercambio |
|---|---|---|---|
| Remuneración | Sin interés | Con interés | Sin interés protege depósitos; con interés amplía la política monetaria |
| Límite de tenencia | Con tope | Sin tope | El tope protege la intermediación; limita la utilidad |
| Distribución | Directa del banco central | Dos niveles vía intermediarios | Dos niveles preserva el papel del sector |
| Identificación | Plena | Anonimato acotado para montos bajos | Trazabilidad frente a privacidad |
| Programabilidad | Sí | No | Utilidad de política frente a libertad de uso |
| Funcionamiento sin conexión | Sí | No | Inclusión y resiliencia frente a riesgo de doble gasto |

```text
EL MODELO DE DOS NIVELES ES EL CONSENSO EMERGENTE
  el banco central emite y opera el registro
  los intermediarios gestionan la relación con el usuario:
  identificación, atención, aplicaciones, servicios

  el banco no desaparece: cambia de función
  de custodio de saldos a proveedor de servicios sobre saldos
```

### 3. Efecto sobre la intermediación

```text
EL MECANISMO DE LA DESINTERMEDIACIÓN

  el público convierte depósitos en moneda digital
      ↓
  los bancos pierden financiamiento estable y barato
      ↓
  deben sustituirlo con financiamiento mayorista, más caro
      ↓
  sube el costo de fondos
      ↓
  sube el costo del crédito o baja su volumen
```

```text
Y EL EFECTO EN ESTRÉS ES MAYOR
  en una crisis de confianza, la migración
  hacia un activo sin riesgo se acelera
  → una moneda digital sin límites podría
    hacer las corridas más rápidas y más severas
    (Parte 11, clase 4)

POR ESO LOS LÍMITES DE TENENCIA
  un tope por persona acota la migración máxima
  y convierte la moneda digital en un medio de pago
  más que en un depósito alternativo
```

| Salvaguarda | Cómo funciona |
|---|---|
| Límite de tenencia | Tope de saldo por persona |
| Sin remuneración | Elimina el incentivo de ahorro |
| Remuneración escalonada | Interés cero o negativo sobre saldos altos |
| Conversión automática | El exceso se transfiere a la cuenta bancaria vinculada |
| Distribución en dos niveles | El banco conserva la relación |

### 4. Privacidad y trazabilidad

```text
EL CONFLICTO CENTRAL

  EL EFECTIVO ES ANÓNIMO
    y esa propiedad tiene valor social:
    protege de vigilancia, de perfilado y de coacción

  UNA MONEDA DIGITAL TOTALMENTE TRAZABLE
    daría al Estado visibilidad de cada pago
    de cada persona

  UNA TOTALMENTE ANÓNIMA
    sería incompatible con las obligaciones
    de prevención de lavado
```

```text
SOLUCIONES EN DISEÑO
  · anonimato para montos pequeños, identificación
    a partir de un umbral (como el efectivo, en la práctica)
  · el intermediario conoce al usuario; el banco central
    ve transacciones sin identidad
  · separación técnica entre datos de identidad
    y datos de transacción
  · garantías legales explícitas sobre el uso de los datos

NINGUNA ES PERFECTA, Y LA DECISIÓN ES POLÍTICA
  no técnica: qué grado de privacidad
  quiere preservar una sociedad
```

### 5. Papel del banco

```text
LO QUE UN BANCO PUEDE APORTAR EN UN MODELO DE DOS NIVELES
  · identificación y cumplimiento
  · atención al usuario y resolución de problemas
  · aplicaciones y experiencia de uso
  · integración con el resto de los productos
  · servicios de valor: financiamiento, ahorro, asesoría
  · conversión entre moneda digital y depósito

LO QUE PIERDE
  · el saldo como fuente de financiamiento
  · parte del ingreso por pagos (ya reducido, clase 2)

LA PREGUNTA ESTRATÉGICA
  ¿cómo se remunera el papel de distribuidor?
  si no hay modelo de ingreso para el intermediario,
  el modelo de dos niveles no se sostiene
```

## 🧮 Ejemplo guiado

**Situación.** Un banco evalúa el efecto de una moneda digital minorista anunciada por su banco central.

```text
DISEÑO ANUNCIADO
  modelo de dos niveles: bancos distribuyen
  sin remuneración
  límite de tenencia por persona: 3,0
  conversión automática del exceso a cuenta bancaria vinculada
  identificación por el intermediario
  piloto en 18 meses, despliegue en 36

EL BANCO
  clientes personas                        584 000
  depósitos a la vista de personas         162 000
  saldo medio a la vista por persona           0,28
  costo de fondos de los depósitos a la vista  0,4 %
  costo de fondos mayorista                    6,2 %
  cartera de crédito                       248 000
```

**Paso 1 — estima la migración potencial.**

```text
LÍMITE DE TENENCIA: 3,0 por persona
SALDO MEDIO ACTUAL: 0,28

  el 87 % de los clientes tiene un saldo medio
  inferior al límite → podrían migrar TODO su saldo

NO USES EL SALDO MEDIO PARA ESTIMAR LA MIGRACIÓN
  la distribución de saldos a la vista es muy asimétrica:
  una minoría concentra la mayor parte del saldo

  con un saldo medio de 0,28 y un límite de 3,0,
  suponer que "el 87 % está bajo el límite"
  y repartir el resto uniformemente produce
  un grupo de saldo alto con saldo medio menor
  que el promedio general: una contradicción
  que delata el error de método
```

```text
  RECONSTRUCCIÓN CON LA DISTRIBUCIÓN REAL
    clientes con saldo < 0,5:   428 000, saldo total  64 200
    entre 0,5 y 3,0:            132 000, saldo total  59 400
    sobre 3,0:                   24 000, saldo total  38 400
    TOTAL:                      584 000              162 000
    saldo medio: 0,277  ✓ coherente

  MIGRACIÓN MÁXIMA TEÓRICA
    los dos primeros grupos, completo:      123 600
    el tercero, hasta el límite: 24 000 × 3,0 = 72 000
      pero su saldo total es 38 400 → migra todo
    TOTAL TEÓRICO: 162 000  (el 100 %)
```

**Paso 2 — estima la migración realista.**

```text
LA MIGRACIÓN MÁXIMA NO OCURRE PORQUE
  · el saldo a la vista se usa para pagar,
    y volverá a la cuenta con cada ingreso
  · sin remuneración, no hay incentivo de ahorro
  · la conveniencia depende de la experiencia de uso
  · muchos clientes no cambian por inercia

EVIDENCIA DE PILOTOS Y ESTUDIOS
  adopción esperada como medio de pago: alta
  saldo mantenido: bajo, típicamente equivalente
  a lo que se mantiene hoy en efectivo o billeteras

ESTIMACIÓN
  saldo migrado en régimen: 18 % de los depósitos a la vista
  = 29 160
```

**Paso 3 — calcula el efecto sobre el costo de fondos.**

```text
DEPÓSITOS PERDIDOS: 29 160
sustitución con financiamiento mayorista:
  costo actual de esos fondos: 29 160 × 0,4 % = 117
  costo de sustitución: 29 160 × 6,2 % = 1 808

INCREMENTO DEL COSTO DE FONDOS: 1 691 anuales

sobre la cartera de 248 000: 0,68 puntos de margen
```

**Paso 4 — evalúa el efecto en el escenario de estrés.**

```text
EN UNA CRISIS DE CONFIANZA
  el límite de 3,0 por persona acota la migración

  MIGRACIÓN MÁXIMA EN ESTRÉS
    los clientes correrían hasta su límite:
    584 000 × 3,0 = 1 752 000 de capacidad teórica
    pero solo pueden migrar lo que tienen: 162 000

  → el límite NO protege a este banco en estrés:
    todos sus depósitos a la vista de personas
    caben bajo el límite

CONSECUENCIA
  el límite de tenencia protege el sistema en promedio
  y no protege a un banco cuyos depositantes
  tienen saldos medios bajos
```

**Paso 5 — calcula la cobertura de liquidez en ese escenario.**

```text
SUPUESTO DE SALIDA EN ESTRÉS (Parte 11, clase 4)
  depósitos minoristas estables: 5 % de salida
  con moneda digital disponible: la salida se acelera
  supuesto revisado: 12 %

  salidas adicionales: 162 000 × 7 % = 11 340
  efecto sobre la cobertura de liquidez:
    salidas netas actuales: 93 600
    salidas revisadas: 104 940
    LCR: de 78,97 % (ejemplo de la Parte 11) a 70,4 %

  → el diseño de la moneda digital cambia
    los supuestos de salida de todo el sistema
```

**Paso 6 — evalúa el papel de distribuidor.**

```text
EL BANCO SERÁ DISTRIBUIDOR

  COSTOS
    integración técnica: 1 800 inicial
    operación y soporte: 420 anuales
    identificación y cumplimiento de usuarios: 280 anuales
    atención de incidencias: 190 anuales
    TOTAL: 1 800 inicial + 890 anuales

  INGRESOS
    ¿cuál es el modelo de remuneración del distribuidor?
    el diseño anunciado NO lo define

  ESCENARIOS
    a) sin remuneración: el banco asume 890 anuales
       más 1 691 de mayor costo de fondos = 2 581 anuales
    b) comisión por usuario activo: 584 000 × 0,0018 = 1 051
       resultado: −1 530 anuales
    c) comisión por transacción: depende del volumen
```

**Paso 7 — identifica las oportunidades.**

```text
LO QUE EL BANCO PUEDE MONETIZAR

  1. CONVERSIÓN AUTOMÁTICA
     el exceso sobre el límite va a la cuenta vinculada
     → ser la cuenta vinculada preferente
     valor: retención de 24 000 clientes de saldo alto

  2. SERVICIOS SOBRE EL SALDO
     ahorro programado, redondeo, inversión automática
     → el saldo vuelve al banco por decisión del cliente

  3. CRÉDITO INTEGRADO
     financiamiento en el momento del pago (clase 1)

  4. SERVICIOS AL COMERCIO
     conciliación, anticipo, información

  5. IDENTIDAD Y CUMPLIMIENTO COMO SERVICIO
     el banco ya identifica; puede ofrecerlo a otros
```

**Paso 8 — define la posición del banco.**

```text
ACCIONES INMEDIATAS
  1. participar en el piloto: la información
     sobre el diseño final vale más que el costo
  2. incidir en el diseño a través del gremio:
     · modelo de remuneración del distribuidor
     · límite de tenencia calibrado por saldo, no uniforme
     · conversión automática por defecto a la cuenta
       del banco donde el cliente tiene su relación principal

  3. preparar el balance:
     · reducir la dependencia de depósitos a la vista
       de 44 % a 36 % en 36 meses
     · alargar el financiamiento mayorista
     · costo estimado de la transición: 620 anuales
       frente a 1 691 del escenario no preparado

  4. desarrollar los cinco servicios monetizables
     ingreso estimado en régimen: 2 240 anuales

RESULTADO PROYECTADO
  mayor costo de fondos (preparado):     −620
  costo de distribución:                 −890
  remuneración estimada del distribuidor: +840
  servicios monetizables:               +2 240
  NETO:                                 +1 570 anuales
```

**Interpreta:** una moneda digital minorista **no destruye la banca: cambia de qué vive**. El efecto
negativo es real y cuantificable —1 691 anuales de mayor costo de fondos si no se prepara— y es menor
que el valor de los servicios que la misma infraestructura permite ofrecer. La decisión crítica no es
técnica: es participar en el diseño mientras el diseño está abierto, porque el modelo de remuneración
del distribuidor determinará si el modelo de dos niveles es viable.

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Tendré dinero del banco central en el teléfono» | Tercera forma de dinero | 14, clase 10 |
| «Mi saldo tiene un tope» | Límite que protege la intermediación | 14, clase 10 |
| «¿El Estado verá mis pagos?» | Diseño de privacidad, decisión política | 12, clase 10 |
| «El banco me ofrece servicios sobre ese saldo» | Papel del distribuidor | 14, clase 10 |
| «Mi depósito da menos interés que antes» | Mayor costo de fondos del banco | 11, clase 4 |

## 🧪 Práctica

En `labs/lab-05.md`, sección de moneda digital:

1. Evalúa seis decisiones de diseño y sus intercambios.
2. Estima la migración de depósitos con una distribución realista de saldos.
3. Calcula el efecto sobre el costo de fondos y sobre la cobertura de liquidez.
4. Diseña la estrategia de un banco como distribuidor.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se usa el saldo medio para estimar migración | Distribución asimétrica | Reconstruye la distribución real. |
| Se supone que el límite protege a todos | Depende de la base de depositantes | Evalúa tu propia distribución. |
| Se ignora el efecto sobre la liquidez en estrés | Supuestos de salida obsoletos | Revisa los supuestos conductuales. |
| Se espera al despliegue | El diseño se decide antes | Participa en el piloto. |
| Se ve solo el costo | La infraestructura permite servicios | Identifica lo monetizable. |
| Se supone remuneración del distribuidor | Puede no existir | Incide en el diseño. |

## ❓ Preguntas de comprobación

1. ¿Qué hace disruptiva a una moneda digital minorista frente a una mayorista?
2. ¿Por qué los límites de tenencia y la no remuneración son las salvaguardas principales?
3. ¿Por qué el límite de tenencia puede no proteger a un banco concreto?
4. ¿Por qué el conflicto entre privacidad y trazabilidad es una decisión política?
5. ¿Qué determina la viabilidad del modelo de dos niveles?

## 📥 Entregable

Guarda en `portfolio/parte-14/clase-10/`:

- las seis decisiones de diseño evaluadas con sus intercambios;
- la estimación de migración con distribución de saldos reconstruida;
- el efecto sobre costo de fondos y cobertura de liquidez;
- la estrategia del banco como distribuidor, con su cuantificación.

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

- Bank for International Settlements (2020). *Central bank digital currencies: foundational principles and core features*. BIS y siete bancos centrales. <https://www.bis.org/publ/othp33.htm>
- Bank for International Settlements (2021). *CBDCs: an opportunity for the monetary system*. Annual Economic Report, capítulo III. BIS.
- Committee on Payments and Market Infrastructures (2018). *Central bank digital currencies*. BIS. <https://www.bis.org/cpmi/publ/d174.htm>
- Bank of England (2023). *The digital pound: a new form of money for households and businesses?* Documento de consulta.
- European Central Bank (2023). *Digital euro: progress reports* y estudios de diseño.
- Verificación local: revisa si tu banco central tiene un proyecto de moneda digital, en qué fase está y qué decisiones de diseño ha anunciado.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 09 · Criptoactivos y registro distribuido](09-criptoactivos-y-registro-distribuido.md) | [Parte 14](../README.md) · [Programa](../../../SYLLABUS.md) | [11 · Ética algorítmica y sesgo →](11-etica-algoritmica-y-sesgo.md) |
<!-- gen:footer:end -->
