<!-- meta
part: 16
class: 13
title: "Cumplimiento y prevención"
level: profesional
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 13 · Cumplimiento y prevención

> [← 12 · Marco de riesgos](12-marco-de-riesgos.md) · [Índice de la parte](../README.md) · [14 · Cuadro de mando del banco →](14-cuadro-de-mando-del-banco.md)

**Parte 16 — Proyecto Banco Virtual** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Construir el sistema de cumplimiento del Banco Austral. Su modelo —clientes sin historial, datos
alternativos, canal digital, corresponsales— concentra **exactamente los factores que más elevan el
riesgo de integridad**, y su sistema debe ser proporcionalmente más exigente sin excluir al segmento que
el banco existe para atender.

Esta clase construye el programa de cumplimiento del banco aplicando la Parte 12. Y plantea la tensión que un banco dirigido a segmentos desatendidos tiene que resolver de forma explícita: un programa demasiado estricto excluye precisamente a los clientes que el modelo de negocio quería servir.

## 📚 Objetivos

Al finalizar podrás:

1. **Evaluar** el riesgo de integridad del modelo de negocio.
2. **Diseñar** el proceso de conocimiento del cliente adaptado al segmento.
3. **Calibrar** el monitoreo transaccional para un banco nuevo.
4. **Construir** el programa de cumplimiento con sus recursos.
5. **Resolver** la tensión entre integridad e inclusión.

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

Los cuatro primeros términos son la evaluación y la diligencia; los cuatro siguientes, los corresponsales y la tensión con la inclusión. El **riesgo del agente** es el que un modelo con corresponsales no bancarios tiene que gestionar y que muchos proyectos olvidan.

| Concepto | Comprensión verificable |
|---|---|
| `evaluación de riesgo institucional` | Diagnóstico del riesgo de integridad del banco. |
| `debida diligencia` | Conocimiento del cliente proporcional a su riesgo. |
| `perfil transaccional` | Comportamiento esperado, base del monitoreo. |
| `corresponsal no bancario` | Comercio que opera por cuenta del banco. |
| `riesgo del agente` | El que introduce quien opera en nombre del banco. |
| `tasa de conversión` | Alertas que terminan en reporte. |
| `inclusión financiera` | Acceso a servicios de quien no lo tenía. |
| `de-risking` | Exclusión por costo de cumplimiento. |

## 🧠 Modelo mental

El modelo mental es un enfoque basado en riesgo aplicado de verdad: no se trata de aplicar el máximo control a todos sino de concentrar el esfuerzo donde el riesgo está. Un banco que aplica diligencia reforzada a todo su segmento no está cumpliendo mejor, está renunciando a su modelo de negocio.

```text
LA TENSIÓN CENTRAL DEL BANCO AUSTRAL

  SU RAZÓN DE SER
    dar acceso a 68 000 personas sin historial

  SU RIESGO DE INTEGRIDAD
    esas mismas personas son difíciles de verificar
    por las vías tradicionales
    y el canal digital sin presencia
    facilita la suplantación

  LA RESPUESTA INCORRECTA
    exigir documentación tradicional
    → excluye al segmento y destruye el modelo

  LA RESPUESTA CORRECTA
    verificación por medios alternativos
    con la misma o mayor fiabilidad
    y monitoreo proporcional al riesgo
```

## 📖 Desarrollo

### 1. Evaluación de riesgo institucional

La evaluación institucional identifica los riesgos propios del modelo de negocio. La tabla los recoge.

| Factor | Nivel | Fundamento |
|---|---|---|
| Clientes | Alto | Sin historial, difíciles de verificar por vías tradicionales |
| Productos | Medio | Créditos pequeños, cuentas de pagos; sin productos opacos |
| Canales | Alto | No presencial y corresponsales |
| Geografía | Medio | Un solo país, sin operaciones transfronterizas |
| Corresponsales | Alto | 12 000 puntos operando en nombre del banco |
| Efectivo | Alto | Depósitos y retiros en corresponsales |
| Nuevas tecnologías | Medio | Identidad digital, datos alternativos |

La combinación de esos factores da un nivel institucional que determina el
tamaño del programa.

