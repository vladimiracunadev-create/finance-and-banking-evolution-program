---
part: 18
class: 7
title: "Compensación, liquidación y finalidad"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global, chile]
regulatory_topics: [cross-border-payments, infraestructura, firmeza]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [CPMI, Banco Central de Chile]
requires_legal_review: true
---

<!-- gen:header:start -->
# Clase 07 · Compensación, liquidación y finalidad

> [← 06 · SWIFT, CBPR+ e ISO 20022](06-swift-cbpr-e-iso-20022.md) · [Índice de la parte](../README.md) · [08 · Liquidez, prefinanciación, netting y horarios →](08-liquidez-prefinanciacion-y-netting.md)

**Parte 18 — Pagos transfronterizos, remesas y liquidación internacional** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Separar tres momentos que se confunden y que determinan quién soporta la pérdida
si algo falla: **compensación**, **liquidación** y **finalidad**. El tercero no
es un concepto técnico: es una consecuencia jurídica.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** compensación, liquidación y finalidad con un caso de quiebra.
2. **Comparar** liquidación bruta en tiempo real con liquidación neta diferida.
3. **Explicar** qué da finalidad a un pago y por qué no la da el mensaje.
4. **Analizar** el riesgo de liquidación en una cadena transfronteriza.
5. **Determinar** en qué momento un beneficiario puede disponer sin riesgo.

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
| `compensación` | Cálculo de las posiciones netas entre participantes |
| `liquidación` | Transferencia efectiva de los fondos |
| `finalidad` | Momento en que la transferencia es irrevocable e incondicional |
| `liquidación bruta en tiempo real` | Cada operación se liquida individualmente, al instante |
| `liquidación neta diferida` | Se compensan las posiciones y se liquida el neto, en ciclos |
| `riesgo de liquidación` | Riesgo de entregar sin recibir |
| `riesgo Herstatt` | Riesgo de liquidación en operaciones de cambio por husos horarios |
| `revocación` | Anulación de una instrucción antes de la finalidad |

## 🧠 Modelo mental

```text
TRES MOMENTOS, TRES PREGUNTAS DISTINTAS

  COMPENSACIÓN   ¿cuánto se deben las partes en neto?
                 es un CÁLCULO. Nadie ha pagado todavía.

  LIQUIDACIÓN    ¿ya se movieron los fondos?
                 es un HECHO. El dinero cambió de cuenta.

  FINALIDAD      ¿puede deshacerse?
                 es una CONSECUENCIA JURÍDICA.
                 La da la ley o las reglas del sistema,
                 no el software.

EL ORDEN NO ES NEGOCIABLE
  puede haber compensación sin liquidación
  puede haber liquidación sin finalidad
  NO puede haber finalidad sin liquidación

LA PREGUNTA QUE DECIDE TODO
  «si el banco pagador quiebra AHORA MISMO,
   ¿este pago se deshace?»
  si la respuesta es sí, no hay finalidad.
```

## 📖 Desarrollo

### 1. Los dos modelos de liquidación

| | Bruta en tiempo real | Neta diferida |
|---|---|---|
| Cuándo liquida | Operación a operación, al instante | En ciclos, el neto |
| Liquidez necesaria | Alta: el importe completo | Baja: solo el neto |
| Riesgo de crédito entre ciclos | Ninguno | Sí, hasta liquidar |
| Finalidad | Inmediata | Al liquidar el ciclo |
| Uso típico | Mayorista, importes altos | Minorista, alto volumen |
| Qué pasa si un participante falla | Solo su operación no ocurre | Puede deshacerse el ciclo entero |

```text
EL COMPROMISO CENTRAL DE LOS SISTEMAS DE PAGO
  LIQUIDEZ  ⟷  RIESGO

  liquidar bruto: sin riesgo, con mucha liquidez inmovilizada
  liquidar neto:  poca liquidez, con riesgo entre ciclos

  los sistemas modernos combinan ambos:
  bruto con mecanismos de ahorro de liquidez
  (colas, compensación bilateral continua, algoritmos)
```

### 2. Qué da finalidad

