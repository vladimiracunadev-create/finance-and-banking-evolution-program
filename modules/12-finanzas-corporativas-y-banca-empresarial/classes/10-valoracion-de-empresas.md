<!-- meta
part: 13
class: 10
title: "Valoración de empresas"
level: profesional
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 10 · Valoración de empresas

> [← 09 · Financiamiento de proyectos](09-financiamiento-de-proyectos.md) · [Índice de la parte](../README.md) · [11 · Fusiones y adquisiciones →](11-fusiones-y-adquisiciones.md)

**Parte 13 — Finanzas corporativas y banca empresarial** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Estimar cuánto vale una empresa y entender por qué dos valoraciones competentes del mismo negocio dan
resultados distintos. Un banco necesita valorar para financiar adquisiciones, evaluar garantías
accionarias, asesorar en ventas y estimar la recuperación en una reestructuración.

Las clases anteriores prestan a empresas. Esta las valora, que es la base de las dos siguientes. Y su enseñanza principal no es el método sino la honestidad del resultado: una valoración es un rango que depende de supuestos declarados, y presentarla como una cifra exacta es la forma más común de perder credibilidad.

## 📚 Objetivos

Al finalizar podrás:

1. **Aplicar** los tres enfoques de valoración y saber cuándo usa cada uno.
2. **Construir** una valoración por flujos descontados con su valor terminal.
3. **Usar** múltiplos comparables corrigiendo sus distorsiones.
4. **Distinguir** valor de empresa de valor del patrimonio.
5. **Interpretar** un rango de valoración y sus fuentes de variación.

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

Los cuatro primeros términos son las medidas de valor; los cuatro siguientes, los ajustes que las separan. La distinción entre **valor de empresa y valor del patrimonio** es la que más errores produce: uno incluye la deuda y el otro no, y compararlos entre sí no tiene sentido.

| Concepto | Comprensión verificable |
|---|---|
| `valor de empresa` | Valor de la operación, independiente de cómo se financia. |
| `valor del patrimonio` | Valor de empresa menos deuda neta. |
| `flujo de caja libre` | Flujo disponible para todos los proveedores de capital. |
| `valor terminal` | Valor de los flujos posteriores al horizonte explícito. |
| `múltiplo` | Razón entre valor y una magnitud financiera. |
| `prima de control` | Sobreprecio por adquirir el control. |
| `descuento por iliquidez` | Menor valor por no poder vender fácilmente. |
| `sinergia` | Valor adicional que solo existe con la combinación. |

## 🧠 Modelo mental

El modelo mental son tres enfoques que deberían converger y no lo hacen: flujos, múltiplos y valor de los activos dan cifras distintas sobre la misma empresa. La convergencia no es el objetivo; entender por qué difieren sí lo es.

```text
UNA VALORACIÓN NO ES UN NÚMERO: ES UN RANGO
Y EL RANGO REVELA MÁS QUE EL PUNTO MEDIO

  si el rango es estrecho: el valor depende poco de los supuestos
  si es amplio: el valor depende de cosas inciertas
                → identifica CUÁLES y negocia sobre ellas

EL VALOR TAMBIÉN DEPENDE DE QUIÉN VALORA
  valor para el dueño actual     ≠
  valor para un comprador financiero  ≠
  valor para un comprador estratégico (con sinergias)  ≠
  valor de liquidación
```

## 📖 Desarrollo

### 1. Los tres enfoques

Los tres enfoques miran la misma empresa desde ángulos distintos. La tabla los compara con sus supuestos.

| Enfoque | Pregunta | Cuándo se usa |
|---|---|---|
| Ingresos (flujos descontados) | ¿Cuánto generará? | Empresa en marcha con flujo proyectable |
| Mercado (múltiplos) | ¿Cuánto pagan por negocios similares? | Existen comparables observables |
| Activos (valor patrimonial ajustado) | ¿Cuánto valen sus bienes? | Empresa sin flujo, holding, liquidación |

```text
NO SON ALTERNATIVOS: SON TRIANGULACIÓN
  un valor por flujos muy distinto del de múltiplos
  no significa que uno esté mal:
  significa que hay algo que explicar
```

### 2. Flujos descontados

El método de flujos exige proyección, tasa y valor terminal, y este último suele ser la mayor parte del resultado. El procedimiento siguiente lo construye.

```text
FLUJO DE CAJA LIBRE DE LA EMPRESA
  resultado operacional × (1 − t)
  + depreciación y amortización
  − inversión en activo fijo
  − aumento de capital de trabajo
  = FLUJO DE CAJA LIBRE

VALOR DE EMPRESA = Σ  flujo_t / (1+WACC)^t  +  valor terminal / (1+WACC)^n
```

