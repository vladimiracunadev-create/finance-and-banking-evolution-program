---
part: 16
class: 8
title: "Modelos de riesgo"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 08 · Modelos de riesgo

> [← 07 · Originación y decisión](07-originacion-y-decision.md) · [Índice de la parte](../README.md) · [09 · Operaciones y pagos →](09-operaciones-y-pagos.md)

**Parte 16 — Proyecto Banco Virtual** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Construir los modelos que sostienen las decisiones del Banco Austral: probabilidad de incumplimiento,
pérdida dado el incumplimiento y exposición. Son la capacidad diferenciadora del banco y el insumo de
su precio, su provisión y su capital, y por eso **su gobierno importa tanto como su estadística**.

El motor de la clase anterior necesita estimaciones de riesgo, y un banco nuevo no tiene historia con la que construirlas. Esta clase resuelve ese problema real: qué se usa en la fase uno, cómo se sustituye en la dos y qué validación se exige en cada etapa.

## 📚 Objetivos

Al finalizar podrás:

1. **Desarrollar** un modelo de PD con datos alternativos.
2. **Estimar** LGD y EAD para los productos del banco.
3. **Validar** los modelos con los seis componentes de la validación.
4. **Documentar** el dominio de aplicación y sus condiciones.
5. **Diseñar** el monitoreo y la revalidación desde el inicio.

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

Los tres primeros términos son los parámetros de la pérdida esperada; los cinco siguientes, la construcción y validación del modelo. El **dominio de aplicación** es la declaración que evita el mayor riesgo: un modelo construido con una población no vale para otra, y usarlo igualmente es el error más frecuente.

| Concepto | Comprensión verificable |
|---|---|
| `probabilidad de incumplimiento` | Probabilidad de que el deudor incumpla en 12 meses. |
| `pérdida dado el incumplimiento` | Porcentaje de la exposición que se pierde. |
| `exposición al incumplimiento` | Saldo esperado en el momento del incumplimiento. |
| `muestra de desarrollo` | Datos con los que se estima el modelo. |
| `muestra fuera de tiempo` | Período distinto, para validar estabilidad. |
| `poder discriminante` | Capacidad de separar buenos de malos pagadores. |
| `calibración` | Que la probabilidad predicha coincida con la observada. |
| `dominio de aplicación` | Población y condiciones donde el modelo es válido. |

## 🧠 Modelo mental

El modelo mental es una escalera de sustitución: se empieza con parámetros de la industria, se pasa a modelos propios cuando hay datos y se recalibra continuamente. Declarar en qué escalón se está es parte de la honestidad del proyecto.

```text
EL PROBLEMA DEL BANCO NUEVO

  un modelo de PD se estima sobre créditos otorgados
  que ya se sabe si pagaron o no

  UN BANCO NUEVO NO TIENE ESOS DATOS

TRES CAMINOS, EN ORDEN DE PREFERENCIA
  1. datos de un socio o de un buró, del mismo segmento
  2. modelo experto: criterios de política sin modelo
     estadístico, con calibración conservadora
  3. modelo de un mercado comparable, con ajuste
     y con vigilancia estrecha

  Y EN LOS TRES CASOS
    el modelo propio se construye con los datos
    que el propio banco genere: 18 a 30 meses
```

## 📖 Desarrollo

### 1. Estrategia de modelos por fase

La estrategia cambia según la madurez del banco. La tabla la recoge.

| Fase | Meses | Enfoque | Vigilancia |
|---|---|---|---|
| Inicial | 0–12 | Modelo experto con reglas de política | Máxima; revisión mensual |
| Transición | 12–24 | Modelo estadístico sobre datos propios parciales | Alta; revisión trimestral |
| Maduro | 24+ | Modelo propio validado, con muestra fuera de tiempo | Estándar; revisión semestral |

```text
EN LA FASE INICIAL
  el "modelo" es la política de crédito de la clase 7
  con una calibración conservadora de PD por segmento

  su PD no se estima: se SUPONE, con fundamento
  y ese supuesto es crítico y se declara
```

### 2. Modelo de PD para P2

El modelo de probabilidad de incumplimiento se construye con datos propios cuando los hay. El procedimiento lo recorre.

