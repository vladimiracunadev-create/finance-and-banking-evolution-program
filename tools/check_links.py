"""Verifica que todos los enlaces relativos del repositorio apunten a algo real.

Recorre cada archivo Markdown, extrae los enlaces que no son externos y comprueba
que el destino exista. Un enlace roto en un programa de estudio es un callejón sin
salida para quien lo recorre, y por eso se trata como error de integración.

Uso:
    python tools/check_links.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".github", "__pycache__", ".venv", "node_modules"}
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
EXTERNAL = ("http://", "https://", "mailto:", "tel:", "#")


def markdown_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        files.append(path)
    return sorted(files)


def main() -> int:
    broken: list[str] = []
    checked = 0

    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        for raw in LINK.findall(text):
            target = raw.strip()
            if target.startswith(EXTERNAL) or not target:
                continue
            # Ignora enlaces con protocolo desconocido o anclas puras.
            if "://" in target:
                continue
            checked += 1
            resolved = (path.parent / target.split("#", 1)[0]).resolve()
            if not resolved.exists():
                broken.append(f"{path.relative_to(ROOT)} -> {target}")

    print(f"archivos revisados: {len(markdown_files())}")
    print(f"enlaces relativos:  {checked}")

    if broken:
        print(f"\n{len(broken)} enlace(s) roto(s):")
        for item in broken[:60]:
            print(f"  - {item}")
        if len(broken) > 60:
            print(f"  ... y {len(broken) - 60} mas")
        return 1

    print("\nTodos los enlaces relativos resuelven correctamente")
    return 0


if __name__ == "__main__":
    sys.exit(main())
