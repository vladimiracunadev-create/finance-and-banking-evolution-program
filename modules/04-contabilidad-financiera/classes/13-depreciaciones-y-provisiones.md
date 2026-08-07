<!-- meta
part: 5
class: 13
title: "Depreciaciones y provisiones"
level: intermedio
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 13 · Depreciaciones y provisiones

> [← 12 · Estado de flujo de efectivo](12-estado-de-flujo-de-efectivo.md) · [Índice de la parte](../README.md) · [14 · Análisis vertical y horizontal →](14-analisis-vertical-y-horizontal.md)

**Parte 05 — Contabilidad financiera** · **Nivel:** Intermedio — requiere las partes anteriores · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Analizar las dos grandes familias de estimaciones contables, que son donde el juicio de la
administración tiene mayor efecto sobre el resultado. Cambiar una vida útil o una tasa de
incobrabilidad modifica la utilidad sin que ocurra nada en el mundo real. Esta clase enseña a
calcularlas, a evaluar su razonabilidad y a ajustarlas para comparar.

Los tres estados ya están construidos. Esta clase entra en las partidas que no salen de una transacción sino de una estimación, que son las que más margen dejan y las que más se discuten. Cambiar una vida útil no mueve un peso de caja y sí mueve el resultado.

## 📚 Objetivos

Al finalizar podrás:

1. **Calcular** la depreciación por los tres métodos principales y comparar su efecto.
2. **Evaluar** la razonabilidad de una vida útil y un valor residual.
3. **Estimar** una provisión de incobrables por antigüedad y por pérdida esperada.
4. **Reconocer** el efecto de un cambio de estimación en el resultado.
5. **Ajustar** estados financieros para comparar empresas con estimaciones distintas.

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

Los tres primeros términos son la depreciación y sus supuestos; los cuatro siguientes, las provisiones y el efecto de cambiarlas. La **sensibilidad** es lo que hay que calcular siempre: saber cuánto cambia el resultado si la vida útil se mueve dos años es lo que permite juzgar si la estimación es razonable.

| Concepto | Comprensión verificable |
|---|---|
| `depreciación` | Distribución sistemática del costo de un activo a lo largo de su vida útil. No es un fondo de reposición. |
| `vida útil` | Periodo durante el cual se espera usar el activo. Es una estimación, revisable anualmente. |
| `valor residual` | Importe que se espera obtener al final de la vida útil. Reduce la base depreciable. |
| `provisión de incobrables` | Estimación de las cuentas por cobrar que no se recuperarán. |
| `pérdida esperada` | Modelo de deterioro que reconoce pérdidas antes de que ocurra el incumplimiento (NIIF 9). |
| `cambio de estimación` | Se aplica prospectivamente: afecta el periodo actual y los futuros, no los pasados. |
| `sensibilidad` | Cuánto cambia el resultado ante un cambio razonable en la estimación. |

## 🧠 Modelo mental

Una estimación contable es **una opinión con formato de número**:

```text
la máquina costó 8 000 000          → hecho, verificable con una factura
durará 5 años                       → estimación de la administración
tendrá valor residual de 800 000    → estimación de la administración
depreciación anual = 1 440 000      → consecuencia aritmética de dos opiniones
```

Cambiar la vida útil de 5 a 8 años reduce el gasto anual a 900 000 y **aumenta la utilidad en 540 000
sin que nada cambie en la máquina**. Por eso las estimaciones se revelan en notas y se comparan entre
empresas.

## 📖 Desarrollo

### 1. Métodos de depreciación

Activo de 8 000 000, vida útil 5 años, valor residual 800 000.

**Lineal:**

```text
depreciación anual = (8 000 000 − 800 000) / 5 = 1 440 000
```

**Suma de dígitos (acelerado):**

```text
suma de dígitos = 5+4+3+2+1 = 15
año 1: 7 200 000 × 5/15 = 2 400 000
año 2: 7 200 000 × 4/15 = 1 920 000
año 3: 7 200 000 × 3/15 = 1 440 000
año 4: 7 200 000 × 2/15 =   960 000
año 5: 7 200 000 × 1/15 =   480 000
```

