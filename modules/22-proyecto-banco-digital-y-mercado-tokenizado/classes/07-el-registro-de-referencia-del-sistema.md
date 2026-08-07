<!-- meta
part: 23
class: 7
title: "El registro de referencia del sistema"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [registro-de-referencia, conciliacion, atomicidad]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [CPMI, IOSCO, CMF]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 07 · El registro de referencia del sistema

> [← 06 · Decisión de producto: qué se ofrece](06-decision-de-producto-que-se-ofrece.md) · [Índice de la parte](../README.md) · [08 · Interfaces, consentimiento y terceros →](08-interfaces-consentimiento-y-terceros.md)

**Parte 23 — Proyecto — banco digital y mercado tokenizado** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Determinar, para cada dato que el sistema guarda, **cuál es el registro que
manda** cuando dos fuentes discrepan, y diseñar el procedimiento para cuando
ocurra.

Las clases 4 y 5 decidieron la arquitectura y el dinero. Esta abre el bloque de
construcción resolviendo la tercera decisión previa, que es la que determina si
la conciliación será un proceso permanente o una transición puntual.

## 📚 Objetivos

Al finalizar podrás:

1. **Determinar** el registro de referencia de cada dato del sistema.
2. **Diseñar** el procedimiento de divergencia en cuatro tiempos.
3. **Calcular** la ventana de conciliación que protege.
4. **Demostrar** que la atomicidad es alcanzable en el componente que la promete.
5. **Designar** la autoridad de resolución antes de operar.

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

Los cuatro primeros términos son el registro y su divergencia; los cuatro siguientes, los mecanismos que la resuelven. La **conciliación a tres bandas** es la que exige este sistema: hay tres registros —el propio, el del custodio y el del banco emisor— y conciliar dos de ellos no basta.

| Concepto | Comprensión verificable |
|---|---|
| `registro de referencia` | Aquel cuya versión prevalece |
| `espejo` | Representación que sigue a otro registro |
| `bloqueo de origen` | Inmovilizar en uno para representar en otro |
| `ventana de divergencia` | Tiempo hasta detectar una diferencia |
| `conciliación a tres bandas` | Comparación simultánea de tres registros |
| `autoridad de resolución` | Quien decide qué versión es correcta |
| `congelación simultánea` | Suspender en todos los registros a la vez |
| `compensación` | Resarcir en vez de revertir |

## 🧠 Modelo mental

El sistema de este proyecto tiene al menos tres registros: el propio, el del
custodio del colateral y el del banco que emite el depósito tokenizado. Cada dato
vive en uno o en varios, y para cada uno hay que decidir cuál manda.

```text
LA PREGUNTA, DATO A DATO

  saldo de la cuenta        → el propio
  colateral pignorado       → ¿el nuestro o
                              el del custodio?
  saldo de liquidación      → el del banco
  posición del cliente      → el propio

Y LA REGLA QUE EVITA LA CONCILIACIÓN
PERMANENTE
  bloqueo de origen: mientras el colateral
  está pignorado, solo nuestro registro lo
  mueve; el custodio lo tiene inmovilizado
```

## 📖 Desarrollo

### 1. Las seis causas de divergencia

Dos vienen de fuera del sistema y ninguna automatización las cubre. Por eso hay
que designar una autoridad de resolución antes de operar, no cuando llegue el
primer embargo.

```text
DENTRO DEL SISTEMA
  fallo de propagación · orden distinto
  error operativo · ataque

FUERA
  evento corporativo · decisión judicial

Y LAS DOS DE FUERA SON LAS QUE OBLIGAN
A TENER UN PROCEDIMIENTO HUMANO
```

### 2. La ventana que protege

Una conciliación cuya ventana es mayor que el intervalo entre dos operaciones del
mismo saldo no protege: documenta el daño. El cálculo es simple y casi nunca se
hace.

