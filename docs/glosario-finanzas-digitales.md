# Glosario de finanzas digitales

Términos de la **Etapa 5**. A diferencia del [glosario general](glosario.md),
cada entrada incluye **qué no significa**: la mayoría de los errores de esta
etapa no vienen de desconocer un término, sino de usarlo como sinónimo de otro.

> Este glosario crece con cada parte publicada. Hoy cubre las Partes 17 a 20.

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

## Registro distribuido

### Registro distribuido

- **Definición.** Registro replicado y sincronizado que permite a partes que no
  confían entre sí ni en un tercero común mantener un estado que **ninguna
  controla**.
- **Qué NO significa.** No significa «base de datos moderna». Su única propiedad
  distintiva se paga con redundancia total, lentitud e irreversibilidad.
- **Ejemplo.** Un consorcio sin tercero neutral aceptable por todos.
- **Riesgo.** Pagar el precio sin obtener el beneficio, que es lo que ocurre
  cuando sí existe un tercero de confianza disponible.
- **Primera clase.** 19.1 · **Otras.** 19.7, 19.14.

### Fallo bizantino

- **Definición.** Nodo que **responde**, y responde mal: puede mentir,
  contradecirse o decir cosas distintas a distintos interlocutores.
- **Qué NO significa.** No es un nodo caído. Con caídas el silencio es
  información; con bizantinos ninguna respuesta individual lo es.
- **Ejemplo.** Tolerar `f` bizantinos exige `3f + 1` nodos, no `2f + 1`.
- **Riesgo.** Diseñar para caídas y encontrarse un fallo bizantino.
- **Primera clase.** 19.1 · **Otras.** 19.5.

### Independencia efectiva

- **Definición.** Número de nodos que **no fallan a la vez**, frente al número de
  nodos que hay.
- **Qué NO significa.** No es el recuento. Siete nodos con el mismo software, el
  mismo proveedor o la misma jurisdicción son, para el fallo que importa, uno.
- **Ejemplo.** Un esquema 4-de-7 con siete módulos del mismo proveedor tolera
  cero fallos de ese proveedor.
- **Riesgo.** Un umbral que protege sobre el papel y no en la práctica.
- **Primera clase.** 19.5 · **Otras.** 19.3, 19.11.

### Finalidad determinística

- **Definición.** Garantía del protocolo de que, cerrada la ronda, la operación
  no revierte.
- **Qué NO significa.** No es finalidad jurídica. Y vale **cero** si el supuesto
  de seguridad —menos de un tercio defectuoso— no se sostiene.
- **Ejemplo.** Una red no designada con finalidad perfecta y sin protección
  frente a un concurso.
- **Riesgo.** Contabilizar como firme lo que no lo es.
- **Primera clase.** 19.6 · **Otras.** 18.7, 22.7.

### Reorganización

- **Definición.** Sustitución de bloques ya difundidos por una cadena
  alternativa.
- **Qué NO significa.** No es necesariamente un ataque: la mayoría son el
  funcionamiento normal de un sistema distribuido.
- **Ejemplo.** Dos nodos proponen casi a la vez.
- **Riesgo.** Tratarla como incidente de seguridad y parar el servicio cada vez.
- **Primera clase.** 19.6.

### Contrato inteligente

- **Definición.** Código que se ejecuta sobre el registro y controla activos.
- **Qué NO significa.** **No es un contrato** —no expresa consentimiento ni
  tiene remedios— y **no es inteligente**: ejecuta lo escrito, incluido el error.
- **Ejemplo.** Un depósito en garantía con máquina de estados e invariantes.
- **Riesgo.** Reentrada, control de acceso ausente, clave de actualización única.
- **Primera clase.** 19.8 · **Otras.** 19.13, 21.3.

### Reentrada

- **Definición.** Una llamada externa vuelve al contrato antes de que este haya
  actualizado su estado.
- **Qué NO significa.** No es un fallo del registro: es un fallo del programa
  que corre sobre él.
