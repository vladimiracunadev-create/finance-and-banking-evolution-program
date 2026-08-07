---
part: 8
class: 12
title: "Análisis técnico: introducción crítica"
level: intermedio
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 12 · Análisis técnico: introducción crítica

> [← 11 · Análisis fundamental](11-analisis-fundamental.md) · [Índice de la parte](../README.md) · [13 · Costos, impuestos y sesgos →](13-costos-impuestos-y-sesgos.md)

**Parte 08 — Inversiones y mercados** · **Nivel:** Intermedio — requiere las partes anteriores · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Conocer el análisis técnico —qué afirma, qué herramientas usa y qué dice la evidencia sobre su
capacidad predictiva— con el mismo rigor con que se examina cualquier otro método. Esta clase no
promueve ni descarta el enfoque: entrega los elementos para evaluarlo y para reconocer cuándo se usa
como sustituto del análisis.

Esta clase trata un tema donde la evidencia y la práctica no coinciden, y por eso se presenta de forma crítica. No se enseña a operar con él: se enseña qué afirma, qué dice la evidencia sobre esas afirmaciones y por qué la mayoría de los resultados publicados no sobreviven a un análisis riguroso.

## 📚 Objetivos

Al finalizar podrás:

1. **Explicar** los supuestos del análisis técnico y su relación con la eficiencia de mercado.
2. **Interpretar** las herramientas más usadas y su construcción.
3. **Evaluar** la evidencia empírica sobre su capacidad predictiva.
4. **Distinguir** un patrón real de una interpretación retrospectiva.
5. **Diseñar** una prueba honesta de una estrategia técnica.

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

Los tres primeros términos son el método y su relación con la teoría de eficiencia; los cuatro siguientes, sus herramientas y los sesgos metodológicos que las invalidan. El **sobreajuste** es el problema central: con suficientes reglas probadas sobre los mismos datos, alguna siempre parece funcionar.

| Concepto | Comprensión verificable |
|---|---|
| `análisis técnico` | Estudio del precio y el volumen históricos para anticipar movimientos futuros. |
| `eficiencia débil` | Hipótesis de que los precios ya incorporan toda la información de precios pasados. |
| `soporte y resistencia` | Niveles donde históricamente el precio se detuvo. |
| `media móvil` | Promedio de los últimos N precios. Suaviza la serie. |
| `momentum` | Tendencia de los activos que subieron a seguir subiendo en horizontes intermedios. |
| `sesgo de anticipación` | Usar información que no estaba disponible en el momento de la señal. |
| `sobreajuste` | Encontrar reglas que funcionan en los datos históricos y no fuera de ellos. |

## 🧠 Modelo mental

El análisis técnico y la hipótesis de eficiencia son **afirmaciones contrapuestas**:

```text
ANÁLISIS TÉCNICO     los precios pasados contienen información sobre los futuros
EFICIENCIA DÉBIL     los precios pasados NO contienen información explotable
```

La pregunta no es cuál es más elegante, sino **qué dice la evidencia**. Y la evidencia es matizada: la
mayoría de los patrones no sobrevive a pruebas rigurosas, y algunos efectos —notablemente el
momentum— han mostrado persistencia en múltiples mercados y periodos.

## 📖 Desarrollo

### 1. Los supuestos declarados

El análisis técnico se apoya en tres afirmaciones:

```text
1. el precio descuenta toda la información
2. los precios se mueven en tendencias
3. la historia se repite, porque la psicología humana es estable
```

La primera es compatible con la eficiencia. La segunda y la tercera son las que se someten a prueba
empírica.

### 2. Herramientas principales

**Medias móviles:**

```text
MM(n) = promedio de los últimos n cierres

señal habitual: cruce de la MM corta sobre la MM larga → compra
                cruce inverso → venta
```

```text
precios: 100, 102, 105, 103, 108, 110, 107, 112
MM(3) al día 8 = (110 + 107 + 112)/3 = 109,67
MM(5) al día 8 = (103 + 108 + 110 + 107 + 112)/5 = 108,00
MM(3) > MM(5) → señal de compra
```

