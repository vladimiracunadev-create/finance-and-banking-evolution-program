<!-- meta
part: 8
class: 9
title: "Diversificación"
level: avanzado
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 09 · Diversificación

> [← 08 · Riesgo y rentabilidad](08-riesgo-y-rentabilidad.md) · [Índice de la parte](../README.md) · [10 · Construcción de portafolios →](10-construccion-de-portafolios.md)

**Parte 08 — Inversiones y mercados** · **Nivel:** Avanzado — perfil analista · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Comprender el único mecanismo de la inversión que **reduce el riesgo sin reducir el retorno esperado**,
y aplicarlo correctamente. La diversificación es más sutil de lo que parece: depende de la
correlación, no del número de instrumentos, y falla precisamente cuando más se necesita.

La clase anterior estableció que hay riesgo eliminable. Esta muestra cómo se elimina, y con qué límites. Su hallazgo incómodo es que la diversificación funciona menos justo cuando más hace falta: las correlaciones aumentan en las crisis, y una cartera que parecía diversificada deja de estarlo.

## 📚 Objetivos

Al finalizar podrás:

1. **Explicar** el mecanismo de la diversificación mediante la correlación.
2. **Calcular** el riesgo de una cartera de dos y de N activos.
3. **Distinguir** diversificación real de diversificación aparente.
4. **Reconocer** por qué las correlaciones aumentan en las crisis.
5. **Diseñar** una cartera diversificada en las dimensiones que importan.

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

Los dos primeros términos miden la relación entre activos; los cinco siguientes, el beneficio que producen y sus límites. La **diversificación aparente** es lo que hay que saber detectar: tener veinte fondos no diversifica si todos siguen al mismo mercado.

| Concepto | Comprensión verificable |
|---|---|
| `correlación (ρ)` | Grado en que dos activos se mueven juntos. Entre −1 y +1. |
| `covarianza` | `ρ × σ₁ × σ₂`. Insumo del cálculo del riesgo de cartera. |
| `beneficio de diversificación` | Reducción del riesgo por combinar activos con `ρ < 1`. |
| `diversificación aparente` | Muchos instrumentos con alta correlación entre sí. No reduce el riesgo. |
| `dimensiones de diversificación` | Emisor, sector, geografía, moneda, clase de activo, factor, horizonte. |
| `correlación condicional` | La correlación en periodos de estrés, habitualmente mayor que la media. |
| `número efectivo de activos` | Medida que corrige el conteo por concentración y correlación. |

## 🧠 Modelo mental

El riesgo de una cartera **no es el promedio de los riesgos**:

```text
σ_cartera² = w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρσ₁σ₂
```

El tercer término es la clave: **cuando `ρ < 1`, el riesgo de la cartera es menor que el promedio
ponderado de los riesgos individuales**. Ese es el único beneficio "gratis" que existe en inversión.

```text
dos activos, cada uno con σ = 20 %, en partes iguales:
  ρ = 1,0  → σ_cartera = 20,0 %   (sin beneficio)
  ρ = 0,5  → σ_cartera = 17,3 %
  ρ = 0,0  → σ_cartera = 14,1 %
  ρ = −0,5 → σ_cartera = 10,0 %
  ρ = −1,0 → σ_cartera = 0,0 %    (riesgo eliminado por completo)
```

## 📖 Desarrollo

### 1. Cartera de dos activos

El caso de dos activos muestra todo el mecanismo con la aritmética mínima. El procedimiento siguiente lo desarrolla.

```text
E(r_p) = w₁ E(r₁) + w₂ E(r₂)
σ_p = √(w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρσ₁σ₂)
```

Las dos fórmulas se aplican a un par de activos con características opuestas y una correlación baja, que es el caso donde la diversificación se nota.

```text
Activo A: E(r) = 11 % · σ = 22 %
Activo B: E(r) = 6 %  · σ = 9 %
ρ = 0,25
```

| w_A | w_B | E(r_p) | σ_p |
|---:|---:|---:|---:|
| 100 % | 0 % | 11,00 % | 22,00 % |
| 80 % | 20 % | 10,00 % | 18,17 % |
| 60 % | 40 % | 9,00 % | 14,66 % |
| 40 % | 60 % | 8,00 % | 11,79 % |
| 20 % | 80 % | 7,00 % | 9,88 % |
| **10 %** | **90 %** | **6,50 %** | **9,05 %** |
| 0 % | 100 % | 6,00 % | 9,00 % |

