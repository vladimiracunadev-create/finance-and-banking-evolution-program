<!-- meta
part: 7
class: 2
title: "Tasas equivalentes"
level: avanzado
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 02 · Tasas equivalentes

> [← 01 · Tasas nominales y efectivas](01-tasas-nominales-y-efectivas.md) · [Índice de la parte](../README.md) · [03 · Conversión de periodicidades →](03-conversion-de-periodicidades.md)

**Parte 07 — Matemática financiera avanzada** · **Nivel:** Avanzado — perfil analista · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Construir el puente entre cualquier par de tasas de periodicidades distintas, que es la operación que
permite comparar, calzar y estructurar. Un tesorero que capta a 30 días y coloca a 180 necesita saber
exactamente qué tasa a 30 días equivale a una a 180, y esta clase entrega ese aparato.

La clase anterior convirtió entre nominal y efectiva. Esta generaliza esa conversión a cualquier par de periodicidades, y añade lo que hace falta para trabajar con curvas: la tasa implícita entre dos plazos, que es la que el mercado está descontando aunque nadie la publique.

## 📚 Objetivos

Al finalizar podrás:

1. **Calcular** la tasa equivalente entre dos periodicidades cualesquiera.
2. **Distinguir** tasas equivalentes de tasas proporcionales.
3. **Construir** e interpretar tasas forward implícitas.
4. **Aplicar** la equivalencia al calce de plazos de una tesorería.
5. **Detectar** arbitrajes aparentes que desaparecen al usar tasas equivalentes.

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

Los tres primeros términos son la equivalencia y su cálculo; los tres siguientes, lo que se deduce de una curva. La distinción entre **tasas equivalentes y proporcionales** es la que hay que fijar: las proporcionales se obtienen dividiendo y son incorrectas salvo en interés simple.

| Concepto | Comprensión verificable |
|---|---|
| `tasas equivalentes` | Producen el mismo monto final en el mismo plazo, con distinta periodicidad. |
| `tasas proporcionales` | Se obtienen dividiendo o multiplicando linealmente. Solo válidas para tasas nominales. |
| `fórmula de equivalencia` | `(1 + i₁)^n₁ = (1 + i₂)^n₂` para el mismo plazo. |
| `tasa forward implícita` | Tasa futura que hace indiferente invertir a plazo largo o encadenar plazos cortos. |
| `curva de rendimiento` | Conjunto de tasas por plazo. Su forma contiene las tasas forward. |
| `arbitraje` | Ganancia sin riesgo por inconsistencia de precios. En equilibrio no debería existir. |

## 🧠 Modelo mental

Dos tasas son equivalentes si **llevan el mismo capital al mismo monto en el mismo tiempo**:

```text
1 000 000 al 1,5 % mensual durante 12 meses  → 1 195 618
1 000 000 al 19,5618 % anual durante 1 año   → 1 195 618
→ equivalentes
```

Y son **proporcionales** si una se obtiene de la otra dividiendo: `18 % / 12 = 1,5 %`. Proporcional y
equivalente coinciden solo en interés simple; con capitalización, nunca.

## 📖 Desarrollo

### 1. La fórmula general

Una sola fórmula convierte entre dos periodicidades cualesquiera, y de ella salen todos los casos particulares de la clase anterior.

```text
(1 + i₁)^m₁ = (1 + i₂)^m₂

donde m₁ y m₂ son el número de periodos por año de cada tasa
```

Despejando:

```text
i₂ = (1 + i₁)^(m₁/m₂) − 1
```

Ejemplos:

```text
de mensual a anual:      i_a = (1 + i_m)^12 − 1
de anual a mensual:      i_m = (1 + i_a)^(1/12) − 1
de trimestral a semestral: i_s = (1 + i_t)^2 − 1
de 45 días a 90 días:    i_90 = (1 + i_45)^2 − 1
de 30 días a 47 días:    i_47 = (1 + i_30)^(47/30) − 1
```

