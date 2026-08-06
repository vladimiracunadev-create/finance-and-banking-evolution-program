---
part: 16
class: 12
title: "Marco de riesgos"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 12 · Marco de riesgos

> [← 11 · Tesorería y balance](11-tesoreria-y-balance.md) · [Índice de la parte](../README.md) · [13 · Cumplimiento y prevención →](13-cumplimiento-y-prevencion.md)

**Parte 16 — Proyecto Banco Virtual** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Integrar todos los riesgos del Banco Austral en un marco único, con su apetito, sus límites y su
gobierno. Once clases han identificado riesgos por separado; esta clase los reúne, revisa el apetito
preliminar de la clase 2 con lo que ahora se sabe, y construye el tablero que dirigirá el banco.

## 📚 Objetivos

Al finalizar podrás:

1. **Construir** la taxonomía de riesgos del banco y su materialidad.
2. **Revisar** el apetito de riesgo con la información del diseño completo.
3. **Definir** los límites, sus alertas y sus acciones comprometidas.
4. **Estimar** el capital económico y compararlo con el regulatorio.
5. **Diseñar** el gobierno de riesgos y su tablero.

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
| `taxonomía de riesgos` | Clasificación de todos los riesgos de la institución. |
| `materialidad` | Relevancia de un riesgo para el banco. |
| `apetito de riesgo` | Cantidad y tipo de riesgo que se decide asumir. |
| `límite` | Umbral cuantitativo que no debe superarse. |
| `alerta` | Umbral previo que exige acción. |
| `acción comprometida` | Lo que se hará al alcanzar la alerta. |
| `capital económico` | Capital que el perfil real de riesgo exige. |
| `tablero de riesgos` | Panel de métricas con límites y tendencia. |

## 🧠 Modelo mental

```text
EL APETITO DE LA CLASE 2 SE FIJÓ CON UNA ESTIMACIÓN
EL DE ESTA CLASE SE FIJA CON EL DISEÑO COMPLETO

  y va a diferir, porque once clases
  cambiaron los parámetros:

    LGD de P2:  58 % → 69,2 %
    LGD de E2:  48 % → 46,3 %
    EAD de E2:  saldo → saldo + 40 % de lo no usado
    eficiencia: 55 % → 42 % (compromiso con reserva)
    dependencia mayorista: no evaluada → 74 %

  UN APETITO QUE NO SE REVISA
  CUANDO EL DISEÑO CAMBIA
  DEJA DE SER UNA RESTRICCIÓN
```

## 📖 Desarrollo

### 1. Taxonomía y materialidad

| Riesgo | Materialidad | Fuente principal | Clase |
|---|---|---|---|
| Crédito | Muy alta | Carteras P2 y E2 | 8 |
| Liquidez y financiamiento | Muy alta | Dependencia mayorista del 74 % | 11 |
| Concentración | Alta | E2 es el 64 % de la cartera | 12 |
| Tasa en el libro de banca | Media | Brecha de duración 0,458 | 11 |
| Operacional | Alta | Procesos nuevos, sin historial | 9 |
| Tecnológico y ciber | Muy alta | Modelo íntegramente digital | 4 |
| Modelo | Alta | Modelos sin validar con datos propios | 8 |
| Cumplimiento | Alta | Segmento sin historial, datos alternativos | 13 |
| Conducta | Alta | Segmento vulnerable | 5 |
| Estratégico | Alta | Banco nuevo, modelo no probado | 2 |
| Reputacional | Alta | Sin marca establecida | 2 |
| Mercado | Baja | Sin libro de negociación | — |
| Moneda | Nula | Todo en moneda local | — |

```text
LOS TRES RIESGOS DE MATERIALIDAD MUY ALTA
  crédito, liquidez y tecnológico

  y el tercero suele subestimarse en el apetito
  de un banco cuyo modelo es digital:
  si el sistema no opera, el banco no existe
```

### 2. Apetito revisado

