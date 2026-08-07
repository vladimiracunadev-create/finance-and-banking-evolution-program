---
part: 9
class: 10
title: "Scoring"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 10 · Scoring

> [← 09 · Flujo de caja del deudor empresarial](09-flujo-de-caja.md) · [Índice de la parte](../README.md) · [11 · Crédito de consumo →](11-credito-de-consumo.md)

**Parte 09 — Análisis y gestión de crédito** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Comprender cómo se construye, valida y usa un modelo de scoring, que es el instrumento que decide la
mayoría de las operaciones minoristas. Esta clase entrega el proceso completo, las métricas de
evaluación y —especialmente— los límites y riesgos que un modelo mal gobernado introduce.

## 📚 Objetivos

Al finalizar podrás:

1. **Explicar** el proceso de construcción de un modelo de scoring.
2. **Interpretar** las métricas de discriminación y calibración.
3. **Traducir** un puntaje en probabilidad y en decisión.
4. **Detectar** el deterioro de un modelo y sus causas.
5. **Identificar** los riesgos de sesgo y de uso indebido.

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
| `scoring` | Modelo estadístico que estima la probabilidad de incumplimiento de un solicitante. |
| `variable predictiva` | Característica con poder de discriminación entre buenos y malos pagadores. |
| `definición de malo` | Criterio que define el evento a predecir. Habitualmente mora ≥ 90 días en 12 meses. |
| `discriminación` | Capacidad del modelo de separar buenos de malos. Se mide con Gini o AUC. |
| `calibración` | Correspondencia entre la probabilidad estimada y la observada. |
| `punto de corte` | Puntaje bajo el cual se rechaza. Es una decisión de negocio, no del modelo. |
| `deriva del modelo` | Pérdida de poder predictivo por cambios en la población o en el entorno. |

## 🧠 Modelo mental

Un modelo de scoring hace **dos cosas distintas** que se evalúan por separado:

```text
DISCRIMINAR   ordenar correctamente de mejor a peor riesgo
              se mide con Gini / AUC

CALIBRAR      asignar la probabilidad correcta a cada nivel
              se mide comparando esperado contra observado
```

Un modelo puede discriminar bien y calibrar mal: ordena correctamente y **sobrestima o subestima el
nivel de riesgo de todos**. Eso produce precios equivocados aunque la selección sea correcta.

## 📖 Desarrollo

### 1. Proceso de construcción

```text
1. definir el evento ("malo"): mora ≥ 90 días en los 12 meses siguientes
2. definir la ventana: cosecha de originación y periodo de observación
3. construir la muestra: solicitudes con desenlace conocido
4. seleccionar variables candidatas
5. analizar el poder predictivo individual de cada variable
6. agrupar variables continuas en tramos con comportamiento monótono
7. estimar el modelo (regresión logística u otra técnica)
8. validar en muestra de prueba y fuera de tiempo
9. calibrar a la tasa de incumplimiento esperada
10. definir el punto de corte según la política de negocio
11. documentar y someter a validación independiente
```

**El paso 3 tiene un problema estructural conocido:** la muestra solo contiene solicitudes
**aprobadas**, porque de las rechazadas no se conoce el desenlace. Eso sesga el modelo hacia la
población que ya pasó el filtro anterior. Las técnicas de inferencia de rechazados intentan corregirlo
con supuestos que deben declararse.

### 2. Variables típicas y su poder predictivo

| Categoría | Variables | Poder predictivo relativo |
|---|---|---|
| Comportamiento | Moras históricas, utilización de cupos, antigüedad crediticia | **Muy alto** |
| Endeudamiento | Carga financiera, número de acreedores, deuda/renta | Alto |
| Estabilidad | Antigüedad laboral, continuidad de cotizaciones | Medio-alto |
| Demográficas | Edad, nivel educacional | Medio |
| Producto | Monto, plazo, destino, LTV | Medio |
| Relación | Antigüedad como cliente, productos contratados | Medio |

**Variables prohibidas o de uso restringido:**

```text
· características protegidas por la normativa de no discriminación
· variables que actúan como aproximación de esas características (proxy)
· información obtenida sin base legal
```

