<!-- meta
part: 3
class: 4
title: "Tarjetas de débito"
level: fundamento
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 04 · Tarjetas de débito

> [← 03 · Cuenta corriente y cheques](03-cuenta-corriente-y-cheques.md) · [Índice de la parte](../README.md) · [05 · Tarjetas de crédito →](05-tarjetas-de-credito.md)

**Parte 03 — Productos y servicios financieros** · **Nivel:** Fundamento — sin conocimientos previos · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Entender qué ocurre en los dos segundos que transcurren entre pasar una tarjeta y recibir la
aprobación, y por qué esa cadena de actores determina tus derechos ante un fraude. La tarjeta de
débito es el medio de pago más usado y el peor comprendido: mueve tu propio dinero, lo que la hace
más barata y, ante un fraude, potencialmente más peligrosa que una de crédito.

Esta clase abre el medio de pago más usado y explica lo que ocurre en los segundos que van del acercamiento de la tarjeta al descuento del saldo. Entenderlo importa por una razón práctica: casi todas las dudas sobre cargos duplicados, retenciones y devoluciones se resuelven sabiendo en qué etapa de esa cadena está la operación.

## 📚 Objetivos

Al finalizar podrás:

1. **Describir** la cadena de una transacción con los cinco actores que intervienen.
2. **Distinguir** autorización, captura y liquidación, y explicar el saldo retenido.
3. **Comparar** débito y crédito en costo, protección y efecto sobre tu flujo.
4. **Aplicar** el protocolo de respuesta ante un cargo no reconocido.
5. **Configurar** los controles que reducen la exposición al fraude.

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

Los cinco primeros términos son los actores y las etapas de la cadena de pago; los tres últimos son los mecanismos de protección y de seguridad. El **saldo retenido** explica la mayoría de las llamadas al servicio al cliente: el dinero está comprometido y todavía no cobrado, y eso no es un error.

| Concepto | Comprensión verificable |
|---|---|
| `emisor` | Banco que emite tu tarjeta y mantiene tu cuenta. Es tu contraparte contractual. |
| `adquirente` | Entidad que afilia al comercio y le abona las ventas. |
| `marca o red` | Sistema que enruta los mensajes entre adquirente y emisor. |
| `autorización` | Verificación en línea de fondos y de reglas de riesgo. Retiene el monto, no lo transfiere. |
| `captura y liquidación` | Proceso posterior en que el dinero efectivamente se mueve, habitualmente en 1–3 días. |
| `saldo retenido` | Monto bloqueado por una autorización aún no capturada. Reduce tu disponible sin figurar como cargo. |
| `contracargo` | Mecanismo por el cual se disputa y eventualmente reversa una operación. |
| `tokenización` | Sustitución del número de tarjeta por un identificador que no sirve fuera de ese contexto. |

## 🧠 Modelo mental

Una transacción viaja por **cinco manos en menos de dos segundos**:

```text
tú → terminal del comercio → adquirente → red (marca) → emisor (tu banco)
                                                            ↓
                                          decisión: aprobar / rechazar
                                                            ↓
                                    vuelve por el mismo camino
```

Cada actor cobra una parte y cada uno tiene reglas propias. Cuando algo sale mal, saber quién es quién
determina a quién reclamar: **tu contraparte es siempre el emisor**, no el comercio ni la marca.

## 📖 Desarrollo

### 1. Autorización, captura y liquidación

Un pago con tarjeta no es un movimiento sino tres, separados en el tiempo y con efectos distintos sobre el saldo. El esquema siguiente los separa.

```text
día 0, 14:32  autorización      se retienen 45 000 de tu disponible
día 0–2       captura           el comercio confirma la venta
día 1–3       liquidación       el dinero sale de tu cuenta y llega al comercio
```

Consecuencias prácticas que explican casi todas las dudas de cartola:

| Situación | Qué ocurre |
|---|---|
| Compra anulada el mismo día | La autorización puede tardar días en liberarse; el disponible sigue reducido |
| Reserva en hotel o arriendo de vehículo | Se autoriza un monto mayor como garantía; se libera al cierre |
| Combustible en autoservicio | Se preautoriza un monto fijo, luego se ajusta al consumo real |
| Cargo duplicado en cartola | Puede ser una autorización no liberada, no un cobro doble |

Antes de reclamar un cargo duplicado, verifica si es una autorización pendiente: la mayoría se libera
sola en 3 a 7 días.

### 2. Débito frente a crédito

Las dos tarjetas se usan igual y protegen distinto. La tabla enfrenta las dimensiones donde la diferencia importa, sobre todo ante un cargo no reconocido.

| Criterio | Débito | Crédito |
|---|---|---|
| Origen de los fondos | Tu cuenta, ahora | Línea del emisor, después |
| Costo si pagas al día | Nulo o comisión baja | Nulo (con cuota de administración) |
| Costo si no pagas | No aplica | Interés rotativo alto |
| Efecto de un fraude | **El dinero ya salió**; se recupera tras la investigación | Se disputa antes de pagar |
| Construcción de historial | No aporta | Aporta si se usa bien |
| Riesgo de sobreendeudamiento | Ninguno | Real |

