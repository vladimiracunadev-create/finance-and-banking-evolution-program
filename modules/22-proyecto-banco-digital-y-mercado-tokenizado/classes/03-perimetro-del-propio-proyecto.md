<!-- meta
part: 23
class: 3
title: "Perímetro del propio proyecto"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [chile, internacional]
regulatory_topics: [perimetro, autorizacion, cumplimiento]
regulation_last_verified: 2026-08-20
regulatory_status: vigente
primary_authorities: [CMF, FSB, IOSCO]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 03 · Perímetro del propio proyecto

> [← 02 · Construir, integrar o comprar](02-construir-integrar-o-comprar.md) · [Índice de la parte](../README.md) · [04 · Decisión de arquitectura: ¿hace falta un registro? →](04-decision-de-arquitectura-registro.md)

**Parte 23 — Proyecto — banco digital y mercado tokenizado** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Aplicar al propio proyecto el método de la Parte 22: determinar qué actividades
ejerce **por sus hechos**, no por lo que el equipo cree estar construyendo.

La clase 2 decidió qué se construye y qué se integra. Esa decisión no cambia el
perímetro: integrar una función de un tercero no la saca del régimen si la
entidad es quien se relaciona con el cliente. Aquí se comprueba.

## 📚 Objetivos

Al finalizar podrás:

1. **Aplicar** las seis preguntas del perímetro al diseño propio.
2. **Identificar** los regímenes que el diseño activa sin querer.
3. **Determinar** qué actividades quedan en la entidad al integrar de terceros.
4. **Estimar** la carga regulatoria del perímetro resultante.
5. **Ajustar** el diseño para no activar regímenes que no aportan.

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

Los cuatro primeros términos son el perímetro efectivo y sus accesorios; los cuatro siguientes, la carga y su corrección. El **hecho de diseño** es el concepto propio de esta clase: una línea de arquitectura activa un régimen, y por eso el perímetro se determina antes de escribirla y no después.

| Concepto | Comprensión verificable |
|---|---|
| `perímetro efectivo` | El que activan los hechos del diseño |
| `régimen accesorio` | El que activa una función secundaria |
| `actividad delegada` | Ejecutada por un tercero, responsabilidad propia |
| `carga incremental` | Coste de añadir un régimen más |
| `ajuste de diseño` | Cambio que evita activar un régimen |
| `autorización adicional` | La que exige una función concreta |
| `hecho de diseño` | Decisión técnica con consecuencia regulatoria |
| `revisión de perímetro` | Comprobación periódica al cambiar el diseño |

## 🧠 Modelo mental

El perímetro no se decide: se descubre. Un equipo puede creer que construye una
billetera y estar construyendo un banco, y la diferencia la marcan decisiones de
diseño que parecen técnicas.

```text
HECHOS DE DISEÑO CON CONSECUENCIA

  «el saldo queda en nuestra cuenta»    captación
  «guardamos las claves»                custodia
  «casamos órdenes entre clientes»      mercado
  «ordenamos las opciones en pantalla»  asesoría
  «convertimos con margen propio»       cambio
  «adelantamos contra el saldo»         crédito

CADA UNA ES UNA LÍNEA DE CÓDIGO
Y UN RÉGIMEN.

Y la pregunta útil en esta fase no es
«¿qué régimen nos aplica?» sino
«¿qué decisión de diseño lo activó,
y podemos tomar otra?»
```

## 📖 Desarrollo

### 1. Integrar no saca del perímetro

Es la confusión más frecuente al llegar aquí desde la clase 2. Si el cliente
contrata con la entidad, la entidad ejerce la actividad aunque la ejecute un
tercero.

```text
QUIÉN EJERCE LA ACTIVIDAD

  el que se relaciona con el cliente
  y responde ante él

  · si el proveedor es invisible para el
    cliente, la actividad es de la entidad
  · si el cliente contrata directamente
    con el proveedor, es de él, y entonces
    la entidad solo intermedia

Y ESO ÚLTIMO TAMBIÉN ES UNA ACTIVIDAD
```

### 2. Ajustar el diseño para no activar

La consecuencia útil de determinar el perímetro pronto es que todavía se puede
cambiar el diseño. Un régimen que no aporta nada al cliente y cuesta 200 000 al
año se evita cambiando una decisión técnica.

```text
EJEMPLOS DE AJUSTE

  ordenar por criterio objetivo publicado
  en vez de destacar
    → evita el régimen de asesoría

  liquidar el cambio contra un tercero
  autorizado en vez de con margen propio
    → evita el régimen de cambio

  no adelantar contra el saldo
    → evita el régimen de crédito

Y EN CADA CASO HAY QUE PREGUNTAR
  ¿el cliente pierde algo? Si sí, el
  régimen se asume; si no, se evita
```

