# Laboratorio 1: Modelo de negocio bancario

## Propósito

Descomponer el resultado de tres bancos y **encontrar el que es rentable hoy y no sostenible**.

Es el primer laboratorio de la parte y el que instala su mirada. Un banco puede ejecutar impecablemente un modelo que ya no rinde, y eso no aparece en ningún indicador operativo.

## Escenario

Tres bancos con rentabilidad sobre patrimonio parecida y modelos de negocio muy distintos: minorista de volumen, empresas de nicho y tesorería.

## Datos

Los estados de los tres durante cinco años, con su detalle de margen y comisiones.

## Supuestos del ejercicio

- Los tres tienen rentabilidad sobre patrimonio entre el 11 % y el 13 %.
- El grupo de pares se entrega con su criterio de selección.
- Un banco depende del margen de un producto que la competencia está erosionando.

## Pasos

1. Descompón el resultado de cada uno en sus componentes.
2. Sigue la tendencia de cada componente durante los cinco años.
3. Identifica el banco cuyo agregado es estable con componentes que se compensan.
4. Comprueba las señales de agotamiento del modelo en cada uno.
5. Distingue la viabilidad de la sostenibilidad y evalúa las dos por banco.
6. Compara con el grupo de pares y verifica que el grupo está bien elegido.
7. Determina cuál de los tres tiene un problema y cuánto tiempo le queda.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | El resultado está descompuesto | Los tres bancos |
| 2 | Las tendencias por componente están seguidas | Cinco años |
| 3 | El caso de compensación está identificado | Con sus componentes |
| 4 | Viabilidad y sostenibilidad se evalúan aparte | Por banco |
| 5 | El grupo de pares está verificado | Con su criterio |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Mirar el agregado | Componentes que se compensan esconden el problema |
| Confundir viabilidad con sostenibilidad | Son dos preguntas y dos horizontes |
| Comparar con un grupo de pares mal elegido | La comparación no informa |
| Ignorar las señales de agotamiento | Aparecen antes que la caída del resultado |

## Entregables

- `solution.md` con la descomposición de los tres.
- Las tendencias por componente.
- La evaluación separada de viabilidad y sostenibilidad.
- El banco con problema y su horizonte.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Descomposición | 25 |
| Tendencias | 20 |
| Caso de compensación | 20 |
| Viabilidad y sostenibilidad | 20 |
| Grupo de pares | 15 |
