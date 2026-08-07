---
part: 22
class: 7
title: "Moneda digital de banco central: marco jurídico"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [chile, internacional]
regulatory_topics: [cbdc, curso-legal, privacidad]
regulation_last_verified: 2026-08-06
regulatory_status: en-desarrollo
primary_authorities: [BIS, BCCh, CPMI]
requires_legal_review: true
---

<!-- gen:header:start -->
# Clase 07 · Moneda digital de banco central: marco jurídico

> [← 06 · Protección del cliente y de sus fondos](06-proteccion-del-cliente-y-de-sus-fondos.md) · [Índice de la parte](../README.md) · [08 · Tratamiento prudencial de las exposiciones →](08-tratamiento-prudencial-de-las-exposiciones.md)

**Parte 22 — Regulación de mercados financieros digitales** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Estudiar las decisiones **jurídicas** que una moneda digital de banco central
exige antes que las técnicas: si tiene curso legal, quién puede tenerla, qué se
registra de cada pago y con qué mandato se emite.

## 📚 Objetivos

Al finalizar podrás:

1. **Identificar** las cuatro decisiones jurídicas previas al diseño técnico.
2. **Explicar** qué implica el curso legal y qué no.
3. **Evaluar** un régimen de privacidad por lo que permite y lo que impide.
4. **Analizar** el reparto de responsabilidad en el modelo de dos niveles.
5. **Determinar** qué habilitación legal exige emitir.

<!-- gen:agenda:start -->
## Agenda de 90 minutos

| Minutos | Bloque | Qué ocurre |
|---:|---|---|
| 0–10 | Activación | Pregunta diagnóstica y recuperación de la clase anterior. |
| 10–35 | Conceptos | Desarrollo guiado con la fuente oficial a la vista. |
| 35–55 | Ejemplo guiado | El docente resuelve el caso numérico paso a paso. |
| 55–80 | Práctica | El estudiante replica con datos propios o sintéticos. |
| 80–90 | Cierre | Preguntas de comprobación y registro en el portafolio. |
<!-- gen:agenda:end -->

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| `curso legal` | Obligación de aceptar en pago de una deuda |
| `poder liberatorio` | Que el pago extingue la obligación |
| `habilitación legal` | Norma que faculta al banco central a emitir |
| `modelo de dos niveles` | El banco central emite; los intermediarios distribuyen |
| `titularidad del pasivo` | De quién es el saldo del cliente |
| `anonimato por umbral` | Sin identificación por debajo de un importe |
| `separación de vistas` | Cada actor ve solo lo que necesita |
| `inclusión obligatoria` | Deber de atender a quien no puede usar el canal |

## 🧠 Modelo mental

```text
CUATRO DECISIONES JURÍDICAS, ANTES
DE CUALQUIER DECISIÓN TÉCNICA

  1 ¿HAY HABILITACIÓN LEGAL PARA EMITIRLA?
      la ley orgánica suele hablar de billetes
      y monedas; puede no bastar

  2 ¿TIENE CURSO LEGAL?
      · si sí, todo acreedor debe aceptarla
      · y eso incluye a quien no tiene móvil

  3 ¿DE QUIÉN ES EL SALDO DEL CLIENTE?
      pasivo del banco central en todo momento,
      o pasivo del intermediario
      → decide qué pasa si el intermediario quiebra

  4 ¿QUÉ SE REGISTRA DE CADA PAGO Y QUIÉN LO VE?
      es una decisión política, no técnica

SIN LAS CUATRO, EL PROYECTO TÉCNICO
NO TIENE REQUISITOS: TIENE PREFERENCIAS.
```

## 📖 Desarrollo

### 1. Curso legal y sus consecuencias

```text
CURSO LEGAL SIGNIFICA
  el acreedor debe aceptarla en pago
  y el pago extingue la deuda

LO QUE NO SIGNIFICA
  · no obliga a que todo comercio tenga
    terminal
  · no impide pactar otro medio de pago
  · no convierte en ilegal el efectivo

CONSECUENCIAS QUE HAY QUE RESOLVER
  · quien no tiene teléfono, ¿cómo paga
    y cómo cobra?
  · un corte de red, ¿suspende el curso legal?
  · un comercio sin conexión, ¿incumple?

  → DE AHÍ EL MODO FUERA DE LÍNEA,
    que deja de ser una funcionalidad
    y pasa a ser un requisito jurídico
```

