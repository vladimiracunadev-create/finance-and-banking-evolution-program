# Solución de referencia — Laboratorio 4: consenso con nodos defectuosos

> Material docente.

## Contar nodos no es contar independencias

Es el hallazgo del laboratorio y de la clase 5.

```text
n = 5, f = 1
  el protocolo tolera UN nodo que miente

  PERO si 3 de los 5 ejecutan la misma implementación
  y esa implementación tiene un defecto que produce
  el mismo resultado incorrecto en los tres:

  → 3 votos coincidentes y erróneos
  → 3 ≥ 2f + 1 = 3
  → EL SISTEMA ACUERDA UN VALOR ERRÓNEO
```

El consenso bizantino tolera participantes que mienten **de forma
independiente**. Tres nodos que se equivocan igual no son tres fallos: son uno.

## Umbral medido

```text
n = 4 (f = 1)
  0 mentirosos  → acuerdo en 1 ronda
  1 mentiroso   → acuerdo en 1 ronda
  2 mentirosos  → SIN acuerdo, el sistema se detiene

n = 7 (f = 2)
  2 mentirosos  → acuerdo
  3 mentirosos  → SIN acuerdo

MEDIDO, NO SUPUESTO: el laboratorio lo ejecuta.
```

## Detenerse en vez de divergir

```python
def test_sin_quorum_no_hay_dos_estados(red):
    red.configurar(nodos=4, mentirosos=2)
    resultado = red.ejecutar_ronda()

    assert resultado.decidido is False
    estados = {n.estado_actual() for n in red.nodos_honestos()}
    assert len(estados) == 1     # todos en el MISMO estado anterior
```

La segunda comprobación es la importante: sin quórum, los honestos no avanzan y
no divergen. En finanzas eso es lo correcto (clase 1): divergir es crear dinero.

## El fallo común

```python
def test_el_fallo_comun_produce_acuerdo_erroneo(red):
    # Tres nodos con la MISMA implementacion defectuosa:
    # no mienten, se equivocan igual.
    red.configurar(nodos=5, con_defecto_comun=3)
    resultado = red.ejecutar_ronda()

    assert resultado.decidido is True
    assert resultado.valor == VALOR_INCORRECTO
```

Esta prueba **debe pasar**. Documenta la limitación que ningún umbral corrige y
que el expediente de la clase 14 tiene que declarar como riesgo residual.

## Mensajes por ronda

```text
n = 4   → 16 mensajes
n = 7   → 49
n = 10  → 100

crecimiento cuadrático confirmado

CON n ENTRE 5 Y 20, ES IRRELEVANTE
  el «no escala» que se le reprocha al consenso
  bizantino es un criterio de red abierta,
  no de consorcio
```

## Detección de desviación de orden

```python
def desviacion(bloque, mempool_firmada) -> list[str]:
    """Devuelve las operaciones incluidas fuera de su turno."""
    esperado = sorted(mempool_firmada, key=lambda t: (t.recibido_en, t.id))
    incluidas = bloque.transacciones
    fuera = []
    for posicion, tx in enumerate(incluidas):
        if posicion < len(esperado) and tx.id != esperado[posicion].id:
            fuera.append(tx.id)
    return fuera
```

No impide la desviación: la hace **detectable y atribuible**, que es lo
alcanzable (clase 5).

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Suponer el umbral | El laboratorio existe para medirlo |
| No probar el fallo común | Es el hallazgo de la clase |
| Comprobar solo que no hay acuerdo | Falta comprobar que no divergen |
| Concluir que «no escala» | Con pocos participantes escala |
| Rotación sin detección | Resuelve el turno, no la elección |

## Límites

- El protocolo es **didáctico**: no reproduce ningún protocolo de producción ni
  sus optimizaciones.
- No se modela la pérdida de mensajes ni la partición de red salvo cuando se
  indica.
- Los relojes están sincronizados; en producción el desajuste produce
  reorganizaciones espurias (clase 6).
