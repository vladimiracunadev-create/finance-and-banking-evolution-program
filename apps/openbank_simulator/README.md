# OpenBank Learning Simulator

MVP educativo de un banco virtual con clientes, cuentas, movimientos, transferencias y préstamos simples.

## Ejecutar

```bash
python apps/openbank_simulator/cli.py demo
python apps/openbank_simulator/cli.py reset
```

Escenario de **crisis digital** (incidente de custodia, pausa de retiros,
reposición y reapertura), sin alterar el comportamiento anterior:

```bash
python apps/openbank_simulator/cli.py crisis
```

El módulo `crisis_digital.py` agrega sus propias tablas (`crisis_reserves`,
`crisis_state`) y opera sobre las cuentas existentes; `bank.py` no cambia.
Materiales: [guía de crisis financiera digital](../../docs/crisis-financiera-digital.md)
y [laboratorio de crisis de custodia](../custody_crisis_lab/README.md).

La base `openbank.db` se crea localmente y está ignorada por Git.

## Limitaciones

- No es software bancario real.
- No usa dinero ni datos reales.
- No implementa requisitos regulatorios, contables o de seguridad completos.
