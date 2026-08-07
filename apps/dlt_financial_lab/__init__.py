"""Laboratorio de registro distribuido de la Parte 19.

AVISO: todo lo que hay aqui es DIDACTICO. La criptografia esta simplificada, el
consenso no reproduce ningun protocolo de produccion y la cadena no es segura.
No debe usarse para nada real, y no crea ninguna criptomoneda.

El modulo existe para demostrar cinco cosas que se afirman mucho y se comprueban
poco:

1. el encadenamiento NO impide reescribir la historia (solo la encarece);
2. una firma prueba QUIEN, no que algo sea verdad;
3. un arbol de Merkle demuestra pertenencia, no que el conjunto sea completo;
4. el consenso bizantino tolera nodos que MIENTEN, no software que se equivoca
   igual en todos;
5. dos lineas intercambiadas en una retirada vacian un contrato.
"""

from __future__ import annotations

from .chain import Bloque, Cadena, TransaccionInvalida
from .consensus import Comportamiento, Nodo, Red, ResultadoRonda
from .contracts import Escrow, EstadoIlegal, Interruptor, SinFondos
from .crypto import (
    Par,
    derivar_direccion,
    direccion_valida,
    firmar,
    generar_par,
    verificar,
)
from .merkle import ArbolMerkle, PruebaExclusion, PruebaInclusion
from .oracle import Oraculo, SinFuentesSuficientes
from .signatures import EsquemaMultifirma, analizar_correlacion

__all__ = [
    "ArbolMerkle",
    "Bloque",
    "Cadena",
    "Comportamiento",
    "EsquemaMultifirma",
    "Escrow",
    "EstadoIlegal",
    "Interruptor",
    "Nodo",
    "Oraculo",
    "Par",
    "PruebaExclusion",
    "PruebaInclusion",
    "Red",
    "ResultadoRonda",
    "SinFondos",
    "SinFuentesSuficientes",
    "TransaccionInvalida",
    "analizar_correlacion",
    "derivar_direccion",
    "direccion_valida",
    "firmar",
    "generar_par",
    "verificar",
]
