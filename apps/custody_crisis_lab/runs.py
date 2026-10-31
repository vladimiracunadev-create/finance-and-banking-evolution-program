"""Riesgo de retiros masivos: demanda, cobertura y horizonte de liquidez.

Formulas:

    demanda del dia t     D_t = P_t * min(1, r0 + k * max(0, 1 - R_b,t))
    tasa maxima atendible r*  = A_liq / P     (sin vender activos no liquidos)
    cobertura de retiros  C   = A_liq / (r * P)

Variables: r0 = tasa base diaria de retiros (sin unidad), k = sensibilidad de
la corrida al deterioro del respaldo (sin unidad), R_b = respaldo bruto,
`descuento` = perdida al vender un activo no liquido en tension.

Supuestos: la relacion lineal entre deterioro y retiros es una hipotesis de
trabajo, no una ley; los activos no liquidos se venden con descuento fijo.
Limitacion: la reaccion real depende de la comunicacion y de si hay pausa de
retiros, factor que aqui se modela solo como `pausa_dias`.
"""

from __future__ import annotations

from dataclasses import dataclass

from .entity import Custodio


def tasa_maxima_atendible(entidad: Custodio) -> float:
    """Fraccion de P que se puede pagar hoy sin vender activos no liquidos."""
    return min(1.0, entidad.respaldo_disponible)


def cobertura_de_retiros(entidad: Custodio, tasa: float) -> float:
    """A_liq / (tasa * P). Menor que 1 significa que no se alcanza a pagar."""
    if tasa <= 0:
        raise ValueError("la tasa debe ser positiva")
    return entidad.activos_liquidos / (tasa * entidad.pasivos_clientes)


@dataclass(frozen=True)
class Dia:
    dia: int
    demanda: float
    pagado: float
    vendido_nominal: float
    impagado: float
    respaldo_bruto: float


def simular_corrida(
    entidad: Custodio,
    r0: float,
    k: float,
    dias: int,
    descuento: float = 0.05,
    pausa_dias: int = 0,
    reposiciones: dict[int, float] | None = None,
) -> list[Dia]:
    """Simula `dias` de retiros. Los dias dentro de `pausa_dias` no se paga nada.

    Se paga primero con activos liquidos; si faltan, se venden no liquidos con
    `descuento`. Lo que no se alcanza a pagar queda como `impagado` (el cliente
    sigue siendo acreedor: el pasivo baja solo por lo efectivamente pagado).

    `reposiciones` mapea dia -> monto liquido que ingresa al comienzo de ese dia.
    """
    if not 0.0 <= descuento < 1.0:
        raise ValueError("descuento debe estar en [0, 1)")
    if dias < 1 or r0 < 0 or k < 0 or pausa_dias < 0:
        raise ValueError("parametros invalidos")
    liquidos = entidad.activos_liquidos
    no_liquidos = entidad.activos_no_liquidos
    pasivos = entidad.pasivos_clientes
    historia: list[Dia] = []
    reposiciones = reposiciones or {}
    for dia in range(1, dias + 1):
        liquidos += reposiciones.get(dia, 0.0)
        rb = (liquidos + no_liquidos) / pasivos if pasivos > 0 else 1.0
        if dia <= pausa_dias:
            historia.append(Dia(dia, 0.0, 0.0, 0.0, 0.0, rb))
            continue
        tasa = min(1.0, r0 + k * max(0.0, 1.0 - rb))
        demanda = pasivos * tasa
        pagado_liquido = min(liquidos, demanda)
        liquidos -= pagado_liquido
        falta = demanda - pagado_liquido
        vendido_nominal = 0.0
        pagado_venta = 0.0
        if falta > 0 and no_liquidos > 0:
            vendido_nominal = min(no_liquidos, falta / (1.0 - descuento))
            pagado_venta = vendido_nominal * (1.0 - descuento)
            no_liquidos -= vendido_nominal
        pagado = pagado_liquido + pagado_venta
        pasivos -= pagado
        rb_despues = (liquidos + no_liquidos) / pasivos if pasivos > 0 else 1.0
        historia.append(
            Dia(dia, demanda, pagado, vendido_nominal, demanda - pagado, rb_despues)
        )
    return historia
