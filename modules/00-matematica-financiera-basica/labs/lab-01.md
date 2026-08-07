# Laboratorio 1: Diagnóstico y operaciones esenciales

## Propósito

Resolver veinte operaciones sin calculadora y **verificar cada resultado por un segundo camino**, para descubrir cuáles se dan por sabidas y no lo están.

Es el primer laboratorio del programa y el que fija el método. Todo lo que viene después se apoya en estas operaciones, así que un hueco aquí se arrastra durante trece partes.

## Escenario

Un analista recibe veinte cifras sueltas de un estado de cuenta y tiene que ordenarlas, convertirlas a una unidad común y detectar las tres que no pueden ser correctas.

## Datos

Veinte magnitudes sintéticas con su unidad y su fecha, tres de ellas inconsistentes.

## Supuestos del ejercicio

- Todas las cifras están en la misma moneda.
- El redondeo se declara a dos decimales salvo indicación en contrario.
- Las fechas se expresan en formato ISO.

## Pasos

1. Clasifica cada cifra por magnitud, momento y signo.
2. Convierte todas a una unidad común y declara la conversión aplicada.
3. Estima el orden de magnitud de cada resultado antes de calcularlo.
4. Calcula y compara con tu estimación previa.
5. Identifica las tres cifras inconsistentes y explica por qué lo son.
6. Declara el criterio de redondeo y aplícalo de forma uniforme.
7. Verifica tres resultados por un camino distinto del original.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Cada cifra tiene magnitud, momento y signo | Tabla completa, sin celdas vacías |
| 2 | La estimación previa está escrita | Antes del cálculo, no después |
| 3 | Las tres inconsistentes se detectan | Con la razón de cada una |
| 4 | El redondeo es uniforme | Un solo criterio declarado |
| 5 | Tres resultados verificados por otro camino | Con el camino descrito |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Calcular sin estimar antes | La estimación es lo que detecta el error de orden de magnitud |
| Omitir el signo | Un cargo y un abono con el mismo valor absoluto no son lo mismo |
| Redondear con criterios distintos | Las sumas dejan de cuadrar y nadie sabe por qué |
| Verificar repitiendo el mismo cálculo | Repetir un error no lo detecta |

## Entregables

- `solution.md` con la tabla de las veinte cifras clasificadas.
- Las tres inconsistencias con su explicación.
- El criterio de redondeo declarado.
- Las tres verificaciones por segundo camino.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Clasificación completa | 30 |
| Estimación previa | 20 |
| Inconsistencias detectadas | 25 |
| Redondeo uniforme | 10 |
| Verificación independiente | 15 |