### 2. La titularidad del pasivo

```text
LA PREGUNTA QUE DECIDE LA QUIEBRA
DEL INTERMEDIARIO

  OPCIÓN A · PASIVO DEL BANCO CENTRAL
    el intermediario solo administra
    · si quiebra, el saldo no entra en su masa
    · exige que el banco central lleve el
      registro de titulares o pueda reconstruirlo

  OPCIÓN B · PASIVO DEL INTERMEDIARIO
    respaldado por CBDC que él tiene
    · si quiebra, el cliente es acreedor
    · se parece a un depósito, y entonces
      ¿para qué la CBDC?

  LA OPCIÓN A ES LA COHERENTE
  y obliga a resolver cómo se reconstruye
  el registro si el intermediario desaparece
```

### 3. Privacidad como decisión política

```text
EL RANGO POSIBLE

  EFECTIVO      anónimo, sin registro
  DEPÓSITO      identificado, con registro
  CBDC          en algún punto entre ambos

DISEÑOS QUE ACOTAN
  · el banco central ve importes agregados,
    no identidades
  · el intermediario ve identidad y no el
    detalle de cada pago
  · anonimato por debajo de umbrales bajos,
    como el efectivo
  · separación criptográfica de las vistas

QUÉ NO SE PUEDE PROMETER
  anonimato completo con cumplimiento completo
  → hay que elegir dónde ponerse
    y decirlo en la norma, no en un anexo técnico
```

### 4. Habilitación legal

```text
LA MAYORÍA DE LEYES ORGÁNICAS
FACULTAN A EMITIR «BILLETES Y MONEDAS»

  ¿ALCANZA ESO A UN SALDO DIGITAL?
  · una lectura amplia dice que sí:
    es emisión de dinero
  · una estricta dice que no:
    la ley enumera formas físicas

  Y LA DUDA NO SE RESUELVE CON UN INFORME:
  se resuelve con una reforma o con una
  norma habilitante expresa

QUÉ MÁS EXIGE LA HABILITACIÓN
  · límites de tenencia, si los hay
  · régimen de remuneración, si lo hay
  · reparto de responsabilidad
  · régimen de datos
```

### 5. Reparto de responsabilidad

| Hecho | Quién responde | Por qué |
|---|---|---|
| Pago no autorizado | Intermediario, salvo negligencia del cliente | Es quien autentica |
| Fallo del registro central | Banco central | Es quien lo opera |
| Fallo del intermediario | Intermediario, con continuidad del saldo | El pasivo es del banco central |
| Pérdida del dispositivo | Según el modo de recuperación | Depende del diseño |
| Fraude por ingeniería social | Según diligencia y controles | Régimen general |
| Corte prolongado de red | Nadie, si hay modo fuera de línea | Por eso es requisito |

## 🧮 Ejemplo guiado

**Situación.** Un banco central prepara la propuesta normativa de su CBDC
minorista. Hay que resolver las cuatro decisiones.

```text
DATOS
  población adulta                  15 200 000
  con teléfono inteligente               84 %
  con cuenta bancaria                    88 %
  comercios formales                  620 000
  con terminal de pago                   61 %
  límite de tenencia propuesto          2 000
```

**Paso 1 — resuelve la habilitación.**

```text
LA LEY ORGÁNICA FACULTA A EMITIR
«BILLETES Y MONEDAS»

  OPCIÓN 1 · interpretación amplia
    riesgo: impugnable, y la impugnación
    llegaría cuando ya circule

  OPCIÓN 2 · norma habilitante expresa
    plazo supuesto: 18 meses
    ventaja: certeza

  RECOMENDACIÓN: opción 2
  el coste de 18 meses es menor que el de
  una emisión impugnada
```

**Paso 2 — decide el curso legal.**

```text
SI SE LE DA CURSO LEGAL

  todo acreedor debe aceptarla
  → 620 000 comercios, de los que el 39 %
    no tiene terminal
  → 242 000 comercios tendrían que adaptarse

  COSTE DE ADAPTACIÓN
  supuesto 45 por comercio
  242 000 × 45 = 10 890 000

  Y EL 16 % DE LA POBLACIÓN SIN TELÉFONO
  no podría pagar con ella

SI NO SE LE DA CURSO LEGAL
  · aceptación voluntaria
  · adopción más lenta
  · sin obligación de adaptación

RECOMENDACIÓN
  curso legal con excepción tasada para
  quien no disponga de medios técnicos,
  y modo fuera de línea obligatorio
```

