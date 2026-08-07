# Laboratorio 6: Tensiones de diseño

## Propósito

Encontrar las contradicciones entre decisiones que eran correctas por separado, **cuantificarlas y declarar qué se sacrifica**.

Es el laboratorio central del capstone y el que justifica que la parte exista. Los cinco anteriores construyeron componentes; este los hace funcionar juntos durante un día y descubre lo que ninguno mostraba.

## Escenario

El sistema completo opera un día con 420 operaciones, seis llamadas de margen, un pago de intereses, una orden judicial y un corte de red de 40 minutos.

## Contexto

La clase 12 cierra la construcción con el ciclo diario y sostiene que la emisión se prueba y el ciclo de vida se improvisa.

## Datos

Una jornada sintética con sus incidencias.

## Supuestos del ejercicio

- Las tolerancias fueron fijadas por el consejo, por función.
- El corte de red afecta al banco emisor, no al registro propio.
- El aprovisionamiento del pago de intereses es insuficiente en 1 500.

## Requisitos

- Laboratorio 5 completado.
- Haber leído la clase 12.

## Pasos

1. Registra las decisiones de las clases 4 a 11 con su coste.
2. Comprueba que la tolerancia la fija el consejo y no el área técnica.
3. Ejecuta el pago de intereses con aprovisionamiento insuficiente.
4. Aplica la orden judicial con la función de inmovilización.
5. Simula el corte de red y mide las interrupciones por función.
6. Detecta qué tolerancias se incumplen.
7. Declara cada tensión y comprueba que sin resolver bloquea el sistema.
8. Resuelve cada una declarando el sacrificio y su cuantificación.

## Arquitectura

```text
Sistema
  decidir(Decision)
  fijar_tolerancia(funcion, horas, CONSEJO)
  declarar_tension(a, b, descripcion)

Tension.resolver(sacrificio, cuantificacion)
  sin sacrificio declarado se rechaza

puede_operar()  falso con tensiones abiertas
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | La tolerancia la fija el consejo | Excepción si la fija sistemas |
| 2 | Sin aprovisionamiento no se paga a nadie | Excepción esperada |
| 3 | La inmovilización exige doble aprobación | Registro inmutable |
| 4 | Las tolerancias incumplidas se detectan | Lista por función |
| 5 | Una tensión sin resolver bloquea | `puede_operar` falso |
| 6 | Resolver exige declarar el sacrificio | Excepción si falta |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Diseñar solo el día uno | Es lo que se prueba | El día doscientos rompe |
| Tolerancias fijadas por área | Cada una la suya | Un día completo las contrasta |
| Pagar sin verificar | El proceso «ya paga» | Verificar antes |
| Programar el embargo | Se automatiza todo | Solo la inmovilización |
| Resolver tensiones en silencio | Parece un detalle | Se declaran en el expediente |

## Pruebas

```bash
python -m pytest tests/test_digital_bank_capstone.py -q -k "tension or tolerancia or consejo"
```

```bash
python apps/digital_bank_capstone/cli.py tensions
```

## Entregables

- Las decisiones registradas con su coste.
- Las tensiones declaradas entre pares de decisiones.
- Las tolerancias incumplidas en la jornada.
- `solution.md` con cada tensión resuelta y cuantificada.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Decisiones registradas | 15 |
| Tensiones declaradas | 30 |
| Tolerancias contrastadas | 20 |
| Resolución con sacrificio | 25 |
| Cuantificación | 10 |

## Solución de referencia

En [`solutions/lab-06.md`](../solutions/lab-06.md).
