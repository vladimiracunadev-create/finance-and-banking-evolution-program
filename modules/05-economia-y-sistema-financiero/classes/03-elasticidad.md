---
part: 6
class: 3
title: "Elasticidad"
level: intermedio
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 03 · Elasticidad

> [← 02 · Oferta y demanda](02-oferta-y-demanda.md) · [Índice de la parte](../README.md) · [04 · Competencia y estructuras de mercado →](04-competencia-y-estructuras-de-mercado.md)

**Parte 06 — Economía y sistema financiero** · **Nivel:** Intermedio — requiere las partes anteriores · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Medir cuánto responde una variable ante el cambio de otra, que es la información que convierte el
modelo de oferta y demanda en una herramienta de decisión. Un banco que sube su tasa necesita saber
cuánto volumen perderá; una empresa que sube su precio, cuánta venta sacrificará. La elasticidad
responde exactamente eso.

## 📚 Objetivos

Al finalizar podrás:

1. **Calcular** elasticidad precio de la demanda por el método del punto medio.
2. **Clasificar** una demanda como elástica, inelástica o unitaria y predecir el efecto en el ingreso.
3. **Calcular** elasticidades ingreso y cruzada, e interpretar su signo.
4. **Determinar** el precio que maximiza el ingreso a partir de la elasticidad.
5. **Aplicar** la elasticidad a decisiones de precio bancario.

<!-- gen:agenda:start -->
## Agenda de 90 minutos

| Minutos | Bloque | Qué ocurre |
|---:|---|---|
| 0–10 | Activación | Pregunta diagnóstica y recuperación de la clase anterior. |
| 10–35 | Conceptos | Desarrollo guiado con la fuente oficial a la vista. |
| 35–55 | Ejemplo guiado | El docente resuelve el caso numérico paso a paso. |
| 55–80 | Práctica | El estudiante replica con datos propios o sintéticos. |
| 80–90 | Cierre | Preguntas de comprobación y registro en el portafolio. |
<!-- gen:agenda:end -->

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| `elasticidad precio` | `%Δ cantidad / %Δ precio`. Habitualmente negativa; se cita en valor absoluto. |
| `demanda elástica` | `\|E\| > 1`. La cantidad responde más que proporcionalmente. |
| `demanda inelástica` | `\|E\| < 1`. La cantidad responde menos que proporcionalmente. |
| `método del punto medio` | Usa el promedio como base, para que la elasticidad sea igual en ambos sentidos. |
| `elasticidad ingreso` | `%Δ cantidad / %Δ ingreso`. Positiva en bienes normales, negativa en inferiores. |
| `elasticidad cruzada` | `%Δ cantidad de A / %Δ precio de B`. Positiva entre sustitutos, negativa entre complementarios. |
| `ingreso total` | `precio × cantidad`. Su dirección ante un cambio de precio depende de la elasticidad. |

## 🧠 Modelo mental

La elasticidad responde una pregunta comercial concreta:

```text
si subo el precio 10 %, ¿cuánto pierdo en cantidad?

  pierdo menos de 10 %  → inelástica  → el ingreso SUBE
  pierdo exactamente 10 % → unitaria   → el ingreso NO CAMBIA
  pierdo más de 10 %    → elástica    → el ingreso BAJA
```

Esa regla —una línea— es la que decide si una subida de precio conviene, y no requiere conocer los
costos.

## 📖 Desarrollo

### 1. Cálculo por el método del punto medio

```text
        (Q₂ − Q₁) / ((Q₂ + Q₁)/2)
E = ─────────────────────────────────
        (P₂ − P₁) / ((P₂ + P₁)/2)
```

```text
precio pasa de 1 000 a 1 200; cantidad de 800 a 640

%ΔQ = (640 − 800) / 720 = −22,22 %
%ΔP = (1 200 − 1 000) / 1 100 = +18,18 %
E = −22,22 / 18,18 = −1,22  → |E| = 1,22 → ELÁSTICA
```

El método del punto medio se usa porque el método simple da resultados distintos según la dirección
del cambio, lo que es indeseable para comparar.

### 2. Elasticidad e ingreso total

| Elasticidad | Si sube el precio | Si baja el precio |
|---|---|---|
| Elástica (\|E\| > 1) | Ingreso **baja** | Ingreso **sube** |
| Unitaria (\|E\| = 1) | Ingreso igual | Ingreso igual |
| Inelástica (\|E\| < 1) | Ingreso **sube** | Ingreso **baja** |

Verificación con el ejemplo anterior:

```text
antes:   1 000 × 800 =   800 000
después: 1 200 × 640 =   768 000  → el ingreso BAJÓ, consistente con demanda elástica
```

