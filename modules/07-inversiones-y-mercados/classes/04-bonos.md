<!-- meta
part: 8
class: 4
title: "Bonos"
level: intermedio
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 04 · Bonos

> [← 03 · Acciones](03-acciones.md) · [Índice de la parte](../README.md) · [05 · Fondos mutuos →](05-fondos-mutuos.md)

**Parte 08 — Inversiones y mercados** · **Nivel:** Intermedio — requiere las partes anteriores · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Dominar el instrumento que constituye la mayor parte del mercado de capitales mundial y el activo
principal del balance de un banco. Un bono es un préstamo negociable, y entender su mecánica de
precios —por qué sube cuando las tasas bajan y en qué magnitud— es indispensable para gestionar
cualquier cartera o balance.

La acción de la clase anterior es propiedad. El bono es deuda, y por eso su análisis es el de la Parte 7: un bono es una serie de flujos conocidos, y su precio es el valor presente de esa serie. Lo que añade esta clase es la relación inversa entre precio y tasa, que es la base de la gestión de carteras de renta fija.

## 📚 Objetivos

Al finalizar podrás:

1. **Identificar** los elementos de un bono y leer su ficha.
2. **Calcular** el precio de un bono a partir de su rendimiento y viceversa.
3. **Explicar** la relación inversa entre precio y tasa, y su magnitud.
4. **Interpretar** la curva de rendimientos y los diferenciales de crédito.
5. **Evaluar** los riesgos de un bono y su medición.

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

Los tres primeros términos son la estructura del instrumento; los cuatro siguientes, cómo se valora y cómo se mide su riesgo de crédito. El **rendimiento al vencimiento** es la TIR de la clase 9 de la Parte 7 aplicada al bono, y es la cifra que permite compararlos.

| Concepto | Comprensión verificable |
|---|---|
| `valor nominal` | Monto que se paga al vencimiento. Base del cálculo del cupón. |
| `cupón` | Interés periódico, expresado como porcentaje del nominal. |
| `rendimiento al vencimiento (TIR)` | Tasa que iguala el precio con el valor presente de todos los flujos. |
| `precio sobre o bajo la par` | Sobre la par si el cupón supera al rendimiento; bajo la par en el caso inverso. |
| `curva de rendimientos` | Rendimiento por plazo de emisores equivalentes. Su forma tiene contenido informativo. |
| `diferencial de crédito (spread)` | Rendimiento adicional sobre un bono soberano de igual plazo. Compensa el riesgo de crédito. |
| `clasificación de riesgo` | Opinión sobre la capacidad de pago del emisor. No es recomendación de compra. |

## 🧠 Modelo mental

Un bono es **un flujo fijo con precio variable**:

```text
el flujo NO cambia: cupones y nominal están en el contrato
lo que cambia es el PRECIO, para que el rendimiento se ajuste al mercado

tasas de mercado SUBEN → el precio del bono existente BAJA
tasas de mercado BAJAN → el precio SUBE
```

La razón es aritmética: si un bono paga 5 % y el mercado ahora exige 7 %, nadie lo compra a la par;
su precio cae hasta que su rendimiento efectivo sea 7 %.

## 📖 Desarrollo

### 1. Elementos de un bono

Un bono se describe con pocos elementos y todos importan para el precio. La tabla los recoge.

```text
FICHA DE EMISIÓN
  emisor                      Empresa ABC S.A.
  valor nominal               1 000 por título
  cupón                       5,80 % anual, pagadero semestral
  fecha de emisión            2024-03-15
  fecha de vencimiento        2031-03-15
  amortización                bullet (todo el capital al vencimiento)
  moneda                      unidad indexada
  clasificación               AA−
  garantías                   sin garantía específica
  covenants                   deuda neta/EBITDA ≤ 3,5x; cobertura ≥ 2,5x
  opción de rescate           a partir del año 5, al 101 %
```

Cada línea tiene consecuencias:

| Elemento | Consecuencia |
|---|---|
| Amortización bullet | Todo el riesgo de refinanciamiento al vencimiento |
| Moneda indexada | El inversionista queda protegido de la inflación |
| Sin garantía | Ante incumplimiento, concurre con los acreedores comunes |
| Covenants | Protegen al tenedor; su incumplimiento puede acelerar |
| Opción de rescate | El emisor puede pagar antes si las tasas bajan: **perjudica al tenedor** |

