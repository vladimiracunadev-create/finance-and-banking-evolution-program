"""Construccion y validacion de mensajes ISO 20022 de la familia de pagos.

Cubre un subconjunto de campos, no el esquema completo: el objetivo didactico es
que se vea por que un campo mal puesto convierte un pago automatico en una cola
manual, no reproducir las guias de uso vigentes.

La decision de diseno central: la referencia extremo a extremo y el UETR se
generan UNA VEZ, al crear la orden, y se conservan en los reintentos. Sin eso,
el receptor detecta el reintento como duplicado por heuristica de contenido.
"""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field

NS = "urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08"

IMPORTE = re.compile(r"^\d+\.\d{2}$")
DIVISA = re.compile(r"^[A-Z]{3}$")
BIC = re.compile(r"^[A-Z]{6}[A-Z0-9]{2}([A-Z0-9]{3})?$")

# Subconjunto del catalogo externo. Un codigo fuera de la tabla del corredor
# provoca rechazo en destino, y es una de las causas mas frecuentes.
PROPOSITOS = frozenset(
    {"SALA", "SUPP", "TAXS", "LOAN", "DIVI", "TRAD", "CHAR", "RENT", "OTHR"}
)

MOTIVOS_RECHAZO = frozenset(
    {"AC01", "AC04", "AM05", "BE05", "BE23", "RR04", "RC01", "FF01"}
)


@dataclass
class Parte:
    nombre: str
    pais: str
    calle: str = ""
    numero: str = ""
    ciudad: str = ""
    identificador: str = ""


@dataclass
class Orden:
    """Una orden de pago. Sus identificadores se generan aqui y no cambian."""

    end_to_end_id: str
    uetr: str
    importe: str
    divisa: str
    fecha_liquidacion: str
    deudor: Parte
    deudor_agente: str
    acreedor: Parte
    acreedor_agente: str
    proposito: str = "OTHR"
    reparto_gastos: str = "SHAR"
    deudor_ultimo: Parte | None = None
    acreedor_ultimo: Parte | None = None
    informacion_remesa: str = ""
    intentos: int = field(default=0)

    def reintentar(self) -> "Orden":
        """Un reintento conserva los identificadores. Ese es el punto."""
        self.intentos += 1
        return self


def _parte(padre: ET.Element, etiqueta: str, parte: Parte) -> None:
    nodo = ET.SubElement(padre, etiqueta)
    ET.SubElement(nodo, "Nm").text = parte.nombre
    direccion = ET.SubElement(nodo, "PstlAdr")
    if parte.calle:
        ET.SubElement(direccion, "StrtNm").text = parte.calle
    if parte.numero:
        ET.SubElement(direccion, "BldgNb").text = parte.numero
    if parte.ciudad:
        ET.SubElement(direccion, "TwnNm").text = parte.ciudad
    ET.SubElement(direccion, "Ctry").text = parte.pais


def construir_pacs008(orden: Orden, mensaje_id: str, creado: str) -> str:
    raiz = ET.Element("Document", xmlns=NS)
    documento = ET.SubElement(raiz, "FIToFICstmrCdtTrf")

    cabecera = ET.SubElement(documento, "GrpHdr")
    ET.SubElement(cabecera, "MsgId").text = mensaje_id
    ET.SubElement(cabecera, "CreDtTm").text = creado
    ET.SubElement(cabecera, "NbOfTxs").text = "1"

    operacion = ET.SubElement(documento, "CdtTrfTxInf")
    identificadores = ET.SubElement(operacion, "PmtId")
    ET.SubElement(identificadores, "InstrId").text = mensaje_id
    ET.SubElement(identificadores, "EndToEndId").text = orden.end_to_end_id
    ET.SubElement(identificadores, "UETR").text = orden.uetr

    importe = ET.SubElement(operacion, "IntrBkSttlmAmt", Ccy=orden.divisa)
    importe.text = orden.importe
    ET.SubElement(operacion, "IntrBkSttlmDt").text = orden.fecha_liquidacion
    ET.SubElement(operacion, "ChrgBr").text = orden.reparto_gastos

    if orden.deudor_ultimo is not None:
        _parte(operacion, "UltmtDbtr", orden.deudor_ultimo)
    _parte(operacion, "Dbtr", orden.deudor)
    agente_deudor = ET.SubElement(operacion, "DbtrAgt")
    ET.SubElement(
        ET.SubElement(agente_deudor, "FinInstnId"), "BICFI"
    ).text = orden.deudor_agente

    agente_acreedor = ET.SubElement(operacion, "CdtrAgt")
    ET.SubElement(
        ET.SubElement(agente_acreedor, "FinInstnId"), "BICFI"
    ).text = orden.acreedor_agente
    _parte(operacion, "Cdtr", orden.acreedor)
    if orden.acreedor_ultimo is not None:
        _parte(operacion, "UltmtCdtr", orden.acreedor_ultimo)

    proposito = ET.SubElement(operacion, "Purp")
    ET.SubElement(proposito, "Cd").text = orden.proposito
    if orden.informacion_remesa:
        remesa = ET.SubElement(operacion, "RmtInf")
        ET.SubElement(remesa, "Ustrd").text = orden.informacion_remesa

    return ET.tostring(raiz, encoding="unicode")


