---
part: 17
class: 9
title: "APIs de cuentas, productos, créditos, seguros e inversiones"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global, chile]
regulatory_topics: [open-finance, contratos-de-api, proteccion-de-datos]
regulation_last_verified: 2026-08-06
regulatory_status: en-despliegue-por-fases
primary_authorities: [CMF]
requires_legal_review: true
---

<!-- gen:header:start -->
# Clase 09 · APIs de cuentas, productos, créditos, seguros e inversiones

> [← 08 · Diseño, versionado e idempotencia](08-diseno-versionado-e-idempotencia.md) · [Índice de la parte](../README.md) · [10 · Iniciación de pagos y confirmación de fondos →](10-iniciacion-de-pagos-y-confirmacion-de-fondos.md)

**Parte 17 — Finanzas abiertas, APIs y economía de datos** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Modelar los datos de **todos** los productos financieros, no solo de la cuenta
corriente. Cada familia de producto tiene una estructura, un ciclo y una
sensibilidad distintas, y el modelo que sirve para una rompe en la siguiente.

## 📚 Objetivos

Al finalizar podrás:

1. **Modelar** las cinco familias de producto con su estructura propia.
2. **Identificar** qué campo de cada familia concentra la sensibilidad.
3. **Resolver** los tres problemas transversales: titularidad compartida,
   productos cerrados y datos de terceros.
4. **Diseñar** el orden de exposición por fases, con criterio de valor y riesgo.
5. **Detectar** cuándo un dato del producto revela un dato de otra persona.

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
| `familia de producto` | Conjunto de productos con la misma estructura de datos |
| `titularidad compartida` | Un producto con más de un titular con derechos plenos |
| `producto cerrado` | Producto terminado cuyo histórico sigue siendo relevante |
| `dato de tercero` | Dato de una persona distinta del titular que consiente |
| `posición` | Foto del estado actual del producto |
| `movimiento` | Hecho que cambia la posición |
| `condición` | Parámetro contractual: tasa, plazo, cobertura, comisión |
| `beneficiario` | Persona designada, típica de seguros y previsión |

## 🧠 Modelo mental

```text
TODO PRODUCTO FINANCIERO SE DESCRIBE CON TRES BLOQUES

  IDENTIDAD     qué es, de quién, desde cuándo, en qué estado
  CONDICIONES   qué se pactó: tasa, plazo, cobertura, comisiones
  DINÁMICA      qué ha pasado: movimientos, cuotas, siniestros, aportes

LO QUE CAMBIA ENTRE FAMILIAS NO ES EL ESQUEMA:
ES QUÉ BLOQUE CONCENTRA EL VALOR Y CUÁL LA SENSIBILIDAD

  cuentas       valor en DINÁMICA      sensibilidad en DINÁMICA
  crédito       valor en CONDICIONES   sensibilidad en DINÁMICA (mora)
  seguros       valor en CONDICIONES   sensibilidad en DINÁMICA (siniestros)
  inversiones   valor en DINÁMICA      sensibilidad en IDENTIDAD (patrimonio)
  previsión     valor en CONDICIONES   sensibilidad en IDENTIDAD (edad, saldo)
```

## 📖 Desarrollo

### 1. Cuentas y medios de pago

```text
IDENTIDAD     id opaco, tipo, moneda, titulares, estado, apertura
CONDICIONES   comisión de mantención, línea asociada, límites
DINÁMICA      saldo contable, saldo disponible, movimientos

CAMPOS QUE CONCENTRAN LA SENSIBILIDAD
  · glosa y comercio del movimiento → inferencia (clase 4)
  · saldo → capacidad de pago
  · movimientos recurrentes → estructura de vida

DECISIÓN DE DISEÑO IMPRESCINDIBLE
  saldo contable ≠ saldo disponible
  y hay que exponer LOS DOS, con su definición,
  porque el tercero que use el equivocado
  dirá al cliente que tiene dinero que no tiene
```

### 2. Créditos

```text
IDENTIDAD     tipo (consumo, hipotecario, comercial), estado
CONDICIONES   monto, tasa, plazo, sistema de amortización,
              seguros asociados, comisiones, garantías
DINÁMICA      cuotas pagadas y pendientes, saldo insoluto,
              días de mora, prepagos

EL CAMPO MÁS SENSIBLE ES «días de mora»
  revela dificultad financiera actual
  y es exactamente el que un tercero quiere para decidir
  si ofrece crédito

  → la exposición de mora requiere consentimiento
    con finalidad explícita, y NO debe ir en el mismo
    alcance que la posición

EL CAMPO MÁS ÚTIL ES «tasa» + «saldo insoluto»
  permite calcular si conviene refinanciar
  → es el caso de uso que justifica toda la familia
```