### 3. Determinantes de la elasticidad

| Factor | Más elástica cuando |
|---|---|
| Sustitutos disponibles | Hay muchos y cercanos |
| Necesidad o lujo | Es un lujo |
| Definición del mercado | Es estrecha (un banco vs. "el crédito") |
| Horizonte de tiempo | El plazo es largo (hay tiempo de ajustarse) |
| Peso en el presupuesto | Representa una fracción grande del gasto |

El tercer factor explica una asimetría clave en banca: **la demanda por "crédito de consumo" es
inelástica; la demanda por "crédito de consumo del Banco X" es muy elástica**, porque los sustitutos
son inmediatos. Por eso la competencia por precio es intensa aunque el producto agregado responda poco
a la tasa.

### 4. Elasticidad ingreso y cruzada

```text
elasticidad ingreso = %ΔQ / %Δingreso

  > 1     bien de lujo (crece más que el ingreso)
  0 a 1   bien normal necesario
  < 0     bien inferior (baja cuando sube el ingreso)
```

```text
elasticidad cruzada = %ΔQ de A / %ΔP de B

  > 0     sustitutos (sube el precio de B, sube la demanda de A)
  < 0     complementarios (sube el precio de B, baja la demanda de A)
  ≈ 0     independientes
```

Aplicaciones bancarias:

| Par | Elasticidad cruzada esperada | Implicancia |
|---|---|---|
| Crédito de consumo del banco A y del banco B | Alta positiva | Competencia directa por precio |
| Crédito hipotecario y seguro de desgravamen | Negativa | Complementarios: se venden juntos |
| Depósito a plazo y fondo mutuo de deuda | Positiva | Sustitutos parciales |
| Tarjeta de crédito y cuenta corriente | Negativa | Complementarios |

### 5. Precio que maximiza el ingreso

```text
el ingreso total se maximiza donde |E| = 1
```

```text
demanda estimada: Q = 2 000 − 0,8 P

P = 1 000 → Q = 1 200 → ingreso 1 200 000 · E = −0,67 (inelástica)
P = 1 250 → Q = 1 000 → ingreso 1 250 000 · E = −1,00 (unitaria) ← máximo
P = 1 500 → Q =   800 → ingreso 1 200 000 · E = −1,50 (elástica)
```

Advertencia necesaria: **maximizar el ingreso no es maximizar la utilidad**. Con costos variables, el
precio óptimo es mayor que el que maximiza el ingreso, porque vender menos unidades ahorra costo. La
Parte 15, clase 7, desarrolla el precio óptimo con costos.

## 🧮 Ejemplo guiado

**Situación.** Un banco evalúa bajar la tasa de su crédito de consumo de 21,5 % a 19,0 % efectivo
anual para ganar participación. Datos de su análisis:

```text
colocaciones actuales                  48 000 millones/año
tasa actual                            21,5 %
costo de fondos                         5,8 %
costo operativo por operación           1,9 % del monto
pérdida esperada por riesgo             4,2 % del monto
elasticidad estimada de la demanda      −2,4  (mercado competitivo)
```

**Paso 1 — variación esperada de volumen.**

```text
%ΔP = (19,0 − 21,5)/((19,0 + 21,5)/2) = −2,5/20,25 = −12,35 %
%ΔQ = E × %ΔP = −2,4 × (−12,35 %) = +29,63 %
nuevas colocaciones = 48 000 × 1,2963 = 62 222 millones
```

**Paso 2 — margen por unidad, antes y después.**

```text
margen actual  = 21,5 − 5,8 − 1,9 − 4,2 = 9,6 %
margen nuevo   = 19,0 − 5,8 − 1,9 − 4,2 = 7,1 %
```

**Paso 3 — resultado total.**

```text
resultado actual = 48 000 × 0,096 = 4 608 millones
resultado nuevo  = 62 222 × 0,071 = 4 418 millones
variación                          = −190 millones  → EMPEORA
```

**Paso 4 — la elasticidad de indiferencia.**

```text
¿qué elasticidad haría indiferente la decisión?
  48 000 × 0,096 = Q × 0,071  →  Q = 64 901 millones
  %ΔQ necesario = +35,2 %
  E necesaria = 35,2 / 12,35 = 2,85
```

Con una elasticidad de 2,85 o mayor, la rebaja conviene. Con 2,4, no.

**Paso 5 — el efecto que el cálculo anterior omite.**

```text
si la rebaja atrae clientes de MAYOR riesgo (selección adversa):
  pérdida esperada sube de 4,2 % a 4,9 %
  margen nuevo = 19,0 − 5,8 − 1,9 − 4,9 = 6,4 %
  resultado = 62 222 × 0,064 = 3 982 millones → −626 millones
```

