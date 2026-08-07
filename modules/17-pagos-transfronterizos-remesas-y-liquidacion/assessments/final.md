# Evaluación final: Pagos transfronterizos, remesas y liquidación

## Instrucciones

Responde sin consultar las soluciones de los laboratorios. Puedes usar las clases
y las fuentes oficiales. Declara los supuestos que necesites: un supuesto
explícito suma; uno oculto resta.

**Puntaje total:** 100 puntos. **Aprobación:** 70. **Tiempo sugerido:** 3 horas.

## Sección A — Arquitectura y conceptos (20 puntos)

**1.** (5 pts) Traza los cuatro flujos de un pago con dos corresponsales e indica
qué falla característico tiene cada uno.

**2.** (5 pts) Explica la diferencia entre pago en serie y pago con cobertura, y
qué riesgo adicional asume el banco beneficiario en el segundo.

**3.** (5 pts) ¿Qué es la banca anidada, por qué el corresponsal no la ve y qué
tres medidas la controlan?

**4.** (5 pts) Distingue compensación, liquidación y finalidad con un ejemplo de
quiebra del banco ordenante en tres instantes distintos.

## Sección B — Cálculo (30 puntos)

**5.** (12 pts) Una persona envía 800 000 unidades de moneda A hacia moneda B.

- **a)** Ruta 1: comisión 24 000; tipo aplicado A/USD 1 020 (referencia 990);
  comisión de intermediario 18 USD; tipo USD/B aplicado 51,2 (referencia 53,0);
  comisión del receptor 250 unidades de B. Calcula cuánto recibe el beneficiario.
- **b)** Calcula cuánto recibiría al tipo cruzado de referencia, sin ningún coste.
- **c)** Calcula el coste total en porcentaje y descomponlo en comisiones visibles
  y diferencial de cambio. Indica qué porcentaje del coste no aparece en el
  comprobante.

**6.** (10 pts) Un banco tiene estas salidas netas diarias en dólares: media
380 000, desviación 165 000, percentil 95 de 690 000, percentil 99 de 1 020 000 y
máximo observado 1 480 000. El saldo actual es de 2 200 000 y el coste neto de
fondeo es del 4,0 %.

- **a)** Calcula el coste anual del saldo actual.
- **b)** Propón un saldo objetivo justificando el percentil y el colchón.
- **c)** Calcula el ahorro y describe el plan por etapas con su regla de parada.

**7.** (8 pts) Tres operaciones de cambio: 60 M entregada a las 09:00 y recibida a
las 16:00; 35 M entregada a las 11:00 y recibida a las 16:00; 45 M entregada a las
15:00 y recibida a las 16:00. Calcula la exposición máxima simultánea y explica
por qué no es 60 M.

## Sección C — Mensajería y cumplimiento (20 puntos)

**8.** (7 pts) Un pago se reenvía tras un tiempo de espera agotado y el receptor lo
marca como duplicado, aunque los identificadores eran distintos. Explica la causa
y la corrección, y relaciónala con un concepto de la Parte 17.

**9.** (7 pts) Un sistema de screening genera 7,5 % de alertas con 0,029 % de
precisión. El área de negocio propone subir el umbral. Describe la prueba que
harías antes de responder y qué harías si esa prueba muestra que se pierden
verdaderos positivos.

**10.** (6 pts) ¿Qué información debe acompañar a una transferencia según la
Recomendación 16, y qué obligación tiene un banco intermediario respecto de ella?

## Sección D — Arquitecturas alternativas (20 puntos)

**11.** (8 pts) Un enlace de pagos inmediatos cubre el 71 % de un corredor y baja el
coste del 7,9 % al 1,1 %. Analiza qué ocurre con el 29 % restante y propón dos
mitigaciones que deban entrar en la fase 1.

**12.** (7 pts) Una ruta con stablecoin ahorra 126,96 USD frente a la clásica en un
corredor con dos intermediarios. Descompón el ahorro por fuente y di qué
porcentaje es atribuible al registro distribuido.

**13.** (5 pts) Enumera los seis problemas que hay que resolver para enlazar dos
sistemas de pagos inmediatos e indica cuántos son técnicos.

