---
part: 17
class: 14
title: "Proyecto: agregador financiero regulado"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global, chile]
regulatory_topics: [open-finance, licenciamiento, seguridad, proteccion-de-datos]
regulation_last_verified: 2026-08-06
regulatory_status: en-despliegue-por-fases
primary_authorities: [CMF]
requires_legal_review: true
---

<!-- gen:header:start -->
# Clase 14 · Proyecto: agregador financiero regulado

> [← 13 · Disponibilidad, SLA, observabilidad e incidentes](13-disponibilidad-sla-y-observabilidad.md) · [Índice de la parte](../README.md) · [Proyecto de la parte →](../project/README.md)

**Parte 17 — Finanzas abiertas, APIs y economía de datos** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Integrar las trece clases en una decisión defendible: el expediente completo de un
agregador financiero, desde el dato mínimo hasta la defensa ante un comité que
pregunta lo que un comité pregunta.

## 📚 Objetivos

Al finalizar podrás:

1. **Construir** el expediente completo del proyecto con sus doce piezas.
2. **Priorizar** el modelo de amenazas por impacto y probabilidad, no por
   novedad técnica.
3. **Defender** cada decisión con el dato que la sostiene y la alternativa
   descartada.
4. **Declarar** los límites del trabajo sin que eso lo debilite.
5. **Evaluar** el proyecto de otra persona con la rúbrica, actuando de revisor.

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
| `expediente` | Conjunto de documentos y evidencias que sostienen una autorización |
| `registro de decisiones` | Cada decisión con su alternativa descartada y su motivo |
| `modelo de amenazas` | Amenazas priorizadas con su control y su responsable |
| `matriz regulatoria` | Actividad, obligación, autoridad, fuente y fecha |
| `evidencia` | Prueba ejecutable de que el sistema hace lo que se afirma |
| `límite declarado` | Lo que el trabajo no cubre, dicho antes de que lo pregunten |
| `defensa` | Exposición ante un panel que decide, no que aprende |
| `criterio de aceptación` | Condición verificable, no opinable |

## 🧠 Modelo mental

```text
UN EXPEDIENTE RESPONDE TRES PREGUNTAS, EN ESTE ORDEN

  1. ¿QUÉ HACES?        actividad, figura, perímetro
  2. ¿CÓMO LO HACES?    arquitectura, controles, pruebas
  3. ¿QUÉ PASA SI FALLA? riesgos, incidentes, salida, resolución

LA MAYORÍA DE LOS PROYECTOS RESPONDE BIEN LA 2
Y SE HUNDE EN LA 1 Y EN LA 3

  la 1 porque nadie descompuso el producto en actividades
  la 3 porque «no va a fallar» no es una respuesta
```

## 📖 Desarrollo

### 1. Las doce piezas del expediente

| # | Pieza | Qué demuestra |
|---:|---|---|
| 1 | Producto y usuario | Que resuelve un problema real |
| 2 | Dato mínimo | Que se pensó antes de mirar la API |
| 3 | Modelo de alcances | Que hay una finalidad por alcance |
| 4 | Descomposición en actividades | Que se conoce el perímetro |
| 5 | Arquitectura y flujos | Que el sistema es comprensible |
| 6 | Contrato OpenAPI | Que un tercero puede integrarse |
| 7 | Modelo de amenazas | Que se pensó en el atacante |
| 8 | Matriz regulatoria | Que cada obligación tiene fuente y fecha |
| 9 | Pruebas, incluidas las negativas | Que los controles funcionan |
| 10 | Evidencia de ejecución | Que no es solo un documento |
| 11 | Registro de decisiones | Que hubo criterio, no inercia |
| 12 | Límites declarados | Que se sabe qué no se cubrió |

### 2. Priorizar el modelo de amenazas

```text
EL ERROR: ordenar por «lo más sofisticado»
LA REGLA: ordenar por impacto × probabilidad

  IMPACTO       1 molestia · 3 pérdida de datos ·
                5 pérdida patrimonial o suplantación
  PROBABILIDAD  1 requiere un atacante muy capaz ·
                3 requiere una condición ·
                5 ocurre por un error de configuración

  PRIORIDAD = impacto × probabilidad

CONSECUENCIA HABITUAL DEL EJERCICIO
  «token registrado en el log» (5 × 5 = 25)
  queda por encima de
  «ataque criptográfico al algoritmo de firma» (5 × 1 = 5)

  y esa ordenación es correcta
```

