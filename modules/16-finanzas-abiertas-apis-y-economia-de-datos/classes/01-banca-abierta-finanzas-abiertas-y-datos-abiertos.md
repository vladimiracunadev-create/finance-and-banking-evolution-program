<!-- meta
part: 17
class: 1
title: "Banca abierta, finanzas abiertas y datos abiertos"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global, chile, union-europea]
regulatory_topics: [open-finance]
regulation_last_verified: 2026-08-06
regulatory_status: en-despliegue
primary_authorities: [CMF]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 01 · Banca abierta, finanzas abiertas y datos abiertos

> [← Índice de la parte](../README.md) · [Índice de la parte](../README.md) · [02 · Ecosistema, participantes y modelos de implantación →](02-ecosistema-participantes-y-modelos-de-implantacion.md)

**Parte 17 — Finanzas abiertas, APIs y economía de datos** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Fijar la distinción que sostiene toda la parte: **banca abierta**, **finanzas
abiertas** y **datos abiertos** no son tres nombres del mismo fenómeno. Cambia
qué se comparte, quién está obligado, con qué consentimiento y qué riesgo aparece.

La Parte 14, clase 3 presentó el concepto. Aquí empieza la ingeniería y el
régimen jurídico que lo sostiene.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** banca abierta, finanzas abiertas y datos abiertos con un
   criterio que resista un caso límite.
2. **Identificar** qué actividad realiza cada participante y si esa actividad
   entra en el perímetro regulado.
3. **Explicar** por qué el consentimiento —y no la API— es el núcleo del modelo.
4. **Evaluar** qué problema resuelve el modelo y para quién, separando el valor
   del cliente del valor del proveedor.
5. **Reconocer** los riesgos que el modelo crea y que no existían antes.

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

Los tres primeros términos son tres cosas distintas que se nombran igual, y confundirlas hace imposible saber qué obliga. Los cinco siguientes son las figuras del ecosistema y su pieza central. El **consentimiento** es el núcleo del régimen: no lo define la tecnología sino el permiso del titular, y por eso una API sin consentimiento no es finanzas abiertas.

| Concepto | Comprensión verificable |
|---|---|
| `banca abierta` | Compartir datos de cuentas bancarias e iniciar pagos con consentimiento |
| `finanzas abiertas` | Extensión a todos los productos financieros: crédito, seguros, inversiones, previsión |
| `datos abiertos` | Publicación de datos no personales de la entidad: tarifas, sucursales, condiciones |
| `proveedor de información` | Quien accede a datos del cliente por cuenta de este |
| `proveedor de iniciación` | Quien ordena un pago desde la cuenta del cliente |
| `institución proveedora` | Quien custodia el dato o la cuenta y debe darle acceso |
| `consentimiento` | Acto del cliente que delimita alcance, finalidad y plazo |
| `reciprocidad` | Obligación de compartir de quien exige compartir |

## 🧠 Modelo mental

El modelo mental son tres capas concéntricas: los datos abiertos no tienen titular, la banca abierta cubre cuentas y pagos, y las finanzas abiertas alcanzan a seguros, inversiones y previsión. Cada capa amplía el alcance y mantiene la misma exigencia de consentimiento.

```text
LAS TRES CAPAS, DE MENOS A MÁS SENSIBLE

  DATOS ABIERTOS
    qué        tarifas, comisiones, sucursales, requisitos de productos
    de quién   de la entidad
    consentimiento  NO se necesita: no hay dato personal
    riesgo     bajo; el peor caso es información desactualizada

  BANCA ABIERTA
    qué        cuentas, saldos, movimientos, iniciación de pagos
    de quién   del cliente
    consentimiento  IMPRESCINDIBLE, por finalidad y con plazo
    riesgo     acceso indebido, pago no autorizado, perfilado

  FINANZAS ABIERTAS
    qué        todo lo anterior + crédito, seguros, inversiones, previsión
    de quién   del cliente
    consentimiento  IMPRESCINDIBLE, y más difícil de explicar
    riesgo     todo lo anterior + inferencia sobre salud, familia y solvencia

LA PREGUNTA QUE ORDENA LAS TRES
  ¿el dato identifica o permite inferir algo sobre una persona?
    NO  → datos abiertos: publícalo
    SÍ  → hace falta consentimiento, y el diseño empieza por ahí
```

