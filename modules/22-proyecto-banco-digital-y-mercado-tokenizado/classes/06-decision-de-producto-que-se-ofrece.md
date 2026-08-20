<!-- meta
part: 23
class: 6
title: "Decisión de producto: qué se ofrece"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [chile, internacional]
regulatory_topics: [producto, idoneidad, calificacion]
regulation_last_verified: 2026-08-20
regulatory_status: vigente
primary_authorities: [IOSCO, CMF, OCDE]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 06 · Decisión de producto: qué se ofrece

> [← 05 · Decisión de arquitectura: el dinero](05-decision-de-arquitectura-el-dinero.md) · [Índice de la parte](../README.md) · [07 · El registro de referencia del sistema →](07-el-registro-de-referencia-del-sistema.md)

**Parte 23 — Proyecto — banco digital y mercado tokenizado** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Definir los instrumentos concretos que el sistema ofrece y **la calificación de
cada uno**, porque de ella dependen la información exigible, la protección del
cliente y la autorización necesaria.

Las clases 4 y 5 fijaron la arquitectura. Esta cierra el bloque de decisiones
previas con la que mira al cliente: qué se le ofrece exactamente. Y aplica al
propio catálogo el método de la Parte 22, clase 3.

## 📚 Objetivos

Al finalizar podrás:

1. **Calificar** cada instrumento del catálogo con los cuatro criterios.
2. **Determinar** el importe mínimo de equilibrio de cada producto.
3. **Evaluar** la idoneidad exigible al segmento objetivo.
4. **Redactar** la información precontractual que informa de verdad.
5. **Excluir** los productos cuya calificación no está clara.

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

Los cuatro primeros términos son el catálogo y su calificación; los cuatro siguientes, la información al cliente y sus límites. El **importe de equilibrio** es la cifra que decide el mínimo: por debajo de él el producto no rinde para el cliente, y ofrecerlo igualmente es una decisión comercial que hay que justificar.

| Concepto | Comprensión verificable |
|---|---|
| `catálogo` | Conjunto de instrumentos ofrecidos |
| `calificación` | Qué es jurídicamente cada uno |
| `importe de equilibrio` | Mínimo desde el que el cliente obtiene prima |
| `idoneidad` | Aptitud del cliente para el producto |
| `información precontractual` | La que se entrega antes de contratar |
| `comprensión efectiva` | Que el cliente entienda, no que se le informe |
| `producto excluido` | El descartado por calificación dudosa |
| `promesa verificable` | Afirmación del folleto con evidencia |

## 🧠 Modelo mental

El catálogo es donde el proyecto se encuentra por primera vez con una persona
concreta. Todo lo decidido hasta aquí —arquitectura, dinero, perímetro— importa
menos que la respuesta a una pregunta: qué está comprando el cliente y si le
conviene.

```text
CADA PRODUCTO NECESITA CUATRO RESPUESTAS

  1 ¿QUÉ ES?             calificación con los
                         cuatro criterios
  2 ¿PARA QUIÉN?         segmento y su idoneidad
  3 ¿DESDE CUÁNTO?       importe de equilibrio
  4 ¿QUÉ PROMETE?        y con qué evidencia

Y SI LA 1 NO ESTÁ CLARA, EL PRODUCTO
NO SE OFRECE.
No se ofrece «mientras se aclara»:
no se ofrece.
```

## 📖 Desarrollo

### 1. La calificación decide la protección

Un mismo instrumento con dos calificaciones da al cliente dos protecciones
distintas. Elegir la más cómoda para la entidad es elegir la menos protectora
para él, y eso el supervisor lo lee así.

```text
LO QUE CAMBIA CON LA CALIFICACIÓN

  autorización necesaria
  información exigible
  régimen de custodia aplicable
  prelación en un concurso
  y a quién reclama el cliente

EN ESTE PROYECTO
  el crédito con colateral tokenizado
  exige calificar el colateral: si es un
  valor, aplica el régimen de custodia
  de valores y su protección
```

### 2. El importe de equilibrio

Es la conclusión de la Parte 21, clase 7 aplicada al catálogo. Por debajo de
cierto importe, el coste unitario se come la prima por riesgo y el cliente rinde
menos que sin asumirlo.

