# Proyecto integrador: red de pagos transfronterizos

## Desafío

Diseña, implementa y defiende una **red de pagos transfronterizos** que atienda
seis corredores con características distintas. El proyecto se evalúa por el
**criterio con que eliges entre rutas** y por la honestidad con que atribuyes tus
resultados, no por la ruta que implementas.

## Alcance

| Incluido | Fuera de alcance |
|---|---|
| Motor de rutas con seis criterios | Conexión con redes de pago reales |
| Los cuatro flujos de cada pago | Liquidación real de fondos |
| Mensajería ISO 20022 sintética | Conformidad plena con las guías de uso |
| Screening con métricas | Listas de sanciones oficiales |
| Modelo de liquidez y prefinanciación | Operación con divisas reales |
| Comparación de cuatro arquitecturas | Despliegue en producción |
| Quince métricas medidas | Carga sostenida |

## Los seis corredores

Cada uno está diseñado para forzar una decisión distinta:

| Corredor | Característica | Qué obliga a decidir |
|---|---|---|
| A | Enlace de pagos inmediatos disponible | Prioridad del enlace |
| B | Cadena clásica de un intermediario | Ruta clásica frente a alternativa |
| C | Cadena clásica de tres intermediarios | Punto de cruce de la ruta alternativa |
| D | Salida ilíquida en destino | Descartar la ruta con stablecoin |
| E | Diferencia horaria de 12 horas | Ventanas y compromiso de fecha |
| F | Receptor mayoritariamente sin cuenta | Última milla y exclusión |

## Requisitos mínimos

1. **Motor de rutas** con los seis criterios en orden: elegibilidad,
   cumplimiento y disponibilidad como **filtros**; tiempo, coste y riesgo como
   factores ponderados. Cada decisión devuelve su **motivo**.
2. **Los cuatro flujos** modelados de forma independiente, con ventanas, husos y
   calendarios.
3. **Mensajería ISO 20022** válida, con la cadena de estados completa, incluidos
   rechazo, cancelación y devolución.
4. **Screening** con precisión y exhaustividad medidas, y prueba retrospectiva
   ante cualquier cambio de umbral.
5. **Modelo de liquidez**: saldo objetivo por corredor, coste de prefinanciación
   y efecto del netting.
6. **Comparación de cuatro arquitecturas** por corredor: corresponsalía, enlace
   de pagos inmediatos, ruta con stablecoin y depósito tokenizado.
7. **Quince métricas**, reportadas en percentiles p50, p95 y p99 las de tiempo.
8. **Descomposición del ahorro por fuente** de tu arquitectura preferida, con el
   porcentaje atribuible a la tecnología aislado.
9. **Matriz regulatoria**: actividad → obligación → autoridad → fuente oficial →
   fecha de verificación → limitaciones.
10. **Contingencia ensayada** en al menos un corredor, con su resultado medido.
11. **Registro de decisiones** con los cuatro campos: decisión, alternativa,
    motivo y **consecuencia**.
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
├── data/
├── src/
├── tests/
├── evidence/
├── presentation-outline.md
├── rubric.md
└── solution-reference/
```

| Archivo | Qué contiene |
|---|---|
| `requirements.md` | Corredores, criterios de enrutamiento y compromisos |
| `architecture.md` | Los cuatro flujos, componentes y diagramas |
| `assumptions.md` | Supuestos y su efecto si cambian |
| `risk-register.md` | Riesgos priorizados por impacto × probabilidad |
| `regulatory-matrix.md` | Seis columnas, con fecha de verificación |
| `security.md` | Cumplimiento, screening y gestión de secretos |
| `evidence/` | Trazas, métricas, informe de contingencia |
| `presentation-outline.md` | Guion de la defensa de 12 minutos |

## Criterios de aceptación

| # | Criterio | Verificación |
|---:|---|---|
| 1 | Un filtro no se compensa con precio | Prueba negativa |
| 2 | Toda decisión tiene motivo | Ninguna respuesta sin el campo |
| 3 | El corredor A elige el enlace | Prueba por corredor |
| 4 | El corredor D descarta la stablecoin | Prueba por corredor |
| 5 | Los mensajes ISO 20022 validan | `tools/validate_iso20022.py` |
| 6 | Un reintento no genera un duplicado | Prueba de referencia estable |
| 7 | Las quince métricas se reportan | Informe completo |
| 8 | Las de tiempo van en percentiles | Revisión del informe |
| 9 | El ahorro está descompuesto por fuente | Suma igual al total |
| 10 | La contingencia se ensayó | Informe con fecha y resultado |
| 11 | No hay secretos ni datos personales | `detect_secrets.py`, `detect_pii.py` |
| 12 | Cada norma citada tiene fecha | Revisión de la matriz |

## Defensa

Doce minutos ante un panel que hace de comité de pagos. Las cuatro preguntas que
siempre se hacen:

1. ¿Por qué esta ruta para el corredor C y no la otra?
2. Este ahorro, ¿de dónde viene exactamente?
3. Enséñame el corredor F: ¿qué pasa con quien no tiene cuenta?
4. ¿Qué parte de esto no has probado?

## Rúbrica

| Área | Peso | Qué distingue el nivel alto |
|---|---:|---|
| Motor de rutas y criterios | 25 % | Filtros antes de ponderar; motivo reconstruible |
| Métricas y medición | 20 % | Quince métricas, percentiles, no promedios |
| Cumplimiento | 20 % | Prueba retrospectiva y clasificación por causa |
| Arquitectura y contingencia | 15 % | Alternativa ensayada, no documentada |
| Análisis de coste y atribución | 15 % | Ahorro descompuesto por fuente |
| Límites declarados | 5 % | Se dice qué no se cubrió, antes de que lo pregunten |

## Solución de referencia

`solution-reference/` contiene una implementación comentada. Es material
**docente**: sirve para corregir y para desbloquear, no para entregar. Un
proyecto que la reproduce sin decisiones propias obtiene el mínimo de la franja
de aprobación.

## Límites de este proyecto

- Entorno simulado: no hay red de pagos real ni movimiento de fondos.
- Datos sintéticos: no reproducen distribuciones reales de volumen ni de coste.
- Las cifras de coste y plazo son ilustrativas.
- Los proyectos institucionales citados son pilotos o pruebas de concepto.
- La matriz regulatoria refleja una consulta con fecha y **no sustituye asesoría
  legal**.