```text
RIESGO INSTITUCIONAL: ALTO

  CONSECUENCIA
    · sistema de cumplimiento robusto desde el inicio
    · recursos proporcionales: 9 personas de 190 (4,7 %)
    · monitoreo desde la primera operación
    · auditoría del programa en el primer año
```

### 2. Conocimiento del cliente

La diligencia se diseña proporcional al riesgo del segmento. La tabla la recoge.

```text
IDENTIFICACIÓN Y VERIFICACIÓN — SEGMENTO PERSONAS

  IDENTIFICACIÓN
    documento oficial, capturado con lectura del chip
    o del código de seguridad

  VERIFICACIÓN
    · contraste biométrico con prueba de vida
    · contraste del documento con el registro oficial
    · verificación del dispositivo y su geolocalización
    · contraste del número de teléfono con su titularidad

  ¿ES MÁS O MENOS FIABLE QUE LA VERIFICACIÓN PRESENCIAL?
    MÁS: la verificación presencial depende del criterio
    de una persona que compara una foto
    la digital contrasta con registros oficiales
    y detecta documentos alterados

  → el canal digital no es una debilidad
    si la verificación se diseña bien
```

```text
CONOCIMIENTO — LA PARTE MÁS DIFÍCIL DEL SEGMENTO

  el perfil transaccional exige saber
  qué actividad tiene el cliente y qué flujos esperar

  FUENTES PARA EL SEGMENTO SIN HISTORIAL
    · declaración de actividad, con verificación
      contra el flujo observado
    · pagos de servicios: revelan estabilidad de domicilio
    · ingreso verificado por las fuentes alternativas
    · para independientes: ventas por medios de pago

  EL PERFIL SE CONSTRUYE Y SE AJUSTA
    perfil inicial declarado
    → a los 3 meses, ajustado con el comportamiento observado
    → alerta si la desviación es material
```

### 3. Corresponsales

Los corresponsales no bancarios amplían el alcance y añaden riesgo propio. La tabla lo recoge.

```text
12 000 CORRESPONSALES SON 12 000 PUNTOS
DONDE EL BANCO NO CONTROLA DIRECTAMENTE

  RIESGOS
    · el corresponsal fracciona operaciones
      para evitar umbrales
    · el corresponsal opera con identidad ajena
    · el corresponsal es usado por terceros
      para colocar efectivo
    · el corresponsal no aplica los controles

  CONTROLES
    · debida diligencia del corresponsal al contratar
    · límite por operación y por día por corresponsal
    · monitoreo del comportamiento de cada punto
    · identificación del cliente en cada operación
      sobre un umbral
    · visitas y verificación por muestreo
    · terminación por incumplimiento, con proceso
```

| Indicador del corresponsal | Alerta |
|---|---|
| Operaciones justo bajo el umbral | > 15 % de sus operaciones |
| Concentración en pocos clientes | > 40 % del volumen |
| Crecimiento atípico | > 3 veces la media de su categoría |
| Operaciones fuera de horario declarado | Cualquiera |
| Ratio depósitos/retiros atípico | Fuera del rango de su categoría |

**El monitoreo de corresponsales es tan importante como el de clientes.** Un corresponsal comprometido
introduce riesgo en miles de operaciones y su detección temprana depende de mirar su comportamiento
agregado, no las operaciones individuales.

### 4. Monitoreo transaccional

El monitoreo se calibra con el perfil transaccional del segmento. La tabla recoge los criterios.

```text
CALIBRACIÓN PARA UN BANCO NUEVO

  EL PROBLEMA
    sin historia, no hay línea base
    el perfil de cada cliente es una declaración
    → las reglas basadas en desviación del propio
      comportamiento no funcionan los primeros meses

  ESTRATEGIA POR FASES

    MESES 0-6
      reglas de umbral y de patrón
      revisión manual de una proporción mayor
      tasa de conversión esperada: baja (1-2 %)
      recursos: 4 analistas

    MESES 6-18
      se incorpora la desviación del perfil propio
      recalibración mensual
      tasa de conversión objetivo: 3-5 %

    MESES 18+
      análisis de red y comportamiento
      tasa de conversión objetivo: 5-8 %
```

