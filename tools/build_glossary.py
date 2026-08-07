"""Genera el glosario maestro del programa desde las tablas de conceptos.

Cada clase declara sus conceptos centrales con una comprension verificable. Ese
material ya existe, esta verificado por `validate_program.py` y se actualiza con
cada clase; el problema es que esta repartido en 352 archivos y un termino no se
puede buscar.

Este generador lo reune en un solo documento alfabetico. No inventa
definiciones: toma la que la clase ya declaro y anade donde se estudia el
termino. Cuando un termino aparece en varias clases, recoge todas sus
apariciones, y eso hace visible algo que archivo a archivo no se ve: los
terminos que se definen en varias partes y podrian estar diciendo cosas
distintas.

Las entradas ampliadas —con ejemplo y con lo que hay que tener en cuenta— viven
en `docs/glosario-maestro-ampliado.yml` y se inyectan aqui. Son las de los
terminos transversales, que son los que de verdad se buscan.

Uso:
    python tools/build_glossary.py            # genera docs/glosario-maestro.md
    python tools/build_glossary.py --check    # verifica que este al dia
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULES = ROOT / "modules"
SALIDA = ROOT / "docs" / "glosario-maestro.md"
AMPLIADO = ROOT / "docs" / "glosario-maestro-ampliado.yml"

FILA = re.compile(r"^\|\s*`?([^`|]+?)`?\s*\|\s*(.+?)\s*\|\s*$", re.M)
SECCION = re.compile(r"^##\s+(.*)$", re.M)


def sin_tildes(texto: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", texto.lower())
        if unicodedata.category(c) != "Mn"
    )


def conceptos_de(archivo: Path) -> tuple[int, int, list[tuple[str, str]]]:
    texto = archivo.read_text(encoding="utf-8")
    parte = int(re.search(r"^part:\s*(\d+)", texto, re.M).group(1))
    clase = int(re.search(r"^class:\s*(\d+)", texto, re.M).group(1))
    pos = [(m.start(), m.end(), m.group(1)) for m in SECCION.finditer(texto)]
    cuerpo = ""
    for i, (_, fin, titulo) in enumerate(pos):
        if "Conceptos centrales" in titulo:
            corte = pos[i + 1][0] if i + 1 < len(pos) else len(texto)
            cuerpo = texto[fin:corte]
            break
    filas = []
    for fila in FILA.finditer(cuerpo):
        nombre = fila.group(1).strip()
        if nombre in ("Concepto", "") or set(nombre) <= set("-: "):
            continue
        filas.append((nombre, fila.group(2).strip()))
    return parte, clase, filas


def recolectar() -> dict[str, list[tuple[int, int, str, str, str]]]:
    """termino normalizado -> [(parte, clase, nombre, definicion, ruta)]"""
    entradas: dict[str, list[tuple[int, int, str, str, str]]] = defaultdict(list)
    for modulo in sorted(MODULES.iterdir()):
        clases = modulo / "classes"
        if not clases.is_dir():
            continue
        for archivo in sorted(clases.glob("*.md")):
            parte, clase, filas = conceptos_de(archivo)
            ruta = f"../{modulo.name}/classes/{archivo.name}".replace(
                "../", "../modules/", 1
            )
            for nombre, definicion in filas:
                entradas[nombre.lower()].append(
                    (parte, clase, nombre, definicion, ruta)
                )
    return entradas


def leer_ampliado() -> dict[str, dict[str, str]]:
    """Lee el YAML de entradas ampliadas sin depender de PyYAML.

    El formato es deliberadamente simple —clave, y debajo `ejemplo:` y
    `considerar:` en una linea cada uno— para que el generador no necesite
    ninguna dependencia y el archivo se pueda revisar en un diff.
    """
    if not AMPLIADO.exists():
        return {}
    ampliado: dict[str, dict[str, str]] = {}
    actual = None
    for linea in AMPLIADO.read_text(encoding="utf-8").splitlines():
        if not linea.strip() or linea.lstrip().startswith("#"):
            continue
        if not linea.startswith(" "):
            actual = linea.rstrip(":").strip().strip('"').lower()
            ampliado[actual] = {}
        elif actual:
            clave, _, valor = linea.strip().partition(":")
            ampliado[actual][clave.strip()] = valor.strip().strip('"')
    # Se indexa tambien sin tildes: el YAML se escribe en ASCII para que sea
    # facil de teclear, y los terminos del programa llevan tilde.
    return {sin_tildes(k): v for k, v in ampliado.items()}


CABECERA = """<!-- portada:inicio -->
<div align="center">

# 📖 Glosario maestro

**Todos los conceptos centrales del programa en un solo documento, con su definicion y la clase donde se estudian.**