```text
LA FINALIDAD LA DA
  · la ley del sistema de pagos aplicable
  · las reglas del propio sistema
  · a veces, un momento definido: «la anotación en la cuenta
    del banco central es final e irrevocable»

LA FINALIDAD NO LA DA
  · el mensaje de pago
  · el aviso al beneficiario
  · el apunte contable interno
  · que el dinero «se vea» en la cuenta

EL CASO QUE LO ILUSTRA
  un banco abona a su cliente en cuanto recibe el mensaje,
  antes de que llegue la cobertura.
  El cliente ve el saldo y dispone.
  La cobertura no llega porque el banco ordenante quebró.
  → el abono no tenía finalidad: era un adelanto
    del banco beneficiario, y la pérdida es suya
```

### 3. Zona de liquidación y zona de disponibilidad

```text
TRES ESTADOS DEL DINERO PARA EL BENEFICIARIO

  ANUNCIADO     hay un mensaje; no hay fondos
                riesgo: total

  LIQUIDADO     los fondos llegaron al banco beneficiario
                riesgo: el del banco beneficiario

  DISPONIBLE    el beneficiario puede usarlo
                riesgo: ninguno si hubo finalidad

  ENTRE LIQUIDADO Y DISPONIBLE PUEDE HABER HORAS
    el banco beneficiario aplica sus propios controles
    y su propio horario de acreditación
```

### 4. El riesgo Herstatt

```text
26 DE JUNIO DE 1974. Bankhaus Herstatt, Colonia.

  varias contrapartes habían pagado marcos alemanes
  durante la mañana europea, esperando recibir dólares
  en Nueva York por la tarde.

  las autoridades alemanas cerraron el banco
  al cierre de la jornada alemana,
  antes de que Nueva York abriera.

  → los marcos se habían entregado
  → los dólares nunca llegaron

DE AHÍ EL NOMBRE
  riesgo Herstatt = riesgo de liquidación en operaciones
  de cambio, por la falta de simultaneidad entre husos

LA RESPUESTA DEL SISTEMA
  liquidación con pago contra pago (clase 15):
  ninguna pata se liquida si la otra no se liquida
```

### 5. Cuándo puede disponer el beneficiario

```text
LA REGLA PRUDENTE
  disponer cuando hay FINALIDAD, no cuando hay saldo

CÓMO SE SABE
  · en un sistema bruto con finalidad legal: al liquidar
  · en un sistema neto: al cerrar el ciclo
  · en una cadena de corresponsales: cuando el último
    tramo liquida en un sistema con finalidad

  → en la práctica, el banco beneficiario decide su
    política de disponibilidad y ASUME el riesgo
    de adelantar

QUÉ DEBE DECIRSE AL CLIENTE
  «disponible» y «confirmado» no son lo mismo.
  Un comercio que entrega contra «disponible» sin
  finalidad asume un riesgo que probablemente no sabe
  que está asumiendo (Parte 17, clase 10).
```

## 🧮 Ejemplo guiado

**Situación.** Un banco beneficiario define su política de acreditación para
pagos internacionales. Hay que decidir cuándo abona al cliente.

```text
DATOS DEL CORREDOR (12 meses, 24 000 pagos recibidos)
  pagos con cobertura recibida el mismo día      22 560   94,0 %
  cobertura al día siguiente                      1 176    4,9 %
  cobertura con más de un día de retraso            216    0,9 %
  cobertura que nunca llegó                          48    0,2 %

IMPORTE MEDIO POR PAGO                            8 400 USD
POLÍTICA ACTUAL: abonar al recibir el mensaje

INGRESO POR EL SERVICIO                          310 000 USD/año
```

**Paso 1 — calcula la exposición de la política actual.**

```text
PAGOS ABONADOS SIN COBERTURA FIRME
  1 176 + 216 + 48 = 1 440 pagos al año

EXPOSICIÓN MÁXIMA SIMULTÁNEA (aproximada)
  pagos de un día sin cobertura: 1 440 / 250 ≈ 5,8
  5,8 × 8 400 ≈ 48 700 USD de exposición diaria media

PÉRDIDA EFECTIVA
  48 pagos sin cobertura × 8 400 = 403 200 USD/año
```

**Paso 2 — compara con el ingreso.**

```text
INGRESO                310 000 USD
PÉRDIDA POR ADELANTO   403 200 USD
RESULTADO             −93 200 USD

LA POLÍTICA ACTUAL DESTRUYE VALOR
```

**Paso 3 — evalúa la política contraria.**

