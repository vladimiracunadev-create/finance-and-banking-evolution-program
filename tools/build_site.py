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

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent))

import argparse
import html
import re
import shutil
import sys
from pathlib import Path

import portal_extra

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

# Python-Markdown trata cualquier bloque HTML de nivel de bloque como HTML en
# crudo y no convierte lo que hay dentro. El README y los documentos usan
# `<div align="center">` para la portada y `<td>` para las columnas, asi que sin
# esto el portal servia las insignias y las tablas como texto plano. La
# extension `md_in_html` si convierte el interior, pero solo cuando el elemento
# declara `markdown="1"`; ese atributo se pone aqui y no en el Markdown, porque
# en GitHub no hace falta y ensuciaria la fuente.
ABRIR_HTML = re.compile(r"<(div|td|th|details|summary)((?:\s[^>]*)?)>")


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


# Los metadatos de una clase van en un comentario HTML y no en un bloque
# YAML: GitHub renderiza el bloque YAML como una tabla delante del titulo, y
# esos datos son para las herramientas. Aqui se separan del cuerpo para usar
# el titulo en la pagina sin volcar el resto en ella.
META_CLASE = re.compile(r"^<!--\s*meta\n(.*?)\n-->\n", re.S)


def separar_frontmatter(texto: str) -> tuple[dict[str, str], str]:
    encontrado = META_CLASE.match(texto)
    if not encontrado:
        return {}, texto
    meta: dict[str, str] = {}
    for linea in encontrado.group(1).strip().splitlines():
        if ":" in linea:
            clave, valor = linea.split(":", 1)
            meta[clave.strip()] = valor.strip().strip('"')
    return meta, texto[encontrado.end():].lstrip("\n")


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
    cuerpo = ABRIR_HTML.sub(r'<\1 markdown="1"\2>', cuerpo)

    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "codehilite", "sane_lists", "attr_list",
                    "toc", "md_in_html"],
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
<link rel="manifest" href="{manifiesto}">
<meta name="theme-color" content="#0969da">
<link rel="icon" href="{icono}" type="image/png">
</head>
<body>
<a class="saltar" href="#contenido">Saltar al contenido</a>
<header class="cabecera">
  <a class="marca" href="{inicio}">Finance &amp; Banking<br><span>Evolution Program</span></a>
  <nav class="navegacion">
    <a href="{temario}">Temario</a>
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
<script>
if ("serviceWorker" in navigator) {{
  window.addEventListener("load", function () {{
    navigator.serviceWorker.register("{sw}").catch(function () {{}});
  }});
}}
</script>
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
/* ── Portada ─────────────────────────────────────────────────────── */
.hero {
  padding: 3.5rem 0 2.5rem;
  border-bottom: 1px solid var(--borde);
  text-align: center;
}
.hero-cinta {
  display: inline-block; margin: 0 0 1.2rem;
  padding: .3rem .85rem; border-radius: 999px;
  background: var(--destacado); border: 1px solid var(--borde);
  font-size: .8rem; letter-spacing: .04em; text-transform: uppercase;
  color: var(--suave);
}
.hero h1 {
  margin: 0 0 1rem; font-size: clamp(1.9rem, 5.2vw, 3.1rem);
  line-height: 1.15; letter-spacing: -.02em;
}
.hero h1 span { color: var(--acento); }
.hero-bajada {
  max-width: 46rem; margin: 0 auto 2rem;
  font-size: 1.08rem; color: var(--suave);
}
.hero-acciones { display: flex; flex-wrap: wrap; gap: .75rem; justify-content: center; }
.contenido .boton {
  display: inline-block; padding: .7rem 1.35rem; border-radius: 8px;
  background: var(--acento); color: #fff; font-weight: 600; text-decoration: none;
  border: 1px solid transparent;
}
.contenido .boton:hover { filter: brightness(1.08); text-decoration: none; }
.contenido .boton.secundario {
  background: transparent; color: var(--texto); border-color: var(--borde);
}
.contenido .boton.secundario:hover { border-color: var(--acento); color: var(--acento); text-decoration: none; }
.cifras {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(7rem, 1fr));
  gap: 1rem; margin: 2.5rem 0 0; padding: 0;
}
.cifras div { margin: 0; }
.cifras dt { font-size: 1.65rem; font-weight: 700; letter-spacing: -.02em; }
.cifras dd {
  margin: .15rem 0 0; font-size: .82rem; color: var(--suave);
  text-transform: uppercase; letter-spacing: .05em;
}

