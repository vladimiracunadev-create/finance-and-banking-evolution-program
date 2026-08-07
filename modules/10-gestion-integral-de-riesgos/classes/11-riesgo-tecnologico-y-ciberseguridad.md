---
part: 11
class: 11
title: "Riesgo tecnológico y ciberseguridad"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 11 · Riesgo tecnológico y ciberseguridad

> [← 10 · Riesgo operacional](10-riesgo-operacional.md) · [Índice de la parte](../README.md) · [12 · Riesgo de modelo →](12-riesgo-de-modelo.md)

**Parte 11 — Gestión integral de riesgos** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Gestionar el riesgo de que la tecnología del banco falle, sea comprometida o quede indisponible. Es el
riesgo que más rápido ha crecido, el único con un adversario inteligente que se adapta, y el que puede
convertir un problema técnico en una corrida de depósitos en horas.

El riesgo operacional de la clase anterior incluye el tecnológico, y esta clase lo separa porque su naturaleza es distinta: tiene un adversario que se adapta. Un fallo operativo ocurre; un ataque se diseña contra los controles que uno tiene, y por eso la medición histórica sirve menos.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** riesgo tecnológico de riesgo cibernético y de riesgo de información.
2. **Aplicar** un marco de ciberseguridad reconocido a un banco.
3. **Evaluar** la superficie de ataque y priorizar su reducción.
4. **Diseñar** la respuesta a un incidente con sus obligaciones de notificación.
5. **Gestionar** el riesgo de terceros tecnológicos y la concentración de proveedores.

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

Los dos primeros términos separan el fallo del ataque; los seis siguientes, la superficie, las arquitecturas de defensa y la medida del daño. El **tiempo de permanencia** es la métrica que más dice: cuánto tiempo estuvo un atacante dentro antes de ser detectado, y suele medirse en meses.

| Concepto | Comprensión verificable |
|---|---|
| `riesgo tecnológico` | Fallas de disponibilidad, integridad o capacidad de los sistemas. |
| `riesgo cibernético` | Compromiso deliberado por un adversario. |
| `superficie de ataque` | Conjunto de puntos por los que un sistema puede ser atacado. |
| `defensa en profundidad` | Capas sucesivas de control, ninguna suficiente por sí sola. |
| `confianza cero` | Ningún acceso se presume legítimo por su origen en la red. |
| `deuda técnica` | Costo acumulado de decisiones técnicas postergadas. |
| `tiempo de permanencia` | Días entre el compromiso y su detección. |
| `resiliencia cibernética` | Capacidad de operar y recuperarse durante un ataque. |

## 🧠 Modelo mental

El modelo mental es el del atacante racional: compara lo que gana con lo que le cuesta y ataca por donde sale más barato. La defensa no consiste en ser inexpugnable sino en ser más caro de atacar que el valor que hay detrás.

```text
LOS DEMÁS RIESGOS NO TIENEN INTENCIÓN. ESTE SÍ.

  el riesgo de mercado no estudia tus controles
  el riesgo de crédito no cambia de táctica cuando lo detectas
  un atacante hace ambas cosas

CONSECUENCIAS METODOLÓGICAS
  · la historia predice peor que en otros riesgos
  · los controles se degradan solos: lo que protegía ayer no protege hoy
  · la medición no puede ser solo estadística: necesita
    simulación adversaria (equipos de ataque y defensa)
  · el objetivo no es impedir todo ataque: es DETECTAR RÁPIDO
    y RECUPERAR SIN PÉRDIDA DE INTEGRIDAD
```

## 📖 Desarrollo

### 1. Tres riesgos distintos

Fallo tecnológico, ataque y obsolescencia son riesgos distintos con controles distintos. La tabla los separa.

| | Tecnológico | Cibernético | De información |
|---|---|---|---|
| Origen | Falla, obsolescencia, capacidad | Adversario | Ambos, más error humano |
| Se manifiesta como | Indisponibilidad, error | Compromiso, extorsión, fraude | Fuga, alteración, pérdida |
| Se gestiona con | Arquitectura, capacidad, continuidad | Detección, respuesta, simulación | Clasificación, cifrado, acceso |
| Métrica clave | Disponibilidad, incidentes | Tiempo de detección | Datos clasificados y protegidos |

### 2. Marco de ciberseguridad

Las cinco funciones del marco del NIST, aplicadas a un banco:

