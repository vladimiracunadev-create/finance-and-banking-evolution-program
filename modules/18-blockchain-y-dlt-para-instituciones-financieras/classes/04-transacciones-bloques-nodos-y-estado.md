---
part: 19
class: 4
title: "Transacciones, bloques, nodos y estado"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global]
regulatory_topics: [dlt, infraestructura]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [NIST, CPMI]
requires_legal_review: false
---

<!-- gen:header:start -->
# Clase 04 · Transacciones, bloques, nodos y estado

> [← 03 · Claves, direcciones y gestión criptográfica](03-claves-direcciones-y-gestion-criptografica.md) · [Índice de la parte](../README.md) · [05 · Mecanismos de consenso →](05-mecanismos-de-consenso.md)

**Parte 19 — Blockchain y DLT para instituciones financieras** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Abrir la caja: qué es exactamente una transacción, cómo se agrupa en bloques,
qué guarda cada tipo de nodo y qué significa «el estado». Sin esta anatomía, las
clases de consenso y de finalidad son palabras.

## 📚 Objetivos

Al finalizar podrás:

1. **Describir** el ciclo de una transacción desde que se firma hasta que forma
   parte del estado.
2. **Distinguir** los dos modelos de estado y decir qué gana cada uno.
3. **Comparar** los tipos de nodo por lo que pueden verificar por sí mismos.
4. **Explicar** qué es la mempool y qué riesgos introduce.
5. **Calcular** el crecimiento del registro y su efecto sobre quién puede
   participar.

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
| `transacción` | Instrucción firmada que cambia el estado |
| `mempool` | Conjunto de transacciones válidas aún no incluidas |
| `bloque` | Grupo de transacciones ordenadas, encadenado al anterior |
| `estado` | Situación resultante de aplicar todas las transacciones |
| `nodo completo` | Verifica todo por sí mismo; guarda lo necesario |
| `nodo ligero` | Verifica pertenencia; confía en otros para el resto |
| `nodo archivo` | Guarda todos los estados históricos |
| `reorganización` | Sustitución de bloques ya difundidos por otra cadena |

## 🧠 Modelo mental

```text
EL ESTADO NO SE GUARDA: SE DEDUCE

  bloque 0 (génesis)
     + todas las transacciones del bloque 1
     + todas las del bloque 2
     ...
     = ESTADO ACTUAL

  cualquiera que tenga la cadena completa
  puede recalcular el estado sin confiar en nadie

  ESA ES LA PROPIEDAD QUE SE PAGA CARA:
  la verificación independiente exige que cada nodo
  reejecute toda la historia
```

## 📖 Desarrollo

### 1. Ciclo de una transacción

```text
1. CONSTRUCCIÓN  se arma la instrucción: origen, destino,
                 importe, comisión, número de orden
2. FIRMA         con la clave privada del origen
3. DIFUSIÓN      se envía a un nodo, que la propaga
4. VALIDACIÓN    cada nodo comprueba firma, saldo, formato
                 y número de orden
5. MEMPOOL       queda pendiente de inclusión
6. INCLUSIÓN     un productor de bloques la selecciona
7. PROPAGACIÓN   el bloque se difunde
8. CONFIRMACIÓN  bloques posteriores la consolidan

ENTRE EL 5 Y EL 6 ESTÁ TODO EL PROBLEMA
  la transacción es pública, válida y no ejecutada.
  Cualquiera puede verla y actuar antes.
```

### 2. Los dos modelos de estado

| | Modelo de saldos | Modelo de salidas no gastadas |
|---|---|---|
| Qué guarda | Un saldo por cuenta | Un conjunto de «monedas» sin gastar |
| Transacción | Resta de una cuenta, suma a otra | Consume salidas y crea otras |
| Paralelización | Difícil: dos operaciones tocan la misma cuenta | Fácil: salidas distintas son independientes |
| Privacidad | Menor: la cuenta acumula historia | Mayor: se usan salidas distintas |
| Contratos complejos | Natural | Más difícil |
| Repetición | Se evita con número de orden | Imposible: la salida ya se gastó |

