<!-- meta
part: 18
class: 9
title: "El cambio de divisa dentro de un pago"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global, chile]
regulatory_topics: [cross-border-payments, fx, transparencia, cambios-internacionales]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [Banco Central de Chile, CPMI]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 09 · El cambio de divisa dentro de un pago

> [← 08 · Liquidez, prefinanciación, netting y horarios](08-liquidez-prefinanciacion-y-netting.md) · [Índice de la parte](../README.md) · [10 · Remesas y corredores internacionales →](10-remesas-y-corredores-internacionales.md)

**Parte 18 — Pagos transfronterizos, remesas y liquidación internacional** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Aislar el componente de cambio de divisa dentro de un pago y aprender a medirlo.
El diferencial es el coste que no aparece como comisión y, en la mayoría de los
corredores minoristas, es el mayor de todos.

Casi todo pago transfronterizo cambia de moneda en algún punto. Esta clase abre ese tramo, y encuentra el ingreso que no aparece como comisión y que suele superarla: el margen sobre el tipo de referencia.

## 📚 Objetivos

Al finalizar podrás:

1. **Descomponer** un tipo aplicado en tipo de referencia más diferencial.
2. **Calcular** el diferencial en puntos básicos y compararlo entre rutas.
3. **Identificar** quién asume el riesgo de cambio en cada momento del pago.
4. **Distinguir** el diferencial legítimo del margen no revelado.
5. **Diseñar** una política de precios de cambio que se pueda defender.

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

Los cuatro primeros términos son el precio de la divisa y su medida; los cuatro siguientes, el riesgo y su cobertura. El **diferencial** es donde está el ingreso invisible: el margen sobre el tipo de referencia no aparece como comisión y suele superarla con holgura.

| Concepto | Comprensión verificable |
|---|---|
| `tipo de referencia` | Tipo medio de mercado en un instante, sin margen |
| `diferencial` | Diferencia entre el tipo aplicado y el de referencia |
| `punto básico` | Una centésima de punto porcentual |
| `tipo cruzado` | Tipo entre dos divisas calculado a través de una tercera |
| `riesgo de cambio` | Riesgo de que el tipo se mueva antes de liquidar |
| `cobertura` | Operación que elimina o reduce ese riesgo |
| `tipo garantizado` | Tipo comprometido al cliente antes de liquidar |
| `mercado cambiario formal` | Conjunto de entidades autorizadas a operar cambios en una jurisdicción |

## 🧠 Modelo mental

El modelo mental es un precio con dos componentes: el tipo de referencia, que es público, y el diferencial, que no lo es. Comparar proveedores por comisión sin mirar el diferencial es comparar la parte pequeña.

```text
TODO PAGO CON CAMBIO TIENE TRES PRECIOS
Y EL CLIENTE SOLO VE UNO

  TIPO DE REFERENCIA   lo que vale la divisa en el mercado
  TIPO MAYORISTA       lo que le cuesta al banco comprarla
  TIPO APLICADO        lo que el banco cobra al cliente

  margen del banco = tipo aplicado − tipo mayorista
  coste del cliente = tipo aplicado − tipo de referencia

LA CONFUSIÓN ÚTIL PARA QUIEN VENDE
  «sin comisiones» significa que el margen
  está TODO en el diferencial

  no significa que sea gratis: significa
  que no se puede ver
```

## 📖 Desarrollo

### 1. Cómo se mide un diferencial

```text
TIPO DE REFERENCIA:  1 USD = 950,00 CLP
TIPO APLICADO:       1 USD = 978,00 CLP

DIFERENCIAL ABSOLUTO
  978,00 − 950,00 = 28,00 CLP por USD

Y AQUÍ ESTÁ LA TRAMPA DE LA BASE
  28,00 / 950,00 = 2,947 %
  ese número mide el encarecimiento de la COTIZACIÓN,
  no la pérdida del CLIENTE

  el cliente entrega pesos y recibe dólares:
  lo que pierde es
     1 − 950/978 = 2,8629 %

  MIDE SIEMPRE SOBRE LA MAGNITUD QUE EL CLIENTE RECIBE
  (dólares por peso), no sobre la que el banco cotiza
  (pesos por dólar). Con diferenciales pequeños las dos
  cifras se parecen; con diferenciales grandes, no.

DIFERENCIAL EN PUNTOS BÁSICOS
  2,8629 % × 100 = 286,3 pb

POR QUÉ SE USAN PUNTOS BÁSICOS
  permiten comparar corredores con tipos muy distintos.
  «286,3 pb» significa lo mismo en CLP/USD que en JPY/EUR.
```

