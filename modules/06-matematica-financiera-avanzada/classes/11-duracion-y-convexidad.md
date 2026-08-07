<!-- meta
part: 7
class: 11
title: "Duración y convexidad"
level: avanzado
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 11 · Duración y convexidad

> [← 10 · Payback y rentabilidad](10-payback-y-rentabilidad.md) · [Índice de la parte](../README.md) · [12 · Sensibilidad →](12-sensibilidad.md)

**Parte 07 — Matemática financiera avanzada** · **Nivel:** Avanzado — perfil analista · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Medir cuánto cambia el valor de un instrumento o de una cartera ante un movimiento de tasas. La
duración es la herramienta central de la gestión de riesgo de tasa —del libro de tesorería y del libro
de banca— y su aplicación errónea ha estado detrás de episodios de estrés bancario documentados.

Las clases anteriores valoran flujos a una tasa dada. Esta mide qué pasa cuando la tasa cambia, que es la pregunta central de la gestión de riesgo de tasa. De aquí sale la herramienta que un banco usa para medir la exposición de todo su balance, y que reaparece en la Parte 11.

## 📚 Objetivos

Al finalizar podrás:

1. **Calcular** duración de Macaulay, duración modificada y duración en dinero.
2. **Estimar** el cambio de valor ante un movimiento de tasas.
3. **Calcular** convexidad y corregir la estimación de primer orden.
4. **Aplicar** la duración a una cartera y al balance completo de un banco.
5. **Diseñar** una cobertura por inmunización.

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

Los tres primeros términos son medidas de sensibilidad de creciente concreción; los tres siguientes, la corrección de segundo orden y sus aplicaciones. La **brecha de duración** es la aplicación bancaria: la diferencia entre la duración del activo y la del pasivo dice cuánto pierde el patrimonio si suben las tasas.

| Concepto | Comprensión verificable |
|---|---|
| `duración de Macaulay (D)` | Plazo promedio ponderado de los flujos, con pesos iguales a su valor presente relativo. Se expresa en años. |
| `duración modificada (D*)` | `D/(1+y)`. Sensibilidad porcentual del precio ante un cambio de 1 punto en la tasa. |
| `duración en dinero (DV01)` | Cambio de valor en unidades monetarias por 1 punto base de movimiento. |
| `convexidad (C)` | Segunda derivada del precio respecto de la tasa. Corrige el error de la aproximación lineal. |
| `inmunización` | Igualar la duración de activos y pasivos para neutralizar el efecto de un cambio de tasas. |
| `brecha de duración` | `D_activos − D_pasivos × (pasivos/activos)`. Mide la exposición del patrimonio. |

## 🧠 Modelo mental

La duración responde una pregunta operativa:

```text
si las tasas suben 1 %, ¿cuánto pierdo?

  ΔP/P ≈ −D* × Δy
```

Un instrumento con duración modificada de 6,4 pierde aproximadamente **6,4 %** de su valor si las
tasas suben 1 punto. Esa aproximación es buena para movimientos pequeños y se degrada con movimientos
grandes: ahí entra la convexidad.

## 📖 Desarrollo

### 1. Duración de Macaulay

La duración es el plazo medio ponderado de los flujos, y esa interpretación es la que la hace intuitiva. El procedimiento siguiente la calcula.

```text
D = Σ [t × VP(FC_t)] / Σ VP(FC_t)
```

Bono con valor nominal 1 000, cupón 6 % anual, 5 años, rendimiento 7 %:

| t | Flujo | VP al 7 % | t × VP |
|---:|---:|---:|---:|
| 1 | 60 | 56,07 | 56,07 |
| 2 | 60 | 52,41 | 104,82 |
| 3 | 60 | 48,98 | 146,94 |
| 4 | 60 | 45,77 | 183,08 |
| 5 | 1 060 | 755,79 | 3 778,95 |
| | | **959,02** | **4 269,86** |

Las dos últimas columnas contienen todo lo necesario: su cociente da la
duración, y un ajuste adicional la convierte en la versión modificada.

```text
D = 4 269,86 / 959,02 = 4,4523 años
D* = 4,4523/1,07 = 4,1610
```

Lectura: **la duración modificada de 4,161 significa que el bono pierde 4,161 % de su valor si el
rendimiento sube 1 punto**.

### 2. Estimación del cambio de valor

Con la duración modificada se estima el cambio de precio ante un movimiento de tasas. La fórmula siguiente lo hace, y es exacta solo para cambios pequeños.

```text
ΔP ≈ −D* × Δy × P
```

Comparar la estimación con el precio recalculado permite medir cuánto se pierde por usar la aproximación lineal en un movimiento pequeño.

