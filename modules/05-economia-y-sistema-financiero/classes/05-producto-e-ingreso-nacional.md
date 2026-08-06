---
part: 6
class: 5
title: "Producto e ingreso nacional"
level: intermedio
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 05 · Producto e ingreso nacional

> [← 04 · Competencia y estructuras de mercado](04-competencia-y-estructuras-de-mercado.md) · [Índice de la parte](../README.md) · [06 · Inflación →](06-inflacion.md)

**Parte 06 — Economía y sistema financiero** · **Nivel:** Intermedio — requiere las partes anteriores · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Aprender a leer los agregados que describen una economía completa, porque son el contexto en el que
opera cualquier banco y cualquier empresa. Esta clase enseña qué mide el PIB, qué deja fuera, cómo se
descompone y cómo se usa para anticipar el comportamiento de la cartera de crédito.

## 📚 Objetivos

Al finalizar podrás:

1. **Calcular** el PIB por los tres enfoques y verificar su equivalencia.
2. **Distinguir** PIB nominal, real y per cápita, y usarlos correctamente.
3. **Interpretar** la composición del gasto y su ciclo.
4. **Explicar** qué no mide el PIB y por qué importa.
5. **Relacionar** el crecimiento del PIB con el desempeño de la cartera bancaria.

<!-- gen:agenda:start -->
## Agenda de 90 minutos

| Minutos | Bloque | Qué ocurre |
|---:|---|---|
| 0–10 | Activación | Pregunta diagnóstica y recuperación de la clase anterior. |
| 10–35 | Conceptos | Desarrollo guiado con la fuente oficial a la vista. |
| 35–55 | Ejemplo guiado | El docente resuelve el caso numérico paso a paso. |
| 55–80 | Práctica | El estudiante replica con datos propios o sintéticos. |
| 80–90 | Cierre | Preguntas de comprobación y registro en el portafolio. |
<!-- gen:agenda:end -->

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| `PIB` | Valor de mercado de todos los bienes y servicios **finales** producidos dentro del país en un periodo. |
| `valor agregado` | Valor de la producción menos los consumos intermedios. Evita la doble contabilización. |
| `enfoque del gasto` | `PIB = C + I + G + (X − M)`. El más usado para análisis de ciclo. |
| `enfoque del ingreso` | Suma de remuneraciones, excedente de explotación e impuestos netos. |
| `PIB real` | Medido a precios de un año base. Elimina el efecto de la inflación. |
| `deflactor del PIB` | `PIB nominal / PIB real × 100`. Índice de precios de toda la producción. |
| `PIB per cápita` | PIB dividido por la población. Aproxima el nivel de vida promedio, no su distribución. |

## 🧠 Modelo mental

El PIB se puede medir de tres formas que **deben dar el mismo resultado**:

```text
lo que se PRODUCE  =  lo que se GASTA  =  lo que se GANA
   valor agregado       C + I + G + XN     remuneraciones + excedente
```

La identidad no es una coincidencia: todo lo producido se vende (o se acumula como inventario, que
cuenta como inversión), y todo lo vendido se convierte en ingreso de alguien.

## 📖 Desarrollo

### 1. Los tres enfoques

**Por producción (valor agregado):**

```text
    trigo            productor vende a 100     valor agregado 100
    harina           molino vende a 180        valor agregado  80
    pan              panadería vende a 300     valor agregado 120
    PIB = 300 (valor final) = 100 + 80 + 120 (suma de valores agregados) ✔
```

Sumar 100 + 180 + 300 = 580 sería **doble contabilización**: el trigo se contaría tres veces.

**Por gasto:**

```text
PIB = C + I + G + (X − M)

C  consumo de los hogares
I  formación bruta de capital fijo + variación de existencias
G  gasto de gobierno en bienes y servicios (no transferencias)
X  exportaciones
M  importaciones (se restan porque ya están en C, I o G)
```

**Por ingreso:**

```text
PIB = remuneraciones + excedente de explotación bruto
    + impuestos netos sobre la producción y las importaciones
```

### 2. Composición típica del gasto

| Componente | Rango habitual | Volatilidad |
|---|---|---|
| Consumo (C) | 55–70 % | Baja |
| Inversión (I) | 15–28 % | **Muy alta** |
| Gasto de gobierno (G) | 10–25 % | Baja |
| Exportaciones netas (X−M) | −5 a +10 % | Alta |

La inversión es el componente más pequeño y el más volátil: **suele explicar la mayor parte de la
variación del PIB en un ciclo**, aunque represente menos de un cuarto del total. Por eso es la variable
que más se vigila para anticipar una recesión, y la que más responde a la tasa de interés (Parte 6,
clase 14).