```text
LA FILA QUE MÁS IMPORTA EN FINANZAS
  «repetición»

  con saldos, hace falta un contador por cuenta;
  si dos transacciones llevan el mismo número,
  una se rechaza

  sin ese contador, la misma transacción firmada
  se puede reenviar y ejecutar dos veces
  → es la idempotencia de la Parte 17, clase 8,
    resuelta en la capa del protocolo
```

### 3. Anatomía de un bloque

```text
CABECERA
  resumen del bloque anterior      ← el encadenamiento
  raíz de Merkle de las transacciones
  marca de tiempo
  datos del consenso (dificultad, firma, ronda...)

CUERPO
  lista ordenada de transacciones

POR QUÉ EL ORDEN IMPORTA
  dos transacciones sobre la misma cuenta dan
  resultados distintos según el orden

  quien decide el orden tiene poder económico
  → clase 12 y Parte 21, clase 14
```

### 4. Tipos de nodo y qué puede verificar cada uno

```text
NODO COMPLETO
  descarga y verifica cada bloque y cada transacción
  mantiene el estado actual
  NO confía en nadie
  coste: almacenamiento, ancho de banda, cómputo

NODO ARCHIVO
  además, guarda TODOS los estados históricos
  permite responder «¿cuál era el saldo el día X?»
  coste: mucho mayor

NODO LIGERO
  descarga solo cabeceras
  verifica pertenencia con pruebas de Merkle
  CONFÍA en que la cadena de cabeceras es la correcta
  coste: mínimo

LA PREGUNTA INSTITUCIONAL
  ¿un banco puede operar con nodo ligero?
  puede, y entonces DEPENDE de terceros para saber
  cuál es la cadena válida
  → eso es una dependencia que hay que declarar
    en el mapa de riesgo
```

### 5. Crecimiento y centralización

```text
EL REGISTRO SOLO CRECE

  si cada bloque ocupa B y se produce cada T segundos:
  crecimiento anual = B × (31 536 000 / T)

  CON B = 1,5 MB Y T = 12 s
    1,5 × 2 628 000 = 3 942 000 MB ≈ 3,9 TB al año

CONSECUENCIA
  cuanto más crece, menos participantes pueden
  ejecutar un nodo completo
  → menos verificadores independientes
  → más dependencia de unos pocos

ES EL COMPROMISO CENTRAL DE LA CLASE 12
  más capacidad por bloque = más transacciones
  = menos nodos completos = más centralización
```

## 🧮 Ejemplo guiado

**Situación.** Un consorcio de cinco bancos dimensiona su red autorizada. Debe
decidir tamaño de bloque, intervalo y tipo de nodo por participante.

```text
REQUISITOS
  operaciones al día                    180 000
  pico por segundo                           40
  tamaño medio de una operación             450 bytes
  retención exigida por normativa       10 años
  consulta histórica («saldo al día X»)  sí, obligatoria

INFRAESTRUCTURA DISPONIBLE POR BANCO
  almacenamiento asignado                   40 TB
  ancho de banda entre nodos             200 Mbps
```

**Paso 1 — dimensiona el bloque.**

```text
PICO DE 40 OPERACIONES POR SEGUNDO

  con intervalo de 2 s:  80 operaciones por bloque
  80 × 450 = 36 000 bytes = 36 KB por bloque
  + cabecera y sobrecarga ≈ 40 KB

  MARGEN
    se dimensiona al doble del pico: 80 KB por bloque
```

**Paso 2 — calcula el crecimiento.**

```text
BLOQUES AL AÑO
  31 536 000 / 2 = 15 768 000

VOLUMEN ANUAL EN EL PEOR CASO (bloques llenos)
  15 768 000 × 80 KB = 1 261 440 000 KB ≈ 1,26 TB

VOLUMEN ANUAL REAL (ocupación media estimada del 30 %)
  ≈ 0,38 TB

A 10 AÑOS
  peor caso: 12,6 TB
  real:       3,8 TB
```

**Paso 3 — detente: falta el mayor consumidor.**

