"""Verificador offline del registro de fuentes.

Este script no toca la red. Esa es su virtud: puede correr en cada cambio, en
cualquier máquina y sin depender de que un servidor externo esté de buen humor.
Si la comprobación de red entrara aquí, el CI empezaría a fallar por causas
ajenas al repositorio y en poco tiempo nadie miraría el resultado. La resolución
de ISBN, DOI y enlaces vive en `refresh_sources.py`, que corre aparte y **no
bloquea**.

Comprueba nueve cosas:

1. el registro parsea y cumple el esquema;
2. todo libro dado por verificado tiene ISBN-13 con dígito de control válido, y
   todo artículo, DOI;
3. el `locator` coincide con la forma canónica de su tipo;
4. toda obra citada en una clase existe en el registro;
5. ninguna entrada del registro queda sin usar;
6. ninguna cita se queda sin declarar **qué uso hace esa clase de la obra**;
7. ningún bloque de fuentes se repite entre clases;
8. las cifras que muestra el README coinciden con el recuento del registro;
9. la página `docs/fuentes.md` refleja el registro y no una copia envejecida.

Uso:
    python scripts/verify_sources.py             # verifica; falla si algo no cuadra
    python scripts/verify_sources.py --rebuild   # regenera registro, README y docs
    python scripts/verify_sources.py --stats     # imprime el recuento en JSON
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import sources_lib as S  # noqa: E402
import sources_docs as D  # noqa: E402

TIPOS = {"book", "paper", "standard", "reference", "dataset"}
ESTADOS = {"verificada", "pendiente"}
FECHA = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ID_VALIDO = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

POLITICA = (
    "Toda afirmación del programa se apoya en una entrada de este registro. "
    "Ninguna entrada se acepta sin localizador verificable: ISBN-13 para libros, "
    "DOI para artículos y URL oficial con fecha de acceso para normas y "
    "documentación. Lo que no se pudo resolver queda como pendiente, con el "
    "motivo escrito; no se borra. El ISBN-13 identifica la obra tal como la "
    "resuelve Open Library: se prefiere la edición del año citado y, cuando esa "
    "edición no declara ISBN, se registra el de otra edición de la misma obra, "
    "por lo que el campo published sigue siendo el año que cita la clase."
)

# Campos que produce la capa de red y que la reconstrucción no debe destruir.
CAMPOS_RESUELTOS = ("isbn13", "doi", "locator", "accessed", "status", "pending_reason", "http_status")


# --------------------------------------------------------------------------- #
# Localizadores
# --------------------------------------------------------------------------- #
def isbn13_valido(isbn: str) -> bool:
    """Dígito de control del ISBN-13: suma ponderada 1-3 múltiplo de diez."""
    digitos = re.sub(r"[^0-9Xx]", "", isbn or "")
    if len(digitos) != 13 or not digitos.isdigit():
        return False
    suma = sum(int(d) * (1 if i % 2 == 0 else 3) for i, d in enumerate(digitos[:12]))
    return (10 - suma % 10) % 10 == int(digitos[12])


def doi_valido(doi: str) -> bool:
    return bool(re.match(r"^10\.\d{4,9}/\S+$", (doi or "").strip()))


def locator_canonico(entrada: dict) -> str:
    tipo = entrada.get("type")
    if tipo == "book" and entrada.get("isbn13"):
        return f"https://openlibrary.org/isbn/{entrada['isbn13']}"
    if tipo == "paper" and entrada.get("doi"):
        return f"https://doi.org/{entrada['doi']}"
    return entrada.get("locator") or ""


# --------------------------------------------------------------------------- #
# Reconstrucción del registro desde las clases
# --------------------------------------------------------------------------- #
def registro_desde_clases(previo: dict | None = None) -> tuple[dict, list[str]]:
    """Deriva el registro de las citas reales, conservando lo ya resuelto."""
    resueltos = {}
    if previo:
        for entrada in previo.get("entries", []):
            resueltos[entrada["id"]] = {
                campo: entrada[campo] for campo in CAMPOS_RESUELTOS if campo in entrada
            }

    problemas: list[str] = []
    por_id: dict[str, dict] = {}
    claves_por_id: dict[str, set[str]] = defaultdict(set)
    urls_por_id: dict[str, set[str]] = defaultdict(set)

    for cita in S.lee_citas():
        if cita.interna:
            continue
        identificador = cita.id
        claves_por_id[identificador].add(cita.clave)
        if cita.url:
            urls_por_id[identificador].add(cita.url)
        entrada = por_id.get(identificador)
        if entrada is None:
            entrada = {
                "id": identificador,
                "type": cita.tipo,
                "authors": list(cita.autores),
                "title": cita.titulo,
                "published": re.sub(r"[^0-9]", "", cita.anio)[:4],
                "publisher": "" if S._parece_prosa(cita.editorial) else cita.editorial,
                "authority": cita.autoridad,
                "amendable": cita.enmendable,
                "cited_url": cita.url,
                "used_in": [],
                "status": "pendiente",
                "pending_reason": "sin resolver todavía; ejecuta scripts/refresh_sources.py",
            }
            por_id[identificador] = entrada
        if cita.clase not in entrada["used_in"]:
            entrada["used_in"].append(cita.clase)

    # Una misma obra citada con año en una clase y sin él en otra produciría dos
    # entradas. Se unen cuando la unión es inequívoca: el título sin año encaja
    # con un único año. Si encajara con varios, son ediciones distintas y se
    # dejan separadas.
    for identificador in [i for i in list(por_id) if not re.search(r"-\d{4}$", i)]:
        con_anio = [
            otro for otro in por_id
            if otro != identificador and re.fullmatch(rf"{re.escape(identificador)}-\d{{4}}", otro)
        ]
        if len(con_anio) != 1:
            continue
        destino, origen = por_id[con_anio[0]], por_id.pop(identificador)
        destino["used_in"] = sorted(set(destino["used_in"]) | set(origen["used_in"]))
        claves_por_id[con_anio[0]] |= claves_por_id.pop(identificador, set())
        urls_por_id[con_anio[0]] |= urls_por_id.pop(identificador, set())

    for identificador, claves in claves_por_id.items():
        if len(claves) > 1:
            problemas.append(
                f"dos obras distintas colisionan en el id «{identificador}»: "
                + " / ".join(sorted(claves))
            )

    # Cuando una obra se cita con varios enlaces, lo normal es que uno sea la
    # portada del organismo y otro el documento: se toma el más específico. Si
    # ninguno contiene al otro, son documentos distintos citados con el mismo
    # título, y eso hay que arreglarlo en la clase, no aquí.
    for identificador, urls in urls_por_id.items():
        if not urls or identificador not in por_id:
            continue
        elegida = max(urls, key=len)
        if any(not elegida.startswith(u) for u in urls):
            problemas.append(
                f"«{identificador}» se cita con enlaces a documentos distintos: "
                + " / ".join(sorted(urls))
            )
        por_id[identificador]["cited_url"] = elegida

    entradas = []
    for identificador in sorted(por_id):
        entrada = por_id[identificador]
        entrada["used_in"] = sorted(entrada["used_in"])
        entrada.update(resueltos.get(identificador, {}))
        entrada["locator"] = locator_canonico(entrada) or entrada.get("cited_url", "")
        if entrada["status"] == "verificada" and not entrada.get("accessed"):
            entrada["status"] = "pendiente"
            entrada["pending_reason"] = "sin fecha de acceso comprobada"
        entradas.append({k: v for k, v in entrada.items() if v not in ("", [], None)})

    registro = {
        "schema_version": 1,
        "verified_on": (previo or {}).get("verified_on", date.today().isoformat()),
        "policy": POLITICA,
        "entries": entradas,
    }
    return registro, problemas


def lee_registro() -> dict:
    if not S.REGISTRO.exists():
        return {}
    return json.loads(S.REGISTRO.read_text(encoding="utf-8"))


def escribe_registro(registro: dict) -> None:
    S.REGISTRO.parent.mkdir(parents=True, exist_ok=True)
    S.REGISTRO.write_text(
        json.dumps(registro, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n"
    )


# --------------------------------------------------------------------------- #
# Recuento
# --------------------------------------------------------------------------- #
def recuento(registro: dict) -> dict:
    entradas = registro.get("entries", [])
    citas = [c for c in S.lee_citas() if not c.interna]
    verificadas = [e for e in entradas if e.get("status") == "verificada"]
    # Cobertura del registro: cuántas de las obras que las clases citan tienen
    # entrada. Se calcula contra las citas reales, no contra el propio registro:
    # medir un archivo consigo mismo siempre da cien por cien y no dice nada.
    registradas = {e["id"] for e in entradas}
    # Una cita sin año se une a la entrada que sí lo declara, así que su obra
    # puede estar registrada bajo el id con año. Se cuenta cubierta igual.
    def cubierta(identificador: str) -> bool:
        return identificador in registradas or any(
            re.fullmatch(rf"{re.escape(identificador)}-\d{{4}}", otro) for otro in registradas
        )

    cubiertas = sum(1 for c in citas if cubierta(c.id))
    return {
        "clases": len(S.clases()),
        "citas": len(citas),
        "obras": len(entradas),
        "verificadas": len(verificadas),
        "pendientes": len(entradas) - len(verificadas),
        "cobertura_registro": round(100.0 * cubiertas / len(citas), 1) if citas else 0.0,
        "cobertura_verificada": round(100.0 * len(verificadas) / len(entradas), 1) if entradas else 0.0,
        "por_tipo": dict(sorted(Counter(e.get("type") for e in entradas).items())),
        "reguladores": len({e.get("authority") for e in entradas if e.get("amendable") or e.get("type") == "standard"}),
        "enmendables": sum(1 for e in entradas if e.get("amendable")),
        "verified_on": registro.get("verified_on", ""),
    }


# --------------------------------------------------------------------------- #
# Comprobaciones
# --------------------------------------------------------------------------- #
def comprueba(registro: dict) -> list[str]:
    fallos: list[str] = []
    hoy = date.today().isoformat()

    if registro.get("schema_version") != 1:
        fallos.append("schema_version debe ser 1")
    if not FECHA.match(registro.get("verified_on", "")):
        fallos.append("verified_on ausente o con formato no ISO")
    elif registro["verified_on"] > hoy:
        fallos.append(f"verified_on está en el futuro: {registro['verified_on']}")
    if not registro.get("policy"):
        fallos.append("falta la política del registro")

    entradas = registro.get("entries", [])
    if not entradas:
        fallos.append("el registro no tiene entradas")
        return fallos

    vistos: set[str] = set()
    for entrada in entradas:
        identificador = entrada.get("id", "")
        etiqueta = identificador or entrada.get("title", "(sin id)")
        if not ID_VALIDO.match(identificador):
            fallos.append(f"{etiqueta}: el id no está en kebab-case")
        if identificador in vistos:
            fallos.append(f"{etiqueta}: id repetido")
        vistos.add(identificador)

        if entrada.get("type") not in TIPOS:
            fallos.append(f"{etiqueta}: tipo desconocido «{entrada.get('type')}»")
        if not entrada.get("title"):
            fallos.append(f"{etiqueta}: sin título")
        if not entrada.get("authority"):
            fallos.append(f"{etiqueta}: sin organismo o editorial que responda por la fuente")
        if entrada.get("status") not in ESTADOS:
            fallos.append(f"{etiqueta}: estado desconocido «{entrada.get('status')}»")
        if not entrada.get("used_in"):
            fallos.append(f"{etiqueta}: entrada del registro que ninguna clase usa")

        if entrada.get("isbn13") and not isbn13_valido(entrada["isbn13"]):
            fallos.append(f"{etiqueta}: ISBN-13 con dígito de control inválido")
        if entrada.get("doi") and not doi_valido(entrada["doi"]):
            fallos.append(f"{etiqueta}: DOI con forma inválida")

        if entrada.get("status") == "verificada":
            tipo = entrada.get("type")
            locator = entrada.get("locator", "")
            if tipo == "book":
                if not entrada.get("isbn13"):
                    fallos.append(f"{etiqueta}: libro verificado sin ISBN-13")
                elif locator != f"https://openlibrary.org/isbn/{entrada['isbn13']}":
                    fallos.append(f"{etiqueta}: el locator no es la forma canónica de un ISBN")
            elif tipo == "paper":
                if not entrada.get("doi"):
                    fallos.append(f"{etiqueta}: artículo verificado sin DOI")
                elif locator != f"https://doi.org/{entrada['doi']}":
                    fallos.append(f"{etiqueta}: el locator no es la forma canónica de un DOI")
            elif not locator.startswith("https://"):
                fallos.append(f"{etiqueta}: norma o documentación verificada sin URL https")
            if not FECHA.match(entrada.get("accessed", "")):
                fallos.append(f"{etiqueta}: verificada sin fecha de acceso")
            elif entrada["accessed"] > hoy:
                fallos.append(f"{etiqueta}: fecha de acceso en el futuro")
        elif not entrada.get("pending_reason"):
            fallos.append(f"{etiqueta}: pendiente sin motivo declarado")

        for ruta in entrada.get("used_in", []):
            if not (S.ROOT / ruta).exists():
                fallos.append(f"{etiqueta}: usa una clase que no existe ({ruta})")

    esperado, problemas = registro_desde_clases(registro)
    fallos.extend(problemas)

    ids_registro = {e["id"] for e in entradas}
    ids_clases = {e["id"] for e in esperado["entries"]}
    for sobra in sorted(ids_registro - ids_clases):
        fallos.append(f"{sobra}: está en el registro pero ninguna clase la cita")
    for falta in sorted(ids_clases - ids_registro):
        fallos.append(f"{falta}: la citan las clases y no está en el registro")

    usos_registro = {e["id"]: e.get("used_in", []) for e in entradas}
    for entrada in esperado["entries"]:
        if entrada["id"] in usos_registro and usos_registro[entrada["id"]] != entrada["used_in"]:
            fallos.append(f"{entrada['id']}: la lista de clases que la usan está desfasada")

    fallos.extend(comprueba_citas())
    fallos.extend(comprueba_bloques())
    fallos.extend(D.comprueba_documentos(recuento(registro), registro))
    return fallos


def comprueba_citas() -> list[str]:
    """Cada cita tiene que decir qué uso hace esa clase de la obra."""
    fallos = []
    for cita in S.lee_citas():
        if cita.interna:
            continue
        if len(cita.uso) < D.USO_MINIMO:
            fallos.append(f"{cita.clase}: la cita «{cita.titulo[:50]}» no declara qué uso hace la clase")
    return fallos


def comprueba_bloques() -> list[str]:
    """Dos clases con el mismo bloque de fuentes citan sin haber leído."""
    fallos = []
    firmas: dict[str, str] = {}
    for archivo in S.clases():
        firma = S.firma_bloque(archivo.read_text(encoding="utf-8"))
        ruta = S.ruta_relativa(archivo)
        if firma in firmas:
            fallos.append(f"{ruta}: repite el bloque de fuentes de {firmas[firma]}")
        else:
            firmas[firma] = ruta
    return fallos


# --------------------------------------------------------------------------- #
def main() -> int:
    analizador = argparse.ArgumentParser(description=__doc__)
    analizador.add_argument("--rebuild", action="store_true", help="regenera registro y documentos")
    analizador.add_argument("--stats", action="store_true", help="imprime el recuento en JSON")
    opciones = analizador.parse_args()

    if opciones.rebuild:
        registro, problemas = registro_desde_clases(lee_registro())
        escribe_registro(registro)
        D.escribe_documentos(recuento(registro), registro)
        for problema in problemas:
            print(f"AVISO  {problema}")
        print(f"Registro reconstruido: {len(registro['entries'])} obras en {S.REGISTRO.relative_to(S.ROOT)}")
        return 1 if problemas else 0

    registro = lee_registro()
    if not registro:
        print("FALLO  no existe sources/bibliography.json; ejecuta --rebuild")
        return 1

    if opciones.stats:
        print(json.dumps(recuento(registro), ensure_ascii=False, indent=2))
        return 0

    fallos = comprueba(registro)
    numeros = recuento(registro)
    if fallos:
        for fallo in fallos[:80]:
            print(f"FALLO  {fallo}")
        if len(fallos) > 80:
            print(f"...y {len(fallos) - 80} incidencias más")
        print(f"\n{len(fallos)} incidencias sobre {numeros['obras']} obras.")
        return 1

    print(
        f"OK  {numeros['obras']} obras registradas, {numeros['citas']} citas en "
        f"{numeros['clases']} clases; {numeros['verificadas']} verificadas y "
        f"{numeros['pendientes']} pendientes (revalidación {numeros['verified_on']})."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
