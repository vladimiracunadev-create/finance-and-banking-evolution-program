<!-- meta
part: 17
class: 2
title: "Ecosistema, participantes y modelos de implantación"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global, chile, union-europea, brasil]
regulatory_topics: [open-finance]
regulation_last_verified: 2026-08-06
regulatory_status: en-despliegue
primary_authorities: [CMF]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 02 · Ecosistema, participantes y modelos de implantación

> [← 01 · Banca abierta, finanzas abiertas y datos abiertos](01-banca-abierta-finanzas-abiertas-y-datos-abiertos.md) · [Índice de la parte](../README.md) · [03 · El Sistema de Finanzas Abiertas de Chile →](03-sistema-de-finanzas-abiertas-de-chile.md)

**Parte 17 — Finanzas abiertas, APIs y economía de datos** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Mapear el ecosistema completo —incluidas las figuras que no aparecen en ningún
folleto— y comparar los modelos de implantación por sus **resultados
observables**, no por su retórica.

La clase anterior distinguió las tres capas y situó el consentimiento en el centro. Esta sale del régimen y entra en quién lo opera: un ecosistema con más participantes de los que el cliente ve, y con una capa de infraestructura que concentra el riesgo sin aparecer en ningún panel.

## 📚 Objetivos

Al finalizar podrás:

1. **Dibujar** el mapa de participantes de un caso concreto, incluidos los que no
   tienen relación contractual con el cliente.
2. **Comparar** modelo regulatorio, de mercado e híbrido con criterios medibles.
3. **Identificar** dónde se concentra el riesgo en cada modelo.
4. **Explicar** qué gobierna un esquema de estándar y por qué su gobernanza
   determina el resultado.
5. **Evaluar** la madurez de un ecosistema con indicadores, no con opiniones.

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

Los cuatro primeros términos son las piezas de infraestructura del ecosistema; los cuatro siguientes, su gobierno y su medición. El **proveedor tecnológico crítico** es la figura que no aparece en ningún panel de consentimientos y cuya caída deja sin servicio a decenas de entidades a la vez.

| Concepto | Comprensión verificable |
|---|---|
| `esquema` | Conjunto de reglas, estándares y gobernanza que ordena el ecosistema |
| `directorio` | Registro autoritativo de quién está autorizado a participar |
| `agregador técnico` | Intermediario que conecta a muchos con muchos |
| `proveedor tecnológico crítico` | Proveedor cuya caída afecta a varios participantes |
| `certificación de conformidad` | Prueba de que una implementación cumple el estándar |
| `interoperabilidad` | Que dos implementaciones distintas se entiendan sin acuerdo bilateral |
| `modelo de implantación` | Quién obliga, quién estandariza y quién paga |
| `indicador de madurez` | Medida objetiva del funcionamiento real del ecosistema |

## 🧠 Modelo mental

El modelo mental es un esquema con tres capas de actores: los que tienen los datos, los que los consumen y los que operan la infraestructura por la que viajan. La tercera capa es la que concentra el riesgo sistémico y la que menos visibilidad tiene.

```text
UN ECOSISTEMA DE FINANZAS ABIERTAS TIENE CUATRO CAPAS

  CAPA 1 · REGLAS       quién debe abrir, a quién, con qué límites
  CAPA 2 · ESTÁNDARES   cómo se habla: API, seguridad, mensajes
  CAPA 3 · CONFIANZA    directorio, certificados, certificación
  CAPA 4 · OPERACIÓN    disponibilidad, soporte, incidentes, disputas

SI FALTA UNA CAPA, EL SISTEMA NO FUNCIONA AUNQUE LAS OTRAS TRES SEAN BUENAS
  sin reglas       nadie abre
  sin estándares   cada conexión es un proyecto bilateral
  sin confianza    no se sabe con quién se habla
  sin operación    funciona en la demostración y no en producción
```

## 📖 Desarrollo

### 1. El mapa completo

```text
                       ┌──────────────────────┐
                       │  ESQUEMA / GOBIERNO  │  reglas, estándar, sanciones
                       └──────────┬───────────┘
                                  │
          ┌───────────────────────┼───────────────────────┐
          ▼                       ▼                       ▼
   ┌─────────────┐        ┌──────────────┐        ┌──────────────┐
   │ DIRECTORIO  │        │ CERTIFICACIÓN│        │  SUPERVISOR  │
   │ quién es    │        │ conformidad  │        │  autoriza    │
   └──────┬──────┘        └──────────────┘        └──────────────┘
          │
   ┌──────▼───────────────────────────────────────────────────┐
   │                      OPERACIÓN                           │
   │                                                          │
   │  CLIENTE ──consiente──► PROVEEDOR ──API──► INSTITUCIÓN   │
   │                          (info/pago)        PROVEEDORA    │
   │                              │                   │        │
   │                              ▼                   ▼        │
   │                    PROVEEDOR TECNOLÓGICO (uno o los dos)  │
   └──────────────────────────────────────────────────────────┘
```

