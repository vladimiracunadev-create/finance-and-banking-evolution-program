---
part: 12
class: 3
title: "Prevención de lavado de activos"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 03 · Prevención de lavado de activos

> [← 02 · Arquitectura regulatoria internacional](02-arquitectura-regulatoria-internacional.md) · [Índice de la parte](../README.md) · [04 · Conozca a su cliente y debida diligencia →](04-conozca-a-su-cliente.md)

**Parte 12 — Regulación, cumplimiento y auditoría** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Construir y operar el sistema que impide que el banco sea usado como infraestructura del delito. Es la
obligación de cumplimiento con mayor exposición sancionatoria del sector y, al mismo tiempo, la que
produce más exclusión financiera cuando se aplica sin criterio.

Esta clase trata la obligación cuyo incumplimiento produce las sanciones mayores y las consecuencias más difíciles de revertir. Y la plantea con su tensión propia: un programa demasiado laxo expone a la entidad, y uno demasiado estricto excluye del sistema financiero a poblaciones enteras sin reducir el delito.

## 📚 Objetivos

Al finalizar podrás:

1. **Describir** las etapas del lavado y los métodos asociados a cada una.
2. **Aplicar** el enfoque basado en riesgo a la asignación de recursos de control.
3. **Diseñar** reglas de monitoreo y evaluar su calidad por sus falsos positivos.
4. **Conducir** el proceso desde la alerta hasta el reporte de operación sospechosa.
5. **Evaluar** el conflicto entre integridad e inclusión financiera.

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

Los tres primeros términos son las etapas del lavado; los cinco siguientes, el enfoque de la respuesta y sus figuras. El **soplo** es la prohibición que más sorprende: avisar al cliente de que se le ha reportado es delito en casi cualquier jurisdicción.

| Concepto | Comprensión verificable |
|---|---|
| `colocación` | Introducción del dinero de origen ilícito en el sistema financiero. |
| `estratificación` | Movimientos sucesivos que rompen el rastro del origen. |
| `integración` | Reingreso del dinero a la economía con apariencia legítima. |
| `enfoque basado en riesgo` | Intensidad del control proporcional al riesgo evaluado. |
| `beneficiario final` | Persona natural que en última instancia controla o se beneficia. |
| `persona expuesta políticamente` | Quien ejerce o ejerció función pública relevante. |
| `operación sospechosa` | Aquella sin justificación económica o legal aparente. |
| `soplo` | Advertir al cliente que se le está investigando. Está prohibido. |

## 🧠 Modelo mental

El modelo mental son tres etapas con propósitos distintos: meter el dinero en el sistema, moverlo hasta que su origen se pierda y sacarlo con apariencia lícita. Cada etapa deja huellas distintas, y por eso el monitoreo busca cosas distintas en cada una.

```text
EL BANCO NO INVESTIGA DELITOS. DETECTA INCOHERENCIAS.

  no se determina si el dinero es ilícito
  se determina si la operación es COHERENTE
  con lo que se conoce del cliente

  incoherencia + sin explicación razonable = REPORTE

  el reporte no es una acusación:
  es información para quien sí investiga
```

**Esta distinción libera y obliga a la vez.** Libera de una tarea imposible —probar el origen ilícito— y
obliga a otra exigente: conocer al cliente lo suficiente como para saber qué es coherente en su caso.

## 📖 Desarrollo

### 1. Las tres etapas y sus métodos

Cada etapa usa métodos característicos y deja rastros distintos. La tabla los recoge.

```text
COLOCACIÓN — la etapa más vulnerable para el delincuente
  · depósitos fraccionados bajo el umbral de reporte (estructuración)
  · uso de negocios intensivos en efectivo
  · uso de terceros (personas interpuestas)
  · compra de instrumentos monetarios

ESTRATIFICACIÓN — la más difícil de detectar
  · transferencias sucesivas entre cuentas y jurisdicciones
  · sociedades pantalla y estructuras opacas
  · facturación falsa en comercio exterior
  · compra y venta de activos entre partes vinculadas

INTEGRACIÓN — la que da apariencia definitiva
  · inversión inmobiliaria
  · préstamos a sí mismo desde estructuras propias
  · negocios legítimos financiados con fondos previamente estratificados
```

| Señal por etapa | Dónde se detecta |
|---|---|
| Depósitos justo bajo el umbral | Monitoreo transaccional |
| Actividad incoherente con el perfil | Perfil vs. transaccionalidad |
| Estructura societaria sin propósito económico | Debida diligencia |
| Comercio exterior con precios atípicos | Análisis documental |
| Vinculación con jurisdicción de alto riesgo | Segmentación por riesgo |

### 2. Enfoque basado en riesgo

