# Solución de referencia — Laboratorio 8: escenario de tensión

> Material docente.

## Un proveedor con tres papeles rompió tres componentes

El escenario no combinó tres fallos independientes —eso sería improbable— sino un solo fallo correlacionado. La fuente era un banco corresponsal que emitía el depósito, liquidaba los pagos y custodiaba efectivo.

## La fuente de correlación

```python
def test_un_proveedor_con_varios_papeles_es_la_fuente_documenta_el_problema():
    assert proveedor.es_fuente_de_correlacion

    nuevos = e.desencadenar(72.0, "problemas de liquidez")
    assert len(nuevos) == 3
```

**Esta prueba debe pasar.** Un solo fallo alcanza a los tres papeles a la vez, y por eso lo que en la declaración eran tres dependencias distintas es en realidad una.

## Un escenario de un componente no enseña nada

```python
simple = Proveedor("x", frozenset({"uno"}))
e = Escenario(simple)
e.desencadenar(2.0, "caida")
assert not e.demuestra_algo
```

El modelo se niega a considerar demostrativo un escenario que afecta a un solo componente, porque probar que un sistema sobrevive a un fallo aislado no dice nada sobre su resiliencia.

## A cuántas desviaciones está

```text
caída del 9 % con volatilidad diaria
del 1,8 % → 5,0 desviaciones

  en un día es improbable
  en una semana está a 1,9
```

La pregunta que cierra el escenario es esa: si el punto de rotura está a menos de tres desviaciones, no es un escenario adverso, es un martes.

## Las correcciones y con qué se comparan

```text
segundo emisor           18 000 al año
corresponsal alternativo 12 000 al año
TOTAL                    30 000

  menos que un solo día de interrupción
```

Y el nivel de prueba se declara: nivel 3 de 5, con compromiso de nivel 4 en seis meses. «Se probó la continuidad» no informa; «nivel 3» sí.

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Escenario que el sistema aguanta | No enseña nada |
| Fallos independientes | La correlación hace el episodio |
| Un proveedor con varios papeles | Es la fuente |
| Reportar sin nivel | Sin nivel no informa |
| Alternativa sin acuerdo | Sin firma no existe |

## Límites

- El escenario es **sintético** y su plausibilidad depende de la volatilidad supuesta.
- El modelo conserva la peor interrupción por componente y no acumula fallos sucesivos sobre el mismo.
- El coste de un día de interrupción no incluye el efecto reputacional a medio plazo, que suele dominar.
