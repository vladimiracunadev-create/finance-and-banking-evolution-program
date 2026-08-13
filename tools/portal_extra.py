"""Portada, temario y capa instalable del portal de estudio.

`build_site.py` convierte cada archivo del repositorio a HTML, y eso basta para
leerlo. Pero la entrada del portal no puede ser el README volcado: quien llega
por primera vez necesita ver de un vistazo de que va el programa, cuantas
clases tiene y por donde entrar.

Este modulo produce las tres piezas que faltan:

* la **portada**, con las cifras reales, las cinco etapas y las 23 partes;
* el **temario**, con las 356 clases y un buscador que filtra sin recargar;
* el **manifiesto y el trabajador de servicio**, que permiten instalar el
  portal en el telefono y consultarlo despues sin conexion.

Todo se calcula leyendo el repositorio: ninguna cifra esta escrita a mano.
"""

from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULES = ROOT / "modules"

# Etapa, rango de partes, color e idea de salida. El color es el mismo que usa
# el README para que las dos superficies se lean como el mismo programa.
ETAPAS = [
    ("Fundamentos", 1, 4, "#2ea44f", "🟢",
     "Para quien empieza sin base. Al terminarla se calcula un interés, se lee un "
     "estado de cuenta, se compara un crédito y se reconoce un fraude."),
    ("Analista", 5, 8, "#1f6feb", "🔵",
     "El salto del cliente al profesional. Se interpretan estados financieros, se "
     "entiende de dónde viene una tasa y se valora un instrumento."),
    ("Bancario", 9, 12, "#8957e5", "🟣",
     "El banco por dentro. Se evalúa un crédito con criterio, se sigue el dinero "
     "entre entidades y se sabe qué riesgo consume capital."),
    ("Dirección", 13, 16, "#e67e22", "🟠",
     "La vista del comité. Se defiende una estrategia con números y se construye "
     "un banco completo de principio a fin."),
    ("Finanzas digitales", 17, 23, "#d1242f", "🔴",
     "La infraestructura por debajo: finanzas abiertas, pagos transfronterizos, "
     "DLT, activos digitales, tokenización y su regulación."),
]

META = re.compile(r"^<!--\s*meta\n(.*?)\n-->\n", re.S)


def _meta(texto: str) -> dict[str, str]:
    m = META.match(texto)
    if not m:
        return {}
    datos: dict[str, str] = {}
    for linea in m.group(1).splitlines():
        if ":" in linea:
            k, _, v = linea.partition(":")
            datos[k.strip()] = v.strip().strip('"')
    return datos


# Tabla de «Conceptos centrales»: el termino va en la primera columna.
SECCION = re.compile(r"^##\s+(.*)$", re.M)
FILA = re.compile(r"^\|\s*`?([^`|]+?)`?\s*\|\s*(.+?)\s*\|\s*$", re.M)


def conceptos(texto: str) -> list[str]:
    """Terminos de la tabla de conceptos de una clase.

    El buscador del temario los indexa junto al titulo. Sin ellos solo se
    puede buscar por el nombre de la clase, y terminos como «Basilea»,
    «duracion» o «LGD» no devuelven nada aunque el programa les dedique
    clases enteras.
    """
    marcas = list(SECCION.finditer(texto))
    for i, marca in enumerate(marcas):
        if "Conceptos centrales" not in marca.group(1):
            continue
        fin = marcas[i + 1].start() if i + 1 < len(marcas) else len(texto)
        filas = [f.group(1).strip() for f in FILA.finditer(texto[marca.end():fin])]
        # La primera fila es la cabecera y la segunda el separador de la tabla.
        return [f for f in filas if f and not set(f) <= set("-: ")][1:]
    return []


def _titulo_parte(mod: Path) -> str:
    readme = mod / "README.md"
    if not readme.exists():
        return mod.name
    primera = readme.read_text(encoding="utf-8").splitlines()[0]
    return re.sub(r"^#\s*", "", primera).replace("Parte ", "", 1).split(":", 1)[-1].strip()