### 2. Tabla de equivalencias

Para una TEA de 15 %:

| Periodicidad | Periodos/año | Tasa equivalente |
|---|---:|---:|
| Anual | 1 | 15,000000 % |
| Semestral | 2 | 7,238053 % |
| Cuatrimestral | 3 | 4,768955 % |
| Trimestral | 4 | 3,555810 % |
| Bimestral | 6 | 2,356176 % |
| Mensual | 12 | 1,171492 % |
| Quincenal | 24 | 0,582669 % |
| Diaria (365) | 365 | 0,038300 % |

Verificación de una fila:

```text
(1,01171492)^12 − 1 = 0,150000 ✔
```

Compárese con las proporcionales de una nominal del 15 %:

| Periodicidad | Proporcional | Equivalente | Diferencia |
|---|---:|---:|---:|
| Mensual | 1,250000 % | 1,171492 % | 0,078508 pp |
| Trimestral | 3,750000 % | 3,555810 % | 0,194190 pp |

Sobre un crédito de 100 millones a 36 meses, usar 1,25 % en lugar de 1,171492 % aumenta la cuota en
aproximadamente 130 000 mensuales.

### 3. Tasas forward implícitas

Si conoces las tasas a dos plazos, la tasa forward es la que hace indiferente ambas estrategias:

```text
(1 + i_largo)^n_largo = (1 + i_corto)^n_corto × (1 + f)^(n_largo − n_corto)
```

Con dos tasas observadas en la curva, la igualdad se despeja para obtener la tasa que el mercado espera para el tramo intermedio.

```text
tasa a 1 año  = 6,0 %
tasa a 2 años = 6,8 %

(1,068)^2 = (1,06)^1 × (1 + f)^1
1,140624 = 1,06 × (1 + f)
f = 1,140624/1,06 − 1 = 7,6060 %
```

Lectura: **el mercado espera que la tasa a un año, dentro de un año, sea 7,606 %**. No es una
predicción con certeza: es la tasa que hace equivalentes las dos estrategias hoy.

Uso práctico: si tu expectativa de la tasa a un año dentro de un año es menor que 7,606 %, conviene
invertir a dos años; si es mayor, conviene invertir a un año y reinvertir.

### 4. Aplicación al calce de plazos

Un banco capta a 90 días al 5,2 % efectivo anual y quiere colocar a 360 días. Necesita saber a qué
tasa debe colocar para no perder si las tasas de captación suben.

```text
estrategia: captar 4 veces a 90 días
si la tasa se mantiene: costo anual = 5,2 %
si la tasa sube 1 punto en cada renovación:
  periodo 1: 5,2 % · periodo 2: 6,2 % · periodo 3: 7,2 % · periodo 4: 8,2 %
  costo efectivo anual = [(1,052)^0,25 × (1,062)^0,25 × (1,072)^0,25 × (1,082)^0,25] − 1
                       = 6,6903 %
```

De ese escenario se deduce el rendimiento mínimo que debe exigirse a la colocación larga para que la estrategia no pierda dinero.

```text
la colocación a 360 días debe rendir al menos 6,69 % + margen
para cubrir el escenario de alza
```

Este cálculo es la base de la gestión de riesgo de tasa de la Parte 11, clase 5: **el descalce de
plazos se cuantifica con tasas equivalentes**.

### 5. Arbitrajes aparentes

Cuando dos tasas parecen ofrecer una ganancia sin riesgo, casi siempre hay un supuesto oculto. La tabla recoge los casos habituales con el supuesto que los explica.

```text
oferta A: depósito a 180 días al 3,10 % del periodo
oferta B: depósito a 90 días al 1,52 % del periodo, renovable

¿conviene encadenar dos veces B?
```

```text
B encadenado: (1,0152)^2 − 1 = 3,0631 %
A:                              3,1000 %
→ A es mejor por 0,0369 puntos
```

