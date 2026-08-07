<!-- meta
part: 22
class: 14
title: "Resiliencia operativa y terceros críticos"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [union-europea, internacional]
regulatory_topics: [resiliencia, externalizacion, continuidad]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [BCBS, CPMI, ESAs]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 14 · Resiliencia operativa y terceros críticos

> [← 13 · Protección de datos y economía de la información](13-proteccion-de-datos-y-economia-de-la-informacion.md) · [Índice de la parte](../README.md) · [15 · Estabilidad financiera y vigilancia macroprudencial →](15-estabilidad-financiera-y-vigilancia.md)

**Parte 22 — Regulación de mercados financieros digitales** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Estudiar el régimen que obliga a **seguir funcionando** y el problema que ninguna
norma de externalización clásica resolvió: cuando veinte entidades dependen del
mismo proveedor, el contrato bilateral de cada una no protege a ninguna.

La clase 13 cerró el bloque de conducta. Esta abre el de resiliencia, y lo hace
retomando un hallazgo que ya apareció dos veces en el programa: el nodo crítico
de la Parte 20, clase 14, y el proveedor común de la Parte 17, clase 2. Aquí lo
miramos desde la norma.

Todo lo regulado hasta aquí tiene que seguir funcionando. Esta clase trata la continuidad desde la norma reciente, que cambió el criterio: ya no se mide la disponibilidad del sistema sino el daño al cliente.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** continuidad de negocio, resiliencia operativa y ciberseguridad.
2. **Identificar** a un tercero crítico y medir la concentración del sector.
3. **Evaluar** un contrato de externalización por sus derechos de salida.
4. **Diseñar** una prueba de resiliencia que demuestre algo.
5. **Explicar** por qué la vigilancia directa del proveedor es la única
   respuesta al riesgo de concentración.

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

Los cuatro primeros términos son la continuidad y sus funciones; los cuatro siguientes, los terceros y su vigilancia. La **tolerancia al impacto** es el concepto que la norma incorporó y que cambia el enfoque: no se trata de recuperar rápido sino de no superar el tiempo tras el cual el daño al cliente es irreversible.

| Concepto | Comprensión verificable |
|---|---|
| `continuidad de negocio` | Capacidad de seguir prestando el servicio |
| `resiliencia operativa` | Capacidad de resistir, adaptarse y recuperarse |
| `función crítica` | Aquella cuya interrupción daña gravemente |
| `tercero crítico` | Proveedor cuyo fallo afecta a muchos a la vez |
| `tolerancia al impacto` | Interrupción máxima admisible por función |
| `estrategia de salida` | Plan para dejar de depender de un proveedor |
| `prueba de resiliencia` | Ejercicio que verifica la capacidad real |
| `vigilancia directa` | Supervisión del proveedor, no solo de la entidad |

## 🧠 Modelo mental

El modelo mental es un cambio de sujeto: la resiliencia deja de medirse por la disponibilidad del sistema y pasa a medirse por el efecto sobre el cliente. Un sistema caído dos horas puede ser aceptable o inadmisible según qué función soporte.

Conviene separar tres cosas que en la práctica se mezclan y que exigen respuestas
distintas.

```text
CONTINUIDAD DE NEGOCIO
  «si algo falla, ¿puedo seguir operando?»
  → planes, respaldos, sitios alternativos

RESILIENCIA OPERATIVA
  «¿cuánta interrupción puede soportar
   cada función antes de causar daño?»
  → tolerancias por función, no por sistema

CIBERSEGURIDAD
  «¿resisto un ataque deliberado?»
  → controles, detección y respuesta

LA SEGUNDA ES LA QUE CAMBIA EL ENFOQUE
  no se pregunta si el sistema está arriba,
  sino cuánto tiempo puede estar abajo
  ESA FUNCIÓN antes de que el daño sea grave
```

El giro es importante. Una entidad puede tener todos sus sistemas con alta
disponibilidad y aun así no ser resiliente, porque nunca se preguntó cuánto
tiempo puede estar sin poder atender una redención antes de que el cliente sufra
un perjuicio irreversible.

## 📖 Desarrollo

### 1. Tolerancia al impacto

La tolerancia se fija por función de negocio y desde la perspectiva del cliente y
del sistema, no desde la del área técnica. Es una decisión del consejo, no del
responsable de sistemas.

