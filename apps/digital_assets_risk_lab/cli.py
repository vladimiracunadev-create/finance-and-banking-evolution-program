"""Interfaz de linea de comandos del laboratorio de activos digitales.

Uso:
    python apps/digital_assets_risk_lab/cli.py reserves --redemption 0.35
    python apps/digital_assets_risk_lab/cli.py queue --requests 1800000000
    python apps/digital_assets_risk_lab/cli.py spiral --rounds 4
    python apps/digital_assets_risk_lab/cli.py custody
    python apps/digital_assets_risk_lab/cli.py market --position 12000000
    python apps/digital_assets_risk_lab/cli.py contagion
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from apps.digital_assets_risk_lab.algorithmic import (  # noqa: E402
    SistemaDeDosTokens,
    descomponer_rendimiento,
)
from apps.digital_assets_risk_lab.contagion import Entidad, Grafo  # noqa: E402
from apps.digital_assets_risk_lab.custody import Esquema, Guardian  # noqa: E402
from apps.digital_assets_risk_lab.market import (  # noqa: E402
    Libro,
    Nivel,
    cocientes,
    limite_de_posicion,
    riesgo_de_esperar,
    venta_escalonada,
)
from apps.digital_assets_risk_lab.redemption import Cola, Regla  # noqa: E402
from apps.digital_assets_risk_lab.reserves import Cartera, atender  # noqa: E402


def _cartera() -> Cartera:
    return Cartera(
        circulante=8_400_000_000,
        tramos={
            "efectivo": 840_000_000,
            "letras": 3_010_000_000,
            "deuda_corta": 2_580_000_000,
            "pactos_inversos": 860_000_000,
            "papel_comercial": 945_000_000,
            "deposito_plazo": 358_200_000,
        },
    )


def cmd_reserves(args: argparse.Namespace) -> int:
    cartera = _cartera()
    print("RESERVAS · antes de la redencion\n")
    print(f"  cobertura contable:   {cartera.cobertura_contable:7.2%}")
    print(f"  cobertura liquida:    {cartera.cobertura_liquida:7.2%}")
    print(f"  peso iliquido:        {cartera.peso_iliquido:7.2%}")

    importe = round(cartera.circulante * args.redemption)
    resultado = atender(cartera, importe, escalera=args.escalera)

    print(f"\nREDENCION DEL {args.redemption:.0%} · {importe:,}\n")
    print(f"  cubierta:             {resultado.cubierta}")
    print(f"  coste de venta:       {resultado.coste_de_venta:,}")
    print(f"  coste relativo:       {resultado.coste_relativo:7.3%}")

    print("\nRESERVAS · despues\n")
    print(f"  cobertura contable:   {cartera.cobertura_contable:7.2%}   <- SUBIO")
    print(f"  cobertura liquida:    {cartera.cobertura_liquida:7.2%}")
    print(f"  peso iliquido:        {cartera.peso_iliquido:7.2%}   <- EMPEORO")
    print("\n  La cifra que se publica se mueve")
    print("  en direccion contraria al riesgo real.")
    return 0


def cmd_queue(args: argparse.Namespace) -> int:
    for antidilucion, minimo in ((False, 0), (True, 0), (True, 5_000)):
        cola = Cola(
            efectivo=900_000_000,
            coste_de_venta=0.01112,
            antidilucion=antidilucion,
            tramo_minimo_integro=minimo,
        )
        for i in range(12_000):
            cola.solicitar(f"t{i}", args.requests // 12_000)

        llegada = cola.resolver(Regla.ORDEN_DE_LLEGADA)
        prorrateo = cola.resolver(Regla.PRORRATEO)

        etiqueta = (
            f"antidilucion={'si' if antidilucion else 'no'} · "
            f"tramo minimo={minimo}"
        )
        print(f"COLA · {etiqueta}\n")
        print(f"  orden de llegada · ventaja del primero: "
              f"{llegada.ventaja_del_primero:.4f}")
        print(f"  prorrateo        · ventaja del primero: "
              f"{prorrateo.ventaja_del_primero:.4f}")
        print()

    print("  Con ventaja cero, solicita quien necesita el dinero.")
    print("  Con ventaja positiva, solicita todo el mundo.")
    return 0


def cmd_spiral(args: argparse.Namespace) -> int:
    sistema = SistemaDeDosTokens(
        circulante_e=2_000_000_000, unidades_v=400_000_000, precio_v=3.0
    )
    print(f"ESPIRAL · ratio inicial {sistema.ratio_absorcion:.3f}\n")
    print("  vuelta   ratio    emision/unidad   precio V")
    for i in range(args.rounds):
        vuelta = sistema.canjear(200_000_000)
        print(
            f"  {vuelta.numero:>6}   {vuelta.ratio_absorcion:.3f}"
            f"   {vuelta.emision_por_unidad:>12.4f}"
            f"   {vuelta.precio_v_despues:>8.4f}"
        )

    print(f"\n  el ratio SUBE:              {sistema.vueltas[0].ratio_absorcion:.3f}"
          f" -> {sistema.vueltas[-1].ratio_absorcion:.3f}")
    print(f"  la emision/unidad SE DISPARA")
    print(f"  espiral acelerando:         {sistema.espiral_acelera()}")

    reparto = descomponer_rendimiento(2_000_000_000, 0.12, 42_000_000)
    print(f"\n  rendimiento pagado:         {reparto['pagado']:,.0f}")
    print(f"  de el, dilucion:            {reparto['porcentaje_dilucion']:.1%}")
    return 0


def cmd_custody(args: argparse.Namespace) -> int:
    inicial = Esquema(
        umbral=3,
        guardianes=[
            Guardian("G1", "oficina_A", "tipo_X", "cl"),
            Guardian("G2", "oficina_A", "tipo_X", "cl"),
            Guardian("G3", "oficina_A", "tipo_X", "cl"),
            Guardian("G4", "externo_1", "tipo_X", "cl"),
            Guardian("G5", "externo_2", "tipo_X", "cl"),
        ],
    )
    corregido = Esquema(
        umbral=3,
        guardianes=[
            Guardian("G1", "oficina_A", "tipo_X", "cl", "interno_1"),
            Guardian("G2", "oficina_B", "tipo_Y", "cl", "interno_2"),
            Guardian("G3", "oficina_C", "tipo_X", "uy", "interno_3"),
            Guardian("G4", "externo_1", "tipo_Z", "pe", "proveedor_ext"),
            Guardian("G5", "externo_2", "tipo_Y", "es", "despacho"),
        ],
    )

    for nombre, esquema in (("INICIAL", inicial), ("CORREGIDO", corregido)):
        print(f"ESQUEMA {nombre} · {esquema.umbral}-de-{esquema.n}\n")
        for factor, cuantos in esquema.grupos_correlacionados().items():
            print(f"  mayor grupo por {factor:<14} {cuantos}")
        print(f"  independencia efectiva:       {esquema.independencia_efectiva()}")
        print(f"  tolera evento correlacionado: "
              f"{esquema.tolera_evento_correlacionado()}")
        print(f"  probabilidad de bloqueo:      "
              f"{esquema.probabilidad_de_bloqueo(0.04):.5%}\n")

    print("  El umbral no cambio. Cambio donde y con que")
    print("  estan las partes.")
    print("\n  La probabilidad de bloqueo es la misma en ambos:")
    print("  supone independencia, y ese supuesto solo es")
    print("  defendible en el esquema corregido.")
    return 0


def cmd_market(args: argparse.Namespace) -> int:
    libro = Libro(
        precio_actual=100.0,
        volumen_diario=184_000_000,
        niveles=[
            Nivel(100.00, 420_000),
            Nivel(99.50, 1_150_000),
            Nivel(99.00, 2_080_000),
            Nivel(98.00, 3_340_000),
            Nivel(96.00, 5_100_000),
            Nivel(93.00, 7_800_000),
            Nivel(88.00, 11_200_000),
        ],
    )
    posicion = args.position

    print(f"LIQUIDEZ · posicion de {posicion:,} unidades\n")
    for caida in (0.01, 0.02, 0.05):
        print(f"  profundidad al {caida:.0%}:      {libro.profundidad(caida):>12,}")

    par = cocientes(libro, posicion)
    print(f"\n  posicion / volumen:      {par['sobre_volumen']:>12.2%}  <- tranquiliza")
    print(f"  posicion / profundidad:  {par['sobre_profundidad']:>12.2f}x <- la verdad")

    golpe = libro.vender(posicion, precio_de_cola=84.0)
    print(f"\n  venta de golpe · impacto {golpe['impacto']:.2%}"
          f" · perdida {golpe['perdida']:,.0f}")

    escalonada = venta_escalonada(posicion, 1_500_000, 0.007, 0.70)
    valor = posicion * libro.precio_actual
    print(f"  escalonada en {escalonada['sesiones']} sesiones · impacto "
          f"{escalonada['impacto']:.2%}"
          f" · perdida {valor * escalonada['impacto']:,.0f}")

    horas = escalonada["sesiones"] * 0.5
    print(f"\n  riesgo de esperar {horas:.1f} h: "
          f"{riesgo_de_esperar(0.052, horas):.2%}")
    print(f"  limite de posicion propuesto: {limite_de_posicion(libro):,}")
    return 0


def cmd_contagion(args: argparse.Namespace) -> int:
    grafo = Grafo()
    grafo.agregar(Entidad("banco", capital=420_000_000))
    grafo.agregar(
        Entidad("F", capital=120_000_000, posicion_directa=38_000_000,
                proveedor_de_precios="P1")
    )
    grafo.agregar(
        Entidad("D", capital=340_000_000, posicion_directa=105_000_000,
                proveedor_de_precios="P1")
    )
    grafo.agregar(
        Entidad("P", capital=80_000_000, posicion_directa=12_000_000,
                proveedor_de_precios="P1")
    )
    grafo.agregar(
        Entidad("C", capital=210_000_000, custodia_por_terceros=900_000_000)
    )

    grafo.vincular("banco", "F", 42_000_000)
    grafo.vincular("banco", "D", 68_000_000)
    grafo.vincular("banco", "P", 25_000_000)
    grafo.vincular("banco", "C", 180_000_000, tipo="deposito_recibido")

    print("CONTAGIO · exposicion del banco\n")
    print(f"  exposicion DIRECTA:        {grafo.exposicion_directa('banco'):>14,}")
    for contraparte, importe in grafo.exposicion_indirecta("banco").items():
        print(f"    via {contraparte:<20}   {importe:>12,}")
    print(f"  exposicion ECONOMICA:      {grafo.exposicion_economica('banco'):>14,}")

    critico = grafo.nodo_critico()
    if critico:
        clave, afectadas = critico
        print(f"\n  nodo critico: {clave}")
        print(f"  afecta a: {', '.join(afectadas)}")

    cascada = grafo.cascada("banco", 0.60, 0.40, 0.35)
    print(f"\n  lineas dispuestas:         {cascada['lineas_dispuestas']:>14,}")
    print(f"  depositos retirados:       {cascada['depositos_retirados']:>14,}")
    print(f"  NECESIDAD DE LIQUIDEZ:     {cascada['necesidad_de_liquidez']:>14,}")
    print(f"\n  y la exposicion declarada era "
          f"{cascada['exposicion_declarada']}.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="comando", required=True)

    p = sub.add_parser("reserves", help="cobertura antes y despues de redimir")
    p.add_argument("--redemption", type=float, default=0.35)
    p.add_argument("--escalera", action="store_true")
    p.set_defaults(func=cmd_reserves)

    p = sub.add_parser("queue", help="orden de llegada frente a prorrateo")
    p.add_argument("--requests", type=int, default=1_800_000_000)
    p.set_defaults(func=cmd_queue)

    p = sub.add_parser("spiral", help="espiral de un diseno de dos tokens")
    p.add_argument("--rounds", type=int, default=4)
    p.set_defaults(func=cmd_spiral)

    p = sub.add_parser("custody", help="independencia efectiva de un esquema")
    p.set_defaults(func=cmd_custody)

    p = sub.add_parser("market", help="profundidad, impacto y limite")
    p.add_argument("--position", type=int, default=12_000_000)
    p.set_defaults(func=cmd_market)

    p = sub.add_parser("contagion", help="exposicion directa frente a economica")
    p.set_defaults(func=cmd_contagion)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
