<!-- meta
part: 21
class: 2
title: "El registro de referencia"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [chile, union-europea, internacional]
regulatory_topics: [registro-de-valores, conciliacion, infraestructura]
regulation_last_verified: 2026-08-20
regulatory_status: vigente
primary_authorities: [CPMI, IOSCO, CMF]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 02 · El registro de referencia

> [← 01 · Qué es y qué no es tokenizar](01-que-es-y-que-no-es-tokenizar.md) · [Índice de la parte](../README.md) · [03 · Derechos económicos y políticos del tenedor →](03-derechos-economicos-y-politicos-del-tenedor.md)

**Parte 21 — Tokenización, FX on-chain y mercados programables** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Responder por escrito la pregunta que decide si un proyecto de tokenización
existe: **cuando el token y el registro oficial dicen cosas distintas, ¿cuál
prevalece?** Y diseñar el procedimiento para cuando ocurra, porque ocurrirá.

La clase anterior mostró que el beneficio depende de dónde viva el derecho. Esta desarrolla esa idea y la convierte en regla de diseño: en todo momento un derecho tiene un solo registro que manda.

## 📚 Objetivos

Al finalizar podrás:

1. **Identificar** el registro de referencia de un instrumento y su fundamento
   jurídico.
2. **Enumerar** las causas por las que dos registros divergen.
3. **Diseñar** un procedimiento de conciliación con detección, congelación y
   resolución.
4. **Calcular** el coste de mantener dos registros alineados.
5. **Explicar** por qué un espejo nunca permite liquidación atómica.

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

Los cuatro primeros términos son el registro y su patología; los cuatro siguientes, los mecanismos que la evitan. El **bloqueo de origen** es la solución estructural: mientras el activo está anotado en un registro, se inmoviliza en el otro, y así nunca hay dos versiones activas del mismo derecho.

| Concepto | Comprensión verificable |
|---|---|
| `registro de referencia` | Aquel cuya versión prevalece en un conflicto |
| `espejo` | Representación que sigue a otro registro sin decidir |
| `divergencia` | Estado en que ambos registros afirman cosas distintas |
| `conciliación` | Proceso periódico que compara y corrige |
| `congelación` | Suspensión de movimientos mientras se resuelve |
| `ventana de divergencia` | Tiempo entre que aparece y se detecta |
| `autoridad de resolución` | Quien decide cuál versión es la correcta |
| `bloqueo de origen` | Inmovilizar en un registro lo emitido en el otro |

## 🧠 Modelo mental

El modelo mental es una regla simple: en todo momento un derecho tiene un solo registro que manda. Cuando dos registros pueden modificarse a la vez, la divergencia no es un fallo sino una certeza estadística.

```text
TRES CONFIGURACIONES POSIBLES

  A · EL REGISTRO OFICIAL MANDA
      el token es un espejo
      · toda transferencia en el token debe
        reflejarse en el oficial para valer
      · la atomicidad es IMPOSIBLE: no se
        puede entregar de forma atómica algo
        cuya titularidad decide otro
      · hace falta conciliación permanente

  B · EL TOKEN MANDA
      el registro oficial no existe, o se
      limita a reconocerlo
      · exige una norma que lo permita
      · la atomicidad es alcanzable
      · el riesgo se concentra en el registro

  C · NO ESTÁ DECIDIDO
      · es el estado real de muchos proyectos
      · y significa que, ante un conflicto,
        lo decidirá un tribunal, tarde y caro

LA CONFIGURACIÓN C NO ES UNA OPCIÓN:
ES LA AUSENCIA DE UNA DECISIÓN.
```

## 📖 Desarrollo

### 1. Por qué divergen dos registros

Cuando existen dos registros del mismo saldo, divergen; la pregunta es por qué
y con qué frecuencia. El bloque enumera las causas observadas ordenadas por lo
habitual que son.

