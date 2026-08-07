---
part: 23
class: 12
title: "Ciclo de vida y operación diaria"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [operaciones, eventos, continuidad]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [CPMI, BCBS, CMF]
requires_legal_review: false
---

<!-- gen:header:start -->
# Clase 12 · Ciclo de vida y operación diaria

> [← 11 · Pagos y conexión con el exterior](11-pagos-y-conexion-con-el-exterior.md) · [Índice de la parte](../README.md) · [13 · Expediente regulatorio del sistema →](13-expediente-regulatorio-del-sistema.md)

**Parte 23 — Proyecto — banco digital y mercado tokenizado** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Cerrar la construcción con lo que ocurre **todos los días después del
lanzamiento**: eventos, incidencias, conciliaciones y el cierre diario.

Las clases 7 a 11 construyeron los componentes. Esta los pone a funcionar juntos
durante un día completo, y ahí aparecen las contradicciones que ninguna clase
anterior podía mostrar.

## 📚 Objetivos

Al finalizar podrás:

1. **Diseñar** el ciclo diario con sus hitos y sus cortes.
2. **Clasificar** los eventos en programables, con dato externo y no programables.
3. **Implementar** el pago de intereses con verificación previa.
4. **Especificar** la función de inmovilización y su gobierno.
5. **Identificar** las tensiones de diseño que aparecen al integrar.

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
| `ciclo diario` | Secuencia de hitos de una jornada operativa |
| `corte` | Momento que separa un día del siguiente |
| `evento programable` | El que depende solo del calendario |
| `evento no programable` | El que viene de fuera del sistema |
| `inmovilización` | Congelar el saldo de un titular por orden |
| `aprovisionamiento` | Fondos disponibles antes de pagar |
| `tensión de diseño` | Contradicción entre dos decisiones correctas |
| `cierre diario` | Conciliación y cuadre de la jornada |

## 🧠 Modelo mental

La emisión se prueba y el ciclo de vida se improvisa. Es el patrón que rompe más
proyectos, y la causa es que el día uno se diseña con cuidado y el día
doscientos no se diseña.

```text
EL DÍA COMPLETO

  apertura      saldos, conciliación de la
                víspera, aprovisionamiento
  jornada       operaciones, alertas,
                llamadas de margen
  corte         fin de la ventana de
                liquidación
  cierre        conciliación a tres bandas,
                cuadre, reporte

Y ENTRE EL CORTE Y LA APERTURA
  las operaciones se encolan y se ejecutan
  al abrir, y hay que decírselo al cliente
```

## 📖 Desarrollo

### 1. Las tres familias de eventos

Solo la primera se puede automatizar por completo. La tercera —embargos,
órdenes judiciales, sucesiones— exige una vía humana con autorización, y es la
que más se olvida en el diseño.

```text
PROGRAMABLES         calendario conocido
CON DATO EXTERNO     exigen un oráculo, y
                     con él sus problemas
NO PROGRAMABLES      vienen de fuera del
                     sistema

Y PARA LA TERCERA SE DISEÑA UNA FUNCIÓN
QUE SOLO INMOVILIZA
  no transfiere, no altera saldos, y exige
  doble aprobación y registro inmutable
```

### 2. Verificar antes de pagar

Un proceso que paga por orden hasta quedarse sin fondos divide a los clientes en
dos grupos sin ningún criterio. La verificación previa convierte un fallo
irrecuperable en uno recuperable.

```text
LA REGLA

  si el aprovisionamiento no alcanza para
  todos, no se paga a nadie y se alerta

Y ES LA MISMA REGLA DE LA COLA DE
REDENCIÓN: el orden de llegada no reparte,
discrimina
```

### 3. Las tensiones que aparecen al integrar

Aquí está el contenido específico de esta clase. Cada decisión anterior era
correcta por separado y algunas se contradicen al funcionar juntas.

```text
TENSIONES HABITUALES

  atomicidad ↔ coste de liquidez
  horario ampliado ↔ saldo de reserva
  mínimo bajo ↔ rentabilidad del cliente
  conciliación frecuente ↔ coste operativo
  lista blanca con espera ↔ agilidad

CADA UNA SE RESUELVE ELIGIENDO,
y lo que el expediente exige es que la
elección esté cuantificada y declarada
```

## 🧮 Ejemplo guiado

**Situación.** El equipo simula un día completo y encuentra tres tensiones.

```text
JORNADA SIMULADA
  operaciones                        420
  llamadas de margen                   6
  pago de intereses del mes           sí
  una orden judicial recibida         sí
  un corte de red de 40 minutos       sí
```

**Paso 1 — ejecuta el pago de intereses.**

```text
necesario                       84 000
aprovisionado                   82 500

  FALTAN 1 500
  → NO SE PAGA A NADIE y se alerta

  tras aprovisionar
  pagados 412 de 420 titulares
  8 con cuenta bloqueada, al reintento
```

**Paso 2 — aplica la orden judicial.**

```text
FUNCIÓN DE INMOVILIZACIÓN

  · activada por la dirección de operaciones
  · doble aprobación
  · solo inmoviliza: no transfiere
  · registro inmutable del quién, cuándo
    y en virtud de qué

Y EL DERECHO AL INTERÉS DEVENGADO
  subsiste: se consigna a disposición
  de la autoridad, no se anula
```

**Paso 3 — resuelve el corte de red.**

