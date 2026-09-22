# GAMECO: de moneda cerrada a mercado tokenizado

> Caso sintético. No describe una empresa real ni constituye asesoría legal,
> contable, tributaria o de inversión.

## 1. Hechos

GAMECO vende `1.000 GEM = CLP 5.990`. Los usuarios compran skins, Battle Pass y
contenido digital. El caso evoluciona por fases; cada una conserva lo anterior y
añade exactamente un cambio económico principal.

| Fase | Cambio respecto de la anterior | Hecho nuevo |
|---|---|---|
| A | Base | GEM no transferible y sin retiro |
| B | Transferibilidad | Items pasan de Jugador A a Jugador B |
| C | Intermediación | GAMECO abre marketplace P2P y cobra comisión |
| D | Convertibilidad | Sellers pueden retirar CLP mediante payout |
| E | Tokenización | Items se registran como tokens y pueden salir a mercado externo |

Datos sintéticos del periodo:

```text
GEM emitidas                         1.000.000
GEM gastadas                           600.000
GEM pendientes                         400.000
jugadores                               10.000
payer conversion                            5 %
ARPPU                               CLP 12.000
refund rate                                  3 %
chargeback rate                            0,5 %
```

## 2. Actores

- Jugador/comprador: paga y recibe GEM o un entitlement.
- Seller/creador: entrega un activo y, desde la fase D, recibe payout.
- GAMECO: operador del ledger, plataforma y posible intermediario.
- Store, merchant o merchant of record: rol que depende del contrato y país.
- PSP/adquirente: autoriza, procesa y liquida según el flujo acordado.
- Supervisor/autoridad: califica la actividad por sustancia.

## 3. Decisiones por fase

### Fase A — moneda cerrada

GAMECO registra el cobro separado de la obligación comercial. El usuario tiene
derecho de uso, no una afirmación automática de efectivo exigible. La empresa
mide GEM outstanding, refunds, chargebacks, consumo y breakage.

### Fase B — items transferibles

GAMECO añade historial de propiedad, controles de account takeover y robo de
items. Aparece un precio implícito y un mercado gris potencial, aunque no exista
cash-out oficial.

### Fase C — marketplace P2P

GAMECO define seller, buyer, comisión, custodia, reglas de precio, disputas y
settlement del activo. Distingue mercado primario de reventa y vigila wash
trading y manipulación.

### Fase D — payout en CLP

GAMECO separa fondos propios, dinero en tránsito y payable a sellers; introduce
reserva de liquidez, estados de payout, límites, evaluación de contraparte y
análisis AML/KYC potencial. No se concluye automáticamente que sea institución
financiera: se abre la calificación especializada.

### Fase E — tokenización

GAMECO documenta qué derecho acompaña al token, quién custodia claves, qué
registro manda, cómo se reconcilian metadatos y entitlement, qué fees existen y
qué ocurre al salir del entorno controlado. Tokenizar no crea valor ni liquidez.

## 4. Riesgos

| Categoría | A | B | C | D | E |
|---|---:|---:|---:|---:|---:|
| Operacional / ledger | ✓ | ✓ | ✓ | ✓ | ✓ |
| Robo de activo / ATO |  | ✓ | ✓ | ✓ | ✓ |
| Manipulación de mercado |  | potencial | ✓ | ✓ | ✓ |
| Liquidez / payout |  |  |  | ✓ | ✓ |
| AML/KYC potencial |  |  | revisar | ✓ | ✓ |
| Smart contract / claves |  |  |  |  | ✓ |
| Recalificación regulatoria | revisar | revisar | ✓ | ✓ | ✓ |

## 5. Regulación

La revisión no empieza por «es un videojuego», sino por doce preguntas:
transferibilidad, venta, convertibilidad, mercado secundario, saldo mantenido,
custodia, intermediación, payouts, azar, expectativa de rentabilidad, emisión
pública y profesionalidad. Según las respuestas se revisan pagos, stored value,
servicios financieros, activos virtuales, AML/KYC, valores, gambling, consumo e
impuestos.

Para Chile se consultan Ley 21.521, NCG 502, normativa de pagos del Banco
Central, sujetos obligados UAF, criterios SII y protección SERNAC. Una semejanza
técnica no sustituye el análisis legal.

## 6. Controles

- doble entrada para issuance, burn, transferencias, fees y payouts;
- conciliación `Orden ↔ Pago ↔ Settlement ↔ Ledger ↔ Wallet ↔ Entitlement`;
- idempotencia y evidencia de entrega;
- límites y aprobación parental cuando corresponda;
- reserva para refunds, chargebacks y payouts;
- segregación de fondos y funciones;
- monitoreo de concentración, wash trading, bot farming y mule accounts;
- documento de calificación revisado al pasar de fase.

## 7. Resultado calculado

```text
10.000 × 5 % × CLP 12.000 = CLP 6.000.000 gross bookings
```

El importe no es aún ingreso reconocido ni recepción neta. El laboratorio aplica
supuestos explícitos de impuesto incluido, platform fee, payment fee, refunds y
chargebacks. Para las GEM:

```text
1.000.000 emitidas − 600.000 gastadas = 400.000 pendientes
```

La igualdad concilia unidades; no convierte las 400.000 GEM en CLP 400.000.

## 8. Lecciones

1. Una unidad cerrada puede cumplir funciones monetarias internas sin ser dinero
   soberano ni depósito.
2. Transferibilidad, convertibilidad y negociación son saltos distintos.
3. Cash collected, bookings, net receipts y revenue responden preguntas
   diferentes.
4. Cash-out introduce payout, liquidez e intermediación; no entrega por sí solo
   una etiqueta jurídica.
5. Tokenización cambia soporte y custodia, no crea el derecho económico.

## 9. Preguntas

1. ¿Qué debe GAMECO en la fase A y qué evidencia contractual falta?
2. ¿Qué riesgo aparece primero al abrir transferencias sin cash-out?
3. ¿Quién es contraparte en una disputa de la fase C?
4. ¿Qué actividad de la fase D obliga a revisar AML/KYC y pagos?
5. ¿Qué derecho tiene el token de la fase E fuera de GAMECO?

## 10. Fuentes

- [Dossier de economías virtuales](../../docs/economias-virtuales-y-bienes-digitales.md), fuentes oficiales y fecha de verificación 2026-09-22.
- [Ley 21.521, BCN](https://www.bcn.cl/leychile/navegar?idNorma=1187323), texto oficial.
- [NCG 502, CMF](https://cmfchile.cl/portal/normativa/624/w4-article-106882.html), vigente al 2026-09-22.
- [IFRS 15, IFRS Foundation](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/), reconocimiento de ingresos.
