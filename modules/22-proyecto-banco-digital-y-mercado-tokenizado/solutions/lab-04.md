# Solución de referencia — Laboratorio 4: custodia integrada

> Material docente.

## El hallazgo mayor no estaba en las claves

El esquema 3-de-5 tenía una independencia efectiva de 1 y se arregló redistribuyendo. Lo que valía 19,7 millones era una cláusula ausente del contrato del custodio, y no la habría encontrado ninguna revisión técnica.

## La medición

```text
ANTES
  mayor grupo por ubicación     3
  mayor grupo por dispositivo   5
  independencia efectiva        1

DESPUÉS, SIN TOCAR EL UMBRAL
  mayor grupo por cualquier factor 2
  independencia efectiva           4
```

El umbral no cambió. Cambió dónde y con qué están las partes, y eso cuesta reorganizar personas, no rehacer criptografía.

## Las tres cláusulas

```text
propiedad del cliente        sí
prohibición de disponer      NO CONSTA
verificación independiente   NO

  sin la segunda, en un concurso los 180
  clientes son acreedores ordinarios
  pérdida = 24 000 000 × 82 % = 19 680 000
```

El coste de corregirlo es una cláusula y 34 000 al año de verificación. La desproporción entre el coste y el efecto es lo que hace de esta la revisión más rentable del capstone.

## El orden de la revocación

```text
1 el cliente revoca
2 los tokens del tercero se invalidan
3 SOLO ENTONCES se responde al cliente
```

Responder antes deja una ventana en la que el tercero sigue accediendo a datos que ya no debería ver. Medida en el sistema era de menos de un segundo, y bastaba.

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Umbral por intuición | «3 de 5 suena bien» no es un análisis |
| Mismo dispositivo | Una vulnerabilidad los tumba |
| Delegar y creerse cubierto | Las cláusulas deciden en el concurso |
| Verificar internamente | Lo hace quien podría tener la diferencia |
| Revocar y luego responder | Deja una ventana abierta |

## Límites

- El modelo de independencia usa cuatro factores; en la práctica hay más.
- La recuperación ordinaria del 18 % es un **supuesto** y depende de la masa y de la prelación.
- La verificación documental no sustituye una opinión jurídica sobre la oponibilidad de las cláusulas.
