---
part: 8
class: 13
title: "Costos, impuestos y sesgos"
level: intermedio
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 13 · Costos, impuestos y sesgos

> [← 12 · Análisis técnico: introducción crítica](12-analisis-tecnico-introductorio.md) · [Índice de la parte](../README.md) · [14 · Seguimiento y rebalanceo →](14-seguimiento-y-rebalanceo.md)

**Parte 08 — Inversiones y mercados** · **Nivel:** Intermedio — requiere las partes anteriores · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Cuantificar las tres fuerzas que separan el rendimiento de un instrumento del rendimiento que el
inversionista efectivamente obtiene. Los costos y los impuestos son ciertos y calculables; los sesgos
de conducta son el mayor de los tres y el menos medido. Esta clase los mide y entrega contramedidas
concretas.

Las clases anteriores buscan rentabilidad. Esta se ocupa de lo que se la lleva, y su hallazgo es que las tres causas principales no son de mercado: son costos, impuestos y comportamiento propio. Los tres se pueden reducir con decisiones concretas y ninguno depende de acertar con el instrumento.

## 📚 Objetivos

Al finalizar podrás:

1. **Inventariar** y cuantificar todos los costos explícitos e implícitos.
2. **Calcular** el efecto tributario de una decisión de inversión.
3. **Medir** la brecha entre el rendimiento del fondo y el del inversionista.
4. **Identificar** los sesgos que más destruyen rentabilidad.
5. **Diseñar** contramedidas mecánicas para cada sesgo.

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

Los dos primeros términos son las clases de costo; los cuatro siguientes, el efecto del comportamiento y su corrección. La **brecha del inversionista** es la cifra que resume el problema: la diferencia entre lo que rindió un fondo y lo que ganaron sus partícipes, causada por entrar y salir en los peores momentos.

| Concepto | Comprensión verificable |
|---|---|
| `costo explícito` | Comisión de administración, corretaje, custodia. Aparece en documentos. |
| `costo implícito` | Diferencial compra-venta, impacto de mercado, retorno de rolado. No aparece. |
| `brecha del inversionista` | Diferencia entre el rendimiento del fondo y el que obtuvo el partícipe promedio. |
| `diferimiento tributario` | Postergar el impuesto permite que el monto no pagado siga rindiendo. |
| `sesgo` | Desviación sistemática del juicio que produce decisiones peores. |
| `contramedida mecánica` | Regla automática que no depende de la voluntad en el momento. |

## 🧠 Modelo mental

Tu rendimiento efectivo es el del mercado **menos tres deducciones**:

```text
rendimiento del mercado         8,0 %
− costos                       −0,9 %
− impuestos                    −0,8 %
− brecha de conducta           −1,6 %   ← la mayor, y la menos medida
= rendimiento del inversionista 4,7 %
```

Las tres se pueden reducir. La primera con selección de instrumentos, la segunda con estructura y
horizonte, y la tercera con **reglas mecánicas**, no con fuerza de voluntad.

## 📖 Desarrollo

### 1. Inventario completo de costos

Los costos visibles son una parte pequeña del total. La tabla recoge el inventario completo.

| Costo | Tipo | Magnitud típica anual | Dónde aparece |
|---|---|---:|---|
| Comisión de administración | Explícito | 0,05 %–3,5 % | Ficha del fondo |
| Comisión de corretaje | Explícito | 0,10 %–0,50 % por operación | Confirmación |
| Custodia | Explícito | 0 %–0,20 % | Contrato |
| Diferencial compra-venta | Implícito | 0,02 %–1,0 % por operación | No aparece |
| Impacto de mercado | Implícito | Variable, alto en órdenes grandes | No aparece |
| Error de seguimiento | Implícito | 0,02 %–0,40 % | Comparación con índice |
| Rotación de cartera del fondo | Implícito | 0,10 %–1,0 % | Se estima de la rotación |
| Conversión de moneda | Explícito | 0,20 %–1,0 % por operación | Confirmación |
| Retrocesión no informada | Implícito | 0,20 %–1,0 % | Debe consultarse |

```text
ejemplo de cartera con costos "bajos":
  comisión de fondos         0,42 %
  corretaje (2 operaciones)  0,18 %
  diferencial                0,08 %
  rotación de los fondos     0,25 %
  conversión de moneda       0,12 %
  COSTO TOTAL REAL           1,05 %  ← más del doble de la comisión publicada
```