### 2. El tipo cruzado y dónde se esconde el doble margen

```text
UN PAGO CLP → PHP SUELE PASAR POR USD

  CLP → USD → PHP

  si el banco aplica margen en las DOS patas,
  el cliente paga dos diferenciales

TIPO CRUZADO DE REFERENCIA
  1 CLP = (1/950) USD
  1 USD = 56,00 PHP
  1 CLP = 56,00/950 = 0,058947 PHP

TIPO CRUZADO APLICADO
  1 CLP = (1/978) USD = 0,00102249 USD
  1 USD = 54,60 PHP
  1 CLP = 0,00102249 × 54,60 = 0,055828 PHP

DIFERENCIAL TOTAL
  (0,058947 − 0,055828) / 0,058947 = 5,291 % = 529,1 pb

  NO ES LA SUMA DE LOS DOS (286,3 + 250 = 536,3)
  ES EL PRODUCTO COMPUESTO, sobre la base del cliente:
  1 − (1 − 0,028629) × (1 − 0,025) = 5,291 %  ✓

  Y COMPRUÉBALO: el cálculo directo del cruzado da
  exactamente lo mismo. Si tu composición no cuadra
  con el cálculo directo, has medido sobre la base
  equivocada en alguna de las dos patas.
```

### 3. Quién asume el riesgo de cambio y cuándo

```text
LÍNEA DE TIEMPO DE UN PAGO CON CAMBIO

  T0  el cliente ve un tipo en pantalla
  T1  el cliente confirma la orden
  T2  el banco ejecuta la compra de divisa
  T3  el pago se liquida
  T4  el beneficiario recibe

  ENTRE T0 Y T1  riesgo del banco si garantiza el tipo,
                 del cliente si es indicativo
  ENTRE T1 Y T2  riesgo del banco: ya se comprometió
  ENTRE T2 Y T3  ninguno: la divisa ya se compró
  ENTRE T3 Y T4  ninguno en cambio; sí en liquidación

LA PREGUNTA QUE HAY QUE HACER SIEMPRE
  «el tipo que veo, ¿es garantizado o indicativo,
   y hasta cuándo?»
  si la respuesta no está en pantalla, es indicativo
```

### 4. Diferencial legítimo y margen no revelado

```text
UN DIFERENCIAL CUBRE COSTES REALES
  · riesgo de mercado entre T1 y T2
  · coste de la propia operación mayorista
  · coste operativo del servicio
  · margen de la entidad

ESO ES LEGÍTIMO. LO QUE NO LO ES:
  · presentar el servicio como «sin comisiones»
    cuando todo el precio está en el diferencial
  · aplicar un tipo distinto del mostrado, sin avisar
  · aplicar el tipo del peor momento del día
  · cambiar el tipo entre la confirmación y la ejecución
    sin que el cliente pueda cancelar

LA PRUEBA DE TRANSPARENCIA
  ¿puede el cliente saber, ANTES de confirmar,
  cuánto recibirá exactamente el beneficiario?
  si no, el precio no es comparable
```

### 5. El mercado cambiario formal

```text
MUCHAS JURISDICCIONES DEFINEN QUIÉN PUEDE
REALIZAR OPERACIONES DE CAMBIO Y BAJO QUÉ REGLAS

  · qué entidades están autorizadas
  · qué operaciones deben informarse
  · qué documentación respalda cada operación
  · qué plazos de información aplican

CONSECUENCIA PARA UN PRODUCTO DE PAGOS
  ofrecer conversión de divisa puede constituir
  una actividad regulada distinta de la de pagos

  → hay que verificar, no suponer
  → y la respuesta cambia por jurisdicción
```

## 🧮 Ejemplo guiado

El ejemplo descompone el precio de un cambio en referencia y diferencial. Conviene expresar el diferencial en puntos básicos: comparado así, la diferencia entre proveedores es evidente.

