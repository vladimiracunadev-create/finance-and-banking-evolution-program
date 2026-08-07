---
part: 11
class: 10
title: "Riesgo operacional"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 10 · Riesgo operacional

> [← 09 · Derivados y coberturas](09-derivados-y-coberturas.md) · [Índice de la parte](../README.md) · [11 · Riesgo tecnológico y ciberseguridad →](11-riesgo-tecnologico-y-ciberseguridad.md)

**Parte 11 — Gestión integral de riesgos** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Gestionar el riesgo de que fallen los procesos, las personas o los sistemas. Es el único riesgo que
existe en todas las áreas del banco, el que produce las pérdidas individuales más grandes registradas
y el más difícil de medir, porque sus eventos graves son raros y cada uno es distinto del anterior.

## 📚 Objetivos

Al finalizar podrás:

1. **Clasificar** eventos según las categorías supervisoras de riesgo operacional.
2. **Construir** una base de eventos de pérdida y usarla para gestionar.
3. **Calcular** el requerimiento de capital por el enfoque estandarizado.
4. **Aplicar** autoevaluaciones de riesgo e indicadores clave.
5. **Diseñar** controles proporcionales al riesgo y verificar su efectividad.

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
| `riesgo operacional` | Pérdida por fallas de procesos, personas, sistemas o eventos externos. |
| `evento de pérdida` | Suceso con efecto económico registrable, ocurrido o evitado. |
| `casi-pérdida` | Evento que no produjo pérdida por azar o por un control tardío. |
| `indicador de negocio` | Base de cálculo del capital en el enfoque estandarizado. |
| `multiplicador de pérdidas internas` | Ajuste del capital por el historial de pérdidas del banco. |
| `autoevaluación de riesgos y controles` | Ejercicio estructurado de identificación por proceso. |
| `indicador clave de riesgo` | Métrica que anticipa el deterioro de un control. |
| `distribución de severidad` | Cómo se reparten las pérdidas por tamaño. Cola muy pesada. |

## 🧠 Modelo mental

```text
LA DISTRIBUCIÓN DEL RIESGO OPERACIONAL TIENE DOS MUNDOS

ALTA FRECUENCIA, BAJA SEVERIDAD      errores de digitación, fraudes menores
  · predecibles, se presupuestan
  · se gestionan con procesos y automatización
  · son COSTO, no riesgo

BAJA FRECUENCIA, ALTA SEVERIDAD      fraude interno mayor, falla sistémica,
                                      sanción regulatoria, ciberincidente
  · impredecibles, no se presupuestan
  · se gestionan con controles y con capital
  · son el RIESGO de verdad

el 80 % de los EVENTOS está en el primer mundo
el 80 % de la PÉRDIDA está en el segundo
```

**Un sistema de gestión que solo mira frecuencia gestiona el mundo equivocado.**

## 📖 Desarrollo

### 1. Las siete categorías supervisoras

| Categoría | Ejemplos |
|---|---|
| Fraude interno | Apropiación, operaciones no autorizadas, ocultamiento de pérdidas |
| Fraude externo | Clonación, suplantación, robo, intrusión informática |
| Prácticas laborales | Discriminación, seguridad en el trabajo, conflictos laborales |
| Clientes, productos y prácticas | Venta indebida, abuso de información, incumplimiento de deber fiduciario |
| Daños a activos físicos | Desastres naturales, vandalismo, terrorismo |
| Interrupción del negocio | Fallas de sistemas, de suministro, de proveedores |
| Ejecución y gestión de procesos | Errores de registro, de liquidación, de documentación, de datos |

```text
DISTRIBUCIÓN TÍPICA (bases sectoriales públicas)
  por FRECUENCIA: ejecución de procesos y fraude externo dominan
  por SEVERIDAD:  clientes/productos/prácticas y fraude interno dominan

  la categoría "clientes, productos y prácticas de negocio"
  concentra las mayores pérdidas del sector:
  son las sanciones y compensaciones por conducta
```

### 2. Base de eventos de pérdida

```text
QUÉ REGISTRAR
  · fecha de ocurrencia, de descubrimiento y de contabilización
  · categoría, línea de negocio, proceso
  · pérdida bruta, recuperaciones, pérdida neta
  · causa raíz
  · controles que fallaron
  · acción correctiva y su verificación

UMBRAL DE REGISTRO
  típicamente bajo (equivalente a unos pocos miles)
  demasiado alto → se pierde la señal temprana
  demasiado bajo → se satura el proceso
```

