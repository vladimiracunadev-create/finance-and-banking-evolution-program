"""Interfaz de linea de comandos del motor de perimetro regulatorio.

Uso:
    python apps/regulatory_perimeter_engine/cli.py perimeter
    python apps/regulatory_perimeter_engine/cli.py qualification
    python apps/regulatory_perimeter_engine/cli.py compliance
    python apps/regulatory_perimeter_engine/cli.py dossier
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from apps.regulatory_perimeter_engine.compliance import (  # noqa: E402
    MapaDeTerceros,
    Salvaguarda,
    Vigilancia,
    justifica_el_indicador,
)
from apps.regulatory_perimeter_engine.dossier import (  # noqa: E402
    Expediente,
    Nivel,
)
from apps.regulatory_perimeter_engine.perimeter import (  # noqa: E402
    Entidad,
    Regimen,
    informe,
)
from apps.regulatory_perimeter_engine.qualification import (  # noqa: E402
    Instrumento,
    coste_de_una_recalificacion,
)


def cmd_perimeter(args: argparse.Namespace) -> int:
    entidad = Entidad("plataforma")
    entidad.declarar()  # no declara ningun regimen

    hechos = [
        ("recibe_fondos", "los usuarios transfieren a una cuenta suya", "condiciones 4.1"),
        ("obligacion_de_devolver", "el saldo se retira cuando el usuario quiera", "condiciones 4.3"),
        ("tiene_las_claves", "la plataforma custodia las claves", "documentacion tecnica"),
        ("casa_ordenes_de_terceros", "la aplicacion casa ordenes entre usuarios", "manual de usuario"),
        ("ejecuta_por_cuenta_ajena", "ejecuta la orden del cliente", "condiciones 7.2"),
        ("destaca_instrumentos", "tres activos destacados en portada", "captura del 2026-08-06"),
        ("cobra_por_destacar", "tarifa de destaque publicada", "tarifario 2026"),
        ("convierte_moneda_con_margen", "cambio con margen propio", "tarifario 2026"),
        ("presta_fondos", "prestamo contra el saldo", "condiciones 9.1"),
    ]
    for clave, descripcion, fuente in hechos:
        entidad.observar(clave, descripcion, fuente)

    resultado = informe(entidad)
    print("PERIMETRO · determinado por hechos observables\n")
    print(f"  regimenes DECLARADOS:     {len(resultado['declarado'])}")
    print(f"  regimenes EFECTIVOS:      {len(resultado['hecho'])}")
    print(f"  ejercidos SIN DECLARAR:   {len(resultado['no_declarado'])}\n")
    for regimen in resultado["no_declarado"]:
        fuentes = ", ".join(resultado["hecho"][regimen])
        print(f"    {regimen:<16} evidencia: {fuentes}")
    print("\n  Y aunque no se activara ninguno, siguen aplicando:")
    for norma in resultado["siempre_aplican"]:
        print(f"    · {norma}")
    return 0


def cmd_qualification(args: argparse.Namespace) -> int:
    token = Instrumento(
        nombre="token de logistica",
        servicio_en_funcionamiento=False,
        se_consume_al_usarlo=True,
        mercado_secundario_desde_el_inicio=True,
        financia_el_desarrollo=True,
        promocion=[
            "El token da acceso a la plataforma de seguimiento de envios.",
            "A medida que crezca la red, la demanda del token aumentara.",
        ],
        compradores_que_usan_el_servicio=0.08,
    )

    criterios = token.criterios()
    print(f"CALIFICACION · {token.nombre}\n")
    print(f"  1 inversion de dinero:      {criterios.inversion_de_dinero}")
    print(f"  2 proyecto comun:           {criterios.proyecto_comun}")
    print(f"  3 expectativa de beneficio: {criterios.expectativa_de_beneficio}")
    print(f"  4 esfuerzo de un tercero:   {criterios.esfuerzo_de_un_tercero}")
    print(f"\n  criterios cumplidos: {criterios.cuantos} de 4")
    print(f"  calificacion:        {token.calificar().value}")
    print(f"  utilidad aparente:   {token.utilidad_aparente}")

    frases = token.frases_que_crean_expectativa()
    print(f"\n  frases de la promocion que califican: {len(frases)}")
    for frase in frases:
        print(f"    «{frase}»")

    coste = coste_de_una_recalificacion(30_000_000, 400_000, token.calificar())
    print(f"\n  ahorro por calificar como utilidad: {coste['ahorro']:>12,}")
    print(f"  riesgo de la recalificacion:        {coste['riesgo']:>12,}")
    print(f"  el ahorro es el {coste['ahorro_sobre_riesgo']:.1%} del riesgo")
    return 0


def cmd_compliance(args: argparse.Namespace) -> int:
    salvaguarda = Salvaguarda(
        a_nombre_de_clientes=True,
        contrato_especifico=True,
        renuncia_a_compensar=False,
        conciliacion_diaria=False,
        saldo_de_clientes=68_000_000,
        deuda_con_el_banco=4_200_000,
        diferencia_de_conciliacion=900_000,
    )
    print("SALVAGUARDA · las cuatro preguntas\n")
    for pregunta in ("a_nombre_de_clientes", "contrato_especifico",
                     "renuncia_a_compensar", "conciliacion_diaria"):
        marca = "OK " if getattr(salvaguarda, pregunta) else "NO "
        print(f"  [{marca}] {pregunta}")
    exposicion = salvaguarda.exposicion()
    print(f"\n  por compensacion:  {exposicion['por_compensacion']:>12,}")
    print(f"  por conciliacion:  {exposicion['por_conciliacion']:>12,}")
    print(f"  recuperable:       {exposicion['recuperable']:>12,}"
          f"  ({exposicion['recuperable'] / 68_000_000:.1%})")

    antes = Vigilancia(alertas=3_640, confirmados=44, casos_reales=62,
                       coste_por_alerta=18)
    despues = antes.con_indicador(alertas_extra=940, confirmados_extra=9)
    decision = justifica_el_indicador(antes, despues, valor_de_un_caso=45_000)

    print("\nVIGILANCIA\n")
    print(f"  precision antes:      {antes.precision:>8.2%}")
    print(f"  exhaustividad antes:  {antes.exhaustividad:>8.2%}")
    print(f"  precision despues:    {despues.precision:>8.2%}")
    print(f"  exhaustividad despues:{despues.exhaustividad:>8.2%}")
    print(f"\n  coste MEDIO por caso:    {decision['coste_medio_por_caso']:>10,.0f}")
    print(f"  coste MARGINAL por caso: {decision['coste_marginal_por_caso']:>10,.0f}")
    print(f"  se justifica: {decision['se_justifica']}")
    print("  (decide el marginal frente al valor, no el medio)")

    mapa = MapaDeTerceros()
    mapa.registrar("p1", "C")
    mapa.registrar("p2", "C")
    mapa.registrar("p3", "D")
    for i in range(19):
        mapa.depende(f"e{i}", "p1" if i % 2 == 0 else "p2")
    for i in range(19, 22):
        mapa.depende(f"e{i}", "p3")

    print("\nTERCEROS CRITICOS\n")
    print(f"  proveedores distintos: {len(mapa.proveedores)}")
    for nombre, cuota in sorted(mapa.concentracion_por_proveedor().items()):
        print(f"    proveedor {nombre}: {cuota:>6.1%}")
    for nombre, cuota in sorted(mapa.concentracion_por_infraestructura().items()):
        print(f"    INFRAESTRUCTURA {nombre}: {cuota:>6.1%}")
    print(f"\n  criticas al umbral del 40 %: {mapa.criticos(0.40)}")
    print("  Contar proveedores da diversificacion aparente.")
    return 0


def cmd_dossier(args: argparse.Namespace) -> int:
    expediente = Expediente("entidad de custodia y cambio", clientes=42_000)
    for pieza in (
        "perimetro", "calificacion", "autorizacion", "regimen_por_jurisdiccion",
        "salvaguarda", "informacion_y_conducta", "prevencion_de_lavado",
        "datos_personales", "vigilancia_de_mercado", "resiliencia",
        "prudencial", "hallazgos_y_remediacion",
    ):
        expediente.afirmar(pieza, f"seccion {pieza} elaborada", f"documento-{pieza}.pdf")

    expediente.registrar_hallazgo(
        Nivel.BLOQUEANTE, ("perimetro", "resiliencia"),
        "custodia no declarada: la entidad tiene 4 de 5 partes", 42_000)
    expediente.registrar_hallazgo(
        Nivel.BLOQUEANTE, ("salvaguarda", "prevencion_de_lavado"),
        "devoluciones desde la cuenta operativa", 42_000)
    expediente.registrar_hallazgo(
        Nivel.BLOQUEANTE, ("calificacion", "informacion_y_conducta"),
        "la promocion crea expectativa de beneficio", 11_400)
    expediente.registrar_hallazgo(
        Nivel.RELEVANTE, ("datos_personales", "vigilancia_de_mercado"),
        "tratamiento de direcciones vinculadas no declarado", 42_000)

    print(f"EXPEDIENTE · {expediente.entidad}\n")
    print(f"  piezas presentes: {len(expediente.piezas_presentes)} de 12")
    print(f"  completo:         {expediente.completo}")
    print(f"  la revision miro donde debia: "
          f"{expediente.revision_miro_donde_debia}\n")
    print("  HALLAZGOS PRIORIZADOS POR EFECTO SOBRE EL CLIENTE\n")
    for h in expediente.priorizados():
        print(f"    nivel {h.nivel}  {h.clientes_afectados:>7,} clientes"
              f"  {h.piezas[0]} x {h.piezas[1]}")
        print(f"              {h.descripcion}")

    puede, motivo = expediente.puede_operar()
    print(f"\n  puede operar: {puede} · {motivo}")
    print("\n  Ninguno se veia dentro de su propia pieza:")
    print("  los cuatro aparecen al leer por parejas.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="comando", required=True)

    p = sub.add_parser("perimeter", help="regimenes activados por hechos")
    p.set_defaults(func=cmd_perimeter)

    p = sub.add_parser("qualification", help="los cuatro criterios y la promocion")
    p.set_defaults(func=cmd_qualification)

    p = sub.add_parser("compliance", help="salvaguarda, vigilancia y terceros")
    p.set_defaults(func=cmd_compliance)

    p = sub.add_parser("dossier", help="expediente y lectura cruzada")
    p.set_defaults(func=cmd_dossier)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
