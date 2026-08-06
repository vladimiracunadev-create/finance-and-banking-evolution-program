# Fichas normativas estructuradas

Este directorio guarda **una ficha por instrumento normativo**, en formato
legible por máquina, para que el programa pueda responder tres preguntas sin
depender de la memoria de nadie:

1. ¿qué norma regula esta actividad, en esta jurisdicción?
2. ¿en qué estado está y desde cuándo?
3. ¿cuándo se verificó por última vez y contra qué fuente?

## Por qué existe

Una norma citada sin fecha de verificación es una afirmación que no caduca.
Dentro de un año nadie sabrá si seguía siendo cierta. Todo el material
regulatorio del programa se apoya en que la vigencia se comprueba, y esa
comprobación necesita quedar registrada en algún sitio.

`tools/validate_metadata.py` falla si una ficha no tiene fecha, si la fecha no
es una fecha o si está en el futuro.

## Estructura

```text
regulatory/
├── chile/
├── union-europea/
└── internacional/
```

## Formato

Las fichas usan a propósito un **subconjunto plano de YAML** —`clave: valor`,
bloques `>-` y listas con guion—. El repositorio se valida con la biblioteca
estándar de Python y no añade una dependencia solo para leer doce campos.

```yaml
country:
authority:
instrument_type:
instrument_number:
title:
publication_date:
effective_date:
implementation_stage:
status:
scope:
activities_covered:
official_source:
last_verified:
supersedes:
superseded_by:
notes:
```

Campos obligatorios: `country`, `authority`, `instrument_type`,
`instrument_number`, `title`, `publication_date`, `implementation_stage`,
`status`, `scope`, `official_source`, `last_verified`.

## Límites

- **Ninguna ficha es asesoría legal.** Son un índice de trabajo, no una fuente.
- La fuente es siempre el sitio oficial de la autoridad; la ficha solo apunta a
  él y registra cuándo se consultó.
- Una ficha con `last_verified` antiguo no es un error: es una señal de que hay
  que volver a comprobar. El validador exige que la fecha exista y sea
  coherente, no que sea reciente.
- El calendario real de exigibilidad suele estar en las disposiciones
  transitorias y en los anexos técnicos, no en el cuerpo del instrumento.

## Verificación

```bash
python tools/validate_metadata.py
```
