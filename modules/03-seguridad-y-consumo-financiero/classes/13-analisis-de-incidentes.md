<!-- meta
part: 4
class: 13
title: "Análisis de incidentes"
level: intermedio
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 13 · Análisis de incidentes

> [← 12 · Prevención y respuesta ante fraude](12-prevencion-y-respuesta-ante-fraude.md) · [Índice de la parte](../README.md) · [14 · Proyecto: protocolo personal de seguridad →](14-proyecto-protocolo-personal-de-seguridad.md)

**Parte 04 — Seguridad y consumo financiero** · **Nivel:** Intermedio — requiere las partes anteriores · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Convertir un incidente —propio o ajeno— en aprendizaje estructurado. Un fraude que ocurre y no se
analiza se repite; uno que se analiza produce controles nuevos. Esta clase enseña el método de
análisis de causa raíz aplicado a incidentes financieros personales, y la construcción de una
retrospectiva que efectivamente cambie algo.

Las clases anteriores responden a un incidente. Esta aprende de él, que es lo único que evita el segundo. El método viene de la ingeniería de seguridad y se aplica igual a una persona que a una entidad: separar la causa inmediata de la causa raíz y diseñar el control sobre la segunda, porque corregir la primera deja el problema intacto.

## 📚 Objetivos

Al finalizar podrás:

1. **Reconstruir** la cronología de un incidente con evidencia.
2. **Aplicar** el análisis de los cinco porqués para llegar a la causa raíz.
3. **Distinguir** causa raíz, causa inmediata y factor contribuyente.
4. **Diseñar** controles que ataquen la causa raíz y no el síntoma.
5. **Redactar** una retrospectiva sin culpa que produzca cambios verificables.

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

Los tres primeros términos separan niveles de causa y los tres últimos son el método y su resultado. La distinción entre **causa inmediata y causa raíz** es toda la clase: la causa inmediata explica este incidente y la causa raíz explica por qué era posible, y solo la segunda admite un control que sirva.

| Concepto | Comprensión verificable |
|---|---|
| `causa inmediata` | El último eslabón: "entregué el código". Es visible y poco útil por sí sola. |
| `causa raíz` | La condición que hizo posible la cadena: "no distingo un mensaje legítimo de uno falso porque nunca verifico el remitente". |
| `factor contribuyente` | Circunstancia que aumentó la probabilidad o el daño: cansancio, urgencia, límite alto. |
| `barrera` | Control que debió detener el incidente. Se analiza por qué no lo hizo. |
| `retrospectiva sin culpa` | Análisis centrado en el sistema y no en la persona. Produce información honesta. |
| `acción correctiva` | Cambio concreto, con responsable y fecha, verificable. |

## 🧠 Modelo mental

Un incidente **no tiene una causa: tiene una cadena de barreras que fallaron**.

```text
mensaje falso llega   →  [barrera 1: filtro de correo]        falló
se lee y se cree      →  [barrera 2: verificación de dominio] no existía
se entrega el código  →  [barrera 3: regla de no compartir]   no existía
se transfiere el saldo→  [barrera 4: límite diario]           no configurado
se detecta tarde      →  [barrera 5: notificación]            desactivada
```

Culpar a la persona por la tercera barrera ignora que había cinco, y que **cuatro de las cinco se
configuran una sola vez**. Ese es el valor del análisis: mueve la solución desde "ser más cuidadoso"
—que no es un control— hacia controles concretos.

## 📖 Desarrollo

### 1. Reconstruir la cronología

El análisis empieza por una cronología con horas, no por una explicación. El formato siguiente es el que hace visibles los huecos.

```text
formato de línea de tiempo

hora     evento                                  evidencia
22:12    llega mensaje de "verificación"         captura del correo
22:14    se abre el enlace                       historial del navegador
22:18    se ingresan credenciales                —
22:20    llega código al teléfono                captura del mensaje
22:22    se ingresa el código en el sitio falso  —
22:38    transferencia de 780 000                notificación
22:40    llega la notificación                   captura
22:41    bloqueo                                 registro del caso
```

