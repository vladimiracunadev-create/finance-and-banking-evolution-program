---
part: 19
class: 3
title: "Claves, direcciones y gestión criptográfica"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global]
regulatory_topics: [dlt, custodia, criptografia, riesgo-operacional]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [NIST, Comité de Basilea]
requires_legal_review: true
---

<!-- gen:header:start -->
# Clase 03 · Claves, direcciones y gestión criptográfica

> [← 02 · Resúmenes, firmas y árboles de Merkle](02-resumenes-firmas-y-arboles-de-merkle.md) · [Índice de la parte](../README.md) · [04 · Transacciones, bloques, nodos y estado →](04-transacciones-bloques-nodos-y-estado.md)

**Parte 19 — Blockchain y DLT para instituciones financieras** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Tratar la clave privada como lo que es en un registro distribuido: **el activo
mismo**. Quien la tiene, dispone; quien la pierde, no recupera. No hay servicio
de atención al cliente detrás.

Las firmas de la clase anterior necesitan claves. Esta trata de cómo se custodian, y con una advertencia que ordena la clase entera: quien tiene la clave tiene el activo, y no hay recuperación posible.

## 📚 Objetivos

Al finalizar podrás:

1. **Explicar** la relación entre clave privada, clave pública y dirección.
2. **Comparar** los cuatro modelos de custodia por su superficie de fallo.
3. **Diseñar** un esquema de firma múltiple con umbral justificado.
4. **Especificar** un procedimiento de recuperación que no dependa de una sola
   persona.
5. **Evaluar** el riesgo de una jerarquía determinista y su punto único de fallo.

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

Los cuatro primeros términos son la identidad criptográfica; los cuatro siguientes, los esquemas de custodia. La **computación multiparte** es la alternativa a la firma múltiple cuando la red no la soporta, y su diferencia práctica es que produce una sola firma y no revela el esquema.

| Concepto | Comprensión verificable |
|---|---|
| `clave privada` | Secreto que autoriza a disponer; es el activo |
| `clave pública` | Derivada de la privada; permite verificar, no disponer |
| `dirección` | Identificador derivado de la clave pública |
| `semilla` | Valor del que se derivan todas las claves de una jerarquía |
| `firma múltiple` | Se exigen m firmas de n claves para disponer |
| `computación multiparte` | La clave nunca existe entera en ningún sitio |
| `módulo de seguridad` | Dispositivo que guarda claves y firma sin exponerlas |
| `almacenamiento en frío` | Claves sin conexión a ninguna red |

## 🧠 Modelo mental

El modelo mental es que quien tiene la clave tiene el activo, sin excepciones ni recuperación. Toda la gestión criptográfica consiste en repartir esa capacidad entre varias personas y sistemas sin perderla del todo.

```text
LA ASIMETRÍA QUE DEFINE TODO

  clave privada  ──derivación irreversible──►  clave pública
                                                    │
                                          ──resumen──►  dirección

  de la privada se obtiene todo lo demás
  del resto NO se obtiene la privada

CONSECUENCIAS QUE NO TIENE UNA CUENTA BANCARIA
  · perder la clave = perder el activo, definitivamente
  · robar la clave = disponer del activo, sin fricción
  · no hay «he olvidado mi contraseña»
  · no hay reversión de una transferencia autorizada

POR ESO LA CUSTODIA NO ES UN DETALLE OPERATIVO:
ES EL PRODUCTO
```

## 📖 Desarrollo

### 1. De la clave a la dirección

```text
1. se genera una clave privada: un número aleatorio
   de suficiente entropía
2. se deriva la clave pública mediante una operación
   de un solo sentido sobre una curva elíptica
3. se aplica una función de resumen a la clave pública
4. se codifica el resultado con verificación de errores

LA CODIFICACIÓN CON VERIFICACIÓN IMPORTA
  detecta un carácter mal tecleado antes de enviar
  → sin ella, un error de tecla envía los fondos
    a una dirección que nadie controla, y no vuelven

LA ENTROPÍA IMPORTA MÁS
  una clave generada con un generador predecible
  se puede reconstruir. Ha ocurrido, y ha vaciado
  carteras enteras.
```

