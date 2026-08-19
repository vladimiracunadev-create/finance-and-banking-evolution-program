<!-- meta
part: 14
class: 3
title: "Banca abierta y APIs"
level: profesional
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 03 · Banca abierta y APIs

> [← 02 · Pagos digitales y dinero electrónico](02-pagos-digitales.md) · [Índice de la parte](../README.md) · [04 · Datos en un banco →](04-datos-en-un-banco.md)

**Parte 14 — Fintech, datos e inteligencia artificial** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Entender el cambio de propiedad de los datos financieros y sus consecuencias. La banca abierta parte de
un principio simple —**los datos de una cuenta pertenecen a su titular, no al banco**— y de él se
derivan la competencia, la interoperabilidad y un conjunto nuevo de riesgos.

El pago de la clase anterior se desagregó por infraestructura. Este eslabón se desagrega por norma: la banca abierta obliga al banco a compartir con terceros los datos de sus clientes, y con eso desmonta la barrera de entrada más antigua del sector, que era la información.

## 📚 Objetivos

Al finalizar podrás:

1. **Explicar** el fundamento de la banca abierta y sus modelos de implantación.
2. **Describir** la arquitectura técnica y de consentimiento.
3. **Identificar** los riesgos de seguridad, privacidad y responsabilidad.
4. **Evaluar** las oportunidades de negocio que abre para un banco.
5. **Distinguir** banca abierta de finanzas abiertas y de datos abiertos.

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

Los tres primeros términos son el mecanismo y su alcance; los cinco siguientes, los actores y las prácticas que sustituye. El **consentimiento** es la pieza que sostiene todo el modelo: sin él no hay acceso, y su diseño decide si el cliente entiende lo que autoriza.

| Concepto | Comprensión verificable |
|---|---|
| `interfaz de programación (API)` | Punto de acceso normalizado a datos o servicios. |
| `banca abierta` | Acceso de terceros autorizados a datos y pagos, con consentimiento. |
| `finanzas abiertas` | Extensión a seguros, pensiones, inversiones y crédito. |
| `proveedor de información` | Tercero que agrega datos de cuentas. |
| `proveedor de iniciación de pago` | Tercero que ordena pagos por cuenta del usuario. |
| `consentimiento` | Autorización explícita, específica y revocable del titular. |
| `raspado de pantalla` | Acceso mediante las credenciales del usuario. Práctica insegura. |
| `reciprocidad` | Que quien accede a datos ajenos también comparta los propios. |

## 🧠 Modelo mental

El modelo mental es un cambio de propietario del dato: la información de la cuenta deja de ser del banco y pasa a ser del cliente, que puede llevársela a donde quiera. Todo lo demás —las interfaces, el consentimiento, la responsabilidad— es la mecánica de ese cambio.

```text
LA PREGUNTA QUE ORIGINA TODO

  cuando un cliente hace una transferencia,
  ¿de quién es el dato de esa transferencia?

  RESPUESTA TRADICIONAL   del banco: está en sus sistemas
  RESPUESTA DE LA BANCA   del cliente: es información sobre él
  ABIERTA                 y el banco es su custodio

DE LA SEGUNDA RESPUESTA SE DERIVA TODO LO DEMÁS
  · el cliente puede autorizar a un tercero a verlos
  · el banco debe proveer un canal seguro para ello
  · el banco no puede cobrar por lo que no es suyo
  · la competencia deja de depender de retener información
```

## 📖 Desarrollo

### 1. Modelos de implantación

Los países han implantado la banca abierta de formas distintas, con resultados distintos. La tabla los compara.

| Modelo | Cómo se impone | Ventaja | Limitación |
|---|---|---|---|
| Regulatorio obligatorio | La norma exige APIs con estándar común | Cobertura universal, estándar único | Costo de cumplimiento |
| Guiado por el mercado | El sector define estándares | Flexibilidad | Cobertura desigual |
| Híbrido | Norma con principios, mercado con estándares | Equilibrio | Ambigüedad inicial |

El debate entre modelos se concentra en una cuestión que es política antes que
técnica.