**Situación.** Una empresa de pagos revisa su política de precios de cambio. Le
acusan de opacidad y quiere responder con datos.

```text
CORREDOR CLP → USD, ÚLTIMO TRIMESTRE
  operaciones                     18 400
  volumen                        4 200 000 000 CLP
  ingreso por comisión explícita     0 CLP  («sin comisiones»)
  ingreso por diferencial       118 900 000 CLP

  diferencial medio aplicado        283 pb
  coste mayorista medio del banco    41 pb
  coste operativo por operación   1 900 CLP

COMPETENCIA
  competidor A: comisión 4 900 CLP + 95 pb
  competidor B: sin comisión + 310 pb
  competidor C: comisión 2 500 CLP + 180 pb
```

**Paso 1 — calcula el margen bruto real.**

```text
DIFERENCIAL MEDIO         283 pb
COSTE MAYORISTA            41 pb
MARGEN BRUTO SOBRE FX     242 pb

VOLUMEN × MARGEN
  4 200 000 000 × 2,42 % = 101 640 000 CLP

COSTE OPERATIVO
  18 400 × 1 900 = 34 960 000 CLP

MARGEN NETO
  101 640 000 − 34 960 000 = 66 680 000 CLP
  por operación: 3 624 CLP
```

**Paso 2 — construye el precio efectivo comparable.**

```text
PARA COMPARAR HAY QUE FIJAR UN IMPORTE.
TICKET MEDIO: 4 200 000 000 / 18 400 = 228 261 CLP

  NUESTRO PRECIO
    0 + 228 261 × 2,83 % = 6 460 CLP

  COMPETIDOR A
    4 900 + 228 261 × 0,95 % = 4 900 + 2 168 = 7 068 CLP

  COMPETIDOR B
    0 + 228 261 × 3,10 % = 7 076 CLP

  COMPETIDOR C
    2 500 + 228 261 × 1,80 % = 2 500 + 4 109 = 6 609 CLP

EN EL TICKET MEDIO SOMOS LOS MÁS BARATOS
```

**Paso 3 — comprueba si eso se sostiene en todo el rango.**

```text
PRECIO EFECTIVO SEGÚN IMPORTE

  importe      nosotros    A         B         C
   50 000        1 415     5 375     1 550     3 400
  228 261        6 460     7 068     7 076     6 609
  500 000       14 150     9 650    15 500    11 500
2 000 000       56 600    23 900    62 000    38 500

EL HALLAZGO
  somos los más baratos hasta ~300 000 CLP
  y los más caros —después de B— por encima

  el 71 % de nuestras operaciones está bajo 300 000
  y el 6 % está sobre 1 000 000

  ese 6 % aporta el 38 % del volumen
  y es donde somos claramente peores
```

**Paso 4 — enfrenta la acusación de opacidad.**

```text
LA ACUSACIÓN NO ES SOBRE EL PRECIO: ES SOBRE
QUE NO SE PUEDE COMPARAR

  «sin comisiones» es literalmente cierto
  y hace imposible que el cliente calcule su coste

  LA PRUEBA
    ¿puede un cliente saber, antes de confirmar,
    cuánto recibirá el beneficiario? SÍ, lo mostramos.
    ¿puede saber cuánto le estamos cobrando? NO,
    porque no publicamos el tipo de referencia.

  → la información existe pero no es COMPARABLE
```

**Paso 5 — evalúa publicar el diferencial.**

```text
OPCIÓN · mostrar «tipo de referencia», «tipo aplicado»
         y «coste total» en cada operación

  RIESGO COMERCIAL
    en el tramo alto quedamos peor que A y C
    supuesto: perdemos el 25 % de las operaciones
    sobre 1 000 000

    volumen perdido: 4 200 000 000 × 38 % × 25 %
                   = 399 000 000 CLP
    margen perdido: 399 000 000 × 2,42 % = 9 656 000 CLP
    menos coste operativo evitado: 276 × 1 900 = 524 400
    PÉRDIDA NETA ≈ 9 131 600 CLP por trimestre

  BENEFICIO
    difícil de cuantificar en ingreso directo:
    confianza, defensa ante el supervisor,
    y evitar una obligación impuesta más adelante
    en peores términos
```

**Paso 6 — busca la respuesta que no es binaria.**

