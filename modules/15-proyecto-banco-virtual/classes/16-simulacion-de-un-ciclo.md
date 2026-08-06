---
part: 16
class: 16
title: "Simulación de un ciclo"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 16 · Simulación de un ciclo

> [← 15 · Prueba de estrés del banco](15-prueba-de-estres-del-banco.md) · [Índice de la parte](../README.md) · [17 · Simulación de una crisis →](17-simulacion-de-una-crisis.md)

**Parte 16 — Proyecto Banco Virtual** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Operar el Banco Austral durante tres años simulados, tomando las decisiones mes a mes con la información
que efectivamente estaría disponible. Es la clase donde el proyecto deja de ser un diseño y **se
convierte en una secuencia de decisiones bajo incertidumbre**.

## 📚 Objetivos

Al finalizar podrás:

1. **Operar** el banco con decisiones periódicas y consecuencias acumulativas.
2. **Decidir** con información incompleta y rezagada.
3. **Reaccionar** a desviaciones del plan con las acciones comprometidas.
4. **Distinguir** las desviaciones que exigen acción de las que son ruido.
5. **Evaluar** tu propio desempeño como director del banco.

<!-- gen:agenda:start -->
## Agenda de 90 minutos

| Minutos | Bloque | Qué ocurre |
|---:|---|---|
| 0–10 | Activación | Pregunta diagnóstica y recuperación de la clase anterior. |
| 10–35 | Conceptos | Desarrollo guiado con la fuente oficial a la vista. |
| 35–55 | Ejemplo guiado | El docente resuelve el caso numérico paso a paso. |
| 55–80 | Práctica | El estudiante replica con datos propios o sintéticos. |
| 80–90 | Cierre | Preguntas de comprobación y registro en el portafolio. |
<!-- gen:agenda:end -->

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| `simulación` | Ejercicio de decisión secuencial con consecuencias. |
| `rezago de información` | Tiempo entre el hecho y su medición. |
| `desviación material` | La que exige acción, frente a la que es ruido. |
| `decisión irreversible` | La que no se puede deshacer sin costo. |
| `sesgo de acción` | Tendencia a actuar ante cualquier desviación. |
| `sesgo de inacción` | Tendencia a esperar más información. |
| `efecto acumulativo` | Consecuencia de decisiones previas sobre el estado actual. |
| `evaluación del desempeño` | Juicio sobre la calidad de las decisiones, no del resultado. |

## 🧠 Modelo mental

```text
LA DIFERENCIA ENTRE DISEÑAR Y DIRIGIR

  DISEÑAR
    todas las variables a la vista
    tiempo para calcular
    posibilidad de revisar

  DIRIGIR
    información incompleta y con rezago
    plazo para decidir
    las decisiones anteriores condicionan las actuales
    y no se pueden deshacer

  Y UNA ASIMETRÍA
    la mora de una cosecha se conoce a los 6 meses
    la decisión que la produjo se tomó hace 6 meses
    → siempre se corrige con retraso
```

## 📖 Desarrollo

### 1. Estructura de la simulación

```text
HORIZONTE: 36 meses
PERIODICIDAD DE DECISIÓN: mensual
DECISIONES DISPONIBLES CADA MES

  ORIGINACIÓN
    · corte de aprobación por producto (decil)
    · límites de escalón
    · objetivo de volumen por segmento

  PRECIO
    · tasa de cada producto
    · tasa de captación

  BALANCE
    · emisión o no de instrumentos
    · nivel de activos líquidos
    · uso de colateral

  GASTOS
    · plantilla por área
    · inversión en tecnología
    · marketing

  RIESGO
    · ajuste de parámetros de provisión
    · política de cobranza
    · límites internos
```

### 2. Información disponible

| Información | Rezago | Fiabilidad |
|---|---|---|
| Volumen originado | 0 días | Alta |
| Tasa de aprobación | 0 días | Alta |
| Excepciones | 0 días | Alta |
| Saldos y liquidez | 1 día | Alta |
| Mora corriente | 5 días | Alta |
| Mora de cosecha a 6 meses | 6 meses | Alta |
| Resultado del mes | 8 días | Media |
| Costo de riesgo real | 12 meses | Alta |
| Reclamos | 15 días | Media |
| Desempeño del modelo | 3 meses | Media |
| Datos de mercado y competencia | 30 días | Baja |

```text
LA DECISIÓN MÁS IMPORTANTE — EL CORTE DE APROBACIÓN
SE TOMA CON LA INFORMACIÓN MÁS REZAGADA

  su efecto se conoce a los 6 meses (mora de cosecha)
  y se confirma a los 12 (costo de riesgo)
  → toda corrección llega tarde
  → por eso los indicadores principales importan tanto
```

