---
part: 6
class: 10
title: "Política monetaria"
level: intermedio
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 10 · Política monetaria

> [← 09 · Política fiscal](09-politica-fiscal.md) · [Índice de la parte](../README.md) · [11 · Bancos centrales →](11-bancos-centrales.md)

**Parte 06 — Economía y sistema financiero** · **Nivel:** Intermedio — requiere las partes anteriores · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Entender el instrumento que más directamente afecta el negocio bancario: la tasa de política
monetaria. Un cambio de esa tasa modifica el costo de fondos, el margen, la demanda de crédito, el
valor de la cartera de bonos y la morosidad futura. Esta clase explica cómo se decide, cómo se
transmite y con qué rezagos.

La política fiscal de la clase anterior actúa despacio y por decisión política. Esta actúa más rápido y por decisión técnica, y es la que fija el precio del dinero del que dependen todas las tasas del sistema. Para un banco, es la variable exógena más importante que existe.

## 📚 Objetivos

Al finalizar podrás:

1. **Explicar** los objetivos y los instrumentos de la política monetaria.
2. **Interpretar** una decisión de tasa a partir de sus fundamentos.
3. **Describir** los canales de transmisión y sus rezagos.
4. **Aplicar** una regla de tasa como referencia de razonabilidad.
5. **Anticipar** el efecto de un cambio de tasa sobre el balance de un banco.

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

Los cuatro primeros términos son el instrumento y su referencia; los tres siguientes, cómo llega a la economía y cómo se comunica. La **tasa neutral** es la referencia que da sentido a todo: sin ella no se puede decir si una tasa concreta es expansiva o contractiva.

| Concepto | Comprensión verificable |
|---|---|
| `tasa de política monetaria` | Tasa de referencia que fija el banco central para las operaciones interbancarias overnight. |
| `meta de inflación` | Objetivo numérico, habitualmente en un horizonte de 12 a 24 meses. |
| `tasa neutral` | Nivel de tasa real que no estimula ni contrae la actividad. No es observable: se estima. |
| `postura` | Expansiva si la tasa real está bajo la neutral; contractiva si está sobre ella. |
| `canal de transmisión` | Mecanismo por el que la tasa afecta la economía: tasas de mercado, crédito, activos, cambiario y expectativas. |
| `forward guidance` | Comunicación sobre la trayectoria futura esperada de la tasa. Es un instrumento en sí mismo. |
| `regla de Taylor` | Referencia que relaciona la tasa con la desviación de la inflación y la brecha del producto. |

## 🧠 Modelo mental

Un banco central mueve **una sola tasa muy corta** y con eso afecta toda la economía:

```text
tasa overnight → tasas interbancarias → tasas de depósitos y créditos
                                      → precios de bonos y acciones
                                      → tipo de cambio
                                      → decisiones de consumo e inversión
                                      → demanda agregada → inflación
```

Cada eslabón agrega rezago. Por eso la política monetaria **actúa sobre la inflación de dentro de uno
o dos años**, no sobre la de este mes, y por eso se decide mirando proyecciones y no datos observados.

## 📖 Desarrollo

### 1. Objetivos e instrumentos

El banco central tiene objetivos declarados y un conjunto acotado de instrumentos. La tabla los relaciona.

| Objetivo | Alcance |
|---|---|
| Estabilidad de precios | Objetivo primario en la mayoría de los marcos |
| Estabilidad financiera | Objetivo complementario o compartido |
| Empleo | Objetivo explícito en algunos marcos (mandato dual) |
| Estabilidad del sistema de pagos | Función operativa |

| Instrumento | Cómo funciona |
|---|---|
| Tasa de política | Referencia para el mercado interbancario |
| Operaciones de mercado abierto | Compra y venta de instrumentos para gestionar la liquidez |
| Encaje o reservas obligatorias | Fracción de los depósitos que el banco debe mantener |
| Facilidades permanentes | Ventanilla de préstamo y de depósito, que acotan la tasa de mercado |
| Compras de activos | Compra de bonos de plazos largos para influir en tasas largas |
| Comunicación (*forward guidance*) | Influye en las expectativas de tasa futura |

### 2. Cómo se decide

La decisión sigue un procedimiento con información, deliberación y comunicación. Los pasos siguientes lo recorren.

