"""Criptografia DIDACTICA: resumenes, firmas y direcciones.

AVISO IMPRESCINDIBLE
  El esquema de firma de este modulo es una construccion simplificada con fines
  educativos. NO ofrece las garantias de un esquema real y NO debe usarse fuera
  del laboratorio. En produccion se usan bibliotecas auditadas, nunca una
  implementacion propia.

Lo que el modulo si demuestra correctamente:
  · un mensaje alterado invalida la firma;
  · una direccion mal tecleada se detecta antes de enviar;
  · una firma prueba quien, no que algo sea verdad.
"""

from __future__ import annotations

import hashlib
import hmac
import secrets
from dataclasses import dataclass

RESUMEN = hashlib.sha256


def resumen(datos: bytes) -> bytes:
    return RESUMEN(datos).digest()


def resumen_hex(datos: bytes) -> str:
    return RESUMEN(datos).hexdigest()


@dataclass(frozen=True)
class Par:
    """Par de claves didactico.

    La «clave publica» se deriva de la privada con una funcion de un solo
    sentido. La verificacion usa HMAC con la clave privada, de modo que este
    esquema es SIMETRICO en la practica: cualquiera que verifique podria
    tambien firmar. Se mantiene asi porque el objetivo es enseñar la mecanica
    y sus limites, y esta limitacion se declara en cada uso.
    """

    privada: bytes
    publica: bytes


def generar_par() -> Par:
    privada = secrets.token_bytes(32)
    return Par(privada=privada, publica=resumen(b"pub" + privada))


def firmar(par: Par, mensaje: bytes) -> bytes:
    return hmac.new(par.privada, resumen(mensaje), RESUMEN).digest()


def verificar(par: Par, mensaje: bytes, firma: bytes) -> bool:
    esperada = hmac.new(par.privada, resumen(mensaje), RESUMEN).digest()
    return hmac.compare_digest(esperada, firma)


# Longitudes fijas de la direccion. El cuerpo son 20 bytes y la verificacion 3,
# y cada byte ocupa ocho bits que se reparten en simbolos de cinco.
BYTES_CUERPO = 20
BYTES_VERIFICACION = 3


def _caracteres(n_bytes: int) -> int:
    return -(-n_bytes * 8 // 5)


CARACTERES_CUERPO = _caracteres(BYTES_CUERPO)
CARACTERES_VERIFICACION = _caracteres(BYTES_VERIFICACION)
LARGO_DIRECCION = 4 + CARACTERES_CUERPO + CARACTERES_VERIFICACION


def _codificar(datos: bytes) -> str:
    """Codificacion de longitud fija.

    El relleno por delante no es cosmetico. Si se codifica tratando los bytes
    como un entero y se corta al primer digito significativo, un cuerpo que
    empieza por cero pierde ese byte al codificar y ya no se puede reconstruir:
    la direccion se genera bien y no valida. El fallo aparece en una de cada
    doscientas cincuenta y seis claves, que es justo la frecuencia con la que
    un defecto se atribuye al azar en vez de al codigo.
    """
    alfabeto = "0123456789abcdefghjkmnpqrstuvwxyz"
    numero = int.from_bytes(datos, "big")
    salida = []
    for _ in range(_caracteres(len(datos))):
        numero, resto = divmod(numero, 32)
        salida.append(alfabeto[resto])
    return "".join(reversed(salida))


def derivar_direccion(publica: bytes) -> str:
    """Direccion con digitos de verificacion.

    Los caracteres finales detectan un error de tecleo antes de enviar. Sin
    ellos, un caracter equivocado envia los fondos a una direccion que nadie
    controla, y no vuelven.
    """
    cuerpo = resumen(publica)[:BYTES_CUERPO]
    verificacion = resumen(cuerpo)[:BYTES_VERIFICACION]
    return "dlt1" + _codificar(cuerpo) + _codificar(verificacion)


def direccion_valida(direccion: str) -> bool:
    """Recalcula la direccion completa desde su cuerpo y la compara entera.

    Con longitudes fijas la comprobacion es exacta: no hay que probar donde
    termina el cuerpo, y una direccion de largo distinto se rechaza antes de
    tocar el alfabeto.
    """
    if not direccion.startswith("dlt1") or len(direccion) != LARGO_DIRECCION:
        return False
    cuerpo_texto = direccion[4:4 + CARACTERES_CUERPO]
    try:
        cuerpo = _decodificar(cuerpo_texto, BYTES_CUERPO)
    except ValueError:
        return False
    esperada = "dlt1" + cuerpo_texto + _codificar(resumen(cuerpo)[:BYTES_VERIFICACION])
    return esperada == direccion


def _decodificar(texto: str, n_bytes: int) -> bytes:
    """Inverso exacto de `_codificar`.

    La longitud se pasa como argumento en vez de deducirla del valor: deducirla
    es lo que hacia perder los bytes iniciales que valen cero.
    """
    alfabeto = "0123456789abcdefghjkmnpqrstuvwxyz"
    numero = 0
    for caracter in texto:
        indice = alfabeto.find(caracter)
        if indice < 0:
            raise ValueError(f"caracter invalido: {caracter}")
        numero = numero * 32 + indice
    return numero.to_bytes(n_bytes, "big")
