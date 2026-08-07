---
part: 23
class: 16
title: "Resolución ordenada y salida"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [resolucion, continuidad, proteccion-al-cliente]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [FSB, CPMI, CMF]
requires_legal_review: true
---

<!-- gen:header:start -->
# Clase 16 · Resolución ordenada y salida

> [← 15 · Escenario de tensión y continuidad](15-escenario-de-tension-y-continuidad.md) · [Índice de la parte](../README.md) · [17 · Lo que el sistema no puede hacer →](17-lo-que-el-sistema-no-puede-hacer.md)

**Parte 23 — Proyecto — banco digital y mercado tokenizado** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Diseñar qué ocurre si el sistema **deja de operar**: quién asume las posiciones,
en qué plazo y qué recupera cada cliente.

La clase 15 midió dónde se rompe el sistema bajo tensión. Esta responde la
pregunta siguiente y más incómoda: qué pasa si no se recupera. Es la parte del
diseño que nadie quiere escribir y la primera que un supervisor lee.

## 📚 Objetivos

Al finalizar podrás:

1. **Diseñar** el plan de resolución con sus seis elementos.
2. **Determinar** qué recupera cada tipo de cliente y en qué plazo.
3. **Identificar** las funciones que deben seguir prestándose durante la salida.
4. **Probar** el traspaso a una entidad receptora.
5. **Redactar** la comunicación a los clientes.

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
| `resolución ordenada` | Cese sin daño desproporcionado al cliente |
| `entidad receptora` | Quien asume las posiciones |
| `función crítica` | La que debe seguir prestándose |
| `copia del registro` | En poder de un tercero, diaria |
| `prelación` | Orden de cobro de los acreedores |
| `plazo de traspaso` | Tiempo máximo de la transición |
| `comunicación` | Qué se dice a los clientes y cuándo |
| `prueba de traspaso` | Ejecución real sobre un subconjunto |

## 🧠 Modelo mental

Un plan de resolución escrito por quien tendría que ejecutarlo estando en
dificultades no sirve. Los tres elementos que lo hacen ejecutable son externos:
la entidad receptora, la copia del registro y el ejecutor.

```text
LOS SEIS ELEMENTOS

  1 ENTIDAD RECEPTORA identificada por contrato
  2 COPIA DEL REGISTRO diaria, en un tercero
  3 PLAZO MÁXIMO de traspaso
  4 QUIÉN PAGA el traslado
  5 QUÉ PASA con los eventos en transición
  6 COMUNICACIÓN a los clientes, con plazo

Y UNA PRUEBA
  traspasar un subconjunto real, al menos
  una vez al año
```

## 📖 Desarrollo

### 1. Qué recupera cada cliente

La respuesta depende de la calificación de lo que tenga y de si la segregación
está acreditada. Y hay que poder responderla por tipo de cliente, no en
general.

```text
POR TIPO DE POSICIÓN

  saldo en cuenta        depende de la
                         salvaguarda
  colateral pignorado    depende de la
                         segregación del custodio
  crédito vivo           se cede a la receptora
  operación pendiente    se liquida o se cancela

Y PARA CADA UNA: cuánto, de quién y cuándo
```

### 2. Las funciones que no pueden parar

Algunas funciones deben seguir prestándose durante la transición aunque la
entidad esté cesando, porque su interrupción causa un daño que el cese no
justifica.

```text
SUELEN SER

  acceso del cliente a su saldo
  liquidación de operaciones ya casadas
  atención de reclamos
  reporte al supervisor

Y ESO EXIGE FINANCIACIÓN DURANTE LA
TRANSICIÓN, que hay que prever antes
```

### 3. La comunicación

Una comunicación tardía o ambigua convierte un cese ordenado en una corrida. El
plazo y el contenido se deciden antes, no en el momento.

```text
QUÉ SE DICE

  · qué ha ocurrido, sin eufemismos
  · qué pasa con su dinero y su posición
  · qué tiene que hacer él, si algo
  · en qué plazo
  · y a quién preguntar

EN 24 HORAS DESDE LA DECISIÓN,
y por los mismos canales por los que opera
```

## 🧮 Ejemplo guiado

**Situación.** El equipo diseña el plan de resolución y lo prueba con un
subconjunto de clientes.

```text
POSICIONES
  saldos en cuenta             91 200 000
  colateral pignorado          24 000 000
  crédito vivo                 16 800 000
  clientes                          2 400
```

**Paso 1 — determina qué recupera cada uno.**

```text
SALDOS EN CUENTA
  con salvaguarda acreditada y renuncia
  a compensar → 100 %, en 30 días

COLATERAL PIGNORADO
  custodiado por un tercero con las tres
  cláusulas → 100 %, tras cancelar el crédito

CRÉDITO VIVO
  se cede a la receptora con sus condiciones
  → el cliente no cambia de condiciones

OPERACIONES PENDIENTES
  las casadas se liquidan; las no casadas
  se cancelan y se comunica
```

**Paso 2 — designa a la receptora y prueba.**

```text
RECEPTORA
  entidad autorizada con acuerdo marco
  firmado y revisión anual

PRUEBA EJECUTADA
  traspaso de 40 clientes reales, con su
  consentimiento, en entorno de producción

  plazo real medido: 6 días hábiles
  incidencias: 3, todas de formato

  → el plazo máximo declarado de 20 días
    tiene holgura
```

