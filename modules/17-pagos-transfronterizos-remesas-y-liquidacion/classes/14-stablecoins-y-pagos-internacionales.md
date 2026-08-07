<!-- meta
part: 18
class: 14
title: "Stablecoins y pagos internacionales"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global]
regulatory_topics: [cross-border-payments, stablecoins, aml-cft]
regulation_last_verified: 2026-08-06
regulatory_status: en-desarrollo
primary_authorities: [FSB, CPMI, GAFI]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 14 · Stablecoins y pagos internacionales

> [← 13 · Interconexión de sistemas de pagos inmediatos](13-interconexion-de-pagos-inmediatos.md) · [Índice de la parte](../README.md) · [15 · Payment versus Payment y liquidación atómica →](15-payment-versus-payment-y-liquidacion-atomica.md)

**Parte 18 — Pagos transfronterizos, remesas y liquidación internacional** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Evaluar una ruta de pago que usa una stablecoin **con el mismo criterio que
cualquier otra**: coste total, tiempo hasta la disponibilidad, riesgo asumido y
cumplimiento. Sin entusiasmo y sin rechazo previo.

> Esta clase trata la stablecoin **como medio de pago transfronterizo**. Su
> diseño, sus reservas, su redención y su regulación se estudian en la Parte 20,
> que es donde corresponde. Aquí solo se pregunta: ¿mejora el pago?

La clase anterior conecta infraestructuras públicas. Esta explora la vía privada, y su análisis exige mirar los tres tramos: el intermedio es barato y los dos extremos, que son las conversiones, no lo son.

## 📚 Objetivos

Al finalizar podrás:

1. **Trazar** la ruta completa de un pago con stablecoin, incluidos sus extremos.
2. **Calcular** su coste total y compararlo con la ruta clásica sobre la misma
   base.
3. **Identificar** dónde se concentran el riesgo y el coste reales.
4. **Explicar** por qué el ahorro observado no proviene de la tecnología de
   registro.
5. **Determinar** en qué corredores la ruta tiene sentido y en cuáles no.

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

Los cuatro primeros términos son el instrumento y sus puntos de conversión; los cuatro siguientes, sus riesgos propios y su régimen. La **entrada y la salida** son donde vive el coste real: mover valor entre carteras es barato y convertirlo a moneda local en el destino no lo es.

| Concepto | Comprensión verificable |
|---|---|
| `stablecoin` | Criptoactivo que busca mantener un valor de referencia |
| `entrada` | Conversión de moneda fiduciaria a stablecoin |
| `salida` | Conversión de stablecoin a moneda fiduciaria |
| `emisor` | Entidad que emite y redime la stablecoin |
| `riesgo de emisor` | Riesgo de que el emisor no pueda redimir a la par |
| `pérdida de paridad` | Situación en que el precio se aparta del valor de referencia |
| `coste de red` | Comisión por registrar la transferencia |
| `regla del viaje en activos virtuales` | Obligación de que los datos acompañen la transferencia |

## 🧠 Modelo mental

El modelo mental es que el tramo intermedio no es el problema. Un pago con stablecoin sustituye la corresponsalía por una red pública, y el coste se traslada a la conversión en los dos extremos y al riesgo del emisor.

```text
UNA RUTA CON STABLECOIN TIENE CINCO TRAMOS,
Y EL DE LA TECNOLOGÍA ES EL MÁS BARATO

  1. ENTRADA        moneda local → stablecoin
     coste: comisión del proveedor + diferencial de cambio
  2. TRANSFERENCIA  registro de la operación
     coste: comisión de red — céntimos
  3. TENENCIA       tiempo en stablecoin
     coste: riesgo de emisor y de paridad
  4. SALIDA         stablecoin → moneda de destino
     coste: comisión + diferencial + disponibilidad local
  5. ÚLTIMA MILLA   llegar al beneficiario
     coste: igual que en cualquier otra ruta

EL ERROR DE ANÁLISIS MÁS COMÚN
  comparar el tramo 2 con la ruta clásica completa

  «cuesta un céntimo y tarda segundos» es cierto
  del tramo 2, y falso de la ruta
```

## 📖 Desarrollo

### 1. Los tramos que realmente cuestan

Al comparar rutas conviene mirar dónde está el coste, no dónde está la
novedad. El bloque descompone la ruta con stablecoin y muestra que los tramos
caros exigen exactamente los mismos requisitos que un operador clásico.