**Unidades de producción** (capacidad estimada: 200 000 unidades):

```text
tasa = 7 200 000 / 200 000 = 36 por unidad
si el año 1 produce 55 000 unidades → 1 980 000
```

Comparación del valor en libros:

| Año | Lineal | Suma de dígitos | Diferencia |
|---:|---:|---:|---:|
| 1 | 6 560 000 | 5 600 000 | 960 000 |
| 2 | 5 120 000 | 3 680 000 | 1 440 000 |
| 3 | 3 680 000 | 2 240 000 | 1 440 000 |
| 5 | 800 000 | 800 000 | 0 |

**El total depreciado es idéntico; solo cambia la distribución en el tiempo.** Pero durante los años
intermedios, el resultado y el activo difieren de forma material.

### 2. Evaluar la razonabilidad de una vida útil

Una vida útil se compara con la del sector y con la realidad física del activo. El procedimiento siguiente la evalúa.

```text
señales de vida útil sobreestimada:
· superior a la de empresas comparables del sector
· superior a la vida técnica del activo
· se extendió justo cuando el resultado necesitaba mejorar
· los activos totalmente depreciados siguen en uso masivamente
```

Referencias orientativas:

| Activo | Vida útil habitual |
|---|---|
| Edificios | 40–60 años |
| Maquinaria industrial | 8–15 años |
| Vehículos | 5–8 años |
| Equipos computacionales | 3–5 años |
| Mobiliario | 5–10 años |
| Software | 3–5 años |

Un cambio de vida útil de equipos computacionales de 3 a 6 años **duplica el valor en libros al segundo
año** y reduce el gasto a la mitad.

### 3. Provisión de incobrables

**Método de antigüedad:**

| Tramo | Saldo | Tasa estimada | Provisión |
|---|---:|---:|---:|
| Por vencer | 3 200 000 | 0,5 % | 16 000 |
| 1–30 días | 980 000 | 2,0 % | 19 600 |
| 31–60 días | 540 000 | 8,0 % | 43 200 |
| 61–90 días | 310 000 | 25,0 % | 77 500 |
| 91–180 días | 220 000 | 50,0 % | 110 000 |
| > 180 días | 150 000 | 90,0 % | 135 000 |
| **Total** | **5 400 000** | | **401 300** |

La provisión representa el 7,4 % de la cartera. Un cambio de las tasas de un punto porcentual en cada
tramo modifica la provisión en unos 54 000 y el resultado en la misma magnitud.

**Modelo de pérdida esperada (NIIF 9):**

```text
pérdida esperada = probabilidad de incumplimiento × severidad × exposición
                 =        PD             ×      LGD      ×      EAD
```

```text
cartera 5 400 000 · PD 4,2 % · LGD 45 %
pérdida esperada = 5 400 000 × 0,042 × 0,45 = 102 060
```

La diferencia con el método de antigüedad (401 300) proviene de que este último ya incorpora la
severidad implícita en las tasas por tramo. Ambos enfoques son válidos y **deben producir resultados
comparables**; una brecha grande indica que alguna de las estimaciones no es realista. La Parte 11,
clase 2, desarrolla PD, LGD y EAD en profundidad.

### 4. Cambio de estimación

Un cambio de estimación afecta al futuro y no rehace el pasado, y esa asimetría es la que permite usarlo para gestionar el resultado. La tabla explica su tratamiento.

```text
aplicación PROSPECTIVA: afecta el periodo actual y los futuros
NO se reexpresan periodos anteriores
DEBE revelarse en notas, con su efecto cuantificado
```

Ejemplo:

```text
máquina de 8 000 000, vida útil original 5 años, valor residual 800 000
al inicio del año 3 se revisa la vida útil a 8 años totales

valor en libros al inicio del año 3 = 8 000 000 − 2×1 440 000 = 5 120 000
vida útil remanente = 8 − 2 = 6 años
nueva depreciación anual = (5 120 000 − 800 000)/6 = 720 000
efecto en el resultado del año 3: +720 000 respecto de la estimación anterior
```