| Métrica | Clase 2 | Revisado | Alerta | Fundamento del cambio |
|---|---:|---:|---:|---|
| Capital nivel 1 ordinario | ≥ 13,0 % | ≥ 14,0 % | 15,0 % | Modelos sin validar |
| Costo de riesgo | ≤ 2,00 % | ≤ 3,80 % | 3,40 % | LGD y EAD corregidas |
| Mora > 90 días | ≤ 4,20 % | ≤ 5,60 % | 4,80 % | Segmento y escalonamiento |
| Concentración por segmento | ≤ 55 % | ≤ 68 % | 64 % | E2 es 64 % por diseño |
| Concentración sectorial | ≤ 20 % | ≤ 22 % | 19 % | Sin cambio sustantivo |
| Cobertura de liquidez | ≥ 130 % | ≥ 130 % | 145 % | Se mantiene (clase 11) |
| Dependencia mayorista | no fijada | ≤ 78 % | 72 % | **Nueva** |
| Exposición individual | ≤ 5 % | ≤ 4 % | 3,5 % | Banco pequeño |
| Reclamos fundados/1000 | ≤ 1,50 | ≤ 1,50 | 1,20 | Sin cambio |
| Disponibilidad de sistemas | no fijada | ≥ 99,7 % | 99,8 % | **Nueva** |
| Modelos fuera de validación | no fijada | 0 | — | **Nueva** |
| Excepciones/aprobaciones | no fijada | ≤ 10 % | 8 % | **Nueva** |

```text
CUATRO MÉTRICAS NUEVAS
  y las cuatro corresponden a riesgos
  que el diseño detallado hizo visibles:
  dependencia mayorista, disponibilidad,
  validación de modelos y excepciones
```

### 3. Límites operativos

```text
LÍMITES DERIVADOS DEL APETITO

  CRÉDITO
    exposición individual: 4 % de 55 575 = 2 223
    exposición a grupo económico: 6 % = 3 335
    concentración sectorial: 22 % de la cartera
    excepciones: 10 % de las aprobaciones mensuales
    crecimiento máximo de cartera: 32 % anual
      (derivado de la capacidad de capital)

  LIQUIDEZ
    cobertura mínima: 130 %
    activos líquidos mínimos: 70 806
    dependencia mayorista: 78 %
    vencimientos concentrados en 30 días: ≤ 12 % del pasivo
    colateral preparado: ≥ 80 000

  TASA
    brecha de duración: ≤ 0,80
    caída del valor económico: ≤ 12 % del capital

  OPERACIONAL
    pérdida operacional anual: ≤ 0,9 % del margen bruto = 503
    partidas de conciliación > 3 días: 0
    disponibilidad de sistemas: ≥ 99,7 %

  MODELO
    modelos fuera de plazo de validación: 0
    desviación de calibración: ≤ 25 % durante 2 trimestres
```

### 4. Acciones comprometidas

| Métrica en alerta | Acción comprometida | Plazo |
|---|---|---|
| Capital < 15,0 % | Revisión del plan de crecimiento; sin dividendos | Inmediato |
| Costo de riesgo > 3,40 % | Endurecimiento del corte de aprobación en 1 decil | 30 días |
| Mora > 4,80 % | Análisis de cosechas; refuerzo de cobranza temprana | 15 días |
| Concentración E2 > 64 % | Suspensión de crecimiento en E2 | Inmediato |
| Cobertura < 145 % | Compra de activos líquidos; freno a desembolsos | 5 días |
| Dependencia mayorista > 72 % | Aceleración del plan de captación | 30 días |
| Excepciones > 8 % | Revisión del comité de crédito; análisis por analista | 15 días |
| Disponibilidad < 99,8 % | Revisión técnica y plan de remediación | 10 días |
| Modelo fuera de validación | Suspensión de su uso | Inmediato |

```text
LA ÚLTIMA ACCIÓN ES LA MÁS DURA Y LA MÁS NECESARIA
  suspender el uso de un modelo detiene la originación
  → por eso la validación se programa con antelación
    y no se deja llegar al plazo
```