Pero si la tasa forward a 90 días dentro de 90 días fuera del 1,60 %:

```text
B encadenado: (1,0152)(1,0160) − 1 = 3,1443 %  → ahora B es mejor
```

**No hay arbitraje: hay una apuesta sobre la tasa futura.** Confundir ambas cosas es el error que
convierte una decisión de tesorería en una posición especulativa no reconocida.

## 🧮 Ejemplo guiado

El ejemplo obtiene la tasa forward implícita entre dos plazos de una curva. Conviene fijarse en el sentido de la operación: la forward es la tasa que hace indiferentes las dos estrategias.

**Situación.** La tesorería de un banco enfrenta esta curva de captación y debe decidir la estructura
de fondeo de una colocación de 12 meses por 8 000 millones.

```text
CURVA DE CAPTACIÓN (efectiva anual)
  30 días    5,10 %
  90 días    5,45 %
  180 días   5,90 %
  360 días   6,35 %

la colocación rinde 9,80 % efectivo anual a 360 días
```

**Paso 1 — margen de la estrategia calzada.**

```text
captar a 360 días al 6,35 %
margen = 9,80 % − 6,35 % = 3,45 puntos
resultado = 8 000 × 0,0345 = 276 millones
```

**Paso 2 — margen de la estrategia descalzada (captar a 90 días, renovar 4 veces).**

```text
si las tasas se mantienen:
  costo = 5,45 %
  margen = 4,35 puntos → resultado 348 millones
  ganancia adicional frente a calzar: 72 millones
```

**Paso 3 — calcula las tasas forward implícitas.**

```text
f(90→180) : (1,0590)^0,5 = (1,0545)^0,25 × (1 + f)^0,25
  → f = 6,3512 %
f(180→360): (1,0635)^1 = (1,0590)^0,5 × (1 + f)^0,5
  → f = 6,8016 %
```

**Paso 4 — costo de la estrategia descalzada si las forward se cumplen.**

```text
costo efectivo = (1,0545)^0,25 × (1,0545)^0,25 × ... 
más precisamente, encadenando con las forward implícitas:
  (1,0545)^0,25 × (1,0635)^0,25 × (1,0680)^0,25 × (1,0725)^0,25 − 1 ≈ 6,35 %
```

**Si las tasas evolucionan según las forward implícitas, ambas estrategias cuestan lo mismo.** Ese es
precisamente el significado de la tasa forward.

**Paso 5 — la estrategia descalzada es una apuesta.**

```text
gana si las tasas suben MENOS que lo implícito en la curva
pierde si suben MÁS

escenario adverso: la tasa de política sube 250 pb en 6 meses
  costo estimado de la estrategia corta ≈ 7,60 %
  margen = 2,20 puntos → resultado 176 millones
  pérdida frente a calzar: 100 millones
```

**Paso 6 — decisión y su formulación correcta.**

```text
NO decir: "captar a 90 días es más barato"
SÍ decir: "captar a 90 días gana 72 millones si las tasas se mantienen,
           cuesta 100 millones si suben 250 pb, y es indiferente si evolucionan
           según las tasas forward implícitas en la curva.
           Esta es una posición de riesgo de tasa de 8 000 millones a 12 meses,
           y debe autorizarse como tal por el comité de activos y pasivos."
```

**Interpreta:** las tasas equivalentes y forward convierten una comparación aparentemente obvia
—"5,45 % es menos que 6,35 %"— en lo que realmente es: **una decisión de asumir o no riesgo de tasa,
con su ganancia y su pérdida cuantificadas**. Esa reformulación es lo que distingue una tesorería
profesional.

## 🏦 Del cliente al banco

