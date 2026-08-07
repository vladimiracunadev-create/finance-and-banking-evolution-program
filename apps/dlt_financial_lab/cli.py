"""Interfaz de linea de comandos del laboratorio de registro distribuido.

Uso:
    python apps/dlt_financial_lab/cli.py chain --blocks 100
    python apps/dlt_financial_lab/cli.py merkle --leaves 10000
    python apps/dlt_financial_lab/cli.py consensus --nodes 5 --common-fault 3
    python apps/dlt_financial_lab/cli.py escrow --attack reentrancy
    python apps/dlt_financial_lab/cli.py compare --operations 5000
"""

from __future__ import annotations

import argparse
import sqlite3
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from apps.dlt_financial_lab.chain import Cadena, Transaccion  # noqa: E402
from apps.dlt_financial_lab.consensus import (  # noqa: E402
    Comportamiento,
    Nodo,
    Red,
    independencia_efectiva,
)
from apps.dlt_financial_lab.contracts import Escrow  # noqa: E402
from apps.dlt_financial_lab.crypto import generar_par  # noqa: E402
from apps.dlt_financial_lab.merkle import ArbolMerkle  # noqa: E402


def _cadena(dificultad: int, bloques: int) -> Cadena:
    cadena = Cadena(dificultad=dificultad, cada=10)
    par = generar_par()
    cadena.registrar_clave("acc_a", par)
    cadena.acreditar("acc_a", 10_000_000)
    for i in range(bloques):
        tx = Transaccion("acc_a", "acc_b", 10, i).firmar_con(par)
        cadena.anadir_bloque([tx])
    return cadena