### 2. Efecto tributario

El régimen varía por país; el **mecanismo** es universal:

```text
diferir el impuesto permite que el monto no pagado siga rindiendo
```

```text
inversión de 20 000 000, rendimiento 8 % anual, impuesto 20 % sobre la ganancia

ESTRATEGIA A: realizar la ganancia cada año y reinvertir lo que queda
  rendimiento neto anual = 8 % × 0,80 = 6,4 %
  a 20 años: 20 000 000 × 1,064^20 = 68 900 000

ESTRATEGIA B: mantener y realizar al final
  a 20 años bruto: 20 000 000 × 1,08^20 = 93 219 000
  ganancia = 73 219 000 · impuesto = 14 644 000
  neto = 78 575 000

DIFERENCIA: 9 675 000 (14,0 % más) por diferir
```

**El diferimiento vale más cuanto mayor el horizonte y la tasa.** Es la razón por la que la rotación
excesiva de una cartera es doblemente cara: costos de transacción y adelantamiento del impuesto.

Otras consideraciones tributarias con efecto material:

```text
· realización de pérdidas para compensar ganancias (donde el régimen lo permite)
· tratamiento distinto de dividendos y de ganancias de capital
· regímenes de ahorro previsional con beneficio tributario (Parte 3, clase 11)
· tributación de instrumentos extranjeros y obligaciones de declaración
```

### 3. La brecha del inversionista

La brecha se mide y es persistente entre mercados y periodos. El procedimiento siguiente la calcula.

```text
brecha = rendimiento del fondo − rendimiento del inversionista promedio en ese fondo
```

La brecha existe porque los aportes y rescates no son uniformes: **entra más dinero después de las
subidas y sale después de las caídas**.

```text
ejemplo simplificado:
  año 1: fondo rinde +30 % · el inversionista tiene 10 000 000 invertidos
  fin de año 1: aporta 20 000 000 más (entusiasmo)
  año 2: fondo rinde −20 % · pierde sobre 33 000 000
  fin de año 2: rescata 15 000 000 (miedo)
  año 3: fondo rinde +25 % · gana solo sobre 11 400 000

  rendimiento del fondo en 3 años: 30 % × 0,80 × 1,25 → +30,0 %
  rendimiento del inversionista: significativamente menor
```

Estudios de la industria estiman esta brecha en rangos que van desde menos de un punto hasta varios
puntos porcentuales anuales según el periodo, el tipo de fondo y la metodología. **La conclusión
cualitativa es robusta aunque la magnitud se discuta:** la conducta reduce el rendimiento efectivo.

### 4. Los sesgos que más cuestan

Los sesgos que más dinero cuestan están identificados y cuantificados. La tabla los recoge con su contramedida mecánica.

| Sesgo | Descripción | Costo estimado |
|---|---|---|
| **Sobrerreacción** | Comprar tras subidas, vender tras caídas | El mayor componente de la brecha |
| Exceso de confianza | Operar demasiado | Costos de transacción y peores decisiones |
| Aversión a la pérdida | Mantener perdedores, vender ganadores | Efecto tributario adverso y peor selección |
| Sesgo doméstico | Concentrar en el mercado local | Menor diversificación |
| Anclaje | Fijarse en el precio de compra | Decisiones basadas en un dato irrelevante |
| Contabilidad mental | Tratar el dinero distinto según su origen | Asignación subóptima |
| Descuento hiperbólico | Preferir lo inmediato de forma inconsistente | Menor ahorro |
| Sesgo de confirmación | Buscar información que apoye la posición | Persistencia en el error |

**La aversión a la pérdida** merece detalle por su efecto tributario:

```text
el inversionista tiende a vender los que subieron (realiza la ganancia y paga impuesto)
y mantener los que bajaron (no realiza la pérdida ni la compensación)

el comportamiento óptimo desde lo tributario es exactamente el contrario:
  realizar pérdidas para compensar, y diferir ganancias
```

### 5. Contramedidas mecánicas

**La regla:** una contramedida que depende de decidir bien en el momento **no es una contramedida**.

