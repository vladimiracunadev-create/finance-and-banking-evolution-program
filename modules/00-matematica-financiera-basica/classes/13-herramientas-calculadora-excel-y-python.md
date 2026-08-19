<!-- meta
part: 1
class: 13
title: "Herramientas: calculadora, Excel y Python"
level: fundamento
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 13 · Herramientas: calculadora, Excel y Python

> [← 12 · Amortización básica](12-amortizacion-basica.md) · [Índice de la parte](../README.md) · [14 · Proyecto: calculadora financiera personal →](14-proyecto-calculadora-financiera-personal.md)

**Parte 01 — Matemática financiera básica** · **Nivel:** Fundamento — sin conocimientos previos · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Pasar del cálculo a mano al cálculo reproducible. Un resultado financiero que no puede volver a
obtenerse con los mismos datos no sirve para decidir ni para auditar. Esta clase enseña las tres
herramientas del oficio, cuándo usar cada una, y —lo más importante— cómo dejar por escrito los
supuestos para que otra persona llegue al mismo número.

Las doce clases anteriores resolvieron a mano para entender el mecanismo. Esta decide con qué herramienta se resuelve cuando el cálculo se repite, cambian los datos o el resultado tiene que sostenerse ante otra persona. La elección no es de gusto: depende de cuántas veces se va a ejecutar y de quién tiene que poder verificarlo.

## 📚 Objetivos

Al finalizar podrás:

1. **Resolver** los cálculos de las clases 5 a 12 en calculadora, planilla y Python.
2. **Escribir** una planilla auditable con celdas de supuestos separadas de las de cálculo.
3. **Usar** las funciones financieras estándar y conocer sus trampas de signo.
4. **Programar** funciones financieras básicas con verificación automática.
5. **Documentar** un cálculo para que sea reproducible por un tercero.

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

Los tres primeros términos son criterios de método y los tres últimos, prácticas concretas. La **separación entre supuesto y cálculo** es la que decide si un trabajo se puede auditar: una planilla en la que los números están escritos dentro de las fórmulas no es verificable por nadie, ni siquiera por quien la hizo tres meses después.

| Concepto | Comprensión verificable |
|---|---|
| `reproducibilidad` | Otra persona, con tus datos y tu documento, obtiene tu mismo número. Sin esto no hay auditoría posible. |
| `separación supuesto/cálculo` | Los datos de entrada viven en celdas propias, identificadas y de un solo color. Ninguna fórmula lleva números escritos dentro. |
| `funciones financieras` | `PAGO/PMT`, `VA/PV`, `VF/FV`, `TASA/RATE`, `NPER`, `VNA/NPV`, `TIR/IRR`. Existen en toda planilla y en `numpy-financial`. |
| `convención de signo en planillas` | `PMT` devuelve negativo porque representa una salida de caja. No es un error: es la convención. |
| `prueba unitaria` | Un caso con resultado conocido que se ejecuta automáticamente. Si falla, el cambio rompió algo. |
| `trazabilidad` | Registro de fuente, fecha y versión de cada dato usado. |

## 🧠 Modelo mental

Elige la herramienta según **cuántas veces vas a repetir el cálculo**:

```text
una vez, para decidir ahora        → calculadora
varias veces, con datos que cambian → planilla
muchas veces, con reglas y volumen  → código
```

Usar código para un cálculo único es sobreingeniería. Usar una planilla para procesar 50 000 créditos
es una fuente garantizada de errores. La Parte 14, clase 8, retoma esta frontera al hablar de
arquitectura de datos.

## 📖 Desarrollo

### 1. Calculadora: el orden correcto

Para `A = P·i/(1−(1+i)^-n)` con `P=5 000 000`, `i=0,0145`, `n=36`:

```text
1.  1,0145            [potencia] 36  [+/-]   → 0,596753
2.  1 − 0,596753                            → 0,403247
3.  5 000 000 × 0,0145                      → 72 500
4.  72 500 ÷ 0,403247                       → 179 787
```

