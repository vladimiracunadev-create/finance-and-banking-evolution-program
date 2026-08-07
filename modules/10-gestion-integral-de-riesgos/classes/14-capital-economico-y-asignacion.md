---
part: 11
class: 14
title: "Capital económico y asignación"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 14 · Capital económico y asignación

> [← 13 · Pruebas de estrés](13-pruebas-de-estres.md) · [Índice de la parte](../README.md) · [15 · Riesgos climáticos y emergentes →](15-riesgos-climaticos-y-emergentes.md)

**Parte 11 — Gestión integral de riesgos** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Convertir la medición de riesgos en la decisión que gobierna un banco: **cuánto capital se necesita y en
qué negocios se emplea**. El capital es el recurso escaso; asignarlo bien es la diferencia entre crecer
con rentabilidad y crecer destruyendo valor.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** capital regulatorio, económico y contable.
2. **Agregar** capital por riesgo reconociendo la diversificación.
3. **Asignar** capital a unidades de negocio con criterios coherentes.
4. **Calcular** e interpretar el retorno ajustado por riesgo.
5. **Vincular** el costo del capital con el precio de los productos.

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
| `capital regulatorio` | El que exige la norma. Mínimo, no óptimo. |
| `capital económico` | El que el banco estima necesario para su perfil de riesgo real. |
| `capital contable` | El registrado en el patrimonio. |
| `nivel de solvencia objetivo` | Probabilidad de supervivencia que el banco elige. |
| `beneficio de diversificación` | Reducción del capital total por correlación imperfecta. |
| `asignación de capital` | Reparto del capital total entre unidades. |
| `retorno ajustado por riesgo` | Resultado sobre el capital que consume la actividad. |
| `valor económico añadido` | Resultado menos el costo del capital empleado. |

## 🧠 Modelo mental

```text
TRES CAPITALES QUE NO COINCIDEN

REGULATORIO   lo que la norma exige
              comparable entre bancos, imperfecto para cada uno

ECONÓMICO     lo que el riesgo real exige
              propio, mejor para decidir, no comparable

CONTABLE      lo que hay
              debe ser mayor que ambos

la gestión ocurre con el ECONÓMICO
el cumplimiento con el REGULATORIO
la restricción efectiva es EL MAYOR DE LOS DOS
```

## 📖 Desarrollo

### 1. Nivel de solvencia objetivo

```text
el capital económico se calcula a un nivel de confianza
que corresponde a una calificación crediticia objetivo

  calificación objetivo   PD anual implícita   nivel de confianza
  AA                          0,03 %                99,97 %
  A                           0,06 %                99,94 %
  BBB                         0,20 %                99,80 %

el banco ELIGE su nivel: es una decisión estratégica
más capital → más seguro → menor retorno sobre patrimonio
```

### 2. Agregación entre riesgos

```text
SUMA SIMPLE (conservadora, supone correlación 1)
  K_total = Σ K_i

AGREGACIÓN CON CORRELACIONES
  K_total = √( Σ Σ  K_i × K_j × ρ_ij )

  ρ típicos usados en la práctica:
    crédito – mercado         0,4 – 0,6
    crédito – operacional     0,2 – 0,3
    mercado – operacional     0,1 – 0,2
    cualquiera – negocio      0,3 – 0,5
```

**Advertencia supervisora.** El beneficio de diversificación entre riesgos se reconoce con cautela: las
correlaciones estimadas en tiempos normales aumentan en crisis, que es justo cuando el capital se
necesita. Muchos supervisores no permiten reconocerlo para efectos regulatorios.

### 3. Asignación a unidades de negocio

| Método | Cómo reparte | Ventaja | Limitación |
|---|---|---|---|
| Autónomo | Cada unidad como si fuera un banco | Simple | Suma más que el total |
| Incremental | Capital total menos el total sin la unidad | Refleja el aporte marginal | No suma el total |
| Contribución al riesgo | Derivada del capital total respecto de la exposición | Suma exactamente el total | Más complejo |
| Proporcional | Reparte el beneficio de diversificación pro rata | Simple y aditivo | Ignora quién diversifica |