```text
ENTRADA Y SALIDA SON EL 90 % DEL COSTE

  porque en ambos extremos hace falta
    · una entidad que compre o venda la stablecoin
    · con acceso al sistema bancario local
    · con licencia si la jurisdicción la exige
    · con liquidez en las dos puntas
    · y con cumplimiento

  ES DECIR: exactamente los mismos requisitos
  que un operador de remesas clásico

LA CONSECUENCIA
  la ruta con stablecoin no elimina intermediarios:
  los sustituye por otros distintos
```

### 2. Qué mejora de verdad

| Elemento | ¿Mejora? | Por qué |
|---|---|---|
| Tiempo del tramo intermedio | Sí, mucho | No hay ventana ni día inhábil |
| Operación en fin de semana | Sí | La red no cierra |
| Número de intermediarios en tránsito | Sí | La cadena de corresponsales desaparece |
| Prefinanciación en el tramo intermedio | Sí | No hay nostro que dotar |
| Coste de entrada y salida | No necesariamente | Depende del mercado local |
| Última milla | No | Es el mismo problema |
| Cumplimiento | No | Se aplica igual, y a veces es más difícil |
| Riesgo de contraparte | Cambia | Pasa del corresponsal al emisor |

El resultado se ordena aplicando la pregunta de la clase 5, que separa lo que
mejora de lo que permanece igual.

```text
LA PREGUNTA DE LA CLASE 5 APLICADA AQUÍ
  ¿en qué capa actúa?

  la stablecoin actúa en la capa de LIQUIDACIÓN
  del tramo intermedio, y por eso sí reduce tiempo

  pero no actúa en las entradas, las salidas
  ni la última milla, que es donde está el coste
```

### 3. Riesgos que la ruta introduce

Cambiar de ruta no elimina riesgos: los sustituye por otros. El bloque
enumera los que introduce esta y señala en cada caso de qué depende su
magnitud, que casi siempre es el tiempo de tenencia.

```text
RIESGO DE EMISOR
  mientras el valor está en stablecoin, se tiene
  una exposición al emisor, no al banco
  → ¿está respaldada? ¿la reserva es líquida?
    ¿el derecho de redención es exigible?
  → se estudia en la Parte 20

RIESGO DE PARIDAD
  si el precio se aparta del valor de referencia
  durante la tenencia, el importe convertido cambia
  → la exposición es proporcional al TIEMPO en tenencia
  → una ruta de minutos tiene poca; una de días, mucha

RIESGO OPERACIONAL
  · dirección de destino errónea: irreversible
  · pérdida de claves: irreversible
  · red congestionada: comisión y tiempo suben

RIESGO DE CUMPLIMIENTO
  la regla del viaje aplica igual a las transferencias
  de activos virtuales, y su implantación entre
  proveedores es desigual
  → un tramo sin la información exigida puede
    bloquear la salida en destino
```

### 4. Dónde tiene sentido y dónde no

La respuesta honesta a «¿sirve una stablecoin para este pago?» es «depende del
corredor». El bloque da los criterios de los dos lados, para que la decisión
se apoye en condiciones verificables y no en una preferencia previa.

```text
TIENE MÁS SENTIDO CUANDO
  · el corredor tiene pocos corresponsales o ninguno
  · hay diferencia horaria grande
  · el importe es mediano o alto (el coste fijo se diluye)
  · existe mercado líquido de entrada y salida
    en las dos puntas
  · el receptor puede recibir en cuenta o billetera

TIENE MENOS SENTIDO CUANDO
  · el corredor ya tiene un enlace de pagos inmediatos
    (clase 13: más barato y sin riesgo de emisor)
  · la salida local es ilíquida o cara
  · el importe es pequeño y el coste fijo domina
  · la jurisdicción de destino restringe la actividad
  · el receptor necesita efectivo en zona rural
```

### 5. Depósitos tokenizados: la alternativa que no es lo mismo

Un depósito tokenizado se parece por fuera a una stablecoin y es otra cosa por
dentro. El bloque marca las diferencias que importan y el intercambio que
propone: menos riesgo de emisor a cambio de menos acceso abierto.

