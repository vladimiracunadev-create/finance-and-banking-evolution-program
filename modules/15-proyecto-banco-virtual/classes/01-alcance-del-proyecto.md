---
part: 16
class: 1
title: "Alcance del proyecto"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 01 · Alcance del proyecto

> [← Índice de la parte](../README.md) · [Índice de la parte](../README.md) · [02 · Modelo de negocio del banco →](02-modelo-de-negocio-del-banco.md)

**Parte 16 — Proyecto Banco Virtual** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Abrir el proyecto final del programa definiendo qué se va a construir, con qué criterios se evaluará y
cómo se organizará el trabajo de las diecisiete clases siguientes. **El proyecto es un banco completo en
escala reducida**, y su valor está en que cada decisión se tome con el criterio que las quince partes
anteriores construyeron.

Esta parte cierra las cuatro primeras etapas construyendo un banco completo. No introduce temas nuevos: obliga a que los quince anteriores encajen entre sí, y ahí es donde aparecen las contradicciones que ninguna parte por separado podía mostrar. Empieza acotando el alcance, porque un proyecto de este tamaño sin límites declarados no se termina.

## 📚 Objetivos

Al finalizar podrás:

1. **Describir** el alcance del banco virtual y sus componentes.
2. **Organizar** el trabajo en entregables verificables.
3. **Aplicar** los criterios de evaluación del proyecto.
4. **Establecer** las convenciones de datos, unidades y documentación.
5. **Planificar** tu propio recorrido según tu perfil.

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

Los cuatro primeros términos son el objeto y sus reglas de datos; los cuatro siguientes, lo que se exige del entregable. La **reproducibilidad** es el criterio que gobierna todo: cualquier cifra del proyecto tiene que poder recalcularse desde sus supuestos, y si no se puede, no entra.

| Concepto | Comprensión verificable |
|---|---|
| `banco virtual` | Institución simulada con balance, productos, clientes y controles. |
| `entregable` | Producto verificable de una clase o de un bloque. |
| `datos sintéticos` | Generados artificialmente, sin persona real detrás. |
| `supuesto declarado` | Hipótesis que sostiene un cálculo, escrita y justificada. |
| `reproducibilidad` | Que otro pueda repetir el cálculo y obtener lo mismo. |
| `trazabilidad` | Que cada cifra se pueda seguir hasta su origen. |
| `criterio de aceptación` | Condición que un entregable debe cumplir. |
| `defensa` | Presentación y sustentación del proyecto completo. |

## 🧠 Modelo mental

El modelo mental es un banco que no existe y del que hay que poder responder cualquier pregunta. Todo lo que se afirme sobre él tiene que salir de un cálculo reproducible con datos sintéticos declarados, y esa exigencia es lo que convierte el ejercicio en formación profesional.

```text
EL PROYECTO NO ES UN EJERCICIO DE PROGRAMACIÓN
NI UN TRABAJO ESCRITO

  ES LA CONSTRUCCIÓN DE UN CONJUNTO DE DECISIONES
  COHERENTES ENTRE SÍ

  el precio depende del costo del capital
  el capital depende del riesgo
  el riesgo depende del modelo
  el modelo depende de los datos
  y los datos dependen de cómo se diseñó el producto

  UNA DECISIÓN INCOHERENTE SE PROPAGA
  y el proyecto está diseñado para que se note
```

## 📖 Desarrollo

### 1. El banco virtual

El Banco Austral es una entidad ficticia con parámetros definidos que se mantienen constantes durante las dieciocho clases. La tabla los recoge.

```text
"BANCO AUSTRAL" — INSTITUCIÓN A CONSTRUIR

  PERFIL
    banco minorista y de pequeña empresa
    mercado: economía emergente, moneda local
    escala: 120 000 clientes potenciales
    capital inicial aportado: 42 000
    horizonte de simulación: 3 años

  LO QUE HABRÁ QUE DECIDIR Y CONSTRUIR
    modelo de negocio y segmentos
    catálogo de productos y sus precios
    política y modelos de crédito
    operaciones, pagos y contabilidad
    tesorería y gestión del balance
    marco de riesgos y de cumplimiento
    gobierno y cuadro de mando
```

```text
LAS UNIDADES DEL PROYECTO
  todos los importes en MILES de unidades monetarias
  todas las tasas en porcentaje anual, con dos decimales
  todos los plazos en meses
  todas las fechas relativas al mes 0

  ESTA CONVENCIÓN ES OBLIGATORIA
  y el ejercicio de verificación de escala
  que apareció en varias clases anteriores
  existe precisamente porque su ausencia produce errores
```

