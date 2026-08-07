<!-- meta
part: 23
class: 4
title: "Decisión de arquitectura: ¿hace falta un registro?"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [arquitectura, dlt, criterio]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [BIS, CPMI, IOSCO]
requires_legal_review: false
-->

<!-- gen:header:start -->
# Clase 04 · Decisión de arquitectura: ¿hace falta un registro?

> [← 03 · Perímetro del propio proyecto](03-perimetro-del-propio-proyecto.md) · [Índice de la parte](../README.md) · [05 · Decisión de arquitectura: el dinero →](05-decision-de-arquitectura-el-dinero.md)

**Parte 23 — Proyecto — banco digital y mercado tokenizado** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Responder con números la primera de las cuatro decisiones previas: **si el sistema
necesita un registro distribuido o si una base de datos compartida hace lo mismo
más barato, más rápido y corregible**.

La clase 3 fijó el perímetro. Esta toma la decisión de arquitectura que más
condiciona el resto, y lo hace con el criterio de la Parte 19, clase 1: seis
preguntas de las que solo una justifica la respuesta afirmativa.

## 📚 Objetivos

Al finalizar podrás:

1. **Aplicar** las seis preguntas de criterio al propio sistema.
2. **Comparar** el registro distribuido con la alternativa centralizada, con números.
3. **Identificar** qué componente del sistema —si alguno— lo justifica.
4. **Cuantificar** el coste de gobierno de un consorcio.
5. **Concluir** que no hace falta, si los números lo dicen.

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

Los cuatro primeros términos son las preguntas que justifican un registro compartido; los cuatro siguientes, su coste y su resultado posible. La **conclusión negativa** es un resultado válido y frecuente: si ninguna de las seis preguntas se responde afirmativamente, la base centralizada es la respuesta correcta.

| Concepto | Comprensión verificable |
|---|---|
| `problema de confianza` | Partes que no confían entre sí ni en un tercero |
| `base compartida` | Una base de datos operada por una sociedad conjunta |
| `coste de gobierno` | Lo que cuesta que varios decidan juntos |
| `redundancia total` | Todos guardan todo |
| `irreversibilidad` | Lo escrito no se corrige |
| `alternativa medida` | La opción descartada, con sus cifras |
| `componente justificante` | El único que exigiría el registro |
| `conclusión negativa` | Decidir que no hace falta, con fundamento |

## 🧠 Modelo mental

La pregunta se responde mal casi siempre porque se formula mal. No es «¿podemos
usar un registro distribuido?» —casi siempre se puede— sino «¿existe aquí un
tercero de confianza disponible?». Si existe, la base compartida gana.

```text
LAS SEIS PREGUNTAS

  ¿el problema es de CONFIANZA?
     → SÍ es la única que lo justifica sola
  ¿de coordinación?   una base lo resuelve
  ¿de datos?          un formato común
  ¿de proceso?        la automatización
  ¿regulatorio?       ninguna arquitectura
                      elimina una obligación
  ¿de liquidez?       no

Y LA PREGUNTA DE CONFIANZA HAY QUE
HACERLA BIEN
  no «¿confiamos en ese participante?»
  sino «¿aceptaríamos un tercero neutral?»
```

## 📖 Desarrollo

### 1. El coste que no aparece en la comparación

Las comparaciones técnicas miden latencia, coste por operación y capacidad. El
coste que decide en un consorcio es otro y no aparece en ninguna de ellas.

```text
EL COSTE DE GOBIERNO

  · constituir la sociedad conjunta
  · acordar las reglas de cambio
  · decidir quién puede entrar
  · resolver qué pasa si uno quiere salir
  · y sostener una reunión de decisión
    cada vez que algo cambia

SUPUESTO HABITUAL
  entre 200 000 y 600 000 al año para
  un consorcio de cinco participantes

Y ES EL MISMO COSTE PARA UNA BASE
COMPARTIDA OPERADA EN CONJUNTO
  → por eso no discrimina entre las dos
    opciones, y sí las descarta a ambas
    frente a una solución de un solo
    operador
```

### 2. Qué justifica de verdad en un capstone

En un sistema como el de este proyecto, con una sola entidad y sus clientes, la
respuesta suele ser que no hace falta. Conviene decirlo pronto y buscar el único
componente donde podría hacer falta.

