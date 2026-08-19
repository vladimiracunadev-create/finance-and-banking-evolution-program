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
## 🏛️ Los documentos que sostienen cada parte

Esta es la tabla que importa: qué documento de qué regulador sostiene qué parte del programa, con el enlace a la fuente primaria. Se ordena por cuántas clases se apoyan en cada documento, y el 🔁 marca la norma cuya versión vigente puede cambiar por enmienda —Basilea, MiCA, las NIIF—, que por eso lleva fecha de revalidación.

| Regulador | Documento | Partes |
|---|---|---|
| Comité de Supervisión Bancaria de Basilea (BCBS) | [Basel III: Finalising post-crisis reforms](https://www.bis.org/bcbs/publ/d424.htm) 🔁 | 3, 6, 9, 10, 11, 12, 13, 15, 16, 22 |
| Comité de Supervisión Bancaria de Basilea (BCBS) | [Corporate governance principles for banks](https://www.bis.org/bcbs/publ/d328.htm) 🔁 | 11, 12, 13, 15, 16, 20, 22, 23 |
| Comité de Supervisión Bancaria de Basilea (BCBS) | [Principles for Operational Resilience](https://www.bis.org/bcbs/publ/d516.htm) 🔁 | 4, 10, 11, 14, 16, 17, 19, 22, 23 |
| Comité de Supervisión Bancaria de Basilea (BCBS) | [Principles for effective risk data aggregation and risk reporting (BCBS 239)](https://www.bis.org/publ/bcbs239.htm) 🔁 | 1, 4, 5, 7, 10, 14, 15, 16, 17 |
| Comité de Supervisión Bancaria de Basilea (BCBS) | [Prudential treatment of cryptoasset exposures](https://www.bis.org/bcbs/publ/d545.htm) 🔁 | 14, 19, 20, 21, 22, 23 |
| Comité de Supervisión Bancaria de Basilea (BCBS) | [Basel III: The Liquidity Coverage Ratio and liquidity risk monitoring tools](https://www.bis.org/publ/bcbs238.htm) 🔁 | 2, 10, 11, 16, 18, 20, 22 |
| Comité de Supervisión Bancaria de Basilea (BCBS) | [Core Principles for Effective Banking Supervision](https://www.bis.org/publ/bcbs230.htm) 🔁 | 12, 16, 22 |
| Comité de Supervisión Bancaria de Basilea (BCBS) | [Prudential treatment of problem assets — definitions of non-performing exposures and forbearance](https://www.bis.org/bcbs/publ/d403.htm) 🔁 | 2, 4, 7, 9, 13, 16 |
| Banco de Pagos Internacionales (BIS) | [Annual Economic Report, capítulo III](https://www.bis.org/publ/arpdf/ar2023e3.htm) | 18, 19, 20, 21, 22, 23 |
| Banco de Pagos Internacionales (BIS) | [Annual Economic Report](https://www.bis.org/publ/arpdf/ar2023e.htm) | 6, 11, 15, 16 |
| Banco de Pagos Internacionales (BIS) | [Sound Practices: Implications of fintech developments for banks and bank supervisors](https://www.bis.org/bcbs/publ/d431.htm) | 10, 14, 16, 22, 23 |
| Banco de Pagos Internacionales (BIS) | [Core Principles for Effective Deposit Insurance Systems](https://www.iadi.org/) | 3, 12 |
| Banco de Pagos Internacionales (BIS) | [Triennial Central Bank Survey of foreign exchange and OTC derivatives markets](https://www.bis.org/statistics/rpfx22.htm) | 6, 18, 21 |
| Banco de Pagos Internacionales (BIS) | [Annual Economic Report, capítulo III](https://www.bis.org/publ/arpdf/ar2022e3.htm) | 20 |
| Banco de Pagos Internacionales (BIS) | [CBDCs: an opportunity for the monetary system](https://www.bis.org/publ/arpdf/ar2021e3.htm) | 14, 20, 22 |
| Banco de Pagos Internacionales (BIS) | [Central bank digital currencies: foundational principles and core features](https://www.bis.org/publ/othp33.htm) | 14, 20, 22 |
| Comité de Pagos e Infraestructuras de Mercado (CPMI) | [Principles for Financial Market Infrastructures](https://www.bis.org/cpmi/publ/d101.htm) | 3, 8, 10, 14, 17, 18, 19, 21, 22, 23 |
| Comité de Pagos e Infraestructuras de Mercado (CPMI) | [Tokenisation in the context of money and other assets: concepts and implications for central banks](https://www.bis.org/cpmi/publ/d225.htm) | 20, 21, 22, 23 |
| Comité de Pagos e Infraestructuras de Mercado (CPMI) | [Distributed ledger technology in payment, clearing and settlement: an analytical framework](https://www.bis.org/cpmi/publ/d157.htm) | 19 |
| Comité de Pagos e Infraestructuras de Mercado (CPMI) | [Application of the Principles for Financial Market Infrastructures to stablecoin arrangements](https://www.bis.org/cpmi/publ/d206.htm) | 14, 18, 19, 20, 22 |
| Comité de Pagos e Infraestructuras de Mercado (CPMI) | [Payment aspects of financial inclusion](https://www.bis.org/cpmi) | 3, 4, 10 |
| Comité de Pagos e Infraestructuras de Mercado (CPMI) | [Fast payments — Enhancing the speed and availability of retail payments](https://www.bis.org/cpmi/publ/d154.htm) | 10, 14, 16 |
| Comité de Pagos e Infraestructuras de Mercado (CPMI) | [Correspondent banking](https://www.bis.org/cpmi/publ/d147.htm) | 10, 18 |
| Comité de Pagos e Infraestructuras de Mercado (CPMI) | [Enhancing cross-border payments: building blocks of a global roadmap](https://www.bis.org/cpmi/publ/d193.htm) | 18 |
| Organización Internacional de Comisiones de Valores (IOSCO) | [Policy Recommendations for Crypto and Digital Asset Markets](https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf) | 20, 21, 22, 23 |
| Organización Internacional de Comisiones de Valores (IOSCO) | [Decentralized Finance Report](https://www.iosco.org/library/pubdocs/pdf/IOSCOPD699.pdf) | 19, 20, 21 |
| Organización Internacional de Comisiones de Valores (IOSCO) | [Objectives and Principles of Securities Regulation](https://www.iosco.org/library/pubdocs/pdf/IOSCOPD323.pdf) | 21, 22 |
| Organización Internacional de Comisiones de Valores (IOSCO) | [Policy Recommendations for Decentralized Finance](https://www.iosco.org/library/pubdocs/pdf/IOSCOPD754.pdf) | 21, 22 |
| Organización Internacional de Comisiones de Valores (IOSCO) | [Principles for Financial Benchmarks](https://www.iosco.org/library/pubdocs/pdf/IOSCOPD415.pdf) | 19, 20, 22 |
| Organización Internacional de Comisiones de Valores (IOSCO) | [Good Practice for Fees and Expenses of Collective Investment Schemes](https://www.iosco.org/) | 3, 8 |
| Organización Internacional de Comisiones de Valores (IOSCO) | [Objectives and Principles of Securities Regulation](https://www.iosco.org/) | 13, 15 |
| Organización Internacional de Comisiones de Valores (IOSCO) | [Recommendations for Securities Settlement Systems](https://www.iosco.org/library/pubdocs/pdf/IOSCOPD176.pdf) | 21, 22 |
| Consejo de Estabilidad Financiera (FSB) | [Global Regulatory Framework for Crypto-asset Activities](https://www.fsb.org/2023/07/fsb-global-regulatory-framework-for-crypto-asset-activities) | 14, 20, 22, 23 |
| Consejo de Estabilidad Financiera (FSB) | [Effective Practices for Cyber Incident Response and Recovery](https://www.fsb.org/2020/10/effective-practices-for-cyber-incident-response-and-recovery-final-report) | 4, 10, 11, 14, 16, 22, 23 |
| Consejo de Estabilidad Financiera (FSB) | [Enhancing third-party risk management and oversight: a toolkit](https://www.fsb.org/2023/12/enhancing-third-party-risk-management-and-oversight-a-toolkit-for-financial-institutions-and-financial-authorities) | 14, 17, 18, 19 |
| Consejo de Estabilidad Financiera (FSB) | [Principles for an Effective Risk Appetite Framework](https://www.fsb.org/2013/11/r_131118) | 11, 15, 16 |
| Consejo de Estabilidad Financiera (FSB) | [High-level Recommendations for the Regulation, Supervision and Oversight of Global Stablecoin Arrangements](https://www.fsb.org/2023/07/high-level-recommendations-for-the-regulation-supervision-and-oversight-of-global-stablecoin-arrangements-final-report) | 18, 20, 22 |
| Consejo de Estabilidad Financiera (FSB) | [Assessment of Risks to Financial Stability from Crypto-assets](https://www.fsb.org/2022/02/assessment-of-risks-to-financial-stability-from-crypto-assets) | 20, 22 |
| Consejo de Estabilidad Financiera (FSB) | [Key Attributes of Effective Resolution Regimes for Financial Institutions](https://www.fsb.org/2014/10/r_141015) | 6, 12, 15, 16, 23 |
| Consejo de Estabilidad Financiera (FSB) | [Enhancing Cross-border Payments: Stage 3 roadmap](https://www.fsb.org/2020/10/enhancing-cross-border-payments-stage-3-roadmap) | 14, 18, 21 |
| Grupo de Acción Financiera Internacional (GAFI/FATF) | [Updated Guidance for a Risk-Based Approach to Virtual Assets and VASPs](https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-rba-virtual-assets-2021.html) | 14, 18, 20, 22, 23 |
| Grupo de Acción Financiera Internacional (GAFI/FATF) | [FATF Recommendations](https://www.fatf-gafi.org/) 🔁 | 9, 10 |
| Grupo de Acción Financiera Internacional (GAFI/FATF) | [Guidance on Digital Identity](https://www.fatf-gafi.org/) | 4, 9 |
| Grupo de Acción Financiera Internacional (GAFI/FATF) | Stocktake on Data Pooling, Collaborative Analytics and Data Protection | 12 |
| Grupo de Acción Financiera Internacional (GAFI/FATF) | [The FATF Recommendations](https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html) 🔁 | 16, 22 |
| Grupo de Acción Financiera Internacional (GAFI/FATF) | Anti-money laundering and terrorist financing measures and financial inclusion | 16 |
| Grupo de Acción Financiera Internacional (GAFI/FATF) | [Guidance for a risk-based approach](https://www.fatf-gafi.org/) | 18 |
| Grupo de Acción Financiera Internacional (GAFI/FATF) | [Guidance on Beneficial Ownership of Legal Persons](https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-Beneficial-Ownership-Legal-Persons.html) | 12 |
| Unión Europea (EUR-Lex) | [Reglamento (UE) 2023/1114 relativo a los mercados de criptoactivos](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32023R1114) 🔁 | 20, 22 |
| Unión Europea (EUR-Lex) | [Reglamento (UE) 2022/2554 sobre la resiliencia operativa digital del sector financiero](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32022R2554) | 17, 22, 23 |
| Unión Europea (EUR-Lex) | [Directive 2008/48/EC on credit agreements for consumers](https://eur-lex.europa.eu/) | 3, 4 |
| Unión Europea (EUR-Lex) | [Reglamento (UE) 2016/679 (RGPD)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) 🔁 | 17, 19 |
| Unión Europea (EUR-Lex) | [Reglamento (UE) 2022/858 sobre el régimen piloto de infraestructuras del mercado basadas en DLT](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32022R0858) 🔁 | 21, 22 |
| Unión Europea (EUR-Lex) | [Reglamento (UE) 2022/858 sobre un régimen piloto de infraestructuras del mercado basadas en la tecnología de registro descentralizado](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32022R0858) 🔁 | 21, 22 |
| Unión Europea (EUR-Lex) | [Directiva (UE) 2015/2366 (PSD2): iniciación de pagos y confirmación de fondos](https://eur-lex.europa.eu/eli/dir/2015/2366/oj) 🔁 | 17 |
| Unión Europea (EUR-Lex) | Directiva (UE) 2015/2366 sobre servicios de pago (PSD2) 🔁 | 14 |
| Comisión para el Mercado Financiero (CMF, Chile) | [Normativa aplicable a entidades financieras](https://www.cmfchile.cl/portal/principal/613/w3-channel.html) | 23 |
| Comisión para el Mercado Financiero (CMF, Chile) | [Normativa sobre custodia y depósito de valores](https://www.cmfchile.cl/portal/principal/613/w3-channel.html) | 21, 22 |
| Comisión para el Mercado Financiero (CMF, Chile) | [Normativa sobre oferta pública de valores e inscripción en el Registro de Valores](https://www.cmfchile.cl/portal/principal/613/w3-channel.html) | 21, 22 |
| Comisión para el Mercado Financiero (CMF, Chile) | [Anexo técnico del Sistema de Finanzas Abiertas: definiciones y esquemas de datos](https://www.cmfchile.cl/) | 17 |
| Comisión para el Mercado Financiero (CMF, Chile) | [Anexo técnico del Sistema de Finanzas Abiertas: esquemas por tipo de producto y calendario de fases](https://www.cmfchile.cl/) | 17 |
| Comisión para el Mercado Financiero (CMF, Chile) | [Anexo técnico del Sistema de Finanzas Abiertas: versionado y disponibilidad](https://www.cmfchile.cl/) | 17 |
| Comisión para el Mercado Financiero (CMF, Chile) | [Iniciativas de innovación financiera y normativa de la Ley 21.521](https://www.cmfchile.cl/portal/principal/613/w3-channel.html) | 22 |
| Comisión para el Mercado Financiero (CMF, Chile) | [Normativa aplicable a la custodia de instrumentos financieros](https://www.cmfchile.cl/portal/principal/613/w3-channel.html) | 20 |
| IFRS Foundation | [NIC 1 Presentación de Estados Financieros](https://www.ifrs.org/) 🔁 | 5, 16 |
| IFRS Foundation | [NIIF 9 Instrumentos Financieros](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments) 🔁 | 1, 5, 9, 11, 13, 16 |
| IFRS Foundation | [Marco Conceptual para la Información Financiera](https://www.ifrs.org/) 🔁 | 2, 5 |
| IFRS Foundation | [NIC 7 Estado de Flujos de Efectivo](https://www.ifrs.org/) 🔁 | 5, 13 |
| IFRS Foundation | [NIIF 16 Arrendamientos](https://www.ifrs.org/) 🔁 | 5, 7 |
| IFRS Foundation | [NIC 16 Propiedades, Planta y Equipo](https://www.ifrs.org/) 🔁 | 5 |
| IFRS Foundation | NIC 37 Provisiones, Pasivos Contingentes y Activos Contingentes 🔁 | 5 |
| IFRS Foundation | [NIIF S1 y NIIF S2](https://www.ifrs.org/issued-standards/ifrs-sustainability-standards-navigator) 🔁 | 11, 15 |
| Organización para la Cooperación y el Desarrollo Económicos (OCDE) | Recommendation on Financial Literacy | 1, 2, 3 |
| Organización para la Cooperación y el Desarrollo Económicos (OCDE) | [G20/OECD High-Level Principles on Financial Consumer Protection](https://www.oecd.org/finance/financial-education) | 12, 15, 16 |
| Organización para la Cooperación y el Desarrollo Económicos (OCDE) | [G20/OECD High-Level Principles on Financial Consumer Protection](https://www.oecd.org/finance/financial-education/48892010.pdf) | 4, 22, 23 |
| Organización para la Cooperación y el Desarrollo Económicos (OCDE) | Consumer Price Index Manual: Theory and Practice | 1, 6 |
| Organización para la Cooperación y el Desarrollo Económicos (OCDE) | Debt and Financial Vulnerability of Households | 4, 9 |
| Organización para la Cooperación y el Desarrollo Económicos (OCDE) | [Digital Disruption in Banking and its Impact on Competition](https://www.oecd.org/competition/digital-disruption-in-banking-and-its-impact-on-competition.htm) | 6, 14, 15 |
| Organización para la Cooperación y el Desarrollo Económicos (OCDE) | OECD Pensions Outlook | 1, 2, 3 |
| Organización para la Cooperación y el Desarrollo Económicos (OCDE) | Toolkit for Measuring Financial Literacy and Financial Inclusion | 1, 2 |
| Banco Mundial | Good Practices for Financial Consumer Protection | 1, 2, 3, 4, 9, 10 |
| Banco Mundial | [Remittance Prices Worldwide](https://remittanceprices.worldbank.org/) | 10, 18 |
| Banco Mundial | Alternative Data Transforming SME Finance | 14, 16 |
| Banco Mundial | Good Practices for Financial Consumer Protection | 10, 12, 15 |
| Banco Mundial | De-risking in the Financial Sector | 12, 16 |
| Banco Mundial | [General Principles for Credit Reporting](https://www.worldbank.org/) | 9 |
| Banco Mundial | Digital Financial Services | 14 |
| Banco Mundial | Digital Identity for Development | 12 |

## 📚 Quién responde por cada obra

El resto de la bibliografía, agrupada por quién responde por ella. **Con enlace** cuenta las obras cuyo localizador —ISBN-13, DOI o URL oficial— está en el registro; cuando una fila muestra menos, el hueco es visible a propósito.

| Emisor o editorial | Obras | Con enlace | Partes |
|---|---:|---:|---|
| Comité de Supervisión Bancaria de Basilea (BCBS) | 51 | 43 | 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 |
| Banco de Pagos Internacionales (BIS) | 33 | 26 | 1, 3, 6, 8, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 |
| Comisión para el Mercado Financiero (CMF, Chile) | 30 | 30 | 17, 20, 21, 22, 23 |
| Consejo de Estabilidad Financiera (FSB) | 30 | 22 | 3, 4, 6, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 |
| Grupo de Acción Financiera Internacional (GAFI/FATF) | 25 | 16 | 4, 9, 10, 12, 14, 16, 17, 18, 19, 20, 22, 23 |
| Organización para la Cooperación y el Desarrollo Económicos (OCDE) | 25 | 16 | 1, 2, 3, 4, 6, 9, 10, 12, 13, 14, 15, 16, 17, 20, 21, 22, 23 |
| Comité de Pagos e Infraestructuras de Mercado (CPMI) | 23 | 23 | 3, 4, 8, 10, 11, 14, 16, 17, 18, 19, 20, 21, 22, 23 |
| Wiley | 22 | 16 | 1, 2, 3, 4, 5, 7, 8, 9, 11, 13, 14, 15, 16 |
| Autoridad Bancaria Europea (EBA) | 21 | 9 | 4, 9, 10, 11, 12, 13, 14, 15, 16, 17, 22 |
| IFRS Foundation | 21 | 16 | 1, 2, 5, 7, 9, 11, 12, 13, 15, 16, 17, 18, 20 |
| McGraw-Hill | 21 | 15 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16 |
| Unión Europea (EUR-Lex) | 20 | 16 | 3, 4, 9, 12, 14, 17, 19, 20, 21, 22, 23 |
| Organización Internacional de Normalización (ISO) | 17 | 9 | 4, 10, 11, 12, 14, 17, 18, 19, 21 |
| Fondo Monetario Internacional (FMI) | 16 | 7 | 1, 6, 9, 11, 12, 13, 16, 22 |
| Organización Internacional de Comisiones de Valores (IOSCO) | 16 | 13 | 3, 4, 8, 13, 14, 15, 19, 20, 21, 22, 23 |
| NIST (Estados Unidos) | 15 | 13 | 4, 11, 12, 14, 17, 19, 20, 23 |
| Journal of Finance | 13 | 9 | 3, 6, 8, 9, 11, 13 |
| Pearson | 13 | 9 | 1, 2, 3, 5, 6, 7, 8, 11, 12, 16 |
| Banco Mundial | 12 | 3 | 1, 2, 3, 4, 9, 10, 12, 13, 14, 15, 16, 18 |
| Consumer Financial Protection Bureau (CFPB) | 12 | 1 | 2, 3, 4, 9, 10, 12, 14 |
| IETF | 9 | 9 | 17 |
| Cámara de Comercio Internacional (ICC) | 7 | 3 | 10, 13, 18 |
| Financial Analysts Journal | 7 | 4 | 3, 8 |
| MIT Press | 7 | 3 | 1, 3, 6, 7, 8, 10, 12, 13, 14 |
| Princeton University Press | 7 | 4 | 2, 4, 6, 10, 12, 14, 15 |
| Banco Central de Chile | 6 | 6 | 17, 18, 20, 22 |
| Biblioteca del Congreso Nacional de Chile | 6 | 6 | 17, 20, 22, 23 |
| OpenID Foundation | 6 | 6 | 17 |
| American Economic Review | 5 | 2 | 3, 5, 6, 13 |
| IAASB (IFAC) | 5 | 4 | 5, 10, 12 |
| Journal of Financial Economics | 4 | 3 | 7, 8, 13 |
| Reserva Federal de los Estados Unidos | 4 | 1 | 1, 2, 3, 7, 9, 11, 14, 16 |
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
| Autoridad Europea de Valores y Mercados (ESMA) | 2 | 2 | 15, 22 |
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
| SWIFT | 2 | 2 | 18 |
| Springer | 2 | 0 | 7, 11 |
| UNCITRAL (Naciones Unidas) | 2 | 1 | 3, 13 |
| 19.ª CIET | 1 | 1 | 6 |
| ACM SIGACT News | 1 | 0 | 19 |
| ACM TOPLAS | 1 | 1 | 19 |
| ACTEX | 1 | 1 | 1, 3, 7 |
| APWG | 1 | 1 | 4 |
| Addison-Wesley | 1 | 1 | 14 |
| American Psychologist | 1 | 1 | 2 |
| Asamblea Legislativa de El Salvador | 1 | 1 | 22 |
| Ashgate | 1 | 0 | 4 |
| BIS Occasional Paper 10 | 1 | 1 | 10, 15, 16 |
| BIS Working Papers | 1 | 1 | 6 |
| Bagehot, W. | 1 | 0 | 6 |
| Banco Central de Reserva de El Salvador | 1 | 1 | 22 |
| Banco Central do Brasil | 1 | 1 | 17 |
| Bank of England Quarterly Bulletin | 1 | 1 | 6 |
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
| FIDA | 1 | 1 | 18 |
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
| OSDI | 1 | 1 | 19 |
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
| Servicio de Impuestos Internos (Chile) | 1 | 1 | 20 |
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
