---
part: 8
class: 11
title: "Análisis fundamental"
level: avanzado
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 11 · Análisis fundamental

> [← 10 · Construcción de portafolios](10-construccion-de-portafolios.md) · [Índice de la parte](../README.md) · [12 · Análisis técnico: introducción crítica →](12-analisis-tecnico-introductorio.md)

**Parte 08 — Inversiones y mercados** · **Nivel:** Avanzado — perfil analista · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Aplicar el análisis de estados financieros de la Parte 5 a la valoración de una empresa cotizada, y
llegar a una conclusión defendible sobre si su precio es razonable. Esta clase entrega el proceso
completo, desde el negocio hasta el rango de valor, con las verificaciones que hacen el resultado
auditable.

## 📚 Objetivos

Al finalizar podrás:

1. **Estructurar** el análisis en las cinco capas del proceso.
2. **Evaluar** la calidad y sostenibilidad del negocio.
3. **Valorar** por flujos descontados y por múltiplos, y conciliar ambos.
4. **Construir** un rango de valor con supuestos declarados.
5. **Reconocer** los límites del análisis fundamental y del propio analista.

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
| `análisis fundamental` | Estimación del valor de una empresa a partir de su capacidad de generar caja. |
| `ventaja competitiva` | Característica que permite sostener retornos sobre el costo del capital. |
| `retorno sobre el capital invertido (ROIC)` | `resultado operativo neto / capital invertido`. Mide la calidad del negocio. |
| `creación de valor` | Ocurre cuando `ROIC > WACC`. Si no, el crecimiento destruye valor. |
| `margen de seguridad` | Diferencia entre el valor estimado y el precio pagado. |
| `rango de valor` | Resultado correcto de una valoración: nunca un punto único. |

## 🧠 Modelo mental

Una empresa crea valor **solo si su retorno supera su costo de capital**:

```text
ROIC > WACC  →  crecer CREA valor
ROIC = WACC  →  crecer es indiferente
ROIC < WACC  →  crecer DESTRUYE valor
```

Esa relación explica por qué dos empresas que crecen al mismo ritmo pueden valer cosas muy distintas,
y por qué "crecimiento" no es sinónimo de "buena inversión".

## 📖 Desarrollo

### 1. Las cinco capas del proceso

```text
1. NEGOCIO       ¿qué hace, cómo gana dinero, quién es su cliente?
2. INDUSTRIA     ¿cómo es la competencia, las barreras, la regulación?
3. FINANZAS      ¿genera caja, con qué rentabilidad, con qué riesgo?
4. VALORACIÓN    ¿cuánto vale bajo supuestos explícitos?
5. PRECIO        ¿qué supone el precio actual y es razonable?
```

Saltarse la capa 1 y 2 es el error más frecuente: **se valora una empresa cuyo negocio no se
comprende**, y entonces los supuestos de crecimiento y margen son arbitrarios.

### 2. Evaluar el negocio

Preguntas que estructuran la capa 1 y 2:

```text
· ¿cómo gana dinero exactamente? (unidad económica: por cliente, por transacción, por unidad)
· ¿qué proporción de sus ingresos es recurrente?
· ¿quién es su cliente y qué poder de negociación tiene?
· ¿quiénes son sus proveedores y qué poder tienen?
· ¿qué impide que un competidor haga lo mismo?
· ¿qué cambio tecnológico o regulatorio podría destruir el negocio?
```

Fuentes de ventaja competitiva sostenible:

| Fuente | Mecanismo | Verificación |
|---|---|---|
| Costos bajos estructurales | Escala, ubicación, tecnología propia | Margen superior sostenido |
| Efecto de red | El valor crece con los usuarios | Crecimiento acelerado, baja fuga |
| Costo de cambio | Al cliente le cuesta irse | Alta retención, ingresos recurrentes |
| Activo intangible | Marca, patente, licencia | Precio superior sostenido |
| Escala eficiente | El mercado solo sostiene pocos actores | Estabilidad de participaciones |

**Verificación cuantitativa de la ventaja:**

```text
si existe ventaja competitiva sostenible → ROIC > WACC de forma persistente
si el ROIC converge al WACC en pocos años → la ventaja no era sostenible
```

### 3. Análisis financiero orientado a la valoración

