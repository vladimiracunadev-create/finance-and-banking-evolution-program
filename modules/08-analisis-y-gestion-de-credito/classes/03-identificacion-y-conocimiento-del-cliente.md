---
part: 9
class: 3
title: "Identificación y conocimiento del cliente"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 03 · Identificación y conocimiento del cliente

> [← 02 · Solicitud y expediente](02-solicitud-y-expediente.md) · [Índice de la parte](../README.md) · [04 · Ingresos y estabilidad →](04-ingresos-y-estabilidad.md)

**Parte 09 — Análisis y gestión de crédito** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Cumplir la obligación que antecede a cualquier análisis crediticio: saber con certeza quién es el
cliente, de dónde provienen sus recursos y si su perfil es coherente con las operaciones que solicita.
Esta obligación tiene fundamento en la prevención del lavado de activos y, además, es la primera
defensa contra el fraude de identidad.

Antes de evaluar si alguien puede pagar hay que saber quién es, y esa obligación no viene del riesgo de crédito sino de la norma de prevención de lavado. Esta clase la desarrolla porque su incumplimiento tiene consecuencias que ninguna pérdida crediticia alcanza: sanciones, pérdida de corresponsalías y responsabilidad personal.

## 📚 Objetivos

Al finalizar podrás:

1. **Aplicar** el proceso de identificación y verificación del cliente.
2. **Determinar** el beneficiario final de una estructura societaria.
3. **Clasificar** el riesgo del cliente y aplicar la diligencia proporcional.
4. **Construir** el perfil transaccional esperado y detectar desviaciones.
5. **Identificar** las situaciones que exigen diligencia reforzada.

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

Los cuatro primeros términos son la obligación y sus niveles; los tres siguientes, los casos que exigen más y el seguimiento posterior. El **beneficiario final** es el concepto que más trabajo cuesta y más importa: la persona natural que en última instancia controla, que puede estar varias capas societarias más arriba.

| Concepto | Comprensión verificable |
|---|---|
| `conoce a tu cliente (KYC)` | Conjunto de procedimientos para identificar, verificar y entender al cliente. |
| `beneficiario final` | Persona natural que en última instancia posee o controla al cliente. |
| `diligencia debida` | Nivel de verificación aplicado. Es proporcional al riesgo. |
| `diligencia reforzada` | Nivel superior, para clientes o situaciones de mayor riesgo. |
| `persona expuesta políticamente (PEP)` | Quien ejerce o ejerció funciones públicas prominentes, y su entorno. |
| `perfil transaccional` | Comportamiento esperado del cliente, contra el que se comparan sus operaciones. |
| `operación inusual` | La que se aparta del perfil sin explicación económica aparente. |

## 🧠 Modelo mental

El proceso responde **tres preguntas encadenadas**:

```text
1. ¿QUIÉN es?          identificación y verificación
2. ¿QUÉ hace?          actividad económica y origen de fondos
3. ¿QUÉ ESPERO de él?  perfil transaccional

y luego, permanentemente:
4. ¿lo que hace coincide con lo que esperaba?  monitoreo
```

Sin la pregunta 3, la pregunta 4 no se puede responder: **no se puede detectar una operación inusual
sin haber definido qué es usual para ese cliente**.

## 📖 Desarrollo

### 1. Identificación y verificación

Identificar y verificar son dos cosas distintas y las dos son obligatorias. La tabla las separa con lo que exige cada una.

```text
IDENTIFICAR   obtener los datos que individualizan al cliente
VERIFICAR     comprobar esos datos con documentos o fuentes confiables
```

| Tipo de cliente | Datos mínimos | Verificación |
|---|---|---|
| Persona natural | Nombre, identificación, fecha de nacimiento, domicilio, nacionalidad, actividad | Documento oficial vigente; contraste con registro |
| Persona jurídica | Razón social, identificación tributaria, domicilio, giro, constitución, representantes | Certificados de vigencia y de poderes |
| Estructura sin personalidad | Fideicomisos, fondos, sucesiones | Documento constitutivo; identificación de las partes |

**Verificación en contratación remota** (Parte 4, clase 3):

```text
la contratación no presencial exige controles reforzados:
  · verificación biométrica o videollamada
  · contraste con bases de datos oficiales
  · verificación de vida (prueba de que la persona está presente)
  · verificación del documento (autenticidad y no alteración)
```

### 2. Beneficiario final

Determinar el beneficiario final exige recorrer la cadena de propiedad hasta llegar a personas naturales. El procedimiento siguiente lo estructura.

```text
beneficiario final = persona natural que posee o controla, directa o indirectamente,
                     al cliente, o en cuyo nombre se realiza una operación
```