### 3. Nominal, real y per cápita

```text
PIB nominal año 1   180 000 000 · PIB real (base año 1)  180 000 000 · deflactor 100,0
PIB nominal año 2   201 600 000 · PIB real               190 800 000 · deflactor 105,7

crecimiento nominal = 12,0 %
crecimiento real    =  6,0 %
inflación implícita = (105,7/100,0) − 1 = 5,7 %
```

Con población creciendo 1,1 %:

```text
crecimiento del PIB real per cápita = (1,060/1,011) − 1 = 4,85 %
```

**El crecimiento per cápita es el que aproxima la mejora del nivel de vida.** Un país que crece 3 % con
población creciendo 3 % no mejora en promedio.

### 4. Qué no mide el PIB

```text
· producción doméstica no remunerada (cuidado, trabajo del hogar)
· economía informal y actividades ilegales (parcialmente estimadas)
· distribución del ingreso: dos países con igual PIB per cápita pueden ser muy distintos
· agotamiento de recursos naturales y daño ambiental
· calidad de vida, salud, educación, seguridad
· mejoras de calidad no capturadas por los precios
```

La consecuencia práctica para un analista: **el PIB es un buen indicador de actividad y un mal
indicador de bienestar**. Para lo segundo se usan indicadores complementarios como el índice de
desarrollo humano o medidas de distribución. Confundirlos lleva a conclusiones erróneas de política y
de negocio.

### 5. PIB y cartera bancaria

La relación es empíricamente robusta y con rezago:

```text
crecimiento del PIB  →  (rezago 2–4 trimestres)  →  crecimiento de colocaciones
caída del PIB        →  (rezago 3–6 trimestres)  →  aumento de la morosidad
```

| Fase del ciclo | Colocaciones | Morosidad | Provisiones |
|---|---|---|---|
| Expansión | Crecen | Baja | Bajas |
| Peak | Crecen fuerte | Muy baja | Mínimas |
| Contracción | Se desaceleran | Empieza a subir | Suben |
| Recesión | Caen | Alta | Altas |
| Recuperación | Se estabilizan | Alta con rezago | Empiezan a bajar |

El rezago de la morosidad es la razón por la cual **el peor momento de la cartera ocurre después del
peor momento de la economía**, y por la que los modelos de provisión de la Parte 9, clase 14,
incorporan proyecciones macroeconómicas.

## 🧮 Ejemplo guiado

**Situación.** Un banco proyecta su cartera para el próximo año con estos datos macroeconómicos.

| | Año −2 | Año −1 | Año 0 | Proyección año 1 |
|---|---:|---:|---:|---:|
| PIB real (var. %) | 3,8 % | 2,1 % | −0,6 % | 1,4 % |
| Consumo (var. %) | 4,2 % | 2,8 % | 0,3 % | 1,8 % |
| Inversión (var. %) | 6,1 % | −1,4 % | −8,2 % | 0,9 % |
| Desempleo | 7,1 % | 7,8 % | 9,3 % | 9,0 % |
| Colocaciones consumo (var. %) | 8,4 % | 5,1 % | 1,2 % | ? |
| Morosidad consumo | 1,8 % | 2,1 % | 2,9 % | ? |

**Paso 1 — verifica el patrón de rezago histórico.**

```text
PIB año −2: 3,8 %  → colocaciones año −1: 5,1 %   (rezago ~4 trimestres)
PIB año −1: 2,1 %  → colocaciones año 0:  1,2 %
```

La relación se sostiene con un rezago aproximado de un año.

**Paso 2 — proyecta colocaciones.**

```text
PIB año 0: −0,6 %  → colocaciones año 1 ≈ contracción o crecimiento nulo
estimación: −1,0 % a +0,5 %
```

**Paso 3 — proyecta morosidad.**

```text
la morosidad reacciona con rezago de 3–6 trimestres a la caída del PIB
el PIB cayó en el año 0 → el peor momento de morosidad es el año 1, no el año 0

morosidad año 0: 2,9 %
proyección año 1: 3,6 % a 4,2 %
```

**Paso 4 — el componente que más informa.**

```text
inversión cayó 8,2 % en el año 0 y proyecta +0,9 % en el año 1
→ la recuperación de la inversión es débil
→ la demanda de crédito comercial seguirá deprimida
→ el desempleo baja solo 0,3 puntos: la capacidad de pago de los hogares no mejora
```

**Paso 5 — traduce a provisiones.**

