# Caso integrador: Custodia Andina Digital

## Ficha

| Campo | Valor |
|---|---|
| Institución | Custodia Andina Digital S.A. (**ficticia**) |
| Fecha de corte | 2026-09-07, 18:00 UTC |
| Moneda de presentación | USD equivalentes sintéticos |
| Actividad | Custodia, ejecución y tesorería de activos digitales |
| Propósito | Probar existencia, propiedad y disponibilidad sin confundir fondos propios |

Todos los nombres, importes y operaciones son educativos. El caso no representa
a una institución real ni constituye asesoría financiera, contable o legal.

## La pregunta del comité

La institución muestra USD 7 150 000 en banco, exchanges y blockchain frente a
USD 7 000 000 de saldos de clientes. El directorio concluye que hay una cobertura
de 102,14 %. ¿Puede afirmar que todos los activos existen, le pertenecen a los
clientes y estarán disponibles cuando los retiren?

No con esa cifra. Primero hay que separar cinco pruebas:

| Evidencia | Qué responde | Qué no responde |
|---|---|---|
| Proof of Assets | Qué saldos se observan | Quién debe y si están libres |
| Proof of Reserves | Qué activos se designan como reserva | Pasivo completo y disponibilidad futura |
| Proof of Liabilities | Cuánto se debe a clientes | Si existen activos suficientes |
| Proof of Ownership | Quién controla y posee los activos | Si están libres de gravámenes |
| Financial Audit | Estados, controles y evidencia según un marco | Disponibilidad continua después del corte |

## 1. Mayor de obligaciones con clientes

Fuente: [`custody_ledger_synthetic.csv`](../../datasets/synthetic/custody_ledger_synthetic.csv).

```text
opening balance                  6 800 000
+ inflows                        1 000 000
- outflows                        (600 000)
± trading P/L                     (150 000)
± fees                             (50 000)
= closing balance                7 000 000
```

La ecuación cuadra tanto por activo como en total. Eso prueba integridad
aritmética del mayor, **no prueba reservas**.

## 2. Saldos observados fuera del mayor

Fuente: [`custody_positions_synthetic.csv`](../../datasets/synthetic/custody_positions_synthetic.csv).

| Activo | Pasivo cliente | Activo bruto | No disponible | Disponible | Diferencia |
|---|---:|---:|---:|---:|---:|
| BTC | 2 400 000 | 2 400 000 | 200 000 | 2 200 000 | **−200 000** |
| ETH | 1 600 000 | 1 650 000 | 100 000 | 1 550 000 | **−50 000** |
| USDC | 3 000 000 | 3 100 000 | 400 000 | 2 700 000 | **−300 000** |
| **Total** | **7 000 000** | **7 150 000** | **700 000** | **6 450 000** | **−550 000** |

```text
COBERTURA BRUTA       7 150 000 / 7 000 000 = 102,14 %
COBERTURA DISPONIBLE  6 450 000 / 7 000 000 =  92,14 %

EL MISMO CORTE PERMITE DOS TITULARES:
  «hay más activos que pasivos»       cierto en bruto
  «faltan USD 550 000 disponibles»    cierto para retiros
```

El tramo pignorado en margin y el tramo congelado existen, pero no están a libre
disposición. Además, una captura de pantalla del exchange no prueba propiedad;
una dirección en cadena no prueba por sí sola quién controla su clave ni si hay
un acuerdo fuera de cadena que la grava.

## 3. Balance de la compañía y patrimonio segregado

| Balance propio de la compañía | USD |
|---|---:|
| Efectivo y equivalentes propios | 1 200 000 |
| Activos digitales propios | 400 000 |
| Cuentas por cobrar | 200 000 |
| **Activos propios** | **1 800 000** |
| Préstamo | (600 000) |
| Pasivo por trading y derivados | (350 000) |
| Restitución por operaciones no autorizadas | (250 000) |
| Proveedores y otros | (150 000) |
| **Pasivos propios** | **(1 350 000)** |
| **Patrimonio** | **450 000** |

Los USD 6 450 000 disponibles de clientes se presentan en el registro de
custodia y se concilian, pero **no son activos propios de la compañía**. El saldo
del cliente es una obligación del registro auxiliar; el activo custodiado es
propiedad del cliente si el contrato y el régimen de segregación así lo sostienen;
el pasivo propio nace cuando la compañía debe restituir una pérdida, financiar
una posición o pagar a una contraparte.

## 4. Trading y riesgos que introduce

Fuente: [`custody_trading_synthetic.csv`](../../datasets/synthetic/custody_trading_synthetic.csv).

| Instrumento | Libro | Nocional | P/L | Pasivo creado | Colateral inmovilizado | Riesgo incremental |
|---|---|---:|---:|---:|---:|---|
| Spot | Clientes, sin mandato | 800 000 | −50 000 | 0 | 0 | Mercado, custodia, operacional, fraude |
| Margin | Clientes, sin mandato | 1 200 000 | −100 000 | 150 000 | 400 000 | Los anteriores + contraparte, apalancamiento, liquidez |
| Futures | Propio | 900 000 | −180 000 | 250 000 | 250 000 | Mercado, contraparte, liquidez |
| Derivatives | Propio | 700 000 | +30 000 | 100 000 | 100 000 | Mercado, contraparte, liquidez |
| **Total** | | **3 600 000** | **−300 000** | **500 000** | **750 000** | |