```text
LA RECIPROCIDAD ES LA CUESTIÓN POLÍTICA CENTRAL

  si el banco debe abrir sus datos
  y una gran tecnológica que también presta servicios financieros
  no debe abrir los suyos,
  la regulación crea una asimetría competitiva

  las normas más recientes tienden a exigir
  reciprocidad a todo participante
```

### 2. Arquitectura

La arquitectura técnica tiene componentes definidos y estándares de seguridad propios. El esquema los recoge.

```text
COMPONENTES
  1. IDENTIFICACIÓN DEL TERCERO
     registro y certificado; solo entidades autorizadas
  2. AUTENTICACIÓN DEL USUARIO
     ocurre EN EL BANCO, nunca en el tercero
  3. CONSENTIMIENTO
     explícito, específico en alcance y plazo, revocable
  4. AUTORIZACIÓN
     token con permisos acotados y vencimiento
  5. ACCESO
     el tercero consulta datos o inicia pagos con el token
  6. REGISTRO
     el usuario ve y revoca sus consentimientos activos
```

Esa arquitectura existe para sustituir una práctica anterior, y conviene ver con detalle por qué aquella era inaceptable.

```text
POR QUÉ EL RASPADO DE PANTALLA ES INACEPTABLE
  el usuario entrega sus CREDENCIALES al tercero
  · el tercero puede hacer todo lo que el usuario puede
  · el banco no distingue al tercero del usuario
  · no hay alcance acotado ni revocación
  · si hay fraude, no se puede determinar responsabilidad
  · las credenciales quedan almacenadas en otro sistema

la banca abierta lo sustituye por un canal
donde el alcance es explícito y el acceso es trazable
```

### 3. Alcances típicos

El acceso se otorga por alcances acotados y no en bloque. La tabla los recoge.

| Alcance | Qué permite | Riesgo |
|---|---|---|
| Información de cuentas | Ver saldos y movimientos | Privacidad, perfilado |
| Confirmación de fondos | Verificar si hay saldo suficiente | Bajo |
| Iniciación de pago único | Ordenar un pago concreto | Fraude en la orden |
| Iniciación de pagos recurrentes | Órdenes periódicas | Cargos no deseados |
| Datos de productos y precios | Comparar ofertas | Ninguno relevante |
| Datos de crédito | Evaluar solvencia | Alto: discriminación, error |

Cualquiera de esos alcances requiere un consentimiento que identifique el
dato, el plazo y la finalidad.

```text
EL CONSENTIMIENTO DEBE SER ESPECÍFICO
  "acceso a mi información financiera" NO es consentimiento válido
  "acceso a los movimientos de la cuenta X
   de los últimos 12 meses, durante 90 días,
   con el fin de evaluar una solicitud de crédito"  SÍ lo es
```

### 4. Riesgos y responsabilidad

Cuando algo sale mal en una cadena de tres actores, hay que saber quién responde. La tabla lo recoge.

```text
PREGUNTA CENTRAL: SI ALGO SALE MAL, ¿QUIÉN RESPONDE?

  el usuario autorizó a un tercero
  el tercero ordenó un pago erróneo o fraudulento
  el banco lo ejecutó porque la autorización era válida

REGLA HABITUAL EN LAS NORMAS
  el banco reembolsa al usuario de inmediato
  y luego repite contra el tercero si le corresponde
  → el usuario no queda atrapado entre dos empresas
```

| Riesgo | Mitigante |
|---|---|
| Tercero no autorizado | Registro y verificación de certificado en cada llamada |
| Consentimiento excesivo | Alcance mínimo necesario; plazo acotado |
| Consentimiento olvidado | Panel de consentimientos activos y recordatorios |
| Uso secundario de los datos | Prohibición y auditoría del tercero |
| Concentración de agregadores | Riesgo sistémico de un solo punto |
| Disponibilidad de las APIs | Obligación de servicio y de rendimiento |

**El riesgo menos discutido es el de concentración de agregadores.** Si un puñado de empresas concentra
el acceso a los datos de casi todos los clientes de un país, esa concentración es sistémica: su
compromiso afectaría al sistema entero.

