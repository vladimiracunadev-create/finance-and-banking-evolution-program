<!-- meta
part: 11
class: 8
title: "Riesgo país y de contraparte"
level: profesional
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 08 · Riesgo país y de contraparte

> [← 07 · Riesgo de moneda](07-riesgo-de-moneda.md) · [Índice de la parte](../README.md) · [09 · Derivados y coberturas →](09-derivados-y-coberturas.md)

**Parte 11 — Gestión integral de riesgos** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Medir dos riesgos que comparten una característica incómoda: **la exposición no es fija**. En el riesgo
de contraparte, la exposición depende del valor futuro de un contrato; en el riesgo país, la capacidad
de pago del deudor depende de decisiones de un soberano sobre las que nadie tiene control.

Las clases anteriores tratan riesgos dentro de una jurisdicción. Esta añade dos que aparecen al operar con otros: el del país donde está el deudor, que puede impedir el pago aunque el deudor quiera pagar, y el de la contraparte de un derivado, cuya exposición cambia todos los días.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** riesgo soberano, de transferencia y de país en sentido amplio.
2. **Calcular** la exposición al incumplimiento de un derivado y su componente potencial futuro.
3. **Aplicar** la compensación contractual y las garantías a la reducción de exposición.
4. **Explicar** el ajuste de valoración por crédito y el riesgo de correlación adversa.
5. **Evaluar** la exposición cruzada de un banco a una jurisdicción.

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

Los dos primeros términos son las capas del riesgo país; los seis siguientes, la exposición de contraparte y sus correcciones. La **correlación adversa** es la que produce las pérdidas mayores: cuando la exposición crece justo cuando la contraparte se deteriora, porque ambas cosas tienen la misma causa.

| Concepto | Comprensión verificable |
|---|---|
| `riesgo soberano` | Que el Estado no pague su propia deuda. |
| `riesgo de transferencia` | Que el deudor pueda pagar pero el Estado impida la salida de divisas. |
| `riesgo de contraparte` | Que la contraparte de un contrato bilateral incumpla antes del vencimiento. |
| `exposición actual` | Valor de mercado positivo del contrato hoy. |
| `exposición potencial futura` | Cuánto podría crecer ese valor antes del vencimiento. |
| `compensación contractual` | Acuerdo que permite netear posiciones con una misma contraparte. |
| `ajuste de valoración por crédito` | Descuento al valor del derivado por el riesgo de la contraparte. |
| `correlación adversa` | La exposición crece justo cuando la contraparte empeora. |

## 🧠 Modelo mental

El modelo mental de la exposición de contraparte es que no es un número sino una película: hoy vale poco, mañana puede valer mucho, y lo que hay que capitalizar no es lo que vale hoy sino lo que puede llegar a valer antes del vencimiento.

```text
UN CRÉDITO tiene exposición CONOCIDA: el saldo
UN DERIVADO tiene exposición DESCONOCIDA: depende del mercado

  swap de tasa a 5 años, nocional 100 000
  hoy vale 0 → exposición actual 0
  si las tasas se mueven, puede valer +8 000 o −8 000

  si vale +8 000 y la contraparte incumple, pierdo 8 000
  si vale −8 000 y la contraparte incumple, no pierdo nada

  la exposición es la parte POSITIVA de un valor incierto
  → es una opción, y por eso tiene "valor de tiempo"
```

**De ahí que la exposición de un derivado se mida como exposición actual más una estimación de cuánto
puede crecer.** Y de ahí el riesgo más traicionero de la clase: cuando ese crecimiento está
correlacionado con el deterioro de la contraparte.

## 📖 Desarrollo

### 1. Las capas del riesgo país

El riesgo país tiene capas que se pueden materializar por separado. La tabla las recoge.

