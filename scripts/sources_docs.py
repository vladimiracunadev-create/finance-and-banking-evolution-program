"""Documentos que se generan desde el registro de fuentes.

Las cifras de trazabilidad no se escriben a mano en ninguna página. Una cifra
escrita a mano envejece en silencio: el registro crece, el README sigue diciendo
lo de antes y nadie se entera hasta que alguien la comprueba. Aquí se producen
las dos vistas que ve un lector —el bloque del README y la página
`docs/fuentes.md`— a partir del mismo recuento que usa el verificador.

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
# sostiene una afirmación sobre capital bancario es Basilea, no un manual.
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

DOCUMENTOS_POR_EMISOR = 4


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
def bloque_readme(numeros: dict, registro: dict) -> str:
    agrupado = _por_emisor(registro)
    filas = []
    cubiertos = 0
    for emisor in EMISORES_RECTORES:
        entradas = agrupado.get(emisor, [])
        cubiertos += len(entradas)
        for entrada in entradas[:DOCUMENTOS_POR_EMISOR]:
            titulo = entrada["title"].replace("|", "\\|")
            locator = entrada.get("locator", "")
            documento = f"[{titulo}]({locator})" if locator.startswith("https://") else titulo
            marca = " 🔁" if entrada.get("amendable") else ""
            filas.append(f"| {emisor} | {documento}{marca} | {_lista_partes(entrada)} |")

    restantes = numeros["obras"] - cubiertos
    organismos = len({e.get("authority") for e in registro.get("entries", [])})

    lineas = [
        "## 📗 Trazabilidad de fuentes",
        "",
        "Toda afirmación del programa se apoya en una obra registrada. El registro "
        "es un archivo, no una promesa: **[sources/bibliography.json](sources/bibliography.json)** "
        "guarda cada obra con su emisor, su localizador y la fecha en que se comprobó, "
        "y **[scripts/verify_sources.py](scripts/verify_sources.py)** falla en CI si una clase "
        "cita algo que no está registrado o si una entrada del registro dejó de usarse.",
        "",
        f"| 📚 Obras registradas | 📎 Citas en clase | ✅ Con localizador comprobado | "
        f"🕓 Pendientes | 🏛️ Organismos | 🔁 Normas revalidables |",
        "|:---:|:---:|:---:|:---:|:---:|:---:|",
        f"| **{_miles(numeros['obras'])}** | **{_miles(numeros['citas'])}** | "
        f"**{_miles(numeros['verificadas'])}** | **{_miles(numeros['pendientes'])}** | "
        f"**{organismos}** | **{_miles(numeros['enmendables'])}** |",
        "",
        f"**Cobertura del registro: {numeros['cobertura_registro']} %.** Es decir: de todas "
        f"las obras que las {numeros['clases']} clases citan, esa proporción tiene entrada "
        f"propia en el registro. De ellas, **{numeros['cobertura_verificada']} %** tiene además "
        "el localizador resuelto contra su fuente.",
        "",
        "Las cifras de esta tabla las produce el verificador; no se escriben a mano. "
        "«Pendiente» no significa dudosa: significa que su localizador todavía no se "
        "resolvió contra la fuente y que el hueco está declarado en vez de disimulado. "
        "Un hueco declarado es información; un hueco rellenado por intuición sería una "
        "invención con formato de bibliografía.",
        "",
        "### Documentos rectores por regulador",
        "",
        "Estos son los documentos que más veces sostienen una afirmación del programa. "
        "El 🔁 marca la norma cuya versión vigente puede cambiar por enmienda, y que por "
        "eso se revalida con fecha.",
        "",
        "| Regulador | Documento | Partes |",
        "|---|---|---|",
        *filas,
        "",
        f"Y {_miles(restantes)} obras más de {organismos} organismos y editoriales, "
        f"con el detalle completo en el registro y la vista de lectura en "
        f"**[docs/fuentes.md](docs/fuentes.md)**. Última revalidación en red: "
        f"**{numeros['verified_on']}**.",
    ]
    return "\n".join(lineas)


def bloque_pagina(numeros: dict, registro: dict) -> str:
    agrupado = _por_emisor(registro)
    entradas = registro.get("entries", [])

    filas_emisor = []
    for emisor, obras in sorted(agrupado.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        partes = sorted({p for o in obras for p in partes_de(o)})
        verificadas = sum(1 for o in obras if o.get("status") == "verificada")
        filas_emisor.append(
            f"| {emisor or '—'} | {len(obras)} | {verificadas} | "
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
        "## 🧾 El registro en cifras",
        "",
        f"El programa cita **{_miles(numeros['citas'])} veces** un total de "
        f"**{_miles(numeros['obras'])} obras** a lo largo de sus "
        f"**{numeros['clases']} clases**. De esas obras, "
        f"**{_miles(numeros['verificadas'])}** tienen hoy un localizador comprobado "
        f"—ISBN-13, DOI o URL oficial con fecha de acceso— y "
        f"**{_miles(numeros['pendientes'])}** siguen pendientes de resolver.",
        "",
        "El detalle está en **[sources/bibliography.json](../sources/bibliography.json)**, "
        "que es la fuente de verdad. Esta página es su vista de lectura: agrupa por quién "
        "responde por cada obra y en qué partes del programa se apoya.",
        "",
        "| Tipo | Obras | Localizador que exige |",
        "|---|---:|---|",
        f"| Libro | {numeros['por_tipo'].get('book', 0)} | ISBN-13 con dígito de control válido |",
        f"| Artículo | {numeros['por_tipo'].get('paper', 0)} | DOI |",
        f"| Norma o documento oficial | {numeros['por_tipo'].get('standard', 0)} | URL https de la fuente primaria, con fecha de acceso |",
        f"| Referencia | {numeros['por_tipo'].get('reference', 0)} | URL https de la fuente primaria, con fecha de acceso |",
        "",
        "El ISBN-13 se resuelve contra Open Library comparando título y autores, y se "
        "prefiere la edición del año que cita la clase. Cuando esa edición concreta no "
        "declara ISBN, se registra el de otra edición de la misma obra: el localizador "
        "lleva al libro correcto, y el año que aparece en el registro sigue siendo el "
        "que cita la clase. Cuando ni título ni autores coinciden con seguridad, la "
        "entrada se queda pendiente antes que arriesgar un ISBN casi correcto, que es "
        "peor que ninguno porque aparenta una comprobación que nadie hizo.",
        "",
        "## 🏛️ Quién responde por cada obra",
        "",
        "La columna **Comprobadas** dice cuántas de esas obras tienen hoy el localizador "
        "resuelto contra su fuente. Cuando una fila muestra menos comprobadas que obras, "
        "el hueco es visible a propósito.",
        "",
        "| Emisor o editorial | Obras | Comprobadas | Partes |",
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
    texto = README.read_text(encoding="utf-8")
    texto = inyecta(texto, "fuentes", bloque_readme(numeros, registro))
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
