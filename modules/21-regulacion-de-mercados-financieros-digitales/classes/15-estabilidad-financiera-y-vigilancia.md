---
part: 22
class: 15
title: "Estabilidad financiera y vigilancia macroprudencial"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [estabilidad-financiera, macroprudencial, interconexion]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [FSB, BIS, BCCh]
requires_legal_review: false
---

<!-- gen:header:start -->
# Clase 15 · Estabilidad financiera y vigilancia macroprudencial

> [← 14 · Resiliencia operativa y terceros críticos](14-resiliencia-operativa-y-terceros-criticos.md) · [Índice de la parte](../README.md) · [16 · Regulación comparada: Chile y el mundo →](16-regulacion-comparada-chile-y-el-mundo.md)

**Parte 22 — Regulación de mercados financieros digitales** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Cambiar de escala. Hasta aquí la parte ha mirado a cada entidad por separado;
ahora mira **al conjunto**, que es donde aparecen riesgos que ninguna entidad
individual puede ver ni corregir.

La clase 14 terminó con una constatación que anticipa esta: veintidós entidades
cumplían su norma y el sector tenía un punto único de fallo del 86,4 %. Ese es
exactamente el tipo de riesgo que la vigilancia macroprudencial existe para
detectar.

Las clases anteriores supervisan entidad por entidad. Esta mira el conjunto, y busca lo que la supervisión individual no ve: las dependencias comunes que hacen frágil un sistema de entidades sanas.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** supervisión microprudencial de vigilancia macroprudencial.
2. **Identificar** los canales por los que un activo digital afecta al sistema.
3. **Construir** los indicadores de un tablero de vigilancia.
4. **Evaluar** si una actividad ha alcanzado relevancia sistémica.
5. **Explicar** por qué el tamaño no es el único criterio de relevancia.

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

Los tres primeros términos son los dos enfoques de supervisión y su criterio; los cinco siguientes, las dimensiones de la relevancia sistémica y sus herramientas. La **sustituibilidad** es la dimensión que más pesa y menos se mide: cuánto costaría reemplazar a un participante si desapareciera.

| Concepto | Comprensión verificable |
|---|---|
| `microprudencial` | Vigilancia de la solidez de cada entidad |
| `macroprudencial` | Vigilancia de la estabilidad del conjunto |
| `relevancia sistémica` | Capacidad de causar daño al sistema al fallar |
| `sustituibilidad` | Facilidad de reemplazar a un participante |
| `interconexión` | Densidad de vínculos entre participantes |
| `prociclicidad` | Que el mecanismo amplifique el ciclo |
| `canal de transmisión` | Vía por la que un shock llega al sistema |
| `herramienta macroprudencial` | Medida que actúa sobre el conjunto |

## 🧠 Modelo mental

El modelo mental es que la suma de entidades sanas puede ser un sistema frágil. La supervisión individual no ve las dependencias comunes, y por eso hace falta una mirada distinta que las busque explícitamente.

La diferencia entre las dos vigilancias no es de intensidad sino de objeto, y
confundirlas lleva a conclusiones tranquilizadoras y falsas.

```text
MICROPRUDENCIAL
  «¿está sana esta entidad?»
  → 22 respuestas correctas

MACROPRUDENCIAL
  «¿está sano el sistema?»
  → una respuesta, y puede ser NO
    aunque las 22 anteriores sean SÍ

POR QUÉ NO SE DEDUCE UNA DE OTRA
  · el riesgo puede estar en los vínculos,
    no en los nodos
  · lo que es prudente para una entidad
    puede ser desestabilizador si lo hacen
    todas a la vez
  · y hay riesgos que no están en el
    perímetro de nadie
```

El segundo punto merece detenerse. Vender un activo que cae es prudente para una
entidad. Si todas venden a la vez, el precio se hunde y la prudencia individual
produce el daño colectivo. Es el mismo mecanismo de la cascada de la Parte 21,
clase 14, visto a escala de sistema.

## 📖 Desarrollo

### 1. Los cuatro canales de transmisión

Antes de medir hace falta saber por dónde llega el shock. La experiencia de los
últimos episodios ha ido decantando cuatro canales, y solo el primero está en los
balances.