Criterios habituales de determinación, en orden:

```text
1. participación en la propiedad por sobre un umbral (habitualmente 10 % o 25 %)
2. si no hay quien supere el umbral: quien ejerza el control por otros medios
3. si no se identifica: la persona natural que ocupe el cargo de administración superior
```

Ejemplo de cadena societaria:

```text
Cliente: Comercial Andes SpA
  └─ 60 % Inversiones Sur Ltda.
       └─ 55 % Holding Norte S.A.
            └─ 70 % Sra. Rivas          → 60 % × 55 % × 70 % = 23,1 %
            └─ 30 % Sr. Pardo           → 60 % × 55 % × 30 % =  9,9 %
       └─ 45 % Sr. Toledo               → 60 % × 45 %        = 27,0 %
  └─ 40 % Sra. Guzmán                                        = 40,0 %

beneficiarios finales con umbral de 25 %: Sra. Guzmán (40,0 %) y Sr. Toledo (27,0 %)
con umbral de 10 %: se agrega la Sra. Rivas (23,1 %)
```

**El cálculo es multiplicativo a lo largo de la cadena**, y detenerse en el primer nivel es el error
más común.

### 3. Clasificación de riesgo y diligencia proporcional

La intensidad de la diligencia se ajusta al riesgo del cliente, y esa proporcionalidad es una exigencia normativa. La tabla la recoge.

| Factor | Menor riesgo | Mayor riesgo |
|---|---|---|
| Tipo de cliente | Persona natural asalariada | Estructura con múltiples niveles |
| Actividad | Regulada y transparente | Intensiva en efectivo; comercio internacional complejo |
| Jurisdicción | Local, con marco robusto | Jurisdicciones de alto riesgo o con deficiencias identificadas |
| Producto | Cuenta de ahorro simple | Banca privada, corresponsalía, productos con anonimato |
| Canal | Presencial con verificación | Remoto sin controles reforzados |
| Condición | Sin condiciones especiales | PEP, o vinculado a una PEP |

```text
DILIGENCIA SIMPLIFICADA   riesgo bajo, verificación básica
DILIGENCIA ESTÁNDAR       riesgo normal
DILIGENCIA REFORZADA      riesgo alto: verificación adicional del origen de fondos
                          y del patrimonio, aprobación de nivel superior,
                          monitoreo más frecuente
```

**Situaciones que exigen diligencia reforzada:**

```text
· persona expuesta políticamente, su familia o su entorno cercano
· cliente o beneficiario final en jurisdicción de alto riesgo
· estructuras societarias complejas sin justificación económica
· operaciones con jurisdicciones con secreto reforzado
· cliente que se niega a proporcionar información sobre el beneficiario final
· actividad económica no coherente con el perfil declarado
```

### 4. Perfil transaccional

El perfil transaccional es lo que permite detectar después lo que no encaja. La tabla recoge cómo se construye.

```text
el perfil declara lo que se ESPERA del cliente:
  · monto promedio y máximo de operaciones
  · frecuencia
  · contrapartes habituales
  · productos que utilizará
  · origen de los fondos
  · destino de los pagos
  · zonas geográficas involucradas
```

```text
ejemplo de perfil:
  cliente: comerciante minorista, ventas mensuales declaradas 42 millones
  depósitos esperados: 35–50 millones mensuales, principalmente en efectivo y tarjetas
  transferencias emitidas: a proveedores identificados, 25–35 millones mensuales
  operaciones internacionales: ninguna
  productos: cuenta corriente, línea de capital de trabajo
```

Y contra ese perfil se contrastan las operaciones:

```text
mes observado:
  depósitos en efectivo:        118 millones   → 2,8x el perfil ⚠
  transferencias al exterior:    62 millones   → no contemplado en el perfil ⚠
  contrapartes nuevas:          14 empresas    → sin relación aparente con el giro ⚠
```

**Tres desviaciones simultáneas exigen investigación**, no un juicio inmediato. La investigación puede
concluir que hay una explicación legítima —una expansión del negocio, una venta de activos— y en ese
caso **se actualiza el perfil**.

### 5. Del hallazgo a la acción

Detectar una operación inusual abre un procedimiento con plazos y con reglas de confidencialidad estrictas. Los pasos siguientes lo recorren.

```text
1. desviación detectada por el monitoreo
2. análisis: ¿hay explicación económica aparente?
3. si no la hay: solicitar información al cliente
4. evaluar la explicación y la documentación que la respalde
5. si la explicación es satisfactoria: actualizar el perfil, documentar
6. si no lo es: escalar al oficial de cumplimiento
7. el oficial evalúa si corresponde reportar a la unidad de inteligencia financiera
```