## 📖 Desarrollo

### 1. Qué problema pretende resolver el modelo

Antes del modelo, un cliente que quería usar una aplicación de finanzas
personales tenía dos opciones, ambas malas:

```text
OPCIÓN A — entregar usuario y clave del banco a la aplicación
  · la aplicación puede hacer TODO lo que puede hacer el cliente
  · no hay forma de acotar el acceso
  · no hay forma de revocar salvo cambiar la clave
  · no hay registro de qué hizo la aplicación
  · si hay fraude, el banco alega uso indebido de credenciales

OPCIÓN B — teclear los datos a mano
  · funciona, y no escala
```

El modelo sustituye la credencial compartida por una **delegación acotada**: la
aplicación obtiene permiso para leer tres cosas concretas, durante un plazo
concreto, y el cliente puede retirarlo.

```text
LO QUE CAMBIA NO ES LA TECNOLOGÍA: ES QUIÉN CONTROLA EL ACCESO
  antes  el que tiene la contraseña
  ahora  el que otorgó el consentimiento, mientras lo mantenga
```

### 2. Los tres modelos de implantación

| Modelo | Quién obliga | Ejemplo de referencia | Efecto observado |
|---|---|---|---|
| Regulatorio | La norma obliga a compartir | Unión Europea, Chile, Brasil | Cobertura amplia, ritmo lento |
| De mercado | Los participantes acuerdan | Estados Unidos por vía contractual | Ritmo rápido, cobertura desigual |
| Híbrido | La norma fija principios, el mercado los estándares | Varios | Depende de la gobernanza del estándar |

```text
NINGUNO ES SUPERIOR EN ABSTRACTO
  regulatorio  resuelve la cobertura, no resuelve la calidad
  de mercado   resuelve la calidad donde hay incentivo, deja huecos
  híbrido      funciona si la gobernanza del estándar es creíble
```

### 3. Quién es quién

El modelo reparte el trabajo entre cinco figuras, y cada una tiene una
obligación distinta. Conviene fijarlas ahora porque el resto de la parte se
apoya en estos nombres: cuando más adelante se diga «el proveedor de
iniciación», se estará hablando exactamente de la cuarta.

```text
CLIENTE
  titular del dato y de la cuenta; otorga y revoca

INSTITUCIÓN PROVEEDORA (banco, aseguradora, administradora)
  custodia el dato; está OBLIGADA a darle acceso al tercero autorizado
  responde de la autenticación del cliente

PROVEEDOR DE INFORMACIÓN
  accede a datos por cuenta del cliente; NO mueve dinero

PROVEEDOR DE INICIACIÓN
  ordena pagos desde la cuenta del cliente; NO custodia fondos

PROVEEDOR DE SERVICIOS TECNOLÓGICOS
  opera la infraestructura de los anteriores
  NO tiene relación con el cliente, y CONCENTRA riesgo
```

La última figura es la que más se subestima. Un proveedor tecnológico que opera
la conexión de cuarenta entidades no aparece en el contrato del cliente, no
está en su panel de consentimientos y, sin embargo, su caída deja sin servicio a
todo el sistema.

### 4. Reciprocidad y acceso obligatorio

Dos reglas sostienen que el modelo arranque y que se mantenga en pie. La
primera obliga a abrir; la segunda impide que abrir sea un mal negocio para
quien abre. El bloque las separa porque un sistema puede tener la primera sin
la segunda, y ahí es donde aparece el desequilibrio.

```text
ACCESO OBLIGATORIO
  «las instituciones deben dar acceso a los terceros autorizados»
  → resuelve el arranque: sin obligación, nadie abre primero

RECIPROCIDAD
  «quien exige acceso debe también darlo»
  → resuelve el equilibrio: evita el participante que solo extrae

SIN RECIPROCIDAD APARECE UN INCENTIVO PERVERSO
  el gran agregador consume datos de todos
  y no aporta los suyos
  → concentra información sin coste de apertura
```

