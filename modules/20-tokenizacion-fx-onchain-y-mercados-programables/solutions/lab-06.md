# Solución de referencia — Laboratorio 6: creación de mercado automatizada

> Material docente.

## El deslizamiento es el tamaño relativo a la reserva

Es el hallazgo del laboratorio y de la clase 13.

```python
def test_el_deslizamiento_es_el_tamano_relativo_a_la_reserva():
    for entrega in (5_000, 10_000, 25_000):
        c = _piscina().cotizar(entrega)
        assert c["deslizamiento"] == pytest.approx(c["tamano_relativo"], abs=0.005)
```

```text
  entrega     recibe   precio efectivo   deslizamiento   relativo
   10 000     19 560         1,95598          2,20 %      2,00 %
   20 000     38 369         1,91845          4,08 %      4,00 %
   30 000     56 470         1,88234          5,88 %      6,00 %
```

**Consecuencia:** para operar 1 000 000 con menos del 1 % de deslizamiento hace
falta una reserva de 100 000 000. El capital necesario es enorme comparado con
el volumen que sirve, y ese es el problema estructural del mecanismo.

## El precio efectivo es siempre peor que el marginal

```python
c = _piscina().cotizar(10_000)
assert c["precio_efectivo"] < c["precio_marginal"]
```

No es una comisión oculta: es la forma de la curva. Cada unidad se ejecuta a un
precio peor que la anterior porque las reservas se han movido.

## La reserva nunca se vacía, y eso no es una buena noticia

```python
c = _piscina().cotizar(10_000_000_000)
assert c["recibe"] < 1_000_000
assert c["deslizamiento"] > 0.99
```

Es la propiedad del producto constante: la reserva tiende a cero sin llegar. Por
eso **el mecanismo siempre da precio**, y por eso ese precio puede ser ruinoso.
Dar precio no es lo mismo que dar liquidez.

## La pérdida por divergencia

```text
fórmula   2·√r / (1 + r) − 1

  r = 1,25  →   −0,62 %
  r = 1,45  →   −1,70 %
  r = 1,50  →   −2,02 %
  r = 2,00  →   −5,72 %
  r = 4,00  →  −20,00 %
```

Es **simétrica**: mover el precio al doble o a la mitad produce la misma
pérdida.

```python
assert perdida_por_divergencia(2.0) == pytest.approx(perdida_por_divergencia(0.5))
```

Y es **estructural, no accidental**: si el precio externo se mueve, los
arbitrajistas operan contra la reserva hasta igualarlo, y el aportante acaba con
más del activo que baja y menos del que sube. Comparado con haberse quedado
quieto, pierde. Siempre.

## El neto del aportante

```text
VALOR APORTADO             100 000
comisiones anuales         +12 600
divergencia con r = 1,45    −1 701
NETO                       +10 899   (10,9 %)

FRENTE A UNA ALTERNATIVA AL 4,3 %
  prima de 6,6 puntos

¿POR QUÉ RIESGO?
  · pérdida mayor si el precio se mueve más
  · riesgo del emisor de cada activo
  · riesgo del contrato
  · iliquidez: retirar la reserva mueve el precio
```

La divergencia se comió el 13,5 % del rendimiento por comisiones. Con un
movimiento mayor se lo come entero.

## El punto en que deja de compensar

```python
r = razon_que_anula_las_comisiones(12_600, 100_000)
assert r == pytest.approx(2.89, abs=0.05)
```

```text
HACE FALTA UNA PÉRDIDA DEL 12,6 %
  2·√r / (1 + r) − 1 = −0,126
  → r ≈ 2,89 (o su inverso 0,346)

CON UNA VOLATILIDAD MENSUAL DEL 9 %
  la anualizada es 9 % × √12 = 31,2 %
  un movimiento del 189 % está a unas 6 desviaciones

  → improbable en un año
  → perfectamente posible en tres
```

## A qué se está apostando

```text
COMISIONES  dependen del VOLUMEN
DIVERGENCIA depende del MOVIMIENTO DE PRECIO

  → aportar reservas es una apuesta a que habrá
    mucho volumen y poco movimiento

Y ES LA APUESTA DE UN CREADOR DE MERCADO
TRADICIONAL, con una diferencia:

  este NO PUEDE RETIRARSE NI AJUSTAR
  SU COTIZACIÓN. La fórmula opera sola.
```

En un par volátil y de poco volumen, aportar reservas pierde dinero de forma
sistemática, y quien lo hace suele no haberlo calculado.

## Frente a un libro de órdenes

| Aspecto | Creador automatizado | Libro de órdenes |
|---|---|---|
| Precio disponible | Siempre | Solo si hay órdenes |
| Capital por unidad de volumen | Muy alto | Menor |
| Deslizamiento | Predecible por fórmula | Depende del libro |
| Ajuste a noticias | Por arbitraje, con retardo | Inmediato |
| Coste del proveedor | Pérdida por divergencia | Riesgo de inventario |
| Idóneo para | Pares sin creadores dispuestos | Mercados con participantes |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Mirar solo la comisión | La divergencia se come una parte |
| Llamarla «pérdida impermanente» | Se materializa al retirar |
| Operar grande de golpe | El deslizamiento es el tamaño relativo |
| Usar el precio como índice | Lo forma una fórmula, no un mercado |
| Suponer que el precio vuelve | Si no vuelve, la pérdida es real |
| Comparar con un libro sin ajustar | Compara a igual profundidad efectiva |

## Límites

- La fórmula implementada es la de producto constante; otras curvas tienen
  perfiles de deslizamiento y de divergencia distintos.
- El modelo no incluye el coste de operación en el registro, que en la práctica
  hace inviables las operaciones pequeñas.
- La razón crítica se calcula sobre un año de comisiones a volumen constante: si
  el volumen cae, el punto se acerca.
- No se modela el arbitraje: se supone que el precio converge al externo, y en un
  mercado sin arbitrajistas puede no hacerlo.
