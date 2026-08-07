<!-- meta
part: 6
class: 4
title: "Competencia y estructuras de mercado"
level: intermedio
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 04 · Competencia y estructuras de mercado

> [← 03 · Elasticidad](03-elasticidad.md) · [Índice de la parte](../README.md) · [05 · Producto e ingreso nacional →](05-producto-e-ingreso-nacional.md)

**Parte 06 — Economía y sistema financiero** · **Nivel:** Intermedio — requiere las partes anteriores · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Entender por qué el precio de un producto depende tanto de la estructura del mercado como de sus
costos, y aplicar ese marco al sistema financiero, que en la mayoría de los países es un oligopolio
con barreras de entrada regulatorias. Esta clase entrega las herramientas para medir concentración y
para leer el comportamiento competitivo de una industria.

Las clases anteriores suponen mercados donde nadie fija el precio. Esta levanta ese supuesto, porque la banca no es uno de esos mercados: es concentrada, tiene barreras de entrada altas y sus participantes tienen poder sobre el precio. Medir esa concentración es un ejercicio con norma propia.

## 📚 Objetivos

Al finalizar podrás:

1. **Clasificar** un mercado según su estructura y verificar los supuestos.
2. **Calcular** índices de concentración e interpretarlos.
3. **Identificar** barreras de entrada y su origen.
4. **Explicar** la diferenciación de producto y su efecto sobre el poder de mercado.
5. **Analizar** la competencia bancaria de tu mercado con datos públicos.

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

Los cuatro primeros términos son las estructuras posibles y los tres últimos, las herramientas para medir dónde está un mercado concreto. El **índice Herfindahl-Hirschman** es el que usan las autoridades de competencia, y conviene saber calcularlo porque decide autorizaciones de fusiones.

| Concepto | Comprensión verificable |
|---|---|
| `competencia perfecta` | Muchos oferentes, producto homogéneo, información completa, libre entrada. Nadie fija el precio. |
| `monopolio` | Un solo oferente sin sustitutos cercanos. Fija precio y restringe cantidad. |
| `oligopolio` | Pocos oferentes interdependientes. Cada uno considera la reacción de los demás. |
| `competencia monopolística` | Muchos oferentes con producto diferenciado. Poder de mercado limitado. |
| `barrera de entrada` | Obstáculo que impide o encarece el ingreso de nuevos competidores. |
| `índice de concentración (CRn)` | Participación conjunta de las n mayores empresas. |
| `índice Herfindahl-Hirschman` | Suma de los cuadrados de las participaciones. Más sensible a la asimetría. |

## 🧠 Modelo mental

La estructura determina **cuánto poder tiene cada actor sobre el precio**:

```text
competencia perfecta      → precio = costo marginal, sin poder de mercado
competencia monopolística → precio > costo marginal por diferenciación
oligopolio                → precio depende de la interacción estratégica
monopolio                 → precio muy por sobre el costo marginal
```

La banca minorista de la mayoría de los países se ubica entre las dos últimas: pocos actores grandes,
productos parcialmente diferenciados y barreras de entrada regulatorias significativas.

## 📖 Desarrollo

### 1. Las cuatro estructuras

Las cuatro estructuras se distinguen por el número de participantes, la diferenciación y las barreras. La tabla las separa con un ejemplo financiero de cada una.

| | Perfecta | Monopolística | Oligopolio | Monopolio |
|---|---|---|---|---|
| Número de oferentes | Muchísimos | Muchos | Pocos | Uno |
| Producto | Homogéneo | Diferenciado | Homogéneo o diferenciado | Único |
| Poder sobre el precio | Ninguno | Limitado | Considerable | Alto |
| Barreras de entrada | Ninguna | Bajas | Altas | Muy altas |
| Interdependencia | No | No | **Sí** | No aplica |
| Ejemplo aproximado | Commodities agrícolas | Restaurantes, peluquerías | Banca, telecomunicaciones | Servicios de red regulados |

La fila de interdependencia distingue al oligopolio: **cada actor decide considerando la reacción de
los otros**, lo que produce comportamientos que ninguna otra estructura genera, como el seguimiento de
precios y la rigidez a la baja.