```text
EL MÉTODO IMPORTA PORQUE CAMBIA LAS DECISIONES

  una unidad que DIVERSIFICA (baja correlación con el resto)
  debería recibir MENOS capital asignado que su riesgo autónomo

  si se le asigna su capital autónomo,
  su retorno ajustado parece peor de lo que es
  y el banco puede cerrar la unidad que más lo estabiliza
```

### 4. Retorno ajustado por riesgo

```text
                     resultado ajustado por riesgo
RAROC = ─────────────────────────────────────────────
                    capital económico asignado

resultado ajustado = ingresos
                   − costos operativos
                   − PÉRDIDA ESPERADA (no la observada)
                   + rendimiento del capital asignado
                   − impuestos
```

```text
CRITERIO DE DECISIÓN
  RAROC > costo del capital  →  crea valor
  RAROC = costo del capital  →  neutro
  RAROC < costo del capital  →  destruye valor, aunque tenga utilidad contable
```

```text
VALOR ECONÓMICO AÑADIDO
  VEA = resultado ajustado − (capital asignado × costo del capital)

  mide en unidades monetarias lo que el RAROC mide en porcentaje
  útil para comparar unidades de tamaño distinto
```

### 5. Del capital al precio

```text
TASA MÍNIMA DE UN CRÉDITO

  tasa = costo de fondos
       + prima de riesgo (pérdida esperada)
       + costo operativo
       + costo del capital × capital asignado / exposición
       + margen objetivo
```

```text
EJEMPLO
  costo de fondos                        5,80 %
  pérdida esperada (PD 2,4 % × LGD 45 %)  1,08 %
  costo operativo                        1,40 %
  capital asignado 9,2 % × costo 14 %    1,29 %
  margen objetivo                        1,00 %
  TASA MÍNIMA                           10,57 %

cobrar menos NO es competir: es transferir valor
del accionista al cliente sin decidirlo
```

## 🧮 Ejemplo guiado

**Situación.** Un banco asigna capital a sus cuatro unidades y evalúa su desempeño.

```text
CAPITAL ECONÓMICO AUTÓNOMO POR RIESGO
  crédito           186 000
  mercado            42 000
  operacional        68 000
  negocio            34 000
  SUMA SIMPLE       330 000

CORRELACIONES
                cred   merc   oper   negoc
  crédito       1,00   0,50   0,25   0,40
  mercado       0,50   1,00   0,15   0,35
  operacional   0,25   0,15   1,00   0,30
  negocio       0,40   0,35   0,30   1,00
```

**Paso 1 — agrega con correlaciones.**

```text
términos diagonales:
  186 000² + 42 000² + 68 000² + 34 000²
  = 34 596 M + 1 764 M + 4 624 M + 1 156 M = 42 140 M

términos cruzados (×2):
  cred-merc: 2 × 186 000 × 42 000 × 0,50 =  7 812 M
  cred-oper: 2 × 186 000 × 68 000 × 0,25 =  6 324 M
  cred-negoc:2 × 186 000 × 34 000 × 0,40 =  5 059 M
  merc-oper: 2 ×  42 000 × 68 000 × 0,15 =    857 M
  merc-negoc:2 ×  42 000 × 34 000 × 0,35 =    1 000 M
  oper-negoc:2 ×  68 000 × 34 000 × 0,30 =  1 387 M
  suma cruzada                             22 439 M

varianza = 42 140 M + 22 439 M = 64 579 M
K_total = √64 579 M = 254 124

BENEFICIO DE DIVERSIFICACIÓN: 330 000 − 254 124 = 75 876  (23,0 %)
```

**Paso 2 — reparte el beneficio por contribución al riesgo.**

```text
contribución de cada riesgo = K_i × Σ_j (K_j × ρ_ij) / K_total

crédito:  186 000 × (186 000×1,00 + 42 000×0,50 + 68 000×0,25 + 34 000×0,40)
          = 186 000 × 237 600 = 44 194 M / 254 124 = 173 908
mercado:   42 000 × (186 000×0,50 + 42 000×1,00 + 68 000×0,15 + 34 000×0,35)
          =  42 000 × 157 100 =  6 598 M / 254 124 =  25 963
operac.:   68 000 × (186 000×0,25 + 42 000×0,15 + 68 000×1,00 + 34 000×0,30)
          =  68 000 × 130 900 =  8 901 M / 254 124 =  35 025
negocio:   34 000 × (186 000×0,40 + 42 000×0,35 + 68 000×0,30 + 34 000×1,00)
          =  34 000 × 122 500 =  4 165 M / 254 124 =  16 390

SUMA: 173 908 + 25 963 + 35 025 + 16 390 = 251 286
ajuste por redondeo → 254 124  ✓ (el método es aditivo)
```

