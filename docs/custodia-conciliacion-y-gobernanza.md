# Custodia, conciliación y gobernanza de activos digitales

Esta guía conecta la contabilidad, la tesorería, el riesgo y el control interno.
No repite gestión de claves ni ciberseguridad: esas materias están en las Partes
19 y 20. Aquí la pregunta es **cómo demuestra una institución que los activos
que afirma custodiar existen, pertenecen al cliente y están disponibles**.

## El sistema mínimo de evidencia

```text
SUBMAYOR DE CLIENTES
opening + inflows − outflows ± trading P/L − fees = closing
        │
        ▼
LEDGER  ↔  BANK  ↔  EXCHANGE  ↔  BLOCKCHAIN
        │
        ▼
activo bruto − no disponible − pasivo cliente = diferencia por activo
```

Cada fuente tiene hora de corte, responsable, evidencia archivada y excepción.
Una diferencia no desaparece porque el total en USD coincida: se investiga por
activo, propiedad, fuente y horizonte.

## Las cuatro naturalezas que deben separarse

| Naturaleza | Qué es | Dónde vive |
|---|---|---|
| Customer balance | Saldo que el submayor atribuye al cliente | Pasivo/obligación de custodia |
| Company asset | Recurso controlado para beneficio propio | Balance de la compañía |
| Custodied asset | Activo mantenido por cuenta del cliente | Registro de custodia y revelaciones aplicables |
| Liability | Obligación de entregar, financiar o restituir | Balance o submayor según los hechos |

```text
activos propios = pasivos propios + patrimonio
activos custodiados disponibles − pasivos de clientes = diferencia de custodia
```

No se netean. La presentación contable exacta requiere analizar contrato,
control, derechos y marco aplicable.

## Reservas y evidencia

| Trabajo | Responde | No reemplaza |
|---|---|---|
| Proof of Assets | Saldo observado | Pasivos, propiedad o disponibilidad |
| Proof of Reserves | Activos designados como respaldo | Auditoría financiera completa |
| Proof of Liabilities | Universo de obligaciones | Existencia de activos |
| Proof of Ownership | Control y titularidad | Liquidez y ausencia de todo gravamen |
| Financial Audit | Opinión bajo alcance y marco definidos | Monitoreo continuo después del corte |

La etiqueta nunca sustituye la lectura del alcance, período, procedimientos,
materialidad, excepciones y conclusión del informe.

## Trading, treasury y liquidez

Spot introduce riesgo de mercado y liquidación. Margin, futures y derivatives
agregan apalancamiento, contraparte, llamadas de margen, colateral inmovilizado y
liquidity gaps. Antes de operar hay que responder:

1. ¿Libro propio o activo de cliente?
2. ¿Existe mandato específico y vigente?
3. ¿Quién absorbe P/L, fees, funding y default?
4. ¿Qué pasivo nace y qué colateral deja de estar disponible?
5. ¿Puede cerrarse la posición bajo estrés sin usar patrimonio segregado?

Treasury mantiene colchones separados para compañía y clientes, y límites por
activo, contraparte, exchange, red, custodio y horizonte.

## Taxonomía común

| Riesgo | Medida mínima |
|---|---|
| Custody | Diferencia disponible por activo |
| Liquidity | Brecha por horizonte, sin netear patrimonios |
| Counterparty | Exposición y colateral por entidad |
| Operational | Excepciones abiertas y antigüedad |
| Market | P/L y pérdida bajo salida forzada |
| Technology | Fuentes sin confirmación alternativa |
| Fraud | Operaciones sin mandato o con evidencia alterada |
| Concentration | Mayor dependencia por activo/proveedor/red |

## Gobernanza

| Rol | Responsabilidad |
|---|---|
| Maker | Prepara la instrucción |
| Checker | Verifica datos y mandato |
| Approver | Decide dentro de límites |
| Executor | Opera en el sistema externo |
| Reconciler | Compara ledger y evidencia externa |
| Auditor | Prueba diseño y funcionamiento |

Ninguna persona concentra dos funciones sobre la misma operación. Una excepción
lleva dueño, causa, importe, antigüedad, evidencia, plazo y aprobación separada.

## Ruta práctica

- [Clase 12 — Custodia de activos digitales](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/12-custodia-de-activos-digitales.md)
- [Clase 15 — Contabilidad, tributación y balance](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/15-contabilidad-tributacion-y-balance.md)
- [Caso Custodia Andina Digital](../case-studies/custody/custodia-andina-digital.md)
- [Laboratorio 9 — Conciliación de custodia](../modules/19-activos-digitales-stablecoins-y-dinero-programable/labs/lab-09.md)
- [`digital_assets_risk_lab`](../apps/digital_assets_risk_lab/README.md)

## Referencias con fecha

- IOSCO (2023), recomendaciones 12–16 de custodia, segregación, conciliación y
  aseguramiento independiente. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- PCAOB Office of the Investor Advocate (2023-03-08), limitaciones de los
  informes de proof of reserves. <https://pcaobus.org/resources/information-for-investors/investor-advisories/investor-advisory-exercise-caution-with-third-party-verification-proof-of-reserve-reports>
- IFRS Interpretations Committee (2019-06), decisión de agenda sobre tenencias
  del subconjunto de criptomonedas analizado. <https://www.ifrs.org/projects/completed-projects/2019/holdings-of-cryptocurrencies/>
- Basel Committee, DIS55, vigente desde 2026-01-01, divulgaciones de exposiciones
  y liquidez de criptoactivos para bancos dentro de su alcance.
  <https://www.bis.org/committees/bcbs/basel-framework/standard/dis/55/inforce/2026-01-01/published/2024-07-17>

**Referencias verificadas el 2026-09-07.** Las fuentes internacionales no se
incorporan automáticamente al derecho local; verifica jurisdicción, actividad y
fecha antes de una decisión real.