**Paso 6 — decisión y alternativa.**

```text
NO bajar la tasa de forma general

alternativa: rebaja SEGMENTADA a clientes de bajo riesgo
  segmento objetivo: 30 % de la cartera, pérdida esperada 2,1 %
  margen en ese segmento a 19,0 % = 9,2 %
  elasticidad en ese segmento (más bancarizado, más comparador) ≈ 3,2
  %ΔQ = 39,5 % sobre 14 400 millones → +5 688 millones
  resultado adicional = 5 688 × 0,092 = 523 millones  → CONVIENE
```

**Interpreta:** la pregunta "¿bajamos la tasa?" no tiene respuesta única. **Tiene una respuesta por
segmento**, porque tanto la elasticidad como la pérdida esperada difieren entre segmentos. Esa es la
lógica que conecta esta clase con la segmentación de la Parte 15, clase 6, y con el pricing basado en
riesgo de la clase 7.

## 🏦 Del cliente al banco

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| Elasticidad por segmento | Pricing diferenciado | 15, clase 7 |
| Elasticidad cruzada | Venta cruzada y paquetes de productos | 15, clase 8 |
| Selección adversa | Bajar el precio atrae peor riesgo | 9, clase 10 |
| Elasticidad de los depósitos | Sensibilidad del fondeo a la tasa | 10, clase 2 |
| Elasticidad de largo plazo | Efecto acumulado de una decisión de precio | 15, clase 7 |

## 🧪 Práctica

En `labs/lab-02.md`:

1. Calcula la elasticidad precio por el método del punto medio en seis casos.
2. Verifica la relación entre elasticidad e ingreso total en cada caso.
3. Calcula elasticidad ingreso y cruzada para cuatro pares de productos financieros.
4. Resuelve una decisión de rebaja de tasa con elasticidad de indiferencia y segmentación.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| La elasticidad cambia según la dirección | Se usó el método simple | Usa el método del punto medio. |
| Se baja el precio y el ingreso cae | Demanda inelástica | Verifica la elasticidad antes de decidir. |
| Se maximiza el ingreso y baja la utilidad | No se consideraron los costos | El precio óptimo con costos es mayor. |
| Se usa una elasticidad única para todo el mercado | Difiere por segmento | Estima por segmento. |
| Se ignora el cambio de perfil de riesgo | Selección adversa omitida | Incluye la pérdida esperada del nuevo volumen. |
| Se confunde elasticidad del producto y de la marca | Definición de mercado | La marca siempre es más elástica que la categoría. |

## ❓ Preguntas de comprobación

1. Calcula la elasticidad si el precio sube de 800 a 900 y la cantidad cae de 500 a 430.
2. ¿Qué ocurre con el ingreso total si se baja el precio de un bien inelástico?
3. ¿Por qué la demanda por el crédito de un banco específico es más elástica que la del crédito en general?
4. ¿Qué signo tiene la elasticidad cruzada entre dos sustitutos y por qué?
5. ¿Por qué el precio que maximiza el ingreso no maximiza la utilidad?

## 📥 Entregable

Guarda en `portfolio/parte-06/clase-03/`:

- seis elasticidades calculadas por el método del punto medio con su clasificación;
- la verificación de la relación entre elasticidad e ingreso total;
- las elasticidades ingreso y cruzada de cuatro pares de productos financieros;
- la decisión de rebaja de tasa resuelta con elasticidad de indiferencia y segmentación.

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

- Mankiw, N. G. (2021). *Principios de economía* (9.ª ed.). Cengage. Capítulo 5: elasticidad y sus aplicaciones.
- Krugman, P. y Wells, R. (2021). *Economics* (6.ª ed.). Worth. Capítulo 6: elasticidad y decisiones de precio.
- Nagle, T. y Müller, G. (2018). *The Strategy and Tactics of Pricing* (6.ª ed.). Routledge. Estimación y uso de la elasticidad en decisiones comerciales.
- Stiglitz, J. y Weiss, A. (1981). "Credit Rationing in Markets with Imperfect Information". *American Economic Review*. Selección adversa al variar la tasa.
- Varian, H. (2014). *Intermediate Microeconomics* (9.ª ed.). Norton. Capítulo 15: demanda de mercado y elasticidad.
- Verificación local: contrasta con estudios de competencia y de tasas del supervisor o de la autoridad de competencia de tu país, que suelen estimar elasticidades por producto.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 02 · Oferta y demanda](02-oferta-y-demanda.md) | [Parte 06](../README.md) · [Programa](../../../SYLLABUS.md) | [04 · Competencia y estructuras de mercado →](04-competencia-y-estructuras-de-mercado.md) |
<!-- gen:footer:end -->