La figura del proveedor tecnológico aparece **debajo** de las dos partes que sí
tienen contrato con el cliente. Ese es exactamente el problema: el riesgo está
donde la visibilidad no llega.

### 2. Los tres modelos, con criterios medibles

| Criterio | Regulatorio | De mercado | Híbrido |
|---|---|---|---|
| Cobertura de entidades | Alta por obligación | Desigual | Media-alta |
| Velocidad de despliegue | Baja | Alta | Media |
| Homogeneidad técnica | Alta si el estándar es único | Baja | Depende del esquema |
| Coste para la entidad pequeña | Alto y no elegible | Bajo, opcional | Medio |
| Calidad del servicio | Variable: cumplir no es servir | Alta donde hay negocio | Depende de la certificación |
| Resolución de disputas | Vía supervisor | Vía contrato | Mixta |
| Riesgo de captura | Del regulador | Del participante dominante | De la gobernanza del esquema |

```text
EL ERROR DE ANÁLISIS MÁS COMÚN
  «el modelo regulatorio es mejor porque hay más entidades conectadas»

  conectadas ≠ funcionando
  la métrica correcta es la tasa de éxito de llamadas en horario real,
  no el número de entidades con un endpoint publicado
```

### 3. Gobernanza del esquema

```text
UN ESQUEMA DECIDE, COMO MÍNIMO
  · qué versión del estándar es obligatoria y desde cuándo
  · cuánto dura el periodo de coexistencia entre versiones
  · qué se certifica y quién certifica
  · qué ocurre si un participante no cumple
  · quién paga la infraestructura común
  · cómo se admiten y expulsan participantes

QUIÉN DECIDE DETERMINA EL RESULTADO
  si deciden solo las entidades obligadas → estándar mínimo
  si deciden solo los terceros            → exigencias insostenibles
  si decide solo el regulador             → estándar rígido y lento
  → los esquemas que funcionan tienen representación de las tres partes
    y un mecanismo de desempate
```

### 4. Directorio y confianza

El directorio responde a una pregunta operativa: *cuando llega una petición
firmada por `tpp_042`, ¿esa entidad está autorizada hoy?*

```text
UN DIRECTORIO ÚTIL TIENE
  · identidad del participante y su figura
  · alcances que está autorizado a solicitar
  · estado: activo, suspendido, revocado, en cese
  · certificados vigentes y sus huellas
  · fecha del último cambio de estado
  · consulta en tiempo real, con caché acotada

SIN DIRECTORIO EN TIEMPO REAL
  un participante suspendido esta mañana
  sigue accediendo a datos esta tarde
```

### 5. Indicadores de madurez

| Indicador | Qué mide | Señal de alarma |
|---|---|---|
| Tasa de éxito de llamadas | Si el sistema sirve | Por debajo del 97 % |
| Latencia p95 en hora punta | Si sirve cuando importa | Por encima de 2 s |
| Entidades con certificación vigente | Si el estándar se cumple | Menos del 90 % |
| Consentimientos activos por cliente | Si hay uso real | Cerca de 1 en promedio |
| Tasa de revocación | Si el cliente confía | Por encima del 25 % anual |
| Concentración de los tres mayores | Riesgo sistémico | Por encima del 70 % |
| Incidentes con impacto en cliente | Operación real | Tendencia creciente |

## 🧮 Ejemplo guiado

El ejemplo compara dos modelos de implantación sobre el mismo mercado. Conviene mirar el ritmo de adopción y el costo por participante: los dos modelos funcionan y no producen el mismo ecosistema.

**Situación.** Un supervisor debe decidir si el ecosistema está listo para
ampliar el alcance obligatorio a productos de inversión. Tiene estos datos del
último trimestre.

```text
ENTIDADES OBLIGADAS                        48
ENTIDADES CON ENDPOINT PUBLICADO           46
ENTIDADES CON CERTIFICACIÓN VIGENTE        31

LLAMADAS DEL TRIMESTRE                     412 000 000
LLAMADAS CON ÉXITO                         389 340 000
LATENCIA p95 EN HORA PUNTA                 3,4 s

CONSENTIMIENTOS ACTIVOS                    2 940 000
CLIENTES CON AL MENOS UNO                  2 610 000
REVOCACIONES DEL TRIMESTRE                 214 000

CUOTA DE LOS TRES MAYORES AGREGADORES      76 %
INCIDENTES CON IMPACTO EN CLIENTE          Q1: 4   Q2: 7   Q3: 11
```

**Paso 1 — calcula la tasa de éxito.**

