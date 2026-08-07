"""Validación estructural del programa.

Comprueba que el repositorio sea internamente coherente:

1. cada clase tiene encabezado YAML completo y las secciones obligatorias;
2. cada clase está renderizada (navegación, agenda y pie generados);
3. cada clase declara al menos cuatro fuentes verificables;
4. los enlaces relativos de los README de parte apuntan a archivos existentes;
5. el avance declarado en `STATUS.md` coincide con los archivos reales;
6. cada parte tiene laboratorios, evaluaciones y proyecto.

Uso:
    python tools/validate_program.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULES = ROOT / "modules"

REQUIRED_META = ("part", "class", "title", "level", "duration_minutes", "status")
REQUIRED_SECTIONS = (
    "## 🎯 Propósito",
    "## 📚 Objetivos",
    "## Agenda de 90 minutos",
    "## 🧩 Conceptos centrales",
    "## 📖 Desarrollo",
    "## 🧮 Ejemplo guiado",
    "## 🏦 Del cliente al banco",
    "## ⚠️ Errores frecuentes",
    "## ❓ Preguntas de comprobación",
    "## 📥 Entregable",
    "## 📗 Fuentes y verificación",
)
GENERATED_MARKERS = (
    "<!-- gen:header:start -->",
    "<!-- gen:agenda:start -->",
    "<!-- gen:etica:start -->",
    "<!-- gen:footer:start -->",
)
MIN_SOURCES = 4


# Los metadatos de una clase van dentro de un comentario HTML: un bloque
# YAML delimitado por `---` lo renderiza GitHub como una tabla de seis o
# doce filas delante del titulo, y esos datos son para las herramientas, no
# para quien estudia. Dentro del comentario siguen siendo legibles por
# maquina y dejan de ocupar la primera pantalla.
META_CLASE = re.compile(r"^<!--\s*meta\n(.*?)\n-->\n", re.S)


def frontmatter(text: str) -> dict[str, str]:
    encontrado = META_CLASE.match(text)
    if not encontrado:
        return {}
    meta: dict[str, str] = {}
    for line in encontrado.group(1).strip().splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip()
    return meta


def check_classes(errors: list[str]) -> None:
    for path in sorted(MODULES.glob("*/classes/*.md")):
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        meta = frontmatter(text)

        missing_meta = [key for key in REQUIRED_META if key not in meta]
        if missing_meta:
            errors.append(f"{rel}: faltan claves en el encabezado YAML: {missing_meta}")

        missing_sections = [head for head in REQUIRED_SECTIONS if head not in text]
        if missing_sections:
            errors.append(f"{rel}: faltan secciones: {missing_sections}")

        missing_generated = [mark for mark in GENERATED_MARKERS if mark not in text]
        if missing_generated:
            errors.append(
                f"{rel}: sin renderizar. Ejecuta: python tools/render_program.py"
            )

        if path.name != path.name.encode("ascii", "ignore").decode("ascii"):
            errors.append(f"{rel}: el nombre de archivo debe ser ASCII")

        parts = text.split("## 📗 Fuentes y verificación", 1)
        if len(parts) == 2:
            bullets = [ln for ln in parts[1].splitlines() if ln.startswith("- ")]
            if len(bullets) < MIN_SOURCES:
                errors.append(
                    f"{rel}: {len(bullets)} fuentes declaradas; se exigen al menos {MIN_SOURCES}"
                )


def check_links(errors: list[str]) -> None:
    pattern = re.compile(r"\[[^\]]+\]\((?!https?://|#|mailto:)([^)]+)\)")
    for readme in sorted(MODULES.glob("*/README.md")):
        text = readme.read_text(encoding="utf-8")
        for target in pattern.findall(text):
            target = target.split("#", 1)[0]
            if not target:
                continue
            if not (readme.parent / target).exists():
                errors.append(f"{readme.relative_to(ROOT)}: enlace roto -> {target}")


def check_structure(errors: list[str], pending: list[str]) -> dict[str, int]:
    """Verifica la estructura de cada parte.

    Una parte sin clases redactadas todavia no es un error: es contenido
    pendiente, y `STATUS.md` lo declara de forma explicita. Lo que si es un
    error es una parte sin laboratorios, sin evaluaciones o sin proyecto,
    porque esa estructura debe existir desde el diseno del programa.
    """
    counts = {"modules": 0, "classes": 0, "labs": 0, "assessments": 0, "projects": 0}
    for module in sorted(p for p in MODULES.iterdir() if p.is_dir()):
        counts["modules"] += 1
        rel = module.relative_to(ROOT)
        classes = sorted((module / "classes").glob("*.md"))
        labs = list((module / "labs").glob("*.md"))
        assessments = list((module / "assessments").glob("*.md"))
        project = module / "project" / "README.md"

        counts["classes"] += len(classes)
        counts["labs"] += len(labs)
        counts["assessments"] += len(assessments)
        counts["projects"] += int(project.exists())

        if not classes:
            pending.append(str(rel))
        if not labs:
            errors.append(f"{rel}: sin laboratorios")
        if len(assessments) < 2:
            errors.append(f"{rel}: se esperan diagnóstico y evaluación final")
        if not project.exists():
            errors.append(f"{rel}: falta project/README.md")

        numbers = sorted(
            int(frontmatter(p.read_text(encoding="utf-8")).get("class", 0))
            for p in classes
        )
        if classes and numbers != list(range(1, len(classes) + 1)):
            errors.append(f"{rel}: numeración de clases no correlativa: {numbers}")
    return counts


def check_status(errors: list[str], counts: dict[str, int]) -> None:
    """STATUS.md debe declarar exactamente las clases que existen.

    SYLLABUS.md describe el programa completo planificado; STATUS.md declara el
    avance real. La coherencia que se exige aqui es contra STATUS.md, para que la
    documentacion nunca afirme mas contenido del que el repositorio contiene.
    """
    status = ROOT / "STATUS.md"
    if not status.exists():
        errors.append("falta STATUS.md; ejecuta: python tools/progress.py")
        return
    text = status.read_text(encoding="utf-8")
    match = re.search(r"Avance global:\s*(\d+)\s+de\s+(\d+)\s+clases", text)
    if not match:
        errors.append("STATUS.md: no se encontro la linea de avance global")
        return
    declared = int(match.group(1))
    if declared != counts["classes"]:
        errors.append(
            f"STATUS.md declara {declared} clases redactadas y existen "
            f"{counts['classes']}. Ejecuta: python tools/progress.py"
        )


def main() -> int:
    errors: list[str] = []
    pending: list[str] = []
    counts = check_structure(errors, pending)
    check_classes(errors)
    check_links(errors)
    check_status(errors, counts)

    print(f"partes:        {counts['modules']}")
    print(f"clases:        {counts['classes']}")
    print(f"laboratorios:  {counts['labs']}")
    print(f"evaluaciones:  {counts['assessments']}")
    print(f"proyectos:     {counts['projects']}")
    if pending:
        print(f"\npartes con contenido pendiente: {len(pending)}")
        for item in pending:
            print(f"  - {item}")

    if errors:
        print(f"\n{len(errors)} problema(s) encontrados:")
        for item in errors[:60]:
            print(f"  - {item}")
        if len(errors) > 60:
            print(f"  ... y {len(errors) - 60} mas")
        return 1

    print("\nPrograma validado correctamente")
    return 0


if __name__ == "__main__":
    sys.exit(main())