[![terminos](https://img.shields.io/badge/t%C3%A9rminos-{terminos}-7c5cff?style=flat-square)](glosario-maestro.md)
[![transversales](https://img.shields.io/badge/transversales-{ampliados}%20con%20ejemplo-2e8b57?style=flat-square)](glosario-maestro.md)
[![generado por](https://img.shields.io/badge/generado%20por-build__glossary.py-007c83?style=flat-square)](https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/blob/main/tools/build_glossary.py)

[⬅️ Documentación](README.md) ·
[🏠 Inicio](../README.md) ·
[📗 Glosario general](glosario.md) ·
[📘 Finanzas digitales](glosario-finanzas-digitales.md) ·
[🧮 Formulario](formulas.md)

</div>
<!-- portada:fin -->

---

Todos los conceptos centrales del programa en un solo documento, ordenados
alfabéticamente. Cada entrada trae la definición que declara la clase donde se
estudia, y un enlace para leerla completa.

Este documento **se genera** desde las tablas de conceptos de las {clases}
clases: no se escribe a mano y no puede desviarse de lo que el programa enseña.
Si una definición cambia en una clase, cambia aquí en la siguiente ejecución de
`python tools/build_glossary.py`.

## 🧭 Cómo se usa

Un término se busca aquí y se estudia en su clase. Las entradas indican **dónde
se estudia**, y cuando el término aparece en varias clases las recogen todas, en
orden: la primera es donde se introduce y las siguientes lo desarrollan o lo
aplican en otro contexto.

Las entradas marcadas con **⭐** son las transversales —las que aparecen en tres
o más clases de partes distintas— y llevan además un ejemplo y una advertencia
de uso. Son los términos que se buscan de verdad, y los que más se confunden
precisamente porque significan algo ligeramente distinto en cada parte.

> **Aviso.** Este glosario es material formativo. Las definiciones son
> operativas y están orientadas a la comprensión, no son definiciones legales.
> Toda norma citada en el programa debe verificarse en su fuente oficial
> vigente antes de cualquier uso profesional.

## 🔤 Índice alfabético

"""

PIE = """
---

<div align="center">

[⬅️ Documentación](README.md) · [🏠 Inicio](../README.md) ·
[📗 Glosario general](glosario.md) ·
[📘 Finanzas digitales](glosario-finanzas-digitales.md) ·
[🧮 Formulario](formulas.md) ·
[📚 Programa](../SYLLABUS.md)

</div>
"""


def documento() -> str:
    entradas = recolectar()
    ampliado = leer_ampliado()
    total_clases = sum(
        len(list((m / "classes").glob("*.md")))
        for m in MODULES.iterdir() if m.is_dir()
    )

    ordenadas = sorted(entradas.items(), key=lambda kv: sin_tildes(kv[0]))
    letras: dict[str, list[tuple[str, list]]] = defaultdict(list)
    for clave, apariciones in ordenadas:
        inicial = sin_tildes(clave)[:1].upper()
        if not inicial.isalpha():
            inicial = "#"
        letras[inicial].append((clave, apariciones))

    n_ampliados = sum(1 for clave in entradas if sin_tildes(clave) in ampliado)
    piezas = [
        CABECERA.format(
            clases=total_clases, terminos=len(entradas), ampliados=n_ampliados
        )
    ]
    orden_letras = sorted(letras, key=lambda x: (x == "#", x))
    piezas.append(" · ".join(f"[{ltr}](#{ltr.lower() if ltr != '#' else 'otros'})"
                             for ltr in orden_letras))
    piezas.append("")
    piezas.append(
        f"**{len(ordenadas)} términos** de las {total_clases} clases del programa. "
        f"**{sum(1 for _, ap in ordenadas if len({p for p, *_ in ap}) >= 3)}** son "
        "transversales y llevan entrada ampliada."
    )

    for letra in orden_letras:
        ancla = letra.lower() if letra != "#" else "otros"
        titulo = letra if letra != "#" else "Otros"
        piezas.append(f'\n<h2 id="{ancla}">{titulo}</h2>\n')
        for clave, apariciones in letras[letra]:
            apariciones = sorted(apariciones)
            nombre = apariciones[0][2]
            transversal = len({p for p, *_ in apariciones}) >= 3
            marca = " ⭐" if transversal else ""
            piezas.append(f"### {nombre}{marca}\n")
            piezas.append(f"- **Definición.** {apariciones[0][3]}")
            otras = {d for _, _, _, d, _ in apariciones[1:]
                     if d != apariciones[0][3]}
            for otra in sorted(otras):
                piezas.append(f"- **También.** {otra}")
            extra = ampliado.get(sin_tildes(clave), {})
            if extra.get("ejemplo"):
                piezas.append(f"- **Ejemplo.** {extra['ejemplo']}")
            if extra.get("considerar"):
                piezas.append(f"- **A considerar.** {extra['considerar']}")
            donde = " · ".join(
                f"[{p}.{c}]({r})" for p, c, _, _, r in apariciones
            )
            piezas.append(f"- **Dónde se estudia.** {donde}")
            piezas.append("")

    piezas.append(PIE)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(piezas)).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="solo verifica")
    args = parser.parse_args()

    nuevo = documento()
    if args.check:
        actual = SALIDA.read_text(encoding="utf-8") if SALIDA.exists() else ""
        if actual.replace("\r\n", "\n") != nuevo:
            print("glosario-maestro.md esta desactualizado. Ejecuta: "
                  "python tools/build_glossary.py")
            return 1
        print("glosario-maestro.md refleja los conceptos reales del programa")
        return 0

    SALIDA.write_text(nuevo, encoding="utf-8")
    terminos = nuevo.count("\n### ")
    print(f"docs/glosario-maestro.md: {terminos} terminos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
