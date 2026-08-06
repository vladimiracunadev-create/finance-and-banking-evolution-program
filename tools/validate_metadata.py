"""Valida los metadatos regulatorios del programa.

Este validador existe por una razon concreta: **una norma citada sin fecha de
verificacion es una afirmacion que no caduca**. Dentro de un ano nadie sabra si
seguia siendo cierta, y el material entero se apoya en que la vigencia se
comprueba.

Comprueba tres cosas:

1. toda clase que cite un instrumento normativo concreto declara una linea de
   verificacion, sea cual sea su parte;
2. las clases de la Etapa 5 (parte >= 17) llevan el encabezado regulatorio
   ampliado y las secciones adicionales que esa etapa exige;
3. las fichas de `regulatory/` tienen los campos obligatorios y una fecha de
   verificacion valida y no futura.

La compatibilidad con las clases anteriores es deliberada: la regla 1 se aplica
a todas, y las reglas 2 y 3 solo a lo que se creo con ellas.

Uso:
    python tools/validate_metadata.py
"""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULES = ROOT / "modules"
REGULATORY = ROOT / "regulatory"

PRIMERA_PARTE_ETAPA_5 = 17

# Instrumentos concretos: una ley, una norma de caracter general, un reglamento
# o una directiva identificados por su numero. Marcos y principios sin numero
# (Basilea, GAFI) no caducan del mismo modo y no activan la regla.
INSTRUMENTO = re.compile(
    r"Ley N\.[oº]\s*[\d.]+"
    r"|Ley\s+\d{2}\.\d{3}"
    r"|NCG N\.[oº]\s*\d+"
    r"|Reglamento \(UE\)\s*\d{4}/\d+"
    r"|Directiva \(UE\)\s*\d{4}/\d+"
    r"|Decreto\s+N\.[oº]\s*\d+"
)
VERIFICACION = re.compile(r"Verificaci[oó]n local|Fecha de verificaci[oó]n")

META_ETAPA_5 = (
    "jurisdictions",
    "regulatory_topics",
    "regulation_last_verified",
    "regulatory_status",
    "primary_authorities",
    "requires_legal_review",
)

SECCIONES_ETAPA_5 = (
    "## 🧠 Modelo mental",
    "## 🧭 Perspectivas",
    "## ⚖️ Riesgos y controles",
    "## 🧪 Práctica",
    "## 🔗 Referencias cruzadas",
)

CAMPOS_FICHA = (
    "country",
    "authority",
    "instrument_type",
    "instrument_number",
    "title",
    "publication_date",
    "implementation_stage",
    "status",
    "scope",
    "official_source",
    "last_verified",
)


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    try:
        _, front, _ = text.split("---", 2)
    except ValueError:
        return {}
    meta: dict[str, str] = {}
    for linea in front.strip().splitlines():
        if ":" in linea:
            clave, valor = linea.split(":", 1)
            meta[clave.strip()] = valor.strip()
    return meta


def leer_ficha(path: Path) -> dict[str, object]:
    """Lector minimo de las fichas normativas.

    Las fichas usan a proposito un subconjunto plano de YAML —`clave: valor` y
    listas con guion— para que el repositorio siga validandose con la biblioteca
    estandar, sin anadir una dependencia solo para leer doce campos.
    """
    datos: dict[str, object] = {}
    clave_actual: str | None = None
    for linea in path.read_text(encoding="utf-8").splitlines():
        if not linea.strip() or linea.lstrip().startswith("#"):
            continue
        if linea.lstrip().startswith("- ") and clave_actual:
            datos.setdefault(clave_actual, [])
            lista = datos[clave_actual]
            if isinstance(lista, list):
                lista.append(linea.split("- ", 1)[1].strip())
            continue
        if ":" in linea and not linea.startswith(" "):
            clave, valor = linea.split(":", 1)
            clave_actual = clave.strip()
            valor = valor.strip()
            datos[clave_actual] = valor if valor else []
    return datos