### 5. Capital económico

```text
CAPITAL ECONÓMICO POR RIESGO (nivel de confianza 99,8 %)

  crédito           enfoque IRB con ajuste por concentración
                    y por incertidumbre de parámetros
                    34 600
  operacional       enfoque estandarizado + escenarios
                    de un banco nuevo
                    6 800
  tasa              caída del valor económico en el peor
                    de los seis escenarios
                    4 344
  liquidez          costo de sustituir el financiamiento
                    mayorista en estrés durante 90 días
                    5 200
  negocio           caída del 30 % del margen por
                    competencia o cambio regulatorio
                    5 900
  modelo            incertidumbre de parámetros no validados
                    3 800
  SUMA SIMPLE       60 644

CAPITAL REGULATORIO REQUERIDO
  11,34 % × 311 725 = 35 349

  CAPITAL ECONÓMICO: 60 644
  CAPITAL REGULATORIO: 35 349
  CAPITAL DISPONIBLE: 55 575

  EL CAPITAL ECONÓMICO SUPERA AL DISPONIBLE EN 5 069
```

## 🧮 Ejemplo guiado

**Situación.** Resolver el déficit de capital económico.

**Paso 1 — verifica la agregación.**

```text
LA SUMA SIMPLE SUPONE CORRELACIÓN 1

  ¿es razonable?
    para efectos regulatorios: sí, es lo prudente
    para gestión: se puede reconocer diversificación

  AGREGACIÓN CON CORRELACIONES
    crédito-liquidez:      0,60  (se materializan juntos)
    crédito-negocio:       0,55
    crédito-operacional:   0,25
    crédito-modelo:        0,70  (el modelo mide el crédito)
    crédito-tasa:          0,30
    resto: 0,20 a 0,35

  CAPITAL AGREGADO: 48 920
  beneficio de diversificación: 11 724  (19,3 %)

  CAPITAL DISPONIBLE: 55 575
  HOLGURA: 6 655  ✓
```

**Paso 2 — cuestiona el reconocimiento de la diversificación.**

```text
¿ES LEGÍTIMO RECONOCERLA EN UN BANCO NUEVO?

  las correlaciones se estiman con datos históricos
  el Banco Austral no los tiene
  → las correlaciones son SUPUESTOS

  Y LA CORRELACIÓN CRÉDITO-MODELO DE 0,70
    subestima el problema:
    si el modelo está mal, el crédito está mal
    la correlación real puede ser cercana a 1

  DECISIÓN CONSERVADORA
    reconocer diversificación solo entre los riesgos
    con mecanismos claramente independientes:
    operacional, tecnológico y el resto

    crédito, modelo y liquidez: suma simple
      34 600 + 3 800 + 5 200 = 43 600
    tasa, negocio y operacional, agregados: 10 900
    CAPITAL ECONÓMICO: 54 500

  CAPITAL DISPONIBLE: 55 575
  HOLGURA: 1 075  (1,9 %)
```

**Paso 3 — evalúa la holgura.**

```text
UNA HOLGURA DEL 1,9 % SOBRE EL CAPITAL ECONÓMICO
NO ES SUFICIENTE PARA UN BANCO NUEVO

  cualquier desviación de un parámetro
  la elimina

  OPCIONES
    a) reducir el capital económico actuando
       sobre sus componentes
    b) aumentar el capital
    c) reducir el tamaño del banco
```

**Paso 4 — actúa sobre los componentes.**

```text
COMPONENTE DE MODELO: 3 800
  se elimina cuando los modelos se validan
  con datos propios: mes 24
  → decrece de 3 800 a 0 en 24 meses

COMPONENTE DE LIQUIDEZ: 5 200
  se calculó sobre una dependencia mayorista del 74 %
  con el plan de la clase 11 (bajar a 55 % en 24 meses):
  componente: 5 200 → 2 900
  reducción: 2 300

COMPONENTE DE CRÉDITO: 34 600
  incluye 4 200 de ajuste por incertidumbre
  de parámetros; se libera con la validación

COMPONENTE DE NEGOCIO: 5 900
  se reduce cuando el modelo demuestra su viabilidad
  → año 3 en adelante
```