### 5. Qué riesgo crea el modelo que antes no existía

| Riesgo nuevo | Por qué aparece | A quién afecta |
|---|---|---|
| Concentración de agregadores | Pocos intermedian a muchos | Sistema |
| Proveedor tecnológico crítico | Infraestructura compartida no visible | Sistema |
| Fatiga de consentimiento | El cliente acepta sin leer | Cliente |
| Inferencia sensible | Los movimientos revelan salud, ideología, familia | Cliente |
| Reparto de responsabilidad opaco | Tres partes en un fraude | Cliente y entidades |
| Superficie de ataque ampliada | Cada conexión es una puerta | Todos |

```text
EL MODELO NO ES NEUTRAL EN RIESGO
  reduce   el riesgo de la credencial compartida
  aumenta  el riesgo de concentración y de inferencia
  y traslada parte del riesgo de la entidad al ecosistema
```

## 🧮 Ejemplo guiado

El ejemplo clasifica productos concretos en las tres capas y determina qué figura y qué consentimiento exige cada uno. Conviene hacer la clasificación antes de mirar ninguna especificación técnica: la capa decide el régimen.

**Situación.** Una empresa quiere lanzar tres productos y necesita saber, para
cada uno, qué capa del modelo usa, si la actividad es regulada y qué
consentimiento requiere.

```text
PRODUCTO 1 — comparador de comisiones de cuentas corrientes
PRODUCTO 2 — panel que muestra saldos de cuatro bancos
PRODUCTO 3 — panel anterior + botón «pagar mi tarjeta desde el banco A»
```

**Paso 1 — clasifica el Producto 1.**

```text
¿QUÉ DATO USA?
  tarifas y condiciones publicadas por las entidades
  → NO hay dato personal
  → NO hay cuenta de cliente

CAPA:            datos abiertos
CONSENTIMIENTO:  no aplica
ACTIVIDAD:       en principio no regulada como servicio financiero
CUIDADO:         si además RECOMIENDA un producto concreto,
                 puede constituir asesoría, que sí está regulada
```

**Paso 2 — clasifica el Producto 2.**

```text
¿QUÉ DATO USA?
  saldos y movimientos de cuentas del cliente en cuatro entidades
  → dato personal financiero
  → acceso por cuenta del cliente

CAPA:            banca abierta
FIGURA:          proveedor de servicios de información
CONSENTIMIENTO:  por finalidad, con plazo y revocable
ACTIVIDAD:       regulada; requiere inscripción o autorización
                 según la norma local
```

**Paso 3 — clasifica el Producto 3.**

```text
AÑADE:  ordenar un pago desde la cuenta del cliente
FIGURA: proveedor de iniciación de pagos

CAMBIO SUSTANTIVO
  el Producto 2 puede equivocarse y mostrar un saldo erróneo
  el Producto 3 puede equivocarse y MOVER DINERO

  → autenticación reforzada
  → consentimiento de un solo uso, ligado a importe y beneficiario
  → régimen de responsabilidad por operación no autorizada
  → normalmente, mayor exigencia de capital y de seguro
```

**Paso 4 — cuantifica la diferencia de coste de cumplimiento.**

```text
SUPUESTOS DEL EJERCICIO (cifras ilustrativas, no de mercado)

  PRODUCTO 2 — información
    inscripción y asesoría inicial          8 000
    seguro de responsabilidad civil anual   4 500
    auditoría de seguridad anual            6 000
    cumplimiento y reporte anual            9 000
    TOTAL primer año                       27 500

  PRODUCTO 3 — información + iniciación
    autorización y asesoría inicial        22 000
    seguro de responsabilidad civil anual  14 000
    auditoría de seguridad anual           11 000
    cumplimiento y reporte anual           18 000
    gestión de fraude y disputas anual     16 000
    TOTAL primer año                       81 000
```

**Paso 5 — decide con el número delante.**

