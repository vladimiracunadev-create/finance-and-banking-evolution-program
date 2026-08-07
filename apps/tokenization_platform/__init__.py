"""Plataforma de tokenizacion didactica — Parte 21.

Cinco modulos, cada uno asociado a una afirmacion concreta de una clase:

    registry     el espejo impide la atomicidad; el bloqueo la permite
    issuance     el bloqueo del importe es lo que hace informar al libro
    lifecycle    un cupon sin verificar el aprovisionamiento discrimina
    settlement   atomicidad es que NO exista estado intermedio observable
    collateral   liquidar posiciones enteras convierte una caida en cascada

Todo es didactico y trabaja con datos sinteticos. No emite ningun valor, no se
conecta a ninguna red, no mueve fondos y no recomienda ninguna inversion.
"""

__all__ = [
    "collateral",
    "issuance",
    "lifecycle",
    "registry",
    "settlement",
]