### 5. Oportunidades para el banco

La banca abierta también abre oportunidades al banco que la cumple bien. La tabla las recoge.

```text
EL BANCO NO ES SOLO UN OBLIGADO: TAMBIÉN PUEDE CONSUMIR

  como CONSUMIDOR de APIs de otros bancos:
    · ver la posición completa del cliente, no solo la suya
    · evaluar crédito con información de todas sus cuentas
    · ofrecer agregación y asesoría sobre el total
    · detectar que el cliente concentra su actividad
      en otro banco y actuar

  como PROVEEDOR de servicios sobre su infraestructura:
    · banca como servicio para terceros
    · verificación de identidad y de ingresos
    · iniciación de pagos para comercios
```

```text
LA VENTAJA COMPETITIVA SE DESPLAZA
  antes: retener la información del cliente
  ahora: usar mejor la información que todos tienen

  y el banco que consume APIs activamente
  tiene MÁS información que antes, no menos
```

## 🧮 Ejemplo guiado

El ejemplo diseña un consentimiento con alcance por finalidad. Conviene comparar con un consentimiento en bloque: el primero es más trabajo y es el único defendible.

**Situación.** Un banco define su estrategia de banca abierta ante la entrada en vigor de la norma.

```text
SITUACIÓN
  clientes                                    640 000
  de ellos, con el banco como principal       384 000  (60 %)
  con actividad relevante en otros bancos     256 000  (40 %)

  costo de cumplimiento estimado
    desarrollo de APIs                          2 800
    operación y disponibilidad anual              640
    gestión de consentimientos                    280
    seguridad y monitoreo                         420
    TOTAL: 2 800 inicial + 1 340 anuales
```

**Paso 1 — evalúa el escenario de cumplimiento mínimo.**

```text
CUMPLIR Y NADA MÁS
  costo: 2 800 + 1 340 anuales
  ingreso: 0

  RIESGO ADICIONAL
  los 384 000 clientes principales quedan expuestos:
  cualquier competidor puede ver su actividad completa
  con el consentimiento del cliente y hacer ofertas dirigidas

  fuga estimada de clientes principales: 2,5 % anual
  9 600 clientes × margen anual 0,096 = 922 anuales de pérdida

COSTO TOTAL DEL CUMPLIMIENTO MÍNIMO: 2 262 anuales
```

**Paso 2 — evalúa el consumo activo de APIs.**

```text
LOS 256 000 CLIENTES CON ACTIVIDAD EN OTROS BANCOS

  si el banco obtiene su consentimiento para ver esas cuentas:
    · conoce su ingreso real, no el que declara
    · conoce su endeudamiento total
    · conoce su capacidad de pago verificable
    · puede ofrecer consolidación de deuda con datos

  adopción esperada del consentimiento: 22 %  (56 320 clientes)
    (la adopción depende de que el servicio ofrecido
     tenga valor evidente para el cliente)
```

**Paso 3 — cuantifica el valor del consumo.**

```text
1. MEJOR EVALUACIÓN DE CRÉDITO
   sobre los 56 320 con datos completos:
   tasa de aprobación sube de 42 % a 58 %
   (se aprueban solicitudes que antes se rechazaban por falta
    de información, no por riesgo)
   solicitudes adicionales aprobadas: 56 320 × 31 % × 16 % = 2 793
   monto medio 3,2 → colocación adicional: 8 938
   margen neto de riesgo 6,4 %: 572 anuales

2. MEJOR DECISIÓN DE RECHAZO
   se detectan solicitantes con endeudamiento oculto
   rechazos adicionales: 1 240 solicitudes
   pérdida evitada: 1 240 × 3,2 × PD 11 % × LGD 62 % = 271 anuales

3. CONSOLIDACIÓN DE DEUDA
   clientes con deuda cara en otros bancos identificados: 18 400
   conversión: 12 % → 2 208 operaciones
   monto medio 4,6 → 10 157 de colocación
   margen 4,8 %: 488 anuales

4. RETENCIÓN
   se detecta al cliente que migra su actividad
   antes de que complete la migración
   retención adicional estimada: 3 400 clientes
   valor: 3 400 × 0,096 = 326 anuales

TOTAL DEL CONSUMO ACTIVO: 1 657 anuales
```