### 3. Seguros

```text
IDENTIDAD     ramo, póliza, vigencia, estado
CONDICIONES   coberturas, sumas aseguradas, deducibles,
              exclusiones, prima, periodicidad
DINÁMICA      siniestros, liquidaciones, renovaciones

DOS PROBLEMAS PROPIOS

  1 · EXCLUSIONES
      son el dato que determina si la póliza sirve,
      y son texto libre, no estructurado.
      Un comparador que ignore exclusiones compara mal.

  2 · DATOS DE SALUD
      en seguros de salud y vida, el siniestro ES un dato de salud.
      → categoría especialmente protegida
      → alcance separado, consentimiento reforzado,
        y en muchos diseños: NO SE EXPONE
```

### 4. Inversiones

```text
IDENTIDAD     tipo de cuenta, custodio, régimen tributario
CONDICIONES   perfil, comisiones, restricciones de rescate
DINÁMICA      posiciones, valor de mercado, aportes, retiros,
              rentabilidad, operaciones

EL PROBLEMA DE LA VALORACIÓN
  ¿a qué precio se expone una posición?
    · último precio de mercado          → volátil, sin hora no significa nada
    · precio de cierre del día anterior → estable, desfasado
    · valor cuota del fondo             → oficial, con retardo

  SE EXPONEN AMBOS: valor y FECHA/HORA de valoración.
  Un valor sin su instante es un número sin unidad.

SENSIBILIDAD
  el patrimonio total es el dato más sensible
  de todo el conjunto de finanzas abiertas
```

### 5. Los tres problemas transversales

```text
PROBLEMA 1 · TITULARIDAD COMPARTIDA
  una cuenta con dos titulares plenos.
  ¿Puede uno consentir el acceso a los movimientos,
  que incluyen los del otro?

  RESPUESTA DE DISEÑO
    · el consentimiento de un titular alcanza al producto
    · pero el otro titular tiene derecho a saberlo
    · y ciertos productos exigen consentimiento de todos
  → la regla concreta la fija la norma local: verifícala

PROBLEMA 2 · PRODUCTOS CERRADOS
  un crédito pagado hace 8 meses sigue siendo relevante
  para evaluar comportamiento.

  RESPUESTA DE DISEÑO
    · se exponen con estado «cerrado» y fecha de cierre
    · dentro de la ventana declarada
    · el alcance de productos cerrados es SEPARADO:
      no todo caso de uso lo necesita

PROBLEMA 3 · DATOS DE TERCEROS
  el movimiento «transferencia a Juan Pérez, cuenta ***4821»
  contiene datos de una persona que no consintió.

  RESPUESTA DE DISEÑO
    · enmascarar identificadores de contraparte
    · nombre de contraparte solo si la norma lo permite
    · nunca exponer la cuenta completa de un tercero
```

### 6. Orden de exposición por fases

| Fase | Familia | Por qué en ese orden |
|---:|---|---|
| 1 | Cuentas y medios de pago | Máximo valor, estructura conocida, universal |
| 2 | Créditos (sin mora) | Alto valor, sensibilidad acotada |
| 3 | Créditos (con mora) | Requiere finalidad reforzada |
| 4 | Inversiones | Alta sensibilidad patrimonial |
| 5 | Seguros (sin salud) | Estructura irregular, valor medio |
| 6 | Seguros de salud y vida | Categoría especialmente protegida |

## 🧮 Ejemplo guiado

**Situación.** Un producto de «salud financiera» quiere calcular la capacidad de
ahorro mensual del cliente. Hay que decidir qué familias necesita, en qué fase se
puede lanzar y qué campo sensible se puede evitar.

**Paso 1 — escribe la fórmula del producto antes de mirar las APIs.**

```text
CAPACIDAD DE AHORRO MENSUAL
  = ingreso recurrente
  − gasto recurrente comprometido
  − servicio de deuda
  − prima de seguros
```

**Paso 2 — deriva el dato mínimo de cada término.**