- **Ejemplo.** Transferir antes de poner el saldo a cero.
- **Riesgo.** El contrato se vacía.
- **Primera clase.** 19.8.

### Oráculo

- **Definición.** Mecanismo que introduce en el registro un dato del exterior.
- **Qué NO significa.** No elimina la confianza: **es un tercero de confianza**,
  y su presencia reabre la pregunta de si hacía falta el registro.
- **Ejemplo.** Mediana de cinco fuentes con banda de descarte y mínimo de
  fuentes vivas.
- **Riesgo.** Con media en vez de mediana, una sola fuente mueve el resultado.
- **Primera clase.** 19.9 · **Otras.** 19.11, 21.12.

### Puente

- **Definición.** Mecanismo que representa en un registro un activo de otro.
- **Qué NO significa.** El activo **no se mueve**: se inmoviliza en origen y se
  emite una representación en destino. El envuelto no es el original: es un
  derecho frente al custodio.
- **Ejemplo.** Un conjunto de validadores que firma que el bloqueo ocurrió.
- **Riesgo.** Umbral efectivo menor que el nominal; sin derecho de canje.
- **Primera clase.** 19.11 · **Otras.** 20.5.

### Disponibilidad de datos

- **Definición.** Garantía de que existen los datos necesarios para verificar el
  estado y para poder salir.
- **Qué NO significa.** No es «el servicio está arriba». Es la diferencia real
  entre una segunda capa que hereda la seguridad de la base y una que no.
- **Ejemplo.** Si el operador no publica los datos, el usuario no puede
  construir la prueba para retirar sus fondos.
- **Riesgo.** Una segunda capa sin salida es un custodio con otro nombre.
- **Primera clase.** 19.12.

### Valor extraíble del orden

- **Definición.** Beneficio que obtiene quien decide el orden de las operaciones.
- **Qué NO significa.** No aparece como comisión: aparece como un peor precio.
- **Ejemplo.** Adelantarse a una operación visible en la mempool.
- **Riesgo.** Distorsiona la formación de precios sin que nadie lo vea.
- **Primera clase.** 19.12 · **Otras.** 21.14.

### Compensación (frente a reversión)

- **Definición.** Corregir el efecto de un error **añadiendo** una operación, en
  vez de reescribir la historia.
- **Qué NO significa.** No es deshacer. La historia conserva el error y su
  corrección, que es lo que permite auditarla.
- **Ejemplo.** Es la respuesta contable y, por la misma razón, la correcta aquí.
- **Riesgo.** Revertir una vez destruye la propiedad que justificaba el sistema.
- **Primera clase.** 19.13.

## Activos digitales y dinero

### Activo digital

- **Definición.** Cualquier representación digital de valor o de un derecho.
- **Qué NO significa.** No es sinónimo de criptoactivo: un apunte en la base de
  datos de un banco también lo es. Y **no dice nada sobre la promesa**, que es lo
  único que clasifica.
- **Ejemplo.** Un depósito, una milla de fidelización y un criptoactivo son los
  tres activos digitales.
- **Riesgo.** Agrupar por el soporte instrumentos con regímenes opuestos.
- **Primera clase.** 20.1 · **Otras.** 20.8, 20.15.

### Token

- **Definición.** Unidad de anotación en un registro.
- **Qué NO significa.** **No es un tipo de activo.** Es un contenedor, igual que
  «fila de una tabla» no es un tipo de contrato.
- **Ejemplo.** Un depósito tokenizado y un criptoactivo no respaldado son ambos
  tokens y no se parecen en nada.
- **Riesgo.** La palabra sugiere parentesco entre instrumentos que no lo tienen.
- **Primera clase.** 20.1 · **Otras.** 20.8.

### Paridad de derecho

- **Definición.** Obligación contractual del emisor de entregar el importe
  nominal por unidad.
- **Qué NO significa.** No es el precio observado. Puede haber paridad de derecho
  con el mercado cotizando a 0,97, y ambas cosas ser ciertas a la vez.