```text
Δy = +0,50 % (50 pb)
ΔP ≈ −4,1610 × 0,005 × 959,02 = −19,95
precio estimado = 939,07
precio exacto (recalculado al 7,5 %) = 939,31
error = 0,24 (0,03 %)
```

Con un movimiento mayor:

```text
Δy = +3,00 %
ΔP ≈ −4,1610 × 0,03 × 959,02 = −119,71
precio estimado = 839,31
precio exacto (al 10 %) = 848,37
error = 9,06 (1,07 %)  ← la aproximación lineal subestima el precio
```

**La duración siempre subestima el precio ante alzas y lo subestima también ante bajas** (es decir,
subestima la ganancia). Esa asimetría es lo que corrige la convexidad.

### 3. Convexidad

La relación entre precio y tasa es curva, y la duración la aproxima con una recta. La convexidad corrige esa aproximación, y el esquema muestra cuánto importa.

```text
C = Σ [t(t+1) × VP(FC_t)] / [P × (1+y)²]

ΔP/P ≈ −D* × Δy + ½ × C × (Δy)²
```

Para el bono del ejemplo:

```text
Σ t(t+1) × VP = 1×2×56,07 + 2×3×52,41 + 3×4×48,98 + 4×5×45,77 + 5×6×755,79
              = 112,14 + 314,46 + 587,76 + 915,40 + 22 673,70 = 24 603,46

C = 24 603,46 / (959,02 × 1,07²) = 24 603,46/1 097,88 = 22,4098
```

Corrigiendo la estimación con Δy = +3 %:

```text
ΔP/P ≈ −4,1610 × 0,03 + 0,5 × 22,4098 × 0,0009
     = −0,124830 + 0,010084 = −0,114746
ΔP = −0,114746 × 959,02 = −110,04
precio estimado = 848,98
precio exacto = 848,37
error = 0,61 (0,07 %)  ← quince veces mejor que sin convexidad
```

### 4. Duración de una cartera y del balance

La duración de un conjunto es el promedio ponderado de las duraciones, y eso permite llevarla del instrumento al balance completo.

```text
duración de una cartera = Σ (peso_i × duración_i)
```

El promedio ponderado se calcula instrumento a instrumento, y la última columna es la que suma.

```text
Instrumento        Valor      Peso     D*      Peso × D*
bono soberano 10a  40 000     0,40    7,82      3,128
bono corporativo 5a 25 000    0,25    4,16      1,040
depósito 90 días   20 000     0,20    0,24      0,048
crédito 3 años     15 000     0,15    2,68      0,402
TOTAL             100 000     1,00              4,618
```

Con la duración de la cartera ya calculada, la pérdida ante un movimiento dado de la curva se obtiene con una sola multiplicación.

```text
D* de la cartera = 4,618
ante un alza de 100 pb: pérdida ≈ 4 618
```

Para el balance completo de un banco se usa la **brecha de duración**:

```text
brecha = D*_activos − D*_pasivos × (pasivos/activos)
```

Aplicada a un balance completo, la brecha traduce el riesgo de tasa a lo único que preocupa al accionista: cuánto patrimonio se pierde.

```text
D*_activos = 3,8 · D*_pasivos = 1,4 · activos 100 000 · pasivos 92 000

brecha = 3,8 − 1,4 × 0,92 = 3,8 − 1,288 = 2,512

Δ valor del patrimonio ante +100 pb ≈ −2,512 % × 100 000 = −2 512
sobre un patrimonio de 8 000 → −31,4 % del patrimonio
```

**Una brecha de duración de 2,5 con un patrimonio del 8 % del activo significa que 100 puntos base de
alza borran casi un tercio del patrimonio económico.** Ese es exactamente el cálculo que faltó en
episodios recientes de estrés bancario.

### 5. Inmunización

Igualar la duración del activo y la del pasivo protege el patrimonio ante cambios de tasa. El procedimiento siguiente lo plantea con sus límites.

```text
objetivo: hacer que el valor del patrimonio sea insensible a cambios de tasas
condición: D*_activos × activos = D*_pasivos × pasivos
```

Del ejemplo:

```text
actual:   3,8 × 100 000 = 380 000  vs.  1,4 × 92 000 = 128 800
para inmunizar, se requiere:
  D*_activos objetivo = 128 800/100 000 = 1,288
  o bien D*_pasivos objetivo = 380 000/92 000 = 4,130
```

Alternativas para cerrar la brecha:

| Acción | Efecto sobre la brecha |
|---|---|
| Vender bonos largos y comprar cortos | Reduce `D*_activos` |
| Emitir deuda de largo plazo | Aumenta `D*_pasivos` |
| Contratar swaps de tasa (pagar fija, recibir variable) | Reduce la duración neta |
| Aumentar colocaciones a tasa variable | Reduce `D*_activos` |
| Captar depósitos a plazo más largo | Aumenta `D*_pasivos` |

