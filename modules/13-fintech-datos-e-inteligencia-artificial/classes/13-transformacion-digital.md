<!-- meta
part: 14
class: 13
title: "Transformación digital"
level: profesional
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 13 · Transformación digital

> [← 12 · Regulación de la tecnología financiera](12-regulacion-de-la-tecnologia-financiera.md) · [Índice de la parte](../README.md) · [14 · Estrategia tecnológica →](14-estrategia-tecnologica.md)

**Parte 14 — Fintech, datos e inteligencia artificial** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Ejecutar el cambio, no solo diseñarlo. Las transformaciones digitales bancarias fracasan con una
frecuencia bien documentada, y la causa dominante no es tecnológica: es que **se digitaliza un proceso
existente en lugar de rediseñarlo**, y que la organización que lo opera no cambia con él.

Las clases anteriores describen tecnologías. Esta trata de cómo un banco existente las adopta, que es un problema de organización antes que de tecnología. Y empieza distinguiendo dos cosas que se confunden: digitalizar un proceso malo produce un proceso malo más rápido.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** digitalización de transformación.
2. **Diagnosticar** el estado de una organización en sus cuatro dimensiones.
3. **Priorizar** iniciativas por valor y por capacidad de ejecución.
4. **Gestionar** la deuda técnica y la migración del núcleo bancario.
5. **Medir** el avance con indicadores que no se puedan simular.

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

Los cuatro primeros términos son el objeto de la transformación; los cuatro siguientes, la organización y su medición. La **deuda técnica** es la restricción que explica los plazos: cada año de aplazamiento encarece el cambio, y en algún momento reemplazar sale más barato que arreglar.

| Concepto | Comprensión verificable |
|---|---|
| `digitalización` | Trasladar un proceso existente a un canal digital. |
| `transformación` | Rediseñar el proceso aprovechando lo que lo digital permite. |
| `núcleo bancario` | Sistema que registra cuentas, saldos y movimientos. |
| `deuda técnica` | Costo acumulado de decisiones técnicas postergadas. |
| `arquitectura desacoplada` | Componentes que evolucionan de forma independiente. |
| `capacidad de entrega` | Ritmo al que la organización pone cambios en producción. |
| `producto digital` | Servicio gestionado por un equipo estable con responsabilidad completa. |
| `indicador de resultado` | Métrica que mide efecto, no actividad. |

## 🧠 Modelo mental

El modelo mental es una distinción entre capa y núcleo: se puede poner una aplicación bonita sobre un sistema central de treinta años, y funciona hasta que el cliente pide algo que el núcleo no sabe hacer. La transformación real toca el núcleo y por eso cuesta lo que cuesta.

```text
DIGITALIZAR                        TRANSFORMAR

el formulario de papel             se elimina el formulario:
se convierte en un formulario      los datos ya están en el banco
en pantalla

el cliente sube el documento       el banco verifica contra la fuente
que antes llevaba a la sucursal

la aprobación tarda 3 días         la aprobación es inmediata
pero ahora en línea                porque el proceso se rediseñó

RESULTADO
  digitalizar: el mismo proceso, más barato
  transformar: un proceso distinto, mucho mejor

Y EL SEGUNDO EXIGE CAMBIAR LA ORGANIZACIÓN,
no solo la tecnología
```

## 📖 Desarrollo

### 1. Cuatro dimensiones del diagnóstico

El diagnóstico cubre cuatro dimensiones y ninguna es solo tecnológica. La tabla las recoge.

```text
1. PROPUESTA AL CLIENTE
   ¿qué problema del cliente resolvemos mejor
    que antes o que la competencia?

2. PROCESOS Y DATOS
   ¿el proceso está rediseñado o solo trasladado?
   ¿los datos están gobernados? (clase 4)

3. TECNOLOGÍA
   ¿la arquitectura permite cambiar rápido
    sin romper lo existente?

4. ORGANIZACIÓN Y PERSONAS
   ¿quién decide? ¿con qué velocidad?
   ¿el equipo tiene las capacidades?
```