**El hallazgo:** la cartera de 10 % A / 90 % B tiene σ de 9,05 %, prácticamente igual a B solo
(9,00 %), y **rentabilidad esperada 0,5 puntos mayor**. Añadir un activo más riesgoso puede aumentar
el retorno sin aumentar el riesgo, si la correlación es baja.

Existe una cartera de **mínima varianza**:

```text
w_A* = (σ_B² − ρσ_Aσ_B)/(σ_A² + σ_B² − 2ρσ_Aσ_B)
     = (81 − 0,25×22×9)/(484 + 81 − 2×0,25×22×9)
     = (81 − 49,5)/(565 − 99) = 31,5/466 = 6,76 %
```

Resuelta la expresión, la combinación de mínimo riesgo resulta muy desequilibrada, y su desviación queda por debajo de la del activo más tranquilo.

```text
cartera de mínima varianza: 6,76 % en A, 93,24 % en B
σ = 8,98 % · E(r) = 6,34 %
```

### 2. Cartera de N activos

Al añadir activos, el beneficio de diversificación crece y se agota. El esquema muestra dónde está ese límite.

```text
σ_p² = Σ Σ w_i w_j ρ_ij σ_i σ_j
```

Con N activos de igual peso, igual σ e igual correlación ρ entre pares:

```text
σ_p² = σ²/N + σ²ρ(N−1)/N

cuando N → ∞:  σ_p² → σ²ρ
                σ_p → σ√ρ
```

**El límite inferior del riesgo de una cartera diversificada es `σ√ρ`.**

```text
σ individual = 35 % · ρ promedio = 0,30
límite inferior = 35 % × √0,30 = 19,2 %
```

Por más instrumentos que se agreguen, **el riesgo no baja de 19,2 %**. Ese piso es el riesgo
sistemático de la clase 8.

### 3. Diversificación real y aparente

Contar instrumentos no mide diversificación. La tabla contrasta las dos lecturas y da la medida correcta.

```text
DIVERSIFICACIÓN APARENTE
  30 acciones, todas del mismo país y del mismo sector
  correlación promedio entre ellas: 0,72
  límite inferior = σ√0,72 = 0,85 × σ  → apenas 15 % de reducción

DIVERSIFICACIÓN REAL
  acciones globales de múltiples sectores + bonos + inmuebles
  correlación promedio: 0,28
  límite inferior = σ√0,28 = 0,53 × σ  → 47 % de reducción
```

Prueba práctica para detectar diversificación aparente:

```text
1. calcula la correlación promedio entre tus posiciones
2. si supera 0,60, tu cartera está poco diversificada aunque tenga muchos instrumentos
3. revisa la exposición efectiva por sector, geografía y factor
```

Ejemplo de exposición oculta:

```text
cartera de 25 fondos distintos
al mirar sus carteras subyacentes:
  · 8 de ellos tienen las mismas 5 acciones entre sus principales posiciones
  · exposición efectiva a esas 5 acciones: 19 % de la cartera total
  · el inversionista cree tener 25 posiciones y tiene una concentración del 19 %
```

### 4. Correlaciones en crisis

Las correlaciones no son estables: aumentan cuando los mercados caen. La tabla recoge magnitudes observadas y su consecuencia.

```text
correlación promedio entre acciones globales:
  periodos normales:  0,35 a 0,50
  periodos de estrés: 0,70 a 0,90
```

Este fenómeno —documentado en múltiples episodios— significa que **la diversificación funciona peor
justo cuando más se necesita**. Las razones:

```text
· en crisis, los inversionistas venden todo indistintamente para obtener liquidez
· los factores de riesgo comunes (liquidez, apalancamiento) dominan sobre los específicos
· las llamadas de margen fuerzan ventas correlacionadas
```

Consecuencia práctica:

```text
una cartera diseñada con correlaciones de periodos normales
SUBESTIMA su riesgo en crisis

la prueba correcta es calcular el riesgo de la cartera
con las correlaciones observadas en el peor periodo histórico
```

### 5. Dimensiones de diversificación

Se puede diversificar por varias dimensiones y no todas aportan lo mismo. La tabla las recoge.

