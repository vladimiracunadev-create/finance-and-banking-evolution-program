"""Cifras publicas del caso Binance 2026 y entidad estilizada del ejercicio.

IMPORTANTE. Las cifras de `CIFRAS_PUBLICAS` son ESTIMACIONES publicadas por la
entidad o por terceros el 29 y el 30 de octubre de 2026. Estan sujetas a
revision, difieren segun la fuente y NO son un balance auditado. Los pasivos con
clientes y la composicion de activos de `entidad_binance_estilizada()` son un
SUPUESTO del ejercicio, no datos de la entidad.

Fuentes (consultadas el 2026-10-30): CoinDesk, CNBC y Al Jazeera (lectura
directa); The Hacker News solo como resultado de busqueda.
Ver case-studies/custody/binance-2026.md.
"""

from __future__ import annotations

from .entity import Custodio

# metrica -> (valor en MUSD, quien lo reporta, nota)
CIFRAS_PUBLICAS: dict[str, tuple[float, str, str]] = {
    "sustraido_binance": (6_300.0, "Binance (via prensa)", "estimacion"),
    "sustraido_trm": (6_360.0, "TRM Labs (via CNBC)", "monto movido, aprox."),
    "sustraido_chainalysis": (6_430.0, "Chainalysis (via prensa)", "estimacion; CNBC cita 6 400"),
    "congelado_binance": (
        3_000.0,
        "Binance (via prensa)",
        "aprox.; un titular inicial citaba 2 540",
    ),
    "congelado_inicial": (2_540.0, "titular inicial", "reemplazado por ~3 000"),
    "congelado_tether": (1_570.0, "Tether (via prensa)", "USDT; 'mas de'; no contrastado en lectura directa"),
    "congelado_circle": (800.0, "Circle (via prensa)", "USDC; 'mas de'; no contrastado en lectura directa"),
    "reserva_compania": (6_340.0, "Binance (via CoinDesk)", "fondos propios apartados"),
    "reserva_ya_en_activo_afectado": (
        5_000.0,
        "Binance (via CoinDesk)",
        "ya mantenido en los mismos activos",
    ),
    "safu": (1_000.0, "CoinDesk", "habitualmente ~1 000 en bitcoin; saldo actual no confirmado"),
    "safu_cnbc": (1_200.0, "CNBC", "aprox.; discrepa con CoinDesk"),
    "activos_bajo_gestion": (
        155_000.0,
        "CoinMarketCap (via Al Jazeera)",
        "referencia de orden de magnitud",
    ),
}


def entidad_binance_estilizada() -> Custodio:
    """Entidad estilizada PRE-incidente.

    Supuestos del ejercicio: pasivos con clientes = activos bajo gestion
    reportados (155 000 MUSD); respaldo inicial 100 %; 85 % de los activos son
    liquidos a 24 h. No son datos de la entidad.
    """
    pasivos = CIFRAS_PUBLICAS["activos_bajo_gestion"][0]
    return Custodio(
        activos_liquidos=pasivos * 0.85,
        activos_no_liquidos=pasivos * 0.15,
        pasivos_clientes=pasivos,
        fondo_proteccion=CIFRAS_PUBLICAS["safu"][0],
    )
