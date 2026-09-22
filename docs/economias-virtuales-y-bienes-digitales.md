# Economías virtuales y bienes digitales como sistemas financieros

Este documento usa videojuegos como **laboratorio de representación de valor**.
No enseña a desarrollar juegos, no recomienda inversiones y no convierte toda
moneda virtual en dinero ni todo token en instrumento financiero. La pregunta
rectora es:

> **¿Qué es económicamente una moneda o activo de videojuego y en qué momento
> deja de ser solamente una unidad interna de software?**

La respuesta depende de la función, los derechos, la transferibilidad, la
convertibilidad, la aceptación, la custodia, el mercado, el emisor, la
intermediación y el régimen aplicable. El soporte técnico no basta.

## 1. El modelo mental

```text
Representación digital de valor
            │
            ├── Cerrada
            │     └── sólo dentro del sistema
            │
            ├── Transferible
            │     └── usuario ↔ usuario
            │
            ├── Convertible
            │     └── activo virtual ↔ dinero
            │
            └── Negociable
                  └── mercado y precio externo
```

Cada salto aumenta potencialmente liquidez, riesgo, fraude, complejidad
contable, obligaciones y exposición regulatoria. «Potencialmente» importa: el
salto abre preguntas; no resuelve la calificación.

## 2. Taxonomía comparativa por sustancia

La tabla es una guía de investigación. «Puede» significa que hay que leer el
contrato y la jurisdicción, no que el rasgo exista siempre.

| Representación | Emisor / registro | Qué representa y quién debe | Uso / transferencia / conversión | Rentabilidad y riesgo |
|---|---|---|---|---|
| Dinero soberano / efectivo | Estado o banco central; posesión o registro oficial | Unidad monetaria; obligación según su forma | Aceptación amplia; transferible | No promete rentabilidad; riesgo soberano y operacional |
| Depósito bancario | Banco; core bancario | Deuda monetaria del banco al depositante | Pagable, transferible y redimible según contrato | Contraparte bancaria; puede remunerar |
| Dinero electrónico / prepaid value | Emisor autorizado; ledger del emisor | Valor monetario recibido contra fondos, con derecho definido | Aceptación y reembolso dependen del régimen | Riesgo del emisor, salvaguarda y operación |
| Stored value / gift card | Comercio o emisor; ledger o soporte | Derecho a bienes/servicios o, en algunos diseños, obligación monetaria | Suele limitarse a una red; reembolso variable | Breakage, insolvencia y condiciones de expiración |
| Puntos de fidelización / cupones | Comercio o programa | Descuento, premio o derecho promocional | Cerrado, limitado y normalmente no convertible | Devaluación contractual y caducidad |
| Crédito comercial / saldo de plataforma | Plataforma | Derecho contra el comercio o acceso futuro | Puede ser reembolsable o no; puede cubrir terceros | Contraparte y clasificación contractual |
| Moneda virtual cerrada / premium currency | Operador; ledger del juego | Unidad de precio y acceso interno, no necesariamente efectivo exigible | Solo dentro del sistema; sin cash-out | Cambio de reglas, revocación, fraude y continuidad |
| Moneda parcialmente transferible | Operador / marketplace | Lo anterior más capacidad de mover valor entre usuarios | P2P interno; sin conversión oficial | Custodia, robo, mercado gris y concentración |
| Moneda virtual convertible | Operador o red; uno o varios ledgers | Derecho interno más canal de conversión | Cash-in y cash-out según reglas | Liquidez, payout, AML/KYC potencial y contraparte |
| Activo de videojuego / bien digital | Operador o creador; inventario | Entitlement de uso, licencia o derecho contractual | Transferencia y venta dependen del contrato | Precio, escasez diseñada, custodia y fraude |
| NFT | Emisor/contrato; blockchain y metadatos | Token único; los derechos externos se leen aparte | Técnicamente transferible si no está restringido | Mercado, claves, contrato y vínculo con el contenido |
| Token fungible / criptoactivo | Emisor o protocolo; DLT | Promesa, utilidad o ninguna obligación identificable | Puede negociarse externamente | Volatilidad, custodia, protocolo y emisor |
| Stablecoin | Emisor o mecanismo; DLT + registros externos | Referencia de valor y posible derecho de redención | Transferible y normalmente convertible | Reserva, redención, liquidez y pérdida de paridad |
| Instrumento financiero | Emisor/intermediario; registro aplicable | Deuda, participación, derivado u otro derecho financiero | Transferencia según régimen de mercado | Retorno esperado, disclosure, idoneidad y mercado |

