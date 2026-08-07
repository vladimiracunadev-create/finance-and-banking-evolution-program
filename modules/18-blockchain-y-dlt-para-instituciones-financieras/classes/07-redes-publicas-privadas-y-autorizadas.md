---
part: 19
class: 7
title: "Redes públicas, privadas y autorizadas"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global]
regulatory_topics: [dlt, gobernanza, cumplimiento]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [CPMI, IOSCO]
requires_legal_review: true
---

<!-- gen:header:start -->
# Clase 07 · Redes públicas, privadas y autorizadas

> [← 06 · Finalidad, reorganizaciones y tolerancia a fallos](06-finalidad-reorganizaciones-y-tolerancia-a-fallos.md) · [Índice de la parte](../README.md) · [08 · Contratos inteligentes →](08-contratos-inteligentes.md)

**Parte 19 — Blockchain y DLT para instituciones financieras** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Sustituir la clasificación de folleto —«pública, privada, híbrida»— por las dos
preguntas que de verdad la determinan: **quién puede leer** y **quién puede
escribir**. Y ver qué obligación regulatoria se activa con cada respuesta.

## 📚 Objetivos

Al finalizar podrás:

1. **Clasificar** una red por sus dos ejes independientes en vez de por su
   etiqueta.
2. **Determinar** qué obligaciones de cumplimiento son viables en cada
   combinación.
3. **Explicar** por qué una red abierta es incompatible con ciertas obligaciones
   bancarias.
4. **Evaluar** el gobierno de una red autorizada: admisión, expulsión y cambio
   de reglas.
5. **Decidir** la configuración de una red financiera con criterios trazables.

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
| `permiso de lectura` | Quién puede ver el contenido del registro |
| `permiso de escritura` | Quién puede proponer operaciones |
| `permiso de validación` | Quién participa en el consenso |
| `red abierta` | Cualquiera lee, escribe y valida sin autorización |
| `red autorizada` | Los participantes están identificados y admitidos |
| `admisión` | Proceso por el que un participante entra |
| `expulsión` | Proceso por el que un participante deja de operar |
| `gobierno de la red` | Quién decide las reglas y cómo se cambian |

## 🧠 Modelo mental

```text
DOS EJES INDEPENDIENTES, NO UNA ETIQUETA

                    ESCRITURA / VALIDACIÓN
                 abierta            autorizada
              ┌──────────────────┬──────────────────┐
   LECTURA    │  red pública     │  red pública     │
   abierta    │  abierta         │  de validadores  │
              │                  │  autorizados     │
              ├──────────────────┼──────────────────┤
   LECTURA    │  (poco frecuente)│  red autorizada  │
   restringida│                  │  de consorcio    │
              └──────────────────┴──────────────────┘

LA CASILLA DE ABAJO A LA DERECHA ES LA ÚNICA
COMPATIBLE CON LAS OBLIGACIONES DE UN BANCO
SOBRE DATOS DE CLIENTES

Y LA DE ARRIBA A LA DERECHA es la que usan varios
proyectos institucionales: cualquiera verifica,
solo los autorizados escriben
```

## 📖 Desarrollo

### 1. Qué cambia con cada permiso

```text
LECTURA ABIERTA
  · máxima verificabilidad por terceros
  · IMPOSIBLE cumplir el secreto bancario
    si el dato del cliente está dentro
  · el análisis de la cadena permite reconstruir
    relaciones comerciales

LECTURA RESTRINGIDA
  · confidencialidad entre participantes
  · la verificación externa exige confiar en el consorcio
    o en su auditor

ESCRITURA ABIERTA
  · no se puede identificar al ordenante
  · IMPOSIBLE cumplir la Recomendación 16 (Parte 18, clase 12)
  · imposible sancionar a un participante

ESCRITURA AUTORIZADA
  · identidad conocida y responsabilidad atribuible
  · se puede excluir a quien incumple
```

### 2. La incompatibilidad que decide

