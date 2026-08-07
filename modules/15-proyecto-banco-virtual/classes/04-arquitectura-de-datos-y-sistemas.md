---
part: 16
class: 4
title: "Arquitectura de datos y sistemas"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 04 · Arquitectura de datos y sistemas

> [← 03 · Constitución y gobierno](03-constitucion-y-gobierno.md) · [Índice de la parte](../README.md) · [05 · Catálogo de productos →](05-catalogo-de-productos.md)

**Parte 16 — Proyecto Banco Virtual** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Diseñar la arquitectura sobre la que operará el Banco Austral y el modelo de datos que sostendrá todas
sus decisiones. Es la clase que determina si el banco podrá **medir lo que necesita medir**, y su
resultado condiciona las trece clases siguientes.

## 📚 Objetivos

Al finalizar podrás:

1. **Diseñar** la arquitectura por capas de un banco digital.
2. **Decidir** qué construir y qué comprar con el marco de capacidades.
3. **Construir** el modelo de datos maestro y sus definiciones.
4. **Establecer** el gobierno de datos desde el inicio.
5. **Verificar** que la arquitectura soporte los indicadores necesarios.

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
| `arquitectura por capas` | Separación entre registro, negocio, canales y análisis. |
| `dato maestro` | Información de referencia compartida por todo el banco. |
| `identificador único` | Clave que identifica a una entidad en todo el sistema. |
| `evento` | Registro inmutable de algo que ocurrió. |
| `capa semántica` | Definiciones únicas de los conceptos de negocio. |
| `linaje` | Recorrido del dato desde su origen hasta su uso. |
| `desacoplamiento` | Que un componente cambie sin obligar a cambiar otros. |
| `diccionario de datos` | Definición documentada de cada campo. |

## 🧠 Modelo mental

```text
UN BANCO NUEVO TIENE UNA VENTAJA IRREPETIBLE

  puede diseñar sus datos ANTES de generarlos

  un banco establecido gasta años y millones
  en consolidar información que se creó
  sin un modelo común (Parte 14, clase 4)

  el Banco Austral no tiene ese problema
  Y PUEDE CREARLO SI DISEÑA MAL

LA DECISIÓN MÁS IRREVERSIBLE DEL PROYECTO
  el modelo de datos: cambiarlo después
  exige migrar todo lo que ya se registró
```

## 📖 Desarrollo

### 1. Arquitectura por capas

```text
CANALES
  aplicación móvil · web · corresponsales · centro de contacto
      ↕ interfaces
CAPA DE NEGOCIO
  motor de decisión · precios · productos · límites
  originación · cobranza · alertas
      ↕
CAPA DE REGISTRO (núcleo)
  cuentas · saldos · movimientos · contabilidad
      ↕
CAPA DE DATOS
  eventos · almacén analítico · capa semántica
      ↕
CAPA DE CONTROL
  riesgos · cumplimiento · reportes regulatorios
```

```text
EL PRINCIPIO DE DISEÑO
  el NÚCLEO solo registra
  las REGLAS DE NEGOCIO viven fuera de él

  así, cambiar un precio, una política de crédito
  o un límite NO exige tocar el núcleo
  → el problema de la Parte 14, clase 13
    se evita por diseño
```

### 2. Construir o comprar

| Capacidad | Decisión | Fundamento |
|---|---|---|
| Núcleo de registro | Comprar | Infraestructura; hay soluciones maduras |
| Contabilidad | Comprar | Estandarizada |
| Motor de decisión | Comprar la herramienta | Configuración y políticas propias (Parte 14, clase 14) |
| Modelos de riesgo | Construir | Capacidad diferenciadora |
| Aplicación móvil | Construir | Define la relación con el cliente |
| Verificación de identidad | Comprar | Especializado |
| Antifraude | Comprar el motor, calibrar propio | Intermedia |
| Prevención de lavado | Comprar el motor, calibrar propio | Intermedia |
| Almacén analítico | Comprar la infraestructura | Infraestructura |
| Capa semántica | Construir | Son las definiciones del negocio |
| Reportes regulatorios | Comprar o construir según el mercado | Depende de la estandarización |

```text
LA CONSECUENCIA PARA EL PRESUPUESTO
  inversión inicial estimada
    núcleo y contabilidad (nube, por uso)     1 200
    motor de decisión                           980
    verificación de identidad (por uso)           0
    antifraude y prevención de lavado           640
    almacén y plataforma de datos               420
    desarrollo de aplicación y capa de negocio 2 800
    integración                                 900
    TOTAL INICIAL                             6 940
  operación anual: 1 840
```

