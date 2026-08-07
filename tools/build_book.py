"""Genera el programa completo como un unico documento imprimible.

El repositorio se lee bien archivo a archivo, y el portal se recorre bien
clase a clase. Pero ninguno de los dos permite leer el programa **de corrido**,
que es la unica forma de comprobar que el hilo pedagogico se sostiene de la
primera clase a la ultima: si una parte repite lo que otra ya explico, si una
clase supone algo que todavia no se ha visto, o si un termino cambia de
significado a mitad del camino, eso solo se ve leyendo seguido.

Produce dos archivos en `book/`:

* `programa-completo.md`  el documento maestro en Markdown, para revisar y para
  cualquier conversor externo;
* `programa-completo.html` autocontenido, con hoja de estilo de impresion;
* `programa-completo.pdf`  el manual completo, impreso desde ese HTML con un
  navegador en modo headless. No hace falta instalar nada: se usa el Edge o el
  Chrome que ya esta en el sistema. Si no hay ninguno, el HTML sigue ahi y se
  imprime a mano con Ctrl+P.

Uso:
    python tools/build_book.py            # genera el Markdown, el HTML y el PDF
    python tools/build_book.py --sin-pdf  # solo Markdown y HTML (mas rapido)
    python tools/build_book.py --check    # verifica que sea generable
"""

from __future__ import annotations

import argparse
import html
import re
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import date
from pathlib import Path

try:
    import markdown
except ImportError:  # pragma: no cover - solo ocurre sin requirements-site
    print("Falta la dependencia 'markdown'. Instala: pip install -r requirements-site.txt")
    raise SystemExit(1)

ROOT = Path(__file__).resolve().parents[1]
SALIDA = ROOT / "book"
MODULES = ROOT / "modules"

TITULO = "Finance & Banking Evolution Program"
SUBTITULO = "De no saber calcular un porcentaje a dirigir un banco digital"

# Bloques generados que no aportan nada leyendo de corrido: el pie de cada
# clase repite la misma navegacion 352 veces.
GENERADO = re.compile(r"<!-- gen:(footer|header):start -->.*?<!-- gen:\1:end -->", re.S)
# Los metadatos de una clase viven en un comentario HTML para que GitHub no
# los renderice como una tabla delante del titulo. Aqui se leen y se
# descartan: en el libro no aportan nada al lector.
FRONTMATTER = re.compile(r"^<!--\s*meta\n(.*?)\n-->\n", re.S)
MERMAID = re.compile(r"```mermaid\n(.*?)```", re.S)


def frontmatter(texto: str) -> tuple[dict[str, str], str]:
    m = FRONTMATTER.match(texto)
    if not m:
        return {}, texto
    meta: dict[str, str] = {}
    for linea in m.group(1).splitlines():
        if ":" in linea:
            k, _, v = linea.partition(":")
            meta[k.strip()] = v.strip().strip('"')
    return meta, texto[m.end():]


def partes() -> list[Path]:
    return sorted(p for p in MODULES.iterdir() if p.is_dir())


def desangrar(cuerpo: str, nivel: int) -> str:
    """Baja los encabezados `nivel` niveles para que encajen en el libro."""
    def bajar(m: re.Match[str]) -> str:
        return "#" * min(6, len(m.group(1)) + nivel) + " " + m.group(2)
    fuera = []
    for i, trozo in enumerate(re.split(r"(```.*?```)", cuerpo, flags=re.S)):
        if trozo.startswith("```"):
            fuera.append(trozo)
        else:
            fuera.append(re.sub(r"^(#{1,6})\s+(.*)$", bajar, trozo, flags=re.M))
    return "".join(fuera)


def limpiar(cuerpo: str) -> str:
    cuerpo = GENERADO.sub("", cuerpo)
    # Los enlaces relativos entre archivos no significan nada dentro del libro:
    # se dejan como texto para no producir enlaces rotos al imprimir.
    cuerpo = re.sub(r"\[([^\]]+)\]\((?!https?://|#)[^)]+\.md(?:#[^)]*)?\)", r"\1", cuerpo)
    return re.sub(r"\n{3,}", "\n\n", cuerpo).strip()


