---
part: 1
class: 9
title: "Valor presente"
level: fundamento
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 09 · Valor presente

> [← 08 · Valor del dinero en el tiempo](08-valor-del-dinero-en-el-tiempo.md) · [Índice de la parte](../README.md) · [10 · Valor futuro →](10-valor-futuro.md)

**Parte 01 — Matemática financiera básica** · **Nivel:** Fundamento — sin conocimientos previos · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Convertir el principio de la clase 8 en la operación más usada de las finanzas profesionales:
**traer el futuro a hoy**. Todo precio de un bono, toda valoración de empresa, todo análisis de
proyecto y toda evaluación de crédito es, en el fondo, un valor presente. Esta clase enseña a
calcularlo, a leer su sensibilidad a la tasa y a reconocer cuándo el resultado depende más del
supuesto que del cálculo.

## 📚 Objetivos

Al finalizar podrás:

1. **Calcular** el valor presente de un flujo único y de un conjunto de flujos.
2. **Construir** e interpretar un factor de descuento y su tabla.
3. **Medir** la sensibilidad del valor presente a cambios en la tasa.
4. **Explicar** por qué los flujos lejanos pesan poco y qué implica para las proyecciones largas.
5. **Aplicar** el valor presente a una decisión real de compra o financiamiento.

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
| `valor presente (VP)` | `VP = F / (1+i)^n`. Lo que hay que tener hoy, a la tasa `i`, para llegar a `F` en `n` periodos. |
| `factor de descuento` | `1/(1+i)^n`. Siempre entre 0 y 1. Multiplica el flujo futuro; es la forma cómoda de trabajar en tabla. |
| `valor presente de una serie` | `VP = Σ Fₜ/(1+i)^t`. La suma de valores presentes individuales, nunca la suma de flujos descontada una vez. |
| `sensibilidad a la tasa` | El VP cae cuando la tasa sube, y cae más cuanto más lejano es el flujo. Es la raíz de la duración (Parte 7, clase 11). |
| `horizonte efectivo` | Plazo más allá del cual los flujos aportan poco al VP. Al 12 %, el año 30 aporta 3,3 % de un flujo constante. |
| `precisión falsa` | Un VP con seis decimales sobre flujos proyectados a diez años transmite una certeza que no existe. |

## 🧠 Modelo mental

El factor de descuento es un **filtro que va apagando el futuro**:

```text
i = 10 %
  año 1   0,9091   se conserva el 91 %
  año 5   0,6209   se conserva el 62 %
  año 10  0,3855   se conserva el 39 %
  año 20  0,1486   se conserva el 15 %
  año 30  0,0573   se conserva el 6 %
```

Por eso discutir el flujo del año 28 de una proyección es casi siempre discutir sobre nada, mientras
que discutir la tasa cambia todo el resultado. Saber dónde está la palanca es el criterio profesional.

## 📖 Desarrollo

### 1. Flujo único

```text
VP = F / (1 + i)^n
```

¿Cuánto vale hoy recibir 5 000 000 en 3 años, si la alternativa rinde 7 % anual?

```text
VP = 5 000 000 / (1,07)^3 = 5 000 000 / 1,225043 = 4 081 490
```

Lectura: **4 081 490 invertidos hoy al 7 % producen exactamente 5 000 000 en tres años**. Verificar
siempre en la dirección contraria:

```text
4 081 490 × 1,225043 = 5 000 001  ✔ (diferencia por redondeo)
```

### 2. Tabla de factores de descuento

Trabajar con factores evita recalcular potencias y hace visible la estructura:

| n | 5 % | 8 % | 12 % | 20 % |
|---:|---:|---:|---:|---:|
| 1 | 0,9524 | 0,9259 | 0,8929 | 0,8333 |
| 3 | 0,8638 | 0,7938 | 0,7118 | 0,5787 |
| 5 | 0,7835 | 0,6806 | 0,5674 | 0,4019 |
| 10 | 0,6139 | 0,4632 | 0,3220 | 0,1615 |
| 20 | 0,3769 | 0,2145 | 0,1037 | 0,0261 |
| 30 | 0,2314 | 0,0994 | 0,0334 | 0,0042 |

Lectura obligada de esta tabla: al 20 %, un peso del año 30 vale **cuatro milésimas** de peso hoy. Una
promesa a treinta años con tasa alta es, financieramente, casi nada.