| Regla | Fase | Umbral inicial |
|---|---|---|
| Depósitos en efectivo acumulados | 0 | Según norma local |
| Fraccionamiento (varias operaciones bajo umbral) | 0 | 3 en 5 días |
| Depósito seguido de retiro inmediato | 0 | > 80 % en 48 h |
| Actividad incoherente con el perfil declarado | 6 | > 4 veces lo declarado |
| Desviación del comportamiento propio | 6 | > 5 desviaciones |
| Red de cuentas relacionadas | 18 | Análisis de grafo |
| Comportamiento del corresponsal | 0 | Ver tabla anterior |

### 5. Programa de cumplimiento

El programa reúne todo con sus responsables y sus pruebas. La tabla lo recoge.

```text
RECURSOS
  oficial de cumplimiento                      1
  analistas de monitoreo                       4
  debida diligencia reforzada y expedientes    2
  corresponsales y agentes                     1
  normativo y reportes                         1
  TOTAL: 9 personas

  costo: 9 × 24,0 = 216 anuales
  más sistemas: 640 anuales
  TOTAL: 856 anuales
  sobre margen bruto de 55 942: 1,53 %
```

```text
INVENTARIO DE OBLIGACIONES
  · identificación y verificación
  · beneficiario final
  · personas expuestas políticamente
  · monitoreo y reporte de operaciones sospechosas
  · cribado de sanciones
  · conservación de registros
  · formación anual del personal
  · auditoría independiente del programa
  · reportes periódicos a la autoridad
  · protección de datos personales

  cada una con: proceso, control, evidencia,
  responsable y frecuencia de verificación
```

## 🧮 Ejemplo guiado

El ejemplo diseña la diligencia proporcional para el segmento del Banco Austral. Conviene medir la tasa de conversión resultante: un diseño que excluye al segmento objetivo no sirve.

**Situación.** Resolver la tensión entre integridad e inclusión en un caso concreto.

```text
EL CASO
  8 400 solicitantes del segmento personas
  no pueden completar la verificación estándar:

    sin documento con chip legible:            3 200
    sin teléfono a su nombre:                  2 800
    sin pagos de servicios a su nombre:        1 900
    con domicilio no verificable:                500

  representan el 12,4 % de los solicitantes
  y son, por definición, los más excluidos
```

**Paso 1 — evalúa la respuesta por defecto.**

```text
RECHAZARLOS
  · cumple con la norma
  · elimina el riesgo
  · excluye a 8 400 personas
  · contradice la razón de ser del banco
  · y es exactamente el de-risking que el GAFI
    ha señalado como respuesta incorrecta
    (Parte 12, clase 3)
```

**Paso 2 — analiza cada caso por separado.**

```text
SIN DOCUMENTO CON CHIP LEGIBLE (3 200)
  causa: documento antiguo o deteriorado
  ¿el riesgo es mayor? no necesariamente
  ALTERNATIVA
    verificación biométrica contra el registro oficial
    de identidad, si la jurisdicción lo permite
    + verificación de datos con el registro civil
  fiabilidad: equivalente o superior
  → VIABLE, con costo adicional de 0,0012 por verificación

SIN TELÉFONO A SU NOMBRE (2 800)
  causa: teléfono prepago o familiar
  ¿el riesgo es mayor? sí: dificulta la trazabilidad
    y facilita el uso por terceros
  ALTERNATIVA
    verificación presencial en corresponsal
    con captura biométrica
    + límites operativos menores el primer año
  → VIABLE, con diligencia reforzada

SIN PAGOS DE SERVICIOS (1 900)
  causa: vive en casa de terceros o alquiler informal
  ¿el riesgo es mayor? no para integridad;
    sí para la evaluación de crédito
  ALTERNATIVA
    verificación de domicilio por otros medios
    (declaración de un tercero verificable,
     geolocalización recurrente del dispositivo)
  → VIABLE para la cuenta; el crédito requiere
    otras fuentes de ingreso verificado

DOMICILIO NO VERIFICABLE (500)
  causa: situación de calle, movilidad, zona sin nomenclatura
  ¿el riesgo es mayor? sí
  ALTERNATIVA
    cuenta con límites reducidos y monitoreo intensificado
    domicilio de referencia (institución, empleador)
  → VIABLE con restricciones
```

