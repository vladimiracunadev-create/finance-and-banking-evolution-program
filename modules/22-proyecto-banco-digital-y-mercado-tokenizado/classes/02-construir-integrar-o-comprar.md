---
part: 23
class: 2
title: "Construir, integrar o comprar"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [externalizacion, arquitectura, terceros]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [BCBS, CPMI, CMF]
requires_legal_review: true
---

<!-- gen:header:start -->
# Clase 02 · Construir, integrar o comprar

> [← 01 · Alcance y modelo de negocio](01-alcance-y-modelo-de-negocio.md) · [Índice de la parte](../README.md) · [03 · Perímetro del propio proyecto →](03-perimetro-del-propio-proyecto.md)

**Parte 23 — Proyecto — banco digital y mercado tokenizado** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Decidir qué se construye y qué se integra. **Cada componente propio es una
capacidad y una carga**, y cada integración es una dependencia que hay que poder
abandonar.

La clase 1 redujo el alcance a cuatro funciones. Esta decide, para cada una, si
el equipo la construye, la integra de un tercero o la compra hecha. Es la
decisión que más condiciona el coste operativo y la que más se toma por
costumbre en vez de por análisis.

## 📚 Objetivos

Al finalizar podrás:

1. **Aplicar** el criterio de decisión a cada componente del sistema.
2. **Calcular** el coste total de construir frente a integrar.
3. **Evaluar** una dependencia por su capacidad de salida.
4. **Identificar** los componentes que nunca deben externalizarse.
5. **Documentar** cada decisión con su alternativa medida.

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
| `componente crítico` | Aquel cuyo fallo detiene el servicio |
| `capacidad propia` | Lo que la entidad sabe hacer y mantener |
| `dependencia` | Componente de un tercero del que no se puede prescindir |
| `coste total de propiedad` | Construcción más operación y mantenimiento |
| `estrategia de salida` | Plan para dejar de depender de un proveedor |
| `bloqueo de proveedor` | Imposibilidad práctica de cambiar |
| `componente diferenciador` | El que da ventaja competitiva |
| `componente de utilidad` | El que todos necesitan y nadie valora |

## 🧠 Modelo mental

La decisión no es técnica ni económica: es sobre qué capacidades quiere tener la
entidad dentro de cinco años. Un componente construido hoy es un equipo que hay
que sostener; uno integrado es un proveedor del que hay que poder salir.

```text
LA MATRIZ DE DECISIÓN

  ¿ES DIFERENCIADOR?     ¿HAY PROVEEDOR MADURO?

  sí   +   no    →  CONSTRUIR
  sí   +   sí    →  construir, si el proveedor
                    limita lo que se puede hacer
  no   +   sí    →  INTEGRAR
  no   +   no    →  esperar, o construir lo mínimo

Y UNA REGLA QUE NO ADMITE EXCEPCIÓN
  lo que la norma exige que controle la
  entidad no se externaliza: se puede
  delegar la ejecución, nunca la
  responsabilidad
```

## 📖 Desarrollo

### 1. Coste total, no coste inicial

Comparar el precio de una licencia con el sueldo de un equipo es el error
habitual. Un componente propio cuesta durante toda su vida, y un componente
integrado también.

```text
CONSTRUIR
  desarrollo inicial
  + mantenimiento anual (20–30 % del inicial)
  + evolución normativa
  + guardia y operación
  + el coste de que la persona que lo sabe
    se vaya

INTEGRAR
  licencia o comisión
  + integración inicial
  + adaptación a cada cambio del proveedor
  + coste de auditarlo
  + coste de salir, si hay que salir

EL ÚLTIMO SE OMITE SIEMPRE
  y es el que decide, porque sin él la
  comparación supone que nunca habrá
  que cambiar de proveedor
```

### 2. Lo que no se externaliza

Hay funciones cuya responsabilidad la norma atribuye a la entidad. Se puede
contratar a alguien para que las ejecute, y la responsabilidad no se traslada con
el contrato.

```text
NO SE EXTERNALIZA LA RESPONSABILIDAD DE

  · decidir a quién se admite como cliente
  · decidir si una operación es sospechosa
  · el control interno y la auditoría
  · la relación con el supervisor
  · las decisiones de riesgo
  · la custodia, si es actividad reservada

SE PUEDE DELEGAR LA EJECUCIÓN
  y entonces hay que poder auditarla,
  entenderla y sustituirla
```

### 3. La estrategia de salida como criterio de entrada

Un proveedor del que no se puede salir no es un proveedor: es una parte del
sistema que no se controla. La pregunta se hace antes de firmar, no cuando hay
un problema.