```text
CÁLCULO

  rentabilidad neta = bruta − comisiones
                      − coste_unitario/importe

  el equilibrio está donde la neta supera
  a la alternativa sin riesgo

Y EL MÍNIMO DEL FOLLETO ES ESE,
no el que elige el área comercial
```

### 3. Información que informa

Un documento que cumple el contenido mínimo legal y que nadie entiende no
informa. La comprobación no es que se entregue: es que el cliente pueda
responder cuatro preguntas después de leerlo.

```text
LAS CUATRO PREGUNTAS

  ¿qué pasa si sale mal?
  ¿cuándo puedo salir?
  ¿cuánto cuesta en dinero, no en porcentaje?
  ¿qué pasa si la entidad desaparece?

SE MIDE CON USUARIOS REALES
y la tasa de respuestas correctas es el
dato que nunca se publica y el único que
demuestra que la información informó
```

## 🧮 Ejemplo guiado

El ejemplo califica el catálogo y calcula los importes de equilibrio. Conviene comparar con el mínimo comercial propuesto: casi nunca coinciden.

**Situación.** El equipo define el catálogo para las pymes exportadoras y
descubre que dos productos no superan el filtro.

```text
CATÁLOGO PROPUESTO
  1 cuenta operativa en dos monedas
  2 pago transfronterizo
  3 cambio de divisas al contado
  4 seguro de cambio a 90 días
  5 crédito con colateral tokenizado
  6 depósito a plazo tokenizado

SEGMENTO
  pymes exportadoras, saldo medio 38 000
  coste unitario 20 al año
```

**Paso 1 — califica cada producto.**

```text
1 cuenta operativa      depósito bancario
2 pago                  servicio de pago
3 cambio al contado     operación de cambio
4 seguro de cambio      DERIVADO
5 crédito con colateral crédito con garantía
6 depósito tokenizado   ¿depósito o valor?

  DOS DUDAS: el 4 activa el régimen de
  derivados y el 6 no está claro
```

**Paso 2 — resuelve el producto 4.**

```text
SEGURO DE CAMBIO A 90 DÍAS

  es un derivado, y ofrecerlo exige
  autorización adicional y capital

  ¿LO NECESITA EL SEGMENTO?
  sí: una pyme exportadora tiene riesgo
  de cambio real

  ¿HAY ALTERNATIVA?
  intermediarlo de un banco autorizado,
  cobrando comisión

  → SE INTERMEDIA, no se emite
```

**Paso 3 — resuelve el producto 6.**

```text
DEPÓSITO A PLAZO TOKENIZADO

  ¿es un depósito anotado en otro registro
  o un instrumento nuevo?

  la Parte 20, clase 8 lo respondió: si el
  obligado es el banco y hay garantía de
  depósitos, es un depósito

  PERO EN ESTE PROYECTO
  la entidad no es un banco con garantía
  de depósitos

  → EL PRODUCTO NO ES UN DEPÓSITO
  → y llamarlo así induce a error
  → SE EXCLUYE del catálogo
```

**Paso 4 — calcula el importe de equilibrio del crédito.**

```text
CRÉDITO CON COLATERAL

  no aplica un mínimo de inversión: aplica
  un mínimo de operación

  coste de originar supuesto        340
  margen sobre saldo               3,2 %
  plazo medio                    8 meses

  mínimo que cubre el coste
  340 / (3,2 % × 8/12) = 15 938

  → MÍNIMO DE 16 000, y por debajo se
    rechaza en vez de ofrecerse con
    condiciones peores
```

**Interpreta:** De seis productos, uno se intermedia en vez de emitirse y otro se excluye
porque **la entidad no puede ofrecer la protección que su nombre sugiere**. La
exclusión no fue por dificultad técnica: fue porque llamarlo depósito habría
inducido a error a un cliente que no tiene por qué conocer la diferencia.

## 🧭 Perspectivas

El catálogo afecta a cada actor de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Seis productos en el catálogo | Cuál contrata |
| Pyme | Riesgo de cambio real | Si cubre |
| Equipo | Dos productos con dudas | Si los ofrece |
| Banco | Un derivado que intermediar | Qué comisión acepta |
| Supervisor | Un producto llamado depósito | Qué exige corregir |
| Auditor | Calificación documentada | Qué verifica |
| Abogado | Dos calificaciones dudosas | Qué recomienda |
| Sociedad | Productos que dicen lo que son | — |

## 🏦 Del cliente al banco