def inventario() -> list[dict]:
    """Las 23 partes con sus clases, leidas del repositorio."""
    partes = []
    for mod in sorted(p for p in MODULES.iterdir() if p.is_dir()):
        numero = int(mod.name.split("-")[0]) + 1
        clases = []
        for archivo in sorted((mod / "classes").glob("*.md")):
            texto = archivo.read_text(encoding="utf-8")
            datos = _meta(texto)
            clases.append({
                "conceptos": conceptos(texto),
                "n": int(datos.get("class", 0)),
                "titulo": datos.get("title", archivo.stem),
                "nivel": datos.get("level", ""),
                "ruta": archivo.relative_to(ROOT).with_suffix(".html").as_posix(),
            })
        partes.append({
            "n": numero,
            "titulo": _titulo_parte(mod),
            "ruta": (mod.relative_to(ROOT) / "README.html").as_posix(),
            "labs": len(list((mod / "labs").glob("*.md"))),
            "clases": clases,
        })
    return partes


def _etapa_de(numero: int) -> tuple:
    for etapa in ETAPAS:
        if etapa[1] <= numero <= etapa[2]:
            return etapa
    return ETAPAS[-1]


PORTADA = """<section class="hero">
  <p class="hero-cinta">Programa abierto · español · licencia MIT</p>
  <h1>De no saber calcular un porcentaje<br><span>a defender un banco digital</span></h1>
  <p class="hero-bajada">{clases} clases en {partes} partes y cinco etapas, con caso numérico
     resuelto y bibliografía verificable en cada una. Sin registro, sin coste y sin publicidad.</p>
  <div class="hero-acciones">
    <a class="boton" href="modules/00-matematica-financiera-basica/classes/01-diagnostico-y-operaciones-esenciales.html">Empezar por la clase 1</a>
    <a class="boton secundario" href="temario.html">Ver las {clases} clases</a>
    <a class="boton secundario" href="descargas/programa-completo.pdf">Manual en PDF</a>
  </div>
  <dl class="cifras">
    <div><dt>{clases}</dt><dd>clases</dd></div>
    <div><dt>{partes}</dt><dd>partes</dd></div>
    <div><dt>{horas}</dt><dd>horas</dd></div>
    <div><dt>{labs}</dt><dd>laboratorios</dd></div>
    <div><dt>{fuentes}</dt><dd>fuentes citadas</dd></div>
    <div><dt>{terminos}</dt><dd>términos</dd></div>
  </dl>
</section>

<section class="bloque">
  <h2>Las cinco etapas</h2>
  <p class="bloque-intro">Cada etapa supone la anterior y añade una capa: primero se aprende a
     calcular, después a analizar, después a operar un banco, después a dirigirlo y, por último,
     a construir la infraestructura sobre la que funcionan las finanzas digitales.</p>
  <div class="etapas">{etapas}</div>
</section>

<section class="bloque">
  <h2>Las {partes} partes</h2>
  <p class="bloque-intro">Cada parte trae sus clases, sus laboratorios, su evaluación y su
     proyecto integrador. Pulsa una para abrir su índice.</p>
  <div class="rejilla">{tarjetas}</div>
</section>

<section class="bloque">
  <h2>Para consultar</h2>
  <div class="rejilla">
    <a class="tarjeta" href="descargas/programa-completo.pdf"><span class="tarjeta-emoji">📕</span>
      <strong>Manual completo en PDF</strong>
      <span class="tarjeta-nota">Las {clases} clases en un documento, con índice de 380 marcadores</span></a>
    <a class="tarjeta" href="docs/glosario-maestro.html"><span class="tarjeta-emoji">📖</span>
      <strong>Glosario maestro</strong>
      <span class="tarjeta-nota">{terminos} conceptos con su definición y dónde se estudian</span></a>
    <a class="tarjeta" href="docs/formulas.html"><span class="tarjeta-emoji">🧮</span>
      <strong>Formulario</strong>
      <span class="tarjeta-nota">Las fórmulas del programa, cada una con su trampa habitual</span></a>
    <a class="tarjeta" href="docs/ruta-aprendizaje.html"><span class="tarjeta-emoji">🧭</span>
      <strong>Ruta de aprendizaje</strong>
      <span class="tarjeta-nota">Por dónde entrar según tu punto de partida</span></a>
    <a class="tarjeta" href="docs/guia-docente.html"><span class="tarjeta-emoji">👩‍🏫</span>
      <strong>Guía docente</strong>
      <span class="tarjeta-nota">Sesión de 90 minutos, evaluación y rúbricas</span></a>
    <a class="tarjeta" href="SYLLABUS.html"><span class="tarjeta-emoji">🗂️</span>
      <strong>Programa completo</strong>
      <span class="tarjeta-nota">El índice con las horas, los niveles y los proyectos</span></a>
  </div>
</section>

<section class="bloque aviso">
  <h2>Antes de aplicar nada</h2>
  <p>Este material es <strong>formativo</strong>. No constituye asesoría financiera, tributaria ni
     legal, y no reemplaza títulos ni autorizaciones regulatorias. Las tasas, comisiones, límites y
     normas citados <strong>cambian por país y por fecha</strong>: cada clase cierra con sus fuentes
     y con la fecha en que se verificaron.</p>
</section>
"""

