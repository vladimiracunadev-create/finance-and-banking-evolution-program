# Documentación

Guías de referencia del programa. Todas complementan a las clases; ninguna las
sustituye. El número exacto de partes y clases está en
**[STATUS.md](../STATUS.md)**, que se genera contando los archivos.

---

## Para quien estudia

| Documento | Para qué sirve |
|---|---|
| 🗺️ **[Ruta de aprendizaje](ruta-aprendizaje.md)** | Por dónde entrar según tu perfil, cadenas de dependencia entre partes y método de estudio |
| 🎯 **[Mapa de competencias](mapa-competencias.md)** | Qué sabes hacer en cada nivel, con listas de verificación para autoevaluarte |
| 📖 **[Glosario](glosario.md)** | Definición operativa de los términos, con la parte donde se desarrollan |
| 🧮 **[Formulario](formulas.md)** | Las fórmulas del programa con su trampa habitual |
| 🌐 **[Etapa 5 — finanzas digitales](etapa-5-finanzas-digitales.md)** | Qué es y qué no es la etapa de infraestructura financiera digital, con sus seis criterios |
| 🔓 **[Mapa de finanzas abiertas](mapa-finanzas-abiertas.md)** | Dónde está cada concepto de la Parte 17 y qué se puede ejecutar |
| 🌍 **[Mapa de pagos transfronterizos](mapa-pagos-transfronterizos.md)** | Dónde está cada concepto de la Parte 18 y los siete errores que persigue |
| ⛓️ **[Mapa de blockchain y DLT](mapa-blockchain-dlt.md)** | Dónde está cada concepto de la Parte 19 y las cinco afirmaciones que desmonta |
| 🪙 **[Mapa de activos digitales](mapa-activos-digitales.md)** | Dónde está cada concepto de la Parte 20 y las seis afirmaciones que desmonta |
| 🏛️ **[Mapa de tokenización](mapa-tokenizacion.md)** | Dónde está cada concepto de la Parte 21 y las seis afirmaciones que desmonta |
| ⚖️ **[Mapa regulatorio](mapa-regulatorio.md)** | Dónde está cada concepto de la Parte 22 y las seis afirmaciones que desmonta |
| 🏗️ **[Mapa del capstone](mapa-capstone.md)** | La cadena de decisiones de la Parte 23 y las cinco afirmaciones que desmonta |
| 📘 **[Glosario de finanzas digitales](glosario-finanzas-digitales.md)** | Términos de la Etapa 5, cada uno con su «qué NO significa» |

## Para quien enseña

| Documento | Para qué sirve |
|---|---|
| 👩‍🏫 **[Guía docente](guia-docente.md)** | Sesión de 90 minutos, evaluación, rúbricas, adaptación al contexto y errores docentes |
| 🧪 **[Guía de laboratorios digitales](guia-laboratorios-digitales.md)** | Cómo son, cómo se ejecutan y cómo se corrigen los laboratorios de la Etapa 5 |

## Para todos

| Documento | Para qué sirve |
|---|---|
| 📗 **[Fuentes](fuentes.md)** | Bibliografía consolidada: manuales, marcos institucionales y artículos fundacionales |
| ⚖️ **[Ética y limitaciones](etica-y-limitaciones.md)** | Qué es y qué no es este material, uso de datos, modelos y contenidos sensibles |
| 🏛️ **[Verificación regulatoria](metodologia-verificacion-regulatoria.md)** | Cómo se cita una norma, cómo se comprueba su vigencia y qué hacer si no se puede |
| 🗂️ **[Fichas normativas](../regulatory/README.md)** | Índice legible por máquina de los instrumentos citados, con su fecha de verificación |

---

## Documentos del repositorio

| Documento | Contenido |
|---|---|
| [README](../README.md) | Presentación general y cómo empezar |
| [SYLLABUS](../SYLLABUS.md) | Índice completo de las clases, generado desde los archivos |
| [STATUS](../STATUS.md) | Estado real del contenido, generado automáticamente |
| [CONTRIBUTING](../CONTRIBUTING.md) | Cómo contribuir y qué se acepta |
| [CODE_OF_CONDUCT](../CODE_OF_CONDUCT.md) | Normas de convivencia del proyecto |
| [SECURITY](../SECURITY.md) | Cómo reportar un problema de seguridad |
| [CHANGELOG](../CHANGELOG.md) | Historial de versiones |
| [ROADMAP](../ROADMAP.md) | Qué sigue |
| [MANIFEST](../MANIFEST.md) | Ficha técnica de la entrega |
| [LICENSE](../LICENSE) | Licencia MIT |

---

## Cómo se mantiene esta documentación

Tres documentos se **generan automáticamente** desde los archivos del repositorio y no
deben editarse a mano:

| Documento | Generador | Verificación en CI |
|---|---|---|
| `SYLLABUS.md` | `tools/build_syllabus.py` | `--check` |
| `STATUS.md` | `tools/progress.py` | `--check` |
| Bloques generados de cada clase | `tools/render_program.py` | `--check` |
| Portal de estudio (`site/`) | `tools/build_site.py` | `--check` |

El resto se edita a mano y se valida con `tools/check_links.py`, que comprueba que
**todos** los enlaces relativos del repositorio resuelvan, y con `markdownlint`,
configurado en `.markdownlint-cli2.jsonc`.

```bash
python tools/build_syllabus.py && python tools/progress.py && python tools/check_links.py
```

## Validadores adicionales

| Validador | Qué comprueba |
|---|---|
| `tools/validate_program.py` | Estructura, secciones obligatorias y mínimo de fuentes |
| `tools/validate_metadata.py` | Que ninguna norma se cite sin fecha de verificación |
| `tools/validate_openapi.py` | Contratos de API: alcances, errores, importes y enumerados |
| `tools/validate_iso20022.py` | Mensajes de pago: campos, formatos y referencia estable |
| `tools/validate_datasets.py` | Que todo conjunto de datos tenga ficha y toda columna, diccionario |
| `tools/detect_secrets.py` | Que no haya credenciales reales versionadas |
| `tools/detect_pii.py` | Que no haya datos personales reales en datos ni portafolio |

```bash
python tools/validate_metadata.py && python tools/validate_openapi.py && python tools/validate_datasets.py
```

## El portal de estudio

El mismo material se publica como sitio navegable en
**[GitHub Pages](https://vladimiracunadev-create.github.io/finance-and-banking-evolution-program/)**.

El sitio **espeja la estructura del repositorio**: cada `X.md` produce un `X.html` en la
misma ruta relativa, de modo que cualquier enlace del material sigue funcionando dentro
del portal. Para generarlo en local:

```bash
pip install -r requirements-site.txt && python tools/build_site.py
```

---

**[⬅ Volver al inicio](../README.md)**