```text
1. SOBERANO        el Estado no paga su deuda
2. TRANSFERENCIA   el deudor privado paga en moneda local
                   pero no puede convertir ni remitir
3. CONVERTIBILIDAD la moneda deja de ser convertible
4. EXPROPIACIÓN    los activos son tomados o su uso restringido
5. MACRO           recesión, inflación o devaluación afectan a todos
                   los deudores de esa jurisdicción a la vez
```

**El riesgo de transferencia es el que más sorprende:** un deudor solvente, con recursos, puede resultar
en incumplimiento por una decisión del banco central de su país. Por eso las exposiciones se limitan
por jurisdicción y no solo por deudor.

```text
TECHO SOBERANO
  tradicionalmente, ninguna empresa de un país podía tener
  mejor calificación que su soberano

  hoy se admiten excepciones (exportadores con ingresos y activos
  fuera del país, filiales con garantía de matriz extranjera)
  pero el principio general se mantiene: el soberano
  es un piso de riesgo para todos sus residentes
```

### 2. Exposición de contraparte

La exposición de un derivado tiene un componente actual y uno potencial futuro. El procedimiento siguiente los calcula.

```text
EXPOSICIÓN AL INCUMPLIMIENTO (enfoque estandarizado)

  EAD = α × (RC + PFE)

  α    factor 1,4
  RC   costo de reposición = max(V − C, 0)
       V valor de mercado neto, C garantía recibida
  PFE  exposición potencial futura, por clase de activo y plazo
```

| Clase de activo | Factor supervisor típico |
|---|---:|
| Tasa de interés | 0,5 % |
| Moneda | 4,0 % |
| Crédito, grado de inversión | 0,38 % |
| Crédito, grado especulativo | 1,06 % |
| Acciones, índice | 20 % |
| Acciones, individual | 32 % |
| Materias primas, energía | 40 % |

*(Factores del enfoque estandarizado vigente; verifica los aplicables.)*

### 3. Mitigación

La exposición se reduce con compensación contractual y con garantías. La tabla recoge los mecanismos y su efecto.

| Mecanismo | Qué reduce | Condición para reconocerlo |
|---|---|---|
| Compensación contractual | Convierte muchas exposiciones en una neta | Acuerdo válido y exigible en la jurisdicción |
| Garantía en efectivo | Costo de reposición | Valoración y llamado de margen diarios |
| Margen inicial | Exposición potencial futura | Segregado, no reutilizable |
| Cámara de contrapartida central | Sustituye a la contraparte | Cámara reconocida y capitalizada |
| Cláusula de terminación anticipada | Plazo de exposición | Detonantes objetivos |

El primero de esos mecanismos merece un cálculo propio, porque su efecto sobre
la exposición es mayor de lo que sugiere su descripción.

```text
EFECTO DE LA COMPENSACIÓN
  sin compensación: exposición = Σ max(V_i, 0)
  con compensación: exposición = max(Σ V_i, 0)

  ejemplo con tres contratos: +900, −600, +200
    sin compensación: 900 + 0 + 200 = 1 100
    con compensación: max(500, 0)   =   500
    reducción: 55 %
```

**La condición crítica es la exigibilidad legal** en la jurisdicción de la contraparte, en caso de
insolvencia. Un acuerdo de compensación no reconocido por el tribunal competente no reduce nada: el
liquidador puede exigir los contratos favorables y dejar los desfavorables como créditos ordinarios.

### 4. Ajuste de valoración por crédito

El ajuste por crédito lleva al precio el riesgo de que la contraparte no cumpla. El procedimiento lo calcula.

```text
CVA = pérdida esperada por el riesgo de crédito de la contraparte
      sobre la vida del derivado

  ≈ Σ  PD_t × LGD × EE_t × factor de descuento

  EE_t  exposición esperada en el momento t
```

```text
CONSECUENCIAS PRÁCTICAS
  · el derivado vale menos que su valor teórico
  · la diferencia es un cargo que alguien debe absorber
  · su variación produce resultado: es volatilidad de resultado
  · tiene requerimiento de capital propio
  · se puede cubrir con derivados de crédito, con límites
```

