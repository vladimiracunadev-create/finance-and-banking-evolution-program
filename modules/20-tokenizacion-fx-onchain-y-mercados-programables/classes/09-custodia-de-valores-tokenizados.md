---
part: 21
class: 9
title: "Custodia de valores tokenizados"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [chile, internacional]
regulatory_topics: [custodia, segregacion, depositario]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [IOSCO, CPMI, CMF]
requires_legal_review: true
---

<!-- gen:header:start -->
# Clase 09 · Custodia de valores tokenizados

> [← 08 · Entrega contra pago atómica](08-entrega-contra-pago-atomica.md) · [Índice de la parte](../README.md) · [10 · El tramo de dinero →](10-el-tramo-de-dinero.md)

**Parte 21 — Tokenización, FX on-chain y mercados programables** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Aplicar a los valores tokenizados la custodia de la Parte 20, clase 12, y añadir
lo que un valor exige y un activo al portador no: **el ejercicio de derechos por
cuenta del titular** y la relación con el depositario central.

El instrumento liquidado en la clase anterior queda en algún sitio. Esta clase trata la cadena de custodia y la estructura de cuentas, que es lo que decide si el cliente recupera su valor en un concurso.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** custodia de valores de custodia de criptoactivos.
2. **Determinar** quién ejerce los derechos cuando la titularidad es indirecta.
3. **Diseñar** la conciliación entre el registro, el custodio y el depositario.
4. **Evaluar** un modelo de custodia por su comportamiento en un concurso.
5. **Especificar** el plan de sustitución del custodio.

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

Los cuatro primeros términos son las estructuras de custodia; los cuatro siguientes, la cadena y sus protecciones. La distinción entre **cuenta ómnibus y segregada** es la que decide en un concurso: en la primera los activos de los clientes están mezclados y probar cuál es de quién puede llevar años.

| Concepto | Comprensión verificable |
|---|---|
| `custodia de valores` | Guarda y administración por cuenta del titular |
| `administración` | Cobro de cupones y ejercicio de derechos |
| `cuenta ómnibus` | Una posición global con varios titulares detrás |
| `cuenta segregada` | Una posición por titular en el registro |
| `depositario central` | Infraestructura que lleva el registro de valores |
| `cadena de custodia` | Secuencia de intermediarios hasta el titular final |
| `sustitución del custodio` | Traslado de posiciones a otro custodio |
| `no pignoración` | Compromiso de no usar el activo como garantía propia |

## 🧠 Modelo mental

El modelo mental es una cadena de custodia con eslabones que pueden quebrar. La tokenización no elimina la cadena: la reordena, y hay que saber en qué eslabón está el derecho del cliente en cada momento.

```text
UNA CUSTODIA DE VALORES HACE DOS COSAS

  GUARDAR
    y aquí aplica todo lo de la Parte 20,
    clase 12: umbral, independencia efectiva,
    lista blanca, segregación jurídica

  ADMINISTRAR
    cobrar cupones, ejercer opciones, votar,
    reclamar, informar
    → y esto NO existe en la custodia
      de un criptoactivo al portador

LA SEGUNDA ES LA QUE SE OLVIDA
  un custodio que solo guarda claves no es
  un custodio de valores: es un almacén.
  Y un valor sin quien administre sus derechos
  pierde valor real, no nominal.
```

## 📖 Desarrollo

### 1. Ómnibus frente a segregada

| Aspecto | Cuenta ómnibus | Cuenta segregada |
|---|---|---|
| Registro | Una posición global | Una por titular |
| Coste | Menor | Mayor |
| Trazabilidad | En los libros del custodio | En el registro |
| Concurso del custodio | Depende de sus libros | Directa |
| Ejercicio de derechos | Agregado por el custodio | Directo |
| Fecha de corte | El custodio reparte | El registro fija |
| Error de conciliación | Afecta al conjunto | Afecta a un titular |

```text
LA TOKENIZACIÓN HACE BARATA LA SEGREGADA
  y esa es una ventaja real y poco citada:
  con un registro programable, una posición
  por titular no cuesta significativamente
  más que una global
```

### 2. La cadena de custodia

```text
UNA POSICIÓN PUEDE ATRAVESAR VARIOS
INTERMEDIARIOS

  titular final
    └── su banco
          └── custodio global
                └── custodio local
                      └── depositario central

  CADA ESLABÓN
    · añade un riesgo de crédito
    · añade un punto de fallo operativo
    · añade un retraso en el ejercicio
      de derechos
    · puede aplicar su propia política

QUÉ CAMBIA CON UN REGISTRO PROGRAMABLE
  la cadena PUEDE acortarse, pero solo si
  el régimen lo permite: muchos eslabones
  existen porque una norma los exige

QUÉ NO CAMBIA
  si la cadena sigue, el token no la elimina:
  la representa
```