El enfoque basado en riesgo concentra los recursos donde el riesgo está, y es lo que la norma exige. La tabla lo desarrolla.

```text
EL PRINCIPIO
  no todos los clientes ni todas las operaciones
  presentan el mismo riesgo
  → los recursos se asignan según el riesgo evaluado

  aplicar el mismo control a todos
  es a la vez ineficaz e ineficiente:
  gasta donde no hay riesgo y no alcanza donde sí lo hay
```

```text
FACTORES DE RIESGO
  CLIENTE     tipo, actividad, estructura, condición de persona expuesta,
              antecedentes, transparencia del beneficiario final
  PRODUCTO    efectivo, transferencias internacionales, banca privada,
              productos con anonimato relativo
  CANAL       presencial, no presencial, a través de terceros
  GEOGRAFÍA   jurisdicción de residencia, de operación, de contraparte
```

| Nivel de riesgo | Debida diligencia | Frecuencia de revisión |
|---|---|---|
| Bajo | Simplificada | Cada 3–5 años |
| Medio | Estándar | Cada 2–3 años |
| Alto | Reforzada, con aprobación de alta gerencia | Anual o menor |

**La debida diligencia simplificada no es ausencia de diligencia.** Es un conjunto reducido de
verificaciones para casos de riesgo demostrablemente bajo, y su aplicación debe estar fundada en una
evaluación de riesgo documentada, no en la conveniencia comercial.

### 3. Monitoreo transaccional

El monitoreo genera alertas con reglas y con modelos, y su calibración decide si sirve. La tabla recoge los criterios.

```text
CÓMO FUNCIONA
  1. se construye el PERFIL esperado del cliente
     (actividad, montos, frecuencia, contrapartes, geografía)
  2. las transacciones se comparan con ese perfil
  3. las desviaciones generan ALERTAS
  4. las alertas se analizan
  5. las que no tienen explicación razonable se reportan
```

| Tipo de regla | Ejemplo | Debilidad |
|---|---|---|
| Umbral simple | Operación sobre un monto | Fácil de eludir |
| Umbral acumulado | Suma en un período | Mejor, aún eludible |
| Desviación del perfil | 5 veces el promedio propio | Requiere buen perfil |
| Patrón | Depósitos seguidos de retiro inmediato | Más selectiva |
| Red | Conexiones entre cuentas aparentemente no relacionadas | La más potente y costosa |

```text
EL PROBLEMA DE LOS FALSOS POSITIVOS
  una regla mal calibrada genera miles de alertas
  el analista revisa superficialmente por volumen
  y la alerta verdadera se pierde entre las falsas

  MÉTRICA CLAVE: tasa de conversión de alerta a reporte
    < 1 %   reglas mal calibradas: se revisa ruido
    2–8 %   rango de operación razonable
    > 20 %  posible sub-detección: las reglas solo ven lo evidente
```

### 4. Del alerta al reporte

Una alerta recorre un proceso con plazos hasta convertirse o no en reporte. El esquema lo recorre.

```text
1. ALERTA          generada por regla o por reporte interno de personal
2. ANÁLISIS        revisión del perfil, historial y documentación
3. SOLICITUD       si procede, se pide información al cliente
                   SIN revelar que existe una alerta
4. DECISIÓN        se descarta con fundamento, o se escala
5. COMITÉ          casos complejos se resuelven en comité
6. REPORTE         a la unidad de inteligencia financiera, en plazo
7. CONTINUIDAD     decisión sobre mantener o terminar la relación
8. CONSERVACIÓN    documentación por el plazo legal
```

```text
PROHIBICIÓN DE SOPLO
  advertir al cliente que se le investiga o se le reportó
  constituye infracción en prácticamente toda jurisdicción

  consecuencia práctica: la solicitud de información al cliente
  debe formularse como parte de la actualización ordinaria,
  nunca como consecuencia visible de un análisis
```

**Reportar no obliga a terminar la relación, y terminarla no sustituye al reporte.** Son dos decisiones
independientes: una es una obligación legal de información, la otra es una decisión de riesgo del banco.

### 5. Integridad frente a inclusión

Un programa demasiado estricto excluye sin reducir el delito. La tabla recoge esa tensión con evidencia.

```text
EL CONFLICTO REAL
  aplicar controles con máxima severidad
  → excluye clientes legítimos de difícil documentación:
    trabajadores informales, migrantes, personas sin domicilio estable,
    organizaciones sin fines de lucro, remesadores pequeños

  el propio GAFI ha advertido que la exclusión masiva
  es una respuesta INCORRECTA al enfoque basado en riesgo:
  empuja la actividad al circuito informal,
  donde no hay ninguna trazabilidad
```

