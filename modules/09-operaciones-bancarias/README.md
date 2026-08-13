# Parte 10: Operaciones bancarias

La Parte 9 evaluó el crédito. Esta sale del crédito y recorre todo lo demás que
hace un banco todos los días: captar, pagar, compensar, conciliar, cambiar
divisas y cuadrar la caja. Es la parte más operativa del programa y la que
explica de dónde sale realmente el margen de una entidad.

Casi todos sus controles se deducen de una sola idea, que la clase 1 instala:
quien origina una operación no la aprueba, y quien la aprueba no la registra. Las
quince clases siguientes son esa idea aplicada a procesos concretos.

El eje es que **el negocio bancario vive de una transformación de plazos**: se
capta a corto y se coloca a largo. De ahí salen su utilidad, su riesgo de liquidez
y buena parte de la regulación que la Parte 12 desarrolla.

## Con qué hay que llegar

| Parte | Qué aporta |
|---|---|
| 3 | Los productos vistos desde el cliente |
| 5 | Contabilidad, asientos y conciliación |
| 9 | Colocación de crédito y su ciclo |

## Qué se aprende

1. **Recorrer** una operación por las tres áreas del banco y ubicar sus controles.
2. **Calcular** el costo de fondos y estimar el saldo núcleo que permite prestar a largo plazo.
3. **Situar** el momento de firmeza de un pago y decidir qué se puede hacer antes y después.
4. **Conciliar** una cuenta clasificando cada partida y detectando patrones de fraude.
5. **Dimensionar** la capacidad operativa por volumen pico y no por la media.

## Cómo se encadenan las 16 clases

Las dieciséis clases van del marco al proceso y del proceso a su continuidad.

La **clase 1** describe el modelo operativo y el principio de segregación que
justifica casi todos los controles que vienen después.

Las **clases 2 y 3** son las dos caras del balance: de dónde sale el dinero y dónde
se pone, con las medidas que deciden si crecer conviene.

Las **clases 4 a 8** recorren los procesos del día a día en el orden en que ocurren:
abrir una cuenta, depositar, transferir, compensar entre bancos y conciliar. La 8
es el control que detecta lo que los siete anteriores dejaron pasar.

Las **clases 9 y 10** miran los pagos como un mercado, con su economía y sus dos
negocios opuestos dentro de las tarjetas.

Las **clases 11 y 12** son los dos extremos del modelo: el canal más caro y la
función que gestiona todo el balance.

Las **clases 13 y 14** cruzan la frontera, donde no existe infraestructura común y
los instrumentos documentales sustituyen a la confianza.

Las **clases 15 y 16** cierran con el canal por el que llega cada operación y con
lo que ocurre cuando el proceso no funciona.

## Secuencia

1. [Modelo operativo de un banco](classes/01-modelo-operativo-de-un-banco.md)
2. [Captaciones](classes/02-captaciones.md)
3. [Colocaciones](classes/03-colocaciones.md)
4. [Apertura y administración de cuentas](classes/04-apertura-y-administracion-de-cuentas.md)
5. [Depósitos y giros](classes/05-depositos-y-giros.md)
6. [Transferencias](classes/06-transferencias.md)
7. [Compensación y liquidación](classes/07-compensacion-y-liquidacion.md)
8. [Conciliación bancaria](classes/08-conciliacion-bancaria.md)
9. [Medios de pago](classes/09-medios-de-pago.md)
10. [Tarjetas y adquirencia](classes/10-tarjetas-y-adquirencia.md)
11. [Caja y sucursales](classes/11-caja-y-sucursales.md)
12. [Tesorería](classes/12-tesoreria.md)
13. [Operaciones internacionales](classes/13-operaciones-internacionales.md)
14. [Comercio exterior](classes/14-comercio-exterior.md)
15. [Canales y experiencia del cliente](classes/15-canales-y-experiencia-del-cliente.md)
16. [Continuidad y eficiencia operativa](classes/16-continuidad-y-eficiencia-operativa.md)

## Cómo se trabaja

Son **16 clases de 90 minutos** —24 horas de sesión— con **6 laboratorios**, **2 evaluaciones** y un proyecto integrador. Cada clase supone la anterior, así que el orden importa: saltarse una deja sin base a las que vienen después.

Los laboratorios se resuelven con datos propios o sintéticos y nunca con datos reales de terceros. Las evaluaciones son dos: una diagnóstica al empezar, que no se califica para aprobar sino para saber qué reforzar, y una final. El proyecto es el entregable que demuestra que la parte se entendió.

## Qué queda como evidencia

- El recorrido de una operación con sus controles y su punto de segregación.
- El costo de fondos y el saldo núcleo de un banco sintético.
- Una conciliación con sus partidas clasificadas y su hallazgo.
- El mapa de criticidad de los procesos con la prueba de continuidad de uno.
- La autoevaluación final con lo que quedó flojo.

## Continúa en la Etapa 5

Aquí se opera un banco por dentro. La Parte 18 sale del país: coge la misma
transferencia y la sigue por una cadena de corresponsales, con su mensajería, su
liquidez y sus controles. Casi todo lo que allí parece complicado se entiende sin
esfuerzo si esta parte está asentada.

| Qué se profundiza | Dónde |
|---|---|
| Corresponsalía bancaria y sus responsabilidades | Parte 18, clase 3 |
| Cuentas nostro, vostro y loro | Parte 18, clase 4 |
| Mensajería frente a movimiento de fondos | Parte 18, clase 5 |
| ISO 20022 y datos estructurados | Parte 18, clase 6 |
| Compensación, liquidación y finalidad | Parte 18, clase 7 |
| Liquidez, prefinanciación y neteo | Parte 18, clase 8 |
| Remesas y corredores internacionales | Parte 18, clase 10 |
| Pago contra pago y liquidación atómica | Parte 18, clase 15 |
| Interconexión de sistemas de pago inmediato | Parte 18, clase 13 |

**Casos relacionados:** [`cross-border-payments/pago-retenido`](../../case-studies/cross-border-payments/pago-retenido.md) ·
[`cross-border-payments/falta-de-liquidez`](../../case-studies/cross-border-payments/falta-de-liquidez.md) ·
[`iso20022/error-de-migracion`](../../case-studies/iso20022/error-de-migracion.md)