```text
POLÍTICA B · abonar solo con cobertura liquidada

  PÉRDIDA: 0
  PERO
    el 6 % de los clientes recibe el pago con retraso
    y algunos son cobros de operaciones comerciales

  EFECTO ESTIMADO
    reclamaciones: 1 440 × 40 % = 576 al año × 45 USD = 25 920
    abandono: 2 % de los 1 440 afectados = 29 clientes
    valor anual por cliente: 1 200 USD → 34 800 USD

  RESULTADO
    310 000 − 25 920 − 34 800 = 249 280 USD
```

**Paso 4 — busca la política intermedia.**

```text
POLÍTICA C · abonar según el ORDENANTE, no según el pago

  segmentar por banco ordenante y su historial:
    bancos con 0 incidencias en 24 meses  → abono inmediato
    resto                                  → abono con cobertura

  DISTRIBUCIÓN
    pagos de bancos sin incidencias:  20 640  (86 %)
    pagos del resto:                   3 360  (14 %)

  DE LOS 48 SIN COBERTURA, ¿DE DÓNDE VENÍAN?
    de bancos del segundo grupo:  44
    de bancos del primer grupo:    4

  PÉRDIDA CON LA POLÍTICA C
    4 × 8 400 = 33 600 USD

  RECLAMACIONES Y ABANDONO
    afectan solo al 14 %:
    reclamaciones: 3 360 × 6 % × 40 % × 45 = 3 629 USD
    abandono: 3 360 × 6 % × 2 % × 1 200 = 4 838 USD

  RESULTADO
    310 000 − 33 600 − 3 629 − 4 838 = 267 933 USD
```

**Paso 5 — compara las tres.**

```text
A · abono inmediato a todos      −93 200 USD
B · abono solo con cobertura     249 280 USD
C · segmentado por ordenante     267 933 USD

LA C GANA POR 18 653 USD SOBRE LA B
```

**Paso 6 — cuestiona el resultado antes de aceptarlo.**

```text
DOS PROBLEMAS CON LA POLÍTICA C

  1. EL HISTORIAL NO PREDICE LA QUIEBRA
     un banco con 24 meses sin incidencias puede fallar
     mañana. El modelo asume estabilidad donde hay
     una distribución de cola gruesa.

     MITIGACIÓN
       límite de exposición por banco ordenante,
       no solo criterio binario:
       exposición máxima simultánea = X por banco
       y revisión trimestral del segmento

  2. LA DIFERENCIA ENTRE B Y C ES DE 18 653 USD
     frente a una exposición diaria de decenas de miles
     → el margen no compensa un evento de cola

     MITIGACIÓN
       la política C solo se sostiene CON el límite
       por banco. Sin él, es la política A disfrazada.
```

**Paso 7 — formula la política final.**

```text
POLÍTICA APROBADA

  1. abono inmediato solo a bancos del segmento sin
     incidencias, y con LÍMITE DE EXPOSICIÓN por banco
     y por día, calibrado sobre su tamaño
  2. el resto: abono con cobertura liquidada
  3. revisión trimestral de los segmentos
  4. suspensión automática del abono inmediato ante
     una sola incidencia
  5. al cliente se le informa la fecha de disponibilidad,
     no un «disponible» ambiguo

  Y UNA DECISIÓN EXPLÍCITA
    el banco reconoce que el abono anticipado es un
    CRÉDITO al banco ordenante, no una mejora de servicio.
    Se registra como tal, consume límite y aparece en
    el informe de riesgo de contraparte.
```

**Interpreta:** la política de acreditación parecía una decisión de experiencia
de cliente y era **una decisión de riesgo de crédito no reconocida**. El banco
llevaba años concediendo crédito intradía a bancos con los que no tenía línea
aprobada, y la pérdida superaba el ingreso del servicio.

## 🧭 Perspectivas

| Actor | Qué ve | Qué decide |
|---|---|---|
| Beneficiario | Saldo en su cuenta | Si dispone |
| Comercio | «Pago recibido» | Si entrega la mercancía |
| Banco beneficiario | Abono sin cobertura | Su política de acreditación |
| Banco ordenante | Su pago se abonó rápido | Nada: no asume el riesgo |
| Riesgo de crédito | Exposición no registrada | Si exige línea |
| Banco central | Finalidad en su sistema | Reglas y horarios |
| Supervisor | Crédito intradía no declarado | Si observa |

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Ya lo tengo en mi cuenta» | Abono sin cobertura: es un adelanto | 18, clase 7 |
| «Me revirtieron un abono» | El pago no tenía finalidad | 18, clase 7 |
| «El banco tardó en liberarlo» | Política de disponibilidad | 18, clase 7 |
| «Entregué contra el comprobante» | Comprobante ≠ finalidad | 17, clase 10 |