```text
IDENTIFICAR   inventario de activos, datos, proveedores y dependencias
              ¿qué tengo, dónde está, qué pasa si falla?

PROTEGER      control de acceso, cifrado, segmentación, formación
              autenticación multifactor, mínimo privilegio

DETECTAR      registro y correlación, monitoreo continuo, alertas
              ¿cuánto tardo en darme cuenta?

RESPONDER     contención, erradicación, comunicación, notificación
              ¿quién decide desconectar y con qué autoridad?

RECUPERAR     restauración verificada, lecciones, mejora
              ¿mis respaldos están fuera del alcance del atacante?
```

```text
LA PREGUNTA QUE MÁS BANCOS FALLAN
  "¿mis respaldos están aislados del entorno comprometido?"

  el patrón de los ataques de extorsión es cifrar primero los respaldos
  un respaldo accesible desde la red comprometida NO es un respaldo
```

### 3. Superficie de ataque

La superficie de ataque se puede inventariar y reducir. El procedimiento siguiente la mide.

```text
COMPONENTES
  · personas          suplantación, ingeniería social, personal interno
  · aplicaciones      vulnerabilidades, configuración, dependencias
  · infraestructura   sistemas sin actualizar, servicios expuestos
  · terceros          acceso de proveedores, cadena de suministro
  · datos             copias no controladas, entornos de prueba con datos reales
  · identidades       credenciales, accesos privilegiados, cuentas huérfanas
```

| Vector de entrada | Participación típica en incidentes |
|---|---|
| Credenciales comprometidas | La más frecuente |
| Correo con suplantación | Muy frecuente |
| Vulnerabilidad sin corregir | Frecuente |
| Tercero comprometido | Creciente |
| Personal interno | Menos frecuente, más costoso |

**Los dos primeros vectores no son técnicos.** La mayor parte de los incidentes empieza con una persona,
no con una falla de software. Por eso la formación y la autenticación multifactor tienen el mejor
retorno entre todos los controles disponibles.

### 4. Respuesta a incidentes

La respuesta tiene fases con objetivos distintos y en orden. La tabla las recoge.

```text
FASES
  0. PREPARACIÓN     plan, roles, autoridad, canales alternos, ensayos
  1. DETECCIÓN       identificar y clasificar
  2. CONTENCIÓN      limitar el alcance sin destruir evidencia
  3. ERRADICACIÓN    eliminar la presencia del atacante
  4. RECUPERACIÓN    restaurar con integridad verificada
  5. LECCIONES       causa raíz y mejora

DECISIONES QUE DEBEN ESTAR PREDEFINIDAS
  · quién puede desconectar un sistema crítico, a qué hora, sin consultar
  · cuándo se notifica al supervisor (hay plazos normativos)
  · cuándo y cómo se informa a los clientes afectados
  · si existe política sobre el pago de rescates
  · quién habla públicamente
```

```text
CONFLICTO CENTRAL DE LA CONTENCIÓN
  desconectar rápido    limita el daño, interrumpe el servicio
  desconectar tarde     mantiene el servicio, extiende el compromiso

  esa decisión no puede tomarse por primera vez durante el incidente
```

### 5. Terceros y concentración

La dependencia de proveedores comunes concentra el riesgo del sector entero. La tabla lo describe, y esta idea reaparece en las Partes 17 y 22.

```text
EL PERÍMETRO YA NO EXISTE
  proveedor de nube, procesador de pagos, plataforma de núcleo bancario,
  proveedor de identidad, servicio de mensajería

RIESGO DE CONCENTRACIÓN SISTÉMICA
  si todos los bancos del país usan el mismo proveedor,
  su falla es un evento sistémico
  y ningún banco individual puede resolverlo
```

| Control sobre terceros | Qué asegura |
|---|---|
| Debida diligencia previa | Capacidad y madurez del proveedor |
| Derecho de auditoría contractual | Verificación, no confianza |
| Requisitos de notificación de incidentes | Enterarse a tiempo |
| Portabilidad de datos y salida ordenada | No quedar cautivo |
| Plan de salida probado | Que la alternativa exista de verdad |
| Segmentación del acceso del proveedor | Que su compromiso no sea el tuyo |

## 🧮 Ejemplo guiado

El ejemplo prioriza amenazas con el criterio del atacante racional. El orden que sale no coincide con el que sugiere la sofisticación técnica, y esa es la conclusión.

**Situación.** Un banco sufre un incidente y evalúa su preparación después.