Dos métricas se leen de inmediato:

```text
tiempo de compromiso  22:12 → 22:38 = 26 minutos
tiempo de detección   22:38 → 22:40 = 2 minutos
tiempo de contención  22:40 → 22:41 = 1 minuto
```

Un tiempo de detección de 2 minutos indica que la capa 2 funcionó. Un tiempo de compromiso de 26
minutos indica que hubo margen: entre las 22:14 y las 22:22 existieron al menos tres oportunidades de
detener la cadena.

### 2. Los cinco porqués

Preguntar por qué cinco veces seguidas lleva de la causa inmediata a la raíz, y suele detenerse antes de tiempo. El ejemplo siguiente lo recorre entero.

```text
¿por qué se transfirió el dinero?
  porque el atacante inició sesión en la banca en línea
¿por qué pudo iniciar sesión?
  porque obtuvo usuario, clave y código de verificación
¿por qué obtuvo el código?
  porque la víctima lo ingresó en un sitio falso
¿por qué lo ingresó?
  porque creyó que el sitio era del banco
¿por qué lo creyó?
  porque nunca verificó el dominio, y no tenía el hábito de hacerlo
      ← CAUSA RAÍZ
```

El resultado es accionable: la causa raíz no es "fue descuidado" sino **"no existía un procedimiento
de verificación de dominio ni un factor que lo hiciera innecesario"**. De ahí salen dos controles
concretos: aprender el método de la clase 2, e implantar un factor resistente al phishing que hace
irrelevante la verificación manual.

### 3. Causa raíz, causa inmediata y factores

Las tres categorías se confunden y llevan a controles distintos. La tabla las separa con un ejemplo de cada una.

| Tipo | Ejemplo del caso | Qué produce si se ataca |
|---|---|---|
| Causa inmediata | Ingresó el código | "Ser más cuidadoso": sin efecto medible |
| Causa raíz | No hay verificación de dominio ni factor resistente | Elimina la clase completa de ataques |
| Factor contribuyente | Domingo 22:12, cansancio | No se elimina; se compensa con controles automáticos |
| Factor contribuyente | Sin límite diario configurado | Se elimina en 2 minutos |
| Factor contribuyente | Correo del banco igual al correo público | Se elimina separando cuentas |

La distinción es práctica: **los factores contribuyentes suelen ser los más fáciles de eliminar** y
reducen el daño incluso cuando la causa raíz persiste.

### 4. Diseñar controles sobre la causa raíz

Un control sobre la causa inmediata evita la repetición exacta y nada más. La tabla contrasta ambos diseños sobre el mismo incidente.

```text
control 1  llave de seguridad física en correo y banca (donde esté disponible)
           → elimina la clase de ataque, no solo este caso
control 2  regla escrita: ningún código se entrega por ningún canal
           → verificable: se puede recitar
control 3  límite diario ajustado a la operación habitual
           → acota el daño si 1 y 2 fallan
control 4  notificación instantánea de todo monto
           → mantiene el tiempo de detección bajo
control 5  correo dedicado a banca, distinto del público
           → reduce la superficie de llegada de mensajes falsos
```

Cada control se evalúa con dos preguntas: **¿elimina la clase de ataque o solo este caso?** y **¿funciona
sin atención humana?**. Los controles que dependen de recordar algo en el momento equivocado fallan
exactamente cuando se necesitan.

### 5. Retrospectiva sin culpa

El análisis solo funciona si se puede decir lo que pasó, y eso exige separar el análisis de la responsabilidad. Los criterios siguientes lo consiguen.

```text
ESTRUCTURA

1. QUÉ OCURRIÓ        cronología con evidencia, sin adjetivos
2. IMPACTO            pérdida, tiempo, efectos secundarios
3. QUÉ FUNCIONÓ       barreras que sí operaron (importante: hay que nombrarlas)
4. QUÉ FALLÓ          barreras ausentes o inefectivas
5. CAUSA RAÍZ         resultado de los cinco porqués
6. ACCIONES           control, responsable, fecha, cómo se verifica
7. SEGUIMIENTO        fecha de revisión de que las acciones se ejecutaron
```

