---
part: 14
class: 11
title: "Ética algorítmica y sesgo"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 11 · Ética algorítmica y sesgo

> [← 10 · Monedas digitales de banco central](10-monedas-digitales-de-banco-central.md) · [Índice de la parte](../README.md) · [12 · Regulación de la tecnología financiera →](12-regulacion-de-la-tecnologia-financiera.md)

**Parte 14 — Fintech, datos e inteligencia artificial** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Detectar y corregir la discriminación producida por sistemas automatizados. Un modelo que nunca ve el
atributo protegido puede discriminar igual, y esta clase enseña por qué ocurre, cómo se mide y qué se
puede hacer al respecto — incluyendo lo que **no** se puede resolver técnicamente.

Las clases 6 y 7 usan modelos que deciden sobre personas. Esta trata de que decidan de forma justa, y su resultado más incómodo es matemático: existen varias definiciones razonables de equidad y está demostrado que no se pueden cumplir todas a la vez. Elegir cuál se cumple es una decisión que hay que tomar y declarar.

## 📚 Objetivos

Al finalizar podrás:

1. **Explicar** cómo un modelo discrimina sin usar el atributo protegido.
2. **Aplicar** las definiciones formales de equidad y su incompatibilidad.
3. **Medir** el sesgo de un sistema con métricas verificables.
4. **Aplicar** técnicas de mitigación y evaluar su costo.
5. **Diseñar** la explicabilidad y el derecho a revisión.

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

Los tres primeros términos son las formas de discriminación; los cinco siguientes, las definiciones de equidad y su medición. El **impacto dispar** es la forma que aparece sin intención: un modelo que no usa ningún atributo protegido puede producir resultados sistemáticamente peores para un grupo.

| Concepto | Comprensión verificable |
|---|---|
| `atributo protegido` | Característica sobre la que la ley prohíbe discriminar. |
| `variable sustituta` | Dato correlacionado con un atributo protegido. |
| `discriminación directa` | Trato distinto por el atributo protegido. |
| `impacto dispar` | Efecto desigual sobre un grupo, sin trato explícito distinto. |
| `paridad demográfica` | Igual tasa de aprobación entre grupos. |
| `igualdad de oportunidad` | Igual tasa de acierto entre grupos, entre los que sí pagan. |
| `calibración por grupo` | Que la probabilidad predicha signifique lo mismo en cada grupo. |
| `explicabilidad` | Justificar una decisión individual en términos comprensibles. |

## 🧠 Modelo mental

El modelo mental es un conflicto sin solución técnica: paridad demográfica, igualdad de oportunidad y calibración por grupo son incompatibles entre sí salvo en casos triviales. No hay un modelo justo; hay un modelo que cumple la definición de equidad que la entidad eligió y justificó.

```text
UN MODELO NO NECESITA VER EL ATRIBUTO PARA DISCRIMINAR

  el código postal correlaciona con el origen étnico
  el tipo de teléfono correlaciona con el ingreso
  la antigüedad laboral correlaciona con la edad y el género
  el sector de actividad correlaciona con el género
  el nombre correlaciona con el origen

  quitar la variable protegida NO elimina el sesgo:
  lo hace INVISIBLE

Y HAY UNA RAZÓN MÁS PROFUNDA
  el modelo aprende de decisiones históricas
  si esas decisiones discriminaban,
  el modelo aprende a reproducir esa discriminación
  con eficiencia y a escala
```

## 📖 Desarrollo

### 1. Cómo se produce el sesgo

El sesgo entra por vías identificables y ninguna requiere mala intención. La tabla las recoge.

```text
FUENTES, EN ORDEN DE FRECUENCIA

1. SESGO EN LOS DATOS HISTÓRICOS
   el modelo aprende de decisiones pasadas sesgadas

2. SESGO DE MUESTRA
   un grupo está subrepresentado
   → el modelo predice peor para ese grupo

3. SESGO DE ETIQUETA
   el resultado que se predice está sesgado
   (se predice "incumplimiento reportado",
    y algunos grupos se reportan más que otros)

4. VARIABLES SUSTITUTAS
   sin la variable protegida, sus sustitutas hacen el trabajo

5. SESGO DE RETROALIMENTACIÓN
   se rechaza a un grupo, no se generan datos suyos,
   el modelo se reentrena y confirma su sesgo

6. SESGO DE AGREGACIÓN
   un modelo único para poblaciones distintas
   funciona bien para la mayoritaria y mal para el resto
```

