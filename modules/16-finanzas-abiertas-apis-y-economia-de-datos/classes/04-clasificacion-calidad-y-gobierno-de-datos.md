---
part: 17
class: 4
title: "Clasificación, calidad y gobierno de datos financieros"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global, chile]
regulatory_topics: [open-finance, proteccion-de-datos, gobierno-del-dato]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [CMF]
requires_legal_review: false
---

<!-- gen:header:start -->
# Clase 04 · Clasificación, calidad y gobierno de datos financieros

> [← 03 · El Sistema de Finanzas Abiertas de Chile](03-sistema-de-finanzas-abiertas-de-chile.md) · [Índice de la parte](../README.md) · [05 · Consentimiento: creación, vigencia, renovación y revocación →](05-consentimiento-ciclo-de-vida.md)

**Parte 17 — Finanzas abiertas, APIs y economía de datos** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Aprender a clasificar un dato financiero **antes** de exponerlo, y a medir su
calidad con números. Una API de finanzas abiertas expone datos que otra empresa
usará para decidir; si el dato es de mala calidad, el error se propaga con la
firma de quien lo publicó.

## 📚 Objetivos

Al finalizar podrás:

1. **Clasificar** un dato por sensibilidad, titularidad y finalidad admisible.
2. **Medir** la calidad de un conjunto de datos con seis dimensiones y umbrales.
3. **Diseñar** el diccionario de datos que acompaña a una API pública.
4. **Detectar** inferencias sensibles que un dato aparentemente inocuo permite.
5. **Decidir** qué dato no se expone, y justificarlo por escrito.

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
| `clasificación` | Asignar a un dato un nivel de sensibilidad y un tratamiento |
| `dato derivado` | Dato producido por cálculo sobre otros datos |
| `dato inferido` | Atributo deducido que el titular nunca declaró |
| `linaje` | Trazabilidad del dato desde su origen hasta su uso |
| `diccionario de datos` | Definición formal de cada campo, su tipo y su significado |
| `calidad del dato` | Grado en que el dato sirve para la decisión que sostiene |
| `minimización` | Tratar solo el dato necesario para la finalidad declarada |
| `finalidad` | Uso declarado y limitado para el que se obtuvo el dato |

## 🧠 Modelo mental

```text
TRES PREGUNTAS ANTES DE EXPONER UN CAMPO

  1. ¿DE QUIÉN ES?
       del cliente        → consentimiento
       de la entidad      → decisión comercial
       de un tercero      → no es tuyo para compartirlo

  2. ¿QUÉ PERMITE INFERIR?
       el campo «comercio» de un movimiento
       permite inferir salud, religión, afiliación y domicilio
       → la sensibilidad del dato NO es la del campo:
         es la de lo que el campo permite deducir

  3. ¿PARA QUÉ SE VA A USAR?
       si la finalidad no está declarada, el dato no se expone
       «por si sirve después» no es una finalidad
```

## 📖 Desarrollo

### 1. Clasificación por sensibilidad efectiva

| Nivel | Ejemplo de campo | Tratamiento |
|---|---|---|
| Público | Comisión de mantención publicada | Sin restricción |
| Interno | Volumen agregado de la entidad | Sin exposición externa |
| Personal | Saldo, movimientos, productos | Consentimiento y finalidad |
| Personal sensible por inferencia | Comercio, glosa, geolocalización del gasto | Consentimiento reforzado o no exponer |
| Prohibido | Credencial, semilla, clave privada | Nunca sale del sistema |

```text
LA CATEGORÍA QUE MÁS SE SUBESTIMA ES LA CUARTA

  «pago en Clínica Oncológica»          → estado de salud
  «transferencia mensual a Fundación X» → convicción
  «pago recurrente en guardería»        → estructura familiar
  «compra semanal, misma calle, 07:45»  → domicilio y rutina

  ninguno de esos campos se llama «salud», «religión» ni «domicilio».
  Todos los revelan.
```

### 2. Dato declarado, derivado e inferido

