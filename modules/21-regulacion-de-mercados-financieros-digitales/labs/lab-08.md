# Laboratorio 8: Comparación de regímenes

## Propósito

Construir una tabla comparada útil y demostrar que **el arbitraje regulatorio ahorra en la autorización y no en el coste permanente**.

Los siete laboratorios anteriores trabajaron dentro de una jurisdicción. Este añade la dimensión que aparece en cuanto una entidad tiene un cliente fuera: varios regímenes a la vez. El error que arruina la mayoría de las comparaciones no es de contenido sino de nivel, y el hallazgo es que la estructura que parecía ahorrar no ahorra nada.

## Escenario

Una entidad quiere ofrecer custodia y cambio a clientes de tres jurisdicciones con regímenes distintos, y estudia domiciliarse en la más laxa.

## Contexto

La clase 16 distingue requisito, guía y práctica, y señala que la comercialización activa activa el régimen del cliente con independencia de dónde esté la entidad. La clase 15 añade la escala de sistema.

## Datos

Tres jurisdicciones sintéticas con sus obligaciones y una base de clientes por país.

## Supuestos del ejercicio

- Los costes de autorización y mantenimiento por jurisdicción son los declarados.
- Ingreso medio por cliente y año de 62.
- Los indicios de comercialización activa se verifican sobre el plan comercial.

## Requisitos

- Laboratorio 7 completado.
- Haber leído las clases 15 y 16.

## Pasos

1. Construye la tabla comparada con nivel, referencia y fecha por celda.
2. Aplica los seis indicios de comercialización activa al plan comercial.
3. Calcula la carga regulatoria de cada jurisdicción y su porcentaje sobre el ingreso.
4. Evalúa renunciar a la jurisdicción más cara y a la más barata.
5. Evalúa la estructura de arbitraje y explica por qué no funciona.
6. Construye el tablero macroprudencial con sus cuatro bloques.
7. Calcula la exposición directa y la económica, y compáralas.
8. Evalúa la relevancia sistémica por los cinco criterios.

## Arquitectura

```text
TRES NIVELES QUE NO SE MEZCLAN
  REQUISITO  obliga
  GUIA       orienta
  PRACTICA   describe

CADA CELDA: nivel + referencia + FECHA

COMERCIALIZACION ACTIVA
  idioma · moneda · publicidad · horario
  · pagos locales · dominio
  varios juntos activan el regimen ajeno
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Cada celda lleva nivel y fecha | Revisión de la tabla |
| 2 | Los seis indicios se aplican | Sobre el plan comercial |
| 3 | La carga se compara con el ingreso | Por jurisdicción |
| 4 | Renunciar a una se evalúa | Con su base de clientes |
| 5 | El arbitraje se descarta | Con su razón |
| 6 | La exposición económica supera a la directa | Nueve veces |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Comparar resúmenes | Es lo accesible | Citar artículo, fecha y fuente |
| Mezclar norma y práctica | Ambas describen | Solo una obliga |
| Ignorar la comercialización activa | Se mira dónde está la entidad | Se mira hacia dónde se dirige |
| Descartar la jurisdicción cara | Solo se mira el coste | Comparar con su base |
| Tabla sin dueño | Se hizo para un proyecto | Caduca y engaña |

## Pruebas

```bash
python -m pytest tests/test_regulatory_perimeter_engine.py -q -k proveedores
```

```bash
python apps/regulatory_perimeter_engine/cli.py compliance
```

## Entregables

- La tabla comparada con nivel, referencia y fecha por celda.
- El análisis de comercialización activa.
- La carga regulatoria frente al ingreso de cada jurisdicción.
- `solution.md` con el tablero macroprudencial y la evaluación de relevancia.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Tabla con los tres niveles | 25 |
| Comercialización activa | 20 |
| Carga frente a ingreso | 20 |
| Crítica del arbitraje | 20 |
| Tablero y relevancia | 15 |

## Solución de referencia

En [`solutions/lab-08.md`](../solutions/lab-08.md).
