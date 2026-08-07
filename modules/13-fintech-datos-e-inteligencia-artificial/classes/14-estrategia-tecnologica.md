<!-- meta
part: 14
class: 14
title: "Estrategia tecnológica"
level: profesional
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 14 · Estrategia tecnológica

> [← 13 · Transformación digital](13-transformacion-digital.md) · [Índice de la parte](../README.md) · [Proyecto de la parte →](../project/README.md)

**Parte 14 — Fintech, datos e inteligencia artificial** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Cerrar la parte con la decisión que la resume: **qué capacidades tecnológicas debe tener un banco propias
y cuáles debe comprar**. Es la decisión que determina su margen, su velocidad y su dependencia durante
la década siguiente, y se toma una y otra vez sin marco explícito.

Esta clase cierra la parte con la decisión que ordena todas las anteriores: qué construye el banco y qué compra. Y su criterio no es de costo sino de estrategia, porque una capacidad que diferencia y se compra deja de diferenciar en cuanto el competidor compra la misma.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** capacidades estratégicas de infraestructura.
2. **Aplicar** un marco de decisión de construir, comprar o asociarse.
3. **Evaluar** el riesgo de dependencia y de concentración de proveedores.
4. **Construir** el caso económico completo de una decisión tecnológica.
5. **Integrar** la estrategia tecnológica con la de negocio.

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

Los tres primeros términos son la clasificación y su costo; los cinco siguientes, la dependencia y su gobierno. El **plan de salida** es el requisito que rara vez se exige al contratar y que decide el coste real: sin él, la relación con el proveedor deja de ser una decisión.

| Concepto | Comprensión verificable |
|---|---|
| `capacidad estratégica` | Aquella que diferencia al banco o define su riesgo. |
| `capacidad de infraestructura` | Necesaria y no diferenciadora. |
| `costo total de propiedad` | Costo de una solución durante toda su vida útil. |
| `costo de cambio` | Costo de sustituir un proveedor. |
| `cautividad` | Situación en que el costo de cambio hace inviable salir. |
| `concentración de proveedores` | Dependencia del sector de pocos proveedores. |
| `plan de salida` | Procedimiento probado para dejar de usar un proveedor. |
| `arquitectura de referencia` | Modelo que orienta las decisiones individuales. |

## 🧠 Modelo mental

El modelo mental separa dos tipos de capacidad: las que diferencian al banco y las que son infraestructura. Las primeras se construyen aunque salgan caras, y las segundas se compran aunque construirlas sea posible. Confundirlas es lo que produce bancos que programan lo que podrían comprar y compran lo que los distinguía.

```text
LA PREGUNTA QUE ORDENA TODA DECISIÓN TECNOLÓGICA

  ¿ESTA CAPACIDAD NOS DIFERENCIA
   O SOLO NOS PERMITE OPERAR?

  DIFERENCIA           → construir o controlar
    modelo de riesgo propio
    experiencia del cliente
    datos y su explotación
    decisiones de precio

  PERMITE OPERAR       → comprar
    correo, ofimática, infraestructura de cómputo
    procesamiento de tarjetas
    verificación documental
    contabilidad general

EL ERROR MÁS CARO
  construir infraestructura, porque "es estratégica"
  y comprar la capacidad diferenciadora,
  porque "el proveedor sabe más"
```

## 📖 Desarrollo

### 1. Clasificación de capacidades

Las capacidades se clasifican por si diferencian o no. La tabla recoge el criterio.

| Capacidad | Clasificación habitual | Razón |
|---|---|---|
| Modelos de riesgo de crédito | Estratégica | Define el riesgo y el precio |
| Experiencia del cliente en canales | Estratégica | Define la relación |
| Motor de decisión y políticas | Estratégica | Es la política de negocio codificada |
| Gobierno y explotación de datos | Estratégica | Insumo de todo lo anterior |
| Núcleo bancario de registro | Intermedia | Necesario, no diferenciador, difícil de cambiar |
| Procesamiento de tarjetas | Infraestructura | Estandarizado |
| Verificación de identidad | Infraestructura | Estandarizado, con proveedores especializados |
| Infraestructura de cómputo | Infraestructura | Escala del proveedor imbatible |
| Antifraude | Intermedia | El motor se compra; las reglas son propias |
| Prevención de lavado | Intermedia | La herramienta se compra; la calibración es propia |

