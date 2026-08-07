---
part: 19
class: 8
title: "Contratos inteligentes"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global]
regulatory_topics: [dlt, riesgo-operacional, contratos]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [IOSCO, NIST]
requires_legal_review: true
---

<!-- gen:header:start -->
# Clase 08 · Contratos inteligentes

> [← 07 · Redes públicas, privadas y autorizadas](07-redes-publicas-privadas-y-autorizadas.md) · [Índice de la parte](../README.md) · [09 · Oráculos →](09-oraculos.md)

**Parte 19 — Blockchain y DLT para instituciones financieras** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Tratar un contrato inteligente por lo que es: **código irreversible con dinero
dentro**. No es un contrato, no es inteligente, y el error que contenga se
ejecutará exactamente como está escrito.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** contrato inteligente de contrato jurídico y decir qué relación
   tienen.
2. **Identificar** los seis defectos que concentran la mayor parte de las
   pérdidas conocidas.
3. **Diseñar** un contrato con máquina de estados explícita y límites.
4. **Evaluar** los mecanismos de actualización y su coste en descentralización.
5. **Decidir** qué debe ir en el código y qué debe quedar fuera.

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
| `contrato inteligente` | Código que se ejecuta en el registro y controla activos |
| `determinismo` | El mismo estado y la misma entrada dan el mismo resultado |
| `reentrada` | Una llamada externa vuelve al contrato antes de que termine |
| `interruptor de emergencia` | Mecanismo para detener la ejecución |
| `contrato actualizable` | Diseño que permite cambiar la lógica tras el despliegue |
| `invariante` | Propiedad que debe cumplirse siempre |
| `coste de ejecución` | Recurso que se consume al ejecutar |
| `verificación formal` | Demostración matemática de una propiedad del código |

## 🧠 Modelo mental

```text
TRES COSAS QUE NO ES

  NO ES UN CONTRATO
    no expresa consentimiento, no interpreta,
    no tiene remedios ante un incumplimiento
    → el contrato jurídico existe aparte, y es el que vale

  NO ES INTELIGENTE
    ejecuta lo escrito, incluido el error

  NO ES INMUTABLE «PARA BIEN»
    la inmutabilidad protege del cambio arbitrario
    Y ATRAPA el defecto

LA CONSECUENCIA OPERATIVA
  el momento del despliegue es el último momento
  en que se puede corregir barato
```

## 📖 Desarrollo

### 1. La relación con el contrato jurídico

```text
TRES CONFIGURACIONES POSIBLES

  A · el código EJECUTA lo que el contrato dice
      el contrato manda; el código es la herramienta
      si discrepan, vale el contrato

  B · el código ES el acuerdo
      «el código es la ley»
      → sin remedio ante un defecto, y sin foro

  C · híbrida
      el contrato jurídico define qué ocurre
      si el código se comporta de forma imprevista

LA (C) ES LA ÚNICA DEFENDIBLE EN FINANZAS
  y exige escribir de antemano la cláusula
  «qué pasa si el código hace algo que no queríamos»
```

### 2. Los seis defectos que concentran las pérdidas

| Defecto | Qué ocurre | Control |
|---|---|---|
| **Reentrada** | Una llamada externa vuelve antes de actualizar el estado | Actualizar el estado antes de llamar |
| **Control de acceso** | Una función crítica sin restricción | Comprobación explícita en cada función |
| **Aritmética** | Desbordamiento o división que no se previó | Tipos con control y comprobaciones |
| **Dependencia de un dato externo** | El precio viene de una fuente manipulable | Ver clase 9 |
| **Suposición sobre el orden** | Otro observa la operación y actúa antes | Ver clase 12 |
| **Inicialización** | El contrato queda sin dueño o con dueño ajeno | Inicialización atómica con el despliegue |

```text
LOS SEIS TIENEN ALGO EN COMÚN
  ninguno es un fallo del registro: son fallos
  del programa que corre sobre él

  → un registro perfectamente seguro ejecuta
    un contrato defectuoso con total fidelidad
```

### 3. Diseñar con máquina de estados