La fila del fraude es la que decide el uso: para compras en línea o en comercios desconocidos, la
tarjeta de crédito ofrece mejor posición porque el dinero aún no ha salido de tu patrimonio. Para el
gasto cotidiano controlado, el débito evita el riesgo de endeudamiento.

### 3. Protocolo ante un cargo no reconocido

Ante un cargo que no se reconoce hay un orden de actuación que conserva los plazos y las pruebas. Los pasos siguientes son ese orden.

```text
hora 0–2
  1. bloquea la tarjeta desde la aplicación o el canal telefónico
  2. revisa si hay más movimientos no reconocidos
  3. NO respondas llamados, mensajes ni correos que "te ayuden" a resolverlo

hora 2–24
  4. desconoce formalmente ante el EMISOR, por el canal oficial, y guarda el número de caso
  5. solicita el bloqueo definitivo y la reemisión
  6. cambia claves de banca en línea y del correo asociado

día 1–5
  7. presenta los antecedentes que te pidan por escrito
  8. si corresponde, denuncia ante la autoridad competente
  9. registra plazos: la mayoría de las normativas fijan un plazo de respuesta al emisor
```

El paso 3 es crítico: tras un fraude es habitual recibir un contacto que se presenta como del banco
para "revertir la operación". Ese contacto es la segunda fase del mismo fraude. La Parte 4, clase 2,
lo desarrolla en detalle.

### 4. Controles que reducen la exposición

La mayor parte de la exposición se reduce con configuraciones que ya existen en la aplicación de la entidad y que casi nadie activa. La tabla las recoge.

| Control | Efecto | Costo |
|---|---|---|
| Límites diarios por canal (compra, giro, internet) | Acota la pérdida máxima | Ninguno |
| Deshabilitar compras internacionales si no se usan | Elimina un vector completo | Ninguno |
| Notificación instantánea de cada movimiento | Detección en minutos | Ninguno |
| Tarjeta virtual desechable para compras en línea | El número no sirve dos veces | Ninguno, si el emisor lo ofrece |
| Cuenta secundaria con saldo acotado para compras | Limita la exposición al saldo de esa cuenta | Requiere gestión |
| Tokenización en billetera digital | El comercio nunca ve tu número real | Ninguno |

La combinación de límites por canal + notificación instantánea reduce la pérdida esperada más que
cualquier otra medida, y ninguna de las dos cuesta dinero.

### 5. Quién paga qué en la cadena

Cada actor de la cadena cobra una parte de la comisión del comercio, y saber ese reparto explica por qué algunos comercios recargan por pagar con tarjeta.

```text
comercio paga  →  comisión de adquirencia (merchant discount)
                     ↓ se reparte entre
                  tasa de intercambio (al emisor)
                  comisión de la marca
                  margen del adquirente
```

El cliente no ve esta comisión porque está incorporada en el precio. Entenderla explica dos cosas: por
qué algunos comercios ofrecen descuento por pago en efectivo, y por qué el emisor de tu tarjeta gana
dinero aunque no te cobre nada. La Parte 10, clase 10, desarrolla el negocio de adquirencia completo.

## 🧮 Ejemplo guiado

El ejemplo sigue una operación completa desde la autorización hasta la liquidación, con las fechas de cada etapa. Conviene mirar el saldo disponible en cada paso: es donde se ve por qué el dinero desaparece antes de que el comercio cobre.

**Situación.** Sofía revisa su cartola y encuentra tres situaciones el mismo día.

```text
1. dos cargos idénticos de 34 990 en el mismo comercio, con 4 minutos de diferencia
2. un cargo de 128 000 de un comercio en el extranjero que no reconoce
3. su saldo disponible es 260 000 menor que su saldo contable
```

**Paso 1 — clasifica cada situación.**

| # | Hipótesis principal | Acción |
|---|---|---|
| 1 | Reintento tras un rechazo: una autorización quedará sin capturar | Esperar 3–7 días antes de reclamar |
| 2 | Fraude | Protocolo inmediato |
| 3 | Autorizaciones pendientes (reserva, combustible) | Verificar el detalle de retenciones |

**Paso 2 — ejecuta el protocolo para el punto 2.**

```text
14:05  bloquea la tarjeta desde la app
14:07  revisa: no hay más movimientos desconocidos
14:12  desconoce la operación por el canal oficial → caso N.º 88-4412
14:20  solicita reemisión
14:35  cambia clave de banca en línea y del correo asociado
```

**Paso 3 — verifica el punto 1 a los 5 días.** Uno de los dos cargos desapareció: era una
autorización no capturada. **No había cobro duplicado.** Reclamar el día 1 habría generado un caso
innecesario y, en algunos emisores, el bloqueo preventivo de la tarjeta.

**Paso 4 — resuelve el punto 3.** El detalle de retenciones muestra:

```text
reserva de hotel        180 000  (se libera al check-out)
combustible             40 000   (preautorización, ajuste en 48 h)
compra en línea         40 000   (pendiente de captura)
total retenido          260 000  ✔ coincide con la diferencia
```

