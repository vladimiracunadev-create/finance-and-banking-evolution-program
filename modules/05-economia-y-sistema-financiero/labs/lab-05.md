# Laboratorio 5: Creación de dinero

## Propósito

Seguir los asientos de una operación de crédito y **comprobar que el depósito no existía antes del préstamo**.

Los laboratorios anteriores midieron la economía. Este demuestra con asientos el mecanismo que la conecta con la banca, y corrige la idea más extendida sobre el negocio bancario.

## Escenario

Un banco otorga un crédito de 40 000 000 a una empresa que no tenía cuenta previa, y esta paga a un proveedor de otro banco.

## Datos

La secuencia completa de operaciones y los balances iniciales de los dos bancos.

## Supuestos del ejercicio

- Los dos bancos parten con posición de reserva conocida.
- El encaje exigido se entrega como dato.
- El proveedor mantiene el saldo recibido en su cuenta.

## Pasos

1. Registra los asientos del otorgamiento en el banco prestamista.
2. Comprueba qué agregados monetarios cambian y en cuánto.
3. Registra el pago al proveedor y su efecto en los dos bancos.
4. Sigue la posición de reserva de cada banco tras el pago.
5. Determina qué limita realmente la capacidad de prestar del primer banco.
6. Explica en tres frases por qué el multiplicador monetario no describe el proceso.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los asientos del otorgamiento están registrados | Con las dos cuentas |
| 2 | El efecto sobre los agregados está medido | M1 y M2 |
| 3 | El pago entre bancos está registrado | En ambos |
| 4 | La posición de reserva se sigue | Después del pago |
| 5 | El límite real está identificado | Y no es el encaje |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Suponer que el banco presta lo que captó | El depósito lo crea el propio crédito |
| Tratar el encaje como el límite operativo | El límite es el capital y la demanda solvente |
| No seguir el pago entre bancos | Ahí es donde la reserva se mueve |
| Confundir base monetaria con dinero | La mayor parte del dinero es bancario |

## Entregables

- `solution.md` con los asientos de las dos operaciones.
- El efecto sobre los agregados monetarios.
- La posición de reserva de los dos bancos.
- Las tres frases sobre el multiplicador.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Asientos correctos | 30 |
| Efecto en agregados | 20 |
| Pago entre bancos | 20 |
| Límite real identificado | 20 |
| Conclusión | 10 |