```text
1. proyección de inflación a 12–24 meses, condicionada a supuestos
2. evaluación de la brecha del producto y del mercado laboral
3. evaluación de las expectativas de inflación (encuestas y mercado)
4. balance de riesgos: qué escenario alternativo preocupa más
5. decisión de tasa y comunicación de la trayectoria esperada
```

**Regla de Taylor** como referencia de razonabilidad, no como fórmula de decisión:

```text
i = r* + π + 0,5 (π − π*) + 0,5 × brecha del producto

r*  tasa real neutral
π   inflación observada
π*  meta de inflación
```

```text
ejemplo: r* = 1,0 % · π = 6,4 % · π* = 3,0 % · brecha = +1,1 %

i = 1,0 + 6,4 + 0,5 × (6,4 − 3,0) + 0,5 × 1,1
  = 1,0 + 6,4 + 1,7 + 0,55 = 9,65 %
```

Si la tasa de política está en 7,5 %, la regla sugiere que la postura es **más expansiva de lo que las
condiciones justificarían**. Eso no significa que la decisión sea incorrecta —la regla ignora rezagos,
shocks transitorios y riesgos de estabilidad financiera— pero sí que la desviación debe explicarse.

### 3. Canales de transmisión y rezagos

La tasa de política llega a la economía por varios canales con velocidades distintas, y el rezago total es largo. La tabla los recoge.

| Canal | Mecanismo | Rezago |
|---|---|---|
| **Tasas de mercado** | La tasa corta se traslada a depósitos y créditos | 1–2 trimestres |
| **Crédito** | Cambia la oferta de crédito bancaria vía costo de fondos y capital | 2–4 trimestres |
| **Precios de activos** | Suben las tasas → caen bonos y acciones → menor riqueza → menor consumo | 1–3 trimestres |
| **Tipo de cambio** | Mayor tasa local → entrada de capitales → aprecia la moneda → menor inflación de transables | 1–2 trimestres |
| **Expectativas** | La comunicación cambia lo que los agentes esperan | Inmediato a 2 trimestres |
| **Efecto total sobre la inflación** | | **4–8 trimestres** |

La transmisión es **asimétrica e incompleta**:

```text
alza de tasa → las tasas de colocación suben rápido y completo
baja de tasa → las tasas de colocación bajan lento y parcialmente
```

Esta asimetría está documentada en múltiples sistemas bancarios y se explica por la estructura
competitiva (Parte 6, clase 4) y por el costo de fondos con vencimientos escalonados.

### 4. Efecto sobre el balance de un banco

Un alza de 100 puntos base afecta simultáneamente:

| Partida | Efecto | Signo |
|---|---|---|
| Costo de fondos | Sube con rezago de 1–2 trimestres | Negativo |
| Tasa de colocaciones nuevas | Sube casi de inmediato | Positivo |
| Cartera a tasa variable | Se repactiza al alza | Positivo |
| Cartera a tasa fija | No cambia el ingreso; cae su valor económico | Negativo |
| Cartera de bonos | Cae su valor de mercado | Negativo |
| Demanda de crédito | Se contrae con rezago | Negativo |
| Morosidad | Sube con rezago de 3–6 trimestres | Negativo |
| Depósitos a la vista | Su valor como fondeo barato aumenta | Positivo |

El efecto neto sobre el margen depende de la **estructura de repreciación** del balance: cuánto del
activo y del pasivo se repacta en cada tramo de plazo. Ese análisis es la gestión de riesgo de tasa
del libro de banca de la Parte 11, clase 5.

### 5. Límites de la política monetaria

La política monetaria no puede con todo, y conocer sus límites evita esperar de ella lo que no puede dar. La lista los recoge.

```text
· no puede corregir problemas de oferta (sequía, shock de energía) sin costo en actividad
· no puede reducir el desempleo estructural
· su efecto tiene rezagos largos y variables
· cerca del límite inferior de tasas, su capacidad de estimular se reduce
· puede generar efectos no deseados: búsqueda de rendimiento, burbujas de activos
```

El penúltimo punto explica el uso de instrumentos no convencionales —compras de activos, guías de
trayectoria— y el último explica por qué la estabilidad financiera se incorporó como consideración
explícita después de 2008.

## 🧮 Ejemplo guiado

