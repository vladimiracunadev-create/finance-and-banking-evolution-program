# Solución de referencia — Laboratorio 5: liquidez del mercado secundario

> Material docente.

## «Liquidez diaria» describía la posibilidad de enviar una orden

Es el hallazgo del laboratorio y de la clase 6. La plataforma no mentía: **la
palabra hacía todo el trabajo**.

```text
DÍAS CON AL MENOS UNA OPERACIÓN
  74 / 182 = 40,7 %

  → EN EL 59,3 % DE LOS DÍAS NO SE PUDO OPERAR
```

## El promotor ponía la mitad del volumen

```text
OPERACIONES CON PARTE VINCULADA
  148 / 412 = 35,9 % de las operaciones
  9 900 000 / 18 400 000 = 53,8 % del volumen

VOLUMEN GENUINO
  8 500 000 en seis meses = 1 416 667 al mes
  sobre 120 000 000 emitidos = 1,18 % mensual

ROTACIÓN ANUAL GENUINA
  14,2 % del capital

  más cerca de un inmueble directo
  que de un fondo cotizado
```

Y el compromiso del folleto decía que el promotor «procurará dar
contrapartida»: **el 53,8 % del volumen dependía de una intención**.

## El tiempo de salida

```text
UN TENEDOR QUIERE VENDER 400 000

  absorbiendo el 10 % del volumen mensual
  sin mover el precio: 141 667 al mes
  → 2,8 MESES

  para salir en una semana tendría que
  absorber el 113 % del volumen semanal
  → impacto de precio muy alto
```

## Las tres cosas que se presentan como una

| Concepto | Quién la da | Estado en este caso |
|---|---|---|
| Transferibilidad | El registro | Sí |
| Negociabilidad | La plataforma | Sí |
| **Liquidez** | **Participantes dispuestos a comprar** | **No** |

Ninguna tecnología da la tercera. Un activo ilíquido tokenizado es un activo
ilíquido con mejor infraestructura de transferencia.

## Por qué fraccionar no crea liquidez

```text
ARGUMENTO
  «al fraccionar, más gente puede comprar,
   luego habrá más demanda»

QUÉ FALTA
  · más compradores potenciales no es más demanda:
    es más gente que PODRÍA
  · un activo ilíquido suele serlo porque es difícil
    de valorar, no porque el mínimo sea alto

CUÁNDO SÍ AYUDA
  cuando la barrera era el importe Y hay demanda
  demostrada por debajo de él Y existe un precio
  de referencia creíble e independiente
```

## La rentabilidad neta por tamaño

```text
RENTABILIDAD BRUTA            9,2 %
menos comisiones (1,5 + 0,8)  −2,3
NETA DE COMISIONES            6,9 %

MENOS EL COSTE UNITARIO DE 18 AL AÑO

  inversión 50 000  →  0,036 %  →  neta 6,864 %
  inversión  5 000  →  0,360 %  →  neta 6,540 %
  inversión    500  →  3,600 %  →  neta 3,300 %

ALTERNATIVA SIN RIESGO: 4,1 %

  con 50 000  prima de +2,76 puntos
  con    500  prima de −0,80 puntos

EL INVERSIONISTA DE 500 ASUME RIESGO DE CRÉDITO
PRIVADO E ILIQUIDEZ A CUATRO AÑOS PARA GANAR
MENOS QUE EN UN DEPÓSITO.
```

## El importe de equilibrio

```text
PARA EMPATAR CON LA ALTERNATIVA
  6,9 % − 18/x > 4,1 %
  x > 18 / 0,028 = 643

PARA UNA PRIMA RAZONABLE DE 2 PUNTOS
  6,9 % − 18/x > 6,1 %
  x > 2 250

EL MÍNIMO PROPUESTO ERA 500.
El de equilibrio era 2 250, y estaba
a un cálculo de distancia.
```

## El compromiso de cotización que sí sirve

| Elemento | Valor exigido |
|---|---|
| Diferencial máximo | 2 % |
| Importe mínimo cotizado | 50 000 por lado |
| Horario | La ventana de subasta declarada |
| Plazo | 24 meses |
| Retirada | Solo por causas tasadas, con preaviso de 30 días |

La quinta es la trampa: las cláusulas de retirada habituales —«circunstancias
excepcionales de mercado», «a discreción con preaviso»— se activan exactamente
cuando hace falta la liquidez.

## Página de divulgación adaptada

```text
QUÉ ES
  Una participación en una sociedad que invierte en
  inmuebles en desarrollo. No es un depósito y no
  está garantizada.

SI SALE BIEN
  Cobras una parte de los alquileres y de la venta
  final. El folleto estima un 9,2 % anual bruto.

SI SALE MAL
  Puedes perder todo lo invertido. En proyectos
  comparables se han registrado pérdidas del 100 %.

CUÁNDO PUEDO SALIR
  El plazo es de 4 años. Existe un mercado
  secundario en el que, en los últimos seis meses,
  hubo operaciones en 74 de 182 días.

CUÁNTO CUESTA
  Sobre una inversión de 5 000: 115 al año en
  comisiones más 18 de coste de servicio.

SI LA PLATAFORMA CIERRA
  Tu participación consta en el libro de socios a
  nombre del vehículo. El procedimiento para
  inscribirte directamente está en la cláusula 14.
```

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Leer «liquidez» en el folleto | Mide días con ejecución |
| Volumen agregado sin desglose | El 53,8 % era del promotor |
| Elegir el mínimo por marketing | El pequeño rinde menos que sin riesgo |
| Ignorar el coste unitario | Es la variable que decide |
| Contar con el promotor | Sin compromiso, puede irse |
| No medir el tiempo de salida | Es lo que decide para quien necesita el dinero |

## Límites

- El coste unitario de 18 al año es un supuesto: incluye verificación,
  información periódica y atención, y varía mucho entre operadores.
- El modelo de impacto por venta rápida es lineal y optimista: se apoya en un
  mercado donde el 53,8 % del volumen lo pone el promotor.
- Los seis meses de datos son un período corto: una serie más larga podría
  mostrar estacionalidad que aquí no se ve.
- La página de divulgación **no sustituye al folleto**: lo acompaña, y es lo que
  la mayoría leerá.
