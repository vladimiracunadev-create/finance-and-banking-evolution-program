<!-- meta
part: 8
class: 7
title: "Divisas y commodities"
level: avanzado
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 07 · Divisas y commodities

> [← 06 · ETF y fondos indexados](06-etf.md) · [Índice de la parte](../README.md) · [08 · Riesgo y rentabilidad →](08-riesgo-y-rentabilidad.md)

**Parte 08 — Inversiones y mercados** · **Nivel:** Avanzado — perfil analista · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Analizar dos clases de activo que no generan flujo por sí mismas y cuya rentabilidad proviene
únicamente del cambio de precio. Esa característica las hace estructuralmente distintas de acciones y
bonos, y determina el papel limitado que deben tener en una cartera de largo plazo.

Los cuatro instrumentos anteriores producen flujos: dividendos, cupones o participaciones en ellos. Los de esta clase no producen ninguno, y esa diferencia cambia por completo cómo se analizan: su rentabilidad depende solo del precio y, en el caso de los futuros, de un efecto de rolado que sorprende a quien no lo conoce.

## 📚 Objetivos

Al finalizar podrás:

1. **Explicar** por qué una divisa o un commodity no generan flujo y qué implica.
2. **Distinguir** cobertura de especulación y aplicar el criterio.
3. **Descomponer** el retorno de una posición en commodities.
4. **Evaluar** el papel de estos activos en una cartera diversificada.
5. **Reconocer** los riesgos específicos de los instrumentos apalancados.

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

Los tres primeros términos son la naturaleza del activo y sus dos usos; los cuatro siguientes, la mecánica de los futuros y su riesgo. El **retorno de rolado** es el concepto que explica por qué un fondo de materias primas puede perder dinero con el precio del subyacente subiendo.

| Concepto | Comprensión verificable |
|---|---|
| `activo sin flujo` | No paga cupón, dividendo ni arriendo. Su único retorno es el cambio de precio. |
| `cobertura` | Tomar una posición que compensa un riesgo que **ya tienes**. |
| `especulación` | Tomar una posición para ganar con un movimiento de precio. Crea exposición nueva. |
| `contango` | La curva de futuros es ascendente: los contratos lejanos valen más. |
| `backwardation` | La curva es descendente. |
| `retorno de rolado` | Ganancia o pérdida al renovar un contrato de futuros. Puede dominar el retorno total. |
| `apalancamiento` | Exposición superior al capital comprometido. Multiplica ganancias y pérdidas. |

## 🧠 Modelo mental

La diferencia estructural con acciones y bonos:

```text
ACCIÓN   una empresa produce, vende y genera utilidad → hay un flujo subyacente
BONO     un deudor paga cupones                        → hay un flujo subyacente
DIVISA   no produce nada                               → NO hay flujo
ORO      no produce nada                               → NO hay flujo
```

Consecuencia: **su valor esperado de largo plazo depende únicamente de que alguien pague más
después**. Eso no las hace inválidas —cumplen funciones específicas— y sí explica por qué no pueden
ser el núcleo de una cartera de acumulación.

## 📖 Desarrollo

### 1. Divisas

Una divisa no es una inversión sino una exposición, y conviene tratarla como tal. El esquema lo plantea.

```text
comprar una divisa = tomar posición sobre el diferencial de tasas y sobre la
                     evolución relativa de dos economías
```

Componentes del retorno de mantener una divisa extranjera:

```text
retorno = variación del tipo de cambio + tasa de interés de esa moneda
                                        − tasa de interés de la moneda local
```

```text
tasa local 8,5 % · tasa externa 4,5 % · tipo de cambio estable
retorno de mantener la moneda externa = 0 + 4,5 − 8,5 = −4,0 % anual
```

**Mantener una divisa con tasa menor tiene un costo cierto**, que solo se compensa si la moneda se
aprecia. La paridad de tasas (Parte 7, clase 2) indica cuánta apreciación está implícita en el
mercado.

Usos legítimos de una posición en divisas:

| Uso | Naturaleza |
|---|---|
| Cubrir un pasivo en esa moneda | Cobertura |
| Cubrir un gasto futuro cierto (estudios, viaje) | Cobertura |
| Diversificar el riesgo de la moneda local | Diversificación |
| Apostar a una depreciación | **Especulación** |