| Dimensión | Qué diversifica | Cómo verificar |
|---|---|---|
| Emisor | Riesgo específico de una empresa | Máximo por emisor |
| Sector | Riesgo de una industria | Exposición por sector |
| Geografía | Riesgo país y regulatorio | Exposición por país |
| Moneda | Riesgo cambiario | Exposición por moneda |
| Clase de activo | Riesgo de un mercado completo | Asignación por clase |
| Factor | Estilo (valor, crecimiento, tamaño, calidad) | Exposición factorial |
| Horizonte temporal | Riesgo de entrar en un mal momento | Aportes periódicos |

La última fila —diversificación temporal— merece mención: **aportar periódicamente en lugar de todo de
una vez** reduce el riesgo de haber entrado en el peor momento, a costa de un retorno esperado
levemente menor (porque parte del capital permanece sin invertir).

## 🧮 Ejemplo guiado

El ejemplo calcula el riesgo de una cartera de dos activos a distintas correlaciones. Conviene fijarse en el caso de correlación uno: ahí la diversificación no aporta nada, y es el que se aproxima en una crisis.

**Situación.** Un inversionista con 60 000 000 cree tener una cartera diversificada. Se analiza su
composición efectiva.

```text
POSICIONES DECLARADAS (18 instrumentos)
  6 acciones locales del sector financiero          22 %
  4 acciones locales del sector retail              14 %
  3 fondos accionarios locales                      18 %
  2 fondos de deuda local                           16 %
  1 ETF accionario global                           12 %
  1 fondo inmobiliario local                         8 %
  1 depósito a plazo                                10 %
```

**Paso 1 — exposición efectiva por clase de activo.**

```text
renta variable local:  22 + 14 + 18 = 54 %
renta variable global: 12 %
renta fija local:      16 + 10 = 26 %
inmobiliario local:    8 %

TOTAL exposición local: 88 %
```

**Paso 2 — mira dentro de los fondos.**

```text
los 3 fondos accionarios locales tienen entre sus 5 principales posiciones
las mismas 4 acciones del sector financiero que el inversionista ya posee

exposición directa al sector financiero:  22 %
exposición indirecta vía fondos:          18 % × 0,42 = 7,6 %
EXPOSICIÓN EFECTIVA AL SECTOR FINANCIERO: 29,6 %
```

**Paso 3 — calcula la correlación promedio.**

```text
correlación promedio entre las posiciones de renta variable local: 0,68
correlación entre renta variable local y el ETF global: 0,55
correlación entre renta variable local y el fondo inmobiliario local: 0,61
correlación entre renta variable local y renta fija local: 0,22

correlación promedio ponderada de la cartera: 0,58
```

**Paso 4 — calcula el riesgo efectivo.**

```text
σ individual promedio: 24 %
límite inferior teórico con ρ = 0,58: 24 % × √0,58 = 18,3 %

σ de la cartera calculada: 18,9 %
σ de una cartera realmente diversificada con la misma asignación por clase: 12,4 %
```

**La cartera tiene 6,5 puntos más de riesgo que una equivalente bien diversificada**, sin ningún
retorno esperado adicional.

**Paso 5 — prueba con correlaciones de crisis.**

```text
en el peor periodo de los últimos 15 años:
  correlación entre acciones locales: 0,89
  entre local y global: 0,81
  entre local e inmobiliario: 0,78
  entre acciones y renta fija local: 0,45  ← también subió

σ de la cartera con correlaciones de crisis: 22,7 %
caída máxima estimada: −38 %

la política del inversionista declara pérdida máxima aceptable de 25 %
→ la cartera EXCEDE su propio límite en un escenario de estrés
```

**Paso 6 — rediseño.**

| Dimensión | Actual | Propuesta | Efecto |
|---|---:|---:|---|
| Renta variable local | 54 % | 22 % | Reduce concentración geográfica |
| Renta variable global | 12 % | 32 % | Diversifica país y moneda |
| Renta variable emergente | 0 % | 6 % | Diversifica factor |
| Renta fija local | 26 % | 24 % | Sin cambio material |
| Renta fija global | 0 % | 8 % | Diversifica moneda y emisor |
| Inmobiliario | 8 % | 8 % | Mantiene |
| Sector financiero (exposición efectiva) | 29,6 % | 8 % | Elimina la concentración |
| **Correlación promedio** | **0,58** | **0,31** | |
| **σ estimada** | **18,9 %** | **13,1 %** | **−31 %** |
| **σ con correlaciones de crisis** | **22,7 %** | **17,4 %** | **−23 %** |
| Retorno esperado | 8,4 % | 8,3 % | −0,1 pp |

```text
RESULTADO: 31 % menos de riesgo por 0,1 punto de retorno esperado
```