**Situación.** El banco central sube la tasa de política de 5,00 % a 8,25 % en cuatro reuniones a lo
largo de nueve meses. Un banco comercial evalúa el impacto.

```text
BALANCE DEL BANCO (miles de millones)
ACTIVOS
  colocaciones a tasa variable (repactan ≤ 3 meses)    18 000
  colocaciones a tasa fija corto plazo (≤ 12 meses)    12 000
  colocaciones a tasa fija largo plazo (> 12 meses)    26 000
  cartera de bonos (duración 4,2 años)                  9 000
  TOTAL                                                65 000

PASIVOS
  depósitos a la vista                                 21 000
  depósitos a plazo (≤ 6 meses)                        24 000
  deuda emitida (tasa fija, > 2 años)                  12 000
  patrimonio                                            8 000
  TOTAL                                                65 000
```

**Paso 1 — brecha de repreciación a 12 meses.**

```text
activos que repactan en ≤ 12 meses:  18 000 + 12 000 = 30 000
pasivos que repactan en ≤ 12 meses:  24 000 (depósitos a plazo)
                                     + parte de los depósitos a la vista (beta 30 %) = 6 300
                                     total 30 300

BRECHA = 30 000 − 30 300 = −300  → prácticamente calzado
```

**Paso 2 — efecto sobre el margen financiero en 12 meses.**

```text
Δmargen ≈ brecha × Δtasa = −300 × 0,0325 = −9,75 miles de millones
```

Efecto pequeño y levemente negativo. El balance está bien calzado en el tramo de un año.

**Paso 3 — efecto sobre el valor económico de la cartera de bonos.**

```text
Δvalor ≈ −duración × Δtasa × valor
       = −4,2 × 0,0325 × 9 000 = −1 228,5 miles de millones
```

**Este efecto es 126 veces mayor que el del margen.** Si esos bonos se miden a valor razonable con
efecto en resultados o en patrimonio, el impacto es inmediato y material.

**Paso 4 — efecto sobre el valor económico de la cartera de colocaciones a tasa fija larga.**

```text
duración estimada de las colocaciones fijas largas: 2,8 años
Δvalor ≈ −2,8 × 0,0325 × 26 000 = −2 366 miles de millones
```

Este efecto no aparece en el resultado contable si las colocaciones están a costo amortizado, y **sí
afecta el valor económico del patrimonio**, que es lo que la Parte 11, clase 5, mide.

**Paso 5 — efectos con rezago.**

```text
demanda de crédito: −8 a −14 % en 3–4 trimestres
morosidad de consumo: +0,6 a +1,1 puntos en 4–6 trimestres
  sobre una cartera de consumo de 20 000 → provisión adicional 84 a 154 miles de millones
depósitos a la vista: migración hacia depósitos a plazo (más caros)
  si migra el 15 % de 21 000 al 6,5 % → costo adicional 205 miles de millones al año
```

**Paso 6 — cuadro completo y decisiones.**

| Efecto | Magnitud (miles de millones) | Horizonte |
|---|---:|---|
| Margen financiero por brecha | −10 | 12 meses |
| Valor de la cartera de bonos | −1 229 | Inmediato |
| Valor económico de colocaciones fijas | −2 366 | Inmediato (no contable) |
| Migración de depósitos | −205/año | 2–4 trimestres |
| Provisiones adicionales | −119 (punto medio) | 4–6 trimestres |
| Menor volumen por caída de demanda | Variable | 3–4 trimestres |

```text
DECISIONES
1. reducir la duración de la cartera de bonos: cada año de duración cuesta 292 mil millones
   por cada 100 pb de alza
2. aumentar la proporción de colocaciones a tasa variable en la originación nueva
3. gestionar la migración de depósitos a la vista con productos de retención
4. anticipar provisiones: no esperar a ver la morosidad
5. revisar el pricing: la tasa de las colocaciones nuevas debe recoger el mayor costo de fondos
   y la mayor pérdida esperada
```

**Interpreta:** el efecto sobre el **margen** —lo que la mayoría mira— fue insignificante gracias al
calce. El efecto material estuvo en el **valor económico** de las carteras a tasa fija, que no aparece
en el estado de resultados. Ese es exactamente el riesgo que quebró bancos en episodios recientes: un
balance con margen sano y un valor económico severamente deteriorado.

