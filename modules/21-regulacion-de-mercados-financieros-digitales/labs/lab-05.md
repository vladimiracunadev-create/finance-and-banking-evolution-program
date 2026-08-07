# Laboratorio 5: Programa de cumplimiento

## Propósito

Diseñar un programa proporcionado al riesgo y **gestionar el resto que ninguna medida elimina**: el tercio de destinos no identificables.

Este laboratorio trata la parte del cumplimiento que no tiene solución perfecta. La regla del viaje exige saber a quién se envían los datos, y el registro no lo dice; el resto no identificable no es un fallo del programa sino una consecuencia estructural, y lo que define la calidad del programa es cómo lo gestiona.

## Escenario

Un proveedor con 28 400 transferencias mensuales, de las que 9 100 van a destinos que no se pueden identificar. Hay que decidir si prohibirlas o tratarlas por tramos.

## Contexto

La clase 12 sostiene que prohibir parece más barato y solo desplaza la actividad a un proveedor sin controles. La clase 13 añade la contradicción entre supresión y conservación, y la 8, el capital que consume cada exposición.

## Datos

Un mes de transferencias sintéticas con su distribución por importe y sus alertas de sanciones.

## Supuestos del ejercicio

- Coste de una medida reforzada de 22.
- Recuperación ordinaria del 18 % en un concurso.
- Los umbrales por tramo derivan del análisis de riesgo escrito.

## Requisitos

- Laboratorio 4 completado.
- Haber leído las clases 8, 12 y 13.

## Pasos

1. Mide el resto no identificable y su importe.
2. Calcula la pérdida de ingreso de prohibir esas transferencias.
3. Diseña el tratamiento por tramos con su coste por tramo.
4. Compara ambas opciones y explica por qué la comparación simple engaña.
5. Añade el análisis de procedencia y recalcula las alertas.
6. Clasifica qué campos de un registro son datos personales.
7. Diseña el reparto entre registro y sistema externo, y la respuesta a una solicitud de supresión.
8. Clasifica tres exposiciones prudenciales y calcula el capital de cada una.

## Arquitectura

```text
REGLA DEL VIAJE
  1 determinar si el destino es sujeto obligado
  2 enviar los datos por el canal acordado
  3 si no lo es, medidas reforzadas

EL PASO 1 NO TIENE SOLUCION COMPLETA
  → el resto no identificable es estructural
  → y su tratamiento define el programa
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | El resto se mide, no se estima | Sobre las transferencias reales |
| 2 | La prohibición se cuantifica | Pérdida de ingreso |
| 3 | El tratamiento por tramos tiene coste | Por tramo |
| 4 | La comparación simple se critica | Con su razón |
| 5 | Los campos personales se clasifican | Con su fundamento |
| 6 | El capital por exposición se calcula | Tres exposiciones |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Enfoque de riesgo sin análisis | Se copian umbrales | El análisis justifica el umbral |
| Prohibir por simplicidad | Parece más barato | Desplaza la actividad |
| Cotejar solo el nombre | Es lo que hace el sistema | Las listas incluyen direcciones |
| Dato personal en el registro | Concepto libre con nombres | Validación en la entrada |
| Ignorar la custodia en el prudencial | No está en el balance | Consume capital operacional |

## Pruebas

```bash
python -m pytest tests/test_regulatory_perimeter_engine.py -q -k vigilancia
```

```bash
python apps/regulatory_perimeter_engine/cli.py compliance
```

## Entregables

- La medición del resto no identificable.
- El tratamiento por tramos con su coste.
- La clasificación de campos y el reparto de datos.
- `solution.md` con la crítica a la comparación simple.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Resto medido | 20 |
| Tratamiento por tramos | 25 |
| Crítica a la comparación simple | 20 |
| Clasificación de datos personales | 20 |
| Capital por exposición | 15 |

## Solución de referencia

En [`solutions/lab-05.md`](../solutions/lab-05.md).
