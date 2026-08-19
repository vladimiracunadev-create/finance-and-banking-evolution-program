<!-- meta
part: 8
class: 2
title: "Mercados e intermediarios"
level: intermedio
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 02 · Mercados e intermediarios

> [← 01 · Objetivos y perfil de riesgo](01-objetivos-y-perfil-de-riesgo.md) · [Índice de la parte](../README.md) · [03 · Acciones →](03-acciones.md)

**Parte 08 — Inversiones y mercados** · **Nivel:** Intermedio — requiere las partes anteriores · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Comprender la infraestructura por la que circula el dinero de las inversiones: quién emite, quién
intermedia, dónde se transa, quién custodia y quién supervisa. Saber dónde está tu dinero en cada
momento y qué protección tiene es la diferencia entre una inversión y una apuesta.

El perfil de la clase anterior dice qué se puede hacer. Esta dice a través de quién, y su punto crítico es dónde queda el dinero: la protección del inversionista depende mucho más de cómo están custodiados los activos que del instrumento que se compre.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** mercado primario y secundario, y qué ocurre en cada uno.
2. **Identificar** a cada actor de la cadena y su función.
3. **Explicar** el ciclo completo de una orden, desde el envío hasta la custodia.
4. **Evaluar** la protección que tienes en cada eslabón.
5. **Verificar** la autorización de un intermediario antes de operar.

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

Los cuatro primeros términos son la estructura del mercado y sus actores; los tres últimos, la infraestructura que protege. La **segregación de activos** es lo que decide qué pasa si el intermediario quiebra, y es la comprobación que hay que hacer antes de abrir cualquier cuenta.

| Concepto | Comprensión verificable |
|---|---|
| `mercado primario` | Emisión: el dinero va al emisor. Solo ocurre una vez por instrumento. |
| `mercado secundario` | Transacción entre inversionistas. El emisor no recibe nada. Aporta liquidez. |
| `intermediario` | Corredora o agente autorizado que ejecuta órdenes por cuenta de clientes. |
| `bolsa` | Mercado organizado con reglas de negociación y difusión de precios. |
| `custodio` | Entidad que mantiene los instrumentos a nombre del titular. Separado del intermediario. |
| `depósito central de valores` | Registro electrónico de la propiedad de los instrumentos. |
| `segregación de activos` | Los instrumentos del cliente no forman parte del patrimonio del intermediario. |

## 🧠 Modelo mental

Tu dinero pasa por **cinco manos** y en cada una tiene una protección distinta:

```text
tú → intermediario → bolsa → contraparte → custodio/depósito central
     ↑                                      ↑
   riesgo operacional                    aquí están tus instrumentos,
   y de conducta                         a tu nombre, segregados
```

La pregunta clave ante cualquier intermediario: **¿a nombre de quién quedan mis instrumentos?** Si
quedan a nombre del intermediario en una cuenta global sin identificación individual, tu protección
ante su quiebra es sustancialmente menor.

## 📖 Desarrollo

### 1. Primario y secundario

El mismo instrumento se compra de dos formas distintas y con consecuencias distintas. La tabla las separa.

| | Mercado primario | Mercado secundario |
|---|---|---|
| Qué ocurre | Emisión de instrumentos nuevos | Transacción de instrumentos existentes |
| Quién recibe el dinero | El emisor | El vendedor |
| Ejemplos | Colocación de acciones, emisión de bonos | Bolsa, mercado extrabursátil |
| Función económica | Financiamiento | Liquidez y formación de precios |
| Regulación | Prospecto, inscripción, información | Reglas de negociación, transparencia |

El mercado secundario **no financia a las empresas** y es indispensable para que el primario funcione:
nadie compraría una emisión si no pudiera venderla después. Esa es su función económica.

### 2. Los actores

Entre el inversionista y el instrumento hay varios intermediarios con funciones distintas. La tabla los recoge.