```text
UN BANCO TIENE OBLIGACIONES QUE NO PUEDE SUSPENDER

  · conocer a su cliente
  · que la información acompañe a la transferencia
  · no operar con personas designadas
  · guardar el secreto bancario
  · poder responder ante su supervisor por lo que ocurre

EN UNA RED CON ESCRITURA ABIERTA
  el banco no sabe quién está al otro lado
  → no puede cumplir las tres primeras

EN UNA RED CON LECTURA ABIERTA Y DATOS DE CLIENTE
  → no puede cumplir la cuarta

CONCLUSIÓN QUE NO ES IDEOLÓGICA
  un banco puede TENER EXPOSICIÓN a una red abierta
  (comprar un activo, custodiarlo) y no puede
  OPERAR SU INFRAESTRUCTURA sobre ella para sus clientes
```

### 3. Lo que sí se puede hacer sobre una red abierta

```text
· mantener exposición propia, con tratamiento prudencial
· custodiar activos de clientes, con controles
· liquidar contra ella a través de un proveedor regulado
· publicar compromisos verificables (raíces de Merkle)
· usarla como capa de disponibilidad de datos,
  con el contenido cifrado o resumido

LO QUE NO
· poner datos de clientes en claro
· aceptar operaciones de origen no identificable
· depender de ella para la firmeza de una liquidación
  sin protección jurídica (clase 6)
```

### 4. Gobierno de una red autorizada

```text
UN CONSORCIO TIENE QUE RESPONDER, POR ESCRITO

  ADMISIÓN
    ¿qué requisitos? ¿quién decide? ¿con qué mayoría?
    ¿puede un participante vetar a otro?

  EXPULSIÓN
    ¿por qué causas? ¿con qué procedimiento?
    ¿qué pasa con sus operaciones en curso?

  CAMBIO DE REGLAS
    ¿qué mayoría? ¿qué preaviso?
    ¿qué pasa con quien no actualiza?

  RESOLUCIÓN DE DISPUTAS
    ¿qué foro? ¿qué ley?

  SALIDA ORDENADA
    ¿cómo se lleva un participante sus datos?
    ¿qué pasa si el consorcio se disuelve?

LA ÚLTIMA ES LA QUE NADIE ESCRIBE Y LA QUE MÁS
IMPORTA EN UNA EVALUACIÓN DE RIESGO DE TERCEROS
```

### 5. La trampa de la etiqueta

```text
«RED PRIVADA» PUEDE SIGNIFICAR

  a) un consorcio con gobierno paritario
  b) una red operada por un proveedor,
     con los bancos como usuarios

  LA (b) NO ES UN REGISTRO DISTRIBUIDO EN EL SENTIDO
  DE LA CLASE 1: hay un operador que controla el estado
  → es una base de datos compartida con más pasos

  LA PREGUNTA QUE LO DISTINGUE
    si el operador desaparece o decide cambiar el estado,
    ¿los participantes pueden continuar sin él?
```

## 🧮 Ejemplo guiado

**Situación.** Un banco evalúa tres propuestas de proveedor para tokenizar
depósitos entre entidades. Debe clasificarlas y decidir.

```text
PROPUESTA 1
  red abierta pública, contrato inteligente propio
  los depósitos circulan entre direcciones
  coste de infraestructura: bajo
  «cualquiera puede auditar»

PROPUESTA 2
  red operada por el proveedor, participantes autorizados
  el proveedor produce todos los bloques
  coste: medio, por suscripción

PROPUESTA 3
  consorcio de 8 bancos, validación rotatoria,
  lectura restringida a participantes y supervisor
  coste: alto, con inversión inicial compartida
```

**Paso 1 — clasifica por los dos ejes.**

```text
                 lectura        escritura      validación
  P1             abierta        abierta        abierta
  P2             restringida    autorizada     ÚNICA (proveedor)
  P3             restringida    autorizada     rotatoria (8)
```

**Paso 2 — aplica la incompatibilidad.**

```text
P1 · ESCRITURA ABIERTA
  el banco no puede saber quién recibe un depósito
  tokenizado ni aplicar la Recomendación 16
  → INCOMPATIBLE con la operación para clientes

  Y LECTURA ABIERTA
  los importes y las relaciones entre entidades
  serían públicos
  → INCOMPATIBLE con el secreto

  DESCARTADA. No por preferencia: por obligación.
```

**Paso 3 — evalúa P2 con la pregunta de la clase 1.**