**El sesgo de retroalimentación es el más difícil de detectar** porque los datos nunca contradicen al
modelo: al no prestar a un grupo, nunca se observa que habría pagado.

### 2. Definiciones de equidad y su incompatibilidad

Las definiciones son varias y demostradamente incompatibles. La tabla las recoge con su conflicto.

```text
TRES DEFINICIONES RAZONABLES

  PARIDAD DEMOGRÁFICA
    igual tasa de aprobación en todos los grupos

  IGUALDAD DE OPORTUNIDAD
    entre quienes SÍ habrían pagado,
    igual tasa de aprobación en todos los grupos

  CALIBRACIÓN
    una probabilidad predicha de 8 % significa
    un 8 % real en todos los grupos
```

```text
RESULTADO DE IMPOSIBILIDAD (demostrado formalmente)
  si la tasa base de incumplimiento DIFIERE entre grupos,
  no se pueden satisfacer las tres a la vez

  → hay que ELEGIR cuál se prioriza
  → y esa elección es NORMATIVA, no técnica

  un equipo técnico que elige sin declarar la elección
  está tomando una decisión de política
  sin mandato para hacerlo
```

| Definición | Cuándo priorizarla |
|---|---|
| Paridad demográfica | Cuando el objetivo es corregir exclusión histórica |
| Igualdad de oportunidad | Cuando el objetivo es no perjudicar a quien cumpliría |
| Calibración | Cuando la probabilidad se usa para fijar precio |

### 3. Medición

El sesgo se mide con métricas concretas por grupo. El procedimiento las calcula.

```text
MÉTRICAS POR GRUPO, TODAS NECESARIAS

  tasa de aprobación
  tasa de aprobación a igual nivel de riesgo predicho
  tasa de falsos negativos (buenos rechazados)
  tasa de falsos positivos (malos aprobados)
  calibración: predicho vs. observado
  precio medio a igual riesgo
```

```text
LA MÉTRICA MÁS REVELADORA
  aprobación A IGUAL NIVEL DE RIESGO PREDICHO

  si a un mismo nivel de riesgo predicho
  un grupo se aprueba menos que otro,
  hay discriminación en la DECISIÓN, no en el modelo

  si a igual riesgo predicho la aprobación es igual
  pero la distribución de riesgo predicho difiere,
  el problema está en el MODELO o en la REALIDAD
  → y distinguir entre ambas cosas exige más análisis
```

### 4. Mitigación

La mitigación se puede aplicar antes, durante o después del entrenamiento. La tabla recoge las opciones.

| Momento | Técnica | Efecto |
|---|---|---|
| Antes del modelo | Reponderar o rebalancear la muestra | Corrige subrepresentación |
| Antes | Auditar variables sustitutas y retirarlas | Reduce el canal indirecto |
| Durante | Restricción de equidad en el entrenamiento | Optimiza sujeto a la restricción |
| Después | Umbrales distintos por grupo | Efectivo y jurídicamente delicado |
| Después | Revisión humana de los rechazos del grupo afectado | Corrige casos, no el modelo |
| Proceso | Datos alternativos que amplíen la información | Reduce el rechazo por desconocimiento |

```text
EL INTERCAMBIO ES REAL
  toda restricción de equidad reduce el poder predictivo
  → más pérdida esperada, o menos aprobación total

  el costo debe cuantificarse y decidirse explícitamente
  con quien tiene el mandato para decidirlo

  presentarlo como "el modelo es justo ahora"
  sin declarar el costo es ocultar la decisión
```

```text
LA MITIGACIÓN MÁS EFECTIVA NO ES TÉCNICA
  ampliar la INFORMACIÓN disponible sobre el grupo
  desfavorecido (clase 7) reduce el rechazo
  por desconocimiento sin sacrificar poder predictivo

  el sesgo por falta de datos se corrige con datos,
  no con restricciones al modelo
```

