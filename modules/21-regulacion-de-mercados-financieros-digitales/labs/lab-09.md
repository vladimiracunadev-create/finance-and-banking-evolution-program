# Laboratorio 9: Expediente regulatorio

## Propósito

Ensamblar las doce piezas y descubrir que **las contradicciones solo aparecen al leerlas por parejas**.

Este laboratorio cierra la parte y reproduce lo que hace un supervisor en su primera lectura. Las doce piezas llegan de equipos distintos, cada una internamente coherente, y el ejercicio consiste en cruzarlas: los hallazgos que importan no están dentro de ninguna, están entre dos.

## Escenario

Una entidad de custodia y cambio con 42 000 clientes entrega su expediente completo. Hay que cruzarlo, priorizar los hallazgos y construir el plan de remediación.

## Contexto

La clase 18 enumera las doce piezas y las cinco parejas críticas, y sostiene que el elemento que falta casi siempre en un plan de remediación es la medida provisional: entre que se detecta y se corrige, el cliente está expuesto.

## Datos

Doce piezas sintéticas, cada una con sus afirmaciones y su evidencia.

## Supuestos del ejercicio

- Las afirmaciones de cada pieza son las que entregó su equipo.
- El material comercial revisado es el vigente.
- Los clientes afectados se estiman sobre la base declarada.

## Requisitos

- Laboratorios 1 a 8 completados.
- Haber leído las clases 17 y 18.

## Pasos

1. Registra las doce piezas y comprueba que una afirmación sin evidencia se rechaza.
2. Verifica que un expediente incompleto no permite operar.
3. Cruza perímetro con resiliencia y anota la contradicción.
4. Cruza calificación con conducta, salvaguarda con prevención, y datos con vigilancia.
5. Cruza régimen por jurisdicción con conducta.
6. Prioriza los hallazgos por nivel y clientes afectados.
7. Comprueba que si todo es ordinario, la revisión no miró donde debía.
8. Construye la remediación con su medida provisional y verifica que sin ella se rechaza.
9. Evalúa cuatro solicitudes de espacio de prueba por su hipótesis.

## Arquitectura

```text
Expediente
  afirmar(pieza, texto, EVIDENCIA)
     → sin evidencia se rechaza

PAREJAS_CRITICAS
  perimetro x resiliencia
  calificacion x conducta
  salvaguarda x prevencion
  datos x vigilancia
  jurisdiccion x conducta

puede_operar()  falso con un bloqueante
                sin remediar
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Una afirmación sin evidencia se rechaza | Excepción esperada |
| 2 | El expediente incompleto no permite operar | Con su motivo |
| 3 | Las cinco parejas revelan contradicciones | Una por pareja |
| 4 | Los hallazgos se ordenan por efecto | Nivel y clientes |
| 5 | Todo ordinario indica mala revisión | Comprobación |
| 6 | Sin medida provisional se rechaza | Excepción esperada |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Leer de principio a fin | Es lo natural | Leer por parejas |
| Cada equipo entrega su pieza | Es lo organizado | Alguien tiene que cruzarlas |
| Priorizar por gravedad formal | Es lo jurídico | Priorizar por efecto sobre el cliente |
| Plan sin provisional | Se asume corrección rápida | El intervalo también expone |
| Afirmar sin evidencia | Se sabe que es cierto | Sin evidencia se retira |

## Pruebas

```bash
python -m pytest tests/test_regulatory_perimeter_engine.py -q -k "expediente or afirmacion or bloqueante or hallazgos or remediacion or ordinario"
```

```bash
python apps/regulatory_perimeter_engine/cli.py dossier
```

## Entregables

- Las doce piezas con su evidencia.
- La lectura cruzada con las contradicciones halladas.
- Los hallazgos priorizados por efecto sobre el cliente.
- `solution.md` con el plan de remediación y sus medidas provisionales.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Doce piezas con evidencia | 15 |
| Lectura cruzada por parejas | 30 |
| Priorización por efecto | 20 |
| Plan con medidas provisionales | 25 |
| Evaluación de espacios de prueba | 10 |

## Solución de referencia

En [`solutions/lab-09.md`](../solutions/lab-09.md).
