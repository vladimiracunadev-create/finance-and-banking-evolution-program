# Solución de referencia — Laboratorio 3: árbol de Merkle

> Material docente.

## Qué demuestra y qué no demuestra la construcción

| Construcción | Demuestra | NO demuestra |
|---|---|---|
| Árbol simple | Que un elemento **está** | Que el conjunto sea completo |
| Árbol ordenado | Que un elemento **no está** | Que el conjunto sea correcto |
| Árbol con sumas | Que el total es la suma real | Que las hojas sean legítimas |
| Con prueba de rango | Que ninguna hoja es negativa | Que existan activos que respalden |

La última fila es la que la clase 2 usa para desmontar la afirmación «tus fondos
están respaldados».

## Tamaño de la prueba

```text
10 000 hojas
  altura del árbol: 14 niveles
  elementos de la prueba: 14 resúmenes
  tamaño: 14 × 32 bytes = 448 bytes

  frente a enviar el conjunto completo:
  10 000 × 32 = 320 000 bytes

  ratio: 714 : 1
```

Esa es la propiedad que hace útil el árbol: verificación con coste logarítmico.

## Prueba de exclusión

```python
def probar_exclusion(arbol, buscado):
    """Requiere que el conjunto esté ORDENADO."""
    i = bisect.bisect_left(arbol.hojas_ordenadas, buscado)
    if i < len(arbol.hojas) and arbol.hojas_ordenadas[i] == buscado:
        raise ValueError("el elemento SI esta")
    anterior = arbol.hojas_ordenadas[i - 1] if i > 0 else None
    siguiente = arbol.hojas_ordenadas[i] if i < len(arbol.hojas) else None
    return PruebaExclusion(
        anterior=anterior,
        siguiente=siguiente,
        prueba_anterior=arbol.probar(anterior) if anterior else None,
        prueba_siguiente=arbol.probar(siguiente) if siguiente else None,
    )
```

El verificador comprueba tres cosas: que ambas están en el árbol, que son
consecutivas en el orden y que el buscado cae entre ellas. Sin orden total, la
tercera no se puede afirmar.

## El árbol con sumas y la omisión

```text
CONJUNTO COMPLETO: 10 000 hojas, total 4 820 000

  SIN SUMAS
    se omite la hoja 7 431 (saldo 12 000)
    raíz distinta, pero nadie lo sabe:
    cada cliente verifica la suya y coincide
    → OMISIÓN NO DETECTADA

  CON SUMAS
    la raíz declara 4 808 000 en vez de 4 820 000
    quien compara con el pasivo declarado lo ve
    → OMISIÓN DETECTADA
```

## La hoja negativa

```text
CON SUMAS, PERO SIN PRUEBA DE RANGO
  se añade una hoja con saldo −12 000
  el total vuelve a 4 808 000... no: 4 820 000 − 12 000
  el emisor puede ajustar el total sin omitir a nadie

CORRECCIÓN
  cada hoja demuestra que su valor está en [0, MAX]
  → prueba de rango, que es donde entra la clase 10
```

## Segunda preimagen en el árbol

Un detalle que se penaliza omitir:

```python
# MAL: un nodo interno y un par de hojas pueden producir
# el mismo resumen, permitiendo dos conjuntos con la misma raiz.
def nodo(izq, der):
    return sha256(izq + der)

# BIEN: prefijos distintos para hoja y para nodo.
def hoja(dato):
    return sha256(b"\x00" + dato)

def nodo(izq, der):
    return sha256(b"\x01" + izq + der)
```

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Árbol sin ordenar | No hay prueba de exclusión |
| Sin sumas | La omisión no se detecta |
| Sin prueba de rango | La hoja negativa ajusta el total |
| Sin prefijos distintos | Segunda preimagen |
| Llamarlo «prueba de reservas» | Solo demuestra el pasivo |

## Límites

- El árbol demuestra propiedades del **pasivo**. La existencia de activos se
  verifica fuera y con otro procedimiento.
- La prueba de rango se enuncia pero no se implementa: requiere criptografía
  que queda fuera del alcance de un laboratorio con biblioteca estándar.
- Con 10 000 hojas los tiempos son cómodos; con millones, la construcción
  completa en cada publicación deja de serlo.
