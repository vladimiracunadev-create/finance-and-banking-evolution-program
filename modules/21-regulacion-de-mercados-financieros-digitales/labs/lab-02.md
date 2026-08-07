# Laboratorio 2: Calificación de instrumentos

## Propósito

Calificar tres instrumentos con los cuatro criterios y comprobar que **el material de promoción forma parte de la calificación**.

Determinado el perímetro en el laboratorio anterior, toca la segunda pregunta: con qué instrumentos se opera. Aquí aparece el hallazgo que más sorprende a quien viene del lado técnico: la misma unidad, con el mismo código, puede ser un token de utilidad o un valor según cómo se venda, y la diferencia cuesta 340 000 al año.

## Escenario

Un proyecto emite un token para una plataforma de logística que se lanzará en 18 meses. Hay que calificarlo, evaluar las tres defensas del emisor y cuantificar el riesgo de una recalificación.

## Contexto

La clase 3 enuncia los cuatro criterios y señala que el cuarto —el esfuerzo de un tercero— es el decisivo. También muestra que el hecho más elocuente del caso no era jurídico: el 92 % de los compradores no usaba el servicio.

## Datos

Tres instrumentos sintéticos con sus características y su material de promoción literal.

## Supuestos del ejercicio

- El material de promoción recogido es el vigente y está fechado.
- La proporción de compradores que usan el servicio procede de la propia plataforma.
- El coste de cumplimiento por calificación es el declarado en el módulo.

## Requisitos

- Laboratorio 1 completado.
- Haber leído la clase 3.

## Pasos

1. Aplica los cuatro criterios al token de logística y cuenta cuántos se cumplen.
2. Extrae del material de promoción las frases que crean expectativa de beneficio.
3. Comprueba que retirar esa frase cambia el resultado del tercer criterio.
4. Determina si la utilidad es genuina o aparente, y explica qué la distingue.
5. Califica un saldo prepago con emisor autorizado y comprueba que da un resultado distinto.
6. Calcula el ahorro de calificar como utilidad y compáralo con el riesgo de la recalificación.
7. Evalúa las tres defensas del emisor y explica por qué ninguna se sostiene.
8. Redacta el documento de calificación con sus siete elementos.

## Arquitectura

```text
Instrumento
  criterios()  →  CuatroCriterios
     1 inversion de dinero
     2 proyecto comun
     3 expectativa de beneficio  ← la promocion
     4 esfuerzo de un tercero    ← el decisivo

  frases_que_crean_expectativa()
     analiza el material, no pregunta al emisor
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los cuatro criterios se cumplen | Calificación como valor |
| 2 | La promoción cambia el criterio 3 | Con y sin la frase |
| 3 | La utilidad aparente se detecta | Servicio que no funciona hoy |
| 4 | Una utilidad genuina se califica bien | Servicio en funcionamiento |
| 5 | El ahorro es el 1,1 % del riesgo | Cálculo comparado |
| 6 | El documento tiene siete elementos | Revisión de la estructura |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Calificar por el nombre | Lo elige el emisor | Aplicar los cuatro criterios |
| Ignorar la promoción | Parece marketing | Es prueba y califica |
| «No prometemos rentabilidad» | Se cree que basta | Basta con crear la expectativa |
| Servicio futuro como utilidad | Se planea lanzarlo | Tiene que funcionar hoy |
| Calificar una vez | Es un trámite inicial | Se revisa al cambiar los hechos |

## Pruebas

```bash
python -m pytest tests/test_regulatory_perimeter_engine.py -q -k "criterios or promocion or utilidad or dinero_electronico or ahorro"
```

```bash
python apps/regulatory_perimeter_engine/cli.py qualification
```

## Entregables

- Los cuatro criterios aplicados a tres instrumentos.
- Las frases de la promoción que califican, con su fuente.
- El ahorro frente al riesgo de la recalificación.
- `solution.md` con el documento de calificación completo.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Cuatro criterios aplicados | 25 |
| Análisis del material de promoción | 25 |
| Utilidad genuina frente a aparente | 20 |
| Cuantificación del riesgo | 15 |
| Documento de calificación | 15 |

## Solución de referencia

En [`solutions/lab-02.md`](../solutions/lab-02.md).
