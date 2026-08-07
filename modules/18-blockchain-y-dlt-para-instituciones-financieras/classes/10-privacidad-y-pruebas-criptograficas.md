---
part: 19
class: 10
title: "Privacidad y pruebas criptográficas"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global, union-europea]
regulatory_topics: [dlt, proteccion-de-datos, privacidad]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [CPMI, NIST]
requires_legal_review: true
---

<!-- gen:header:start -->
# Clase 10 · Privacidad y pruebas criptográficas

> [← 09 · Oráculos](09-oraculos.md) · [Índice de la parte](../README.md) · [11 · Interoperabilidad y puentes →](11-interoperabilidad-y-puentes.md)

**Parte 19 — Blockchain y DLT para instituciones financieras** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Resolver la contradicción que aparece en cuanto un banco pone un pie en un
registro compartido: **verificable por todos** y **confidencial para cada uno**
parecen incompatibles, y la criptografía ofrece una salida parcial que hay que
saber medir.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** confidencialidad, anonimato y no vinculabilidad.
2. **Comparar** las cuatro técnicas de privacidad por lo que ocultan y lo que
   cuestan.
3. **Explicar** qué demuestra una prueba de conocimiento cero y qué no.
4. **Resolver** la tensión entre inmutabilidad y derecho de supresión.
5. **Diseñar** el reparto entre lo que va dentro del registro y lo que queda
   fuera.

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
| `confidencialidad` | El contenido no es legible por quien no debe |
| `anonimato` | No se sabe quién participó |
| `no vinculabilidad` | Dos operaciones del mismo actor no se pueden asociar |
| `canal privado` | Subconjunto de participantes que comparte datos |
| `compromiso` | Valor que fija un dato sin revelarlo |
| `prueba de conocimiento cero` | Demuestra una afirmación sin revelar por qué es cierta |
| `prueba de rango` | Demuestra que un valor está entre dos límites |
| `análisis de la cadena` | Deducción de relaciones a partir de los metadatos |

## 🧠 Modelo mental

```text
TRES PROPIEDADES QUE SE CONFUNDEN

  CONFIDENCIALIDAD  no se ve QUÉ
  ANONIMATO         no se ve QUIÉN
  NO VINCULABILIDAD no se ve que sea EL MISMO

  UN SISTEMA PUEDE TENER UNA Y NO LAS OTRAS

EL ERROR CLÁSICO EN FINANZAS
  cifrar los importes y dejar las direcciones a la vista
  → confidencialidad sin no vinculabilidad
  → el análisis de la cadena reconstruye quién opera
    con quién, cuándo y con qué frecuencia

  para un banco, saber que su cliente A paga a B
  cada mes ya es información competitiva,
  aunque el importe esté cifrado
```

## 📖 Desarrollo

### 1. Las cuatro técnicas

| Técnica | Qué oculta | Coste | Quién verifica |
|---|---|---|---|
| Datos fuera del registro | Todo el contenido | Bajo | Solo quien tiene el dato |
| Canales privados | Contenido y existencia, a los ajenos | Medio | Los del canal |
| Compromisos | El valor, no la existencia | Bajo | Cualquiera, la consistencia |
| Pruebas de conocimiento cero | El valor, demostrando propiedades | Alto | Cualquiera, la propiedad |

```text
LA PRIMERA ES LA MÁS USADA Y LA MENOS RECONOCIDA
  «lo ponemos fuera y dejamos el resumen dentro»

  ventaja: resuelve confidencialidad y supresión
  coste: se pierde la verificabilidad del contenido;
         el registro solo prueba que el dato no cambió,
         no qué dice
```

### 2. Qué demuestra una prueba de conocimiento cero

```text
DEMUESTRA
  que una afirmación es cierta, sin revelar los datos
  que la hacen cierta

  «este importe está entre 0 y 10⁶»
  «este saldo es suficiente para este pago»
  «esta persona está en la lista de autorizados»

NO DEMUESTRA
  · que el dato de partida sea correcto
    → si el saldo de entrada es falso, la prueba es
      válida sobre un dato falso
  · que quien la genera sea quien dice
  · nada sobre lo que no se le pidió demostrar

Y TIENE UN COSTE QUE HAY QUE MEDIR
  generación: de milisegundos a minutos según el circuito
  verificación: normalmente barata
  tamaño de la prueba: de cientos de bytes a kilobytes
  → en un registro donde todos guardan todo,
    el tamaño importa
```