```text
ROIC = NOPAT / capital invertido
     = (resultado operativo × (1 − tasa impuesto)) / (patrimonio + deuda financiera neta)
```

```text
resultado operativo 4 200 · tasa impuesto 25 % · patrimonio 18 400 · deuda neta 6 200
NOPAT = 4 200 × 0,75 = 3 150
capital invertido = 24 600
ROIC = 3 150/24 600 = 12,80 %
WACC = 9,40 %
diferencial = +3,40 puntos → CREA valor
```

Descomposición del ROIC:

```text
ROIC = margen operativo neto × rotación del capital
     = (NOPAT/ventas) × (ventas/capital invertido)
     = 0,0875 × 1,463 = 12,80 %
```

Esta descomposición indica **de dónde viene la rentabilidad**: márgenes altos (poder de precio) o
rotación alta (eficiencia de capital). Son estrategias distintas con vulnerabilidades distintas.

Verificaciones de calidad (Parte 5):

```text
□ ¿el resultado se convierte en flujo operativo? (calidad del resultado ≥ 0,8)
□ ¿las cuentas por cobrar y existencias crecen en línea con las ventas?
□ ¿hay partidas no recurrentes que inflan el resultado?
□ ¿las estimaciones (depreciación, provisiones) son consistentes en el tiempo?
□ ¿la deuda incluye obligaciones fuera de balance?
```

### 4. Valorar

**Por flujos descontados:**

```text
valor de la firma = Σ FCF_t/(1+WACC)^t + VT/(1+WACC)^n
valor del patrimonio = valor de la firma − deuda financiera neta
```

**Por múltiplos:**

```text
valor = múltiplo de comparables × métrica de la empresa
```

Los dos métodos deben **conciliarse**: si difieren mucho, hay que explicar por qué.

```text
flujos descontados:  valor patrimonio 32 400
múltiplos (EV/EBITDA de comparables 8,2x): valor patrimonio 27 900
diferencia: 16 %

explicaciones posibles:
  · el modelo de flujos supone un crecimiento que los comparables no tienen
  · los comparables están momentáneamente subvalorados
  · el WACC usado es demasiado bajo
  · la empresa tiene una característica que justifica un múltiplo mayor
```

**La conciliación no es opcional:** si no se puede explicar la diferencia, alguno de los dos métodos
tiene un error.

### 5. Límites del análisis y del analista

```text
LÍMITES DEL MÉTODO
· el valor depende de supuestos sobre un futuro incierto
· pequeños cambios en WACC o g mueven el resultado significativamente (Parte 7, clase 6)
· la información pública es incompleta y llega con rezago
· el mercado puede estar equivocado durante mucho tiempo

LÍMITES DEL ANALISTA
· sesgo de confirmación: buscar datos que apoyen la conclusión inicial
· sesgo de anclaje: quedar fijado en el precio actual o en el valor de un análisis previo
· exceso de confianza: rangos demasiado estrechos
· sesgo de disponibilidad: sobreponderar la información reciente
```

Contramedidas concretas:

```text
· escribir la tesis contraria antes de concluir: ¿por qué podría estar equivocado?
· declarar el rango ANTES de mirar el precio de mercado
· documentar qué evidencia cambiaría la conclusión
· revisar valoraciones pasadas y medir el error sistemático propio
```

## 🧮 Ejemplo guiado

**Situación.** Analiza una empresa de servicios que cotiza a 3 850 por acción.

```text
DATOS (últimos 12 meses, millones)
  ingresos                    68 400
  resultado operativo          9 850
  NOPAT                        7 388
  depreciación                 2 940
  inversión en activos fijos   3 200
  variación capital de trabajo   890
  deuda financiera neta       14 600
  patrimonio contable         31 200
  acciones en circulación      18,4 millones
  WACC estimado                 9,8 %

HISTORIA (5 años)
  crecimiento de ingresos      7,8 % anual
  margen operativo             13,2 % → 14,4 %
  ROIC                         11,1 % → 16,1 %
```

**Paso 1 — capa 1 y 2: el negocio.**

```text
· ingresos 82 % recurrentes (contratos plurianuales)
· tasa de retención de clientes: 94 %
· 3 competidores relevantes; participación estable en 5 años
· costo de cambio alto: integración con sistemas del cliente
· regulación estable

VENTAJA COMPETITIVA: costo de cambio + contratos recurrentes
verificación: ROIC creciente de 11,1 % a 16,1 %, sostenidamente sobre el WACC ✔
```