### 5. Riesgo de correlación adversa

Cuando exposición y deterioro comparten causa, la mitigación falla justo cuando hace falta. La tabla recoge los casos típicos.

```text
CORRELACIÓN ADVERSA GENERAL
  la exposición crece cuando la calidad de la contraparte
  se deteriora, por factores macro comunes

CORRELACIÓN ADVERSA ESPECÍFICA
  la exposición crece POR LA MISMA CAUSA
  que deteriora a la contraparte

  ejemplo canónico: comprar protección crediticia sobre un país
  a un banco domiciliado en ese país
  → si el país incumple, la protección vale mucho
    y quien debe pagarla ya no puede
```

| Caso | Tipo | Tratamiento |
|---|---|---|
| Swap de tasas con un banco del mismo país en crisis | General | Escenarios conjuntos |
| Protección sobre un emisor comprada a su filial | Específica | Exposición sin beneficio de la cobertura |
| Garantía en acciones del propio deudor | Específica | No reconocer la garantía |
| Repo con colateral emitido por la contraparte | Específica | Prohibido o sin reconocimiento |

## 🧮 Ejemplo guiado

El ejemplo calcula la exposición de una cartera de derivados con y sin compensación contractual. La reducción es grande, y comprobar que el acuerdo es oponible es lo que la hace real.

**Situación.** Un banco evalúa su exposición a una jurisdicción y a una contraparte financiera de ella.

```text
EXPOSICIÓN AL PAÍS Z
  bonos soberanos de Z                      54 000
  créditos a empresas residentes en Z       92 000
  líneas a bancos de Z                      38 000
  derivados con el Banco Q (residente en Z) según cálculo
  patrimonio efectivo del banco             420 000

DERIVADOS CON EL BANCO Q
  contrato    tipo              nocional   valor de mercado   plazo residual
  1  swap de tasa receptor       180 000        +6 400          3,2 años
  2  swap de tasa pagador         90 000        −2 800          1,8 años
  3  forward de moneda            60 000        +3 100          0,6 años
  4  swap de moneda               75 000        −1 900          4,1 años

  acuerdo de compensación: sí, exigible en Z (opinión legal vigente)
  garantía recibida en efectivo: 2 000, con llamado diario
```

**Paso 1 — calcula el costo de reposición.**

```text
valor de mercado neto = 6 400 − 2 800 + 3 100 − 1 900 = 4 800
garantía recibida = 2 000

RC = max(4 800 − 2 000, 0) = 2 800
```

**Paso 2 — calcula la exposición potencial futura.**

```text
por clase de activo:

TASA DE INTERÉS (contratos 1 y 2)
  nocional neto ajustado por duración:
    contrato 1: 180 000 × factor de duración 0,87 = 156 600  (receptor, +)
    contrato 2:  90 000 × factor de duración 0,94 =  84 600  (pagador, −)
  nocional efectivo neto = 156 600 − 84 600 = 72 000
  PFE_tasa = 72 000 × 0,5 % = 360

MONEDA (contratos 3 y 4)
  el forward y el swap involucran pares distintos → no se compensan
    contrato 3: 60 000 × 4,0 % = 2 400
    contrato 4: 75 000 × 4,0 % = 3 000
  PFE_moneda = 5 400

PFE TOTAL = 360 + 5 400 = 5 760
```

**Paso 3 — calcula la exposición al incumplimiento.**

```text
EAD = 1,4 × (2 800 + 5 760) = 1,4 × 8 560 = 11 984
```

**Paso 4 — compara con el cálculo sin compensación.**

```text
sin acuerdo de compensación:
  RC = 6 400 + 0 + 3 100 + 0 = 9 500  (solo valores positivos)
  garantía no aplicable contrato a contrato de la misma forma
  PFE sin compensar = 900 + 423 + 2 400 + 3 000 = 6 723
  EAD = 1,4 × (9 500 + 6 723) = 22 712

la compensación reduce la exposición en 10 728  (47 %)

y todo ese beneficio depende de UN documento:
la opinión legal sobre la exigibilidad del acuerdo en la jurisdicción Z
```