## Sección E — Decisión y ética (10 puntos)

**14.** (5 pts) Tu banco evalúa cerrar una corresponsalía con un país pequeño por
riesgo de cumplimiento. Es el único corresponsal del corredor. Argumenta la
decisión considerando qué ocurre con los flujos tras el cierre.

**15.** (5 pts) El comercial quiere anunciar «pagos internacionales instantáneos»
para un producto que cumple ese plazo en el 71 % de los casos. Redacta la
comunicación que sí propondrías y justifica por qué.

## Rúbrica

| Sección | Peso | Criterio de logro |
|---|---:|---|
| A — Arquitectura y conceptos | 20 | Traza flujos, no repite definiciones |
| B — Cálculo | 30 | Números correctos y decisión justificada |
| C — Mensajería y cumplimiento | 20 | Identifica la causa raíz, no el síntoma |
| D — Arquitecturas alternativas | 20 | Atribuye el ahorro a su fuente real |
| E — Decisión y ética | 10 | Considera a quien queda fuera |

## Escala

- 0–49: reforzar fundamentos; repetir clases 1 a 7 y laboratorios 1 y 3.
- 50–69: comprensión parcial; rehacer el laboratorio donde perdiste más puntos.
- 70–84: logro esperado; puedes iniciar el proyecto.
- 85–100: dominio destacado; puedes actuar como revisor de otros proyectos.

## Guía de corrección y retroalimentación

**Pregunta 5a.** Neto tras comisión: 776 000. A USD: 776 000 / 1 020 = 760,78 USD.
Menos intermediario: 742,78 USD. A moneda B: 742,78 × 51,2 = 38 030,34. Menos
comisión del receptor: **37 780,34 unidades de B**.

**Pregunta 5b.** Tipo cruzado de referencia: 53,0 / 990 = 0,0535354 B por A.
800 000 × 0,0535354 = **42 828,28 unidades de B**.

**Pregunta 5c.** Coste: 42 828,28 − 37 780,34 = 5 047,94, es decir **11,79 %**.
Descomposición aproximada, todo convertido a B al tipo de referencia: comisión de
envío 1 284,85; diferencial A/USD ≈ 1 202,4; comisión del intermediario 954,0;
diferencial USD/B ≈ 1 336,9; comisión del receptor 250,0. Comisiones visibles
2 488,85 (**49,3 %**); diferenciales 2 539,3 (**50,3 %**). Más de la mitad del
coste no aparece en el comprobante. Se acepta un margen de redondeo del 2 %.

**Pregunta 6b.** Se espera P99 más colchón hasta el máximo observado: **1 480 000**.
Quien fije la media (380 000) obtiene cero puntos en el apartado: ignora la cola.

**Pregunta 6c.** Ahorro: (2 200 000 − 1 480 000) × 4,0 % = **28 800**. El plan por
etapas y la regla de parada valen la mitad del apartado: reducir de golpe se
penaliza aunque el número sea correcto.

**Pregunta 7.** Máximo entre las 15:00 y las 16:00: 60 + 35 + 45 = **140 M**. No es
60 M porque las exposiciones se acumulan mientras están vivas.

**Pregunta 8.** La referencia extremo a extremo se regeneró en el reintento. Se
genera una vez, al crear la orden, y se conserva. Es la idempotencia de la Parte
17, clase 8, aplicada a la mensajería.

**Pregunta 9.** La prueba retrospectiva: recalcular las coincidencias confirmadas
del periodo con el umbral propuesto. Si se pierden verdaderos positivos, se
rechaza el cambio y se corrige la **calidad de la comparación**. Quien responda
«subir el umbral con vigilancia» obtiene cero: en sanciones no hay apetito de
riesgo.

**Pregunta 12.** Intermediarios evitados 62 %, prefinanciación 24 %, diferencial
11 %, coste de red 3 %. Atribuible al registro: **3 %**.

**Pregunta 15.** Se valora una comunicación por franja o con fecha de
disponibilidad calculada. «Instantáneo» con asterisco no puntúa: el asterisco no
corrige un titular falso.
