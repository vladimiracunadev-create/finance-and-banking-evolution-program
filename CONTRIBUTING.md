<!-- portada:inicio -->
<div align="center">

# 🤝 Contribuir

**Cómo proponer una corrección, una fuente o una traducción, y qué tiene que pasar antes de abrirla.**

[![tipo](https://img.shields.io/badge/tipo-gu%C3%ADa%20de%20contribuci%C3%B3n-7c5cff?style=flat-square)](CONTRIBUTING.md)
[![validación](https://img.shields.io/badge/validaci%C3%B3n-15%20comprobaciones-2e8b57?style=flat-square)](README.md#-calidad-y-ci)

[🏠 Inicio](README.md) ·
[📚 Documentación](docs/README.md) ·
[🗺️ Roadmap](ROADMAP.md) ·
[🤗 Código de conducta](CODE_OF_CONDUCT.md) ·
[🔐 Seguridad](SECURITY.md)

</div>
<!-- portada:fin -->

---

Gracias por el interés. Este programa mejora con correcciones de contenido, fuentes
adicionales, adaptaciones por país y traducciones.

> Antes de contribuir, lee **[docs/etica-y-limitaciones.md](docs/etica-y-limitaciones.md)**.
> Define qué es este material y qué obligaciones asume quien lo edita.

---

## ✅ Qué se acepta

| ✅ Bienvenido | ❌ No se acepta |
|---|---|
| Corrección de un error de contenido, con la fuente correcta | Contenido sin fuente verificable |
| Fuente adicional consultable para una clase existente | Blogs, resúmenes o material sin autoría |
| Actualización de un enlace roto o de una norma superada | Datos reales de personas, aun anonimizados |
| Adaptación normativa por país, en su propia sección | Presentar una norma nacional como universal |
| Traducción de una parte completa | Traducciones parciales de clases sueltas |
| Mejora de las herramientas, con pruebas | Cambios que rompan la validación |
| Corrección de un cálculo, con verificación | Cálculos sin su verificación de escala |
| Casos y datos **sintéticos** adicionales | Capturas o datos de sistemas productivos |

---

## 🤝 Antes de abrir una propuesta

```bash
python tools/validate_program.py
python tools/render_program.py --check
python tools/build_syllabus.py --check
python tools/progress.py --check
python tools/build_file_index.py --check
python tools/validate_metadata.py
python scripts/verify_sources.py
python tools/validate_openapi.py
python tools/validate_datasets.py
python tools/detect_secrets.py
python tools/detect_pii.py
python tools/check_links.py
pytest -q
npx markdownlint-cli2
```

Los catorce deben pasar. Es lo mismo que verifica la integración continua.

Si tocas el portal de estudio, verifica además que se genere:

```bash
pip install -r requirements-site.txt && python tools/build_site.py --check
```

Si tu cambio afecta a una clase, ejecuta el renderizador antes de confirmar:

```bash
python tools/render_program.py
```

Y si añades o quitas clases:

```bash
python tools/build_syllabus.py && python tools/progress.py
```

---

## 🧩 Convención de una clase

La validación exige que **toda clase** contenga estas once secciones:

```text
## 🎯 Propósito
## 📚 Objetivos
## ⚙️ Agenda de 90 minutos          ← generada por render_program.py
## 🧩 Conceptos centrales
## 📖 Desarrollo
## 🧮 Ejemplo guiado
## 🏦 Del cliente al banco
## ⚠️ Errores frecuentes
## ❓ Preguntas de comprobación
## 📥 Entregable
## 📗 Fuentes y verificación
```

Además:

| Requisito | Verificado por |
|---|---|
| Encabezado YAML con `part`, `class`, `title`, `level`, `duration_minutes`, `status` | `validate_program.py` |
| Nombre de archivo en ASCII, numerado y correlativo | `validate_program.py` |
| Bloques generados presentes (`gen:header`, `gen:agenda`, `gen:etica`, `gen:footer`) | `validate_program.py` |
| **Al menos cuatro fuentes** en `📗 Fuentes y verificación` | `validate_program.py` |
| **Cada fuente declara el uso** que esa clase hace de ella | `verify_sources.py` |
| Toda obra citada tiene entrada en `sources/bibliography.json` | `verify_sources.py` |
| Enlaces relativos que resuelvan | `check_links.py` |
| Línea de verificación si la clase cita un instrumento normativo | `validate_metadata.py` |

### Adicional para la Etapa 5 (parte ≥ 17)

Las clases de finanzas digitales llevan además un encabezado regulatorio y cinco
secciones más. `validate_metadata.py` las exige:

| Requisito | Detalle |
|---|---|
| Encabezado regulatorio | `jurisdictions`, `regulatory_topics`, `regulation_last_verified`, `regulatory_status`, `primary_authorities`, `requires_legal_review` |
| Secciones adicionales | `🧠 Modelo mental`, `🧭 Perspectivas`, `⚖️ Riesgos y controles`, `🧪 Práctica`, `🔗 Referencias cruzadas` |
| Fecha de verificación | ISO 8601 y **no futura** |
| Aviso legal | Si `requires_legal_review: true`, la clase declara que no constituye asesoría legal |

Usa listas en línea (`[global, chile]`) en el encabezado: el renderizador reconstruye
el YAML clave a clave y una lista multilínea se perdería.

### Secciones recomendadas

`🧠 Modelo mental` y `🧪 Práctica` no son obligatorias en las Partes 1 a 16, y todas
las clases del programa las incluyen porque sostienen su estructura pedagógica.

### Lo que no se edita a mano

Los bloques entre `<!-- gen:*:start -->` y `<!-- gen:*:end -->` los genera
`tools/render_program.py`. Si los editas, el siguiente renderizado los sobrescribirá.

---

## ✍️ Estilo del contenido

| Criterio | Regla |
|---|---|
| **Lenguaje** | Claro y directo. Si un término técnico es imprescindible, defínelo en `🧩 Conceptos`. |
| **Ejemplos numéricos** | Siempre con verificación de escala antes de sumar o multiplicar. |
| **Supuestos** | Se declaran **antes** del cálculo que depende de ellos. |
| **Datos** | Exclusivamente sintéticos. Nunca reales, ni siquiera anonimizados. |
| **Normativa** | Se describe el marco internacional y se añade la línea de *verificación local*. |
| **Cifras** | Con su unidad declarada. |
| **Anchura** | Líneas de hasta ~100 caracteres, para que el diff sea legible. |

---

## 📗 Fuentes

Toda afirmación técnica necesita respaldo. Se aceptan:

- Manuales universitarios de referencia, con autor, año, edición y capítulo.
- Normas contables emitidas (NIIF/NIC) y sus documentos oficiales.
- Documentos de organismos de estándares: BIS, FSB, GAFI, IOSCO, CPMI, OCDE, FMI,
  Banco Mundial, NIST, ISO, IADI, IAIS.
- Artículos académicos identificables, con revista, volumen y año.

**No se aceptan** blogs, resúmenes, contenidos sin autoría, ni referencias a «la práctica
del sector» sin documento que la sustente.

Formato de una entrada:

```markdown
- Saunders, A. y Cornett, M. (2021). *Financial Institutions Management* (10.ª ed.).
  McGraw-Hill. Capítulos 8, 9 y 17: gestión de activos y pasivos y de liquidez.
- Basel Committee on Banking Supervision (2016). *Interest rate risk in the banking book*.
  BIS. Escenarios de choque de tasas y medidas de valor económico y margen.
  <https://www.bis.org/bcbs/publ/d368.htm>
- Verificación local: revisa los requerimientos que aplica tu supervisor.
```

La frase que sigue a la editorial **no es opcional**: dice qué toma esa clase de esa obra.
Sin ella, quien quiera comprobar la afirmación tendría que leerse el documento entero para
averiguar si dice lo que la clase supone, y `verify_sources.py` rechaza la cita.

### El registro de fuentes

Las citas no viven solo en la clase: alimentan
**[sources/bibliography.json](sources/bibliography.json)**, donde cada obra tiene emisor,
localizador y fecha de comprobación. No se edita a mano — se reconstruye desde las clases:

```bash
python scripts/verify_sources.py --rebuild
```

Un localizador admite exactamente tres formas: **ISBN-13** para un libro, **DOI** para un
artículo y **URL https de la fuente primaria** para una norma o documento oficial. Los
resuelve `scripts/refresh_sources.py` contra Open Library, Crossref y el propio sitio del
emisor; lo que no resuelve queda como `pendiente` con el motivo escrito.

**Nunca inventes un ISBN, un DOI, una URL o una fecha**, y **nunca borres** una fuente que
no resuelva: se marca, no se elimina. Un hueco declarado es información; un hueco relleno
por intuición es una invención con formato de bibliografía.

---

## 🌎 Adaptaciones por país

Las ediciones locales son bienvenidas y **no sustituyen** el contenido internacional.

- Añade una sección al final de la clase; no modifiques la existente.
- Cita la norma nacional con su identificador y su fecha de vigencia.
- Registra la **fecha de revisión** de la adaptación.
- Ver [ROADMAP.md](ROADMAP.md) para las ediciones previstas.

---

## 🤝 Flujo de trabajo

1. **Abre un issue** describiendo el cambio, salvo que sea trivial.
2. **Crea una rama** por cambio: `fix/parte-11-clase-04-fuente`, `docs/glosario`.
3. **Haz el cambio** siguiendo las convenciones de arriba.
4. **Ejecuta las siete verificaciones.**
5. **Abre la propuesta** describiendo qué cambia, por qué y qué fuente lo respalda.

### Mensajes de confirmación

```text
Corrige la LGD de la clase 8 de la Parte 16

El calculo original omitia el descuento por el plazo de recuperacion.
Fuente: Caouette et al. (2008), capitulo 12.
```

Imperativo, con el porqué y la fuente cuando corresponda.

---

## 🔧 Herramientas y dependencias

| Ámbito | Herramienta |
|---|---|
| Python | 3.12; dependencias en `requirements.txt` |
| Pruebas | `pytest` |
| JavaScript / TypeScript | `pnpm`; no añadas `npm` como gestor principal |
| Finales de línea | LF, forzado por `.gitattributes` |
| Codificación | UTF-8 sin BOM |

---

## 📣 Reportar sin contribuir código

| Situación | Canal |
|---|---|
| Error de contenido | [Issue](https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/issues) citando la clase y la fuente correcta |
| Fuente rota o superada | Issue con la referencia vigente |
| Ambigüedad o texto confuso | Issue indicando qué no se entiende |
| Sesgo o formulación problemática | Issue; se revisa con prioridad |
| Problema de seguridad | [SECURITY.md](SECURITY.md) |

---

## 🤗 Código de conducta

Este proyecto se rige por su **[Código de Conducta](CODE_OF_CONDUCT.md)**. Participar
implica aceptarlo.

---

**Ver también:** [README](README.md) · [Documentación](docs/README.md) ·
[Ética y limitaciones](docs/etica-y-limitaciones.md)

<!-- pie:inicio -->
---

<div align="center">

[🏠 Inicio](README.md) · [📚 Documentación](docs/README.md) · [🗺️ Roadmap](ROADMAP.md) · [🤗 Código de conducta](CODE_OF_CONDUCT.md) · [🔐 Seguridad](SECURITY.md)

</div>
<!-- pie:fin -->