### 3. Modelo de datos maestro

```text
ENTIDADES MAESTRAS Y SU IDENTIFICADOR

  PERSONA          identificador interno único, permanente
                   nunca el documento de identidad como clave
  EMPRESA          identificador interno único
  RELACIÓN         vínculo entre persona y empresa,
                   con su tipo y su vigencia
  PRODUCTO         catálogo, con versión
  CONTRATO         instancia de un producto para un cliente
  CUENTA           registro de saldo
  MOVIMIENTO       evento sobre una cuenta
  SOLICITUD        petición con su decisión y su fundamento
  GARANTÍA         bien afecto, con su valoración y su fecha
```

```text
POR QUÉ EL DOCUMENTO DE IDENTIDAD NO PUEDE SER LA CLAVE
  · cambia (renovación, corrección, cambio de nacionalidad)
  · se repite entre jurisdicciones
  · es dato personal sensible replicado en cada tabla
  · impide la seudonimización (Parte 12, clase 10)

  un identificador interno resuelve las cuatro cosas
```

| Principio de diseño | Consecuencia |
|---|---|
| Un identificador por entidad | Visión única del cliente desde el día uno |
| Eventos inmutables | Trazabilidad completa; nada se sobrescribe |
| Versionado del catálogo | Se sabe qué producto tenía el cliente en cada fecha |
| Fecha de vigencia en todo | Se puede reconstruir cualquier momento |
| Decisión con su fundamento | Explicabilidad (Parte 14, clase 11) |
| Separación identidad/transacción | Protección de datos por diseño |

### 4. Capa semántica

```text
DEFINICIONES ÚNICAS Y CERTIFICADAS

  CLIENTE ACTIVO
    persona o empresa con al menos un contrato vigente
    y una operación en los últimos 90 días

  CARTERA
    saldo de capital de contratos de crédito vigentes,
    bruto de provisiones, sin intereses devengados

  MORA > 90 DÍAS
    saldo total de contratos con alguna cuota vencida
    en más de 90 días, no el saldo vencido

  COSTO DE RIESGO
    dotación neta de provisiones del período
    sobre cartera media del período

  MARGEN DE INTERMEDIACIÓN
    margen financiero sobre activos productivos medios
```

```text
CADA DEFINICIÓN TIENE
  · fórmula exacta
  · fuente de cada componente
  · dueño responsable
  · fecha de aprobación
  · registro de cambios

Y NADIE CALCULA UN INDICADOR
FUERA DE LA CAPA SEMÁNTICA
  si un área necesita una variante,
  se define y se certifica; no se calcula aparte
```

### 5. Gobierno desde el inicio

```text
LO QUE DEBE EXISTIR ANTES DE LA PRIMERA OPERACIÓN

  · diccionario de datos de las 9 entidades maestras
  · dueño designado para cada dato crítico
  · reglas de validación en el punto de captura
  · linaje documentado de los datos que van a reportes
  · política de calidad con sus dimensiones y umbrales
  · comité de datos con periodicidad definida

COSTO DE HACERLO AHORA: 180
COSTO DE HACERLO EN EL AÑO 5: el del caso de la Parte 14, clase 4
  3 580 inicial + la información perdida
```

## 🧮 Ejemplo guiado

**Situación.** Verificar que la arquitectura soporta todo lo que el banco necesitará medir.

```text
MÉTODO
  listar los indicadores que las clases siguientes exigirán
  y verificar que el modelo de datos permita calcularlos
```

**Paso 1 — lista los indicadores requeridos.**

```text
DE LAS CLASES SIGUIENTES DEL PROYECTO
  clase 6  precios: tasa mínima por producto y segmento
  clase 7  originación: tasa de aprobación, tiempo, excepciones
  clase 8  riesgo: PD, LGD, EAD, mora por cosecha
  clase 9  operaciones: costo por transacción, conciliación
  clase 10 contabilidad: estados completos
  clase 11 tesorería: brechas, precio de transferencia
  clase 12 riesgos: el tablero de 13 métricas
  clase 13 cumplimiento: alertas, conversión, expedientes
  clase 14 dirección: cuadro de mando de 4 perspectivas
  clase 15 estrés: proyección por segmento y cosecha
```

**Paso 2 — verifica el más exigente: mora por cosecha.**