| Dimensión | Síntoma de inmadurez |
|---|---|
| Propuesta | Se copia lo que hace la competencia |
| Procesos | El proceso digital replica los pasos del manual |
| Datos | Cada iniciativa empieza construyendo su propio conjunto |
| Tecnología | Cualquier cambio exige tocar el núcleo |
| Organización | Un proyecto cruza ocho áreas para decidir |

**La restricción más frecuente es la cuarta.** Un banco con buena tecnología y una organización que
necesita seis meses para aprobar un cambio entrega igual de lento que uno con tecnología antigua.

### 2. El núcleo bancario

El sistema central condiciona todo lo demás, y sus opciones de evolución son pocas. La tabla las compara.

```text
EL PROBLEMA
  · construido hace décadas, funciona y es confiable
  · cada cambio es lento y riesgoso
  · pocas personas lo conocen
  · acopla registro contable, productos, precios y canales

ESTRATEGIAS DE MIGRACIÓN

  REEMPLAZO COMPLETO
    reescribir o comprar y migrar todo
    riesgo muy alto; los fracasos son públicos y caros

  COEXISTENCIA
    núcleo nuevo para productos nuevos,
    antiguo para los existentes
    dos sistemas conviviendo, con reconciliación

  DESACOPLAMIENTO PROGRESIVO
    se extraen capacidades del núcleo una a una
    (precios, productos, límites, canales)
    hasta que el núcleo solo lleva el registro contable

  ENVOLTURA
    se deja el núcleo intacto y se construye
    una capa de servicios sobre él
    rápido y no reduce la deuda técnica
```

| Estrategia | Plazo | Riesgo | Reduce deuda |
|---|---|---|---|
| Reemplazo completo | 4–7 años | Muy alto | Sí |
| Coexistencia | 3–5 años | Alto | Parcial |
| Desacoplamiento progresivo | 3–6 años | Medio | Sí |
| Envoltura | 1–2 años | Bajo | No |

En la práctica las estrategias no se eligen en exclusiva: se combinan dos de
ellas por razones de plazo.

```text
LA COMBINACIÓN HABITUAL Y RAZONABLE
  envoltura para ganar velocidad ahora
  + desacoplamiento progresivo para reducir deuda
  y evitar el proyecto de reemplazo total
```

### 3. Deuda técnica

La deuda técnica se mide y su costo crece con el tiempo. El procedimiento la estima.

```text
QUÉ ES
  el costo futuro de una decisión técnica
  que se tomó por conveniencia presente

  no es un error: es un préstamo
  y como todo préstamo, tiene intereses

SUS INTERESES SE PAGAN EN
  · tiempo adicional de cada cambio
  · incidentes en producción
  · imposibilidad de hacer ciertas cosas
  · dificultad para incorporar personas
```

```text
CÓMO SE GESTIONA
  · se registra: inventario con su costo estimado
  · se prioriza: la que bloquea el negocio primero
  · se asigna capacidad fija: entre 15 % y 25 %
    de la capacidad de entrega, permanentemente
  · se mide: tiempo de entrega, incidentes, cobertura

SIN CAPACIDAD ASIGNADA, LA DEUDA SOLO CRECE
  porque siempre hay algo más urgente
```

### 4. Organización

La organización determina la capacidad de entrega más que la tecnología. La tabla recoge los modelos.

```text
DE PROYECTOS A PRODUCTOS

  PROYECTO                     PRODUCTO
  equipo temporal              equipo estable
  alcance fijo                 evolución continua
  éxito: entregar a tiempo     éxito: el indicador de negocio
  responsabilidad se disuelve  responsabilidad permanente
  el negocio "pide"            el negocio está en el equipo
```

```text
CONDICIONES PARA QUE FUNCIONE
  · el equipo tiene todas las capacidades necesarias
  · el equipo decide dentro de su ámbito, sin comités
  · el equipo responde por un indicador de negocio
  · el equipo es estable en el tiempo
  · el ámbito del equipo coincide con un componente
    técnico que puede cambiar sin coordinar con otros

la última condición es la que más se incumple:
equipos autónomos sobre una arquitectura acoplada
producen coordinación permanente y ninguna autonomía
```

### 5. Medición

La transformación se mide con indicadores de resultado y no de actividad. La tabla los separa.

