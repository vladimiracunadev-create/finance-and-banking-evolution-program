<!-- meta
part: 1
class: 1
title: "Diagnóstico y operaciones esenciales"
level: fundamento
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 01 · Diagnóstico y operaciones esenciales

> [← Índice de la parte](../README.md) · [Índice de la parte](../README.md) · [02 · Fracciones, decimales y razones →](02-fracciones-decimales-y-razones.md)

**Parte 01 — Matemática financiera básica** · **Nivel:** Fundamento — sin conocimientos previos · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Establecer el punto de partida real de cada estudiante y fijar las cuatro operaciones sobre las que
descansa todo el programa: sumar, restar, multiplicar y dividir **con unidades y con signo**. La
mayoría de los errores caros en finanzas no son errores de álgebra avanzada; son un porcentaje
aplicado sobre la base equivocada, una tasa mensual sumada a una anual, o un signo perdido al pasar
de "me deben" a "debo". Esta clase entrena la disciplina que evita esos tres.

Esta es la primera clase del programa y no supone nada anterior. Empieza por el diagnóstico porque el resto de las trescientas cincuenta y una clases se apoyan en operaciones que casi todo el mundo cree dominar, y que casi nadie ejecuta con la disciplina que exige el dinero de otra persona. No es una clase de repaso: es la que instala el hábito de verificar.

## 📚 Objetivos

Al finalizar podrás:

1. **Medir** tu nivel de partida con un diagnóstico de 20 puntos y saber qué reforzar.
2. **Escribir** cualquier cantidad financiera con su unidad, su periodicidad y su signo.
3. **Ordenar** el orden de operaciones en expresiones financieras sin ambigüedad.
4. **Redondear** de forma trazable y explicar por qué un banco redondea distinto que una planilla.
5. **Verificar** un resultado con una comprobación independiente antes de darlo por bueno.

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

Los seis términos que siguen no son definiciones de diccionario, son los que hacen que un número financiero signifique algo. Un número solo no dice nada: `1 250 000` puede ser un ingreso o un cargo, de hoy o de dentro de un año. El que concentra más errores en todo el programa es la **convención de signo**, porque se omite tan a menudo que se vuelve invisible.

| Concepto | Comprensión verificable |
|---|---|
| `magnitud financiera` | Un número **nunca** viaja solo: lleva unidad (pesos, %, años), momento (hoy, mes 12) y signo (entrada o salida). Sin los tres, no es un dato; es una cifra huérfana. |
| `convención de signo` | Entrada de dinero positiva, salida negativa, **desde el punto de vista de quien decide**. El mismo crédito es `+` para el cliente y `−` para el banco. Declarar el punto de vista es obligatorio. |
| `orden de operaciones` | Paréntesis, potencias, multiplicación/división, suma/resta. En finanzas la potencia aparece antes de lo que uno espera: la capitalización es `(1+i)^n`, no `1+i·n`. |
| `redondeo y truncamiento` | Redondear al centavo más cercano no es lo mismo que truncar. En una cartera de 100 000 cuotas la diferencia es material y debe estar escrita en el contrato. |
| `cifras significativas` | Un resultado no puede ser más preciso que su peor dato de entrada. Una tasa estimada "más o menos 8 %" no produce una cuota de 341 287,4419 pesos. |
| `verificación independiente` | Recalcular por otro camino (estimación de orden de magnitud, planilla, código) antes de firmar. Es un control, no un lujo. |

## 🧠 Modelo mental

Piensa en cada cálculo financiero como una **oración con sujeto, verbo y complemento**:

```text
1 250 000 pesos    ·   hoy   ·   entrada
   magnitud          momento     signo
```

Si al leer tu propio cálculo en voz alta la oración no está completa, el cálculo no está terminado.
Este hábito parece trivial en la clase 1 y es exactamente lo que sostiene la conciliación bancaria
de la Parte 10 y las provisiones de la Parte 9.

## 📖 Desarrollo

### 1. El diagnóstico: saber dónde estás antes de avanzar

Resuelve el diagnóstico de `assessments/diagnostic.md` **sin calculadora en las primeras cinco
preguntas**. No es un examen: es un mapa. La interpretación es la siguiente.

| Puntaje | Lectura | Acción sugerida |
|---:|---|---|
| 0–7 | Base aritmética por consolidar | Dedica dos sesiones extra a las clases 2 y 3 antes de seguir. |
| 8–14 | Base suficiente con vacíos puntuales | Avanza normalmente y repite los laboratorios 1 y 2. |
| 15–20 | Base sólida | Avanza y usa las clases 2–4 como repaso rápido; profundiza en la clase 8. |

Un puntaje bajo aquí **no predice** el resultado final del programa. Predice cuántas veces habrá que
volver sobre las clases 5 y 6, que son las que sostienen todo lo demás.