- **Ejemplo.** El emisor redime a 1,00 a los grandes mientras el minorista solo
  puede vender a 0,994.
- **Riesgo.** Suponer un derecho que el umbral de redención no concede.
- **Primera clase.** 20.3 · **Otras.** 20.5, 20.9.

### Banda de no arbitraje

- **Definición.** Rango de precio dentro del cual corregir el desvío no compensa.
- **Qué NO significa.** No es un margen de tolerancia elegido: la fija el diseño
  del emisor mediante su comisión, su plazo y su mínimo.
- **Ejemplo.** Con 12,9 puntos básicos de coste, la banda es 0,99871 – 1,00129.
- **Riesgo.** Sin calcularla, se confunde ruido con crisis, y al revés.
- **Primera clase.** 20.3 · **Otras.** 20.6.

### Participante autorizado

- **Definición.** Quien puede emitir y redimir directamente contra el emisor.
- **Qué NO significa.** No es un detalle operativo: **su número es un dato de
  riesgo tan importante como la composición de las reservas**, porque si se
  retiran, el arbitraje se detiene aunque las reservas estén intactas.
- **Ejemplo.** Siete participantes, de los que dos hacen el 61 % del volumen.
- **Riesgo.** Dos puntos únicos de fallo en el mecanismo que sostiene el precio.
- **Primera clase.** 20.3 · **Otras.** 20.6, 20.16.

### Cobertura líquida

- **Definición.** Parte de la reserva convertible en efectivo en un plazo dado.
- **Qué NO significa.** No es la cobertura contable. La primera puede ser del
  102 % y la segunda del 73 % sin que nadie haya mentido.
- **Ejemplo.** Tras una redención del 35 %, la contable sube al 103,5 % y la
  líquida cae al 78,9 %.
- **Riesgo.** La cifra publicada se mueve en dirección contraria al riesgo real.
- **Primera clase.** 20.4 · **Otras.** 20.6, 20.16.

### Atestación

- **Definición.** Informe de un profesional sobre una afirmación de la dirección,
  **en una fecha concreta**.
- **Qué NO significa.** No es una auditoría de estados financieros. No dice nada
  del día anterior ni del siguiente, y puede excluir la valoración o la
  titularidad.
- **Ejemplo.** «A 30 de junio, los saldos declarados coinciden con los extractos.»
- **Riesgo.** Aceptar «auditado» como sinónimo y no preguntar el alcance.
- **Primera clase.** 20.4.

### Comisión antidilución

- **Definición.** Cargo que traslada a quien redime el coste real de realizar los
  activos.
- **Qué NO significa.** No es una penalización por salir: sin ella, ese coste lo
  pagan **los que se quedan**, y ese traslado es el premio por salir primero.
- **Ejemplo.** Realizar 900 millones cuesta 10 millones: un 1,112 % sobre lo
  pagado.
- **Riesgo.** Externalizar el coste crea el incentivo a correr.
- **Primera clase.** 20.5.

### Prorrateo

- **Definición.** Reparto de la liquidez disponible en la misma fracción para
  todos los solicitantes de una ventana.
- **Qué NO significa.** No es una restricción a la salida: es lo que hace que ser
  el primero **no valga nada**, y por tanto que solicite quien necesita el dinero.
- **Ejemplo.** 900 millones para 1 800 millones solicitados: todos cobran el 50 %.
- **Riesgo.** Sin tramo mínimo íntegro, deja sin efectivo a quien lo necesita de
  verdad.
- **Primera clase.** 20.5.

### Punto de no retorno

- **Definición.** Redención acumulada a partir de la cual la venta forzada
  consume el margen de sobrecolateralización.
- **Qué NO significa.** No se calcula con un descuento constante: con escalera
  creciente aparece, y sin ella parece no existir.
- **Ejemplo.** Con un margen del 1,45 %, se alcanza al redimir el 77 % del
  circulante.
