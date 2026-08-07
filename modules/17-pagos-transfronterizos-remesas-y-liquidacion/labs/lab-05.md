# Laboratorio 5: Comparador de remesas

## Propósito

Calcular el coste real de una remesa y hacerlo comparable. Al terminar sabrás por
qué la comisión anunciada explica menos de la mitad del precio.

## Escenario

Una asociación de migrantes pide un comparador honesto para su corredor. Los
operadores publican «comisión 4,90» y «sin comisiones», y nadie sabe cuál es más
barato. Tu tarea es construir la herramienta que responda.

## Contexto

La única cifra comparable es **cuánto recibe el beneficiario**, medida contra el
importe que recibiría al tipo de referencia. Todo lo demás es marketing.

## Datos

`datasets/synthetic/remittance_corridors.csv` — 9 corredores, 34 operadores, con
comisión, tipo aplicado, comisión de retiro y plazo. Diccionario en
`datasets/schemas/remittance_corridors.md`.

## Supuestos del ejercicio

- Los tipos de referencia son del mismo instante para todas las rutas.
- Las cifras son **sintéticas** y no describen a ningún operador real.
- No se modelan promociones ni descuentos por volumen.
- El plazo declarado es el del operador, no el observado.

## Requisitos

- Python 3.11 o superior.
- Haber leído las clases 1, 9 y 10.

## Pasos

1. Implementa el cálculo del **importe recibido** para una ruta: comisión, tipo
   aplicado, comisiones intermedias y comisión de retiro.
2. Implementa el **denominador honesto**: importe recibido al tipo de referencia,
   sin ningún coste.
3. Calcula el **coste total** como porcentaje sobre ese denominador.
4. Descompón el coste en: comisión explícita, comisiones intermedias,
   diferencial de cambio y comisión de retiro.
5. Calcula el diferencial en **puntos básicos** y, si hay tipo cruzado, el
   diferencial compuesto.
6. Genera la tabla de **precio efectivo por importe**: 50, 200, 500 y 2 000
   unidades.
7. Compara cada corredor con el objetivo internacional vigente y marca los que
   lo superan.
8. Añade una advertencia automática cuando la comisión explícita sea menos del
   50 % del coste total.

## Arquitectura

```text
importe enviado
      │
      ├── comisión de envío
      ├── tipo aplicado ──► conversión
      ├── comisiones intermedias
      └── comisión de retiro
                    │
                    ▼
            importe recibido
                    │
   coste = (recibido al tipo de referencia − recibido) / recibido al tipo
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | El denominador es el tipo de referencia | Revisión de la fórmula |
| 2 | El coste se descompone en cuatro componentes | Suma igual al total |
| 3 | El diferencial cruzado se compone, no se suma | Prueba con dos patas |
| 4 | La tabla cubre cuatro importes | Salida del comparador |
| 5 | Se marca cuando la comisión < 50 % del coste | Prueba con ruta «sin comisiones» |
| 6 | Se compara con el objetivo internacional | Marca por corredor |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Comparar solo comisiones | Se elige la ruta más cara | Comparar importe recibido |
| Usar el tipo del operador como referencia | Denominador sesgado | Tipo medio de mercado |
| Sumar diferenciales cruzados | Coste subestimado | Composición multiplicativa |
| Tipos de instantes distintos | Se compara ruido de mercado | Mismo instante para todas |
| Presentar datos sintéticos como reales | Desinformación | Declararlo en cada salida |

## Pruebas

```bash
python -m pytest tests/test_cross_border_payments_lab.py -q -k remittance
```

```bash
python apps/cross_border_payments_lab/cli.py compare --corridor CL-PH --amount 500000
```

## Entregables

- El comparador funcional con los cuatro importes.
- La descomposición del coste de cinco rutas.
- El diferencial en puntos básicos, incluido el cruzado.
- La comparación con el objetivo internacional.
- `solution.md` explicando qué ruta gana y por qué, y en qué tramo cambia.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Denominador y fórmula correctos | 25 |
| Descomposición en cuatro componentes | 25 |
| Diferencial cruzado compuesto | 20 |
| Tabla por importe y cambio de ganador | 20 |
| Declaración de límites y de datos sintéticos | 10 |

## Solución de referencia

En [`solutions/lab-05.md`](../solutions/lab-05.md).