El error clásico es calcular `(1+i)^-n` como `1/(1+i)^n` con paréntesis mal cerrados. Verifica
siempre el paso 1 de forma aislada: debe estar entre 0 y 1.

### 2. Planilla auditable

Estructura mínima obligatoria:

```text
A1  SUPUESTOS               ← bloque de entrada, fondo amarillo
A2  Capital          5000000
A3  Tasa mensual     0,0145
A4  Plazo (meses)    36
A5  Fuente tasa      "Oferta Banco X, 2026-08-01"

A7  RESULTADOS              ← bloque de cálculo, sin números escritos
A8  Cuota            =PAGO(A3;A4;-A2)
A9  Total pagado     =A8*A4
A10 Interés total    =A9-A2
A11 Control          =SI(ABS(A10-SUMA(tabla_interes))<1;"OK";"REVISAR")
```

Tres reglas que separan una planilla profesional de una casera:

1. **Ningún número dentro de una fórmula.** Si aparece `*0,0145` en una celda de cálculo, está mal.
2. **Toda entrada lleva fuente y fecha.** La celda A5 no es decoración.
3. **Existe al menos una celda de control** que se pone en rojo si algo deja de cuadrar.

Funciones equivalentes en español e inglés:

| Español | Inglés | Devuelve |
|---|---|---|
| `PAGO` | `PMT` | Cuota de un crédito |
| `VA` | `PV` | Valor presente |
| `VF` | `FV` | Valor futuro |
| `TASA` | `RATE` | Tasa periódica implícita |
| `NPER` | `NPER` | Número de periodos |
| `VNA` | `NPV` | Valor presente de flujos (¡desde el periodo 1!) |
| `TIR` | `IRR` | Tasa interna de retorno |

**Trampa de `VNA`/`NPV`:** descuenta el primer flujo un periodo. Si el flujo inicial ocurre en `t=0`,
la fórmula correcta es `=A2+VNA(tasa;rango_desde_t1)`, no `=VNA(tasa;rango_completo)`.

### 3. Python: el mismo cálculo, verificable

Este repositorio incluye las funciones en `apps/financial_calculators/calculators.py`:

```python
from calculators import fixed_payment, amortization_schedule

cuota = fixed_payment(5_000_000, 0.0145, 36)
print(round(cuota))            # 179787

tabla = amortization_schedule(5_000_000, 0.0145 * 12, 36)
print(tabla[-1].balance < 0.01)  # True → cierra en cero
```

Ejecuta las calculadoras desde la línea de comandos:

```bash
python apps/financial_calculators/cli.py compound --principal 100000 --rate 0.08 --years 5
python apps/financial_calculators/cli.py loan --principal 5000000 --annual-rate 0.174 --months 36
```

### 4. Pruebas: el control que la planilla no tiene

Una planilla puede estar mal y parecer bien indefinidamente, porque nada comprueba sus resultados. Una prueba automática sí lo hace, y el ejemplo siguiente muestra la forma mínima que tiene: un caso resuelto a mano en una clase anterior, comparado con lo que devuelve la función.

```python
def test_cuota_conocida():
    # Caso verificado a mano en la clase 11
    assert round(fixed_payment(5_000_000, 0.0145, 36)) == 179_787

def test_tabla_cierra_en_cero():
    filas = amortization_schedule(1_000_000, 0.12, 12)
    assert len(filas) == 12
    assert filas[-1].balance < 0.01

def test_tasa_cero():
    # Sin interés, la cuota es capital dividido por plazo
    assert fixed_payment(1200, 0, 12) == 100
```

Ejecuta con `pytest -q` desde la raíz del repositorio. La diferencia con una planilla es que estas
comprobaciones **se ejecutan solas cada vez que alguien cambia el código**, mientras que la celda de
control de la planilla depende de que alguien la mire.

### 5. Documentar para reproducir

Toda entrega de este programa incluye una hoja de supuestos con esta forma mínima:

```text
Cálculo:       cuota de crédito de consumo
Fecha:         2026-08-05
Capital:       5 000 000 (dato del cliente)
Tasa:          1,45 % mensual (oferta Banco X, cotización 2026-08-01, adjunta)
Plazo:         36 meses
Convención:    interés vencido, base 30/360, redondeo al peso en la cuota
Herramienta:   apps/financial_calculators/cli.py, commit a1b2c3d
Resultado:     cuota 179 787; interés total 1 472 332
Limitación:    no incluye seguros ni comisión de apertura
```

Sin la línea "Limitación", el documento afirma más de lo que calculó.

## 🧮 Ejemplo guiado

El ejemplo resuelve el mismo cálculo con las tres herramientas para que la comparación sea sobre resultados idénticos. Lo que cambia entre ellas no es el número: es cuánto cuesta repetirlo y cuánto cuesta que otra persona lo verifique.

**Situación.** Debes entregar a un comité la comparación de tres ofertas de crédito por 4 500 000 a
24 meses, y el comité pedirá reproducir tus números.

**Paso 1 — recolecta y documenta las entradas.**

| Oferta | Tasa mensual | Comisión | Seguro mensual | Fuente |
|---|---:|---:|---:|---|
| A | 1,30 % | 0 | 3 200 | Cotización 2026-08-01 |
| B | 1,15 % | 60 000 | 3 200 | Cotización 2026-08-02 |
| C | 1,45 % | 0 | 0 | Cotización 2026-08-01 |

**Paso 2 — calcula la cuota base de cada una.**

```text
A  (1,013)^24 = 1,362463 → cuota = 4 500 000×0,013×1,362463/0,362463 = 219 970
B  capital financiado 4 560 000; (1,0115)^24 = 1,315932
   cuota = 4 560 000×0,0115×1,315932/0,315932 = 218 385
C  (1,0145)^24 = 1,412974 → cuota = 4 500 000×0,0145×1,412974/0,412974 = 223 273
```

**Paso 3 — agrega el seguro y calcula el desembolso total.**

| Oferta | Cuota total | Total 24 meses | Recibido | Costo |
|---|---:|---:|---:|---:|
| A | 223 170 | 5 356 080 | 4 500 000 | 856 080 |
| B | 221 585 | 5 318 040 | 4 500 000 | 818 040 |
| C | 223 273 | 5 358 552 | 4 500 000 | 858 552 |

**Paso 4 — calcula la tasa efectiva comparable de cada una** (la que iguala 4 500 000 con el flujo
real de 24 cuotas):

```text
A  1,562 % mensual → 20,44 % efectivo anual
B  1,529 % mensual → 19,97 % efectivo anual
C  1,450 % mensual → 18,87 % efectivo anual
```

**Paso 5 — el resultado contraintuitivo.** C tiene la tasa nominal **más alta** (1,45 %) y el costo
efectivo **más bajo** (18,87 %), porque no cobra seguro. B, con la tasa nominal más baja, queda
segunda por la comisión financiada. **La tasa nominal ordenó las ofertas al revés que el costo real.**