| Sesgo | Contramedida mecánica |
|---|---|
| Sobrerreacción | Aporte automático de monto fijo, en fecha fija |
| Exceso de confianza | Límite escrito de operaciones al año |
| Aversión a la pérdida | Regla de rebalanceo por bandas, que fuerza vender lo que subió |
| Sesgo doméstico | Asignación objetivo por región, con límite máximo local |
| Anclaje | Prohibición escrita de usar el precio de compra como criterio |
| Contabilidad mental | Una sola política para todo el patrimonio |
| Descuento hiperbólico | Transferencia automática el día del ingreso |
| Sesgo de confirmación | Escribir la tesis contraria antes de decidir |

```text
la contramedida más potente y más simple:
  APORTE AUTOMÁTICO DE MONTO FIJO EN FECHA FIJA

  elimina la decisión de cuándo entrar
  compra más unidades cuando el precio es bajo y menos cuando es alto
  no requiere ninguna voluntad en el momento
```

## 🧮 Ejemplo guiado

El ejemplo calcula el costo total de una cartera y estima la brecha del inversionista. Conviene sumar las tres fuentes: por separado ninguna parece grande.

**Situación.** Se analiza el historial real de un inversionista durante 10 años.

```text
DATOS
  aportes totales                     48 000 000
  patrimonio final                    71 400 000
  rendimiento del índice de referencia   8,9 % anual
```

**Paso 1 — calcula el rendimiento efectivo del inversionista.**

```text
la tasa que iguala los aportes con el patrimonio final (TIR de los flujos)
resultado: 5,1 % anual
brecha contra el índice: 3,8 puntos anuales
```

**Paso 2 — descompón la brecha.**

```text
costos (calculados de sus estados de cuenta):
  comisiones de fondos       0,94 %
  corretaje                  0,31 %
  diferenciales estimados    0,14 %
  conversión de moneda       0,08 %
  SUBTOTAL COSTOS            1,47 %

impuestos:
  realizó ganancias 14 veces en 10 años
  efecto estimado del adelantamiento tributario  0,62 %
  SUBTOTAL IMPUESTOS         0,62 %

RESIDUO (conducta) = 3,80 − 1,47 − 0,62 = 1,71 %
```

**Paso 3 — verifica el residuo con el historial de operaciones.**

```text
fechas de sus mayores aportes:
  3 de los 5 mayores aportes ocurrieron en los 2 meses siguientes
  a un alza del índice superior al 10 %

fechas de sus mayores rescates:
  4 de los 5 mayores rescates ocurrieron en los 3 meses siguientes
  a una caída superior al 12 %
```

**El patrón confirma la sobrerreacción.** El residuo de 1,71 puntos no era ruido: era conducta.

**Paso 4 — cuantifica el costo acumulado.**

```text
con rendimiento de 8,9 %: patrimonio a 10 años = 82 700 000
con rendimiento de 5,1 %: patrimonio a 10 años = 71 400 000
DIFERENCIA: 11 300 000 (23,5 % de los aportes totales)

descomposición de los 11 300 000:
  costos       4 370 000
  impuestos    1 840 000
  conducta     5 090 000  ← el mayor componente
```

**Paso 5 — diseña las contramedidas.**

| Fuente | Costo anual | Contramedida | Ahorro estimado |
|---|---:|---|---:|
| Comisiones de fondos | 0,94 % | Migrar a fondos indexados o series institucionales | 0,60 % |
| Corretaje y diferenciales | 0,45 % | Reducir operaciones de 14 a 2 al año | 0,32 % |
| Conversión de moneda | 0,08 % | Consolidar operaciones cambiarias | 0,04 % |
| Adelantamiento tributario | 0,62 % | Mantener posiciones; realizar pérdidas para compensar | 0,45 % |
| Conducta | 1,71 % | Aporte automático + rebalanceo por bandas + política escrita | 1,20 % |
| **TOTAL** | **3,80 %** | | **2,61 %** |

**Paso 6 — proyecta el efecto de las contramedidas.**

```text
rendimiento efectivo esperado: 5,1 % + 2,61 % = 7,71 %

patrimonio a 20 años con aportes de 400 000 mensuales:
  a 5,10 %: 172 800 000
  a 7,71 %: 233 900 000
  DIFERENCIA: 61 100 000
```

**Paso 7 — la contramedida que hace la mayor parte del trabajo.**

```text
de las cinco contramedidas, la de mayor efecto es la más simple:

  transferencia automática de 400 000 el día 3 de cada mes,
  distribuida según la asignación objetivo, sin excepciones

  · elimina la decisión de cuándo entrar (el mayor componente de la brecha)
  · no requiere voluntad
  · toma 15 minutos configurarla una vez
```

