# Laboratorio 3: Registro de referencia y atomicidad

## Propósito

Determinar qué registro manda en cada dato y **demostrar si la atomicidad es alcanzable** en el componente que la promete.

Los dos laboratorios anteriores decidieron qué se construye y qué régimen activa. Este cierra la dependencia que quedó abierta: el registro de colateral solo se justifica si la atomicidad existe, y eso depende de dónde esté el dinero.

## Escenario

El sistema tiene tres registros: el propio, el del custodio y el del banco emisor. Hay que decidir cuál manda en cada dato y calcular la ventana de conciliación.

## Contexto

Las clases 5 y 7 resuelven las decisiones del dinero y del registro de referencia, que en conjunto determinan si la promesa de atomicidad se puede sostener.

## Datos

Tres registros sintéticos con su distribución de operaciones por cliente.

## Supuestos del ejercicio

- El 5 % más activo hace el 55 % de las operaciones.
- Coste de financiación del 4,3 % anual.
- Probabilidad de incumplimiento a un día del 0,003 %.

## Requisitos

- Laboratorio 2 completado.
- Haber leído las clases 5 y 7.

## Pasos

1. Determina el registro de referencia de cada dato del sistema.
2. Comprueba que el bloqueo de origen evita dos versiones activas.
3. Calcula la ventana con la distribución real, no con la media.
4. Compara las cuatro opciones de tramo de dinero.
5. Calcula el saldo prefinanciado y su coste.
6. Contrasta ese coste con la pérdida esperada evitada.
7. Cierra la cadena de decisiones que dependía de esta.
8. Escribe la distinción entre registro distribuido y registro programable.

## Arquitectura

```text
LA CADENA DE DECISIONES

  dinero DENTRO del registro
    → atomicidad alcanzable
    → el registro de colateral se justifica

  dinero FUERA
    → no hay atomicidad
    → el registro no aporta nada

NO HAY UNA TERCERA RAMA.
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Cada dato tiene su registro de referencia | Tabla completa |
| 2 | El bloqueo evita dos versiones | Suma constante |
| 3 | La ventana se calcula con el más activo | No con la media |
| 4 | Las cuatro opciones se comparan | Riesgo y coste |
| 5 | El saldo prefinanciado se calcula | Con y sin neteo |
| 6 | La cadena de decisiones se cierra | Explícitamente |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Un registro de referencia para todo | Simplifica | Se decide dato a dato |
| Ventana por la media | Es el cálculo fácil | Decide el cliente más activo |
| Prometer atomicidad sin el dinero dentro | La arquitectura lo impide | Verificar cada tramo |
| Ignorar el saldo prefinanciado | No aparece en el piloto | Es el coste principal |
| Dejar la dependencia abierta | Se olvida | Cerrar la cadena por escrito |

## Pruebas

```bash
python -m pytest tests/test_digital_bank_capstone.py -q -k "tension or tolerancia"
```

```bash
python apps/digital_bank_capstone/cli.py tensions
```

## Entregables

- El registro de referencia de cada dato.
- La ventana calculada con la distribución real.
- La comparación de las cuatro opciones de dinero.
- `solution.md` con la cadena de decisiones cerrada.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Registro por dato | 20 |
| Ventana con distribución real | 20 |
| Opciones de dinero comparadas | 25 |
| Saldo prefinanciado | 20 |
| Cadena cerrada | 15 |

## Solución de referencia

En [`solutions/lab-03.md`](../solutions/lab-03.md).