La opción de rescate merece atención: **el emisor la ejerce cuando le conviene**, es decir, cuando las
tasas bajaron y el tenedor querría mantener el bono. Esa asimetría se compensa con un cupón mayor.

### 2. Precio y rendimiento

Precio y rendimiento se mueven en direcciones opuestas, y esa relación es la clave de toda la renta fija. El esquema la muestra.

```text
P = Σ (C/(1+y)^t) + VN/(1+y)^n
```

Bono de 1 000, cupón 6 % anual, 5 años, rendimiento de mercado 7 %:

| t | Flujo | Factor (7 %) | VP |
|---:|---:|---:|---:|
| 1 | 60 | 0,934579 | 56,07 |
| 2 | 60 | 0,873439 | 52,41 |
| 3 | 60 | 0,816298 | 48,98 |
| 4 | 60 | 0,762895 | 45,77 |
| 5 | 1 060 | 0,712986 | 755,76 |
| | | **Precio** | **958,99** |

La suma de la última columna es el precio, y su posición respecto del valor
nominal ya anticipa la relación entre cupón y rendimiento.

```text
precio 958,99 < 1 000 → BAJO LA PAR, porque el cupón (6 %) < rendimiento (7 %)
```

Relación general:

```text
cupón > rendimiento  →  precio sobre la par
cupón = rendimiento  →  precio a la par
cupón < rendimiento  →  precio bajo la par
```

### 3. Magnitud de la sensibilidad

Usando la duración modificada (Parte 7, clase 11):

```text
D* del bono ≈ 4,16
Δ precio ≈ −4,16 × Δy × precio
```

| Δ rendimiento | Precio estimado | Precio exacto | Variación |
|---:|---:|---:|---:|
| −200 pb | 1 038,8 | 1 043,8 | +8,8 % |
| −100 pb | 998,9 | 1 000,0 | +4,3 % |
| 0 | 959,0 | 959,0 | — |
| +100 pb | 919,1 | 920,1 | −4,1 % |
| +200 pb | 879,2 | 883,3 | −7,9 % |

**Un bono a 5 años pierde alrededor del 4 % de su valor por cada punto de alza de tasas.** Un bono a
20 años puede perder más del 15 %. Esa diferencia —la duración— es lo que determina el riesgo de una
cartera de renta fija.

### 4. Curva de rendimientos y diferenciales

**Formas de la curva y su lectura:**

| Forma | Descripción | Interpretación habitual |
|---|---|---|
| Normal (ascendente) | Tasas largas > cortas | Expectativa de crecimiento; prima por plazo |
| Plana | Tasas similares en todos los plazos | Transición; incertidumbre |
| Invertida | Tasas cortas > largas | Expectativa de bajas de tasa; históricamente asociada a recesión |
| Con joroba | Máximo en plazos intermedios | Expectativas mixtas |

**Diferenciales de crédito:**

```text
rendimiento del bono corporativo = rendimiento soberano de igual plazo + spread

spread compensa:
  · pérdida esperada por incumplimiento
  · prima por riesgo (incertidumbre sobre esa pérdida)
  · prima de liquidez
```

| Clasificación | Spread típico sobre soberano | Probabilidad de incumplimiento acumulada a 5 años (referencial) |
|---|---:|---:|
| AAA | 30–60 pb | < 0,3 % |
| AA | 50–90 pb | 0,3–0,7 % |
| A | 80–150 pb | 0,7–1,5 % |
| BBB | 130–250 pb | 1,5–4,0 % |
| BB | 250–450 pb | 6–12 % |
| B | 400–800 pb | 15–25 % |
| CCC | > 800 pb | > 35 % |

Los rangos son referenciales y **se amplían fuertemente en periodos de estrés**: durante crisis, los
spreads pueden multiplicarse por tres o cuatro sin que cambie la calidad del emisor.

### 5. Riesgos de un bono

Un bono tiene varios riesgos además del de impago, y algunos son mayores. La tabla los recoge.

| Riesgo | Descripción | Medición |
|---|---|---|
| De tasa | El precio cae si las tasas suben | Duración y convexidad |
| De crédito | El emisor no paga | Clasificación, spread, análisis fundamental |
| De liquidez | No se puede vender al precio de referencia | Volumen, diferencial compra-venta |
| De reinversión | Los cupones se reinvierten a tasas menores | Duración, bonos cupón cero |
| De rescate | El emisor paga antes cuando conviene a él | Rendimiento al rescate (yield to call) |
| De inflación | El rendimiento real cae | Bonos indexados |
| Cambiario | Si el bono está en otra moneda | Cobertura |

