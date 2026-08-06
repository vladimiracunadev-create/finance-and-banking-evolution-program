# Documentación

Guías de referencia del programa. Todas complementan a las 240 clases; ninguna las
sustituye.

---

## Para quien estudia

| Documento | Para qué sirve |
|---|---|
| 🗺️ **[Ruta de aprendizaje](ruta-aprendizaje.md)** | Por dónde entrar según tu perfil, cadenas de dependencia entre partes y método de estudio |
| 🎯 **[Mapa de competencias](mapa-competencias.md)** | Qué sabes hacer en cada nivel, con listas de verificación para autoevaluarte |
| 📖 **[Glosario](glosario.md)** | Definición operativa de los términos, con la parte donde se desarrollan |
| 🧮 **[Formulario](formulas.md)** | Las fórmulas del programa con su trampa habitual |

## Para quien enseña

| Documento | Para qué sirve |
|---|---|
| 👩‍🏫 **[Guía docente](guia-docente.md)** | Sesión de 90 minutos, evaluación, rúbricas, adaptación al contexto y errores docentes |

## Para todos

| Documento | Para qué sirve |
|---|---|
| 📗 **[Fuentes](fuentes.md)** | Bibliografía consolidada: manuales, marcos institucionales y artículos fundacionales |
| ⚖️ **[Ética y limitaciones](etica-y-limitaciones.md)** | Qué es y qué no es este material, uso de datos, modelos y contenidos sensibles |

---

## Documentos del repositorio

| Documento | Contenido |
|---|---|
| [README](../README.md) | Presentación general y cómo empezar |
| [SYLLABUS](../SYLLABUS.md) | Índice completo de las 240 clases, generado desde los archivos |
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

El resto se edita a mano y se valida con `tools/check_links.py`, que comprueba que los
~2 000 enlaces relativos del repositorio resuelvan.

```bash
python tools/build_syllabus.py && python tools/progress.py && python tools/check_links.py
```

---

**[⬅ Volver al inicio](../README.md)**