**Paso 6 — entrega reproducible.** Adjunta: la planilla con bloque de supuestos, el script y su
salida, las tres cotizaciones con fecha, y la limitación explícita ("no considera prepago ni costo de
oportunidad del pie").

## 🏦 Del cliente al banco

El cliente usa una calculadora y el banco necesita reproducibilidad. La tabla enfrenta las dos lecturas y muestra por qué una entidad no puede sostener decisiones sobre cálculos que solo existen en la planilla de una persona.

| Nivel | Herramienta habitual | Exigencia de control |
|---|---|---|
| Persona | Calculadora o planilla simple | Guardar los supuestos |
| Ejecutivo comercial | Simulador corporativo | Cotización con fecha y vigencia |
| Analista de riesgo | Planilla auditada + SQL | Trazabilidad de fuente y versión |
| Modelador | Python/R con control de versiones | Pruebas automáticas y validación independiente del modelo |

## 🧪 Práctica

El laboratorio pide resolver el mismo caso en las tres herramientas y comparar no los resultados sino el esfuerzo de reproducirlos. Es el ejercicio que justifica el trabajo aparentemente excesivo de escribir pruebas para un cálculo que ya salió bien.

En `labs/lab-06.md`, sección de herramientas:

1. Resuelve la misma cuota en las tres herramientas y verifica que coincidan al peso.
2. Construye una planilla con bloque de supuestos, celda de control y fuente de cada dato.
3. Escribe dos pruebas nuevas en `tests/` para una función que agregues.
4. Redacta la hoja de supuestos completa de uno de tus cálculos.

## ⚠️ Errores frecuentes

Los síntomas de esta tabla aparecen semanas después de hacer el trabajo, cuando alguien pide reproducirlo. Las causas están todas en el momento de construirlo: supuestos incrustados, versiones sin control o resultados sin caso de prueba.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| `PAGO` devuelve un número negativo | Convención de signo de la planilla | Es correcto; usa `-PAGO(...)` o interpreta el signo. |
| `VNA` da un resultado desplazado | Se incluyó el flujo de `t=0` en el rango | `=flujo0+VNA(tasa;flujos_desde_t1)`. |
| Cambiar un dato no cambia el resultado | Hay números escritos dentro de fórmulas | Refactoriza: toda entrada en celda propia. |
| Dos analistas obtienen cuotas distintas | Bases o convenciones no declaradas | Documenta convención de días, redondeo y momento del pago. |
| El script funciona pero nadie sabe qué datos usó | Falta hoja de supuestos | Sin supuestos documentados el resultado no es auditable. |
| Se detecta un error semanas después | No había pruebas | Escribe una prueba por cada caso verificado a mano. |

## ❓ Preguntas de comprobación

1. ¿Por qué `PAGO` devuelve un valor negativo y qué significa ese signo?
2. ¿Cuál es la trampa de `VNA`/`NPV` y cómo se corrige?
3. Nombra las tres reglas de una planilla auditable.
4. ¿Cuándo conviene usar código en lugar de planilla?
5. ¿Qué debe contener una hoja de supuestos para que un tercero reproduzca tu cálculo?

## 📥 Entregable

Guarda en `portfolio/parte-01/clase-13/`:

- el mismo cálculo resuelto en las tres herramientas con la verificación de coincidencia;
- la planilla auditable con bloque de supuestos y celda de control;
- las dos pruebas nuevas y la salida de `pytest -q`;
- la hoja de supuestos completa de un cálculo propio.

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

- Benninga, S. (2014). *Financial Modeling* (4.ª ed.). MIT Press. Capítulos 1 a 3: construcción de modelos auditables y funciones financieras.
- Swan, J. (2015). *Practical Financial Modelling* (3.ª ed.). Elsevier. Estándares de diseño de planillas y separación de entradas y cálculos.
- Ross, S., Westerfield, R. y Jordan, B. (2022). *Fundamentos de finanzas corporativas* (12.ª ed.). McGraw-Hill. Apéndices de calculadora financiera y hoja de cálculo.
- Basel Committee on Banking Supervision (2013). *Principles for effective risk data aggregation and risk reporting (BCBS 239)* (BCBS 239). BIS. Requisitos de trazabilidad y reproducibilidad de datos de riesgo. <https://www.bis.org/publ/bcbs239.htm>
- Federal Reserve / OCC (2011). *Supervisory Guidance on Model Risk Management* (SR 11-7). Validación independiente y documentación de modelos.
- Verificación local: comprueba qué exige tu supervisor sobre documentación y validación de modelos internos antes de usarlos en decisiones de crédito.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 12 · Amortización básica](12-amortizacion-basica.md) | [Parte 01](../README.md) · [Programa](../../../SYLLABUS.md) | [14 · Proyecto: calculadora financiera personal →](14-proyecto-calculadora-financiera-personal.md) |
<!-- gen:footer:end -->