**Paso 3 — define las funciones que no paran.**

```text
DURANTE LA TRANSICIÓN SIGUEN

  · consulta de saldo
  · liquidación de lo ya casado
  · atención de reclamos
  · reporte al supervisor

FINANCIACIÓN
  supuesto 90 000 para 20 días
  provisionados en un fondo de transición
  dotado desde el inicio

  → 1 500 al mes durante cinco años
```

**Paso 4 — redacta la comunicación.**

```text
BORRADOR APROBADO PREVIAMENTE

  «Hemos comunicado a la autoridad el cese
   de nuestra actividad. Tu saldo está en
   una cuenta separada de nuestro patrimonio
   y se te devolverá íntegro en un plazo
   máximo de 30 días. Tu crédito pasa a X
   sin cambio de condiciones. No tienes que
   hacer nada; te escribiremos cuando el
   traspaso esté hecho. Para preguntas: ...»

  SE ENVÍA EN 24 HORAS
  y está escrito antes de que haga falta
```

**Interpreta:** La prueba de traspaso con 40 clientes reales midió 6 días frente a los 20
declarados, y encontró tres incidencias de formato que en una ejecución real
habrían costado semanas. **El plan valía porque se había ejecutado**, no porque
estuviera bien redactado.

## 🧭 Perspectivas

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Su dinero en un cese | Si confía en el plazo |
| Prestatario | Su crédito cedido | Si cambian condiciones |
| Equipo | Un plan que ejecutar | Si lo prueba |
| Receptora | 40 clientes de prueba | Si acepta el acuerdo |
| Custodio | Colateral que devolver | Cómo lo libera |
| Supervisor | Un plan probado | Qué autoriza |
| Auditor | Fondo de transición | Qué verifica |
| Sociedad | Un cese sin daño | Qué exige |

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «¿Y si cierran?» | 30 días y el 100 %, acreditado | 23, clase 16 |
| «Tienen un plan» | Probado con 40 clientes reales | 23, clase 16 |
| «Me avisarán» | En 24 horas, con texto ya escrito | 23, clase 16 |

## ⚖️ Riesgos y controles

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Plan ejecutado por quien cesa | No podrá hacerlo | Ejecutor y receptora externos |
| Sin copia del registro | Depende del que falla | Copia diaria en un tercero |
| Plan sin probar | No funciona cuando hace falta | Traspaso real de un subconjunto |
| Funciones que paran | Daño desproporcionado | Financiación de la transición |
| Comunicación improvisada | Convierte el cese en corrida | Texto aprobado de antemano |
| Sin fondo de transición | No hay con qué operar | Dotarlo desde el inicio |

## 🧪 Práctica

En [`labs/lab-09.md`](../labs/lab-09.md):

1. Determina qué recupera cada tipo de posición y en qué plazo.
2. Designa la receptora y prueba el traspaso con un subconjunto.
3. Define las funciones que no pueden parar y su financiación.
4. Redacta la comunicación y apruébala antes de necesitarla.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Escribir el plan y archivarlo | Cumple el requisito | Pruébalo |
| Ejecutor interno | Es quien conoce el sistema | Estará en dificultades |
| Plazo sin medir | Se estima | Mídelo con una prueba |
| Todas las funciones paran | Simplifica | Algunas causan daño desproporcionado |
| Comunicar cuando ocurra | Se improvisa | El texto va escrito antes |
| Sin fondo | Se financiará entonces | Entonces no hay con qué |

## ❓ Preguntas de comprobación

1. ¿Cuáles son los seis elementos de un plan de resolución?
2. ¿Por qué el ejecutor y la receptora tienen que ser externos?
3. ¿Qué funciones deben seguir prestándose durante la transición?
4. ¿Qué debe decir la comunicación y en qué plazo?
5. En el ejemplo, ¿qué demostró la prueba con 40 clientes?

## 📥 Entregable

Guarda en `portfolio/parte-23/clase-16/`:

- qué recupera cada tipo de posición, con su plazo;
- la receptora designada y la prueba de traspaso ejecutada;
- las funciones que no paran y su financiación;
- la comunicación redactada y aprobada.

## 🔗 Referencias cruzadas

- **Viene de:** clases 9 y 15; Parte 21, clase 9; Parte 22, clase 10.
- **Continúa en:** clases 17 y 18 de esta parte.
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

- Financial Stability Board (2014). *Key Attributes of Effective Resolution Regimes*. FSB. <https://www.fsb.org/2014/10/r_141015/>
- CPMI e IOSCO (2012). *Principles for Financial Market Infrastructures*. BIS. <https://www.bis.org/cpmi/publ/d101.htm>
- Basel Committee on Banking Supervision (2021). *Principles for Operational Resilience*. BIS. <https://www.bis.org/bcbs/publ/d516.htm>
- Comisión para el Mercado Financiero. *Normativa aplicable a entidades financieras*. CMF. <https://www.cmfchile.cl/portal/principal/613/w3-channel.html>
- Verificación local: comprueba en la fuente oficial vigente qué exige tu jurisdicción sobre este punto. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 15 · Escenario de tensión y continuidad](15-escenario-de-tension-y-continuidad.md) | [Parte 23](../README.md) · [Programa](../../../SYLLABUS.md) | [17 · Lo que el sistema no puede hacer →](17-lo-que-el-sistema-no-puede-hacer.md) |
<!-- gen:footer:end -->