### 2. Los cuatro modelos de custodia

| Modelo | Quién tiene la clave | Riesgo dominante | Uso típico |
|---|---|---|---|
| Autocustodia | El titular | Pérdida y error humano | Individuo |
| Custodia de un tercero | El custodio | Insolvencia y concentración | Inversionista institucional |
| Firma múltiple | Repartida entre m de n | Coordinación y disponibilidad | Tesorería corporativa |
| Computación multiparte | Nunca existe entera | Complejidad de implementación | Institución financiera |

```text
LA DIFERENCIA ENTRE FIRMA MÚLTIPLE Y MULTIPARTE

  FIRMA MÚLTIPLE   existen n claves completas;
                   se necesitan m firmas
                   → si un guardián es comprometido,
                     se compromete UNA clave entera

  MULTIPARTE       la clave nunca se ensambla;
                   cada parte tiene un fragmento
                   → comprometer un fragmento no da nada
                   → pero la implementación es mucho más
                     difícil de auditar
```

### 3. Elegir el umbral

```text
UN ESQUEMA m-de-n TIENE DOS FALLOS OPUESTOS

  m demasiado bajo  → basta comprometer m guardianes
  m demasiado alto  → basta perder n − m + 1 para
                      quedarse sin acceso

  DISPONIBILIDAD    exige m pequeño
  SEGURIDAD         exige m grande

CÓMO SE ELIGE
  1. ¿cuántos guardianes pueden fallar a la vez
     por una causa común? (mismo edificio, mismo
     proveedor, mismo país)
  2. ¿cuántos podrían coludir?
  3. m > número de coludidos plausibles
  4. n − m ≥ número de fallos simultáneos plausibles

EJEMPLO DE 3-DE-5 BIEN CONSTRUIDO
  cinco guardianes en cinco ubicaciones, con tres
  proveedores de módulo distintos y dos jurisdicciones
  → tolera 2 pérdidas y exige colusión de 3
```

### 4. Jerarquías deterministas y su punto único

```text
UNA SEMILLA GENERA UNA JERARQUÍA COMPLETA DE CLAVES

  VENTAJA
    una copia de seguridad basta para todas

  RIESGO
    esa copia es el punto único de fallo del sistema entero

  Y UN RIESGO MENOS OBVIO
    en algunas construcciones, conocer una clave pública
    extendida MÁS una clave privada hija permite derivar
    la clave privada padre

    → una clave de una cuenta puede comprometer todas
    → hay que conocer la construcción concreta antes
      de repartir claves derivadas
```

### 5. Recuperación: el procedimiento que casi nadie escribe

```text
UN PROCEDIMIENTO DE RECUPERACIÓN RESPONDE

  1. ¿qué se recupera? claves, o acceso a la firma
  2. ¿quién lo autoriza? nunca una sola persona
  3. ¿dónde están las copias? ubicaciones separadas
  4. ¿cómo se verifica la integridad de una copia?
  5. ¿cada cuánto se ENSAYA?
  6. ¿qué pasa si un guardián muere o se va?
  7. ¿cómo se rota tras una recuperación?

LA 5 ES LA QUE FALLA
  un procedimiento no ensayado es una intención.
  Y el ensayo revela lo que el documento oculta:
  que la copia estaba en un formato ilegible,
  que el guardián olvidó su parte, o que la caja
  fuerte cambió de combinación.
```

## 🧮 Ejemplo guiado

El ejemplo mide la independencia efectiva de un esquema de firma múltiple. Conviene contar los factores compartidos: un esquema de cinco partes con un solo tipo de dispositivo tiene la independencia de una.

