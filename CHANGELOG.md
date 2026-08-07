# Historial de cambios

El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y el
versionado sigue [SemVer](https://semver.org/lang/es/).

---

## [1.3.0] — 2026-08-06

Segunda parte de la **Etapa 5**: la infraestructura por la que un pago cruza una
frontera. Continúa desde la Parte 10 hacia la corresponsalía, la mensajería
ISO 20022, la liquidación y las arquitecturas que intentan sustituirla.

### Añadido

**Parte 18 — Pagos transfronterizos, remesas y liquidación internacional**

- 16 clases de 90 minutos, con el eje de que **un mensaje no es un movimiento de
  fondos**: la red transporta instrucciones, el dinero se mueve en cuentas, la
  liquidación ocurre en un sistema de pagos y la finalidad la da la norma.
- 8 laboratorios con solución de referencia comentada.
- Evaluación diagnóstica y final con guía de corrección y cálculos resueltos.
- Proyecto integrador «red de pagos transfronterizos» con seis corredores, cada
  uno diseñado para forzar una decisión distinta del motor de rutas.

**Aplicación `apps/cross_border_payments_lab/`**

- Los cuatro flujos modelados por separado, con husos, ventanas y calendarios.
- Motor de rutas con tres filtros y tres factores: un filtro de cumplimiento no
  se compensa con precio, y hay una prueba que lo demuestra.
- Construcción y validación de `pacs.008`, `pacs.002` y la máquina de estados
  que impide devolver antes de liquidar.
- Screening con precisión, exhaustividad y prueba retrospectiva.
- Liquidación con pago contra pago, incluidos los dos escenarios de fallo.
- Enlace de pagos inmediatos con resolución de alias y subasta de liquidez.
- Comparación honesta de la ruta con stablecoin, con el ahorro descompuesto por
  fuente.
- 56 pruebas, cada una asociada a una afirmación concreta de una clase.

**Herramientas**

- `tools/validate_iso20022.py`: campos obligatorios, formato de importe, divisa
  ISO, direcciones estructuradas, códigos de propósito y **referencia estable**
  entre reintentos. Es independiente del espacio de nombres del esquema, para
  que no deje de funcionar en la siguiente versión.

**Datos y metadatos**

- `datasets/synthetic/remittance_corridors.csv` (36 rutas, 9 corredores) y
  `sanctions_screening_alerts.csv` (12 000 alertas con resolución etiquetada),
  ambos con ficha, supuestos y **limitaciones explícitas**.
- Fichas normativas de la Recomendación 16 del GAFI y de la hoja de ruta del G20.

**Documentación**

- `docs/mapa-pagos-transfronterizos.md` y ampliación del glosario digital con
  los 12 términos de la parte.

### Cambiado

- La CI valida los mensajes ISO 20022 en cada cambio.
- `tools/build_file_index.py` usa `--cached --others --exclude-standard`: el
  índice ya no depende de si se generó antes o después de `git add`.
- `tools/build_site.py` descubre los adjuntos enlazados leyendo los enlaces
  reales, en lugar de una lista mantenida a mano.

### Corregido

- **Base del diferencial de cambio (Parte 18, clase 9).** El material medía el
  diferencial sobre la cotización inversa (28/950 = 2,947 %) cuando la pérdida
  del cliente es 1 − 950/978 = 2,863 %. Con la base equivocada, la composición
  del diferencial cruzado no cuadraba con el cálculo directo. La clase explica
  ahora la diferencia y el laboratorio la comprueba.
- **Descomposición del ahorro de la ruta con stablecoin.** Las partes no sumaban
  el ahorro total, lo que producía porcentajes sin sentido. Ahora suman, incluida
  una componente negativa que el análisis honesto no puede ocultar.
- `CHANGELOG.md`: 66 líneas con codificación corrompida en la entrada 1.1.0.

### Seguridad

- Las listas de sanciones y los nombres del laboratorio son sintéticos y se
  declara en cada salida. El módulo **no sirve para calibrar un sistema real**.
- El screening nunca descarta un caso por **falta** de información: lo escala.
  Descartar por ausencia de dato es el falso negativo que la Parte 18 persigue.

### Notas de migración

- Las Partes 1 a 17 no cambian.
- Quien tuviera un guion contra `tools/build_file_index.py` debe saber que ahora
  incluye los archivos sin rastrear que no están ignorados.

---

## [1.2.0] — 2026-08-06

Comienza la **Etapa 5 — Finanzas digitales, infraestructura y mercados
tokenizados**, que continúa el programa desde la introducción fintech de la
Parte 14 hacia la infraestructura financiera. Esta versión publica la primera de
sus siete partes.

> **Sobre la numeración.** La ampliación completa de la Etapa 5 se publicará como
> `2.0.0` cuando existan sus siete partes. Declarar `2.0.0` con una de siete
> contradiría el principio que sostiene el repositorio: `STATUS.md` describe lo
> que hay, no lo que se planea.

### Añadido

**Parte 17 — Finanzas abiertas, APIs y economía de datos**

- 14 clases de 90 minutos, con el eje de que las finanzas abiertas no son una
  API sino un régimen de consentimiento con soporte técnico.
- 6 laboratorios reproducibles, cada uno con escenario, supuestos, criterios de
  aceptación, amenazas, rúbrica y **solución de referencia comentada**.
- Evaluación diagnóstica y evaluación final con rúbrica, escala y guía de
  corrección con los cálculos resueltos.
- Proyecto integrador «agregador financiero regulado», con expediente de doce
  piezas y guion de defensa.

**Aplicación `apps/open_finance_sandbox/`**

- Entorno simulado completo: servidor de autorización con PKCE, API de cuentas,
  panel de consentimientos, iniciación de pagos y proveedor tercero.
- Contrato `openapi.json` validado en integración continua.
- 28 pruebas, en su mayoría **negativas**, y batería de conformidad de 16 casos
  en cuatro familias, con sus limitaciones declaradas.
- Modelo de amenazas priorizado por impacto × probabilidad, con la prueba que
  verifica cada control.

**Herramientas de validación**

- `tools/validate_metadata.py`: falla si una clase cita un instrumento normativo
  sin declarar su fecha de verificación.
- `tools/validate_openapi.py`: alcances declarados, respuestas de error,
  referencias resueltas, importes que no son coma flotante y enumerados con
  cláusula de compatibilidad.
- `tools/validate_datasets.py`: todo conjunto de datos con ficha, toda columna
  con diccionario.
- `tools/detect_secrets.py` y `tools/detect_pii.py`: credenciales reales y datos
  personales, distinguiendo el valor de ejemplo del secreto.

**Metadatos regulatorios**

- Directorio `regulatory/` con una ficha por instrumento: autoridad, número,
  fechas, estado, alcance, fuente oficial y `last_verified`.
- Encabezado YAML ampliado en las clases de la Etapa 5: `jurisdictions`,
  `regulatory_topics`, `regulation_last_verified`, `regulatory_status`,
  `primary_authorities` y `requires_legal_review`.

**Datos**

- `datasets/synthetic/open_finance_consents.csv`: 1 200 consentimientos con los
  patrones que las clases analizan (revocación temprana, fatiga).
- Separación `raw/`, `processed/`, `synthetic/`, `schemas/`.
- Ficha con diccionario, supuestos, calidad y límites para **los cuatro**
  conjuntos, incluidos los tres históricos que no la tenían.

**Documentación**

- `docs/etapa-5-finanzas-digitales.md`, `docs/mapa-finanzas-abiertas.md`,
  `docs/metodologia-verificacion-regulatoria.md`,
  `docs/guia-laboratorios-digitales.md` y
  `docs/glosario-finanzas-digitales.md`, este último con el campo «qué NO
  significa» en cada término.

### Cambiado

- `tools/progress.py` cuenta los componentes no curriculares sobre los archivos
  reales en lugar de declararlos a mano.
- `tools/build_syllabus.py` reconoce la Etapa 5 y calcula el número de proyectos
  y la clase final desde el contenido.
- `tools/build_site.py` deriva el número de partes y clases del repositorio: el
  pie del portal ya no puede quedar desactualizado.
- `datasets/README.md` documenta la organización y las cinco reglas de datos.

### Corregido

- `CHANGELOG.md` tenía 66 líneas con codificación corrompida (mojibake) en la
  entrada 1.1.0. Reparadas a UTF-8 correcto.
- Las cifras «240 clases» y «16 partes» escritas a mano en generadores y
  documentación quedaban desactualizadas al crecer el programa; ahora se
  calculan.

### Seguridad

- Las claves del entorno simulado son de juguete y están versionadas a
  propósito; `tools/detect_secrets.py` distingue ese caso del secreto real.
- Ningún dato personal, ningún fondo real, ninguna red externa y ninguna
  herramienta reutilizable de ataque: los ataques existen solo como pruebas que
  deben fallar.

### Notas de migración

- Las clases de las Partes 1 a 16 **no cambian**. El encabezado ampliado y las
  secciones adicionales solo se exigen a partir de la parte 17.
- La regla «toda cita de un instrumento lleva línea de verificación» sí se
  aplica a todo el repositorio; las 15 clases anteriores que citan instrumentos
  ya la cumplían.
- Quien tuviera un guion propio contra `tools/progress.py` debe saber que
  `PLANNED` incluye ahora las siete partes de la Etapa 5.

---

## [1.1.0] — 2026-08-06

Portal de estudio publicado y endurecimiento de la integración continua siguiendo las
convenciones del resto de los programas del autor.

### Añadido

**Portal de estudio**

- `tools/build_site.py` genera un sitio navegable con las 467 páginas del material:
  240 clases, documentación, laboratorios, evaluaciones y proyectos.
- El sitio espeja la estructura del repositorio (`X.md` → `X.html` en la misma ruta),
  de modo que cualquier enlace del material funciona dentro del portal.
- Diagramas mermaid renderizados, tema claro y oscuro, navegación por migas y diseño
  adaptable.
- Publicado en GitHub Pages y verificado tras el despliegue.

**Flujos de integración continua**

- `ci.yml` reemplaza a `validate.yml`: añade estilo de Markdown, matriz de
  compatibilidad (3 sistemas × 3 versiones de Python), auditoría de los propios
  workflows con `actionlint` y `zizmor`, y puerta de calidad final.
- `security.yml`: `pip-audit` sobre las dependencias, `bandit` sobre el código y
  escaneo de secretos con `gitleaks` sobre el historial completo.
- `codeql.yml`: análisis semántico del código Python.
- `pages.yml`: genera, publica y verifica el portal.
- `enlaces-externos.yml`: revisa semanalmente los enlaces a fuentes oficiales y abre
  un issue si alguno cae. Informativo: no bloquea la CI.
- `release.yml`: al etiquetar una versión publica el programa completo, las clases por
  separado, el SBOM en formato CycloneDX y las sumas de verificación.

**Configuración**

- `.markdownlint-cli2.jsonc` con las reglas de estilo y la razón de cada excepción.
- `.lycheeignore` con los dominios que bloquean agentes automáticos.
- `requirements-site.txt` con las dependencias del portal.

### Cambiado

- Acciones de terceros **fijadas por SHA de commit**, con su versión en comentario.
- `persist-credentials: false` en todos los checkout, para no dejar el token en `.git`.
- `timeout-minutes` en todos los jobs.
- Ninguna expresión `${{ }}` se interpola dentro de un `run`: los valores entran por
  `env` y el script los lee como variables de shell. Es la vía de inyección que señala
  `zizmor`, y el repositorio cierra su auditoría **sin un solo hallazgo**.
- La publicación usa `gh release`, ya incluido en el runner, en lugar de una acción de
  terceros: una dependencia externa menos que fijar, auditar y renovar.
- `pytest` sube a `>=9.0.3` para resolver la vulnerabilidad PYSEC-2026-1845.
- README con las insignias de los cuatro flujos y el enlace al portal.

### Corregido

- Seis errores de estilo de Markdown detectados por `markdownlint`: un nivel de
  encabezado saltado, tres tablas con celdas de más por barras verticales sin escapar,
  una almohadilla sin espacio interpretada como encabezado y un enlace vacío.

---

## [1.0.0] — 2026-08-06

Primera versión completa del programa: **las 240 clases redactadas, verificadas y con
bibliografía oficial**.

### Añadido

**Contenido — 240 clases en 16 partes**

- Partes 1–4 · *Fundamentos* (56 clases): matemática financiera, finanzas personales,
  productos y servicios, seguridad y consumo financiero.
- Partes 5–8 · *Analista* (60 clases): contabilidad, economía y sistema financiero,
  matemática financiera avanzada, inversiones y mercados.
- Partes 9–12 · *Bancario* (64 clases): crédito, operaciones, gestión integral de
  riesgos, regulación y cumplimiento.
- Partes 13–16 · *Dirección* (60 clases): finanzas corporativas, fintech y datos,
  estrategia y dirección, y el proyecto integrador «Banco Virtual».

**Estructura pedagógica**

- Trece secciones por clase, incluidas ejemplo numérico guiado paso a paso, puente
  «del cliente al banco», errores frecuentes con causa y corrección, preguntas de
  comprobación y entregable de portafolio.
- Mínimo de cuatro fuentes verificables por clase, con línea de verificación local en
  todo contenido normativo.
- 96 laboratorios, 32 evaluaciones y 16 proyectos integradores.

**Herramientas de verificación**

- `tools/validate_program.py` — estructura, secciones obligatorias y fuentes.
- `tools/render_program.py` — genera navegación, agenda docente y bloque de ética,
  con modo `--check` idempotente.
- `tools/build_syllabus.py` — genera `SYLLABUS.md` con el índice de las 240 clases.
- `tools/progress.py` — genera `STATUS.md` desde los archivos reales.
- `tools/check_links.py` — verifica los ~2 000 enlaces relativos del repositorio.

**Documentación**

- `README.md` reescrito con navegación, insignias, diagramas y anatomía de una clase.
- `docs/fuentes.md` — bibliografía consolidada de manuales, marcos institucionales y
  artículos fundacionales.
- `docs/glosario.md` — definiciones operativas indexadas por parte.
- `docs/formulas.md` — formulario por dominio, con la trampa habitual de cada fórmula.
- `docs/guia-docente.md` — sesión de 90 minutos, rúbricas y adaptación por contexto.
- `docs/ruta-aprendizaje.md` — progresión, puntos de entrada y cadenas de dependencia.
- `docs/mapa-competencias.md` — competencias por nivel con listas de autoevaluación.
- `docs/etica-y-limitaciones.md` — alcance, uso de datos, modelos y contenidos sensibles.
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` y `SECURITY.md` ampliados.

**Integración continua**

- Flujo `Validate program` con trabajos de validación, enlaces y calidad de Markdown.
- Permisos mínimos, control de concurrencia y caché de dependencias.

### Cambiado

- `SYLLABUS.md` pasa de ser una tabla escrita a mano a un índice generado desde los
  archivos: incluye las 240 clases con su nivel y su enlace.
- `STATUS.md` se genera desde los archivos y nunca declara más contenido del que existe.
- Nombres de archivo normalizados a ASCII para compatibilidad entre sistemas y URL.
- Finales de línea unificados a LF mediante `.gitattributes`.

---

## [0.1.0] — 2026-08-05

Versión inicial: estructura del programa y herramientas base.

### Añadido

- Arquitectura curricular de 16 partes y 240 clases.
- 96 laboratorios y 32 evaluaciones estructurados.
- Calculadoras financieras con interfaz de línea de comandos.
- Modelo de scoring crediticio con métricas.
- Banco virtual sobre SQLite.
- Conjuntos de datos sintéticos.
- Validación estructural inicial.

---

[1.1.0]: https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/releases/tag/v1.1.0
[1.0.0]: https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/releases/tag/v1.0.0
[0.1.0]: https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/releases/tag/v0.1.0
