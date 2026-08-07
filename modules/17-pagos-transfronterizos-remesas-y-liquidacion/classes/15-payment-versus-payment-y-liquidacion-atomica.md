<!-- meta
part: 18
class: 15
title: "Payment versus Payment y liquidación atómica"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global]
regulatory_topics: [cross-border-payments, liquidacion, riesgo-de-liquidacion]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [CPMI, Comité de Basilea]
requires_legal_review: false
-->

<!-- gen:header:start -->
# Clase 15 · Payment versus Payment y liquidación atómica

> [← 14 · Stablecoins y pagos internacionales](14-stablecoins-y-pagos-internacionales.md) · [Índice de la parte](../README.md) · [16 · Proyecto: red de pagos transfronterizos →](16-proyecto-red-de-pagos-transfronterizos.md)

**Parte 18 — Pagos transfronterizos, remesas y liquidación internacional** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Estudiar el mecanismo que elimina el riesgo Herstatt: **ninguna pata se liquida
si la otra no se liquida**. Y entender qué cuesta esa garantía, porque no es
gratis.

La clase 7 identificó el riesgo de liquidación y la 8 lo acotó con liquidez. Esta lo elimina, condicionando cada tramo al otro, y delimita con precisión qué riesgo desaparece y cuál queda.

## 📚 Objetivos

Al finalizar podrás:

1. **Explicar** el pago contra pago y qué riesgo elimina exactamente.
2. **Distinguir** atomicidad, condicionalidad y simultaneidad.
3. **Calcular** la exposición de liquidación de una cartera de operaciones.
4. **Comparar** las arquitecturas que ofrecen liquidación condicional.
5. **Identificar** qué riesgos siguen existiendo después del pago contra pago.

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

Los tres primeros términos son los mecanismos de condicionalidad; los cinco siguientes, sus requisitos y su efecto. La **atomicidad** es la propiedad que elimina el riesgo de principal: o se ejecutan los dos tramos o no se ejecuta ninguno, y no existe estado intermedio.

| Concepto | Comprensión verificable |
|---|---|
| `pago contra pago` | Mecanismo por el que una pata solo se liquida si la otra también |
| `entrega contra pago` | Equivalente para valores contra efectivo |
| `atomicidad` | Las dos patas ocurren enteras o no ocurre ninguna |
| `condicionalidad` | La ejecución depende de que se cumpla una condición verificable |
| `simultaneidad` | Que ambas ocurran en el mismo instante |
| `exposición de liquidación` | Importe en riesgo entre entregar y recibir |
| `sincronización` | Coordinación de dos liquidaciones en sistemas distintos |
| `liquidación neta con garantía` | Neteo con fondo que cubre el fallo de un participante |

## 🧠 Modelo mental

El modelo mental es una condición mutua: cada tramo solo se ejecuta si el otro también lo hace. Lograrlo exige que ambos tramos estén bajo el control del mismo mecanismo, y eso no siempre es posible entre jurisdicciones.

```text
EL RIESGO QUE SE ELIMINA ES MUY CONCRETO

  SIN PAGO CONTRA PAGO
    banco A entrega euros a las 10:00 en Fráncfort
    banco B debe entregar dólares a las 15:00 en Nueva York
    entre las 10:00 y las 15:00, A tiene el 100 %
    del importe en riesgo frente a B

  CON PAGO CONTRA PAGO
    ninguna entrega ocurre hasta que ambas pueden ocurrir
    exposición: 0

TRES PALABRAS QUE NO SON SINÓNIMAS

  ATOMICIDAD     o las dos, o ninguna
  CONDICIONALIDAD  una ocurre SI se verifica algo
  SIMULTANEIDAD  ocurren en el mismo instante

  el pago contra pago exige ATOMICIDAD.
  La simultaneidad es una forma de conseguirla,
  no la única.
```

## 📖 Desarrollo

### 1. Cómo se consigue la atomicidad