**Situación.** Un banco diseña la custodia de activos digitales de clientes.
Debe elegir el esquema y justificarlo ante el comité de riesgo.

```text
ACTIVOS BAJO CUSTODIA PREVISTOS      680 000 000
OPERACIONES DE SALIDA AL DÍA                  42
IMPORTE MEDIO POR OPERACIÓN            1 200 000
IMPORTE MÁXIMO POR OPERACIÓN          45 000 000

RESTRICCIONES
  · el banco opera en dos países
  · el proveedor de módulos de seguridad es uno solo
  · el equipo de tesorería digital son 6 personas
  · el objetivo de disponibilidad es 99,5 %
```

**Paso 1 — separa los fondos por función.**

```text
NO TODO EL SALDO NECESITA LA MISMA CUSTODIA

  OPERATIVO (caliente)
    lo necesario para las salidas de un día
    42 × 1 200 000 = 50 400 000
    + margen para el máximo: 45 000 000
    ≈ 95 000 000  (14 % del total)

  RESERVA (templado)
    reposición de 3 días: 150 000 000  (22 %)

  FRÍO
    el resto: 435 000 000  (64 %)

ESTA SEPARACIÓN ES LA DECISIÓN MÁS IMPORTANTE
  el 64 % pasa a un esquema donde un compromiso
  del entorno operativo no lo alcanza
```

**Paso 2 — asigna esquema a cada bolsa.**

```text
CALIENTE (95 M)
  firma múltiple 2-de-3, con módulos de seguridad
  automatizada, con límites por operación y por día
  disponibilidad alta, seguridad media

TEMPLADO (150 M)
  firma múltiple 3-de-5, aprobación humana
  ventana de firma de 4 horas

FRÍO (435 M)
  firma múltiple 4-de-7, guardianes en dos países,
  material fuera de línea, ventana de 48 horas
```

**Paso 3 — comprueba la independencia de los guardianes.**

```text
EL ESQUEMA 4-DE-7 DEL FRÍO

  ¿pueden fallar 4 a la vez por una causa común?
    · los 7 usan módulos del MISMO PROVEEDOR
    · un defecto del proveedor los afecta a todos

  → el esquema tolera 3 pérdidas independientes
    y CERO fallos del proveedor

HALLAZGO: el punto único de fallo no es un guardián,
es el proveedor de módulos
```

**Paso 4 — corrige la dependencia.**

```text
OPCIÓN A · segundo proveedor para 3 de los 7
  coste: 340 000 inicial + 90 000 anual
  efecto: un defecto de un proveedor deja 3 o 4 claves
          → con umbral 4, un fallo del proveedor mayoritario
            deja 3: NO se puede firmar
          → hay que bajar el umbral a 3-de-7, y eso
            reduce la seguridad

OPCIÓN B · segundo proveedor para 4 de los 7, umbral 4
  coste: 450 000 inicial + 120 000 anual
  efecto: cualquier proveedor que falle deja al menos 3...
          tampoco basta

OPCIÓN C · 4-de-9, con 3 proveedores (3+3+3)
  coste: 610 000 inicial + 180 000 anual
  efecto: fallo de un proveedor deja 6 claves ≥ 4  ✓
          colusión exige 4 guardianes de al menos 2 proveedores
```

**Paso 5 — verifica el coste frente al riesgo.**

```text
COSTE ADICIONAL DE LA OPCIÓN C
  610 000 inicial + 180 000 anual
  amortizado a 5 años: 302 000 al año

RIESGO QUE CUBRE
  pérdida de acceso a 435 000 000 por un defecto
  del único proveedor

  la probabilidad es baja y NO se puede estimar bien.
  Lo que sí se puede afirmar:
    · el evento es catastrófico y no recuperable
    · el coste de cubrirlo es el 0,07 % del importe protegido

  302 000 / 435 000 000 = 0,069 % anual

CON ESE COCIENTE, LA DISCUSIÓN SE ACABA
```