```text
DECLARADO   el cliente lo dio:      renta declarada, teléfono
DERIVADO    se calculó:             gasto medio mensual, deuda total
INFERIDO    se dedujo:              probablemente tiene hijos,
                                    probablemente cambiará de trabajo

EL RÉGIMEN NO ES EL MISMO
  el declarado se corrige pidiéndoselo al cliente
  el derivado se corrige recalculando
  el inferido NO SE PUEDE CORREGIR: el cliente ni siquiera
  sabe que existe, y el error se propaga sin señal

  → todo dato inferido que afecte a una decisión sobre la persona
    debe ser explicable y contestable (Parte 14, clase 11)
```

### 3. Seis dimensiones de calidad, con umbral

| Dimensión | Pregunta | Métrica | Umbral sugerido |
|---|---|---|---|
| Completitud | ¿Faltan valores? | % de nulos en campos obligatorios | < 0,1 % |
| Exactitud | ¿Coincide con la realidad? | % de discrepancias en muestra auditada | < 0,5 % |
| Consistencia | ¿Cuadra consigo mismo? | % de saldos que no igualan la suma de movimientos | 0 % |
| Puntualidad | ¿Está al día? | Retardo p95 respecto del hecho económico | < 60 s |
| Unicidad | ¿Hay duplicados? | % de identificadores repetidos | 0 % |
| Validez | ¿Cumple el formato? | % de valores fuera del dominio declarado | 0 % |

```text
LA CONSISTENCIA ES LA ÚNICA QUE ADMITE UMBRAL CERO
  si el saldo no es la suma de los movimientos,
  no es un problema de calidad: es un descuadre contable
```

### 4. El diccionario de datos

Cada campo expuesto necesita, como mínimo:

```text
nombre técnico        booking_date
nombre funcional      fecha de contabilización
tipo                  string, ISO 8601 con zona horaria
obligatorio           sí
dominio               fechas entre la apertura de la cuenta y hoy
significado           instante en que el movimiento afecta al saldo contable
NO significa          la fecha en que el cliente hizo la operación
origen                sistema central, tabla de movimientos
frecuencia            tiempo real
nulo permitido        no
ejemplo               2026-06-30T03:14:00Z
```

La línea **«NO significa»** es la que evita la mitad de los incidentes de
integración. Un tercero que confunde fecha de operación con fecha de
contabilización produce categorizaciones desplazadas un día, y el cliente ve un
gasto en el mes equivocado.

### 5. Gobierno: quién responde de qué

```text
PROPIETARIO DEL DATO      área de negocio; decide finalidad y acceso
CUSTODIO                  tecnología; garantiza integridad y disponibilidad
ADMINISTRADOR DE CALIDAD  mide, publica y escala los incumplimientos
OFICIAL DE PRIVACIDAD     valida finalidad, base de licitud y retención
AUDITORÍA                 verifica que lo anterior ocurre

REGLA PRÁCTICA
  un dato sin propietario nombrado no se expone.
  «es del banco» no es un propietario.
```

## 🧮 Ejemplo guiado

**Situación.** Antes de publicar la API de movimientos, calidad audita una muestra
de 50 000 movimientos de 2 400 cuentas.

```text
RESULTADOS DE LA AUDITORÍA

  movimientos totales                      50 000
  con campo «glosa» vacío                   1 340
  con «comercio» sin normalizar             8 900
  con importe positivo en cargos                17
  identificadores duplicados                     6
  saldo de la cuenta ≠ suma de movimientos      31 cuentas de 2 400
  retardo p95 desde el hecho económico       42 s
  fechas fuera del rango de la cuenta          104
```

**Paso 1 — calcula cada dimensión.**

```text
COMPLETITUD (campos obligatorios)
  «glosa» NO es obligatorio → no computa aquí
  campos obligatorios sin valor: 0 → 0,00 %      ✓

VALIDEZ
  importe positivo en cargo:  17 / 50 000 = 0,034 %   ✗ (umbral 0 %)
  fecha fuera de rango:      104 / 50 000 = 0,208 %   ✗

UNICIDAD
  6 / 50 000 = 0,012 %                                ✗ (umbral 0 %)

CONSISTENCIA
  31 / 2 400 cuentas = 1,29 %                         ✗✗ (umbral 0 %)

PUNTUALIDAD
  p95 = 42 s < 60 s                                   ✓

EXACTITUD
  no medida en esta auditoría                         ⚠ sin dato
```

**Paso 2 — ordena por gravedad, no por magnitud.**