### 2. Estructura del trabajo

El proyecto se organiza en fases con entregables encadenados. La tabla los recoge.

| Bloque | Clases | Entregable |
|---|---|---|
| Diseño | 2–5 | Modelo de negocio, gobierno, arquitectura, catálogo |
| Construcción | 6–11 | Precios, originación, modelos, operaciones, contabilidad, tesorería |
| Control | 12–14 | Marco de riesgos, cumplimiento, cuadro de mando |
| Prueba | 15–17 | Estrés, ciclo completo, crisis |
| Cierre | 18 | Defensa del proyecto |

```text
CADA CLASE PRODUCE UN ENTREGABLE
Y CADA ENTREGABLE ALIMENTA AL SIGUIENTE

  si el catálogo de la clase 5 no está,
  los precios de la clase 6 no se pueden calcular

  el proyecto está encadenado a propósito
```

### 3. Criterios de evaluación

El proyecto se evalúa con criterios explícitos y en proporciones conocidas. La tabla los recoge.

| Criterio | Peso | Qué se evalúa |
|---|---:|---|
| Coherencia | 25 % | Que las decisiones se sostengan entre sí |
| Rigor técnico | 20 % | Que los cálculos sean correctos y reproducibles |
| Supuestos | 15 % | Que estén declarados, justificados y estresados |
| Control y cumplimiento | 15 % | Que el banco sea viable regulatoriamente |
| Cliente y ética | 15 % | Que las decisiones consideren al afectado |
| Comunicación | 10 % | Que la defensa sea clara y honesta |

```text
EL CRITERIO DE MAYOR PESO ES LA COHERENCIA
  un proyecto con cálculos impecables y decisiones
  que se contradicen vale menos que uno con cálculos
  simples y decisiones consistentes

  porque el primero no podría dirigirse
```

### 4. Convenciones obligatorias

Hay convenciones que se aplican a todos los entregables sin excepción. La tabla las recoge.

```text
DATOS
  · exclusivamente sintéticos
  · sin ninguna persona real, ni siquiera anonimizada
  · generados con semilla fija, para reproducibilidad
  · documentados: qué representa cada campo

SUPUESTOS
  · cada supuesto en un registro único: assumptions.md
  · con su valor, su fuente o fundamento, y su rango
  · marcados los que son críticos para el resultado

CÁLCULOS
  · reproducibles: mismo insumo, mismo resultado
  · con la fórmula visible
  · con verificación de escala antes de sumar o multiplicar

DOCUMENTACIÓN
  · cada decisión con su fundamento
  · cada cifra con su origen
  · lo que no se sabe, declarado como tal
```

```text
LA REGLA MÁS IMPORTANTE DE TODAS
  si un cálculo depende de un supuesto,
  el supuesto se declara ANTES del cálculo

  un resultado sin su supuesto no es un resultado:
  es una cifra
```

### 5. Recorridos por perfil

El proyecto admite recorridos distintos según el perfil de quien lo hace. La tabla los recoge.

| Perfil | Énfasis | Profundidad sugerida |
|---|---|---|
| Sin experiencia previa | Comprender el encadenamiento | Ejecutar todo con los datos provistos |
| Analista financiero | Modelos y proyecciones | Construir tus propios modelos |
| Profesional bancario | Riesgo, control y cumplimiento | Comparar con tu institución |
| Dirección | Estrategia y decisiones | Foco en las clases 2, 12, 14, 16, 17, 18 |
| Docente | El proyecto como caso | Adaptar los datos a tu mercado |

```text
TODOS LOS PERFILES HACEN EL MISMO PROYECTO
  lo que cambia es la profundidad de cada bloque
  y ninguno puede omitir la defensa,
  porque sostener las decisiones propias
  es la competencia que el programa entero construye
```

## 🧮 Ejemplo guiado

El ejemplo declara los supuestos de un cálculo y demuestra su reproducibilidad. Conviene fijarse en la hoja de supuestos: es el documento que hace defendible todo lo demás.

**Situación.** Primera decisión del proyecto: verificar que el capital inicial permite el banco que se
quiere construir.

```text
DATO DE PARTIDA
  capital inicial aportado: 42 000
  requerimiento total estimado: 11,34 %
  objetivo interno propuesto: 14,00 %
```

**Paso 1 — calcula la capacidad máxima de activos ponderados.**

