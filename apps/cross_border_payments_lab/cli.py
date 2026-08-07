"""Interfaz de linea de comandos del laboratorio de pagos transfronterizos.

Uso:
    python apps/cross_border_payments_lab/cli.py trace --corridor CL-VN --amount 10000
    python apps/cross_border_payments_lab/cli.py route --corridor C --amount 20000
    python apps/cross_border_payments_lab/cli.py compare-routes --amount 20000
    python apps/cross_border_payments_lab/cli.py pvp --scenario coordinator-failure
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from apps.cross_border_payments_lab import build  # noqa: E402
from apps.cross_border_payments_lab.routing_engine import Pago  # noqa: E402
from apps.cross_border_payments_lab.settlement import (  # noqa: E402
    SistemaLiquidacion,
    liquidar_pvp,
)
from apps.cross_border_payments_lab.stablecoin_route import (  # noqa: E402
    RutaClasica,
    RutaStablecoin,
    comparar,
    descomponer_ahorro,
    porcentaje_atribuible_al_registro,
)

ORDENADO_POR_DEFECTO = "2026-06-16T16:40:00"


def _clasica(intermediarios: int) -> RutaClasica:
    """Ruta clasica del ejemplo de la clase 14.

    Cada intermediario adicional anade comision Y diferencial: por eso el coste
    crece mas deprisa que el numero de eslabones.
    """
    return RutaClasica(
        comision_envio=Decimal(38),
        diferencial_pb=Decimal(185),
        diferencial_por_intermediario_pb=Decimal(70),
        comision_por_intermediario=Decimal(22),
        intermediarios=intermediarios,
        comision_receptor=Decimal(14),
        saldo_prefinanciado=Decimal(400_000),
        coste_fondeo_anual=Decimal("0.042"),
        operaciones_anuales=1_200,
        coste_mensajeria=Decimal("3.84"),
        horas_hasta_disponible=Decimal(58),
    )


def cmd_trace(args: argparse.Namespace) -> int:
    lab = build()
    traza, asientos = lab.pagar(args.corridor, args.amount, args.at)
    inicio = datetime.fromisoformat(args.at)

    print(f"CORREDOR {args.corridor} · {args.amount:,.2f} · ordenado {args.at}\n")
    for flujo in ("mensaje", "fondos", "contable", "cumplimiento"):
        eventos = traza.de(flujo)
        if not eventos:
            continue
        print(flujo.upper())
        for evento in eventos:
            transcurrido = (evento.momento - inicio).total_seconds() / 3600
            print(f"  +{transcurrido:8.2f} h  {evento.detalle}")
        print()

    partes = traza.descomposicion(inicio)
    print("DESCOMPOSICION DEL TIEMPO")
    print(f"  total          {partes['total_horas']:8.2f} h")
    print(f"  mensajeria     {partes['mensaje_horas']:8.4f} h")
    print(f"  espera         {partes['espera_horas']:8.2f} h")
    if partes["total_horas"]:
        peso = partes["espera_horas"] / partes["total_horas"] * 100
        print(f"\n  la espera es el {peso:.1f} % del tiempo total")
    print(f"\nasientos: {len(asientos)} · cuadran: {abs(sum(a.importe for a in asientos)) < 0.01}")
    return 0


def cmd_route(args: argparse.Namespace) -> int:
    lab = build()
    pago = Pago(
        corredor=args.corridor,
        importe=args.amount,
        moneda_origen="MA",
        moneda_destino="MB",
        canal_beneficiario=args.channel,
        controles=frozenset(args.controls),
    )
    decision = lab.enrutar(pago)
    print(f"CORREDOR {args.corridor} · {args.amount:,.2f} · canal {args.channel}\n")
    if decision.ruta is None:
        print(f"SIN RUTA: {decision.motivo}")
    else:
        print(f"ELEGIDA      {decision.ruta.nombre} ({decision.ruta.tipo})")
        print(f"COSTE        {decision.ruta.coste_total(pago):,.2f}"
              f"  ({decision.ruta.coste_relativo(pago):.2%})")
        print(f"ALTERNATIVA  {decision.alternativa.nombre if decision.alternativa else '—'}")
        print(f"MOTIVO       {decision.motivo}")
    if decision.descartadas:
        print("\nDESCARTADAS")
        for nombre, motivo in decision.descartadas.items():
            print(f"  {nombre:20s} {motivo}")
    return 0


def cmd_compare_routes(args: argparse.Namespace) -> int:
    importe = Decimal(str(args.amount))
    stablecoin = RutaStablecoin(
        entrada_comision_pct=Decimal("0.0035"),
        entrada_diferencial_pb=Decimal(60),
        comision_red=Decimal("0.04"),
        salida_comision_pct=Decimal("0.0045"),
        salida_diferencial_pb=Decimal(95),
        comision_retiro=Decimal(9),
        minutos_tenencia=22,
        horas_hasta_disponible=Decimal("0.63"),
    )
    print(f"IMPORTE {importe:,.2f}\n")
    print("intermediarios   clasica   stablecoin   diferencia   gana")
    for intermediarios in (1, 2, 3):
        clasica = _clasica(intermediarios)
        r = comparar(clasica, stablecoin, importe)
        gana = "stablecoin" if r["gana_stablecoin"] else "clasica"
        print(f"      {intermediarios}          {r['coste_clasica']:9,.2f}"
              f"  {r['coste_stablecoin']:10,.2f}  {r['ahorro']:11,.2f}   {gana}")

    clasica = _clasica(2)
    print("\nDESCOMPOSICION DEL AHORRO (2 intermediarios)")
    fuentes = descomponer_ahorro(clasica, stablecoin, importe)
    total = sum(fuentes.values())
    for nombre, valor in fuentes.items():
        peso = valor / total * 100 if total else Decimal(0)
        print(f"  {nombre:28s} {valor:10,.2f}  {peso:5.1f} %")
    registro = porcentaje_atribuible_al_registro(clasica, stablecoin, importe)
    print(f"\n  ATRIBUIBLE AL REGISTRO: {registro:.1f} %")
    print(f"  ATRIBUIBLE A LA TOPOLOGIA: {100 - registro:.1f} %")
    return 0


def cmd_pvp(args: argparse.Namespace) -> int:
    a = SistemaLiquidacion("EUR")
    b = SistemaLiquidacion("USD")
    escenarios = {
        "ok": {},
        "coordinator-failure": {"coordinador_cae": True},
        "b-failure": {"sistema_b_falla_al_liberar": True},
    }
    opciones = escenarios[args.scenario]
    resultado = liquidar_pvp("OP-0001", Decimal(1_000_000), Decimal(1_080_000), a, b,
                             plazo_s=30, **opciones)
    print(f"ESCENARIO {args.scenario}")
    print(f"  liquidado        {resultado.liquidado}")
    print(f"  motivo           {resultado.motivo}")
    print(f"  patas liberadas  {resultado.patas_liberadas}")
    if resultado.patas_liberadas == 1:
        print("\n  CASO LIMITE: la pata A se liquido y la B no.")
        print("  La atomicidad del protocolo NO cubre un fallo posterior")
        print("  a la primera liberacion. Exposicion: importe completo.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="comando", required=True)

    p = sub.add_parser("trace", help="traza los cuatro flujos de un pago")
    p.add_argument("--corridor", default="CL-VN")
    p.add_argument("--amount", type=float, default=10_000)
    p.add_argument("--at", default=ORDENADO_POR_DEFECTO)
    p.set_defaults(func=cmd_trace)

    p = sub.add_parser("route", help="elige la ruta de un pago")
    p.add_argument("--corridor", default="C")
    p.add_argument("--amount", type=float, default=20_000)
    p.add_argument("--channel", default="cuenta")
    p.add_argument("--controls", nargs="*", default=["screening", "travel_rule"])
    p.set_defaults(func=cmd_route)

    p = sub.add_parser("compare-routes", help="clasica frente a stablecoin")
    p.add_argument("--amount", type=float, default=20_000)
    p.set_defaults(func=cmd_compare_routes)

    p = sub.add_parser("pvp", help="liquidacion con pago contra pago")
    p.add_argument("--scenario", choices=["ok", "coordinator-failure", "b-failure"],
                   default="ok")
    p.set_defaults(func=cmd_pvp)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