```text
PARA CADA FUNCIÓN CRÍTICA

  · ¿qué interrupción máxima es admisible?
  · ¿a partir de qué momento el daño es
    irreversible para el cliente?
  · ¿y para el mercado?

EJEMPLO
  liquidación de operaciones      2 horas
  atención de redenciones         4 horas
  acceso a la aplicación         12 horas
  reporte al supervisor          24 horas

Y LUEGO SE COMPRUEBA SI LA ARQUITECTURA
LO SOSTIENE, no al revés
```

### 2. El tercero crítico

Aquí está el problema que da nombre a la clase. La norma de externalización
clásica supone una relación bilateral: una entidad contrata a un proveedor, y el
contrato le da derechos de auditoría, de información y de salida. Eso funciona
mientras el proveedor sea uno de muchos.

```text
CUANDO VEINTE ENTIDADES DEPENDEN
DEL MISMO PROVEEDOR

  · cada contrato bilateral está bien
  · y ninguno protege del fallo simultáneo
  · el proveedor no está supervisado
  · y ninguna entidad puede exigirle sola
    lo que necesitaría el sector

RESPUESTAS QUE SE HAN INTENTADO
  a  exigir a cada entidad que diversifique
  b  exigir cláusulas contractuales mínimas
  c  designar al proveedor como crítico
     y vigilarlo directamente

LA a NO FUNCIONA cuando solo hay dos
proveedores en el mercado
LA b MEJORA la posición individual y no
el riesgo del conjunto
LA c ES LA ÚNICA QUE ATACA EL PROBLEMA
```

### 3. La estrategia de salida

Un contrato sin salida real no es una externalización: es una dependencia. Y la
mayoría de los contratos tienen cláusula de terminación y ninguna capacidad
efectiva de ejercerla.

```text
QUÉ HACE REAL A UNA ESTRATEGIA DE SALIDA

  · un proveedor alternativo identificado
  · los datos en un formato portable,
    verificado
  · un plazo de migración estimado con
    evidencia, no supuesto
  · el coste presupuestado
  · y una prueba: migrar algo, aunque sea
    un subconjunto

SIN LA ÚLTIMA, LA ESTRATEGIA ES UN
DOCUMENTO Y NO UN PLAN
```

### 4. Pruebas que demuestran algo

Una prueba anunciada, en horario laboral, sobre un entorno de pruebas y con el
proveedor avisado no demuestra resiliencia: demuestra que el procedimiento está
escrito.

```text
GRADIENTE DE PRUEBAS

  1 REVISIÓN DOCUMENTAL     no demuestra nada
  2 SIMULACIÓN DE ESCRITORIO demuestra que se
                             conoce el plan
  3 PRUEBA EN ENTORNO AISLADO demuestra que
                             el procedimiento funciona
  4 CONMUTACIÓN REAL PLANIFICADA demuestra
                             que la arquitectura aguanta
  5 CONMUTACIÓN NO ANUNCIADA demuestra que
                             la organización aguanta

LA MAYORÍA SE QUEDA EN EL NIVEL 2
Y REPORTA HABER PROBADO LA CONTINUIDAD
```

### 5. Registro de dependencias

No se puede gestionar lo que no está inventariado, y el inventario de terceros es
el documento que más rápido envejece de todos.

```text
QUÉ TIENE QUE CONTENER

  · proveedor, servicio y función que soporta
  · si esa función es crítica
  · dónde se prestan los servicios
  · subcontratación, hasta el cuarto nivel
  · derechos de auditoría y de salida
  · fecha de la última prueba

LA SUBCONTRATACIÓN ES LO QUE SE OMITE
  se contrata a A, que subcontrata a B,
  que usa la infraestructura de C
  → y C es el que comparte con las otras
    diecinueve entidades
```

## 🧮 Ejemplo guiado

El ejemplo fija tolerancias al impacto por función y las contrasta con la capacidad real. La brecha es lo que hay que corregir.

**Situación.** Un supervisor mide la concentración de proveedores en su sector y
decide si designa a alguno como crítico.

```text
DATOS DEL SECTOR
  entidades supervisadas                    22
  funciones críticas por entidad             6
  proveedores declarados                    41
```

**Paso 1 — construye el mapa de dependencias.**

```text
DECLARACIÓN INICIAL
  41 proveedores distintos entre 22 entidades
  → parece diversificado

TRAS PEDIR LA SUBCONTRATACIÓN
  · 18 de los 41 usan la infraestructura
    del proveedor C
  · 14 usan el proveedor de precios P1
  · 11 usan el mismo custodio técnico

  → LA DIVERSIFICACIÓN ERA APARENTE
```

**Paso 2 — mide la concentración por función.**

