# Laboratorio 4: Custodia integrada

## Propósito

Medir la **independencia efectiva** del esquema de claves del sistema completo y verificar la custodia delegada del colateral.

El laboratorio 3 decidió qué registro manda. Este protege las claves que lo operan, y encuentra que el hallazgo mayor no está en la criptografía sino en una cláusula ausente del contrato de custodia.

## Escenario

El sistema propone un esquema 3-de-5 con tres guardianes en la oficina central y todos con el mismo dispositivo. Hay que medirlo, corregirlo y verificar el contrato del custodio.

## Contexto

Las clases 8 y 9 construyen las interfaces y la custodia. La segunda aplica al capstone el método de la Parte 20, clase 12.

## Datos

Un esquema de claves y un contrato de custodia sintéticos.

## Supuestos del ejercicio

- Colateral delegado de 24 000 000 sobre 180 clientes.
- Recuperación ordinaria del 18 % en un concurso.
- Probabilidad de indisponibilidad por guardián del 4 % anual.

## Requisitos

- Laboratorio 3 completado.
- Haber leído las clases 8 y 9.

## Pasos

1. Mide la independencia efectiva del esquema propuesto.
2. Redistribuye las partes sin cambiar el umbral y vuelve a medir.
3. Diseña la recuperación con umbral mayor, retardo y cancelación.
4. Verifica las tres cláusulas del contrato de custodia.
5. Cuantifica la exposición del cliente si falta la de no disposición.
6. Define el alcance por finalidad de cada consentimiento.
7. Prueba el orden de la revocación y mide la ventana.
8. Implementa la idempotencia con huella canónica.

## Arquitectura

```text
independencia efectiva = n − peor grupo + 1

y la condicion
  peor grupo < umbral

LAS TRES CLAUSULAS DEL CUSTODIO
  de quien es el activo
  prohibicion de disponer
  verificacion independiente
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | La independencia efectiva se mide | Cuatro factores |
| 2 | La redistribución no cambia el umbral | Sigue siendo 3-de-5 |
| 3 | La recuperación es más difícil que firmar | Umbral mayor |
| 4 | Las tres cláusulas se verifican | Con evidencia |
| 5 | La exposición se cuantifica | Si falta una cláusula |
| 6 | La revocación invalida antes de responder | Prueba de orden |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Umbral por intuición | «3 de 5 suena bien» | Medir la independencia |
| Mismo dispositivo | Compra centralizada | Diversificar |
| Delegar y creerse cubierto | El custodio está autorizado | Las tres cláusulas deciden |
| Sin verificación independiente | La hace quien custodia | Un tercero, mensual |
| Revocar y luego responder | Parece equivalente | Deja una ventana abierta |

## Pruebas

```bash
python -m pytest tests/test_digital_bank_capstone.py -q -k "tolerancia or consejo"
```

```bash
python apps/digital_bank_capstone/cli.py tensions
```

## Entregables

- La independencia efectiva antes y después.
- El diseño de recuperación con retardo y cancelación.
- La verificación de las tres cláusulas con su cuantificación.
- `solution.md` con el consentimiento y la prueba de revocación.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Independencia medida | 25 |
| Redistribución sin cambiar umbral | 20 |
| Recuperación diseñada | 20 |
| Cláusulas verificadas | 20 |
| Revocación probada | 15 |

## Solución de referencia

En [`solutions/lab-04.md`](../solutions/lab-04.md).