```text
CUATRO PREGUNTAS ANTES DE INTEGRAR

  1 ¿existe un proveedor alternativo real?
  2 ¿los datos son portables y en qué formato?
  3 ¿cuánto tardaría la migración y cuánto
    costaría?
  4 ¿el contrato permite salir sin penalización
    desproporcionada?

SI LA 1 ES «NO», LA INTEGRACIÓN ES
UNA DEPENDENCIA ESTRUCTURAL
  y hay que tratarla como tal: con plan
  de contingencia y con vigilancia
```

### 4. El riesgo de concentración del sector

La Parte 22, clase 14 mostró que veintidós entidades pueden cumplir su norma y
compartir un punto único de fallo. Al elegir proveedor, esa pregunta también es
del proyecto.

```text
ANTES DE ELEGIR, PREGUNTAR

  · ¿cuántas entidades del sector usan
    este proveedor?
  · ¿sobre qué infraestructura se apoya él?
  · ¿está designado como tercero crítico?

Y SI LA RESPUESTA A LA PRIMERA ES «CASI
TODAS», ELEGIRLO AÑADE AL RIESGO DEL
SECTOR, aunque para la entidad sea la
opción más segura
```

## 🧮 Ejemplo guiado

**Situación.** El equipo decide para las cuatro funciones del alcance. Hay que
comparar construir e integrar con coste total, incluida la salida.

```text
COMPONENTES A DECIDIR
  núcleo de cuentas y saldos
  motor de pagos locales
  conexión de pagos transfronterizos
  motor de cambio de divisas
  verificación de identidad
  motor de decisión de crédito
  registro de colateral tokenizado
```

**Paso 1 — clasifica por diferenciación.**

```text
                          DIFERENCIADOR   PROVEEDOR
                                          MADURO

  núcleo de cuentas          no             sí
  motor de pagos locales     no             sí
  conexión transfronteriza   no             sí
  motor de cambio            sí             sí
  verificación de identidad  no             sí
  decisión de crédito        SÍ             no
  registro de colateral      sí             no

  DOS CLARAMENTE PROPIOS: decisión de
  crédito y registro de colateral
```

**Paso 2 — calcula el coste total del núcleo.**

```text
CONSTRUIR
  desarrollo supuesto            420 000
  mantenimiento 25 % anual       105 000
  operación y guardia            160 000
  COSTE A 5 AÑOS               1 745 000

INTEGRAR
  licencia anual supuesta        120 000
  integración inicial             90 000
  adaptación anual                40 000
  auditoría anual                 25 000
  COSTE A 5 AÑOS                 1 015 000

  INTEGRAR AHORRA 730 000
```

**Paso 3 — añade el coste de salir.**

```text
SI HAY QUE CAMBIAR DE PROVEEDOR EN EL AÑO 4

  migración supuesta             280 000
  doble operación 6 meses         60 000
  COSTE DE SALIDA                340 000

  INTEGRAR CON UNA SALIDA        1 355 000
  frente a CONSTRUIR             1 745 000

  sigue ahorrando 390 000

Y SI NO HAY PROVEEDOR ALTERNATIVO
  el coste de salida no es 340 000:
  es rehacer el núcleo, o sea 1 745 000
  → y entonces integrar cuesta más
```

**Paso 4 — aplica las cuatro preguntas de salida.**

```text
NÚCLEO DE CUENTAS
  1 ¿alternativa real?        sí, tres
  2 ¿datos portables?         sí, formato estándar
  3 ¿plazo y coste?           6 meses, 340 000
  4 ¿salida sin penalización? sí, con 90 días

  → INTEGRAR

REGISTRO DE COLATERAL
  1 ¿alternativa real?        no
  2 ¿datos portables?         no hay formato
  3 ¿plazo y coste?           no estimable
  4 ¿salida?                  no prevista

  → CONSTRUIR, aunque cueste más
```

**Paso 5 — comprueba la concentración del sector.**

```text
VERIFICACIÓN DE IDENTIDAD

  proveedor candidato: usado por 14 de las
  18 entidades comparables del mercado

  · para la entidad, es la opción probada
  · para el sector, añade al 78 % de
    concentración

  DECISIÓN
  integrar el candidato Y mantener un
  segundo proveedor activo para el 20 %
  del volumen, de modo que la migración
  esté probada

  coste adicional supuesto: 34 000 al año
  → el precio de no ser parte del problema
```

**Paso 6 — cierra la tabla de decisiones.**

```text
  núcleo de cuentas       INTEGRAR   ahorra 390 000
  motor de pagos          INTEGRAR   proveedor maduro
  transfronterizo         INTEGRAR   corresponsalía
  motor de cambio         INTEGRAR   con margen propio
                                     configurable
  verificación identidad  INTEGRAR   con segundo
                                     proveedor activo
  decisión de crédito     CONSTRUIR  diferenciador
  registro de colateral   CONSTRUIR  sin salida posible

  CINCO INTEGRADOS, DOS PROPIOS

Y LO QUE NO SE EXTERNALIZA EN NINGÚN CASO
  la decisión de admitir un cliente,
  la de considerar sospechosa una operación
  y la relación con el supervisor
```

