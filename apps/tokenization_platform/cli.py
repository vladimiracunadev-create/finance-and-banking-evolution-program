"""Interfaz de linea de comandos de la plataforma de tokenizacion.

Uso:
    python apps/tokenization_platform/cli.py registry
    python apps/tokenization_platform/cli.py issuance --demand 112400000
    python apps/tokenization_platform/cli.py coupon
    python apps/tokenization_platform/cli.py settlement
    python apps/tokenization_platform/cli.py collateral --drop 0.12
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from apps.tokenization_platform.collateral import (  # noqa: E402
    Posicion,
    Sistema,
    colchon_implicito,
    recorte,
)
from apps.tokenization_platform.issuance import Emision, Mecanismo  # noqa: E402
from apps.tokenization_platform.lifecycle import (  # noqa: E402
    AprovisionamientoInsuficiente,
    Instrumento,
    Titular,
)
from apps.tokenization_platform.registry import (  # noqa: E402
    Causa,
    Configuracion,
    Emisor,
    coste_anual,
)
from apps.tokenization_platform.settlement import (  # noqa: E402
    Liquidador,
    Operacion,
    ahorro_de_la_atomicidad,
    coste_de_liquidez,
)


def cmd_registry(args: argparse.Namespace) -> int:
    print("REGISTRO DE REFERENCIA\n")
    for configuracion in (Configuracion.ESPEJO, Configuracion.BLOQUEO_DE_ORIGEN):
        emisor = Emisor(configuracion, autoridad_de_resolucion="administrador")
        emisor.emitir("inv_a", 1_000)
        etiqueta = configuracion.value.replace("_", " ")
        print(f"  {etiqueta:<20} atomicidad: {emisor.permite_atomicidad}")

    espejo = Emisor(Configuracion.ESPEJO, autoridad_de_resolucion="administrador")
    espejo.emitir("inv_a", 1_000)
    espejo.provocar_divergencia("inv_a", Causa.EVENTO_CORPORATIVO, -40)
    encontradas = espejo.conciliar({"inv_a": Causa.EVENTO_CORPORATIVO})

    print(f"\n  divergencias detectadas: {len(encontradas)}")
    for d in encontradas:
        print(f"    {d.titular}: oficial {d.saldo_oficial} / token {d.saldo_token}")
        print(f"    causa: {d.causa.value} · viene de fuera: {d.viene_de_fuera}")

    # Cifras de la clase 2: conciliacion diaria completa mas incremental
    # horaria sobre los saldos con movimiento, y 40 divergencias al ano.
    espejo_coste = coste_anual(22 * 12, 380, 0, 0) + 120_384 + 179_760
    bloqueo_coste = coste_anual(0, 0, 0, 0) + 27_900 + 12_600
    print(f"\n  coste anual espejo:            {espejo_coste:>10,}")
    print(f"  coste anual bloqueo de origen: {bloqueo_coste:>10,}")
    print("\n  Con un espejo, la atomicidad es imposible:")
    print("  no se puede entregar de forma atomica algo")
    print("  cuya titularidad decide otro registro.")
    return 0


def cmd_issuance(args: argparse.Namespace) -> int:
    ordenes = 6_800
    por_orden = args.demand // ordenes

    for bloqueo in (False, True):
        emision = Emision(
            objetivo=30_000_000,
            minimo=18_000_000,
            tramo_minimo=2_000,
            bloqueo_obligatorio=bloqueo,
        )
        for i in range(ordenes):
            emision.ordenar(f"inv{i}", por_orden)

        simple = emision.adjudicar(Mecanismo.PRORRATEO_SIMPLE)
        con_minimo = emision.adjudicar(Mecanismo.PRORRATEO_CON_MINIMO)
        llegada = emision.adjudicar(Mecanismo.ORDEN_DE_LLEGADA)

        print(f"EMISION · bloqueo del importe: {'si' if bloqueo else 'no'}\n")
        print(f"  sobredemanda:              {emision.sobredemanda:>8.2f}x")
        print(f"  demanda genuina estimada:  "
              f"{emision.demanda_genuina(2.86):>12,}")
        print(f"  coste de bloquear 500 000: "
              f"{emision.coste_del_bloqueo(500_000):>12,.0f}")
        print(f"  ventaja del primero · llegada:  "
              f"{llegada.ventaja_del_primero:.4f}")
        print(f"  ventaja del primero · prorrateo: "
              f"{simple.ventaja_del_primero:.4f}")
        print(f"  adjudicado a inv0 · simple:      "
              f"{simple.adjudicaciones[0].adjudicado:>10,}")
        print(f"  adjudicado a inv0 · con minimo:  "
              f"{con_minimo.adjudicaciones[0].adjudicado:>10,}\n")

    desierta = Emision(objetivo=30_000_000, minimo=18_000_000)
    for i in range(100):
        desierta.ordenar(f"inv{i}", 150_000)
    resultado = desierta.adjudicar(Mecanismo.PRORRATEO_SIMPLE)
    print(f"  EMISION DESIERTA · demanda {desierta.demanda:,} < minimo 18 000 000")
    print(f"  desierta: {resultado.desierta} · colocado: {resultado.colocado}")
    return 0


def cmd_coupon(args: argparse.Namespace) -> int:
    bono = Instrumento(nominal_por_unidad=1_000, unidades=30_000, cupon_anual=0.064)
    for i in range(40):
        bono.registrar(
            Titular(
                f"t{i}",
                unidades=750,
                cuenta_bloqueada=i < 3,
                localizable=i >= 3 or i > 1,
            )
        )
    foto = bono.instantanea("dia 178, 18:00")
    necesario = bono.cupon_total(foto)

    print("CUPON\n")
    print(f"  cupon por unidad:  {bono.cupon_por_unidad:>10,}")
    print(f"  necesario:         {necesario:>10,}")

    try:
        bono.pagar_cupon(foto, necesario - 5_000)
    except AprovisionamientoInsuficiente as error:
        print(f"\n  con 5 000 menos:   RECHAZADO · {error}")
        print("  NO se paga a nadie: el orden de llegada")
        print("  no reparte, discrimina.")

    resultado = bono.pagar_cupon(foto, necesario)
    print(f"\n  con aprovisionamiento completo:")
    print(f"    pagado:          {resultado.pagado:>10,}")
    print(f"    pendiente:       {resultado.pendiente:>10,}")
    print(f"    titulares pagados: {resultado.titulares_pagados}")

    bono.inmovilizar("t10", 750, ("operaciones", "cumplimiento"), "orden judicial")
    print(f"\n  inmovilizaciones registradas: {len(bono.inmovilizaciones)}")

    cierre = bono.vencer(bono.pagos_confirmados)
    print(f"\n  al vencer · destruidas: {cierre['destruidas']:,}"
          f" · vivas: {cierre['vivas']:,}")
    print("  Solo se destruye lo pagado y confirmado.")
    return 0


def cmd_settlement(args: argparse.Namespace) -> int:
    liquidador = Liquidador()
    liquidador.acreditar_valor("vendedor", 1_000)
    liquidador.acreditar_dinero("comprador", 185_000)

    antes = liquidador.observar()
    operacion = Operacion("op1", "vendedor", "comprador", 1_000, 185_000)
    resultado = liquidador.liquidar(operacion)
    despues = liquidador.observar()

    print("LIQUIDACION ATOMICA\n")
    print(f"  antes:   {antes}")
    print(f"  despues: {despues}")
    print(f"  ejecutada: {resultado.ejecutada}")
    print("\n  No hay ningun estado observable en que")
    print("  uno se movio y el otro no.")

    fallo = Liquidador()
    fallo.acreditar_valor("v2", 500)
    r = fallo.liquidar(Operacion("op2", "v2", "c2", 500, 90_000))
    print(f"\n  sin dinero del comprador: {r.motivo.value}")
    print(f"  estado tras el rechazo:   {fallo.observar()}")
    print("  Rechaza ANTES de bloquear: no deja rastro.")

    ahorro = ahorro_de_la_atomicidad(444_000_000, 2, 0.00004, 0.45)
    coste_bruto = coste_de_liquidez(444_000_000, 0.22 - 0.06, 0.043)
    coste_neteo = coste_de_liquidez(444_000_000, 0.09 - 0.06, 0.043)
    print(f"\n  ahorro por atomicidad:  {ahorro:>14,.0f}")
    print(f"  coste liquidez bruto:   {coste_bruto:>14,.0f}")
    print(f"  coste liquidez neteado: {coste_neteo:>14,.0f}")
    print(f"  neto con neteo:         {ahorro - coste_neteo:>14,.0f}")
    return 0


def cmd_collateral(args: argparse.Namespace) -> int:
    print(f"COLATERAL · caida del {args.drop:.0%}\n")
    r = recorte(0.018, 2.33, 0.0015, 0.0005)
    print(f"  recorte calculado:  {r:>8.2%}")
    print(f"  colchon implicito:  {colchon_implicito(1.50, 1.20):>8.2%}")
    print("  (cubren momentos distintos: despues y antes de decidir)\n")

    for parcial in (False, True):
        sistema = Sistema(precio=1.0, liquidacion_parcial=parcial)
        for i in range(340):
            ratio = 1.15 + i * 0.0035
            sistema.agregar(Posicion(f"p{i}", prestamo=352_941,
                                     colateral_unidades=round(352_941 * ratio)))
        vueltas = sistema.cascada(args.drop)
        etiqueta = "PARCIAL " if parcial else "ENTERA  "
        print(f"  LIQUIDACION {etiqueta} · vueltas: {len(vueltas)}"
              f" · amplifica: {sistema.amplifica}")
        for v in vueltas[:4]:
            print(f"    vuelta {v.numero}: liquidadas {v.liquidadas:>3}"
                  f" · vendido {v.volumen_vendido:>12,.0f}"
                  f" · impacto {v.impacto:>6.2%}")
        print()

    print("  Vender solo lo necesario no toca ningun")
    print("  parametro de riesgo y apaga la cascada.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="comando", required=True)

    p = sub.add_parser("registry", help="espejo frente a bloqueo de origen")
    p.set_defaults(func=cmd_registry)

    p = sub.add_parser("issuance", help="adjudicacion y sobredemanda artificial")
    p.add_argument("--demand", type=int, default=112_400_000)
    p.set_defaults(func=cmd_issuance)

    p = sub.add_parser("coupon", help="pago de cupon con verificacion previa")
    p.set_defaults(func=cmd_coupon)

    p = sub.add_parser("settlement", help="liquidacion atomica y sus fallos")
    p.set_defaults(func=cmd_settlement)

    p = sub.add_parser("collateral", help="cascada de liquidaciones")
    p.add_argument("--drop", type=float, default=0.12)
    p.set_defaults(func=cmd_collateral)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
