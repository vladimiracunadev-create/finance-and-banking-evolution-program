# Solución de referencia — Laboratorio 2: calificación de instrumentos

> Material docente.

## Cuatro criterios cumplidos y una frase que los activa

El hecho decisivo del caso fue el menos jurídico de todos: el 92 % de los compradores no usaba el servicio. Si nueve de cada diez no lo compraron para usarlo, lo compraron esperando otra cosa, y esa expectativa es uno de los cuatro criterios.

## Los cuatro criterios

```text
1 inversión de dinero        sí
2 proyecto común            sí
3 expectativa de beneficio  sí
4 esfuerzo de un tercero    sí   ← el decisivo

CUATRO SÍES → VALOR
```

El cuarto es el que separa una compra de una inversión. Si el resultado depende del trabajo del promotor y el tenedor solo espera, está invirtiendo en él, no comprando un producto.

## La promoción forma parte de la calificación

```python
con_frase = _token_de_logistica()
sin_frase = _token_de_logistica(
    promocion=["El token da acceso a la plataforma."],
    compradores_que_usan_el_servicio=0.9,
)

assert con_frase.criterios().expectativa_de_beneficio
assert not sin_frase.criterios().expectativa_de_beneficio
```

**Esta prueba debe pasar.** Es el hallazgo del laboratorio: el mismo instrumento, con las mismas características técnicas, cambia de calificación según cómo se venda. Y no hace falta prometer rentabilidad: basta con crear la expectativa.

## Las tres defensas del emisor

```text
«se consume al contratar un servicio»
  → no hay servicio que contratar en 18 meses

«es una preventa, como un producto»
  → una preventa no tiene mercado secundario
    desde el día 1 ni se promociona por su precio

«no prometemos rentabilidad»
  → no hace falta prometerla: basta con
    crear la expectativa, y la frase la crea
```

Ninguna se sostiene, y las tres son las que aparecen en cualquier discusión sobre calificación. Conviene tenerlas escritas con su respuesta antes de la reunión.

## El ahorro frente al riesgo

```text
ahorro por calificar como utilidad     340 000
riesgo de la recalificación         30 400 000

el ahorro es el 1,1 % del riesgo
```

Ahí está el incentivo a calificar mal, y por eso la calificación no la elige quien emite. Un emisor que ahorra 340 000 pone en riesgo treinta millones y la responsabilidad de sus administradores.

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Calificar por el nombre | Lo elige el emisor |
| Ignorar la promoción | Es prueba y califica |
| «No prometemos rentabilidad» | Basta con crear la expectativa |
| Servicio futuro como utilidad | Tiene que funcionar hoy |
| Sin documento de calificación | Sin documento no hay calificación |

## Límites

- Los patrones de expectativa son una heurística: detectan las formulaciones habituales y no sustituyen la lectura del material completo.
- Los criterios implementados son los de uso más extendido; cada jurisdicción tiene los suyos y pueden diferir.
- El coste de cumplimiento por calificación es un **supuesto declarado** y varía mucho entre mercados.
