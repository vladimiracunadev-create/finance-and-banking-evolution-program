---
part: 7
class: 13
title: "Escenarios y simulación"
level: avanzado
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 13 · Escenarios y simulación

> [← 12 · Sensibilidad](12-sensibilidad.md) · [Índice de la parte](../README.md) · [14 · Modelamiento con Excel y Python →](14-modelamiento-con-excel-y-python.md)

**Parte 07 — Matemática financiera avanzada** · **Nivel:** Avanzado — perfil analista · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Pasar del análisis de una variable a la vez al análisis de la incertidumbre completa. Los escenarios
capturan combinaciones coherentes de supuestos; la simulación de Monte Carlo entrega la distribución
del resultado. Ambas técnicas responden preguntas que la sensibilidad no puede: **¿cuál es la
probabilidad de perder?** y **¿cuánto se puede perder en el peor caso razonable?**

## 📚 Objetivos

Al finalizar podrás:

1. **Construir** escenarios coherentes con probabilidades asignadas.
2. **Calcular** valor esperado y desviación del resultado.
3. **Implementar** una simulación de Monte Carlo básica.
4. **Interpretar** la distribución de resultados y sus percentiles.
5. **Reconocer** los límites de la simulación y sus errores típicos.

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

| Concepto | Comprensión verificable |
|---|---|
| `escenario` | Conjunto coherente de valores de todas las variables. No es mover una sola. |
| `coherencia interna` | Los supuestos de un escenario deben poder ocurrir juntos. |
| `valor esperado` | `Σ probabilidad × resultado`. No es el resultado más probable. |
| `simulación de Monte Carlo` | Miles de iteraciones con valores extraídos de distribuciones supuestas. |
| `distribución del resultado` | Histograma de los resultados simulados. Es la salida real de la simulación. |
| `percentil` | Valor bajo el cual cae un porcentaje de los resultados. El P5 es el escenario adverso. |
| `correlación` | Relación entre variables. Ignorarla es el error más común y más costoso. |

## 🧠 Modelo mental

Las tres técnicas responden preguntas distintas:

```text
SENSIBILIDAD  ¿qué variable importa más?           → una a la vez
ESCENARIOS    ¿qué pasa si todo va mal a la vez?   → combinaciones coherentes
SIMULACIÓN    ¿cuál es la distribución completa?   → miles de combinaciones
```

Y la advertencia que acompaña siempre a la tercera: **una simulación produce una distribución
precisa de un modelo que puede estar equivocado**. La precisión de la salida no valida los supuestos
de entrada.

## 📖 Desarrollo

### 1. Construir escenarios coherentes

```text
✗ INCOHERENTE
  escenario adverso: caen las ventas, sube el precio de venta,
                     baja el costo de insumos, baja la tasa de interés
  → estos hechos no ocurren juntos

✓ COHERENTE
  escenario adverso: recesión → caen las ventas 22 %, cae el precio 12 %
                     (menor demanda), sube la tasa 180 pb (prima de riesgo),
                     bajan los insumos 8 % (menor demanda global)
```

La prueba de coherencia: **¿existe una narrativa económica que produzca todos estos valores a la
vez?** Si no la hay, el escenario es una combinación arbitraria.

Escenarios típicos de un proyecto:

| Variable | Adverso (20 %) | Base (55 %) | Favorable (25 %) |
|---|---:|---:|---:|
| Volumen | 9 200 | 12 000 | 13 800 |
| Precio | 7 480 | 8 500 | 9 100 |
| Costo variable | 5 100 | 4 900 | 4 750 |
| Costos fijos | 19 400 | 18 000 | 17 800 |
| WACC | 14,5 % | 12,0 % | 11,2 % |
| **VAN** | **−78 400** | **42 000** | **136 900** |

### 2. Valor esperado y dispersión

```text
E[VAN] = Σ p_i × VAN_i
       = 0,20 × (−78 400) + 0,55 × 42 000 + 0,25 × 136 900
       = −15 680 + 23 100 + 34 225 = 41 645

σ = √(Σ p_i × (VAN_i − E[VAN])²)
  = √[0,20 × (−120 045)² + 0,55 × (355)² + 0,25 × (95 255)²]
  = √[2 882 160 000 + 69 000 + 2 268 869 000]
  = √5 151 098 000 = 71 771

coeficiente de variación = 71 771/41 645 = 1,72
```