**Paso 3 — diseña el proceso de excepción.**

```text
PROCESO DE VERIFICACIÓN ALTERNATIVA

  1. el solicitante que no completa la verificación estándar
     recibe la opción de la vía alternativa,
     con explicación de qué se requiere
     → NO se le rechaza sin ofrecerla

  2. la vía alternativa exige:
     · al menos dos fuentes independientes de verificación
     · verificación biométrica en todos los casos
     · aprobación del área de cumplimiento, no automática

  3. el cliente verificado por vía alternativa:
     · se clasifica en riesgo medio o alto
     · opera con límites reducidos los primeros 6 meses
     · su monitoreo es intensificado
     · a los 6 meses, si su comportamiento es coherente,
       se normaliza su clasificación

  4. si no se puede verificar por ninguna vía:
     · se rechaza, con explicación
     · se le indica qué necesitaría aportar
```

**Paso 4 — cuantifica el costo.**

```text
COSTO ADICIONAL
  verificación biométrica contra registro oficial
    3 200 × 0,0012 = 3,8
  verificación presencial en corresponsal
    2 800 × 0,0032 = 9,0
  revisión manual de cumplimiento
    8 400 × 18 minutos / 60 / 1 560 = 1,6 personas = 38,4
  monitoreo intensificado 6 meses
    8 400 × 0,0008 = 6,7
  TOTAL: 57,9 anuales
```

**Paso 5 — cuantifica el beneficio.**

```text
CLIENTES INCORPORADOS
  de los 8 400, se verifican por vía alternativa: 7 100
  se rechazan: 1 300

  de los 7 100, con crédito: 62 % = 4 402
  monto medio: 2,80
  cartera adicional: 12 326
  margen: 12 326 × 15,62 % = 1 925
  menos costo de riesgo (PD algo mayor: 8,1 %)
    12 326 × 8,1 % × 69,2 % = 691
  MARGEN NETO: 1 234 anuales

  frente a 57,9 de costo adicional
  RELACIÓN: 21 a 1
```

**Paso 6 — verifica que el riesgo de integridad esté controlado.**

```text
LOS 7 100 CLIENTES DE VÍA ALTERNATIVA
  · clasificados en riesgo medio o alto
  · con límites reducidos 6 meses
  · con monitoreo intensificado

  ¿QUÉ PROPORCIÓN DE ALERTAS GENERARÍAN?
    tasa de alerta esperada: 4,2 % anual
    frente a 1,8 % de la base general
    alertas: 298 al año
    carga adicional: 0,3 analistas

  ¿Y DE REPORTES?
    tasa de conversión esperada: 6 %
    reportes: 18 al año

  ¿ES ACEPTABLE?
    sí: 18 reportes de 7 100 clientes es 0,25 %
    y su detección es precisamente la función
    del sistema
```

**Paso 7 — evalúa el riesgo residual.**

```text
LO QUE QUEDA SIN RESOLVER

  1 300 personas rechazadas por no poder verificarse
  por ninguna vía

  ¿QUÉ PASA CON ELLAS?
    · siguen sin acceso al sistema financiero formal
    · el banco no puede resolverlo con su sistema

  LO QUE SÍ PUEDE HACER
    · documentar los casos y sus causas
    · reportar el patrón al supervisor y al gremio
    · participar en las iniciativas de identidad
      que resuelvan la causa raíz

  LO QUE NO DEBE HACER
    · relajar la verificación para incluirlas
      → eso no es inclusión: es crear una vía
        de entrada para el uso indebido
```

**Paso 8 — establece la métrica de la tensión.**

```text
EL PROGRAMA REPORTA MENSUALMENTE, JUNTAS:

  MÉTRICAS DE INTEGRIDAD
    alertas generadas y su conversión
    reportes de operación sospechosa
    clientes de riesgo alto y su proporción
    corresponsales con indicadores atípicos
    hallazgos de la auditoría del programa

  MÉTRICAS DE INCLUSIÓN
    solicitantes que no completan la verificación estándar
    de ellos, verificados por vía alternativa
    rechazados por imposibilidad de verificación
    tiempo medio de la vía alternativa
    clientes de vía alternativa normalizados a los 6 meses

  REPORTAR SOLO LAS PRIMERAS
  PRODUCE EXCLUSIÓN SIN QUE NADIE LA VEA
```

