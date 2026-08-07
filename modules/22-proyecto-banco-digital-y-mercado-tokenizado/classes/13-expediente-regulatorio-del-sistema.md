---
part: 23
class: 13
title: "Expediente regulatorio del sistema"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [chile, internacional]
regulatory_topics: [cumplimiento, expediente, supervision]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [CMF, FSB, IOSCO]
requires_legal_review: true
---

<!-- gen:header:start -->
# Clase 13 · Expediente regulatorio del sistema

> [← 12 · Ciclo de vida y operación diaria](12-ciclo-de-vida-y-operacion-diaria.md) · [Índice de la parte](../README.md) · [14 · Modelo de amenazas priorizado →](14-modelo-de-amenazas-priorizado.md)

**Parte 23 — Proyecto — banco digital y mercado tokenizado** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Reunir todo lo construido en el expediente que sostiene el sistema ante un
supervisor, y **cruzarlo por parejas** para encontrar lo que ninguna pieza
muestra por separado.

Las clases 7 a 12 construyeron el sistema y la 12 encontró tres tensiones al
hacerlo funcionar un día. Esta abre el bloque de defensa aplicando el método de
la Parte 22, clase 18 al propio proyecto.

## 📚 Objetivos

Al finalizar podrás:

1. **Ensamblar** las doce piezas del expediente del sistema.
2. **Cruzar** las cinco parejas críticas y anotar las contradicciones.
3. **Priorizar** los hallazgos por su efecto sobre el cliente.
4. **Construir** la remediación con su medida provisional.
5. **Retirar** del expediente toda afirmación sin evidencia.

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
| `expediente` | Conjunto ordenado que sostiene la posición |
| `pieza` | Una sección con sus afirmaciones y su evidencia |
| `lectura cruzada` | Revisión por parejas de piezas |
| `hallazgo bloqueante` | El que impide operar hasta corregirse |
| `medida provisional` | Lo que protege mientras se corrige |
| `evidencia` | Documento o dato que sostiene una afirmación |
| `trazabilidad` | Quién afirmó qué, cuándo y con qué base |
| `revisión periódica` | Rehacer el expediente al cambiar los hechos |

## 🧠 Modelo mental

Las doce piezas las escriben equipos distintos y cada una suele ser internamente
coherente. Lo que un supervisor hace en su primera lectura es cruzarlas, y ahí
aparecen las contradicciones.

```text
LAS CINCO PAREJAS CRÍTICAS

  perímetro     x resiliencia
  calificación  x información y conducta
  salvaguarda   x prevención
  datos         x vigilancia
  jurisdicción  x conducta

Y LA REGLA
  cada afirmación con su evidencia,
  o se retira del expediente

Un supervisor que encuentra una afirmación
sin respaldo revisa las demás con otra
actitud.
```

## 📖 Desarrollo

### 1. Qué cuenta como evidencia

Una política que describe lo que debería ocurrir no es evidencia. Lo es un dato
extraído del sistema con fecha, un contrato con su cláusula o el registro de una
prueba ejecutada.

```text
SÍ
  contrato firmado, con su cláusula
  dato del sistema, con fecha
  informe de un tercero, con su alcance
  registro de una prueba ejecutada
  acta con la decisión y quién la tomó

NO
  una política que describe el deber ser
  una captura sin fecha
  «así lo hacemos siempre»
```

### 2. La priorización por efecto

El criterio no es la gravedad formal de la infracción sino qué le pasa al
cliente. Y hay una comprobación de control sobre la propia revisión.

```text
NIVEL 1  el cliente puede perder dinero
         y nada lo evita
NIVEL 2  está protegido y no acreditado
NIVEL 3  correcto y mejorable

Y LA COMPROBACIÓN
  si todos los hallazgos son de nivel 3,
  la revisión no miró donde debía
```

### 3. La medida provisional

Entre que se detecta un hallazgo y se corrige hay un intervalo, y el cliente está
expuesto durante ese intervalo. Es el elemento que falta en casi todos los
planes.

```text
CADA REMEDIACIÓN NECESITA

  la corrección concreta
  el responsable, con nombre
  el plazo
  cómo se verificará
  Y QUÉ SE HACE MIENTRAS TANTO

Sin la última, el plan documenta el
problema y no protege de él.
```

## 🧮 Ejemplo guiado

**Situación.** El equipo ensambla las doce piezas del sistema construido y las
cruza.

```text
PIEZAS
  las doce, elaboradas por los equipos de
  arquitectura, producto, cumplimiento,
  operaciones y legal

CLIENTES                          2 400
COLATERAL                    24 000 000
```

**Paso 1 — cruza perímetro con resiliencia.**

```text
PERÍMETRO  «la custodia del colateral está
           delegada en un tercero»
RESILIENCIA describe el esquema 3-de-5
           del registro propio

  ¿CONTRADICCIÓN?
  no: son claves distintas, las del registro
  y las del colateral

  → SE ANOTA COMO ACLARACIÓN, no como
    hallazgo, y se precisa en ambas piezas
    para que un lector externo no lo lea
    como contradicción
```

**Paso 2 — cruza calificación con conducta.**

```text
CALIFICACIÓN  «el depósito tokenizado se
              excluyó del catálogo»
CONDUCTA      el material comercial en
              preparación lo menciona

  HALLAZGO 1 · NIVEL 1
  el material describe un producto que la
  clase 6 excluyó por inducir a error

  MEDIDA PROVISIONAL
  el material no se publica hasta corregirse
```

**Paso 3 — cruza salvaguarda con prevención.**