.bloque { padding: 2.75rem 0; border-bottom: 1px solid var(--borde); }
.bloque > h2 { margin: 0 0 .6rem; font-size: 1.45rem; }
.bloque-intro { margin: 0 0 1.5rem; color: var(--suave); max-width: 52rem; }
.bloque.aviso { border-bottom: 0; }
.bloque.aviso p {
  padding: 1rem 1.15rem; border-left: 4px solid var(--acento);
  background: var(--destacado); border-radius: 0 8px 8px 0; color: var(--suave);
}

.etapas { display: grid; gap: 1rem; grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr)); }
.etapa {
  padding: 1.1rem 1.2rem; border: 1px solid var(--borde);
  border-top: 4px solid var(--color, var(--acento)); border-radius: 10px;
  background: var(--fondo);
}
.etapa h3 { margin: 0 0 .2rem; font-size: 1.05rem; }
.etapa-meta { margin: 0 0 .55rem; font-size: .8rem; color: var(--suave);
  text-transform: uppercase; letter-spacing: .04em; }
.etapa p { margin: 0; font-size: .92rem; color: var(--suave); }

.rejilla { display: grid; gap: .85rem; grid-template-columns: repeat(auto-fill, minmax(16rem, 1fr)); }
.contenido .tarjeta {
  display: flex; flex-direction: column; gap: .3rem;
  padding: 1rem 1.1rem; border: 1px solid var(--borde);
  border-left: 4px solid var(--color, var(--acento)); border-radius: 10px;
  text-decoration: none; color: inherit; background: var(--fondo);
  transition: border-color .15s, transform .15s;
}
.contenido .tarjeta:hover { border-color: var(--acento); transform: translateY(-2px); text-decoration: none; }
.tarjeta-numero, .tarjeta-nota { font-size: .78rem; color: var(--suave); }
.tarjeta-numero { text-transform: uppercase; letter-spacing: .06em; }
.tarjeta strong { font-size: 1rem; line-height: 1.3; }
.tarjeta-emoji { font-size: 1.5rem; }

