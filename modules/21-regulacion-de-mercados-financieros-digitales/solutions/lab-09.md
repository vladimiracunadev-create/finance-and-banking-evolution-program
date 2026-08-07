# Solución de referencia — Laboratorio 9: expediente regulatorio

> Material docente.

## Cuatro hallazgos bloqueantes y ninguno visible dentro de su pieza

Las doce piezas eran correctas por separado y el conjunto tenía cuatro hallazgos bloqueantes. Los cuatro aparecieron al leer el expediente por parejas, que es exactamente como lo lee un supervisor en su primera revisión.

## Las cinco parejas críticas

```text
perímetro     x resiliencia
  «no custodiamos» frente a 4 de 5 partes

calificación  x conducta
  «es utilidad» frente a la promoción

salvaguarda   x prevención
  «cuenta segregada» frente a devoluciones
  desde la operativa

datos         x vigilancia
  «no hay dato personal» frente al análisis
  de direcciones vinculadas

jurisdicción  x conducta
  «solo régimen local» frente a tres idiomas
```

Cada contradicción enfrenta una afirmación con un hecho descrito en otra pieza. Ninguna es detectable leyendo la pieza que la contiene, y las cinco lo son leyendo dos.

## La evidencia no es opcional

```python
def test_una_afirmacion_sin_evidencia_se_rechaza():
    with pytest.raises(AfirmacionSinEvidencia):
        expediente.afirmar("perimetro", "no custodiamos", evidencia="")
```

Un supervisor que encuentra una afirmación sin respaldo revisa las demás con otra actitud. Por eso la regla no es «anotar la carencia» sino retirar la afirmación del expediente.

## La priorización por efecto

```text
nivel 1  42 000 clientes  custodia no declarada
nivel 1  42 000 clientes  fondos no segregados
nivel 1  11 400 clientes  promoción que califica
nivel 2  42 000 clientes  datos no declarados
```

El criterio no es la gravedad formal de la infracción sino qué le pasa al cliente. Y hay una comprobación de control: si todos los hallazgos son de nivel 3, la revisión no ha mirado donde debía.

## La medida provisional

```python
def test_la_remediacion_exige_medida_provisional_documenta_el_problema():
    with pytest.raises(ValueError):
        expediente.remediar(..., medida_provisional="")
```

**Esta prueba debe pasar.** Entre que se detecta un hallazgo y se corrige hay un intervalo, y el cliente está expuesto durante ese intervalo. Es el elemento que falta en casi todos los planes de remediación.

## La respuesta honesta

```text
«si quiebran mañana, ¿qué recupera el cliente?»

HOY: no se puede afirmar, porque el hallazgo
     de salvaguarda impide sostener la segregación

TRAS LA REMEDIACIÓN: el 99,5 %, acreditado
```

Decir «hoy no puedo afirmarlo» vale más que una afirmación sin evidencia, y es lo que distingue un expediente defendible de uno que se cae en la segunda pregunta.

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Leer de principio a fin | Léelo por parejas de piezas |
| Cada equipo entrega su pieza | Alguien tiene que cruzarlas |
| Priorizar por gravedad formal | Prioriza por efecto sobre el cliente |
| Plan sin provisional | El intervalo también expone |
| Defender lo que no se sostiene | «Hoy no puedo afirmarlo» vale más |

## Límites

- Las cinco parejas críticas son las de mayor rendimiento observado; no agotan las combinaciones posibles.
- El expediente modela la estructura, no el contenido jurídico: cada pieza exige el análisis de un especialista.
- La conclusión de `puede_operar()` es **didáctica** y no sustituye ninguna resolución administrativa.