```text
EL CÁLCULO ANTERIOR ES DEL REGISTRO DE TRANSACCIONES.
LA NORMATIVA EXIGE CONSULTA HISTÓRICA DE SALDOS.

  eso obliga a NODOS ARCHIVO, que guardan
  cada estado intermedio

  ESTIMACIÓN
    estado actual: 5 000 000 de cuentas × 200 bytes = 1 GB
    guardar el estado tras cada bloque es inviable:
    15,7 millones de bloques al año × 1 GB = imposible

  LA SOLUCIÓN NO ES MÁS DISCO: ES OTRO DISEÑO
```

**Paso 4 — diseña la consulta histórica sin nodos archivo.**

```text
OPCIÓN A · instantáneas periódicas
  se guarda el estado completo cada N bloques
  y se reconstruye lo intermedio reejecutando

  con N = 43 200 bloques (un día):
    365 instantáneas al año × 1 GB = 365 GB/año
    a 10 años: 3,65 TB
    reconstrucción de un momento cualquiera:
    reejecutar como mucho un día de operaciones

OPCIÓN B · índice externo de eventos
  el registro guarda solo transacciones;
  un índice fuera del registro responde consultas

  más barato, y ROMPE la propiedad:
  el índice hay que auditarlo aparte

DECISIÓN: OPCIÓN A
  3,65 TB de instantáneas + 3,8 TB de cadena = 7,45 TB
  frente a 40 TB disponibles  ✓
```

**Paso 5 — asigna tipo de nodo por participante.**

```text
LOS CINCO BANCOS: NODO COMPLETO CON INSTANTÁNEAS
  cada uno verifica todo por sí mismo
  ninguno depende de otro para saber el estado

  ¿Y EL SUPERVISOR?
    nodo completo de solo lectura
    → puede verificar sin participar en el consenso

  ¿Y UN BANCO PEQUEÑO QUE QUIERA ENTRAR?
    con 40 TB de requisito, no puede
    → o se le ofrece nodo ligero, y depende
    → o el consorcio subvenciona su nodo

EL DISEÑO TÉCNICO ACABA DE DECIDIR QUIÉN PUEDE PARTICIPAR
```

**Paso 6 — comprueba el ancho de banda.**

```text
PROPAGACIÓN DE UN BLOQUE DE 80 KB A 5 NODOS
  80 KB × 8 = 640 kbit por nodo
  a 4 destinos: 2 560 kbit por bloque

  con un bloque cada 2 s: 1 280 kbps = 1,28 Mbps
  frente a 200 Mbps disponibles  ✓

  MARGEN AMPLIO, pero comprobar el caso de resincronización:
  un nodo que estuvo caído un día debe descargar
  43 200 bloques × 80 KB = 3,4 GB
  a 200 Mbps: ≈ 2,3 minutos  ✓
```

**Paso 7 — declara lo que el dimensionamiento no cubre.**

```text
LO QUE FALTA POR DECIDIR Y NO ES TÉCNICO

  · quién produce los bloques y en qué orden (clase 5)
  · qué pasa si el productor censura una operación
  · quién paga la infraestructura del banco pequeño
  · qué ocurre con los datos al cabo de 10 años:
    ¿se pueden borrar? El registro solo crece,
    y la normativa de datos puede exigir supresión
    → es la tensión de la clase 10, y no la resuelve
      el dimensionamiento

EL ÚLTIMO PUNTO ES EL MÁS SERIO
  un registro inmutable y un derecho de supresión
  son incompatibles si el dato personal está dentro.
  La solución es no meterlo: guardar el resumen,
  no el dato.
```

**Interpreta:** el dimensionamiento parecía un ejercicio de disco y reveló dos
decisiones estructurales: **la consulta histórica obligó a rediseñar el
almacenamiento**, y el requisito de recursos acabó determinando quién puede
participar en la red. La técnica fijó la política de acceso sin que nadie la
discutiera.

## 🧭 Perspectivas

| Actor | Qué ve | Qué decide |
|---|---|---|
| Banco grande | 40 TB disponibles | Nodo completo |
| Banco pequeño | Un requisito que no puede cumplir | Si entra o depende |
| Supervisor | Necesidad de verificar | Nodo de solo lectura |
| Tecnología | 7,45 TB a 10 años | Diseño de instantáneas |
| Cumplimiento | Retención de 10 años | Qué se guarda dentro |
| Protección de datos | Registro inmutable | Qué NO puede entrar |
| Auditor | Reconstrucción de un estado pasado | Qué evidencia acepta |

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Quiero mi saldo de hace tres años» | Instantáneas y reejecución | 19, clase 4 |
| «Envié y no se ha procesado» | La transacción está en la mempool | 19, clase 4 |
| «Quiero que borren mis datos» | El registro solo crece | 19, clase 10 |

