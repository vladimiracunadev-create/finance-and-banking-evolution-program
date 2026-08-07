<!-- meta
part: 22
class: 13
title: "Protección de datos y economía de la información"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [chile, union-europea, internacional]
regulatory_topics: [proteccion-de-datos, privacidad, economia-de-datos]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [OCDE, CMF, EDPB]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 13 · Protección de datos y economía de la información

> [← 12 · Prevención de lavado y financiamiento del terrorismo](12-prevencion-de-lavado-y-financiamiento.md) · [Índice de la parte](../README.md) · [14 · Resiliencia operativa y terceros críticos →](14-resiliencia-operativa-y-terceros-criticos.md)

**Parte 22 — Regulación de mercados financieros digitales** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Resolver la tensión entre dos obligaciones que se contradicen: **la norma de
datos exige poder borrar y la de prevención exige conservar**, y un registro
distribuido no permite borrar nada.

Esta clase cierra el bloque de conducta que empezó en la clase 11. Allí vimos qué
protege la integridad del mercado; en la 12, qué obliga a conocer al cliente.
Ahora vemos el reverso de esa misma moneda: todo ese conocimiento son datos
personales, y tenerlos también obliga.

Los registros de las clases anteriores son compartidos e inmutables. Esta clase enfrenta esa característica con el derecho de supresión, y muestra que el conflicto se resuelve en la arquitectura y no en la política de privacidad.

## 📚 Objetivos

Al finalizar podrás:

1. **Identificar** qué datos de un registro son datos personales.
2. **Resolver** la contradicción entre supresión y conservación.
3. **Determinar** quién es responsable del tratamiento en una cadena de
   servicios.
4. **Diseñar** un tratamiento que minimice el dato desde el origen.
5. **Evaluar** el valor económico de los datos y qué límites tiene su uso.

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

Los cuatro primeros términos son el dato y sus grados de protección; los cuatro siguientes, los roles y los derechos. La distinción entre **seudonimización y anonimización** es la que decide el régimen: un dato seudonimizado sigue siendo personal y le aplica todo, y en un registro público la reidentificación suele ser posible.

| Concepto | Comprensión verificable |
|---|---|
| `dato personal` | El que identifica o hace identificable a una persona |
| `seudonimización` | Sustituir el identificador sin eliminar la vinculación |
| `anonimización` | Eliminar la posibilidad de reidentificar |
| `responsable` | Quien decide los fines y los medios del tratamiento |
| `encargado` | Quien trata por cuenta del responsable |
| `base de licitud` | Motivo jurídico que permite tratar |
| `minimización` | Tratar solo lo necesario para el fin |
| `derecho de supresión` | Facultad de pedir el borrado |

## 🧠 Modelo mental

El modelo mental es un choque entre dos exigencias: la norma de datos reconoce el derecho de supresión y un registro inmutable no puede borrar. Resolverlo exige no escribir datos personales en el registro, y eso es una decisión de arquitectura.

Antes de entrar en la contradicción conviene fijar un punto que casi siempre se
discute mal. Una dirección de un registro parece un dato anónimo: es una cadena
de caracteres sin nombre. Pero el dato personal no se define por cómo se ve, sino
por si permite llegar a una persona.

```text
UNA DIRECCIÓN ES UN DATO PERSONAL
CUANDO ALGUIEN PUEDE VINCULARLA
A UNA PERSONA

  · el proveedor que la abrió sabe quién es
  · el análisis de patrones puede deducirlo
  · una operación con un comercio la revela

  → ES SEUDÓNIMA, NO ANÓNIMA

Y LA DIFERENCIA IMPORTA
  el dato seudónimo sigue siendo dato personal
  y le aplica todo el régimen
```

De ahí nace el problema central de la clase, y conviene enunciarlo entero antes
de intentar resolverlo:

```text
LA CONTRADICCIÓN

  NORMA DE DATOS      derecho de supresión
  NORMA DE PREVENCIÓN conservar N años
  REGISTRO            no se puede borrar

  TRES OBLIGACIONES QUE NO CABEN JUNTAS
```

## 📖 Desarrollo

### 1. Cómo se resuelve la contradicción

La contradicción no se resuelve eligiendo qué norma incumplir. Se resuelve
cambiando **qué se escribe en el registro**, y esa decisión hay que tomarla antes
de la primera operación, porque después ya no hay marcha atrás.

