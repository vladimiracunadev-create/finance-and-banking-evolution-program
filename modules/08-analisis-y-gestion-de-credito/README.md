# Parte 9: Análisis y gestión de crédito

Aquí empieza la Etapa 3 y con ella el banco por dentro. Las etapas anteriores
miraron el crédito desde quien lo pide; esta lo mira desde quien decide
otorgarlo, y con la responsabilidad que eso implica: cada decisión compromete
dinero de depositantes y queda registrada en un expediente que alguien va a
revisar.

La parte sigue el ciclo completo de una operación, del apetito de riesgo que fija
el directorio hasta la cobranza de lo que salió mal. Y su hallazgo central es de
secuencia: casi todo el daño de una cartera se origina en la admisión y se
manifiesta en la mora dieciocho meses después, cuando ya no hay nada que hacer.

El eje es que **una garantía no convierte un mal crédito en uno bueno**. Reduce la
pérdida si el crédito falla, que es distinto de reducir la probabilidad de que
falle, y confundir las dos cosas produce carteras problemáticas con excelentes
garantías.

## Con qué hay que llegar

| Parte | Qué aporta |
|---|---|
| 2 | Capacidad de pago y comportamiento del deudor |
| 5 | Estados financieros y calidad del resultado |
| 6 | Ciclo económico y su efecto sobre la mora |

## Qué se aprende

1. **Construir** un expediente donde cada afirmación tenga su documento y su verificación.
2. **Determinar** la renta admisible pasando el ingreso por sus tres filtros y ponderándolo por estabilidad.
3. **Calcular** capacidad de pago con prueba de estrés y deducir el monto máximo financiable.
4. **Valorar** una garantía a criterio de liquidación y traducirla en severidad esperada.
5. **Provisionar** una cartera por el modelo de tres etapas y evaluar la suficiencia del resultado.

## Cómo se encadenan las 16 clases

Las dieciséis clases siguen el ciclo de una operación de principio a fin.

La **clase 1** da el marco: las siete etapas, sus indicadores y las tres líneas de
defensa que reaparecen en las Partes 11 y 12.

Las **clases 2 y 3** construyen el expediente y cumplen la obligación de conocer al
cliente, que no viene del riesgo de crédito sino de la norma de prevención y
tiene consecuencias personales para quien la incumple.

Las **clases 4 a 7** evalúan al deudor por partes: cuánto gana y con qué certeza,
cuánto puede comprometer, cuánto debe ya —incluido lo que no aparece en ningún
informe— y cómo se ha comportado antes.

Las **clases 8 y 9** tratan las dos fuentes de pago. La primera es el flujo; la
garantía es la segunda y nunca la primera, y la clase 9 construye el flujo de una
empresa hasta encontrar su punto de quiebre.

Las **clases 10 a 13** automatizan y especializan: scoring para volumen, y después
consumo, hipotecario y pyme, cada uno con las variables que le corresponden.

Las **clases 14 y 15** miden lo ya otorgado y gestionan lo que falló, comparando
alternativas por su valor presente. La **clase 16** codifica las quince anteriores
en un motor que decide y explica por qué.

## Secuencia

1. [Ciclo de vida del crédito](classes/01-ciclo-de-vida-del-credito.md)
2. [Solicitud y expediente](classes/02-solicitud-y-expediente.md)
3. [Identificación y conocimiento del cliente](classes/03-identificacion-y-conocimiento-del-cliente.md)
4. [Ingresos y estabilidad](classes/04-ingresos-y-estabilidad.md)
5. [Capacidad de pago](classes/05-capacidad-de-pago.md)
6. [Nivel de endeudamiento](classes/06-nivel-de-endeudamiento.md)
7. [Historial crediticio](classes/07-historial-crediticio.md)
8. [Garantías](classes/08-garantias.md)
9. [Flujo de caja del deudor empresarial](classes/09-flujo-de-caja.md)
10. [Scoring](classes/10-scoring.md)
11. [Crédito de consumo](classes/11-credito-de-consumo.md)
12. [Crédito hipotecario](classes/12-credito-hipotecario.md)
13. [Crédito comercial y pyme](classes/13-credito-comercial-y-pyme.md)
14. [Provisiones e incumplimiento](classes/14-provisiones-e-incumplimiento.md)
15. [Cobranza y reestructuración](classes/15-cobranza-y-reestructuracion.md)
16. [Proyecto: motor de evaluación crediticia](classes/16-proyecto-motor-de-evaluacion-crediticia.md)

## Cómo se trabaja

Son **16 clases de 90 minutos** —24 horas de sesión— con **6 laboratorios**, **2 evaluaciones** y un proyecto integrador. Cada clase supone la anterior, así que el orden importa: saltarse una deja sin base a las que vienen después.

Los laboratorios se resuelven con datos propios o sintéticos y nunca con datos reales de terceros. Las evaluaciones son dos: una diagnóstica al empezar, que no se califica para aprobar sino para saber qué reforzar, y una final. El proyecto es el entregable que demuestra que la parte se entendió.

## Qué queda como evidencia

- Un expediente completo con sus verificaciones y sus excepciones justificadas.
- La renta admisible y la capacidad de pago con y sin estrés, de tres perfiles.
- La valoración de garantías a criterio de liquidación con su severidad.
- El motor de evaluación con su política codificada y sus casos de validación.
- La autoevaluación final con lo que quedó flojo.
