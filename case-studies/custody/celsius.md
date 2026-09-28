# Caso · Celsius: «custodia» no es lo mismo que préstamo

**Tema:** propiedad, rendimiento y liquidez · **Partes relacionadas:** 11, 20 y
22 · **Naturaleza:** caso real documentado · **Fecha de verificación:** 2026-09-28

Este caso obliga a leer el contrato junto con la interfaz. Alexander Mashinsky se
declaró culpable en diciembre de 2024 y fue sentenciado el 8 de mayo de 2025 a 12
años de prisión. Las acusaciones civiles se presentan como acusaciones; no se
confunden con la declaración de culpabilidad ni con la sentencia.

## Hechos

- Celsius ofrecía, entre otros servicios, un programa que recibía criptoactivos y
  pagaba rendimiento. Sus términos permitían prestar, vender, pignorar, invertir,
  usar o mezclar los activos transferidos.
- El DOJ documentó falsedades sobre seguridad, rentabilidad, sostenibilidad del
  rendimiento y riesgo; también documentó manipulación del token CEL.
- Celsius detuvo retiros el 12 de junio de 2022 y solicitó protección concursal el
  13 de julio de 2022.
- La sentencia penal acredita delitos concretos. La suspensión de retiros, por sí
  sola, solo demuestra indisponibilidad, no el tipo penal.

### Lectura financiera en once preguntas

| Pregunta | Respuesta documentada o límite |
|---|---|
| Producto o servicio | Préstamo/rendimiento sobre criptoactivos, además de otros servicios. |
| Qué entendía el cliente | La comunicación destacaba seguridad y rendimiento pasivo; el contrato transfería amplias facultades de uso. |
| Flujo económico | El cliente transfería activos; Celsius los desplegaba para generar retorno y pagaba recompensas. |
| Activos | Préstamos, inversiones, criptoactivos y posiciones con distinta liquidez y riesgo. |
| Pasivos | Obligaciones frente a clientes, cuya naturaleza dependía del contrato. |
| Control de fondos | Celsius controlaba y podía reutilizar activos bajo los términos citados por la SEC. |
| Riesgo | Crédito, contraparte, mercado, liquidez, concentración, conducta y fraude. |
| Qué ocurrió | La liquidez se deterioró, se detuvieron retiros y siguieron concurso y procesos de cumplimiento. |
| Qué está documentado | Declaración de culpabilidad, sentencia y hechos de la causa penal; la demanda SEC distingue alegaciones. |
| Controles pertinentes | Clasificación contractual visible, ALM por activo, límites de reutilización, trazabilidad del rendimiento y estrés de retiros. |
| Qué no permite concluir | Que todo producto de rendimiento sea custodia, que todo préstamo sea fraude o que toda pérdida sea apropiación. |

## Actores

Cliente, plataforma, prestatarios, contrapartes, dirección, consejo y supervisor
veían horizontes distintos. El cliente miraba un saldo disponible; tesorería debía
mirar cuándo regresaba cada activo y con qué probabilidad.

## Decisiones

La decisión inicial es clasificar: **custodia** conserva activo y mandato;
**préstamo** transfiere control y crea riesgo de crédito. Una interfaz no puede
borrar esa diferencia, y un contrato difícil de leer no corrige una comunicación
que induce una comprensión incompatible.

## Riesgos

La reutilización transforma un activo aparentemente disponible en exposición a
contraparte. El rendimiento alto puede venir de préstamo, apalancamiento, subsidio
comercial, emisión propia o una mezcla: cada fuente exige evidencia distinta.

## Regulación

La SEC demandó a Celsius y Mashinsky en 2023. Celsius consintió determinadas
medidas; la causa contra Mashinsky se describe en la fuente como acción civil. El
resultado penal posterior no convierte automáticamente cada alegación civil en un
hecho adjudicado.

## Controles

Preventivos: consentimiento específico para reutilización, límites por contraparte
y activo, vencimientos compatibles y prohibición de financiar recompensas con
compras no reveladas del token propio. Detectivos: atribución mensual del
rendimiento por fuente, conciliación de obligaciones, gap de liquidez diario y
comparación entre contrato, marketing y operación.

## Resultado y ejercicio sintético

```text
obligaciones con clientes                     800
activos líquidos libres                       150
préstamos cobrables a 30 días                  260
préstamos cobrables a más de 90 días           300
token propio y otros activos volátiles         190
retiro masivo supuesto en 7 días       35 % = 280
brecha inmediata                       280 − 150 = 130
```

Explica de dónde proviene un rendimiento sintético del 8 %: separa interés cobrado,
subsidio, apreciación y emisión propia. Repite el estrés con recuperación del 70 %
de préstamos y caída del 60 % del activo volátil.

## Lecciones

1. La etiqueta «cuenta» no determina propiedad, prelación ni liquidez.
2. El rendimiento debe reconciliarse con una fuente económica identificable.
3. Liquidez y solvencia son preguntas diferentes.
4. La comunicación al cliente es un control, no una pieza de marketing aislada.

## Preguntas

1. ¿Qué frase del contrato cambia la clasificación económica?
2. ¿Qué activos sirven para retiros hoy y cuáles solo sostienen solvencia esperada?
3. ¿Qué evidencia demostraría la procedencia del rendimiento?
4. ¿Cómo limitarías reutilización y concentración?
5. ¿Qué no puedes inferir de una suspensión de retiros?

## Fuentes

- U.S. Department of Justice (2025). *Founder of Celsius Sentenced to 12 Years
  for Fraud and Market Manipulation*.
  <https://www.justice.gov/usao-sdny/pr/founder-celsius-sentenced-12-years-fraud-and-market-manipulation>
- U.S. Securities and Exchange Commission (2023). *Celsius Network Limited and
  Alexander “Alex” Mashinsky*, Litigation Release No. 25779.
  <https://www.sec.gov/enforcement-litigation/litigation-releases/lr-25779>
- U.S. Securities and Exchange Commission (2023). *SEC v. Celsius Network Limited
  and Alexander Mashinsky, Complaint*.
  <https://www.sec.gov/files/litigation/complaints/2023/comp25779.pdf>
- Verificación local: se distinguen contrato, alegación civil, declaración de
  culpabilidad y sentencia. No constituye asesoría legal ni una estimación de
  recuperación concursal.
