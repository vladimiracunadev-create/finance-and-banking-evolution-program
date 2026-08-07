# Laboratorio 8: Colateral con llamada de margen

## Propósito

Demostrar que **liquidar posiciones enteras convierte una caída en una cascada**, y que la corrección más eficaz no toca ningún parámetro de riesgo.

## Escenario

Una plataforma acepta bonos tokenizados como colateral de 340 préstamos, con umbrales de llamada al 135 % y de liquidación al 120 %.

## Contexto

La clase 14 sostiene que el recorte estaba bien calculado y era irrelevante: lo que rompía el sistema era vender entero contra un mercado cinco veces menos profundo que el volumen a liquidar.

## Datos

340 posiciones sintéticas con ratios distribuidos entre el 115 % y el 233 %.

## Supuestos del ejercicio

- Volatilidad diaria del colateral del 1,8 %.
- Profundidad al 1 % de 2 400 000.
- Reposición nula entre vueltas de la misma cascada.

## Requisitos

- Laboratorio 7 completado.
- Haber leído la clase 14.

## Pasos

1. Calcula el recorte con volatilidad, impacto y coste de operación.
2. Calcula el colchón implícito del ratio exigido y explica en qué se diferencia del recorte.
3. Mide la distribución de umbrales y cuántas posiciones cruzan con una caída del 12 %.
4. Ejecuta la cascada con liquidación de posiciones enteras.
5. Repite con liquidación parcial y compara el volumen de la primera vuelta.
6. Añade una pausa por caída y comprueba que detiene la cascada.
7. Halla el punto de amplificación probando distintas caídas iniciales.
8. Redacta la llamada de margen con sus cuatro parámetros y su vía de excepción.

## Arquitectura

```text
CASCADA
  precio cae → llamadas → liquidaciones
            → venta forzada → precio cae mas

liquidacion_parcial=False  vende la posicion entera
liquidacion_parcial=True   vende lo justo para volver
                           al ratio exigido

pausa_si_cae_mas_de  suspende y da tiempo a aportar
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | El recorte se calcula, no se copia | Tres componentes |
| 2 | Recorte y colchón se distinguen | Cubren momentos distintos |
| 3 | La cascada con posiciones enteras se sostiene | Varias vueltas |
| 4 | La liquidación parcial la apaga | Menos vueltas y menos volumen |
| 5 | La pausa detiene la cascada | Cero liquidaciones en la vuelta 1 |
| 6 | El punto de amplificación se halla | Probando caídas |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Recorte por analogía | Se copia de un activo líquido | Calcularlo con la profundidad real |
| Liquidar posiciones enteras | Es lo simple de programar | Vender solo lo necesario |
| Ignorar la distribución de umbrales | Es lo que decide la cascada | Medirla antes |
| Plazo de minutos | Nadie puede aportar | Liquidar es peor que dejar aportar |
| Sin pausa por caída | La cascada no encuentra freno | Pausa con reanudación ordenada |

## Pruebas

```bash
python -m pytest tests/test_tokenization_platform.py -q -k "recorte or cascada or parcial or pausa or forzado"
```

```bash
python apps/tokenization_platform/cli.py collateral --drop 0.12
```

## Entregables

- El recorte con sus tres componentes y el colchón implícito.
- La cascada con posiciones enteras y con liquidación parcial.
- El punto de amplificación antes y después de las correcciones.
- `solution.md` con la llamada de margen y su vía de excepción.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Recorte calculado y distinguido del colchón | 20 |
| Distribución de umbrales medida | 20 |
| Cascada simulada con ambos modos | 25 |
| Punto de amplificación hallado | 20 |
| Llamada de margen con vía de excepción | 15 |

## Solución de referencia

En [`solutions/lab-08.md`](../solutions/lab-08.md).