**Paso 5 — evalúa la correlación adversa.**

```text
el contrato 4 es un swap de moneda: el banco RECIBE moneda local de Z
y PAGA moneda fuerte

si Z entra en crisis:
  · la moneda de Z se deprecia
  · el valor del swap para nuestro banco AUMENTA (recibimos menos valor...)

  verificación: recibimos moneda de Z → si se deprecia,
  el contrato nos resulta DESFAVORABLE, valor negativo mayor
  → no hay correlación adversa en este contrato

el contrato 3 es un forward donde COMPRAMOS moneda fuerte contra moneda de Z
  si Z entra en crisis, el contrato nos es FAVORABLE (+)
  y el Banco Q, residente en Z, está en peores condiciones de pagar

  CORRELACIÓN ADVERSA ESPECÍFICA identificada
  la exposición del contrato 3 crece exactamente
  cuando la contraparte se deteriora
```

**Paso 6 — agrega la exposición al país.**

```text
bonos soberanos de Z                    54 000
créditos a empresas residentes           92 000
líneas a bancos de Z                     38 000
derivados con Banco Q (EAD)              11 984
EXPOSICIÓN TOTAL AL PAÍS Z              195 984

sobre patrimonio efectivo: 195 984 / 420 000 = 46,7 %

límite interno de exposición por país: 30 %
EXCESO: 16,7 puntos → 70 116
```

**Paso 7 — evalúa el riesgo de transferencia.**

```text
de los 92 000 en empresas residentes:
  exportadores con cuentas en el exterior     31 000  → riesgo de transferencia bajo
  empresas con ingresos locales                61 000  → riesgo de transferencia ALTO

si Z impone controles de cambio:
  · los 61 000 no pueden remitir aunque puedan pagar
  · los 38 000 en bancos de Z quedan igualmente atrapados
  · los bonos soberanos pueden reestructurarse
  EXPOSICIÓN SUJETA A TRANSFERENCIA: 153 000
```

**Paso 8 — decisiones.**

```text
1. LÍMITE
   exceso de 70 116 sobre el límite de país
   plan de reducción en 12 meses: no renovar líneas a bancos de Z,
   no originar nuevo crédito a empresas con ingresos locales

2. CORRELACIÓN ADVERSA
   el contrato 3 no debe computar el beneficio de compensación
   en un escenario de crisis de Z: medirlo por separado y en bruto

3. GARANTÍA
   exigir garantía en efectivo en moneda fuerte, custodiada
   FUERA de la jurisdicción Z
   → una garantía atrapada por controles de cambio no es garantía

4. OPINIÓN LEGAL
   la compensación reduce la exposición en 47 %;
   revalidar anualmente la opinión legal sobre su exigibilidad en Z

5. AJUSTE DE VALORACIÓN
   calcular el CVA del Banco Q con la PD implícita en el mercado
   y reconocerlo en la valoración de la cartera
```

**Interpreta:** el análisis mostró dos cosas que ninguna medición individual habría revelado. Primero,
que **el 47 % de la reducción de exposición dependía de un documento legal**, no de una garantía real.
Segundo, que **la garantía en efectivo estaba en la jurisdicción cuyo riesgo pretendía cubrir**, lo que
la anulaba precisamente en el escenario donde se necesitaba. El riesgo país no es una capa adicional
sobre los demás riesgos: **es una condición que puede desactivar sus mitigantes**.

## 🏦 Del cliente al banco