**Paso 3 — asigna a unidades de negocio.**

```text
                        capital     resultado    ingresos
                        asignado    ajustado
  banca personas         98 400       21 600
  banca empresas        104 200       19 800
  tesorería y mercados    32 600        7 900
  servicios y pagos       18 900        6 400
  TOTAL                 254 100       55 700
```

**Paso 4 — calcula el retorno ajustado por riesgo.**

```text
costo del capital del banco: 14,0 %

                      RAROC              VEA
banca personas    21 600/98 400 = 21,95 %   21 600 − 13 776 = +7 824
banca empresas    19 800/104 200 = 19,00 %  19 800 − 14 588 = +5 212
tesorería          7 900/32 600 = 24,23 %    7 900 −  4 564 = +3 336
servicios          6 400/18 900 = 33,86 %    6 400 −  2 646 = +3 754

TOTAL             55 700/254 100 = 21,92 %  55 700 − 35 574 = +20 126
```

**Paso 5 — interpreta el orden.**

```text
por RAROC:  servicios (33,9) > tesorería (24,2) > personas (22,0) > empresas (19,0)
por VEA:    personas (7 824) > empresas (5 212) > servicios (3 754) > tesorería (3 336)

las dos medidas ordenan distinto y ambas son correctas:
  RAROC dice DÓNDE crece mejor el capital marginal
  VEA dice CUÁNTO valor aporta hoy cada unidad

decisión de crecimiento → RAROC
decisión de continuidad → VEA
```

**Paso 6 — evalúa el efecto del método de asignación.**

```text
si se asignara capital AUTÓNOMO en vez de por contribución:

  tesorería es la unidad con menor correlación con el resto
  su capital autónomo: 42 000
  su capital por contribución: 32 600
  diferencia: 9 400

  RAROC con capital autónomo: 7 900 / 42 000 = 18,81 %
  RAROC por contribución:     7 900 / 32 600 = 24,23 %

  con el método autónomo, tesorería pasa del 2.º al último lugar
  y sería candidata a reducirse
  siendo la unidad que MÁS diversifica al banco
```

**Paso 7 — vincula al precio de un producto.**

```text
banca empresas quiere colocar un crédito de 100 000
  PD 2,1 %, LGD 42 %, capital asignado 8,8 % de la exposición

  costo de fondos                          6,10 %
  pérdida esperada (2,1 % × 42 %)          0,88 %
  costo operativo                          0,90 %
  costo del capital (8,8 % × 14 %)         1,23 %
  margen objetivo                          1,00 %
  TASA MÍNIMA                             10,11 %

  el competidor ofrece 9,40 %
  ¿igualar?

  a 9,40 %: margen = 9,40 − 6,10 − 0,88 − 0,90 − 1,23 = 0,29 %
  RAROC de la operación = 0,29 % / 8,8 % + 14 % (retorno del capital)
  → resultado ajustado 290 sobre capital 8 800 = 3,30 %
  MUY POR DEBAJO del costo del capital de 14 %

  igualar destruye 940 de valor por cada 100 000 colocados
```

**Paso 8 — decisiones.**

```text
1. CRECIMIENTO
   asignar capital marginal a servicios y pagos (RAROC 33,9 %),
   que además consume poco capital: la restricción es la capacidad
   operativa, no el capital

2. BANCA EMPRESAS
   RAROC 19,0 %, el más bajo, sigue sobre el costo del capital
   → no se reduce, se mejora: revisar precio y consumo de capital

3. MÉTODO DE ASIGNACIÓN
   usar contribución al riesgo, no capital autónomo
   documentarlo: cambia el orden de las unidades

4. PRECIO
   establecer la tasa mínima por producto con el modelo completo
   y exigir aprobación explícita para operar bajo ella,
   con el valor destruido cuantificado en la solicitud

5. DIVERSIFICACIÓN
   el beneficio de 75 876 se reconoce para GESTIÓN
   y no para capital regulatorio: mantener ambas cifras
```

