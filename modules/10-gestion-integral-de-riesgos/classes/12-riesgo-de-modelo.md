---
part: 11
class: 12
title: "Riesgo de modelo"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 12 · Riesgo de modelo

> [← 11 · Riesgo tecnológico y ciberseguridad](11-riesgo-tecnologico-y-ciberseguridad.md) · [Índice de la parte](../README.md) · [13 · Pruebas de estrés →](13-pruebas-de-estres.md)

**Parte 11 — Gestión integral de riesgos** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Gestionar el riesgo de decidir mal por confiar en un modelo. Los bancos aprueban créditos, calculan
capital, fijan precios y detectan fraude con modelos; cuando un modelo está mal construido, mal usado o
aplicado fuera de su dominio, el error se produce a escala industrial y en la misma dirección.

Las clases anteriores usan modelos para medir riesgos. Esta trata el riesgo de que esos modelos estén mal, que es una categoría propia desde que un modelo puede decidir miles de operaciones al día. Y su parte más difícil no es técnica: es que el modelo se usa como coartada para decisiones que nadie quiere firmar.

## 📚 Objetivos

Al finalizar podrás:

1. **Definir** riesgo de modelo y sus tres fuentes.
2. **Aplicar** un ciclo de vida completo de gestión de modelos.
3. **Ejecutar** una validación independiente con sus componentes.
4. **Monitorear** el deterioro de un modelo en producción.
5. **Evaluar** los riesgos específicos de los modelos de aprendizaje automático.

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

Los tres primeros términos son el modelo y su control; los cinco siguientes, las formas en que deja de funcionar. La **deriva de concepto** es la más difícil de detectar: la relación entre las variables y el resultado cambia, y el modelo sigue prediciendo con confianza sobre una realidad distinta.

| Concepto | Comprensión verificable |
|---|---|
| `modelo` | Método cuantitativo que procesa datos para producir una estimación. |
| `riesgo de modelo` | Pérdida por decisiones basadas en modelos incorrectos o mal usados. |
| `validación independiente` | Revisión por quien no lo construyó ni lo usa. |
| `dominio de aplicación` | Rango de datos y condiciones donde el modelo es válido. |
| `deriva de población` | Cambio en la distribución de los datos de entrada. |
| `deriva de concepto` | Cambio en la relación entre entradas y resultado. |
| `sobreajuste` | El modelo aprendió el ruido de la muestra, no el patrón. |
| `explicabilidad` | Capacidad de justificar una predicción individual. |

## 🧠 Modelo mental

El modelo mental es un modelo con fecha de caducidad: todo modelo se construyó sobre una población y un contexto, y ambos cambian. La pregunta no es si el modelo es correcto sino si sigue siéndolo, y eso exige medirlo periódicamente.

```text
TRES FUENTES DEL RIESGO DE MODELO

1. EL MODELO ESTÁ MAL          error de datos, de especificación,
                                de implementación, de calibración

2. EL MODELO SE USA MAL        fuera de su dominio, para una decisión
                                distinta de aquella para la que se construyó

3. EL MODELO ESTÁ BIEN Y SE USA BIEN
   pero el mundo cambió        deriva de población o de concepto

la tercera es la más peligrosa
porque no hay nada que "corregir": todo funcionó como se diseñó
```

## 📖 Desarrollo

### 1. Ciclo de vida

Un modelo tiene un ciclo con etapas y controles en cada una. La tabla lo recorre.

```text
1. DEFINICIÓN      ¿qué decisión apoya? ¿qué se estima exactamente?
2. DATOS           origen, calidad, representatividad, linaje
3. DESARROLLO      especificación, estimación, pruebas fuera de muestra
4. DOCUMENTACIÓN   supuestos, limitaciones, dominio de aplicación
5. VALIDACIÓN      independiente, antes del uso
6. APROBACIÓN      comité, con condiciones y vigencia
7. IMPLANTACIÓN    verificación de que el código replica el modelo
8. USO             según lo aprobado, con anulaciones registradas
9. MONITOREO       desempeño, estabilidad, deriva
10. REVALIDACIÓN   periódica y ante cambios materiales
11. RETIRO         con plan de sustitución
```

**El paso 7 se subestima constantemente.** Un modelo correcto implementado con un error de código
produce decisiones incorrectas indistinguibles de un modelo incorrecto. La verificación de implantación
—recalcular una muestra con dos implantaciones independientes— es barata y detecta este caso.

### 2. Validación independiente

La validación la hace quien no construyó el modelo, y revisa cosas concretas. La tabla las recoge.