```text
NO ES «PUBLICAR O NO PUBLICAR».
ES «QUÉ PRECIO TENEMOS QUE PODER DEFENDER».

  PROBLEMA REAL
    un diferencial plano de 283 pb cobra lo mismo
    en porcentaje a quien envía 50 000 que a quien
    envía 2 000 000, cuando el coste operativo
    es el MISMO en ambos casos (1 900 CLP)

  ESTRUCTURA DE PRECIO COHERENTE CON EL COSTE
    componente fijo: cubre el coste operativo
    componente variable: cubre el riesgo y el margen

  PROPUESTA
    comisión fija 2 200 CLP
    + diferencial 120 pb

  PRECIO RESULTANTE
    importe      nuevo      antes
     50 000       2 800     1 415
    228 261       4 939     6 460
    500 000       8 200    14 150
  2 000 000      26 200    56 600
```

**Paso 7 — evalúa el cambio de estructura.**

```text
INGRESO CON LA NUEVA ESTRUCTURA (mismo volumen)
  fijo:      18 400 × 2 200 = 40 480 000
  variable:  4 200 000 000 × 1,20 % = 50 400 000
  TOTAL                        90 880 000
  antes                       101 640 000
  DIFERENCIA                  −10 760 000 por trimestre

PERO
  el tramo alto pasa de ser el peor precio del mercado
  al mejor: recuperación esperada de volumen
  supuesto: +40 % de operaciones sobre 1 000 000

  volumen adicional: 4 200 000 000 × 38 % × 40 %
                   = 638 400 000 CLP
  margen adicional: 638 400 000 × 1,20 % = 7 660 800
  fijo adicional: 442 × 2 200 = 972 400
  coste operativo adicional: 442 × 1 900 = 839 800
  NETO ADICIONAL: 7 793 400

RESULTADO: −10 760 000 + 7 793 400 = −2 966 600
```

**Paso 8 — decide.**

```text
LA NUEVA ESTRUCTURA CUESTA ~3 MILLONES POR TRIMESTRE
Y COMPRA TRES COSAS

  1. un precio que se puede publicar y defender
  2. una estructura coherente con el coste real
  3. la posición competitiva en el tramo alto,
     que es donde está el 38 % del volumen y el
     crecimiento

DECISIÓN: adoptarla, con publicación del tipo de
referencia y del coste total en cada operación

CONDICIONES
  · medir la elasticidad real a 90 días,
    no quedarse con el supuesto del 40 %
  · si la recuperación de volumen es menor del 20 %,
    revisar el componente fijo
  · verificar antes si la conversión de divisa
    constituye actividad regulada distinta en cada
    jurisdicción donde operamos

Y UNA NOTA DE MÉTODO
  el supuesto del 40 % de recuperación es el número
  más frágil del análisis y el que decide el signo
  del resultado. Se declara como tal.
```

**Interpreta:** la acusación era de opacidad y el análisis reveló un problema
distinto: **un precio plano sobre un coste que no lo es**. La transparencia
obligaba a arreglar la estructura, no solo a publicarla.

## 🧭 Perspectivas

El cambio de divisa afecta a cada participante de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | «Sin comisiones» | Si compara o confía |
| Empresa que paga a proveedores | Coste alto en importes grandes | Si cambia de proveedor |
| Banco | Margen en el diferencial | Cómo estructura el precio |
| Competidor | Precio no comparable | Si publica el suyo |
| Banco central | Operaciones de cambio | Qué informa y quién puede operar |
| Supervisor de conducta | Precio no comparable | Si exige revelar |
| Sociedad | Coste de las remesas | Presión regulatoria |

## 🏦 Del cliente al banco

El cliente ve un tipo y el banco cobra un diferencial sobre la referencia. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Dice sin comisiones» | Todo el precio está en el diferencial | 18, clase 9 |
| «El tipo cambió al confirmar» | Tipo indicativo, no garantizado | 18, clase 9 |
| «Envío grande, precio malo» | Diferencial plano sobre coste fijo | 18, clase 9 |
| «No sé cuánto llega» | Sin tipo de referencia no hay comparación | 18, clases 1 y 9 |

## ⚖️ Riesgos y controles