```text
389 340 000 / 412 000 000 = 94,50 %

UMBRAL DE REFERENCIA: 97 %
  → 2,5 puntos por debajo
  → 22 660 000 llamadas fallidas en el trimestre
```

**Paso 2 — traduce el fallo a experiencia del cliente.**

```text
LLAMADAS POR CLIENTE ACTIVO Y TRIMESTRE
  412 000 000 / 2 610 000 = 158 llamadas

FALLOS POR CLIENTE
  158 × 5,50 % = 8,7 fallos por cliente y trimestre
  ≈ 1 fallo cada 10 días para un cliente medio

CON p95 DE 3,4 s EN HORA PUNTA
  1 de cada 20 llamadas tarda más de 3,4 s
  en el momento en que más gente mira su panel
```

**Paso 3 — evalúa la certificación.**

```text
31 / 48 = 64,6 % de entidades certificadas
46 / 48 = 95,8 % con endpoint publicado

LA BRECHA ES EL DATO
  31 puntos entre «publicó algo» y «cumple el estándar»
  → 15 entidades exponen una API que nadie verificó
  → cada integración con esas 15 es un proyecto bilateral
```

**Paso 4 — evalúa la confianza del cliente.**

```text
TASA DE REVOCACIÓN TRIMESTRAL
  214 000 / 2 940 000 = 7,3 %
  anualizada aproximada: 1 − (1 − 0,073)^4 = 26,4 %

CONSENTIMIENTOS POR CLIENTE
  2 940 000 / 2 610 000 = 1,13

INTERPRETACIÓN
  · uso poco profundo: la mayoría tiene un solo consentimiento
  · revocación anual del 26 %: por encima del umbral de alarma
  · combinación típica de «probé y lo quité»
```

**Paso 5 — evalúa la concentración.**

```text
76 % EN TRES AGREGADORES

CONSECUENCIA OPERATIVA
  la caída de uno solo afecta a ~25 % de los accesos del sistema

CONSECUENCIA DE MERCADO
  las entidades negocian con tres contrapartes, no con un mercado
  el precio de las APIs premium lo fijan esas tres

CONSECUENCIA REGULATORIA
  ninguno de los tres es una entidad financiera supervisada
  por su actividad de agregación
```

**Paso 6 — formula la decisión.**

```text
NO AMPLIAR TODAVÍA EL ALCANCE OBLIGATORIO

MOTIVOS, EN ORDEN DE PESO
  1. tasa de éxito 2,5 puntos bajo el umbral, con tendencia
     de incidentes creciente (4 → 7 → 11)
  2. un tercio de las entidades sin certificación vigente:
     ampliar el alcance multiplica una deuda ya existente
  3. concentración del 76 % sin supervisión específica
     de los agregadores

QUÉ HACER ANTES
  · exigir certificación vigente como condición de operación,
    con plazo y consecuencia
  · publicar el cuadro de disponibilidad por entidad:
    la transparencia mueve la aguja más que la sanción
  · abrir la vigilancia de proveedores tecnológicos críticos
  · fijar el umbral de éxito y latencia en la norma,
    no en una guía

CONDICIÓN DE REVISIÓN
  · éxito ≥ 97 % durante dos trimestres consecutivos
  · certificación vigente ≥ 90 % de las entidades
  · incidentes con impacto en cliente en tendencia decreciente

Y REGISTRAR LA DISCREPANCIA
  la industria argumentará que 94,5 % es «suficiente».
  El dato que responde no es el porcentaje: es 1 fallo
  cada 10 días por cliente, en un producto que el cliente
  usa para decidir si le alcanza el dinero
```

**Interpreta:** el ecosistema estaba «conectado» al 95,8 % y **funcionando** muy
por debajo. La diferencia entre esas dos cifras es la mayor parte del trabajo de
supervisión de un sistema de finanzas abiertas.

## 🧭 Perspectivas

Cada actor del ecosistema ve una parte del sistema y decide sobre ella. La tabla las enfrenta, y la fila de la infraestructura es la que revela la concentración.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un panel que a veces no carga | Si sigue usándolo |
| Fintech | 15 integraciones bilaterales | Usar un agregador y concentrar riesgo |
| Banco | Coste sin ingreso directo | Cumplir el mínimo o competir |
| Agregador | Posición de intermediación | Precio y cobertura |
| Banco central | Nuevo canal de pagos | Si lo vigila |
| Supervisor | Cifras de conformidad | Si amplía el alcance |
| Auditor | Certificaciones vencidas | Qué observa |
| Sociedad | Promesa de competencia | Si se cumple |

## 🏦 Del cliente al banco

El cliente ve una aplicación y el banco ve una cadena de participantes con responsabilidades repartidas. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «La app no carga mi banco» | Tasa de éxito por entidad | 17, clase 13 |
| «Todas las apps usan lo mismo» | Concentración de agregadores | 17, clase 2 |
| «Cambié de app y fue igual» | Interoperabilidad del estándar | 17, clase 8 |
| «Me pidieron autorizar otra vez» | Certificado o directorio caducado | 17, clase 7 |