**Paso 5 — proyecta la trayectoria.**

```text
CAPITAL ECONÓMICO PROYECTADO
                        año 3    año 4    año 5
  crédito               34 600   32 800   38 400
    (crece con la cartera, baja el ajuste)
  modelo                 3 800    1 200        0
  liquidez               5 200    3 600    2 900
  tasa                   4 344    4 600    5 100
  negocio                5 900    4 800    4 200
  operacional            6 800    7 400    8 100
  agregado (parcial)    54 500   49 200   52 600

CAPITAL DISPONIBLE
  año 3: 55 575
  año 4: 55 575 + retención (11 400) = 66 975
  año 5: + retención (14 200) = 81 175

  HOLGURA
  año 3:  1 075   (1,9 %)
  año 4: 17 775  (36,1 %)
  año 5: 28 575  (54,3 %)

  EL AÑO 3 ES EL AÑO CRÍTICO
```

**Paso 6 — decide sobre el año 3.**

```text
OPCIONES PARA EL AÑO 3

  a) moderar el crecimiento de la cartera
     reducir 8 % la cartera del año 3
     capital económico: 54 500 → 51 800
     holgura: 3 775  (7,3 %)
     costo: 2 400 de margen

  b) aportar capital adicional
     los accionistas comprometieron hasta 12 000 (clase 3)
     aporte de 6 000
     holgura: 7 075  (13,0 %)
     costo: dilución o retorno exigido sobre más capital

  c) acelerar la validación de modelos
     validación externa a los 12 meses en lugar de 24
     costo: 320
     libera 2 000 del componente de modelo
     holgura: 3 075  (5,6 %)

  DECISIÓN: (c) y (a) parcial
    validación acelerada: libera 2 000
    moderación del crecimiento en 4 %: libera 1 350
    holgura resultante: 4 425  (8,4 %)
    costo total: 320 + 1 200 = 1 520
```

**Paso 7 — construye el tablero.**

```text
TABLERO DE RIESGOS DEL BANCO AUSTRAL

| dimensión         métrica                   límite  alerta  actual |
| solvencia         capital nivel 1 ordinario 14,0 %  15,0 %  17,8 % |
| solvencia         capital económico/dispon. 100 %   92 %    98,1 % |
| crédito           costo de riesgo            3,80 %  3,40 %  3,09 %|
| crédito           mora > 90 días             5,60 %  4,80 %  4,10 %|
| crédito           mora de cosecha a 6 meses  2,80 %  2,40 %  2,10 %|
| crédito           excepciones/aprobaciones  10,0 %   8,0 %   6,4 % |
| concentración     E2 sobre cartera          68,0 %  64,0 %  63,7 % |
| concentración     mayor deudor/patrimonio    4,0 %   3,5 %   2,8 % |
| liquidez          cobertura de liquidez      130 %   145 %   220 % |
| liquidez          dependencia mayorista     78,0 %  72,0 %  74,0 % |
| liquidez          colateral preparado       80 000  90 000  83 460 |
| tasa              caída del valor económico 12,0 %  10,0 %   7,8 % |
| operacional       pérdida anual/margen bruto 0,90 %  0,70 %  0,42 %|
| operacional       partidas pendientes >3 días    0      —       0  |
| tecnológico       disponibilidad             99,7 % 99,8 %  99,84 %|
| modelo            modelos fuera de validación    0      —       0  |
| conducta          reclamos fundados/1000      1,50    1,20    0,84 |
```

**Paso 8 — establece el gobierno.**

