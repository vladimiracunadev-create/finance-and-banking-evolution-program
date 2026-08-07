# Laboratorio 2: Motor de rutas

## Propósito

Construir el componente que decide por dónde va cada pago, con criterios
explícitos y auditables. Un motor que elige sin explicar no se puede corregir
cuando se equivoca.

## Escenario

`Banco Andino` opera seis corredores. Hoy la elección de ruta la hace una tabla
que alguien escribió hace tres años. Nadie recuerda por qué el corredor a
Vietnam va por Singapur y no por Hong Kong. Tu tarea es sustituir la tabla por
un motor con criterios.

## Contexto

Los seis criterios de la clase 16 se aplican **en orden**: la elegibilidad y el
cumplimiento son filtros, no factores a ponderar. Una ruta que no admite el pago
no compite por precio.

## Datos

`apps/cross_border_payments_lab/data/corridors.json` y `routes.json`.

## Supuestos del ejercicio

- Seis corredores, con dos o tres rutas cada uno.
- Los costes y plazos son ilustrativos y están en los datos.
- La disponibilidad de cada ruta se simula con una serie histórica.
- No hay negociación de precio en tiempo real.

## Requisitos

- Laboratorio 1 completado.
- Python 3.11 o superior.

## Pasos

1. Modela una ruta con: corredor, límites, monedas, canales admitidos, coste
   fijo, coste variable, diferencial, plazo p50 y p95, y disponibilidad.
2. Implementa el filtro de **elegibilidad**: importe, moneda, canal del
   beneficiario y jurisdicción.
3. Implementa el filtro de **cumplimiento**: si la ruta no soporta un control
   exigido, queda fuera. No se pondera.
4. Implementa el filtro de **disponibilidad** con la serie histórica.
5. Implementa la comparación por **tiempo**, **coste** y **riesgo**, con pesos
   configurables y declarados.
6. Devuelve siempre: ruta elegida, ruta alternativa y **el motivo**.
7. Añade la regla de la clase 14: si existe enlace de pagos inmediatos, se
   prioriza.
8. Escribe pruebas que demuestren que cambiar un peso cambia la elección, y que
   un filtro no se puede compensar con precio.

## Arquitectura

```text
pago ──► ELEGIBILIDAD ──► CUMPLIMIENTO ──► DISPONIBILIDAD
                                                │
                                                ▼
                                    comparación ponderada
                                    tiempo · coste · riesgo
                                                │
                                                ▼
                            { ruta, alternativa, motivo }
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los filtros no se ponderan | Prueba: ruta barata no elegible se descarta |
| 2 | Siempre hay motivo | Ninguna respuesta sin campo `motivo` |
| 3 | Siempre hay alternativa, o se declara que no hay | Prueba por corredor |
| 4 | Cambiar un peso cambia la elección | Prueba paramétrica |
| 5 | El enlace de pagos inmediatos tiene prioridad | Prueba del corredor con enlace |
| 6 | La decisión es reproducible | Misma entrada, misma salida |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Ruta elegida por precio sin cumplir | Operación no autorizada | Filtro antes de la comparación |
| Motor sin motivo | No se puede auditar | Campo obligatorio |
| Pesos ocultos | Nadie sabe por qué elige | Configuración declarada y versionada |
| Ruta única sin alternativa | El corredor cae entero | Alternativa o declaración explícita |
| Datos de disponibilidad viejos | Se elige una ruta caída | Frescura del dato con alerta |

## Pruebas

```bash
python -m pytest tests/test_cross_border_payments_lab.py -q -k routing
```

```bash
python apps/cross_border_payments_lab/cli.py route --corridor CL-VN --amount 20000
```

## Entregables

- `routing_engine/` con los seis criterios.
- Configuración de pesos, versionada y documentada.
- Pruebas de que un filtro no se compensa con precio.
- `solution.md` explicando por qué el orden de los criterios importa.
- Tabla de supuestos.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Filtros aplicados antes de ponderar | 30 |
| Motivo y alternativa siempre presentes | 25 |
| Pruebas paramétricas de los pesos | 20 |
| Prioridad del enlace de pagos inmediatos | 15 |
| Documentación de la configuración | 10 |

## Solución de referencia

En [`solutions/lab-02.md`](../solutions/lab-02.md).