- **Riesgo.** Vigilar la cobertura en vez de la redención acumulada.
- **Primera clase.** 20.6 · **Otras.** 20.4, 20.16.

### Respaldo endógeno

- **Definición.** Colateral formado por un activo del propio sistema.
- **Qué NO significa.** No es sobrecolateralización. La diferencia es si el
  colateral pierde valor exactamente cuando hace falta: si lo hace, no absorbe,
  **amplifica**.
- **Ejemplo.** Un token estable respaldado por el token de gobernanza del mismo
  protocolo.
- **Riesgo.** Toda la cobertura vale cero en el único escenario en que importa.
- **Primera clase.** 20.7 · **Otras.** 20.1.

### Rendimiento por dilución

- **Definición.** Pago financiado emitiendo unidades nuevas en lugar de con
  ingresos.
- **Qué NO significa.** No es un rendimiento: es una transferencia de los que
  entran después a los que entraron antes.
- **Ejemplo.** Se pagan 240 millones con 42 millones de ingresos reales: el
  82,5 % es dilución.
- **Riesgo.** Atrae depósitos, y con ellos crece el tamaño del día de la salida.
- **Primera clase.** 20.7.

### Depósito tokenizado

- **Definición.** Un depósito bancario anotado en un registro programable.
- **Qué NO significa.** **No es una moneda del banco ni una stablecoin
  bancaria.** Conserva el obligado, la garantía de depósitos, el encaje y el
  capital: el registro cambia cómo se transfiere, no qué es.
- **Ejemplo.** Un pago que se liquida el domingo y se salda en el banco central
  al abrir.
- **Riesgo.** Operar 24/7 genera crédito intradía entre bancos que hay que
  limitar.
- **Primera clase.** 20.8 · **Otras.** 20.10, 20.11.

### Singularidad del dinero

- **Definición.** Que una unidad valga lo mismo con independencia del banco que
  la debe.
- **Qué NO significa.** No es automática: la sostienen la conversión a la par, la
  liquidación interbancaria en dinero de banco central y la supervisión común.
- **Ejemplo.** Nadie cotiza «pesos del banco A» frente a «pesos del banco B».
- **Riesgo.** Si cada banco emitiera un token negociable, aparecería un descuento
  por banco: un sistema monetario peor, no más moderno.
- **Primera clase.** 20.8 · **Otras.** 20.10.

### Dinero electrónico

- **Definición.** Valor almacenado, emitido contra la recepción de fondos y
  aceptado como pago por terceros.
- **Qué NO significa.** No es una stablecoin ni un depósito. Su régimen **prohíbe
  remunerar el saldo** y exige redención a la par y salvaguarda de fondos.
- **Ejemplo.** El saldo de una entidad autorizada de dinero electrónico.
- **Riesgo.** Un producto que cumple los tres elementos lo es aunque se llame
  token, y descubrirlo tarde es caro.
- **Primera clase.** 20.9 · **Otras.** 20.1.

### Salvaguarda de fondos

- **Definición.** Segregación de los fondos recibidos en cuenta separada o
  cobertura equivalente.
- **Qué NO significa.** No basta con abrir una cuenta aparte: sin **renuncia
  expresa del banco depositario a compensar** con deudas del emisor, la
  salvaguarda se evapora.
- **Ejemplo.** Cuenta a nombre de «Fintech S.A. — cuenta de clientes», con
  conciliación diaria.
- **Riesgo.** El punto que suele fallar es la renuncia a compensar.
- **Primera clase.** 20.9.

### CBDC

- **Definición.** Pasivo del banco central en forma digital.
- **Qué NO significa.** No es una criptomoneda —hay emisor y es soberano—, ni una
  stablecoin —no hay reserva: **es** la reserva—, ni un depósito.
- **Ejemplo.** Un saldo minorista con límite de tenencia, distribuido por
  intermediarios en un modelo de dos niveles.