ETAPAS = [
    (1, 4, "Etapa 1 — Fundamentos",
     "Para quien empieza sin base. Al terminarla se calcula un interes, se lee "
     "un estado de cuenta, se compara un credito y se reconoce un fraude."),
    (5, 8, "Etapa 2 — Analista",
     "El salto del cliente al profesional. Al terminarla se interpretan estados "
     "financieros, se entiende de donde viene una tasa y se valora un instrumento."),
    (9, 12, "Etapa 3 — Bancario",
     "El banco por dentro. Al terminarla se evalua un credito con criterio, se "
     "entiende como se mueve el dinero entre entidades y se sabe que riesgo "
     "consume capital."),
    (13, 16, "Etapa 4 — Direccion",
     "La vista del comite. Al terminarla se defiende una estrategia con numeros "
     "y se construye un banco completo de principio a fin."),
    (17, 23, "Etapa 5 — Finanzas digitales, infraestructura y mercados tokenizados",
     "La infraestructura por debajo. Llega hasta construir, operar y defender un "
     "banco digital con mercado tokenizado."),
]


def numero_de_parte(mod: Path) -> int:
    return int(mod.name.split("-")[0]) + 1


def documento() -> tuple[str, list[tuple[int, str, str]]]:
    """Devuelve el Markdown maestro y el indice (nivel, ancla, titulo)."""
    piezas: list[str] = []
    indice: list[tuple[int, str, str]] = []
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    total_clases = sum(len(list((p / "classes").glob("*.md"))) for p in partes())

    piezas.append(
        f"# {TITULO}\n\n**{SUBTITULO}**\n\n"
        f"Documento completo del programa: {len(partes())} partes y "
        f"{total_clases} clases.\n\n"
        f"Version {version} · Licencia MIT · "
        "<https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program>\n\n"
        "> **Aviso.** Material formativo. No constituye asesoria financiera, "
        "tributaria ni legal. Las tasas, comisiones, limites y normas citados "
        "cambian: verifica siempre en la fuente oficial vigente del pais donde "
        "apliques el contenido. Cada clase cierra con sus fuentes y con la fecha "
        "en que se verificaron.\n"
    )

    for desde, hasta, titulo, entrada in ETAPAS:
        ancla = "etapa-" + str(desde)
        indice.append((1, ancla, titulo))
        piezas.append(f'\n<h1 id="{ancla}" class="etapa">{html.escape(titulo)}</h1>\n\n{entrada}\n')

        for mod in partes():
            n = numero_de_parte(mod)
            if not (desde <= n <= hasta):
                continue
            readme = mod / "README.md"
            if readme.exists():
                _, cuerpo = frontmatter(readme.read_text(encoding="utf-8"))
                cuerpo = limpiar(cuerpo)
                titulo_parte = cuerpo.splitlines()[0].lstrip("# ").strip()
                ancla_p = f"parte-{n}"
                indice.append((2, ancla_p, titulo_parte))
                cuerpo = "\n".join(cuerpo.splitlines()[1:]).strip()
                piezas.append(
                    f'\n<h2 id="{ancla_p}" class="parte">{html.escape(titulo_parte)}</h2>\n\n'
                    + desangrar(cuerpo, 1)
                )

            for clase in sorted((mod / "classes").glob("*.md")):
                meta, cuerpo = frontmatter(clase.read_text(encoding="utf-8"))
                # El titulo se toma de los metadatos y no de la primera linea del
                # cuerpo: el H1 de la clase vive dentro del bloque generado que
                # `limpiar()` retira, asi que ahi la primera linea es ya la
                # primera seccion. Leerla como titulo dejaba las 352 clases
                # llamadas «Proposito» y ademas se comia esa seccion.
                cuerpo = limpiar(cuerpo).strip()
                numero = meta.get("class", "0")
                titulo_clase = f"Clase {int(numero):02d} · {meta.get('title', clase.stem)}"
                ancla_c = f"clase-{n}-{numero}"
                indice.append((3, ancla_c, titulo_clase))
                piezas.append(
                    f'\n<h3 id="{ancla_c}" class="clase">{html.escape(titulo_clase)}</h3>\n\n'
                    + desangrar(cuerpo, 2)
                )

    return "\n".join(piezas) + "\n", indice


