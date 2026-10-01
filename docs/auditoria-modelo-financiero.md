# Auditoría de modelamiento financiero empresarial

**Fecha de corte:** 2026-10-01

**Alcance:** `README.md`, `SYLLABUS.md`, `STATUS.md`, `ROADMAP.md`, `modules/`,
laboratorios dentro de cada módulo, `apps/`, `sources/`, `scripts/`, `tests/` y
`.github/workflows/`.

## Objetivo y criterio

La auditoría verifica si el programa enseña a convertir supuestos empresariales
en una proyección financiera comprobable. No evalúa ni incorpora investigación
de mercado, mapas de empatía o Business Model Canvas: esas herramientas no son
necesarias para el objetivo financiero de este cambio.

La fuente de verdad de la estructura sigue siendo el repositorio: 356 clases en
23 partes, con las 11 secciones obligatorias validadas por
`tools/validate_program.py`. Los laboratorios están dentro de `modules/*/labs/`;
no existe un directorio raíz `labs/`. Los workflows están en
`.github/workflows/`.

## Matriz de cobertura

La profundidad describe la cobertura encontrada antes del refuerzo. La acción
indica qué se preservó o añadió sin crear una clase ni una aplicación nueva.

| Concepto | Clase/módulo actual | Profundidad | Brecha encontrada | Acción |
|---|---|---|---|---|
| Cost accounting / contabilidad de costos | Parte 5, clase 6; Parte 15, clase 4 | Media | Clasificaciones separadas y orientadas a contabilidad o banca | Parte 13, clase 3 conecta cuatro ejes con decisiones y proyección |
| Costos fijos | Parte 5, clase 6; Parte 7, clase 8 | Media | Sin puente único hacia equilibrio, EBITDA y caja | Integrados en clase 3, laboratorio 6 y app |
| Costos variables | Parte 5, clase 6; Parte 7, clase 8 | Media | Cobertura dispersa | Se convierten en costo unitario, contribución y capital de trabajo |
| Costos semifijos | Sin tratamiento explícito | Ausente | No se modelaban saltos de capacidad | Tramos explícitos en clase, caso y app |
| Costos directos e indirectos | Parte 15, clase 4 | Media | Enfoque de rentabilidad bancaria, no de modelo empresarial | Se separan de comportamiento y tratamiento contable |
| Costos hundidos | Parte 13, clase 6 y laboratorio 2 | Alta | Bien tratados en inversión, sin trazabilidad en la app general | El caso los muestra y excluye de la decisión futura |
| Costos incrementales | Parte 13, clase 6; Parte 7, clase 8 | Alta | No enlazados al presupuesto mensual | Se incorporan a OPEX, CAPEX y caja proyectada |
| CAPEX y OPEX | Conceptos presentes sin nomenclatura sistemática | Baja | No aparecían como capas reconciliadas del modelo | Clasificación, depreciación y salida de caja explícitas |
| Precio e ingreso unitario | Partes 5, 7 y casos digitales | Media | No alimentaban una cadena empresarial única | Son supuestos del caso y entradas del margen unitario |
| Margen de contribución | Parte 5, clase 6; Parte 7, clase 12 | Media | Aislado de adquisición, capacidad y capital | Alimenta equilibrio, LTV, EBITDA y escenarios |
| CAC | Sin cobertura empresarial identificable | Ausente | No se explicaba aplicabilidad | Se calcula solo con gasto atribuible y clientes nuevos |
| LTV de cliente | `LTV` existente significa loan-to-value en crédito | Ausente | Riesgo de confundir dos métricas homónimas | LTV de cliente se define por recurrencia; se declara cuándo no aplica |
| Payback | Parte 7, clase 10 | Alta para inversión | No había payback de adquisición | Se añade payback de CAC con condición de aplicabilidad |
| Punto de equilibrio | Partes 5, 7, 10 y 18 | Media | No incorporaba el salto semifijo del caso empresarial | Búsqueda del primer volumen que cubre el tramo correspondiente |
| Presupuesto empresarial | Parte 2 cubre presupuesto personal; Parte 15 planificación | Baja | Faltaba caso base empresarial aprobado | Clase 3 distingue presupuesto de forecast y preserva versiones |
| Forecast | Parte 6, enfoque macroeconómico | Baja para empresa | No había actualización del modelo desde nueva evidencia | Se define como actualización trazable del presupuesto |
| Estado de resultados | Parte 5, clase 11 y proyecto | Alta | Faltaba derivarlo desde clientes, precio y volumen en el mismo modelo | La app produce ingresos, EBITDA, depreciación y resultado operativo |
| Balance | Parte 5, clases 2, 9 y 10 | Alta | No era necesario duplicar teoría | Se preserva; el refuerzo se concentra en capital de trabajo y caja |
| Flujo de caja | Partes 2, 5, 9 y 13 | Alta | La conexión con unit economics estaba fragmentada | Se reconcilia EBITDA, capital de trabajo, CAPEX y caja mensual |
| Capital de trabajo | Parte 13, clases 3 y 4 | Alta | Bien cubierto; faltaba enlazarlo a adquisición y volumen | Días de cobro, inventario y pago entran al caso integrado |
| EBITDA | Partes 5, 8 y 9 | Media | Podía confundirse con caja | Se declara su alcance y se reconcilia con depreciación, NOF y CAPEX |
| Financiamiento | Partes 9, 13 y 16 | Alta | Monto a veces parte de la solicitud o del crédito, no del déficit del modelo | Se deriva del peor saldo más reserva mínima |
| Valoración | Partes 7 y 13 | Alta | Sin brecha relevante para este objetivo | Se preserva sin añadir teoría genérica |
| Sensibilidad | Parte 7, clase 12; Parte 13, clases 6 y 10 | Alta | No se exigía antes de escenarios multivariables | Laboratorio y app mueven primero solo el precio |
| Escenarios | Partes 7, 11, 13, 15, 16 y 23 | Alta | Amplios, pero no sobre un modelo empresarial pequeño común | Caso conservador, base y expansivo con causalidad explícita |
| Stress testing | Parte 11, clase 13; Parte 16, clase 15 | Alta | Es bancario y sistémico, no reemplaza sensibilidad del negocio | Se conserva y se diferencia del escenario conservador |
| Inversión inicial | Partes 7 y 13 | Media | No cerraba con capital de trabajo y reserva | Salida específica del resumen de capital |
| Déficit máximo acumulado | Implícito en proyecciones de caja | Baja | No era un output obligatorio | Se calcula desde el menor saldo mensual |
| Runway | Sin tratamiento explícito | Ausente | No se declaraba cuándo aplica | Meses completos antes de perforar la reserva; `no aplica` si no ocurre |
| Momento de break-even | Cobertura dispersa | Media | No había mes de equilibrio en el mismo modelo | Primer mes con EBITDA no negativo |
| Trazabilidad | Parte 16, clase 18 | Media | Principio narrativo, no contrato de datos en la herramienta | Capas `INPUT`, `ASSUMPTION`, `CALCULATION` y `OUTPUT` |