La pregunta de control es siempre: **¿quién está obligado a hacer qué, frente a
quién y bajo qué condiciones?** Un nombre comercial como «gold», «coin» o
«token» no responde nada de eso.

## 3. Tres niveles de GEM

GAMECO vende `1.000 GEM = CLP 5.990`.

| Dimensión | Nivel A | Nivel B | Nivel C |
|---|---|---|---|
| Flujo | `CLP → GEM → bienes internos` | Nivel A + `Jugador A → activo → Jugador B` | Nivel B + `activo → CLP/USD` |
| Naturaleza económica inicial | Unidad interna / entitlement | Valor transferible de plataforma | Valor convertible con canal monetario |
| Contraparte | Operador por la prestación prometida | Operador y contraparte usuaria | Operador, marketplace, PSP y seller/buyer |
| Liquidez | No hay salida monetaria | Hay intercambio, no cash-out oficial | Depende de profundidad, límites y payout |
| Custodia | Cuenta e inventario del operador | Ledger e inventario por usuario | Ledger, fondos, escrow y cuentas de payout |
| Fraude | Compra no autorizada, duplicación | Lo anterior + robo, farming y manipulación | Lo anterior + mule accounts, chargeback y lavado potencial |
| Balance | Cobro frente a obligación comercial | Añade comisión y saldos de terceros | Añade payable a sellers, reservas y settlement |
| Regulación potencial | Consumo, contrato, impuesto | Añade marketplace, datos e intermediación | Exige revisar pagos, AML/KYC, activos virtuales y servicios financieros |

Cash-out no convierte automáticamente a GAMECO en institución financiera. Sí
cambia el hecho económico: aparece una obligación de pago, un canal de liquidez,
settlement y una actividad que debe calificarse con asesoría especializada.

## 4. Emisión, fuentes, sumideros e inflación

```text
Faucets / Sources
        ↓
Moneda circulante
        ↓
Transferencia / gasto
        ↓
Sinks
```

```text
MISIONES → +100 GOLD
TIENDA   →  -60 GOLD
NETO     →  +40 GOLD
```

Si el patrón se repite masivamente, el stock aumenta. Puede existir inflación
de precios internos aunque GOLD no sea moneda de curso legal: la inflación es
un fenómeno de poder de compra dentro del sistema, no una etiqueta jurídica.

Métricas mínimas:

```text
stock final       = stock inicial + issuance − burn
sinks/sources     = unidades destruidas / unidades creadas
velocity          = transferencias del periodo / stock medio
concentration     = saldo del grupo superior / saldo total
```

El paralelo monetario tiene límite. GAMECO puede alterar reglas, precios,
recompensas y acceso; no tiene la soberanía, mandato macroeconómico ni estructura
institucional del peso chileno. Una stablecoin privada añade una promesa de
referencia o redención que GEM puede no tener.

## 5. ¿Qué debe el operador?

Comprar `1.000 GEM` por `CLP 5.990` no crea necesariamente un depósito por
CLP 5.990. Según el contrato, puede crear:

- derecho a usar unidades en un catálogo;
- derecho a recibir contenido digital o servicio futuro;
- entitlement revocable o sujeto a licencia;
- crédito de plataforma no reembolsable;
- saldo reembolsable, si el contrato o la ley lo exige;
- obligación de estar disponible para cumplir una prestación.

Hay que separar la unidad del precio pagado. `400.000 GEM pendientes` no son
`CLP 400.000`, ni necesariamente el valor monetario de un pasivo exigible. Para
medir la obligación se necesita el contrato, la asignación del precio de la
transacción, el patrón de uso, la reembolsabilidad y las obligaciones de
desempeño.

## 6. Cobro, bookings, recepción neta e ingreso

```text
Cobro bruto / gross bookings
− impuestos cuando correspondan
− comisión de plataforma
− comisión de procesamiento
− refunds
− chargebacks
= recepción neta de caja
```

