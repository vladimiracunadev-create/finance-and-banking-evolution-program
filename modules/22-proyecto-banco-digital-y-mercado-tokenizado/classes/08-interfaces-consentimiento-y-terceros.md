<!-- meta
part: 23
class: 8
title: "Interfaces, consentimiento y terceros"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [chile, internacional]
regulatory_topics: [finanzas-abiertas, consentimiento, api]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [IOSCO, CMF, OCDE]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 08 · Interfaces, consentimiento y terceros

> [← 07 · El registro de referencia del sistema](07-el-registro-de-referencia-del-sistema.md) · [Índice de la parte](../README.md) · [09 · Custodia y gestión de claves →](09-custodia-y-gestion-de-claves.md)

**Parte 23 — Proyecto — banco digital y mercado tokenizado** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Construir las interfaces por las que terceros acceden a los datos del cliente,
con el **consentimiento como régimen** y no como una casilla.

La clase 7 resolvió qué registro manda. Esta abre el sistema al exterior, que es
donde el diseño se encuentra con el derecho del cliente sobre sus propios datos.
Aplica el método de la Parte 17.

## 📚 Objetivos

Al finalizar podrás:

1. **Diseñar** el ciclo de vida del consentimiento con su revocación.
2. **Especificar** el contrato de la interfaz con su versionado.
3. **Implementar** la idempotencia de las operaciones que mueven dinero.
4. **Determinar** el reparto de responsabilidad con los terceros.
5. **Medir** la disponibilidad con un presupuesto de error.

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

Los cuatro primeros términos son el consentimiento y su alcance; los cuatro siguientes, el contrato de interfaz y su responsabilidad. La **idempotencia** es el requisito que evita el problema más caro de esta capa: un reintento no puede producir un segundo movimiento.

| Concepto | Comprensión verificable |
|---|---|
| `consentimiento` | Permiso del titular, con alcance y plazo |
| `revocación` | Retirada del permiso, con efecto inmediato |
| `alcance por finalidad` | Un permiso por cada uso concreto |
| `contrato de interfaz` | Especificación versionada de la integración |
| `idempotencia` | Que repetir una orden no la duplique |
| `presupuesto de error` | Fallo admisible dentro del objetivo |
| `tercero autorizado` | Quien accede con permiso del titular |
| `reparto de responsabilidad` | Quién responde ante el cliente |

## 🧠 Modelo mental

El consentimiento no es una pantalla: es lo único que hace legítimo que un
tercero vea los datos de una persona. Y su prueba no es que se haya obtenido,
sino que se pueda retirar y que la retirada tenga efecto de verdad.

```text
EL CICLO DE VIDA

  otorgamiento  alcance, finalidad y plazo
  uso           registrado y auditable
  renovación    activa, no tácita
  REVOCACIÓN    inmediata y verificable
  expiración    automática al vencer

Y LA PRUEBA QUE IMPORTA
  al revocar, los tokens del tercero dejan
  de funcionar ANTES de responder al
  cliente que se revocó
```

## 📖 Desarrollo

### 1. Alcance por finalidad, no por sistema

Un permiso que dice «acceso a mis cuentas» no dice para qué. El alcance útil se
define por la finalidad concreta, y eso permite revocar una sin retirar las
demás.

```text
MAL   «acceso a cuentas y movimientos»
BIEN  «consultar el saldo para calcular
       un límite de crédito, durante
       90 días»

Y ENTONCES
  el cliente puede revocar la finalidad
  de crédito y mantener la de agregación
```

### 2. Idempotencia en lo que mueve dinero

Una orden de pago que se repite por un reintento no puede ejecutarse dos veces.
La solución no es confiar en que no pase: es una huella canónica que identifique
la operación con independencia del formato.

```text
DISEÑO

  huella = resumen de los campos que
           identifican la operación
  primera vez → se ejecuta y se guarda
                la respuesta
  repetición  → se devuelve la respuesta
                guardada, sin ejecutar

Y UN BLOQUEO POR HUELLA
  para que dos intentos simultáneos no
  pasen ambos la comprobación
```