El cliente ve productos y el sistema asume un régimen por cada uno. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Es un depósito» | Sin garantía de depósitos detrás | 23, clase 6 |
| «Cubren el riesgo de cambio» | Lo intermedian de un banco | 23, clase 6 |
| «Desde cualquier importe» | Por debajo de 16 000 no cubre su coste | 23, clase 6 |

## ⚖️ Riesgos y controles

Los riesgos son de calificación y de comprensión efectiva. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Calificación dudosa ofrecida | Se lanza «mientras se aclara» | Si no está clara, no se ofrece |
| Nombre que induce a error | Suena familiar al cliente | El nombre tiene que decir lo que es |
| Mínimo por marketing | «Desde cualquier importe» | Calcular el de equilibrio |
| Emitir lo que se puede intermediar | Da más margen | Compara con la autorización que exige |
| Información que cumple y no informa | Se entrega el mínimo legal | Medir la comprensión |
| Idoneidad que nunca excluye | Reduce la colocación | Publicar la tasa de exclusión |

## 🧪 Práctica

El laboratorio pide calificar el catálogo y calcular los importes de equilibrio. El producto excluido con su razón es parte del entregable.

En [`labs/lab-02.md`](../labs/lab-02.md):

1. Califica cada producto del catálogo con los cuatro criterios.
2. Determina cuáles se emiten, cuáles se intermedian y cuáles se excluyen.
3. Calcula el importe de equilibrio de cada producto.
4. Redacta la información precontractual con las cuatro preguntas.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen catálogos con problemas. Las causas son calificaciones por nombre e importes mínimos fijados por marketing.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Calificar por el nombre | Es lo rápido | Los cuatro criterios |
| Ofrecer con la calificación pendiente | El lanzamiento apremia | No se ofrece |
| Usar nombres familiares | Facilita la venta | Si induce a error, no vale |
| Mínimo elegido | Es una decisión comercial | Es un cálculo |
| Emitir por margen | Da más ingreso | Cuenta la autorización que exige |
| Folleto sin probar | Cumple la norma | Pruébalo con usuarios |

## ❓ Preguntas de comprobación

1. ¿Qué cuatro respuestas necesita cada producto del catálogo?
2. ¿Qué cambia con la calificación de un instrumento?
3. ¿Cómo se calcula el importe de equilibrio?
4. ¿Qué cuatro preguntas debe poder responder el cliente tras leer la información?
5. En el ejemplo, ¿por qué se excluyó el depósito tokenizado?

## 📥 Entregable

Guarda en `portfolio/parte-23/clase-06/`:

- la calificación de cada producto con su fundamento;
- la decisión de emitir, intermediar o excluir;
- el importe de equilibrio de cada uno;
- la información precontractual con las cuatro preguntas.

## 🔗 Referencias cruzadas

- **Viene de:** clases 1, 3 y 5; Parte 20, clase 8; Parte 22, clase 3.
- **Continúa en:** clases 8 y 12 de esta parte.
- **Se aplica en:** clases 13 y 17 de esta parte.

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

- IOSCO (2023). *Policy Recommendations for Crypto and Digital Asset Markets*. IOSCO. Calificación de cada instrumento y sus consecuencias. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- OCDE (2011). *G20/OECD High-Level Principles on Financial Consumer Protection*. OECD. Idoneidad y revelación exigibles al producto ofrecido. <https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0394>
- Biblioteca del Congreso Nacional de Chile. *Ley 21.521 que promueve la competencia e inclusión financiera a través de la innovación y tecnología en la prestación de servicios financieros*. Encaje de los productos en las figuras de la ley chilena. <https://www.bcn.cl/leychile/navegar?idNorma=1187323>
- Comisión para el Mercado Financiero. *Normativa aplicable a entidades financieras*. CMF. Obligaciones chilenas asociadas a cada producto del catálogo. <https://www.cmfchile.cl/portal/principal/613/w3-channel.html>
- Verificación local: comprueba en la fuente oficial vigente qué exige tu jurisdicción sobre este punto. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-20.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 05 · Decisión de arquitectura: el dinero](05-decision-de-arquitectura-el-dinero.md) | [Parte 23](../README.md) · [Programa](../../../SYLLABUS.md) | [07 · El registro de referencia del sistema →](07-el-registro-de-referencia-del-sistema.md) |
<!-- gen:footer:end -->