La recepción neta tampoco es automáticamente ingreso reconocido. NIIF 15 exige
identificar el contrato, las promesas, el precio de la transacción, su asignación
y el momento en que se satisface cada obligación de desempeño. En acuerdos con
plataformas también se analiza si GAMECO actúa como principal o agente.

Ejemplo pedagógico — no asiento universal:

```text
Jugador paga                              CLP 5.990
GEM entregadas                                1.000
GEM gastadas                                    600
Proporción ejercida                              60 %
```

Si el contrato atribuye todo el cobro al derecho futuro y el patrón de consumo
es una aproximación válida, el ejercicio permite ilustrar `60 % × 5.990 = CLP
3.594` cumplidos y `CLP 2.396` pendientes antes de analizar breakage. El asiento
real puede cambiar por impuestos, comisión, múltiples promesas, principal/agente,
refunds, jurisdicción y términos contractuales.

### Breakage

Si se vendieron 100 millones GEM y 15 millones nunca se usan, esos 15 millones
son derechos no ejercidos, no ingreso automático. La estimación requiere datos,
actualización y coherencia con el contrato. Cuando la entidad espera tener
derecho al breakage, NIIF 15 contempla reconocerlo en proporción al patrón de
ejercicio; si no, el análisis espera hasta que sea remoto que el cliente ejerza
los derechos restantes. Si la obligación es financiera o existe norma de bienes
no reclamados, el análisis puede ser distinto.

## 7. Marketplace P2P y flujo de fondos

```text
Jugador A → activo digital → Marketplace → Jugador B
```

Sin dinero real ya hay mercado primario, posible mercado secundario, precio,
spread, escasez, concentración, custodia y manipulación. Con dinero real:

```text
Buyer
  │ dinero
  ▼
Marketplace ── comisión
  │ escrow / settlement
  ▼
Seller
```

Preguntas de control:

1. ¿Quién recibe primero el dinero y en qué cuenta?
2. ¿Quién mantiene saldo o custodia el activo?
3. ¿Quién debe pagar a quién y cuándo el pago es final?
4. ¿Quién absorbe refund, chargeback y disputa?
5. ¿Qué ocurre si falla el payout?

Seller, merchant, merchant of record, marketplace, PSP, acquirer, platform,
developer y publisher pueden coincidir o separarse. El contrato y la
jurisdicción mandan. La documentación oficial de Apple, Google Play o Steam no
autoriza a asumir que todas cumplen el mismo rol en todo país o modalidad.

## 8. Modelos de negocio y unit economics

| Modelo | Ingreso y payer | Obligación pendiente / riesgo principal |
|---|---|---|
| Premium game | Precio inicial pagado por jugador | Entrega, soporte, refunds |
| Free-to-play / freemium | Microtransactions de pagadores | Saldos, contenido, conducta y concentración |
| Suscripción | Cargo recurrente | Servicio continuo, churn y renovación |
| DLC / Battle Pass | Venta de contenido o acceso temporal | Entrega, expiración y progreso prometido |
| Advertising-supported | Anunciante paga por audiencia | Medición, privacidad y dependencia del intermediario |
| Marketplace P2P | Take rate sobre comprador/vendedor | Escrow, payout, fraude y disputas |
| Creator marketplace | Venta y reparto con creador | Payable, propiedad intelectual, impuestos |
| Play-and-earn | Emisión/recompensas y actividad de usuarios | Sostenibilidad, liquidez y expectativa de retorno |
| Blockchain gaming | Venta/fee/token/mercado | Custodia, smart contract, mercado externo y regulación |

Métricas financieras: ARPU, ARPPU, payer conversion, LTV, CAC, gross margin,
platform fee, payment fee, refund rate, chargeback rate y marketplace take rate.
Métricas de producto: retención, churn, actividad y cohortes. Se relacionan, pero
no se sustituyen.

Ejercicio:

```text
10.000 jugadores × 5 % pagadores × CLP 12.000 ARPPU
= CLP 6.000.000 gross bookings
```