def cmd_chain(args: argparse.Namespace) -> int:
    cadena = _cadena(args.difficulty, args.blocks)
    print(f"CADENA · {args.blocks} bloques · dificultad {args.difficulty}\n")
    print(f"  valida:                     {cadena.validar()}")

    cadena.bloques[args.blocks // 2].transacciones[0].importe = 999_999
    print(f"  tras manipular un bloque:   {cadena.validar()}   <- DETECTADO")

    tiempo = cadena.recalcular_desde(args.blocks // 2)
    print(f"  tras recalcular la cadena:  {cadena.validar()}   <- NO detectado")
    print(f"\n  coste de rehacer {args.blocks // 2} bloques: {tiempo:.4f} s")
    print("\n  La inmutabilidad no la da el encadenamiento:")
    print("  la dan el consenso y el coste de rehacer.")
    return 0


def cmd_merkle(args: argparse.Namespace) -> int:
    arbol = ArbolMerkle()
    for i in range(1, args.leaves + 1):
        arbol.agregar(f"cuenta_{i:06d}", i)

    raiz = arbol.raiz()
    clave = f"cuenta_{args.leaves // 2:06d}"
    prueba = arbol.probar(clave)

    print(f"ARBOL DE MERKLE · {args.leaves} hojas\n")
    print(f"  raiz:                {raiz.hex()[:32]}...")
    print(f"  total declarado:     {arbol.total():,}")
    print(f"  prueba de inclusion: {len(prueba.camino)} elementos"
          f" ({prueba.tamano_bytes} bytes)")
    print(f"  verifica:            {ArbolMerkle.verificar(prueba, raiz)}")

    exclusion = arbol.probar_exclusion(clave + "x")
    print(f"  prueba de exclusion: {ArbolMerkle.verificar_exclusion(exclusion, raiz)}")

    total_antes = arbol.total()
    del arbol.hojas[clave]
    print(f"\n  omitiendo una hoja de valor {args.leaves // 2}:")
    print(f"    total antes:  {total_antes:,}")
    print(f"    total ahora:  {arbol.total():,}   <- la omision SE VE")
    return 0


def cmd_consensus(args: argparse.Namespace) -> int:
    nodos = []
    for i in range(args.nodes):
        if i < args.liars:
            comportamiento = Comportamiento.MENTIROSO
        elif i < args.liars + args.common_fault:
            comportamiento = Comportamiento.DEFECTO_COMUN
        else:
            comportamiento = Comportamiento.HONESTO
        implementacion = "principal" if i < args.common_fault else "alterna"
        nodos.append(Nodo(f"n{i}", comportamiento, implementacion=implementacion))

    red = Red(nodos)
    resultado = red.ejecutar_ronda()

    print(f"CONSENSO · n={red.n} · f={red.f} · quorum={red.quorum}\n")
    print(f"  mentirosos:      {args.liars}")
    print(f"  defecto comun:   {args.common_fault}")
    print(f"  decidido:        {resultado.decidido}")
    print(f"  valor:           {resultado.valor}")
    print(f"  mensajes:        {red.mensajes_ultima_ronda}")
    print(f"  estados honestos: {len(red.estados_honestos())} distinto(s)")

    if resultado.valor == "valor_incorrecto":
        print("\n  ACUERDO SOBRE UN VALOR ERRONEO")
        print("  El umbral tolera nodos que MIENTEN de forma independiente.")
        print("  No tolera software que se equivoca igual en todos.")

    analisis = independencia_efectiva(nodos)
    print(f"\n  mayor grupo por implementacion: {analisis['por_implementacion']}")
    return 0


def cmd_escrow(args: argparse.Namespace) -> int:
    class Atacante:
        def __init__(self, contrato, direccion):
            self.contrato, self.direccion, self.reentradas = contrato, direccion, 0

        def recibir(self, importe):
            if self.reentradas >= 40:
                return
            clave = f"beneficiario:{self.direccion}"
            if self.contrato.saldos.get(clave, 0) >= importe:
                self.reentradas += 1
                self.contrato.retirar(self.direccion)

    for correcto in (False, True):
        contrato = Escrow(verificador="verif", orden_correcto=correcto)
        contrato.acreditar_beneficiario("atacante", 180_000)
        atacante = Atacante(contrato, "atacante")
        contrato.registrar_receptor(atacante)
        contrato.retirar("atacante")
        etiqueta = "ORDEN CORRECTO  " if correcto else "ORDEN DEFECTUOSO"
        print(f"{etiqueta} · reentradas: {atacante.reentradas}")

    print("\n  La diferencia son dos lineas intercambiadas:")
    print("  poner el saldo a cero ANTES de la llamada externa.")
    return 0


def cmd_compare(args: argparse.Namespace) -> int:
    n = args.operations

    inicio = time.perf_counter()
    cadena = _cadena(0, n // 10)
    tiempo_cadena = time.perf_counter() - inicio

    conexion = sqlite3.connect(":memory:")
    conexion.execute(
        "CREATE TABLE ops (id INTEGER PRIMARY KEY, origen TEXT, "
        "destino TEXT, importe INTEGER, firma TEXT)"
    )
    inicio = time.perf_counter()
    conexion.executemany(
        "INSERT INTO ops (origen, destino, importe, firma) VALUES (?,?,?,?)",
        [("acc_a", "acc_b", 10, f"firma{i}") for i in range(n)],
    )
    conexion.commit()
    tiempo_base = time.perf_counter() - inicio

    print(f"COMPARACION · {n} operaciones\n")
    print(f"  cadena ({n // 10} bloques):  {tiempo_cadena:.4f} s")
    print(f"  base compartida:            {tiempo_base:.4f} s")
    if tiempo_base > 0:
        print(f"  relacion:                   {tiempo_cadena / tiempo_base:.1f}x")
    print(f"\n  bloques en la cadena:       {len(cadena.bloques)}")
    print("\n  Los numeros comparan entre si, no con produccion.")
    print("  No incluyen el coste de gobierno, que en un consorcio")
    print("  suele ser el mayor y favorece a la base compartida.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="comando", required=True)

    p = sub.add_parser("chain", help="cadena y su reescritura")
    p.add_argument("--blocks", type=int, default=100)
    p.add_argument("--difficulty", type=int, default=0)
    p.set_defaults(func=cmd_chain)

    p = sub.add_parser("merkle", help="arbol con inclusion, exclusion y sumas")
    p.add_argument("--leaves", type=int, default=10_000)
    p.set_defaults(func=cmd_merkle)

    p = sub.add_parser("consensus", help="consenso con nodos defectuosos")
    p.add_argument("--nodes", type=int, default=5)
    p.add_argument("--liars", type=int, default=0)
    p.add_argument("--common-fault", type=int, default=0)
    p.set_defaults(func=cmd_consensus)

    p = sub.add_parser("escrow", help="contrato con y sin reentrada")
    p.add_argument("--attack", default="reentrancy")
    p.set_defaults(func=cmd_escrow)

    p = sub.add_parser("compare", help="cadena frente a base compartida")
    p.add_argument("--operations", type=int, default=5_000)
    p.set_defaults(func=cmd_compare)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
