<!-- meta
part: 20
class: 10
title: "Monedas digitales de banco central"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [chile, internacional]
regulatory_topics: [cbdc, politica-monetaria, inclusion-financiera]
regulation_last_verified: 2026-08-06
regulatory_status: en-desarrollo
primary_authorities: [BIS, BCCh, CPMI]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 10 · Monedas digitales de banco central

> [← 09 · Dinero electrónico: el régimen que ya existía](09-dinero-electronico-el-regimen-que-ya-existia.md) · [Índice de la parte](../README.md) · [11 · Dinero programable y sus límites →](11-dinero-programable-y-sus-limites.md)

**Parte 20 — Activos digitales, stablecoins y dinero programable** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Analizar el pasivo del banco central en formato digital: **qué problema resuelve
que el efectivo o las reservas no resuelvan ya**, y qué efecto tiene sobre los
depósitos bancarios, que son la fuente del crédito.

Las clases anteriores tratan dinero privado. Esta trata el público en formato digital, y su análisis se concentra en los cuatro parámetros de diseño que deciden si la banca comercial pierde o no sus depósitos.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** una CBDC mayorista de una minorista y qué problema aborda cada
   una.
2. **Explicar** el modelo de dos niveles y por qué es la opción dominante.
3. **Calcular** el efecto de una migración de depósitos sobre la capacidad de
   crédito.
4. **Evaluar** los mecanismos que limitan esa migración y su coste.
5. **Analizar** el compromiso entre privacidad, trazabilidad e inclusión.

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

Los cuatro primeros términos son los tipos y su distribución; los cuatro siguientes, los parámetros de diseño y sus efectos. El **límite de tenencia** es el parámetro que decide si hay desintermediación: sin él, en una crisis los depósitos migrarían al banco central en horas.

| Concepto | Comprensión verificable |
|---|---|
| `CBDC` | Pasivo del banco central en forma digital |
| `mayorista` | Para entidades con cuenta en el banco central |
| `minorista` | Para el público general |
| `modelo de dos niveles` | El banco central emite; los intermediarios distribuyen |
| `desintermediación` | Salida de depósitos hacia el banco central |
| `límite de tenencia` | Tope al saldo por persona |
| `remuneración escalonada` | Interés distinto por tramo de saldo |
| `privacidad por diseño` | Datos mínimos y separación de funciones |

## 🧠 Modelo mental

El modelo mental es una competencia por el pasivo bancario. Si el público puede tener dinero de banco central directamente, el depósito pierde su ventaja de seguridad, y los parámetros de diseño existen para acotar ese efecto.

```text
QUÉ ES Y QUÉ NO ES

  UNA CBDC MINORISTA ES
    efectivo en forma digital:
    un pasivo del banco central que
    el público puede tener directamente

  NO ES
    · una criptomoneda: hay emisor y es soberano
    · una stablecoin: no hay reserva, ES la reserva
    · un depósito: no hay banco de por medio
    · una cuenta en el banco central para todos,
      si se diseña en dos niveles

LA PREGUNTA QUE ORDENA EL DEBATE
  ¿QUÉ PROBLEMA RESUELVE
   QUE EL EFECTIVO Y LAS TRANSFERENCIAS
   INMEDIATAS NO RESUELVAN YA?

Si la respuesta no es concreta,
el proyecto tiene un problema de diseño
antes que de tecnología.
```

## 📖 Desarrollo

### 1. Mayorista y minorista

| Aspecto | Mayorista | Minorista |
|---|---|---|
| Quién la tiene | Bancos y entidades autorizadas | Público general |
| Qué sustituye | Reservas, con más funcionalidad | Efectivo |
| Problema que aborda | Liquidación atómica y transfronteriza | Acceso, resiliencia, competencia |
| Riesgo de desintermediación | Ninguno | Central |
| Complejidad de privacidad | Baja | Alta |
| Estado habitual | Pruebas avanzadas | Estudio y pilotos |

### 2. El modelo de dos niveles

Casi todos los diseños en estudio reparten el trabajo en dos niveles, y las
razones son prácticas antes que doctrinales. El bloque describe qué hace cada
nivel y por qué esta arquitectura se ha impuesto.

```text
NIVEL 1 · BANCO CENTRAL
  emite, liquida y mantiene el registro
  del pasivo

NIVEL 2 · INTERMEDIARIOS
  distribuyen, identifican al cliente,
  atienden, cumplen las obligaciones
  de prevención y dan el servicio

POR QUÉ ES LA OPCIÓN DOMINANTE
  · el banco central no quiere ni debe
    hacer atención al cliente para millones
  · la identificación y el cumplimiento
    ya están en los intermediarios
  · preserva el papel del sector privado
    en la innovación

RIESGO DEL MODELO
  si el intermediario quiebra, ¿qué pasa
  con el saldo del cliente?
  → debe ser un pasivo del banco central
    en todo momento, no del intermediario
```