| Práctica incorrecta | Alternativa proporcionada |
|---|---|
| Rechazar categorías completas de clientes | Evaluar caso a caso con diligencia reforzada |
| Exigir documentación imposible | Aceptar medios alternativos de verificación |
| Cerrar cuentas ante la primera alerta | Analizar antes de decidir |
| Tratar toda organización sin fines de lucro como alto riesgo | Segmentar por actividad real |

## 🧮 Ejemplo guiado

El ejemplo sigue una alerta desde su generación hasta la decisión de reportar. Conviene fijarse en el análisis: la mayoría de las alertas se cierran, y documentar por qué es tan importante como reportar.

**Situación.** El oficial de cumplimiento revisa el desempeño del sistema de monitoreo.

```text
DATOS DEL AÑO
  clientes                                 640 000
  transacciones monitoreadas            94 000 000
  alertas generadas                         48 200
  alertas analizadas                        48 200
  reportes de operación sospechosa             186
  analistas dedicados                           14

DISTRIBUCIÓN DE ALERTAS POR REGLA
  regla                          alertas   reportes   conversión
  R1 umbral efectivo             18 400        22       0,12 %
  R2 acumulado mensual           12 600        18       0,14 %
  R3 desviación del perfil        9 800        61       0,62 %
  R4 transferencias exterior      4 900        34       0,69 %
  R5 patrón depósito-retiro       1 900        38       2,00 %
  R6 análisis de red                600        13       2,17 %
```

**Paso 1 — evalúa la eficiencia global.**

```text
tasa de conversión global: 186 / 48 200 = 0,39 %
→ muy por debajo del rango razonable de 2–8 %

carga por analista: 48 200 / 14 = 3 443 alertas al año
                    ≈ 14 alertas por día hábil por analista
                    ≈ 34 minutos por alerta en jornada de 8 horas

el tiempo disponible por alerta es insuficiente
para un análisis con profundidad
```

**Paso 2 — identifica dónde está el ruido.**

```text
R1 y R2 generan 31 000 alertas (64 % del total)
y producen 40 reportes (21,5 % del total)

R5 y R6 generan 2 500 alertas (5,2 % del total)
y producen 51 reportes (27,4 % del total)

razón de productividad:
  R5+R6: 51 / 2 500 = 2,04 %
  R1+R2: 40 / 31 000 = 0,13 %
  R5+R6 es 16 veces más productiva
```

**Paso 3 — analiza por qué R1 y R2 rinden tan poco.**

```text
R1: umbral fijo de efectivo
  · alcanza a todos los comercios intensivos en efectivo
    con actividad normal: farmacias, restaurantes, ferias
  · el 91 % de sus alertas corresponde a 2 400 clientes
    que la generan todos los meses, siempre con explicación

R2: acumulado mensual con umbral fijo
  · mismo problema: no considera el perfil del cliente
```

**Paso 4 — recalibra.**

```text
PROPUESTA
  R1 y R2 se combinan con el perfil del cliente:
  la alerta se genera si el efectivo supera el umbral
  Y se desvía del comportamiento histórico del propio cliente

  simulación sobre el año:
    alertas de R1: 18 400 → 3 200
    alertas de R2: 12 600 → 2 400
    reportes conservados: 38 de 40 (se pierden 2)

  alertas totales: 48 200 → 21 800  (−54,8 %)
  reportes: 186 → 184  (−1,1 %)
  conversión global: 0,84 %
```

**Paso 5 — reinvierte la capacidad liberada.**

```text
capacidad liberada: 26 400 alertas ≈ 7,7 analistas equivalentes

DESTINO
  · ampliar R6 (análisis de red), la regla más productiva:
    su cobertura actual alcanza al 12 % de la base
    ampliarla al 60 % generaría ~3 000 alertas
    con conversión estimada de 2,17 % → ~65 reportes adicionales
  · profundizar el análisis de las alertas conservadas:
    de 34 minutos a ~75 minutos por alerta

RESULTADO ESPERADO
  alertas: 24 800
  reportes: ~249  (+34 % sobre los 186 actuales)
  tiempo por alerta: más del doble
  mismos 14 analistas
```

**Paso 6 — verifica el riesgo de la recalibración.**

```text
¿la recalibración crea un punto ciego?

  los 2 400 clientes que ya no generarán alerta de R1
  siguen cubiertos por:
    · R3 (desviación del perfil), que es precisamente
      lo que se incorporó a R1
    · R5 (patrón), R6 (red)
    · revisión periódica según su nivel de riesgo
    · reporte interno del personal de sucursal

CONTROL COMPENSATORIO
  muestreo aleatorio mensual de 30 clientes
  del grupo que dejó de alertar, con análisis completo
  → verifica que la regla no esté ocultando actividad
```

**Paso 7 — documenta la decisión.**

