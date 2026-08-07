# Laboratorio 1: Transferencia con corresponsales

## Propósito

Trazar los cuatro flujos de un pago transfronterizo —mensaje, fondos, contable y
cumplimiento— y demostrar, con código, que se desincronizan.

## Escenario

`Banco Andino` (Chile) debe pagar 10 000 USD a un cliente de `Ngan Hang Viet`
(Vietnam). No tiene relación directa: la cadena pasa por un corresponsal en Nueva
York y otro en Singapur. El equipo cree que «el pago tarda dos días por SWIFT».
Tu tarea es demostrar dónde está realmente el tiempo.

## Contexto

El 80 % de las investigaciones de pagos nacen de una desincronización entre dos
de los cuatro flujos. Un simulador que solo modele el mensaje no puede
reproducir ni un solo incidente real.

## Datos

`apps/cross_border_payments_lab/data/` — participantes, corredores, calendarios
y tipos de referencia. Diccionario en
`datasets/schemas/cross_border_corridors.md`.

## Supuestos del ejercicio

- Tres eslabones: Chile → Nueva York → Singapur → Vietnam.
- Cada plaza tiene su huso horario y su calendario de días inhábiles.
- El cambio de divisa ocurre en la primera pata (diseño A de la clase 13).
- No hay liquidación real: los estados se simulan.

## Requisitos

- Python 3.11 o superior, biblioteca estándar.
- Haber leído las clases 2, 4, 5 y 7.

## Pasos

1. Modela los cuatro flujos como cuatro listas de eventos con marca temporal.
2. Implementa el **flujo de mensaje**: cada eslabón recibe y reenvía, con su
   latencia.
3. Implementa el **flujo de fondos**: cada tramo liquida solo dentro de la
   ventana operativa de su plaza y en día hábil.
4. Implementa el **flujo contable**: los asientos nostro y vostro de cada
   eslabón, en los dos libros.
5. Implementa el **flujo de cumplimiento**: screening en cada eslabón, con una
   probabilidad de alerta y un tiempo de revisión.
6. Ejecuta el pago ordenado a las 16:40 hora de Santiago y mide cuánto tarda
   cada flujo.
7. Repite con el pago ordenado un jueves, con festivo el viernes en Singapur.
8. Genera el informe: cuánto del tiempo total es mensajería, cuánto ventana,
   cuánto calendario y cuánto cumplimiento.

## Arquitectura

```text
MENSAJE      CL ──2s──► NY ──2s──► SG ──2s──► VN
FONDOS       CL ──ventana NY──► ──ventana SG──► ──ventana VN──►
CONTABLE     4 pares de asientos, uno por eslabón
CUMPLIMIENTO screening en CL, NY, SG y VN

                    ▼
        informe de descomposición del tiempo
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los cuatro flujos existen y son independientes | Inspección del modelo |
| 2 | El mensaje tarda segundos | Traza del flujo 1 |
| 3 | Los fondos respetan ventanas y calendarios | Prueba con festivo |
| 4 | Cada asiento tiene su contrapartida | Suma de los dos libros |
| 5 | Una alerta detiene el flujo de fondos, no el de mensaje | Prueba con alerta forzada |
| 6 | El informe descompone el tiempo por causa | Revisión del informe |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Mensaje sin fondos | El beneficiario ve un aviso y no cobra | Estado real, no «enviado» |
| Fondos sin mensaje | Llega dinero que nadie aplica | Referencia extremo a extremo |
| Asiento sin contrapartida | Descuadre en la conciliación | Verificación de suma cero |
| Alerta que detiene todo sin avisar | El cliente no sabe nada | Estado «en revisión» comunicado |
| Festivo no considerado | Se promete un día imposible | Calendario por plaza y por moneda |

## Pruebas

```bash
python -m pytest tests/test_cross_border_payments_lab.py -q -k flujos
```

```bash
python apps/cross_border_payments_lab/cli.py trace --corridor CL-VN --amount 10000
```

## Entregables

- `solution.md` con la descomposición del tiempo por causa.
- Los cuatro flujos implementados y probados.
- El informe de los dos escenarios (día normal y con festivo).
- Tabla de supuestos.
- Nota de límites: qué del modelo es simulación y qué sería real.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Los cuatro flujos, independientes | 30 |
| Ventanas y calendarios correctos | 25 |
| Contabilidad con contrapartida | 20 |
| Descomposición del tiempo | 15 |
| Supuestos y límites declarados | 10 |

## Solución de referencia

En [`solutions/lab-01.md`](../solutions/lab-01.md).