### 2. Commodities

Las materias primas se acceden casi siempre por futuros, y ahí aparece el rolado. El esquema muestra el mecanismo.

```text
tipos: energía (petróleo, gas), metales industriales (cobre, aluminio),
       metales preciosos (oro, plata), agrícolas (trigo, soja, café)
```

El acceso habitual es mediante **futuros**, no mediante el bien físico, y ahí aparece el componente
que domina el retorno:

```text
retorno total = retorno del precio spot
              + retorno de rolado
              + retorno de la garantía (colateral)
```

**El retorno de rolado:**

```text
CONTANGO (curva ascendente)
  contrato a 1 mes: 82,0 · contrato a 2 meses: 83,4
  al renovar, vendes a 82,0 y compras a 83,4 → PIERDES 1,7 %
  si el spot no se mueve, pierdes ese 1,7 % cada mes

BACKWARDATION (curva descendente)
  contrato a 1 mes: 82,0 · contrato a 2 meses: 80,8
  al renovar, ganas 1,5 %
```

Este efecto explica por qué **un índice de commodities puede caer significativamente mientras el
precio spot se mantiene estable**: el rolado en contango sostenido erosiona el valor mes a mes.

### 3. El oro como caso particular

El oro se comporta distinto del resto de materias primas y su papel en una cartera se discute con argumentos propios. La tabla los recoge.

```text
argumentos habituales a favor              evidencia
"protege de la inflación"                  la relación es débil en horizontes de 5-10 años
"refugio en crisis"                        se cumple en algunos episodios, no en todos
"reserva de valor de largo plazo"          en horizontes muy largos, aproximadamente mantiene
                                            poder de compra, sin generar rendimiento real
"diversifica"                              su correlación con acciones es baja, y eso sí es cierto
```

La afirmación defendible: **el oro tiene baja correlación con las acciones y no genera flujo**. Esa
combinación lo hace útil como diversificador en proporciones pequeñas (habitualmente 0 % a 10 %) y
inadecuado como núcleo de una cartera.

### 4. Papel en una cartera

Estos activos tienen un papel acotado y justificable en una cartera, o ninguno. La tabla recoge los argumentos de ambos lados.

| Activo | Correlación con acciones | Genera flujo | Papel razonable |
|---|---|---|---|
| Acciones | 1,00 | Sí | Núcleo de crecimiento |
| Bonos | 0,0 a 0,4 | Sí | Estabilización y flujo |
| Inmuebles | 0,4 a 0,6 | Sí (arriendo) | Diversificación con flujo |
| Oro | −0,1 a 0,2 | No | Diversificador, 0–10 % |
| Commodities amplios | 0,3 a 0,5 | No | Cobertura de inflación parcial, 0–10 % |
| Divisas | Variable | Tasa de la moneda | Cobertura de pasivos o gastos |

Regla defendible: **los activos sin flujo se limitan a una proporción menor y su función es
diversificar, no generar retorno**.

### 5. Instrumentos apalancados

Los productos apalancados sobre estos activos tienen un comportamiento que no es el que sugiere su nombre. El esquema muestra el efecto de la composición diaria.

```text
un ETF apalancado 3x busca replicar TRES VECES el movimiento DIARIO del índice
```

El problema es el reajuste diario:

```text
índice     día 1: +10 %  · día 2: −9,09 %  → vuelve al inicio (0 %)
ETF 3x     día 1: +30 %  · día 2: −27,27 % → 1,30 × 0,7273 = 0,945 → −5,5 %
```

**El índice terminó igual y el ETF apalancado perdió 5,5 %.** El efecto se acumula: en mercados
volátiles y sin tendencia, un instrumento apalancado pierde valor de forma sistemática.

```text
consecuencia: los instrumentos apalancados están diseñados para posiciones
de UNO O POCOS DÍAS, no para mantener
```

Los productos inversos y los apalancados sobre volatilidad tienen el mismo problema, agravado. Varios
han perdido más del 90 % de su valor en periodos en que su índice de referencia se mantuvo estable.

## 🧮 Ejemplo guiado