**Paso 3 — resuelve la titularidad.**

```text
PASIVO DEL BANCO CENTRAL EN TODO MOMENTO

  CONSECUENCIA OPERATIVA
  el banco central debe poder reconstruir
  quién tiene qué si un intermediario cae

  DISEÑO
  · el intermediario reporta posiciones
    al cierre de cada día
  · el banco central conserva el agregado
    y la capacidad de reconstruir el detalle
    con la copia del intermediario
  · un tercero conserva copia diaria

  ES EL MISMO PLAN DE SUSTITUCIÓN
  DE LA PARTE 21, CLASE 9
```

**Paso 4 — decide la privacidad.**

```text
PROPUESTA

  TRAMO 1 · hasta 50 por operación y 500 al mes
    sin identificación, como el efectivo
    · el intermediario verifica solo el límite

  TRAMO 2 · por encima
    identificado, con las obligaciones
    ordinarias de prevención

  QUÉ VE CADA UNO
    banco central   importes y agregados,
                    sin identidad
    intermediario   identidad y su relación,
                    sin el detalle de pagos
                    a terceros
    autoridad       con orden judicial, ambos

  Y ESTO VA EN LA NORMA, no en el diseño:
  si va en el diseño, cambia sin debate
```

**Paso 5 — calcula el efecto del límite de tenencia.**

```text
LÍMITE DE 2 000 · 15 200 000 ADULTOS

  migración máxima teórica
  15 200 000 × 2 000 = 30 400 000 000

  supuesto de comportamiento
    30 % no adopta
    45 % mantiene 400 de media
    25 % llena el límite

  migración = 15 200 000 × 45 % × 400
            + 15 200 000 × 25 % × 2 000
            = 2 736 000 000 + 7 600 000 000
            = 10 336 000 000

  → hay que contrastarlo con los depósitos
    a la vista del sistema y calcular
    el efecto sobre el crédito
    (Parte 20, clase 10)
```

**Paso 6 — resuelve la inclusión.**

```text
EL 16 % SIN TELÉFONO INTELIGENTE
= 2 432 000 PERSONAS

  OPCIONES
  · tarjeta física con saldo, sin conexión
  · terminal en oficinas públicas
  · asistencia presencial obligatoria
    en municipios sin cobertura

  SI HAY CURSO LEGAL, LA INCLUSIÓN
  NO ES UNA POLÍTICA: ES UNA CONDICIÓN
  DE LEGALIDAD

  porque obligar a aceptar un medio que
  2,4 millones no pueden usar crea una
  desigualdad que la propia norma provoca
```

**Paso 7 — resume la propuesta.**

```text
  1 HABILITACIÓN    norma expresa, 18 meses
  2 CURSO LEGAL     sí, con excepción tasada
                    y modo fuera de línea obligatorio
  3 TITULARIDAD     pasivo del banco central,
                    con copia diaria en un tercero
  4 PRIVACIDAD      dos tramos, en la norma,
                    con separación de vistas

  MÁS DOS CONDICIONES
  · límite de tenencia de 2 000, revisable
  · tarjeta física para quien no tenga
    teléfono, antes de la entrada en vigor

Y UNA ADVERTENCIA EN LA EXPOSICIÓN
DE MOTIVOS
  el límite de tenencia retrasa una corrida;
  no la evita. Decirlo evita que se le
  atribuya una protección que no da.
```

**Interpreta:** ninguna de las cuatro decisiones es técnica, y las cuatro
condicionan el diseño. **La inclusión deja de ser una política deseable y pasa a
ser una condición de legalidad** en cuanto se otorga curso legal: obligar a
aceptar un medio que 2,4 millones de personas no pueden usar es una desigualdad
creada por la propia norma.

