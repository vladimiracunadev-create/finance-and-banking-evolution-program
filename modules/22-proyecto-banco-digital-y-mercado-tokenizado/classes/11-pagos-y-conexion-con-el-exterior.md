<!-- meta
part: 23
class: 11
title: "Pagos y conexión con el exterior"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [pagos, corresponsalia, sanciones]
regulation_last_verified: 2026-08-19
regulatory_status: vigente
primary_authorities: [CPMI, GAFI, FSB]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 11 · Pagos y conexión con el exterior

> [← 10 · Liquidación y sus modos de fallo](10-liquidacion-y-sus-modos-de-fallo.md) · [Índice de la parte](../README.md) · [12 · Ciclo de vida y operación diaria →](12-ciclo-de-vida-y-operacion-diaria.md)

**Parte 23 — Proyecto — banco digital y mercado tokenizado** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Conectar el sistema con el exterior: pagos locales, transfronterizos y el
cumplimiento que los acompaña. **Un mensaje no es un movimiento de fondos**, y el
diseño tiene que modelar los cuatro flujos por separado.

La clase 10 resolvió la liquidación interna. Esta abre el sistema hacia fuera,
donde ya no manda el propio registro y donde aparecen los tramos, las ventanas
horarias y el cumplimiento de la Parte 18.

## 📚 Objetivos

Al finalizar podrás:

1. **Modelar** los cuatro flujos de un pago por separado.
2. **Calcular** el coste total de una ruta con todos sus tramos.
3. **Diseñar** el screening con su precisión y su exhaustividad.
4. **Determinar** la ventana de exposición y su acotación.
5. **Gestionar** el resto de destinos no identificables.

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

Los cuatro primeros términos son los cuatro flujos de un pago, que se mueven a ritmos distintos; los cuatro siguientes, sus tramos y sus controles. El **resto no identificable** es el problema operativo que ningún diseño elimina: siempre hay pagos que llegan sin referencia y hay que decidir qué se hace con ellos.

| Concepto | Comprensión verificable |
|---|---|
| `flujo de mensaje` | La instrucción que viaja |
| `flujo de fondos` | El dinero que se mueve en cuentas |
| `flujo contable` | Los asientos de cada participante |
| `flujo de cumplimiento` | Las comprobaciones y sus alertas |
| `tramo` | Cada componente del coste de una ruta |
| `ventana de exposición` | De irrevocable a confirmado |
| `screening` | Cotejo contra listas de sanciones |
| `resto no identificable` | Destinos sin sujeto obligado detrás |

## 🧠 Modelo mental

La confusión entre mensaje y fondos es el origen de la mitad de los errores de
esta materia, y en un sistema propio se materializa como un asiento contable que
se hace cuando llega el mensaje en vez de cuando llegan los fondos.

```text
LOS CUATRO FLUJOS

  MENSAJE      la instrucción
  FONDOS       el dinero en cuentas
  CONTABLE     los asientos
  CUMPLIMIENTO las comprobaciones

CADA UNO CON SU MOMENTO Y SU FALLO

Y EL ERROR TÍPICO
  abonar al cliente cuando llega el mensaje,
  antes de que lleguen los fondos
  → eso es crédito, no un pago
```

## 📖 Desarrollo

### 1. El coste total por tramos

Comparar el precio mostrado de dos rutas esconde la mayor parte del coste. La
comparación honesta suma todos los tramos de ambas, y suele invertir la
conclusión.

```text
TRAMOS DE UNA RUTA

  diferencial de cambio
  comisión propia
  comisión de cada corresponsal
  coste de mensajería
  coste de liquidez inmovilizada
  y el impacto si hay que ejecutar en
  varios tramos

EL DE CORRESPONSALÍA ES EL QUE MÁS PESA
en corredores poco líquidos, y el que se
elimina cambiando la topología
```

### 2. Screening con métricas

Un sistema de cotejo se calibra con precisión y exhaustividad, no con la
sensación de que funciona. Y la decisión de mover el umbral es del comité, no del
equipo.

```text
PRECISIÓN      confirmados / alertas
EXHAUSTIVIDAD  confirmados / casos reales

subir el umbral   menos ruido, menos detección
bajarlo           más detección, más coste

Y LA PRUEBA RETROSPECTIVA
  pasar casos conocidos y comprobar
  cuántos se habrían detectado
```

