"""Genera el portal de estudio a partir del Markdown del repositorio.

El programa se puede recorrer entero leyendo los archivos en GitHub. El portal
existe para quien prefiere leerlo como un sitio: navegacion entre clases,
buscador del indice y diagramas renderizados.

El sitio ESPEJA la estructura del repositorio: cada `X.md` produce un `X.html`
en la misma ruta relativa. Asi los enlaces entre documentos siguen funcionando
cambiando solo la extension, sin recalcular rutas.

Uso:
    python tools/build_site.py            # genera site/
    python tools/build_site.py --check    # verifica que el sitio sea generable
"""

from __future__ import annotations

import argparse
import html
import re
import shutil
import sys
from pathlib import Path

try:
    import markdown
except ImportError:  # pragma: no cover - solo ocurre sin requirements-site
    print("Falta la dependencia 'markdown'. Instala: pip install -r requirements-site.txt")
    raise SystemExit(1)

ROOT = Path(__file__).resolve().parents[1]
SALIDA = ROOT / "site"

EXCLUIDOS = {".git", ".github", "node_modules", ".venv", "site", "book", ".pytest_cache", "__pycache__"}

TITULO = "Finance & Banking Evolution Program"
REPO = "https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program"


def inventario() -> tuple[int, int]:
    """Partes y clases reales. Ninguna cifra del portal se escribe a mano."""
    modules = ROOT / "modules"
    if not modules.exists():
        return 0, 0
    partes = [p for p in modules.iterdir() if p.is_dir()]
    clases = sum(len(list((p / "classes").glob("*.md"))) for p in partes)
    return len(partes), clases


PARTES, CLASES = inventario()
DESCRIPCION = (
    f"Programa abierto de {CLASES} clases que recorre finanzas, banca e "
    "infraestructura financiera digital desde cero hasta nivel profesional, "
    "con bibliografia oficial verificable."
)

# Enlaces relativos a un archivo .md, con ancla opcional.
ENLACE_MD = re.compile(r'(href=")(?!https?://|mailto:|#)([^"]+?)\.md((?:#[^"]*)?)(")')

# Bloques mermaid en el origen. Se extraen antes de convertir, porque el
# resaltador de codigo los envolveria y el navegador ya no los reconoceria.
MERMAID = re.compile(r"^```mermaid[ \t]*\n(.*?)^```[ \t]*$", re.S | re.M)


def archivos_markdown() -> list[Path]:
    encontrados: list[Path] = []
    for ruta in ROOT.rglob("*.md"):
        if any(parte in EXCLUIDOS for parte in ruta.relative_to(ROOT).parts):
            continue
        encontrados.append(ruta)
    return sorted(encontrados)


ENLACE_RELATIVO = re.compile(r"\[[^\]]*\]\((?!https?://|mailto:|#)([^)]+)\)")


def adjuntos_enlazados() -> list[Path]:
    """Archivos que NO son Markdown y que algun documento enlaza.

    El portal convierte cada `.md` en `.html`, pero un enlace a un contrato
    OpenAPI, a una ficha normativa o a un modulo de Python apunta a un archivo
    que hay que copiar tal cual. Descubrirlos leyendo los enlaces evita
    mantener una lista a mano que se desactualiza en el primer enlace nuevo.
    """
    encontrados: set[Path] = set()
    for ruta in archivos_markdown():
        for destino in ENLACE_RELATIVO.findall(ruta.read_text(encoding="utf-8")):
            destino = destino.strip().split("#", 1)[0]
            if not destino or destino.endswith(".md"):
                continue
            resuelto = (ruta.parent / destino).resolve()
            if not resuelto.is_file():
                continue
            try:
                relativa = resuelto.relative_to(ROOT)
            except ValueError:
                continue
            if any(parte in EXCLUIDOS for parte in relativa.parts):
                continue
            encontrados.add(relativa)
    return sorted(encontrados)


def separar_frontmatter(texto: str) -> tuple[dict[str, str], str]:
    if not texto.startswith("---"):
        return {}, texto
    try:
        _, front, cuerpo = texto.split("---", 2)
    except ValueError:
        return {}, texto
    meta: dict[str, str] = {}
    for linea in front.strip().splitlines():
        if ":" in linea:
            clave, valor = linea.split(":", 1)
            meta[clave.strip()] = valor.strip().strip('"')
    return meta, cuerpo.lstrip("\n")