```text
VALOR TERMINAL — dos métodos
  CRECIMIENTO PERPETUO
    VT = flujo_(n+1) / (WACC − g)
    g NO puede superar el crecimiento de largo plazo de la economía

  MÚLTIPLO DE SALIDA
    VT = magnitud_n × múltiplo comparable
```

```text
EL VALOR TERMINAL SUELE SER EL 60-80 % DEL VALOR TOTAL

  consecuencia: la mayor parte del valor depende
  de dos supuestos —la tasa de descuento y g—
  y no del detalle de las proyecciones explícitas

  invertir cinco días en afinar el año 3
  y cinco minutos en elegir g es un error de asignación de esfuerzo
```

### 3. Múltiplos

Los múltiplos valoran por comparación y su dificultad está en elegir los comparables. La tabla recoge los criterios.

| Múltiplo | Numerador | Denominador | Cuándo usarlo |
|---|---|---|---|
| VE / resultado operativo antes de depreciación | Valor de empresa | Magnitud operativa | El más usado; comparable entre estructuras |
| VE / ventas | Valor de empresa | Ventas | Empresas sin resultado positivo |
| Precio / utilidad | Valor patrimonial | Utilidad neta | Empresas cotizadas comparables |
| Precio / valor libro | Valor patrimonial | Patrimonio contable | Bancos y financieras |
| VE / métrica operativa | Valor de empresa | Unidades, suscriptores, capacidad | Sectores específicos |

```text
CUIDADO CON LA CONSISTENCIA
  numerador de EMPRESA con denominador ANTES de intereses
  numerador de PATRIMONIO con denominador DESPUÉS de intereses

  mezclarlos (precio/resultado operativo) no significa nada
```

```text
AJUSTES OBLIGATORIOS AL USAR COMPARABLES
  · tamaño: las empresas grandes cotizan a múltiplos mayores
  · crecimiento: mayor crecimiento, mayor múltiplo
  · rentabilidad: mayor margen, mayor múltiplo
  · riesgo: mayor riesgo, menor múltiplo
  · liquidez: empresa no cotizada, descuento del 15-30 %
  · control: la transacción de control incluye prima del 20-40 %
```

### 4. De valor de empresa a valor del patrimonio

El paso de uno a otro exige ajustes concretos. El procedimiento los recoge.

```text
VALOR DE EMPRESA
  − deuda financiera
  + caja y equivalentes no operativos
  − pasivos asimilables a deuda
    (déficit de pensiones, contingencias, arrendamientos)
  − participaciones no controladoras
  + activos no operativos (inmuebles no usados, inversiones)
  = VALOR DEL PATRIMONIO
```

Cada uno de esos ajustes es una partida que las dos partes calculan de forma distinta, y ahí es donde se concentran las discusiones.

```text
LOS AJUSTES SON DONDE SE PIERDEN LAS NEGOCIACIONES
  · caja "operativa" vs. caja excedente: quién se la lleva
  · contingencias fiscales o laborales no provisionadas
  · deuda con partes relacionadas
  · capital de trabajo normalizado al cierre
```

### 5. Rango y sensibilidad

El resultado se presenta como rango con su sensibilidad declarada. La tabla recoge el formato.

```text
CONSTRUYE SIEMPRE UNA MATRIZ DE SENSIBILIDAD

              WACC
        12,5 %  13,0 %  13,5 %  14,0 %  14,5 %
  g 1,5 %  x       x       x       x       x
  g 2,0 %  x       x       x       x       x
  g 2,5 %  x       x       x       x       x
  g 3,0 %  x       x       x       x       x

y presenta el RANGO, no el punto
```

## 🧮 Ejemplo guiado

El ejemplo valora una empresa por los tres enfoques y explica la dispersión. Conviene mirar el peso del valor terminal: suele superar la mitad del total.

**Situación.** Un banco asesora la venta de una empresa mediana y debe estimar su valor.

```text
LA EMPRESA
  ventas año actual                        22 400
  resultado operacional                     3 592
  depreciación                                380
  inversión de mantenimiento                  420
  capital de trabajo actual                 6 856
  deuda financiera                          6 500
  caja                                        210
  tasa de impuesto                             27 %
  WACC estimado                              13,6 %

PROYECCIÓN ACORDADA CON LA ADMINISTRACIÓN
  año 1: ventas +12 %, margen operacional 16,5 %
  año 2: ventas +10 %, margen 17,0 %
  año 3: ventas +8 %,  margen 17,0 %
  año 4: ventas +6 %,  margen 16,8 %
  año 5: ventas +5 %,  margen 16,5 %
  crecimiento perpetuo posterior: 2,5 %
  capital de trabajo: 30,6 % de las ventas (nivel actual)
  inversión: mantenimiento 420 + 25 % del aumento de ventas
```

