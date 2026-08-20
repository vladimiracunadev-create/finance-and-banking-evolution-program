<!-- meta
part: 23
class: 15
title: "Escenario de tensión y continuidad"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [continuidad, resiliencia, liquidez]
regulation_last_verified: 2026-08-20
regulatory_status: vigente
primary_authorities: [BCBS, FSB, CPMI]
requires_legal_review: false
-->

<!-- gen:header:start -->
# Clase 15 · Escenario de tensión y continuidad

> [← 14 · Modelo de amenazas priorizado](14-modelo-de-amenazas-priorizado.md) · [Índice de la parte](../README.md) · [16 · Resolución ordenada y salida →](16-resolucion-ordenada-y-salida.md)

**Parte 23 — Proyecto — banco digital y mercado tokenizado** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Someter el sistema a un escenario adverso y **medir dónde se rompe**, en vez de
comprobar que funciona cuando todo va bien.

La clase 14 identificó lo que alguien haría a propósito. Esta somete el sistema a
lo que ocurre sin que nadie lo busque: un proveedor que cae, un cliente grande
que retira y una caída de precio simultánea.

## 📚 Objetivos

Al finalizar podrás:

1. **Diseñar** el escenario que rompe el propio sistema.
2. **Medir** el punto de rotura de cada componente.
3. **Comprobar** si las tolerancias declaradas se cumplen.
4. **Ejecutar** el plan de continuidad y declarar su nivel de prueba.
5. **Corregir** el diseño con lo que el escenario revela.

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

Los cuatro primeros términos son el escenario y su punto de rotura; los cuatro siguientes, la degradación y su prueba. El **efecto combinado** es lo que hace útil el escenario: no son varios fallos independientes sino un proveedor con varios papeles cuyo fallo alcanza a todos a la vez.

| Concepto | Comprensión verificable |
|---|---|
| `escenario de tensión` | Combinación adversa plausible |
| `punto de rotura` | Nivel donde el sistema deja de cumplir |
| `tolerancia` | Interrupción máxima admisible por función |
| `efecto combinado` | Varios fallos a la vez |
| `modo degradado` | Operación parcial mientras dura el fallo |
| `nivel de prueba` | Del gradiente de cinco, cuál se ejecutó |
| `cascada` | Fallo que provoca más fallos |
| `recuperación` | Vuelta al estado normal, medida |

## 🧠 Modelo mental

Un escenario que el sistema aguanta no enseña nada. El ejercicio consiste en
diseñar el que lo rompe y medir a qué distancia está de lo plausible.

```text
EL ESCENARIO ÚTIL

  · combina al menos tres fallos
  · los combina porque están correlacionados
  · y llega hasta el punto de rotura

Y LA PREGUNTA QUE LO CIERRA
  ¿a cuántas desviaciones está ese punto
  de lo que ocurre en un mes normal?

Si está a menos de tres, no es un
escenario adverso: es un martes.
```

## 📖 Desarrollo

### 1. La correlación es lo que hace el escenario

Tres fallos independientes son improbables. Tres fallos correlacionados son un
episodio, y la correlación viene de compartir proveedor, mercado o cliente.

```text
FUENTES DE CORRELACIÓN

  mismo proveedor de infraestructura
  mismo banco corresponsal
  el mismo mercado que cae
  los mismos clientes que retiran

Y EL ESCENARIO SE CONSTRUYE ELIGIENDO
UNA FUENTE Y SIGUIENDO SUS EFECTOS
```

### 2. Las tolerancias se contrastan aquí

La clase 12 encontró una tolerancia incompatible en un día normal. En tensión se
contrastan todas, y suele haber más de una que no se cumple.

```text
PARA CADA FUNCIÓN

  tolerancia declarada
  interrupción efectiva en el escenario
  y la diferencia

Y SI VARIAS SE INCUMPLEN A LA VEZ
  hay que decidir cuál se protege primero,
  y esa decisión es del consejo
```

### 3. El nivel de la prueba

Declarar el nivel es lo que convierte «probamos la continuidad» en información.
El gradiente va de la revisión documental a la conmutación no anunciada.