### 3. La carga incremental por régimen

Cada régimen añadido tiene un coste que se puede estimar, y compararlo con lo
que aporta la función es la decisión que esta clase permite tomar a tiempo.

```text
CARGA INCREMENTAL SUPUESTA POR RÉGIMEN

  captación        alta, es el núcleo
  custodia         alta, exige claves y seguro
  mercado          alta, exige vigilancia
  intermediación   media
  asesoría         media, exige idoneidad
  cambio           media
  crédito          alta, exige provisiones

Y LA REGLA
  un régimen cuya función no cubre su
  carga incremental se elimina del alcance,
  no se «gestiona»
```

## 🧮 Ejemplo guiado

El ejemplo determina el perímetro del sistema y encuentra dos regímenes no previstos. Conviene identificar qué decisión de diseño activó cada uno: es lo que permite ajustar.

**Situación.** El equipo comprueba el perímetro del alcance reducido de la clase 1
—cuentas y pagos, transfronterizos, cambio y crédito con colateral— y descubre
dos regímenes que no había previsto.

```text
HECHOS DE DISEÑO RECOGIDOS
  a  el saldo del cliente queda en una cuenta
     a nombre de la entidad
  b  el cliente puede retirar cuando quiera
  c  el registro de colateral guarda claves
     de los activos pignorados
  d  la aplicación muestra «mejor tipo» al
     comparar divisas
  e  el cambio se ejecuta con margen propio
  f  se adelanta el 70 % del colateral
```

**Paso 1 — aplica las seis preguntas.**

```text
a + b   → CAPTACIÓN      previsto
c       → CUSTODIA       NO PREVISTO
d       → ASESORÍA       NO PREVISTO
e       → CAMBIO         previsto
f       → CRÉDITO        previsto

  DOS REGÍMENES NO PREVISTOS
```

**Paso 2 — analiza la custodia no prevista.**

```text
EL REGISTRO DE COLATERAL GUARDA CLAVES

  ¿es necesario para el producto?
  el colateral tiene que estar inmovilizado
  mientras dure el crédito

  ¿HAY ALTERNATIVA?
  · un custodio autorizado guarda el
    colateral y la entidad solo recibe
    la garantía
  · coste supuesto: 0,08 % anual del
    colateral

  CARGA DE ASUMIR LA CUSTODIA
  supuesto 180 000 al año
  COSTE DE DELEGARLA
  colateral previsto 24 000 000 × 0,08 %
  = 19 200 al año

  → SE DELEGA
```

**Paso 3 — analiza la asesoría no prevista.**

```text
«MEJOR TIPO» AL COMPARAR DIVISAS

  ¿aporta al cliente? sí, orienta

  ¿ACTIVA LA ASESORÍA?
  depende de si el criterio es objetivo
  y publicado, o de si la entidad gana
  más con una opción

  AJUSTE
  ordenar por coste total para el cliente,
  con el criterio publicado, y sin que la
  entidad gane distinto según la elección

  → EL CLIENTE NO PIERDE NADA
  → EL RÉGIMEN NO SE ACTIVA
```

**Paso 4 — recalcula el perímetro y su carga.**

```text
PERÍMETRO FINAL
  captación · pagos · cambio · crédito

  cuatro regímenes, los previstos en la
  clase 1

CARGA REGULATORIA
  se mantiene en 280 000 al año

Y DOS DECISIONES DE DISEÑO CAMBIADAS
  · el colateral lo custodia un tercero
    autorizado
  · la comparación de divisas ordena por
    criterio objetivo publicado

AMBAS COSTARON UNA REUNIÓN.
Descubrirlas en la clase 13, con el
sistema construido, habría costado
el rediseño de dos componentes.
```

**Interpreta:** Dos líneas de diseño activaban dos regímenes que nadie había previsto y que
sumaban una carga superior a la del resto del proyecto. **Ninguna de las dos era
necesaria para el producto**, y cambiarlas costó una reunión porque el sistema
todavía no existía.

## 🧭 Perspectivas

El perímetro del sistema afecta a cada actor de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un producto que compara divisas | Si confía en el orden |
| Equipo | Dos regímenes inesperados | Si ajusta el diseño |
| Custodio | Un colateral que guardar | Qué cobra |
| Banco | Una entidad con perímetro acotado | Si opera con ella |
| Supervisor | Cuatro regímenes declarados | Qué autoriza |
| Auditor | Hechos de diseño con consecuencia | Qué verifica |
| Abogado | Ajustes que evitan regímenes | Qué valida |
| Sociedad | Servicios con la autorización correcta | — |

## 🏦 Del cliente al banco

