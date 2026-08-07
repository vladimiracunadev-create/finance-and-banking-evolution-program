# Laboratorio 3: Árbol de Merkle

## Propósito

Construir un árbol de Merkle, su prueba de inclusión y —lo que casi nadie
implementa— su **prueba de exclusión** y su versión con sumas.

## Escenario

Un consorcio quiere publicar cada día un compromiso de sus posiciones para que
cada participante verifique la suya sin ver las de los demás. Y un supervisor
quiere comprobar que el total publicado es la suma real.

## Contexto

La prueba de inclusión es barata y demuestra poco. La de exclusión y la de suma
responden las preguntas que un banco necesita: «esta garantía **no** está
pignorada» y «el total es el que dices».

## Datos

Conjunto sintético de 10 000 hojas generado en el laboratorio.

## Supuestos del ejercicio

- Función de resumen de la biblioteca estándar.
- El conjunto se ordena para permitir la prueba de exclusión.
- Los importes son enteros para evitar problemas de redondeo.

## Requisitos

- Laboratorio 1 completado.
- Haber leído las clases 2 y 10.

## Pasos

1. Construye un árbol de Merkle sobre 10 000 hojas.
2. Genera la prueba de inclusión de una hoja y verifícala.
3. Mide el tamaño de la prueba y compáralo con el logaritmo en base 2 de 10 000.
4. Ordena el conjunto e implementa la **prueba de exclusión**: dos hojas
   consecutivas que rodean al elemento buscado.
5. Añade **sumas** a cada nodo y comprueba que la raíz contiene el total.
6. **Omite una hoja** y demuestra que con sumas se detecta y sin sumas no.
7. Añade una hoja con valor negativo y demuestra que reduce el total sin omitir.
8. Escribe qué demuestra y qué no demuestra tu construcción.

## Arquitectura

```text
                    raíz (resumen + suma)
                   /                     \
          nodo (r + s)                nodo (r + s)
          /         \                 /         \
       H(d1)      H(d2)            H(d3)      H(d4)
       s=12       s=45             s=8        s=31

prueba de inclusión de d3: H(d4) y el nodo izquierdo
prueba de exclusión de x:  d2 < x < d3, consecutivas
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | La prueba de inclusión verifica | 10 hojas al azar |
| 2 | El tamaño es logarítmico | Comparación con el logaritmo |
| 3 | La prueba de exclusión funciona | Elemento ausente |
| 4 | La raíz contiene el total | Comparación con la suma directa |
| 5 | Omitir una hoja se detecta con sumas | Prueba comparativa |
| 6 | Una hoja negativa reduce el total | Prueba documentada |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Omisión de hojas | Subdeclaración del total | Árbol con sumas |
| Hoja negativa | Se reduce el total sin omitir | Prueba de rango por hoja |
| Conjunto sin ordenar | No hay prueba de exclusión | Orden total |
| Segunda preimagen en el árbol | Dos conjuntos con la misma raíz | Prefijos distintos para hoja y nodo |
| Confundir pasivo con reservas | Se demuestra lo fácil | Declararlo explícitamente |

## Pruebas

```bash
python -m pytest tests/test_dlt_financial_lab.py -q -k merkle
```

```bash
python apps/dlt_financial_lab/cli.py merkle --leaves 10000
```

## Entregables

- El árbol con inclusión, exclusión y sumas.
- La medición del tamaño de la prueba.
- Las dos demostraciones: omisión detectada y no detectada.
- `solution.md` con qué demuestra y qué no demuestra la construcción.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Árbol y prueba de inclusión | 20 |
| Prueba de exclusión | 25 |
| Árbol con sumas | 25 |
| Demostración de la omisión | 20 |
| Límites declarados | 10 |

## Solución de referencia

En [`solutions/lab-03.md`](../solutions/lab-03.md).