### 3. Serie de flujos

```text
VP = Σ Fₜ / (1+i)^t
```

Un contrato paga 400 000, 600 000, 900 000 y 1 200 000 al final de cada uno de los próximos cuatro
años. Con `i = 9 %`:

| Año | Flujo | Factor | Valor presente |
|---:|---:|---:|---:|
| 1 | 400 000 | 0,9174 | 366 972 |
| 2 | 600 000 | 0,8417 | 505 008 |
| 3 | 900 000 | 0,7722 | 694 980 |
| 4 | 1 200 000 | 0,7084 | 850 080 |
| | **3 100 000** | | **2 417 040** |

Los flujos suman 3 100 000 nominales y valen 2 417 040 hoy. La diferencia de 682 960 es el costo del
tiempo, no una pérdida ni una comisión.

### 4. Sensibilidad a la tasa

El mismo contrato, descontado a distintas tasas:

| Tasa | Valor presente | Variación vs. 9 % |
|---:|---:|---:|
| 5 % | 2 665 000 | +10,3 % |
| 7 % | 2 535 000 | +4,9 % |
| 9 % | 2 417 040 | — |
| 12 % | 2 259 000 | −6,5 % |
| 15 % | 2 118 000 | −12,4 % |

Un cambio de 6 puntos en la tasa mueve el valor un 22 %. Esta es la razón por la cual toda valoración
seria se presenta como un **rango con tabla de sensibilidad**, no como un número. Cuando en la
Parte 13, clase 7, valores una empresa, la tabla de sensibilidad será la parte que el comité mire
primero.

### 5. Precisión honesta

```text
✗ "El proyecto vale 2 417 039,87"
✓ "El proyecto vale entre 2,1 y 2,7 millones según la tasa (9 % ± 3 pp);
   el caso base al 9 % es 2,42 millones."
```

La segunda formulación es más útil y más defendible. Un valor presente hereda **toda** la
incertidumbre de sus flujos y de su tasa; presentarlo al peso es una afirmación de precisión que los
datos no respaldan.

## 🧮 Ejemplo guiado

**Situación.** Un proveedor ofrece a una pyme dos formas de pagar una máquina:

```text
A  8 900 000 al contado
B  3 000 000 hoy + 24 cuotas de 270 000
```

La pyme puede colocar su excedente al 0,45 % mensual, y su línea de crédito cuesta 1,35 % mensual.

**Paso 1 — elige la tasa correcta.** La pyme **tiene** el dinero, así que pagar al contado significa
renunciar al 0,45 % mensual. Esa es la tasa de descuento: la alternativa real. Si no tuviera el
dinero, la tasa sería el 1,35 % de la línea.

**Paso 2 — valor presente de la opción B.**

```text
VP(cuotas) = 270 000 × [1 − (1,0045)^-24] / 0,0045
(1,0045)^24 = 1,113748 → (1,0045)^-24 = 0,897869
VP(cuotas) = 270 000 × (1 − 0,897869)/0,0045 = 270 000 × 22,6958 = 6 127 866
VP(B) = 3 000 000 + 6 127 866 = 9 127 866
```

(La fórmula de la serie de cuotas iguales se demuestra en la Parte 7, clase 4; aquí se usa como
herramienta.)

**Paso 3 — compara.**

| Opción | Valor presente | Diferencia |
|---|---:|---:|
| A — contado | 8 900 000 | — |
| B — financiado | 9 127 866 | +227 866 |

**Paso 4 — ¿y si no tuviera el dinero?** Con la tasa de la línea de crédito, 1,35 % mensual:

```text
(1,0135)^-24 = 0,724847
VP(cuotas) = 270 000 × (1 − 0,724847)/0,0135 = 270 000 × 20,3817 = 5 503 059
VP(B) = 3 000 000 + 5 503 059 = 8 503 059   ← ahora B es MEJOR que A por 396 941
```

**Paso 5 — interpreta.** La misma oferta es peor o mejor **según con qué dinero se compare**. No hay
una respuesta universal: hay una respuesta por situación. Este resultado —que la tasa de descuento
cambia la decisión, no solo el número— es el aprendizaje central de la clase.

**Paso 6 — verificación de razonabilidad.** El costo implícito del financiamiento de B es la tasa que
iguala ambas opciones. Está entre 0,45 % y 1,35 % mensual; resolviendo, ≈ 0,79 % mensual (10,0 %
efectivo anual). Si la pyme consigue rendimiento superior a 0,79 % mensual, conviene financiar.

