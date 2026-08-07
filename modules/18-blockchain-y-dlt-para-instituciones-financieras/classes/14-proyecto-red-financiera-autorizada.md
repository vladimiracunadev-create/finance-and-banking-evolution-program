<!-- meta
part: 19
class: 14
title: "Proyecto: red financiera autorizada"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global]
regulatory_topics: [dlt, gobernanza, riesgo-operacional]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [CPMI, IOSCO]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 14 · Proyecto: red financiera autorizada

> [← 13 · Gobernanza, bifurcaciones y recuperación](13-gobernanza-bifurcaciones-y-recuperacion.md) · [Índice de la parte](../README.md) · [Proyecto de la parte →](../project/README.md)

**Parte 19 — Blockchain y DLT para instituciones financieras** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Integrar las trece clases en un expediente que un comité de riesgo pueda
aprobar o rechazar con fundamento. El proyecto se evalúa por **la comparación con
la alternativa que no usa registro distribuido**, no por lo que se construya.

Esta clase cierra la parte diseñando una red completa. Y con una exigencia que atraviesa las trece anteriores: la comparación con la base de datos centralizada que resolvería lo mismo, medida y no supuesta.

## 📚 Objetivos

Al finalizar podrás:

1. **Construir** el expediente de una red autorizada con sus doce piezas.
2. **Demostrar** con números por qué la alternativa centralizada no sirve, o
   admitir que sirve.
3. **Declarar** los supuestos de seguridad y verificar que se sostienen.
4. **Defender** cada decisión con su alternativa descartada.
5. **Revisar** el proyecto de otra persona con la rúbrica.

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

Los cuatro primeros términos son el entregable y su comparación obligatoria; los cuatro siguientes, lo que lo hace defendible. La **alternativa de referencia** es la exigencia que da valor al proyecto: toda decisión de usar un registro distribuido se compara con la base de datos centralizada que resolvería lo mismo.

| Concepto | Comprensión verificable |
|---|---|
| `expediente` | Conjunto de documentos que sostienen una decisión de arquitectura |
| `alternativa de referencia` | La solución más simple que resolvería el mismo problema |
| `supuesto de seguridad` | Condición sin la cual las garantías no valen |
| `independencia efectiva` | Fallos que no ocurren a la vez, no número de nodos |
| `registro de decisiones` | Cada decisión con alternativa, motivo y consecuencia |
| `límite declarado` | Lo que el trabajo no cubre |
| `plan de salida` | Cómo se deja de usar el sistema sin perder nada |
| `defensa` | Exposición ante quien decide, no ante quien aprende |

## 🧠 Modelo mental

El modelo mental es una pregunta que hay que responder antes de construir: si un solo actor puede operar el registro sin que eso rompa nada, la base centralizada gana en coste, en velocidad y en simplicidad. El registro distribuido se justifica cuando esa condición no se cumple.

```text
UN EXPEDIENTE DE RED AUTORIZADA SE SOSTIENE
SOBRE TRES DEMOSTRACIONES

  1. QUE LA ALTERNATIVA SIMPLE NO SIRVE
     y no basta afirmarlo: hay que medirla

  2. QUE LOS SUPUESTOS DE SEGURIDAD SE SOSTIENEN
     independencia efectiva, no número de nodos

  3. QUE HAY SALIDA
     si el consorcio se disuelve o el banco sale,
     nada queda atrapado

SIN LA PRIMERA, EL PROYECTO ES UNA BASE DE DATOS CARA.
SIN LA SEGUNDA, LAS GARANTÍAS SON DECORATIVAS.
SIN LA TERCERA, ES UNA DEPENDENCIA SIN PRECIO.
```

## 📖 Desarrollo

### 1. Las doce piezas

| # | Pieza | Qué demuestra |
|---:|---|---|
| 1 | Problema y participantes | Que hay un problema real y quién lo tiene |
| 2 | Las seis preguntas de la clase 1 | Que se descartó la alternativa simple |
| 3 | Alternativa de referencia, medida | Que la comparación existe con números |
| 4 | Clasificación por los dos ejes | Que el diseño cumple las obligaciones |
| 5 | Mecanismo de consenso y su `f` | Que el umbral es el correcto |
| 6 | Análisis de independencia efectiva | Que los nodos no fallan a la vez |
| 7 | Política de finalidad y aceptación | Que se sabe cuándo algo es firme |
| 8 | Reparto dentro/fuera del registro | Que la privacidad se decidió al diseñar |
| 9 | Contratos con máquina de estados | Que el código tiene límites |
| 10 | Gobernanza y plan de recuperación | Que se sabe quién decide y qué se hace |
| 11 | Plan de salida | Que la dependencia tiene precio conocido |
| 12 | Límites declarados | Que se sabe qué no se cubrió |