La sección 3 es la que más se omite y la que hace utilizable el documento: si el análisis solo lista
fallas, la conclusión implícita es "todo estuvo mal", lo que no orienta. Nombrar lo que funcionó
—el límite diario que evitó 1 200 000 adicionales— indica qué controles conservar y replicar.

## 🧮 Ejemplo guiado

El ejemplo analiza un incidente completo desde la cronología hasta el control diseñado. Conviene seguir los cinco porqués sin saltárselos: la causa raíz aparece en el cuarto o el quinto, y detenerse antes es el error más común del método.

**Situación.** Analiza un incidente distinto: durante ocho meses se cobró a Paula un seguro no
contratado (caso de la clase 9). No hubo fraude externo; hubo un fallo de control propio y ajeno.

**Paso 1 — cronología.**

```text
04-12  firma del crédito; el ejecutivo menciona seguro "opcional"
05-01  primer cobro de 9 200 en la cuota
05-02 a 05-08  siete cobros más
12-03  primer reclamo telefónico (sin número de caso)
04-05  segundo reclamo telefónico
18-06  tercer reclamo telefónico
05-08  reclamo escrito formal
```

**Paso 2 — métricas.**

```text
tiempo de detección  05-01 → 12-03 = 66 días
tiempo de escalamiento correcto  12-03 → 05-08 = 146 días
costo del retraso  8 cobros × 9 200 = 73 600
```

**Paso 3 — cinco porqués.**

```text
¿por qué se cobró el seguro?
  porque estaba incorporado al crédito sin figurar en el contrato
¿por qué no se detectó al primer cobro?
  porque no se revisó el detalle de la cuota, solo el monto total
¿por qué no se revisó el detalle?
  porque no existía el hábito de revisar la composición de las cuotas
¿por qué el reclamo no avanzó en 5 meses?
  porque se hizo por teléfono, sin número de caso ni fundamento escrito
¿por qué se reclamó así?
  porque no se conocía la estructura de un reclamo eficaz
      ← DOS CAUSAS RAÍZ: falta de revisión y falta de método de reclamo
```

**Paso 4 — qué funcionó y qué falló.**

| | Elemento |
|---|---|
| Funcionó | Paula conservó el contrato, la hoja resumen y los estados de cuenta |
| Funcionó | Detectó la discrepancia al comparar contrato y cuota |
| Falló | No revisó la composición de la cuota durante 66 días |
| Falló | Reclamó por un canal sin trazabilidad |
| Falló | El control de la entidad permitió un cobro sin respaldo contractual |

**Paso 5 — acciones correctivas.**

| Control | Verificación | Fecha |
|---|---|---|
| Revisar la composición de cada cuota el mes 1 de todo crédito nuevo | Registro en el portafolio | Inmediato |
| Revisión trimestral de cargos recurrentes en todos los productos | Lista de cargos verificada | Trimestral |
| Todo reclamo por escrito con los siete apartados (clase 9) | Número de caso obtenido | Inmediato |
| Conservar hoja resumen y contrato de todo producto | Carpeta de portafolio | Inmediato |

**Paso 6 — la lección transferible.** El control más valioso no es el que evita este cobro específico,
sino el que **detecta cualquier cargo no contratado en el primer mes**. Una revisión de la composición
de la cuota, una vez, al mes siguiente de contratar, habría reducido el perjuicio de 73 600 a 9 200 y
el proceso de 7 meses a semanas.

**Interpreta:** los incidentes sin atacante también tienen causa raíz y controles. Y la métrica que
importa no es "cuánto se perdió" sino **"cuánto tiempo pasó hasta detectarlo"**, porque ese tiempo es
lo que un control puede reducir.

## 🏦 Del cliente al banco

La persona analiza su incidente y el banco analiza patrones agregados de miles. La tabla enfrenta las dos lecturas, y la segunda es la que reaparece en la Parte 11 como riesgo operacional.