### 5. Explicabilidad y revisión

Una decisión adversa exige poder explicarse y poder revisarse. La tabla recoge los requisitos.

```text
QUÉ DEBE PODER EXPLICARSE
  · los factores principales que llevaron a la decisión
  · en términos comprensibles para el afectado
  · con indicación de qué podría cambiar el resultado
  · sin revelar información que permita manipular el sistema

EJEMPLO DE EXPLICACIÓN ÚTIL
  "la solicitud no fue aprobada principalmente porque
   la relación entre tus obligaciones mensuales y tus ingresos
   verificados supera el límite de la política (48 % frente
   a un máximo de 40 %). Reducir tus obligaciones existentes
   o acreditar ingresos adicionales cambiaría la evaluación."

EJEMPLO DE EXPLICACIÓN INÚTIL
  "la solicitud no cumple los criterios de evaluación vigentes"
```

| Derecho | Qué implica operativamente |
|---|---|
| Explicación | Motivos concretos de la decisión individual |
| Intervención humana | Revisión por una persona con autoridad |
| Impugnación | Canal, plazo y respuesta fundamentada |
| Corrección de datos | Rectificar el dato inexacto y reevaluar |

## 🧮 Ejemplo guiado

El ejemplo mide el sesgo de un modelo con tres definiciones de equidad. El modelo cumple una y falla las otras dos, que es el resultado normal.

**Situación.** Una auditoría de equidad sobre el modelo de admisión de consumo.

```text
EL MODELO
  no usa género, edad, origen ni estado civil
  usa 34 variables: ingreso, antigüedad, endeudamiento,
  sector, comportamiento de pago, antigüedad de cuenta,
  tipo de contrato, entre otras

RESULTADOS POR GRUPO (población de 28 000 solicitudes)
                        solicitudes  aprobación  mora observada
  hombres                  15 400       46,2 %       4,4 %
  mujeres                  12 600       38,1 %       3,6 %

  menores de 30             8 200       31,4 %       6,1 %
  30 a 50                  14 100       48,6 %       3,8 %
  mayores de 50             5 700       44,2 %       3,2 %
```

**Paso 1 — evalúa la primera señal.**

```text
BRECHA DE APROBACIÓN POR GÉNERO: 8,1 puntos
Y LA MORA DE LAS MUJERES ES MENOR: 3,6 % vs. 4,4 %

  se aprueba menos a un grupo que incumple menos
  → señal fuerte de sesgo
```

**Paso 2 — verifica la aprobación a igual riesgo predicho.**

```text
TASA DE APROBACIÓN POR DECIL DE RIESGO PREDICHO

  decil    hombres    mujeres
   1-2      92,4 %     92,1 %
   3-4      78,6 %     78,9 %
   5-6      54,2 %     53,8 %
   7-8      21,4 %     21,6 %
   9-10      2,1 %      2,0 %

A IGUAL RIESGO PREDICHO, LA APROBACIÓN ES IGUAL
→ no hay discriminación en la DECISIÓN
→ el sesgo, si existe, está en el MODELO
```

**Paso 3 — verifica la calibración por grupo.**

```text
RIESGO PREDICHO vs. MORA OBSERVADA

  decil    predicho  observado H  observado M
   1-2       1,2 %      1,3 %        0,9 %
   3-4       2,8 %      2,9 %        2,1 %
   5-6       5,1 %      5,2 %        3,8 %
   7-8       9,4 %      9,6 %        7,1 %
   9-10     18,2 %     18,4 %       13,9 %

EL MODELO ESTÁ CALIBRADO PARA HOMBRES
Y SOBREESTIMA EL RIESGO DE LAS MUJERES
  en el decil 5-6: predice 5,1 % y ocurre 3,8 %
  sobreestimación relativa: 34 %
```

**Paso 4 — investiga la causa.**

```text
ANÁLISIS DE CONTRIBUCIÓN DE VARIABLES POR GRUPO

  variable                 peso en el modelo   diferencia H/M
  antigüedad laboral            alto            H: 6,8 años
                                                M: 4,2 años
  continuidad de ingresos       alto            H: 94 % de meses
                                                M: 81 % de meses
  sector de actividad           medio           distribución muy distinta
  tipo de contrato              medio           H: 71 % indefinido
                                                M: 54 % indefinido
```

