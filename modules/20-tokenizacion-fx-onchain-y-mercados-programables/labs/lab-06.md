# Laboratorio 6: Creación de mercado automatizada

## Propósito

Comprobar que **el deslizamiento es el tamaño relativo a la reserva** y cuantificar la pérdida por divergencia de quien aporta.

## Escenario

Se evalúa aportar reservas a un mecanismo de producto constante para un par de activos tokenizados.

## Contexto

La clase 13 sostiene que aportar reservas es una apuesta a que habrá mucho volumen y poco movimiento, y que quien la hace no puede retirarse ni ajustar su cotización mientras dura.

## Datos

Piscina sintética de 500 000 y 1 000 000 unidades con comisión del 0,25 %.

## Supuestos del ejercicio

- Volumen mensual del par de 8 400 000 en el segundo activo.
- Aportación evaluada del 5 % de ambas reservas.
- Recorrido de precio equivalente a r = 1,45 en el peor tramo.

## Requisitos

- Laboratorio 5 completado.
- Haber leído la clase 13.

## Pasos

1. Cotiza tres tamaños de operación y verifica la regla del deslizamiento.
2. Comprueba que el precio efectivo es siempre peor que el marginal.
3. Opera contra la piscina y observa cómo se mueven las reservas.
4. Calcula la pérdida por divergencia para cinco movimientos de precio.
5. Comprueba que la pérdida es simétrica en ambos sentidos.
6. Halla el neto entre comisiones y divergencia para la aportación evaluada.
7. Calcula el movimiento de precio que anula un año de comisiones.
8. Compara con un libro de órdenes de la misma profundidad efectiva.

## Arquitectura

```text
PRODUCTO CONSTANTE   X × Y = K

  entregar Δx  →  recibir  Y − K/(X + Δx)
  precio marginal   Y / X
  precio efectivo   Δy / Δx   (siempre peor)

perdida por divergencia = 2·√r / (1 + r) − 1
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | El deslizamiento sigue la regla | Tres tamaños comparados |
| 2 | El efectivo es peor que el marginal | Comparación directa |
| 3 | La divergencia reproduce la clase | Cinco valores de r |
| 4 | La divergencia es simétrica | r y 1/r dan lo mismo |
| 5 | El neto se calcula | Comisiones menos divergencia |
| 6 | La razón crítica se halla | Por bisección |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Mirar solo la comisión | El rendimiento parece alto | Restar la divergencia |
| Llamarla «pérdida impermanente» | Suena reversible | Se materializa al retirar |
| Operar grande de golpe | Deslizamiento proporcional al tamaño | Trocear según la reserva |
| Usar el precio como índice | Lo forma una fórmula, no un mercado | No usarlo como referencia |
| Suponer que el precio vuelve | Es el supuesto cómodo | Si no vuelve, la pérdida es real |

## Pruebas

```bash
python -m pytest tests/test_onchain_fx_lab.py -q -k "deslizamiento or divergencia or aportante or razon"
```

```bash
python apps/onchain_fx_lab/cli.py amm --rounds 4
```

## Entregables

- La tabla de cotizaciones con deslizamiento y tamaño relativo.
- La pérdida por divergencia para cinco movimientos.
- El neto de la aportación con su alternativa de referencia.
- `solution.md` con el punto en que deja de compensar.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Regla del deslizamiento verificada | 20 |
| Pérdida por divergencia calculada | 25 |
| Neto de la aportación | 20 |
| Razón crítica hallada | 20 |
| Comparación con libro de órdenes | 15 |

## Solución de referencia

En [`solutions/lab-06.md`](../solutions/lab-06.md).