```text
LAS CASI-PÉRDIDAS SON LA INFORMACIÓN MÁS VALIOSA
  ocurrieron todos los pasos del evento
  y la pérdida no se materializó por azar

  un banco con muchas casi-pérdidas registradas
  tiene un sistema de gestión SANO,
  no un sistema con problemas
```

**Sesgo a evitar:** las bases de pérdidas registran lo que se descubrió. El fraude interno bien hecho
no aparece hasta que se descubre, y el tiempo medio entre ocurrencia y descubrimiento es de meses o
años. Por eso la base histórica se complementa con **escenarios**.

### 3. Capital por el enfoque estandarizado

El marco vigente reemplazó los enfoques anteriores por uno único:

```text
CAPITAL = COMPONENTE DE INDICADOR DE NEGOCIO × MULTIPLICADOR DE PÉRDIDAS

COMPONENTE DE INDICADOR DE NEGOCIO (BIC)
  se calcula sobre el indicador de negocio (BI), que suma:
    componente de intereses, arriendos y dividendos
    componente de servicios (comisiones)
    componente financiero (resultados de negociación y de banca)

  se aplican coeficientes marginales por tramo:
    tramo 1 (hasta 1 000 M€)      12 %
    tramo 2 (1 000 a 30 000 M€)   15 %
    tramo 3 (más de 30 000 M€)    18 %

MULTIPLICADOR DE PÉRDIDAS INTERNAS (ILM)
  ILM = Ln( e − 1 + (LC / BIC)^0,8 )
  LC = 15 × pérdida operacional media anual de los últimos 10 años

  si LC = BIC → ILM = 1
  si el historial de pérdidas es peor que el promedio → ILM > 1
```

**El diseño premia el buen historial y castiga el malo**, con una función cóncava que evita que un solo
evento extremo domine el resultado. Las jurisdicciones pueden fijar el ILM en 1 para bancos pequeños.

### 4. Autoevaluación e indicadores

```text
AUTOEVALUACIÓN DE RIESGOS Y CONTROLES — proceso
  1. mapear el proceso paso a paso
  2. identificar qué puede fallar en cada paso
  3. estimar probabilidad e impacto (riesgo inherente)
  4. identificar los controles existentes
  5. evaluar su efectividad PROBADA
  6. determinar el riesgo residual
  7. comparar con el apetito y decidir
```

| Indicador clave de riesgo | Qué anticipa |
|---|---|
| Partidas de conciliación pendientes > N días | Falla de registro o de proceso |
| Rotación de personal en áreas críticas | Pérdida de control y de conocimiento |
| Días de vacaciones no tomados | Ocultamiento de irregularidades |
| Accesos privilegiados sin revisar | Fraude interno |
| Incidencias por cambio en producción | Riesgo tecnológico |
| Excepciones a políticas aprobadas | Erosión del marco de control |
| Antigüedad de hallazgos de auditoría sin cerrar | Cultura de control |

**El indicador de vacaciones no tomadas** parece menor y es históricamente uno de los más predictivos:
casi todos los fraudes internos prolongados requieren la presencia continua de quien los comete.

### 5. Controles proporcionales

```text
JERARQUÍA DE CONTROLES (de más a menos efectivo)
  1. ELIMINAR      quitar el paso que puede fallar
  2. AUTOMATIZAR   remover el juicio humano donde no aporta
  3. PREVENIR      impedir que ocurra (validación, autorización dual)
  4. DETECTAR      encontrarlo pronto (conciliación, alerta)
  5. CORREGIR      remediar el efecto
  6. TRANSFERIR    seguro, tercerización (no elimina la responsabilidad)
  7. ACEPTAR       decisión documentada, dentro del apetito
```

```text
PRINCIPIO DE PROPORCIONALIDAD
  el costo del control no debe superar la pérdida esperada que evita

  control que cuesta 400 al año
  y evita una pérdida esperada de 120 al año
  → destruye 280 de valor, salvo que exista una razón
    normativa o reputacional que lo justifique explícitamente
```

## 🧮 Ejemplo guiado

