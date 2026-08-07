---
part: 8
class: 10
title: "Construcción de portafolios"
level: avanzado
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 10 · Construcción de portafolios

> [← 09 · Diversificación](09-diversificacion.md) · [Índice de la parte](../README.md) · [11 · Análisis fundamental →](11-analisis-fundamental.md)

**Parte 08 — Inversiones y mercados** · **Nivel:** Avanzado — perfil analista · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Integrar todo lo anterior en un procedimiento que transforma un perfil y unos objetivos en una cartera
concreta, con instrumentos, pesos, límites y reglas. Esta clase entrega el método completo, desde la
asignación estratégica hasta la selección de instrumentos y la documentación de la decisión.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** asignación estratégica de táctica y de selección de instrumentos.
2. **Construir** la frontera eficiente de un conjunto de activos.
3. **Elegir** la asignación estratégica según perfil, objetivos y restricciones.
4. **Implementar** la cartera con instrumentos concretos y límites.
5. **Documentar** la construcción de forma auditable.

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
| `asignación estratégica` | Distribución de largo plazo entre clases de activo. Explica la mayor parte de la variación del retorno. |
| `asignación táctica` | Desviaciones temporales de la estratégica. Requiere convicción y disciplina. |
| `selección de instrumentos` | Elección concreta dentro de cada clase. |
| `frontera eficiente` | Conjunto de carteras con máximo retorno para cada nivel de riesgo. |
| `cartera de mercado` | Cartera de máxima relación retorno-riesgo, combinable con el activo libre de riesgo. |
| `restricción` | Límite que la cartera debe respetar: liquidez, moneda, normativa, política. |
| `costo de implementación` | Comisiones, diferenciales, impuestos. Reduce el retorno esperado. |

## 🧠 Modelo mental

Las tres decisiones tienen **impactos muy distintos**:

```text
ASIGNACIÓN ESTRATÉGICA   explica la mayor parte de la variación del retorno en el tiempo
ASIGNACIÓN TÁCTICA       aporta poco y consume mucha atención
SELECCIÓN DE INSTRUMENTOS aporta principalmente vía COSTO
```

Consecuencia: **dedicar el 80 % del esfuerzo a la asignación estratégica y al costo** produce mejores
resultados que dedicarlo a elegir el mejor fondo o el mejor momento.

## 📖 Desarrollo

### 1. Las tres decisiones

| Decisión | Horizonte | Frecuencia de revisión | Impacto |
|---|---|---|---|
| Estratégica | 5–30 años | Anual | Alto |
| Táctica | 3–18 meses | Trimestral | Bajo a medio |
| Selección | Permanente | Anual | Medio, vía costo |

### 2. Construir la frontera eficiente

Con tres clases de activo:

```text
                 E(r)      σ      correlaciones
renta variable   9,0 %   17,0 %   RV-RF: 0,15 · RV-INM: 0,55
renta fija       4,5 %    6,0 %   RF-INM: 0,25
inmobiliario     7,0 %   12,0 %
```

Carteras representativas de la frontera:

| Cartera | RV | RF | INM | E(r) | σ | Sharpe (r_f = 3,5 %) |
|---|---:|---:|---:|---:|---:|---:|
| Mínima varianza | 8 % | 82 % | 10 % | 5,00 % | 5,63 % | 0,266 |
| Conservadora | 20 % | 65 % | 15 % | 5,78 % | 6,54 % | 0,349 |
| Moderada | 40 % | 42 % | 18 % | 6,75 % | 8,86 % | 0,367 |
| **Óptima (máx. Sharpe)** | **45 %** | **35 %** | **20 %** | **7,03 %** | **9,53 %** | **0,370** |
| Agresiva | 65 % | 15 % | 20 % | 8,03 % | 12,42 % | 0,365 |
| Solo renta variable | 100 % | 0 % | 0 % | 9,00 % | 17,00 % | 0,324 |

**La cartera de máximo Sharpe no es la de máximo retorno.** Y añadir renta fija a una cartera 100 %
accionaria mejora el Sharpe aunque reduzca el retorno esperado.

### 3. Ajustar el nivel de riesgo