**Situación.** Un inversionista de perfil moderado quiere "protegerse de la inflación" y le proponen
tres alternativas.

```text
A  10 % de la cartera en un ETF de oro
B  10 % en un ETF de commodities amplios
C  10 % en bonos indexados a la inflación
```

Cartera actual: 80 000 000, compuesta 55 % renta variable / 45 % renta fija nominal.

**Paso 1 — evalúa la relación de cada activo con la inflación.**

```text
A  oro: correlación con la inflación en horizontes de 5 años: baja y variable
        protege en algunos episodios inflacionarios y no en otros
        no tiene mecanismo contractual de protección

B  commodities: la energía y los alimentos SON componentes de la inflación
                correlación positiva y más estable que el oro
                pero sujeto a retorno de rolado

C  bonos indexados: el principal y el cupón se ajustan CONTRACTUALMENTE por inflación
                    protección MECÁNICA, no estadística
```

**Solo C tiene un mecanismo contractual de protección.** A y B tienen una relación estadística
variable.

**Paso 2 — analiza el retorno de rolado de B.**

```text
el índice de commodities ha estado en contango la mayor parte de los últimos años
retorno de rolado histórico estimado: −2 % a −5 % anual

→ para que B entregue retorno real positivo, el precio spot debe subir
  más de 2–5 % anual por sobre la inflación, de forma sostenida
```

**Paso 3 — evalúa el efecto en la cartera.**

Sustituyendo 10 % de renta fija nominal por cada alternativa:

| Cartera | Rentabilidad esperada | Desviación estándar | Correlación con inflación |
|---|---:|---:|---|
| Actual (55/45) | 6,8 % | 10,2 % | Negativa (la renta fija nominal pierde) |
| Con A (oro) | 6,7 % | 10,0 % | Débil positiva |
| Con B (commodities) | 6,6 % | 10,9 % | Media positiva |
| Con C (indexados) | 6,5 % | 9,6 % | **Alta positiva** |

**Paso 4 — prueba de estrés inflacionario.**

```text
escenario: inflación pasa de 3 % a 8 % durante 3 años

efecto en cada cartera (rentabilidad REAL acumulada de 3 años):
  actual:            −6,4 %   (la renta fija nominal pierde poder de compra)
  con oro:           −4,1 %
  con commodities:   −2,8 %
  con indexados:     −3,2 %

efecto en un escenario de inflación baja y crecimiento (3 % → 2 %):
  actual:            +18,2 %
  con oro:           +16,9 %
  con commodities:   +15,1 %
  con indexados:     +17,8 %
```

**Paso 5 — el hallazgo.**

```text
en el escenario inflacionario, commodities protege algo más que indexados
en el escenario benigno, indexados cuesta mucho menos

commodities: mejora 3,6 puntos en el escenario malo, cuesta 3,1 puntos en el bueno
indexados:   mejora 3,2 puntos en el escenario malo, cuesta 0,4 puntos en el bueno

→ indexados tiene mejor relación entre protección y costo de oportunidad
```

**Paso 6 — recomendación.**

```text
RECOMENDACIÓN
  C (bonos indexados) por 10 %, sustituyendo renta fija nominal
  
  fundamento:
   · protección contractual, no estadística
   · menor costo de oportunidad en el escenario benigno
   · reduce la desviación estándar de la cartera (9,6 % vs. 10,2 %)
   · sin retorno de rolado negativo

  el oro podría incorporarse en un 3–5 % como diversificador, NO como protección
  inflacionaria, y declarándolo así en la política de inversión

  commodities amplios NO se recomienda para este perfil:
   · aumenta la volatilidad
   · el retorno de rolado en contango erosiona el valor
   · requiere seguimiento activo que el inversionista no hará

ADVERTENCIA: el objetivo declarado era "protegerse de la inflación".
Si el objetivo real es "ganar más", ninguna de las tres alternativas lo resuelve
y la conversación es otra.
```

**Interpreta:** las tres alternativas se presentaban como equivalentes bajo la etiqueta "protección
inflacionaria". **Solo una tiene un mecanismo contractual**; las otras dos tienen una relación
estadística que se cumple a veces. Distinguir protección mecánica de correlación histórica es el
aporte técnico de esta clase.