**Paso 6 — diseña la recuperación.**

```text
PROCEDIMIENTO PARA EL FRÍO

  1. QUÉ SE RECUPERA: la capacidad de firmar, no la clave
  2. AUTORIZA: 2 miembros del comité + auditoría interna
  3. COPIAS: 9 fragmentos en 6 ubicaciones, 2 jurisdicciones
  4. INTEGRIDAD: cada copia lleva su resumen, verificado
     en cada ensayo
  5. ENSAYO: trimestral, con firma real de una operación
     de importe simbólico
  6. GUARDIÁN QUE SE VA: rotación de su fragmento en 5 días
     hábiles, con constancia
  7. TRAS UNA RECUPERACIÓN: rotación completa del esquema

EL PUNTO 5 CON FIRMA REAL ES LO QUE DISTINGUE
UN PROCEDIMIENTO DE UN DOCUMENTO
```

**Paso 7 — declara lo que sigue sin resolver.**

```text
RIESGOS RESIDUALES QUE EL ESQUEMA NO CIERRA

  · error de dirección de destino: irreversible.
    Se mitiga con lista blanca y confirmación,
    no se elimina
  · coacción sobre 4 guardianes: el esquema no distingue
    una firma libre de una forzada
    → se mitiga con ventanas de tiempo y alertas
      fuera de banda
  · defecto en la implementación de multiparte,
    si se adoptara: más difícil de auditar que la
    firma múltiple
  · insolvencia del propio banco: la custodia debe estar
    SEGREGADA y ser oponible; eso es jurídico, no técnico

EL ÚLTIMO ES EL MÁS IMPORTANTE Y EL ÚNICO
QUE NINGUNA CLAVE RESUELVE
```

**Interpreta:** el diseño empezó eligiendo un umbral y el hallazgo estuvo en la
**correlación entre guardianes**: siete claves independientes sobre un solo
proveedor son, para el fallo que importa, una sola clave. La separación por
funciones —caliente, templado, frío— hizo el 64 % del trabajo antes de discutir
ningún umbral.

## 🧭 Perspectivas

La custodia de claves afecta a cada participante de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | «El banco custodia mis activos» | Si confía en la segregación |
| Tesorería digital | 42 salidas al día | Cuánto deja en caliente |
| Guardián | Un fragmento y una responsabilidad | Si acepta el rol |
| Riesgo operacional | Correlación entre guardianes | Qué esquema aprueba |
| Auditor | Ensayos con firma real | Qué evidencia acepta |
| Supervisor | Segregación y oponibilidad | Qué exige |
| Asesor jurídico | Insolvencia del custodio | Cómo se estructura |

## 🏦 Del cliente al banco

El cliente cree que su activo está en una cuenta y depende de quién tenga las claves. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Perdí mi clave y perdí todo» | No hay recuperación posible | 19, clase 3 |
| «Prefiero que lo custodie el banco» | Segregación, seguro y procedimiento | 19, clase 3 |
| «Envié a la dirección equivocada» | Irreversible: lista blanca lo previene | 19, clase 3 |
| «¿Qué pasa si quiebra el banco?» | Oponibilidad de la segregación | 21, clase 10 |

## ⚖️ Riesgos y controles

Los riesgos son de pérdida y de concentración. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Guardianes correlacionados | Un proveedor común los afecta a todos | Diversidad de proveedor y ubicación |
| Umbral mal elegido | Se pierde el acceso o se compromete fácil | Analizar colusión y fallo conjunto |
| Semilla como punto único | Una copia compromete todo | Separar jerarquías por función |
| Procedimiento no ensayado | Falla cuando se necesita | Ensayo trimestral con firma real |
| Dirección errónea | Transferencia irreversible | Lista blanca y confirmación |
| Coacción | Firma válida bajo presión | Ventanas, alertas fuera de banda |
| Segregación no oponible | La custodia entra en la masa | Estructura jurídica verificada |

