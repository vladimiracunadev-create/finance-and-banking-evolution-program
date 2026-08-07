"""Valida los mensajes ISO 20022 sinteticos del repositorio.

No sustituye a la validacion contra el esquema oficial ni a las guias de uso
vigentes: comprueba las reglas que este programa ensena y que un validador de
esquema no detecta, porque son de CONTENIDO y no de forma.

En la migracion real de un banco, casi todos los rechazos pasan el esquema y
fallan por contenido. Estas son las comprobaciones que si los detectan:

1. campos obligatorios presentes y no vacios;
2. importe con dos decimales y divisa ISO 4217;
3. identificadores de institucion con formato valido;
4. direcciones con ciudad y pais estructurados, no en texto libre;
5. codigo de proposito dentro del catalogo;
6. reparto de gastos admitido;
7. referencia extremo a extremo estable: dos mensajes con el mismo importe,
   beneficiario y fecha no pueden llevar referencias distintas.

Uso:
    python tools/validate_iso20022.py
"""

from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from apps.cross_border_payments_lab.iso20022 import validar  # noqa: E402

MENSAJES = ROOT / "apps" / "cross_border_payments_lab" / "data" / "messages"


def _campo(xml: str, etiqueta: str) -> str:
    import xml.etree.ElementTree as ET

    try:
        raiz = ET.fromstring(xml)
    except ET.ParseError:
        return ""
    nodo = next(
        (
            n
            for n in raiz.iter()
            if isinstance(n.tag, str) and n.tag.split("}")[-1] == etiqueta
        ),
        None,
    )
    if nodo is None:
        return ""
    if nodo.text and nodo.text.strip():
        return nodo.text.strip()
    # Para nodos compuestos (Cdtr, por ejemplo) sirve el nombre de la parte.
    hijo = next((h for h in nodo.iter() if (h.text or "").strip()), None)
    return (hijo.text or "").strip() if hijo is not None else ""


def referencias_inestables(mensajes: dict[str, str]) -> list[str]:
    """Detecta reintentos con referencia regenerada.

    Dos mensajes con el mismo importe, mismo acreedor y misma fecha de
    liquidacion son casi con seguridad el mismo pago reenviado. Si llevan
    referencias distintas, el receptor los vera como duplicados.
    """
    huellas: dict[tuple[str, str, str], set[str]] = defaultdict(set)
    for xml in mensajes.values():
        huella = (
            _campo(xml, "IntrBkSttlmAmt"),
            _campo(xml, "Cdtr"),
            _campo(xml, "IntrBkSttlmDt"),
        )
        referencia = _campo(xml, "EndToEndId")
        if all(huella) and referencia:
            huellas[huella].add(referencia)
    return [
        f"mismo pago con {len(refs)} referencias distintas: {sorted(refs)}"
        for huella, refs in huellas.items()
        if len(refs) > 1
    ]


def main() -> int:
    if not MENSAJES.exists():
        print("no hay mensajes que validar en apps/cross_border_payments_lab/data/messages")
        return 0

    archivos = sorted(MENSAJES.glob("*.xml"))
    if not archivos:
        print("no hay mensajes que validar")
        return 0

    problemas: list[str] = []
    contenidos: dict[str, str] = {}

    for ruta in archivos:
        xml = ruta.read_text(encoding="utf-8")
        contenidos[ruta.name] = xml
        for error in validar(xml):
            problemas.append(f"{ruta.name}: {error}")

    for aviso in referencias_inestables(contenidos):
        problemas.append(f"lote: {aviso}")

    print(f"mensajes revisados: {len(archivos)}")

    if problemas:
        print(f"\n{len(problemas)} problema(s):")
        for item in problemas[:40]:
            print(f"  - {item}")
        if len(problemas) > 40:
            print(f"  ... y {len(problemas) - 40} mas")
        return 1

    print("\nMensajes ISO 20022 validados correctamente")
    return 0


if __name__ == "__main__":
    sys.exit(main())
