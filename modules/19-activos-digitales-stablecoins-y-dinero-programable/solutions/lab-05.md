# Solución de referencia — Laboratorio 5: modelo algorítmico y su espiral

> Material docente.

## El ratio de absorción sube mientras el sistema se hunde

Es el hallazgo del laboratorio y de la clase 7.

```python
def test_el_ratio_de_absorcion_sube_durante_el_colapso_documenta_el_problema():
    sistema = _sistema()
    for _ in range(4):
        sistema.canjear(200_000_000)

    ratios  = [v.ratio_absorcion   for v in sistema.vueltas]
    precios = [v.precio_v_despues  for v in sistema.vueltas]

    assert all(b > a for a, b in zip(ratios,  ratios[1:]))    # SUBE
    assert all(b < a for a, b in zip(precios, precios[1:]))   # y V se hunde
```

**Esta prueba debe pasar.** Documenta que el indicador análogo a la cobertura
—el que cualquiera vigilaría— mejora durante todo el colapso.

## Las cinco vueltas

```text
  vuelta   ratio    emisión/unidad   precio V
       1   0,620         0,3333       2,3914
       2   0,649         0,4182       1,8860
       3   0,689         0,5302       1,4706
       4   0,748         0,6800       1,1329
       5   0,835         0,8827       0,8616

  el ratio pasa de 0,620 a 0,835      ← tranquiliza
  la emisión por unidad se duplica    ← la verdad
  el precio de V cae un 64 %
```

## Por qué el ratio sube

El circulante de E cae más deprisa que la capitalización de V. No es un error del
modelo: es aritmética. Retirar 200 000 000 de E reduce el denominador de forma
inmediata y completa; la capitalización de V solo cae por el impacto de la venta.

**El ratio es una foto del estado. La emisión por unidad mide la aceleración**, y
una espiral se detecta por su aceleración.

## La venta generada frente al volumen

```python
def test_una_vuelta_genera_varias_veces_el_volumen_diario():
    assert _sistema().veces_el_volumen(200_000_000) > 2.0
```

```text
venta por vuelta     140 000 000
volumen diario de V   60 000 000
                     → 2,33 veces

CON DOS VUELTAS EN UN DÍA: 4,7 veces
→ el impacto supuesto del 7 % es OPTIMISTA
→ el diseño no soporta una salida del 20 % en un día
```

## El rendimiento es dilución

```text
pagado sobre E     2 000 000 000 × 12 % = 240 000 000
ingresos reales                            42 000 000
DILUCIÓN                                  198 000 000

  82,5 % del rendimiento no es rendimiento:
  es una transferencia de los que entran después
  a los que entraron antes.

En unidades de V a precio 3,00:
  66 000 000 unidades al año sobre 400 000 000
  = 16,5 % de dilución permanente anual
```

Y el rendimiento **atrae depósitos**: la exposición crece, y con ella el tamaño
del día de la salida.

## El híbrido

```python
cobertura = cobertura_de_hibrido(exogeno=700, endogeno=300, circulante=1_000)
assert cobertura["en_calma"]   == 1.0
assert cobertura["en_tension"] == 0.7
```

La cobertura de un híbrido se calcula **siempre con el tramo endógeno a cero**,
porque ese es el escenario en el que la cobertura importa.

## Salida máxima soportable

```text
CRITERIO: la venta de V no debe superar el volumen
diario normal de V

  venta = importe × 0,70
  límite = 60 000 000
  → importe máximo por vuelta = 85 700 000

CON DOS VUELTAS AL DÍA
  salida diaria soportable ≈ 171 400 000
  sobre 2 000 000 000 de circulante
  = 8,6 %

Un emisor con reserva exógena absorbe el 20 %
vendiendo letras con un coste de 800 000.
La diferencia no es de grado: en un caso el activo
que paga es ajeno al problema; en el otro ES el problema.
```

## El mismo mecanismo con otros nombres

- «respaldado por el token de gobernanza»
- «colateralizado con el activo nativo»
- «estabilizado por incentivos de mercado»
- «reserva parcial con módulo algorítmico»
- «respaldado por acciones de la propia sociedad»

**La prueba que los detecta a todos:** rastrea el respaldo paso a paso y
pregunta en cada uno «¿este activo pierde valor si el instrumento principal
pierde la paridad?». Si la respuesta es sí en algún paso, ese respaldo amplifica.

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Vigilar el ratio de absorción | Sube durante el colapso |
| Aceptar el rendimiento sin preguntar | El 82,5 % es dilución |
| Sumar el tramo endógeno | Vale cero cuando hace falta |
| Impacto de mercado constante | El colapso parece más lento |
| Creerlo un caso pasado | Cambia de nombre, no de mecánica |
| Confundirlo con sobrecolateralización | Importa si el colateral es externo |

## Límites

- El impacto de mercado lineal por importe vendido es una simplificación: en
  tensión el libro desaparece y el impacto no es lineal.
- El modelo supone que se vende el 70 % de lo recibido; ese porcentaje es un
  supuesto y cambia la velocidad de la espiral.
- El sistema es sintético y no reproduce ningún diseño concreto; el propósito es
  entender el mecanismo, no evaluar un producto.
