"""Genera FILE_INDEX.md desde los archivos reales del repositorio.

El indice estaba escrito a mano y se desactualizo en el primer cambio de
estructura: llegó a enlazar un workflow que ya no existía. Un indice que miente
es peor que no tener indice, porque quien lo lee deja de comprobar.

Uso:
    python tools/build_file_index.py           # regenera FILE_INDEX.md
    python tools/build_file_index.py --check   # falla si esta desactualizado
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "FILE_INDEX.md"

# Directorios que nunca entran: generados, temporales o de terceros.
EXCLUIDOS = {
    ".git",
    ".venv",
    "node_modules",
    "site",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    ".mypy_cache",
}
EXTENSIONES_BINARIAS = {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip", ".ico"}


def rastreados() -> list[Path] | None:
    """Archivos que formaran parte del repositorio.

    Se prefiere git porque respeta `.gitignore` sin reimplementarlo, pero con
    `--others --exclude-standard`: sin esa parte, un archivo nuevo todavia sin
    `git add` quedaria fuera del indice y el resultado dependeria del orden en
    que se ejecutaran el generador y el `add`. Un generador cuyo resultado
    depende del orden no sirve como puerta de `--check`.

    Si git no esta disponible, se recorre el arbol y se filtra a mano.
    """
    try:
        salida = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
    except (OSError, subprocess.CalledProcessError):
        return None
    return [ROOT / linea for linea in salida.splitlines() if linea]


def recorrido() -> list[Path]:
    encontrados: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        partes = path.relative_to(ROOT).parts
        if any(parte in EXCLUIDOS for parte in partes):
            continue
        encontrados.append(path)
    return encontrados


def archivos() -> list[str]:
    candidatos = rastreados()
    if candidatos is None:
        candidatos = recorrido()
    relativos = []
    for path in candidatos:
        rel = path.relative_to(ROOT).as_posix()
        if any(parte in EXCLUIDOS for parte in Path(rel).parts):
            continue
        if Path(rel).suffix.lower() in EXTENSIONES_BINARIAS:
            continue
        relativos.append(rel)
    return sorted(set(relativos))


# Portada del documento generado, con la misma pauta visual que el README.
PORTADA = """<!-- portada:inicio -->
<div align="center">

# 🗂️ Índice de archivos

**Todo el texto versionado del repositorio, en un listado plano y ordenado.**

[![archivos](https://img.shields.io/badge/archivos-{total}-7c5cff?style=flat-square)](FILE_INDEX.md)
[![generado por](https://img.shields.io/badge/generado%20por-build__file__index.py-007c83?style=flat-square)](tools/build_file_index.py)
[![se edita](https://img.shields.io/badge/se%20edita-nunca%20a%20mano-8b0000?style=flat-square)](MANIFEST.md)

[🏠 Inicio](README.md) ·
[📚 Programa](SYLLABUS.md) ·
[📊 Estado](STATUS.md) ·
[🧾 Ficha técnica](MANIFEST.md)

</div>
<!-- portada:fin -->

---
"""

PIE = """
---

<div align="center">

[🏠 Inicio](README.md) · [📚 Programa](SYLLABUS.md) · [📊 Estado](STATUS.md) · [🧾 Ficha técnica](MANIFEST.md)

</div>
"""


def render() -> str:
    rutas = archivos()
    lineas = [*PORTADA.format(total=len(rutas)).splitlines(), ""]
    lineas += [f"- `{ruta}`" for ruta in rutas]
    lineas += [
        "",
        "## ✅ Verificación",
        "",
        "```bash",
        "python tools/build_file_index.py --check",
        "```",
        *PIE.splitlines(),
        "",
    ]
    return "\n".join(lineas)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    contenido = render()
    actual = INDEX.read_text(encoding="utf-8") if INDEX.exists() else ""

    if args.check:
        if actual != contenido:
            print("FILE_INDEX.md esta desactualizado. Ejecuta: python tools/build_file_index.py")
            return 1
        print("FILE_INDEX.md refleja los archivos reales")
        return 0

    INDEX.write_text(contenido, encoding="utf-8", newline="\n")
    print(f"FILE_INDEX.md generado: {len(archivos())} archivos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