```text
REGLA DE DISEÑO
  el registro guarda el MÍNIMO indispensable
  y el dato personal vive fuera, en un sistema
  donde sí se puede borrar

QUÉ VA AL REGISTRO
  · un identificador sin significado
  · el importe y el momento
  · la referencia de la operación

QUÉ NO VA NUNCA
  · nombre, documento de identidad, domicilio
  · concepto libre escrito por el cliente
  · cualquier dato que identifique por sí solo
```

El derecho de supresión se ejerce entonces sobre el sistema externo: se borra la
vinculación entre el identificador y la persona, y lo que queda en el registro
deja de ser un dato personal para quien ya no tiene la tabla. La conservación
exigida por la norma de prevención se cumple manteniendo esa tabla durante el
plazo legal y borrándola después.

### 2. Responsable y encargado

Determinar quién responde es la segunda pregunta que se resuelve mal, y tiene
consecuencias directas: el responsable es quien atiende los derechos del cliente,
notifica las brechas y responde ante la autoridad.

```text
RESPONSABLE  decide para qué y cómo se tratan
ENCARGADO    trata por cuenta del responsable

EN UNA CADENA DE SERVICIOS
  la plataforma que capta al cliente
  suele ser responsable

  el proveedor de infraestructura
  suele ser encargado

  Y EL PROVEEDOR DE ANÁLISIS DE RIESGO
  puede ser CORRESPONSABLE, si decide
  por su cuenta qué modelos aplica
```

El error habitual es firmar un contrato de encargado con quien en realidad decide
los fines. Si el proveedor elige qué datos analizar y con qué finalidad, es
responsable aunque el contrato diga otra cosa: aquí también la sustancia manda
sobre la forma, igual que en la clase 3.

### 3. Minimización desde el origen

La minimización se suele entender como borrar lo que sobra. Es mucho más barato
entenderla como no pedirlo.

```text
PARA CADA DATO QUE SE RECOGE

  1 ¿para qué fin concreto?
  2 ¿ese fin es lícito?
  3 ¿el dato es necesario para ese fin,
    o solo útil?
  4 ¿cuánto tiempo hace falta conservarlo?
  5 ¿quién debe poder verlo?

EL PUNTO 3 ES EL QUE ELIMINA DATOS
  «útil» no es «necesario», y casi todo
  lo que se recoge de más entra por ahí
```

### 4. El valor económico y su límite

Los datos de pago describen la vida de una persona con una precisión que ningún
otro registro alcanza: dónde está, con quién se relaciona, qué consume y cuándo
cambia de hábitos. Eso los hace valiosos y por eso su uso tiene límites que no
son negociables con el cliente.

```text
USOS QUE SUELEN ADMITIRSE
  · prestar el servicio contratado
  · cumplir obligaciones legales
  · prevenir el fraude
  · mejorar el propio servicio, agregado

USOS QUE EXIGEN BASE ESPECÍFICA
  · publicidad personalizada
  · cesión a terceros
  · elaboración de perfiles con efecto
    jurídico sobre la persona

Y UNO QUE NO SE SALVA CON EL CONSENTIMIENTO
  condicionar el servicio a aceptar un uso
  que no es necesario para prestarlo
```

El último punto es el que más se incumple. Un consentimiento que el cliente no
puede negar sin perder el servicio no es libre, y un consentimiento que no es
libre no es una base de licitud válida.

### 5. Decisiones automatizadas

Buena parte de lo que decide una plataforma sobre un cliente —si le abre cuenta,
si le bloquea una operación, si le concede crédito— lo decide un modelo. Cuando
esa decisión produce efectos jurídicos o afecta significativamente a la persona,
el régimen de datos exige tres cosas.

```text
  1 INFORMACIÓN sobre la lógica aplicada
  2 INTERVENCIÓN HUMANA a petición
  3 DERECHO A IMPUGNAR la decisión

Y LA SEGUNDA ES LA QUE SE INCUMPLE
  una revisión humana que se limita a
  confirmar la salida del modelo no es
  intervención: es un sello
```

## 🧮 Ejemplo guiado

El ejemplo evalúa si un dato de un registro público es personal. La seudonimización no basta cuando el patrón de operaciones identifica.

**Situación.** Una plataforma registra en el registro distribuido el concepto que
el cliente escribe en cada operación. Un cliente ejerce su derecho de supresión.
Hay que determinar qué se puede hacer y qué costó la decisión de diseño.

```text
DATOS
  operaciones registradas             4 100 000
  con concepto libre                    980 000
  clientes                               42 000
  solicitudes de supresión al año           310
  plazo legal de conservación             5 años
  coste de atender una solicitud             65
```

**Paso 1 — determina qué hay en el registro.**