Luego se descuentan, bajo supuestos declarados, impuesto incluido, fee de
plataforma, fee de procesamiento, refunds y chargebacks. El laboratorio
[`gameco`](../modules/19-activos-digitales-stablecoins-y-dinero-programable/labs/lab-10.md)
calcula el puente reproducible.

## 9. Conciliación y riesgos

```text
Orden ↔ Pago ↔ Settlement ↔ Ledger interno ↔ Wallet ↔ Entitlement
```

```text
PSP:          PAID
Game Ledger:  NOT CREDITED
Inventory:    EMPTY
```

No es un problema meramente visual: hay dinero cobrado, prestación no entregada,
posible refund/chargeback y una diferencia que necesita dueño, plazo y
resolución.

| Riesgo | Ejemplos | Controles financieros y operacionales |
|---|---|---|
| Operacional | bugs, duplicación, downtime | idempotencia, doble entrada, conciliación |
| Fraude | tarjeta robada, refund abuse, ATO, bots | autenticación, velocity rules, revisión y reservas |
| Liquidez | payouts y cash-out | escalera, reserva, límites y stress |
| Contraparte | plataforma, PSP, seller | límites, segregación, alternativas y seguimiento |
| Tecnológico | ledger, wallet, smart contract | integridad, auditoría, recuperación y pruebas |
| Regulatorio | recalificación | inventario de actividades y revisión con fecha |
| Reputacional | menores, pérdida de activos | límites, transparencia, soporte y remediación |

El fraude se estudia por pérdida y control: stolen payment instruments, refund
abuse, chargebacks, account takeover, bot farming, item theft, wash trading,
mule accounts y manipulación. Este material no enseña técnicas ofensivas.

## 10. Loot boxes, menores y expectativa de rentabilidad

```text
Pago + resultado aleatorio + premio
                    + transferibilidad
                    + convertibilidad
```

Cada componente puede modificar el análisis de consumo, juego de azar, pagos,
mercado y AML. No toda loot box es automáticamente gambling y tampoco existe
una exclusión universal. En menores importan precios comprensibles, conversión
a dinero visible, aprobación parental, límites, compras accidentales, refunds y
diseño comercial no manipulativo.

También se separa:

```text
comprar item para jugar
≠
comprar activo esperando rentabilidad
```

La segunda narrativa puede cambiar marketing, disclosure, idoneidad y análisis
de instrumentos financieros. El programa no recomienda inversiones.

## 11. Base de datos, NFT y token fungible

| Pregunta | Item en DB | NFT | Premium currency | Token fungible |
|---|---|---|---|---|
| Registro | Operador | Blockchain + metadatos | Ledger del operador | Blockchain u otro ledger |
| Transferencia | Contractual/técnica | Técnica, salvo restricción | Normalmente interna | Frecuentemente técnica |
| Custodia | Cuenta del usuario | Clave/custodio | Cuenta del usuario | Clave/custodio |
| Derecho | Contrato/licencia | Contrato + token | Uso del catálogo | Depende del emisor/protocolo |
| Mercado externo | Si se permite | Posible | Inusual | Posible |
| Riesgo extra | Operador | claves, fees, contrato | cambio de reglas | mercado, protocolo y emisor |

Tokenizar no crea valor, propiedad sobre el contenido, liquidez ni protección
jurídica por sí mismo.

## 12. Árbol de análisis regulatorio

```text
¿Transferible? ─no─► consumo, contrato, impuestos, datos
      │ sí
      ▼
¿Puede venderse o hay mercado secundario? ─► conducta, marketplace, fraude
      │
¿Convertible a dinero / payout? ─► pagos, stored value, AML/KYC, liquidez
      │
¿Operador mantiene saldo o custodia? ─► salvaguarda, custodia, conciliación
      │
¿Intermedia profesionalmente? ─► autorización y servicios financieros
      │
¿Azar? ─► análisis de gambling + consumidor, sin conclusión automática
      │
¿Expectativa de rentabilidad o emisión pública? ─► valores/instrumentos
```

La revisión completa pregunta además por aceptación, emisor, derechos, mercado,
tributación, menores y jurisdicción.

### Chile — método, no conclusión automática

Verificado el **2026-09-22**:

- La Ley 21.521 define instrumentos y servicios financieros por su finalidad y
  actividad, no por usar tokens. La NCG 502 regula registro, autorización y
  obligaciones de prestadores profesionales incluidos en esa ley.
- La normativa del Banco Central sobre tarjetas con provisión de fondos exige
  analizar si existe una cuenta de provisión, obligación monetaria frente al
  público o comercios afiliados y derecho de reembolso; una GEM cerrada no se
  equipara por su sola apariencia.
- Si hay intermediación, custodia, sistemas alternativos de transacción,
  payouts o activos financieros virtuales, se revisan CMF, UAF, Banco Central,
  SII y SERNAC según la actividad.
- AML/KYC, tributación y protección del consumidor se determinan sobre hechos y
  sujetos obligados. Este material no es asesoría jurídica ni tributaria.

## 13. Balance económico conceptual de GAMECO

```text
GEM emitidas       1.000.000
GEM gastadas         600.000
GEM pendientes       400.000
```

Esto describe unidades del ledger. No demuestra que las 400.000 GEM sean CLP,
un depósito, un pasivo financiero ni ingreso diferido por igual importe. Sí
indica una población de derechos o posibilidades de uso pendientes que debe
conciliarse con contratos, cash collected, reembolsos y obligaciones de
desempeño.

Las comparaciones con depósitos, prepaid cards, wallets, e-money, settlement
accounts, custodial accounts y securities accounts son operacionales. No son
equivalencias jurídicas.

## 14. Límites y repositorios relacionados

Aquí se estudia **qué representa el valor y cómo se comporta financieramente**.
Quedan fuera Godot, Unity, Unreal, gameplay programming, anti-cheat, explotación
de vulnerabilidades y smart contracts en profundidad.

- desarrollo de videojuegos → `modern-gamedev-program`;
- ingeniería de pagos → `universal-payments-engineering-lab`;
- comercio → `commerce-operating-system`;
- blockchain → `blockchain-learning-path`;
- seguridad → `modern-cybersecurity-program`;
- diagnóstico blockchain → `rootcause-blockchain-security`;
- empresa en Chile → `modern-business-creation-program`.

## Fuentes verificadas

- IFRS Foundation, [IFRS 15 Revenue from Contracts with Customers](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/), obligaciones de desempeño e ingreso. Consulta: 2026-09-22.
- FATF, [Updated Guidance for a Risk-Based Approach to Virtual Assets and VASPs](https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-rba-virtual-assets-2021.html), perímetro de activos virtuales y sistemas cerrados. Consulta: 2026-09-22.
- Biblioteca del Congreso Nacional, [Ley 21.521](https://www.bcn.cl/leychile/navegar?idNorma=1187323), Ley Fintec de Chile. Consulta: 2026-09-22.
- CMF, [NCG 502](https://cmfchile.cl/portal/normativa/624/w4-article-106882.html), prestadores de servicios financieros Fintec. Consulta: 2026-09-22.
- Banco Central de Chile, [sistemas de pagos](https://www.bcentral.cl/areas/sistemas-de-pagos), normativa de tarjetas y provisión de fondos. Consulta: 2026-09-22.
- Apple, [In-App Purchase](https://developer.apple.com/in-app-purchase/), procesamiento y obligaciones comerciales de plataforma. Consulta: 2026-09-22.
- Google Play, [Payments policy](https://support.google.com/googleplay/android-developer/answer/9858738), bienes digitales y monedas virtuales. Consulta: 2026-09-22.
- Steamworks, [Taxes FAQ](https://partner.steamgames.com/doc/finance/taxfaq), gross revenue, ajustes, chargebacks, impuestos y net revenue. Consulta: 2026-09-22.
- OECD, [Children in the Digital Environment](https://one.oecd.org/document/DSTI/CDEP/DGP%282020%293/FINAL/en/pdf), microtransactions, monedas virtuales y comprensión del precio. Consulta: 2026-09-22.

**Caso transversal:** [GAMECO](../case-studies/virtual-economies/gameco.md) ·
**Laboratorio:** [simulación de GAMECO](../modules/19-activos-digitales-stablecoins-y-dinero-programable/labs/lab-10.md) ·
**Mapa:** [activos digitales](mapa-activos-digitales.md)
