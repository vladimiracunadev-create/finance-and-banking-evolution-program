"""Motor de render del programa.

Cada clase se escribe con un encabezado YAML y un cuerpo pedagógico. Este script
inyecta —de forma idempotente— las partes mecánicas que no deben escribirse a mano:

* cabecera con título, nivel y navegación anterior/siguiente;
* agenda docente de 90 minutos;
* bloque de seguridad, ética y límites;
* pie de navegación.

También regenera el `README.md` de cada parte a partir de los encabezados YAML,
de modo que los enlaces nunca queden desincronizados con los archivos reales.

Uso:
    python tools/render_program.py            # render + READMEs
    python tools/render_program.py --check    # falla si algo quedaría modificado
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULES = ROOT / "modules"

GEN = "gen"
NIVELES = {
    "fundamento": "Fundamento — sin conocimientos previos",
    "intermedio": "Intermedio — requiere las partes anteriores",
    "avanzado": "Avanzado — perfil analista",
    "profesional": "Profesional — perfil bancario",
}

AGENDA = """| Minutos | Bloque | Qué ocurre |
|---:|---|---|
| 0–10 | Activación | Pregunta diagnóstica y recuperación de la clase anterior. |
| 10–35 | Conceptos | Desarrollo guiado con la fuente oficial a la vista. |
| 35–55 | Ejemplo guiado | El docente resuelve el caso numérico paso a paso. |
| 55–80 | Práctica | El estudiante replica con datos propios o sintéticos. |
| 80–90 | Cierre | Preguntas de comprobación y registro en el portafolio. |
"""

ETICA = """Trabaja siempre con datos sintéticos o propios: nunca uses datos reales de terceros,
números de cuenta, documentos de identidad ni antecedentes crediticios ajenos. Este
material es formativo y **no constituye asesoría financiera, tributaria ni legal**; las
tasas, comisiones, límites y normas citados cambian y deben verificarse en la fuente
oficial vigente del país donde se aplique. Cuando un cálculo alimente una decisión que
afecte a otra persona, registra los supuestos y quién los aprobó.
"""


def slugify(text: str) -> str:
    """Convierte un título a un identificador ASCII estable para nombres de archivo."""
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii").lower()
    ascii_text = re.sub(r"[^a-z0-9]+", "-", ascii_text)
    return ascii_text.strip("-")


@dataclass
class ClassDoc:
    path: Path
    meta: dict[str, str]
    body: str

    @property
    def number(self) -> int:
        return int(self.meta["class"])

    @property
    def title(self) -> str:
        return self.meta["title"].strip('"')

    @property
    def level(self) -> str:
        return self.meta.get("level", "fundamento")


def parse(path: Path) -> ClassDoc:
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---"):
        raise SystemExit(f"{path}: falta el encabezado YAML")
    _, front, body = raw.split("---", 2)
    meta: dict[str, str] = {}
    for line in front.strip().splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip()
    for required in ("part", "class", "title"):
        if required not in meta:
            raise SystemExit(f"{path}: falta '{required}' en el encabezado YAML")
    return ClassDoc(path=path, meta=meta, body=body)


def strip_generated(body: str) -> str:
    """Elimina todas las regiones generadas para que el render sea idempotente."""
    pattern = re.compile(rf"<!-- {GEN}:[a-z]+:start -->.*?<!-- {GEN}:[a-z]+:end -->\n?", re.S)
    return pattern.sub("", body).strip() + "\n"


def block(name: str, content: str) -> str:
    return f"<!-- {GEN}:{name}:start -->\n{content.strip()}\n<!-- {GEN}:{name}:end -->\n"


def insert_after_section(body: str, heading: str, content: str) -> str:
    """Inserta contenido justo antes del siguiente encabezado de nivel 2."""
    start = body.find(heading)
    if start == -1:
        raise SystemExit(f"no se encontró la sección '{heading}'")
    nxt = body.find("\n## ", start + len(heading))
    at = len(body) if nxt == -1 else nxt + 1
    return body[:at] + content + "\n" + body[at:]


def insert_before_section(body: str, heading: str, content: str) -> str:
    at = body.find(heading)
    if at == -1:
        raise SystemExit(f"no se encontró la sección '{heading}'")
    return body[:at] + content + "\n" + body[at:]


def module_title(module: Path) -> str:
    readme = module / "README.md"
    if readme.exists():
        first = readme.read_text(encoding="utf-8").splitlines()[0]
        title = first.lstrip("# ").strip()
        return re.sub(r"^Parte\s+\d+:\s*", "", title)
    return module.name


def render_module(module: Path, part_index: int, write: bool) -> list[str]:
    changes: list[str] = []
    docs = sorted(
        (parse(p) for p in (module / "classes").glob("*.md")),
        key=lambda d: d.number,
    )
    total = len(docs)
    part_name = module_title(module)

    for position, doc in enumerate(docs):
        prev_doc = docs[position - 1] if position > 0 else None
        next_doc = docs[position + 1] if position < total - 1 else None

        prev_link = (
            f"[← {prev_doc.number:02d} · {prev_doc.title}]({prev_doc.path.name})"
            if prev_doc
            else "[← Índice de la parte](../README.md)"
        )
        next_link = (
            f"[{next_doc.number:02d} · {next_doc.title} →]({next_doc.path.name})"
            if next_doc
            else "[Proyecto de la parte →](../project/README.md)"
        )

        header = block(
            "header",
            f"# Clase {doc.number:02d} · {doc.title}\n\n"
            f"> {prev_link} · [Índice de la parte](../README.md) · {next_link}\n\n"
            f"**Parte {part_index:02d} — {part_name}** · "
            f"**Nivel:** {NIVELES.get(doc.level, doc.level)} · "
            f"**Duración:** {doc.meta.get('duration_minutes', '90')} minutos",
        )
        footer = block(
            "footer",
            "---\n\n"
            "| Anterior | Índice | Siguiente |\n|---|---|---|\n"
            f"| {prev_link} | [Parte {part_index:02d}](../README.md) · "
            "[Programa](../../../SYLLABUS.md) | "
            f"{next_link} |",
        )

        body = strip_generated(doc.body)
        body = insert_after_section(body, "## 📚 Objetivos", block("agenda", "## Agenda de 90 minutos\n\n" + AGENDA))
        body = insert_before_section(
            body,
            "## 📗 Fuentes y verificación",
            block("etica", "## 🔐 Seguridad, ética y límites\n\n" + ETICA),
        )

        front = "---\n" + "\n".join(f"{k}: {v}" for k, v in doc.meta.items()) + "\n---\n\n"
        rendered = front + header + "\n" + body + "\n" + footer
        rendered = re.sub(r"\n{3,}", "\n\n", rendered)

        current = doc.path.read_text(encoding="utf-8")
        if current != rendered:
            changes.append(str(doc.path.relative_to(ROOT)))
            if write:
                doc.path.write_text(rendered, encoding="utf-8", newline="\n")

    readme = module / "README.md"
    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        sequence = "\n".join(
            f"{d.number}. [{d.title}](classes/{d.path.name})" for d in docs
        )
        new_text = re.sub(
            r"(## Secuencia\n\n).*?(\n\n## )",
            lambda m: m.group(1) + sequence + m.group(2),
            text,
            flags=re.S,
        )
        if new_text != text:
            changes.append(str(readme.relative_to(ROOT)))
            if write:
                readme.write_text(new_text, encoding="utf-8", newline="\n")
    return changes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="no escribe; falla si hay cambios pendientes")
    args = parser.parse_args()

    modules = sorted(p for p in MODULES.iterdir() if p.is_dir())
    changes: list[str] = []
    for index, module in enumerate(modules, start=1):
        changes.extend(render_module(module, index, write=not args.check))

    if args.check and changes:
        print("Estos archivos no están renderizados:")
        for item in changes[:40]:
            print(f"  - {item}")
        if len(changes) > 40:
            print(f"  ... y {len(changes) - 40} más")
        print("\nEjecuta: python tools/render_program.py")
        return 1

    verb = "pendientes" if args.check else "actualizados"
    print(f"{len(modules)} partes procesadas | {len(changes)} archivos {verb}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