```text
40 MINUTOS SIN CONEXIÓN AL BANCO EMISOR

  · las liquidaciones se encolan
  · el registro sigue aceptando operaciones
    que no exigen movimiento de dinero
  · al restablecerse, la cola se ejecuta
    en orden

TENSIÓN 1
  la tolerancia declarada para liquidación
  era de 2 horas → se cumplió
  pero la de llamadas de margen era de
  30 minutos → NO se cumplió

  → hay que revisar la tolerancia del
    margen o el diseño de la cola
```

**Paso 4 — anota las tres tensiones.**

```text
TENSIÓN 1 · tolerancia de margen
  30 minutos es incompatible con una cola
  que espera al banco emisor
  RESOLUCIÓN: subir a 2 horas y ampliar el
  plazo de aportación en la misma medida

TENSIÓN 2 · lista blanca con espera
  la espera de 48 h impide atender una
  urgencia legítima
  RESOLUCIÓN: vía de excepción con doble
  aprobación y registro, revisada mensualmente

TENSIÓN 3 · conciliación diaria
  cuesta 26 000 al año y el volumen no lo
  exigiría todavía
  RESOLUCIÓN: se mantiene diaria porque el
  saldo de liquidación sí se mueve a diario,
  y se declara que el coste es del componente
  de dinero, no del de colateral
```

**Interpreta:** El día completo reveló tres tensiones entre decisiones que eran correctas por
separado. **La más incómoda fue la primera**: una tolerancia de 30 minutos para
las llamadas de margen era incompatible con una cola que depende de un tercero, y
la resolución exigió cambiar un parámetro de riesgo que ya estaba aprobado.

## 🧭 Perspectivas

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un interés que no llega | Si reclama |
| Prestatario | Una llamada de margen tardía | Si puede aportar |
| Operaciones | Una cola de 40 minutos | Cómo la comunica |
| Riesgos | Una tolerancia incumplida | Si la revisa |
| Banco emisor | Una conexión caída | Qué informa |
| Supervisor | Tres tensiones declaradas | Qué observa |
| Auditor | Aprovisionamiento verificado | Qué comprueba |
| Sociedad | Un sistema que reconoce sus límites | — |

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «No llegó el interés» | No se pagó a nadie: faltaban 1 500 | 23, clase 12 |
| «Me bloquearon la cuenta» | Orden judicial, con doble aprobación | 23, clase 12 |
| «Tardó 40 minutos» | La cola se ejecutó al restablecerse | 23, clase 12 |

## ⚖️ Riesgos y controles

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Diseñar solo el día uno | Es lo que se prueba | El día doscientos es el que rompe |
| Pagar sin verificar | El proceso «ya paga» | Verificar antes de empezar |
| Programar el embargo | Se busca automatizar todo | Solo se diseña la inmovilización |
| Tolerancias incompatibles | Se fijaron por separado | Probarlas en un día completo |
| Controles sin vía de excepción | Se confía en la regla | El mundo real no cabe en la regla |
| Tensiones no declaradas | Se resuelven en silencio | El expediente exige declararlas |

## 🧪 Práctica

En [`labs/lab-06.md`](../labs/lab-06.md):

1. Diseña el ciclo diario con sus hitos y su corte.
2. Ejecuta el pago de intereses con aprovisionamiento insuficiente.
3. Aplica una orden judicial con la función de inmovilización.
4. Identifica y cuantifica las tensiones de diseño.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Probar solo el lanzamiento | Es el hito visible | El ciclo diario rompe proyectos |
| Pagar por orden | Es lo que hace el bucle | Discrimina sin criterio |
| Automatizar lo no programable | Se busca cubrir todo | Vía humana con autorización |
| Tolerancias sin probar juntas | Cada área fija la suya | Un día completo las contrasta |
| Resolver tensiones en silencio | Parece un detalle | Se declaran en el expediente |
| Sin comunicación al cliente | La cola se resuelve sola | Hay que decírselo |

## ❓ Preguntas de comprobación

1. ¿Cuáles son los hitos de un ciclo diario y qué ocurre entre el corte y la apertura?
2. ¿Cuáles son las tres familias de eventos y cuál se olvida?
3. ¿Por qué hay que verificar el aprovisionamiento antes de pagar?
4. ¿Qué es una tensión de diseño y por qué solo aparece al integrar?
5. En el ejemplo, ¿cuál fue la tensión más incómoda y por qué?

## 📥 Entregable

Guarda en `portfolio/parte-23/clase-12/`:

- el ciclo diario con sus hitos;
- el pago de intereses con su verificación previa;
- la función de inmovilización con su gobierno;
- las tres tensiones con su cuantificación y su resolución.

## 🔗 Referencias cruzadas

- **Viene de:** clases 8, 10 y 11; Parte 21, clase 5.
- **Continúa en:** clase 13 de esta parte.
- **Se aplica en:** clases 15 y 18 de esta parte.

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
- Basel Committee on Banking Supervision (2021). *Principles for Operational Resilience*. BIS. <https://www.bis.org/bcbs/publ/d516.htm>
- Basel Committee on Banking Supervision (2015). *Corporate governance principles for banks*. BIS. <https://www.bis.org/bcbs/publ/d328.htm>
- Comisión para el Mercado Financiero. *Normativa aplicable a entidades financieras*. CMF. <https://www.cmfchile.cl/portal/principal/613/w3-channel.html>
- Verificación local: comprueba en la fuente oficial vigente qué exige tu jurisdicción sobre este punto. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 11 · Pagos y conexión con el exterior](11-pagos-y-conexion-con-el-exterior.md) | [Parte 23](../README.md) · [Programa](../../../SYLLABUS.md) | [13 · Expediente regulatorio del sistema →](13-expediente-regulatorio-del-sistema.md) |
<!-- gen:footer:end -->