### 2. Unidades, periodicidad y signo

El error más frecuente del programa completo aparece ya en esta clase: **mezclar periodicidades**.

```text
CORRECTO     tasa 1,5 % mensual durante 12 meses
INCORRECTO   tasa 1,5 % mensual + 18 % anual   ← no son sumables tal cual
```

Una tasa mensual y una anual son magnitudes con **base temporal distinta**. Convertirlas es el tema
de la clase 5 y de toda la Parte 7; por ahora basta la regla: si dos números no comparten unidad,
no se suman, no se restan y no se comparan.

Con el signo ocurre algo parecido. Escribe siempre desde un punto de vista declarado:

```text
Punto de vista: el cliente
  mes 0    +5 000 000    recibe el crédito
  mes 1..36  −180 760    paga la cuota
Punto de vista: el banco → los mismos números con el signo invertido
```

Cuando en la Parte 9 evalúes créditos y en la Parte 16 construyas el banco virtual, esta línea
—*punto de vista: el cliente*— será la que evite que un flujo quede sumado dos veces.

### 3. Redondeo: la decisión que sí está en el contrato

Considera una cuota calculada en `180 760,4137` pesos sobre 36 meses.

| Política | Cuota | Total 36 meses | Diferencia |
|---|---:|---:|---:|
| Redondeo al peso | 180 760 | 6 507 360 | — |
| Redondeo al alza | 180 761 | 6 507 396 | +36 |
| Truncamiento | 180 760 | 6 507 360 | 0 |

Treinta y seis pesos parecen nada. Multiplicados por 400 000 créditos vigentes son **14,4 millones**
que alguien recibe y alguien paga, y por eso la política de redondeo aparece escrita en el contrato
y auditada en la Parte 12. La regla profesional: **redondea solo al final**, nunca en pasos
intermedios, y declara la política.

### 4. Verificación independiente

Antes de aceptar un resultado, estima su orden de magnitud por otro camino:

```python
# Cálculo formal
cuota = 180_760

# Verificación grosera: 5 millones a 36 meses, sin intereses, serían 138 889/mes.
# Con intereses debe ser mayor, pero no el doble.
assert 138_889 < cuota < 277_778
```

Si la verificación grosera falla, el error está en el cálculo formal en más del 90 % de los casos.

## 🧮 Ejemplo guiado

**Situación.** Camila recibe 850 000 pesos mensuales líquidos. Paga 320 000 de arriendo, 145 000 de
alimentación, 68 000 de transporte y una cuota de 92 400. Quiere saber cuánto le queda y qué
proporción de su ingreso compromete en deuda.

**Paso 1 — escribe las magnitudes completas.**

```text
Punto de vista: Camila · periodicidad: mensual · unidad: pesos
  +850 000  ingreso líquido
  −320 000  arriendo
  −145 000  alimentación
  − 68 000  transporte
  − 92 400  cuota de crédito
```

**Paso 2 — suma respetando el signo.**

```text
850 000 − (320 000 + 145 000 + 68 000 + 92 400) = 850 000 − 625 400 = 224 600
```

**Paso 3 — calcula la proporción, cuidando la base.**

```text
carga financiera = cuota / ingreso = 92 400 / 850 000 = 0,10871 → 10,87 %
```

La base es el **ingreso**, no el gasto total. Si se dividiera por 625 400 daría 14,77 %, un número
correcto para otra pregunta y equivocado para esta. Elegir la base es la mitad del trabajo.

**Paso 4 — verifica.** 92 400 es aproximadamente un noveno de 850 000, y un noveno es 11,1 %. El
10,87 % es plausible. Resultado aceptado.

**Paso 5 — interpreta sin exagerar.** Camila tiene un excedente de 224 600 pesos y una carga
financiera de 10,87 %. Eso **no** significa que pueda tomar más deuda: falta saber si el excedente
cubre gastos irregulares, si tiene fondo de emergencia y si el ingreso es estable. Esas preguntas
son las clases 5, 7 y 2 de la Parte 2.

## 🏦 Del cliente al banco

La misma operación se ve de dos maneras según de qué lado del mostrador se esté, y las dos son correctas. Esta sección aparece en las trescientas cincuenta y dos clases del programa por una razón: el salto de cliente a profesional consiste, casi entero, en aprender a ver la segunda columna sin dejar de entender la primera.

| En la vida personal | En una mesa de trabajo bancaria |
|---|---|
| "Me queda plata a fin de mes" | Excedente mensual documentado con respaldo de ingresos |
| "Pago como un 10 % en cuotas" | Carga financiera (RCI), variable regulada del expediente de crédito |
| Redondear al peso más cercano | Política de redondeo declarada en contrato y probada en conciliación |
| Revisar el resultado "a ojo" | Control de razonabilidad documentado con evidencia archivada |

