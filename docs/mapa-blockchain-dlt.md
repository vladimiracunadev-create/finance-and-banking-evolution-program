# Mapa de blockchain y DLT

Guía de navegación de la Parte 19: dónde está cada concepto, con qué se conecta
y qué se puede ejecutar para comprobarlo.

## El eje de la parte

```text
UN REGISTRO DISTRIBUIDO PERMITE QUE PARTES QUE NO CONFÍAN
ENTRE SÍ NI EN UN TERCERO COMÚN MANTENGAN UN REGISTRO
QUE NINGUNA CONTROLA

  eso es lo único que da, y lo da caro:
  redundancia total, lentitud, irreversibilidad

LA PREGUNTA NO ES «¿SE PUEDE?»
ES «¿EXISTE AQUÍ UN TERCERO DE CONFIANZA DISPONIBLE?»
```

Y la pregunta hay que hacerla bien: no «¿confiamos en ese participante?», sino
**«¿aceptaríamos un tercero neutral?»**. Casi todos los proyectos que se
justifican mal han respondido la primera creyendo responder la segunda.

## Las seis preguntas del criterio

| Pregunta | ¿Justifica un registro distribuido? |
|---|---|
| ¿El problema es de **confianza**? | **Sí**, es la única que lo hace por sí sola |
| ¿De coordinación? | No: una base compartida lo resuelve |
| ¿De datos? | No: lo resuelve un formato común |
| ¿De proceso? | No: lo resuelve la automatización |
| ¿Regulatorio? | No: ninguna arquitectura elimina una obligación |
| ¿De liquidez? | No |

## Recorrido de la parte

```text
CRITERIO        1 · qué resuelve y a qué precio
                       │
PIEZAS          2 · resúmenes, firmas, Merkle    3 · claves y custodia
                       │
ANATOMÍA        4 · transacciones, bloques, estado
                       │
ACUERDO         5 · consenso     6 · finalidad
                       │
CONFIGURACIÓN   7 · pública, privada, autorizada
                       │
EJECUCIÓN       8 · contratos    9 · oráculos
                       │
LÍMITES        10 · privacidad  11 · puentes  12 · escalabilidad
                       │
GOBIERNO       13 · gobernanza y recuperación
                       │
INTEGRACIÓN    14 · expediente y defensa
```

## Dónde está cada concepto

| Concepto | Clase | Laboratorio | Código |
|---|:---:|:---:|---|
| Las seis preguntas del criterio | 1 | 6 | — |
| Consistencia frente a disponibilidad | 1 | 4 | `consensus` |
| Fallo por caída y bizantino | 1, 5 | 4 | `consensus` |
| Función de resumen y sus propiedades | 2 | 1 | `crypto` |
| Qué demuestra y qué no una firma | 2 | 2 | `crypto` |
| Árbol de Merkle y prueba de inclusión | 2 | 3 | `merkle` |
| Prueba de exclusión | 2 | 3 | `merkle` |
| Árbol con sumas | 2, 10 | 3 | `merkle` |
| Clave, clave pública y dirección | 3 | 2 | `crypto` |
| Cuatro modelos de custodia | 3 | 2 | — |
| Elección del umbral m-de-n | 3 | 2 | `signatures` |
| Correlación entre guardianes | 3 | 2 | `signatures` |
| Ciclo de una transacción | 4 | 1 | `chain` |
| Modelos de estado y repetición | 4 | 1 | `chain` |
| Tipos de nodo | 4 | — | — |
| Crecimiento e instantáneas | 4, 12 | 1 | `chain` |
| Tres familias de consenso | 5 | 4 | `consensus` |
| Umbral de 3f + 1 | 5 | 4 | `consensus` |
| Independencia efectiva | 5 | 4 | `consensus` |
| Finalidad probabilística y determinística | 6 | 4 | — |
| Finalidad jurídica | 6 | — | — |
| Reorganizaciones | 6 | 1 | `chain` |
| Los dos ejes de una red | 7 | 6 | — |
| Gobierno del consorcio | 7, 13 | — | — |
| Contratos y sus seis defectos | 8 | 5 | `contracts` |
| Reentrada | 8 | 5 | `contracts` |
| Interruptor de emergencia | 8, 13 | 5 | `contracts` |
| Oráculos y coste de manipulación | 9 | 5 | `oracle` |
| Mediana frente a media | 9 | 5 | `oracle` |
| Confidencialidad, anonimato, no vinculabilidad | 10 | 3 | — |
| Inmutabilidad y derecho de supresión | 10 | — | — |
| Puentes y su umbral efectivo | 11 | 6 | — |
| Escalabilidad y el supuesto que cambia | 12 | 6 | — |
| Valor extraíble del orden | 12 | 4 | `consensus` |
| Compensación frente a reversión | 13 | 5 | — |
| Plan de recuperación | 13 | 5 | — |
| Expediente en doce piezas | 14 | proyecto | — |

## Las cinco afirmaciones que la parte desmonta

1. **«Una vez en la cadena, no se puede cambiar.»** Recalcular la cadena entera
   vuelve a validar. La inmutabilidad la dan el consenso y el coste de rehacer.
2. **«Está firmado, luego es cierto.»** Una firma prueba quién, no qué es verdad.
3. **«Publicamos la raíz, es verificable.»** Sin sumas, omitir una hoja no se
   detecta.
4. **«Cinco nodos toleran un fallo.»** Tres con el mismo defecto acuerdan un
   valor erróneo.
5. **«Sin terceros de confianza.»** Con un oráculo, un comité y un fondo, hay
   tres.

Las cinco tienen una prueba en
[`tests/test_dlt_financial_lab.py`](../tests/test_dlt_financial_lab.py), y tres
de ellas **documentan defectos y deben pasar**.

## Qué se puede ejecutar

```bash
python apps/dlt_financial_lab/cli.py chain --blocks 100 --difficulty 2
```

```bash
python apps/dlt_financial_lab/cli.py merkle --leaves 10000
```

```bash
python apps/dlt_financial_lab/cli.py consensus --nodes 5 --common-fault 3
```

```bash
python apps/dlt_financial_lab/cli.py escrow
```

```bash
python -m pytest tests/test_dlt_financial_lab.py -q
```

## La conclusión que la parte permite

Un proyecto de esta parte **puede concluir que no hace falta un registro
distribuido, y eso es la máxima calificación**. El objetivo no es construir una
red: es saber cuándo hace falta y cuándo una base de datos compartida operada
por una sociedad conjunta hace lo mismo más barato, más rápido y corregible.

## Hacia dónde sigue

| De esta parte | A | Qué se profundiza |
|---|---|---|
| El registro (todo) | Parte 20 | El activo que circula sobre él |
| Contratos y custodia (3, 8) | Parte 21 | El instrumento financiero tokenizado |
| Redes y gobierno (7, 13) | Parte 22 | El régimen de la infraestructura |
| Todo | Parte 23 | La infraestructura del mercado tokenizado |

---

**Ver también:** [Parte 19](../modules/18-blockchain-y-dlt-para-instituciones-financieras/README.md) ·
[Etapa 5](etapa-5-finanzas-digitales.md) ·
[DLT Financial Lab](../apps/dlt_financial_lab/README.md) ·
[Glosario de finanzas digitales](glosario-finanzas-digitales.md)
