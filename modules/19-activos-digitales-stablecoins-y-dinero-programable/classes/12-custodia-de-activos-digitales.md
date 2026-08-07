<!-- meta
part: 20
class: 12
title: "Custodia de activos digitales"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional, chile]
regulatory_topics: [custodia, segregacion, riesgo-operacional]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [IOSCO, NIST, CMF]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 12 · Custodia de activos digitales

> [← 11 · Dinero programable y sus límites](11-dinero-programable-y-sus-limites.md) · [Índice de la parte](../README.md) · [13 · Mercado, liquidez y formación de precio →](13-mercado-liquidez-y-formacion-de-precio.md)

**Parte 20 — Activos digitales, stablecoins y dinero programable** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Diseñar la custodia de un activo cuyo control es una clave. **Quien tiene la
clave tiene el activo**, y por eso la custodia digital mezcla dos disciplinas que
en el mundo tradicional estaban separadas: la seguridad de la información y la
segregación patrimonial.

Los instrumentos de las once clases anteriores hay que guardarlos en alguna parte. Esta clase trata de dónde, y muestra que la criptografía protege del robo y solo un contrato bien redactado protege de la quiebra del custodio.

## 📚 Objetivos

Al finalizar podrás:

1. **Comparar** los cuatro modelos de custodia por sus modos de fallo.
2. **Diseñar** un esquema de umbral que resista pérdida y coacción.
3. **Distinguir** segregación operativa de segregación jurídica.
4. **Construir** un procedimiento de recuperación que no cree una puerta trasera.
5. **Definir** los controles de una operación de retirada, con sus tiempos.

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

Los cuatro primeros términos son los esquemas de custodia; los cuatro siguientes, sus protecciones jurídicas y operativas. La **segregación jurídica** es la que decide en un concurso: sin una cláusula que declare que el activo es del cliente y que el custodio no puede disponer de él, el cliente es un acreedor ordinario.

| Concepto | Comprensión verificable |
|---|---|
| `autocustodia` | El titular controla la clave |
| `custodia delegada` | Un tercero controla la clave por cuenta del titular |
| `firma múltiple` | Se exigen m de n firmas para mover |
| `cómputo multiparte` | La clave nunca existe completa en ningún sitio |
| `almacenamiento en frío` | Claves sin conexión a red |
| `segregación jurídica` | El activo no entra en la masa del custodio |
| `lista blanca de destinos` | Solo se retira a direcciones aprobadas |
| `ventana de espera` | Retardo obligatorio entre orden y ejecución |

## 🧠 Modelo mental

El modelo mental es que la criptografía protege del robo y no de la quiebra. Un esquema técnicamente impecable con un contrato de custodia deficiente deja al cliente sin nada si el custodio entra en concurso.

```text
LA DIFERENCIA CON LA CUSTODIA TRADICIONAL

  UN VALOR ANOTADO EN UN DEPOSITARIO
    si te roban el acceso, el asiento sigue
    ahí y se corrige

  UN ACTIVO CONTROLADO POR CLAVE
    si te roban la clave, el activo se movió
    y no hay asiento que corregir

  → LA SEGURIDAD DE LA CLAVE NO ES
    UN CONTROL DE TI: ES EL ACTIVO

LOS DOS FALLOS SIMÉTRICOS
  PERDER la clave       → nadie puede mover
  FILTRAR la clave      → cualquiera puede mover

  Y TODA MEDIDA QUE REDUCE UNO
  SUELE AUMENTAR EL OTRO
```

## 📖 Desarrollo

### 1. Los cuatro modelos

| Modelo | Quién controla | Fallo principal | Para quién |
|---|---|---|---|
| Autocustodia individual | El titular | Pérdida sin recuperación | Importes propios y pequeños |
| Autocustodia con umbral | El titular, repartido | Complejidad operativa | Tesorerías propias |
| Custodia delegada | El custodio | Concentración y quiebra | Clientes sin capacidad técnica |
| Custodia compartida | Titular y custodio | Coordinación en urgencia | Institucional |

### 2. Elección del umbral

```text
UN ESQUEMA m-DE-n

  m PEQUEÑO   fácil de operar, fácil de vulnerar
  m GRANDE    difícil de vulnerar, fácil de
              quedarse bloqueado

  LA PREGUNTA CORRECTA NO ES «¿CUÁNTOS?»
  SINO «¿QUÉ EVENTOS DEJAN INOPERATIVOS
  A CUÁNTOS A LA VEZ?»

EVENTOS QUE AFECTAN A VARIOS GUARDIANES
  · están en la misma oficina
  · usan el mismo dispositivo o proveedor
  · viajan juntos
  · dependen del mismo administrador
  · están sujetos a la misma jurisdicción

  → LA INDEPENDENCIA EFECTIVA (Parte 19, clase 5)
    se aplica aquí igual: 5 guardianes con
    el mismo proveedor son 1
```

