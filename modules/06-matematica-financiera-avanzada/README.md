# Parte 7: Matemática financiera avanzada

La Parte 1 usó una sola tasa por periodo y funcionó porque todos los ejemplos
estaban alineados. Esta parte levanta ese supuesto y trata el caso real: tasas
con frecuencias distintas, flujos que no coinciden con los periodos y decisiones
de inversión donde lo difícil no es el cálculo sino decidir qué entra en él.

Es la parte que más se usa después. Las herramientas de aquí aparecen en la
valoración de la Parte 8, en el análisis de proyectos de la 13 y en la medición
de riesgo de tasa de la 11, y por eso conviene hacerla despacio.

El eje es que **una cifra financiera vale lo que valen sus supuestos**. De ahí que
la parte dedique tres clases enteras —sensibilidad, escenarios y modelamiento— a
medir de qué depende el resultado y a construirlo para que otro lo pueda
auditar.

## Con qué hay que llegar

| Parte | Qué aporta |
|---|---|
| 1 | Interés, valor presente, cuotas y amortización |
| 6 | Tasas de mercado y expectativas |

## Qué se aprende

1. **Convertir** entre tasas de cualquier periodicidad sin caer en la proporcionalidad, que solo vale en interés simple.
2. **Valorar** anualidades vencidas, anticipadas, diferidas y perpetuas, y reconocer cuál corresponde leyendo un contrato.
3. **Decidir** sobre un proyecto con el flujo incremental correcto y una tasa justificada por escrito.
4. **Medir** la sensibilidad de una valoración a un cambio de tasas con duración y convexidad.
5. **Construir** un modelo con capas separadas, controles automáticos y casos de prueba.

## Cómo se encadenan las 15 clases

Las quince clases van de la tasa al modelo, en cuatro bloques.

Las **clases 1 a 3** resuelven el problema de las tasas: nominal frente a efectiva,
equivalencia entre periodicidades y qué hacer cuando la tasa y el flujo no están
alineados. Es donde vive el error silencioso de toda la parte.

Las **clases 4 a 7** valoran series de flujos, de la anualidad simple a la
perpetuidad que sostiene el valor terminal de cualquier valoración de empresa.

Las **clases 8 a 10** deciden sobre proyectos. El valor actual neto es aritmética
conocida; lo nuevo es el criterio de qué flujos entran, y la clase 9 delimita los
tres problemas de la tasa interna de retorno que hacen que ordene mal.

Las **clases 11 a 14** miden lo que puede salir distinto: sensibilidad al cambio de
tasas, a los supuestos, y a varios supuestos correlacionados a la vez. La 14
decide con qué herramienta se construye para que sea auditable. La **clase 15**
reúne todo en un motor que produce un informe defendible ante un comité.

## Secuencia

1. [Tasas nominales y efectivas](classes/01-tasas-nominales-y-efectivas.md)
2. [Tasas equivalentes](classes/02-tasas-equivalentes.md)
3. [Conversión de periodicidades](classes/03-conversion-de-periodicidades.md)
4. [Anualidades vencidas](classes/04-anualidades-vencidas.md)
5. [Anualidades anticipadas](classes/05-anualidades-anticipadas.md)
6. [Perpetuidades](classes/06-perpetuidades.md)
7. [Sistemas de amortización](classes/07-sistemas-de-amortizacion.md)
8. [Valor actual neto](classes/08-valor-actual-neto.md)
9. [Tasa interna de retorno](classes/09-tasa-interna-de-retorno.md)
10. [Payback y rentabilidad](classes/10-payback-y-rentabilidad.md)
11. [Duración y convexidad](classes/11-duracion-y-convexidad.md)
12. [Sensibilidad](classes/12-sensibilidad.md)
13. [Escenarios y simulación](classes/13-escenarios-y-simulacion.md)
14. [Modelamiento con Excel y Python](classes/14-modelamiento-con-excel-y-python.md)
15. [Proyecto: motor de valoración](classes/15-proyecto-motor-de-valoracion.md)

## Cómo se trabaja

Son **15 clases de 90 minutos** —22,5 horas de sesión— con **6 laboratorios**, **2 evaluaciones** y un proyecto integrador. Cada clase supone la anterior, así que el orden importa: saltarse una deja sin base a las que vienen después.

Los laboratorios se resuelven con datos propios o sintéticos y nunca con datos reales de terceros. Las evaluaciones son dos: una diagnóstica al empezar, que no se califica para aprobar sino para saber qué reforzar, y una final. El proyecto es el entregable que demuestra que la parte se entendió.

## Qué queda como evidencia

- Las conversiones de tasas con la verificación por un segundo camino.
- Los cuatro despejes de la anualidad resueltos y cerrados sobre sí mismos.
- El flujo incremental de un proyecto con sus exclusiones justificadas.
- El motor de valoración con sus casos de validación y sus límites declarados.
- La autoevaluación final con lo que quedó flojo.