```text
DIFERENCIA: 81 000 − 27 500 = 53 500 el primer año

¿QUÉ INGRESO ADICIONAL APORTA EL BOTÓN DE PAGO?
  supuesto: 12 000 pagos al año, comisión de 0,9 % sobre
  un ticket medio de 180 000 → 12 000 × 1 620 = 19 440 000
  ... si el ticket medio fuera de 180 000

  con un ticket medio de 45 000: 12 000 × 405 = 4 860 000

EL CÁLCULO NO ES EL PUNTO
  el punto es que la iniciación de pagos cambia el RÉGIMEN,
  no solo el producto: cambia la figura regulatoria,
  el capital, el seguro, la responsabilidad y el proceso de disputas
```

**Paso 6 — formula la decisión.**

```text
LANZAR EL PRODUCTO 2 PRIMERO

MOTIVOS
  1. valida la demanda con un tercio del coste de cumplimiento
  2. construye el historial de operación que la autorización
     de iniciación va a exigir
  3. el consentimiento de información es prerrequisito del de pago:
     la curva de aprendizaje es acumulativa

CONDICIÓN PARA AÑADIR EL PRODUCTO 3
  · 40 000 clientes activos con consentimiento vigente
  · tasa de revocación por debajo del 8 % anual
  · cero incidentes de acceso indebido en 12 meses
```

**Interpreta:** los tres productos parecen variaciones del mismo. Regulatoriamente
son tres cosas distintas, y la diferencia no está en el software: está en si el
producto **lee** o **mueve**.

## 🧭 Perspectivas

La misma apertura se ve distinta desde cada actor, y ninguna de esas visiones es completa por sí sola. La tabla las enfrenta, y conviene leerla entera: las decisiones de las trece clases siguientes afectan a varios de estos actores a la vez.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Una aplicación que le pide permiso | Si otorga y por cuánto tiempo |
| Comercio | Un método de cobro más barato | Si lo integra |
| Fintech | Acceso a datos que antes no tenía | Qué figura solicita |
| Banco | Obligación de dar acceso y perder exclusividad | Si compite o se integra |
| Banco central | Cambio en los flujos de pago | Si vigila el nuevo canal |
| Infraestructura | Volumen de llamadas nuevo | Capacidad y disponibilidad |
| Supervisor | Nuevos participantes en el perímetro | Qué exige a cada figura |
| Auditor | Consentimientos y evidencia | Si la evidencia reconstruye la decisión |
| Sociedad | Más competencia y más exposición | El equilibrio entre ambas |

## 🏦 Del cliente al banco

El cliente describe lo que hace con palabras cotidianas y el banco tiene que traducirlo a figuras con consecuencias jurídicas. La tabla enfrenta las dos lecturas y señala en qué clase se desarrolla cada una.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Le di mi clave a esa app» | Credencial compartida, riesgo no acotado | 17, clase 1 |
| «Autoricé ver mis cuentas» | Consentimiento con alcance y plazo | 17, clase 5 |
| «No sé qué apps tienen acceso» | Panel de consentimientos obligatorio | 17, clase 5 |
| «La app me dejó pagar» | Iniciación: cambia la figura y el riesgo | 17, clase 10 |
| «Me cobraron algo que no ordené» | Matriz de responsabilidad | 17, clase 11 |

## ⚖️ Riesgos y controles

Los riesgos de esta clase no vienen de la tecnología sino del diseño del consentimiento y de la estructura del mercado. La tabla los recoge con el control que los acota.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Consentimiento no informado | El cliente acepta un texto que no entiende | Lenguaje verificado y alcance por finalidad |
| Extracción excesiva | Se pide más dato del necesario | Minimización auditada por alcance |
| Concentración | Tres agregadores intermedian el 80 % | Vigilancia del supervisor y planes de sustitución |
| Proveedor crítico | Una caída deja sin servicio a 40 entidades | Registro de proveedores y pruebas de continuidad |
| Responsabilidad difusa | Nadie responde ante el fraude | Matriz contractual y régimen legal |
| Inferencia sensible | Se deduce un dato de salud del gasto | Prohibición de finalidad secundaria |

## 🧪 Práctica

El laboratorio pide clasificar seis productos en las tres capas y determinar su figura y su consentimiento. La clasificación es lo que decide todo lo demás, y hacerla antes de mirar la API es el hábito que la clase instala.

En [`labs/lab-01.md`](../labs/lab-01.md):