**Soporte y resistencia:**

```text
niveles donde el precio se detuvo repetidamente
interpretación: concentración de órdenes de compra (soporte) o de venta (resistencia)
```

**Indicadores de momento:**

```text
RSI = 100 − 100/(1 + RS)     donde RS = ganancia media/pérdida media de n periodos
interpretación habitual: RSI > 70 sobrecompra · RSI < 30 sobreventa
```

**Volumen:**

```text
un movimiento de precio con volumen alto se considera más significativo
que uno con volumen bajo
```

### 3. Qué dice la evidencia

La evidencia académica sobre el análisis técnico es abundante y bastante consistente. La tabla la resume con sus matices, incluido el caso del momentum.

| Afirmación | Estado de la evidencia |
|---|---|
| Los patrones gráficos (hombro-cabeza-hombro, banderas) predicen | Débil; la mayoría no sobrevive a pruebas fuera de muestra |
| Las medias móviles generan retorno superior después de costos | Débil en mercados desarrollados líquidos; algo mejor en mercados menos líquidos |
| El momentum de 3 a 12 meses persiste | **Robusto**: documentado en múltiples mercados, activos y periodos |
| La reversión de muy corto plazo (días) existe | Documentada, difícil de explotar después de costos |
| El RSI predice reversiones | Débil |
| El volumen aporta información predictiva | Mixta; algo de evidencia en combinación con precio |

El **efecto momentum** merece detalle porque es la excepción robusta:

```text
· comprar los activos con mejor rendimiento de los últimos 3-12 meses
  y vender los de peor rendimiento ha generado retorno positivo en múltiples
  mercados y periodos
· es uno de los "factores" reconocidos en la literatura académica
· NO es infalible: sufre caídas severas en los giros de mercado
· su explotación exige rotación alta, con costos de transacción relevantes
```

**Importante:** que el momentum exista **no valida el análisis técnico en general**. Es un efecto
específico, medible y con explicaciones tanto conductuales como de riesgo.

### 4. Sesgo de anticipación y sobreajuste

**Sesgo de anticipación (look-ahead bias):**

```text
✗ "la señal se activa cuando el precio cierra sobre la media móvil"
  y se compra al precio de ese mismo cierre
  → en la práctica solo puedes comprar al día siguiente

✗ usar un índice reconstituido con las empresas que existen HOY
  → excluye a las que quebraron: sesgo de supervivencia
```

**Sobreajuste:**

```text
si pruebas 500 combinaciones de parámetros en la misma serie,
aproximadamente 25 parecerán significativas al 5 % POR AZAR

la regla: cuantas más reglas pruebes, más alto debe ser el umbral de significancia
```

Prueba de honestidad de una estrategia:

```text
□ ¿se probó fuera de la muestra usada para diseñarla?
□ ¿funciona en otros mercados y periodos?
□ ¿incluye costos de transacción realistas?
□ ¿incluye el diferencial compra-venta?
□ ¿la señal se ejecuta al precio DISPONIBLE, no al que generó la señal?
□ ¿cuántas combinaciones de parámetros se probaron antes de encontrar esta?
□ ¿hay una explicación económica de por qué debería funcionar?
```

La última pregunta es decisiva: **una regla sin explicación económica que funciona en los datos
históricos es, muy probablemente, sobreajuste**.

### 5. Uso razonable

Aun cuando su capacidad predictiva sea limitada, el análisis técnico tiene usos defendibles:

| Uso | Justificación |
|---|---|
| Definir puntos de entrada dentro de una decisión ya tomada | No cambia la decisión, solo su ejecución |
| Fijar límites de pérdida (stop loss) | Disciplina de gestión de riesgo |
| Detectar iliquidez o comportamientos anómalos | El volumen aporta información operativa |
| Ejecutar órdenes grandes minimizando el impacto | Análisis de microestructura |

Uso **no** defendible:

```text
✗ sustituir el análisis del negocio por el gráfico
✗ operar con alta frecuencia sin considerar costos
✗ tomar decisiones de asignación estratégica por señales técnicas
```

## 🧮 Ejemplo guiado

El ejemplo aplica una regla técnica a una serie y luego la somete a la comprobación fuera de muestra. La diferencia entre los dos resultados es la lección de la clase.

**Situación.** Alguien propone una estrategia: comprar cuando la media móvil de 50 días cruza sobre la
de 200, vender en el cruce inverso. Muestra un retorno histórico de 14,2 % anual contra 9,8 % del
índice. Evalúala.

**Paso 1 — verifica el sesgo de anticipación.**

```text
¿a qué precio se ejecuta la señal?
  respuesta: "al cierre del día del cruce"
  
problema: el cruce solo se conoce DESPUÉS del cierre
ejecución realista: apertura del día siguiente
```

```text
recalculando con ejecución en la apertura siguiente:
  retorno 12,9 % anual (−1,3 puntos)
```

**Paso 2 — incorpora costos.**

```text
número de operaciones en el periodo: 34 en 20 años (1,7 por año)
costo por operación: comisión 0,25 % + diferencial 0,10 % = 0,35 %
costo anual = 1,7 × 2 × 0,35 % = 1,19 %

retorno neto: 12,9 − 1,19 = 11,71 % anual
```

**Paso 3 — verifica el sesgo de supervivencia.**

```text
la prueba se hizo sobre el índice actual
¿incluye las empresas que salieron del índice? → SÍ, es un índice, no acciones individuales ✔
```

**Paso 4 — prueba fuera de muestra.**

```text
la estrategia se diseñó con datos de 2000-2015
prueba en 2016-2024:
  estrategia: 8,4 % anual neto
  índice:     11,2 % anual
  → la estrategia rindió MENOS fuera de muestra
```

**Paso 5 — cuenta las combinaciones probadas.**

```text
pregunta al proponente: "¿probaste otras combinaciones de medias?"
respuesta: "sí, probamos 20/100, 30/150, 50/200, 100/300 y varias más"

→ se probaron al menos 8 combinaciones
→ que una funcione en el periodo de diseño no es evidencia fuerte
```

**Paso 6 — evalúa la dimensión que la comparación de retorno omite.**

```text
                            estrategia    índice
retorno neto (2000-2024)      11,0 %      10,4 %
desviación estándar           12,8 %      16,1 %
caída máxima                 −28,4 %     −51,2 %
Sharpe (r_f 3 %)               0,625       0,460
tiempo fuera del mercado       31 %          0 %
```

**Hallazgo relevante:** la estrategia rindió apenas 0,6 puntos más y **redujo la caída máxima de 51 %
a 28 %**. Su valor no está en el retorno superior sino en la reducción de la caída.

**Paso 7 — conclusión honesta.**

```text
LO QUE LA EVIDENCIA SOSTIENE
  · la estrategia NO superó al índice fuera de muestra en retorno
  · SÍ redujo consistentemente la caída máxima
  · su Sharpe fue superior en el periodo completo

LO QUE NO SOSTIENE
  · que prediga movimientos
  · que el retorno superior del periodo de diseño se repita

USO DEFENDIBLE
  como mecanismo de reducción de caída máxima para un inversionista cuya
  tolerancia sea la restricción vinculante, aceptando:
    · 1,19 % anual de costo de transacción
    · quedar fuera del mercado el 31 % del tiempo
    · señales falsas frecuentes en mercados laterales

USO NO DEFENDIBLE
  presentarla como una estrategia que "gana al mercado"
```

**Interpreta:** el retorno reportado de 14,2 % se redujo a 11,0 % al corregir tres sesgos, y **fue
inferior al índice fuera de la muestra de diseño**. Lo que sobrevivió al escrutinio fue algo distinto y
más modesto: una reducción real de la caída máxima. Esa es la conclusión defendible, y solo aparece
después de las siete verificaciones.