```text
EL CONCEPTO LIBRE CONTIENE, EN LA MUESTRA
REVISADA DE 500 OPERACIONES

  · 118 con nombre de persona
  · 46 con número de documento
  · 31 con referencia a un tratamiento médico
  · 9 con dirección postal

  → EL 40,8 % CONTIENE DATO PERSONAL
    y 31 contienen dato de salud, que tiene
    protección reforzada

EXTRAPOLADO A 980 000 OPERACIONES
  ≈ 400 000 con dato personal en el registro
```

**Paso 2 — comprueba si se puede borrar.**

```text
EL REGISTRO ES INMUTABLE POR DISEÑO

  · no se puede borrar una entrada
  · reescribir la cadena entera es
    técnicamente posible y jurídicamente
    irrelevante: el dato ya se difundió

  → EL DERECHO DE SUPRESIÓN NO SE PUEDE
    SATISFACER SOBRE EL REGISTRO
```

**Paso 3 — busca la respuesta que sí existe.**

```text
LO QUE SÍ SE PUEDE HACER

  · borrar la vinculación identificador-persona
    en los sistemas de la plataforma
  · dejar de tratar el dato del registro
  · comunicar a los encargados que cesen

  QUÉ NO RESUELVE
  el dato sigue en el registro y cualquiera
  que conserve la tabla de vinculación puede
  reidentificar

  → LA RESPUESTA AL CLIENTE TIENE QUE DECIR
    ESTO, no «hemos borrado sus datos»
```

**Paso 4 — cuantifica el coste de la decisión original.**

```text
COSTE DIRECTO DE LAS SOLICITUDES
  310 × 65 = 20 150 al año

COSTE DEL RIESGO
  · el tratamiento de 400 000 datos personales
    sin base de licitud clara
  · 31 por cada 500 son datos de salud
    → extrapolado, ≈ 60 800 operaciones
      con dato de protección reforzada

  supuesto de sanción por tratamiento
  indebido de categoría especial: no se
  estima aquí porque depende de la
  jurisdicción y del caso

  LO QUE SÍ SE PUEDE AFIRMAR
  la plataforma no puede satisfacer un
  derecho que la norma reconoce, y eso
  es un incumplimiento continuado
```

**Paso 5 — rediseña.**

```text
CAMBIO 1 · EL CONCEPTO NO VA AL REGISTRO
  se guarda en la base de datos de la
  plataforma, vinculado por referencia
  coste supuesto: 34 000 de desarrollo

CAMBIO 2 · VALIDACIÓN EN LA ENTRADA
  se rechaza cualquier concepto que
  contenga patrones de documento o de
  nombre propio
  coste supuesto: 12 000

CAMBIO 3 · CALENDARIO DE BORRADO
  la vinculación se conserva 5 años y se
  borra automáticamente
  coste supuesto: 8 000

CAMBIO 4 · RESPUESTA HONESTA AL CLIENTE
  plantilla que explica qué se borra y
  qué permanece
  coste: una tarde

TOTAL 54 000 UNA VEZ

Y NADA DE ESTO SE PUEDE APLICAR
RETROACTIVAMENTE A LAS 400 000
OPERACIONES YA REGISTRADAS.
```

**Paso 6 — extrae la regla general.**

```text
LO QUE ESTA CLASE DEJA COMO CRITERIO

  antes de escribir el primer dato en un
  registro inmutable, hay que responder:
  «si mañana alguien pide que lo borremos,
   ¿qué le contestamos?»

  · si la respuesta es «no podemos»,
    ese dato no debe ir al registro
  · y la decisión cuesta 54 000 antes
    de empezar y es imposible después
```

**Interpreta:** el error no fue técnico ni jurídico, fue de secuencia. **Nadie
preguntó qué pasaría con el derecho de supresión antes de decidir qué se
escribía en el registro**, y esa pregunta cuesta una reunión antes de empezar y
no tiene respuesta después de cuatro millones de operaciones.

## 🧭 Perspectivas

La protección de datos afecta a cada participante de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | «Hemos borrado sus datos» | Si lo cree |
| Plataforma | Un derecho que no puede satisfacer | Qué responde |
| Encargado | Instrucción de cesar el tratamiento | Cómo la ejecuta |
| Proveedor de análisis | Decide qué modelos aplica | Si es responsable |
| Banco | Datos de sus clientes en un registro | Qué exige |
| Autoridad de datos | Tratamiento sin base clara | Qué requiere |
| Supervisor financiero | Conservación exigida | Cómo se concilia |
| Auditor | Datos de salud en el registro | Qué revela |
| Sociedad | Su vida en un libro público | Qué protección exige |

