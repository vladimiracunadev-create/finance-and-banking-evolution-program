<!-- meta
part: 17
class: 11
title: "Autenticación reforzada, fraude y responsabilidad"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global, chile, union-europea]
regulatory_topics: [open-finance, autenticacion, fraude, proteccion-al-consumidor]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [CMF, SERNAC]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 11 · Autenticación reforzada, fraude y responsabilidad

> [← 10 · Iniciación de pagos y confirmación de fondos](10-iniciacion-de-pagos-y-confirmacion-de-fondos.md) · [Índice de la parte](../README.md) · [12 · Privacidad, finalidad, minimización y portabilidad →](12-privacidad-finalidad-y-portabilidad.md)

**Parte 17 — Finanzas abiertas, APIs y economía de datos** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Responder la pregunta que llega después de cada fraude: **¿quién paga?** Y
mostrar que la respuesta no se decide en el momento del reclamo, sino en el
diseño de la autenticación y de la evidencia meses antes.

La iniciación de pagos de la clase anterior abre una vía nueva para el fraude. Esta la cierra con autenticación reforzada y, sobre todo, reparte la responsabilidad de antemano entre tres actores, porque discutirla caso a caso no funciona.

## 📚 Objetivos

Al finalizar podrás:

1. **Aplicar** el criterio de los tres factores y detectar cuándo dos «factores»
   son en realidad el mismo.
2. **Distinguir** operación no autorizada de operación autorizada y luego
   arrepentida, y de fraude por manipulación del cliente.
3. **Construir** la matriz de responsabilidad entre cliente, iniciador e
   institución.
4. **Especificar** la evidencia que decide un reclamo.
5. **Evaluar** el equilibrio entre fricción y fraude con números.

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

Los cuatro primeros términos son la autenticación y sus requisitos; los cuatro siguientes, el fraude y su reparto de responsabilidad. La **vinculación dinámica** es el requisito que impide el fraude más eficaz: el código de autenticación tiene que estar ligado al importe y al destinatario concretos.

| Concepto | Comprensión verificable |
|---|---|
| `autenticación reforzada` | Verificación con al menos dos factores de categorías distintas e independientes |
| `factor` | Algo que se sabe, algo que se tiene, algo que se es |
| `independencia` | La vulneración de un factor no compromete al otro |
| `vinculación dinámica` | El código de autenticación depende del importe y del beneficiario |
| `operación no autorizada` | El cliente no la ordenó ni la consintió |
| `fraude por manipulación` | El cliente autoriza engañado por un tercero |
| `carga de la prueba` | A quién corresponde demostrar qué |
| `exención` | Supuesto en que la norma permite no aplicar autenticación reforzada |

## 🧠 Modelo mental

El modelo mental es una cadena de tres actores donde el fraude puede ocurrir en cualquiera y la responsabilidad recae según reglas previas. Sin esas reglas escritas, cada caso se discute desde cero.

```text
LA PREGUNTA NO ES «¿HUBO FRAUDE?»
LA PREGUNTA ES «¿QUÉ PUEDE DEMOSTRAR CADA PARTE?»

  el cliente dice        «yo no lo hice»
  la institución dice    «se autenticó correctamente»

  QUIÉN GANA DEPENDE DE
    1. si la autenticación era reforzada de verdad
    2. si estaba vinculada al importe y al beneficiario
    3. si la evidencia registrada reconstruye el acto
    4. de quién es la carga de la prueba según la norma

  UN REGISTRO QUE DICE «autenticado: true»
  NO DEMUESTRA NADA
```

## 📖 Desarrollo

### 1. Los tres factores y la trampa de la independencia

```text
CONOCIMIENTO   contraseña, PIN, respuesta secreta
POSESIÓN       dispositivo registrado, tarjeta, llave física
INHERENCIA     huella, rostro, voz

REGLA: DOS CATEGORÍAS DISTINTAS Y MUTUAMENTE INDEPENDIENTES

LA TRAMPA MÁS FRECUENTE
  «contraseña + código por SMS al teléfono»
  parece conocimiento + posesión

  PERO si el atacante controla el teléfono:
    · lee el SMS                → rompe la posesión
    · ve la contraseña guardada → rompe el conocimiento
  → un solo compromiso rompe los dos factores
  → NO son independientes

OTRAS COMBINACIONES QUE FALLAN LA INDEPENDENCIA
  · contraseña + pregunta secreta      (dos veces conocimiento)
  · huella + rostro del mismo teléfono (misma superficie)
  · código en la app + contraseña en el gestor del mismo dispositivo
```

### 2. Vinculación dinámica