## ⚖️ Riesgos y controles

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Crédito intradía no reconocido | Abono antes de cobertura | Registrarlo como exposición con límite |
| Reversión de un abono | Sin finalidad y el ordenante falla | Política de disponibilidad explícita |
| Riesgo Herstatt | Se paga una pata y no se recibe la otra | Pago contra pago (clase 15) |
| Ciclo neto deshecho | Un participante falla antes de liquidar | Garantías y reglas de reparto de pérdidas |
| Comunicación ambigua | «Disponible» sin decir si es firme | Estado explícito y fecha |
| Segmento obsoleto | Un banco cambia y nadie lo revisó | Revisión periódica y suspensión automática |

## 🧪 Práctica

En [`labs/lab-01.md`](../labs/lab-01.md) y [`labs/lab-07.md`](../labs/lab-07.md):

1. Clasifica ocho momentos de un pago en compensación, liquidación y finalidad.
2. Simula la quiebra del banco ordenante en tres instantes distintos.
3. Calcula la exposición de tres políticas de acreditación.
4. Diseña el límite por banco ordenante y justifica su cálculo.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| «Liquidado» como sinónimo de firme | Se ignoró la finalidad | Pregunta qué pasa si quiebra ahora |
| Abonar al recibir el mensaje | Se buscó experiencia de cliente | Es crédito: regístralo y limítalo |
| Neto sin garantías | Se asumió que el ciclo siempre cierra | Reglas de reparto de pérdidas |
| Confiar en el historial | Se modeló sin cola | Límite de exposición, no criterio binario |
| «Disponible» ambiguo | No se distinguieron los estados | Tres estados explícitos al cliente |
| Ignorar el huso en FX | Se supuso simultaneidad | Riesgo Herstatt y PvP |

## ❓ Preguntas de comprobación

1. ¿Qué pregunta permite saber si un pago tiene finalidad?
2. ¿Qué se intercambia entre liquidación bruta y neta, y por qué existen ambas?
3. ¿Qué ocurrió en 1974 y qué mecanismo se creó como respuesta?
4. ¿Por qué abonar antes de la cobertura es una decisión de crédito?
5. En el ejemplo guiado, ¿por qué la política C sin límite es la política A?

## 📥 Entregable

Guarda en `portfolio/parte-18/clase-07/`:

- la clasificación de ocho momentos en los tres conceptos;
- el resultado de simular una quiebra en tres instantes;
- el cálculo de exposición de tres políticas de acreditación;
- la política que propondrías, con su límite y su regla de suspensión.

## 🔗 Referencias cruzadas

- **Viene de:** clases 4 y 5; Parte 10, clase 10; Parte 11 (riesgo de crédito).
- **Continúa en:** clase 8 (liquidez), clase 15 (pago contra pago).
- **Se aplica en:** Parte 21, clase 15 (liquidación atómica); Parte 23, clase 14.

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

- Committee on Payments and Market Infrastructures e IOSCO (2012). *Principles for Financial Market Infrastructures*. BIS. <https://www.bis.org/cpmi/publ/d101.htm>
- Committee on Payments and Market Infrastructures (2008). *The interdependencies of payment and settlement systems*. BIS. <https://www.bis.org/cpmi/publ/d84.htm>
- Committee on Payments and Market Infrastructures (2013). *Supervisory guidance for managing risks associated with the settlement of foreign exchange transactions*. BIS. <https://www.bis.org/publ/bcbs241.htm>
- Banco Central de Chile. *Normativa del sistema de liquidación bruta en tiempo real*. <https://www.bcentral.cl/>
- Committee on Payments and Market Infrastructures (2003). *A glossary of terms used in payments and settlement systems*. BIS. <https://www.bis.org/cpmi/glossary_030301.htm>
- Verificación local: comprueba qué norma otorga finalidad a los pagos en tu jurisdicción y en qué momento exacto la sitúa. **Fecha de verificación de esta clase: 2026-08-06.** Esta clase no constituye asesoría legal.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 06 · SWIFT, CBPR+ e ISO 20022](06-swift-cbpr-e-iso-20022.md) | [Parte 18](../README.md) · [Programa](../../../SYLLABUS.md) | [08 · Liquidez, prefinanciación, netting y horarios →](08-liquidez-prefinanciacion-y-netting.md) |
<!-- gen:footer:end -->