### 2. La demostración que más falta

La pieza que casi ningún expediente trae es la comparación cuantificada con la
alternativa aburrida. El bloque explica qué se considera una medición y qué es
solo una afirmación repetida.

```text
LA PIEZA 3 ES LA QUE CASI NINGÚN PROYECTO TRAE

  «una base de datos compartida no serviría porque
   los participantes no confían»

  ESO NO ES UNA MEDICIÓN. La medición es:
    · coste de construir y operar la alternativa
    · latencia y capacidad de la alternativa
    · qué gobierno tendría
    · a quién habría que confiar exactamente
    · qué pasaría si ese alguien falla
    · y CUÁNTO CUESTA LA DIFERENCIA

  SI LA DIFERENCIA DE COSTE ES X Y EL ÚNICO BENEFICIO
  ES «no confiar en una sociedad conjunta con gobierno
  paritario», hay que poder decir que X vale la pena
```

### 3. Verificar los supuestos

Cada garantía que anuncia el sistema descansa sobre un supuesto, y el trabajo
consiste en verificarlos uno a uno. El bloque presenta la tabla con la que se
hace y advierte de que la última columna es todo el expediente.

```text
CADA GARANTÍA DEL SISTEMA TIENE UN SUPUESTO.
EL EXPEDIENTE LOS LISTA Y LOS VERIFICA.

  garantía          supuesto                  ¿se sostiene?
  ─────────────────────────────────────────────────────────
  no revierte       menos de f defectuosos    ¿independientes?
  nadie controla    ningún participante tiene ¿y el proveedor
  el estado         mayoría                    de software?
  verificable       cada uno ejecuta un nodo  ¿todos pueden?
  irreversible      no hay clave maestra      ¿y la de
                                               actualización?

LA CUARTA COLUMNA ES EL EXPEDIENTE.
Un supuesto que no se verifica es una afirmación.
```

### 4. Qué pregunta un comité

Las preguntas de un comité son siempre las mismas seis, así que conviene
llevarlas contestadas. El bloque las enumera y señala cuáles hunden proyectos
y cuál delata que el equipo ya se autoevaluó.

```text
LAS SEIS PREGUNTAS QUE SIEMPRE LLEGAN

  1. ¿Por qué no una base de datos compartida?
  2. ¿Qué pasa si dos participantes se caen a la vez?
  3. ¿Quién puede cambiar las reglas, y en cuánto tiempo?
  4. Si mañana queremos salir, ¿qué nos llevamos y qué cuesta?
  5. ¿Qué dato personal hay dentro?
  6. ¿Qué parte de esto no habéis probado?

  LA 1 Y LA 4 SON LAS QUE HUNDEN PROYECTOS.
  La 6 es la que distingue a quien ya se la hizo.
```

### 5. Cómo se declara un límite

Declarar un límite bien tiene una forma reconocible, y no es la breve. El
bloque contrapone las dos redacciones sobre el mismo sistema para que se vea
qué información aporta la segunda.

```text
MAL
  «el sistema es seguro»

BIEN
  «el sistema tolera un participante defectuoso.
   No tolera un defecto de la implementación común
   a los cinco, que hemos aceptado como riesgo residual
   porque la diversidad de implementación introduciría
   riesgo de bifurcación. Lo mitigamos con pruebas de
   conformidad, procedimiento de parada coordinada y
   capacidad de revertir a la versión anterior.»

LA SEGUNDA VERSIÓN ES MÁS LARGA Y ES LA ÚNICA
QUE UN COMITÉ PUEDE APROBAR
```

## 🧮 Ejemplo guiado

El ejemplo compara la red diseñada con su alternativa centralizada. Conviene hacer la comparación en coste, plazo y garantías: en muchos casos la alternativa gana.

**Situación.** Revisas el expediente de otra persona antes de que llegue al
comité.

```text
EXTRACTO 1 · justificación
  «los participantes no confían entre sí, por lo que
   una base de datos centralizada no es viable»

EXTRACTO 2 · consenso
  «bizantino, 6 nodos, tolera 1 fallo»

EXTRACTO 3 · privacidad
  «los datos van cifrados en el registro»

EXTRACTO 4 · contratos
  «auditados por una firma externa»

EXTRACTO 5 · gobernanza
  «decisiones por mayoría simple de participantes»

EXTRACTO 6 · salida
  no figura
```

**Paso 1 — evalúa el extracto 1.**

