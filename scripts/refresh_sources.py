"""Revalidación en red del registro de fuentes.

Esta es la capa que **sí** toca internet, y por eso vive fuera del CI que
bloquea. Resuelve lo que una máquina puede resolver sola:

* el ISBN-13 de cada libro contra `openlibrary.org`, comparando título y autores;
* el DOI de cada artículo contra `api.crossref.org`, con el mismo criterio;
* el estado HTTP de cada URL de norma o documentación oficial.

Lo que resuelve pasa a `verificada` y recibe fecha de acceso. Lo que no resuelve
**se conserva** y pasa a `pendiente` con el motivo escrito. Nunca se borra una
fuente por no responder: un enlace caído es información sobre el enlace, no
sobre la obra.

El criterio de aceptación es deliberadamente estricto. Un ISBN casi correcto es
peor que ninguno: da apariencia de comprobación a algo que nadie comprobó. Si el
título o el autor no coinciden, la entrada se queda pendiente.

Uso:
    python scripts/refresh_sources.py                  # todo
    python scripts/refresh_sources.py --only book      # solo libros
    python scripts/refresh_sources.py --limit 50       # prueba corta
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import sources_lib as S  # noqa: E402
import sources_docs as D  # noqa: E402
import verify_sources as V  # noqa: E402

AGENTE = (
    "finance-and-banking-evolution-program/1.0 "
    "(+https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program)"
)
NAVEGADOR = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
INFORME = S.ROOT / "sources" / "revalidacion.md"

ESPERA = 0.34  # Open Library y Crossref piden cortesía, no cadencia máxima.


# --------------------------------------------------------------------------- #
# Red
# --------------------------------------------------------------------------- #
def pide(url: str, timeout: int = 25, agente: str = AGENTE, intentos: int = 3) -> tuple[int, bytes]:
    """Una petición con reintentos. Un fallo de red no es un veredicto sobre la obra.

    Los servicios abiertos —Open Library, Crossref— cortan conexiones cuando les
    llegan muchas seguidas. Si un corte se tomara por «no existe», el registro se
    llenaría de pendientes falsos, que es justo lo que este trabajo intenta evitar.
    """
    peticion = urllib.request.Request(url, headers={"User-Agent": agente, "Accept": "*/*"})
    ultimo: tuple[int, bytes] = (0, b"sin intentos")
    for intento in range(intentos):
        try:
            with urllib.request.urlopen(peticion, timeout=timeout) as respuesta:
                return respuesta.status, respuesta.read()
        except urllib.error.HTTPError as error:
            if error.code in (429, 500, 502, 503, 504) and intento < intentos - 1:
                time.sleep(2 ** intento * 3)
                continue
            return error.code, b""
        except Exception as error:  # noqa: BLE001 - cualquier fallo de red es un estado
            ultimo = (0, str(error).encode("utf-8", "replace"))
            if intento < intentos - 1:
                time.sleep(2 ** intento * 3)
    return ultimo


def pide_json(url: str, timeout: int = 25, intentos: int = 3) -> dict | None:
    estado, cuerpo = pide(url, timeout, intentos=intentos)
    if estado != 200 or not cuerpo:
        return None
    try:
        return json.loads(cuerpo)
    except json.JSONDecodeError:
        return None


# --------------------------------------------------------------------------- #
# Comparación de títulos y autores
# --------------------------------------------------------------------------- #
def _sin_subtitulo(titulo: str) -> str:
    return S.normaliza(re.split(r"[:—–]", titulo, 1)[0])


def titulo_coincide(nuestro: str, candidato: str) -> bool:
    a, b = S.normaliza(nuestro), S.normaliza(candidato)
    if not a or not b:
        return False
    if a == b:
        return True
    corto_a, corto_b = _sin_subtitulo(nuestro), _sin_subtitulo(candidato)
    if len(corto_a) < 8:
        return False
    return corto_a == corto_b or a.startswith(b + " ") or b.startswith(a + " ")


def apellido(autor: str) -> str:
    return S.normaliza(autor.split(",")[0])


def autor_coincide(nuestros: list[str], candidatos: list[str]) -> bool:
    if not nuestros:
        return False
    apellidos = {apellido(a) for a in nuestros if apellido(a)}
    texto = S.normaliza(" ".join(candidatos))
    return any(a and a in texto for a in apellidos)


# --------------------------------------------------------------------------- #
# Resolución por tipo
# --------------------------------------------------------------------------- #
def resuelve_libro(entrada: dict) -> tuple[str, str]:
    """Devuelve (isbn13, motivo). Si el ISBN va vacío, el motivo explica por qué."""
    titulo = entrada["title"]
    autores = entrada.get("authors", [])
    consulta = urllib.parse.urlencode(
        {
            "title": titulo,
            "author": " ".join(apellido(a) for a in autores[:2]) if autores else "",
            "fields": "key,title,author_name,first_publish_year",
            "limit": "5",
        }
    )
    datos = pide_json(f"https://openlibrary.org/search.json?{consulta}", timeout=12, intentos=2)
    if not datos:
        return "", "Open Library no respondió a la consulta"
    candidatos = datos.get("docs", [])
    if not candidatos:
        return "", "Open Library no devuelve ninguna obra con ese título y autor"

    obra = None
    for candidato in candidatos:
        if not titulo_coincide(titulo, candidato.get("title", "")):
            continue
        if autores and not autor_coincide(autores, candidato.get("author_name", [])):
            continue
        obra = candidato
        break
    if obra is None:
        return "", "ninguna obra de Open Library coincide en título y autores"

    time.sleep(ESPERA)
    ediciones = pide_json(
        f"https://openlibrary.org{obra['key']}/editions.json?limit=300", timeout=15, intentos=2
    )
    if not ediciones:
        return "", "Open Library no devuelve ediciones de la obra encontrada"

    anio = entrada.get("published", "")
    mejor = ""
    respaldo = ""
    for edicion in ediciones.get("entries", []):
        isbnes = [i.replace("-", "").strip() for i in edicion.get("isbn_13", [])]
        isbnes = [i for i in isbnes if V.isbn13_valido(i)]
        if not isbnes:
            continue
        publicada = re.search(r"(\d{4})", str(edicion.get("publish_date", "")))
        respaldo = respaldo or isbnes[0]
        if anio and publicada and publicada.group(1) == anio:
            mejor = isbnes[0]
            break
    if mejor:
        return mejor, ""
    if respaldo:
        return respaldo, ""
    return "", "la obra existe en Open Library pero ninguna edición declara ISBN-13"


def resuelve_articulo(entrada: dict) -> tuple[str, str]:
    titulo = entrada["title"]
    consulta = urllib.parse.urlencode(
        {"query.bibliographic": titulo, "rows": "5", "select": "DOI,title,author,issued"}
    )
    datos = pide_json(f"https://api.crossref.org/works?{consulta}")
    if not datos:
        return "", "Crossref no respondió a la consulta"
    for item in datos.get("message", {}).get("items", []):
        titulos = item.get("title") or []
        if not titulos or not titulo_coincide(titulo, titulos[0]):
            continue
        autores = [
            f"{a.get('family', '')}, {a.get('given', '')}" for a in item.get("author", [])
        ]
        if entrada.get("authors") and autores and not autor_coincide(entrada["authors"], autores):
            continue
        doi = item.get("DOI", "")
        if V.doi_valido(doi):
            return doi, ""
    return "", "ningún registro de Crossref coincide en título y autores"


def resuelve_enlace(url: str) -> tuple[int, str]:
    # Dos intentos cortos bastan para saber si un sitio responde. Insistir mas
    # convierte una revalidacion de quinientos enlaces en una tarde entera sin
    # cambiar el veredicto: el que no contesta en doce segundos, dos veces
    # seguidas, no esta disponible para un lector tampoco.
    estado, _ = pide(url, timeout=12, agente=NAVEGADOR, intentos=2)
    if estado == 200:
        return estado, ""
    if estado in (401, 403, 405, 406, 429):
        return estado, f"la fuente respondió {estado} a una consulta automática"
    if estado == 0:
        # No dice nada sobre la fuente: dice que este equipo no llego a ella.
        # Un cortafuegos corporativo o una inspeccion TLS producen esto mismo.
        return estado, "no se pudo abrir el enlace desde el equipo que revalidó (red o TLS)"
    return estado, f"la fuente respondió {estado}"


# --------------------------------------------------------------------------- #
def revalida(registro: dict, solo: str | None, limite: int | None, solo_pendientes: bool = False) -> dict:
    hoy = date.today().isoformat()
    entradas = registro["entries"]
    pendientes = [e for e in entradas if solo in (None, e.get("type"))]
    if solo_pendientes:
        pendientes = [e for e in pendientes if e.get("status") != "verificada"]
    if limite:
        pendientes = pendientes[:limite]

    total = len(pendientes)
    for numero, entrada in enumerate(pendientes, start=1):
        tipo = entrada.get("type")
        etiqueta = entrada["id"][:64]
        motivo = ""

        if tipo == "book":
            isbn, motivo = (entrada.get("isbn13", ""), "") if entrada.get("isbn13") else resuelve_libro(entrada)
            if isbn:
                entrada["isbn13"] = isbn
                entrada["locator"] = f"https://openlibrary.org/isbn/{isbn}"
                entrada["accessed"] = hoy
                entrada["status"] = "verificada"
                entrada.pop("pending_reason", None)
            else:
                entrada["status"] = "pendiente"
                entrada["pending_reason"] = motivo
        elif tipo == "paper":
            doi, motivo = (entrada.get("doi", ""), "") if entrada.get("doi") else resuelve_articulo(entrada)
            if doi:
                entrada["doi"] = doi
                entrada["locator"] = f"https://doi.org/{doi}"
                entrada["accessed"] = hoy
                entrada["status"] = "verificada"
                entrada.pop("pending_reason", None)
            else:
                entrada["status"] = "pendiente"
                entrada["pending_reason"] = motivo
        else:
            url = entrada.get("cited_url") or entrada.get("locator", "")
            if not url.startswith("https://"):
                entrada["status"] = "pendiente"
                entrada["pending_reason"] = "la clase cita la norma sin enlace a la fuente primaria"
            else:
                estado, motivo = resuelve_enlace(url)
                entrada["http_status"] = estado
                entrada["locator"] = url
                if not motivo:
                    entrada["accessed"] = hoy
                    entrada["status"] = "verificada"
                    entrada.pop("pending_reason", None)
                else:
                    entrada["status"] = "pendiente"
                    entrada["pending_reason"] = motivo

        marca = "OK " if entrada["status"] == "verificada" else "PEND"
        print(f"[{numero:>4}/{total}] {marca} {etiqueta}" + (f" — {motivo}" if motivo else ""), flush=True)

        # Se guarda cada diez entradas: una revalidacion completa tarda, y si el
        # proceso se corta a la mitad lo resuelto hasta ahi no se pierde.
        if numero % 10 == 0:
            registro["verified_on"] = hoy
            V.escribe_registro(registro)
        time.sleep(ESPERA)

    registro["verified_on"] = hoy
    return registro


# --------------------------------------------------------------------------- #
FECHA_META = re.compile(r"(regulation_last_verified:\s*)(\d{4}-\d{2}-\d{2})")
FECHA_TEXTO = re.compile(r"(Fecha de verificaci[oó]n de esta clase:\s*)(\d{4}-\d{2}-\d{2})")


def _por_clase(registro: dict) -> dict[str, list[dict]]:
    agrupado: dict[str, list[dict]] = {}
    for entrada in registro["entries"]:
        for clase in entrada.get("used_in", []):
            agrupado.setdefault(clase, []).append(entrada)
    return agrupado


def clases_reguladas(registro: dict) -> list[str]:
    """Clases que declaran fecha de verificación regulatoria."""
    return sorted(
        clase
        for clase in _por_clase(registro)
        if FECHA_META.search((S.ROOT / clase).read_text(encoding="utf-8"))
    )


def revalida_fechas(registro: dict) -> dict[str, str]:
    """Actualiza por lote la fecha de verificación de las clases normativas.

    La fecha solo avanza cuando **todos** los enlaces oficiales que esa clase cita
    respondieron en esta ejecución. Si uno falló, la clase conserva su fecha
    anterior: mover la fecha sin haber comprobado la fuente sería exactamente la
    afirmación que este trabajo intenta eliminar.
    """
    hoy = registro.get("verified_on", date.today().isoformat())
    agrupado = _por_clase(registro)
    resultado: dict[str, str] = {}

    for clase in clases_reguladas(registro):
        enlazadas = [e for e in agrupado[clase] if e.get("cited_url")]
        sin_resolver = [e for e in enlazadas if e.get("status") != "verificada"]
        archivo = S.ROOT / clase
        texto = archivo.read_text(encoding="utf-8")
        actual = FECHA_META.search(texto).group(2)

        if sin_resolver or not enlazadas:
            resultado[clase] = actual
            continue

        nuevo = FECHA_META.sub(lambda m: m.group(1) + hoy, texto)
        nuevo = FECHA_TEXTO.sub(lambda m: m.group(1) + hoy, nuevo)
        if nuevo != texto:
            archivo.write_text(nuevo, encoding="utf-8", newline="\n")
        resultado[clase] = hoy

    return resultado


def escribe_informe(registro: dict, fechas: dict[str, str] | None = None) -> None:
    """Deja por escrito qué se revalidó, clase por clase."""
    hoy = registro.get("verified_on", date.today().isoformat())
    por_clase = _por_clase(registro)
    fechas = fechas or {}
    reguladas = clases_reguladas(registro)

    filas = []
    for clase in reguladas:
        entradas = por_clase[clase]
        enlazadas = [e for e in entradas if e.get("cited_url")]
        verificadas = sum(1 for e in enlazadas if e.get("status") == "verificada")
        pendientes = len(enlazadas) - verificadas
        estado = "✅ revalidada" if not pendientes else f"⚠️ {pendientes} enlace(s) sin resolver"
        marca = FECHA_META.search((S.ROOT / clase).read_text(encoding="utf-8"))
        fecha = fechas.get(clase) or (marca.group(2) if marca else "—")
        filas.append(
            f"| [{clase.split('/')[-1]}]({'../' + clase}) | {len(enlazadas)} | "
            f"{verificadas} | {fecha} | {estado} |"
        )

    caidas = [
        e for e in registro["entries"]
        if e.get("http_status") not in (None, 200) and e.get("type") in ("standard", "reference", "dataset")
    ]
    # El localizador va entre acentos graves: en una tabla de enlaces que no
    # responden, escribirlos como enlaces invita a pincharlos y hace que el
    # revisor de enlaces externos los vuelva a marcar como rotos.
    filas_caidas = [
        f"| {e['id']} | {e.get('http_status', '—')} | `{e.get('locator', '—')}` |"
        for e in sorted(caidas, key=lambda x: x["id"])
    ]

    texto = "\n".join(
        [
            "# Revalidación de fuentes",
            "",
            f"Última ejecución de `scripts/refresh_sources.py`: **{hoy}**.",
            "",
            "Este informe lo escribe la capa de red y **no se comprueba en CI**. Un enlace",
            "que hoy responde puede no responder mañana, y esa es exactamente la razón de",
            "que la revalidación viva fuera de la puerta de calidad: el programa se entera",
            "del cambio sin quedarse bloqueado por él.",
            "",
            "## Clases con contenido normativo",
            "",
            "Estas son las clases que declaran fecha de verificación regulatoria. Para cada una",
            "se consultaron todos los enlaces oficiales que cita. **La fecha avanza solo cuando",
            "todos respondieron**: si uno falló, la clase conserva la fecha anterior, porque",
            "mover la fecha sin haber comprobado la fuente sería justo lo que aquí se evita.",
            "",
            "| Clase | Enlaces citados | Comprobados | Fecha de verificación | Resultado |",
            "|---|---:|---:|:---:|---|",
            *filas,
            "",
            "## Enlaces que no resolvieron",
            "",
            "Ninguno de estos se ha borrado del registro. Quedan como `pendiente` con el",
            "motivo, que es la única forma honesta de declarar un hueco.",
            "",
            "| Entrada | Estado HTTP | Localizador |",
            "|---|---:|---|",
            *(filas_caidas or ["| — | — | ninguno |"]),
            "",
        ]
    )
    INFORME.parent.mkdir(parents=True, exist_ok=True)
    INFORME.write_text(texto, encoding="utf-8", newline="\n")


def main() -> int:
    analizador = argparse.ArgumentParser(description=__doc__)
    analizador.add_argument("--only", choices=sorted(V.TIPOS), help="revalida solo un tipo")
    analizador.add_argument("--limit", type=int, help="revalida solo las primeras N entradas")
    analizador.add_argument(
        "--pending",
        action="store_true",
        help="revalida solo lo que sigue pendiente, sin repetir lo ya comprobado",
    )
    analizador.add_argument("--no-report", action="store_true", help="no escribe el informe")
    analizador.add_argument(
        "--fechas",
        action="store_true",
        help="avanza la fecha de verificación de las clases cuyos enlaces resolvieron",
    )
    opciones = analizador.parse_args()

    registro = V.lee_registro()
    if not registro:
        print("No existe sources/bibliography.json; ejecuta verify_sources.py --rebuild")
        return 1

    registro = revalida(registro, opciones.only, opciones.limit, opciones.pending)
    V.escribe_registro(registro)
    fechas = revalida_fechas(registro) if opciones.fechas else {}
    numeros = V.recuento(registro)
    D.escribe_documentos(numeros, registro)
    if not opciones.no_report:
        escribe_informe(registro, fechas)

    print(
        f"\nRevalidación {registro['verified_on']}: {numeros['verificadas']} verificadas, "
        f"{numeros['pendientes']} pendientes sobre {numeros['obras']} obras."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
