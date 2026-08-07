# Laboratorio 3: Vía de autorización

## Propósito

Estimar el **plazo real y el coste permanente** de una autorización, y descubrir la cifra que decide si el negocio existe.

Con la actividad determinada y los instrumentos calificados, la tercera pregunta es qué permiso hace falta. Este laboratorio produce un número que casi nunca aparece en un plan de negocio inicial: cuánto hay que facturar solo para sostener la carga regulatoria, antes de ganar nada.

## Escenario

Una entidad de servicios sobre activos digitales prepara su expediente. Hay que estimar el plazo con los requerimientos incluidos, el coste de obtención y el recurrente, y someter un manual a la prueba del caso concreto.

## Contexto

La clase 4 distingue autorización, registro y supervisión, y señala que el plazo legal se suspende con cada requerimiento. La clase 7 añade las decisiones jurídicas de una CBDC y la 10, los límites de un régimen piloto.

## Datos

Parámetros sintéticos de una solicitud: capital exigido, socios en tres jurisdicciones y requerimientos esperados.

## Supuestos del ejercicio

- Tres requerimientos de 30 días cada uno.
- Cuatro meses de preparación del expediente.
- Margen del 22 % sobre ingresos.

## Requisitos

- Laboratorio 2 completado.
- Haber leído las clases 4, 7 y 10.

## Pasos

1. Construye la lista de requisitos con lo que demuestra cada uno.
2. Estima el plazo real sumando la suspensión por requerimientos.
3. Calcula el coste de obtener la autorización y el de mantenerla.
4. Halla la facturación necesaria para cubrir la carga regulatoria anual.
5. Somete un manual a la prueba del caso concreto y anota si responde.
6. Resuelve las cuatro decisiones jurídicas de una CBDC minorista.
7. Comprueba los límites de un régimen piloto frente a un crecimiento a tres años.
8. Diseña la estrategia de transición con sus seis elementos.

## Arquitectura

```text
AUTORIZACION  antes de operar, sin ella es ilicito
REGISTRO      declarativo, puede no controlar solvencia
SUPERVISION   todos los dias despues, y no termina

plazo real = plazo legal + suspension por
             requerimientos + preparacion

carga anual = cumplimiento + amortizacion
              + coste del capital inmovilizado
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | El plazo real supera al legal | Suma de suspensiones |
| 2 | El coste recurrente se calcula | Separado del inicial |
| 3 | La facturación necesaria se halla | Sobre el margen declarado |
| 4 | El manual responde el caso concreto | O se identifica como copiado |
| 5 | Las cuatro decisiones de CBDC se resuelven | Con su fundamento |
| 6 | La transición tiene seis elementos | Revisión de la estructura |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Planificar con el plazo legal | Es el que publica la norma | Los requerimientos lo suspenden |
| Dejar la propiedad para el final | Es lo más incómodo | Es lo primero que se mira |
| Manuales de plantilla | Es lo rápido | La primera pregunta los desmonta |
| No presupuestar el mantenimiento | Se ve como un proyecto | Es una nómina permanente |
| Sin entidad receptora | El cese se improvisa | Designarla antes de autorizar |

## Pruebas

```bash
python -m pytest tests/test_regulatory_perimeter_engine.py -q -k perimetro
```

```bash
python apps/regulatory_perimeter_engine/cli.py perimeter
```

## Entregables

- La lista de requisitos con su forma de acreditación.
- El plazo real y el coste de obtención y mantenimiento.
- La facturación necesaria para cubrir la carga regulatoria.
- `solution.md` con el manual sometido a la prueba y la estrategia de transición.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Requisitos con lo que demuestran | 15 |
| Plazo real estimado | 20 |
| Coste de obtención y mantenimiento | 20 |
| Facturación de equilibrio | 25 |
| Estrategia de transición | 20 |

## Solución de referencia

En [`solutions/lab-03.md`](../solutions/lab-03.md).