Tres reglas que rigen el proceso:

```text
· NO se informa al cliente que se está evaluando un reporte
· la decisión de reportar es del oficial de cumplimiento, no del ejecutivo
· la obligación de reportar no depende de la certeza de un delito:
  basta que la operación sea inusual y no tenga explicación satisfactoria
```

## 🧮 Ejemplo guiado

El ejemplo determina el beneficiario final de una estructura de tres niveles. Conviene seguir los porcentajes: la propiedad indirecta se multiplica, y el umbral se aplica sobre el resultado.

**Situación.** Una empresa solicita una línea de comercio exterior por 400 millones. Aplica el proceso
completo.

```text
SOLICITANTE: Importadora Litoral SpA
  constituida hace 8 meses
  giro: importación de maquinaria industrial
  representante: Sr. Meza
  estructura declarada: 100 % Inversiones Cordillera Ltda.
```

**Paso 1 — identificación y verificación básica.**

```text
✓ certificado de vigencia obtenido y verificado
✓ identidad del representante verificada
✓ poderes vigentes
⚠ antigüedad de 8 meses con solicitud de 400 millones
```

**Paso 2 — determina el beneficiario final.**

```text
Importadora Litoral SpA
  └─ 100 % Inversiones Cordillera Ltda.
       └─ 50 % Sociedad Austral S.A. (constituida en jurisdicción extranjera)
       └─ 30 % Sr. Meza
       └─ 20 % Sra. Fuentes

la cadena se detiene en Sociedad Austral: no se identifica a sus socios
```

```text
participaciones calculadas:
  Sr. Meza:      30,0 %  → beneficiario final identificado
  Sra. Fuentes:  20,0 %  → beneficiario final si el umbral es 10 %
  Sociedad Austral: 50,0 % → BENEFICIARIO FINAL NO IDENTIFICADO
```

**Este es el hallazgo central:** el 50 % de la propiedad tiene un beneficiario final desconocido.

**Paso 3 — clasifica el riesgo.**

| Factor | Evaluación |
|---|---|
| Antigüedad | 8 meses: mayor riesgo |
| Estructura | Multinivel con sociedad extranjera: mayor riesgo |
| Jurisdicción | Verificar si la jurisdicción de Sociedad Austral está en listas de alto riesgo |
| Actividad | Comercio internacional: riesgo medio-alto |
| Producto | Comercio exterior: riesgo medio-alto |
| Beneficiario final | **No identificado en el 50 %**: riesgo alto |

```text
CLASIFICACIÓN: RIESGO ALTO → diligencia reforzada obligatoria
```

**Paso 4 — aplica la diligencia reforzada.**

```text
solicitudes al cliente:
  1. identificación completa de los socios de Sociedad Austral, hasta persona natural
  2. documentación del origen de los fondos aportados al capital
  3. estados financieros de las sociedades de la cadena
  4. explicación de la razón económica de la estructura
  5. contratos o cartas de intención con los proveedores del exterior
  6. detalle de los clientes finales de la maquinaria importada
```

**Paso 5 — construye el perfil transaccional esperado.**

```text
si la operación se aprueba, el perfil sería:
  · cartas de crédito emitidas: 3 a 5 al año, de 60 a 120 millones cada una
  · beneficiarios: proveedores de maquinaria identificados, en 2-3 países
  · pagos al exterior: solo a los beneficiarios de las cartas de crédito
  · ingresos: ventas locales de la maquinaria importada
  · depósitos en efectivo: mínimos o nulos (no corresponde al giro)

ALERTAS que se configurarían:
  · pago al exterior a un beneficiario distinto del proveedor de la carta
  · depósitos en efectivo superiores a 5 millones mensuales
  · operaciones con jurisdicciones distintas de las declaradas
  · triangulación: importación de un país y pago a otro
```

**Paso 6 — decisión.**

```text
LA OPERACIÓN NO PUEDE APROBARSE mientras el beneficiario final del 50 %
de la propiedad no esté identificado.

fundamento:
  · es una obligación normativa, no una decisión comercial
  · la negativa o imposibilidad de identificar al beneficiario final
    es en sí misma una señal de alerta
  · aprobar sin esa identificación expone a la institución a sanción
    y a riesgo reputacional

ACCIONES
  1. suspender la evaluación crediticia hasta completar la identificación
  2. si el cliente no proporciona la información, evaluar el término de la relación
  3. si la estructura no tiene explicación económica razonable, escalar al oficial
     de cumplimiento con independencia de la decisión comercial
  4. documentar toda la gestión en el expediente

NOTA IMPORTANTE
  El análisis de capacidad de pago, garantías y flujo NO se realiza todavía.
  El conocimiento del cliente ANTECEDE al análisis crediticio: si no se sabe
  quién es el cliente, no hay nada que analizar.
```