### 3. El resto no identificable

La regla del viaje exige saber a quién enviar los datos, y el registro no lo
dice. Ese resto es estructural: lo que define el programa es cómo lo gestiona.

```text
TRATAMIENTO POR TRAMOS

  importe bajo   declaración del cliente
  medio          más análisis de procedencia
  alto           medidas reforzadas y
                 aprobación

Y PROHIBIRLO TODO NO ES LA SOLUCIÓN
  desplaza la actividad a un proveedor
  sin controles
```

## 🧮 Ejemplo guiado

El ejemplo modela los cuatro flujos de un pago por separado. Conviene ver dónde se desincronizan: el asiento contable no puede ir con el mensaje.

**Situación.** El equipo diseña la ruta de pagos transfronterizos para las pymes
exportadoras y calibra el screening.

```text
DATOS
  pagos transfronterizos al mes       1 800
  importe medio                      52 000
  corredores                              3
  alertas de screening al mes           240
  confirmadas                             4
  casos conocidos a posteriori            6
```

**Paso 1 — modela los cuatro flujos.**

```text
MENSAJE     se envía y puede perderse
FONDOS      llegan en T+1 o T+2
CONTABLE    el asiento se hace CON LOS
            FONDOS, no con el mensaje
CUMPLIMIENTO se ejecuta antes de enviar

Y LA REGLA
  no se abona al cliente hasta que los
  fondos están; si se abona antes, se
  declara como crédito y se provisiona
```

**Paso 2 — calcula el coste por corredor.**

```text
CORREDOR PRINCIPAL
  diferencial 1,2 pb + comisión 3 pb
  = 3,6 pb

CORREDOR POCO LÍQUIDO
  diferencial 45 pb / 2 + comisión 18
  + dos tramos de corresponsalía 22
  = 62,5 pb

  EN EL SEGUNDO, ELIMINAR UN TRAMO
  DE CORRESPONSALÍA AHORRA MÁS QUE
  CUALQUIER MEJORA DE PRECIO
```

**Paso 3 — calibra el screening.**

```text
precisión      4 / 240 = 1,67 %
exhaustividad  4 / 6 = 66,7 %

  se escapan 2 de 6

PRUEBA RETROSPECTIVA
  de los 2 no detectados, 1 era una
  coincidencia parcial de nombre con
  transliteración distinta

AJUSTE
  añadir equivalencias de transliteración
  supuesto: +38 alertas, +1 caso
  exhaustividad → 83,3 %
```

**Paso 4 — gestiona el resto no identificable.**

```text
destinos no identificables      32 %

TRATAMIENTO
  hasta 5 000      declaración
  5 000 – 40 000   más procedencia
  más de 40 000    reforzadas y aprobación

Y UNA MÉTRICA DE GESTIÓN
  porcentaje del resto sobre el total,
  reportado al comité cada mes

  si sube, el programa se revisa;
  si se lleva a cero, probablemente se
  está rechazando actividad legítima
```

**Interpreta:** El ajuste que más mejoró la detección fue **añadir equivalencias de
transliteración**, un detalle de normalización de texto que subió la exhaustividad
16,6 puntos. Y en el corredor poco líquido, eliminar un tramo de corresponsalía
ahorraba más que cualquier negociación de precio.

## 🧭 Perspectivas

Los pagos con el exterior afectan a cada actor de forma distinta, y varios de ellos solo ven uno de los cuatro flujos. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un pago que tarda dos días | Si acepta |
| Pyme | Coste total del corredor | Por dónde paga |
| Equipo | Cuatro flujos que modelar | Cómo los separa |
| Corresponsal | Un tramo de la ruta | Qué cobra |
| Cumplimiento | 240 alertas al mes | Cómo calibra |
| Supervisor | Exhaustividad del 66,7 % | Qué exige |
| Auditor | Asiento contra fondos | Qué verifica |
| Sociedad | Pagos vigilados | — |

## 🏦 Del cliente al banco