```text
VARIABLES CANDIDATAS (datos alternativos, Parte 14, clase 7)

  DE PAGOS DE SERVICIOS
    · meses con pago a tiempo en los últimos 12
    · número de servicios a su nombre
    · variabilidad del monto pagado

  DE FLUJO DE CUENTA
    · ingreso medio mensual verificado
    · variabilidad del ingreso (coeficiente de variación)
    · meses con ingreso en los últimos 12
    · saldo medio al cierre de mes
    · días con saldo cero

  DE COMPORTAMIENTO
    · antigüedad de la relación con el banco
    · uso de medios de pago
    · cumplimiento en escalones anteriores

  DEMOGRÁFICAS (con cuidado)
    · edad: sí, con relación causal con la estabilidad
    · zona: NO (sustituto de origen socioeconómico)
    · género: NO (atributo protegido)
    · estado civil: NO (sustituto)
```

```text
LA VARIABLE MÁS PREDICTIVA DEL SEGMENTO
  "meses con ingreso en los últimos 12"
  captura la ESTABILIDAD, que es lo que
  determina la capacidad de pagar cuotas

  y su relación causal es directa y explicable
```

### 3. Estimación de LGD

La severidad se estima desde recuperaciones observadas o desde valores de referencia. El procedimiento lo hace.

```text
LGD = 1 − tasa de recuperación

COMPONENTES
  · recuperación por gestión de cobranza
  · recuperación por ejecución de garantía (P2 no tiene)
  · costos del proceso de recuperación
  · valor del tiempo hasta recuperar

P2 — CRÉDITO SIN GARANTÍA
  recuperación observada en el segmento (referencia sectorial): 46 %
  costo de la gestión: 8 % del saldo
  plazo medio de recuperación: 14 meses
  descuento al 17,68 %: factor 0,81
  LGD = 1 − (0,46 − 0,08) × 0,81 = 1 − 0,308 = 69,2 %

  EL SUPUESTO DE LA CLASE 6 ERA 58 %
  → el cálculo completo da 69,2 %
```

**Este es el tipo de hallazgo que el proyecto persigue.** Un supuesto asumido tres clases atrás resulta
optimista al calcularlo con rigor, y su corrección se propaga a precio, provisión y capital.

```text
E2 — CAPITAL DE TRABAJO
  con cesión de flujo de ventas por medios de pago
  recuperación por cesión: 34 % del saldo
  recuperación por gestión: 22 %
  costo: 6 %
  plazo: 9 meses, factor 0,88
  LGD = 1 − (0,34 + 0,22 − 0,06) × 0,88 = 1 − 0,440 = 56,0 %

  el supuesto era 48 %
```

### 4. Exposición al incumplimiento

La exposición depende del producto y de los cupos disponibles. El procedimiento la estima.

```text
P2 — PRODUCTO A CUOTAS
  EAD = saldo en el momento del incumplimiento
  típicamente, el incumplimiento ocurre
  en el primer tercio del plazo
  EAD ≈ 82 % del monto original

E2 — LÍNEA REVOLVENTE
  EAD = saldo utilizado + factor × parte no utilizada
  el deudor en dificultad UTILIZA la línea
  factor de conversión observado: 62 %
  → mucho mayor que el factor regulatorio del 20 %

  EAD = 214 000 + 78 892 × 62 % = 262 913
  frente a los 214 000 supuestos
```

```text
EL FACTOR DE CONVERSIÓN EN EL INCUMPLIMIENTO
  es una de las estimaciones más subestimadas
  quien va a incumplir usa todo lo que tiene disponible

  → la pérdida esperada de una línea revolvente
    se calcula sobre la exposición esperada AL INCUMPLIR,
    no sobre la utilizada hoy
```

### 5. Validación y gobierno

Todo modelo se valida de forma independiente y se gobierna, como exige la Parte 11. La tabla lo recoge.

```text
LOS SEIS COMPONENTES (Parte 11, clase 12)
  conceptual · datos · resultados · implantación · uso · gobierno

PARA UN BANCO NUEVO, EL COMPONENTE CRÍTICO ES DATOS
  la muestra de desarrollo no es propia
  → la validación debe evaluar la REPRESENTATIVIDAD
    de la población de origen respecto de la propia
```

