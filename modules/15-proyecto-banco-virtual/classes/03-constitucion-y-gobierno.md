---
part: 16
class: 3
title: "Constitución y gobierno"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 03 · Constitución y gobierno

> [← 02 · Modelo de negocio del banco](02-modelo-de-negocio-del-banco.md) · [Índice de la parte](../README.md) · [04 · Arquitectura de datos y sistemas →](04-arquitectura-de-datos-y-sistemas.md)

**Parte 16 — Proyecto Banco Virtual** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Constituir el Banco Austral: obtener la licencia, definir su estructura de gobierno y establecer el
marco normativo interno. Un banco no empieza a operar cuando abre: **empieza cuando el supervisor
verifica que sus accionistas, su administración y sus controles son idóneos**.

El modelo de negocio de la clase anterior necesita una entidad que lo ejecute. Esta la constituye, y aplica la Parte 12: un banco no se crea, se autoriza, y el expediente de licenciamiento exige demostrar cosas concretas antes de operar con dinero de nadie.

## 📚 Objetivos

Al finalizar podrás:

1. **Preparar** los requisitos de una solicitud de licencia bancaria.
2. **Diseñar** la estructura de gobierno y sus comités.
3. **Definir** el marco de atribuciones y de delegación.
4. **Establecer** las políticas internas obligatorias.
5. **Verificar** la idoneidad de los actores clave.

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

Los cuatro primeros términos son el licenciamiento y sus requisitos; los cuatro siguientes, la estructura interna. La **atribución** es la pieza operativa: quién puede aprobar qué y hasta qué importe, escrito y con su vía de excepción.

| Concepto | Comprensión verificable |
|---|---|
| `licencia bancaria` | Autorización para captar del público e intermediar. |
| `accionista significativo` | El que supera el umbral que exige aprobación. |
| `idoneidad` | Aptitud, honorabilidad y experiencia exigidas. |
| `plan de negocio de licenciamiento` | Documento que sustenta la viabilidad ante el supervisor. |
| `atribución` | Facultad de decidir hasta un límite definido. |
| `delegación` | Traslado de una atribución con responsabilidad conservada. |
| `política interna` | Norma propia que desarrolla una obligación. |
| `estructura organizativa` | Diseño de áreas, dependencias y separaciones. |

## 🧠 Modelo mental

El modelo mental es una estructura de atribuciones: cada decisión tiene un nivel que la puede tomar, y ese nivel está escrito antes de que la decisión haga falta. Un banco donde las atribuciones se deciden caso a caso no pasa una revisión supervisora.

```text
EL SUPERVISOR NO AUTORIZA UN BANCO PORQUE TENGA CAPITAL
LO AUTORIZA PORQUE CUMPLE CUATRO CONDICIONES

  1. ACCIONISTAS IDÓNEOS
     con capital de origen verificado y capacidad
     de aportar más si hace falta
  2. ADMINISTRACIÓN COMPETENTE
     con experiencia demostrable en lo que se propone
  3. PLAN VIABLE
     que no dependa de supuestos heroicos
  4. CONTROLES DESDE EL DÍA UNO
     riesgos, cumplimiento y auditoría operando
     antes de la primera operación

EL ERROR DEL BANCO NUEVO
  construir el negocio primero
  y los controles cuando haya volumen
  → el supervisor no lo autoriza, y con razón
```

## 📖 Desarrollo

### 1. Requisitos de licenciamiento

El licenciamiento exige acreditar capital, idoneidad y plan de negocio. La tabla recoge los requisitos y su forma de acreditación.

| Requisito | Contenido |
|---|---|
| Capital mínimo | El que exige la norma, íntegramente pagado |
| Origen de los fondos | Verificado, con trazabilidad |
| Accionistas significativos | Idoneidad, solvencia, compromiso de apoyo |
| Administración | Idoneidad y experiencia de directores y gerentes |
| Plan de negocio | 3 a 5 años, con proyecciones y escenarios |
| Estructura organizativa | Áreas, dependencias y separación de funciones |
| Políticas y manuales | Los obligatorios, aprobados por el directorio |
| Sistemas | Núcleo, contabilidad, riesgos, cumplimiento |
| Continuidad operacional | Plan probado |
| Prevención de lavado | Sistema completo antes de operar |