```text
EL PATRÓN DE LAS CAPACIDADES INTERMEDIAS
  se compra la HERRAMIENTA
  y se conserva la CONFIGURACIÓN, los DATOS
  y el CONOCIMIENTO de cómo usarla

  un banco que compra un motor antifraude
  y deja que el proveedor lo calibre
  ha externalizado su política de riesgo
```

### 2. Marco de decisión

La decisión de construir, comprar o asociarse sigue un marco con criterios en orden. La tabla lo recoge.

```text
CINCO PREGUNTAS, EN ORDEN

  1. ¿ES DIFERENCIADORA?
     si sí → construir o controlar; sigue en 5
     si no → sigue en 2

  2. ¿EXISTE UNA SOLUCIÓN MADURA EN EL MERCADO?
     si no → construir, y evaluar si es realmente necesaria

  3. ¿CUÁL ES EL COSTO TOTAL DE PROPIEDAD DE CADA OPCIÓN?
     incluye implantación, operación, evolución,
     personas, integración y salida

  4. ¿CUÁL ES EL COSTO DE CAMBIO Y EL RIESGO DE CAUTIVIDAD?
     si el costo de cambio es prohibitivo,
     el precio futuro lo fija el proveedor

  5. ¿TENEMOS LA CAPACIDAD DE EJECUTAR LA OPCIÓN ELEGIDA?
     construir sin equipo es la peor de las opciones
```

### 3. Costo total de propiedad

El costo total incluye implantación, operación, evolución y salida. El procedimiento lo calcula.

```text
COMPONENTES QUE SE OLVIDAN AL COMPARAR

  CONSTRUIR
    · desarrollo inicial
    · personas para mantenerlo, indefinidamente
    · rotación de esas personas y su reemplazo
    · evolución funcional continua
    · el costo de oportunidad de esas personas
    · el riesgo de que el equipo clave se vaya

  COMPRAR
    · licencia y su escalamiento con el volumen
    · implantación e integración
    · personalización y sus límites
    · actualizaciones obligatorias
    · dependencia del calendario del proveedor
    · costo de salida
```

```text
LA ASIMETRÍA DE HORIZONTE
  las comparaciones se hacen a 3 años
  y las decisiones duran 10 o 15

  a 3 años, comprar casi siempre gana
  a 10 años, la respuesta depende del volumen
  y del costo de cambio
```

### 4. Dependencia y concentración

La dependencia de un proveedor y la concentración del sector son dos riesgos distintos. La tabla los separa, y esta idea reaparece en las Partes 17 y 22.

```text
TRES NIVELES DE RIESGO DE PROVEEDOR

  DEPENDENCIA        el proveedor es necesario para operar
    mitigante: plan de salida probado

  CAUTIVIDAD         el costo de cambio hace inviable salir
    mitigante: portabilidad contractual de datos y lógica,
               arquitectura que aísle al proveedor

  CONCENTRACIÓN      todo el sector depende del mismo proveedor
    mitigante: ninguno a nivel de un banco individual
               → es un riesgo sistémico, y por eso
                 los supervisores vigilan directamente
                 a los proveedores críticos (clase 12)
```

| Cláusula contractual | Qué protege |
|---|---|
| Portabilidad de datos en formato abierto | Salida posible |
| Derecho de auditoría | Verificación, no confianza |
| Niveles de servicio con penalidad | Cumplimiento |
| Notificación de incidentes en plazo | Enterarse a tiempo |
| Continuidad en caso de resolución del contrato | Transición ordenada |
| Depósito del código fuente en garantía | Continuidad si el proveedor desaparece |
| Límite al incremento de precio | Evita el aprovechamiento de la cautividad |
| Aprobación previa de subcontratación | Control de la cadena |