```text
CAUSAS OBSERVADAS, POR FRECUENCIA

  1 FALLO DE PROPAGACIÓN
      la transferencia se registra en uno
      y el mensaje al otro se pierde

  2 ORDEN DISTINTO
      dos transferencias del mismo saldo
      llegan en orden distinto a cada registro

  3 EVENTO CORPORATIVO
      un canje, una amortización parcial o un
      embargo se aplica en uno y no en el otro

  4 DECISIÓN JUDICIAL
      un tribunal ordena una transferencia en
      el registro oficial; el token no lo sabe

  5 ERROR OPERATIVO
      una corrección manual en un solo lado

  6 ATAQUE
      alguien transfiere en el registro más débil

LA 3 Y LA 4 SON LAS QUE NINGUNA
AUTOMATIZACIÓN RESUELVE, PORQUE
VIENEN DE FUERA DEL SISTEMA.
```

### 2. El procedimiento en cuatro tiempos

Resolver una divergencia exige un procedimiento fijado de antemano, porque
improvisar mientras hay saldos en duda agrava el problema. El bloque lo
estructura en cuatro tiempos.

```text
1 DETECCIÓN
    comparación periódica de saldos por titular
    · frecuencia: la que acote la ventana
    · alcance: todos los saldos, no una muestra

2 CONGELACIÓN
    al detectar divergencia, se suspenden
    los movimientos del saldo afectado
    EN AMBOS REGISTROS
    · congelar solo uno agrava el problema

3 RESOLUCIÓN
    la autoridad designada determina la versión
    correcta con la evidencia
    · y hay que decir QUIÉN es, antes

4 REPARACIÓN
    se corrige el registro equivocado
    y se compensa a quien haya sufrido daño
    · nunca se «revierte» al otro:
      se compensa (Parte 19, clase 13)
```

### 3. La ventana de divergencia

El daño de una divergencia depende sobre todo del tiempo que tarda en
detectarse. El bloque relaciona la frecuencia de conciliación con la ventana
resultante y fija la regla de diseño que la acota.

```text
ES EL TIEMPO ENTRE QUE APARECE Y SE DETECTA

  con conciliación diaria:      hasta 24 horas
  con conciliación horaria:     hasta 60 minutos
  con conciliación en línea:    segundos

¿QUÉ PASA DURANTE LA VENTANA?
  · un titular puede transferir en uno de los
    registros un saldo que en el otro ya no tiene
  · si en ese tiempo se liquida contra dinero,
    el dinero se movió contra un activo dudoso

REGLA DE DISEÑO
  la ventana debe ser MENOR que el tiempo
  mínimo entre dos transferencias del mismo
  saldo; si no lo es, la conciliación no
  protege: solo documenta el daño
```

### 4. Por qué un espejo no permite atomicidad

Un registro espejo no puede dar entrega contra pago atómica, y conviene ver
por qué antes de que alguien lo prometa. El bloque lo deduce de la definición
de atomicidad.

```text
ATOMICIDAD = los dos movimientos ocurren
             juntos o no ocurre ninguno

EN UN ESPEJO
  el movimiento del valor solo es válido
  cuando lo confirma el registro oficial

  → hay un intervalo en que el dinero se movió
    y el valor está «pendiente de confirmar»
  → ese intervalo ES el riesgo de principal
    que la atomicidad pretendía eliminar

CONSECUENCIA PRÁCTICA
  un proyecto que promete entrega contra pago
  atómica y mantiene el registro oficial
  como referencia está prometiendo algo
  que su propia arquitectura impide

CÓMO DETECTARLO EN UNA PROPUESTA
  busca la frase «se refleja en el depositario
  central». Si está, no hay atomicidad.
```

### 5. La configuración híbrida que sí funciona

Existe una configuración que sí resuelve el problema: en vez de duplicar el
saldo, se inmoviliza en un registro mientras vive en el otro. El bloque
describe el mecanismo completo, de entrada y de salida.

