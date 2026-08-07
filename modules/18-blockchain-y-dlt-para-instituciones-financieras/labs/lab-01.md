# Laboratorio 1: Cadena didáctica en Python

## Propósito

Construir una cadena de bloques desde cero para entender exactamente qué
garantiza el encadenamiento y qué no. La conclusión que busca el laboratorio es
incómoda: **el encadenamiento por sí solo no impide reescribir la historia**.

## Escenario

El equipo de arquitectura afirma que «una vez en la cadena, el dato no se puede
cambiar». Tu tarea es construir la cadena, demostrar que la afirmación es falsa
sin consenso, y medir cuánto cuesta hacerla cierta.

## Contexto

La inmutabilidad no viene del encadenamiento: viene del **consenso más el coste
de rehacerlo**. Un registro encadenado que una sola parte controla se reescribe
en milisegundos.

## Datos

Se generan en el laboratorio. Sin dependencias externas.

## Supuestos del ejercicio

- Implementación **didáctica**: no es segura, no es eficiente y no debe usarse
  para nada real.
- Un solo proceso; la red se simula con una lista de nodos.
- Las claves son de juguete y viven en memoria.

## Requisitos

- Python 3.11 o superior, biblioteca estándar.
- Haber leído las clases 1, 2 y 4.

## Pasos

1. Implementa `Bloque` con índice, resumen anterior, raíz de Merkle, marca de
   tiempo y lista de transacciones.
2. Implementa `Cadena` con validación completa: cada bloque referencia al
   anterior y su raíz corresponde a sus transacciones.
3. Añade transacciones con firma y **número de orden por cuenta**.
4. Demuestra que una transacción repetida se rechaza.
5. **Manipula un bloque intermedio** y comprueba que la validación lo detecta.
6. **Recalcula toda la cadena desde el bloque manipulado** y comprueba que ahora
   valida: esa es la demostración que el laboratorio busca.
7. Añade un coste de producción y mide cuánto tarda rehacer 100 bloques.
8. Implementa instantáneas del estado cada N bloques y reconstruye un estado
   pasado.

## Arquitectura

```text
Bloque n-1 ──resumen──► Bloque n ──resumen──► Bloque n+1
    │                       │                     │
raíz Merkle             raíz Merkle          raíz Merkle
    │                       │                     │
   txs                     txs                   txs

manipular una tx  →  cambia su raíz  →  cambia el resumen
                  →  el bloque siguiente ya no encaja
                  →  DETECTADO

recalcular todos los siguientes  →  vuelve a encajar
                                 →  NO detectado
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | La cadena valida de extremo a extremo | `validar()` sobre 100 bloques |
| 2 | Una transacción repetida se rechaza | Prueba con el mismo número de orden |
| 3 | Manipular sin recalcular se detecta | Prueba negativa |
| 4 | Recalcular todo **no** se detecta | Prueba que documenta la limitación |
| 5 | El coste de rehacer se mide | Informe con el tiempo |
| 6 | El estado pasado se reconstruye | Comparación con el guardado |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Reescritura completa | La historia cambia sin dejar rastro | Consenso y coste de producción |
| Transacción repetida | Doble gasto | Número de orden por cuenta |
| Firma no verificada | Cualquiera ordena por otro | Verificación obligatoria |
| Raíz de Merkle no comprobada | Se altera una transacción | Recalcular la raíz al validar |
| Marca de tiempo manipulada | Se altera el orden aparente | Tolerancia acotada |

## Pruebas

```bash
python -m pytest tests/test_dlt_financial_lab.py -q -k cadena
```

```bash
python apps/dlt_financial_lab/cli.py chain --blocks 100
```

## Entregables

- `solution.md` con la explicación de por qué el encadenamiento no basta.
- La cadena implementada con validación completa.
- Las dos pruebas de manipulación: la detectada y la no detectada.
- La medición del coste de rehacer.
- Tabla de supuestos y nota de límites.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Cadena y validación correctas | 25 |
| Prueba de manipulación detectada | 20 |
| Prueba de reescritura no detectada | 25 |
| Medición del coste | 15 |
| Límites declarados | 15 |

## Solución de referencia

En [`solutions/lab-01.md`](../solutions/lab-01.md).
