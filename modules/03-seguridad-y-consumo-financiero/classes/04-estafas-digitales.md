---
part: 4
class: 4
title: "Estafas digitales"
level: fundamento
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 04 · Estafas digitales

> [← 03 · Robo de identidad](03-robo-de-identidad.md) · [Índice de la parte](../README.md) · [05 · Contraseñas y autenticación multifactor →](05-contrasenas-y-autenticacion-multifactor.md)

**Parte 04 — Seguridad y consumo financiero** · **Nivel:** Fundamento — sin conocimientos previos · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Reconocer las estructuras de fraude que prometen rentabilidad, empleo, premios o amor, y que tienen en
común una cosa: **la matemática no cuadra**. Esta clase entrega las herramientas cuantitativas para
detectar un esquema piramidal antes de entrar, y el análisis de los patrones más frecuentes de estafa
digital.

Los dos fraudes anteriores buscan un acceso o una identidad. Este busca que la víctima transfiera voluntariamente, y por eso ningún control técnico lo detiene. Lo que sí lo detiene es un control de razonabilidad aritmético, que esta clase enseña a aplicar en menos de un minuto.

## 📚 Objetivos

Al finalizar podrás:

1. **Demostrar** por qué un esquema piramidal colapsa necesariamente, con aritmética.
2. **Aplicar** el control de razonabilidad de rentabilidad a cualquier oferta.
3. **Reconocer** los seis patrones de estafa digital más frecuentes.
4. **Verificar** la existencia y autorización de una entidad antes de entregar dinero.
5. **Responder** cuando el dinero ya fue transferido.

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

Los dos primeros términos son las estructuras que sostienen estas estafas; los cuatro últimos son las comprobaciones y los riesgos asociados. La **irreversibilidad** es lo que decide el desenlace: no todos los medios de pago se pueden revertir, y elegir bien el medio antes de pagar vale más que cualquier verificación posterior.

| Concepto | Comprensión verificable |
|---|---|
| `esquema Ponzi` | Paga a los antiguos con el dinero de los nuevos. No hay actividad económica que genere el retorno. |
| `esquema piramidal` | El retorno depende de reclutar participantes. Colapsa por agotamiento matemático de la población. |
| `control de razonabilidad` | Comparar la rentabilidad ofrecida con la de mercado y exigir explicación del diferencial. |
| `entidad no autorizada` | No inscrita en el registro del supervisor. No puede captar dinero del público. |
| `mula financiera` | Persona que recibe y reenvía dinero de origen ilícito, con o sin conocimiento. Tiene consecuencias legales. |
| `irreversibilidad` | Transferencias, criptoactivos y giros internacionales son difíciles o imposibles de revertir. |

## 🧠 Modelo mental

Todo esquema piramidal enfrenta la misma pared:

```text
cada participante debe reclutar 6 para cobrar

nivel 1        6 personas
nivel 2       36
nivel 3      216
nivel 5    7 776
nivel 8  1 679 616
nivel 10 60 466 176      ← ya supera la población de la mayoría de los países
nivel 13 más de 13 000 millones  ← supera la población mundial
```

El colapso no es un riesgo: es una **certeza aritmética**. La única pregunta es en qué nivel estás
cuando ocurre, y la respuesta es que la gran mayoría está en los últimos niveles, porque cada nivel
tiene más gente que todos los anteriores juntos.

## 📖 Desarrollo

### 1. Control de razonabilidad de rentabilidad

Una rentabilidad prometida se puede contrastar en el acto con lo que produce el mercado, y casi todas las estafas de inversión no sobreviven a esa comprobación. El cálculo siguiente es esa comprobación.

```text
1. ¿cuál es la tasa de un depósito bancario a ese plazo?
2. ¿cuánto ofrece esta alternativa?
3. ¿cuál es el diferencial?
4. ¿qué riesgo concreto justifica ese diferencial?
5. si la respuesta es "ninguno, está garantizado" → incoherencia estructural
```

| Rentabilidad ofrecida | Duplica el capital en (regla del 72) | Lectura |
|---:|---|---|
| 6 % anual | 12 años | Mercado |
| 12 % anual | 6 años | Alta, exige riesgo declarado |
| 30 % anual | 2,4 años | Muy alta, riesgo elevado |
| 10 % mensual | 7 meses | **Imposible de sostener** |
| 5 % semanal | 3,5 meses | **Imposible de sostener** |

Un 10 % mensual equivale a **214 % anual**. Ninguna actividad económica legal sostiene ese retorno de
forma continua para un número creciente de participantes; si existiera, no necesitaría captar dinero
de particulares.

### 2. Los seis patrones más frecuentes

Las estafas cambian de nombre y repiten estructura. La tabla recoge los seis patrones que concentran la mayoría de los casos, con la señal que los delata.