```text
con el objetivo interno del 14,00 %:
  activos ponderados máximos = 42 000 / 0,14 = 300 000

con el requerimiento mínimo del 11,34 %:
  activos ponderados máximos = 42 000 / 0,1134 = 370 370

  la diferencia es el colchón de gestión:
  70 370 de activos ponderados
```

**Paso 2 — traduce a cartera según el mix.**

```text
MIX PRELIMINAR PROPUESTO
  consumo         30 %   ponderación 75 %
  hipotecario     40 %   ponderación 35 %
  pequeña empresa 30 %   ponderación 85 %

  ponderación media: 0,30×0,75 + 0,40×0,35 + 0,30×0,85
                   = 0,225 + 0,140 + 0,255 = 0,620

  cartera máxima = 300 000 / 0,620 = 483 871
```

**Paso 3 — verifica la escala.**

```text
VERIFICACIÓN DE COHERENCIA
  cartera de 483 871 (miles) con 120 000 clientes potenciales
  → 4,03 por cliente si todos tomaran crédito

  con una penetración de crédito del 45 %:
  54 000 clientes con crédito
  monto medio: 483 871 / 54 000 = 8,96

  ¿es plausible un monto medio de 8,96 (miles)
  en un banco minorista de economía emergente?
  → sí, con hipotecario al 40 % de la cartera
```

**Paso 4 — verifica la restricción de apalancamiento.**

```text
exposición total estimada (Parte 12, clase 6)
  cartera 483 871
  + activos líquidos (para cumplir liquidez): ~90 000
  + otros activos: ~35 000
  + partidas fuera de balance ponderadas: ~24 000
  EXPOSICIÓN: 632 871

  apalancamiento = 42 000 / 632 871 = 6,64 %
  mínimo: 3,00 %  ✓

  RESTRICCIÓN ACTIVA: capital (Parte 15, clase 6)
```

**Paso 5 — verifica la viabilidad del resultado.**

```text
¿ESTE BANCO PUEDE SER RENTABLE?

  margen bruto estimado
    cartera 483 871 × margen de intermediación 6,5 % = 31 452
    comisiones: 25 % del margen bruto → margen bruto total 41 936

  gastos operativos
    para un banco de 120 000 clientes con este modelo,
    índice de eficiencia alcanzable: 58 % en régimen
    gastos: 41 936 × 58 % = 24 323

  costo de riesgo
    con el mix propuesto: ~1,9 %
    483 871 × 1,9 % = 9 194

  resultado antes de impuestos: 41 936 − 24 323 − 9 194 = 8 419
  resultado neto (27 %): 6 146
  rentabilidad sobre patrimonio: 6 146 / 42 000 = 14,63 %
```

**Paso 6 — compara con el costo del capital.**

```text
COSTO DEL CAPITAL ESTIMADO
  tasa libre de riesgo local: 6,4 %
  prima de riesgo de mercado: 7,2 %
  beta del sector bancario local: 1,15
  prima por tamaño (banco pequeño): 3,0 %

  ke = 6,4 % + 1,15 × 7,2 % + 3,0 % = 17,68 %

  RENTABILIDAD PROYECTADA: 14,63 %
  COSTO DEL CAPITAL: 17,68 %

  EL BANCO, EN RÉGIMEN, DESTRUYE VALOR
```

**Paso 7 — identifica qué debe cambiar.**

```text
PARA ALCANZAR EL 17,68 %
  resultado neto necesario: 42 000 × 17,68 % = 7 426
  resultado antes de impuestos: 10 173
  frente a 8 419 proyectados
  BRECHA: 1 754

  PALANCAS
    a) mejorar el índice de eficiencia de 58 % a 53,8 %
       → ahorro 1 762  ✓ suficiente por sí sola
    b) mejorar el margen de intermediación de 6,5 % a 6,86 %
       → +1 742
    c) aumentar las comisiones del 25 % al 29,2 %
       del margen bruto → +1 760
    d) reducir el costo de riesgo de 1,9 % a 1,54 %
       → +1 742
    e) combinación de las cuatro, con menor exigencia
       en cada una
```

**Paso 8 — establece el compromiso del proyecto.**

```text
DECISIÓN DE DISEÑO DEL BANCO AUSTRAL

  el banco se diseñará para alcanzar un retorno
  sobre patrimonio del 18,0 % en el año 3,
  con la siguiente combinación:

    índice de eficiencia:          55,0 %  (no 58 %)
    margen de intermediación:       6,70 %
    comisiones sobre margen bruto: 27,0 %
    costo de riesgo:                1,75 %

  Y CADA UNA DE ESAS CUATRO CIFRAS
  SERÁ UN COMPROMISO QUE LAS CLASES SIGUIENTES
  DEBERÁN SOSTENER CON DECISIONES CONCRETAS

    la eficiencia: clases 4, 9 y 14
    el margen: clases 5, 6 y 11
    las comisiones: clases 5 y 9
    el costo de riesgo: clases 7, 8 y 12

  SI AL FINAL DEL PROYECTO LAS DECISIONES TOMADAS
  NO PRODUCEN ESAS CIFRAS, EL PROYECTO
  NO ES COHERENTE, Y ESO ES LO QUE SE EVALÚA
```