### 3. Desintermediación

El riesgo central de una moneda digital minorista no es tecnológico: es que
compita con el depósito bancario. El bloque plantea el problema en calma y en
crisis, y recuerda de dónde sale el crédito.

```text
EL RIESGO CENTRAL DE UNA CBDC MINORISTA

  si el público puede tener un pasivo
  del banco central sin riesgo,
  ¿por qué dejaría el dinero en un banco?

  EN CALMA  por comodidad y por el interés
  EN CRISIS por nada: correría al banco central

  → LA CBDC PUEDE CONVERTIRSE
    EN EL ACELERADOR DE CORRIDAS
    MÁS EFICIENTE JAMÁS CONSTRUIDO

Y EL DEPÓSITO ES LA FUENTE DEL CRÉDITO:
menos depósitos, menos crédito,
o crédito financiado más caro
```

### 4. Los límites y su coste

Los límites existen para contener la desintermediación, y cada uno tiene su
propio coste. El bloque describe los dos mecanismos habituales con el problema
que ninguno resuelve del todo.

```text
LÍMITE DE TENENCIA
  tope de saldo por persona
  · simple y comprensible
  · el excedente se barre a la cuenta bancaria
  · problema: en crisis, el límite se llena
    de inmediato y el resto corre igual

REMUNERACIÓN ESCALONADA
  el primer tramo sin interés,
  el excedente con interés negativo
  · desincentiva acumular
  · problema: es difícil de explicar
    y políticamente costoso

LÍMITE POR OPERACIÓN
  · no impide acumular con muchas operaciones

BARRIDO AUTOMÁTICO
  todo excedente vuelve al banco cada noche
  · mantiene el depósito
  · problema: si el banco es el que preocupa,
    barrer hacia él no tranquiliza a nadie

NINGUNO ES GRATIS Y NINGUNO ES COMPLETO
```

### 5. Privacidad

La privacidad de una moneda digital se sitúa entre el efectivo y el depósito, y
dónde exactamente es una decisión que no toma la técnica. El bloque presenta
el compromiso y los diseños que lo suavizan.

```text
EL COMPROMISO REAL

  EFECTIVO           anónimo, sin registro
  DEPÓSITO           identificado, con registro
  CBDC               en algún punto entre ambos,
                     y ese punto es una DECISIÓN
                     POLÍTICA, no técnica

DISEÑOS QUE MITIGAN
  · el banco central ve importes, no identidades
  · el intermediario ve identidades, no el detalle
    de cada pago
  · anonimato por debajo de umbrales bajos,
    como el efectivo
  · separación criptográfica de las dos vistas

QUÉ NO SE PUEDE PROMETER
  anonimato completo con cumplimiento completo
  → hay que elegir dónde ponerse
    y decirlo con claridad
```

## 🧮 Ejemplo guiado

El ejemplo estima el efecto de una moneda digital sobre los depósitos según su límite de tenencia. Con dos límites distintos el efecto cambia de orden de magnitud.

**Situación.** Un banco central estudia una CBDC minorista con límite de
tenencia. Hay que estimar el efecto sobre el crédito del sistema bancario.

```text
DATOS DEL SISTEMA
  depósitos a la vista de hogares   96 000 000 000
  hogares con cuenta                     7 200 000
  depósito medio por hogar                  13 333
  crédito total del sistema        148 000 000 000
  ratio préstamos/depósitos                  92 %
  coste de los depósitos a la vista         0,60 %
  coste de financiación mayorista           3,90 %

DISEÑO PROPUESTO
  límite de tenencia por persona             2 000
```

**Paso 1 — calcula la migración máxima teórica.**

```text
SI TODOS LLENARAN EL LÍMITE

  7 200 000 × 2 000 = 14 400 000 000

  sobre 96 000 000 000 de depósitos
  = 15,0 % de los depósitos a la vista
```

**Paso 2 — ajusta por comportamiento.**

```text
NO TODOS LLENAN EL LÍMITE

  supuesto declarado:
    30 % no adopta                      0
    45 % mantiene un saldo medio de 400
    25 % llena el límite

  migración =
    7 200 000 × 45 % × 400  =  1 296 000 000
    7 200 000 × 25 % × 2 000 = 3 600 000 000
    TOTAL                    = 4 896 000 000

  = 5,1 % de los depósitos a la vista
```