```text
NO HAY MEDICIÓN DE LA ALTERNATIVA

  ¿se preguntó por un tercero NEUTRAL, no por
  un participante? (clase 1, paso 3)
  ¿se calculó el coste de una sociedad conjunta?
  ¿se comparó latencia y capacidad?

HALLAZGO 1 · pieza 3 ausente
  gravedad: máxima
  sin ella, el comité no puede evaluar si el
  sobrecoste está justificado
```

**Paso 2 — evalúa el consenso.**

```text
6 NODOS, «TOLERA 1 FALLO»

  con n = 6:  f = ⌊(6−1)/3⌋ = 1
  el número es correcto

  PERO n = 7 daría f = 2 con un nodo más

HALLAZGO 2 · dimensionamiento subóptimo
  gravedad: media
  con 6 nodos se paga la infraestructura de 6
  y se obtiene la tolerancia de 4

  Y FALTA EL ANÁLISIS DE INDEPENDENCIA (pieza 6):
  no dice quién opera cada nodo ni con qué software
```

**Paso 3 — evalúa la privacidad.**

```text
«LOS DATOS VAN CIFRADOS»

  no dice
    · qué datos entran y cuáles no
    · quién tiene las claves
    · qué pasa con el derecho de supresión
    · qué revelan los metadatos

HALLAZGO 3 · pieza 8 incompleta
  gravedad: alta
  cifrar no resuelve la supresión ni la no vinculabilidad
  (clase 10)
```

**Paso 4 — evalúa los contratos.**

```text
«AUDITADOS POR UNA FIRMA EXTERNA»

  PREGUNTAS
    · ¿qué alcance tuvo la auditoría?
    · ¿se corrigieron todos los hallazgos?
    · ¿hay máquina de estados e invariantes?
    · ¿quién puede actualizar y con qué umbral?
    · ¿hay interruptor de emergencia?

HALLAZGO 4 · pieza 9 sin contenido
  gravedad: alta
  «auditado» no es una propiedad del sistema:
  es un hecho sobre un momento
```

**Paso 5 — evalúa la gobernanza.**

```text
«MAYORÍA SIMPLE DE PARTICIPANTES»

  con 6 participantes, 4 pueden cambiar las reglas

  ¿PUEDEN CAMBIAR LAS REGLAS ECONÓMICAS?
  ¿pueden expulsar a los otros 2?
  ¿hay preaviso?

HALLAZGO 5 · gobernanza sin escalones
  gravedad: alta
  lo esencial exige unanimidad o mayoría reforzada
  (clase 7)
```

**Paso 6 — evalúa la ausencia del extracto 6.**

```text
HALLAZGO 6 · plan de salida inexistente
  gravedad: máxima

  es la pregunta 4 del comité y la que decide
  una evaluación de riesgo de terceros

  sin ella, el banco entra en una dependencia
  cuyo precio de salida nadie conoce
```

**Paso 7 — puntúa y devuelve.**

```text
Problema y alternativa medida    25 %  →  6/25
Consenso e independencia        20 %  →  9/20
Privacidad y reparto            15 %  →  5/15
Contratos y controles           15 %  →  6/15
Gobernanza y recuperación       15 %  →  6/15
Salida y límites                10 %  →  1/10
TOTAL                                   33/100 → NO APRUEBA

DEVOLUCIÓN

  LO QUE ESTÁ BIEN
    · el consenso está bien elegido para el caso
    · hay auditoría externa, que muchos proyectos
      no traen

  LO QUE HAY QUE CORREGIR, EN ORDEN
    1. medir la alternativa de referencia con números
    2. escribir el plan de salida con los cinco puntos
    3. completar el reparto dentro/fuera y la supresión
    4. documentar máquina de estados, invariantes,
       actualización e interruptor
    5. escalonar la gobernanza: unanimidad para lo esencial
    6. analizar la independencia efectiva de los 6 nodos

  OBSERVACIÓN DE CRITERIO
    el expediente describe lo construido y no
    justifica por qué se construyó así. Un comité
    no evalúa una arquitectura: evalúa una decisión.
```

**Interpreta:** el sistema podía estar perfectamente diseñado y el expediente
suspendía porque **no demostraba que hiciera falta**. Las dos piezas de gravedad
máxima —la alternativa medida y el plan de salida— son las que un comité de
riesgo pregunta primero y las que casi nunca están.

## 🧭 Perspectivas

La red diseñada afecta a todos los participantes de las trece clases anteriores. La tabla los reúne.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Autor | Un sistema que funciona | Si justifica o si describe |
| Revisor | Seis hallazgos | Qué puntúa |
| Comité de riesgo | Una dependencia nueva | Si aprueba |
| Tecnología | Una arquitectura elegida | Si la sostiene |
| Cumplimiento | Datos dentro del registro | Si autoriza |
| Auditor | Supuestos no verificados | Qué observa |
| Supervisor | Una infraestructura compartida | Qué exige |

