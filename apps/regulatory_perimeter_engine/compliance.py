"""Cumplimiento: salvaguarda, vigilancia y concentracion de terceros.

Tres afirmaciones que este modulo hace comprobables:

1. Clase 6: la salvaguarda falla casi siempre en la misma pregunta, la renuncia
   del banco a compensar. Sin ella, la proteccion se evapora.
2. Clase 11: el umbral de vigilancia decide precision y exhaustividad, y la
   decision de anadir un indicador se toma con el coste MARGINAL frente al valor
   del caso, no con el coste medio.
3. Clase 14: contar proveedores no es medir concentracion; hay que contar
   infraestructuras, y para eso hace falta la subcontratacion.
"""

from __future__ import annotations

from dataclasses import dataclass, field

# Las cuatro preguntas de la clase 6, en orden. La tercera es la que falla.
PREGUNTAS_DE_SALVAGUARDA = (
    "a_nombre_de_clientes",
    "contrato_especifico",
    "renuncia_a_compensar",
    "conciliacion_diaria",
)


@dataclass
class Salvaguarda:
    """Verificacion de la proteccion patrimonial de los fondos del cliente."""

    a_nombre_de_clientes: bool
    contrato_especifico: bool
    renuncia_a_compensar: bool
    conciliacion_diaria: bool
    saldo_de_clientes: int = 0
    deuda_con_el_banco: int = 0
    diferencia_de_conciliacion: int = 0

    def fallos(self) -> list[str]:
        return [p for p in PREGUNTAS_DE_SALVAGUARDA if not getattr(self, p)]

    @property
    def acreditada(self) -> bool:
        return not self.fallos()

    def exposicion(self) -> dict[str, int]:
        """Cuanto puede perder el cliente por cada fallo, en un concurso."""
        por_compensacion = 0 if self.renuncia_a_compensar else self.deuda_con_el_banco
        por_conciliacion = 0 if self.conciliacion_diaria else self.diferencia_de_conciliacion
        recuperable = self.saldo_de_clientes - por_compensacion - por_conciliacion
        return {
            "por_compensacion": por_compensacion,
            "por_conciliacion": por_conciliacion,
            "recuperable": max(recuperable, 0),
        }


@dataclass
class Vigilancia:
    """Sistema de deteccion de conducta anomala."""

    alertas: int
    confirmados: int
    casos_reales: int
    coste_por_alerta: int

    @property
    def precision(self) -> float:
        return self.confirmados / self.alertas if self.alertas else 0.0

    @property
    def exhaustividad(self) -> float:
        return self.confirmados / self.casos_reales if self.casos_reales else 0.0

    @property
    def coste(self) -> int:
        return self.alertas * self.coste_por_alerta

    def con_indicador(self, alertas_extra: int, confirmados_extra: int) -> "Vigilancia":
        return Vigilancia(
            alertas=self.alertas + alertas_extra,
            confirmados=self.confirmados + confirmados_extra,
            casos_reales=self.casos_reales,
            coste_por_alerta=self.coste_por_alerta,
        )


def justifica_el_indicador(
    antes: Vigilancia, despues: Vigilancia, valor_de_un_caso: int
) -> dict:
    """Decide con el coste MARGINAL, no con el medio.

    Comparar el coste marginal con el coste medio por caso es el error de la
    clase 11 y puede invertir la conclusion.
    """
    casos_extra = despues.confirmados - antes.confirmados
    coste_extra = despues.coste - antes.coste
    if casos_extra <= 0:
        return {"casos_extra": 0, "se_justifica": False}
    return {
        "casos_extra": casos_extra,
        "coste_extra": coste_extra,
        "coste_marginal_por_caso": coste_extra / casos_extra,
        "coste_medio_por_caso": antes.coste / antes.confirmados
        if antes.confirmados
        else 0.0,
        "valor_de_los_casos": casos_extra * valor_de_un_caso,
        "se_justifica": casos_extra * valor_de_un_caso > coste_extra,
    }


@dataclass
class Proveedor:
    """Un proveedor y la infraestructura que usa por debajo."""

    nombre: str
    infraestructura: str


@dataclass
class MapaDeTerceros:
    """Dependencias del sector, con subcontratacion.

    Contar proveedores da una diversificacion aparente; contar infraestructuras
    da la real (clase 14).
    """

    proveedores: dict[str, Proveedor] = field(default_factory=dict)
    dependencias: dict[str, list[str]] = field(default_factory=dict)

    def registrar(self, nombre: str, infraestructura: str) -> None:
        self.proveedores[nombre] = Proveedor(nombre, infraestructura)

    def depende(self, entidad: str, proveedor: str) -> None:
        if proveedor not in self.proveedores:
            raise KeyError(f"proveedor desconocido: {proveedor}")
        self.dependencias.setdefault(entidad, []).append(proveedor)

    @property
    def entidades(self) -> int:
        return len(self.dependencias)

    def concentracion_por_proveedor(self) -> dict[str, float]:
        cuenta: dict[str, int] = {}
        for usados in self.dependencias.values():
            for proveedor in set(usados):
                cuenta[proveedor] = cuenta.get(proveedor, 0) + 1
        return {k: v / self.entidades for k, v in cuenta.items()} if self.entidades else {}

    def concentracion_por_infraestructura(self) -> dict[str, float]:
        cuenta: dict[str, int] = {}
        for usados in self.dependencias.values():
            infras = {self.proveedores[p].infraestructura for p in usados}
            for infra in infras:
                cuenta[infra] = cuenta.get(infra, 0) + 1
        return {k: v / self.entidades for k, v in cuenta.items()} if self.entidades else {}

    def criticos(self, umbral: float) -> list[str]:
        """Infraestructuras que superan el umbral de designacion."""
        return sorted(
            k for k, v in self.concentracion_por_infraestructura().items() if v >= umbral
        )