## 🏦 Del cliente al banco

El cliente opera con señales y el banco cobra comisión por cada operación. La tabla enfrenta las dos lecturas.

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| Ejecución de órdenes grandes | Mesa de negociación y microestructura | 8, clase 2 |
| Límites de pérdida | Control de riesgo de mesas | 11, clase 12 |
| Sobreajuste | Validación de modelos cuantitativos | 12, clase 13 |
| Momentum como factor | Estrategias sistemáticas de gestión | 8, clase 10 |
| Costos de transacción | Efecto en el retorno de estrategias activas | 8, clase 13 |

## 🧪 Práctica

El laboratorio pide probar una regla técnica dentro y fuera de muestra. El deterioro del resultado fuera de muestra es sistemático y es lo que el ejercicio demuestra.

En `labs/lab-06.md`, sección de análisis técnico:

1. Calcula medias móviles y RSI de una serie real y grafica las señales.
2. Diseña una estrategia simple y pruébala con y sin costos de transacción.
3. Divide la serie en periodo de diseño y de prueba, y compara resultados.
4. Aplica las siete verificaciones de honestidad a una estrategia publicada.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen estrategias que funcionaban en el pasado y no en el futuro. Las causas son el sobreajuste y el sesgo de anticipación.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| La estrategia funciona en el pasado y no después | Sobreajuste | Prueba fuera de muestra. |
| Se ejecuta al precio que generó la señal | Sesgo de anticipación | Ejecuta al precio disponible después. |
| Se omiten los costos de transacción | Retorno inflado | Incluye comisión y diferencial. |
| Se prueban muchas combinaciones | Significancia sobreestimada | Ajusta el umbral por el número de pruebas. |
| Se sustituye el análisis del negocio por el gráfico | Uso no defendible | El gráfico informa la ejecución, no la decisión. |
| Se compara solo el retorno | Riesgo omitido | Compara también caída máxima y Sharpe. |

## ❓ Preguntas de comprobación

1. ¿Qué afirma el análisis técnico y qué afirma la eficiencia débil?
2. ¿Cuál es el único efecto técnico con evidencia robusta y qué límites tiene?
3. ¿Qué es el sesgo de anticipación y cómo se corrige?
4. ¿Por qué probar muchas combinaciones invalida la significancia estadística?
5. Nombra tres usos defendibles y tres no defendibles del análisis técnico.

## 📥 Entregable

Guarda en `portfolio/parte-08/clase-12/`:

- las medias móviles y el RSI de una serie real con sus señales graficadas;
- una estrategia probada con y sin costos, con la diferencia cuantificada;
- la comparación entre periodo de diseño y periodo de prueba;
- las siete verificaciones aplicadas a una estrategia publicada, con tu conclusión.

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

- Fama, E. (1970). "Efficient Capital Markets: A Review of Theory and Empirical Work". *Journal of Finance*. Formulación de las formas de eficiencia.
- Jegadeesh, N. y Titman, S. (1993). "Returns to Buying Winners and Selling Losers". *Journal of Finance*. Evidencia original del efecto momentum.
- Lo, A., Mamaysky, H. y Wang, J. (2000). "Foundations of Technical Analysis". *Journal of Finance*. Evaluación estadística de patrones técnicos.
- Bailey, D. et al. (2014). "Pseudo-Mathematics and Financial Charlatanism". *Notices of the AMS*. Sobreajuste en pruebas de estrategias.
- Malkiel, B. (2023). *A Random Walk Down Wall Street* (13.ª ed.). Norton. Revisión crítica del análisis técnico.
- Verificación local: usa series de precios y volúmenes publicadas por la bolsa de tu país, verificando si están ajustadas por dividendos y por operaciones societarias.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 11 · Análisis fundamental](11-analisis-fundamental.md) | [Parte 08](../README.md) · [Programa](../../../SYLLABUS.md) | [13 · Costos, impuestos y sesgos →](13-costos-impuestos-y-sesgos.md) |
<!-- gen:footer:end -->
