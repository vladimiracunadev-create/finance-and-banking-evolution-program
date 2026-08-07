# Solución de referencia — Laboratorio 6: tensiones de diseño

> Material docente.

## Cinco decisiones correctas y dos contradicciones

Este es el laboratorio que justifica que el capstone exista. Cada decisión de las clases 4 a 11 era correcta por separado y estaba bien fundamentada; al hacerlas funcionar juntas un día, dos de ellas se contradicen.

## La tensión bloquea hasta declararse

```python
def test_una_tension_sin_resolver_bloquea_el_sistema_documenta_el_problema():
    s.declarar_tension("liquidacion atomica", "horario ampliado",
                       "prefinanciar mas horas encarece el saldo ocioso")

    puede, motivo = s.puede_operar()
    assert not puede
```

**Esta prueba debe pasar.** El sistema no puede operar con una tensión declarada y sin resolver, porque una contradicción no resuelta significa que dos partes del sistema se estorban sin que nadie haya decidido cuál cede.

## Resolver exige declarar el sacrificio

```python
with pytest.raises(ValueError):
    t.resolver("", 8_000)

t.resolver("via de excepcion con doble aprobacion", 8_000)
assert t.resuelta
```

Resolver una tensión es elegir, y elegir es sacrificar algo. Lo que el expediente exige no es que no haya sacrificios: es que estén escritos y cuantificados.

## La tolerancia la fija el consejo

```python
with pytest.raises(ValueError):
    s.fijar_tolerancia("liquidacion", 2.0, "sistemas")
```

La tolerancia al impacto se fija por función de negocio y desde la perspectiva del cliente. Si la fija el área que mide disponibilidad, sale una cifra técnica que no dice cuándo el daño es irreversible.

## Sin aprovisionamiento no se paga a nadie

```text
necesario      84 000
aprovisionado  82 500

  faltan 1 500 → NO SE PAGA A NADIE
```

Es la misma regla de la cola de redención: el orden de llegada no reparte, discrimina. Verificar antes convierte un fallo irrecuperable en uno recuperable.

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Diseñar solo el día uno | El día doscientos es el que rompe |
| Tolerancias fijadas por área | Un día completo las contrasta |
| Pagar sin verificar | Divide a los clientes sin criterio |
| Programar el embargo | Solo se diseña la inmovilización |
| Resolver tensiones en silencio | Se declaran en el expediente |

## Límites

- Las cinco tensiones modeladas son las de mayor frecuencia observada; no agotan las posibles.
- El coste anual de cada decisión es un **supuesto**: la comparación entre tensiones sí es robusta, las cifras absolutas no.
- El modelo no ordena las tensiones por importancia: esa es una decisión del consejo.