| Vista personal | Equivalente institucional | Parte |
|---|---|---|
| Cronología del incidente | Línea de tiempo del análisis forense | 11, clase 15 |
| Cinco porqués | Análisis de causa raíz obligatorio | 11, clase 15 |
| Retrospectiva sin culpa | Cultura de reporte de eventos operacionales | 11, clase 7 |
| Acciones con responsable y fecha | Plan de acción de auditoría | 12, clase 13 |
| Barreras que funcionaron | Efectividad de controles medida | 12, clase 12 |

## 🧪 Práctica

El laboratorio pide analizar un incidente sintético y proponer controles sobre la causa raíz. La trampa del ejercicio es que la causa inmediata es evidente y la raíz está dos niveles más abajo.

En `labs/lab-06.md`, sección de incidentes:

1. Reconstruye la cronología de un incidente propio o documentado, con evidencia.
2. Calcula tiempo de compromiso, de detección y de contención.
3. Aplica los cinco porqués hasta llegar a la causa raíz.
4. Redacta la retrospectiva completa con acciones verificables y fecha de seguimiento.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen incidentes que se repiten después de haberlos corregido. La causa es siempre la misma: se corrigió la causa inmediata.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| La conclusión es "hay que tener más cuidado" | Se quedó en la causa inmediata | Aplica los cinco porqués hasta una causa accionable. |
| El análisis busca culpables | Retrospectiva con culpa | Centra el análisis en las barreras, no en la persona. |
| No se nombra lo que funcionó | Sesgo hacia el error | Lista las barreras efectivas: indican qué conservar. |
| Las acciones no tienen fecha | No son verificables | Cada acción con responsable, fecha y verificación. |
| El mismo incidente se repite | No se atacó la causa raíz | Evalúa si el control elimina la clase de ataque. |
| No se mide el tiempo de detección | Se mide solo la pérdida | El tiempo es lo que un control puede reducir. |

## ❓ Preguntas de comprobación

1. ¿Por qué un incidente no tiene una causa sino una cadena de barreras?
2. Aplica los cinco porqués a un incidente y señala dónde está la causa raíz.
3. ¿Qué dos preguntas evalúan la calidad de un control propuesto?
4. ¿Por qué la sección "qué funcionó" es indispensable en una retrospectiva?
5. ¿Qué métrica importa más que la pérdida y por qué?

## 📥 Entregable

Guarda en `portfolio/parte-04/clase-13/`:

- la cronología del incidente con evidencia y las tres métricas de tiempo;
- el análisis de los cinco porqués con la causa raíz identificada;
- la tabla de barreras que funcionaron y que fallaron;
- la retrospectiva completa con acciones, responsables, fechas y verificación.

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

- Reason, J. (1997). *Managing the Risks of Organizational Accidents*. Ashgate. Modelo de barreras y análisis de causa raíz.
- Dekker, S. (2014). *The Field Guide to Understanding Human Error* (3.ª ed.). CRC Press. Retrospectivas sin culpa y factores contribuyentes.
- NIST (2012). *SP 800-61 Rev. 2: Computer Security Incident Handling Guide*. Fases de análisis y lecciones aprendidas.
- Financial Stability Board (2020). *Effective Practices for Cyber Incident Response and Recovery*. FSB. Análisis posterior al incidente.
- Basel Committee on Banking Supervision (2011). *Principles for the Sound Management of Operational Risk*. BIS. Registro y análisis de eventos operacionales. <https://www.bis.org/publ/bcbs195.htm>
- Verificación local: revisa si tu país exige reportar incidentes de seguridad que afecten datos personales y en qué plazo.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 12 · Prevención y respuesta ante fraude](12-prevencion-y-respuesta-ante-fraude.md) | [Parte 04](../README.md) · [Programa](../../../SYLLABUS.md) | [14 · Proyecto: protocolo personal de seguridad →](14-proyecto-protocolo-personal-de-seguridad.md) |
<!-- gen:footer:end -->