Nota importante sobre el riesgo de tasa: **si se mantiene el bono al vencimiento y el emisor paga, la
caída de precio no se materializa**. El riesgo de tasa afecta a quien debe vender antes, o a quien
valora su cartera a mercado, como un banco.

## 🧮 Ejemplo guiado

El ejemplo valora un bono y calcula su rendimiento al vencimiento. Conviene comprobar el signo de la relación precio-tasa: si el precio sube cuando la tasa sube, hay un error.

**Situación.** Un inversionista compara tres bonos para un objetivo a 6 años.

```text
              Bono A            Bono B            Bono C
emisor        soberano          corporativo AA    corporativo BBB
plazo         6 años            6 años            6 años
cupón         4,20 %            5,40 %            7,10 %
precio        100,0             99,2              97,8
moneda        indexada          indexada          indexada
rescate       no                no                a partir del año 4, al 101
liquidez      muy alta          media             baja
```

**Paso 1 — calcula el rendimiento al vencimiento de cada uno.**

```text
A  precio a la par → rendimiento = cupón = 4,20 %
B  precio 99,2 → rendimiento ≈ 5,56 %
C  precio 97,8 → rendimiento ≈ 7,54 %
```

**Paso 2 — descompón los diferenciales.**

```text
spread B sobre soberano = 5,56 − 4,20 = 1,36 % = 136 pb
spread C sobre soberano = 7,54 − 4,20 = 3,34 % = 334 pb
```

**Paso 3 — evalúa si el spread compensa la pérdida esperada.**

```text
probabilidad de incumplimiento acumulada a 6 años (tablas históricas):
  AA:  ≈ 0,8 %
  BBB: ≈ 4,6 %

severidad esperada (LGD) para deuda sin garantía: ≈ 60 %

pérdida esperada anualizada:
  B: 0,008 × 0,60 / 6 ≈ 0,08 % anual = 8 pb
  C: 0,046 × 0,60 / 6 ≈ 0,46 % anual = 46 pb

spread menos pérdida esperada:
  B: 136 − 8 = 128 pb de compensación por riesgo y liquidez
  C: 334 − 46 = 288 pb
```

**Ambos spreads superan ampliamente la pérdida esperada**, lo que es normal: el resto compensa la
incertidumbre y la iliquidez.

**Paso 4 — evalúa la opción de rescate de C.**

```text
si las tasas bajan y en el año 4 el emisor rescata al 101:
  rendimiento al rescate (yield to call) ≈ 7,92 %
  
si las tasas suben, el emisor NO rescata y el tenedor queda con un bono
de mayor duración justo cuando las tasas subieron

el rendimiento relevante para C es el MENOR entre el rendimiento al vencimiento
y el rendimiento al rescate: 7,54 %
```

**Paso 5 — calcula la sensibilidad de cada uno.**

```text
D* aproximada:
  A: 5,25  (cupón bajo, mayor duración)
  B: 5,08
  C: 4,86  (cupón alto, menor duración)

ante un alza de 150 pb:
  A: −7,88 %
  B: −7,62 %
  C: −7,29 %
```

**Paso 6 — decisión según el objetivo.**

```text
el objetivo es a 6 años y el inversionista NO necesitará vender antes

en ese caso:
  · el riesgo de tasa no se materializa si mantiene al vencimiento
  · el riesgo relevante es el de CRÉDITO
  · la liquidez importa poco

ASIGNACIÓN PROPUESTA
  A  40 %  ancla de seguridad
  B  40 %  spread razonable con riesgo de crédito bajo
  C  20 %  spread atractivo, limitado por su riesgo y por la opción de rescate

rendimiento esperado de la cartera = 0,40×4,20 + 0,40×5,56 + 0,20×7,54 = 5,41 %
pérdida esperada por crédito = 0,40×0 + 0,40×0,08 + 0,20×0,46 = 0,12 %
rendimiento neto esperado ≈ 5,29 % real

CONDICIÓN: si el inversionista pudiera necesitar el dinero antes de 6 años,
la asignación cambia: C se reduce a 0 % por iliquidez y A sube a 60 %
```