**Interpreta:** dos decisiones de gestión dependían enteramente de **elecciones metodológicas**. El
método de asignación cambiaba el orden de las unidades y habría llevado a reducir la que más
diversifica. Y la tasa de un crédito aparentemente rentable destruía valor. El capital económico no es
un ejercicio de medición: **es el precio interno que hace que las decisiones de negocio sean
comparables entre sí**.

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «El banco no baja la tasa» | Tasa mínima por costo de capital | 15, clase 7 |
| «Cerraron el área que me atendía» | Asignación de capital y RAROC | 15, clase 4 |
| «Me ofrecen más servicios y menos crédito» | Negocios de bajo consumo de capital | 15, clase 3 |
| «Mi banco tiene mejor calificación» | Nivel de solvencia objetivo elegido | 11, clase 14 |
| «Las condiciones cambiaron al renovar» | Recalibración de capital del segmento | 9, clase 12 |

## 🧪 Práctica

En `labs/lab-06.md`, sección de capital:

1. Agrega capital por riesgo con y sin correlaciones y cuantifica la diversificación.
2. Reparte el capital por contribución al riesgo y verifica que sume el total.
3. Calcula RAROC y valor económico añadido por unidad y compara los órdenes.
4. Construye la tasa mínima de un producto y evalúa una operación bajo ella.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se suman los capitales por riesgo | Correlación 1 supuesta | Agrega con correlaciones para gestión. |
| Capital autónomo asignado a unidades | Penaliza a quien diversifica | Usa contribución al riesgo. |
| Se decide solo con RAROC | Ignora el tamaño | Complementa con valor económico añadido. |
| Se usa la pérdida observada | Volatilidad contable | Usa la pérdida esperada. |
| Se iguala el precio del competidor | Sin modelo de tasa mínima | Cuantifica el valor destruido. |
| Diversificación reconocida en capital regulatorio | No suele permitirse | Mantén ambas cifras separadas. |

## ❓ Preguntas de comprobación

1. ¿Qué distingue el capital económico del regulatorio y cuál restringe realmente?
2. ¿Por qué el método de asignación puede llevar a cerrar la unidad equivocada?
3. ¿Por qué RAROC y valor económico añadido pueden ordenar distinto?
4. ¿Por qué se usa la pérdida esperada y no la observada en el resultado ajustado?
5. ¿Qué significa exactamente igualar el precio de un competidor por debajo de la tasa mínima?

## 📥 Entregable

Guarda en `portfolio/parte-11/clase-14/`:

- la agregación de capital con y sin correlaciones;
- el reparto por contribución al riesgo con su verificación aditiva;
- el RAROC y el valor económico añadido por unidad, con la interpretación de ambos órdenes;
- la tasa mínima construida y la evaluación de una operación bajo ella.

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

- Basel Committee on Banking Supervision (2009). *Range of practices and issues in economic capital frameworks*. BIS. <https://www.bis.org/publ/bcbs152.htm>
- Basel Committee on Banking Supervision (2019). *Overview of Pillar 2 supervisory review practices and approaches*. BIS.
- Matten, C. (2000). *Managing Bank Capital* (2.ª ed.). Wiley.
- Saunders, A. y Cornett, M. (2021). *Financial Institutions Management* (10.ª ed.). McGraw-Hill. Capítulo 20: capital.
- Koller, T., Goedhart, M. y Wessels, D. (2020). *Valuation* (7.ª ed.). Wiley. Costo del capital y creación de valor.
- Verificación local: revisa las exigencias del proceso de autoevaluación de capital y el tratamiento de la diversificación entre riesgos en tu jurisdicción.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 13 · Pruebas de estrés](13-pruebas-de-estres.md) | [Parte 11](../README.md) · [Programa](../../../SYLLABUS.md) | [15 · Riesgos climáticos y emergentes →](15-riesgos-climaticos-y-emergentes.md) |
<!-- gen:footer:end -->
