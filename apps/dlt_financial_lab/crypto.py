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


def _codificar(datos: bytes) -> str:
    alfabeto = "0123456789abcdefghjkmnpqrstuvwxyz"
    numero = int.from_bytes(datos, "big")
    salida = ""
    while numero:
        numero, resto = divmod(numero, 32)
        salida = alfabeto[resto] + salida
    return salida or "0"


def derivar_direccion(publica: bytes) -> str:
    """Direccion con digitos de verificacion.

    Los cuatro caracteres finales detectan un error de tecleo antes de enviar.
    Sin ellos, un caracter equivocado envia los fondos a una direccion que nadie
    controla, y no vuelven.
    """
    cuerpo = resumen(publica)[:20]
    verificacion = resumen(cuerpo)[:3]
    return "dlt1" + _codificar(cuerpo) + _codificar(verificacion)


def direccion_valida(direccion: str) -> bool:
    if not direccion.startswith("dlt1") or len(direccion) < 12:
        return False
    # Se recalcula la direccion completa a partir del cuerpo declarado:
    # comparar la cadena entera es mas simple y no deja huecos.
    for longitud in range(4, len(direccion)):
        cuerpo_texto = direccion[4:longitud]
        try:
            cuerpo = _decodificar(cuerpo_texto)
        except ValueError:
            continue
        if len(cuerpo) != 20:
            continue
        esperada = "dlt1" + cuerpo_texto + _codificar(resumen(cuerpo)[:3])
        if esperada == direccion:
            return True
    return False


def _decodificar(texto: str) -> bytes:
    alfabeto = "0123456789abcdefghjkmnpqrstuvwxyz"
    numero = 0
    for caracter in texto:
        indice = alfabeto.find(caracter)
        if indice < 0:
            raise ValueError(f"caracter invalido: {caracter}")
        numero = numero * 32 + indice
    longitud = (numero.bit_length() + 7) // 8
    return numero.to_bytes(max(longitud, 1), "big")
