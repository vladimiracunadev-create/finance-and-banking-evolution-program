# Proyecto integrador: Tablero integrado de riesgos

## De qué se trata

Este proyecto construye el instrumento con el que un comité de riesgos dirige, y
lo somete a la prueba que justifica que exista: un escenario único aplicado a
todos los riesgos a la vez.

Ese es su hallazgo. Los quince riesgos de la parte se miden por separado, con
metodologías distintas y por áreas distintas, y cada uno puede estar dentro de su
límite. Cuando el mismo escenario los golpea a todos, varios se activan
simultáneamente y algunas acciones comprometidas resultan incompatibles entre sí.

El tablero **debe declarar qué interacciones no captura**. Ningún tablero las
captura todas, y decir cuáles quedan fuera es lo que impide confiar de más.

## Contexto

El comité de riesgos de un banco recibe quince informes mensuales, uno por
riesgo, cada uno de un área distinta. Todos indican cumplimiento. El directorio
pregunta qué pasaría si todos los riesgos se materializaran por la misma causa, y
nadie tiene la respuesta.

## Alcance

| Incluido | Excluido |
|---|---|
| Los quince riesgos con su métrica y su límite | Datos reales de una entidad |
| Escenario único y su traducción por riesgo | Modelos internos de capital autorizados |
| Interacciones y acciones incompatibles | Cumplimiento regulatorio real |
| Escalamiento con niveles de decisión | Sustitución de la función de riesgos |
| Declaración de lo que el tablero no captura | Certificación de suficiencia de capital |

## Entregables

| # | Entregable | Qué debe contener |
|---:|---|---|
| 1 | Tablero de quince métricas | Cada una con su límite, su holgura y su tendencia |
| 2 | Ficha por métrica | Definición, fuente, frecuencia, umbral de alerta y responsable |
| 3 | Escenario único | Narrativa coherente y suficientemente severa |
| 4 | Traducción por riesgo | Cómo el escenario afecta a cada una de las quince |
| 5 | Resultado bajo escenario | Qué se activa, en qué orden y en qué momento |
| 6 | Interacciones | Métricas que se deterioran por el deterioro de otras |
| 7 | Acciones comprometidas | Con su compatibilidad verificada entre pares |
| 8 | Escalamiento | Niveles, plazos y quién decide en cada uno |
| 9 | Límites del tablero | Qué interacciones no captura y por qué |

## Rúbrica

| Criterio | Puntos | Qué se valora |
|---|---:|---|
| Interacciones detectadas | 25 | Lo que la medición individual no ve |
| Escenario coherente y severo | 20 | Rompe algo, y con narrativa |
| Métricas con ficha completa | 15 | Definición, fuente y responsable |
| Acciones compatibles | 15 | Verificadas entre pares |
| Escalamiento con decisión | 15 | Quién decide, en qué plazo |
| Límites declarados | 10 | Lo que no captura |

**Total:** 100 puntos. **Aprobación:** 70.

## Restricciones

- **No** se usan datos reales de ninguna entidad financiera.
- **No** se presenta como evaluación de suficiencia de capital ni de cumplimiento.
- Todos los balances, carteras y parámetros son sintéticos y están declarados.
- Los supuestos conductuales y de correlación se declaran siempre.
- El tablero declara qué interacciones no captura.

## Aviso

Material **docente**. Las carteras y los parámetros son sintéticos. **No
constituye una evaluación de riesgos ni de capital** para ninguna entidad real, y
no sustituye los marcos internos que cada supervisor exige y autoriza.