El cliente usa un servicio y el sistema puede estar ejerciendo actividades que no declaró. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Es solo una comparación» | Ordenar puede activar la asesoría | 23, clase 3 |
| «El colateral está seguro» | Lo custodia un tercero autorizado | 23, clase 3 |
| «Solo hacen pagos» | Captan, cambian y prestan | 23, clase 3 |

## ⚖️ Riesgos y controles

Los riesgos son de régimen descubierto tarde y de ajuste que perjudica al cliente. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Perímetro supuesto | Se cree saber qué se construye | Determinarlo por hechos de diseño |
| Integrar y creerse fuera | El proveedor ejecuta | La responsabilidad es de quien se relaciona con el cliente |
| Régimen descubierto tarde | Obliga a rediseñar | Determinarlo antes de construir |
| Asumir un régimen por costumbre | «Ya que estamos» | Comparar carga con aporte |
| Ajustar en perjuicio del cliente | Se evita el régimen quitando valor | Si el cliente pierde, se asume el régimen |
| No revisar al cambiar el diseño | El perímetro se fijó una vez | Revisión con cada cambio relevante |

## 🧪 Práctica

El laboratorio pide determinar el perímetro con sus hechos de diseño y proponer ajustes. El criterio de que el cliente no pierda es lo que valida el ajuste.

En [`labs/lab-02.md`](../labs/lab-02.md):

1. Recoge los hechos de diseño del sistema con su fuente.
2. Aplica las seis preguntas y anota los regímenes activados.
3. Compara la carga incremental de cada uno con lo que aporta.
4. Propón ajustes de diseño y comprueba que el cliente no pierde.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen proyectos que rediseñan tarde. La causa es haber determinado el perímetro después de construir.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Determinar el perímetro al final | Parece un trámite jurídico | Condiciona el diseño |
| Creer que integrar exime | El proveedor está autorizado | La relación con el cliente decide |
| Aceptar todo régimen activado | Se asume como inevitable | Comprobar si el diseño puede evitarlo |
| Evitar regímenes quitando valor | Es el ajuste fácil | Si el cliente pierde, no vale |
| Olvidar los accesorios | Parecen funcionalidades | Cada uno tiene carga |
| No documentar el hecho de diseño | Se recuerda | Sin fuente no es un hecho |

## ❓ Preguntas de comprobación

1. ¿Por qué integrar de un tercero no saca a la entidad del perímetro?
2. ¿Qué distingue un hecho de diseño de una decisión técnica cualquiera?
3. ¿Cuándo se asume un régimen y cuándo se evita con un ajuste?
4. ¿Qué pregunta hay que hacerse antes de aceptar un régimen activado?
5. En el ejemplo, ¿qué dos ajustes evitaron dos regímenes y qué costaron?

## 📥 Entregable

Guarda en `portfolio/parte-23/clase-03/`:

- los hechos de diseño con su fuente;
- los regímenes activados y los previstos;
- la carga incremental de cada régimen frente a su aporte;
- los ajustes de diseño propuestos, con su efecto sobre el cliente.

## 🔗 Referencias cruzadas

- **Viene de:** clases 1 y 2; Parte 22, clases 1 y 4.
- **Continúa en:** clases 4, 5 y 6 de esta parte.
- **Se aplica en:** clase 13 de esta parte.

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

- Financial Stability Board (2023). *Global Regulatory Framework for Crypto-asset Activities*. FSB. Criterio de actividad que se aplica al propio proyecto. <https://www.fsb.org/2023/07/fsb-global-regulatory-framework-for-crypto-asset-activities/>
- IOSCO (2023). *Policy Recommendations for Crypto and Digital Asset Markets*. IOSCO. Servicios sobre activos digitales que activan obligaciones. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- Biblioteca del Congreso Nacional de Chile. *Ley 21.521 que promueve la competencia e inclusión financiera a través de la innovación y tecnología en la prestación de servicios financieros*. Actividades reservadas por la ley chilena que el proyecto toca. <https://www.bcn.cl/leychile/navegar?idNorma=1187323>
- Comisión para el Mercado Financiero. *Normativa aplicable a entidades financieras*. CMF. Inscripción y obligaciones que el proyecto debe asumir en Chile. <https://www.cmfchile.cl/portal/principal/613/w3-channel.html>
- Verificación local: comprueba en la fuente oficial vigente qué exige tu jurisdicción sobre este punto antes de aplicar cualquier conclusión de la clase. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-20.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 02 · Construir, integrar o comprar](02-construir-integrar-o-comprar.md) | [Parte 23](../README.md) · [Programa](../../../SYLLABUS.md) | [04 · Decisión de arquitectura: ¿hace falta un registro? →](04-decision-de-arquitectura-registro.md) |
<!-- gen:footer:end -->
