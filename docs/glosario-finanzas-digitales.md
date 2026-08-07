# Glosario de finanzas digitales

Términos de la **Etapa 5**. A diferencia del [glosario general](glosario.md),
cada entrada incluye **qué no significa**: la mayoría de los errores de esta
etapa no vienen de desconocer un término, sino de usarlo como sinónimo de otro.

> Este glosario crece con cada parte publicada. Hoy cubre las Partes 17 y 18.

## Finanzas abiertas

### Banca abierta

- **Definición.** Acceso de terceros autorizados a datos de cuentas e iniciación
  de pagos, con consentimiento del titular.
- **Qué NO significa.** No es «finanzas abiertas»: se limita a cuentas y pagos.
  No es «datos abiertos»: aquí hay dato personal.
- **Ejemplo.** Una aplicación muestra el saldo de las cuentas del cliente en
  cuatro bancos.
- **Riesgo.** Acceso indebido, perfilado, pago no autorizado.
- **Primera clase.** 17.1 · **Otras.** 17.9, 17.10.

### Finanzas abiertas

- **Definición.** Extensión del modelo a todos los productos financieros:
  crédito, seguros, inversiones y previsión.
- **Qué NO significa.** No significa que el cliente pueda compartir con quien
  quiera lo que quiera: el acceso está reglado y el tratamiento, limitado.
- **Ejemplo.** El mismo panel incluye pólizas y fondos.
- **Riesgo.** Inferencia sobre salud, familia y solvencia.
- **Primera clase.** 17.1 · **Otras.** 17.9, 17.12.

### Datos abiertos

- **Definición.** Publicación de datos **no personales** de la entidad: tarifas,
  comisiones, sucursales, requisitos de productos.
- **Qué NO significa.** No requiere consentimiento, porque no hay titular del
  dato distinto de la propia entidad.
- **Ejemplo.** Un comparador de comisiones de cuenta corriente.
- **Riesgo.** Información desactualizada que induce a error.
- **Primera clase.** 17.1.

### Proveedor de servicios de información (AIS)

- **Definición.** Quien accede a datos financieros por cuenta del cliente.
- **Qué NO significa.** No mueve dinero. Confundirlo con un iniciador cambia la
  figura regulatoria, el capital y el régimen de responsabilidad.
- **Ejemplo.** Un agregador de posición consolidada.
- **Riesgo.** Extracción excesiva y concentración.
- **Primera clase.** 17.1 · **Otras.** 17.3, 17.9.

### Proveedor de iniciación de pagos (PIS)

- **Definición.** Quien instruye pagos con cargo a la cuenta del cliente.
- **Qué NO significa.** No custodia fondos y no es un adquirente.
- **Ejemplo.** El botón «pagar desde mi banco» de un comercio.
- **Riesgo.** Pago no autorizado, doble cargo, entrega sin cobro.
- **Primera clase.** 17.1 · **Otras.** 17.10, 17.11.

### Consentimiento

- **Definición.** Acto del cliente que delimita **quién** accede, **a qué**,
  **para qué** y **hasta cuándo**.
- **Qué NO significa.** No es una casilla ni un permiso perpetuo. Y no es lo
  mismo que la base de licitud para tratar el dato.
- **Ejemplo.** Tres alcances concedidos por 12 meses con finalidad declarada.
- **Riesgo.** Fatiga: aceptación mecánica que vacía el acto de contenido.
- **Primera clase.** 17.5 · **Otras.** 17.1, 17.12.

### Alcance (`scope`)

- **Definición.** Unidad mínima de autorización, ligada a **una** finalidad.
- **Qué NO significa.** No es una tabla del modelo de datos: la granularidad
  correcta es la del producto, no la del esquema.
- **Ejemplo.** `accounts:balances` = «ver cuánto dinero hay en cada cuenta».
- **Riesgo.** Alcance sin finalidad: se pide lo que ninguna función usa.
- **Primera clase.** 17.5 · **Otras.** 17.9, 17.12.

### Reciprocidad

- **Definición.** Obligación de compartir que recae sobre quien exige compartir.
- **Qué NO significa.** No es lo mismo que acceso obligatorio: uno obliga a
  abrir, el otro obliga a devolver.
- **Ejemplo.** Un gran agregador que consume datos de todos debe aportar los
  suyos.
- **Riesgo.** Sin ella, aparece el participante que solo extrae.
- **Primera clase.** 17.1 · **Otras.** 17.2.

## Autorización y seguridad

### OAuth 2.x