**Situación.** Un banco analiza su base de pérdidas y decide sobre un control.

```text
BASE DE PÉRDIDAS — últimos 5 años (millones)
  categoría                      eventos   pérdida total   máximo
  ejecución de procesos            1 840        842          38
  fraude externo                     620      1 106         184
  clientes y prácticas                42      2 940       1 620
  fraude interno                       7        980         910
  interrupción del negocio            31        412         206
  daños a activos                     12         64          22
  prácticas laborales                 18         58          14
  TOTAL                            2 570      6 402       1 620
```

**Paso 1 — analiza la distribución.**

```text
por FRECUENCIA
  ejecución de procesos: 1 840 / 2 570 = 71,6 % de los eventos
  clientes y prácticas:     42 / 2 570 =  1,6 %

por SEVERIDAD
  ejecución de procesos:   842 / 6 402 = 13,2 % de la pérdida
  clientes y prácticas:  2 940 / 6 402 = 45,9 %

pérdida media por evento:
  ejecución de procesos:   842 / 1 840 =   0,46
  clientes y prácticas:  2 940 /    42 =  70,0
  fraude interno:          980 /     7 = 140,0

razón entre la media de fraude interno y la de procesos: 304 veces
```

**Paso 2 — calcula el indicador de negocio.**

```text
componente de intereses, arriendos y dividendos      1 840
componente de servicios (comisiones)                   920
componente financiero                                  240
INDICADOR DE NEGOCIO (BI)                            3 000  (millones)
```

**Paso 3 — calcula el componente de indicador de negocio.**

```text
tramo 1: 1 000 × 12 % = 120
tramo 2: (3 000 − 1 000) × 15 % = 2 000 × 15 % = 300
BIC = 420
```

**Paso 4 — calcula el componente de pérdidas.**

```text
pérdida media anual (usando los 5 años disponibles):
  6 402 / 5 = 1 280,4

LC = 15 × 1 280,4 = 19 206

ADVERTENCIA: el marco exige 10 años de historial.
Con 5 años y un evento de 1 620 en la muestra,
la media está dominada por un solo suceso.
```

**Paso 5 — calcula el multiplicador y el capital.**

```text
LC / BIC = 19 206 / 420 = 45,73

ILM = Ln( e − 1 + 45,73^0,8 )
    = Ln( 1,71828 + 21,52 )
    = Ln( 23,24 ) = 3,146

CAPITAL = 420 × 3,146 = 1 321 millones
```

**Paso 6 — evalúa el peso del evento único.**

```text
sin el evento de 1 620 (clientes y prácticas):
  pérdida total: 6 402 − 1 620 = 4 782
  media anual: 956,4
  LC = 14 346
  LC / BIC = 34,16
  ILM = Ln(1,71828 + 16,91) = Ln(18,63) = 2,925
  capital = 420 × 2,925 = 1 229

UN SOLO EVENTO explica 92 millones de capital: el 7 %
la función cóncava del ILM cumple su función:
un evento de 1 620 sobre una pérdida total de 6 402 (25 %)
mueve el capital solo un 7 %
```

**Paso 7 — decide sobre un control concreto.**

```text
PROPUESTA: autorización dual obligatoria para transferencias
           internas superiores a un umbral

  eventos de fraude interno en 5 años: 7
  de ellos, ejecutados por esta vía: 4
  pérdida asociada: 780 → 156 anuales de pérdida esperada evitada

  costo del control:
    2 personas adicionales en control de operaciones      84 anuales
    demora media de 40 minutos en 12 000 operaciones/año
    costo de oportunidad estimado                          31 anuales
    desarrollo inicial (una vez)                          120
  COSTO ANUALIZADO (7 años, 9 %): 115 + 24 = 139

  beneficio anual: 156
  costo anual: 139
  BENEFICIO NETO: 17 anuales → marginalmente positivo
```

**Paso 8 — mejora la propuesta antes de decidir.**

```text
el control propuesto es marginal porque aplica a TODAS
las operaciones sobre el umbral

ALTERNATIVA: control basado en riesgo
  autorización dual solo si se cumple alguna condición:
    · destinatario nuevo (< 30 días)
    · monto atípico para el operador
    · fuera del horario habitual del operador
    · operador con accesos privilegiados

  cobertura de los 4 eventos históricos: 4 de 4
  operaciones afectadas: 12 000 → 900 al año
  costo anualizado: 0,5 persona (21) + demora (2) + desarrollo (28) = 51

  beneficio anual: 156
  costo anual: 51
  BENEFICIO NETO: 105 anuales  → 6 veces mejor
```