| Componente | Qué revisa | Pregunta central |
|---|---|---|
| Conceptual | Teoría y especificación | ¿La forma del modelo es adecuada al problema? |
| Datos | Calidad, representatividad, linaje | ¿Los datos representan la población de uso? |
| Resultados | Desempeño dentro y fuera de muestra | ¿Discrimina y calibra bien? |
| Implantación | Código contra especificación | ¿Lo que corre es lo que se aprobó? |
| Uso | Decisiones reales | ¿Se usa como se aprobó? |
| Gobierno | Roles, documentación, controles | ¿Hay trazabilidad? |

```text
INDEPENDENCIA REAL exige que el validador
  · no participe en el desarrollo
  · no dependa jerárquicamente del área usuaria
  · tenga autoridad para rechazar
  · tenga acceso completo a datos y código

si el validador no puede decir "no", no está validando
```

### 3. Medidas de desempeño

El desempeño se mide con métricas de discriminación y de calibración, que dicen cosas distintas. La tabla las separa.

```text
DISCRIMINACIÓN — ¿separa buenos de malos?
  Gini, área bajo la curva, estadístico de Kolmogorov-Smirnov

CALIBRACIÓN — ¿los niveles predichos coinciden con los observados?
  un modelo puede discriminar perfectamente y estar mal calibrado:
  ordena bien y predice 3 % donde ocurre 8 %

ESTABILIDAD — ¿la población sigue siendo la misma?
  índice de estabilidad poblacional (PSI)
```

| Índice de estabilidad | Interpretación |
|---:|---|
| < 0,10 | Población estable |
| 0,10 – 0,25 | Cambio moderado; investigar |
| > 0,25 | Cambio significativo; revalidar |

```text
DISTINCIÓN CLAVE
  DERIVA DE POBLACIÓN   cambian las entradas (PSI lo detecta)
  DERIVA DE CONCEPTO    cambia la relación entrada→salida
                        el PSI NO la detecta
                        solo se ve al comparar predicho vs. observado
```

### 4. Riesgos específicos del aprendizaje automático

Los modelos de aprendizaje automático añaden riesgos que los tradicionales no tienen. La tabla los recoge.

| Riesgo | Por qué es mayor aquí | Mitigación |
|---|---|---|
| Sobreajuste | Muchos parámetros, alta flexibilidad | Validación cruzada, muestra fuera de tiempo |
| Fuga de información | Variables que contienen el resultado | Auditoría del linaje de cada variable |
| Sesgo | Aprende patrones históricos discriminatorios | Pruebas de equidad por grupo |
| Falta de explicabilidad | Relación no lineal, muchas variables | Métodos de atribución; modelo simple de respaldo |
| Inestabilidad | Sensible a cambios pequeños en los datos | Pruebas de robustez |
| Dependencia de datos externos | Proveedor cambia sin aviso | Contrato y monitoreo del insumo |

```text
LA FUGA DE INFORMACIÓN es el error más común y menos detectado

  ejemplo: incluir "número de gestiones de cobranza" como variable
  predictora de incumplimiento

  la gestión de cobranza OCURRE PORQUE el cliente ya está en mora
  el modelo muestra un poder predictivo excelente en desarrollo
  y falla completamente en producción, donde esa variable
  no está disponible antes de la decisión
```

### 5. Uso: anulaciones y el modelo como coartada

El mayor riesgo de modelo suele estar en su uso y no en su construcción. La tabla recoge los patrones.

```text
ANULACIÓN (override)
  el analista decide distinto de lo que el modelo recomienda

  tasa de anulación baja (< 5 %)   → el modelo se usa
  tasa alta (> 20 %)               → el modelo no se cree, o está mal
  tasa cero                        → nadie está pensando

TODA ANULACIÓN DEBE REGISTRARSE con su motivo
y su desempeño posterior debe medirse:
  si las anulaciones tienen mejor desempeño que el modelo,
  el analista sabe algo que el modelo no captura → incorpóralo
  si tienen peor desempeño, el sesgo humano está costando dinero
```

**El modelo como coartada.** Cuando una decisión sale mal, «lo dijo el modelo» no es una explicación: es
una renuncia a la responsabilidad. El marco de gestión de modelos existe, entre otras razones, para
mantener identificable a la persona que responde por cada decisión.

## 🧮 Ejemplo guiado

El ejemplo detecta una deriva en un modelo en producción. Conviene comparar la deriva de población con la de concepto: la primera es visible y la segunda no.

**Situación.** Un modelo de admisión de créditos de consumo se deteriora y se investiga.

