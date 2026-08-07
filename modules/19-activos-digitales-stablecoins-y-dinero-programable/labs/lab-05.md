# Laboratorio 5: Modelo algorítmico y su espiral

## Propósito

Demostrar ejecutando que **el ratio de absorción sube mientras el sistema se
hunde**, y que el indicador que sí funciona es la emisión por unidad retirada.

## Escenario

Un diseño de dos tokens con 2 000 000 000 de token estable respaldado únicamente
por un token variable de 1 200 000 000 de capitalización. Hay que encontrar la
salida máxima que soporta en un día.

## Contexto

La clase 7 sostiene que el respaldo endógeno es circular y que el rendimiento
alto es el acelerador: atrae depósitos, y con ellos crece el día de la salida.

## Datos

Sistema sintético con volumen diario del token variable de 60 000 000 y un
rendimiento declarado del 12 % con 42 000 000 de ingresos reales.

## Supuestos del ejercicio

- El 70 % del token variable recibido se vende de inmediato.
- El impacto de mercado es del 1 % por cada 20 000 000 vendidos.
- Los canjes ocurren en tramos de 200 000 000.

## Requisitos

- Laboratorio 4 completado.
- Haber leído la clase 7.

## Pasos

1. Construye el sistema y anota el ratio de absorción inicial.
2. Ejecuta cuatro vueltas de 200 000 000 y registra ratio, emisión por unidad y
   precio en cada una.
3. Demuestra que el ratio **sube** en las cuatro vueltas.
4. Demuestra que la emisión por unidad **crece** y que `espiral_acelera()` es
   verdadero.
5. Calcula con `veces_el_volumen` cuántas veces el volumen diario supone una
   vuelta, y decide si el impacto supuesto es optimista.
6. Descompón el rendimiento con `descomponer_rendimiento` y anota qué porcentaje
   es dilución.
7. Calcula la cobertura de un híbrido 70/30 en calma y en tensión.
8. Escribe la lista de nombres comerciales bajo los que has visto el mismo
   mecanismo y la prueba que los detecta a todos.

## Arquitectura

```text
E (estable)  ◄── canje ──►  V (variable)

  retirar E  →  emitir V  →  vender V  →  V cae
                                  │
                                  └──► hace falta emitir MÁS V

RATIO DE ABSORCIÓN      cap(V) / circulante(E)   → SUBE
EMISIÓN POR UNIDAD      unidades V / E retirado  → SE DISPARA
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | El ratio sube en las cuatro vueltas | Serie monótona creciente |
| 2 | El precio del token variable cae | Serie monótona decreciente |
| 3 | La emisión por unidad crece | `espiral_acelera()` |
| 4 | Una vuelta supera dos veces el volumen | `veces_el_volumen` |
| 5 | La dilución es del 82,5 % | Descomposición del rendimiento |
| 6 | El híbrido cubre el 70 % en tensión | Tramo endógeno a cero |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Vigilar el ratio de absorción | Tranquiliza mientras cae | Emisión por unidad retirada |
| Aceptar el rendimiento | Es dilución | Comparar con ingresos reales |
| Sumar el tramo endógeno | Cobertura ficticia | Contarlo a cero en tensión |
| Impacto constante | El colapso parece más lento | Crece con el tamaño |
| Creerlo un caso pasado | Cambia de nombre | Rastrear el respaldo |

## Pruebas

```bash
python -m pytest tests/test_digital_assets_risk_lab.py -q -k "ratio or espiral or emision or dilucion or hibrido"
```

```bash
python apps/digital_assets_risk_lab/cli.py spiral --rounds 5
```

## Entregables

- La tabla de cuatro vueltas con las tres métricas.
- La demostración de que el ratio sube y la emisión se dispara.
- El desglose del rendimiento entre ingresos y dilución.
- `solution.md` con la salida máxima soportable y su justificación.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Simulación con cuatro vueltas | 20 |
| Demostración del indicador engañoso | 25 |
| Indicador correcto identificado | 20 |
| Descomposición del rendimiento | 20 |
| Salida máxima justificada | 15 |

## Solución de referencia

En [`solutions/lab-05.md`](../solutions/lab-05.md).