**Paso 1 — proyecta el flujo de caja libre.**

```text
                       año 1   año 2   año 3   año 4   año 5
ventas                 25 088  27 597  29 805  31 593  33 173
resultado operacional   4 140   4 691   5 067   5 308   5 474
× (1 − 0,27)            3 022   3 424   3 699   3 875   3 996
+ depreciación            380     380     380     380     380
− inversión              −1 092  −1 047   −972    −867    −815
− Δ capital de trabajo   −822    −768    −676    −547    −483
FLUJO DE CAJA LIBRE     1 488   1 989   2 431   2 841   3 078
```

```text
VERIFICACIÓN DE LA INVERSIÓN
  año 1: 420 + 25 % × (25 088 − 22 400) = 420 + 672 = 1 092  ✓
VERIFICACIÓN DEL CAPITAL DE TRABAJO
  año 1: 30,6 % × 25 088 = 7 677; aumento 7 677 − 6 856 = 821  ✓
```

**Paso 2 — calcula el valor terminal.**

```text
flujo del año 6 = flujo año 5 × (1 + g)
  = 3 078 × 1,025 = 3 155

VT = 3 155 / (0,136 − 0,025) = 3 155 / 0,111 = 28 423
```

**Paso 3 — descuenta todo.**

```text
factores de descuento a 13,6 %
  año 1: 0,8803   año 2: 0,7749   año 3: 0,6821
  año 4: 0,6005   año 5: 0,5286

VP de los flujos
  año 1: 1 488 × 0,8803 = 1 310
  año 2: 1 989 × 0,7749 = 1 541
  año 3: 2 431 × 0,6821 = 1 658
  año 4: 2 841 × 0,6005 = 1 706
  año 5: 3 078 × 0,5286 = 1 627
  SUMA                    7 842

VP del valor terminal: 28 423 × 0,5286 = 15 025

VALOR DE EMPRESA: 7 842 + 15 025 = 22 867
```

**Paso 4 — evalúa el peso del valor terminal.**

```text
valor terminal / valor total = 15 025 / 22 867 = 65,7 %

dos tercios del valor dependen de g y del WACC
→ la sensibilidad a esos dos parámetros es lo que importa
```

**Paso 5 — construye la matriz de sensibilidad.**

```text
VALOR DE EMPRESA
              WACC 12,6 %  13,1 %  13,6 %  14,1 %  14,6 %
  g = 1,5 %      23 240   21 730   20 400   19 220   18 160
  g = 2,0 %      24 320   22 640   21 180   19 890   18 740
  g = 2,5 %      25 590   23 690   22 867   20 650   19 390
  g = 3,0 %      27 100   24 910   23 010   21 520   20 130

RANGO: 18 160 – 27 100
amplitud: 49 % sobre el mínimo
```

**Paso 6 — contrasta con múltiplos.**

```text
COMPARABLES DEL SECTOR (transacciones recientes)
  empresa   VE/RO+D   tamaño relativo   crecimiento
    A         7,8       3,2× mayor         +6 %
    B         6,4       1,8× mayor         +4 %
    C         5,9       similar            +9 %
    D         5,2       0,7× menor         +3 %
  mediana     6,15

MAGNITUD DE LA EMPRESA: resultado operacional + depreciación
  3 592 + 380 = 3 972

VALOR POR MÚLTIPLO MEDIANO: 3 972 × 6,15 = 24 428
```

**Paso 7 — ajusta el múltiplo.**

```text
AJUSTES
  · tamaño: la empresa es menor que la mediana de comparables
    descuento del 10 %
  · crecimiento: proyecta +12 % el primer año, sobre la mediana
    prima del 8 %
  · iliquidez: no cotiza, comparables incluyen cotizadas
    descuento del 15 %
  · control: las transacciones comparables SON de control
    → ya incluyen la prima; no se añade

múltiplo ajustado: 6,15 × 0,90 × 1,08 × 0,85 = 5,08
VALOR POR MÚLTIPLO AJUSTADO: 3 972 × 5,08 = 20 178
```

**Paso 8 — triangula y calcula el valor del patrimonio.**

```text
FLUJOS DESCONTADOS (caso base):     22 867
FLUJOS DESCONTADOS (rango):    18 160 – 27 100
MÚLTIPLO AJUSTADO:                  20 178
MÚLTIPLO SIN AJUSTAR:               24 428

RANGO DE VALOR DE EMPRESA CONVERGENTE: 20 000 – 25 000
punto central: 22 500
```

```text
DE VALOR DE EMPRESA A VALOR DEL PATRIMONIO
  valor de empresa (central)          22 500
  − deuda financiera                  −6 500
  + caja                                 210
  − contingencia laboral no provisionada −480
    (identificada en la revisión)
  + inmueble no operativo               1 600
  = VALOR DEL PATRIMONIO              17 330

RANGO DEL PATRIMONIO: 14 830 – 19 830
```

