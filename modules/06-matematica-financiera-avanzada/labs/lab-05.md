# Laboratorio 5: Sensibilidad

## Propósito

Construir el diagrama de tornado de un proyecto y **comprobar que la variable dominante no es la que más se discutió**.

El laboratorio 4 decidió con una cifra. Este mide de qué depende esa cifra, y su resultado reordena la discusión antes de que empiece.

## Escenario

Un proyecto con ocho variables, de las cuales el comité discutió principalmente dos y ninguna de ellas es la que más pesa.

## Datos

El modelo del proyecto con sus ocho variables y sus rangos plausibles.

## Supuestos del ejercicio

- Los rangos de cada variable se entregan con su fundamento.
- El caso base es el aprobado por el comité.
- Las variables se mueven una a una, manteniendo el resto en el caso base.

## Pasos

1. Calcula el resultado del caso base.
2. Mueve cada variable a los extremos de su rango y registra el efecto.
3. Construye el diagrama de tornado ordenando por amplitud del efecto.
4. Compara el orden con las dos variables que el comité discutió.
5. Calcula el valor de equilibrio de las tres variables dominantes.
6. Expresa el margen de seguridad de cada una como distancia porcentual al caso base.
7. Construye una sensibilidad bivariante con las dos primeras.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | El tornado está construido y ordenado | Por amplitud del efecto |
| 2 | El orden se contrasta con lo discutido | Y no coincide |
| 3 | Los valores de equilibrio están calculados | De las tres dominantes |
| 4 | El margen de seguridad está expresado | En porcentaje |
| 5 | La bivariante está construida | Con las dos primeras |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Mover variables en proporciones distintas | Los efectos dejan de ser comparables |
| Usar rangos sin fundamento | El tornado ordena por el rango, no por la variable |
| No calcular el valor de equilibrio | Es lo más comunicable del análisis |
| Mover varias a la vez en la univariante | Es otro análisis distinto |

## Entregables

- `solution.md` con el diagrama de tornado.
- El contraste entre el orden y lo discutido por el comité.
- Los valores de equilibrio de las tres dominantes.
- La sensibilidad bivariante.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Tornado correcto | 30 |
| Contraste con lo discutido | 20 |
| Valores de equilibrio | 25 |
| Margen de seguridad | 15 |
| Bivariante | 10 |