## ⚖️ Riesgos y controles

Los riesgos del ecosistema son de estructura antes que de tecnología: concentración, dependencia y responsabilidad difusa. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Cumplimiento formal | Endpoint publicado que falla | Certificación obligatoria y métrica pública |
| Concentración | Tres agregadores, un punto de fallo | Vigilancia y planes de sustitución |
| Directorio desactualizado | Suspendido que sigue accediendo | Consulta en tiempo real y caché corta |
| Captura del esquema | El estándar protege al incumbente | Gobernanza tripartita con desempate |
| Fragmentación de versiones | Cada entidad en una versión distinta | Coexistencia acotada con fecha de corte |
| Proveedor crítico | Caída simultánea de N entidades | Registro, pruebas y salida ordenada |

## 🧪 Práctica

En [`labs/lab-01.md`](../labs/lab-01.md) y [`labs/lab-06.md`](../labs/lab-06.md):

1. Dibuja el mapa de participantes de tu producto, incluidos los tecnológicos.
2. Calcula los siete indicadores de madurez con los datos del ejercicio.
3. Determina qué capa del esquema falta en un caso dado.
4. Propón el umbral de certificación que exigirías y justifícalo.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen problemas de ecosistema. Las causas son concentración no medida y certificaciones tratadas como garantía de seguridad.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Contar entidades conectadas | Se confunde publicar con servir | Mide tasa de éxito |
| Ignorar al proveedor tecnológico | No tiene contrato con el cliente | Inclúyelo en el mapa |
| Comparar modelos por ideología | No hay criterios | Usa indicadores medibles |
| Caché larga del directorio | Se optimizó la latencia | Caché corta e invalidación |
| Estándar sin fecha de corte | Coexistencia indefinida | Fija la fecha desde el inicio |
| Certificación una sola vez | Se trató como trámite | Vigencia y recertificación |

## ❓ Preguntas de comprobación

1. ¿Por qué «entidades conectadas» es una métrica engañosa y cuál la sustituye?
2. ¿Qué cuatro capas debe tener un ecosistema y qué ocurre si falta cada una?
3. ¿Por qué la gobernanza del esquema determina el nivel del estándar?
4. ¿Qué riesgo concreto crea una caché larga del directorio?
5. En el ejemplo guiado, ¿cuál de los seis indicadores pesó más en la decisión y
   por qué?

## 📥 Entregable

Guarda en `portfolio/parte-17/clase-02/`:

- el mapa de participantes de tu producto, con las cuatro capas identificadas;
- los siete indicadores calculados sobre los datos del ejercicio;
- una recomendación de política con su condición de revisión;
- la lista de proveedores tecnológicos que serían críticos en tu caso.

## 🔗 Referencias cruzadas

- **Viene de:** clase 1; Parte 12, clase 2 (supervisión); Parte 15, clase 9
  (riesgo de terceros).
- **Continúa en:** clase 3 (el caso chileno), clase 7 (certificados), clase 13
  (disponibilidad y SLA).
- **Se aplica en:** Parte 22, clase 5; Parte 23, clase 2 (mapa de participantes).

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

- Comisión para el Mercado Financiero (Chile). *Normativa y anexo técnico del Sistema de Finanzas Abiertas*. CMF. <https://www.cmfchile.cl/>
- Banco Central do Brasil. *Open Finance Brasil — regulação e estatísticas*. <https://www.bcb.gov.br/estabilidadefinanceira/openfinance>
- Bank for International Settlements (2019). *Report on open banking and application programming interfaces*. BCBS. <https://www.bis.org/bcbs/publ/d486.htm>
- Financial Stability Board (2023). *Enhancing third-party risk management and oversight*. FSB. <https://www.fsb.org/2023/12/enhancing-third-party-risk-management-and-oversight-a-toolkit-for-financial-institutions-and-financial-authorities/>
- OpenID Foundation. *FAPI conformance testing*. <https://openid.net/certification/>
- Verificación local: identifica quién gobierna el esquema en tu jurisdicción, qué publica sobre disponibilidad y si existe régimen de proveedores tecnológicos críticos. **Fecha de verificación de esta clase: 2026-08-06.** Esta clase no constituye asesoría legal.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 01 · Banca abierta, finanzas abiertas y datos abiertos](01-banca-abierta-finanzas-abiertas-y-datos-abiertos.md) | [Parte 17](../README.md) · [Programa](../../../SYLLABUS.md) | [03 · El Sistema de Finanzas Abiertas de Chile →](03-sistema-de-finanzas-abiertas-de-chile.md) |
<!-- gen:footer:end -->