```text
MORA POR COSECHA (Parte 12, clase 13)
  requiere: para cada contrato,
    · fecha de originación (mes)
    · saldo en cada mes posterior
    · días de atraso en cada mes posterior
    · segmento y canal de originación
    · si fue excepción a política

  ¿EL MODELO LO PERMITE?
    fecha de originación: en CONTRATO  ✓
    saldo mensual: derivable de MOVIMIENTO  ✓
    días de atraso: requiere un evento de estado
      → FALTA una entidad ESTADO DE CONTRATO
        con su fecha de vigencia
    segmento y canal: en SOLICITUD  ✓
    excepción: en SOLICITUD, con su motivo  ✓

  CORRECCIÓN AL MODELO
    añadir entidad ESTADO DE CONTRATO
    con: contrato, estado, días de atraso,
    fecha desde, fecha hasta
```

**Paso 3 — verifica el precio de transferencia.**

```text
PRECIO DE TRANSFERENCIA (Parte 15, clase 4)
  requiere: para cada contrato,
    · plazo contractual y plazo conductual esperado
    · perfil de repreciación
    · el precio de transferencia aplicado en la originación

  ¿EL MODELO LO PERMITE?
    plazo contractual: en CONTRATO  ✓
    plazo conductual: es un parámetro del producto
      → debe estar en PRODUCTO, versionado  ✓
    precio aplicado: NO ESTÁ

  CORRECCIÓN
    el precio de transferencia aplicado se guarda
    EN EL CONTRATO al originar, y no se recalcula después
    → si se recalcula, el margen histórico
      de cada área cambia retroactivamente
```

**Paso 4 — verifica la explicabilidad de las decisiones.**

```text
EXPLICABILIDAD (Parte 14, clase 11)
  requiere: para cada solicitud rechazada,
    · los factores principales de la decisión
    · los valores de las variables usadas
    · la versión del modelo aplicada
    · quién revisó, si hubo revisión humana

  ¿EL MODELO LO PERMITE?
    factores: NO ESTÁ
    valores: NO ESTÁ
    versión del modelo: NO ESTÁ
    revisión: NO ESTÁ

  CORRECCIÓN
    añadir entidad DECISIÓN, ligada a SOLICITUD,
    con: modelo y versión, valores de entrada,
    resultado, factores principales, revisor, fecha

  ESTA ENTIDAD ES OBLIGATORIA POR NORMA
  y su ausencia impediría cumplir el derecho
  a explicación desde la primera solicitud
```

**Paso 5 — verifica el cumplimiento.**

```text
PREVENCIÓN DE LAVADO (Parte 12, clase 3)
  requiere:
    · perfil transaccional esperado por cliente
    · transaccionalidad observada
    · alertas con su análisis y su resolución
    · beneficiario final de cada empresa
    · nivel de riesgo del cliente y su fecha

  ¿EL MODELO LO PERMITE?
    perfil esperado: NO ESTÁ
    beneficiario final: NO ESTÁ
    nivel de riesgo: NO ESTÁ

  CORRECCIÓN
    · añadir PERFIL a la entidad cliente,
      con sus componentes y su fecha de actualización
    · añadir BENEFICIARIO FINAL como relación
      entre PERSONA y EMPRESA, con su porcentaje
    · añadir CLASIFICACIÓN DE RIESGO con fecha de vigencia
```

**Paso 6 — consolida las correcciones.**

```text
ENTIDADES AÑADIDAS AL MODELO
  10. ESTADO DE CONTRATO      (mora por cosecha)
  11. DECISIÓN                (explicabilidad)
  12. PERFIL TRANSACCIONAL    (cumplimiento)
  13. BENEFICIARIO FINAL      (cumplimiento)
  14. CLASIFICACIÓN DE RIESGO (cumplimiento)
  15. ALERTA                  (cumplimiento y fraude)

CAMPOS AÑADIDOS
  · precio de transferencia aplicado, en CONTRATO
  · plazo conductual, en PRODUCTO
  · canal de originación, en SOLICITUD
  · marca de excepción y su motivo, en SOLICITUD

COSTO DE AÑADIRLOS AHORA: incluido en el diseño
COSTO DE AÑADIRLOS EN EL AÑO 2: migración de datos
  y reconstrucción imposible del histórico
```

**Paso 7 — verifica el desacoplamiento.**

```text
PRUEBA: ¿cuántos componentes hay que tocar
para cambiar una política de crédito?

  ARQUITECTURA PROPUESTA
    la política vive en el motor de decisión
    componentes a tocar: 1
    tiempo estimado: 2 días

  ARQUITECTURA ACOPLADA (la que hay que evitar)
    la política vive en el núcleo
    componentes a tocar: núcleo, canales, reportes
    tiempo estimado: 6 semanas (Parte 14, clase 14)

PRUEBA 2: ¿cuántos para cambiar un precio?
  propuesta: 1 (tabla de precios versionada)

PRUEBA 3: ¿para añadir un producto?
  propuesta: 1 (catálogo versionado) + configuración
```

