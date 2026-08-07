"""Interfaz de linea de comandos del capstone.

Uso:
    python apps/digital_bank_capstone/cli.py scope
    python apps/digital_bank_capstone/cli.py build
    python apps/digital_bank_capstone/cli.py tensions
    python apps/digital_bank_capstone/cli.py stress
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from apps.digital_bank_capstone.build import (  # noqa: E402
    Componente,
    Salida,
    concentracion_del_sector,
)
from apps.digital_bank_capstone.scope import (  # noqa: E402
    Alcance,
    Funcion,
    carga_regulatoria,
    facturacion_necesaria,
    saldo_minimo,
)
from apps.digital_bank_capstone.stress import (  # noqa: E402
    Escenario,
    NivelDePrueba,
    Proveedor,
    desviaciones,
)
from apps.digital_bank_capstone.tensions import Decision, Sistema  # noqa: E402


def _alcance() -> Alcance:
    a = Alcance()
    for nombre, quien, ingreso, coste, reg in (
        ("cuentas y pagos locales", 2400, 620000, 180000, "captacion"),
        ("pagos transfronterizos", 2400, 430000, 210000, "pagos"),
        ("custodia de activos digitales", 0, 0, 240000, "custodia"),
        ("cambio de divisas", 2400, 240000, 90000, "cambio"),
        ("emision de bonos tokenizados", 0, 0, 320000, "oferta publica"),
        ("mercado secundario", 0, 0, 280000, "mercado"),
        ("credito con colateral", 640, 77520, 160000, "credito"),
        ("stablecoin propia", 0, 0, 300000, "emisor"),
        ("interfaz de datos", 0, 0, 120000, "consentimiento"),
        ("asesoria automatizada", 0, 0, 140000, "asesoria"),
        ("tarjeta de pago", 380, 0, 260000, "emisor de tarjeta"),
    ):
        a.proponer(Funcion(nombre, quien, ingreso, coste, reg))
    return a


def cmd_scope(args: argparse.Namespace) -> int:
    a = _alcance()
    print("ALCANCE · las cuatro preguntas por funcion\n")
    print(f"  funciones propuestas:      {len(a.funciones)}")
    print(f"  ingreso con todas:         {a.ingreso:>12,}")
    print(f"  regimenes con todas:       {len(a.regimenes)}")

    excluidas = a.excluir_las_que_no_aportan()
    print(f"\n  excluidas por no aportar:  {excluidas}")
    print(f"  funciones incluidas:       {len(a.incluidas)}")
    print(f"  ingreso tras excluir:      {a.ingreso:>12,}   <- NO BAJA")
    print(f"  coste tras excluir:        {a.coste:>12,}")
    print(f"  regimenes tras excluir:    {len(a.regimenes)}")

    carga = carga_regulatoria(len(a.regimenes), 70_000, 480_000, 5, 350_000, 0.08)
    print(f"\n  carga regulatoria anual:   {carga:>12,}")
    print(f"  facturacion necesaria:     {facturacion_necesaria(carga, 0.22):>12,.0f}")
    print(f"  saldo minimo por cliente:  {saldo_minimo(20, 0.018):>12,.0f}")
    print("\n  Reducir el alcance no baja el ingreso:")
    print("  las excluidas no lo generaban.")
    return 0


def cmd_build(args: argparse.Namespace) -> int:
    componentes = [
        Componente("nucleo de cuentas", False, True, 420_000, 265_000,
                   90_000, 185_000, Salida(True, True, 6, 340_000)),
        Componente("motor de cambio", True, True, 260_000, 120_000,
                   70_000, 95_000, Salida(True, True, 4, 180_000)),
        Componente("decision de credito", True, False, 310_000, 90_000,
                   0, 0, Salida(False, False, None, None)),
        Componente("registro de colateral", True, False, 380_000, 140_000,
                   120_000, 110_000, Salida(False, False, None, None)),
    ]
    print("CONSTRUIR, INTEGRAR O COMPRAR\n")
    for c in componentes:
        decision, motivo = c.decidir()
        print(f"  {c.nombre:<24} {decision.value.upper():<10} {motivo}")

    nucleo = componentes[0]
    print(f"\n  nucleo · construir a 5 anos:   {nucleo.coste_construir(5):>12,}")
    print(f"  nucleo · integrar a 5 anos:    {nucleo.coste_integrar(5):>12,}")
    print(f"  nucleo · integrar con salida:  "
          f"{nucleo.coste_integrar(5, con_una_salida=True):>12,}")

    cuota = concentracion_del_sector(14, 18)
    print(f"\n  proveedor de identidad usado por {cuota:.1%} del sector")
    print("  Integrarlo es lo seguro para la entidad")
    print("  y anade al riesgo del sector.")
    return 0


def cmd_tensions(args: argparse.Namespace) -> int:
    s = Sistema()
    s.decidir(Decision("liquidacion atomica", 10, "sin riesgo de principal", 3_096))
    s.decidir(Decision("horario ampliado", 5, "opera de 07:00 a 22:00", 1_238))
    s.decidir(Decision("conciliacion diaria", 7, "ventana de 24 horas", 26_000))
    s.decidir(Decision("lista blanca con espera", 9, "48 h de margen", 0))
    s.decidir(Decision("margen a 30 minutos", 12, "reaccion rapida", 0))

    s.fijar_tolerancia("liquidacion", 2.0, "consejo")
    s.fijar_tolerancia("llamadas de margen", 0.5, "consejo")

    t1 = s.declarar_tension("liquidacion atomica", "horario ampliado",
        "prefinanciar mas horas encarece el saldo ocioso")
    t2 = s.declarar_tension("lista blanca con espera", "margen a 30 minutos",
        "la espera de 48 h impide atender una urgencia legitima")

    print("TENSIONES DE DISENO\n")
    puede, motivo = s.puede_operar()
    print(f"  puede operar: {puede} · {motivo}")

    t1.resolver("ventana de 07:00 a 22:00 en vez de 24/7", 1_238)
    t2.resolver("via de excepcion con doble aprobacion y revision mensual", 8_000)

    puede, motivo = s.puede_operar()
    print(f"  tras resolver: {puede} · {motivo}\n")
    for t in s.tensiones:
        print(f"  {t.a.nombre} x {t.b.nombre}")
        print(f"    {t.descripcion}")
        print(f"    sacrificio: {t.sacrificio} ({t.cuantificacion:,})")

    incumplidas = s.tolerancias_incumplidas({"liquidacion": 1.0,
                                             "llamadas de margen": 0.7})
    print(f"\n  tolerancias incumplidas en un dia normal: {incumplidas}")
    print(f"  coste anual de las decisiones: {s.coste_anual():,}")
    return 0


def cmd_stress(args: argparse.Namespace) -> int:
    corresponsal = Proveedor("banco corresponsal",
                             frozenset({"emisor del deposito",
                                        "liquidador de pagos",
                                        "depositario de efectivo"}))
    e = Escenario(corresponsal, nivel_de_prueba=NivelDePrueba.ENTORNO_AISLADO)

    print("ESCENARIO DE TENSION\n")
    print(f"  fuente de correlacion: {corresponsal.nombre}")
    print(f"  papeles que desempena: {len(corresponsal.papeles)}")
    print(f"  es fuente de correlacion: {corresponsal.es_fuente_de_correlacion}\n")

    nuevos = e.desencadenar(72.0, "problemas de liquidez del corresponsal")
    print(f"  un solo fallo alcanza a {len(nuevos)} componentes:")
    for f in nuevos:
        print(f"    {f.componente}")

    e.anadir("colateral", 0.0, "caida de precio del 9 %")
    print(f"\n  componentes afectados: {e.componentes_afectados}")
    print(f"  el escenario demuestra algo: {e.demuestra_algo}")
    print(f"  nivel de prueba ejecutado: {e.nivel_de_prueba} "
          f"de {int(NivelDePrueba.CONMUTACION_NO_ANUNCIADA)}")

    d = desviaciones(0.09, 0.018, dias=1)
    print(f"\n  la caida del 9 % esta a {d:.1f} desviaciones de un dia normal")
    print("\n  Un proveedor con tres papeles es la fuente:")
    print("  un solo fallo rompe tres componentes a la vez.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="comando", required=True)
    for nombre, ayuda, func in (
        ("scope", "alcance y las cuatro preguntas", cmd_scope),
        ("build", "construir, integrar o comprar", cmd_build),
        ("tensions", "tensiones de diseno al integrar", cmd_tensions),
        ("stress", "escenario de tension y correlacion", cmd_stress),
    ):
        p = sub.add_parser(nombre, help=ayuda)
        p.set_defaults(func=func)
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