### 3. Segregación operativa y jurídica

```text
SEGREGACIÓN OPERATIVA
  cada cliente tiene su dirección
  o su subcuenta identificada
  → resuelve la trazabilidad

SEGREGACIÓN JURÍDICA
  el activo no forma parte del patrimonio
  del custodio
  → resuelve la QUIEBRA

LAS DOS SON NECESARIAS Y NO SE SUSTITUYEN

  un custodio puede llevar direcciones
  separadas y, aun así, si el contrato dice
  que el activo es suyo, el cliente
  es acreedor ordinario

PREGUNTAS AL CONTRATO
  1 ¿de quién es el activo?
  2 ¿puede el custodio prestarlo o pignorarlo?
  3 ¿qué pasa en un concurso?
  4 ¿hay un tercero que verifique el saldo total
    contra la suma de los saldos de clientes?
```

### 4. Recuperación sin puerta trasera

```text
EL PROBLEMA
  hace falta poder recuperar el acceso
  si se pierde una parte
  pero cualquier mecanismo de recuperación
  es también un camino de ataque

DISEÑO QUE FUNCIONA
  · partes de recuperación distintas de las
    partes de firma
  · umbral de recuperación MÁS ALTO que el de firma
  · retardo obligatorio con notificación a todos
    los guardianes
  · posibilidad de que cualquier guardián
    CANCELE la recuperación durante el retardo
  · registro público interno de cada intento

POR QUÉ EL RETARDO ES LA PIEZA CLAVE
  un atacante que consigue el umbral de
  recuperación necesita además que nadie
  cancele durante N días,
  y eso es mucho más difícil que
  conseguir las partes
```

### 5. Controles de una retirada

```text
LA CADENA COMPLETA

  1 ORIGEN AUTORIZADO
      la orden viene de un usuario con permiso
  2 DESTINO EN LISTA BLANCA
      la dirección estaba aprobada antes
  3 ALTA DE DESTINO CON ESPERA
      añadir una dirección tarda 48 h
  4 LÍMITES POR IMPORTE Y POR VENTANA
      superarlos exige más firmas
  5 SEGUNDA APROBACIÓN FUERA DE BANDA
      por un canal distinto del de la orden
  6 VERIFICACIÓN DE LA DIRECCIÓN COMPLETA
      no solo los primeros y últimos caracteres
  7 REGISTRO INMUTABLE DE LA DECISIÓN

EL PASO 3 ES EL QUE DETIENE
EL ATAQUE MÁS COMÚN:
comprometer una sesión y retirar
a una dirección nueva en el momento
```

## 🧮 Ejemplo guiado

El ejemplo mide la independencia efectiva de un esquema y revisa las cláusulas del contrato. El hallazgo mayor suele estar en el contrato.

**Situación.** Un custodio institucional diseña su esquema. Hay que elegir el
umbral y medir si resiste los escenarios que importan.

```text
PROPUESTA INICIAL
  esquema 3-de-5
  guardianes
    G1 director de operaciones · oficina A
    G2 director de tecnología  · oficina A
    G3 director financiero     · oficina A
    G4 proveedor de custodia   · externo
    G5 socio del despacho      · externo

  almacenamiento: todos con el mismo
  modelo de dispositivo del mismo fabricante
```

**Paso 1 — calcula la independencia efectiva.**

```text
POR UBICACIÓN
  oficina A: G1, G2, G3 → 3 juntos
  externos:  G4, G5     → 2

  UN INCIDENTE EN LA OFICINA A
  (incendio, robo, orden judicial local)
  afecta a 3 de 5

  → ALCANZA EXACTAMENTE EL UMBRAL DE 3
    UN SOLO EVENTO PUEDE MOVER LOS FONDOS
    O DEJARLOS BLOQUEADOS

POR DISPOSITIVO
  los 5 usan el mismo modelo
  → una vulnerabilidad del fabricante
    afecta a 5 de 5

  INDEPENDENCIA EFECTIVA REAL: 1
```

**Paso 2 — corrige la distribución.**

```text
NUEVA DISTRIBUCIÓN

  G1 oficina A · dispositivo tipo X
  G2 oficina B · dispositivo tipo Y
  G3 oficina C · dispositivo tipo X
  G4 proveedor externo · tipo Z
  G5 despacho externo  · tipo Y

  MAYOR GRUPO POR UBICACIÓN:  1
  MAYOR GRUPO POR DISPOSITIVO: 2

  UN EVENTO DE UBICACIÓN afecta a 1 → sobra
  UNA VULNERABILIDAD DE TIPO X afecta a 2 → sobra
  UNA DE TIPO Y afecta a 2 → sobra

  → EL ESQUEMA 3-DE-5 AHORA SÍ TOLERA
    UN EVENTO CORRELACIONADO
```