**El plan de salida debe probarse, no escribirse.** Un plan que nunca se ejecutó es una hipótesis, y la
diferencia entre una hipótesis y un plan se descubre precisamente el día que hay que usarlo.

### 5. Arquitectura de referencia

Una arquitectura de referencia hace que las decisiones individuales sumen en vez de estorbarse. La tabla la recoge.

```text
POR QUÉ HACE FALTA
  sin un modelo común, cada decisión individual
  es razonable y el conjunto es incoherente

  → 176 integraciones directas al núcleo (clase 13)
    fueron 176 decisiones razonables

QUÉ DEFINE
  · capas y sus responsabilidades
  · cómo se integran los componentes
  · dónde vive cada tipo de dato
  · qué se compra y qué se construye, por capa
  · estándares obligatorios y excepciones autorizadas
```

## 🧮 Ejemplo guiado

El ejemplo decide sobre cuatro capacidades con el marco completo. Conviene fijarse en el costo de salida: es el que cambia la decisión en dos de los cuatro casos.

**Situación.** Un banco decide sobre su plataforma de decisión de crédito.

```text
SITUACIÓN
  el motor de decisión actual está dentro del núcleo bancario
  cambiar una política de crédito tarda 6 semanas
  las políticas cambian, en promedio, 14 veces al año

OPCIONES
  A. construir un motor de decisión propio
  B. comprar una plataforma de decisión especializada
  C. usar el servicio de decisión de un proveedor externo
     que también aporta su modelo
```

**Paso 1 — clasifica la capacidad.**

```text
¿EL MOTOR DE DECISIÓN ES DIFERENCIADOR?

  el MOTOR (la herramienta que ejecuta reglas)
    → no es diferenciador; hay soluciones maduras

  las POLÍTICAS y los MODELOS que ejecuta
    → son la política de riesgo del banco
    → completamente diferenciadores

  la VELOCIDAD para cambiar políticas
    → diferenciadora: 6 semanas frente a 1 día
      es una diferencia competitiva real

CLASIFICACIÓN: capacidad intermedia
  comprar el motor, conservar políticas, modelos y velocidad
→ la opción C queda descartada de entrada:
  externaliza el modelo, que es lo diferenciador
```

**Paso 2 — evalúa el valor de la velocidad.**

```text
14 CAMBIOS DE POLÍTICA AL AÑO, 6 SEMANAS CADA UNO

  cada cambio de política responde a algo:
  deterioro de un segmento, oportunidad, competencia

  COSTO DE LA DEMORA
    cambios reactivos por deterioro: 6 al año
    exposición promedio afectada por cambio: 4 200
    deterioro adicional durante 6 semanas:
      4 200 × (6/52) × 2,4 puntos de mora × LGD 58 % = 6,7
    total anual: 40

    cambios por oportunidad: 8 al año
    colocación no realizada durante 6 semanas:
      8 × 1 800 × (6/52) = 1 662
      margen perdido: 1 662 × 6,1 % = 101

  COSTO ANUAL DE LA DEMORA: 141
```

**Paso 3 — construye el costo total de propiedad de la opción A.**

```text
CONSTRUIR (horizonte de 10 años)
  desarrollo inicial (18 meses, 8 personas):     2 400
  infraestructura:                                 180 anuales
  equipo de mantenimiento y evolución
    (4 personas permanentes):                      760 anuales
  reemplazo por rotación (estimado):                90 anuales
  COSTO A 10 AÑOS: 2 400 + 10 × 1 030 = 12 700

RIESGOS
  · el equipo clave se va y el conocimiento se pierde
  · el desarrollo tarda más de lo previsto (frecuente)
  · funcionalidad inferior a la de una solución especializada
```

**Paso 4 — construye el costo total de propiedad de la opción B.**

```text
COMPRAR (horizonte de 10 años)
  licencia inicial:                                980
  implantación e integración (9 meses):          1 400
  licencia anual (escala con el volumen):          420 anuales
    con incremento anual del 6 %
  personas para configurar y operar (2):           380 anuales
  actualizaciones y su integración:                120 anuales

  licencias a 10 años con incremento del 6 %:
    420 × [(1,06^10 − 1)/0,06] = 420 × 13,181 = 5 536

  COSTO A 10 AÑOS: 980 + 1 400 + 5 536 + 10 × 500 = 12 916
```