- **Definición.** Marco de **autorización** delegada: permite acceder a un
  recurso sin compartir la credencial del titular.
- **Qué NO significa.** **No es un protocolo de autenticación.** Un token de
  acceso demuestra que alguien autorizó algo, no quién está delante.
- **Ejemplo.** El flujo de código con PKCE.
- **Riesgo.** Usarlo para autenticar produce suplantación.
- **Primera clase.** 17.6 · **Otras.** 17.7.

### OpenID Connect

- **Definición.** Capa de **autenticación** sobre OAuth: añade un token de
  identidad firmado con quién es el usuario y cómo se autenticó.
- **Qué NO significa.** No sustituye al token de acceso ni concede permisos.
- **Ejemplo.** `sub`, `acr` y `amr` para comprobar el nivel de autenticación.
- **Riesgo.** Aceptarlo sin verificar firma, `iss`, `aud`, `exp` y `nonce`.
- **Primera clase.** 17.6.

### PKCE

- **Definición.** Prueba de posesión que liga el código de autorización a quien
  lo pidió (RFC 7636).
- **Qué NO significa.** No es opcional en clientes públicos, y no sustituye a la
  validación exacta de `redirect_uri`.
- **Ejemplo.** `code_challenge = S256(code_verifier)`.
- **Riesgo.** Sin él, una aplicación maliciosa canjea un código interceptado.
- **Primera clase.** 17.6 · **Otras.** 17.7.

### FAPI

- **Definición.** Perfil de seguridad de grado financiero sobre OAuth y OpenID
  Connect, publicado por la OpenID Foundation.
- **Qué NO significa.** No es un estándar de API: restringe uno existente.
- **Ejemplo.** Exigir prueba de posesión y objeto de petición firmado.
- **Riesgo.** Citar «FAPI» sin decir versión: los perfiles cambian.
- **Primera clase.** 17.7.

### mTLS

- **Definición.** Autenticación mutua en la capa de transporte: ambos extremos
  presentan certificado.
- **Qué NO significa.** No protege la **intención**: un importe no firmado puede
  alterarse antes de entrar al canal.
- **Ejemplo.** Token ligado al certificado del canal (RFC 8705).
- **Riesgo.** Terminación de TLS en un balanceador rompe la ligadura.
- **Primera clase.** 17.7.

### DPoP

- **Definición.** Prueba de posesión en la capa de aplicación, con una clave del
  cliente (RFC 9449).
- **Qué NO significa.** No identifica a la **entidad**, solo al poseedor de la
  clave.
- **Ejemplo.** Token que solo sirve acompañado de una firma del cliente.
- **Riesgo.** Sin almacén de `jti`, no hay protección contra repetición.
- **Primera clase.** 17.7.

### Token al portador

- **Definición.** Credencial que sirve a quien la tenga.
- **Qué NO significa.** No prueba que quien la presenta sea su titular.
- **Ejemplo.** Un `access_token` sin ligadura a canal ni a clave.
- **Riesgo.** Una fuga en un registro o en un proxy da acceso pleno.
- **Primera clase.** 17.7 · **Otras.** 17.6.

## Contrato e integración

### Idempotencia

- **Definición.** Propiedad por la que repetir la petición no repite el efecto.
- **Qué NO significa.** No es «no hacer nada la segunda vez»: es devolver **la
  misma respuesta** de la primera.
- **Ejemplo.** `Idempotency-Key` con huella canónica del cuerpo y bloqueo.
- **Riesgo.** Sin bloqueo por clave, falla justo bajo concurrencia.
- **Primera clase.** 17.8 · **Otras.** 17.10.

### Paginación por cursor

- **Definición.** Recorrido estable sobre un orden **total**, codificado en un
  cursor opaco.
- **Qué NO significa.** No es `offset` con otro nombre: `offset` repite y omite
  filas cuando llegan datos nuevos.
- **Ejemplo.** `(booking_date DESC, transaction_id DESC)`.
- **Riesgo.** Sin desempate por identificador, tiene el defecto del `offset`.
- **Primera clase.** 17.8 · **Otras.** 17.9.

### Cambio compatible

- **Definición.** Cambio tras el cual un cliente escrito contra la versión
  anterior sigue funcionando **sin tocar una línea**.
- **Qué NO significa.** «Aditivo» no implica compatible: añadir un valor a un
  enumerado de respuesta rompe al integrador que hizo un `switch` exhaustivo.