```text
MODELO
  scoring de admisión, desarrollado hace 26 meses
  muestra de desarrollo: 180 000 solicitudes de 2 años previos
  Gini en desarrollo: 0,58
  Gini en validación fuera de muestra: 0,55

DESEMPEÑO EN PRODUCCIÓN (por trimestre)
  T1: Gini 0,54   PSI 0,04   tasa de mora observada 2,8 %  predicha 2,9 %
  T2: Gini 0,53   PSI 0,06   observada 3,1 %  predicha 2,9 %
  T3: Gini 0,51   PSI 0,11   observada 3,9 %  predicha 3,0 %
  T4: Gini 0,44   PSI 0,19   observada 5,8 %  predicha 3,1 %
  T5: Gini 0,39   PSI 0,31   observada 7,4 %  predicha 3,2 %
```

**Paso 1 — diagnostica el tipo de deterioro.**

```text
DISCRIMINACIÓN: Gini 0,55 → 0,39   caída de 29 %
CALIBRACIÓN:    predicha 3,2 % vs. observada 7,4 %
                subestimación de 4,2 puntos → factor 2,3

ESTABILIDAD:    PSI 0,04 → 0,31   cambio significativo

hay deriva de POBLACIÓN (PSI alto)
y deriva de CONCEPTO (la calibración se rompió más que la discriminación)
```

**Paso 2 — descompón el PSI por variable.**

```text
variable                        PSI    dirección del cambio
antigüedad laboral             0,14    población más joven laboralmente
ingreso declarado              0,03    estable
razón deuda/ingreso            0,09    creciente
canal de originación           0,21    migración masiva a canal digital
región                         0,02    estable
producto solicitado            0,04    estable

el mayor contribuyente: CANAL DE ORIGINACIÓN
```

**Paso 3 — investiga el canal.**

```text
composición por canal:
              desarrollo   T5
  sucursal        78 %     31 %
  digital         22 %     69 %

el modelo se desarrolló con una población
mayoritariamente originada en sucursal
```

**Paso 4 — mide el desempeño por canal.**

```text
en T5:
  originación en sucursal:  Gini 0,52   mora observada 3,4 %  predicha 3,1 %
  originación digital:      Gini 0,31   mora observada 9,2 %  predicha 3,2 %

EL MODELO SIGUE FUNCIONANDO EN SUCURSAL
Y NO FUNCIONA EN DIGITAL
```

**Paso 5 — identifica la causa.**

```text
el canal digital NO es solo un canal distinto: trae otra población

  · sin contacto presencial → menos verificación documental
  · autoselección: quien no pasaría en sucursal prueba en digital
  · el modelo usa variables declaradas que en sucursal se contrastaban
    con documentos y en digital no

el modelo se aplicó FUERA DE SU DOMINIO
y nadie lo notó porque el dominio nunca se documentó
como "originación con verificación presencial"
```

**Paso 6 — cuantifica el costo.**

```text
originación digital en los últimos 12 meses: 148 000 millones
mora observada 9,2 % vs. la esperada 3,2 %
exceso: 6,0 puntos → 8 880 millones de exposición en mora
LGD 52 % → PÉRDIDA ADICIONAL: 4 618 millones

el precio de los créditos se fijó con la PD del modelo:
  tasa cobrada incluía prima de riesgo de 3,2 %
  riesgo real 9,2 %
  → la cartera digital se originó con precio insuficiente
    durante 12 meses
```

**Paso 7 — evalúa qué falló en el gobierno del modelo.**

```text
MONITOREO
  el PSI superó 0,10 en T3 (hace 3 trimestres)
  umbral de alerta definido: 0,25
  → el umbral era demasiado alto y se llegó tarde

  la desviación de calibración en T3 era ya de 0,9 puntos
  → NO existía un umbral de alerta sobre calibración

DOMINIO DE APLICACIÓN
  el documento del modelo no declaraba restricción de canal
  → el uso en digital no requirió aprobación adicional

REVALIDACIÓN
  programada cada 36 meses
  → demasiado espaciada para un modelo de admisión
```

**Paso 8 — decisiones.**

```text
1. INMEDIATO
   suspender el uso del modelo en canal digital
   admisión digital con criterios expertos más restrictivos
   hasta contar con modelo específico

2. MODELO
   desarrollar un modelo de admisión para canal digital
   con muestra propia y variables verificables sin presencia

3. GOBIERNO DE MODELOS
   · declarar el dominio de aplicación en TODOS los modelos,
     incluyendo canal, segmento y período de validez
   · umbral de alerta de PSI: 0,10 (no 0,25)
   · añadir umbral de alerta de calibración: desviación > 25 %
     entre predicho y observado durante dos trimestres
   · revalidación de modelos de admisión: cada 12 meses
   · cualquier cambio de canal, segmento o proceso de originación
     exige revisión previa del modelo afectado

4. PRECIO
   recalcular la prima de riesgo del canal digital
   y reflejarla en la tasa de las nuevas colocaciones

5. CAPITAL
   reconocer en el Pilar 2 el riesgo de modelo
   mientras no exista un modelo específico validado
```