```text
INGRESO RECURRENTE
  movimientos de abono con patrón mensual
  → familia CUENTAS, alcance movimientos

GASTO RECURRENTE COMPROMETIDO
  cargos con patrón mensual
  → familia CUENTAS, mismo alcance

SERVICIO DE DEUDA
  cuota mensual de cada crédito vigente
  → familia CRÉDITOS
  → ¿hace falta la mora? NO: la cuota basta

PRIMA DE SEGUROS
  prima y periodicidad
  → familia SEGUROS, bloque CONDICIONES
  → ¿hacen falta los siniestros? NO
```

**Paso 3 — comprueba si puede evitarse una familia entera.**

```text
¿SE PUEDE OBTENER LA PRIMA SIN LA FAMILIA SEGUROS?

  sí: la prima se paga, y el pago aparece como cargo
  recurrente en la cuenta

  PERO
    · el cargo no distingue prima de otro pago al mismo emisor
    · si la prima es anual, el patrón mensual no la detecta
    · si se paga por descuento en la remuneración, no aparece

  ERROR ESTIMADO
    supuesto: 22 % de las primas no se detectan por cuenta
    efecto sobre la capacidad de ahorro: sobreestimación
    del 4 % al 9 % en los clientes afectados
```

**Paso 4 — decide con el número.**

```text
DECISIÓN: lanzar en fase 1+2 SIN la familia seguros,
declarando la limitación al cliente

MOTIVO
  · fases 1 y 2 están disponibles antes
  · la sobreestimación afecta al 22 % de los clientes
    con seguro, no al total
  · la alternativa —esperar a la fase 5— retrasa
    el producto entero por un término de la fórmula

CÓMO SE DECLARA AL CLIENTE
  «no vemos los seguros que pagas fuera de tus cuentas;
   si tienes alguno, tu capacidad real es algo menor»

  esta frase es parte del producto, no del pie de página
```

**Paso 5 — evita el campo sensible.**

```text
LA FAMILIA CRÉDITOS SE PIDE SIN EL ALCANCE DE MORA

  qué se gana
    · el consentimiento es más fácil de explicar
    · no se trata un dato de dificultad financiera
    · si hay brecha, el dato no estaba

  qué se pierde
    · no se puede advertir «estás en mora»
    · pero: la mora ya se ve en el gasto y en el cargo
      de intereses; el producto puede detectar el síntoma
      sin pedir el diagnóstico
```

**Paso 6 — resuelve el problema de datos de terceros.**

```text
LOS MOVIMIENTOS INCLUYEN TRANSFERENCIAS CON NOMBRE
Y CUENTA DE CONTRAPARTE

  PARA LA FÓRMULA DEL PRODUCTO, ¿HACEN FALTA?
    ingreso recurrente: basta importe + fecha + tipo
    gasto recurrente:   basta importe + fecha + categoría

  → NO se necesita la identidad de la contraparte

  DECISIÓN
    el producto ignora los campos de contraparte
    y lo documenta: «no leemos a quién le transfieres»

    y si el proveedor los envía igualmente,
    se descartan en la ingesta, no se almacenan
```

**Paso 7 — resume el diseño.**

```text
ALCANCES SOLICITADOS: 3
  cuentas:lista
  cuentas:movimientos
  creditos:posicion        (sin mora)

ALCANCES NO SOLICITADOS Y POR QUÉ
  creditos:mora            no hace falta para la fórmula
  inversiones:*            no entra en la fórmula
  seguros:*                se declara la limitación en su lugar

CAMPOS DESCARTADOS EN LA INGESTA
  contraparte.nombre, contraparte.cuenta
```

**Interpreta:** el diseño empezó por una fórmula de cuatro términos y terminó en
tres alcances. Ningún paso consistió en mirar el catálogo de la API: **la fórmula
del producto determinó el dato, y el dato determinó el alcance**.

## 🧭 Perspectivas

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Una cifra de capacidad de ahorro | Si confía en ella |
| Fintech | Fórmula con un término incompleto | Si lanza o espera |
| Banco | Cinco familias con fases distintas | Qué expone y cuándo |
| Aseguradora | Datos de salud en el siniestro | Si los expone |
| Supervisor | Sensibilidad por familia | Qué fase autoriza |
| Auditor | Campos descartados en ingesta | Si se descartan de verdad |
| Tercero no consintiente | Su nombre en un movimiento ajeno | Nada: por eso hay que protegerlo |

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Dice que tengo más de lo que tengo» | Saldo contable vs. disponible | 17, clase 9 |
| «No ve mi seguro» | Familia no expuesta en esta fase | 17, clase 9 |
| «Aparece a quién transferí» | Dato de tercero sin consentimiento | 17, clase 9 |
| «Sabe que estuve en mora» | Alcance de mora concedido | 17, clase 9 |

