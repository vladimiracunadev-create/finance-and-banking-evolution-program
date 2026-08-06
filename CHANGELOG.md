# Historial de cambios

El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y el
versionado sigue [SemVer](https://semver.org/lang/es/).

---

## [1.1.0] â€” 2026-08-06

Portal de estudio publicado y endurecimiento de la integraciÃ³n continua siguiendo las
convenciones del resto de los programas del autor.

### AÃ±adido

**Portal de estudio**

- `tools/build_site.py` genera un sitio navegable con las 467 pÃ¡ginas del material:
  240 clases, documentaciÃ³n, laboratorios, evaluaciones y proyectos.
- El sitio espeja la estructura del repositorio (`X.md` â†’ `X.html` en la misma ruta),
  de modo que cualquier enlace del material funciona dentro del portal.
- Diagramas mermaid renderizados, tema claro y oscuro, navegaciÃ³n por migas y diseÃ±o
  adaptable.
- Publicado en GitHub Pages y verificado tras el despliegue.

**Flujos de integraciÃ³n continua**

- `ci.yml` reemplaza a `validate.yml`: aÃ±ade estilo de Markdown, matriz de
  compatibilidad (3 sistemas Ã— 3 versiones de Python), auditorÃ­a de los propios
  workflows con `actionlint` y `zizmor`, y puerta de calidad final.
- `security.yml`: `pip-audit` sobre las dependencias, `bandit` sobre el cÃ³digo y
  escaneo de secretos con `gitleaks` sobre el historial completo.
- `codeql.yml`: anÃ¡lisis semÃ¡ntico del cÃ³digo Python.
- `pages.yml`: genera, publica y verifica el portal.
- `enlaces-externos.yml`: revisa semanalmente los enlaces a fuentes oficiales y abre
  un issue si alguno cae. Informativo: no bloquea la CI.
- `release.yml`: al etiquetar una versiÃ³n publica el programa completo, las clases por
  separado, el SBOM en formato CycloneDX y las sumas de verificaciÃ³n.

**ConfiguraciÃ³n**

- `.markdownlint-cli2.jsonc` con las reglas de estilo y la razÃ³n de cada excepciÃ³n.
- `.lycheeignore` con los dominios que bloquean agentes automÃ¡ticos.
- `requirements-site.txt` con las dependencias del portal.

### Cambiado

- Acciones de terceros **fijadas por SHA de commit**, con su versiÃ³n en comentario.
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
  encabezado saltado, tres tablas con celdas de mÃ¡s por barras verticales sin escapar,
  una almohadilla sin espacio interpretada como encabezado y un enlace vacÃ­o.

---

## [1.0.0] â€” 2026-08-06

Primera versiÃ³n completa del programa: **las 240 clases redactadas, verificadas y con
bibliografÃ­a oficial**.

### AÃ±adido

**Contenido â€” 240 clases en 16 partes**

- Partes 1â€“4 Â· *Fundamentos* (56 clases): matemÃ¡tica financiera, finanzas personales,
  productos y servicios, seguridad y consumo financiero.
- Partes 5â€“8 Â· *Analista* (60 clases): contabilidad, economÃ­a y sistema financiero,
  matemÃ¡tica financiera avanzada, inversiones y mercados.
- Partes 9â€“12 Â· *Bancario* (64 clases): crÃ©dito, operaciones, gestiÃ³n integral de
  riesgos, regulaciÃ³n y cumplimiento.
- Partes 13â€“16 Â· *DirecciÃ³n* (60 clases): finanzas corporativas, fintech y datos,
  estrategia y direcciÃ³n, y el proyecto integrador Â«Banco VirtualÂ».

**Estructura pedagÃ³gica**

- Trece secciones por clase, incluidas ejemplo numÃ©rico guiado paso a paso, puente
  Â«del cliente al bancoÂ», errores frecuentes con causa y correcciÃ³n, preguntas de
  comprobaciÃ³n y entregable de portafolio.
- MÃ­nimo de cuatro fuentes verificables por clase, con lÃ­nea de verificaciÃ³n local en
  todo contenido normativo.
- 96 laboratorios, 32 evaluaciones y 16 proyectos integradores.

**Herramientas de verificaciÃ³n**

- `tools/validate_program.py` â€” estructura, secciones obligatorias y fuentes.
- `tools/render_program.py` â€” genera navegaciÃ³n, agenda docente y bloque de Ã©tica,
  con modo `--check` idempotente.
- `tools/build_syllabus.py` â€” genera `SYLLABUS.md` con el Ã­ndice de las 240 clases.
- `tools/progress.py` â€” genera `STATUS.md` desde los archivos reales.
- `tools/check_links.py` â€” verifica los ~2 000 enlaces relativos del repositorio.

**DocumentaciÃ³n**

- `README.md` reescrito con navegaciÃ³n, insignias, diagramas y anatomÃ­a de una clase.
- `docs/fuentes.md` â€” bibliografÃ­a consolidada de manuales, marcos institucionales y
  artÃ­culos fundacionales.
- `docs/glosario.md` â€” definiciones operativas indexadas por parte.
- `docs/formulas.md` â€” formulario por dominio, con la trampa habitual de cada fÃ³rmula.
- `docs/guia-docente.md` â€” sesiÃ³n de 90 minutos, rÃºbricas y adaptaciÃ³n por contexto.
- `docs/ruta-aprendizaje.md` â€” progresiÃ³n, puntos de entrada y cadenas de dependencia.
- `docs/mapa-competencias.md` â€” competencias por nivel con listas de autoevaluaciÃ³n.
- `docs/etica-y-limitaciones.md` â€” alcance, uso de datos, modelos y contenidos sensibles.
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` y `SECURITY.md` ampliados.

**IntegraciÃ³n continua**

- Flujo `Validate program` con trabajos de validaciÃ³n, enlaces y calidad de Markdown.
- Permisos mÃ­nimos, control de concurrencia y cachÃ© de dependencias.

### Cambiado

- `SYLLABUS.md` pasa de ser una tabla escrita a mano a un Ã­ndice generado desde los
  archivos: incluye las 240 clases con su nivel y su enlace.
- `STATUS.md` se genera desde los archivos y nunca declara mÃ¡s contenido del que existe.
- Nombres de archivo normalizados a ASCII para compatibilidad entre sistemas y URL.
- Finales de lÃ­nea unificados a LF mediante `.gitattributes`.

---

## [0.1.0] â€” 2026-08-05

VersiÃ³n inicial: estructura del programa y herramientas base.

### AÃ±adido

- Arquitectura curricular de 16 partes y 240 clases.
- 96 laboratorios y 32 evaluaciones estructurados.
- Calculadoras financieras con interfaz de lÃ­nea de comandos.
- Modelo de scoring crediticio con mÃ©tricas.
- Banco virtual sobre SQLite.
- Conjuntos de datos sintÃ©ticos.
- ValidaciÃ³n estructural inicial.

---

[1.1.0]: https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/releases/tag/v1.1.0
[1.0.0]: https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/releases/tag/v1.0.0
[0.1.0]: https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/releases/tag/v0.1.0