```text
FUNCIÓN: LIQUIDACIÓN

  entidades que dependen de C, directa
  o indirectamente: 19 de 22 = 86,4 %

FUNCIÓN: VALORACIÓN

  dependen de P1: 14 de 22 = 63,6 %

FUNCIÓN: CUSTODIA TÉCNICA

  dependen del mismo: 11 de 22 = 50,0 %

UMBRAL DE DESIGNACIÓN SUPUESTO: 40 %
  → LOS TRES LO SUPERAN
```

**Paso 3 — calcula el efecto de un fallo.**

```text
FALLO DE C DURANTE 6 HORAS

  entidades afectadas                      19
  volumen diario del sector       1 840 000 000
  proporción afectada                    86,4 %
  volumen sin liquidar         1 589 760 000

  y las tolerancias declaradas para
  liquidación son de 2 horas

  → 19 ENTIDADES INCUMPLEN SU PROPIA
    TOLERANCIA A LA VEZ

  y ninguna puede hacer nada: el fallo
  no está en su perímetro
```

**Paso 4 — evalúa la respuesta contractual.**

```text
¿SIRVEN LOS CONTRATOS BILATERALES?

  · 19 entidades con derecho de auditoría
    sobre C
  · si las 19 lo ejercen a la vez, C dedica
    su año a atender auditorías

  · 19 estrategias de salida hacia
    los mismos dos alternativos
  · si las 19 salen a la vez, los
    alternativos no tienen capacidad

  → LOS DERECHOS INDIVIDUALES NO ESCALAN
    AL RIESGO COLECTIVO
```

**Paso 5 — evalúa la diversificación obligatoria.**

```text
EXIGIR QUE CADA ENTIDAD DIVERSIFIQUE

  proveedores con capacidad real: 3
  entidades: 22
  → reparto ideal de 7-8 por proveedor

  COSTE DE MIGRAR UNA ENTIDAD
  supuesto: 240 000 y 9 meses

  para bajar la concentración de C del
  86,4 % al 40 %, migrarían 10 entidades
  10 × 240 000 = 2 400 000 del sector

  Y LA CONCENTRACIÓN RESULTANTE
  seguiría siendo del 40 % en el mayor
```

**Paso 6 — evalúa la designación y la vigilancia directa.**

```text
DESIGNAR A C COMO TERCERO CRÍTICO

  QUÉ HABILITA
  · requerir información directamente
  · inspeccionar sus instalaciones
  · exigir un plan de continuidad del
    servicio al conjunto del sector
  · exigir pruebas de conmutación
  · recomendar que las entidades no
    aumenten su dependencia

  COSTE PARA EL SUPERVISOR
  supuesto: 1,5 personas a tiempo completo
  = 135 000 al año

  COSTE PARA C
  supuesto: 280 000 al año de cumplimiento

  FRENTE A 2 400 000 DE MIGRACIONES
  QUE DEJARÍAN LA CONCENTRACIÓN EN EL 40 %
```

**Paso 7 — decide y combina.**

```text
RECOMENDACIÓN

  1 DESIGNAR a C, P1 y al custodio técnico
    como terceros críticos
    coste 405 000 al año para el supervisor

  2 EXIGIR a las entidades que declaren
    la subcontratación hasta el cuarto nivel
    → el mapa de este ejercicio no existía

  3 NO EXIGIR migración forzosa
    pero sí que ninguna entidad nueva
    aumente la dependencia de C

  4 PRUEBA SECTORIAL ANUAL
    conmutación coordinada, no anunciada,
    de al menos una función

Y UNA CONSTATACIÓN PARA EL INFORME
  las 22 entidades cumplían individualmente
  la norma de externalización. El riesgo
  del conjunto no lo veía ninguna, porque
  ninguna tenía por qué mirarlo.
```

**Interpreta:** cada entidad cumplía su norma y el sector tenía un punto único de
fallo del 86,4 %. **El riesgo no estaba en ningún perímetro individual**, y por
eso la única respuesta proporcionada era supervisar directamente al proveedor en
vez de pedir a veintidós entidades que resolvieran algo que no está en su mano.

## 🧭 Perspectivas

La resiliencia afecta a cada participante de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un servicio caído | Si se va |
| Entidad | Un contrato correcto | Qué exige a su proveedor |
| Proveedor | Diecinueve auditorías | Si acepta la designación |
| Proveedor alternativo | Demanda simultánea | Si amplía capacidad |
| Banco | Dependencia indirecta | Qué declara |
| Supervisor | 86,4 % en un solo punto | Si designa |
| Auditor | Pruebas de nivel 2 | Qué observa |
| Consejo | Tolerancias que no fijó | Cuáles aprueba |
| Sociedad | Un sector que puede parar entero | Qué exige |