```text
1 revisión documental      nada
2 simulación de escritorio  se conoce el plan
3 entorno aislado           el procedimiento
4 conmutación planificada   la arquitectura
5 conmutación no anunciada  la organización

Y EL INFORME DICE CUÁL SE EJECUTÓ
```

## 🧮 Ejemplo guiado

El ejemplo construye el escenario desde la fuente de correlación y mide el punto de rotura. Conviene calcular a cuántas desviaciones está de un día normal: por debajo de tres no es un escenario adverso.

**Situación.** El equipo diseña el escenario que rompe su sistema y lo ejecuta.

```text
SISTEMA
  clientes                          2 400
  saldos                       91 200 000
  colateral                    24 000 000
  saldo de liquidación            144 000
  volumen diario                1 200 000
```

**Paso 1 — elige la fuente de correlación.**

```text
EL BANCO CORRESPONSAL

  emite el depósito tokenizado
  liquida los pagos transfronterizos
  custodia parte del efectivo

  UN SOLO FALLO AFECTA A TRES COMPONENTES
  → es la fuente de correlación del sistema
```

**Paso 2 — construye el escenario.**

```text
DÍA 1  el banco corresponsal anuncia
       problemas de liquidez
DÍA 1  el saldo de liquidación queda
       inaccesible
DÍA 1  los pagos transfronterizos se
       detienen
DÍA 2  el 18 % de los clientes solicita
       retirar
DÍA 2  el precio del colateral cae un 9 %
DÍA 3  se disparan 24 llamadas de margen
```

**Paso 3 — mide el punto de rotura.**

```text
LIQUIDACIÓN
  sin saldo, no se liquida nada
  tolerancia 2 h · interrupción 3 días
  → SE ROMPE

PAGOS
  ruta alternativa por otro corresponsal
  tolerancia 4 h · interrupción 6 h
  → SE ROMPE POR POCO

RETIRADAS
  18 % de 91 200 000 = 16 416 000
  liquidez disponible supuesta 22 000 000
  → AGUANTA

MARGEN
  24 liquidaciones parciales, escalonadas
  → AGUANTA, con impacto del 2,1 %
```

**Paso 4 — corrige y declara el nivel.**

```text
CORRECCIONES

  1 segundo emisor de depósito tokenizado
    activo, con el 30 % del saldo
    coste supuesto 18 000 al año

  2 corresponsal alternativo con acuerdo
    firmado y probado una vez al año
    coste supuesto 12 000 al año

  3 tolerancia de liquidación revisada a
    8 horas, con modo degradado declarado

NIVEL DE PRUEBA EJECUTADO
  nivel 3 · entorno aislado

  → se compromete un nivel 4 en seis meses
    y un nivel 5 en doce

Y SE DECLARA ASÍ EN EL INFORME,
en vez de escribir «se probó la continuidad»
```

**Interpreta:** El escenario rompió el sistema en dos de cuatro funciones, y la fuente de todo
era **un solo banco corresponsal que hacía tres papeles a la vez**. Las dos
correcciones que lo resuelven cuestan 30 000 al año, menos de lo que cuesta un
solo día de interrupción.

## 🧭 Perspectivas

El escenario afecta a cada actor de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un pago que no sale | Si se va |
| Prestatario | Una llamada de margen | Si aporta |
| Equipo | Dos funciones rotas | Qué corrige |
| Tesorería | Saldo inaccesible | Cómo lo sustituye |
| Corresponsal | Problemas de liquidez | Qué informa |
| Dirección | Tolerancias incumplidas | Cuál protege primero |
| Supervisor | Nivel de prueba declarado | Qué exige |
| Auditor | Correcciones y su coste | Qué verifica |

## 🏦 Del cliente al banco

El cliente no puede operar y el sistema mide si superó su tolerancia. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Todo funcionaba bien» | Hasta que un proveedor hizo tres papeles | 23, clase 15 |
| «Probamos la continuidad» | En nivel 3 de 5 | 23, clase 15 |
| «Tenemos plan B» | Sin acuerdo firmado no es un plan | 23, clase 15 |