```text
CRONOLOGÍA
  día 0     credenciales de un administrador comprometidas por suplantación
  día 0-38  el atacante se mueve lateralmente sin ser detectado
  día 38    cifrado de 340 servidores, incluidos 2 de respaldo
  día 38    se detecta el incidente
  día 38-41 servicios digitales indisponibles
  día 41-52 recuperación parcial desde respaldo externo del día 31
  día 52    servicio restablecido; 7 días de transacciones reconstruidos

TIEMPO DE PERMANENCIA: 38 días
```

**Paso 1 — cuantifica la pérdida.**

```text
DIRECTA
  respuesta y recuperación (equipos externos, horas extra)       840
  reconstrucción de 7 días de transacciones                      260
  compensaciones a clientes                                      420
  refuerzo de atención                                           110

REGULATORIA Y LEGAL
  sanción estimada por deficiencias de control                 1 200
  contingencia legal por datos personales                        680

NEGOCIO
  fuga de clientes: 1,8 % de 640 000 = 11 520 clientes
  11 520 × 96 000 × 3,89 (VP 5 años)                           4 302
  captación perdida durante 14 días                              340

PÉRDIDA TOTAL ESTIMADA                                         8 152
```

**Paso 2 — identifica los puntos de falla.**

```text
1. ENTRADA
   credenciales de administrador sin autenticación multifactor
   → control disponible, no implantado para cuentas privilegiadas

2. PERMANENCIA (38 días)
   sin correlación de registros ni detección de movimiento lateral
   → el atacante tuvo 38 días para mapear y preparar

3. RESPALDOS
   2 de 4 conjuntos de respaldo accesibles desde la red comprometida
   → se cifraron junto con el resto

4. RECUPERACIÓN
   el respaldo externo tenía 7 días de antigüedad
   punto objetivo de recuperación declarado: 24 horas
   real: 7 días

5. DECISIÓN
   la desconexión se demoró 6 horas por falta de autoridad definida
```

**Paso 3 — evalúa cada control por su costo y efecto.**

```text
CONTROL A — autenticación multifactor para cuentas privilegiadas
  costo: 42 anuales
  habría impedido: la entrada
  efecto: pérdida evitada 8 152 (el evento no ocurre)

CONTROL B — correlación de registros con detección de comportamiento
  costo: 310 anuales
  habría reducido: permanencia de 38 días a ~4
  efecto: contención antes del cifrado masivo
  pérdida estimada con detección temprana: 640

CONTROL C — respaldos inmutables y aislados
  costo: 180 anuales
  habría reducido: punto de recuperación de 7 días a 4 horas
  efecto: sin reconstrucción, recuperación en 2 días
  pérdida estimada: 2 900

CONTROL D — autoridad de desconexión predefinida
  costo: 0 (decisión de gobierno)
  efecto: 6 horas menos de propagación
```

**Paso 4 — calcula el retorno de cada control.**

```text
probabilidad anual estimada de un evento de esta clase: 0,15

                pérdida    pérdida    reducción    costo    beneficio
                sin ctrl   con ctrl   esperada     anual    neto anual
CONTROL A         8 152        0        1 223        42      1 181
CONTROL B         8 152      640        1 127       310        817
CONTROL C         8 152    2 900          788       180        608
CONTROL D         8 152    7 400          113         0        113
```

**Paso 5 — evalúa la combinación, no los controles aislados.**

```text
los controles NO son independientes:
si A funciona, B y C nunca se activan

VALOR MARGINAL EN CONJUNTO (defensa en profundidad)
  A solo:        reduce la probabilidad de entrada, no la elimina
                 un atacante determinado encuentra otra vía
  A + B:         entrada más difícil + detección temprana si entra
  A + B + C:     + recuperación garantizada si el cifrado ocurre
  A + B + C + D: + contención rápida

  costo total: 532 anuales
  pérdida esperada residual estimada: ~120
  reducción: 1 223 − 120 = 1 103 anuales
  BENEFICIO NETO: 571 anuales

evaluar A solo daría el mejor retorno individual
y dejaría al banco con una sola capa
```

**Paso 6 — extrae la lección sobre la medición.**

```text
antes del incidente, la autoevaluación calificaba:
  "gestión de accesos privilegiados": EFECTIVO
  evidencia: existía una política

  la política exigía autenticación multifactor
  la implantación cubría el 68 % de las cuentas privilegiadas
  la cuenta comprometida estaba en el 32 % restante

LA POLÍTICA ERA EFECTIVA. LA IMPLANTACIÓN NO.
y la autoevaluación medía la política
```

**Paso 7 — decisiones.**