| Actor | Función | Qué NO hace |
|---|---|---|
| Emisor | Emite instrumentos para financiarse | No garantiza el precio secundario |
| Banco de inversión | Estructura y coloca la emisión | No garantiza el resultado de la inversión |
| Corredora / agente | Ejecuta órdenes por cuenta del cliente | No debería operar contra el cliente sin informarlo |
| Bolsa | Provee el mercado y difunde precios | No garantiza la solvencia de los participantes |
| Cámara de compensación | Se interpone entre las partes y garantiza la liquidación | No garantiza el valor del instrumento |
| Depósito central de valores | Registra la propiedad | No custodia dinero |
| Administradora de fondos | Gestiona carteras colectivas | No garantiza rentabilidad |
| Custodio | Mantiene los instrumentos segregados | No decide inversiones |
| Supervisor de valores | Autoriza, fiscaliza y sanciona | No garantiza tus inversiones |
| Clasificadora de riesgo | Opina sobre la capacidad de pago del emisor | No es una recomendación de compra |

Las dos últimas filas concentran malentendidos frecuentes: **el supervisor no protege del riesgo de
mercado** y **una clasificación AAA no significa que el instrumento sea una buena inversión al precio
actual**.

### 3. El ciclo de una orden

Una orden recorre varias etapas antes de quedar liquidada, y saberlo explica plazos y bloqueos. El esquema siguiente lo recorre.

```text
T+0  10:31  envías la orden (compra de 500 acciones a precio de mercado)
     10:31  el intermediario valida saldo y límites
     10:31  la orden entra al libro de la bolsa
     10:31  se calza con una orden de venta → HECHO
     10:32  recibes la confirmación con precio y comisión

T+0  cierre  la bolsa envía las operaciones a la cámara de compensación
T+1  la cámara neteea posiciones y determina obligaciones
T+2  LIQUIDACIÓN: el dinero sale de tu cuenta y las acciones entran a tu custodia
```

Puntos que importan:

```text
· entre T+0 y T+2 tienes un derecho, no el instrumento
· la cámara de compensación reduce el riesgo de contraparte al interponerse
· el ciclo T+2 se ha ido acortando en varios mercados: verifica el de tu jurisdicción
· si el intermediario quiebra entre T+0 y T+2, la operación sigue el procedimiento
  de la cámara, no queda a la deriva
```

### 4. Dónde está tu protección

La protección viene de varias fuentes y ninguna cubre todo. La tabla las separa con su alcance.

| Eslabón | Riesgo | Protección |
|---|---|---|
| Intermediario | Quiebra, fraude, error operacional | Segregación de activos; fondos de garantía acotados |
| Bolsa | Falla operativa | Reglas de contingencia y anulación |
| Cámara de compensación | Incumplimiento de un participante | Márgenes, fondo de garantía, cascada de recursos |
| Depósito central | Error de registro | Conciliaciones y auditoría |
| Emisor | Incumplimiento de pago | **Ninguna**: es riesgo de crédito, y es tuyo |
| Mercado | Caída de precios | **Ninguna**: es riesgo de mercado, y es tuyo |

Las dos últimas filas son las importantes: **la infraestructura protege contra fallas del sistema, no
contra pérdidas de inversión**. Un inversionista protegido por toda la cadena puede perder el 100 % de
su dinero si el emisor no paga o si el precio cae.

### 5. Verificar un intermediario

Antes de entregar dinero hay comprobaciones concretas y rápidas. Los pasos siguientes son esas comprobaciones.

```text
1. ¿está inscrito en el registro del supervisor de valores? (sitio oficial)
2. ¿tiene sanciones o procedimientos vigentes? (registro público)
3. ¿los instrumentos quedan a mi nombre en el depósito central?
4. ¿puedo verificar mi posición directamente en el depósito, sin pasar por el intermediario?
5. ¿qué fondo de garantía cubre y hasta qué monto?
6. ¿cómo se estructura su remuneración? ¿comisión, diferencial o retrocesión?
```

La pregunta 4 es la más discriminante: **poder verificar tu posición en el depósito central sin
intermediación** es la comprobación más directa de que tus instrumentos existen y están a tu nombre.
Varios fraudes documentados consistieron precisamente en posiciones que solo existían en los estados
de cuenta del intermediario.

