"""Documentos que se generan desde el registro de fuentes.

La bibliografía que ve un lector se produce aquí, desde el registro. Son dos
cosas distintas y conviene no confundirlas:

* `docs/fuentes.md` es la **vista de lectura**: qué documento de qué regulador
  sostiene qué parte del programa, con su enlace. Eso es contenido.
* el README solo recibe **dos cifras** que antes estaban escritas a mano. No
  lleva tablero de trazabilidad: quien estudia el programa no necesita un
  marcador de cobertura, necesita la fuente al pie de la clase que está leyendo,
  y esa la trae cada clase.

Una cifra escrita a mano envejece en silencio: el material crece, la página
sigue diciendo lo de antes y nadie se entera hasta que alguien la comprueba. Por
eso las pocas que quedan salen del mismo recuento que usa el verificador.

Este módulo no decide nada: solo redacta lo que el registro ya dice.
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import sources_lib as S  # noqa: E402

README = S.ROOT / "README.md"
PAGINA = S.ROOT / "docs" / "fuentes.md"

# Longitud mínima de la frase que declara para qué usa la clase la obra. Doce
# caracteres no dejan pasar «Cap. 3» pero sí «Capítulo 3: anualidades».
USO_MINIMO = 12

# Emisores por los que responde el programa. El orden es el de autoridad: lo que
# sostiene una afirmación sobre capital bancario es Basilea, no un manual. Sus
# documentos encabezan la página de bibliografía porque son los que un lector
# necesita poder abrir.
EMISORES_RECTORES = (
    "Comité de Supervisión Bancaria de Basilea (BCBS)",
    "Banco de Pagos Internacionales (BIS)",
    "Comité de Pagos e Infraestructuras de Mercado (CPMI)",
    "Organización Internacional de Comisiones de Valores (IOSCO)",
    "Consejo de Estabilidad Financiera (FSB)",
    "Grupo de Acción Financiera Internacional (GAFI/FATF)",
    "Unión Europea (EUR-Lex)",
    "Comisión para el Mercado Financiero (CMF, Chile)",
    "IFRS Foundation",
    "Organización para la Cooperación y el Desarrollo Económicos (OCDE)",
    "Banco Mundial",
)

DOCUMENTOS_POR_EMISOR = 8


def parte_de(ruta: str) -> int:
    """Número de parte que el programa muestra al lector: el módulo, más uno."""
    coincidencia = re.match(r"modules/(\d+)-", ruta)
    return int(coincidencia.group(1)) + 1 if coincidencia else 0


def partes_de(entrada: dict) -> list[int]:
    return sorted({parte_de(r) for r in entrada.get("used_in", [])})


def _lista_partes(entrada: dict) -> str:
    partes = partes_de(entrada)
    return ", ".join(str(p) for p in partes)


def _miles(numero: int) -> str:
    return f"{numero:,}".replace(",", " ")


def _por_emisor(registro: dict) -> dict[str, list[dict]]:
    agrupado: dict[str, list[dict]] = defaultdict(list)
    for entrada in registro.get("entries", []):
        agrupado[entrada.get("authority", "—")].append(entrada)
    for entradas in agrupado.values():
        entradas.sort(key=lambda e: (-len(e.get("used_in", [])), e.get("title", "")))
    return agrupado


# --------------------------------------------------------------------------- #
# Bloques generados
# --------------------------------------------------------------------------- #
def bloque_pagina(numeros: dict, registro: dict) -> str:
    """La página de bibliografía: primero las obras, después el estado del registro."""
    agrupado = _por_emisor(registro)
    entradas = registro.get("entries", [])

    filas_rectoras = []
    for emisor in EMISORES_RECTORES:
        for entrada in agrupado.get(emisor, [])[:DOCUMENTOS_POR_EMISOR]:
            titulo = entrada["title"].replace("|", "\\|")
            locator = entrada.get("locator", "")
            documento = f"[{titulo}]({locator})" if locator.startswith("https://") else titulo
            marca = " 🔁" if entrada.get("amendable") else ""
            filas_rectoras.append(f"| {emisor} | {documento}{marca} | {_lista_partes(entrada)} |")

    filas_emisor = []
    for emisor, obras in sorted(agrupado.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        partes = sorted({p for o in obras for p in partes_de(o)})
        con_enlace = sum(1 for o in obras if o.get("locator", "").startswith("https://"))
        filas_emisor.append(
            f"| {emisor or '—'} | {len(obras)} | {con_enlace} | "
            f"{', '.join(str(p) for p in partes)} |"
        )

    pendientes = [e for e in entradas if e.get("status") != "verificada"]
    motivos: dict[str, int] = defaultdict(int)
    for entrada in pendientes:
        motivos[entrada.get("pending_reason", "sin motivo")] += 1
    filas_motivo = [
        f"| {motivo} | {cuenta} |"
        for motivo, cuenta in sorted(motivos.items(), key=lambda kv: -kv[1])
    ]

    lineas = [
        "## 🏛️ Los documentos que sostienen cada parte",
        "",
        "Esta es la tabla que importa: qué documento de qué regulador sostiene qué parte "
        "del programa, con el enlace a la fuente primaria. Se ordena por cuántas clases se "
        "apoyan en cada documento, y el 🔁 marca la norma cuya versión vigente puede cambiar "
        "por enmienda —Basilea, MiCA, las NIIF—, que por eso lleva fecha de revalidación.",
        "",
        "| Regulador | Documento | Partes |",
        "|---|---|---|",
        *filas_rectoras,
        "",
        "## 📚 Quién responde por cada obra",
        "",
        "El resto de la bibliografía, agrupada por quién responde por ella. **Con enlace** "
        "cuenta las obras cuyo localizador —ISBN-13, DOI o URL oficial— está en el registro; "
        "cuando una fila muestra menos, el hueco es visible a propósito.",
        "",
        "| Emisor o editorial | Obras | Con enlace | Partes |",
        "|---|---:|---:|---|",
        *filas_emisor,
        "",
        "## 🕓 Qué queda pendiente y por qué",
        "",
        "Una fuente pendiente no se borra ni se disimula: se declara. Estas son las "
        "razones por las que una entrada todavía no tiene localizador comprobado.",
        "",
        "| Motivo | Entradas |",
        "|---|---:|",
        *(filas_motivo or ["| — | 0 |"]),
        "",
        f"Última revalidación en red: **{numeros['verified_on']}**. "
        "La ejecuta `scripts/refresh_sources.py`, que resuelve ISBN contra Open Library, "
        "DOI contra Crossref y consulta cada URL oficial. Esa capa **no bloquea el CI**: "
        "si un organismo reorganiza su sitio, el programa no se rompe, se entera.",
    ]
    return "\n".join(lineas)


# --------------------------------------------------------------------------- #
# Inyección en los documentos
# --------------------------------------------------------------------------- #
def _marcadores(nombre: str) -> tuple[str, str]:
    return f"<!-- gen:{nombre}:start -->", f"<!-- gen:{nombre}:end -->"


def inyecta(texto: str, nombre: str, contenido: str) -> str:
    inicio, fin = _marcadores(nombre)
    if inicio not in texto or fin not in texto:
        raise SystemExit(f"faltan los marcadores {inicio} … {fin}")
    antes = texto.split(inicio)[0]
    despues = texto.split(fin, 1)[1]
    # Un valor de una línea vive dentro de una celda o de un párrafo: meterle
    # saltos de línea rompería la tabla que lo contiene.
    salto = "\n" if "\n" in contenido else ""
    return f"{antes}{inicio}{salto}{contenido}{salto}{fin}{despues}"


def _readme_actualizado(numeros: dict, registro: dict) -> str:
    """El README solo toma del registro las dos cifras que ya mostraba.

    No lleva tabla de trazabilidad ni marcador de cobertura. Quien lee el
    programa no necesita un tablero sobre la bibliografía: necesita la fuente
    al pie de la clase que está leyendo, y esa ya está. Lo que aquí se sustituye
    son dos números que antes se escribían a mano y envejecían solos.
    """
    texto = README.read_text(encoding="utf-8")
    texto = inyecta(texto, "fuentes-citas", f"**{_miles(numeros['citas'])}**")
    texto = inyecta(texto, "fuentes-obras", f"**{_miles(numeros['obras'])}** obras registradas")
    return texto


def _pagina_actualizada(numeros: dict, registro: dict) -> str:
    texto = PAGINA.read_text(encoding="utf-8")
    return inyecta(texto, "registro", bloque_pagina(numeros, registro))


def escribe_documentos(numeros: dict, registro: dict) -> None:
    README.write_text(_readme_actualizado(numeros, registro), encoding="utf-8", newline="\n")
    PAGINA.write_text(_pagina_actualizada(numeros, registro), encoding="utf-8", newline="\n")


def comprueba_documentos(numeros: dict, registro: dict) -> list[str]:
    fallos = []
    if README.read_text(encoding="utf-8") != _readme_actualizado(numeros, registro):
        fallos.append("README.md: las cifras de fuentes no coinciden con el registro")
    if PAGINA.read_text(encoding="utf-8") != _pagina_actualizada(numeros, registro):
        fallos.append("docs/fuentes.md: la vista del registro está desfasada")
    return fallos