```text
DOMINIO DE APLICACIÓN DEL MODELO DE P2
  población: personas de 21 a 68 años
  con al menos 6 meses de ingreso verificable
  canal: digital y corresponsal
  monto: hasta 6,0
  plazo: hasta 24 meses
  vigencia: hasta la primera revalidación con datos propios

  CONDICIONES QUE LO INVALIDAN
    · cambio del canal de originación
    · ampliación del rango de monto o plazo
    · cambio material de la composición de solicitantes
    · deriva de población con PSI > 0,10
    · deriva de calibración > 25 % durante dos trimestres
```

## 🧮 Ejemplo guiado

El ejemplo construye un modelo de probabilidad de incumplimiento y lo valida fuera de tiempo. La caída de desempeño fuera de tiempo es lo que hay que medir antes de usarlo.

**Situación.** Recalcular el efecto de las LGD y EAD corregidas sobre todo el modelo del banco.

```text
CORRECCIONES
  LGD de P2: 58 % → 69,2 %
  LGD de E2: 48 % → 56,0 %
  EAD de E2: 214 000 → 262 913
```

**Paso 1 — recalcula la pérdida esperada.**

```text
P2
  cartera: 118 048
  PD media ponderada: 6,84 %
  LGD: 69,2 %
  pérdida esperada: 118 048 × 6,84 % × 69,2 % = 5 588
  costo de riesgo: 4,73 %  (era 3,97 %)

E2
  EAD: 262 913
  PD: 4,2 %
  LGD: 56,0 %
  pérdida esperada: 262 913 × 4,2 % × 56,0 % = 6 183
  sobre cartera utilizada de 214 000: 2,89 %  (era 2,02 %)

E3
  saldo: 3 923, PD 0,4 %, LGD 35 %
  pérdida esperada: 5

PÉRDIDA ESPERADA TOTAL: 11 776
sobre cartera contable de 335 971: 3,51 %
```

**Paso 2 — compara con el compromiso.**

```text
COMPROMISO: 3,60 %
RECALCULADO: 3,51 %

  ¿CUMPLE?
    sí, y por menos margen del que parecía

  ANTES DE LA CORRECCIÓN: 3,26 %
  DESPUÉS: 3,51 %
  el margen sobre el compromiso pasó de 0,34 a 0,09 puntos
```

**Paso 3 — verifica el efecto en el precio.**

```text
LA TASA MÍNIMA DE P2 SE CALCULÓ CON LGD DE 58 %

  costo de fondos                    7,88 %
  pérdida esperada (6,84 % × 69,2 %) 4,73 %  (era 3,94 %)
  costo operativo                    3,20 %
  costo del capital                  2,02 %
  margen objetivo                    2,00 %
  TASA MÍNIMA CORREGIDA             19,83 %  (era 19,04 %)

  precio decidido: 23,50 %
  margen sobre el piso: 3,67 puntos  (era 4,46)
  → sigue siendo suficiente  ✓
```

```text
TASA MÍNIMA DE E2 CORREGIDA
  costo de fondos                    7,55 %
  pérdida esperada (4,2 % × 56 % × factor EAD 1,229)
                                     2,89 %  (era 2,02 %)
  costo operativo                    1,80 %
  costo del capital                  1,66 %
  costo del compromiso               0,35 %
  margen objetivo                    1,60 %
  TASA MÍNIMA CORREGIDA             15,85 %  (era 14,98 %)

  precio decidido: 16,40 %
  margen sobre el piso: 0,55 puntos  (era 1,42)
  → MUY AJUSTADO
```

**Paso 4 — decide sobre el precio de E2.**

```text
UN MARGEN DE 0,55 PUNTOS SOBRE LA TASA MÍNIMA
NO DEJA ESPACIO PARA NINGUNA DESVIACIÓN

  OPCIONES
    a) subir el precio a 17,20 %
       posición competitiva: sigue en el rango bajo
       de la banca (15,5 % a 18,2 %)
    b) reducir la LGD mejorando la cesión de flujo
       de ventas: de 34 % a 45 % de recuperación
       LGD: 56,0 % → 46,3 %
       pérdida esperada: 2,39 %
       tasa mínima: 15,35 %
    c) reducir el factor de conversión de la línea
       con límites dinámicos: si el cliente se deteriora,
       la línea disponible se reduce automáticamente
       factor: 62 % → 40 %
       EAD: 245 557
       pérdida esperada: 2,63 %

  DECISIÓN: (b) y (c) combinadas
    · cesión de flujo con instrucción irrevocable
      al procesador de medios de pago
    · límites dinámicos ligados al comportamiento
    tasa mínima resultante: 14,92 %
    margen sobre el piso: 1,48 puntos  ✓
```