Con la cartera óptima identificada, el nivel de riesgo se ajusta **combinándola con el activo libre de
riesgo**, no cambiando su composición:

```text
w  proporción en la cartera óptima
1−w  en el activo libre de riesgo

E(r_p) = w × 7,03 % + (1−w) × 3,5 %
σ_p    = w × 9,53 %
```

| w | E(r_p) | σ_p |
|---:|---:|---:|
| 40 % | 4,91 % | 3,81 % |
| 60 % | 5,62 % | 5,72 % |
| 80 % | 6,32 % | 7,62 % |
| 100 % | 7,03 % | 9,53 % |

Este resultado —**separar la elección de la cartera de la elección del nivel de riesgo**— es uno de los
más útiles de la teoría de carteras. En la práctica se aplica con matices: las restricciones reales y
la imposibilidad de estimar correctamente los parámetros hacen que la solución sea aproximada.

### 4. Del modelo a la cartera real

Las limitaciones del modelo que hay que reconocer:

```text
· los parámetros (E(r), σ, ρ) se estiman con datos históricos y son inestables
· pequeños cambios en E(r) producen grandes cambios en la asignación óptima
· la optimización tiende a concentrar en los activos con mejores estimaciones,
  que suelen ser los peor estimados
```

Por eso las carteras reales se construyen con **restricciones que estabilizan el resultado**:

```text
· límites mínimos y máximos por clase (por ejemplo, RV entre 30 % y 60 %)
· límite máximo por instrumento (5 %)
· límite máximo por emisor, sector, país y moneda
· mínimo de liquidez
· prohibición de instrumentos no comprendidos
```

Y con enfoques que reducen la dependencia de las estimaciones:

| Enfoque | Descripción |
|---|---|
| Pesos iguales | Igual peso a cada clase. Simple y sorprendentemente robusto |
| Paridad de riesgo | Cada clase aporta el mismo riesgo, no el mismo peso |
| Mínima varianza | No requiere estimar retornos esperados, que es lo peor estimado |
| Ancla en la cartera de mercado | Punto de partida neutral, con desviaciones justificadas |

### 5. Implementación y documentación

```text
CARTERA CONSTRUIDA — [nombre] — [fecha]

ASIGNACIÓN ESTRATÉGICA          objetivo   rango permitido
  renta variable global            32 %      25 % – 40 %
  renta variable local             10 %       5 % – 15 %
  renta variable emergente          6 %       0 % – 10 %
  renta fija local                 26 %      20 % – 35 %
  renta fija global                 8 %       5 % – 12 %
  inmobiliario                      8 %       5 % – 12 %
  liquidez                         10 %       5 % – 20 %

IMPLEMENTACIÓN
  clase                    instrumento               peso   costo anual
  RV global                ETF índice global         32 %      0,12 %
  RV local                 fondo indexado local      10 %      0,45 %
  RV emergente             ETF emergentes             6 %      0,18 %
  RF local                 fondo deuda local         26 %      0,38 %
  RF global                ETF bonos globales         8 %      0,15 %
  inmobiliario             fondo inmobiliario         8 %      1,20 %
  liquidez                 fondo money market        10 %      0,25 %
                           COSTO PONDERADO                     0,33 %

LÍMITES
  máximo por instrumento                    35 %
  máximo por emisor individual               5 %
  mínimo de liquidez                         5 %
  máximo en moneda extranjera sin cobertura 50 %

REGLAS
  R1  rebalanceo si una clase sale de su rango
  R2  revisión de la asignación estratégica una vez al año
  R3  no hay asignación táctica: las desviaciones solo provienen del mercado
  R4  aporte mensual automático distribuido según la asignación objetivo

MÉTRICAS ESPERADAS
  retorno esperado     6,9 % nominal · 3,4 % real
  desviación estándar  9,1 %
  caída máxima estimada en escenario de estrés  −24 %
  límite de política                            −25 %  ✔
```

## 🧮 Ejemplo guiado

**Situación.** Construye la cartera de una persona con estos datos.

```text
patrimonio invertible          85 000 000
aporte mensual                    420 000
horizonte principal              22 años (retiro)
objetivo intermedio              cambio de vivienda en 6 años, 30 000 000
pérdida máxima aceptable         22 %
restricciones                    sin instrumentos que no comprenda
                                 máximo 40 % en moneda extranjera
                                 necesita 8 000 000 líquidos permanentes
```