```text
BLOQUEO DE ORIGEN

  el saldo se INMOVILIZA en el registro oficial
  y se emite su representación en el token

  mientras está inmovilizado:
    · el registro oficial no admite movimientos
    · el token es el único que decide
    · no hay dos versiones: hay una activa
      y una congelada

  al salir:
    · se destruye el token
    · se libera el saldo en el oficial

POR QUÉ FUNCIONA
  no hay divergencia posible, porque en cada
  momento solo un registro está operativo
  para ese saldo

COSTE
  entrar y salir tiene fricción y horario,
  y hay que medirlo
```

## 🧮 Ejemplo guiado

El ejemplo calcula la ventana de divergencia de un sistema con dos registros. Conviene usar la distribución real de operaciones y no la media: quien opera mucho es quien produce la divergencia.

**Situación.** Una plataforma tokeniza participaciones de un fondo. El registro
oficial es el del administrador. Hay que dimensionar la conciliación y decidir la
configuración.

```text
DATOS
  partícipes                              6 400
  transferencias mensuales                1 850
  suscripciones y reembolsos mensuales      920
  eventos corporativos al año                14
  coste de una conciliación completa        380
  coste de resolver una divergencia       4 200
  tasa de divergencia observada          0,12 % de las operaciones
```

**Paso 1 — calcula la frecuencia mínima de conciliación.**

```text
OPERACIONES MENSUALES
  1 850 + 920 = 2 770
  ≈ 92 al día, ≈ 4 por hora en horario

TIEMPO MÍNIMO ENTRE DOS OPERACIONES
DEL MISMO SALDO
  con 6 400 partícipes y 2 770 operaciones,
  la media es 0,43 operaciones por partícipe
  y mes

  pero la distribución no es uniforme:
  supuesto declarado, el 5 % más activo
  hace el 60 % de las operaciones

  ese 5 % son 320 partícipes con
  1 662 operaciones al mes
  → 5,2 operaciones por partícipe y mes
  → una cada 5,8 días
```

**Paso 2 — fija la ventana.**

```text
LA VENTANA DEBE SER MENOR QUE 5,8 DÍAS
PARA EL PARTÍCIPE ACTIVO MEDIO

  pero la media no protege: hay partícipes
  que operan dos veces en un día

  → CONCILIACIÓN DIARIA es el mínimo
  → CONCILIACIÓN HORARIA para el 5 % activo

DISEÑO PROPUESTO
  · completa: diaria
  · incremental sobre saldos con movimiento:
    cada hora
```

**Paso 3 — calcula el coste.**

```text
CONCILIACIÓN COMPLETA DIARIA
  380 × 22 días = 8 360 al mes

INCREMENTAL HORARIA
  supuesto: 15 % del coste completo
  380 × 15 % × 8 horas × 22 = 10 032 al mes

TOTAL = 18 392 al mes = 220 704 al año
```

**Paso 4 — calcula el coste de las divergencias.**

```text
DIVERGENCIAS ESPERADAS
  2 770 × 0,12 % = 3,3 al mes
  ≈ 40 al año

COSTE DE RESOLUCIÓN
  40 × 4 200 = 168 000 al año

MÁS LOS EVENTOS CORPORATIVOS
  14 al año, cada uno con riesgo de aplicarse
  en un solo registro
  supuesto: 20 % genera divergencia
  2,8 × 4 200 = 11 760

TOTAL DIVERGENCIAS ≈ 179 760 al año
```

**Paso 5 — suma y compara.**

```text
COSTE ANUAL DE LA CONFIGURACIÓN ESPEJO
  conciliación      220 704
  divergencias      179 760
  TOTAL             400 464

¿QUÉ APORTA EL TOKEN A CAMBIO?
  · transferencia entre partícipes sin
    pasar por el administrador
  · horario ampliado

¿CUÁNTO VALE ESO?
  supuesto: ahorro de 6 en el coste unitario
  de una transferencia
  1 850 × 6 × 12 = 133 200 al año

  400 464 de coste frente a 133 200 de ahorro
  → LA CONFIGURACIÓN ESPEJO PIERDE
    267 264 al año
```