### 3. La tensión con el derecho de supresión

```text
UN REGISTRO INMUTABLE Y UN DERECHO DE SUPRESIÓN
SON INCOMPATIBLES SI EL DATO PERSONAL ESTÁ DENTRO

  SOLUCIONES POR ORDEN DE PREFERENCIA

  1. NO METERLO
     dentro va un compromiso o un resumen;
     el dato vive fuera y se borra allí
     → la mejor, y la que casi nadie elige al empezar

  2. CIFRAR Y DESTRUIR LA CLAVE
     el dato cifrado permanece; sin clave es ilegible
     → discutible: hay quien sostiene que el dato
       cifrado sigue siendo dato personal mientras
       exista la posibilidad teórica de descifrarlo

  3. REGISTRO CON CAPACIDAD DE PODA
     el protocolo admite eliminar contenido antiguo
     conservando su resumen
     → rompe la reconstrucción completa del estado

LA DECISIÓN SE TOMA ANTES DE ESCRIBIR LA PRIMERA LÍNEA.
Después es una migración.
```

### 4. Análisis de la cadena: lo que revelan los metadatos

```text
AUNQUE EL CONTENIDO ESTÉ CIFRADO, SON VISIBLES

  · quién escribe y con qué frecuencia
  · el tamaño de cada operación
  · el momento exacto
  · el patrón: fin de mes, día de nóminas
  · la topología: quién opera con quién

CON ESO SE RECONSTRUYE
  · volumen de negocio de un participante
  · relaciones comerciales
  · momentos de tensión de liquidez

MITIGACIONES
  · relleno para uniformar tamaños
  · agrupación de operaciones en lotes
  · retardos aleatorios
  · direcciones de un solo uso

  todas cuestan eficiencia, y ninguna es completa
```

### 5. El reparto: qué va dentro

```text
CRITERIO PRÁCTICO

  DENTRO
    · compromisos y resúmenes
    · importes, si el diseño lo permite y hace falta
      verificarlos
    · transiciones de estado
    · pruebas de propiedades

  FUERA
    · identidad de las personas
    · documentación contractual
    · cualquier dato sujeto a derecho de supresión
    · información comercialmente sensible en claro

Y UNA REGLA DE ORO
  todo lo que entra, entra para siempre.
  La pregunta antes de cada campo es
  «¿me molestaría que esto siguiera ahí dentro de 30 años?»
```

## 🧮 Ejemplo guiado

**Situación.** El consorcio de bancos quiere registrar operaciones de préstamo
sindicado. Debe decidir qué entra en el registro.

```text
LO QUE UNA OPERACIÓN CONTIENE
  identidad del prestatario
  importe del préstamo
  reparto entre los bancos participantes
  tipo de interés y comisiones
  garantías constituidas
  calendario de pagos
  documentación contractual

PARTICIPANTES
  8 bancos, lectura restringida a los del sindicato
  supervisor con acceso de lectura total
```

**Paso 1 — clasifica cada campo por su sensibilidad.**

```text
identidad del prestatario   dato personal o societario protegido
importe                     comercialmente sensible
reparto entre bancos        MUY sensible entre competidores
tipo y comisiones           MUY sensible: revela política de precios
garantías                   sensible; con interés de terceros
calendario                  derivable del resto
documentación               contiene datos personales
```

**Paso 2 — comprueba si los canales privados bastan.**

```text
CANAL PRIVADO POR SINDICATO
  solo los bancos de ese préstamo ven sus datos

  ¿RESUELVE EL PROBLEMA DEL REPARTO Y DEL PRECIO?
    entre bancos de OTRO sindicato, sí
    entre los del MISMO sindicato, no: se ven entre ellos

  ¿ES UN PROBLEMA?
    en un sindicato, cada participante conoce el reparto
    por el propio contrato → no añade exposición

  → los canales privados resuelven la mayor parte
```

**Paso 3 — detente en el supervisor.**

```text
EL SUPERVISOR TIENE LECTURA TOTAL

  eso significa que TODOS los datos de TODOS los
  sindicatos están en un ámbito donde el supervisor
  los ve

  ¿ES ACEPTABLE? Depende de la base jurídica de ese acceso.

  Y HAY UN PROBLEMA TÉCNICO ADICIONAL
    si el supervisor debe poder leerlo todo,
    los datos no pueden estar cifrados solo para
    el sindicato: hace falta que también lo estén
    para él

    → cada dato se cifra para n+1 destinatarios
    → si el supervisor rota su clave, hay que
      recifrar el histórico, o conservar la clave
      antigua para siempre

HALLAZGO
  el acceso total del supervisor convierte su gestión
  de claves en un punto crítico del sistema entero
```