```text
«SI EL OPERADOR DESAPARECE O CAMBIA EL ESTADO,
¿LOS PARTICIPANTES PUEDEN CONTINUAR SIN ÉL?»

  el proveedor produce todos los bloques
  → si se detiene, la red se detiene
  → si altera el estado, ningún participante
    puede imponerse

  P2 NO ES UN REGISTRO DISTRIBUIDO:
  es una base de datos del proveedor con firma

  ESO NO LA DESCALIFICA. La descalifica como respuesta
  a la pregunta «¿por qué no una base de datos
  compartida?», que es más barata y más rápida.
```

**Paso 4 — evalúa P3.**

```text
CONSORCIO DE 8, VALIDACIÓN ROTATORIA

  n = 8  →  f = 2  (⌊(8−1)/3⌋ = 2)

  lectura restringida a participantes y supervisor
  → compatible con el secreto

  escritura autorizada
  → identidad conocida, R.16 aplicable

  si un participante desaparece, los 7 siguen
  → sí es un registro distribuido
```

**Paso 5 — pon a prueba el gobierno de P3.**

```text
PREGUNTAS AL CONSORCIO

  admisión: mayoría de 3/4, sin veto individual        ✓
  expulsión: por incumplimiento grave, mayoría 3/4,
             con audiencia previa                       ✓
  cambio de reglas: unanimidad para las esenciales,
             3/4 para el resto, preaviso de 90 días     ✓
  disputas: arbitraje en la jurisdicción del consorcio  ✓
  SALIDA ORDENADA: «se acordará en su momento»          ✗

HALLAZGO
  el punto que decide una evaluación de riesgo
  de terceros es el único sin respuesta
```

**Paso 6 — exige la respuesta antes de entrar.**

```text
LO QUE HAY QUE ACORDAR ANTES DE FIRMAR

  1. formato exportable y firmado del estado propio
     y de la historia que le afecta
  2. plazo máximo de entrega tras una salida
  3. qué ocurre con las operaciones en curso
  4. si el consorcio se disuelve: quién custodia
     el registro y por cuánto tiempo
  5. coste de la salida, fijado de antemano

SIN ESTOS CINCO PUNTOS, EL BANCO ENTRA EN UNA
DEPENDENCIA SIN PRECIO CONOCIDO
```

**Paso 7 — decide.**

```text
DECISIÓN: P3, CONDICIONADA A LOS CINCO PUNTOS DE SALIDA

  MOTIVOS
    1. P1 incumple obligaciones que el banco no puede
       suspender
    2. P2 no aporta la propiedad que justifica el coste;
       si se elige, hay que compararla con una base de
       datos compartida, no con P3
    3. P3 es la única que cumple y que sobrevive
       a la desaparición de un participante

  Y UNA OBSERVACIÓN PARA EL COMITÉ
    P2 podría ser la opción correcta si el consorcio
    no llega a formarse. Pero entonces la pregunta
    a responder no es «qué proveedor», sino
    «¿por qué no una base de datos compartida
    operada por una sociedad conjunta?» (clase 1)
```

**Interpreta:** las tres propuestas se presentaban como la misma tecnología y
eran tres cosas distintas. La clasificación por los dos ejes descartó una por
incumplimiento, reveló que otra no era lo que decía ser, y dejó el trabajo real
donde estaba: **en el acuerdo de gobierno, no en el software**.

## 🧭 Perspectivas

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un depósito tokenizado | Si le da igual la infraestructura |
| Banco | Tres propuestas «equivalentes» | Cuál cumple sus obligaciones |
| Proveedor | Una red que él opera | Cómo la presenta |
| Consorcio | Un gobierno por acordar | Qué escribe antes de operar |
| Cumplimiento | Escritura abierta | Qué descarta |
| Supervisor | Un nodo de lectura | Si le basta |
| Riesgo de terceros | Salida no acordada | Si aprueba la entrada |

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «¿Mis datos son públicos?» | Lectura abierta y secreto bancario | 19, clase 7 |
| «Cambié de banco y perdí el historial» | Salida ordenada no acordada | 19, clase 7 |
| «Mi banco dejó la red» | Expulsión u operaciones en curso | 19, clase 7 |