## ⚖️ Riesgos y controles

Los riesgos son de correlación no identificada y de nivel de prueba no declarado. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Escenario que el sistema aguanta | Tranquiliza | No enseña nada |
| Fallos independientes | Es más fácil de modelar | La correlación hace el episodio |
| Un proveedor con varios papeles | Simplifica la operación | Concentra el fallo |
| Tolerancias sin contrastar | Se fijaron por área | El escenario las contrasta |
| «Se probó la continuidad» | Suena suficiente | Declara el nivel |
| Alternativa sin acuerdo | Se identificó un candidato | Sin firma no existe |

## 🧪 Práctica

El laboratorio pide construir el escenario y medir el punto de rotura. El nivel de prueba declarado es lo que se evalúa.

En [`labs/lab-08.md`](../labs/lab-08.md):

1. Identifica la fuente de correlación de tu sistema.
2. Construye el escenario y llévalo hasta el punto de rotura.
3. Contrasta todas las tolerancias declaradas.
4. Ejecuta el plan y declara el nivel de prueba alcanzado.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen pruebas de continuidad que no informan. Las causas son escenarios que el sistema aguanta y niveles no declarados.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Diseñar el escenario que se aguanta | Da buen resultado | Diseña el que rompe |
| Un solo fallo | Es más limpio | Los episodios combinan |
| Concentrar papeles en un proveedor | Es cómodo | Es la fuente de correlación |
| Tolerancias sin probar juntas | Cada área fija la suya | El escenario las contrasta |
| Reportar sin nivel | Es lo habitual | Sin nivel no informa |
| Alternativa sin probar | Está identificada | Pruébala una vez al año |

## ❓ Preguntas de comprobación

1. ¿Qué hace útil a un escenario de tensión?
2. ¿De dónde viene la correlación entre fallos?
3. ¿Por qué las tolerancias se contrastan en tensión y no en un día normal?
4. ¿Qué añade declarar el nivel de la prueba?
5. En el ejemplo, ¿cuál era la fuente de correlación y qué costó resolverla?

## 📥 Entregable

Guarda en `portfolio/parte-23/clase-15/`:

- la fuente de correlación identificada;
- el escenario con su punto de rotura por función;
- el contraste de todas las tolerancias;
- las correcciones y el nivel de prueba declarado.

## 🔗 Referencias cruzadas

- **Viene de:** clases 12 y 14; Parte 22, clase 14.
- **Continúa en:** clase 16 de esta parte.
- **Se aplica en:** clases 17 y 18 de esta parte.

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

- Basel Committee on Banking Supervision (2021). *Principles for Operational Resilience*. BIS. Tolerancia a la interrupción que el escenario pone a prueba. <https://www.bis.org/bcbs/publ/d516.htm>
- Financial Stability Board (2020). *Effective Practices for Cyber Incident Response and Recovery*. FSB. Secuencia de respuesta y recuperación durante el escenario. <https://www.fsb.org/2020/10/effective-practices-for-cyber-incident-response-and-recovery-final-report/>
- CPMI e IOSCO (2012). *Principles for Financial Market Infrastructures*. BIS. Requisitos de continuidad exigibles a la infraestructura. <https://www.bis.org/cpmi/publ/d101.htm>
- Financial Stability Board (2023). *Global Regulatory Framework for Crypto-asset Activities*. FSB. Riesgos de contagio que el escenario reproduce. <https://www.fsb.org/2023/07/fsb-global-regulatory-framework-for-crypto-asset-activities/>
- Verificación local: comprueba en la fuente oficial vigente qué exige tu jurisdicción sobre este punto. **Fecha de verificación de esta clase: 2026-08-20.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 14 · Modelo de amenazas priorizado](14-modelo-de-amenazas-priorizado.md) | [Parte 23](../README.md) · [Programa](../../../SYLLABUS.md) | [16 · Resolución ordenada y salida →](16-resolucion-ordenada-y-salida.md) |
<!-- gen:footer:end -->