**Paso 5 — verifica el efecto de (c) sobre el cliente.**

```text
LÍMITES DINÁMICOS: ¿ES ACEPTABLE PARA EL CLIENTE?

  reducir la línea disponible de una empresa
  en dificultad puede precipitar su problema

  DISEÑO RESPONSABLE
    · la reducción se comunica con 30 días de antelación
    · no aplica a lo ya utilizado
    · los disparadores son objetivos y están en el contrato
    · el cliente puede solicitar revisión
    · si el deterioro es transitorio y verificable,
      la línea se restituye

  Y LA ALTERNATIVA
    sin límites dinámicos, el precio sube 0,80 puntos
    para todos los clientes, incluidos los que nunca
    se deterioran
    → los límites dinámicos trasladan el costo
      a quien genera el riesgo
```

**Paso 6 — recalcula el modelo económico completo.**

```text
  margen financiero
    P2: 118 048 × (23,50 % − 7,88 %) = 18 439
    E2: 214 000 × (16,40 % − 7,55 %) = 18 939
    E3: 3 923 × 21,10 % = 828
    captación: 5 790
    tesorería: 1 573
    costo de la liquidez: −2 070
    TOTAL: 43 499

  comisiones: 12 443
  margen bruto: 55 942
  gastos (48 %): −26 852
  costo de riesgo (recalculado con las correcciones de (b) y (c)):
    P2: 5 588
    E2: 245 557 × 4,2 % × 46,3 % = 4 775
    E3: 5
    TOTAL: 10 368  → 3,09 % de la cartera
  resultado antes de impuestos: 18 722
  resultado neto: 13 667
  rentabilidad sobre patrimonio: 13 667 / 50 000 = 27,33 %
```

**Paso 7 — cuestiona el resultado.**

```text
27,33 % FRENTE A UN COSTO DE CAPITAL DE 17,68 %
ES UN MARGEN DE 9,65 PUNTOS

  ¿ES CREÍBLE PARA UN BANCO NUEVO EN EL AÑO 3?

  VERIFICACIÓN CONTRA REFERENCIAS
    bancos especializados en el segmento
    de personas sin historial: 22 % a 34 % de retorno
    → el resultado está en el rango

  PERO EL AÑO 3 NO ES EL RÉGIMEN
    · la cartera aún es joven: la mora madura
      entre los meses 12 y 30
    · el modelo de PD no está validado con datos propios
    · las LGD son referencias sectoriales, no propias

  CONSERVADURISMO NECESARIO
    aplicar un factor de incertidumbre del 25 %
    sobre la pérdida esperada mientras
    los modelos no estén validados con datos propios
    provisión adicional: 2 592
    resultado neto: 11 775
    rentabilidad: 23,55 %
```

**Paso 8 — establece el gobierno de los modelos.**

```text
DESDE EL DÍA UNO

  1. VALIDACIÓN INDEPENDIENTE
     antes de usar cualquier modelo, incluido el experto
     validador: no puede ser quien lo construyó
     en un banco de 260 personas: validación externa
     el primer año

  2. DOMINIO DE APLICACIÓN
     documentado para cada modelo, con sus condiciones
     de invalidación

  3. MONITOREO MENSUAL EL PRIMER AÑO
     · PSI por variable
     · calibración: predicho vs. observado
     · poder discriminante
     · tasa de excepciones

  4. UMBRALES DE ALERTA
     PSI > 0,10 · desviación de calibración > 25 %
     · Gini < 0,45

  5. REVALIDACIÓN
     a los 12 meses con datos propios parciales
     a los 24 meses con muestra fuera de tiempo

  6. CONSERVADURISMO EXPLÍCITO
     factor del 25 % sobre la pérdida esperada
     mientras los modelos no estén validados con datos propios
     → se libera gradualmente conforme la validación avanza

  7. REGISTRO DE DECISIONES
     la entidad DECISIÓN de la clase 4
     con modelo, versión, entradas y factores
```