| Indicador de actividad (evítalo) | Indicador de resultado (úsalo) |
|---|---|
| Iniciativas lanzadas | Operaciones completadas en el canal digital |
| Personas capacitadas | Tiempo de entrega de un cambio a producción |
| Presupuesto ejecutado | Costo por operación |
| Aplicaciones migradas | Incidentes en producción por cambio |
| Usuarios registrados | Usuarios activos que completan operaciones |
| Reuniones de gobierno | Decisiones tomadas por semana |

De la columna derecha hay cuatro indicadores que resisten cualquier intento de
maquillaje, porque miden la capacidad de entrega en si misma.

```text
LOS CUATRO INDICADORES QUE NO SE PUEDEN SIMULAR
  1. tiempo desde la idea hasta producción
  2. frecuencia de despliegue
  3. tasa de fallo de los cambios
  4. tiempo de recuperación ante un incidente

  miden la CAPACIDAD DE ENTREGA de la organización
  y correlacionan con el desempeño del negocio
  mejor que cualquier declaración de estrategia
```

## 🧮 Ejemplo guiado

El ejemplo diagnostica la situación de un banco en las cuatro dimensiones. Conviene mirar la de organización: suele ser la peor y la que menos presupuesto recibe.

**Situación.** Un banco evalúa su programa de transformación tras dos años.

```text
INVERSIÓN EJECUTADA: 18 400 en dos años

RESULTADOS REPORTADOS POR EL PROGRAMA
  · 34 iniciativas lanzadas
  · 12 procesos digitalizados
  · aplicación móvil renovada
  · 1 840 personas capacitadas
  · presupuesto ejecutado: 96 %

INDICADORES DE NEGOCIO
                          hace 2 años    actual
  operaciones digitales      62 %         74 %
  costo por operación         0,0042       0,0038
  índice de eficiencia        58 %         56 %
  tiempo de apertura
    de una cuenta            2 días       4 horas
  tiempo de aprobación
    de un crédito de consumo 3 días       2 días
  usuarios activos mensuales 284 000      342 000
  incidentes críticos/año        14           19
```

**Paso 1 — evalúa si hubo transformación o digitalización.**

```text
APERTURA DE CUENTA: 2 días → 4 horas
  mejora del 92 %
  ¿el proceso se rediseñó?
    antes: formulario, verificación manual, firma, activación
    ahora: formulario en pantalla, verificación automática,
           firma electrónica, activación
  → los MISMOS pasos, ejecutados más rápido
  → DIGITALIZACIÓN bien hecha

CRÉDITO DE CONSUMO: 3 días → 2 días
  mejora del 33 %
  ¿por qué solo eso?
    la solicitud es digital
    la evaluación sigue siendo manual para el 66 % de los casos
    porque el modelo no tiene los datos necesarios
  → el cuello de botella NO era el canal: eran los DATOS
  → se digitalizó lo visible y no se tocó la restricción
```

**Paso 2 — analiza el costo por operación.**

```text
0,0042 → 0,0038: mejora del 9,5 %

  con 74 % de operaciones digitales (era 62 %)
  y un costo digital 8 veces menor que el presencial,
  ¿cuánto DEBERÍA haber bajado?

  costo mixto = 0,62 × d + 0,38 × p, con p = 8d
    0,0042 = 0,62d + 3,04d = 3,66d → d = 0,001148
  esperado con 74 % digital:
    0,74 × 0,001148 + 0,26 × 0,009180 = 0,000849 + 0,002387
    = 0,003236

  esperado: 0,0032    real: 0,0038
  BRECHA: 19 %
```

**Paso 3 — investiga la brecha.**

```text
¿POR QUÉ EL COSTO NO BAJÓ LO ESPERADO?

  · las operaciones migraron al canal digital
    pero la estructura presencial NO se ajustó:
    mismas sucursales, mismo personal
  · las operaciones digitales generan más consultas
    al centro de contacto: 1,8 consultas por cada 10 operaciones
    digitales, frente a 0,4 en presencial
  · los procesos de respaldo siguen siendo manuales:
    el 42 % de las operaciones digitales genera
    una tarea manual en la trastienda

EL TERCER PUNTO ES EL DECISIVO
  se digitalizó el FRENTE y no la TRASTIENDA
  el cliente ve una experiencia digital
  y detrás hay una persona haciendo lo mismo que antes
```

