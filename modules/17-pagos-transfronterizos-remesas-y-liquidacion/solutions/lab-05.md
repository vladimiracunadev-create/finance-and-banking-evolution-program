# Solución de referencia — Laboratorio 5: comparador de remesas

> Material docente. Los datos de operadores son **sintéticos**.

## El denominador honesto

```python
def coste_total(ruta: Ruta, importe: Decimal, referencia: Decimal) -> Decimal:
    recibido = ruta.simular(importe)
    sin_coste = importe * referencia          # tipo cruzado de mercado
    return (sin_coste - recibido) / sin_coste
```

Comparar dos rutas entre sí sin `sin_coste` oculta cuánto se pierde en ambas. Es
el error que hace que dos operadores caros parezcan «competitivos entre ellos».

## Descomposición del coste de una ruta

Envío de 500 000 CLP a Filipinas, tipo de referencia 1 CLP = 0,058947 PHP.

| Componente | PHP | % del coste |
|---|---:|---:|
| Comisión de envío | 1 061,0 | 29,6 % |
| Diferencial CLP/USD | 813,7 | 22,7 % |
| Comisión del intermediario | 840,0 | 23,4 % |
| Diferencial USD/PHP | 669,0 | 18,7 % |
| Comisión del banco receptor | 200,0 | 5,6 % |
| **Total** | **3 583,7** | **100 %** |

```text
COMISIONES VISIBLES:   2 101,0  (58,6 %)
DIFERENCIALES:         1 482,7  (41,4 %)

el 41 % del coste no aparece en el comprobante
```

## El diferencial cruzado se compone

```text
MAL   294,7 pb + 250,0 pb = 544,7 pb
BIEN  1 − (1 − 0,029470) × (1 − 0,025000) = 5,291 % = 529,1 pb
```

La diferencia parece pequeña y crece con los diferenciales. Con dos patas al
5 %, la suma da 1 000 pb y la composición 975 pb; con dos al 15 %, 3 000 frente
a 2 775.

## El cambio de ganador por tramo

```text
precio efectivo (CLP) según importe

importe      nosotros    A         B         C
 50 000        1 415     5 375     1 550     3 400
228 261        6 460     7 068     7 076     6 609
500 000       14 150     9 650    15 500    11 500
2 000 000     56 600    23 900    62 000    38 500
```

Ganador por tramo: nosotros hasta ~300 000, `A` por encima. Un comparador que
solo muestre el ticket medio da una respuesta correcta para el 71 % de los
usuarios y equivocada para el 29 % que más dinero mueve.

## La advertencia automática

```python
if ruta.comision_explicita < coste_total * Decimal("0.5"):
    aviso = (
        "Mas de la mitad del coste de esta ruta esta en el tipo de cambio, "
        f"no en la comision. Tipo aplicado: {ruta.tipo}; "
        f"tipo de referencia: {referencia}."
    )
```

Es la única forma de que «sin comisiones» deje de funcionar como argumento.

## Comparación con el objetivo internacional

El comparador marca los corredores por encima del umbral vigente. La
implementación **no codifica el umbral**: lo lee de configuración con su fecha de
verificación, porque los objetivos se revisan.

```json
{
  "objetivo_coste_medio": 0.03,
  "objetivo_techo_corredor": 0.05,
  "fuente": "FSB, Targets for Addressing the Four Challenges",
  "verificado": "2026-08-06"
}
```

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Usar el tipo del operador como referencia | El denominador queda sesgado |
| Sumar diferenciales cruzados | Subestima el coste |
| Un solo importe en la comparación | Oculta el cambio de ganador |
| Umbral del objetivo codificado | Se desactualiza sin que nadie lo note |
| No declarar que los datos son sintéticos | Se lee como información de mercado |

## Límites

- Los tipos son de un instante; rutas que liquidan en momentos distintos tienen
  una parte de la diferencia explicada por el mercado, no por el coste.
- No se modelan promociones, primeros envíos gratuitos ni descuentos por volumen,
  que son habituales y cambian la comparación.
- El plazo es el declarado por el operador, no el observado.
