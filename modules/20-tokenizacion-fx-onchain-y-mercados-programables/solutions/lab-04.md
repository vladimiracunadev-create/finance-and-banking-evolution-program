# Solución de referencia — Laboratorio 4: modos de fallo de la liquidación

> Material docente.

## La atomicidad elimina uno de cinco

Es el hallazgo del laboratorio: los otros cuatro necesitan su propio control, y
presentar la atomicidad como si los cubriera todos es el error de esta clase.

```text
  principal   ELIMINADO por la atomicidad
  reemplazo   subsiste: hay que rehacer la operación a otro precio
  liquidez    subsiste: el saldo estaba comprometido
  operativo   subsiste: el registro puede detenerse
  jurídico    subsiste: la finalidad legal puede no coincidir
```

## El registro detenido rechaza sin tocar nada

```python
liquidador.detenido = True
resultado = liquidador.liquidar(Operacion("op", "vendedor", "comprador", 1_000, 185_000))

assert resultado.motivo is Motivo.REGISTRO_DETENIDO
assert liquidador.valores["vendedor"] == 1_000
```

El mismo principio que el rechazo por falta de saldo: se comprueba antes y no se
toca nada. La diferencia es que aquí el fallo es del sistema y no de las partes.

## El coste de reemplazo del ciclo

```text
SI EL NETEO FALLA, FALLAN LAS 2 400 OPERACIONES

  volumen del ciclo             444 000 000
  variación media en un día           0,35 %
  coste de reemplazo              1 554 000 por episodio

  disponibilidad supuesta            99,9 %
  → 0,25 días al año
  → coste esperado                  388 500 al año
```

Es el riesgo que el neteo introduce a cambio de reducir el coste de liquidez, y
hay que dimensionarlo antes de elegirlo.

## La independencia efectiva del custodio

```text
ESQUEMA INICIAL · 3-de-5
  4 guardianes en la sede, 1 externo
  mayor grupo por ubicación: 4
  4 ≥ 3 → UN SOLO EVENTO ALCANZA EL UMBRAL
  independencia efectiva: 2
  tolera evento correlacionado: NO

TRAS REDISTRIBUIR, SIN CAMBIAR EL UMBRAL
  2 en sede, 1 en filial, 1 proveedor, 1 despacho
  con dispositivos y jurisdicciones distintos
  mayor grupo: 2
  independencia efectiva: 4
  tolera evento correlacionado: SÍ
```

El umbral no cambió. Cambió **dónde y con qué** están las partes.

## La conciliación a tres bandas

```text
TRES REGISTROS QUE DEBEN COINCIDIR
  el registro del token
  los libros del custodio
  el registro del depositario central

EL CASO QUE DOS A DOS NO VE
  token dice 100, custodio dice 100, depositario dice 98

  · token contra custodio: coincide ✓
  · custodio contra depositario: no coincide ✓ se ve

  PERO si el custodio ajusta sus libros al depositario
  sin avisar al token, las dos comprobaciones dan bien
  y la diferencia persiste

CORRECCIÓN
  comparación simultánea de los tres, con un responsable
  designado que mire el conjunto
```

## Los cuatro modelos de conexión

```text
VOLUMEN POR PAR
  A ↔ C   333 000 000 al día   70,3 %
  B ↔ C   114 700 000          24,2 %
  A ↔ B    25 900 000           5,5 %

PARTICIPANTE COMÚN
  473 600 000 × 0,012 % × 250 = 14 208 000 al año
  y 79 millones de exposición permanente

TRES ENLACES DIRECTOS
  año 1  8 400 000 + 1 260 000 = 9 660 000
  año 2  1 260 000

DOS ENLACES + PARTICIPANTE COMÚN PARA A↔B
  año 1  5 600 000 + 840 000 + 777 000 = 7 217 000
  → cubre el 94,5 % del volumen y es lo más barato
```

## El puente se descarta por una medición de tres líneas

```text
COMPOSICIÓN SUPUESTA DE UN 5-DE-9
  5 firmantes de la misma organización
  3 de un proveedor común
  1 externo

  mayor grupo: 5 · umbral: 5
  → UN SOLO EVENTO ALCANZA EL UMBRAL

VALOR QUE ACUMULARÍA
  el 20 % del volumen diario = 94 720 000

  ¿cuánto cuesta comprometer a 5 firmantes
  de la misma organización?
  mucho menos de 94 millones

→ EL PUENTE ES UN OBJETIVO ECONÓMICO RACIONAL
```

El valor total acumulado en un puente supera con mucho el de cualquier operación
individual, y su seguridad es la del umbral más débil de su custodia.

## Plan de sustitución del custodio

```text
1 CUSTODIO SUSTITUTO
    identificado por contrato, o procedimiento
    escrito para designarlo en 5 días hábiles

2 COPIA DEL REGISTRO
    diaria, en poder de un tercero independiente,
    con verificación de integridad

3 PROCEDIMIENTO DE TRASLADO
    probado una vez al año, con plazo máximo
    de 10 días hábiles

4 QUIÉN PAGA
    declarado en el contrato de custodia

5 EVENTOS CORPORATIVOS EN TRANSICIÓN
    quién los aplica y con qué registro

6 COMUNICACIÓN A LOS TITULARES
    plazo máximo de 24 horas desde el hecho

LA COPIA DIARIA ES LA PIEZA CRÍTICA
  sin ella, la sustitución depende de la
  cooperación de quien está en dificultades
```

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Presentar la atomicidad como si cubriera todo | Elimina uno de cinco |
| Conciliar dos a dos | Una diferencia puede persistir dando ambas por buenas |
| Elegir el puente por barato | Mide su umbral efectivo y su valor acumulado |
| Un enlace por par | Prioriza por volumen |
| Sin plan de sustitución | Nadie prevé el cierre hasta que ocurre |
| Consolidar como proyecto técnico | Es una negociación de gobierno |

## Límites

- El modelo de independencia efectiva usa cuatro factores; en la práctica hay
  más (proveedor de correo, cadena de suministro, administrador de sistemas).
- Los costes de enlace y de participante común son supuestos declarados: con
  otras cifras el orden de preferencia puede invertirse.
- El coste de comprometer un umbral no se puede estimar con precisión; lo que el
  análisis sostiene es la comparación de órdenes de magnitud, no una cifra.
- La consolidación se analiza como opción y **no se modela**: su viabilidad
  depende del gobierno, no de la técnica.