```text
UN CONTRATO FINANCIERO SIN MÁQUINA DE ESTADOS
ES UN CONJUNTO DE FUNCIONES QUE CUALQUIERA
PUEDE LLAMAR EN CUALQUIER ORDEN

  DEPÓSITO EN GARANTÍA, BIEN MODELADO
    creado ──depositar──► fondeado
    fondeado ──confirmar──► liberado
    fondeado ──disputar──► en_disputa
    fondeado ──vencer──► devuelto
    en_disputa ──resolver──► liberado | devuelto

  cada función comprueba el estado de partida
  y ninguna transición vuelve atrás

Y ADEMÁS, INVARIANTES QUE SE COMPRUEBAN SIEMPRE
  · el saldo del contrato = suma de depósitos activos
  · ningún depósito puede liberarse y devolverse
  · el total nunca es negativo
```

### 4. Actualización: la tensión central

```text
UN CONTRATO NO ACTUALIZABLE
  · no se puede corromper por un cambio
  · no se puede arreglar si tiene un defecto

UN CONTRATO ACTUALIZABLE
  · se puede corregir
  · quien controla la actualización controla los fondos

  → la «descentralización» de un contrato actualizable
    es la de quien tiene la llave de actualización

MECANISMOS INTERMEDIOS
  · actualización con retardo obligatorio (los usuarios
    pueden salir antes de que entre en vigor)
  · actualización con firma múltiple y umbral alto
  · actualización solo para corregir, no para cambiar
    reglas económicas
  · interruptor de emergencia que solo PARA, no altera

EL INTERRUPTOR QUE SOLO PARA ES EL MEJOR COMPROMISO
  permite contener un incidente sin dar
  a nadie la capacidad de mover fondos
```

### 5. Qué debe quedar fuera del código

```text
FUERA
  · el juicio: «si la mercancía es de calidad aceptable»
  · lo que depende de un hecho no verificable en la red
  · los datos personales
  · las excepciones que exigen criterio
  · la interpretación del contrato jurídico

DENTRO
  · la custodia condicionada de fondos
  · las transiciones objetivas y verificables
  · los límites y los plazos
  · el registro de lo ocurrido

LA REGLA
  si para decidir hace falta una persona,
  el código no decide: el código ESPERA a que
  la persona decida, y ejecuta esa decisión
```

## 🧮 Ejemplo guiado

**Situación.** Un banco despliega un contrato de depósito en garantía para
operaciones de comercio exterior entre clientes. Antes del despliegue, revisión.

```text
LO QUE HACE EL CONTRATO
  el importador deposita
  el exportador embarca y presenta documentos
  un verificador confirma
  el contrato libera al exportador
  si no hay confirmación en 45 días, devuelve al importador

VOLUMEN PREVISTO
  operaciones al mes                  340
  importe medio                   180 000
  saldo máximo simultáneo      28 000 000
```

**Paso 1 — revisa el control de acceso.**

```text
FUNCIONES DEL CONTRATO
  depositar()      cualquiera            ✓ correcto
  confirmar()      cualquiera            ✗ DEFECTO
  devolver()       cualquiera            ✗ DEFECTO
  retirar()        solo el destinatario  ✓

HALLAZGO 1
  confirmar() sin restricción permite a cualquiera
  liberar los fondos al exportador sin que haya
  embarcado nada

  gravedad: máxima. Es el defecto más común y el más caro.
```

**Paso 2 — revisa el orden de operaciones.**

```text
CÓDIGO DE retirar()
  1. comprobar saldo del beneficiario
  2. TRANSFERIR los fondos
  3. poner el saldo a cero

HALLAZGO 2 · REENTRADA
  si el beneficiario es a su vez un contrato,
  puede volver a llamar a retirar() durante el paso 2,
  cuando el saldo todavía no es cero

  → puede vaciar el contrato

CORRECCIÓN
  1. comprobar
  2. poner el saldo a cero
  3. transferir
```

**Paso 3 — revisa el plazo de 45 días.**

```text
¿CÓMO SABE EL CONTRATO QUE HAN PASADO 45 DÍAS?

  usa la marca de tiempo del bloque

  ESA MARCA LA PONE EL PRODUCTOR, con margen de tolerancia
  → un productor puede adelantarla o retrasarla
    dentro de ese margen

  ¿IMPORTA AQUÍ?
    con un margen de segundos sobre un plazo de 45 días,
    no. Con un plazo de 5 minutos, sí.

  HALLAZGO 3 · gravedad baja, pero se documenta:
  el contrato depende de una fuente de tiempo
  que no controla
```

