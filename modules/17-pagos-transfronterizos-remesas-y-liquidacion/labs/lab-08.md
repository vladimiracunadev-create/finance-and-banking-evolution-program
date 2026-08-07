# Laboratorio 8: Ruta mediante stablecoin

## Propósito

Comparar una ruta con stablecoin contra la ruta clásica **sobre la misma base**, y
descomponer el ahorro por su fuente real. Es el laboratorio donde se aprende a no
atribuir a la tecnología lo que produce la topología.

## Escenario

La dirección de `Banco Andino` ha leído que una stablecoin «reduce el coste un
78 %» y pide un piloto. Tu tarea es medir si eso es cierto en sus corredores y
decir de dónde vendría el ahorro.

## Contexto

El error de análisis más común es comparar el tramo de transferencia con la ruta
clásica completa. La ruta con stablecoin tiene cinco tramos, y el barato es uno.

## Datos

`apps/cross_border_payments_lab/data/stablecoin_routes.json` — costes de entrada
y salida por corredor, comisiones de red, liquidez de salida y tiempos.

## Supuestos del ejercicio

- La stablecoin del ejercicio es **sintética**: no representa a ninguna real.
- No se modela el diseño del emisor ni sus reservas: eso es la Parte 20.
- Los tiempos de entrada y salida incluyen los controles de cumplimiento.
- La tenencia media es un parámetro configurable.

## Requisitos

- Laboratorios 1, 2 y 5 completados.
- Haber leído las clases 13 y 14.

## Pasos

1. Modela los **cinco tramos**: entrada, transferencia, tenencia, salida y
   última milla, cada uno con su coste y su tiempo.
2. Calcula el coste total de la ruta y compáralo con la ruta clásica **completa**,
   no con su tramo intermedio.
3. Imputa a la ruta clásica el **coste de prefinanciación** por operación.
4. Modela la **exposición durante la tenencia**: importe × tiempo, y qué pasa si
   la salida se bloquea y la tenencia pasa de minutos a días.
5. Ejecuta el análisis de sensibilidad al **número de intermediarios** de la ruta
   clásica: 1, 2 y 3.
6. Descompón el ahorro por **fuente**: intermediarios evitados, prefinanciación,
   ventana, diferencial, coste de red.
7. Calcula qué porcentaje del ahorro es atribuible al registro y no a la
   topología.
8. Escribe la **regla de enrutamiento** con sus condiciones y sus seis controles.

## Arquitectura

```text
RUTA CON STABLECOIN
  moneda local ──entrada──► stablecoin ──red──► stablecoin
                                                     │
                                            salida ──┴──► moneda destino
                                                              │
                                                       última milla

RUTA CLÁSICA
  banco ordenante ──► corresponsal ──► [intermediarios] ──► banco beneficiario
                                                              │
                                                       última milla
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los cinco tramos con coste asignado | Suma igual al total |
| 2 | Comparación de ruta completa contra ruta completa | Revisión del cálculo |
| 3 | Prefinanciación imputada a la ruta clásica | Coste por operación |
| 4 | Exposición modelada, incluido el bloqueo de salida | Escenario ejecutado |
| 5 | Sensibilidad a 1, 2 y 3 intermediarios | Tres resultados |
| 6 | Ahorro descompuesto por fuente | Suma igual al ahorro total |
| 7 | Regla de enrutamiento con condiciones | Documento con las seis reglas |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Comparar el tramo con la ruta entera | Conclusión falsa | Ruta completa contra ruta completa |
| Salida bloqueada | La tenencia pasa de minutos a días | Límite de tenencia y alerta |
| Dirección de destino errónea | Pérdida irreversible | Lista blanca y verificación |
| Regla del viaje incumplida | Bloqueo en destino | Verificación antes de enviar |
| Exposición al emisor sin límite | Concentración no medida | Límite por emisor |
| Ahorro atribuido al registro | Decisión sobre una premisa falsa | Descomposición obligatoria |

## Pruebas

```bash
python -m pytest tests/test_cross_border_payments_lab.py -q -k stablecoin
```

```bash
python apps/cross_border_payments_lab/cli.py compare-routes --corridor CL-VN --amount 20000
```

## Entregables

- Los cinco tramos con su coste y su tiempo.
- La comparación completa, con prefinanciación imputada.
- El análisis de sensibilidad al número de intermediarios.
- La descomposición del ahorro por fuente, con el porcentaje atribuible al
  registro.
- La regla de enrutamiento con sus condiciones y controles.
- `solution.md` con la respuesta escrita a la dirección.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Cinco tramos con coste correcto | 20 |
| Comparación sobre la misma base | 25 |
| Sensibilidad a los intermediarios | 20 |
| Descomposición del ahorro por fuente | 25 |
| Regla de enrutamiento con controles | 10 |

## Solución de referencia

En [`solutions/lab-08.md`](../solutions/lab-08.md).
