---
part: 5
class: 5
title: "Patrimonio"
level: intermedio
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 05 · Patrimonio

> [← 04 · Pasivos](04-pasivos.md) · [Índice de la parte](../README.md) · [06 · Ingresos, costos y gastos →](06-ingresos-costos-y-gastos.md)

**Parte 05 — Contabilidad financiera** · **Nivel:** Intermedio — requiere las partes anteriores · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Entender el elemento residual que concentra las decisiones más importantes de una empresa: cuánto
capital aportan los dueños, cuánto se reinvierte y cuánto se reparte. El patrimonio es también el
colchón que absorbe pérdidas, y por eso es la variable central de la regulación bancaria que se verá
en la Parte 12.

Los dos elementos anteriores son lo que se tiene y lo que se debe. Este es lo que queda, y tiene una función que ninguno de los otros dos cumple: absorber pérdidas. Esa función es la que convierte al patrimonio en el centro de la regulación bancaria de las Partes 11 y 12.

## 📚 Objetivos

Al finalizar podrás:

1. **Identificar** los componentes del patrimonio y qué representa cada uno.
2. **Construir** el estado de cambios en el patrimonio y conciliar sus movimientos.
3. **Distinguir** resultado del periodo de otro resultado integral.
4. **Evaluar** una política de dividendos y su efecto en el crecimiento sostenible.
5. **Explicar** por qué el patrimonio es el colchón frente a pérdidas.

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

Los cuatro primeros términos son los componentes del patrimonio y los tres últimos, lo que se hace con él y para qué sirve. El **colchón de absorción** es la idea que hay que retener: el patrimonio es lo que permite que una pérdida no se convierta en un impago a los acreedores.

| Concepto | Comprensión verificable |
|---|---|
| `capital emitido` | Aportes de los dueños. No es "dinero disponible": es el origen de recursos ya invertidos. |
| `prima de emisión` | Diferencia entre el precio de emisión y el valor nominal de las acciones. |
| `resultados acumulados` | Utilidades de periodos anteriores no distribuidas. Es la reinversión histórica. |
| `otro resultado integral` | Cambios de valor que no pasan por el resultado del periodo: revaluaciones, coberturas, diferencias de conversión. |
| `dividendo` | Distribución a los dueños. Reduce patrimonio y caja; no es un gasto. |
| `crecimiento sostenible` | `ROE × (1 − tasa de reparto)`. Cuánto puede crecer sin aumentar el apalancamiento ni emitir capital. |
| `colchón de absorción` | Capacidad del patrimonio de absorber pérdidas antes de comprometer a los acreedores. |

## 🧠 Modelo mental

El patrimonio es **lo último en cobrar y lo primero en perder**:

```text
si el activo cae de 100 a 80, con pasivo de 60:
  patrimonio pasa de 40 a 20   → el dueño absorbe TODA la pérdida
si el activo cae a 55:
  patrimonio = −5              → ahora el acreedor pierde
```

Esa asimetría explica dos cosas: por qué los dueños exigen mayor rentabilidad que los acreedores, y
por qué el regulador bancario exige un mínimo de patrimonio. **El patrimonio es el seguro de los
acreedores, pagado por los dueños.**

## 📖 Desarrollo

### 1. Componentes

El patrimonio no es una sola cifra sino varias con orígenes y restricciones distintas. La tabla las separa.

| Componente | Qué representa | Cómo cambia |
|---|---|---|
| Capital emitido | Aportes recibidos | Emisiones, reducciones de capital |
| Prima de emisión | Sobreprecio en emisiones | Nuevas emisiones sobre par |
| Otras reservas | Reservas legales, estatutarias, revaluación | Según normas o estatutos |
| Resultados acumulados | Utilidades retenidas históricas | Resultado del periodo, dividendos |
| Otro resultado integral acumulado | Ganancias y pérdidas no realizadas | Revaluaciones, coberturas, conversión |
| Participaciones no controladoras | Parte de filiales no poseída | Resultado atribuible, dividendos |