## ⚖️ Riesgos y controles

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Dato de tercero expuesto | Nombre y cuenta de contraparte | Enmascarar y descartar en ingesta |
| Saldo equivocado | Se usó contable en vez de disponible | Exponer ambos con definición |
| Dato de salud tratado | Siniestro de seguro de vida | Alcance separado o no exponer |
| Valoración sin instante | Precio sin hora | Valor y momento de valoración juntos |
| Mora pedida sin necesidad | Alcance por comodidad | Regla del rechazo (clase 5) |
| Producto cerrado en el mismo alcance | Se agrupó por comodidad | Alcance separado con ventana |

## 🧪 Práctica

En [`labs/lab-03.md`](../labs/lab-03.md):

1. Modela las cinco familias con los tres bloques.
2. Escribe la fórmula de tu producto y deriva el dato mínimo.
3. Identifica un alcance que puedas eliminar y calcula qué pierdes.
4. Enumera los campos que descartarás en la ingesta y demuéstralo con una prueba.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Un solo modelo para todo | Se generalizó desde cuentas | Cada familia tiene su estructura |
| Solo se expone un saldo | No se distinguieron | Contable y disponible, ambos |
| Exclusiones ignoradas | Son texto libre | Sin exclusiones no hay comparación válida |
| Precio sin fecha | Se copió el campo | Valor y momento juntos |
| Contraparte almacenada | Llegó en la respuesta | Descartar en la ingesta |
| Mora en el alcance de posición | Se agrupó por familia | Separar por sensibilidad |

## ❓ Preguntas de comprobación

1. ¿Qué tres bloques describen cualquier producto y qué cambia entre familias?
2. ¿Por qué hay que exponer saldo contable y disponible, y qué pasa si solo se
   expone uno?
3. ¿Cómo se resuelve el problema de los datos de terceros en un movimiento?
4. En el ejemplo guiado, ¿por qué se evitó el alcance de mora sin perder la
   función?
5. ¿Por qué las exclusiones de una póliza son el dato que determina si sirve?

## 📥 Entregable

Guarda en `portfolio/parte-17/clase-09/`:

- el modelo de las cinco familias con sus tres bloques;
- la fórmula de tu producto y la derivación del dato mínimo;
- la lista de alcances solicitados y, sobre todo, la de los no solicitados con su
  motivo;
- la prueba que demuestra que los campos de contraparte se descartan.

## 🔗 Referencias cruzadas

- **Viene de:** clase 4 (clasificación y calidad), clase 5 (consentimiento),
  clase 8 (contrato de API).
- **Continúa en:** clase 10 (iniciación de pagos), clase 12 (privacidad).
- **Se aplica en:** Parte 21, clase 9 (mercado secundario de instrumentos);
  Parte 23, clase 7.

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

- Comisión para el Mercado Financiero. *Anexo técnico del Sistema de Finanzas Abiertas: esquemas por tipo de producto y calendario de fases*. CMF. <https://www.cmfchile.cl/>
- ISO 20022. *Business model and message definitions for account and payment information*. ISO. <https://www.iso20022.org/>
- European Data Protection Board (2021). *Guidelines 06/2020 on the interplay of PSD2 and the GDPR*. EDPB. <https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-062020-interplay-second-payment-services_en>
- International Association of Insurance Supervisors (2023). *Issues paper on insurance sector operational resilience*. IAIS. <https://www.iais.org/>
- IFRS Foundation. *NIIF 9 y NIIF 17: definiciones de instrumento financiero y contrato de seguro*. <https://www.ifrs.org/>
- Verificación local: comprueba qué familias de producto están en fase obligatoria hoy en tu jurisdicción y qué tratamiento reciben los datos de salud y los de terceros. **Fecha de verificación de esta clase: 2026-08-06.** Esta clase no constituye asesoría legal.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 08 · Diseño, versionado e idempotencia](08-diseno-versionado-e-idempotencia.md) | [Parte 17](../README.md) · [Programa](../../../SYLLABUS.md) | [10 · Iniciación de pagos y confirmación de fondos →](10-iniciacion-de-pagos-y-confirmacion-de-fondos.md) |
<!-- gen:footer:end -->
