# Ley 21.850: ejemplos, ejercicios y evaluación

Guía de trabajo del caso
[«Ley 21.850: qué cambia en el costo de capital, los dividendos y la liquidez»](../case-studies/chile/ley-21850-reconstruccion-nacional.md).
El expediente dice **qué dispone la ley y cuándo**; esta guía enseña a **calcular sus
efectos** y a distinguir, en cada cálculo, qué es texto legal, qué es supuesto del
ejercicio y qué depende de una instrucción que todavía no se conoce. La clase donde se
usa cada ejercicio está en la [matriz](ley-21850-matriz-e-itinerario.md).

> ⚖️ **Aviso.** Todas las cifras son **sintéticas** (empresa «Andes Insumos S.A.» y
> «Banco Costanera», ficticios). Solo las tasas, porcentajes y plazos de la ley son
> datos legales, y están en el expediente con su artículo. Nada de esto es asesoría
> tributaria, legal ni de inversión. Una prueba automática
> (`tests/test_ley_21850_ejercicios.py`) recalcula cada cifra de este documento.

## Cómo leer este documento

Los ejercicios siguen el mismo orden de dificultad que el resto del programa: primero un
ejemplo guiado de cada nivel, luego ejercicios básicos, intermedios y avanzados, después
preguntas abiertas y una evaluación con rúbrica. Cada ejercicio indica **el tema** (de los
once que la integración cubre), **la perspectiva** (cliente, banco, inversionista o
persona natural) y **el riesgo de interpretación** que hay que vigilar.

Las variables se definen una vez aquí y se reutilizan en todo el documento.

| Símbolo | Significado | Unidad |
|---|---|---|
| `RLI` | Renta líquida imponible de la empresa en el año | millones de pesos (MM$) |
| `t_c` | Tasa del impuesto de primera categoría del año | fracción (0,27 = 27 %) |
| `IDPC` | Impuesto de primera categoría pagado: `t_c × RLI` | MM$ |
| `t_f` | Tasa marginal de impuestos finales del accionista | fracción |
| `ρ` | Fracción del crédito que se restituye (restitución) | fracción, entre 0 y 1 |
| `D` | Dividendo bruto distribuido: `RLI − IDPC` | MM$ |
| `NOPAT` | Utilidad operacional después de impuestos: `EBIT × (1 − t_c)` | MM$ |
| `WACC` | Costo promedio ponderado del capital | fracción anual |
| `k_e`, `k_d` | Costo del patrimonio y de la deuda antes de impuestos | fracción anual |

---

## Parte A · Dos ejemplos guiados

### Ejemplo guiado 1 (introductorio): cuánto impuesto soporta una utilidad que se reparte

**Situación.** Andes Insumos obtiene una renta líquida imponible de 1.000 MM$ y reparte
todo lo que le queda después del impuesto a un accionista con tasa marginal de 40 %
**[S]**. La ley baja la tasa de primera categoría año a año y reduce la restitución del
crédito. ¿Cuánto impuesto soporta en total esa utilidad en cada año?

**Idea previa.** El impuesto se paga en dos escalones. Primero la empresa paga su impuesto
(`IDPC`). Después, cuando reparte lo que queda, el accionista paga el suyo, pero puede
descontar el impuesto que la empresa ya pagó. Lo que descuenta se llama **crédito**. Si
el crédito se descontara entero, el accionista terminaría pagando exactamente su tasa
marginal sobre la renta original: eso es la **integración plena**. Si una parte del
crédito debe devolverse (la **restitución**, `ρ`), esa parte es un costo adicional.

**Fórmula.** Cuando `t_f ≥ t_c`, la carga total sobre la utilidad distribuida es

`Carga = t_f × RLI + ρ × IDPC`  (MM$)

El primer término es lo que se paga si la integración fuera plena; el segundo, el castigo
por la restitución. Por eso, cuando `ρ` baja a cero, la carga converge a la tasa marginal
del accionista y deja de depender de la tasa de la empresa.

**Cálculo.** Se usan las tasas del expediente y las restituciones de la lectura del
quinto transitorio (**[I]**: véase el riesgo de interpretación más abajo).