### 2. Estado de cambios en el patrimonio

El movimiento del patrimonio durante el año se explica en un estado propio, que es el menos leído y el que revela las decisiones de los dueños. La tabla muestra su estructura.

```text
                        Capital  Reservas  Result.Acum  ORI    TOTAL
Saldo inicial            5 000     400        3 200     150    8 750
Resultado del periodo        —       —        1 400       —    1 400
Otro resultado integral      —       —            —     220      220
Dividendos declarados        —       —         −560       —     −560
Emisión de acciones      1 000     300            —       —    1 300
Transferencia a reservas     —     140         −140       —        0
Saldo final              6 000     840        3 900     370   11 110
```

Este estado responde una pregunta que ningún otro responde: **de dónde viene el cambio del patrimonio**.
Un patrimonio que crece por emisión de acciones no es lo mismo que uno que crece por utilidades
retenidas, aunque el saldo final sea idéntico.

Control obligatorio:

```text
PN final = PN inicial + resultado + ORI + aportes − dividendos ± transferencias
11 110 = 8 750 + 1 400 + 220 + 1 300 − 560 + 0   ✔
```

### 3. Resultado del periodo y otro resultado integral

Hay resultados que pasan por la cuenta de resultados y otros que van directamente al patrimonio, y confundirlos distorsiona cualquier análisis de rentabilidad. La tabla los separa.

```text
RESULTADO DEL PERIODO      efectos realizados que pasan por el estado de resultados
                           → ventas, costos, gastos, deterioros, intereses

OTRO RESULTADO INTEGRAL    cambios de valor NO realizados, por norma expresa
                           → revaluación de propiedades
                           → coberturas de flujo de efectivo
                           → diferencias de conversión de negocios en el extranjero
                           → ciertos instrumentos de patrimonio a valor razonable
```

La suma de ambos es el **resultado integral total**. La distinción importa porque una empresa puede
mostrar utilidad del periodo positiva y resultado integral negativo, o viceversa. Un analista mira
ambos: el primero indica desempeño operativo; el segundo, cambios de valor que afectan al patrimonio.

### 4. Política de dividendos y crecimiento sostenible

Cuánto se reparte y cuánto se retiene decide cuánto puede crecer la empresa sin endeudarse más. El cálculo siguiente lo cuantifica.

```text
tasa de reparto (payout) = dividendos / utilidad
tasa de retención        = 1 − payout
crecimiento sostenible   = ROE × tasa de retención
```

| Empresa | ROE | Payout | Crecimiento sostenible |
|---|---:|---:|---:|
| A | 18 % | 20 % | 14,4 % |
| B | 18 % | 70 % | 5,4 % |
| C | 8 % | 20 % | 6,4 % |
| D | 25 % | 0 % | 25,0 % |

Lectura: si la empresa B quiere crecer 12 % anual, con un reparto del 70 % **no puede hacerlo sin
endeudarse más o emitir capital**. La política de dividendos no es una decisión independiente del plan
de crecimiento: es la misma decisión vista desde el otro lado.

### 5. El patrimonio como colchón

El patrimonio absorbe pérdidas hasta agotarse, y a partir de ahí las absorben los acreedores. El esquema muestra esa prelación, que reaparece en la Parte 12.

```text
capacidad de absorción = patrimonio / activo total
```

| Empresa | Activo | Patrimonio | Colchón | Caída de activo que la vuelve insolvente |
|---|---:|---:|---:|---:|
| Comercial | 100 | 40 | 40 % | 40 % |
| Industrial | 100 | 25 | 25 % | 25 % |
| Banco típico | 100 | 8 | 8 % | **8 %** |

La última fila explica por qué la banca está regulada de forma distinta a cualquier otro sector: con
un colchón del 8 %, una caída del valor de los activos de esa magnitud borra el patrimonio. La Parte
12, clase 1, desarrolla el requerimiento de capital regulatorio; aquí basta ver de dónde viene la
preocupación.