Limitaciones de la inmunización que hay que conocer:

```text
· solo protege ante movimientos PARALELOS de la curva
· la duración cambia con el tiempo y con las tasas → requiere rebalanceo
· ignora el riesgo de crédito y el de prepago
· los depósitos a la vista no tienen vencimiento contractual: su duración se estima
```

El último punto es crítico en banca: la duración de un depósito a la vista **no es cero**. Aunque el
cliente pueda retirarlo hoy, en la práctica permanece años. Estimar esa duración de comportamiento
—habitualmente entre 1 y 5 años— es una de las decisiones de modelo más relevantes de un banco.

## 🧮 Ejemplo guiado

**Situación.** Un banco mide su exposición al riesgo de tasa antes de un ciclo de alzas esperado.

```text
ACTIVOS                          Valor      D*
  caja y equivalentes            8 000      0,00
  bonos soberanos                24 000     6,40
  cartera hipotecaria tasa fija  46 000     5,10
  cartera consumo tasa fija      28 000     1,60
  cartera comercial tasa variable 34 000    0,25
  TOTAL                         140 000

PASIVOS                          Valor      D*
  depósitos a la vista           38 000     ?  (a estimar)
  depósitos a plazo ≤ 6 meses    52 000     0,35
  depósitos a plazo > 1 año      18 000     1,80
  deuda emitida a 5 años         21 000     4,20
  TOTAL                         129 000

PATRIMONIO                        11 000
```

**Paso 1 — estima la duración de los depósitos a la vista.**

```text
análisis de comportamiento histórico:
  · el 65 % del saldo ha permanecido más de 5 años (saldo "núcleo")
  · el 35 % rota con alta frecuencia
  · beta de traspaso de tasa estimada: 0,25

duración de comportamiento estimada = 0,65 × 4,0 + 0,35 × 0,1 = 2,635
ajustada por beta: 2,635 × (1 − 0,25) = 1,976  ≈ 2,0
```

Este es un supuesto de modelo y debe declararse: **cambiarlo de 2,0 a 3,0 modifica de forma material
toda la conclusión**.

**Paso 2 — duración de los activos.**

```text
D*_A = (8 000×0 + 24 000×6,40 + 46 000×5,10 + 28 000×1,60 + 34 000×0,25)/140 000
     = (0 + 153 600 + 234 600 + 44 800 + 8 500)/140 000
     = 441 500/140 000 = 3,1536
```

**Paso 3 — duración de los pasivos.**

```text
D*_P = (38 000×2,00 + 52 000×0,35 + 18 000×1,80 + 21 000×4,20)/129 000
     = (76 000 + 18 200 + 32 400 + 88 200)/129 000
     = 214 800/129 000 = 1,6651
```

**Paso 4 — brecha de duración.**

```text
brecha = 3,1536 − 1,6651 × (129 000/140 000)
       = 3,1536 − 1,6651 × 0,92143
       = 3,1536 − 1,5343 = 1,6193
```

**Paso 5 — efecto de un alza de 200 puntos base.**

```text
Δ valor económico del patrimonio ≈ −1,6193 % × 2 × 140 000 
                                  = −0,032386 × 140 000 = −4 534

sobre un patrimonio de 11 000 → −41,2 %
```

Incorporando convexidad (estimada en 28 para el activo y 9 para el pasivo):

```text
corrección ≈ ½ × (28 − 9 × 0,92143) × (0,02)² × 140 000
           = ½ × 19,71 × 0,0004 × 140 000 = +552
Δ patrimonio ≈ −3 982 → −36,2 % del patrimonio
```

**Paso 6 — decisiones de cobertura.**

```text
objetivo: reducir la brecha de 1,62 a menos de 0,80

opción 1  swap de tasa: pagar fija, recibir variable, nocional 45 000, plazo 5 años
          efecto en la duración del activo: −45 000 × 4,3/140 000 = −1,382
          brecha resultante: 0,237  ← cumple con holgura
          costo: diferencial del swap

opción 2  vender 20 000 de bonos soberanos y comprar instrumentos de 1 año
          Δ D*_A = (20 000 × (0,95 − 6,40))/140 000 = −0,779
          brecha resultante: 0,840  ← cumple justo
          costo: pérdida por venta si las tasas ya subieron

opción 3  emitir 15 000 de deuda a 7 años (D* = 5,8)
          Δ D*_P = (15 000 × 5,8)/144 000 = +0,604... recalculando la mezcla
          brecha resultante ≈ 1,05  ← insuficiente por sí sola

RECOMENDACIÓN: opción 1, complementada con originación de hipotecarios a tasa variable

y una advertencia obligatoria:
  la duración de 2,0 asignada a los depósitos a la vista es el supuesto crítico.
  Con D* = 1,0, la brecha sería 2,09 y la pérdida estimada −49 % del patrimonio.
  Con D* = 3,0, la brecha sería 1,15 y la pérdida −29 %.
  Este supuesto debe validarse con el comportamiento observado, y revalidarse
  cada vez que cambien las condiciones de tasa.
```