### 3. El registro de decisiones

```text
UNA ENTRADA POR DECISIÓN, CON CUATRO CAMPOS

  DECISIÓN        paginación por cursor
  ALTERNATIVA     paginación por desplazamiento
  MOTIVO          con inserción concurrente, offset repite
                  y omite filas; medido en el laboratorio 3
  CONSECUENCIA    el cursor es opaco: no podemos exponer
                  su formato ni permitir saltos arbitrarios

EL CUARTO CAMPO ES EL QUE FALTA SIEMPRE
  toda decisión cierra puertas. Escribir cuáles
  evita que dentro de un año alguien pida
  «saltar a la página 40» y nadie recuerde por qué no se puede.
```

### 4. Declarar límites fortalece, no debilita

```text
UN EXPEDIENTE SIN LÍMITES SE LEE COMO COBERTURA COMPLETA

  y el panel encontrará el hueco.
  Si lo encuentra él, el trabajo pierde credibilidad entera.
  Si lo declaraste tú, pierde solo ese punto.

LÍMITES TÍPICOS Y LEGÍTIMOS DE ESTE PROYECTO
  · entorno simulado: no hay TLS mutuo real ni
    certificados de una autoridad del esquema
  · datos sintéticos: no se probaron distribuciones reales
  · una sola moneda: la multidivisa es de la Parte 18
  · no se ensayó carga sostenida, solo ráfaga
  · la matriz regulatoria refleja la consulta de una fecha
    concreta y no sustituye asesoría legal
```

### 5. La defensa

```text
DIEZ MINUTOS. TRES BLOQUES.

  0-3   qué hace el producto, para quién,
        y qué actividad regulada realiza
  3-7   una demostración en vivo:
        autorizar → leer → pagar → revocar → fallar
  7-10  riesgos principales, límites y qué harías
        con el doble de tiempo

LAS PREGUNTAS QUE SIEMPRE LLEGAN
  1. ¿qué dato pediste que no necesitabas?
  2. enséñame el segundo posterior a una revocación
  3. si tu proveedor de identidad cae una hora, ¿qué ve el cliente?
  4. ¿de dónde sacaste esa norma y cuándo la verificaste?
  5. ¿qué parte de esto no está probado?

  LA 5 ES LA QUE DISTINGUE UN BUEN PROYECTO:
  quien la responde con precisión ya la había respondido antes
```

## 🧮 Ejemplo guiado

**Situación.** Actúas como revisor de un expediente entregado. Estos son los
extractos relevantes.

```text
EXTRACTO 1 · alcances solicitados
  cuentas:lista, cuentas:saldos, cuentas:movimientos,
  creditos:posicion, creditos:mora, inversiones:posicion

EXTRACTO 2 · producto
  «panel de posición consolidada con alerta de gastos
   inusuales»

EXTRACTO 3 · modelo de amenazas (3 primeras)
  1. ataque de canal lateral sobre la implementación de AES
  2. colisión en el algoritmo de resumen del cursor
  3. inyección en el parámetro de búsqueda

EXTRACTO 4 · matriz regulatoria
  «Actividad: agregación de información. Obligación:
   inscripción. Autoridad: CMF.»

EXTRACTO 5 · pruebas
  38 pruebas, 38 en verde, cobertura 91 %

EXTRACTO 6 · límites
  (sección ausente)
```

**Paso 1 — evalúa el extracto 1 contra el 2.**

```text
APLICA LA REGLA DEL RECHAZO A CADA ALCANCE

  cuentas:lista        sin él no hay panel          → necesario
  cuentas:saldos       es el panel                  → necesario
  cuentas:movimientos  la alerta los necesita       → necesario
  creditos:posicion    aparece en la consolidada    → necesario
  creditos:mora        ¿qué función lo usa?         → NINGUNA
  inversiones:posicion aparece en la consolidada    → necesario

HALLAZGO 1 · alcance sin finalidad: creditos:mora
  gravedad: alta
  es el alcance más sensible del conjunto (clase 9)
  y el único que no sostiene ninguna función
```

**Paso 2 — evalúa el modelo de amenazas.**

