"""Lectura de las citas que hacen las clases y del registro de fuentes.

Este módulo es la única pieza que sabe **cómo se escribe una cita** en este
programa. Lo comparten el verificador offline (`verify_sources.py`) y el
revalidador en red (`refresh_sources.py`), para que ambos vean exactamente el
mismo conjunto de obras: si el verificador y el revalidador contaran distinto,
las cifras del README dejarían de significar nada.

Una cita del programa tiene esta forma:

    - Autor, A. y Autor, B. (2021). *Título exacto* (3.ª ed.). Editorial.
      Uso que hace esta clase de la obra. <https://enlace.oficial/documento>

y de ahí salen los seis campos que necesita el registro: autores, año, título,
editorial, uso y localizador.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULES = ROOT / "modules"
REGISTRO = ROOT / "sources" / "bibliography.json"

ENCABEZADO_FUENTES = "## 📗 Fuentes y verificación"
PREFIJO_VERIFICACION = "- Verificación local"

# Una cita que apunta a una ficha del propio repositorio no es una obra
# externa: es una referencia interna que ya valida `tools/validate_metadata.py`.
REFERENCIA_INTERNA = re.compile(r"^Fichas?\s+normativas?\s+del\s+repositorio", re.IGNORECASE)

_URL = re.compile(r"<(https?://[^>\s]+)>")
_URL_SUELTA = re.compile(r"(?<![<(\[])\b(https?://[^\s>)\]]+)")
_AUTORES_ANIO = re.compile(r"^(?P<autores>.+?)\s*\((?P<anio>\d{4}[^)]*)\)\s*[.:]\s*")
_AUTOR_SIN_ANIO = re.compile(r"^(?P<autores>[^.*\"“]{3,90}?)\.\s+(?=[*\"“])")
_TITULO_CURSIVA = re.compile(r"\*([^*]+)\*")
_TITULO_COMILLAS = re.compile("[\"“]([^\"”]+)[\"”]")
_EDICION = re.compile(r"^\s*\([^)]*(?:\bed\b|\bed\.|edici[oó]n)[^)]*\)\s*\.?\s*", re.IGNORECASE)

# Dominios cuyo material es normativo o de organismo emisor. La distinción
# importa: una norma se revalida por fecha, un manual universitario no.
DOMINIOS_NORMATIVOS = (
    "bis.org", "iosco.org", "fsb.org", "fatf-gafi.org", "gafilat.org",
    "cmfchile.cl", "bcn.cl", "bcentral.cl", "sii.cl", "sbif.cl",
    "eur-lex.europa.eu", "esma.europa.eu", "eba.europa.eu", "ecb.europa.eu",
    "europa.eu", "ifrs.org", "iasb.org", "imf.org", "worldbank.org",
    "oecd.org", "oecd.ai", "nist.gov", "iso.org", "sec.gov",
    "federalreserve.gov", "fdic.gov", "occ.gov", "consumerfinance.gov",
    "fca.org.uk", "bankofengland.co.uk", "treasury.gov", "iadb.org",
    "iaisweb.org", "iadi.org", "coso.org", "theiia.org", "ngfs.net",
    "iccwbo.org", "swift.com", "iso20022.org", "w3.org", "ietf.org",
    "mas.gov.sg", "hkma.gov.hk", "fatf-gafi.org", "un.org", "unidroit.org",
)


# Emisores institucionales. La tabla traduce las muchas formas en que una misma
# institución aparece citada —siglas, nombre en inglés, nombre en español— a un
# único responsable. Sin esto, «BIS», «Basel Committee» y «Comité de Supervisión
# Bancaria de Basilea» contarían como tres autoridades distintas.
ORGANISMOS: tuple[tuple[str, str], ...] = (
    ("basel committee", "Comité de Supervisión Bancaria de Basilea (BCBS)"),
    ("comite de supervision bancaria de basilea", "Comité de Supervisión Bancaria de Basilea (BCBS)"),
    ("bcbs", "Comité de Supervisión Bancaria de Basilea (BCBS)"),
    ("committee on payments and market infrastructures", "Comité de Pagos e Infraestructuras de Mercado (CPMI)"),
    ("cpmi", "Comité de Pagos e Infraestructuras de Mercado (CPMI)"),
    ("cpss", "Comité de Pagos e Infraestructuras de Mercado (CPMI)"),
    ("bank for international settlements", "Banco de Pagos Internacionales (BIS)"),
    ("banco de pagos internacionales", "Banco de Pagos Internacionales (BIS)"),
    ("bis", "Banco de Pagos Internacionales (BIS)"),
    ("iosco", "Organización Internacional de Comisiones de Valores (IOSCO)"),
    ("organizacion internacional de comisiones de valores", "Organización Internacional de Comisiones de Valores (IOSCO)"),
    ("financial stability board", "Consejo de Estabilidad Financiera (FSB)"),
    ("consejo de estabilidad financiera", "Consejo de Estabilidad Financiera (FSB)"),
    ("fsb", "Consejo de Estabilidad Financiera (FSB)"),
    ("financial action task force", "Grupo de Acción Financiera Internacional (GAFI/FATF)"),
    ("fatf", "Grupo de Acción Financiera Internacional (GAFI/FATF)"),
    ("gafi", "Grupo de Acción Financiera Internacional (GAFI/FATF)"),
    ("gafilat", "GAFILAT"),
    ("comision para el mercado financiero", "Comisión para el Mercado Financiero (CMF, Chile)"),
    ("cmf", "Comisión para el Mercado Financiero (CMF, Chile)"),
    ("banco central de chile", "Banco Central de Chile"),
    ("bcch", "Banco Central de Chile"),
    ("unidad de analisis financiero", "Unidad de Análisis Financiero (UAF, Chile)"),
    ("uaf", "Unidad de Análisis Financiero (UAF, Chile)"),
    ("biblioteca del congreso nacional", "Biblioteca del Congreso Nacional de Chile"),
    ("servicio de impuestos internos", "Servicio de Impuestos Internos (Chile)"),
    ("european banking authority", "Autoridad Bancaria Europea (EBA)"),
    ("autoridad bancaria europea", "Autoridad Bancaria Europea (EBA)"),
    ("eba", "Autoridad Bancaria Europea (EBA)"),
    ("esma", "Autoridad Europea de Valores y Mercados (ESMA)"),
    ("european central bank", "Banco Central Europeo (BCE)"),
    ("banco central europeo", "Banco Central Europeo (BCE)"),
    ("bce", "Banco Central Europeo (BCE)"),
    ("edpb", "Comité Europeo de Protección de Datos (EDPB)"),
    ("european union agency for cybersecurity", "Agencia de la Unión Europea para la Ciberseguridad (ENISA)"),
    ("enisa", "Agencia de la Unión Europea para la Ciberseguridad (ENISA)"),
    ("agencia de la union europea para la ciberseguridad", "Agencia de la Unión Europea para la Ciberseguridad (ENISA)"),
    ("europol", "Europol"),
    ("eur lex", "Unión Europea (EUR-Lex)"),
    ("union europea", "Unión Europea (EUR-Lex)"),
    ("comision europea", "Comisión Europea"),
    ("european commission", "Comisión Europea"),
    ("parlamento europeo", "Unión Europea (EUR-Lex)"),
    ("oecd", "Organización para la Cooperación y el Desarrollo Económicos (OCDE)"),
    ("ocde", "Organización para la Cooperación y el Desarrollo Económicos (OCDE)"),
    ("infe", "Organización para la Cooperación y el Desarrollo Económicos (OCDE)"),
    ("world bank", "Banco Mundial"),
    ("banco mundial", "Banco Mundial"),
    ("cgap", "CGAP (Banco Mundial)"),
    ("ifc", "Corporación Financiera Internacional (IFC)"),
    ("international monetary fund", "Fondo Monetario Internacional (FMI)"),
    ("fondo monetario internacional", "Fondo Monetario Internacional (FMI)"),
    ("imf", "Fondo Monetario Internacional (FMI)"),
    ("fmi", "Fondo Monetario Internacional (FMI)"),
    ("ifrs foundation", "IFRS Foundation"),
    ("ifrs", "IFRS Foundation"),
    ("iasb", "IFRS Foundation"),
    ("iaasb", "IAASB (IFAC)"),
    ("ifac", "IAASB (IFAC)"),
    ("iso", "Organización Internacional de Normalización (ISO)"),
    ("nist", "NIST (Estados Unidos)"),
    ("national institute of standards and technology", "NIST (Estados Unidos)"),
    ("ietf", "IETF"),
    ("rfc editor", "IETF"),
    ("w3c", "W3C"),
    ("cfpb", "Consumer Financial Protection Bureau (CFPB)"),
    ("consumer financial protection bureau", "Consumer Financial Protection Bureau (CFPB)"),
    ("federal trade commission", "Federal Trade Commission (FTC)"),
    ("ftc", "Federal Trade Commission (FTC)"),
    ("securities and exchange commission", "Securities and Exchange Commission (SEC)"),
    ("sec", "Securities and Exchange Commission (SEC)"),
    ("federal reserve", "Reserva Federal de los Estados Unidos"),
    ("reserva federal", "Reserva Federal de los Estados Unidos"),
    ("fdic", "FDIC (Estados Unidos)"),
    ("occ", "OCC (Estados Unidos)"),
    ("financial conduct authority", "Financial Conduct Authority (FCA)"),
    ("fca", "Financial Conduct Authority (FCA)"),
    ("bank of england", "Bank of England"),
    ("iais", "Asociación Internacional de Supervisores de Seguros (IAIS)"),
    ("iadi", "Asociación Internacional de Aseguradores de Depósitos (IADI)"),
    ("institute of internal auditors", "Institute of Internal Auditors (IIA)"),
    ("iia", "Institute of Internal Auditors (IIA)"),
    ("coso", "COSO"),
    ("committee of sponsoring organizations", "COSO"),
    ("ngfs", "NGFS"),
    ("pcaf", "PCAF"),
    ("unep fi", "UNEP FI"),
    ("tcfd", "TCFD"),
    ("camara de comercio internacional", "Cámara de Comercio Internacional (ICC)"),
    ("international chamber of commerce", "Cámara de Comercio Internacional (ICC)"),
    ("icc", "Cámara de Comercio Internacional (ICC)"),
    ("naciones unidas", "Naciones Unidas"),
    ("united nations", "Naciones Unidas"),
    ("uncitral", "UNCITRAL (Naciones Unidas)"),
    ("unidroit", "UNIDROIT"),
    ("organizacion internacional del trabajo", "Organización Internacional del Trabajo (OIT)"),
    ("oit", "Organización Internacional del Trabajo (OIT)"),
    ("swift", "SWIFT"),
    ("isda", "ISDA"),
    ("icma", "ICMA"),
    ("loan market association", "Loan Market Association"),
    ("lsta", "LSTA"),
    ("pci security standards council", "PCI Security Standards Council"),
    ("apwg", "APWG"),
    ("monetary authority of singapore", "Monetary Authority of Singapore (MAS)"),
    ("hong kong monetary authority", "Hong Kong Monetary Authority (HKMA)"),
    ("dama international", "DAMA International"),
    ("certified financial planner board of standards", "CFP Board"),
    ("info network", "INFO Network"),
    ("dama", "DAMA International"),
    ("european union", "Unión Europea (EUR-Lex)"),
    ("diario oficial de la union europea", "Unión Europea (EUR-Lex)"),
    ("international swaps and derivatives association", "ISDA"),
    ("egmont group", "Grupo Egmont"),
    ("grupo egmont", "Grupo Egmont"),
    ("cfa institute", "CFA Institute"),
    ("vanguard", "Vanguard Research"),
    ("dalbar", "Dalbar"),
    ("moody s", "Moody's Investors Service"),
    ("s p", "S&P Global Ratings"),
    ("standard poor s", "S&P Global Ratings"),
    ("deloitte", "Deloitte"),
    ("mckinsey", "McKinsey & Company"),
    ("openid foundation", "OpenID Foundation"),
    ("openapi initiative", "OpenAPI Initiative"),
    ("owasp", "OWASP Foundation"),
    ("wolfsberg", "Grupo Wolfsberg"),
    ("global foreign exchange committee", "Global Foreign Exchange Committee"),
    ("bis innovation hub", "BIS Innovation Hub"),
    ("network for greening the financial system", "NGFS"),
    ("partnership for carbon accounting financials", "PCAF"),
    ("unep finance initiative", "UNEP FI"),
    ("banco central do brasil", "Banco Central do Brasil"),
    ("asamblea legislativa de la republica de el salvador", "Asamblea Legislativa de El Salvador"),
    ("comision nacional de activos digitales", "Comisión Nacional de Activos Digitales (El Salvador)"),
    ("banco central de reserva de el salvador", "Banco Central de Reserva de El Salvador"),
    ("uncitral", "UNCITRAL (Naciones Unidas)"),
    ("iso 20022", "ISO 20022 (Registration Authority)"),
    ("equator principles association", "Equator Principles Association"),
    ("fondo internacional de desarrollo agricola", "FIDA"),
    ("organizacion mundial del comercio", "Organización Mundial del Comercio (OMC)"),
    ("board of governors of the federal reserve system", "Reserva Federal de los Estados Unidos"),
)

# Títulos que, por sí solos, identifican una norma aunque no se cite al emisor.
NORMA_POR_TITULO = re.compile(
    r"^\s*(?:NIC|NIIF|IFRS|IAS|NIA|ISA|ISO|IEC|SP\s*800|NISTIR|RFC|UCP|URC|URDG|"
    r"Incoterms|NCG|Ley|Reglamento|Directiva|Regulation|Directive|Recomendaci[oó]n|"
    r"Recommendation|Decreto|Marco Conceptual|The Basel Framework)\b",
    re.IGNORECASE,
)

# Normas cuyo texto vigente se mantiene consolidado y se enmienda: citarlas sin
# fecha de acceso es afirmar algo que puede haber dejado de ser cierto.
NORMA_ENMENDABLE = re.compile(
    r"Bas(?:el|ilea)|BCBS|MiCA|2023/1114|FATF Recommendations|Recomendaciones del GAFI|"
    r"\bNIC\b|\bNIIF\b|\bIFRS\b|\bIAS\b|\bISO\b|2016/679|2015/2366|2022/858|2024/1689",
    re.IGNORECASE,
)


# Sellos editoriales que aparecen en el programa. La lista existe para separar
# «McGraw-Hill» de «Metodología de cálculo de la APR estadounidense»: las dos
# frases ocupan el mismo lugar en la cita, y solo una es la editorial. Sin la
# lista, la frase que declara el uso se contaría como sello y la cita parecería
# no declarar nada.
EDITORIALES = (
    (
        "McGraw-Hill", "McGraw-Hill/Irwin", "McKinsey/Wiley", "Wiley", "Pearson",
        "Cengage", "MIT Press", "Princeton University Press", "Cambridge University Press",
        "Oxford University Press", "Harvard Business School Press", "Harvard Business Review Press",
        "Harvard Business Press", "Norton", "W. W. Norton", "Springer", "Academic Press",
        "Elsevier", "ACTEX", "Routledge", "O'Reilly", "IT Revolution", "Technics Publications",
        "FT Press", "HarperCollins", "Harper Business", "Harper", "Taylor Trade", "Times Books",
        "Crown", "Random House", "Portfolio", "Worth", "The New Press", "Debate", "Taurus",
        "Deusto", "Kogan Page", "CRC Press", "SIAM", "Ashgate", "Houghton Mifflin",
        "Addison-Wesley", "Columbia Business School", "IESE", "Wharton Financial Institutions Center",
        "Stochastic Solutions", "Retirement Researcher Media", "Public Affairs", "PublicAffairs",
        "Penguin", "Free Press", "Basic Books", "Bloomberg Press", "Palgrave Macmillan",
        "John Wiley & Sons", "Prentice Hall", "Thomson Reuters", "LexisNexis", "Anaya",
        "Ariel", "Alienta", "Planeta", "Paidós", "Gestión 2000", "Pirámide", "Alfaomega",
    )
)[0]

# Series y colecciones de trabajo que también ocupan el lugar de la editorial.
SERIES = re.compile(
    r"^(?:BIS|IMF|NBER|ECB|OECD|CGFS|FSI|BCBS|CPMI|World Bank|Banco Mundial|IFC|IADB)\s"
    r"(?:Papers?|Working Papers?|Quarterly Review|Bulletin|Staff|Policy|Insights|Economic|Discussion)",
    re.IGNORECASE,
)

_CONECTORES = {"de", "del", "la", "las", "el", "los", "y", "e", "of", "and", "the", "for", "&", "en"}


@lru_cache(maxsize=1)
def _sellos() -> frozenset[str]:
    return frozenset(normaliza(nombre) for nombre in EDITORIALES)


def es_editorial(texto: str) -> bool:
    """¿Esta frase es el sello que publica la obra, o ya es el uso que hace la clase?"""
    limpio = texto.strip().rstrip(".")
    if not limpio:
        return False
    if normaliza(limpio) in _sellos() or organismo(limpio) or SERIES.match(limpio):
        return True
    palabras = limpio.replace("/", " ").split()
    if len(palabras) > 4:
        return False
    return all(p[0].isupper() or p.lower() in _CONECTORES or p[0].isdigit() for p in palabras)


def organismo(nombre: str) -> str:
    """Devuelve el emisor canónico de un nombre citado, o cadena vacía."""
    clave = normaliza(nombre or "")
    if not clave:
        return ""
    for patron, canonico in ORGANISMOS:
        if clave == patron or clave.startswith(patron + " ") or clave.endswith(" " + patron):
            return canonico
        if f" {patron} " in f" {clave} " and len(patron) > 4:
            return canonico
    return ""


def _sin_acentos(texto: str) -> str:
    descompuesto = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in descompuesto if not unicodedata.combining(c))


def normaliza(texto: str) -> str:
    """Reduce un texto a su forma comparable: sin acentos, sin signos, en minúsculas."""
    plano = _sin_acentos(texto).lower()
    return re.sub(r"[^a-z0-9]+", " ", plano).strip()


def slug(texto: str, largo: int = 76) -> str:
    base = re.sub(r"\s+", "-", normaliza(texto))
    return base[:largo].strip("-")


def canoniza_url(url: str) -> str:
    """Forma canónica de un enlace: sin fragmento y sin barra final superflua."""
    url = url.split("#")[0].strip().rstrip(".,;")
    if url.endswith("/") and url.count("/") > 3:
        url = url[:-1]
    return url


def dominio(url: str) -> str:
    return url.split("//", 1)[-1].split("/", 1)[0].lower()


def es_normativo(url: str) -> bool:
    host = dominio(url)
    return any(host == d or host.endswith("." + d) for d in DOMINIOS_NORMATIVOS)


@dataclass
class Cita:
    """Una línea de bibliografía tal como aparece en una clase."""

    clase: str
    linea: str
    autores: list[str] = field(default_factory=list)
    anio: str = ""
    titulo: str = ""
    editorial: str = ""
    uso: str = ""
    url: str = ""
    revista: str = ""
    interna: bool = False

    @property
    def emisor(self) -> str:
        """Organismo emisor, si la obra la firma una institución y no personas."""
        for candidato in list(self.autores) + [self.editorial]:
            canonico = organismo(candidato)
            if canonico:
                return canonico
        return ""

    @property
    def tipo(self) -> str:
        if self.revista:
            return "paper"
        if self.emisor or NORMA_POR_TITULO.search(self.titulo):
            return "standard" if (self.emisor or es_normativo(self.url)) else "reference"
        # Una obra firmada por personas y publicada en la web —una ponencia, un
        # libro abierto— se localiza por su URL. Exigirle un ISBN que no existe
        # la dejaría pendiente para siempre teniendo el documento a un clic.
        if self.url:
            return "reference"
        if self.autores and all(_es_persona(a) for a in self.autores):
            return "book"
        return "book" if self.editorial else "reference"

    @property
    def autoridad(self) -> str:
        """Quién responde por la fuente: el emisor, la editorial o la revista."""
        if self.revista:
            return self.revista
        if self.emisor:
            return self.emisor
        if self.editorial and not _parece_prosa(self.editorial):
            return self.editorial
        # Si nadie más responde, responde quien firma. Una cita sin responsable
        # no es citable: por eso este último recurso existe.
        if self.autores:
            return self.autores[0]
        if self.url:
            return dominio(self.url).replace("www.", "")
        return ""

    @property
    def enmendable(self) -> bool:
        """Norma cuya versión vigente puede cambiar por enmienda posterior.

        Basilea y MiCA son los casos que este programa cita más: el texto
        consolidado se revisa, y una cita sin fecha de acceso envejece mal.
        """
        return bool(NORMA_ENMENDABLE.search(self.titulo)) or (
            self.tipo == "standard" and bool(NORMA_ENMENDABLE.search(self.emisor))
        )

    @property
    def clave(self) -> str:
        """Identidad de la obra: su título normalizado."""
        return normaliza(self.titulo)

    @property
    def id(self) -> str:
        """Identificador estable y legible: título de la obra y año.

        El enlace **no** entra en el identificador, y esa decisión es la que
        hace útil al registro. Una misma norma se cita con enlace en una clase
        y sin él en otra; si el enlace formara parte de la identidad, la obra
        se partiría en dos entradas y la que se citó sin enlace quedaría
        pendiente para siempre, aunque el documento esté perfectamente
        localizado tres clases más allá.

        El año sí entra, porque distingue ediciones y publicaciones anuales:
        el informe de 2023 no es el de 2024. Cuando el mismo título y año se
        citan con enlaces que apuntan a documentos distintos —el informe
        completo y uno de sus capítulos—, el título de la cita tiene que
        distinguirlos; el verificador avisa si no lo hace.
        """
        base = slug(self.titulo) or slug(self.linea)
        anio = re.sub(r"[^0-9]", "", self.anio)[:4]
        crudo = f"{base}-{anio}" if anio else base
        return re.sub(r"-{2,}", "-", crudo).strip("-")


_PERSONA = re.compile(r"^[A-ZÁÉÍÓÚÑÜ][\wáéíóúñü'’-]+(?:\s+[A-ZÁÉÍÓÚÑÜ][\wáéíóúñü'’-]+)?,\s*[A-ZÁÉÍÓÚÑ]\.?")
_SEPARA_PERSONAS = re.compile(r",\s+(?=[A-ZÁÉÍÓÚÑÜ][\wáéíóúñü'’-]+,)")
_SEPARA_AUTORES = re.compile(r"\s+y\s+|\s+e\s+|\s*/\s*|\s*&\s*")


def _es_persona(nombre: str) -> bool:
    return bool(_PERSONA.match(nombre.strip()))


def _parece_prosa(texto: str) -> bool:
    """Distingue un nombre propio de una frase de uso mal cortada."""
    return bool(re.match(r"^[a-záéíóúñ(]", texto.strip())) or len(texto.split()) > 5


def _corta_autores(bruto: str) -> list[str]:
    bruto = bruto.strip()
    if bruto.endswith(".") and not re.search(r"\b[A-ZÁÉÍÓÚÑ]\.$", bruto):
        bruto = bruto[:-1]
    if not bruto:
        return []
    partes: list[str] = []
    for tramo in _SEPARA_AUTORES.split(bruto):
        partes.extend(p.strip() for p in _SEPARA_PERSONAS.split(tramo) if p.strip())
    return [p.rstrip(",") for p in partes if p]


def analiza_cita(clase: str, texto: str) -> Cita:
    """Descompone una línea de bibliografía en sus campos."""
    cita = Cita(clase=clase, linea=texto)

    if REFERENCIA_INTERNA.match(texto):
        cita.interna = True
        return cita

    resto = texto.strip()

    enlaces = _URL.findall(resto)
    if enlaces:
        cita.url = canoniza_url(enlaces[0])
        resto = _URL.sub(" ", resto)
    else:
        suelto = _URL_SUELTA.search(resto)
        if suelto:
            cita.url = canoniza_url(suelto.group(1))
            resto = resto.replace(suelto.group(1), " ")

    cabecera = _AUTORES_ANIO.match(resto)
    if cabecera:
        cita.autores = _corta_autores(cabecera.group("autores"))
        cita.anio = cabecera.group("anio").strip()
        resto = resto[cabecera.end():]
    else:
        # Norma citada sin año: «IFRS Foundation. *NIC 2 Inventarios*. …».
        sin_anio = _AUTOR_SIN_ANIO.match(resto)
        if sin_anio:
            cita.autores = _corta_autores(sin_anio.group("autores"))
            resto = resto[sin_anio.end():]

    comillas = _TITULO_COMILLAS.search(resto)
    cursiva = _TITULO_CURSIVA.search(resto)
    if comillas and (not cursiva or comillas.start() < cursiva.start()):
        cita.titulo = comillas.group(1).strip()
        resto = resto[comillas.end():]
        revista = _TITULO_CURSIVA.search(resto)
        if revista:
            cita.revista = revista.group(1).strip()
            resto = resto[revista.end():]
    elif cursiva:
        cita.titulo = cursiva.group(1).strip()
        resto = resto[cursiva.end():]
    else:
        # Sin título marcado tipográficamente: la primera oración lo es.
        cita.autores = []
        cita.anio = ""
        primera = re.split(r"(?<=[.])\s", resto.strip())[0].strip()
        cita.titulo = primera.rstrip(".")
        resto = resto.strip()[len(primera):]

    resto = resto.lstrip(" .,;:")
    resto = _EDICION.sub("", resto)

    if not cita.revista:
        trozos = [t.strip() for t in re.split(r"(?<=\.)\s+", resto) if t.strip()]
        # La primera frase tras el título es la editorial solo si de verdad lo
        # parece. Si ya es prosa, la cita está declarando su uso y quitarla haría
        # que el verificador diera por no declarado algo que sí lo está.
        if trozos and es_editorial(trozos[0]):
            cita.editorial = trozos[0].rstrip(".")
            trozos = trozos[1:]
        resto = " ".join(trozos)

    cita.uso = re.sub(r"\s+", " ", resto).strip(" .,;:")
    return cita


def bloque_de_fuentes(texto: str) -> str:
    """Devuelve el cuerpo de la sección de fuentes de una clase."""
    inicio = texto.find(ENCABEZADO_FUENTES)
    if inicio < 0:
        return ""
    resto = texto[inicio + len(ENCABEZADO_FUENTES):]
    corte = re.search(r"\n(?=(#{1,6} |<!-- gen:))", resto)
    return resto[:corte.start()] if corte else resto


def clases() -> list[Path]:
    return sorted(MODULES.glob("*/classes/*.md"))


def ruta_relativa(archivo: Path) -> str:
    return archivo.relative_to(ROOT).as_posix()


def citas_de(archivo: Path) -> list[Cita]:
    texto = archivo.read_text(encoding="utf-8")
    ruta = ruta_relativa(archivo)
    encontradas = []
    for linea in bloque_de_fuentes(texto).splitlines():
        linea = linea.strip()
        if not linea.startswith("- ") or linea.startswith(PREFIJO_VERIFICACION):
            continue
        encontradas.append(analiza_cita(ruta, linea[2:].strip()))
    return encontradas


def lee_citas() -> list[Cita]:
    """Todas las citas de todas las clases, en orden de lectura del programa."""
    encontradas: list[Cita] = []
    for archivo in clases():
        encontradas.extend(citas_de(archivo))
    return encontradas


def firma_bloque(texto: str) -> str:
    """Huella del bloque de fuentes, para detectar clases que citan lo mismo."""
    lineas = [
        normaliza(l.strip()[2:])
        for l in bloque_de_fuentes(texto).splitlines()
        if l.strip().startswith("- ") and not l.strip().startswith(PREFIJO_VERIFICACION)
    ]
    return "\n".join(sorted(lineas))
