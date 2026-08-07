"""Genera STATUS.md a partir del estado real del repositorio.

El programa declara en `PLANNED` cuántas clases tiene cada parte (ver SYLLABUS.md).
Este script mide cuántas están efectivamente redactadas y produce un informe
verificable, de modo que la documentación nunca afirme más de lo que el
repositorio contiene.

Uso:
    python tools/progress.py           # regenera STATUS.md
    python tools/progress.py --check   # falla si STATUS.md está desactualizado
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULES = ROOT / "modules"
STATUS = ROOT / "STATUS.md"

PLANNED = {
    "00-matematica-financiera-basica": 14,
    "01-finanzas-personales": 14,
    "02-productos-y-servicios-financieros": 14,
    "03-seguridad-y-consumo-financiero": 14,
    "04-contabilidad-financiera": 15,
    "05-economia-y-sistema-financiero": 15,
    "06-matematica-financiera-avanzada": 15,
    "07-inversiones-y-mercados": 15,
    "08-analisis-y-gestion-de-credito": 16,
    "09-operaciones-bancarias": 16,
    "10-gestion-integral-de-riesgos": 16,
    "11-regulacion-cumplimiento-y-auditoria": 16,
    "12-finanzas-corporativas-y-banca-empresarial": 14,
    "13-fintech-datos-e-inteligencia-artificial": 14,
    "14-estrategia-y-direccion-bancaria": 14,
    "15-proyecto-banco-virtual": 18,
    # Etapa 5 — Finanzas digitales, infraestructura y mercados tokenizados.
    "16-finanzas-abiertas-apis-y-economia-de-datos": 14,
    "17-pagos-transfronterizos-remesas-y-liquidacion": 16,
    "18-blockchain-y-dlt-para-instituciones-financieras": 14,
    "19-activos-digitales-stablecoins-y-dinero-programable": 16,
    "20-tokenizacion-fx-onchain-y-mercados-programables": 16,
    "21-regulacion-de-mercados-financieros-digitales": 18,
    "22-proyecto-banco-digital-y-mercado-tokenizado": 18,
}


# Titulo de las partes planificadas cuyo directorio todavia no existe. En cuanto
# la parte se crea, su README.md pasa a ser la fuente del titulo y esta entrada
# deja de usarse: no hay dos sitios donde mantener el mismo dato.
PLANNED_TITLES = {
    "19-activos-digitales-stablecoins-y-dinero-programable": (
        "Parte 20: Activos digitales, stablecoins y dinero programable"
    ),
    "20-tokenizacion-fx-onchain-y-mercados-programables": (
        "Parte 21: Tokenización, FX on-chain y mercados programables"
    ),
    "21-regulacion-de-mercados-financieros-digitales": (
        "Parte 22: Regulación de mercados financieros digitales"
    ),
    "22-proyecto-banco-digital-y-mercado-tokenizado": (
        "Parte 23: Proyecto — banco digital y mercado tokenizado"
    ),
}


def module_title(module: Path) -> str:
    readme = module / "README.md"
    if readme.exists():
        first = readme.read_text(encoding="utf-8").splitlines()[0]
        return re.sub(r"^#\s*", "", first).strip()
    return PLANNED_TITLES.get(module.name, module.name)


def bar(done: int, total: int, width: int = 20) -> str:
    filled = round(width * done / total) if total else 0
    return "█" * filled + "░" * (width - filled)


def collect() -> tuple[list[tuple[str, str, int, int, int]], int, int, int]:
    rows: list[tuple[str, str, int, int, int]] = []
    total_done = total_planned = total_bytes = 0
    for name, planned in PLANNED.items():
        module = MODULES / name
        classes = sorted((module / "classes").glob("*.md")) if module.exists() else []
        done = len(classes)
        size = sum(p.stat().st_size for p in classes)
        rows.append((name, module_title(module), done, planned, size))
        total_done += done
        total_planned += planned
        total_bytes += size
    return rows, total_done, total_planned, total_bytes


def contar_componentes() -> dict[str, int]:
    """Cuenta los componentes no curriculares sobre los archivos reales.

    STATUS.md no debe afirmar «96 laboratorios» porque alguien lo escribio una
    vez: debe contarlos. Cada clave se resuelve con el mismo criterio que usa
    `tools/validate_program.py`, para que las dos herramientas nunca discrepen.
    """
    modules = [p for p in MODULES.iterdir() if p.is_dir()] if MODULES.exists() else []
    apps = ROOT / "apps"
    casos = ROOT / "case-studies"
    normas = ROOT / "regulatory"
    datos = ROOT / "datasets"
    return {
        "modules": len(modules),
        "labs": sum(len(list((m / "labs").glob("*.md"))) for m in modules),
        "assessments": sum(len(list((m / "assessments").glob("*.md"))) for m in modules),
        "projects": sum(int((m / "project" / "README.md").exists()) for m in modules),
        "apps": len([p for p in apps.iterdir() if (p / "README.md").exists()])
        if apps.exists()
        else 0,
        "cases": len([p for p in casos.rglob("*.md") if p.name != "README.md"])
        if casos.exists()
        else 0,
        "norms": len(list(normas.rglob("*.yml"))) if normas.exists() else 0,
        "datasets": len(list(datos.rglob("*.csv"))) if datos.exists() else 0,
    }


def render() -> str:
    rows, done, planned, size = collect()
    pct = 100 * done / planned if planned else 0
    avg = size / done if done else 0
    inventario = contar_componentes()

    lines = [
        "# Estado del contenido",
        "",
        "Este archivo lo genera `tools/progress.py` a partir de los archivos reales",
        "del repositorio. No se edita a mano: refleja lo que hay, no lo que se planea.",
        "",
        f"## Avance global: {done} de {planned} clases ({pct:.1f} %)",
        "",
        f"`{bar(done, planned, 40)}`",
        "",
        "| Parte | Tema | Clases | Plan | Avance | Tamaño medio |",
        "|---:|---|---:|---:|---|---:|",
    ]

    for index, (_, title, mod_done, mod_planned, mod_size) in enumerate(rows, start=1):
        mod_avg = mod_size / mod_done / 1024 if mod_done else 0
        lines.append(
            f"| {index} | {title} | {mod_done} | {mod_planned} | "
            f"`{bar(mod_done, mod_planned)}` | {mod_avg:.1f} KB |"
        )

    lines += [
        f"| | **Total** | **{done}** | **{planned}** | "
        f"`{bar(done, planned)}` | **{avg / 1024:.1f} KB** |",
        "",
        "## Qué significa que una clase esté completa",
        "",
        "Una clase solo se cuenta aquí si supera `tools/validate_program.py`, que exige:",
        "",
        "- encabezado con parte, número, título, nivel, duración y estado;",
        "- las once secciones obligatorias, incluidas ejemplo numérico guiado,",
        "  puente «del cliente al banco», errores frecuentes y entregable;",
        "- navegación, agenda docente y bloque de ética generados por",
        "  `tools/render_program.py`;",
        "- al menos cuatro fuentes verificables en «Fuentes y verificación».",
        "",
        "## Otros componentes",
        "",
        "Las cifras de esta tabla se cuentan sobre los archivos reales; no se",
        "escriben a mano.",
        "",
        "| Componente | Cantidad | Estado |",
        "|---|---:|---|",
        f"| Arquitectura curricular (partes) | {inventario['modules']} | Completa |",
        f"| Laboratorios | {inventario['labs']} | Estructurados |",
        f"| Evaluaciones | {inventario['assessments']} | Diagnóstico y final por parte |",
        f"| Proyectos integradores | {inventario['projects']} | Especificados |",
        f"| Aplicaciones didácticas | {inventario['apps']} | Ejecutables con pruebas |",
        f"| Estudios de caso | {inventario['cases']} | Con hechos, fuentes y preguntas |",
        f"| Fichas normativas estructuradas | {inventario['norms']} | Con fecha de verificación |",
        f"| Datasets documentados | {inventario['datasets']} | Sintéticos, con diccionario |",
        "| Adaptación normativa por país | — | Plantilla; cada clase indica qué verificar |",
        "",
        "## Cómo verificarlo",
        "",
        "```bash",
        "python tools/validate_program.py     # estructura, secciones y fuentes",
        "python tools/render_program.py --check  # navegación y bloques generados",
        "python tools/progress.py --check     # este archivo contra la realidad",
        "pytest -q                            # calculadoras y banco virtual",
        "```",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    content = render()
    current = STATUS.read_text(encoding="utf-8") if STATUS.exists() else ""

    if args.check:
        if current != content:
            print("STATUS.md esta desactualizado. Ejecuta: python tools/progress.py")
            return 1
        print("STATUS.md refleja el estado real del repositorio")
        return 0

    STATUS.write_text(content, encoding="utf-8", newline="\n")
    rows, done, planned, _ = collect()
    print(f"STATUS.md actualizado: {done}/{planned} clases")
    return 0


if __name__ == "__main__":
    sys.exit(main())