**Interpreta:** el inversionista perdió 11,3 millones en 10 años, **y el 45 % de esa pérdida provino de
su conducta, no de costos ni de impuestos**. La contramedida más efectiva no fue elegir mejores
instrumentos: fue **eliminar la decisión de cuándo aportar**, que es la que estaba tomando mal de
forma sistemática.

## 🏦 Del cliente al banco

El cliente busca rentabilidad y el banco genera ingresos por operación y por saldo. La tabla enfrenta las dos lecturas.

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| Costos implícitos | Transparencia exigida en la asesoría | 12, clase 4 |
| Retrocesiones | Conflicto de interés a revelar | 12, clase 3 |
| Brecha del inversionista | Argumento de la asesoría de valor | 15, clase 9 |
| Contramedidas mecánicas | Diseño de productos de aporte programado | 15, clase 8 |
| Efecto tributario | Estructuración patrimonial | 13, clase 5 |

## 🧪 Práctica

El laboratorio pide calcular el costo total de propiedad de una cartera a diez años y diseñar contramedidas mecánicas para dos sesgos. Las contramedidas tienen que ser automáticas, no propósitos.

En `labs/lab-06.md`, sección de costos y conducta:

1. Inventaría y cuantifica todos los costos de tu cartera, explícitos e implícitos.
2. Calcula el efecto del diferimiento tributario en dos estrategias a 20 años.
3. Calcula tu rendimiento efectivo y compáralo con el índice para medir tu brecha.
4. Diseña una contramedida mecánica para cada uno de los tres sesgos que más te afecten.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen carteras que rinden menos que sus instrumentos. La causa está en los costos y en el comportamiento, no en el mercado.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se compara solo la comisión publicada | Costos implícitos ignorados | Inventaría los nueve tipos de costo. |
| Se rota la cartera con frecuencia | Costos y adelantamiento tributario | Reduce operaciones; mide el costo total. |
| Se aporta después de las subidas | Sobrerreacción | Aporte automático de monto fijo. |
| Se venden los ganadores y se mantienen los perdedores | Aversión a la pérdida | Rebalanceo por bandas, mecánico. |
| Se confía en la disciplina personal | Las contramedidas no mecánicas fallan | Automatiza; no dependas de decidir bien en el momento. |
| No se mide el rendimiento propio | Brecha desconocida | Calcula la TIR de tus flujos. |

## ❓ Preguntas de comprobación

1. Nombra cinco costos implícitos que no aparecen en la comisión publicada.
2. ¿Cuánto vale diferir el impuesto en un horizonte de 20 años?
3. ¿Qué es la brecha del inversionista y por qué existe?
4. ¿Por qué el comportamiento tributariamente óptimo es contrario a la aversión a la pérdida?
5. ¿Qué distingue una contramedida mecánica de una intención?

## 📥 Entregable

Guarda en `portfolio/parte-08/clase-13/`:

- el inventario cuantificado de todos los costos de tu cartera;
- el cálculo del efecto del diferimiento tributario en dos estrategias;
- tu rendimiento efectivo calculado y tu brecha contra el índice;
- las contramedidas mecánicas diseñadas para tus tres sesgos principales.

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

- Barber, B. y Odean, T. (2000). "Trading Is Hazardous to Your Wealth". *Journal of Finance*. Efecto de la rotación sobre el rendimiento del inversionista.
- Kahneman, D. (2011). *Pensar rápido, pensar despacio*. Debate. Aversión a la pérdida y sesgos de decisión.
- Thaler, R. (2015). *Misbehaving*. Norton. Contabilidad mental y su efecto en decisiones financieras.
- Dalbar. *Quantitative Analysis of Investor Behavior* (informe anual). Medición de la brecha del inversionista.
- Bogle, J. (2017). *The Little Book of Common Sense Investing*. Wiley. Efecto acumulado de costos e impuestos.
- Verificación local: revisa el régimen tributario aplicable a ganancias de capital, dividendos e intereses en tu país, y sus obligaciones de declaración.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 12 · Análisis técnico: introducción crítica](12-analisis-tecnico-introductorio.md) | [Parte 08](../README.md) · [Programa](../../../SYLLABUS.md) | [14 · Seguimiento y rebalanceo →](14-seguimiento-y-rebalanceo.md) |
<!-- gen:footer:end -->