## 🧮 Ejemplo guiado

**Situación.** Una empresa presenta los siguientes datos de tres años. El directorio evalúa aumentar
el reparto de dividendos del 30 % al 60 %.

| | Año 1 | Año 2 | Año 3 |
|---|---:|---:|---:|
| Patrimonio inicial | 8 000 000 | 9 100 000 | 10 470 000 |
| Utilidad | 1 600 000 | 1 900 000 | 2 100 000 |
| Dividendos (30 %) | 480 000 | 570 000 | 630 000 |
| Otro resultado integral | −20 000 | 40 000 | 60 000 |
| Patrimonio final | 9 100 000 | 10 470 000 | 12 000 000 |
| Activo total | 21 000 000 | 24 800 000 | 28 500 000 |

**Paso 1 — verifica la conciliación del año 3.**

```text
10 470 000 + 2 100 000 − 630 000 + 60 000 = 12 000 000  ✔
```

**Paso 2 — calcula ROE y crecimiento sostenible.**

```text
ROE año 3 = 2 100 000 / 10 470 000 = 20,06 %
retención = 70 %
crecimiento sostenible = 0,2006 × 0,70 = 14,04 %
```

**Paso 3 — compara con el crecimiento efectivo del activo.**

```text
crecimiento del activo año 3 = (28 500 000 − 24 800 000) / 24 800 000 = 14,92 %
crecimiento sostenible                                                = 14,04 %
brecha                                                                =  0,88 pp
```

La empresa creció levemente por sobre su capacidad sostenible, financiando la diferencia con deuda:

```text
apalancamiento año 2 = (24 800 000 − 10 470 000)/10 470 000 = 1,37
apalancamiento año 3 = (28 500 000 − 12 000 000)/12 000 000 = 1,38
```

Consistente: el apalancamiento subió apenas.

**Paso 4 — simula el reparto del 60 %.**

```text
retención = 40 %
crecimiento sostenible = 0,2006 × 0,40 = 8,02 %
```

**Paso 5 — proyecta el efecto a 5 años.**

| Escenario | Crecimiento anual | Activo en 5 años | Apalancamiento si se mantiene el crecimiento del 15 % |
|---|---:|---:|---|
| Payout 30 % | 14,04 % | 55 000 000 | Estable en 1,38 |
| Payout 60 % | 8,02 % | 41 900 000 | Sube a ~1,95 |

**Paso 6 — la decisión y su costo.**

```text
si el directorio quiere repartir 60 % Y crecer 15 %:
  debe aumentar el apalancamiento de 1,38 a ~1,95
  efecto: mayor riesgo financiero, mayor costo de la deuda, menor colchón
  colchón de absorción cae de 42 % a 34 % del activo

alternativas:
  A  repartir 60 % y crecer 8 %      → sin más deuda
  B  repartir 30 % y crecer 14 %     → situación actual
  C  repartir 60 %, crecer 15 % y emitir capital por ~4 500 000
```

**Interpreta:** la pregunta "¿repartimos más dividendos?" parece independiente y no lo es. **Reparto,
crecimiento y apalancamiento son tres caras de la misma restricción**, y solo dos pueden fijarse
libremente. Presentar al directorio las tres alternativas con sus consecuencias es exactamente lo que
un analista financiero aporta, y es el mismo razonamiento que la Parte 13, clase 5, formaliza como
estructura de capital.

## 🏦 Del cliente al banco

El dueño ve su participación y el banco ve capacidad de absorción antes de que la pérdida lo alcance. La tabla enfrenta las dos lecturas.