Un aumento de utilidad de 720 000 sin ningún cambio operativo. Es legítimo si la revisión responde a
información nueva, y es una señal de alerta si coincide con la necesidad de cumplir un covenant.

### 5. Ajustar para comparar

Dos empresas con estimaciones distintas no son comparables hasta que se ajustan a una base común. El procedimiento siguiente lo hace.

```text
Empresa A: vida útil de maquinaria 12 años
Empresa B: vida útil de maquinaria 8 años
ambas con maquinaria de 40 000 000
```

```text
depreciación A = 40 000 000/12 = 3 333 333
depreciación B = 40 000 000/8  = 5 000 000
diferencia                       1 666 667 de mayor resultado en A
```

Para comparar, el analista **normaliza a un supuesto común**:

```text
recalcular ambas con 10 años → depreciación 4 000 000
resultado ajustado A = resultado reportado − 666 667
resultado ajustado B = resultado reportado + 1 000 000
```

Sin este ajuste, A parece más rentable que B por una decisión contable, no por desempeño.

## 🧮 Ejemplo guiado

**Situación.** Un analista revisa dos años de una empresa y detecta cambios en las estimaciones.

| | Año 1 | Año 2 |
|---|---:|---:|
| Resultado reportado | 2 100 000 | 2 780 000 |
| Depreciación | 1 850 000 | 1 240 000 |
| Provisión de incobrables (gasto) | 340 000 | 95 000 |
| Cuentas por cobrar brutas | 4 800 000 | 7 200 000 |
| Provisión acumulada | 420 000 | 380 000 |
| Propiedades y equipos (bruto) | 18 500 000 | 19 200 000 |

**Paso 1 — detecta las anomalías.**

```text
depreciación cae 33 % con activo fijo creciendo 3,8 %  → inconsistente
gasto de provisión cae 72 % con cartera creciendo 50 % → inconsistente
provisión acumulada BAJA mientras la cartera SUBE      → muy inconsistente
```

**Paso 2 — cobertura de la provisión.**

```text
año 1  420 000 / 4 800 000 = 8,75 %
año 2  380 000 / 7 200 000 = 5,28 %
```

La cobertura cayó 3,47 puntos porcentuales mientras la cartera crecía 50 %. Si la calidad de la
cartera no mejoró, la provisión está subestimada.

**Paso 3 — normaliza la provisión.**

```text
provisión al 8,75 % sobre 7 200 000 = 630 000
provisión reportada                 = 380 000
subestimación                       = 250 000
```

**Paso 4 — normaliza la depreciación.**

```text
tasa implícita año 1 = 1 850 000 / 18 500 000 = 10,0 % (vida útil ~10 años)
tasa implícita año 2 = 1 240 000 / 19 200 000 =  6,5 % (vida útil ~15,4 años)
depreciación normalizada al 10 % sobre 19 200 000 = 1 920 000
subestimación                                     =   680 000
```

**Paso 5 — resultado ajustado.**

```text
resultado reportado año 2                  2 780 000
(−) mayor provisión de incobrables          −250 000
(−) mayor depreciación                      −680 000
RESULTADO AJUSTADO                          1 850 000
```

| | Año 1 | Año 2 reportado | Año 2 ajustado |
|---|---:|---:|---:|
| Resultado | 2 100 000 | 2 780 000 | **1 850 000** |
| Variación | — | +32,4 % | **−11,9 %** |

**Paso 6 — la conclusión.**

```text
la empresa reporta un crecimiento del resultado de 32,4 %
ajustando dos estimaciones a su nivel del año anterior, el resultado CAE 11,9 %
las dos estimaciones cambiaron en la dirección que mejora el resultado, el mismo año

esto NO prueba manipulación: los cambios pueden estar justificados
lo que exige es la nota de revelación con la justificación de cada cambio
```

**Interpreta:** dos ajustes que cualquier analista puede calcular con la información publicada
convierten un crecimiento del 32 % en una caída del 12 %. Ese es el poder de las estimaciones sobre el
resultado, y la razón por la que **las notas sobre cambios de estimación son de lectura obligatoria**
antes de cualquier decisión de crédito o inversión.

## 🏦 Del cliente al banco

