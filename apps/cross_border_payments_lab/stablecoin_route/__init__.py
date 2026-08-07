"""Comparacion honesta de una ruta con stablecoin frente a la clasica.

El modulo existe para hacer imposible el error de analisis mas comun: comparar
el tramo de transferencia —que cuesta centimos— con la ruta clasica completa.

Aqui se compara ruta completa contra ruta completa, se imputa la prefinanciacion
a la clasica y se descompone el ahorro POR FUENTE, aislando el porcentaje
atribuible al registro distribuido.

La stablecoin del laboratorio es SINTETICA.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class RutaClasica:
    comision_envio: Decimal
    diferencial_pb: Decimal
    comision_por_intermediario: Decimal
    intermediarios: int
    comision_receptor: Decimal
    saldo_prefinanciado: Decimal
    coste_fondeo_anual: Decimal
    operaciones_anuales: int
    horas_hasta_disponible: Decimal
    # Cada eslabon anade comision Y diferencial: es lo que hace que el coste
    # crezca mas rapido que el numero de intermediarios.
    diferencial_por_intermediario_pb: Decimal = Decimal(0)
    # Parte del coste que corresponde a la mensajeria. Se aisla para poder
    # comparar con la comision de red y saber que parte del ahorro es
    # atribuible al registro y cual a la topologia.
    coste_mensajeria: Decimal = Decimal(0)

    @property
    def diferencial_efectivo_pb(self) -> Decimal:
        adicionales = max(self.intermediarios - 1, 0)
        return self.diferencial_pb + self.diferencial_por_intermediario_pb * adicionales

    def coste(self, importe: Decimal, con_prefinanciacion: bool = True) -> Decimal:
        total = (
            self.comision_envio
            + importe * self.diferencial_efectivo_pb / Decimal(10_000)
            + self.comision_por_intermediario * self.intermediarios
            + self.comision_receptor
        )
        if con_prefinanciacion:
            total += self.prefinanciacion_por_operacion()
        return total

    def prefinanciacion_por_operacion(self) -> Decimal:
        if not self.operaciones_anuales:
            return Decimal(0)
        return (
            self.saldo_prefinanciado * self.coste_fondeo_anual
        ) / Decimal(self.operaciones_anuales)


@dataclass(frozen=True)
class RutaStablecoin:
    entrada_comision_pct: Decimal
    entrada_diferencial_pb: Decimal
    comision_red: Decimal
    salida_comision_pct: Decimal
    salida_diferencial_pb: Decimal
    comision_retiro: Decimal
    minutos_tenencia: int
    horas_hasta_disponible: Decimal

    def coste(self, importe: Decimal) -> Decimal:
        return (
            importe * self.entrada_comision_pct
            + importe * self.entrada_diferencial_pb / Decimal(10_000)
            + self.comision_red
            + importe * self.salida_comision_pct
            + importe * self.salida_diferencial_pb / Decimal(10_000)
            + self.comision_retiro
        )

    def tramos(self, importe: Decimal) -> dict[str, Decimal]:
        """Los cinco tramos. El de la tecnologia es el mas barato."""
        return {
            "entrada": importe * self.entrada_comision_pct
            + importe * self.entrada_diferencial_pb / Decimal(10_000),
            "transferencia": self.comision_red,
            "tenencia": Decimal(0),
            "salida": importe * self.salida_comision_pct
            + importe * self.salida_diferencial_pb / Decimal(10_000),
            "ultima_milla": self.comision_retiro,
        }

    def exposicion(self, importe: Decimal, minutos_reales: int | None = None) -> Decimal:
        """Exposicion durante la tenencia.

        `minutos_reales` permite modelar la salida bloqueada: la exposicion NO
        es la planificada, es la que resulte.
        """
        minutos = self.minutos_tenencia if minutos_reales is None else minutos_reales
        return importe * Decimal(minutos) / Decimal(60 * 24)


def comparar(
    clasica: RutaClasica, stablecoin: RutaStablecoin, importe: Decimal
) -> dict[str, object]:
    coste_clasica = clasica.coste(importe)
    coste_stable = stablecoin.coste(importe)
    return {
        "importe": importe,
        "coste_clasica": coste_clasica,
        "coste_stablecoin": coste_stable,
        "ahorro": coste_clasica - coste_stable,
        "gana_stablecoin": coste_stable < coste_clasica,
        "horas_clasica": clasica.horas_hasta_disponible,
        "horas_stablecoin": stablecoin.horas_hasta_disponible,
    }


def descomponer_ahorro(
    clasica: RutaClasica, stablecoin: RutaStablecoin, importe: Decimal
) -> dict[str, Decimal]:
    """Reparte el ahorro por FUENTE. Las partes SUMAN el ahorro total.

    Ninguna de las cinco fuentes es «la tecnologia» salvo la ultima, que es la
    diferencia entre lo que cuesta mover el mensaje por la via clasica y lo que
    cuesta registrar la operacion. Suele ser una fraccion minima del total, y
    ese es exactamente el resultado que el laboratorio busca.
    """
    intermediarios = (
        clasica.comision_por_intermediario * clasica.intermediarios
        - clasica.coste_mensajeria
    )
    prefinanciacion = clasica.prefinanciacion_por_operacion()

    diferencial_clasica = importe * clasica.diferencial_efectivo_pb / Decimal(10_000)
    diferencial_stable = (
        importe * stablecoin.entrada_diferencial_pb / Decimal(10_000)
        + importe * stablecoin.salida_diferencial_pb / Decimal(10_000)
    )
    diferencial = diferencial_clasica - diferencial_stable

    comisiones_clasica = clasica.comision_envio + clasica.comision_receptor
    comisiones_stable = (
        importe * stablecoin.entrada_comision_pct
        + importe * stablecoin.salida_comision_pct
        + stablecoin.comision_retiro
    )
    comisiones = comisiones_clasica - comisiones_stable

    mensajeria = clasica.coste_mensajeria - stablecoin.comision_red

    return {
        "intermediarios_evitados": intermediarios,
        "prefinanciacion_evitada": prefinanciacion,
        "menor_diferencial": diferencial,
        "comisiones_de_servicio": comisiones,
        "mensajeria_frente_a_red": mensajeria,
    }


def porcentaje_atribuible_al_registro(
    clasica: RutaClasica, stablecoin: RutaStablecoin, importe: Decimal
) -> Decimal:
    """Porcentaje del ahorro que produce el registro y no la topologia."""
    fuentes = descomponer_ahorro(clasica, stablecoin, importe)
    total = sum(fuentes.values())
    if total <= 0:
        return Decimal(0)
    return fuentes["mensajeria_frente_a_red"] / total * Decimal(100)


def enrutar(
    hay_enlace_directo: bool,
    intermediarios: int,
    salida_liquida: bool,
    minutos_tenencia: int,
    emisor_dentro_de_limite: bool,
) -> tuple[str, str]:
    """La regla de la clase 14. Devuelve (ruta, motivo)."""
    if hay_enlace_directo:
        return ("enlace_pagos_inmediatos", "mas barato y sin riesgo de emisor")
    if intermediarios <= 1:
        return ("clasica", "cadena corta: la ruta con stablecoin no compensa")
    if not salida_liquida:
        return ("clasica", "salida ilíquida en destino")
    if minutos_tenencia >= 60:
        return ("clasica", "tenencia estimada por encima del limite de 60 minutos")
    if not emisor_dentro_de_limite:
        return ("clasica", "exposicion al emisor fuera del limite aprobado")
    return ("stablecoin", f"cadena de {intermediarios} intermediarios evitada")