## ⚖️ Riesgos y controles

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Escritura abierta | No se puede identificar al ordenante | Red autorizada |
| Lectura abierta con datos | Se rompe el secreto | Datos fuera del registro |
| Operador único disfrazado | Se paga por una propiedad ausente | Pregunta de la desaparición |
| Salida no acordada | Dependencia sin precio | Cinco puntos antes de entrar |
| Cambio de reglas por mayoría simple | Se altera lo esencial | Unanimidad para lo esencial |
| Expulsión sin procedimiento | Arbitrariedad | Causas, audiencia y mayoría |

## 🧪 Práctica

En [`labs/lab-06.md`](../labs/lab-06.md) y el [proyecto](../project/README.md):

1. Clasifica cinco redes por los dos ejes, no por su etiqueta.
2. Determina qué obligaciones son viables en cada combinación.
3. Aplica la pregunta de la desaparición a tres propuestas.
4. Escribe los cinco puntos de salida ordenada de tu consorcio.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Clasificar por la etiqueta | Se copió el folleto | Dos ejes: lectura y escritura |
| «Privada» como sinónimo de segura | Se confundió permiso con control | Pregunta quién produce los bloques |
| Ignorar la salida ordenada | Se firmó la entrada | Cinco puntos antes |
| Descartar redes abiertas por completo | Se generalizó | Hay usos válidos sin datos de cliente |
| Aceptar «se acordará en su momento» | Se pospuso lo difícil | Es lo que decide la evaluación |
| Comparar P2 con P3 | Se compararon dos DLT | P2 se compara con una base de datos |

## ❓ Preguntas de comprobación

1. ¿Cuáles son los dos ejes que clasifican una red y por qué la etiqueta no
   basta?
2. ¿Qué obligaciones bancarias hace imposibles la escritura abierta?
3. ¿Qué sí puede hacer un banco sobre una red abierta?
4. ¿Qué pregunta distingue un registro distribuido de una base de datos con
   firma?
5. ¿Por qué la salida ordenada es el punto que decide una evaluación de riesgo?

## 📥 Entregable

Guarda en `portfolio/parte-19/clase-07/`:

- cinco redes clasificadas por los dos ejes;
- la tabla de obligaciones viables por combinación;
- la pregunta de la desaparición aplicada a tres propuestas;
- los cinco puntos de salida ordenada, redactados.

## 🔗 Referencias cruzadas

- **Viene de:** clases 1, 5 y 6; Parte 18, clase 12 (Recomendación 16).
- **Continúa en:** clase 10 (privacidad), clase 13 (gobernanza).
- **Se aplica en:** Parte 22, clases 12 y 13; Parte 23, clase 11.

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

- Committee on Payments and Market Infrastructures (2017). *Distributed ledger technology in payment, clearing and settlement*. BIS. <https://www.bis.org/cpmi/publ/d157.htm>
- IOSCO (2022). *Decentralized Finance Report*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD699.pdf>
- Financial Stability Board (2023). *Enhancing third-party risk management and oversight: a toolkit*. FSB. <https://www.fsb.org/2023/12/enhancing-third-party-risk-management-and-oversight-a-toolkit-for-financial-institutions-and-financial-authorities/>
- Financial Action Task Force. *Recomendación 16 y guía sobre activos virtuales*. FATF. <https://www.fatf-gafi.org/>
- NIST (2018). *NISTIR 8202: Blockchain Technology Overview*. NIST. <https://csrc.nist.gov/pubs/ir/8202/final>
- Verificación local: comprueba qué exige tu supervisor sobre gobierno y salida de infraestructuras compartidas, y si el secreto bancario de tu jurisdicción admite alguna forma de registro con lectura abierta. **Fecha de verificación de esta clase: 2026-08-06.** Esta clase no constituye asesoría legal.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 06 · Finalidad, reorganizaciones y tolerancia a fallos](06-finalidad-reorganizaciones-y-tolerancia-a-fallos.md) | [Parte 19](../README.md) · [Programa](../../../SYLLABUS.md) | [08 · Contratos inteligentes →](08-contratos-inteligentes.md) |
<!-- gen:footer:end -->