**Paso 6 — evalúa el bloqueo de origen.**

```text
CONFIGURACIÓN CON BLOQUEO

  el partícipe inmoviliza su participación
  en el administrador y recibe el token
  · mientras esté en token, el administrador
    no admite movimientos de ese saldo
  · no hay conciliación: hay una transición

COSTE
  entradas y salidas: supuesto 620 al año
  coste unitario de entrada o salida: 45
  → 27 900 al año

  eventos corporativos: se aplican al saldo
  bloqueado y se propagan al token en una
  operación única y verificada
  14 × 900 = 12 600

TOTAL ≈ 40 500 al año

FRENTE A 400 464 DE LA CONFIGURACIÓN ESPEJO
```

**Paso 7 — decide y documenta la autoridad de resolución.**

```text
RECOMENDACIÓN: BLOQUEO DE ORIGEN

  y aun así hay que designar la autoridad
  de resolución, porque el bloqueo reduce
  la divergencia pero no la elimina:
  una orden judicial sobre un saldo
  bloqueado tiene que poder ejecutarse

AUTORIDAD DESIGNADA
  el administrador del fondo, con obligación
  de comunicar al operador del registro
  en un plazo máximo de 2 horas hábiles

PROCEDIMIENTO
  1 el administrador congela el saldo bloqueado
  2 comunica al operador del registro
  3 el operador congela el token
  4 se resuelve en el registro oficial
  5 se destruye o reemite el token según
    el resultado
  6 se compensa a quien haya sufrido daño

Y ESTO SE ESCRIBE ANTES DE EMITIR,
no cuando llega el primer embargo.
```

**Interpreta:** la configuración espejo perdía 267 000 al año antes de contar
ningún beneficio, y **la conciliación no era el problema: era el síntoma de no
haber respondido quién manda**. El bloqueo de origen elimina la divergencia
estructural por 40 500 al año, y aun así exige designar una autoridad de
resolución para los casos que vienen de fuera del sistema.

## 🧭 Perspectivas

El registro de referencia afecta a cada participante de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un saldo en dos sitios | A cuál mira |
| Emisor | Un registro adicional que mantener | Qué configuración elige |
| Administrador | Órdenes que llegan por dos vías | Cómo las prioriza |
| Infraestructura | Un registro paralelo | Si acepta el bloqueo |
| Custodio | Un activo bloqueado y otro activo | Cómo lo refleja |
| Banco | Un colateral con titularidad dudosa | Si lo acepta en garantía |
| Supervisor | Dos registros sin autoridad designada | Qué exige antes de autorizar |
| Auditor | Diferencias de conciliación | Qué muestrea |
| Juzgado | Una orden que ejecutar | Sobre qué registro actúa |
| Sociedad | Titularidad menos clara | Qué certeza exige |

## 🏦 Del cliente al banco

El cliente ve un saldo y el banco sabe qué registro manda en él. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Mi saldo aparece en la aplicación» | Puede diferir del registro oficial | 21, clase 2 |
| «La transferencia fue instantánea» | Pendiente de reflejarse en el oficial | 21, clase 2 |
| «Es atómico» | Con un espejo, no puede serlo | 21, clase 2 |

## ⚖️ Riesgos y controles

Los riesgos son de divergencia y de autoridad no definida. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Configuración no decidida | Un tribunal decide tarde y caro | Respuesta por escrito antes de emitir |
| Ventana de divergencia larga | Se transfiere un saldo inexistente | Frecuencia menor que el intervalo entre operaciones |
| Congelar un solo registro | Se agrava la divergencia | Congelación simultánea en ambos |
| Evento corporativo desalineado | Cupón pagado dos veces o ninguna | Aplicación única sobre el saldo bloqueado |
| Sin autoridad de resolución | Nadie decide | Designarla con plazo de actuación |
| Reversión en vez de compensación | Se altera el registro correcto | Compensar, no revertir |