El cliente envía dinero al exterior y el sistema coordina cuatro flujos con tramos distintos. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Ya me llegó el aviso» | El aviso no son los fondos | 23, clase 11 |
| «Es más barato por aquí» | 62,5 pb frente a 3,6 | 23, clase 11 |
| «Me piden datos del destino» | La regla del viaje lo exige | 23, clase 11 |

## ⚖️ Riesgos y controles

Los riesgos son de desincronización y de cumplimiento. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Abonar con el mensaje | Parece equivalente | Es crédito y hay que declararlo |
| Comparar precios mostrados | Es lo visible | Suma todos los tramos |
| Screening sin métricas | Se cree que funciona | Precisión y exhaustividad |
| Sin prueba retrospectiva | Nadie la pide | Es lo que descubre lo que falta |
| Prohibir el resto | Parece prudente | Desplaza la actividad |
| Resto llevado a cero | Se persigue el ideal | Rechaza actividad legítima |

## 🧪 Práctica

El laboratorio pide modelar los cuatro flujos y resolver el resto no identificable. El procedimiento para lo no identificable es lo que se evalúa.

En [`labs/lab-05.md`](../labs/lab-05.md):

1. Modela los cuatro flujos con su momento y su fallo.
2. Calcula el coste total por corredor con todos los tramos.
3. Calibra el screening y ejecuta la prueba retrospectiva.
4. Diseña el tratamiento por tramos del resto no identificable.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen pagos con problemas contables o de cumplimiento. La causa es haber tratado los cuatro flujos como uno.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Confundir mensaje y fondos | Llegan casi juntos | El asiento va con los fondos |
| Un solo corredor | Simplifica | El coste varía en un orden de magnitud |
| Optimizar la precisión | Reduce el ruido | La exhaustividad protege |
| Screening sin transliteración | Es un detalle | Sube la detección 16 puntos |
| Prohibir por prudencia | Parece seguro | Desplaza y ciega |
| Sin métrica del resto | No se mide | Es el indicador de gestión |

## ❓ Preguntas de comprobación

1. ¿Cuáles son los cuatro flujos y cuál es el error típico entre dos de ellos?
2. ¿Qué tramo pesa más en un corredor poco líquido?
3. ¿Cómo se calibra un sistema de screening?
4. ¿Qué descubre una prueba retrospectiva?
5. ¿Por qué llevar el resto no identificable a cero es una mala señal?

## 📥 Entregable

Guarda en `portfolio/parte-23/clase-11/`:

- los cuatro flujos modelados por separado;
- el coste total por corredor con todos los tramos;
- el screening calibrado con su prueba retrospectiva;
- el tratamiento por tramos del resto no identificable.

## 🔗 Referencias cruzadas

- **Viene de:** clases 8 y 10; Parte 18, clases 1, 9 y 12.
- **Continúa en:** clase 12 de esta parte.
- **Se aplica en:** clases 13 y 15 de esta parte.

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

- CPMI e IOSCO (2012). *Principles for Financial Market Infrastructures*. BIS. Requisitos de firmeza del sistema de pagos con el que se conecta. <https://www.bis.org/cpmi/publ/d101.htm>
- Financial Action Task Force (2021). *Updated Guidance for a Risk-Based Approach to Virtual Assets and VASPs*. FATF. Obligaciones de información en transferencias de activos virtuales. <https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-rba-virtual-assets-2021.html>
- Financial Stability Board (2023). *Global Regulatory Framework for Crypto-asset Activities*. FSB. Marco global aplicable a la conexión con el exterior. <https://www.fsb.org/2023/07/fsb-global-regulatory-framework-for-crypto-asset-activities/>
- Comisión para el Mercado Financiero. *Normativa aplicable a entidades financieras*. CMF. Obligaciones cambiarias y de pago aplicables en Chile. <https://www.cmfchile.cl/portal/principal/613/w3-channel.html>
- Verificación local: comprueba en la fuente oficial vigente qué exige tu jurisdicción sobre este punto. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-19.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 10 · Liquidación y sus modos de fallo](10-liquidacion-y-sus-modos-de-fallo.md) | [Parte 23](../README.md) · [Programa](../../../SYLLABUS.md) | [12 · Ciclo de vida y operación diaria →](12-ciclo-de-vida-y-operacion-diaria.md) |
<!-- gen:footer:end -->
