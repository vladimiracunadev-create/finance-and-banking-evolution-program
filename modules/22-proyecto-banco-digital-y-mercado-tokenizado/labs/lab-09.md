# Laboratorio 9: Expediente y defensa

## Propósito

Ensamblar el expediente, cruzarlo por parejas y **preparar las siete preguntas** que un comité hará.

Es el último laboratorio del programa. Reúne lo producido en los ocho anteriores y lo somete a la lectura que hace un supervisor, que no lee de principio a fin sino cruzando piezas.

## Escenario

El expediente completo del sistema se cruza por las cinco parejas críticas, y se prepara la defensa ante un comité con un supervisor invitado.

## Contexto

Las clases 13, 16, 17 y 18 construyen el expediente, el plan de resolución, la sección de límites y la defensa.

## Datos

Las doce piezas del expediente del sistema construido.

## Supuestos del ejercicio

- Cada pieza fue elaborada por un equipo distinto.
- El material comercial es el vigente.
- Los clientes afectados se estiman sobre la base declarada.

## Requisitos

- Laboratorios 1 a 8 completados.
- Haber leído las clases 13, 16, 17 y 18.

## Pasos

1. Ensambla las doce piezas con su evidencia.
2. Cruza las cinco parejas críticas y anota lo que aparece.
3. Prioriza los hallazgos por nivel y clientes afectados.
4. Construye la remediación con su medida provisional.
5. Diseña el plan de resolución con sus seis elementos.
6. Prueba el traspaso con un subconjunto y mide el plazo real.
7. Contrasta cada promesa comercial con su evidencia y retira lo que no se sostiene.
8. Prepara las respuestas a las siete preguntas del comité.

## Arquitectura

```text
LAS CINCO PAREJAS
  perimetro x resiliencia
  calificacion x conducta
  salvaguarda x prevencion
  datos x vigilancia
  jurisdiccion x conducta

Y LAS SIETE PREGUNTAS
  salen de las propias piezas:
  por eso son previsibles
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Las doce piezas llevan evidencia | O se retiran |
| 2 | Las cinco parejas se cruzan | Con lo que revela cada una |
| 3 | Los hallazgos se priorizan por efecto | Nivel y clientes |
| 4 | Cada remediación tiene provisional | Sin ella se rechaza |
| 5 | El traspaso se prueba con clientes reales | Plazo medido |
| 6 | Las promesas sin evidencia se retiran | Contraste completo |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Leer de principio a fin | Es lo natural | Léelo por parejas |
| Afirmación sin evidencia | El expediente pierde credibilidad | Se retira |
| Plan sin provisional | Se asume corrección rápida | El intervalo expone |
| Plan de resolución sin probar | Está escrito | Traspasa un subconjunto |
| Respuestas sin dato | Se conoce el sistema | Cita la evidencia |

## Pruebas

```bash
python -m pytest tests/test_digital_bank_capstone.py -q
```

```bash
python apps/digital_bank_capstone/cli.py scope
```

```bash
python apps/digital_bank_capstone/cli.py stress
```

## Entregables

- Las doce piezas con su evidencia.
- La lectura cruzada de las cinco parejas.
- El plan de resolución con su prueba de traspaso.
- `solution.md` con las siete respuestas y las promesas retiradas.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Doce piezas con evidencia | 15 |
| Lectura cruzada | 25 |
| Remediación con provisional | 15 |
| Plan de resolución probado | 20 |
| Siete respuestas preparadas | 25 |

## Solución de referencia

En [`solutions/lab-09.md`](../solutions/lab-09.md).