El cliente aplica sus estimaciones y el banco las ajusta a una base común antes de comparar. La tabla enfrenta las dos lecturas.

| Vista de la empresa | Vista del banco | Parte |
|---|---|---|
| Vida útil extendida | Ajuste del analista para comparar | 9, clase 9 |
| Provisión de incobrables baja | Posible subestimación del riesgo de cartera | 9, clase 14 |
| Cambio de estimación | Se exige la nota de justificación | 9, clase 9 |
| Modelo de pérdida esperada | Mismo marco que el banco aplica a su cartera | 11, clase 2 |
| Covenant sobre EBITDA | La depreciación no lo afecta: por eso se usa | 13, clase 10 |

## 🧪 Práctica

El laboratorio pide calcular la sensibilidad del resultado a cambios en las estimaciones. La magnitud del efecto sorprende, y es la razón por la que estas partidas se revisan primero.

En `labs/lab-06.md`, sección de estimaciones:

1. Calcula la depreciación de un activo por los tres métodos y compara valor en libros año a año.
2. Construye una provisión por antigüedad y otra por pérdida esperada; explica la diferencia.
3. Simula un cambio de vida útil y cuantifica su efecto en el resultado.
4. Ajusta dos empresas con estimaciones distintas a un supuesto común y compara.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen resultados que mejoran sin que la operación cambie. La causa es casi siempre un cambio de estimación.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se cree que la depreciación acumula un fondo | Interpretación incorrecta | Es distribución de costo, no reserva de efectivo. |
| Se comparan empresas sin ajustar vidas útiles | Estimaciones distintas | Normaliza a un supuesto común. |
| La provisión baja mientras la cartera sube | Posible subestimación | Calcula la cobertura y compárala. |
| Se reexpresan periodos anteriores por un cambio de estimación | Tratamiento incorrecto | Los cambios de estimación son prospectivos. |
| Se ignora el valor residual | Base depreciable mal calculada | `base = costo − valor residual`. |
| Un cambio de estimación no se revela | Incumplimiento de revelación | Debe informarse con su efecto cuantificado. |

## ❓ Preguntas de comprobación

1. ¿Por qué la depreciación no es un fondo de reposición?
2. Compara el efecto de la depreciación lineal y acelerada en el año 2.
3. ¿Cómo se detecta que una provisión de incobrables está subestimada?
4. ¿Cómo se aplica un cambio de estimación y por qué no se reexpresa el pasado?
5. ¿Cómo ajustarías dos empresas con vidas útiles distintas para compararlas?

## 📥 Entregable

Guarda en `portfolio/parte-05/clase-13/`:

- la depreciación de un activo por los tres métodos con la comparación de valor en libros;
- la provisión por antigüedad y por pérdida esperada, con la explicación de la diferencia;
- la simulación de un cambio de vida útil y su efecto cuantificado;
- el ajuste de dos empresas a un supuesto común con la conclusión comparativa.

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

- IFRS Foundation. *NIC 16 Propiedades, Planta y Equipo*: métodos de depreciación, vida útil y valor residual. <https://www.ifrs.org/>
- IFRS Foundation. *NIC 8 Políticas Contables, Cambios en Estimaciones Contables y Errores*: tratamiento prospectivo y revelación.
- IFRS Foundation. *NIIF 9 Instrumentos Financieros*, sección 5.5: modelo de pérdida crediticia esperada.
- IFRS Foundation. *NIC 37 Provisiones, Pasivos Contingentes y Activos Contingentes*: medición de provisiones.
- Kieso, D., Weygandt, J. y Warfield, T. (2022). *Intermediate Accounting* (18.ª ed.). Wiley. Capítulos 11 y 13: depreciación y provisiones.
- Verificación local: revisa las vidas útiles fijadas por la autoridad tributaria de tu país y su diferencia con las vidas útiles contables.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 12 · Estado de flujo de efectivo](12-estado-de-flujo-de-efectivo.md) | [Parte 05](../README.md) · [Programa](../../../SYLLABUS.md) | [14 · Análisis vertical y horizontal →](14-analisis-vertical-y-horizontal.md) |
<!-- gen:footer:end -->
