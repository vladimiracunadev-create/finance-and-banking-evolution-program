"""Grafo de exposicion: directa, indirecta y por dependencia comun.

La clase 14 sostiene que una entidad puede declarar exposicion cero y tener una
necesidad de liquidez de 117 millones. El grafo lo hace visible, y el nodo que
mas importa —el proveedor de precios— no aparece en ningun balance.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Entidad:
    nombre: str
    capital: int
    posicion_directa: int = 0
    custodia_por_terceros: int = 0
    proveedor_de_precios: str | None = None
    plataforma: str | None = None
    depositario: str | None = None

    @property
    def fraccion_en_riesgo(self) -> float:
        if self.capital == 0:
            return 0.0
        return self.posicion_directa / self.capital


@dataclass(frozen=True)
class Vinculo:
    """Relacion dirigida: `origen` esta expuesto a `destino` por `importe`."""

    origen: str
    destino: str
    importe: int
    tipo: str = "credito"


@dataclass
class Grafo:
    entidades: dict[str, Entidad] = field(default_factory=dict)
    vinculos: list[Vinculo] = field(default_factory=list)

    def agregar(self, entidad: Entidad) -> None:
        self.entidades[entidad.nombre] = entidad

    def vincular(
        self, origen: str, destino: str, importe: int, tipo: str = "credito"
    ) -> None:
        for nombre in (origen, destino):
            if nombre not in self.entidades:
                raise KeyError(f"entidad desconocida: {nombre}")
        self.vinculos.append(Vinculo(origen, destino, importe, tipo))

    def exposicion_directa(self, nombre: str) -> int:
        return self.entidades[nombre].posicion_directa

    def exposicion_indirecta(self, nombre: str) -> dict[str, int]:
        """Exposicion de segundo grado, por contraparte.

        El metodo supone traslado lineal de la perdida al capital. En una
        quiebra no lo es: sirve para ORDENAR contrapartes, no para predecir el
        importe exacto, y asi hay que declararlo en el informe.
        """
        resultado: dict[str, int] = {}
        for vinculo in self.vinculos:
            if vinculo.origen != nombre or vinculo.tipo != "credito":
                continue
            contraparte = self.entidades[vinculo.destino]
            expuesto = round(vinculo.importe * contraparte.fraccion_en_riesgo)
            if expuesto:
                resultado[vinculo.destino] = expuesto
        return resultado

    def exposicion_economica(self, nombre: str) -> int:
        return self.exposicion_directa(nombre) + sum(
            self.exposicion_indirecta(nombre).values()
        )

    def dependencias_comunes(self) -> dict[str, list[str]]:
        """Proveedores compartidos por dos o mas entidades.

        Es el canal menos visible: no esta en ningun balance y se descubre
        leyendo condiciones de servicio y cuestionarios de contraparte.
        """
        mapa: dict[str, list[str]] = {}
        for entidad in self.entidades.values():
            for atributo in ("proveedor_de_precios", "plataforma", "depositario"):
                valor = getattr(entidad, atributo)
                if valor is None:
                    continue
                clave = f"{atributo}:{valor}"
                mapa.setdefault(clave, []).append(entidad.nombre)
        return {k: sorted(v) for k, v in mapa.items() if len(v) > 1}

    def nodo_critico(self) -> tuple[str, list[str]] | None:
        """La dependencia comun que afecta a mas entidades."""
        comunes = self.dependencias_comunes()
        if not comunes:
            return None
        clave = max(comunes, key=lambda k: len(comunes[k]))
        return clave, comunes[clave]

    def cascada(
        self,
        nombre: str,
        caida: float,
        disposicion_de_lineas: float,
        retirada_de_depositos: float,
    ) -> dict:
        """Necesidad de liquidez de `nombre` ante una caida del instrumento.

        Recoge dos canales que la exposicion directa no ve: las lineas que las
        contrapartes disponen a la vez, y los depositos que un custodio sin
        posicion propia retira por presion de sus clientes.
        """
        deterioro: dict[str, float] = {}
        lineas = 0
        depositos = 0

        for vinculo in self.vinculos:
            if vinculo.origen != nombre:
                continue
            contraparte = self.entidades[vinculo.destino]
            if vinculo.tipo == "credito":
                perdida = contraparte.posicion_directa * caida
                deterioro[contraparte.nombre] = (
                    perdida / contraparte.capital if contraparte.capital else 0.0
                )
                lineas += round(vinculo.importe * disposicion_de_lineas)
            elif vinculo.tipo == "deposito_recibido":
                depositos += round(vinculo.importe * retirada_de_depositos)

        return {
            "deterioro_de_contrapartes": deterioro,
            "lineas_dispuestas": lineas,
            "depositos_retirados": depositos,
            "necesidad_de_liquidez": lineas + depositos,
            "exposicion_declarada": self.exposicion_directa(nombre),
        }
