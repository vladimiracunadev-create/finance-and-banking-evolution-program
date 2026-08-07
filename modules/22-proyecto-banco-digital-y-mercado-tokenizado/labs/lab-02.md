# Laboratorio 2: Perímetro y calificación del proyecto

## Propósito

Determinar qué actividades ejerce el propio sistema **por sus hechos de diseño**, y descubrir los regímenes que nadie había previsto.

El laboratorio anterior fijó qué se construye. Este comprueba qué activa esa construcción, y suele encontrar dos regímenes que ninguna decisión consciente había asumido: entran por una línea de diseño.

## Escenario

El sistema del laboratorio 1 se somete al método de perímetro. Aparecen dos regímenes no previstos y hay que decidir si se asumen o se evitan con un ajuste.

## Contexto

Las clases 3 y 6 aplican al propio proyecto los métodos de la Parte 22: determinar el perímetro por hechos y calificar los instrumentos por criterios.

## Datos

Los hechos de diseño del sistema construido, con su fuente.

## Supuestos del ejercicio

- Los hechos de diseño se documentan con la decisión técnica que los produce.
- La carga incremental por régimen es la declarada en el módulo.
- El segmento no demanda las funciones excluidas.

## Requisitos

- Laboratorio 1 completado.
- Haber leído las clases 3 y 6.

## Pasos

1. Recoge los hechos de diseño con su fuente.
2. Aplica las seis preguntas y anota qué régimen activa cada uno.
3. Identifica los regímenes no previstos.
4. Compara la carga incremental de cada uno con lo que aporta.
5. Propón ajustes de diseño y comprueba que el cliente no pierde.
6. Califica cada producto del catálogo con los cuatro criterios.
7. Decide qué se emite, qué se intermedia y qué se excluye.
8. Calcula el importe de equilibrio de cada producto.

## Arquitectura

```text
HECHO DE DISEÑO → REGIMEN

  «guardamos las claves»      custodia
  «ordenamos las opciones»    asesoria
  «convertimos con margen»    cambio

Y LA PREGUNTA DE ESTA FASE
  ¿podemos tomar otra decision
   sin que el cliente pierda?
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los hechos llevan su fuente | Sin fuente no es un hecho |
| 2 | Dos regímenes no previstos aparecen | Custodia y asesoría |
| 3 | La carga incremental se compara | Con lo que aporta la función |
| 4 | Los ajustes no perjudican al cliente | Comprobación explícita |
| 5 | Cada producto se califica | Cuatro criterios |
| 6 | El importe de equilibrio se calcula | No se elige |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Perímetro supuesto | Se cree saber qué se construye | Determinarlo por hechos |
| Régimen descubierto tarde | Obliga a rediseñar | Determinarlo antes de construir |
| Ajustar quitando valor | Se evita el régimen a costa del cliente | Si el cliente pierde, se asume |
| Calificar por el nombre | Es lo rápido | Los cuatro criterios |
| Mínimo por marketing | «Desde cualquier importe» | Cálculo de equilibrio |

## Pruebas

```bash
python -m pytest tests/test_digital_bank_capstone.py -q -k "alcance or funcion"
```

```bash
python apps/digital_bank_capstone/cli.py scope
```

## Entregables

- Los hechos de diseño con su fuente.
- Los regímenes activados y los previstos.
- Los ajustes de diseño con su efecto sobre el cliente.
- `solution.md` con el catálogo calificado y sus importes de equilibrio.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Hechos con fuente | 20 |
| Regímenes no previstos | 25 |
| Ajustes sin perjuicio | 20 |
| Calificación del catálogo | 20 |
| Importes de equilibrio | 15 |

## Solución de referencia

En [`solutions/lab-02.md`](../solutions/lab-02.md).
