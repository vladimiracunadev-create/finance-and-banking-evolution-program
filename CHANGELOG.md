# Historial de cambios

El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y el
versionado sigue [SemVer](https://semver.org/lang/es/).

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

[1.0.0]: https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/releases/tag/v1.0.0
[0.1.0]: https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/releases/tag/v0.1.0