TEMARIO = """<section class="temario-cabecera">
  <h1>Temario completo</h1>
  <p>Las {clases} clases del programa, en orden. Escribe para filtrar por título, parte o nivel.</p>
  <input id="buscador" type="search" placeholder="Buscar entre las {clases} clases…"
         autocomplete="off" aria-label="Buscar una clase">
  <p id="resultado" class="resultado" role="status">{clases} clases</p>
</section>
<div id="listado">{listado}</div>
<p id="vacio" class="vacio" hidden>Ninguna clase coincide con esa búsqueda.<br>El buscador mira los títulos y los conceptos centrales de cada clase. Para un término suelto, prueba el <a href="docs/glosario-maestro.html">glosario maestro</a>; para buscar dentro del texto, el <a href="descargas/programa-completo.pdf">manual en PDF</a>.</p>
<script>
(function () {{
  var caja = document.getElementById("buscador");
  var filas = Array.prototype.slice.call(document.querySelectorAll("#listado .clase"));
  var grupos = Array.prototype.slice.call(document.querySelectorAll("#listado .grupo"));
  var contador = document.getElementById("resultado");
  var vacio = document.getElementById("vacio");
  function normaliza(t) {{
    return t.normalize("NFD").replace(/[\\u0300-\\u036f]/g, "").toLowerCase();
  }}
  filas.forEach(function (f) {{ f.dataset.busca = normaliza(f.dataset.texto); }});
  caja.addEventListener("input", function () {{
    var q = normaliza(caja.value.trim());
    var vistas = 0;
    filas.forEach(function (f) {{
      var ok = !q || f.dataset.busca.indexOf(q) !== -1;
      f.hidden = !ok;
      if (ok) vistas++;
    }});
    grupos.forEach(function (g) {{
      var algo = g.querySelectorAll(".clase:not([hidden])").length;
      g.hidden = algo === 0;
    }});
    contador.textContent = vistas === filas.length
      ? filas.length + " clases"
      : vistas + " de " + filas.length + " clases";
    vacio.hidden = vistas !== 0;
  }});
}})();
</script>
"""


def portada(clases: int, partes: int, labs: int, fuentes: int, terminos: int) -> str:
    tarjetas = []
    bloques_etapa = []
    datos = inventario()

    for nombre, desde, hasta, color, emoji, idea in ETAPAS:
        propias = [p for p in datos if desde <= p["n"] <= hasta]
        total = sum(len(p["clases"]) for p in propias)
        bloques_etapa.append(
            f'<article class="etapa" style="--color:{color}">'
            f'<h3><span aria-hidden="true">{emoji}</span> {html.escape(nombre)}</h3>'
            f'<p class="etapa-meta">Partes {desde}–{hasta} · {total} clases</p>'
            f"<p>{html.escape(idea)}</p></article>"
        )

    for parte in datos:
        _, _, _, color, emoji, _ = _etapa_de(parte["n"])
        tarjetas.append(
            f'<a class="tarjeta" href="{parte["ruta"]}" style="--color:{color}">'
            f'<span class="tarjeta-numero">Parte {parte["n"]}</span>'
            f'<strong>{html.escape(parte["titulo"])}</strong>'
            f'<span class="tarjeta-nota">{len(parte["clases"])} clases · '
            f'{parte["labs"]} laboratorios</span></a>'
        )

    return PORTADA.format(
        clases=clases, partes=partes, horas=f"{clases * 1.5:.0f}",
        labs=labs, fuentes=f"{fuentes // 100 * 100}+", terminos=terminos,
        etapas="".join(bloques_etapa), tarjetas="".join(tarjetas),
    )