- **Riesgo.** Un límite de tenencia retrasa una corrida; no la evita.
- **Primera clase.** 20.10 · **Otras.** 20.8.

### Dinero programable

- **Definición.** Restricción adherida a la unidad monetaria, que viaja con ella.
- **Qué NO significa.** **No es un pago programable.** La prueba: cuando el
  dinero llega al destinatario, ¿sigue llevando la restricción? Si sí, es dinero
  programable y rompe la fungibilidad.
- **Ejemplo.** Un saldo que solo puede gastarse en comercios de una lista.
- **Riesgo.** Aparece un descuento, un mercado gris y una pérdida que soporta el
  beneficiario peor situado.
- **Primera clase.** 20.11.

### Fungibilidad

- **Definición.** Que una unidad sea intercambiable por otra sin distinción.
- **Qué NO significa.** No es una propiedad técnica del registro: la destruyen las
  restricciones adheridas a la unidad, aunque el registro las trate igual.
- **Ejemplo.** 180 000 con restricción de destino se cambian por 144 000 libres.
- **Riesgo.** El descuento es el síntoma; para cuando se ve, el daño ya ocurrió.
- **Primera clase.** 20.11.

### Independencia efectiva

- **Definición.** Número de guardianes que un solo evento no puede dejar
  inoperativos a la vez.
- **Qué NO significa.** No es el número de guardianes. Cinco con el mismo
  proveedor son uno, y un «3 de 5» puede tener independencia efectiva 1.
- **Ejemplo.** Tres directivos en la misma oficina alcanzan por sí solos un
  umbral de 3.
- **Riesgo.** La probabilidad de bloqueo supone independencia; sin ella, la cifra
  es falsa.
- **Primera clase.** 20.12 · **Otras.** 19.5.

### Segregación jurídica

- **Definición.** Que el activo custodiado no forme parte del patrimonio del
  custodio.
- **Qué NO significa.** No es la segregación operativa. Un custodio puede llevar
  direcciones separadas por cliente y, aun así, si el contrato dice que el activo
  es suyo, el cliente es acreedor ordinario en el concurso.
- **Ejemplo.** Cláusulas de propiedad, no pignoración y verificación
  independiente del saldo total.
- **Riesgo.** Ningún esquema criptográfico protege de la quiebra del custodio.
- **Primera clase.** 20.12 · **Otras.** 20.15.

### Profundidad

- **Definición.** Importe absorbible sin que el precio se mueva más de un umbral
  dado.
- **Qué NO significa.** **No es el volumen.** El volumen se publica y puede
  inflarse sin coste; la profundidad hay que medirla sobre el libro.
- **Ejemplo.** Volumen diario de 184 millones y profundidad al 1 % de 2,08
  millones.
- **Riesgo.** Calibrar el límite de posición con el dato equivocado.
- **Primera clase.** 20.13.

### Exposición indirecta

- **Definición.** Riesgo por un instrumento a través de contrapartes expuestas a
  él.
- **Qué NO significa.** No es una estimación fina: el traslado lineal de pérdidas
  sirve para **ordenar** contrapartes, no para predecir importes.
- **Ejemplo.** Exposición directa cero y 38 millones de crédito en riesgo.
- **Riesgo.** Reportar «cero» es cierto y completamente inútil.
- **Primera clase.** 20.14.

### Dependencia común

- **Definición.** Proveedor o infraestructura compartida por varias entidades.
- **Qué NO significa.** No es una contraparte financiera y no aparece en ningún
  balance. Un fallo suyo puede producir el mismo efecto que una caída del 60 %
  del activo, sin que el activo se mueva.
- **Ejemplo.** Tres contrapartes que usan el mismo proveedor de precios.
- **Riesgo.** Es el canal de contagio menos visible y el que más sorprende.
- **Primera clase.** 20.14 · **Otras.** 17.2.

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
[Mapa de finanzas abiertas](mapa-finanzas-abiertas.md) ·
[Mapa de activos digitales](mapa-activos-digitales.md)