La pregunta 6 revela conflictos de interés: si el intermediario cobra retrocesión del fondo que
recomienda, tiene incentivo a recomendar el que más le paga, no el mejor para el cliente.

## 🧮 Ejemplo guiado

**Situación.** Una persona quiere invertir 30 000 000 y compara tres alternativas de acceso al
mercado.

```text
A  corredora tradicional: comisión 0,45 % por operación, custodia 0,15 % anual
B  plataforma digital: comisión 0,12 %, custodia 0 %, "cero comisiones en algunos productos"
C  banco: comisión 0,60 %, custodia incluida, asesoría incluida
```

**Paso 1 — verifica la autorización de las tres.**

```text
A  inscrita en el registro, sin sanciones vigentes           ✔
B  inscrita, con una sanción por información al cliente en 2024  ⚠
C  inscrita, sin sanciones                                    ✔
```

**Paso 2 — pregunta dónde quedan los instrumentos.**

```text
A  a nombre del cliente en el depósito central, verificable directamente  ✔
B  en cuenta global del intermediario, con registro interno por cliente   ⚠
C  a nombre del cliente en el depósito central                            ✔
```

**La respuesta de B es material.** No es ilegal —muchas plataformas operan así— y significa que ante
una quiebra del intermediario, la separación de los activos del cliente depende de la calidad de sus
registros internos y del procedimiento concursal, no de un registro público.

**Paso 3 — analiza el modelo de negocio de B.**

```text
"cero comisiones" en algunos productos
¿de dónde viene su ingreso?
  · diferencial entre precio de compra y venta
  · pago por flujo de órdenes de terceros
  · retrocesión de los fondos que distribuye
  · intereses sobre el saldo en efectivo de los clientes
```

Ninguna de esas fuentes es ilegítima, y **todas crean incentivos que el cliente debe conocer**. Un
diferencial más amplio puede costar más que una comisión explícita.

**Paso 4 — calcula el costo total a 10 años (cartera de 30 000 000, 6 operaciones al año).**

```text
A  comisiones: 30 000 000 × 0,0045 × 6 × 10 / 10 (asumiendo rotación parcial) ≈ 810 000
   custodia: 30 000 000 × 0,0015 × 10 = 450 000  (sobre saldo creciente, aprox.)
   total ≈ 1 260 000

B  comisiones: ≈ 216 000
   diferencial estimado: 0,25 % por operación ≈ 450 000
   total ≈ 666 000

C  comisiones ≈ 1 080 000
   custodia: 0
   total ≈ 1 080 000
```

**Paso 5 — incorpora la dimensión que el costo no captura.**

| Criterio | A | B | C |
|---|---|---|---|
| Costo a 10 años | 1 260 000 | 666 000 | 1 080 000 |
| Instrumentos a nombre del cliente | Sí | No | Sí |
| Verificación independiente en depósito | Sí | No | Sí |
| Historial de sanciones | Limpio | Una sanción | Limpio |
| Transparencia del modelo de ingreso | Alta | Media | Alta |
| Asesoría | Opcional | No | Incluida |

**Paso 6 — decisión.**

```text
la diferencia de costo entre B y A es 594 000 en 10 años (2,0 % del capital inicial)

¿compensa esa diferencia el riesgo de custodia en cuenta global?
  para una cartera de 30 000 000: la respuesta razonable es NO
  para una cartera de 500 000 en aprendizaje: la respuesta puede ser SÍ

DECISIÓN: A, con verificación semestral de la posición directamente en el depósito central

y una regla permanente:
  cualquiera sea el intermediario, verificar la posición en el registro
  independiente al menos dos veces al año
```

**Interpreta:** la comparación por costo favorecía claramente a B. **La pregunta sobre dónde quedan
los instrumentos cambió la decisión**, y es una pregunta que casi nadie hace porque no sabe que
existe. Ese es el aporte de conocer la infraestructura.

## 🏦 Del cliente al banco

