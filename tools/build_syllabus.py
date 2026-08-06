"""Genera SYLLABUS.md con el índice completo de las clases del programa.

El programa cambia clase a clase, y un índice escrito a mano se desactualiza
en la primera edición. Este script lo construye desde el encabezado YAML de
cada archivo, de modo que el índice siempre describe lo que el repositorio
contiene.

Uso:
    python tools/build_syllabus.py           # regenera SYLLABUS.md
    python tools/build_syllabus.py --check   # falla si está desactualizado
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULES = ROOT / "modules"
SYLLABUS = ROOT / "SYLLABUS.md"

ETAPAS = {
    range(1, 5): "Fundamentos — sin conocimientos previos",
    range(5, 9): "Analista — lenguaje técnico y modelado",
    range(9, 13): "Bancario — crédito, operaciones, riesgo y cumplimiento",
    range(13, 17): "Dirección — empresa, tecnología, estrategia y proyecto",
    range(17, 24): "Finanzas digitales — infraestructura y mercados tokenizados",
}


def etapa(parte: int) -> str:
    for rango, nombre in ETAPAS.items():
        if parte in rango:
            return nombre
    return ""


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    try:
        _, front, _ = text.split("---", 2)
    except ValueError:
        return {}
    meta: dict[str, str] = {}
    for line in front.strip().splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip().strip('"')
    return meta


def module_title(module: Path) -> str:
    readme = module / "README.md"
    if not readme.exists():
        return module.name
    first = readme.read_text(encoding="utf-8").splitlines()[0]
    title = re.sub(r"^#\s*", "", first).strip()
    return re.sub(r"^Parte\s+\d+:\s*", "", title)


def collect() -> list[tuple[int, str, Path, list[tuple[int, str, str, Path]]]]:
    partes: list[tuple[int, str, Path, list[tuple[int, str, str, Path]]]] = []
    for module in sorted(p for p in MODULES.iterdir() if p.is_dir()):
        clases: list[tuple[int, str, str, Path]] = []
        parte_num = 0
        for path in sorted((module / "classes").glob("*.md")):
            meta = frontmatter(path.read_text(encoding="utf-8"))
            parte_num = int(meta.get("part", 0))
            clases.append(
                (
                    int(meta.get("class", 0)),
                    meta.get("title", path.stem),
                    meta.get("level", ""),
                    path,
                )
            )
        partes.append((parte_num, module_title(module), module, clases))
    return partes


def render() -> str:
    partes = collect()
    total_clases = sum(len(c) for *_, c in partes)
    total_horas = total_clases * 1.5

    lines = [
        "# Programa completo",
        "",
        "Índice generado por `tools/build_syllabus.py` desde el encabezado de cada",
        "clase. Describe el contenido real del repositorio, no un plan.",
        "",
        f"**{len(partes)} partes · {total_clases} clases · {total_horas:.0f} horas ·",
        "90 minutos por clase**",
        "",
        "## Estructura por etapas",
        "",
        "| Parte | Tema | Clases | Horas | Etapa |",
        "|---:|---|---:|---:|---|",
    ]

    for parte_num, titulo, module, clases in partes:
        rel = module.relative_to(ROOT).as_posix()
        lines.append(
            f"| {parte_num} | [{titulo}]({rel}/README.md) | {len(clases)} | "
            f"{len(clases) * 1.5:.1f} | {etapa(parte_num)} |"
        )
    lines.append(
        f"| | **Total** | **{total_clases}** | **{total_horas:.0f}** | |"
    )

    lines += [
        "",
        "## Índice de clases",
        "",
        "Cada clase dura 90 minutos e incluye ejemplo numérico guiado, puente",
        "«del cliente al banco», errores frecuentes, preguntas de comprobación,",
        "entregable de portafolio y al menos cuatro fuentes verificables.",
        "",
    ]

    for parte_num, titulo, module, clases in partes:
        rel = module.relative_to(ROOT).as_posix()
        lines += [
            f"### Parte {parte_num} — {titulo}",
            "",
            f"[Índice de la parte]({rel}/README.md) · "
            f"[Laboratorios]({rel}/labs) · "
            f"[Evaluaciones]({rel}/assessments) · "
            f"[Proyecto]({rel}/project/README.md)",
            "",
            "| # | Clase | Nivel |",
            "|---:|---|---|",
        ]
        for numero, titulo_clase, nivel, path in clases:
            enlace = path.relative_to(ROOT).as_posix()
            lines.append(f"| {numero:02d} | [{titulo_clase}]({enlace}) | {nivel} |")
        lines.append("")

    ultima_parte, ultimo_titulo, _, ultimas_clases = partes[-1]
    lines += [
        "## Criterio de aprobación sugerido",
        "",
        "- Recorrer las clases en orden: cada una supone la anterior.",
        "- 70 % de logro en las evaluaciones diagnóstica y final de cada parte.",
        f"- Entrega de los {len(partes)} proyectos integradores.",
        "- Portafolio con el entregable de cada clase.",
        f"- Defensa del proyecto final «{ultimo_titulo}» "
        f"(Parte {ultima_parte}, clase {len(ultimas_clases)}).",
        "",
        "## Resultados finales",
        "",
        "Al completar el programa, quien lo recorra podrá interpretar productos",
        "financieros, modelar decisiones, analizar estados financieros, evaluar",
        "créditos, comprender operaciones bancarias, medir riesgos, diseñar",
        "controles, aplicar el marco regulatorio y dirigir un banco simulado;",
        "y en la Etapa 5, diseñar y defender infraestructura de finanzas abiertas,",
        "pagos transfronterizos, activos digitales, tokenización y liquidación",
        "programable, sosteniendo cada decisión con su fundamento, sus supuestos",
        "y sus límites.",
        "",
        "## Verificación",
        "",
        "```bash",
        "python tools/build_syllabus.py --check",
        "```",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    content = render()
    current = SYLLABUS.read_text(encoding="utf-8") if SYLLABUS.exists() else ""

    if args.check:
        if current != content:
            print("SYLLABUS.md esta desactualizado. Ejecuta: python tools/build_syllabus.py")
            return 1
        print("SYLLABUS.md refleja el indice real de clases")
        return 0

    SYLLABUS.write_text(content, encoding="utf-8", newline="\n")
    total = sum(len(c) for *_, c in collect())
    print(f"SYLLABUS.md generado: {total} clases indexadas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