- **Ejemplo.** Añadir un campo opcional a la respuesta.
- **Riesgo.** Clasificarlo mal rompe código ajeno en producción.
- **Primera clase.** 17.8.

### Depreciación

- **Definición.** Retirada anunciada de una versión, con fecha publicada en la
  propia respuesta.
- **Qué NO significa.** No es apagar en la fecha pase lo que pase: hay regla de
  parada por volumen.
- **Ejemplo.** Cabeceras `Deprecation` y `Sunset` (RFC 8594).
- **Riesgo.** Apagar con volumen vivo es un incidente programado.
- **Primera clase.** 17.8.

## Pagos

### Orden de pago

- **Definición.** Instrucción autorizada por el cliente.
- **Qué NO significa.** No es el pago: el pago es su ejecución.
- **Ejemplo.** Una orden por `Idempotency-Key`, con importe y beneficiario.
- **Riesgo.** Confundirla con el pago produce duplicados al reintentar.
- **Primera clase.** 17.10.

### Firmeza

- **Definición.** Punto a partir del cual el pago no puede revertirse
  unilateralmente.
- **Qué NO significa.** No es «aceptado». Entre aceptación y liquidación puede
  haber horas o días.
- **Ejemplo.** El comercio entrega con `liquidado`, no con `aceptado`.
- **Riesgo.** Entregar en aceptación: mercancía entregada sin cobro.
- **Primera clase.** 17.10 · **Otras.** 18.7 (prevista).

### Confirmación de fondos

- **Definición.** Respuesta booleana sobre si hay saldo suficiente en el
  instante de la consulta.
- **Qué NO significa.** No retiene, no garantiza y no devuelve el saldo.
- **Ejemplo.** `{ "funds_available": true }`.
- **Riesgo.** Repetirla con importes decrecientes deduce el saldo por bisección.
- **Primera clase.** 17.10.

### Autenticación reforzada

- **Definición.** Verificación con al menos dos factores de categorías distintas
  **e independientes**.
- **Qué NO significa.** «Contraseña + SMS al mismo teléfono» puede no serlo: un
  solo compromiso rompe los dos factores.
- **Ejemplo.** Contraseña más firma con clave del elemento seguro.
- **Riesgo.** Contar categorías sin comprobar independencia.
- **Primera clase.** 17.11.

### Vinculación dinámica

- **Definición.** El código de autenticación se calcula sobre el **importe y el
  beneficiario** de la operación.
- **Qué NO significa.** No basta con mostrar el importe: hay que ligarlo al
  código.
- **Ejemplo.** «Confirma 45.000 a JUAN PEREZ, código 481920».
- **Riesgo.** Sin ella, un código robado autoriza otra operación.
- **Primera clase.** 17.11.

## Pagos transfronterizos

### Pago transfronterizo

- **Definición.** Pago en que ordenante y beneficiario están en jurisdicciones
  distintas, de modo que **ningún sistema único liquida las dos patas**.
- **Qué NO significa.** No es «pago a larga distancia» ni implica cambio de
  divisa. Mover dólares entre dos cuentas propias en dos países lo es; comprar
  euros en el banco de la esquina no lo es.
- **Ejemplo.** Una empresa chilena paga a un proveedor vietnamita.
- **Riesgo.** Coste opaco, plazo indeterminado, pérdida en tránsito.
- **Primera clase.** 18.1 · **Otras.** 18.2, 18.16.

### Remesa

- **Definición.** Transferencia de persona a persona, típicamente de un
  trabajador migrante a su hogar.
- **Qué NO significa.** No es «un pago pequeño»: es un ingreso familiar, y por
  eso su elasticidad al coste es distinta de la de un pago comercial.
- **Ejemplo.** 300 dólares mensuales de un país a otro, retirados en efectivo.
- **Riesgo.** Coste alto empuja al canal informal, sin protección ni registro.
- **Primera clase.** 18.10 · **Otras.** 18.1, 18.13.

### Corresponsalía

- **Definición.** Relación por la que un banco presta a otro acceso a su plaza,
  su moneda y su sistema de pagos.
- **Qué NO significa.** No es una conexión técnica: es un **crédito y una
  responsabilidad**. El corresponsal responde ante su supervisor por operaciones
  de clientes que nunca ha visto.
- **Ejemplo.** Un banco chileno con cuenta en dólares en Nueva York.
- **Riesgo.** Banca anidada, retirada de relaciones, concentración.
- **Primera clase.** 18.3 · **Otras.** 18.4, 18.12.

### Nostro y vostro