**Paso 3 — traduce a capacidad de crédito.**

```text
CON UN RATIO PRÉSTAMOS/DEPÓSITOS DEL 92 %

  4 896 000 000 × 92 % = 4 504 320 000
  de crédito que hay que financiar de otro modo
```

**Paso 4 — calcula el coste de sustituir esa financiación.**

```text
DIFERENCIA DE COSTE
  3,90 % − 0,60 % = 3,30 puntos

COSTE ANUAL ADICIONAL
  4 896 000 000 × 3,30 % = 161 568 000

REPARTO POSIBLE
  · lo absorbe el margen del banco
  · se traslada al tipo del crédito
  · se reduce el volumen de crédito

SI SE TRASLADA ÍNTEGRO AL CRÉDITO
  161 568 000 / 148 000 000 000 = 0,109 puntos
  de encarecimiento medio

  → un efecto real pero moderado en calma
```

**Paso 5 — modela el escenario de tensión.**

```text
UN RUMOR SOBRE UN BANCO MEDIANO

  depósitos de ese banco              8 400 000 000
  clientes                                 620 000
  capacidad CBDC de sus clientes
    620 000 × 2 000 = 1 240 000 000

  EN UNA TARDE, ESE 14,8 % PUEDE SALIR
  · sin cola en la sucursal
  · sin límite de efectivo
  · sin horario

  COMPARACIÓN CON UNA CORRIDA CLÁSICA
    el efectivo tiene fricción física
    la transferencia a otro banco requiere
    que ese banco inspire confianza
    la CBDC no requiere confiar en nadie más

EL LÍMITE DE 2 000 NO EVITA LA CORRIDA:
LA ORDENA Y LE PONE UN TECHO
```

**Paso 6 — evalúa si el techo basta.**

```text
¿SOBREVIVE EL BANCO A PERDER EL 14,8 %
DE SUS DEPÓSITOS EN UNA TARDE?

  depende de su ratio de cobertura de liquidez
  supuesto: activos líquidos de alta calidad
  por 1 900 000 000

  salida de 1 240 000 000 → cubierta

  PERO la salida no se detiene ahí:
  quien llenó el límite de CBDC seguirá
  moviendo el resto a otro banco

  → EL LÍMITE RETRASA, NO CONTIENE
    y ese retraso vale: da tiempo a
    que el banco central actúe
```

**Paso 7 — formula la comparación obligatoria.**

```text
¿QUÉ PROBLEMA RESUELVE QUE OTRA COSA
NO RESUELVA YA?

  ACCESO                 lo resuelve la cuenta básica
  PAGOS INMEDIATOS       lo resuelve el sistema
                         de pagos inmediatos
  RESILIENCIA ANTE CAÍDA lo resuelve un modo
                         fuera de línea, y eso SÍ
                         es propio de una CBDC
  COMPETENCIA EN PAGOS   lo resuelve la
                         interoperabilidad obligatoria
  SOBERANÍA MONETARIA
  FRENTE A SUSTITUTOS    lo resuelve una CBDC,
                         y este SÍ es un argumento
                         que no tiene alternativa

CONCLUSIÓN HONESTA
  dos de cinco justificaciones resisten:
  el modo fuera de línea y la soberanía
  frente a sustitutos privados
```

**Interpreta:** el efecto sobre el crédito en calma es moderado y manejable; el
efecto en tensión no lo neutraliza ningún límite, solo lo retrasa. **Ese retraso
es el objetivo realista del diseño**, y presentarlo como prevención de corridas
sería falso.

## 🧭 Perspectivas

Una moneda digital de banco central afecta a cada participante de forma muy distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Dinero del banco central en el móvil | Cuánto deja en el banco |
| Comercio | Un cobro sin comisión de red | Si lo prefiere |
| Fintech | Un riel público | Qué construye encima |
| Banco | Depósitos que migran | Cómo financia el crédito |
| Banco central | Soberanía y política monetaria | Qué límites fija |
| Infraestructura | Un sistema nuevo que operar | Cómo se integra |
| Emisor privado | Un competidor con respaldo soberano | Si su producto sobrevive |
| Supervisor | Corridas más rápidas | Qué liquidez exige |
| Auditor | Trazabilidad nueva | Qué controles verifica |
| Sociedad | Privacidad de los pagos | Qué exige por ley |

## 🏦 Del cliente al banco

