# Solución de referencia — Laboratorio 2: emisión y ciclo de vida

> Material docente.

## El bloqueo del importe es lo que hace informar al libro

Es el hallazgo de la clase 4.

```python
sin = _emision(bloqueo=False)
con = _emision(bloqueo=True)

assert sin.coste_del_bloqueo(500_000) == 0.0
assert con.coste_del_bloqueo(500_000) == pytest.approx(583, abs=2)
```

```text
500 000 × 4,2 % × 10/360 = 583

Para recibir 84 668 adjudicados, el inversionista
pagó 583 de coste de oportunidad: un 0,69 %.

EFECTO SOBRE LA DEMANDA
  la exageración baja de 2,86× a un supuesto 1,4×
  y el libro empieza a informar
```

Sin ese coste, pedir de más es gratis y todo el mundo lo hace.

## La sobredemanda es en su mayor parte artificial

```text
DEMANDA REGISTRADA        112 400 000   3,75 veces
FACTOR DE EXAGERACIÓN            2,86   (supuesto declarado)
DEMANDA GENUINA            39 300 000   1,31 veces

DECIDIR SOBRE EL LIBRO SIN CORREGIRLO
llevaría a encarecer la siguiente emisión
hasta dejarla desierta.
```

El factor es un **supuesto del analista** y el código lo exige explícitamente:
`demanda_genuina(0)` lanza `ValueError`.

## Los tres mecanismos

```text
                        VENTAJA DEL PRIMERO   inv0 recibe

  orden de llegada            1,0000            16 529
  prorrateo simple            0,0000             4 412
  prorrateo con mínimo        0,0000             4 412
```

Con órdenes homogéneas el tramo mínimo no cambia el resultado; con órdenes
desiguales sí, y esa es la prueba que lo demuestra:

```python
def test_el_tramo_minimo_redistribuye_hacia_el_pequeno():
    assert pequeno.fraccion > grande.fraccion
    assert pequeno.adjudicado >= 2_000
```

## La emisión desierta

```python
resultado = emision.adjudicar(Mecanismo.PRORRATEO_SIMPLE)

assert resultado.desierta
assert resultado.colocado == 0
assert all(a.adjudicado == 0 for a in resultado.adjudicaciones)
```

```text
demanda 15 000 000 < mínimo 18 000 000

  · no se anota ninguna unidad
  · todos los bloqueos se liberan en el mismo acto
  · los costes incurridos los asume el emisor,
    según lo declarado en el folleto

LO QUE NO DEBE OCURRIR
  reducir el mínimo sobre la marcha,
  emitir por lo suscrito sin decirlo antes,
  o retener los importes «por si acaso».
```

## Sin aprovisionamiento no se paga a nadie

```python
def test_sin_aprovisionamiento_no_se_paga_a_nadie_documenta_el_problema():
    with pytest.raises(AprovisionamientoInsuficiente):
        bono.pagar_cupon(foto, necesario - 1)

    assert bono.pagos_confirmados == set()
```

**Esta prueba debe pasar.** Un contrato que paga por orden hasta quedarse sin
fondos divide a los tenedores en dos grupos sin ningún criterio: es el mismo
principio de la Parte 20, clase 5, donde el orden de llegada no reparte,
discrimina.

La segunda comprobación es la importante: **nadie cobró**. Verificar antes de
empezar es lo que permite que el fallo sea recuperable.

## El cupón con incidencias

```text
cupón por unidad   1 000 × 6,4 % / 2 = 32
necesario          32 × 30 000 = 960 000

DETALLE POR TITULAR
  t0, t1, t2   CUENTA_BLOQUEADA    reintento a 5, 15 y 30 días
  t5           NO_LOCALIZABLE      notificación y conservación
  t10          INMOVILIZADO        consignado a la autoridad
  resto        PAGADO
```

## El inmovilizado conserva su derecho

```python
bono.inmovilizar("t10", 750, ("operaciones", "cumplimiento"), "orden judicial")
resultado = bono.pagar_cupon(foto, bono.cupon_total(foto))

assert resultado.detalle["t10"] is EstadoPago.INMOVILIZADO
assert resultado.pendiente >= 32 * 750
```

El embargo llegó después de la fecha de corte: **ese titular tiene derecho al
cupón**. El importe se consigna a disposición de la autoridad; no se anula, y
las unidades no se transfieren a nadie.

Y la función exige dos aprobadores distintos:

```python
with pytest.raises(SinDobleAprobacion):
    bono.inmovilizar("t1", 750, ("operaciones", "operaciones"), "orden")
```

## El vencimiento

```python
cierre = bono.vencer(bono.pagos_confirmados)

assert cierre["destruidas"] > 0
assert cierre["vivas"] > 0
assert cierre["destruidas"] + cierre["vivas"] == 40 * 750
```

**Solo se destruye lo pagado y confirmado.** Destruir todas las unidades a la
vez deja sin instrumento —y sin prueba de su derecho— a quien todavía no ha
cobrado.

## El error de una hora en la fecha de corte

```text
46 operaciones en la ventana · 214 unidades afectadas

  importe en disputa   214 × 32 =  6 848
  coste de corregirlo  92 × 85  =  7 820

  CORREGIR CUESTA MÁS QUE EL IMPORTE
```

El problema no es el importe: es que 46 tenedores recibieron lo que no les
correspondía y hay que recuperar dinero ya pagado a personas identificadas.

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Leer el libro literalmente | La mayor parte de la demanda es artificial |
| Adjudicar por orden de llegada | Crea la carrera por el papel |
| Pagar sin verificar fondos | Divide a los tenedores sin criterio |
| Tomar el corte donde conviene | Se toma en el registro de referencia |
| Destruir todo al vencer | El no cobrado pierde la prueba de su derecho |
| Inmovilizar con un solo aprobador | Un actor no debe poder hacerlo solo |

## Límites

- El factor de exageración es un supuesto y no se observa: se estima con el
  histórico de emisiones comparables del propio colocador.
- El modelo de reintento se describe pero no se implementa: exige un calendario
  y un sistema de notificación que quedan fuera del laboratorio.
- El instrumento tiene un solo tipo de cupón; los cupones variables exigen un
  oráculo y con él vuelven los problemas de la Parte 19, clase 9.