```text
COMITÉ DE RIESGOS DEL DIRECTORIO
  · mensual el primer año, bimestral después
  · mayoría independiente
  · sesión sin gerencia, trimestral
  · aprueba: apetito, límites, políticas, modelos

COMITÉ DE ACTIVOS Y PASIVOS
  · quincenal el primer año
  · liquidez, tasa, precio de transferencia, balance

COMITÉ DE CRÉDITO
  · semanal
  · operaciones sobre atribución y excepciones

DIRECTOR DE RIESGOS
  · acceso directo al comité de riesgos
  · derecho de veto sobre productos nuevos
  · presupuesto aprobado por el comité, no por la gerencia

ESCALAMIENTO
  alerta → notificación en 2 días, acción en el comité siguiente
  límite → notificación inmediata, plan en 5 días
  exceso material → sesión extraordinaria
```

**Interpreta:** el capital económico calculado con rigor resultó **superior al capital disponible**, y
solo el reconocimiento parcial de diversificación —el conservador, no el favorable— dejó una holgura del
1,9 %. La decisión de acelerar la validación de modelos, que cuesta 320, libera 2 000 de capital: es el
tipo de decisión que solo aparece cuando el capital económico se calcula en serio en lugar de asumir que
el regulatorio basta.

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «El banco endureció sus criterios» | Alerta de costo de riesgo activada | 16, clase 12 |
| «Dejaron de crecer en empresas» | Límite de concentración | 11, clase 3 |
| «El banco es muy conservador» | Capital económico ajustado | 11, clase 14 |
| «Mi línea tiene un tope bajo» | Límite de exposición individual | 16, clase 12 |
| «El servicio nunca falla» | Límite de disponibilidad | 10, clase 16 |

## 🧪 Práctica

En `labs/lab-06.md`, sección de riesgos:

1. Construye la taxonomía con su materialidad y su fuente.
2. Revisa el apetito con los parámetros del diseño completo.
3. Estima el capital económico y evalúa el reconocimiento de diversificación.
4. Construye el tablero con límites, alertas y acciones comprometidas.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Apetito no revisado tras el diseño | Deja de restringir | Revísalo con los parámetros reales. |
| Diversificación reconocida en exceso | Correlaciones supuestas | Reconoce solo la clara. |
| Capital regulatorio como suficiente | El económico puede superarlo | Calcúlalo. |
| Límite sin acción comprometida | No restringe | Cada alerta con su acción. |
| Riesgo tecnológico subestimado | El modelo es digital | Materialidad muy alta. |
| Modelos sin límite de validación | Se llega al plazo operando | Límite de cero, con antelación. |

## ❓ Preguntas de comprobación

1. ¿Por qué el apetito de la clase 2 tenía que revisarse?
2. ¿Por qué la correlación entre crédito y modelo puede ser cercana a 1?
3. ¿Qué significa que el capital económico supere al disponible?
4. ¿Por qué acelerar la validación de modelos libera capital?
5. ¿Cuál es la acción comprometida más dura y por qué es necesaria?

## 📥 Entregable

Guarda en `portfolio/parte-16/clase-12/`:

- la taxonomía con materialidad y fuente;
- el apetito revisado con el fundamento de cada cambio;
- el capital económico con su agregación justificada y su trayectoria;
- el tablero completo con límites, alertas, acciones y gobierno.

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

- Financial Stability Board (2013). *Principles for an Effective Risk Appetite Framework*. FSB.
- Basel Committee on Banking Supervision (2009). *Range of practices and issues in economic capital frameworks*. BIS.
- Basel Committee on Banking Supervision (2019). *Overview of Pillar 2 supervisory review practices*. BIS.
- Basel Committee on Banking Supervision (2015). *Corporate governance principles for banks*. BIS.
- Hull, J. (2018). *Risk Management and Financial Institutions* (5.ª ed.). Wiley.
- Verificación local: revisa las exigencias de marco de riesgos, apetito y autoevaluación de capital de tu supervisor.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 11 · Tesorería y balance](11-tesoreria-y-balance.md) | [Parte 16](../README.md) · [Programa](../../../SYLLABUS.md) | [13 · Cumplimiento y prevención →](13-cumplimiento-y-prevencion.md) |
<!-- gen:footer:end -->
