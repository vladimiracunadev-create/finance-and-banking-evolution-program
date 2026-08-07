# Laboratorio 8: Grafo de contagio

## Propósito

Demostrar que una entidad con **exposición directa cero** puede tener una
necesidad de liquidez de 117 000 000, y encontrar el nodo crítico que no aparece
en ningún balance.

## Escenario

Un banco no tiene ni una unidad del instrumento S. Presta a tres entidades que sí
lo tienen y recibe depósitos de un custodio que lo guarda por cuenta de sus
clientes. Hay que calcular su exposición económica real.

## Contexto

La clase 14 sostiene que la exposición directa es la que se mide y la indirecta
la que hace daño, y que el canal menos visible es la dependencia común.

## Datos

Cinco entidades sintéticas con capital, posición y proveedores declarados.

## Supuestos del ejercicio

- Caída del instrumento del 60 %.
- Disposición del 40 % de las líneas comprometidas.
- Retirada del 35 % de los depósitos del custodio.
- Traslado lineal de la pérdida al capital: sirve para ordenar, no para predecir.

## Requisitos

- Laboratorio 7 completado.
- Haber leído las clases 12, 13 y 14.

## Pasos

1. Construye el grafo con las cinco entidades y sus cuatro vínculos.
2. Comprueba que la exposición directa del banco es cero.
3. Calcula la exposición indirecta por contraparte y súmala.
4. Comprueba que el custodio **no aporta** exposición indirecta y explica por
   qué.
5. Ejecuta `cascada` y anota líneas dispuestas, depósitos retirados y necesidad
   total.
6. Encuentra el nodo crítico con `nodo_critico` y di a cuántas entidades afecta.
7. Explica por qué un fallo de ese nodo produce el mismo efecto que una caída del
   60 % sin que el instrumento se mueva.
8. Propón cuatro límites nuevos con valor, método, frecuencia y disparador.

## Arquitectura

```text
        banco
       /  |  \  \
      F   D   P   C (custodio, depósitos recibidos)
       \  |  /
        proveedor de precios P1   ◄── nodo crítico

exposición directa    = 0
exposición económica  = 38 050 000
necesidad de liquidez = 117 000 000
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | La exposición directa es cero | Cálculo |
| 2 | La económica es 38 050 000 | Suma de segundo grado |
| 3 | El custodio no aporta indirecta | No aparece en el diccionario |
| 4 | La necesidad de liquidez es 117 000 000 | Cascada |
| 5 | El nodo crítico es el proveedor de precios | Afecta a tres entidades |
| 6 | Vincular una entidad desconocida falla | Excepción esperada |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Reportar solo lo directo | El informe es cierto e inútil | Añadir segundo grado |
| Ignorar al custodio | Es tu depositante mayorista | Modelar el canal de liquidez |
| Olvidar el proveedor de precios | Su fallo equivale a una caída | Mapa de dependencias comunes |
| Tratar el lineal como predicción | Falsa precisión | Usarlo para ordenar |
| Escenarios de un nodo | El daño viene de la simultaneidad | Cascada conjunta |
| Supuestos en anexo | El lector no los ve | Primera página |

## Pruebas

```bash
python -m pytest tests/test_digital_assets_risk_lab.py -q -k "exposicion or custodio or nodo or vincular"
```

```bash
python apps/digital_assets_risk_lab/cli.py contagion
```

## Entregables

- El grafo con nodos, aristas y fuentes de datos.
- La exposición directa, indirecta y económica.
- El mapa de dependencias comunes con el nodo crítico.
- Los cuatro indicadores del comité y la página de supuestos.
- `solution.md` con los cuatro límites propuestos.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Construcción del grafo | 20 |
| Exposición de segundo grado | 20 |
| Canal de liquidez del custodio | 20 |
| Nodo crítico identificado | 25 |
| Límites con sus cuatro elementos | 15 |

## Solución de referencia

En [`solutions/lab-08.md`](../solutions/lab-08.md).