```text
LA RECALIBRACIÓN DEBE DOCUMENTARSE porque:
  · reduce alertas: un supervisor preguntará por qué
  · la justificación no puede ser "reducir carga de trabajo"
  · la justificación válida es "mejorar la detección efectiva",
    y debe estar respaldada por la simulación y el seguimiento

EXPEDIENTE
  · análisis previo con datos
  · simulación sobre el período histórico
  · reportes que se habrían perdido y por qué es aceptable
  · controles compensatorios
  · aprobación del comité de cumplimiento
  · plan de seguimiento a 6 y 12 meses
```

**Interpreta:** el sistema revisaba 48 200 alertas y **detectaba menos que si revisara la mitad**. El
problema no era la falta de recursos: era una calibración que consumía el 64 % de la capacidad en
generar ruido. La métrica que lo reveló —la tasa de conversión por regla— es barata de calcular y rara
vez se mira. Un sistema de prevención se juzga por **lo que detecta**, no por lo que alerta.

## 🏦 Del cliente al banco

El cliente responde preguntas y el banco cumple una obligación con responsabilidad personal asociada. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Me piden explicar cada depósito» | Monitoreo transaccional mal calibrado | 12, clase 3 |
| «Me cerraron la cuenta sin explicación» | Decisión de riesgo; el reporte no se revela | 12, clase 3 |
| «No puedo abrir cuenta sin documentos formales» | Exclusión por diligencia rígida | 12, clase 4 |
| «Mi organización es tratada como sospechosa» | Segmentación por categoría, no por riesgo | 12, clase 3 |
| «El banco no me dice por qué» | Prohibición de soplo | 12, clase 3 |

## 🧪 Práctica

El laboratorio pide analizar alertas sintéticas y decidir cuáles se reportan. Dos son falsos positivos con explicación documentable y una no lo es.

En `labs/lab-02.md`:

1. Clasifica veinte señales de alerta por etapa del lavado.
2. Construye una matriz de riesgo de clientes con los cuatro factores.
3. Calcula la tasa de conversión por regla y propone una recalibración.
4. Documenta un caso completo desde la alerta hasta la decisión de reporte.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen programas que fallan por exceso o por defecto. Las causas son umbrales sin calibrar y enfoque de riesgo no aplicado.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Miles de alertas y pocos reportes | Reglas sin perfil del cliente | Recalibra con desviación propia. |
| Se rechazan categorías completas | Riesgo por categoría, no evaluado | Evalúa caso a caso. |
| Se cierra la cuenta y no se reporta | Confusión de decisiones | Son independientes; haz ambas. |
| Se explica al cliente el motivo | Soplo | Formula como actualización ordinaria. |
| Se recalibra para reducir carga | Justificación inválida | Documenta la mejora de detección. |
| El beneficiario final no se identifica | Estructura opaca aceptada | Sin beneficiario final, no hay relación. |

## ❓ Preguntas de comprobación

1. ¿Por qué el banco detecta incoherencias y no investiga delitos?
2. ¿Qué indica una tasa de conversión de alerta a reporte inferior al 1 %?
3. ¿Por qué reportar y terminar la relación son decisiones independientes?
4. ¿Por qué la exclusión masiva es una respuesta incorrecta al enfoque basado en riesgo?
5. ¿Qué debe documentarse al recalibrar una regla de monitoreo y por qué?

## 📥 Entregable

Guarda en `portfolio/parte-12/clase-03/`:

- las señales clasificadas por etapa del lavado;
- la matriz de riesgo de clientes con sus cuatro factores;
- el análisis de conversión por regla con la recalibración propuesta y sus controles compensatorios;
- el expediente completo de un caso desde la alerta hasta la decisión.

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

- Financial Action Task Force (2012-2025). *International Standards on Combating Money Laundering and the Financing of Terrorism & Proliferation — The FATF Recommendations*. FATF. <https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html>
- Financial Action Task Force (2021). *Guidance on Risk-Based Supervision*. FATF.
- Financial Action Task Force (2021). *Stocktake on Data Pooling, Collaborative Analytics and Data Protection*. FATF.
- Basel Committee on Banking Supervision (2020). *Sound management of risks related to money laundering and financing of terrorism*. BIS. <https://www.bis.org/bcbs/publ/d505.htm>
- World Bank (2018). *De-risking in the Financial Sector*. World Bank Group.
- Verificación local: revisa la ley de prevención de lavado de tu país, los umbrales de reporte, los plazos, la autoridad receptora y las obligaciones de conservación.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 02 · Arquitectura regulatoria internacional](02-arquitectura-regulatoria-internacional.md) | [Parte 12](../README.md) · [Programa](../../../SYLLABUS.md) | [04 · Conozca a su cliente y debida diligencia →](04-conozca-a-su-cliente.md) |
<!-- gen:footer:end -->