**Paso 4 — evalúa la capacidad de entrega.**

```text
LOS CUATRO INDICADORES QUE NO SE PUEDEN SIMULAR

                            hace 2 años   actual   referencia alta
  tiempo idea → producción     14 semanas   11 sem.    < 2 semanas
  frecuencia de despliegue     mensual      quincenal  diaria
  tasa de fallo de cambios     22 %         26 %       < 15 %
  tiempo de recuperación       8 horas      11 horas   < 1 hora

TRES DE CUATRO EMPEORARON O MEJORARON POCO
  y los incidentes críticos subieron de 14 a 19
```

**Paso 5 — diagnostica la causa.**

```text
SE CONSTRUYERON 34 INICIATIVAS SOBRE UNA ARQUITECTURA
QUE NO SE TOCÓ

  cada iniciativa añadió integraciones al núcleo
  la deuda técnica creció con cada entrega
  → más cambios, más acoplamiento, más fallos

EVIDENCIA
  integraciones directas al núcleo:
    hace 2 años: 84
    actual: 176
  capacidad asignada a deuda técnica: 0 %
```

```text
ESTO EXPLICA LOS TRES INDICADORES QUE EMPEORARON
  el programa entregó funcionalidad
  y consumió capacidad futura para hacerlo
```

**Paso 6 — cuantifica la deuda acumulada.**

```text
INVENTARIO DE DEUDA TÉCNICA
  integraciones punto a punto que deberían
    pasar por una capa de servicios: 92
    costo estimado de remediación: 3 400
  procesos manuales de trastienda: 24
    costo de automatización: 2 800
  componentes sin pruebas automatizadas: 38
    costo: 1 200
  duplicación de datos de cliente en 6 sistemas
    costo de consolidación: 1 900
  TOTAL: 9 300

INTERESES ANUALES QUE SE PAGAN HOY
  sobrecosto de cada cambio (26 % de fallo,
    11 horas de recuperación): 1 240 anuales
  trastienda manual: 42 % de operaciones digitales
    × costo de la tarea manual: 2 180 anuales
  incidentes críticos: 19 × costo medio 68 = 1 292 anuales
  TOTAL: 4 712 anuales
```

**Paso 7 — rediseña el programa.**

```text
REASIGNACIÓN DE LA CAPACIDAD

  ANTES: 100 % en nuevas funcionalidades
  PROPUESTO:
    45 % nuevas funcionalidades
    35 % deuda técnica y automatización de trastienda
    20 % desacoplamiento del núcleo

PRIORIZACIÓN DE LA DEUDA
  1. automatización de trastienda      2 800  → ahorra 2 180/año
  2. capa de servicios sobre el núcleo 3 400  → reduce fallos y tiempo
  3. consolidación de datos de cliente 1 900  → habilita el resto
  4. pruebas automatizadas             1 200  → reduce la tasa de fallo

  las cuatro se pagan solas en 2,0 años
```

```text
CAMBIO ORGANIZATIVO
  · de 34 iniciativas a 9 productos con equipo estable
  · cada producto responde por un indicador de negocio
  · ámbito de cada equipo alineado con un componente
    desacoplado (por eso el punto 2 va antes)
  · capacidad de decisión dentro del equipo
```

**Paso 8 — define la medición del segundo período.**

```text
INDICADORES COMPROMETIDOS A 24 MESES

                            actual   objetivo
  tiempo idea → producción   11 sem.   3 sem.
  frecuencia de despliegue   quincenal semanal
  tasa de fallo de cambios   26 %      14 %
  tiempo de recuperación     11 horas  2 horas
  operaciones con tarea
    manual en trastienda     42 %      12 %
  costo por operación        0,0038    0,0029
  incidentes críticos/año    19        8
  integraciones directas
    al núcleo                176       60

Y SE ELIMINAN DEL REPORTE
  iniciativas lanzadas, personas capacitadas,
  presupuesto ejecutado, aplicaciones migradas
```