## 🏦 Del cliente al banco

| Aplicación | Quién la usa | Parte del programa |
|---|---|---|
| Precio de un bono | Mesa de dinero | Parte 8, clase 4 |
| Valoración de una empresa | Banca de inversión | Parte 13, clase 7 |
| Provisión por pérdida esperada | Riesgo de crédito | Parte 9, clase 14 |
| Costo amortizado de un instrumento | Contabilidad NIIF 9 | Parte 5, clase 13 |
| Decisión contado vs. cuotas | Cualquier persona | Esta clase |

## 🧪 Práctica

En `labs/lab-05.md`:

1. Construye tu propia tabla de factores de descuento para cuatro tasas y seis plazos.
2. Descuenta una serie de cinco flujos y verifica capitalizando de vuelta.
3. Elabora la tabla de sensibilidad del VP a la tasa en cinco escenarios.
4. Resuelve una decisión real contado vs. cuotas con dos tasas de descuento distintas y explica el cambio.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| El VP resulta mayor que la suma de los flujos | Se capitalizó en vez de descontar | Descontar **divide** por `(1+i)^n`. |
| Se descuenta la suma de los flujos una sola vez | Se ignoró que cada flujo tiene su propio `n` | `VP = Σ Fₜ/(1+i)^t`, flujo por flujo. |
| El resultado es muy distinto al de un compañero | Tasas de descuento distintas | Declara la tasa y su justificación junto al resultado. |
| Un VP se presenta con céntimos | Falsa precisión | Presenta rango y caso base; redondea a la magnitud del dato peor conocido. |
| Se descuenta con tasa anual flujos mensuales | Unidades incompatibles | Convierte la tasa (Parte 7, clase 3). |
| Los flujos lejanos dominan la conclusión | Tasa demasiado baja o proyección demasiado optimista | Revisa el horizonte efectivo y muestra el peso de cada año. |

## ❓ Preguntas de comprobación

1. ¿Cuánto hay que depositar hoy al 6 % para tener 10 000 000 en 8 años?
2. ¿Por qué un flujo del año 30 descontado al 20 % es prácticamente irrelevante?
3. ¿Qué le ocurre al valor presente cuando la tasa sube, y por qué el efecto es mayor en los flujos lejanos?
4. Dos analistas valoran el mismo contrato en 2,4 y 2,7 millones. ¿Qué es lo primero que hay que comparar?
5. ¿Por qué la decisión contado vs. cuotas puede invertirse según quién la evalúe?

## 📥 Entregable

Guarda en `portfolio/parte-01/clase-09/`:

- la tabla de factores de descuento construida por ti;
- una serie descontada con su verificación en sentido inverso;
- la tabla de sensibilidad del valor presente;
- la decisión contado vs. cuotas resuelta con dos tasas y una conclusión de 200 palabras.

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

- Brealey, R., Myers, S. y Allen, F. (2023). *Principios de finanzas corporativas* (14.ª ed.). McGraw-Hill. Capítulo 2: valor presente y factores de descuento.
- Ross, S., Westerfield, R. y Jordan, B. (2022). *Fundamentos de finanzas corporativas* (12.ª ed.). McGraw-Hill. Capítulos 4 y 5: descuento de flujos múltiples.
- Damodaran, A. (2012). *Investment Valuation* (3.ª ed.). Wiley. Capítulos 2 y 3: valor presente como base de toda valoración y análisis de sensibilidad.
- Koller, T., Goedhart, M. y Wessels, D. (2020). *Valuation: Measuring and Managing the Value of Companies* (7.ª ed.). McKinsey/Wiley. Capítulo 6: horizonte y peso de los flujos lejanos.
- IFRS Foundation (2014). *NIIF 9 Instrumentos Financieros*, apéndice A: definición de costo amortizado y tasa de interés efectiva.
- Verificación local: contrasta la tasa de descuento con la tasa de captación o de colocación vigente publicada por el supervisor financiero de tu país.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 08 · Valor del dinero en el tiempo](08-valor-del-dinero-en-el-tiempo.md) | [Parte 01](../README.md) · [Programa](../../../SYLLABUS.md) | [10 · Valor futuro →](10-valor-futuro.md) |
<!-- gen:footer:end -->