```text
1 EXPOSICIÓN DIRECTA
    bancos y fondos con posiciones
    → medible, y suele ser el menor

2 EXPOSICIÓN INDIRECTA
    crédito a quien está expuesto,
    depósitos de intermediarios
    → la de la Parte 20, clase 14

3 CONFIANZA
    un fallo visible deteriora la percepción
    sobre entidades sin relación
    → no se mide en ninguna parte

4 FUNCIÓN CRÍTICA
    si la actividad se ha vuelto necesaria
    para pagar, liquidar o valorar
    → el más importante y el más tardío
      en reconocerse
```

### 2. Relevancia sistémica no es tamaño

Un participante pequeño puede ser sistémico si nadie puede sustituirlo. El
tamaño es solo uno de los criterios, y suele ser el que menos discrimina en
mercados nuevos.

```text
CRITERIOS HABITUALES

  TAMAÑO           volumen, saldo, cuota
  SUSTITUIBILIDAD  ¿quién ocupa su lugar
                   y en cuánto tiempo?
  INTERCONEXIÓN    ¿a cuántos arrastra?
  COMPLEJIDAD      ¿se puede resolver
                   ordenadamente?
  ACTIVIDAD
  TRANSFRONTERIZA  ¿cuántas jurisdicciones
                   tienen que coordinarse?

EL PROVEEDOR DE PRECIOS DE LA PARTE 20,
CLASE 14, ES EL EJEMPLO
  cuota de mercado pequeña en ingresos
  y sustituibilidad nula
  → sistémico por el segundo criterio
```

### 3. El tablero de vigilancia

Un tablero útil se distingue de uno decorativo en que sus indicadores cambian
antes que los titulares. Los que siguen ya han aparecido en el programa; aquí se
agregan a escala de sistema.

```text
NIVEL DE ACTIVIDAD
  · circulante de instrumentos referenciados
  · volumen liquidado en registros
  · saldo custodiado por terceros

INTERCONEXIÓN
  · exposición del sistema bancario, directa
    e indirecta
  · depósitos de intermediarios digitales
  · concentración por proveedor común

FRAGILIDAD
  · composición y plazo medio de las reservas
  · desvío de precio fuera de banda y su
    duración
  · redención efectiva frente a solicitada
  · participantes autorizados activos

FUNCIÓN CRÍTICA
  · proporción de pagos que dependen de
    la actividad
  · alternativas disponibles y su capacidad
```

### 4. Herramientas

Las herramientas macroprudenciales actúan sobre el conjunto y por eso suelen ser
impopulares: limitan a quien todavía no ha hecho nada mal.

```text
  · límites de exposición del sistema bancario
  · recargos de capital por relevancia sistémica
  · requisitos de liquidez específicos
  · límites de crecimiento por actividad
  · designación de terceros críticos
  · exigencia de información al conjunto

Y UNA QUE NO ES UNA HERRAMIENTA
  advertir públicamente sin actuar
  → informa y no reduce el riesgo
```

### 5. Cuándo actuar

El problema de la vigilancia macroprudencial es que la evidencia llega cuando el
coste de actuar ya es alto. Actuar pronto es barato y se percibe como
injustificado; actuar tarde es caro y se percibe como necesario.

```text
LA REGLA QUE AYUDA

  fijar los umbrales ANTES de acercarse
  a ellos, y publicarlos

  · antes: la decisión es técnica
  · después: la decisión es política
    y llega tarde
```

## 🧮 Ejemplo guiado

El ejemplo evalúa la relevancia sistémica de un participante en las cuatro dimensiones. La sustituibilidad es la que lo convierte en relevante.

**Situación.** Un banco central evalúa si la actividad de activos digitales ha
alcanzado relevancia sistémica en su jurisdicción.

```text
DATOS DEL SISTEMA
  activos del sistema bancario   180 000 000 000
  circulante de referenciados      2 400 000 000
  exposición directa de bancos        90 000 000
  crédito a intermediarios digitales 640 000 000
  depósitos de intermediarios      1 200 000 000
  pagos minoristas diarios         6 800 000 000
  de ellos, por rieles digitales     210 000 000
```

**Paso 1 — mide la exposición directa.**

```text
90 000 000 / 180 000 000 000 = 0,05 %

  → DESPRECIABLE

Y ESTA ES LA CIFRA QUE SE PUBLICA
en casi todos los informes de estabilidad.
```

**Paso 2 — mide la exposición indirecta.**