```text
DÓNDE PODRÍA HACER FALTA

  · si varias entidades comparten el
    registro de colateral y ninguna
    acepta que otra lo opere
  · si el instrumento tiene que circular
    entre infraestructuras
  · si la liquidación atómica contra el
    dinero es un requisito del producto

Y SOLO LA TERCERA APARECE EN ESTE
PROYECTO, en el crédito con colateral
```

### 3. La conclusión negativa es un resultado

Decidir que no hace falta un registro distribuido no es un fracaso del proyecto:
es el resultado más frecuente de aplicar el criterio con honestidad, y el que
más recursos ahorra.

```text
CÓMO SE DOCUMENTA UNA CONCLUSIÓN NEGATIVA

  · las seis preguntas con su respuesta
  · la alternativa elegida y su coste
  · el coste que habría tenido el registro
  · qué componente lo habría justificado
    y por qué no basta
  · en qué condiciones se revisaría

LA ÚLTIMA IMPORTA
  «si en el futuro entran dos entidades
   más y ninguna acepta operar el registro
   de la otra, se revisa»
```

## 🧮 Ejemplo guiado

El ejemplo aplica las seis preguntas al sistema y deja la conclusión pendiente de la clase 5. Conviene no cerrarla aquí: depende de dónde esté el dinero.

**Situación.** El equipo aplica el criterio a su sistema de cuatro funciones y
compara las dos arquitecturas con coste a cinco años.

```text
SISTEMA
  una entidad, 2 400 clientes
  colateral tokenizado como única función
  que sugiere un registro
  colateral previsto            24 000 000
  operaciones de colateral al mes    380
```

**Paso 1 — aplica las seis preguntas.**

```text
¿CONFIANZA?
  la entidad y sus clientes; el cliente
  confía en la entidad porque está
  autorizada y supervisada
  → NO es un problema de confianza

¿coordinación?  una base lo resuelve
¿datos?         formato propio
¿proceso?       automatización
¿regulatorio?   ninguna arquitectura exime
¿liquidez?      no

  NINGUNA JUSTIFICA
```

**Paso 2 — mide el componente que podría justificar.**

```text
CRÉDITO CON COLATERAL TOKENIZADO

  ¿por qué se tokenizó el colateral?
  para poder liquidarlo de forma atómica
  contra el dinero

  ¿ESTÁ EL DINERO EN EL MISMO REGISTRO?
  se decide en la clase 5

  · si sí, la atomicidad es alcanzable y
    el registro tiene sentido
  · si no, no hay atomicidad y el registro
    no aporta nada

  → LA DECISIÓN DEPENDE DE LA CLASE 5,
    y hay que decirlo en vez de resolverla
    por adelantado
```

**Paso 3 — compara las dos arquitecturas.**

```text
REGISTRO DISTRIBUIDO PROPIO
  desarrollo supuesto            380 000
  operación anual                140 000
  gobierno (una entidad)          40 000
  COSTE A 5 AÑOS                1 280 000

BASE COMPARTIDA CON EL CUSTODIO
  desarrollo supuesto             90 000
  operación anual                 60 000
  conciliación con el custodio    36 000
  COSTE A 5 AÑOS                  570 000

  DIFERENCIA: 710 000
```

**Paso 4 — concluye y deja la condición de revisión.**

```text
CONCLUSIÓN

  no hace falta un registro distribuido
  · ninguna de las seis preguntas lo
    justifica
  · el único componente que podría
    justificarlo depende de una decisión
    posterior
  · y la alternativa ahorra 710 000

DECISIÓN
  base de datos propia con el registro
  de colateral, conciliada a diario con
  el custodio autorizado

SE REVISARÍA SI
  · el dinero pasa a estar en un registro
    y la atomicidad se vuelve un requisito
  · entran dos entidades más y ninguna
    acepta operar el registro de la otra
```

**Interpreta:** Ninguna de las seis preguntas justificaba el registro y la alternativa ahorraba
710 000. **La decisión honesta fue además reconocer que el único componente que
podría justificarlo depende de la clase siguiente**, en vez de resolverla por
adelantado para que el resultado saliera como se quería.

## 🧭 Perspectivas

La decisión de arquitectura afecta a cada actor de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un crédito con garantía | — |
| Equipo | Una arquitectura menos vistosa | Si la acepta |
| Custodio | Una conciliación diaria | Qué formato admite |
| Inversionista | 710 000 de ahorro | Si lo valora |
| Banco | Una entidad sin registro propio | Si le presta servicios |
| Supervisor | Una decisión documentada | Qué observa |
| Auditor | Alternativa medida | Qué verifica |
| Sociedad | Menos complejidad | — |