## 🧪 Práctica

El laboratorio pide decidir el registro de referencia de cada dato y calcular la ventana. El bloqueo de origen es la corrección que se evalúa.

En [`labs/lab-01.md`](../labs/lab-01.md):

1. Simula dos registros y provoca las seis causas de divergencia.
2. Implementa detección, congelación simultánea y resolución.
3. Calcula la ventana de divergencia y compárala con el intervalo real.
4. Mide el coste anual de la configuración espejo y del bloqueo de origen.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen divergencias entre registros. La causa es la ausencia de bloqueo de origen.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| No decidir quién manda | Se pospone lo jurídico | Es la decisión que define el proyecto |
| Prometer atomicidad con espejo | Se copia del material comercial | La arquitectura lo impide |
| Conciliación por muestreo | Es más barata | Una divergencia no vista es una pérdida |
| Congelar solo el token | Es el registro que se controla | Hay que congelar los dos |
| Olvidar los eventos corporativos | No están en el piloto | Son la causa que ninguna automatización cubre |
| Revertir el registro correcto | Parece la corrección natural | Se compensa al perjudicado |

## ❓ Preguntas de comprobación

1. ¿Cuáles son las tres configuraciones posibles y por qué la tercera no lo es?
2. Enumera las seis causas de divergencia y di cuáles vienen de fuera.
3. ¿Cómo se fija la frecuencia de conciliación?
4. ¿Por qué un espejo impide la liquidación atómica?
5. ¿Qué elimina el bloqueo de origen y qué no elimina?

## 📥 Entregable

Guarda en `portfolio/parte-21/clase-02/`:

- la configuración elegida con su fundamento jurídico;
- el cálculo de la ventana de divergencia frente al intervalo real;
- el coste anual de conciliación y de resolución;
- el procedimiento en cuatro tiempos con la autoridad designada.

## 🔗 Referencias cruzadas

- **Viene de:** clase 1; Parte 19, clase 13.
- **Continúa en:** clases 5, 8 y 9 de esta parte.
- **Se aplica en:** Parte 22, clase 10; Parte 23, clases 4 y 7.

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

- CPMI e IOSCO (2012). *Principles for Financial Market Infrastructures*. BIS. Exigencia de un registro único y firme de titularidad. <https://www.bis.org/cpmi/publ/d101.htm>
- Committee on Payments and Market Infrastructures (2024). *Tokenisation in the context of money and other assets: concepts and implications for central banks*. BIS. Relación entre el registro tokenizado y el registro oficial. <https://www.bis.org/cpmi/publ/d225.htm>
- Diario Oficial de la Unión Europea (2022). *Reglamento (UE) 2022/858 sobre un régimen piloto de infraestructuras del mercado basadas en la tecnología de registro descentralizado*. EUR-Lex. Excepciones que el régimen piloto permite y sus límites. <https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32022R0858>
- Comisión para el Mercado Financiero. *Normativa sobre custodia y depósito de valores*. CMF. Régimen chileno del depósito y registro de valores. <https://www.cmfchile.cl/portal/principal/613/w3-channel.html>
- Verificación local: comprueba qué exige tu jurisdicción para que una anotación en un registro distribuido produzca efectos frente a terceros y quién resuelve un conflicto entre registros. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-20.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 01 · Qué es y qué no es tokenizar](01-que-es-y-que-no-es-tokenizar.md) | [Parte 21](../README.md) · [Programa](../../../SYLLABUS.md) | [03 · Derechos económicos y políticos del tenedor →](03-derechos-economicos-y-politicos-del-tenedor.md) |
<!-- gen:footer:end -->