def titulo_de(meta: dict[str, str], cuerpo: str, ruta: Path) -> str:
    if meta.get("title"):
        numero = meta.get("class", "")
        return f"Clase {int(numero):02d} · {meta['title']}" if numero else meta["title"]
    for linea in cuerpo.splitlines():
        if linea.startswith("# "):
            return linea[2:].strip()
    return ruta.stem


def convertir(cuerpo: str) -> str:
    diagramas: list[str] = []

    def apartar(coincidencia: re.Match[str]) -> str:
        diagramas.append(coincidencia.group(1))
        return f"\nMERMAIDMARCA{len(diagramas) - 1}FIN\n"

    cuerpo = MERMAID.sub(apartar, cuerpo)

    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "codehilite", "sane_lists", "attr_list", "toc"],
        extension_configs={"codehilite": {"guess_lang": False, "noclasses": False}},
    )
    contenido = md.convert(cuerpo)

    # Los diagramas vuelven como bloques que el navegador renderiza.
    for indice, diagrama in enumerate(diagramas):
        contenido = contenido.replace(
            f"<p>MERMAIDMARCA{indice}FIN</p>",
            f'<pre class="mermaid">{html.escape(diagrama)}</pre>',
        )

    # Todo enlace a un .md del repositorio apunta a su .html equivalente.
    return ENLACE_MD.sub(lambda m: f"{m.group(1)}{m.group(2)}.html{m.group(3)}{m.group(4)}", contenido)


def ruta_relativa(desde: Path, hasta: Path) -> str:
    """Ruta relativa en formato URL entre dos rutas del sitio."""
    import os

    return os.path.relpath(hasta, desde.parent).replace("\\", "/")


def directorios_con_indice() -> set[Path]:
    """Directorios que tendran index.html porque contienen un README.md."""
    indices = {Path(".")}
    for ruta in archivos_markdown():
        if ruta.name == "README.md":
            indices.add(ruta.parent.relative_to(ROOT))
    return indices


def migas(relativa: Path, indices: set[Path]) -> str:
    partes = list(relativa.parts[:-1])
    if not partes:
        return ""
    subir = "../" * len(partes)
    trozos = [f'<a href="{subir}index.html">Inicio</a>']
    for i, parte in enumerate(partes):
        directorio = Path(*partes[: i + 1])
        etiqueta = html.escape(parte)
        # Solo se enlaza un directorio si tiene indice propio; el resto es
        # una etiqueta de ubicacion, no un destino.
        if directorio in indices:
            restante = "../" * (len(partes) - i - 1)
            trozos.append(f'<a href="{restante}index.html">{etiqueta}</a>')
        else:
            trozos.append(f"<span>{etiqueta}</span>")
    return " / ".join(trozos)


PLANTILLA = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo} · {sitio}</title>
<meta name="description" content="{descripcion}">
<link rel="stylesheet" href="{css}">
</head>
<body>
<a class="saltar" href="#contenido">Saltar al contenido</a>
<header class="cabecera">
  <a class="marca" href="{inicio}">Finance &amp; Banking<br><span>Evolution Program</span></a>
  <nav class="navegacion">
    <a href="{syllabus}">Programa</a>
    <a href="{estado}">Estado</a>
    <a href="{docs}">Documentación</a>
    <a href="{repo}" rel="noopener">GitHub</a>
  </nav>
</header>
<div class="migas">{migas}</div>
<main id="contenido" class="contenido">
{cuerpo}
</main>
<footer class="pie">
  <p><strong>{sitio}</strong> · {clases} clases · {partes} partes · Licencia MIT</p>
  <p>Material formativo. No constituye asesoría financiera, tributaria ni legal.
     Verifica siempre la norma vigente en tu país.</p>
  <p><a href="{repo}" rel="noopener">Ver en GitHub</a></p>