```text
CRÉDITO A INTERMEDIARIOS      640 000 000

  fracción media en riesgo de esos
  intermediarios: supuesto 28 %
  exposición de segundo grado
  640 000 000 × 28 % = 179 200 000

DEPÓSITOS DE INTERMEDIARIOS 1 200 000 000
  no son exposición de crédito
  y sí son financiación que puede irse
  de golpe

  supuesto de retirada en tensión: 45 %
  = 540 000 000 de salida simultánea

EXPOSICIÓN ECONÓMICA TOTAL
  90 + 179 + 540 = 809 200 000
  = 0,45 % de los activos bancarios

  NUEVE VECES LA CIFRA PUBLICADA
```

**Paso 3 — mide la concentración.**

```text
LOS 640 000 000 DE CRÉDITO
  se reparten entre 4 bancos
  el mayor concentra 310 000 000

LOS 1 200 000 000 DE DEPÓSITOS
  el mayor banco receptor tiene 780 000 000
  = el 65 %

  y ese banco tiene 14 200 000 000
  de depósitos mayoristas totales

  780 000 000 / 14 200 000 000 = 5,5 %
  de su financiación mayorista

  → RELEVANTE PARA ESE BANCO,
    no para el sistema
```

**Paso 4 — mide la función crítica.**

```text
PAGOS POR RIELES DIGITALES
  210 000 000 / 6 800 000 000 = 3,1 %

  ¿HAY ALTERNATIVA?
  sí: transferencia y tarjeta absorben
  ese volumen sin problema

  → NO ES FUNCIÓN CRÍTICA TODAVÍA

UMBRAL PROPUESTO
  el 15 % de los pagos minoristas, o
  cualquier proporción si no hay alternativa
  con capacidad
```

**Paso 5 — evalúa la sustituibilidad.**

```text
CUSTODIA DE ACTIVOS DIGITALES

  tres custodios en el mercado
  el mayor tiene el 71 %

  ¿CUÁNTO TARDA UNA MIGRACIÓN?
  supuesto: 10 días hábiles por entidad

  si el mayor cae, 71 % del saldo
  custodiado queda inmovilizado
  al menos 10 días

  → SUSTITUIBILIDAD BAJA
  → RELEVANCIA SISTÉMICA POR ESTE CRITERIO,
    con un tamaño que no la habría dado
```

**Paso 6 — resume el tablero.**

```text
                          VALOR      UMBRAL   ESTADO

exposición directa        0,05 %      1,0 %   verde
exposición económica      0,45 %      2,0 %   verde
concentración depósitos   5,5 %       8,0 %   verde
pagos por rieles          3,1 %      15,0 %   verde
custodio mayor           71,0 %      40,0 %   ROJO
plazo de migración       10 días      5 días  ROJO

  CUATRO VERDES Y DOS ROJOS
  y los dos rojos son del mismo criterio:
  sustituibilidad
```

**Paso 7 — decide qué hacer y qué no.**

```text
QUÉ PROCEDE

  1 designar al custodio mayor como
    infraestructura relevante y vigilarlo
  2 exigir plan de migración probado,
    con objetivo de 5 días
  3 pedir a las entidades que declaren
    su dependencia y su alternativa
  4 publicar el tablero con sus umbrales

QUÉ NO PROCEDE

  · límites de exposición bancaria:
    los indicadores están en verde y un
    límite ahora solo desplaza actividad
  · recargos de capital: no hay relevancia
    por tamaño
  · advertencia pública sin medida:
    informa y no reduce el riesgo

Y LA CONCLUSIÓN PARA EL INFORME
  la actividad NO es sistémica por tamaño
  y SÍ tiene un punto de relevancia por
  sustituibilidad. Publicar solo el 0,05 %
  de exposición directa habría sido cierto
  y habría ocultado lo único que importa.
```

**Interpreta:** la exposición directa era del 0,05 % y la económica del 0,45 %,
nueve veces mayor. Y aun así **ninguna de las dos era el hallazgo**: lo era un
custodio con el 71 % del saldo y diez días de migración, que no aparece en
ninguna medida de tamaño.

## 🧭 Perspectivas

La estabilidad financiera afecta a cada participante de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un sector pequeño | — |
| Banco | 5,5 % de su financiación mayorista | Qué límite pone |
| Intermediario | Una designación posible | Cómo se prepara |
| Custodio mayor | 71 % del mercado | Si acepta la vigilancia |
| Custodio pequeño | Una oportunidad | Si amplía capacidad |
| Banco central | Cuatro verdes y dos rojos | Qué medida toma |
| Supervisor micro | 22 entidades sanas | Qué reporta al macro |
| Ministerio | Un informe de estabilidad | Qué publica |
| Sociedad | Un riesgo que no ve | Qué transparencia exige |

