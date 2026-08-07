# Laboratorio 8: Escenario de tensión

## Propósito

Diseñar el escenario que **rompe el propio sistema** y medir a cuántas desviaciones está de un día normal.

El laboratorio 7 buscó lo deliberado. Este busca lo que ocurre sin que nadie lo provoque, y encuentra que la fuente del episodio no son tres fallos independientes sino un proveedor que hace tres papeles.

## Escenario

Un banco corresponsal que emite el depósito, liquida los pagos y custodia efectivo anuncia problemas de liquidez. Hay que seguir los efectos hasta el punto de rotura.

## Contexto

La clase 15 sostiene que un escenario que el sistema aguanta no enseña nada, y que la correlación —no el número de fallos— es lo que hace el episodio.

## Datos

El mapa de proveedores del sistema con sus papeles.

## Supuestos del ejercicio

- Volatilidad diaria del colateral del 1,8 %.
- El 18 % de los clientes solicita retirar en el día 2.
- Liquidez disponible de 22 000 000.

## Requisitos

- Laboratorio 7 completado.
- Haber leído la clase 15.

## Pasos

1. Identifica el proveedor que desempeña varios papeles.
2. Comprueba que un solo fallo alcanza a todos ellos.
3. Añade los fallos correlacionados de los días siguientes.
4. Comprueba que el escenario afecta a más de un componente.
5. Mide el punto de rotura por función.
6. Contrasta todas las tolerancias declaradas.
7. Calcula a cuántas desviaciones está la caída de un día normal.
8. Propón correcciones y declara el nivel de prueba alcanzado.

## Arquitectura

```text
Proveedor.es_fuente_de_correlacion
  cierto si desempena mas de un papel

Escenario.desencadenar(horas, causa)
  un solo fallo alcanza a TODOS sus papeles

demuestra_algo
  falso si afecta a un solo componente
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | El proveedor con varios papeles se detecta | `es_fuente_de_correlacion` |
| 2 | Un fallo alcanza a los tres | Tres componentes |
| 3 | El escenario demuestra algo | Más de un componente |
| 4 | La peor interrupción se conserva | Por componente |
| 5 | Las desviaciones se calculan | Frente a la volatilidad |
| 6 | El nivel de prueba se declara | Del gradiente de cinco |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Escenario que el sistema aguanta | Tranquiliza | Diseña el que rompe |
| Fallos independientes | Es más fácil de modelar | La correlación hace el episodio |
| Un proveedor con varios papeles | Simplifica la operación | Es la fuente |
| Reportar sin nivel | Es lo habitual | Sin nivel no informa |
| Alternativa sin acuerdo | Se identificó un candidato | Sin firma no existe |

## Pruebas

```bash
python -m pytest tests/test_digital_bank_capstone.py -q -k "fuente or escenario or desviaciones or nivel"
```

```bash
python apps/digital_bank_capstone/cli.py stress
```

## Entregables

- La fuente de correlación identificada.
- El escenario con su punto de rotura por función.
- El contraste de todas las tolerancias.
- `solution.md` con las correcciones y el nivel declarado.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Fuente identificada | 20 |
| Escenario construido | 25 |
| Punto de rotura medido | 20 |
| Tolerancias contrastadas | 20 |
| Nivel declarado | 15 |

## Solución de referencia

En [`solutions/lab-08.md`](../solutions/lab-08.md).