ESTILO = """
:root { --tinta:#1b1f24; --suave:#57606a; --linea:#d8dee4; --fondo:#fff;
        --codigo:#f6f8fa; --acento:#0969da; }
* { box-sizing:border-box; }
body { margin:0; background:var(--fondo); color:var(--tinta);
  font:16px/1.65 "Iowan Old Style", Georgia, "Times New Roman", serif; }
.hoja { max-width:46rem; margin:0 auto; padding:3rem 1.5rem 6rem; }
h1,h2,h3,h4,h5,h6 { font-family:-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  line-height:1.25; margin:2.2em 0 .7em; }
h1.etapa { font-size:2.1rem; border-bottom:3px solid var(--tinta); padding-bottom:.4em;
  page-break-before:always; margin-top:0; }
h2.parte { font-size:1.65rem; border-bottom:1px solid var(--linea); padding-bottom:.3em;
  page-break-before:always; }
h3.clase { font-size:1.3rem; color:var(--acento); page-break-before:always; }
h4 { font-size:1.08rem; } h5 { font-size:1rem; color:var(--suave); }
p, li { orphans:3; widows:3; }
code, pre { font-family:"Cascadia Mono", Consolas, "SFMono-Regular", monospace; }
code { background:var(--codigo); padding:.12em .35em; border-radius:3px; font-size:.87em; }
pre { background:var(--codigo); border:1px solid var(--linea); border-radius:6px;
  padding:.9rem 1rem; overflow-x:auto; font-size:.8rem; line-height:1.45;
  page-break-inside:avoid; }
pre code { background:none; padding:0; font-size:1em; }
table { border-collapse:collapse; width:100%; margin:1.2em 0; font-size:.88rem;
  page-break-inside:avoid; }
th, td { border:1px solid var(--linea); padding:.42em .6em; text-align:left;
  vertical-align:top; }
th { background:var(--codigo); font-weight:600; }
blockquote { margin:1.2em 0; padding:.6em 1rem; border-left:4px solid var(--acento);
  background:var(--codigo); color:var(--suave); }
hr { border:0; border-top:1px solid var(--linea); margin:2.5em 0; }
a { color:var(--acento); }
.portada { text-align:center; padding:22vh 0 0; page-break-after:always; }
.portada h1 { font-size:2.6rem; border:0; margin:0 0 .3em; }
.portada .sub { font-size:1.15rem; color:var(--suave); font-style:italic; }
.portada .datos { margin-top:3rem; font-size:.9rem; color:var(--suave); }
nav.indice { page-break-after:always; }
nav.indice ol { list-style:none; padding-left:0; }
nav.indice .n2 { padding-left:1.2rem; } nav.indice .n3 { padding-left:2.6rem; font-size:.9rem; }
nav.indice a { text-decoration:none; color:var(--tinta); }
nav.indice .n1 a { font-weight:700; }
.solo-html { margin-top:1.5rem; font-size:.9rem; color:var(--suave); }
@media print {
  .hoja { max-width:none; padding:0; }
  .solo-html { display:none; }
  a { color:var(--tinta); text-decoration:none; }
  pre { font-size:7.5pt; }
  body { font-size:10.5pt; }
  @page { size:A4; margin:18mm 16mm 20mm; }
}
@media (prefers-color-scheme: dark) {
  :root { --tinta:#e6edf3; --suave:#9198a1; --linea:#30363d; --fondo:#0d1117;
          --codigo:#161b22; --acento:#4493f8; }
}
"""