| Vista de la empresa | Vista del banco | Parte |
|---|---|---|
| Alto reparto de dividendos | Menor capacidad de absorción; se vigila | 9, clase 9 |
| Aumento de capital | Señal positiva de compromiso de los dueños | 13, clase 5 |
| Patrimonio creciendo por retención | Crecimiento autofinanciado, menor riesgo | 9, clase 9 |
| Colchón bajo respecto del sector | Mayor prima de riesgo | 15, clase 7 |
| Patrimonio del propio banco | Capital regulatorio: base de todo el negocio | 12, clase 1 |

## 🧪 Práctica

El laboratorio pide construir el estado de cambios en el patrimonio y calcular el crecimiento sostenible. La segunda cifra suele ser menor que el crecimiento planificado, y esa brecha es lo que hay que financiar.

En `labs/lab-03.md`:

1. Construye el estado de cambios en el patrimonio de un caso y verifica su conciliación.
2. Separa resultado del periodo y otro resultado integral en un estado financiero real.
3. Calcula ROE, tasa de retención y crecimiento sostenible de tres empresas.
4. Simula dos políticas de dividendos y su efecto sobre el apalancamiento a cinco años.

## ⚠️ Errores frecuentes

Los síntomas de la tabla se refieren a patrimonios que no evolucionan como el resultado sugería. Las causas están en el otro resultado integral y en los dividendos.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se trata el capital como dinero disponible | Confusión conceptual | El capital es origen de recursos ya invertidos. |
| El dividendo se registra como gasto | Elemento equivocado | Es una distribución: reduce patrimonio, no resultado. |
| Se ignora el otro resultado integral | Solo se mira la utilidad | El resultado integral total explica el cambio patrimonial. |
| Se fija reparto y crecimiento sin verificar | Restricción no considerada | Solo dos de las tres variables son libres. |
| No se concilia el patrimonio | Falta el estado de cambios | Aplica el control de conciliación. |
| Se compara patrimonio entre sectores | Colchones estructuralmente distintos | Compara dentro del sector. |

## ❓ Preguntas de comprobación

1. ¿Por qué el patrimonio se dice "residual" y qué implica ante una pérdida?
2. ¿Qué diferencia hay entre resultado del periodo y otro resultado integral?
3. Calcula el crecimiento sostenible de una empresa con ROE 15 % y payout 40 %.
4. ¿Por qué reparto, crecimiento y apalancamiento no son decisiones independientes?
5. ¿Por qué el colchón de un banco es mucho menor que el de una empresa comercial?

## 📥 Entregable

Guarda en `portfolio/parte-05/clase-05/`:

- el estado de cambios en el patrimonio construido y conciliado;
- la separación de resultado del periodo y otro resultado integral de un caso real;
- el cálculo de crecimiento sostenible de tres empresas;
- la simulación de dos políticas de dividendos con su efecto en apalancamiento a cinco años.

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

- IFRS Foundation. *NIC 1 Presentación de Estados Financieros*: estado de cambios en el patrimonio y otro resultado integral. <https://www.ifrs.org/>
- IFRS Foundation (2018). *Marco Conceptual para la Información Financiera*, capítulo 4: definición de patrimonio.
- Kieso, D., Weygandt, J. y Warfield, T. (2022). *Intermediate Accounting* (18.ª ed.). Wiley. Capítulos 15 y 16: patrimonio y resultado integral.
- Higgins, R. (2019). *Analysis for Financial Management* (12.ª ed.). McGraw-Hill. Capítulo 4: crecimiento sostenible y su restricción.
- Brealey, R., Myers, S. y Allen, F. (2023). *Principios de finanzas corporativas* (14.ª ed.). McGraw-Hill. Capítulo 16: política de dividendos.
- Verificación local: revisa las reservas legales obligatorias y las restricciones a la distribución de utilidades vigentes en la legislación de sociedades de tu país.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 04 · Pasivos](04-pasivos.md) | [Parte 05](../README.md) · [Programa](../../../SYLLABUS.md) | [06 · Ingresos, costos y gastos →](06-ingresos-costos-y-gastos.md) |
<!-- gen:footer:end -->