## Brecha principal encontrada

El programa ya tenía las piezas financieras y una cobertura fuerte de estados,
capital de trabajo, valoración, financiamiento y stress testing. La brecha no era
falta de teoría: era **integración**. Un alumno podía calcular cada componente,
pero no tenía un caso pequeño y ejecutable donde clientes, conversión, precio,
frecuencia, capacidad y costos alimentaran una sola cadena hasta resultado,
caja, escenarios y capital.

## Cambios aplicados

1. La Parte 13, clase 3 explicita clasificación de costos, unit economics,
   presupuesto/forecast, sensibilidad, escenarios, capital y trazabilidad.
2. El laboratorio 6 incorpora **Taller Circular**, caso sintético que se resuelve
   primero en papel o planilla y después se verifica por una segunda
   implementación.
3. El proyecto integrador exige mapa de supuestos, cuatro ejes de costos, estados
   y caja reconciliados, sensibilidad previa a escenarios y capital derivado.
4. `apps/financial_calculators` se amplía; no se crea otra app. El comando
   `business-model` ofrece texto o JSON y conserva las cuatro capas de
   trazabilidad.
5. Las pruebas comprueban clasificación, exclusión del costo hundido, fórmulas,
   aplicabilidad de métricas, punto de equilibrio, escenarios y capital.

## Cálculos utilizados

```text
clientes = clientes retenidos + oportunidades × conversión
unidades = clientes × frecuencia, limitadas por capacidad
ingresos = unidades × precio
margen unitario = precio − costo variable unitario
EBITDA = margen de contribución − OPEX fijo − OPEX semifijo
resultado operativo = EBITDA − depreciación del CAPEX
capital de trabajo = cuentas por cobrar + inventario − proveedores
caja final = caja anterior + EBITDA − variación de capital de trabajo − CAPEX
necesidad de financiamiento = reserva mínima − peor saldo, si es positiva
```

El punto de equilibrio no divide una sola vez cuando hay costos semifijos: busca
el primer volumen cuyo margen cubre el costo fijo y el tramo de capacidad que
ese mismo volumen activa.

## Compatibilidad y regeneración

No cambian el número ni los metadatos de las 356 clases, las 23 partes o las 11
secciones obligatorias. Tampoco se eliminan bibliografía, apps, portal, manual,
generadores, pruebas o workflows. Los documentos derivados se regeneran con las
herramientas existentes del repositorio; no se editan manualmente.

Los procedimientos de aceptación son exclusivamente los ya declarados en CI:
validadores de programa, render, syllabus, estado, índice, metadatos, fuentes,
contratos, datos, manual, glosario, enlaces, compilación y `pytest`.

### Evidencia ejecutada

| Verificación | Resultado |
|---|---|
| Estructura del programa | 23 partes, 356 clases, 152 laboratorios, 46 evaluaciones y 23 proyectos |
| Suite de aplicaciones | 323 pruebas superadas |
| Render y documentos derivados | Render sin pendientes; syllabus, estado, índice y glosario al día |
| Fuentes | 706 obras, 1 736 citas; registro válido |
| Enlaces internos | 773 archivos y 7 120 enlaces revisados, sin roturas |
| Contratos y datos | OpenAPI, ISO 20022 y nueve datasets válidos |
| Portal | 845 páginas generables con enlaces internos válidos |
| Manual | 384 entradas y 1 064 903 palabras generables |
| Compilación | `tools`, `apps` y `tests` compilan correctamente |

Se regeneraron `STATUS.md`, `FILE_INDEX.md` y
`docs/glosario-maestro.md` mediante sus herramientas canónicas. El portal y el
manual se verificaron con `--check`, tal como exige la CI, sin editar sus salidas
manualmente.