**Paso 2 — capa 3: calidad financiera.**

```text
ROIC = 7 388/(31 200 + 14 600) = 16,13 %
diferencial ROIC − WACC = 16,13 − 9,80 = +6,33 puntos → crea valor

descomposición:
  margen NOPAT = 7 388/68 400 = 10,80 %
  rotación de capital = 68 400/45 800 = 1,493
  ROIC = 10,80 % × 1,493 = 16,13 % ✔

calidad del resultado:
  flujo operativo = 7 388 + 2 940 − 890 = 9 438
  flujo operativo/NOPAT = 1,28  ✔ excelente
  
flujo de caja libre = 9 438 − 3 200 = 6 238
```

**Paso 3 — capa 4: valoración por flujos descontados.**

```text
supuestos declarados:
  crecimiento años 1-5:  7,0 % (bajo el histórico de 7,8 %, por madurez)
  crecimiento años 6-10: 4,5 % (convergencia)
  g perpetuo:            2,8 % (≤ crecimiento nominal de largo plazo de la economía)
  WACC:                  9,8 %
  margen NOPAT estable en 10,8 %
  inversión = depreciación + 25 % del crecimiento de ingresos
```

```text
FCF proyectado (millones)
  año 1   6 505    año 6   8 972
  año 2   6 782    año 7   9 335
  año 3   7 071    año 8   9 712
  año 4   7 373    año 9  10 105
  año 5   7 688    año 10 10 514

VP de los 10 años                      = 51 840
VT = 10 514 × 1,028/(0,098 − 0,028)     = 154 428
VP del VT = 154 428/(1,098)^10          =  60 400
VALOR DE LA FIRMA                       = 112 240
− deuda financiera neta                 = −14 600
VALOR DEL PATRIMONIO                    =  97 640
÷ 18,4 millones de acciones             =   5 306 por acción
```

**Paso 4 — valoración por múltiplos.**

```text
comparables (3 empresas del sector):
  EV/EBITDA promedio  9,4x   rango 8,1x – 10,6x
  P/U promedio       17,2x   rango 15,4x – 19,8x

EBITDA de la empresa = 9 850 + 2 940 = 12 790
valor de la firma = 12 790 × 9,4 = 120 226
valor patrimonio = 120 226 − 14 600 = 105 626 → 5 741 por acción

utilidad neta estimada ≈ 6 100
valor por P/U = 6 100 × 17,2 = 104 920 → 5 702 por acción
```

**Paso 5 — concilia y construye el rango.**

```text
flujos descontados:  5 306
EV/EBITDA:           5 741
P/U:                 5 702

diferencia: los múltiplos dan ~8 % más
explicación: los comparables tienen ROIC promedio de 13,4 %, inferior al 16,1 %
             de esta empresa → un múltiplo superior al promedio está justificado
             pero el modelo de flujos ya incorpora ese ROIC superior

rango de valor: 5 100 – 5 900 por acción
punto central: 5 500
```

**Paso 6 — capa 5: el precio y la decisión.**

```text
precio de mercado: 3 850
rango de valor: 5 100 – 5 900

margen de seguridad respecto del extremo inferior del rango:
  (5 100 − 3 850)/5 100 = 24,5 %
```

**Paso 7 — la verificación que impide el exceso de confianza.**

```text
¿qué tendría que ser cierto para que 3 850 fuera el valor correcto?

resolviendo hacia atrás:
  con g perpetuo de 1,2 % en lugar de 2,8 % → valor 4 020
  con WACC de 11,6 % en lugar de 9,8 %     → valor 3 940
  con margen NOPAT de 8,9 % en lugar de 10,8 % → valor 3 880

→ el precio de mercado supone que el margen cae 1,9 puntos, o que el riesgo
  es 1,8 puntos mayor, o que el crecimiento perpetuo es la mitad del supuesto

TESIS CONTRARIA (escrita antes de concluir):
  · un competidor con tecnología distinta podría reducir el costo de cambio
  · la concentración de clientes: los 5 mayores son el 34 % de los ingresos
  · el margen creció 1,2 puntos en 5 años: ¿es sostenible o hubo un factor transitorio?

CONCLUSIÓN
  La empresa parece subvalorada con un margen de seguridad del 24,5 %.
  Los tres supuestos que sostienen esa conclusión son el margen, el WACC y g.
  El riesgo principal identificado es la concentración de clientes (34 % en 5).
  
  RECOMENDACIÓN: posición de hasta el 4 % de la cartera, respetando el límite
  por emisor de la política. Revisar si el margen cae bajo 10 % o si se pierde
  alguno de los 5 clientes principales.
```