def a_html(md_texto: str, indice: list[tuple[int, str, str]]) -> str:
    def apartar(m: re.Match[str]) -> str:
        return '<pre class="mermaid">' + html.escape(m.group(1)) + "</pre>"

    cuerpo = MERMAID.sub(apartar, md_texto)
    conv = markdown.Markdown(
        extensions=["tables", "fenced_code", "sane_lists", "attr_list", "md_in_html"]
    )
    render = conv.convert(cuerpo)

    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    total = sum(len(list((p / "classes").glob("*.md"))) for p in partes())
    horas = f"{total * 1.5:.0f}"
    fecha = date.today().isoformat()
    filas = "\n".join(
        f'<li class="n{n}"><a href="#{a}">{html.escape(t)}</a></li>' for n, a, t in indice
    )
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(TITULO)} — programa completo</title>
<style>{ESTILO}</style>
</head>
<body>
<div class="hoja">
<header class="portada">
  <h1>{html.escape(TITULO)}</h1>
  <p class="sub">{html.escape(SUBTITULO)}</p>
  <p class="datos">{len(partes())} partes · {total} clases · {horas} horas<br>
  Versión {version} · Licencia MIT · {fecha}<br>
  <a href="https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program">github.com/vladimiracunadev-create/finance-and-banking-evolution-program</a></p>
  <p class="solo-html">Para guardarlo como PDF: Ctrl+P y «Guardar como PDF».</p>
