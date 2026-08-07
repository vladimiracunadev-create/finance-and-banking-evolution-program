# Laboratorio 7: FX y ventana de exposición

## Propósito

Medir la ventana **de irrevocable a confirmado** y comprobar que cada mecanismo debe compararse con la misma base.

## Escenario

Una tesorería opera 40 000 000 diarios en un par entre husos separados por 11 horas, y compara el mayorista con un cambio en registro.

## Contexto

La clase 11 muestra que el registro compite en topología y no en precio. La clase 12 muestra que comparar un mecanismo con la pérdida que ya redujo otro invierte la conclusión.

## Datos

Dos pares sintéticos —uno principal y uno poco líquido— y una contraparte con probabilidad de incumplimiento del 0,003 % diaria.

## Supuestos del ejercicio

- Recuperación esperada del 45 %.
- El neteo reduce el importe expuesto al 18 % del bruto.
- Prefinanciación del 25 % en cada divisa.

## Requisitos

- Laboratorio 6 completado.
- Haber leído las clases 11 y 12.

## Pasos

1. Construye las rutas mayorista y de registro con los seis tramos.
2. Compara ambos pares y explica por qué el resultado se invierte.
3. Corrige el ahorro anunciado con la profundidad del libro.
4. Repite con un libro muy fino y comprueba que el ahorro desaparece.
5. Calcula la ventana de exposición un día normal y un viernes.
6. Halla la pérdida esperada anual sin ningún mecanismo.
7. Compara neteo, PvP bruto y PvP neteado **contra esa misma base**.
8. Repite suponiendo que el acuerdo de neteo no es oponible y halla el límite bilateral que deja la pérdida dentro del apetito.

## Arquitectura

```text
RUTA = suma de tramos en puntos basicos
  mayorista  diferencial/2 + comision + corresponsalia
  registro   margen + diferencial/2 + entrada + salida

VENTANA  de irrevocable a CONFIRMADO
  y el peor caso es el viernes, no el dia medio

CADA MECANISMO se compara con la perdida
SIN ningun mecanismo, no con la que redujo otro
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | El registro pierde en el par principal | 5,4 veces más caro |
| 2 | Gana en el par poco líquido | 33 pb de ahorro |
| 3 | La profundidad corrige el ahorro | De 33 a 9 pb |
| 4 | La ventana va de irrevocable a confirmado | 19 y 67 horas |
| 5 | Los mecanismos se comparan con la misma base | Tabla completa |
| 6 | Sin oponibilidad el neteo no reduce | Igual que sin mecanismo |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Comparar precios mostrados | Se ignoran cuatro tramos | Sumar los seis |
| Suponer profundidad | El ahorro anunciado no se ejecuta | Medirla y escalonar |
| Medir la ventana del envío | Subestima la exposición | De irrevocable a confirmado |
| Olvidar el fin de semana | El peor caso es recurrente | Calcular el viernes |
| Dar el neteo por válido | Está firmado y puede no ser oponible | Exigir opinión jurídica |

## Pruebas

```bash
python -m pytest tests/test_onchain_fx_lab.py -q -k "par or profundidad or ventana or neteo or limite"
```

```bash
python apps/onchain_fx_lab/cli.py pricing
```

```bash
python apps/onchain_fx_lab/cli.py settlement
```

## Entregables

- El coste total de ambos mundos para dos pares.
- El ahorro corregido por profundidad.
- La ventana normal y del peor caso.
- `solution.md` con la comparación de mecanismos y el límite bilateral.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Coste total con los seis tramos | 20 |
| Ahorro corregido por profundidad | 20 |
| Ventana bien medida | 20 |
| Mecanismos comparados con la misma base | 25 |
| Límite bilateral calculado | 15 |

## Solución de referencia

En [`solutions/lab-07.md`](../solutions/lab-07.md).