def temario(clases: int) -> str:
    piezas = []
    for parte in inventario():
        nombre, _, _, color, emoji, _ = _etapa_de(parte["n"])
        filas = []
        for clase in parte["clases"]:
            texto = " ".join([str(parte["n"]), parte["titulo"], clase["titulo"],
                              clase["nivel"], nombre, *clase["conceptos"]])
            filas.append(
                f'<a class="clase" href="{clase["ruta"]}" data-texto="{html.escape(texto, quote=True)}">'
                f'<span class="clase-n">{clase["n"]:02d}</span>'
                f'<span class="clase-t">{html.escape(clase["titulo"])}</span>'
                f'<span class="clase-nivel">{html.escape(clase["nivel"])}</span></a>'
            )
        piezas.append(
            f'<section class="grupo" style="--color:{color}">'
            f'<h2><span aria-hidden="true">{emoji}</span> Parte {parte["n"]} · '
            f'{html.escape(parte["titulo"])}</h2>'
            f'<p class="grupo-meta">Etapa {html.escape(nombre)} · {len(parte["clases"])} clases · '
            f'<a href="{parte["ruta"]}">índice de la parte</a></p>'
            f'<div class="clases">{"".join(filas)}</div></section>'
        )
    return TEMARIO.format(clases=clases, listado="".join(piezas))


MANIFIESTO = {
    "name": "Finance & Banking Evolution Program",
    "short_name": "Finanzas y Banca",
    "description": "356 clases de finanzas, banca e infraestructura financiera digital.",
    "start_url": "./index.html",
    "scope": "./",
    "display": "standalone",
    "background_color": "#0d1117",
    "theme_color": "#0969da",
    "lang": "es",
    "categories": ["education", "finance"],
    "icons": [
        {"src": "assets/icono-192.png", "sizes": "192x192", "type": "image/png",
         "purpose": "any maskable"},
        {"src": "assets/icono-512.png", "sizes": "512x512", "type": "image/png",
         "purpose": "any maskable"},
    ],
}

# Cachea lo que se visita, de modo que una clase leida una vez se puede releer
# sin conexion. No se precachea el sitio entero: son 15 MB y casi nadie los
# quiere todos.
TRABAJADOR = """const CACHE = "fbep-v{version}";
const ESENCIALES = ["./", "./index.html", "./temario.html", "./assets/estilo.css"];

self.addEventListener("install", (evento) => {
  evento.waitUntil(caches.open(CACHE).then((c) => c.addAll(ESENCIALES)));
  self.skipWaiting();
});

self.addEventListener("activate", (evento) => {
  evento.waitUntil(
    caches.keys().then((claves) =>
      Promise.all(claves.filter((k) => k !== CACHE).map((k) => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener("fetch", (evento) => {
  const peticion = evento.request;
  if (peticion.method !== "GET" || !peticion.url.startsWith(self.location.origin)) return;
  evento.respondWith(
    fetch(peticion)
      .then((respuesta) => {
        const copia = respuesta.clone();
        caches.open(CACHE).then((c) => c.put(peticion, copia));
        return respuesta;
      })
      .catch(() => caches.match(peticion).then((r) => r || caches.match("./index.html")))
  );
});
"""


def icono_png(lado: int, color: tuple[int, int, int] = (9, 105, 218)) -> bytes:
    """Genera un PNG cuadrado de un color, sin dependencias.

    El portal necesita un icono para poder instalarse en el telefono. Dibujar
    un logotipo pediria una libreria de imagen; un cuadrado del color de marca
    cumple el requisito y no anade dependencias al flujo.
    """
    import struct
    import zlib

    fila = bytes(color) * lado
    crudo = b"".join(b"\x00" + fila for _ in range(lado))

    def trozo(etiqueta: bytes, datos: bytes) -> bytes:
        return (struct.pack(">I", len(datos)) + etiqueta + datos
                + struct.pack(">I", zlib.crc32(etiqueta + datos) & 0xFFFFFFFF))

    return (b"\x89PNG\r\n\x1a\n"
            + trozo(b"IHDR", struct.pack(">IIBBBBB", lado, lado, 8, 2, 0, 0, 0))
            + trozo(b"IDAT", zlib.compress(crudo, 9))
            + trozo(b"IEND", b""))


def escribir_pwa(salida: Path, version: str) -> None:
    (salida / "manifest.webmanifest").write_text(
        json.dumps(MANIFIESTO, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n"
    )
    (salida / "sw.js").write_text(
        TRABAJADOR.replace("{version}", version), encoding="utf-8", newline="\n"
    )
    for lado in (192, 512):
        (salida / "assets" / f"icono-{lado}.png").write_bytes(icono_png(lado))