**Paso 4 — evalúa la provisión de servicios sobre la infraestructura.**

```text
VERIFICACIÓN DE INGRESOS COMO SERVICIO
  el banco puede confirmar a un tercero, con consentimiento
  del cliente, su ingreso verificado
  demanda estimada: arrendadores, empleadores, otros prestamistas
  operaciones anuales estimadas: 180 000
  precio 0,004 → 720 anuales
  costo marginal: casi cero (la API ya existe)

INICIACIÓN DE PAGOS PARA COMERCIOS
  el banco actúa como iniciador para comercios
  que quieren cobrar sin tarjeta
  volumen estimado: 12 M de operaciones
  comisión 0,0012 → 14,4 anuales
  margen bajo, pero fideliza al comercio

TOTAL PROVISIÓN: 734 anuales
```

**Paso 5 — consolida.**

```text
                                    costo    ingreso
cumplimiento obligatorio           −1 340         0
pérdida por exposición               −922         0
consumo activo de APIs               −380     1 657
provisión de servicios               −210       734
inversión adicional (amortizada)     −390         0
TOTAL ANUAL                        −3 242     2 391

RESULTADO NETO: −851 anuales
```

**Paso 6 — reevalúa: ¿está bien planteado?**

```text
EL RESULTADO NEGATIVO INCLUYE EL COSTO OBLIGATORIO
que se paga con o sin estrategia

  cumplimiento obligatorio: −1 340  (inevitable)
  pérdida por exposición:     −922  (inevitable sin acción)
  SUBTOTAL INEVITABLE:      −2 262

  estrategia activa:
    costo:    −980
    ingreso: +2 391
    NETO:    +1 411

la estrategia activa aporta 1 411 anuales
sobre una obligación que cuesta 2 262 de todos modos
```

**Paso 7 — evalúa el efecto sobre la pérdida por exposición.**

```text
¿LA ESTRATEGIA ACTIVA REDUCE LA FUGA?

  el punto 4 del consumo (retención) ya lo considera: 326

  ADEMÁS
  un banco que ofrece visión consolidada de todas
  las cuentas del cliente se convierte en su interfaz principal
  → la fuga de principales baja de 2,5 % a 1,6 %
  pérdida: 922 → 590
  MEJORA ADICIONAL: 332 anuales

RESULTADO CONSOLIDADO
  inevitable: −1 340 − 590 = −1 930
  estrategia: +1 411 + 332 = +1 743
  NETO: −187 anuales

frente a −2 262 del cumplimiento mínimo
DIFERENCIA A FAVOR DE LA ESTRATEGIA ACTIVA: 2 075 anuales
```

**Paso 8 — define las condiciones de ejecución.**

```text
1. ADOPCIÓN DEL CONSENTIMIENTO
   la estimación del 22 % depende de que el servicio
   ofrecido tenga valor EVIDENTE para el cliente
   → la agregación por sí sola no lo tiene
   → el valor está en: "vemos que pagas 34 % en otro banco
     y podemos ofrecerte 19 %"

2. PRIVACIDAD Y CONFIANZA
   pedir acceso a las cuentas de otro banco exige confianza
   · consentimiento con alcance mínimo y plazo corto
   · uso exclusivo para el fin declarado
   · panel de control visible y revocación en un clic
   · si el cliente percibe uso indebido, la adopción se hunde

3. RECIPROCIDAD
   el banco debe cumplir con la misma calidad de servicio
   que exige a otros: disponibilidad, latencia, completitud

4. NO CONVERTIR EL DATO EN EXCLUSIÓN
   ver el endeudamiento total permite rechazar mejor
   y también permite prestar a quien antes se rechazaba
   por falta de información
   → medir ambos efectos, no solo el rechazo
```