| Año comercial | `t_c` | `IDPC` | `ρ` | `D` | Carga total | Carga / `RLI` |
|---:|---:|---:|---:|---:|---:|---:|
| 2026 | 27 % | 270,0 | 35 % | 730,0 | 494,5 | 49,45 % |
| 2027 | 25,5 % | 255,0 | 30 % | 745,0 | 476,5 | 47,65 % |
| 2028 | 24 % | 240,0 | 20 % | 760,0 | 448,0 | 44,80 % |
| 2029 | 23 % | 230,0 | 0 % | 770,0 | 400,0 | 40,00 % |

**Lectura.** En cuatro años la carga baja 9,45 puntos de la renta, y **toda** esa baja
proviene del término de restitución (de 94,5 a 0 MM$): el término `t_f × RLI` vale 400
MM$ en los cuatro años. La rebaja de la tasa corporativa (de 270 a 230 MM$ de `IDPC`) no
cambia lo que paga el dueño que reparte, porque el crédito aumenta o disminuye con ella.
Es el resultado que sorprende: **para quien reparte, lo que importa es la restitución,
no la tasa corporativa**. Para la empresa que retiene utilidades ocurre lo contrario: no
hay dividendo ni crédito, y la rebaja de tasa es todo el beneficio.

**Perspectiva del cliente.** Reparte antes o después según cuánto valga recibir el dinero
hoy frente al ahorro de esperar. **Perspectiva bancaria.** El banco que presta a la
empresa mira dos cosas distintas: la caja que *queda* en la empresa (`D` si reparte todo,
y toda la utilidad si no reparte) y la capacidad de los dueños de apoyarla con capital.

**Riesgo de interpretación.** El quinto transitorio habla de créditos «generados durante
el año tributario 2028» y «2029», y el año tributario sigue al comercial. Este ejemplo
asume que el crédito del año comercial 2027 tiene `ρ` de 30 % y el de 2028 de 20 %. Es
una **lectura del texto** que debe contrastarse con las instrucciones del SII, que aún no
se confirmaron.

### Ejemplo guiado 2 (profesional): rebaja de tasa, escudo fiscal y valor de la empresa

**Situación.** El banco evalúa un crédito a Andes Insumos y calcula el valor de la
empresa por flujos descontados antes y después de la rebaja de tasa. La empresa tiene un
`EBIT` de 1.000 MM$ constante **[S]**, una estructura de 600 MM$ de patrimonio y 400 MM$
de deuda **[S]**, un `k_e` de 12 % **[S]** y un `k_d` de 7 % **[S]**.

**Idea previa.** El impuesto tiene dos efectos opuestos sobre el valor. Baja el flujo que
llega a los inversionistas (efecto negativo) pero también reduce el ahorro que produce la
deuda, porque los intereses se descuentan de un impuesto que ya es menor (efecto sobre la
tasa de descuento). Al bajar la tasa corporativa, el flujo sube y el escudo fiscal baja.
¿Cuál efecto domina? Hay que calcularlo.

**Fórmulas.**

- Costo de la deuda después de impuestos: `k_d × (1 − t_c)` (fracción anual).
- Costo promedio ponderado: `WACC = (E/V) × k_e + (D/V) × k_d × (1 − t_c)`.
- Valor de una perpetuidad sin crecimiento: `V = NOPAT / WACC` (MM$).

**Cálculo.**

| Concepto | Con `t_c` = 27 % | Con `t_c` = 23 % |
|---|---:|---:|
| `k_d (1 − t_c)` | 5,110 % | 5,390 % |
| `WACC` | 9,244 % | 9,356 % |
| `NOPAT` | 730,0 | 770,0 |
| `V = NOPAT / WACC` | 7.897 | 8.230 |

**Lectura.** El `WACC` sube 0,112 puntos porque el escudo fiscal es menor, pero el
`NOPAT` sube 5,5 % y el valor sube 4,2 %. En este ejemplo **domina el flujo**. El
resultado depende de dos supuestos que conviene hacer explícitos: que `k_e` no cambia y
que la deuda mantiene su costo. El ejercicio A1 mide cuánto puede subir `k_e` antes de
que el valor deje de aumentar.