**Interpreta:** la decisión dependió por completo de una pregunta que no está en ninguna ficha de
bono: **¿puedes mantener hasta el vencimiento?** Si la respuesta es sí, el riesgo de tasa es
irrelevante y manda el crédito. Si es no, la liquidez y la duración pasan al primer plano. Esa
pregunta viene de la clase 1, no del análisis del instrumento.

## 🏦 Del cliente al banco

El cliente compra un bono y el banco lo valora a mercado en su balance. La tabla enfrenta las dos lecturas, y explica por qué un alza de tasas produce pérdidas contables sin que nadie haya vendido nada.

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| Duración de la cartera de bonos | Riesgo de tasa del banco | 11, clase 5 |
| Spread de crédito | Pricing de emisiones y de créditos | 15, clase 7 |
| Curva de rendimientos | Insumo de valoración y de expectativas | 6, clase 10 |
| Clasificación de riesgo | Ponderación de capital regulatorio | 12, clase 1 |
| Valoración a mercado | Efecto en resultado o en patrimonio | 5, clase 3 |

## 🧪 Práctica

El laboratorio pide valorar bonos a distintas tasas y medir el efecto sobre el precio. La sensibilidad crece con el plazo, y comprobarlo prepara la duración de la Parte 7.

En `labs/lab-02.md`, sección de renta fija:

1. Calcula el precio de cinco bonos a partir de su rendimiento y verifica en sentido inverso.
2. Construye la relación precio-rendimiento de un bono en siete puntos y grafícala.
3. Descompón el spread de tres bonos corporativos reales y compáralo con su pérdida esperada.
4. Compara rendimiento al vencimiento y al rescate de un bono con opción.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen pérdidas inesperadas en renta fija. La causa habitual es haber supuesto que un bono no puede perder valor si no hay impago.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se cree que un bono no puede perder valor | Relación precio-tasa desconocida | El precio cae cuando las tasas suben. |
| Se compra por el cupón más alto | Rendimiento y riesgo ignorados | Compara rendimiento al vencimiento y spread. |
| Se ignora la opción de rescate | Asimetría no considerada | Usa el menor entre rendimiento al vencimiento y al rescate. |
| Se supone que una clasificación alta elimina el riesgo | Función mal entendida | Es una opinión sobre capacidad de pago, no una garantía. |
| Se compra un bono ilíquido sin poder mantenerlo | Horizonte no considerado | Verifica si puedes mantener al vencimiento. |
| Se compara cupón entre bonos de distinto precio | Base incorrecta | Compara rendimiento, no cupón. |

## ❓ Preguntas de comprobación

1. ¿Por qué el precio de un bono baja cuando suben las tasas?
2. Un bono con cupón 5 % cotiza a 96. ¿Su rendimiento es mayor o menor que 5 %?
3. ¿Qué compensa el spread de crédito, además de la pérdida esperada?
4. ¿Por qué una opción de rescate perjudica al tenedor?
5. ¿Cuándo el riesgo de tasa de un bono no se materializa?

## 📥 Entregable

Guarda en `portfolio/parte-08/clase-04/`:

- el precio de cinco bonos calculado y verificado en ambos sentidos;
- la curva precio-rendimiento de un bono en siete puntos;
- la descomposición del spread de tres bonos reales contra su pérdida esperada;
- la comparación de rendimiento al vencimiento y al rescate con su decisión.

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

- Fabozzi, F. (2021). *Bond Markets, Analysis, and Strategies* (10.ª ed.). MIT Press. Capítulos 2 a 6: valoración, rendimiento, curva y spreads.
- Bodie, Z., Kane, A. y Marcus, A. (2023). *Investments* (13.ª ed.). McGraw-Hill. Capítulos 14 a 16: precios de bonos y estructura temporal.
- Hull, J. (2021). *Options, Futures, and Other Derivatives* (11.ª ed.). Pearson. Capítulo 4: tasas cero, forward y valoración de bonos.
- Moody's / S&P. *Annual Default Study* (informes anuales). Probabilidades de incumplimiento históricas por clasificación.
- Bank for International Settlements. *BIS Quarterly Review*. Evolución de spreads de crédito por segmento. <https://www.bis.org/publ/quarterly.htm>
- Verificación local: usa las emisiones inscritas en el registro del supervisor de valores de tu país y la curva soberana publicada por el banco central.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 03 · Acciones](03-acciones.md) | [Parte 08](../README.md) · [Programa](../../../SYLLABUS.md) | [05 · Fondos mutuos →](05-fondos-mutuos.md) |
<!-- gen:footer:end -->