```text
LA REGLA

  ventana < intervalo entre dos operaciones
            del mismo saldo

Y EL INTERVALO SE CALCULA CON LA
DISTRIBUCIÓN REAL, no con la media:
el cliente más activo marca el requisito
```

### 3. Demostrar la atomicidad

La clase 5 concluyó que es alcanzable. Aquí hay que demostrarlo, y la
demostración no es una medición de velocidad: es una prueba de que no existe un
estado observable con un tramo movido y el otro no.

```text
CÓMO SE DEMUESTRA

  · el liquidador expone el estado completo
  · una prueba lo observa antes y después
  · y comprueba que no hay estado a medias
  · más una prueba por cada tramo que falla

Y EL DISEÑO QUE LO PERMITE
  rechazar antes de bloquear, porque una
  reversión demuestra que hubo un estado
  intermedio
```

## 🧮 Ejemplo guiado

El ejemplo decide el registro de referencia de cada dato y calcula la ventana con la distribución real. Conviene usar el cliente más activo y no la media.

**Situación.** El equipo determina el registro de referencia de cada dato y
calcula la ventana de conciliación.

```text
REGISTROS DEL SISTEMA
  A  el propio: cuentas, posiciones, colateral
  B  el del custodio: activos pignorados
  C  el del banco: saldo de liquidación

DATOS
  clientes                          2 400
  operaciones de colateral al mes     380
  el 5 % más activo hace el 55 %
```

**Paso 1 — determina el registro de cada dato.**

```text
saldo de cuenta          A, sin discusión
colateral pignorado      A mientras está
                         pignorado, B fuera
saldo de liquidación     C, y A lo refleja
posición del cliente     A

  CON BLOQUEO DE ORIGEN EN EL COLATERAL
  no hay dos versiones activas del mismo
  dato en ningún momento
```

**Paso 2 — calcula la ventana.**

```text
OPERACIONES DE COLATERAL
  380 al mes · el 5 % más activo (120
  clientes) hace 209

  1,74 operaciones por cliente activo y mes
  → una cada 17 días

  PERO LA DISTRIBUCIÓN NO ES UNIFORME
  supuesto: el cliente más activo opera
  3 veces al mes → una cada 10 días

  CONCILIACIÓN DIARIA basta con holgura
  → y se elige diaria por el saldo de
    liquidación, que sí se mueve a diario
```

**Paso 3 — diseña el procedimiento.**

```text
1 DETECCIÓN
    conciliación diaria a tres bandas,
    sobre todos los saldos

2 CONGELACIÓN
    simultánea en A, y comunicación a B y C
    para que congelen

3 RESOLUCIÓN
    la dirección de operaciones, con doble
    aprobación, en un plazo máximo de
    2 días hábiles

4 REPARACIÓN
    se corrige el registro erróneo y se
    compensa al perjudicado; nunca se
    revierte el correcto
```

**Paso 4 — demuestra la atomicidad.**

```text
COMPONENTE: liquidación del colateral
contra el depósito tokenizado

  ambos tramos en el registro A
  → la atomicidad es alcanzable

PRUEBAS EXIGIDAS
  · no existe estado intermedio observable
  · fallo del tramo de colateral deja el
    dinero intacto
  · fallo del tramo de dinero deja el
    colateral intacto
  · dos operaciones sobre el mismo saldo
    no se ejecutan ambas

Y UNA QUE SE OLVIDA
  · con el registro detenido, la operación
    se rechaza sin tocar nada
```

**Interpreta:** El bloqueo de origen eliminó la divergencia estructural del colateral, y la
ventana de conciliación quedó determinada **no por el dato más frecuente sino por
el cliente más activo**. La atomicidad se demostró con cinco pruebas, y la quinta
—el registro detenido— es la que casi nunca se escribe.

## 🧭 Perspectivas