### 2. Medir la concentración

La concentración se mide con dos índices que dan lecturas complementarias. El procedimiento siguiente los calcula.

```text
CR4 = suma de las participaciones de las 4 mayores
HHI = Σ (participación en %)²
```

Ejemplo de un sistema bancario:

| Banco | Participación |
|---|---:|
| A | 24 % |
| B | 21 % |
| C | 17 % |
| D | 13 % |
| E | 8 % |
| F | 6 % |
| Otros (8 bancos) | 11 % |

Con esas participaciones se calculan los dos indicadores habituales, que
resumen la misma realidad con distinta sensibilidad al tamaño.

```text
CR4 = 24 + 21 + 17 + 13 = 75 %
HHI = 24² + 21² + 17² + 13² + 8² + 6² + (8 bancos de ~1,4 %)
    = 576 + 441 + 289 + 169 + 64 + 36 + ~16 = 1 591
```

Interpretación habitual del HHI en análisis de competencia:

| HHI | Lectura |
|---|---|
| < 1 500 | Mercado no concentrado |
| 1 500–2 500 | Moderadamente concentrado |
| > 2 500 | Altamente concentrado |

Con 1 591, este sistema es **moderadamente concentrado**. Un CR4 de 75 % es alto y frecuente en banca:
la mayoría de los sistemas bancarios del mundo tiene los cuatro mayores por sobre el 60 %.

### 3. Barreras de entrada en banca

La banca tiene barreras propias, y algunas son regulatorias por diseño. La tabla las recoge con su origen.

| Barrera | Origen | Efecto |
|---|---|---|
| Licencia bancaria | Regulatorio | Impide la entrada sin autorización |
| Capital mínimo | Regulatorio | Exige inversión inicial alta |
| Cumplimiento normativo | Regulatorio | Costo fijo elevado, independiente del tamaño |
| Red de sucursales y cajeros | Económico | Menos relevante con la digitalización |
| Acceso al sistema de pagos | Estructural | Depende de participar en la infraestructura |
| Confianza y marca | Económico | La captación exige reputación |
| Costo de cambio del cliente | Económico | Trasladar productos es engorroso |
| Datos históricos de comportamiento | Informacional | Los incumbentes tienen mejor información de riesgo |

Las tres últimas son las que la regulación reciente ha intentado reducir: la **portabilidad
financiera** ataca el costo de cambio, y las **finanzas abiertas** atacan la asimetría de datos
(Parte 14, clase 3). Ambas son intervenciones sobre la estructura competitiva, no sobre el precio.

### 4. Diferenciación de producto

En un mercado concentrado, la competencia se traslada de precio a diferenciación. La tabla recoge las formas que toma en banca.

```text
un producto diferenciado permite cobrar más que el sustituto más barato
sin perder a todos los clientes
```

Formas de diferenciación en banca:

| Forma | Ejemplo | Sostenibilidad |
|---|---|---|
| Conveniencia | Red de sucursales, aplicación superior | Media; se copia |
| Servicio | Atención personalizada, ejecutivo asignado | Media-alta |
| Marca y confianza | Percepción de solidez | Alta; toma años construirla |
| Ecosistema | Productos integrados, beneficios cruzados | Alta; aumenta el costo de cambio |
| Segmento | Especialización en un nicho | Alta si el nicho es defendible |
| Precio | Ser el más barato | **Baja**: cualquiera puede igualarla |

La última fila es la trampa competitiva del oligopolio: **una rebaja de precio es la ventaja más fácil
de imitar**, de modo que su efecto sobre la participación es transitorio y su efecto sobre el margen
es permanente.

### 5. Comportamiento oligopólico

Fenómenos observables que la estructura predice:

```text
· liderazgo de precios: un actor mueve y los demás siguen
· rigidez a la baja: las tasas de colocación bajan más lento de lo que suben
· competencia en dimensiones distintas del precio (beneficios, canales, publicidad)
· estabilidad de participaciones de mercado durante años
```