```text
EL COMPROMISO DE APOYO DEL ACCIONISTA
  la mayoría de las jurisdicciones exige que el accionista
  significativo se comprometa a aportar capital
  si el banco lo requiere

  es la contrapartida de la licencia:
  el privilegio de captar del público
  viene con la obligación de sostener la institución
```

### 2. Estructura de gobierno del Banco Austral

La estructura se define con órganos, composiciones y frecuencias. La tabla la recoge.

```text
JUNTA DE ACCIONISTAS
      ↓
DIRECTORIO — 7 miembros
  2 ejecutivos (gerente general y gerente de finanzas)
  2 vinculados al accionista controlador
  3 independientes
      ↓
COMITÉS DEL DIRECTORIO
  AUDITORÍA         3 miembros, 2 independientes
  RIESGOS           3 miembros, 2 independientes
  NOMBRAMIENTOS Y REMUNERACIONES
                    3 miembros, 2 independientes
      ↓
GERENCIA GENERAL
  ├── gerencia comercial
  ├── gerencia de operaciones y tecnología
  ├── gerencia de finanzas
  ├── GERENCIA DE RIESGOS      → acceso directo al comité
  ├── GERENCIA DE CUMPLIMIENTO → acceso directo al comité
  └── AUDITORÍA INTERNA        → reporta al comité de auditoría
```

```text
COMPETENCIAS EXIGIDAS EN EL DIRECTORIO
  · banca minorista y de pequeña empresa
  · riesgo de crédito y modelos
  · tecnología, datos y ciberseguridad
  · contabilidad y auditoría
  · cumplimiento y regulación

  LA TERCERA ES LA QUE MÁS FALTA (Parte 15, clase 9)
  y en un banco cuyo modelo es digital
  su ausencia sería una deficiencia grave
```

### 3. Atribuciones

Las atribuciones se definen por tipo de decisión y por importe. La tabla las recoge.

```text
MATRIZ DE ATRIBUCIONES DE CRÉDITO

  nivel                        límite por operación   límite por deudor
  analista                              0,8                  1,5
  jefe de riesgos de personas           3,0                  5,0
  gerente de riesgos                   20,0                 35,0
  comité de crédito                    80,0                140,0
  directorio                        sin límite           sin límite
                                    (dentro del apetito)

  LÍMITE NORMATIVO POR DEUDOR
    5 % del patrimonio efectivo = 2 100
    → ninguna atribución puede superarlo
```

| Materia | Quién decide |
|---|---|
| Política de crédito | Directorio, propuesta del comité de riesgos |
| Excepciones a política | Comité de crédito, con registro (Parte 12, clase 14) |
| Precios de productos | Comité de gestión, dentro del marco del directorio |
| Nuevos productos | Comité de productos, con veto de riesgos y cumplimiento |
| Apetito de riesgo | Directorio |
| Límites operativos | Comité de activos y pasivos |
| Gasto sobre un umbral | Gerente general; sobre otro, directorio |

### 4. Políticas obligatorias

Hay políticas que un banco debe tener aprobadas antes de operar. La tabla las recoge.

```text
POLÍTICAS QUE DEBEN EXISTIR ANTES DE OPERAR

  DE NEGOCIO
    política de crédito
    política de precios
    política de productos y su gobierno

  DE RIESGO
    marco de gestión integral de riesgos
    apetito de riesgo
    política de provisiones
    política de gestión de activos y pasivos
    política de continuidad operacional

  DE CUMPLIMIENTO
    manual de prevención de lavado
    política de conozca a su cliente
    política de sanciones y cribado
    código de conducta
    política de conflictos de interés
    política de protección de datos

  DE GOBIERNO
    reglamento del directorio y de cada comité
    política de remuneraciones
    política de operaciones con partes relacionadas
    política de canal de denuncia
```