El segundo punto es el más sutil: una variable aparentemente neutra puede ser un proxy de una
característica protegida, y su uso produce discriminación indirecta aunque no haya intención.

### 3. Métricas de evaluación

**Discriminación:**

```text
Gini = 2 × AUC − 1

interpretación de referencia:
  Gini < 0,30      poder bajo
  0,30 – 0,45      aceptable
  0,45 – 0,60      bueno
  > 0,60           muy bueno (verificar que no haya fuga de información)
```

Un Gini muy alto merece sospecha: puede indicar que una variable contiene información del futuro
(fuga), lo que hace que el modelo funcione en el desarrollo y falle en producción.

**Calibración:**

```text
tramo de score   PD estimada   PD observada   desviación
 900–1000           0,4 %         0,5 %         +0,1 pp   ✓
 800–899            1,1 %         1,3 %         +0,2 pp   ✓
 700–799            2,4 %         2,9 %         +0,5 pp   ✓
 600–699            5,1 %         7,2 %         +2,1 pp   ⚠
 500–599           10,3 %        16,8 %         +6,5 pp   ✗
 < 500             21,7 %        34,2 %        +12,5 pp   ✗
```

**El modelo discrimina bien (el orden se mantiene) y calibra mal en los tramos bajos**: subestima
sistemáticamente el riesgo de los peores solicitantes. La consecuencia es que el precio de esos
créditos no cubre la pérdida real.

**Estabilidad de la población:**

```text
índice de estabilidad poblacional (PSI) = Σ (actual% − desarrollo%) × ln(actual%/desarrollo%)

PSI < 0,10   población estable
0,10 – 0,25  cambio moderado: monitorear
> 0,25       cambio significativo: revisar el modelo
```

### 4. Del puntaje a la decisión

```text
el modelo entrega una PROBABILIDAD
la decisión de aprobar o rechazar es de NEGOCIO, no del modelo
```

```text
punto de corte y su efecto:

corte    tasa de aprobación   PD promedio de aprobados   pérdida esperada
 450          82 %                   4,8 %                  2,88 %
 500          74 %                   3,9 %                  2,34 %
 550          66 %                   3,1 %                  1,86 %
 600          57 %                   2,4 %                  1,44 %
 650          47 %                   1,8 %                  1,08 %
```

**El punto de corte se elige maximizando el resultado, no minimizando la pérdida:**

```text
resultado = volumen × (margen − pérdida esperada − costo operativo)

corte 450:  82 % × (9,6 % − 2,88 % − 1,9 %) = 82 % × 4,82 % = 3,95 %
corte 500:  74 % × (9,6 % − 2,34 % − 1,9 %) = 74 % × 5,36 % = 3,97 %
corte 550:  66 % × (9,6 % − 1,86 % − 1,9 %) = 66 % × 5,84 % = 3,85 %
corte 600:  57 % × (9,6 % − 1,44 % − 1,9 %) = 57 % × 6,26 % = 3,57 %

ÓPTIMO: corte 500
```

Alternativamente, **el pricing basado en riesgo** permite aprobar tramos de mayor riesgo a mayor tasa,
en lugar de rechazarlos.

### 5. Deterioro, sesgo y gobierno

**Causas de deterioro:**

```text
· cambio en la población que solicita (nuevo canal, nueva campaña)
· cambio en el entorno económico
· cambio en la política de admisión (el modelo se entrenó con otra)
· cambio en el comportamiento por factores externos
· cambio en la disponibilidad o calidad de una variable
```

**Monitoreo obligatorio:**

```text
mensual      distribución de puntajes, tasa de aprobación, PSI
trimestral   discriminación (Gini) con cosechas maduras
semestral    calibración por tramo
anual        revisión completa y decisión de recalibrar o reconstruir
```

**Riesgos de sesgo:**

```text
· una variable proxy de una característica protegida produce discriminación indirecta
· datos históricos sesgados perpetúan decisiones sesgadas
· la ausencia de datos de rechazados sesga hacia la población previamente aprobada
· un modelo que discrimina bien puede ser injusto: precisión ≠ equidad
```