**Perspectiva del cliente.** La empresa ve su valor aumentar; el accionista, más aún si
la empresa no reparte. **Perspectiva bancaria.** El banco ve mejor cobertura de su
crédito, aunque el valor de la garantía de acciones depende del mercado, no de la
fórmula.

---

## Parte B · Once ejercicios

### Ejercicios básicos

**B1 · Flujo de caja y covenant (tema 1; cliente y banco).** Andes tiene `EBIT` de 1.000 MM$
y un servicio de deuda anual de 600 MM$ **[S]**. El convenio exige una cobertura
`NOPAT / servicio de deuda` de al menos 1,25. Calcula la cobertura entre 2026 y 2029 y
dime en qué año la empresa cumple.

*Respuesta orientadora.* `NOPAT` = 730; 745; 760; 770 → cobertura 1,217; 1,242; 1,267;
1,283. Cumple desde **2028**. El banco debería revisar el covenant: cambió solo por un
cambio de ley y no por desempeño. **Riesgo:** olvidar que el `NOPAT` no es caja libre
(falta depreciación e inversión).

**B2 · Costo de repartir (tema 2; inversionista).** Con los datos del ejemplo 1, calcula el
impuesto *adicional* que paga el accionista al recibir el dividendo (carga total menos
`IDPC`) en 2026 y en 2029.

*Respuesta orientadora.* 494,5 − 270 = **224,5** MM$ y 400 − 230 = **170** MM$. La
diferencia, 54,5 MM$, es lo que cambia el costo de repartir por la sola sucesión de leyes.
**Riesgo:** olvidar que el cálculo vale para `t_f ≥ t_c`.

**B3 · Ganancia de capital (tema 6; persona natural e inversionista).** Una persona compra
acciones de una sociedad abierta por 100 MM$ y las vende en 2027 por 160 MM$, en un caso
que cumple las condiciones del artículo 107. Antes, la ganancia pagaba un impuesto único de
10 %. Calcula la ganancia neta antes y después.

*Respuesta orientadora.* Ganancia 60; impuesto antes 6; neto antes 54; neto después 60
(**+11,1 %**). **Riesgo:** aplicar la exención a casos que no cumplen el artículo 107.

**B4 · Crédito por exportación de servicios (tema 5; cliente).** Una empresa tecnológica
chilena exporta servicios calificados como tales. Sus ingresos de exportación son 60 % de
los ingresos totales **[S]**. Un trabajador residente gana 3.000.000 de pesos mensuales
imponibles (36.000.000 al año) **[S]**. Calcula el crédito si la empresa está en la Región
Metropolitana y si está fuera de ella.

*Respuesta orientadora.* Metropolitana: 15 % × 60 % × 36.000.000 = **3.240.000**; en
regiones: 20 % × 60 % × 36.000.000 = **4.320.000**. El tope de 75 UTM equivale a 5.175.000
con una UTM supuesta de 69.000 pesos **[S]**, de modo que no limita. **Riesgo:** el texto
usa la remuneración imponible, y la base imponible tiene un tope legal; verifica si la
instrucción del SII lo aplica.

**B5 · Facilidades de pago en Tesorería (tema 8; persona natural y empresa).** Una deuda
tributaria de 100 MM$ de capital arrastra 30 MM$ de intereses y 10 MM$ de multas.
Compara el pago al contado con el máximo condonable (100 % de intereses y 80 % de multas)
con un convenio (95 % y 75 %, pie del 10 % del capital).

*Respuesta orientadora.* Contado: 100 + 0 + 2 = **102** MM$. Convenio: 100 + 1,5 + 2,5 =
**104** MM$, con pie de 10 y hasta 48 cuotas. **Riesgo:** la condonación del convenio es
condicional: un incumplimiento la revoca.

**B6 · Valor del dinero en el tiempo del convenio (tema 8; banco).** Con el convenio de B5,
las 48 cuotas mensuales iguales suman 94 MM$ después del pie. Con una tasa de descuento de
12 % anual (equivalente mensual compuesta) **[S]**, ¿cuál es el valor presente de lo que
paga el deudor?