**Paso 1 — separa por objetivo, no por instrumento.**

```text
objetivo A: liquidez permanente         8 000 000   horizonte: 0
objetivo B: vivienda en 6 años         30 000 000   horizonte: 6 años
objetivo C: retiro                     47 000 000   horizonte: 22 años
                                       + aportes mensuales
```

**Paso 2 — asigna cada objetivo según su horizonte.**

```text
A (0 años):   100 % liquidez
B (6 años):   40 % renta variable / 60 % renta fija  → caída máxima estimada −11 %
C (22 años):  65 % renta variable / 35 % renta fija  → caída máxima estimada −29 %
```

**Paso 3 — verifica el límite de pérdida a nivel de cartera total.**

```text
peso de cada objetivo:
  A: 8/85 = 9,4 %
  B: 30/85 = 35,3 %
  C: 47/85 = 55,3 %

caída máxima ponderada = 0,094×0 + 0,353×0,11 + 0,553×0,29 = 0,0388 + 0,1604 = 19,9 %
límite de política: 22 %  ✔ cumple
```

**Paso 4 — asignación consolidada.**

| Clase | Objetivo A | Objetivo B | Objetivo C | Total | % |
|---|---:|---:|---:|---:|---:|
| Liquidez | 8 000 000 | 0 | 0 | 8 000 000 | 9,4 % |
| Renta fija local | 0 | 12 000 000 | 10 500 000 | 22 500 000 | 26,5 % |
| Renta fija global | 0 | 6 000 000 | 5 950 000 | 11 950 000 | 14,1 % |
| RV global | 0 | 9 000 000 | 21 150 000 | 30 150 000 | 35,5 % |
| RV local | 0 | 3 000 000 | 6 110 000 | 9 110 000 | 10,7 % |
| RV emergente | 0 | 0 | 3 290 000 | 3 290 000 | 3,9 % |
| **Total** | **8 000 000** | **30 000 000** | **47 000 000** | **85 000 000** | **100 %** |

**Paso 5 — verifica las restricciones.**

```text
moneda extranjera: RF global 14,1 % + RV global 35,5 % + RV emergente 3,9 % = 53,5 %
límite: 40 %  ✗ INCUMPLE
```

Ajuste necesario:

```text
opción 1: cubrir cambiariamente parte de la renta fija global
          → 11,95 M cubiertos → exposición cae a 39,4 %  ✔
          costo de la cobertura: ~0,4 % anual sobre el monto cubierto = 47 800/año

opción 2: reducir RV global y aumentar RV local
          → aumenta la concentración geográfica y el riesgo
```

**La opción 1 es preferible:** mantiene la diversificación y el costo es acotado.

**Paso 6 — implementación y verificación final.**

```text
IMPLEMENTACIÓN
  liquidez              fondo money market local          9,4 %   0,25 %
  RF local              fondo deuda local                26,5 %   0,38 %
  RF global cubierta    ETF bonos globales + cobertura   14,1 %   0,55 %
  RV global             ETF índice global                35,5 %   0,12 %
  RV local              fondo indexado local             10,7 %   0,45 %
  RV emergente          ETF emergentes                    3,9 %   0,18 %
                        COSTO PONDERADO                           0,30 %

VERIFICACIONES FINALES
  □ caída máxima estimada 19,9 % ≤ límite 22 %                    ✔
  □ moneda extranjera 39,4 % ≤ límite 40 %                        ✔
  □ liquidez 9,4 % ≥ mínimo requerido 8 000 000                   ✔
  □ ningún instrumento supera el 40 %                              ✔
  □ todos los instrumentos son comprendidos por el inversionista   ✔
  □ costo total 0,30 % anual                                       ✔
  □ objetivo B tiene horizonte y riesgo alineados                  ✔

RETORNO ESPERADO: 7,1 % nominal · 3,6 % real
PROBABILIDAD DE ALCANZAR EL OBJETIVO B EN 6 AÑOS: 78 %
```

**Paso 7 — la verificación que suele omitirse.**