```text
DIAGNÓSTICO
  las variables de ESTABILIDAD LABORAL
  penalizan sistemáticamente a las mujeres
  por interrupciones asociadas al cuidado

  y esas interrupciones NO predicen incumplimiento
  en el mismo grado que otras interrupciones:
  el modelo las trata igual y son distintas

  → SESGO DE ETIQUETA Y DE AGREGACIÓN COMBINADOS
```

**Paso 5 — cuantifica el efecto.**

```text
SI EL MODELO ESTUVIERA CALIBRADO PARA MUJERES
  el riesgo predicho bajaría un 26 % en promedio
  la aprobación subiría de 38,1 % a 45,7 %
  solicitudes adicionales aprobadas: 958 mensuales

  mora esperada de esas 958: 5,2 %
  (bajo el umbral de corte del banco, que es 6,0 %)

  → son solicitudes que el banco DEBERÍA aprobar
    según su propio criterio de riesgo
```

**Paso 6 — evalúa las alternativas de corrección.**

```text
OPCIÓN A — modelo separado por grupo
  técnicamente efectivo
  jurídicamente delicado: usar el atributo protegido
  para construir el modelo puede constituir
  discriminación directa en muchas jurisdicciones
  → verificar el marco legal aplicable

OPCIÓN B — recalibración post-modelo por grupo
  ajustar la probabilidad predicha para que
  esté calibrada en cada grupo
  efecto: corrige la sobreestimación
  mismo problema jurídico que A, en menor grado

OPCIÓN C — rediseño de las variables
  sustituir "antigüedad laboral continua" por
  "meses de ingreso verificado en los últimos 24"
  → captura capacidad de pago sin penalizar
    la forma de la trayectoria
  efecto estimado: reduce la sobreestimación
  de 34 % a 11 %

OPCIÓN D — datos adicionales
  incorporar los datos alternativos de la clase 7
  para el grupo con trayectoria discontinua
  efecto: reduce la sobreestimación a 6 %
```

**Paso 7 — evalúa el costo de cada opción.**

```text
                    sobreestimación  poder predictivo  aprobación
                    residual         (Gini)            adicional
  sin corregir           34 %          0,58                 0
  opción B               0 %           0,58               958
  opción C              11 %           0,56               612
  opción D               6 %           0,59               812
  opción C+D             4 %           0,59               874

la opción D MEJORA el poder predictivo
porque añade información en lugar de restringir
```

**Paso 8 — decide y documenta.**

```text
DECISIÓN: opciones C y D combinadas

MOTIVOS
  · corrige el 88 % de la sobreestimación
  · mejora el poder predictivo del modelo (0,58 → 0,59)
  · no requiere usar el atributo protegido
  · aprueba 874 solicitudes adicionales mensuales
    que cumplen el criterio de riesgo del propio banco

CUANTIFICACIÓN
  colocación adicional: 874 × 3,2 = 2 797 mensuales
  margen neto de riesgo: 2 797 × 6,1 % = 171 mensuales
  = 2 046 anuales
  costo de la corrección: 340 inicial + 90 anuales

DOCUMENTACIÓN OBLIGATORIA
  1. la decisión de equidad tomada y su fundamento
  2. la definición de equidad priorizada: calibración
  3. las métricas por grupo, reportadas trimestralmente
  4. el análisis de variables sustitutas, anual
  5. el proceso de revisión humana de rechazos
     del grupo afectado, con su desempeño

Y LA CONCLUSIÓN QUE SE ELEVA AL COMITÉ
  el modelo no discriminaba en su decisión
  discriminaba en su MEDICIÓN
  y corregirlo mejoró simultáneamente
  la equidad y la rentabilidad
```

**Interpreta:** el modelo no usaba el género, la decisión era idéntica a igual riesgo predicho y **el
sistema discriminaba de todos modos**, porque el riesgo predicho estaba sistemáticamente sobreestimado
para un grupo. El caso muestra el resultado más importante de la clase: **el sesgo no siempre implica un
intercambio con la rentabilidad**. Aquí, corregirlo aprobó 874 solicitudes adicionales que el propio
banco consideraba buenas y que estaba rechazando por un error de medición.

