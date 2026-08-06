"""Valida los contratos OpenAPI del repositorio.

No pretende sustituir a un validador completo de la especificacion: comprueba
las reglas que este programa ensena y que un validador generico no exige, porque
son decisiones de diseno y no de sintaxis:

1. estructura minima de OpenAPI 3.x y version declarada;
2. cada operacion tiene `operationId` unico y `summary`;
3. cada operacion protegida declara sus alcances, y esos alcances existen en el
   esquema de seguridad;
4. cada operacion documenta al menos una respuesta de error;
5. todas las referencias `$ref` internas resuelven;
6. ningun importe se declara como `number`: en dinero, la coma flotante es un
   defecto, no un estilo;
7. los enumerados de respuesta documentan que un valor desconocido no debe
   romper al integrador.

Uso:
    python tools/validate_openapi.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Nombres de campo que representan dinero. Si alguno se declara como `number`,
# el contrato promete un tipo que no puede representar decimales exactos.
CAMPOS_DE_DINERO = {
    "amount", "importe", "balance", "booked_balance", "available_balance",
    "opening_balance", "price", "fee", "principal",
}
METODOS = {"get", "post", "put", "patch", "delete", "head", "options"}


def contratos() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("openapi.json")
        if not any(part in {".git", "site", "node_modules"} for part in p.parts)
    )


def refs(node: object) -> list[str]:
    encontrados: list[str] = []
    if isinstance(node, dict):
        for clave, valor in node.items():
            if clave == "$ref" and isinstance(valor, str):
                encontrados.append(valor)
            else:
                encontrados += refs(valor)
    elif isinstance(node, list):
        for item in node:
            encontrados += refs(item)
    return encontrados


def resolve(spec: dict, ref: str) -> bool:
    if not ref.startswith("#/"):
        return False
    nodo: object = spec
    for parte in ref[2:].split("/"):
        parte = parte.replace("~1", "/").replace("~0", "~")
        if not isinstance(nodo, dict) or parte not in nodo:
            return False
        nodo = nodo[parte]
    return True


def money_as_number(node: object, ruta: str = "") -> list[str]:
    fallos: list[str] = []
    if isinstance(node, dict):
        for clave, valor in node.items():
            if (
                clave in CAMPOS_DE_DINERO
                and isinstance(valor, dict)
                and valor.get("type") in {"number", "integer"}
            ):
                fallos.append(f"{ruta}/{clave}")
            fallos += money_as_number(valor, f"{ruta}/{clave}")
    elif isinstance(node, list):
        for indice, item in enumerate(node):
            fallos += money_as_number(item, f"{ruta}[{indice}]")
    return fallos


def enums_sin_clausula(node: object, ruta: str = "") -> list[str]:
    """Un enumerado de respuesta sin nota de compatibilidad rompe integradores."""
    fallos: list[str] = []
    if isinstance(node, dict):
        if "enum" in node and node.get("type") == "string":
            descripcion = (node.get("description") or "").lower()
            if "desconocido" not in descripcion and "unknown" not in descripcion:
                fallos.append(ruta or "(raiz)")
        for clave, valor in node.items():
            fallos += enums_sin_clausula(valor, f"{ruta}/{clave}")
    elif isinstance(node, list):
        for indice, item in enumerate(node):
            fallos += enums_sin_clausula(item, f"{ruta}[{indice}]")
    return fallos


def check(path: Path, errores: list[str]) -> int:
    rel = path.relative_to(ROOT)
    try:
        spec = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errores.append(f"{rel}: JSON invalido -> {exc}")
        return 0

    version = str(spec.get("openapi", ""))
    if not version.startswith("3."):
        errores.append(f"{rel}: se espera OpenAPI 3.x, se declara '{version}'")
    for clave in ("info", "paths", "components"):
        if clave not in spec:
            errores.append(f"{rel}: falta la seccion '{clave}'")
    if "version" not in spec.get("info", {}):
        errores.append(f"{rel}: info.version es obligatorio")

    esquemas = spec.get("components", {}).get("securitySchemes", {})
    alcances_validos: set[str] = set()
    for esquema in esquemas.values():
        for flujo in esquema.get("flows", {}).values():
            alcances_validos |= set(flujo.get("scopes", {}))

    operaciones = 0
    ids: set[str] = set()
    for ruta, item in spec.get("paths", {}).items():
        for metodo, operacion in item.items():
            if metodo.lower() not in METODOS:
                continue
            operaciones += 1
            etiqueta = f"{rel}: {metodo.upper()} {ruta}"

            oid = operacion.get("operationId")
            if not oid:
                errores.append(f"{etiqueta}: falta operationId")
            elif oid in ids:
                errores.append(f"{etiqueta}: operationId duplicado '{oid}'")
            else:
                ids.add(oid)

            if not operacion.get("summary"):
                errores.append(f"{etiqueta}: falta summary")

            for requisito in operacion.get("security", []):
                for nombre, alcances in requisito.items():
                    if nombre not in esquemas:
                        errores.append(f"{etiqueta}: esquema '{nombre}' no definido")
                    desconocidos = set(alcances) - alcances_validos
                    if desconocidos:
                        errores.append(
                            f"{etiqueta}: alcances no declarados {sorted(desconocidos)}"
                        )

            codigos = set(operacion.get("responses", {}))
            if not any(c.startswith(("4", "5")) for c in codigos):
                errores.append(f"{etiqueta}: no documenta ninguna respuesta de error")

    for ref in set(refs(spec)):
        if not resolve(spec, ref):
            errores.append(f"{rel}: referencia sin resolver -> {ref}")

    for campo in money_as_number(spec):
        errores.append(
            f"{rel}: importe declarado como numero en {campo}; usa cadena decimal"
        )

    for ubicacion in enums_sin_clausula(spec):
        errores.append(
            f"{rel}: enumerado sin nota de compatibilidad en {ubicacion}; "
            "documenta como tratar un valor desconocido"
        )

    return operaciones


def main() -> int:
    errores: list[str] = []
    archivos = contratos()
    if not archivos:
        print("no se encontro ningun contrato openapi.json")
        return 0

    total = 0
    for path in archivos:
        total += check(path, errores)

    print(f"contratos revisados: {len(archivos)}")
    print(f"operaciones:         {total}")

    if errores:
        print(f"\n{len(errores)} problema(s):")
        for item in errores[:40]:
            print(f"  - {item}")
        if len(errores) > 40:
            print(f"  ... y {len(errores) - 40} mas")
        return 1

    print("\nContratos OpenAPI validados correctamente")
    return 0


if __name__ == "__main__":
    sys.exit(main())
