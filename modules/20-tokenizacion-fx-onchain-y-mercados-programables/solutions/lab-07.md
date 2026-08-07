# Solución de referencia — Laboratorio 7: FX y ventana de exposición

> Material docente.

## El precio mostrado esconde cuatro de los seis tramos

Es el hallazgo de la clase 11.

```text
PAR PRINCIPAL
  mayorista   diferencial/2 0,6 + comisión 3,0  =  3,60 pb
  registro    margen 8,0 + diferencial/2 3,0
              + entrada 4,0 + salida 4,5        = 19,50 pb

  EL REGISTRO ES 5,4 VECES MÁS CARO
```

De los cuatro tramos del registro, **solo el diferencial sería visible en el
precio mostrado**. El margen sobre el precio importado, la entrada y la salida
no aparecen en ninguna comparación comercial.

## En el par poco líquido se invierte, y por una razón concreta

```text
PAR POCO LÍQUIDO
  mayorista   diferencial/2 22,5 + comisión 18
              + corresponsalía 22               = 62,50 pb
  registro    margen 12 + diferencial/2 9
              + entrada 4 + salida 4,5          = 29,50 pb

  AHORRO: 33,00 pb = 9 900 sobre 3 000 000
```

El ahorro **no viene del registro**: viene de eliminar dos tramos de
corresponsalía. Es exactamente la conclusión de la Parte 18, clase 16, y de la
ruta con stablecoin: el ahorro era de topología, no de tecnología.

## La profundidad corrige el ahorro anunciado

```python
corregido = ahorro_corregido_por_profundidad(33.0, 3_000_000, 5_200_000, 6)

assert corregido["impacto_pb"]     == pytest.approx(24.0, abs=0.2)
assert corregido["ahorro_real_pb"] == pytest.approx(9.0, abs=0.2)
```

```text
DE GOLPE
  3 000 000 / 5 200 000 = 0,58 veces la profundidad
  → impacto de 58 pb: se come el ahorro entero

EN SEIS TRAMOS DE 500 000
  impacto por tramo  500 000 / 5 200 000 × 100 = 9,6 pb
  con reposición del 70 %, residuo del 30 % por tramo:
  9,6 × [1 + 5 × 0,30] = 24,0 pb

  AHORRO REAL = 33 − 24 = 9 pb = 2 700
```

Y con un libro de 480 000 —diez veces más fino— el ahorro real es **negativo**:

```python
corregido = ahorro_corregido_por_profundidad(33.0, 3_000_000, 480_000, 6)
assert not corregido["sigue_compensando"]
```

## De dónde sale el precio

| Mecanismo | ¿Forma precio? |
|---|---|
| Oráculo que importa el precio | **No**: lo copia, con retardo y margen |
| Libro de órdenes propio | Sí |
| Fórmula automatizada | **No**: lo deriva de sus reservas |

En la práctica casi todo es la primera o la tercera. **El registro no forma
precio: lo consume, y le añade su propio coste.**

## La ventana va de irrevocable a confirmado

```python
normal = ventana_de_exposicion(10, 16, 11)
finde  = ventana_de_exposicion(10, 16, 11, dias_no_habiles=2)

assert normal.horas == 19
assert finde.horas  == 67
```

```text
DÍA NORMAL
  pago A irrevocable        10:00 hora de A
  confirmación de B         16:00 hora de B
                          = 05:00 del día siguiente en A
  VENTANA                   19 horas

VIERNES
  el sistema de B no reabre hasta el lunes
  VENTANA                   67 horas
```

Medir del envío a la recepción esperada subestima la exposición. Y el peor caso
—el fin de semana— **es recurrente, no excepcional**.

## Cada mecanismo contra la misma base

Es la trampa del ejercicio.

```text
PÉRDIDA ESPERADA SIN NINGÚN MECANISMO
  días normales   40 000 000 × 0,003 % × 0,55 × 250 = 165 000
  fines de semana 40 000 000 × 0,003 % × 2,8 × 0,55 × 50 = 92 400
  TOTAL = 257 400

                        PÉRDIDA      COSTE      TOTAL
  sin mecanismo          257 400          0    257 400
  solo neteo              46 332          0     46 332
  PvP sobre el bruto           0    860 000    860 000
  PvP sobre el neteado         0    154 800    154 800

  → SOLO NETEO es la opción más barata
```

**Si se compara el PvP con la pérdida que el neteo ya bajó a 46 332, el PvP
parece no compensar, y esa conclusión es falsa**: el PvP sustituye al neteo como
mecanismo, no se suma a él.

## Sin oponibilidad, el neteo no reduce nada

```python
def test_sin_oponibilidad_el_neteo_no_reduce_nada_documenta_el_problema():
    assert evaluacion["neteo"]["total"] == evaluacion["ninguno"]["total"]
    assert comparacion.mejor() == MecanismoLiquidacion.NINGUNO.value
```

**Esta prueba debe pasar.** Un acuerdo firmado que no es oponible en el concurso
de la contraparte no reduce la exposición, aunque el informe la declare
reducida.

```text
                        PÉRDIDA      COSTE      TOTAL
  sin mecanismo          257 400          0    257 400
  «neteo»                257 400          0    257 400
  PvP sobre el bruto           0    860 000    860 000

  → NINGÚN MECANISMO MEJORA
```

## El límite bilateral

```python
limite = limite_bilateral(_base(), 40_000_000, 80_000)
assert limite == pytest.approx(12_433_000, rel=0.01)
```

Cuando ningún mecanismo mejora, lo que procede es **reducir la exposición hasta
que la pérdida esperada quepa en el apetito**: 12 433 000 en vez de 40 000 000.

## La conclusión

La decisión no la determina el volumen sino **la oponibilidad jurídica del
acuerdo de neteo**. Con un acuerdo válido, el neteo basta y cuesta menos; sin él,
ningún mecanismo mejora y lo que procede es bajar el límite.

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Comparar precios mostrados | Se ignoran cuatro tramos |
| Suponer profundidad | El ahorro anunciado no se ejecuta |
| Medir la ventana del envío | Subestima la exposición |
| Olvidar el fin de semana | Es el peor caso y es recurrente |
| Dar el neteo por válido | Está firmado y puede no ser oponible |
| Comparar mecanismos entre sí | Cada uno contra la pérdida base |

## Límites

- Los tramos en puntos básicos son supuestos declarados: con otra estructura de
  comisiones el orden puede invertirse.
- El modelo de impacto por profundidad es lineal; en tensión el libro desaparece
  y el impacto no lo es.
- La probabilidad de incumplimiento del 0,003 % diario es una estimación de
  cartera, no de una contraparte concreta.
- El coste de prefinanciación supone que el saldo no rinde nada: si rinde algo,
  el coste del PvP baja y la comparación se acerca.