## 🏦 Del cliente al banco

El cliente recibe un rechazo y el banco tiene que poder demostrar que el criterio no discrimina. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Me rechazaron y no sé por qué» | Derecho a explicación concreta | 14, clase 11 |
| «Mi pareja con el mismo ingreso sí calificó» | Variables sustitutas | 14, clase 11 |
| «El sistema no entiende mi trayectoria» | Sesgo de agregación | 14, clase 11 |
| «Pedí que lo revisara una persona» | Derecho a intervención humana | 14, clase 6 |
| «Corregí un dato y cambió la decisión» | Derecho a rectificación | 12, clase 10 |

## 🧪 Práctica

El laboratorio pide medir el sesgo de un modelo y elegir una definición de equidad justificada. La justificación es lo que se evalúa.

En `labs/lab-06.md`:

1. Identifica variables sustitutas de atributos protegidos en un conjunto de variables.
2. Mide las seis métricas de equidad por grupo sobre un modelo sintético.
3. Distingue si el sesgo está en la decisión, en el modelo o en la realidad.
4. Evalúa cuatro opciones de mitigación por su efecto y su costo.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen modelos con sesgo no detectado. Las causas son variables sustitutas y equidad no medida por grupo.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se quita la variable protegida y se declara resuelto | Sustitutas siguen actuando | Audita las sustitutas. |
| Se elige una definición de equidad sin declararlo | Decisión normativa sin mandato | Explicita y eleva la elección. |
| Se mide solo la tasa de aprobación agregada | Oculta el mecanismo | Mide a igual riesgo predicho. |
| Se ignora la calibración por grupo | El sesgo está en la medición | Compara predicho y observado. |
| Se supone que corregir cuesta rentabilidad | No siempre | Añadir información puede mejorar ambas. |
| Explicación genérica al rechazado | No cumple el derecho | Motivos concretos y accionables. |

## ❓ Preguntas de comprobación

1. ¿Por qué quitar el atributo protegido no elimina el sesgo?
2. ¿Qué establece el resultado de imposibilidad entre definiciones de equidad?
3. ¿Qué distingue el sesgo en la decisión del sesgo en el modelo?
4. ¿Por qué el sesgo de retroalimentación es el más difícil de detectar?
5. ¿Por qué corregir un sesgo puede mejorar la rentabilidad?

## 📥 Entregable

Guarda en `portfolio/parte-14/clase-11/`:

- las variables sustitutas identificadas con su correlación;
- las seis métricas de equidad medidas por grupo;
- el diagnóstico del origen del sesgo con su evidencia;
- la evaluación de las opciones de mitigación con su costo y efecto.

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

- Barocas, S., Hardt, M. y Narayanan, A. (2023). *Fairness and Machine Learning: Limitations and Opportunities*. MIT Press. <https://fairmlbook.org/>
- Kleinberg, J., Mullainathan, S. y Raghavan, M. (2017). "Inherent Trade-Offs in the Fair Determination of Risk Scores". *ITCS 2017*. Resultado de imposibilidad.
- Hardt, M., Price, E. y Srebro, N. (2016). "Equality of Opportunity in Supervised Learning". *NIPS 2016*.
- NIST (2022). *Towards a Standard for Identifying and Managing Bias in Artificial Intelligence* (NIST SP 1270). NIST.
- Consumer Financial Protection Bureau (2023). *Adverse action notification requirements in connection with credit decisions based on complex algorithms*. CFPB.
- OECD (2021). *Artificial Intelligence, Machine Learning and Big Data in Finance*. OECD.
- Verificación local: revisa los atributos protegidos por la normativa antidiscriminación de tu país y las obligaciones de notificación de rechazo de crédito.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 10 · Monedas digitales de banco central](10-monedas-digitales-de-banco-central.md) | [Parte 14](../README.md) · [Programa](../../../SYLLABUS.md) | [12 · Regulación de la tecnología financiera →](12-regulacion-de-la-tecnologia-financiera.md) |
<!-- gen:footer:end -->