## 🏦 Del cliente al banco

El cliente no puede operar y la entidad mide si superó su tolerancia. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Se cayó todo a la vez» | Diecinueve entidades, un proveedor | 22, clase 14 |
| «Tienen plan de continuidad» | Probado sobre papel, nivel 2 | 22, clase 14 |
| «Trabajan con 41 proveedores» | Que usan tres infraestructuras | 22, clase 14 |

## ⚖️ Riesgos y controles

Los riesgos son de terceros críticos y de concentración. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Diversificación aparente | 41 proveedores, 3 infraestructuras | Declarar subcontratación hasta el 4.º nivel |
| Tolerancias fijadas por sistemas | Se mide disponibilidad, no daño | Fijarlas por función, en el consejo |
| Derechos que no escalan | 19 auditorías simultáneas | Vigilancia directa del proveedor |
| Estrategia de salida sin probar | Nadie migró nunca nada | Migrar un subconjunto real |
| Pruebas de nivel 2 | Se reporta haber probado | Conmutación real, y una no anunciada |
| Riesgo fuera de todo perímetro | Ninguna entidad debe mirarlo | Designación de tercero crítico |

## 🧪 Práctica

El laboratorio pide fijar tolerancias y mapear terceros críticos. La concentración por infraestructura, y no por proveedor, es lo que revela el ejercicio.

En [`labs/lab-07.md`](../labs/lab-07.md):

1. Construye el mapa de dependencias con subcontratación.
2. Mide la concentración por función y compárala con un umbral.
3. Compara diversificación forzosa con designación, con sus costes.
4. Diseña la prueba sectorial y su nivel.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen interrupciones con daño irreversible. La causa es la tolerancia fijada con criterio técnico.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Contar proveedores | Es el dato declarado | Cuenta infraestructuras |
| Tolerancia por sistema | La fija el área técnica | Se fija por función y en el consejo |
| Confiar en el contrato | Está bien redactado | No escala al riesgo colectivo |
| Salida sin probar | Migrar es caro | Migra un subconjunto |
| Reportar pruebas de escritorio | Cumplen el requisito | Declara el nivel de la prueba |
| Esperar que la entidad lo resuelva | Es su proveedor | El riesgo está fuera de su perímetro |

## ❓ Preguntas de comprobación

1. ¿Qué diferencia hay entre continuidad, resiliencia operativa y
   ciberseguridad?
2. ¿Por qué la tolerancia al impacto cambia el enfoque?
3. ¿Por qué los contratos bilaterales no resuelven el riesgo de concentración?
4. ¿Qué hace real a una estrategia de salida?
5. ¿Qué nivel de prueba demuestra que la organización aguanta?

## 📥 Entregable

Guarda en `portfolio/parte-22/clase-14/`:

- el mapa de dependencias con subcontratación hasta el cuarto nivel;
- la concentración por función frente al umbral;
- la comparación entre diversificación y designación, con costes;
- la prueba sectorial diseñada, con su nivel declarado.

## 🔗 Referencias cruzadas

- **Viene de:** clases 10 y 13; Parte 17, clase 2; Parte 20, clase 14.
- **Continúa en:** clase 15 de esta parte.
- **Se aplica en:** clase 18 de esta parte; Parte 23, clase 15.

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

- Basel Committee on Banking Supervision (2021). *Principles for Operational Resilience*. BIS. <https://www.bis.org/bcbs/publ/d516.htm>
- Basel Committee on Banking Supervision (2021). *Revisions to the Principles for the Sound Management of Operational Risk*. BIS. <https://www.bis.org/bcbs/publ/d515.htm>
- Diario Oficial de la Unión Europea (2022). *Reglamento (UE) 2022/2554 sobre la resiliencia operativa digital del sector financiero*. EUR-Lex. <https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32022R2554>
- Financial Stability Board (2020). *Effective Practices for Cyber Incident Response and Recovery*. FSB. <https://www.fsb.org/2020/10/effective-practices-for-cyber-incident-response-and-recovery-final-report/>
- Verificación local: comprueba si tu jurisdicción prevé la designación de terceros críticos, qué umbral aplica y qué obligaciones de declaración de subcontratación impone. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 13 · Protección de datos y economía de la información](13-proteccion-de-datos-y-economia-de-la-informacion.md) | [Parte 22](../README.md) · [Programa](../../../SYLLABUS.md) | [15 · Estabilidad financiera y vigilancia macroprudencial →](15-estabilidad-financiera-y-vigilancia.md) |
<!-- gen:footer:end -->
