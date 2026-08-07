# Laboratorio 4: Anatomía de una pérdida de paridad

## Propósito

Separar **detonante** de **mecanismo** en un episodio completo, y construir el
indicador que anticipa la fase 3 antes de que ocurra.

## Escenario

Un banco depositario donde está el 55 % del efectivo de un emisor entra en
resolución un viernes. Hay que reconstruir el episodio, calcular la banda de no
arbitraje y decidir si el desvío observado es ruido o señal.

## Contexto

La clase 3 define la banda; la clase 6 encadena las cinco fases y sostiene que
un arbitraje rentable que nadie ejecuta es la información más valiosa del
mercado.

## Datos

Serie horaria sintética de precios y los costes de arbitraje del emisor.

## Supuestos del ejercicio

- Recuperación del 90 % del efectivo atrapado.
- Escalera de descuentos creciente por tamaño.
- El tamaño de arbitraje es 2 400 000 unidades.

## Requisitos

- Laboratorios 2 y 3 completados.
- Haber leído las clases 3 y 6.

## Pasos

1. Calcula la banda de no arbitraje con `banda_de_no_arbitraje` y anota su
   anchura en puntos básicos.
2. Evalúa el arbitraje a un precio de 0,9940 y anualiza la rentabilidad.
3. Repite con un tamaño de 40 000 y explica por qué el resultado cambia.
4. Construye la serie horaria y alimenta `VigilanciaDeDesvio`; encuentra la hora
   en que se dispara la alerta.
5. Comprueba que volver a la banda reinicia el contador y discute si eso es
   correcto.
6. Modela el episodio con `Episodio` y las cinco fases, en dos versiones: canal
   que funciona y canal que no.
7. Calcula el punto de no retorno de la cartera del laboratorio 2 y exprésalo en
   porcentaje de circulante.
8. Aplica `recuperacion_corrige_la_causa` a los cuatro motivos posibles y escribe
   qué preguntarías ante una recuperación del precio.

## Arquitectura

```text
FASE 1 detonante   ──►  FASE 2 desvío
                              │
                    FASE 3 PRUEBA DEL CANAL
                       ├── funciona → se cierra en horas
                       └── no funciona → FASE 4 carrera
                                           └── FASE 5 venta forzada

banda de no arbitraje = paridad ± coste por unidad
alerta = precio fuera de banda durante N horas
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | La banda es de unos 12,9 pb | Comparación con la clase 3 |
| 2 | El arbitraje anualizado supera el 80 % | Cálculo |
| 3 | Bajo el mínimo no se puede arbitrar | Tamaño de 40 000 |
| 4 | La alerta se dispara a las 6 horas | Serie horaria |
| 5 | Volver a la banda reinicia el contador | Observación de 1,0000 |
| 6 | Solo la reanudación corrige la causa | Cuatro motivos evaluados |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Banda de cero | Se confunde ruido con crisis | Calcular con costes reales |
| Comprar el desvío | Se entra en una crisis | Investigar la causa antes |
| Explicar por el detonante | El análisis no sirve para el siguiente | Estudiar el mecanismo |
| Dar por cerrado el episodio | El mecanismo sigue intacto | Preguntar qué cambió en el canal |
| Descuento constante | El punto de no retorno se aleja | Escalera creciente |

## Pruebas

```bash
python -m pytest tests/test_digital_assets_risk_lab.py -q -k "banda or arbitraje or desvio or fase or recuperacion"
```

## Entregables

- La banda con su anchura en puntos básicos.
- El cálculo del arbitraje con dos tamaños.
- La serie con la hora exacta de la alerta.
- Los dos episodios modelados y comparados.
- `solution.md` con las preguntas ante una recuperación de precio.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Banda calculada con costes reales | 20 |
| Arbitraje evaluado con dos tamaños | 20 |
| Indicador de desvío persistente | 25 |
| Los dos episodios modelados | 20 |
| Preguntas ante la recuperación | 15 |

## Solución de referencia

En [`solutions/lab-04.md`](../solutions/lab-04.md).
