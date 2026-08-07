# Laboratorio 2: Ingresos y estabilidad

## Propósito

Pasar cuatro rentas por los tres filtros y **comprobar que la de mayor media no es la de mayor renta admisible**.

El laboratorio 1 mostró dónde nace el problema. Este entra en la primera variable de la admisión, donde la cifra que se usa casi nunca es la que el solicitante declara.

## Escenario

Cuatro solicitantes con renta media parecida y variabilidad muy distinta: sueldo fijo, comisiones, honorarios y renta mixta con bonos anuales.

## Datos

Veinticuatro meses de ingreso de cada uno, con su documentación de respaldo.

## Supuestos del ejercicio

- El coeficiente de variación se calcula sobre los últimos 24 meses.
- Las ponderaciones de referencia por tipo de renta se entregan como dato.
- Los bonos anuales se anualizan y se ponderan aparte.

## Pasos

1. Clasifica cada componente de renta por su tipo.
2. Calcula el coeficiente de variación de cada solicitante.
3. Aplica los tres filtros: declarada, acreditada y admisible.
4. Pondera cada componente según su estabilidad medida.
5. Ordena los cuatro por renta media y por renta admisible, y compara los órdenes.
6. Detecta las señales de ingreso sobreestimado en la documentación de uno de ellos.
7. Calcula cuánto cambia la renta admisible si se usan 12 meses en vez de 24.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Cada componente está clasificado | Por tipo de renta |
| 2 | El coeficiente de variación está calculado | Los cuatro |
| 3 | Los tres filtros están aplicados | En orden |
| 4 | Los dos órdenes se comparan | Y no coinciden |
| 5 | Las señales de sobreestimación están detectadas | En el caso que las tiene |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Usar la renta declarada | Es el primer filtro, no el resultado |
| Tomar la renta variable entera | Se pondera por su estabilidad medida |
| Usar la media sin la variabilidad | Dos medias iguales soportan compromisos distintos |
| Ignorar el plazo de la serie | Doce meses pueden esconder la estacionalidad |

## Entregables

- `solution.md` con los tres filtros aplicados a los cuatro.
- Los coeficientes de variación y las ponderaciones.
- Los dos órdenes comparados.
- Las señales de sobreestimación detectadas.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Clasificación de rentas | 20 |
| Coeficientes de variación | 20 |
| Tres filtros | 25 |
| Órdenes comparados | 20 |
| Señales detectadas | 15 |
