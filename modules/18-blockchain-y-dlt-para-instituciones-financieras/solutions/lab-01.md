# Solución de referencia — Laboratorio 1: cadena didáctica

> Material docente.

## Por qué el encadenamiento no basta

El encadenamiento hace que **manipular sin recalcular** sea detectable. No hace
nada contra **recalcular todo**.

```text
manipular la tx del bloque 40
  → cambia la raíz de Merkle del 40
  → cambia el resumen del 40
  → el bloque 41 apunta a un resumen que ya no existe
  → DETECTADO en la validación

recalcular los bloques 40 a 100
  → todos los resúmenes vuelven a encajar
  → la validación pasa
  → NO detectado
```

La inmutabilidad viene de **el coste de rehacer** más **que otros tengan la
versión original**. Ninguna de las dos la aporta el encadenamiento.

## La prueba que el laboratorio busca

```python
def test_reescribir_la_cadena_entera_no_se_detecta(cadena):
    cadena.bloques[40].transacciones[0].importe = 999_999
    assert not cadena.validar()          # se detecta

    cadena.recalcular_desde(40)
    assert cadena.validar()              # ya NO se detecta
```

Una prueba que solo comprueba la primera afirmación deja al estudiante con la
idea equivocada. La segunda es la que enseña.

## Medición del coste

```text
sin coste de producción
  rehacer 60 bloques:        0,004 s

con coste de producción (dificultad didáctica)
  rehacer 60 bloques:       18,3 s

  → el coste no hace imposible la reescritura:
    la hace CARA, y esa es toda la diferencia
```

En una red real, el coste se compara con el beneficio del ataque. Es el mismo
razonamiento de la clase 6.

## El número de orden

```python
def aplicar(self, tx: Transaccion) -> None:
    esperado = self.ordenes.get(tx.origen, 0)
    if tx.orden != esperado:
        raise TransaccionInvalida(f"orden {tx.orden}, esperado {esperado}")
    self.ordenes[tx.origen] = esperado + 1
```

Sin esas tres líneas, la misma transacción firmada se reenvía y se ejecuta dos
veces. Es la idempotencia de la Parte 17, clase 8, resuelta en el protocolo.

## Instantáneas

```text
cada 1 000 bloques se guarda el estado completo
reconstruir el estado del bloque 3 456:
  cargar la instantánea del 3 000
  reejecutar 456 bloques
  → coste acotado y previsible
```

Sin instantáneas, reconstruir un estado antiguo exige reejecutar desde el
génesis, y ese coste crece sin límite (clase 4).

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Probar solo la manipulación detectada | Deja la idea equivocada |
| Validar sin recalcular la raíz | La manipulación pasa |
| Sin número de orden | La transacción se repite |
| Sin instantáneas | El coste de consulta histórica no está acotado |
| Presentar la cadena como segura | Es didáctica y hay que decirlo |

## Límites

- La implementación es **didáctica**: sin red, sin consenso real, con firma
  simplificada. No debe usarse para nada.
- La dificultad de producción es un parámetro del ejercicio, no una medida de
  seguridad.
- Un solo proceso: no se reproduce la propagación ni la partición.