El cliente contrata una cobertura y el banco asume una exposición que varía con el mercado. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Mi empresa es solvente pero no me prestan» | Techo soberano y límite de país | 11, clase 8 |
| «No pude remitir el pago al exterior» | Riesgo de transferencia | 10, clase 13 |
| «El banco exige garantía en el exterior» | Garantía fuera de la jurisdicción de riesgo | 11, clase 8 |
| «Contraté una cobertura y no me sirvió» | Correlación adversa específica | 11, clase 9 |
| «El derivado valía menos de lo pactado» | Ajuste de valoración por crédito | 11, clase 9 |

## 🧪 Práctica

El laboratorio pide calcular la exposición de contraparte con mitigantes y detectar un caso de correlación adversa. El caso está construido para que la garantía pierda valor con el mismo evento que deteriora a la contraparte.

En `labs/lab-04.md`, sección de contraparte:

1. Calcula la exposición al incumplimiento de una cartera de derivados con y sin compensación.
2. Identifica los casos de correlación adversa específica en un conjunto de contratos.
3. Agrega la exposición a una jurisdicción por todos sus canales.
4. Evalúa qué parte de esa exposición está sujeta a riesgo de transferencia.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen pérdidas con contrapartes garantizadas. La causa es la correlación adversa o una compensación no oponible.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se mide solo la exposición actual | Falta el componente potencial futuro | Añade la PFE. |
| Compensación reconocida sin opinión legal | Riesgo de inexigibilidad | Valida y revalida la opinión anualmente. |
| Garantía en la jurisdicción de riesgo | Se anula con controles de cambio | Custódiala fuera. |
| Cobertura comprada a una contraparte correlacionada | Correlación adversa específica | No reconozcas el beneficio. |
| Exposición al país medida por un solo canal | Agregación incompleta | Suma soberano, empresas, bancos y derivados. |
| Se ignora el riesgo de transferencia | Solo se mira solvencia | Clasifica por capacidad de remitir. |

## ❓ Preguntas de comprobación

1. ¿Por qué la exposición de un derivado se comporta como una opción?
2. ¿Qué diferencia el riesgo soberano del riesgo de transferencia?
3. ¿De qué depende que un acuerdo de compensación reduzca realmente la exposición?
4. ¿Qué es la correlación adversa específica y cómo debe tratarse?
5. ¿Por qué una garantía puede dejar de serlo en un escenario de riesgo país?

## 📥 Entregable

Guarda en `portfolio/parte-11/clase-08/`:

- la exposición al incumplimiento calculada con y sin compensación;
- los casos de correlación adversa identificados y su tratamiento;
- la exposición agregada a una jurisdicción por todos los canales;
- la porción sujeta a riesgo de transferencia con su justificación.

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

- Basel Committee on Banking Supervision (2014). *The standardised approach for measuring counterparty credit risk exposures*. BIS. Cálculo de la exposición de contraparte por el método estándar. <https://www.bis.org/publ/bcbs279.htm>
- Basel Committee on Banking Supervision (2015). *Review of the Credit Valuation Adjustment risk framework*. BIS. Cargo de capital por ajuste de valoración del crédito.
- Gregory, J. (2020). *The xVA Challenge: Counterparty Risk, Funding, Collateral, Capital and Initial Margin* (4.ª ed.). Wiley. Familia de ajustes de valoración y su efecto en el precio.
- International Monetary Fund (2013). *Sovereign Debt Restructuring — Recent Developments*. IMF Policy Papers. Mecánica y precedentes de una reestructuración soberana.
- Hull, J. (2018). *Risk Management and Financial Institutions* (5.ª ed.). Wiley. Capítulo sobre riesgo de contraparte.
- Verificación local: revisa el tratamiento de exposiciones soberanas, los límites por país y el reconocimiento de acuerdos de compensación en tu jurisdicción.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 07 · Riesgo de moneda](07-riesgo-de-moneda.md) | [Parte 11](../README.md) · [Programa](../../../SYLLABUS.md) | [09 · Derivados y coberturas →](09-derivados-y-coberturas.md) |
<!-- gen:footer:end -->