```text
cartera de consumo 8 400 000 millones
morosidad esperada 3,9 % (punto medio)
severidad (LGD) 62 %
pérdida esperada = 8 400 000 × 0,039 × 0,62 = 203 112 millones
provisión del año 0 (morosidad 2,9 %) = 151 032 millones
INCREMENTO DE PROVISIONES = 52 080 millones
```

**Paso 6 — implicancias de negocio.**

```text
1. el resultado del año 1 será menor por mayor provisión, aunque las colocaciones no caigan
2. la política de originación debe endurecerse ANTES, no después de ver la morosidad
3. el crecimiento del año 1 no vendrá del volumen: debe venir de margen o de comisiones
4. el peor trimestre de morosidad se espera a mediados del año 1, no ahora
```

**Interpreta:** los datos macroeconómicos permiten anticipar en tres o cuatro trimestres el
comportamiento de la cartera. **La decisión más valiosa —endurecer la originación— debe tomarse cuando
los indicadores de cartera todavía se ven bien**, y esa es exactamente la razón por la que un banco
tiene un área que sigue la economía agregada.

## 🏦 Del cliente al banco

| Indicador | Uso bancario | Parte |
|---|---|---|
| PIB real | Proyección de colocaciones y de riesgo | 11, clase 13 |
| Inversión | Anticipa demanda de crédito comercial | 13, clase 4 |
| Desempleo | Predictor de morosidad de consumo | 9, clase 10 |
| PIB per cápita | Segmentación y potencial de mercado | 15, clase 6 |
| Escenarios macro | Insumo de las pruebas de estrés | 11, clase 13 |

## 🧪 Práctica

En `labs/lab-03.md`:

1. Calcula el PIB por los tres enfoques con un caso sencillo y verifica su equivalencia.
2. Descompón el PIB de tu país por gasto de los últimos cinco años y calcula la volatilidad de cada componente.
3. Calcula PIB real, deflactor y crecimiento per cápita de una serie.
4. Estima la relación con rezago entre PIB y colocaciones o morosidad con datos públicos.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se suman valores de todas las etapas | Doble contabilización | Suma valores agregados o solo bienes finales. |
| Se compara PIB nominal entre años | No se deflactó | Usa PIB real para comparar. |
| Se concluye mejora del nivel de vida | No se ajustó por población | Usa PIB per cápita. |
| El PIB se interpreta como bienestar | Alcance del indicador | Complementa con indicadores sociales. |
| Se espera que la morosidad suba con el PIB | Rezago ignorado | La morosidad reacciona 3–6 trimestres después. |
| Se incluyen transferencias en G | Definición incorrecta | G es gasto en bienes y servicios, no transferencias. |

## ❓ Preguntas de comprobación

1. ¿Por qué sumar el valor de todas las etapas productivas sobrestima el PIB?
2. Escribe la identidad del gasto y explica por qué se restan las importaciones.
3. ¿Qué componente del PIB es más volátil y por qué importa para un banco?
4. Nombra cuatro cosas que el PIB no mide.
5. ¿Por qué el peor momento de la morosidad ocurre después del peor momento de la economía?

## 📥 Entregable

Guarda en `portfolio/parte-06/clase-05/`:

- el PIB calculado por los tres enfoques con su equivalencia verificada;
- la descomposición por gasto de tu país con la volatilidad de cada componente;
- la serie de PIB real, deflactor y crecimiento per cápita;
- la estimación de la relación con rezago entre PIB y un indicador de cartera, con su fuente.

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

- Blanchard, O. (2021). *Macroeconomía* (8.ª ed.). Pearson. Capítulos 2 y 3: medición de la actividad y el mercado de bienes.
- Mankiw, N. G. (2021). *Principios de economía* (9.ª ed.). Cengage. Capítulo 23: medición del ingreso nacional.
- International Monetary Fund et al. (2009). *System of National Accounts 2008*. Naciones Unidas. Metodología estándar de las cuentas nacionales. <https://unstats.un.org/unsd/nationalaccount/>
- Stiglitz, J., Sen, A. y Fitoussi, J. (2010). *Mis-measuring Our Lives: Why GDP Doesn't Add Up*. The New Press. Límites del PIB como medida de bienestar.
- Borio, C., Drehmann, M. y Xia, D. (2020). "Forecasting recessions: the importance of the financial cycle". *BIS Working Papers*. Relación entre ciclo financiero y actividad.
- Verificación local: descarga las cuentas nacionales publicadas por el banco central o el instituto de estadística de tu país, con su año base y fecha de revisión.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 04 · Competencia y estructuras de mercado](04-competencia-y-estructuras-de-mercado.md) | [Parte 06](../README.md) · [Programa](../../../SYLLABUS.md) | [06 · Inflación →](06-inflacion.md) |
<!-- gen:footer:end -->