**Interpreta:** el proceso se detuvo en el paso 2, **antes de cualquier análisis financiero**. Esa
secuencia no es burocrática: si el 50 % de la propiedad es desconocida, no se sabe a quién se le está
prestando, y ningún análisis de capacidad de pago corrige eso.

## 🏦 Del cliente al banco

El cliente aporta documentos y el banco cumple una obligación con sanción personal asociada. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| "Piden datos de mis socios" | Identificación del beneficiario final: obligación normativa | 12, clase 5 |
| Cuenta rechazada sin explicación detallada | Puede haber prohibición de informar | 12, clase 9 |
| Solicitud de origen de fondos | Diligencia reforzada por perfil de riesgo | 12, clase 5 |
| Operación bloqueada temporalmente | Revisión por desviación del perfil | 12, clase 8 |
| Actualización periódica de datos | Obligación de mantener la información vigente | 12, clase 5 |

## 🧪 Práctica

El laboratorio pide determinar el beneficiario final en estructuras societarias sintéticas y clasificar el riesgo. Una de las estructuras está diseñada para ocultarlo, y detectarla es el objetivo.

En `labs/lab-02.md`:

1. Determina el beneficiario final de tres estructuras societarias con cadenas de tres niveles.
2. Clasifica el riesgo de cinco perfiles de cliente y define la diligencia aplicable.
3. Construye el perfil transaccional de dos clientes y define sus alertas.
4. Analiza un caso de desviación del perfil y define el curso de acción.

## ⚠️ Errores frecuentes

Los síntomas de la tabla aparecen en revisiones de cumplimiento. Las causas están en cadenas de propiedad no recorridas hasta el final y en perfiles transaccionales no construidos.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se identifica solo al primer nivel de propiedad | Cadena no recorrida | El cálculo es multiplicativo hasta persona natural. |
| Se aplica la misma diligencia a todos | Proporcionalidad ignorada | Clasifica el riesgo y ajusta el nivel. |
| No hay perfil transaccional | No se puede detectar lo inusual | Define el perfil al inicio de la relación. |
| Se informa al cliente de una investigación | Prohibición normativa | No se comunica; se escala al oficial. |
| Se analiza el crédito antes de identificar al cliente | Secuencia invertida | El conocimiento del cliente antecede al análisis. |
| El perfil no se actualiza | Desviaciones legítimas mal clasificadas | Actualiza el perfil cuando la explicación es satisfactoria. |

## ❓ Preguntas de comprobación

1. ¿Cuáles son las tres preguntas encadenadas del proceso y por qué ese orden?
2. Calcula el beneficiario final de una cadena de tres niveles con participaciones cruzadas.
3. Nombra cinco situaciones que exigen diligencia reforzada.
4. ¿Por qué no se puede detectar una operación inusual sin perfil transaccional?
5. ¿Qué se hace cuando no se logra identificar al beneficiario final?

## 📥 Entregable

Guarda en `portfolio/parte-09/clase-03/`:

- el beneficiario final determinado de tres estructuras con su cálculo;
- la clasificación de riesgo de cinco perfiles con la diligencia aplicable;
- dos perfiles transaccionales construidos con sus alertas configuradas;
- el análisis de un caso de desviación con el curso de acción documentado.

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

- Financial Action Task Force (2023). *FATF Recommendations*, R.10 (diligencia debida), R.12 (PEP), R.24 y R.25 (beneficiario final). <https://www.fatf-gafi.org/>
- Basel Committee on Banking Supervision (2016, rev. 2020). *Sound management of risks related to money laundering and financing of terrorism*. BIS. <https://www.bis.org/bcbs/publ/d505.htm>
- Wolfsberg Group (2022). *Wolfsberg Standards on Correspondent Banking and CDD*. Buenas prácticas de la industria. <https://www.wolfsberg-principles.com/>
- Financial Action Task Force (2020). *Guidance on Digital Identity*. Verificación en contratación remota.
- Egmont Group. *Best Practices for Suspicious Transaction Reporting*. Proceso de reporte a unidades de inteligencia financiera.
- Verificación local: revisa la ley de prevención de lavado de activos de tu país, el umbral de beneficiario final aplicable y las obligaciones de reporte de tu institución.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 02 · Solicitud y expediente](02-solicitud-y-expediente.md) | [Parte 09](../README.md) · [Programa](../../../SYLLABUS.md) | [04 · Ingresos y estabilidad →](04-ingresos-y-estabilidad.md) |
<!-- gen:footer:end -->