```text
PUNTÚA LAS TRES

  1. canal lateral sobre AES     impacto 5 × probabilidad 1 =  5
  2. colisión en el resumen      impacto 3 × probabilidad 1 =  3
  3. inyección en búsqueda       impacto 4 × probabilidad 4 = 16

ESTÁN ORDENADAS AL REVÉS

Y FALTAN LAS DE PRIORIDAD MÁS ALTA
  token en el registro           5 × 5 = 25
  redirect_uri por prefijo       5 × 4 = 20
  revocación sin invalidar token 4 × 4 = 16
  ausencia de idempotencia       4 × 5 = 20

HALLAZGO 2 · el modelo prioriza por sofisticación
  y omite cuatro amenazas de prioridad superior a todas
  las listadas
```

**Paso 3 — evalúa la matriz regulatoria.**

```text
LA FILA TIENE 3 DE 6 CAMPOS

  presentes:  actividad, obligación, autoridad
  ausentes:   fuente oficial, fecha de verificación, limitaciones

HALLAZGO 3 · matriz sin fuente ni fecha
  gravedad: alta
  sin fecha, la afirmación no es verificable ni caduca;
  dentro de un año nadie sabrá si sigue siendo cierta

Y ADEMÁS
  «agregación de información» no es una actividad
  del catálogo: es una descripción de producto.
  Falta la descomposición del extracto 2:
  la alerta de gastos inusuales, ¿es información
  o es una recomendación? (clase 3)
```

**Paso 4 — evalúa las pruebas.**

```text
38 PRUEBAS, 38 EN VERDE, 91 % DE COBERTURA

  LA PREGUNTA CORRECTA NO ES «¿CUÁNTAS?»
  ES «¿CUÁNTAS SON NEGATIVAS?»

  revisión del listado:
    positivas (camino feliz):  34
    negativas:                  4

HALLAZGO 4 · 4 pruebas negativas para 7 controles críticos
  faltan, como mínimo:
    · acceso con consentimiento revocado
    · reintento con la misma clave de idempotencia
    · redirect_uri con sufijo
    · cuenta ajena y cuenta inexistente indistinguibles
```

**Paso 5 — evalúa la ausencia del extracto 6.**

```text
HALLAZGO 5 · sin sección de límites
  gravedad: media en sí misma, alta por lo que implica

  el expediente afirma implícitamente que cubre todo.
  Un revisor que encuentra el primer hueco deja de confiar
  en el resto, incluido lo que sí está bien hecho.
```

**Paso 6 — puntúa con la rúbrica.**

```text
Diseño de consentimiento         20 %  →  11/20  (alcance sin finalidad)
Seguridad de la autorización     20 %  →   9/20  (modelo mal priorizado,
                                                  4 pruebas negativas)
Calidad del contrato de API      15 %  →  12/15  (correcto)
Riesgo y regulación              20 %  →   7/20  (matriz incompleta,
                                                  actividad no descompuesta)
Evidencia y reproducibilidad     15 %  →  11/15  (pruebas ejecutan)
Defensa                          10 %  →   —     (pendiente)

TOTAL SOBRE 90 EVALUADO: 50 → 55,6 %
NO ALCANZA EL 70 % DE APROBACIÓN
```

**Paso 7 — escribe la devolución.**

```text
DEVOLUCIÓN AL AUTOR

  LO QUE ESTÁ BIEN
    · el contrato de API es sólido y versionado
    · las pruebas ejecutan y son reproducibles
    · la arquitectura es comprensible

  LO QUE HAY QUE CORREGIR, EN ORDEN
    1. eliminar creditos:mora o justificar su función
    2. repriorizar el modelo de amenazas por impacto ×
       probabilidad e incorporar las cuatro ausentes
    3. completar la matriz con fuente, fecha y limitaciones,
       y descomponer el producto en actividades
    4. añadir al menos siete pruebas negativas
    5. escribir la sección de límites

  ESTIMACIÓN: 3 y 5 son de un día; 1, 2 y 4 son de tres.

  Y UNA OBSERVACIÓN DE CRITERIO
    los tres hallazgos más graves no son técnicos.
    El autor construyó bien y decidió poco. Un expediente
    se evalúa sobre todo por sus decisiones.
```

**Interpreta:** el proyecto tenía buen software y mal expediente. La diferencia
entre ambos es exactamente lo que esta parte enseña: **la ingeniería sostiene la
decisión, pero no la sustituye**.

