"""Laboratorio de crisis de custodia digital.

Siete modulos, cada uno asociado a una pregunta que un comite se hace tras un
incidente con perdida extraordinaria de activos de clientes:

    entity      que tiene y que debe la entidad custodia (respaldo antes)
    incident    sustraido, congelado, recuperable y perdido NO son lo mismo
    runs        riesgo de retiros masivos y horizonte de liquidez
    replenish   cuanto cuesta volver al 100 % y con que fuentes
    costs       costo total del incidente, componente por componente
    recovery    trayectoria del respaldo y plan de continuidad por fases
    cases       cifras publicas del caso Binance 2026 como estimaciones

Todo es didactico y trabaja con datos sinteticos o con estimaciones publicas
declaradas como tales. No se conecta a ninguna red, no mueve fondos y no
recomienda ninguna inversion. Las unidades son millones de USD (MUSD) salvo que
se indique otra cosa.
"""

__all__ = [
    "cases",
    "costs",
    "entity",
    "incident",
    "recovery",
    "replenish",
    "runs",
]
