# Laboratorio 6: Conformidad y seguridad

## Propósito

Escribir la batería de pruebas que un tercero ejecutaría para decidir si tu
implementación puede conectarse. La conformidad se demuestra fallando bien.

## Escenario

Antes de habilitar a `Cuentas Claras SpA`, la institución proveedora exige pasar
una batería de conformidad. Tu tarea es escribir esa batería y ejecutarla contra
tu propia implementación de los laboratorios 2, 3 y 4.

## Contexto

Una prueba de conformidad no comprueba que el camino feliz funcione: eso lo
comprueba cualquiera. Comprueba que los caminos infelices **fallan del modo
documentado**, porque de eso depende que el otro extremo pueda programar contra
tu API sin adivinar.

## Datos

Las respuestas de tus propios servicios de los laboratorios anteriores.

## Supuestos del ejercicio

- La batería se ejecuta en local, sin red externa.
- No se prueban aspectos de red (TLS, certificados) porque el entorno los simula;
  se documenta explícitamente qué queda fuera.

## Requisitos

- Laboratorios 2, 3 y 4 completados.
- `pytest`.

## Pasos

1. Clasifica las pruebas en cuatro familias: autorización, contrato, seguridad y
   resiliencia.
2. Para cada familia escribe al menos cuatro casos negativos.
3. Verifica que cada error devuelto está en el catálogo del laboratorio 3.
4. Comprueba que ningún mensaje de error revela información que el llamante no
   debería tener (existencia de una cuenta, por ejemplo).
5. Ejecuta una prueba de límite de tasa y comprueba la cabecera de reintento.
6. Ejecuta una prueba de carga breve y registra los percentiles de latencia.
7. Escribe el informe de conformidad: qué pasó, qué falló, qué queda fuera de
   alcance y por qué.
8. Declara explícitamente las **limitaciones de la batería**. Una batería que se
   presenta como completa cuando no lo es es peor que una parcial declarada.

## Arquitectura

```text
batería
 ├── autorización   PKCE ausente · redirect_uri laxa · código reusado · alcance excedido
 ├── contrato       campo faltante · tipo erróneo · página fuera de rango · cursor inválido
 ├── seguridad      token ajeno · consentimiento revocado · enumeración · fuga en el error
 └── resiliencia    reintento idéntico · clave reusada · límite de tasa · respuesta lenta
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | ≥ 16 casos negativos | Recuento en el informe |
| 2 | Todos los errores del catálogo | Comparación automática |
| 3 | Sin fuga en mensajes | Revisión de respuestas 401/403/404 |
| 4 | Límite de tasa observable | Cabecera presente |
| 5 | Informe con limitaciones | Sección explícita |
| 6 | La batería es reproducible | Segunda ejecución idéntica |

## Amenazas a considerar

| Amenaza | Efecto | Control |
|---|---|---|
| Batería que solo prueba el camino feliz | Falsa confianza | Mínimo de casos negativos |
| Error distinto para «no existe» y «no autorizado» | Enumeración | Respuesta uniforme |
| Prueba dependiente del orden | Resultado no reproducible | Aislamiento por caso |
| Datos de prueba reales | Exposición | Solo datos sintéticos |
| Conformidad sin fecha | Se cita años después | Fecha e identificador de versión |

## Pruebas

```bash
python -m pytest tests/test_open_finance_sandbox.py -q
python apps/open_finance_sandbox/conformance_tests/run.py
```

## Entregables

- `conformance_tests/` con las cuatro familias.
- Informe de conformidad fechado.
- Sección de limitaciones.
- Percentiles de latencia medidos.
- `solution.md` con el análisis de los fallos encontrados.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Cobertura de casos negativos | 30 |
| Coherencia con el catálogo de errores | 20 |
| Ausencia de fugas de información | 20 |
| Informe con limitaciones declaradas | 20 |
| Reproducibilidad | 10 |

## Solución de referencia

En [`solutions/lab-06.md`](../solutions/lab-06.md).