### 3. Distinguir señal de ruido

```text
CRITERIOS PARA DECIDIR SI UNA DESVIACIÓN EXIGE ACCIÓN

  1. MAGNITUD
     ¿supera el umbral de alerta?

  2. PERSISTENCIA
     ¿se repite en dos o tres períodos?

  3. EXPLICACIÓN
     ¿hay una causa identificada?

  4. TENDENCIA
     ¿la dirección es sostenida?

  5. COHERENCIA
     ¿otros indicadores apuntan en el mismo sentido?

  DOS O MÁS CRITERIOS → ACTÚA
  UNO SOLO → OBSERVA UN PERÍODO MÁS
  NINGUNO → RUIDO
```

| Sesgo | Síntoma | Costo |
|---|---|---|
| De acción | Se ajusta el corte cada mes | El modelo nunca se estabiliza; se pierde comparabilidad |
| De inacción | Se espera confirmación completa | La corrección llega 6 meses tarde |

### 4. Efectos acumulativos

```text
DECISIONES CUYO EFECTO SE ACUMULA

  el corte de aprobación de hoy
    → determina la cosecha de hoy
    → determina la mora de dentro de 6 meses
    → determina el costo de riesgo de dentro de 12
    → determina el capital de dentro de 18

  la contratación de personal
    → tarda 3 meses en ser productiva
    → y 12 meses en poder reducirse

  la emisión de deuda
    → fija el costo por su plazo completo

  la inversión en tecnología
    → tarda 9 meses en producir efecto
```

### 5. Evaluación del desempeño

```text
SE EVALÚA LA CALIDAD DE LAS DECISIONES,
NO EL RESULTADO

  una decisión correcta puede tener mal resultado
  una decisión incorrecta puede tener buen resultado

  CRITERIOS
    · ¿usó la información disponible en ese momento?
    · ¿aplicó los criterios de señal frente a ruido?
    · ¿fue coherente con el apetito y con los compromisos?
    · ¿anticipó el efecto acumulativo?
    · ¿registró el fundamento?
    · ¿revisó su efecto cuando la información llegó?
```

## 🧮 Ejemplo guiado

**Situación.** Los primeros doce meses de operación del Banco Austral.

```text
ESTADO INICIAL
  capital: 56 000  (elevado tras la prueba de estrés)
  objetivo interno: 16,5 %
  plan: crecimiento del 24 % anual
  corte de aprobación P2: decil 6
```

**Paso 1 — mes 3: primera desviación.**

```text
INFORMACIÓN DISPONIBLE
  solicitudes recibidas:      7 400  (plan: 6 200)  +19 %
  tasa de aprobación:          64 %  (plan: 60 %)   +4 pp
  excepciones/aprobaciones:   11,2 % (límite: 10 %)  ✗
  volumen originado:          13 400 (plan: 10 800) +24 %

APLICA LOS CRITERIOS
  magnitud: excepciones sobre el límite  ✓
  persistencia: primer mes sobre el límite
  explicación: la demanda superó el plan y los analistas
    aprobaron casos límite para no perderlos
  tendencia: 8,1 % → 9,8 % → 11,2 %  ✓
  coherencia: la tasa de aprobación también subió  ✓

  CUATRO DE CINCO CRITERIOS → ACTÚA
```

```text
DECISIÓN MES 3
  · recordar el límite de excepciones al comité de crédito
  · revisión de las 82 excepciones del mes
  · las que no cumplen el fundamento se reversan
    (no se han desembolsado todas)
  · el objetivo de volumen NO se aumenta pese a la demanda

  FUNDAMENTO REGISTRADO
    la demanda superior al plan no justifica
    relajar el criterio; el capital limita el crecimiento
    y las excepciones anticipan el costo de riesgo
```

**Paso 2 — mes 6: primera cosecha.**

```text
INFORMACIÓN DISPONIBLE
  mora a 6 meses de la cosecha del mes 0: 1,8 %
  objetivo: ≤ 2,10 %  ✓

  PERO
    la cosecha del mes 0 fue pequeña (1 200)
    y se originó con el corte más estricto
    → no es representativa

  DECISIÓN: no actuar; esperar cosechas mayores
  y registrar la limitación de la muestra
```

**Paso 3 — mes 9: segunda señal.**

