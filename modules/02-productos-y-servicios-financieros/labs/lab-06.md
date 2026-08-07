# Laboratorio 6: Proyecto: comparador de productos

## Propósito

Construir el comparador y **diseñar su salida de forma que no induzca a error**, que es más difícil que calcular bien.

Es el último laboratorio de la parte y la antesala del proyecto. Reúne los cinco anteriores y añade la exigencia que separa una herramienta útil de una que vende.

## Escenario

El comparador debe llevar a base común ofertas de crédito, de cuenta y de fondo, y presentar el resultado sin inclinar la decisión.

## Datos

Las ofertas usadas en los laboratorios 3, 4 y 5.

## Supuestos del ejercicio

- La base común es el costo total por peso obtenido o el rendimiento neto por peso invertido.
- Todos los supuestos se muestran en la propia salida.
- La herramienta declara qué no compara.

## Pasos

1. Escribe los requisitos como casos de prueba con valores esperados independientes.
2. Implementa la conversión a base común de los tres tipos de producto.
3. Diseña dos versiones de la salida: una que induce y otra que no, y compáralas.
4. Incluye los supuestos en la salida, no en una nota aparte.
5. Añade la sección de límites: qué no compara y por qué.
6. Valida contra los resultados calculados a mano en los laboratorios 3, 4 y 5.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los tres tipos se llevan a base común | Con la conversión visible |
| 2 | Las dos salidas se comparan | Y se explica qué induce en la primera |
| 3 | Los supuestos están en la salida | No en un anexo |
| 4 | Los límites están declarados | Al menos cinco |
| 5 | La validación usa los laboratorios previos | Con sus valores |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Ordenar por una sola variable | Induce a decidir por ella |
| Ocultar los supuestos | El resultado no se puede juzgar |
| Comparar productos de horizontes distintos | No son comparables |
| Validar contra el propio código | No valida nada |

## Entregables

- `solution.md` con las decisiones de diseño de la salida.
- El comparador con sus pruebas en verde.
- Las dos versiones de la salida, con lo que cambia entre ellas.
- La lista de límites declarados.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Base común correcta | 25 |
| Salida honesta | 25 |
| Supuestos en la salida | 20 |
| Límites declarados | 15 |
| Validación independiente | 15 |