# Limite de tamano de un mensaje del laboratorio. Un mensaje real de pagos no
# se acerca a esta cifra; un intento de agotar memoria, si.
TAMANO_MAXIMO_BYTES = 512 * 1024


class XmlNoSeguro(Exception):
    """El documento contiene una construccion que no se acepta parsear."""


def parsear_seguro(xml: str) -> ET.Element:
    """Parsea un mensaje comprobando ANTES lo que el parser no comprueba.

    `xml.etree.ElementTree` no expande entidades externas, pero SI expande las
    internas: un documento con una declaracion de entidades anidadas agota la
    memoria del proceso. La defensa no es una biblioteca distinta, es rechazar
    la construccion que lo permite antes de entregar el texto al parser:

    1. limite de tamano, para que el propio texto no sea el ataque;
    2. rechazo de cualquier declaracion DOCTYPE o ENTITY.

    Un mensaje de pago legitimo no necesita ninguna de las dos.
    """
    if len(xml.encode("utf-8")) > TAMANO_MAXIMO_BYTES:
        raise XmlNoSeguro(
            f"mensaje de mas de {TAMANO_MAXIMO_BYTES} bytes: no se parsea"
        )
    cabecera = xml[:4096].upper()
    if "<!DOCTYPE" in cabecera or "<!ENTITY" in cabecera:
        raise XmlNoSeguro(
            "el mensaje declara DOCTYPE o ENTITY; un pago no las necesita "
            "y son el vector de la expansion de entidades"
        )
    # La supresion va acompanada de las dos comprobaciones anteriores, que son
    # las que cierran el vector real de esta biblioteca. Sin ellas, no se pone.
    return ET.fromstring(xml)  # nosec B314


def _sin_espacio_de_nombres(raiz: ET.Element) -> ET.Element:
    """Quita el espacio de nombres de cada etiqueta.

    Los mensajes reales lo llevan y la version del esquema cambia con cada
    revision. Un validador que dependa del literal del espacio de nombres deja
    de funcionar en la siguiente version sin que nadie lo note.
    """
    for nodo in raiz.iter():
        if isinstance(nodo.tag, str) and "}" in nodo.tag:
            nodo.tag = nodo.tag.split("}", 1)[1]
    return raiz