```text
INFORMACIÓN
  mora a 6 meses de la cosecha del mes 3: 3,4 %
  objetivo: 2,10 %  ✗  alerta: 2,40 %  ✗

  esa es la cosecha con 11,2 % de excepciones

APLICA LOS CRITERIOS
  magnitud: 62 % sobre el objetivo  ✓
  persistencia: segunda cosecha medida
  explicación: las excepciones del mes 3  ✓
  tendencia: 1,8 % → 3,4 %  ✓
  coherencia: los créditos con excepción
    tienen mora del 8,2 % frente al 2,1 % del resto  ✓

  ACTÚA
```

```text
DECISIÓN MES 9
  1. límite de excepciones reducido de 10 % a 6 %
  2. las excepciones requieren aprobación del gerente
     de riesgos, no solo del comité
  3. seguimiento mensual de la mora de las excepciones
     por analista
  4. NO se endurece el corte general:
     la mora del resto de la cartera está en objetivo
     → el problema son las excepciones, no el corte

  ESTA DISTINCIÓN ES LA DECISIÓN CLAVE DEL MES
    endurecer el corte general habría reducido
    la inclusión sin resolver la causa
```

**Paso 4 — mes 11: presión comercial.**

```text
SITUACIÓN
  el crecimiento acumulado es del 19 % anualizado
  frente al plan del 24 %
  la gerencia comercial propone bajar la tasa de P2
  de 23,50 % a 21,80 % para acelerar

INFORMACIÓN
  elasticidad estimada del segmento: no medida
  tasa mínima de P2: 19,83 %
  margen sobre el piso con 21,80 %: 1,97 puntos

APLICA EL CRITERIO
  ¿la propuesta está sobre la tasa mínima? sí
  ¿hay elasticidad medida? NO
  ¿el crecimiento menor compromete algo? el capital
    tiene holgura; el plan es indicativo

  DECISIÓN
    · NO bajar la tasa sin medir la elasticidad
    · ejecutar un experimento controlado (Parte 14, clase 5):
      ofrecer 21,80 % al 15 % de los solicitantes,
      elegidos al azar, durante 2 meses
    · decidir con el resultado
```

**Paso 5 — mes 12: cierre del primer año.**

```text
RESULTADOS DEL AÑO 1
  cartera:            142 400  (plan: 148 000)   −3,8 %
  clientes:            31 200  (plan: 32 400)    −3,7 %
  margen bruto:        18 240  (plan: 19 100)    −4,5 %
  gastos:              19 800  (plan: 19 400)    +2,1 %
  costo de riesgo:      4 620  (plan: 4 200)     +10,0 %
  resultado:           −6 180  (plan: −4 500)
  capital:             49 820
  activos ponderados: 132 400
  ratio CET1:           37,6 %  ✓

EVALUACIÓN DEL AÑO
  · el banco creció menos que el plan
  · el costo de riesgo superó el plan por las excepciones
  · el capital tiene amplia holgura (año inicial)
```

**Paso 6 — evalúa la calidad de las decisiones, no el resultado.**

```text
DECISIÓN DEL MES 3 (frenar las excepciones)
  ¿usó la información disponible? sí
  ¿aplicó los criterios? sí, cuatro de cinco
  ¿fue coherente con el apetito? sí
  ¿anticipó el efecto acumulativo? sí
  RESULTADO: la mora de la cosecha del mes 3
    fue 3,4 % de todos modos
  → LA DECISIÓN FUE CORRECTA Y LLEGÓ TARDE
    porque la información llegó tarde
  → BUENA DECISIÓN, MAL RESULTADO

DECISIÓN DEL MES 9 (distinguir excepciones de corte)
  → identificó la causa correcta
  → evitó reducir la inclusión sin necesidad
  → EXCELENTE DECISIÓN

DECISIÓN DEL MES 11 (no bajar la tasa sin medir)
  → resistió la presión comercial
  → generó la información que faltaba
  → BUENA DECISIÓN
  RESULTADO: el crecimiento quedó 3,8 % bajo el plan
  → un resultado peor con una decisión mejor
```

**Paso 7 — extrae el aprendizaje del año.**

```text
LO QUE LA SIMULACIÓN ENSEÑÓ

  1. EL REZAGO ES EL PROBLEMA CENTRAL
     la decisión del mes 3 se corrigió en el mes 9
     con información del mes 3
     → 6 meses de cosechas deterioradas

     ¿SE PODÍA ANTICIPAR?
       sí: el indicador de excepciones estaba disponible
       EN TIEMPO REAL
       → se actuó en el mes 3, y aun así el daño ocurrió
       → sin ese indicador, se habría descubierto
         en el mes 15

  2. LA PRESIÓN COMERCIAL ES CONSTANTE
     y su argumento siempre es plausible

  3. DISTINGUIR LA CAUSA ES LO QUE MÁS VALOR APORTA
     endurecer el corte habría sido la respuesta obvia
     y la equivocada

  4. UN RESULTADO PEOR PUEDE VENIR
     DE DECISIONES MEJORES
```

