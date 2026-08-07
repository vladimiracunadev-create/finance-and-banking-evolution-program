# Laboratorio 6: Custodia y segregación

## Propósito

Medir la **independencia efectiva** de un esquema de umbral y comprobar que el
control que detiene el ataque más común no es criptográfico: es una espera de
48 horas.

## Escenario

Un custodio institucional propone un esquema 3-de-5 con cinco directivos, tres
en la misma oficina y todos con el mismo modelo de dispositivo. Hay que
evaluarlo, corregirlo y diseñar la recuperación.

## Contexto

La clase 12 sostiene que «3 de 5» no dice nada por sí solo, y que lo que importa
es qué eventos dejan inoperativos a cuántos a la vez. La clase 11 añade que toda
condición programada necesita una vía de excepción.

## Datos

Dos distribuciones de guardianes, una inicial y otra corregida.

## Supuestos del ejercicio

- Probabilidad anual de indisponibilidad por guardián: 4 %.
- El cálculo de probabilidad supone independencia, y ese supuesto solo es
  defendible tras la corrección.
- La lista blanca contiene un único destino conocido.

## Requisitos

- Laboratorio 5 completado.
- Haber leído las clases 11 y 12, y la Parte 19, clase 5.

## Pasos

1. Construye el esquema inicial y calcula `grupos_correlacionados()`.
2. Comprueba que la independencia efectiva es 1 y que no tolera un evento
   correlacionado.
3. Redistribuye ubicación, dispositivo, jurisdicción y proveedor **sin cambiar
   el umbral**, y vuelve a medir.
4. Calcula la probabilidad de bloqueo en ambos y explica por qué es idéntica.
5. Diseña la recuperación con `Recuperacion` y enumera sus defectos si el umbral
   no supera al de firma.
6. Configura `PoliticaDeRetirada` y ejecuta el escenario de sesión comprometida;
   anota las horas de detección ganadas.
7. Ejecuta el escenario de importe alto sin segunda aprobación.
8. Clasifica cinco condiciones programables como pago o dinero programable, y
   redacta la vía de excepción con sus cuatro elementos.

## Arquitectura

```text
Esquema(umbral, guardianes)
   grupos_correlacionados()  ubicación · dispositivo ·
                             jurisdicción · proveedor
   independencia_efectiva()  n − peor_grupo + 1

Retirada  →  1 origen  2 lista blanca  3 ESPERA 48 h
             4 límite   5 segunda aprobación fuera de banda
             6 dirección completa  7 registro
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | El esquema inicial tiene independencia 1 | Cálculo |
| 2 | La corrección no cambia el umbral | Sigue siendo 3-de-5 |
| 3 | El esquema corregido tolera un evento | `tolera_evento_correlacionado` |
| 4 | La recuperación defectuosa se detecta | Dos defectos enumerados |
| 5 | La lista blanca gana 48 horas | Escenario de ataque |
| 6 | Las cinco condiciones se clasifican | Prueba de la restricción |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Guardianes en la misma oficina | Un evento alcanza el umbral | Distribución geográfica |
| Mismo dispositivo | Una vulnerabilidad afecta a todos | Diversificar fabricante |
| Recuperación igual de fácil | Segundo camino de ataque | Umbral mayor y retardo |
| Destino nuevo sin espera | Retirada inmediata al atacante | Espera de 48 horas |
| Sin segregación jurídica | El cliente es acreedor ordinario | Cláusulas de propiedad |
| Señal de coacción sin probar | No existe cuando hace falta | Simulacro documentado |

## Pruebas

```bash
python -m pytest tests/test_digital_assets_risk_lab.py -q -k "independencia or redistribuir or recuperacion or lista_blanca or importe_alto"
```

```bash
python apps/digital_assets_risk_lab/cli.py custody
```

## Entregables

- Los grupos correlacionados de ambas distribuciones.
- La independencia efectiva antes y después.
- El diseño de recuperación con umbral, retardo y cancelación.
- El escenario de ataque con las horas ganadas.
- `solution.md` con la clasificación de condiciones y la vía de excepción.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Medición de independencia efectiva | 25 |
| Redistribución sin tocar el umbral | 20 |
| Diseño de recuperación | 20 |
| Escenario de ataque y controles | 20 |
| Vía de excepción con cuatro elementos | 15 |

## Solución de referencia

En [`solutions/lab-06.md`](../solutions/lab-06.md).