```text
MECANISMO 1 · LIQUIDADOR CENTRAL
  ambas patas se liquidan en los libros de una entidad
  que tiene las dos divisas
  → atomicidad por construcción: es un asiento único
  → exige que ambos participen y prefinancien

MECANISMO 2 · BLOQUEO Y CONFIRMACIÓN
  cada sistema BLOQUEA los fondos de su pata
  un coordinador comprueba que ambos bloqueos existen
  y ordena la liberación
  → atomicidad por protocolo
  → exige un coordinador de confianza y manejo del fallo

MECANISMO 3 · LIQUIDACIÓN EN UNA PLATAFORMA COMÚN
  ambas patas viven en el mismo registro programable
  → atomicidad por ejecución conjunta
  → exige que ambos activos estén en la plataforma

EL PROBLEMA COMÚN DE LOS TRES
  ¿qué pasa si el coordinador o el liquidador falla
  DESPUÉS de bloquear y ANTES de liberar?
  → hay que definir el procedimiento de desbloqueo
    y su plazo, o el remedio es peor que la enfermedad
```

### 2. Exposición de liquidación

```text
FÓRMULA
  exposición = importe × tiempo entre entregar y recibir

MEDIDA EN UNA CARTERA
  se suman las exposiciones vivas en cada instante
  y se toma el máximo del día

EJEMPLO
  operación 1: 40 M, entrega 09:00, recibe 15:00
  operación 2: 25 M, entrega 10:00, recibe 15:00
  operación 3: 30 M, entrega 14:00, recibe 15:00

  exposición máxima (14:00–15:00): 95 M
  y NO 40 M, que es el mayor individual

POR QUÉ IMPORTA
  el límite de contraparte se consume por la exposición
  MÁXIMA SIMULTÁNEA, no por el importe de la mayor
```

### 3. Qué no elimina el pago contra pago

```text
ELIMINA
  el riesgo de entregar y no recibir

NO ELIMINA
  · riesgo de REPOSICIÓN: si la operación no se liquida,
    hay que rehacerla al precio de mercado del momento
  · riesgo de LIQUIDEZ: los fondos bloqueados no se pueden
    usar mientras dure el bloqueo
  · riesgo OPERACIONAL del coordinador
  · riesgo LEGAL: ¿el bloqueo es oponible en una quiebra?
  · riesgo de CONCENTRACIÓN en el liquidador central

EL ÚLTIMO ES EL MÁS IMPORTANTE
  un mecanismo que elimina el riesgo bilateral
  lo concentra en una sola entidad.
  Esa entidad pasa a ser sistémica.
```

### 4. Liquidación atómica en plataformas programables

```text
LA PROMESA
  si ambos activos viven en el mismo registro,
  una sola ejecución transfiere los dos
  → atomicidad sin coordinador externo

LAS CONDICIONES QUE HAY QUE CUMPLIR
  1. ambos activos deben estar representados
     en la misma plataforma
  2. la representación debe ser oponible
     jurídicamente: transferir el token
     tiene que transferir el derecho
  3. la plataforma debe dar finalidad
     reconocida por la norma aplicable
  4. debe haber un procedimiento si la ejecución falla
     a medias por un defecto del propio código

LO QUE SE ESTUDIA EN LA PARTE 21
  la condición 2 es la difícil, y es jurídica,
  no técnica
```

### 5. Sincronización sin plataforma común

```text
UNA VÍA INTERMEDIA
  no hace falta que los dos activos vivan en el mismo
  registro: basta un mecanismo que ORDENE a dos
  sistemas distintos liquidar solo si ambos pueden

  · cada sistema reserva
  · el sincronizador comprueba
  · ambos liquidan, o ninguno libera

VENTAJA
  no exige migrar nada: los sistemas nacionales
  siguen siendo los mismos

DIFICULTAD
  el sincronizador necesita conexión, confianza
  y reglas en ambos sistemas; y el plazo de reserva
  consume liquidez mientras dura

  varios proyectos institucionales han explorado
  esta vía; verifica su estado en la fuente
  antes de citarlos como operativos
```

## 🧮 Ejemplo guiado