```text
CADA POLÍTICA DEBE TENER
  · aprobación del órgano competente y fecha
  · responsable de su aplicación
  · periodicidad de revisión
  · indicadores de cumplimiento
  · procedimiento asociado que la operacionaliza

UNA POLÍTICA SIN PROCEDIMIENTO ES UNA DECLARACIÓN
```

### 5. Separación de funciones

La separación de funciones se diseña desde el organigrama y no se parchea después. La tabla la recoge.

```text
SEPARACIONES OBLIGATORIAS

  quien ORIGINA no puede APROBAR
  quien APRUEBA no puede DESEMBOLSAR
  quien DESEMBOLSA no puede REGISTRAR
  quien REGISTRA no puede CONCILIAR
  quien OPERA no puede VALORAR su propia posición
  quien CONTROLA no puede depender de quien controla

EN UN BANCO PEQUEÑO ESTO ES DIFÍCIL
  con 60 personas, las separaciones completas
  exigen controles compensatorios:
    · revisión por muestreo de un tercero
    · registro y trazabilidad de toda acción
    · alertas automáticas sobre excepciones
    · rotación de funciones
```

## 🧮 Ejemplo guiado

El ejemplo construye la matriz de atribuciones del Banco Austral. Conviene comprobar que ninguna decisión queda sin nivel asignado: los huecos son los que producen excepciones informales.

**Situación.** Preparar la solicitud de licencia del Banco Austral.

```text
ELEMENTOS DISPONIBLES
  capital comprometido: 42 000
  accionistas: 3
    A: 48 %, grupo empresarial local
    B: 32 %, fondo de inversión regional
    C: 20 %, equipo fundador
  plan de negocio: el de las clases 1 y 2
  brecha pendiente: 1,31 puntos de rentabilidad
    frente al costo del capital
```

**Paso 1 — verifica el capital mínimo.**

```text
CAPITAL MÍNIMO NORMATIVO (dato del proyecto): 38 000
CAPITAL COMPROMETIDO: 42 000  ✓

  holgura: 4 000  (10,5 %)

  ¿ES SUFICIENTE LA HOLGURA?
    el plan proyecta pérdida de 2 400 en el año 1
    capital al cierre del año 1: 39 600
    sobre el mínimo: 1 600  (4,2 %)

  → holgura muy ajustada en el año 1
  → el supervisor lo observará
```

**Paso 2 — evalúa las opciones.**

```text
  a) aumentar el capital inicial a 46 000
     los accionistas deben comprometer 4 000 más
  b) reducir la pérdida del año 1
     con menor inversión inicial o menor crecimiento
  c) compromiso formal de aporte adicional
     de los accionistas, verificable

  DECISIÓN: (a) y (c) combinadas
    capital inicial: 46 000
    compromiso de aporte adicional hasta 12 000,
    con verificación de la capacidad de los accionistas

  EFECTO EN EL PLAN
    capacidad de activos ponderados al 14 %: 328 571
    cartera máxima: 421 245  → cubre el plan de 410 940
```

**Paso 3 — evalúa la idoneidad de los accionistas.**

```text
ACCIONISTA A — grupo empresarial local, 48 %
  · es accionista significativo: requiere aprobación
  · origen de fondos: recursos propios del grupo,
    con estados auditados
  · SEÑAL DE ATENCIÓN: el grupo tiene empresas
    que serían clientes potenciales del banco
    → operaciones con partes relacionadas (Parte 15, clase 9)
    → límite específico y aprobación reforzada

ACCIONISTA B — fondo de inversión regional, 32 %
  · accionista significativo
  · origen de fondos: verificable
  · SEÑAL DE ATENCIÓN: los fondos tienen horizonte
    de salida (5-7 años)
    → ¿quién aportaría capital en el año 6?
    → el compromiso de apoyo debe considerarlo

ACCIONISTA C — equipo fundador, 20 %
  · no supera el umbral de significativo
  · su participación alinea incentivos  ✓
```

**Paso 4 — resuelve las señales de atención.**