**Paso 5 — compara y examina el resultado.**

```text
CONSTRUIR:  12 700 a 10 años
COMPRAR:    12 916 a 10 años

diferencia: 1,7 % → PRÁCTICAMENTE EQUIVALENTES

  a 3 años:
    construir: 2 400 + 3 × 1 030 = 5 490
    comprar:   980 + 1 400 + 1 337 + 1 500 = 5 217
    → comprar gana por poco

  a 15 años:
    construir: 2 400 + 15 × 1 030 = 17 850
    comprar:   980 + 1 400 + 9 776 + 7 500 = 19 656
    → construir gana

EL RESULTADO DEPENDE DEL HORIZONTE
y ninguna de las dos opciones domina claramente
```

**Paso 6 — decide con los criterios no económicos.**

```text
CRITERIO 4: COSTO DE CAMBIO Y CAUTIVIDAD
  comprar: si las políticas y los modelos se expresan
  en el formato propietario del proveedor,
  migrarlas a otra plataforma cuesta
  → riesgo de cautividad ALTO
  mitigable con: políticas expresadas en formato abierto,
  exportables; contrato con límite de incremento de precio

  construir: sin cautividad, con dependencia del equipo propio

CRITERIO 5: CAPACIDAD DE EJECUTAR
  ¿el banco tiene equipo para construir
  y mantener un motor de decisión durante 10 años?
    equipo actual de desarrollo: 34 personas
    con experiencia en motores de reglas: 3
    rotación anual del área: 18 %
  → la capacidad NO existe hoy y construirla
    es en sí un proyecto
```

**Paso 7 — decide.**

```text
DECISIÓN: COMPRAR (opción B), con condiciones

CONDICIONES
  1. las políticas y modelos se expresan en formato
     abierto y exportable; el contrato lo garantiza
  2. los datos de decisión son del banco,
     en formato abierto, exportables en cualquier momento
  3. límite contractual al incremento anual de licencia
  4. derecho de auditoría
  5. depósito del código en garantía
  6. plan de salida documentado y PROBADO
     en un ejercicio a los 24 meses
  7. los modelos los desarrolla y valida el banco;
     la plataforma solo los ejecuta

CUANTIFICACIÓN DEL BENEFICIO
  tiempo de cambio de política: 6 semanas → 2 días
  costo de la demora evitado: 141 × (1 − 2/30) = 132 anuales
  capacidad liberada del área de núcleo: 180 anuales
  BENEFICIO: 312 anuales
  costo incremental frente a la situación actual: 500 anuales
  
  el beneficio directo NO cubre el costo
```

**Paso 8 — completa el caso con lo que faltaba.**

```text
EL CASO ECONÓMICO DIRECTO ES INSUFICIENTE
¿QUÉ FALTA EN EL CÁLCULO?

  1. la plataforma habilita decisiones automáticas
     de aprobación (clase 6): 1 829 anuales
  2. permite ejecutar los modelos con datos alternativos
     (clase 7): 4 246 anuales
  3. permite probar políticas con experimentos
     controlados (clase 5): efecto estimado 890 anuales
  4. reduce integraciones directas al núcleo
     (clase 13): parte del programa de deuda técnica

  ninguna de esas tres capacidades es posible
  con el motor actual dentro del núcleo

BENEFICIO TOTAL: 312 + 1 829 + 4 246 + 890 = 7 277 anuales
COSTO: 500 anuales
BENEFICIO NETO: 6 777 anuales
```

```text
LA LECCIÓN DEL EJERCICIO
  el motor de decisión no vale por lo que hace:
  vale por lo que HABILITA

  evaluar una capacidad de infraestructura
  solo por su función directa la subestima siempre
  → el caso económico debe incluir
    lo que se vuelve posible
```

