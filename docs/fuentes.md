<!-- portada:inicio -->
<div align="center">

# 📗 Fuentes

**La bibliografía consolidada: manuales de referencia, marcos institucionales y artículos fundacionales.**

[![registro](https://img.shields.io/badge/registro-sources%2Fbibliography.json-007c83?style=flat-square)](../sources/bibliography.json)
[![verificación](https://img.shields.io/badge/verificaci%C3%B3n-fecha%20por%20norma-2e8b57?style=flat-square)](metodologia-verificacion-regulatoria.md)

[⬅️ Documentación](README.md) ·
[🏠 Inicio](../README.md) ·
[🏛️ Verificación regulatoria](metodologia-verificacion-regulatoria.md) ·
[🗂️ Fichas normativas](../regulatory/README.md)

</div>
<!-- portada:fin -->

---

Bibliografía consolidada del programa. Cada clase cita las suyas al cierre y declara qué
uso hace de cada una; esta página reúne todas esas citas en una sola vista y explica de
dónde salen las cifras.

La fuente de verdad no es esta página: es
**[sources/bibliography.json](../sources/bibliography.json)**, un registro donde cada obra
tiene emisor, localizador y fecha de comprobación. Esta página se **genera** desde ese
registro, y por eso no puede desviarse de él: si alguien añadiera una obra aquí a mano,
`scripts/verify_sources.py` haría fallar la integración continua.

> **Criterio de selección.** Solo se citan fuentes consultables: manuales universitarios
> de referencia, normas contables emitidas, documentos publicados por organismos de
> estándares y artículos académicos identificables. No se citan blogs, resúmenes ni
> materiales sin autoría verificable.
>
> **Criterio de aceptación.** Una obra entra en el registro con un localizador resoluble:
> ISBN-13 para un libro, DOI para un artículo, o la URL oficial de la fuente primaria para
> una norma. Lo que no se pudo resolver queda como **pendiente**, con el motivo escrito. Un
> hueco declarado es información; un hueco rellenado por intuición sería una invención con
> formato de bibliografía.

---

## 🔍 Cómo leer una cita del programa

Cada clase cierra con una sección `📗 Fuentes y verificación` que contiene **al menos
cuatro referencias** y una línea final de verificación local:

```text
- Saunders, A. y Cornett, M. (2021). Financial Institutions Management (10.ª ed.).
  McGraw-Hill. Capítulos 8, 9 y 17: gestión de activos y pasivos y de liquidez.
- Basel Committee on Banking Supervision (2016). Interest rate risk in the banking book.
  BIS. Escenarios de choque de tasas y medidas de valor económico y margen.
  <https://www.bis.org/bcbs/publ/d368.htm>
- Verificación local: revisa los requerimientos de liquidez y de riesgo de tasa del
  libro de banca que aplica tu supervisor.
```

| Elemento | Para qué sirve |
|---|---|
| Autor, año y edición | Localizar la obra exacta; las ediciones difieren |
| Capítulo o sección | Ir directamente a lo que sostiene la afirmación |
| **Uso que hace la clase** | Saber qué sostiene esa obra aquí, y no solo que se citó |
| Enlace, cuando existe | Acceder al documento oficial sin intermediarios |
| **Verificación local** | Saber qué cambia por país y por fecha, y dónde comprobarlo |

La penúltima fila es la que distingue una bibliografía de un adorno. Citar una obra sin
decir qué se toma de ella deja al lector sin forma de comprobar la afirmación: tendría que
leerse el documento entero para averiguar si dice lo que la clase supone. Por eso el
verificador exige esa frase en **todas** las citas del programa, sin excepción.

La línea de verificación local es obligatoria en toda clase con contenido normativo.
El programa describe marcos internacionales; **la norma que obliga es siempre la
nacional**.

---

<!-- gen:registro:start -->
## 🧾 El registro en cifras

El programa cita **1 729 veces** un total de **699 obras** a lo largo de sus **356 clases**. De esas obras, **408** tienen hoy un localizador comprobado —ISBN-13, DOI o URL oficial con fecha de acceso— y **291** siguen pendientes de resolver.

El detalle está en **[sources/bibliography.json](../sources/bibliography.json)**, que es la fuente de verdad. Esta página es su vista de lectura: agrupa por quién responde por cada obra y en qué partes del programa se apoya.

| Tipo | Obras | Localizador que exige |
|---|---:|---|
| Libro | 130 | ISBN-13 con dígito de control válido |
| Artículo | 78 | DOI |
| Norma o documento oficial | 481 | URL https de la fuente primaria, con fecha de acceso |
| Referencia | 10 | URL https de la fuente primaria, con fecha de acceso |

El ISBN-13 se resuelve contra Open Library comparando título y autores, y se prefiere la edición del año que cita la clase. Cuando esa edición concreta no declara ISBN, se registra el de otra edición de la misma obra: el localizador lleva al libro correcto, y el año que aparece en el registro sigue siendo el que cita la clase. Cuando ni título ni autores coinciden con seguridad, la entrada se queda pendiente antes que arriesgar un ISBN casi correcto, que es peor que ninguno porque aparenta una comprobación que nadie hizo.

## 🏛️ Quién responde por cada obra

La columna **Comprobadas** dice cuántas de esas obras tienen hoy el localizador resuelto contra su fuente. Cuando una fila muestra menos comprobadas que obras, el hueco es visible a propósito.

| Emisor o editorial | Obras | Comprobadas | Partes |
|---|---:|---:|---|
| Comité de Supervisión Bancaria de Basilea (BCBS) | 51 | 43 | 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 |
| Banco de Pagos Internacionales (BIS) | 33 | 24 | 1, 3, 6, 8, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 |
| Comisión para el Mercado Financiero (CMF, Chile) | 30 | 30 | 17, 20, 21, 22, 23 |
| Consejo de Estabilidad Financiera (FSB) | 30 | 19 | 3, 4, 6, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 |
| Grupo de Acción Financiera Internacional (GAFI/FATF) | 25 | 6 | 4, 9, 10, 12, 14, 16, 17, 18, 19, 20, 22, 23 |
| Organización para la Cooperación y el Desarrollo Económicos (OCDE) | 25 | 5 | 1, 2, 3, 4, 6, 9, 10, 12, 13, 14, 15, 16, 17, 20, 21, 22, 23 |
| Comité de Pagos e Infraestructuras de Mercado (CPMI) | 23 | 22 | 3, 4, 8, 10, 11, 14, 16, 17, 18, 19, 20, 21, 22, 23 |
| Wiley | 22 | 16 | 1, 2, 3, 4, 5, 7, 8, 9, 11, 13, 14, 15, 16 |
| Autoridad Bancaria Europea (EBA) | 21 | 7 | 4, 9, 10, 11, 12, 13, 14, 15, 16, 17, 22 |
| IFRS Foundation | 21 | 0 | 1, 2, 5, 7, 9, 11, 12, 13, 15, 16, 17, 18, 20 |
| McGraw-Hill | 21 | 15 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16 |
| Unión Europea (EUR-Lex) | 20 | 16 | 3, 4, 9, 12, 14, 17, 19, 20, 21, 22, 23 |
| Organización Internacional de Normalización (ISO) | 17 | 2 | 4, 10, 11, 12, 14, 17, 18, 19, 21 |
| Fondo Monetario Internacional (FMI) | 16 | 1 | 1, 6, 9, 11, 12, 13, 16, 22 |
| Organización Internacional de Comisiones de Valores (IOSCO) | 16 | 13 | 3, 4, 8, 13, 14, 15, 19, 20, 21, 22, 23 |
| NIST (Estados Unidos) | 15 | 13 | 4, 11, 12, 14, 17, 19, 20, 23 |
| Journal of Finance | 13 | 9 | 3, 6, 8, 9, 11, 13 |
| Pearson | 13 | 9 | 1, 2, 3, 5, 6, 7, 8, 11, 12, 16 |
| Banco Mundial | 12 | 2 | 1, 2, 3, 4, 9, 10, 12, 13, 14, 15, 16, 18 |
| Consumer Financial Protection Bureau (CFPB) | 12 | 0 | 2, 3, 4, 9, 10, 12, 14 |
| IETF | 9 | 9 | 17 |
| Cámara de Comercio Internacional (ICC) | 7 | 3 | 10, 13, 18 |
| Financial Analysts Journal | 7 | 4 | 3, 8 |
| MIT Press | 7 | 3 | 1, 3, 6, 7, 8, 10, 12, 13, 14 |
| Princeton University Press | 7 | 4 | 2, 4, 6, 10, 12, 14, 15 |
| Banco Central de Chile | 6 | 5 | 17, 18, 20, 22 |
| Biblioteca del Congreso Nacional de Chile | 6 | 6 | 17, 20, 22, 23 |
| OpenID Foundation | 6 | 6 | 17 |
| American Economic Review | 5 | 2 | 3, 5, 6, 13 |
| IAASB (IFAC) | 5 | 4 | 5, 10, 12 |
| Journal of Financial Economics | 4 | 3 | 7, 8, 13 |
| Reserva Federal de los Estados Unidos | 4 | 0 | 1, 2, 3, 7, 9, 11, 14, 16 |
| Agencia de la Unión Europea para la Ciberseguridad (ENISA) | 3 | 3 | 4, 19 |
| Banco Central Europeo (BCE) | 3 | 0 | 6, 14, 15 |
| Cambridge University Press | 3 | 2 | 6, 14 |
| Cengage | 3 | 1 | 1, 2, 3, 5, 6, 13 |
| Financial Conduct Authority (FCA) | 3 | 2 | 10, 12, 15, 16 |
| Grupo Wolfsberg | 3 | 3 | 9, 12, 18 |
| Harvard Business Review | 3 | 0 | 14, 15, 16 |
| Naciones Unidas | 3 | 2 | 4, 12, 18 |
| Norton | 3 | 2 | 6, 8 |
| Oxford University Press | 3 | 2 | 7, 8, 9, 16 |
| Quarterly Journal of Economics | 3 | 3 | 2, 3, 6, 10 |
| Review of Financial Studies | 3 | 3 | 2, 8, 14 |
| Unidad de Análisis Financiero (UAF, Chile) | 3 | 3 | 17, 18, 22 |
| Academic Press | 2 | 1 | 7, 13 |
| Asociación Internacional de Supervisores de Seguros (IAIS) | 2 | 2 | 2, 3, 17 |
| Autoridad Europea de Valores y Mercados (ESMA) | 2 | 1 | 15, 22 |
| Bank of England | 2 | 1 | 11, 14 |
| CFA Institute | 2 | 1 | 8 |
| COSO | 2 | 1 | 5, 10, 11, 12 |
| Comisión Europea | 2 | 1 | 4, 22 |
| Comité Europeo de Protección de Datos (EDPB) | 2 | 2 | 17 |
| Federal Trade Commission (FTC) | 2 | 1 | 4, 6 |
| Harvard Business School Press | 2 | 0 | 15, 16 |
| Institute of Internal Auditors (IIA) | 2 | 2 | 9, 11, 12, 15, 16 |
| International Capital Market Association | 2 | 2 | 1, 7, 15 |
| Journal of Banking & Finance | 2 | 2 | 6, 13 |
| Journal of Marketing Research | 2 | 2 | 2 |
| Journal of Political Economy | 2 | 1 | 1, 2, 11 |
| O'Reilly | 2 | 2 | 14, 16 |
| OWASP Foundation | 2 | 2 | 17, 19 |
| Review of Economics and Statistics | 2 | 1 | 6, 7 |
| Routledge | 2 | 0 | 6, 15, 16 |
| SWIFT | 2 | 0 | 18 |
| Springer | 2 | 0 | 7, 11 |
| UNCITRAL (Naciones Unidas) | 2 | 1 | 3, 13 |
| 19.ª CIET | 1 | 0 | 6 |
| ACM SIGACT News | 1 | 0 | 19 |
| ACM TOPLAS | 1 | 0 | 19 |
| ACTEX | 1 | 1 | 1, 3, 7 |
| APWG | 1 | 1 | 4 |
| Addison-Wesley | 1 | 1 | 14 |
| American Psychologist | 1 | 1 | 2 |
| Asamblea Legislativa de El Salvador | 1 | 0 | 22 |
| Ashgate | 1 | 0 | 4 |
| BIS Occasional Paper 10 | 1 | 0 | 10, 15, 16 |
| BIS Working Papers | 1 | 1 | 6 |
| Bagehot, W. | 1 | 0 | 6 |
| Banco Central de Reserva de El Salvador | 1 | 1 | 22 |
| Banco Central do Brasil | 1 | 1 | 17 |
| Bank of England Quarterly Bulletin | 1 | 0 | 6 |
| Bank of England Working Paper 529 | 1 | 1 | 6 |
| Business Horizons | 1 | 1 | 7 |
| CFP Board | 1 | 1 | 2 |
| CRC Press | 1 | 1 | 4 |
| Carnegie-Rochester Conference Series | 1 | 1 | 6 |
| Columbia Business School | 1 | 0 | 8 |
| Comisión Nacional de Activos Digitales (El Salvador) | 1 | 1 | 22 |
| Corporación Financiera Internacional (IFC) | 1 | 1 | 13 |
| Crown | 1 | 0 | 6 |
| DAMA International | 1 | 0 | 14, 16 |
| DOJ | 1 | 1 | 12 |
| Dalbar | 1 | 0 | 8 |
| Debate | 1 | 0 | 1, 8 |
| Deloitte | 1 | 0 | 10 |
| Deusto | 1 | 0 | 8 |
| Econometrica | 1 | 1 | 8 |
| Economic Inquiry | 1 | 1 | 2 |
| Economic Policy | 1 | 1 | 6, 11 |
| Elsevier | 1 | 0 | 1, 7 |
| Equator Principles Association | 1 | 1 | 13 |
| European Journal of Operational Research | 1 | 1 | 15 |
| European Spreadsheet Risks Interest Group | 1 | 1 | 7 |
| Europol | 1 | 0 | 4, 10 |
| FIDA | 1 | 0 | 18 |
| FIDO Alliance | 1 | 1 | 4 |
| FT Press | 1 | 1 | 2 |
| Farrar, Straus and Giroux | 1 | 1 | 16 |
| Financial Services Review | 1 | 1 | 8 |
| Global Foreign Exchange Committee | 1 | 1 | 18, 21 |
| Grupo Egmont | 1 | 0 | 9 |
| Handbook of Macroeconomics | 1 | 1 | 6 |
| Harper Business | 1 | 0 | 4 |
| HarperCollins | 1 | 1 | 2 |
| Harvard Business Review Press | 1 | 0 | 10 |
| Houghton Mifflin | 1 | 1 | 11 |
| IEEE Symposium on Security and Privacy | 1 | 1 | 4 |
| IESE | 1 | 0 | 13 |
| INFO Network | 1 | 1 | 12 |
| ISDA | 1 | 0 | 11 |
| IT Revolution | 1 | 1 | 14, 16 |
| ITCS 2017 | 1 | 0 | 14 |
| Internet Engineering Task Force | 1 | 1 | 17 |
| Journal of Applied Corporate Finance | 1 | 1 | 10 |
| Journal of Economic Perspectives | 1 | 1 | 6 |
| Journal of Economic Theory | 1 | 1 | 10 |
| Journal of Financial Intermediation | 1 | 1 | 13 |
| Journal of Financial Planning | 1 | 0 | 2 |
| Journal of Financial and Quantitative Analysis | 1 | 1 | 8 |
| Journal of Investment Management | 1 | 0 | 8 |
| Journal of Legal Studies | 1 | 0 | 6 |
| Journal of Portfolio Management | 1 | 0 | 8 |
| Kogan Page | 1 | 0 | 10 |
| Little, Brown | 1 | 0 | 16 |
| Loan Market Association | 1 | 0 | 13 |
| Macmillan | 1 | 0 | 1, 3 |
| Management Review | 1 | 0 | 2 |
| Mathematical Finance | 1 | 1 | 11 |
| McGraw-Hill/Irwin | 1 | 1 | 1, 7 |
| McKinsey & Company | 1 | 0 | 1, 7, 8, 11, 13 |
| Merkle, R. | 1 | 0 | 19 |
| Moody's Investors Service | 1 | 0 | 8 |
| NBER | 1 | 0 | 7 |
| NBER Working Paper 22476 | 1 | 0 | 14 |
| NGFS | 1 | 1 | 11, 15 |
| NIPS 2016 | 1 | 0 | 14 |
| Notices of the AMS | 1 | 1 | 8 |
| OSDI | 1 | 0 | 19 |
| OpenAPI Initiative | 1 | 1 | 17 |
| Organización Mundial del Comercio (OMC) | 1 | 1 | 18 |
| PCAF | 1 | 1 | 15 |
| PCI Security Standards Council | 1 | 1 | 3, 4, 10 |
| Portfolio | 1 | 1 | 8 |
| RAND Journal of Economics | 1 | 1 | 10, 14 |
| Random House | 1 | 1 | 8 |
| Retirement Researcher Media | 1 | 1 | 2 |
| Risk | 1 | 0 | 11 |
| SIAM | 1 | 1 | 9 |
| Securities and Exchange Commission (SEC) | 1 | 1 | 4 |
| Servicio de Impuestos Internos (Chile) | 1 | 0 | 20 |
| Statistical Science | 1 | 1 | 14 |
| Stochastic Solutions | 1 | 0 | 14 |
| Taurus | 1 | 0 | 1, 2 |
| Taylor Trade | 1 | 1 | 2 |
| Technics Publications | 1 | 0 | 14 |
| The New Press | 1 | 0 | 6 |
| Times Books | 1 | 0 | 2, 4 |
| UBS/LBS | 1 | 0 | 8 |
| UNEP FI | 1 | 0 | 15 |
| USENIX Security | 1 | 0 | 4 |
| Vanguard Research | 1 | 0 | 8 |
| Wharton Financial Institutions Center | 1 | 0 | 9 |
| Worth | 1 | 1 | 6 |

## 🕓 Qué queda pendiente y por qué

Una fuente pendiente no se borra ni se disimula: se declara. Estas son las razones por las que una entrada todavía no tiene localizador comprobado.

| Motivo | Entradas |
|---|---:|
| la clase cita la norma sin enlace a la fuente primaria | 134 |
| la fuente respondió 403 a una consulta automática | 33 |
| ningún registro de Crossref coincide en título y autores | 27 |
| Open Library no devuelve ninguna obra con ese título y autor | 27 |
| no se pudo abrir el enlace desde el equipo que revalidó (red o TLS) | 25 |
| Open Library no respondió a la consulta | 20 |
| la fuente respondió 404 | 12 |
| Open Library no devuelve ediciones de la obra encontrada | 10 |
| la obra existe en Open Library pero ninguna edición declara ISBN-13 | 2 |
| la fuente respondió 410 | 1 |

Última revalidación en red: **2026-08-19**. La ejecuta `scripts/refresh_sources.py`, que resuelve ISBN contra Open Library, DOI contra Crossref y consulta cada URL oficial. Esa capa **no bloquea el CI**: si un organismo reorganiza su sitio, el programa no se rompe, se entera.
<!-- gen:registro:end -->

---

## 🚧 Qué hacer si una fuente ya no está disponible

Los enlaces a documentos oficiales cambian. Si uno no responde:

1. Busca el **título exacto** en el sitio del organismo emisor.
2. Los documentos del BIS tienen identificador estable (`d368`, `bcbs239`); búscalo.
3. Las normas NIIF están en el navegador de normas de la IFRS Foundation.
4. Si el documento fue sustituido, la versión vigente suele citarlo en su introducción.

Si detectas una fuente rota o superada, **[abre un issue](https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/issues)**
indicando la clase y la referencia.

Lo que el repositorio **no** hace es borrarla. Cuando `scripts/refresh_sources.py` encuentra
un enlace que dejó de responder, la entrada se conserva con su motivo y pasa a `pendiente`.
Un enlace caído dice algo sobre el enlace, no sobre la obra, y eliminar la referencia haría
desaparecer la única pista para reencontrarla.

---

**Ver también:** [Glosario](glosario.md) · [Fórmulas](formulas.md) ·
[Ética y limitaciones](etica-y-limitaciones.md) · [Índice del programa](../SYLLABUS.md)

<!-- pie:inicio -->
---

<div align="center">

[⬅️ Documentación](README.md) · [🏠 Inicio](../README.md) · [🏛️ Verificación regulatoria](metodologia-verificacion-regulatoria.md) · [🗂️ Fichas normativas](../regulatory/README.md)

</div>
<!-- pie:fin -->