**Interpreta:** la primera decisión del proyecto reveló que **el banco tal como se planteaba destruía
valor**, y esa es la razón de empezar por aquí. Los cuatro compromisos establecidos —eficiencia, margen,
comisiones y costo de riesgo— son las restricciones que darán sentido a las diecisiete clases
siguientes: cada decisión de producto, precio, riesgo o proceso tendrá que ser coherente con ellas o
justificar por qué se apartan.

## 🏦 Del cliente al banco

El estudiante construye un banco de papel y un banco real hace exactamente lo mismo antes de pedir su licencia. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Un banco nuevo en el mercado» | Capital que limita el tamaño | 12, clase 6 |
| «Sus tasas son parecidas a las demás» | El margen es un compromiso de diseño | 15, clase 7 |
| «Atiende sobre todo a personas» | Segmento definido por el capital disponible | 15, clase 3 |
| «Tiene pocos productos» | Catálogo acotado por costo de complejidad | 15, clase 8 |
| «Es un banco pequeño» | Prima por tamaño en el costo de capital | 13, clase 5 |

## 🧪 Práctica

El laboratorio pide fijar el alcance del propio proyecto con sus renuncias declaradas. Las renuncias son la parte que se evalúa.

En `labs/lab-01.md`:

1. Calcula la capacidad de activos ponderados y de cartera de tu banco.
2. Verifica la coherencia de escala entre cartera, clientes y monto medio.
3. Proyecta el resultado en régimen y compáralo con el costo del capital.
4. Establece los cuatro compromisos de diseño de tu proyecto.

## ⚠️ Errores frecuentes

La tabla se usa buscando el síntoma. En esta clase casi todos vienen de un alcance sin límites o de supuestos no declarados.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se diseña el banco y luego se mira el capital | El capital fija el tamaño | Empieza por la capacidad. |
| No se verifica la escala | Errores de unidades | Verifica antes de sumar. |
| Rentabilidad sin comparar con el costo del capital | Puede destruir valor | Compara siempre. |
| Supuestos no declarados | El resultado no es interpretable | Regístralos antes del cálculo. |
| Compromisos sin decisiones que los sostengan | Incoherencia | Cada cifra con su decisión. |
| Datos no sintéticos | Riesgo real | Solo datos generados. |

## ❓ Preguntas de comprobación

1. ¿Por qué el criterio de mayor peso del proyecto es la coherencia?
2. ¿Por qué el capital inicial determina el tamaño del banco y no al revés?
3. ¿Qué se declara antes de un cálculo y por qué?
4. ¿Qué significa que un banco proyecte 14,63 % con un costo de capital de 17,68 %?
5. ¿Qué función cumplen los cuatro compromisos de diseño?

## 📥 Entregable

Guarda en `portfolio/parte-16/clase-01/`:

- el cálculo de capacidad de activos ponderados y de cartera;
- la verificación de coherencia de escala;
- la proyección de resultado en régimen y su comparación con el costo del capital;
- los cuatro compromisos de diseño, con las clases que deberán sostenerlos.

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

- Basel Committee on Banking Supervision (2017). *Basel III: Finalising post-crisis reforms*. BIS.
- Rose, P. y Hudgins, S. (2013). *Bank Management and Financial Services* (9.ª ed.). McGraw-Hill.
- Damodaran, A. (2012). *Investment Valuation* (3.ª ed.). Wiley. Costo del capital y prima por tamaño.
- Basel Committee on Banking Supervision (2012). *Core Principles for Effective Banking Supervision*, criterios de licenciamiento. BIS.
- Matten, C. (2000). *Managing Bank Capital* (2.ª ed.). Wiley.
- Verificación local: revisa el capital mínimo exigido para constituir un banco en tu país y los requisitos de licenciamiento.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← Índice de la parte](../README.md) | [Parte 16](../README.md) · [Programa](../../../SYLLABUS.md) | [02 · Modelo de negocio del banco →](02-modelo-de-negocio-del-banco.md) |
<!-- gen:footer:end -->
