# Laboratorio 9: existencia, disponibilidad y conciliación de custodia

## Propósito

Responder con evidencia a la pregunta: **¿los activos que la institución afirma
custodiar existen, pertenecen a quien dice y están disponibles?**

## Caso y datos

Trabaja con [Custodia Andina Digital](../../../case-studies/custody/custodia-andina-digital.md)
y sus tres datasets sintéticos:

- [`custody_ledger_synthetic.csv`](../../../datasets/synthetic/custody_ledger_synthetic.csv);
- [`custody_positions_synthetic.csv`](../../../datasets/synthetic/custody_positions_synthetic.csv);
- [`custody_trading_synthetic.csv`](../../../datasets/synthetic/custody_trading_synthetic.csv).

## Secuencia obligatoria

```text
Ledger  ↕  Bank  ↕  Exchange  ↕  Blockchain
   │          evidencia externa          │
   └──── excepciones con dueño y plazo ──┘
```

1. Recalcula `opening + inflows − outflows ± trading P/L − fees = closing` por
   activo y total. No continúes si el mayor no cuadra.
2. Obtén confirmación bancaria a la hora de corte y separa saldo propio de saldo
   segregado.
3. Obtén del exchange saldo, propiedad de la cuenta, retiros pendientes,
   gravámenes, margin y activos congelados.
4. Verifica saldos de blockchain y prueba control/propiedad por un procedimiento
   autorizado; una dirección observada no basta.
5. Compara pasivo de clientes contra activo bruto y activo disponible por activo.
6. Construye dos balances: compañía y custodia. No los netees.
7. Agrega spot, margin, futures y derivatives; calcula P/L, pasivo creado,
   colateral inmovilizado y exposición nocional.
8. Calcula brecha de liquidez de clientes y compañía en 24 horas, separadas.
9. Clasifica custody, liquidity, counterparty, operational, market, technology,
   fraud y concentration risk.
10. Asigna Maker, Checker, Approver, Executor, Reconciler y Auditor a seis
    personas distintas.
11. Explica qué aporta y qué omite cada prueba: Assets, Reserves, Liabilities,
    Ownership y Financial Audit.
12. Formula una decisión: continuar, restringir o suspender, con umbral y salida.

## Criterios de aceptación

| Criterio | Evidencia |
|---|---|
| El roll-forward cuadra por activo | Hoja de conciliación |
| Bruto y disponible no se confunden | Dos ratios y diferencia |
| No hay neteo entre compañía y clientes | Dos balances y dos brechas |
| Trading se atribuye al libro correcto | Tabla por operación |
| Cada riesgo tiene control | Matriz de ocho riesgos |
| Ninguna persona concentra funciones | Matriz de seis roles |
| La decisión tiene disparadores | Memo de máximo dos páginas |

## Ejecución

```bash
python apps/digital_assets_risk_lab/cli.py reconcile
```

```bash
python -m pytest tests/test_digital_assets_risk_lab.py -q -k "ledger or proof_of_assets or liquidez_de_clientes or persona"
```

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Conciliación y trazabilidad de las cuatro fuentes | 25 |
| Activos, pasivos, patrimonio y segregación | 20 |
| Reservas brutas/disponibles y diferencias | 20 |
| Trading, pérdidas, pasivos y liquidez | 15 |
| Riesgos, controles y separación de funciones | 15 |
| Decisión defendible | 5 |

## Solución de referencia

En [`solutions/lab-09.md`](../solutions/lab-09.md).