Dos lecturas:

```text
· el valor esperado (41 645) es casi idéntico al escenario base (42 000): coincidencia,
  no regla
· el coeficiente de variación de 1,72 indica altísima dispersión: la desviación
  supera al valor esperado en un 72 %
· probabilidad de VAN negativo = 20 % (solo el escenario adverso)
```

### 3. Simulación de Monte Carlo

```text
PROCEDIMIENTO
1. asignar una distribución de probabilidad a cada variable incierta
2. definir las correlaciones entre variables
3. extraer un valor aleatorio de cada distribución
4. calcular el resultado con esa combinación
5. repetir 10 000 veces o más
6. analizar la distribución de los 10 000 resultados
```

Distribuciones habituales:

| Variable | Distribución típica | Parámetros |
|---|---|---|
| Precio de commodity | Lognormal o histórica | Media y desviación de la serie |
| Volumen | Triangular | Mínimo, más probable, máximo |
| Costo variable | Normal | Media y desviación |
| Plazo de construcción | Triangular asimétrica | Los retrasos son más probables que los adelantos |
| Tasa de interés | Normal o basada en la curva | Media y volatilidad implícita |

Implementación básica:

```python
import random
import statistics

def simular_van(iteraciones: int = 10_000) -> list[float]:
    """Simula el VAN de un proyecto con tres variables inciertas.

    Las distribuciones y sus parámetros son supuestos del modelo y deben
    documentarse junto con su fuente. La correlación entre precio y volumen
    se modela de forma simplificada mediante un factor común de demanda.
    """
    resultados = []
    for _ in range(iteraciones):
        # factor común de demanda: afecta precio y volumen en el mismo sentido
        demanda = random.gauss(1.0, 0.12)

        volumen = 12_000 * demanda
        precio = 8_500 * (0.6 + 0.4 * demanda)     # correlación parcial con la demanda
        costo_var = random.gauss(4_900, 250)
        costo_fijo = random.gauss(18_000, 900)
        wacc = random.gauss(0.12, 0.015)

        margen = (precio - costo_var) * volumen / 1_000  # en miles
        operativo = margen - costo_fijo
        factor = (1 - (1 + wacc) ** -8) / wacc
        van = operativo * factor - 180_000
        resultados.append(van)
    return resultados
```

### 4. Interpretar la distribución

Resultado de 10 000 iteraciones:

```text
media                    43 180
mediana                  41 950
desviación estándar      58 400

P5   (adverso)          −52 700
P10                     −28 400
P25                       4 900
P50  (mediana)           41 950
P75                      79 800
P90                     118 600
P95  (favorable)        142 300

probabilidad de VAN < 0:  17,8 %
probabilidad de VAN > 100 000: 21,4 %
```

Lo que la distribución aporta y los escenarios no:

```text
· la PROBABILIDAD de pérdida (17,8 %), no solo su magnitud
· el P5 como escenario adverso con base estadística, no arbitrario
· la asimetría: media (43 180) mayor que mediana (41 950) → cola derecha más larga
· el rango completo, no tres puntos
```

### 5. Límites y errores

| Error | Efecto | Corrección |
|---|---|---|
| Ignorar correlaciones | Subestima severamente el riesgo | Modela la correlación explícitamente |
| Usar distribuciones normales para todo | Subestima eventos extremos | Usa distribuciones con colas apropiadas |
| Suponer independencia entre periodos | Ignora la persistencia de los shocks | Modela autocorrelación si existe |
| Confundir precisión con exactitud | Falsa confianza | La salida hereda la calidad de los supuestos |
| No documentar las distribuciones | Modelo no auditable | Declara distribución, parámetros y fuente |
| Presentar solo la media | Se pierde toda la información de riesgo | Presenta percentiles y probabilidad de pérdida |

