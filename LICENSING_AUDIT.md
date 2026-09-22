# Auditoría de propiedad intelectual y licencias

**Repositorio:** `vladimiracunadev-create/finance-and-banking-evolution-program`<br>
**Corte:** 22 de septiembre de 2026<br>
**Alcance:** 931 archivos versionados y 105 commits visibles en el historial Git local

## Estado previo

El repositorio aplicaba un único texto MIT a «Finance & Banking Evolution
Program contributors». El README, `MANIFEST.md`, las fichas de datasets, el
contrato OpenAPI y los generadores del portal y del manual presentaban MIT como
régimen global. Esa formulación mezclaba software, contenido educativo, datos,
fuentes normativas, referencias de terceros y marca.

## Evidencia de autoría y contributors

`git shortlog -sne HEAD` atribuye 102 commits a `Vladimir Acuña` y 3 a
`vladimiracunadev-create`; ambas identidades usan el mismo correo. No aparece
otro autor de commits. El primer commit local es `a1abf69` (2026-08-05) y el
último anterior a la auditoría es `0fec136` (2026-09-07). Esta evidencia permite
normalizar el aviso de los archivos originales como:

> Copyright © 2026 Vladimir Acuña<br>
> GitHub: vladimiracunadev-create

Git acredita quién confirmó archivos, pero no prueba por sí solo identidad civil,
cesiones laborales o contractuales, ni originalidad absoluta. No se encontraron
contributors externos en el historial local. Si existen aportes recibidos fuera
de Git, deben identificarse antes de afirmar titularidad exclusiva sobre ellos.

## Inventario y resultado

| Categoría auditada | Hallazgo | Régimen desde 2026-09-22 |
|---|---|---|
| Código, tests, herramientas y simuladores | Implementación original; sin encabezados de licencia incompatibles hallados | MIT |
| Clases, ejercicios, soluciones, evaluaciones y casos | Redacción educativa original declarada, apoyada en bibliografía enlazada | CC BY-NC-SA 4.0 sobre la expresión original |
| Metodología, rutas y matrices | Estructura pedagógica propia expresada en documentos y generadores | CC BY-NC-SA 4.0 sobre su expresión protegible |
| Fórmulas | Fórmulas financieras y matemáticas de uso general; la selección y explicación sí contienen redacción original | Fórmula o hecho fuera de la concesión cuando no sea protegible; explicación original CC BY-NC-SA 4.0 |
| Gráficos | Diagramas Mermaid y esquemas textuales propios; no se hallaron imágenes de terceros versionadas | CC BY-NC-SA 4.0, salvo aviso individual |
| Datasets | CSV declarados sintéticos; `datasets/raw/` vacío; fichas con origen y fecha | Régimen por fuente en `DATA_LICENSES.md` |
| Fixtures de aplicaciones | JSON sintético ligado al funcionamiento técnico | MIT |
| Fuentes financieras y bibliografía | Referencias, ISBN, DOI y enlaces; no son obras relicenciadas | Régimen de autores y editoriales |
| Normativa y documentos oficiales | Fichas resumen enlazan fuentes oficiales de Chile, UE, El Salvador y organismos internacionales | Régimen jurídico de la fuente; redacción original de fichas bajo CC BY-NC-SA 4.0 |
| Nombre y signos | No existía política separada | Reserva y reglas de uso en `TRADEMARKS.md` |

## Cambios realizados

- `LICENSE`: MIT acotada a software, con autoría normalizada.
- `LICENSE-CONTENT.md`: CC BY-NC-SA 4.0 para contenido y metodología originales.
- `DATA_LICENSES.md`: matriz por origen y regla de incorporación futura.
- `THIRD_PARTY_NOTICES.md`: fuentes, estándares, regulación y límites de la concesión.
- `TRADEMARKS.md`: uso nominativo y ausencia de licencia de marca.
- `DISCLAIMER.md`: finalidad educativa, ausencia de asesorías y garantías, y cambio regulatorio.
- `docs/LICENSING_HISTORY.md`: preservación explícita de MIT histórico y fecha de transición.
- README y documentación: tabla de regímenes y aviso visible.
- Fichas y generadores: eliminación de declaraciones MIT globales.

## Riesgos pendientes

1. **MIT histórico amplio.** Las copias ya distribuidas bajo MIT conservan esa
   licencia; el nuevo régimen no puede retirar permisos concedidos.
2. **Originalidad a escala.** La revisión estructural y bibliográfica no equivale
   a una comparación forense de similitud de las 356 clases contra cada obra.
3. **Fuentes oficiales.** Que un documento sea oficial o accesible no implica
   automáticamente dominio público o libre redistribución en toda jurisdicción.
4. **Estándares y marcas.** ISO, IFRS y otros organismos pueden imponer términos
   sobre textos, esquemas y signos; el repositorio debe seguir enlazando en vez
   de copiar salvo permiso confirmado.
5. **Contribuciones futuras.** `CONTRIBUTING.md` todavía debe respaldarse con una
   declaración expresa de procedencia y derecho suficiente en cada propuesta;
   para aportes relevantes conviene un DCO o CLA revisado jurídicamente.
6. **Marca.** `TRADEMARKS.md` no reemplaza búsqueda de disponibilidad ni registro.
7. **Asesoría profesional.** Esta auditoría técnica organiza evidencia y avisos;
   una revisión jurídica local sigue siendo necesaria antes de licenciar usos
   comerciales, registrar marca o integrar material con condiciones dudosas.

## Recomendaciones

- Exigir en toda contribución identificación del autor, procedencia y aceptación
  del régimen aplicable; conservar evidencia de consentimiento.
- Añadir una entrada a `DATA_LICENSES.md` y `THIRD_PARTY_NOTICES.md` antes de
  incorporar cualquier dataset, gráfico, captura o texto externo.
- Crear una etiqueta o release posterior al commit de transición para fijar una
  frontera verificable; no reescribir etiquetas históricas.
- Revisar periódicamente enlaces regulatorios, condiciones de organismos y
  posibles cambios en la regulación citada.
- Obtener revisión de abogado competente para el país y los usos comerciales
  previstos, en especial sobre la cadena de titularidad y la marca.

## Método y límites

Se inspeccionaron el árbol Git, autores y correos del historial, etiquetas,
licencia previa, documentación principal, clases y generadores, datasets y sus
fichas, fórmulas, regulación estructurada, bibliografía, CI, contrato OpenAPI y
referencias textuales a MIT/copyright/licencia. Se validaron las rutas internas
y las puertas de calidad disponibles. No se descargaron ni reprodujeron obras
citadas, y no se presume permiso por su disponibilidad en internet.
