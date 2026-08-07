# Laboratorio 1: Clasificador de activos digitales

## Propósito

Construir la ficha de cinco preguntas y comprobar que **clasifica correctamente
sin mirar ni una línea de código, ni una red, ni un estándar de contrato**.

## Escenario

Una tesorería recibe cuatro propuestas presentadas como «dólares digitales». Hay
que clasificarlas, rastrear su respaldo y decidir cuáles sirven para mantener
saldo operativo.

## Contexto

La clase 1 sostiene que dos instrumentos idénticos técnicamente pueden tener
regímenes opuestos. La clase 9 añade que la sustancia manda sobre el nombre: un
producto que cumple los tres elementos es dinero electrónico aunque se llame
token.

## Datos

Cuatro fichas sintéticas, más las cadenas de respaldo de cada instrumento.

## Supuestos del ejercicio

- Los términos contractuales se dan por escritos y verificables.
- La verificación regulatoria de cada jurisdicción queda fuera del alcance.
- Los importes son enteros.

## Requisitos

- Haber leído las clases 1, 8, 9 y 10.
- Python 3.11 o superior.

## Pasos

1. Construye la ficha de cinco preguntas de las cuatro propuestas.
2. Clasifica cada una con `clasificar()` y comprueba que el resultado no depende
   de la red.
3. Aplica `apta_para_tesoreria()` con un saldo de 40 000 y con uno de 500 000, y
   explica por qué el resultado cambia.
4. Rastrea el respaldo de cada instrumento con `CadenaDeRespaldo` hasta un
   activo externo.
5. Demuestra que uno de ellos es **circular** y que por tanto no llega a ningún
   activo fuera del sistema.
6. Aplica los tres elementos del dinero electrónico a las cuatro propuestas.
7. Enumera los incumplimientos de la que se presenta como token estable.
8. Añade la ficha de un depósito tokenizado y otra de una CBDC, y comprueba que
   la misma función las separa.

## Arquitectura

```text
Ficha(5 preguntas) ──► clasificar() ──► Tipo

CadenaDeRespaldo
   S ──► letras (externo)        rastreo termina: OK
   E ──► V ──► E                 rastreo cierra ciclo: CIRCULAR

TresElementos(v, f, t) ──► es_dinero_electronico
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | La clasificación no usa datos técnicos | Revisión del código de `clasificar` |
| 2 | El umbral cambia la aptitud | Dos saldos, dos resultados |
| 3 | El respaldo circular se detecta | `es_circular` verdadero |
| 4 | El respaldo exógeno llega a un activo real | `llega_a_activo_externo` |
| 5 | Los tres elementos califican | Cuatro propuestas evaluadas |
| 6 | Los incumplimientos se enumeran | Tres, con su motivo |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Clasificar por el nombre | Régimen equivocado | Ficha de cinco preguntas |
| Detener el rastreo pronto | Respaldo circular no visto | Rastrear hasta activo externo |
| Ignorar el umbral | Se supone un derecho que no se tiene | Evaluar con el saldo real |
| Confundir soporte con sustancia | Depósito tratado como criptoactivo | Clasificar por el obligado |
| Aceptar «respaldado» sin más | Se asume calidad | Preguntar con qué y quién lo verifica |

## Pruebas

```bash
python -m pytest tests/test_digital_assets_risk_lab.py -q -k "clasificacion or respaldo or elementos or minimo"
```

## Entregables

- Las cuatro fichas con su clasificación y su justificación.
- El rastreo de respaldo de cada una, con el ciclo detectado.
- La evaluación de aptitud con dos saldos distintos.
- `solution.md` con la decisión de tesorería y su fundamento.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Fichas completas y correctas | 25 |
| Clasificación justificada por la promesa | 20 |
| Rastreo de respaldo y detección de circularidad | 25 |
| Aplicación de los tres elementos | 20 |
| Decisión de tesorería fundamentada | 10 |

## Solución de referencia

En [`solutions/lab-01.md`](../solutions/lab-01.md).