**Interpreta:** la comparación de costo total dio prácticamente empate y **la decisión se tomó con los
criterios 4 y 5**, no con el número. Y el caso económico solo se sostuvo al incorporar las capacidades
que la plataforma habilita, que estaban repartidas en cuatro clases anteriores de esta parte. Esa es la
integración que cierra la Parte 14: **las decisiones tecnológicas no se evalúan de a una, porque su
valor está en lo que hacen posible en conjunto**.

## 🏦 Del cliente al banco

El cliente ve un servicio y el banco depende de proveedores que también sirven a sus competidores. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «El banco tarda meses en cambiar algo» | Capacidad dentro del núcleo | 14, clase 13 |
| «Todos los bancos ofrecen lo mismo» | Se compró la capacidad diferenciadora | 14, clase 14 |
| «Mi banco decide en segundos» | Motor de decisión desacoplado | 14, clase 6 |
| «El banco cambió de proveedor y todo falló» | Plan de salida no probado | 11, clase 11 |
| «Cayeron varios bancos a la vez» | Concentración de proveedores | 14, clase 12 |

## 🧪 Práctica

El laboratorio pide clasificar capacidades y decidir. Una capacidad diferenciadora se puede comprar más barato, y sostener la decisión de construirla es el ejercicio.

En `labs/lab-06.md`, sección de estrategia:

1. Clasifica quince capacidades entre estratégicas, intermedias e infraestructura.
2. Aplica el marco de cinco preguntas a tres decisiones concretas.
3. Construye el costo total de propiedad de dos opciones a 3, 10 y 15 años.
4. Redacta las cláusulas contractuales que evitan la cautividad.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen decisiones tecnológicas que salieron caras. Las causas son costo de salida no calculado y capacidades diferenciadoras externalizadas.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se construye infraestructura | Se cree estratégica | Clasifica antes de decidir. |
| Se compra la capacidad diferenciadora | «El proveedor sabe más» | Conserva modelos y políticas. |
| Comparación a 3 años | Las decisiones duran 10-15 | Evalúa el horizonte real. |
| No se evalúa el costo de cambio | Cautividad futura | Cláusulas de portabilidad. |
| Plan de salida escrito y no probado | Es una hipótesis | Pruébalo. |
| Se evalúa la capacidad por su función directa | Se subestima | Incluye lo que habilita. |

## ❓ Preguntas de comprobación

1. ¿Qué distingue una capacidad estratégica de una de infraestructura?
2. ¿Cuál es el patrón correcto para las capacidades intermedias?
3. ¿Por qué el horizonte de comparación cambia la respuesta?
4. ¿Por qué la concentración de proveedores no tiene mitigante a nivel de un banco?
5. ¿Por qué evaluar una capacidad por su función directa la subestima?

## 📥 Entregable

Guarda en `portfolio/parte-14/clase-14/`:

- las quince capacidades clasificadas con su justificación;
- el marco de cinco preguntas aplicado a tres decisiones;
- el costo total de propiedad a tres horizontes;
- las cláusulas contractuales redactadas contra la cautividad.

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

- Basel Committee on Banking Supervision (2018). *Sound Practices: Implications of fintech developments for banks and bank supervisors*. BIS.
- Financial Stability Board (2023). *Enhancing Third-Party Risk Management and Oversight*. FSB. <https://www.fsb.org/2023/12/enhancing-third-party-risk-management-and-oversight-a-toolkit-for-financial-institutions-and-financial-authorities/>
- Basel Committee on Banking Supervision (2021). *Principles for Operational Resilience*. BIS.
- European Banking Authority (2019). *Guidelines on outsourcing arrangements*. EBA.
- Carr, N. (2003). "IT Doesn't Matter". *Harvard Business Review*. Debate sobre capacidad diferenciadora frente a infraestructura.
- Verificación local: revisa las exigencias de tu supervisor sobre externalización de funciones materiales, notificación previa y planes de salida.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 13 · Transformación digital](13-transformacion-digital.md) | [Parte 14](../README.md) · [Programa](../../../SYLLABUS.md) | [Proyecto de la parte →](../project/README.md) |
<!-- gen:footer:end -->
