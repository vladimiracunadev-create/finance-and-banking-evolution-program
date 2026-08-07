# Laboratorio 7: Liquidez y profundidad de mercado

## Propósito

Comprobar que **el cociente sobre volumen y el cociente sobre profundidad dan
conclusiones opuestas**, y derivar un límite de posición que cuelgue del dato
correcto.

## Escenario

Una tesorería tiene 12 000 000 de unidades de un activo cuyo volumen diario
publicado es 184 000 000. Hay que saber en cuánto tiempo puede salir y a qué
coste.

## Contexto

La clase 13 sostiene que la liquidez tiene cuatro dimensiones y solo se publica
una: el volumen, que además puede inflarse sin coste real.

## Datos

Libro de órdenes agregado sintético con siete niveles, expresados en importe
acumulado.

## Supuestos del ejercicio

- El libro se repone un 70 % cada 30 minutos.
- El impacto por sesión de 1 500 000 unidades es del 0,70 %.
- La volatilidad diaria es del 5,2 %.
- Lo que excede el último nivel se ejecuta a 84,00.

## Requisitos

- Laboratorio 6 completado.
- Haber leído la clase 13 y la Parte 8.

## Pasos

1. Construye el libro y calcula la profundidad al 1 %, 2 % y 5 %.
2. Calcula los dos cocientes con `cocientes` y explica por qué discrepan.
3. Ejecuta la venta de golpe **sin declarar precio de cola** y comprueba que la
   función se niega a inventarlo.
4. Repite declarando el precio de cola y anota impacto y pérdida.
5. Calcula la venta escalonada y compara la pérdida.
6. Calcula el riesgo de esperar durante la ventana de ejecución y decide si
   escalonar sigue compensando.
7. Deriva el límite de posición con `limite_de_posicion` y compáralo con la
   posición actual.
8. Construye un libro con acumulado decreciente y comprueba que se rechaza.

## Arquitectura

```text
VOLUMEN       cuánto se negoció        → se publica
AMPLITUD      coste de entrar y salir  → visible
PROFUNDIDAD   cuánto absorbe al 1 %    → hay que medirla
RESILIENCIA   en cuánto vuelve         → solo tras una orden

posición / volumen      = 6,52 %   parece cómodo
posición / profundidad  = 5,77x    y no lo es
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Profundidad al 1 % igual a 2 080 000 | Cálculo sobre el libro |
| 2 | Los dos cocientes discrepan | Comparación |
| 3 | Sin precio de cola la venta falla | Excepción esperada |
| 4 | El impacto de golpe es del 6,95 % | Cálculo |
| 5 | Escalonar reduce el impacto al 2,17 % | Cálculo |
| 6 | El límite propuesto es 6 240 000 | Tres veces la profundidad |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Usar el volumen | Límite mal calibrado | Colgarlo de la profundidad |
| Suponer salida instantánea | Se ignora el riesgo del tiempo | Medir el riesgo de esperar |
| Sumar profundidad de plataformas | No es accesible a la vez | Medir la accesible |
| Precio de cola inventado | Resultado sin base | Declararlo como supuesto |
| Medir solo en calma | Sobreestima la capacidad | Medir también en tensión |

## Pruebas

```bash
python -m pytest tests/test_digital_assets_risk_lab.py -q -k "cocientes or profundidad or venta or escalonar or limite or libro"
```

```bash
python apps/digital_assets_risk_lab/cli.py market --position 12000000
```

## Entregables

- Las tres profundidades medidas.
- Los dos cocientes con su interpretación.
- El impacto de golpe y escalonado, con el riesgo del tiempo.
- El límite de posición derivado y su frecuencia de recálculo.
- `solution.md` con las señales de volumen inflado que revisarías.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Medición de profundidad | 20 |
| Contraste de los dos cocientes | 25 |
| Venta de golpe y escalonada | 20 |
| Riesgo del tiempo de exposición | 20 |
| Límite de posición justificado | 15 |

## Solución de referencia

En [`solutions/lab-07.md`](../solutions/lab-07.md).
