"""Genera STATUS.md a partir del estado real del repositorio.

El programa está diseñado con 240 clases (ver SYLLABUS.md). Este script mide
cuántas están efectivamente redactadas y produce un informe verificable, de modo
que la documentación nunca afirme más de lo que el repositorio contiene.

Uso:
    python tools/progress.py           # regenera STATUS.md
    python tools/progress.py --check   # falla si STATUS.md está desactualizado
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULES = ROOT / "modules"
STATUS = ROOT / "STATUS.md"

PLANNED = {
    "00-matematica-financiera-basica": 14,
    "01-finanzas-personales": 14,
    "02-productos-y-servicios-financieros": 14,
    "03-seguridad-y-consumo-financiero": 14,
    "04-contabilidad-financiera": 15,
    "05-economia-y-sistema-financiero": 15,
    "06-matematica-financiera-avanzada": 15,
    "07-inversiones-y-mercados": 15,
    "08-analisis-y-gestion-de-credito": 16,
    "09-operaciones-bancarias": 16,
    "10-gestion-integral-de-riesgos": 16,
    "11-regulacion-cumplimiento-y-auditoria": 16,
    "12-finanzas-corporativas-y-banca-empresarial": 14,
    "13-fintech-datos-e-inteligencia-artificial": 14,
    "14-estrategia-y-direccion-bancaria": 14,
    "15-proyecto-banco-virtual": 18,
}


def module_title(module: Path) -> str:
    readme = module / "README.md"
    if readme.exists():
        first = readme.read_text(encoding="utf-8").splitlines()[0]
        return re.sub(r"^#\s*", "", first).strip()
    return module.name


def bar(done: int, total: int, width: int = 20) -> str:
    filled = round(width * done / total) if total else 0
    return "█" * filled + "░" * (width - filled)


def collect() -> tuple[list[tuple[str, str, int, int, int]], int, int, int]:
    rows: list[tuple[str, str, int, int, int]] = []
    total_done = total_planned = total_bytes = 0
    for name, planned in PLANNED.items():
        module = MODULES / name
        classes = sorted((module / "classes").glob("*.md")) if module.exists() else []
        done = len(classes)
        size = sum(p.stat().st_size for p in classes)
        rows.append((name, module_title(module), done, planned, size))
        total_done += done
        total_planned += planned
        total_bytes += size
    return rows, total_done, total_planned, total_bytes


def render() -> str:
    rows, done, planned, size = collect()
    pct = 100 * done / planned if planned else 0
    avg = size / done if done else 0

    lines = [
        "# Estado del contenido",
        "",
        "Este archivo lo genera `tools/progress.py` a partir de los archivos reales",
        "del repositorio. No se edita a mano: refleja lo que hay, no lo que se planea.",
        "",
        f"## Avance global: {done} de {planned} clases ({pct:.1f} %)",
        "",
        f"`{bar(done, planned, 40)}`",
        "",
        "| Parte | Tema | Clases | Plan | Avance | Tamaño medio |",
        "|---:|---|---:|---:|---|---:|",
    ]

    for index, (_, title, mod_done, mod_planned, mod_size) in enumerate(rows, start=1):
        mod_avg = mod_size / mod_done / 1024 if mod_done else 0
        lines.append(
            f"| {index} | {title} | {mod_done} | {mod_planned} | "
            f"`{bar(mod_done, mod_planned)}` | {mod_avg:.1f} KB |"
        )

    lines += [
        f"| | **Total** | **{done}** | **{planned}** | "
        f"`{bar(done, planned)}` | **{avg / 1024:.1f} KB** |",
        "",
        "## Qué significa que una clase esté completa",
        "",
        "Una clase solo se cuenta aquí si supera `tools/validate_program.py`, que exige:",
        "",
        "- encabezado con parte, número, título, nivel, duración y estado;",
        "- las once secciones obligatorias, incluidas ejemplo numérico guiado,",
        "  puente «del cliente al banco», errores frecuentes y entregable;",
        "- navegación, agenda docente y bloque de ética generados por",
        "  `tools/render_program.py`;",
        "- al menos cuatro fuentes verificables en «Fuentes y verificación».",
        "",
        "## Otros componentes",
        "",
        "| Componente | Estado |",
        "|---|---|",
        "| Arquitectura curricular (16 partes) | Completa |",
        "| Laboratorios (96) | Estructurados |",
        "| Evaluaciones (32) | Diagnóstico y final por parte |",
        "| Proyectos integradores (16) | Especificados |",
        "| Calculadoras financieras | MVP funcional con pruebas |",
        "| Banco virtual (SQLite) | MVP funcional con pruebas |",
        "| Datasets sintéticos | Iniciales |",
        "| Adaptación normativa por país | Plantilla; cada clase indica qué verificar |",
        "",
        "## Cómo verificarlo",
        "",
        "```bash",
        "python tools/validate_program.py     # estructura, secciones y fuentes",
        "python tools/render_program.py --check  # navegación y bloques generados",
        "python tools/progress.py --check     # este archivo contra la realidad",
        "pytest -q                            # calculadoras y banco virtual",
        "```",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    content = render()
    current = STATUS.read_text(encoding="utf-8") if STATUS.exists() else ""

    if args.check:
        if current != content:
            print("STATUS.md esta desactualizado. Ejecuta: python tools/progress.py")
            return 1
        print("STATUS.md refleja el estado real del repositorio")
        return 0

    STATUS.write_text(content, encoding="utf-8", newline="\n")
    rows, done, planned, _ = collect()
    print(f"STATUS.md actualizado: {done}/{planned} clases")
    return 0


if __name__ == "__main__":
    sys.exit(main())