**Interpreta:** el inversionista tenía 18 instrumentos y **una concentración efectiva del 29,6 % en un
solo sector**, invisible sin mirar dentro de los fondos. El rediseño redujo el riesgo casi un tercio
sin costo en retorno esperado. Ese es el único "almuerzo gratis" que ofrece la inversión, y exige
mirar la exposición efectiva, no el número de líneas del estado de cuenta.

## 🏦 Del cliente al banco

El cliente diversifica su cartera y el banco diversifica su cartera de créditos. La tabla enfrenta las dos lecturas, y el mecanismo es el mismo.

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| Correlación de la cartera | Riesgo de concentración de crédito | 11, clase 2 |
| Exposición efectiva | Límites por grupo económico | 11, clase 1 |
| Correlaciones en crisis | Supuesto crítico de las pruebas de estrés | 11, clase 13 |
| Diversificación sectorial | Política de concentración de cartera | 15, clase 5 |
| Límite por emisor | Norma de créditos relacionados y grandes exposiciones | 12, clase 1 |

## 🧪 Práctica

El laboratorio pide medir la diversificación real de una cartera y recalcularla con correlaciones de crisis. La diferencia entre ambas es lo que hay que saber antes de necesitarlo.

En `labs/lab-05.md`:

1. Calcula el riesgo de una cartera de dos activos para siete correlaciones distintas.
2. Determina la cartera de mínima varianza de un par de activos reales.
3. Calcula la correlación promedio de tu cartera y su exposición efectiva por sector.
4. Recalcula el riesgo con correlaciones observadas en un periodo de crisis.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen carteras que cayeron todas juntas. La causa es diversificación aparente o correlaciones estimadas en periodos tranquilos.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Muchos instrumentos y riesgo alto | Diversificación aparente | Calcula la correlación promedio. |
| Concentración sectorial invisible | No se miró dentro de los fondos | Calcula la exposición efectiva. |
| La cartera cae más de lo esperado en crisis | Correlaciones de periodos normales | Prueba con correlaciones de estrés. |
| Se diversifica solo por emisor | Otras dimensiones ignoradas | Diversifica por sector, país, moneda y clase. |
| Se agregan instrumentos sin evaluar correlación | Beneficio nulo | Verifica que aporte diversificación real. |
| Se invierte todo de una vez | Riesgo de momento de entrada | Considera aportes periódicos. |

## ❓ Preguntas de comprobación

1. ¿Por qué el riesgo de una cartera no es el promedio de los riesgos individuales?
2. Calcula el riesgo de una cartera 50/50 con σ de 20 % y 12 % y correlación 0,3.
3. ¿Cuál es el límite inferior del riesgo de una cartera con σ 30 % y ρ 0,4?
4. ¿Cómo detectas una diversificación aparente?
5. ¿Por qué la diversificación funciona peor en las crisis?

## 📥 Entregable

Guarda en `portfolio/parte-08/clase-09/`:

- el riesgo de una cartera de dos activos en siete correlaciones y su gráfico;
- la cartera de mínima varianza de un par real con su cálculo;
- la correlación promedio y la exposición efectiva de tu cartera;
- el riesgo recalculado con correlaciones de crisis y la comparación con tu límite de política.

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

- Markowitz, H. (1952). "Portfolio Selection". *Journal of Finance*, 7(1). Formulación original de la diversificación.
- Bodie, Z., Kane, A. y Marcus, A. (2023). *Investments* (13.ª ed.). McGraw-Hill. Capítulos 6 y 7: diversificación y frontera eficiente.
- Statman, M. (1987). "How Many Stocks Make a Diversified Portfolio?". *Journal of Financial and Quantitative Analysis*. Evidencia sobre cuántos instrumentos hacen falta para diversificar de verdad.
- Ang, A. y Chen, J. (2002). "Asymmetric Correlations of Equity Portfolios". *Journal of Financial Economics*. Aumento de correlaciones en caídas.
- Ilmanen, A. (2011). *Expected Returns*. Wiley. Diversificación por factores y sus límites.
- Verificación local: calcula las correlaciones con series de índices y precios publicados por la bolsa de tu país y por proveedores de índices globales.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 08 · Riesgo y rentabilidad](08-riesgo-y-rentabilidad.md) | [Parte 08](../README.md) · [Programa](../../../SYLLABUS.md) | [10 · Construcción de portafolios →](10-construccion-de-portafolios.md) |
<!-- gen:footer:end -->