**Interpreta:** calcular las LGD con rigor en lugar de suponerlas **elevó el costo de riesgo de 3,26 % a
3,51 %**, dejó a E2 con un margen de 0,55 puntos sobre su tasa mínima y obligó a rediseñar dos elementos
del producto. El proyecto está construido para que ese tipo de hallazgo aparezca: un supuesto cómodo
asumido en una clase temprana se propaga hasta que alguien lo calcula, y entonces cambia el diseño.

## 🏦 Del cliente al banco

El cliente recibe una decisión y el banco la basa en un modelo con su dominio declarado. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Me redujeron la línea sin usarla» | Límite dinámico por deterioro | 16, clase 8 |
| «Cedí mi flujo de ventas» | Recuperación que baja la LGD y el precio | 13, clase 4 |
| «Mi tasa es menor que la del mercado» | LGD menor por la cesión | 16, clase 6 |
| «El banco es muy prudente al inicio» | Factor de incertidumbre por modelos no validados | 16, clase 8 |
| «Me explicaron los factores del rechazo» | Registro de decisión | 14, clase 11 |

## 🧪 Práctica

El laboratorio pide construir y validar un modelo. Declarar su dominio de aplicación es parte del entregable.

En `labs/lab-04.md`, sección de modelos:

1. Selecciona variables candidatas y descarta las que sean sustitutas prohibidas.
2. Estima LGD y EAD con sus componentes completos.
3. Recalcula precio, provisión y capital con los parámetros corregidos.
4. Diseña el gobierno de modelos con dominio, monitoreo y revalidación.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen modelos que fallaron en producción. Las causas son validación insuficiente y uso fuera del dominio.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| LGD supuesta y no calculada | Optimista | Calcula con todos sus componentes. |
| EAD igual al saldo utilizado | El deudor usa todo antes de incumplir | Usa el factor de conversión observado. |
| Modelo sin validación por ser nuevo | El riesgo es mayor, no menor | Validación externa el primer año. |
| Sin factor de conservadurismo | Modelos no validados | Aplícalo y libéralo gradualmente. |
| Variables sustitutas de atributos protegidos | Discriminación | Descártalas en la selección. |
| Dominio de aplicación no documentado | Uso fuera de rango | Documéntalo con sus invalidaciones. |

## ❓ Preguntas de comprobación

1. ¿Qué problema enfrenta un banco nuevo al construir su modelo de PD?
2. ¿Por qué la LGD calculada resultó mayor que la supuesta?
3. ¿Por qué el factor de conversión en el incumplimiento supera al regulatorio?
4. ¿Cómo trasladan los límites dinámicos el costo a quien genera el riesgo?
5. ¿Por qué un banco nuevo necesita un factor de conservadurismo explícito?

## 📥 Entregable

Guarda en `portfolio/parte-16/clase-08/`:

- la selección de variables con las descartadas y su razón;
- la estimación de LGD y EAD con todos sus componentes;
- el recálculo de precio, provisión y capital;
- el gobierno de modelos con dominio, monitoreo, umbrales y revalidación.

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

- Siddiqi, N. (2017). *Intelligent Credit Scoring* (2.ª ed.). Wiley.
- Basel Committee on Banking Supervision (2005). *Studies on the Validation of Internal Rating Systems*. BIS.
- Basel Committee on Banking Supervision (2017). *Basel III: Finalising post-crisis reforms*, parámetros IRB. BIS.
- Board of Governors of the Federal Reserve System (2011). *SR 11-7: Guidance on Model Risk Management*.
- Caouette, J., Altman, E., Narayanan, P. y Nimmo, R. (2008). *Managing Credit Risk* (2.ª ed.). Wiley.
- Verificación local: revisa las exigencias de tu supervisor sobre estimación de parámetros, validación de modelos y provisiones mínimas.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 07 · Originación y decisión](07-originacion-y-decision.md) | [Parte 16](../README.md) · [Programa](../../../SYLLABUS.md) | [09 · Operaciones y pagos →](09-operaciones-y-pagos.md) |
<!-- gen:footer:end -->