El ciudadano tendría dinero público y el banco comercial perdería su pasivo más barato. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Es más seguro que el banco» | Es cierto, y por eso migra el depósito | 20, clase 10 |
| «Tiene un tope de 2 000» | El tope retrasa la corrida, no la evita | 20, clase 10 |
| «¿Van a ver mis pagos?» | Depende del diseño, y es una decisión política | 20, clase 10 |

## ⚖️ Riesgos y controles

Los riesgos son de desintermediación y de privacidad. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Desintermediación estructural | Migración permanente de depósitos | Límite de tenencia y barrido |
| Corrida acelerada | Salida masiva en horas | Límite, más liquidez y facilidad del banco central |
| Saldo confundido con el intermediario | El cliente cree que es del banco | Titularidad clara del pasivo |
| Exclusión digital | Quien no tiene móvil queda fuera | Modo fuera de línea y soporte físico |
| Privacidad insuficiente | Trazabilidad total de los pagos | Separación de vistas y umbrales |
| Dependencia de un sistema único | Una caída deja al país sin pagos | Redundancia y modo degradado |

## 🧪 Práctica

El laboratorio pide estimar el efecto sobre los depósitos con distintos parámetros. El límite de tenencia es la variable dominante.

En [`labs/lab-01.md`](../labs/lab-01.md):

1. Clasifica una CBDC con la ficha de cinco preguntas de la clase 1.
2. Calcula la migración de depósitos y su efecto sobre el crédito.
3. Modela la salida en tensión con un límite de tenencia dado.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen análisis mal planteados. Las causas son confundir mayorista con minorista e ignorar los límites.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Llamarla criptomoneda | Se agrupa por el soporte | Tiene emisor soberano |
| Suponer que el límite evita corridas | Es el argumento cómodo | Retrasa; no contiene |
| Ignorar el efecto sobre el crédito | No se ve en el piloto | El depósito financia el crédito |
| Prometer anonimato y cumplimiento | Se quieren ambas cosas | Hay que elegir y decirlo |
| Justificarla por la inclusión sin más | Es la razón más presentable | Compara con la cuenta básica |
| Olvidar el modo fuera de línea | Es difícil de implementar | Es de las pocas ventajas exclusivas |

## ❓ Preguntas de comprobación

1. ¿Qué diferencia hay entre CBDC mayorista y minorista?
2. ¿Por qué el modelo de dos niveles es la opción dominante?
3. ¿Cómo se calcula el efecto de la migración sobre el crédito?
4. ¿Por qué un límite de tenencia no evita una corrida?
5. ¿Qué dos justificaciones resisten la comparación con las alternativas?

## 📥 Entregable

Guarda en `portfolio/parte-20/clase-10/`:

- el cálculo de migración de depósitos con supuestos declarados;
- el efecto sobre el coste y el volumen del crédito;
- el escenario de tensión con el techo de salida calculado;
- la comparación de las cinco justificaciones con sus alternativas.

## 🔗 Referencias cruzadas

- **Viene de:** clases 1, 8 y 9; Parte 14, clase 10.
- **Continúa en:** clase 11 de esta parte.
- **Se aplica en:** Parte 21, clase 11; Parte 22, clase 7; Parte 23, clase 5.

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

- Bank for International Settlements (2021). *Central bank digital currencies: financial stability implications*. BIS. Efectos sobre los depósitos bancarios y la intermediación. <https://www.bis.org/publ/othp42_fin_stab.htm>
- Committee on Payments and Market Infrastructures (2020). *Central bank digital currencies: foundational principles and core features*. BIS. Principios rectores del diseño que la clase evalúa. <https://www.bis.org/publ/othp33.htm>
- Banco Central de Chile (2022). *Emisión de moneda digital de banco central en Chile*. BCCh. Estado del análisis chileno sobre una moneda digital. <https://www.bcentral.cl/documents/33528/3060272/Informe_CBDC.pdf>
- Bank for International Settlements (2023). *Annual Economic Report, capítulo III*. BIS. Papel de la moneda digital mayorista en el libro unificado. <https://www.bis.org/publ/arpdf/ar2023e3.htm>
- Verificación local: comprueba el estado actual del proyecto de moneda digital en tu jurisdicción y qué decisiones de diseño se han publicado; este ámbito cambia con rapidez. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 09 · Dinero electrónico: el régimen que ya existía](09-dinero-electronico-el-regimen-que-ya-existia.md) | [Parte 20](../README.md) · [Programa](../../../SYLLABUS.md) | [11 · Dinero programable y sus límites →](11-dinero-programable-y-sus-limites.md) |
<!-- gen:footer:end -->