**Paso 4 — busca lo que el código no debería decidir.**

```text
«UN VERIFICADOR CONFIRMA»

  ¿quién es el verificador? ¿cómo se designa?
  ¿qué pasa si no confirma por error?
  ¿qué pasa si confirma y los documentos eran falsos?

  EL CÓDIGO NO PUEDE RESPONDER NINGUNA
  → y no debe intentarlo

  LO CORRECTO
    el código guarda la dirección del verificador,
    designado en el contrato jurídico
    el código EJECUTA su decisión
    el contrato jurídico dice qué ocurre si se equivoca

HALLAZGO 4
  el contrato jurídico correspondiente no existe todavía.
  Se está desplegando el código sin el acuerdo que
  le da sentido.
```

**Paso 5 — evalúa el mecanismo de actualización.**

```text
EL CONTRATO ES ACTUALIZABLE POR UNA SOLA CLAVE
DEL EQUIPO DE DESARROLLO

  → esa clave puede cambiar la lógica y mover
    28 000 000

HALLAZGO 5
  la clave de actualización es, en la práctica,
  la clave de los fondos

CORRECCIÓN PROPUESTA
  · interruptor de emergencia (solo detiene) con
    firma 2-de-3 del equipo de operaciones
  · actualización de lógica con firma 4-de-7 del comité,
    retardo obligatorio de 7 días y aviso a los usuarios
  · las reglas económicas (plazos, destinatarios)
    NO son actualizables: exigen desplegar de nuevo
```

**Paso 6 — cuantifica antes de decidir el despliegue.**

```text
EXPOSICIÓN MÁXIMA: 28 000 000

  HALLAZGOS 1 Y 2 permiten vaciarlo
  HALLAZGO 5 permite vaciarlo a una sola persona

  COSTE DE CORREGIR
    revisión y corrección           1 800 000
    auditoría externa               3 200 000
    verificación formal de los
    invariantes principales         4 500 000
    TOTAL                           9 500 000

  9 500 000 sobre 28 000 000 de exposición máxima
  = 34 %

  parece mucho, y la comparación correcta no es esa:
  es contra la pérdida esperada de desplegar con
  dos defectos de gravedad máxima, que es
  prácticamente la exposición completa
```

**Paso 7 — decide.**

```text
NO DESPLEGAR. CONDICIONES PARA RECONSIDERAR:

  1. corregir los hallazgos 1, 2 y 5
  2. auditoría externa independiente, con informe público
     para los participantes
  3. verificación formal de los tres invariantes
  4. contrato jurídico firmado ANTES del despliegue,
     con la cláusula de comportamiento imprevisto
  5. despliegue por fases: límite de 500 000 de saldo
     durante 90 días, luego 5 000 000, luego sin límite
  6. interruptor de emergencia probado en preproducción
     y en producción, con un simulacro trimestral

  Y UNA REGLA DE OPERACIÓN
    el límite de la fase 1 no se levanta por calendario:
    se levanta cuando se cumplan 90 días SIN incidentes
    y con el simulacro ejecutado
```

**Interpreta:** cinco hallazgos, y el más caro no era ninguno de los técnicos:
**el contrato jurídico que le da sentido no existía**. El código estaba a punto
de custodiar 28 millones bajo un acuerdo que nadie había escrito.

## 🧭 Perspectivas

| Actor | Qué ve | Qué decide |
|---|---|---|
| Importador | Fondos retenidos hasta confirmar | Si acepta el mecanismo |
| Exportador | Cobro condicionado a un tercero | Si embarca |
| Verificador | Una responsabilidad sin contrato | Si acepta el rol |
| Banco | 28 M en un código | Si despliega |
| Desarrollo | Una clave de actualización | Si acepta el reparto |
| Auditor | Dos defectos de gravedad máxima | Qué informa |
| Asesor jurídico | Código sin contrato | Qué exige antes |

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «El sistema liberó el pago solo» | Control de acceso ausente | 19, clase 8 |
| «Nadie puede cambiarlo, es seguro» | Inmutable también atrapa el defecto | 19, clase 8 |
| «¿Y si el verificador se equivoca?» | Eso lo resuelve el contrato jurídico | 19, clase 8 |