**Paso 4 — busca una alternativa al acceso total.**

```text
OPCIÓN · ACCESO BAJO DEMANDA CON PRUEBA

  el registro guarda compromisos de cada campo
  el supervisor puede:
    · verificar propiedades agregadas sin ver el detalle
      («ningún banco supera el límite de concentración»)
    · exigir la revelación de una operación concreta,
      y comprobar contra el compromiso que lo revelado
      es lo registrado

  VENTAJAS
    · no hay una copia legible de todo
    · el supervisor obtiene lo que necesita
    · queda registro de cada acceso

  COSTE
    · circuitos de prueba para cada propiedad agregada
    · más complejidad
```

**Paso 5 — cuantifica el caso de la concentración.**

```text
PROPIEDAD A DEMOSTRAR
  «la exposición del banco X a un mismo prestatario
   no supera el 25 % de sus fondos propios»

  SIN PRUEBAS
    el supervisor lee todas las operaciones del banco X
    y suma
    → ve también el precio y el reparto

  CON PRUEBA DE RANGO
    el banco X publica un compromiso de su exposición
    total por prestatario y una prueba de que está
    bajo el límite
    → el supervisor verifica sin ver el detalle

  COSTE ESTIMADO
    diseño del circuito                4 200 000
    generación por banco y mes            180 000 anuales
    verificación                        despreciable

  BENEFICIO
    ningún dato de precio ni de reparto sale del sindicato
```

**Paso 6 — resuelve la documentación y la supresión.**

```text
LA DOCUMENTACIÓN CONTRACTUAL NO ENTRA. NUNCA.

  dentro: el resumen del documento y la fecha
  fuera: el documento, en el gestor documental
         de cada banco, con su política de retención

  ASÍ
    · el registro prueba que el documento no cambió
    · el derecho de supresión se ejerce sobre el documento
    · el resumen que queda dentro no es dato personal
      si el documento ya no existe

  ESTA ES LA SOLUCIÓN 1 DEL APARTADO 3,
  Y ES LA QUE HAY QUE ELEGIR AL EMPEZAR
```

**Paso 7 — escribe el reparto final.**

```text
DENTRO DEL REGISTRO
  · identificador seudónimo de la operación
  · compromisos de importe, reparto, tipo y comisiones
  · resúmenes de los documentos y sus fechas
  · transiciones de estado (constituido, desembolsado,
    amortizado, vencido)
  · pruebas de propiedades agregadas

DENTRO DEL CANAL PRIVADO DEL SINDICATO
  · importe, reparto, tipo y comisiones en claro

FUERA DEL REGISTRO
  · identidad del prestatario
  · documentación contractual
  · datos personales de cualquier tipo

ACCESO DEL SUPERVISOR
  · verificación de propiedades agregadas por defecto
  · revelación bajo demanda de operaciones concretas,
    con registro del acceso

LO QUE SE ACEPTA COMO RESIDUAL
  el análisis de metadatos permite estimar el volumen
  de actividad de cada banco. Se mitiga con lotes
  y no se elimina.
```

**Interpreta:** la pregunta empezó siendo «cómo ciframos» y acabó siendo **qué no
metemos**. La técnica más eficaz de privacidad en un registro inmutable sigue
siendo la más simple: dejar fuera lo que no tiene por qué entrar.

## 🧭 Perspectivas

| Actor | Qué ve | Qué decide |
|---|---|---|
| Prestatario | Su operación en un registro compartido | Si consiente |
| Banco del sindicato | El precio de sus competidores | Si participa |
| Banco ajeno al sindicato | Metadatos de actividad | Qué deduce |
| Supervisor | Acceso total o bajo demanda | Qué exige |
| Protección de datos | Registro inmutable | Qué prohíbe meter |
| Tecnología | Cifrado para n+1 destinatarios | Cómo gestiona claves |
| Auditor | Compromisos y revelaciones | Qué evidencia acepta |

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Quiero que borren mis datos» | Solo se puede si están fuera | 19, clase 10 |
| «¿Ven mis datos otros bancos?» | Canales privados por sindicato | 19, clase 10 |
| «Está cifrado, es privado» | Los metadatos siguen visibles | 19, clase 10 |