Una operación spot puede generar pérdida sin apalancamiento. Margin, futures y
derivatives pueden exigir colateral adicional antes de realizar la pérdida,
crear pasivos y abrir una brecha de liquidez. Si se usan activos custodiados sin
mandato, la pérdida de mercado se convierte además en riesgo de custodia y
fraude, con una obligación de restitución para la compañía.

## 5. Liquidez

| Universo que no se netea | Recursos 24 h | Salidas 24 h | Brecha |
|---|---:|---:|---:|
| Clientes | 6 450 000 | 6 800 000 | **350 000** |
| Compañía | 1 200 000 | 1 400 000 | **200 000** |

La compañía no puede cubrir su brecha con activos segregados. Tampoco puede
resolver un faltante de BTC entregando USDC sin consentimiento, mercado,
liquidez y coste de conversión. La liquidez se mide por activo, fuente y
horizonte, no solo en un total valorizado.

## 6. Riesgos del caso

| Riesgo | Exposición observable | Decisión de control |
|---|---:|---|
| Custody risk | Déficit disponible de 550 000 | Suspender reutilización y reponer por activo |
| Liquidity risk | Brecha de clientes 350 000; propia 200 000 | Dos colchones, nunca neteados |
| Counterparty risk | 1 600 000 nocionales apalancados | Límites por exchange y cámara |
| Market risk | P/L total −300 000 | VaR/estrés y stop de libro propio |
| Operational risk | Fuentes y cortes distintos | Conciliación diaria con gestión de excepciones |
| Technology risk | Dependencia de nodo, API y exchange | Fuente alterna y evidencia archivada |
| Fraud risk | 2 operaciones sin mandato | Bloqueo, investigación y restitución |
| Concentration risk | 1 550 000 brutos en un exchange | Límite por contraparte y ruta de salida |

## 7. Control interno

| Rol | Persona ficticia | Función | No puede |
|---|---|---|---|
| Maker | Ana | Prepara instrucción | Aprobarla ni ejecutarla |
| Checker | Bruno | Verifica datos y mandato | Cambiar la instrucción |
| Approver | Carla | Autoriza dentro de límites | Firmar técnicamente |
| Executor | Diego | Ejecuta en banco/exchange/cadena | Conciliar su propia ejecución |
| Reconciler | Elena | Compara las cuatro fuentes | Alterar origen o evidencia |
| Auditor | Fátima | Prueba diseño y operación | Operar el control |

Ninguna persona ocupa dos filas. Toda excepción conserva evidencia, responsable,
hora, causa, resolución y aprobación independiente.

## Preguntas para el estudiante

1. Calcula activos propios, pasivos propios y patrimonio sin incluir custodia.
2. Reconstruye el closing balance y explica qué prueba ese cierre.
3. Calcula cobertura bruta y disponible total y por activo.
4. Identifica la diferencia de USD 550 000 y separa congelado de pignorado.
5. Calcula nocional, P/L, pasivos y colateral de trading por libro.
6. Determina las dos brechas de liquidez y explica por qué no se netean.
7. Prioriza los ocho riesgos y propone límite, indicador, frecuencia y disparador.
8. Decide si se aceptan depósitos y retiros, se restringen o se suspenden.

## Decisión de referencia

Suspender trading con activos de clientes y nuevas operaciones apalancadas;
mantener retiros hasta el saldo inequívocamente disponible por activo con regla
justa y documentada; aportar activos propios libres para restituir el déficit;
obtener prueba de control y ausencia de gravámenes; ejecutar conciliación diaria;
y escalar fraude, incumplimiento contractual y suficiencia patrimonial a asesoría
legal, auditoría y autoridad competente según la jurisdicción.

## Fuentes y vigencia

- IOSCO (2023). *Policy Recommendations for Crypto and Digital Asset Markets*.
  Recomendaciones 12–16 sobre custodia, segregación, conciliación y aseguramiento
  independiente. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- PCAOB Office of the Investor Advocate (2023-03-08). *Exercise Caution With
  Third-Party Verification/Proof of Reserve Reports*. Delimita lo que un PoR no
  prueba. <https://pcaobus.org/resources/information-for-investors/investor-advisories/investor-advisory-exercise-caution-with-third-party-verification-proof-of-reserve-reports>
- IFRS Interpretations Committee (2019-06). *Holdings of Cryptocurrencies*.
  Distingue IAS 2 e IAS 38 para el subconjunto analizado; no resuelve por sí sola
  la contabilidad de la custodia. <https://www.ifrs.org/projects/completed-projects/2019/holdings-of-cryptocurrencies/>
- Basel Committee on Banking Supervision. *DIS55 Cryptoasset exposures*, vigente
  desde 2026-01-01. Exige divulgación de clasificación, exposición y liquidez
  para bancos dentro de su alcance. <https://www.bis.org/committees/bcbs/basel-framework/standard/dis/55/inforce/2026-01-01/published/2024-07-17>

**Referencias verificadas el 2026-09-07.** El tratamiento aplicable depende de
la jurisdicción, el contrato y los hechos; debe revisarse en la fuente vigente.