**Gobierno mínimo del modelo:**

```text
□ documentación completa: datos, variables, técnica, supuestos, limitaciones
□ validación independiente antes de producción
□ monitoreo con umbrales de alerta definidos
□ intervención humana disponible ante decisiones adversas
□ explicabilidad: capacidad de indicar los factores principales de una decisión
□ revisión periódica de sesgo por grupos
□ registro de todas las decisiones y de las excepciones
```

## 🧮 Ejemplo guiado

**Situación.** Un modelo de scoring de consumo muestra deterioro. Diagnostícalo.

```text
                        desarrollo   hace 12m   hace 6m   actual
Gini                        0,52       0,49      0,41      0,33
tasa de aprobación          68 %       71 %      78 %      81 %
PSI                          —         0,08      0,19      0,34
PD promedio estimada        2,8 %      2,7 %     2,6 %     2,5 %
PD observada (cosechas)     2,9 %      3,1 %     4,8 %     6,9 %
```

**Paso 1 — identifica el tipo de problema.**

```text
Gini cae de 0,52 a 0,33 → pérdida de DISCRIMINACIÓN
PD estimada baja mientras la observada sube → pérdida de CALIBRACIÓN
PSI de 0,34 → cambio SIGNIFICATIVO de población

los tres problemas simultáneamente
```

**Paso 2 — investiga el cambio de población.**

```text
distribución de solicitudes por canal:
                    desarrollo   actual
  sucursal             72 %       31 %
  digital propio       21 %       28 %
  alianza comercial     7 %       41 %  ← nuevo canal dominante
```

**El canal de alianza comercial pasó de 7 % a 41 % de las solicitudes.** El modelo se desarrolló con
una población en la que ese canal era marginal.

**Paso 3 — analiza el desempeño por canal.**

```text
canal                 Gini    PD observada   tasa de aprobación
sucursal              0,48        3,2 %           64 %
digital propio        0,44        4,1 %           72 %
alianza comercial     0,19       11,4 %           94 %
```

```text
en el canal de alianza:
  · el modelo casi no discrimina (Gini 0,19)
  · la PD observada es 3,5 veces la del canal sucursal
  · la tasa de aprobación es 94 %: el modelo casi no rechaza
```

**Paso 4 — busca la causa en las variables.**

```text
disponibilidad de variables por canal:
                              sucursal   alianza
  historial crediticio          98 %       41 %  ← muchos sin historial
  antigüedad laboral verificada 96 %       12 %  ← no se verifica
  renta acreditada              99 %       23 %  ← se declara, no se acredita
  antigüedad como cliente       74 %        3 %  ← clientes nuevos
```

**La causa raíz:** el canal de alianza no captura las variables de mayor poder predictivo. El modelo
las imputa con valores por defecto, y esa imputación asigna puntajes altos por ausencia de información
negativa.

**Paso 5 — cuantifica el impacto.**

```text
cartera originada por el canal de alianza en 12 meses: 184 000 millones
PD observada 11,4 % vs. 3,2 % esperada
exceso de pérdida esperada = 184 000 × (0,114 − 0,032) × 0,62 (LGD) = 9 353 millones
```

**Paso 6 — plan de acción.**

```text
INMEDIATO (esta semana)
  1. suspender la originación por el canal de alianza hasta implementar controles
  2. si no es viable comercialmente, elevar el punto de corte de ese canal
     de forma que la tasa de aprobación baje de 94 % a 55 %
  3. ajustar el precio del canal para reflejar una PD de 11,4 %

CORTO PLAZO (60 días)
  4. exigir acreditación de renta y verificación de antigüedad en el canal
  5. revisar la lógica de imputación: la ausencia de información NO debe
     asignar el valor más favorable
  6. recalibrar el modelo a la tasa de incumplimiento observada

MEDIANO PLAZO (6 meses)
  7. desarrollar un modelo específico para el canal de alianza, con las
     variables efectivamente disponibles
  8. establecer monitoreo por canal, no solo agregado

GOBIERNO
  9. el monitoreo agregado ocultó el problema durante 12 meses:
     incorporar segmentación por canal en el tablero mensual
 10. definir umbral de alerta: PSI > 0,15 por segmento exige revisión
```