### 3. Concurso del custodio

```text
LA PREGUNTA DE LA CLASE 12, APLICADA
A VALORES

  ¿EL VALOR ES DEL CLIENTE O DEL CUSTODIO?

  EN VALORES, LA RESPUESTA SUELE ESTAR
  EN LA NORMA Y NO EN EL CONTRATO
  → la mayoría de regímenes de custodia
    de valores establecen que los valores
    custodiados no integran la masa

  PERO ESO APLICA A VALORES
  RECONOCIDOS COMO TALES

  SI EL INSTRUMENTO TOKENIZADO NO ESTÁ
  CALIFICADO COMO VALOR EN ESA
  JURISDICCIÓN, EL RÉGIMEN PROTECTOR
  PUEDE NO APLICARLE

  → y entonces vuelve a depender del contrato
    y de las tres cláusulas de la clase 12

ES OTRA CONSECUENCIA DE LA CALIFICACIÓN
DE LA CLASE 1.
```

### 4. La conciliación a tres bandas

```text
TRES REGISTROS QUE DEBEN COINCIDIR

  el registro del token
  los libros del custodio
  el registro del depositario central

  Y LA CONCILIACIÓN NO ES DOS A DOS:
  es a tres bandas, y una diferencia puede
  estar en cualquiera de los tres

PROCEDIMIENTO
  1 comparación diaria de los tres
  2 al detectar diferencia, congelación
    en los tres
  3 identificación del registro erróneo
    con la evidencia de las operaciones
  4 corrección y compensación

QUIÉN LO HACE
  hay que designarlo: si cada uno concilia
  contra el siguiente, nadie mira el conjunto
```

### 5. Sustitución del custodio

```text
EL PLAN QUE NADIE ESCRIBE HASTA QUE
HACE FALTA

  ¿QUÉ PASA SI EL CUSTODIO PIERDE
   LA AUTORIZACIÓN, QUIEBRA O DECIDE
   DEJAR EL NEGOCIO?

  ELEMENTOS DEL PLAN
    · custodio sustituto identificado
      o procedimiento para designarlo
    · copia del registro de posiciones
      en poder de un tercero, diaria
    · procedimiento de traslado con plazo
    · quién paga el traslado
    · qué pasa con los eventos corporativos
      durante la transición
    · comunicación a los titulares

LA COPIA DIARIA ES LA PIEZA CRÍTICA
  sin ella, la sustitución depende de la
  cooperación de quien está en dificultades
```

## 🧮 Ejemplo guiado

El ejemplo compara la posición del cliente en cuenta ómnibus y en segregada ante un concurso. La diferencia es entre recuperar el activo y ser acreedor ordinario.

**Situación.** Un custodio institucional custodia bonos tokenizados por
280 000 000 de 1 840 clientes. Hay que evaluar el modelo y su resiliencia.

```text
DATOS
  valor custodiado               280 000 000
  clientes                             1 840
  modelo actual              cuenta ómnibus
  esquema de firma                    3-de-5
  guardianes                4 en la sede, 1 externo
  conciliación               semanal, dos a dos
  eventos corporativos al año             46
  copia del registro en tercero          no
  custodio sustituto                     no
```

**Paso 1 — mide la independencia efectiva.**

```text
GUARDIANES
  4 en la sede + 1 externo

  mayor grupo por ubicación: 4
  umbral: 3

  4 ≥ 3 → UN SOLO EVENTO EN LA SEDE
  ALCANZA EL UMBRAL

  independencia efectiva = 5 − 4 + 1 = 2
  tolera evento correlacionado: NO
```

**Paso 2 — evalúa el modelo ómnibus.**

```text
UNA POSICIÓN GLOBAL DE 280 000 000
CON 1 840 TITULARES EN LOS LIBROS
DEL CUSTODIO

  EN UN CONCURSO
    hay que demostrar quién es titular de qué
    con los libros del custodio,
    que es la parte en concurso

  COSTE DE LA SEGREGADA
    supuesto: 0,4 al mes por posición
    1 840 × 0,4 × 12 = 8 832 al año

  → 8 832 AL AÑO PARA QUE 1 840 TITULARES
    APAREZCAN EN EL REGISTRO
    sobre 280 000 000 custodiados
    = 0,0032 % anual

  LA SEGREGADA ES ASEQUIBLE
  Y LA DECISIÓN DE NO USARLA NO SE
  SOSTIENE POR COSTE.
```