**Paso 8 — establece el gobierno de datos.**

```text
DESDE EL DÍA UNO

  DUEÑOS DE DATO
    cliente y persona:        gerente comercial
    contrato y producto:      gerente de productos
    contabilidad:             gerente de finanzas
    riesgo y clasificación:   gerente de riesgos
    cumplimiento:             gerente de cumplimiento

  REGLAS DE VALIDACIÓN EN CAPTURA
    · formato y dominio de cada campo
    · obligatoriedad según el tipo de cliente
    · coherencia entre campos relacionados
    · verificación contra fuente externa cuando exista

  UMBRALES DE CALIDAD
    completitud de datos críticos:  ≥ 98 %
    exactitud verificada:           ≥ 95 %
    unicidad de cliente:            100 %
    linaje documentado:             100 % de los datos
                                    que llegan a reportes

  COMITÉ DE DATOS
    mensual el primer año, trimestral después
```

**Interpreta:** la verificación contra los indicadores futuros **añadió seis entidades y cuatro campos**
al modelo, y todos eran obligatorios. Diseñar los datos preguntando «qué vamos a necesitar medir» en
lugar de «qué vamos a registrar» es la diferencia entre un banco que puede dirigirse desde el primer año
y uno que pasará cinco años reconstruyendo su información.

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «El banco me conoce en todos los canales» | Identificador único desde el diseño | 14, clase 4 |
| «Me explicaron por qué me rechazaron» | Entidad decisión con sus factores | 14, clase 11 |
| «Cambian cosas rápido» | Arquitectura desacoplada | 14, clase 13 |
| «No me piden los datos dos veces» | Dato maestro único | 15, clase 8 |
| «Mi historial está completo» | Eventos inmutables | 16, clase 4 |

## 🧪 Práctica

En `labs/lab-02.md`, sección de arquitectura:

1. Diseña la arquitectura por capas con sus responsabilidades.
2. Aplica el marco de construir o comprar a diez capacidades.
3. Construye el modelo de datos maestro y verifícalo contra diez indicadores futuros.
4. Define la capa semántica con cinco definiciones certificadas.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Reglas de negocio en el núcleo | Cambios lentos | Sepáralas en la capa de negocio. |
| Documento de identidad como clave | Cambia y se replica | Identificador interno único. |
| Se registra sin pensar en medir | Faltan entidades | Verifica contra los indicadores futuros. |
| Precio de transferencia recalculado | Margen histórico cambia | Guárdalo en el contrato. |
| Sin entidad de decisión | No hay explicabilidad | Es obligatoria por norma. |
| Gobierno de datos después | Costo veinte veces mayor | Desde el día uno. |

## ❓ Preguntas de comprobación

1. ¿Cuál es la ventaja irrepetible de un banco nuevo en materia de datos?
2. ¿Por qué el documento de identidad no puede ser la clave del cliente?
3. ¿Por qué las reglas de negocio no deben vivir en el núcleo?
4. ¿Por qué el precio de transferencia aplicado se guarda en el contrato?
5. ¿Qué método verifica que un modelo de datos está completo?

## 📥 Entregable

Guarda en `portfolio/parte-16/clase-04/`:

- la arquitectura por capas con sus responsabilidades;
- las decisiones de construir o comprar con su fundamento;
- el modelo de datos maestro verificado contra los indicadores futuros;
- la capa semántica y el gobierno de datos con sus umbrales.

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

- Basel Committee on Banking Supervision (2013). *Principles for effective risk data aggregation and risk reporting (BCBS 239)*. BIS.
- DAMA International (2017). *DAMA-DMBOK: Data Management Body of Knowledge* (2.ª ed.). Technics Publications.
- Basel Committee on Banking Supervision (2019). *Report on open banking and application programming interfaces*. BIS.
- Basel Committee on Banking Supervision (2021). *Principles for Operational Resilience*. BIS.
- Kleppmann, M. (2017). *Designing Data-Intensive Applications*. O'Reilly.
- Verificación local: revisa los requisitos de conservación de información, trazabilidad de decisiones y reportes regulatorios de tu supervisor.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 03 · Constitución y gobierno](03-constitucion-y-gobierno.md) | [Parte 16](../README.md) · [Programa](../../../SYLLABUS.md) | [05 · Catálogo de productos →](05-catalogo-de-productos.md) |
<!-- gen:footer:end -->