</header>
<nav class="indice"><h1>Índice</h1><ol>{filas}</ol></nav>
{render}
</div>
</body>
</html>
"""


# Rutas habituales de un navegador basado en Chromium. Se usa en modo headless
# para imprimir el HTML a PDF: es la unica via que produce un PDF con el mismo
# aspecto que el documento y no exige instalar ninguna dependencia de Python.
NAVEGADORES = (
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "/usr/bin/microsoft-edge",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
)


def navegador() -> str | None:
    for ruta in NAVEGADORES:
        if Path(ruta).exists():
            return ruta
    return shutil.which("msedge") or shutil.which("google-chrome") or shutil.which("chromium")


def a_pdf(html: Path, pdf: Path) -> bool:
    """Imprime el HTML a PDF con un navegador en modo headless."""
    exe = navegador()
    if not exe:
        print("No se encontro un navegador basado en Chromium para generar el PDF.")
        print("El HTML esta listo: abrelo y usa Ctrl+P -> Guardar como PDF.")
        return False
    # Perfil propio y desechable. Sin el, si el usuario ya tiene el navegador
    # abierto, la invocacion headless delega en esa instancia y termina con
    # codigo 0 sin escribir el PDF: falla en silencio, que es la peor forma de
    # fallar. Con un perfil aparte el proceso es siempre independiente.
    with tempfile.TemporaryDirectory(prefix="book-perfil-") as perfil:
        orden = [
            exe, "--headless=new", "--disable-gpu", "--no-sandbox",
            f"--user-data-dir={perfil}",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf}",
            html.resolve().as_uri(),
        ]
        # El documento supera el millon de palabras: la impresion tarda minutos.
        resultado = subprocess.run(orden, capture_output=True, text=True, timeout=1800)

        # No se puede dar por terminada la impresion cuando el proceso vuelve.
        # Las versiones recientes de Chrome y Edge lanzan el trabajo en segundo
        # plano y salen en decimas de segundo con codigo 0: mirar `pdf.exists()`
        # justo despues declara fallida una impresion que esta en curso. Se
        # espera a que el archivo aparezca y a que deje de crecer.
        if not esperar_pdf(pdf):
            print("El navegador no produjo el PDF.")
            salida = ((resultado.stderr or "") + (resultado.stdout or "")).strip()
            print(salida[-400:] if salida else f"(sin mensaje; codigo {resultado.returncode})")
            return False
    return True


def esperar_pdf(pdf: Path, limite: int = 900, quieto: int = 6) -> bool:
    """Espera a que el PDF exista y deje de crecer. Devuelve si se completo."""
    fin = time.monotonic() + limite
    anterior = -1
    estable = 0
    while time.monotonic() < fin:
        time.sleep(2)
        if not pdf.exists():
            continue
        actual = pdf.stat().st_size
        estable = estable + 1 if actual == anterior and actual > 0 else 0
        anterior = actual
        if estable >= quieto:
            return True
    return False


def rematar_pdf(pdf: Path, indice: list[tuple[int, str, str]]) -> None:
    """Anade al PDF impreso lo que el navegador no sabe poner.

    Chrome imprime bien la pagina pero no produce ni marcadores ni folio: un
    manual de miles de paginas sin panel de navegacion y sin numero de pagina
    es incomodo de usar y imposible de citar. Aqui se resuelven los dos.

    La pagina de cada entrada del indice no se calcula: se lee del propio PDF.
    Chrome registra el `id` de cada encabezado como destino con nombre, asi que
    resolver el ancla da la pagina exacta sin depender de como se ordenen los
    enlaces.

    Si PyMuPDF no esta instalado, el PDF queda como lo dejo el navegador y se
    avisa: es un extra, no un requisito.
    """
    try:
        import pymupdf
    except ImportError:
        print("  (sin PyMuPDF: el PDF va sin marcadores ni numeracion)")
        print("   instala con: pip install -r requirements-site.txt")
        return

    doc = pymupdf.open(pdf)
    destinos = doc.resolve_names()
    marcadores = [
        [nivel, titulo, destinos[ancla]["page"] + 1]
        for nivel, ancla, titulo in indice
        if ancla in destinos
    ]

    if len(marcadores) == len(indice):
        doc.set_toc(marcadores)
        print(f"  marcadores: {len(marcadores)}")
    else:
        print(f"  (marcadores incompletos: {len(marcadores)} de {len(indice)} anclas "
              "resueltas; el PDF se guarda igual)")
        if marcadores:
            doc.set_toc(marcadores)

    # Folio centrado al pie, desde la primera pagina de contenido. La portada y
    # el indice no se numeran: no se citan.
    primera = (marcadores[0][2] - 1) if marcadores else 1
    for numero in range(primera, doc.page_count):
        pagina = doc[numero]
        caja = pymupdf.Rect(0, pagina.rect.height - 34, pagina.rect.width,
                            pagina.rect.height - 16)
        pagina.insert_textbox(caja, str(numero + 1), fontname="helv", fontsize=8.5,
                              color=(0.42, 0.45, 0.49), align=pymupdf.TEXT_ALIGN_CENTER)

    doc.set_metadata({
        "title": f"{TITULO} — programa completo",
        "author": "Vladimir Acuna",
        "subject": SUBTITULO,
        "keywords": ("finanzas, banca, NIIF, Basilea III, credito, riesgos, "
                     "finanzas abiertas, pagos transfronterizos, DLT, "
                     "stablecoins, tokenizacion"),
    })
    doc.saveIncr()
    doc.close()
    print(f"  numeracion desde la pagina {primera + 1}")


def generar(con_pdf: bool = True) -> int:
    SALIDA.mkdir(exist_ok=True)
    md_texto, indice = documento()
    (SALIDA / "programa-completo.md").write_text(md_texto, encoding="utf-8")
    html = SALIDA / "programa-completo.html"
    html.write_text(a_html(md_texto, indice), encoding="utf-8")
    palabras = len(md_texto.split())
    print(f"book/programa-completo.md   {len(md_texto):>9,} caracteres · {palabras:,} palabras")
    print(f"book/programa-completo.html {len(indice):>9,} entradas de indice")
    if con_pdf:
        pdf = SALIDA / "programa-completo.pdf"
        if pdf.exists():
            pdf.unlink()
        print("Imprimiendo el PDF... (tarda unos minutos)")
        if not a_pdf(html, pdf):
            return 1
        rematar_pdf(pdf, indice)
        print(f"book/programa-completo.pdf  {pdf.stat().st_size / 1_048_576:>9,.1f} MB")
    return 0


def verificar() -> int:
    md_texto, indice = documento()
    if not md_texto.strip() or not indice:
        print("El libro sale vacio.")
        return 1
    print(f"Libro generable: {len(indice)} entradas, {len(md_texto.split()):,} palabras")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--check", action="store_true", help="solo verifica")
    p.add_argument("--sin-pdf", action="store_true",
                   help="genera solo el Markdown y el HTML, sin imprimir el PDF")
    args = p.parse_args()
    if args.check:
        return verificar()
    return generar(con_pdf=not args.sin_pdf)


if __name__ == "__main__":
    sys.exit(main())