El ejemplo calcula la exposición de liquidación con y sin pago contra pago. La reducción es completa en el riesgo de principal y no en el de reposición.

**Situación.** Un banco mide su exposición de liquidación en operaciones de
cambio y evalúa si vale la pena entrar en un mecanismo de pago contra pago.

```text
OPERACIONES DE CAMBIO DEL DÍA TÍPICO
  número de operaciones                          180
  valor nocional total                    1 240 M USD
  operaciones ya liquidadas con PvP           38 %
  operaciones bilaterales                     62 %

DE LAS BILATERALES
  valor                                     768,8 M USD
  exposición máxima simultánea               412 M USD
  duración media de la exposición            5,8 horas

CONTRAPARTES BILATERALES: 22
CONCENTRACIÓN: las 3 mayores suman el 54 % de la exposición

COSTE DE ENTRAR EN EL MECANISMO PvP
  cuota anual                              240 000 USD
  coste por operación                          1,20 USD
  prefinanciación adicional requerida       85 M USD
  coste de esa prefinanciación (4,1 %)   3 485 000 USD/año
```

**Paso 1 — calcula el coste de entrar.**

```text
CUOTA                              240 000
OPERACIONES: 180 × 62 % × 250 días = 27 900
COSTE POR OPERACIÓN: 27 900 × 1,20 = 33 480
PREFINANCIACIÓN                  3 485 000
TOTAL ANUAL                      3 758 480 USD
```

**Paso 2 — calcula el beneficio en pérdida esperada.**

```text
PÉRDIDA ESPERADA SIN PvP
  exposición máxima simultánea: 412 M
  probabilidad de fallo de una contraparte
  en el día: supongamos 0,004 % (dato del ejercicio)
  severidad: 100 % del importe expuesto

  412 000 000 × 0,004 % = 16 480 USD/día
  × 250 días = 4 120 000 USD/año

BENEFICIO: 4 120 000 USD
COSTE:     3 758 480 USD
MARGEN:      361 520 USD  → conviene, por poco
```

**Paso 3 — desconfía del número que decide.**

```text
EL RESULTADO DEPENDE DE UNA PROBABILIDAD INVENTADA

  con 0,002 %:  beneficio 2 060 000 → NO conviene
  con 0,004 %:  beneficio 4 120 000 → conviene por poco
  con 0,010 %:  beneficio 10 300 000 → conviene claramente

  → la decisión NO se sostiene sobre este cálculo
```

**Paso 4 — busca el argumento que no depende de esa cifra.**

```text
EL CAPITAL REGULATORIO

  la exposición de liquidación consume capital
  bajo el marco prudencial, y ese consumo es
  un dato del banco, no un supuesto

  DATO
    capital asignado a riesgo de liquidación
    en cambios: 28,4 M USD
    coste de ese capital al 11 %: 3 124 000 USD/año

    con PvP, la exposición cae drásticamente
    liberación estimada de capital: 74 %
    ahorro: 3 124 000 × 74 % = 2 311 760 USD/año

BENEFICIO TOTAL RECALCULADO
  pérdida esperada evitada (escenario central) 4 120 000
  coste de capital liberado                    2 311 760
  TOTAL                                        6 431 760
  COSTE                                        3 758 480
  MARGEN                                       2 673 280 USD

Y AHORA EL RESULTADO ES ROBUSTO
  incluso con la probabilidad más baja (0,002 %):
  2 060 000 + 2 311 760 − 3 758 480 = 613 280 USD
```

**Paso 5 — analiza la concentración.**

```text
LAS 3 MAYORES CONTRAPARTES SUMAN EL 54 %

  ¿QUÉ PASA SI SOLO ESAS TRES ENTRAN EN PvP?
    exposición cubierta: 412 M × 54 % = 222,5 M
    exposición residual: 189,5 M

  COSTE DE ESA OPCIÓN
    la prefinanciación no es proporcional:
    el mecanismo exige un mínimo
    supuesto: 60 M en vez de 85 M
    coste: 2 460 000 + cuota 240 000 + operaciones 18 000
         = 2 718 000 USD

  BENEFICIO
    pérdida esperada evitada: 4 120 000 × 54 % = 2 224 800
    capital liberado: 2 311 760 × 54 % = 1 248 350
    TOTAL: 3 473 150
    MARGEN: 755 150 USD

  MENOR MARGEN ABSOLUTO, MENOR RIESGO DE EJECUCIÓN
```