```text
1,29 % de descuadre parece pequeño al lado de
17,8 % de comercios sin normalizar.
No lo es.

DESCUADRE (31 cuentas)
  el saldo que publicaremos no cuadra con los movimientos
  que publicaremos, en la misma respuesta
  → un tercero que sume verá el error inmediatamente
  → es un defecto de INTEGRIDAD, no de presentación

COMERCIO SIN NORMALIZAR (8 900)
  la categorización del tercero será peor
  → es un defecto de UTILIDAD
  → degrada el producto, no lo invalida
```

**Paso 3 — cuantifica el impacto del descuadre.**

```text
2 400 cuentas en la muestra, 31 con descuadre = 1,29 %

SI LA CARTERA TIENE 1 850 000 CUENTAS
  1 850 000 × 1,29 % ≈ 23 900 cuentas con descuadre

SI EL 12 % DE LOS CLIENTES OTORGA CONSENTIMIENTO
  23 900 × 12 % ≈ 2 870 clientes verían el error

CON 158 LLAMADAS POR CLIENTE Y TRIMESTRE
  ≈ 453 000 respuestas incoherentes por trimestre
```

**Paso 4 — investiga la causa del descuadre.**

```text
HIPÓTESIS A · movimientos en curso no contabilizados
  → si es esto, NO es un descuadre: es que se están
    mezclando saldo disponible y saldo contable

HIPÓTESIS B · movimientos anteriores a la ventana de 24 meses
  → el saldo incluye historia que los movimientos no muestran

HIPÓTESIS C · error real de contabilización

VERIFICACIÓN
  se recalcula el saldo contable a partir de los movimientos
  de los últimos 24 meses MÁS el saldo inicial de la ventana

  resultado: 29 de las 31 cuentas cuadran con esa fórmula
             2 no cuadran por ningún camino
```

**Paso 5 — reformula el problema.**

```text
NO HABÍA 31 CUENTAS DESCUADRADAS
HABÍA UN CAMPO QUE FALTA EN LA API

  «saldo al inicio de la ventana consultada»

  sin ese campo, el tercero no puede reconstruir el saldo
  y concluye que el proveedor publica datos incoherentes

  29 de 31 casos eran un defecto de DISEÑO DEL CONTRATO,
  no de calidad del dato

  2 de 31 sí son error contable → escalado al área responsable
```

**Paso 6 — decide.**

```text
BLOQUEAR LA PUBLICACIÓN hasta corregir:
  · validez: 17 signos invertidos y 104 fechas fuera de rango
  · unicidad: 6 duplicados
  · contrato: añadir «saldo al inicio de la ventana»
  · los 2 casos de error contable real

NO BLOQUEAR por:
  · comercios sin normalizar (8 900)
    → se publica con el campo tal cual, se DECLARA en el
      diccionario que no está normalizado, y se abre un plan
    → publicar un dato imperfecto y declararlo
      es mejor que retenerlo o que maquillarlo

MEDIR LO QUE NO SE MIDIÓ
  la exactitud quedó sin dato: se programa auditoría
  contra el sistema central antes del siguiente hito
```

**Interpreta:** la auditoría encontró un problema de calidad y, al investigarlo,
apareció un defecto de **contrato**. Es lo habitual: la mayoría de los «datos
malos» de una API son datos correctos expuestos sin el campo que los hace
interpretables.

## 🧭 Perspectivas

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un gasto en el mes equivocado | Si confía en la app |
| Fintech | Saldos que no cuadran | Si integra o descarta al proveedor |
| Banco | Coste de normalizar comercios | Cuánto invierte en calidad |
| Infraestructura | Retardo de publicación | Arquitectura de eventos |
| Supervisor | Reclamos por datos erróneos | Si exige métricas de calidad |
| Auditor | Ausencia de medición de exactitud | Qué observa |
| Oficial de privacidad | Campo con inferencia sensible | Si autoriza su exposición |
| Sociedad | Decisiones automáticas sobre datos malos | Exigencia de explicabilidad |

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «El gasto salió en otro mes» | Fecha de operación vs. contabilización | 17, clase 4 |
| «La app dice otro saldo» | Falta el saldo inicial de la ventana | 17, clase 4 |
| «Categoriza mal mis compras» | Comercio sin normalizar | 17, clase 4 |
| «¿Cómo saben que tengo hijos?» | Dato inferido no declarado | 17, clase 12 |

