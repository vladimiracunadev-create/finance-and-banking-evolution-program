# Solución de referencia — Laboratorio 3: entrega contra pago atómica

> Material docente.

## No existe estado intermedio observable

Es el hallazgo del laboratorio y de la clase 8.

```python
antes = liquidador.observar()
liquidador.liquidar(Operacion("op", "vendedor", "comprador", 1_000, 185_000))
despues = liquidador.observar()

assert antes["valores"]["vendedor"] == 1_000
assert antes["dinero"].get("vendedor", 0) == 0
assert despues["valores"]["vendedor"] == 0
assert despues["dinero"]["vendedor"] == 185_000
```

Solo hay dos estados: el de antes y el de después. **En ninguno de los dos se
movió un tramo sin el otro**, y esa ausencia es lo que se demuestra, no la
rapidez de la ejecución.

Atomicidad no es que los movimientos ocurran «casi a la vez». No basta con que
haya una reversión: una reversión implica que hubo un estado intermedio, y en
ese estado alguien pudo actuar.

## Rechazar antes de bloquear

```python
liquidador = Liquidador()
liquidador.acreditar_valor("v", 1_000)
resultado = liquidador.liquidar(Operacion("op", "v", "c", 1_000, 185_000))

assert not resultado.ejecutada
assert resultado.motivo is Motivo.SIN_DINERO
assert liquidador.valores["v"] == 1_000     # nada se bloqueo
```

Es la decisión de diseño central del módulo. **Rechazar no deja rastro;
bloquear y revertir, sí.** El orden es:

```text
1 verificar valor del vendedor
2 verificar dinero del comprador
3 si falla cualquiera → RECHAZAR sin tocar nada
4 si no → los cuatro movimientos en un solo acto
```

Y simétricamente, un fallo del tramo de valor deja el dinero intacto.

## Doble gasto imposible

```python
primera = liquidador.liquidar(Operacion("op1", "vendedor", "comprador", 1_000, 185_000))
segunda = liquidador.liquidar(Operacion("op2", "vendedor", "c2", 1_000, 185_000))

assert primera.ejecutada
assert not segunda.ejecutada
assert segunda.motivo is Motivo.SIN_VALOR
```

La segunda operación no falla por un control añadido: falla porque el saldo ya
no está. La verificación previa es la que lo garantiza.

## Sin el dinero en el registro, el liquidador se niega

```python
liquidador = Liquidador(dinero_en_el_registro=False)
assert not liquidador.permite_atomicidad

with pytest.raises(NoHayAtomicidad):
    liquidador.liquidar(Operacion("op", "v", "c", 1_000, 185_000))
```

Es deliberado: el código **se niega a simular atomicidad** cuando la condición
no se cumple, en vez de ejecutar algo que se le parece. Las cuatro opciones de
tramo de dinero son las de la clase 10, y solo tres permiten atomicidad.

## El neteo

```python
saldos = netear(operaciones)

assert sum(saldos["valores"].values()) == 0
assert sum(saldos["dinero"].values()) == 0
```

El conjunto compensado debe liquidarse **como una sola unidad**: o todo el neteo
o nada. Y de ahí el riesgo nuevo: si falla, fallan todas las operaciones del
ciclo, no una.

## El ahorro neto

```text
AHORRO POR ATOMICIDAD
  exposición = 444 000 000 × 2 días = 888 000 000
  pérdida esperada = 888 000 000 × 0,004 % × 0,55
                   = 19 536 al día
  anual (250 días) = 4 884 000

COSTE DE LIQUIDEZ
  bruto     444 000 000 × 16 % × 4,3 % = 3 054 720
  neteado   444 000 000 ×  3 % × 4,3 % =   572 760

NETO
  con bruto    1 829 280
  con neteo    4 311 240   ← casi el doble

MENOS EL FALLO DEL CICLO
  0,25 días al año × 1 554 000 = 388 500
  NETO CORREGIDO = 3 922 740
```

## Los cinco riesgos

```python
def test_la_atomicidad_elimina_exactamente_un_riesgo_de_cinco():
    eliminados = [k for k, v in RIESGOS.items() if v.startswith("lo elimina")]
    assert len(RIESGOS) == 5
    assert eliminados == ["principal"]
```

| Riesgo | Estado | Control |
|---|---|---|
| Principal | **Eliminado** | La atomicidad |
| Reemplazo | Subsiste | Límites y garantías |
| Liquidez | Subsiste | Neteo y ventanas de liquidación |
| Operativo | Subsiste | Redundancia y modo degradado |
| Jurídico | Subsiste | Verificar la finalidad legal aplicable |

Y hay un sexto que aparece al llevar la liquidación a un registro: **el riesgo
del emisor del dinero**. Si el tramo de dinero no es un pasivo de banco central,
el riesgo de principal no desapareció: cambió de sitio.

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Llamar atómico a «casi a la vez» | No debe existir estado intermedio |
| Bloquear y revertir | La reversión prueba que hubo estado intermedio |
| Olvidar el coste de liquidez | El ahorro se sobrestima en un 62 % |
| Prometerla con el dinero fuera | La arquitectura lo impide |
| Ignorar el emisor del dinero | Es riesgo de crédito nuevo |
| Presentarla como si cubriera todo | Elimina uno de cinco |

## Límites

- El liquidador corre en un solo proceso: no modela concurrencia real ni
  latencias de red.
- La probabilidad de incumplimiento y la recuperación esperada son supuestos
  declarados; con otros valores el ahorro cambia proporcionalmente.
- El coste del fallo del ciclo supone una disponibilidad del 99,9 % y una
  variación de precio del 0,35 %: ambos son estimaciones y no observaciones.
- El modelo no incluye el riesgo del emisor del dinero, que se analiza en la
  clase 10 y se cuantifica aparte.
