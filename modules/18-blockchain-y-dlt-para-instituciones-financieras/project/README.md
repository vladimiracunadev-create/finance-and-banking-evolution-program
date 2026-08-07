# Proyecto integrador: red financiera autorizada

## Desafío

Diseña, implementa y **defiende** una red autorizada para un consorcio
financiero. El proyecto se evalúa por la calidad de la **justificación**, no por
la del software: un sistema perfecto sin la pieza 3 del expediente suspende.

## El caso

Cinco entidades quieren compartir el registro de un activo o de un proceso a
elección del estudiante. Requisitos mínimos:

- ninguna acepta que otra opere el registro;
- hay datos sujetos a secreto y a derecho de supresión;
- se exige consulta histórica a 7 años;
- el sistema debe seguir con una entidad caída.

## Requisitos mínimos

1. **Problema y participantes**, con el coste actual medido.
2. **Las seis preguntas de la clase 1**, respondidas una a una, preguntando por
   un tercero **neutral**, no por un participante.
3. **Alternativa de referencia medida**: coste, latencia, capacidad,
   almacenamiento y recuperación de una base de datos compartida operada por una
   sociedad conjunta.
4. **Clasificación por los dos ejes** y obligaciones viables.
5. **Consenso** con su `f` calculado y justificado.
6. **Análisis de independencia efectiva**: quién opera cada nodo, con qué
   software, en qué jurisdicción.
7. **Política de finalidad y aceptación**, con la distinción técnica/jurídica.
8. **Reparto dentro/fuera del registro** y procedimiento de supresión.
9. **Contratos** con máquina de estados, invariantes, control de acceso,
   mecanismo de actualización e interruptor de emergencia.
10. **Gobernanza y plan de recuperación** con sus ocho puntos.
11. **Plan de salida** con los cinco puntos de la clase 7.
12. **Límites declarados**.

## Entregables

```text
project/
├── README.md
├── requirements.md
├── architecture.md
├── assumptions.md
├── risk-register.md
├── regulatory-matrix.md
├── security.md
├── baseline-comparison.md      ← la pieza 3, medida
├── data/
├── src/
├── tests/
├── evidence/
├── presentation-outline.md
├── rubric.md
└── solution-reference/
```

`baseline-comparison.md` es específico de esta parte y es el documento que más
pesa: contiene la medición de la alternativa que no usa registro distribuido.

## Criterios de aceptación

| # | Criterio | Verificación |
|---:|---|---|
| 1 | La alternativa está medida, no afirmada | Números en `baseline-comparison.md` |
| 2 | La pregunta 1 se hizo sobre un tercero neutral | Redacción de la respuesta |
| 3 | `f` corresponde al número de nodos | Cálculo |
| 4 | La independencia efectiva se analiza | Tabla por nodo |
| 5 | Una transacción repetida se rechaza | Prueba |
| 6 | El ataque de reentrada falla | Prueba negativa |
| 7 | El interruptor detiene sin alterar | Prueba de estado |
| 8 | Ningún dato personal dentro del registro | Revisión del reparto |
| 9 | El plan de salida tiene los cinco puntos | Revisión |
| 10 | Sin secretos ni datos personales | `detect_secrets.py`, `detect_pii.py` |
| 11 | Cada norma citada tiene fecha | `validate_metadata.py` |
| 12 | Los límites están declarados | Sección obligatoria |

## Defensa

Doce minutos ante un panel que hace de comité de riesgo. Las seis preguntas que
siempre llegan:

1. ¿Por qué no una base de datos compartida?
2. ¿Qué pasa si dos participantes se caen a la vez?
3. ¿Quién puede cambiar las reglas, y en cuánto tiempo?
4. Si mañana queremos salir, ¿qué nos llevamos y qué cuesta?
5. ¿Qué dato personal hay dentro?
6. ¿Qué parte de esto no habéis probado?

## Rúbrica

| Área | Peso | Qué distingue el nivel alto |
|---|---:|---|
| Problema y alternativa medida | 25 % | Números, y disposición a concluir que no compensa |
| Consenso e independencia | 20 % | Analiza fallos conjuntos, no cuenta nodos |
| Privacidad y reparto | 15 % | Decidido al diseñar, con supresión resuelta |
| Contratos y controles | 15 % | Ataque demostrado y corregido |
| Gobernanza y recuperación | 15 % | Política de reversión escrita **antes** |
| Salida y límites | 10 % | Precio de salida conocido |

## Una nota sobre la conclusión

**Un proyecto que concluye «la base de datos compartida es mejor» y lo demuestra
con números obtiene la máxima calificación.** El objetivo de la parte no es
construir una red: es saber cuándo hace falta y cuándo no.

## Solución de referencia

`solution-reference/` contiene un expediente comentado. Es material **docente**:
sirve para corregir y para desbloquear, no para entregar.

## Límites de este proyecto

- La implementación es **didáctica**: la criptografía, el consenso y los
  contratos son simulaciones, no código de producción.
- **No se crea ninguna criptomoneda** ni se despliega nada en una red pública.
- Los números de la comparación son de una máquina concreta y comparan entre sí.
- La matriz regulatoria refleja una consulta con fecha y **no sustituye asesoría
  legal**.
