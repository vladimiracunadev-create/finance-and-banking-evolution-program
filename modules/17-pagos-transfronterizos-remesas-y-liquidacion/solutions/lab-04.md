# Solución de referencia — Laboratorio 4: screening y reparaciones

> Material docente. Los nombres y la lista son **sintéticos**.

## La respuesta escrita al área de negocio

> La propuesta de subir el umbral del 82 % al 90 % reduce las alertas un 58 % y
> ahorra unos 200 000 al trimestre. La prueba retrospectiva sobre las 9
> coincidencias confirmadas del periodo muestra que **3 de ellas quedaban por
> debajo del 90 %**: con el umbral propuesto, esas tres operaciones se habrían
> ejecutado.
>
> Una operación ejecutada con una persona designada no es un riesgo que se pueda
> comparar con un ahorro operativo. La propuesta se rechaza.
>
> El problema que la motiva es real. La corrección propuesta actúa sobre la
> calidad de la comparación y reduce las alertas un 75 % **mejorando** la
> detección: pasa de 41 a 57 casos detectados sobre 60 en el conjunto de prueba.

## Métricas por umbral

```text
umbral   alertas   VP   FP      precisión   exhaustividad
 70 %    52 400     9   52 391    0,017 %      100 %
 78 %    41 100     9   41 091    0,022 %      100 %
 82 %    31 500     9   31 491    0,029 %      100 %
 86 %    21 900     8   21 892    0,037 %     88,9 %
 90 %    13 230     6   13 224    0,045 %     66,7 %
 95 %     4 800     3    4 797    0,063 %     33,3 %
```

La precisión mejora con el umbral y la exhaustividad se desploma. **En sanciones
manda la segunda columna.**

## Clasificación de falsos positivos

| Causa | Casos | % | Corrección | Efecto |
|---|---:|---:|---|---:|
| Apellido de alta frecuencia | 14 220 | 45,7 % | Exigir segundo campo coincidente | −11 400 |
| Transliteración | 7 890 | 25,4 % | Normalización fonética por origen | −6 300 |
| Falta fecha de nacimiento | 5 106 | 16,4 % | Exigir el campo en el mensaje | −4 100 |
| Entidad con nombre genérico | 2 480 | 8,0 % | Depurar la lista | −1 900 |
| Otras | 1 422 | 4,6 % | — | — |

## La corrección que mejora las dos métricas

```python
def coincide(nombre_pago: str, entrada: EntradaLista, umbral: float) -> Match | None:
    a = normalizar(nombre_pago, origen=detectar_origen(nombre_pago))
    b = normalizar(entrada.nombre, origen=entrada.origen)

    puntuacion = similitud(a, b)
    if puntuacion < umbral:
        return None

    # Apellido de alta frecuencia: exige un segundo campo.
    if apellido_frecuente(a):
        if not entrada.fecha_nacimiento:
            # NO se descarta: se escala. La ausencia del dato
            # no puede convertirse en un descarte automatico.
            return Match(puntuacion, motivo="apellido frecuente, sin fecha")
        if not coincide_fecha(nombre_pago, entrada):
            return None

    return Match(puntuacion, motivo="coincidencia de nombre")
```

La línea que la corrección busca es la marcada: cuando falta el dato que
permitiría descartar, **el caso se escala, no se descarta**. Descartar por falta
de información es exactamente el falso negativo que hay que evitar.

## La normalización fonética mejora la exhaustividad

```text
CONJUNTO DE PRUEBA: 60 variantes conocidas de nombres designados

  sistema actual (comparación literal):     41 de 60
  con normalización fonética:               57 de 60

  los 3 no detectados se documentan uno a uno
  como limitación conocida, con su plan
```

Este es el resultado que justifica todo el laboratorio: **reducir el ruido
mejoró la detección**, porque el ruido venía de comparar mal, no de comparar
mucho.

## El beneficio que no es el ahorro

```text
CON 31 500 ALERTAS Y 14 REVISORES
  31 500 × 6 min = 3 150 h/trimestre
  225 h por persona de 480 disponibles
  → casi la mitad del tiempo revisando ruido

CON 7 800 ALERTAS
  56 h por persona
  → tiempo para el análisis que sí lo merece
```

Un equipo que revisa 225 horas de ruido comete errores por fatiga. La reducción
del ruido no ahorra dinero: **evita falsos negativos por agotamiento**.

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Subir el umbral sin prueba retrospectiva | Es la decisión que la clase prohíbe |
| Descartar por falta de dato | Convierte la ausencia en un descarte |
| Reportar solo precisión | La exhaustividad es la que importa |
| Descarte sin motivo registrado | No se puede auditar |
| Presentar la lista sintética como real | Confusión grave |

## Límites

- La lista y los nombres son sintéticos y no reproducen la distribución real de
  ninguna lista oficial.
- El laboratorio no cubre el componente de comportamiento del modelo de
  prevención de lavado, que tiene su propia calibración.
- La etiqueta de resolución está disponible, cosa que en producción no ocurre:
  la calibración real exige revisión humana muestreada.
