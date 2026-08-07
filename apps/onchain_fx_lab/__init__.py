"""Laboratorio de FX sobre registros — Parte 21.

Tres modulos, cada uno asociado a una afirmacion concreta de una clase:

    pricing     el registro no forma precio: lo consume, y le anade su coste
    amm         el ratio de comisiones tranquiliza; la divergencia se lo come
    settlement  la ventana va de irrevocable a confirmado, no de envio a envio

Todo es didactico y trabaja con datos sinteticos. No se conecta a ninguna red,
no ejecuta ninguna operacion real y no recomienda ninguna estrategia.
"""

__all__ = ["amm", "pricing", "settlement"]
