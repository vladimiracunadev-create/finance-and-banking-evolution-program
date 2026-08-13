# Referencias oficiales de finanzas digitales

**Dónde verificar cada cosa.** Este documento no repite la bibliografía general
—esa está en **[fuentes.md](fuentes.md)**— sino que reúne las fuentes **oficiales**
que sostienen las Partes 17 a 23, ordenadas por lo que hay que comprobar.

La regla que ordena todo el documento es la misma que el programa repite en cada
clase: **una norma citada sin fecha de verificación es una afirmación que no
caduca**, y dentro de un año nadie sabrá si seguía siendo cierta. Por eso cada
entrada dice qué se verifica ahí, y no solo dónde está.

---

## Qué se verifica en cada sitio

### Chile

| Qué verificar | Dónde |
|---|---|
| Texto oficial de una ley | Biblioteca del Congreso Nacional · <https://www.bcn.cl/leychile> |
| Normas de carácter general, plazos y transitorios | CMF · <https://www.cmfchile.cl/> |
| Registro de prestadores de servicios financieros | CMF · <https://www.cmfchile.cl/> |
| Anexo técnico del Sistema de Finanzas Abiertas | CMF · <https://www.cmfchile.cl/> |
| Normas de cambios internacionales | Banco Central de Chile · <https://www.bcentral.cl/> |
| Sistemas de pago y estadística monetaria | Banco Central de Chile · <https://www.bcentral.cl/> |
| Obligaciones de prevención de lavado | UAF · <https://www.uaf.cl/> |
| Protección del consumidor financiero | SERNAC · <https://www.sernac.cl/> |

### Unión Europea

| Qué verificar | Dónde |
|---|---|
| Versión consolidada de un reglamento | EUR-Lex · <https://eur-lex.europa.eu/> |
| Normas técnicas y directrices bancarias | EBA · <https://www.eba.europa.eu/> |
| Normas técnicas y criterios de mercados | ESMA · <https://www.esma.europa.eu/> |
| Paquete de finanzas digitales y política | Comisión Europea · <https://finance.ec.europa.eu/digital-finance_en> |

### El Salvador

| Qué verificar | Dónde |
|---|---|
| Texto y reformas de la Ley Bitcoin | Asamblea Legislativa · <https://www.asamblea.gob.sv/> |
| Régimen de activos digitales y registro de proveedores | CNAD · <https://www.cnad.gob.sv/> |
| Estadística de remesas | Banco Central de Reserva · <https://www.bcr.gob.sv/> |
| Análisis de estabilidad y programa vigente | FMI · <https://www.imf.org/en/Countries/SLV> |

---

## Organismos internacionales

| Organismo | Qué publica que este programa usa | Sitio |
|---|---|---|
| **BIS — CPMI** | Hoja de ruta de pagos transfronterizos, principios de infraestructuras, trabajos sobre pago contra pago | <https://www.bis.org/cpmi/> |
| **BIS — Comité de Basilea** | Tratamiento prudencial de exposiciones a criptoactivos, resiliencia operativa | <https://www.bis.org/bcbs/> |
| **BIS — Innovation Hub** | Proyectos institucionales de infraestructura financiera | <https://www.bis.org/about/bisih/> |
| **FSB** | Marco global de criptoactivos, stablecoins globales, riesgo de terceros | <https://www.fsb.org/> |
| **IOSCO** | Recomendaciones sobre mercados de activos digitales y finanzas descentralizadas, principios de índices | <https://www.iosco.org/> |
| **GAFI** | Recomendación 16, activos virtuales y sus proveedores | <https://www.fatf-gafi.org/> |
| **FMI** | Informes de estabilidad financiera global e informes de país | <https://www.imf.org/> |
| **Banco Mundial** | Precios de remesas, inclusión financiera, estudios de banca abierta | <https://www.worldbank.org/> |
| **OCDE** | Tokenización de activos, política de datos y privacidad | <https://www.oecd.org/> |
| **IFRS Foundation** | Tratamiento contable de activos digitales | <https://www.ifrs.org/> |
| **UNIDROIT** | Principios sobre activos digitales y derecho privado | <https://www.unidroit.org/> |
| **CNUDMI** | Comercio electrónico y documentos transmisibles electrónicos | <https://uncitral.un.org/es> |

---

## Estándares técnicos

| Organismo | Qué aporta | Sitio |
|---|---|---|
| **OpenID Foundation** | Perfiles de seguridad de interfaces financieras y OpenID Connect | <https://openid.net/> |
| **IETF** | OAuth 2.x, JOSE, protocolos de transporte y seguridad | <https://www.ietf.org/> |
| **NIST** | Gestión de claves, continuidad, marco de ciberseguridad | <https://csrc.nist.gov/> |
| **ISO 20022** | Definiciones de mensajes de pago y guías de implantación | <https://www.iso20022.org/> |
| **SWIFT** | Guías de migración y práctica de mensajería | <https://www.swift.com/> |
| **OWASP** | Riesgos de aplicaciones y de interfaces | <https://owasp.org/> |

---

## Cómo se cita en este repositorio

```text
FORMATO DE UNA CITA NORMATIVA

  Autoridad (año). Título del instrumento.
  Fuente oficial. URL

  Y SIEMPRE, EN EL BLOQUE DE FUENTES:
  «Fecha de verificación de esta clase:
   AAAA-MM-DD»

QUÉ ACTIVA LA OBLIGACIÓN DE VERIFICAR
  citar un instrumento CONCRETO:
  una ley con número, una norma de carácter
  general con número, un reglamento o una
  directiva de la Unión con número

QUÉ NO LA ACTIVA
  marcos y principios sin número, que no
  caducan del mismo modo

EL VALIDADOR QUE LO COMPRUEBA
  tools/validate_metadata.py
```

Las fichas estructuradas de los instrumentos citados están en
**[`regulatory/`](../regulatory/README.md)**, con su campo `last_verified`. El
validador comprueba que la fecha exista y no sea futura; **que siga siendo cierta
lo compruebas tú**.

---

## Qué no sirve como fuente normativa

```text
NO SE USAN COMO FUENTE PRINCIPAL

  · blogs y medios especializados
  · resúmenes de despachos, salvo como
    orientación citada como tal
  · material comercial de un proveedor
  · versiones no consolidadas cuando
    existe la consolidada
  · traducciones no oficiales para
    determinar el alcance de un texto

SÍ SIRVEN
  · para orientarte sobre dónde mirar
  · nunca para decidir
```

---

## Limitaciones

- Los enlaces de este documento son **puntos de entrada** a sitios oficiales; su
  estructura cambia y una URL puede dejar de resolver.
- Ninguna referencia de esta página constituye asesoría legal, financiera ni
  tributaria.
- El programa cita fuentes de varias jurisdicciones: **la única que obliga es la
  del país donde se aplique la actividad**.

**Fecha de verificación de este documento: 2026-08-12.**

---

[🏠 Inicio](../README.md) · [📚 Documentación](README.md) · [📖 Programa](../SYLLABUS.md)
