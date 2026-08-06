"""Busca datos personales reales en los conjuntos de datos y en el portafolio.

El programa exige trabajar con datos sinteticos. Este detector comprueba que la
exigencia se cumple en los sitios donde el dato viaja: `datasets/`, `portfolio/`,
`apps/**/data/` y los proyectos.

No revisa el texto de las clases: ahi los identificadores aparecen como ejemplo
didactico y estan enmascarados por diseno.

Uso:
    python tools/detect_pii.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

AMBITOS = ("datasets", "portfolio", "projects")
SKIP_DIRS = {".git", ".venv", "node_modules", "site", "__pycache__", ".pytest_cache"}
EXTENSIONES = {".csv", ".json", ".tsv", ".txt", ".md", ".yml", ".yaml"}


def luhn(numero: str) -> bool:
    """Comprueba el digito verificador de una tarjeta.

    Un numero de 16 cifras que NO pasa Luhn es casi seguro sintetico; uno que si
    lo pasa merece una mirada humana.
    """
    digitos = [int(c) for c in numero if c.isdigit()]
    if len(digitos) < 13:
        return False
    total = 0
    for indice, digito in enumerate(reversed(digitos)):
        if indice % 2 == 1:
            digito *= 2
            if digito > 9:
                digito -= 9
        total += digito
    return total % 10 == 0


def rut_valido(rut: str) -> bool:
    """Digito verificador de un RUT chileno (modulo 11)."""
    cuerpo = re.sub(r"[^0-9]", "", rut[:-1])
    verificador = rut[-1].upper()
    if not cuerpo or len(cuerpo) < 7:
        return False
    suma, factor = 0, 2
    for caracter in reversed(cuerpo):
        suma += int(caracter) * factor
        factor = 2 if factor == 7 else factor + 1
    resto = 11 - (suma % 11)
    esperado = {11: "0", 10: "K"}.get(resto, str(resto))
    return esperado == verificador


DETECTORES = (
    ("RUT con digito verificador valido",
     re.compile(r"\b\d{1,2}\.?\d{3}\.?\d{3}-[\dkK]\b"), rut_valido),
    ("numero de tarjeta que pasa Luhn",
     re.compile(r"\b(?:\d[ -]?){13,19}\b"), luhn),
    ("IBAN con formato completo",
     re.compile(r"\b[A-Z]{2}\d{2}[A-Z0-9]{11,30}\b"), lambda s: True),
    ("direccion de correo con dominio real",
     re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.]{2,}\b"),
     lambda s: not s.lower().endswith((".example", ".test", ".invalid", "example.com"))),
)


def archivos() -> list[Path]:
    encontrados: list[Path] = []
    for ambito in AMBITOS:
        base = ROOT / ambito
        if base.exists():
            encontrados += [p for p in base.rglob("*") if p.is_file()]
    apps = ROOT / "apps"
    if apps.exists():
        encontrados += [p for p in apps.rglob("data/*") if p.is_file()]
    return sorted(
        p for p in set(encontrados)
        if p.suffix.lower() in EXTENSIONES
        and not any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts)
    )


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
            for nombre, patron, confirma in DETECTORES:
                for coincidencia in patron.findall(linea):
                    valor = coincidencia if isinstance(coincidencia, str) else coincidencia[0]
                    if confirma(valor.strip()):
                        hallazgos.append(f"{rel}:{numero}: {nombre} -> {valor.strip()[:24]}")
                        break

    print(f"archivos revisados: {revisados}")

    if hallazgos:
        print(f"\n{len(hallazgos)} hallazgo(s):")
        for item in hallazgos[:40]:
            print(f"  - {item}")
        if len(hallazgos) > 40:
            print(f"  ... y {len(hallazgos) - 40} mas")
        print(
            "\nLos datos del repositorio deben ser sinteticos. Si un valor lo es y "
            "aun asi pasa la comprobacion, cambialo: un dato que parece real se "
            "trata como real."
        )
        return 1

    print("\nSin datos personales detectados en los ambitos revisados")
    return 0


if __name__ == "__main__":
    sys.exit(main())