## 🧭 Perspectivas

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un medio de pago del Estado | Si lo usa |
| Persona sin teléfono | Una obligación que no puede cumplir | — |
| Comercio | Obligación de aceptar | Si se adapta |
| Banco | Depósitos que migran | Cómo financia el crédito |
| Banco central | Cuatro decisiones jurídicas | Qué propone |
| Intermediario | Responsabilidad por autenticación | Qué controles pone |
| Legislador | Habilitación y privacidad | Qué aprueba |
| Supervisor | Reparto de responsabilidad | Qué exige |
| Autoridad de datos | Régimen de tratamiento | Qué informa |
| Sociedad | Trazabilidad de sus pagos | Qué acepta |

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Es dinero del Estado» | Y el saldo es pasivo del banco central | 22, clase 7 |
| «Hay que aceptarla» | Solo si tiene curso legal, con excepciones | 22, clase 7 |
| «Van a ver mis pagos» | Depende de la norma, no del diseño | 22, clase 7 |

## ⚖️ Riesgos y controles

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Habilitación dudosa | La emisión se impugna en curso | Norma habilitante expresa |
| Curso legal sin inclusión | Se obliga a quien no puede | Excepción tasada y medio físico |
| Titularidad del intermediario | El cliente es acreedor si quiebra | Pasivo del banco central siempre |
| Privacidad en el diseño | Cambia sin debate | Fijarla en la norma |
| Límite presentado como protección | Se le atribuye evitar corridas | Declarar que solo retrasa |
| Sin modo fuera de línea | Un corte suspende el curso legal | Requisito jurídico, no funcionalidad |

## 🧪 Práctica

En [`labs/lab-03.md`](../labs/lab-03.md):

1. Resuelve las cuatro decisiones para un caso dado.
2. Calcula el coste de adaptación que impone el curso legal.
3. Diseña el régimen de privacidad por tramos con sus vistas.
4. Estima la migración de depósitos y su efecto.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Empezar por el diseño técnico | Es lo que sabe hacer el equipo | Las cuatro decisiones van antes |
| Suponer la habilitación | «Emitir dinero es emitir dinero» | Resolver la duda con norma |
| Curso legal sin excepciones | Parece más fuerte | Crea una desigualdad legal |
| Privacidad como parámetro | Se deja al equipo técnico | Es una decisión política |
| Presentar el límite como escudo | Suena tranquilizador | Retrasa, no evita |
| Inclusión como fase posterior | Se deja para después | Con curso legal, es condición |

## ❓ Preguntas de comprobación

1. ¿Cuáles son las cuatro decisiones jurídicas previas al diseño?
2. ¿Qué implica el curso legal y qué no implica?
3. ¿Por qué la titularidad del pasivo decide la quiebra del intermediario?
4. ¿Por qué la privacidad debe fijarse en la norma y no en el diseño?
5. ¿Por qué la inclusión pasa a ser condición de legalidad con curso legal?

## 📥 Entregable

Guarda en `portfolio/parte-22/clase-07/`:

- las cuatro decisiones resueltas con su fundamento;
- el coste de adaptación del curso legal;
- el régimen de privacidad por tramos con las vistas de cada actor;
- la estimación de migración con sus supuestos.

## 🔗 Referencias cruzadas

- **Viene de:** Parte 20, clase 10; clases 1 y 4 de esta parte.
- **Continúa en:** clases 13 y 15 de esta parte.
- **Se aplica en:** clase 18 de esta parte; Parte 23, clase 5.

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

- Committee on Payments and Market Infrastructures (2020). *Central bank digital currencies: foundational principles and core features*. BIS. <https://www.bis.org/publ/othp33.htm>
- Bank for International Settlements (2021). *CBDCs: an opportunity for the monetary system*, Annual Economic Report. BIS. <https://www.bis.org/publ/arpdf/ar2021e3.htm>
- Banco Central de Chile (2022). *Emisión de moneda digital de banco central en Chile*. BCCh. <https://www.bcentral.cl/documents/33528/3060272/Informe_CBDC.pdf>
- Bank for International Settlements (2021). *Central bank digital currencies: financial stability implications*. BIS. <https://www.bis.org/publ/othp42_fin_stab.htm>
- Verificación local: comprueba si la ley orgánica de tu banco central habilita a emitir dinero digital, qué medios tienen curso legal y qué régimen de datos aplicaría. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 06 · Protección del cliente y de sus fondos](06-proteccion-del-cliente-y-de-sus-fondos.md) | [Parte 22](../README.md) · [Programa](../../../SYLLABUS.md) | [08 · Tratamiento prudencial de las exposiciones →](08-tratamiento-prudencial-de-las-exposiciones.md) |
<!-- gen:footer:end -->