</footer>
<script type="module">
import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
const oscuro = window.matchMedia("(prefers-color-scheme: dark)").matches;
mermaid.initialize({{ startOnLoad: true, theme: oscuro ? "dark" : "default" }});
</script>
</body>
</html>
"""

CSS = """:root {
  --fondo: #ffffff;
  --texto: #1f2328;
  --suave: #59636e;
  --borde: #d1d9e0;
  --acento: #0969da;
  --codigo: #f6f8fa;
  --destacado: #f6f8fa;
  --ancho: 62rem;
}
@media (prefers-color-scheme: dark) {
  :root {
    --fondo: #0d1117;
    --texto: #e6edf3;
    --suave: #9198a1;
    --borde: #3d444d;
    --acento: #4493f8;
    --codigo: #151b23;
    --destacado: #151b23;
  }
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  background: var(--fondo);
  color: var(--texto);
  font: 16px/1.65 -apple-system, BlinkMacSystemFont, "Segoe UI", Inter, Roboto,
        "Helvetica Neue", Arial, sans-serif;
}
.saltar {
  position: absolute; left: -999px;
  background: var(--acento); color: #fff; padding: .6rem 1rem; z-index: 10;
}
.saltar:focus { left: 1rem; top: 1rem; }
.cabecera {
  display: flex; flex-wrap: wrap; gap: 1rem;
  align-items: center; justify-content: space-between;
  max-width: var(--ancho); margin: 0 auto; padding: 1.25rem 1.5rem;
  border-bottom: 1px solid var(--borde);
}
.marca {
  font-weight: 700; font-size: .95rem; line-height: 1.25;
  color: var(--texto); text-decoration: none; letter-spacing: -.01em;
}
.marca span { font-weight: 400; color: var(--suave); }
.navegacion { display: flex; flex-wrap: wrap; gap: 1.25rem; }
.navegacion a {
  color: var(--suave); text-decoration: none; font-size: .9rem; font-weight: 500;
}
.navegacion a:hover { color: var(--acento); }
.migas {
  max-width: var(--ancho); margin: 0 auto; padding: .85rem 1.5rem 0;
  font-size: .82rem; color: var(--suave);
}
.migas a { color: var(--suave); }
.contenido {
  max-width: var(--ancho); margin: 0 auto; padding: 1.5rem 1.5rem 4rem;
}
.contenido h1 {
  font-size: 2rem; line-height: 1.25; letter-spacing: -.02em;
  margin: 1.5rem 0 1rem; padding-bottom: .5rem; border-bottom: 1px solid var(--borde);
}
.contenido h2 {
  font-size: 1.4rem; margin: 2.5rem 0 .85rem;
  padding-bottom: .35rem; border-bottom: 1px solid var(--borde);
}
.contenido h3 { font-size: 1.15rem; margin: 2rem 0 .75rem; }
.contenido h4 { font-size: 1rem; margin: 1.5rem 0 .5rem; }
.contenido a { color: var(--acento); text-decoration: none; }
.contenido a:hover { text-decoration: underline; }
.contenido p, .contenido li { overflow-wrap: break-word; }
.contenido ul, .contenido ol { padding-left: 1.4rem; }
.contenido li { margin: .3rem 0; }
.contenido blockquote {
  margin: 1.25rem 0; padding: .75rem 1.1rem;
  border-left: 4px solid var(--acento); background: var(--destacado);
  border-radius: 0 6px 6px 0;
}
.contenido blockquote > :first-child { margin-top: 0; }
.contenido blockquote > :last-child { margin-bottom: 0; }
.contenido code {
  background: var(--codigo); border: 1px solid var(--borde);
  border-radius: 5px; padding: .12em .4em; font-size: .875em;
  font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
}
.contenido pre {
  background: var(--codigo); border: 1px solid var(--borde);
  border-radius: 8px; padding: 1rem; overflow-x: auto; line-height: 1.45;
}
.contenido pre code { background: none; border: 0; padding: 0; font-size: .84rem; }
.contenido pre.mermaid {
  background: transparent; border: 0; text-align: center; padding: 1rem 0;
}
.contenido table {
  width: 100%; border-collapse: collapse; margin: 1.25rem 0;
  font-size: .92rem; display: block; overflow-x: auto;
}
.contenido th, .contenido td {
  border: 1px solid var(--borde); padding: .5rem .7rem; text-align: left;
  vertical-align: top;
}
.contenido th { background: var(--destacado); font-weight: 600; }
.contenido tr:nth-child(even) td { background: color-mix(in srgb, var(--destacado) 45%, transparent); }
.contenido hr { border: 0; border-top: 1px solid var(--borde); margin: 2.5rem 0; }
.contenido img { max-width: 100%; }
.pie {
  max-width: var(--ancho); margin: 0 auto; padding: 2rem 1.5rem 3rem;
  border-top: 1px solid var(--borde); color: var(--suave); font-size: .85rem;
}
.pie p { margin: .4rem 0; }
.pie a { color: var(--acento); }
@media (max-width: 640px) {
  .cabecera { flex-direction: column; align-items: flex-start; }
  .contenido h1 { font-size: 1.6rem; }
}
"""


def generar() -> int:
    if SALIDA.exists():
        shutil.rmtree(SALIDA)
    SALIDA.mkdir(parents=True)

    (SALIDA / "assets").mkdir()
    (SALIDA / "assets" / "estilo.css").write_text(CSS, encoding="utf-8", newline="\n")
    # Evita que GitHub Pages procese el sitio con Jekyll.
    (SALIDA / ".nojekyll").write_text("", encoding="utf-8")

    # Archivos sin extension .md que la documentacion enlaza y deben viajar
    # con el sitio para que esos enlaces resuelvan. Se descubren leyendo los
    # enlaces reales en vez de mantener una lista a mano, que es lo que hacia
    # que un enlace nuevo a un contrato o a una ficha rompiera el portal.
    for relativa in adjuntos_enlazados():
        origen_extra = ROOT / relativa
        destino_extra = SALIDA / relativa
        destino_extra.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(origen_extra, destino_extra)

    indices = directorios_con_indice()
    paginas = 0
    for origen in archivos_markdown():
        relativa = origen.relative_to(ROOT)
        destino = SALIDA / relativa.with_suffix(".html")
        destino.parent.mkdir(parents=True, exist_ok=True)

        texto = origen.read_text(encoding="utf-8")
        meta, cuerpo = separar_frontmatter(texto)
        titulo = titulo_de(meta, cuerpo, origen)

        subir = "../" * (len(relativa.parts) - 1)
        pagina = PLANTILLA.format(
            titulo=html.escape(titulo),
            sitio=TITULO,
            descripcion=html.escape(DESCRIPCION),
            css=f"{subir}assets/estilo.css",
            inicio=f"{subir}index.html",
            syllabus=f"{subir}SYLLABUS.html",
            estado=f"{subir}STATUS.html",
            docs=f"{subir}docs/index.html",
            repo=REPO,
            migas=migas(relativa, indices),
            cuerpo=convertir(cuerpo),
            partes=PARTES,
            clases=CLASES,
        )
        destino.write_text(pagina, encoding="utf-8", newline="\n")
        paginas += 1

        # Un README.md tambien responde como indice de su directorio.
        if origen.name == "README.md":
            (destino.parent / "index.html").write_text(pagina, encoding="utf-8", newline="\n")
            paginas += 1

    return paginas


def verificar() -> int:
    """Comprueba que el sitio se genere y que sus enlaces internos resuelvan."""
    paginas = generar()

    faltantes: list[str] = []
    patron = re.compile(r'href="(?!https?://|mailto:|#)([^"#]+)')
    for pagina in SALIDA.rglob("*.html"):
        contenido = pagina.read_text(encoding="utf-8")
        for destino in patron.findall(contenido):
            resuelto = (pagina.parent / destino).resolve()
            if not resuelto.exists():
                faltantes.append(f"{pagina.relative_to(SALIDA)} -> {destino}")

    print(f"paginas generadas: {paginas}")
    print(f"enlaces internos revisados en {len(list(SALIDA.rglob('*.html')))} paginas")

    if faltantes:
        print(f"\n{len(faltantes)} enlace(s) roto(s) en el sitio:")
        for item in sorted(set(faltantes))[:40]:
            print(f"  - {item}")
        return 1

    print("\nEl portal se genera y todos sus enlaces internos resuelven")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="genera y verifica sin publicar")
    args = parser.parse_args()

    if args.check:
        return verificar()

    paginas = generar()
    print(f"Portal generado en site/: {paginas} paginas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