El cliente compara plazos y el banco extrae de la curva la tasa a la que puede fondearse. La tabla enfrenta las dos lecturas.

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| Tasas equivalentes | Comparación de fondeo y colocación | 10, clase 12 |
| Tasa forward | Precio implícito de las expectativas | 8, clase 4 |
| Descalce de plazos | Riesgo de tasa del libro de banca | 11, clase 5 |
| Curva de rendimiento | Insumo de pricing y de valoración | 8, clase 4 |
| Estrategia descalzada | Posición que requiere autorización de límites | 11, clase 12 |

## 🧪 Práctica

El laboratorio pide construir tasas equivalentes y forwards implícitas a partir de una curva sintética. El ejercicio incluye un arbitraje aparente que se deshace al declarar el supuesto.

En `labs/lab-01.md`, sección de equivalencias:

1. Construye la tabla de equivalencias de tres TEA distintas en ocho periodicidades.
2. Compara tasas proporcionales y equivalentes y cuantifica el error en una cuota real.
3. Calcula las tasas forward implícitas de una curva real de tu mercado.
4. Evalúa una estrategia de fondeo descalzada con tres escenarios de tasas.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen equivalencias que no cuadran. La causa casi siempre es haber usado tasas proporcionales donde correspondían equivalentes.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se dividen tasas efectivas | Se usó proporcionalidad | Usa la fórmula de equivalencia con exponentes. |
| Se cree que fondearse corto es siempre más barato | La curva ya incorpora las expectativas | Calcula las tasas forward implícitas. |
| Se detecta un arbitraje que no existe | No se compararon plazos equivalentes | Lleva todo al mismo plazo. |
| Se toma una posición descalzada sin autorización | No se reconoció como riesgo de tasa | Formula la decisión como posición de riesgo. |
| La tasa forward se interpreta como predicción | Concepto mal entendido | Es la tasa de indiferencia, no un pronóstico. |
| Se comparan tasas de bases de días distintas | Convención ignorada | Homologa la base antes de comparar. |

## ❓ Preguntas de comprobación

1. Escribe la fórmula de equivalencia y aplícala de trimestral a mensual.
2. ¿Cuál es la diferencia entre tasa proporcional y equivalente, y cuándo coinciden?
3. Calcula la tasa forward a un año dentro de un año con tasas de 5,5 % y 6,4 %.
4. ¿Qué significa exactamente que una estrategia de fondeo corto sea "más barata"?
5. ¿Por qué una tasa forward no es una predicción?

## 📥 Entregable

Guarda en `portfolio/parte-07/clase-02/`:

- las tablas de equivalencias de tres TEA en ocho periodicidades;
- la comparación proporcional vs. equivalente con el error cuantificado en una cuota;
- las tasas forward implícitas de una curva real con su fuente;
- la evaluación de una estrategia de fondeo descalzada en tres escenarios.

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

- Kellison, S. (2008). *The Theory of Interest* (3.ª ed.). McGraw-Hill/Irwin. Capítulo 1: tasas equivalentes y fuerza de interés.
- Broverman, S. (2017). *Mathematics of Investment and Credit* (7.ª ed.). ACTEX. Capítulo 1: equivalencia y capitalización.
- Fabozzi, F. (2021). *Bond Markets, Analysis, and Strategies* (10.ª ed.). MIT Press. Capítulo 5: tasas spot y forward.
- Hull, J. (2021). *Options, Futures, and Other Derivatives* (11.ª ed.). Pearson. Capítulo 4: tasas cero, forward y acuerdos de tasa futura.
- Saunders, A. y Cornett, M. (2021). *Financial Institutions Management* (10.ª ed.). McGraw-Hill. Gestión del descalce de plazos.
- Verificación local: descarga la curva de tasas de captación por plazo publicada por el supervisor o el banco central de tu país.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 01 · Tasas nominales y efectivas](01-tasas-nominales-y-efectivas.md) | [Parte 07](../README.md) · [Programa](../../../SYLLABUS.md) | [03 · Conversión de periodicidades →](03-conversion-de-periodicidades.md) |
<!-- gen:footer:end -->
