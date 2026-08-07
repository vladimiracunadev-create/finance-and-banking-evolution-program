# Laboratorio 2: Libro mayor y movimientos

## Propósito

Construir el registro contable del banco y **comprobar que la ecuación cuadra tras cada operación**.

El laboratorio 1 fijó qué se construye. Este construye el registro sobre el que se apoyará todo lo demás, con la restricción de integridad de la Parte 5.

## Escenario

Ciento veinte operaciones del primer mes del banco: aperturas, depósitos, colocaciones, pagos y devengos.

## Datos

Las 120 operaciones con su fecha, su tipo y su importe.

## Supuestos del ejercicio

- El plan de cuentas del banco se entrega como dato.
- Los devengos se practican al cierre diario.
- Cada operación tiene su documento de respaldo identificado.

## Pasos

1. Diseña el modelo de datos con su identificador único por entidad.
2. Registra las 120 operaciones con partida doble.
3. Comprueba que la ecuación contable cuadra tras cada una.
4. Practica los devengos diarios y verifica su acumulación.
5. Construye el balance de comprobación del mes y revisa la naturaleza de cada saldo.
6. Reconstruye el linaje de tres saldos hasta su operación de origen.
7. Introduce un error deliberado y comprueba qué control lo detecta.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | El modelo de datos tiene identificador único | Por entidad |
| 2 | Las 120 están registradas | Con partida doble |
| 3 | La ecuación cuadra tras cada una | Comprobado, no supuesto |
| 4 | El linaje de tres saldos está reconstruido | Hasta su origen |
| 5 | El error deliberado se detecta | Con el control que lo hace |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Identificadores no únicos | Ninguna agregación posterior cuadrará |
| No comprobar la ecuación en cada paso | El error se descubre al final y cuesta más |
| Devengar al cierre de mes | El resultado diario deja de existir |
| Sin linaje | Ninguna cifra se puede defender |

## Entregables

- `solution.md` con el modelo de datos y su identificador.
- El registro de las 120 operaciones y la comprobación de la ecuación.
- El balance de comprobación del mes.
- El linaje de tres saldos y el error detectado.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Modelo de datos | 20 |
| Registro correcto | 25 |
| Ecuación comprobada | 20 |
| Linaje | 20 |
| Error detectado | 15 |
