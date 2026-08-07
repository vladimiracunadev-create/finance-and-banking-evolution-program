# DLT Financial Lab

Laboratorio de registro distribuido de la **Parte 19**. Implementa una cadena,
firmas, árboles de Merkle con sumas, consenso bizantino, un contrato de depósito
en garantía y un oráculo, **con la biblioteca estándar y sin red**.

> ## Aviso
>
> **Todo lo que hay aquí es didáctico.** La criptografía está simplificada, el
> consenso no reproduce ningún protocolo de producción y la cadena no es segura.
> **No debe usarse para nada real** y **no crea ninguna criptomoneda**. En
> producción se usan bibliotecas auditadas, nunca una implementación propia.

## Qué demuestra ejecutando

Cinco afirmaciones que se repiten mucho y se comprueban poco:

| Afirmación habitual | Lo que el laboratorio demuestra | Clase |
|---|---|---|
| «Una vez en la cadena, no se puede cambiar» | Recalcular la cadena entera vuelve a validar | 1, 4 |
| «Está firmado, luego es cierto» | Una firma prueba **quién**, no qué es verdad | 2 |
| «Publicamos la raíz, es verificable» | Sin sumas, omitir una hoja no se detecta | 2, 10 |
| «Cinco nodos toleran un fallo» | Tres con el mismo defecto acuerdan un valor erróneo | 5 |
| «El contrato está auditado» | Dos líneas intercambiadas lo vacían | 8 |

## Estructura

```text
apps/dlt_financial_lab/
├── README.md
├── __init__.py
├── crypto.py       resúmenes, firmas y direcciones con verificación
├── merkle.py       árbol con sumas, inclusión y exclusión
├── chain.py        bloques, estado, instantáneas y reescritura
├── consensus.py    nodos honestos, silenciosos, mentirosos y con defecto común
├── contracts.py    depósito en garantía, con y sin reentrada
├── oracle.py       agregación con mediana, banda y mínimo de fuentes
├── signatures.py   firma múltiple y análisis de correlación
└── cli.py
```

## Uso

Demostrar que el encadenamiento no impide reescribir:

```bash
python apps/dlt_financial_lab/cli.py chain --blocks 100 --difficulty 2
```

Construir el árbol y ver que la omisión de una hoja se detecta con sumas:

```bash
python apps/dlt_financial_lab/cli.py merkle --leaves 10000
```

Provocar un acuerdo sobre un valor erróneo con un fallo común:

```bash
python apps/dlt_financial_lab/cli.py consensus --nodes 5 --common-fault 3
```

Ejecutar el ataque de reentrada y su corrección:

```bash
python apps/dlt_financial_lab/cli.py escrow
```

Comparar con una base de datos compartida:

```bash
python apps/dlt_financial_lab/cli.py compare --operations 5000
```

## Pruebas

```bash
python -m pytest tests/test_dlt_financial_lab.py -q
```

Tres de ellas **documentan defectos y deben pasar**:

- `test_recalcular_toda_la_cadena_NO_se_detecta`
- `test_un_fallo_comun_produce_acuerdo_erroneo`
- `test_el_ataque_de_reentrada_vacia_el_contrato_defectuoso`

Sin ellas, el material afirmaría cosas que el código no sostiene.

## Decisiones de diseño que conviene mirar

**Prefijos distintos en el árbol.** `\x00` para hoja y `\x01` para nodo interno.
Sin ellos existen dos conjuntos con la misma raíz.

**Promoción del nodo suelto.** En un nivel impar, el nodo sin pareja se promueve
tal cual en vez de duplicarse: duplicarlo sumaría su valor dos veces y la raíz
dejaría de declarar la suma real, que es la propiedad por la que existe el árbol.

**Número de orden por cuenta.** Sin él, la misma transacción firmada se reenvía y
se ejecuta dos veces. Es la idempotencia de la Parte 17, clase 8, resuelta en el
protocolo.

**El interruptor solo para.** No altera saldos ni transfiere. Da capacidad de
contener sin dar a nadie capacidad de mover fondos.

## Límites declarados

- **La firma es simétrica en la práctica**: quien puede verificar podría también
  firmar. Es una simplificación deliberada y se declara en el módulo.
- El consenso no modela pérdida de mensajes, partición de red ni desajuste de
  relojes salvo cuando se indica.
- La cadena corre en un solo proceso: no hay propagación ni mempool real.
- El contrato es una clase de Python: no reproduce el modelo de ejecución ni el
  coste de ninguna plataforma.
- La comparación con SQLite mide entre sí, no contra producción, y **no incluye
  el coste de gobierno**, que en un consorcio suele ser el mayor.

## Referencias

- [Parte 19 — Blockchain y DLT para instituciones financieras](../../modules/18-blockchain-y-dlt-para-instituciones-financieras/README.md)
- [Etapa 5](../../docs/etapa-5-finanzas-digitales.md)
