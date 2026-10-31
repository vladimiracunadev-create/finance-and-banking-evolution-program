"""Trayectoria del respaldo y plan de recuperacion y continuidad.

Formula (respaldo bruto en el dia t):

    R(t) = (A_liq + A_nl - S + Rest(t) + Rep(t)) / P

con Rest(t) y Rep(t) acumulados de restituciones y reposiciones hasta t.

El plan por fases fija, para cada una, el objetivo, la accion, el responsable,
la condicion de entrada y la condicion de salida. Una fase no termina por
calendario sino cuando se cumple su condicion de salida.

Limitacion: el calendario de restituciones es un supuesto; la trayectoria es un
instrumento para ordenar decisiones, no un pronostico.
"""

from __future__ import annotations

from dataclasses import dataclass

from .entity import Custodio


def trayectoria_de_respaldo(
    entidad_antes: Custodio,
    sustraido: float,
    restituciones: dict[int, float],
    reposiciones: dict[int, float],
    horizonte: int,
) -> list[tuple[int, float]]:
    """Respaldo bruto dia a dia. Los dicts mapean dia -> monto que entra ese dia."""
    if horizonte < 0 or sustraido < 0:
        raise ValueError("parametros invalidos")
    resultado = []
    acumulado = 0.0
    for dia in range(0, horizonte + 1):
        acumulado += restituciones.get(dia, 0.0) + reposiciones.get(dia, 0.0)
        activos = entidad_antes.activos_totales - sustraido + acumulado
        resultado.append((dia, activos / entidad_antes.pasivos_clientes))
    return resultado


@dataclass(frozen=True)
class Fase:
    nombre: str
    horizonte: str
    accion: str
    responsable: str
    entrada: str
    salida: str


PLAN = [
    Fase(
        "1. Contencion",
        "0-4 h",
        "Pausar salidas, aislar hot wallets, rotar credenciales, preservar evidencia",
        "CISO y jefe de operaciones",
        "Alerta confirmada de transferencia no autorizada",
        "Vector cerrado y ningun movimiento adicional no autorizado",
    ),
    Fase(
        "2. Cuantificacion",
        "4-48 h",
        "Conciliar activos y pasivos por activo; clasificar S, F, p y perdida",
        "Finanzas y riesgos",
        "Contencion completa",
        "Cifra de brecha firmada y revisada por segunda linea",
    ),
    Fase(
        "3. Comunicacion y reporte",
        "6-72 h",
        "Informar a clientes, supervisor, fuerzas de seguridad y emisores",
        "Cumplimiento y comunicaciones",
        "Primera cifra de brecha disponible",
        "Informes enviados y canal unico de actualizacion activo",
    ),
    Fase(
        "4. Reposicion",
        "1-14 dias",
        "Reponer hasta el objetivo de respaldo con las fuentes aprobadas",
        "Tesoreria",
        "Brecha firmada y fuentes aprobadas por el comite",
        "Respaldo bruto >= objetivo con activos propios",
    ),
    Fase(
        "5. Reapertura gradual",
        "2-10 dias",
        "Reanudar retiros por tramos, con limites y monitoreo de cola",
        "Operaciones y riesgos",
        "Respaldo disponible cubre la demanda esperada con margen",
        "Retiros normalizados dos dias consecutivos",
    ),
    Fase(
        "6. Verificacion independiente",
        "7-30 dias",
        "Proof of Reserves y de pasivos con alcance definido; auditoria forense",
        "Auditoria y tercero independiente",
        "Reapertura estable",
        "Informe publicado con alcance, fecha de corte y excepciones",
    ),
    Fase(
        "7. Aprendizaje",
        "30-90 dias",
        "Corregir causa raiz, segregar llaves y funciones, probar el plan",
        "Comite de riesgos",
        "Informe forense final",
        "Plan de remediacion cerrado y prueba de continuidad aprobada",
    ),
]