| Patrón | Cómo opera | Señal decisiva |
|---|---|---|
| Inversión con retorno garantizado | Retorno fijo alto, "sin riesgo" | Rentabilidad y garantía son incompatibles |
| Reclutamiento | Ganas por incorporar personas | El ingreso depende de reclutar, no de vender |
| Empleo falso | Piden pago por materiales, curso o "activación" | Un empleo no exige pagar por adelantado |
| Premio o herencia | Ganaste algo; paga impuestos o gastos | Nunca se paga por recibir un premio |
| Romance | Vínculo afectivo prolongado, luego emergencia | Nunca han podido reunirse en persona |
| Falso soporte o comercio | Tienda o servicio inexistente | Sin registro, sin historial, pago irreversible |

En los seis, el punto de decisión es el mismo: **una transferencia irreversible a alguien que no puedes
verificar**.

### 3. Verificación antes de transferir

Antes de transferir a alguien desconocido hay tres comprobaciones que cuestan dos minutos. Los pasos siguientes son esas comprobaciones.

```text
1. ¿la entidad está en el registro del supervisor de valores o bancario? (sitio oficial)
2. ¿el producto está inscrito, si corresponde?
3. ¿la cuenta receptora está a nombre de la entidad o de una persona natural?
4. ¿existe contrato escrito con identificación completa de la contraparte?
5. ¿hay presión para decidir hoy?
6. ¿me piden reclutar o me ofrecen comisión por hacerlo?
7. ¿el medio de pago es reversible?
```

La pregunta 3 es la más discriminante en la práctica: **las entidades autorizadas reciben en cuentas a
su nombre**. Una transferencia a la cuenta personal de un intermediario es, por sí sola, motivo
suficiente para detener la operación.

### 4. Irreversibilidad por medio de pago

Los medios de pago se ordenan por su posibilidad de reversión, y esa es la variable que más importa cuando hay dudas. La tabla los ordena.

| Medio | Reversibilidad | Ventana |
|---|---|---|
| Tarjeta de crédito | Alta (contracargo) | Semanas |
| Tarjeta de débito | Media | Días |
| Transferencia bancaria local | Baja | Horas, si el destino no retiró |
| Transferencia internacional | Muy baja | — |
| Criptoactivos | **Nula** | — |
| Efectivo o giro | **Nula** | — |

Un vendedor que insiste en un medio irreversible está eligiendo, deliberadamente, el que no permite
reclamo. Esa insistencia es información.

### 5. Cuando ya transferiste

Si la transferencia ya salió, quedan acciones cuyo éxito depende casi por completo de las primeras horas. Los pasos siguientes están en orden de urgencia.

```text
hora 0–2
  1. contacta a tu banco: si la transferencia es reciente, puede intentarse el bloqueo
  2. denuncia ante la autoridad competente
  3. reúne toda la evidencia: mensajes, comprobantes, sitio, datos de la contraparte

día 1–7
  4. si pagaste con tarjeta, solicita contracargo dentro del plazo
  5. reporta al supervisor financiero si la entidad captaba sin autorización
  6. si hay más afectados, la denuncia conjunta suele avanzar más rápido

siempre
  7. NO pagues nada para "recuperar" el dinero: es la segunda ola (clase 2)
  8. si recibiste y reenviaste dinero de terceros, informa de inmediato:
     podrías figurar como mula financiera
```

El punto 8 merece atención especial: aceptar recibir dinero en tu cuenta y reenviarlo a cambio de una
comisión —presentado como "trabajo de gestión de pagos"— constituye participación en el circuito del
fraude, con consecuencias legales reales aunque no supieras el origen.

## 🧮 Ejemplo guiado

**Situación.** A Andrés le ofrecen una "plataforma de trading automatizado" que promete 8 % mensual,
con retiro libre, y una comisión del 10 % por cada persona que incorpore.

**Paso 1 — control de razonabilidad.**

```text
8 % mensual → (1,08)^12 − 1 = 152,7 % anual
depósito bancario a 12 meses ≈ 6 % anual
diferencial ≈ 147 puntos porcentuales
regla del 72: duplica el capital en 9 meses
```

**Paso 2 — la pregunta que define todo.** ¿Qué actividad genera 152,7 % anual de forma sostenida? Si
existiera y fuera repetible, no necesitaría captar dinero de particulares: se financiaría con deuda
bancaria al 8 % anual y quedaría con el diferencial.

**Paso 3 — el componente de reclutamiento.** La comisión por incorporar personas convierte el esquema
en piramidal por definición: parte del retorno proviene de nuevos participantes, no de la actividad.

**Paso 4 — proyecta el colapso.** Supongamos 1 000 participantes iniciales con 2 000 000 cada uno.

```text
capital captado                     2 000 000 000
retorno prometido mensual (8 %)       160 000 000
para pagarlo sin actividad real se necesitan 80 nuevos participantes al mes
mes 12: se requieren 960 participantes nuevos acumulados
mes 24: el requerimiento crece de forma exponencial
```

El sistema requiere crecimiento permanente. En el momento en que el reclutamiento se desacelera —no
cuando se detiene— los pagos no alcanzan y se suspenden los retiros. Ese es el patrón observado en
todos los casos documentados: **primero se restringen los retiros, luego se anuncia un "problema
técnico", luego desaparece**.

**Paso 5 — verifica en el registro.**

```text
consulta en el registro del supervisor de valores: la entidad NO aparece
la cuenta receptora está a nombre de una persona natural
el "contrato" es un documento sin identificación tributaria de la contraparte
```

