"""Arboles de Merkle con sumas, inclusion y exclusion.

Tres decisiones de diseno que la clase 2 justifica:

1. PREFIJOS DISTINTOS para hoja y para nodo interno. Sin ellos, un par de hojas
   y un nodo interno pueden producir el mismo resumen, y existen dos conjuntos
   con la misma raiz.
2. SUMAS en cada nodo. Sin ellas, omitir una hoja no se detecta: cada
   participante verifica la suya y nadie ve la ausencia.
3. ORDEN TOTAL. Sin el, no hay prueba de exclusion, y «esta garantia NO esta
   pignorada» es la pregunta que un banco necesita responder.
"""

from __future__ import annotations

import bisect
import hashlib
from dataclasses import dataclass, field

PREFIJO_HOJA = b"\x00"
PREFIJO_NODO = b"\x01"


def _hoja(clave: str, valor: int) -> bytes:
    return hashlib.sha256(
        PREFIJO_HOJA + clave.encode("utf-8") + b"|" + str(valor).encode("ascii")
    ).digest()


def _nodo(izquierda: bytes, derecha: bytes) -> bytes:
    return hashlib.sha256(PREFIJO_NODO + izquierda + derecha).digest()


@dataclass(frozen=True)
class PruebaInclusion:
    clave: str
    valor: int
    camino: list[tuple[bytes, bool]]

    @property
    def tamano_bytes(self) -> int:
        return len(self.camino) * 32


@dataclass(frozen=True)
class PruebaExclusion:
    buscado: str
    anterior: str | None
    siguiente: str | None
    prueba_anterior: PruebaInclusion | None
    prueba_siguiente: PruebaInclusion | None


@dataclass
class ArbolMerkle:
    """Arbol sobre un conjunto ORDENADO de pares clave-valor."""

    hojas: dict[str, int] = field(default_factory=dict)
    con_sumas: bool = True

    @property
    def claves(self) -> list[str]:
        return sorted(self.hojas)

    def agregar(self, clave: str, valor: int) -> None:
        self.hojas[clave] = valor

    def _niveles(self) -> list[list[tuple[bytes, int]]]:
        """Devuelve los niveles del arbol, de las hojas a la raiz."""
        nivel = [(_hoja(c, self.hojas[c]), self.hojas[c]) for c in self.claves]
        if not nivel:
            return [[(hashlib.sha256(PREFIJO_NODO).digest(), 0)]]
        niveles = [nivel]
        while len(nivel) > 1:
            siguiente: list[tuple[bytes, int]] = []
            for i in range(0, len(nivel), 2):
                if i + 1 >= len(nivel):
                    # Nodo suelto: se PROMUEVE tal cual al nivel siguiente.
                    # Duplicarlo consigo mismo sumaria su valor dos veces y el
                    # total de la raiz dejaria de ser la suma real, que es
                    # justo la propiedad por la que existe este arbol.
                    siguiente.append(nivel[i])
                    continue
                izq, der = nivel[i], nivel[i + 1]
                siguiente.append((_nodo(izq[0], der[0]), izq[1] + der[1]))
            niveles.append(siguiente)
            nivel = siguiente
        return niveles

    def raiz(self) -> bytes:
        return self._niveles()[-1][0][0]

    def total(self) -> int:
        """Suma que declara la raiz. Omitir una hoja la reduce, y se ve."""
        if not self.con_sumas:
            raise ValueError("este arbol se construyo sin sumas")
        return self._niveles()[-1][0][1]

    def probar(self, clave: str) -> PruebaInclusion:
        if clave not in self.hojas:
            raise KeyError(clave)
        indice = self.claves.index(clave)
        niveles = self._niveles()
        camino: list[tuple[bytes, bool]] = []
        for nivel in niveles[:-1]:
            pareja = indice ^ 1
            if pareja < len(nivel):
                camino.append((nivel[pareja][0], indice % 2 == 1))
            # Si no hay pareja, el nodo se promovio: no hay hermano que
            # aportar y el camino simplemente no crece en este nivel.
            indice //= 2
        return PruebaInclusion(clave, self.hojas[clave], camino)

    @staticmethod
    def verificar(prueba: PruebaInclusion, raiz: bytes) -> bool:
        actual = _hoja(prueba.clave, prueba.valor)
        for hermano, soy_derecha in prueba.camino:
            actual = (
                _nodo(hermano, actual) if soy_derecha else _nodo(actual, hermano)
            )
        return actual == raiz

    def probar_exclusion(self, buscado: str) -> PruebaExclusion:
        """Demuestra que algo NO esta. Exige orden total."""
        if buscado in self.hojas:
            raise ValueError(f"{buscado} si esta en el arbol")
        claves = self.claves
        i = bisect.bisect_left(claves, buscado)
        anterior = claves[i - 1] if i > 0 else None
        siguiente = claves[i] if i < len(claves) else None
        return PruebaExclusion(
            buscado=buscado,
            anterior=anterior,
            siguiente=siguiente,
            prueba_anterior=self.probar(anterior) if anterior else None,
            prueba_siguiente=self.probar(siguiente) if siguiente else None,
        )

    @staticmethod
    def verificar_exclusion(prueba: PruebaExclusion, raiz: bytes) -> bool:
        for parcial in (prueba.prueba_anterior, prueba.prueba_siguiente):
            if parcial is not None and not ArbolMerkle.verificar(parcial, raiz):
                return False
        if prueba.anterior is not None and not prueba.anterior < prueba.buscado:
            return False
        if prueba.siguiente is not None and not prueba.buscado < prueba.siguiente:
            return False
        return True