Los riesgos son de precio y de exposición cambiaria. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Precio no comparable | «Sin comisiones» con diferencial alto | Publicar referencia y coste total |
| Tipo cambiado tras confirmar | Se aplica el del momento de ejecutar | Tipo garantizado con ventana declarada |
| Doble margen en el cruzado | Se cobra en las dos patas | Revelar el diferencial total |
| Riesgo de mercado no cubierto | Se garantiza el tipo sin cobertura | Política de cobertura por importe |
| Actividad no autorizada | Se convierte divisa sin permiso | Verificar el perímetro por jurisdicción |
| Precio incoherente con el coste | Diferencial plano | Componente fijo más variable |

## 🧪 Práctica

El laboratorio pide descomponer el precio de varios proveedores en referencia y diferencial. El orden por comisión y el orden por coste total no coinciden.

En [`labs/lab-05.md`](../labs/lab-05.md):

1. Descompón cinco tipos aplicados en referencia y diferencial, en pb.
2. Calcula el diferencial compuesto de un tipo cruzado.
3. Construye la tabla de precio efectivo por importe frente a tres competidores.
4. Propón una estructura de precio coherente con el coste y evalúa su efecto.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen cambios más caros de lo esperado. La causa es el diferencial no cotizado.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Sumar diferenciales del cruzado | Se trataron como aditivos | Se componen multiplicativamente |
| Comparar solo comisiones | El diferencial no se vio | Precio efectivo por importe |
| Diferencial plano | No se separó coste fijo de variable | Fijo más variable |
| «Sin comisiones» como argumento | Se confundió con gratuito | Publica el coste total |
| Tipo indicativo sin decirlo | No se declaró la garantía | Indica hasta cuándo vale |
| Suponer que se puede convertir | No se verificó el perímetro | Comprueba por jurisdicción |

## ❓ Preguntas de comprobación

1. ¿Cómo se calcula un diferencial en puntos básicos y por qué se usa esa unidad?
2. ¿Por qué el diferencial de un tipo cruzado no es la suma de los dos?
3. ¿Quién asume el riesgo de cambio entre la confirmación y la ejecución?
4. ¿Cuál es la prueba de que un precio de cambio es comparable?
5. En el ejemplo guiado, ¿por qué un diferencial plano era incoherente con el
   coste?

## 📥 Entregable

Guarda en `portfolio/parte-18/clase-09/`:

- la descomposición de cinco tipos aplicados, en puntos básicos;
- el cálculo de un diferencial cruzado compuesto;
- la tabla de precio efectivo por importe frente a tres alternativas;
- una propuesta de estructura de precio con su efecto y sus supuestos frágiles
  señalados.

## 🔗 Referencias cruzadas

- **Viene de:** clase 1 (coste total); Parte 7, clase 12 (mercado de divisas).
- **Continúa en:** clase 10 (remesas), clase 15 (pago contra pago).
- **Se aplica en:** Parte 21, clases 13 y 14 (FX on-chain); Parte 23, clase 9.

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

- Banco Mundial. *Remittance Prices Worldwide: metodología de cálculo del coste total*. <https://remittanceprices.worldbank.org/>
- Bank for International Settlements (2022). *Triennial Central Bank Survey of foreign exchange and OTC derivatives markets*. BIS. <https://www.bis.org/statistics/rpfx22.htm>
- Committee on Payments and Market Infrastructures (2018). *Cross-border retail payments*. BIS. <https://www.bis.org/cpmi/publ/d173.htm>
- Global Foreign Exchange Committee. *FX Global Code*. <https://www.globalfxc.org/fx_global_code.htm>
- Banco Central de Chile. *Compendio de Normas de Cambios Internacionales y Mercado Cambiario Formal*. <https://www.bcentral.cl/>
- Verificación local: comprueba quién puede realizar operaciones de cambio en tu jurisdicción, qué debe informarse y qué obligaciones de transparencia de precio existen. **Fecha de verificación de esta clase: 2026-08-06.** Esta clase no constituye asesoría legal ni recomendación de inversión.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 08 · Liquidez, prefinanciación, netting y horarios](08-liquidez-prefinanciacion-y-netting.md) | [Parte 18](../README.md) · [Programa](../../../SYLLABUS.md) | [10 · Remesas y corredores internacionales →](10-remesas-y-corredores-internacionales.md) |
<!-- gen:footer:end -->