**Paso 3 — dimensiona la conciliación.**

```text
CONCILIACIÓN SEMANAL Y DOS A DOS

  ventana de divergencia: hasta 7 días
  operaciones semanales: supuesto 640

  UNA DIFERENCIA PUEDE AFECTAR A
  hasta 640 operaciones antes de detectarse

  Y AL SER DOS A DOS, UNA DIFERENCIA
  ENTRE EL TOKEN Y EL DEPOSITARIO
  puede quedar oculta si el custodio
  concilia bien con cada uno por separado

EJEMPLO CONCRETO
  token dice 100, custodio dice 100,
  depositario dice 98
  · token contra custodio: coincide ✓
  · custodio contra depositario: no ✓ se ve
  pero si el custodio ajusta sus libros al
  depositario sin avisar al token,
  las dos conciliaciones dan bien
  y la diferencia persiste
```

**Paso 4 — calcula el riesgo de los eventos corporativos.**

```text
46 EVENTOS AL AÑO SOBRE UNA CUENTA ÓMNIBUS

  el custodio recibe el importe global
  y lo reparte según sus libros

  SI SUS LIBROS TIENEN UNA DIFERENCIA
  el reparto es incorrecto y el error
  se propaga a todos los eventos siguientes

  supuesto: tasa de error del 0,3 % por evento
  46 × 0,3 % = 0,14 eventos con error al año
  → uno cada siete años

  ¿ES POCO? el importe medio de un evento
  supuesto: 1 900 000
  un reparto erróneo sobre 1 840 titulares
  cuesta más corregirlo que su importe
  (clase 5, paso 2)
```

**Paso 5 — evalúa la ausencia de plan de sustitución.**

```text
SIN COPIA DEL REGISTRO EN UN TERCERO

  si el custodio pierde la autorización
  · las posiciones están en sus libros
  · el registro del token dice «custodio X»
    para toda la posición ómnibus
  · nadie fuera sabe quién tiene qué

  TIEMPO ESTIMADO DE RECONSTRUCCIÓN
  supuesto: 4 a 8 semanas
  durante las cuales 1 840 titulares
  no pueden operar ni cobrar

COSTE PARA LOS TITULARES
  280 000 000 × 4,3 % × 6/52 = 1 390 000
  solo de coste de oportunidad
```

**Paso 6 — propón el rediseño.**

```text
1 REDISTRIBUIR GUARDIANES
    2 en sede, 1 en filial, 1 proveedor,
    1 despacho, con dispositivos distintos
    → independencia efectiva 4, tolera evento

2 PASAR A CUENTA SEGREGADA
    8 832 al año, 0,0032 % del custodiado
    → titularidad directa en el registro

3 CONCILIACIÓN DIARIA A TRES BANDAS
    con un responsable designado que mire
    los tres a la vez

4 COPIA DIARIA EN UN TERCERO
    y un custodio sustituto identificado
    con procedimiento probado una vez al año

5 CLÁUSULA DE NO PIGNORACIÓN EXPRESA
    y verificación independiente mensual

COSTE TOTAL ESTIMADO
  supuesto: 46 000 al año
  frente a 1 390 000 de un solo episodio
  de sustitución
```

**Paso 7 — comprueba la calificación.**

```text
Y ANTES DE TODO LO ANTERIOR:

  ¿ESTÁ EL INSTRUMENTO CALIFICADO
   COMO VALOR EN ESTA JURISDICCIÓN?

  SI SÍ
    el régimen de custodia de valores aplica
    y los valores no integran la masa

  SI NO
    todo depende del contrato, y hay que
    exigir las tres cláusulas de la
    Parte 20, clase 12

  ESTA PREGUNTA VA PRIMERO
  porque cambia qué protege al cliente.
```

**Interpreta:** el custodio tenía una independencia efectiva de 2 con un umbral
de 3, conciliaba de forma que una diferencia podía persistir dando ambas
comprobaciones por buenas, y **la cuenta segregada que habría resuelto la mitad
de los problemas costaba 8 832 al año sobre 280 millones custodiados**.

## 🧭 Perspectivas