```text
LO QUE HAY QUE COMUNICAR AL VENDEDOR
  · el valor está entre 14 830 y 19 830
  · el 66 % del valor depende del crecimiento perpetuo
    y de la tasa de descuento
  · las tres palancas que más lo mueven:
      1. sostener el margen operacional por encima del 16 %
      2. reducir el capital de trabajo (cada punto de ventas
         liberado añade ~224 al valor)
      3. resolver la contingencia laboral antes de vender
  · un comprador estratégico con sinergias pagaría más;
    uno financiero, dentro del rango
```

**Interpreta:** el ejercicio produjo un rango de casi 5 000 sobre un valor central de 17 330, y **esa
amplitud es el resultado honesto**. Presentar 17 330 como «el valor» ocultaría que dos supuestos
explican dos tercios de la cifra. La utilidad de una valoración para negociar no está en el número: está
en saber **qué tres cosas mover para cambiarlo**.

## 🏦 Del cliente al banco

El dueño tiene una cifra en la cabeza y el banco valora con sus propios supuestos. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Mi empresa vale X» | Depende de quién compre y con qué supuestos | 13, clase 10 |
| «Dos asesores me dieron cifras distintas» | Supuestos distintos, ambos defendibles | 13, clase 10 |
| «El comprador descontó por la contingencia» | Ajuste de valor de empresa a patrimonio | 13, clase 10 |
| «Vale menos por no cotizar» | Descuento por iliquidez | 8, clase 6 |
| «El banco valoró mi garantía accionaria» | Misma metodología, otro propósito | 9, clase 9 |

## 🧪 Práctica

El laboratorio pide valorar una empresa por los tres enfoques y explicar las diferencias. La explicación es lo que se evalúa, no la cifra.

En `labs/lab-05.md`, sección de valoración:

1. Construye una valoración por flujos descontados con su valor terminal.
2. Calcula el peso del valor terminal y la matriz de sensibilidad.
3. Aplica múltiplos comparables con sus ajustes por tamaño, crecimiento e iliquidez.
4. Convierte valor de empresa en valor del patrimonio con todos sus ajustes.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen valoraciones que no se sostuvieron. Las causas son valor terminal desproporcionado y comparables mal elegidos.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se presenta un número, no un rango | Falsa precisión | Presenta rango y sensibilidad. |
| g superior al crecimiento de la economía | Imposible a perpetuidad | Limita g. |
| Múltiplo de empresa con magnitud de patrimonio | Inconsistencia | Verifica numerador y denominador. |
| Comparables sin ajustar | Tamaño y liquidez distintos | Aplica los ajustes. |
| Se añade prima de control sobre transacciones de control | Doble cómputo | Verifica qué incluye el comparable. |
| Esfuerzo en las proyecciones y no en g | Asignación errónea | El valor terminal pesa más. |

## ❓ Preguntas de comprobación

1. ¿Por qué una valoración es un rango y no un número?
2. ¿Por qué el valor terminal suele pesar más que las proyecciones explícitas?
3. ¿Qué debe cumplir la consistencia entre numerador y denominador de un múltiplo?
4. ¿Qué ajustes exige usar comparables cotizados para valorar una empresa no cotizada?
5. ¿Qué separa el valor de empresa del valor del patrimonio?

## 📥 Entregable

Guarda en `portfolio/parte-13/clase-10/`:

- la valoración por flujos descontados con su valor terminal y su peso;
- la matriz de sensibilidad con el rango resultante;
- la valoración por múltiplos con todos sus ajustes;
- la conversión a valor del patrimonio y las tres palancas de valor identificadas.

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

- Damodaran, A. (2012). *Investment Valuation* (3.ª ed.). Wiley.
- Koller, T., Goedhart, M. y Wessels, D. (2020). *Valuation: Measuring and Managing the Value of Companies* (7.ª ed.). Wiley.
- Brealey, R., Myers, S. y Allen, F. (2020). *Principles of Corporate Finance* (13.ª ed.). McGraw-Hill.
- Penman, S. (2013). *Financial Statement Analysis and Security Valuation* (5.ª ed.). McGraw-Hill.
- IFRS Foundation. *NIIF 13 Medición del Valor Razonable*. <https://www.ifrs.org/>
- Verificación local: revisa las normas de valoración aceptadas en tu jurisdicción para efectos tributarios y societarios.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 09 · Financiamiento de proyectos](09-financiamiento-de-proyectos.md) | [Parte 13](../README.md) · [Programa](../../../SYLLABUS.md) | [11 · Fusiones y adquisiciones →](11-fusiones-y-adquisiciones.md) |
<!-- gen:footer:end -->
