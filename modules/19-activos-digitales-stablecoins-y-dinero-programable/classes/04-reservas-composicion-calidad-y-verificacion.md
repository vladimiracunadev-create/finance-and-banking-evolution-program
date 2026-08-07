---
part: 20
class: 4
title: "Reservas: composición, calidad y verificación"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional, union-europea]
regulatory_topics: [reservas, liquidez, atestacion]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [FSB, CPMI, IOSCO]
requires_legal_review: true
---

<!-- gen:header:start -->
# Clase 04 · Reservas: composición, calidad y verificación

> [← 03 · Stablecoins: tipologías y mecánica de la paridad](03-stablecoins-tipologias-y-mecanica-de-la-paridad.md) · [Índice de la parte](../README.md) · [05 · Redención: el derecho, el proceso y la cola →](05-redencion-el-derecho-el-proceso-y-la-cola.md)

**Parte 20 — Activos digitales, stablecoins y dinero programable** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Analizar la cartera que respalda una stablecoin como lo que es: **una cartera de
inversión con un pasivo exigible a la vista**. El problema no es cuánto vale la
reserva, sino cuánto vale **el día en que todos redimen a la vez**.

La paridad de la clase anterior se sostiene sobre una reserva. Esta la abre, y establece la distinción que produce las corridas: tener activos suficientes no es lo mismo que poder convertirlos a tiempo.

## 📚 Objetivos

Al finalizar podrás:

1. **Descomponer** una cartera de reservas por instrumento, plazo y emisor.
2. **Calcular** la cobertura contable y la cobertura líquida a un día.
3. **Cuantificar** el descuento por venta forzada de cada tramo.
4. **Distinguir** atestación, revisión y auditoría, y qué asegura cada una.
5. **Detectar** el descalce de plazo que un porcentaje de cobertura oculta.

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

Los cuatro primeros términos son las dos coberturas y sus descalces; los cuatro siguientes, la protección jurídica y su verificación. La distinción entre **cobertura contable y líquida** es la clave: tener activos por el cien por cien no significa poder redimir hoy, y esa diferencia es la que produce las corridas.

| Concepto | Comprensión verificable |
|---|---|
| `cobertura contable` | Valor de la reserva dividido por el circulante |
| `cobertura líquida` | Parte convertible en efectivo en un plazo dado |
| `descalce de plazo` | Pasivo a la vista frente a activo a plazo |
| `descuento por venta forzada` | Pérdida al vender rápido y en volumen |
| `segregación` | Separación jurídica de la reserva del patrimonio del emisor |
| `atestación` | Informe sobre una afirmación en una fecha |
| `auditoría` | Opinión sobre estados financieros con alcance normado |
| `concentración` | Peso del mayor emisor o de la mayor contraparte |

## 🧠 Modelo mental

El modelo mental son dos preguntas distintas sobre la misma reserva: si vale lo suficiente y si se puede convertir a tiempo. Una reserva de bonos a diez años cubre la primera y falla la segunda.

```text
UNA RESERVA TIENE TRES CIFRAS, Y SOLO SE PUBLICA LA PRIMERA

  1 CUÁNTO VALE HOY
      la que aparece en el informe mensual
      cobertura del 101 %, 102 %...

  2 CUÁNTO SE OBTIENE MAÑANA
      si hay que convertir todo en efectivo
      en 24 horas, vendiendo en el mercado

  3 QUIÉN COBRA SI EL EMISOR QUIEBRA
      depende de la segregación, no del valor

LA CIFRA 1 PUEDE SER 102 %
Y LA CIFRA 2 SER 91 %
SIN QUE NADIE HAYA MENTIDO
```

## 📖 Desarrollo

### 1. Composición y qué significa cada tramo

| Instrumento | Liquidez a 1 día | Riesgo principal |
|---|---|---|
| Efectivo en banco central | Total | Ninguno relevante |
| Depósito bancario a la vista | Alta | Crédito del banco depositario |
| Deuda pública muy corta | Alta | Precio si hay que vender en tensión |
| Deuda pública a plazo | Media | Tipo de interés y precio |
| Pacto de recompra inverso | Media | Contraparte y garantía |
| Papel comercial | Baja en tensión | Crédito y liquidez |
| Fondo de mercado monetario | Media | Reglas de reembolso del propio fondo |
| Depósito a plazo | Muy baja | Penalización por cancelación |
| Otros activos | Variable | El que sea, y hay que decirlo |

