# Laboratorio 4: Salvaguarda y segregación

## Propósito

Verificar una salvaguarda con las cuatro preguntas y **cuantificar lo que separa al cliente de recuperar el 18 % o el 99,5 %**.

Los tres laboratorios anteriores miraron a la entidad; este mira al cliente. Es el punto donde el cumplimiento formal y la protección real se separan más, porque una entidad puede tener cuenta segregada, contrato específico y una declaración correcta en su web, y aun así dejar al cliente como acreedor ordinario en un concurso.

## Escenario

Una entidad con 42 000 clientes y 68 000 000 en saldos, más un custodio con 280 000 000 y cuenta ómnibus. Hay que determinar qué recupera el cliente en cada escenario de fallo.

## Contexto

La clase 6 distingue protección de conducta de protección patrimonial y señala que solo se audita la primera. La clase 9 añade la pregunta previa: si el instrumento no está calificado como valor, el régimen protector de custodia no aplica.

## Datos

Una salvaguarda documentada y un custodio sintético con su contrato y su esquema de claves.

## Supuestos del ejercicio

- Recuperación como acreedor ordinario del 18 %.
- Diferencia de conciliación de 900 000.
- Coste de la cuenta segregada de 0,4 por posición y mes.

## Requisitos

- Laboratorio 3 completado.
- Haber leído las clases 6 y 9.

## Pasos

1. Aplica las cuatro preguntas de la salvaguarda y anota cuáles fallan.
2. Cuantifica la exposición por compensación y por conciliación.
3. Comprueba que con las cuatro resueltas la exposición es cero.
4. Determina si el régimen protector de custodia aplica al instrumento.
5. Aplica las seis preguntas del supervisor sobre la custodia.
6. Calcula el coste de pasar a cuenta segregada como porcentaje del custodiado.
7. Construye la tabla de recuperación por escenario de fallo.
8. Prioriza las correcciones por su efecto y su coste.

## Arquitectura

```text
Salvaguarda
  1 a nombre de clientes
  2 contrato especifico
  3 RENUNCIA A COMPENSAR   ← la que falla
  4 conciliacion diaria

  exposicion()
    por_compensacion  = deuda si no hay renuncia
    por_conciliacion  = diferencia si no es diaria
    recuperable       = saldo − ambas
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Las cuatro preguntas se aplican | Con evidencia por cada una |
| 2 | La renuncia a compensar es la que falla | Identificada como tal |
| 3 | La exposición se cuantifica | Por compensación y por conciliación |
| 4 | Con las cuatro resueltas la exposición es cero | Comprobación |
| 5 | El régimen protector se verifica primero | Antes de las tres segregaciones |
| 6 | La segregada es asequible | Porcentaje del custodiado |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Auditar solo la conducta | Es lo visible en inspección | Preguntar qué recupera el cliente |
| Confiar en «cuenta segregada» | Suena suficiente | Falta la renuncia a compensar |
| Conciliar semanalmente | Es lo cómodo | La diferencia la pagan los clientes |
| Suponer el régimen de valores | Se asume por parecido | Depende de la calificación |
| Ómnibus por coste | Se cree caro segregar | 0,0032 % del custodiado |

## Pruebas

```bash
python -m pytest tests/test_regulatory_perimeter_engine.py -q -k "salvaguarda or preguntas"
```

```bash
python apps/regulatory_perimeter_engine/cli.py compliance
```

## Entregables

- Las cuatro preguntas respondidas con evidencia.
- La cuantificación de cada hallazgo.
- La tabla de recuperación por escenario.
- `solution.md` con las correcciones priorizadas por efecto y coste.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Cuatro preguntas con evidencia | 25 |
| Cuantificación de la exposición | 25 |
| Régimen protector verificado | 20 |
| Tabla de recuperación | 15 |
| Correcciones priorizadas | 15 |

## Solución de referencia

En [`solutions/lab-04.md`](../solutions/lab-04.md).
