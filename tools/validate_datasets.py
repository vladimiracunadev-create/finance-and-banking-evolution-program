"""Comprueba que cada conjunto de datos esté documentado y sea coherente.

Un dataset sin diccionario es un archivo que alguien tendrá que adivinar. La
regla del repositorio es simple: **todo CSV tiene su ficha en
`datasets/schemas/`**, y la ficha describe las columnas que el CSV realmente
tiene.

Comprueba:

1. cada `*.csv` de `datasets/` tiene una ficha con su mismo nombre;
2. la ficha declara origen, licencia, fecha, supuestos y limitaciones;
3. toda columna del CSV aparece nombrada en la ficha;
4. el CSV no tiene filas con un número de campos distinto de la cabecera;
5. no hay identificadores duplicados en la primera columna, si termina en `_id`.

Uso:
    python tools/validate_datasets.py
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATASETS = ROOT / "datasets"
SCHEMAS = DATASETS / "schemas"

SECCIONES_FICHA = (
    "Origen",
    "Licencia",
    "Supuestos",
    "Limitaciones",
    "Diccionario",
)


def fichas() -> dict[str, Path]:
    if not SCHEMAS.exists():
        return {}
    return {p.stem: p for p in SCHEMAS.glob("*.md") if p.name != "README.md"}


def main() -> int:
    errores: list[str] = []
    if not DATASETS.exists():
        print("no existe datasets/")
        return 0

    documentacion = fichas()
    archivos = sorted(p for p in DATASETS.rglob("*.csv"))

    for path in archivos:
        rel = path.relative_to(ROOT)
        ficha = documentacion.get(path.stem)
        if ficha is None:
            errores.append(
                f"{rel}: sin ficha en datasets/schemas/{path.stem}.md"
            )
            continue

        texto = ficha.read_text(encoding="utf-8")
        faltan = [s for s in SECCIONES_FICHA if s.lower() not in texto.lower()]
        if faltan:
            errores.append(f"{ficha.relative_to(ROOT)}: faltan secciones {faltan}")

        with path.open(encoding="utf-8", newline="") as fh:
            lector = csv.reader(fh)
            try:
                cabecera = next(lector)
            except StopIteration:
                errores.append(f"{rel}: archivo vacio")
                continue

            no_documentadas = [c for c in cabecera if f"`{c}`" not in texto]
            if no_documentadas:
                errores.append(
                    f"{ficha.relative_to(ROOT)}: columnas sin documentar {no_documentadas}"
                )

            identificadores: set[str] = set()
            duplicados = 0
            irregulares = 0
            for numero, fila in enumerate(lector, start=2):
                if len(fila) != len(cabecera):
                    irregulares += 1
                    if irregulares == 1:
                        errores.append(
                            f"{rel}:{numero}: {len(fila)} campos, se esperan "
                            f"{len(cabecera)}"
                        )
                elif cabecera[0].endswith("_id"):
                    if fila[0] in identificadores:
                        duplicados += 1
                    identificadores.add(fila[0])

            if duplicados:
                errores.append(f"{rel}: {duplicados} identificador(es) duplicado(s)")

    print(f"conjuntos de datos: {len(archivos)}")
    print(f"fichas:             {len(documentacion)}")

    if errores:
        print(f"\n{len(errores)} problema(s):")
        for item in errores[:40]:
            print(f"  - {item}")
        if len(errores) > 40:
            print(f"  ... y {len(errores) - 40} mas")
        return 1

    print("\nConjuntos de datos documentados y coherentes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
