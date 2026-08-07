"""Interfaz de linea de comandos del laboratorio de FX sobre registros.

Uso:
    python apps/onchain_fx_lab/cli.py pricing --notional 3000000
    python apps/onchain_fx_lab/cli.py amm --rounds 3
    python apps/onchain_fx_lab/cli.py settlement
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from apps.onchain_fx_lab.amm import (  # noqa: E402
    Piscina,
    perdida_por_divergencia,
    razon_que_anula_las_comisiones,
    resultado_del_aportante,
)
from apps.onchain_fx_lab.pricing import (  # noqa: E402
    Mecanismo,
    ahorro_corregido_por_profundidad,
    comparar,
    ruta_mayorista,
    ruta_registro,
)
from apps.onchain_fx_lab.settlement import (  # noqa: E402
    Comparacion,
    limite_bilateral,
    perdida_esperada,
    ventana_de_exposicion,
)


def cmd_pricing(args: argparse.Namespace) -> int:
    nominal = args.notional

    print(f"COSTE TOTAL DE UN CAMBIO · nominal {nominal:,}\n")

    principal = comparar(
        ruta_mayorista(1.2, 3.0),
        ruta_registro(8.0, 6.0, 4.0, 4.5),
        nominal,
    )
    print("  PAR PRINCIPAL")
    print(f"    mayorista: {principal['mayorista_pb']:>6.2f} pb")
    print(f"    registro:  {principal['registro_pb']:>6.2f} pb"
          f"  ({principal['veces']:.1f} veces mas caro)")
    print(f"    gana el registro: {principal['gana_el_registro']}\n")

    exotico = comparar(
        ruta_mayorista(45.0, 18.0, 22.0),
        ruta_registro(12.0, 18.0, 4.0, 4.5),
        nominal,
    )
    print("  PAR POCO LIQUIDO")
    print(f"    mayorista: {exotico['mayorista_pb']:>6.2f} pb")
    print(f"    registro:  {exotico['registro_pb']:>6.2f} pb")
    print(f"    ahorro:    {exotico['ahorro_pb']:>6.2f} pb"
          f" = {exotico['ahorro']:,.0f}")

    corregido = ahorro_corregido_por_profundidad(
        exotico["ahorro_pb"], nominal, 5_200_000, 6
    )
    print(f"\n    impacto por profundidad: {corregido['impacto_pb']:>6.2f} pb")
    print(f"    AHORRO REAL:             {corregido['ahorro_real_pb']:>6.2f} pb")
    print(f"    sigue compensando: {corregido['sigue_compensando']}")

    print("\n  Mecanismos de formacion de precio:")
    for mecanismo in Mecanismo:
        print(f"    {mecanismo.value:<24} forma precio: {mecanismo.forma_precio}")
    print("\n  El registro no compite en precio: compite")
    print("  en topologia, eliminando tramos.")
    return 0


def cmd_amm(args: argparse.Namespace) -> int:
    piscina = Piscina(reserva_a=500_000, reserva_b=1_000_000, comision=0.0025)

    print(f"CREADOR AUTOMATIZADO · precio marginal "
          f"{piscina.precio_marginal:.5f}\n")
    print("  entrega       recibe   precio efectivo   deslizamiento   relativo")
    for i in range(args.rounds):
        entrega = 10_000 * (i + 1)
        c = Piscina(500_000, 1_000_000, 0.0025).cotizar(entrega)
        print(f"  {entrega:>7,}  {c['recibe']:>11,.0f}"
              f"   {c['precio_efectivo']:>13.5f}"
              f"   {c['deslizamiento']:>12.2%}"
              f"   {c['tamano_relativo']:>7.2%}")

    print("\n  El deslizamiento es aproximadamente el tamano")
    print("  relativo a la reserva: por eso el capital")
    print("  necesario es enorme frente al volumen que sirve.\n")

    print("  PERDIDA POR DIVERGENCIA")
    for r in (1.25, 1.45, 1.50, 2.00, 4.00):
        print(f"    r = {r:.2f}  ->  {perdida_por_divergencia(r):>7.2%}")

    aportado = 100_000
    resultado = resultado_del_aportante(aportado, 12_600, 1.45)
    print(f"\n  APORTANTE · valor {aportado:,}")
    print(f"    comisiones:  {resultado['comisiones']:>10,.0f}")
    print(f"    divergencia: {resultado['divergencia']:>10,.0f}")
    print(f"    neto:        {resultado['neto']:>10,.0f}"
          f"  ({resultado['rendimiento']:.1%})")
    print(f"    compensa: {resultado['compensa']}")

    r_critica = razon_que_anula_las_comisiones(12_600, aportado)
    print(f"\n  movimiento que anula un ano de comisiones: r = {r_critica:.2f}")
    return 0


def cmd_settlement(args: argparse.Namespace) -> int:
    normal = ventana_de_exposicion(10, 16, 11)
    finde = ventana_de_exposicion(10, 16, 11, dias_no_habiles=2)

    print("RIESGO DE LIQUIDACION\n")
    print(f"  ventana dia normal: {normal.horas:>5.0f} horas")
    print(f"  ventana fin de semana: {finde.horas:>2.0f} horas")

    base = perdida_esperada(40_000_000, 0.00003, 0.45, 1.0, 250)
    base += perdida_esperada(40_000_000, 0.00003, 0.45, 2.8, 50)
    print(f"\n  perdida esperada sin mecanismo: {base:>12,.0f}\n")

    for oponible in (True, False):
        comparacion = Comparacion(
            perdida_sin_mecanismo=base,
            exposicion_bruta=40_000_000,
            fraccion_neteada=0.18,
            coste_financiacion_anual=0.043,
            fraccion_prefinanciada=0.25,
            neteo_oponible=oponible,
        )
        etiqueta = "OPONIBLE" if oponible else "NO OPONIBLE"
        print(f"  ACUERDO DE NETEO {etiqueta}")
        for nombre, valores in comparacion.evaluar().items():
            print(f"    {nombre:<14} perdida {valores['perdida_esperada']:>10,.0f}"
                  f" · coste {valores['coste']:>10,.0f}"
                  f" · total {valores['total']:>10,.0f}")
        print(f"    mejor: {comparacion.mejor()}\n")

    limite = limite_bilateral(base, 40_000_000, 80_000)
    print(f"  limite bilateral para un apetito de 80 000: {limite:>12,.0f}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="comando", required=True)

    p = sub.add_parser("pricing", help="coste total por ruta y par")
    p.add_argument("--notional", type=int, default=3_000_000)
    p.set_defaults(func=cmd_pricing)

    p = sub.add_parser("amm", help="deslizamiento y perdida por divergencia")
    p.add_argument("--rounds", type=int, default=3)
    p.set_defaults(func=cmd_amm)

    p = sub.add_parser("settlement", help="ventana, neteo, limites y PvP")
    p.set_defaults(func=cmd_settlement)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