El registro de referencia afecta a cada actor de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un saldo que cuadra | — |
| Equipo | Tres registros que coordinar | Cuál manda en cada dato |
| Custodio | Colateral inmovilizado | Cómo lo refleja |
| Banco | Saldo de liquidación | Cómo concilia |
| Operaciones | Una divergencia que resolver | En qué plazo |
| Supervisor | Autoridad designada | Qué verifica |
| Auditor | Conciliación a tres bandas | Qué muestrea |
| Juzgado | Una orden que ejecutar | Sobre qué registro |

## 🏦 Del cliente al banco

El cliente ve un saldo y el sistema sabe cuál de los tres registros manda en él. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «El saldo es el que veo» | Puede estar en conciliación | 23, clase 7 |
| «Es instantáneo» | Y atómico, con cinco pruebas | 23, clase 7 |
| «Nunca hay diferencias» | Hay procedimiento por si las hay | 23, clase 7 |

## ⚖️ Riesgos y controles

Los riesgos son de divergencia y de autoridad de resolución no definida. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Registro de referencia sin decidir | Lo decide un tribunal | Decidirlo dato a dato |
| Conciliación dos a dos | Una diferencia se oculta | A tres bandas |
| Ventana por la media | El cliente activo la incumple | Calcular con el más activo |
| Congelar un solo registro | La diferencia crece | Congelación simultánea |
| Revertir el correcto | Parece la corrección natural | Compensar al perjudicado |
| Atomicidad sin probar el sistema detenido | No se piensa | Es la quinta prueba |

## 🧪 Práctica

El laboratorio pide decidir el registro de referencia por dato y calcular la ventana. El bloqueo de origen es la corrección que se evalúa.

En [`labs/lab-03.md`](../labs/lab-03.md):

1. Determina el registro de referencia de cada dato del sistema.
2. Calcula la ventana con la distribución real, no con la media.
3. Diseña el procedimiento en cuatro tiempos con su autoridad.
4. Ejecuta las cinco pruebas de atomicidad.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen divergencias entre registros. La causa es la ventana calculada con la media.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Un registro de referencia para todo | Simplifica | Se decide dato a dato |
| Conciliar dos a dos | Es lo natural | Oculta diferencias |
| Ventana por la media | Es el cálculo fácil | Decide el más activo |
| Sin autoridad designada | Se resolverá cuando pase | Sin ella no se resuelve |
| Probar solo el camino feliz | Es lo que funciona | Cada fallo con su prueba |
| Olvidar el sistema detenido | No se contempla | Es un modo de fallo real |

## ❓ Preguntas de comprobación

1. ¿Por qué el registro de referencia se decide dato a dato?
2. ¿Qué elimina el bloqueo de origen y qué no elimina?
3. ¿Cómo se calcula la ventana de conciliación que protege?
4. ¿Cuáles son los cuatro tiempos del procedimiento de divergencia?
5. ¿Cuáles son las cinco pruebas de atomicidad y cuál se olvida?

## 📥 Entregable

Guarda en `portfolio/parte-23/clase-07/`:

- el registro de referencia de cada dato;
- el cálculo de la ventana con la distribución real;
- el procedimiento en cuatro tiempos con su autoridad designada;
- las cinco pruebas de atomicidad ejecutadas.

## 🔗 Referencias cruzadas

- **Viene de:** clases 4 y 5; Parte 21, clases 2 y 8.
- **Continúa en:** clases 9 y 10 de esta parte.
- **Se aplica en:** clases 12 y 15 de esta parte.

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
- IOSCO (2023). *Policy Recommendations for Crypto and Digital Asset Markets*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- Comisión para el Mercado Financiero. *Normativa aplicable a entidades financieras*. CMF. <https://www.cmfchile.cl/portal/principal/613/w3-channel.html>
- Verificación local: comprueba en la fuente oficial vigente qué exige tu jurisdicción sobre este punto. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 06 · Decisión de producto: qué se ofrece](06-decision-de-producto-que-se-ofrece.md) | [Parte 23](../README.md) · [Programa](../../../SYLLABUS.md) | [08 · Interfaces, consentimiento y terceros →](08-interfaces-consentimiento-y-terceros.md) |
<!-- gen:footer:end -->