El cliente opera y el banco ejecuta, custodia y liquida. La tabla enfrenta las dos lecturas.

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| Segregación de activos | Obligación del intermediario | 12, clase 12 |
| Ciclo de liquidación | Gestión de riesgo de liquidación | 10, clase 7 |
| Cámara de compensación | Reducción del riesgo de contraparte | 10, clase 7 |
| Retrocesiones | Conflicto de interés a revelar | 12, clase 3 |
| Registro del supervisor | Verificación previa obligatoria | 3, clase 1 |

## 🧪 Práctica

El laboratorio pide verificar intermediarios reales y determinar dónde quedaría cada activo. La verificación de la custodia es la parte que decide.

En `labs/lab-01.md`, sección de infraestructura:

1. Mapea la cadena completa de una inversión tuya, nombrando cada actor.
2. Verifica en el registro oficial la autorización de dos intermediarios.
3. Determina dónde quedan tus instrumentos y si puedes verificarlo de forma independiente.
4. Calcula el costo total a 10 años de tres alternativas de acceso al mercado.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen problemas que aparecen cuando el intermediario falla. Las causas están casi siempre en la custodia y no en el instrumento.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se compara solo por comisión | Diferenciales y retrocesiones ignorados | Calcula el costo total, incluidos los implícitos. |
| Se supone que el supervisor garantiza la inversión | Función mal entendida | El supervisor no cubre el riesgo de mercado ni de crédito. |
| No se sabe dónde están los instrumentos | Pregunta no formulada | Exige saber a nombre de quién quedan. |
| Se confía en el estado de cuenta del intermediario | Sin verificación independiente | Verifica en el depósito central. |
| Se interpreta una clasificación como recomendación | Confusión de propósito | Es una opinión sobre capacidad de pago, no sobre precio. |
| Se opera con un intermediario no inscrito | Verificación omitida | Consulta el registro oficial antes de transferir. |

## ❓ Preguntas de comprobación

1. ¿Qué diferencia hay entre mercado primario y secundario y por qué ambos son necesarios?
2. Describe el ciclo de una orden desde el envío hasta la custodia.
3. ¿Qué protege la infraestructura del mercado y qué no protege?
4. ¿Cuál es la pregunta más discriminante para evaluar un intermediario?
5. ¿Qué conflictos de interés puede tener un intermediario "sin comisiones"?

## 📥 Entregable

Guarda en `portfolio/parte-08/clase-02/`:

- el mapa de la cadena completa de una inversión propia;
- la verificación en el registro oficial de dos intermediarios, con captura;
- la determinación de dónde quedan tus instrumentos y su verificación independiente;
- la comparación de costo total a 10 años de tres alternativas con su decisión justificada.

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

- Bodie, Z., Kane, A. y Marcus, A. (2023). *Investments* (13.ª ed.). McGraw-Hill. Capítulos 3 y 4: mercados, intermediarios y mecánica de la negociación.
- IOSCO (2017). *Objectives and Principles of Securities Regulation*. Organización Internacional de Comisiones de Valores. Funciones del supervisor de valores y protección del inversionista. <https://www.iosco.org/>
- CPMI-IOSCO (2012). *Principles for Financial Market Infrastructures*. BIS. Cámaras de compensación y depósitos centrales. <https://www.bis.org/cpmi/publ/d101.htm>
- Harris, L. (2003). *Trading and Exchanges: Market Microstructure for Practitioners*. Oxford University Press. Funcionamiento del mercado secundario.
- IOSCO (2021). *Retail Market Conduct Task Force Report*. Modelos de ingreso de plataformas digitales y conflictos de interés.
- Verificación local: consulta el registro de intermediarios de valores del supervisor de tu país, el depósito central de valores y el fondo de garantía aplicable.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 01 · Objetivos y perfil de riesgo](01-objetivos-y-perfil-de-riesgo.md) | [Parte 08](../README.md) · [Programa](../../../SYLLABUS.md) | [03 · Acciones →](03-acciones.md) |
<!-- gen:footer:end -->