```text
UN DEPÓSITO TOKENIZADO ES UN PASIVO BANCARIO
REPRESENTADO EN UN REGISTRO PROGRAMABLE

  frente a una stablecoin de emisor no bancario:
    · el riesgo es del banco, supervisado
    · está dentro del perímetro prudencial
    · puede tener garantía de depósitos
    · y NO circula libremente: se mueve entre
      participantes conocidos

  → resuelve buena parte del riesgo de emisor
    a cambio de perder el acceso abierto

  se estudia en la Parte 20, clase 8
```

## 🧮 Ejemplo guiado

El ejemplo compara el coste total de un corredor con y sin stablecoin. Conviene incluir entrada, salida y riesgo de emisor: el ahorro se reduce mucho.

**Situación.** Un operador compara dos rutas para un corredor sin enlace de pagos
inmediatos y con solo un corresponsal disponible.

```text
IMPORTE: 20 000 USD equivalentes
CORREDOR: país M → país N

RUTA CLÁSICA (corresponsalía)
  comisión de envío                    38,00 USD
  diferencial de cambio                185 pb
  comisión del intermediario           22,00 USD
  comisión del banco receptor          14,00 USD
  tiempo hasta disponibilidad          2,4 días
  prefinanciación necesaria            sí

RUTA CON STABLECOIN
  entrada: comisión                    0,35 %
  entrada: diferencial                 60 pb
  comisión de red                      0,04 USD
  salida: comisión                     0,45 %
  salida: diferencial                  95 pb
  comisión de retiro local             9,00 USD
  tiempo hasta disponibilidad          38 minutos
  tenencia media en stablecoin         22 minutos
```

**Paso 1 — calcula la ruta clásica.**

```text
comisión de envío                        38,00
diferencial: 20 000 × 1,85 %            370,00
comisión del intermediario               22,00
comisión del banco receptor              14,00
TOTAL                                   444,00 USD
SOBRE 20 000                              2,22 %
```

**Paso 2 — calcula la ruta con stablecoin.**

```text
entrada comisión: 20 000 × 0,35 %        70,00
entrada diferencial: 20 000 × 0,60 %    120,00
comisión de red                           0,04
salida comisión: 20 000 × 0,45 %         90,00
salida diferencial: 20 000 × 0,95 %     190,00
comisión de retiro local                  9,00
TOTAL                                   479,04 USD
SOBRE 20 000                              2,40 %
```

**Paso 3 — detente en el resultado.**

```text
LA RUTA CON STABLECOIN CUESTA 35,04 USD MÁS

  y sin embargo el tramo de transferencia
  costó 0,04 USD frente a los 22,00 del intermediario

  ¿DÓNDE SE FUE LA VENTAJA?
    entrada + salida = 470,00 USD
    frente a los 408,00 de diferencial y comisiones
    de la ruta clásica

  EL DIFERENCIAL COMBINADO DE ENTRADA Y SALIDA
  (60 + 95 = 155 pb) NO ES MUCHO MEJOR
  QUE EL DE LA RUTA CLÁSICA (185 pb)
```

**Paso 4 — valora lo que sí mejora.**

```text
TIEMPO
  2,4 días → 38 minutos

  ¿CUÁNTO VALE ESO?
    para una remesa familiar urgente: mucho
    para un pago a proveedor a 30 días: nada

PREFINANCIACIÓN
  la ruta clásica exige mantener saldo en el nostro
  supongamos 400 000 USD al 4,2 % = 16 800 USD/año
  con 1 200 operaciones al año: 14,00 USD por operación

  → si se imputa, la ruta clásica sube a 458,00 USD
  → la diferencia se reduce a 21,04 USD
```

**Paso 5 — valora el riesgo que se asume.**

```text
TENENCIA MEDIA: 22 MINUTOS

  exposición al emisor y a la paridad durante 22 minutos
  sobre 20 000 USD

  ESTIMACIÓN GRUESA
    si la probabilidad de un evento de paridad
    relevante en una ventana de 22 minutos es muy baja,
    la pérdida esperada es pequeña

  PERO LA DISTRIBUCIÓN NO ES NORMAL
    los episodios de pérdida de paridad documentados
    han sido bruscos y han durado horas o días.
    Si ocurre durante la tenencia, la pérdida
    puede ser de varios puntos porcentuales.

  Y HAY UN RIESGO PEOR
    si la salida se bloquea —por congestión, por
    cumplimiento o por el propio emisor— la tenencia
    de 22 minutos se convierte en días
    → la exposición no es la planificada,
      es la que resulte
```

