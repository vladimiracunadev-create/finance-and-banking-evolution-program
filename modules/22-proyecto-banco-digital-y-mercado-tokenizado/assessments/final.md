# Evaluación final: Proyecto de banco digital y mercado tokenizado

## Instrucciones

Responde sin consultar las soluciones de los laboratorios. Puedes usar las clases
de todo el programa y las fuentes oficiales. Declara los supuestos que necesites:
un supuesto explícito suma; uno oculto resta.

Esta evaluación cierra el programa, y por eso califica algo distinto de las
veintidós anteriores. **No se evalúa si sabes cada tema, sino si sostienes un
sistema completo ante alguien que va a buscar dónde se contradice.** Una respuesta
técnicamente impecable que ignore lo que decidiste tres secciones antes puntúa
menos que una respuesta modesta y coherente. Lo que se mide es el conjunto.

**Puntaje total:** 100 puntos. **Aprobación:** 70. **Tiempo sugerido:** 4 horas.

## Sección A — Alcance y arquitectura (25 puntos)

**1.** (9 pts) Un equipo propone doce funciones para un banco digital dirigido a
1 800 pymes importadoras.

- **a)** Aplica las cuatro preguntas y determina cuáles no aportan.
- **b)** Calcula la carga regulatoria de las incluidas y la facturación necesaria
  con un margen del 22 %.
- **c)** Di qué harías si esa facturación excede el mercado direccionable.

**2.** (8 pts) El equipo debe decidir sobre cuatro componentes: núcleo de cuentas,
motor de cambio, decisión de crédito y registro de colateral.

- **a)** Aplica el análisis de construir, integrar o comprar.
- **b)** Identifica en cuál la salida manda sobre el coste y justifícalo.
- **c)** Un proveedor sirve al 78 % del sector. Explica por qué integrarlo es
  racional para la entidad e irracional para el sistema.

**3.** (8 pts) Aplica las seis preguntas del registro distribuido al sistema
propuesto. Si ninguna lo justifica, escribe la arquitectura alternativa y di qué
se pierde. Si alguna lo justifica, di cuál y por qué.

## Sección B — Perímetro del propio sistema (15 puntos)

**4.** (8 pts) El sistema guarda las claves del colateral, ordena las opciones de
crédito en pantalla y convierte divisas con margen propio.

- **a)** Enumera los regímenes que activa cada hecho de diseño.
- **b)** Para cada uno, di si lo asumirías o ajustarías el diseño.
- **c)** Formula el criterio que distingue un ajuste legítimo de uno que perjudica
  al cliente.

**5.** (7 pts) Califica un depósito tokenizado y un bono tokenizado con los cuatro
criterios, y di qué consecuencia tiene cada calificación sobre el alcance.

## Sección C — Construcción y prueba (30 puntos)

**6.** (10 pts) Diseña la liquidación atómica de colateral contra depósito
tokenizado.

- **a)** Escribe la secuencia con el rechazo previo al bloqueo.
- **b)** Enumera las cinco pruebas de modos de fallo, incluida la del registro
  detenido.
- **c)** Calcula el ahorro neto restando el coste de liquidez y el del fallo del
  ciclo completo. Comenta el resultado.

**7.** (10 pts) El esquema de claves propuesto es 3-de-5 con tres partes en la
oficina central y todas en el mismo dispositivo.

- **a)** Calcula la independencia efectiva.
- **b)** Redistribuye sin cambiar el umbral y vuelve a calcularla.
- **c)** El colateral está delegado en un custodio cuyo contrato no incluye la
  prohibición de disponer. Cuantifica la exposición sobre 24 000 000 con una
  recuperación ordinaria del 18 %.

**8.** (10 pts) El sistema opera un día completo con 420 operaciones, seis llamadas
de margen, un pago de intereses con aprovisionamiento insuficiente en 1 500, una
orden judicial de embargo y un corte de red de 40 minutos.

- **a)** Di qué ocurre con el pago de intereses y por qué.
- **b)** Identifica dos tensiones de diseño entre decisiones previas.
- **c)** Resuelve cada una declarando qué se sacrifica y cuantificándolo.

## Sección D — Amenazas, tensión y resolución (20 puntos)

**9.** (7 pts) Aplica el criterio del atacante racional al sistema con 91 200 000 en
saldos y 24 000 000 en colateral. Di dónde está el mayor valor detrás del control
más débil y qué prueba ejecutable asociarías a ese control.

**10.** (7 pts) Un banco corresponsal emite el depósito, liquida los pagos y
custodia efectivo.

- **a)** Explica por qué eso convierte tres dependencias en una.
- **b)** Construye el escenario y di a cuántas desviaciones de un día normal está
  el punto de rotura con una volatilidad diaria del 1,8 % y una caída del 9 %.
- **c)** Declara el nivel de prueba alcanzado en el gradiente de cinco.

**11.** (6 pts) Diseña el plan de resolución ordenada con sus seis elementos y di
cómo probarías que funciona antes de necesitarlo.

## Sección E — Defensa (10 puntos)

**12.** (5 pts) Cruza dos parejas críticas del expediente y escribe el hallazgo que
aparece en cada una. Prioriza los dos por nivel y clientes afectados.

**13.** (5 pts) Escribe la sección de límites del sistema: al menos cinco cosas que
no puede hacer, cada una con la razón concreta por la que no puede hacerla. Luego
responde a la pregunta «¿qué es lo que no sabéis?» en un párrafo.

## Rúbrica global

| Dimensión | Puntos | Qué se valora |
|---|---:|---|
| Coherencia entre secciones | 25 | Que ninguna respuesta contradiga a otra |
| Cálculo correcto y verificable | 25 | Cifras derivadas, no elegidas |
| Decisiones con su sacrificio declarado | 20 | Ninguna elección se presenta como gratuita |
| Evidencia y fuentes con fecha | 15 | Norma citada y fecha de verificación |
| Límites reconocidos | 15 | Lo que el sistema no puede hacer, y por qué |

## Aviso

Esta evaluación es **material docente**. Sus cifras son sintéticas, sus escenarios
son ficticios y ninguna de sus respuestas constituye asesoría legal, financiera ni
de inversión. Toda referencia normativa debe verificarse en su fuente oficial
antes de cualquier uso profesional.
