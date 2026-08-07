# Proyecto integrador: Motor de evaluación crediticia

## De qué se trata

Este proyecto codifica en un motor la política de las quince clases anteriores.
No es un ejercicio de programación: es el ejercicio de escribir una política de
crédito con la precisión suficiente para que una máquina la ejecute, que es mucha
más de la que suele tener escrita.

Lo que se evalúa por encima de todo es la explicabilidad. Un motor que aprueba y
rechaza sin decir por qué no se puede defender ante un cliente que reclama ni
ante un supervisor que revisa, y en varias jurisdicciones no se puede usar.

El proyecto **debe incluir una vía formal de excepción**. Un proceso sin ella
produce excepciones informales que nadie registra, que es peor que no tenerlas.

## Contexto

Una entidad quiere automatizar la evaluación de créditos de consumo hasta cierto
importe. Su política existe en un documento de cuarenta páginas escrito en
lenguaje natural, con reglas que se contradicen en al menos dos puntos.

## Alcance

| Incluido | Excluido |
|---|---|
| Política codificada como reglas con su origen | Datos reales de solicitantes |
| Evaluación de renta, capacidad y endeudamiento | Decisiones sobre personas reales |
| Motor de decisión con motivo y trazabilidad | Modelos entrenados con datos reales |
| Vía de excepción con nivel y registro | Uso de atributos protegidos o sus sustitutos |
| Casos de validación de los laboratorios | Puesta en producción de ningún tipo |

## Entregables

| # | Entregable | Qué debe contener |
|---:|---|---|
| 1 | Política codificada | Cada regla con el documento de política que la origina |
| 2 | Capa de cálculo | Renta admisible, capacidad con estrés y endeudamiento consolidado |
| 3 | Motor de decisión | Aprueba, rechaza o deriva, con las tres zonas definidas |
| 4 | Motivo de cada decisión | La regla concreta que la produjo, en lenguaje del cliente |
| 5 | Precedencia entre reglas | Definida y probada con un caso contradictorio |
| 6 | Vía de excepción | Con nivel de aprobación, motivo obligatorio y registro |
| 7 | Casos de validación | Los de los laboratorios 2 a 5, con sus resultados esperados |
| 8 | Documento de límites | Qué no evalúa el motor y qué siempre va a análisis manual |

## Rúbrica

| Criterio | Puntos | Qué se valora |
|---|---:|---|
| Explicabilidad de cada decisión | 25 | Motivo concreto, no puntaje |
| Política separada del código | 20 | Cambiarla no exige tocar el cálculo |
| Cálculo correcto | 20 | Contrastado con los laboratorios |
| Vía de excepción con registro | 15 | Formal, no informal |
| Precedencia definida | 10 | Probada con el caso contradictorio |
| Límites declarados | 10 | Lo que siempre va a análisis manual |

**Total:** 100 puntos. **Aprobación:** 70.

## Restricciones

- **No** se usan datos reales de solicitantes ni de deudores.
- **No** se usan atributos protegidos ni variables que los sustituyan.
- **No** se toma ninguna decisión sobre personas reales con este motor.
- Cada rechazo devuelve su motivo concreto; ninguno devuelve solo un puntaje.
- El motor declara qué no evalúa y qué deriva siempre a análisis manual.

## Cómo se comprueba

```bash
python -m pytest -q
```

## Aviso

Material **docente**. El motor es un ejercicio de formación y **no debe usarse
para decidir sobre personas reales**. Las políticas de crédito y las obligaciones
de explicabilidad varían por jurisdicción y deben verificarse en la norma
vigente.
