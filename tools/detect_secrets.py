"""Busca credenciales reales en el repositorio.

Un programa que ensena seguridad no puede tener secretos versionados. El
laboratorio 2 de la Parte 17 usa claves de juguete a proposito, y por eso el
detector distingue dos cosas:

* un patron de secreto REAL (clave privada, token de proveedor, cadena de
  conexion con contrasena) -> error;
* un valor de ejemplo claramente marcado como tal -> se ignora, porque el
  material didactico necesita mostrar la forma de un secreto sin contenerlo.

Uso:
    python tools/detect_secrets.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".venv", "node_modules", "site", "__pycache__", ".pytest_cache"}
SKIP_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip", ".ico", ".woff2"}

PATRONES: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("clave privada", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |PGP )?PRIVATE KEY-----")),
    ("clave de acceso AWS", re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b")),
    ("token de GitHub", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,}\b")),
    ("token de Slack", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b")),
    ("clave de Google", re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b")),
    ("token de Stripe", re.compile(r"\b(?:sk|rk)_live_[0-9A-Za-z]{20,}\b")),
    ("cadena de conexion con contrasena",
     re.compile(r"\b[a-z][a-z0-9+.-]*://[^\s:/@]+:[^\s:/@]{6,}@[^\s/]+")),
    ("asignacion de secreto",
     re.compile(r"(?i)\b(?:password|passwd|secret|api[_-]?key|token|private[_-]?key)\b"
                r"\s*[:=]\s*[\"'][^\"'\n]{12,}[\"']")),
)

# Valores que el material usa deliberadamente para mostrar la FORMA de un
# secreto. Cada entrada esta aqui porque no es un secreto, no por comodidad.
MARCAS_DE_EJEMPLO = (
    "ejemplo", "example", "sample", "placeholder", "cambiar", "changeme",
    "tu-clave", "your-", "xxxxx", "<", "...", "juguete", "sintetic", "synthetic",
    "de-juguete", "no-usar", "dummy", "fake", "redacted",
)


def archivos() -> list[Path]:
    encontrados: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        if path.suffix.lower() in SKIP_SUFFIXES:
            continue
        encontrados.append(path)
    return sorted(encontrados)


def es_ejemplo(linea: str) -> bool:
    minuscula = linea.lower()
    return any(marca in minuscula for marca in MARCAS_DE_EJEMPLO)


def main() -> int:
    hallazgos: list[str] = []
    revisados = 0

    for path in archivos():
        try:
            texto = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        revisados += 1
        rel = path.relative_to(ROOT)
        for numero, linea in enumerate(texto.splitlines(), start=1):
            if es_ejemplo(linea):
                continue
            for nombre, patron in PATRONES:
                if patron.search(linea):
                    hallazgos.append(f"{rel}:{numero}: posible {nombre}")
                    break

    # Un .env versionado es un hallazgo por si mismo, tenga lo que tenga dentro.
    for env in ROOT.rglob(".env"):
        if not any(part in SKIP_DIRS for part in env.relative_to(ROOT).parts):
            hallazgos.append(f"{env.relative_to(ROOT)}: un .env nunca se versiona")

    print(f"archivos revisados: {revisados}")

    if hallazgos:
        print(f"\n{len(hallazgos)} hallazgo(s):")
        for item in hallazgos[:40]:
            print(f"  - {item}")
        if len(hallazgos) > 40:
            print(f"  ... y {len(hallazgos) - 40} mas")
        print("\nSi alguno es un valor de ejemplo, marcalo como tal en la propia linea.")
        return 1

    print("\nSin credenciales detectadas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
