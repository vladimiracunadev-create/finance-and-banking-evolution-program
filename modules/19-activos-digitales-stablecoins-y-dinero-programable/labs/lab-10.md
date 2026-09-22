# Laboratorio 10: GAMECO, de unidad cerrada a cash-out

## Propósito

Determinar cuándo una GEM deja de ser solo una unidad interna de software,
cuantificar su economía y conciliar el flujo comercial sin confundir cobro con
ingreso.

## Caso y datos

Trabaja con [GAMECO](../../../case-studies/virtual-economies/gameco.md) y el
módulo `virtual_economy.py`. Todos los datos son ficticios.

## Secuencia obligatoria

1. Clasifica las fases A, B y C por derechos, transferencia, conversión y mercado.
2. Calcula stock final, emisión neta, sinks/sources, velocidad y concentración.
3. Explica si una subida de precios internos sería inflación y dónde acaba la analogía.
4. Calcula pagadores y gross bookings para 10.000 jugadores, 5 % y CLP 12.000.
5. Declara supuestos de impuesto, platform fee, processing fee, refunds y chargebacks.
6. Construye el puente hasta net receipts; no lo llames revenue.
7. Para 1.000 GEM por CLP 5.990, separa cobro, cumplimiento y saldo pendiente.
8. Simula 15 % de breakage y explica por qué no es ingreso inmediato universal.
9. Concilia un pago `PAID` con ledger `NOT CREDITED` e inventory `EMPTY`.
10. Completa la matriz de riesgos y el árbol regulatorio para fases A–E.

## Ejecución

```bash
python apps/digital_assets_risk_lab/cli.py gameco
```

```bash
python -m pytest tests/test_digital_assets_risk_lab.py -q -k "gameco or sources or bookings or breakage or pagado"
```

## Entregables

- ficha comparativa de fases A–E;
- estado de stock y flujo de GEM;
- waterfall de bookings a net receipts;
- roll-forward de obligación comercial y breakage;
- conciliación con excepción, dueño, plazo y remediación;
- memo regulatorio de dos páginas que diga qué debe revisarse, sin concluir por analogía.

## Criterios de aceptación

| Criterio | Evidencia |
|---|---|
| No llama dinero a toda GEM | Clasificación por función y derecho |
| Stock y flujo cuadran | Ecuaciones reproducibles |
| Bookings, caja e ingreso se separan | Waterfall y nota NIIF 15 |
| Breakage conserva incertidumbre | Supuesto y patrón de ejercicio |
| Cash-out cambia el análisis | Payout, liquidez y AML/KYC potencial |
| Conciliación llega al entitlement | Seis estados y una excepción |
| No hay asesoría jurídica | Preguntas de perímetro, no veredictos |

## Solución de referencia

En [`solutions/lab-10.md`](../solutions/lab-10.md).