*Respuesta orientadora.* Cuota 1,958; valor presente total **85,2** MM$ frente a 104
nominales. **Riesgo:** suponer que las cuotas se reajustan; el ejercicio las trata sin
reajuste **[S]**. El banco que refinancie esa deuda debería considerar este valor, no el
nominal.

### Ejercicios intermedios y avanzados

**A1 · Sensibilidad del costo del patrimonio (tema 3; inversionista).** Con el ejemplo 2,
¿cuánto puede subir `k_e` para que el valor con `t_c` = 23 % siga igualando al de 27 %?

*Respuesta orientadora.* El valor a igualar es 7.897; el `WACC` de equilibrio es
770 / 7.897 = 9,751 %; despejando `k_e` = (9,751 % − 0,4 × 5,39 %) / 0,6 = **12,66 %**.
El costo del patrimonio puede aumentar unos 0,66 puntos antes de que desaparezca la
ganancia de valor. **Riesgo:** olvidar que la estructura de capital también puede cambiar.

**A2 · Valor de la invariabilidad (tema 7; cliente).** Un proyecto genera 200 MM$ de renta
imponible por 10 años; la tasa corporativa es 23 %. Sin invariabilidad, se supone que con
probabilidad `p` la tasa sube a 30 % desde el año 6 **[S]**. El estatuto del artículo 26
exige un costo adicional de 1,5 puntos de tasa durante los diez años (**[D]**, dato de una
fuente secundaria; **no verificado** en el texto oficial consultado). Descuenta al 10 %.
¿Desde qué probabilidad conviene contratar la invariabilidad?

*Respuesta orientadora.* Costo de la invariabilidad: 3 × 6,1446 = 18,43 MM$. Pérdida
esperada sin ella: 14 × `p` × 2,3538 = 32,95 `p`. Equilibrio: `p*` = **55,9 %**. Con una
probabilidad menor, la invariabilidad es un seguro caro. **Riesgo:** el recargo y los
detalles del contrato deben verificarse en el texto oficial y en el reglamento.

**A3 · Banco: activos por impuesto diferido (tema 10; banco).** Banco Costanera tiene un
activo por impuesto diferido de 200 MM$ calculado con una tasa de 27 %. Su patrimonio es
1.400 MM$ y sus activos ponderados por riesgo, 10.000 MM$ **[S]**. Si la tasa esperada de
reversión fuese 23 %, ¿cuánto se reajusta ese activo y cómo cambia el índice
(patrimonio / activos ponderados)?

*Respuesta orientadora.* Nuevo activo: 200 × 23/27 = 170,4; ajuste **−29,6** MM$. Índice:
14,00 % → **13,70 %** (−0,30 puntos), si el activo no se deduce del capital. **[I]** El
tratamiento contable de un cambio de tasa (remedir a la tasa que se espera aplicar) es un
principio general de la NIC 12, **no una regla de esta ley**; verifícalo con la
normativa de la CMF antes de aplicarlo.

**A4 · Costo fiscal y escenarios (tema 11; Estado).** La recaudación del impuesto de primera
categoría es `t_c × B`, con `B` la base imponible agregada. Si la tasa baja de 27 % a
23 %, ¿en qué porcentaje debe crecer `B` para que la recaudación no cambie?

*Respuesta orientadora.* `B' / B = 27 / 23 = 1,1739`: la base debe crecer **17,4 %**. Si
crece menos, hay costo fiscal; si más, la rebaja se autofinancia. **Riesgo:** el cálculo
ignora el efecto sobre otros impuestos y sobre la evasión; es una cota, no un pronóstico.

**A5 · Impuesto único sobre saldos de utilidades (tema 9; empresa).** Una empresa tiene un
saldo distribuible de 500 MM$ con un crédito asociado de 100 MM$ **[S]**. Si lo distribuye
a un accionista con `t_f` = 40 %, el impuesto es `t_f × (500 + 100) − 100` = 140. La opción
del undécimo transitorio permite pagar 10 % sobre el saldo (50 MM$), sin derecho a los
créditos. Si la distribución habría ocurrido en tres años y se descuenta al 10 %, ¿cuánto
se ahorra en valor presente?