### 2. El descalce que el porcentaje oculta

```text
DOS RESERVAS CON LA MISMA COBERTURA DEL 102 %

  RESERVA A                      RESERVA B
  70 % efectivo y letras         20 % efectivo
  30 % deuda 3 meses             45 % deuda 2 años
                                 25 % papel comercial
                                 10 % depósitos a plazo

  MISMA CIFRA PUBLICADA. RIESGO DISTINTO.

  ANTE UNA REDENCIÓN DEL 30 % EN UN DÍA
    A vende letras con descuento mínimo
    B tiene que vender deuda larga y papel
      comercial en un mercado que ya está tenso
```

### 3. Descuento por venta forzada

```text
EL PRECIO DE PANTALLA NO ES EL PRECIO DE VENTA

  vender 50 millones de letras         ≈ sin impacto
  vender 400 millones de deuda 2 años  ≈ impacto visible
  vender papel comercial en tensión    ≈ puede no haber
                                          comprador

REGLA DE TRABAJO
  aplicar un descuento por tramo
  y por tamaño relativo al mercado

  el descuento NO es una opinión pesimista:
  es la diferencia entre valorar y realizar
```

### 4. Atestación, revisión y auditoría

```text
NO SON LO MISMO Y LA DIFERENCIA ES GRANDE

  ATESTACIÓN
    un profesional informa sobre una afirmación
    de la dirección, en UNA FECHA CONCRETA
    · no dice nada del día anterior ni del siguiente
    · el alcance lo define el encargo
    · puede excluir la valoración o la titularidad

  REVISIÓN LIMITADA
    procedimientos menos extensos que una auditoría
    conclusión en negativo: «no hemos detectado»

  AUDITORÍA DE ESTADOS FINANCIEROS
    opinión sobre unos estados completos,
    con normas de auditoría y responsabilidad

QUÉ PREGUNTAR SIEMPRE
  1 ¿qué se atestigua exactamente?
  2 ¿a qué fecha, y qué pasó los días alrededor?
  3 ¿quién eligió la fecha?
  4 ¿se verificó la TITULARIDAD, no solo el saldo?
  5 ¿se verificó que no estaban pignorados?
```

### 5. Segregación

```text
LA PREGUNTA QUE SOLO IMPORTA EN LA QUIEBRA

  ¿LA RESERVA ESTÁ EN EL PATRIMONIO DEL EMISOR?
    sí  → los tenedores son acreedores ordinarios
          y comparten con todos los demás
    no  → hay separación patrimonial y los
          tenedores cobran de esa masa

  ¿DÓNDE ESTÁ DEPOSITADA?
    un banco, un custodio, varios
    → el riesgo del depositario es riesgo real
      y se ha materializado en el pasado

  ¿ESTÁ PIGNORADA O PRESTADA?
    una reserva prestada rinde más
    y responde peor
```

## 🧮 Ejemplo guiado

El ejemplo calcula la cobertura líquida de una reserva con descuento por venta forzada. La diferencia con la cobertura contable es la exposición real.

**Situación.** Un emisor publica una cobertura del 102,3 %. Hay que calcular qué
queda tras una redención del 35 % en 24 horas.

```text
CIRCULANTE               8 400 000 000
RESERVA DECLARADA        8 593 200 000   (102,30 %)

COMPOSICIÓN
  efectivo en bancos           840 000 000    9,8 %
  letras ≤ 3 meses           3 010 000 000   35,0 %
  deuda pública 1–2 años     2 580 000 000   30,0 %
  pactos de recompra inverso   860 000 000   10,0 %
  papel comercial              945 000 000   11,0 %
  depósitos a plazo 6 meses    358 200 000    4,2 %
```

**Paso 1 — clasifica por disponibilidad a 24 horas.**

```text
DISPONIBLE SIN VENDER
  efectivo                        840 000 000

DISPONIBLE VENDIENDO
  letras ≤ 3 meses              3 010 000 000
  deuda 1–2 años                2 580 000 000
  pactos inversos (vencen)        860 000 000

NO DISPONIBLE EN 24 HORAS
  papel comercial                 945 000 000
  depósitos a plazo               358 200 000
  → 1 303 200 000 fuera de juego
```

