# Solución de referencia — Laboratorio 6: comparación con base centralizada

> Material docente. Los números son de una máquina concreta y sirven para
> comparar entre sí, no con producción.

## Mediciones de referencia

```text
10 000 operaciones, misma máquina, mismo conjunto

                        CADENA          BASE COMPARTIDA
  latencia p50           41 ms              0,8 ms
  latencia p95          118 ms              2,1 ms
  latencia p99          260 ms              4,7 ms
  capacidad             ~240 op/s        ~9 800 op/s
  almacenamiento/millón   1,9 GB            0,4 GB
  recuperar un error    compensar         actualizar
                        (nueva operación)  (con traza)
  tiempo de corrección    ~1 bloque         inmediato
```

## Los seis criterios, rellenos

| Criterio | Base compartida | Cadena | Gana |
|---|---|---|---|
| Quién controla el estado | El operador | Ninguno en solitario | Cadena |
| Corrección de un error | Actualización con traza | Compensación | Base |
| Latencia de escritura | 0,8 ms | 41 ms | Base |
| Coste por operación | Bajo | 40× mayor | Base |
| Verificación por un tercero | Requiere confiar | Independiente | Cadena |
| Si el operador desaparece | El sistema muere | Sigue | Cadena |

**Tres a tres.** El empate es el resultado honesto, y el desempate lo dan las
seis preguntas.

## Las seis preguntas, respondidas

```text
1. ¿EL PROBLEMA ES DE CONFIANZA?
   ¿aceptarían un tercero NEUTRAL con gobierno paritario?
   → si la respuesta es sí, la base compartida gana

2. ¿DE COORDINACIÓN?
   sí, y una base compartida también lo resuelve

3. ¿DE DATOS?
   sí, y lo resuelve un formato común, no una cadena

4. ¿DE PROCESO?
   sí, y lo resuelve la automatización

5. ¿REGULATORIO?
   la fricción viene de una obligación: ninguna
   arquitectura la elimina

6. ¿DE LIQUIDEZ?
   no

SOLO LA 1 JUSTIFICA EL SOBRECOSTE
```

## La conclusión honesta

La conclusión del laboratorio depende del caso, y el laboratorio está diseñado
para que **pueda ser negativa**:

```text
SI LA PREGUNTA 1 SE RESPONDE «SÍ, ACEPTARÍAMOS
UN TERCERO NEUTRAL»

  → la base compartida gana en cuatro de seis criterios
    medibles y empata en los otros dos por irrelevancia
  → la conclusión correcta es NO construir la cadena

SI SE RESPONDE «NO, POR NINGUNA VÍA»

  → las dos filas que la cadena gana son las que importan
  → y hay que cuantificar el sobrecoste:
    40× en latencia y ~5× en almacenamiento

UN EXPEDIENTE QUE NUNCA PUEDE CONCLUIR «NO»
NO ES UN ANÁLISIS: ES UNA JUSTIFICACIÓN
```

## Lo que no se midió y hay que declarar

```text
· coste de gobierno del consorcio: puede superar
  al de infraestructura y no está en estos números
· coste de personal especializado
· coste de auditoría de contratos
· coste de la salida
· fiabilidad bajo carga sostenida
· comportamiento con partición de red real

LOS SEIS SE DECLARAN. Omitirlos favorece a la cadena,
porque la base compartida los tiene mucho menores.
```

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Concluir antes de medir | El resultado se busca en vez de encontrarse |
| Omitir las filas que pierde la cadena | El expediente no convence a un comité |
| No declarar lo no medido | Sesga a favor de la cadena |
| Preguntar por un participante en la pregunta 1 | No es la pregunta (clase 1) |
| Comparar con producción | Los números son de una máquina |

## Límites

- Ambas implementaciones son didácticas y se ejecutan en la misma máquina: los
  números comparan entre sí, no con un sistema real.
- No se modela el coste de gobierno, que en un consorcio suele ser el mayor.
- La base compartida no incluye replicación ni alta disponibilidad, que
  encarecerían su columna.