**Paso 3 — comprueba el fallo por pérdida.**

```text
CON 3-DE-5, SE TOLERA PERDER 2 GUARDIANES

  ¿ES SUFICIENTE?
  probabilidad anual de indisponibilidad
  por guardián: supuesto 4 %

  probabilidad de que 3 o más
  estén indisponibles a la vez
  (supuesto: independientes)

  P(3 de 5) = C(5,3) × 0,04³ × 0,96²
            = 10 × 0,000064 × 0,9216
            = 0,00059

  P(4 de 5) = 5 × 0,04⁴ × 0,96 = 0,0000123
  P(5 de 5) = 0,04⁵ = 0,0000001

  TOTAL ≈ 0,06 % anual
  → aceptable, y el supuesto de independencia
    ahora es defendible tras el paso 2
```

**Paso 4 — diseña la recuperación.**

```text
PARTES DE RECUPERACIÓN: 4-DE-7

  los 5 guardianes de firma
  + 2 depositarios de partes que NO firman
    (un notario y una caja de seguridad
     en otra jurisdicción)

  RETARDO: 7 días
  NOTIFICACIÓN: a los 7 tenedores, por dos canales
  CANCELACIÓN: cualquiera de los 7 la detiene

  ¿POR QUÉ 4-DE-7 Y NO 3-DE-5?
    porque la recuperación evita el esquema
    normal: tiene que ser MÁS difícil,
    no igual de fácil
```

**Paso 5 — mide el ataque más probable.**

```text
ESCENARIO: SESIÓN DE UN OPERADOR COMPROMETIDA

  el atacante intenta retirar a una
  dirección propia

  CONTROL 2 · LISTA BLANCA
    la dirección no está → bloqueado

  el atacante intenta darla de alta

  CONTROL 3 · ESPERA DE 48 h
    → el alta queda pendiente y notificada

  CONTROL 5 · SEGUNDA APROBACIÓN FUERA DE BANDA
    → el atacante necesitaría también
      el canal de otro aprobador

  TIEMPO DISPONIBLE PARA DETECTAR: 48 h
  frente a los minutos que tendría
  sin el control 3
```

**Paso 6 — mide el ataque más costoso.**

```text
ESCENARIO: COACCIÓN SOBRE UN GUARDIÁN

  con 3-de-5, coaccionar a uno no basta

  ¿Y SI SE COACCIONA A DOS?
    tampoco

  ¿Y SI EL ATACANTE SABE QUIÉNES SON?
    ahí está el problema: la lista de
    guardianes es información sensible

  CONTROLES ADICIONALES
    · no publicar la composición
    · rotación periódica
    · señal de coacción: una firma
      con una parte alternativa que
      valida la operación en apariencia
      y dispara la alerta

  LA SEÑAL DE COACCIÓN ES UN CONTROL REAL
  y hay que probarla en un simulacro,
  no solo documentarla
```

**Paso 7 — cierra con la segregación jurídica.**

```text
TODO LO ANTERIOR ES SEGURIDAD.
FALTA LA PREGUNTA DE LA QUIEBRA.

  ¿DE QUIÉN ES EL ACTIVO?
    contrato: «el cliente conserva la
    propiedad; el custodio actúa por su cuenta»

  ¿PUEDE PRESTARLO O PIGNORARLO?
    contrato: «no, salvo instrucción expresa
    y específica del cliente»

  ¿VERIFICACIÓN INDEPENDIENTE?
    conciliación mensual del saldo total
    en cadena contra la suma de saldos
    de clientes, por un tercero

  SIN ESTAS TRES, EL MEJOR ESQUEMA
  CRIPTOGRÁFICO DEL MUNDO
  NO PROTEGE AL CLIENTE DE LA QUIEBRA
  DEL CUSTODIO
```

**Interpreta:** el esquema 3-de-5 inicial tenía una independencia efectiva de
**1**, y el número «3 de 5» sonaba prudente. La corrección no cambió el umbral:
cambió **dónde y con qué** están las partes. Y ningún control criptográfico
sustituye a las tres cláusulas del contrato.

## 🧭 Perspectivas

La custodia afecta a cada participante de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un saldo en una aplicación | En quién confía |
| Fintech | Un servicio de custodia | Qué contrata |
| Banco | Riesgo operacional nuevo | Si lo asume o lo delega |
| Custodio | Umbral y procedimientos | Cómo los diseña |
| Infraestructura | Direcciones de gran saldo | Qué vigila |
| Supervisor | Segregación y solvencia | Qué autoriza y qué exige |
| Auditor | Conciliación en cadena | Qué puede verificar |
| Aseguradora | Cobertura de pérdida | Qué excluye |
| Sociedad | Fondos perdidos sin recurso | Qué protección exige |