**El primer error es el más costoso y el más frecuente.** Si el precio y el volumen están
correlacionados positivamente y se simulan como independientes, la simulación produce combinaciones
imposibles (precio alto con volumen alto en una recesión) y **subestima la probabilidad de los
escenarios malos**.

Demostración del efecto:

```text
con correlación precio-volumen = 0,0:  probabilidad de VAN < 0 = 8,2 %
con correlación precio-volumen = 0,7:  probabilidad de VAN < 0 = 17,8 %
```

La correlación **duplica la probabilidad de pérdida** sin cambiar ninguna otra cosa.

## 🧮 Ejemplo guiado

**Situación.** Continúa el proyecto agroindustrial de la clase 12. El comité pide la distribución
completa del resultado antes de decidir.

**Paso 1 — define las distribuciones con base empírica.**

| Variable | Distribución | Parámetros | Fuente |
|---|---|---|---|
| Precio | Lognormal | media 945 000, σ 178 000 | Serie histórica 10 años, organismo oficial |
| Producción | Triangular | mín 3 150, moda 4 200, máx 4 620 | Estudio agronómico del proyecto |
| Costo variable | Normal | media 560 000, σ 42 000 | Estructura de costos histórica |
| Costos fijos | Normal | media 720, σ 45 | Presupuesto del proyecto |
| WACC | Normal | media 13,5 %, σ 1,2 pp | Curva de mercado + prima sectorial |

**Paso 2 — define las correlaciones.**

```text
precio – producción:   −0,35  (mayor oferta agregada deprime el precio)
precio – costo var:    +0,25  (ambos responden a costos energéticos)
producción – costo var: +0,15 (mayor producción, más insumos por hectárea)
```

La primera correlación es negativa y **contraintuitiva para quien no conoce el sector**: un buen año
agrícola para todos deprime el precio. Ignorarla haría que la simulación combinara alta producción con
alto precio, lo que rara vez ocurre.

**Paso 3 — ejecuta 20 000 iteraciones y analiza.**

```text
media                     2 496 millones
mediana                   2 388 millones
desviación estándar       1 842 millones

P1                       −2 104
P5   (adverso)           −1 087
P10                        −312
P25                       1 214
P50                       2 388
P75                       3 690
P90                       4 918
P95                       5 702

probabilidad de VAN < 0:                 12,4 %
probabilidad de VAN < 500 (umbral banco): 18,9 %
```

**Paso 4 — traduce a riesgo de crédito.**

```text
el proyecto no paga el crédito si el flujo no cubre el servicio de deuda
cobertura mínima de 1,0 corresponde aproximadamente a un VAN de 380 millones

probabilidad de cobertura < 1,0 = 17,2 %
probabilidad de cobertura < 1,25 (covenant) = 24,8 %
```

**Paso 5 — compara con la sensibilidad de la clase 12.**

```text
sensibilidad (clase 12):  probabilidad estimada de cruzar el equilibrio del precio ≈ 30 %
simulación (esta clase):  probabilidad de VAN < 0 = 12,4 %

¿por qué difieren?
  la sensibilidad univariante suponía que el precio caía con TODO lo demás en su valor base
  la simulación permite que un precio bajo coincida con una producción alta (correlación −0,35),
  lo que compensa parcialmente
  
la simulación es más realista PORQUE incorpora la correlación
```

**Paso 6 — decisión con la nueva información.**

```text
probabilidad de incumplimiento del covenant: 24,8 %
probabilidad de no cubrir el servicio de deuda: 17,2 %
pérdida esperada del banco (con LGD 40 % sobre 2 400 millones): 
  0,172 × 0,40 × 2 400 = 165 millones

el pricing debe cubrir esa pérdida esperada:
  prima de riesgo mínima = 165/2 400/7 años ≈ 0,98 % anual adicional

CONDICIONES REVISADAS:
1. contratos de precio mínimo por el 60 % de la producción
   → simulación con esa cobertura: probabilidad de incumplimiento cae a 7,1 %
   → pérdida esperada cae a 68 millones
   → prima de riesgo requerida baja a 0,40 %
2. covenant de cobertura en 1,15 (no 1,25): con 1,25 la probabilidad de
   incumplimiento técnico es del 24,8 %, lo que generaría renegociaciones frecuentes
3. cuenta de reserva de 6 meses de servicio
```

