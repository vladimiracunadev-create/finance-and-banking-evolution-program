# Evaluación final: Finanzas abiertas, APIs y economía de datos

## Instrucciones

Responde sin consultar las soluciones de los laboratorios. Puedes usar las
clases y las fuentes oficiales. Declara los supuestos que necesites: un supuesto
explícito suma; uno oculto resta.

**Puntaje total:** 100 puntos. **Aprobación:** 70. **Tiempo sugerido:** 3 horas.

## Sección A — Conceptos y perímetro (20 puntos)

**1.** (5 pts) Sitúa en el perímetro regulatorio a: un agregador de saldos, un
iniciador de pagos, un comparador que no accede a datos y un proveedor de
software que opera la infraestructura de un banco. Indica en cada caso si la
actividad es regulada y por qué.

**2.** (5 pts) Explica por qué «finanzas abiertas» no es sinónimo de «los datos son
del cliente, así que puede compartirlos con quien quiera».

**3.** (5 pts) Distingue **reciprocidad** de **acceso obligatorio** y explica qué
incentivo cambia cada uno.

**4.** (5 pts) ¿Qué es una **API premium** y qué problema regulatorio plantea?

## Sección B — Cálculo y diseño (25 puntos)

**5.** (10 pts) Un proveedor de información atiende 4 200 000 llamadas al mes con un
objetivo de disponibilidad del 99,5 %. Calcula:

- **a)** los minutos de indisponibilidad admitidos al mes;
- **b)** cuántas llamadas fallarían si toda la indisponibilidad ocurriera en la hora punta, que concentra el 9 % del tráfico diario;
- **c)** si un acuerdo de nivel de servicio del 99,9 % con penalización es razonable cuando el coste marginal de pasar de 99,5 % a 99,9 % es de 18 000 al año y la penalización esperada es de 6 500 al año.

**6.** (8 pts) Diseña el conjunto mínimo de alcances para un producto que ofrece
«categorización de gastos del último año». Justifica cada alcance y explica
cuál rechazarías si el producto pidiera más.

**7.** (7 pts) Escribe la respuesta de error para: token expirado, consentimiento
revocado, cuenta inexistente y cuenta existente pero fuera del alcance.
Explica por qué dos de ellas deben ser indistinguibles.

## Sección C — Seguridad (20 puntos)

**8.** (6 pts) Un cliente público implementa el flujo de autorización sin PKCE.
Describe el ataque concreto, paso a paso.

**9.** (7 pts) Un desarrollador propone aceptar `redirect_uri` que empiece por el
dominio registrado. Explica el riesgo con un ejemplo de URI que pasaría el
filtro y no debería.

**10.** (7 pts) Diseña tres pruebas negativas que detectarían una implementación que
no invalida los tokens al revocar el consentimiento.

## Sección D — Riesgo y regulación (20 puntos)

**11.** (7 pts) Analiza el riesgo de concentración: tres agregadores intermedian el
80 % de los accesos del sistema. Enumera cuatro consecuencias y dos medidas.

**12.** (7 pts) Un pago iniciado por un tercero resulta no autorizado. Construye la
matriz de responsabilidad entre cliente, iniciador y proveedor de cuenta, y
di de qué hechos depende cada casilla.

**13.** (6 pts) Indica qué norma o normativa regula las finanzas abiertas en tu
jurisdicción, con su identificador, su autoridad y **la fecha en que la
verificaste**. Si está en despliegue por fases, indica en cuál está.

## Sección E — Decisión y ética (15 puntos)

**14.** (8 pts) Tu empresa puede inferir un embarazo a partir de la categorización de
gastos y usar esa inferencia para ofrecer un crédito. Es técnicamente
posible y comercialmente rentable. Argumenta la decisión distinguiendo:
técnicamente posible / jurídicamente válido / éticamente defendible.

**15.** (7 pts) El equipo quiere guardar los datos brutos «por si sirven después».
Redacta la política de retención que propondrías y su justificación.

## Rúbrica

| Sección | Peso | Criterio de logro |
|---|---:|---|
| A — Conceptos y perímetro | 20 | Ubica la actividad, no repite el eslogan |
| B — Cálculo y diseño | 25 | Números correctos y decisión justificada |
| C — Seguridad | 20 | Describe el ataque, no solo el control |
| D — Riesgo y regulación | 20 | Cita norma, autoridad y fecha |
| E — Decisión y ética | 15 | Separa los tres planos sin refugiarse en uno |

## Escala

- 0–49: reforzar fundamentos; repetir clases 1 a 6 y laboratorios 1 y 2.
- 50–69: comprensión parcial; rehacer el laboratorio donde perdiste más puntos.
- 70–84: logro esperado; puedes iniciar el proyecto.
- 85–100: dominio destacado; puedes actuar como revisor de otros proyectos.

## Guía de corrección y retroalimentación

**Pregunta 5a.** 30 días × 24 h × 60 min = 43 200 min. 0,5 % = **216 minutos**.

**Pregunta 5b.** Tráfico diario = 4 200 000 / 30 = 140 000 llamadas. Hora punta =
9 % = 12 600 llamadas/hora = 210 por minuto. 216 minutos × 210 = **45 360
llamadas** fallidas en el peor caso. Compárese con el 0,5 % del total mensual
(21 000): la diferencia muestra por qué el acuerdo debe medirse en la ventana
crítica y no en el promedio mensual.

**Pregunta 5c.** 18 000 > 6 500: el coste supera a la penalización esperada. La
respuesta correcta **no** es «no lo hagas»: es señalar que la penalización no
mide el daño real (pérdida de clientes, incidente reputacional, exigencia
regulatoria) y que la decisión depende de si ese daño está o no en el número.
Quien responda solo comparando 18 000 con 6 500 obtiene la mitad del puntaje.

**Pregunta 7.** «Cuenta inexistente» y «cuenta fuera del alcance» deben ser
indistinguibles: si difieren, el llamante enumera cuentas ajenas comprobando cuál
de los dos errores recibe.

**Pregunta 13.** Se exige la fecha de verificación. Una respuesta que cite la
norma correcta sin fecha obtiene como máximo la mitad del puntaje, porque el
programa entero se apoya en que la vigencia se comprueba.