def fecha_valida(valor: str) -> date | None:
    try:
        return date.fromisoformat(valor.strip().strip('"'))
    except ValueError:
        return None


def revisar_clases(errores: list[str]) -> tuple[int, int]:
    con_instrumento = etapa_5 = 0
    hoy = date.today()

    for path in sorted(MODULES.glob("*/classes/*.md")):
        rel = path.relative_to(ROOT)
        texto = path.read_text(encoding="utf-8")
        meta = frontmatter(texto)
        parte = int(meta.get("part", 0) or 0)

        # Regla 1 - se aplica a todas las clases, antiguas y nuevas.
        if INSTRUMENTO.search(texto):
            con_instrumento += 1
            if not VERIFICACION.search(texto):
                errores.append(
                    f"{rel}: cita un instrumento normativo sin linea de verificacion"
                )

        if parte < PRIMERA_PARTE_ETAPA_5:
            continue

        # Reglas 2 - solo para la Etapa 5.
        etapa_5 += 1
        faltan = [clave for clave in META_ETAPA_5 if clave not in meta]
        if faltan:
            errores.append(f"{rel}: faltan claves regulatorias en el encabezado: {faltan}")

        secciones = [s for s in SECCIONES_ETAPA_5 if s not in texto]
        if secciones:
            errores.append(f"{rel}: faltan secciones de la Etapa 5: {secciones}")

        verificada = meta.get("regulation_last_verified", "")
        fecha = fecha_valida(verificada) if verificada else None
        if verificada and fecha is None:
            errores.append(
                f"{rel}: regulation_last_verified no es una fecha ISO: '{verificada}'"
            )
        elif fecha and fecha > hoy:
            errores.append(
                f"{rel}: regulation_last_verified esta en el futuro: {fecha.isoformat()}"
            )

        if meta.get("requires_legal_review", "").lower() == "true":
            if "no constituye asesoría legal" not in texto:
                errores.append(
                    f"{rel}: requires_legal_review es true pero la clase no declara "
                    "que no constituye asesoria legal"
                )

    return con_instrumento, etapa_5


def revisar_fichas(errores: list[str]) -> int:
    if not REGULATORY.exists():
        return 0
    hoy = date.today()
    fichas = sorted(REGULATORY.rglob("*.yml"))
    for path in fichas:
        rel = path.relative_to(ROOT)
        datos = leer_ficha(path)
        faltan = [campo for campo in CAMPOS_FICHA if campo not in datos]
        if faltan:
            errores.append(f"{rel}: faltan campos obligatorios: {faltan}")
        vacios = [
            campo
            for campo in CAMPOS_FICHA
            if campo in datos and not str(datos[campo]).strip()
        ]
        if vacios:
            errores.append(f"{rel}: campos declarados pero vacios: {vacios}")

        verificada = str(datos.get("last_verified", ""))
        fecha = fecha_valida(verificada) if verificada else None
        if verificada and fecha is None:
            errores.append(f"{rel}: last_verified no es una fecha ISO: '{verificada}'")
        elif fecha and fecha > hoy:
            errores.append(f"{rel}: last_verified esta en el futuro: {fecha.isoformat()}")

        fuente = str(datos.get("official_source", ""))
        if fuente and not fuente.startswith("http"):
            errores.append(f"{rel}: official_source debe ser una URL oficial")
    return len(fichas)


def main() -> int:
    errores: list[str] = []
    con_instrumento, etapa_5 = revisar_clases(errores)
    fichas = revisar_fichas(errores)

    print(f"clases que citan un instrumento: {con_instrumento}")
    print(f"clases de la Etapa 5:            {etapa_5}")
    print(f"fichas normativas:               {fichas}")

    if errores:
        print(f"\n{len(errores)} problema(s):")
        for item in errores[:40]:
            print(f"  - {item}")
        if len(errores) > 40:
            print(f"  ... y {len(errores) - 40} mas")
        return 1

    print("\nMetadatos regulatorios validados correctamente")
    return 0


if __name__ == "__main__":
    sys.exit(main())