```text
1. Implantar A, B, C y D como conjunto, no como alternativas
2. Cambiar el criterio de evaluación de controles:
   se evalúa COBERTURA MEDIDA, no existencia de política
3. Ejercicio de simulación adversaria anual con equipo externo
4. Prueba de restauración desde respaldo aislado, trimestral,
   con criterio de éxito verificable
5. Revisar la concentración: el proveedor de identidad es único
6. Incorporar el escenario cibernético a las pruebas de estrés
   con su efecto sobre la liquidez (Parte 11, clase 13)
```

**Interpreta:** el control que habría evitado todo costaba **42 al año** y existía como política desde
hacía tres años. La brecha no estaba en el diseño ni en el presupuesto: estaba en **la diferencia entre
tener una política y haberla implantado por completo**. Por eso la métrica correcta de un control de
seguridad no es su existencia sino su **cobertura medida**, y por eso la simulación adversaria es
insustituible: es lo único que descubre el 32 % que la autoevaluación no vio.

## 🏦 Del cliente al banco

El cliente confía en la aplicación y el banco defiende una superficie que crece con cada canal nuevo. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «El banco estuvo caído dos semanas» | Punto objetivo de recuperación no cumplido | 10, clase 16 |
| «Filtraron mis datos» | Riesgo de información y notificación | 4, clase 10 |
| «Me piden un segundo factor y molesta» | El control con mejor retorno del catálogo | 4, clase 3 |
| «Me llamaron del banco y era falso» | Suplantación como vector principal | 4, clase 4 |
| «Todos los bancos fallaron el mismo día» | Concentración de proveedores | 11, clase 11 |

## 🧪 Práctica

El laboratorio pide inventariar la superficie de ataque de un servicio y priorizar. El punto más barato para el atacante no es el más protegido.

En `labs/lab-06.md`:

1. Aplica las cinco funciones del marco de ciberseguridad a un banco sintético.
2. Mapea la superficie de ataque y prioriza tres reducciones por costo y efecto.
3. Evalúa cuatro controles por su reducción de pérdida esperada y en combinación.
4. Diseña el plan de respuesta con las decisiones y plazos predefinidos.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen incidentes detectados tarde. Las causas son ausencia de detección y confianza en controles perimetrales.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se evalúa la política, no su cobertura | Autoevaluación formal | Mide implantación efectiva. |
| Respaldos accesibles desde la red | Diseño incompleto | Respaldos aislados e inmutables. |
| Autoridad de desconexión indefinida | Gobierno no resuelto | Define quién decide y cuándo. |
| Se elige un solo control por su retorno | Sin defensa en profundidad | Evalúa la combinación. |
| Proveedor único de identidad o nube | Concentración | Evalúa alternativa y salida. |
| Se mide con estadística histórica | Adversario adaptativo | Añade simulación adversaria. |

## ❓ Preguntas de comprobación

1. ¿Qué implica metodológicamente que este riesgo tenga un adversario inteligente?
2. ¿Por qué un respaldo accesible desde la red comprometida no es un respaldo?
3. ¿Por qué la autenticación multifactor tiene el mejor retorno del catálogo de controles?
4. ¿Qué mide el tiempo de permanencia y por qué es el indicador central?
5. ¿Por qué evaluar controles por separado lleva a una arquitectura frágil?

## 📥 Entregable

Guarda en `portfolio/parte-11/clase-11/`:

- el marco de ciberseguridad aplicado con sus cinco funciones;
- el mapa de superficie de ataque con las reducciones priorizadas;
- la evaluación de controles individual y combinada;
- el plan de respuesta con decisiones, plazos y responsables.

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

- NIST (2024). *Cybersecurity Framework 2.0*. National Institute of Standards and Technology. <https://www.nist.gov/cyberframework>
- Basel Committee on Banking Supervision (2021). *Principles for Operational Resilience*. BIS.
- Financial Stability Board (2020). *Effective Practices for Cyber Incident Response and Recovery*. FSB. <https://www.fsb.org/2020/10/effective-practices-for-cyber-incident-response-and-recovery-final-report/>
- Committee on Payments and Market Infrastructures e IOSCO (2016). *Guidance on cyber resilience for financial market infrastructures*. BIS.
- ISO/IEC (2022). *ISO/IEC 27001: Information security management systems*. ISO.
- Verificación local: revisa los plazos de notificación de incidentes, los requisitos de gestión de proveedores tecnológicos y la normativa de protección de datos personales de tu país.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 10 · Riesgo operacional](10-riesgo-operacional.md) | [Parte 11](../README.md) · [Programa](../../../SYLLABUS.md) | [12 · Riesgo de modelo →](12-riesgo-de-modelo.md) |
<!-- gen:footer:end -->
