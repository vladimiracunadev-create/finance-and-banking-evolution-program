"""Redacta las notas de una publicacion a partir del CHANGELOG.

Las notas del primer release se armaban volcando la salida cruda de
`validate_program.py` seguida de una tabla generica. Eso describe el
repositorio, no la version: quien abre un release quiere saber que cambio y
que se lleva al descargar.

El CHANGELOG ya cuenta lo primero, escrito a mano y revisado. Este script lo
extrae y le anade la lista real de artefactos publicados, con su tamano.

Uso:
    python tools/release_notes.py v2.2.1 entrega/ > notas.md
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHANGELOG = ROOT / "CHANGELOG.md"
REPO = "https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program"

# Titular de la publicacion. Es lo unico que se escribe a mano por version: el
# resto sale del CHANGELOG y de los archivos que se publican.
TITULAR = """## 📦 El paquete completo, ahora completo de verdad

La **v2.2.0** trajo la regulación con nombre propio —cuatro clases sobre MiCA, sus normas conexas y el caso de El Salvador— y la biblioteca de 26 casos. Pero su `programa-completo.zip` se armaba con una lista de carpetas escrita a mano, y esa lista nunca incluyó `case-studies/` ni `regulatory/`: el paquete se publicó sin ellas y nada falló.

**v2.2.1** lo arma desde `git ls-files` y lo verifica abriéndolo. El APK, la aplicación de Windows y el PDF de la 2.2.0 ya estaban completos.

El programa sigue en **356 clases y 534 horas**."""

# Que es cada artefacto. Los que no aparezcan aqui se listan igual, sin
# descripcion, para que anadir uno nuevo no lo deje fuera de la tabla.
ARTEFACTOS = {
    ".apk": "Aplicación de Android con las clases dentro. Instalación lateral: "
            "habilita «orígenes desconocidos» en el teléfono.",
    "-windows-": "Aplicación de Windows, portable. Descomprime y ejecuta "
                 "`FinanzasYBanca.exe`; para desinstalar, borra la carpeta.",
    "programa-completo.pdf": "El manual completo: las clases en un documento, "
                             "con marcadores en tres niveles y numeración.",
    "programa-completo.zip": "El repositorio entero: clases, documentación, "
                             "herramientas, aplicaciones y datos.",
    "solo-clases.zip": "Solo las clases y su índice, sin herramientas.",
    "sbom.json": "Inventario de dependencias en formato CycloneDX.",
    "SHA256SUMS": "Sumas de verificación de los archivos anteriores.",
}


def descripcion(nombre: str) -> str:
    for clave, texto in ARTEFACTOS.items():
        if clave in nombre or nombre.endswith(clave):
            return texto
    return ""


def seccion_del_changelog(version: str) -> str:
    """El bloque del CHANGELOG correspondiente a esta version."""
    if not CHANGELOG.exists():
        return ""
    texto = CHANGELOG.read_text(encoding="utf-8")
    numero = version.lstrip("v")
    patron = re.compile(
        rf"^## \[{re.escape(numero)}\][^\n]*\n(.*?)(?=^## \[|\Z)", re.S | re.M
    )
    encontrado = patron.search(texto)
    if not encontrado:
        return ""
    cuerpo = encontrado.group(1).strip().rstrip("-").strip()
    # La primera linea del bloque es el resumen de la version. En el release ya
    # esta dicho en el titular, asi que se retira para no decirlo dos veces.
    if not cuerpo.startswith("#"):
        _, _, cuerpo = cuerpo.partition("\n\n")
    return cuerpo.strip()


def tamano(bytes_: int) -> str:
    if bytes_ >= 1_048_576:
        return f"{bytes_ / 1_048_576:.1f} MB"
    if bytes_ >= 1024:
        return f"{bytes_ / 1024:.0f} KB"
    return f"{bytes_} B"


def tabla(directorio: Path) -> str:
    archivos = sorted(p for p in directorio.iterdir() if p.is_file())
    if not archivos:
        return ""
    filas = [
        f"| `{p.name}` | {tamano(p.stat().st_size)} | {descripcion(p.name)} |"
        for p in archivos
    ]
    return "\n".join(["| Archivo | Tamaño | Qué es |", "|---|---:|---|", *filas])


def main() -> int:
    if len(sys.argv) < 2:
        print("uso: release_notes.py <version> [directorio de artefactos]", file=sys.stderr)
        return 2
    version = sys.argv[1]
    directorio = Path(sys.argv[2]) if len(sys.argv) > 2 else None

    piezas = [TITULAR] if TITULAR else []
    cuerpo = seccion_del_changelog(version)
    if cuerpo:
        piezas.append(cuerpo)
    else:
        piezas.append(
            f"Publicación **{version}** del programa. El detalle de los cambios "
            f"está en [CHANGELOG.md]({REPO}/blob/main/CHANGELOG.md)."
        )

    if directorio and directorio.is_dir():
        filas = tabla(directorio)
        if filas:
            piezas += ["## 📦 Qué se publica", filas]

    piezas += [
        "Comprueba la integridad de lo que descargues:",
        "```bash\nsha256sum -c SHA256SUMS.txt --ignore-missing\n```",
        f"🌐 **[Portal de estudio](https://vladimiracunadev-create.github.io/"
        f"finance-and-banking-evolution-program/)** · "
        f"📚 **[Programa completo]({REPO}/blob/main/SYLLABUS.md)** · "
        f"📜 **[Historial de cambios]({REPO}/blob/main/CHANGELOG.md)**",
        "> Material formativo. No constituye asesoría financiera, tributaria ni "
        "legal. Las tasas, comisiones, límites y normas citados cambian por país "
        "y por fecha: cada clase cierra con sus fuentes y con la fecha en que se "
        "verificaron.",
    ]
    print("\n\n".join(piezas))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