**Paso 6 — considera lo que el PvP no resuelve.**

```text
QUEDA EL RIESGO DE REPOSICIÓN

  si una contraparte falla, la operación no se liquida
  y hay que rehacerla al precio del momento

  con volatilidad diaria del 0,7 % y exposición
  nocional de 768,8 M:
    pérdida potencial por reposición si falla
    una contraparte del 20 % del volumen:
    153,8 M × 0,7 % ≈ 1 076 000 USD

  → el PvP protege el PRINCIPAL, no el precio
  → sigue haciendo falta límite por contraparte
    y gestión de la exposición de reposición

Y QUEDA EL RIESGO DE CONCENTRACIÓN
  al entrar en el mecanismo, el banco pasa a depender
  de una infraestructura única
  → hay que tener procedimiento de contingencia
    si esa infraestructura falla
```

**Paso 7 — decide.**

```text
ENTRAR CON EL ALCANCE COMPLETO, NO PARCIAL

  MOTIVOS
    1. el margen es 3,5 veces mayor (2,67 M frente a 0,76 M)
    2. el resultado es robusto a la probabilidad de fallo
       gracias al capital liberado, que es un dato
    3. entrar parcialmente deja 189,5 M de exposición
       residual que sigue consumiendo capital y límite

  CONTROLES QUE ACOMPAÑAN
    · límite de contraparte por exposición de reposición,
      que el PvP no cubre
    · procedimiento de contingencia si el mecanismo falla
    · seguimiento de la prefinanciación: 85 M es liquidez
      inmovilizada que hay que gestionar (clase 8)
    · revisión anual del coste frente al capital liberado

  Y UNA NOTA DE MÉTODO
    el análisis cambió de signo al sustituir un supuesto
    inventado por un dato del propio banco.
    Cuando una decisión depende de una probabilidad
    que nadie puede estimar, hay que buscar el argumento
    que no dependa de ella.
```

**Interpreta:** el primer cálculo daba un margen pequeño sobre una probabilidad
inventada. El segundo se apoyó en **el capital que el banco ya tiene asignado**,
que es un dato verificable, y el resultado pasó a ser robusto. Cambiar el
argumento por uno medible fue más útil que refinar la estimación.

## 🧭 Perspectivas

El mecanismo afecta a cada participante de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Tesorería | 85 M inmovilizados | Cómo los financia |
| Riesgo de contraparte | 412 M de exposición | Qué límites fija |
| Capital | 28,4 M asignados | Si se libera |
| Contraparte | El banco exige PvP | Si entra también |
| Liquidador central | Concentración sistémica | Su propia resiliencia |
| Banco central | Riesgo Herstatt del sistema | Si promueve el mecanismo |
| Supervisor | Exposición de liquidación | Qué exige medir |

## 🏦 Del cliente al banco

El cliente no lo ve y su banco elimina o no un riesgo que puede costarle el importe entero. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Mi operación se liquidó sin incidencias» | Atomicidad: o las dos patas o ninguna | 18, clase 15 |
| «Me cobran más por operar en esa divisa» | Coste de prefinanciar el mecanismo | 18, clases 8 y 15 |
| «El banco no opera con esa contraparte» | Límite por exposición de reposición | 18, clase 15 |

## ⚖️ Riesgos y controles

Los riesgos residuales son de sincronización y de reposición. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Riesgo de reposición | La operación no se liquida y el precio se movió | Límite por contraparte, independiente del PvP |
| Concentración en el liquidador | El mecanismo falla | Procedimiento de contingencia |
| Liquidez inmovilizada | La prefinanciación crece | Gestión activa del saldo |
| Bloqueo sin liberación | El coordinador falla a medias | Plazo y procedimiento de desbloqueo |
| Riesgo legal del bloqueo | No es oponible en quiebra | Verificación jurídica por jurisdicción |
| Decidir con una probabilidad inventada | El resultado cambia de signo | Buscar el argumento medible |