- **Definición.** La **misma cuenta** vista desde los dos lados: nostro es
  «nuestra cuenta en vuestro banco»; vostro, «vuestra cuenta en el nuestro».
- **Qué NO significa.** El prefijo no indica dónde está la cuenta, sino **de
  quién es el dinero**.
- **Ejemplo.** Un pago produce un cargo en un libro y un abono en el otro, por
  el mismo importe y la misma fecha valor.
- **Riesgo.** Descuadres que tardan semanas en resolverse.
- **Primera clase.** 18.4 · **Otras.** 18.8.

### Finalidad

- **Definición.** Momento en que una transferencia es **irrevocable e
  incondicional**.
- **Qué NO significa.** No la da el mensaje, ni el aviso al beneficiario, ni el
  apunte contable, ni que el dinero «se vea» en la cuenta. La da la norma.
- **Ejemplo.** La anotación en la cuenta del banco central, cuando la ley se la
  atribuye.
- **Riesgo.** Abonar antes de la finalidad es conceder crédito sin saberlo.
- **Primera clase.** 18.7 · **Otras.** 18.15, 17.10.

### ISO 20022

- **Definición.** Norma de mensajería financiera con un diccionario común y
  campos estructurados.
- **Qué NO significa.** No es «un formato nuevo» ni acelera la liquidación:
  actúa en la capa de mensajería.
- **Ejemplo.** `pacs.008` para una transferencia de cliente; `pacs.004` para su
  devolución.
- **Riesgo.** Un campo en el sitio equivocado convierte un pago automático en
  una cola manual.
- **Primera clase.** 18.6 · **Otras.** 18.11, 18.12.

### Deudor último

- **Definición.** Persona **por cuenta de la cual** se paga, cuando no coincide
  con el titular de la cuenta de cargo.
- **Qué NO significa.** No es el ordenante técnico. Omitirlo no rompe el
  esquema: rompe el screening.
- **Ejemplo.** Una gestora paga la factura de la empresa que administra.
- **Riesgo.** Hallazgo de auditoría y screening incompleto.
- **Primera clase.** 18.6 · **Otras.** 18.12.

### Diferencial de cambio

- **Definición.** Diferencia entre el tipo aplicado y el de referencia, medida
  **sobre la magnitud que el cliente recibe**.
- **Qué NO significa.** No es la diferencia sobre la cotización inversa: si el
  banco cotiza pesos por dólar y el cliente compra dólares, medir sobre la
  cotización da un número distinto del que el cliente pierde.
- **Ejemplo.** 286,3 pb con tipo aplicado 978 y referencia 950.
- **Riesgo.** Es la mitad del coste de una remesa y no aparece como comisión.
- **Primera clase.** 18.9 · **Otras.** 18.1, 18.10.

### Regla del viaje

- **Definición.** Obligación de que ciertos datos del ordenante y del
  beneficiario **acompañen** a la transferencia.
- **Qué NO significa.** No es prevención de lavado ni sanciones: es una
  obligación de datos, con su propia consecuencia si falta.
- **Ejemplo.** Nombre y cuenta del ordenante conservados por el intermediario.
- **Riesgo.** El intermediario trunca campos y el destino no puede aplicar ni
  justificar el pago.
- **Primera clase.** 18.12 · **Otras.** 18.6, 18.14.

### Payment versus Payment

- **Definición.** Mecanismo por el que **ninguna pata se liquida si la otra no
  se liquida**.
- **Qué NO significa.** No elimina el riesgo de reposición, ni el de liquidez,
  ni el operacional del coordinador. Protege el principal, no el precio.
- **Ejemplo.** Bloqueo en dos sistemas, comprobación y liberación conjunta.
- **Riesgo.** Concentra en un liquidador lo que antes era bilateral.
- **Primera clase.** 18.15 · **Otras.** 18.7, 21.15.

### Riesgo Herstatt

- **Definición.** Riesgo de liquidación en operaciones de cambio por la falta de
  simultaneidad entre husos horarios.
- **Qué NO significa.** No es riesgo de mercado: es riesgo de entregar y no
  recibir.
- **Ejemplo.** Se entregan marcos por la mañana europea y no llegan los dólares
  de la tarde neoyorquina.
- **Riesgo.** Pérdida del principal completo.
- **Primera clase.** 18.7 · **Otras.** 18.15.

### Exposición máxima simultánea

- **Definición.** Mayor importe expuesto a la vez, sumando todas las operaciones
  vivas en cada instante.