**Paso 6 — analiza el caso donde sí gana.**

```text
CAMBIA UN SOLO PARÁMETRO: EL CORREDOR NO TIENE
CORRESPONSAL DISPONIBLE

  ruta clásica: hay que encadenar DOS intermediarios
    comisión adicional: +22,00
    diferencial adicional: +70 pb → +140,00
    tiempo: 4,1 días
    TOTAL: 606,00 USD = 3,03 %

  ruta con stablecoin: sin cambios
    TOTAL: 479,04 USD = 2,40 %

  AHORRO: 126,96 USD = 0,63 puntos

Y AHÍ ESTÁ LA CONCLUSIÓN REAL
  la ruta con stablecoin gana donde la cadena
  de corresponsales es LARGA, no donde es corta

  su ventaja es proporcional al número de eslabones
  que evita, no a la tecnología que usa
```

**Paso 7 — decide y escribe la regla.**

```text
REGLA DE ENRUTAMIENTO PROPUESTA

  SI existe enlace de pagos inmediatos
     → usarlo (más barato y sin riesgo de emisor)
  SI NO, Y la cadena clásica tiene ≤ 1 intermediario
     → ruta clásica
  SI NO, Y la cadena tiene ≥ 2 intermediarios
     Y hay mercado líquido de salida en destino
     Y la tenencia estimada es inferior a 60 minutos
     → ruta con stablecoin

  CONTROLES OBLIGATORIOS SI SE USA
    1. límite de exposición por emisor
    2. límite de tenencia: si supera 60 min, alertar
    3. procedimiento si la salida se bloquea
    4. verificación de la dirección de destino
       con lista blanca
    5. cumplimiento de la regla del viaje en el tramo
    6. evaluación del emisor según los criterios
       de la Parte 20

  Y UNA CONDICIÓN DE REVISIÓN
    si aparece un enlace de pagos inmediatos
    en el corredor, la regla lo prioriza
    automáticamente: la ruta con stablecoin
    es una respuesta a la ausencia de infraestructura,
    no una preferencia
```

**Interpreta:** la ruta con stablecoin costó más en el caso base y ganó al añadir
un eslabón a la cadena clásica. **El ahorro no venía del registro distribuido:
venía de evitar intermediarios**, y cualquier arquitectura que los evite produce
el mismo efecto. Es exactamente el criterio de la Parte 14, clase 9: identificar
la fuente real del ahorro antes de atribuirlo a la tecnología.

## 🧭 Perspectivas

El uso de stablecoins afecta a cada participante de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Remitente | Llega en 38 minutos | Si acepta el canal |
| Receptor | Necesita convertir a moneda local | Si hay salida líquida |
| Operador | Menos prefinanciación | Qué ruta usa por corredor |
| Banco | Exposición a un emisor no bancario | Si participa |
| Emisor de la stablecoin | Volumen de uso como medio de pago | Su política de redención |
| Banco central | Sustitución del canal bancario | Si vigila o restringe |
| Supervisor | Regla del viaje en el tramo | Qué exige al proveedor |
| GAFI | Trazabilidad de la transferencia | Guía sobre activos virtuales |

## 🏦 Del cliente al banco

El remitente ve una transferencia barata y el sistema tiene un emisor con riesgo de crédito propio. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Llegó en minutos» | Se evitó la cadena de corresponsales | 18, clase 14 |
| «No pude convertir a moneda local» | Salida ilíquida en destino | 18, clase 14 |
| «El valor cambió mientras esperaba» | Exposición a la paridad durante la tenencia | 20, clase 7 |
| «Mandé a la dirección equivocada» | Irreversible: no hay reclamación | 19, clase 3 |

## ⚖️ Riesgos y controles

Los riesgos son de emisor, de paridad y de cumplimiento. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Riesgo de emisor | El emisor no redime a la par | Límite por emisor y evaluación previa |
| Pérdida de paridad | El valor se aparta durante la tenencia | Límite de tiempo en tenencia |
| Salida bloqueada | Congestión, cumplimiento o emisor | Procedimiento y ruta alternativa |
| Dirección errónea | Transferencia irreversible | Lista blanca y verificación |
| Regla del viaje incumplida | El tramo no lleva los datos | Verificación antes de enviar |
| Atribución errónea del ahorro | Se acredita a la tecnología | Identificar la fuente real |

