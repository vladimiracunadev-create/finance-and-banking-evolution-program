# Solución de referencia — Laboratorio 7: liquidez y profundidad de mercado

> Material docente.

## Los dos cocientes dan conclusiones opuestas

Es el hallazgo del laboratorio y de la clase 13.

```python
def test_los_dos_cocientes_dan_conclusiones_opuestas_documenta_el_problema():
    par = cocientes(_libro(), 12_000_000)
    assert par["sobre_volumen"]     < 0.07   # 6,52 %  → parece cómodo
    assert par["sobre_profundidad"] > 5.0    # 5,77x   → y no lo es
```

**Esta prueba debe pasar.** El cociente sobre volumen usa el dato que se publica
y que puede inflarse sin coste real; el cociente sobre profundidad usa el libro,
que es lo que efectivamente absorbe una venta.

## Las tres profundidades

```text
  precio actual 100,00

  −1 %  → 99,00  →  2 080 000
  −2 %  → 98,00  →  3 340 000
  −5 %  → 95,00  →  6 000 000   (interpolado entre 96,00 y 93,00)

POSICIÓN / PROFUNDIDAD AL 1 %
  12 000 000 / 2 080 000 = 5,77
  la posición es casi seis veces lo que el mercado
  absorbe con un 1 % de impacto
```

## La función se niega a inventar un precio

```python
def test_una_venta_que_agota_el_libro_exige_declarar_el_precio_de_cola():
    with pytest.raises(ValueError):
        _libro().vender(12_000_000)
```

Es una decisión de diseño deliberada. Un modelo que rellena el hueco con un
supuesto invisible produce una cifra que nadie revisa. Aquí el supuesto hay que
escribirlo.

## Venta de golpe

```text
  tramo 1     420 000 a 100,00 =    42 000 000
  tramo 2     730 000 a  99,50 =    72 635 000
  tramo 3     930 000 a  99,00 =    92 070 000
  tramo 4   1 260 000 a  98,00 =   123 480 000
  tramo 5   1 760 000 a  96,00 =   168 960 000
  tramo 6   2 700 000 a  93,00 =   251 100 000
  tramo 7   3 400 000 a  88,00 =   299 200 000
  cola        800 000 a  84,00 =    67 200 000

  INGRESO      1 116 645 000
  VALOR A 100  1 200 000 000
  PRECIO MEDIO        93,05
  IMPACTO             6,95 %
  PÉRDIDA        83 355 000
```

## Venta escalonada

```text
  8 sesiones de 1 500 000, impacto 0,70 % cada una
  reposición del 70 % → residuo del 30 % por sesión

  impacto = 0,70 % × [1 + 7 × 0,30] = 2,17 %
  pérdida = 1 200 000 000 × 2,17 % = 26 040 000

  AHORRO FRENTE A LA VENTA DE GOLPE: 57 360 000
```

## El riesgo de esperar

```python
riesgo = riesgo_de_esperar(0.052, 4.0)   # 2,12 %
```

```text
  ahorro de escalonar      4,78 puntos
  riesgo de las 4 horas    2,12 puntos

  ESCALONAR SIGUE COMPENSANDO
  pero no por un margen cómodo,
  y en un día de tensión la relación se invierte:
  la volatilidad sube y el libro se repone menos.
```

## El límite de posición

```python
assert limite_de_posicion(_libro()) == 6_240_000
```

| Elemento | Valor |
|---|---|
| **Valor** | 6 240 000 |
| **Método** | 3 × profundidad al 1 %, medida sobre el libro |
| **Frecuencia** | Mensual, y tras cualquier episodio de tensión |
| **Disparador** | 80 % informa al comité · 100 % detiene compras · 110 % reduce en 5 días |

La posición actual de 12 000 000 **duplica** el límite.

## Señales de volumen inflado

- Volumen alto con libro fino: la relación volumen/profundidad es la señal más
  clara.
- Concentración del volumen en horarios estrechos o en tamaños idénticos.
- Órdenes grandes canceladas antes de ejecutarse, de forma repetida.
- Diferencias persistentes entre plataformas sin arbitraje que las corrija.
- Movimientos bruscos cerca de la hora de cálculo de un precio de referencia.

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Usar el volumen publicado | Es el dato más visible y el menos informativo |
| Suponer salida instantánea | El tiempo tiene su propio riesgo |
| Sumar la profundidad de varias plataformas | No es accesible a la vez |
| Rellenar la cola sin declararlo | Produce una cifra sin base |
| Medir solo en calma | Es cuando se hacen los informes y cuando menos importa |
| Límite sin disparador | Una cifra en una diapositiva no es un límite |

## Límites

- El libro es una foto: la resiliencia solo se observa tras una orden real, y el
  70 % de reposición es un supuesto.
- El modelo trabaja sobre un libro agregado; la fragmentación entre plataformas
  hace que esa agregación sobreestime lo accesible en tensión.
- La volatilidad del 5,2 % diario es un supuesto declarado y no se estima aquí.
- El precio de cola de 84,00 es arbitrario y su efecto sobre la pérdida es
  material: cambiarlo cambia la conclusión.