def validar(xml: str) -> list[str]:
    """Comprueba estructura y CONTENIDO.

    Un validador de esquema comprueba que el XML este bien formado; casi todos
    los rechazos reales pasan el esquema y fallan por contenido. Estos son los
    controles que si los detectan.
    """
    errores: list[str] = []
    try:
        raiz = _sin_espacio_de_nombres(parsear_seguro(xml))
    except XmlNoSeguro as exc:
        return [f"mensaje rechazado: {exc}"]
    except ET.ParseError as exc:
        return [f"XML no valido: {exc}"]

    def buscar(ruta: str) -> ET.Element | None:
        return raiz.find(ruta)

    def texto(ruta: str) -> str:
        nodo = buscar(ruta)
        return (nodo.text or "").strip() if nodo is not None else ""

    operacion = "FIToFICstmrCdtTrf/CdtTrfTxInf"

    for etiqueta, ruta in (
        ("MsgId", "FIToFICstmrCdtTrf/GrpHdr/MsgId"),
        ("EndToEndId", f"{operacion}/PmtId/EndToEndId"),
        ("UETR", f"{operacion}/PmtId/UETR"),
        ("Dbtr/Nm", f"{operacion}/Dbtr/Nm"),
        ("Cdtr/Nm", f"{operacion}/Cdtr/Nm"),
    ):
        if not texto(ruta):
            errores.append(f"falta {etiqueta}")

    nodo_importe = buscar(f"{operacion}/IntrBkSttlmAmt")
    if nodo_importe is None:
        errores.append("falta IntrBkSttlmAmt")
    else:
        valor = (nodo_importe.text or "").strip()
        if not IMPORTE.match(valor):
            errores.append(f"importe con formato invalido: '{valor}'")
        divisa = nodo_importe.get("Ccy", "")
        if not DIVISA.match(divisa):
            errores.append(f"divisa no ISO 4217: '{divisa}'")

    for etiqueta in ("DbtrAgt", "CdtrAgt"):
        bic = texto(f"{operacion}/{etiqueta}/FinInstnId/BICFI")
        if not BIC.match(bic):
            errores.append(f"{etiqueta}: identificador invalido '{bic}'")

    proposito = texto(f"{operacion}/Purp/Cd")
    if proposito and proposito not in PROPOSITOS:
        errores.append(f"codigo de proposito no admitido: '{proposito}'")

    for etiqueta in ("Dbtr", "Cdtr"):
        pais = texto(f"{operacion}/{etiqueta}/PstlAdr/Ctry")
        if len(pais) != 2 or not pais.isupper():
            errores.append(f"{etiqueta}: pais no ISO 3166 alfa-2 '{pais}'")
        if not texto(f"{operacion}/{etiqueta}/PstlAdr/TwnNm"):
            errores.append(
                f"{etiqueta}: direccion sin ciudad estructurada; "
                "el texto libre degrada el screening en destino"
            )

    reparto = texto(f"{operacion}/ChrgBr")
    if reparto not in {"DEBT", "CRED", "SHAR"}:
        errores.append(f"reparto de gastos invalido: '{reparto}'")

    return errores


def pacs002(orden: Orden, aceptado: bool, motivo: str | None = None) -> str:
    """Informe de estado. El rechazo lleva SIEMPRE un codigo del catalogo."""
    if not aceptado and motivo not in MOTIVOS_RECHAZO:
        raise ValueError(f"motivo de rechazo fuera del catalogo: {motivo}")
    raiz = ET.Element("Document")
    documento = ET.SubElement(raiz, "FIToFIPmtStsRpt")
    estado = ET.SubElement(documento, "TxInfAndSts")
    ET.SubElement(estado, "OrgnlEndToEndId").text = orden.end_to_end_id
    ET.SubElement(estado, "OrgnlUETR").text = orden.uetr
    ET.SubElement(estado, "TxSts").text = "ACCP" if aceptado else "RJCT"
    if not aceptado:
        razon = ET.SubElement(ET.SubElement(estado, "StsRsnInf"), "Rsn")
        ET.SubElement(razon, "Cd").text = motivo
    return ET.tostring(raiz, encoding="unicode")


ESTADOS = {
    "recibido": {"aceptado", "rechazado"},
    "aceptado": {"liquidado", "rechazado", "cancelado"},
    "liquidado": {"devuelto"},
    "cancelado": set(),
    "rechazado": set(),
    "devuelto": set(),
}


class TransicionIlegal(Exception):
    """Se intento una transicion que la maquina de estados no admite."""


def transitar(actual: str, destino: str) -> str:
    """Antes de liquidar se CANCELA; despues de liquidar se DEVUELVE."""
    if destino not in ESTADOS.get(actual, set()):
        raise TransicionIlegal(f"{actual} -> {destino}")
    return destino