**Interpreta:** el análisis produjo dos conclusiones de distinto orden. La primera, de medición: el
capital operacional está dominado por la categoría de **conducta con el cliente**, no por los errores de
proceso que consumen la atención diaria. La segunda, de gestión: **un control bien focalizado cuesta un
tercio y cubre lo mismo**. La proporcionalidad no consiste en controlar menos, sino en controlar donde
el riesgo está.

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Me cobraron dos veces» | Evento de ejecución de procesos | 10, clase 8 |
| «Me vendieron un producto que no necesitaba» | Categoría de mayor severidad del sector | 12, clase 8 |
| «El sistema estuvo caído» | Interrupción del negocio | 10, clase 16 |
| «Alguien usó mi tarjeta» | Fraude externo | 4, clase 4 |
| «El banco tardó en detectarlo» | Tiempo entre ocurrencia y descubrimiento | 11, clase 10 |

## 🧪 Práctica

En `labs/lab-05.md`, sección de operacional:

1. Clasifica 30 eventos en las siete categorías supervisoras y analiza su distribución.
2. Calcula el capital por el enfoque estandarizado con y sin un evento extremo.
3. Construye una autoevaluación de riesgos y controles de un proceso completo.
4. Evalúa dos diseños de control por su relación entre costo y pérdida esperada evitada.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se gestiona lo frecuente y no lo severo | Foco en el número de eventos | Ordena también por pérdida. |
| Las casi-pérdidas no se registran | Se ven como no-eventos | Son la mejor señal temprana. |
| Umbral de registro muy alto | Se pierde la señal | Baja el umbral y prioriza el análisis. |
| Controles uniformes para todo | Sin proporcionalidad | Focaliza por condición de riesgo. |
| Se terceriza y se da por resuelto | Responsabilidad no transferible | Gestiona al proveedor como riesgo propio. |
| Efectividad de control no probada | Evaluación de diseño | Prueba y documenta. |

## ❓ Preguntas de comprobación

1. ¿Por qué el 80 % de los eventos y el 80 % de la pérdida están en mundos distintos?
2. ¿Por qué las casi-pérdidas son la información más valiosa de la base?
3. ¿Qué logra la forma cóncava del multiplicador de pérdidas internas?
4. ¿Por qué el indicador de vacaciones no tomadas es predictivo del fraude interno?
5. ¿Qué significa que un control sea proporcional al riesgo?

## 📥 Entregable

Guarda en `portfolio/parte-11/clase-10/`:

- la clasificación de eventos con el análisis de frecuencia y severidad;
- el cálculo de capital por el enfoque estandarizado, con su sensibilidad;
- la autoevaluación de riesgos y controles del proceso elegido;
- la comparación de dos diseños de control con su beneficio neto.

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

- Basel Committee on Banking Supervision (2017). *Basel III: Finalising post-crisis reforms*, sección de riesgo operacional. BIS. <https://www.bis.org/bcbs/publ/d424.htm>
- Basel Committee on Banking Supervision (2021). *Revisions to the Principles for the Sound Management of Operational Risk*. BIS. <https://www.bis.org/bcbs/publ/d515.htm>
- Basel Committee on Banking Supervision (2011). *Operational Risk — Supervisory Guidelines for the Advanced Measurement Approaches*. BIS.
- Chapelle, A. (2019). *Operational Risk Management: Best Practices in the Financial Services Industry*. Wiley.
- COSO (2013). *Internal Control — Integrated Framework*. COSO.
- Verificación local: revisa el enfoque de capital operacional aplicable, el umbral de registro exigido y las obligaciones de reporte de eventos de tu supervisor.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 09 · Derivados y coberturas](09-derivados-y-coberturas.md) | [Parte 11](../README.md) · [Programa](../../../SYLLABUS.md) | [11 · Riesgo tecnológico y ciberseguridad →](11-riesgo-tecnologico-y-ciberseguridad.md) |
<!-- gen:footer:end -->