**Paso 8 — decide el año 2.**

```text
CON LO APRENDIDO

  1. el límite de excepciones baja a 6 % y se monitorea
     semanalmente, no mensualmente
  2. el experimento de precio se completa y decide
  3. el crecimiento objetivo se mantiene en 24 %
     y no se fuerza
  4. se añade al cuadro de mando el indicador
     "mora de las excepciones a 6 meses", desagregado
     por analista
  5. se acelera el plan de reducción de dependencia
     mayorista (decisión de la clase 15)

  Y UNA DECISIÓN DE GOBIERNO
    el comité de gestión revisará mensualmente
    las decisiones tomadas 6 meses antes,
    cuando su información esté disponible
    → institucionaliza el aprendizaje del rezago
```

**Interpreta:** la mejor decisión del año —distinguir las excepciones del corte general— **produjo un
resultado peor que el plan**, y la decisión correcta del mes 3 no evitó el daño porque la información
llegó después del hecho. Dirigir un banco es tomar decisiones cuyo efecto se conocerá en seis meses con
información de hace seis meses, y la única defensa es mirar los indicadores que no tienen rezago.

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «El banco endureció los criterios» | Corrección con seis meses de rezago | 16, clase 16 |
| «Me ofrecieron mejor tasa que a otros» | Experimento controlado de precio | 14, clase 5 |
| «El banco creció menos de lo anunciado» | Decisión de no forzar el crecimiento | 15, clase 5 |
| «Mi crédito se aprobó por excepción» | Y su mora fue cuatro veces mayor | 12, clase 14 |
| «El banco corrigió su error» | Revisión de decisiones a los 6 meses | 16, clase 16 |

## 🧪 Práctica

En `labs/lab-06.md`, sección de simulación:

1. Opera el banco 12 meses tomando decisiones mensuales registradas.
2. Aplica los cinco criterios de señal frente a ruido en cada desviación.
3. Evalúa la calidad de tus decisiones separándola del resultado.
4. Deriva las reglas de decisión para el año siguiente.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se ajusta el corte cada mes | Sesgo de acción | Aplica los cinco criterios. |
| Se espera confirmación completa | Sesgo de inacción | Dos criterios bastan. |
| Se endurece el corte ante cualquier mora | Causa no identificada | Distingue corte de excepciones. |
| Se baja el precio sin medir elasticidad | Presión comercial | Experimento antes de decidir. |
| Se evalúa por el resultado | Confunde suerte con juicio | Evalúa la decisión. |
| No se revisan las decisiones pasadas | Se pierde el aprendizaje | Revisión a los 6 meses. |

## ❓ Preguntas de comprobación

1. ¿Por qué la decisión más importante se toma con la información más rezagada?
2. ¿Cuántos criterios de señal frente a ruido bastan para actuar?
3. ¿Por qué endurecer el corte general habría sido la respuesta equivocada?
4. ¿Cómo se evalúa una decisión separándola de su resultado?
5. ¿Qué institucionaliza la revisión de decisiones a los seis meses?

## 📥 Entregable

Guarda en `portfolio/parte-16/clase-16/`:

- el registro de las doce decisiones mensuales con su fundamento;
- la aplicación de los criterios de señal frente a ruido en cada una;
- la evaluación de la calidad de las decisiones, separada del resultado;
- las reglas de decisión derivadas para el año siguiente.

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

- Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux. Evaluación de decisiones y resultados.
- Kahneman, D., Sibony, O. y Sunstein, C. (2021). *Noise: A Flaw in Human Judgment*. Little, Brown.
- Basel Committee on Banking Supervision (2015). *Corporate governance principles for banks*. BIS.
- Basel Committee on Banking Supervision (2018). *Stress testing principles*. BIS.
- Rose, P. y Hudgins, S. (2013). *Bank Management and Financial Services* (9.ª ed.). McGraw-Hill.
- Verificación local: revisa la frecuencia con que tu supervisor exige reportes y compárala con el rezago de la información que necesitas para decidir.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 15 · Prueba de estrés del banco](15-prueba-de-estres-del-banco.md) | [Parte 16](../README.md) · [Programa](../../../SYLLABUS.md) | [17 · Simulación de una crisis →](17-simulacion-de-una-crisis.md) |
<!-- gen:footer:end -->