```text
SIN VINCULACIÓN
  el código autentica AL USUARIO
  → sirve para cualquier operación durante su validez
  → un atacante que obtiene el código lo usa para otra cosa

CON VINCULACIÓN
  el código se calcula sobre importe + beneficiario
  → si el atacante cambia cualquiera de los dos,
    el código deja de ser válido

Y ADEMÁS: LO QUE SE MUESTRA AL CLIENTE
  «Confirma 45.000 a JUAN PEREZ, código 481920»
  el cliente ve QUÉ está autorizando

  frente a
  «Tu código es 481920»
  que autoriza cualquier cosa
```

### 3. Tres cosas que no son lo mismo

| Situación | Qué pasó | Quién soporta, por defecto |
|---|---|---|
| Operación no autorizada | El cliente no participó | La institución, salvo prueba en contrario |
| Operación autorizada y arrepentida | El cliente ordenó y se arrepintió | El cliente |
| Fraude por manipulación | El cliente autorizó, engañado | El caso más disputado |

```text
EL TERCERO ES EL QUE CRECE

  el atacante no rompe la criptografía:
  convence al cliente de que la use

  «soy del banco, hay un cargo fraudulento,
   para bloquearlo confirma con tu app»

  técnicamente: autenticación reforzada superada,
  vinculación dinámica correcta, evidencia impecable
  materialmente: el cliente fue engañado

  → los controles técnicos NO resuelven este caso.
    Lo mitigan el diseño del mensaje, las alertas,
    los límites por comportamiento y la educación.
```

### 4. La evidencia que decide un reclamo

```text
MÍNIMO PARA SOSTENER «la operación fue autorizada»

   1. método de autenticación empleado, por factor
   2. instante de cada factor, con zona horaria
   3. identificador del dispositivo y su antigüedad de registro
   4. texto EXACTO mostrado al cliente al confirmar
   5. importe y beneficiario vinculados al código
   6. resultado de los controles antifraude y su puntuación
   7. canal e identificadores de sesión y de petición
   8. si hubo exención aplicada, cuál y por qué

EL PUNTO 4 ES EL QUE FALTA CASI SIEMPRE
  sin él, no se puede rebatir «yo confirmé otra cosa»
```

### 5. La matriz de responsabilidad

```text
TRES PARTES: cliente, iniciador, institución de la cuenta

  ¿HUBO AUTENTICACIÓN REFORZADA VÁLIDA?
    NO  → responde quien debía aplicarla
    SÍ  ↓

  ¿ESTABA VINCULADA AL IMPORTE Y BENEFICIARIO EJECUTADOS?
    NO  → responde quien ejecutó algo distinto de lo confirmado
    SÍ  ↓

  ¿EL CLIENTE ACTUÓ CON NEGLIGENCIA GRAVE O DOLO?
    SÍ  → puede responder el cliente
    NO  ↓

  ¿EL FALLO ESTÁ EN EL INICIADOR O EN LA INSTITUCIÓN?
    → la institución suele responder frente al cliente
      y repetir contra quien corresponda

EL DETALLE QUE DECIDE
  «negligencia grave» no es «se dejó engañar».
  El umbral concreto lo fija la norma y la jurisprudencia
  local: verifícalo, no lo supongas.
```

## 🧮 Ejemplo guiado

El ejemplo reparte la responsabilidad de un fraude concreto entre los tres actores. Conviene aplicar la carga de la prueba: quién tiene que demostrar qué decide la mayoría de los casos.

**Situación.** Una institución revisa 1 000 reclamos de operaciones disputadas del
trimestre para decidir su política de autenticación.

```text
CLASIFICACIÓN DE LOS 1 000 RECLAMOS
  operación no autorizada, sin autenticación válida        62
  operación no autorizada, con autenticación válida       118
  autorizada y arrepentida                                 94
  fraude por manipulación del cliente                     641
  sin determinar                                           85

IMPORTE MEDIO DISPUTADO                              184 000
COSTE DE GESTIÓN POR RECLAMO                          38 000
```

**Paso 1 — separa lo que el control técnico puede resolver.**

```text
RESOLUBLE CON CONTROL TÉCNICO
   62  sin autenticación válida        → aplicar bien la norma
  118  con autenticación válida        → revisar si era reforzada
                                          de verdad e independiente

NO RESOLUBLE CON CONTROL TÉCNICO
  641  manipulación del cliente        → 64,1 % del total
   94  arrepentimiento                 → no es fraude
   85  sin determinar                  → mejorar la evidencia
```

**Paso 2 — investiga los 118.**

```text
DE LOS 118 CON «AUTENTICACIÓN VÁLIDA»
  segundo factor por SMS al mismo teléfono
  donde estaba la app y la contraseña guardada:  91

  → esos 91 NO eran autenticación reforzada:
    eran dos factores sin independencia

RECLASIFICACIÓN
  62 + 91 = 153 casos de autenticación insuficiente
  quedan 27 con autenticación genuinamente independiente
```

**Paso 3 — calcula el coste de los 153.**