**Interpreta:** la medición de la brecha revela una exposición que **borraría más de un tercio del
patrimonio económico ante 200 puntos base**, sin que el estado de resultados lo muestre en el momento.
Y el supuesto que más mueve el resultado —la duración de los depósitos a la vista— es el menos
observable y el que más juicio requiere. Reconocerlo explícitamente es parte del trabajo.

## 🏦 Del cliente al banco

El cliente ve un bono y el banco mide la sensibilidad de su balance. La tabla enfrenta las dos lecturas.

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| Duración modificada | Medición del riesgo de tasa | 11, clase 5 |
| Brecha de duración | Exposición del patrimonio económico | 11, clase 5 |
| Duración de depósitos a la vista | Supuesto de modelo crítico | 11, clase 5 |
| Inmunización | Estrategia de cobertura | 11, clase 5 |
| Convexidad | Corrección ante movimientos grandes | 8, clase 4 |

## 🧪 Práctica

El laboratorio pide calcular la duración de una cartera y estimar la pérdida ante un alza de cien puntos base. La estimación se compara con el cálculo exacto, y la diferencia es la convexidad.

En `labs/lab-06.md`:

1. Calcula duración de Macaulay, modificada y convexidad de cinco bonos.
2. Compara la estimación por duración con el precio exacto en cinco magnitudes de movimiento.
3. Calcula la duración de una cartera y la brecha de duración de un balance.
4. Diseña una cobertura para reducir la brecha a un objetivo definido.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen estimaciones de pérdida que se quedan cortas. La causa es haber usado solo duración ante movimientos grandes.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se asigna duración cero a los depósitos a la vista | Supuesto implícito incorrecto | Estima la duración de comportamiento. |
| La estimación falla ante movimientos grandes | Solo se usó duración | Incorpora convexidad. |
| Se cree que inmunizar elimina todo el riesgo | Solo cubre movimientos paralelos | Complementa con análisis de cambios de forma de la curva. |
| Se mide solo el efecto en el margen | Valor económico omitido | Mide ambos (Parte 6, clase 10). |
| La duración no se recalcula | Cambia con el tiempo y las tasas | Rebalancea periódicamente. |
| Se suma duración en años entre instrumentos | Ponderación omitida | Pondera por valor de mercado. |

## ❓ Preguntas de comprobación

1. ¿Qué significa una duración modificada de 5,2?
2. ¿Por qué la duración subestima el precio ante alzas y ante bajas?
3. Calcula la brecha de duración de un balance con `D*_A = 4,1`, `D*_P = 1,9` y pasivos del 90 % del activo.
4. ¿Por qué la duración de los depósitos a la vista no es cero?
5. ¿Qué riesgos NO cubre una estrategia de inmunización?

## 📥 Entregable

Guarda en `portfolio/parte-07/clase-11/`:

- duración y convexidad de cinco bonos con su verificación;
- la comparación estimación vs. precio exacto en cinco magnitudes de movimiento;
- la brecha de duración de un balance con el supuesto de depósitos declarado;
- el diseño de cobertura con su efecto cuantificado y el análisis de sensibilidad al supuesto crítico.

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

- Fabozzi, F. (2021). *Bond Markets, Analysis, and Strategies* (10.ª ed.). MIT Press. Capítulos 4 y 5: duración, convexidad y su aplicación.
- Hull, J. (2021). *Options, Futures, and Other Derivatives* (11.ª ed.). Pearson. Capítulo 4: duración y cobertura de riesgo de tasa.
- Saunders, A. y Cornett, M. (2021). *Financial Institutions Management* (10.ª ed.). McGraw-Hill. Capítulos 8 y 9: modelo de duración aplicado al balance bancario.
- Basel Committee on Banking Supervision (2016). *Interest rate risk in the banking book* (IRRBB). BIS. Marco estándar de medición y supuestos de comportamiento. <https://www.bis.org/bcbs/publ/d368.htm>
- Macaulay, F. (1938). *Some Theoretical Problems Suggested by the Movements of Interest Rates*. NBER. Formulación original de la duración.
- Verificación local: revisa qué exige tu supervisor sobre medición del riesgo de tasa del libro de banca y sobre la modelación de depósitos sin vencimiento.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 10 · Payback y rentabilidad](10-payback-y-rentabilidad.md) | [Parte 07](../README.md) · [Programa](../../../SYLLABUS.md) | [12 · Sensibilidad →](12-sensibilidad.md) |
<!-- gen:footer:end -->