## 🏦 Del cliente al banco

El cliente pide que borren sus datos y el registro es inmutable. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Borren mis datos» | Se borra la vinculación, no el registro | 22, clase 13 |
| «Es una dirección anónima» | Es seudónima, y sigue siendo dato personal | 22, clase 13 |
| «Acepté los términos» | Un consentimiento forzado no es libre | 22, clase 13 |

## ⚖️ Riesgos y controles

Los riesgos son de reidentificación y de derechos no ejercitables. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Dato personal en el registro | Concepto libre con nombres | Validación en la entrada |
| Supresión imposible | El registro es inmutable | Dato personal fuera, por referencia |
| Contrato de encargado incorrecto | El proveedor decide los fines | Determinar el rol por los hechos |
| Consentimiento no libre | Se condiciona el servicio | Base de licitud distinta |
| Revisión humana simbólica | Se confirma la salida del modelo | Capacidad real de cambiar la decisión |
| Conservación sin calendario | Se guarda indefinidamente | Borrado automático al vencer el plazo |

## 🧪 Práctica

El laboratorio pide evaluar la reidentificación de datos seudonimizados. El resultado obliga a rediseñar qué se escribe en el registro.

En [`labs/lab-05.md`](../labs/lab-05.md):

1. Clasifica qué campos de un registro son datos personales.
2. Diseña el reparto entre registro y sistema externo.
3. Redacta la respuesta honesta a una solicitud de supresión.
4. Determina el rol de cada actor de la cadena.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen conflictos entre inmutabilidad y protección de datos. La causa es haber escrito datos personales en el registro.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Creer que una dirección es anónima | No lleva nombre | Es seudónima si alguien puede vincularla |
| Escribir texto libre en el registro | Es cómodo para el cliente | Validar y guardarlo fuera |
| «Hemos borrado sus datos» | Es la respuesta esperada | Explicar qué permanece |
| Contrato de encargado por defecto | Es la plantilla habitual | El rol lo dan los hechos |
| Consentimiento para todo | Es la base más fácil | Si no es libre, no vale |
| Revisión humana formal | Cumple el requisito escrito | Debe poder cambiar la decisión |

## ❓ Preguntas de comprobación

1. ¿Cuándo una dirección de un registro es un dato personal?
2. ¿Cómo se resuelve la contradicción entre supresión, conservación e
   inmutabilidad?
3. ¿Qué distingue a un responsable de un encargado, y qué pasa si el contrato
   dice otra cosa?
4. ¿Por qué un consentimiento condicionado al servicio no es válido?
5. ¿Qué pregunta hay que responder antes de escribir el primer dato en un
   registro inmutable?

## 📥 Entregable

Guarda en `portfolio/parte-22/clase-13/`:

- la clasificación de campos por su condición de dato personal;
- el diseño de reparto entre registro y sistema externo;
- la respuesta honesta a una solicitud de supresión;
- el mapa de roles de la cadena, con su fundamento.

## 🔗 Referencias cruzadas

- **Viene de:** clases 11 y 12; Parte 17, clase 10; Parte 19, clase 10.
- **Continúa en:** clase 14 de esta parte.
- **Se aplica en:** clase 18 de esta parte; Parte 23, clase 13.

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

- OCDE (2013). *Guidelines governing the Protection of Privacy and Transborder Flows of Personal Data*. OECD. <https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0188>
- Diario Oficial de la Unión Europea (2016). *Reglamento (UE) 2016/679, general de protección de datos*. EUR-Lex. <https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32016R0679>
- Biblioteca del Congreso Nacional de Chile. *Ley 19.628 sobre protección de la vida privada*. <https://www.bcn.cl/leychile/navegar?idNorma=141599>
- Financial Action Task Force (2021). *Updated Guidance for a Risk-Based Approach to Virtual Assets and VASPs*. FATF. <https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-rba-virtual-assets-2021.html>
- Verificación local: comprueba qué régimen de datos personales aplica en tu jurisdicción, qué plazos de conservación impone la norma de prevención y cómo se concilian ambos. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 12 · Prevención de lavado y financiamiento del terrorismo](12-prevencion-de-lavado-y-financiamiento.md) | [Parte 22](../README.md) · [Programa](../../../SYLLABUS.md) | [14 · Resiliencia operativa y terceros críticos →](14-resiliencia-operativa-y-terceros-criticos.md) |
<!-- gen:footer:end -->