## 🏦 Del cliente al banco

El cliente ve una oportunidad y el banco gestiona una posición de tesorería o cubre a un cliente. La tabla enfrenta las dos lecturas.

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| Cobertura vs. especulación | Política de uso de derivados | 11, clase 6 |
| Posición en divisas | Descalce cambiario del banco | 11, clase 6 |
| Retorno de rolado | Valoración de posiciones en futuros | 11, clase 3 |
| Productos apalancados | Idoneidad y advertencias obligatorias | 12, clase 4 |
| Bonos indexados | Instrumento de calce de pasivos indexados | 11, clase 5 |

## 🧪 Práctica

El laboratorio pide medir el efecto del rolado sobre un año de futuros en contango. La pérdida acumulada sin que el precio del subyacente baje es el resultado que el ejercicio busca.

En `labs/lab-04.md`:

1. Calcula el retorno de mantener tres divisas considerando el diferencial de tasas.
2. Analiza la curva de futuros de un commodity y estima su retorno de rolado.
3. Simula el efecto del reajuste diario en un instrumento apalancado durante 60 días.
4. Compara tres alternativas de protección inflacionaria en dos escenarios.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen pérdidas con el subyacente al alza. La causa es el rolado o la composición diaria de un producto apalancado.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se compra oro "porque protege de la inflación" | Correlación supuesta | Su relación con la inflación es débil y variable. |
| Se mantiene un ETF apalancado semanas | Reajuste diario ignorado | Están diseñados para uno o pocos días. |
| Se ignora el retorno de rolado | Solo se miró el precio spot | En contango, el rolado erosiona sistemáticamente. |
| Se llama cobertura a una especulación | Concepto mal aplicado | Cobertura compensa un riesgo existente. |
| Se mantiene una divisa con tasa menor | Costo de acarreo ignorado | Calcula el diferencial de tasas. |
| Se asigna una proporción alta a activos sin flujo | Función mal entendida | Son diversificadores, no generadores de retorno. |

## ❓ Preguntas de comprobación

1. ¿Por qué un activo sin flujo no puede ser el núcleo de una cartera de acumulación?
2. Calcula el retorno de mantener una divisa con tasa de 3 % cuando la local paga 9 %.
3. ¿Qué es el retorno de rolado y cuándo es negativo?
4. Demuestra por qué un ETF apalancado 3x pierde valor en un mercado volátil sin tendencia.
5. ¿Qué distingue una protección contractual de una correlación histórica?

## 📥 Entregable

Guarda en `portfolio/parte-08/clase-07/`:

- el retorno calculado de mantener tres divisas con su diferencial de tasas;
- el análisis de la curva de futuros de un commodity con su retorno de rolado estimado;
- la simulación del efecto del reajuste diario en 60 días;
- la comparación de alternativas de protección inflacionaria en dos escenarios.

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

- Bodie, Z., Kane, A. y Marcus, A. (2023). *Investments* (13.ª ed.). McGraw-Hill. Capítulos 22 y 23: futuros, commodities y divisas.
- Hull, J. (2021). *Options, Futures, and Other Derivatives* (11.ª ed.). Pearson. Capítulos 2, 3 y 5: mecánica de futuros, contango y cobertura.
- Erb, C. y Harvey, C. (2006). "The Strategic and Tactical Value of Commodity Futures". *Financial Analysts Journal*. Descomposición del retorno de commodities.
- Erb, C. y Harvey, C. (2013). "The Golden Dilemma". *Financial Analysts Journal*. Evidencia sobre el oro como protección inflacionaria.
- Cheng, M. y Madhavan, A. (2009). "The Dynamics of Leveraged and Inverse ETFs". *Journal of Investment Management*. Efecto del reajuste diario.
- Verificación local: consulta las curvas de futuros publicadas por las bolsas de commodities y el tipo de cambio y las tasas de tu banco central.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 06 · ETF y fondos indexados](06-etf.md) | [Parte 08](../README.md) · [Programa](../../../SYLLABUS.md) | [08 · Riesgo y rentabilidad →](08-riesgo-y-rentabilidad.md) |
<!-- gen:footer:end -->