La rigidez asimétrica está ampliamente documentada: cuando la tasa de política monetaria sube, las
tasas de colocación suben rápido; cuando baja, bajan más lentamente. La Parte 6, clase 14, examina ese
fenómeno como parte del mecanismo de transmisión.

## 🧮 Ejemplo guiado

**Situación.** Analiza la competencia del mercado de crédito de consumo de un país con estos datos
públicos.

| Actor | Colocaciones (miles de millones) | Tasa promedio |
|---|---:|---:|
| Banco A | 3 200 | 21,4 % |
| Banco B | 2 900 | 21,8 % |
| Banco C | 2 100 | 22,1 % |
| Banco D | 1 400 | 22,6 % |
| Cajas y cooperativas | 1 800 | 24,9 % |
| Emisores no bancarios | 1 100 | 32,4 % |
| Fintech de crédito | 500 | 28,7 % |
| **Total** | **13 000** | |

**Paso 1 — participaciones y concentración.**

```text
A 24,6 % · B 22,3 % · C 16,2 % · D 10,8 % · Cajas 13,8 % · No bancarios 8,5 % · Fintech 3,8 %

CR4 = 24,6 + 22,3 + 16,2 + 13,8 = 76,9 %
HHI = 605 + 497 + 262 + 117 + 190 + 72 + 14 = 1 757  → moderadamente concentrado
```

**Paso 2 — dispersión de tasas entre los cuatro bancos grandes.**

```text
rango 21,4 % a 22,6 % → 1,2 puntos porcentuales
coeficiente de variación de las tasas de los cuatro bancos ≈ 2,4 %
```

Una dispersión de 1,2 puntos entre los cuatro mayores, en un producto sustancialmente homogéneo, es
**baja**. Es consistente con comportamiento oligopólico: los precios se mueven juntos.

**Paso 3 — el segmento no bancario.**

```text
emisores no bancarios: 32,4 %, 11 puntos por sobre los bancos
fintech: 28,7 %, 7 puntos por sobre
```

Dos hipótesis, que se verifican con datos distintos:

| Hipótesis | Cómo se verifica |
|---|---|
| Atienden a clientes de mayor riesgo | Comparar morosidad y perfil de deudores por segmento |
| Cobran una prima por menor competencia en su nicho | Comparar costos operativos y márgenes |

**Paso 4 — la prueba discriminante.**

```text
morosidad promedio de la cartera bancaria de consumo   2,1 %
morosidad de emisores no bancarios                     6,8 %
diferencia en pérdida esperada (con LGD 65 %)          ≈ 3,1 puntos porcentuales
brecha de tasa observada                               11,0 puntos porcentuales
brecha NO explicada por riesgo                          7,9 puntos porcentuales
```

**Paso 5 — investigar la brecha no explicada.**

```text
costo operativo por operación: los no bancarios operan montos menores
  monto promedio bancario 3 100 000 · no bancario 480 000
  costo operativo fijo por operación ≈ 42 000
  como % del monto: bancario 1,4 % · no bancario 8,8 %  → +7,4 puntos
```

**La brecha se explica casi por completo por el costo operativo del monto pequeño**, no por poder de
mercado. Esa conclusión solo aparece al buscar el dato del monto promedio.

**Paso 6 — conclusión del análisis competitivo.**

```text
· mercado moderadamente concentrado (HHI 1 757)
· CR4 de 76,9 %: alto, típico de banca
· baja dispersión de tasas entre los grandes: comportamiento coordinado en precio
· la brecha con los no bancarios se explica por riesgo y por costo operativo del ticket pequeño
· la competencia efectiva ocurre por canal y por segmento, no por precio general

recomendación de política: reducir barreras al cambio (portabilidad) y a los datos
(finanzas abiertas) tiene más efecto sobre la competencia que un tope de tasa
```

**Interpreta:** el dato más llamativo —una brecha de 11 puntos de tasa— resultó explicable por riesgo y
costos, no por abuso. **La conclusión correcta requirió tres datos adicionales al de las tasas.** Ese
es el estándar de un análisis competitivo serio y la razón por la que las autoridades de competencia
exigen estudios de mercado antes de intervenir.