## 🏦 Del cliente al banco

El cliente ve cambiar su tasa y el banco reprecia activos y pasivos a velocidades distintas. La tabla enfrenta las dos lecturas, y ese desfase es el riesgo de tasa de la Parte 11.

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| Tasa de política | Base del costo de fondos y del pricing | 15, clase 7 |
| Brecha de repreciación | Gestión de riesgo de tasa | 11, clase 5 |
| Duración | Sensibilidad del valor económico | 7, clase 11 |
| Beta de depósitos | Cuánto del alza se traslada al depositante | 10, clase 2 |
| Transmisión asimétrica | Comportamiento del margen en ciclos de tasa | 15, clase 3 |

## 🧪 Práctica

El laboratorio pide aplicar una regla de política a datos de inflación y brecha, y comparar con la decisión observada. Las diferencias son las que se discuten en un comité real.

En `labs/lab-05.md`, sección de política monetaria:

1. Lee tres comunicados de política monetaria de tu banco central y extrae sus fundamentos.
2. Calcula la tasa que sugiere una regla de Taylor con datos actuales y compara con la vigente.
3. Construye la brecha de repreciación de un balance bancario simplificado.
4. Estima el efecto de un alza de 100 pb sobre margen, valor de cartera y provisiones.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen expectativas equivocadas sobre el efecto de una decisión. Las causas están en ignorar los rezagos o en confundir tasa nominal con real.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se espera efecto inmediato sobre la inflación | Rezagos ignorados | El efecto pleno toma 4–8 trimestres. |
| Se mira solo el efecto en el margen | Valor económico omitido | Mide también el efecto sobre el valor. |
| Se supone traslado completo y simétrico | Transmisión asimétrica | Las bajas se trasladan menos y más lento. |
| Se usa la regla de Taylor como regla de decisión | Es una referencia | Complementa con proyecciones y balance de riesgos. |
| Se ignora la beta de depósitos | Supuesto implícito de cero | Estímala con datos históricos. |
| Se provisiona al ver la morosidad | Rezago de 3–6 trimestres | Anticipa con escenarios. |

## ❓ Preguntas de comprobación

1. ¿Por qué la política monetaria se decide mirando proyecciones y no datos observados?
2. Nombra los cinco canales de transmisión y su rezago aproximado.
3. Calcula la tasa sugerida por una regla de Taylor con datos que elijas.
4. ¿Por qué el efecto sobre el margen puede ser pequeño y el efecto sobre el valor económico enorme?
5. ¿Qué significa que la transmisión sea asimétrica y por qué ocurre?

## 📥 Entregable

Guarda en `portfolio/parte-06/clase-10/`:

- el análisis de tres comunicados con sus fundamentos extraídos;
- el cálculo de la regla de Taylor comparado con la tasa vigente y la explicación de la brecha;
- la brecha de repreciación construida de un balance;
- la estimación del efecto de 100 pb sobre margen, valor y provisiones.

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

- Mishkin, F. (2022). *The Economics of Money, Banking and Financial Markets* (13.ª ed.). Pearson. Capítulos 15 a 17: instrumentos, objetivos y transmisión.
- Blanchard, O. (2021). *Macroeconomía* (8.ª ed.). Pearson. Capítulos 4 y 23: política monetaria y sus límites.
- Taylor, J. (1993). "Discretion versus Policy Rules in Practice". *Carnegie-Rochester Conference Series*. Formulación original de la regla.
- Bank for International Settlements (2023). *Annual Economic Report*, capítulo sobre transmisión de la política monetaria al sistema bancario. <https://www.bis.org/publ/arpdf/ar2023e.htm>
- Basel Committee on Banking Supervision (2016). *Interest rate risk in the banking book*. BIS. Medición del efecto de la tasa sobre margen y valor económico. <https://www.bis.org/bcbs/publ/d368.htm>
- Verificación local: descarga los comunicados y el informe de política monetaria de tu banco central, con su meta de inflación y su estimación de tasa neutral.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 09 · Política fiscal](09-politica-fiscal.md) | [Parte 06](../README.md) · [Programa](../../../SYLLABUS.md) | [11 · Bancos centrales →](11-bancos-centrales.md) |
<!-- gen:footer:end -->