**Interpreta:** la conclusión es favorable **y viene con tres supuestos identificados, una tesis
contraria escrita y dos gatillos de revisión**. Esa estructura es lo que distingue un análisis de una
opinión, y es también lo que permite evaluar después si el analista se equivocó por mala suerte o por
mal análisis.

## 🏦 Del cliente al banco

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| ROIC vs. WACC | Evaluación de la capacidad de repago de largo plazo | 13, clase 4 |
| Calidad del resultado | Verificación en el análisis de crédito | 9, clase 9 |
| Ventaja competitiva | Sostenibilidad del flujo del deudor | 9, clase 9 |
| Concentración de clientes | Riesgo del deudor comercial | 13, clase 13 |
| Rango de valor | Formato del informe de análisis | 13, clase 7 |

## 🧪 Práctica

En `labs/lab-06.md`:

1. Analiza el negocio y la industria de una empresa cotizada con las seis preguntas.
2. Calcula ROIC, su descomposición y el diferencial contra el WACC en cinco años.
3. Valora por flujos descontados y por múltiplos, y concilia ambos resultados.
4. Escribe la tesis contraria y determina qué supone el precio de mercado.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se valora sin comprender el negocio | Capas 1 y 2 omitidas | Empieza por cómo gana dinero. |
| Se supone que crecer siempre crea valor | ROIC vs. WACC ignorado | Si `ROIC < WACC`, crecer destruye valor. |
| Los dos métodos difieren y no se explica | Conciliación omitida | Explica la diferencia o revisa ambos. |
| Se entrega un valor puntual | Falsa precisión | Presenta un rango con supuestos. |
| Se busca evidencia que confirme la tesis | Sesgo de confirmación | Escribe la tesis contraria antes de concluir. |
| No se define qué cambiaría la conclusión | Sin gatillos de revisión | Declara los umbrales de revisión. |

## ❓ Preguntas de comprobación

1. ¿Por qué crecer puede destruir valor?
2. Descompón un ROIC de 14 % en margen y rotación e interpreta ambas rutas.
3. ¿Qué haces si la valoración por flujos y por múltiplos difieren un 20 %?
4. ¿Cómo determinas qué supone el precio de mercado?
5. ¿Qué contramedidas reducen el sesgo de confirmación en un análisis?

## 📥 Entregable

Guarda en `portfolio/parte-08/clase-11/`:

- el análisis del negocio y la industria con las seis preguntas respondidas;
- el ROIC descompuesto de cinco años y su diferencial contra el WACC;
- las dos valoraciones conciliadas con el rango de valor y sus supuestos;
- la tesis contraria escrita, lo que supone el precio actual y los gatillos de revisión.

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

- Damodaran, A. (2012). *Investment Valuation* (3.ª ed.). Wiley. Proceso completo de valoración fundamental.
- Koller, T., Goedhart, M. y Wessels, D. (2020). *Valuation* (7.ª ed.). McKinsey/Wiley. Capítulos 2 a 8: ROIC, crecimiento y creación de valor.
- Penman, S. (2013). *Financial Statement Analysis and Security Valuation* (5.ª ed.). McGraw-Hill. Análisis de calidad del resultado.
- Greenwald, B. et al. (2001). *Competition Demystified*. Portfolio. Identificación de ventajas competitivas sostenibles.
- Mauboussin, M. y Callahan, D. (2020). *Expectations Investing* (edición revisada). Columbia Business School. Qué supone el precio de mercado.
- Verificación local: usa memorias anuales y estados financieros publicados en el registro del supervisor de valores de tu país, con su fecha.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 10 · Construcción de portafolios](10-construccion-de-portafolios.md) | [Parte 08](../README.md) · [Programa](../../../SYLLABUS.md) | [12 · Análisis técnico: introducción crítica →](12-analisis-tecnico-introductorio.md) |
<!-- gen:footer:end -->
