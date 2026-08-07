# Laboratorio 2: Variaciones porcentuales e índices

## Propósito

Medir el mismo cambio de tres maneras y comprobar que **las tres son correctas y cuentan historias distintas**.

El laboratorio 1 dejó las cifras ordenadas. Este las pone en el tiempo, que es donde la elección de la base decide la conclusión.

## Escenario

Una serie de colocaciones mensuales de un banco durante 24 meses. La dirección pregunta «cuánto crecimos» y hay tres respuestas defendibles.

## Datos

Serie sintética de 24 meses con estacionalidad y un salto en el mes 14.

## Supuestos del ejercicio

- La serie es nominal; la inflación se entrega aparte.
- El mes 14 incorpora una cartera adquirida, no crecimiento orgánico.
- El año base para el índice se elige y se justifica.

## Pasos

1. Calcula la variación mes contra mes, en doce meses y acumulada.
2. Construye el número índice con base 100 en el mes que justifiques.
3. Calcula la media geométrica del crecimiento y compárala con la aritmética.
4. Deflacta la serie con el índice de precios entregado.
5. Explica qué respuesta darías a la dirección y por qué.
6. Señala el efecto del mes 14 y cómo lo tratarías.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Las tres variaciones calculadas | Con su fórmula visible |
| 2 | El año base justificado | No elegido por comodidad |
| 3 | La media geométrica difiere de la aritmética | Y se explica por qué |
| 4 | La serie real se distingue de la nominal | Deflactada |
| 5 | El salto del mes 14 se identifica y se trata | Con criterio declarado |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Promediar crecimientos con la media aritmética | Sobrestima siempre; la geométrica es la correcta |
| Comparar nominal con real | Son unidades distintas con el mismo nombre |
| Elegir el año base por comodidad | Cambia la conclusión sin que se note |
| Tratar una adquisición como crecimiento | Infla la cifra y no es sostenible |

## Entregables

- `solution.md` con las tres variaciones y su interpretación.
- La serie indexada con su base justificada.
- La serie deflactada junto a la nominal.
- La respuesta a la dirección en menos de 150 palabras.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Tres variaciones correctas | 25 |
| Índice con base justificada | 20 |
| Media geométrica | 20 |
| Deflactado | 20 |
| Respuesta con criterio | 15 |