/* ── Temario ─────────────────────────────────────────────────────── */
.temario-cabecera { padding: 2rem 0 1.5rem; border-bottom: 1px solid var(--borde); }
.temario-cabecera h1 { margin: 0 0 .4rem; }
.temario-cabecera p { margin: 0 0 1rem; color: var(--suave); }
#buscador {
  width: 100%; padding: .75rem 1rem; font-size: 1rem; color: var(--texto);
  background: var(--fondo); border: 1px solid var(--borde); border-radius: 8px;
}
#buscador:focus { outline: 2px solid var(--acento); outline-offset: 1px; }
.resultado { margin: .6rem 0 0 !important; font-size: .85rem; }
.vacio { padding: 2rem 0; color: var(--suave); text-align: center; }
.grupo { padding: 1.75rem 0 .5rem; border-bottom: 1px solid var(--borde); }
.grupo h2 { margin: 0 0 .2rem; font-size: 1.15rem; }
.grupo-meta { margin: 0 0 .9rem; font-size: .82rem; color: var(--suave); }
.clases { display: grid; gap: .35rem; }
.contenido .clase {
  display: grid; grid-template-columns: 2.5rem 1fr auto; gap: .75rem;
  align-items: baseline; padding: .5rem .7rem; border-radius: 7px;
  text-decoration: none; color: inherit; border: 1px solid transparent;
}
.contenido .clase:hover { background: var(--destacado); border-color: var(--borde); text-decoration: none; }
.clase-n { font-variant-numeric: tabular-nums; color: var(--color, var(--acento)); font-weight: 700; }
.clase-nivel { font-size: .75rem; color: var(--suave); text-transform: uppercase; letter-spacing: .04em; }
@media (max-width: 34rem) {
  .clase { grid-template-columns: 2.2rem 1fr; }
  .clase-nivel { display: none; }
  .cifras { grid-template-columns: repeat(3, 1fr); }
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
            manifiesto=f"{subir}manifest.webmanifest",
            icono=f"{subir}assets/icono-192.png",
            sw=f"{subir}sw.js",
            temario=f"{subir}temario.html",
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

        # Un README.md tambien responde como indice de su directorio. El de la
        # raiz no: la entrada del portal es la portada, no el README volcado.
        if origen.name == "README.md" and relativa.parent != Path("."):
            (destino.parent / "index.html").write_text(pagina, encoding="utf-8", newline="\n")
            paginas += 1

    # Portada y temario: las dos unicas paginas que no existen como archivo del
    # repositorio, porque solo tienen sentido dentro del portal.
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    modulos = [m for m in (ROOT / "modules").iterdir() if m.is_dir()]
    labs = sum(len(list((m / "labs").glob("*.md"))) for m in modulos)

    for nombre, cuerpo, titulo in (
        ("index.html",
         portal_extra.portada(CLASES, PARTES, labs, contar_fuentes(), contar_terminos()),
         TITULO),
        ("temario.html", portal_extra.temario(CLASES), "Temario completo"),
    ):
        (SALIDA / nombre).write_text(
            PLANTILLA.format(
                titulo=html.escape(titulo), sitio=TITULO,
                descripcion=html.escape(DESCRIPCION),
                css="assets/estilo.css", manifiesto="manifest.webmanifest",
                icono="assets/icono-192.png", sw="sw.js", temario="temario.html",
                inicio="index.html", syllabus="SYLLABUS.html", estado="STATUS.html",
                docs="docs/index.html", repo=REPO, migas="", cuerpo=cuerpo,
                partes=PARTES, clases=CLASES,
            ),
            encoding="utf-8", newline="\n",
        )
        paginas += 1

    portal_extra.escribir_pwa(SALIDA, version)
    return paginas


def contar_fuentes() -> int:
    """Referencias citadas al cierre de las clases, contadas sobre los archivos."""
    total = 0
    for archivo in (ROOT / "modules").glob("*/classes/*.md"):
        texto = archivo.read_text(encoding="utf-8")
        bloque = re.search(r"## 📗 Fuentes y verificación(.*?)(?=\n## |\Z)", texto, re.S)
        if bloque:
            total += len(re.findall(r"^\s*[-*0-9]", bloque.group(1), re.M))
    return total


def contar_terminos() -> int:
    glosario = ROOT / "docs" / "glosario-maestro.md"
    if not glosario.exists():
        return 0
    return len(re.findall(r"^### ", glosario.read_text(encoding="utf-8"), re.M))


def verificar() -> int:
    """Comprueba que el sitio se genere y que sus enlaces internos resuelvan."""
    paginas = generar()

    faltantes: list[str] = []
    patron = re.compile(r'href="(?!https?://|mailto:|#)([^"#]+)')
    # El manual lo genera y lo copia el flujo del portal despues de este
    # script, y ese mismo flujo comprueba sus tres URL tras el despliegue.
    aparte = ("descargas/",)
    for pagina in SALIDA.rglob("*.html"):
        contenido = pagina.read_text(encoding="utf-8")
        for destino in patron.findall(contenido):
            resuelto = (pagina.parent / destino).resolve()
            if not resuelto.exists():
                if not destino.startswith(aparte):
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
