# Proyecto integrador: Plataforma bancaria digital

## De qué se trata

Este proyecto diseña una plataforma que usa varias de las tecnologías de la
parte, y su criterio de calificación es incómodo: se valora tanto lo que se
adopta como lo que se descarta con la comparación hecha.

La razón es que en este ámbito la presión por adoptar suele preceder al análisis.
Un registro distribuido donde una base centralizada resolvería lo mismo, un
modelo donde bastaba una regla, o un consentimiento en bloque donde la norma pide
alcance por finalidad son decisiones que se toman por defecto y cuestan años.

El proyecto **debe clasificar cada caso de uso de modelos por su efecto sobre las
personas** y definir controles proporcionales, porque aplicar el máximo a todo
hace inviable la plataforma sin proteger más a nadie.

## Contexto

Un banco quiere lanzar una plataforma digital con originación de crédito,
agregación de cuentas de otras entidades, detección de fraude y un asistente
conversacional. El comité de tecnología ha propuesto usar un registro distribuido
para la conciliación con dos socios.

## Alcance

| Incluido | Excluido |
|---|---|
| Arquitectura de datos con linaje y gobierno | Datos reales de clientes |
| Consentimiento con alcance por finalidad | Modelos entrenados con datos reales |
| Casos de uso de modelos clasificados por riesgo | Decisiones sobre personas reales |
| Detección de fraude con costo total | Uso de atributos protegidos o sus sustitutos |
| Comparación con alternativas descartadas | Puesta en producción |

## Entregables

| # | Entregable | Qué debe contener |
|---:|---|---|
| 1 | Arquitectura de datos | Capas, dato maestro, identificador único y linaje desde el origen |
| 2 | Diseño de consentimiento | Alcances por finalidad, vigencia, revocación probada y evidencia |
| 3 | Clasificación de casos de uso | Los seis, por efecto sobre las personas |
| 4 | Controles proporcionales | Por nivel, con explicabilidad solo donde corresponde |
| 5 | Medición de sesgo | Con tres definiciones, la elegida y lo que sacrifica |
| 6 | Calibración de fraude | Umbral de menor costo total, con fricción incluida |
| 7 | Decisión sobre el registro distribuido | Seis preguntas, alternativa centralizada y conclusión |
| 8 | Perímetro regulatorio | Qué obligaciones activa la plataforma y con qué fundamento |

## Rúbrica

| Criterio | Puntos | Qué se valora |
|---|---:|---|
| Comparación con la alternativa | 20 | Especialmente en lo que se descarta |
| Controles proporcionales | 20 | Por efecto sobre las personas |
| Consentimiento por finalidad | 15 | Con revocación probada |
| Equidad medida y elegida | 15 | Con su sacrificio declarado |
| Costo total del fraude | 15 | Con la fricción cuantificada |
| Linaje desde el origen | 15 | Construido, no reconstruido |

**Total:** 100 puntos. **Aprobación:** 70.

## Restricciones

- **No** se usan datos reales de clientes en ninguna parte del proyecto.
- **No** se entrenan modelos con datos reales de personas.
- **No** se usan atributos protegidos ni variables que los sustituyan.
- **No** se toma ninguna decisión sobre personas reales.
- Toda adopción tecnológica va con su alternativa comparada y medida.

## Aviso

Material **docente**. La plataforma es un ejercicio de diseño con datos
sintéticos. **No constituye asesoría tecnológica ni legal**, y el perímetro
regulatorio de cada actividad debe verificarse en la norma vigente de la
jurisdicción correspondiente.