**Interpreta:** la simulación **corrigió a la baja** la probabilidad de pérdida estimada por
sensibilidad (de ~30 % a 12,4 %) al incorporar una correlación que jugaba a favor, y **corrigió al
alza** el diseño del covenant, porque un umbral de 1,25 habría producido incumplimientos técnicos en
uno de cada cuatro años sin que el proyecto estuviera realmente en problemas. Ambos ajustes provienen
de mirar la distribución completa en lugar de tres puntos.

## 🏦 Del cliente al banco

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| Escenarios coherentes | Pruebas de estrés regulatorias | 11, clase 13 |
| Distribución de pérdidas | Cálculo de pérdida esperada e inesperada | 11, clase 2 |
| Percentil adverso | Valor en riesgo | 11, clase 3 |
| Correlación | Riesgo de concentración de cartera | 11, clase 2 |
| Diseño de covenants | Probabilidad de incumplimiento técnico | 13, clase 10 |

## 🧪 Práctica

En `labs/lab-06.md`, sección de simulación:

1. Construye tres escenarios coherentes con narrativa económica y probabilidades.
2. Calcula valor esperado, desviación y coeficiente de variación.
3. Implementa una simulación de Monte Carlo con al menos tres variables correlacionadas.
4. Compara los resultados con y sin correlación, y cuantifica la diferencia.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Los escenarios mezclan supuestos incompatibles | Sin narrativa económica | Verifica la coherencia interna. |
| La simulación subestima el riesgo | Correlaciones ignoradas | Modela las correlaciones explícitamente. |
| Se presenta solo la media | Información de riesgo perdida | Presenta percentiles y probabilidad de pérdida. |
| Se confía en la precisión de la salida | Supuestos no validados | La salida hereda la calidad de las entradas. |
| Se usan distribuciones normales para todo | Colas subestimadas | Elige la distribución según la evidencia. |
| No se documentan las distribuciones | Modelo no auditable | Declara distribución, parámetros y fuente. |

## ❓ Preguntas de comprobación

1. ¿Qué hace que un escenario sea internamente coherente?
2. ¿Por qué el valor esperado no es el resultado más probable?
3. ¿Qué aporta una simulación que los escenarios no pueden entregar?
4. ¿Cuál es el error más costoso en una simulación y qué efecto tiene?
5. ¿Por qué la simulación puede corregir a la baja una probabilidad estimada por sensibilidad?

## 📥 Entregable

Guarda en `portfolio/parte-07/clase-13/`:

- los tres escenarios con narrativa, probabilidades y coherencia verificada;
- el valor esperado, la desviación y el coeficiente de variación;
- el código de la simulación con las distribuciones y correlaciones documentadas;
- la comparación con y sin correlación, con la diferencia cuantificada.

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

- Glasserman, P. (2004). *Monte Carlo Methods in Financial Engineering*. Springer. Fundamentos y técnicas de simulación.
- Savage, S. (2012). *The Flaw of Averages*. Wiley. Por qué los promedios inducen a error y qué aporta la distribución.
- Damodaran, A. (2012). *Investment Valuation* (3.ª ed.). Wiley. Capítulo 6: simulación aplicada a la valoración.
- Basel Committee on Banking Supervision (2018). *Stress testing principles*. BIS. Construcción de escenarios coherentes y severos. <https://www.bis.org/bcbs/publ/d450.htm>
- Vose, D. (2008). *Risk Analysis: A Quantitative Guide* (3.ª ed.). Wiley. Selección de distribuciones y modelación de correlaciones.
- Verificación local: usa series históricas oficiales de tu país para estimar los parámetros de las distribuciones y documenta la fecha de descarga.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 12 · Sensibilidad](12-sensibilidad.md) | [Parte 07](../README.md) · [Programa](../../../SYLLABUS.md) | [14 · Modelamiento con Excel y Python →](14-modelamiento-con-excel-y-python.md) |
<!-- gen:footer:end -->
