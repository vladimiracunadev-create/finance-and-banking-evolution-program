# Solución de referencia — Laboratorio 2: análisis de una cartera de reservas

> Material docente.

## La cobertura sube y el riesgo empeora

Es el hallazgo del laboratorio y de la clase 4. La prueba lo documenta:

```python
def test_la_cobertura_sube_mientras_la_composicion_empeora_documenta_el_problema():
    cartera = _cartera()
    cobertura_antes = cartera.cobertura_contable   # 102,30 %
    iliquido_antes = cartera.peso_iliquido         # 15,17 %

    resultado = atender(cartera, 2_940_000_000)

    assert cartera.cobertura_contable > cobertura_antes   # 103,50 %
    assert cartera.peso_iliquido > iliquido_antes         #  23,06 %
    assert cartera.tramos["efectivo"] == 0
```

**Esta prueba debe pasar.** Documenta que la cifra publicada se mueve en
dirección contraria al riesgo real, y por eso una ficha de reservas necesita
composición y plazo, no solo el porcentaje.

## Las tres cifras

```text
                            ANTES      DESPUÉS
  cobertura contable       102,30 %    103,50 %   ← la que se publica
  cobertura líquida 24 h    86,30 %     78,93 %   ← la que paga
  peso ilíquido             15,17 %     23,06 %   ← la que anticipa

  efectivo                840 000 000        0
```

## Dos carteras con el mismo 102 %

```python
liquida  = Cartera(1_000, {"efectivo": 700, "letras": 320})
ilikida  = Cartera(1_000, {"efectivo": 200, "papel_comercial": 820})

assert liquida.cobertura_contable == ilikida.cobertura_contable  # 1,02
assert liquida.cobertura_liquida  >  ilikida.cobertura_liquida
```

Misma cifra publicada, riesgos opuestos. El papel comercial no está disponible en
24 horas, y por eso no cuenta en la cobertura líquida.

## El coste de la redención del 35 %

```text
NECESIDAD    2 940 000 000

ORDEN DE VENTA (coste creciente)
  efectivo         840 000 000   descuento 0,00 %
  pactos inversos  860 000 000   descuento 0,00 %
  subtotal       1 700 000 000

  falta          1 240 000 000
  en letras: 1 240 000 000 / 0,9985 = 1 241 862 794

COSTE = 1 862 794   →  0,063 % de lo redimido
```

## La escalera cambia la conclusión

```python
def test_la_escalera_encarece_la_venta_frente_al_descuento_constante():
    plano     = atender(_cartera(), 5_000_000_000).coste_de_venta
    creciente = atender(_cartera(), 5_000_000_000, escalera=True).coste_de_venta
    assert creciente > plano
```

Con descuento constante el margen aguanta cualquier venta de deuda; con escalera,
el punto de no retorno aparece entre los 4 000 y los 5 000 millones. **El
descuento no es una opinión pesimista: es la diferencia entre valorar y
realizar.**

## El segundo golpe

```text
REMANENTE TRAS LA PRIMERA REDENCIÓN
  circulante                5 460 000 000
  efectivo                              0
  letras                    1 768 137 206
  deuda 1–2 años            2 580 000 000
  papel comercial             945 000 000
  depósitos a plazo           358 200 000

SEGUNDA REDENCIÓN DEL 35 % = 1 911 000 000
  realizable a 24 h ≈ 4 309 364 000  → aún cubre

PERO el descuento del 1,40 % ya no vale:
vender 2 580 millones de deuda en un mercado
que sabe que hay una corrida es otra cosa.
```

Sobrevivir al primer escenario no dice nada sobre el segundo, y es el segundo el
que hunde a los emisores.

## Las cinco preguntas al informe

1. **¿Qué se atestigua exactamente?** ¿El saldo, la valoración, la titularidad?
2. **¿A qué fecha, y qué pasó los días alrededor?**
3. **¿Quién eligió la fecha?**
4. **¿Se verificó la titularidad**, no solo el saldo?
5. **¿Se verificó que no estaban pignorados?**

La cuarta y la quinta son las que suelen faltar, y son las que deciden en una
quiebra.

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Mirar solo el porcentaje | Es la única cifra publicada y la menos útil |
| Valorar a precio de pantalla | No es el precio de venta |
| Celebrar que la cobertura sube | Mira qué quedó en la cartera |
| Descuento constante | El punto de no retorno se aleja artificialmente |
| Un solo escenario | El segundo golpe es el que hunde |
| Aceptar «auditado» | Pregunta el alcance del encargo |

## Límites

- Los descuentos de `DESCUENTO_BASE` son **supuestos declarados**, no
  observaciones de mercado, y cambiarlos cambia la conclusión.
- La escalera multiplica por 1,5 cada mil millones: es una simplificación de un
  fenómeno que depende de la profundidad real de cada instrumento.
- El modelo supone que se vende primero lo barato; un emisor bajo presión puede
  no comportarse así.