## 🧪 Práctica

El laboratorio pide medir la exposición de liquidación con y sin el mecanismo. La diferencia es el riesgo de principal, y verlo en cifras justifica el coste.

En [`labs/lab-07.md`](../labs/lab-07.md):

1. Calcula la exposición máxima simultánea de una cartera de operaciones.
2. Implementa la liquidación condicional con bloqueo y confirmación.
3. Simula el fallo del coordinador entre el bloqueo y la liberación.
4. Compara el coste de entrar en un mecanismo con el capital que libera.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen exposiciones de liquidación no gestionadas. La causa es suponer simultaneidad donde no la hay.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| «PvP elimina el riesgo» | Se ignoró la reposición | Protege el principal, no el precio |
| Exposición = mayor operación | No se sumaron las simultáneas | Máximo simultáneo |
| Atomicidad = simultaneidad | Se confundieron los términos | La simultaneidad es un medio |
| Ignorar el coste de prefinanciar | Solo se miró la cuota | Es el componente mayor |
| Decidir con una probabilidad supuesta | No había dato | Usa el capital asignado |
| Sin plan si el mecanismo falla | Se asumió disponible | Contingencia obligatoria |

## ❓ Preguntas de comprobación

1. ¿Qué riesgo elimina exactamente el pago contra pago y cuál no?
2. ¿Qué diferencia hay entre atomicidad, condicionalidad y simultaneidad?
3. ¿Por qué la exposición se mide como máximo simultáneo?
4. ¿Qué riesgo nuevo introduce un liquidador central?
5. En el ejemplo guiado, ¿por qué el segundo cálculo era más sólido que el
   primero?

## 📥 Entregable

Guarda en `portfolio/parte-18/clase-15/`:

- el cálculo de exposición máxima simultánea de una cartera;
- la implementación de la liquidación condicional y su prueba de fallo;
- la comparación de coste frente a capital liberado;
- la lista de riesgos que persisten tras el pago contra pago, con su control.

## 🔗 Referencias cruzadas

- **Viene de:** clases 7, 8 y 9; Parte 11, clase 7 (riesgo de contraparte).
- **Continúa en:** clase 16 (proyecto); **Parte 21, clase 15** (DvP, PvP y
  liquidación atómica en mercados tokenizados).
- **Se aplica en:** Parte 23, clase 14.

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

- Committee on Payments and Market Infrastructures e IOSCO (2012). *Principles for Financial Market Infrastructures*, principio 12. BIS. <https://www.bis.org/cpmi/publ/d101.htm>
- Basel Committee on Banking Supervision (2013). *Supervisory guidance for managing risks associated with the settlement of foreign exchange transactions*. BIS. <https://www.bis.org/publ/bcbs241.htm>
- Committee on Payments and Market Infrastructures (2008). *Progress in reducing foreign exchange settlement risk*. BIS. <https://www.bis.org/cpmi/publ/d83.htm>
- BIS Innovation Hub. *Proyectos sobre liquidación con pago contra pago y sincronización*. BIS. <https://www.bis.org/about/bisih/topics.htm>
- Global Foreign Exchange Committee. *FX Global Code*, principios sobre gestión del riesgo de liquidación. <https://www.globalfxc.org/fx_global_code.htm>
- Verificación local: comprueba cómo se trata la exposición de liquidación en el marco prudencial aplicable y si el bloqueo de fondos es oponible en las jurisdicciones donde operes. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 14 · Stablecoins y pagos internacionales](14-stablecoins-y-pagos-internacionales.md) | [Parte 18](../README.md) · [Programa](../../../SYLLABUS.md) | [16 · Proyecto: red de pagos transfronterizos →](16-proyecto-red-de-pagos-transfronterizos.md) |
<!-- gen:footer:end -->
