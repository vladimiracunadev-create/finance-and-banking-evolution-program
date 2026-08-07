# Onchain FX Lab

Laboratorio de cambio de divisas sobre registros de la **Parte 21**. Tres módulos
que implementan el coste total por ruta, el creador de mercado automatizado y el
riesgo de liquidación, **con la biblioteca estándar y sin red**.

> ## Aviso
>
> **Todo lo que hay aquí es didáctico y trabaja con datos sintéticos.** No se
> conecta a ninguna plataforma, no ejecuta ninguna operación real y **no
> recomienda ninguna estrategia ni ningún proveedor**.

## Qué demuestra ejecutando

| Afirmación habitual | Lo que el laboratorio demuestra | Clase |
|---|---|---|
| «El precio es el mismo» | El mostrado esconde cuatro de los seis tramos | 11 |
| «Ahorra 33 puntos básicos» | 9 tras medir la profundidad del libro | 11 |
| «Rinde un 12,6 % por comisiones» | La divergencia se come una parte | 13 |
| «Siempre hay precio» | Y puede ser ruinoso: dar precio no es dar liquidez | 13 |
| «Tenemos acuerdo de neteo» | Solo vale si es oponible en concurso | 12 |

## Estructura

```text
apps/onchain_fx_lab/
├── README.md
├── __init__.py
├── pricing.py     rutas, tramos y corrección por profundidad
├── amm.py         producto constante, deslizamiento y divergencia
├── settlement.py  ventana, neteo, límites y pago contra pago
└── cli.py
```

## Uso

Comparar el coste total en un par principal y en uno poco líquido:

```bash
python apps/onchain_fx_lab/cli.py pricing --notional 3000000
```

Medir el deslizamiento y la pérdida por divergencia:

```bash
python apps/onchain_fx_lab/cli.py amm --rounds 4
```

Comparar los mecanismos de riesgo de liquidación contra la misma base:

```bash
python apps/onchain_fx_lab/cli.py settlement
```

## Pruebas

```bash
python -m pytest tests/test_onchain_fx_lab.py -q
```

Dos de ellas **documentan un error de razonamiento y deben pasar**:

- `test_el_precio_mostrado_esconde_cuatro_tramos_documenta_el_problema`
- `test_sin_oponibilidad_el_neteo_no_reduce_nada_documenta_el_problema`

## Decisiones de diseño que conviene mirar

**Cada mecanismo se compara con la pérdida sin ningún mecanismo.** Es la trampa
de la clase 12: comparar el pago contra pago con la pérdida que el neteo ya
redujo invierte la conclusión. `Comparacion.evaluar()` devuelve las cuatro filas
contra la misma base para que el error no se pueda cometer.

**`neteo_oponible` es un parámetro y no un supuesto silencioso.** Un acuerdo
firmado que no es oponible en el concurso de la contraparte no reduce nada, y el
código lo modela: con `False`, el neteo da exactamente el mismo total que no
tener mecanismo.

**La ventana va de irrevocable a confirmado.** `ventana_de_exposicion` recibe la
hora de irrevocabilidad y la de confirmación, no las de envío, y admite días no
hábiles para calcular el peor caso, que es el viernes y es recurrente.

**La piscina nunca se vacía, y eso no es una buena noticia.** Es la propiedad del
producto constante: siempre hay precio, y ese precio puede ser ruinoso. Dar
precio no es lo mismo que dar liquidez.

**`Mecanismo.forma_precio` distingue los tres orígenes.** Solo un libro propio
forma precio; el oráculo lo copia y la fórmula lo deriva de sus reservas. Es lo
que sostiene que el registro consume precio en vez de formarlo.

**`razon_que_anula_las_comisiones` se resuelve por bisección** sobre un tramo
donde la función es monótona, de modo que converge siempre y no depende de un
punto de partida afortunado.

## Límites declarados

- La fórmula implementada es la de producto constante; otras curvas tienen
  perfiles de deslizamiento y de divergencia distintos.
- El impacto de mercado es lineal por importe vendido: en tensión el libro
  desaparece y deja de serlo.
- Los tramos en puntos básicos son **supuestos declarados**: con otra estructura
  de comisiones el orden de preferencia entre rutas puede invertirse.
- La probabilidad de incumplimiento es una estimación de cartera, no de una
  contraparte concreta.
- No se modela el arbitraje: se supone que el precio converge al externo, y en un
  mercado sin arbitrajistas puede no hacerlo.
- El coste de prefinanciación supone que el saldo no rinde nada; si rinde algo,
  el coste del pago contra pago baja.

## Referencias

- [Parte 21 — Tokenización, FX on-chain y mercados programables](../../modules/20-tokenizacion-fx-onchain-y-mercados-programables/README.md)
- [`apps/tokenization_platform/`](../tokenization_platform/README.md)
- [Parte 18 — Pagos transfronterizos](../../modules/17-pagos-transfronterizos-remesas-y-liquidacion/README.md)
- [Etapa 5](../../docs/etapa-5-finanzas-digitales.md)