*Respuesta orientadora.* Ahorro nominal 90 MM$. Valor presente del impuesto ordinario:
140 / 1,331 = 105,2; opción: 50 hoy. **Ahorro en valor presente: 55,2** MM$. **Riesgo:**
la opción tiene plazo (ocho meses desde la publicación) y requiere el formulario que el
SII debe establecer; no es una elección libre.

---

## Parte C · Cinco preguntas abiertas

1. ¿Por qué el fin de la restitución puede importar más a un accionista que la rebaja de
   tasa corporativa? Responde con la fórmula del ejemplo 1.
2. Un banco recalcula el valor de sus garantías. ¿Qué datos del cliente cambian por la ley
   y cuáles no?
3. Distingue, para un crédito a una empresa exportadora de servicios, qué efecto de la ley
   es seguro, cuál es probable y cuál depende de una instrucción del SII.
4. ¿Qué diferencia hay entre la invariabilidad del artículo 26 y una promesa política de
   mantener las reglas?
5. Un cliente pregunta si debe acogerse a la opción del 10 %. ¿Qué información necesitas
   antes de responder y a quién derivas la decisión final?

## Parte D · Actividad integradora: informe de cartera para Banco Costanera

**Laboratorio con datos sintéticos.** El siguiente script genera tres empresas ficticias
y calcula su cobertura antes y después de la rebaja. Cópialo, cámbiale los supuestos y
guarda los resultados en `portfolio/ley-21850/`.

```python
EMPRESAS = {              # EBIT (MM$) y servicio de deuda anual (MM$), todo [S]
    "Andes Insumos": (1000, 600),
    "Costa Software": (400, 200),
    "Pampa Retail": (300, 250),
}
TASAS = {2026: 0.27, 2027: 0.255, 2028: 0.24, 2029: 0.23}

for nombre, (ebit, servicio) in EMPRESAS.items():
    cobertura = {a: ebit * (1 - t) / servicio for a, t in TASAS.items()}
    print(nombre, {a: round(c, 3) for a, c in cobertura.items()})
```

**Entregable.** Un informe de dos páginas con la cobertura por año de cada empresa, una
tabla de **escenarios** (rebaja completa, rebaja pausada en 24 %, ley derogada), la
identificación de qué empresas cruzan el umbral de 1,25 y una lista de **qué información
falta** (instrucciones del SII, valor de la UTM, estructura de deuda real). Debe indicar
qué parte del análisis es texto legal, cuál supuesto y cuál pendiente.

## Parte E · Evaluación

### Ponderación

| Criterio | Peso |
|---|---:|
| Distinguir texto legal, supuesto y pendiente en cada cifra | 20 % |
| Cálculo correcto con variables y unidades definidas | 30 % |
| Interpretación diferenciada por actor (empresa, banco, inversionista, persona) | 30 % |
| Riesgos y límites declarados | 20 % |

### Descriptores de desempeño

| Nivel | Qué se observa |
|---|---|
| **Sobresaliente** | Etiqueta cada dato; calcula sin errores; explica por qué cada actor se ve afectado de manera distinta; declara qué depende del SII |
| **Logrado** | Calcula con errores menores; distingue dos o tres actores; menciona los pendientes |
| **En desarrollo** | Aplica la fórmula sin interpretarla; mezcla efectos de medidas distintas |
| **Inicial** | Cita cifras sin año ni artículo; presenta la ley como completamente vigente |

### Errores de razonamiento para detectar

- Dar por vigente en 2026 lo que rige desde 2027.
- Mezclar la tasa corporativa con la carga que soporta el accionista.
- Suponer que todo ahorro tributario se traslada al valor sin tocar la tasa de descuento.
- Tratar un resumen de una firma de abogados como si fuera el texto de la ley.
- Concluir que la ley «beneficia» o «perjudica» a «los bancos» sin separar balance propio y cartera.

## Verificación

Las cifras de este documento las recalcula `tests/test_ley_21850_ejercicios.py`. Las
tasas, plazos y porcentajes de la ley se contrastaron con el texto de la BCN el
2026-11-05; las afirmaciones marcadas **[D]** provienen de una fuente secundaria y quedan
sin verificar contra el texto oficial.