## 🧭 Perspectivas

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un producto que le pide seis permisos | Si acepta |
| Autor | Un sistema que funciona | Si documenta las decisiones |
| Revisor | Cinco hallazgos | Qué puntúa |
| Banco | Un tercero que quiere conectarse | Si lo habilita |
| Supervisor | Un expediente de inscripción | Si lo admite |
| Auditor | Pruebas mayoritariamente positivas | Qué observa |
| Inversionista | Riesgo de ejecución | Si financia |

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Me pide ver mi mora» | Alcance sin finalidad | 17, clases 5 y 14 |
| «¿Están autorizados?» | Inscripción y perímetro | 17, clase 3 |
| «¿Qué pasa si se cae?» | Degradación y salida | 17, clase 13 |
| «¿Quién responde?» | Matriz de responsabilidad | 17, clase 11 |

## ⚖️ Riesgos y controles

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Alcance sin finalidad | Se pidió por si acaso | Regla del rechazo aplicada por escrito |
| Amenazas mal priorizadas | Se ordenó por sofisticación | Impacto × probabilidad |
| Matriz sin fecha | Se citó de memoria | Fuente oficial y fecha obligatorias |
| Pruebas solo positivas | Se probó lo que funciona | Mínimo de pruebas negativas por control |
| Ausencia de límites | Se temió mostrar debilidad | Sección obligatoria |
| Decisiones sin registro | Se construyó por inercia | Cuatro campos por decisión |

## 🧪 Práctica

En el [proyecto de la parte](../project/README.md):

1. Construye las doce piezas del expediente.
2. Prioriza tu modelo de amenazas y compáralo con la lista de la clase.
3. Escribe el registro de decisiones con los cuatro campos.
4. Revisa el expediente de otra persona con la rúbrica y escríbele la devolución.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Buen software, mal expediente | Se construyó antes de decidir | Empieza por las piezas 1 a 4 |
| Amenazas exóticas primero | Se buscó demostrar nivel técnico | Ordena por impacto × probabilidad |
| Todas las pruebas en verde | Solo se probó el camino feliz | Cuenta las negativas |
| Sin sección de límites | Se creyó que resta | Declarar fortalece |
| Decisión sin alternativa | No se registró | Cuatro campos por decisión |
| Norma sin fecha | Se citó de segunda mano | Fuente oficial y fecha |

## ❓ Preguntas de comprobación

1. ¿Cuáles son las doce piezas del expediente y cuáles dos suelen faltar?
2. ¿Por qué «token en el registro» debe ir por encima de «ataque criptográfico»?
3. ¿Cuál es el cuarto campo del registro de decisiones y por qué es el que falta?
4. ¿Por qué declarar límites fortalece un expediente?
5. ¿Qué distingue a quien responde bien la pregunta «¿qué parte no está probada?»?

## 📥 Entregable

Guarda en `portfolio/parte-17/clase-14/`:

- el expediente completo con sus doce piezas;
- el modelo de amenazas priorizado por impacto × probabilidad;
- el registro de decisiones con los cuatro campos;
- la revisión del expediente de otra persona, con su puntuación y su devolución.

## 🔗 Referencias cruzadas

- **Viene de:** las trece clases anteriores de esta parte.
- **Continúa en:** Parte 18 (el mismo producto, ahora transfronterizo).
- **Se aplica en:** Parte 22, clase 18 (expediente de autorización); Parte 23,
  clase 18 (defensa ante directorio y supervisor).

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

- Comisión para el Mercado Financiero. *Requisitos de inscripción y autorización de prestadores de servicios financieros de la Ley N.º 21.521*. CMF. <https://www.cmfchile.cl/>
- OWASP Foundation. *Threat Modeling Process* y *Application Security Verification Standard*. OWASP. <https://owasp.org/www-community/Threat_Modeling>
- NIST (2018). *Framework for Improving Critical Infrastructure Cybersecurity*. NIST. <https://www.nist.gov/cyberframework>
- Basel Committee on Banking Supervision (2021). *Principles for operational resilience*. BIS. <https://www.bis.org/bcbs/publ/d516.htm>
- OpenID Foundation. *FAPI conformance suite: criterios de certificación*. <https://openid.net/certification/>
- Verificación local: comprueba qué antecedentes exige el supervisor de tu jurisdicción para la inscripción o autorización, y en qué formato. **Fecha de verificación de esta clase: 2026-08-06.** Este material no constituye asesoría legal.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 13 · Disponibilidad, SLA, observabilidad e incidentes](13-disponibilidad-sla-y-observabilidad.md) | [Parte 17](../README.md) · [Programa](../../../SYLLABUS.md) | [Proyecto de la parte →](../project/README.md) |
<!-- gen:footer:end -->