```text
SALVAGUARDA «los fondos están en cuenta
            de clientes con renuncia a
            compensar»
PREVENCIÓN  describe devoluciones desde
            la cuenta operativa

  HALLAZGO 2 · NIVEL 1
  hay movimientos entre ambas cuentas que
  la pieza de salvaguarda no describe

  MEDIDA PROVISIONAL
  conciliación manual diaria con reporte
  al comité, hasta separar los flujos
```

**Paso 4 — prioriza y cierra.**

```text
HALLAZGOS
  1 material con producto excluido   nivel 1
                                     2 400 clientes
  2 flujos entre cuentas             nivel 1
                                     2 400 clientes
  3 tolerancia de margen incompatible nivel 2
                                     180 clientes
  4 documentación de claves dispersa  nivel 3

  DOS BLOQUEANTES, UNO RELEVANTE
  Y UNO ORDINARIO

  → LA REVISIÓN MIRÓ DONDE DEBÍA

Y EL SISTEMA NO PUEDE OPERAR hasta que
los dos bloqueantes estén remediados o
sus medidas provisionales activas
```

**Interpreta:** El cruce encontró dos hallazgos bloqueantes, y el primero venía de un material
comercial que describía un producto que la clase 6 había excluido. **Nadie había
avisado al área comercial de la exclusión**, y esa desconexión entre piezas es
exactamente lo que el cruce existe para detectar.

## 🧭 Perspectivas

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un material que anuncia un producto | Si lo contrata |
| Área comercial | Una exclusión que no conocía | Qué corrige |
| Cumplimiento | Dos bloqueantes | Qué medida provisional activa |
| Operaciones | Flujos entre cuentas | Cómo los separa |
| Dirección | El sistema no puede operar | Si acepta el plazo |
| Supervisor | Un expediente cruzado | Qué observa |
| Auditor | Afirmaciones con evidencia | Qué muestrea |
| Sociedad | Un sistema que se revisa antes | — |

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Ofrecen un depósito» | Se excluyó del catálogo | 23, clase 13 |
| «Está todo separado» | Hay movimientos no descritos | 23, clase 13 |
| «Cada área hizo lo suyo» | Y nadie cruzó las piezas | 23, clase 13 |

## ⚖️ Riesgos y controles

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Piezas por separado | Cada una coherente, el conjunto no | Lectura cruzada por parejas |
| Afirmación sin evidencia | El expediente pierde credibilidad | Se retira |
| Todo de nivel 3 | La revisión no miró bien | Comprobación explícita |
| Plan sin provisional | El cliente queda expuesto | Qué se hace mientras tanto |
| Expediente que no se revisa | Los hechos cambian | Revisión con disparadores |
| Aclaración leída como contradicción | Dos piezas dicen cosas parecidas | Precisar en ambas |

## 🧪 Práctica

En [`labs/lab-09.md`](../labs/lab-09.md):

1. Ensambla las doce piezas con su evidencia.
2. Cruza las cinco parejas críticas y anota lo que aparece.
3. Prioriza los hallazgos por nivel y clientes afectados.
4. Construye la remediación con su medida provisional.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Leer de principio a fin | Es lo natural | Léelo por parejas |
| Aceptar una política como evidencia | Describe el deber ser | No es evidencia |
| Priorizar por gravedad jurídica | Es lo formal | Prioriza por efecto en el cliente |
| Remediación sin provisional | Se asume corrección rápida | El intervalo expone |
| No avisar entre áreas | Cada una hace lo suyo | El cruce lo detecta tarde |
| Cruzar una sola vez | Se hace para la revisión | Se rehace al cambiar los hechos |

## ❓ Preguntas de comprobación

1. ¿Por qué las contradicciones solo aparecen al cruzar las piezas?
2. ¿Qué cuenta como evidencia y qué no?
3. ¿Con qué criterio se priorizan los hallazgos?
4. ¿Qué elemento falta en casi todos los planes de remediación?
5. En el ejemplo, ¿de dónde venía el primer hallazgo bloqueante?

## 📥 Entregable

Guarda en `portfolio/parte-23/clase-13/`:

- las doce piezas con su evidencia;
- la lectura cruzada de las cinco parejas;
- los hallazgos priorizados por efecto;
- la remediación con sus medidas provisionales.

## 🔗 Referencias cruzadas

- **Viene de:** clases 3, 6 y 12; Parte 22, clase 18.
- **Continúa en:** clases 14 y 18 de esta parte.
- **Se aplica en:** clase 18 de esta parte.

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

- Financial Stability Board (2023). *Global Regulatory Framework for Crypto-asset Activities*. FSB. <https://www.fsb.org/2023/07/fsb-global-regulatory-framework-for-crypto-asset-activities/>
- IOSCO (2023). *Policy Recommendations for Crypto and Digital Asset Markets*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- Basel Committee on Banking Supervision (2015). *Corporate governance principles for banks*. BIS. <https://www.bis.org/bcbs/publ/d328.htm>
- Comisión para el Mercado Financiero. *Normativa aplicable a entidades financieras*. CMF. <https://www.cmfchile.cl/portal/principal/613/w3-channel.html>
- Verificación local: comprueba en la fuente oficial vigente qué exige tu jurisdicción sobre este punto. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 12 · Ciclo de vida y operación diaria](12-ciclo-de-vida-y-operacion-diaria.md) | [Parte 23](../README.md) · [Programa](../../../SYLLABUS.md) | [14 · Modelo de amenazas priorizado →](14-modelo-de-amenazas-priorizado.md) |
<!-- gen:footer:end -->