## ⚖️ Riesgos y controles

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Función crítica sin restricción | Cualquiera libera fondos | Comprobación explícita por función |
| Reentrada | Se vacía el contrato | Estado antes de la llamada externa |
| Clave de actualización única | Una persona controla los fondos | Firma múltiple y retardo |
| Código sin contrato jurídico | Sin remedio ante lo imprevisto | Acuerdo firmado antes del despliegue |
| Dependencia de la marca de tiempo | Margen manipulable | Plazos largos o fuente propia |
| Despliegue sin límites | La exposición es máxima desde el día 1 | Fases con límite y condición de salida |

## 🧪 Práctica

En [`labs/lab-05.md`](../labs/lab-05.md):

1. Implementa el depósito en garantía con su máquina de estados.
2. Introduce el defecto de reentrada y demuestra que vacía el contrato.
3. Corrígelo y demuestra que la prueba ahora falla en el atacante.
4. Implementa el interruptor de emergencia y su simulacro.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| «El código es el contrato» | Se adoptó un eslogan | El contrato jurídico existe aparte |
| Funciones sin control de acceso | Se probó el camino feliz | Comprobación explícita en cada una |
| Transferir antes de actualizar | Orden natural al escribir | Estado primero, llamada después |
| Actualización con una clave | Se buscó agilidad | Es la clave de los fondos |
| Desplegar sin límite | Se confió en la revisión | Fases con condición de salida |
| Meter juicio en el código | Se quiso automatizar todo | El código ejecuta, no juzga |

## ❓ Preguntas de comprobación

1. ¿Por qué un contrato inteligente no es un contrato ni es inteligente?
2. ¿Cuáles son los seis defectos y qué tienen en común?
3. ¿Por qué la clave de actualización es la clave de los fondos?
4. ¿Qué debe quedar fuera del código y cuál es la regla que lo decide?
5. En el ejemplo guiado, ¿cuál fue el hallazgo más grave y por qué no era
   técnico?

## 📥 Entregable

Guarda en `portfolio/parte-19/clase-08/`:

- la máquina de estados de tu contrato, con sus invariantes;
- la demostración del defecto de reentrada y su corrección;
- el diseño del mecanismo de actualización, con su justificación;
- la lista de lo que queda fuera del código y por qué.

## 🔗 Referencias cruzadas

- **Viene de:** clases 3, 4 y 7; Parte 17, clase 8 (máquinas de estado).
- **Continúa en:** clase 9 (oráculos), clase 12 (orden), clase 13 (recuperación).
- **Se aplica en:** Parte 21, clases 3 y 12; Parte 23, clases 12 y 13.

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

- IOSCO (2022). *Decentralized Finance Report*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD699.pdf>
- NIST (2018). *NISTIR 8202: Blockchain Technology Overview*. NIST. <https://csrc.nist.gov/pubs/ir/8202/final>
- OWASP Foundation. *Smart Contract Top 10*. OWASP. <https://owasp.org/www-project-smart-contract-top-10/>
- European Union Agency for Cybersecurity (2021). *Distributed Ledger Technology and Cybersecurity*. ENISA. <https://www.enisa.europa.eu/>
- Committee on Payments and Market Infrastructures (2017). *Distributed ledger technology in payment, clearing and settlement*. BIS. <https://www.bis.org/cpmi/publ/d157.htm>
- Verificación local: comprueba qué eficacia jurídica reconoce tu ordenamiento a la ejecución automatizada y qué remedios existen ante un comportamiento no querido del código. **Fecha de verificación de esta clase: 2026-08-06.** Esta clase no constituye asesoría legal.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 07 · Redes públicas, privadas y autorizadas](07-redes-publicas-privadas-y-autorizadas.md) | [Parte 19](../README.md) · [Programa](../../../SYLLABUS.md) | [09 · Oráculos →](09-oraculos.md) |
<!-- gen:footer:end -->