## 🧪 Práctica

El laboratorio pide medir la independencia efectiva de varios esquemas y corregir el peor. La corrección se hace redistribuyendo y no cambiando el umbral.

En [`labs/lab-02.md`](../labs/lab-02.md):

1. Genera un par de claves y deriva la dirección, con verificación de errores.
2. Implementa un esquema de firma múltiple y prueba el umbral.
3. Analiza la correlación entre guardianes de un esquema dado.
4. Escribe el procedimiento de recuperación con sus siete preguntas.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen pérdidas de acceso o de activos. Las causas son esquemas con independencia efectiva de uno y recuperación mal diseñada.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Un solo esquema para todo el saldo | No se separó por función | Caliente, templado y frío |
| Guardianes con el mismo proveedor | Se contaron claves, no fallos | Diversidad efectiva |
| Umbral elegido «porque suena bien» | No se analizó colusión ni pérdida | Cuatro preguntas del umbral |
| Copia de seguridad única de la semilla | Se buscó comodidad | Fragmentos separados |
| Procedimiento sin ensayo | Se documentó y archivó | Firma real trimestral |
| Confundir custodia técnica con segregación | Se resolvió lo técnico | La oponibilidad es jurídica |

## ❓ Preguntas de comprobación

1. ¿Qué se deriva de qué, y qué operación es irreversible?
2. ¿Qué diferencia hay entre firma múltiple y computación multiparte, y qué
   riesgo cambia?
3. ¿Cuáles son las cuatro preguntas para elegir un umbral?
4. En el ejemplo guiado, ¿por qué siete claves eran, para el fallo que importa,
   una sola?
5. ¿Cuál de los riesgos residuales no lo resuelve ninguna clave?

## 📥 Entregable

Guarda en `portfolio/parte-19/clase-03/`:

- la separación de un saldo en caliente, templado y frío, con su justificación;
- el esquema de firma múltiple elegido, con el análisis de correlación;
- el procedimiento de recuperación con las siete preguntas respondidas;
- la lista de riesgos residuales, señalando cuál no es técnico.

## 🔗 Referencias cruzadas

- **Viene de:** clase 2 (firmas); Parte 17, clase 7 (rotación de claves).
- **Continúa en:** clase 8 (contratos), clase 13 (recuperación).
- **Se aplica en:** Parte 20, clase 11 (wallets y custodia); Parte 21, clase 10;
  Parte 23, clase 10.

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

- NIST (2020). *SP 800-57 Part 1 Rev. 5: Recommendation for Key Management*. NIST. <https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final>
- NIST (2019). *FIPS 140-3: Security Requirements for Cryptographic Modules*. NIST. <https://csrc.nist.gov/pubs/fips/140-3/final>
- Basel Committee on Banking Supervision (2022). *Prudential treatment of cryptoasset exposures*. BIS. <https://www.bis.org/bcbs/publ/d545.htm>
- Committee on Payments and Market Infrastructures e IOSCO (2022). *Application of the Principles for Financial Market Infrastructures to stablecoin arrangements*. BIS. <https://www.bis.org/cpmi/publ/d206.htm>
- NIST (2018). *NISTIR 8202: Blockchain Technology Overview*. NIST. <https://csrc.nist.gov/pubs/ir/8202/final>
- Verificación local: comprueba qué exige tu supervisor en materia de custodia y segregación de activos digitales, y si la segregación es oponible en un procedimiento de insolvencia en tu jurisdicción. **Fecha de verificación de esta clase: 2026-08-06.** Esta clase no constituye asesoría legal.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 02 · Resúmenes, firmas y árboles de Merkle](02-resumenes-firmas-y-arboles-de-merkle.md) | [Parte 19](../README.md) · [Programa](../../../SYLLABUS.md) | [04 · Transacciones, bloques, nodos y estado →](04-transacciones-bloques-nodos-y-estado.md) |
<!-- gen:footer:end -->