**Interpreta:** el caso se resolvió **cliente por cliente y causa por causa**, y el resultado fue incluir
a 7 100 de 8 400 con un costo de 57,9 y un margen neto de 1 234. Las 1 300 personas restantes siguen
excluidas y el banco lo documenta en lugar de resolverlo relajando controles. Esa distinción —entre
buscar una vía alternativa fiable y bajar el estándar— es la que separa la inclusión responsable de la
creación de una puerta trasera.

## 🏦 Del cliente al banco

El cliente sin documentación completa no accede y el banco cumple una obligación que puede excluirlo. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Mi documento es viejo y no lo leen» | Vía de verificación alternativa | 16, clase 13 |
| «Me pidieron ir a un corresponsal» | Verificación presencial con biometría | 12, clase 4 |
| «Mis límites son bajos al inicio» | Diligencia reforzada temporal | 12, clase 3 |
| «No pude abrir cuenta en ningún banco» | Causa raíz que un banco no resuelve solo | 12, clase 3 |
| «El almacén me atiende como banco» | Corresponsal con sus controles | 10, clase 15 |

## 🧪 Práctica

El laboratorio pide diseñar el programa y medir su efecto sobre la conversión del segmento. El equilibrio con su justificación es lo que se evalúa.

En `labs/lab-06.md`, sección de cumplimiento:

1. Realiza la evaluación de riesgo institucional con sus siete factores.
2. Diseña el proceso de verificación con su vía alternativa.
3. Calibra el monitoreo por fases con sus reglas y umbrales.
4. Construye las métricas conjuntas de integridad e inclusión.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen programas que excluyen o que no protegen. La causa es no haber aplicado el enfoque basado en riesgo.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se rechaza a quien no verifica por vía estándar | De-risking | Ofrece vía alternativa fiable. |
| Se relaja el estándar para incluir | Crea puerta trasera | Vía alternativa, no estándar menor. |
| Corresponsales sin monitoreo agregado | Riesgo del agente | Mide su comportamiento. |
| Reglas de desviación en un banco nuevo | Sin línea base | Calibra por fases. |
| Solo se reportan métricas de integridad | La exclusión no se ve | Repórtalas juntas. |
| Recursos de cumplimiento proporcionales al tamaño | El riesgo del modelo es alto | Proporcionales al riesgo. |

## ❓ Preguntas de comprobación

1. ¿Por qué la verificación digital puede ser más fiable que la presencial?
2. ¿Qué distingue una vía alternativa de un estándar más bajo?
3. ¿Por qué el monitoreo de corresponsales requiere mirar su comportamiento agregado?
4. ¿Por qué las reglas de desviación no funcionan en un banco nuevo?
5. ¿Qué debe hacer el banco con quienes no puede verificar por ninguna vía?

## 📥 Entregable

Guarda en `portfolio/parte-16/clase-13/`:

- la evaluación de riesgo institucional con sus factores;
- el proceso de verificación con su vía alternativa y su costo-beneficio;
- la calibración del monitoreo por fases;
- las métricas conjuntas de integridad e inclusión.

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

- Financial Action Task Force (2012-2025). *The FATF Recommendations*. FATF.
- Financial Action Task Force (2021). *Guidance on Digital Identity*. FATF. <https://www.fatf-gafi.org/en/publications/Financialinclusionandnpoissues/Digital-identity-guidance.html>
- Financial Action Task Force (2017). *Anti-money laundering and terrorist financing measures and financial inclusion*. FATF.
- Basel Committee on Banking Supervision (2020). *Sound management of risks related to money laundering and financing of terrorism*. BIS.
- World Bank (2018). *De-risking in the Financial Sector*. World Bank Group.
- Verificación local: revisa los medios de verificación de identidad aceptados en tu país, el régimen de corresponsales y los umbrales de reporte.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 12 · Marco de riesgos](12-marco-de-riesgos.md) | [Parte 16](../README.md) · [Programa](../../../SYLLABUS.md) | [14 · Cuadro de mando del banco →](14-cuadro-de-mando-del-banco.md) |
<!-- gen:footer:end -->