## 🏦 Del cliente al banco

El cliente compara ofertas y el banco compite en un mercado concentrado. La tabla enfrenta las dos lecturas, y explica por qué las tarifas convergen sin necesidad de acuerdo.

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| Concentración | Análisis de competencia y fusiones | 15, clase 11 |
| Barreras de entrada | Licencias, capital y cumplimiento | 12, clase 1 |
| Diferenciación | Estrategia y propuesta de valor | 15, clase 8 |
| Costo de cambio | Portabilidad financiera | 15, clase 9 |
| Asimetría de datos | Finanzas abiertas | 14, clase 3 |

## 🧪 Práctica

El laboratorio pide calcular los dos índices sobre datos de participación de mercado y clasificar la estructura. El ejercicio incluye el efecto de una fusión hipotética, que es el uso real del índice.

En `labs/lab-02.md`, sección de estructura:

1. Calcula CR4 y HHI del sistema bancario de tu país con datos públicos del supervisor.
2. Clasifica la estructura y verifica los supuestos con evidencia.
3. Identifica cinco barreras de entrada y clasifícalas por origen.
4. Analiza la dispersión de tasas entre actores y formula hipótesis verificables sobre las brechas.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen conclusiones equivocadas sobre competencia. Las causas están en índices calculados sobre mercados mal delimitados.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se concluye abuso por una brecha de tasas | No se controló por riesgo ni costos | Compara pérdida esperada y costo operativo. |
| Se usa solo CR4 | Ignora la asimetría entre actores | Complementa con HHI. |
| Se supone competencia perfecta en banca | Supuestos no verificados | Verifica homogeneidad, entrada e información. |
| Se compite solo por precio | Ventaja fácilmente imitable | Diferencia en dimensiones defendibles. |
| Se ignoran las barreras regulatorias | Análisis incompleto | La licencia y el capital son barreras centrales. |
| Se compara la tasa sin considerar el monto | Costo operativo por operación | Expresa el costo fijo como % del monto. |

## ❓ Preguntas de comprobación

1. ¿Qué distingue un oligopolio de una competencia monopolística?
2. Calcula el HHI de un mercado con participaciones 30, 25, 20, 15 y 10 % e interpreta.
3. Nombra cinco barreras de entrada en banca y su origen.
4. ¿Por qué competir por precio es la ventaja menos sostenible en un oligopolio?
5. Una brecha de 11 puntos de tasa entre dos tipos de oferente. ¿Qué tres datos pides antes de concluir?

## 📥 Entregable

Guarda en `portfolio/parte-06/clase-04/`:

- el CR4 y el HHI del sistema bancario de tu país con la fuente y fecha de los datos;
- la clasificación de la estructura con los supuestos verificados;
- las cinco barreras de entrada identificadas y clasificadas;
- el análisis de dispersión de tasas con las hipótesis verificadas o refutadas.

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

- Mankiw, N. G. (2021). *Principios de economía* (9.ª ed.). Cengage. Capítulos 15 a 17: monopolio, oligopolio y competencia monopolística.
- Tirole, J. (1988). *The Theory of Industrial Organization*. MIT Press. Interdependencia estratégica y barreras de entrada.
- Vives, X. (2016). *Competition and Stability in Banking*. Princeton University Press. Estructura competitiva del sistema bancario y su relación con la estabilidad.
- OECD (2020). *Digital Disruption in Banking and its Impact on Competition*. OCDE. Efecto de las fintech y las finanzas abiertas sobre la competencia. <https://www.oecd.org/competition/>
- U.S. Department of Justice y FTC (2023). *Merger Guidelines*. Umbrales de HHI usados en el análisis de concentración.
- Verificación local: descarga las participaciones de mercado publicadas por el supervisor bancario de tu país y los informes de la autoridad de competencia sobre el sector financiero.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 03 · Elasticidad](03-elasticidad.md) | [Parte 06](../README.md) · [Programa](../../../SYLLABUS.md) | [05 · Producto e ingreso nacional →](05-producto-e-ingreso-nacional.md) |
<!-- gen:footer:end -->