**Interpreta:** el programa entregó **34 iniciativas y empeoró la capacidad de entrega de la
organización**. La causa no fue mala ejecución: fue que ninguna capacidad se asignó a lo que no se ve.
La transformación digital que solo construye funcionalidad sobre una arquitectura sin mantener es un
préstamo cuyo interés se paga en velocidad, y la velocidad es exactamente lo que la transformación
pretendía comprar.

## 🏦 Del cliente al banco

El cliente quiere una aplicación que funcione y el banco tiene un sistema central que condiciona lo que puede ofrecer. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Abrir la cuenta fue rápido» | Digitalización bien ejecutada | 14, clase 13 |
| «El crédito sigue tardando días» | El cuello de botella eran los datos | 14, clase 4 |
| «Hice todo en la app y me llamaron igual» | Trastienda manual | 14, clase 13 |
| «La app falla más que antes» | Deuda técnica acumulada | 14, clase 13 |
| «Cada área me pide lo mismo» | Datos de cliente duplicados | 14, clase 4 |

## 🧪 Práctica

El laboratorio pide diagnosticar un banco y priorizar. La prioridad que sale del diagnóstico rara vez es la que el banco tenía.

En `labs/lab-06.md`, sección de transformación:

1. Diagnostica una organización en las cuatro dimensiones.
2. Distingue en diez iniciativas cuáles digitalizan y cuáles transforman.
3. Calcula la brecha entre el costo esperado y el real de una migración de canal.
4. Construye el inventario de deuda técnica con sus intereses anuales.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen transformaciones que no transformaron. Las causas son digitalizar sin rediseñar y no tocar el núcleo.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se digitaliza el proceso existente | No se rediseñó | Pregunta qué pasos ya no hacen falta. |
| Se digitaliza el frente y no la trastienda | El cliente ve digital, detrás hay manual | Mide tareas manuales por operación. |
| Sin capacidad asignada a deuda técnica | Siempre hay algo más urgente | Asigna 15-25 % permanente. |
| Se mide actividad | No dice nada del resultado | Usa indicadores de entrega y de negocio. |
| Equipos autónomos sobre arquitectura acoplada | Coordinación permanente | Desacopla antes de dar autonomía. |
| El canal migra y la estructura no | El ahorro no se materializa | Ajusta la capacidad instalada. |

## ❓ Preguntas de comprobación

1. ¿Qué distingue digitalizar de transformar?
2. ¿Por qué la restricción más frecuente es organizativa y no tecnológica?
3. ¿Por qué la deuda técnica es un préstamo y no un error?
4. ¿Cuáles son los cuatro indicadores que no se pueden simular?
5. ¿Por qué dar autonomía a equipos sobre una arquitectura acoplada no funciona?

## 📥 Entregable

Guarda en `portfolio/parte-14/clase-13/`:

- el diagnóstico en las cuatro dimensiones;
- las diez iniciativas clasificadas entre digitalización y transformación;
- el cálculo de la brecha de costo con su explicación;
- el inventario de deuda técnica con sus intereses anuales y su priorización.

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

- Forsgren, N., Humble, J. y Kim, G. (2018). *Accelerate: The Science of Lean Software and DevOps*. IT Revolution. Los cuatro indicadores de entrega.
- Basel Committee on Banking Supervision (2018). *Sound Practices: Implications of fintech developments for banks and bank supervisors*. BIS. Capacidades que el supervisor espera de un banco que se digitaliza.
- Basel Committee on Banking Supervision (2021). *Principles for Operational Resilience*. BIS. Resiliencia exigible al proceso digitalizado.
- Fowler, M. (2019). *Refactoring* (2.ª ed.). Addison-Wesley. Deuda técnica y su gestión.
- Bank for International Settlements (2021). *Fintech and the digital transformation of financial services*. FSI Insights. Evidencia sobre el alcance real de la transformación digital bancaria.
- Verificación local: revisa las exigencias de tu supervisor sobre gestión de cambios, continuidad operacional y notificación de incidentes tecnológicos.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 12 · Regulación de la tecnología financiera](12-regulacion-de-la-tecnologia-financiera.md) | [Parte 14](../README.md) · [Programa](../../../SYLLABUS.md) | [14 · Estrategia tecnológica →](14-estrategia-tecnologica.md) |
<!-- gen:footer:end -->