**Interpreta:** el modelo **nunca se rompió**. Siguió funcionando exactamente donde fue construido para
funcionar, con un Gini de 0,52 en sucursal. Lo que ocurrió fue que **la organización lo aplicó a una
población distinta sin revisarlo**, porque su documentación no decía a qué población se aplicaba. Ese es
el riesgo de modelo en estado puro: la falla no está en la estadística, está en el gobierno.

## 🏦 Del cliente al banco

El cliente recibe una decisión de un modelo y el banco responde por ella. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «El sistema me rechazó y nadie me explica» | Explicabilidad y derecho a revisión | 14, clase 11 |
| «Me aprobaron un monto que no puedo pagar» | Modelo fuera de su dominio | 11, clase 12 |
| «La tasa de mi crédito digital es más alta» | Prima de riesgo por canal | 15, clase 7 |
| «Un ejecutivo revirtió la decisión» | Anulación registrada y medida | 9, clase 8 |
| «Los modelos discriminan» | Sesgo aprendido de datos históricos | 14, clase 11 |

## 🧪 Práctica

El laboratorio pide validar un modelo y detectar su deriva. El modelo mantiene su discriminación y ha perdido calibración, que es el caso difícil.

En `labs/lab-06.md`, sección de modelos:

1. Ejecuta una validación independiente sobre un modelo sintético con sus seis componentes.
2. Calcula el índice de estabilidad poblacional y descompónlo por variable.
3. Distingue deriva de población de deriva de concepto en una serie de desempeño.
4. Documenta el dominio de aplicación de un modelo y las condiciones que lo invalidan.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen modelos que fallaron en producción. Las causas son deriva no vigilada y uso fuera del dominio de aplicación.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| El modelo falla al cambiar el canal | Dominio no documentado | Declara canal, segmento y vigencia. |
| Se monitorea discriminación y no calibración | Métrica incompleta | Añade umbral de calibración. |
| Umbral de alerta demasiado alto | Se llega tarde | PSI 0,10 como alerta. |
| Variable que contiene el resultado | Fuga de información | Audita el linaje de cada variable. |
| Anulaciones no registradas | Sin aprendizaje | Registra motivo y mide desempeño. |
| «Lo dijo el modelo» | Responsabilidad diluida | La decisión siempre tiene dueño. |

## ❓ Preguntas de comprobación

1. ¿Cuáles son las tres fuentes del riesgo de modelo y cuál es la más peligrosa?
2. ¿Qué diferencia la deriva de población de la deriva de concepto?
3. ¿Por qué un modelo puede discriminar bien y estar mal calibrado?
4. ¿Qué es la fuga de información y por qué produce modelos excelentes que fallan?
5. ¿Qué indica una tasa de anulación de cero?

## 📥 Entregable

Guarda en `portfolio/parte-11/clase-12/`:

- la validación independiente con sus seis componentes;
- el índice de estabilidad descompuesto por variable;
- el diagnóstico del tipo de deriva con su evidencia;
- el documento de dominio de aplicación del modelo.

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

- Board of Governors of the Federal Reserve System y OCC (2011). *SR 11-7: Guidance on Model Risk Management*. <https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm>
- European Banking Authority (2017). *Guidelines on internal governance* y guías de validación de modelos internos. EBA.
- Basel Committee on Banking Supervision (2005). *Studies on the Validation of Internal Rating Systems*. BIS. <https://www.bis.org/publ/bcbs_wp14.htm>
- Siddiqi, N. (2017). *Intelligent Credit Scoring* (2.ª ed.). Wiley. Desarrollo, validación y monitoreo.
- Hastie, T., Tibshirani, R. y Friedman, J. (2009). *The Elements of Statistical Learning* (2.ª ed.). Springer. Sobreajuste y validación.
- Verificación local: revisa las exigencias de validación independiente, revalidación y aprobación de modelos que aplica tu supervisor.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 11 · Riesgo tecnológico y ciberseguridad](11-riesgo-tecnologico-y-ciberseguridad.md) | [Parte 11](../README.md) · [Programa](../../../SYLLABUS.md) | [13 · Pruebas de estrés →](13-pruebas-de-estres.md) |
<!-- gen:footer:end -->
