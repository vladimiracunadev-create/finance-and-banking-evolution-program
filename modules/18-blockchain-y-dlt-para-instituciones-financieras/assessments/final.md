# Evaluación final: Blockchain y DLT para instituciones financieras

## Instrucciones

Responde sin consultar las soluciones de los laboratorios. Puedes usar las
clases y las fuentes oficiales. Declara los supuestos que necesites: un supuesto
explícito suma; uno oculto resta.

**Puntaje total:** 100 puntos. **Aprobación:** 70. **Tiempo sugerido:** 3 horas.

## Sección A — Fundamentos y criterio (25 puntos)

**1.** (8 pts) Aplica las seis preguntas de la clase 1 a este caso: cuatro
aseguradoras quieren compartir un registro de siniestros para detectar
duplicidades. Indica cuál justifica un registro distribuido y por qué.

**2.** (7 pts) Explica por qué el encadenamiento de bloques no impide reescribir la
historia, y qué dos cosas sí lo impiden.

**3.** (5 pts) Clasifica estas tres redes por los dos ejes de la clase 7 e indica
qué obligación bancaria hace inviable cada configuración:
a) lectura abierta, escritura abierta; b) lectura restringida, validación por un
único proveedor; c) lectura restringida, validación rotatoria entre 8.

**4.** (5 pts) Un consorcio afirma que su red «no tiene terceros de confianza» y usa
un oráculo de precios. Explica la contradicción y di qué sería correcto afirmar.

## Sección B — Cálculo y diseño (30 puntos)

**5.** (10 pts) Una red autorizada tiene 10 nodos.

- **a)** Calcula `f` para consenso bizantino.
- **b)** Si 6 de los 10 ejecutan la misma implementación, ¿qué fallo no cubre `f`?
- **c)** Propón una configuración de 10 nodos que sí lo cubra, y di qué riesgo
  nuevo introduce tu propuesta.

**6.** (10 pts) Un registro produce bloques de 120 KB cada 3 segundos.

- **a)** Calcula el crecimiento anual en el peor caso.
- **b)** Con retención de 7 años y 30 TB por nodo, ¿cabe?
- **c)** Si además hay que responder «¿cuál era el estado el día X?», ¿qué
  diseño propones y cuánto ocupa?

**7.** (10 pts) Un esquema 4-de-9 reparte guardianes así: 3 en la ubicación A con
proveedor P1, 3 en B con P1, 3 en C con P2.

- **a)** ¿Cuántas pérdidas independientes tolera?
- **b)** ¿Qué ocurre si falla P1?
- **c)** Rediseña el reparto para tolerar el fallo de cualquier proveedor.

## Sección C — Contratos y oráculos (20 puntos)

**8.** (7 pts) Escribe el código defectuoso de una retirada con reentrada, explica
el ataque paso a paso y muestra la corrección.

**9.** (7 pts) Un oráculo usa la media de 4 fuentes. Calcula cuántas fuentes hay que
comprometer para mover el valor un 15 %, con media y con mediana, y explica la
diferencia.

**10.** (6 pts) Enumera cinco cosas que deben quedar **fuera** del código de un
contrato y la regla que lo decide.

## Sección D — Finalidad y gobernanza (15 puntos)

**11.** (8 pts) Una red con consenso bizantino y finalidad determinística no está
designada como sistema de pagos. Un banco quiere contabilizar sus operaciones
como firmes. Redacta la respuesta al asesor jurídico, con su fundamento.

**12.** (7 pts) Ocurre un defecto que permite retirar fondos indebidamente. Describe
los tres primeros pasos del plan de recuperación y explica por qué el primero
**no** es corregir el defecto.

## Sección E — Decisión (10 puntos)

**13.** (10 pts) Tu equipo ha construido una red autorizada que funciona. El comité
pregunta por qué no una base de datos compartida operada por una sociedad
conjunta. Escribe la respuesta que darías, incluyendo la posibilidad de que la
respuesta correcta sea «tenéis razón».

## Rúbrica

| Sección | Peso | Criterio de logro |
|---|---:|---|
| A — Fundamentos y criterio | 25 | Aplica el criterio, no repite definiciones |
| B — Cálculo y diseño | 30 | Números correctos y riesgo nuevo identificado |
| C — Contratos y oráculos | 20 | Describe el ataque, no solo el control |
| D — Finalidad y gobernanza | 15 | Distingue lo técnico de lo jurídico |
| E — Decisión | 10 | Admite que la respuesta puede ser negativa |

## Escala

- 0–49: reforzar fundamentos; repetir clases 1 a 6 y laboratorios 1 y 4.
- 50–69: comprensión parcial; rehacer el laboratorio donde perdiste más puntos.
- 70–84: logro esperado; puedes iniciar el proyecto.
- 85–100: dominio destacado; puedes actuar como revisor de otros proyectos.

## Guía de corrección y retroalimentación

**Pregunta 1.** Solo la pregunta de **confianza** justifica por sí sola un registro
distribuido. Y hay que preguntar por un **tercero neutral**, no por un
participante: si las cuatro aseguradoras aceptarían una entidad conjunta con
gobierno paritario, la respuesta es que no hace falta.

**Pregunta 5a.** `f = ⌊(10−1)/3⌋ = 3`.

**Pregunta 5b.** Un defecto de la implementación mayoritaria afecta a 6 > 3: el
umbral no lo cubre. Es un fallo común, no un fallo bizantino independiente.

**Pregunta 5c.** Se espera una configuración con al menos 3 implementaciones
repartidas de forma que ninguna alcance 4 nodos, y el riesgo nuevo es la
**bifurcación** si dos implementaciones interpretan una regla de forma distinta.
Quien no mencione ese riesgo obtiene la mitad del apartado.

**Pregunta 6a.** 31 536 000 / 3 = 10 512 000 bloques × 120 KB ≈ **1,26 TB al año**.

**Pregunta 6b.** 7 × 1,26 = 8,82 TB < 30 TB: **sí cabe**.

**Pregunta 6c.** Se espera **instantáneas periódicas** más reejecución, con el
cálculo de su volumen. Un nodo archivo que guarde el estado tras cada bloque no
es viable, y decirlo forma parte de la respuesta.

**Pregunta 7a.** Tolera 5 pérdidas independientes (9 − 4).

**Pregunta 7b.** Si falla P1 se pierden 6 guardianes y quedan 3 < 4: **no se puede
firmar**.

**Pregunta 7c.** Se espera 3+3+3 con tres proveedores distintos, de modo que el
fallo de cualquiera deje 6 ≥ 4.

**Pregunta 9.** Con media de 4 fuentes, mover el valor un 15 % exige que una
fuente publique un 60 % de desviación: **una fuente**. Con mediana, hacen falta
**3 de 4**. Quien no explique que la media es manipulable con un solo valor
extremo obtiene la mitad.

**Pregunta 11.** La respuesta correcta es **no**: la finalidad determinística es una
propiedad del protocolo sujeta a su supuesto de seguridad, y la protección frente
a un concurso la da la designación del sistema. Se valora que la respuesta
proponga qué hacer mientras tanto.

**Pregunta 12.** El primer paso es **parar**. Corregir el defecto con el incidente
en curso alarga la exposición; parar la detiene. Quien ponga «corregir» primero
obtiene cero en el apartado.

**Pregunta 13.** Se valora explícitamente la disposición a concluir que la
alternativa simple es mejor. Una respuesta que solo defiende lo construido, por
bien argumentada que esté, obtiene como máximo la mitad.