**Paso 2 — calcula la necesidad de efectivo.**

```text
REDENCIÓN DEL 35 % DEL CIRCULANTE
  8 400 000 000 × 35 % = 2 940 000 000
```

**Paso 3 — aplica descuentos por venta forzada.**

```text
SUPUESTOS DE DESCUENTO (declarados, no observados)

  letras ≤ 3 meses              0,15 %
  deuda 1–2 años                1,40 %
  pactos inversos               0,00 %  (vencen)

VALOR REALIZABLE
  efectivo                  840 000 000
  letras     3 010 000 000 × 99,85 % = 3 005 485 000
  pactos                    860 000 000
  deuda      2 580 000 000 × 98,60 % = 2 543 880 000

  TOTAL REALIZABLE A 24 h = 7 249 365 000
```

**Paso 4 — comprueba si cubre la redención.**

```text
NECESIDAD          2 940 000 000
REALIZABLE         7 249 365 000

COBERTURA DE LA REDENCIÓN: 246 %
→ SOPORTA EL ESCENARIO
```

**Paso 5 — calcula el orden de venta y su coste.**

```text
UN GESTOR PRUDENTE NO VENDE TODO:
VENDE LO JUSTO, EMPEZANDO POR LO BARATO

  efectivo                       840 000 000
  pactos que vencen              860 000 000
  subtotal                     1 700 000 000

  falta                        1 240 000 000
  se vende en letras: 1 240 000 000 / 0,9985
                    = 1 241 862 794 nominales

  COSTE DE LA VENTA
  1 241 862 794 − 1 240 000 000 = 1 862 794

  → 1,86 millones, un 0,063 % de lo redimido
```

**Paso 6 — mira la cobertura del remanente.**

```text
TRAS LA REDENCIÓN

  circulante  8 400 000 000 − 2 940 000 000
            = 5 460 000 000

  reserva     8 593 200 000 − 2 940 000 000
                            − 1 862 794
            = 5 651 337 206

  cobertura = 103,50 %

LA COBERTURA SUBIÓ.
¿ES BUENA NOTICIA?

  NO NECESARIAMENTE: la composición empeoró
```

**Paso 7 — recalcula la composición del remanente.**

```text
QUEDA
  efectivo                              0
  letras         3 010 000 000 − 1 241 862 794
               = 1 768 137 206         31,3 %
  deuda 1–2 años 2 580 000 000          45,7 %
  papel comercial  945 000 000          16,7 %
  depósitos plazo  358 200 000           6,3 %

  EFECTIVO: CERO
  ILÍQUIDO: 23,0 % frente al 15,2 % inicial

UNA SEGUNDA REDENCIÓN DEL 35 %
  necesidad = 5 460 000 000 × 35 % = 1 911 000 000
  realizable a 24 h:
    letras  1 768 137 206 × 99,85 % = 1 765 484 000
    deuda   2 580 000 000 × 98,60 % = 2 543 880 000
    → 4 309 364 000, aún cubre

  PERO EL DESCUENTO YA NO SERÍA 1,40 %:
  vender 2 580 millones de deuda en un mercado
  que sabe que hay una corrida es otra cosa
```

**Interpreta:** el emisor sobrevive al escenario, y sin embargo su reserva sale
**peor de lo que entró**: sin efectivo y con más peso ilíquido, mientras la
cobertura publicada mejora del 102,3 % al 103,5 %. **La cifra que se publica se
mueve en dirección contraria al riesgo real**, y por eso una ficha de reservas
tiene que incluir composición y plazo, no solo el porcentaje.

## 🧭 Perspectivas

La composición de la reserva afecta a cada participante de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | «102 %, está sobrecubierto» | Si confía |
| Fintech | Un instrumento de tesorería | Si lo usa para saldos operativos |
| Banco | Riesgo indirecto del depositario | Qué límites pone |
| Emisor | Rendimiento de la reserva | Qué plazo asume |
| Custodio | Titularidad y pignoración | Qué certifica |
| Auditor | Alcance del encargo | Qué puede afirmar |
| Mercado | Un informe mensual | Cómo lo interpreta |
| Supervisor | Composición y descalce | Qué exige y con qué frecuencia |
| Sociedad | Un medio de pago | Qué transparencia espera |