El analista de crédito de la Parte 9 hace exactamente el cálculo de Camila. La diferencia no está en
la matemática: está en que debe poder **demostrar** de dónde salió cada número.

## 🧪 Práctica

La práctica no repite el ejemplo guiado con otros números. Comprueba otra cosa: que el hábito de verificar aguanta cuando nadie está mirando el resultado. Los ejercicios del laboratorio están diseñados para que un descuido de signo o de unidad produzca un número plausible, no uno absurdo, que es exactamente como se cuelan los errores caros.

Trabaja el `labs/lab-01.md` con estos requisitos mínimos:

1. Construye tu propia tabla de magnitudes con unidad, periodicidad y signo (mínimo 8 líneas).
2. Calcula excedente y carga financiera declarando explícitamente la base de cada porcentaje.
3. Ejecuta una verificación independiente de al menos dos resultados.
4. Repite el ejercicio truncando en lugar de redondear y cuantifica la diferencia a 12 meses.

## ⚠️ Errores frecuentes

La tabla se lee de izquierda a derecha, pero se usa al revés. Cuando un resultado no cuadra, se busca el **síntoma** en la primera columna y desde ahí se llega a la causa, en vez de revisar el cálculo entero desde el principio. Casi todos los errores de esta clase producen síntomas reconocibles, y reconocerlos ahorra más tiempo que recalcular.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Dos personas obtienen porcentajes distintos con los mismos datos | Usaron bases diferentes sin declararlo | Escribe siempre `porcentaje = parte / base` con la base nombrada. |
| El total de un flujo no cuadra por unos pesos | Se redondeó en pasos intermedios | Redondea solo en la presentación final; mantén la precisión completa en el cálculo. |
| Una suma de flujos da un número absurdamente alto | Se sumaron entradas y salidas sin signo | Declara el punto de vista y aplica la convención de signo antes de sumar. |
| Se compara una tasa mensual con una anual | Se ignoró la periodicidad | Lleva ambas a la misma base temporal (clase 5 y Parte 7, clase 1). |
| El resultado tiene seis decimales sobre datos estimados | Falsa precisión | Limita las cifras significativas al peor dato de entrada. |
| Se acepta un resultado sin comprobarlo | No existe hábito de verificación | Toda cifra que salga del cuaderno lleva una comprobación de orden de magnitud. |

## ❓ Preguntas de comprobación

1. ¿Qué tres atributos debe tener toda magnitud financiera y qué falla si falta alguno?
2. ¿Por qué una tasa de 1,5 % mensual no se puede sumar a una de 18 % anual?
3. Camila quiere saber qué proporción de sus **gastos** representa la cuota. ¿Cambia el numerador, el denominador o ambos?
4. ¿En qué momento del cálculo se debe redondear y por qué la respuesta importa a escala de cartera?
5. Da un ejemplo de verificación independiente para el resultado "la cuota de 5 millones a 36 meses es 180 760".

## 📥 Entregable

Guarda en `portfolio/parte-01/clase-01/`:

- el diagnóstico resuelto con tu puntaje y tu plan de refuerzo;
- la tabla de magnitudes con unidad, periodicidad y signo;
- los dos porcentajes calculados con su base declarada;
- una nota de 150–250 palabras explicando qué cambió en tu forma de escribir un número.

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

- Ross, S., Westerfield, R. y Jordan, B. (2022). *Fundamentos de finanzas corporativas* (12.ª ed.). McGraw-Hill. Capítulo 1: notación, convención de signos y punto de vista del flujo.
- Blank, L. y Tarquin, A. (2018). *Ingeniería económica* (8.ª ed.). McGraw-Hill. Capítulo 1: terminología, unidades y diagramas de flujo de efectivo.
- Kellison, S. (2008). *The Theory of Interest* (3.ª ed.). McGraw-Hill/Irwin. Capítulo 1: magnitudes, periodicidad y la construcción del eje de tiempo.
- OECD/INFE (2022). *Toolkit for Measuring Financial Literacy and Financial Inclusion*. OCDE. Marco del diagnóstico de entrada y de los dominios de competencia.
- OECD (2020). *Recommendation on Financial Literacy*. OCDE. Definición de alfabetización financiera usada por este programa.
- Verificación local: consulta la norma de redondeo y de expresión de tasas del regulador de tu país antes de aplicar estos criterios a un contrato real.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← Índice de la parte](../README.md) | [Parte 01](../README.md) · [Programa](../../../SYLLABUS.md) | [02 · Fracciones, decimales y razones →](02-fracciones-decimales-y-razones.md) |
<!-- gen:footer:end -->