### 3. El reparto de responsabilidad

Cuando algo sale mal entre la entidad, el tercero y el cliente, la pregunta es
quién responde. Dejarlo sin escribir significa que responderá quien tenga menos
capacidad de negarse: casi siempre la entidad.

```text
QUÉ HAY QUE ESCRIBIR

  · quién autentica al cliente
  · quién valida la orden
  · quién responde de un pago no autorizado
  · en qué plazo se devuelve
  · y cómo se recupera después entre ellos

EL CLIENTE NO DEBE ESPERAR A QUE
DECIDAN: se le devuelve primero y se
resuelve después
```

## 🧮 Ejemplo guiado

El ejemplo diseña un consentimiento con alcance por finalidad y prueba el orden de la revocación. Conviene medir la ventana entre invalidar y responder: tiene que ser cero.

**Situación.** El equipo diseña la interfaz para dos terceros que quieren agregar
datos y uno que quiere iniciar pagos.

```text
DATOS
  clientes                          2 400
  terceros previstos                    3
  peticiones diarias estimadas     42 000
  objetivo de disponibilidad         99,5 %
```

**Paso 1 — define el alcance por finalidad.**

```text
FINALIDADES DECLARADAS
  agregación de saldos       lectura, 180 días
  cálculo de límite          lectura, 90 días
  iniciación de pagos        escritura, por
                             operación

  TRES PERMISOS SEPARADOS
  y el cliente revoca cada uno por su
  cuenta
```

**Paso 2 — prueba la revocación.**

```text
LA PRUEBA QUE IMPORTA

  1 el cliente revoca
  2 los tokens del tercero se invalidan
  3 SOLO ENTONCES se responde al cliente

  si se responde antes, hay una ventana
  en la que el tercero sigue accediendo
  a datos que ya no debería ver

  → la prueba comprueba el orden
```

**Paso 3 — calcula el presupuesto de error.**

```text
OBJETIVO 99,5 % SOBRE 42 000 PETICIONES
DIARIAS

  fallo admisible
  42 000 × 0,5 % = 210 al día
  = 76 650 al año

  Y ESO ES UN PRESUPUESTO, NO UN INFORME
  se gasta en despliegues y en cambios,
  y cuando se agota se paran los cambios

  MEDIRLO EN MINUTOS DE INCIDENTE
  ocultaría el goteo continuo de errores
```

**Paso 4 — reparte la responsabilidad.**

```text
PAGO NO AUTORIZADO INICIADO POR UN TERCERO

  · la entidad devuelve al cliente en 24 h
  · después reclama al tercero si el fallo
    fue de autenticación suya
  · el tercero mantiene un seguro y un
    depósito de garantía

Y LO QUE NO SE HACE
  hacer esperar al cliente a que la entidad
  y el tercero decidan de quién fue
```

**Interpreta:** El diseño más difícil de esta clase no fue técnico: fue **el orden de dos pasos
en la revocación**. Invalidar los tokens antes de responder al cliente cierra una
ventana que, medida en el sistema, era de menos de un segundo y bastaba para que
un tercero leyera datos que ya no debía ver.

## 🧭 Perspectivas

Las interfaces afectan a cada actor de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Tres permisos separados | Cuáles revoca |
| Tercero | Una interfaz versionada | Si integra |
| Equipo | Un presupuesto de error | Cómo lo gasta |
| Banco | Pagos iniciados por otros | Qué responsabilidad asume |
| Supervisor | Consentimiento con revocación probada | Qué verifica |
| Auditor | Registro de usos | Qué muestrea |
| Autoridad de datos | Alcance por finalidad | Qué observa |
| Sociedad | Datos que se pueden retirar | — |

## 🏦 Del cliente al banco