## 🧪 Práctica

El laboratorio pide comparar el coste total de un corredor por ambas vías. El coste de entrada y salida es lo que decide.

En [`labs/lab-08.md`](../labs/lab-08.md):

1. Traza los cinco tramos de una ruta con stablecoin y asigna coste a cada uno.
2. Compara con la ruta clásica sobre la misma base, incluida la prefinanciación.
3. Modela el efecto de añadir un intermediario a la cadena clásica.
4. Escribe la regla de enrutamiento con sus controles y su condición de revisión.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen expectativas incumplidas con stablecoins. La causa es haber comparado solo el tramo intermedio.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Comparar el tramo intermedio con la ruta entera | Se aisló lo favorable | Compara ruta completa con ruta completa |
| «Elimina intermediarios» | Se ignoraron entrada y salida | Los sustituye por otros |
| Ignorar la prefinanciación clásica | No se imputó | Impútala por operación |
| Suponer la tenencia planificada | Se ignoró el bloqueo de salida | La exposición es la que resulte |
| Atribuir el ahorro al registro | Se leyó el titular | El ahorro viene de evitar eslabones |
| Usarla donde hay enlace directo | Se prefirió por novedad | El enlace es más barato y sin emisor |

## ❓ Preguntas de comprobación

1. ¿Cuáles son los cinco tramos de una ruta con stablecoin y cuál es el más
   barato?
2. ¿Por qué la ruta no elimina intermediarios?
3. ¿Qué riesgo sustituye al del corresponsal, y de qué depende su magnitud?
4. En el ejemplo guiado, ¿qué cambió para que la ruta pasara a ganar?
5. ¿Por qué un enlace de pagos inmediatos se prefiere a esta ruta cuando existe?

## 📥 Entregable

Guarda en `portfolio/parte-18/clase-14/`:

- los cinco tramos con su coste asignado;
- la comparación completa con la ruta clásica, con prefinanciación imputada;
- el análisis de sensibilidad al número de intermediarios;
- la regla de enrutamiento con sus seis controles y su condición de revisión.

## 🔗 Referencias cruzadas

- **Viene de:** clases 5, 9, 12 y 13; Parte 14, clase 9 (criptoactivos).
- **Continúa en:** clase 15 (pago contra pago); **Parte 20** (diseño, reservas y
  regulación de stablecoins).
- **Se aplica en:** Parte 21, clase 15; Parte 23, clases 8 y 10.

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

- Financial Stability Board (2023). *High-level Recommendations for the Regulation, Supervision and Oversight of Global Stablecoin Arrangements*. FSB. <https://www.fsb.org/2023/07/high-level-recommendations-for-the-regulation-supervision-and-oversight-of-global-stablecoin-arrangements-final-report/>
- Committee on Payments and Market Infrastructures e IOSCO (2022). *Application of the Principles for Financial Market Infrastructures to stablecoin arrangements*. BIS. <https://www.bis.org/cpmi/publ/d206.htm>
- Financial Action Task Force. *Updated Guidance for a Risk-Based Approach to Virtual Assets and VASPs*. FATF. <https://www.fatf-gafi.org/>
- Bank for International Settlements (2023). *Annual Economic Report*, capítulo sobre el sistema monetario del futuro. BIS. <https://www.bis.org/publ/arpdf/ar2023e3.htm>
- Committee on Payments and Market Infrastructures (2021). *Central bank digital currencies for cross-border payments*. BIS. <https://www.bis.org/publ/othp38.htm>
- Verificación local: comprueba si tu jurisdicción admite el uso de stablecoins como medio de pago, qué licencia exige al proveedor de entrada y salida y cómo aplica la regla del viaje a las transferencias de activos virtuales. **Fecha de verificación de esta clase: 2026-08-06.** Esta clase no constituye asesoría legal ni recomendación de inversión.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 13 · Interconexión de sistemas de pagos inmediatos](13-interconexion-de-pagos-inmediatos.md) | [Parte 18](../README.md) · [Programa](../../../SYLLABUS.md) | [15 · Payment versus Payment y liquidación atómica →](15-payment-versus-payment-y-liquidacion-atomica.md) |
<!-- gen:footer:end -->