**Paso 5 — implementa controles.** Tras el fraude, Sofía configura:

```text
límite de compras por internet     150 000 diarios
compras internacionales            deshabilitadas
notificación instantánea           activada para todo monto
tarjeta virtual                    activada para comercios nuevos
```

**Paso 6 — interpreta.** De las tres situaciones, **solo una era un problema real**. La capacidad de
distinguirlas evita dos cosas igualmente costosas: reclamar lo que no corresponde y no reclamar a
tiempo lo que sí. Y la medida más valiosa del día no fue el reclamo, sino los cuatro controles del
paso 5, que reducen la pérdida máxima futura de "todo el saldo" a "150 000".

## 🏦 Del cliente al banco

El cliente ve un pago y el banco ve una comisión de intercambio repartida entre cuatro actores. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| "Pasé la tarjeta" | Mensaje de autorización evaluado por reglas de riesgo en milisegundos | 14, clase 11 |
| Cargo no reconocido | Caso de fraude; puede derivar en contracargo | 12, clase 15 |
| Saldo retenido | Compromiso de fondos aún no liquidado | 10, clase 9 |
| Comisión al comercio | Ingreso de adquirencia e intercambio | 10, clase 10 |
| Límites por canal | Control de riesgo operacional del emisor | 11, clase 7 |

## 🧪 Práctica

El laboratorio pide reconstruir la cronología de una operación con retención y devolución. El ejercicio resuelve de una vez la confusión más frecuente con este producto, que es por qué una devolución tarda más que el cargo.

En `labs/lab-02.md`, sección de medios de pago:

1. Dibuja la cadena de una transacción identificando a los cinco actores con nombres reales.
2. Concilia tu saldo contable con tu disponible identificando cada retención.
3. Redacta tu protocolo personal ante cargo no reconocido, con canales y números.
4. Configura y documenta los controles disponibles en tu emisor.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen situaciones que parecen errores del banco y casi nunca lo son. La causa suele ser la etapa de la cadena en que está la operación.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se reclama un cargo duplicado que no existía | Autorización no capturada | Espera 3–7 días y verifica antes de reclamar. |
| El disponible no coincide con el saldo | Retenciones pendientes | Consulta el detalle de autorizaciones. |
| Se atiende una llamada "del banco" tras un fraude | Segunda fase del mismo fraude | El banco no pide claves; corta y llama tú al canal oficial. |
| Se usa débito para compras en sitios desconocidos | Mayor exposición del dinero propio | Usa crédito o tarjeta virtual para esos casos. |
| Se descubre el fraude semanas después | Sin notificaciones activadas | Activa alertas instantáneas para todo monto. |
| Se reclama al comercio y no al emisor | Contraparte equivocada | Tu contraparte contractual es el emisor. |

## ❓ Preguntas de comprobación

1. Nombra los cinco actores de una transacción con tarjeta y el rol de cada uno.
2. ¿Qué diferencia hay entre autorización, captura y liquidación?
3. ¿Por qué una tarjeta de crédito ofrece mejor posición ante un fraude que una de débito?
4. Describe los tres primeros pasos del protocolo ante un cargo no reconocido.
5. ¿Qué dos controles reducen más la pérdida esperada y cuánto cuestan?

## 📥 Entregable

Guarda en `portfolio/parte-03/clase-04/`:

- el diagrama de la cadena de transacción con los actores reales de tu tarjeta;
- la conciliación de tu saldo contable y disponible con el detalle de retenciones;
- tu protocolo escrito ante cargo no reconocido con canales y plazos;
- la evidencia de los controles configurados en tu emisor.

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

- Committee on Payments and Market Infrastructures (2020). *Payment aspects of financial inclusion*. CPMI/Banco Mundial. Arquitectura de los sistemas de pago minorista. <https://www.bis.org/cpmi/>
- Evans, D. y Schmalensee, R. (2005). *Paying with Plastic: The Digital Revolution in Buying and Borrowing* (2.ª ed.). MIT Press. Economía de las redes de tarjetas y tasas de intercambio.
- Casu, B., Girardone, C. y Molyneux, P. (2021). *Introduction to Banking* (3.ª ed.). Pearson. Capítulo 3: medios de pago y adquirencia.
- PCI Security Standards Council (2022). *PCI DSS v4.0*. Requisitos de seguridad de datos de tarjetas y tokenización. <https://www.pcisecuritystandards.org/>
- World Bank (2017). *Good Practices for Financial Consumer Protection*. Banco Mundial. Responsabilidad ante operaciones no autorizadas.
- Verificación local: revisa la norma de tu país sobre responsabilidad del emisor ante operaciones no reconocidas y los plazos de respuesta (en Chile, Ley 20.009 y sus modificaciones).

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 03 · Cuenta corriente y cheques](03-cuenta-corriente-y-cheques.md) | [Parte 03](../README.md) · [Programa](../../../SYLLABUS.md) | [05 · Tarjetas de crédito →](05-tarjetas-de-credito.md) |
<!-- gen:footer:end -->