1. Clasifica seis productos en las tres capas del modelo.
2. Determina para cada uno la figura regulatoria y el consentimiento necesario.
3. Escribe el dato mínimo de uno de ellos antes de mirar ninguna API.
4. Identifica en cuál de los seis aparece un proveedor tecnológico crítico.

## ⚠️ Errores frecuentes

La tabla se usa buscando el síntoma. En esta clase casi todos vienen de haber confundido las tres capas o de haber tratado la API como si fuera el régimen.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| «Finanzas abiertas es una API» | Se confunde el medio con el régimen | El núcleo es el consentimiento |
| Datos abiertos tratados con consentimiento | No se distinguió el dato personal | Clasifica el dato primero |
| Leer e iniciar tratados igual | Se ignora que uno mueve dinero | Figuras y regímenes distintos |
| Se olvida al proveedor tecnológico | No tiene relación con el cliente | Inclúyelo en el mapa de riesgo |
| Se asume que el modelo reduce riesgo | Solo se miró el riesgo que elimina | Enumera también el que crea |
| Reciprocidad confundida con acceso | Términos usados como sinónimos | Uno obliga a abrir, otro a devolver |

## ❓ Preguntas de comprobación

1. ¿Qué distingue exactamente banca abierta de finanzas abiertas, y por qué la
   distinción cambia el diseño del consentimiento?
2. ¿Por qué compartir usuario y clave es peor que la delegación por token, aunque
   ambos funcionen?
3. ¿Qué actividad convierte a un producto de «no regulado» a «regulado» en el
   ejemplo guiado, y por qué?
4. ¿Qué riesgo introduce el modelo que no existía antes, y a quién afecta?
5. ¿Por qué un proveedor tecnológico crítico no aparece en el panel de
   consentimientos del cliente y por qué eso es un problema?

## 📥 Entregable

Guarda en `portfolio/parte-17/clase-01/`:

- la clasificación de seis productos en las tres capas, con figura regulatoria;
- el dato mínimo de uno de ellos, escrito antes de consultar ninguna API;
- el mapa de participantes de ese producto, incluido el proveedor tecnológico;
- tres riesgos que el modelo crea, con el control que propondrías.

## 🔗 Referencias cruzadas

- **Viene de:** Parte 14, clase 3 (banca abierta y APIs); Parte 14, clase 4
  (datos en un banco); Parte 12, clase 1 (perímetro regulatorio).
- **Continúa en:** clase 2 (ecosistema y modelos), clase 3 (Chile), clase 5
  (consentimiento).
- **Se aplica en:** Parte 18, clase 13 (interconexión de pagos inmediatos);
  Parte 22, clase 5 (registro y autorización); Parte 23, clase 6.

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

- Comisión para el Mercado Financiero (Chile). *Normativa del Sistema de Finanzas Abiertas de la Ley N.º 21.521*. CMF. <https://www.cmfchile.cl/>
- Bank for International Settlements (2019). *Report on open banking and application programming interfaces*. Basel Committee on Banking Supervision. <https://www.bis.org/bcbs/publ/d486.htm>
- Financial Stability Board (2019). *BigTech in finance: market developments and potential financial stability implications*. FSB. <https://www.fsb.org/2019/12/bigtech-in-finance-market-developments-and-potential-financial-stability-implications/>
- OpenID Foundation. *FAPI — Financial-grade API security profile*. <https://openid.net/wg/fapi/>
- Parlamento Europeo y Consejo. *Directiva (UE) 2015/2366 sobre servicios de pago en el mercado interior (PSD2)*. <https://eur-lex.europa.eu/eli/dir/2015/2366/oj>
- Verificación local: comprueba qué norma regula las finanzas abiertas en tu país, en qué fase de despliegue está y qué figuras contempla. **Fecha de verificación de esta clase: 2026-08-06.** Esta clase no constituye asesoría legal.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← Índice de la parte](../README.md) | [Parte 17](../README.md) · [Programa](../../../SYLLABUS.md) | [02 · Ecosistema, participantes y modelos de implantación →](02-ecosistema-participantes-y-modelos-de-implantacion.md) |
<!-- gen:footer:end -->