La custodia de valores tokenizados afecta a cada participante de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un saldo en su aplicación | En quién confía |
| Inversionista | Derechos ejercidos por otro | Si lo verifica |
| Emisor | Un custodio entre él y el titular | Cómo informa |
| Custodio | Coste de la segregación | Qué modelo ofrece |
| Depositario | Una posición ómnibus | Qué exige conciliar |
| Banco | Cadena de custodia larga | Cuántos eslabones acepta |
| Supervisor | Titularidad opaca | Qué segregación exige |
| Auditor | Tres registros | Cómo los concilia |
| Administrador concursal | Libros de la parte en concurso | Cómo reparte |
| Sociedad | Titularidad menos clara | Qué certeza exige |

## 🏦 Del cliente al banco

El cliente cree que el valor es suyo y depende de la estructura de la cuenta. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «El custodio tiene mis bonos» | Están en una posición global | 21, clase 9 |
| «Está todo conciliado» | Dos a dos puede ocultar una diferencia | 21, clase 9 |
| «Si quiebra, me los devuelven» | Solo si está calificado como valor | 21, clase 9 |

## ⚖️ Riesgos y controles

Los riesgos son de segregación y de pignoración indebida. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Guardianes correlacionados | Un evento alcanza el umbral | Redistribuir sin cambiar el umbral |
| Ómnibus sin necesidad | Titularidad en libros del custodio | Segregada, ahora asequible |
| Conciliación dos a dos | Una diferencia persiste | A tres bandas con responsable |
| Sin copia en un tercero | La sustitución depende del que falla | Copia diaria e independiente |
| Calificación no verificada | El régimen protector no aplica | Verificarla antes de contratar |
| Administración no prestada | El valor pierde sus derechos | Exigirla en el contrato |

## 🧪 Práctica

El laboratorio pide analizar una cadena de custodia y localizar dónde está el derecho del cliente. La cláusula de no pignoración es lo que hay que verificar.

En [`labs/lab-04.md`](../labs/lab-04.md):

1. Mide la independencia efectiva del esquema y redistribúyelo.
2. Simula la conciliación a tres bandas y provoca la diferencia oculta.
3. Calcula el coste de la cuenta segregada frente al valor custodiado.
4. Escribe el plan de sustitución con sus seis elementos.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen valores custodiados que no se recuperan. La causa es la cuenta ómnibus sin registro individualizado.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Custodiar solo claves | Se copia de los criptoactivos | Un valor exige administración |
| Ómnibus por defecto | Era lo barato | Con registro programable ya no lo es |
| Conciliar dos a dos | Es lo natural | Una diferencia puede ocultarse |
| Sin plan de sustitución | Nadie prevé el cierre | La copia diaria es la pieza crítica |
| Suponer el régimen de valores | Se asume por parecido | Depende de la calificación |
| Cadena larga sin contar | Cada eslabón parece menor | Cada uno añade riesgo y retraso |

## ❓ Preguntas de comprobación

1. ¿Qué dos funciones tiene una custodia de valores y cuál se olvida?
2. ¿Por qué la tokenización hace asequible la cuenta segregada?
3. ¿Cómo puede una conciliación dos a dos ocultar una diferencia?
4. ¿De qué depende que el régimen protector de custodia aplique?
5. ¿Cuál es la pieza crítica de un plan de sustitución y por qué?

## 📥 Entregable

Guarda en `portfolio/parte-21/clase-09/`:

- la medición de independencia efectiva antes y después;
- el coste comparado de ómnibus y segregada;
- el procedimiento de conciliación a tres bandas con su responsable;
- el plan de sustitución con sus seis elementos.

## 🔗 Referencias cruzadas

- **Viene de:** clases 2, 3 y 5; Parte 20, clase 12.
- **Continúa en:** clases 14 y 15 de esta parte.
- **Se aplica en:** Parte 22, clases 9 y 10; Parte 23, clase 10.

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

- CPMI e IOSCO (2012). *Principles for Financial Market Infrastructures*. BIS. <https://www.bis.org/cpmi/publ/d101.htm>
- IOSCO (2023). *Policy Recommendations for Crypto and Digital Asset Markets*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- IOSCO (2004). *Recommendations for Securities Settlement Systems*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD176.pdf>
- Comisión para el Mercado Financiero. *Normativa sobre custodia y depósito de valores*. CMF. <https://www.cmfchile.cl/portal/principal/613/w3-channel.html>
- Verificación local: comprueba si el instrumento está calificado como valor en tu jurisdicción, qué régimen de custodia le aplica y si admite cuentas segregadas en un registro distribuido. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 08 · Entrega contra pago atómica](08-entrega-contra-pago-atomica.md) | [Parte 21](../README.md) · [Programa](../../../SYLLABUS.md) | [10 · El tramo de dinero →](10-el-tramo-de-dinero.md) |
<!-- gen:footer:end -->