**Interpreta:** La comparación de coste favorecía integrar en seis de siete componentes, y el
criterio que cambió dos decisiones **no fue el coste sino la capacidad de
salir**. El registro de colateral se construye porque no hay a dónde migrar, y
eso lo convierte en una dependencia estructural si se integra.

## 🧭 Perspectivas

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un servicio que funciona | — |
| Equipo | Siete componentes que sabe construir | Cuáles construye |
| Proveedor | Una integración más | Qué contrato ofrece |
| Banco | Una entidad con dependencias | Qué exige |
| Auditor | Externalización con derechos | Qué verifica |
| Supervisor | Responsabilidades delegadas | Qué recuerda que no se delega |
| Inversionista | Coste total a cinco años | Si financia |
| Sociedad | Concentración del sector | Qué diversidad espera |

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Lo hacen ellos mismos» | Cinco de siete están integrados | 23, clase 2 |
| «Cambian de proveedor si hace falta» | Solo si hay alternativa real | 23, clase 2 |
| «Es responsabilidad del proveedor» | La responsabilidad no se delega | 23, clase 2 |

## ⚖️ Riesgos y controles

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Comparar coste inicial | Se ignoran mantenimiento y salida | Coste total a cinco años |
| Integrar sin alternativa | Dependencia estructural | Cuatro preguntas antes de firmar |
| Externalizar la responsabilidad | Se cree delegada | Solo se delega la ejecución |
| Elegir al proveedor de todos | Añade al riesgo del sector | Segundo proveedor activo |
| Construir lo que no diferencia | Coste sin ventaja | Matriz de decisión |
| Salida sin probar | No funciona cuando hace falta | Migrar un subconjunto real |

## 🧪 Práctica

En [`labs/lab-01.md`](../labs/lab-01.md):

1. Clasifica cada componente por diferenciación y madurez del proveedor.
2. Calcula el coste total a cinco años de construir e integrar.
3. Añade el coste de salir y comprueba si cambia la decisión.
4. Aplica las cuatro preguntas de salida a cada integración.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Comparar licencia con sueldo | Es la comparación visible | Coste total, no inicial |
| Integrar por rapidez | Acelera el lanzamiento | Comprueba la salida primero |
| Construir por control | Da sensación de dominio | Solo si diferencia |
| Un solo proveedor | Es más barato | Sin alternativa es dependencia |
| Delegar el cumplimiento | El proveedor lo ofrece | La responsabilidad es de la entidad |
| Salida en el contrato y no probada | Está redactada | Migra un subconjunto |

## ❓ Preguntas de comprobación

1. ¿Qué cuatro casos define la matriz de decisión?
2. ¿Qué componente del coste total se omite siempre y por qué decide?
3. ¿Qué funciones no se externalizan nunca?
4. ¿Cuáles son las cuatro preguntas antes de integrar?
5. En el ejemplo, ¿qué criterio cambió dos decisiones y por qué?

## 📥 Entregable

Guarda en `portfolio/parte-23/clase-02/`:

- la matriz de decisión con los siete componentes;
- el coste total a cinco años de construir e integrar;
- las cuatro preguntas de salida por cada integración;
- la tabla final de decisiones con su justificación.

## 🔗 Referencias cruzadas

- **Viene de:** clase 1; Parte 22, clase 14.
- **Continúa en:** clases 8 y 9 de esta parte.
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

- Basel Committee on Banking Supervision (2021). *Principles for Operational Resilience*. BIS. <https://www.bis.org/bcbs/publ/d516.htm>
- Basel Committee on Banking Supervision (2018). *Sound Practices: implications of fintech developments*. BIS. <https://www.bis.org/bcbs/publ/d431.htm>
- Diario Oficial de la Unión Europea (2022). *Reglamento (UE) 2022/2554 sobre resiliencia operativa digital*. EUR-Lex. <https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32022R2554>
- Comisión para el Mercado Financiero. *Normativa sobre externalización de servicios*. CMF. <https://www.cmfchile.cl/portal/principal/613/w3-channel.html>
- Verificación local: comprueba qué exige tu jurisdicción para externalizar funciones relevantes, qué derechos de auditoría impone y qué funciones no admite delegar. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 01 · Alcance y modelo de negocio](01-alcance-y-modelo-de-negocio.md) | [Parte 23](../README.md) · [Programa](../../../SYLLABUS.md) | [03 · Perímetro del propio proyecto →](03-perimetro-del-propio-proyecto.md) |
<!-- gen:footer:end -->