- **Qué NO significa.** No es la operación mayor. Tres operaciones de 40, 25 y
  30 solapadas exponen 95, no 40.
- **Ejemplo.** El límite de contraparte se consume por esta cifra.
- **Riesgo.** Subestimarla deja el límite mal calibrado.
- **Primera clase.** 18.15 · **Otras.** 18.8.

### Enlace de pagos inmediatos

- **Definición.** Conexión entre dos sistemas nacionales que liquidan en
  segundos, de modo que un pago internacional sean dos pagos domésticos con un
  cambio de divisa en medio.
- **Qué NO significa.** No resuelve el cumplimiento, ni la protección al
  consumidor, ni las disputas, ni la última milla. De los seis problemas de un
  enlace, **solo uno es técnico**.
- **Ejemplo.** Un corredor que baja del 7,9 % al 1,1 % para el 71 % de los
  pagos.
- **Riesgo.** Mejora al 71 % y puede **empeorar** al 29 % que queda fuera.
- **Primera clase.** 18.13 · **Otras.** 18.10, 18.14.

## Datos y privacidad

### Base de licitud

- **Definición.** Fundamento jurídico que habilita un tratamiento.
- **Qué NO significa.** No es lo mismo que consentimiento: el consentimiento es
  **una** de las bases posibles.
- **Ejemplo.** Ejecución de contrato, obligación legal, interés legítimo.
- **Riesgo.** Suponer que el acceso concedido habilita cualquier uso.
- **Primera clase.** 17.12.

### Minimización

- **Definición.** Tratar solo el dato necesario para la finalidad declarada.
- **Qué NO significa.** No es solo «menos campos»: también menor granularidad,
  menor precisión, agregación y seudonimización.
- **Ejemplo.** Descartar los campos de contraparte en la ingesta.
- **Riesgo.** «Por si sirve después» no es una finalidad.
- **Primera clase.** 17.12 · **Otras.** 17.4, 17.9.

### Dato inferido

- **Definición.** Atributo deducido que el titular nunca declaró.
- **Qué NO significa.** No es un dato derivado: el derivado se recalcula, el
  inferido el cliente ni siquiera sabe que existe.
- **Ejemplo.** Deducir estructura familiar de un gasto recurrente.
- **Riesgo.** No es corregible ni contestable si no se hace explicable.
- **Primera clase.** 17.4 · **Otras.** 17.12.

### Anonimización

- **Definición.** Transformación **no reversible** que elimina la posibilidad de
  reidentificar.
- **Qué NO significa.** No es seudonimización. Si se puede revertir, sigue
  siendo dato personal.
- **Ejemplo.** Agregados con umbral mínimo de celda y ruido calibrado.
- **Riesgo.** Celdas pequeñas permiten reidentificar por diferencia.
- **Primera clase.** 17.12 · **Otras.** 17.4.

## Operación

### SLI, SLO y SLA

- **Definición.** Indicador medido, objetivo interno y compromiso contractual.
- **Qué NO significa.** No son intercambiables, y el SLA debe ser **más laxo**
  que el SLO.
- **Ejemplo.** SLI: peticiones correctas bajo 2 s; SLO 99,5 %; SLA 99,0 %.
- **Riesgo.** Igualarlos hace que cada desviación sea un incumplimiento y el
  equipo deje de reportar la verdad.
- **Primera clase.** 17.13.

### Presupuesto de error

- **Definición.** Fallo admisible dentro del objetivo, usado para **decidir**.
- **Qué NO significa.** No es un informe. Y medirlo en minutos de incidente
  oculta el goteo continuo de errores.
- **Ejemplo.** 0,5 % de 412 millones de peticiones = 2,06 millones admisibles.
- **Riesgo.** Elegir la métrica equivocada esconde la mitad del problema.
- **Primera clase.** 17.13.

### Proveedor tecnológico crítico

- **Definición.** Proveedor cuya caída afecta simultáneamente a varios
  participantes del ecosistema.
- **Qué NO significa.** No tiene relación contractual con el cliente y no
  aparece en su panel de consentimientos. Eso no lo hace menos importante.
- **Ejemplo.** Quien opera la conexión de cuarenta entidades.
- **Riesgo.** Un punto de fallo invisible en el mapa de riesgo.
- **Primera clase.** 17.2 · **Otras.** 17.13.

---

**Ver también:** [Glosario general](glosario.md) ·
[Etapa 5](etapa-5-finanzas-digitales.md) ·
[Mapa de finanzas abiertas](mapa-finanzas-abiertas.md)