**Interpreta:** el modelo no se deterioró: **la población cambió y el modelo se siguió usando sobre
una población para la que no fue construido**. El monitoreo agregado ocultó el problema porque el
canal sucursal, que seguía funcionando bien, compensaba en el promedio. El costo de esa demora fue de
9 353 millones.

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| "Me rechazaron sin explicación" | Derecho a conocer los factores principales | 12, clase 10 |
| Decisión automatizada | Debe existir intervención humana disponible | 14, clase 13 |
| Mismo perfil, distinta tasa | Pricing basado en riesgo | 15, clase 7 |
| Modelo que discrimina | Riesgo de sesgo y de sanción | 14, clase 13 |
| Sin historial, rechazo automático | Puede requerir modelo específico | 9, clase 7 |

## 🧪 Práctica

En `labs/lab-05.md`, sección de scoring:

1. Calcula Gini y la tabla de calibración de un modelo con datos sintéticos.
2. Determina el punto de corte óptimo maximizando el resultado, no minimizando la pérdida.
3. Calcula el PSI entre dos poblaciones y diagnostica el cambio.
4. Diseña el tablero de monitoreo con sus umbrales de alerta.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| El modelo funciona en desarrollo y falla en producción | Fuga de información o cambio de población | Valida fuera de tiempo y monitorea el PSI. |
| Se elige el corte minimizando la pérdida | Volumen ignorado | Maximiza el resultado, no minimices la pérdida. |
| Se monitorea solo el agregado | Problemas por segmento ocultos | Monitorea por canal y segmento. |
| La ausencia de datos asigna puntaje favorable | Lógica de imputación incorrecta | La ausencia no debe ser una ventaja. |
| Se usa una variable proxy de característica protegida | Discriminación indirecta | Revisa sesgo por grupos. |
| El modelo no se puede explicar | Sin explicabilidad | Debe poder indicar los factores principales. |

## ❓ Preguntas de comprobación

1. ¿Qué diferencia hay entre discriminación y calibración, y cómo se mide cada una?
2. ¿Por qué un Gini muy alto merece sospecha?
3. ¿Cómo se elige el punto de corte y por qué no se minimiza la pérdida?
4. ¿Qué indica un PSI de 0,34 y qué se hace?
5. Nombra cuatro elementos del gobierno mínimo de un modelo de scoring.

## 📥 Entregable

Guarda en `portfolio/parte-09/clase-10/`:

- el Gini y la tabla de calibración calculados con datos sintéticos;
- el punto de corte óptimo con su cálculo de resultado por nivel;
- el PSI calculado entre dos poblaciones con su diagnóstico;
- el tablero de monitoreo diseñado con umbrales y frecuencias.

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

- Anderson, R. (2007). *The Credit Scoring Toolkit*. Oxford University Press. Proceso completo de construcción y validación.
- Siddiqi, N. (2017). *Intelligent Credit Scoring* (2.ª ed.). Wiley. Desarrollo, monitoreo e inferencia de rechazados.
- Thomas, L., Edelman, D. y Crook, J. (2017). *Credit Scoring and Its Applications* (2.ª ed.). SIAM. Métricas de evaluación.
- Federal Reserve / OCC (2011). *Supervisory Guidance on Model Risk Management* (SR 11-7). Gobierno, validación y documentación de modelos.
- European Banking Authority (2023). *Machine Learning for IRB models*. EBA. Explicabilidad y sesgo en modelos de crédito. <https://www.eba.europa.eu/>
- Verificación local: revisa la normativa de tu país sobre decisiones automatizadas, derecho a explicación y no discriminación en el acceso al crédito.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 09 · Flujo de caja del deudor empresarial](09-flujo-de-caja.md) | [Parte 09](../README.md) · [Programa](../../../SYLLABUS.md) | [11 · Crédito de consumo →](11-credito-de-consumo.md) |
<!-- gen:footer:end -->