## 🏦 Del cliente al banco

El cliente no distingue la tecnología y sus garantías dependen de esta decisión. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Usan blockchain» | No hacía falta y ahorra 710 000 | 23, clase 4 |
| «Es más moderno» | La modernidad no es un criterio | 23, clase 4 |
| «Sin intermediarios» | El custodio sigue estando | 23, clase 4 |

## ⚖️ Riesgos y controles

Los riesgos son de arquitectura injustificada y de coste de gobierno. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Decidir por preferencia | Se elige la arquitectura de moda | Las seis preguntas con respuesta |
| Olvidar el coste de gobierno | No aparece en las comparaciones | Estimarlo y sumarlo |
| Resolver una decisión dependiente | Se adelanta para que salga bien | Declarar la dependencia |
| Sin condición de revisión | La decisión queda congelada | Escribir cuándo se revisaría |
| Comparar solo lo técnico | Latencia y coste por operación | El gobierno decide más |
| Ver el «no» como fracaso | Se buscó justificar el registro | Es el resultado más frecuente |

## 🧪 Práctica

El laboratorio pide aplicar las seis preguntas y medir la alternativa centralizada. Dejar la conclusión pendiente de la clase siguiente es parte del ejercicio.

En [`labs/lab-01.md`](../labs/lab-01.md):

1. Aplica las seis preguntas a tu sistema y documenta cada respuesta.
2. Identifica el componente que podría justificar el registro.
3. Compara las dos arquitecturas a cinco años, con coste de gobierno.
4. Escribe la conclusión con su condición de revisión.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen arquitecturas elegidas antes de justificarse. La causa es haber decidido la tecnología y buscado después el argumento.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Justificar el registro | Ya se decidió usarlo | Las preguntas deciden |
| Ignorar el gobierno | No es técnico | Es el coste que discrimina |
| Comparar sin la alternativa | No se estimó | Sin alternativa no hay decisión |
| Resolver dependencias por adelantado | Estorban | Declararlas |
| Conclusión sin revisión | Se da por definitiva | Las condiciones cambian |
| Tratar el «no» como problema | Parece poco ambicioso | Ahorra 710 000 |

## ❓ Preguntas de comprobación

1. ¿Cuál de las seis preguntas justifica por sí sola un registro distribuido?
2. ¿Por qué el coste de gobierno no discrimina entre las dos opciones de consorcio?
3. ¿Qué componente de este proyecto podría justificar el registro y de qué depende?
4. ¿Cómo se documenta una conclusión negativa?
5. ¿Por qué conviene escribir la condición de revisión?

## 📥 Entregable

Guarda en `portfolio/parte-23/clase-04/`:

- las seis preguntas con su respuesta y su fundamento;
- la comparación de arquitecturas a cinco años;
- el componente que podría justificar el registro y su dependencia;
- la conclusión con su condición de revisión.

## 🔗 Referencias cruzadas

- **Viene de:** clases 1 y 3; Parte 19, clase 1.
- **Continúa en:** clases 5 y 7 de esta parte.
- **Se aplica en:** clases 10 y 13 de esta parte.

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

- Bank for International Settlements (2023). *Annual Economic Report*, capítulo III. BIS. <https://www.bis.org/publ/arpdf/ar2023e3.htm>
- Committee on Payments and Market Infrastructures (2024). *Tokenisation in the context of money and other assets*. BIS. <https://www.bis.org/cpmi/publ/d225.htm>
- CPMI e IOSCO (2012). *Principles for Financial Market Infrastructures*. BIS. <https://www.bis.org/cpmi/publ/d101.htm>
- IOSCO (2023). *Policy Recommendations for Crypto and Digital Asset Markets*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- Verificación local: comprueba en la fuente oficial vigente qué exige tu jurisdicción sobre este punto antes de aplicar cualquier conclusión de la clase. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 03 · Perímetro del propio proyecto](03-perimetro-del-propio-proyecto.md) | [Parte 23](../README.md) · [Programa](../../../SYLLABUS.md) | [05 · Decisión de arquitectura: el dinero →](05-decision-de-arquitectura-el-dinero.md) |
<!-- gen:footer:end -->