## ⚖️ Riesgos y controles

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Inferencia sensible | Un campo revela salud o convicción | Clasificación por inferencia, no por nombre |
| Descuadre publicado | Saldo y movimientos no coinciden | Consistencia con umbral cero |
| Campo mal entendido | El tercero confunde dos fechas | Línea «NO significa» en el diccionario |
| Dato inferido no contestable | El cliente no puede corregirlo | Explicabilidad y vía de impugnación |
| Retención indefinida | «Por si sirve después» | Política de retención por finalidad |
| Dato sin propietario | Nadie decide ni responde | Propietario nombrado antes de exponer |

## 🧪 Práctica

En [`labs/lab-03.md`](../labs/lab-03.md):

1. Clasifica quince campos por sensibilidad efectiva, no por su nombre.
2. Calcula las seis dimensiones sobre el dataset sintético del repositorio.
3. Escribe el diccionario de tres campos, con la línea «NO significa».
4. Identifica un campo que decidas **no** exponer, y justifícalo por escrito.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Clasificar por nombre del campo | No se pensó en la inferencia | Clasifica por lo que permite deducir |
| Calidad medida solo por nulos | Se usó una sola dimensión | Usa las seis |
| Descuadre tratado como estético | No se distinguió integridad de utilidad | Consistencia con umbral cero |
| Diccionario sin «NO significa» | Se documentó el tipo, no el significado | Añade la línea |
| Dato inferido sin explicación | Se trató como un dato más | Explicable y contestable |
| Publicar y no declarar el defecto | Se prefirió no mostrar debilidad | Declarar es más barato que el incidente |

## ❓ Preguntas de comprobación

1. ¿Por qué la sensibilidad de un campo no es la del campo, sino la de lo que
   permite inferir? Da dos ejemplos.
2. ¿Qué distingue un dato derivado de uno inferido, y por qué el segundo es más
   difícil de corregir?
3. ¿Cuál de las seis dimensiones admite umbral cero y por qué?
4. En el ejemplo guiado, ¿por qué 29 de los 31 descuadres no eran un problema de
   calidad?
5. ¿Por qué publicar un dato imperfecto declarándolo es mejor que retenerlo?

## 📥 Entregable

Guarda en `portfolio/parte-17/clase-04/`:

- la clasificación de quince campos por sensibilidad efectiva;
- las seis dimensiones calculadas sobre un conjunto sintético;
- el diccionario de tres campos con su línea «NO significa»;
- la justificación escrita de un campo que decidiste no exponer.

## 🔗 Referencias cruzadas

- **Viene de:** Parte 14, clase 4 (datos en un banco); Parte 14, clase 11 (ética
  algorítmica); clase 1 de esta parte.
- **Continúa en:** clase 9 (APIs de información), clase 12 (privacidad y
  portabilidad).
- **Se aplica en:** Parte 18, clase 6 (datos estructurados en ISO 20022);
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

- ISO/IEC 25012. *Data quality model*. International Organization for Standardization. <https://www.iso.org/standard/35736.html>
- Basel Committee on Banking Supervision (2013). *BCBS 239 — Principles for effective risk data aggregation and risk reporting*. BIS. <https://www.bis.org/publ/bcbs239.htm>
- Comisión para el Mercado Financiero. *Anexo técnico del Sistema de Finanzas Abiertas: definiciones y esquemas de datos*. CMF. <https://www.cmfchile.cl/>
- OECD (2021). *Recommendation of the Council on Enhancing Access to and Sharing of Data*. OECD. <https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0463>
- NIST (2020). *NIST Privacy Framework 1.0*. National Institute of Standards and Technology. <https://www.nist.gov/privacy-framework>
- Verificación local: comprueba qué esquema de datos exige el anexo técnico vigente en tu jurisdicción y qué categorías de dato personal recibe tratamiento reforzado. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 03 · El Sistema de Finanzas Abiertas de Chile](03-sistema-de-finanzas-abiertas-de-chile.md) | [Parte 17](../README.md) · [Programa](../../../SYLLABUS.md) | [05 · Consentimiento: creación, vigencia, renovación y revocación →](05-consentimiento-ciclo-de-vida.md) |
<!-- gen:footer:end -->