## 🏦 Del cliente al banco

El cliente confía en un respaldo y el banco mira su liquidez y su segregación. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Está auditado» | Puede ser una atestación a una fecha | 20, clase 4 |
| «Cobertura 102 %» | ¿Cuánto de eso es efectivo mañana? | 20, clase 4 |
| «La cobertura subió» | La composición empeoró | 20, clase 4 |

## ⚖️ Riesgos y controles

Los riesgos son de descalce y de segregación. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Descalce de plazo | Pasivo a la vista, activo a 2 años | Límite de plazo medio y publicación |
| Descuento subestimado | Se valora a precio de pantalla | Descuentos por tramo y por tamaño |
| Fecha de corte elegida | La foto se toma el mejor día | Fechas aleatorias y varias al mes |
| Reserva pignorada | Rinde más y no responde | Certificación de no pignoración |
| Concentración en un depositario | Un banco tiene todo el efectivo | Límite por depositario |
| Confundir atestación con auditoría | Los nombres se parecen | Leer el alcance del encargo |

## 🧪 Práctica

El laboratorio pide calcular las dos coberturas de una reserva. La brecha entre ambas es el resultado que importa.

En [`labs/lab-02.md`](../labs/lab-02.md):

1. Descompón una cartera y calcula cobertura contable y líquida.
2. Aplica descuentos por tramo y halla el coste de una redención del 35 %.
3. Recalcula la composición del remanente y explica su deterioro.
4. Redacta las cinco preguntas al informe de atestación.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen reservas insuficientes en el momento de la redención. Las causas son descalce de plazo y atestación confundida con auditoría.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Mirar solo el porcentaje | Es lo único publicado | Exige composición y plazo |
| Valorar a precio de pantalla | Es el dato disponible | Aplica descuento por venta forzada |
| Celebrar que la cobertura sube | Parece buena noticia | Mira qué quedó en la cartera |
| Aceptar «auditado» | Se usa como sinónimo | Pregunta el alcance |
| Ignorar el depositario | Se supone neutral | Es riesgo de crédito real |
| Un solo escenario | Se hace el que cubre | Haz también el segundo golpe |

## ❓ Preguntas de comprobación

1. ¿Qué tres cifras tiene una reserva y cuál se publica?
2. ¿Por qué dos reservas con el mismo 102 % pueden tener riesgos opuestos?
3. ¿Qué diferencia hay entre atestación y auditoría?
4. En el ejemplo, ¿por qué sube la cobertura mientras empeora el riesgo?
5. ¿Qué cinco preguntas se le hacen a un informe de reservas?

## 📥 Entregable

Guarda en `portfolio/parte-20/clase-04/`:

- la descomposición de una cartera con cobertura contable y líquida;
- el cálculo de la redención del 35 % con descuentos declarados;
- la composición del remanente y su interpretación;
- las cinco preguntas al informe, respondidas con un caso real.

## 🔗 Referencias cruzadas

- **Viene de:** clase 3.
- **Continúa en:** clases 5 y 6 de esta parte.
- **Se aplica en:** Parte 22, clase 5; Parte 23, clase 6.

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
- CPMI e IOSCO (2022). *Application of the Principles for Financial Market Infrastructures to stablecoin arrangements*. BIS. <https://www.bis.org/cpmi/publ/d206.htm>
- Basel Committee on Banking Supervision (2013). *Basel III: The Liquidity Coverage Ratio and liquidity risk monitoring tools*. BIS. <https://www.bis.org/publ/bcbs238.htm>
- Diario Oficial de la Unión Europea (2023). *Reglamento (UE) 2023/1114*, título sobre reservas de activos. EUR-Lex. <https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32023R1114>
- IOSCO (2023). *Policy Recommendations for Crypto and Digital Asset Markets*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- Verificación local: comprueba qué composición de reservas exige tu jurisdicción, con qué frecuencia de publicación y qué tipo de informe externo requiere. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 03 · Stablecoins: tipologías y mecánica de la paridad](03-stablecoins-tipologias-y-mecanica-de-la-paridad.md) | [Parte 20](../README.md) · [Programa](../../../SYLLABUS.md) | [05 · Redención: el derecho, el proceso y la cola →](05-redencion-el-derecho-el-proceso-y-la-cola.md) |
<!-- gen:footer:end -->
