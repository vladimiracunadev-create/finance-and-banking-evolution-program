# Laboratorio 5: Liquidez del mercado secundario

## Propósito

Contrastar la liquidez **prometida** en un folleto con la que se mide, y calcular el importe mínimo de equilibrio de una oferta fraccionada.

## Escenario

Una plataforma promete «liquidez diaria» para participaciones inmobiliarias tokenizadas, con seis meses de datos disponibles.

## Contexto

La clase 6 sostiene que transferibilidad, negociabilidad y liquidez son tres cosas distintas. La clase 7 añade que el acceso sin salida no es acceso, y que el coste unitario de servicio decide el mínimo.

## Datos

Serie sintética de 412 operaciones en 182 días, con 96 contrapartes y 148 operaciones con parte vinculada.

## Supuestos del ejercicio

- Coste unitario de servicio de 18 al año por inversionista.
- Alternativa sin riesgo al 4,1 % anual.
- El impacto crece un 1 % por cada 25 % del volumen mensual vendido de golpe.

## Requisitos

- Laboratorio 4 completado.
- Haber leído las clases 6 y 7, y la Parte 20, clase 13.

## Pasos

1. Calcula el porcentaje de días con al menos una operación.
2. Separa el volumen de partes vinculadas y recalcula la rotación.
3. Estima el tiempo de salida de una posición de 400 000.
4. Calcula el impacto de una salida rápida frente a una escalonada.
5. Halla la rentabilidad neta por tamaño de inversión con el coste unitario.
6. Calcula el importe mínimo de equilibrio frente a la alternativa sin riesgo.
7. Evalúa el compromiso de liquidez del folleto con sus cinco elementos.
8. Redacta la página de divulgación adaptada, de una sola cara.

## Arquitectura

```text
TRANSFERIBILIDAD  la da el registro
NEGOCIABILIDAD    la da una plataforma
LIQUIDEZ          la dan PARTICIPANTES dispuestos a comprar

rentabilidad neta = bruta − comisiones − coste_unitario/inversion
minimo de equilibrio: donde la neta supera la alternativa
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los días con operación se miden | 74 de 182 |
| 2 | El volumen vinculado se separa | 53,8 % del total |
| 3 | El tiempo de salida se calcula | Sobre el volumen genuino |
| 4 | La rentabilidad neta varía con el tamaño | Tres tamaños |
| 5 | El mínimo de equilibrio se halla | Frente a la alternativa |
| 6 | El compromiso se evalúa | Cinco elementos |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Confundir transferibilidad con liquidez | El folleto usa una por otra | Medir días con ejecución |
| Volumen sostenido por el promotor | Se retira y desaparece | Publicar operaciones vinculadas |
| Mínimo elegido por marketing | El pequeño rinde menos que sin riesgo | Calcular el equilibrio |
| Acceso sin salida | Se entra y no se sale | Declarar la liquidez medida |
| Compromiso sin obligación | «Procurará dar contrapartida» | Exigir parámetros y causas de retirada |

## Pruebas

```bash
python -m pytest tests/test_digital_assets_risk_lab.py -q -k profundidad
```

```bash
python apps/digital_assets_risk_lab/cli.py market --position 400000
```

## Entregables

- La medición de liquidez con los siete indicadores.
- La rentabilidad neta por tamaño y el mínimo de equilibrio.
- El compromiso de cotización con sus cinco elementos.
- `solution.md` con la página de divulgación adaptada.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Medición de liquidez real | 25 |
| Separación del volumen vinculado | 20 |
| Rentabilidad neta por tamaño | 20 |
| Mínimo de equilibrio calculado | 20 |
| Divulgación adaptada | 15 |

## Solución de referencia

En [`solutions/lab-05.md`](../solutions/lab-05.md).