```text
probabilidad de alcanzar el objetivo B: 78 %
¿es suficiente?

si NO: opciones
  · aumentar el aporte destinado a B
  · postergar la meta a 8 años (probabilidad sube a 89 %)
  · reducir el monto objetivo
  · aceptar el 78 % con un plan de contingencia

la decisión es del inversionista, y debe tomarla con el número a la vista
```

**Interpreta:** la construcción por objetivos —en lugar de una sola cartera— permitió alinear horizonte
y riesgo en cada uno, y **la restricción de moneda obligó a un ajuste que una optimización mecánica
habría pasado por alto**. La verificación final con checklist es lo que hace la construcción auditable.

## 🏦 Del cliente al banco

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| Asignación estratégica | Política de inversión institucional | 11, clase 12 |
| Límites por clase y emisor | Marco de apetito de riesgo | 11, clase 12 |
| Costo de implementación | Comparación de vehículos | 8, clase 13 |
| Construcción por objetivos | Asesoría patrimonial | 15, clase 6 |
| Verificación con checklist | Control de cumplimiento de política | 12, clase 12 |

## 🧪 Práctica

En `labs/lab-05.md`, sección de portafolios:

1. Construye la frontera eficiente de tres clases de activo con datos reales.
2. Identifica la cartera de máximo Sharpe y la de mínima varianza.
3. Diseña una cartera por objetivos con horizontes distintos.
4. Verifica todas las restricciones con un checklist y documenta los ajustes.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se dedica el esfuerzo a elegir instrumentos | Impacto relativo mal entendido | La asignación estratégica y el costo pesan más. |
| La optimización concentra en un activo | Sensibilidad a las estimaciones | Impón restricciones de rango por clase. |
| Una sola cartera para todos los objetivos | Horizontes distintos | Construye por objetivo. |
| Se incumple una restricción sin notarlo | Sin checklist de verificación | Verifica todas las restricciones al final. |
| Se ignora el costo de implementación | Reduce el retorno esperado | Calcula el costo ponderado. |
| No se estima la probabilidad de alcanzar la meta | Objetivo sin verificación | Calcúlala y decide con el número a la vista. |

## ❓ Preguntas de comprobación

1. ¿Cuál de las tres decisiones explica la mayor parte de la variación del retorno?
2. ¿Por qué la cartera de máximo Sharpe no es la de máximo retorno?
3. ¿Cómo se ajusta el nivel de riesgo sin cambiar la composición de la cartera óptima?
4. ¿Por qué las carteras reales se construyen con restricciones de rango?
5. ¿Qué ventaja tiene construir por objetivos en lugar de una sola cartera?

## 📥 Entregable

Guarda en `portfolio/parte-08/clase-10/`:

- la frontera eficiente construida con datos reales y su gráfico;
- la cartera de máximo Sharpe y la de mínima varianza identificadas;
- tu cartera diseñada por objetivos con su implementación e instrumentos;
- el checklist de verificación completo con los ajustes documentados.

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

- Markowitz, H. (1952). "Portfolio Selection". *Journal of Finance*. Frontera eficiente.
- Bodie, Z., Kane, A. y Marcus, A. (2023). *Investments* (13.ª ed.). McGraw-Hill. Capítulos 6 a 8 y 28: construcción de carteras y política de inversión.
- Brinson, G., Hood, R. y Beebower, G. (1986). "Determinants of Portfolio Performance". *Financial Analysts Journal*. Peso relativo de la asignación de activos.
- Michaud, R. (1989). "The Markowitz Optimization Enigma: Is Optimized Optimal?". *Financial Analysts Journal*. Sensibilidad de la optimización a las estimaciones.
- DeMiguel, V., Garlappi, L. y Uppal, R. (2009). "Optimal Versus Naive Diversification". *Review of Financial Studies*. Robustez de la cartera de pesos iguales.
- Verificación local: usa series de índices locales e internacionales publicadas por la bolsa de tu país y por proveedores de índices, con su fecha.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 09 · Diversificación](09-diversificacion.md) | [Parte 08](../README.md) · [Programa](../../../SYLLABUS.md) | [11 · Análisis fundamental →](11-analisis-fundamental.md) |
<!-- gen:footer:end -->