```text
ACCIONISTA A — PARTES RELACIONADAS
  política específica:
    · límite agregado a partes relacionadas: 10 % del patrimonio
      efectivo (más estricto que el normativo)
    · condiciones no más favorables que las de mercado
    · aprobación del directorio con abstención
      de los directores vinculados
    · revelación en los estados financieros
    · revisión anual por auditoría interna

ACCIONISTA B — HORIZONTE DE SALIDA
  · el compromiso de apoyo se estructura como
    obligación transferible al adquirente de la participación
  · cláusula de aprobación previa del supervisor
    para cualquier cambio de control
  · el plan de capital considera el año 6
    sin contar con aportes de B
```

**Paso 5 — verifica la idoneidad de la administración.**

```text
POSICIONES CLAVE Y SU EXIGENCIA

  gerente general
    experiencia en dirección bancaria: 12 años  ✓
  gerente de riesgos
    experiencia en riesgo de crédito minorista: 9 años  ✓
    INDEPENDENCIA: no puede reportar al gerente comercial  ✓
  gerente de cumplimiento
    experiencia en prevención de lavado: 7 años  ✓
  auditor interno
    reporta al comité de auditoría  ✓
  gerente de tecnología
    experiencia en banca digital: 6 años  ✓

  DIRECTORES INDEPENDIENTES
    1: ex supervisor, experiencia regulatoria  ✓
    2: experiencia en contabilidad y auditoría  ✓
    3: experiencia en tecnología y datos  ✓

  → la competencia tecnológica está cubierta
    en el directorio, que es lo que el modelo exige
```

**Paso 6 — dimensiona la estructura y verifica el compromiso de eficiencia.**

```text
PLANTILLA PROYECTADA AL AÑO 3
  comercial y atención             142
  operaciones y tecnología          68
  riesgos                           14
  cumplimiento                       9
  auditoría interna                  5
  finanzas y contabilidad           12
  administración                    10
  TOTAL                            260

  costo medio por persona: 24,0
  costo de personal: 6 240
  otros gastos operativos: 28 559  (proyección)
  GASTOS TOTALES: 34 799

  compromiso de eficiencia: 55 %
  margen bruto proyectado: 63 270
  índice: 34 799 / 63 270 = 55,0 %  ✓
```

**Paso 7 — verifica la proporción de las funciones de control.**

```text
FUNCIONES DE CONTROL: 14 + 9 + 5 = 28 personas
  sobre 260: 10,8 %

  referencia del sector para un banco pequeño:
  entre 8 % y 14 %
  → dentro del rango  ✓

  Y UNA VERIFICACIÓN ADICIONAL
    ¿el presupuesto de las funciones de control
     lo aprueba alguien que ellas controlan?
    → no: lo aprueba el comité correspondiente
      del directorio (Parte 12, clase 16)  ✓
```

**Paso 8 — arma el expediente de licenciamiento.**

```text
CONTENIDO DE LA SOLICITUD

  1. capital: 46 000, con origen verificado de cada accionista
  2. accionistas: expedientes de idoneidad y compromisos
     de apoyo, incluida la cláusula de transferencia
  3. administración: expedientes de idoneidad de 7 directores
     y 6 gerentes
  4. plan de negocio a 5 años, con:
     · proyecciones base y adversa
     · plan de capital con la brecha de 1,31 puntos
       declarada y su plan de cierre
     · supuestos críticos, con su sensibilidad
  5. estructura organizativa con separaciones y controles
     compensatorios
  6. las 18 políticas obligatorias, aprobadas
  7. descripción de sistemas y su plan de implantación
  8. plan de continuidad operacional
  9. sistema de prevención de lavado, operativo antes
     de la primera operación

  LO QUE SE DECLARA EXPLÍCITAMENTE
    · la brecha de rentabilidad de 1,31 puntos
      y el plan para cerrarla
    · la exposición potencial a partes relacionadas
      y su límite autoimpuesto
    · el horizonte del accionista B y su tratamiento

  DECLARARLO ES MEJOR QUE QUE LO ENCUENTREN
  (Parte 12, clase 13)
```