Tres verificaciones objetivas, sin necesidad de juzgar intenciones.

**Paso 6 — la conversación difícil.** A Andrés lo invitó un familiar que ya cobró dos retornos y está
convencido. Los cobros iniciales **son reales**: es exactamente así como el esquema construye
credibilidad y consigue que los primeros participantes recluten a los siguientes de buena fe.

```text
argumento útil: "Si el retorno es real, ¿por qué paga comisión por reclutar?
                 Un negocio rentable no necesita pagar por captar capital al 152 % anual."
```

**Interpreta:** Andrés no necesitó detectar un engaño sofisticado. Le bastó **aritmética de dos
minutos y tres verificaciones objetivas**. Esa es la propiedad valiosa: el control de razonabilidad no
depende de detectar la mentira, sino de comprobar que los números no cierran.

## 🏦 Del cliente al banco

La víctima ve una oportunidad y el banco ve una transferencia autorizada por el titular. La tabla enfrenta las dos lecturas, y explica por qué estos casos son los más difíciles de reclamar: la operación fue legítima desde el sistema.

| Vista del cliente | Vista del sistema financiero | Parte |
|---|---|---|
| Transferencia a un particular | Posible operación inusual; puede generar reporte | 12, clase 8 |
| Recibir y reenviar fondos | Patrón típico de mula financiera; se monitorea | 12, clase 6 |
| Entidad no registrada | Captación irregular; competencia del supervisor | 12, clase 1 |
| Denuncia del cliente | Insumo para inteligencia financiera | 12, clase 9 |

## 🧪 Práctica

El laboratorio pide aplicar el control de razonabilidad a ofertas sintéticas y ordenar medios de pago por reversibilidad. Los números de las ofertas están tomados de estructuras reales, y el control las descarta todas en el primer paso.

En `labs/lab-03.md`:

1. Construye la tabla de crecimiento de un esquema piramidal con distintos factores de reclutamiento.
2. Aplica el control de razonabilidad a tres ofertas reales que hayas recibido.
3. Verifica en el registro oficial tres entidades que ofrezcan inversión.
4. Documenta el procedimiento de denuncia y contracargo de tu país con plazos.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen el momento en que la estafa se hace evidente, que suele ser cuando se intenta retirar. Las causas están en la ausencia del control de razonabilidad al principio.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se confía porque otros ya cobraron | Los pagos iniciales son parte del esquema | La credibilidad temprana es el mecanismo, no la prueba. |
| Se acepta "rentabilidad garantizada alta" | No se aplicó el control de razonabilidad | Rentabilidad alta y garantía son incompatibles. |
| Se transfiere a una cuenta personal | No se verificó la titularidad | Las entidades reciben a su nombre. |
| Se paga por adelantado por un empleo | Patrón de empleo falso | Un empleo no exige pago previo. |
| Se paga para "recuperar" el dinero perdido | Segunda ola | Nadie cobra por devolverte tu dinero. |
| Se acepta recibir y reenviar fondos | Rol de mula financiera | Tiene consecuencias legales; repórtalo. |

## ❓ Preguntas de comprobación

1. Demuestra con números por qué un esquema piramidal colapsa necesariamente.
2. ¿Qué anualiza un 8 % mensual y por qué es insostenible?
3. ¿Cuál es la verificación más discriminante antes de transferir y por qué?
4. Ordena los medios de pago por reversibilidad y explica la consecuencia práctica.
5. ¿Por qué los primeros participantes cobran de verdad y qué función cumple eso?

## 📥 Entregable

Guarda en `portfolio/parte-04/clase-04/`:

- la tabla de crecimiento piramidal con al menos tres factores de reclutamiento;
- el control de razonabilidad aplicado a tres ofertas reales;
- la evidencia de verificación en el registro oficial de tres entidades;
- el procedimiento documentado de denuncia y contracargo con plazos vigentes.

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

- IOSCO (2020). *Investor Protection and Financial Fraud*. Organización Internacional de Comisiones de Valores. Tipología de fraudes de inversión. <https://www.iosco.org/>
- Securities and Exchange Commission. *Ponzi Schemes — Investor Alerts and Bulletins*. SEC. Señales de alerta y casos documentados. <https://www.investor.gov/>
- Financial Action Task Force (2023). *Money Laundering Typologies*. GAFI/FATF. Uso de mulas financieras y circuitos de fraude.
- Europol (2024). *Internet Organised Crime Threat Assessment (IOCTA)*. Europol. Fraude de inversión y estafas románticas.
- Cialdini, R. (2021). *Influence: The Psychology of Persuasion*. Harper Business. Prueba social y compromiso en esquemas de reclutamiento.
- Verificación local: consulta el registro de entidades autorizadas del supervisor de valores de tu país y sus alertas públicas sobre entidades no inscritas.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 03 · Robo de identidad](03-robo-de-identidad.md) | [Parte 04](../README.md) · [Programa](../../../SYLLABUS.md) | [05 · Contraseñas y autenticación multifactor →](05-contrasenas-y-autenticacion-multifactor.md) |
<!-- gen:footer:end -->