## ⚖️ Riesgos y controles

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Dato personal dentro | Inmutable y no suprimible | Fuera desde el diseño |
| Metadatos reveladores | Se reconstruye la actividad | Lotes, relleno, retardos |
| Clave del supervisor | Punto crítico del sistema | Acceso bajo demanda con prueba |
| Prueba sobre dato falso | La prueba es válida, el dato no | Verificar el origen del dato |
| Cifrado como única medida | Confidencialidad sin no vinculabilidad | Combinar técnicas |
| Decidir el reparto tarde | Migración en vez de diseño | Decidir antes de la primera línea |

## 🧪 Práctica

En [`labs/lab-03.md`](../labs/lab-03.md) y el [proyecto](../project/README.md):

1. Clasifica diez campos por sensibilidad y decide dentro o fuera.
2. Implementa compromisos y demuestra la consistencia sin revelar el valor.
3. Simula un análisis de metadatos sobre tu registro y di qué deduces.
4. Escribe cómo ejercería un cliente su derecho de supresión en tu diseño.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Cifrar y creerlo resuelto | Se confundieron las tres propiedades | Los metadatos siguen |
| Meter el documento | Se quiso «todo en la cadena» | Resumen dentro, documento fuera |
| Acceso total del supervisor | Se copió el modelo de base de datos | Prueba de propiedades agregadas |
| Confiar en la prueba sin mirar el dato | Se verificó la matemática | La prueba no valida el origen |
| Decidir la privacidad al final | Se empezó por la funcionalidad | Es una decisión de diseño inicial |
| Ignorar el coste de las pruebas | Se leyó que «son baratas de verificar» | Generar y almacenar cuesta |

## ❓ Preguntas de comprobación

1. ¿Qué diferencia hay entre confidencialidad, anonimato y no vinculabilidad?
2. ¿Qué demuestra y qué no demuestra una prueba de conocimiento cero?
3. ¿Cuál es la mejor solución a la tensión con el derecho de supresión, y por
   qué casi nadie la elige?
4. ¿Qué se puede deducir de los metadatos aunque el contenido esté cifrado?
5. En el ejemplo guiado, ¿por qué el acceso total del supervisor era un problema
   técnico además de jurídico?

## 📥 Entregable

Guarda en `portfolio/parte-19/clase-10/`:

- diez campos clasificados, con la decisión de dentro o fuera;
- una implementación de compromisos con su verificación;
- el análisis de metadatos de tu propio diseño;
- el procedimiento de supresión, explicado paso a paso.

## 🔗 Referencias cruzadas

- **Viene de:** clases 2, 4 y 7; Parte 17, clase 12 (privacidad).
- **Continúa en:** clase 12 (escalabilidad, por el coste de las pruebas).
- **Se aplica en:** Parte 21, clase 11; Parte 22, clase 12; Parte 23, clase 16.

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

- Parlamento Europeo y Consejo. *Reglamento (UE) 2016/679 (RGPD)*, artículo 17 sobre supresión. <https://eur-lex.europa.eu/eli/reg/2016/679/oj>
- NIST (2020). *NIST Privacy Framework 1.0*. NIST. <https://www.nist.gov/privacy-framework>
- Committee on Payments and Market Infrastructures (2017). *Distributed ledger technology in payment, clearing and settlement*. BIS. <https://www.bis.org/cpmi/publ/d157.htm>
- European Union Agency for Cybersecurity (2021). *Data Protection Engineering*. ENISA. <https://www.enisa.europa.eu/publications/data-protection-engineering>
- NIST (2018). *NISTIR 8202: Blockchain Technology Overview*. NIST. <https://csrc.nist.gov/pubs/ir/8202/final>
- Verificación local: comprueba qué autoridad de protección de datos es competente, qué criterio ha publicado sobre registros inmutables y si considera dato personal un valor cifrado. **Fecha de verificación de esta clase: 2026-08-06.** Esta clase no constituye asesoría legal.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 09 · Oráculos](09-oraculos.md) | [Parte 19](../README.md) · [Programa](../../../SYLLABUS.md) | [11 · Interoperabilidad y puentes →](11-interoperabilidad-y-puentes.md) |
<!-- gen:footer:end -->