**Interpreta:** el expediente declara **tres debilidades que nadie obligaba a declarar**: la brecha de
rentabilidad, la exposición potencial a partes relacionadas y el horizonte de salida de un accionista.
Declararlas con su tratamiento convierte tres hallazgos futuros en tres decisiones documentadas, y es la
diferencia entre una licencia que se otorga con condiciones y una que se otorga con reservas.

## 🏦 Del cliente al banco

El cliente confía en una entidad autorizada y el banco acredita ante el supervisor que merece esa autorización. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «¿Este banco es seguro?» | Licencia, capital y controles verificados | 12, clase 1 |
| «Es un banco nuevo» | Holgura de capital ajustada al inicio | 16, clase 3 |
| «Sus dueños tienen otras empresas» | Límite a partes relacionadas | 15, clase 9 |
| «Tiene poco personal» | Controles compensatorios por escala | 16, clase 3 |
| «Me atendieron con rapidez» | Atribuciones bien definidas | 16, clase 7 |

## 🧪 Práctica

El laboratorio pide construir la estructura de gobierno con sus atribuciones. Las decisiones sin nivel asignado son lo que se busca.

En `labs/lab-02.md`:

1. Verifica el capital mínimo y la holgura en el escenario del año 1.
2. Diseña la estructura de gobierno con comités y competencias exigidas.
3. Construye la matriz de atribuciones de crédito con el límite normativo.
4. Arma el expediente de licenciamiento con lo que se declara explícitamente.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen problemas de gobierno en la fase de licenciamiento. Las causas son atribuciones incompletas y separación de funciones no diseñada.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Controles después del volumen | El supervisor no autoriza | Operativos desde el día uno. |
| Holgura de capital ajustada | Pérdida del año 1 | Dimensiona con el escenario, no con el inicio. |
| Competencia tecnológica ausente | El modelo es digital | Es una deficiencia grave. |
| Política sin procedimiento | Es una declaración | Cada política con su procedimiento. |
| Separaciones imposibles por escala | Banco pequeño | Controles compensatorios documentados. |
| Debilidades no declaradas | Se convierten en hallazgos | Declararlas con su tratamiento. |

## ❓ Preguntas de comprobación

1. ¿Cuáles son las cuatro condiciones que verifica el supervisor al licenciar?
2. ¿Por qué el compromiso de apoyo del accionista es la contrapartida de la licencia?
3. ¿Qué separaciones de funciones son obligatorias y qué hacer cuando la escala lo impide?
4. ¿Por qué el horizonte de salida de un accionista financiero es una señal de atención?
5. ¿Por qué conviene declarar las debilidades en el expediente?

## 📥 Entregable

Guarda en `portfolio/parte-16/clase-03/`:

- la verificación de capital mínimo con el escenario del año 1;
- la estructura de gobierno con comités, competencias y separaciones;
- la matriz de atribuciones con su límite normativo;
- el expediente de licenciamiento con las declaraciones explícitas.

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

- Basel Committee on Banking Supervision (2012). *Core Principles for Effective Banking Supervision*, principios 4 a 6 sobre licenciamiento. BIS. <https://www.bis.org/publ/bcbs230.htm>
- Basel Committee on Banking Supervision (2015). *Corporate governance principles for banks*. BIS.
- Basel Committee on Banking Supervision (2018). *Sound Practices: Implications of fintech developments for banks and bank supervisors*, licenciamiento de bancos digitales. BIS.
- European Banking Authority (2021). *Guidelines on internal governance* y guías de idoneidad. EBA.
- Institute of Internal Auditors (2020). *The IIA's Three Lines Model*. IIA.
- Verificación local: revisa los requisitos de licenciamiento bancario de tu país, el capital mínimo, el umbral de accionista significativo y las políticas obligatorias.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 02 · Modelo de negocio del banco](02-modelo-de-negocio-del-banco.md) | [Parte 16](../README.md) · [Programa](../../../SYLLABUS.md) | [04 · Arquitectura de datos y sistemas →](04-arquitectura-de-datos-y-sistemas.md) |
<!-- gen:footer:end -->