```text
153 × 184 000 = 28 152 000  en importe disputado
153 ×  38 000 =  5 814 000  en gestión
TOTAL                        33 966 000 en el trimestre
ANUALIZADO                  135 864 000
```

**Paso 4 — evalúa la corrección técnica.**

```text
SUSTITUIR EL SMS POR APP CON CLAVE EN EL ELEMENTO SEGURO
DEL DISPOSITIVO, CON VINCULACIÓN DINÁMICA

  COSTE
    desarrollo e integración                 42 000 000
    migración de 1,4 M de clientes           28 000 000
    soporte del primer año                   19 000 000
    TOTAL PRIMER AÑO                         89 000 000

  BENEFICIO
    elimina los 91 por dependencia de canal
    reduce parcialmente los 62
    supuesto: 70 % de reducción de los 153
    153 × 70 % = 107 casos/trimestre evitados
    107 × 222 000 = 23 754 000 por trimestre
    ANUALIZADO                               95 016 000

  PRIMER AÑO: 95 016 000 − 89 000 000 = +6 016 000
  AÑOS SIGUIENTES: ahorro casi íntegro
```

**Paso 5 — enfrenta el problema real, que es el 64,1 %.**

```text
641 CASOS DE MANIPULACIÓN
  641 × 222 000 = 142 302 000 por trimestre
  ANUALIZADO ≈ 569 208 000

  CUATRO VECES el problema técnico

MEDIDAS QUE SÍ ACTÚAN SOBRE ESTE CASO
  1. mensaje de confirmación en lenguaje de consecuencia
     «vas a ENVIAR 850.000 a una cuenta NUEVA.
      El banco nunca te pide hacer esto.»
  2. retardo obligatorio en el primer pago a un beneficiario
     nuevo por encima de un umbral
  3. límite por comportamiento: importe muy fuera del patrón
     → verificación adicional por canal distinto
  4. alerta al cliente por canal independiente
  5. confirmación de nombre del beneficiario contra el
     titular real de la cuenta destino
```

**Paso 6 — evalúa la medida 2 con la fricción que introduce.**

```text
RETARDO DE 30 MINUTOS EN EL PRIMER PAGO A BENEFICIARIO
NUEVO POR ENCIMA DE 300 000

  OPERACIONES AFECTADAS: 4,1 % del total
  DE ELLAS, LEGÍTIMAS: 99,3 %

  COSTE DE FRICCIÓN
    supuesto: 2,8 % de las afectadas se abandona
    4,1 % × 2,8 % = 0,115 % de las operaciones
    valor perdido estimado por trimestre:  11 400 000

  BENEFICIO
    de los 641 casos, 388 eran a beneficiario nuevo
    por encima de 300 000
    supuesto: el retardo + alerta evita el 45 %
    388 × 45 % = 175 casos
    175 × 222 000 = 38 850 000 por trimestre

  NETO: +27 450 000 por trimestre
```

**Paso 7 — formula la política.**

```text
POLÍTICA APROBADA

  TÉCNICA
    · migrar el segundo factor fuera del canal SMS
    · vinculación dinámica obligatoria en todo pago
    · mostrar importe y beneficiario en la confirmación
    · registrar los ocho elementos de evidencia

  DE COMPORTAMIENTO
    · retardo de 30 min en primer pago a beneficiario nuevo
      sobre 300 000, con alerta por canal independiente
    · confirmación de nombre del beneficiario

  DE PROCESO
    · reclasificar los 85 «sin determinar» tras mejorar
      la evidencia, y volver a medir en 90 días

  Y UNA DECISIÓN EXPLÍCITA SOBRE LOS 641
    la institución NO puede resolver la manipulación
    solo con tecnología. Se asume que una parte
    seguirá ocurriendo, se documenta el criterio de
    reparto y se comunica al cliente antes del incidente,
    no después.
```

**Interpreta:** el 64,1 % de los reclamos no lo resolvía ningún control
criptográfico. La decisión importante no fue elegir un factor mejor: fue **medir
que el problema estaba en otro sitio** y actuar allí, sin dejar de corregir lo
técnico.

## 🧭 Perspectivas

El fraude afecta a cada actor con consecuencias distintas. La tabla las recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un cargo que no reconoce | Si reclama |
| Comercio | Devoluciones | Si acepta el método |
| Iniciador | Reclamos que le repiten | Qué evidencia guarda |
| Banco | 1 000 reclamos y su coste | Qué política adopta |
| Supervisor | Tasa de fraude por método | Qué exige |
| Auditor | Evidencia de autenticación | Si sostiene la posición del banco |
| Sociedad | Fraude por manipulación creciente | Educación y responsabilidad compartida |

## 🏦 Del cliente al banco