El cliente autoriza un acceso y el sistema tiene que poder demostrar exactamente qué autorizó. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Di mi consentimiento» | A tres finalidades separadas | 23, clase 8 |
| «Lo revoqué y siguió entrando» | Los tokens se invalidan antes de responder | 23, clase 8 |
| «Fue el otro» | Al cliente se le devuelve primero | 23, clase 8 |

## ⚖️ Riesgos y controles

Los riesgos son de consentimiento amplio y de reintento no idempotente. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Consentimiento por sistema | No se puede revocar en parte | Alcance por finalidad |
| Revocación en el orden equivocado | Ventana de acceso indebido | Invalidar antes de responder |
| Sin idempotencia | Un reintento duplica el pago | Huella canónica y bloqueo |
| Presupuesto en minutos | Oculta el goteo de errores | Medirlo en peticiones |
| Responsabilidad sin escribir | Responde quien no puede negarse | Reparto escrito y plazo |
| Interfaz sin versionar | Un cambio rompe integraciones | Contrato versionado |

## 🧪 Práctica

El laboratorio pide diseñar el consentimiento y probar la revocación. El orden de las operaciones en la revocación es lo que se evalúa.

En [`labs/lab-04.md`](../labs/lab-04.md):

1. Define el alcance por finalidad de cada consentimiento.
2. Prueba el orden de la revocación y mide la ventana.
3. Implementa la idempotencia con huella canónica.
4. Calcula el presupuesto de error y su regla de gasto.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen problemas en la capa de interfaces. Las causas son alcances en bloque y operaciones no idempotentes.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Consentimiento como casilla | Cumple el trámite | Es un régimen con ciclo de vida |
| Revocar y luego responder | Parece equivalente | Deja una ventana abierta |
| Confiar en que no se repita | Los reintentos existen | Idempotencia por diseño |
| Disponibilidad en minutos | Es lo que se reporta | Mide peticiones fallidas |
| Responsabilidad en el contrato marco | Está redactada | Que diga quién responde y en qué plazo |
| Cambiar la interfaz sin versión | Es más rápido | Rompe a los integrados |

## ❓ Preguntas de comprobación

1. ¿Qué cinco fases tiene el ciclo de vida del consentimiento?
2. ¿Por qué el alcance se define por finalidad y no por sistema?
3. ¿Qué orden tienen los dos pasos de la revocación y por qué importa?
4. ¿Cómo se diseña la idempotencia de una orden de pago?
5. ¿Por qué medir el presupuesto de error en peticiones y no en minutos?

## 📥 Entregable

Guarda en `portfolio/parte-23/clase-08/`:

- el ciclo de vida del consentimiento con sus tres finalidades;
- la prueba de orden de la revocación;
- el diseño de idempotencia con su huella;
- el presupuesto de error y el reparto de responsabilidad.

## 🔗 Referencias cruzadas

- **Viene de:** clase 7; Parte 17, clases 3, 4 y 8.
- **Continúa en:** clases 11 y 12 de esta parte.
- **Se aplica en:** clases 13 y 14 de esta parte.

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

- IOSCO (2023). *Policy Recommendations for Crypto and Digital Asset Markets*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- OCDE (2011). *G20 High-Level Principles on Financial Consumer Protection*. OECD. <https://www.oecd.org/finance/financial-education/48892010.pdf>
- Biblioteca del Congreso Nacional de Chile. *Ley 21.521*. <https://www.bcn.cl/leychile/navegar?idNorma=1187323>
- Comisión para el Mercado Financiero. *Normativa aplicable a entidades financieras*. CMF. <https://www.cmfchile.cl/portal/principal/613/w3-channel.html>
- Verificación local: comprueba en la fuente oficial vigente qué exige tu jurisdicción sobre este punto. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 07 · El registro de referencia del sistema](07-el-registro-de-referencia-del-sistema.md) | [Parte 23](../README.md) · [Programa](../../../SYLLABUS.md) | [09 · Custodia y gestión de claves →](09-custodia-y-gestion-de-claves.md) |
<!-- gen:footer:end -->