## 🏦 Del cliente al banco

El cliente no lo percibe y su entidad puede depender de un nodo sin sustituto. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Es un sector pequeño» | La exposición económica es nueve veces mayor | 22, clase 15 |
| «Todos los bancos están sanos» | El riesgo está en los vínculos | 22, clase 15 |
| «Hay tres custodios» | Uno tiene el 71 % | 22, clase 15 |

## ⚖️ Riesgos y controles

Los riesgos son de interconexión y de prociclicidad. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Publicar solo exposición directa | Es cierto y oculta lo demás | Publicar la económica y sus canales |
| Confundir micro con macro | 22 respuestas correctas | El riesgo puede estar en los vínculos |
| Medir solo por tamaño | Es el criterio disponible | La sustituibilidad decide más |
| Prociclicidad no vista | Lo prudente individual daña al conjunto | Escenarios de venta simultánea |
| Umbrales fijados tarde | La decisión se politiza | Fijarlos y publicarlos antes |
| Advertir sin actuar | Parece una medida | Informa y no reduce el riesgo |

## 🧪 Práctica

El laboratorio pide evaluar la relevancia sistémica de varios participantes. La sustituibilidad es la dimensión que decide.

En [`labs/lab-08.md`](../labs/lab-08.md):

1. Construye el tablero con sus cuatro bloques de indicadores.
2. Calcula la exposición económica y compárala con la directa.
3. Evalúa la relevancia por los cinco criterios.
4. Propón medidas y justifica también las que descartas.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen riesgos sistémicos no detectados. La causa es la supervisión solo individual.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Reportar exposición directa | Es la que se puede calcular | Añade indirecta y depósitos |
| Deducir el macro del micro | Todas las entidades están bien | No se deduce |
| Tamaño como único criterio | Es el más objetivo | La sustituibilidad discrimina más |
| Umbrales al acercarse | Se fijan cuando hay presión | Antes, y publicados |
| Advertencia como medida | Es lo políticamente viable | No reduce el riesgo |
| Actuar sobre lo verde | Hay presión por hacer algo | Justifica también lo que descartas |

## ❓ Preguntas de comprobación

1. ¿Por qué la vigilancia macroprudencial no se deduce de la microprudencial?
2. Enumera los cuatro canales de transmisión y di cuál se mide peor.
3. ¿Por qué el tamaño no basta para determinar relevancia sistémica?
4. ¿Qué indicadores componen un tablero de vigilancia útil?
5. ¿Por qué conviene fijar los umbrales antes de acercarse a ellos?

## 📥 Entregable

Guarda en `portfolio/parte-22/clase-15/`:

- el tablero con sus indicadores y umbrales;
- el cálculo de exposición directa frente a económica;
- la evaluación de relevancia por los cinco criterios;
- las medidas propuestas y las descartadas, ambas justificadas.

## 🔗 Referencias cruzadas

- **Viene de:** clases 8, 11 y 14; Parte 20, clase 14.
- **Continúa en:** clases 16 y 17 de esta parte.
- **Se aplica en:** clase 18 de esta parte; Parte 23, clase 14.

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

- Financial Stability Board (2022). *Assessment of Risks to Financial Stability from Crypto-assets*. FSB. <https://www.fsb.org/2022/02/assessment-of-risks-to-financial-stability-from-crypto-assets/>
- Financial Stability Board (2023). *The Financial Stability Implications of Multifunction Crypto-asset Intermediaries*. FSB. <https://www.fsb.org/2023/11/the-financial-stability-implications-of-multifunction-crypto-asset-intermediaries/>
- Basel Committee on Banking Supervision (2018). *Framework for dealing with domestic systemically important banks*. BIS. <https://www.bis.org/publ/bcbs233.htm>
- Banco Central de Chile. *Informe de Estabilidad Financiera*. BCCh. <https://www.bcentral.cl/areas/estabilidad-financiera>
- Verificación local: comprueba qué autoridad ejerce la vigilancia macroprudencial en tu jurisdicción, qué indicadores publica y si tiene facultades para designar infraestructuras relevantes. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 14 · Resiliencia operativa y terceros críticos](14-resiliencia-operativa-y-terceros-criticos.md) | [Parte 22](../README.md) · [Programa](../../../SYLLABUS.md) | [16 · Regulación comparada: Chile y el mundo →](16-regulacion-comparada-chile-y-el-mundo.md) |
<!-- gen:footer:end -->