El cliente desconoce una operación y el banco aplica un reparto de responsabilidad con reglas previas. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Yo no hice esa transferencia» | Operación no autorizada: carga de la prueba | 17, clase 11 |
| «Me llamaron del banco» | Manipulación: control técnico no aplica | 17, clase 11 |
| «Confirmé otra cosa» | Vinculación dinámica y texto mostrado | 17, clase 11 |
| «Me pide esperar 30 minutos» | Retardo por beneficiario nuevo | 17, clase 11 |

## ⚖️ Riesgos y controles

Los riesgos son de autenticación y de reparto. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Factores no independientes | SMS al mismo dispositivo | Factor fuera del canal |
| Código reutilizable | Sin vinculación dinámica | Código sobre importe y beneficiario |
| Evidencia insuficiente | «autenticado: true» | Los ocho elementos |
| Manipulación del cliente | Ingeniería social | Retardo, alerta y confirmación de nombre |
| Exención mal aplicada | Se omitió la autenticación | Registrar cuál y por qué |
| Fricción excesiva | Se blindó todo | Medir abandono frente a fraude evitado |

## 🧪 Práctica

En [`labs/lab-02.md`](../labs/lab-02.md) y [`labs/lab-06.md`](../labs/lab-06.md):

1. Evalúa cinco combinaciones de factores y di cuáles fallan la independencia.
2. Implementa la vinculación dinámica y demuestra que alterar el importe invalida.
3. Construye la matriz de responsabilidad para tres casos concretos.
4. Calcula el equilibrio entre fricción y fraude con los datos del ejercicio.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen fraudes mal repartidos. Las causas son vinculación dinámica ausente y carga de la prueba mal aplicada.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| SMS como segundo factor | Se contó la categoría, no la independencia | Factor fuera del canal comprometido |
| Código no vinculado | Se autenticó al usuario, no la operación | Vinculación dinámica |
| Evidencia booleana | Se registró el resultado | Ocho elementos con el texto mostrado |
| Todo fraude tratado igual | No se clasificó | Tres categorías distintas |
| Solo controles técnicos | Se ignoró la manipulación | Medidas de comportamiento |
| Fricción sin medir | Se priorizó la seguridad sin dato | Compara abandono y fraude evitado |

## ❓ Preguntas de comprobación

1. ¿Por qué «contraseña + SMS» puede no ser autenticación reforzada?
2. ¿Qué añade la vinculación dinámica y qué ataque concreto corta?
3. ¿Cuáles son las tres situaciones distintas que se confunden bajo «fraude»?
4. ¿Cuál de los ocho elementos de evidencia falta con más frecuencia y qué se
   pierde sin él?
5. En el ejemplo guiado, ¿por qué la mejor medida técnica no era la más rentable?

## 📥 Entregable

Guarda en `portfolio/parte-17/clase-11/`:

- la evaluación de cinco combinaciones de factores por independencia;
- la matriz de responsabilidad aplicada a tres casos;
- la especificación de los ocho elementos de evidencia;
- el cálculo de fricción frente a fraude evitado, con tu decisión.

## 🔗 Referencias cruzadas

- **Viene de:** clase 6 (autorización), clase 10 (iniciación de pagos);
  Parte 3, clase 8 (fraude); Parte 14, clase 8 (fraude digital).
- **Continúa en:** clase 13 (incidentes), clase 12 (privacidad).
- **Se aplica en:** Parte 18, clase 12 (AML y sanciones); Parte 23, clase 15.

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

- Parlamento Europeo y Consejo. *Reglamento Delegado (UE) 2018/389 sobre autenticación reforzada de clientes y comunicación segura*. <https://eur-lex.europa.eu/eli/reg_del/2018/389/oj>
- European Banking Authority. *Opinion and guidelines on strong customer authentication*. EBA. <https://www.eba.europa.eu/>
- NIST (2017, con revisiones posteriores). *SP 800-63B — Digital Identity Guidelines: Authentication and Lifecycle Management*. NIST. <https://pages.nist.gov/800-63-3/sp800-63b.html>
- Comisión para el Mercado Financiero. *Normativa sobre gestión de la seguridad de la información y fraude en medios de pago*. CMF. <https://www.cmfchile.cl/>
- Financial Action Task Force. *Guidance on digital identity*. FATF. <https://www.fatf-gafi.org/>
- Verificación local: comprueba el régimen de operaciones no autorizadas, el umbral de negligencia grave y las exenciones admitidas en tu jurisdicción. **Fecha de verificación de esta clase: 2026-08-06.** Esta clase no constituye asesoría legal.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 10 · Iniciación de pagos y confirmación de fondos](10-iniciacion-de-pagos-y-confirmacion-de-fondos.md) | [Parte 17](../README.md) · [Programa](../../../SYLLABUS.md) | [12 · Privacidad, finalidad, minimización y portabilidad →](12-privacidad-finalidad-y-portabilidad.md) |
<!-- gen:footer:end -->