## ⚖️ Riesgos y controles

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Dato personal en el registro | Inmutable, no suprimible | Guardar resumen, no dato |
| Crecimiento sin límite | Menos nodos completos | Instantáneas y poda |
| Dependencia de nodo ligero | Se confía en un tercero | Declararlo en el mapa de riesgo |
| Exclusión por requisitos | Solo los grandes participan | Subvención o modelo escalonado |
| Orden de transacciones | Quien ordena tiene ventaja | Reglas de ordenación explícitas |
| Repetición de transacción | Se ejecuta dos veces | Número de orden por cuenta |

## 🧪 Práctica

En [`labs/lab-01.md`](../labs/lab-01.md):

1. Implementa la cadena con transacciones firmadas y número de orden.
2. Demuestra que una transacción repetida se rechaza.
3. Calcula el crecimiento anual con tres configuraciones.
4. Implementa instantáneas y reconstruye un estado pasado.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Dimensionar solo la cadena | Se olvidó la consulta histórica | Instantáneas o índice auditado |
| Guardar dato personal | Se trató como base de datos | Resumen dentro, dato fuera |
| Ignorar la mempool | Se pensó en la inclusión | Es pública y accionable |
| Nodo ligero sin declararlo | Se asumió equivalente | Es una dependencia de terceros |
| Sin número de orden | Se confió en la unicidad | La transacción se puede repetir |
| Requisitos que excluyen | Se optimizó para el grande | Decide quién participa |

## ❓ Preguntas de comprobación

1. ¿Por qué se dice que el estado se deduce y no se guarda?
2. ¿Qué gana cada modelo de estado y cuál resuelve la repetición por diseño?
3. ¿Qué puede verificar por sí mismo un nodo ligero y qué no?
4. ¿Por qué el tamaño de bloque afecta a la descentralización?
5. En el ejemplo guiado, ¿qué dos decisiones estructurales salieron de un
   cálculo de disco?

## 📥 Entregable

Guarda en `portfolio/parte-19/clase-04/`:

- el ciclo completo de una transacción, con los ocho pasos;
- el cálculo de crecimiento a 10 años con tres configuraciones;
- el diseño de consulta histórica elegido, con su justificación;
- la lista de lo que el dimensionamiento no decide y quién debe decidirlo.

## 🔗 Referencias cruzadas

- **Viene de:** clases 1, 2 y 3.
- **Continúa en:** clase 5 (consenso), clase 6 (finalidad), clase 12
  (escalabilidad).
- **Se aplica en:** Parte 21, clase 14 (libros de órdenes); Parte 23, clase 11.

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

- NIST (2018). *NISTIR 8202: Blockchain Technology Overview*. NIST. <https://csrc.nist.gov/pubs/ir/8202/final>
- Committee on Payments and Market Infrastructures (2017). *Distributed ledger technology in payment, clearing and settlement*. BIS. <https://www.bis.org/cpmi/publ/d157.htm>
- ISO/TC 307. *ISO 22739: Blockchain and distributed ledger technologies — Vocabulary*. ISO. <https://www.iso.org/standard/82208.html>
- European Union Agency for Cybersecurity (2021). *Distributed Ledger Technology and Cybersecurity*. ENISA. <https://www.enisa.europa.eu/>
- Committee on Payments and Market Infrastructures e IOSCO (2012). *Principles for Financial Market Infrastructures*. BIS. <https://www.bis.org/cpmi/publ/d101.htm>
- Verificación local: comprueba los plazos de retención y los derechos de supresión de datos personales aplicables, y su compatibilidad con un registro inmutable. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 03 · Claves, direcciones y gestión criptográfica](03-claves-direcciones-y-gestion-criptografica.md) | [Parte 19](../README.md) · [Programa](../../../SYLLABUS.md) | [05 · Mecanismos de consenso →](05-mecanismos-de-consenso.md) |
<!-- gen:footer:end -->
