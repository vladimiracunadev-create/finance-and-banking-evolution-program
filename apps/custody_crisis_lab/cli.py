"""Interfaz de linea de comandos del laboratorio de crisis de custodia.

Uso:
    python apps/custody_crisis_lab/cli.py caso --escenario crd_002
    python apps/custody_crisis_lab/cli.py fondos --sustraido 6300 --congelado 3000 --p 0.8
    python apps/custody_crisis_lab/cli.py corrida --escenario crd_002
    python apps/custody_crisis_lab/cli.py plan
    python apps/custody_crisis_lab/cli.py binance
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from apps.custody_crisis_lab.cases import (  # noqa: E402
    CIFRAS_PUBLICAS,
    entidad_binance_estilizada,
)
from apps.custody_crisis_lab.datos import (  # noqa: E402
    Escenario,
    cargar_entidad,
    cargar_escenarios,
)
from apps.custody_crisis_lab.incident import clasificar_fondos  # noqa: E402
from apps.custody_crisis_lab.recovery import PLAN  # noqa: E402
from apps.custody_crisis_lab.scenario import ejecutar  # noqa: E402


def _imprimir_resultado(r, esc: Escenario) -> None:
    antes, despues = r.antes, r.despues
    print(f"ESCENARIO {esc.scenario_id} · {esc.nombre} · MUSD\n")
    print("RESPALDO")
    print(f"  antes   bruto {antes.respaldo_bruto:8.2%} · disponible {antes.respaldo_disponible:8.2%}")
    print(f"  despues bruto {despues.respaldo_bruto:8.2%} · disponible {despues.respaldo_disponible:8.2%}")
    print(f"  brecha  {despues.brecha:>12,.0f}")

    f = r.fondos
    print("\nFONDOS (no son equivalentes)")
    print(f"  sustraido            {f.sustraido:>12,.0f}")
    print(f"  congelado            {f.congelado:>12,.0f}")
    print(f"  restituible esperado {f.restituible:>12,.0f}")
    print(f"  sin congelar         {f.sin_congelar:>12,.0f}")
    print(f"  perdida definitiva   {f.perdida_definitiva:>12,.0f}")

    print("\nCORRIDA (dia · demanda · pagado · impagado · respaldo)")
    for d in r.corrida:
        print(f"  {d.dia:>3} {d.demanda:>10,.0f} {d.pagado:>10,.0f} "
              f"{d.impagado:>10,.0f} {d.respaldo_bruto:8.2%}")

    p = r.reposicion
    print(f"\nREPOSICION · necesidad {p.necesidad:,.0f} · costo {p.costo_total:,.1f}")
    for a in p.aportes:
        print(f"  {a.fuente:<24} {a.monto:>10,.0f}  costo {a.costo:>8,.1f}  dia {a.dias}")

    c = r.costos
    print("\nCOSTOS")
    print(f"  perdida definitiva  {c.perdida_definitiva:>10,.1f}")
    print(f"  reposicion          {c.reposicion:>10,.1f}")
    print(f"  forense y legal     {c.forense_legal:>10,.1f}")
    print(f"  oportunidad         {c.oportunidad:>10,.1f}")
    print(f"  compensaciones      {c.compensaciones:>10,.1f}")
    print(f"  TOTAL               {c.bruto:>10,.1f}")

    print("\nTRAYECTORIA DEL RESPALDO BRUTO")
    for dia, rb in r.trayectoria:
        print(f"  dia {dia:>2}: {rb:8.2%}")


def cmd_caso(args: argparse.Namespace) -> int:
    escenarios = cargar_escenarios()
    if args.escenario not in escenarios:
        print(f"escenario desconocido: {args.escenario}", file=sys.stderr)
        return 2
    esc = escenarios[args.escenario]
    _imprimir_resultado(ejecutar(cargar_entidad(), esc), esc)
    return 0


def cmd_fondos(args: argparse.Namespace) -> int:
    try:
        f = clasificar_fondos(args.sustraido, args.congelado, args.p)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(f"sustraido {f.sustraido:,.0f} · congelado {f.congelado:,.0f} · "
          f"restituible {f.restituible:,.0f} · perdida definitiva {f.perdida_definitiva:,.0f}")
    return 0


def cmd_corrida(args: argparse.Namespace) -> int:
    return cmd_caso(args)


def cmd_plan(args: argparse.Namespace) -> int:
    print("PLAN DE RECUPERACION Y CONTINUIDAD\n")
    for fase in PLAN:
        print(f"{fase.nombre} ({fase.horizonte})")
        print(f"  accion:      {fase.accion}")
        print(f"  responsable: {fase.responsable}")
        print(f"  entrada:     {fase.entrada}")
        print(f"  salida:      {fase.salida}\n")
    return 0


def cmd_binance(args: argparse.Namespace) -> int:
    print("CIFRAS PUBLICAS · estimaciones sujetas a revision (MUSD)\n")
    for clave, (valor, quien, nota) in CIFRAS_PUBLICAS.items():
        print(f"  {clave:<32} {valor:>10,.0f}  {quien} · {nota}")
    entidad = entidad_binance_estilizada()
    esc = Escenario("bin_est", "Binance 2026 estilizado", 6_300.0, 3_000.0,
                    0.8, 1.0, 0.03, 3.0, 2, 0.05)
    print("\nENTIDAD ESTILIZADA (pasivos = activos bajo gestion: SUPUESTO)\n")
    _imprimir_resultado(ejecutar(entidad, esc), esc)
    return 0


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="comando", required=True)

    p = sub.add_parser("caso", help="escenario completo desde el dataset")
    p.add_argument("--escenario", default="crd_002")
    p.set_defaults(func=cmd_caso)

    p = sub.add_parser("fondos", help="clasificar sustraido, congelado y perdido")
    p.add_argument("--sustraido", type=float, required=True)
    p.add_argument("--congelado", type=float, required=True)
    p.add_argument("--p", type=float, default=0.8)
    p.set_defaults(func=cmd_fondos)

    p = sub.add_parser("corrida", help="alias de caso: incluye la corrida")
    p.add_argument("--escenario", default="crd_002")
    p.set_defaults(func=cmd_corrida)

    p = sub.add_parser("plan", help="plan de recuperacion y continuidad")
    p.set_defaults(func=cmd_plan)

    p = sub.add_parser("binance", help="cifras publicas y entidad estilizada")
    p.set_defaults(func=cmd_binance)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
