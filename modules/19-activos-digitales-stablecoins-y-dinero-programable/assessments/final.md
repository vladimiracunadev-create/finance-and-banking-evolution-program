# Evaluación final: Activos digitales, stablecoins y dinero programable

## Instrucciones

Responde sin consultar las soluciones de los laboratorios. Puedes usar las
clases y las fuentes oficiales. Declara los supuestos que necesites: un supuesto
explícito suma; uno oculto resta.

**Puntaje total:** 100 puntos. **Aprobación:** 70. **Tiempo sugerido:** 3 horas.

## Sección A — Clasificación y régimen (25 puntos)

**1.** (8 pts) Aplica la ficha de cinco preguntas a estos tres instrumentos y di
qué régimen le corresponde a cada uno:

- **a)** saldo emitido por una entidad autorizada, redimible a la par por
  cualquiera, sin remuneración;
- **b)** token emitido por una sociedad no financiera, redimible a la par solo
  desde 100 000, que paga un 5 % anual;
- **c)** anotación de un depósito de un banco supervisado en un registro
  programable.

**2.** (7 pts) Explica por qué dos instrumentos idénticos en su red, su estándar
de contrato y su billetera pueden tener regímenes opuestos. Di dónde se mira para
distinguirlos.

**3.** (5 pts) Un producto se presenta como «token de pago». Cumple los tres
elementos del dinero electrónico y además remunera el saldo. ¿Qué significa eso, y
qué tres correcciones exigirías antes de que se lance?

**4.** (5 pts) Explica qué es la singularidad del dinero y qué pasaría si cada
banco emitiera un token negociable entre sí. Di qué mecanismo la conserva.

## Sección B — Cálculo (30 puntos)

**5.** (10 pts) Una reserva de 10 200 000 000 respalda un circulante de
10 000 000 000, con esta composición: 12 % efectivo, 40 % letras ≤ 3 meses, 28 %
deuda 1–2 años, 8 % pactos inversos, 9 % papel comercial, 3 % depósitos a plazo.

- **a)** Calcula cobertura contable, cobertura líquida a 24 horas y peso ilíquido.
- **b)** Atiende una redención del 30 % con los descuentos de la tabla y anota el
  coste.
- **c)** Recalcula las tres métricas y explica por qué la cobertura publicada
  mejora.

**6.** (10 pts) Un emisor cobra un 0,08 % de comisión de redención, liquida en
3 días con un coste de financiación del 4,80 %, cobra 15 por operación y exige un
mínimo de 250 000 unidades.

- **a)** Calcula la banda de no arbitraje para un tamaño de 1 000 000.
- **b)** El precio de mercado está en 0,9955 desde hace nueve horas. ¿Está fuera
  de banda? ¿Rinde arbitrar?
- **c)** Si rinde y nadie lo hace, enumera las causas posibles y di cuál
  investigarías primero.

**7.** (10 pts) Un diseño de dos tokens tiene 1 500 000 000 de token estable y un
token variable con 500 000 000 de unidades a 1,80.

- **a)** Calcula el ratio de absorción inicial.
- **b)** Simula dos canjes de 150 000 000 suponiendo que se vende el 70 % de lo
  recibido y un impacto del 1 % por cada 20 000 000 vendidos. Anota ratio,
  emisión por unidad y precio en cada vuelta.
- **c)** Di cuál de las dos series usarías como indicador y por qué.

## Sección C — Riesgo y control (25 puntos)

**8.** (9 pts) Un custodio propone un esquema 4-de-7: cuatro guardianes en la sede
central con el mismo modelo de dispositivo, dos en una filial con otro modelo y
uno externo.

- **a)** Calcula el mayor grupo por cada factor y la independencia efectiva.
- **b)** ¿Tolera un evento correlacionado?
- **c)** Rediséñalo **sin cambiar el umbral** y demuestra que ahora sí.

**9.** (8 pts) Un banco no tiene posición en el instrumento X. Presta 60 000 000 a
una entidad con capital de 200 000 000 y posición de 50 000 000 en X, y recibe
120 000 000 en depósitos de un custodio que guarda X por cuenta de terceros.

- **a)** Calcula la exposición de segundo grado.
- **b)** Ante una caída del 60 %, con disposición del 40 % de la línea y retirada
  del 30 % de los depósitos, calcula la necesidad de liquidez.
- **c)** Explica por qué el custodio no aparece en (a) y sí en (b).

**10.** (8 pts) Una administración quiere entregar una ayuda restringida a
comercios de una lista, con caducidad a 60 días.

- **a)** Clasifica la propuesta como pago o dinero programable, con la prueba.
- **b)** Nombra tres costes que la restricción introduce y quién los soporta.
- **c)** Propón un diseño alternativo que cumpla el objetivo declarado.

## Sección D — Expediente y decisión (20 puntos)

**11.** (12 pts) Redacta el expediente resumido de decisión para el instrumento de
la pregunta 5, con destino a una tesorería de 6 000 000 y un apetito del 2 % sobre
un capital de 300 000 000. Incluye al menos: clasificación, análisis de reservas,
canal de redención, límite de posición con sus cuatro elementos, tres indicadores
de alerta y plan de salida.

**12.** (8 pts) Un comité te pregunta: «entonces, ¿es seguro?». Redacta la
respuesta en un máximo de diez líneas, separando **hecho**, **supuesto** e
**interpretación**, y sin usar la palabra «seguro» sin cuantificar.

## Rúbrica

| Sección | Criterio | Puntos |
|---|---|---:|
| A | Clasifica por la promesa, no por la tecnología | 25 |
| B | Cálculos correctos con supuestos declarados | 30 |
| C | Identifica el riesgo que la cifra publicada oculta | 25 |
| D | Expediente completo y respuesta honesta | 20 |

### Criterios transversales

| Criterio | Efecto |
|---|---|
| Supuesto declarado junto a la cifra | Suma |
| Supuesto oculto | Resta el doble de lo que valía la cifra |
| Recomendación de inversión | Anula la pregunta |
| Usar «estable», «seguro» o «respaldado» sin cuantificar | Resta |
| Conclusión de rechazo bien fundada | Vale lo mismo que una aprobación |

## Guía de corrección

| Pregunta | Idea que debe aparecer |
|---:|---|
| 1 | a) dinero electrónico · b) referenciado con tres incumplimientos · c) depósito |
| 2 | El derecho y el propósito, no el soporte; se mira el prospecto y el balance |
| 3 | Es dinero electrónico en sustancia; eliminar remuneración, mínimo y resolver la circulación al portador |
| 4 | Que un peso valga lo mismo sea del banco que sea; lo conserva la liquidación en dinero de banco central |
| 5 | Cobertura 102 % · líquida ≈ 86 % · el remanente pierde efectivo y gana peso ilíquido |
| 6 | Banda ≈ 12,4 pb · el precio está fuera y rinde · investigar primero las dudas sobre reservas |
| 7 | Ratio 0,60 y creciente; emisión por unidad creciente; usar la segunda |
| 8 | Mayor grupo 4 = umbral → no tolera; redistribuir dispositivo y ubicación |
| 9 | 15 000 000 de segundo grado · 60 000 000 de liquidez · el custodio no tiene posición propia pero es acreedor |
| 10 | Dinero programable; mercado gris, exclusión y caducidad; dinero libre con condicionalidad en la elegibilidad |
| 11 | Las piezas presentes, límites con disparador y plan de salida con canal cerrado |
| 12 | Sin adjetivos sin cifra; las tres capas separadas |