**Interpreta:** la banca abierta se presenta habitualmente como una amenaza para los bancos
establecidos, y el análisis muestra que **la amenaza es real solo para quien la cumple pasivamente**. El
banco que consume activamente termina con más información sobre sus clientes que antes de la norma. El
punto 4 de las condiciones es el que decide si el resultado es socialmente bueno: la misma información
que permite rechazar mejor permite **aprobar a quien antes se rechazaba por desconocimiento**.

## 🏦 Del cliente al banco

El cliente comparte sus datos y el banco pierde exclusividad sobre la información que lo protegía. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Puedo ver todas mis cuentas en una app» | Agregación con consentimiento | 14, clase 3 |
| «Me pidieron mis claves para agregar cuentas» | Raspado de pantalla: rechazar | 4, clase 3 |
| «Autoricé una vez y siguen accediendo» | Consentimiento sin plazo | 14, clase 3 |
| «Me ofrecieron mejor tasa sabiendo mi deuda» | Consumo activo de datos | 14, clase 3 |
| «El banco me reembolsó y luego reclamó al tercero» | Regla de responsabilidad | 12, clase 9 |

## 🧪 Práctica

El laboratorio pide diseñar los alcances de un consentimiento y determinar responsabilidades ante un incidente. La cadena de responsabilidad es lo que se evalúa.

En `labs/lab-02.md`:

1. Diseña el flujo de consentimiento para tres casos de uso distintos.
2. Redacta un consentimiento específico y compáralo con uno genérico.
3. Evalúa el efecto económico del consumo activo de APIs.
4. Identifica los riesgos de un esquema de banca abierta y sus mitigantes.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen problemas de banca abierta. Las causas son consentimientos demasiado amplios y responsabilidades no repartidas.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se cumple pasivamente | Solo costo, sin ingreso | Consume APIs activamente. |
| Consentimiento genérico | No es válido | Alcance, fin y plazo específicos. |
| Se acepta raspado de pantalla | Credenciales compartidas | Canal con alcance acotado. |
| El usuario queda entre dos empresas | Responsabilidad no definida | El banco reembolsa y repite. |
| Concentración de agregadores no evaluada | Riesgo sistémico | Mídela y repórtala. |
| Los datos solo se usan para rechazar | Se pierde el efecto inclusivo | Mide también las aprobaciones nuevas. |

## ❓ Preguntas de comprobación

1. ¿Qué principio origina la banca abierta y qué se deriva de él?
2. ¿Por qué el raspado de pantalla es inaceptable?
3. ¿Qué hace específico y válido a un consentimiento?
4. ¿Por qué un banco que consume APIs puede terminar con más información que antes?
5. ¿Por qué la reciprocidad es la cuestión política central?

## 📥 Entregable

Guarda en `portfolio/parte-14/clase-03/`:

- los tres flujos de consentimiento diseñados;
- el consentimiento específico redactado y su comparación;
- la evaluación económica del consumo activo;
- los riesgos identificados con sus mitigantes.

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

- Basel Committee on Banking Supervision (2019). *Report on open banking and application programming interfaces*. BIS. Modelos de banca abierta comparados y sus riesgos prudenciales. <https://www.bis.org/bcbs/publ/d486.htm>
- Bank for International Settlements (2019). *The design of digital financial infrastructure: lessons from India*. BIS Papers 106. Infraestructura pública de identidad y pagos como caso de referencia.
- Financial Stability Board (2019). *FinTech and market structure in financial services*. FSB. Competencia entre bancos y terceros proveedores de servicios.
- Unión Europea (2015). *Directiva (UE) 2015/2366 sobre servicios de pago (PSD2)*. Marco de referencia de banca abierta.
- OECD (2023). *Open Finance Policy Considerations*. OECD. Extensión de la banca abierta al conjunto de datos financieros.
- Verificación local: revisa si existe un marco de banca o finanzas abiertas en tu país, qué entidades están obligadas, qué alcances cubre y quién autoriza a los terceros.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 02 · Pagos digitales y dinero electrónico](02-pagos-digitales.md) | [Parte 14](../README.md) · [Programa](../../../SYLLABUS.md) | [04 · Datos en un banco →](04-datos-en-un-banco.md) |
<!-- gen:footer:end -->