## 🏦 Del cliente al banco

El cliente cree que el activo es suyo y eso depende de una cláusula. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Mis fondos están seguros» | Depende del contrato, no solo de la clave | 20, clase 12 |
| «Es 3 de 5, es robusto» | La independencia efectiva puede ser 1 | 20, clase 12 |
| «El custodio quebró pero mis activos están» | Solo con segregación jurídica | 20, clase 12 |

## ⚖️ Riesgos y controles

Los riesgos son de concentración de claves y de segregación. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Guardianes correlacionados | Misma oficina o mismo dispositivo | Medir independencia efectiva |
| Recuperación como puerta trasera | Se usa para robar | Umbral mayor, retardo y cancelación |
| Retirada a dirección nueva | Sesión comprometida | Lista blanca con espera de 48 h |
| Sin segregación jurídica | El cliente es acreedor ordinario | Cláusula de propiedad y no pignoración |
| Coacción sobre un guardián | Amenaza directa | Composición reservada y señal de coacción |
| Saldo no conciliado | Diferencia entre libros y cadena | Conciliación mensual por un tercero |

## 🧪 Práctica

El laboratorio pide medir la independencia efectiva y verificar las tres cláusulas. La cuantificación de la exposición sin la cláusula de no disposición es lo que decide.

En [`labs/lab-06.md`](../labs/lab-06.md):

1. Calcula la independencia efectiva de un esquema dado.
2. Rediseña la distribución de partes y vuelve a medirla.
3. Diseña el procedimiento de recuperación con su retardo.
4. Ejecuta el escenario de sesión comprometida y mide el tiempo ganado.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen pérdidas de activos custodiados. Las causas son independencia efectiva de uno y segregación no pactada.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Elegir el umbral por intuición | «3 de 5 suena bien» | Mide qué eventos afectan a cuántos |
| Todos con el mismo dispositivo | Compra centralizada | Diversifica fabricante y modelo |
| Recuperación igual de fácil | Se busca comodidad | Debe ser más difícil que firmar |
| Sin espera para destinos nuevos | Molesta a los operadores | Es el control que detiene el ataque típico |
| Confiar en la segregación operativa | Se ven las subcuentas | La jurídica es la que importa en la quiebra |
| No probar la señal de coacción | Nadie quiere simularlo | Sin simulacro, no existe |

## ❓ Preguntas de comprobación

1. ¿Cuáles son los dos fallos simétricos de la custodia por clave?
2. ¿Qué es la independencia efectiva y cómo se mide aquí?
3. ¿Por qué el umbral de recuperación debe ser mayor que el de firma?
4. ¿Qué control detiene el ataque por sesión comprometida y por qué?
5. ¿Qué tres cláusulas contractuales protegen ante la quiebra del custodio?

## 📥 Entregable

Guarda en `portfolio/parte-20/clase-12/`:

- el cálculo de independencia efectiva antes y después del rediseño;
- el esquema de recuperación con umbral, retardo y cancelación;
- la cadena de siete controles de retirada con sus tiempos;
- las tres preguntas al contrato, respondidas con un caso real.

## 🔗 Referencias cruzadas

- **Viene de:** Parte 19, clases 3 y 5.
- **Continúa en:** clases 14 y 15 de esta parte.
- **Se aplica en:** Parte 21, clase 9; Parte 22, clase 9; Parte 23, clase 10.

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

- IOSCO (2023). *Policy Recommendations for Crypto and Digital Asset Markets*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- NIST (2016). *SP 800-57 Part 1: Recommendation for Key Management*. NIST. <https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final>
- NIST (2020). *SP 800-207: Zero Trust Architecture*. NIST. <https://csrc.nist.gov/pubs/sp/800/207/final>
- Comisión para el Mercado Financiero. *Normativa aplicable a la custodia de instrumentos financieros*. CMF. <https://www.cmfchile.cl/portal/principal/613/w3-channel.html>
- Verificación local: comprueba qué exige tu jurisdicción para custodiar activos digitales por cuenta de terceros, si requiere autorización previa y qué régimen de segregación impone. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 11 · Dinero programable y sus límites](11-dinero-programable-y-sus-limites.md) | [Parte 20](../README.md) · [Programa](../../../SYLLABUS.md) | [13 · Mercado, liquidez y formación de precio →](13-mercado-liquidez-y-formacion-de-precio.md) |
<!-- gen:footer:end -->