## 🏦 Del cliente al banco

El cliente no distingue la tecnología y sus garantías dependen del diseño. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Mi banco usa blockchain» | Una decisión que hay que justificar | 19, clase 14 |
| «Es más seguro» | Depende de supuestos verificables | 19, clase 14 |
| «Nadie puede cambiarlo» | Depende de la clave de actualización | 19, clases 8 y 14 |

## ⚖️ Riesgos y controles

Los riesgos del proyecto reúnen los de toda la parte. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Alternativa no medida | Se construye lo caro sin comparar | Pieza 3 obligatoria |
| Supuesto no verificado | Las garantías no valen | Tabla de supuestos con verificación |
| Sin plan de salida | Dependencia sin precio | Cinco puntos antes de entrar |
| Gobernanza plana | Una mayoría simple cambia lo esencial | Escalones por tipo de decisión |
| «Auditado» como propiedad | Se confunde un hecho con una garantía | Alcance, hallazgos y correcciones |
| Expediente descriptivo | No se justifica la decisión | Cada decisión con su alternativa |

## 🧪 Práctica

El laboratorio es el proyecto completo. La comparación con la alternativa centralizada es lo que decide su calificación.

En el [proyecto de la parte](../project/README.md):

1. Construye las doce piezas de tu expediente.
2. Mide la alternativa de referencia con números.
3. Verifica cada supuesto de seguridad en su tabla.
4. Revisa el expediente de otra persona con la rúbrica.

## ⚠️ Errores frecuentes

Los síntomas de la tabla aparecen en la defensa. Casi todos se evitan comparando con la alternativa antes de construir.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Justificar con «no confían» | No se preguntó por un tercero neutral | Mide la alternativa |
| Describir en vez de justificar | Se documentó lo construido | Cada decisión con su alternativa |
| Supuestos sin verificar | Se enunciaron las garantías | Tabla con cuarta columna |
| Sin plan de salida | Se pospuso | Es la pregunta 4 del comité |
| «Auditado» sin más | Se citó el hecho | Alcance y hallazgos |
| Gobernanza plana | Se simplificó | Escalones por decisión |

## ❓ Preguntas de comprobación

1. ¿Cuáles son las tres demostraciones que sostienen un expediente?
2. ¿Qué contiene una medición de la alternativa de referencia?
3. ¿Cuál es la cuarta columna de la tabla de supuestos y por qué es la que
   importa?
4. ¿Cuáles son las seis preguntas de un comité y cuáles hunden proyectos?
5. En el ejemplo guiado, ¿por qué un sistema bien diseñado suspendía?

## 📥 Entregable

Guarda en `portfolio/parte-19/clase-14/`:

- las doce piezas del expediente;
- la medición de la alternativa de referencia, con números;
- la tabla de supuestos con su verificación;
- la revisión del expediente de otra persona, con puntuación y devolución.

## 🔗 Referencias cruzadas

- **Viene de:** las trece clases anteriores de esta parte.
- **Continúa en:** Parte 20 (el activo que circula sobre el registro).
- **Se aplica en:** Parte 22, clase 18; Parte 23, clases 11 y 18.

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

- Committee on Payments and Market Infrastructures e IOSCO (2012). *Principles for Financial Market Infrastructures*. BIS. <https://www.bis.org/cpmi/publ/d101.htm>
- Committee on Payments and Market Infrastructures (2017). *Distributed ledger technology in payment, clearing and settlement*. BIS. <https://www.bis.org/cpmi/publ/d157.htm>
- Basel Committee on Banking Supervision (2021). *Principles for operational resilience*. BIS. <https://www.bis.org/bcbs/publ/d516.htm>
- Financial Stability Board (2023). *Enhancing third-party risk management and oversight: a toolkit*. FSB. <https://www.fsb.org/2023/12/enhancing-third-party-risk-management-and-oversight-a-toolkit-for-financial-institutions-and-financial-authorities/>
- NIST (2018). *NISTIR 8202: Blockchain Technology Overview*. NIST. <https://csrc.nist.gov/pubs/ir/8202/final>
- Verificación local: comprueba qué antecedentes exige tu supervisor antes de que una entidad adopte una infraestructura compartida basada en registro distribuido. **Fecha de verificación de esta clase: 2026-08-06.** Esta clase no constituye asesoría legal.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 13 · Gobernanza, bifurcaciones y recuperación](13-gobernanza-bifurcaciones-y-recuperacion.md) | [Parte 19](../README.md) · [Programa](../../../SYLLABUS.md) | [Proyecto de la parte →](../project/README.md) |
<!-- gen:footer:end -->
